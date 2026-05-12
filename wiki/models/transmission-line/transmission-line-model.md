---
title: "输电线路模型 (Transmission Line)"
type: model
tags: [transmission-line, bergeron, frequency-dependent, traveling-wave]
created: "2026-04-13"
updated: "2026-05-12"
---

# 输电线路模型 (Transmission Line)

## 概述

输电线路是电力系统中分布范围最广的元件，其电磁暂态特性对系统仿真精度有重要影响。准确的线路模型需要考虑频率相关参数、分布参数特性和行波传播效应。

## 主要模型类型

### 1. Bergeron模型
- 恒定参数的行波模型
- 无损耗线路假设
- 计算简单，EMTP标准模型
- 忽略频率相关性

### 2. 频变线路模型
- 考虑集肤效应和大地回路
- 参数随频率变化
- 模域变换解耦
- 矢量拟合实现

### 3. π型等值电路
- 集中参数近似
- 适用于短时线路
- 精确等值π电路
- 可变步长仿真算法

### 4. 多导体线路
- 三相耦合线路
- 非平行多导体
- 模态分解方法
- 交叉换位效应

## 频率相关特性

### 集肤效应
- 导线电阻随频率增加
- 内部电感减小

### 大地回路
- Carson公式
- 土壤电阻率影响
- 频率相关大地返回阻抗

### 模态变换
- 相域→模域解耦
- 频率相关变换矩阵
- 常数变换矩阵近似

## 特殊问题

- 截断电荷效应（线路开断）
- 电晕效应（高压线路）
- 半波长线路暂态
- 混合线路（架空线+电缆）

## 相关方法
- [[vector-fitting]]
- [[passivity-enforcement]]
- [[numerical-integration]]

## 相关模型
- [[cable-model|电缆模型]] - 架空线与电缆对比
- [[fdne-model|频变网络等值(FDNE)]] - 线路网络等值
- [[transformer-model|变压器模型]] - 线路-变压器接口
- [[grounding-system-model|接地系统模型]] - 线路接地

## 相关主题
- [[frequency-dependent-modeling]]
- [[cable-modeling]]
- [[real-time-simulation]]
- [[parallel-computing]]
- [[network-equivalent]]

## 量化性能边界

**折叠线等效模型（FLE）大步长精度**（Colqui 2022）：
- 在300 m三相架空线路（传播延时约1 μs）上，改进FLE（MFLE）模型允许步长提升至传播延时的400%（4 μs vs 1 μs），归一化均方根偏差（NRMSD）控制在0.1%~0.8%
- 验证工况覆盖开路、负载投切及单相接地故障，对比基线为PSCAD ULM及ATP JMarti
- 矢量拟合采用20对共轭极点，通过Clarke矩阵电路实现三相线路模态解耦

**FPGA相域频变（FDPD）模型实时仿真性能**（Liu 2021）：
- 全流水线并行架构将实时仿真步长压缩至2.4 µs（8导体）~3.27 µs（12导体），较传统处理器大时间步长模型（约50 µs）提升约15~20倍
- 自定义48位浮点格式（32位尾数+16位指数）彻底消除32位单精度在长递归卷积中的数值发散问题
- VCU118平台资源占用：LUT 48.39%，DSP 47.08%，支持嵌入式和Bergeron接口两种模式
- 基于PSCAD/EMTDC离线基准与RTDS NovaCor实时平台验证

**ULM无源性强制策略效果**（Gustavsen 2008）：
- 三层防御：人工并联电导（时间常数1 s，截止频率0.159 Hz）+ 低通滤波（截止10 MHz，比典型拟合上界高一个数量级）+ 端口二阶校正（1.1倍放大因子确保收敛）
- 对三根145 kV单芯同轴电缆、长度1000 m的电缆系统，原始ULM因带外无源性违规产生时域发散，强制后仿真稳定
- 低频电导只影响0.159 Hz以下频段，二阶校正对非违规频段精度影响可忽略

**频变土壤模型对接地影响**（Schroeder 2018）：
- 纯电阻接地模型导致地电位升（GPR）计算误差达18%~25%，但绝缘子过电压误差<5%
- 土壤频变特性使接地冲击阻抗降低12%~20%，反击跳闸率下降约15%
- 频变效应对GPR的影响强度是绝缘子过电压的3~4倍
- 矢量拟合等效电路在EMTP/ATP中的仿真耗时仅为全波电磁模型的1/50，频域拟合误差<1%

**DWT多尺度频变线路模型精度**（Ozgun & Abur 2001）：
- 在50 μs固定步长与5个小波尺度（起始75 kHz）配置下，DWT模型重构波形RMSE较传统FD模型降低约60%
- 非换位线路工况下，恒定模变换矩阵引入的模态耦合误差导致FD模型峰值偏差达4.2%，DWT模型将误差控制在1.8%以内
- 首个行波到达时刻的电压过冲误差从FD模型的3.8%降至DWT模型的0.9%
- 稀疏DWT/IDWT矩阵运算使多尺度解算的计算开销仅增加约15%~20%

**非换位线路频变变换矩阵NR法精度**（Wedepohl 2004）：
- 全频段（1 Hz~1 MHz）模态变换矩阵元素有理函数拟合最大误差<1.0%
- NR法彻底消除传统算法的模态跳变现象，特征向量连续性满足最小相移有理函数拟合条件
- 验证基于垂直双回非换位架空线路（6相导线+地线）

**频变线路传播矩阵降阶效率**（Jeewantha & De Silva 2025）：
- 相域传播矩阵拟合误差控制在0.5%以内（ε_max = 0.5%）
- 初始模态拟合阶数最高达18阶，经模态截断（MT）或平衡截断（BT）后有效压缩
- BT方法提供严格的先验误差上界，并数学保证降阶后系统的渐近稳定性
- 模态时延分布：0.240 ms、0.297 ms、1.191 ms和1.195 ms（四组）
- 验证基于双回30 km三相地下电缆系统

**非均匀线路模型精度**（Ramirez 2001）：
- 对称三相7段非均匀线路（总长2185.4 m，高度变化26.2 m→15.24 m），传播函数频域基频f₀≈5 kHz
- 恒定参数特征线法（MC）与频变模型的偏差随线路长度增加而显著增大，长线路（>2 km）中MC误差可达20%~30%

**FDM/DC分区拟合直流校正**（Cervantes 2020）：
- 高频段：1 Hz~1 MHz（第一阶段拟合），低频段：0.001 Hz~1 Hz（第二阶段DC校正）
- 通过低阶有理函数校正项补偿直流附近拟合偏差，消除了大留数/极点比导致的数值不稳定问题
- 适用于HVDC线路/电缆宽频EMT仿真

**数据缺口声明**：FLE模型在大规模网络、强非线性终端及实时仿真平台下的推广性需要进一步验证。FPGA FDPD模型对大导体数（>12）和长期HIL闭环稳定性的验证尚未充分展开。DWT多尺度模型对母小波类型、尺度划分敏感性和数值稳定性缺乏系统性量化。非均匀线路模型对极端几何非均匀性和复杂接地结构的误差边界未充分报告。频变土壤模型的验证集中于138 kV线路雷击场景，对开关操作暂态、换流站接地网和实时仿真的适用性需进一步确认。

## 深度增强内容

 # 输电线路模型深度技术文档

## 1. 各类模型数学描述

### 1.1 Bergeron行波模型（恒定参数）

基于无损线假设的分布参数模型，通过特征线法将偏微分方程转化为常微分方程。

**电报方程**：
$$
\begin{aligned}
-\frac{\partial v(x,t)}{\partial x} &= -L\frac{\partial i(x,t)}{\partial t} \\
-\frac{\partial i(x,t)}{\partial x} &= -C\frac{\partial v(x,t)}{\partial t}
\end{aligned}
$$

**特征线方程**（时域等效电路基础）：
$$
v_k(t) - Z_c i_k(t) = v_m(t-\tau) + Z_c i_m(t-\tau)
$$

其中特征阻抗 $Z_c = \sqrt{L/C}$，传播时延 $\tau = l\sqrt{LC}$。该模型在EMTP中通过诺顿等效实现：
$$
i_k(t) = \frac{v_k(t)}{Z_c} - I_{hist,k}(t)
$$

**历史电流源**：
$$
I_{hist,k}(t) = -\frac{1}{Z_c}v_m(t-\tau) - i_m(t-\tau)
$$

### 1.2 频变线路模型（FD模型）

考虑集肤效应和大地回路导致的频变参数 $R(s)$、$L(s)$、$G(s)$。

**频域特征参数**：
$$
Z_c(s) = \sqrt{\frac{R(s) + sL(s)}{G(s) + sC(s)}}, \quad \gamma(s) = \sqrt{(R(s)+sL(s))(G(s)+sC(s))}
$$

**传播函数与特征导纳**：
$$
H(s) = e^{-l\gamma(s)}, \quad Y_c(s) = \frac{1}{Z_c(s)}
$$

**矢量拟合有理逼近**（Vector Fitting）：
$$
Y_c(s) \approx \sum_{k=1}^{N}\frac{r_k}{s-p_k} + d + se
$$

$$
H(s) \approx \sum_{k=1}^{N_h}\frac{r_{h,k}}{s-p_{h,k}}e^{-s\tau_k}
$$

**时域递归卷积**（Recursive Convolution）：
历史电流源通过指数函数递推更新，避免全卷积计算：
$$
I_{hist}(t) = \sum_{k} h_k(t) * i(t) \approx \sum_{k} \alpha_k i(t-\Delta t) + \beta_k I_{hist,k}(t-\Delta t)
$$

### 1.3 通用线路模型（ULM）——相域实现

直接在相域建立模型，避免模态变换误差，适用于非对称线路。

**相域端口方程**：
$$
I_{ph}(s) = Y_c(s)V_{ph}(s) - H(s)[Y_c(s)V_{ph}(s) + I_{ph}(s)]
$$

**状态空间实现**：
将频变元件转化为微分方程组：
$$
\dot{x}(t) = Ax(t) + Bu(t)
$$
$$
y(t) = Cx(t) + Du(t)
$$

其中状态变量 $x$ 包含有理逼近引入的辅助变量，维度等于极点总数 $N_{poles}$。

### 1.4 折叠线等效模型（Folded Line Equivalent）

突破传统模型步长限制 $\Delta t < \tau$，允许大步长仿真。

**复频域插值**：
通过动态相量变换 $e^{-j\omega_0 t}$ 处理额定频率分量，历史电流采用复数插值：
$$
I_{hist}(t) = \text{Re}\left\{ \tilde{I}_{hist}(t) e^{j\omega_0 t} \right\}
$$

**大步长适用性**：
允许 $\Delta t > \tau$，通过等效电路重构实现：
$$
Y_{eq} = Y_c \cdot \frac{1+e^{-2\gamma l}}{1-e^{-2\gamma l}}
$$

### 1.5 非均匀线路模型（参数沿线变化）

针对阻抗指数变化的线路（如电缆接头、渐变线）：

**参数分布假设**：
$$
Z(x) = Z_0 e^{qx}, \quad Y(x) = Y_0 e^{-qx}
$$

**二端口频域解**：
$$
\begin{bmatrix} V_2 \\ I_2 \end{bmatrix} = \begin{bmatrix} \cosh(\theta) & -Z_{c,eq}\sinh(\theta) \\ -\frac{1}{Z_{c,eq}}\sinh(\theta) & \cosh(\theta) \end{bmatrix} \begin{bmatrix} V_1 \\ I_1 \end{bmatrix}
$$

其中 $\theta = \sqrt{ZY}\cdot l$，等效特征阻抗 $Z_{c,eq} = \sqrt{Z_0/Y_0}\cdot\frac{1}{\sqrt{1+(q/2\gamma)^2}}$

### 1.6 电晕效应电压相关模型

考虑电晕导致的非线性并联电容：

**电压相关电容**：
$$
C(v) = C_0 + \Delta C(v)
$$

**空间离散化**：
将线路离散为长度 $\Delta x \leq 50\text{m}$ 的段，每段集总参数随电压变化：
$$
i_{corona}(t) = C(v(t))\frac{dv(t)}{dt}
$$

**无迭代求解**：
通过预测-校正技术避免非线性迭代，步长采用ns量级（$\Delta t \sim 10\text{ns}$）。

---

## EMT中的作用

输电线路模型 (Transmission Line) 在EMT仿真中主要用于：

- **建模对象**：描述输电线路模型 (Transmission Line)在电力系统中的物理角色和电气特性
- **仿真场景**：适用于输电线路模型 (Transmission Line)相关的电磁暂态分析、故障响应、控制交互等场景
- **模型接口**：提供输电线路模型 (Transmission Line)的端口变量、状态方程和边界条件
- **验证基准**：可作为输电线路模型 (Transmission Line)仿真模型正确性的验证基准
## 数学模型

### 基本方程

输电线路模型 (Transmission Line)的数学模型基于以下基本物理定律：

$$
\text{待补充：基于输电线路模型 (Transmission Line)的物理特性建立数学描述}
$$

### 状态空间表示

$$
\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \mathbf{u})
$$

$$
\mathbf{y} = \mathbf{g}(\mathbf{x}, \mathbf{u})
$$

其中 $\mathbf{x}$ 为状态向量，$\mathbf{u}$ 为输入向量，$\mathbf{y}$ 为输出向量。
## 2. 仿真参数参考表

| 参数类别 | 参数值/范围 | 适用模型 | 典型应用 | 来源论文 |
|---------|------------|---------|---------|---------|
| **频率范围** | 0.01 Hz – 2 MHz | 频变土壤模型 | 雷电暂态分析 | 高频暂态与土壤频变 |
| | DC – 10 MHz | 宽带频变模型 | 开关过电压、GIS暂态 | 显式接地模型 |
| | 10 Hz – 1 MHz | 多相模域模型 | 工频及谐波暂态 | 多相模域模型 |
| **土壤参数** | $\rho = 100\ \Omega\cdot\text{m}$ | 常规土壤模型 | 一般输电线路 | 数值效率优化 |
| | $\rho = 1000-10000\ \Omega\cdot\text{m}$ | 频变土壤模型 | 高阻土壤、岩石地区 | 有损地线分析 |
| | $\varepsilon_r = 1-100$ (频变) | Nakagawa模型 | 高频地回路阻抗 | 土壤频变扩展 |
| **仿真步长** | $\Delta t = 2.4\ \mu\text{s}$ (8导体) | FPGA相域模型 | 实时仿真(RTDS) | FPGA相域实现 |
| | $\Delta t = 50-100\ \mu\text{s}$ | 状态空间模型 | 快慢暂态混合 | 对称/非对称配置 |
| | $\Delta t = 40-60\ \text{ms}$ | 折叠线模型 | 机电暂态 | 变步长算法 |
| | $\Delta t \leq 1\ \mu\text{s}$ | 电晕模型 | 雷击过电压 | 电晕效应模型 |
| **矢量拟合设置** | 极点数 $N = 8-20$ | ULM/FD模型 | 常规频变建模 | 电晕与频变耦合 |
| | 极点数 $N = 40$ (保守设置) | 频域分区拟合 | 高精度宽带模型 | 频域分区拟合 |
| | 最大误差 $\varepsilon_{max} < 0.5\%$ | 平衡截断降阶 | 降阶模型 | 数值效率优化 |
| | RMS误差 $< 0.1\%$ | 无源性强制 | 严格无源模型 | 无源性强制算法 |
| **线路离散化** | 段长 $\leq 50\text{m}$ | 电晕模型 | 空间电荷效应 | 电压相关电晕 |
| | 段长 $l/10 \sim l/20$ ($l$为总长) | $\pi$级联模型 | 行波传播 | 多相模域模型 |
| **无源性参数** | 人工电导时间常数 $\tau = 1\text{s}$ | 低频无源强制 | 直流偏移抑制 | 无源性强制 |
| | 低通截止 $f_c = 10^7\text{Hz}$ | 高频无源强制 | 避免高频发散 | 无源性强制 |
| | 品质因数Q修正 | RLC滤波器法 | 局部无源修正 | 改进无源算法 |

---

## 3. 模型选择指南

### 3.1 按暂态类型选择

| 应用场景 | 推荐模型 | 关键配置 | 精度指标 |
|---------|---------|---------|---------|
| **雷电过电压** (1-10 MHz) | 频变相域模型 + 频变土壤 | Nakagawa地回路公式，$\rho$频变 | 峰值误差<3%，波前时间误差<5% |
| **操作过电压** (100 Hz – 10 kHz) | 频变Bergeron模型 | 3-4个RL支路（低频） | 幅值误差<1.5% |
| **电力电子开关** (高频PWM) | FPGA相域模型 (FDPD) | 步长2.4-5.0 $\mu$s，48位浮点 | 实时性满足，量化误差消除 |
| **机电暂态** (0.1-10 Hz) | 折叠线等效模型 | 步长40-60 ms，复数插值 | 效率提升40-60倍 |
| **电晕效应分析** | 电压相关分布模型 | 空间离散≤50m，步长10ns | 非迭代求解，过电压低估修正27-49% |
| **混合线路** (架空+电缆) | 全频域参数模型 | 相模变换+改进NILT | 误差<0.3%，耗时减少40-70% |

### 3.2 按计算资源选择

**实时仿真/硬件在环(HIL)**：
- **首选**：FPGA相域频变模型（2.4-3.27 $\mu$s步长，48位自定义浮点）
- **备选**：Bergeron模型（大步长，嵌入式无接口模式5.0 $\mu$s）
- **避免**：传统模域ULM（变换矩阵计算延迟）

**大规模电网离线仿真**：
- **长线路/机电暂态**：折叠线模型（步长可大至传播时延400%，NRMSD<0.8%）
- **高精度电磁暂态**：降阶平衡截断模型（极点数压缩，误差<0.5%）
- **多回并行线路**：混合换位模型（利用块对角化，速度提升3.5-9.2倍）

**非对称/非换位线路**：
- **高精度**：相域模型（避免模态变换误差，恒定矩阵近似误差可>15%）
- **快速近似**：修正Clarke变换模型（实常数矩阵，高频误差<2°）

### 3.3 按土壤与接地特性选择

| 土壤条件 | 模型要求 | 关键公式/参数 |
|---------|---------|--------------|
| 低阻土壤 ($\rho < 300\ \Omega\cdot\text{m}$) | Carson公式足够 | $\sigma \gg \omega\varepsilon$，忽略位移电流 |
| 高阻土壤 ($\rho > 1000\ \Omega\cdot\text{m}$) | Nakagawa频变模型 | $\varepsilon_r$随频率变化(20-100)，Carson误差可达200% |
| 频变接地阻抗 | 矢量拟合等效电路 | 0.1Hz-1MHz拟合，接地冲击阻抗降低12-20% |
| 杆塔接地系统 | 显式接地模型 | 节点消除算法复杂度$O(\log_2 n)$ |

---

## 4. 前沿研究方向

### 4.1 模型降阶与计算效率优化

**模态截断(Modal Truncation, MT)与平衡截断(Balanced Truncation, BT)**：
- **技术要点**：对传播函数矩阵 $H(s)$ 进行汉克尔奇异值分解，删除弱可控/弱可观状态
- **性能提升**：原始62阶系统可降至20阶以下，提供严格先验误差界 $\|H - H_r\|_\infty \leq 2\sum_{i=r+1}^n \sigma_i$
- **稳定性保证**：BT方法数学保证降阶后系统特征值实部为负（渐近稳定）

**频率分区拟合(Frequency-Partitioning Fitting, FpF)**：
- 将宽频带划分为子区间分别拟合，避免病态条件数
- 相比传统VF，极点数减少15-20%，病态奇异值（$<10^{-15}$）处理成功率100%

### 4.2 无源性强制算法演进

**传统方法局限**：ULM在带外(out-of-band)可能出现负实部特征值，导致仿真发散。

**前沿方案**：
1. **人工电导法**：在对角线并联 $G_{add}$，时间常数1s（截止0.159Hz），消除低频违规
2. **RLC滤波器法**：并联无源RLC网络，局部修正品质因数Q，导纳修正误差$<6\times10^{-7}$
3. **高频渐近约束**：强制 $s\to\infty$ 时 $Y_c(s) \to D > 0$，确保高频无源性

### 4.3 硬件并行架构与实时仿真

**FPGA全流水线实现**：
- **架构**：相域递归卷积全并行化，自定义48位浮点（32位尾数+16位指数）
- **资源占用**：LUT 48.39%，DSP 47.08%（VCU118平台）
- **步长突破**：8导体线路2.4 $\mu$s，12导体2.8 $\mu$s，满足电力电子高频开关需求

**自动化代码生成**：
- 基于MANA（Modified Nodal Analysis）与FAMNM（Fast Associated Nodal Network Method）的自动化FPGA求解器
- 稀疏矩阵乘法器优化：Slice寄存器减少53.5%，DSP块减少86.2%

### 4.4 非线性与多物理场耦合

**电压-频率双重依赖模型**：
- 将电晕效应与频变特性耦合：$Y_c(s, v)$，$H(s, v)$
- 预计算耗时<0.6s（100电压采样点），仿真步长10ns
- 相比传统宽带模型，过电压预测误差降低27-49%

**电晕空间电荷动态**：
- 分布参数电晕模型，单位长度电容$C(v)$动态变化
- 非迭代节点电压求解，复杂度从$O(N_{iter}\cdot N^3)$降至$O(N^3)$

### 4.5 多速率与联合仿真接口

**RMS-EMT联合仿真**：
- 基于虚构传输线(Fictitious Transmission Line)的解耦接口
- 时间步长比1:100至1:1000（$\mu$s级EMT vs ms级RMS）
- 零缓冲快速曲线拟合算法，消除FFT固有20-40ms延迟

**跨平台协同**：
- FMI（Functional Mock-up Interface）标准实现OpenModelica与OpenDSS联合
- 稳定性判据：离散系统特征值$|\lambda|<1$（通过调整虚构线路阻抗$Z_c$实现）

### 4.6 特殊线路结构建模

**非平行多导体线路**：
- 分布源传输线(DSFTL)模型，考虑交叉角度$\alpha$（0°-90°任意角度）
- 散射场积分闭式解，计算速度较FDTD/FEM提升>1000倍

**混合线路(Overhead-Cable)**：
- 相模变换结合改进数值拉普拉斯逆变换(NILT)
- 突破$\Delta t < \tau$限制，计算耗时仅为传统FDPM的32-59%

**半波长线路与超长线路**：
- 精确考虑传播时延与相位常数，谐振频率定位精度<1%

### 4.7 开放研究问题

1. **宽频无源性保持**：如何在10 Hz - 10 MHz全频段严格保证无源性，同时避免过补偿导致的精度损失
2. **时变参数在线辨识**：基于量测数据的线路参数实时更新（温度、老化、覆冰导致的参数漂移）
3. **大规模并行效率**：>1000导体系统的降阶与并行分解算法
4. **量子计算应用**：线路特征值求解与模态分析的量子加速潜力
5. **数字孪生集成**：高频电磁暂态模型与SCADA/PMU数据的实时融合与校准

---
*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[耦合长线电磁暂态分析的扩展bergeron模型|耦合长线电磁暂态分析的扩展Bergeron模型]] | 1996 |
| [[new-multiphase-mode-domain-transmission-line-model|New multiphase mode domain transmission line model]] | 1999 |
| [[transmission-line-model-for-variable-step-size-simulation-algorithms|Transmission line model for variable step size simulation al]] | 1999 |
| [[a-wavelet-transform-based-method-for-improved-modeling-of-transmission-lines-pow|A wavelet transform-based method for improved modeling of tr]] | 2001 |
| [[frequency-dependent-transmission-line-modeling-utilizing-transposed-conditions-p|Frequency-dependent transmission line modeling utilizing tra]] | 2001 |
| [[modeling-nonuniform-transmission-lines-for-time-domain-simulation-of-electromagn|Modeling nonuniform transmission lines for time domain simul]] | 2001 |
| [[transmission-line-modeling-with-explicit-grounding-representation|Transmission Line Modeling with Explicit Grounding Represent]] | 2002 |
| [[zfunction-convolution-in-ehv|Z.function convolution in EHV]] | 2002 |
| [[a-simple-and-efficient-method-for-including-frequency-dependent-effects-in-trans|A simple and efficient method for including frequency-depend]] | 2003 |
| [[a-probabilistic-approach-for-secondary-arc-risk-assessment|A Probabilistic Approach for Secondary Arc Risk Assessment]] | 2004 |
| [[comparison-of-the-atp-version-of-the-emtp-and-the-netomac-program-for-simulation|Comparison of the ATP version of the EMTP and the NETOMAC pr]] | 2004 |
| [[computation-of-the-periodic-steady-state-in-systems-with-nonlinear-components-us|Computation of the periodic steady state in systems with non]] | 2004 |
| [[decision-tree-based-methodology-for-high-impedance-fault-detection|Decision tree-based methodology for high impedance fault det]] | 2004 |
| [[emtp-modeling-of-electromagnetic-transients-power-delivery-ieee-transactions-on|EMTP Modeling Of Electromagnetic Transients - Power Delivery]] | 2004 |
| [[frequency-dependent-transformation-matrices-for-untransposed-transmission-lines-|Frequency-Dependent Transformation Matrices for Untransposed]] | 2004 |
| [[modelling-of-single-phase-nonuniform-transmission-lines-in-electromagnetic-trans|Modelling of Single-Phase Nonuniform Transmission Lines in E]] | 2004 |
| [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i|Multi-port frequency dependent network equivalents for the E]] | 2004 |
| [[multiphase-power-flow-solutions-using-emtp-and-newtons-method-power-systems-ieee|Multiphase power flow solutions using EMTP and Newtons metho]] | 2004 |
| [[protection-system-representation-in-the-electromagnetic-transients-program-power|Protection system representation in the Electromagnetic Tran]] | 2004 |
| [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del|Rational approximation of frequency domain responses by vect]] | 2004 |
| [[real-time-digital-simulator-of-the-electromagnetic-transients-of-power-transmiss|Real-time digital simulator of the electromagnetic transient]] | 2004 |
| [[state-equation-approximation-of-transfer-matrices-and-its-application-to-the-pha|State equation approximation of transfer matrices and its ap]] | 2004 |
| [[suppression-of-numerical-oscillations-in-the-emtp-power-systems-power-systems-ie|Suppression of numerical oscillations in the EMTP power syst]] | 2004 |
| [[time-domain-modeling-of-external-systems-for-electromagnetic-transients-programs|Time domain modeling of external systems for electromagnetic]] | 2004 |
| [[using-tacs-functions-within-empt-to-teach-protective-relaying-fundamentals-power|Using TACS Functions Within EMPT To Teach Protective Relayin]] | 2004 |
| [[a-systematic-approach-to-the-evaluation|A Systematic Approach to the Evaluation]] | 2005 |
| [[a-new-procedure-to-derive-transmission-line-parameters-applications-and-restrict|A new procedure to derive transmission-line parameters Appli]] | 2005 |
| [[validation-of-frequency-dependent|Validation of Frequency-Dependent]] | 2005 |
| [[inclusion-of-frequency-dependent-soil-parameters-in|Inclusion of Frequency-Dependent Soil Parameters in]] | 2006 |
| [[2728nested-fast-and-simultaneous-solution-for-time-domain-simulation-of-integrat|Nested fast and simultaneous solution for time-domain simula]] | 2006 |
| [[potential-risk-of-failures-in-switching-ehv-shunt-reactors|Potential risk of failures in switching EHV shunt reactors]] | 2006 |
| [[电力系统机电暂态和电磁暂态混合仿真程序设计和实现|电力系统机电暂态和电磁暂态混合仿真程序设计和实现]] | 2006 |
| [[noda-a-binary-frequency-region-partitioning-algorithm-for-the-identification-of-|Noda | A Binary Frequency-Region Partitioning Algorithm for ]] | 2007 |
| [[real-time-transient-simulation-based-on-a-robust|Real-Time Transient Simulation Based on a Robust]] | 2007 |
| [[earth-return-impedance-of-overhead-and-underground-conductors-considering-earth-stratification-13&14|Earth Return Impedance of Overhead and Underground Conductor]] | 2008 |
| [[earth-return-impedances-of-conductor-arrangements-13&14|Earth Return Impedances of Conductor Arrangements]] | 2008 |
| [[passivity-enforcement-for-transmission-line-models|Passivity Enforcement for Transmission Line Models]] | 2008 |
| [[frequency-adaptive-power-system-modeling-for|Frequency-Adaptive Power System Modeling for]] | 2009 |
| [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb-fix|Interfacing Techniques for Transient Stability and Electroma]] | 2009 |
| [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb|Interfacing Techniques for Transient Stability and Electroma]] | 2009 |
| [[improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an-fix|Improvement of Numerical Stability for the Computation of Tr]] | 2010 |
| [[improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an|Improvement of Numerical Stability for the Computation of Tr]] | 2010 |
| [[robust-passivity-enforcement-scheme-for|Robust Passivity Enforcement Scheme for]] | 2010 |
| [[39pes20116039582|39/pes.2011.6039582]] | 2011 |
| [[analyses-of-the-modifications-in-the-pi-circuits-for-inclusion-of-frequency-infl|Analyses of the modifications in the pi circuits for inclusi]] | 2011 |
| [[application-of-pi-circuits-for-simulation-of-corona-effect-in-transmission-lines|Application of pi circuits for simulation of corona effect i]] | 2011 |
| [[digital-hardware-emulation-of-universal-machine-13&14|Digital Hardware Emulation of Universal Machine]] | 2011 |
| [[proposal-of-an-alternative-transmission-line-model-for-symmetrical-and-asymmetri|Proposal of an alternative transmission line model for symme]] | 2011 |
| [[a-novel-distance-protection-algorithm-in-frequency-domain-based-on-parameter-ide|A Novel Distance Protection Algorithm in Frequency Domain Ba]] | 2012 |
| [[modal-domain-based-modeling-of-parallel-transmission-lines|Modal Domain Based Modeling of Parallel Transmission Lines]] | 2012 |
| [[published-in-iet-generation-transmission-distribution|Multi-FPGA digital hardware design for detailed large-scale ]] | 2013 |
| [[published-in-iet-generation-transmission-distribution-27&28|Numerical Integration by the 2-Stage Diagonally Implicit Run]] | 2013 |
| [[dynamic-average-value-modeling-of-13&14|Dynamic Average-Value Modeling of]] | 2014 |
| [[fitting-the-frequency-dependent-parameters-in-the-bergeron-line-model|Fitting the frequency-dependent parameters in the Bergeron l]] | 2014 |
| [[parallel-massive-thread-electromagnetic-transient-simulation-on-gpu|Parallel Massive-Thread Electromagnetic Transient Simulation]] | 2014 |
| [[proximity-effect-in-fast-transient-simulations-of-an-underground-transmission-ca|Proximity effect in fast transient simulations of an undergr]] | 2014 |
| [[a-parallel-multi-rate-electromagnetic-transient-simulation-algorithm-based-on-ne|基于传输线分网的并行多速率电磁暂态仿真算法]] | 2014 |
| [[基于adpss的电力系统和牵引供电系统机电电磁暂态混合仿真|基于ADPSS的电力系统和牵引供电系统机电–电磁暂态混合仿真]] | 2014 |
| [[application-of-frequency-partitioning-fitting-to-the-phase-domain-frequency-depe|Application of Frequency-Partitioning Fitting to the Phase-D]] | 2015 |
| [[frequency-domain-simulation-of-electromagnetic-transients-using-variable|Frequency-Domain Simulation of Electromagnetic Transients Us]] | 2015 |
| [[frequency-dependent-multiconductor-line-model-based-on-the-bergeron-method|Frequency-dependent multiconductor line model based on the B]] | 2015 |
| [[modulation-index-dependent-thevenin-equivalent-circuit-model-of-vsc-and-apdr|Modulation Index Dependent Thévenin Equivalent Circuit Model]] | 2015 |
| [[transient-stability-analysis-of-mmc-hvdc-system-considering-dc-side-fault|Transient Stability Analysis of MMC-HVDC System Considering ]] | 2015 |
| [[an-automated-fpga-real-time-simulator-for-power-electronics-and-power-systems-el|An automated FPGA real-time simulator for power electronics ]] | 2016 |
| [[extension-of-a-modal-domain-transmission-line-model-for-including-frequency-depe|Extension of a modal-domain transmission line model for incl]] | 2016 |
| [[frequency-dependent-line-model-in-the-time-domain-for-simulation-of-fast-and-imp|Frequency-dependent line model in the time domain for simula]] | 2016 |
| [[influence-of-frequency-characteristics-of-soil-on-lightning-transient-response-o|Influence of frequency characteristics of soil on lightning ]] | 2016 |
| [[nonlinear-magnetic-equivalent-circuit-based-real-time-sen-transformer-electromag|Nonlinear Magnetic Equivalent Circuit-Based Real-Time Sen Tr]] | 2016 |
| [[2728multi-scale-and-frequency-dependent-modeling-of-electric-power-transmission-|Multi-scale and Frequency-dependent Modeling of Electric Pow]] | 2017 |
| [[a-full-frequency-dependent-line-model-based-on-folded-line-equivalencing-and-lat|A full frequency dependent line model based on folded line e]] | 2017 |
| [[a-novel-interfacing-technique-for-distributed-hybrid-simulations-combining-emt-a|A Novel Interfacing Technique for Distributed Hybrid Simulat]] | 2017 |
| [[dynamic-phasor-based-interface-model-for-emt-and-transient-stability-hybrid-simu|Dynamic Phasor Based Interface Model for EMT and Transient S]] | 2017 |
| [[modal-decoupling-of-overhead-transmission-lines-using-real-and-constant-matrices|Modal decoupling of overhead transmission lines using real a]] | 2017 |
| [[single-ended-travelling-wave-based-protection-scheme-for-double-circuit-transmis|Single-ended travelling wave-based protection scheme for dou]] | 2017 |
| [[accelerated-frequency-dependent-method-of-characteristics-for-the-simulation-of-|Accelerated frequency-dependent method of characteristics fo]] | 2018 |
| [[electromagnetic-disturbances-in-gas-insulated-substations-and-vft-calculations|Electromagnetic disturbances in gas-insulated substations an]] | 2018 |
| [[evaluation-of-the-impact-of-different-transmission-line-models-on-electromagneti|Evaluation of the impact of different transmission line mode]] | 2018 |
| [[fast-electromagnetic-transient-model-for-mmc-hvdc-considering-dc-fault|Fast Electromagnetic Transient Model for MMC-HVDC Considerin]] | 2018 |
| [[new-investigations-on-the-method-of-characteristics-for-the-evaluation-of-line-t|New investigations on the method of characteristics for the ]] | 2018 |
| [[partitioned-fitting-and-dc-correction-for-the-simulation-of-electromagnetic-tran|Partitioned Fitting and DC Correction for the Simulation of ]] | 2018 |
| [[real-time-fpga-rtds-co-simulator-for-power-systems|Real-Time FPGA-RTDS Co-Simulator for Power Systems]] | 2018 |
| [[38tpwrd20182794887|Time-Window Based Discrete-Time Fourier Series for Electroma]] | 2018 |
| [[a-harmonic-phasor-domain-co-simulation-method-and-new-insight-for-harmonic-analy|A Harmonic Phasor Domain Co-Simulation Method and New Insigh]] | 2020 |
| [[a-multi-area-thevenin-equivalent-based-multi-rate-co-simulation-for-control-desi|A multi-area Thevenin equivalent based multi-rate co-simulat]] | 2019 |
| [[a-multi-rate-co-simulation-of-combined-phasor-domain-and-time-domain-models-for-|A Multi-rate Co-simulation of Combined Phasor-Domain and Tim]] | 2019 |
| [[a-novel-linking-domain-extraction-decomposition-method-for-parallel-electromagne|A Novel Linking-Domain Extraction Decomposition Method for P]] | 2020 |
| [[a-novel-ultra-high-speed-traveling-wave-protection-principle-for-vsc-based-dc-gr|A Novel Ultra-High-Speed Traveling-Wave Protection Principle]] | 2019 |
| [[characteristics-and-optimal-configuration-of-capacitive-current-limiter-consider|Characteristics and Optimal Configuration of Capacitive Curr]] | 2020 |
| [[development-of-a-voltage-dependent-line-model-to-represent-the-corona-effect-in-|Development of a Voltage-Dependent Line Model to Represent t]] | 2020 |
| [[effect-of-frequency-dependent-soil-parameters-on-wave-propagation-and-transient-|Effect of frequency-dependent soil parameters on wave propag]] | 2020 |
| [[gpu-based-power-converter-transient-simulation-with-matrix-exponential-integrati|GPU-based power converter transient simulation with matrix e]] | 2020 |
| [[high-performance-computing-engines-for-the-fpga-based-simulation-of-the-ulm|High performance computing engines for the FPGA-based simula]] | 2020 |
| [[iet-generation-transmission-distribution|IET Generation, Transmission & Distribution]] | 2020 |
| [[mmc-upfc电磁-机电混合仿真技术研究|MMC-UPFC电磁-机电混合仿真技术研究]] | 2019 |
| [[partitioned-fitting-and-dc-correction-in-transmission-linecable-models-for-wideb|Partitioned fitting and DC correction in transmission line/c]] | 2020 |
| [[passivity-enforcement-of-wideband-line-model-through-coupled-perturbation-of-res|Passivity enforcement of wideband line model through coupled]] | 2020 |
| [[simulation-of-electromagnetic-transients-with-modelica-accuracy-and-performance-|Simulation of electromagnetic transients with Modelica, accu]] | 2020 |
| [[three-phase-adaptive-auto-reclosing-for-single-outgoing-line-of-wind-farm-based-|Three-phase Adaptive Auto-Reclosing for Single Outgoing Line]] | 2019 |
| [[time-domain-modeling-of-transmission-line-crossing-using-electromagnetic-scatter|Time-Domain Modeling of Transmission Line Crossing Using Ele]] | 2020 |
| [[a-study-on-interpolation-and-weighting-function-for-numerical-fourier-transform|A study on interpolation and weighting function for numerica]] | 2021 |
| [[an-accurate-analysis-of-lightning-overvoltages-in-mixed-overhead-cable-lines|An accurate analysis of lightning overvoltages in mixed over]] | 2021 |
| [[an-efficient-analytical-based-technique-to-numerical-calculation-of-extended-ear|An efficient analytical based technique to numerical calcula]] | 2021 |
| [[an-improved-passivity-enforcement-algorithm-for-transmission-line-models-using-p|An improved passivity enforcement algorithm for transmission]] | 2021 |
| [[compact-matrix-formulation-for-calculating-lightning-induced-voltages-on-electro|Compact Matrix Formulation for Calculating Lightning-Induced]] | 2021 |
| [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga-|Development of phase domain frequency-dependent transmission]] | 2021 |
| [[evaluation-of-the-extended-modal-domain-model-in-the-calculation-of-lightning-in|Evaluation of the extended modal-domain model in the calcula]] | 2021 |
| [[generalized-formulation-of-overhead-line-parameters-for-multi-layer-earth-19、20、21|Generalized Formulation of Overhead Line Parameters for Mult]] | 2021 |
| [[generalized-formulation-of-overhead-line-parameters-for-multi-layer-earth|Generalized Formulation of Overhead Line Parameters for Mult]] | 2021 |
| [[implementation-of-the-universal-line-model-in-the-alternative-transients-program|Implementation of the universal line model in the alternativ]] | 2021 |
| [[modal-propagation-characteristics-and-transient-analysis-of-multiconductor-cable|Modal propagation characteristics and transient analysis of ]] | 2021 |
| [[modeling-of-overhead-transmission-lines-for-trapped-charge-discharge-rate-studie|Modeling of overhead transmission lines for trapped charge d]] | 2021 |
| [[multi-scale-formulation-of-admittance-based-modeling-of-cables|Multi-scale formulation of admittance-based modeling of cabl]] | 2021 |
| [[real-time-rms-emt-co-simulation-and-its-application-in-hil-testing-of-protective|Real-time RMS-EMT co-simulation and its application in HIL t]] | 2021 |
| [[review-and-comparison-of-frequency-domain-curve-fitting-techniques-vector-fittin|Review and comparison of frequency-domain curve-fitting tech]] | 2021 |
| [[a-new-approach-to-represent-the-corona-effect-and-frequency-dependent-transmissi|A New Approach to Represent the Corona Effect and Frequency-]] | 2022 |
| [[a-modified-implementation-of-the-folded-line-equivalent-transmission-line-model-|A modified implementation of the Folded Line Equivalent tran]] | 2022 |
| [[acceleration-of-electromagnetic-transient-simulations-in-modelica-using-spatial-|Acceleration of electromagnetic transient simulations in mod]] | 2022 |
| [[accuracy-evaluation-of-electromagnetic-transients-simulation-algorithms|Accuracy Evaluation of Electromagnetic Transients Simulation]] | 2022 |
| [[average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail|Average-Value Modeling of Line-Commutated Inverter Systems W]] | 2022 |
| [[co-simulation-applied-to-power-systems-with-high-penetration-of-distributed-ener|Co-simulation applied to power systems with high penetration]] | 2022 |
| [[efficient-steady-state-analysis-of-the-grid-using-electromagnetic-transient-mode|Efficient steady state analysis of the grid using electromag]] | 2022 |
| [[electromechanical-electromagnetic-hybrid-simulation-technology-with-large-number|Electromechanical-electromagnetic Hybrid Simulation Technolo]] | 2022 |
| [[electromechanical-electromagnetic-transient-hybrid-simulation-of-an-acdc-hybrid-|Electromechanical-electromagnetic transient hybrid simulatio]] | 2022 |
| [[faster-than-real-time-hardware-emulation-of-extensive-contingencies-for-dynamic-|Faster-Than-Real-Time Hardware Emulation of Extensive Contin]] | 2022 |
| [[implementation-of-modal-domain-transmission-line-models-in-the-atp-software|Implementation of Modal Domain Transmission Line Models in t]] | 2022 |
| [[interfacing-real-time-and-offline-power-system-simulation-tools-using-udp-or-fpg|Interfacing real-time and offline power system simulation to]] | 2022 |
| [[low-complexity-graph-based-traveling-wave-models-for-hvdc-grids-with-hybrid-tran|Low-complexity graph-based traveling wave models for HVDC gr]] | 2022 |
| [[msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st|MSEMT: An Advanced Modelica Library for Power System Electro]] | 2022 |
| [[time-domain-coupling-model-for-nonparallel-frequency-dependent-overhead-multicon|Time-Domain Coupling Model for Nonparallel Frequency-Depende]] | 2022 |
| [[transient-analysis-on-multiphase-transmission-line-above-lossy-ground-combining-|Transient Analysis on Multiphase Transmission Line Above Los]] | 2022 |
| [[using-the-exact-equivalent-x03c0-circuit-of-transmission-lines-for-electromagnet|Using the Exact Equivalent &#x03C0;-Circuit of Transmission ]] | 2022 |
| [[2728基于电压源换流器的高压直流输电系统多尺度暂态建模与仿真研究|基于电压源换流器的高压直流输电系统多尺度暂态建模与仿真研究]] | 2022 |
| [[电力系统机电-电磁混合仿真边界解耦算法研究|电力系统机电-电磁混合仿真边界解耦算法研究]] | 2022 |
| [[电力系统电磁暂态实时仿真中并行算法的研究|电力系统电磁暂态实时仿真中并行算法的研究]] | 2022 |
| [[电力系统移频电磁暂态仿真原理及应用综述|电力系统移频电磁暂态仿真原理及应用综述]] | 2022 |
| [[a-new-tool-for-calculation-of-line-and-cable-parameters|A new tool for calculation of line and cable parameters]] | 2023 |
| [[accuracy-enhancement-of-shifted-frequency-based-simulation-using-root-matching-a|Accuracy Enhancement of Shifted Frequency-Based Simulation U]] | 2023 |
| [[admittance-based-modelling-of-cables-and-overhead-lines-by-idempotent-decomposit|Admittance-based modelling of cables and overhead lines by i]] | 2023 |
| [[algorithms-for-fast-calculation-of-energization-overvoltage-of-hybrid-overhead-l|Algorithms for fast calculation of energization overvoltage ]] | 2023 |
| [[alternative-method-to-include-the-frequency-effect-on-transmission-line-paramete|Alternative method to include the frequency-effect on transm]] | 2023 |
| [[an-enhanced-method-to-achieve-exact-dc-values-for-frequency-dependent-transmissi|An Enhanced Method to Achieve Exact DC Values for Frequency-]] | 2023 |
| [[an-investigation-of-electromagnetic-transients-for-a-mixed-transmission-system-w|An Investigation of Electromagnetic Transients for a Mixed T]] | 2023 |
| [[analysis-and-general-calculation-of-dc-fault-currents-in-mmc-mtdc-grids|Analysis and general calculation of DC fault currents in MMC]] | 2023 |
| [[benchmark-high-fidelity-emt-models-for-power|Benchmark High-Fidelity EMT Models for Power]] | 2023 |
| [[electromagnetic-transient-emt-simulation-algorithms-for-evaluation-of-large-scal|Electromagnetic Transient (EMT) Simulation Algorithms for Ev]] | 2023 |
| [[loop-closing-analytical-calculation-system-based-on-electromagnetic-electromecha|Loop closing analytical calculation system based on electrom]] | 2023 |
| [[modeling-and-simulation-of-vsc-hvdc-with-dynamic-phasors|Modeling and simulation of VSC-HVDC with dynamic phasors]] | 2023 |
| [[modeling-for-large-scale-offshore-wind-farm-using-multi-thread-parallel-computin|Modeling for large-scale offshore wind farm using multi-thre]] | 2023 |
| [[multi-conductor-cable-modeling-with-inclusion-of-measured-coaxial-wave-propagati|Multi-Conductor Cable Modeling With Inclusion of Measured Co]] | 2023 |
| [[parallelization-of-emt-simulations-for-integration-of-inverter-based-resources|Parallelization of EMT simulations for integration of invert]] | 2023 |
| [[passivity-enforcement-of-wideband-model-through-a-new-and-full-perturbation-form|Passivity enforcement of wideband model through a new and fu]] | 2023 |
| [[real-time-simulation-of-power-system-electromagnetic-transients-on-fpga-using-ad|Real-Time Simulation of Power System Electromagnetic Transie]] | 2023 |
| [[tower-foot-grounding-model-for-emt-programs-based-on-transmission-line-theory-an|Tower-foot grounding model for EMT programs based on transmi]] | 2023 |
| [[wideband-model-based-on-constant-transformation-matrix-and-rational-krylov-fitti|Wideband model based on constant transformation matrix and r]] | 2023 |
| [[交直流电力系统分割并行电磁暂态数字仿真方法|交直流电力系统分割并行电磁暂态数字仿真方法]] | 2023 |
| [[双导体有损频变均匀传输线的电磁暂态时域仿真模型研究|双导体有损频变均匀传输线的电磁暂态时域仿真模型研究]] | 2023 |
| [[a-waveform-dependence-lightning-impulse-corona-model-in-pscademtdc-for-investiga|A waveform-dependence lightning impulse corona model in PSCA]] | 2024 |
| [[advanced-wideband-linecable-modeling-for-transient-studies|Advanced Wideband Line/Cable Modeling for Transient Studies]] | 2024 |
| [[an-open-source-parallel-emt-simulation-framework|An open-source parallel EMT simulation framework]] | 2024 |
| [[an-ultra-fast-mmc-hvdc-fault-location-algorithm-based-on-transient-voltage-featu|An ultra-fast MMC-HVDC fault location algorithm based on tra]] | 2024 |
| [[assessment-of-the-accuracy-of-the-modal-domain-line-models-with-real-and-frequen|Assessment of the accuracy of the modal-domain line models w]] | 2024 |
| [[efficient-electromagnetic-transient-simulation-for-dfig-based-wind-farms-using-f|Efficient electromagnetic transient simulation for DFIG-base]] | 2024 |
| [[time-domain-modeling-of-a-subsea-buried-cable|Time-domain modeling of a subsea buried cable]] | 2024 |
| [[新能源电力系统细粒度并行与多速率电磁暂态仿真|新能源电力系统细粒度并行与多速率电磁暂态仿真]] | 2024 |
| [[a-julia-based-simulation-platform-for-power-system-transients|A Julia-based simulation platform for power system transient]] | 2025 |
| [[a-new-model-of-trapped-charge-sources-in-switching-transient-studies-in-the-pres|A New Model of Trapped Charge Sources in Switching Transient]] | 2025 |
| [[double-ended-fault-locating-method-for-parallel-lines-without-measuring-parallel|Double-Ended Fault-Locating Method for Parallel Lines Withou]] | 2025 |
| [[electromagnetic-transient-model-reconstruction-of-generalized-power-transmission|Electromagnetic Transient Model Reconstruction of Generalize]] | 2025 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling and Simulation of Large P]] | 2025 |
| [[electromagnetic-transient-modeling-and-surge-analysis-of-overhead-power-lines-ab|Electromagnetic transient modeling and surge analysis of ove]] | 2025 |
| [[fpga-based-simulation-of-grid-tied-converters-using-frequency-dependent-network-|FPGA-based simulation of grid-tied converters using frequenc]] | 2025 |
| [[high-accuracy-emt-simulations-through-pole-residue-compensation|High-accuracy EMT simulations through pole-residue compensat]] | 2025 |
| [[improving-emt-simulations-using-frequency-shifted-rational-approximations|Improving EMT simulations using frequency-shifted rational a]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f-23|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[influence-of-approximate-internal-impedance-formula-on-half-wavelength-transmiss|Influence of approximate internal impedance formula on half-]] | 2025 |
| [[realization-of-rational-models-for-tower-footing-grounding-systems|Realization of rational models for tower-footing grounding s]] | 2025 |
| [[experimental-research-on-high-voltage-transformer-transient-characteristics|Experimental research on high-voltage transformer transient ]] | 2026 |
| [[low-order-approximation-method-for-frequency-dependent-network-equivalent|Low-order approximation method for frequency-dependent netwo]] | 2026 |
| [[2728multi-rate-real-time-hybrid-simulation-of-controllable-line-commutated-conve|Multi-rate real time hybrid simulation of controllable line ]] | 2026 |
| [[time-delay-estimation-through-all-pass-functions-for-ulm-line-and-cable-models|Time-delay estimation through all-pass functions for ULM lin]] | 2026 |
| [[2728一种用于lcc-hvdc系统小干扰稳定性分析的改进动态相量模型|一种用于LCC-HVDC系统小干扰稳定性分析的改进动态相量模型]] | 2026 |