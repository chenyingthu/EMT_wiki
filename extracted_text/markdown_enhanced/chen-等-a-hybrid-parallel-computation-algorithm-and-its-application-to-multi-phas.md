文章编号：0258-8013（2010）28-0039-07  中图分类号：TM 74  文献标志码：A  学科分类号：470.40

## 一种混合并行算法及其在多相交直流电力系统中的应用
陈来军1，陈颖1，梅生伟1，许寅1，付立军2，纪锋2
（1．电力系统及发电设备控制和仿真国家重点实验室（清华大学电机系），北京市海淀区 100084；
2．舰船综合电力技术国防科技重点实验室（海军工程大学），湖北省武汉市 430033）

## A Hybrid Parallel Computation Algorithm and Its Application to Multi-phase Hybrid AC/DC Power Systems
CHEN Laijun1, CHEN Ying1, MEI Shengwei1, XU Yin1, FU Lijun2, JI Feng2
（1. State Key Lab of Control and Simulation of Power Systems and Generation Equipments (Dept. of Electrical Engineering, Tsinghua University), Haidian District, Beijing 100084, China;
2. National Key Lab for Vessel Integrated Power System Technology (Naval University of Engineering), Wuhan 430033, Hubei Province, China）

**ABSTRACT:** The integrated power system is a typical hybrid AC/DC power system, which usually consists of multi-phase motors and power electronic devices. Because of the many electrical ports used, the multi-phase motors are hard to be decomposed optimally for parallel computing, which limit the speedup of the electromagnetic transients simulation of the integrated power system. In this work, a hybrid parallel simulation algorithm was proposed, which is based on both component and network decomposition. Through dividing multi-phase motor into several small motors, the proposed algorithm makes the overall system partitioned more flexibly and balanced. Furthermore, the parallel computation flow is optimized also to reduce the synchronization costs and make full use of the computational resources. Test results of a typical integrated power system were presented to validate the efficiency and accuracy of the proposed algorithm.

**KEY WORDS:** parallel computation; component level parallelization; hybrid parallel algorithm; integrated power system; electromagnetic transient

**摘要：** 综合电力系统是典型的多相交直流混合电力系统，多由多相电机和电力电子设备构成。由于多相电机计算量大、端口数多，采用传统并行算法难以提高综合电力系统电磁暂态仿真效率，为此提出一种混合并行算法，该算法由元件级并行和网络级并行2部分组成。其中前者通过将计算量大的多相电机元件分拆为多个互相耦合的电机，以大幅减少单个元件的计算量和显著提高系统分区的灵活性；后者则利用元件级并行实现系统切分方案的优化设计和计算流程中等待时间的高效利用，从而显著提高网络并行计算的总体效率。典型综合电力系统算例的仿真结果验证了所提出算法的正确性和有效性。

**关键词：** 并行计算；元件级并行；混合并行算法；综合电力系统；电磁暂态

**基金项目：** 国家自然科学青年基金资助项目（50807026）；高等学校博士学科点专项科研基金资助项目（2007003152）。
**Project Supported by** National Natural Science Foundation of China (50807026); Project Supported by Special Scientific and Research Funds for Doctoral Speciality of Institution of Higher Learning (2007003152).

## 0 引言
近年来，并行计算技术作为重要的加速手段，在电力系统仿真和分析中得到了广泛的应用[1-6]。并行计算的基本思想是将规模较大的原问题分解为几个规模较小的子问题，各子问题间通过协调侧交互信息完成各自计算，从而实现原问题的整体求解。由于子问题的规模一般较小，且可以同时展开计算，因此往往可以获得较高的计算效率。

系统切分方案是影响并行计算效率的一个重要因素。经典的系统切分方法是利用长传输线对系统中的各区域进行解耦[7-9]，该方法广泛应用于包含远距离输电线路的大规模电力系统的并行计算。由于在该方法中系统必须在长输电线处解开，使得系统的分区数量和各分区的计算规模均受到输电线数量和位置的限制，往往很难达到较高的并行效率。文献[10-11]将电力系统分层分区的特性与并行计算领域的图划分算法相结合，提出了一种优化的任务划分策略。文献[12-15]研究了基于多端口戴维南等效（multi-area Thevenin equivalent, MATE）的并行仿真算法，该方法通过对系统的各个部分进行戴维南等效，使用常规元件支路即可实现系统的分解，扩展了并行算法在电力系统中的应用范围。

综合电力系统（integrated power system, IPS）是近年来舰船电力系统研究的热点之一，多由多相电机和电力电子设备组成，并具有功率密度大、可靠性高等特点[16]。由于综合电力系统为交直流紧凑型系统，系统中没有长传输线，且分层分区的特性并不明显，这使得经典的系统切分方法不再适用，相应的优化切分策略也难以实施。而当采用多端口戴维南等效的方法对综合电力系统进行并行仿真时，由于多相电机仿真计算量大、端口多，使得并行仿真时的系统切分较为困难，并行仿真总体效率难以提高。

针对上述难题，本文提出一种混合并行算法。该算法包含元件级并行和网络级并行2个部分。其中，元件级并行算法可实现多相电机元件仿真的分解协调计算，既可降低单个元件的计算量，又可提高系统分区的灵活性。而考虑了元件级并行的网络级并行算法则可通过改变常规的系统切分方式，使得分区侧和协调侧计算规模同时降低成为可能。进一步，通过合理分配元件级并行中的计算任务，可有效减少网络级并行中计算资源的浪费和同步等待时间的消耗。本文采用典型的综合电力系统构建仿真算例，测试结果表明，本文所提出的混合并行算法可显著提高综合电力系统的并行仿真效率。

## 1 问题的提出
采用传统并行算法实现电磁暂态仿真，其仿真耗时主要由各子分区并发计算的最大耗时和协调计算耗时2部分组成。其中，分区侧的计算耗时主要...

下文以一个由十二相发电机、整流桥、逆变器和十五相电动机组成的典型综合电力系统为例，说明使用传统算法对其进行并行仿真时所遇到的困难。

针对图1所示的综合电力系统，若采用传统的MATE算法进行并行计算，则一般有表1所示的2种典型系统分区方案。表中数字1~9分别代表图1中对应标号的区域。

**图1 典型综合电力系统结构图**
*(Figure 1 Typical integrated power system topology)*

**表1 典型的系统分区方案**
| 分区方案 | 分区数目 | 分区组合 | 加速比 |
|---|---|---|---|
| 方案1 | 2 | (1 2 3 4 5; 6 7 8 9) | 2 |
| 方案2 | 9 | (1; 2; 3; 4; 5; 6; 7; 8; 9) | 2.5 |

方案1中，分区数目仅为2，虽然有效控制了协调侧的计算规模，但每个分区的计算量都很大，导致并行仿真整体效率不高，加速比一般很难超过2，因此，难以应用于对计算效率要求较高的场合。

方案2中，系统被分为9个子分区。其中，十二相发电机和十五相电动机分别被作为一个单独的分区来进行处理，单个分区的计算规模较方案1有所降低。但该方案仍然存在2个不足：1）由于该方案在多相电机的机端处进行系统切分，需切割较多联接支路，例如，从十二相发电机和十五相电动机端口处对系统进行切分时，会使协调侧计算规模分别增加12和30维，导致协调侧计算规模过大，