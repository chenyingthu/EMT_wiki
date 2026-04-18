## Assessment of the transmission line theory in the modeling of multiconductor underground cable systems for transient analysis using a full-wave FDTD method

Naiara Duarte a, *, Alberto De Conti b, Rafael Alipio a, 1, Farhad Rachidi a

a Electromagnetic Compatibility Laboratory, Swiss Federal Institute of Technology in Lausanne (EPFL), 1015, Switzerland
b Department of Electrical Engineering, Universidade Federal de Minas Gerais (UFMG), 31270-901, Brazil

* Corresponding author.
E-mail addresses: naiara.duarte@epfl.ch (N. Duarte), conti@cpdee.ufmg.br (A. De Conti), rafael.alipio@cefetmg.br (R. Alipio), farhad.rachidi@epfl.ch (F. Rachidi).
1 on leave from the Federal Center of Technological Education of Minas Gerais

https://doi.org/10.1016/j.epsr.2023.109570
Received 13 December 2022; Received in revised form 14 February 2023; Accepted 21 June 2023
Available online 1 July 2023
0378-7796/© 2023 Published by Elsevier B.V.

## Keywords
Electromagnetic transients
Ground-return admittance
Ground-return impedance
Transmission line theory
Underground cable systems

## Abstract
In this paper, a rigorous and independent validation of two different approaches for calculating the ground-return impedance and admittance of multiconductor underground cable systems using the transmission line theory is carried out. Furthermore, analyses are performed to evaluate the accuracy of a closed-form approximation for the calculation of the ground-return admittance of underground cable systems. The validations are based on the full-wave finite-difference time-domain (FDTD) method and consider the calculation of transients on flat and trefoil underground cable arrangements for different excitation types. Short cable lengths of 50 m and 100 m and soil resistivities of up to 1000 Ωm are considered. The results demonstrate the validity of the transmission line theory for the calculation of fast transients (with risetimes as low as 0.2 µs) on underground cables provided the ground-return parameters are rigorously determined, with the advantage of presenting much greater efficiency and easiness to implement in electromagnetic transient simulators compared to the full-wave FDTD method. Lastly, it is shown that the ground-return admittance approximation, despite its simplicity, leads to results comparable to those obtained through more complete formulations for the calculation of transients in underground cables, but more efficiently and without significant loss of accuracy.

## 1. Introduction
THERE has been a renewed interest in the search for more accurate models for the simulation of electromagnetic transients in underground cables using the transmission line theory, including a more rigorous calculation of the ground-return parameters [1]. It has been shown, for example, that neglecting the ground-return admittance leads to inaccurate results in the simulation of high-frequency transients, especially for high-resistivity soils [1–5]. However, most electromagnetic transient (EMT)-type simulators still neglect this parameter in the calculation of the per-unit-length cable parameters [6]. This may compromise the accuracy of insulation coordination studies, especially in case of short cable sections used in grid-connected renewable energy sources and hybrid overhead/underground line systems [7,8], which present natural frequencies reaching hundreds of kHz and beyond.

Different approaches have been proposed to calculate the ground-return parameters of underground cables [5,9–13]. Recent contributions include the formulations of Papadopoulos et al. [5] and Xue et al. [13], which were derived based on a quasi-TEM approximation of the modal equation resulting from the application of the Hertz potentials to solve the problem of a buried dielectric-coated wire. The overall consistency of these formulations has been confirmed via comparisons with existing expressions [1,5,13,14] or frequency-domain studies taking as reference full-wave electromagnetic models [15,16]. However, their validity for the simulation of transients on multiconductor underground cable systems has not been fully demonstrated.

A first attempt to provide a rigorous and independent validation of the expressions proposed by Papadopoulos et al. [5] and Xue et al. [13] for the calculation of transients in underground cables was carried out by the authors in [17] using the full-wave finite-difference time-domain (FDTD) method. Nevertheless, only the case of a single underground cable was considered. Here, the analysis presented in [17] is extended to

**Fig. 1.** Cable system configurations: (a) flat and (b) trefoil.

**Fig. 2.** (a) Longitudinal and (b) lateral excitations.

**Fig. 3.** Voltage waveforms calculated at the receiving ends of phases A (left) and C (right) considering a cable length of 50 m, soil resistivities (a) 200 Ωm and (b) 1000 Ωm and longitudinal excitation for a horizontal configuration.

**Fig. 4.** Voltage waveforms calculated at the receiving ends of phases A (left) and C (right) considering a cable length of 100 m, soil resistivities (a) 200 Ωm and (b) 1000 Ωm and longitudinal excitation for a horizontal configuration.

**Fig. 5.** Voltage waveforms calculated at the receiving ends of phases A (left) and C (right) considering a cable length of 50 m, soil resistivities (a) 200 Ωm and (b) 1000 Ωm and longitudinal excitation for a trefoil configuration.