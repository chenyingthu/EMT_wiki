---
title: "网络等值 (Network Equivalent)"
type: topic
tags: [network-equivalent, thevenin, ward, fdne, reduction]
created: "2026-04-13"
---

# 网络等值 (Network Equivalent)

## 概述

网络等值技术将大规模电力系统简化为等效模型，在保持端口特性不变的前提下大幅减少仿真规模。这是混合仿真、并行计算和大电网仿真的基础技术。

## 等值类型

### 1. 稳态等值
- Ward等值
- REI等值
- 适用于潮流和机电暂态

### 2. 频变等值 (FDNE)
- 考虑频率相关特性的宽频等值
- 多端口Thevenin等值
- 矢量拟合实现

### 3. 动态等值
- 保留关键动态特性
- 同步机等值聚合
- 新能源场站等值

### 4. 多层等值
- 双层网络等值（局部+全局）
- 多区域Thevenin等值
- 混合仿真中的接口等值

## 关键技术

- 参数辨识（Prony分析、最小二乘）
- 无源性补偿
- 在线更新策略
- 等值误差评估

## 定义与边界

网络等值是在选定边界端口上保留外部系统电压、电流、阻抗或动态响应的模型压缩技术。它不是简单删除节点，而是把外部网络替换成可接入 [[emtp|EMTP]]、[[pscad-emtdc|PSCAD/EMTDC]] 或 [[rtds|RTDS]] 的等效模型；常见路径包括 [[fdne-model|频变网络等值]]、[[prony-analysis|Prony 分析]]、[[vector-fitting|矢量拟合]] 和 [[passivity-enforcement|无源性补偿]]。

适用边界取决于端口选择、频段、线性化工作点和所需暂态类型。稳态 Ward/REI 等值不能替代宽频 EMT 等值；单端口戴维南等值也不能表达多馈入 HVDC、[[vsc-model|VSC]] 或 [[lcc-model|LCC]] 系统之间的强耦合。

## 代表性来源与内部链接

代表性来源包括 [[a-time-domain-approach-to-transmission-network-equivalents-via-prony-analysts-fo|A time-domain approach to transmission network equivalents via Prony analysis]]、[[a-guaranteed-passive-model-for-multi-port-frequency-dependent-network-equivalent|A guaranteed passive model for multi-port frequency-dependent network equivalent]]、[[efficient-implementation-of-multi-port-frequency-dependent-network-equivalents-f|Efficient implementation of multi-port frequency-dependent network equivalents]] 和 [[a-two-layer-network-equivalent-with-local-passivity-compensation-with-applicatio|A two-layer network equivalent with local passivity compensation]]。相关模型包括 [[synchronous-machine-model]]、[[transmission-line-model]]、[[cable-model]] 和 [[mmc-model]]。

## 相关方法
- [[vector-fitting]]
- [[prony-analysis]]
- [[passivity-enforcement]]

## 相关模型
- [[fdne-model]]
- [[synchronous-machine-model]]

## 相关主题
- [[co-simulation|混合仿真]] - 等值模型用于EMT-机电混合
- [[frequency-dependent-modeling|频率相关建模]] - 宽频FDNE基础
- [[real-time-simulation|实时仿真]] - 等值模型实时实现
- [[parallel-computing|并行计算]] - 网络分割与并行
- [[network-equivalent|网络等值]] - 系统级等值策略

## 技术演进脉络

### 1990-2000年：戴维南等值基础
- **经典戴维南-诺顿等值** (1990s)
  - 基于工频阻抗的简化等值方法，用于机电暂态仿真
- **频率相关等值初步探索** (1995-1999)
  - 考虑简单频变特性的改进等值模型

### 2001-2010年：矢量拟合与宽频等值
- **矢量拟合(VF)算法** (2003-2006)
  - 提出鲁棒矢量拟合方法，实现宽频导纳精确有理逼近
- **频变网络等值(FDNE)** (2005-2008)
  - 建立FDNE统一框架，支持多端口宽频等值
- **实时仿真等值** (2008-2010)
  - 开发适用于实时仿真的简化等值模型

### 2011-2015年：混合仿真接口
- **机电-电磁混合接口** (2011-2013)
  - 提出基于等值模型的混合仿真接口方法
- **多区域等值协调** (2013-2015)
  - 实现大规模电网多区域等值协调策略

### 2016-2026年：并行与高效计算
- **GPU并行等值计算** (2016-2020)
  - 利用GPU加速大规模网络等值参数计算
- **深度学习辅助等值** (2021-2026)
  - 探索神经网络代理模型用于快速等值

## 关键发现汇总

### 等值精度与效率权衡
- **[2006]** 矢量拟合在0.1Hz-1MHz范围内可实现<1%的逼近误差，极点数通常20-50个
- **[2010]** FDNE在保持宽频精度(10kHz)的同时，计算效率提升10-100倍
- **[2015]** 多区域等值协调在百节点规模下误差<3%，千节点规模<5%

### 关键技术突破
- **[2003]** 鲁棒矢量拟合解决传统VF的数值稳定性问题，支持自动极点选择
- **[2013]** 混合仿真接口实现机电(10ms步长)与电磁(50μs步长)无缝耦合
- **[2020]** GPU并行使10万节点网络等值计算时间从小时级降至分钟级

### 应用效果验证
- **[2008]** RTDS实时等值模型在HIL测试中稳定性误差<2%
- **[2016]** 风电场FDNE在1kHz内与详细模型误差<5%，适用于并网稳定性分析
- **[2022]** 基于测量的FDNE修正使高频(>10kHz)误差从15%降至3%

### 前沿研究方向
- **数据驱动等值**：利用PMU测量数据在线修正等值参数
- **宽频统一框架**：覆盖10mHz-10MHz的统一等值建模方法
- **不确定性量化**：考虑参数不确定性的鲁棒等值模型
- **数字孪生集成**：等值模型与数字孪生平台的实时交互

## 深度增强内容

 # 网络等值 (Network Equivalent) - 深度增强版

## 1. 关键技术详解

### 1.1 频变网络等值(FDNE)与矢量拟合技术

频变网络等值(Frequency Dependent Network Equivalent, FDNE)是宽频电磁暂态仿真的核心技术，通过有理函数逼近外部系统的频域导纳特性，将大规模网络压缩为紧凑的多端口等效电路。

#### 1.1.1 基于矢量拟合(VF)的宽频建模

FDNE的核心是将导纳矩阵$\mathbf{Y}(s)$拟合为有理函数形式：

$$\mathbf{Y}(s) \approx \mathbf{Y}_{fit}(s) = \mathbf{C} + s\mathbf{D} + \sum_{m=1}^{N_p} \frac{\mathbf{R}_m}{s - p_m}$$

其中，$p_m$为公共极点，$\mathbf{R}_m$为留数矩阵，$N_p$为模型阶数。根据论文数据，采用**公共极点策略**（所有矩阵元素共享相同极点）可显著降低时域实现计算量，而非对称系统可采用**复数矢量拟合(CVF)**解除复共轭极点约束，提升基带频响拟合灵活性。

**关键参数与性能**：
- 频率覆盖范围：1–2 kHz（覆盖12脉波HVDC的11、13、23、25次特征谐波）至10 MHz（接地系统暂态）
- 拟合误差：频带内误差通常<1%，无源性强制引入的附加误差<0.5%
- 迭代收敛：3–4次迭代即可实现极点收敛

#### 1.1.2 无源性强制与稳定性保证

无源性是保证FDNE时域仿真数值稳定的前提。采用基于**半尺寸无源性测试矩阵**的扰动算法：

$$\mathbf{G}(j\omega) + \mathbf{G}^H(j\omega) \geq 0, \quad \forall \omega$$

其中$\mathbf{G}(s)$为有理函数模型。通过奇异值分解检测违规频点，对留数矩阵进行扰动修正，确保所有特征值大于零。

#### 1.1.3 模型降阶与压缩技术

针对多端口系统计算复杂度$O = 2nN^2 + N^2 + 2nN$（$n$为极点数，$N$为端口数）的问题，采用**奇异值分解(SVD)压缩**：

当留数矩阵秩$r < (N+1)/2$时，单极点计算量从$2N^2+2N$降至$4rN$，最大降幅超过50%。例如Y4案例中，计算量从3900降至3276，精度损失仅$0.32 \times 10^{-5}$。

**低阶近似方法**通过单调区间划分与分段误差控制（传播系数分段绝对误差区间系数$\xi_1=0.2$与$\xi_2=0.03$），可将正序特征阻抗拟合阶数从15阶降至3阶（压缩率70–80%），递归卷积历史电流源更新项减少约75%。

### 1.2 机电-电磁混合仿真接口等值

混合仿真接口等值是解决大规模电网（10,000+节点）与局部电磁暂态详细模型（100+节点）协同仿真的关键。

#### 1.2.1 多速率接口与边界解耦

接口两侧时间尺度差异达200倍（机电侧10 ms vs 电磁侧50 μs）。采用**边界节点分组解耦**策略：

- **机电侧**：计算复杂度与边界节点数$N$成正比，$f_{\text{st}}(N, n) \approx 2 \cdot O(3n + \text{flops}) + (3N + 3) \cdot O(\text{flops})$
- **电磁侧**：计算复杂度与$N^3$成正比，$f_{\text{emt}}(N, m) \approx N^3 + (3N + 2)(m^2 + m) + m^3/3$

**临界阈值**：当$N > 150$时，电磁侧计算量进入非线性快速增长区域，成为效率瓶颈。解决方案包括：
- 采用分布参数长传输线实现子网弱耦合分割
- 基于诺顿/戴维南等值的电气孤岛解耦

#### 1.2.2 等值电路形式与数据转换

| 等值类型 | 适用场景 | 数学描述 | 精度特点 |
|---------|---------|---------|---------|
| 单端口戴维南 | 远离非线性负荷 | $\dot{V} = \dot{E}_{\text{eq}} - Z_{\text{eq}}\dot{I}$ | 需考虑正/负/零序阻抗 |
| 多端口戴维南 | 多馈入系统 | $\mathbf{V} = \mathbf{E}_{\text{eq}} - \mathbf{Z}_{\text{eq}}(s)\mathbf{I}$ | 导纳矩阵维数随端口平方增长 |
| FDNE | 含电力电子设备 | $\mathbf{I}(s) = \mathbf{Y}_{\text{fdne}}(s)\mathbf{V}(s)$ | 准确表征宽频特性，计算开销大 |

**数据转换精度**：改进的dq-120结合Prony算法可在故障后5个采样点精确提取基波相量，接口插值算法将边界数值振荡幅度降低85%以上（最大过冲从12%降至1.5%）。

### 1.3 电力电子设备高效等值

#### 1.3.1 MMC戴维南等效整体建模

针对模块化多电平换流器(MMC)，采用**戴维南等效整体建模**方法：

- **计算复杂度**：从$O(N^2)$（详细模型）降至$O(N)$（整体模型），121电平MMC加速比达2770倍
- **精度**：暂稳态最大误差<0.2%
- **数值稳定性**：采用后退欧拉法离散化（$G_{\text{eq}} = C/\Delta t$）消除梯形积分法引起的数值振荡，具有A-稳定性

子模块聚合策略：将$N_{\text{HB}}$个半桥和$N_{\text{FB}}$个全桥子模块聚合为2个等效阀段，状态变量从$O(N)$降至$O(1)$每桥臂。

#### 1.3.2 高频隔离型PET等值

高频隔离型电力电子变压器(PET)开关频率(1–20 kHz)远高于MMC(150–300 Hz)，详细模型节点密度比达7.3:1。采用**嵌套快速求解法**进行内部节点消去，将DAB模块的9阶节点导纳矩阵降阶为仅保留外端子的低阶矩阵，避免每步长直接求逆高阶矩阵。

### 1.4 传输线路频变等值

#### 1.4.1 精确等效π型电路

传统标称π型级联方法因分段数量过多(>10段)会引入虚假振荡。精确等效π型电路通过矢量拟合将频变导纳近似为有理函数：

$$Y_{\text{line}}(s) \approx \sum_{k=1}^{N_p} \frac{1}{R_k + sL_k} + sC_{\infty}$$

实现任意长度线路的单一π型电路表示，避免卷积运算，可直接集成于通用电路仿真软件。

#### 1.4.2 接地系统频变建模

杆塔接地系统采用主导极点准则，模型阶数减少近50%（从20–40极点降至11极点），在100 Hz–10 MHz范围内满足$rms \leq \min(|Y_g|)/1000$（相对误差<0.1%）。

## 2. 硬件平台对比

| 平台类型 | 典型步长 | 节点规模 | FDNE支持能力 | 适用场景 |
|---------|---------|---------|-------------|---------|
| **RTDS** | 20–50 μs | 单机架~100节点 | 单机架18个FDNE子模块，计算量阈值3396 | 实时仿真、HIL测试 |
| **CPU-GPU混合** | 可达100 μs | 3,000+子模块(MMC) | 依赖GPU并行度，传输瓶颈为NMS数据映射 | 大规模电力电子系统离线仿真 |
| **PC集群** | 20 μs | 大规模外部系统 | 支持双层网络等值(TLNE) | 实时仿真、大规模系统并行计算 |
| **FPGA** | 1–10 μs | 受限 | 需预存导纳矩阵逆（$2^N$拓扑限制） | 电力电子详细模型 |

**性能瓶颈分析**：
- **RTDS**：FDNE计算复杂度与端口数平方关系，当留数矩阵满秩时，10端口以上系统易触及实时计算阈值
- **GPU**：CPU-GPU数据传输耗时是主要瓶颈，采用节点映射结构(NMS)可减少传输数据量
- **FPGA**：换流器$N$个开关阀存在$2^N$种拓扑，预存所有导纳矩阵逆矩阵的存储量随$N$指数增长

## 3. 实际应用案例汇总

### 3.1 大规模MMC-HVDC系统仿真

**场景**：双端MMC-HVDC系统，含3,000个子模块（鲁西工程±350kV/1000MW规模）

**等值方案**：
- 子模块聚合法：将400+子模块/桥臂聚合为2个等效阀段
- 打靶法初始化：相比详细模型，AVM模型将状态变量从$O(N)$降至$O(1)$，显著降低雅可比矩阵维度

**效果**：
- 详细模型仿真5s需3,000+小时，等效模型可在数分钟至数小时内完成
- 仿真步长20 μs下，实时仿真比从1:960提升至满足实时要求

### 3.2 多端口外部系统FDNE等值

**场景**：含密集网络的500kV变电站外部系统（Y4、Y10案例）

**技术方案**：
- 采用SVD压缩，当$r < (N+1)/2$时，Y4案例计算量从3900降至3276
- 划分11个子模块后，最大单模块计算量3204，低于RTDS阈值3396，实现100%实时仿真成功率

### 3.3 交直流混联电网分割并行仿真

**场景**：含HVDC的交直流混联电网

**分割策略**：
- 利用分布参数长传输线解耦，将电磁网天然分割为弱耦合子网
- 交直流分割后，换流器拓扑变化仅影响所在子网（12维矩阵运算），而非全网矩阵

**性能**：换流阀动作导致的矩阵重构计算量从$O(n^3)$（全网）降至$O(m^3)$（子网，$m \ll n$）

### 3.4 接地系统宽频等值

**场景**：输电线路杆塔接地系统（90m–120m电极，1,000 Ω·m土壤）

**模型**：11阶有理函数模型，覆盖100 Hz–10 MHz

**精度**：与详细电磁模型偏差三个数量级以内，高频振荡特性准确复现。

## 4. 研究趋势与开放问题

### 4.1 当前技术瓶颈

1. **非线性与时变系统**：现有FDNE基于线性时不变假设，对于含饱和特性（如变压器、CVT）的系统，需结合状态方程离散化与导纳互差法，但模型阶数与复杂度显著增加。

2. **大规模电力电子接入**：当系统中存在数千个电力电子变换器时，接口母线数目随端口规模平方增长，电磁侧等值电路导纳矩阵维数过高，实时仿真面临"维度灾难"。

3. **多速率接口稳定性**：并行交互时序在稳态下无误差，但暂态过程中存在时延偏差；串行时序无偏差但不满足实时性要求。需开发无延迟、非倍率步长(non-multirate)的混合仿真协议。

### 4.2 前沿研究方向

**1. 数据驱动与AI增强等值**
- 基于深度学习的参数辨识替代传统Prony分析
- 神经网络逼近非线性网络等值，处理饱和、死区等强非线性

**2. 宽频带统一等值框架**
- 融合FDNE（宽频）与动态等值（低频），构建全频段统一等值模型
- 发展考虑频率相关特性的多层等值（表层线路模型+深层FDNE）

**3. 实时仿真优化**
- 基于模型预测控制的在线等值参数更新（更新周期从10 ms缩短至ms级）
- FPGA异构计算架构下的FDNE流水线优化，突破3396计算量阈值限制

**4. 标准化与自动化**
- 自动确定最优等值端口位置（基于可观性/可控性分析）
- 自适应模型阶数选择算法（根据频响特性自动调整极点数）

**5. 新型电力系统适配**
- 构网型变换器(Grid-Forming)的暂态等值，考虑虚拟惯量与频率耦合
- 直流电网故障自清除能力等值（全桥子模块比例$\eta$对等值模型影响）

### 4.3 关键开放问题

- **无源性与精度权衡**：无源性强制算法可能引入附加误差，如何在保证严格无源性的同时最小化精度损失（当前最优<0.5%）仍是挑战。
- **多物理场等值**：如何将热、机械等慢动态与电磁暂态统一等值，支持电-热-机耦合仿真。
- **不确定性量化**：等值模型参数不确定性对仿真结果置信度的影响评估方法。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[transmission-line-model-for-variable-step-size-simulation-algorithms|Transmission line model for variable step size simulation al]] | 1999 |
| [[transmission-line-modeling-with-explicit-grounding-representation|Transmission Line Modeling with Explicit Grounding Represent]] | 2002 |
| [[zfunction-convolution-in-ehv|Z.function convolution in EHV]] | 2002 |
| [[state-equation-approximation-of-transfer-matrices-and-its-application-to-the-pha|State equation approximation of transfer matrices and its ap]] | 2004 |
| [[time-domain-modeling-of-external-systems-for-electromagnetic-transients-programs|Time domain modeling of external systems for electromagnetic]] | 2004 |
| [[time-domain-modeling-of-external-systems-for-electromagnetic-transients-programs|Time domain modeling of external systems for electromagnetic]] | 2004 |
| [[time-domain-modeling-of-external-systems-for-electromagnetic-transients-programs|Time domain modeling of external systems for electromagnetic]] | 2004 |
| [[含统一潮流控制器装置的电力系统动态混合仿真接口算法研究|含统一潮流控制器装置的电力系统动态混合仿真接口算法研究]] | 2005 |
| [[电力系统机电暂态和电磁暂态混合仿真程序设计和实现|电力系统机电暂态和电磁暂态混合仿真程序设计和实现]] | 2006 |
| [[电力系统机电暂态和电磁暂态混合仿真程序设计和实现|电力系统机电暂态和电磁暂态混合仿真程序设计和实现]] | 2006 |
| [[real-time-transient-simulation-based-on-a-robust|Real-Time Transient Simulation Based on a Robust]] | 2007 |
| [[saturation-in-transient-and-stability-phenomena-for-cylindrical-13&14|Saturation in Transient and Stability Phenomena for Cylindri]] | 2012 |
| [[the-recongurable-hardware-real-time-and|The Reconﬁgurable-Hardware Real-Time and]] | 2012 |
| [[time-domain-transformation-method|Time Domain Transformation Method]] | 2012 |
| [[基于频率相关网络等值的电磁-机电暂态解耦混合仿真|基于频率相关网络等值的电磁-机电暂态解耦混合仿真]] | 2012 |
| [[电磁机电暂态混合仿真中机电侧故障的仿真方法|电磁–机电暂态混合仿真中机电侧故障的仿真方法]] | 2012 |
| [[电磁机电暂态混合仿真中机电侧故障的仿真方法|电磁–机电暂态混合仿真中机电侧故障的仿真方法]] | 2012 |
| [[电磁机电暂态混合仿真中的频率相关网络等值|电磁–机电暂态混合仿真中的频率相关网络等值]] | 2012 |
| [[模块化多电平换流器戴维南等效整体建模方法|模块化多电平换流器戴维南等效整体建模方法]] | 2015 |
| [[模块化多电平换流器戴维南等效整体建模方法|模块化多电平换流器戴维南等效整体建模方法]] | 2015 |
| [[基于电流轨迹相似度的双馈风电机群电磁暂态同调分群方法|基于电流轨迹相似度的双馈风电机群电磁暂态同调分群方法]] | 2017 |
| [[基于电流轨迹相似度的双馈风电机群电磁暂态同调分群方法|基于电流轨迹相似度的双馈风电机群电磁暂态同调分群方法]] | 2017 |
| [[unified-high-speed-emt-equivalent-and-implementation-method-of-mmcs-with-single-|Unified High-Speed EMT Equivalent and Implementation Method ]] | 2018 |
| [[双端口子模块mmc电磁暂态通用等效建模方法|双端口子模块MMC电磁暂态通用等效建模方法]] | 2018 |
| [[适用于交直流混联电网的ch-mmc电磁暂态快速仿真模型-15|适用于交直流混联电网的CH-MMC电磁暂态快速仿真模型]] | 2019 |
| [[time-domain-implementation-of-damping-factor-white-box-transformer-model-for-inc|Time-Domain Implementation of Damping Factor White-Box Trans]] | 2020 |
| [[适用于电磁暂态仿真的变阶变步长3s-dirk算法|适用于电磁暂态仿真的变阶变步长3S-DIRK算法]] | 2020 |
| [[review-and-comparison-of-frequency-domain-curve-fitting-techniques-vector-fittin|Review and comparison of frequency-domain curve-fitting tech]] | 2021 |
| [[级联h桥型电力电子变压器的闭锁状态等效建模方法-33|级联H桥型电力电子变压器的闭锁状态等效建模方法]] | 2021 |
| [[考虑中间变压器饱和特性的电容式电压互感器宽频非线性模型|考虑中间变压器饱和特性的电容式电压互感器宽频非线性模型]] | 2021 |
| [[structure-preserving-aggregation-method-for-doubly-fed-induction-generators-in-w|Structure Preserving Aggregation Method for Doubly-Fed Induc]] | 2022 |
| [[using-the-exact-equivalent-x03c0-circuit-of-transmission-lines-for-electromagnet|Using the Exact Equivalent &#x03C0;-Circuit of Transmission ]] | 2022 |
| [[中-国-电-机-工-程-学-报-34|中  国  电  机  工  程  学  报]] | 2022 |
| [[协调分布式潮流控制器串并联变流器能量交换的等效模型|协调分布式潮流控制器串并联变流器能量交换的等效模型]] | 2022 |
| [[协调分布式潮流控制器串并联变流器能量交换的等效模型|协调分布式潮流控制器串并联变流器能量交换的等效模型]] | 2022 |
| [[大规模电力电子设备接入的电力系统混合仿真接口技术综述|大规模电力电子设备接入的电力系统混合仿真接口技术综述]] | 2022 |
| [[大规模电力电子设备接入的电力系统混合仿真接口技术综述|大规模电力电子设备接入的电力系统混合仿真接口技术综述]] | 2022 |
| [[模块化多电平换流器电磁暂态模型研究综述|模块化多电平换流器电磁暂态模型研究综述]] | 2022 |
| [[混合型mmc全状态高效电磁暂态仿真方法研究|混合型MMC全状态高效电磁暂态仿真方法研究]] | 2022 |
| [[电力系统机电-电磁混合仿真边界解耦算法研究|电力系统机电-电磁混合仿真边界解耦算法研究]] | 2022 |
| [[电力系统电磁暂态实时仿真中并行算法的研究|电力系统电磁暂态实时仿真中并行算法的研究]] | 2022 |
| [[电力系统电磁暂态实时仿真中并行算法的研究|电力系统电磁暂态实时仿真中并行算法的研究]] | 2022 |
| [[级联h桥型电力电子变压器的电磁暂态等效建模方法|级联H桥型电力电子变压器的电磁暂态等效建模方法]] | 2022 |
| [[级联h桥型电力电子变压器的电磁暂态等效建模方法|级联H桥型电力电子变压器的电磁暂态等效建模方法]] | 2022 |
| [[高频隔离型电力电子变压器电磁暂态加速仿真方法与展望|高频隔离型电力电子变压器电磁暂态加速仿真方法与展望]] | 2022 |
| [[switch-averaged-frequency-domain-simulation-of-photovoltaic-systems|Switch-Averaged Frequency Domain Simulation of Photovoltaic ]] | 2023 |
| [[unified-mana-based-load-flow-for-multi-frequency-hybrid-acdc-multi-microgrids|Unified MANA-based load-flow for multi-frequency hybrid AC/D]] | 2023 |
| [[一种级联h桥型电力电子变压器电磁暂态解耦与仿真模型|一种级联H桥型电力电子变压器电磁暂态解耦与仿真模型]] | 2023 |
| [[交直流电力系统分割并行电磁暂态数字仿真方法|交直流电力系统分割并行电磁暂态数字仿真方法]] | 2023 |
| [[多类型子模块mmc电磁暂态通用建模和实现方法|多类型子模块MMC电磁暂态通用建模和实现方法]] | 2023 |
| [[大功率链式statcom电磁暂态快速等效建模和误差评估|大功率链式STATCOM电磁暂态快速等效建模和误差评估]] | 2023 |
| [[大功率链式statcom电磁暂态快速等效建模和误差评估|大功率链式STATCOM电磁暂态快速等效建模和误差评估]] | 2023 |
| [[新能源高占比电力系统电磁暂态并行仿真的优化分网方法|新能源高占比电力系统电磁暂态并行仿真的优化分网方法]] | 2023 |
| [[新能源高占比电力系统电磁暂态并行仿真的优化分网方法|新能源高占比电力系统电磁暂态并行仿真的优化分网方法]] | 2023 |
| [[电力系统数字混合仿真技术综述及展望|电力系统数字混合仿真技术综述及展望]] | 2023 |
| [[电力系统数字混合仿真技术综述及展望|电力系统数字混合仿真技术综述及展望]] | 2023 |
| [[shooting-method-based-modular-multilevel-converter-initialization-for-electromag|Shooting method based modular multilevel converter initializ]] | 2024 |
| [[基于模块化多电平换流器的超级电容储能系统高效仿真方法|基于模块化多电平换流器的超级电容储能系统高效仿真方法]] | 2024 |
| [[大规模海上风电场电磁暂态受控源解耦加速模型|大规模海上风电场电磁暂态受控源解耦加速模型]] | 2024 |
| [[电力系统风力发电建模与仿真研究综述|电力系统风力发电建模与仿真研究综述]] | 2024 |
| [[realization-of-rational-models-for-tower-footing-grounding-systems|Realization of rational models for tower-footing grounding s]] | 2025 |
| [[sfa-emt-hybrid-simulation-of-power-systems-application-to-hvdc-systems|SFA-EMT hybrid simulation of power systems: Application to H]] | 2025 |
| [[simplified-emt-model-of-multiple-active-bridge-based-power-electronic-transforme|Simplified EMT Model of Multiple-Active-Bridge Based Power E]] | 2025 |
| [[stability-assessment-of-multi-rate-electromagnetic-transient-simulations|Stability Assessment of Multi-Rate Electromagnetic Transient]] | 2025 |
| [[z-tool-frequency-domain-characterization-of-emt-models-for-small-signal-stabilit|Z-Tool: Frequency-domain characterization of EMT models for ]] | 2025 |
| [[改善暂态稳定性的多构网型变换器频率同步协同控制|改善暂态稳定性的多构网型变换器频率同步协同控制]] | 2025 |
| [[改善暂态稳定性的多构网型变换器频率同步协同控制|改善暂态稳定性的多构网型变换器频率同步协同控制]] | 2025 |
| [[适用于电网频率响应分析的直驱型风电场实用化等值方法|适用于电网频率响应分析的直驱型风电场实用化等值方法]] | 2025 |
| [[stability-improved-network-partition-based-on-a-small-step-synthesis-model-for-e|Stability-improved network partition based on a small-step s]] | 2026 |