## 新型电力系统电磁暂态并行仿真关键技术及展望
江艺宝，于佳乐，赵浩然，李 冰，韩明哲，赵长旺
（山东大学电气工程学院，济南 250061）

**摘 要：**在“碳达峰、碳中和”战略目标驱动下，电力系统逐渐发展成为高比例新能源并网和高比例电力电子设备接入的新型电力系统，其电源结构、电网形态和运行特征发生了显著变化。电磁暂态仿真由于能够全面、精确刻画电力系统的高频动态特性，已成为掌握新型电力系统运行特性的关键手段。然而，传统串行计算模式下的电磁暂态仿真技术在仿真效率上无法应对新能源大规模并网、交直流复杂耦合的仿真场景，亟需从高效并行算法和硬件加速角度出发，开展并行计算模式下的电磁暂态仿真相关研究。为此，首先概括了新型电力系统对电磁暂态仿真的新需求；其次，介绍了电磁暂态仿真的分网并行算法；再次，介绍了能够进一步提升电磁暂态仿真效率的多速率仿真方法；接着，介绍了基于并行计算设备的并行仿真实现方案；最后，梳理了国内外电磁暂态仿真平台的并行策略，总结指出算法硬件深度融合的仿真平台是未来的发展方向，并对其中的关键技术进行分析和展望。
**关键词：**新型电力系统；电磁暂态；并行计算；多速率；硬件加速；仿真平台

## Key Technologies and Prospects for Electromagnetic Transient Parallel Simulation in New Power Systems
JIANG Yibao, YU Jiale, ZHAO Haoran, LI Bing, HAN Mingzhe, ZHAO Changwang
(School of Electrical Engineering, Shandong University, Jinan 250061, China)

**Abstract:** Driven by the strategic goals of “peak carbon emissions” and “carbon neutrality”, power system is transforming into a new power system marked by extensive integration of new energy sources and a significant presence of power electronic devices. This transformation induces significant changes in its power source structure, and operational characteristics. Electromagnetic transient simulation, possessing the capability to comprehensively and precisely depict the high-frequency dynamic traits of the power system, has become a pivotal tool for understanding the operational features of the new power system. However, electromagnetic transient simulation techniques under the traditional serial computing mode is inadequate in addressing the simulation scenarios involving the large-scale integration of new energy sources and the complex coupling of AC and DC systems. Urgent research is needed to explore efficient parallel algorithms and hardware acceleration perspectives for electromagnetic transient simulation in a parallel computing mode. To this end, this paper first outlines the new demands of the new power system for electromagnetic transient simulation. It then introduces parallel algorithms for electromagnetic transient simulation, followed by a presentation of multi-rate simulation methods to further enhance efficiency, and introduces parallel simulation implementation schemes based on parallel computing devices. Finally, it reviews the parallel strategies of electromagnetic transient simulation platforms domestically and internationally, concludes that a simulation platform with deep integration of algorithm and hardware is the future direction, and also provides an analysis and outlook on key technologies involved.
**Key words:** new power system; electromagnetic transient; parallel computing; multi-rate; hardware acceleration; simulation platform

基金资助项目：国家自然科学基金(52307112)；山东省自然科学基金(ZR2023QE204)。
Project supported by National Natural Science Foundation of China (52307112), Shandong Provincial Natural Science Foundation (ZR2023QE204).

## 0 引言
构建新型电力系统，是贯彻落实我国能源安全新战略、实现“双碳”目标的重要途径。伴随着新型电力系统建设的不断进行，电力系统在源网荷储各环节呈现出高比例电子电子化和高比例新能源趋势，使得电力系统具有越来越明显的低惯性，强不确定性、弱抗扰性等特征[1]。相较于传统电力系统，新型电力系统的平衡与稳定将更加难以保证，开展大量仿真研究已成为推进新型电力系统建设的必要手段。但大量电力电子设备微秒级的开关动作和交流系统毫秒级的过渡过程相互影响，使得电力系统呈现出多时间尺度的宽频特征，机电暂态仿真由于仅考虑电气量的基波分量，无法反映系统中的高频动态，因而难以满足新型电力系统精确仿真的需求；而电磁暂态仿真能够表征电力电子设备的高频开关过程和新型电力系统的复杂控制策略，因此成为当前的重要仿真手段[2]。

然而，在新型电力系统仿真时，传统电磁暂态仿真方法仍面临仿真效率不足的问题，原因可概括为如下 3 个方面[3]：首先，新型电力系统源网荷储各环节均引入了大量电力电子设备，为准确模拟电力系统高频动态特性，需要纳秒级或亚微秒级的仿真步长；其次，伴随着多区域交直流电网混联和高比例新能源并网的不断推进，电力系统节点数目大幅增加，导致系统方程维数骤增；最后，新型电力系统中接入了大量复杂电气设备(分布式电源、换流器等)，以模块化多电平换流器(modular multilevel converter，MMC)为例[4]，单个 MMC 可包含数百个开关器件，使得仿真面临海量开关状态判断困难、电气设备计算复杂度显著提升的问题。

因此，亟需建立面向新型电力系统的高效电磁暂态仿真方法。并行仿真技术作为提升计算效率的重要手段，正在与电磁暂态仿真方法相融合，成为新型电力系统仿真技术研究的重点[5]。近年来，该技术已在并行仿真算法和硬件实现方面得到了不断的发展与改进。在并行仿真算法层面[6]，可按需选取高精度或高效率的分网算法，进而满足交直流混联输电网络、新能源场站、有源配电网等多元场景下的分网需求；同时，还可通过多速率仿真设计进一步提升分网并行算法的效率。在硬件实现方面[7]，中央处理单元(central processing unit，CPU)、图形处理器单元(graphics processing unit，GPU)、现场可编程门列阵(field programmable gate arrays，FPGA)等并行计算设备高速发展，计算机运算速度不断提升，异构型硬件设计方案的不断出现，既为并行算法的高效实现提供了必要的硬件基础，又能够提供强大的算力支持，使得仿真超大规模新型电力系统的详细电磁暂态过程成为可能。

因此，本文旨在通过详细的论文综述，梳理国内外电磁暂态并行仿真技术的新进展。本文从新型电力系统对电磁暂态仿真的新需求出发，引出电磁暂态并行仿真技术；然后从分网并行算法、多速率仿真设计、硬件并行实现、并行仿真平台 4 个方面对电磁暂态并行仿真技术进行详细梳理，并总结其中可进一步研究的重点内容以供参考。

## 1 新型电力系统对电磁暂态仿真的新需求
伴随着新型电力系统的发展，电力系统在源网荷储各环节都经历了深刻的变化[8]，呈现图 1 所示的全景态势。在电源侧，风电、光伏等可再生能源将成为电量供应主体；在电网侧，特高压直流输电、柔性交直流输电技术将得到广泛应用，形成大规模交直流混联的网架结构；在负荷侧，以分布式发电设备、电动汽车为代表的电力电子类负荷将持续提升，配电网络结构将愈发复杂；在储能侧，多元化储能设备将配置于源网荷各环节。上述各方面的变化对电力系统的电磁暂态仿真提出了如下 3 个方面的新需求。

### 1.1 更高的仿真维度需求
为解决我国资源分布极不均衡的问题，我国电力行业制定了“西电东送、南北互供、全国联网”的电网发展战略，电力系统规模不断扩大[9]；同时，新能源成为新型电力系统装机主体，但其单机容量通常小于传统同步发电机组，还经常以分布式电源的形式接入，使得电力系统中新能源发电设备数量众多；此外，高压场景下电力电子设备常采用级联型拓扑，设备电路模型愈发复杂[10]。因而，相较于传统电力系统仿真，新型电力系统仿真面临着系统节点数目急剧增加、网络方程维数骤增的问题，对电磁暂态仿真的维度也提出了更高的需求。

### 1.2 更高的仿真精度需求
在进行电磁暂态仿真时，现有方法通常对复杂设备采用简化或等值模型，如大规模新能源场站仿真时通常采用聚合等值模型，开关设备仿真时采用平均值模型或开关函数模型。此种方法在电网级的仿真分析中能够满足仿真精度的要求，但是在考虑设备级运行状态的仿真中，该模型既无法反映新能源场站内部故障，也无法涵盖多元运行工况，使得仿真面临精度不高、应用场景受限、灵活性不足等问题[11]。近年来，在新型电力系统数字化、智能化转型需求下，基于详细模型实现大规模电网、新能源场站的电磁暂态仿真具有重要意义。因而，新型电力系统对电磁暂态仿真的仿真精度提出了更高的要求。

### 1.3 更高的仿真速度需求
一方面，新型电力系统中电力电子设备高频的开关动作、复杂的控制策略和拓扑结构严重制约了电磁暂态仿真速度的提升，采用传统的电磁暂态仿真方法仿真新型电力系统的时间成本高，已难以满足科研和实际工程的需求。另一方面，在大规模新型电力系统背景下，硬件在环技术缩短研发周期、降低仿真成本、提升仿真结果可靠性的优势愈发明显，因而得到了广泛的研究与应用[12]，但硬件在环技术要求具有与实物严格同步的能力，必须采用对算法和硬件要求都较高实时仿真[13]。综上，新型电力系统对电磁暂态的仿真速度提出了更高的要求。

针对以上 3 方面的需求，电磁暂态并行仿真技术提供了有效的解决和缓解方法：对于高仿真维度需求，其能够实现高维矩阵的降维求解；对于高仿真精度需求，其能够支持详细模型的高效计算；对于高仿真速度需求，其能够通过并行架构大幅缩短仿真时间。图 2 展示了电力系统电磁暂态并行仿真技术的整体框架。

> 图 1 新型电力系统全景态势
> Fig.1 Comprehensive overview of new power system

> 图 2 电力系统电磁暂态并行仿真技术
> Fig.2 Parallel simulation technology for electromagnetic transients in power system

## 2 电磁暂态仿真的分网并行算法
新型电力系统中交直流电网节点数目庞大且构成复杂，在传统交流电网的基础上，融合了柔性交流输电、柔性直流输电、新能源发电等多类电力电子设备，导致网络方程高阶并呈现快速时变特征，难以进行快速求解。借助于电磁暂态仿真的分网并行算法，能够实现复杂电气设备或新型电力系统状态方程的降维与并行求解，从而显著提升电力系统的仿真效率。其基本思想经抽象总结，可概括为如图 3 所示的 3 个环节。首先，选择合适的分网元件，将复杂电气设备或大规模电力系统分