DOI:10.13334/j.0258-8013.pcsee.2010.13.002

## 考虑不对称故障的机电暂态–电磁暂态混合仿真方法
刘文焯，侯俊贤，汤涌，宋新立，万磊，范圣韬
(中国电力科学研究院，北京市 海淀区 100192)

## Electromechanical Transient/Electromagnetic Transient Hybrid Simulation Method Considering Asymmetric Faults
LIU Wen-zhuo, HOU Jun-xian, TANG Yong, SONG Xin-li, WAN Lei, FAN Sheng-tao
(China Electric Power Research Institute, Haidian District, Beijing 100192, China)

**ABSTRACT:** An effective solution of electromechanical transient and electromagnetic transient hybrid simulation was proposed, including interface selection, mutual equivalence methods between electromechanical transient and electromagnetic transient network. It is able to deal with the situation that the positive and negative sequence parameters of equivalence circuit are different. Least square method was adopted to obtain three-sequence fundamental frequency current which indicated the influence of electromagnetic transiet simulation on the electromechanical network. The solution is demonstrated effective and feasible through several cases. Problems in hybrid simulation are solved when various faults (including symmetric and asymmetric faults) occur in electromechanical network.

**KEY WORDS:** HVDC transmission; electromechanical transient; electromagnetic transient; hybrid simulation; Norton equivalence

**摘要：** 提出一套机电暂态–电磁暂态混合仿真方案，包括接口母线的选取方法、机电暂态子系统对电磁暂态子系统的等效、等值电路正序和负序参数不相等情况的处理(基波负序补偿法)，并采用最小二乘法求取 3 序基波电流来反映电磁暂态系统仿真结果对机电暂态网络的影响。仿真计算结果证明了该套仿真方案的有效性和可行性，解决了机电暂态网络发生各种对称和不对称故障复杂情况下局部电路的详细电磁暂态仿真问题，并通过了大型电网仿真的检验。

**关键词：** 高压直流输电；机电暂态；电磁暂态；混合仿真；诺顿等值

基金项目：国家自然科学基金重大项目(50595412)；国家电网公司科技项目(SGKJ[2007]189)。
Project Supported by National Natural Science Foundation of China (50595412); Project Supported by the State Grid Corporation of China (SGKJ[2007]189)．

## 0 引言
电磁暂态仿真与机电暂态仿真进行接口混合仿真的需求是从直流输电研究开始的。机电暂态程序描述直流换流站和直流线路时通常采用准稳态模型，其假设条件为：1）换流器母线的三相交流电压是对称、平衡的正弦波；2）换流器本身的运行是完全对称平衡的；3）直流电流和直流电压都是平直的；4）换流变压器不考虑饱和，忽略激磁电流。

直流准稳态模型的缺陷是非常明显的，具体表现在：1）准稳态模型在不对称故障期间不适用；2）换流器本身的暂态过程忽略不计，不能表示详细的换相过程，不能表示不对称故障对换流阀的影响和换流器内部故障、逆变器换相失败以及控制系统对换流过程的影响等；3）不能确切表示直流线路故障，以及在此情况下的直流后续控制行为。因此，要想准确研究直流系统的详细暂态过程，直流的仿真必须采用电磁暂态模型。

传统电磁暂态程序受到模型、算法以及步长的限制，只能对局部小型装置或网络进行电磁暂态仿真，并且需要将与其相连的外部电网进行等值化简。当接口处与外部电网联系较弱，如直流系统换流母线两端交流系统的短路容量相对于直流额定输送功率较小(有效短路比小于 2.5)，以及计算时间超过常见的电磁暂态仿真领域而进入电网中机组的摇摆过程(数秒至数十秒)时，采用等值化简后的系统来表示整个外部电网就不能满足仿真的需要。

为弥补上述机电暂态仿真和电磁暂态仿真的不足，Heffernan 等人首先提出了在暂态稳定程序中考虑 HVDC 系统详细暂态模型的混合仿真算法 [1-9]，其基本思想是根据对电力系统各区域研究兴趣的不同，把电力系统分解为电磁暂态子系统、机电暂态系统以及接口母线这 3 个部分。含有电力电子装置的详细系统定义为电磁暂态子系统，使用电磁暂态程序进行详细仿真；而把传统的外部交流电力网络定义为机电暂态系统，使用机电暂态程序进行仿真；联接 2 个子系统的母线定义为混合仿真的接口母线，电磁暂态子系统和机电暂态子系统通过接口母线进行 2 种仿真的同步和数据交换。由于超大规模的电网采用的是机电暂态程序进行仿真，而局部需详细研究的小系统使用微秒级步长的电磁暂态仿真，所以机电暂态–电磁暂态混合仿真算法既可以精确地模拟非线性电力电子器件的动态特性，又可以准确仿真大规模电网，具有较高的仿真效率。

由于中国东部和南方面临能源紧缺的问题，中国采取了西电东送、发展特高压智能电网的战略，特高压长距离直流送电显得极其重要，许多国内学者自 2005 年以来，先后开展了电力系统机电暂态、电磁暂态以及机电暂态–电磁暂态的混合仿真研究 [10-22]。

本文提出一套机电暂态–电磁暂态混合仿真方法，包括接口选取方法、机电暂态子系统对电磁暂态子系统的等效方法、等值电路正序和负序参数不相等情况的处理以及电磁暂态系统仿真结果对机电暂态网络的等效方法等，能完全适应电网中发生各种对称和不对称故障复杂情况下局部电路的详细电磁暂态仿真问题，并通过了大型电网仿真的检验。

$P + jQ$

**图1** 采用 AC-DC 系统换流器端母线作为接口母线的混合仿真方法
**Fig. 1** Hybrid simulation method which selects converter AC buses as the interface buses

**表1** 电磁暂态和机电暂态网络划分与计算的对比
**Tab. 1** Differences of network partition and calculation between electromechanical and electromagnetic transient simulation

| 项目 | 机电暂态系统 | 电磁暂态子系统 |
|---|---|---|
| 网络划分 | 发电机、励磁、调速、电力系统稳定器、变压器、线路、负荷和安全自动装置等 | 换流器、换流变压器、无功补偿、滤波器、直流线路、平波电抗器、灵活交流输电系统和控制保护系统等 |
| 网络规模 | 庞大，几万个节点，几千台发电机 | 规模小，只限于局部系统的详细研究，如直流、灵活交流输电系统和微网等 |
| 积分算法 | 隐式梯形算法、吉尔(Gear)法、龙格–库塔法等 | 隐式梯形算法(需处理网络突变和事件发生)和状态空间解法等 |
| 步长 | 周波级 | 微秒级 |
| 计算速度 | 快 | 慢 |
| 电网模型 | 基波、正序、相量模型，用负序、零序表达网络不对称情况 | abc 三相、瞬时值模型 |
| 研究目标 | 全网能量传输、功角稳定、电压稳定等问题 | 详细研究局部系统的响应和接口处功率的变化 |

如果接口母线选为换流器的终端母线，电磁暂态子系统和机电