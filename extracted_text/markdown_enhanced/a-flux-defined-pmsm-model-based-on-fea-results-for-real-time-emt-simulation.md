## A Flux-Defined PMSM Model Based on FEA Results for Real-Time EMT Simulation
Dong Li a,*, Ali B. Dehkordi a,b, Yi Zhang a,b
a RTDS Technologies Inc., Winnipeg, Canada
b University of Manitoba, Winnipeg, Canada

**Keywords:** Finite element analysis, Look-up table, Permanent magnet synchronous machine, Reduced-order-model, Real time simulation

**Abstract:** To expedite the PMSM design and test process, high-fidelity PMSM model derived from Finite Element Analysis (FEA) has been studied by many researchers. This paper proposed a new approach to calculate derivatives of currents with flux linkage data, which does not require taking hours to inverse the data table. Detailed mathematical proof is reported, based on which the implementation is explained, including presenting an efficient trilinear interpolation method. Simulation stability issue in the extrapolated range is also discussed and a solution is provided. The proposed method was implemented on RTDS hardware and can run in real time with the simulation time step of less than 1 µs. The test results of the proposed model are compared with FEA and conventional lumped-parameter PMSM model. An EV powertrain test case is also used to demonstrate the new model.

*This work has been done with the financial support of RTDS® Technologies Inc.*
*Paper submitted to the International Conference on Power Systems Transients (IPST2025) in Guadalajara, Mexico, June 8–12, 2025.*
\* Corresponding author.
E-mail addresses: dong.li@ametek.com (D. Li), ali.dehkordi@ametek.com (A.B. Dehkordi), yi.zhang@ametek.com (Y. Zhang).
https://doi.org/10.1016/j.epsr.2025.112427
Received 21 October 2025; Accepted 21 October 2025
Available online 4 November 2025

## 1. Introduction
Permanent Magnet Synchronous Machines (PMSM) are widely used in various industries, due to efficiency, power density, precision, and reliability in electromechanical systems.

The inherent characteristics of magnet form, stator winding geometry, and the variable air gap length in a PMSM can lead to notable spatial harmonics, potentially influencing the machine’s performance, efficiency, and noise characteristics. In certain applications like EV powertrains, it’s crucial to take into account the impact of spatial harmonics due to their potential effects on the performance and even control behaviors [1–3]. To study the PMSM high-frequency transients, especially when interaction with power electronics and machine nonlinearity are involved, Electromagnetic Transients (EMT) type simulation is essential. However, most conventional PMSM models used in EMT simulations are lumped parameter models which ignore the effect of spatial harmonics [2]. As a result, the potential influence of spatial harmonics would be omitted in the simulation study.

On the other hand, Finite Element Method tools are widely used in machine design, due to their ability to analyze complex geometries and materials with high precision. Given a machine 2d or 3d design and excitation, Finite Element Analysis (FEA) tools can generate accurate flux distribution and torque due to any instantaneous condition, which naturally considers spatial harmonics, cogging torques and saturation effects [4–6]. However, the computation cost of FEA is heavy, thus this method is not commonly used in EMT simulation.

To take advantage of high accuracy of FEA and apply it into EMT type simulation, one way is to use co-simulation by interfacing an FEA tool and an EMT circuit simulator. However, the co-simulation is usually computationally heavy and is not suitable for real-time simulation. Authors in [7] implemented real time FEA based on additional FPGA hardware, where interfacing the FEA model with the rest of network becomes challenging. Another approach is to use FEA-based Reduced-Order-Models (ROMs) [8,9]. By using pre-computed FEA sweeping tabular data, it is possible to run a model, like PMSM, in EMT study with level of accuracy close to FEA, in a computation-cost friendly manner, even possible in real time. The accuracy depends on the granularity of the pre-computed FEA tabular data. Such model would be especially useful in control design including Hardware-In-the-Loop (HIL) studies, which has become a typical procedure in developing EV powertrain [10, 11].

With such a PMSM model that runs in real time and utilizes data generated from FEA design, the drivetrain design process can be significantly simplified. While the conventional PMSM model relying on lumped parameters obtained from test measurements and estimations of a real machine, the PMSM model derived from the FEA design could be tested with real control hardware, and accurately includes spatial harmonics, cogging torque and saturation effects without manufacturing the machine. In this way, the motor design, motor drive design, testing and optimization processes can be integrated [12].

Authors in [2] introduced the classic constant dq inductance PMSM model for real time simulation, where saturation and spatial harmonics are not included. Authors in [9] and [13] included saturation and slotting effects by using Look-Up Tables (LUTs) of pre-stored inductance matrices and excitation [17].

In this paper, a Flux-Defined PMSM (FD-PMSM) model is introduced and implemented on a real-time simulator hardware platform. Instead of inverting the LUTs to have a flux – current correlation, this paper utilized a different approach which solves the derivative of currents first to form a current – flux – current derivative correlation, which can save hours of time building the inversed LUT. This paper also provides details on implementing the proposed method including a trilinear interpolation and an extrapolation method to maximize the efficiency for real time simulation. 

**Fig. 1.** The process of using FEA results in the proposed FD-PMSM model.

The procedure also applies to some research work in the literature review but may with different LUT format and excitation.