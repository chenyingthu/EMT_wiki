## 含 VSC-HVDC 交直流系统多尺度暂态建模与仿真研究
叶华 1，安婷 2，裴玮 1，韩丛达 2，齐智平 1
(1．中国科学院电工研究所，北京市 海淀区 100190；2．全球能源互联网研究院，北京市 昌平区 102211)

## Multi-scale Modeling and Simulation of Transients for VSC-HVDC and AC Systems
YE Hua1, AN Ting2, PEI Wei1, HAN Congda2, QI Zhiping1
(1. Institute of Electrical Engineering, Chinese Academy of Sciences, Haidian District, Beijing 100190, China; 2. Global Energy Interconnection Research Institute, Changping District, Beijing 102211, China)

**ABSTRACT:** To meet the needs of accurate, fast and flexible simulation of electromagnetic and electromechanical transients in AC/DC systems, methods such as shifted-frequency analysis were developed for multi-scale modeling of voltage source converter-based high voltage direct current (VSC-HVDC)-embedded AC system. The shifted-frequency method uses the Hilbert transform, and then removes or retains the carrier at power-frequency to track slow or fast-changing transients, respectively. A shifted-frequency- based VSC model was first established, mathematical relationships of transforming the SFA-domain and $dq$-domain quantities were derived, then selective insertion of a $\pi$-segment leaded to a multi-scale model of DC line, and finally a multi-scale model of VSC-HVDC/AC systems was constructed. By adjusting simulation parameters such as time-step sizes, diverse transients with multiple time-scales and in different network positions can be simulated. The simulation results show that multi-time-scale transients can be simulated accurately in which the computational cost is reduced significantly. In addition, the flexibility of simulating electromagnetic and electromechanical transients in AC/DC systems is enhanced.

**KEY WORDS:** voltage source converter-based high voltage direct current (VSC-HVDC); multi-scale transient model; shifted-frequency analysis; electromagnetic transients; electromechanical transients; Hilbert transform

**摘要：** 为满足对交直流系统电磁–机电暂态特性准确、快速和灵活仿真的需要，提出基于移频分析等方法的含柔性高压直流(voltage source converter-based high voltage direct current，VSC-HVDC)输电交直流电力系统多尺度暂态模型。移频分析法采用希尔伯特变换，通过移除或保留交流信号基频载波实现慢–快变化暂态的模拟。该文建立了 VSC 移频相量模型，推导出 VSC 移频域与其控制系统 $dq$ 域的转换关系，选择性插入 $\pi$ 模型获得直流输电线多尺度暂态模型，进而构建了全系统多尺度暂态模型。该模型通过设置仿真参数(如时间步长)能够满足不同时间、不同电网位置电磁或机电暂态仿真的需求。仿真结果表明，所提模型不仅准确描述了 VSC-HVDC 多尺度暂态过程，节省了计算时间，而且增强了交直流系统电磁–机电暂态混合仿真的灵活性。

**关键词：** 柔性直流输电；多尺度暂态模型；移频分析；电磁暂态；机电暂态；希尔伯特变换

**基金项目：** 国家电网公司“千人计划”科技专项(SGRIzlsdgcjsyjs JS [2014]264)。
State Grid Corporation of China Through the 1000-Plan Project (SGRIzlsdgcjsyjs JS [2014]264).

## 0 引言
柔性高压直流输电(voltage source converter based-high voltage direct current，VSC-HVDC)因具备独立控制有功无功、易实现多端直流(multi-terminal DC，MTDC)输电等特征，将被广泛应用于工程实际[1]。为适用于高压远距离大容量柔性直流输电，基于模块化多电平换流器(modular multilevel converter，MMC)的多端直流输电或直流电网已成为当前研究热点[1-2]。

为准确、快速分析 VSC-HVDC 复杂暂态特性及其与交流系统相互影响，合理设计控制器，保证交直流电网安全稳定运行，有必要开展含 VSC-HVDC 交直流系统的电磁与机电暂态仿真[3-4]。电磁暂态程序(electromagnetic transients program，EMTP)被广泛用于非线性元件高频暂态仿真，但其易受电网规模、仿真速度等方面的限制[5]。为加快电力电子开关特性仿真速度，通常基于换流器平均值模型(averaged-value model，AVM)构建柔性直流输电系统等效模型[6-8]，该模型仍属于电磁暂态模型的范畴。另一方面，机电暂态稳定程序(如 PSS/E)关注电力系统慢变化低频暂态过程，通常忽略电力电子高频暂态特性[9]。该类程序算法难以精确模拟 VSC 等非线性系统的暂态特性，并且在模拟换流器交流侧不对称故障、高频谐波等方面存在一定不足[10-11]。

为准确模拟直流系统高频暂态并提高交流系统暂态稳定仿真速度，国内外学者针对传统直流输电(line-commutated converter，LCC-HVDC)的电磁–机电混合仿真开展了大量工作[12-15]。文献[16]借鉴上述工作提出了柔性直流输电系统的电磁–机电混合仿真算法并给出几种接口方案。联合两类程序因两者建模机理不同会面临接口复杂、数据交换繁琐、仿真灵活性差等问题。

近年来，动态相量(dynamic phasor)理论被应用于含 LCC-HVDC 或 VSC-HVDC 交直流系统电磁–机电暂态建模与仿真中[17-20]。动态相量理论基于时变傅里叶变换，根据研究目的选择不同频段进行暂态建模。采用高阶傅里叶系数模拟详细的电磁暂态过程，但阶数对应的方程数目增多会影响计算速度，对于在仿真进程中确定时变的主导频率也较为困难。另外，动态相量模型不能完全有效仿真交流电经 VSC-HVDC 并网多尺度暂态现象如风功率波动期间发生的不对称故障等，并将其用于 CIGRE B4 多端直流测试系统电磁–机电暂态混合仿真。通过与电磁暂态模型仿真结果比较，验证所提模型的准确性、有效性和灵活性。

## 1 柔性直流输电系统动态平均值模型
为阐述方便，下文柔性直流输电系统中 AC/DC 换流器指两电平、三电平 VSC 或 MMC-VSC。为提高计算效率，通常忽略电力电子元件物理特性，采用平均值方法建立换流器等效 AVM 如图 1 所示[6-8]。该模型处理时域瞬时值，交流侧电压和电流在稳态时表现为基频正弦波。

**图1 换流器动态平均值模型及其控制系统**
**Fig. 1 Dynamic AVM of typical converters and corresponding control system**

*(图中标注组件：受控直流源, $i_a$, $u_{aN}$, $i_b$, $i_{dc}$, 控制信号, $u_{dc}$, $u_{bN}$, $i_c$, 受控电压源, $u_{cN}$, 交流电力系统, $u_{abc}$, $i_{abc}$, $m_{dq}$, $P$, $u_{dc}$, 锁相环, 内环与外环控制器, $u_{dq}$, $i_{dq}$, $Q$, Park 变换)*

由图 1 可见，换流器交流侧等效为三相受控电压源...