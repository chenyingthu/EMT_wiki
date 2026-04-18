# Spurious power and its elimination in modular multilevel converter models

**Anton Stepanov**$^{a,⁎}$, **Hani Saad**$^{b}$, **Ulas Karaagac**$^{c}$, **Jean Mahseredjian**$^{a}$

$^{a}$ Polytechnique Montreal, Montréal, Canada  
$^{b}$ Réseau de Transport d'Electricité, Lyon, France  
$^{c}$ Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong  

⁎ Corresponding author. E-mail address: anton.stepanov@polymtl.ca (A. Stepanov).

### Keywords
Arm equivalent model  
Average value model  
HVDC  
Modular multilevel converter  
Simulation  

### Abstract
This paper demonstrates the presence of spurious power generation or losses in two commonly used Modular Multilevel Converter (MMC) models: the Arm Equivalent Model (AEM) and the Average Value Model (AVM). Such power does not represent any physical phenomenon and appears due to numerical effects. It is demonstrated that spurious power is present when the model equations are not solved simultaneously with the surrounding electrical circuit equations, which is the case when the AEM and AVM are implemented using control system blocks. Depending on operating conditions and simulation parameters, such power can represent a significant part of the total converter station losses or even surpass them, thus making simulation results inaccurate. Several solutions to eliminate the spurious power are proposed for the AEM and AVM. Their effects are demonstrated in steady-state and transient conditions on a point-to-point MMC-HVDC simulation test case.

## 1. Introduction
Modular Multilevel Converter (MMC) shown in Fig. 1 is a Voltage Source Converter (VSC) topology that has several advantages in comparison with conventional two- and three-level power electronic converters. Increasing the number of sub-modules (SMs) per arm helps reduce or eliminate filters, improve reliability, and easily achieve scalability to higher voltages. In addition, MMCs have lower losses, lower switching frequency, lower transient peak voltages on IGBTs, and lower switching voltages. During normal operation, the desired AC voltage waveform is constructed by inserting or bypassing the appropriate number of SMs [1].

Due to the increased structural complexity of this type of converter compared to the conventional VSCs, a larger set of models is applicable in electromagnetic transient (EMT) simulations, including the detailed model (DM), the detailed equivalent model (DEM), the arm equivalent model (AEM), and the average value model (AVM) [2]. The choice of the model depends on the given simulated phenomenon and is usually associated with a compromise between required accuracy and tolerable computational burden [3].

The DM representing nonlinear characteristics of IGBTs and diodes offers a very high accuracy. However, this model is the slowest due to the significant number of nodes and nonlinearities [3,4]. The DEM simplifies the details of the nonlinear characteristics of power switches to only two states (ON and OFF) and uses Thevenin or Norton equivalent circuits to represent each converter arm, which considerably reduces computational burden [4].

The AEM hides individual SM details and deals with a single equivalent capacitor in each arm (see Fig. 2). This makes this model advantageous for a large set of grid studies where the converter behavior on SM level is disregarded [5]. The AVM combines all six arm capacitors into one, so only the external behavior of the converter is represented [4].

The MMC models can be implemented in different ways in an EMT-type software: the model equations can be incorporated into the main network equations (MNE) matrix, which eliminates the one-time-step delay between the model equations and the MNE. However, the main drawback is the inaccessibility of model equations to the user. Otherwise, the model equations can be implemented using control diagram blocks of the EMT software [6,7]. In this case, the drawback is the one-time-step delay between the solution of control system equations and the MNE.

In this paper it will be analytically demonstrated that in the second approach (models in control blocks), additional spurious power can occur, that affects the overall behavior of the circuit and makes the simulation results less reliable. Such spurious power has been researched in [8] and [9] but only the AEM has been considered. This paper extends the spurious power analysis presented in [8] to the AVM, which is often used with large time-steps so considerable effects of the spurious power can be expected. Several solutions to remediate the

The powers in (5) and (6) must be equal, because there is no other element that can consume, produce or store energy (as semiconductor losses are not considered in this equation). Considering (2), (6) can be rewritten as
$$p_{C_{tot}} = i_{C_{tot}} v_{C_{tot}} \quad (6)$$
When considering (1), (5), and (7) it is clear that $p_{arm} = p_{C_{tot}}$, so no spu