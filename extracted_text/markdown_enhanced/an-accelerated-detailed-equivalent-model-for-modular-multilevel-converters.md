## An accelerated detailed equivalent model for modular multilevel converters✩
Ramin Parvari a, Shaahin Filizadeh a,∗, Dharshana Muthumuni b  
a University of Manitoba, Winnipeg, MB R3T 5V6, Canada  
b Manitoba Hydro International, Winnipeg, MB R3P 1A3, Canada  

**Keywords:**  
Modular multilevel converters  
Detailed equivalent models  
Electromagnetic transient simulation  

**ABSTRACT**  
Detailed Equivalent Models (DEMs) of Modular Multilevel Converters (MMCs) are generally developed based on Thevenin equivalent circuits with a time-varying resistor. This approach may become computationally inefficient, specifically for the simulation of large power systems with many nodes, where the network admittance matrix needs to be frequently re-inverted every time a switching event occurs. This paper proposes a novel strategy to eliminate admittance matrix re-inversions during the converter’s normal operation and restrict it only to when the converter undergoes blocking. The proposed DEM thus yields marked reductions in the simulation time of MMC circuits, and is particularly useful in studies wherein repetitive simulations are necessary. Models are implemented for MMCs with half-bridge (HBSM) and full-bridge (FBSM) sub-modules in the PSCAD/EMTDC simulator, and their accuracy is thoroughly validated for normal and blocked operating conditions. It is shown that the developed models are 30% and 60% more computationally efficient, respectively, for HBSM and FBSM MMCs in comparison to existing DEMs.

## 1. Introduction
Modular multilevel converters are widely used in HVDC transmission systems. In comparison to two- or three-level converters [1], they have important advantages such as modularity, scalability, low harmonics, and reduced switching losses [2,3]. MMCs generate output voltage waveforms with low harmonics by stacking building blocks, known as sub-modules (SMs), which make it possible to closely follow the reference waveform. Half-Bridge and Full-Bridge sub-modules (HBSMs and FBSMs) are by far the most commonly used sub-module types for they consist of a relatively small number of switches and have an inherent ability to block DC fault currents, respectively.

Computer simulation models of MMCs play critical rules in power system studies. The model needs to both accurately and efficiently represent the dynamics of the converter under normal and faulted operating conditions. However, the large number of switches in MMCs imposes a significant computational burden for EMT-type simulators if the MMC were to be modeled with connection of individual switches, known as a Detailed Switching Model (DSM). In such a case, a prohibitively large network admittance matrix must be inverted every time a switching event occurs. Thus DSMs are usually used for very specific applications or MMCs with a low number of SMs, e.g., as in [4]. To overcome this, several equivalent models have been introduced that represent the dynamic response of the MMC while alleviating its computational burden. The Averaged-Value Model (AVM) proposed in [5,6] is a popular model, which is suitable for low-frequency analysis of MMCs in normal mode of operation. This model has been used for system-level and controller design studies, e.g., for suppression of circulating currents [7,8]. It is also useful for the analysis of the voltage ripple in capacitors and sizing them [9]. Although AVMs are generally intended to study the terminal behavior of the MMCs, several works [10–14] have introduced improved AVMs that include the blocking mode as well (see Table 1). The main drawback of AVMs is that a single equivalent capacitor is used to characterize the stack of SMs in the arm, which prevents the study of individual capacitor voltages.

Detailed Equivalent Models (DEMs), on the contrary, efficiently represent MMCs in full detail and with an accuracy equal to a DSM. The core idea in a DEM is to replace the stack of SMs with a Thevenin or Norton equivalent circuit, which reduces its hundreds of nodes to two or three, thus diminishing the size of the network admittance matrix by many orders of magnitude. The Thevenin or Norton resistor and source parameters are affected by the numerical integration method employed for discretizing the voltage and current of the SM capacitors. Using trapezoidal integration method, Refs. [15–22] have developed DEMs with Thevenin and Norton equivalent circuits. Although these models offer remarkable computational efficiency compared with a DSM, the network admittance matrix must still be modified frequently, which makes re-triangularization of the admittance matrix, albeit a

**Table 1**  
Summary of MMC models in the literature.
| Ref. | DSM | DEM | AVM | SM type(s) | Ability for blocked mode simulation | Focus of study |
|---|---|---|---|---|---|---|
| [4] | ✓ | | | HBSM | ✓ | Dynamic performance of MMC with 6 SM per arm |
| [5] | | | ✓ | N/A | | Simplified HVDC model for analysis of MMC’s dynamic behavior |
| [6] | | | ✓ | HBSM | | |