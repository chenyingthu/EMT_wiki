DOI：10.13334/j.0258-8013.pcsee.172160  文章编号：0258-8013 (2018) 20-6079-12  中图分类号：TM 721

## 双端口子模块 MMC 电磁暂态通用等效建模方法
徐义良，赵成勇，赵禹辰，石璐，许建中*
(新能源电力系统国家重点实验室(华北电力大学)，北京市 昌平区 102206)

### Generalized Electromagnetic Transient (EMT) Equivalent Modeling of MMCs With Arbitrary Two-port Sub-module Structures
XU Yiliang, ZHAO Chengyong, ZHAO Yuchen, SHI Lu, XU Jianzhong*
(State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources (North China Electric Power University), Changping District, Beijing 102206, China)

**ABSTRACT:** This paper proposed an accurate and high-speed electromagnetic transient (EMT) equivalent modeling method for arbitrary novel two-port MMC by using paralleled full bridge sub-module (SMs) modular multilevel converter (MMC) topology. Unlike the previous equivalent method for single-port MMCs, the two-port MMC did not enjoy the feature that the same arm current flows through all the SMs. With respect to this issue, the recursive solution algorithm for two-port MMC was proposed. All the internal nodes both inside the SMs and between SMs were eliminated recursively, then the whole bridge arm was represented by 4 nodes in the main EMT solver. During this process, all the internal information was preserved though increased the bookkeeping effort. After solving the reduced order admittance matrix, the previously eliminated node information such as the capacitor voltages and interfacing node currents were updated. Therefore, the proposed algorithm is very time efficient yet satisfactorily accurate to reproduce identical external as well as internal dynamics. The EMT simulations on PSCAD/EMTDC validated the accuracy and speed up factor of the proposed model.

**KEY WORDS:** modular multilevel converter (MMC); electromagnetic transient (EMT); two-port sub-module (SM); equivalent model

**摘要：** 针对一种新型并联全桥子模块构成的模块化多电平换流器(paralleled full bridge sub-module MMC，PFB-MMC)拓扑，提出一种适用于任意新型双端口 MMC 的电磁暂态通用等效建模方法。传统单端口子模块 MMC 的等效算法要求全部子模块流过相同的桥臂电流，这对双端口 MMC 不再适用。针对这一问题，适用于双端口 MMC 的迭代求解算法被提出。MMC 桥臂中全部子模块的内部节点和模块间的互联节点均被迭代消去，整个桥臂在电磁暂态解算器中被等效成仅含 4 个外部节点，尽管在这一过程中求解的步骤有所增加，但依然能够完整保留各桥臂全部的内部信息。对降阶导纳矩阵进行求解后，即可完成之前被等效消去的节点信息例如电容电压、连接节点电流的更新。因此，该文提出的建模方法，能够在精确仿真系统内、外部动态特性的同时，大幅提高其电磁暂态仿真速度。在 PSCAD/EMTDC 环境中验证所提出模型的精度和加速比。

**关键词：** 模块化多电平换流器；电磁暂态；双端口子模块；等效模型

基金项目：国家自然科学基金项目(51607065)。
Project Supported by National Natural Science Foundation of China (51607065).

## 0 引言
模块化多电平换流器(modular multilevel converter，MMC)凭借其开关损耗低等优点，已在国内外各大柔性直流输电工程中得到了广泛应用[1-3]。但是，目前应用范围最广的半桥型子模块 MMC 在发生直流侧短路故障闭锁后，依然可以通过反并联二极管向直流短路点馈入电流，因而无法清除直流故障[4]。此外，当电平数较高时，半桥型子模块 MMC 的电容电压排序即使采用质因子分解法、希尔排序法等低排序复杂度的方法[5-9]，依然存在较大数量的排序运算。

针对这些问题，目前国内外不断有新型双端口子模块拓扑被提出[10-12]，相比于全桥及钳位双子模块等单端口子模块拓扑，这些新型双端口子模块拓扑在具备直流故障钳位能力的同时还具备自均压的能力，被视为 MMC 子模块未来的候选拓扑之一，具有一定的发展前景。文献[10]在并联 IGBT 开关组型全桥子模块(full-bridge sub-module，FBSM)的基础上，提出了开关分列运行的并联全桥子模块(paralleled full bridge sub-module，P-FBSM)拓扑，经对称翻转得到，其拓扑结构如图 1 所示。

**图 1 并联全桥子模块拓扑结构**
**Fig. 1 Topology of the P-FBSM**

由图 1 可知，与半桥、全桥等单端口(两端子)子模块不同，单个 P-FBSM 拥有 4 个端子：P1、P2、N1、N2，是一种双端口子模块，它由 8 个 IGBT 开关器件及其反并联二极管和 1 个直流存储电容构成。通过 8 个开关器件的触发信号 T1—T8 工作状态的切换，单个 P-FBSM 一共有 9 种运行状态，具体的调制和电压平衡控制方法如文献[21]所示。文献[21]基于最近电平逼近调制，设计了一种 P-FBSM 动态分配均压控制策略，可同时实现子模块电容电压的自均衡和直流故障电流快速清除。

并联全桥子模块 MMC(paralleled full bridge sub-module MMC，PFB-MMC)拓扑如图 2 所示，它依然为三相、六桥臂对称结构。

目前国内外已有的关于 MMC 的电磁暂态等效模型全部针对单端口子模块拓扑，例如半桥、全桥、双钳位型子模块等[13-20]。这些等效模型适用的前提是全部子模块必须流过相同的桥臂电流，单端口子模块必然满足这一条件，而双端口子模块因为包含 4 个端子，相邻子模块间电流流通路径复杂多变，无法满足这一条件，因而现有的关于 MMC 的电磁暂态等效模型均不适用。文献[13-16]提出了一种戴维南等效模型，通过分别求解单个子模块的戴维南等效电路，进而直接求和得到单个桥臂的戴维南等效电路。新型双端口子模块有 4 个端子，无法求解其戴维南等效电路，且无法像单端口子模块那样将全部子模块等效电路直接求和得到桥臂等效电路。文献[16]提出了一种基于受控源的 MMC 通用建模方法，使用 PSCAD 软件中已有的器件搭建模型，具有一定的通用性。但是其使用的器件数目多于详细模型，且扩展的灵活性受限。文献[18]提出了一