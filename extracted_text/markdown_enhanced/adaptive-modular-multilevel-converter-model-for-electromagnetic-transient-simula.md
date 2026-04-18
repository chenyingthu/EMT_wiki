## Adaptive Modular Multilevel Converter Model for Electromagnetic Transient Simulations
Anton Stepanov, Student Member, IEEE, Jean Mahseredjian, Fellow, IEEE, Ulas Karaagac, Member, IEEE, Hani Saad, Member, IEEE

**Abstract**—This paper proposes an adaptive model of modular multilevel converter (MMC) for electromagnetic transient (EMT) simulations. The model is applicable to MMCs with arbitrary numbers of half-bridge and full-bridge submodules. The proposed design includes average value model, arm equivalent model, and detailed equivalent model. It allows smoothly transitioning from one model to another during time-domain simulations depending on the desired accuracy and execution time constraints.

Modifications required in conventional MMC models to achieve smooth transitions are presented in the paper. Time-domain initialization methods are developed for each constituting model, including initialization of the appropriate control system blocks. Validity and effectiveness of the proposed adaptive model is demonstrated using EMT simulations of 401-level MMC-HVDC system.

**Index Terms**—adaptive model, average value model, arm equivalent, detailed equivalent, High-Voltage Direct Current, model switching, modular multilevel converter, simulation

## I. INTRODUCTION
Modular multilevel converters (MMCs) have become the state-of-the-art technology for HVDC systems. A typical MMC in HVDC applications has six arms of series-connected submodules (SMs), each providing one step in the resulting multilevel AC waveform, Fig. 1. Due to its advantages over conventional two- and three-level converters, including easier scalability to higher voltages, lower harmonic content, better reliability, lower switching frequency and voltage [1], [2], MMCs are used in modern HVDC projects [3], [4].

Different MMC models for electromagnetic transient (EMT) simulations are available in the literature and the choice of the model represents a compromise between the necessary accuracy and computational burden:

- The detailed equivalent model (DEM) simplifies IGBT switch representation to two-value resistances [5], [7]. All SM voltages and gating signals are available. It is often implemented independently and is interfaced with the main EMT solver using a two-port Thevenin or Norton equivalent circuit so internal electrical nodes are inaccessible [6].
- The arm equivalent model (AEM) assumes that all SMs in each arm are perfectly balanced, so only one equivalent capacitor is used to represent the whole arm [8]. Grid studies and controller design can be performed with such a model [6].
- The average value model (AVM) is composed of two parts, AC and DC, disconnected from each other and aggregates SM capacitors of all arms into a single DC side capacitor. Neither voltage ripple nor circulating current are available but AC and DC currents and voltages in normal balanced operating conditions are sufficiently accurate [5], [9].

EMT simulation studies of power systems can provide accurate results over a wide frequency range, especially if small time-steps are used, but high accuracy increases computing times. Many methods have been proposed in the literature to accelerate time-domain simulations of MMCs, including various improvements to standalone models [8, 10-13].

The method presented in this paper provides acceleration based on the assumption that during time-domain simulations there could be intervals during which the details of converter internal behavior can be ignored. Initialization and slower electromechanical transients constitute such intervals. It is then possible and sufficient to model accurately only converter’s external behavior to accelerate computations, which makes the proposed new relaxation method an additional improvement to existing acceleration methods.