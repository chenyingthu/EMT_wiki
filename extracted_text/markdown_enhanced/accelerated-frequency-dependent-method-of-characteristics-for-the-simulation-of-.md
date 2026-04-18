# Accelerated frequency-dependent method of characteristics for the simulation of multiconductor transmission lines in the time domain

Pablo Torrez Caballero$^a$, Sergio Kurokawa$^a$, Behzad Kordi$^b$

$^a$ São Paulo State University – UNESP, Ilha Solteira, Brazil  
$^b$ University of Manitoba, Winnipeg, Manitoba, Canada R3T 5V6

**Keywords:** Transmission line modeling, Electromagnetic transient analysis, Multiconductor transmission lines

**Abstract:** Simulation of transients in transmission lines can be time consuming and resource demanding when performed directly in the time domain using small time steps. This paper proposes an efficient implementation of the frequency-dependent method of characteristics. The proposed implementation exploits the circuit topology of the system to reduce the number of state equations. State-space matrices are then grouped and sparsity techniques are used to solve the system of the ordinary differential equations faster. We post-process the calculated state variables to reduce the memory usage and the number of memory accesses needed in each iteration and propose a technique to correct the error due to the time discretization of the travel time along the transmission line. To decouple the multiconductor transmission line equations, the real part of the modal transformation matrix at a fix frequency is considered. Presented results demonstrate that the proposed approach is accurate for overhead transmission lines, and significantly reduces the overall computation time and memory consumption of the model.

☆ This work was supported by the São Paulo Research Foundation – FAPESP, project 2014/17051-0 and 2017/08486-0, and by the Coordination for the Improvement of Higher Education Personnel – CAPES.  
⁎ Corresponding author. E-mail addresses: pablotorrezcaballero@gmail.com (P. Torrez Caballero), kurokawa@dee.feis.unesp.br (S. Kurokawa), Behzad.Kordi@UManitoba.CA (B. Kordi).  
https://doi.org/10.1016/j.epsr.2018.11.006  
Received 4 June 2018; Received in revised form 5 October 2018; Accepted 9 November 2018  
Available online 28 November 2018  
0378-7796/ © 2018 Elsevier B.V. All rights reserved.

## 1. Introduction

One of the most important aspects in transmission line modeling for electromagnetic transient (EMT) studies is to take into account the frequency dependence and the distributed nature of the transmission line parameters. Many simulation models have been proposed and enhanced over decades to accurately describe the frequency-dependent characteristics of multiconductor transmission lines (MTL) in the time domain.

A number of EMT-simulator-compatible models have been developed based on the method of characteristics. The method of characteristics was first applied by Bergeron to solve hydraulic problems and later by Branin [1] to simulate transients in lossless transmission lines. Subsequently, Dommel implemented the lossy, lumped-element method of characteristics into the nodal admittance matrix method, which was incorporated in the MTL models of EMTP [2]. Many enhancements were proposed to increase the performance of this model, e.g. [3,4], and more recently in [5]. The method of characteristics has been modified to include the frequency-dependence of the line parameters of a single-phase transmission line [6] and a MTL [7] by incorporating losses as lumped elements into line segments and using modal analysis.

A group of MTL models are based on the time-domain representation of the frequency-domain equations of the MTL by using convolutions [8–10]. Direct evaluation of the convolution integrals is computationally expensive. To resolve this problem, fitting techniques, e.g. Vector Fitting (VF) [11], have been employed. Fitting techniques produce rational functions that represent the frequency-domain data. These rational functions can be used to increase the performance of a model by reducing the number of operations required to evaluate the convolutions needed to solve the MTL equations directly in the time-domain [12,13,8,10]. Fitting techniques can also be used to directly represent the frequency dependence of the MTL parameters in the time domain [14]. The resulting rational functions from the fitting process can be linked to frequency independent equivalent circuits [4,15,16]. Some models take advantage of this by lumping the losses into many segments and present the resulting equations directly in the time-domain [17–19]. All models that use fitting techniques depend on the accuracy of the fitting method. Achieving higher accuracy requires a higher order of the rational function approximation which makes the simulation more complex. Therefore, high accuracy becomes expensive in terms of processing power and memory.

This paper introduces an accelerated method of characteristics that incorporates the frequency dependence of the MTL parameters and addresses the computational complexity of the cascaded method of characteristics with the fitted equivalent circuits. This is achieved by exploiting the circuit properties of the model to reduce the number of equations, assemble a global solution matrix for the system, and enhance accessing the historical current sources and correct the time discretization truncation effect. The proposed technique presented in this paper accelerates the modeling by reducing the time it needs to access the memory and by r

impedance $Z_m$.

An approach to represent frequency-dependent elements directly in the time-domain is to fit an electrical circuit that has similar frequency behavior. An equivalent circuit can be accurately determined as follows:

1. First, the circuit topology that is going to be fitted must be chosen. Two circuit topologies that represent an impedance are shown in Fig. 1. For an impedance with an inductive reactance such as $Z_m(s)$,