# 基于 FPGA 的变电站实时仿真培训系统
**张炳达，王岚禹**
（智能电网教育部重点实验室（天津大学），天津 300072）

**摘要：**为降低变电站仿真培训系统的建设成本，提高变电站实时数字仿真的质量，提出了一种基于 FPGA 的变电站实时仿真培训系统。采用最小度最大独立集法安排节点消去和电压计算的顺序，较好地兼顾了运算量和运算并行度。采用多输入多输出的指令流运算器实现细粒度的并行计算，提高了 FPGA 资源利用率。利用状态字和影响字间接完成仿真参数的修改，减少了仿真计算时间和节约了数据存储空间。实例表明，采用最小度最大独立集法、指令流运算器及仿真参数间接修改方法，一个具有 542 节点的仿真变电站能以 40 μs 仿真步长在一块 EP4CGX150 芯片上正常运行。
**关键词：**变电站；仿真培训；电磁暂态；实时仿真；现场可编程门阵列

基金项目：国家自然科学基金项目（51477114）；天津市科技计划项目（13TXSYJC40400）

# Real-time simulation training system for substation based on FPGA
**ZHANG Bingda, WANG Lanyu**
(Key Laboratory for Smart Grid of the Ministry of Education, Tianjin University, Tianjin 300072, China)

**Abstract:** Real-time simulation training system for substation based on field-programmable gate array (FPGA) is proposed in order to reduce the construction cost of substation simulation training system and enhance the quality of real-time digital simulation. A minimum degree maximum independent set method is adopted to arrange the sequence of nodes elimination and voltage computation, which has a good balance of computation burden and degree of parallelism. Fine granularity parallel computing is realized by adopting a multi-input and multi-output instruction stream arithmetic unit, therefore improving FPGA resource utilization. The simulation parameters are indirectly modified by the status word and effect word, thus reducing the simulation time and saving data memory space. Simulation example shows that a simulation substation with 542 nodes could be processed in an EP4CGX150 chip with 40 μs simulation step, according to the proposed minimum degree maximum independent set method, instruction stream arithmetic unit and indirect modification method for simulation parameters.
This work is supported by National Natural Science Foundation of China (No. 51477114) and Tianjin Science and Technology Program (No. 13TXSYJC40400).
**Key words:** substation; simulation training; electromagnetic transients; real-time simulation; field-programmable gate array (FPGA)

## 0 引言
对变电站运行人员进行技术培训是一项保证电力安全生产的重要措施。数字-物理混合型变电站仿真系统是一种高性价比的培训工具，已被电力培训部门广泛使用[1-3]。
为能在变电站仿真系统上进行各种各样的倒闸操作和事故处理训练，变电站实时数字仿真模型应涉及隔离开关、挂地线点、故障设置点等[4-5]。同时，为了与瞬时值电压电流为输入数据的继电保护、自动控制装置等真实设备连接，应采用电磁暂态仿真算法实现变电站实时数字仿真[6-7]。因此，规模不大的变电站实时数字仿真也需要较高级的计算机来承担。
基于微机群的变电站实时数字仿真具备硬件扩展性好，软件开发方便，且性价比高等特点，但受微机的通信速率的约束，难以胜任规模较大或步长较短的变电站实时数字仿真。变电站实时数字仿真也可采用加拿大 RTDS 公司的商业实时仿真装置[8-10]，它的仿真步长小至微秒级，甚至亚微秒级，但其成本高和扩展性差。
现场可编程门阵列 (Field-Programmable Gate Array, FPGA)具有高度并行性和深度流水线的特点，在电力系统仿真领域已成为一种有效的算法加速器件[11-15]。文献[16-17]将 RLC 无源元件、线路、开关、分布式电源等元件形成不同的 FPGA 单元模块，通过单元模块的组合完成电力系统仿真计算。这种方法的优势在于单元模块的功能明确，且可方便增减，但这些模块在大部分时间内处于闲置状态，造成 FPGA 硬件资源的浪费。
本文在使用最小度最大独立集法安排节点消去和电压计算顺序的基础上，设计一种多输入多输出的指令流运算器，给出相应的判断数据有效性和读写数据冲突的准则，使 FPGA 的硬件资源得到充分利用。为能从开关位置、故障设置、变压器磁饱和状态快速地确定各种仿真参数，提出一种同时节约计算时间和存储空间的仿真参数间接修改方法。在此基础上，实现了基于 FPGA 的变电站实时数字仿真。

## 1 变电站仿真培训系统组成
变电站仿真培训系统主要包括教员机、学员操作设备、实时数字仿真器等，如图 1 所示。

**图 1 变电站仿真培训系统**
Fig. 1 Simulation training system for substation

教员机不仅为教员提供仿真参数调整，故障设置等操作手段，而且能够记录并评判学员的操作过程。
为尽量贴近实际变电站的工作环境，学员操作设备采用真实的数字式保护盘、控制盘以及模拟一次系统现场的操作盘。
基于 FPGA 的实时数字仿真器是变电站仿真培训系统的核心，负责变电站一次系统的实时数字仿真计算。实时数字仿真器接收来自教员机的变电站一次系统仿真程序和故障设置以及数字式保护盘、控制盘、操作盘上的设备状态，并将一次系统的运行状态反送给数字式保护盘、控制盘、操作盘。

## 2 变电站一次系统仿真过程
为对变电站一次系统进行电磁暂态仿真，对变电站模型中的元件采用梯形法进行差分化处理，形成等效电导和历史电流源并联形式的伴随电路。对于具有磁饱和特性的变压器励磁电感，采用分段线性化的方式描述非线性特性。
用各个伴随电路替代原电路元件，并将节点多个注入电流用一个理想电流源表示，形成新的电路网络。这样，网络中的所有节点，均可表示为如图 2 的形式，其中 $I_i$ 是节点 $i$ 的理想电流源，$G_i$ 是节点 $i$ 的对地电导，$G_{ij}$ 是节点 $i$ 与节点 $j$ 之间的互电导。

**图 2 电路网络节点**
Fig. 2 Circuit network node

消去节点 $i$ 后，在与节点 $i$ 相邻的节点 $j$ 处需分别添加理想电流源 $I'_j$，对地电导 $G'_j$，以及与节点 $k$ 的互电导 $G'_{jk}$。
$$
\begin{cases}
I'_j = - I_i G_{ij} / \left( G_i + \sum_{p=1}^{n} G_{ip} \right) \\
G'_j = G_i G_{ij} / \left( G_i + \sum_{p=1}^{n} G_{ip} \right) \\
G'_{jk} = G_{ik} G_{ij} / \left( G_i + \sum_{p=1}^{n} G_{ip} \right) \quad k = 1, 2, \dots, n; \ k \neq j
\end{cases} \tag{1}
$$
整理化简节点消去后的电路网络，使所有节点再次变为如图 2 所示的形式。
若图 2 中的 $u_1, u_2, \dots, u_n$ 已知，则节点 $i$ 的电压为
$$
u_i = \left( I_i + \sum_{p=1}^{n} G_{ip} u_p \right) / \left( G_i + \sum_{p=1}^{n} G_{ip} \right) \tag{2}
$$
由以上分析可看出，节点消去和节点电压的计算量随相邻节点个数 $n$ (即节点度)的增加而增加。因此，为减少网络节点电压求解的运算量，应优先选择度最小的节点进行消去运算。
消去某一节点的运算过程，仅对与此节点相邻的节点有影响，而与其余节点无关。因此，有必要寻找出可同时进行节点消去的所有节点，即最大节点独立集，以提高运算并行度。
综合以上两点，采用最小度最大独立集法安排节点消去和电压计算顺序的基础上，设计一种多输入多输出的指令流运算器，给出相应的判断数据有效性和读写数据冲突的准则，使 FPGA 的硬件资源得到充分利用。为能从开关位置、故障设置、变压器磁饱和状态快速地确定各种仿真参数，提出一种同时节约计算时间和存储空间的仿真参数间接修改方法。在此基础上，实现了基于 FPGA 的变电站实时数字仿真。
对 MUX、读数据、写数据的控制，可根据变电站一次系统的仿真计算步骤编入过程控制模块中。这样，每当修改计算步骤时就需重新编写过程控