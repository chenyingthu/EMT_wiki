# Real-time Simulation of Hybrid Modular Multilevel Converters using Shifted Phasor Models

**YINGDONG WEI**$^1$, (Member, IEEE), **DEWU SHU**$^2$, (Member, IEEE), **XIAORONG XIE**$^2$, (Senior Member, IEEE), **VENKATA DINAVAHI**$^3$, (Senior Member, IEEE), **ZHENG YAN**$^1$

$^1$ State Key Laboratory of Power System, Department of Electrical Engineering, Tsinghua University, Beijing, China  
$^2$ Department of Electrical Engineering, Shanghai Jiaotong University, Shanghai (e-mail: shudewu@sjtu.edu.cn)  
$^3$ Department of Electrical and Computer Engineering, University of Alberta, Edmonton, Alberta, Canada T6G2V4  

**Corresponding author:** Dewu Shu (e-mail: shudewu@sjtu.edu.cn).  
This work is partly supported by National Key R&D Program of China (2017YFB0902000), National Natural Science Foundation of China (51737007), and Science and Technology Project of State Grid (SGXJ0000KXJS1700841).

**ABSTRACT** The real-time simulation of modular multilevel converter (MMC) is essential to the evaluation and validation of its control and protection systems. Moreover, the dynamics at both sub-module level and system level are expected from the real-time simulations of MMCs. To achieve this objective, the paper proposes the shifted phasor modelling (SPM) of the MMC by representing each sub-module with a Thevenin equivalent circuit that is derived using shifted phasors with improved accuracy. The efficiency of the SPM is guaranteed by modelling each arm as a switch-dependent Thevenin equivalent circuit. The computational burden remains almost unchanged even when the number of sub-modules increases considerably. The proposed model are materialized using field programmable gate array (FPGA). And thus the real-time simulation of MMC-based DC grids can be realized to capture the dynamics at the system level as well as the sub-module level. The effectiveness of this work has been validated in terms of both accuracy and efficiency on a two-terminal MMC-based low voltage direct current (LVDC) system.

**INDEX TERMS** DC systems, electromagnetic transient (EMT), field-programmable gate array (FPGA), hardware design, modular multilevel converter (MMC).

## I. INTRODUCTION

MMC offers a better prospect for cost-effective power transmissions [1]-[2]. In practical MMC projects, the real-time simulation on FPGA plays an essential role in the implementation of the control and protection systems [3]-[4]. Since the voltage and current stresses in the circuits and components of MMC are critical for the design of its control and protection strategies, the real-time simulations need to provide the very details of dynamic responses of the system, including dynamics not only at the system level but also at the sub-module level.

Recently, different MMC accelerated models have been proposed, which can be categorized into two types: (i) Analytical models, such as the continuous-variable dynamic model [5]-[6], and the steady state model [7]-[8], etc. They are accurate and efficient to represent the MMC under steady-state conditions or small disturbances. However, these models cannot simulate DC faults because the nonlinear characteristics of the freewheeling diodes are not represented. (ii) Averaged value models or AVM, for instance, i.e., the converter-averaged model (CAM) [9]-[10] and the arm-averaged model (AAM) [11]. The CAM separates the whole MMC into ac- and dc- side circuits, or controlled sources. The AAM uses six arms as the basic elements and thus improves the simulation accuracy, especially under dc faults or blockings. The above two types of models focus more on system level dynamics and are mainly adopted in off-line analyses.

For the real-time simulation based on field programmable gate arrays (FPGAs), both sub-module level and system level dynamics are required for detailed studies of a MMC-based system. However, the sub-module level modeling of MMC has always been a challenging task due to the large number of sub-modules in a single arm [3]-[4]. On the one hand, the massive switching components greatly increase the number of nodes and the size of the admittance matrix of the system. As a result, it is very hard to model the MMC with high accuracy and real-time efficiency simultaneously. On the other hand, the real-time simulation of a practical AC/DC system would consume huge hardware resources of FPGAs. Usually some special emulation strategies, for instance, system decomposition and parallelization, should

4) The SPM has been successfully implemented in the FPGA-based real-time simulation platform, on which the detailed dynamics of hybrid MMCs are emulated accurately and efficiently.

The rest of the paper is organized as follows: Section 2