# Evaluation of the extended modal-domain model in the calculation of lightning-induced voltages on parallel and double-circuit distribution line configurations

**Osis E.S. Leal**<sup>b, *</sup>, **Alberto De Conti**<sup>a</sup>

<sup>a</sup> Department of Electrical Engineering (DEE), Federal University of Minas Gerais (UFMG), Brazil  
<sup>b</sup> UTFPR – Federal University of Technology – Paraná, Pato Branco, Brazil

## Keywords
Lightning-induced voltages  
Distribution lines  
Transmission line modeling  
Electromagnetic transient simulators  
Extended modal-domain model

## Abstract
This paper evaluates the applicability of the extended modal-domain (EMD) model in the calculation of lightning-induced voltages on parallel and double-circuit distribution lines. The influence of a real and constant transformation matrix and of the fitting technique required in the model on the induced-voltage waveforms is also investigated. It is shown that the EMD model presents good accuracy in most of the tested configurations. Also, in most cases the influence of the frequency selected for the calculation of the transformation matrix required in the EMD model is minimal. On the other hand, the requirement of using strictly real poles and residues and the use of the built-in fitting tool available in the Alternative Transients Program (ATP) have both a detrimental influence on the accuracy of the EMD model, at least in the investigated cases.

## 1. Introduction
Lightning-induced voltage calculations on overhead distribution lines are mostly performed using transmission line theory, which is motivated by features like efficiency, accuracy, and possibility of implementation in electromagnetic transient (EMT) simulators [1-3]. Although the latter feature is of particular importance for the simulation of realistic networks including laterals, surge arresters, and transformers [4,5], it can actually be quite a demanding task because the user is expected to implement not only a code for the calculation of lightning electromagnetic fields and their coupling with the illuminated line, but also a lossy transmission line model for the calculation of the resulting transients [6]. In a recent paper, De Conti and Leal [6] proposed two models that make it possible to calculate lightning-induced voltages simply by adding independent current sources to both ends of lossy transmission line models that are already available in the libraries of EMT simulators. By using the proposed models, the user does not need to implement a dedicated transmission line model to solve the transients on the line, which greatly simplifies the process.

One of the models proposed in [6], called extended phase-domain (EPD) model, solves telegrapher’s equations including the influence of external electromagnetic fields directly in the phase domain and is compatible with the universal line model (ULM) [7]. The EPD model can be used to calculate lightning-induced voltages on overhead distribution lines with arbitrary configuration even if the associated eigenvectors present a large variation with frequency, which is a characteristic commonly observed in lines with strongly asymmetric configuration and underground cables [6-8].

The other model proposed in [6], called extended modal-domain (EMD) model, uses modal decomposition techniques assuming a real and constant transformation matrix to solve telegrapher’s equations including the influence of external electromagnetic fields. This model is compatible with Marti’s model [9], which is expected to perform accurately as long as the line geometry is not strongly asymmetric. If this assumption is violated, the associated eigenvectors present a stronger variation with frequency and, consequently, the assumption of a real and constant transformation matrix may no longer hold. In practice, however, it is often difficult to characterize the line configuration simply in terms of its asymmetry. In fact, it was demonstrated in [10] that Marti’s model can be used to simulate transients with accuracy at least comparable to ULM for a wide range of transmission line configurations. However, the analysis was restricted to switching transients on high-voltage lines. No similar study has been presented so far dealing with voltages induced by nearby lightning strikes on distribution lines.

In [6] and [11] it was shown that the EMD model predicts lightning-induced voltage waveforms in excellent agreement with the EPD model and the finite-difference time-domain (FDTD) method. However, the investigated cases were restricted to a single-circuit compact distribution line [11] and a typical medium-voltage (MV)/low-voltage (LV) line configuration [6]. It is still unclear whether the EMD model maintains its accuracy for more complex configurations, such as parallel and double-circuit distribution lines.

For the calculation of the incident electromagnetic fields, Barbosa and Paulino’s equations [15-17] that include the influence of a lossy ground on the horizontal component of the incident electric field were used. The formulation is written directly in the time domain assuming the transmission line (TL) return-stroke model [18] to represent the return-stroke current propagation. The channel-base current was modeled as the sum of two Heidler functions whose parameters are described in [19], taking as reference the median parameters of subsequent currents measured at Morro do Cachimbo, Brazil. It has a peak value of 16 k

---
*This paper was supported by the National Council for Scientific and Technological Development (CNPq), grant 306006/2019-7, and by the State of Minas Gerais Research Foundation (FAPEMIG), grant TEC-PPM-00280-17. Paper submitted to the International Conference on Power Systems Transients (IPST2021) in Belo Horizonte, Brazil June 6–10, 2021.*  
* Corresponding author.  
E-mail addresses: osisleal@utfpr.edu.br (O.E.S. Leal), conti@cpdeee.ufmg.br (A. De Conti).  
https://doi.org/10.1016/j.epsr.2021.107100  
Received 26 October 2020; Received in revised form 22 January 2021; Accepted 28 January 2021  
Available online 23 February 2021  
0378-7796/© 2021 Elsevier B.V. All rights reserved.