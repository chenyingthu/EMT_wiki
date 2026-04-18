# Coupling model for time-domain analysis of nonparallel overhead wires and buried conductors in the presence of lossy ground

Manuja Gunawardana, Behzad Kordi ∗  
Department of Electrical & Computer Engineering, University of Manitoba, Winnipeg, MB, Canada R3T 5V6

**Keywords:** Transmission line theory, Nonuniform transmission lines, Electromagnetic analysis, Time-domain analysis, Underground electromagnetic propagation

**Abstract**  
Buried conductors crossing paths with overhead transmission lines is a common occurrence. Interference caused by overhead lines has been found capable of affecting the safe, sustainable operation of the buried conductors. Such occurrences introduce an electromagnetic problem of a nonparallel structure with conductors present in both air and ground half-spaces. Electromagnetic transient (EMT) simulations of such structures are vital in predicting the behaviour of modern power networks. This paper develops a novel EMT compatible time-domain model for nonparallel overhead wires and conductors that are buried in a frequency-dependent lossy (finitely-conducting) ground. Analytical expressions are derived for the per-unit-length (PUL) impedance and admittance matrices based on thin-wire electromagnetic scattering theory. The closed-form formulations derived in this work can be easily incorporated in an EMT simulator to calculate the coupling effect between nonparallel overhead lines and buried conductors. The validity of the proposed approach is examined for various values of the ground conductivity, the radius of the buried conductor, the crossing angle, and burial depth of the conductor by comparing with results with those obtained using a full-wave approach. A case study on the induced voltage in buried conductors due to typical lightning transients in overhead lines has also been performed.

∗ Corresponding author.  
E-mail addresses: gunawams@myumanitoba.ca (M. Gunawardana), behzad.kordi@umanitoba.ca (B. Kordi).

https://doi.org/10.1016/j.epsr.2022.108788  
Received 22 April 2022; Received in revised form 7 August 2022; Accepted 2 September 2022  
Available online 15 September 2022  
0378-7796/© 2022 Elsevier B.V. All rights reserved.

## 1. Introduction

Buried conductors such as pipelines or communication and power cables, that share the spatial corridor or crossing paths with overhead power transmission lines, is a common occurrence in modern power networks [1–3]. At such occurrences, overhead power lines have the potential to create induced power-frequency or transient voltages in the buried conductor [4,5]. In the case of pipelines, this arises the danger of electric shock while induced currents affect corrosion protection mechanisms in pipelines [2,6,7]. Therefore, electromagnetic transient (EMT) analysis of such structures is important for the safe and sustainable operation of the network as well as for the safety of the technical personnel.

An overhead power line crossing a buried conductor in finitely conducting ground introduces an electromagnetic problem of a nonuniform structure with conductors present in both half-spaces (i.e. air and ground). Classical transmission line models based on Telegrapher’s equations used in EMT simulators [8,9] assume the lines have a uniform cross-section. To accurately model nonuniform structures, full-wave electromagnetic techniques can be used, however, the computation burden associated with them makes them not very suitable to be used in EMT simulators [3,10]. Computational complexity of full-wave models can be simplified by using the thin-wire approximation [11]. In order to apply the thin-wire approximation, the cross sectional radius of a wire should be much smaller than its length while the length is comparable with the minimum wavelength of interest [12]. Power transmission lines and pipelines under typical power system transients satisfy this requirement. Thin-wire scattering models along with image theory has been used to model crossing and bent overhead wires placed above perfect electric conducting (PEC) ground in [13–15]. An EMT-compatible model for nonparallel overhead conductors above finitely conducting ground, namely the dispersive scattered field transmission line model (DSFTL) was introduced by the authors in [16] based on thin-wire scattering theory and complex image theory. In [16], space-dependent, closed-form formulas for the per-unit-length (PUL) impedance and admittance matrices have been obtained in order to represent the nonparallel nature of wires. Image-theory-based models for the case of uniform buried conductors have been discussed in [17–19]. However, to the best of our knowledge, the image-theory-based models have not been developed for the coupling between overhead wires and buried conductors.

Pollaczek developed an expression for the mutual impedance between parallel overhead and buried wires in the form of an infinite integral (see [20] for details). Pollaczek’s integral does not have an analytical solution and is highly unstable during numerical integration [20,21]. Also, Pollaczek’s integral as well as Carson’s integral [22] used for overhead lines are not applicable to conductors that are nonparallel to each other. Therefore, several researchers have developed closed-form

*Fig. 1.* A schematic of an overhead transmission line above a conductor buried in finitely-conducting ground at a depth of $d$ with a crossing angle of $\alpha$.

### 2.1. DSFTL model for overhead and buried conductors

Transmission line equations for a nonuniform wire structure in the frequency domain are [27]