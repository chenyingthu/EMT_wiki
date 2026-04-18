# 柔性直流输电系统高频稳定性分析及抑制策略(一)：稳定性分析
李云丰 1，贺之渊 2，庞辉 2，阳岳希 2，季柯 2，黄伟颖 3
(1．长沙理工大学电气与信息工程学院，湖南省 长沙市 410114；
2．先进输电技术国家重点实验室(全球能源互联网研究院有限公司)，北京市 昌平区 102200；
3．可再生能源电力技术湖南省重点实验室(长沙理工大学)，湖南省 长沙市 410114)

## High Frequency Stability Analysis and Suppression Strategy of MMC-HVDC Systems (Part I): Stability Analysis
LI Yunfeng1, HE Zhiyuan2, PANG Hui2, YANG Yuexi2, JI Ke2, HUANG Weiying3
(1. School of Electrical & Information Engineering (Changsha University of Science and Technology), Changsha 410114, Hunan Province, China; 2. State Key Laboratory of Advanced Power Transmission Technology (Global Energy Interconnection Research Institute Co., Ltd.), Changping District, Beijing 102200, China; 3. Laboratory of Renewable Energy Electric-Technology of Hunan Province (Changsha University of Science and Technology), Changsha 410114, Hunan Province, China)

**ABSTRACT:** The phenomena of high frequency resonances caused by large time delay in flexible MMC-HVDC systems have appeared in practical projects. To explore the mechanism of high frequency resonance and its key influencing factors, the high frequency state space mathematical models of MMC and AC system were established. Firstly, the model of MMC integrated the internal dynamic process, outer and inner loop, phase-locked loop, circulating current suppression and Pade approximation of large time delay, etc. The general state space model of AC system was established, in which the high frequency characteristics of AC transmission line were simulated by using the multiple $\pi$ models. Secondly, the key influencing factors such as inner loop, time delay, voltage feed forward channel, phase-locked loop, steady-state operation point, AC line length, equivalent capacitance contributing to the high frequency resonance were identified by the participation factor analysis method. Finally, the root locus method was used to study how the above factors affect the high-frequency stability of the system, and the related links were verified by electromagnetic transient simulation models.

**KEY WORDS:** flexible high voltage direct current; modular multilevel convert (MMC); state-space model; high-frequency resonance; stability analysis; root locus; participation factors

**摘要：** 柔性直流输电系统因大链路延时导致的高频振荡现象已经在实际工程出现。为探究高频振荡的机理及关键影响因素，该文首先从换流站和交流系统 2 个方面分别建立高频状态空间数学模型，换流站模型聚集 MMC 内部动态过程、控制内外环、锁相环、环流抑制及 Pade 函数模拟的大链路延时环节，交流系统则是建立以多个 $\pi$ 模型来模拟线路分布式参数特性的通用状态空间模型；其次，采用参与因子分析方法辨识出内环环节、延时大小、电压前馈、锁相环、稳态运行点、交流线路长度、线路电容等因素是导致高频振荡的关键影响环节；最后，以根轨迹方法为研究手段，阐述上述环节及其参数如何影响系统高频稳定性，并对相关环节进行电磁暂态仿真验证。

**关键词：** 柔性直流输电；模块化多电平换流器；状态空间模型；高频振荡；稳定性分析；根轨迹；参与因子

基金项目：湖南省自然科学基金项目(2021JJ40586)；可再生能源电力技术湖南省重点实验室基金项目(2020ZNDL005)。
Project Supported by Natural Science Foundation of Hunan Province (2021JJ40586); Key Laboratory of Renewable Energy Electric-Technology of Hunan Province (2020ZNDL005).

## 0 引言
基于模块化多电平换流器(modular multilevel converter，MMC)的柔性直流输电(flexible high voltage direct current，HVDC)是新一代输电技术，具有可控性好、低次谐波含量低、增压扩容方便、适应于海上风电接入等优势，近 10 年来得到快速发展 [1-3]。目前，国内在建和规划的柔性直流工程以 $500\,\text{kV}$ 交流主网接入，换流站的最大容量已经达到 $800\,\text{万}\,\text{kW}$[4]。工程的安全稳定运行对交流骨干网架的影响也越来越深刻，若柔性直流换流站因某些扰动(如高频振荡)导致闭锁，由此产生的功率盈/缺额将对接入的交流电网产生严重冲击 [5-9]。

柔性直流换流站与交流系统之间的高频振荡问题已在国内的鲁西工程和渝鄂工程中实际发生。2017 年 4 月，鲁西工程因接入的交流系统故障只有单回线路运行，导致广西电网 $500\,\text{kV}$ 母线出现 $1270\,\text{Hz}$ 的高频振荡，使得换流站闭锁[6-7]。2018 年 12 月，渝鄂工程南通道施州换流站调试期间，在换流站解锁升直流电压过程中，湖北侧出现了约 $1.8\,\text{kHz}$ 的高频振荡，该高频振荡解决方案是在电压前馈环节加入 $400\,\text{Hz}$ 的低通滤波器。然而，同样的方案应用于重庆侧时则失效，在不同时间段分别出现了 $660\,\text{Hz}$ 和 $700\,\text{Hz}$ 左右的高频振荡，由于高频振荡并未有消除的迹象，一段时间后，阀侧电流高频谐波保护动作，换流站闭锁跳闸[5]。因此，研究柔性直流输电系统的高频振荡机理及其关键影响因素具有科学和工程意义。

柔性直流输电系统在大电网互联、新能源接入、城市供电等应用场景下的振荡问题属于小干扰稳定性范畴[9-10]。该领域的研究方法主要是基于状态空间法和阻抗法，闭环系统在全频带范围内是否具有负实部的特征根，或非负阻尼特性直接决定了其稳定性[11-13]。随着这类问题研究的深入，控制系统中的锁相环(phase-locked loop，PLL)、外环及内环、环流抑制控制器(circulating current suppression controller，CCSC)、控制模式、风电场输送功率及交流电网阻抗对稳定性的影响机理也逐渐被揭示[14-16]。文献[17-20]针对风电场接入柔性直流换流站的应用场景，以谐波状态空间法和阻抗法建立了多种理论分析模型，分析了引起次同步振荡问题的关键因素，并通过优化控制系统架构、控制器参数和增加附加控制策略等手段抑制系统振荡。文献[21-22]针对张北直流电网稳定性问题，基于换流站简化模型，建立闭环系统传递函数模型，研究低频谐振振荡的关键影响因素，提出了功率前馈和桥臂串联虚拟阻抗的阻尼控制策略。然而，这些研究绝大部分没有考虑柔性直流换流站采样、传输、计算、执行等链路延时环节的影响，所得结论可能最适用于百 Hz 以下的低频段，对于高频稳定性的影响研究还需进一步揭示。

针对高频稳定性的研究，在两电平换流器采用献对考虑延时环节的影响进行大量研究，分析了延时环节和控制系统参数如何影响高频振荡的机理[23-25]。然而，这类电力电子装置的链路延时一般小于 $200\,\mu\text{s}$，其模拟往往是一阶或二阶，相较于 $550\,\mu\text{s}$ 链路延时的柔性直流输电系统来说，二阶模型难以精确模拟高频特性，所得结论可能不具有普遍性。关于柔性直流输电系统高频振荡问题，仅有少量文献开展了相关研究。文献[6-7]基于两电平模型和阻抗法研究了鲁西工程高频振荡的影响因素和抑制策略，起到了一定的抑制效果，并未从交流系统和换流站精细化模型方面进行建模，理论深度还需进一步提升。文献[8]针对渝鄂工程高频振荡问题，以 $dq$ 阻抗法建立了交流系统和换流站的数学模型，分析了关键因素对高频振荡的影响，然而这些影响仅仅局限于定性描述，没有做到定量描述。所采用的广义奈奎斯特判据是基于 2 个特征值实部与虚部相对于角频率的参数方程，通过判断曲线围绕 $(-1, j0)$ 进行稳定性判定，由于实部和虚部没有体现具体角频率信息，在判断谐振频率时，较为繁琐且曲线变化较为复杂。状态空间建模方法是通过求解系统的特征根直接判定稳定性和谐振频率，同时也能采用参与变量方法定量识别关键影响因素及其影响程度，有利于实现高阶模型的可靠降阶。

综上，本文以柔性直流工程高频振荡问题为切入点，从换流站控制系统、高精度延时和交流线路模拟等环节出发，建立表征系统全部动态特性的状态空间模型，通过求解特征根及参与因子分析，辨识引起高频振荡的关键因素及其参与程度。采用根轨迹方法，研究这些因素影响高频稳定性的规律，从规划、设计、建设、运行等方面，为实际工程规避和抑制高频振荡提供理论基础。

## 1 换流站数学模型及验证
渝鄂工程接入系统示意图如图 1 所示，换流站经换流变接入公共耦合点(point of common coupling，PCC)，再经交流线路与电网互联[5]。MMC 结构如图 2 所示，其框图可等效为如图 3 所示电路。交流系统和 MMC 之间经过交流电压和交流电流耦合，直流侧与其它换流站经直流电压和直流等效电源、等效阻抗、交流线路接入点、换流变、MMC...