Received 10 June 2024, accepted 13 July 2024, date of publication 23 July 2024, date of current version 31 July 2024. Digital Object Identifier 10.1109/ACCESS.2024.3432791

RESEARCH ARTICLE

# A Bidirectional Interleaved Totem Pole PFC-Based Integrated On-Board Charger for EV SRM Drive

T. FAHEEM ALI 1 , (Graduate Student Member, IEEE), D. ARUN DOMINIC 1 (Member, IEEE), PRAJOF PRABHAKARAN 1, (Senior Member, IEEE), AND ARUN P. PARAMESWARAN 2 1Department of Electrical and Electronics Engineering, National Institute of Technology Karnataka (NITK), Surathkal, Mangaluru 575025, India 2Department of Electrical and Electronics Engineering, Manipal Institute of Technology, Manipal Academy of Higher Education, Manipal, Udupi 576104, India Corresponding author: Arun P. Parameswaran (arun.p@manipal.edu)

ABSTRACT This paper presents an improved integrated on-board charger (IOBC) tailored for a 4-phase switched reluctance motor (SRM) drive. The proposed IOBC is non-isolated and utilizes the totem pole power factor correction (PFC) operation for reduced common-mode voltage. Furthermore, the proposed system accommodates bidirectional functions, ensuring versatility during charging mode. A non-isolated IOBC for SRM with reduced common-mode voltage and bidirectional capability has largely been ignored in the literature. The proposed system utilizes a modified Miller converter in the motoring mode and is easily reconfigured into a two-phase interleaved totem pole converter during charging modes without the need for any magnetic contactors. The proposed system features zero instantaneous torque (ZIT) at steady-state, ensuring minimal machine wear during charging modes. The proposed IOBC is controlled to ensure symmetric positive and negative grid currents for any given rotor position (during charging), thereby eliminating even harmonics and enhancing the power quality of grid current. The proposed system achieves charging power twice the motoring power with parallel-connected phase windings. Ansys electromagnetic transient simulation, MATLAB-based SRM drive simulations, experimental results, and comprehensive comparative analysis are presented to validate the various features and effectiveness of the proposed IOBC for SRM.

INDEX TERMS Electric vehicle (EV), integrated on-board charger (IOBC), power factor correction circuit (PFCC), interleaved totem pole PFC converter, switched reluctance machine (SRM).

## I. INTRODUCTION

As fossil fuels deplete, electric vehicles (EVs) emerge as a promising solution with performance, simplicity, and reduced fossil fuel dependency. However, challenges like high upfront costs, long charging times, and limited infrastructure necessitate research for a cleaner transportation future.

One of the key components in EVs is the electric motor, and currently, permanent magnet (PM) machines are the favored choice due to their high efficiency and power density. However, there are ecological and supply chain intricacies associated with the extraction and processing of rare earth minerals for PM-based motors [1]. In contrast, Switched Reluctance Motors (SRMs) offer a robust alternative to PM motors and induction motors with no PM elements or conductors on the rotor. Moreover, SRMs exhibit notable advantages in high-speed performance, fault tolerance, and resilience under challenging high-temperature conditions [2].

The availability of charging infrastructure remains a significant hurdle for EVs, but an on-board charger (OBC) can provide a reliable option for commutes within the vehicle’s battery range. The traditional OBC typically comprises two dedicated power converters for motor driving and charging. In contrast, integrated on-board chargers (IOBCs) combine these functionalities, resulting in cost savings and increased power density of the overall system [3].

As a result, the combination of IOBCs and SRM drives is emerging as a promising avenue for EV applications [4]. These technological advancements have the potential to make EVs more affordable and efficient for consumers, addressing some of the challenges that have traditionally hindered their widespread adoption. Traditionally, OBCs are isolated from the grid, but non-isolated chargers hold the advantage of greater efficiency [5]. However, they introduce potential safety concerns due to leakage current from common mode voltage, as discussed in [6]. Recent research works have identified methods to mitigate common mode voltage in nonisolated on-board chargers, making them a viable option [7]. In the literature, it is demonstrated that compared to various power factor correction (PFC) converter topologies (which is part of an OBC), the totem-pole PFC has a small common mode leakage current [8]. Additionally, the totem pole PFC converter has higher efficiency, reduced ripple in the input AC current, and fewer components compared to the other PFC topologies [8].

As mentioned earlier, research exploring the use of SRM-based IOBCs in EVs is rapidly gaining traction. Specifically, studies presented in [9], [10], [11], and [12] have delved into IOBCs for SRM-equipped Plug-in Hybrid EVs (PHEVs), while research works in [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], and [23] have investigated methodologies for SRM-equipped pure EVs.

Among the various IOBCs for SRM-equipped EVs, some have employed machine windings as filter inductors, achieving higher power density and an increased power rating for the OBC without significantly increasing system weight [3]. However, utilizing machine windings as filter inductors can induce torque pulsation or rotor rotation during charging mode. Blocking the rotor during charging may not eliminate rotor vibrations and associated wear and tear in the machine. Even when the average torque is controlled to zero, pulsating torque may still exist, resulting in rotor vibrations and associated wear and tear [24]. For example, the research presented in [17], [18], and [19] utilizes machine winding as a filter inductor during the input PFC stage. However, these methods have unequal current distribution across the machine windings during charging, leading to torque pulsation. To address this issue, research in [13] and [14] has proposed using separate inductors instead of machine windings as filter inductors during charging mode. However, this approach increases cost and reduces power density.

To address the mentioned challenge, various innovative solutions have been proposed to achieve zero instantaneous torque (ZIT) using machine windings as filter inductors. For instance, the research in [9] and [10] aims to achieve ZIT for a three-phase SRM by ensuring equal current through all three machine windings. This, in contrast to the approaches in [17], [18], and [19], gives 6 ZIT positions. However, the proposed topology is a two-stage topology, i.e., a diode bridge rectifier (DBR) followed by a three-phase PFC boost converter using machine windings. For higher efficiency, [12] suggests a bridgeless boost converter with two phases connected in series during the charging mode. This configuration ensures four stable positions with ZIT during charging. However, it necessitates the use of two magnetic contactors for reconfiguration during charging, adding to the overall cost and bulkiness, especially when considering their automotive-grade expense. Furthermore, the converters in [9], [10], and [12] lack bidirectional operation capability for OBCs.

The methods discussed in [11], [15], and [16] utilize SRM with split-phase windings to attain ZIT during the charging mode. In these approaches, one phase is split into two and excited during charging, providing two stable positions with ZIT. However, these methods require a specialized split-phase SRM and the incorporation of additional magnetic contactors for reconfiguration. The introduction of split-phase windings necessitates constructional modifications, and the inclusion of extra contactors adds to the overall expense and complexity of the system.

In [21] and [23], a four-phase SRM is reconfigured into a bridgeless boost PFC converter without using any magnetic contactors. Both have four stable ZIT positions. However, both configurations have disparities in equivalent inductances in the positive and negative cycles. This leads to even harmonics in the grid current due to unequal current ripples in positive and negative cycles. These even harmonics are mitigated in [22], with the same inductance in positive and negative cycles irrespective of the rotor position. Also, the charging methodology proposed in [22] has 8 stable ZIT positions. However, in [22], the conduction losses and switching losses are higher, with four windings and their respective semiconductor switches conducting simultaneously. Also, the converters discussed in [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [23], and [22] lack bidirectional operation capability for OBCs. Bidirectional operation capability for OBCs can facilitate versatile operating modes such as returning power back to the grid, supplying power to other loads, grid forming mode, and reactive power compensation [25].

In [23], the motor drive converter is reconfigured into a bidirectional single-phase totem-pole PFC converter for charging. The totem pole configuration enables the suppression of common mode voltage or current. However, the bidirectional operation is not detailed in the paper. Also, it requires two additional magnetic contactors. Additionally, in [23], a conventional VSI is used to drive the motor, hindering independent control of phase currents with slower demagnetization in motoring mode.

The literature shows that the development of SRM-based OBCs for EVs has gained significant traction. However, existing OBC designs often face challenges in achieving ZIT with machine windings as filter inductance. These systems often involve trade-offs between cost, complexity, and performance. Addressing these limitations requires detailed analysis and further research into innovative topologies and control strategies.

![](images/b0b277a3255ce951aa4dbcdc1aa36bda60acff7ff315f4b94c26d179143d53fb.jpg)  
FIGURE 1. Circuit configuration for the proposed SRM drive.

This paper presents a 4-phase SRM drive with integrated on-board charging capability. The advantages offered by the proposed system are listed below:

1) A modified Miller converter is used. This ensures independent control of phase currents and, hence smooth control of the SRM in motoring mode.

2) This converter can be readily reconfigured as a two-phase interleaved totem pole PFC converter utilizing the machine windings as filter inductors. This enables the suppression of common mode voltage or current and higher efficiency compared to reported IOBCs in the literature. No magnetic contactors are required for reconfiguring avoids additional costs.

3) The rotor is not blocked during charging for the proposed system. The instantaneous torque at steady-state during charging is zero. There exist four stable ZIT positions, ensuring the reliable utilization of machine windings as filter inductors.

4) The variation of machine inductance with respect to rotor position is considered for the controller design, ensuring a good power factor irrespective of rotor positions. The inductance during positive and negative cycles is equal, eliminating the even harmonics.

5) The proposed topology is capable of operating in all the following modes: (a) motoring mode, (b) regenerative breaking, grid-to-vehicle (G2V) charging mode, (c) vehicle-to-grid (V2G) mode, (d) bidirectional DC grid charging mode, and (e) vehicle-to-vehicle (V2V) mode.

6) Utilizing two interleaved, parallel-connected windings of the SRM as filter inductors enables charging power up to twice the motoring power.

In this paper, an improved and non-isolated IOBC based on an interleaved Totempole converter is proposed for a 4-phase SRM, featuring ZIT during the charging mode. Here, a detailed analysis of instantaneous torque during charging modes is provided. Finite Element Analysis (FEA) results and MATLAB simulation results are presented to validate the ZIT during charging. A hardware prototype is developed to confirm the efficacy and reliability of the system. The experimental results for motoring mode and charging modes (G2V and V2G modes) are also presented.

The organization of the remaining sections is as follows: Section II details the converter’s operation and control. Section III examines instantaneous torque under charging conditions using Ansys and MATLAB simulations. Section IV presents experimental results. Section V concludes the paper by summarizing the key contributions.

## II. PROPOSED SYSTEM

Fig. 1 shows the circuit configuration for the proposed SRM drive. It comprises a modified Miller converter-fed SRM drive with three current sensors: $\mathrm { C T _ { 1 } }$ for measuring phase A current $( i _ { A } ) , \mathrm { C T } _ { 2 }$ for measuring phase C current $( i _ { C } ) ,$ and $\mathrm { C T } _ { 3 }$ for measuring the sum of currents in phases B and D $( i _ { B } + i _ { D } )$ . In the presented drive, the converter intentionally incorporates asymmetry with diode $\mathrm { D } _ { 1 1 }$ to minimize costs, as diodes are less expensive compared to IGBT/MOSFET. Nevertheless, symmetry can be restored by substituting $\mathrm { D } _ { 1 1 }$ with IGBT/MOSFET. The subsequent sections explain the operating modes and control of the proposed converter during motoring and charging (G2V and V2G) modes.

## A. MOTORING AND REGENERATIVE BRAKING MODES1) OPERATING MODES

To achieve independent control of phase currents, the phases are shared between alternate phases as depicted in Fig. 1. The various operating states for phase A winding during motoring/regenerative braking modes are illustrated in Fig. 2. During magnetization, $\mathrm { T } _ { 2 }$ and $\mathrm { T } _ { 3 }$ conduct to apply the battery voltage across the windings. In freewheeling mode, T3 is turned off to apply zero voltage across the winding, while the switch $\mathrm { T } _ { 2 }$ and the diode $\mathrm { D } _ { 4 }$ conduct for the winding current to decay due to winding resistance. When both $\mathrm { T } _ { 2 }$ and $\mathrm { T } _ { 3 }$ are turned off, negative battery voltage is applied through $\mathrm { D } _ { 4 }$ and the reverse diode of $\mathrm { T } _ { 1 }$ to demagnetize the windings before entering the negative torque region. The identical approach is followed for the remaining phases as well. The switching table and the current sensor to be read during each switching mode are shown in Table 1. During motoring, the phase windings are energized in the positive inductance slope region, whereas during regenerative braking, they are energized in the negative inductance slope region.

TABLE 1. Table showing the switching states and sensor used for each phase during motoring and regenerative braking modes.
<table><tr><td rowspan=2 colspan=1>Components</td><td rowspan=1 colspan=3>Phase A</td><td rowspan=1 colspan=3>Phase B</td><td rowspan=1 colspan=3>Phase C</td><td rowspan=1 colspan=3>Phase D</td></tr><tr><td rowspan=1 colspan=1>Magnetiz-ing</td><td rowspan=1 colspan=1>Freewheel-ing</td><td rowspan=1 colspan=1>Demagne-tization</td><td rowspan=1 colspan=1>Magnetiz-ing</td><td rowspan=1 colspan=1>Freewheel-ing</td><td rowspan=1 colspan=1>Demagne-tization</td><td rowspan=1 colspan=1>Magnetiz-ing</td><td rowspan=1 colspan=1>Freewheel-ing</td><td rowspan=1 colspan=1>Demagne-tization</td><td rowspan=1 colspan=1>Magnetiz-ing</td><td rowspan=1 colspan=1>Freewheel-ing</td><td rowspan=1 colspan=1>Demagne-tization</td></tr><tr><td rowspan=1 colspan=1>Switches / Diodes</td><td rowspan=1 colspan=1> $\mathrm { T } _ { 2 } , \mathrm { T } _ { 3 }$ </td><td rowspan=1 colspan=1> $\mathrm { T } _ { 2 } , \mathrm { D } _ { 4 }$ </td><td rowspan=1 colspan=1> $\mathrm { D } _ { 4 } ,$ Diode $\mathrm { o f ~ T _ { 1 } }$ </td><td rowspan=1 colspan=1> $\mathrm { T } _ { 8 } , \mathrm { T } _ { 9 }$ </td><td rowspan=1 colspan=1> $\mathrm { T } _ { 8 } , \mathrm { D } _ { 1 0 }$ </td><td rowspan=1 colspan=1> $\Gamma _ { 1 0 } ,$ DiodeofT7</td><td rowspan=1 colspan=1> $\mathrm { T } _ { 3 } , \mathrm { T } _ { 6 }$ </td><td rowspan=1 colspan=1> $\mathrm { { T } } _ { 6 } , \mathrm { { D } } _ { 4 }$ </td><td rowspan=1 colspan=1> $\mathrm { D } _ { 4 } ,$ DiodeofTs</td><td rowspan=1 colspan=1> $\mathrm { T } _ { 9 } , \mathrm { T } _ { 1 2 }$ </td><td rowspan=1 colspan=1> $\mathrm { T } _ { 1 2 } , \mathrm { D } _ { 1 0 }$ </td><td rowspan=1 colspan=1> $\mathrm { D } _ { 1 0 } , \mathrm { D } _ { 1 1 }$ </td></tr><tr><td rowspan=1 colspan=1>Current Sensor</td><td rowspan=1 colspan=3> $\mathrm { C T _ { 1 } }$ </td><td rowspan=1 colspan=3>CT3</td><td rowspan=1 colspan=3>CT</td><td rowspan=1 colspan=3>CT</td></tr></table>

![](images/736ca18c416b4e70c3a5b13c1e63970a32dcedcb9996066ddcc8ee0b23c8107d.jpg)

![](images/0122f93b46d1936a6c855ee87e1cfa84935a6e5eb9cf8b18b9226aa22cd1cc0e.jpg)

![](images/dfbb777acfd54be0922ba899cd565a7d4eacb58a60208cb3cf42af11f12133e5.jpg)  
FIGURE 2. Three operating states of phase A during the motoring and regenerative braking modes. (a) Magnetization mode. (b) Zero voltage mode. (c) Demagnetization mode.

TABLE 2. Machine parameters.
<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>SRMMachine</td><td>8/6,1 hp,2000 RPM</td></tr><tr><td>Stator Resistance (Rs)</td><td>1Ω</td></tr><tr><td>Inertia (J),Friction (B)</td><td>0.00082 kg.m²,0.001 N.m.s</td></tr><tr><td>Unaligned Phase Inductance</td><td>3.8mH</td></tr><tr><td>Aligned Phase Inductance</td><td>22.8mH</td></tr><tr><td>Voltage and Current</td><td>400V,2.5 A</td></tr></table>

![](images/58f836d4ec6c6f05db795413f3e9315685d3dc554bc76a200528d840a81d5ff6.jpg)  
FIGURE 3. Control block diagram for the proposed SRM drive in motoring mode.

![](images/7451ca4b38ed41b699071d81da3d141ef63c43e457576f6087d34cfda032aa59.jpg)  
FIGURE 4. Circuit configuration of the power converter during charging mode (reconfigured version of the circuit in Fig. 1.

## 2) CONTROL DESIGN

Fig. 3 shows the control block diagram for the proposed SRM drive in motoring mode. The linearized model of SRM based on the machine parameters outlined in Table 2 is derived using small signal analysis [26]. The obtained transfer functions are expressed as follows:

$$
\begin{array} { l } { \displaystyle \frac { I ( s ) } { d ( s ) } = \frac { 7 4 . 0 7 s + 9 0 . 3 3 } { 0 . 0 0 2 5 s ^ { 2 } + 2 . 7 0 7 s + 9 . 7 3 4 } } \\ { \displaystyle \frac { \omega _ { r } ( s ) } { I ( s ) } = \frac { 2 0 5 . 9 } { s + 1 . 2 2 } } \end{array}\tag{1}
$$

(2)

Here, $I , d ,$ , and $\omega _ { r }$ denote the current, the duty cycle, and the rotor speed, respectively. Whereas the $\omega _ { r } ^ { * }$ and $I ^ { * }$ refers to speed and current command signals, respectively.

The current controller (type 2 compensator) is designed using the K-factor approach [27] to achieve a desired phase margin of $7 0 ^ { \circ }$ at a loop gain bandwidth of 800 Hz (as the switching frequency is 10 kHz). Similarly, the speed controller is designed for a loop gain bandwidth of 4 Hz and with a desired phase margin of $8 0 ^ { \circ }$ . The obtained speed $( G _ { m \omega } )$ and current $( G _ { m i } )$ control transfer functions are as follows:

![](images/97dbf001b60692720044fd22b634c626f8cee59b2dd38830e8ef216b1966c723.jpg)  
FIGURE 5. Operating modes for phase A winding in G2V/V2G modes. (a) While $\tau _ { 2 }$ is turned on during the positive cycle. (b) While $\tau _ { 2 }$ is turned off during the positive cycle. (c) While $\tau _ { 1 }$ is turned on during the negative cycle. (d) While $\tau _ { 1 }$ is turned off during the negative cycle.

![](images/9487be65796b152899a2485405625a832239d9933e55b6c9b6faac0462db2183.jpg)  
FIGURE 6. Control block for G2V (positive current reference) and V2G (negative current reference) modes.

$$
G _ { m \omega } = \frac { 2 8 . 5 7 } { s } \frac { s + 2 . 7 0 5 } { s + 2 3 3 . 5 } ; \quad G _ { m i } = \frac { 8 7 3 6 } { s } \frac { s + 5 9 3 . 2 } { s + 4 2 5 9 0 }\tag{3}
$$

The obtained controller transfer function is in the continuous domain. This is discretized using bilinear transformation for a sampling period of $2 0 \mu s$ for the digital implementation of the controller.

## B. CHARGING (G2V AND V2G) MODES

## 1) OPERATING MODES

During the charging (G2V and V2G) modes, when the vehicle is parked, the rotor shaft must first be disengaged from the transmission and, hence, the wheels, allowing the rotor to rotate freely. Then, the switch S in Fig. 1 is closed. During steady-state operation, as the dc-link voltage exceeds the peak grid voltage, the free-wheeling diode of $\mathrm { T } _ { 3 }$ and the diode $\mathrm { D } _ { 4 }$ remain non-conductive. Switches $\mathrm { T } _ { 1 } , \mathrm { T } _ { 2 } , \mathrm { T } _ { 5 } , \mathrm { T } _ { 6 } , \mathrm { T } _ { 7 }$ and $\mathrm { T } _ { 8 }$ form a two-phase interleaved totem pole PFC rectifier, as depicted in Fig. 4.

The operational modes of the converter in AC gridconnected modes for phase A are illustrated in Fig. 5. The totem-pole PFC operates in the positive and negative cycles of the AC mains input. The current flow depends on how

$T _ { 2 }$ and $T _ { 1 }$ are switched. The switches, together with the inductor, create a synchronous boost converter. Similarly, phase C operates interleaved with phase A, utilizing switches $T _ { 5 }$ and $T _ { 6 }$ with a 180◦ phase shift.

Fig. 6 illustrates the control block diagram for G2V and V2G modes. In the positive half cycle, $T _ { 2 }$ and $T _ { 6 }$ serve as boost switches with duty cycles $d _ { 1 }$ and d2, while $T _ { 1 }$ and $T _ { 5 }$ are driven by complementary PWM signals $( 1 ~ - ~ d _ { 1 } )$ and $( 1 - d _ { 2 } )$ respectively. Simultaneously, $T _ { 8 }$ conducts continuously. In the negative half cycle, the roles reverse with $T _ { 1 }$ and $T _ { 5 }$ as boost switches, and $T _ { 2 }$ and $T _ { 6 }$ driven by complementary PWM signals. Throughout, $T _ { 7 }$ conducts continuously. Seamless bidirectional operation is achieved by switching $T _ { 8 }$ during the positive cycle and $T _ { 7 }$ during the negative half cycle of the input voltage.

## 2) CONTROL DESIGN

As shown in Fig. 6, the converter can operate in constant voltage (CV) and current (CC) modes. In CV mode, the battery voltage is regulated, while in CC mode, the grid current (or indirectly the battery current) is regulated. A second-order generalized integrator (SOGI) based phase locked loop (PLL) with offset rejection is designed and implemented [28]. The reference peak current is multiplied by the sine output of the PLL and the sign of grid voltage to get the reference current. The measured current is multiplied by the sign of grid voltage and compared with the reference current. In V2G mode, the reference peak current is set to a negative value.

The machine windings have a rating of 2.5 A. In gridconnected modes, where two windings are interleaved, the controller is specifically designed for a rated current of 2.5 A per inductor. The small signal model for the converter is derived based on an average inductance value [29]. The subsequent sections provide a detailed discussion of the variation of inductance with respect to the rotor position. The voltage and current controllers shown in Fig. 6 are designed using the K-factor method [27]. The current controller is designed to achieve a phase margin of $6 0 ^ { \circ }$ at a loop gain bandwidth of 2 kHz (as the switching frequency is 20 kHz), while the voltage controller is designed for a phase margin of $6 0 ^ { \circ }$ at a loop gain bandwidth of 20 Hz. The obtained voltage $( G _ { c \nu } )$ and current $( G _ { c i } )$ controller transfer functions are as follows:

$$
G _ { c \nu } = \frac { 3 . 9 7 6 } { s } \frac { s + 8 . 3 3 5 } { s + 4 7 . 9 9 } ; G _ { c i } = \frac { 2 2 1 0 0 } { s } \frac { s + 3 3 6 6 } { s + 4 6 9 1 0 }\tag{4}
$$

For digital implementation of the controller, the controller is discretized using bilinear transformation for a sampling period of $2 0 \mu s$

## III. DISCUSSION ON INSTANTANEOUS TORQUE AND VARIATION OF INDUCTANCE DURING CHARGING MODES

In charging modes, the proposed system functions exclusively with two specific windings: phase A and phase C. As a result, the torque generated is the combined sum of the torques produced by phase A and phase C. Hence, the net

![](images/4e2ec15c2a0f32a92cf5c5d512c6146b04dae3a58a6fb5ea9211c90901720c73.jpg)

![](images/8dd03f456561083f028ec9856cf346c5512a64a082f557da6e3088d8d5a98c3c.jpg)  
FIGURE 7. Look-up tables (LUTs) obtained from SRM characterization using Ansys. (a) Current LUT. (b) Torque LUT.

torque $( T _ { n e t } )$ is given by:

$$
T _ { n e t } = T _ { A } + T _ { C }\tag{5}
$$

In charging modes, the Totempole PFC is controlled to ensure equal currents in both phases’ windings, with the polarity determined by the AC cycles. Nevertheless, the torque generated per phase remains unipolar. This unipolarity is a consequence of the torque per phase in the SRM being directly proportional to the square of the phase current, as illustrated in the equation below:

$$
T _ { p h } = i { _ { p h } } ^ { 2 } \frac { d L _ { p h } } { d \theta } .\tag{6}
$$

Equation (6), further demonstrates that the magnitude of torque produced per phase also increases with the inductance slope and depends on its sign.

In subsequent sections, individual phase torques and net torque during the charging modes are analyzed theoretically, along with the Ansys and MATLAB Simulink simulation results.

## A. DEVELOPMENT OF SIMULATION MODEL

To accurately analyze the performance of the SRM during charging mode, an appropriate model needs to be developed using FEA [2]. For this purpose, the motor is designed using Ansys RMxprt by providing geometric parameters of the motor. The resulting model serves two primary purposes: (i) to investigate the transient behavior of the rotor position during charging using Ansys Maxwell Transient analysis, and (ii) to develop a MATLAB Simulink model to analyze the voltage, current, and torque of the SRM during charging.

The 2D model of the SRM generated using Ansys RMxprt simulation is utilized for the Ansys Maxwell simulation (with the solution type set to Transient). The Ansys Maxwell simulation results are discussed in more detail in the next section. To derive the MATLAB Simulink model of the SRM, flux data is extracted from the Ansys RMxprt simulation results. The obtained flux data is then interpolated to maintain uniformity, and the interpolated results are inverted to generate the phase current lookup table (LUT) data, plotted and shown in Fig. 7(a). This LUT data facilitates the mapping of phase current for a given flux and rotor position. Utilizing the interpolated flux data, the torque LUT is generated by integrating the flux data along the current vector. The torque LUT data, plotted and shown in Fig. 7(b), are used for calculating the torque of the SRM for any given current and rotor position. Utilizing the LUTs (Fig. 7), an accurate MATLAB Simulink SRM model is derived.

## B. ANSYS TRANSIENT ANALYSIS: RESULTS AND DISCUSSION

The transient simulation for the Ansys Maxwell model is carried out with phases A and C excited with a 4A peak sinusoidal current, as these phases are utilized in charging. Fig. 8(a) shows the rotor trajectory with different initial rotor positions when the two phases are excited as mentioned above. The phase inductance profile and torque profile of the two phases of the SRM, along with the net torque for the given excitation, are plotted alongside the rotor position trajectory to provide a clear understanding. Fig. 8(b) shows the inductance profile obtained using FEA for different phase current values.

In Fig. 8(a), one electrical cycle is divided into four segments. From the figure, it is evident that if the initial rotor position is in segment I, the rotor settles at stable position I. In segment I, the slopes of the inductance for phases A and C are opposite, resulting in opposing torques (as per (6)). Hence, the rotor tends to settle at the position where the net torque is zero. The same applies to segment III. Consequently, in segments I and III, the rotor settles at the position where the phase inductance values of the phases are exactly equal. It is evident from the figure that if the initial rotor position lies in segment III, the rotor settles at stable position III. Therefore, when the rotor is at stable positions I or III,

$$
{ \frac { d L _ { A } } { d \theta } } = - { \frac { d L _ { C } } { d \theta } } \Rightarrow T _ { A } = - T _ { C } \Rightarrow T = 0\tag{7}
$$

These are the positions referred to as stable position I (7.5◦) and stable position III (37.5◦) in Fig. 8(a), with an inductance value of 11.5 mH.

As shown in Fig. 8(a), if the initial rotor position is in segment II or III, the rotor settles at rotor positions II and III, respectively. In segment II, as evident from Fig. 8(a), the C-phase torque $( T _ { C } )$ is low compared to the A-phase torque $\left( T _ { A } \right)$ since phase C is nearly in the unaligned position. In segment II, $T _ { A }$ is positive below stable position II and negative beyond stable position II. Consequently, if the initial position of the rotor is at any point in segment II, the rotor aligns with phase A of the stator pole at position II (22.31◦) during steady state, where the net torque is zero. Similarly, in segment IV, the rotor aligns with phase C of the stator pole at position IV (52.69◦), where the net torque is zero. Hence, when the rotor is at stable positions II or IV,

$$
{ \frac { d L _ { A } } { d \theta } } = { \frac { d L _ { C } } { d \theta } } = 0 \Rightarrow T = T _ { A } = T _ { C } = 0\tag{8}
$$

As a result, the inductances of phases A and C differ at these stable positions. At stable position II, the inductance of phase A matches the aligned inductance (22.8 mH), while the inductance of phase C corresponds to the unaligned inductance (3.8 mH) of the SRM. Conversely, at stable position ${ \mathrm { I V } } ,$ the inductance of phase C takes the aligned inductance value (22.8 mH), whereas the inductance of phase A takes the unaligned inductance value (3.8 mH).

![](images/6cd8b1fbb6ca030f1c4e9c2dc92eabed12b3ff1ce591c9e3f7e63be89b2c05f6.jpg)  
(b)

![](images/05f82dddb9fa50ac56bdd6486581c3022a88641bd79f243737c1e8d6fb95b4a2.jpg)  
(b)

FIGURE 8. FEA results depicting (a) rotor trajectory with arbitrary initial position plotted along with inductance and torque profiles. (b) Phase inductance profile of the SRM for different phase currents.  
![](images/763dad9ffdf3d30cb76cb3b8879f247ee739de82f7ce18775179f5a1bdcc1920.jpg)  
(a)

![](images/0ac96442c4225988b916338eeb06087e8b193d2896c1d26fe43f8805e2f0954f.jpg)  
(b)

![](images/ba0489f7b9cdc0ec640727dc90a5182a76f989d49aba0d180bce1ed6d609d868.jpg)  
（c）

![](images/b3addf44bcd7768543ec55156433eaf578fdf9840703ec5738f2f992870b45f5.jpg)  
(d)  
FIGURE 9. Ansys FEA results showing flux lines at the stable positions. (a) Stable Position I (7.5◦) (b) Stable Position II (22.31◦) (c) Stable Position III (37.5◦) (d) Stable Position IV (52.69◦).

Hence, it is clear from the above discussion that with equal currents in phases A and C during charging mode, from any arbitrary initial position, the rotor aligns along any one of the aforementioned stable positions. Fig. 9 shows the steady-state rotor positions (stable positions I, II, III, and IV) and flux lines during charging modes. From Fig. 8 and Fig. 9, it is evident that the maximum angular displacement from any arbitrary initial position to the corresponding stable position is nearly equal to 7.5◦.

## C. INDUCTANCE VALUES DURING CHARGING MODE

As discussed in the previous section, designing the controller for charging modes requires an accurate small signal model of the power electronic converter. This requires the phase inductance values. From the above discussion, the three potential combinations of inductance values during charging mode are as follows:

$$
\begin{array} { l } { { L _ { A } = L _ { C } = 1 1 . 5 m H P o s I \& I I I } } \\ { { L _ { A } = 2 2 . 8 m H L _ { C } = 3 . 8 m H P o s I I } } \\ { { L _ { A } = 3 . 8 m H L _ { C } = 2 2 . 8 m H P o s I V } } \end{array}\tag{9}
$$

The average value of inductance of a phase across the four stable positions can be calculated as below:

$$
L _ { a \nu g } = { \frac { ( 3 . 8 + 1 1 . 5 + 1 1 . 5 + 2 2 . 8 ) m H } { 4 } } = 1 2 . 4 m H\tag{10}
$$

For small signal modeling of the totem pole converter, a filter inductor value of 12.4 mH is assumed, representing the average inductance at stable rotor positions (as in (10)). Analysis of (9) reveals significant inductance deviations from the average during stable positions II and IV. Consequently, the phase with the lowest inductance value (3.8 mH) exhibits a higher current ripple, while the phase with a higher inductance value (22.8 mH) experiences a lower ripple. However, interleaving ensures that these variations in inductance values do not impact the power quality of the grid current during charging mode. Furthermore, once the rotor is immobilized (i.e., in stable positions), the inductance remains constant for both phases during both positive and negative cycles. This ensures a symmetric current waveform, effectively preventing the occurrence of even harmonic currents.

## D. MATLAB SIMULATIONS: RESULTS AND DISCUSSION

As discussed in Section III-A, the FEA-based SRM simulation model is employed in MATLAB Simulink to analyze the converter’s performance during charging modes. Alongside the SRM model, the converter is designed and implemented in the MATLAB simulation. For this purpose, the DC link capacitor $( C _ { b a t } )$ is designed considering a battery voltage $V _ { b a t } )$ of 400 V, a voltage ripple (1V ) of 1%, and a minimum power $( P _ { o u t } )$ of 1 kW. The frequency of the output voltage ripple $( f _ { r i p p l e } )$ is known to be 100 Hz (given the grid frequency is 50 Hz), and the calculation for $C _ { b a t }$ is expressed

![](images/69fca739627eecf54fb4c0dcb072e5cde192ad95d06973f79f44475909ec48bb.jpg)  
FIGURE 10. Simulation results showing input grid voltage, grid current, inductor currents, A-phase and C-phase torques, and net torque for stable positions. (a) Position I. (b) Position II. (c) Position III. (d) Position IV.

![](images/3a9c679eda11158ce1d3a73db8ac629daefe47ad0f1d6a757a5985f158fdc449.jpg)  
FIGURE 11. Photograph of the experimental setup.

as follows [30]:

$$
C _ { b a t } = \frac { P _ { o u t } } { 2 \pi f _ { r i p p l e } V _ { b a t } ^ { 2 } \Delta V } \approx 1 0 0 0 \mu F\tag{11}
$$

The converter’s switching frequency during the charging mode is set at 20 kHz. The control block diagram and controller parameters utilized for the simulation are depicted in Fig. 6 and (4), respectively. This MATLAB simulation evaluates the performance of the designed controllers and PFC operation in both charging modes (i.e., G2V and V2G). Furthermore, the simulation validates and presents the phase torque and net torque of the SRM at steady-state positions.

Fig. 10 illustrates simulation results during charging mode, showcasing input grid voltage, grid current, inductor currents, A-phase and C-phase torques, and net torque at stable positions I, II, III, and IV. In Fig. 10, the phase C currents is intentionally inverted to enhance visibility. In Fig. 10(a) (stable position-1), equal current ripples in phase A and phase C are evident due to identical inductances (11.5 mH). Also, it is observed that the A-phase and C-phase torques are equal and opposite, leading to a net instantaneous torque that is negligibly low and a zero average net torque. Additionally, as evident from 10(a), during the mode transition from G2V to V2G at 0.053 seconds, the converter exhibits seamless tracking of the reference current, and negligible net torque ensures no pulsation during the switching process. Fig. 10(b) displays simulation results for stable position II, revealing unequal current ripples due to differing inductance values (as discussed earlier). Despite the higher phase-C current ripple (3.8 mH), interleaved operation reduces the grid current’s THD to 4.61% [Fig. 10(b)]. Additionally, it can be observed that the phase A and phase C torque is low, giving negligible net zero instantaneous torque, and zero average torque.

![](images/7f56505e5abe04ed86b1a799bca22b4b3e7e4424ecb9867ddc245e73f79b9099.jpg)  
FIGURE 12. Experimental results during motoring mode. (a) Steady-state speed and phase (phase A) current at a speed of 300 rpm. (b) Steady-state speed and phase (phase A) current at a speed of 500 rpm. (c) Speed transient for increasing speed reference from 0 to 800 rpm. (d) Speed transient for decreasing speed reference from 800 to 300 rpm. (e) Speed for variable speed references.

Similar waveforms are observed at stable positions III and IV (Fig. 10(c) and Fig. 10(d)), following patterns seen in stable positions I and II, respectively. From Fig. 10(b) to Fig. 10(d), it is also observed that seamless tracking of reference current and negligible instantaneous torque persist during transitions from G2V to V2G and vice versa across stable positions II to IV.

## IV. EXPERIMENTAL RESULTS

To validate the efficacy of the proposed motor drive with IOBC capability for an SRM-based EV, an experimental prototype is set up in the laboratory, featuring a 1-hp SRM coupled with a separately excited DC machine as shown in Fig. 11. The parameters of the motor employed in the experimental setup are detailed in Table 2.

In the experimental setup, a 0-750V, 15A regulated power supply (with voltage setting ranging from 350 to 400V) is used to emulate the battery for testing the motor drive and V2G functionality of the proposed system. For validating the performance of the system in G2V mode, a resistor bank with a rating of 100, 5A, is used and connected at the DC link to dissipate the power drawn from the grid. The motor drive prototype comprises six SKM50GB12T4 IGBT legs (rated 1200 V, 50 A) equipped with Skyper 32R drivers. An incremental encoder (ERA50T) with a resolution of 1024 PPR is connected to the motor shaft to detect precise rotor position. Additionally, three hall current sensors (LA25P) are utilized to measure the phase currents, as shown in Fig. 1. MCP6022 op-amp-based differential amplifier circuits are employed for signal conditioning in the current and grid-side voltage sensing circuits. A DSP microcontroller TMS320F28379D is employed for the digital control implementation of the entire system.

## A. MOTORING MODE

The proposed drive in motoring mode is analyzed for steadystate and dynamic performance. To enhance the dynamic performance of the drive, integrator anti-windup using the back-calculation method for the speed loop is incorporated into the closed-loop control system depicted in Fig. 3.

Fig. 12 displays closed-loop steady-state and dynamic waveforms during motoring mode. The efficacy of closed-loop current control is evident in Fig. 12(a) and 12(b), depicting speed and phase current profiles at reference speeds of 300 rpm and 500 rpm, respectively. Fig. 12(c) reveals that with a speed reference of 800 rpm, the motor settles within 1.52 seconds with minimal overshoot. Similarly, Fig. 12(d) demonstrates a 2-second settling time with a 100 rpm undershoot at a reference speed of 300 rpm, while the motor operates at 800 rpm. Fig. 12(e) showcases successful tracking of the reference speed, demonstrating the efficacy of the designed controllers (shown in (3)). Integral anti-windup implementation effectively mitigates windup effects, contributing to improved control performance for the drive.

## B. G2V AND V2G MODES

To validate the performance of the experimental prototype of the proposed IOBC’s during charging modes, a single-phase autotransformer was employed to connect the AC supply to the converter. The converter, configured in a totem pole arrangement, is operated in closed-loop with two levels of interleaving. The obtained experimental results, showcasing basic waveforms, switch stress, and output voltage, are presented in Fig. 13. Fig. 13(a) illustrates the input voltage and duty cycle waveforms for $T _ { 2 }$ and $T _ { 6 } ,$ while Fig. 13(b) depicts the output waveform of the PLL, along with the two inductor currents and the grid current. It is evident that interleaved operation effectively reduces the ripple in the grid current compared to the two inductor currents. Fig. 13(c) demonstrates the voltage stress across the low-side switches $( T _ { 2 }$ and $T _ { 6 } )$ and highlights the interleaved operation of the switches with 20 kHz switching frequency. Fig. 13(d) presents the output DC-link voltage and the dc current. Overall, the waveforms presented in Fig. 13 closely align with the theoretical analysis and effectively demonstrate the performance of the designed controller.

![](images/a4e29929a016533df30d794a73686d3fcdd24b46204d5c6fb866c5940f90d6d1.jpg)  
FIGURE 13. Experimental results showing waveforms in G2V/V2G modes for a grid reference current of 4 A. (a) Grid voltage and duty cycles for $\tau _ { 2 }$ and $\pmb { \tau _ { 6 } } .$ (b) PLL output, inductor currents $\check { ( i _ { A } ) }$ and $i _ { c } ) ,$ and grid current (iGrid ). (c) Voltage across $\tau _ { 2 }$ and $\pmb { \tau _ { 6 } } .$ (d) Battery voltage $( \bar { v } _ { b a t } )$ and battery current.

Fig. 14 illustrates the steady-state grid current for various grid currents in charging modes. A negative current reference triggers the transition from G2V to V2G mode. THD measurements of grid current for different reference values are performed using a Fluke Power Quality Analyzer. The worst harmonic distortion recorded is 8% for a current of 1.4 A (Fig. 14(a)), while the lowest harmonic distortion is 3.5% for 4.6 A (Fig. 14(c)). These THD values adhere to IEEE 519-2022 standards. Remarkably, the converter smoothly achieved PFC operation without any significant torque pulsation in the machine during charging modes. Additionally, Fig. 14 illustrates symmetric current waveforms with equal ripples in positive and negative cycles. This is further confirmed by the absence of even harmonics in the power quality analysis.

Efficiency is evaluated in both G2V and V2G modes with varying loads, as depicted in Fig. 15. Notably, efficiency peaked at 65% load and dropped to its lowest point at 30% load for both modes. In G2V mode, the system achieved a maximum efficiency of 95.7% and a minimum of 95.23%, while in V2G mode, it demonstrated a peak efficiency of 95.43% and a minimum of 94.96%. These findings underscore the system’s robust performance across varying load conditions.

TABLE 3. Comparison of different IOBCs utilizing machine windings as filter inductors for SRM based EVs.
<table><tr><td rowspan=1 colspan=1>Reference</td><td rowspan=1 colspan=1>ZIT</td><td rowspan=1 colspan=1>Equal Inductancein +ve and -veCycles</td><td rowspan=1 colspan=1>Switches</td><td rowspan=1 colspan=1>Diodes</td><td rowspan=1 colspan=1>MagneticContactors</td><td rowspan=1 colspan=1>BidirectionalCapability</td><td rowspan=1 colspan=1>Totem PolePFC</td><td rowspan=1 colspan=2>Charging powercapability (in times ofSRM traction power)</td></tr><tr><td rowspan=1 colspan=1>[17]</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=2>1</td></tr><tr><td rowspan=1 colspan=1>[18]</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=2>1</td></tr><tr><td rowspan=1 colspan=1>[19]</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1></td><td rowspan=3 colspan=1>121</td></tr><tr><td rowspan=1 colspan=1>[20]</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>[21]</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>×</td><td></td></tr><tr><td rowspan=1 colspan=1>[22]</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=2>2</td></tr><tr><td rowspan=1 colspan=1>Proposed</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>9</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=2>2</td></tr></table>

![](images/0a14ff164624fc816ad4afafd747488775614827564c92df6e257b2c195058a0.jpg)  
(@)

![](images/c0ab01851dfc7e150c7ab505268b6b14390978913f0ffce7e1e387ac26332fd7.jpg)  
(b)

![](images/aa338289e025ac77b0bca8b086530ca55b1d0a9ef8cb66e04502df6ef2aefd27.jpg)  
（c）

![](images/b09118d8dbae5d8f7a4501466cf39a89ae8bdad5839ef9d808d9b32f4f354d54.jpg)  
(d）

![](images/f5df049389b7eaca1fdd8aeae8bdd1a8ee7b817e0db189c8c0b6727ca076b593.jpg)  
(e)

![](images/0d50340848a2951eae3f1f62d225791761e0b3d2c608ed3db7d439dd2072c69d.jpg)

![](images/cbd73c07e75f61187fde68988941fe7bd042cb548661ee9dd18b515294f3b7b8.jpg)  
(g）

(f)  
![](images/af5a05ba586553d0b3fa5fca25890bb11b4c5d56480c2e0d28f9c01f7803f719.jpg)  
(h)  
FIGURE 14. Experimental results showing grid voltages and current waveforms in G2V/V2G modes for different reference grid currents. (a) 1.4 A. (b) 2.83 A. (c) 4.6 A. (d) 5.3 A. (e) -2.12 A. (f) -3.18 A. (g) -3.9 A. (h) -5.2 A.

Table 3 provides a comprehensive comparison of the proposed IOBC’s features against other reported IOBCs for SRM-based EVs. The comparison is based on various key criteria, including instantaneous electromagnetic torque production during charging, even harmonics, power electronic component count, magnetic contactor usage, bidirectional capability, and power capacity. From Table 3, it can be inferred that the proposed SRM drive with IOBC capability (with interleaved totem pole PFC operation) exhibits bidirectional power transfer with a capacity twice that of the traction power. Other SRM-based OBCs reported in the literature do not exhibit bidirectional capability. Additionally, the proposed OBC has the advantage of reduced common-mode voltage with the totem-pole PFC converter [8]. During charging mode, the system achieves ZIT operation, eliminating torque pulsations. By employing equal filter inductance values in both positive and negative cycles during charging modes, the proposed converter maintains symmetrical grid current, effectively suppressing even harmonics. Furthermore, the absence of additional magnetic contactors for reconfiguration contributes to the system’s cost-effectiveness.

![](images/ac33106c732e4122bf9246c801db6457548317d5399ba08083a5f98c549f1099.jpg)  
FIGURE 15. Efficiency vs load curve obtained from experimental results.

## V. CONCLUSIONS

In conclusion, this paper introduces a novel IOBC system specifically designed for a 4-phase SRM drive. The proposed IOBC employs a modified Miller converter in motoring mode and seamlessly transitions to a two-phase interleaved totem pole converter during charging modes, eliminating the need for magnetic contactors. Leveraging interleaved totem pole PFC operation, the system attains commendable power quality, heightened efficiency, and reduced common mode leakage currents in charging modes (G2V/V2G).

This versatile IOBC demonstrates bidirectional capability, accommodating various operational modes, including G2V, V2G, V2V, etc., although the G2V and V2G functionalities are exclusively validated in this study. The IOBC’s circuit configuration and control ensures ZIT for the motor during charging, mitigating wear and tear induced by torque pulsations. The system’s performance is further substantiated through simulations conducted using Ansys and Matlab Simulink, validating its efficacy in charging modes.

Experimental results from the hardware prototype of the IOBC affirm the SRM drive’s performance in both driving and charging modes. Key findings from the theoretical analysis, simulation and experimental results include:

1) ZIT on the motor during charging modes.

2) Grid current THD below 5% under near-rated conditions.

3) PFC operation (>0.99 power factor) ensuring enhanced power quality in the grid current during charging.

4) Equal inductance in positive and negative cycles of the grid voltage, resulting in symmetrical grid currents with no even harmonics.

5) Usage of zero magnetic contactors for transitioning from motoring to charging modes.

6) Bidirectional operation with minimum number of power electronic components (i.e. 9 switches and 3 diodes).

7) Peak efficiencies of 95.7% in G2V mode and 95.43% in V2G mode.

8) Precise tracking of motor speed reference with superior dynamic performance (settling time = 1.52 s and 100 rpm overshoot) in motoring mode.

In summary, the proposed IOBC system demonstrates robust performance across various modes, providing a promising solution for efficient and high-quality power transfer in 4-phase SRM drives.

## REFERENCES

[1] I. Boldea, L. N. Tutelea, L. Parsa, and D. Dorrell, ‘‘Automotive electric propulsion systems with reduced or no permanent magnets: An overview,’’ IEEE Trans. Ind. Electron., vol. 61, no. 10, pp. 5696–5711, Oct. 2014.

[2] B. Bilgin, B. Howey, A. D. Callegaro, J. Liang, M. Kordic, J. Taylor, and A. Emadi, ‘‘Making the case for switched reluctance motors for propulsion applications,’’ IEEE Trans. Veh. Technol., vol. 69, no. 7, pp. 7172–7186, Jul. 2020.

[3] A. Khaligh and M. D’Antonio, ‘‘Global trends in high-power on-board chargers for electric vehicles,’’ IEEE Trans. Veh. Technol., vol. 68, no. 4, pp. 3306–3324, Apr. 2019.

[4] M. Yilmaz and P. T. Krein, ‘‘Review of battery charger topologies, charging power levels, and infrastructure for plug-in electric and hybrid vehicles,’’ IEEE Trans. Power Electron., vol. 28, no. 5, pp. 2151–2169, May 2013.

[5] S. Rivera, S. M. Goetz, S. Kouro, P. W. Lehn, M. Pathmanathan, P. Bauer, and R. A. Mastromauro, ‘‘Charging infrastructure and grid integration for electromobility,’’ Proc. IEEE, vol. 111, no. 4, pp. 371–396, Apr. 2023.

[6] Y. Zhang, G. Yang, X. He, M. Elshaer, W. Perdikakis, H. Li, C. Yao, J. Wang, K. Zou, Z. Xu, and C. Chen, ‘‘Leakage current issue of nonisolated integrated chargers for electric vehicles,’’ in Proc. IEEE Energy Convers. Congr. Expo. (ECCE), Sep. 2018, pp. 1221–1227.

[7] Y. Zhang, W. Perdikakis, Y. Cong, X. Li, M. Elshaer, Y. Abdullah, J. Wang, K. Zou, Z. Xu, and C. Chen, ‘‘Leakage current mitigation of non-isolated integrated chargers for electric vehicles,’’ in Proc. IEEE Energy Convers. Congr. Expo. (ECCE), Sep. 2019, pp. 1195–1201.

[8] M.-H. Park, J. Baek, Y. Jeong, and G.-W. Moon, ‘‘An interleaved totem-pole bridgeless boost PFC converter with soft-switching capability adopting phase-shifting control,’’ IEEE Trans. Power Electron., vol. 34, no. 11, pp. 10610–10618, Nov. 2019.

[9] C. Gan, Q. Sun, J. Wu, W. Kong, C. Shi, and Y. Hu, ‘‘MMC-based SRM drives with decentralized battery energy storage system for hybrid electric vehicles,’’ IEEE Trans. Power Electron., vol. 34, no. 3, pp. 2608–2621, Mar. 2019.

[10] H. Cheng, Z. Wang, S. Yang, J. Huang, and X. Ge, ‘‘An integrated SRM powertrain topology for plug-in hybrid electric vehicles with multiple driving and onboard charging capabilities,’’ IEEE Trans. Transport. Electrific., vol. 6, no. 2, pp. 578–591, Jun. 2020.

[11] Y. Hu, C. Gan, Q. Sun, P. Li, J. Wu, and H. Wen, ‘‘Modular tri-port highpower converter for SRM based plug-in hybrid electrical trucks,’’ IEEE Trans. Power Electron., vol. 33, no. 4, pp. 3247–3257, Apr. 2018.

[12] H. Cheng, L. Wang, L. Xu, X. Ge, and S. Yang, ‘‘An integrated electrified powertrain topology with SRG and SRM for plug-in hybrid electrical vehicle,’’ IEEE Trans. Ind. Electron., vol. 67, no. 10, pp. 8231–8241, Oct. 2020.

[13] K.-W. Hu, P.-H. Yi, and C.-M. Liaw, ‘‘An EV SRM drive powered by battery/supercapacitor with G2V and V2H/V2G capabilities,’’ IEEE Trans. Ind. Electron., vol. 62, no. 8, pp. 4714–4727, Aug. 2015.

[14] J. Thankachan and S. P. Singh, ‘‘Bidirectional multiport solar-assisted SRM drive for pure electric vehicle applications with versatile driving and autonomous charging capabilities,’’ IET Electric Power Appl., vol. 14, no. 4, pp. 570–583, Apr. 2020.

[15] Y. Hu, C. Gan, W. Cao, Y. Fang, S. J. Finney, and J. Wu, ‘‘Solar PV-powered SRM drive for EVs with flexible energy control functions,’’ IEEE Trans. Ind. Appl., vol. 52, no. 4, pp. 3357–3366, Jul. 2016.

[16] Y. Hu, C. Gan, W. Cao, C. Li, and S. J. Finney, ‘‘Split converter-fed SRM drive for flexible charging in EV/HEV applications,’’ IEEE Trans. Ind. Electron., vol. 62, no. 10, pp. 6085–6095, Oct. 2015.

[17] H.-C. Chang and C.-M. Liaw, ‘‘Development of a compact switchedreluctance motor drive for EV propulsion with voltage-boosting and PFC charging capabilities,’’ IEEE Trans. Veh. Technol., vol. 58, no. 7, pp. 3198–3215, Sep. 2009.

[18] H.-C. Chang and C.-M. Liaw, ‘‘An integrated driving/charging switched reluctance motor drive using three-phase power module,’’ IEEE Trans. Ind. Electron., vol. 58, no. 5, pp. 1763–1775, May 2011.

[19] J. Cai and X. Zhao, ‘‘An on-board charger integrated power converter for EV switched reluctance motor drives,’’ IEEE Trans. Ind. Electron., vol. 68, no. 5, pp. 3683–3692, May 2021.

[20] V. Shah and S. Payami, ‘‘An integrated driving/charging four-phase switched reluctance motor drive with reduced current sensors for electric vehicle application,’’ IEEE J. Emerg. Sel. Topics Power Electron., vol. 10, no. 6, pp. 6880–6890, Dec. 2022.

[21] H.-C. Chen, W.-A. Wang, and B.-W. Huang, ‘‘Integrated driving/charging/ discharging battery-powered four-phase switched reluctance motor drive with two current sensors,’’ IEEE Trans. Power Electron., vol. 34, no. 6, pp. 5019–5022, Jun. 2019.

[22] V. Shah and S. Payami, ‘‘Switched reluctance motor drivetrain with fully integrated battery charger and instantaneous zero charging torque for electric transportation,’’ IEEE Trans. Transport. Electrific., vol. 10, no. 2, pp. 4529–4541, Jun. 2024.

[23] Z. Yu, C. Gan, K. Ni, Y. Chen, and R. Qu, ‘‘Dual-electric-port bidirectional flux-modulated switched reluctance machine drive with multiple charging functions for electric vehicle applications,’’ IEEE Trans. Power Electron., vol. 36, no. 5, pp. 5818–5831, May 2021.

[24] N. Bodo, E. Levi, I. Subotic, J. Espina, L. Empringham, and C. M. Johnson, ‘‘Efficiency evaluation of fully integrated on-board EV battery chargers with nine-phase machines,’’ IEEE Trans. Energy Convers., vol. 32, no. 1, pp. 257–266, Mar. 2017.

[25] V. Monteiro, J. G. Pinto, and J. L. Afonso, ‘‘Operation modes for the electric vehicle in smart grids and smart homes: Present and proposed modes,’’ IEEE Trans. Veh. Technol., vol. 65, no. 3, pp. 1007–1020, Mar. 2016.

[26] R. Krishnan, Switched Reluctance Motor Drives: Modeling, Simulation, Analysis, Design, and Applications. Boca Raton, FL, USA: CRC Press, 2017.

[27] H. D. Venable, ‘‘The K factor: A new mathematical tool for stability analysis and synthesis,’’ in Proc. Powercon, 1983, vol. 10, no. 1, p. 1.

[28] M. Xie, H. Wen, C. Zhu, and Y. Yang, ‘‘DC offset rejection improvement in single-phase SOGI-PLL algorithms: Methods review and experimental evaluation,’’ IEEE Access, vol. 5, pp. 12810–12819, 2017.

[29] R. W. Erickson and D. Maksimovic, Fundamentals of Power Electronics. Berlin, Germany: Springer, 2007.

[30] D. W. Hart, Power Electronics, vol. 166. New York, NY, USA: McGraw-Hill, 2011.

![](images/e25d05c29993020119770710c716162d3fef3082092147c788c16bb5a3537931.jpg)

T. FAHEEM ALI (Graduate Student Member, IEEE) received the B.Tech. degree in electrical and electronics engineering from the Rajiv Gandhi Institute of Technology, Kottayam, in 2013, and the M.Tech. degree in power electronics and drives from the Government College of Engineering, Kannur, in 2016. He is currently pursuing the Ph.D. degree with the National Institute of Technology Karnataka, Surathkal.

He was an Assistant Professor with the MEA

Engineering College, Malappuram, from 2016 to 2019. His research interests include power electronics, electric drives, and on-board chargers.

![](images/966fcee683f80b643c5f025678f8b59f6b37dc2a4df37e3aab1397f6f4830174.jpg)

D. ARUN DOMINIC (Member, IEEE) received the B.E. and M.E. degrees in electrical and electronics engineering from Anna University, Chennai, in 2006 and 2008, respectively, and the Ph.D. degree from Indian Institute of Technology Roorkee, in 2016, with a focus on fault tolerance control of electrical drives.

From 2008 to 2011, he was an Assistant Professor with the Loyola Institute of Technology and Science Thovalai, Kanyakumari, and Noorul

Islam University, Kumaracoil, Kanyakumari. He was also an Ad-Hoc Faculty Member with the National Institute of Technology Jalandhar from 2016 to 2018 and the National Institute of Technology Warangal from 2018 to 2019. Since 2019, he has been an Assistant Professor with the Department of Electrical and Electronics Engineering, National Institute of Technology Karnataka, Surathkal. His research interests include electrical drives, power electronics, electric vehicles, and fault tolerance control of electrical drives.

![](images/0e8ebe0a667a1d26656b33b96e4622c71c88344263ecfbe3f7aaa1f2da8e2ee6.jpg)

PRAJOF PRABHAKARAN (Senior Member, IEEE) received the B.Tech. degree in electrical and electronics engineering and the M.Tech. degree in power electronics from Amrita Vishwa Vidyapeetham (Amrita University), Coimbatore, in 2009 and 2011, respectively, and the Ph.D. degree in electrical engineering from Indian Institute of Technology Bombay, Mumbai, in 2018.

His doctoral research focused on DC microgrids. From 2011 to 2013, he was an Assistant Professor with the Electrical and Electronics Engineering Department, Amrita School of Engineering, Coimbatore. After a brief stint with the National Institute of Technology Calicut, Kozhikode, as an Ad-Hoc Faculty Member in 2018, he joined the Transportation Solutions Department, L&T Technological Services, Bengaluru, where he worked for a year as a Project Lead for the research and development of powertrain and battery management system for electric vehicle. Since 2019, he has been an Assistant Professor with the Department of Electrical and Electronics Engineering, National Institute of Technology Karnataka, Surathkal. His research interests include power electronics, renewable energy, electric vehicles, and microgrids.

![](images/9fb1488545e30ba4740f734796e0f4ace5b790d89971bce9d5e733115729f8ee.jpg)

ARUN P. PARAMESWARAN received the B.E. degree (Hons.) in electrical and electronics engineering from the College of Engineering Farmagudi, Goa University, in 2006, the M.Tech. degree from MIT Manipal, in 2008, and the Ph.D. degree in system dynamics and control from NITK Surathkal, in 2015.

He is currently an Associate Professor with the Department of Electrical and Electronics Engineering, Manipal Institute of Technology (MIT Manipal), Karnataka, India. His current research interests include system design, vibration and its active control, smart materials and their application in vibration control, analysis and control of various lowfrequency dynamics, and dynamics of biomedical devices and rehabilitation.