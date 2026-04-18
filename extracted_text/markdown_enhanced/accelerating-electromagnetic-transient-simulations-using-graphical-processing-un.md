# Accelerating electromagnetic transient simulations using graphical processing units^I, ^II, ^H

Devin Aluthge ^a, Ian Jeffrey ^a, Shaahin Filizadeh ^a,*, Dharshana Muthumuni ^b
^a University of Manitoba, Winnipeg, MB, Canada
^b Manitoba Hydro International, Winnipeg, MB, Canada

**ARTICLE INFO**
**Keywords:** EMT simulations, GPUs, Large systems, cuDSS

**ABSTRACT**
This paper explores and evaluates various approaches to accelerate Electromagnetic Transient (EMT) simulations of power systems using Graphical Processing Units (GPUs). Existing EMT simulation methods face computational challenges in systems with extensive renewable energy sources due to the complexity and switching dynamics of the system. The paper focuses on simulation methods based upon specialized GPU solvers to handle simulations of large and complicated power systems (e.g., with extensive switching components) with computational efficiency. Results from benchmark systems show significant speedups, particularly for large networks with high-frequency switching events.

^I This article is part of a Special issue entitled: ‘IPST 2025’ published in Electric Power Systems Research.
^II This work was supported by the Natural Sciences and Engineering Research Council (NSERC) of Canada, Manitoba Hydro International, Canada, and MITACS, Canada.
^H Paper submitted to the International Conference on Power Systems Transients (IPST2025) in Guadalajara, Mexico, June 8-12, 2025.
* Corresponding author. E-mail addresses: shaahin.filizadeh@umanitoba.ca (S. Filizadeh), dharshana@mhi.ca (D. Muthumuni).
https://doi.org/10.1016/j.epsr.2025.112314
Received 6 January 2025; Received in revised form 12 April 2025; Accepted 30 September 2025
Available online 14 October 2025
0378-7796/© 2025 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

## 1. Introduction

Electromagnetic Transient (EMT) simulators are necessary tools to model modern power systems [1], due to their accuracy in representing fast transients. The escalating adoption of inverter-based resources (IBRs) has resulted in significant presence of power-electronic converters leading to the erosion of system inertia and the need for EMT modeling and simulations of uncommonly large networks; this has exposed crippling computational limitations of current EMT solvers. Substantial efforts are underway to develop new algorithms, solution methods, and platforms to enable EMT simulation of exceedingly large and complex networks [2–4].

In EMT simulations node voltages are calculated using current injections as inputs to network equations. Normally these are done in sequence, resulting in computational inefficiencies. Various factorization methods, e.g., the KLU method (particularly suited for large networks) [5,6], are used to solve network equations efficiently. Sequential solutions, which have inherent computational deficiencies, can be avoided by using parallel computing. Although distributed parallel computing scales well, its communication overhead, required at each time step, drastically slows the simulation [2]. The distributed parallel model created in [2] has an exponential increment in the communication time as the number of sub-networks increases, which effectively nullifies any reduction in calculation time due to smaller sub-networks; the computational burden of EMT simulations is impacted by both the network size and complexity [3].

A shared-memory implementation of the network solution is presented in [7]; a recent study [8] introduces a parallel-in-time equation (re-)grouping technique for CPU-based parallelization with KLU factorization. Since load balancing is needed if the (re-)grouping blocks are more than the number of processors [7], an inefficient hardware scaling of shared memory implementation will occur. Otherwise, this approach might be sub-optimal when modeling practical power systems.

Perhaps the most promising approach to accelerating network simulation is the use of graphics processing units (GPUs). Specifically, the sizes of networks encountered in practice (even large networks), combined with the ability to implement the entire network solution on the GPU (eliminating communication between the host CPU and the device GPU), make GPUs well-suited to the application. While the work presented in [9] addresses basic acceleration using GPUs, it does not develop a fully-fledged GPU-based EMT solver. The authors of [10] present timing and speedup gains, using GPUs, but do not address how classical network equations can be solved efficiently, nor do they compare results to existing serial algorithms, e.g., KLU [5]. Primitive techniques, such as pre-inverting the admittance matrix [4], may enhance the simulation (serial or GPU implementation), however, switching devices, which are exceedingly common and abundant in modern power systems, pose significant challenges to such methods as the matrix needs to be altered frequently. The GPU-based pre-inversion of the matrix is shown in [4] although no comparison of KLU with direct sparse techniques is given.

This paper delves into GPU-based computations for EMT solutions, and compares the performance of several GPU and CPU-based solution methods with the aim to det

### 2.3. The Woodbury formula

The Woodbury formula [12] accounts for modifications to the $\mathbf{Y}$ matrix without inverting (or solving) the entire matrix when there is a change in the network. Assuming that $k$ entries in the admittance matrix change, the Woodbury formula can be stated as follows.

$$ (\mathbf{Y} + \mathbf{U} \mathbf{V}^T)^{-1} = $$