# MMC-UPFC 电磁–机电混合仿真技术研究

**叶小晖，汤涌，刘文焯，宋新立，李霞，吴国旸**  
（电网安全与节能国家重点实验室(中国电力科学研究院有限公司)，北京市 海淀区 100192）

**Research on MMC-UPFC Electromagnetic-electromechanical Hybrid Simulation Technology**  
YE Xiaohui, TANG Yong, LIU Wenzhuo, SONG Xinli, LI Xia, WU Guoyang  
(China Electrical Power Research Institute, Haidian District, Beijing 100192, China)

**ABSTRACT**: In view of the demand for large-scale power grid simulation ability in the southern Suzhou 500 kV UPFC project, the electromagnetic transient modeling for unified power flow controller (UPFC) based on modularized multilevel converter (MMC) technology is carried out. The adaptability of the hybrid simulation interface position to different working conditions is explored with the IEEE 39 node example, Finally, an example of Suzhou 500 kV UPFC project is given to demonstrate the effectiveness of the proposed model and the hybrid interface.  
**KEY WORDS**: UPFC; hybrid simulation; electromagnetic transient model; interface position

**摘要**：针对苏州南部 500 kV UPFC 工程对大规模电网仿真能力提出的需求，对基于模块化多电平(modular multi-level converter，MMC)技术的统一潮流控制器(unified power flow controller，UPFC)进行了电磁暂态建模，结合 IEEE 39 节点实例探索了混合仿真接口位置针对不同工况的适应性，最后基于苏州 500 kV UPFC 工程算例验证了所建立模型以及混合接口的有效性。  
**关键词**：统一潮流控制器；混合仿真；电磁暂态模型；接口位置

**DOI**：10.13335/j.1000-3673.pst.2018.1467  
**基金项目**：国家电网公司总部科技项目(适用于电磁暂态仿真的交直流设备仿真建模及初始化技术研究)。  
Project Supported by Science and Technology Project of SGCC.

## 0 引言

随着超/特高压远距离输电的建设和新能源大规模接入，我国电网网架结构日益复杂，特别是电网发展建设过程中，电网潮流变化大，给电网的运行调度提出了更高要求。电力电子技术在柔性输电(flexible AC transmission systems，FACTS)方面的应用可以大大提升交流线路的可控性，优化电网潮流。作为第 3 代 FACTS 技术的代表，统一潮流控制(unified power flow controller，UPFC)具有串联和并联系统的综合控制能力[1-2]。可以通过控制系统调节线路参数和功率，分别或同时实现并联补偿、串联补偿、移相等几种不同的功能，提高线路的传输能力、稳定性及阻尼振荡等，可提高大规模电网的潮流控制能力[3-6]。

自 1998 年世界第 1 套 UPFC 在美国 Inez 投运以来，国外共有 4 套 UPFC 工程投入运行[7-9]，这些工程由于普遍采用门级可关断晶闸管(gate turn-off thyristor，GTO)和曲折变压器技术，存在 GTO 阀驱动复杂、损耗大，变压器结构复杂、设备占地面积大、制造成本高，控制保护系统的扩展性、移植性、维护性较差等缺点。

江苏电网分别于 2015 年底和 2017 年底正式投运了南京西环网 220 kV UPFC 示范工程[10]和苏州南部电网 500 kV UPFC 科技示范工程[11]，前者是世界上首个使用模块化多电平(modular multi-level converter，MMC)技术的 UPFC 工程，后者是世界上电压等级最高、容量最大的 UPFC 工程，2 个工程的建设对大规模电网的仿真与建模技术提出了更高的要求。

柔性输电技术主要作用于大规模电网的潮流动态特性，局部电磁暂态仿真虽然可以详细仿真系统中的每一个器件的响应过程[12]，但是由于电网规模较大，受限于目前硬件的计算能力，需要对电网参数进行大量的等值替代，会对仿真精度有较大影响[13]；如果通过机电暂态软件进行仿真，虽仿真能力不再受电网规模限制，计算速度也比较快，但机电暂态一般采取准稳态模型进行仿真，并不能反映系统的动态响应能力以及由于三相不平衡引起的波形畸变等情况[14-15]。

基于以上原因，研究电磁–机电暂态混合仿真技术，对含有 UPFC 的电力系统进行混合仿真，既能体现 UPFC 的动态过程，又能保留外网特性，可较好地实现对复杂系统的仿真分析，具有重要的理论意义和工程实用价值[16-20]。混合仿真当前主要采用交–直接口方案，使用电磁暂态技术对直流系统进行精细化仿真并以直流换流站变压器交流侧母线作为接口母线，这种方案在直流仿真中得到了广泛应用[21]。Reeve 和 Adapa 等提出了交–交接口方案，探讨了将接口扩展到交流后的优缺点[22]，但这种方案建立在直流仿真的基础上，仍是交–直接口的扩展[23]。针对于 UPFC 等 FACTS 设备的交–交接口方案尚无研究。

针对目前含 UPFC 电网仿真手段存在的局限性，本文搭建了含 UPFC 电力系统的仿真模型，并且结合 IEEE 39 节点系统探索了混合仿真接口的位置在不同工况下的适应性；最后基于苏州 500 kV UPFC 工程的算例验证本文模型以及混合接口的有效性。

## 1 UPFC 模型介绍

### 1.1 江苏 UPFC 工程结构

目前江苏建有 2 条 UPFC 工程。南京西环网 220 kV UPFC 工程的建设是为解决南京西环网近远期潮流分布不均、整体供电能力受限且开辟新的输电通道代价高昂的问题[10]。该工程安装在铁北—晓庄双回线路上，共设置 2 个串联换流变和一个并联换流变，并联换流变接在 35 kV 母线上。苏州南部 500 kV UPFC 工程的建设是为解决苏州南部电网动态无功电压支撑能力不足的问题和直流小方式下梅里—木渎双线的 N–1 过载问题[11]。该工程安装在梅里—木渎双回线的木渎侧，其系统结构如图 1 所示。

**图 1 苏州 500 kV UPFC 结构**  
*Fig. 1 Structure of Suzhou 500 kV UPFC*

在这 2 个工程中，串联侧 2 个换流器通过 2 个管旁路开关导通，保护换流阀免受冲击。TBS 动作时间小于 2 ms，可以在变压器机械旁路开关合闸前动作。

### 1.2 UPFC 换流器与 TBS 数学模型

#### 1.2.1 MMC 桥臂模型

江苏 UPFC 工程中采用的换流器均为 MMC，较为通用的 MMC 仿真模型有平均值模型、基于受控源的高效模型和戴维南等效模型[24]。本文采用戴维南等效模型[25]，其原理如图 2 所示。

**图 2 戴维南等效模型**  
*Fig. 2 Thevenin equivalent model*

图 2(a)中，$I_{SM}$ 为桥臂电流，子模块电容中流过的电流 $I_C$ 的取值以及子模块端口电压 $V_{SM}$ 的取值均取决于该子模块的投切状态。当子模块为切除状态时，电容电压保持不变；当子模块为投入状态时，则子模块电容会根据桥臂电流方向的不同，进行充电或者放电，电容电压随之变化。

电容可以用后退欧拉法表示为式(1)的形式，等效为电阻 $R_C$ 和电源 $V_C(t-\Delta t)$ 的并联电路：

$$V_C(t) = V_C(t - \Delta t) + \Delta V_C = V_C(t - \Delta t) + I_C \frac{\Delta t}{C} = V_C(t - \Delta t) + I_C R_C \tag{1}$$

其中：$\Delta t$ 为仿真步长；$C$ 为子模块电容容值；$R_C$ 为戴维南等效电阻。

假设所有二极管、IGBT 的通态电阻都为 $R_{ON}$。对于图 2(b)中单个子模块的戴维南子模块等效电路，各电气量可以用式(2)代入式(4)公式表示：

$$R_{SMEQ} = \begin{cases} R_{ON} + R_C, & \text{投入} \\ R_{ON}, & \text{切除} \end{cases} \tag{2}$$