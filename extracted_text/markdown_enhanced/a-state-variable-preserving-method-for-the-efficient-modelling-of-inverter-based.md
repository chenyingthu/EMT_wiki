Received: 22 October 2024 | Revised: 3 January 2025 | Accepted: 20 January 2025
DOI: 10.1049/gtd2.70013

ORIGINAL RESEARCH

# A state-variable-preserving method for the efficient modelling of inverter-based resources in parallel EMT simulation

Qiguo Wang<sup>1</sup>, Jin Xu<sup>1</sup>, Keyou Wang<sup>1</sup>, Guojie Li<sup>1</sup>, Zhenyuan Feng<sup>2</sup>

<sup>1</sup> Key Laboratory of Control of Power Transmission and Conversion (Shanghai Jiao Tong University), Ministry of Education, Shanghai, China
<sup>2</sup> State Grid Jiaxing Power Supply Company, Jiaxing, Zhejiang, China

### Correspondence
Jin Xu, Key Laboratory of Control of Power Transmission and Conversion (Shanghai Jiao Tong University), Ministry of Education, Shanghai, China.
Email: xujin20506@sjtu.edu.cn

### Funding information
National Key Research and Development Program of China, Grant/Award Number: 2022YFE0105200; State Grid Zhejiang Electric Power Co., LTD., Jiaxing power supply company, Grant/Award Number: 5211JX230004

## Abstract
The aggregation models of renewable energy power stations are difficult to apply to the stability research of the fault inside the station or the oscillation analysis between the station and the grid-side system, and the high dimensional characteristics of their detailed model will pose an enormous challenge to the simulation efficiency. To alleviate the contradiction between accuracy and efficiency, this paper proposes a state-variable-preserving method to efficiently model inverter-based resources and a node tearing method to realize parallel simulation of the renewable energy power station consisting of inverter-based resources. The state-variable-preserving model uses discrete state space expression to eliminate the internal nodes on the basis of preserving the original variables of the generation unit and reduces the solving scale of the generation station. The node tearing method reduces the solving complexity of the associated variables, which is more consistent with the topology characteristic that different power generation clusters are interconnected by the same bus. In the case study, the results of numerical accuracy analysis and numerical stability analysis of a photovoltaic power plant verify the reliability of the proposed method, and its simulation efficiency is verified by changing the scale of the photovoltaic power plant.

## 1 INTRODUCTION
The power system is transforming into a complex network with renewable energies as the main body. The proportion of power electronic equipment in the power system has increased significantly, greatly changing the basic structure of the power grid and the stability mechanism of the system [1]. Considering the cost and safety of the electric power test, electromagnetic transient (EMT) simulation is an important method to analyse the stable operation mechanism of renewable energy power systems.

For simulation scenarios with different precision and specific requirements, relevant research has improved the efficiency of EMT simulation of renewable energy power stations through model simplification. The device-level simplification mainly increased the simulation step size by establishing the average value model [2] and the dynamic phasor model [3] of the power electronic equipment. The station-level simplification was mainly to reduce the number of renewable energy power generation units through aggregation. The single-machine equivalent model used one equivalent generation unit to represent the whole station [4], and its output power was the weighting of all the generation units in the station. Considering the different operating conditions of various units, the multi-machine equivalent model [5] performed equivalent processing for units in the same group according to different cluster indexes, further improving the accuracy of the aggregation model.

However, the simplified model at the device level ignores the switch action process, and the aggregation model at the station level cannot reflect the internal characteristics of the original system [6]. They are hard to apply to the stability research of the fault inside the station or the cascading accident of multiple stations [7] and the oscillation analysis between the renewable energy stations and the grid-side system [8].

The detailed modelling of renewable energy power stations based on the structure-preserving method retains the original circuit topology and introduces the microsecond switching process, which will dramatically increase the simulation burden of the system. Scholars put forward optimization methods to reduce the calculation amount of simulation and accelerate the solution process. The matrix exponential function [9] used large step size to speed up the simulation of the slow dynamic process, which realized the multi-time scale simulation of large-scale wind farms based on ensuring high fidelity. Then, an order reduction technique based on Krylov subspace [10] was further introduced to improve the simulation efficiency of high-dimensional EMT models of wind farms. The state space node method [11] used the state variables of dynamic components to form groups and the state space expression to solve the intra-group variables, which eliminated the internal nodes domain extraction decomposition method [28], were proposed for specific topologies, all of which are also difficult to apply to decouple renewable energy power stations.

Therefore, a state-variable-preserving (SVP) method for the efficient modelling of inverter-based resources in parallel EMT simulation is proposed in this work. Firstly, the SVP method uses the combination of controlled admittances and controlled historical current sources determined by internal state variables