# 含电池储能的直流配电网振荡抑制有源阻尼控制及参数计算方法
罗华伟 1，王立娜 1，吴昌龙 1，徐志强 1，陈霖华 1，龚岸榕 1，李云丰 2，陈星 3，谭鑫 1
（1．规模化电池储能应用技术湖南省工程研究中心(湖南经研电力设计有限公司)，湖南省 长沙市 410007；
2．长沙理工大学电气与信息工程学院，湖南省 长沙市 410114；
3．国家电投集团湖南娄底新能源有限公司，湖南省 娄底市 417000）

## Active Damping Control and Parameter Calculation for Resonance Suppression in DC Distribution Network
LUO Huawei1, WANG Lina1, WU Changlong1, XU Zhiqiang1, CHEN Linhua1, GONG Anrong1, LI Yunfeng2, CHEN Xing3, TAN Xin1
(1. Hunan Engineering Research Center of Large-scale Battery Energy Storage Application Technology (Hunan Economic Institute Electric Power Design Co., Ltd.), Changsha 410007, Hunan Province, China;
2. School of Electrical & Information Engineering, Changsha University of Science and Technology, Changsha 410114, Hunan Province, China;
3. SPIC Hunan Loudi New Energy Co., Ltd., Loudi 417000, Hunan Province, China)

**ABSTRACT:** The bidirectional DC-DC converter operating in the buck mode is one of the main factors causing the resonant instability in the DC distribution network. Firstly, the impedance model of the three-phase VSC considering the dynamic process of the AC system and the one of the bidirectional DC-DC converter are established in this paper through a simple case of a DC distribution network. The influence of the main circuit parameters, the control system parameters and the steady-state operation points on their impedance models has been analyzed. The mechanism of the resonant instability in the DC distribution network induced by the DC network equivalent inductance and the bidirectional DC-DC converter is therefore revealed. Secondly, an active damping control strategy of the DC current feedback of the bidirectional DC-DC converter is proposed by considering the impedance characteristics required for the DC distribution network resonance suppression. After that, the influence of the damping controller parameters on its impedance characteristics is studied. Thirdly, taking the parallel resonance suppression of the battery energy storage device and the series resonance suppression of the DC network as the two constraints, the expression of the parameter selection range of the damping controller is presented. Finally, the correctness of the calculation formula is verified by the electromagnetic transient simulation.

**KEY WORDS:** DC distribution network; battery energy storage; bidirectional DC-DC converter; resonance stability; damping control; parameters calculation

**摘要：** 运行于 Buck 模式的双向 DC-DC 变换器是引起直流配电网发生振荡失稳的主要因素之一。首先，该文通过简单的直流配电网案例，建立了三相 VSC 考虑交流系统动态过程的阻抗模型和双向 DC-DC 变换器的阻抗模型，分析了主电路参数、控制系统参数以及稳态运行点对两者阻抗模型的影响程度与规律，并揭示了直流网络等效电感和双向 DC-DC 变换器相互作用诱发直流配电网振荡失稳的机理。其次，从直流配电网振荡抑制所需的阻抗特性角度考虑，提出了一种双向 DC-DC 变换器反馈直流电流的有源阻尼控制策略，并研究了阻尼控制器参数对其阻抗特性的影响规律。再次，以电池储能装置并联谐振抑制和直流网络串联谐振抑制为约束条件，解析了阻尼控制器的参数选择范围表达式。最后，采用电磁暂态仿真验证所给计算公式的正确性。

**关键词：** 直流配电网；电池储能；双向 DC-DC 变换器；谐振稳定性；阻尼控制；参数计算

**基金项目：** 湖南省科技创新重大项目(2020GK1010)；湖南经研电力设计有限公司科技项目(基于电池储能的交直流柔性配电网故障运行关键技术研究)。
**Project Supported by** Science and Technology Innovation Major Project of Hunan Province(2020GK1010); Science and Technology Project of Hunan Economic Institute Electric Power Design Co., Ltd (Research on Key Technologies of Fault Operation of AC/DC Flexible Distribution Network Based on Battery Energy Storage).

**DOI：** 10.13335/j.1000-3673.pst.2022.0199

## 0 引言
随着我国提出了“碳达峰、碳中和”发展战略的要求，大力发展风电、光伏等可再生能源成为不可阻挡的历史趋势[1-3]。在新能源、直流负荷的渗透率不断提高的情况下，作为今后电力系统的重要组成部分，融合电池储能装置的直流配电网在中小规模可再生能源接入与送出以及工业园区供电能力提升方面已经逐渐显示出其独有的优势，具有广阔的发展空间，当前国内外已有多个直流配电网工程投入运行[4-5]。

三相电压源换流器(voltage source converter，VSC)和双向 DC-DC 变换器通常作为直流配电网的功率接口装置[6-7]，前者用于连接交流系统和直流系统，后者多用于连接直流网络和其他不同类型的直流系统，例如电池储能装置。相比于交流系统来说，含有三相 VSC 和双向 DC-DC 变换器的直流配电网是典型的电力电子化系统，具有更加快速的灵活可控特性以及短路故障电流发展特性[8-10]。为了抑制短路故障电流的发展与传播以及为保护系统和直流开断装置争取更多时间，在各个装置出口配置一定大小的直流限流电抗器是一种经济可行的方案[5,11]。然而，直流限流电抗器也带来了不利影响，例如与快速控制的双向 DC-DC 变换器相互作用恶化了直流配电网的谐振稳定性，可能诱发振荡失稳，威胁直流配电网的可靠与安全运行[12-14]。直流配电网谐振振荡的本质是各个装置控制不协调所产生的瞬时功率振荡现象。若是采用阻抗理论解释，则是某些个装置的呈现出“负电阻”效应[15]。

针对含有电池储能装置的直流配电网谐振稳定性和振荡抑制问题，相关文献从模型构建、机理分析、振荡抑制等方面做了大量的理论研究工作[7,14-20]。文献[16]以全局下垂控制策略为基础，在考虑 VSC 交直流瞬时功率、系统损耗以及不确定性因素之后，建立了系统阻抗模型并采用 2 自由度方法设计了鲁棒控制器。文献[18]推导了孤网运行模式下含有恒功率负荷的直流微电网小干扰线性化状态方程，提出了以直流电压和直流电流为状态反馈变量的阻尼控制策略。文献[19]提出了直流微电网下垂控制的 DC-DC 变换器阻容输出阻抗设计方法，给出了电容的选择准则和下垂阻抗设计准则，采用简单的级联结构，分析了负载特性和控制器参数对直流微电网的稳定性影响，指出电源的快速控制有利于提升稳定性，而负载的快速控制则会恶化稳定性。文献[24]以直流微电网中各装置的阻抗匹配为目标，提出了 VSC 的串联虚拟阻抗控制方法，并利用 Middlebrook 稳定判据对串联虚拟阻抗后的系统进行了稳定性分析。上述文献在直流配(微)电网建模和稳定控制方面做了非常充足的工作，但均是以系统高阶模型为基础对阻尼控制器参数进行设计，并没有给出相关参数选择范围的解析表达式。

本文以级联的三相 VSC 和含有双向 DC-DC 变换器的电池储能装置为案例，在揭示直流配电网振荡失稳机理之后，提出了在双向 DC-DC 变换器中反馈直流电流的有源阻尼控制策略，并对阻尼控制器参数的选择范围进行了解析计算与验证。

## 1 直流配电网主电路结构
本文重点是反馈双向 DC-DC 变换器直流电流进行有源阻尼控制，为方便参数解析计算，将以图 1 所示的 VSC 和电池储能模型为例开展理论研究。图 1(a)中：$u_{gabc}$ 和 $i_{gabc}$ 为交流系统等效三相电源和电流；$u_{sabc}$ 和 $i_{sabc}$ 为接入点三相电压和电流；$u_{cabc}$ 为 VSC 交流侧输出的三相电压；$u_{dc}$ 和 $i_{dc1}$ 为直流侧电压和电流；$L_{dc1}$ 为 VSC 直流侧出口的直流限流电抗器。图 1(b)中：储能电池用理想电压源 $E_{be}$ 代替，经过功率双向 DC-DC 变换器与直流配电网连接；$L_{dc2}$ 为电池储能装置出口的直流限流电抗器；$u_{dccb}$ 为支撑电容电压；$i_{lb}$ 为缓冲电感电流；$i_{dc2}$ 为 DC-DC 变换器的直流电流；滤波电感 $L_f$ 和滤波电容 $C_f$ 平抑双向 DC-DC 变换器产生的高频脉动电流。储能电池放电时 DC-DC 变换器工作于升压模式，充电时工作于降压模式；各个元器件的电压和电流方向如图 1 所示。系统相关参数如表 1、2 所示。

Lg      us ab c         Zeq                idc1
igabc
         Ldc1     接入
V
is ab c
ucabc   S    udc