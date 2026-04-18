## 基于 UMEC 的双芯 Sen 变压器电磁暂态模型
卜亮，韩松，周超，冯金铃
（贵州大学 电气工程学院，贵州省 贵阳市 550025）

## Electromagnetic Transient Model of Two-core Sen Transformer Based on UMEC
BU Liang, HAN Song, ZHOU Chao, FENG Jinling
(School of Electrical Engineering, Guizhou University, Guiyang 550025, Guizhou Province, China)

**ABSTRACT:** This paper proposes an electromagnetic transient model of the two-core Sen transformer (TCST) based on the unified magnetic equivalent circuit (UMEC) in order to analyze its electromagnetic characteristics. Firstly, the TCST may be divided into the two parts of the series winding and the exciting winding so that their magnetic equivalent circuits are established based on their iron core structures respectively, according to the magnetic coupling relationships among the internal windings of the TCST. Secondly, with the mathematical expressions of the electromagnetic transient models derived by the UMEC method for the two parts separately, an electromagnetic transient model of the TCST can be acquired by the combination of the series winding and the exciting winding in the light of their electrical connections in the TCST. Finally, with the help of the MATLAB and the PSCAD/EMTDC, the analytical calculation and the time-domain simulation have been carried out, proving the effectiveness of the proposed model. In comparisons with the results involving the currents, the voltages and the power flows in the existing published papers, it is found that the current flowing through the tap-changers in the TCST is about 50% of the line current, which can effectively reduce the manufacturing cost of the tap-changer. Meanwhile, the actual adjustment step length of the TCST is about 0.5 times smaller than that of the single-core Sen transformer (SCST), which may lead to more accurate performance in the TCST.
**KEY WORDS:** Sen transformer; two-core structure; unified magnetic equivalent circuit; electromagnetic transient model; series compensating voltage

**摘要：** 为了分析 Sen 变压器(Sen transformer，ST)在双芯结构下的电磁特性，该文提出一种基于统一磁路模型(unified magnetic equivalent circuit，UMEC)法的双芯 Sen 变压器(two-core Sen transformer，TCST)电磁暂态模型。首先，根据 TCST 内部绕组的磁耦合关系，将 TCST 分为串联变和励磁变两部分，并基于各自的铁芯结构建立了它们的磁等值回路；其次，采用 UMEC 原理分别对上述两部分进行电磁暂态建模，并由 TCST 内部串–励部分之间的电气连接关系，将该串–励部分结合，继而构建了 TCST 的电磁暂态模型。最后，借助 MATLAB 和 PSCAD/EMTDC 进行了解析计算与时域仿真分析，验证了该文所提模型的有效性。通过与现有论文电流电压和功率结果的对比，发现流过 TCST 分接开关的电流约为线路电流的 50%，可有效降低分接开关的制造成本。同时 TCST 的实际调节步长相比于单芯结构的 ST(single-core Sen transformer，SCST)要小，约为 SCST 的 0.5 倍，使得其控制精度更高。
**关键词：** Sen 变压器；双芯结构；统一磁路模型；电磁暂态模型；串联电压补偿

DOI：10.13335/j.1000-3673.pst.2021.0095
文章编号：1000-3673（2021）08-3283-08  中图分类号：TM 721  文献标志码：A  学科代码：470·40
基金项目：贵州省普通高等学校科技拔尖人才支持计划(2018036)；贵州省科学技术基金(黔科合基础 20191100，2021277)。
Project Supported by Program for Top Science & Technology Talents in Universities of Guizhou Province (2018036); Guizhou Province Science and Technology Fund(20191100, 2021277).

## 0 引言
光伏、风能等新能源的大量接入以及电网结构的复杂化给电力系统带来了潮流分布不均衡、系统运行灵活性以及稳定性下降等问题[1-4]。潮流控制器能够改变系统的潮流分布，改善系统的动态运行特性，在提高电力系统运行的稳定性、可靠性和输电能力等方面发挥着重要的作用[5-7]。Sen 变压器(Sen transformer，ST)是一种电磁式潮流控制器，其通过控制补偿电压的幅值与相位来实现潮流调节[8]。相较于同等容量的统一潮流控制器(unified power flow controller，UPFC)，ST 的成本与损耗更低，具有良好的应用前景[9-10]。

从 ST 的拓扑结构发展角度来看，由于 ST 是通过控制副边绕组上的机械式分接开关来获取所需补偿电压，其调节属于离散调节，导致其潮流控制精度较差、调节速度慢。因此，文献[11-12]提出一种由 ST 与 UPFC 串联组成的混合式潮流控制器，其结合了 ST 大容量和高可靠性的优点和 UPFC 快速响应和控制精度高的优点，但是 ST 和 UPFC 之间协调控制较为复杂。文献[13-14]和[15]分别提出基于副边绕组反相的扩展型 Sen 变压器和采用带有反相开关的不对称分布绕组的 ST，有效提高了 ST 的控制精度，使得 ST 的调节具有更高的灵活性。上述文献所研究的 ST 均为单芯结构，单芯结构具有结构简单，绕组数少等优点，但是其副边绕组直接串联接入输电线路，由系统故障所产生的过电流和过电压会直接作用于调节绕组和分接开关，可能会导致设备损坏，也使得其绝缘成本和加工难度大幅增加[11,16-17]。从变压器的铁芯结构角度来看，双芯结构能够将调节绕组和分接开关从线路中隔离开来使其免于系统过电压和过电流的影响，使得分接开关的绝缘水平和成本大幅降低[17]，在特/超高压等应用场景中相较于单芯结构有一定优势。这也是双芯结构的移相变压器应用于特/超高压电网的潮流调控的原因[18-20]。因此，双芯结构的 ST 或是特/超高压场景下一种潜在应用形式。

从 ST 的建模研究角度来看，文献[21]提出由多个单相理想变压器组合的 ST 模型，其结构简单，但是忽略了多绕组耦合效应和铁芯饱和特性。文献[22]基于 BCTRAN 模型的构建方法提出 ST 的电磁暂态模型，其考虑了副边绕组的耦合效应以及铁芯饱和特性，但是未考虑铁芯的几何结构和磁通路径，而且忽略了涡流效应和磁滞效应。进而

## 1 TCST 的结构与原理
TCST 的结构如图 1 所示，TCST 励磁变原边为星形联结，并联接入电气系统送端，副边每相由 3 个带有载分接开关的绕组串联而成，构成补偿电压调节单元，并与串联变相连。其中，绕组 a1、b1、c1 组成励磁变副边 A 相输出电压 $U_{Ea}$，绕组 a2、b2、c2 组成励磁变副边 B 相输出电压 $U_{Eb}$，绕组 a3、b3、c3 组成励磁变副边 C 相输出电压 $U_{Ec}$。串联变由 3 个单相双绕组变压器组成，原边与励磁变副边相连，副边串联接入电气系统。以 A 相为例，$U_{Ea} = U_{a1} + U_{b1} + U_{c1}$，$U_{Ea}$ 经过串联变感应至线路，形成串联补偿电压 $\Delta U_A$。由于 $U_{a1}$、$U_{b1}$、$U_{c1}$ 之间的相角差为 $120^\circ$，通过调节励磁变副边绕组的抽头位置，从而改变串联补偿电压 $\Delta U_A$，达到调节线路潮流的目的。同理，亦可实现 B 相、C 相的潮流调节。