# A computationally efficient approach for power semiconductor loss estimation of modular multilevel converters in EMT simulations

![](images/cb80acfe7ec1d508645688db93d05ddf6103a09c82ec84692ab502836c4bb30a.jpg)

Ajinkya Sinkar a,\* , Chen Jiang b , Rohitha Jayasinghe b , Aniruddha M. Gole a

a Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB R3T 2N2, Canada

b Manitoba Hydro International, Winnipeg, MB R3R 1A3, Canada

## A R T I C L E I N F O

Keywords:   
Electromagnetic Transient (EMT) Simulations   
Modular Multilevel Converters (MMC)   
Power Loss

## A B S T R A C T

This paper presents a computationally efficient approach for estimating the power semiconductor losses of a modular multilevel converter (MMC) in electromagnetic transient (EMT) simulations. Earlier approaches required the loss estimation to be carried out at the individual IGBT-diode component level. In contrast, this paper extends this concept to the simulation of an entire MMC arm thus speeding up the simulation significantly. The proposed approach can accurately estimate the losses during steady state as well as transient operation with great speed. Furthermore, the loss estimates of each individual submodule can also be reported separately with the proposed approach, if needed. It is verified using a simulation test case of a two-terminal MMC-HVdc link and comparing the computed losses against the earlier (but much slower) approach of computing the losses at individual switch level.

## 1. Introduction

MODULAR multilevel converter (MMC) is a popular voltage source converter (VSC) topology commonly used for medium and high voltage applications due to its flexibility, scalability, modularity, and superior harmonic performance [1]. Each phase leg of an MMC consists of an upper and lower arm (as shown in Fig. 1), each of which contains stacks of series-connected submodules (SM) for generating a stepped waveform that closely resembles a sinusoidal wave [2]. Typical SMs comprise of power semiconductor switches (IGBT-diode pairs) and a capacitor as illustrated in Fig. 2. Power loss occurs in these switches in the ON state (i.e., conduction loss), the OFF state (i.e., blocking loss) and while transitioning between the ON and OFF state (i.e., switching loss). An accurate quantification of these losses under all operating scenarios (steady-state as well as transient) is essential to ensure that the switches always operate within their limits as well as for effectively designing their thermal management system [3].

For high-power applications, it is generally not feasible to evaluate these power losses experimentally [4]. Hence, one has to resort to analytical or simulation-based techniques for effectively estimating them. Several analytical approaches for loss estimation of MMCs have been proposed in the literature [5–8]. However, these approaches make a lot of simplifying assumptions and typically are not able to quantify the impact of a converter’s controls on its power losses [4].

On the other hand, simulation-based approaches can estimate the losses under a wide range of operating scenarios (steady-state as well as transient). Additionally, the impact of a converter’s controls on its power losses can also be studied [2,4]. This makes such approaches an attractive option for estimating the power losses of MMCs. Several simulation-based approaches have been proposed in the literature for estimating the losses of VSCs [9–13]. However, these approaches generally require device-level voltage and current information for estimating the losses. If applied directly for estimating the losses of an entire MMC, these methods can make the simulation computationally burdensome. This is because each switch in an MMC would need to be modelled individually in order to obtain the required device-level information. This increases the number of nodes in the simulated circuit, thereby significantly increasing the computational burden.

Modern electromagnetic transient (EMT) simulation programs typically combine an entire MMC arm into a single equivalent whose parameters in each time-step are calculated from the individual firing pulses and the initial conditions at the beginning of the time-step [14]. This approach can improve the simulation time significantly [14]. However, as the switches are not individually modelled, it is not possible to directly apply the loss estimation procedures that require device-level information (e.g., [9–13]).

![](images/46ae903569bfe589de76e03ad8c54140e5666b59948bddc7d4ca2bc476298d33.jpg)  
Fig. 1. Modular Multilevel Converter (MMC).

![](images/400fdf4c6fc4f6dc38fc20829fb95b9d24977a84192a216e19a17076db93d050.jpg)  
Fig. 2. Typical MMC Submodules.

In this paper we present a computationally efficient approach for estimating the power losses of MMCs in EMT simulations. The loss estimation is carried out using an arm-level detailed equivalent model (DEM) [14] of an MMC, thereby speeding up the overall simulation significantly. The approach proposed in [13] is utilized in this paper for estimating the power semiconductor losses. The device-level information required for this approach is obtained by coalescing the algorithm used for updating the DEM in every simulation time-step with the loss estimation approach of [13]. Note that even though an arm-level equivalent is utilized, the losses are not just estimated for the entire arm; the proposed approach also allows for reporting the loss estimates of each individual MMC submodule separately, if needed. In order to make sure that the MMC’s losses are accurately evaluated during steady state operation as well as transient conditions, an enhanced DEM [15, 16] of MMC is utilized.

The paper begins with a brief discussion of the simulation-based loss estimation approach proposed in [13]. Then, a brief review of the DEM [14–16] of an MMC is presented. The proposed approach for efficiently estimating the losses of an MMC is presented in detail after this. Finally, a simulation test case of a two-terminal MMC-based HVdc link is used for benchmarking the accuracy and computational efficiency of the proposed approach. Although the approach in this paper is discussed for an MMC that uses half-bridge SMs, it can be easily extended to other SM topologies as well.

## 2. Semiconductor Power Loss Estimation in EMT Simulations

## 2.1. Losses in Power Semiconductor Switches

Losses in power semiconductor switches can be categorized as: (i) conduction loss, (ii) blocking loss, and (iii) switching loss. Conduction loss can be easily evaluated in an EMT simulation by multiplying the device’s ON state current with its ON-state voltage drop. Similarly, blocking loss can be evaluated by multiplying the OFF-state voltage across the device with its OFF-state leakage current. The challenge lies in estimating the switching loss. EMT simulators usually model a semiconductor switch using a bivalued ON/OFF resistor [3]. However, such a simplified model by itself is not sufficient for estimating the switching loss.

## 2.2. Switching Loss Estimation in EMT Simulations

Switching loss in an IGBT-diode pair (such as the one used in MMCs – see Fig. 2) mainly consist of turn-on and turn-off losses of the IGBT as well as the reverse recovery loss of the freewheeling diode [3]. A device-level simulation model [17] of a power semiconductor switch can certainly be used for estimating its switching loss. However, such models require the use of a very small time-step (in the range of nanoseconds) for accurately capturing the switching phenomena [3]. It is generally not feasible to use such small time-steps in system-level EMT simulations (that typically use time-steps in the microsecond range) without significantly increasing the computational burden.

Reference [13] proposes an EMT simulation-based loss estimation approach that is not only accurate but also computationally efficient and simple to implement. In this approach, a device-level switch model is NOT used in the network simulation of an EMT simulation; instead, the network solution is still computed using the bivalued ON/OFF resistor model for the switches. Then, physics-based piecewise linear approximations for the waveforms of the device voltage and current (as shown in Fig. 31 ) are obtained from the (larger time-step) EMT simulation using the following:

(a). The pre- and post-switching device voltages and currents, which can be obtained from the network solution of the EMT simulation, (b). The precise time of switching (tsw) for the devices which can be obtained from EMT simulations that support interpolated switching [18,19], and (c). the information about the device’s switching performance, which can be obtained from physical tests or from its datasheet.

These waveforms are then multiplied and averaged to yield the switching loss in that time-step. The time-step can be several times larger than the switching interval (although it must be sufficiently small to capture each individual switching as a separate event) [3,13]. As the estimated waveforms adhere to the physics of the switching process, they can be used for estimating the switching loss [3]. The detailed equations used for computing the switching loss using the estimated waveforms shown in Fig. 3 are given in [13]. As the device representation in the network solution is still the simple ON/OFF resistor type, the incremental computational burden of this approach is very marginal [3,13].

A number of parameters associated with the switching performance of a semiconductor device are required for obtaining the approximated switching waveforms (as in Fig. 3) in the approach of [13]. These are given in Table 1 for the Toshiba ST1500GXH24 IGBT-diode power module [20] rated at 4.5 kV, 1.5 kA (same as the one used in [2]). Information on how to obtain these parameters can be found in [3,4,13].

![](images/33cb8fade98900e06d735ebb05bfcee82679e32a1492a83f3c005ab2988dd541.jpg)

(a) Approximated IGBT turn-on waveform  
![](images/a358b3320a02cd6d8321166938878b850dfe3e3525d1041fb351577f01a02383.jpg)

(b)Approximated IGBT turn-off waveform  
![](images/4e15aabd80bf43d9c2c526a99282057754bc5e120b5d3c5787b137bf09cc4ab0.jpg)  
(c)Approximated diode reverse recovery (turn-off) waveform  
Fig. 3. Piecewise linear switching waveforms used in the approach of [13].

Table 1  
Device parameters required for the approach of [13] (Toshiba ST1500GXH24 IGBT-diode module [20]).
<table><tr><td>Parameter</td><td>Nominal Values</td></tr><tr><td>IGBT on-state saturation voltage  $\left( V _ { c e s } \right)$ </td><td>3.0V</td></tr><tr><td>Turn-on delay  $( t _ { d ( o n ) } )$  and rise time  $\left( t _ { r } \right)$ </td><td>700.0 ns, 500.0 ns</td></tr><tr><td>Turn-on voltage tail time  $( t _ { v t a i l } )$ </td><td>2500.0 ns</td></tr><tr><td>Turn-off delay  $( t _ { d ( o f f ) } )$  and falling time (tf)</td><td>7500.0 ns,2000.0 ns</td></tr><tr><td>Turn-off voltage rise delay factor  $( k _ { o f f } )$ </td><td>0.95</td></tr><tr><td>Turn-off current tail time  $( t _ { i t a i l } )$ </td><td>2000.0 ns</td></tr><tr><td>Diode on-state saturation voltage  $\left( V _ { d s } \right)$ </td><td>3.2V</td></tr><tr><td>Diode reverse recovery time  $\left( t _ { r r } \right)$ </td><td>1000.0 ns</td></tr><tr><td>Diode reverse recovery time ratio  $( k _ { r r } )$ </td><td>0.4</td></tr><tr><td>Diode peak reverse recovery current  $\left( { { I _ { r m } } } \right)$ </td><td>1.75 kA</td></tr><tr><td>Stray inductance  $( L _ { p } )$  and capacitance  $( C _ { p } )$ </td><td>330 nH,5.0 nF</td></tr></table>

Using the estimated losses and known ambient conditions, the junction temperature of each device can also be determined. In this paper, this is done using the method proposed in [3], which solves a heat flow problem where the thermal model of the IGBT-diode module and the heat sink is represented by a lumped parameter equivalent circuit. This process is schematically illustrated in Fig. 4. The details about this can be found in [3] and are not discussed here for the sake of brevity.

![](images/2aacad3457f5d2144fcdfd50349b69d2c22cb1782acc543869b3a435328e6bee.jpg)  
Fig. 4. Schematic illustration of the approach for device loss estimation and junction temperature calculation.

![](images/12dccfaa7ff4c699964d068fb1f7aea722ea85b3919673b1c668953b6a418542.jpg)  
Fig. 5. Reduced order equivalent for an MMC arm in an EMT simulation.

## 3. Detailed Equivalent Model of MMC

## 3.1. Basic Detailed Equivalent Model (DEM)

As seen in Fig. 1, MMCs employ a large number of power semiconductor switches to facilitate the required power conversion (AC to DC or vice versa). While simulating an MMC in an EMT simulator, if each of these switches is modelled explicitly, then the simulation can become computationally onerous. To overcome this bottleneck, a detailed equivalent model (DEM) of an MMC has been proposed in the literature [14].

In this technique, firstly knowing the values of the firing pulses for each switch as well as the initial conditions at the beginning of a timestep, an SM is replaced with its Thevenin equivalent. This is possible because in an EMT simulation, the switches are typically modelled as bivalued ON/OFF resistors and the capacitor is modelled using its discrete-time companion circuit equivalent [21]. Now, as all the SMs in each MMC arm are series-connected, the entire arm can be combined into a single Thevenin equivalent (as shown in Fig. 5). This reduced-order equivalent is then utilized for computing the network solution of an EMT simulation. This drastically reduces the number of nodes in the simulated circuit, and hence makes the simulation computationally efficient [14].

Although this “basic” DEM technique is efficient, [15,16] have shown that it is accurate only under steady-state operating conditions and fails to accurately model an MMC’s behavior when it is completely blocked (i.e., when gate pulses to all SM switches are 0). To remedy this, [15,16] propose an “enhanced” DEM. This technique is briefly discussed here for the half-bridge SM case.

## 3.2. Special Considerations for Accurately Modelling Complete Blocking of the MMC bridge

During startup as well as following a dc side fault, typically an MMC is completely blocked (i.e., each SM’s IGBTs are NOT issued any gate pulses). In this case, although the IGBTs are off, their anti-parallel diodes can still conduct depending on the direction of the arm current $i _ { a r m }$ (as shown in Fig. 6). Additionally, these diodes can change their conduction state depending on the direction of $i _ { a r m }$ . A change in the direction of $i _ { a r m }$ can happen at any time (need not be at an integral multiple of the timestep). However, with the “basic” DEM of [14], these changes get constrained to occur at the integral multiples of the time-step in a fixed time-step EMT simulator, which can cause significant inaccuracies [15, 16].

References [15,16] propose an “enhanced” DEM for remedying this situation. The arm-level equivalent circuit for this approach for an MMC comprising of half-bridge SMs is as shown in Fig. 7. In this, the basic DEM obtained from internal node collapsing using the approach of [14] (shown in the red dotted box in Fig. 7) is augmented with two extra

![](images/f83ed0f08e6fb6e5f3bb2a8e55bb554b98328aff6524440e251635e0a61736fe.jpg)  
Fig. 6. Half-bridge SM - Possible conduction paths when completely blocked.

![](images/e5c8972b6fdbfaabbd91e91178a1139f662c7f5e769bb0d736ee55f015849e4c.jpg)  
Fig. 7. Enhanced DEM for a half-bridge SM-based MMC.

IGBTs $( \mathrm { T _ { e q 1 } }$ and $\mathrm { T _ { e q 2 } } )$ and a diode $\mathrm { ( D _ { e q 1 } ) }$ . These extra switching elements must support interpolated switching [18,19] in a fixed time-step EMT simulator so that the transitions in between time-steps between the scenarios shown in Fig. 6 can be modelled accurately [16].

## 4. Efficiently Estimating the Power Loss of MMC

The approach proposed in [13] has been shown to provide reliable loss estimates through EMT simulations for various voltage source converter topologies, including the MMC [2,4,13]. However, as discussed in Section ${ \mathrm { I I } } ,$ it requires device-level information obtained from the network solution of an EMT simulation for estimating the losses. If this approach is used directly for estimating the losses of an entire MMC, it would require modelling each switch in an MMC individually for obtaining the required device-level information. This increases the number of nodes in the simulated circuit and thus makes it computationally burdensome. An arm-level DEM of an MMC has been shown to significantly improve the computational efficiency of an EMT simulation [14–16]. However, the device-level information required for the loss estimation is not directly available in this case as all internal nodes of an MMC arm are eliminated. Thus, directly applying the loss estimation approach of [13] with a DEM is not possible.

Based on the discussion in Section III, we know that the parameters $R _ { T H }$ and $V _ { T H }$ of a DEM (seen in Fig. 7) can change in every simulation time-step and are determined by knowing the following at the beginning of each time-step: (i) the firing pulses for each switch, which come from the converter’s controls, and (ii) the initial conditions. These initial conditions are each SM’s node voltages and branch currents, which are computed in every time-step internally while updating the arm-level DEM. Knowledge of these initial conditions along with the ON/OFF status of each switch and the device parameters (like those given in Table 1) is sufficient to obtain the approximated switching waveforms (as given in Fig. 3) and thereby estimating the power loss.

Thus, a computationally efficient way of estimating the power semiconductor losses of an MMC is by coalescing the loss-estimation approach of [13] with the algorithm used for deriving the DEM in every time-step, as illustrated in Fig. 8. As this approach utilizes the

DEM, it estimates the losses of an MMC without penalizing the computational efficiency of the simulation. The details of how the loss estimation can be carried out using each SM’s initial conditions as well as the ON/OFF status of the switches is illustrated in the flowchart2 of Fig. 8. To ensure that MMC’s losses are accurately evaluated during normal operation as well as when it is completely blocked, the enhanced DEM $[ 1 5 , 1 6 ]$ discussed in Section III.B is utilized and the flowchart shown in Fig. 8 is also divided accordingly (i.e., one part (blue) that estimates the losses under normal operation whereas the other part (red) that estimates them when the MMC is completely blocked). The nomenclature used for the different switching elements (i.e., IGBTs, diodes) and the firing pulse signals $( \mathrm { F P _ { 1 } } ,$ FP2) in the flowchart of Fig. 8 is based on that in Figs. 6 and 7. Note that as seen from Fig. 8, the loss estimates of each individual submodule are separately computed and can be made available to the user, if required.

## 4.1. Obtaining the required device-level information

As discussed in Section II.B, the approach of [13] requires two pieces of device-level information from the network solution of an EMT simulation in each time-step to estimate the power losses. These are: (i) the pre- and post-switching device voltages and currents, and (ii) the time of switching $( t _ { s w } )$ for the devices. The prior can be obtained from the internal node voltages and branch currents computed for each SM when the DEM is updated at the beginning of each simulation time-step, while the latter can be obtained in the case of a DEM, as explained below:

Normal Operation (BLK = 0):

In the enhanced DEM of Fig. 7, during normal operation the IGBT $\mathrm { T _ { e q 2 } }$ is always OFF (as BLK = 0) whereas the $\mathrm { I G B T ~ T _ { e q 1 } }$ and the diode $\mathrm { D _ { e q 1 } }$ conduct based on the direction of the arm current $i _ { a r m } .$ Therefore, the arm-level equivalent circuit is the same as the basic DEM given in Fig. 5.

In the case of the basic DEM, by knowing the values of the firing pulses of each SM’s switches at the present and the previous time-step as well as the direction of $i _ { a r m } ,$ the status of these switches at the present time-step can be accurately inferred. Then using these as well as the known status of the switches at the previous time-step, the time of switching $( t _ { s w } )$ for each SM’s switches can be computed.

Complete Blocking Scenario (i.e., BLK = 1):

When the MMC bridge is completely blocked, each SM can be in either one of the states that are shown in Fig. 6. Moreover, the transition between these two states can happen at any time. This fact is modelled accurately in the enhanced DEM of Fig. 7 by having the extra IGBTs $( \mathrm { T _ { e q 1 } }$ and $\mathrm { T _ { e q 2 } } )$ and diode $\mathrm { ( D _ { e q 1 } ) }$ support interpolated switching $[ 1 8 , 1 9 ]$ Additionally, IGBT $\mathrm { T _ { e q 1 } }$ is always OFF (as BLK = 1) whereas the IGBT $\mathrm { T _ { e q 2 } }$ and the diode $\mathrm { D _ { e q 1 } }$ conduct based on the direction of the arm current $i _ { a r m }$

When $\mathrm { D _ { e q 1 } }$ conducts, the behavior shown in Fig. 6 (a) is modelled whereas when $\mathrm { T _ { e q 2 } }$ conducts, the behavior shown in Fig. 6 (b) is modelled for the overall MMC arm. Therefore, using the switching times of $\mathrm { D _ { e q 1 } }$ and $\mathrm { T _ { e q 2 } } ,$ , the precise times of switching can be obtained for each SM’s diodes $\mathrm { D } _ { 1 }$ and $\mathrm { D } _ { 2 } ,$ respectively under the complete blocking scenario.

## 5. Validation Test Case

In order to validate the proposed approach, we consider a simulation test case consisting of a two-terminal MMC-HVdc link as shown in Fig. 9. The system is rated at 180 MW, ± 75 kV and the converters at each end have 50 half-bridge SMs per arm with a nominal SM voltage of 3 kV. Both ends are interconnected using two 200 km overhead transmission lines which are modelled using the frequency dependent model [22]. The IGBT-diode module used in each SM of the MMC bridges is assumed to be the Toshiba ST1500GXH24 [20] rated at 4.5 kV, 1.5 kA (same as the one used in [2]).

![](images/2af029724156105c042de1ffc80b2497a22219973c4e9f6144fbf0c88a612dcb.jpg)  
Fig. 8. The proposed approach for efficiently estimating the power semiconductor losses of an MMC comprising of half-bridge SMs.

![](images/b0e0470f534bc78f8b89cdb17dd05dc9a27d3d5680a6f0f33eb69ea99b54ff97.jpg)  
Fig. 9. Two-terminal MMC-HVdc test system.

Each converter is controlled using the decoupled dq-control strategy [23]. The rectifier end controls the dc-side voltage $( V _ { d c } )$ and the ac-side reactive power $( Q _ { r e c t } ) _ { : }$ , while the inverter end controls the ac-side active power $( P _ { i n \nu } )$ and reactive power $( Q _ { i m } )$ . Nearest-level control (NLC) is utilized for submodule switching. A circulating current suppression controller (CCSC) is also included to eliminate the second harmonic component in the MMC’s circulating current.

For validating the accuracy of the loss estimates obtained using the proposed approach during steady state as well as transient operation, we consider two scenarios:

(A). Start-up of the MMC-HVdc link.

(B). A pole-to-pole fault at the midpoint of the dc line.

In each of these cases, the loss estimates obtained for the rectifier end MMC using the proposed approach are compared against those obtained from a detailed switching model (DSM) of the rectifier end MMC bridge where each switch is modelled individually. Parameters required for the loss estimation for the ST1500GXH24 IGBT-diode module are given in Table 1. The simulations are carried out in PSCAD/EMTDC with a timestep $\Delta t = 1 0 \ \mu s .$

## 5.1. Start-up of the HVdc link

Before starting the HVdc link, both the MMCs are completely blocked $( \mathrm { i . e . } ,$ , the gate pulses to all SM switches are 0) and all the ac breakers (viz. $\mathrm { B R K } _ { \mathrm { G 1 } }$ , BRK1, BRKP1, BRKG2, BRK2 and $\mathrm { { B R K } _ { P 2 } ) }$ are kept open. In order to gracefully start the link, the following start-up sequence is adopted:

1). $\mathrm { A t } ~ t = 0 . 1 ~ \mathsf { s } , ~ \mathsf { B R K } _ { \mathrm { G 1 } }$ and $\mathrm { B R K } _ { \mathrm { G 2 } }$ are closed to energize the converter transformers on both sides.

2). At $t = 0 . 2 \ s , \ \mathrm { { B R K } _ { P 1 } }$ and $\mathrm { B R K } _ { \mathrm { P 2 } }$ are closed to pre-charge the SM capacitors in each of the MMC bridges.

3). At $t = 2 . 2 \ s , \ \mathrm { B R K _ { 1 } }$ on the rectifier side is closed to bypass the BRKP1 branch.

4). $\mathrm { A t } ~ t = 2 . 7 ~ \mathrm { s } ,$ BRK2 on the inverter side is closed to bypass the BRK branch.

5). At $t = 3 \ \mathsf { s } ,$ the rectifier end MMC bridge is deblocked to charge the HVdc link to its rated voltage $( \mathrm { i . e . , \pm 7 5 \ k V } )$

6). At $t = 3 . 5 s ,$ the inverter end MMC bridge is deblocked and the active power $( \mathbf { P } _ { \mathrm { i n v } } )$ is linearly ramped-up at the rate of 200 MW/s to the rated value (i.e., 180 MW).

Figs. 10–13 depict the loss estimates (viz. conduction loss, blocking loss, switching loss and total power loss) as a function of time in the rectifier end MMC bridge obtained using the proposed approach. This is compared with the loss estimates obtained using a DSM for the rectifier end MMC bridge in the same plots (Figs. 10–13). Fig. 14 shows the rectifier end active power $( P _ { r e c t } )$ for the two cases.

![](images/e5ce4bc1940ad02332b325bf129d31330e73792194419ed909bf7502bb2c5cb9.jpg)  
Fig. 10. Total conduction loss $( P _ { L o s s ( c o n d ) } )$ in the rectifier-end MMC bridge.

![](images/82f42854e9530e76ddb1d8d2192826e7e59b5cd79aecae05b6d6a312ba4cf32c.jpg)  
Fig. 11. Total blocking loss $( P _ { L o s s ( b l o c k ) } )$ in the rectifier-end MMC bridge.

![](images/5dddcbc7f7568835955d0fe8ac898b5f1b4bc5f7afd120b42003b116a591193a.jpg)  
Fig. 12. Total switching loss $( P _ { L o s s ( s w i t c h ) } )$ in the rectifier-end MMC bridge.

![](images/21e032ee894a3ac7d9edb19f5fcd6c488e54911f7a428a93864ee58c8ec66259.jpg)  
Fig. 13. Total loss $( P _ { L o s s ( t o t ) } = P _ { L o s s ( c o n d ) }$ + $P _ { L o s s ( b l o c k ) } + P _ { L o s s ( s w i t c h ) } )$ in the rectifierend MMC bridge.

![](images/3bc35ae3620b383f90d09ac83fca19017cad4cc26a0017224a01a1e609d33ecc.jpg)  
Fig. 14. Rectifier-end active power $( P _ { r e c t } ) .$

The plots in Figs. 10–13 show that the loss estimates obtained using the two approaches match very closely while starting-up the link as well as in steady state. Thus, this validates the accuracy of the loss estimates obtained using the proposed approach.

## 5.2. Dc side fault

In this case, the HVdc link is initially assumed to be operating in steady state with rated power $( \mathrm { i . e . , P _ { i n v } = 1 8 0 ~ M W } )$ being transferred. ${ \mathrm { A t ~ } } t = 4 \ s ,$ a pole-to-pole dc fault is applied at the mid-point of the transmission line. In order to protect the IGBT switches, the dc fault clearing procedure shown in Fig. 15 is followed [16].

The pick-up value $( \mathrm { i } _ { \mathrm { p i c k } } )$ for the MMC arm current $\mathrm { ( i _ { a r m } ) }$ for the dc fault detection in Fig. 15 is taken to be the rated current (i.e., 1.5 kA) of the ST1500GXH24 IGBT-diode module. In this case as well, the loss estimates (viz. conduction loss, blocking loss, switching loss and total power loss) in the rectifier end MMC bridge obtained using the proposed approach are compared with those obtained using a DSM for the rectifier end MMC bridge. These comparisons are shown in Figs. 16–19. Additionally, Fig. 20 shows the rectifier end active power $( P _ { r e c t } )$ for the two cases.

![](images/dcfd61e819418a4d42b9d338831945ea2d42de2e7f16f3f4d91bd2174a98c822.jpg)  
Fig. 15. Dc fault detection and clearing procedure.

For this case as well, the loss estimates obtained using the two approaches match very closely not only during steady state but also

![](images/3b02b7d23429090e0ab3f999551720b64863162436937647d536aaef26e0bd00.jpg)  
Fig. 16. Total conduction loss $( P _ { L o s s ( c o n d ) } )$ in the rectifier-end MMC bridge.

![](images/67bf01f735091fd53e698c551bbe3c3df12abc53e3e4d29699a24a5c20386af7.jpg)  
Fig. 17. Total blocking loss $( P _ { L o s s ( b l o c k ) } )$ in the rectifier-end MMC bridge.

![](images/53720d587d272686644d0fe51426c1eea6d4cd57b9fb2be794f62d760424aa1b.jpg)  
Fig. 18. Total switching loss $( P _ { L o s s ( s w i t c h ) } )$ in the rectifier-end MMC bridge.

![](images/8e95214ab0cd28b0132cc6f3dd812b5f12aa61d7ef922335c651da0d1f351424.jpg)  
Fig. 19. Total loss $( P _ { L o s s ( t o t ) } = P _ { L o s s ( c o n d ) } + P _ { L o s s ( b l o c k ) } + P _ { L o s s ( s w i t c h ) } )$ in the rectifierend MMC bridge.

![](images/ee1044bb5380bd67f71f331a6cc51886ba3f3add680910ef951d0b7ca9a12482.jpg)  
Fig. 20. Rectifier-end active power $( P _ { r e c t } ) .$

Table 2  
Comparison of CPU Times.
<table><tr><td>Using DEM (Proposed Approach)[T1]</td><td>Using DSM (Earlier Approach)[T2]</td><td>Speedup Factor [T2/T1]</td></tr><tr><td>196 s, (3 min. 16 s)</td><td>8646 s,(~ 2 hr. 24 min.)</td><td>44.1</td></tr></table>

following a dc side fault, thus validating the accuracy of the proposed approach.

## 5.3. CPU Time comparison

Table 2 gives the CPU time for a simulation which uses the proposed approach and compares it with that for a simulation which uses the earlier approach of estimating the losses at individual switch level (i.e., using DSM). These results are obtained for a 10 s simulation with Δt = 10 μs. The platform used is a general-purpose Intel i7-8700 based Windows 11 PC having 6 physical cores running at 3.2 GHz.

These results show that the proposed approach is able to speed up the loss estimation process by a factor of 44. This clearly demonstrates the superior computational efficiency of the proposed approach for estimating the power semiconductor losses of an MMC as against the earlier approach of estimating them at the individual IGBT-diode component level.

## 6. Conclusion

In this paper, we present a computationally efficient approach for estimating the power semiconductor losses of an MMC in EMT simulations. The proposed approach coalesces the loss estimation procedure (previously used at individual IGBT-diode component level) with a detailed equivalent model of an MMC arm in order to efficiently estimate the MMC’s losses without the need to model each of its switch explicitly. Nevertheless, the proposed approach still allows for reporting the loss estimates of any individual submodule, if required. It is able to estimate the losses during normal operation as well as when the MMC is completely blocked.

A simulation test case of a two-terminal MMC-based HVdc link shows that the proposed approach is able to not only provide accurate and reliable loss estimates, but it also speeds up the loss estimation process significantly as compared to the earlier approach of estimating the losses at individual IGBT-diode component level. Although the approach proposed in this paper is discussed in the context of an MMC using halfbridge SMs, it can easily be extended to other SM topologies as well.

## CRediT authorship contribution statement

Ajinkya Sinkar: Writing – review & editing, Formal analysis, Software, Investigation, Conceptualization, Methodology, Validation, Writing – original draft. Chen Jiang: Software, Writing – review & editing, Investigation, Validation, Methodology. Rohitha Jayasinghe: Resources, Supervision, Funding acquisition, Writing – review & editing, Software, Project administration. Aniruddha M. Gole: Supervision,

Resources, Funding acquisition, Methodology, Writing – review & editing, Project administration, Conceptualization.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Funding

This work was in part supported by the IRC program of NSERC, Canada and in part by MITACS Elevate Program, Canada under Grant IT40444.

## Data availability

Data will be made available on request.

## References

[1] G. Li, J. Liang, Modular multilevel converters: recent applications [History], IEEE Electrif. Mag. 10 (3) (2022) 85–92. Sept.

[2] U. Gnanarathna, A. Gole, A. Rajapakse, and S. Chaudhary, “Loss estimation of modular multi-level converters using electr-magnetic transients simulation,” presented at the International Conference on Power System Transients (IPST) 2011, Delft, The Netherlands, 2011.

[3] A. Rajapakse, A. Gole, P. Wilson, Electromagnetic transients simulation models for accurate representation of switching losses and thermal performance in power electronic systems, IEEE Trans. Power Deliv. 20 (1) (2005) 319–327. Jan.

[4] X. Shi, S. Filizadeh, D. Jacobson, Loss evaluation for the hybrid cascaded MMC under different voltage-regulation methods, IEEE Trans. Energy Convers. 33 (3) (2018) 1487–1498. Sept.

[5] C. Oates and C. Davidson, “A comparison of two methods of estimating losses in the Modular Multi-Level Converter,” in Proceedings of the 2011 14th European Conference on Power Electronics and Applications, 2011, pp. 1–10.

[6] P. Jones and C. Davidson, “Calculation of power losses for MMC-based VSC HVDC stations,” in 2013 15th European Conference on Power Electronics and Applications (EPE), 2013, pp. 1–10.

[7] M. Zygmanowski, B. Grzesik, M. Fulczyk, and R. Nalepa, “Analytical and numerical power loss analysis in Modular Multilevel Converter,” in IECON 2013 - 39th Annual Conference of the IEEE Industrial Electronics Society, 2013, pp. 465–470.

[8] L. Bieber, L. Wang, J. Jatskevich, Numerically efficient and accurate analytical converter semiconductor loss calculation for hybrid and modular multilevel

converters in VSC-HVDC applications, IEEE Open Access J. Power Energy 11 (2024) 493–507. Sept.

[9] F. Blaabjerg, U. Jaeger, S. Munk-Nielsen, and J. Pedersen, “Power losses in PWM-VSI inverter using NPT or PT IGBT devices,” in Proceedings of 1994 Power Electronics Specialist Conference - PESC’94, 1994, vol. 1, pp. 434–441.

[10] C. Wong, EMTP modeling of IGBT dynamic performance for power dissipation estimation, IEEE Trans. Ind. Appl. 33 (1) (1997) 64–71. Jan. - Feb.

[11] S. Munk-Nielsen, L. Tutelea, and U. Jaeger, “Simulation with ideal switch models combined with measured loss data provides a good estimate of power loss,” in Conference Record of the 2000 IEEE Industry Applications Conference. Thirty-Fifth IAS Annual Meeting and World Conference on Industrial Applications of Electrical Energy (Cat. No.00CH37129), 2000, vol. 5, pp. 2915–2922.

[12] Y. Xu, C.N.M. Ho, A. Ghosh, D. Muthumuni, An electrical transient model of IGBTdiode switching cell for power semiconductor loss estimation in electromagnetic transient simulation, IEEE Trans. Power Electron 35 (3) (2020) 2979–2989. Mar.

[13] A. Rajapakse, A. Gole, R. Jayasinghe, An improved representation of FACTS controller semiconductor losses in EMTP-type programs using accurate loss-power injection into network solution, IEEE Trans. Power Deliv. 24 (1) (2009) 381–389. Jan.

[14] U. Gnanarathna, A. Gole, R. Jayasinghe, Efficient modeling of modular multilevel HVDC converters (MMC) on electromagnetic transient simulation programs, IEEE Trans. Power Deliv. 26 (1) (2010) 316–324. Jan.

[15] F. Ajaei, R. Iravani, Enhanced equivalent model of the modular multilevel converter, IEEE Trans. Power Deliv. 30 (2) (2015) 666–673. Apr.

[16] J. C. G Alonso, S. Howell, and K. Abdel-Hadi, “Half-bridge and H-bridge equivalent MMC models for EMT simulation,” presented at the International Conference on Power System Transients (IPST) 2019, Perpignan, France, 2019.

[17] T. Mizoguchi, Y. Sakiyama, N. Tsukamoto, and W. Saito, “High accurate IGBT/ IEGT compact modeling for prediction of power efficiency and EMI noise,” in 2019 31st International Symposium on Power Semiconductor Devices and ICs (ISPSD), 2019, pp. 307–310.

[18] G. Irwin, D. Woodford, and A. Gole, “Precision simulation of PWM controllers,” presented at the International Conference on Power System Transients (IPST) 2001, Rio de Janeiro, Brazil, 2001.

[19] M. Zou, J. Mahseredijian, G. Joos, B. Delourme, and L. Gerin-Lajoie, “Interpolation and reinitialization for the simulation of power electronic circuits,” presented at the International Conference on Power System Transients (IPST) 2003, New Orleans, USA, 2003.

[20] “Toshiba ST1500GXH24 Silicon N-channel IEGT datasheet.” [Online]. Available: https://www.digchip.com/datasheets/parts/datasheet/2/487/ST1500GXH24-pdf. php. Accessed: 25 Dec, 2024.

[21] H. Dommel, Digital computer solution of electromagnetic transients in single-and multiphase networks, IEEE Trans. Power Appar. Syst. 88 (4) (1969) 388–399. PAS-Apr.

[22] A. Morched, B. Gustavsen, M. Tartibi, A universal model for accurate calculation of electromagnetic transients on overhead lines and underground cables, IEEE Trans. Power Deliv. 14 (3) (1999) 1032–1038. Jul.

[23] A. Yazdani, R. Iravani, Voltage-sourced Converters in Power Systems: Modeling, Control, and Applications, John Wiley & Sons, 2010.