DOI：10.13334/j.0258-8013.pcsee.202511 文章编号：0258-8013 (2021) 24-8520-11 中图分类号：TM 46 文献标识码：A

## 混合型 MMC 全状态高效电磁暂态仿真方法研究
连攀杰，刘文焯，杨泽栋，汤涌，郁舒雁，李霞，许克
(电网安全与节能国家重点实验室(中国电力科学研究院有限公司)，北京市 海淀区 100192)

## Research on Hybrid MMC Full-state Efficient Electromagnetic Transient Simulation Method
LIAN Panjie, LIU Wenzhuo, YANG Zedong, TANG Yong, YU Shuyan, LI Xia, XU Ke
(State Key Laboratory of Power Grid Safety and Energy Conservation (China Electric Power Research Institute), Haidian District, Beijing 100192, China)

**ABSTRACT:** The hybrid modular multilevel converter (MMC), which composed of half-bridge sub-modules and full-bridge sub-modules, takes into account the DC fault ride-through capability and economy, with broad engineering application prospects. For the problems of complex equivalent, multiple internal nodes and low computational efficiency in the electromagnetic transient simulation model of the hybrid MMC, this paper analyzed the working state of the hybrid MMC in the unlocked and locked modes, and proposed a “efficient electromagnetic transient simulation method for hybrid MMC full-state”. According to the blocked characteristics of the half-bridge sub-modules and the full-bridge sub-modules in the hybrid MMC, the equivalent simulation method was optimized to improve the simulation efficiency in the blocked mode. According to the modulation characteristics of the hybrid MMC in unlocked mode, a flexible capacitor voltage sorting algorithm was proposed to improve the simulation efficiency for unlocked mode. Finally, with typical testing examples in Matlab and PSCAD, the accuracy and rapidity of the hybrid MMC high-efficiency electromagnetic transient simulation method proposed in this paper were verified.

**摘要：**由半桥子模块和全桥子模块组成的混合型模块化多电平换流器(modular multilevel converter，MMC)兼顾直流故障穿越能力和经济性，具有广阔的工程运用前景。针对混合型MMC 电磁暂态模型存在等效复杂、内部节点多、计算效率低的问题，文章分析混合型 MMC 解闭锁模式的工作状态，提出一种“混合型 MMC 全状态高效电磁暂态仿真方法”：根据混合型 MMC 中半桥子模块和全桥子模块的闭锁特性，提出一种混合型 MMC 的闭锁等效方法，提高混合型 MMC 闭锁模式的仿真效率；根据混合型 MMC 的调制特性，改进灵活堆排序的电容电压排序算法，提高混合型 MMC 解锁模式的仿真效率。最后，结合 Matlab 和 PSCAD 典型算例进行测试，验证所提高效混合型 MMC 全状态电磁暂态仿真方法的精确性和快速性。

**关键词：**混合型模块化多电平换流器；电磁暂态；全状态；闭锁等效；灵活堆排序算法
**KEY WORDS:** hybrid modular multilevel converter (MMC); electromagnetic transients; full-state; locked equivalent; flexible heap sorting algorithm

## 0 引言
模块化多电平换流器 (modular multilevel converter，MMC)以其谐波含量少、故障处理能力强、开关频率低、扩展性能好、便于模块化设计等优势，迅速得到了国内外高度关注[1-3]。目前 MMC 逐渐从低电压、小容量示范工程向高电压、大容量方向快速发展，在异步联网、风电场并网、城市中心供电、常规直流混联等场合展现出独特的技术优势和经济效益，成为柔性直流输电系统的优选主流拓扑[4]。

MMC 子模块存在半桥、全桥和双箝位等多种拓扑形式。双箝位及其它改进子模块拓扑仍处理论实验研究，国内尚无工程应用。半桥子模块成本低，损耗小，应用最广泛，但不具备直流故障穿越能力。全桥子模块具备直流故障穿越能力，但造价高，运行损耗大。由半桥子模块和全桥子模块组成的混合型 MMC 兼顾直流故障穿越能力和经济性，运用前景广阔[5-9]。

随着混合型 MMC 柔性直流输电系统的不断规划和投运，研究混合型 MMC 电磁暂态仿真方法，建立适用于大电网全电磁暂态仿真的混合型 MMC 电磁暂态模型，对柔性直流系统调试，大规模交直流电网故障分析、稳定性分析和控制保护策略设计与验证等工程前期设计意义重大。

针对混合型 MMC 详细模型电磁暂态仿真效率低下，不适用于大型电力系统全电磁暂态仿真的问题。文献[10]基于嵌套快速同时求解算法提出了戴维南等效模型，与平均值模型[11]、详细模型[12]和受控源模型[13]相比，戴维南等效模型兼顾高精度和高效率，在大规模电力系统仿真中具有得天独厚的优势。文献[14-15]优化等效方式，文献[16-17]优化排序算法，对经典戴维南模型进一步提速。文献[18]基于多频段动态相量法，建立了 MMC 多频段动态相量频段间解耦模型。文献[19]基于旋转坐标系变换的大步长建模仿真理论，建立了 MMC 大步长仿真模型。文献[20]将半桥 MMC 仿真方法运用于全桥 MMC 和混合型 MMC 的电磁暂态仿真，建立混合型 MMC 戴维南模型，实现了混合型 MMC 解锁模式下高精度仿真。

但在电磁暂态仿真中，诸多情况都会涉及闭锁模式。针对混合型 MMC 闭锁模式下工作状态灵活复杂，且面临插值问题。如何正确模拟混合型 MMC 闭锁模式，从而实现高精度、高效率仿真混合型 MMC 解闭锁模式，是混合型 MMC 全状态电磁暂态仿真的难点。目前许多文献[21-23]借助 PSCAD/EMTDC 自带的二极管模型，通过控制开关的闭合模拟 MMC 闭锁模式。但此方法中单桥臂混合型 MMC 需用 6 个二极管等效，增加了内部节点个数。部分混合型 MMC 等效模型在解锁模式下二极管仍根据动作准则进行不必要的插值计算[21]，在闭锁模式下仍在进行电容电压排序[22]，均影响了混合型 MMC 的计算效率。

针对混合型 MMC 全状态电磁暂态仿真模型存在等效复杂、内部节点数量多、计算效率低、依赖 PSCAD 等问题，文章分析混合型 MMC 解闭锁模式存在的多种工作状态，提出了一种混合型 MMC 全状态高效电磁暂态仿真方法。针对混合型 MMC 中半桥子模块和全桥子模块的闭锁特性，提出一种混合型 MMC 的闭锁等效方法，实现混合型 MMC 闭锁模式下的高精度、高效率仿真。根据混合型 MMC 解锁模式的调制原理，改进灵活堆排序的电容电压排序算法，提高混合型 MMC 解锁模式的仿真效率。最后结合 Matlab 和 PSCAD 典型算例进行测试，验证本文所提混合型 MMC 全状态高效电磁暂态仿真方法的精确性和快速性。

## 1 混合型 MMC 工作状态分析

### 1.1 混合型 MMC 拓扑结构
三相混合型 MMC 的拓扑结构如图 1 所示，各桥臂由 N 个子模块组成，其中半桥子模块的数量为 Nh，全桥子模块的数量为 Nf。一定数量的全桥子模块不仅使 MMC 具备了直流故障箝位能力，且能够输出负电平，提高了 MMC 的运行灵活性。

图 1 三相混合型 MMC 的拓扑结构
Fig. 1 Topological structure of three-phase hybrid MMC

混合型 MMC 存在解锁和闭锁两种不同的工作模式，每种模式均包括多种工作状态。

### 1.2 闭锁工作状态分析
闭锁模式下，混合型 MMC 子模块中的 IGBT 全部关断，由二极管确定子模块工作状态。二极管具有一定阈值的正向电压则导通，具有反向电压则关断。根据二极管通断状态的不同，闭锁模式下子模块具有多种工作状态。半桥子模块对应的工作状态如图 2(a)所示，全桥子模块对应的工作状态如图 2(b)所示。

图 2 中红色表示二极管处于关断状态，绿色表示二极管处于导通状态。半桥子模块具有正向充电、反向旁路和截止 3 种状态，全桥子模块具有正向充电、反向充电和截止 3 种状态。混合型 MMC 子模块串联组成各桥臂，闭锁模式下同桥臂的子模块电流相同，因此同桥臂同类型子模块具有相同的工作状态[21-23]。

图 2 子模块闭锁模式下工作状态
Fig. 2 Working status in sub-module blocking mode

### 1.3 解锁工作状态分析
解锁模式下，混合型 MMC 的调制环节生成 IGBT 控制信号，部分 IGBT 导通。通过控制子模块的投退，维持混合型 MMC 子模块电容电压均衡，并使交流侧输出的电压波形接近正弦波。

图 3 混合型 MMC 全状态等效模型
Fig. 3 Hybrid MMC full state equivalent model

路。式(1)、(2)为等效公式。

$$u_{\text{arm,eq}}(t) = u_{\text{all\_sm,eq}}^{\text{HB}}(t) + u_{\text{all\_sm,eq}}^{\text{FB}}(t) + u_L(t) \tag{1}$$

$$R_{\text{arm,eq}}(t) = R_{\text{all\_sm,eq}}^{\text{HB}}(t) + R_{\text{all\_sm,eq}}^{\text{FB}}(t) \tag{2}$$