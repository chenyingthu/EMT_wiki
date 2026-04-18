Received July 26, 2019, accepted August 15, 2019, date of publication August 19, 2019, date of current version September 6, 2019. Digital Object Identifier 10.1109/ACCESS.2019.2936276

# A Novel Ultra-High-Speed Traveling-Wave Protection Principle for VSC-based DC Grids

XIANGYU PEI 1, HUI PANG2, YUNFENG LI 3, LONGLONG CHEN2, XIAO DING2, AND GUANGFU TANG2, (Member, IEEE)

1School of Electrical and Information Engineering (Hunan Province Key Laboratory of Smart Grids Operation and Control), Changsha University of Science and Technology, Changsha 410114, China

2Global Energy Interconnection Research Institute Company Ltd., State Key Laboratory of Advanced Power Transmission Technology, Beijing 102209, China   
3State Grid Hunan Electric Power Company Limited Economic and Technical Research Institute, Changsha 410004, China

Corresponding author: Xiangyu Pei (646888200@qq.com)

This work was supported by the National Key Research and Development Program of China under Grant 2017YFB0902400.

ABSTRACT Protection of direct current (DC) transmission lines is one of the key difficulties to be urgently solved in the construction of the future voltage-sourced converter (VSC)-based DC grids. In this paper, a novel ultra-high-speed traveling-wave (TW) protection principle for DC transmission lines is proposed which is based on characteristics of modulus voltage TWs. First, the absolute value of the change in amplitude of the 1-mode voltage TW is used to construct the protection starting-up element. Then, the dyadic wavelet transform is utilized to extract the wavelet-transform modulus maxima (WTMM) of 1-mode and 0-mode initial reverse voltage TWs separately, which are used for fault section identification and selection of fault line successively. A four-terminal annular VSC-based DC grid electromagnetic transient model is established in PSCAD/EMTDC, and performance of the proposed novel ultra-high-speed TW protection principle is evaluated. Extensive simulation results under different fault conditions show that the proposed ultra-high-speed TW protection principle is excellent in rapidity, reliability and robustness. Therefore, the proposed novel ultra-high-speed TW protection principle in this paper can be adopted as an outstanding main protection for VSC-based DC grids.

INDEX TERMS VSC-based DC grid, traveling-wave protection, modulus traveling-wave voltage, wavelet transform modulus maximum, main protection.

## I. INTRODUCTION

The voltage-sourced converter (VSC)-based direct current (DC) grid is a feasible solution to realize wide-area complementarity and flexible consumption of large-scale renewable clean energy, and as a result has bright future and important application value [1], [2]. However, VSC-based DC girds are ‘‘low damping’’ systems when compared with traditional alternating current (AC) systems, and as a result the phenomenon that a local fault cause the whole DC gird breakdown is more likely to occur [3]. Moreover, a higher probability of temporary faults will inevitably appear because of the application of overhead transmission lines (OHLs) in complex environments [4], [5]. Consequently, ultra-highspeed protection for DC transmission lines is one of the key difficulties to be urgently solved in the construction of the future VSC-based DC grids.

The ‘‘low damping’’ characteristic puts forward severe requirements for the action speed of line protection in VSCbased DC grids [6]. Therefore, the main protection should be based on non-unit protection principles so as to realize a faster action speed [7]–[11]. On basis of the propagation characteristics of aerial-mode voltage traveling waves in the MMC-MTDC grid, a novel non-unit faulty line identification principle based on the aerial-mode voltage on the currentlimiting inductor at the line terminal is proposed in [12]. With the current-limiting inductor as the protection boundary, the non-unit line protection based on the wavelet transform modulus maximum value is constructed by analyzing the difference of the amplitude-frequency characteristics of aerialmode voltage transfer functions between internal and external faults, and the fault-pole identification is designed. Based on the supplemental inductor placed at each end of the dc line, a new non-unit protection scheme for dc line in multi-terminal VSC-HVDC system is proposed in [13]. The supplemental inductor acts as a boundary of DC line and provides a high impedance path for the high-frequency component, with the obvious difference in the ratio of the transient voltages at both sides of the inductor during DC line fault and external fault, fault identification is realized. Based on analysis of features of fault-induced travelling waves (TWs) after DC line fault, two ultra-high-speed TW protection principles for transmission lines of VSC-HVDC systems are proposed in [14], [15]. Both non-unit protection principles are achieved by characteristics of 0-mode and 1-mode TWs. However, the above mentioned non-unit protection principles will show poor reliability when suffered from interferences.

A novel ultra-high-speed TW protection principle for VSC-based DC girds is proposed in this paper. Firstly, modulus directional voltage TWs are introduced. Then, based on their characteristics, the corresponding detail criteria consisting of protection starting-up, fault-section identification and fault-pole selection are designed successively.

The structure of this paper is organized as follows. The basic configuration and parameters of Zhangbei ±500 kV VSC-based DC grid is described in Section 2, which is the technical background of this paper. In Section 3, directional voltage TWs, phase-mode transformation and wavelet analysis theory are separately introduced. In Section 4, the detailed ultra-high-speed TW protection principle is presented. In Section 5, extensive simulations under different fault conditions are carried out to assess the performance of the proposed ultra-high-speed TW protection principle. Finally, some conclusions are drawn in Section 6.

## II. ZHANGBEI 500 KV VSC-BASED DC GRID

Zhangbei is located in Hebei province of China, which is one of the abundant areas of renewable clean energy resources including wind energy, solar energy, and hydroelectric power. It is estimated that the total installed capacity of renewable clean energy resources in this area will increase to 20 GW by 2020 [16]–[19].

To solve the integration and transmission of large-scale renewable clean energy resources in this area, a four-terminal annular bipolar VSC-based DC gird demonstration project of which the rated voltage is ±500 kV will be constructed around the end of 2019. As shown in Fig. 1, Kangbao (KB) and Zhangbei (ZB) converter stations are used to integrate local wind energy into the DC gird and send the renewable energy to Beijing (BJ) converter station. Besides, a pumped storage power station is integrated to Fengning (FN) converter station for participating the power dispatch and suppressing the power fluctuation. In this demonstration project, OHLs and DC breakers (DBs) chosen as the primary scheme. In addition, the values of DC reactors are all 150 mH. Main parameters and length of each OHL are listed in Table I and Table II respectively.

![](images/1ba9c6283a47b02b1c3d8618e3cfc11d3d1e5260904813b767f005d6e0191795.jpg)  
FIGURE 1. Zhangbei ± 500 kV VSC-based DC grid.

TABLE 1. Main parameters of Zhangbei ± 500 kV VSC-based DC grid.
<table><tr><td>Items</td><td>KB</td><td>ZB</td><td>FN</td><td>BJ</td></tr><tr><td>DC rated voltage/kV</td><td>±500</td><td>±500</td><td>±500</td><td>±500</td></tr><tr><td>Control mode</td><td>P/Q</td><td>P/Q</td><td>Vdc/Q</td><td>P/Q</td></tr><tr><td>AC rated voltage/kV</td><td>220</td><td>220</td><td>500</td><td>500</td></tr><tr><td>Transformer ratio</td><td>220/275</td><td>220/275</td><td>500/275</td><td>500/275</td></tr><tr><td>Rated power/MW</td><td>1500</td><td>3000</td><td>1500</td><td>3000</td></tr><tr><td>Number of SMs per arm/N</td><td>264</td><td>264</td><td>264</td><td>264</td></tr><tr><td>Redundancy</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td></tr><tr><td>SM capacitance/mF</td><td>9</td><td>15</td><td>9</td><td>15</td></tr><tr><td>Arm inductance/mH</td><td>100</td><td>50</td><td>100</td><td>50</td></tr></table>

TABLE 2. Length of each OHL.
<table><tr><td>Items</td><td> $\overline { { \mathrm { \ O H L } _ { 1 2 } } }$ </td><td> $\overline { { \mathrm { O H L } _ { 1 3 } } }$ </td><td> $\overline { { \mathrm { { O H L } } _ { 2 4 } } }$ </td><td>OHL34</td></tr><tr><td>Length/km</td><td>50</td><td>205</td><td>206</td><td>187</td></tr></table>

![](images/11f4084f62f2bcc079a1cd5fe815399c6b6e92f2a8f4cd1897c5de189e3f4cc8.jpg)  
FIGURE 2. Equivalent circuit of a transmission line unit.

## III. BASIC PRINCIPLES

## A. DIRECTIONAL VOLTAGE TRAVELING WAVES

As shown in Fig. 2, in the equivalent circuit of a lossy uniform transmission line unit with length 1x, r0, g0, l0 and c0 are the distributed resistance (/m), conductance (S/m), inductance (H/m), and capacitance (F/m) in per unit length respectively. According to Kirchhoff’s laws, the following wave equations can be satisfied for this transmission line unit [20].

$$
\left\{ \begin{array} { l l } { - \displaystyle \frac { \partial u ( x , t ) } { \partial x } = r _ { 0 } i ( x , t ) + l _ { 0 } \displaystyle \frac { \partial i ( x , t ) } { \partial t } } \\ { - \displaystyle \frac { \partial i ( x , t ) } { \partial x } = g _ { 0 } u ( x , t ) + c _ { 0 } \displaystyle \frac { \partial u ( x , t ) } { \partial t } } \end{array} \right.\tag{1}
$$

Solving (1), the general solution can be given as:

$$
\left\{ \begin{array} { l l } { \displaystyle U ( x , t ) = u _ { f } ( x , t ) e ^ { - \gamma x } + u _ { r } ( x , \omega ) e ^ { \gamma x } } \\ { \displaystyle I ( x , t ) = \frac { 1 } { Z _ { c } } ( u _ { f } ( x , t ) e ^ { - \gamma x } - u _ { r } ( x , t ) e ^ { \gamma x } ) } \end{array} \right.\tag{2}
$$

Based on (2), directional voltage TWs can be shown as:

$$
\left\{ \begin{array} { l } { { \displaystyle u _ { f } ( x , t ) = \frac { 1 } { 2 } \left[ U ( x , t ) + Z _ { c } I ( x , t ) \right] e ^ { \gamma x } } } \\ { { \displaystyle u _ { r } ( x , t ) = \frac { 1 } { 2 } \left[ U ( x , t ) - Z _ { c } I ( x , t ) \right] e ^ { - \gamma x } } } \end{array} \right.\tag{3}
$$

where $u _ { f } ( x , t )$ is the forward voltage TW (FVTW), $u _ { r } ( x , t )$ is the reverse voltage TW (RVTW). $Z _ { c }$ is the line characteristic impedance and $\gamma$ is the corresponding TW propagation coefficient respectively, which can be shown as in frequencydomain form:

$$
\left\{ \begin{array} { l l } { Z _ { c } = \sqrt { \displaystyle \frac { r _ { 0 } + j \omega l _ { 0 } } { g _ { 0 } + j \omega c _ { 0 } } } } \\ { \gamma = \sqrt { \left( r _ { 0 } + j \omega l _ { 0 } \right) \left( g _ { 0 } + j \omega c _ { 0 } \right) } } \end{array} \right.\tag{4}
$$

## B. PHASE-MODE TRANSFORMATION

For a bipolar VSC-based DC grid, (1) can be rewritten as the following wave equations with mutual coupling [21]:

$$
\left\{ \begin{array} { l l } { \displaystyle { \frac { \partial { \pmb u } } { \partial x } } = - { \pmb R i } - { \pmb L } \displaystyle { \frac { \partial { \pmb u } } { \partial t } } } \\ { \displaystyle { \frac { \partial { \pmb i } } { \partial x } } = - { \pmb G } { \pmb u } - { \pmb C } \displaystyle { \frac { \partial { \pmb u } } { \partial t } } } \end{array} \right.\tag{5}
$$

where

$$
\begin{array} { r l } { \boldsymbol { u } = \left[ \begin{array} { l } { u _ { p } } \\ { u _ { n } } \end{array} \right] } & { { } i = \left[ \begin{array} { l } { i _ { p } } \\ { i _ { n } } \end{array} \right] } \\ { \boldsymbol { R } = \left[ \begin{array} { l l } { R _ { s } } & { R _ { m } } \\ { R _ { m } } & { R _ { s } } \end{array} \right] } & { { } \boldsymbol { L } = \left[ \begin{array} { l l } { L _ { s } } & { L _ { m } } \\ { L _ { m } } & { L _ { s } } \end{array} \right] } \\ { \boldsymbol { G } = \left[ \begin{array} { l l } { G _ { s } } & { G _ { m } } \\ { G _ { m } } & { G _ { s } } \end{array} \right] } & { { } \boldsymbol { C } = \left[ \begin{array} { l l } { C _ { s } } & { C _ { m } } \\ { C _ { m } } & { C _ { s } } \end{array} \right] } \end{array}
$$

$u _ { p }$ and $i _ { p }$ are voltage and current of the positive-pole line, $u _ { n }$ and $i _ { n }$ are voltage and current of the negative-pole line, $R _ { s } , L _ { s } , G _ { s }$ and $C _ { s }$ are self-resistance, self-inductance, selfconductance and self-capacitance, $R _ { m } , L _ { m } , G _ { m }$ and $C _ { m }$ are mutual-resistance, mutual-inductance, mutual-conductance and mutual-capacitance, respectively.

A phase-mode transformation matrix can be shown as:

$$
S = \frac { 1 } { \sqrt { 2 } } \left[ \begin{array} { c c } { 1 } & { 1 } \\ { - 1 } & { 1 } \end{array} \right]\tag{6}
$$

The following decoupling transformation can be applied to (5) with this matrix:

$$
\left\{ \begin{array} { l l } { \displaystyle { \frac { \partial { \pmb u } _ { \mathrm { m } } } { \partial x } } = - S ^ { - 1 } { \pmb R } S i _ { \mathrm { m } } - S ^ { - 1 } { \pmb L } S \displaystyle { \frac { \partial { \pmb i } _ { \mathrm { m } } } { \partial t } } } \\ { \displaystyle { \frac { \partial { \pmb i } _ { \mathrm { m } } } { \partial x } } = - S ^ { - 1 } { \pmb G } S { \pmb u } _ { \mathrm { m } } - S ^ { - 1 } { \pmb C } S \displaystyle { \frac { \partial { \pmb u } _ { \mathrm { m } } } { \partial t } } } \end{array} \right.\tag{7}
$$

where

$$
\begin{array}{c} \begin{array}{c} \begin{array}{c} \begin{array} { c } { { \begin{array} { c c } { { \displaystyle { u _ { \mathrm { m } } } = S ^ { - 1 } { u } = [ { u _ { 1 } } ] } } \\ { { \displaystyle { } } } \\ { { S ^ { - 1 } R S = [ { R _ { 1 } } ] = [ { R _ { s } } - { R _ { m } } } \\ { { 0 } } \end{array} } } \\ { { \begin{array} { c c } { { S ^ { - 1 } L S = [ { L _ { 1 } } ] = [ { L _ { s } } - { L _ { m } } } \\ { { 0 } } \end{array} } } \\ { { \begin{array} { c c } { { S ^ { - 1 } L S = [ { L _ { 0 } } ] = [ { L _ { 0 } } } \\ { { 0 } } \end{array} } } \end{array} } } \\ { { \begin{array} { c c } { { S ^ { - 1 } G S = [ { G _ { 1 } } ] } } \\ { { G _ { 0 } } } \end{array} } } \end{array} }  \end{array}   \\ { { { \begin{array} { c c } { { { } } } } \\ { { { S ^ { - 1 } G S = [ { G _ { 0 } } ] = [ { G _ { 0 } } + 2 { G _ { m } } } } } & { { { 0 } } \\ { { 0 } } } \end{array} ] } } \end{array}
$$

![](images/6ea7cb320e15d2e4d9761f461ca4f21ff7d5b599837d239e3a1b206fbc627a60.jpg)  
FIGURE 3. Wavelet Transformation Multi-resolution Analysis.

$$
S ^ { - 1 } C S = \binom { C _ { 1 } } { C _ { 0 } } = \left[ \begin{array} { c c } { { C _ { 0 } + 2 C _ { m } } } & { { 0 } } \\ { { 0 } } & { { C _ { 0 } } } \end{array} \right]
$$

$u _ { 1 }$ and $i _ { 1 }$ are the voltage and current of the 1-mode TWs, u0 and $i _ { 0 }$ are the voltage and current of the 0-mode TWs, $R _ { i } , G _ { i } ,$ $L _ { i } .$ , and $C _ { i }$ are the corresponding i-mode $( i = 0 , 1 )$ resistance, conductance, inductance and capacitance, respectively.

## C. WAVELET ANALYSIS THEORY

The wavelet transformation is a powerful tool to detect the local singularity in transient signals, and as a result it has been widely utilized to extract and analyze characteristics of nonstationary high-frequency fault TW signals [22]. When the dyadic wavelet transform (DWT) is applied to a given discrete signal $f _ { 0 } ( n )$ , the corresponding low-frequency approximation coefficients $A _ { 2 ^ { j } } f _ { 0 } ( n )$ and high-frequency detail coefficients $W _ { 2 ^ { j } } f _ { 0 } ( n )$ in scale $2 ^ { j }$ can be calculated as:

$$
\left\{ \begin{array} { l l } { { A _ { 2 ^ { j } } f _ { 0 } ( n ) = \displaystyle \sum _ { k } h _ { k } A _ { 2 ^ { j - 1 } } f _ { 0 } ( n - 2 ^ { j - 1 } k ) } } \\ { { W _ { 2 ^ { j } } f _ { 0 } ( n ) = \displaystyle \sum _ { k } g _ { k } A _ { 2 ^ { j - 1 } } f _ { 0 } ( n - 2 ^ { j - 1 } k ) } } \end{array} \right.\tag{8}
$$

where $h _ { k }$ and $g _ { k }$ are the low-pass and high-pass filter coefficients, respectively.

Based on (8), for a given discrete signal whose frequencies range from 0 to $f _ { n } ,$ wavelet transformation multi-resolution analysis shown in Fig. 3 can be realized.

The local maximum of high-frequency detail coefficients can be defined as the wavelet transform modulus maxima (WTMM), which has been widely used to describe the local singularity of a transient signal [23]. Therefore, WTMM is utilized to analyze the wave-fronts’ characteristics of directional voltage TWs in this paper.

## IV. PROTECTION SCHEME

## A. PROTECTION STARTING-UP ELEMENT

The absolute value of the change in amplitude of 1-mode voltage TW can be defined as:

$$
\Delta u _ { 1 } ( k ) = | u _ { 1 } ( k ) - u _ { 1 } ( k - 1 ) |\tag{9}
$$

where $u _ { 1 } ( k )$ is the sampling 1-mode voltage TW value at present time, and $u _ { 1 } ( k - 1 )$ denotes the 1-mode voltage TW value of the previous time.

When the VSC-based DC grid is in normal operation, $\Delta u _ { 1 } ( k )$ nearly equals to 0. However, once there is a failure on the DC transmission line, a sharp change will occur in the 1-mode voltage TW $u _ { 1 }$ , and as a result the corresponding $\Delta u _ { 1 } ( k )$ will increases drastically. Therefore, the protection starting-up element can be designed as:

$$
\Delta u _ { 1 } ( k ) > \mathrm { T H } _ { 1 }\tag{10}
$$

![](images/dd3932cb242979b500d9b09a6e14989bb6674048e8e43d60c650a844ddf0ba5b.jpg)

FIGURE 4. Schematic diagram of the fault section.  
![](images/2fef3def30be210fbde4d1085bba71e2bd524ae0157f0d4d37182cd672104f13.jpg)  
FIGURE 5. Peterson equivalent circuit.

where $\mathrm { T H } _ { 1 }$ is the threshold value for the protection startingup element, which can be set as 0.01 p.u. of the DC rated voltage.

To guarantee the reliability, if three consecutive values $\Delta u _ { 1 } ( k )$ ， $\Delta u _ { 1 } ( k + 1 )$ and $\Delta u _ { 1 } ( k + 2 )$ exceed the threshold value TH1, a protection starting-up signal will be given out.

## B. FAULT-SECTION IDENTIFICATION

As shown in Fig. 4, fault f belongs to an external fault for OH $- \boldsymbol { \mathrm { n } } \boldsymbol { \cdot }$ while it is an internal fault for $\mathrm { O H L } _ { \mathrm { m } }$

When a failure occurs on ${ \mathrm { O H L } } _ { \mathrm { m } } .$ , the corresponding Peterson equivalent circuit is shown in Fig. 5, where $C _ { \mathrm { e q } } , L _ { \mathrm { e q } }$ and $R _ { \mathrm { e q } }$ are the equivalent capacitance, inductance and resistance of the MMC before blocking respectively.

Based on the Peterson equivalent circuit shown in Fig. 5, the complex frequency-domain forms of $u _ { \mathrm { m } } , u _ { \mathrm { n } } , i _ { \mathrm { m } }$ and $i _ { \mathrm { n } }$ can be expressed as:

On basis of (3), (11) and (12), as shown at the bottom of this page, the RVTWs for both sections can be deduced as:

$$
\left\{ \begin{array} { l l } { \displaystyle U _ { \mathrm { m r } } ( s ) = - \frac { 1 } { s } } \\ { U _ { \mathrm { n r } } ( s ) = 0 } \end{array} \right.\tag{13}
$$

where $U _ { \mathrm { m r } } ( \mathbf { s } )$ is the RVTW for the internal section, and $U _ { \mathrm { n r } } ( \mathbf { s } )$ is the RVTW for the external section.

Based on (13), the initial RVTWs in both sections are independent of $Z _ { \mathrm { c } } , \ L _ { \mathrm { d c } } , \ C _ { \mathrm { e q } } , \ L _ { \mathrm { e q } }$ and $R _ { \mathrm { e q } }$ . Moreover, the time-domain form of $U _ { \mathrm { m r } } ( \mathbf { s } )$ is a step signal with negative polarity, while that of $U _ { \mathrm { n r } } ( { \bf s } )$ is 0. Therefore, the WTMM of the 1-mode initial RVTW can be extracted and used for faultsection identification, and the corresponding criterion can be designed as:

![](images/d438f3e8bf3498838f1e9a842463a133d3b86e8f7921426ccffe93bcf0146d1c.jpg)  
FIGURE 6. Positive pole-to-ground fault.

$$
f = \left\{ \begin{array} { l l } { \mathrm { i n t e r n a l ~ f a u l t , } } & { \left| \mathrm { W T M M } _ { u _ { 1 r } } \right| > \mathrm { T H } _ { 2 } } \\ { \mathrm { e x t e r n a l ~ f a u l t , } } & { \mathrm { o t h e r s } } \end{array} \right.\tag{14}
$$

where $u _ { \mathrm { l r } }$ is the initial 1-mode RVTW, and $\mathrm { T H } _ { 2 }$ is the threshold value for fault section identification, respectively.

## C. FAULT-POLE SELECTION

For a bipolar VSC-based DC grid, when a failure occurs on the positive-pole transmission lines, the corresponding faultsuperimposed network can be revealed by Fig. 6.

As shown in Fig. 6, on basis of the fault-superimposed network, the following boundary conditions is satisfied:

$$
\left\{ \begin{array} { l l } { u _ { \mathrm { p } } = u _ { \mathrm { p f } } - 2 i _ { \mathrm { p } } R _ { \mathrm { f } } } \\ { u _ { \mathrm { p f } } = - U _ { \mathrm { d c } } } \\ { i _ { \mathrm { n } } = 0 } \end{array} \right.\tag{15}
$$

where $R _ { \mathrm { f } }$ is the fault transition resistance, and $u _ { \mathrm { p f } }$ is the additional DC voltage source, respectively.

Based on modulus resistances from phase-mode transformation, initial voltage TWs for both poles can be deduced as:

$$
\left\{ \begin{array} { l } { u _ { \mathrm { p } } = - \frac { U _ { \mathrm { d c } } ( Z _ { 0 } + Z _ { 1 } ) } { Z _ { 0 } + Z _ { 1 } + 4 R _ { \mathrm { f } } } } \\ { u _ { \mathrm { n } } = - \frac { U _ { \mathrm { d c } } ( Z _ { 0 } - Z _ { 1 } ) } { Z _ { 0 } + Z _ { 1 } + 4 R _ { \mathrm { f } } } } \end{array} \right.\tag{16}
$$

where $Z _ { 0 }$ and $Z _ { 1 }$ are the 0-mode and 1-mode wave impedance respectively.

$$
\begin{array} { l }   \{ \begin{array} { l l } { { U _ { \mathrm { m } } ( s ) = - { \displaystyle { \frac { 2 } { s } } } + { \frac { 2 Z _ { \mathrm { c } } [ ( L _ { \mathrm { e q } } + L _ { \mathrm { d c } } ) C _ { \mathrm { { e q } } } s ^ { 2 } + ( R _ { \mathrm { e q } } + Z _ { \mathrm { c } } ) C _ { \mathrm { e q } } s + 1 ] } } } } \\ { { { } } } \\  { I _ { \mathrm { m } } ( s ) = { \displaystyle { \frac { 2 [ ( L _ { \mathrm { e q } } + L _ { \mathrm { d c } } ) C _ { \mathrm { { e q } } } s ^ { 2 } + ( R _ { \mathrm { e q } } + L _ { \mathrm { c } } ) C _ { \mathrm { e q } } s ^ { 2 } + ( 2 R _ { \mathrm { e q } } + Z _ { \mathrm { c } } ) C _ { \mathrm { e q } } s + 2 ] } { s ( L _ { \mathrm { d c } } s + Z _ { \mathrm { c } } ) [ ( 2 L _ { \mathrm { e q } } + L _ { \mathrm { d c } } ) C _ { \mathrm { { e q } } } s + 2 ] } } } } \\ { { { } } } \\   { } \{ \begin{array} { l l }  { U _ { \mathrm { n } } ( s ) = - { \displaystyle { \frac { 2 Z _ { \mathrm { c } } ( L _ { \mathrm { e q } } + L _ { \mathrm { d c } } ) C _ { \mathrm { { e q } } } s ^ { 2 } + ( 2 R _ { \mathrm { e q } } + Z _ { \mathrm { c } } ) C _ { \mathrm { { e q } } } s ^ { 2 } + ( 2 R _ { \mathrm { e q } } + Z _ { \mathrm { c } } ) C _ { \mathrm { { e q } } } s + 2 ] } } } } \\  { { } } \\   { } [  L _ { \mathrm { n } } ( L ) = -  \displaystyle  \frac  2 Z _ { \mathrm { c } } ( L _ { \mathrm { e q } } C _ { \mathrm { { e q } } } s ^ { 2 } + R _ { \mathrm { e q } } C _ { \mathrm { { e q } } } s ^ { 2 } + ( 2 R _  \mathrm  \end{array} \end{array} \end{array}\tag{11}
$$

(12)

Processed by the phase-mode transformation matrix shown in (6), the corresponding initial modulus voltage TWs can be solved as:

$$
\left\{ \begin{array} { l } { { u } _ { 1 } = - \frac { \sqrt { 2 } U _ { \mathrm { d c } } Z _ { 1 } } { Z _ { 0 } + Z _ { 1 } + 4 R _ { \mathrm { f } } } } \\ { { u } _ { 0 } = - \frac { \sqrt { 2 } U _ { \mathrm { d c } } Z _ { 0 } } { Z _ { 0 } + Z _ { 1 } + 4 R _ { \mathrm { f } } } } \end{array} \right.\tag{17}
$$

In the same method, when a failure occurs on the negativepole transmission lines, the corresponding initial modulus voltage TWs can be expressed as:

$$
\left\{ \begin{array} { l l } { u _ { 1 } = - \frac { \sqrt { 2 } U _ { \mathrm { d c } } Z _ { 1 } } { Z _ { 0 } + Z _ { 1 } + 4 R _ { \mathrm { f } } } } \\ { u _ { 0 } = \frac { \sqrt { 2 } U _ { \mathrm { d c } } Z _ { 0 } } { Z _ { 0 } + Z _ { 1 } + 4 R _ { \mathrm { f } } } } \end{array} \right.\tag{18}
$$

Similarly, when there is a pole-to-pole short-circuit fault on the transmission lines, the corresponding initial modulus voltage TWs can be calculated as:

$$
\left\{ \begin{array} { l l } { u _ { 1 } = - \frac { \sqrt { 2 } U _ { \mathrm { d c } } Z _ { 1 } } { Z _ { 1 } + R _ { f } } } \\ { u _ { 0 } = 0 } \end{array} \right.\tag{19}
$$

According to (17)–(19), the 0-mode initial voltage TWs under three typical fault conditions mentioned above are different from each other. Therefore, the WTMM of the 0-mode initial RVTWs can be extracted and used for fault-pole selection, and the corresponding criterion can be designed as (20), as shown at the bottom of this page, where $u _ { \mathrm { 0 r } }$ is the initial 0-mode RVTW, and $\mathrm { T H } _ { 3 }$ is the threshold value for fault-pole selection, respectively.

## D. FLOW CHART OF PROTECTION SCHEME

Based on the study mentioned above, flow chart of the proposed novel ultra-high-speed TW protection principle for VSC-based DC grids can be designed successfully. As shown in Fig. 7, both the voltage and current data of both poles are sampled with a higher sampling frequency and stored at the same time. If the criterion for starting-up element shown in (10) is satisfied, then sampling of both the voltage and current data will be continued for a short time. With 64 data before starting-up and 192 data after starting-up, a data window consisting of 256 data is constructed. Thereafter, the phase-mode transformation is employed and the modulus RVTWs are calculated. Next, WTMMs corresponding to the initial 1-mode and 0-mode RVTWs are extracted respectively. If an internal fault has been preliminary determined on basis of (14), then the interference identification is should be executed to prevent malfunction. For a true internal fault, fault-pole selection will be implemented for DBs breaking.

![](images/a68d6a621974a10f5bf3da24dc72d7f42c77c28a8ea2961272f96828ef00be0d.jpg)  
FIGURE 7. Flow chart of the proposed protection scheme.

![](images/59d5030d2c76594db186767343dff449da4f6411f6492bdc10dfe2efc8d24d23.jpg)  
FIGURE 8. 1-mode voltage TW and of which the absolute value of the change in amplitude.

## V. SIMULATIONS

To evaluate the performance of the proposed novel ultra-highspeed traveling-wave protection scheme, an electromagnetic transient simulation model on basis of the actual parameters of Zhangbei ±500 kV VSC-based DC grid shown in Fig. 1 was built, where the sampling frequency for signals is 500 kHz, and moreover the frequency-dependent transmission line is adopted.

In this paper, extensive simulations around the transmission line $\mathrm { O H L } _ { 2 4 }$ are carried out. For the convenience of elaboration, failures on $\mathrm { O H L } _ { 2 4 }$ are defined as internal faults, however failures in other locations are external faults. Based on the modulus TW propagation characteristics [3], WTMMs corresponding to the initial 1-mode and 0-mode RVTWs in scale $\dot { 2 } ^ { 4 }$ are utilized comprehensively for fault identification.

## A. PERFORMANCE OF THE STARTING-UP ELEMENT

A positive pole-to-ground short-circuit fault whose transition resistance is 400  occurs at 205.5 km away from ZB converter station. Waveforms in time-domain of 1-mode voltage TW and of which the corresponding absolute value of the change in amplitude detected by $\mathtt { R } _ { 2 4 }$ are shown in Fig. 8. Before the failure, there is no obvious change in the amplitude of 1-mode voltage TW, and the corresponding

$$
f = \left\{ \begin{array} { l l } { \mathrm { p o s i t i v e ~ p o l e - t o - g r o u n d ~ s h o r t - c i r c u t ~ f a u l t , } } & { \mathrm { W T M M } _ { u _ { 0 r } } < - \mathrm { T H _ { 3 } } } \\ { \mathrm { n e g a t i v e ~ p o l e - t o - g r o u n d ~ s h o r t - c i r c u t ~ f a u l t , } } & { \mathrm { W T M M } _ { u _ { 0 r } } > \mathrm { T H _ { 3 } } } \\ { \mathrm { p o l e - t o - p o l e ~ s h o r t - c i r c u t ~ f a u l t , } } & { \mathrm { o t h e r s } } \end{array} \right.\tag{20}
$$

TABLE 3. Performance of the protection starting-up element.
<table><tr><td rowspan="2">Distance /km</td><td rowspan="2">Resistance /Ω</td><td colspan="4"> $\overline { { \Delta { u } _ { \mathrm { l } } / \mathbf { k } \mathbf { V } } }$ </td></tr><tr><td> $\underline { { \Delta u _ { 1 } ( k - 1 ) } }$ </td><td>△u(k)</td><td> $\underline { { \Delta u _ { 1 } ( k + 1 ) } }$ </td><td> $\underline { { \Delta u _ { 1 } ( k + 2 ) } }$ </td></tr><tr><td rowspan="5">0.5</td><td>0</td><td>0.0177</td><td>459.8</td><td>371.7</td><td>294.4</td></tr><tr><td>100</td><td>0.0177</td><td>276.9</td><td>135.0</td><td>63.3</td></tr><tr><td>200</td><td>0.0177</td><td>198.1</td><td>69.1</td><td>22.8</td></tr><tr><td>300</td><td>0.0177</td><td>154.2</td><td>41.9</td><td>16.5</td></tr><tr><td>400</td><td>0.0177</td><td>126.3</td><td>28.1</td><td>12.7</td></tr><tr><td rowspan="5">50</td><td>0</td><td>0.0324</td><td>202.9</td><td>202.4</td><td>36.5</td></tr><tr><td>100</td><td>0.0324</td><td>122.2</td><td>122.8</td><td>23.4</td></tr><tr><td>200</td><td>0.0324</td><td>87.4</td><td>88.1</td><td>17.1</td></tr><tr><td>300</td><td>0.0324</td><td>68.1</td><td>68.7</td><td>13.5</td></tr><tr><td>400</td><td>0.0324</td><td>55.7</td><td>56.3</td><td>11.2</td></tr><tr><td rowspan="5">150</td><td>0</td><td>0.0161</td><td>127.6</td><td>208.2</td><td>81.7</td></tr><tr><td>100</td><td>0.0161</td><td>76.9</td><td>125.9</td><td>50.5</td></tr><tr><td>200</td><td>0.0161</td><td>55</td><td>90.3</td><td>36.5</td></tr><tr><td>300</td><td>0.0161</td><td>42.8</td><td>70.4</td><td>28.6</td></tr><tr><td>400</td><td>0.0161</td><td>35.1</td><td>57.7</td><td>23.5</td></tr><tr><td rowspan="5">205.5</td><td>0</td><td>0.0302</td><td>44.1</td><td>171.8</td><td>180.5</td></tr><tr><td>100</td><td>0.0302</td><td>26.5</td><td>103.6</td><td>117.3</td></tr><tr><td>200</td><td>0.0302</td><td>18.9</td><td>74.2</td><td>86.5</td></tr><tr><td>300</td><td>0.0302</td><td>14.7</td><td>57.8</td><td>68.5</td></tr><tr><td>400</td><td>0.0302</td><td>12.1</td><td>47.3</td><td>56.7</td></tr></table>

absolute value of the change in amplitude is nearly 0. However, when there is a failure, the amplitude of 1-mode voltage TW will change drastically, and a larger increment will appear in the corresponding absolute value of the change in amplitude.

Performance of the starting-up element under different fault condition is shown in Table III. When there is no failure on the line, the absolute value of the change in amplitude of 1-mode voltage TW is nearly 0. However, a larger increment will arise in the corresponding absolute value of the change in amplitude when there is a failure. Therefore, the reliability of the starting-up element is excellent.

## B. PERFORMANCE OF THE FAULT-SECTION IDENTIFICATION

In the simulation model, a typical external metallic positive pole-to-ground short-circuit fault locating on the line between DC breaker $\mathrm { D B } _ { 2 4 }$ and DC reactor $\mathrm { L } _ { 2 4 }$ and another typical internal positive pole-to-ground short-circuit fault of which the location is 205.5 km away from ZB converter station and the transition resistance is 400  are set respectively.

Based on the results shown in Fig. 9, all of the absolute values of the WTMMs corresponding to 1-mode RVTWs for the external fault are less than 0.5, while the absolute value of the WTMM corresponding to 1-mode RVTW for the internal fault is up to 128.9, which prove the performance of the fault section identification criterion is excellent.

## C. PERFORMANCE OF THE FAULT-POLE SELECTION

## 1) DIFFERENT FAULT TYPES

In the simulation model, three typical faults under different fault conditions are set respectively to evaluate the performance of the fault-pole selection. When the fault location is 100 km away from ZB converter station and the transition resistance is 400 , the WTMMs corresponding to 0-mode initial RVTWs for the three typical faults are different from each other. As shown in Fig. 10, polarity of the first WTMM corresponding to the positive pole-to-ground short-circuit fault is negative, while that corresponding to the negative pole-to-ground short-circuit fault is positive, and that corresponding to the pole-to-pole short-circuit fault is nearly 0.

![](images/1863cd76a378ce66cf96a8cb09c77da2100ed36e2b61636bf82f553950528a9b.jpg)

(a)  
![](images/46668d442e8ac315e455e8e3a6335d9d98a68f0b17d75c48521bad1b0bca023d.jpg)  
(b)

FIGURE 9. 1-mode RVTW and of which the WTMMs for different fault sections: (a) 1-mode RVTW and of which the WTMM for external fault; (b) 1-mode RVTW and of which the WTMM for internal fault.  
![](images/70aeeda07db00472cca9bafa4e524f1c7e47120b688f9b1867a1ff2dac61a5cd.jpg)

(a)  
![](images/c90dc23bcba525d7f925344aaaffe9d5fa78b55b8d78957c3fa949d5276df47d.jpg)

![](images/ae7cfee0133df9cf616d4daf5204e050618ad4a3bb03b241b36f9947e8cac29c.jpg)  
（c）  
FIGURE 10. 0-mode RVTW and the corresponding WTMMs for different fault types: (a) 0-mode RVTW and the corresponding WTMM for positive pole-to-ground short-circuit fault; (b) 0-mode RVTW and the corresponding WTMM for negative pole-to-ground short-circuit fault; (c) 0-mode RVTW and the corresponding WTMM for pole-to-pole short-circuit fault.

TABLE 4. WTMMs of 0-mode initial RVTWs under different fault resistances.
<table><tr><td>Types</td><td>Resistance/Ω</td><td>WTMMs</td><td>Results</td></tr><tr><td rowspan="5">1</td><td>0</td><td>-256.9</td><td rowspan="5">Positive pole-to-ground short-circuit fault</td></tr><tr><td>100</td><td>-157.2</td></tr><tr><td>200</td><td>-113.2</td></tr><tr><td>300</td><td>-88.5</td></tr><tr><td>400</td><td>-72.6</td></tr><tr><td rowspan="6">2</td><td>0</td><td>257.3</td><td rowspan="6">Negative pole-to-ground short-circuit fault</td></tr><tr><td>100</td><td>157.4</td></tr><tr><td>200</td><td>113.3</td></tr><tr><td>300</td><td>88.6</td></tr><tr><td>400</td><td>72.7</td></tr><tr><td>0</td><td>0.03</td></tr><tr><td rowspan="5">3</td><td>100</td><td></td><td>Pole-to-pole</td></tr><tr><td></td><td>0.02</td><td></td></tr><tr><td>200</td><td>0.04</td><td>short-circuit fault</td></tr><tr><td>300</td><td>0.04</td><td></td></tr><tr><td>400</td><td>0.03</td><td></td></tr></table>

TABLE 5. WTMMs of 0-mode initial RVTWs under different fault distances.
<table><tr><td>Types</td><td>Distances/km</td><td>WTMM</td><td>Result</td></tr><tr><td>1</td><td>0.5 50</td><td>-262.3 -135.1</td><td rowspan="6">Positive pole-to-ground short-circuit fault</td></tr><tr><td>100</td><td>-72.6</td></tr><tr><td>150</td><td>-71.9</td></tr><tr><td>205.5</td><td>-191.7</td></tr><tr><td>0.5</td><td>262.5</td></tr><tr><td>50</td><td>134.9</td></tr><tr><td rowspan="6"></td><td>100</td><td>72.7</td><td rowspan="6">Negative pole-to-ground short-circuit fault</td></tr><tr><td>150</td><td>71.8</td></tr><tr><td>205.5</td><td>192.2</td></tr><tr><td>0.5</td><td>0.03</td></tr><tr><td>50</td><td>0.06</td></tr><tr><td>100</td><td>0.05</td></tr><tr><td>3</td><td></td><td></td></tr><tr><td>150</td><td>0.06</td><td>short-circuit fault</td></tr><tr><td></td><td></td><td></td></tr><tr><td>205.5</td><td>0.04</td><td></td></tr></table>

## 2) DIFFERENT TRANSITION RESISTANCES

When the fault location is 100 km away from ZB converter station, the WTMMs corresponding to 0-mode initial RVTWs for the three typical faults under different transition resistances are given in Table IV. The first WTMMs for the positive pole-to-ground short-circuit faults are always negative values, while those for the negative pole-to-ground shortcircuit faults are always positive values, and those for the pole-to-pole short-circuit faults are always 0 considering the measurement error.

## 3) DIFFERENT FAULT DISTANCES

When the transition resistance is 400 , the WTMMs corresponding to 0-mode initial RVTWs for the three typical faults under different fault distances are shown in Table V. As expected, the first WTMMs are always negative values for positive pole-to-ground short-circuit faults, while those are always positive values for negative pole-to-ground shortcircuit faults, and those are always 0 for pole-to-pole shortcircuit faults considering the measurement error.

![](images/68b604a3b08e7e9043f19bdddbdbe9c92515edc2a0994b4173e6276bf43758fc.jpg)  
FIGURE 11. 1-mode RVTW and of which the WTMMs.

## D. PERFORMANCE UNDER NOISE INTERFERENCE

1) EXTERNAL METALLIC FAULTS CLOSING

TO THE FAULT POSITION

An external metallic positive pole-to-ground short-circuit fault occurs on the transmission line between DC breaker $\mathrm { D B } _ { 2 4 }$ and DC reactor $\mathsf { L } _ { 2 4 }$ . In the 1-mode RVTWs acquired by $\mathrm { R } _ { 2 4 }$ , 20dB Gauss white noise is added. As shown in Fig. 11, absolute values of the WTMMs corresponding to 1-mode initial RVTWs are very small, and therefore there will no protection action order to be sent out.

## 2) INTERNAL FAULTS LOCATING AT THE END OF THE

TRANSMISSION LINE WITH A HIGH TRANSITION RESISTANCE An internal positive pole-to-ground short-circuit fault at the end of the transmission line with a transition resistance of 400  occurs at 205.5 km away from ZB converter station. In the 1-mode and 0-mode RVTWs acquired by ${ \mathrm { R } } _ { 2 4 }$ , 20dB Gauss white noise is added respectively. As shown in Fig. 12, absolute value of the WTMM corresponding to 1-mode initial RVTW is relatively larger, and meanwhile the first WTMM corresponding to 0-mode initial RVTW is a negative value. Therefore, it is can be determined that there is an internal positive pole-to-ground short-circuit fault on the transmission line, and as a result the corresponding protection action order will be sent out.

![](images/d3fb44d7894d66044595c3c750fe2ec04de22b24b4592f50c95d065eb9cfe269.jpg)

(a)  
![](images/0837afbaf48bcc898cec772874af92eb8e739cc46bf92b578cc892b4ed779d41.jpg)  
(b)  
FIGURE 12. Modulus RVTWs and of which the WTMMs: (a) 1-mode RVTW and of which the WTMM; (b) 0-mode RVTW and of which the WTMM.

Based on the above extensive simulation results, it can be concluded that performance of the proposed novel ultrahigh-speed traveling-wave protection scheme in this paper is excellent in rapidity, reliability and robustness.

## VI. CONCLUSION

In this paper, a novel ultra-high-speed traveling-wave protection principle for VSC-based DC grids is proposed, which is based on characteristics of modulus voltage TWs. First, the absolute value of the change in amplitude of the 1-mode voltage TW is used to construct the protection starting-up element. Then, the dyadic wavelet transform is utilized to extract the wavelet-transform modulus maxima (WTMM) of 1-mode and 0-mode initial RVTWs separately, which are used for fault-section identification and fault-pole selection successively. Extensive simulation results under different fault conditions show that the proposed ultra-high-speed TW protection principle is excellent in rapidity, reliability and robustness. Therefore, the proposed novel ultra-high-speed TW protection principle in this paper can be adopted as an outstanding main protection for DC transmission lines in VSC-based DC grids.

The ultra-high-speed identification scheme for lightning interference based on traveling-wave protection principle will be conducted in the future research.

## REFERENCES

[1] X. Pei, G. Tang, and S. Zhang, ‘‘Sequential auto-reclosing strategy for hybrid HVDC breakers in VSC-based DC grids,’’ J. Modern Power Syst. Clean Energy, vol. 7, no. 3, pp. 633–643, May 2019.

[2] X. Zheng, R. Jia, L. Gong, G. Zhang, and X. Pei, ‘‘An optimized coordination strategy between line main protection and hybrid DC breakers for VSC-based DC grids using overhead transmission lines,’’ Energies, vol. 12, no. 8, pp. 1–13, Apr. 2019.

[3] X. Pei, G. Tang, and S. Zhang, ‘‘A novel pilot protection principle based on modulus traveling-wave currents for voltage-sourced converter based high voltage direct current (VSC-HVDC) transmission lines,’’ Energies, vol. 11, no. 9, p. 2395, Sep. 2018.

[4] S. Li, W. Chen, X. Yin, and D. Chen, ‘‘Protection scheme for VSC-HVDC transmission lines based on transverse differential current,’’ IET Gener., Transmiss. Distrib., vol. 11, no. 11, pp. 2805–2813, Aug. 2017.

[5] X. Li, Q. Song, W. Liu, H. Rao, S. Xu, and L. Li, ‘‘Protection of nonpermanent faults on DC overhead lines in MMC-based HVDC systems,’’ IEEE Trans. Power Del., vol. 28, no. 1, pp. 483–490, Jan. 2013.

[6] S. Xue, J. Lian, J. Qi, and B. Fan, ‘‘Pole-to-ground fault analysis and fast protection scheme for HVDC based on overhead transmission lines,’’ Energies, vol. 10, no. 7, p. 1059, Jul. 2017.

[7] B. H. Zhang, S. Zhang, M. You, and R. F. Cao, ‘‘Research on transientbased protection for HVDC lines,’’ (in Chinese), Power System Protection Control, vol. 38, no. 15, pp. 18–23, Aug. 2010.

[8] M. Zhang, J. He, G. Luo, and X. Wang, ‘‘Local information-based fault location method for multi-terminal flexible DC grid,’’ (in Chinese), Power Syst. Protection Control, vol. 38, no. 3, pp. 155–161, Mar. 2018.

[9] X. Yu, L. Xiao, L. Lin, Q. Qiu, and Z. Zhang, ‘‘Single-ended fast fault detection scheme for MMC-based HVDC,’’ (in Chinese), High Voltage Eng., vol. 44, no. 2, pp. 440–447, Feb. 2018.

[10] J. Sneath and A. D. Rajapakse, ‘‘Fault detection and interruption in an earthed HVDC grid using ROCOV and hybrid DC breakers,’’ IEEE Trans. Power Del., vol. 31, no. 3, pp. 973–981, Jun. 2016.

[11] S. Azizi, M. Sanaye-pasand, M. Abedini, and A. Hasani, ‘‘A travelingwave-based methodology for wide-area fault location in multiterminal DC systems,’’ IEEE Trans. Power Del., vol. 29, no. 6, pp. 2552–2560, Dec. 2014.

[12] S. Zhang, G. Zou, C. Xu, and C. Sun, ‘‘A non-unit line protection scheme for MMC-MTDC grids based on aerial-mode voltage traveling waves,’’ in Proc. Int. Conf. Power Syst. Technol. (POWERCON), Guangzhou, China, Nov. 2018, pp. 2482–2489.

[13] J. Liu, N. Tai, and C. Fan, ‘‘Transient-voltage-based protection scheme for DC line faults in the multiterminal VSC-HVDC system,’’ IEEE Trans. Power Del., vol. 32, no. 3, pp. 1483–1494, Jun. 2017.

[14] L. Tang, X. Dong, S. Shi, M. Kong, and Y. Qiu, ‘‘Principle and implementation of ultra-high-speed travelling wave based protection for transmission line of flexible HVDC grid,’’ (in Chinese), Power Syst. Technol., vol. 42, no. 10, pp. 3176–3186, Oct. 2018.

[15] N. Tong, X. Lin, Y. Li, Z. Hu, N. Jin, F. Wei, and Z. Li, ‘‘Local measurement-based ultra-high-speed main protection for long distance VSC-MTDC,’’ IEEE Trans. Power Del., vol. 34, no. 1, pp. 353–364, Feb. 2019.

[16] X. Guo, Y. Zhou, N. Mei, and B. Zhao, ‘‘Construction and Characteristic Analysis of Zhangbei Flexible DC Grid,’’ (in Chinese), Power Syst. Technol., vol. 42, no. 11, pp. 3698–3707, Nov. 2018.

[17] X. Guo, T. Li, G. Li, Z. Wei, B. Yuan, and D. Chen, ‘‘Fault ride-through strategy and protection setting optimization of converter valve for Zhangbei VSC-HVDC grid,’’ Power Syst. Technol., vol. 42, no. 24, pp. 196–202, Dec. 2018. (In Chinese).

[18] G. Tang, G. Wang, Z. He, H. Pang, X. Zhou, Y. Shan, and Q. Li, ‘‘Research on key technology and equipment for Zhangbei 500 kV DC grid,’’ (in Chinese), High Voltage Eng., vol. 44, no. 7, pp. 2097–2106, Jul. 2018.

[19] P. Li, W. Wang, C. Liu, Y. Huang, Y. Wang, and L. Zhang, ‘‘Economic assessment of Zhangbei VSC-based DC grid planning scheme with integration of renewable energy and pumped-hydro storage power station,’’ (in Chinese), Proc. Chin. Soc. Elect. Eng., vol. 38, no. 24, pp. 7206–7214, Dec. 2018.

[20] L. Tang and X. Dong, ‘‘Study on the characteristic of travelling wave differential current on half-wave-length AC transmission lines,’’ (in Chinese), Proc. Chin. Soc. Elect. Eng., vol. 37, no. 8, pp. 2261–2269, Apr. 2017.

[21] J. Suonan, S. Gao, G. Song, Z. Jiao, and X. Kang, ‘‘A novel fault-location method for HVDC transmission lines,’’ IEEE Trans. Power Del., vol. 25, no. 2, pp. 1203–1209, Apr. 2010.

[22] A. Lei, X. Dong, S. Shi, B. Wang, and V. Terzija, ‘‘Equivalent traveling waves based current differential protection of EHV/UHV transmission lines,’’ Int. J. Electr. Power Energy Syst., vol. 97, pp. 282–289, Apr. 2018.

[23] L. Jiang, Q. Chen, W. Huang, L. Wang, Y. Zen, and P. Zhao, ‘‘Pilot protection based on amplitude of directional travelling wave for voltage source converter-high voltage direct current (VSC-HVDC) transmission lines,’’ Energies, vol. 11, no. 8, p. 2021, Aug. 2018.

![](images/d8b54a4bce7c89536c5465d14aa92dad1371b017c6c91508059fd48595a31c1c.jpg)  
XIANGYU PEI received the B.Sc. degree from the Central South University, in 2012, the M.Sc. degree from the Huazhong University of Science and Technology, in 2015, and the Ph.D. degree from the China Electric Power Research Institute, in 2019. He is currently with the School of Electrical and Information Engineering, Changsha University of Science and Technology, Changsha, China. His research interests are power system protection and HVDC transmission line protection.

![](images/e41eb5a1c26ec2558e05544470d911b95b68f456c05d4159de882c0e4be4e2cf.jpg)

HUI PANG received the B.S. and M.S. degrees in electrical engineering from the Hefei University of Technology, China, in 2002 and 2005, respectively, and the Ph.D. degree in electrical engineering from the China Electric Power Research Institute, in 2010. His major research areas include power electronics technology, VSC-HVDC transmission, and DC grid technology.

![](images/4d8a1c2033b701d239204f32e42b4b4dce97df54975b2ef9d23128872e41802d.jpg)

![](images/0ab2e5cc32dba3fcb5122a04a2972733c53a8dc6c6d2a28c7aebf1d1e7d9b024.jpg)

YUNFENG LI received the B.S. and M.S. degrees in electrical engineering from Huadong Jiaotong University, Nanchang, China, in 2011 and 2014, respectively, and the Ph.D. degree in electrical engineering from the China Electric Power Research Institute, Beijing, China, in 2017. He is currently with State Grid Hunan Electric Power Company Limited Economic and Technical Research Institute. His research interests are VSC-HVDC transmission and DC grid technology.

LONGLONG CHEN received the B.Sc., M.Sc., and Ph.D. degrees from the Xi’an Jiaotong University and the Huazhong University of Science and Technology, in 2007 and 2009, respectively. He is currently with the Global Energy Internection Research Institute. His research interests are HVDC thyristor valves, DC circuit breakers, and transmission line protection.

![](images/0c9b750f7a7100923c13121b4410cb110b9f58d682a3c34f51ec70467289ef30.jpg)

![](images/80435de5164ffd6de69500a99347ed4a26555e0ae752918b92ae360a2f21b309.jpg)

XIAO DING received the B.Sc. and M.Sc. degrees in microelectronics and solid state electronics from the Huazhong University of Science and Technology, Wuhan, China, in 2008 and 2012, respectively, and the Ph.D. degree in power electronics and power drives from the China Electric Power Research Institute, Beijing, China, in 2018. His research interests include design of power electronic systems and their applications in HVDC transmission.

GUANGFU TANG (M’11) received the B.S. degree in electrical engineering from Xi’an Jiaotong University, Xi’an, China, in 1990, and the M.S. and Ph.D. degrees in electrical engineering from the Institute of Plasma Physics, Chinese Academy of Sciences, Hefei, China, in 1993 and 1996, respectively. He is currently an Academician with the Chinese Academy of Engineering and the Vice President of the Global Energy Interconnection Research Institute (GEIRI), Beijing, China.