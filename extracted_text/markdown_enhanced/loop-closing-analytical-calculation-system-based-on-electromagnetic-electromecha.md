## 基于机电暂态-电磁暂态混合仿真的电网合环分析计算系统
**Loop closing analytical calculation system based on electromagnetic-electromechanical transient simulation for power network**

朱雨晨 1，赵冬梅 1，刘世良 2，李亚楼 3，朱旭凯 3，张 星 3，宋 军 4
(1.华北电力大学，北京 102206；2.青海电力公司住处通信公司，青海 西宁 810008；3.中国电力科学研究院，北京 100192； 4. 新疆疆南电力有限责任公司，新疆 喀什 844000）

ZHU Yu-chen1, ZHAO Dong-mei1, LIU Shi-liang2, LI Ya-lou3, ZHU Xu-kai3, ZHANG Xing3, SONG Jun4
(1. North China Electric Power University, Beijing 102206, China; 2. Qinghai Information and Communication Company, Xining 810008, China; 3. China Electric Power Research Institute, Beijing 100192, China; 4. Xinjiang Jiangnan Electricity Co., Ltd, Kashi 844000, China)

**摘要：** 为了提高电网的安全运行，开发了基于机电暂态-电磁暂态混合仿真原理的电网合环分析计算系统。利用机电-电磁混合仿真原理，提出了基于最大级数搜索算法的电磁网络自动划分方法，实现了机电暂态模型自动转换为电磁暂态模型的功能，并完成了地理图与厂站图相关联的功能，方便用户操作的同时提高了合环计算结果的准确性。利用开关统计功能，可以得到系统不同时刻的合环情况。通过对新疆喀什地区电网的合环仿真计算，其结果表明该系统能够提高合环操作的准确性，为合环操作提供了重要依据。
**关键词：** 电网合环；机电暂态仿真；电磁暂态仿真；机电暂态-电磁暂态混合仿真；电磁网络自动划分；电磁模型自动转换；单机并行算法

**Abstract:** To improve safe operation of power network, a loop closing analytical calculation system based on electromagnetic-electromechanical transient hybrid simulation theory is developed. An automatic electromagnetic network partition solution based on the maximal stair search algorithm is put forward. The system also implements the function of automatic transformation from the electromechanical transient models to electromagnetic models and links the geographic maps and station maps, which not only makes loop closing operation easy but also enhances veracity. Simulation and calculation results show that the system can increase the accuracy of loop closing, providing evidence for loop closing operation.
This work is supported by National High-tech R&D Program of China (863 Program) (No. 2011AA05A105).
**Key words:** power network loop closing; electromechanical transient simulation; electromagnetic transient simulation; electromagnetic-electromechanical transient hybrid simulation; automatic electromagnetic network partition solution; automatic transformation of electromechanical models; single machine parallel algorithm

## 0 引言
提高供电可靠性一直是电力系统致力的首要目标。带电合环操作可以减少停电时间，是提高系统供电可靠性的一种重要方法[1-2]。电网正常运行时，不同母线所带的负荷区域之间的联络开关都是打开的。线路故障或者检修时，通过先停电隔离，再转供负荷的方式，可以在一定程度上减少停电时间，提高供电可靠性[3-4]。当前，转供负荷的实现方法是先将待转供负荷的线路从现有电源断开，再将它投运到另一个电源供电，操作过程中会有短时停电，这样既损失了电量，又造成负荷用户减产，影响正常的生产秩序，甚至可能导致重大的经济损失。此外，在执行合环操作时，由于合环点两侧电压或系统短路阻抗相差较大，使合环稳态电流和冲击电流过大，导致系统过电压、过电流，引起保护误动甚至设备损坏。瞬时合环电流过大还可能造成联络开关和线路过载，甚至发生爆炸，威胁操作人员的人身安全[5]。

目前，对合环操作问题的处理方式可纳为以下四种：一、工作人员根据运行经验判断合环操作可行性[6]，但由于电力系统本身的复杂性，该方法具有较大的局限性；二、调度员根据潮流计算得到合环后稳态电流大小并以此来判断合环操作的可行性[7-8]，但此方法不适用于暂态冲击电流过大导致合环失败的情形；三、利用离线分析工具，对合环操作进行模拟来判断合环条件，常见的软件有 PSASP、BPA、PSCAD[9-11]等；四、根据电网实际情况开发专门的合环计算系统[12-14]，这些系统大都采用等值的方法，工作量随着电网规模的增大呈指数递增。
鉴于以上原因，开发了基于机电-电磁暂态混合仿真的电网合环分析计算系统，用于判断电网合环操作的可行性。

## 1 机电暂态-电磁暂态混合仿真原理
### 1.1 机电暂态仿真与电磁暂态仿真
机电暂态仿真主要研究电力系统受到大扰动后的暂态稳定性能[15]；而电磁暂态仿真主要研究系统元件中电场和磁场以及相应的电压和电流的变化情况[16]。电力系统电磁暂态仿真和机电暂态仿真的仿真差异见表 1[17-19]。

**表 1 机电暂态仿真与电磁暂态仿真对比**
**Table 1 Comparison between electromechanical and electromagnetic transient simulation**

| 项目 | 机电仿真 | 电磁仿真 |
|---|---|---|
| 仿真步长 | 微秒级 | 毫秒级 |
| 模型描述 | 代数、微分、偏微分方程 | 线性相量方程 |
| 仿真条件 | ABC 三相瞬时值 | 基波相量 |
| 分析问题 | 过电压、高次谐波 | 工频特性、低频振荡特性 |

### 1.2 机电-电磁混合仿真的必要性
机电暂态仿真往往因为仿真步长较大，无法获得电气量更精细的变化结果，不能分析系统过电压、过电流等情况。当需要详细研究次同步谐振等电力系统复杂问题时，需采用电磁暂态仿真。但电磁暂态仿真模型复杂、计算量大，与之相关的网络常需等值简化，从而降低了计算分析的准确性。
为了解决上述问题，将电磁暂态计算与机电暂态计算进行实时接口，在一次仿真过程中同时实现对大规模电力系统的机电暂态仿真和局部网络的电磁暂态仿真，不但可以了解大系统暂态稳定过程的动态特性，而且有助于了解大系统中某一区域电网的详细暂态变化过程。

### 1.3 机电-电磁混合仿真接口等值电路
混合仿真时，整个网络分为机电暂态网络和电磁暂态网络。在对电磁暂态网络进行仿真时，接入机电暂态网络的戴维南等值电路，如图 1（a）所示；在对机电暂态网络进行仿真时，接入电磁暂态网络的诺顿等值电路，如图 1（b）所示。由于机电暂态网络为三序相量网络，而电磁暂态网络为三相瞬时值网络，因此，还需要进行序-相变换以及瞬时值-相量变换。该等值电路对于有源网络和无源网络都适用。

图 1 机电-电磁网络接口等值电路
Fig. 1 Equivalent circuit of interface between electromagnetic transient simulation and electromechanical transient simulation

### 1.4 机电-电磁混合仿真接口时序（图 2）
由于机电暂态网络计算步长大于电磁暂态网络计算的步长，因此两个网络之间的数据交换是以机电暂态步长为单位进行的。以机电暂态网络计算步长为 $DTP=0.01\ \text{s}$、电磁暂态网络计算步长为 $DTE=0.001\ \text{s}$ 为例说明：机电暂态网络和电磁暂态网络在每个机电暂态网络积分时段，即 $t = 0.01\ \text{s}$，$0.02\ \text{s}\dots$ 时刻交换一次数据，其中初始化时机电暂态网络向电磁暂态网络发送正、负、零序等值阻抗阵及等值电势的初始值；在每一次数据交换时刻机电暂态网络向电磁暂态网络发送边界点的正、负、零序等值电势，电磁暂态网络向机电暂态网络发送边界点的正、负、零序电压和电流。在有故障或操作导致机电暂态网络结构发生变化时，机电暂态网络还需向电磁暂态网络发送机电暂态网络的正、负、零序等值阻抗阵。交换的数据均为两网在 $0.009\ \text{s}$、$0.019\ \text{s}\dots t-DTE$ 时刻的值。

图 2 机电暂态网络和电磁暂态网络数据接口时序
Fig. 2 Interface timing of between electromagnetic transient network and electromechanical transient network

上述为机电暂态网络和电磁暂态网络并行计算数据交换时序，在对计算时间要求不严的情况下，也可采用串行计算数据交换时序，这里不作介绍。

## 2 电网合环分析计算系统的设计与实现
考虑到机电-电磁混合仿真的优点以及现有解决方案的不足，比如电磁暂态仿真（如 PSCAD）难以反映潮流转移情况，而机电暂态仿真（如 PSASP）无法分析合环可能出现的过电压、过电流情况，本文介绍了基于机电-电磁暂态混合仿真的合环分析计算系统。

### 2.1 系统架构
输配电网合环仿真计算系统包括合环潮流计算与合环暂态计算两部分，合环潮流计算可得到合环稳态电流，合环暂态计算可得到合环冲击电流。系统架构如图 3 所示。

图 4 地理图
Fig. 4 Geographic map

PQ 分解转牛顿法）供选择。与常规潮流计算相比，合环潮流计算包含了合环前与合环后两次潮流计算。通过潮流计算用户可以直观地发现合环操作可能带来的潮流转移及其他潮流不合理问题。

图 5 厂站单线图
Fig. 5 Station single line map

### 2.3.2 机电暂态仿真模块
合环机电暂态仿真模块主要用来计算合环冲击