---
title: "频变网络等值 (FDNE)"
type: model
tags: [fdne, frequency-dependent, network-equivalent, multi-port, passivity]
created: "2026-04-13"
---

# 频变网络等值 (FDNE)


```mermaid
graph TD
    subgraph Ncmp[频变网络等值 (FDNE)]
        N0[[[multi-port-frequency-depen…]
        N1[[[real-time-transient-simula…]
        N2[[[a-type-4-wind-power-plant-…]
        N3[[[time-domain-transformation…]
        N4[[[基于频率相关网络等值的电磁-机电暂态解耦混合仿真: …]
        N5[[[电磁机电暂态混合仿真中机电侧故障的仿真方法: 电磁–…]
        N6[[[电磁机电暂态混合仿真中的频率相关网络等值: 电磁–机…]
        N7[[[frequency-domain-simulatio…]
    end
```


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
| [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i|Multi-port frequency dependent network equivalents for the E]] | 2004 |
| [[real-time-transient-simulation-based-on-a-robust|Real-Time Transient Simulation Based on a Robust]] | 2007 |
| [[a-type-4-wind-power-plant-equivalent-model|A Type-4 Wind Power Plant Equivalent Model]] | 2012 |
| [[time-domain-transformation-method|Time Domain Transformation Method]] | 2012 |
| [[基于频率相关网络等值的电磁-机电暂态解耦混合仿真|基于频率相关网络等值的电磁-机电暂态解耦混合仿真]] | 2012 |
| [[电磁机电暂态混合仿真中机电侧故障的仿真方法|电磁–机电暂态混合仿真中机电侧故障的仿真方法]] | 2012 |
| [[电磁机电暂态混合仿真中的频率相关网络等值|电磁–机电暂态混合仿真中的频率相关网络等值]] | 2012 |
| [[frequency-domain-simulation-of-electromagnetic-transients-using-variable|Frequency-Domain Simulation of Electromagnetic Transients Us]] | 2015 |
| [[loewner-matrix-approach-for-modelling-fdnes-of-power-systems|Loewner matrix approach for modelling FDNEs of power systems]] | 2015 |
| [[development-and-applicability-of-online-passivity-enforced-wide-band-multi-port-|Development and Applicability of Online Passivity Enforced W]] | 2018 |
| [[a-two-layer-network-equivalent-with-local-passivity-compensation-with-applicatio|A Two-layer Network Equivalent with Local Passivity Compensa]] | 2019 |
| [[a-two-layer-network-equivalent-with-local-passivity-compensation-with-applicatio|A Two-layer Network Equivalent with Local Passivity Compensa]] | 2019 |
| [[compacting-and-partitioningbased-simulation-solution-for-frequencydependent-netw|Compacting and partitioning‐based simulation solution for fr]] | 2020 |
| [[a-guaranteed-passive-model-for-multi-port-frequency-dependent-network-equivalent|A guaranteed passive model for multi-port frequency dependen]] | 2021 |
| [[full-wave-black-box-transmission-line-tower-model-for-the-assessment-of-lightnin|Full-wave black-box transmission line tower model for the as]] | 2021 |
| [[full-wave-black-box-transmission-line-tower-model-for-the-assessment-of-lightnin|Full-wave black-box transmission line tower model for the as]] | 2021 |
| [[review-and-comparison-of-frequency-domain-curve-fitting-techniques-vector-fittin|Review and comparison of frequency-domain curve-fitting tech]] | 2021 |
| [[efficient-implementation-of-multi-port-frequency-dependent-network-equivalents-f|Efficient Implementation of Multi-Port Frequency Dependent N]] | 2022 |
| [[中-国-电-机-工-程-学-报-34|中  国  电  机  工  程  学  报]] | 2022 |
| [[电力系统数字混合仿真技术综述及展望|电力系统数字混合仿真技术综述及展望]] | 2023 |
| [[电力系统数字混合仿真技术综述及展望|电力系统数字混合仿真技术综述及展望]] | 2023 |
| [[electromagnetic-transient-analysis-using-a-frequency-dependent-network-equivalen|Electromagnetic Transient Analysis Using a Frequency Depende]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend-17|Enhancing computation performance of rational approximation ]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend|Enhancing computation performance of rational approximation ]] | 2024 |
| [[fpga-based-simulation-of-grid-tied-converters-using-frequency-dependent-network-|FPGA-based simulation of grid-tied converters using frequenc]] | 2025 |
| [[realization-of-rational-models-for-tower-footing-grounding-systems|Realization of rational models for tower-footing grounding s]] | 2025 |
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
- QR分解占VF算法95%以上时间，并行化C语言+Intel MKL实现可贡献MATLAB性能瓶颈

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

## 技术演进脉络

### 1990年代 (理论奠基)
- **矢量拟合算法提出 (1999)**
  - Gustavsen和Semlyen提出矢量拟合(VF)算法
  - 为频变网络等值提供数学基础
  - 解决频域数据有理函数逼近问题

- **频变网络等值概念确立**
  - 将外部网络等效为频率相关多端口模型
  - 保留宽频特性同时降低仿真规模
  - 应用于EMTP类仿真器

### 2000年代 (方法成熟)
- **多端口FDNE (2004)**
  - 扩展至MIMO系统
  - 公共极点策略降低计算复杂度
  - 应用于大规模电网边界等值

- **无源性强制技术 (2008-2010)**
  - 提出残差摄动法确保模型无源性
  - 解决时域仿真发散问题
  - 建立Hamiltonian矩阵检验方法

### 2010年代 (应用扩展)
- **在线辨识与实时仿真 (2018)**
  - RLS递推最小二乘实现z域在线辨识
  - 免除离线频域扫描
  - FPGA实现亚微秒级实时仿真

- **双层网络等值 (2019)**
  - FDNE+DLFE分层结构
  - 高频电磁与低频机电分离
  - 局部无源性补偿策略

- **Loewner矩阵数据驱动 (2015)**
  - 非迭代模型降阶方法
  - SVD自动确定模型阶数
  - 适用于黑箱系统辨识

### 2020年代 (异构并行与智能化)
- **网络综合法 (2021)**
  - Tellegen综合实现物理RLCM网络
  - 内禀保证无源性
  - 计算加速3.3倍

- **并行复数矢量拟合 (2024)**
  - C语言+Intel MKL并行化
  - CVF解除共轭约束
  - 支持8端口以上大规模系统

- **FPGA超实时仿真 (2025)**
  - 状态空间方程定点实现
  - 亚微秒级步长
  - 电力电子开关动态捕捉

## 代表性来源

| 论文 | 年份 | 关联要点 |
|------|------|----------|
| [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i|Multi-port frequency dependent network equivalents for the EMTP]] | 2004 | 多端口FDNE基础理论 |
| [[loewner-matrix-approach-for-modelling-fdnes-of-power-systems|Loewner matrix approach for modelling FDNEs of power systems]] | 2015 | Loewner矩阵数据驱动方法 |
| [[development-and-applicability-of-online-passivity-enforced-wide-band-multi-port-|Development and Applicability of Online Passivity Enforced Wide-Band Multi-Port FDNE]] | 2018 | 在线无源性强制与实时仿真 |
| [[a-two-layer-network-equivalent-with-local-passivity-compensation-with-applicatio|A Two-layer Network Equivalent with Local Passivity Compensation]] | 2019 | 双层网络等值与局部补偿 |
| [[a-guaranteed-passive-model-for-multi-port-frequency-dependent-network-equivalent|A Guaranteed Passive Model for Multi-Port FDNE]] | 2021 | 严格无源性保证模型 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend|Enhancing computation performance of rational approximation for FDNE]] | 2024 | 并行CVF与高性能计算 |
| [[fpga-based-simulation-of-grid-tied-converters-using-frequency-dependent-network-|FPGA-based Simulation of Grid-Tied Converters Using FDNE]] | 2025 | FPGA硬件加速实现 |

## 最佳实践与注意事项

### 5.1 建模前准备
1. **确定端口位置**：选择电气距离适中的边界点
2. **频率范围设定**：覆盖关注频段（通常DC-10MHz）
3. **采样策略**：对数均匀分布，谐振峰处加密

### 5.2 矢量拟合参数调优
- **初始极点**：对数分布，实部为虚部1/100
- **模型阶数**：每decade 2-3个极点，每个谐振峰2-4个
- **迭代收敛**：通常3-5次，最大21次

### 5.3 无源性强制策略
| 违规类型 | 推荐方法 | 关键参数 |
|---------|---------|---------|
| 低频大违规 | 人工电导 | $G_{add}=10^{-6}$ S/m, $\tau=1$s |
| 带内小违规 | 残差摄动 | 仅修正传播矩阵对角 |
| 高频渐近违规 | 高频约束 | $f_c=10$ MHz |
| 多频点分散违规 | 全摄动优化 | Frobenius距离<5% |

### 5.4 实时仿真适配
- **状态空间实现**：极点-留数转A,B,C,D矩阵
- **步长选择**：满足稳定性条件 $\Delta t < 2/|p_{max}|$
- **定点化**：注意数值精度损失

### 5.5 验证与校核
- [ ] 频域拟合误差<1%
- [ ] 无源性全频段验证
- [ ] 时域波形对比详细模型
- [ ] 能量守恒检查
- [ ] 极端工况稳定性测试

### 5.6 常见问题与解决

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| 拟合不收敛 | 初始极点选择不当 | 复数极点，对数分布 |
| 时域发散 | 无源性违规 | 强制无源性后重新验证 |
| 低频精度差 | 采样点不足 | DC附近加密采样 |
| 计算太慢 | QR分解瓶颈 | 并行化或降阶 |
| 实时性不足 | 状态数太多 | SVD压缩或MOR降阶 |

## 来源论文

| 论文 | 年份 |
|------|------|
| [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i|Multi-port frequency dependent network equivalents for the E]] | 2004 |
| [[real-time-transient-simulation-based-on-a-robust|Real-Time Transient Simulation Based on a Robust]] | 2007 |
| [[a-type-4-wind-power-plant-equivalent-model|A Type-4 Wind Power Plant Equivalent Model]] | 2012 |
| [[time-domain-transformation-method|Time Domain Transformation Method]] | 2012 |
| [[基于频率相关网络等值的电磁-机电暂态解耦混合仿真|基于频率相关网络等值的电磁-机电暂态解耦混合仿真]] | 2012 |
| [[电磁机电暂态混合仿真中机电侧故障的仿真方法|电磁–机电暂态混合仿真中机电侧故障的仿真方法]] | 2012 |
| [[电磁机电暂态混合仿真中的频率相关网络等值|电磁–机电暂态混合仿真中的频率相关网络等值]] | 2012 |
| [[frequency-domain-simulation-of-electromagnetic-transients-using-variable|Frequency-Domain Simulation of Electromagnetic Transients Us]] | 2015 |
| [[loewner-matrix-approach-for-modelling-fdnes-of-power-systems|Loewner matrix approach for modelling FDNEs of power systems]] | 2015 |
| [[development-and-applicability-of-online-passivity-enforced-wide-band-multi-port-|Development and Applicability of Online Passivity Enforced W]] | 2018 |
| [[a-two-layer-network-equivalent-with-local-passivity-compensation-with-applicatio|A Two-layer Network Equivalent with Local Passivity Compensa]] | 2019 |
| [[a-two-layer-network-equivalent-with-local-passivity-compensation-with-applicatio|A Two-layer Network Equivalent with Local Passivity Compensa]] | 2019 |
| [[compacting-and-partitioningbased-simulation-solution-for-frequencydependent-netw|Compacting and partitioning‐based simulation solution for fr]] | 2020 |
| [[a-guaranteed-passive-model-for-multi-port-frequency-dependent-network-equivalent|A guaranteed passive model for multi-port frequency dependen]] | 2021 |
| [[full-wave-black-box-transmission-line-tower-model-for-the-assessment-of-lightnin|Full-wave black-box transmission line tower model for the as]] | 2021 |
| [[full-wave-black-box-transmission-line-tower-model-for-the-assessment-of-lightnin|Full-wave black-box transmission line tower model for the as]] | 2021 |
| [[review-and-comparison-of-frequency-domain-curve-fitting-techniques-vector-fittin|Review and comparison of frequency-domain curve-fitting tech]] | 2021 |
| [[efficient-implementation-of-multi-port-frequency-dependent-network-equivalents-f|Efficient Implementation of Multi-Port Frequency Dependent N]] | 2022 |
| [[中-国-电-机-工-程-学-报-34|中  国  电  机  工  程  学  报]] | 2022 |
| [[电力系统数字混合仿真技术综述及展望|电力系统数字混合仿真技术综述及展望]] | 2023 |
| [[电力系统数字混合仿真技术综述及展望|电力系统数字混合仿真技术综述及展望]] | 2023 |
| [[electromagnetic-transient-analysis-using-a-frequency-dependent-network-equivalen|Electromagnetic Transient Analysis Using a Frequency Depende]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend-17|Enhancing computation performance of rational approximation ]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend|Enhancing computation performance of rational approximation ]] | 2024 |
| [[fpga-based-simulation-of-grid-tied-converters-using-frequency-dependent-network-|FPGA-based simulation of grid-tied converters using frequenc]] | 2025 |
| [[realization-of-rational-models-for-tower-footing-grounding-systems|Realization of rational models for tower-footing grounding s]] | 2025 |
## 相关主题
- [[network-equivalent|网络等值]]
- [[frequency-dependent-modeling|频率相关建模]]
- [[co-simulation|混合仿真]]
- [[real-time-simulation|实时仿真]]
- [[passivity-enforcement|无源性强制]]

## 相关方法
- [[vector-fitting|矢量拟合]]
- [[state-space-method|状态空间法]]
- [[numerical-integration|数值积分]]
- [[prony-analysis|Prony分析]]

## 相关模型
- [[transmission-line-model|输电线路模型]] - FDNE端口边界模型
- [[transformer-model|变压器模型]] - 变压器宽频等值
- [[vsc-model|VSC模型]] - 换流器外部系统简化
- [[wind-farm-modeling|风电场模型]] - 风电场宽频聚合
- [[mmc-model|MMC模型]] - MMC外部网络等值

## 典型应用案例

### 案例1：风电场并网宽频等值
**场景**：含66台风机的海上风电场，需进行电能质量与谐波分析
**方案**：
- 端口设置：PCC点（3相）+ 集电线路中点
- 频率范围：0.1 Hz - 10 kHz
- 模型阶数：80个极点（考虑电力电子设备开关频率）
- 验证指标：频域拟合误差<0.5%，时域故障波形偏差<1%

### 案例2：MMC-HVDC交直流混合仿真
**场景**：MMC换流站接入大电网，需兼顾内部子模块动态与外部网络响应
**方案**：
- 双层等值结构：FDNE层（>10Hz）+ DLFE层（控制动态）
- 局部无源性补偿：层间解耦，避免全局优化
- 实时性：FPGA实现，步长<1μs
**效果**：仿真发散率从18.7%降至0%

### 案例3：雷击过电压杆塔建模
**场景**：500kV输电线路雷击塔顶过电压计算
**方案**：
- 黑盒FDNE模型：10kHz - 10MHz
- 杆塔三端口等值：塔顶、塔身、接地极
- 对比传统多节Π模型：误差从11.5%降至<1%
**性能**：计算加速3.3倍
