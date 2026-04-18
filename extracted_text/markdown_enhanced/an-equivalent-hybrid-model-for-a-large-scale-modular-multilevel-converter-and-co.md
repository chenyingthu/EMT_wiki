Received April 20, 2022, accepted May 15, 2022, date of publication May 18, 2022, date of current version May 23, 2022.
Digital Object Identifier 10.1109/ACCESS.2022.3176006

# An Equivalent Hybrid Model for a Large-Scale Modular Multilevel Converter and Control Simulations

**MOHAMMED ALHARBI**<sup>1</sup>, **SEMIH ISIK**<sup>2</sup>, (Graduate Student Member, IEEE), AND **SUBHASHISH BHATTACHARYA**<sup>2</sup>, (Fellow, IEEE)
<sup>1</sup> Department of Electrical Engineering, College of Engineering, King Saud University, Riyadh 11421, Saudi Arabia
<sup>2</sup> Department of Electrical and Computer Engineering, North Carolina State University, Raleigh, NC 27606, USA

**Corresponding author:** Mohammed Alharbi (mohalharbi@ksu.edu.sa)
This work was supported by the King Saud University, Riyadh, Saudi Arabia, through the Researchers Supporting, under Project RSP2022R467.

**ABSTRACT** Modular multilevel converter (MMC) is adopted mainly for high voltage applications with many power blocks per arm. Before commissioning a large-scale MMC application, it is vital to simulate and study internal and system-level dynamics. However, it is challenging to simulate an MMC with many SMs in EMT simulation tools due to simulation time and computation burden. Therefore, several simplified modeling techniques are proposed to reduce the challenges. Even though the existing models reasonably reduce the computation complexity and simulation time, there are still challenges as the internal dynamics of an MMC cannot be fully captured. On the other hand, the detailed equivalent models capture the internal dynamics, but the simulation complexity and the time increase. Therefore, it is still a need for better, faster, and more accurate simulation models to study the system-level and internal dynamics of an MMC. Therefore, this paper proposes a hybrid simulation model for a large-scale MMC application using a scale-up control structure method. The proposed method is verified in the MATLAB/Simulink simulation tool. Besides, the proposed model is tested and verified at the Real-Time Digital Simulator (RTDS) in a Hardware-in-Loop (HIL) environment.

**INDEX TERMS** EMT, hybrid model, MMC, HVDC, simulation, RTDS.

## I. INTRODUCTION
Voltage Source Converter (VSC) based High Voltage Direct Current (HVDC) applications is witnessed a global rise in the last two decades. Significantly, the technical developments in the VSC topology and the invention of the Modular Multi-level Converter (MMC) in the early 2000s helped increase the number of HVDC projects worldwide. Besides, it is expected that it will grow by around 11% between 2020 to 2025 based on the compound annual growth rate [1]. One reason for this increase is to integrate more renewable energy sources. Besides, VSC-based HVDC provides several benefits to the existing AC grids, such as grid stability and black-start capability under abnormal conditions. Furthermore, the MMC topology helps reduce the cost of HVDC applications cost by reducing the component sizing and reducing the total land area by requiring a much smaller filter.

The MMC topology is flexible to increase the capacity based on the demand due to its modular and scalable features. The MMC structure can be built by several hundreds of power blocks called Sub-Module (SM), as seen in Fig. 1. Different SM structures are available for MMC applications, but Half-Bridge SM (HBSM) or Full-Bridge SM (FBSM) is the most used type. The HBSM includes two switching elements, such as Insulated Gate Bipolar Transistors (IGBTs), and an energy storage element such as a capacitor. In contrast, the FBSM includes four IGBTs and a capacitor, as seen in Fig. 2(a) and 2(b). The HBSM causes fewer losses, and it is more economical than the FBSM. However, unlike the HBSM, the FBSM can block a DC fault from the AC grid. The scope of this paper does not include DC side fault analysis, hence HBSM is adopted throughout the paper.

Regardless of the SM type, each phase of an MMC consists of positive and negative arms with the same number of SMs. The number of SMs can be increased or decreased based on the desired capacity. The higher number of SM results in higher losses as each SM consists of switching elements and the energy storage element. Besides, it is challenging for simulation tools to analyze the dynamic operation of an MMC-based HVDC system with many SMs. An MMC with hundreds of SMs creates a large number of nodes, resulting in an extensive network admittance matrix. The generated network admittance matrix needs to be recalculated for every switching event. Hence, repeating this process at every switch

**FIGURE 1.** Illustration of the conventional three-phase MMC system.

**FIGURE 2.** (a) HBSM and (b) FBSM circuits.

**FIGURE 3.** MMC scale-up structure.

Transient (EMT) model. However, performance degradation still occurs, especially with many MMC applications. Averaging-based models for MMC are proposed in [5]–[8], resulting in less computational and simulation time. Even though the system-level accuracy is enough in these models, the user does not have the flexibility to test the internal dynamic of the MMC, such as SM voltage balancing control. The authors [9], [10] proposed a co-simulation model where a part of the system is modeled based on a detailed equivalent model, and the rest of the system is modeled with a less detailed orientation. Although faster simulation time is achieved in this work, implementing parallel processing at different time steps and synchronization of the different control structures such as MMC internal current control, the system-level control can be highly challenging. Researchers in [11]–[15] adopted the dynamic phasors approach to MMC