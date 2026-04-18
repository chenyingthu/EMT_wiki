## An Interface Method for Co-Simulation of EMT Model and Shifted Frequency EMT Model Based on Estimation of Signal Parameters via Rotational Invariance Techniques
Shilin Gao, Member, IEEE, Ying Chen, Senior Member, IEEE, Zhitong Yu, Tian Cao, Graduate Student Member, IEEE, Wensheng Chen, Yankan Song, Member, IEEE, and Yuhong Wang, Senior Member, IEEE

**Abstract**—The shifted frequency-based electromagnetic transient (SFEMT) simulation is much more efficient than traditional electromagnetic transient (EMT) simulation for AC grids. This letter proposes a novel interface for the co-simulation of the SFEMT model and the conventional EMT model. The fundamentals of SFEMT modeling are first derived. Then, an interface for the co-simulation of EMT and SFEMT models is proposed based on the estimation of signal parameters via rotational invariance techniques. Theoretical analyses and test results demonstrate the effectiveness of the proposed method.

**Index Terms**—Analytical signal, co-simulation, interface, electromagnetic transient simulation, shifted-frequency simulation.

Received 28 August 2024; revised 3 January 2025; accepted 21 March 2025. Date of publication 31 March 2025; date of current version 20 June 2025. This work was supported by the Natural Science Foundation of China under Grant 52307127. Paper no. PESL-00271-2024. (Corresponding author: Ying Chen.)

Shilin Gao, Tian Cao, Wensheng Chen, and Yuhong Wang are with the College of Electrical Engineering, Sichuan University, Chengdu 610065, China (e-mail: gaoshilin@scu.edu.cn; caotiankd@stu.scu.edu.cn; chenwensheng@stu.scu.edu.cn; yuhongwang@scu.edu.cn).

Ying Chen, Zhitong Yu, and Yankan Song are with the Department of Electrical Engineering, Tsinghua University, Beijing 100084, China (e-mail: chen_ying@tsinghua.edu.cn; yuzhitong@cloudpss.net; songyankan@cloudpss.net).

Color versions of one or more figures in this article are available at https://doi.org/10.1109/TPWRS.2025.3555374.
Digital Object Identifier 10.1109/TPWRS.2025.3555374

## I. INTRODUCTION
The dynamics of a power system involve multi-scale transients. As a result, it is meaningful to develop a multi-scale simulation method that adopts different modeling methods and time steps for different subsystems. An idea of multi-rate EMT simulation, which uses large step sizes for the AC grid and small step sizes for power electronics, was proposed two decades ago.

The shifted frequency-based EMT (SFEMT) simulation with large step size is proposed for the AC power grid in [1], [2]. Then, the co-simulation interface based on SFEMT simulation and traditional EMT simulation is proposed in [3], [4], in which some subsystems of the power system are calculated by SFEMT simulation and the others are calculated by traditional EMT simulation. However, the interfaces for these co-simulation methods have a certain degree of accuracy loss. In these interfaces, the analytical signals for SFEMT simulation, which are generated from real signals in the EMT simulation, are not true analytical signals that are orthogonal to the original real signals, because these analytical signals still contain negative-frequency signal components. This will affect simulation accuracy.

To address the issues of the existing interfaces, this paper proposes a novel interface for the SFEMT and EMT models. First, the general form of SFEMT modeling is derived, giving a guideline for the design of co-simulation interface. Then, an interface based on the estimation of signal parameters via rotational invariance techniques (ESPRIT) is proposed. The ESPRIT can accurately calculate the frequency, amplitude and phase of each component in an instantaneous signal with a short data window. According to signal processing theory, once the frequency, amplitude, and phase of the original signal are known, the analytical signal required for SFEMT simulation can be constructed. The proposed interface offers better accuracy compared to existing interfaces.

The letter is organized as follows. Section II derives SFEMT modeling fundamentals. The interface of co-simulation is designed and studied in Sections III and IV. Section IV concludes.

## II. SFEMT MODELING FUNDAMENTALS
### A. General Form of SFEMT Modeling
In EMT simulation, the dynamic equation of an electrical component can be generally expressed as:
$$\frac{dx(t)}{dt} = Ax(t) + u(t) \quad (1)$$
where $x(t)$ is the state variable, $A$ is the coefficient of $x(t)$, and $u(t)$ is the input. In (1), the nonlinear part of the component dynamic is combined into $u(t)$, which is generally calculated by means of delay or prediction. For SFEMT modeling, a mathematical transformation $T[\cdot]$ (e.g., Hilbert transform) with the differential property ($T\left[\frac{dx(t)}{dt}\right] = \frac{dT[x(t)]}{dt}$) and linear property ($T[kx(t)] = kT[x(t)]$) is performed on both sides of (1) simultaneously to construct the adjoint system of (1):
$$\frac{dT[x(t)]}{dt} = AT[x(t)] + T[u(t)]$$

**Algorithm 1: ESPRIT Algorithm.**
1: Construct the Hankel matrix $X$;