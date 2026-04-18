# A New Model of Trapped Charge Sources in Switching Transient Studies in the Presence of Shunt Reactors

MOHSEN AKAFI-MOBARAKEH 1, REZA SHARIATINASAB 1, (Senior Member, IEEE), PIERLUIGI SIANO 2,3, (Senior Member, IEEE), BEHROOZ VAHIDI 4, (Senior Member, IEEE), AND HAMID REZA NAJAFI 1

1 Department of Electrical and Computer Engineering, University of Birjand, Birjand 9717434765, Iran
2 Department of Management and Innovation Systems, University of Salerno, 84084 Fisciano, Italy
3 Department of Power Systems, National University of Science and Technology POLITEHNICA Bucharest, 060042, Bucharest, Romania
4 Department of Electrical Engineering, Amirkabir University of Technology (Tehran Polytechnic), Tehran 1591634311, Iran

Corresponding author: Pierluigi Siano (psiano@unisa.it)

The work of Pierluigi Siano was supported in part by the Ministry of Research, Innovation and Digitalization under Project PNRR-C9-I8-760090/23.05.2023 CF30/14.11.2022.

## ABSTRACT
Insulation coordination studies are of great importance in power grid reliability. In this paper, a new method is proposed for modeling trapped charge sources (TCS) in switching transient studies. The TCS is used to take into account the voltage stored in line capacitors during reclosing operation after fault occurrence. The proposed model is designed based on the active filter concept, thus overcoming the limitations of conventional TCS for simulating transient states in EMTP/ATPDraw. Given the natural frequencies of a transmission line to which the proposed TCS (PTCS) is connected, it injects the appropriate frequencies and eliminates voltage oscillations which limit the use of TCS. To verify the efficiency of the PTCS, it is implemented in a real system with a shunt reactor, and the results are then compared with field measurements. A comparison of the results shows that the PTCS eliminates the voltage oscillations in the simulation before closing and provides a smooth voltage with the desired amplitude. Using the proposed model, the maximum line switching overvoltage is correctly calculated; this, in turn, results in a more accurate transmission line insulation design, which is technically and economically beneficial.

## INDEX TERMS
Insulation coordination, trapped charge sources, EMTP/ATPDraw, shunt reactor.

## I. INTRODUCTION
One of the major reasons behind the transmission line reliability reduction and transmission line outage, especially for voltage levels above 345 kV, is the insulation failure due to switching overvoltages [1]. Therefore, the network insulation should be designed such that the stresses caused by overvoltages are less than the allowable value. For this purpose, the amplitude and location of the maximum switching overvoltage in a transmission line should be identified. Moreover, by running transient state simulations and regarding economic considerations, a proper method should be used to reduce the associated costs [2]. In the insulation design stage, the designer should consider the worst case that may involve an open end-of-line and the trapped charge voltage. In other words, the line has to be disconnected from the feeding substation after a blackout and re-energized after a short time under no-load conditions. In [2], insulation coordination was investigated by considering switching overvoltages. In this reference, the uncertainty in the insulator response against switching overvoltage stresses was assumed to be Gaussian. Then, the statistical distribution of the maximum overvoltage stress of circuit breaker (CB) closing, caused by both the closing point uncertainty and the trapped charge, was obtained from simulation or field data. Consequently, the insulation risk of failure was calculated from the intersection of insulation stress and strength curves.

In [3] and [4], switching stresses and the resulting risk were calculated using the ANFIS neural network. In the simulations in [4], the TCS in the phases was modeled using three DC voltage sources in series with an impedance, according to [5]. In [6], the insulation coordination of the transmission line against overvoltages simultaneously driven by lightning and switching was investigated. In this study, the default ATP trapped charge model was employed, and no shunt compensation reactor was considered.

In the past, shunt reactors were employed to reduce transient overvoltages [7], but with the development of zinc oxide surge arresters, this application of shunt reactors was abandoned [8]. However, today, shunt reactors are used for steady-state voltage control [9]. Therefore, during low-load or no-load periods, the reactors are normally connected to the lines and should be considered in the transmission line energization studies [10]. In [11] and [12], studies on shunt reactors focus on transient states followed by energization and de-energization of the reactors. Although the presence of shunt reactors has an important effect on switching overvoltages, no accurate method has so far been proposed to model the worst-case switching in a line equipped with these devices. Indeed, the recorded field data have generally been considered sufficient (see [13] and [14]), and the installation of shunt reactors has been ignored in some studies ( [15] and [16]).

The purpose of this paper is to present a new model for TCS during line reclosing by using an active frequency

**TABLE 1.** Comparison with related works.
| | |
|---|---|
| *(Table content not provided in source text)* | |

**TABLE 2.** Equivalent grid impedance seen by receiving substations in the line under study [15].
| | |
|---|---|
| *(Table content not provided in source text)* | |

in Figure 1 [15]. Switching operation is performed on the transmission line SA913, as shown in Figure 2, by using the Electro-Magnetic Transients Program/Alternative Transients Program (EMTP/ATP). A 121 MVAr shunt reactor is installed at the end of the transmission line with a loss of 15%. The capacity of the reacto