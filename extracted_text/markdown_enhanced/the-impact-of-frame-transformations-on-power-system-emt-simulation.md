# The Impact of Frame Transformations on Power System EMT Simulation
**Jiahang Li**, Student Member, IEEE, **Yitong Li**, Member, IEEE, and **Yunjie Gu**, Senior Member, IEEE

**Abstract**—This article investigates the impact of frame transformations on the accuracy of numerical discretization in power system transient and stability studies. As analysed, frame transformations influence the convergence of the numerical discretization. Specifically, for an explicit discretization method (e.g., forward Euler method), the stability of the original system is best preserved in the frame where the system eigenvalue is closer to the origin of the complex plane, e.g., in the stationary frame for inductors and capacitors, and in the synchronous frame for $dq$-frame controllers of inverters. Simulation results are given to validate the theoretical analysis.

**Index Terms**—Power system stability, electromagnetic transients, frame transformation, numerical simulation.

*Manuscript received 22 July 2022; revised 10 December 2022; accepted 19 January 2023. Date of publication 10 February 2023; date of current version 26 December 2023. Paper no. TPWRS-01076-2022. (Corresponding author: Yitong Li.)*

Jiahang Li is with the Department of Electronic and Electrical Engineering, University of Bath, Bath BA2 7AY, U.K. (e-mail: jl3370@bath.ac.uk).

Yitong Li is with the School of Electrical Engineering, Xi’an Jiaotong University, Xi’an 710049, China (e-mail: yitong.li15@imperial.ac.uk).

Yunjie Gu is with the Department of Electrical and Electronic Engineering, Imperial College London, London SW7 2AZ, U.K. (e-mail: yunjie.gu@imperial.ac.uk).

Color versions of one or more figures in this article are available at https://doi.org/10.1109/TPWRS.2023.3242823.

## I. INTRODUCTION
NUMERICAL simulation is an important tool for power system transient stability analysis. With the increasing penetration of inverter-based resources (IBRs), electromagnetic transients (EMTs) are becoming increasingly prominent and ubiquitous in stability problems [1], [2], [3], [4], [5], [6], [7]. The resulted large-scale (very high dimensional) and stiff (multiple timescales) model poses a challenge to numerical simulation. This challenge has been recognised by system operators and simulation software suppliers. For example, National Grid, the major transmission system operator-owner in the U.K., is collaborating with PSCAD to develop a U.K.-wide EMT simulation tool [8].

There are two streams of numerical method for transient simulation: variable-step method, and fix-step method. The variable-step method is more suitable for stiff systems because this method adjusts the time step adaptively according to the minimum timescale in the system dynamics [9], [10], [11]. Fix-step method, on the other hand, uses a single time step for the entire simulation, and may be non-converging when the time step is not sufficiently small compared to the timescale of the system dynamics. That said, the fix-step method ensures fixed computation time and therefore is the unique method that can be used for real-time simulation [9], [10], [11], [12], [13], [14].

A common technique to improve the convergence of fix-step method for stiff systems is to use implicit discretization, the most well-known example of which is the trapezoidal method [9], [13], [15], [16]. In the implicit discretization, an algebraic function must be solved at each simulation step, which is known as the algebraic loop [9], [11], [17]. The algebraic loop can be easily solved for a linear system via matrix inversion. For a linear time-invariant system, the solution of the algebraic loop can be done one-off at the beginning of the simulation and does not to be repeated each step [13], [15]. For non-linear systems, solving an algebraic loop can be rather time consuming and therefore may substantially increase the simulation time [9], [11], [18]. For such non-linear systems, it is often necessary to insert extra delays to break the algebraic loop, but the extra delay may compromise convergence [13], [18], [19].

While the ongoing efforts of EMT software suppliers (e.g., PSCAD, DigSILENT, Simulink, and OPAL-RT) are largely focused on developing new discretization method for stiff systems [13], [18], [19], [20], [21], [22], [23], [24], [25], this paper takes a different perspective by investigating the effects of the reference frames on the convergence of numerical discretization. We illustrate that, by performing discretization in a proper reference frame (stationary or synchronous), an explicit (e.g., forward Euler) method can have comparable convergence to implicit methods for some EMT studies. This may resolve the dilemma between convergence and algebraic loops and provide a new way for EMT simulation of stiff inverter-based power systems.

This article is organized as follows: Section II presents a quantitative model for the discretization in the synchronous and stationary frames. Section III evaluates the convergence of the discretization in different frames. Case studies are shown in Section IV and Section V concludes the article.

## II. DISCRETIZATION WITH FRAME TRANSFORMATION
For power system modelling, three-phase current or voltage is normally transformed from ac variables in natural stationary frame (also kn