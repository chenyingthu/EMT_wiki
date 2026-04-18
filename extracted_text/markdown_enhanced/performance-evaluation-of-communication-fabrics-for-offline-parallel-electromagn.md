## Performance evaluation of communication fabrics for offline parallel electromagnetic transient simulation based on MPI
P. Le-Huy *, S. Guérette, F. Guay
Power System Simulation group at the Hydro-Québec Research Center (IREQ), 1800 boul. Lionel-Boulet, Varennes, Québec, J3 × 1S1, Canada

✰ Paper submitted to the International Conference on Power Systems Transients (IPST2023) in Thessaloniki, Greece, June 12–15, 2023.
* Corresponding author. E-mail address: le-huy.philippe@ireq.ca (P. Le-Huy).

**Keywords:** Electromagnetic transient simulation, Large-scale simulation, MPI, Offline simulation, Parallel processing, PC cluster

**Abstract:** Offline electromagnetic transient (EMT) simulation is a very time-consuming activity for large-scale and complex power systems. Hydro-Québec (HQ) is involved in the development of EMT simulation tools, one of which can operate both in real-time (RT) and offline. This software heavily relies on parallel processing to achieve high-level performance. However, the offline mode is currently limited as it targets only single system image computers. As the offline mode uses the Message Passing Interface (MPI) standard to implement its parallel processing, porting the offline mode to PC clusters is the logical step to increase the offline simulation capabilities of HQ EMT simulation software.
This paper evaluates the performance of different communication fabrics for the execution of offline EMT simulation operating in parallel with MPI. The performance metrics used for this evaluation are first discussed. The evaluated communication fabrics are then presented and tested with an offline simulation of the HQ power transmission system.

## 1. Introduction
ELECTROMAGNETIC transient (EMT) simulation has always been considered a computationally intensive endeavor. For real-time (RT) applications, mainly control hardware-in-the-loop (HIL), parallelism was quickly adopted to divide the workload associated to a simulation on multiple processing units [1–2]. Specialized and expensive hardware was necessary, effectively making RT-HIL simulation a luxury activity reserved to a few laboratories and utilities.
As most EMT simulation tools were designed and developed prior to the wide spread of affordable multi-core CPUs, exploiting parallelism was never part of their original design goals and it impacted all technical development choices thereafter. Various efforts were recently made to exploit the multiple cores available in most PC nowadays [3–4].
In the case of Hydro-Québec’s (HQ) EMT simulation tool [2], as the offline mode is derived from the RT mode, parallel processing was already built in. It relies on the Message Passing Interface (MPI) standard [5] for inter-core communication and synchronization on a single system image computer.
As simulated systems continue to grow in both scale and complexity, the need for faster and more efficient offline simulation tools keeps increasing. As the current implementation relies on MPI and this communication mechanism is supported on PC clusters, exploring the use of clusters for offline simulation was the next logical step.
In this paper, four communication fabrics supporting MPI are evaluated for offline EMT simulation: SGI NUMAlink (NL) 7 [6], HPE Flex Grid Interconnect (FGI) [7] and Mellanox InfiniBand [8,9] ConnectX-3 Quad Data Rate (QDR) and ConnectX-6 High Data Rate (HDR). NL and FGI are interconnects that enable several motherboards, each with their own CPUs and memory, to operate as a single system where all the physically-distributed resources are shared and coherent. On the other hand, InfiniBand interconnects are used to create clusters of computers, each with their local operating system and resources. The purpose of this work is to evaluate the time cost per simulation step and the impact on EMT simulation performance of using such communication fabrics, not to evaluate the raw processing power of supercomputers/PC clusters or CPU performances.
The paper is organized as follow: Section II presents the performance metrics used in this work while Section III explores SGI and HPE communication fabrics. Section IV briefly discusses InfiniBand communication fabric and Section V describes the simulated system used to stress and evaluate each communication fabric. Results are presented and analyzed in regard to the performance metrics previously presented. Finally, Section VI concludes the paper with a summary and a description of future work.

## 2. Parallelism Quality Evaluation
Quite early, parallelism was exploited to decrease the EMT simulation execution time, mainly for the purpose of RT HIL applications. However, parallelism is not a panacea: it has a cost and presents limitations. The three following metrics (the execution speedup, the computational efficiency, and the Karp-Flatt metric) are used in this paper to evaluate the i

not monotonically increasing anymore. $\kappa'(n,1)$ is non-null and has to be considered in the measured total execution time obtained with a single processing unit.

$$T'(n, 1) = \sigma(n) + \phi(n) + \kappa'(n, 1) \tag{6}$$

It is of primary importance to use caution when directly using (6) instead of (3) in (4): if $\kappa'(n,1)$ is not negligeable, it will typically lead to artificially-increased, and even super-linear, speedups. Approximating $\sigma(n)$ and $\phi(n)$ is then mandatory for a proper performance analysis.

### 2.2. Efficiency