**Parallel-in-Time Object-Oriented Electromagnetic Transient Simulation of Power Systems**

TIANSHI CHENG (Graduate Student Member, IEEE), TONG DUAN (Graduate Student Member, IEEE), AND VENKATA DINAVAHI (Fellow, IEEE)
Department of Electrical and Computer Engineering, University of Alberta, Edmonton, AB T6G 2V4, Canada
CORRESPONDING AUTHOR: T. CHENG (tcheng1@ualberta.ca)
This work was supported by the Natural Science and Engineering Research Council of Canada (NSERC).

**ABSTRACT** Parallel-in-time methods are emerging to accelerate the solution of time-consuming problems in different research fields. However, the complexity of power system component models brings challenges to realize the parallel-in-time power system electromagnetic transient (EMT) simulation, including the traveling wave transmission lines. This paper proposes a system-level parallel-in-time EMT simulation method based on traditional nodal analysis and the Parareal algorithm. A new interpretation scheme is proposed to solve the transmission line convergence problem. To integrate different kinds of traditional EMT models, a component-based EMT system solver architecture is proposed to address the increasing model complexity. An object-oriented C++ implementation is proposed to realize the parallel-in-time Parareal algorithm based on the proposed architecture. The results on the IEEE-118 test system show 2.30x speed-up compared to the sequential algorithm under the same accuracy with 6 CPU threads, and a high parallel efficiency around 40%. The performance comparison of various IEEE test cases shows that the system’s time-domain characteristics determine the speed-up of Parareal algorithm, and the delays in transmission lines significantly affect the performance of parallel-in-time power system EMT simulations.

**INDEX TERMS** Electromagnetic transient analysis, multi-core processors, object-oriented programming, parallel-in-time, parallel processing, power system simulation.

## NOMENCLATURE
| Symbol | Description |
|---|---|
| DAE | Differential-Algebraic Equation |
| DDE | Delay Differential Equation |
| EMT | Electromagnetic Transient |
| ODE | Ordinary Differential Equation |
| $F$ | Fine Solution Operator |
| $G$ | Coarse Solution Operator |
| $U_k$ | System State Vector of k-th Iteration |
| $W$ | System of Equations |
| $\Delta t$ | Coarse-Grid Time-Step |
| $\delta t$ | Fine-Grid Time-Step |
| $n$ | n-th Discrete Simulation Time-Step |
| $\tau$ | Propagation Delay of Transmission Line |

## I. INTRODUCTION
THE electromagnetic transient (EMT) program, which simulates the temporary electromagnetic phenomena in the time domain such as voltage disturbances, surges, faults, and other transient behaviors in the power system, is essential for modern power system design and analysis [1]. The simulation often requires detailed models with high computation complexity to accommodate large-scale power systems. The algorithms of mainstream EMT tools are highly optimized using sparse matrix methods and fine-tuned power system models, but the performance is bound by the sequential programming based on the central processing unit (CPU). To get through the bottleneck, parallel computing became a popular option to speed up large-scale EMT simulation. By partitioning a large system into smaller parts, the rate of parallelism and the speed of convergence increased for nonlinear systems [2]. Both direct and iterative spatial domain decomposition were proposed to partition the system. Based on these domain decomposition methods, various parallel EMT off-line or real-time programs were implemented on different multi-core CPU, many-core graphic processing unit (GPU), field programmable gate array (FPGA), and multiprocessor systems-on-chip (MPSoCs) architectures [3]–[5]. However, few works were done on EMT simulation based on the parallel-in-time domain decomposition.

Parallel-in-time algorithms have a long history of 50 years [6], which are now widely used in many research fields to solve time-consuming simulation problems [7], [8]. In electrical engineering, parallel-in-time methods to solve power system dynamic problems were proposed in the 1990s [9]. After 1998, there had been few works on the parallel-in-time simulation until the recent 5 years. The Parareal algorithm, which solves the initial value problems iteratively using two ordinary differential equation (ODE) integration methods, has become one of the most widely studied parallel-in-time integration methods for it. In this research, the proposed simulation program has the following advantages and features:

1) Based on highly abstracted component class, the system architecture is flexible and extensible to integrate different kinds of traditional EMT models of power system equipment into the parallel-in-time algorithm and maintain all the advantages from nodal analysis;
2) Initial support for delay differential equations. With the modified interpolation strategy, the convergence speed increases so that transmission line models are able to work with the Parareal;
3) Reusing solver workers and workspace to reduce memory usage and decrease the overhead caused by object allocation in the Parareal iterations.

The paper is organized as follows: Section II describes the basics of the Parareal algorithm and implementations of EMT