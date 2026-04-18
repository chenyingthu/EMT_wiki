## 含大量电磁直流模型的机电–电磁暂态混合仿真技术研究
### Electromechanical-electromagnetic Hybrid Simulation Technology With Large Number of Electromagnetic HVDC Models

陈绪江 1，张星 1，田芳 1，张怡 2，金一丁 2，周孝信 1
（1．电网安全与节能国家重点实验室(中国电力科学研究院有限公司)，北京市 海淀区 100192；2．国家电力调度控制中心，北京市 西城区 100031）

CHEN Xujiang1, ZHANG Xing1, TIAN Fang1, ZHANG Yi2, JIN Yiding2, ZHOU Xiaoxin1
(1. State Key Laboratory of Power Grid Safety and Energy Conservation (China Electric Power Research Institute), Haidian District, Beijing 100192, China; 2. National Power Dispatching and Control Center, Xicheng District, Beijing 100031, China)

**ABSTRACT:** With the rapid development of UHVDC and the step-by-step improvement of its transmission capacity, China's power grid has the characteristics of “Strong HVDC and weak AC system”. The coupling between the transmitting and receiving ends, AC and HVDC, and multiple HVDCs is getting closer and closer so that the operating characteristics of the power grid are becoming increasingly complex. In the simulation analysis of large-scale AC-DC power grids, the HVDC obtains accurate dynamic characteristics and the AC grids can improve its simulation efficiency via electromagnetic transient simulation. However, the hybrid simulation with multiple HVDC electromagnetic transient models has difficulties in data establishment, mode adjustment and smooth start, which restricts the working efficiency and simulation accuracy of large-scale power grid analysis. In this paper, a solution is presented for automatic establishment of hybrid simulation data through HVDC standardization modeling and data mapping splicing, which greatly improves the modeling efficiency. And a method is provided for automatically adjusting the operation mode of the HVDC electromagnetic model and the smooth start of the hybrid simulation so that the hybrid simulation can reach steady state within the simulation process of 0.6s. The method proposed in this paper improves the working efficiency and simulation accuracy of electromechanical-electromagnetic.

**KEY WORDS:** large-scale AC-DC power grid; electromechanical-electromagnetic hybrid simulation; UHVDC transmission; HVDC electromagnetic model; operating condition adjustment

**摘要：** 伴随特高压直流的飞速发展和其输电容量阶跃式提升，我国电网呈现出“强直弱交”的特点。送受端、交直流、多直流之间耦合日趋紧密，电网运行特性日趋复杂。在大规模交直流电网的仿真分析中，直流输电系统需要采用电磁暂态仿真以获得准确动态特性，其余交流电网采用机电暂态仿真以提高仿真效率。然而，含多条直流电磁暂态模型的混合仿真在数据建立、方式调整及平稳启动方面存在困难，制约了大规模电网分析的工作效率和仿真精度。提供了通过直流标准化建模和数据映射拼接实现混合仿真数据自动建立的解决方案，提高了建模效率；提供了直流输电电磁模型运行方式自动调整、混合仿真接口电压箝位平稳启动的方法，使混合仿真能在 0.6s 的仿真过程内达到稳态。所提方法提高了大规模交直流电网机电–电磁混合仿真分析的工作效率和仿真精度。

**关键词：** 大规模交直流电网；机电–电磁暂态混合仿真；特高压直流输电；直流输电电磁模型；运行工况调整

DOI：10.13335/j.1000-3673.pst.2018.1810

基金项目：国家重点研发计划资助项目(2018YFB0904500)。
Project Supported by National Key Research and Development Program of China (2018YFB0904500).

## 0 引言
能源与负荷需求之间的反向分布是中国的基本国情之一，也是电力系统规划和运行中应该考虑的重要因素[1]。高压直流输电已成为我国区域间最常见的电力传输方式，它将西部的可再生能源传输到东部满足负荷需求。伴随特高压直流快速发展和输电规模阶跃式提升，“强直弱交”矛盾突出，送受端、交直流、多直流之间耦合日趋紧密，电网运行特性发生了深刻变化。由于高压直流输电并不总是可靠，整个电力系统的稳定性受到威胁。

对于送端电网，高压直流输电的换相失败等暂态过程对西北地区风电场的运行产生了影响，已实际发生了一些事故[2-4]。如文献[3]提供的一个案例分析，虽然是受端交流电网发生了故障，但引发了HVDC 的换相失败或闭锁，进而引发送端电网瞬态过电压振荡并导致风机部分脱网，此后无功过剩进一步推高电压，导致风机脱网越发严重。对于直流多馈入的受端电网，发生交流系统故障可能造成多回直流同时换相失败，实际系统中也多次发生交流故障造成多回直流同时换相失败的事故[5-8]，随着直流接入规模的增大，需滚动校核多直流同时换相失败对受端电网安全稳定性的影响[9]。

机电暂态仿真程序所采用的直流模型均是准稳态模型，可以对直流双极闭锁等严重故障进行模拟计算[10-11]，但对于研究交流系统不对称故障对直流换相过程的影响、直流控制系统对系统稳定性的影响等问题时，难以给出合理的结果[12]，因此现有以机电暂态为主导的大电网仿真难以准确描述直流系统快速暂态特性，导致电网运行分析精确度不够，难以满足交直流大电网分析的要求，在模拟直流换相失败、励磁涌流等非基波、非线性特性时也可能存在较大误差。电磁暂态仿真模拟精度高，选用合适的模型能够准确模拟换相失败等直流的动态过程，但其模型复杂、计算规模有限，难以成为大电网运行仿真分析的主要研究手段。

近年来，机电–电磁混合仿真在大电网分析中得到越来越多的应用，通过将直流输电及其周边区域采用电磁暂态建模、其他交流电网采用机电暂态建模，能够实现更加精细化的电网仿真，兼顾仿真精度和仿真规模，已成为国网和南网运行方式计算的重要工具。

在国调方式计算等混合仿真应用场景中，交直流混联电网一般先进行方式调整和潮流计算，然后人工建立各回直流的电磁暂态模型，再人工定义电磁侧直流模型与机电侧大电网之间的混合仿真接口，以实现混合仿真。在混合仿真数据产生以后，还需要根据在线潮流将电磁侧各回直流模型的运行工况调整到与潮流一致的状态，并解决混合仿真启动时机电侧与电磁侧接口电压不匹配导致的暂态冲击问题。传统方法通常采用在接口处添加临时箝位电源，待混合仿真稳态建立的情况仿真人员设定钳位电源切除时间。这种混合仿真启动方法，可以避免启动阶段潮流不平衡对整个大电网的冲击与相互影响，但在大批量的计算方式扫描计算中，每个任务都进行一次初始化，浪费了大量的时间和计算资源。

由于电磁直流模型建模复杂，运行工况人工调整工作量大，难以从稳态直接启动，这些问题制约了含大量电磁直流模型的机电–电磁暂态混合仿真在大批量方式计算校核以及在线分析中的应用。本文将就含大量电磁直流模型的机电–电磁暂态混合仿真批量式仿真分析面临的建模工作效率、电磁直流模型初始工况调整及混合仿真平稳启动方面的问题提出有效可行的技术方法。

## 1 技术框架
由于电磁直流模型建模复杂，运行工况人工调整工作量大，难以从稳态直接启动，这些问题制约了含大量电磁直流模型的机电–电磁暂态混合仿真在大批量方式计算校核以及在线分析中的应用。为了解决上一瓶颈问题，本文提出了根据潮流数据和指定分网方案的机电–电磁暂态混合仿真数据自动建立和电磁直流模型自动初始化和混合仿真平稳启动的技术框架，如图 1 所示。

含大量电磁直流模型的机电–电磁暂态混合仿真建模及仿真计算的具体步骤为：
1）面向实际直流工程分别建立电磁直流标准化模型作为模型库，并建立电磁直流模型库与方式计算数据或在线数据中直流元件的映射关系。
2）根据混合仿真分网预案确定电磁暂态仿真的直流工程范围并从电磁直流模型库中调取仿真模型，实现电磁暂态仿真数据拼接。
3）程序自动定义机电–电磁暂态混合仿真接口，自动添加接口平稳启动的临时箝位电源。
4）采用本文描述的初始化方法，基于潮流数据对电磁直流模型进行运行状态的初始化。
5）混合仿真启动进行到稳态，切除箝位电源，保存运行点，套用预设的故障集，启动交直流大电网