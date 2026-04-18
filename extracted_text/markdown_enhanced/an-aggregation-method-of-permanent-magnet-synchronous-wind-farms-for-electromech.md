## 用于电磁暂态仿真分析的永磁同步发电机风电场模型聚合方法
### An Aggregation Method of Permanent Magnet Synchronous Generators Wind Farm Model for Electromagnetic Transient Simulation Analysis
杨晓波，岳程燕，谢海莲
（ABB(中国)有限公司，北京市 朝阳区 100015）
YANG Xiaobo, YUE Chengyan, XIE Hailian
(ABB (China) Company Limited, Chaoyang District, Beijing 100015, China)

**ABSTRACT:** An aggregation method to build the model of large-scale wind farm utilizing permanent magnet synchronous generators (PMSG), which is used in the electromagnetic transient analysis of the wind farm, is presented. A simplified transient model of PMSG-based wind farm is built and the simulation results from the simplified transient model and those from corresponding detailed electromagnetic transient simulation model are compared and verified. The response characteristics of PMSG unit under various power grid faults are analyzed; on this basis two kinds of wind farm simulation models, namely a detailed model of wind farm, which consists of forty PMSGs and the capacity of each PMSG is 5MW, and an equivalent aggregation model with the capacity of 200MW for the very wind farm, are built. The aggregation principle for the aggregation model of wind farm is researched and the aggregation course for the aggregation model of 200MW wind farm is given. Through the comparative research on the behaviors of the two kinds of models during the wind farm faults, the influences of step-up transformers and the network inside the wind farm on the aggregation model are analyzed to verify the correctness and effectiveness of the proposed aggregation model.

**KEY WORDS:** permanent magnet synchronous generators (PMSG); wind farm; aggregation model; simulation

**摘要：** 给出了一种用于大规模永磁同步发电机(permanent magnet synchronous generator，PMSG)风电场电磁暂态仿真分析的聚合模型的建模方法。建立了含 PMSG 的风电场简化电磁暂态仿真模型，对简化模型及其对应的全仿真模型的仿真结果进行了对比验证。分析了在不同电网故障情况下 PMSG 风力发电机组的响应特性。在此基础上，建立了 2 种风电场仿真模型：包含 40 台 5 MW 风力发电机组模型的风电场全仿真模型及其 200 MW 等效聚合模型。讨论了风电场聚合模型的聚合原则，给出了 200 MW 风电场模型的聚合过程。通过对 2 种模型在风电场故障过程中特性的对比研究，分析了风电场内部升压变压器和集电线路对聚合模型的影响，验证了该聚合模型的正确性和有效性。

**关键词：** 永磁同步发电机；风电场；聚合模型；仿真

## 0 引言
近年来，全球风力发电装机容量持续增加。截至 2009 年，全球风力发电装机总量已达 157.9 GW。根据预测，到 2013 年，风电将提供全球电力的 3.35%，而到 2018 年，这个数字将增长到 8%。在较高的风电穿透功率下，风电场的动态特性将影响电网的稳定性；准确的风电场模型也帮助电力部门更合理地选择风电场接入点以及配套的无功补偿设备。目前，用于系统研究的风电场模型可以分为 2 类：1）由多台风力发电机组模型和风电场内部的电网模型组成的全仿真风电场模型。这种建模方法可以研究风电场内部的一些故障特性以及发电机组之间的相互影响。其缺点是模型过于庞大，对仿真工具要求苛刻。2）风电场聚合模型。研究表明，在电磁暂态仿真过程中，大规模风场的特性与其中单一风力发电机组的特性一致[1]，因此可以采用简化的风电场模型，该简化模型通过将单台风力发电机组在容量上进行放大，极大地降低了仿真计算量，目前应用得较广泛。无论采用何种模型，风力发电机的类型都会对风电场在电网故障下的响应特性产生不同影响。

目前得到广泛应用的风力发电机组可分为 4 种类型[2]：1）采用鼠笼感应发电机的定速风力发电机；2）带有发电机转子电阻的速度小范围可调风力发电机；3）双馈感应发电机(doubly fed induction generator，DFIG)变速风力发电机；4）采用同步发电机和全功率变流器的变速风力发电机。

对于不同类型风力发电机的风电场，其模型的实现方法也各不相同。与其他风力发电机类型相比，第 4 种风力发电机组通过全功率变流器实现了发电机和电网的完全解耦，在电网跌落期间，电机仍可以保持很好的控制特性[3]。因此，与其他机型风电场相比，由第 4 种风力发电机组组成的风电场模型的实现过程可以大为简化。

同步发电机可以采用绕组励磁同步发电机，也可以采用永磁同步发电机(permanent magnet synchronous generator，PMSG)。PMSG 结构简单，效率高；多极 PMSG 可以低速运行，从而取消齿轮箱，实现直驱式风力发电[4]。近年来，永磁直驱风力发电机组的累计装机容量份额一直保持在 13%~15%之间，伴随着海上风电场的大力发展，预计 PMSG 将得到更为广泛的应用[5]。

本文将讨论用于电磁暂态稳定研究的 PMSG 大规模风电场聚合模型。迄今为止，虽然已经有一些文献讨论了风电场模型，但主要集中在定速型风电场[1,6-8]和 DFIG 风电场[9]或针对稳态分析[10-11]，对 PMSG 风力发电机组的风电场电磁暂态模型的研究相对较少。J. Conroy 等讨论了由 12 台 5 MW 永磁同步发电机组构成的风电场聚合模型[12]，分析了撬棒保护和风电场布局对风电场聚合模型的影响，对 2 种简化的 PMSG 风电场聚合模型与详细模型进行了比较验证，然而该文献没有给出电网不对称故障下模型的电磁暂态响应特性。V. Akhmatov 建立了一种用于短时电压稳定性分析的通用聚合模型，给出了采用该聚合模型表示的 80 台 2 MW PMSG 风电场仿真结果[2]。A. Perdana 分析了 PMSG 风电场内部风速差异和撬棒保护电路对聚合模型精度的影响[13]。上述文献均没有考虑风电场内部的集电线路对聚合模型的影响。文献[14]建立了包含集电系统的风电场模型，然而仅限于潮流计算。

本文将在以下几个方面开展研究工作：1）建立 PMSG 风力发电机组简化仿真模型，使其适用于大规模风电场或风电场集群电磁暂态仿真，对电网

## 1 PMSG 风力发电机组模型及不同故障类型下风力发电机组的动态特性
PMSG 风力发电机组模型一般由以下几个部分构成：1）风速模型；2）空气动力模型；3）轴模型；4）发电机/变流器模型；5）变桨控制模型；6）控制与保护系统模型。模型中各部分的建模依照仿真目的不同可以简化或细化。

首先，本文研究用于电磁暂态分析的风电场模型，所仿真的时间范围一般为 10 s 以内，因此可以忽略风速模型，即认为在仿真过程中风速不变[12]、风能利用系数 $c_p$ 不变[13]。基于相同的原因，可以认为桨距角不变，因此可以忽略风电场空气动力模型和变桨控制模型。其次，考虑到 PMSG 风力发电机组中的全功率变流器的解耦作用，风力发电机组传动链的特性对电网的影响很小[15]，因此风力发电机组中的轴模型可以大大简化。最后，电网电压跌落期间，不平衡功率将引起变流器直流母线上升，因此需要对风力发电机组进行额外的控制。一种方法是降低发电机侧变流器和网侧变流器的有功功率输出，将多余的能量转化为传动链的动能，在这种方法中，输入到传动链的能量会引起发电机转速上升，因此在某些工况下最终会触发变桨控制，限制发电机转速在允许范围内[16]。也有方案采用附加的撬棒保护装置(Crowbar)吸收过剩的能量，防止直流母线发生过电压[17]。无论哪种方法，都可认为变流器直流母线电压保持不变，从而忽略母线电压控制环节。研究表明，这种简化可以提供足够的精确度[18]。为了保证模型在电磁暂态仿真过程中能正确体现动态特性，模型中变流器的电流控制环节必须保留。变流器有功和无功电流控制通过在 $d-q$ 坐标系下的带有前馈解耦的比例–积分(proportional integral，PI)调节器实现，变流器控制模型的简化控制框图见图 1。图中：$i_d^*$ 和 $i_q^*$ 分别为 $d-q$ 坐标系有功和无功电流参考值；$i_d$ 和 $i_q$ 分别为 $d-q$ 坐标系有功电流和无功电流分量；$e_d$ 和 $e_q$ 分别为 $d-q$ 坐标系
$i_d^*$, $i_q^*$, $e_d$, $e_q$, PI, Park, $R$, $\omega L$, $u_A$