---
title: "输电线路模型 (Transmission Line)"
type: model
tags: [transmission-line, bergeron, frequency-dependent, traveling-wave]
created: "2026-04-13"
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

## 相关主题
- [[frequency-dependent-modeling]]
- [[cable-modeling]]


## 论文方法分析
> 基于 56 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|| 状态空间法 | 3 | Accelerated frequency-dependent method of characteristics for the simu |
| 有理函数逼近 | 3 | Passivity Enforcement for Transmission Line Models |
| 递归卷积法 | 2 | A New Approach to Represent the Corona Effect and Frequency-Dependent  |
| 频变参数建模 | 2 | A wavelet transform-based method for improved modeling of transmission |
| 固定频率实部模态变换解耦 | 2 | Accelerated frequency-dependent method of characteristics for the simu |
| 状态变量法 | 2 | Analyses of the modifications in the pi circuits for inclusion of freq |
| 传输线理论 | 2 | Assessment of the transmission line theory in the modeling of multicon |
| 频变相域(FDPD)建模 | 2 | Development of phase domain frequency-dependent transmission line mode |
| FPGA硬件实现 | 2 | Development of phase domain frequency-dependent transmission line mode |
| 传输线理论建模 | 2 | High-frequency transients in buried insulated wires: Transmission line |
| 频率自适应暂态仿真 | 1 | 27&28/Multi-Scale and Frequency-Dependent Modeling of Electric Power T |
| 动态相量法（解析信号） | 1 | 27&28/Multi-Scale and Frequency-Dependent Modeling of Electric Power T |
| 频域傅里叶谱平移技术 | 1 | 27&28/Multi-Scale and Frequency-Dependent Modeling of Electric Power T |
| 多相模态分解 | 1 | 27&28/Multi-Scale and Frequency-Dependent Modeling of Electric Power T |
| 数值递归卷积 | 1 | 27&28/Multi-Scale and Frequency-Dependent Modeling of Electric Power T |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|| 输电线路 | 7 |
| 架空输电线路 | 7 |
| 多相输电线路 | 5 |
| 三相输电线路 | 3 |
| 通用线路模型（ULM） | 3 |
| 地下电缆 | 3 |
| 多导体传输线(MTL) | 3 |
| 通用线路模型(ULM) | 3 |
| 杆塔接地系统 | 3 |
| 电晕效应模型 | 2 |
| Bergeron分布参数模型 | 2 |
| π型等效电路 | 2 |
| 频变输电线路模型 | 2 |
| 架空线路 | 2 |
| 多导体地下电缆系统 | 2 |
### 验证方式分布
- **仿真对比**: 14 篇
- **仿真**: 10 篇
- **仿真/对比**: 9 篇
- **仿真与实验对比**: 4 篇
- **仿真与对比**: 4 篇
- **实验对比**: 1 篇
- **对比/现场测量数据**: 1 篇
- **仿真与文献实测数据对比**: 1 篇
- **仿真与对比验证**: 1 篇
- **仿真/实时数字仿真器(RTDS)验证**: 1 篇
- **仿真验证与对比**: 1 篇
- **对比/仿真**: 1 篇
- **仿真验证（利用ATP软件生成多场景暂态数据作为基准，与重构模型响应进行对比分析）**: 1 篇
- **实验与仿真对比**: 1 篇
- **实验与仿真对比验证**: 1 篇
- **仿真验证（频域与时域对比）**: 1 篇
- **仿真对比与实验数据验证**: 1 篇
- **数字故障仿真与现场录波数据对比验证**: 1 篇
- **实验**: 1 篇
- **仿真验证**: 1 篇
## 技术演进脉络
### 1996年 (1篇)
- **耦合长线电磁暂态分析的扩展Bergeron模型**
  - 💡 通过坐标变换将多相耦合线路解耦为集中电阻与无损线路并分别处理，实现了Bergeron模型向多相耦合长线的有效扩展。
  - 提出将多相耦合输电线路分解为集中电阻和无损线路两部分的处理方法。
  - 在不同坐标系中分别求解两部分，推导出适用于耦合长线的扩展Bergeron模型。
### 1999年 (2篇)
- **New multiphase mode domain transmission line model**
  - 💡 采用恒定实数变换矩阵结合理想变压器实现相模解耦，克服了传统频变复数矩阵在时域仿真中的实现难题。
  - 提出了一种基于模态域的新型多相输电线路模型，有效处理了纵向参数的频率依赖性。
  - 采用全频段恒定的实数变换矩阵结合理想变压器实现相模变换，解决了复数频变矩阵在时域程序中的实现难题。
- **Transmission line model for variable step size simulation algorithms**
  - 💡 提出了一种突破传统EMTP线路模型最大步长限制的输电线路建模方法，实现了电磁暂态与机电暂态仿真步长的动态自适应调整。
  - 提出了一种新型输电线路建模方法，突破了传统EMTP线路模型对仿真最大步长的限制。
  - 实现了在同一模型框架下对高频波传播现象和低频网络变化的准确高效仿真。
### 2001年 (3篇)
- **A wavelet transform-based method for improved modeling of transmission lines - P**
  - 💡 利用离散小波变换在时域仿真中动态处理模态变换矩阵的频率依赖性，突破了传统频变线路模型常数矩阵近似的精度瓶颈。
  - 提出了一种基于小波变换的输电线路时域建模方法，将模态变换矩阵的频率依赖性直接纳入仿真过程。
  - 克服了传统J. Marti模型中模态变换矩阵近似为常数矩阵的局限，提升了复杂杆塔与导线配置下的仿真精度。
- **Frequency-dependent transmission line modeling utilizing transposed conditions -**
  - 💡 通过引入恒定变换矩阵与降阶相域/模态模型相结合的混合架构，在利用线路连续换位特性的同时兼顾了高精度与高计算效率。
  - 提出一种结合恒定变换矩阵与降阶相域模型的混合线路建模方法
  - 在保持全相域模型精度的同时显著提升电磁暂态仿真计算效率
- **Modeling nonuniform transmission lines for time domain simulation of electromagn**
  - 💡 提出了一种基于行波理论、考虑参数频变特性且支持任意几何构型的连续非均匀输电线路时域建模方法，可直接嵌入EMTP等主流暂态仿真软件。
  - 提出了一种适用于多相非均匀输电线路的时域电磁暂态数学模型。
  - 模型充分考虑了线路参数的频率依赖性与空间连续性，克服了传统分段均匀或忽略频变特性的局限。
### 2002年 (1篇)
- **Transmission Line Modeling with Explicit Grounding Representation**
  - 💡 首次在电磁暂态仿真中显式集成接地系统，实现宽频带、不对称线路的高精度与高效率时域建模。
  - 提出显式包含杆塔与变电站接地结构的输电线路新模型
  - 实现直流至数兆赫兹范围内线路参数的精确频率依赖表征
### 2003年 (1篇)
- **A simple and efficient method for including frequency-dependent effects in trans**
  - 💡 将复杂的频变分布式线路参数简化为无损分布式线路与简单L-R阻抗电路的组合，在保持高精度的同时大幅提升了EMTP时域仿真的计算效率。
  - 提出了一种将频变分布式参数线路等效为无损分布式线路与简单L-R阻抗电路组合的建模方法。
  - 基于四端参数理论推导频变阻抗电路，有效克服了传统实时卷积法计算耗时大、内存占用高及数值不稳定的缺陷。
### 2004年 (4篇)
- **Frequency-Dependent Transformation Matrices for Untransposed Transmission Lines **
  - 💡 首次将牛顿-拉夫逊法应用于非换位多回路架空线路的频变变换矩阵求解，实现了矩阵元素的光滑化与稳定有理逼近，突破了传统方法在宽频域下的不连续瓶颈。
  - 提出基于牛顿-拉夫逊法的频变变换矩阵计算方法，有效克服了传统对角化法在多回路架空线中矩阵元素不光滑的缺陷。
  - 证明了该方法生成的模态参数可被具有实负极点和零点的最小相移型有理函数精确拟合。
- **Mode domain multiphase transmission line model - use in transient studies - Powe**
  - 💡 首次将Clarke实数变换矩阵与模态π型合成电路结合，在EMTP时域环境中实现了全频段频变多相输电线路的高效精确建模。
  - 提出了一种基于模态域的多相输电线路新模型，有效处理了纵向参数的频率依赖性。
  - 采用Clarke实数变换矩阵作为全频段唯一变换矩阵，并通过理想变压器在EMTP中实现，简化了相模变换过程。
- **Modelling of Single-Phase Nonuniform Transmission Lines in Electromagnetic Trans**
  - 💡 通过指数参数假设、频域有理函数综合与快速递归卷积的结合，首次实现了非均匀传输线模型在通用EMTP程序中的直接高效时域求解。
  - 提出了一种基于参数指数变化假设的单相非均匀传输线频域两端口方程模型。
  - 利用最小相移型有理函数对频变函数进行综合，实现了频域特性到时域的精确映射。
- **Real-time digital simulator of the electromagnetic transients of power transmiss**
  - 💡 首次将基于时域公式的数字信号处理技术应用于输电线路电磁暂态的实时仿真，实现了高精度、低成本的数字化替代方案。
  - 提出了一种基于时域公式的输电线路电磁暂态实时数字仿真器。
  - 实现了平衡与不平衡电源激励下三相输电线路的实时电磁暂态性能计算。
### 2008年 (2篇)
- **Earth Return Impedance of Overhead and Underground Conductors Considering Earth **
  - 💡 构建了统一涵盖架空与地下导体、多层非均匀土壤的广义地回路阻抗解析模型，并配套高效数值积分算法。
  - 推导了多层土壤中架空与地下导体排列的广义自阻抗和互阻抗解析表达式。
  - 证明了Carson、Pollaczek等现有经典阻抗公式均为该广义模型在特定近似下的特例。
- **Passivity Enforcement for Transmission Line Models**
  - 💡 提出结合人工并联电导、低通滤波与二阶校正项的无源性强制策略，从根本上解决ULM模型因无源性违规导致的EMT仿真不稳定问题。
  - 揭示了ULM中有理函数逼近易导致带外无源性违规并引发仿真不稳定的问题。
  - 提出通过添加人工并联电导和低通滤波分别抑制低频与高频带外无源性违规的实用方法。
### 2011年 (3篇)
- **Analyses of the modifications in the pi circuits for inclusion of frequency infl**
  - 💡 将特征线法与梯形积分法结合，并通过并联RL支路在状态变量框架下简化了输电线路频率相关特性的建模，实现了高精度与低计算复杂度的平衡。
  - 提出了一种结合特征线法与梯形积分法的简化数值算法，降低了电磁暂态仿真的使用门槛。
  - 系统分析了π型电路级联数量及并联RL支路数量对抑制数值振荡的影响并确定了其饱和极限。
- **Application of pi circuits for simulation of corona effect in transmission lines**
  - 💡 将简化π型电路、状态变量法与并联RL频率补偿相结合，并局部嵌入电晕模型，构建了一种兼顾精度、抗振荡能力与教学易用性的输电线路电磁暂态仿真方法。
  - 提出结合状态变量与π型电路的简化电磁暂态模型，便于本科教学与入门。
  - 引入并联RL模块以表征线路纵向参数的频率依赖性并有效抑制数值振荡。
- **Proposal of an alternative transmission line model for symmetrical and asymmetri**
  - 💡 提出了一种无需反变换的时域直接建模方法，可统一高效处理对称与非对称线路的稳态与快慢暂态混合仿真。
  - 提出了一种直接在时域建模三相输电线路的实用方法，避免了显式或隐式反变换的使用。
  - 针对非对称线路设计了修正程序，可获得实数且恒定的模态变换矩阵以实现相模解耦。
### 2012年 (1篇)
- **Modal Domain Based Modeling of Parallel Transmission Lines**
  - 💡 通过独立FD-line结合宽频有理耦合模型与模态揭示变换，突破了传统FD-line恒定变换矩阵在平行线路互耦仿真中的精度瓶颈。
  - 提出将独立FD-line模型与宽频状态空间有理模型相结合的混合建模架构，以精确表征平行线路间的互耦效应。
  - 引入模态揭示变换技术，有效防止相间模态被共模分量掩盖，显著提升耦合计算精度。
### 2015年 (1篇)
- **Application of Frequency-Partitioning Fitting to the Phase-Domain Frequency-Depe**
  - 💡 将频率分区拟合技术引入相域频变线路建模，结合自适应加权与数值增强策略，有效解决了传统矢量拟合在传播函数矩阵拟合中的局限性及模域模型的精度缺陷。
  - 成功将基于频率分区与自适应加权的线性系统辨识方法应用于相域频变输电线路建模。
  - 提出了针对传播函数矩阵拟合的数值增强技术，有效处理了模态行波时间差导致的阶跃响应拟合难题。
### 2017年 (3篇)
- **27&28/Multi-Scale and Frequency-Dependent Modeling of Electric Power Transmissio**
  - 💡 提出基于动态相量频域自适应平移与π型段自动插入的多尺度频变线路建模方法，实现电磁与机电暂态的统一高效仿真
  - 提出了一种适用于宽频带多尺度仿真的频变输电线路模型
  - 利用动态相量与解析信号实现频域自适应平移，有效减少时域离散步长并提升计算效率
- **Modal decoupling of overhead transmission lines using real and constant matrices**
  - 💡 首次量化分析了线路长度对模态解耦精度的影响，并明确了Clarke矩阵在长线路EMT仿真中的适用优势。
  - 证明了恒定实数模态变换矩阵的近似精度同时受频率相关参数和线路长度的影响。
  - 系统评估并对比了单一恒定矩阵法与频变解耦结合Clarke矩阵法两种模态解耦流程的精度。
- **Single-ended travelling wave-based protection scheme for double-circuit transmis**
  - 💡 首次将单端行波特征与交叉差动电流偏差相结合，利用双回线环路传播特性实现无需通信通道的快速、可靠内部故障判别。
  - 提出了一种适用于双回输电线路的单端行波保护新方案。
  - 利用故障与健全回路构成的环路特性分析行波传播规律以实现扰动检测。
### 2018年 (2篇)
- **Accelerated frequency-dependent method of characteristics for the simulation of **
  - 💡 提出一种加速的频变特征线法实现方案，通过拓扑降阶、稀疏求解、变量后处理及时间离散误差校正，在保证精度的同时大幅提升多导体传输线时域仿真的计算效率与内存利用率。
  - 利用系统电路拓扑结构有效减少状态方程数量。
  - 对状态空间矩阵进行分组并引入稀疏技术加速常微分方程组求解。
- **Partitioned Fitting and DC Correction for the Simulation of Electromagnetic Tran**
  - 💡 提出分区拟合与直流校正相结合的两阶段策略，在避免宽频拟合数值病态的同时，精准还原了线路/电缆的直流与低频暂态响应。
  - 提出了一种两阶段拟合程序，通过排除近直流频段进行初步拟合，显著改善了方程组的数值条件。
  - 引入了针对近直流频段样本的校正项，有效解决了传统方法在低频/直流区域拟合精度差的问题。
### 2019年 (1篇)
- **Accelerated frequency-dependent method of characteristics for the simulation of **
  - 💡 通过融合拓扑降阶、稀疏求解、内存优化与离散误差校正，实现了频率相关特征线法在多导体传输线时域仿真中的高效加速。
  - 提出利用系统电路拓扑结构减少状态方程数量的优化策略。
  - 通过状态空间矩阵分组与稀疏技术加速常微分方程组求解。
### 2020年 (3篇)
- **Partitioned fitting and DC correction in transmission line/cable models for wide**
  - 💡 提出结合高频分区拟合与独立直流校正的两阶段策略，在宽频EMT仿真中同步实现高精度直流响应与数值稳定性。
  - 提出两阶段分区拟合程序，将高频拟合与低频直流校正分离处理。
  - 提供基于分区拟合的状态空间实现的时域实现细节。
- **Simulation of electromagnetic transients with Modelica, accuracy and performance**
  - 💡 将声明式、方程驱动的Modelica语言引入EMT仿真领域，突破了传统命令式编程的封闭架构，实现了高可读、易维护且性能可靠的暂态建模新范式。
  - 系统验证了声明式方程语言Modelica在电磁暂态(EMT)仿真中的可行性与核心优势。
  - 基于Modelica成功开发了输电线路的常参数(CP)与宽频(WB)两种高精度模型。
- **Time-Domain Modeling of Transmission Line Crossing Using Electromagnetic Scatter**
  - 💡 首次将电磁散射理论引入传输线建模，提出SFTL模型以克服传统MTL理论在非均匀交叉结构建模中的局限性。
  - 提出基于电磁散射理论的SFTL模型，可精确计算交叉区域空间变化的单位长度参数矩阵。
  - 突破传统MTL理论对无限长均匀导线的假设限制，实现了对非均匀交叉线路的时域建模。
### 2021年 (5篇)
- **An improved passivity enforcement algorithm for transmission line models using p**
  - 💡 首次将并联无源RLC滤波器直接引入传输线节点以物理电路方式强制实现模型无源性，避免了复杂的数学优化与矩阵运算。
  - 提出了一种基于并联无源RLC滤波器的简单有效的无源性强制方法。
  - 将该算法成功应用于EMT软件中广泛使用的通用线路模型(ULM)。
- **Development of phase domain frequency-dependent transmission line model on FPGA **
  - 💡 首次在FPGA平台上实现全流水线并行化的频变相域输电线路模型，并结合定制48位浮点架构实现高精度、低步长的实时电磁暂态仿真。
  - 提出并实现了适用于实时电磁暂态仿真的FPGA频变相域输电线路模型
  - 采用全流水线与并行化硬件架构设计，实现了最低仿真时间步长
- **Development of phase domain frequency-dependent transmission line model on FPGA **
  - 💡 将频变相域输电线路模型通过全流水线并行架构与自定义高精度浮点格式在FPGA上实现，突破了传统EMT仿真在实时性与精度上的瓶颈。
  - 提出了一种适用于EMT实时数字仿真器的FPGA频变相域(FDPD)输电线路模型。
  - 通过硬件级全流水线与并行化架构设计，实现了极低的仿真时间步长。
- **Full-wave black-box transmission line tower model for the assessment of lightnin**
  - 💡 突破传统简化杆塔模型精度不足的局限，将全波电磁场仿真与EMT兼容黑盒建模结合，实现含频变土壤特性的杆塔暂态过电压高精度评估。
  - 建立了基于全波频域麦克斯韦方程的电磁场仿真模型，精确计及杆塔几何细节与土壤参数频变特性。
  - 提取了兼容EMT时域仿真的杆塔黑盒（宏）模型，克服了传统简化模型误差大的问题。
- **Modeling of overhead transmission lines for trapped charge discharge rate studie**
  - 💡 首次系统评估传统频变模型在残余电荷放电仿真中的局限性，并确立宽带模型作为该场景下的标准建模方法。
  - 提出适用于架空线路残余电荷放电研究的EMT建模指南
  - 揭示传统频变模型因拟合局限导致放电仿真结果不一致的问题
### 2022年 (8篇)
- **A modified implementation of the Folded Line Equivalent transmission line model **
  - 💡 提出了一种基于正交矩阵的FLE模型电路实现方法，摆脱了特征线法的限制，允许使用大于线路传播延迟的仿真步长而不损失精度。
  - 提出了一种用于三相输电线的折叠线等效模型的改进电路实现方法。
  - 设计了一种替代正交矩阵，实现了参数、电压和电流到FLE域的双向直接电路转换。
- **A New Approach to Represent the Corona Effect and Frequency-Dependent Transmissi**
  - 💡 将电晕电压依赖性与线路参数频率依赖性统一嵌入传输线本构方程，提出物理一致且完全兼容EMT求解器的VFDLM建模方法。
  - 提出VFDLM模型，将电晕效应与线路频变特性直接耦合于传输线方程中。
  - 采用递归卷积与矢量拟合技术求解时域行波方程，实现诺顿等效表示。
- **Implementation of Modal Domain Transmission Line Models in the ATP Software**
  - 💡 提出基于理想变压器阵列的Clarke模态变换电路实现方案，使用户能在ATP等EMT软件中灵活自定义并集成新型输电线路模型。
  - 提出了一种基于理想变压器阵列的Clarke模态变换电路表示法，可直接在ATP-EMTP中实现模态解耦。
  - 构建了将自定义单相频变/频不变线路模型组合为三相换位线路的模块化仿真框架。
- **Influence of a lossy ground on the lightning performance of overhead transmissio**
  - 💡 将考虑位移电流与频变土壤参数的Sunde地回路阻抗公式创新性地嵌入时域EMT仿真器，显著提升了高阻土壤下输电线路雷击反击闪络率评估的准确性。
  - 提出了一种在时域仿真器中结合Sunde公式与Marti线路模型的替代实现方法，用于精确计算地回路阻抗。
  - 系统评估了频变土壤参数和位移电流对138 kV和230 kV架空输电线路直击雷反击闪络率的影响。
- **Low-complexity graph-based traveling wave models for HVDC grids with hybrid tran**
  - 💡 首次将图论拓扑分析与物理-行为混合参数化行波模型相结合，实现了混合HVDC电网故障行波的低复杂度显式建模与区段识别。
  - 提出了一种结合物理传播特性与行为畸变特性的参数化行波建模方法。
  - 利用图论将电网拓扑抽象化，实现有限时间窗口内行波路径的系统性筛选与紧凑描述。
- **Time-Domain Coupling Model for Nonparallel Frequency-Dependent Overhead Multicon**
  - 💡 突破了传统EMT模型仅适用于无限长均匀线路的假设，首次构建了适用于非平行、频变多导体架空线路的时域闭式耦合模型。
  - 提出了一种适用于有损大地上方非平行、频变多导体架空线路的时域色散散射场传输线（DSFTL）模型。
  - 推导了该模型的时域闭式方程，并采用修正有限差分时域（MFDTD）算法进行高效数值求解。
- **Transient Analysis on Multiphase Transmission Line Above Lossy Ground Combining **
  - 💡 将矢量拟合技术与考虑频变土壤参数的Nakagawa模型结合集成至ATP工具，实现了多相输电线路雷击暂态的高精度仿真。
  - 系统评估了Carson与Nakagawa大地模型对ATP电磁暂态仿真结果的影响差异。
  - 对比了Bode法与矢量拟合技术在JMarti模型中逼近频变特征阻抗与传播函数的性能。
- **Using the Exact Equivalent &#x03C0;-Circuit of Transmission Lines for Electromag**
  - 💡 通过矢量拟合与RLC电路综合技术，将传统仅适用于频域或稳态的精确等效π型电路直接拓展至时域电磁暂态仿真，彻底规避了卷积与积分变换的计算瓶颈。
  - 提出了一种基于精确等效π型电路的时域输电线路模型，能够直接考虑线路参数的分布特性与频变效应。
  - 利用矢量拟合技术对π型电路导纳进行有理函数逼近，并综合为离散的RLC等效电路。
### 2023年 (6篇)
- **Algorithms for fast calculation of energization overvoltage of hybrid overhead l**
  - 💡 提出结合全频域频变参数、相模变换与改进NILT的解析算法，实现了混合线路合闸过电压的高精度快速计算，有效克服了传统EMT仿真耗时长的缺陷。
  - 提出了一种基于全频域频率相关参数的混合线路合闸过电压快速计算算法。
  - 结合相模变换与改进的数值拉普拉斯逆变换，实现了复频域到时域的高效解析转换。
- **Alternative method to include the frequency-effect on transmission line paramete**
  - 💡 提出一种通过独立求解各π型电路状态方程来直接时域建模频变输电线路参数的新方法，在保持高精度的同时实现了计算效率的百倍级提升。
  - 提出一种无需频时转换工具即可直接在时域包含频率效应的输电线路建模方法。
  - 通过独立求解每个π型电路的状态空间方程，有效降低了系统状态矩阵的阶数。
- **An Enhanced Method to Achieve Exact DC Values for Frequency-dependent Transmissi**
  - 💡 通过修改有理函数形式并引入加权因子强制实现0 Hz精确直流值，结合模型降阶技术，在提升低频拟合精度的同时优化了计算效率。
  - 提出改进的有理函数逼近方法，强制在0 Hz处实现精确的直流值。
  - 引入加权因子显著提升低频段拟合精度，改善时域响应特性。
- **Assessment of the transmission line theory in the modeling of multiconductor und**
  - 💡 首次以全波FDTD方法为基准，严格验证了传输线理论及导纳近似模型在多导体地下电缆快速暂态分析中的有效性与工程高效性。
  - 基于全波FDTD方法严格验证了传输线理论计算多导体地下电缆接地返回阻抗与导纳的准确性。
  - 系统评估了接地返回导纳闭式近似公式在暂态分析中的有效性。
- **Locating arc faults on coupling two parallel transmission lines using the novel **
  - 💡 提出基于新相模变换矩阵的时域测距算法，利用单一模量电弧电压电流转移特性结合最小二乘法，实现了对耦合双回线电弧故障的高精度、强抗干扰定位。
  - 推导了适用于耦合双回线系统的新相模变换矩阵，实现了单一模量反映所有故障类型。
  - 提出了一种基于新模量转移特性的时域故障定位算法，无需滤波且数据窗短。
- **Tower-foot grounding model for EMT programs based on transmission line theory an**
  - 💡 将经典Marti传输线模型与电报方程结合，构建了适用于EMT程序的高精度杆塔接地系统模型，有效平衡了雷电暂态仿真的精度与计算效率。
  - 提出了一种基于电报方程和Marti模型的杆塔接地系统EMT兼容模型。
  - 在ATP（Alternative Transients Program）中成功实现了该接地模型。
### 2024年 (4篇)
- **A waveform-dependence lightning impulse corona model in PSCAD/EMTDC for investig**
  - 💡 提出了一种结合临界体积法与电离弛豫过程的波形依赖性电晕模型，并采用无迭代算法实现其在PSCAD/EMTDC中的高效集成。
  - 提出了一种考虑波形依赖性的雷电冲击电晕模型，可准确计算不同波形下的电晕电容与电荷。
  - 基于临界体积法计算电晕起始延迟时间，并引入电离弛豫过程以精确描述空间电荷生成机制。
- **Comprehensive [formula omitted] impedance modeling of AC power-electronics-based**
  - 💡 首次将频率依赖型分布参数输电线路直接融入交流电力电子系统的宽频DQ阻抗模型中，实现了免时域仿真与FFT的精确稳态求解与谐波稳定性分析。
  - 提出了一种用于精确识别宽频DQ阻抗模型的时频解析方法。
  - 直接将具有分布参数和频率依赖特性的输电线路纳入阻抗模型，避免了有理逼近。
- **High-frequency transients in buried insulated wires: Transmission line simulatio**
  - 💡 首次构建埋地绝缘导线高频瞬态实验平台，为新型地回路参数公式在EMT仿真中的工程应用提供了关键实测依据。
  - 提供了埋地绝缘导线在快速瞬态激励下的首端电压/电流及末端电压的实测数据集。
  - 利用实测数据系统评估了最新地回路阻抗与导纳计算公式的准确性。
- **High-frequency transients in buried insulated wires: Transmission line simulatio**
  - 💡 首次构建并公开埋地绝缘导线高频暂态响应的实验数据集，为新型地回路参数计算公式在EMT仿真中的工程应用提供了关键验证依据。
  - 提供了埋地绝缘导线在快速暂态激励下的首端电压/电流及末端电压的实验测量数据。
  - 系统评估并验证了用于计算地下电缆地回路阻抗和导纳的最新理论公式的准确性。
### 2025年 (5篇)
- **Efficient modeling of parallel counterpoise wires using an FDTD-based transmissi**
  - 💡 提出了一种计及频变效应的FDTD传输线高效建模方法，并首次发现平行接地极的有效长度独立于其间距，显著简化了高压输电线路接地系统设计。
  - 提出了一种基于FDTD和传输线理论的高效平行接地极建模方法，并计及了纵向阻抗和并联导纳的频变效应。
  - 通过与严格电磁场模型对比验证了所提方法的准确性，全工况下偏差均低于5%。
- **Electromagnetic Transient Model Reconstruction of Generalized Power Transmission**
  - 💡 首次利用广域同步波形测量数据结合数值拉普拉斯变换，实现复杂工况下输电线路宽频电磁暂态黑盒模型的直接、高精度重构。
  - 提出了一种基于同步波形测量单元(WMU)记录的宽频输电线路电磁暂态模型重构方法。
  - 该方法统一适用于单相/三相、均匀/非均匀、换位/非换位及混合线路等多种复杂拓扑与参数变化场景。
- **Improving numerical efficiency of frequency dependent transmission line models f**
  - 💡 将模态截断与平衡截断降阶技术引入频率相关输电线路传播矩阵的近似过程，在保证精度的前提下突破大规模电缆系统EMT仿真的计算瓶颈。
  - 对比分析了模态截断与平衡截断两种降阶技术在降低传播矩阵阶数中的应用效果。
  - 显著提升了大规模电缆或架空线路系统在电磁暂态仿真中的数值计算效率。
- **Improving numerical efficiency of frequency dependent transmission line models f**
  - 💡 将模态截断与平衡截断两种模型降阶技术系统应用于频变输电线路传播矩阵的降阶，在保证仿真精度的前提下大幅提升了大规模电缆系统EMT仿真的数值效率。
  - 对比分析了模态截断与平衡截断两种模型降阶技术在频变线路传播矩阵降阶中的适用性与效果。
  - 显著提升了大规模多回路地下电缆系统在电磁暂态仿真中的数值计算效率与运行速度。
- **Influence of approximate internal impedance formula on half-wavelength transmiss**
  - 💡 首次系统量化了内部阻抗近似公式在半波长输电线路稳态与暂态分析中的误差传播机制及工程风险。
  - 系统评估了近似与精确内部阻抗公式在半波长输电线路及高波阻抗负载应用中的影响差异。
  - 揭示了近似公式在计算波阻抗负载(SIL)和电压时的精度下降问题及其对功率传输的限制。
## 关键发现汇总
- [1996] **耦合长线电磁暂态分析的扩展Bergeron模型**: 扩展模型能准确反映多相线路间的电磁耦合暂态过程。
- [1996] **耦合长线电磁暂态分析的扩展Bergeron模型**: 与传统Bergeron模型相比，暂态波形仿真精度显著提升。
- [1996] **耦合长线电磁暂态分析的扩展Bergeron模型**: 算法计算效率高，满足电磁暂态程序集成需求。
- [1999] **New multiphase mode domain transmission line model**: 在ATP-EMTP中成功完成了440 kV三相输电线路的模型实现与暂态仿真。
- [1999] **New multiphase mode domain transmission line model**: 与经典的Semlyen和JMarti频变模型对比，验证了该模型在电磁暂态计算中的精度与有效性。
- [1999] **New multiphase mode domain transmission line model**: 实数变换矩阵的引入消除了模态间的耦合，显著降低了多相线路时域仿真的计算复杂度。
- [1999] **Transmission line model for variable step size simulation al**: 新模型在CIGRE线路投切案例中准确复现了波传播与低频动态特性，且不受最小行波时间约束。
- [1999] **Transmission line model for variable step size simulation al**: 变步长仿真结果与采用极小固定步长的MICROTRAN参考解高度吻合，验证了模型的精度。
- [1999] **Transmission line model for variable step size simulation al**: 该方法在保证精度的前提下显著提升了跨时间尺度暂态仿真的计算效率。
- [2001] **A wavelet transform-based method for improved modeling of tr**: 在参数随频率剧烈变化的工况下，所提模型相比传统FD线路模型显著降低了模态解耦近似带来的误差。
- [2001] **A wavelet transform-based method for improved modeling of tr**: 仿真结果表明该方法能有效处理多相线路的频变特性，验证了其在电磁暂态分析中的优越性。
- [2001] **Frequency-dependent transmission line modeling utilizing tra**: 相比传统全相域模型，该混合模型的计算速度提升3至4倍
- [2001] **Frequency-dependent transmission line modeling utilizing tra**: 在连续换位条件下模型精度与全相域模型保持一致
- [2001] **Frequency-dependent transmission line modeling utilizing tra**: 模型能够准确处理任意几何结构与换位组合的多回路输电系统
- [2001] **Modeling nonuniform transmission lines for time domain simul**: 所提模型与频域数值拉普拉斯变换法及特征线法的仿真结果高度一致。
- [2001] **Modeling nonuniform transmission lines for time domain simul**: 模型计算结果与其他研究者报告的实验测试数据吻合良好，验证了其在实际非均匀线路暂态分析中的准确性。
- [2002] **Transmission Line Modeling with Explicit Grounding Represent**: 模型可准确预测雷击或操作过电压下的暂态地电位升
- [2002] **Transmission Line Modeling with Explicit Grounding Represent**: 阶跃响应矩阵结合线性卷积显著提升了时域仿真计算效率
- [2002] **Transmission Line Modeling with Explicit Grounding Represent**: 实际系统测试数据验证了模型在宽频带内的高精度
- [2003] **A simple and efficient method for including frequency-depend**: 该方法在地下电缆瞬态计算中的结果与高精度频域瞬态程序(FTP)高度吻合。
- [2003] **A simple and efficient method for including frequency-depend**: 相比传统实时卷积法，新方法显著降低了计算时间与内存需求，并消除了参数迭代中的数值不稳定现象。
- [2003] **A simple and efficient method for including frequency-depend**: 现场测试数据验证表明，该简化模型能够准确反映频率依赖效应对线路瞬态过程的影响。
- [2004] **Frequency-Dependent Transformation Matrices for Untransposed**: 牛顿-拉夫逊法求得的变换矩阵元素在1Hz至1MHz宽频范围内保持光滑且行为良好。
- [2004] **Frequency-Dependent Transformation Matrices for Untransposed**: 拟合后的有理函数可直接结合梯形积分法嵌入EMTP，实现稳定的时域数值计算。
- [2004] **Frequency-Dependent Transformation Matrices for Untransposed**: 相比传统对角化法，该方法计算效率显著提升，更适用于实际工程中的多回路非换位线路建模。
- [2004] **Mode domain multiphase transmission line model - use in tran**: 在440 kV三相线路的统计合闸过电压仿真中，该模型与Semlyen模型的瞬态响应结果高度吻合。
- [2004] **Mode domain multiphase transmission line model - use in tran**: 频率扫描分析表明，所提模型在全频段内能准确复现线路的模态阻抗与传播特性。
- [2004] **Mode domain multiphase transmission line model - use in tran**: 对于非换位线路，采用Clarke矩阵的准模态近似方法在垂直对称条件下误差极小，满足工程瞬态研究需求。
- [2004] **Modelling of Single-Phase Nonuniform Transmission Lines in E**: 所提模型的时域仿真结果与已发表的实验数据高度吻合。
- [2004] **Modelling of Single-Phase Nonuniform Transmission Lines in E**: 模型计算精度与将非均匀线离散为多段均匀线的级联模型结果一致，验证了其有效性。
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
| [[a-simple-and-efficient-method-for-including-frequency-dependent-effects-in-trans|A simple and efficient method for including frequency-depend]] | 2003 |
| [[frequency-dependent-transformation-matrices-for-untransposed-transmission-lines-|Frequency-Dependent Transformation Matrices for Untransposed]] | 2004 |
| [[mode-domain-multiphase-transmission-line-model-use-in-transient-studies-power-de|Mode domain multiphase transmission line model - use in tran]] | 2004 |
| [[modelling-of-single-phase-nonuniform-transmission-lines-in-electromagnetic-trans|Modelling of Single-Phase Nonuniform Transmission Lines in E]] | 2004 |
| [[real-time-digital-simulator-of-the-electromagnetic-transients-of-power-transmiss|Real-time digital simulator of the electromagnetic transient]] | 2004 |
| [[earth-return-impedance-of-overhead-and-underground-conductors-considering-earth-stratification-13&14|Earth Return Impedance of Overhead and Underground Conductor]] | 2008 |
| [[passivity-enforcement-for-transmission-line-models|Passivity Enforcement for Transmission Line Models]] | 2008 |
| [[analyses-of-the-modifications-in-the-pi-circuits-for-inclusion-of-frequency-infl|Analyses of the modifications in the pi circuits for inclusi]] | 2011 |
| [[application-of-pi-circuits-for-simulation-of-corona-effect-in-transmission-lines|Application of pi circuits for simulation of corona effect i]] | 2011 |
| [[proposal-of-an-alternative-transmission-line-model-for-symmetrical-and-asymmetri|Proposal of an alternative transmission line model for symme]] | 2011 |
| [[modal-domain-based-modeling-of-parallel-transmission-lines|Modal Domain Based Modeling of Parallel Transmission Lines]] | 2012 |
| [[application-of-frequency-partitioning-fitting-to-the-phase-domain-frequency-depe|Application of Frequency-Partitioning Fitting to the Phase-D]] | 2015 |
| [[2728multi-scale-and-frequency-dependent-modeling-of-electric-power-transmission-|27&28/Multi-Scale and Frequency-Dependent Modeling of Electr]] | 2017 |
| [[modal-decoupling-of-overhead-transmission-lines-using-real-and-constant-matrices|Modal decoupling of overhead transmission lines using real a]] | 2017 |
| [[single-ended-travelling-wave-based-protection-scheme-for-double-circuit-transmis|Single-ended travelling wave-based protection scheme for dou]] | 2017 |
| [[accelerated-frequency-dependent-method-of-characteristics-for-the-simulation-of-multiconductor-transmission-lines-05|Accelerated frequency-dependent method of characteristics fo]] | 2018 |
| [[partitioned-fitting-and-dc-correction-for-the-simulation-of-electromagnetic-tran|Partitioned Fitting and DC Correction for the Simulation of ]] | 2018 |
| [[accelerated-frequency-dependent-method-of-characteristics-for-the-simulation-of-|Accelerated frequency-dependent method of characteristics fo]] | 2019 |
| [[partitioned-fitting-and-dc-correction-in-transmission-linecable-models-for-wideb|Partitioned fitting and DC correction in transmission line/c]] | 2020 |
| [[simulation-of-electromagnetic-transients-with-modelica-accuracy-and-performance-|Simulation of electromagnetic transients with Modelica, accu]] | 2020 |
| [[time-domain-modeling-of-transmission-line-crossing-using-electromagnetic-scatter|Time-Domain Modeling of Transmission Line Crossing Using Ele]] | 2020 |
| [[an-improved-passivity-enforcement-algorithm-for-transmission-line-models-using-p|An improved passivity enforcement algorithm for transmission]] | 2021 |
| [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga--13&14|Development of phase domain frequency-dependent transmission]] | 2021 |
| [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga-|Development of phase domain frequency-dependent transmission]] | 2021 |
| [[full-wave-black-box-transmission-line-tower-model-for-the-assessment-of-lightnin|Full-wave black-box transmission line tower model for the as]] | 2021 |
| [[modeling-of-overhead-transmission-lines-for-trapped-charge-discharge-rate-studie|Modeling of overhead transmission lines for trapped charge d]] | 2021 |
| [[a-new-approach-to-represent-the-corona-effect-and-frequency-dependent-transmissi|A New Approach to Represent the Corona Effect and Frequency-]] | 2022 |
| [[a-modified-implementation-of-the-folded-line-equivalent-transmission-line-model-|A modified implementation of the Folded Line Equivalent tran]] | 2022 |
| [[implementation-of-modal-domain-transmission-line-models-in-the-atp-software|Implementation of Modal Domain Transmission Line Models in t]] | 2022 |
| [[influence-of-a-lossy-ground-on-the-lightning-performance-of-overhead-transmissio|Influence of a lossy ground on the lightning performance of ]] | 2022 |
| [[low-complexity-graph-based-traveling-wave-models-for-hvdc-grids-with-hybrid-tran|Low-complexity graph-based traveling wave models for HVDC gr]] | 2022 |
| [[time-domain-coupling-model-for-nonparallel-frequency-dependent-overhead-multicon|Time-Domain Coupling Model for Nonparallel Frequency-Depende]] | 2022 |
| [[transient-analysis-on-multiphase-transmission-line-above-lossy-ground-combining-|Transient Analysis on Multiphase Transmission Line Above Los]] | 2022 |
| [[using-the-exact-equivalent-x03c0-circuit-of-transmission-lines-for-electromagnet|Using the Exact Equivalent &#x03C0;-Circuit of Transmission ]] | 2022 |
| [[algorithms-for-fast-calculation-of-energization-overvoltage-of-hybrid-overhead-l|Algorithms for fast calculation of energization overvoltage ]] | 2023 |
| [[alternative-method-to-include-the-frequency-effect-on-transmission-line-paramete|Alternative method to include the frequency-effect on transm]] | 2023 |
| [[an-enhanced-method-to-achieve-exact-dc-values-for-frequency-dependent-transmissi|An Enhanced Method to Achieve Exact DC Values for Frequency-]] | 2023 |
| [[assessment-of-the-transmission-line-theory-in-the-modeling-of-multiconductor-und|Assessment of the transmission line theory in the modeling o]] | 2023 |
| [[locating-arc-faults-on-coupling-two-parallel-transmission-lines-using-the-novel-|Locating arc faults on coupling two parallel transmission li]] | 2023 |
| [[tower-foot-grounding-model-for-emt-programs-based-on-transmission-line-theory-an|Tower-foot grounding model for EMT programs based on transmi]] | 2023 |
| [[a-waveform-dependence-lightning-impulse-corona-model-in-pscademtdc-for-investiga|A waveform-dependence lightning impulse corona model in PSCA]] | 2024 |
| [[comprehensive-formula-omitted-impedance-modeling-of-ac-power-electronics-based-p|Comprehensive [formula omitted] impedance modeling of AC pow]] | 2024 |
| [[high-frequency-transients-in-buried-insulated-wires-transmission-line-simulation-19、20、21|High-frequency transients in buried insulated wires: Transmi]] | 2024 |
| [[high-frequency-transients-in-buried-insulated-wires-transmission-line-simulation|High-frequency transients in buried insulated wires: Transmi]] | 2024 |
| [[efficient-modeling-of-parallel-counterpoise-wires-using-an-fdtd-based-transmissi|Efficient modeling of parallel counterpoise wires using an F]] | 2025 |
| [[electromagnetic-transient-model-reconstruction-of-generalized-power-transmission|Electromagnetic Transient Model Reconstruction of Generalize]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f-23|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[influence-of-approximate-internal-impedance-formula-on-half-wavelength-transmiss|Influence of approximate internal impedance formula on half-]] | 2025 |