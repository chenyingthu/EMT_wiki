# Development and Applicability of Online Passivity Enforced Wide-Band Multi-Port Equivalents For Hybrid Transient Simulation

Abilash Thakallapelli, Student Member, IEEE, Sudipta Ghosh, Member, IEEE, and Sukumar Kamalasadan, Senior Member, IEEE

**Abstract**—This paper presents a method for developing single and multi-port Frequency Dependent Network Equivalent (FDNE) based on a passivity enforced online recursive least squares (RLS) identification algorithm which identifies the input admittance matrix in z-domain. Further, with the proposed architecture, a real-time hybrid model of the reduced power system is developed that integrate Transient Stability Analysis (TSA) and FDNE. Main advantages of the proposed architecture are, it identifies the FDNE even with unknown network parameters in the frequency range of interest, and yet can be implemented directly due to discrete formulation while maintaining desired accuracy, stability and passivity conditions. The accuracy and characteristics of the proposed method are verified by implementing on two-area, IEEE 39 and 68 bus power system models.

**Index Terms**—Electromagnetic Transient (EMT) Simulation, Transient Stability Analysis, Frequency Dependent Network Equivalent, Recursive Least Square Identification (RLS), Aggregated Generator Model (AGG).

## NOMENCLATURE

| Term | Description |
|---|---|
| EMT Model | The study and external areas are modeled as EMT type (Original model). |
| EMT+TSA | The external area is modeled as TSA type equivalent with only network aggregation. |
| EMT+TSA(AGG) | The external area is modeled as TSA type with both network and generator aggregation. |
| EMT+FDNE | The external area is modeled as FDNE type generated using the proposed algorithm. |
| EMT+FDNE (VF) | The external area is modeled as FDNE using the Vector Fitting (VF) from literature. |
| EMT+FDNE+TSA | The external area is modeled as |

## I. INTRODUCTION

REAL-TIME EMT simulation requires detailed modeling of transmission systems to understand the effect of transients and harmonics arising due to varying operating conditions and disturbances in power grid. Effect of power electronic components associated with renewable energy sources on the power grid and performance of different controllers can be analyzed using EMT simulations [1]. Typically, integration time step of EMT simulation is in microseconds (µs). This makes modeling of a large transmission system for EMT studies impractical as detail modeling increases complexity and computational burden. One solution is to model the transmission system as TSA type with larger integration time as TSA simulations can run faster than EMT. However, in TSA type, due to large integration time, high-frequency transients following a disturbance in the system are not preserved making this approach not very accurate [2].

Another approach is to model large transmission network as frequency dependent reduced order systems that can represent the power grid under any operating condition. One way to reduce large power grid is to model part of the grid which is of interest (study area) in detail and the remainder of the system (external area) by an efficient equivalent such as FDNE [3]. In this process, initially, the network is divided into study and external area based on the coherency grouping of generators such that all coherent generators are present in the external area [4]. The boundary between the study and external area is divided considering the fact that interconnecting points should have the least minimum number of ports. Generally, in TSA type equivalent, the network admittance is evaluated only at the fundamental frequency, hence this representation ignores high-frequency oscillations. The high-frequency behavior of the external area can be preserved by using FDNE [5], ho