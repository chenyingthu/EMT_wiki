# Multi-rate real time hybrid simulation of controllable line commutated converter based HVDC

Guoqing Li $^{\text{a}}$, Mingcheng Yang $^{\text{a,*}}$, Wei Wang $^{\text{a}}$, Guobin Jin $^{\text{a}}$, Jun Yang $^{\text{b}}$, Yahu Gao $^{\text{b}}$

$^{\text{a}}$ Key Laboratory of Modern Power System Simulation and Control & Renewable Energy Technology, Ministry of Education, Northeast Electric Power University, Jilin 132012, China  
$^{\text{b}}$ State Key Laboratory of Advanced Power Transmission Technology, China Electric Power Research Institute Co., Ltd., Beijing 102200, China

**Keywords:** Controllable line-commutated converter HVDC systems, CPU–FPGA collaborative architecture, Real-time simulation, Multi-rate simulation, Parameter optimization

**Abstract:** This paper proposes a CPU-FPGA collaborative multi-rate real-time simulation framework tailored for controllable line-commutated converter high-voltage direct current systems (CLCC-HVDC), addressing the core demands of small-time step modeling parameter optimization and high-efficiency real-time simulation for this complex hybrid topology. First, a discrete inductor decoupling method is presented that treats inductors as natural decoupling boundaries and implements topology segmentation using latency and controlled voltage sources. Second, an analytical parameter selection strategy for the associated discrete circuit model is established: the strategy decomposes the characteristic operating intervals of the CLCC converter, solves the corresponding circuit differential equations to determine the voltage and current stresses of each valve group as rated parameters, and then derives the optimal equivalent admittance based on the minimum loss error criterion. Finally, experimental verification results demonstrate that the proposed framework operates on the FPGA platform with a time step of 2 μs, achieving a normalized root mean square voltage error of less than 7% and reducing computation time by approximately 77% compared with the CPU-only offline simulation scheme. This study establishes a robust and efficient digital simulation paradigm for the verification of emerging hybrid HVDC topologies.

## 1. Introduction

High-voltage direct current (HVDC) transmission systems are increasingly important for integrating large-scale renewable energy over long distances [1]. Among converter topologies, the controllable line-commutated converter (CLCC) has emerged as a promising alternative to traditional LCCs due to improved commutation stability and cost efficiency [2]. By combining fully controlled insulated-gate bipolar transistors (IGBTs) with thyristors, CLCCs enhance controllability in weak AC networks and effectively reduce the risk of commutation failures. Furthermore, CLCC-HVDC has been applied in practical engineering, proving its effectiveness in resisting commutation failure [3].

Despite these advantages, achieving high-precision modeling of CLCC-HVDC systems remains challenging. The hybrid topology and integrated multi-semiconductor device characteristics of such systems readily induce nonlinear electromagnetic transients, coupled with complex and variable switching behavior. High-precision electromagnetic transient (EMT) simulation is crucial for verifying controller performance, testing protection strategy logic, and optimizing system topology design. However, the coupled effects of the system's multi-timescale dynamics and complex switching actions significantly increase the computational complexity and processing load of simulations. This poses challenges to the computational power and timing response capabilities of real-time simulation platforms.

Current real-time simulation methods rely primarily on multi-core CPUs or FPGAs [4,5]. Multi-core CPUs offer software flexibility but require small time steps to accurately capture switching events, increasing computational load and limiting scalability [6–9]. FPGA-based platforms offer higher processing speed and lower latency, while associated discrete-circuit (ADC)-based switch models maintain nodal admittance-matrix consistency, thereby improving real-time performance [10–13]. However, FPGA-only methods are constrained by sequential EMT algorithms and high resource consumption when modeling complex circuits [14].

To address the limitations of single-platform simulations, multi-rate co-simulation on heterogeneous processors has emerged as a promising

### Table 1
Comparison of mainstream real-time simulation platforms.

| Platform type | Advantages | Limitations | Typical applications |
|---|---|---|---|
| CPU-based [6–9] | • High flexibility and easy software modification<br>• Wide compatibility with modeling tools | • Requires a heavy computational source to capture switching transients<br>• Larger simulation step (e.g., 20–50 μs) | • EMT simulation of medium- and large-scale power networks (e.g., LCC–HVDC) |
| FPGA-based [10–14] | • High computation speed and low latency<br>• ADC-based switch models ensure nodal admittance consistency | • Limited by the sequential EMT algorithm structure<br>• High hardware resource usage<br>• Model modification requires re-synthesis | • Hardware-in-the-loop (HIL) controller testing<br>• Fast-switching converter simulation<br>• EMT simulation |

* Corresponding author. E-mail address: 1121725221@qq.com (M. Yang).  
https://doi.org/10.1016/j.ijepes.2026.111707  
Received 3 June 2025; Received in revised form 3 January 2026; Accepted 13 February 2026  
Available online 20 February 2026