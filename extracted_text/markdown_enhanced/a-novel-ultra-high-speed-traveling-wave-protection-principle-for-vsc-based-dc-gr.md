Received July 26, 2019, accepted August 15, 2019, date of publication August 19, 2019, date of current version September 6, 2019.
Digital Object Identifier 10.1109/ACCESS.2019.2936276

# A Novel Ultra-High-Speed Traveling-Wave Protection Principle for VSC-based DC Grids

XIANGYU PEI$^1$, HUI PANG$^2$, YUNFENG LI$^3$, LONGLONG CHEN$^2$, XIAO DING$^2$, AND GUANGFU TANG$^2$, (Member, IEEE)

$^1$ School of Electrical and Information Engineering (Hunan Province Key Laboratory of Smart Grids Operation and Control), Changsha University of Science and Technology, Changsha 410114, China
$^2$ Global Energy Interconnection Research Institute Company Ltd., State Key Laboratory of Advanced Power Transmission Technology, Beijing 102209, China
$^3$ State Grid Hunan Electric Power Company Limited Economic and Technical Research Institute, Changsha 410004, China

Corresponding author: Xiangyu Pei (646888200@qq.com)

This work was supported by the National Key Research and Development Program of China under Grant 2017YFB0902400.

**ABSTRACT** Protection of direct current (DC) transmission lines is one of the key difficulties to be urgently solved in the construction of the future voltage-sourced converter (VSC)-based DC grids. In this paper, a novel ultra-high-speed traveling-wave (TW) protection principle for DC transmission lines is proposed which is based on characteristics of modulus voltage TWs. First, the absolute value of the change in amplitude of the 1-mode voltage TW is used to construct the protection starting-up element. Then, the dyadic wavelet transform is utilized to extract the wavelet-transform modulus maxima (WTMM) of 1-mode and 0-mode initial reverse voltage TWs separately, which are used for fault section identification and selection of fault line successively. A four-terminal annular VSC-based DC grid electromagnetic transient model is established in PSCAD/EMTDC, and performance of the proposed novel ultra-high-speed TW protection principle is evaluated. Extensive simulation results under different fault conditions show that the proposed ultra-high-speed TW protection principle is excellent in rapidity, reliability and robustness. Therefore, the proposed novel ultra-high-speed TW protection principle in this paper can be adopted as an outstanding main protection for VSC-based DC grids.

**INDEX TERMS** VSC-based DC grid, traveling-wave protection, modulus traveling-wave voltage, wavelet transform modulus maximum, main protection.

## I. INTRODUCTION

The voltage-sourced converter (VSC)-based direct current (DC) grid is a feasible solution to realize wide-area complementarity and flexible consumption of large-scale renewable clean energy, and as a result has bright future and important application value [1], [2]. However, VSC-based DC girds are “low damping” systems when compared with traditional alternating current (AC) systems, and as a result the phenomenon that a local fault cause the whole DC gird breakdown is more likely to occur [3]. Moreover, a higher probability of temporary faults will inevitably appear because of the application of overhead transmission lines (OHLs) in complex environments [4], [5]. Consequently, ultra-high-speed protection for DC transmission lines is one of the key difficulties to be urgently solved in the construction of the future VSC-based DC grids.

The “low damping” characteristic puts forward severe requirements for the action speed of line protection in VSC-based DC grids [6]. Therefore, the main protection should be based on non-unit protection principles so as to realize a faster action speed [7]–[11]. On basis of the propagation characteristics of aerial-mode voltage traveling waves in the MMC-MTDC grid, a novel non-unit faulty line identification principle based on the aerial-mode voltage on the current-limiting inductor at the line terminal is proposed in [12]. With the current-limiting inductor as the protection boundary, the non-unit line protection based on the wavelet transform modulus maximum value is constructed by analyzing the difference of the amplitude-frequency characteristics of aerial-mode voltage transfer functions between internal and external faults, and the fault-pole identification is designed. Based on the supplemental inductor placed at each end of the dc line, a new non-unit protection scheme for dc line in multi-terminal VSC-HVDC system is proposed in [13]. The supplemental inductor acts as a boundary of DC line and provides a high impedance path for the high-frequency component, with the obvious difference in the ratio of the transient voltages at both sides of the inductor during DC line fault and external fault, fault identification is realized. Based on analysis of features of fault-induced travelling waves (TWs) after DC line fault, two ultra-high-speed TW protection principles for transmission lines of VSC-HVDC systems are proposed in [14], [15]. Both non-unit protection principles are achieved by characteristics of 0-mode and 1-mode TWs. However, the above mentioned non-unit protection principles will show poor reliability when suffered from interferences.

A novel ultra-high-speed TW protection principle for VSC-based DC girds is proposed in this paper. Firstly, modulus directional voltage TWs are introduced. Then, based on their characteristics, the corresponding detail criteria consisting of protection starting-up, fault-section identification and fault-pole selection are designed successively.

The structure of this paper is organized as follows. The basic configuration and parameters of Zhangbei ±500 kV VSC-based DC grid is described in Section 2, which is the technical background of this paper. In Section 3, directional voltage TWs, phase-mode transformation and wavelet analysis theory are separately introduced. In Section 4, the detailed ultra-high-speed TW protection principle is presented. In Section 5, extensive simulations under different fault conditions are carried out to assess the performance of the proposed ultra-high-speed TW protection principle. Finally, some con-

**TABLE 1.** Main parameters of Zhangbei ± 500 kV VSC-based DC grid.
*(Table data not provided in source excerpt)*

**TABLE 2.** Length of each OHL.
*(Table data not provided in source excerpt)*