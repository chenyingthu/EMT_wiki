# Effect of frequency-dependent soil parameters on wave propagation and transient behaviors of underground cables

Haoyan Xue$^{a,*}$, Akihiro Ametani$^{b}$, Yanfei Liu$^{c,1}$, Jeewantha De Silva$^{d,1}$

$^a$ African Office, Global Energy Interconnection Development and Cooperation Organization (GEIDCO), Bole Sub City, Addis Ababa, Ethiopia
$^b$ The Department of Electrical Engineering, University of Manitoba, 66 Chancellors Cir, Winnipeg, Manitoba R3T 2N2, Canada
$^c$ Independent Consultant, Ningxia International Language College, Yinchuan, Ningxia, China
$^d$ Manitoba Hydro International Ltd, 211 Commerce Drive, Winnipeg, Manitoba R3P 1A3, Canada

$^*$ Corresponding author. E-mail address: haoyan-xue@geidco.org (H. Xue).
$^1$ Co-authors.

**Keywords:** Underground cables, Frequency-dependent soil parameter, Earth-return impedance / admittance, Wave propagation, Transient simulations

**Abstract:** This paper investigates the influence of frequency-dependent (FD) soil parameters in comparison to the constant soil (CS) parameters on wave propagations and transient characteristics of underground cables. Various FD soil models are summarized, and the calculated results of the FD soil parameters are compared with independent measured FD soil data. Longmire / Smith (LS) model is found to show the best agreement with the measured results. The frequency responses of wave propagations on underground cables are studied by the recently proposed extended transmission line (TL) approach together with the CS and the LS FD soil models. Calculated transient responses show more attenuation with a large soil resistivity at 100 Hz in comparison with those with a small soil resistivity at 100 Hz. Further, the transient voltage responses of a cross-bonded cable are compared with the transients solved by the Cable Constants and the existing FD soil routine in an EMT-type simulation tool, and a significant difference is observed.

## 1. Introduction

Surge analysis in power transmission systems requires accurate calculations of earth-return parameters. The earth-return impedance formula of underground cables was initially developed by Pollaczek [1]. It was further modified by Sunde to include the soil permittivity [2]. Fundamental underground cable modeling and wave propagation characteristics have been investigated by Wedepohl [3]. Also, a systematic study of modal sensitivities of propagation constants on underground cables was performed by Indulkar [4]. Wait and Bridges [5,6] independently derived formulas of the earth-return impedance and admittance for a single underground cable based on an exact expression from electromagnetic theories. More generalized earth-return impedance and admittance formulas for a multi-phase underground cable were derived in [7–11].

Those papers investigated the influence of the constant soil (CS) parameters on wave propagations and transient characteristics of underground cables adopting the derived earth-return impedance and admittance formulas, although the soil parameters are frequency-dependent (FD) as is well-known in [12–19].

Recently, Papadopoulos studied the impact of FD soil properties on electromagnetic field propagations in a single phase underground cable by adopting his earth-return impedance and admittance formulas of underground cables [8,20]. It shows a significant influence of FD soil properties for the wave propagations and transient characteristics of an underground cable. However, the single phase cable investigated in [20] only involves the earth-return mode propagation, and thus the mixed propagation characteristics of a multi-phase underground cable with the CS and the FD soil characteristics require further studies.

Based on the above facts, Section 2 in this paper briefly reviews and summarizes various FD soil models [12–14,18]. The FD soil parameters using values of soil resistivity at 100 Hz based on a logarithmic sampling method [21] are calculated by different FD soil models. The overall characteristics of the FD soil parameters are made clear. Also, some typical calculations [19] of FD soil resistivity and permittivity are performed and compared with the measured results of soil [22,23], and the numerical values are summarized in Appendix A.1.

In Section 3, the series impedance and shunt admittance on the underground cables [20] are calculated by a recently proposed extended transmission line (TL) approach in Appendix A.2 [11] with the CS model and the Longmire / Smith (LS) FD soil model [14] which shows more reasonable agreement with the given measured FD soil data in Appendix A.1. Also, the wave propagation characteristics of the cable are evaluated.

Section 4 performs surge simulations of different modes and presents transient simulations for a cross-bonded cable [24] by adopting the extended TL approach with the CS and the LS soil models. The calculated transient responses show more attenuation with a large soil resistivity at 100 Hz in comparison with those with a small soil resistivity at 100 Hz. Further, the transient voltage responses of a cross-bonded cable are compared with the transients solved by the Cable Constants and the existing FD soil routine in an EMT-type simulation tool, and a significant difference is observed.

$$ \sigma(f) = \left[ \sigma_0 + 1.26 \sigma_0^{0.27} \left( \frac{f}{10^6} \right)^\gamma \right] \cdot 10^{-3} \text{ (mS/m)} \tag{5} $$

$$ \varepsilon_r(f) = \varepsilon_{r\infty} + 1.26 \cdot 10^{-3} \tan\left(\frac{\pi \gamma_{av}}{2}\right) \sigma(f) $$