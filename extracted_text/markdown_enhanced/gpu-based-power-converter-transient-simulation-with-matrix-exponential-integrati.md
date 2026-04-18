# GPU-based power converter transient simulation with matrix exponential integration and memory management

Wei Wu^a, Peng Li^a, Xiaopeng Fu^a,*, Zhiying Wang^a, Jianzhong Wu^b, Chengshan Wang^a

^a Key Laboratory of Smart Grid of Ministry of Education, Tianjin University, Tianjin 300072, China
^b Institute of Energy, School of Engineering, Cardiff University, Cardiff CF24 3AA, UK

\* Corresponding author.
E-mail address: fuxiaopeng@tju.edu.cn (X. Fu).

**Keywords:**
Electromagnetic transient simulation
Power converter
Graphics processing unit
Matrix exponential integration
Memory management

**Abstract**
With the extensive application of power electronic equipment in power systems, electromagnetic transient (EMT) simulation involving power converters becomes more challenging. Due to its multithreads and high throughput architecture, the graphics processing unit (GPU) can be used to accelerate those EMT simulations. A GPU-based matrix exponential method and its memory management for power converter transient simulation are proposed in this paper. A parallel exponential integration algorithm is established from two aspects to fully utilize the GPU multithreads capability. The matrix exponentials which are recomputed with the on/off state changes of power electronic switches are cached in GPU memory. The simulation efficiency is improved by reusing the cached data and reducing heterogeneous data transmission between CPU and GPU. Several strategies are experimented to manage the cache memory considering the EMT simulation workflow. The proposed memory management expands the simulation capability by substantially reducing the memory requirement and maintains the speed advantage of the GPU-based simulator. The proposed method is tested on wind power plants of different scales with power electronic interfaced wind generators. Simulation results indicate that the proposed method and its memory management expand the simulation capability and achieve speedups.

## 1. Introduction

With the rapid development of renewable generation integration [1], power converters are widely used in power systems to condition nonstandard AC or DC electric power for the grids and the users [2]. The precise control of converters in the microsecond scale raises the need for high-fidelity electromagnetic transient (EMT) simulations [3]. Specifically, high-frequency switching devices within the converters require detailed PWM control model and small simulation time-steps to precisely locate switching events. To accurately study the transients of the power system, the converters are required to be simulated with their detailed model [4]. However, EMT simulation of these detailed modeling systems poses challenges toward simulators from both software and hardware perspectives. Switches in power systems lead to time-varying system matrices, which become a computational bottleneck during the repeated calculation. The simulation step size limitation arises when handling the switch operations, and it becomes very inefficient for large-scale systems with long simulation timespan.

In response to these challenges, a variety of research have been conducted. Network partition methods have been proposed for decoupling the time-varying portion from the main network equation. Among them is the conventional decoupling method through propagative transmission lines that provide natural delay [5], and the more recent Multiarea Thévénin Equivalent (MATE) framework [6] and the Nested Fast and Simultaneous Solution method [7], which have theoretical roots from Diakoptics. Another trend is to relax the stringent requirement on the step sizes by exploiting the timescale property of the power systems. Multirate method decouples the power system by latency and adopts different time-steps for subsystems [8]. Dynamic average-value models (AVMs) allows larger time-steps by simplifying the model of power converter equipment. AVMs are cost-effective when switching frequency harmonics are not of concern [9]. Dynamic phasor simulation results capture the envelopes of the power system waveforms, and the step size is not limited by the power frequency [10].

Exploiting the rapid advancements of parallel computing hardware is another major aspect to address the simulation challenges. It helps to resolve the conflict between the time-consuming calculation process and the necessary simulation precision of power systems with complicated controls. Instead of processor units with higher clock rates, the increased computation power is expected to be delivered through parallelism. Coarse-grained parallel EMT simulation on multi-core CPUs was reported for realistic large grids [11]. FPGAs (Field-Programmable Gate Arrays), which are intrinsic parallel hardware with pipelined architecture, are popular in the real-time simulation scenario [12] and are included in commercial real-time simulation platforms along with other processor units [13,14]. In contrast to CPUs which are designed to optimize the performance of sequential converter states. This method presents good speedup in time-varying system simulations, especially for power systems with many high-frequency power converters.
(b) A memory management method, which updates cached data as

**Fig. 1.** A small power system example for state-space analysis.