# An FPGA based electromagnetic transient analysis of power distribution network

Swati Shukla a, *, Abhishek Agrawal b, Balbir Singh b, Gaurav Trivedi b  
a School of Energy Sciences and Engineering, Indian Institute of Technology Guwahati, India  
b Department of Electronics and Electrical Engineering, Indian Institute of Technology Guwahati, India  

**Keywords:**  
Power distribution network (PDN)  
Electromagnetic transient (EMT) analysis  
Field programmable gate array (FPGA)  

## Abstract
The electrical power distribution network (PDN) is in the transition phase due to the integration of distributed energy resources (DERs). Therefore, an accurate and efficient modeling and simulation platform is the need of the hour to determine the dynamic behavior of the PDN. The recent computational hardware, such as GPU, FPGA, etc. enables new simulation paradigm and develop a more realistic platform in the form of system emulators. In this paper, an FPGA based electromagnetic transient (EMT) simulation framework for the PDN is presented. Conjugate-gradient (CG) based electrical network solver is implemented in the proposed framework, and a test case is analyzed for Jail substation of Guwahati city, India, to validate the simulation environment. It has been compared with the MATLAB based implementation for verifying its accuracy. The proposed EMT simulator is approximately 12.5 times faster as compared to its MATLAB implementation and exhibits good accuracy as well.

## 1. Introduction
The electrical power distribution network (PDN) is evolving for the effective integration of the distributed generation (DG). In this scenario, an accurate and efficient modeling and simulation tool is desired to determine the dynamic behavior of the PDN [1]. A typical PDN mainly consists of a distribution transformer, distribution feeder, and connected load [2]. The equivalent PDN can be represented by a combination of network elements such as resistor, inductor, capacitor, etc. [2,3]. The new generation high-performance hardware accelerators such as GPU, FPGAs based simulation framework may be useful for the efficient modeling and simulation of the PDN [4,5]. The efficiency of a PDN simulation framework is evaluated by the accuracy of the PDN model and the performance of solver incorporated in the simulation environment [6]. Considerable efforts are devoted to the development of accurate PDN models and efficient solvers [7–9].

The Electromagnetic Transient (EMT) simulation is a useful tool for the design, planning, operation, and control of the PDN [6]. The EMT simulation framework with FPGA [10,11] and GPU [12] based hardware accelerator to improve computational performance is introduced. The EMT simulation framework with FPGA enables improved computational performance over GPUs as inter-processor communication imposes additional overhead time [13]. Therefore, several work on the development of FPGA based simulation framework is presented [14–17].

Another approach, in the progress of FPGA based simulator, i.e., a system on chip (SoC) implementation, is presented in [18]. The simulator performs a complete solution of the system for each simulation time step. Prior to this work, the FPGA-based simulator was based on the pre-storing the resulting inverse matrices for all possible combinations of the states of the time-variant elements. Pre-storing the possible inverse matrices limits the scope of simulation upto a few no of time-variant power system elements. Most recent FPGA based EMT simulator design approach is presented in [19]. In this work a co-simulation framework, integrating the MATLAB/Simulink based user oriented section and hardware oriented (FPGA based) computational framework is presented.

Exhaustive reflection of the literature review reveals the scope of further improvement in network matrix formulation and the development of an effective solver. The system conductance matrix generated during the PDN network analysis is sparse, Symmetric Positive Definite (SPD), but ill-conditioned. The conjugate-gradient (CG) based solver is an appropriate choice for the SPD matrix [20]. As the condition number of conductance matrix is very high; the preconditioned CG based network solver is preferred to improve the convergence.

In this paper, the EMT simulation framework for PDN with SoC-FPGA board is presented. A detailed discussion on the selection of CG based solver is presented. A preconditioned CG (PCG), based network matrix solver unit is developed. The proposed solver is developed with:
- Memory efficient storage format for sparse matrix
- Optimized matrix vector multiplication

FPGA is a programmable VLSI circuit. The underlying architecture of FPGA consists of an array of the configurable logic block (CLB), I/O block, and interconnect switch matrices, as shown in Fig. 1(a). Internally, the user-defined logic is implemented in FPGA by programming the basic logic-building units of CLB, called a logic cell (Xilinx). A logic cell usually contains function generators (4-input Look-up table), flip-flops, and multiplexers, as shown in Fig. 1(b). A Lookup table (LUT)