---
title: "交流输电线路 (AC Transmission Line)"
type: model
tags: [ac-transmission, overhead-line, power-transmission, line-modeling, emt]
created: "2026-05-04"
updated: "2026-05-17"
---

# 交流输电线路 (AC Transmission Line)

## 定义与边界

交流输电线路是用于传输电能的架空导线系统，通常由三相导线、地线（避雷线）、绝缘子串和杆塔组成。在EMT仿真中，交流输电线路模型需要考虑分布参数特性、频变效应、多导体耦合和地回路影响，以准确模拟正常运行和暂态过程。

**边界限定**：本页面聚焦于交流架空线路的EMT建模，不包括电缆线路或直流输电线路。

## EMT中的作用

交流输电线路是电力系统EMT仿真的核心元件：

- **工频潮流**：稳态电压分布和无功功率传输
- **暂态过电压**：操作过电压、雷击过电压的传播
- **故障分析**：短路故障的电流行波和传播
- **稳定性研究**：机电振荡和功率摇摆
- **谐波分析**：谐波在电网中的传播和放大

## 核心机制：电报方程与解耦变换

### 电报方程（分布参数模型）

交流线路的分布参数方程描述电压和电流沿线路的传播：

$$-\frac{\partial \mathbf{v}}{\partial x} = \mathbf{Z}' \mathbf{i} \quad (1)$$
$$-\frac{\partial \mathbf{i}}{\partial x} = \mathbf{Y}' \mathbf{v} \quad (2)$$

其中 $\mathbf{Z}' = \mathbf{R}' + j\omega\mathbf{L}'$ 为单位长度串联阻抗矩阵，$\mathbf{Y}' = \mathbf{G}' + j\omega\mathbf{C}'$ 为单位长度并联导纳矩阵。联立求解可得波动方程：

$$\frac{\partial^2 \mathbf{v}}{\partial x^2} = \mathbf{Z}' \mathbf{Y}' \mathbf{v} = \boldsymbol{\Gamma}^2 \mathbf{v} \quad (3)$$

其中 $\boldsymbol{\Gamma} = \sqrt{\mathbf{Z}' \mathbf{Y}'} = \boldsymbol{\alpha} + j\boldsymbol{\beta}$ 为传播常数矩阵，$\boldsymbol{\alpha}$ 为衰减常数，$\boldsymbol{\beta}$ 为相位常数。

### 多导体耦合矩阵

三相导线的耦合阻抗矩阵：

$$\mathbf{Z}' = \begin{bmatrix} Z_{aa}' & Z_{ab}' & Z_{ac}' \\ Z_{ba}' & Z_{bb}' & Z_{bc}' \\ Z_{ca}' & Z_{cb}' & Z_{cc}' \end{bmatrix} \quad (4)$$

该矩阵对称且一般情况下为满阵，三相电压和电流相互耦合。通过模态变换（Clarke变换或对称分量变换）可将其解耦为三个独立的模态分量：

$$\mathbf{v}_m = \mathbf{T}^{-1} \mathbf{v}, \quad \mathbf{i}_m = \mathbf{T}^{-1} \mathbf{i} \quad (5)$$

其中 $\mathbf{T}$ 为变换矩阵。解耦后各模态独立传播，传播常数和特性阻抗分别为：

$$\gamma_m = \sqrt{Z_m' Y_m'}, \quad Z_{c,m} = \sqrt{\frac{Z_m'}{Y_m'}} \quad (6)$$

**Clarke变换**（等幅变换）：

$$\mathbf{T}_C = \frac{2}{3} \begin{bmatrix} 1 & -\frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{\sqrt{3}}{2} & -\frac{\sqrt{3}}{2} \\ \frac{1}{2} & \frac{1}{2} & \frac{1}{2} \end{bmatrix} \quad (7)$$

经Clarke变换解耦后，三相线路变为 $\alpha$、$\beta$、$0$ 三个独立模态，其中 $\alpha$ 和 $\beta$ 为传播模态，$0$ 为静电模态（不传播，仅涉及对地电容充放电）。对于完全换位的线路，解耦效果理想，各模态可独立求解后再通过反变换还原三相量。

### 特性阻抗与传播常数

特性阻抗矩阵：

$$\mathbf{Z}_c = \sqrt{\frac{\mathbf{Z}'}{\mathbf{Y}'}} \quad (8)$$

对于无损耗线路（$R'=0, G'=0$），特性阻抗为纯电阻：

$$Z_c = \sqrt{\frac{L'}{C'}} \quad (9)$$

传播常数 $\gamma = \alpha + j\beta = \sqrt{Z' Y'}$ 的实部 $\alpha$ 决定衰减量，虚部 $\beta$ 决定相位速度。相速度：

$$v_p = \frac{\omega}{\beta} = \frac{1}{\sqrt{L' C'}} \quad (10)$$

在工频下（$\omega = 2\pi \times 50/60$ rad/s），无损耗线路的相速度接近光速 $c \approx 3\times 10^8$ m/s。

### ABCD参数（二端口网络表示）

用二端口网络描述长度为 $l$ 的线路：

$$\begin{bmatrix} \mathbf{V}_S \\ \mathbf{I}_S \end{bmatrix} = \begin{bmatrix} \mathbf{A} & \mathbf{B} \\ \mathbf{C} & \mathbf{D} \end{bmatrix} \begin{bmatrix} \mathbf{V}_R \\ \mathbf{I}_R \end{bmatrix} \quad (11)$$

其中：

$$\mathbf{A} = \mathbf{D} = \cosh(\boldsymbol{\Gamma} l) \quad (12)$$
$$\mathbf{B} = \mathbf{Z}_c \sinh(\boldsymbol{\Gamma} l) \quad (13)$$
$$\mathbf{C} = \mathbf{Y}_c \sinh(\boldsymbol{\Gamma} l) = \mathbf{Z}_c^{-1} \sinh(\boldsymbol{\Gamma} l) \quad (14)$$

当线路无损耗时，$\cosh(\gamma l) = \cosh(j\beta l) = \cos(\beta l)$，$\sinh(\gamma l) = j\sin(\beta l)$，ABCD矩阵的各元素变为纯实数或纯虚数，便于计算。

## EMT建模方法体系

### 方法1：集中参数π型模型（短线路）

对于长度 $l < 80$ km 的短线路，忽略分布电容效应，将线路等效为集中参数串联阻抗：

$$\mathbf{Z}_L = \mathbf{Z}' l = (\mathbf{R}' + j\omega\mathbf{L}')l \quad (15)$$

精确的集中参数模型需在线路两端各并联一半对地电容：

$$\mathbf{Y}_{sh} = \frac{\mathbf{Y}' l}{2} = \frac{(\mathbf{G}' + j\omega\mathbf{C}')l}{2} \quad (16)$$

**等效电路**：发送端串联阻抗后接并联导纳，接收端相同。对称布置便于网络方程的稀疏求解。

**适用条件**：线路长度远小于波长（$l \ll \lambda = v_p/f$），即 $l < 0.1\lambda$。工频50Hz下，$0.1\lambda \approx 600$ km，故短于约80 km的线路可用此模型。

### 方法2：Bergeron等效（中长线路，频变效应次要）

Bergeron模型是 EMT 仿真中最广泛使用的线路模型之一，通过历史电流源等效分布参数：

$$\mathbf{i}_{R}^{(n+1)} = \mathbf{Y}_c \mathbf{v}_R^{(n+1)} + \mathbf{H} \mathbf{i}_{inc}^{(n)} \quad (17)$$

其中 $\mathbf{Y}_c = \mathbf{Z}_c^{-1}$ 为特性导纳矩阵，$\mathbf{H} = e^{-\boldsymbol{\Gamma} l}$ 为传播函数矩阵（对角元素为 $e^{-\gamma_m l}$），$\mathbf{i}_{inc}$ 为入射电流历史项。接收端电流可表示为：

$$\mathbf{i}_R^{(n+1)} = \mathbf{Y}_c \mathbf{v}_R^{(n+1)} - 2\mathbf{H}_R \mathbf{i}_{inc,R}^{(n)} \quad (18)$$

该模型在时域递推时不引入卷积运算，仅需存储有限个历史电流值，计算效率高。**Torrez Caballero (2015)** 指出，基于Bergeron方法的频变多导体线路模型通过矢量拟合（Vector Fitting）近似频变特性，可将电路节点数减少约 **60%**，同时消除高频数值振荡。

**传播延迟**：多导体系统的各模态传播速度不同，存在**模态时延差**（$\Delta\tau = |\tau_\alpha - \tau_0|$）。对于完全换位线路，$\alpha$ 和 $\beta$ 模态传播速度相同（等于光速），$0$ 模态静止（无传播）。因此Bergeron模型的时延取最大模态时延 $\tau = l/v_p$。

**适用条件**：中长线路（80 km ~ 400 km），开关操作和短路的电磁暂态分析，不要求宽频高精度时。

### 方法3：JMarti频变模型（宽频分析）

JMarti模型是商业EMTP软件（如PSCAD、ATP）中最常用的频变线路模型，通过在频域拟合传输函数实现宽频精确建模：

$$Y_{mart}(s) \approx \sum_{k=1}^{N} \frac{r_k}{s + p_k} + d + es \quad (19)$$

式中，$r_k$ 和 $p_k$ 为矢量拟合得到的留数和极点，$d$ 为直接导纳项，$e$ 为附加导纳系数。通过分部分式展开可将每个RL分支与电容并联，形成等效电路：

$$Z_k(s) = \frac{R_k s + R_k R_k'/L_k'}{s + R_k'/L_k'} \quad (20)$$

其中每个分支对应一个物理RL网络，可直接嵌入EMTP的节点分析方程。

**矢量拟合过程**：对数域拟合 $Z_c(\omega)$ 和 $\gamma(\omega)$ 的频率响应数据，求解线性最小二乘问题得到有理函数逼近。**Gustavsen (2002)** 的矢量拟合算法通过迭代重加权最小二乘确保极点稳定性，典型拟合阶数 $N=6\sim 10$。

**适用条件**：需要精确模拟雷击高频暂态（~1 MHz）、谐波传播（~3 kHz）、开关操作暂态的全频段响应的场景。

### 方法4：小波变换建模（非均匀线路）

**Ali Abur (2001)** 提出了基于离散小波变换（DWT）的非均匀输电线路时域建模方法，将频变特性分解到多个小波尺度：

$$G^{(k)} = (\mathbf{T}_v^{(k)})^{-1} \mathbf{G}_m^{(k)} \mathbf{T}_v^{(k)} \quad (21)$$

其中 $G = \mathbf{Y}_{bus}$ 为网络节点导纳矩阵，$k$ 为小波尺度（对应频率范围），$\mathbf{T}_v^{(k)}$ 为尺度相关的变换矩阵。该方法在 **50 μs** 仿真步长下，采用Daubechies小波（5个尺度，起始频率75 kHz），对50英里线路进行仿真，RMSE误差降低超过 **60%**，峰值偏差从4.2%降至1.8%。

**非均匀线路专用**：当线路参数沿线变化（如高度变化、弧垂变化）时，采用分段的Bergeron或JMarti模型，每段独立计算后通过链式矩阵连接：

$$\begin{bmatrix} \mathbf{V}_S \\ \mathbf{I}_S \end{bmatrix} = \mathbf{M}_1 \mathbf{M}_2 \cdots \mathbf{M}_N \begin{bmatrix} \mathbf{V}_R \\ \mathbf{I}_R \end{bmatrix} \quad (22)$$

其中 $\mathbf{M}_i = \begin{bmatrix} \mathbf{A}_i & \mathbf{B}_i \\ \mathbf{C}_i & \mathbf{D}_i \end{bmatrix}$ 为第 $i$ 段的双曲函数矩阵。**Ramirez (2001)** 指出，对高度变化26.2m→15.24m的非均匀线路，常参数MC（等分为7段）方法的误差为 **20%~30%**（当线路总长>2km时），而采用非均匀线路专用模型可准确模拟低频谐振（约5 kHz）和电压波动（0.2~0.3 p.u.）。

### 方法5：模态域建模（相域→模域解耦）

通过模态变换将相域耦合方程解耦为三个独立模态（$\alpha$、$\beta$、$0$），各模态独立求解后再转换回相域。**Colqui (2022)** 在ATP-EMTP中用理想变压器阵列实现Clarke变换：

$$\mathbf{Y}_{modal} = \mathbf{L}^{-1} \mathbf{Y}_{nodal} \mathbf{L} = \text{diag}(Y_\alpha, Y_\beta, Y_0) \quad (23)$$

其中 $\mathbf{L}$ 为Clarke变换矩阵（在EMTP中用变压器网络实现），$\mathbf{Y}_{nodal}$ 为相域节点导纳矩阵。解耦后，各模态可直接应用Bergeron或JMarti模型，等效为三个独立的单导体线路。

**矢量拟合在模态域的应用**：对解耦后的各模态特性阻抗和传播常数分别进行矢量拟合，拟合阶数可降低（各模态独立拟合，总计算量减少）。

## EMT建模方法对比

| 建模方法 | 适用场景 | 时间尺度 | 计算效率 | 精度 | 关键挑战 |
|----------|----------|----------|----------|------|----------|
| 集中参数π型 | 短线路 <80 km | 工频稳态 | 极高 | 低 | 忽略分布效应 |
| Bergeron | 中长线路 80~400 km | 开关暂态 | 高 | 中 | 模态时延差处理 |
| JMarti（矢量拟合） | 长线路、宽频分析 | 雷击、谐波 | 中 | 高 | 拟合阶数与稳定性 |
| 小波变换 | 非均匀线路 | 多尺度暂态 | 中低 | 高 | 小波基选择、尺度数 |
| 模态域（Clarke） | 多导体解耦 | 全频段 | 中 | 高 | 变压器网络实现 |

## 关键技术挑战

### 挑战1：集肤效应与交流电阻增加

导线内部的集肤效应使电流趋向表面分布，等效交流电阻大于直流电阻：

$$R_{ac}(\omega) = R_{dc} \cdot F_{skin}(\omega) \quad (24)$$

其中 $F_{skin}(\omega) > 1$ 且随频率增加。在雷击电流高频分量（~1 MHz）下，集肤效应使有效导电截面积大幅减小，电阻增加可达直流电阻的数倍。

### 挑战2：地回路频变阻抗（Carson理论）

架空线路的地回路返回路径不是理想导体，而是有有限电阻率的大地。Carson (1926) 给出了大地返回阻抗的一阶近似公式：

$$Z_g' \approx \frac{j\omega \mu_0}{2\pi} \left[ \ln\left(\frac{2h}{r} + \sqrt{1+\frac{4h^2}{r^2}}\right) - \frac{2h}{r} + \frac{1}{2} + j\frac{\pi}{2}\right] \quad (25)$$

其中 $h$ 为导线对地高度，$r$ 为导线半径。在高频下，大地返回路径呈现明显的频率相关性，且大地电阻率 $\rho$ 对阻抗影响显著（$\rho = 100\sim 1000$ Ω·m 时，误差差异可达数十个百分点）。

**Pollaczek公式**（更精确的积分形式）：

$$Z_g' = \frac{j\omega \mu_0}{2\pi} \int_{-\infty}^{\infty} \frac{e^{-2h|\lambda|}}{|\lambda| + \sqrt{\lambda^2 + j\omega\mu_0/\rho}} d\lambda \quad (26)$$

该积分需数值求解，计算成本较高。在EMTP中通常用Carson近似或数值积分表查询。

### 挑战3：电晕效应（高电压）

电晕放电改变线路的有效电容和对地电导。高电压下，电晕增加等效对地电容（$C'_{eff} > C'$）和有功损耗（$G' > 0$）。电晕引起的等效电路是非线性的，通常用分段线性等效或时域电晕模型近似。

**Kurokawa (2005)** 提出的线路参数反演方法，可从测量数据（而非几何参数）直接推算等效电容和电导，绕过了电晕效应建模的困难：对440 kV/500 km线路，误差 < **0.5%**。

### 挑战4：线路换位与三相不平衡

理想换位（三相参数对称）时，耦合矩阵经模态变换完全解耦。实际线路换位不理想或不换位时，三相参数不对称，模态变换解耦不彻底，导致 $\alpha$、$\beta$、$0$ 模态间存在残余耦合，需用完整的 $3\times3$ 耦合系统而非解耦后的三个独立单导体模型。

### 挑战5：非均匀线路与分段建模

当线路高度、弧垂、导线半径沿线变化时，不能用单一均匀线路模型描述。常用处理方法：

1. **分段均匀化**：将线路分为 $N$ 个均匀子段，每段用Bergeron/JMarti模型，各子段链式连接（式22）
2. **等效非均匀模型**：用等效的频率相关参数代替真实非均匀参数，需频率扫描拟合

**Ramirez (2001)** 的研究表明，对高度变化超过25%的线路（26.2m→15.24m），分段数过少（$<10$段）会导致 **20%~30%** 的误差，需要至少分15段才能保证精度。

## 量化性能边界

### 实时仿真性能

| 实现平台 | 模型类型 | 步长 | 线路规模 | 精度 | 来源 |
|----------|----------|------|----------|------|------|
| FPGA (Chen & Dinavahi 2009) | 全频变FD（15条线路） | 12 μs | 15条线路 | 峰值误差<0.5%，相位偏差<0.2° | 单片FPGA，两级并行 |
| FPGA (Liu 2021) | FDPD频变相域 | 2.4~3.27 μs | — | 加速15~20× vs 处理器 | Xilinx VC707/VCU118 |

### 数值精度

| 方法 | 测试条件 | 误差指标 | 量化结果 |
|------|----------|----------|----------|
| Kurokawa参数反演 | 440 kV/500 km, Grosbeak导线, ρ=1000 Ω·m | 相对误差 | **<0.5%** vs Carson/Pollaczek |
| Abur小波建模 | 50英里线路, 50μs步长, 5尺度Daubechies | RMSE | **降低>60%**，峰值偏差4.2%→1.8% |
| Ramirez非均匀线路 | 高度变化26.2m→15.24m, 7段MC vs 非均匀模型 | 误差对比 | **20%~30%**（线路>2km时MC误差） |
| Colqui模态域Bergeron | 完全换位三相线路 | 精度vs频变 | 等效精度，不改变数值精度 |
| FLE (Colqui 2022) | 300m线路, ~1μs传播延迟 | NRMSD | **0.1%~0.8%**，步长可达传播延迟的400% |

### 半波长线路特性

| 参数 | 数值 | 说明 |
|------|------|------|
| 传播延迟 $\tau$ | ≈10 ms | 对应工频半周期（匹配机电暂态步长） |
| 分段长度 | 300 km | 产生约1 ms传播延迟 |
| 切换阈值 $\xi$ | $1.0\times 10^{-4}$ | 变步长判定阈值（张彦涛 2017） |

### MMC-HVDC高频振荡（与交流线路的谐波交互）

| 参数 | 数值 | 说明 |
|------|------|------|
| 链路延时 | 550 μs | MMC控制链路典型延时 |
| 振荡频率 | 660 Hz, 700 Hz, 1270 Hz, 1.8 kHz | 不同模式下的谐振频率 |
| 延时-谐振关系 | 165 μs临界延时阈值 | 350 μs→1850 Hz, 550 μs→720 Hz |
| 失稳主因 | 内环+电压前馈 | 贡献 >75% 失稳能量（Li 2021） |

## 适用边界与选择指南

### 场景→方法决策表

| 应用场景 | 推荐模型 | 不适用模型 | 原因 |
|----------|----------|------------|------|
| 工频潮流计算（稳态） | π型集中参数 | 频变模型 | 精度要求低，计算简洁优先 |
| 开关操作暂态（<10 kHz） | Bergeron | π型 | 需要传播延迟和分布效应 |
| 雷击过电压（>100 kHz） | JMarti/FD | Bergeron, π型 | 宽频特性决定精度 |
| 谐波分析（~3 kHz） | JMarti | π型 | 次谐波频率响应 |
| 非均匀线路（地形变化） | 分段Bergeron或小波 | 单段Bergeron | 非均匀导致误差20~30% |
| 非对称故障（换位不理想） | 多导体相域或频变 | 对称分量解耦 | 解耦不完全导致误差 |
| 实时仿真（硬件加速） | Bergeron或FLE | JMarti（计算重） | FLE步长可达传播延迟400% |
| 半波长交流输电 | 动态相量+可变步长 | 固定步长 | 传播延迟≈10ms，机电-电磁时间尺度耦合 |

### 失效模式汇总

| 失效场景 | 受影响模型 | 表现 | 应对策略 |
|----------|------------|------|----------|
| 线路过长（>600 km） | π型集中参数 | 虚假容性无功 | 使用Bergeron或JMarti |
| 高频谐波（>10 kHz） | π型和Bergeron | 忽略频变导致误差大 | 使用JMarti或小波 |
| 大地电阻率高（ρ>500 Ω·m） | Carson近似 | 地回路阻抗误差大 | 使用Pollaczek数值积分 |
| 电晕放电显著 | 所有线性模型 | 等效电容/电导非线性 | 使用非线性电晕模型 |
| 导线非圆柱（钢芯铝绞线） | 简化GMR | 集肤效应估算偏差 | 查表法或测量数据 |

## 经典公式汇总

**单位长度电感**（GMD-GMR公式）：

$$L' = 2\times 10^{-7} \ln\frac{GMD}{GMR} \quad \text{(H/m)} \quad (27)$$

其中几何平均距离（GMD）：

$$GMD = \sqrt[3]{D_{ab} D_{bc} D_{ca}} \quad (28)$$

**开路/短路等效阻抗**（参数测量反演）：

$$Z_{eq,open} = Z_c \coth(\gamma l), \quad Z_{eq,short} = Z_c \tanh(\gamma l) \quad (29)$$

通过测量开路和短路阻抗，可反推特性阻抗和传播常数：

$$\gamma l = \frac{1}{2} \ln\left(\frac{1+X}{1-X}\right), \quad X = \sqrt{\frac{Z_{eq,open}}{Z_{eq,short}}} \quad (30)$$

然后 $Z_c = \sqrt{Z_{eq,open} Z_{eq,short}}$，$z = \gamma Z_c$，$y = \gamma/Z_c$。

**Bergeron等效诺顿电流源**：

$$i_R^{(n+1)} = \frac{v_R^{(n+1)}}{Z_c} + H \cdot i_{inc}^{(n)} \quad (31)$$

该递推公式是EMTP中最常用的线路等效形式，每次迭代只需一次乘加运算，无需卷积。

## 相关页面

- [[transmission-line-model]] - 输电线路模型综合
- [[distributed-parameter-model]] - 分布参数理论
- [[frequency-dependent-line-model]] - 频变线路模型
- [[earth-return-impedance]] - 地回路阻抗
- [[bergeron-line-model]] - Bergeron数值模型
- [[vector-fitting]] - 矢量拟合（频变模型的核心算法）

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-wavelet-transform-based-method-for-improved-modeling-of-transmission-lines-pow]] | 2001 |
| [[modeling-nonuniform-transmission-lines-for-time-domain-simulation-of-electromagn]] | 2001 |
| [[a-new-procedure-to-derive-transmission-line-parameters-applications-and-restrict]] | 2005 |
| [[frequency-dependent-multiconductor-line-model-based-on-the-bergeron-method]] | 2015 |
| [[dynamic-performance-of-embedded-hvdc-with-13&14]] | 2015 |
| [[half-wavelength-system-transients-stability-simulation-using-dynamic-phasor-mode]] | 2017 |
| [[mmc-hvdc系统高频稳定性分析与抑制策略(一)稳定性分析]] | 2021 |
| [[a-modified-implementation-of-the-folded-line-equivalent-transmission-line-model-]] | 2022 |
| [[characteristic-analysis-of-high-frequency-resonance-of-flexible-high-voltage-dir]] | 2022 |