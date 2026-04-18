## A steady-state initialization procedure for generic voltage-source converters in electromagnetic transient simulations

**Guilherme Cirilo Leandro**\*, **Taku Noda**  
*ENIC Division, Grid Innovation Research Laboratory, Central Research Institute of Electric Power Industry (CRIEPI), 2-6-1 Nagasaka, Yokosuka, Kanagawa 240-0196, Japan*

**Keywords:** Control-system part initialization, Electromagnetic transient simulation, Heuristic procedure, Steady-state initialization, Systematic procedure, Voltage-source converter

**Abstract:** Electromagnetic transient (EMT) simulations are often performed to analyze disturbances which occur during a steady-state operation of the power grid. In modern transmission and distribution power grids, a number of voltage-source converters (VSCs) are used for renewable energy interconnections and system control. To perform EMT simulations with such VSCs, a time step of the order of microseconds is used to represent the switching operations of the VSCs. In order to avoid a prohibitively-long computation time, a steady-state initialization method is required to directly start from a steady state. This paper proposes a systematic and heuristic procedure for the steady-state initialization of generic VSCs. Using an AC steady-state solution, detailed portions in the circuit part and the control-system part of a VSC are systematically initialized. For validation, EMT simulations of a 6.6-kV distribution grid with two VSCs are performed with and without the proposed initialization procedure in this paper. Practically no transient is observed in the result with the proposed procedure, and therefore it is confirmed that directly starting from a steady state is made possible. On the other hand, the result without the proposed procedure does not reach the steady state even after continuing the EMT simulation for 300 ms.

\* This work is supported by the following electric power companies in Japan: Hokkaido Electric Power Company, Tohoku Electric Power Company, Tokyo Electric Power Company Holdings, Hokuriku Electric Power Company, Japan, Chubu Electric Power Company, Japan, Kansai Electric Power Company, Chugoku Electric Power Company, Shikoku Electric Power Company, Kyushu Electric Power Company, and Okinawa Electric Power Company.  
\*\* Paper submitted to the International Conference on Power Systems Transients (IPST2023) in Thessaloniki, Greece, June 12–15, 2023.  
\* Corresponding author. E-mail addresses: ciriloleandro3886@criepi.denken.or.jp (G. Cirilo Leandro), takunoda@ieee.org (T. Noda).  
https://doi.org/10.1016/j.epsr.2023.109404  
Received 9 December 2022; Received in revised form 2 April 2023; Accepted 8 April 2023  
Available online 4 May 2023  
0378-7796/© 2023 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/).

## 1. Introduction

Electromagnetic transient (EMT) simulations are often performed to analyze disturbances which occur during a steady-state operation of the power grid. In modern transmission and distribution power grids, a number of power-electronics converters are being used. Most of those power-electronics converters are voltage-source converters (VSCs) [1]. To perform EMT simulations of such modern power grids with VSCs, the time step needs to be in the order of microseconds to represent the switching operations of the VSCs. If the simulation was started from a zero initial condition, a prohibitively-long computation time would be required to establish a steady state. In some cases, a steady state will not be reached at all [2]. Therefore, it is essential to use a steady-state initialization method to start directly from a steady state [3,4].

Mathematically, the existing steady-state initialization methods can be classified, in general, into the following categories: time-domain methods, frequency-domain methods and hybrid time–frequency domain methods. Most of them are based on power flow calculation, and linear circuit elements can be initialized in a straightforward way based on an AC steady state obtained by a power-flow solution [4–7]. Non-linear elements can also be initialized, if the method proposed in [8] is used. Some methods can be expanded to consider harmonics [9,10]. The methods proposed in [11,12] are based on the shooting method, and therefore they involve a significant number of unknown variables for the calculation. On the other hand, the method proposed in [13] reduces the number of unknown variables by applying the chain-matrix concept to represent the VSCs. The method proposed in [14] is able to initialize a modular multilevel converter (MMC), which is a more complicated power-electronics converter. The methods above are algorithmically sophisticated and general. Since they are general, however, they involve iterative calculations requiring a relatively large amount of computations. It should be noted that some experts often implement custom-made initialization procedures based on their own heuristic knowledge to speed up the simulation.

Rather than exploiting algorithmically-sophisticated general methods, this paper proposes a heuristic but systematic procedure for the

### Nomenclature

| Symbol | Description |
|---|---|
| $V_h$, $V_{h\Delta}$ | Phase voltage at the ideal transformer primary side and its line-to-line counterpart. |
| $C_h$, $C_{h\Delta}$ | Capacitor’s capacitance for the Y-connected and the $\Delta$-connected LC filters. |
| $\theta$ | Phase angle of $\hat{V}_g$. |

## 2. Overall steady-state initialization procedure

The overall steady-state initialization procedure proposed in this paper consists of the following three stages.
- Stage 1: Positive-sequence power-flow calculation,
- Stage 2: Three-phase AC steady-state calculation, and
- Stage 3: Initialization of indi