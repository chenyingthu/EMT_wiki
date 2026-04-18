## Parallelization of MMC detailed equivalent model
A. Stepanov a, *, J. Mahseredjian a, H. Saad b, U. Karaagac c  
a Department of Electrical Engineering, Polytechnique Montréal, Montreal, QC, Canada  
b Réseau de Transport d’Electricité, Paris, France  
c Department of Electrical Engineering, Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong  
* Corresponding author. E-mail address: anton.stepanov@polymtl.ca (A. Stepanov).

**Keywords:** Detailed equivalent model, Parallelization, Modular multilevel converter, Simulations

**Abstract:** This paper proposes a method to parallelize the computations of the detailed equivalent model of modular multilevel converter (MMC) on multicore CPUs in offline simulations of electromagnetic transients (EMTs). Each arm of the converter is implemented as a DLL independently from the main solver and is interfaced with it using standard procedures. It is also proposed to parallelize the capacitor balancing algorithm using a similar approach. Depending on the simulated system, the proposed method allows to accelerate simulations by five times without affecting accuracy of the results. Results also demonstrate that parallelization of the capacitor balancing algorithm plays an important role in improving simulation speed and can have a larger impact than the parallelization of electrical circuit equations.

## 1. Introduction
Modular multilevel converter (MMC) is a power electronic converter that is used in many modern HVDC transmission projects, Fig. 1. It has several significant advantages, including easy scalability to high voltage levels, smooth AC voltage waveform, and relatively low losses, all due to its modular structure and lower switching frequency. The MMC generates AC voltages by inserting the appropriate number of submodules (SMs), which are essentially capacitors with quasi-constant voltage, each of which represents one level of the resulting voltage waveform [1].

It is essential to perform electromagnetic transient (EMT) simulations to ensure safe and reliable operation of HVDC systems. To do so, accurate time-domain models of various equipment are required. Owing to the structural complexity of MMCs, numerous EMT models have been developed, some of the most used ones are [2-4]:
- The detailed model (DM), that represents IGBTs in each SM using a piecewise linear v-i characteristic.
- The detailed equivalent model (DEM), that represents IGBTs as two-value resistances.
- The arm equivalent model, that aggregates all SMs in each arm into a single equivalent circuit.
- The average value model, that represents all SMs in whole converter as a single capacitor.

While detailed models provide high accuracy, they are typically much slower, which restricts their application. Efforts have been put forward to improve the speed of simulations involving MMCs in various ways [4-6]. However, parallelization of MMC model computations has not been widely researched [7].

Parallelization in EMT simulations has been applied through network decoupling by transmission lines [8,9], co-simulation methods [10], parallel implementation of LU factorization [11]. CPU or FPGA implementations have been used to accelerate the simulations of power electronic devices. Real-time applications are investigated in [7,12].

This paper proposes a method to parallelize the computations of the DEM on multicore CPUs in offline simulations. Among the conventional MMC models, the DEM is a good candidate for parallelization because:
- It has relatively high computational burden, which offers potentially significant time-gains.

*This work was supported by the Natural Sciences and Engineering Research Council (NSERC) of Canada as part of the industrial chair “Multi time-frame simulation of transients for large scale power systems.”. Paper submitted to the International Conference on Power Systems Transients (IPST2021) in Belo Horizonte, Brazil June 6–10, 2021.*

current time-point and then the solicited DEMs only retrieve the results when requested by CC, as shown in Fig. 2 (EMT-core is CC). The CBA parallelization is performed in a similar manner with the difference being that it only participates in the control system equations part, but not in the MNE.

There are similarities between the proposed approach and the one used in [7]. However, this paper deals with offline simulations and focuses on the simulation time reduction and evaluation of various contributing factors. Besides, the proposed parallelization approach is applicable to computers with any number of cores and to circuits with any number of DEM and CBA blocks and any number of SMs.

## 3. DEM parallelization
Each DEM arm is interfaced with the CC by using its Norton equivalent circuit. To calcul