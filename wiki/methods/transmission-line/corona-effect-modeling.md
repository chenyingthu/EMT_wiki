---
title: "电晕效应建模 (Corona Effect Modeling)"
type: method
tags: [corona, transmission-line, emt, bergeron-model, nonlinear-modeling, overvoltage, lightning, vdlm, vfdlm]
created: "2026-05-10"
updated: "2026-05-14"
---

# 电晕效应建模 (Corona Effect Modeling)

## 定义

电晕效应是指架空输电线路导线表面电场强度超过空气击穿阈值时，导体周围空气发生电离放电的物理现象。在 EMT 仿真中，电晕表现为线路并联参数的电压相关非线性变化：导线附近空间电荷的积累使线路单位长度电容增大，同时电离过程中的能量耗散引入并联电晕损耗电导。这两者共同改变行波传播特性，导致过电压波的幅值衰减和波形畸变。

电晕效应在高电压架空线路的雷击过电压和操作过电压分析中不可忽视——忽略电晕的线路模型会给出偏保守（偏高）的过电压估计。Pereira & Tavares (2022) 对 Tidd、EDF 和 Shiobara 三条现场线路的验证表明，忽略电晕时 WB 线路模型分别高估过电压峰值约 27%（Tidd）、49%（EDF）和 31%（Shiobara）。

核心公式——经验电晕模型将单位长度电容和电导表示为电压的函数：

$$
C(v) = \begin{cases}
C_0, & |v| \leq v_0 \\
C_0 + f_c(|v| - v_0), & |v| > v_0
\end{cases}
$$

$$
G(v) = \begin{cases}
G_0, & |v| \leq v_0 \\
G_0 + g_c(|v| - v_0)^\alpha, & |v| > v_0
\end{cases}
$$

其中 $v_0$ 为起晕阈值电压（inception voltage），$C_0$ 为线路几何电容，$G_0 \approx 10^{-11}$ S/m 为微小背景电导，$f_c$、$g_c$、$\alpha$ 为经验参数，由线路导线类型、直径、高度和气象条件决定。

## EMT 中的角色

电晕效应在 EMT 仿真中直接影响过电压评估和绝缘配合设计的准确性：

- **幅值衰减**：电晕增大的并联电容和电导吸收行波能量，使传播中的过电压峰值低于忽略电晕时的结果。Pereira & Tavares (2022) 实测验证：Tidd 线（$v_{crit}=470$ kV）过电压高估 27%，EDF 线（$v_{crit}=250$ kV）高估 49%，Shiobara 线（$v_{crit}=303$ kV）高估 31%。
- **波形畸变**：电压相关电容使波前陡度降低、上升时间延长。Jiang 等 (2024) 在 110 kV 线路（LGJ-150 导线）上的仿真表明，当传播距离达 15 km、峰值 1200 kV 时，3.83/75 μs 波形的峰值衰减 209.2 kV、前沿时间增加 19.7 μs；0.43/40 μs 陡波衰减 341.2 kV、前沿增加 20.2 μs。
- **波速变化**：电容增大使特征阻抗降低、传播时间增加。Pereira & Tavares (2022) 对 Tidd 线（100 m 分段）的测量显示：无电晕时传播时间 $\tau = 33.39$ μs，当 $v = 1000$ kV 时增大，$v = 2000$ kV 时进一步增大——电压越高，时延越长。
- **波形依赖性**：Jiang 等 (2024) 发现电晕衰减程度强烈依赖冲击波波形：波前/波尾时间越短（陡波），电晕造成的衰减和畸变越严重；这是因为陡波具有更高的峰值电场，更早触发起晕，空间电荷有更多时间吸收能量。

忽略电晕的线路模型在雷击过电压和操作过电压分析中给出偏保守结果，可能导致绝缘配合设计过于昂贵。因此，在精确过电压评估中，电晕建模是必要的。

## 核心建模方法

### 方法一：集中电晕支路（Lumped Corona Branch）

传统工程做法将线路沿空间离散为若干分段，在每段端点（junction node）外接非线性 RC 并联支路表示该段的电晕效应。线路本身的分布参数（$Z(s)$、$Y(s)$）保持不变，电晕仅作为节点上的集总导纳注入。

**数学表达**：在节点 $k$ 处，电晕支路注入电流为

$$i_{corona,k} = G(v_k) \cdot v_k + C(v_k) \frac{dv_k}{dt}$$

其中 $G(v)$ 和 $C(v)$ 由经验电晕模型（如 Umoto-Hara 模型）计算。

**特点**：
- 实现简单，可直接嵌入任何 EMT 程序
- 物理上电晕是沿线分布的，集中近似在长线路波过程中引入离散化误差
- 波前越陡、线路越长，集中近似的误差越大
- 适用场景：工程快速评估、短线路、对精度要求不高的绝缘配合初步设计

**局限**：电晕与线路传播模型解耦，无法反映电晕对行波传播速度和高频衰减的耦合影响。

### 方法二：电压相关线路模型（VDLM / Voltage-Dependent Line Model）

Pereira & Tavares (2020) 首次提出 VDLM，将电晕效应内嵌到 Bergeron/Dommel 线路模型中，替代传统的外接集中电晕支路。核心思路是把单位长度并联导纳处理为电压相关量：

$$Y(s, v) = G(v) + sC(v)$$

从而特征导纳和传播函数变为电压和频率的双相关函数：

$$Y_c(s, v) = \sqrt{Z(s) \cdot Y(s, v)}$$

$$H(s, v) = e^{-\sqrt{Y(s, v) \cdot Z(s)} \cdot l}$$

线路仍保持 Norton 等效形式，端口导纳和历史电流源随电压更新。

**非迭代求解策略**：为避免同一时间步内反复迭代非线性方程，VDLM 用前一时间步的导体电压 $v(t-\Delta t)$ 更新当前步的线路参数和历史量，直接求解节点电压方程：

$$[Y_{sh}(v(t-\Delta t))] \cdot [v(t)] = [i(t)] - [i_{hist}(v(t-\Delta t))]$$

**特点**：
- 电晕从线路参数层面表达为分布效应，而非外接集中支路
- 保持 EMT 程序需要的 Norton 端口接口，可嵌入任意网络
- 非迭代求解避免了传统非线性迭代在每步求解中的实现复杂性
- 验证：Matlab 实现，与 Tidd、EDF、Shiobara 三条现场线路测量数据吻合

**局限**：原始 VDLM 仅支持单相线路；未耦合频率相关参数（后续 VFDLM 弥补）；验证限于雷击过电压场景。

### 方法三：电压-频率双相关线路模型（VFDLM / Voltage- and Frequency-Dependent Line Model）

Pereira & Tavares (2022) 将 VDLM 扩展为 VFDLM，同时耦合电晕（电压相关）和频变参数（频率相关）。这是 FD/WB 线路模型的更一般形式：

串联阻抗保留频率相关特性：
$$Z(s) = R(s) + sL(s)$$

并联导纳同时依赖电压和频率：
$$Y(s, v) = G(v) + sC(v)$$

特征导纳和传播函数为双相关：
$$Y_c(s, v) = \sqrt{Z^{-1}(s) \cdot Z(s) \cdot Y(s, v)}$$

$$H(s, v) = e^{-\sqrt{Y(s, v) \cdot Z(s)} \cdot l}$$

**时域实现**：对每个预计算的电压样本 $v_j$，用矢量拟合（Vector Fitting, VF）将 $Y_c(s, v_j)$ 和 $H(s, v_j)$ 近似为有理函数：

$$Y_c(s, v_j) \sim d + \sum_{i=1}^{N_{p}^{Y_c}} \frac{r_i^{Y_c}(v_j)}{s - p_i^{Y_c}(v_j)}$$

$$H(s, v_j) \sim \sum_{i=1}^{N_{p}^{H}} \frac{r_i^{H}(v_j)}{s - p_i^{H}(v_j)} \cdot e^{-s\tau}$$

然后通过递归卷积求解时域卷积，得到时间域实现参数（TDIP）：$G_s(v_j)$、$r_i^{Y_c}(v_j)$、$\alpha_i^{Y_c}(v_j)$、$\lambda_i^{Y_c}(v_j)$、$\mu_i^{Y_c}(v_j)$、$r_i^{H}(v_j)$、$\alpha_i^{H}(v_j)$、$\lambda_i^{H}(v_j)$、$\mu_i^{H}(v_j)$ 和 $\tau(v_j)$。

**仿真流程**：
1. **预计算阶段**：在 $v_{crit} \leq v_j \leq v_{max}$ 范围内取 $n$ 个电压样本（Tidd 线取 $n=100$，范围 470–2000 kV），为每个样本计算 TDIP。对 Tidd 线，100 个电压样本的 TDIP 计算耗时 < 0.6 s。
2. **仿真循环**：每步检查导体电压，搜索最接近的电压样本 $v_j$，更新对应 TDIP。
3. **缓冲区管理**：传播时延 $\tau$ 随电压变化，历史缓冲区大小由最大时延决定：

$$BS = \left\lfloor \frac{\tau(v_{max})}{\Delta t} \right\rfloor + 1$$

4. **线性插值**：当 $\tau$ 不是 $\Delta t$ 的整数倍时，对历史缓冲区进行线性插值。

**特点**：
- 同时处理电晕和频变参数，是现有 EMT 线路模型中精度最高的方案
- VF 拟合误差 < 0.02%，最多 8 个极点即可达到精度
- 仅使用实极点可大幅减少 TDIP 存储量
- 仿真循环中仅增加"电压搜索+参数更新"的开销，计算负担极小
- 验证：三条现场线路（Tidd、EDF、Shiobara），时间步 $\Delta t = 10$ ns，分段长度 50–100 m

**局限**：
- 预计算阶段需要为多个电压样本做矢量拟合，增加线路常数程序的计算量
- 原始实现仅支持单相线路；多相扩展需处理模态耦合
- $v_{max}$ 通常取 $4 \cdot v_{crit}$ 或 $5 \cdot v_{crit}$（实际过电压极少超过 4 p.u.，否则会发生电弧）
- 递归卷积优于梯形积分：Pereira & Tavares 验证梯形积分会引入更严重的虚假振荡

### 方法四：波形依赖电晕模型（Waveform-Dependence Corona Model）

Jiang 等 (2024) 提出考虑起晕延时和电离弛豫的波形依赖电晕模型，在 PSCAD/EMTDC 中实现。与传统固定阈值电晕模型不同，该模型认为：

1. **起晕延时依赖波形**：采用临界体积法（critical volume method）计算起晕延时——导线周围满足电子雪崩条件的空间体积决定了起晕概率。陡波（短波前）因电场上升更快，起晕延时更短；缓波则延时更长。
2. **电离弛豫过程**：空间电荷不是在电压越过阈值后瞬时达到稳态，而是按弛豫过程逐步建立。这减缓了初始电晕电荷的增长速率，略微降低了最大电晕电荷量。

**数学框架**：电晕支路的状态量为导线电压、起晕延时、空间电荷线密度、电晕电容和电晕支路电流。通过梯形积分将时变电容支路改写为等效电导/电阻与历史电流源的 Norton 形式，嵌入 PSCAD/EMTDC 节点导纳矩阵。

**验证**：
- Q-V 曲线：与 coaxial 配置（250 kV, 120/2200 μs）和 conductor-above-ground 配置（2.5/60 μs）的实测结果吻合
- 线路传播：Wagner 实验（1.28 MV, 1.3/6.2 μs, ACSR 导线, 半径 2.54 cm, 平均高度 18.89 m），正极性 surge 衰减比负极性更显著
- 波形影响：在 110 kV 线路（LGJ-150）上，15 km 传播距离、1200 kV 峰值时，0.43/40 μs 陡波的衰减（341.2 kV）显著大于 3.83/75 μs 缓波（209.2 kV）

**特点**：
- 首次将波形依赖性系统性地纳入 EMT 电晕建模
- 免迭代等效使模型可直接嵌入 PSCAD/EMTDC
- 能反映不同波前/波尾雷电冲击在传播中不同的衰减和畸变特性

**局限**：
- 验证限于单相线路和文献测量场景
- 未报告量化误差指标、运行时间统计
- 未验证多导体耦合、复杂地形或气象条件

### 方法五：π 电路离散化电晕模型

Lessa 等 (2012) 提出用级联 π 型集中参数电路模拟输电线路分布参数，并在状态空间框架中嵌入电晕表示。该方法面向教学/入门研究，在 Matlab 中实现：

**状态空间方程**：
$$\dot{x} = Ax + Bu$$

其中 $x$ 为状态变量向量（沿线节点电压和 π 电路纵向支路电流），$u$ 为外部激励或边界输入。

**频率相关参数近似**：在纵向参数中引入并联 RL 块，模拟纵向阻抗随频率变化的特性（集肤效应和大地影响）。

**电晕表示**：在不考虑频率影响的模型上加入电晕，设定电晕只发生在线路的一小段区域，比较有无电晕时的暂态响应差异。

**时间积分**：采用 Heun 法（梯形积分）离散连续状态方程：

$$x[k+1] = A'' \cdot x[k] + B' \cdot (u[k] + u[k+1])$$

其中 $A''$ 和 $B'$ 由 $A$、$B$、积分步长 $T$ 和单位矩阵组装。

**特点**：
- 模型层级清晰：π 电路（空间离散）→ 状态变量（矩阵方程）→ 梯形积分（时域步进）→ 电晕模块（非线性）
- 便于教学和理解输电线路暂态中的各物理概念
- 矩阵实现有利于扩展 π 电路数量，观察空间离散化对波形的影响

**局限**：
- 仅面向单相等效线路和简单暂态激励
- 未验证多相耦合、复杂网络或实际测量波形
- 未报告可核验的线路长度、时间步长、π 电路数量、误差指标

## 形式化表达

### 电报方程（Telegrapher's Equations）

线路微元 $\Delta x$ 的电压电流关系：

$$-\frac{\partial V(x,s)}{\partial x} = Z(s) \cdot I(x,s)$$

$$-\frac{\partial I(x,s)}{\partial x} = Y(s, v) \cdot V(x,s)$$

其中 $Z(s) = R(s) + sL(s)$ 为串联阻抗，$Y(s, v) = G(v) + sC(v)$ 为并联导纳（电晕使 $G$ 和 $C$ 依赖电压）。

### 行波方程（Traveling-Wave Equations）

终端 $k$ 和 $m$ 的电压电流关系：

$$I_k(s) = Y_c(s,v) \cdot V_k(s) - I_{ki}(s)$$

$$I_{ki}(s) = H(s,v) \cdot I_{mr}(s)$$

变换到时域（Norton 等效）：

$$i_k(t) = G_s \cdot v_k(t) - i_{hist,k}(t)$$

$$i_{kr}(t) = i_k(t) + i_{ki}(t)$$

$$i_{ki}(t+\Delta t) = H^* \ast i_{mr}(t-\tau)$$

$$i_{hist,k}(t+\Delta t) = Y_c^* \ast v_k(t) - 2i_{ki}(t+\Delta t)$$

### 电压相关特征导纳

$$Y_c(s, v) = \sqrt{Z^{-1}(s) \cdot Z(s) \cdot Y(s, v)}$$

$$H(s, v) = e^{-\sqrt{Y(s, v) \cdot Z(s)} \cdot l}$$

### 缓冲区大小

$$BS = \left\lfloor \frac{\tau(v_{max})}{\Delta t} \right\rfloor + 1$$

### Umoto-Hara 电晕经验模型

电晕电荷密度 $\rho_c$ 和电晕电容 $C_c$ 由导线半径 $r$、起晕电压 $v_0$、导体电压 $v$ 和空气密度 $\delta$ 决定：

$$\rho_c = 2\pi\epsilon_0 \cdot v_0 \cdot \ln\left(\frac{r_c}{r}\right)$$

$$C_c = \frac{d\rho_c}{dv}$$

其中 $r_c$ 为电离区半径，$\epsilon_0$ 为真空介电常数。

## 关键技术挑战

### 非线性求解与数值稳定性

电晕使线路参数成为电压的函数，导致 Norton 等效导纳矩阵 $[Y_{sh}(v(t))]$ 和历史电流源 $[i_{hist}(v(t))]$ 均为电压相关量。若采用隐式迭代求解，每步需反复更新参数直到收敛，增加计算负担且可能发散。VDLM 采用的前一时步显式更新策略（用 $v(t-\Delta t)$ 更新当前步参数）避免了迭代，但要求时间步长足够小以捕捉电压快速变化。

### 空间离散化精度

VFDLM 基于 TEM 模态传播假设，必须将线路离散为短分段。Pereira & Tavares (2022) 建议：雷击过电压（最高频率 ~1 MHz）分段长度应 ≤ 100 m；操作过电压（频率较低）可放宽至 10–20 km。分段越长，高频衰减和色散误差越大。

### 矢量拟合的电压离散化

VFDLM 需为多个电压样本分别做矢量拟合。Pereira & Tavares (2022) 发现 $n=100$ 个线性分布电压样本已足够，增加到 $n=200$ 时波形无明显差异。拟合阶数自动调整，最大极点数为 8 即可使拟合误差 < 0.02%。仅使用实极点可大幅减少存储量。

### 波形依赖性建模

传统电晕模型使用固定的起晕阈值和 Q-V 曲线，无法反映不同波前/波尾雷电冲击的差异化衰减。Jiang 等 (2024) 证明波前时间越短、电晕衰减越严重（15 km 传播距离下，0.43/40 μs 陡波衰减 341.2 kV vs 3.83/75 μs 缓波衰减 209.2 kV）。将波形依赖性纳入 EMT 建模需要临界体积法和电离弛豫的额外计算。

### 多相耦合扩展

现有验证（Pereira 2020/2022、Jiang 2024）均限于单相线路。实际输电线路为三相（或多回线）耦合系统，电晕效应在各相之间通过互电容和互电导耦合。多相扩展需处理模态变换和相域参数的联合非线性更新。

## 量化性能边界

| 来源 | 验证场景 | 关键数据 |
|------|---------|---------|
| Pereira & Tavares 2022 (VFDLM) | Tidd 线 ($v_{crit}=470$ kV) | 忽略电晕高估过电压 27%；$\tau=33.39$ μs (无电晕) → 增大 (有电晕)；100 电压样本 TDIP 计算 < 0.6 s；拟合误差 < 0.02%，最多 8 极点 |
| Pereira & Tavares 2022 (VFDLM) | EDF 线 ($v_{crit}=250$ kV) | 忽略电晕高估过电压 49%；分段 50 m，$\Delta t=10$ ns；电压范围 250–1300 kV |
| Pereira & Tavares 2022 (VFDLM) | Shiobara 线 ($v_{crit}=303$ kV) | 忽略电晕高估过电压 31%；分段 100 m；电压范围 303–1800 kV |
| Pereira & Tavares 2022 (VFDLM) | 递归卷积 vs 梯形积分 | 梯形积分引入更严重的虚假振荡，递归卷积更稳定 |
| Jiang 等 2024 | 110 kV 线路 (LGJ-150), 15 km | 1200 kV 峰值下：3.83/75 μs 衰减 209.2 kV, 前沿 +19.7 μs；0.43/40 μs 衰减 341.2 kV, 前沿 +20.2 μs；3.83/40 μs 衰减 296.3 kV, 前沿 +17.2 μs |
| Jiang 等 2024 | Wagner 实验 (1.28 MV, ACSR) | 正极性 surge 衰减比负极性更显著；Q-V 曲线与 coaxial/conductor-above-ground 实测吻合 |
| Lessa 等 2012 | 单相 π 电路 (Matlab) | 电晕仅在线路一小段区域；比较有无电晕的暂态响应差异；未报告量化误差 |

## 适用边界与选择指南

| 应用场景 | 推荐模型 | 理由 |
|---------|---------|------|
| 工程快速评估、短线路 | 集中电晕支路 | 实现简单，计算开销最低 |
| 雷击过电压精确分析（单相） | VDLM | 分布电晕+非迭代求解，与现场测量吻合 |
| 雷击/操作过电压（需频变+电晕耦合） | VFDLM | 同时处理电晕和频变参数，精度最高 |
| 波形依赖性分析（陡波 vs 缓波） | 波形依赖电晕模型 | 考虑起晕延时和电离弛豫，反映波形影响 |
| 教学/入门理解 | π 电路离散化 | 物理含义清晰，便于扩展和观察 |

**选择决策**：
- 若只需定性了解电晕对过电压的影响 → 集中电晕支路
- 若需精确评估绝缘配合（单相） → VDLM
- 若需同时考虑频变参数和电晕（单相） → VFDLM
- 若需研究不同雷电波形下的衰减差异 → 波形依赖电晕模型
- 若为教学目的理解各物理概念 → π 电路模型

## 相关方法

- [[transmission-line-theory]] — 传输线建模基础
- [[bergeron-line-model]] — Bergeron 行波模型
- [[universal-line-model]] — 通用线路模型（ULM）
- [[frequency-dependent-network-equivalent]] — 频变参数建模
- [[lightning-transient-analysis]] — 雷击暂态分析
- [[switching-transient]] — 操作过电压分析
- [[lightning-overvoltage]] — 雷击过电压

## 相关模型

- [[transmission-line-model]] — 输电线路模型
- [[cable-model]] — 电缆模型

## 相关主题

- [[grounding-lightning-overvoltage]] — 接地与雷击过电压
- [[transmission-line-modeling]] — 输电线路建模
- [[insulation-coordination]] — 绝缘配合

## 来源论文

- **Pereira & Tavares (2022)** — *A New Approach to Represent the Corona Effect and Frequency-Dependent Transmission Line Models in EMT-Type Programs* (IEEE Trans. on Power Delivery, Vol. 37, No. 6)。提出 VFDLM，将特征导纳和传播函数扩展为电压-频率双相关，通过矢量拟合+递归卷积实现时域等效，在三条现场线路上验证。
- **Pereira & Tavares (2020)** — *Development of a Voltage-Dependent Line Model to Represent the Corona Effect in Electromagnetic Transient Program*。首次提出 VDLM，将电晕内嵌到 Bergeron/Dommel 线路模型中，采用前一时步显式更新避免迭代求解。
- **Jiang, Lin & Li (2024)** — *A waveform-dependence lightning impulse corona model in PSCAD/EMTDC for investigating surge propagation on transmission lines* (Electric Power Systems Research 236)。提出波形依赖电晕模型，用临界体积法计算起晕延时，纳入电离弛豫过程，在 PSCAD/EMTDC 中实现免迭代求解。
- **Lessa et al. (2012)** — *Application of π circuits for simulation of corona effect in transmission lines*。用级联 π 电路和状态空间方法模拟输电线路暂态，在 Matlab 中嵌入电晕表示，面向教学入门。
