# Structure Preserving Aggregation Method for Doubly-Fed Induction Generators in Wind Power Conversion
Wei Li, Member, IEEE, Iman Kaffashan, Graduate Student Member, IEEE, Aniruddha M. Gole, Fellow, IEEE, and Yi Zhang, Fellow, IEEE

**Abstract**—An aggregation method is proposed that transforms the multiple DFIGs into an equivalent DFIG model that retains the major collective dynamic characteristics of a group of DFIGs. It is intended for Electromagnetic Transients Simulation (EMT). The aggregated machine can take into account different speeds and parameters of each of the individual DFIGs and the connecting impedance of individual DFIGs. Starting with a State Variable (SV) model of an individual DFIG, aggregation is carried out recursively, by combining two DFIGs at a time and then reducing the order of the aggregate to match the state variable equations of a single DFIG so that the steady state performances are identical. Validation is carried out by comparing the detailed electromagnetic transient (EMT) simulation of the unreduced system with the reduced aggregate system. It is shown that the proposed aggregation method accurately matches the steady state response and also accurately reproduces the dominant transient response of the unreduced system. As the aggregate DFIG has the same number of state variables as a single DFIG, the overall wind farm’s order is reduced significantly to increase the modelling and simulation efficiency.

**Index Terms**—Aggregation method, DFIG, dynamic model, EMT simulation, structural preserving.

## NOMENCLATURE
| Symbol | Description |
|---|---|
| $A_{mi}, \omega_i, \alpha_{mi}$ | Amplitude, frequency and angle modulation indices of GSC |
| $A_{mo}, \omega_o, \alpha_{mo}$ | Amplitude, frequency and angle modulation indices of RSC |
| $C, v_{dc}$ | Back to back converter dc link capacitance and its voltage |
| $i_{di}, i_{qi}$ | GSC d and q-axis component current |
| $i_{dr}, i_{qr}$ | Rotor d and q-axis component current |
| $i_{ds}, i_{qs}$ | Stator d and q-axis component current |
| $L_{ls}, L_{lr}, L_m$ | Stator leakage, rotor leakage and mutual inductance of induction machine |
| $L_{s\_g}, R_{s\_g}$ | GSC side inductance and resistance |
| $L_{s\_r}, R_{s\_r}$ | RSC side inductance and resistance |
| $r_r, r_s$ | Rotor and stator resistance of induction machine |
| $R, X$ | Equivalent impedance resistance and reactance |
| $T_m, T_e$ | Prime mover and electromagnetic torque |
| $V_H, V_L, V_T$ | Three-winding transformer high, low and tertiary winding nominal voltage |
| $V_0, \theta_0$ | PCC bus voltage magnitude and angle |
| $\omega_r, \omega_s$ | Rotor and synchronous angular velocity |
| $\lambda_{dr}, \lambda_{qr}$ | Rotor d and q-axis component flux linkage |
| $\lambda_{ds}, \lambda_{qs}$ | Stator d and q-axis component flux linkage |

Manuscript received February 21, 2021; revised June 11, 2021 and October 10, 2021; accepted November 3, 2021. Date of publication November 9, 2021; date of current version May 20, 2022. This work was supported by the IRC Program of the Natural Sciences and Engineering Research Council (NSERC) of Canada. Paper no. TEC-00196-2021. (Corresponding author: Wei Li.)
Wei Li, Iman Kaffashan, and Aniruddha M. Gole are with the University of Manitoba, Winnipeg, Manitoba R3T 2N2, Canada (e-mail: wei.li2@umanitoba.ca; kaffashi@myumanitoba.ca; aniruddha.gole@umanitoba.ca).
Yi Zhang is with RTDS Technologies Inc., Winnipeg, Manitoba R3T 2E1, Canada (e-mail: yzhang@rtds.com).

## I. INTRODUCTION
Wind power is the world’s fastest growing energy source in the past decade. An even higher wind power penetration demand is expected to arrive in a near future [1]. To date, the two most widely used large scale wind energy conversion systems are the doubly fed induction generator (DFIG) and the permanent magnet synchronous generator (PMSG) [2]. Aggregation of DFIGs is the focus of this paper. The DFIG is a variable-speed wind turbine generation system, which can harness wind power with higher efficiency compared with fixed-speed systems [3]–[5]. Accumulated experience from installations over the world, demonstrates its many advantages. It increases the energy conversion efficiency, it has a large single-unit capacity and reduced mechanical stress caused by wind gusts [6]. However, modern wind farms require an expensive power converter interface to capture the maximum power from the wind at different rotor speeds [7]. Nevertheless, the power converter makes an asynchronous connection between the induction machine and the grid, and enables independent control of active and reactive power [8]. The converter only has to process the slip power in the rotor circuits, which is approximately 30% of the generator’s total power, in comparison with Type 4 generators where power electronic converters must have the full power rating [9].

The proposed aggregate DFIG model of wind farm is intended for representing the collective behavior of a group of DFIGs in a power system for steady state and dynamic behaviors. Hence the model can be used for efficient EMT simulations of several phenomena such as faults, instability, SSR and so on with a fraction of the computational resources of modelling the entire system in detail with multiple DFIGs. It is not intended for protection studies of individual DFIGs within the farm as the identity of individual machines is not retained. This is a feature desired by many system level modelers for studying very large systems. It is particularly important for real-time simulators, where hardware limitations may preclude a fully detailed representation. A large grid can have several wind farms, each with hundreds of DFIGs. If each DFIG were individually modelled in detail on an electromagnet