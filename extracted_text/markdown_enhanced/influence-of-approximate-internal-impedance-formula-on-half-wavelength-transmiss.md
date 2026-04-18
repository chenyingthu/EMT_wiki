# Influence of approximate internal impedance formula on half-wavelength transmission lines

J.E. Guevara Asorza, R.E. Rojas, J. Pissolato Filho  
School of Electrical and Computer Engineering, University of Campinas - UNICAMP, Campinas, Brazil

**Keywords:** Long distance transmission, Half-wavelength transmission line, Internal impedance, Overvoltage, Statistical switching

**Abstract:** This paper evaluates the impact of using approximate versus exact internal impedance formulations in Overhead Transmission Lines (OHTL), focusing on Half-Wavelength Transmission lines (HWTL) and high-surge impedance loading applications, where multiple conductors per phase are employed. Approximate formulations for the internal impedance of conductors simplify calculations but may introduce minor errors that, in specific applications, can become more significant. These inaccuracies affect key parameters, including active power transfer, surge impedance loading (SIL), and Joule losses, and can also compromise the accuracy of transient analysis. The study compares approximate and exact impedance formulations under steady-state and transient conditions across three OHTL configurations of varying designs. Results reveal that approximate formulations reduce accuracy in SIL and voltages calculations, resulting in potential power transfer limitations and increased voltage drops. Furthermore, a statistical analysis of switching manoeuvres demonstrates that the approximate model predicts higher overvoltages than the exact formula, with phase C exhibiting the most significant deviations. These findings underscore the critical importance of precise internal impedance modelling in HWTL studies to ensure reliable power system analysis.

*I This paper was supported by the São Paulo Research Foundation (FAPESP), Brazil grants: 2021/11258-5, 2023/05066-1 and 2024/14472-6, and National Council for Scientific and Technological Development (CNPq), Brazil grants: 161959/2022-9.*  
*II Paper submitted to the International Conference on Power Systems Transients (IPST2025) in Guadalajara, Mexico, June 8-12, 2025.*  
*Corresponding author. E-mail addresses: j272296@dac.unicamp.br (J.E.G. Asorza), rerojasvarela@gmail.com (R.E. Rojas), pisso@unicamp.br (J.P. Filho).*  
https://doi.org/10.1016/j.epsr.2025.112229  
Received 30 December 2024; Received in revised form 14 April 2025; Accepted 4 September 2025  
Available online 19 September 2025

## 1. Introduction

Accurate computation of electrical parameters in overhead transmission lines (OHTL) is essential for designing and analysing power systems, particularly in applications involving long-distance power transmission. Parameters such as series impedance and shunt admittance are influenced by conductor properties and their position concerning ground, ground characteristics, and frequency-dependent behaviour, including skin effect and electromagnetic field interactions. In ultra-long transmission lines, power transfer efficiency is impacted by increased line impedance, voltage stability concerns, and significant reactive power generation, requiring specialised solutions such as high-voltage direct current (HVDC) transmission systems or half-wavelength transmission lines (HWTL) [1–3], to mitigate these effects, as seen in large continental countries like Brazil, where generation sources and demand centres are widely separated. HWTL designs can optimise power transfer, reduce losses, and enhance grid resilience, proving indispensable for large-scale power applications.

The concept of a HWTL is predicated on the electrical length that corresponds to half the wavelength of the operating frequency. For a 60 Hz system, the wavelength in a vacuum is approximately 5000 km; however, the propagation velocity of electromagnetic waves in transmission lines is affected by the line’s construction and the surrounding medium, resulting in a velocity factor that is less than unity. This reduction in propagation speed leads to a shorter wavelength within the transmission line [4]. It can thus be concluded that the half-wavelength of practical 60 Hz transmission lines is less than 2500 km. However, to ensure a stable response, it is necessary that the line should be slightly longer than half the wavelength [5,6] Consequently, the HWTL examined in this study spans 2600 km.

Some electromagnetic transient (EMT) programs use approximate internal impedance formulations to become computationally more efficient and hold good accuracy in the results. However, these approximations may introduce deviations that affect the calculation of power losses, surge impedance loading (SIL), and transient performance—particularly under switching manoeuvres and high-surge impedance loading (HSIL) conditions. Therefore, the central aim of this work is to address the implications introduced by such approximations.

Therefore, this paper evaluates the influence of approximate versus exact internal impedance formulations on the modelling of HSIL HWTLs. Unlike previous studies that primarily focus on the computational efficiency of different formulations [7], this study emphasises the accuracy of the resulting electrical models. Through simulations

### Table 1: Input data of the OHTLs.
| Description | Unit | TL1 | TL2 | TL3 |
|---|---|---|---|---|
| Voltage level | | 440 | 765 | 800 |
| N◦ of conductors | – | 4 | 6 | 8 |
| Internal radius | mm | 4.64 | 4.135 | |