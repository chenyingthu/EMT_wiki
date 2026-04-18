# Real-time RMS-EMT co-simulation and its application in HIL testing of protective relays

**Renzo Fabián Espinoza** a, *, **Guilherme Justino** a, **Rodrigo B. Otto** a, **Rodrigo Ramos** b  
a Itaipu Technological Park Foundation, Foz do Iguaçu, PR, Brazil  
b São Carlos School of Engineering, University of Sao Paulo, SP, Brazil  

*Paper submitted to the International Conference on Power Systems Transients (IPST2021) in Belo Horizonte, Brazil June 17–20, 2021.*  
\* Corresponding author.  
E-mail addresses: renzo.espinoza@pti.org.br (R. Fabián Espinoza), guilherme.justino@pti.org.br (G. Justino), rodrigobueno@pti.org.br (R.B. Otto), rodrigo.ramos@ieee.org (R. Ramos).

**Keywords:** Real-time simulation, Co-simulation, Hardware-in-the-loop, Protective relay, Multi-domain, Multi-rate

**Abstract**  
This work proposes an interfacing technique that uses the built-in three-phase transmission line models available in simulation platforms to perform Root Mean Square (RMS)- Electromagnetic Transient (EMT) real-time, multi-domain and multi-rate co-simulation. The main objective of this paper is to show the application of this kind of simulation in hardware-in-the-loop (HIL) testing of protective relays. Two well-known platforms are considered in this work: OPAL-RT with its ePhasorSim tool is used for RMS simulation, and RTDS is used for EMT simulation. However, the proposed technique is sufficiently general to be applied to other real-time simulation platforms that have similar built-in transmission line models. To convert waveforms to phasors, a non-buffered rapid curve fitting method was implemented to attend to real-time constraints. During the testing phase of this research, tests for the HIL were completed using an actual transmission line protection relay. The presented results of tests highlight the benefits of the proposed interfacing technique.

## 1. Introduction

The computational process involved in real-time simulations requires calculations to be finished before the end of each time step. Therefore, the size of the modeled electrical system is limited to enable the real-time simulation. In the case of Electromagnetic Transient (EMT) approach to conduct Hardware-in-the-Loop (HIL) tests by means of digital real-time simulation, usually the electrical system to be studied is reduced considering this limitation, using Thevenin equivalents. This practice is common in HIL protective relay tests. This reduction eliminates the dynamics of the reduced part and, thus, a co-simulation multi-domain approach is interesting because it maintains the EMT details of the studied circuit and the dynamics of the external circuit.

There is increasing interest among utilities in performing real-time simulations of large power systems. If a large power system is simulated using EMT real-time simulators, the cost of hardware can be restricting to many users. There have been many efforts to develop real-time multi-domain co-simulation platforms where the portion of the network that needs to be modeled with details is done so using EMT models, while the remaining part is modeled using Root Mean Square (RMS) models [1–15]. A vast review of advanced laboratory technique methods that include co-simulation frameworks is presented in [16].

This work proposes a transmission line interfacing technique that uses the built-in transmission line models available on real-time simulators to conduct real-time, multi-domain, and multi-rate co-simulation using OPAL-RT and RTDS platforms. The ePhasorSim [17] tool of OPAL-RT is used as the RMS simulator, and RTDS is used as the EMT simulator. The analog inputs and outputs of both simulators are used as communication interface. RTDS is an EMT-focused simulator that requires detailed modeling and time steps on the order of microseconds; on the other hand, ePhasorSim allows the RMS simulation and can run using time steps on the order of milliseconds. Therefore, it is possible to conduct a detailed EMT simulation interacting with an RMS simulation that allows the user to expand the studied electrical system and explore the benefits of both approaches. The main purpose of this work is to allow RMS-EMT real-time HIL tests of protective relays having the external electrical power system in an RMS solution and the electrical system of interest in an EMT solution. The EMT part interacts directly with the protective relay under test.

The remainder of this paper is structured as follows. In section II, the proposed technique is described. In section III, the results of tests considering two transmission systems of four and five buses are analyzed, as well as HIL tests using a real protective relay. Finally, section IV presents the main conclusions of this work and address future directions for research.

## 2. The proposed transmission line interface

EMT). Fig. b shows a simplified single phase lossless model of the transmission line used by EMT solution (RTDS in this case). It is the Bergeron model of transmission line [22], where,

$$i_{km}(t) = \frac{v_k(t)}{Z_c} + h_k(t-\tau) \quad (1)$$

$$i_{mk}(t) = \frac{v_m(t)}{Z_c} + h_m(t-\tau) \quad (2)$$