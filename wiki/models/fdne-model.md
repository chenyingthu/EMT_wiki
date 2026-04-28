---
title: "频变网络等值 (FDNE)"
type: model
tags: [fdne, frequency-dependent, network-equivalent, multi-port, passivity]
created: "2026-04-13"
---

# 频变网络等值 (FDNE)

## 概述

频变网络等值（Frequency-Dependent Network Equivalent, FDNE）是将大规模电力系统的外部网络等效为多端口频率相关阻抗模型的技术。它保留了外部网络的宽频特性，同时大幅减少了仿真规模。

## 核心原理

- 从端口频率响应提取等值参数
- 矢量拟合获得有理函数模型
- 无源性强制确保稳定性
- 转换为状态空间或递归卷积形式

## 关键技术

### 参数辨识
- 频率扫描法
- Prony分析
- 最小二乘拟合
- 在线辨识

### 无源性保证
- 无源性检查算法
- 残差摄动修正
- 局部无源性补偿
- 双层网络等值

### 多端口扩展
- 多输入多输出系统
- 端口间耦合
- MIMO矢量拟合

## 应用场景

- 大电网边界简化
- 混合仿真接口模型
- 电磁-机电暂态混合仿真
- 外部系统宽频建模
- 实时仿真中的外部等值

## 相关方法
- [[vector-fitting]]
- [[passivity-enforcement]]
- [[prony-analysis]]

## 相关主题
- [[network-equivalent]]
- [[frequency-dependent-modeling]]
- [[co-simulation]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-time-domain-approach-to-transmission-network-equivalents-via-prony-analysts-fo|A TIME-DOMAIN APPROACH TO TRANSMISSION NETWORK EQUIVALENTS V]] | 2004 |
| [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i|Multi-port frequency dependent network equivalents for the E]] | 2004 |
| [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical|Frequency Dependent Network Equivalent for Electromagnetic a]] | 2012 |
| [[基于频率相关网络等值的电磁-机电暂态解耦混合仿真|基于频率相关网络等值的电磁-机电暂态解耦混合仿真]] | 2012 |
| [[loewner-matrix-approach-for-modelling-fdnes-of-power-systems|Loewner matrix approach for modelling FDNEs of power systems]] | 2015 |
| [[a-two-layer-network-equivalent-with-local-passivity-compensation-with-applicatio|A Two-layer Network Equivalent with Local Passivity Compensa]] | 2019 |
| [[compacting-and-partitioningbased-simulation-solution-for-frequencydependent-netw|Compacting and partitioning‐based simulation solution for fr]] | 2020 |
| [[electromagnetic-transient-modeling-of-grounding-electrodes-buried-in-frequency-d|Electromagnetic transient modeling of grounding electrodes b]] | 2020 |
| [[a-guaranteed-passive-model-for-multi-port-frequency-dependent-network-equivalent|A guaranteed passive model for multi-port frequency dependen]] | 2021 |
| [[analysis-of-frequency-dependent-network-equivalents-in-dynamic-harmonic-domain|Analysis of Frequency-Dependent Network Equivalents in Dynam]] | 2021 |
| [[efficient-implementation-of-multi-port-frequency-dependent-network-equivalents-f|Efficient Implementation of Multi-Port Frequency Dependent N]] | 2022 |
| [[electromagnetic-transient-analysis-using-a-frequency-dependent-network-equivalen|Electromagnetic Transient Analysis Using a Frequency Depende]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend-17|Enhancing computation performance of rational approximation ]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend|Enhancing computation performance of rational approximation ]] | 2024 |
| [[fpga-based-simulation-of-grid-tied-converters-using-frequency-dependent-network-|FPGA-based simulation of grid-tied converters using frequenc]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f-23|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[low-order-approximation-method-for-frequency-dependent-network-equivalent|Low-order approximation method for frequency-dependent netwo]] | 2026 |

## 深度增强内容

 # 频变网络等值 (FDNE) - 深度技术文档

## 1. 各类模型数学描述

### 1.1 基于有理函数的多端口导纳模型

FDNE的核心是将外部网络的频变导纳特性 $\mathbf{Y}(s) \in \mathbb{C}^{N_p \times N_p}$ 拟合为有理函数形式：

$$
\mathbf{Y}(s) = \sum_{k=1}^{N} \frac{\mathbf{R}_k}{s - p_k} + \mathbf{D} + s\mathbf{E}
$$

其中：
- $N_p$ 为端口数，$N$ 为模型阶数（极点数）
- $\mathbf{R}_k \in \mathbb{C}^{N_p \times N_p}$ 为第 $k$ 个极点对应的留数矩阵
- $p_k$ 为系统极点（实数或共轭复数对）
- $\mathbf{D}, \mathbf{E} \in \mathbb{R}^{N_p \times N_p}$ 分别为常数项和微分项矩阵

**复数矢量拟合（CVF）扩展形式**（2024）：
传统VF要求极点共轭成对（$p_{k+1} = p_k^*$），CVF解除该约束，允许独立拟合复极点：

$$
\mathbf{Y}(s) = \sum_{k=1}^{N} \frac{\mathbf{R}_k}{s - (\sigma_k + j\omega_k)} + \mathbf{D} + s\mathbf{E}
$$

### 1.2 状态空间实现模型

将有理函数转化为MIMO状态空间方程（2025, 2022）：

$$
\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{v}(t)
$$
$$
\mathbf{i}(t) = \mathbf{C}\mathbf{x}(t) + \mathbf{D}\mathbf{v}(t)
$$

其中状态矩阵 $\mathbf{A} \in \mathbb{R}^{nN_p \times nN_p}$ 具有块对角结构：

$$
\mathbf{A} = \text{blkdiag}(\mathbf{A}_1, \mathbf{A}_2, \dots, \mathbf{A}_N), \quad \mathbf{A}_k = \begin{bmatrix} \sigma_k & \omega_k \\ -\omega_k & \sigma_k \end{bmatrix}
$$

系统计算复杂度为 $O(N^2)$，状态空间矩阵维度为 $N \cdot N_p \times N \cdot N_p$（2024）。

### 1.3 离散时间z域模型

适用于在线辨识与实时仿真的离散形式（2018, 2024）：

$$
\mathbf{Y}(z) = \sum_{k=1}^{N} \frac{\mathbf{R}_k}{z - \gamma_k} + \mathbf{D}_d
$$

其中 $\gamma_k = e^{p_k \Delta t}$，$\Delta t$ 为仿真步长。递推最小二乘（RLS）在线辨识算法直接估计 $\mathbf{R}_k$ 和 $\gamma_k$ 参数。

### 1.4 双层网络等值模型

适用于含电力电子设备的混合仿真（2019, 2012）：

$$
\mathbf{Y}_{\text{total}}(s) = \mathbf{Y}_{\text{FDNE}}(s) + \mathbf{Y}_{\text{DLFE}}(s)
$$

- **FDNE层**：表征高频电磁特性（>10 Hz），通过扰动测试或频率扫描获得
- **DLFE层（Dynamic Low-Frequency Equivalent）**：表征低频机电动态，含风机控制、锁相环等状态方程

### 1.5 无源网络综合模型

基于Tellegen综合法的RLCM无源网络（2021）：

将导纳矩阵 $\mathbf{Y}(s)$ 直接合成为物理RLC网络：

$$
\mathbf{Y}(s) = \mathbf{C}_p s + \mathbf{G}_p + \sum_{k=1}^{N_{\text{branch}}} \frac{1}{\mathbf{L}_k s + \mathbf{R}_k}
$$

其中 $\mathbf{C}_p, \mathbf{G}_p, \mathbf{L}_k, \mathbf{R}_k$ 分别为综合得到的电容、电导、电感和电阻矩阵，内禀保证无源性。

## 2. 仿真参数参考表

| 参数类别 | 参数值 | 应用场景 | 来源论文 |
|---------|--------|----------|----------|
| **模型阶数** | 40-50个极点 | 杆塔全波模型（10kHz-10MHz） | 2021（Full-wave tower） |
| | 80个RLCM模块 | 三端口复杂输电网络 | 2021（Network synthesis） |
| | 自适应阶数（SVD截断） | Loewner矩阵方法 | 2015 |
| **频率范围** | 5 Hz - 5 kHz | 输电网络工频及谐波 | 2022 |
| | 0 - 50 kHz | Type-4风电场宽频建模 | 2012 |
| | 10 kHz - 10 MHz | 雷击杆塔高频暂态 | 2021 |
| **仿真步长** | 20 µs | EMT离线仿真 | 2021 |
| | <1 µs | FPGA超实时仿真 | 2025 |
| | µs级单步长 | RTDS实时接口 | 2018 |
| **计算性能** | 加速3.3倍 | 网络综合法vs详细模型 | 2021 |
| | 加速218倍 | 风电场等值（18480s→110s） | 2012 |
| | 加速3.45倍 | Type-69诺顿等效实现 | 2022 |
| | 实时成功率100% | 11个子模块划分（Y10案例） | 2020 |
| **精度指标** | 幅值误差<0.8% | 全频段导纳拟合 | 2015 |
| | 相位偏差<0.5° | Loewner矩阵方法 | 2015 |
| | 误差$8.805\times10^{-5}$ mho | 诺顿等效导纳矩阵 | 2022 |
| | 时域偏差<0.5% | 风电机组故障暂态 | 2024 |
| **无源性裕度** | Re(Y)最小特征值>0 | 全频段验证 | 2015 |
| | 发散率从18.7%→0% | 局部补偿后 | 2019 |

## 3. 模型选择指南

### 3.1 实时仿真与硬件加速场景
**推荐模型**：压缩划分FDNE（2020）+ FPGA状态空间实现（2025）

**选择依据**：
- 当端口数 $N_p > 8$ 时，采用SVD压缩降低状态冗余（留数矩阵秩 $r < (N+1)/2$ 时可降计算量50%以上）
- 基于HLS的FPGA实现可实现亚微秒级步长（<1 µs），适合电力电子开关动态

**配置建议**：
- 采用CuFP定制浮点算术，资源占用降低30%~40%，误差<0.1%
- 单机架（4张GPC卡）最多承载18个FDNE子模块，需合理划分

### 3.2 风电场与新能源并网
**推荐模型**：双层等值（2012）或离散z域模型（2024）

**选择依据**：
- Type-4风电场需覆盖0-50 kHz宽频带，单一FDNE无法复现低频控制动态
- 故障穿越（VRT）仿真要求PCC电压偏差<1.2%

**配置建议**：
- 高频FDNE层：拟合背靠背变流器高频特性（>10 Hz）
- 低频DLFE层：聚合网侧变流器控制（17台等效替代66台）
- 采用多正弦信号激励+RLS辨识，幅值误差可达$10^{-7}$量级

### 3.3 多端口大规模网络（$N_p \geq 10$）
**推荐模型**：Loewner矩阵法（2015）或并行复数矢量拟合（2024）

**选择依据**：
- 传统VF迭代收敛困难时，Loewner矩阵非迭代特性可节省30%~50%建模时间
- QR分解占VF算法95%以上时间，并行化C语言+Intel MKL实现可突破MATLAB性能瓶颈

**配置建议**：
- 数据划分比例保持50:50（左右插值点），偏差>20%时误差上升3~5倍
- CVF解除共轭约束，适合非对称/基带频响拟合

### 3.4 严格无源性要求场景
**推荐模型**：网络综合法（2021）或局部无源性补偿（2019）

**选择依据**：
- 传统残差摄动法可能不收敛，网络综合法通过物理RLCM拓扑内禀保证无源性
- 局部补偿算法构建时间仅0.1~0.2秒，较全局优化提升200倍

**配置建议**：
- 相位角极点/零点识别阈值设为0.5°
- 双层结构中层间解耦，避免全局优化

## 4. 前沿研究方向

### 4.1 异构并行计算架构
- **多核CPU/GPU加速**：基于C语言与底层线性代数库（Intel MKL）实现VF/CVF并行化，QR分解步骤并行度提升是关键（2024）
- **FPGA超实时仿真**：状态空间方程的定点/浮点混合运算优化，实现亚微秒级延迟（2025）

### 4.2 在线自适应辨识技术
- **递推最小二乘（RLS）z域辨识**：免除预计算50001个频点的离线扫描，模型构建时间缩短90%以上（2018）
- **宽频无源性在线强制**：离散域直接实现无源性约束，长时仿真数值发散概率降为0（2018）

### 4.3 多物理场耦合等值
- **电磁-热耦合FDNE**：考虑接地极频率依赖土壤参数（2020）
- **机电-电磁混合接口**：TS-EMT混合仿真中，FDNE作为宽频接口模型，高频段（>1 kHz）幅频响应偏差<0.5 dB（2019）

### 4.4 智能算法融合
- **Loewner矩阵数据驱动**：基于SVD的模型阶数自动识别（2015）
- **AI辅助极点选择**：利用机器学习预测最优极点初始位置，减少VF迭代次数

### 4.5 新型电力系统应用
- **MMC-HVDC电网**：双层网络等值在含MMC的AC/DC电网混合仿真中，局部无源性补偿避免18.7%的仿真发散率（2019）
- **雷击过电压黑盒模型**：全波麦克斯韦方程+FDNE，替代传统多节杆塔模型，误差从11.5%降至<1%（2021）
