# 基于 POD-αATS 的油浸变压器瞬态温升降阶自适应变步长计算方法
刘刚 1，郝世缘 1，胡万君 1，刘云鹏 1，李琳 2
(1．河北省输变电设备安全防御重点实验室(华北电力大学)，河北省 保定市 071003；
2．新能源电力系统国家重点实验室(华北电力大学)，北京市 昌平区 102206)

# Adaptive Variable Step Size Calculation Method for Transient Temperature Rise and Fall of Oil Immersed Transformer Based on POD-αATS
LIU Gang1, HAO Shiyuan1, HU Wanjun1, LIU Yunpeng 1, LI Lin2
(1. Hebei Provincial Key Laboratory of Power Transmission Equipment Security Defense (North China Electric Power University), Baoding 071003, Hebei Province, China; 2. State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources (North China Electric Power University), Changping District, Beijing 102206, China)

**ABSTRACT:** In response to the problem of low efficiency in calculating transient temperature rise of oil immersed power transformers, this paper proposes POD-αATS reduced order adaptive variable step size transient calculation method. First, the article briefly derives the finite element discrete equation for calculating the transient temperature rise of transformer windings. Next, the proper orthogonal decomposition (POD) order reduction algorithm is adopted to improve the problems of excessive number of conditions and equation orders in traditional transient calculations. Meanwhile, for the time step selection problem in transient calculations, this paper proposes a method suitable for nonlinear problems α ATS (adaptive time stepping based on α factor, αATS) variable step size strategy. Then, in order to verify the effectiveness of the method, this paper establishes a two-dimensional eight zone numerical calculation model based on the basic structure of the 110 kV oil-immersed power transformer winding, and compares the calculation results with the temperature rise experimental results based on the 110 kV winding. The numerical calculation and experimental results show that the accuracy of the proposed algorithm is almost the same as that of the full order fixed step algorithm in the flow field and temperature field, the efficiency of flow field calculation is improved by about 45 times, and the efficiency of temperature field calculation is improved by about 38 times, significantly improving the calculation speed. This has also been verified in temperature rise experiments, which fully demonstrates the accuracy, efficiency, and certain engineering practicality of the algorithm proposed in this paper.

**KEY WORDS:** αATS variable step size algorithm; proper orthogonal decomposition (POD) order reduction method; transient flow thermal coupling problem; fast calculation method; temperature rise experiment

**摘要：**针对油浸式电力变压器瞬态温升计算效率过低的问题，该文提出本征正交分解-αATS(proper orthogonal decomposition- adaptive time stepping based on α factor，POD-αATS)降阶自适应变步长瞬态计算方法。首先，推导变压器绕组瞬态温升计算的有限元离散方程；其次，采用 POD 降阶算法改善传统瞬态计算中存在的条件数过大及方程阶数过高的问题；同时对于瞬态计算中的时间步长选择问题，提出适用于非线性问题的αATS 变步长策略；然后，为验证方法的有效性，基于 110 kV 油浸式电力变压器绕组的基本结构建立二维八分区数值计算模型，同时将计算结果与基于 110 kV 绕组的温升实验结果进行对比。数值计算及实验结果表明，所提算法与全阶定步长算法在流场和温度场中的精度几乎相同，且流场计算效率提升约 45 倍，温度场计算效率提升约 38 倍，计算速度得到显著提高。这一点在温升实验中同样得到验证，说明该文所提算法的准确性、高效性及一定的工程实用性。

**关键词：**αATS 变步长算法；本征正交分解降阶方法；瞬态流热耦合问题；快速计算方法；温升实验

基金项目：国家重点研发计划项目(2021YFB2401700)。
National Key R&D Program of China (2021YFB2401700).

## 0 引言
随着人工智能、大数据等现代计算机技术的不断发展，大型电力设备的数字化监测和管理已逐渐成为当下电网建设的趋势。作为电力系统中重要的一次设备，油浸式电力变压器的稳定运行对电网的安全意义重大，温升热点作为变压器设计和运维关注的重要指标之一，其分布和变化规律也是广大设计和运维人员关注的重点。

数值分析法作为获取油浸式电力变压器温升及热点的主要手段之一，其一般采用有限元[1-3]及有限体积法[4-5]。其中，有限元法及其改良方法在处理边界条件时复杂程度较有限体积法低且易于编程实现。刘成远等[6]采用有限元法对变压器绕组内的油流和温度进行计算，将得到的计算结果与实验进行比较，取得较为满意的结果；李建勋等基于有限元法针对磁场、流体场-温度场的多场耦合问题展开仿真计算，结果表明，所得结果与流体力学的理论相符合，证明有限元模型的有效性[7]。同时，最小二乘有限元[8]及迎风有限元[9]等基于传统伽辽金有限元方法的改良方案近年来也逐渐应用于绕组温升的计算当中。刘刚等[10-11]应用混合有限元法分别解决油浸式电力变压器稳态及瞬态温升问题，研究表明，该方法能够在保证计算精度的条件下解决传统伽辽金有限元法存在的数值振荡问题。但是由于非线性材料属性、非周期边界条件等影响，加之实际模型尺寸一般较大，绕组的瞬态温升计算一般较慢，且当涉及快速的时间响应和场的急剧变化时，除非时间步长选择得很小，否则很难确定响应峰值；小的时间步长也意味着需要大量的时间步数，这就使得计算的整体效率偏低；较大规模的实际模型还会使得求解的离散方程组阶数偏高，导致产生难以接受的步进计算成本。

在其他工程领域，目前较为常用的为基于传统截断误差的变步长策略[18-19]，该方法在线性问题中的效率及精度较为可观，但对于非线性问题，该方法的计算速度、准确度及步长变化的合理性均需进一步提高[20]。且将传统变步长方法应用于有限元方程中时，由于刚度矩阵阶数较高且病态的特性，有时还会出现计算不稳定的情况。

因此，基于上述问题及目前已有的方案，本文提出了 POD-αATS 降阶自适应变步长瞬态计算方法，如图 1 所示。

图1 POD-αATS 方法示意图
Fig. 1 POD-αATS method diagram

| 存在问题 | 解决方案 |
| :--- | :--- |
| ①方程阶数较高、条件数较大 | 单步计算过慢、计算不稳定 → 降阶算法 (POD降阶) |
| ②固定步长选择不当 | 时步过多或精度较低 → 变步长策略 (αATS变步长策略) |
| **综合** | **POD-αATS** |

首先，本文采用有限元方法推导油浸式电力变压器瞬态温升计算的控制方程，分析传统瞬态计算中的效率瓶颈；针对固定时步选择不当导致的时步过多或精度较低的问题，提出适用于非线性问题的 αATS(adaptive time stepping based on α factor)变步长策略，并应用于油浸式电力变压器绕组的流-热耦合温升计算中；其次，采用 POD 降阶算法解决传统瞬态计算中存在的条件数过大及方程阶数过高的问题来降低单步计算时间；同时，基于 110 kV 油浸式电力变压器的基本结构建立二维八分区分匝绕组数值计算模型，在此基础上验证了