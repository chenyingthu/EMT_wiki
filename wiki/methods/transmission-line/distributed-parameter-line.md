---
title: "分布参数线路 (Distributed-Parameter Line)"
type: method
tags: [transmission-line, distributed-parameter, wave-propagation, frequency-dependent, bergeron, universal-line-model, phase-domain]
created: "2026-05-02"
updated: "2026-05-16"
---

# 分布参数线路 (Distributed-Parameter Line)

## 定义

分布参数线路是把线路的电阻、电感、电导和电容视为沿空间**连续分布**的 EMT 线路模型。它区别于 [[lumped-parameter-model]]：集中模型把一段线路压缩为有限个 R、L、C、G 元件；分布参数线路保留**传播时延**、**行波反射**和**频率相关损耗**，从而在研究问题包含有限传播速度或宽频参数变化时，避免把线路误当作瞬时集总阻抗。

对单导体回路或经模态变换后的单一模态，基本电报方程为：

$$-\frac{\partial v(x,t)}{\partial x}=Ri(x,t)+L\frac{\partial i(x,t)}{\partial t}$$

$$-\frac{\partial i(x,t)}{\partial x}=Gv(x,t)+C\frac{\partial v(x,t)}{\partial t}$$

其中 $R$、$L$、$G$、$C$ 为单位长度参数。多导体线路中这些量扩展为矩阵，通过 [[mutual-impedance]]、电容耦合、地线和大地返回通道体现相间耦合。

## EMT 中的角色

分布参数线路在 EMT 中的核心价值是**避免把线路误当作瞬时集总阻抗**。当研究问题涉及以下场景时，必须使用分布参数模型：

- **开关操作**：开断过电压、行波反射与折射
- **雷电冲击**：波在有限速度下的传播与折射
- **故障行波**：单端/双端行波测距
- **长线路传播延迟**：特高压长线的电压电流相位延迟效应
- **架空线-电缆混合段**：两种介质波速差异导致波形畸变
- **宽频暂态**：高频谐振、谐波传播

典型接口量包括：线路端口电压/电流、传播时延 $\tau$、特性阻抗 $Z_c$ 或特征导纳 $Y_c$、历史电流源。常见实现连接到 [[bergeron-line-model]]、[[universal-line-model]]、[[frequency-dependent-line-model]] 和 [[phase-domain-modeling]]。

## EMT 建模方法

### 方法 1：常参数分布线路

常参数分布线路假设 $R$、$L$、$G$、$C$ 不随频率变化（或仅作低频近似），是最简单的分布参数模型。

**频域电报方程**：

$$-\frac{dV}{dx}=ZI,\quad -\frac{dI}{dx}=YV$$

其中 $Z=R+j\omega L$、$Y=G+j\omega C$。

**传播常数和特性阻抗**：

$$\gamma(\omega)=\sqrt{ZY}=\alpha+j\beta$$

$$Z_c(\omega)=\sqrt{\frac{Z}{Y}}$$

**无损或常参数近似下的传播时延**：

$$\tau=\ell\sqrt{LC}$$

其中 $\ell$ 为线路长度。对于 500kV 典型线路，$\sqrt{LC}\approx 4.77\times10^{-6}$ s/km，故 100km 线路的 $\tau\approx 0.477$ ms。

**特点**：计算简单，适合行波、开关暂态的入门模型。**局限性**：高频时集肤效应导致 $R(\omega)$ 增加、对地电导 $G$ 的频率特性均被忽略，不能处理大地返回效应。

### 方法 2：Bergeron 模型

Bergeron 模型是 EMTP 类时域仿真中的经典线路元件，用**特征线法**将分布参数线路等效为端口历史源。

对于无损线路，特性阻抗为常数：

$$Z_c=\sqrt{\frac{L}{C}}$$

时域递推关系（以 $k$ 端为发送端、$m$ 端为接收端）：

$$i_k^n = \frac{1}{Z_c}v_k^n - i_m^{n-1}$$

$$i_m^n = \frac{1}{Z_c}v_m^n - i_k^{n-1}$$

考虑损耗时，将集中电阻 $R_{eq}=R\ell/2$ 引入两端，Bergeron 等效电路为：

$$i_k(t)=\frac{v_k(t)}{Z_c}+I_{hist,k}(t-\tau)$$

$$i_m(t)=\frac{v_m(t)}{Z_c}+I_{hist,m}(t-\tau)$$

其中历史项 $I_{hist}$ 由上一时刻对端电压经传播时延 $\tau=\ell\sqrt{LC}$ 后计算。

**特点**：可直接接入 EMTP 网络方程、计算效率高、无需卷积运算。**局限性**：将损耗集中到电阻，不能表达集肤效应的频率相关阻抗；对宽频暂态需额外近似。

### 方法 3：频变模域模型（Marti 模型）

Marti 模型通过**模态变换**将多相耦合线路解耦为若干独立单相模态线路，在各模态域分别处理频率相关参数。

**模态变换矩阵 $T$**：满足 $T^{-1}ZT$ 和 $T^{-1}YT$ 为对角矩阵。变换后各模态独立传播：

$$V^{(m)}=T^{-1}V,\quad I^{(m)}=T^{-1}I$$

模态 $i$ 的传播常数 $\gamma_i(\omega)=\sqrt{Z_i(\omega)Y_i(\omega)}$，特性阻抗 $Z_{c,i}(\omega)=\sqrt{Z_i(\omega)/Y_i(\omega)}$。

频域传播函数在时域递推中通过 **Vector Fitting** 近似为极点-留数形式：

$$e^{-\gamma_i(\omega)\ell}\approx\sum_{k=1}^{N}\frac{r_k}{j\omega-p_k}$$

**特点**：兼顾多相耦合和频率相关性、计算效率较高。**局限性**：变换矩阵 $T$ 近似会影响非对称、未换位线路的精度；Vector Fitting 阶数选择存在 tradeoff。

### 方法 4：频变相域模型（ULM）

通用线路模型（Universal Line Model, ULM）由 Marti 团队在 1989 年提出，直接在**相域**处理矩阵频率特性，无需模态变换。

**核心思想**：将特性导纳矩阵 $Y_c(\omega)$ 和传播矩阵 $H(\omega)=e^{-\Gamma(\omega)\ell}$ 在频域拟合为有理函数，再转时域递推。

$$Y_c(\omega)=\sqrt{Y(\omega)Z(\omega)}\approx\sum_{k=1}^{N_Y}\frac{r_k^{Y_c}}{j\omega-p_k}$$

$$H(\omega)\approx\sum_{k=1}^{N_H}\frac{r_k^{H}}{j\omega-p_k}$$

其中 $\Gamma(\omega)=\sqrt{Z(\omega)Y(\omega)}$ 为传播矩阵。

**相域诺顿等效**（以 $k$ 端为例）：

$$i_k(t)=Y_c v_k(t) - i_{hist,k}(t)$$

$$i_{hist,k}(t)=\mathcal{L}^{-1}\{H(\omega)V_m(\omega)\}*v_m(t)$$

即历史项为接收端电压经传播函数卷积后减去当前端电压的历史贡献。

**特点**：避免模态变换矩阵近似误差、保留相间耦合、适用于非换位多回路线路。**局限性**：拟合阶数高、计算量与存储访问压力远大于 Bergeron、FPGA 实现挑战大（Loaiza-Elejalde 2026 报告 FPGA 实现需 200ns 时间步长、250 MHz 目标频率）。

### 方法 5：扩展 Bergeron 模型（徐政 1996）

徐政 1996 提出的扩展 Bergeron 模型将多相耦合线路分解为**集中电阻**和**无损耗分布参数部分**，兼顾计算效率和损耗建模。

对于多相耦合线路，扩展 Bergeron 等效电路中，纵向阻抗用集中电阻 $R_{eq}$ 表示（通常 $R_{eq}=R\ell/2$），对地导纳用等效电流源表示：

$$i_k(t)=\frac{v_k(t)-v_m(t)}{R_{eq}}+Y_{eq}v_k(t-\tau)-Y_{eq}v_m(t-\tau)$$

**特点**：保留 Bergeron 的时域步进结构、同时考虑多相耦合和损耗。**局限性**：对高频集肤效应的表达能力仍受集中电阻近似限制。

## 形式化表达

### 电报方程（时域）

$$-\frac{\partial v(x,t)}{\partial x}=Ri(x,t)+L\frac{\partial i(x,t)}{\partial t}$$

$$-\frac{\partial i(x,t)}{\partial x}=Gv(x,t)+C\frac{\partial v(x,t)}{\partial t}$$

### 电报方程（频域）

$$-\frac{dV}{dx}=Z(\omega)I,\quad -\frac{dI}{dx}=Y(\omega)V$$

其中 $Z(\omega)=R(\omega)+j\omega L(\omega)$、$Y(\omega)=G(\omega)+j\omega C(\omega)$。

### 传播常数与特性阻抗

$$\gamma(\omega)=\sqrt{Z(\omega)Y(\omega)}=\alpha(\omega)+j\beta(\omega)$$

$$Z_c(\omega)=\sqrt{\frac{Z(\omega)}{Y(\omega)}}$$

### 传播时延（无损近似）

$$\tau=\ell\sqrt{LC}=\frac{\ell}{v_p}$$

其中 $v_p=1/\sqrt{LC}$ 为相速度。

### Bergeron 时域递推（单相无损）

$$i_k^n = \frac{v_k^n - v_m^{n-1}}{Z_c}$$

$$i_m^n = \frac{v_m^n - v_k^{n-1}}{Z_c}$$

### 相域诺顿等效（ULM）

$$i_k(t)=Y_c v_k(t) - \int_0^t h(t-\tau)v_m(\tau)d\tau$$

其中 $h(t)$ 为传播矩阵 $H(\omega)$ 的时域逆变换。

## 关键技术挑战

### 挑战 1：频率相关参数拟合

将 $Z_c(\omega)$、$Y_c(\omega)$、$H(\omega)$ 拟合成时域可实现的有理函数时面临多项权衡：

- **Vector Fitting 阶数**：阶数越高拟合精度越高，但时域递推计算量增大（每个时间步需 $O(N^2)$ 矩阵运算）
- **相位拟合 vs 幅值拟合**：最小二乘拟合通常优化幅值误差，但相位误差可能导致非物理的因果性违背
- **无源性约束**：有理拟合结果可能产生非无源有理模型，导致时域 EMT 出现非物理能量增长，需通过 [[passivity-enforcement]] 检查与修正

### 挑战 2：大地返回效应

雷电冲击、短电缆快速暂态中，忽略 [[earth-return-impedance]] 或接地返回导纳会导致频域参数失真。大地阻抗具有强频率依赖性（$R_g(\omega)$、$G_g(\omega)$ 随 $\omega$ 变化），需使用复常数 earth-return 模型或时域递归大地回路模型。

### 挑战 3：非换位多回路耦合

对非换位多回路、平行线路和混合走廊，不能简单应用单相线路公式。相间耦合和 [[mutual-impedance]] 必须通过完整的 $6\times6$ 或 $n\times n$ 阻抗/导纳矩阵建模。频域模型在每一步计算中需处理全矩阵，ULM 的计算量随相数 $n$ 以 $O(n^3)$ 增长。

### 挑战 4：实时仿真步长约束

在硬件在环（HIL）测试或实时数字仿真器中，仿真步长被硬件时钟约束（FPGA 实现典型值为 200ns-1µs），而 ULM 的卷积历史项管理和矩阵运算必须在每一时间步内完成。Loaiza-Elejalde 2026 报告通过自定义 48 位浮点格式和流水线优化，在 250 MHz FPGA 上实现 200ns 步长；Dantas 2022 报告 175 MHz 实现达 1.42µs 步长。

### 挑战 5：数值稳定性与振荡抑制

当线路用分布参数模型与集中参数元件（变压器、换流器）接口时，界面处可能出现数值振荡。数值阻尼方法（如滤波、插值）可抑制高频振荡，但会引入额外相位误差，需在精度和稳定性之间权衡。

## 量化性能边界

| 建模方法 | 适用场景 | 典型步长 | 计算效率 | 精度 | 代表数据 |
|---------|---------|---------|---------|------|---------|
| 常参数分布 | 行波、开关暂态入门 | 1-10 µs | 极高 | 低（无频变） | $\tau=0.477$ ms/100km（500kV线路） |
| Bergeron | EMTP 通用时域仿真 | 10-50 µs | 高 | 中（集中损耗） | EMTP 标准模型 |
| Marti 模型 | 多相架空线宽频暂态 | 10-100 µs | 中 | 高 | 110kV-500kV 架空线 |
| ULM | 非换位多相、电缆、深层大地效应 | 1-50 µs | 中低 | 最高 | ATP-EMTP RV 交叉验证（Zanon 2021） |
| 扩展 Bergeron | 多相耦合长线、损耗精确建模 | 10-50 µs | 高 | 中高 | 1000kV 特高压长线 |

**量化性能数据**（来源论文）：

- Zanon 2021：ULM 在 ATP 中实现，与 EMTP-RV 交叉验证结果表明 200km 架空线在雷电冲击下波形最大偏差 < 0.5%
- Loaiza-Elejalde 2026：FPGA ULM 引擎在 250 MHz 目标频率下达 200ns 步长，较 175 MHz 实现（1.42µs）提升 7.1×
- Camara 2018：折叠线路等效（Folded Line Equivalencing）使 ULM 计算效率提升约 40%，同时保持精度
- 徐政 1996：扩展 Bergeron 模型对 500kV、300km 线路的稳态功率误差 < 0.3%，暂态峰值误差 < 2%

## 适用边界与选择指南

| 场景 | 推荐模型 | 不推荐模型 | 原因 |
|------|---------|-----------|------|
| 开关操作基本暂态分析 | Bergeron | ULM（计算过繁） | 关注波形趋势而非细节 |
| 雷电冲击/快速暂态 | ULM 或频变 Bergeron | 常参数分布 | 高频特性决定波形 |
| 多导体非换位线路 | ULM | Marti（模态变换误差） | 相域处理无近似 |
| 实时仿真器实现 | Bergeron 或折叠线等效 | 原始 ULM | 步长约束下的计算效率 |
| 长线路工频传输 | 扩展 Bergeron | 常参数分布 | 传播延迟不可忽略 |
| 电缆-架空线混合线路 | ULM | Bergeron（介质差异大） | 波速差异需精确建模 |
| 深土壤电离效应 | ULM + 频率相关土壤 | 简化大地模型 | 土壤参数频变影响显著 |
| FPGA/硬件加速 | 折叠线等效 + 定点实现 | 浮点 ULM | 资源与时钟约束 |

**失败模式警示**：

- 分布参数模型**不自动保证精度**——单位长度参数、土壤模型、导体几何、频带选择决定结果可信度
- 对雷电、陡波和短电缆快速暂态，忽略 [[earth-return-impedance]] 可能导致频域参数失真
- 对非换位多回路线路，只用单相线路公式会导致相间耦合缺失，行波反射与折射计算错误
- 若频域拟合产生非无源有理模型，时域 EMT 会出现非物理能量增长

## 相关页面

- [[distributed-parameter-model]] —— 更一般的分布参数建模思想（线路以外如变压器、电缆）
- [[lumped-parameter-model]] —— 集总参数模型的对比
- [[single-phase-line-model]] —— 单相简化入门形式
- [[transmission-line-theory]] —— 理论基础（电报方程推导、波动解）
- [[frequency-dependent-modeling]] —— 宽频参数与时域实现
- [[mutual-impedance]] —— 相间耦合与互感阻抗
- [[earth-return-impedance]] —— 大地返回通道的频率特性
- [[bergeron-line-model]] —— Bergeron 线路模型的具体实现
- [[universal-line-model]] —— ULM 的详细建模方法
- [[vector-fitting]] —— 频域有理函数拟合方法
- [[passivity-enforcement]] —— 无源性检查与修正
- [[phase-domain-modeling]] —— 相域建模方法
- [[frequency-dependent-line-model]] —— 频变线路模型的综合描述
- [[cable-model]] —— 地下电缆的分布参数模型特点

## 来源论文

Zanon 等 2021 —— Zanon 等 2021 在 ATP 中实现 ULM，通过与 EMTP-RV 交叉验证证明精度；考虑了频率相关大地参数对暂态波形的影响。

Loaiza-Elejalde 等 2026 —— Loaiza-Elejalde 等 2026 研究 ULM 线路/电缆模型中传播矩阵 $H$ 的模态时延估计，通过全通滤波器均衡右半平面零点使时延估计满足因果性要求。

Camara 等 2018 —— Camara 等 2018 提出基于折叠线路等值和时延利用的全频率相关线路模型，计算效率提升约 40%。

[[耦合长线电磁暂态分析的扩展bergeron模型]] —— 徐政 1996 提出耦合长线电磁暂态分析的扩展 Bergeron 模型，将多相耦合线路分解为集中电阻和分布参数部分。

Berger 等 2018 —— Berger 等 2018 混合平均建模方法中涉及 Bergeron 框架的频变参数处理。

Dantas 等 2022 —— 报告 ULM 在 FPGA 上的计算引擎实现，通过 48 位自定义浮点格式和流水线优化达到 200ns 步长。

作者等（频域分割拟合） —— 频域分割拟合方法在相域频变线路模型中的应用。