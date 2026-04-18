文章编号：1000-3673（2015）01-0257-07                   中图分类号：TM 721           文献标志码：A            学科代码：470·4051

## 模块化多电平换流器快速电磁暂态仿真模型
喻锋 1，王西田 1，林卫星 2，解大 1
（1．电力传输与功率变换控制教育部重点实验室(上海交通大学)，上海市 闵行区 200240；
2．强电磁工程与新技术国家重点实验室(华中科技大学)，湖北省 武汉市 430074）

## Fast Electromagnetic Transient Simulation Models of Modular Multilevel Converter
YU Feng1, WANG Xitian1, LIN Weixing2, XIE Da1
(1. Key Laboratory of Control of Power Transmission and Conversion(Shanghai Jiao Tong University), Ministry of Education, Minhang District, Shanghai 200240, China;
2. State Key Laboratory of Advanced Electromagnetic Engineering and Technology(Huazhong University of Science and Technology), Wuhan 430074, Hubei Province, China)

**ABSTRACT:** To shorten the time expended in electromagnetic transient simulation for modular multilevel converter (MMC), two kinds of fast simulation models are proposed. Through analyzing the principle of the sub-module of MMC, it is put forward to define the bridge arms of MMC as a detailed numerical calculation model, which is composed of a self-defined numerical calculation model and controlled voltage source; on the basis of this model, a simulation method for a hybrid model, which combines electromagnetic transient model of independent sub-module with numerical calculation model for common sub-module, is designed to remedy the defect that it is hard for numerical calculation model to simulate electromagnetic transient process of sub-module. To further improve simulation speed of this model, through simplifying the voltage balancing control of MMC and the difference among sub-modules an averaged model of numerical calculation is established. An MMC-HVDC model is constructed on a platform of PSCAD/EMTDC, and the effectiveness of the proposed fast numerical calculation models and hybrid simulation method are verified.

**KEY WORDS：** MMC; numerical calculation model; averaged model; hybrid model simulation method; electromagnetic transient simulations

**摘 要：** 针对模块化多电平换流器(modular multilevel converter，MMC)电磁暂态仿真耗时过长的问题，提出了2种MMC快速仿真模型。通过分析MMC子模块原理，提出将MMC桥臂等效为自定义数值计算模块与受控电压源组合的数值计算详细模型；并在该模型的基础上设计了一种将独立子模块电磁暂态模型和一般子模块数值计算模型结合的混合模型仿真方法，弥补了数值计算模型难以模拟子模块电磁暂态过程的缺陷。为了进一步提高模型的仿真速度，通过简化MMC的电压均衡控制及子模块状态的差异性，建立了数值计算平均值模型。在PSCAD/EMTDC上搭建MMC-HVDC模型，对所提出的快速仿真模型及仿真方法的有效性进行了验证。

**关键词：** 模块化多电平换流器；数值计算模型；平均值模型；混合模型仿真方法；电磁暂态仿真
**DOI：** 10.13335/j.1000-3673.pst.2015.01.039

基金项目：国家自然科学基金项目(51277119)。
Project Supported by National Natural Science Foundation of China(51277119)。

## 0 引言
随着电力电子技术发展，模块化多电平换流器(modular multilevel converter，MMC)以其高度模块化的结构、具有公共直流母线、便于工程实现的优点在高压直流输电(high-voltage direct current，HVDC)方向得到大力推广。采用较多电平数的模块化多电平换流器型高压直流输电(MMC-HVDC)可避免器件直接串联带来的均压问题，对交流电网的谐波影响也较小，成为了高压直流输电重点发展方向[1]。随着MMC-HVDC不断向更高的传输功率及直流电压等级发展，为了改善接入交流系统的波形质量、减小半导体器件的损耗以及解决器件耐压的限制，都需要提高MMC级联子模块数(sub-module，SM)[2]。由西门子公司承建的MMC-HVDC工程Trans Bay Cable Project，其额定容量为200 MW，单个桥臂串联200个子模块，双端系统共有2592个子模块[3]。随着级联数的增加，MMC内部包含的电力电子器件也将相应大幅增加，这无疑将极大降低MMC电磁暂态仿真计算的速度。MMC-HVDC具有有功无功独立控制、无需无功补偿、潮流翻转无需改变电压极性的优点，使其适于构建多端直流输电及直流电网[4-6]，而集合多个MMC的大型直流系统的仿真研究对现有模型适用性提出了新的挑战。因此设计一种适合大规模MMC仿真研究的计算快速、精度高及通用性强的模型具有重要意义。

国内外文献已就MMC建模问题开展了大量的研究工作。文献[7]将开关函数和瞬时功率结合，建立MMC的时域解析数学模型；但该模型不能用于电磁暂态仿真研究。文献[8]将绝缘栅双极型晶体管(insulated gate bipolar transistor，IGBT)与反并联二极管替换为断路器，减少了电力电子器件的数量，一定程度上实现仿真提速；但随着MMC电平数的增加，该方法仿真用时显著增长。文献[9]提出将MMC串联结构分解为独立的子模块及受控电压源组合方法(本文统称为分解模型)，在保证仿真精度的前提下，仿真速度显著提升；但对于超大规模的MMC，其分解后数目巨大的电力电子器件使其电磁暂态仿真计算仍然需要较长时间。文献[10]将子模块中串联半导体器件简化为可变电阻，将MMC转化为两端口戴维南电路，在保证仿真精度的前提下极大地提高了MMC模型电磁暂态仿真速度；但该方法采用封装及复杂的等效使其扩展性及用户友好度受到限制，且该方法不能模拟MMC子模块内部故障的电磁暂态过程。文献[11]在最近电平控制(nearest level control，NLC)的基础上建立了MMC平均值模型，然而该模型简化了子模块电容电压的波动规律，一定程度上改变了MMC的外特性。文献[12-13]对现有MMC模型的特性及仿真计算精度进行了比较总结，指出基于数值计算的MMC模型具有较高的精度；而现有的平均值模型在电磁暂态过程中的精度与传统模型存在一定差距。

以上分析表明对于涉及子模块内部电磁暂态过程，或者对于多端直流输电等大规模集成系统应用场合，现有模型仿真处理能力略显不足，为此本切，任意时刻保持同时投入的子模块总数为 $N$，可维持直流电压 $U_{dc}$ 恒定。通过上、下桥臂投入子模块个数变化跟踪控制系统解调电压，整个桥臂可等效为受控电压源[14]。图 2 为 MMC 中常采用的半 H桥型子模块(half-bridge SM，HBSM)，每个子模块主要由 2 个 IGBT 开关 $T_1$、$T_2$，2 个反并联二极管 $D_1$、$D_2$，及直流储能电容 $C$ 组成。图 2 中 $I_{RM}$、$U_{SM}$、$U_c$ 分别为桥臂电流、子模块端口电压和电容电压，$K_2$ 为晶闸管，当直流母线发生双极短路时，晶闸管导通，保护 IGBT 及二极管不被短路电流损坏[11]。

```
相单元
SM1 SM1 SM1
SM2 SM2 SM2
上桥臂 Udc/2
SMn SMn SMn
A B Udc O C
SM1 SM1 SM1 Udc/2
下桥臂 SM2 SM2 SM2
SMn SMn SMn -
```
**图 1 MMC 结构图**
*Fig. 1 Schematic of MMC*

```
T1
IRM
 UC
USM K2
T2

```
**图 2 子模块结构图**
*Fig. 2 Schematic of SM*

## 2 数值计算详细模型
### 2.1 数值计算详细模型
子模块