# Modal propagation characteristics and transient analysis of multiconductor cable systems buried in lossy dispersive soils

T.A. Papadopoulos a, Z.G. Datsios b, c, A.I. Chrysochos d, P.N. Mikropoulos b, G.K. Papagiannis b, *
a Power Systems Laboratory, Department of Electrical and Computer Engineering, Democritus University of Thrace, Xanthi 67100, Greece
b School of Electrical and Computer Engineering, Aristotle University of Thessaloniki, Thessaloniki 54124, Greece
c Department of Electrical and Computer Engineering, University of Western Macedonia, Kozani 50131, Greece
d R&D Department of Hellenic Cables, Maroussi, 15125 Athens, Greece

**Keywords:** Earth conduction effects, Electromagnetic transients, Frequency-dependent soil properties, Modal analysis, Power cables, Wave propagation

**Abstract:** In surge analysis, an important issue is the influence of the imperfect earth on the propagation characteristics of the conductors. In this paper, the wave propagation characteristics and the transient performance of underground multiconductor cable systems in flat, vertical and trefoil arrangement are investigated. The Longmire and Smith frequency-dependent (FD) soil model as well as a generalized earth formulation are considered, taking into account in the analysis the impact of earth conduction effects on both the series impedance and shunt admittance of the cable conductors and sheaths. Comparisons are carried out with approximate earth formulations, neglecting the influence of imperfect earth on shunt admittances. Finally, resonance frequency analysis and transient simulations are performed for the different cable arrangements to evaluate the importance of FD soil modeling and earth formulation per cable arrangement.

## 1. Introduction

The propagation characteristics and the transient performance of multiconductor cable systems can be analyzed in terms of natural modes of propagation; these are calculated on the basis of the per-unit length impedance and admittance matrices of the cable systems by applying proper modal transformations [1, 2]. The modal propagation characteristics of different cable configurations and their sensitivities to the electromagnetic (EM) and geometrical properties of the system under study have been systematically investigated in [2–5]. It is important to indicate that in these works the analysis is based on two specific assumptions regarding earth conduction effects on propagation characteristics:

- The influence of the imperfect earth is considered only on the cable impedance; thus, cable admittance earth conduction effects are neglected. This implies that the earth is assumed to act as an electrostatic shield and the accuracy of such approaches is limited to low-frequency applications [6], e.g., up to a few kHz. Many efforts to develop expressions for the series impedances have been reported in literature, with the most known proposed by Pollaczek [7], being implemented in EMT-type simulation tools, and by Sunde [8], that extends [7] by including the influence of earth permittivity.
- The electrical properties of the soil, i.e., conductivity and permittivity are assumed constant; however, in reality they are frequency-dependent (FD) [6, 9–23].

In order to develop more accurate earth models, approaches involving earth correction terms for both the impedance and admittance of underground cables have been proposed in [24–26], raising the first of the above assumptions.

Additionally, several models have been proposed for the prediction of the FD soil electrical properties [9–21, 23], as summarized in [22] and [23]. However, only a few recent studies have used FD soil models to investigate the propagation characteristics and the transient performance of underground cable systems [6, 27, 28], revealing a significant influence especially for short cable lengths [6]. In particular, in [6] guidelines for the accurate evaluation of earth conduction effects on the transient performance of underground multiconductor cable systems have been introduced. However, the analysis has been presented only for cables in flat formation.

This paper extends previous work [6] by investigating the propagation characteristics and the transient responses of different multiconductor, underground cable systems, i.e., flat, vertical and trefoil arrangements. The propagation characteristics of the cable system are calculated by using the FD soil model of [12], considering both the generalized earth formulation of [24] and the approximate earth formulation of Sunde [8]. Results are compared and discussed also on the basis of EM transient responses, demonstrating the applicability of the guidelines introduced in [6] for the investigation and accurate evaluation of earth conduction effects on the transient performance of underground cable systems.

## 2.2. Earth formulation criterion

calculated as [22]
$$f_n = 10^{n-1} (125 \sigma_{1,DC})^{0.8312} \tag{3}$$

Note that the Longmire and Smith model can also be considered as appropriate for EMT simulations with $f < 100$ Hz. This is because the predicted decrease of soil conductivity with decreasing frequency is in line with experimental results on actual soils, such as those of [19].