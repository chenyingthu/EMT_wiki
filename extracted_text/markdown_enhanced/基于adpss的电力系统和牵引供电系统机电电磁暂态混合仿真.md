文章编号：1000-3673（2014）07-1923-05 | 中图分类号：TM 721 | 文献标志码：A | 学科代码：470·4051

## 基于 ADPSS 的电力系统和牵引供电系统机电–电磁暂态混合仿真
徐家俊，王晓茹，王天钰，李宏强
（西南交通大学 电气工程学院，四川省 成都市 610031）

Electromagnetic-Electromechanical Transient Hybrid Simulation of Electric System and Traction Power Supply System Based on ADPSS
XU Jiajun, WANG Xiaoru, WANG Tianyu, LI Hongqiang
(School of Electrical Engineering, Southwest Jiaotong University, Chengdu 610031, Sichuan Province, China)

**ABSTRACT:** Recently it just built the detailed simulation model of traction power supply system in the study of the impact on the power system brought by traction power supply system. However the power system is generally replaced by simplified circuit in those models. There is not a joint simulation model of real power system and traction power supply system now. So it cannot further study the effect and influence between power system and traction power supply system. With the electromagnetic transient simulation model of the traction power supply system, this paper built an electromechanical-electromagnetic transient hybrid simulation model of real power system and traction power supply system based on advanced digital power system simulator(ADPSS). And it proves the accuracy of the hybrid simulation by comparing the result of hybrid simulation and that of electromagnetic transient simulation. It also studies the load characteristic of traction power supply system and the influence on the power system brought by the traction power supply system.

**关键词：**牵引供电系统；电力系统全数字仿真装置(ADPSS)；机电暂态；电磁暂态；混合仿真
**DOI：**10.13335/j.1000-3673.pst.2014.07.031

**摘要：**目前在牵引供电系统对电力系统的影响研究中，大多只单一对牵引供电系统建立详细仿真模型，而电力系统侧则是采用简化后的电路代替，缺乏一种实际电力系统与牵引供电系统的联合仿真模型，对电力系统–牵引供电系统的相互作用与影响认识不足。文中在牵引供电系统电磁仿真模型的基础上，基于电力系统全数字仿真装置(advanced digital power system simulator，ADPSS)搭建出了牵引供电系统与实际电网系统的机电–电磁暂态混合仿真模型，并将混合仿真计算结果与典型值相比较，验证了混合仿真的正确性，并研究分析了牵引供电系统负荷特性、牵引供电系统对电力系统的影响。

**KEY WORDS:** traction power supply system; advanced digital power system simulator; electromechanical transient; electromagnetic transient; hybrid simulation

## 0 引言
电铁牵引负荷是一种具有冲击性的单相整流负荷，因而会产生较大的谐波，这些谐波又经过牵引网注入到电网中，同时电力机车的突然接入还会造成电网电压的波动，谐波和电压波动都会对电网的电能质量造成影响[1-5]。

目前对牵引供电系统的详细仿真中，大多采用电磁暂态仿真，在仿真时需要对电力系统部分进行等值简化，但简化后的等值网络的各种特性很难与原网络相同，从而降低了计算分析的准确性，并且一旦电网系统运行方式发生变化，需要对网络进行重新简化，工作量较大[6]。也即现今缺乏一种实际电力系统与牵引供电系统联合仿真的模型，导致对电力系统–牵引供电系统的相互作用与影响认识不足。

电力系统全数字仿真装置(advanced digital power system simulator，ADPSS)是由中国电力科学研究院自主研制而成，在大规模电力系统实时仿真、机电暂态–电磁暂态混合仿真等关键技术上取得了理论创新和技术突破[7-13]。ADPSS可以应用于机电–电磁暂态混合仿真的模式，集中了电磁暂态仿真和机电暂态仿真各自的优点[6]。在对含有牵引变电站的大电网进行仿真时，由于牵引负荷为不对称负荷，且运行过程中产生谐波，相当于一个谐波源，因而牵引负荷必须建立其电磁暂态模型，而对于其余部分电网则构建其机电暂态仿真模型，并在仿真过程中保持2种模型的仿真同步性[14]。这样，既可以详细模拟牵引供电系统内部快速暂态变化过程，又能兼顾仿真系统规模，还不需要对电力系统部分进行等值简化，进而提高了仿真分析的准确性[15]。

本文基于牵引供电系统的电磁暂态模型，在ADPSS上搭建出牵引供电系统与实际电网系统的机电–电磁暂态混合仿真模型，并将混合仿真计算结果与典型值相比较，验证混合仿真的正确性，并研究分析牵引供电系统负荷特性及牵引供电系统对电力系统的影响。

## 1 电力系统的机电暂态模型
电力系统为牵引供电系统提供高压电源，其电压等级为110 kV或者220 kV。目前我国普通电气化铁路大多接入110 kV电网，而高速客运专线则接入220 kV电网。

本文混合仿真时电力系统采用四川某电网系统，在ADPSS上搭建出其机电暂态模型，此电网系统模型中共计有383个节点，其中包括122台变压器、77台发电机组、248回交流输电线路、10个牵引变电所以及98个负荷等，牵引变电所在机电暂态模型中等效为负荷。

## 2 牵引供电系统的电磁暂态模型
牵引供电系统主要由外部电源(电力系统)、牵引变电所、牵引网和电力机车等组成，其结构示意图如图1所示。

图1 牵引供电系统结构

外部电源也即电力系统；牵引变电所是连接外部电源和牵引网的纽带，主要元件是牵引变压器，本文电磁暂态模型中采用的是V/V牵引变压器；牵引网主要由接触网、回流线、馈线等组成，是将电能输送给电力机车的网络，参照文献[16]在ADPSS上搭建出牵引网的仿真模型；电力机车通过牵引电机及其变换和控制机构，将电能转化为可用机械能，牵引列车运行，参照文献[17]在ADPSS上搭建出韶山4型电力机车的仿真模型。

本文在ADPSS上搭建了详细的牵引供电系统电磁暂态模型，牵引供电系统采用的是AT供电方式，牵引网采用单线双臂，左右2条供电臂均长20 km，每10 km设置一个AT所，2辆电力机车分别运行在2条供电臂距牵引变电所5 km处，电力机车运行在牵引工况(第IV段)，电力系统由理想电压源代替，基于此进行电磁暂态仿真。

仿真时间设为 3 s，且机车在仿真时间内一直运行。左臂机车的电流 $I_L$ 波形如图 2 所示，并测出其谐波含量。可以看出波形是畸变的，含有大量谐波。

图 2 机车电流波形

在对韶山 4 型电力机车的研究过程中，人们也总结了机车电流的各次谐波含量的典型值[18]，将本文所得到的牵引供电系统电磁仿真结果中各次谐波含量与典型统计值比较，结果如表 1 所示。

表1 电磁仿真结果与典型统计值的谐波含量对比
| 参数 | 谐波含量/% | | | | |
|---|---|---|---|---|---|
| | 3次 | 5次 | 7次 | 9次 | 11次 |
| 典型统计值 | 23 | 12 | 7 | 4 | 3 |
| 机车取流 $I_L$ | 23.980 4 | 14.532 7 | 5.724 03 | 4.655 77 | 2.780 74 |

由表 1 可知，电磁仿真结果与典型统计值基本相近，本文所搭建的牵引供电系统电磁暂态模型是正确的。

## 3 牵引供电系统与实际电网的机电–电磁暂态混合仿真
### 3.1 ADPSS混合仿真的步骤
基于ADPSS进行机电–电磁暂态混合仿真时，通常有以下几个步骤[6]：
1）建立实际电网系统的机电暂态模型，并进行潮流计算。
2）根据具体情况确定分网方案，合理划分机电暂态子网和电磁暂态子网。
3）根据网络的划分情况，建立电磁暂态子网的仿真模型，并添加机电暂态接口，填写电磁暂态的初始潮流。