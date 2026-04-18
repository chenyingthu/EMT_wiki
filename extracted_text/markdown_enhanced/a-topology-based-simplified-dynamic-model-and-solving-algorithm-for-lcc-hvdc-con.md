# A topology-based simplified dynamic model and solving algorithm for LCC-HVDC converters considering commutation failure

Yangyang He a,*, Nengling Tai a, Jin Xu b, Wenzhuo Liu c, Panjie Lian c, Haizhen Zhang d  
a College of Smart Energy, Shanghai Jiao Tong University, Shanghai 200240, China  
b School of Electrical Engineering, Shanghai Jiao Tong University, Shanghai 200240, China  
c China Electric Power Research Institute, Beijing 100192, China  
d Huadian Electric Power Research Institute CO., Ltd, Hangzhou 310030, China  
* Corresponding author. E-mail address: michael-yang@sjtu.edu.cn (Y. He).

**Keywords:** Topology-based, Dynamic model, Algorithms, HVDC converters, Commutation failure

**Abstract:** Dynamic modeling of line-commutated converter (LCC) based high-voltage direct current (HVDC) systems faces a trade-off between computational efficiency and accuracy in capturing commutation failure (CF) behavior. Existing electromagnetic transient (EMT) models are highly accurate but computationally intensive, whereas simplified models often neglect valve-level switching dynamics and CF mechanisms. To overcome these limitations, this paper proposes a topology-based simplified dynamic (TBSD) model for LCC-HVDC converters. The model adopts ideal switch representations to preserve the discrete switching behavior of thyristors, and decomposes the converter circuit into a main network and a valve-level auxiliary network based on topological states. Then, a structure-stable solving algorithm is developed to maintain consistent matrix dimensions across different switching configurations. Furthermore, an adaptive time-step control strategy is introduced, which dynamically adjusts the simulation step based on the rate of change in DC current, achieving both computational acceleration during steady-state and high-resolution tracking during transients. The proposed model and solution method are implemented in the PSModel simulation platform and validated against PSCAD/EMTDC under steady-state and fault conditions. Simulation results confirm that the TBSD model accurately captures commutation failure dynamics while significantly improving computational efficiency.

## 1. Introduction

The line-commutated converter (LCC) based high-voltage direct current (HVDC) system has become a critical component in long-distance and high-capacity power transmission, particularly within AC/DC hybrid grids. Its mature technology, low cost, and high-power transfer capability make it the preferred choice in large-scale inter-regional energy delivery. However, the reliance of LCC-HVDC systems on the strength and stability of the AC network introduces inherent vulnerability—most notably, the phenomenon of commutation failure (CF) [1–3].

Commutation failure (CF) is an inherent phenomenon in LCC-HVDC systems due to their reliance on the AC-side voltage for successful commutation [4]. During AC faults, the reduction in voltage amplitude and distortion of zero-crossing may lead to insufficient commutation margin, preventing the valve from turning off as expected. In some cases, the valve may even be re-triggered by a forward voltage shortly after turn-off resulting in CF. This leads to a sharp drop in DC voltage, a surge in current, and reduced power transfer, which poses a significant threat to system stability. In interconnected or multi-terminal systems, CF can propagate across the network, further exacerbating disturbances and complicating recovery [5].

To evaluate and simulate LCC-HVDC system dynamics under such conditions, various modeling approaches have been proposed. Quasi-steady-state (QSS) models express the characteristics of the converter in a steady-state equation and offer computational efficiency [6–8]. Dynamic phasor models [9–11], based on time-varying Fourier series, provide frequency-domain insights but simplify commutation dynamics by assuming linear current transitions and neglecting delayed valve characteristics. Switch-function-based models [12–15] improve precision but either neglect commutation dynamics or rely on QSS-derived overlap angles that cannot resolve time-dependent valve switching. In [13], a spectral model incorporating the commutation overlap angle was proposed using 3-D Fourier series, and its influence on the rectifier-side impedance was analysed via harmonic linearization. The study

## Nomenclature

| Symbol | Description |
|---|---|
| $\Delta t$ | Simulation time step |