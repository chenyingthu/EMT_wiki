---
title: "电缆模型 (Cable)"
type: model
tags: [cable, underground, submarine, frequency-dependent, multi-core]
created: "2026-04-13"
---

# 电缆模型 (Cable)

## 概述

电力电缆（地下电缆、海底电缆）的EMT建模需要考虑集肤效应、邻近效应、绝缘层、护套接地等复杂因素。相比架空线路，电缆的电磁耦合更强，频率相关特性更显著。

## 主要特性

### 频率相关阻抗
- 导体集肤效应
- 邻近效应（多芯电缆）
- 护套涡流效应
- 螺线管效应（三芯铠装电缆）

### 导纳参数
- 绝缘层电容
- 护套接地
- 半导体层影响

### 暂态特性
- 行波传播
- 反射与折射
- 截断电荷
-  trapped charge放电

## 建模方法

### 相域模型
- 直接多导体建模
- 考虑相间耦合

### 模域模型
- 模态变换解耦
- 频率相关变换矩阵

### 频变模型
- 矢量拟合阻抗
- 无源性强制
- 递归卷积计算

## 特殊问题

- 海底电缆长距离暂态
- 多芯电缆螺线管效应
- 土壤电离化（接地故障）
- 混合架空线-电缆线路

## 相关方法
- [[vector-fitting]]
- [[passivity-enforcement]]

## 相关主题
- [[frequency-dependent-modeling]]
- [[transmission-line-model]]


## 论文方法分析
> 基于 28 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|| MoM-SO（矩量法-表面算子）理论 | 2 | A new tool for calculation of line and cable parameters |
| 数值拉普拉斯变换(NLT) | 2 | An accurate analysis of lightning overvoltages in mixed overhead-cable |
| 电磁暂态(EMT)仿真 | 2 | An Investigation of Electromagnetic Transients for a Mixed Transmissio |
| 准TEM近似法 | 2 | Earth return admittance impact on crossbonded underground cables |
| 部分分式展开(PFE) | 2 | Improvement of Numerical Stability for the Computation of Transients i |
| 约束线性最小二乘法 | 2 | Improvement of Numerical Stability for the Computation of Transients i |
| 有理函数逼近 | 2 | Improvement of Numerical Stability for the Computation of Transients i |
| 特征线法(MoC) | 2 | Improvement of Numerical Stability for the Computation of Transients i |
| 级联阻抗与并联导纳频变参数计算 | 1 | A new tool for calculation of line and cable parameters |
| 传统Line/Cable Constants与FEM对比分析 | 1 | A new tool for calculation of line and cable parameters |
| 闭式解析表达式评估 | 1 | Accuracy assessment of analytical expressions for the ground return im |
| 误差分析 | 1 | Accuracy assessment of analytical expressions for the ground return im |
| 参数灵敏度分析 | 1 | Accuracy assessment of analytical expressions for the ground return im |
| 电磁暂态仿真 | 1 | Accuracy assessment of analytical expressions for the ground return im |
| 幂等分解（Idempotent Decomposition） | 1 | Admittance-based modelling of cables and overhead lines by idempotent  |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|| 地下电缆 | 6 |
| 通用线路模型(ULM) | 6 |
| 架空线路 | 5 |
| 电力电缆 | 3 |
| 输电线路 | 2 |
| 地上电缆 | 2 |
| 电缆（Cables） | 2 |
| 地下电缆系统 | 2 |
| 频变相位模型(FDPM) | 2 |
| 多导体地下电缆系统 | 2 |
| 混合架空-地下线路 | 1 |
| 多分层土壤 | 1 |
| 绞合导线 | 1 |
| 双回路电缆系统 | 1 |
| 大地返回阻抗模型 | 1 |
### 验证方式分布
- **仿真/对比**: 9 篇
- **仿真对比**: 7 篇
- **仿真与对比**: 3 篇
- **仿真**: 3 篇
- **实验/测量对比**: 1 篇
- **仿真与对比验证**: 1 篇
- **仿真与实测对比**: 1 篇
- **实验**: 1 篇
- **电磁瞬态仿真与近似模型对比**: 1 篇
- **仿真验证与对比分析**: 1 篇
## 技术演进脉络
### 2010年 (2篇)
- **Improvement of Numerical Stability for the Computation of Transients in Lines an**
  - 💡 基于部分分式展开误差估计提出约束线性最小二乘拟合方法，从根本上解决了频变线路/电缆模型在时域卷积计算中的数值不稳定问题。
  - 提出基于传递函数参数估计时域卷积数值误差的量化方法
  - 推导留数与极点比值的约束条件以将时域误差限制在安全边界内
- **Improvement of Numerical Stability for the Computation of Transients in Lines an**
  - 💡 通过建立时域卷积数值误差与频域部分分式参数的映射关系，引入残差/极点比值约束实现相域稳定拟合。
  - 提出基于传递函数参数估计时域卷积数值误差的量化方法
  - 建立残差与极点比值的约束条件以将时域误差限制在安全边界内
### 2016年 (1篇)
- **An Efficient and Accurate Calculation of Electric Field and Temperature Distribu**
  - 💡 提出了一种基于实测复阻抗特性的通用方法，可快速构建适用于EMTP仿真的磁芯频率相关非线性集总参数等效电路。
  - 提出了一种基于复阻抗测量数据的磁芯频率相关非线性等效电路建模方法。
  - 构建了适用于kHz~MHz频段及kA级电流范围的通用集总参数模型。
### 2018年 (2篇)
- **Efficiently computing the electrical parameters of cables with arbitrary cross-s**
  - 💡 首次将二维矩量法与准静电场离散化相结合，突破了传统闭式近似公式对电缆几何形状的限制，实现了任意截面电缆并联导纳矩阵的高效精确提取。
  - 提出了一种基于二维矩量法的准静电场离散化公式，用于快速计算任意形状电缆的并联导纳矩阵。
  - 结合已有的串联阻抗提取方法，实现了电缆全频域单位长度电气参数的高效精确提取。
- **Partitioned Fitting and DC Correction for the Simulation of Electromagnetic Tran**
  - 💡 提出一种将低频拟合与直流校正分离的两阶段分区拟合策略，从根本上解决了传统宽频有理拟合在直流附近精度差且易引发数值不稳定的问题。
  - 提出仅针对低频样本的两阶段拟合流程，有效改善方程组的数值条件并降低拟合难度。
  - 引入直流校正项精确补偿近直流频段的带外样本，显著提升低频拟合精度。
### 2019年 (1篇)
- **Effects of cable insulations’ physical and geometrical parameters on sheath tran**
  - 💡 提出基于有限元暂态电流计算的介质损耗评估方法，并从过电压与损耗双重视角优化确定了电缆保护套的最优相对介电常数。
  - 系统研究了电缆绝缘物理与几何参数对护套暂态电压及绝缘损耗的影响机制。
  - 提出了一种基于有限元模型数值计算暂态电流的电缆绝缘介质损耗计算方法。
### 2020年 (3篇)
- **Analytical study of the frequency‐dependent earth conduction effects on undergro**
  - 💡 构建了适用于均匀与分层大地的频变大地参数精确解析框架，并首次量化给出了近似模型在地下电缆EMT仿真中的频率适用边界与分层模型选用准则。
  - 系统对比了新型大地阻抗/导纳精确公式与传统近似公式的计算差异
  - 明确了近似大地模型在电磁暂态仿真中适用的频率上限
- **Effect of frequency-dependent soil parameters on wave propagation and transient **
  - 💡 系统评估了多种频率相关土壤模型对多相地下电缆波传播及暂态特性的影响，并揭示了现有EMT仿真工具中FD土壤例程的局限性。
  - 系统总结并对比了多种频率相关土壤参数模型与独立实测数据。
  - 验证了Longmire/Smith模型在拟合实测土壤数据方面具有最佳吻合度。
- **Partitioned fitting and DC correction in transmission line/cable models for wide**
  - 💡 提出结合高频分区拟合与独立直流校正的两阶段策略，同步解决宽频线路模型中的数值不稳定与直流响应失真问题。
  - 提出两阶段分区拟合流程，将高频拟合与低频/直流校正分离处理。
  - 详细推导并给出了基于分区拟合的状态空间实现在时域EMT程序中的具体实现方法。
### 2021年 (4篇)
- **An accurate analysis of lightning overvoltages in mixed overhead-cable lines**
  - 💡 综合应用扩展传输线方法、频率相关土壤与接地模型，结合数值拉普拉斯变换，克服了传统恒定参数假设在高频雷电暂态分析中的精度局限。
  - 系统评估了扩展传输线方法、频率相关土壤模型及接地系统建模在暂态分析中的适用性。
  - 在频域内对比研究了经典与扩展传输线方法下架空线与电缆的波传播特性。
- **Earth return admittance impact on crossbonded underground cables**
  - 💡 量化了大地返回导纳（位移电流）对短段交叉互联地下电缆暂态过电压的阻尼效应，修正了传统保守建模的局限性。
  - 系统评估了大地返回导纳对交叉互联地下电缆暂态过电压的影响机制。
  - 针对1 km与300 m短段电缆长度开展对比，明确了导纳效应在短段中的显著性。
- **Modal propagation characteristics and transient analysis of multiconductor cable**
  - 💡 将频变土壤模型与同时修正阻抗和导纳的广义大地公式相结合，全面量化了其对多导体电缆系统模态传播与电磁瞬态特性的影响。
  - 提出了同时考虑大地导电效应对电缆串联阻抗和并联导纳影响的广义大地公式。
  - 将Longmire-Smith频变土壤模型引入多导体电缆系统的波传播特性分析中。
- **Multi-scale formulation of admittance-based modeling of cables**
  - 💡 将导纳建模、FLE变换与FAST变步长解析信号技术深度融合，突破了传统电缆模型的时间步长限制，实现了多尺度暂态的高效统一仿真。
  - 提出了一种基于相坐标的多尺度电缆模型，利用全耦合节点导纳矩阵替代传统的特征线法。
  - 采用折叠线等效（FLE）变换有效解决了节点导纳矩阵有理拟合过程中的精度问题。
### 2022年 (1篇)
- **Algorithm for fast calculating the energization overvoltages along a power cable**
  - 💡 将模态解耦与数值拉普拉斯逆变换相结合，突破了传统商业软件在电缆投切过电压计算中耗时长的瓶颈，实现了高精度与高效率的统一。
  - 提出了一种基于模态理论与数值拉普拉斯逆变换的快速计算电缆投切过电压的新算法。
  - 通过相模变换将耦合电缆导体解耦为独立模态，并在复频域推导电压解析公式。
### 2023年 (8篇)
- **A new tool for calculation of line and cable parameters**
  - 💡 将MoM-SO理论集成至EMT参数计算工具中，首次在同一框架内统一解决邻近效应、混合线路/电缆拓扑及多分层介质的精确建模问题。
  - 提出基于MoM-SO理论的新型参数计算工具，突破传统EMT软件内置程序的局限。
  - 实现集肤效应与邻近效应的精确建模，显著提升电缆暂态仿真精度。
- **Admittance-based modelling of cables and overhead lines by idempotent decomposit**
  - 💡 首次将幂等分解技术引入节点导纳矩阵的有理拟合过程，从根本上解决了低频最小特征值拟合失真问题，并实现了适用于任意长度线路的高效全耦合相域建模。
  - 提出了一种基于节点导纳矩阵幂等分解的电缆与架空线路新型建模方法。
  - 通过对幂等矩阵而非完整导纳矩阵进行有理拟合，有效克服了低频段最小特征值可观测性差的问题。
- **Algorithms for fast calculation of energization overvoltage of hybrid overhead l**
  - 💡 提出结合全频域频变参数、模态变换与改进NILT的解析算法，在保证工程精度的同时大幅降低混合线路合闸过电压的计算耗时。
  - 提出了一种基于全频域频率相关参数的混合线路合闸过电压快速计算算法。
  - 结合相模变换与改进的数值拉普拉斯逆变换(NILT)实现了频域到时域的高效转换。
- **An Investigation of Electromagnetic Transients for a Mixed Transmission System W**
  - 💡 提出基于精确大地返回阻抗公式的等效均匀大地法及混合输电系统参数建模新流程，突破了传统传输线理论在复杂混合线路EMT仿真中的精度瓶颈。
  - 推导了综合考虑空气、海水与海床介质的海底电缆大地返回阻抗精确表达式。
  - 基于精确公式提出了一种适用于海底电缆的新型等效均匀大地法(EHEM)。
- **Assessment of the transmission line theory in the modeling of multiconductor und**
  - 💡 首次基于全波FDTD基准严格验证了传输线理论及接地返回导纳闭式近似在多导体地下电缆快速暂态分析中的有效性、高精度与计算高效性。
  - 基于全波FDTD方法对传输线理论中两种接地返回阻抗/导纳计算方法进行了严格独立的验证。
  - 系统评估了用于计算地下电缆系统接地返回导纳的闭式近似公式的准确性与适用性。
- **Impact of solenoid effects on series impedance of three-core armoured cables**
  - 💡 首次系统构建三维有限元模型量化了螺线管效应对三芯铠装电缆串联阻抗及电磁暂态特性的影响，弥补了传统2.5D方法的精度缺陷。
  - 提出了基于有限元法的三维全电磁场模型，用于精确计算三芯铠装电缆在工频及高频下的串联阻抗。
  - 揭示了传统二维半(2.5D)方法因忽略螺线管效应而导致阻抗计算存在显著偏差的问题。
- **Morales 等 | A new tool for calculation of line and cable parameters**
  - 💡 将MoM-SO理论引入EMT参数计算，开发出兼顾高精度、复杂几何/环境建模能力与计算效率的统一化线路电缆参数计算工具。
  - 提出基于MoM-SO理论的新型参数计算工具，显著提升EMT仿真中线路与电缆参数的计算精度。
  - 实现了对集肤效应、邻近效应、多股绞线及多层土壤环境的精确建模。
- **Multi-Conductor Cable Modeling With Inclusion of Measured Coaxial Wave Propagati**
  - 💡 通过频域融合程序将实测同轴波传播特性无缝嵌入宽频多导体行波模型，实现了复杂接地电缆系统高频瞬态电压应力的精确仿真。
  - 提出将实测同轴波传播特性融入宽频多导体电缆模型的方法，显著提升高频电压波前阻尼的仿真精度。
  - 设计频域融合程序，在增强高频性能的同时对非共轴传播模式的影响极小。
### 2024年 (3篇)
- **Advanced Wideband Line/Cable Modeling for Transient Studies**
  - 💡 通过最小相位时延优化、自适应模式分组与衰减频率截断的协同改进，从根本上解决了大规模短距离线路/电缆EMT仿真中的数值不稳定难题。
  - 提出基于最小相位基的最优时延计算方法，有效降低传播函数相位振荡并提升拟合精度。
  - 设计基于时延接近度的自适应模式分组新策略，显著缓解高留数/极点比导致的数值不稳定问题。
- **Assessment of the accuracy of the modal-domain line models with real and frequen**
  - 💡 系统量化了实数频不变变换矩阵在含地线非对称架空线路电磁暂态仿真中的精度偏差，并明确了相域模型的适用边界。
  - 系统评估了采用实数且频不变变换矩阵的模态域线路模型在含地线架空线路电磁暂态仿真中的精度局限性。
  - 揭示了地线数量增加和土壤电阻率升高会显著加剧模态域模型的仿真电压误差。
- **Time-domain modeling of a subsea buried cable**
  - 💡 结合准TEM全波近似与EMT时域算法，首次实现了双损耗介质中海底埋设厚铠装电缆的高精度时域建模。
  - 提出了一种适用于EMT程序的海底埋设高压直流电缆时域建模方法。
  - 基于全波公式的准TEM近似推导单位长度参数，突破了传统EMT要求单一介质无损的限制。
### 2025年 (2篇)
- **Accuracy assessment of analytical expressions for the ground return impedance of**
  - 💡 确立并验证了De Conti-Lima闭式表达式在宽频带（至10 MHz）及宽间距地下电缆系统中计算大地返回阻抗的精度与稳定性优势，克服了传统近似公式的局限。
  - 系统评估了Saad-Gaba-Giroux与De Conti-Lima两种闭式表达式在计算大地返回阻抗时的性能差异。
  - 深入分析了两种表达式对土壤参数变化的敏感性及其在宽间距双回路电缆系统中的适用性。
- **Frequency and transient responses of A 275 kV pressure oil-filled cable: Model v**
  - 💡 针对传统管型电缆建模局限，建立了高精度的频率相关详细模型，并通过多工况现场实测数据全面验证了其在EMT暂态仿真中的可靠性。
  - 系统分析了275 kV充油电缆的频率响应与电磁暂态特性。
  - 深入研究了电缆内部传播特性（护套间模式与护套-管道模式）。
### 2026年 (1篇)
- **Time-delay estimation through all-pass functions for ULM line and cable models**
  - 💡 首次将全通函数与延迟均衡技术结合用于ULM时延估计，从根本上保证了有理拟合模型的因果性与最小相位特性。
  - 提出了一种基于全通滤波器和延迟均衡的迭代时延估计新方法。
  - 确保合成的传播矩阵H模型严格满足因果性和最小相位特性。
## 关键发现汇总
- [2010] **Improvement of Numerical Stability for the Computation of Tr**: 新方法有效消除了非整数倍仿真步长延迟导致的插值误差累积
- [2010] **Improvement of Numerical Stability for the Computation of Tr**: 约束拟合算法显著提升了频变线路与电缆模型在EMTP中的长期数值稳定性
- [2010] **Improvement of Numerical Stability for the Computation of Tr**: 所提方法可直接应用于各类多导体电力电缆与输电线路的宽频暂态仿真
- [2010] **Improvement of Numerical Stability for the Computation of Tr**: 新方法有效抑制了由非整数倍仿真步长延迟引起的插值误差
- [2010] **Improvement of Numerical Stability for the Computation of Tr**: 通过约束拟合使时域数值误差被严格限制在安全范围内
- [2010] **Improvement of Numerical Stability for the Computation of Tr**: 与现有模型对比验证表明该方法显著提升了宽频线路/电缆暂态计算的数值稳定性
- [2016] **An Efficient and Accurate Calculation of Electric Field and **: 模型在kHz至MHz频段及kA级电流范围内能准确复现磁芯的阻抗特性。
- [2016] **An Efficient and Accurate Calculation of Electric Field and **: 与实测数据对比验证了该等效电路模型在高频大电流暂态仿真中的高精度。
- [2018] **Efficiently computing the electrical parameters of cables wi**: 频域计算结果与有限元法（FEM）高度吻合，且在高频下显著优于传统近似公式。
- [2018] **Efficiently computing the electrical parameters of cables wi**: 该方法能够准确捕捉邻近效应和集肤效应对任意截面电缆阻抗和导纳矩阵的影响。
- [2018] **Efficiently computing the electrical parameters of cables wi**: 基于提取参数进行的EMTP时域暂态仿真运行稳定，计算时间合理，满足工程应用需求。
- [2018] **Partitioned Fitting and DC Correction for the Simulation of **: 两阶段拟合显著改善了低频段的数值条件，避免了传统宽频拟合中的大残差极点比问题。
- [2018] **Partitioned Fitting and DC Correction for the Simulation of **: 直流校正项确保了模型在直流处的精确响应，同时消除了高频段的非自然偏差。
- [2018] **Partitioned Fitting and DC Correction for the Simulation of **: 在HVDC线路/电缆算例中验证了FDM/DC方法相比传统ULM具有更高的电磁暂态仿真精度与稳定性。
- [2019] **Effects of cable insulations’ physical and geometrical param**: 在0-2ms暂态过程中，220kV电缆绝缘层与保护套产生的介质损耗分别为34.362 W/m和3.365 W/m。
- [2019] **Effects of cable insulations’ physical and geometrical param**: 绝缘相对介电常数与保护套厚度显著影响电缆电容、传播常数及护套最大过电压幅值。
- [2020] **Analytical study of the frequency‐dependent earth conduction**: 传统近似大地模型在高频段会引入显著误差，必须设定明确的频率使用边界
- [2020] **Analytical study of the frequency‐dependent earth conduction**: 分层大地结构与均匀大地假设下的波传播特性存在显著差异，不可随意忽略
- [2020] **Analytical study of the frequency‐dependent earth conduction**: 引入完整大地导纳与传播项的精确模型可大幅改善地下电缆宽频暂态响应的仿真精度
- [2020] **Effect of frequency-dependent soil parameters on wave propag**: Longmire/Smith模型与实测频率相关土壤数据的吻合度最高。
- [2020] **Effect of frequency-dependent soil parameters on wave propag**: 在100Hz下，高土壤电阻率引起的暂态响应衰减显著大于低电阻率情况。
- [2020] **Effect of frequency-dependent soil parameters on wave propag**: 采用不同土壤模型计算的交叉互联电缆暂态电压响应与现有EMT工具结果存在显著差异。
- [2020] **Partitioned fitting and DC correction in transmission line/c**: 分区拟合方法成功避免了大留数/极点比，彻底消除了时域仿真中的数值不稳定现象。
- [2020] **Partitioned fitting and DC correction in transmission line/c**: 该方法在不牺牲高频精度的前提下，准确复现了线路/电缆的直流稳态电压与电流。
- [2020] **Partitioned fitting and DC correction in transmission line/c**: 结合不同积分与插值方案的测试验证了该状态空间模型在宽频EMT研究中的鲁棒性与适用性。
- [2021] **An accurate analysis of lightning overvoltages in mixed over**: 频率相关土壤与接地特性会显著改变电缆护套过电压的峰值与波形。
- [2021] **An accurate analysis of lightning overvoltages in mixed over**: 传统恒定参数模型在kHz至MHz高频段会引入明显的雷电过电压计算误差。
- [2021] **An accurate analysis of lightning overvoltages in mixed over**: 扩展传输线方法结合NLT能准确复现混合线路的雷电暂态传播过程。
- [2021] **Earth return admittance impact on crossbonded underground ca**: 引入大地返回导纳显著提升了电缆暂态响应的阻尼水平。
- [2021] **Earth return admittance impact on crossbonded underground ca**: 在300 m短段长度及高土壤电阻率条件下，大地返回导纳对过电压的影响最为突出。
## 来源论文

| 论文 | 年份 |
|------|------|
| [[improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an-fix|Improvement of Numerical Stability for the Computation of Tr]] | 2010 |
| [[improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an|Improvement of Numerical Stability for the Computation of Tr]] | 2010 |
| [[an-efficient-and-accurate-calculation-of-electric-field-and-temperature-distribu|An Efficient and Accurate Calculation of Electric Field and ]] | 2016 |
| [[efficiently-computing-the-electrical-parameters-of-cables-with-arbitrary-cross-s|Efficiently computing the electrical parameters of cables wi]] | 2018 |
| [[partitioned-fitting-and-dc-correction-for-the-simulation-of-electromagnetic-tran|Partitioned Fitting and DC Correction for the Simulation of ]] | 2018 |
| [[effects-of-cable-insulations-physical-and-geometrical-parameters-on-sheath-trans|Effects of cable insulations’ physical and geometrical param]] | 2019 |
| [[analytical-study-of-the-frequencydependent-earth-conduction-effects-on-undergrou|Analytical study of the frequency‐dependent earth conduction]] | 2020 |
| [[effect-of-frequency-dependent-soil-parameters-on-wave-propagation-and-transient-|Effect of frequency-dependent soil parameters on wave propag]] | 2020 |
| [[partitioned-fitting-and-dc-correction-in-transmission-linecable-models-for-wideb|Partitioned fitting and DC correction in transmission line/c]] | 2020 |
| [[an-accurate-analysis-of-lightning-overvoltages-in-mixed-overhead-cable-lines|An accurate analysis of lightning overvoltages in mixed over]] | 2021 |
| [[earth-return-admittance-impact-on-crossbonded-underground-cables|Earth return admittance impact on crossbonded underground ca]] | 2021 |
| [[modal-propagation-characteristics-and-transient-analysis-of-multiconductor-cable|Modal propagation characteristics and transient analysis of ]] | 2021 |
| [[multi-scale-formulation-of-admittance-based-modeling-of-cables|Multi-scale formulation of admittance-based modeling of cabl]] | 2021 |
| [[algorithm-for-fast-calculating-the-energization-overvoltages-along-a-power-cable|Algorithm for fast calculating the energization overvoltages]] | 2022 |
| [[a-new-tool-for-calculation-of-line-and-cable-parameters|A new tool for calculation of line and cable parameters]] | 2023 |
| [[admittance-based-modelling-of-cables-and-overhead-lines-by-idempotent-decomposit|Admittance-based modelling of cables and overhead lines by i]] | 2023 |
| [[algorithms-for-fast-calculation-of-energization-overvoltage-of-hybrid-overhead-l|Algorithms for fast calculation of energization overvoltage ]] | 2023 |
| [[an-investigation-of-electromagnetic-transients-for-a-mixed-transmission-system-w|An Investigation of Electromagnetic Transients for a Mixed T]] | 2023 |
| [[assessment-of-the-transmission-line-theory-in-the-modeling-of-multiconductor-und|Assessment of the transmission line theory in the modeling o]] | 2023 |
| [[impact-of-solenoid-effects-on-series-impedance-of-three-core-armoured-cables|Impact of solenoid effects on series impedance of three-core]] | 2023 |
| [[morales-等-a-new-tool-for-calculation-of-line-and-cable-parameters|Morales 等 | A new tool for calculation of line and cable par]] | 2023 |
| [[multi-conductor-cable-modeling-with-inclusion-of-measured-coaxial-wave-propagati|Multi-Conductor Cable Modeling With Inclusion of Measured Co]] | 2023 |
| [[advanced-wideband-linecable-modeling-for-transient-studies|Advanced Wideband Line/Cable Modeling for Transient Studies]] | 2024 |
| [[assessment-of-the-accuracy-of-the-modal-domain-line-models-with-real-and-frequen|Assessment of the accuracy of the modal-domain line models w]] | 2024 |
| [[time-domain-modeling-of-a-subsea-buried-cable|Time-domain modeling of a subsea buried cable]] | 2024 |
| [[accuracy-assessment-of-analytical-expressions-for-the-ground-return-impedance-of|Accuracy assessment of analytical expressions for the ground]] | 2025 |
| [[frequency-and-transient-responses-of-a-275-kv-pressure-oil-filled-cable-model-va|Frequency and transient responses of A 275 kV pressure oil-f]] | 2025 |
| [[time-delay-estimation-through-all-pass-functions-for-ulm-line-and-cable-models|Time-delay estimation through all-pass functions for ULM lin]] | 2026 |