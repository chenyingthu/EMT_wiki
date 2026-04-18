# 连接弱交流电网的柔性直流换流站外环控制器参数解析计算及其限制因素分析
Analytical Calculation Method of Outer Loop Controller Parameters of HVDC Converter Station Connected to Weak AC Grid and Analysis of Limiting Factors

李云丰 1，赵文广 1，贺之渊 2*，杨杰 2，周家培 2，许杰锋 1
(1．电网防灾减灾全国重点实验室(长沙理工大学)，湖南省 长沙市 410114；2．先进输电技术全国重点实验室(国网智能电网研究院有限公司)，北京市 昌平区 102200)

LI Yunfeng1, ZHAO Wenguang1, HE Zhiyuan2*, YANG Jie2, ZHOU Jiapei2, XU Jiefeng1
(1. State Key Laboratory of Power Grid Disaster Prevention and Reduction (Changsha University of Science and Technology), Changsha 410114, Hunan Province, China; 2. State Key Laboratory of Advanced Power Transmission Technology (State Grid Smart Grid Research Institute Co., Ltd.), Changping District, Beijing 102200, China)

**ABSTRACT:** The dynamic response speed of AC voltage of flexible high voltage direct current (HVDC) converter connected to weak AC grid is manly related to the parameters of AC voltage controller, SCR, steady state operating points and equivalent capacitance paralleled at point of common coupling (PCC). Firstly, due to the lack of analytical calculation of the parameters of AC voltage controller and analysis of their limiting factors, the key influence variables and participations of eigenvalues related to dynamic response and stability have been analyzed according to the distribution of zeros and poles based on the detailed analytical model of whole system. Secondly, based on the quasi steady state model of AC system, the analytical calculation expressions of outer loop controller parameters are derived, and their selection ranges are preliminarily analyzed. Thirdly, the effects of outer loop controller parameters, bandwidth of current inner loop, PLL parameters and SCR on stability are studied. The results show that bandwidth of PLL closed to that of AC voltage loop may not be the factor inducing resonance of system. Reducing the parameters of AC voltage controller and PLL can improve the stability of converter station running in inverter mode. Finally, the correctness of parameter calculation and stability analysis is verified by electromagnetic transient simulations.

**KEY WORDS:** weak AC grid; flexible high voltage direct current (HVDC) converter; parameter analytical calculation; impedance model; stability analysis

**摘要：** 柔直换流站连接弱交流电网的交流电压动态响应速度与交流电压控制器参数、短路比、稳态点和公共耦合接入点并联等效电容有关。针对柔直换流站连接弱交流电网外环控制器参数解析计算及其限制因素分析研究欠缺问题，该文在建立整个系统详细模型的基础之上，根据外环闭环传递函数零极点分布情况，分析影响系统动态响应速度和稳定性相关特征根的关键变量及其参与程度。其次，基于交流系统准稳态模型，推导外环控制器参数解析计算表达式，并对其选择范围进行了初步分析。再次，研究外环控制器参数、电流内环带宽、锁相环参数以及短路比对稳定性的影响，结果表明，外环带宽与锁相环带宽接近并不一定是诱导系统发生谐振失稳的因素，降低交流电压控制器和锁相环参数有利于提升柔直换流站运行于逆变状态下的稳定性。最后，通过电磁暂态仿真验证了参数计算与稳定性分析的正确性。

**关键词：** 弱交流电网；柔直换流站；参数解析计算；阻抗模型；稳定性分析

**基金项目：** 国家电网公司总部科技项目(5100-202158471A-0-5-ZN)。
**Project Supported by the Technology Project of State Grid Corporation of China (5100-202158471A-0-5-ZN).**

## 0 引言
基于模块化多电平换流器(modular multilevel converter，MMC)的柔性直流输电技术(flexible high voltage direct current，HVDC)，采用了具有自主关断能力的电力电子器件，为有功类和无功类的解耦控制提供了坚实基础[1-2]。柔性直流输电克服了常规直流输电需要交流电源提供换相电压的根本缺陷，其优越的控制与运行性能引起了输电领域的重大变革，为多回直流落点负荷中心、异步电网跨区互联、偏远地区弱交流电网支撑、新能源送出等应场景提供了较好的解决方案[3-5]，有利于促进我国“碳达峰、碳中和”战略目标的早日实现。

柔性直流换流站连接交流电网的控制方式与其是否有同步电源以及交流电网强度密切相关[6-7]。短路比(short circuit ration，SCR)作为衡量交流电网强度的指标[8-9]，其定义为公共耦合接入点(point of common coupling，PCC)的短路容量与额定直流功率之比，当 $SCR \ge 3$ 时认为是强电网；当 $2 \le SCR < 3$ 时为弱电网；$1 < SCR < 2$ 为极弱电网。上述只是从静态角度给出的参考定义，实际系统的稳定性与交直流系统主电路和控制系统多个因素相关。弱交流电网主要呈现以下特征[10-12]：1）输电线路长导致线路等效阻抗大、抗扰动能力弱、线路容性效应强；2）同步发电机数目少致使转动惯量低，交流电压和频率支撑能力弱，功角稳定性较弱；3）有功功率与无功功率之间呈现非线性强耦合关系。

柔直换流站连接弱交流电网时，控制系统一般采用交流电压控制以提升对弱交流电网的支撑能力，其主电路模型分为两种，一种是不考虑 PCC 点等效电容[9]，另外一种是考虑等效电容[13-14]。尽管 MMC 型换流站无需在 PCC 点并联滤波器，但是从弱交流电网所呈现出的特征来说，考虑 PCC 点等效电容更符合实际工程情况。这是因为弱交流电网具有长交流线路特征，在 PCC 点的等效电容不能被忽略；再加上高功率水平运行时，为了维持 PCC 点电压恒定，换流变压器和交流线路产生的感性无功功率需要有容性无功功率进行补偿，否则将会增加 MMC 的容量和功率损耗，降低了经济性。不管是否考虑 PCC 点等效电容以及何种控制模式，柔直换流站连接弱交流电网均有发生失稳现象的风险，特别是连接极弱交流电网情况下[15]。

针对柔直换流站连接弱交流电网存在的失稳风险，相关文献采用状态空间法[16]、动力学[17]、阻抗法[18]和频率响应解析计算[19]等形式研究了系统失稳情况下的机理及其关键影响因素，指出锁相环出了非线性功率控制方法，通过构建的李亚普若夫能量函数验证了所提方法的正确性。文献[23]通过改进外环控制结构提出一种先进的双闭环矢量控制策略，有效提高换流站连接弱电网的功率运行范围。文献[24]利用功率同步控制提出 MMC 连接弱交流电网时的虚拟电阻控制策略，分析了虚拟电阻的作用机理并采用根轨迹方法给出了虚拟电阻的选择范围。文献[25]在分析弱交流电网 PV 曲线的基础上，提出一种功率交叉耦合补偿控制策略，并利用根轨迹方法设计了交叉补偿系数。文献[26]考虑三相并网系统连接弱交流电网时 PLL 带宽过大所导致的谐振失稳问题，提出了一种在内环输出与调制环节之间的相角补偿控制方法，并利用波特图实现了补偿参数选择范围的设计。然而，上述文献尽管在失稳机理和稳定性提升方面做了很多努力工作，但是关于柔性直流换流站连接交流弱电网的外环控制器参数解析计算方法方面所做的研究工作鲜有涉及。

针对上述问题，本文在建立详细模型的基础上，分析了影响外环动态响应速度和系统稳定性的关键环节，推导了外环控制器参数的解析计算表达式，初步给出了参数选择的限制范围，并从幅值裕度和相位裕度两个维度分析了相关环节参数如何影响系统稳定性的机理。

## 1 主电路结构与控制系统架构
柔直换流站接入弱交流电网的简化主电路如图 1 所示。图中：$U_g$ 和 $U_s$ 为等效电源和 PCC 点相电压幅值；$\delta$ 为相位差；$R_g$ 和 $L_g$ 为交流电网等效阻抗，$C_{pcc}$ 为 PCC 点无功补偿和线路总等效电容；$R_t$ 和 $L_t$ 为换流变压器等效电阻和漏感；$I_g$、$I_c$ 和 $I_s$ 为交流系统、等效电容和换流站电流；$P_g$ 和 $Q_g$ 是交流电网注入 PCC 点的有功和无功功率；$Q_c$ 是等效电容 $C_{pcc}$ 注入 PCC 点的无功功率；$P_s$ 和 $Q_s$ 是交流电网注入换流变压器的有功和无功功率；$u_{dc}$ 和 $i_{dc}$ 为 $P_g, Q_g$ $P_s, Q_s$ $U_g \angle 0$ $R$ $I$ $L_g$