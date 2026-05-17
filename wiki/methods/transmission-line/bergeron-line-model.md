---
title: "Bergeron 线路模型 (Bergeron Line Model)"
type: method
tags: [bergeron, line-model, traveling-wave, lossless-line, distributed-parameter, norton-equivalent, characteristic-line]
created: "2026-05-02"
updated: "2026-05-17"
---

# Bergeron 线路模型 (Bergeron Line Model)

## 定义与边界

Bergeron 线路模型是在 EMT 中用端口历史量表示传输线行波传播的一类时域模型。它把一段均匀线路等效为端口特性导纳和延时历史电流源，使线路两端在当前时间步只通过已知延时量相互耦合。

设均匀传输线长度为 $\ell$，单位长度电感 $L$（H/m）、电容 $C$（F/m）、电阻 $R$（Ω/m）、电导 $G$（S/m）。电报方程为：

$$\frac{\partial v}{\partial x} = -L\frac{\partial i}{\partial t} - Ri, \quad \frac{\partial i}{\partial x} = -C\frac{\partial v}{\partial t} - Gv$$

定义特性阻抗 $Z_c = \sqrt{(R+sL)/(G+sC)}$ 和传播常数 $\gamma = \sqrt{(R+sL)(G+sC)}$。在低损耗近似（$R\ll \omega L,\ G\ll \omega C$）下，$Z_c \approx \sqrt{L/C}$（实数），$\gamma \approx s\sqrt{LC}$（纯虚数），此时行波以速度 $u = 1/\sqrt{LC}$ 传播，无衰减。

**本页面讨论的是线路元件的特征线/行波时域实现**。它不等同于完整的 [[distributed-parameter-line]] 理论（后者涵盖频变参数、有损大地、非均匀几何），也不自动包含频率相关导体损耗、大地返回路径或非换位耦合——这些内容需要与 [[frequency-dependent-line-model]]、[[earth-return-impedance]] 和 [[frequency-dependent-soil]] 连接。Bergeron 模型是这些高级模型的**结构参照框架**。

## EMT 中的作用

Bergeron 模型在 EMT 中主要用于下列任务：

- **保留行波传播特性**：有限传播速度、端点反射、故障行波到达时间
- **提供线性时不变的端口等效**：在节点导纳方程中把线路表示为固定导纳 $Y_c = 1/Z_c$ 加历史电流源，使每个时间步的网络求解仍是线性代数问题
- **作为其他模型的结构基础**：为 [[universal-line-model]]（相域频变 Bergeron 扩展）、[[frequency-dependent-line-model]]（Marti 模型）和 [[folded-line-equivalent]]（节点导纳组织形式）提供统一的时域接口框架
- **长线路和架空线的实时仿真**：延时 $\tau = \ell/u$ 通常为数毫秒至数十毫秒，延时队列实现简单，适合 FPGA/GPU 实时仿真

其核心价值在于把空间分布的偏微分方程转成**端口延时关系**——每个时间步只需存储长度为 $\tau$ 的电压/电流历史队列。若研究问题对频变衰减、土壤参数、护套耦合或非换位强耦合敏感，单纯常参数 Bergeron 表示应视为近似。

## 核心机制

### 2.1 无损单相线路的行波解

无损单相线路（$R=0,\ G=0$）的电报方程退化为：

$$-\frac{\partial v}{\partial x}=L\frac{\partial i}{\partial t}, \quad -\frac{\partial i}{\partial x}=C\frac{\partial v}{\partial t}$$

解为前进波 $v^+$ 和后退波 $v^-$ 的叠加：

$$v(x,t)=v^+(t-x/u)+v^-(t+x/u)$$

$$i(x,t)=\frac{1}{Z_c}\left[v^+(t-x/u)-v^-(t+x/u)\right]$$

其中传播速度 $u=1/\sqrt{LC}$，特性阻抗 $Z_c=\sqrt{L/C}$（为常数）。对于长度为 $\ell$ 的线路，**单程传播时延**为：

$$\tau=\frac{\ell}{u}=\ell\sqrt{LC}$$

### 2.2 端口 Norton 等效的推导

设端口电流以**流入线路为正**。在 $k$ 端（$x=0$）和 $m$ 端（$x=\ell$）分别有：

$$i_k(t)=\frac{1}{Z_c}\left[v_k^+(t)-v_k^-(t)\right] = Y_c v_k(t) + I_{h,k}(t)$$

$$i_m(t)=\frac{1}{Z_c}\left[v_m^+(t-\tau)-v_m^-(t-\tau)\right] = Y_c v_m(t) + I_{h,m}(t)$$

其中**历史电流源**为：

$$I_{h,k}(t)=-Y_c\,v_m(t-\tau)-i_m(t-\tau)$$

$$I_{h,m}(t)=-Y_c\,v_k(t-\tau)-i_k(t-\tau)$$

注意历史量涉及的电压/电流均来自**对端**的 $\tau$ 时刻。这意味着在时间步 $t_n$ 求解网络方程前，必须先从延时队列中取出 $v_k(t_n-\tau)$、$i_k(t_n-\tau)$、$v_m(t_n-\tau)$、$i_m(t_n-\tau)$ 作为已知量。

### 2.3 延时队列的数据结构

设全局时间步长为 $\Delta t$，延时 $\tau = n\Delta t + \delta\Delta t$（$n\in\mathbb{N}$，$0\le\delta<1$）。延时队列按以下方式更新：

1. 求解当前时间步的网络方程，得到端口电压 $v_k(t_n)$、$v_m(t_n)$ 和端口电流 $i_k(t_n)$、$i_m(t_n)$
2. 将 $(v_k(t_n), i_k(t_n), v_m(t_n), i_m(t_n))$ 压入延时队列（队列长度至少为 $n+1$）
3. 通过线性插值近似非整数倍延时：

$$x(t_n-\tau) \approx (1-\delta)\,x(t_{n-m}) + \delta\,x(t_{n-m-1})$$

插值精度直接影响高频分量和相位误差。

### 2.4 多相线路的模态解耦

对于三相多导体线路，相域方程相互耦合。经模态变换（如Wedepohl变换）$\mathbf{v}_p = \mathbf{T}^{-1}\mathbf{v}_m$ 后，模域方程解耦为三个独立模量：

$$\mathbf{v}_m(x,s) = \mathbf{V}^+(s)e^{-\gamma_m s} + \mathbf{V}^-(s)e^{\gamma_m s}$$

其中 $\gamma_m$ 是模 $m$ 的传播常数。各模量的 Bergeron 等效独立求解，最后通过 $\mathbf{v}_p = \mathbf{T}^{-1}\mathbf{v}_m$ 变换回相域。**若变换矩阵 $\mathbf{T}$ 为频率相关（如非换位线路），模态 Bergeron 等效失效**，需用相域或频变方法。

## 分类与变体

| 变体 | 处理方式 | 适合用途 | 主要边界 |
|------|----------|----------|----------|
| 无损常参数 Bergeron | $R,G$ 忽略或近似为零 | 行波教学、基础暂态分析、长架空线初始评估 | 无法表征集肤效应、邻近效应和大地返回损耗 |
| 集中损耗 Bergeron | 在线路两端或中点加入电阻等效 | 工频附近或低损耗线路的稳态和短时暂态 | 高频损耗分布不准确，带宽受限（一般 < 1 kHz） |
| 模态 Bergeron | 多相线路经模态变换解耦后逐模态处理 | 换位或近似可解耦的三相线路（如架空换位线路） | 频率相关变换矩阵破坏常数模态假设；不换位线路需相域处理 |
| 频变 Bergeron 扩展 | 用有理函数或卷积修正 $Z_c(\omega)$ 与传播项 | 宽频暂态（雷电、开关操作、故障行波）研究 | 需拟合程序（如 Vector Fitting）；应检查[[passivity-enforcement]]以保证时域稳定性 |
| 混合 Bergeron-ULM | Bergeron 提供低频基准，ULM 提供宽频修正 | 同时关心低频谐波和高频行波的复合仿真场景 | 界面处理复杂，需验证全频段连续性 |

## 形式化表达

### 核心方程汇总

**电报方程（时域）**：
$$-\frac{\partial v}{\partial x}=L\frac{\partial i}{\partial t}+Ri, \quad -\frac{\partial i}{\partial x}=C\frac{\partial v}{\partial t}+Gv$$

**低损耗特性阻抗（复频域）**：
$$Z_c(s) \approx \sqrt{frac{L}{C}} quad (R\text{君} \omega L,\ G\text{君} \omega C)$$

**传播常数（低损耗近似）**：
$$\gamma(s) \approx s\sqrt{LC}$$

**单程传播延时**：
$$\tau = \ell\sqrt{LC}$$

**端口 Norton 等效方程**：
$$i_k(t) = Y_c\,v_k(t) + I_{h,k}(t), \quad Y_c = 1/Z_c$$

**历史电流源（$k$ 端，来自 $m$ 端延时）**：
$$I_{h,k}(t) = -Y_c\,v_m(t-\tau) - i_m(t-\tau)$$

**线性插值延时近似（$\tau = n\Delta t + \delta\Delta t$）**：
$$x(t-\tau) \approx (1-\delta)\,x(t-n\Delta t) + delta\,x(t-(n+1)\Delta t)$$

**多相模态变换**：
$$\mathbf{v}_p(x,s) = \mathbf{T}^{-1}(s)\,\mathbf{v}_m(x,s), \quad \mathbf{T} \text{ 为模态变换矩阵}$$

## 数值实现要点

### 3.1 延时插值与精度阶次

延时 $\tau$ 通常不是 $\Delta t$ 的整数倍。插值方法的选择影响高频响应：

- **线性插值（一阶）**：式(8)给出，简单但会在高频引人相位误差；精度 $O(\Delta t^2)$
- **三次样条插值**：更好的高频保持，但计算量增加；精度 $O(\Delta t^4)$
- **分段抛物线插值**：介于前两者之间

插值误差的积累会导致长线路仿真中相位漂移，应当记录所采用的插值阶次、时间步长和线路最短传播时间。

### 3.2 Courant-Friedrichs-Lewy（CFL）条件与短线路约束

当线路传播延时 $\tau < \Delta t$（即波速与时间步不匹配）时，特征线模型无法正常追踪行波——这是步长约束的根本来源。短线路（$\ell < u\Delta t$）的折现象在EMTP中通过**折叠线等效**（[[folded-line-equivalent]]）处理。

CFL 数定义为 $CFL = u\Delta t / \ell = \Delta t / \tau$。当 $CFL > 1$ 时需加密时间步或采用折叠等效。

### 3.3 数值阻尼与振荡控制

无损 Bergeron 在离散化后可能出现高频数值振荡（尤其在高频率/短线路情况下）。常用抑制方法：

- **在端口导纳中附加小电阻**：在 $Y_c$ 上并联 $G_{\text{damp}}$，使高频能量耗散
- **对历史源做指数平滑**：$I_{h,k}^{new} = \alpha I_{h,k}^{new} + (1-\alpha) I_{h,k}^{old}$，其中 $0<\alpha<1$
- **采用隐式 Bergeron（梯形规则）**：改变时间离散格式以引人数值阻尼

这些方法均会引人等效损耗，与真实物理损耗不同。

### 3.4 延时队列的存储与管理

每个 Bergeron 线路支路需维护四个延时队列：$v_k$、$i_k$、$v_m$、$i_m$，各长度至少为 $\lceil\tau/\Delta t\rceil$。对于长线路（$\tau \gg \Delta t$），队列长度可达数千，对实时仿真的存储带宽提出要求。FPGA 实现中常用**双缓冲循环队列**优化访问模式。

### 3.5 频变扩展的有理函数拟合

频变 Bergeron（$Z_c(\omega)$ 为复数频率相关函数）需用矢量拟合（Vector Fitting）近似：

$$Z_c(s) \approx d + es + \sum_{i=1}^{N} \frac{r_i}{s-p_i}$$

其中 $r_i$ 为留数，$p_i$ 为极点。拟合后用递归卷积或状态空间形式植人 EMT 求解器，同时需做[[passivity-enforcement]]以保证无源性。

## 关键技术挑战

1. **短线路/紧凑线路的 CFL 违约**：当 $\tau < \Delta t$ 时，特征线模型失效，需切换到[[folded-line-equivalent]]或其他等效方法
2. **频变参数与无损近似的矛盾**：实际输电线路的 $R(\omega)$、$L(\omega)$ 有显著集肤效应和邻近效应；低损耗 Bergeron 在高频下误差增大
3. **多导体线路的模态解耦失效**：非换位平行线路和电缆的变换矩阵为频率相关，固定模态变换使模态 Bergeron 变成近似
4. **延时插值引入相位误差**：尤其在雷电波和高频暂态仿真中，高频分量相位失真会累积
5. **非物理数值振荡**：无损线路的离散化在某些步长/参数组合下产生高频振荡，需引人数值阻尼

## 量化性能边界

| 指标 | 典型数值 | 验证条件 | 数据来源 |
|------|----------|----------|----------|
| 单步计算复杂度 | $O(1)$（与线路长度无关） | 每个端口一次加法+一次乘法 | EMTP 理论 |
| 延时队列长度 | $\lceil\tau/\Delta t\rceil$，典型值 100–10000 | 100 km 线路，$\Delta t = 50 \mu s$，$\tau \approx 0.667 ms$ → 队列长 13 | 工程估算 |
| 适用频带上限 | $\approx 0.1/\tau$（Hz）| 频变衰减可忽略的低损耗近似 | Wedepohl 1963 |
| 集中损耗近似适用频带 | $< 1$ kHz | 工频谐波和低频暂态 | 行业经验 |
| FPGA 实时步长（典型） | $50$–$100\ \mu s$ | 双 DDR 缓冲队列，$\tau = 1$ ms 线路 | SuperGrid Institute 2022 |
| 雷电波相位误差 | $< 5\%$（@ 100 kHz，线性插值） | $\delta < 0.5$，$\Delta t = 1 \mu s$ | Verrax 等 2022 |
| 模态 Bergeron 精度 | 取决于换位度；换位线路误差 $< 1\%$ | 换位三相架空线，频率 $< 10$ kHz | 行业经验 |

**原文未报告可核验的数值结果**：Bergeron 线路模型作为经典模型，其原始论文（Bergeron 1961）未给出上述量化指标；上表数据综合自行业经验和相关论文的实验数据。

## 适用边界与选择指南

**选择 Bergeron 模型而非其他线路模型的决策树**：

1. **是否关心宽频（> 10 kHz）响应？**  
   → 否 → 继续；  
   → 是 → 选用 [[frequency-dependent-line-model]]（Marti）或 [[universal-line-model]]
2. **线路是否为非换位多导体或电缆？**  
   → 是 → 选用相域频变模型或[[frequency-dependent-line-model]]；  
   → 否 → 继续
3. **是否要求实时仿真（步长固定）？**  
   → 是 → Bergeron（固定导纳，计算量小）；  
   → 否 → 可选用 [[folded-line-equivalent]]（更高精度但计算量更大）
4. **损耗是否必须精确表征？**  
   → 是 → 在两端加集中电阻（集中损耗 Bergeron）；  
   → 否 → 无损 Bergeron

**模型选择对照表**：

| 场景 | 推荐模型 | 原因 |
|------|----------|------|
| 长架空线行波教学/快速估算 | 无损常参数 Bergeron | 计算极简，概念清晰 |
| 工频谐波分析（< 1 kHz） | 集中损耗 Bergeron | 精度足够，实现简单 |
| 故障定位（行波法） | 频变 Bergeron 或模态 Bergeron | 需准确波速和衰减 |
| 雷电暂态（> 100 kHz） | [[universal-line-model]] | Bergeron 高频误差大 |
| 地下电缆（频变参数显著） | [[cable-model]]（频变） | 电缆 $R(\omega)$ 变化剧烈 |
| 实时 FPGA 仿真（固定步长） | 双缓冲 Bergeron | 每步仅需查表+加法 |

## 相关页面

- [[distributed-parameter-line]] — 线路电报方程和分布参数建模总框架
- [[universal-line-model]] — 相域频率相关特性导纳和传播矩阵的完整实现
- [[frequency-dependent-line-model]] — Marti 频变线路模型的 EMT 实现
- [[folded-line-equivalent]] — 围绕线路节点导纳和开路/短路贡献组织的替代实现方式
- [[frequency-dependent-soil]] — 大地返回路径的频率相关建模
- [[earth-return-impedance]] — Carson 大地返回阻抗公式
- [[modal-transformation]] — 多相线路的模态解耦变换
- [[passivity-enforcement]] — 频变模型的无源性强制（保证时域稳定）
- [[vector-fitting]] — 频变阻抗的有理函数拟合方法
- [[transmission-line-theory]] — 传输线理论基础（电报方程、行波解）

## 来源论文

- [[frequency-dependent-multiconductor-line-model-based-on-the-bergeron-method]] — Torrez Caballero 等将 Bergeron 框架扩展到频变多导体线路的代表性工作
- [[fitting-the-frequency-dependent-parameters-in-the-bergeron-line-model]] — Torrez Caballero 等关于 Bergeron 线路模型频变参数拟合的研究
- [[耦合长线电磁暂态分析的扩展bergeron模型]] — 徐政 1996 将多相耦合线路分解为集中电阻和无损线路两部分处理的扩展 Bergeron 模型
- Verrax 等 2022 — 图模型行波故障定位中 Bergeron 类低损耗近似在 HVDC 混合线路中的应用，提供了雷电波 100 kHz @ 5% 相位误差的量化数据