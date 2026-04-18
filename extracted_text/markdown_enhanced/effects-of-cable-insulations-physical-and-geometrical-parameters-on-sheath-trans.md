# Effects of cable insulations’ physical and geometrical parameters on sheath transients and insulation losses
Natheer Alatawneh
Cysca Technologies Inc., 275A Pierre-Le Gardeur blvd., Repentigny, Quebec, Canada
Polytechnique Montréal, 2900 boul. Édouard-Montpetit, Québec, Canada

**Keywords:** Underground power cable, Cable parameters, Sheath voltage, Finite-element method (FEM), Dielectric loss, Electromagnetic Transient Program (EMTP)

**Abstract:** This paper investigates the influence of insulations’ physical and geometrical parameters on cable sheath transients and insulation losses considering power cables for high voltage alternating current (HVAC) applications. The study is based on theoretical analysis, Electromagnetic Transient Program (EMTP) simulations, and finite element (FE) simulations. Special attention is paid to the effects of the insulations’ relative permittivities and the protective jacket thickness on cable capacitance, transient voltages, and dielectric losses for different possible conditions including the variations in insulation permittivity and ground resistivity. The cable model used in this work is a single core (SC) underground coaxial cable with an AC voltage supply of $220$ kV and $60$ Hz frequency. A method for calculating the dielectric losses in cable insulations due to transient voltages was developed. The proposed method is based on the numerical calculations of the flowing electric currents through insulations using FE model. In addition, the relation of the dielectric loss and the maximum sheath overvoltage as a function of permittivites and as a function of protective jacket thickness was explored to obtain an optimum protective jacket relative permittivity from the viewpoint of both the overvoltage and the loss. For given cable system parameters, the transient voltage waveforms within a time period of $t = 0\text{--}2$ ms obtained on the core and the sheath produced dielectric losses $34.362$ [W/m] and $3.365$ [W/m] at insulation and protective jacket, respectively.
Results and conclusion provide a useful background for the ongoing power cable design process and application studies.

## 1. Introduction
Many cables are going to be installed and are under construction [1–5]. For example, the ongoing London’s Power Tunnels project consists of $32$ km of tunnels between $20$ m and $60$ m deep below the ground. The tunnels are planned to host $400$ kV cables to connect several substations. The project is expected to be completed by 2018 [1]. The Maritime Transmission Link is a Canadian project that includes subsea cables with an approximate length of $450$ km [2]. The aforementioned references present examples of active projects of power cable installation across the world. This motivates researchers for continuous development and optimization of cable design process. Better understanding of cable insulations’ physical and geometrical parameters on sheath transients and insulation losses is of crucial importance for accurately calculating cable parameters during power system simulations including electromagnetic transients. The transients concept, herein, applies on any sudden changes of voltage and current in limited time. Transients may be caused by switching, lightning, or faults.

Considering the above, a number of papers and reports have been published in the last decade for modelling and analysis of cable parameters [6–9]. However, the effects of the physical and geometrical parameters of cable insulations on transients and losses have not been discussed in detail in the publications. The permittivity and thickness are dominant factors to determine cable capacitances and affect significantly the propagation constant and the characteristic impedance of the cable. It is well known that the relative permittivity changes with several physical quantities such as temperature, humidity and mechanical stress. However, and since this study does not focus on the physical parameter variations, standard conditions of permittivity are considered, such that ambient temperature and $50$ Hz [10].

In this paper, a single core coaxial cable model is considered to study and analyze the model parameters. The effect of the insulation permittivity, loss factor and thickness on the cable capacitances, transients and losses are investigated based on theoretical formulas, EMTP simulations and FE simulations. The capacitances are calculated as a function of the insulation permittivity and the insulation thickness. Then, the effect of the permittivity and thickness on cable transients, especially on transient overvoltages on the cable metallic sheath and insulation losses are investigated.

Finally, a method for calculating the dielectric losses in cable insulations due to transient voltages was developed. The proposed method was validated and compared to the analytical formula in the case of steady state.

**Table 1** Geometrical and physical parameters.
| Parameter | Value |
|---|---|
| $r_2, r_3, r_4, r_5$ | $25.4, 45.6, 50.8, 65.9$ [mm] |
| $c, s$ | $3.19 \times 10^{-8}, 1.87 \times 10^{-7}$ [Ω·m] |
| $\varepsilon_1, \varepsilon_2, \varepsilon_0$ | $1\text{--}4, 1\text{--}6, 10^{-9}/36\pi$ [F/m] |

### 2.2. Effect of relative permittivity on capacitance
The metallic sheath has been assumed a non-ferromagnetic material with a