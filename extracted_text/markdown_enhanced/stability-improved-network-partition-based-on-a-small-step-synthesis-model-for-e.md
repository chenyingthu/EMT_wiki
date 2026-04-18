# Stability-improved network partition based on a small-step synthesis model for electromagnetic transient simulation
Haoran Zhao, Changwang Zhao, Bing Li ∗, Luwei Tan
School of Electrical Engineering, Shandong University, Jinan 250061, China

∗ Corresponding author.
E-mail addresses: hzhao@sdu.edu.cn (H. Zhao), zhaocw@mail.sdu.edu.cn (C. Zhao), bingli@mail.sdu.edu.cn (B. Li), 13625660215@163.com (L. Tan).

## Keywords
Electromagnetic transient, Simulation, Network partition, Stability analysis, Small-time step synthesis

## Abstract
Electromagnetic transient simulation offers high fidelity for modern power systems with high penetration of power electronics, but it suffers from low efficiency due to small time step requirements. To improve efficiency, network partition based on energy storage elements (i.e., capacitors and inductors) has gained attention, yet its numerical stability is limited by the simulation time step. This paper proposes a stability-improved network partition method using a small-step synthesis model. First, the semi-implicit leapfrog method-based network partition formulation is derived. Second, the small-step synthesis model-based network partition method is proposed. The method improves the numerical stability of the simulation by applying a small-step synthesis model to the network partition branches. Finally, the stability boundaries for the time step and synthesis order are derived based on the Lyapunov criterion and spectral radius analysis. The IEEE 14-bus system and a wind farm model are used to validate the proposed method. The results demonstrate that the proposed method enhances stability without sacrificing accuracy or efficiency.

## 1. Introduction
With the large-scale integration of wind and photovoltaic power, modern power systems are increasingly characterized by high penetration of power electronics and renewable generation [1,2]. As a result, the broadband oscillation phenomenon gradually intensifies in modern power systems [3]. Traditional electromechanical transient simulation method can only capture the dynamics near the fundamental frequency (e.g., 50 Hz or 60 Hz) [4]. It fails to reflect broadband oscillation phenomenon. In contrast, electromagnetic transient simulation (EMT) retains all physical details including system nonlinearity and high-frequency characteristics introduced by power electronic devices [5,6].

Despite its advantages, EMT simulation suffers from efficiency limitations [7]. To accurately represent the switching behavior of power electronic devices, the simulation time step must be constrained to the microsecond level [8,9]. Such a small time step leads to extremely low computational efficiency when applied to large-scale renewable energy-integrated power systems with thousands of nodes [10]. Hence, it highlights the urgent need for more efficient EMT simulation methods.

By network partition, the large-scale power system can be divided into multiple subsystems, thereby reducing the dimension of the admittance matrix. Thus, the simulation efficiency can be highly improved [11,12]. Existing network partition methods can be broadly classified into three categories based on the underlying principles. The first category involves natural partitioning based on long transmission lines [13] which leverage the inherent wave propagation delay of the transmission lines. It can achieves high accuracy without introducing simulation errors. However, long transmission lines of sufficient length are not present in many power systems, thereby restricting the practical applicability [14]. The second category involves rigorous mathematical transformations applied to the original system equations to enable network partitioning, with the key challenge being the accurate and efficient calculation of interface variables between subsystems. Representative approaches include the branch tearing and node splitting methods proposed in [15,16], where interface variables between subsystems are determined by updating a reduced-order nodal admittance matrix involving only the boundary nodes. In a similar context, the multi-area Thevenin equivalent method proposed in [17] models each subsystem as a multi-port equivalent circuit and coordinates them through centralized interface equations. Additionally, the waveform relaxation method enables each subsystem to independently solve its dynamic equations while iteratively exchanging waveforms of the interface variables to ensure consistency [18,19]. Recently, hybrid approaches that combine the strengths of the mentioned methods have been introduced to enhance partition granularity and improve overall simulation efficiency [20,21]. Although these methods offer high accuracy, they are limited by the increasing computational burden

**Table 1** Comparison of existing methods.
| Refs. | Cat. I | Cat. II | Cat. III |
| :--- | :--- | :--- | :--- |
| | [13] [14] | [15]–[21] | [22]–[25] |

guidance for selecting an appropriate synthesis order $k$ for constructing the model.
The rest of this article is organized as follows. Section 2 introduces the basic theory of SILM