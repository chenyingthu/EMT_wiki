# Proposal of an alternative transmission line model for symmetrical and asymmetrical configurations

Eduardo Coelho Marques da Costa $^{a,\ast}$, Sérgio Kurokawa $^{b,2}$, Afonso José do Prado $^{b,2}$, José Pissolato $^{a,1}$

$^a$ Unicamp – Universidade Estadual de Campinas, Mail Box 6101, CEP 13081-970, Campinas, SP, Brazil  
$^b$ Unesp – Univ. Estadual Paulista, Av. Brasil Centro 56, Mail Box 31, CEP 15385-000, Ilha Solteira, SP, Brazil

**Abstract**  
This article shows a transmission line model for simulation of fast and slow transients, applied to symmetrical or asymmetrical configurations. A transmission line model is developed based on lumped elements representation and state-space techniques. The proposed methodology represents a practical procedure to model three-phase transmission lines directly in time domain, without the explicit or implicit use of inverse transforms. In three-phase representation, analysis modal techniques are applied to decouple the phases in their respective propagation modes, using a correction procedure to set a real and constant matrix for untransposed lines with or without vertical symmetry plane. The proposed methodology takes into account the frequency-dependent parameters of the line and in order to include this effect in the state matrices, a fitting procedure is applied. To verify the accuracy of the proposed state-space model in frequency domain, a simple methodology is described based on line distributed parameters and transfer function associated with input/output signals of the lumped parameters representation. In addition, this article proposes the use of a fast and robust integration procedure to solve the state equations, enabling transient and steady-state simulations. The results obtained by the proposed methodology are compared with several established transmission line models in EMTP, taking into account an asymmetrical three-phase transmission line. The principal contribution of the proposed methodology is to handle a steady fundamental signal mixed with fast and slow transients, including impulsive and oscillatory behavior, by a practical procedure applied directly in time domain for symmetrical or asymmetrical representations.

**Keywords:** Electromagnetic transients, Transmission line parameters, Lumped parameters, State-space

**Article history:**  
Received 1 November 2009  
Received in revised form 15 March 2011  
Accepted 3 June 2011  
Available online 5 July 2011

$\ast$ Corresponding author. Tel.: +55 1935213755.  
E-mail addresses: educosta@dsce.fee.unicamp.br (E.C.M. da Costa), kurokawa@dee.feis.unesp.br (S. Kurokawa), afonsojp@uol.com.br (A.J. do Prado), pisso@dsce.fee.unicamp.br (J. Pissolato).  
$^1$ Tel.: +55 1935213755.  
$^2$ Tel.: +55 1837431129.

## 1. Introduction

There are several transmission line models available in the Electromagnetic Transient Program (EMTP) and Alternative Transient Program (ATP) based on lumped and distributed parameters.

From a lumped parameters model, the line is represented by multiple elemental sections connected in cascade. An approach of the distributed nature of the line parameters can be adequately obtained, considering the transient frequency range, line length and a sufficient number of nominal elements.

When a lumped parameters line model is adopted, the representation of the differential equations in state space is an alternative way to carry out simulations directly in time domain, without the explicit use of inverse transforms, by using of numerical or analytic integration methods [1]. Therefore, it is possible to simulate electromagnetic transients taking into account time-variable and nonlinear components, such as corona effects and fault arcs [2–4], or when a detailed voltage and current profile is required [5]. These characteristics are some of the main advantages of line modeling by lumped elements instead a distributed-parameters model.

The distributed-parameters models are implemented directly from the two-port line representation in frequency domain and the time-domain simulations are performed by inverse transforms. This procedure represents a wide range of frequencies and the transients are calculated with good accuracy. However, the line models based on distributed parameters have restrictions in the inclusion of time-variable and nonlinear components in line modeling as well as when a detailed profile of current and voltage along the line is required [6].

Another fundamental aspect about transmission line modeling is the frequency dependence of the electric parameters. Several published papers show that the lumped parameters models have been developed without take into account the frequency dependence of the line longitudinal parameters [1–5] and then limiting the modeling accuracy. Furthermore, it is well known that models with constant parameters cannot adequately simulate the line response over the