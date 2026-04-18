# Computation of ground potential rise and grounding impedance of simple arrangement of electrodes buried in frequency-dependent stratified soil

Anderson R.J. de Araújo $^{a,*}$, Jaimis S.L. Colqui $^{b}$, Claudiner M. de Seixas $^{c}$, Sérgio Kurokawa $^{b}$, Bamdad Salarieh $^{d}$, José Pissolato Filho $^{a}$, Behzad Kordi $^{d}$

$^{a}$ University of Campinas, SP, Brazil
$^{b}$ São Paulo State University, SP, Brazil
$^{c}$ Federal Institute of São Paulo-IFSP, SP, Brazil
$^{d}$ University of Manitoba, Winnipeg, MB, Canada

**Keywords:** Electromagnetic transients, Lightning, Grounding impedance, Stratified soil, Frequency-dependent soil

**Abstract:** Grounding electrodes are used to provide a low-impedance dissipation path for the excess lightning or fault currents. Several studies have been dedicated to the computation of the grounding impedance of different electrode arrangements considering either the frequency dependence of soil parameters (resistivity $\rho$ and relative permittivity $\varepsilon_r$) or the multi-layer nature of soil. This paper aims at the calculation of the grounding impedance and the ground potential rise (GPR) of simple electrode arrangements (vertical and cross electrodes) due to the injection of first and subsequent lightning currents in various configurations of soil, considering a frequency-dependent stratified soil.

A frequency-domain full-wave electromagnetic solver based on the Method of Moment (MoM) that employs a stratified medium Green’s function is used to compute the grounding impedance in a frequency range of 100 Hz to 10 MHz. The transient GPRs are computed using the equivalent circuit of the grounding system, obtained through the application of the Vector Fitting (VF) technique and recursive convolution method.

The simulation results show that considering the frequency dependence of the soil parameters has no effect on the low-frequency grounding impedance up to $\approx 10$ kHz. However, the frequency dependence of soil parameters leads to a considerable variation of the grounding impedance at higher frequencies especially for soils of higher resistivity. Furthermore, it is shown that considering the layers of soil has a more significant impact on the GPR of the vertical electrode than that of the cross electrode.

## 1. Introduction

Grounding systems play a fundamental role for the protection and stability of electrical power systems. Power systems are subjected to several transient events such as lightning strikes or faults with high-amplitude currents and grounding systems must properly dissipate the excess current into the soil. Furthermore, grounding electrodes provide protection for humans in the surrounding area of the affected structure and prevent damage to the facilities and equipment during transients or faulty operational conditions. A grounding system having a low impedance is required to mitigate the surge overvoltages caused by lightning strikes in transmission lines [1,2]. Additionally, it is necessary to dissipate the fault current in a way to minimize the step and touch voltages around the affected structure [3,4]

In this context, there are several factors to be taken into account to accurately compute the grounding impedance in power systems, such as: (i) arrangement of the grounding conductors; (ii) frequency dependence of the soil electrical parameters; (iii) multi-layer structure of soil; (iv) mutual coupling between the segments of grounding system; and (v) the soil ionization effect [5,6]. Concerning the grounding arrangement, cylindrical conductors buried either as driven vertical electrodes (rods) or horizontal electrodes (counterpoises) or combination of these are used to achieve a low grounding impedance. As an example, the cross topology that combines the vertical and horizontal electrodes is described and analysed in [7–9]. Long vertical electrodes have the advantage of reaching deep layers of soil with lower resistivity [10]. Any electrode arrangement should guarantee that the ground potential rise (GPR) is below a threshold to avoid danger to equipment and personnel working nearby these grounding systems.

An important characteristic of soil is the frequency dependence of the its electrical parameters (relative permittivity $\varepsilon_r$ and resistivity $\rho$) [2, 11–14]. These electrical parameters are significantly affected by the frequency, especially at the high frequencies and for soil of high resistivity and water content [2,15,16]. The frequency dependence of soil parameters has been extensively investigated in the literature and several formulae have been developed based on measurements on soil samples in laboratory and field experiments [12,13,17]. As a consequence of considering the frequency dependence of soil parameters in the grounding performance

$$
\varepsilon_r(f) = \begin{cases}
7.6 \times 10^3 f^{-0.4} + 1.30 & f \geqslant 10 \text{ kHz} \\
192 & f < 10 \text{ kHz}
\end{cases} \tag{2}
$$

where $\rho_0$ is the DC resistivity measured at a frequency of 100 Hz. These expressions are used in this paper to compute the grounding impedance where each layer of soil is modeled as having frequency-dependent $\rho(f)$

*Fig. 1. View of the cross electrode in the simulation software FEKO.*