# Parallelization of EMT simulations for integration of inverter-based resources

M. Ouafi^a^, J. Mahseredjian^b^, J. Peralta^c^, H. Gras^d^, S. Dennetière^a,*^, B. Bruned^a^

^a^ RTE, Jonage, France  
^b^ Polytechnique Montréal  
^c^ Chilean ISO  
^d^ PGSTech, Montreal  

**Keywords:** Electromagnetic Transient, Co-simulation, Parallel computations, multi-rate, FMI, IBR

**Abstract:** This paper presents a co-simulation tool to link multiple instances of an electromagnetic transient (EMT) simulation tool for parallel and fast computations. The tool exploits the propagation delays of transmission lines and cables to create network decoupling into several smaller sub-networks. These sub-networks are solved in parallel without approximations. A multi-rate option is also incorporated, in which the sub-networks can use different numerical integration time-steps. The Functional Mock-up Interface (FMI) is used for creating the co-simulation interface between multiple instances according to a master-slave communication scheme and the data sharing method is implemented using low-level synchronization primitives called semaphores. The interfaces between each subnetwork are automatically initialized for time-domain simulations using load-flow results.

## I. Introduction

The study of modern large electrical networks requires the modeling of massive numbers of inverter-based resources (IBRs), such as wind turbines and photovoltaics. The focus of this paper is on the detailed circuit-based electromagnetic transient (EMT) modeling and simulation of power grids with renewable energy sources. Such accurate simulations are computationally intensive and require research for accelerated solutions with maintained accuracy. The reliability of simulation results is of paramount importance, since simulation tools are used in various analysis stages required for integrating renewable energy sources. These stages have impact on construction costs, operation, reliability and maintenance of power grids.

An important challenge with EMT simulations is the computation time with power electronics components used in renewable energy sources. It constitutes a barrier to the massive establishment of EMT-type simulation tools in the power system industry. Several solutions have been proposed in the past for fast parallel computations. Well established real-time and off-line applications [1–4] are capable to simulate in parallel, using the most common decoupling method, which is based on the exploitation of natural propagation delays in transmission line (or cable) models (TLMs). The matrix solver-based approach presented in [4] uses TLM delays for parallelizing network equations only, while maintaining control system solutions in sequential mode. A co-simulation type approach is applied in [5] for exchanging network models through the cloud for simulating renewable energy sources.

It is also possible to cut networks at arbitrary locations when TLMs are not available, by using the compensation method [6,7] or state-space nodal analysis [8]. Such decoupling requires code changes in related EMT solvers, which is not the purpose of this paper.

In this paper, the purpose is to apply and test TLM based decoupling for solving in parallel complete subnetworks using the Functional Mock-up Interface (FMI) standard [9]. The target is to accelerate the computations of clusters (subnetworks) of wind and photovoltaic parks integrated into large scale power grids. The subnetworks can be executed on separate cores with their network and control system equations. The co-simulation approach is applied to execute the computational tasks of subnetworks in parallel. In the co-simulation approach each EMT-type software instance executes its subnetwork on a separate core and shares history information at each time-point, through the decoupling TLMs. One or more decoupling TLMs can be used. The FMI standard is implemented for establishing the co-simulation and the communication process is developed with low-level synchronization primitives, called semaphores.

| Component 1 | Component 2 |
|---|---|
| Master Device | Master Device |
| Master Link | Master Link |
| Buffer 1 | Buffer 1 |
| Buffer 2 | Buffer 2 |
| Slave Link | Slave Link |

The presented approach is implemented in EMTP® [10], but in fact it can be also directly implemented in any other EMT-type simulation tool. Its main advantage resides in the fact that it does not require any modification in the actual EMT-type software code by using only DLL interfacing. Which is a distinctive contribution against other existing solutions.

This work is based on initial research conducted in [11–13], by adding several improvements in actual implementation. The improvements include a new double-buffer (second co-simulation bus) scheme that guarantees data integrity during communications, simplified code structure for better efficiency, and a new multi-rate capability. Various other coding improvements have been used to accelerate computations and to generalize the proposed scheme. The complete FMI implementation has been automated to allow the automatic parallelization of selected subnetworks.

It is the first time that the proposed (FMI based) parallelization approach is tested on such large network cases with massive integration of IBRs. There are several distinctive features in this paper. Large net