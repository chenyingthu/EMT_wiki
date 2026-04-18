## 多类型子模块 MMC 电磁暂态通用建模和实现方法
许建中$^{1}$，徐义良$^{2}$，赵禹辰$^{1}$，赵成勇$^{1}$
（1．新能源电力系统国家重点实验室(华北电力大学)，北京市 昌平区 102206；2．直流输电技术国家重点实验室(南方电网科学研究院有限责任公司)，广东省 广州市 510080)

**Generalized Electromagnetic Transient Equivalent Modeling and Implementation of MMC With Arbitrary Multi-type Submodule Structures**
XU Jianzhong$^{1}$, XU Yiliang$^{2}$, ZHAO Yuchen$^{1}$, ZHAO Chengyong$^{1}$
(1. State Key Laboratory of Alternate Electrical Power System With Renewable Energy Sources (North China Electric Power University), Changping District, Beijing 102206, China; 2. State Key Laboratory of HVDC (Electric Power Research Institute, China Southern Power Grid), Guangzhou 510080, Guangdong Province, China)

**ABSTRACT:** The key issue of electromagnetic transient (EMT) modelling of modular multilevel converters (MMC) is calculation of equivalent circuit of entire MMC arm containing a large number of cascaded sub-modules (SM) with identical structure. During this process, all internal information should be preserved. This paper proposes a general EMT modelling approach for arbitrary multi-port MMC topologies, also suitable for traditional single-port MMC and emerging two-port MMC. A submodule topology identification method is proposed to minimize the efforts of the model users when they have specific MMC topologies at hand. In addition, the model codes can be inherited to a large extent. Finally, the approaches are validated in PSCAD/EMTDC with results of very good applicability of the general algorithm and unified implementation method.

**KEY WORDS:** modular multilevel converter (MMC); electromagnetic transient (EMT); equivalent model; multi-port sub-module; submodule topology identification

**DOI:** 10.13335/j.1000-3673.pst.2018.2121

**摘要：** 模块化多电平换流器(modular multilevel converter，MMC)电磁暂态高效建模的难点，在于对桥臂中大量结构相同的级联子模块(sub-module，SM)进行等效的同时保证消去的节点信息都可以被精确反解。提出一种针对多类型 MMC 的电磁暂态通用建模和实现方法，它对传统的单端口 MMC 和新近出现的双端口 MMC 都适用。同时提出一种 MMC 拓扑自动识别方法，可以大幅降低模型用户在对特定拓扑建模时候的工作量，同时绝大部分模型代码都可以继承。最后，在 PSCAD/EMTDC 中分别以单端口和双端口 MMC 为例，对所介绍的等效建模算法进行了验证，结果表明所提出的算法具有很强的通用性。

**关键词：** 模块化多电平换流器；电磁暂态；等效模型；多类型子模块；子模块拓扑识别

**基金项目：** 国家自然科学基金资助项目(51607065)。
**Project Supported by National Natural Science Foundation of China (51607065).**

## 0 引言
由半桥、全桥等单端口子模块构成的模块化多电平换流器(modular multilevel converter，MMC)，已成为国内外各大柔性直流输电工程的首选换流器拓扑[1-5]。近来，新型双端口子模块 MMC 拓扑不断涌现[9-11]，这些拓扑通常具备直流故障穿越能力和电容电压自平衡能力等优良特性。随着柔性直流电网对快速清除直流故障的需求不断增强，这些新型拓扑具有良好的应用前景。

当前柔性直流输电工程正朝着高电平、大容量、多端的方向快速发展。当电平数较高时，无论是半桥、全桥等单端口子模块还是新型双端口子模块构成的 MMC 在进行电磁暂态仿真时，都将面临仿真速度难以满足研究需求的问题。针对 MMC 模型计算效率问题，国内外学者提出了大量电磁暂态等效模型[12-20]，这些模型针对单端口子模块 MMC 拓扑提出，算法适用前提是同一个桥臂内的子模块必须流过相同的桥臂电流。文献[21]提出了一种对任意单端口 MMC 拓扑通用的等效建模方法，在求解子模块戴维南等效电路时无需获得符号解析解，可以极大提高新拓扑的建模效率。然而，文献[12-21]都要求桥臂电流流过全部子模块的正负端子，以便通过对子模块戴维南电路求和以获得桥臂的等效电路。

图 1 为本文将涉及到的双端口子模块构成的 MMC 拓扑，相比于传统的单端口子模块拓扑，双端口子模块兼具隔离直流故障和自均压等功能。随着新型子模块拓扑外部端子数目的增加，相邻子模块间电流流通路径多样化，两两端子之间不一定严格的满足成为端口的条件，传统的戴维南等效方法将不再适用于该种类型的子模块的建模。

> 图 1 双端口子模块 MMC 示意图
> Fig. 1 Schematic diagram of the two-port MMC

为解决这一问题，文献[22]针对双端口 MMC 提出了一种通用等效建模方法，该方法可以在实现对外部等效的同时，完整保留消去节点的全部信息。然而，文献[22]中方法针对的是对称双端口子模块结构，不适用于子模块外部端口数量大于二的多端口 MMC 或子模块两侧结构不对称的多端口 MMC 情况。同时，文献[21]和[22]中的方法都无法实现针对模型用户特定 MMC 拓扑的快速识别和通用建模，对用户的编程能力要求较高。

本文将在文献[21-22]工作的基础上，提出一种多类型 MMC 拓扑等效模型的通用实现方法，用户只需输入表征新型子模块结构的拓扑识别矩阵，就可以实现新拓扑的电磁暂态快速建模，最终实现建模算法和编程实现的双通用。同时，本文所提建模方法既可用于离线仿真，也可用于实时仿真。

## 1 多类型子模块 MMC 拓扑的自动识别方法
本节将介绍本文提出的不同类型子模块拓扑的快速自动识别方法。为了不失一般性，假定任意新型子模块拓扑中最多包含 2 个电容(本文提出方法所涉及公式可以根据实际电容数量进行修改)，将电容进行积分离散化为诺顿等效形式，并使用阻值可变的电阻来代替开关器件，可得任意子模块的伴随电路如图 2 所示。图 2 共含 $n$ 个节点，其中第 $1 \sim 2m$ 个节点为子模块的外部连接节点，其余均为子模块内部节点，第 $i \sim n$ 号节点为电容节点。

> 图 2 任意拓扑子模块对应的伴随电路
> Fig. 2 Companion circuit of the arbitrary sub-module topology

在 PSCAD/EMTDC 等电磁暂态仿真软件中对任意拓扑子模块构成的 MMC 进行建模编程时，传统方法需要由图 2 子模块的伴随电路预先计算出子模块节点电压方程中各矩阵对应元素的解析表达式，然后编入程序中。通常一旦子模块拓扑发生改变，所编程序将不再适用，需要根据新的子模块拓扑重新求解获得等效电路的符号解析解，然后将其编程到仿真软件当中，这大大限制了所编程序的通用性。同时，当子模块拓扑较复杂时，由于涉及到矩阵求逆过程，符号解析解将非常冗长，不利于程序的实现。另外，虽然 MMC 子模块拓扑确定后用户可以容易地自行列写出节点电压方程，但是却增加了用户地编程工作量，而且节点电压方程中的电导元素是每个步长都要改变的，这样将使得用户在编程时要将控制部分给触发信号的部分输出并且整合到程序中去，这无疑大大增加了用户的编程工作量。因此，本文将探索一种通用实现方法。

### 1.1 适用任意端口 MMC 子模块拓扑的识别方法
针对上述问题，本文提出一种任意拓扑 MMC 等效模型通用实现方法，用户只需要在程序界面输入相应子模块对应的关联矩阵、支路导纳矩阵和支路电流源列向量，可以由仿真软件通过矩阵运算即可得到子模块对应的节点电压方程，无需预先求出节点电压方程中各矩阵对应元素的解析表达式，可以实现所编程序代码对任意拓扑子模块的通用。

以图 2 为例，假设任意拓扑子模块伴随电路中共含 $n$ 个节点、$b$ 条支路(其中电容虽然被离散化为一个电导和电流源并联，但依然视为一条支路)。首先对子模块伴随电路中各节点和支路分别从 $1 \sim n$、

### 1.2 单端口 MMC 子模块拓扑识别