## 一种级联 H 桥型电力电子变压器电磁暂态解耦与仿真模型
## Electromagnetic Transient Decoupling and Simulation Model of Cascaded H-bridge Power Electronic Transformer

许明旺 1，马嘉昊 1，李蕴红 2，王潇 2，姚蜀军 1，汪燕 1，韩民晓 1
（1．华北电力大学电气与电子工程学院，北京市 昌平区 102206；2．华北电力科学研究院有限责任公司，北京市 西城区 100045）

XU Mingwang1, MA Jiahao1, LI Yunhong2, WANG Xiao2, YAO Shujun1, WANG Yan1, HAN Minxiao1
(1. School of Electrical and Electronic Engineering, North China Electric Power University, Changping District, Beijing 102206, China; 2. North China Electric Power Research Institute Co., Ltd., Xicheng District, Beijing 100045, China)

**ABSTRACT:** The detailed electromagnetic transient model of the power electronic transformer (PET) has the problems of high matrix dimension, small simulation step and slow speed. Based on the semi-implicit delay decoupling electromagnetic transient simulation, this paper applies it to the electromagnetic transient fast simulation research of the cascaded H-bridge power electronic transformer (CHB-PET), and proposes a decoupling and fast simulation with simple decoupling circuit, constant admittance matrix, and easy parallel and high simulation efficiency. In this paper, first, based on the state equation, a semi-implicit delay decoupling model of dual active bridge (DAB) was established by using the matrix splitting and the delay technique. Then, the equivalent decoupling value path was given when the outer port and the cascaded H-bridge adopted different series and parallel combinations. The fine-grained decoupling of each transformation stage and between different modules were realized. The calculation flow was given, and the characteristics of the method were analyzed. Finally, an example is given to verify the accuracy and effectiveness of the proposed method.

**KEY WORDS:** electromagnetic transient simulation; semi-implicit delay decoupling; cascaded H-bridge power electronic transformer; fine-grained decoupling; parallel computing

**摘要：** 电力电子变压器电磁暂态详细模型存在矩阵维数高、仿真步长小、速度慢的问题。基于半隐式延迟解耦电磁暂态仿真方法，该文将其应用于级联 H 桥型电力电子变压器的电磁暂态快速仿真研究中，提出一种解耦电路简单、导纳矩阵恒定、易于并行、仿真效率高的解耦和快速仿真方法。该文首先从状态方程出发，利用矩阵分裂和延迟技术，建立双有源桥的半隐式延迟解耦模型；然后给出外端口及级联 H 桥采用不同串、并联组合时的等值解耦电路，实现了各变换级以及不同模块间的细粒度解耦，给出了计算流程，并分析了方法的特点。最后，通过算例验证了该文方法的准确性和有效性。

**关键词：** 电磁暂态仿真；半隐式延迟解耦；级联 H 桥型电力电子变压器；细粒度解耦；并行计算

**DOI：** 10.13335/j.1000-3673.pst.2022.0448

**基金项目：** 国家自然科学基金项目(52077077)；冀北电力科学研究院科技项目(KJZ2021029)。
**Project Supported by** National Natural Science Foundation of China (52077077); Science and Technology Foundation of North China Electric Power Research Institute Co., Ltd.(KJZ2021029).

## 0 引言
随着电力系统的日益电力电子化，电力电子变压器(power electronic transformer，PET)成为新能源并网和直流电网中实现电压等级变换及功率路由的一种重要设备[1-3]。高功率、大容量场景中，通常采用隔离型 PET，其以双有源桥(dual active bridge，DAB)为中间级，可实现功率大小和方向的灵活调控[4]。DAB 单元外接级联 H 桥(cascaded H-bridge，CHB)后，外部端口通过串并联组合可构成多模块级联的级联 H 桥型 PET (cascaded H-bridge PET，CHB-PET)[5-6]。一般来说，高功率 PET 的模块众多、拓扑复杂、开关频率高，电磁暂态仿真面临着规模大、矩阵维数高、仿真速度慢等诸多挑战。

文献[7-9]主要针对 CHB-PET 的 PET 控制策略进行研究，其仿真采用传统的详细模型，由于高频变压器的影响，只能选取较小的仿真步长，仿真速度缓慢。

文献[10]基于平均值模型对 DAB 单元进行暂态情况下的仿真研究。文献[11]针对双有源桥谐振变换器提出一种平均值模型，即通过 RL 组合支路对变压器进行等效，再将直流电流一个周期内的值用平均电流等效。文献[12]应用平均值模型对单台 PET 的稳态情况进行仿真验证，并且和开关模型进行了对比。总体来说，平均值模型只关注变换器的外特性而忽略内部动作，仿真精度不高，无法计及设备的内部特性。

文献[13-14]针对 PET 提出一种提速模型。通过将高频链变压器的原、副边进行一步约等，实现高、低压侧解耦，进而通过嵌套快速求解法消去内部节点，最终得到高、低压解耦的双端口等值电路。文献[15]提出一种基于节点导纳方程预处理的输入串联输出并联(input series output parallel，ISOP)型 DAB 变换器双端口解耦等效模型，原理与上述方法相同。一方面，一步约等即为一步延时的前向欧拉，限制了仿真精度和步长的提高；另一方面，PET 外部电气量反解其内部电路更新历史电流源的过程，会由于内部电路拓扑复杂而极大影响计算效率。此外，将该方法拓展到多有源桥(multi active bridge，MAB)或者具有类似文献[16]复杂拓扑的中间级场景时，解耦方法需要重新设计，通用性不佳。

文献[17]针对 PET 细模型仿真效率低下的问题，提出利用级间电容解耦的方法，将复杂的拓扑划分为多个子网络，再采取戴维南等效方法实现多模块拓扑的节点降维。该方法中的电容元件电压和电流间的一步延时解耦，实质上是显式前向欧拉法，其精度和稳定性均有限。此外，由于电容电流是非状态变量，当开关动作时，存在着非状态量突变。为了消除由此可能引起的数值振荡，需要在开关动作时将显式前向欧拉法切换为隐式的后退欧拉法，从而失去解耦特性，进而无法提高仿真速度。

文献[18]中提出一种具有普适性的半隐式延迟解耦方法用于电磁暂态仿真。本文将该方法应用于 PET 电磁暂态快速仿真的研究。基于该方法，一方面，可实现 PET 各级电路和子模块间的细粒度解耦与并行仿真。另一方面，解耦后的系统导纳矩阵恒定，可消除因开关高频动作引起的导纳矩阵频繁下、上(lower and upper，LU)三角矩阵重分解而带来的巨大计算量。此外，由于是状态变量之间的解耦(电容电压和电感电流)，因此当开关动作时，不存在为消除非状态变量突变引起的数值振荡而切换解耦变量积分算法的问题(中心积分切换为后退欧拉)，因而能够始终保持解耦形式的一致性和计算的可并行性。

本文根据半隐式延迟解耦方法的原理，首先，从 DAB 的状态方程出发，利用矩阵分裂和延迟技术，建立 PET 的半隐式解耦模型；然后，给出外端口及级联 H 桥采用不同串、并联组合方式时的等值解耦电路，实现各变换级以及不同模块间的细粒度解耦，给出了计算流程，并分析了方法的特点。最后，通过算例验证了本文方法的准确性和有效性。

## 1 级联 H 桥型 PET 拓扑
根据电压等级与功能的不同，PET 的功率模块连接方式多样，图 1 为常用的一种级联 H 桥型 PET 三相拓扑，由 DAB 模块和端口电路构成，图中 $U_a$、$U_b$、$U_c$ 分别为三相电源电压，$L_{11}$ 为桥臂电感。

**图 1 ISOP 型 PET 连接图**
**Fig. 1 Connection diagram of ISOP type PET**

## 2 级联 H 桥型 PET 解耦
半隐式延迟解耦方法从系统的状态方程出发，通过矩阵分裂，利用中心积分与梯形积分的近似等效性，实现基于状态变量之间的半步延时解耦，既有隐式积分方法的高精度和数值稳定性，又有显式积分的并行性。半隐式延迟解耦方法的原理和特点分析详见文献[18]，本文不做详细介绍。下面将该方法应用于 CHB-PET 的解耦。

### 2.1 DAB 模块的解耦
DAB 是常见的中间级模块，如图 2(a)所示，图中 $i_1$、$i_2$ 分别为端口注入电流，$u_{C1}$、$u_{C2}$ 分别为端口电容电压，$i_{T1}$、$i_{T2}$ 分别为变压器绕组电流，$u_{T1}$、$u_{T2}$ 分别为变压器绕组电压，$T_{ij}$、$D_{ij}$ ($i=1,2$, $j=1,2,3,4$) 分别为开关管及其反并联二极管。将每个绝缘栅双极型晶体管(insulated gate bipolar transistor，IGBT)及与其反并联的二极管看成一个开关组，每个开关对电容 $C_1$、$C_2$，根据基尔霍夫电流定律(Kirchhoff current laws，KCL)可得：