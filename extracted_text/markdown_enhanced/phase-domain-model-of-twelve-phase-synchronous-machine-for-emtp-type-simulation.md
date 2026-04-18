# Phase-domain model of twelve-phase synchronous machine for EMTP-type simulation

Shilin Gao a, Zhendong Tan b, Yankan Song b,∗, Ying Chen a,b, Chen Shen a,b, Zhitong Yu b  
a Department of Electrical Engineering, Tsinghua University, 100084, Beijing, China  
b Sichuan Energy Internet Research Institute, Tsinghua University, 610000, Chengdu, China  

**Keywords:** CC-PD, Constant conductance model, Electromagnetic transient simulation, EMTP, Integrated power system, PD, Phase-domain model, Twelve-phase synchronous machine  

**Abstract:** The twelve-phase synchronous machines are widely used for the power supply of integrated power systems on board. This paper formulates two phase-domain (PD)-type models of twelve-phase synchronous machines for the simulation of nodal analysis-based electromagnetic transients programs (i.e., EMTP-type simulation). The PD model for the twelve-phase machine is first formulated, which avoids the interface error in the qd0 model. It is well-suitable for the implementation in EMTP-type simulators. To further improve the simulation efficiency of a power system with twelve-phase machines, a constant conductance PD (CC-PD) model is proposed, avoiding the re-factorization of the network conductance matrix at every time-step. Test results demonstrate the accuracy and efficiency of the two proposed PD-type models for the EMTP-type solution.

## 1. Introduction

In industrial applications such as aviation, ship and electric vehicle, there are stringent demands for power density, power quality and torque ripple of power supplies, especially integrated power systems on vessels and airplanes [1,2]. In these scenarios, three-phase synchronous machines are difficult to meet the actual demand. In contrast, multi-phase machines have high power density, small torque ripple and high reliability [3,4], and are widely used in the above areas [5]. Among multi-phase machines, the twelve-phase synchronous machine is one of the most promising machines [6] and has been successfully applied to the power supply of an integrated power system on board [7].

For the twelve-phase synchronous machines, the modeling is the basis of their design, operation and control and has been an active topic of research and application. In [8], a continuous twelve-phase machine model considering magnetic coupling is formulated. In [9], a continuous state-space model of a twelve-phase machine is established and simulated in MATLAB/Simulink. To analyze the electromagnetic transient (EMT) characteristics of a power system with twelve-phase synchronous machines, the power system with twelve-phase machine models should be constructed in the nodal analysis-based EMT programs (i.e., EMTP-type programs) [10–12], which are extensively used by power engineers and researchers in industry and academia all over the world as standard simulation tools. However, there is currently no EMT model of twelve-phase machine available in the field of EMTP-type simulation. Formulating the models of twelve-phase synchronous machines for EMTP-type simulation is urgent and meaningful for the analyses of power systems with twelve-phase synchronous machines.

In the EMTP-type simulations, various kinds of three-phase machine models, such as qd0 [13], voltage-behind-reactance (VBR) [14–16] and phase-domain (PD) [17–19] models have been formulated. In the qd0 model, machines are equivalent to predicted current sources when interfaced with the network model, where numerical instability may happen. As alternatives, the VBR and PD models are directly interfaced with the network solution and are stable even with large time-steps. Following the idea of three-phase synchronous machine modeling, this paper formulates two PD-type models of the twelve-phase synchronous machine for the EMTP-type solution, which facilitates the EMT analysis of integrated power systems with twelve-phase machines. The continuous-time model for a twelve-phase synchronous machine is first derived, and the way to obtain the parameters in the phase domain is addressed. Based on this, the discretized PD model is derived for the EMTP-type solution. Then, to improve the computational efficiency of EMTP network solution with PD models, a constant conductance PD (CC-PD) model is formulated. Furthermore, aiming at improving the accuracy of the PD models in large time-step simulation, an embedded small step algorithm is proposed.

The contributions made in this paper are threefold. (1) To the best of the authors’ knowledge, this is the first time that twelve-phase synchronous machines have been modeled for the EMTP-type solution. It fills the gap in EMT simulation for an integrated power system

∗ Corresponding author.  
E-mail address: songyankan@cloudpss.net (Y. Song).  

https://doi.org/10.1016/j.ijepes.2022.108459  
Received 25 March 2022; Received in revised form 2 June 2022; Accepted 29 June 2022  
Available online 15 July 2022  
0142-0615/© 2022 Elsevier Ltd. All rights reserved.

## Nomenclature

| Symbol | Description |
|---|---|
| $\boldsymbol{\lambda}_s, \boldsymbol{\lambda}_r$ | Stator and rotor flux linkage vectors. |
| $\boldsymbol{e}_h, \boldsymbol{i}_h$ | Equivalent history voltage and current sources. |
| $\boldsymbol{i}_s, \boldsymbol{i}_r$ | Stator and |

## 2. Continuous-time model of twelve-phase synchronous machine

### 2.1. Continuous-time model of twelve-phase machine

The stator windings of a twelve-phase synchronous machine consist of four groups of three-phase windings, which are separated by an