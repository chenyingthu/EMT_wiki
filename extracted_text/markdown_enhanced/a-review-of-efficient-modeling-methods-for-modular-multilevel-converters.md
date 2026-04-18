## 模块化多电平换流器高效建模方法研究综述
**许建中1，李承昱1，熊岩1，姬煜轲1，赵成勇1，安婷2**
（1．新能源电力系统国家重点实验室（华北电力大学），北京市昌平区 102206；2．国网智能电网研究院，北京市昌平区 102211）

## A Review of Efficient Modeling Methods for Modular Multilevel Converters
**XU Jianzhong1, LI Chengyu1, XIONG Yan1, JI Yuke1, ZHAO Chengyong1, AN Ting2**
(1. State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources (North China Electric Power University), Changping District, Beijing 102206, China; 2. State Grid Smart Grid Research Institute, Changping District, Beijing 102211, China)

**ABSTRACT:** The modular multilevel converter (MMC) based HVDC system has shown its significant project prospects, hence the efficient modeling method of MMC is the basis for a series of theoretical and engineering studies. This paper respectively focused on different time scales and application scenarios to summarize the state of the art literatures of this field methodically, and then to explore the cutting-edge research to show the core issues and concerns in the MMC modeling area. The recent achievements on electromagnetic transient (EMT) accurate MMC models, i.e. the controlled sources based universal accelerated MMC model and the Thévenin equivalent integral MMC model based on the backward Euler method and the trapezoidal rule were rigorously and horizontally compared and validated. Then the applicability of the proposed simplified averaged-value MMC model under severe AC and DC transients were validated and the usage scenarios were pointed out. Finally, this paper introduces the main features of the electromechanical transient MMC model and the real time simulation models, then points out that both models have very good research and application prospects.

**KEY WORDS:** modular multilevel converter; electromagnetic transient; controlled source based model; Thévenin equivalent model; averaged-value model

**摘要：** 模块化多电平换流器（modular multilevel converter, MMC）已经展现出极其重要的工程应用前景，MMC的高效建模方法是开展一系列理论性和工程性问题研究的基础。文中分别针对不同时间尺度和不同的应用场景，对国内外已有的涉及到MMC建模的主要文献进行条分缕析式地整理归纳，进而探索该领域的研究前沿和关注的核心问题。对所提出的3种微秒级电磁暂态精确模型，也即基于受控源的MMC通用提速模型和基于后退欧拉法和梯形法的MMC戴维南等效整体模型进行了严格的横向对比和仿真验证；同时，针对所提出的电磁暂态平均简化模型，验证了其在仿真严重交直流暂态过程中的适用性，分析其适用场景和使用方法。最后，文中介绍了MMC机电暂态模型和实时仿真模型的主体思想，并指出二者具有很好的研究和应用前景。

**关键词：** 模块化多电平换流器；电磁暂态；受控源模型；戴维南等效模型；平均值模型

**基金项目：** 国家自然科学基金重点资助项目（51177042）；国家863高技术基金项目（2013AA050105）；新能源电力系统国家重点实验室开放课题资助（LAPS15017）；中央高校基本科研业务费专项资金（2015QN04）。
Project Supported by National Natural Science Foundation of China (51177042); The National High Technology Research and Development of China (863 Program) (2013AA050105); State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources (LAPS15017); Fundamental Research Funds for the Central Universities (2015QN04).

## 0 引言
模块化多电平换流器（modular multilevel converter, MMC）已成为柔性直流输电系统的首选换流器拓扑[1-7]。我国已建成的上海南汇柔性直流工程[1]、南澳三端柔性直流工程[2]、舟山五端柔性直流输电工程[3]以及正在建设中的厦门柔性直流工程[4]都采用MMC结构。国际上SIEMENS已建成的美国跨湾工程（Trans Bay Cable Project, TBC）[5]和法国—西班牙联网工程（INELFE工程）[6]都采用MMC结构。同时，ABB公司提出了一种级联两电平结构（cascaded two level, CTL），其本质仍为MMC，并且ABB后续建设的数项柔性直流工程都采用CTL结构[7]。因此，MMC已由最初的低压、小容量示范工程向高电压、大容量方向快速发展，展现出很好的发展前景。

然而，高电压、大容量、超大规模MMC高效建模受限于建模方法、数学理论、等效实验方法和计算机硬件等众多限制[5-9]，严重制约着相关领域的快速发展[10-12]。因此，建立MMC的数学和仿真模型能反映换流器的一般运行规律，对研究柔性直流输电系统运行特性、主电路参数的选取以及控制保护系统的设计具有重要的指导作用[13-14]，开展不同时间尺度的MMC电磁暂态建模方法的研究，在保证仿真精度的前提下研究极大地提高MMC仿真效率的理论和方法，提出适用于不同应用场景的MMC高效仿真模型，具有重要的理论和工程意义。

MMC系统的仿真分析，较之现场试验具有良好的可控性、无破坏性和经济性，对验证控制系统的有效性及进行工程方案的比较等方面发挥着重要作用，为工程调试奠定了基础。目前对MMC的仿真研究按仿真计算同实际过程的时间比例主要分为离线仿真和实时仿真，按仿真基于瞬时值或有效值分为电磁暂态仿真和机电暂态仿真，按不同的仿真步长可分为纳秒级仿真、微秒级仿真、毫秒级仿真。

MMC具有很好的工程应用前景，针对不同的仿真类型与仿真需求，MMC的建模方法各有不同。因此，对MMC建模方法的研究现状进行总结和剖析是很有必要的。本文在分析MMC拓扑结构及其仿真建模特点的基础上，针对国内外MMC建模方法的研究现状和最新研究成果，进行了详细的分类阐述。

## 1 MMC的拓扑结构与仿真特点
### 1.1 MMC及其子模块拓扑
模型共有6个桥臂，每个桥臂包含$N$个子模块。MMC拓扑创始人德国慕尼黑联邦国防军大学的Marquardt教授共提出了三种常见的子模块拓扑[10]，分别是半桥型子模块、全桥型子模块和双箝位型子模块。其中，半桥型子模块目前工程中应用最为普遍，但是其不具备直流故障穿越能力，需要依靠交流断路器实现故障电流的切除。全桥和双箝位子模块都具备直流故障穿越能力，但是由于投资和运行损耗较大目前尚无工程应用。为了在换流器投资、损耗和故障电流箝位能力之间实现折中平衡，有文献[15-16]等提出了改进MMC子模块拓扑，并给出了MMC桥臂中使用多种模块拓扑混联的方式以降低工程投资的思路，但是截止目前都尚未进入工程应用阶段。

对于MMC的仿真模型，已有文献大都针对半桥型MMC开展研究，所得成果可以较容易地通过自定义编程的方式扩展至其余MMC拓扑，因此本文将着重针对半桥型MMC的仿真建模方法进行探讨。

半桥型MMC子模块的详细拓扑如图2所示，其中最主要的器件是2组反并联的IGBT和二极管以及储能电容$C$。在图2中，$K_1$是一个高速旁路开关，其作用是保证子模块发生故障时将其快速、可靠地旁路。$K_2$是一个压接式封装晶闸管，它可以在MMC闭锁时保护与其并联的续流二极管$D_2$[17]。由于$K_1$和$K_2$与子模块为并联结构，因此已有的MMC高效仿真模型大都不包含$K_1$和$K_2$，在某些特殊情况下需要仿真$K_1$、$K_2$时，本文将给出一种混合电路，用于在串联MMC阀中精确仿真$K_1$、$K_2$。图2中$R$为子模块电容的并联电阻，用于电容