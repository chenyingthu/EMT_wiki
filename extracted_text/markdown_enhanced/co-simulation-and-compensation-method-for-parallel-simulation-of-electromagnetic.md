## Co-simulation and compensation method for parallel simulation of electromagnetic transients
Boris Bruned $^{a,*}$, Mehdi Ouafi $^{a}$, Jean Mahseredjian $^{b}$, Sébastien Dennetière $^{a}$  
$^{a}$ RTE, Campus Transfo, Jonage, France  
$^{b}$ Polytechnique Montréal, Canada  

**Keywords:** Electromagnetic transient, Co-simulation, Parallel computations, Compensation method, FMI  

**Abstract:** This paper introduces a co-simulation tool designed to parallelize the computation of electromagnetic transients (EMTs) using the Compensation Method (CM). The CM is a delay-free parallel technique that allows decoupling network equations anywhere while maintaining accuracy. It overcomes limitations in the delay-based (transmission line model delay) approach which cannot be used directly in several cases, without inserting artificial delays that can cause accuracy deterioration. It is generalized to the Modified Augmented Nodal Analysis (MANA) formulation. The Functional Mock-up Interface (FMI) is used for creating the co-simulation interface. The CM is automatically initialized from load-flow. To handle discontinuities, an adaptative time-step and order CM has been implemented. This generic and scalable co-simulation implementation of CM achieves substantial performance gains on networks with inverter-based resources (IBRs), enabling parallel EMT simulations up to six times faster.  

## 1. Introduction  
In the scope of modern energy transition, more and more power electronics converters are installed on the grid for the integration of renewable energy resources. Electromagnetic transient (EMT) type modelling is required to study the impact of inverted-based resources (IBRs) on network stability and performance. The computation time of EMT simulations can become a bottleneck. Parallelization is a key technique to speed up EMT simulations with multi-core computers.  

The basic parallel decoupling approach is delay-based. It relies on the natural propagation delay of transmission line models (TLMs) to decouple network equations. Firstly, it has been widely implemented in real-time EMT simulation tools [1,2] where performances are constrained due to hardware communication. Then, it has been developed for offline simulation tools [3–5]. The co-simulation technique used in [3,5] has proven to be an efficient method for parallelizing existing serial codes, offering a scalable solution that accelerates the simulation process.  

However, for networks with IBRs, TLM delays are not always available for parallel TLM decoupling. Fictitious delays can be used to emulate TLM propagation and to allow decoupling, but such delays may significantly deteriorate accuracy or even become inapplicable. To maintain accuracy, it is possible to apply delay-free decoupling techniques. Some implementations have been proposed for the real-time environment [6–10]. The compensation method (CM) [11,12] is one of these delay-free techniques. Decoupling can be applied anywhere in the network while maintaining accuracy. Other denominations of this techniques can be found in the literature [13,14]. Recent implementation [9,10] has shown promising performance gains for real-time EMT simulations.  

This paper proposes a new implementation of the CM for offline EMT simulations through co-simulation. The co-simulation interface, based on the Functional Mock-up Interface (FMI) [15], is inspired by previous work [5,16] where it has been applied for TLM delay-based decoupling. It has demonstrated good scalability and performance. The master-slave communication scheme on shared-memory is kept and adapted to CM inter-time-point communication which involves data exchange, such as Thevenin equivalents and branch currents for compensation. The co-simulation CM is implemented in EMTP® [17]. The proposed implementation is generic and can be applied to any other EMT simulation tool that embeds a co-simulation interface.  

This paper proposes the following contributions, which enhance previous CM implementation [9,10]:  
1. A generalization of CM to modified augmented nodal analysis (MANA) formulation [17,18], which uses an iterative solver for nonlinear models.  
2. A generic scalable co-simulation implementation of CM.  
3. Automatic initialization of CM using load-flow results.  
4. An adaptative time-step and order CM to handle discontinuities [19].  

The new co-simulation CM is validated on practical power grids.  

The structure of this paper is as follows. Firstly, in Section 2, the theoretical foundation of the Compensation Method (CM) based on the  

$$\hat{A}^{(k)} = J^{(k)}$$  
$$B^{(k)} = J^{(k)} x^{(k)} - F(x^{(k)}) \quad (6)$$  

The solution of nonlinear networks used in [18] is based on linearization where each nonlinear device provides a linearized Norton equivalent. In this approach, the matrix $A$ is the Jacobian matrix of network equations. At each iteration, solving Eq. (5) is equivalent to solve Eq. (3).