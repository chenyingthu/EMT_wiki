# Machine-Learning-Reinforced Massively Parallel Transient Simulation for Large-Scale Renewable-Energy-Integrated Power Systems
Tianshi Cheng, Member, IEEE, Ruogu Chen, Graduate Student Member, IEEE, Ning Lin, Senior Member, IEEE, Tian Liang, Member, IEEE, and Venkata Dinavahi, Fellow, IEEE

Manuscript received 8 December 2023; revised 5 March 2024 and 25 April 2024; accepted 1 June 2024. Date of publication 5 June 2024; date of current version 27 December 2024. This work was supported in part by the Natural Science and Engineering Research Council of Canada (NSREC), in part by Mitacs, and in part by RTDS Technologies Inc. Paper no. TPWRS-01920-2023. (Corresponding author: Tianshi Cheng.)
Tianshi Cheng, Ruogu Chen, and Venkata Dinavahi are with the Department of Electrical and Computer Engineering, University of Alberta, Edmonton, AB T6G 2V4, Canada (e-mail: tcheng1@ualberta.ca; ruogu@ualberta.ca; dinavahi@ualberta.ca).
Ning Lin is with Powertech Labs Inc., Surrey, BC V3W 7R7, Canada (e-mail: ning3@ualberta.ca).
Tian Liang is with RTDS Technologies Inc., Winnipeg, MB R3T 2E1, Canada (e-mail: tian.liang@ualberta.ca).
Color versions of one or more figures in this article are available at https://doi.org/10.1109/TPWRS.2024.3409729.
Digital Object Identifier 10.1109/TPWRS.2024.3409729

## Abstract
Renewable energy systems (RESs) are pivotal in the transition to eco-friendly smart grids. The complexity and uncertainty of RESs, driven by uncontrollable natural forces like sunlight and wind, bring challenges to integrating RESs into modern power systems. Electromagnetic transient (EMT) simulation is an effective method for studying the integration of RESs. Currently, the EMT simulation of RESs is limited to small-scale and lumped RES models due to the model complexity and nonlinearity, which cannot reflect the detailed characteristics of large-scale RESs in practice. This paper introduces a data-oriented, machine learning-enhanced approach to achieve massively parallel EMT simulation on CPU-GPU, designed to efficiently model and simulate large-scale, detailed RES. It incorporates data-driven machine learning modeling of RES via artificial neural networks and integrates these models using a data-oriented entity-component-system framework. The model training was based on reliable model data produced by traditional physical EMT models and the results were validated with MATLAB/Simulink. The RES components are grouped into a microgrid connected to a synthetic AC/DC system based on the IEEE 118-Bus system, achieving an acceleration performance of 400 times faster than traditional CPU nonlinear iterative computations with 2 million RES entities.

## Index Terms
Artificial neural networks, data-oriented programming, entity-component-system, energy storage, electromagnetic transients, gated recurrent units, graphical processors, solar farms, wind farms, machine learning, renewable energy systems, parallel processing.

## Nomenclature
| Acronym | Definition |
|---|---|
| ANN | Artificial neural network. |
| CPU | Central processing unit. |
| DFIG | Doubly-fed induction generator. |
| ECS | Entity-component-system. |
| EMT | Electromagnetic transient. |
| GPU | Graphical processing unit. |
| GRU | Gated recurrent unit. |
| GSC | Grid side converter. |
| MLP | Multi-layer perceptron. |
| MSE | Mean squared error. |
| PV | Photovoltaic. |
| RES | Renewable energy system. |
| RNN | Recurrent neural network. |
| RSC | Rotor side converter. |

## I. INTRODUCTION
RENEWABLE energy systems (RESs) are pivotal in the transition to eco-friendly smart grids. Yet, the inherent complexity and uncertainty of these systems, arising from the unpredictability of natural forces such as sunlight and wind, present significant challenges in power system control and operation [1]. Detailed electromagnetic transient (EMT) simulation plays an important role in the analysis of control and operation for RES integrating power systems [2], [3]. However, there are more than 300,000 PV panels in a 100MW solar power farm [4], while each module may have an impact on the entire solar farm performance in partial shading scenarios [5], [6]. The same problem also exists for battery groups where the battery management system needs to take care of inconsistencies within the series battery array to maintain the optimal performance [7]. The traditional approach of detailed EMT simulations to address these challenges faces scalability issues due to the computational burden of modeling extensive RES components. For example, the nonlinearity of the PV model requires the Newton-Raphson method to assemble a huge global Jacobian matrix in each iteration, adding prohibitive computational complexity for large-scale power systems with many PV arrays.

A common solution is to utilize massively parallel hardware: Graphical Processing Unit (GPU) to solve large groups of RES components concurrently [8], [9]. However, the nonlinearity of these models limited the solution methods and parallel efficiency as GPUs are not good at complex logics such as branch predictions; nonlinear methods such as the Newton-Raphson method are iterative and needs frequent data exchange between host and device memory, which brings significant overheads. Furthermore, it is challenging to adapt and reimplement complex RES EMT models to highly efficient and scalable GPU codes, making it difficult to keep pace with rapidly evolving new energy and power storage technologies.

- This paper employs data-oriented entity-component-system (ECS) architecture and GPU instancing strategies to incorporate the ANN model of RES into the EMT power grid simulation program, ac