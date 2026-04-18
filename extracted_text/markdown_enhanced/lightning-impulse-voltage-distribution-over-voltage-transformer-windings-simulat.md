## Lightning impulse voltage distribution over voltage transformer windings — Simulation and measurement

Bojan Trkulja a, Ana Drandić a,∗, Viktor Milardić a, Tomislav Župan a, Igor Žiger b, Dalibor Filipović-Grčić c  
a University of Zagreb, Faculty of Electrical Engineering and Computing, University of Zagreb, 10000 Zagreb, Croatia  
b Končar — Instrument Transformers Inc, 10000 Zagreb, Croatia  
c Končar Electrical Engineering Institute, 10000 Zagreb, Croatia  

∗ Corresponding author.  
E-mail address: ana.drandic@fer.hr (A. Drandić).

**Article history:**  
Received 25 August 2016  
Received in revised form 17 February 2017  
Accepted 22 February 2017  

**Keywords:**  
Voltage transformers  
Numerical simulation  
Electromagnetic transients  
Impulse testing  
Coils  
Internal overvoltages  

**Abstract**  
This paper presents a fast and precise method for the calculation of internal voltage transients over the voltage instrument transformer windings. Lumped circuit parameters of the transformer winding are calculated using self-developed solvers based on the boundary element method and integral equations approach. A detailed equivalent circuit of the transformer winding is solved in time domain. Test model of the voltage instrument transformer is constructed with a number of measurement points along the windings. Results of the calculation are in a good agreement with the measured voltages.

## 1. Introduction

Voltage transformers in a power system are designed to transform voltages from high voltage on a transmission level to low voltage necessary for relays and measurement equipment. During their operation, the voltage transformer’s windings are subjected to high frequency transient overvoltages due to switching operations and lightning strikes. Transient overvoltages can potentially lead to excessive electric stress in the transformer windings and insulation and consequently result in insulation failure and breakdown. In order to adequately dimension the transformer windings and interturn or interlayer insulation, the transient voltage distribution needs to be obtained on a design level. Considering the typical winding geometry of a voltage transformer, which normally entails a very large number of turns and discrete interlayer insulations, this is a complex task.

In order to model and simulate the transient voltage distribution, an equivalent electric circuit representation of distributed or lumped parameters is developed [1]. It is of great interest to calculate the equivalent parameters accurately since they have a major inﬂuence on transient voltages. They are commonly calculated using simple analytical formulas [1–3] or ﬁnite element method (FEM) based calculations [4–7]. Calculation of lumped circuit parameters can be performed using genetic algorithm [8]. Due to a complex geometry of system model, order reduction techniques can be employed [9]. In this paper, boundary element method and integral equations approach are employed to calculate the equivalent electric circuit parameters. The solvers for evaluating the parameters are self-developed and presented in Section 2.

The system of equations is often formulated using the methods based on Dommel’s approach [10–14]. Transient analysis can be performed in frequency domain [15,16] and time domain [4]. In this paper, a transient solver specially developed for this purpose, and based on formulations made by Dommel, is presented. Measurement based analysis of transformers can be based on frequency response analysis (FRA) methods [17].

Analysis of very fast transient overvoltages is of great interest and it has been the topic of various papers which mostly revolve around power transformers [18–26]. Even though some of those methods can be used in voltage transformers, their speciﬁc design differences make the transient analysis approach slightly different. The position of voltage transformers in substations and the large number of turns in the high voltage winding can lead to highly nonlinear voltage distribution during fast transients. This can result in high interturn voltages which can be hazardous to the insulation.

The purpose of this paper is to present the methodology for simulating the overvoltage distribution along the high voltage winding of the voltage transformer. As such, its goal is different from most of the EMTP (Electromagnetic Transients Program)-type programs used for simulation of the transferred overvoltages between the power transformers’ windings that are beneﬁcial to network operators. Presented method relies on the detailed geometry and material data of the transformer. Obtaining the interturn voltages can help transformer manufacturers during the design stage of the voltage transformer production.

Total charge on the j-th conductor inﬂuenced by the charge on the i-th conductor $Q_{ij}$ is:
$$ Q_{ij} = \int_{S_j} \sigma_j \, dS_j = \sum_{k=1}^{N} \sigma_{kj} S_{kj} \tag{3} $$
where $\sigma_{kj}$ is the surface charge density on the k-th segment of the j-th conductor and $S_{kj}$ is its surface, while N is the number of the ﬁnite segments of j-th conductor.

Capacitance matrix elements are calculated with equa