# A multi-solver framework for co-simulation of transients in modern power systems☆,☆☆

![](images/43571a637e2740196140ff9b33d2ed43177f1a9c3892890b131c4f179a59428b.jpg)

Janesh Rupasinghe a , Shaahin Filizadeh b,\* , Dharshana Muthumuni c , Ramin Parvari

a RTDS Technologies, Winnipeg, MB R3T 2E1, Canada

b Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB R3T 5V6, Canada

c Manitoba Hydro International, Winnipeg, MB R3P 1A3, Canada

## A R T I C L E I N F O

Keywords:   
Co-simulation   
Dynamic phasors   
Electromagnetic transient simulation   
Multi-rate simulation   
Transient stability

## A B S T R A C T

This paper develops a novel multi-rate, multi-solver co-simulation framework combining dynamic phasors, transient stability, base-frequency dynamic phasors for frequency-adaptive simulation of transients, and electromagnetic transient (EMT) models. This framework subdivides a given power network into several types of subsystems based on the connected devices, required accuracy in representing dynamic details, electrical distance from perturbations, and the intended purpose of the study; as such, the paper describes methods and guidelines to simulate each subsystem using the most appropriate solver and time-step size to maximize simulation efficiency and accuracy. It also addresses the tasks of multiple interfacing and solver interactions that are essential in coupling different solvers. The proposed framework is built around an industrial-grade EMT simulator, to which other solvers are interfaced, enabling access to a variety of power system models and distinct features. The accuracy and efficiency of the framework are demonstrated through co-simulations carried out on a modified version of the 118-bus network, which includes an MMC-HVDC system.

## 1. Introduction

Transients in modern power systems differ markedly in terms of frequency content and time scale, leading to a wide range of impacts on the system. Disturbance occurring at a particular location of the network often causes dissimilar dynamic responses in different network segments. The close electrical vicinity of the disturbance experiences a great amount of fast electromagnetic transients (EMT) while the rest of the network experiences far less or no noticeable dynamics depending on the electrical distance from the disturbance. In addition to transients caused by temporary events such as faults or control actions, there may be regions of the network that experience fast dynamics continually, such as the ones created by high-frequency power electronic systems that generate fast dynamics even during normal operation.

Among the tools used for power system transient simulations, the transient stability (TS) solvers focus on steady-state and low-frequency events; therefore, they allow large simulation time-steps (ms) and offer better computational efficiency. The EMT solvers are recognized for greater accuracy; they require small simulation time-steps (μs) that render them computationally prohibitive for simulating very large networks. Due to converter-tied resources and HVDC systems, and hence the reduced inertia, modern power systems are expected to contain a much richer spectrum of harmonics, and are more susceptible to farreaching transients. The limitations these aspects imposed on traditional solvers have led to co-simulators, which aptly employ proper solvers for different network segments to maintain simulation accuracy and efficiency [1]. As the demand mounts, alternative solution methods such as dynamic phasors (DPs) [2,3] and frequency-adaptive simulation of transients (FAST) [4] have been devised. DPs have sparked much interest as they allow to retain a considerable amount of waveform dynamics without compromising the computational benefits given by conventional phasors. The FAST method switches between an EMT solution with a small time-step and a DP solution with a large time-step by observing the network status. Challenges such as continuously occurring fast events and non-linear phenomena pose difficulties for both DP- and FAST-based methods to operate as standalone simulators.

Despite recent advances in EMT-TS co-simulation platforms [5–8], problems such as interaction delays, inaccuracies, and numerical instabilities, on the one hand, and the rapid rise of fast-acting systems, on the other hand, have necessitated further development of alternative solvers such as DP-EMT co-simulators [9,10] to improve the frequency bandwidth of simulations. Works in [11,12] show that co-simulation of EMT and TS solvers, with an intermediate DP layer, offers greatly enhanced accuracy. According to the findings in [13], co-simulation using FAST and EMT solvers yields a sophisticated multi-rate platform with unique benefits such as multi-modal operations, enhanced transient accuracy, and the ability to retain fast dynamics in all subsystems.

Incorporation of latest techniques into simulation tools is critical as the nature of modern power systems has changed and conventional dynamic simulation algorithms are no longer adequate. Modern power systems require modern and drastically more capable simulation programs. Thus, this paper develops a novel multi-solver co-simulation framework for the next generation of co-simulation engines. It combines multiple EMT subsystems with a base-frequency dynamic phasor solver for frequency-adaptive simulation of transients (BFAST solver) [13]. Additionally, a conventional TS solution is obtained at far enough portions of the network where fast network transients are essentially nonexisting. A set of guidelines for identifying subsystems, selecting multiple interfacing topologies, and developing interaction algorithms have also been presented.

## 2. Multi-solver co-simulation framework

The proposed multi-solver co-simulation architecture is illustrated in Fig. 1. In this context, several solvers are interfaced, each with distinct numerical features and algorithms. Solver interfacing schemes are classified broadly as core-type, chain-type, and loop-type according to [14]; the proposed framework uses a combination of core- and chaintype interfaces. The EMT subsystems are implemented inside an industrial-grade simulator (PSCAD/EMTDC), which serves as the core of the multi-solver co-simulator.

Use of multiple simulation time-steps and solution methods poses challenges, especially in interfacing the solvers and handling the interactions between them as time-delays and unequal granularity of samples on the opposite sides of interfaces cause complications. These difficulties may have an adverse effect on the numerical stability and accuracy of the overall solution, particularly during transients. Thus, in the context of a multi-solver environment, subsystems, interfaces, and interaction algorithms must be properly defined.

![](images/01e2acd60944dbc5fd5665de27ba66d18973871cb8a2d7cc868ccfc15069ce4d.jpg)  
Fig. 1. The proposed multi-solver co-simulation architecture.

## 2.1. Subsystems types

The proposed framework relies on EMT models to provide the highest level of accuracy; thus, the study areas that require high levels of accuracy are implemented in an EMT simulator. The rest of the network is segmented into several types of subsystems as follows:

## 2.1.1. EMT subsystem type 1

This is the area that undergoes continuous and high-frequency transients. This subsystem may include non-linear devices, power electronic systems, or other high-frequency device. Therefore, this subsystem needs to be solved using an adequately small simulation time-step (e.g., a few μs). This type of a subsystem is typically confined to small areas within a large network.

Segmentation of EMT subsystem 1 depends on the location of power electronic converters; however, if the guidelines to partition and interface each subsystem are followed, it does not affect the accuracy of the simulation. For different locations for the converter, the electrical distance between the converter and the other buses is the crucial factor for the time gain for it determines how many buses can be included in each type of subsystem. For a relatively small system, it is possible that there will not be enough electrical distance between the converter and the buses at the far ends of the network to include in the TS subsystems if the fast-acting devices are located, for instance, at a central location. However, this is not the case for larger systems with thousands of electrical buses, and hence the impact of location, if any, will be negligible.

## 2.1.2. EMT subsystem type 2

This subsystem is subjected to continuous or moderately fast transients, which are not as severe as in the EMT subsystem type 1. Thus, this subsystem is simulated using EMT models, but with a time-step larger than of the EMT subsystem 1 (e.g., tens of μs).

When segmenting EMT1 and EMT2, there is no specific rule to determine how many buses must be modeled in each EMT subsystem, other than there must be enough electrical distance between fast-acting devices and the interface buses. It is also worthwhile to note that it is not mandatory to have two EMT subsystems. If there are no extremely fastacting devices in the network or if the study does not require specially small time-steps, then the user may opt to include all the EMT models in a single subsystem.

If additional power electronic converter are present in other areas of the network, extra EMT subsystems must be included in the multidomain solver in order to address their unique modeling requirements. One must note that some converters may be modeled using average-value models if their switching transients are not of interest and they could be modeled in subsystems that use large time-steps.

## 2.1.3. BFAST subsystem

In this subsystem, fast dynamics occur intermittently. For example, a fault in one of the EMT subsystems may affect adjacent areas for a short period, and for the rest of the time this subsystem operates in steadystate or with relatively slow dynamics. Therefore, it is simulated with an adaptive solver known as the BFAST (see Section 2.2) that changes its simulation method and solution time-step depending on whether fast transients are present or not.

## 2.1.4. Dynamic phasor (DP) subsystem

In this subsystem, transients are slower than those observed in the EMT subsystems. Disturbances applied at the EMT subsystems have low dynamic impact on this region. Therefore, it is simulated with DPs using a large simulation time-step for the entire duration. DP subsystem(s) may be used as a buffer region between EMT and TS solvers.

## 2.1.5. TS subsystem

Areas of the network that operate in steady-state or near steady-state throughout the simulation are assigned to this subsystem. Typically, these subsystems fall far from EMT subsystems where fast transients are not prevalent. In these subsystems, only the positive-sequence solution is obtained using conventional phasor models. Therefore, any unbalanced condition is essentially ignored and a large simulation time-step is used.

Dynamic phasors capture both slow and moderately fast dynamics more accurately than a TS solver and more efficiently than an EMT solver. Moreover, the DP solver uses a large and fixed simulation timestep for its solution as it operates in the phasor domain. Therefore, the DP solver is suitable to be used as a buffer zone between an EMT subsystem and a TS subsystem rather than directly linking a TS to the EMT solver, which may provide complications in terms of accuracy and stability. The BFAST solver, on the other hand, adapts its solution method and the simulation time-step according to the frequency contents of the waveforms being simulated. When it detects a relatively high frequency transients, it uses a detailed EMT solution with a small time-step, and during steady-state or slowly varying dynamics, it reverts to a dynamic phasor solution with a large time-step. This implies that the BFAST solver is particularly effective when simulating subsystems that undergo fast transients for a short duration of the overall simulation.

For a given simulation, the network may consist of zero or multiple subsystem of a particular type. Assignment of subsystem types depends on such factors as the size of the network, presence of high-frequency and non-linear devices, and the expected dynamic details of various sub-regions of the network. While TS and EMT simulators are used to solve steady state and detailed behaviors of network subsystems, respectively, this framework needs more flexible simulator(s) to build a more versatile co-simulation engine. The BFAST solver developed in [13] provides such freedom by giving options to operate in different solution methods (BFAST, DP, and EMT) and to adjust time-step size based on the state of the network. The multi-solver co-simulation framework utilizes several simulation modes of this solver; thus, the basis of the BFAST simulator is explained below.

## 2.2. Operating principle of the BFAST solver

## 2.2.1. Definition of a base-frequency dynamic phasor

A base-frequency dynamic phasor (BFDP) is a mathematical artifact that represents the entire harmonic spectrum of a time-domain signal as a single DP defined at a single frequency that is often selected to be the fundamental frequency of the network. Consider a time-domain signal, x(t), over the time window $( t - T , t )$ . The Fourier series expansion and the Fourier coefficients of this signal over this interval are as follows [2].

$$
x ( t - T + s ) = \sum _ { k = - \infty } ^ { + \infty } \langle x \rangle _ { k } ( t ) \mathrm { e } ^ { \mathrm { j } k \omega _ { s } ( t - T + s ) }\tag{1}
$$

$$
\langle x \rangle _ { k } ( t ) = \frac { 1 } { T } \int _ { 0 } ^ { T } x ( t - T + s ) \mathrm { e } ^ { - \mathrm { j } k \omega _ { s } ( t - T + s ) } \mathrm { d } s\tag{2}
$$

where $\omega _ { \mathrm { s } } = 2 \pi / T , s \in ( 0 , T ]$ , and k is the harmonic order. The window length T may be arbitrarily selected, although in the analysis of ac-dc systems it is often set to the fundamental period. The series given in (1) can be readily written as:

$$
x ( t - T + s ) = \mathrm { R e } \big ( \langle \mathrm { X } \rangle _ { \mathrm { B } } ( t ) \mathrm { e } ^ { \mathrm { i } \omega _ { \mathrm { s } } ( t - T + s ) } \big )\tag{3}
$$

where

$$
\langle \mathbf { X } \rangle _ { \mathrm { B } } ( t ) = \langle x \rangle _ { 0 } ( t ) \mathrm { e } ^ { - \mathrm { j } \omega _ { \mathrm { s } } ( t - T + s ) }
$$

$$
+ 2 \sum _ { k = 1 } ^ { + \infty } \left. x \right. _ { k } ( t ) \mathbf { e } ^ { \mathbf { j } ( k - 1 ) \omega _ { s } ( t - T + s ) }\tag{4}
$$

![](images/2bea6663ff33d7ea25dbbf9fd7ba569b25417488aa44cec1a265bad61dd3d445.jpg)  
Fig. 2. Discretized BFDP equivalent of basic circuit elements.

is termed as the BFDP of x(t). Note that (3) shows the complete signal as the real part of a complex quantity at the frequency of ωs; and therefore, the network needs to be modeled only at $\omega _ { \mathrm { s } }$ rather than individually for each harmonic. Network simulation based upon BFDPs requires development of discretized companion models for basic circuit components in the form of Norton equivalents as given in Fig. 2 [15]. Table 1 shows models for basic elements.

## 2.2.2. Changeover between EMT and BFDP solutions

In the element models given in Table 1, ωs is referred to as the shift frequency and is used as a simulation parameter, along with the timestep, Δt. With such element models, the network’s nodal admittance matrix depends on both $\omega _ { \mathrm { s } }$ and Δt:

$$
\mathbf { Y } = f ( \Delta t , \omega _ { \mathrm { s } } )\tag{5}
$$

The $\omega _ { \mathrm { s } }$ is normally equal to the fundamental frequency, $\omega _ { 0 } ,$ , and the resulting models are suited for DP solution; however, if $\omega _ { \mathrm { s } }$ is set to zero, $\mathrm { i . e . , }$ no frequency shifting, the element models in Table 1 reduce to typical EMT companion models. Therefore, the task of altering between DP and EMT solutions in the BFAST solver is simply achieved by setting the value of the shift frequency. The decision on setting shift-frequency and time-step size is made based on the state of the network being simulated. If the system is experiencing a transient, $\omega _ { \mathrm { s } }$ is set to zero to obtain the EMT solution for the network; this also calls for a small Δt to be used. Before and after transient events, the solver operates with a DP solution by setting $\omega _ { \mathrm { s } } = \omega _ { 0 } .$ . Since DPs provide a low-pass representation of time-domain signals, a large Δt can be employed. Additional details about the changeover algorithm between the two solution methods in BFAST solver are available in [13].

The BFAST solver’s ability to acquire both the EMT and DP solutions allows it to operate in three simulation modes:

a. EMT mode: the solver operates with the EMT solution with a small time-step for the entire simulation;

b. DP mode: the solver operates with the BFDP solution with a large time-step for the entire simulation; and

c. BFAST mode: the solver switches between EMT and DP solutions by changing the shift-frequency and simulation time-step according to the state of the network.

## 2.2.3. Representation of power system components

Considering numerical robustness, ability to use large time-steps, and ease of interfacing with the electric network, synchronous machine in the BFAST solver is represented as a voltage-source behind an impedance with a constant-parameter stator interface [16]. Transformers are included using the basic transformer model [17], for which the discretized equivalent circuit is developed in BFAST domain. The transmission lines are modeled as lumped-parameter π-sections to preserve its ability to use large simulation time-steps and retain benefits such as ease of modeling with BFAST and zero wave propagation time interpolations.

## 3. Multiple interfacing and solver interactions

Network partitioning and solver interface topologies have implications on several aspects of co-simulations including accuracy, speed, and stability. Also of importance are whether or not they could be implemented at arbitrary places within a network and the capability to facilitate multi-rate simulations. For example, an internal interface can only be used when the user has access to the internal algorithms of the solvers, which may not be readily possible for most commercial-grade simulators. External interfaces eliminate such difficulties and allow to implement and solve subsystems independently. In the following subsections, various interfacing methods that are used in the multi-solver framework in Fig. 1 are explained.

Table 1  
Discretized BFDP equivalents of RLC elements.
<table><tr><td>Element</td><td>Discretized BFDP equivalents</td></tr><tr><td>Resistor</td><td> $\begin{array} { r } { y = \frac { 1 } { R } I _ { \mathrm { h } } ( t ) = 0 } \end{array}$  (No history current source)</td></tr><tr><td>Inductor</td><td> $\begin{array} { r } { y = \frac { A t } { 2 L ( 1 + \mathrm { j } \omega _ { \mathrm { s } } \varDelta t / 2 ) } } \end{array}$ </td></tr><tr><td>Capacitor</td><td> $\begin{array} { r } { I _ { \mathrm { h } } ( t ) \ = ( \frac { 1 - \mathrm { j } \omega _ { \mathrm { s } } \varDelta t / 2 } { 1 + \mathrm { j } \omega _ { \mathrm { s } } \varDelta t / 2 } ) \langle \mathrm { I } \rangle _ { \mathrm { B } } ( t - \varDelta t ) - y \langle \mathrm { V } \rangle _ { \mathrm { B } } ( t - \varDelta t ) } \end{array}$   $\begin{array} { r } { y = \frac { 2 C } { \Delta t } ( 1 + \frac { \mathrm { j } \omega _ { s } \Delta t } { 2 } ) } \end{array}$   $I _ { \mathrm { h } } ( t ) = - \langle \mathrm { I } \rangle _ { \mathrm { B } } ( t$  -△t)-  $\cdot \mathbf { y } ^ { * } \langle \mathbf { V } \rangle _ { \mathrm { B } } ( t - \Delta t )$ </td></tr></table>

## 3.1. EMT-EMT multi-rate interaction

PSCAD/EMTDC allows to simulate different subsystems of a network simultaneously as dependent projects and with multiple time-steps. Interaction between these subsystems are established via the electrical network interface (ENI) [18] wherein boundaries of each subsystem are defined using transmission lines. Fig. 3 shows how the proposed multisolver framework employs ENI to segment EMT subsystems.

## 3.2. EMT-BFAST interface and interaction

The interface between PSCAD/EMTDC and BFAST subsystems is formed using a lossless Bergeron transmission line model [17] as interfacing to an industrial software whose internal algorithm is not attainable calls for an external interface. It uses the propagation time of waves through the transmission line to compensate for the time delay caused by the partitioning and interaction between solvers and hence, does not insert any time delay to the solution [9,13]. Fig. 4 shows the Bergeron model of a lossless transmission line between nodes K and M, wherein $Z _ { \mathrm { C } }$ is the surge impedance of the line.

Assume that the simulation time-step of the EMT subsystem is ΔtEMT; the BFAST subsystem has time-steps of $\varDelta t _ { \mathrm { D P l } }$ and $\varDelta t _ { \mathrm { T } }$ for its DP and EMT solutions, respectively. Time-steps ΔtDP1 and ΔtT are chosen to be integer multiples of $\begin{array} { r } { \varDelta t _ { \mathrm { E M T } _ { : } } } \end{array}$ , and interpolation is enabled at the BFAST-side interface to balance the data granularity. The boundary values calculated by each solver are transformed to respective domains and injected to the opposite side of the interface bus after a delay equal to the wave propagation time, $\tau ,$ of the transmission line as depicted in Fig. 5. The current injection to the EMT-side of the interface, i.e. node M, is calculated as follows.

$$
h _ { \mathrm { M } } ( t ) = \frac { 2 \nu _ { \mathrm { K } } ( t - \tau ) } { Z _ { \mathrm { C } } } - h _ { \mathrm { K } } ( t - \tau )\tag{6}
$$

![](images/c9b750bfa56fc8a76af235587086bf7851e78610c94b3bcdcdcafb2cd51c9501.jpg)  
Fig. 3. EMT-EMT multi-rate interaction in PSCAD/EMTDC via ENI.

![](images/b78bf1a236057f40a034cd0924e62072058692d79b036454d1da3f5b75dc5720.jpg)  
Fig. 4. Explicit coupling of BFAST and PSCAD/EMTDC solvers using a transmission line interface.

![](images/4f6c7d9074365aa1518cf4b50b35d6a91195310430ff4bd1a807f42a6d415650.jpg)  
Fig. 5. EMT-BFAST interaction.

When the BFAST solver is operating with the EMT solution and once it switches to the DP solution, the interface current source at node K is updated using (7) and (8), respectively.

$$
h _ { \mathrm { K } } ( t ) = \frac { 2 \nu _ { \mathrm { M } } ( t - \tau ) } { Z _ { \mathrm { C } } } - h _ { \mathrm { M } } ( t - \tau )\tag{7}
$$

$$
\begin{array} { l } { \langle \mathbf { h } _ { \mathrm { K } } \rangle _ { \mathrm { B } } ( t ) = \left( \frac { 2 \left. \mathbf { v } _ { \mathrm { M } } \right. _ { \mathrm { B } } \left( t - \tau \right) } { Z _ { \mathrm { C } } } - \right. } \\ { \left. \left( \frac { 2 \left. \mathbf { v } _ { \mathrm { K } } \right. _ { \mathrm { B } } \left( t - 2 \tau \right) } { Z _ { \mathrm { C } } } - \left. \mathbf { h } _ { \mathrm { K } } \right. _ { \mathrm { B } } \left( t - 2 \tau \right) \right) \mathrm { e } ^ { - \mathrm { j } \omega _ { \mathrm { s } } \tau } \right) \mathrm { e } ^ { - \mathrm { j } \omega _ { \mathrm { s } } \tau } } \end{array}\tag{8}
$$

The delay compensation and the explicit implementation of the Bergeron model allow two solvers to operate in parallel.

## 3.3. EMT-DP interface and interaction

The simulation of the DP subsystem is attained by enforcing the DP mode (see Section 2.2.2) of the BFAST solver. Therefore, the EMT and DP interface is also formed using the same transmission lines model given in Fig. 4, and the same interaction procedure. However, in this mode the DP solver operates entirely with $\omega _ { \mathrm { s } } = \omega _ { 0 } ,$ , and with a fixed simulation time-step, ΔtDP2.

## 3.4. DP-TS interface and interaction

The transmission line interface restricts the maximum simulation time-step that can be used in either side of the line to its wave propagation time. This greatly hinders the practicality of the TS solver using a large simulation time-step in the milliseconds range. Furthermore, both the DP and TS subsystems are implemented external to PSCAD/EMTDC, which implies that internal algorithms and the admittance matrices of both subsystems are readily accessible. Therefore, in the proposed multisolver framework, the DP-TS interface is established using the Multi-Area Th´evenin Equivalent (MATE) method [19], whose mathematical foundation is described next.

Assume that DP and TS subsystems consist of N and M number of nodes, respectively, and that they are connected by u number of branches as shown in Fig. 6. The network equations of the entire system can be written using modified nodal analysis in the following form:

![](images/c00aa017da1773d7b4fd78ceb3e8834ab8057ef9d52a38ea3a254ecfe3b2ea20.jpg)  
Fig. 6. Coupling of DP and TS solvers using MATE.

$$
\left[ \begin{array} { c c c } { \mathbf { Y } _ { \mathrm { A } } } & { \mathbf { 0 } } & { \mathbf { P } } \\ { \mathbf { 0 } } & { \mathbf { Y } _ { \mathrm { B } } } & { \mathbf { Q } } \\ { \mathbf { P } ^ { \mathrm { T } } } & { \mathbf { Q } ^ { \mathrm { T } } } & { - \mathbf { Z } } \end{array} \right] \left[ \frac { \mathbf { V } _ { \mathrm { A } } } { \mathbf { V } _ { \mathrm { B } } } \right] = \left[ \frac { \mathbf { h } _ { \mathrm { A } } } { \mathbf { h } _ { \mathrm { B } } } \right]\tag{9}
$$

where Z and $\underline { { \mathbf { I } } } _ { \alpha }$ are the link impedance matrix (u × u) and the link current vector $( u \times 1 )$ . Matrices P and Q are the connectivity arrays of the link currents to each subsystem, with $N \times u$ and M× u dimensions, respectively. They are constructed based on the direction of current flow in the linking branches. If the current flow of a particular branch is out of the node, then it is assigned a ＋1 and if flow is into the node, then it is assigned a − 1. If there is no connectivity to a node, it is assigned a value of 0. Rearranging (9) yields:

$$
\begin{array} { r } { \left[ \widehat { \mathbf { I 0 A 0 I B 0 0 Z } } _ { \alpha } \right] \left[ \begin{array} { l } { \underline { { \mathbf { v } } } _ { \mathrm { A } } } \\ { \underline { { \mathbf { v } } } _ { \mathrm { B } } } \\ { \underline { { \mathbf { i } } } _ { \alpha } } \end{array} \right] = \left[ \begin{array} { l } { \underline { { \mathbf { e } } } _ { \mathrm { A } } } \\ { \underline { { \mathbf { e } } } _ { \mathrm { B } } } \\ { \underline { { \mathbf { e } } } _ { \alpha } } \end{array} \right] } \end{array}\tag{10}
$$

where $\mathbf { A } = \mathbf { Y } _ { \mathrm { A } } ^ { - 1 } \mathbf { P } ; \mathbf { B } = \mathbf { Y } _ { \mathrm { B } } ^ { - 1 } \mathbf { Q } ; { \underline { { \mathbf { e } } } } _ { \mathrm { A } } = \mathbf { Y } _ { \mathrm { A } } ^ { - 1 } { \underline { { \mathbf { h } } } } _ { \mathrm { A } } ; { \underline { { \mathbf { e } } } } _ { \mathrm { B } } = \mathbf { Y } _ { \mathrm { B } } ^ { - 1 } { \underline { { \mathbf { h } } } } _ { \mathrm { B } } ; \mathbf { Z } _ { \alpha } = \mathbf { Z } _ { \mathrm { t h \_ A } } + $ ${ \bf Z } _ { \mathrm { t h \_ B } } + { \bf Z } ; \underline { { \mathbf { e } } } _ { \alpha } = \underline { { \mathbf { e } } } _ { \mathrm { t h \_ A } } + \underline { { \mathbf { e } } } _ { \mathrm { t h \_ B } } ,$ and ̂I is the identity matrix. Matrices $\mathbf { Z } _ { \mathrm { t h \_ A } }$ and $\mathbf { Z } _ { \mathrm { t h } , \mathrm { ~ B ~ } }$ represent the Th´evenin impedances and $\underline { { \mathbf { e } } } _ { \mathrm { t h \_ A } }$ and $\underline { { \mathbf { e } } } _ { \mathrm { t h } , \mathrm { ~ B ~ } }$ represent the Th´evenin voltage vectors of corresponding subsystems. They are calculated as $\mathbf { Z } _ { \mathrm { t h \_ A \ } } = \mathbf { P } ^ { \mathrm { T } } \mathbf { A } ; \mathbf { Z } _ { \mathrm { t h \_ B \ } } = \mathbf { Q } ^ { \mathrm { T } } \mathbf { B } ; \mathbf { e } _ { \mathrm { t h \_ A \ } } = \mathbf { P } ^ { \mathrm { T } } \mathbf { e } _ { \mathrm { A } } ; \mathbf { e } _ { \mathrm { t h \_ B \ } } = \mathbf { Q } ^ { \mathrm { T } } \mathbf { e } _ { \mathrm { B } } .$ . The admittance matrices and the Th´evenin impedances of subsystems, and the link impedance matrix are calculated and stored prior to the simulation to minimize run-time computations. The need to re-compute those matrices arises only if the configuration of a subsystem changes.

Consider the case shown in Fig. 7, for which the simulation timesteps of the TS and DP solvers are $\varDelta t _ { \mathrm { T S } } ,$ and $\varDelta t _ { \mathrm { D P 2 } }$ , respectively, and the solutions at $t = t _ { k - 1 }$ corresponding to both subsystems are obtained. Then the following algorithm takes place within the interval $[ t _ { k - 1 } , t ] .$

(I) Partial solutions, i.e. without linking branches, of TS subsystem at $t = t _ { k }$ and the DP subsystem at t = ti are obtained simultaneously by solving them independently.

(II) The TS subsystem’s partial solution is linearly interpolated to $t =$ $t _ { \mathrm { i } } .$ The interpolated positive-sequence solution is transformed to a three-phase one for interfacing with the three-phase DP subsystem as $\left[ \underline { { \mathbf { V } } } , \underline { { \mathbf { V } } } \mathrm { e } ^ { - \mathrm { j } 2 \pi / 3 } , \underline { { \mathbf { V } } } \mathrm { e } ^ { \mathrm { j } 2 \pi / 3 } \right] ^ { \mathrm { T } }$

(III) Using the DP subsystem’s partial solution at $t = t _ { \mathrm { i } }$ and the interpolated TS subsystem’s partial solution (three-phase), the Th´evenin equivalent voltages are computed for each subsystem. Then the interface branch current vector is computed as follows.

$$
\underline { { \mathbf { I } } } _ { \alpha } ( i ) = \mathbf { Z } _ { \alpha } ^ { - 1 } \underline { { \mathbf { e } } } _ { \alpha } ( i )\tag{11}
$$

![](images/a50fa322c17fcb081e9d58d62532713308a6e11639482a319c12d62290749340.jpg)  
Fig. 7. DP-TS interaction.

The complete solution for DP subsystem at $t = t _ { \mathrm { i } }$ is obtained by injecting $I _ { \alpha } ( t _ { \mathrm { i } } )$ to the interface nodes and solving it independently. The same process is repeated at all other intermediate instances of the DP subsystem.

(IV) At $t = t _ { k }$ , the interface branch current vector is calculated in the same manner. It is then injected to both the DP and TS subsystems, and complete solutions of both are computed simultaneously.

This algorithm neither inserts a time-step delay to the solution nor imposes restriction on the maximum simulation time-step; therefore, an appropriately large time-step can be used to solve the subsystems involved. Additionally, It provides benefits such as a reduced-size admittance matrices and parallel solution as subsystems are fully decoupled.

## 3.5. EMT-TS interface and interaction

The interface between the PSCAD/EMTDC (the employed EMT solver) and a TS solver is a well-established one at an industrial level [8]. In a situation where an EMT subsystem should be directly connected to a TS subsystem in the proposed multi-domain co-simulator, such an interface may be readily used.

## 4. Simulations and validation

The accuracy and the efficiency of the proposed method are verified by simulating a modified version of the IEEE 118-bus system as illustrated in Fig. 8 and comparing against standalone EMT simulations performed in PSCAD/EMTDC.

## 4.1. Subsystem divisions of the test system

The generator at bus 62 is replaced with an MMC-HVDC system as shown in Fig. 9; it is controlled to maintain the same active power and bus voltage levels. Areas in the IEEE 118-bus system are segmented based on various criteria such as presence of high frequency and nonlinear devices and their locations, location of the disturbance, intended area of study, electrical distance form the disturbance location and from high-frequency devices, and requirements for dynamic details. The MMC and the network buses in its vicinity are included in the EMT subsystem 1 as it is constantly subjected to switching events that require a small time-step. The MMC parameters are listed in Table 2. The area around this subsystem is included in the EMT subsystem 2 and it is chosen as the study area of interest of the simulation. The rest of the network is segmented as follows: the regions that may be highly affected by the study area disturbances are included in the BFAST subsystem; moderately affected areas are included in the DP subsystem, and undisturbed areas are included in the TS subsystem. Table 3 shows the breaking of subsystems and respective simulation time-step(s). The benchmark PSCAD/EMTDC case is simulated with a 10-μs time-step.

![](images/7ceb07edae9d505e6f3f978c8d65ac82780e919697227ca54021e83d03a21942.jpg)  
Fig. 8. 118-bus test system.

![](images/5a60c0bf0d67679a77c8059dfac13f1e3d9d3405bf9f7fc321b861e5c3e58e02.jpg)  
Fig. 9. EMT subsystem 1 of the 118-bus test system.

The DP and BFAST subsystems are developed independently as two external simulation projects using Microsoft Visual Studio and are programmed in C++ and interfaced to PSCAD/EMTDC using the transmission line models. Run-time communication between these projects and the PSCAD/EMTDC is established via the built-in cosimulation component. The TS subsystem is also separately programmed in C++ using Microsoft Visual Studio and linked to the DP project using the MATE method. The transmission lines used to form interfaces between subsystems are listed in Table 4.

## 4.2. Simulations results

A solid line-to-ground unbalanced fault is applied at bus 47 at t = 5 s for 0.2 s. According to EMT subsystem 1 waveforms shown in Fig. 10, the MMC’s output contains a slight amount of harmonics. However, the fault appears to have no major effect on the MMC operation. Nevertheless, this subsystems has to be simulated with a small time-step considering the harmonics and number of switching events taking place in the MMC. The MMC’s internal and external waveforms and control variables simulated by the multi-domain solver show identical behavior to the benchmark simulation results.

Fig. 11 shows that the waveforms obtained from EMT subsystem 2 using the multi-solver co-simulator and PSCAD/EMTDC are essentially identical. Despite this EMT subsystem being directly connected to the DP and the BFAST subsystems via transmission line interfaces, the interfaces retain such accuracy that solving the network in different domains and using different time-steps has no perceptible implications for the simulation accuracy.

The interface line 69–77 current and the corresponding boundary bus voltages simulated by the BFAST solver are compared in Fig. 12. The solver changes its solution method from DP to EMT right before the transient begins, and changes back to DP solution at the end of the transient, which is automatically detected by the BFAST solver. As such, details of the transient caused by the fault are accurately retained in the BFAST waveforms. A small oscillation is visible in the line current waveform just after it is changed to the DP solution due to a presence of a small dc offset in the waveform. The ability to change the solution method and the time-step of the BFAST solver provides more flexibility for network partitioning locations and interfacing as it ensures accurate interactions between solvers, particularly during transients when cosimulators are mostly vulnerable to fail.

Table 2  
MMC parameters.
<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>Ratings</td><td>230 kV,300 MW</td></tr><tr><td>Dc-bus voltage</td><td>400kV</td></tr><tr><td>Number of sub-modules per arm</td><td>20</td></tr><tr><td>Sub-module capacitance</td><td>5mF</td></tr><tr><td>Arm inductance,arm resistance</td><td>0.001 H,0.025 Ω</td></tr></table>

Table 3

Subsystem allocation of 118-bus test system.
<table><tr><td>Subsystem</td><td>Bus composition</td><td>Simulation time-Step</td></tr><tr><td>EMT1</td><td>59-67</td><td>△tEMT1 =10 μs</td></tr><tr><td>EMT 2</td><td>24,33-58,68-75,116</td><td>△tEMT2 = 50 μs</td></tr><tr><td>BFAST</td><td>76-112, 118</td><td>△tT =50 μs,△tDP1 = 200 μs</td></tr><tr><td>DP</td><td>13-23,25-32,113-115</td><td>△tDP2 = 250 μs</td></tr><tr><td>TS</td><td>1-12, 117</td><td>△ts =5 ms</td></tr></table>

Table 4

Interface branches of partitioned 118-bus network.
<table><tr><td>Solver 1</td><td>Solver 2</td><td>Interface Branches</td></tr><tr><td>EMT1</td><td>EMT 2</td><td>lines 38-65,49-66,54-59,55-59,56-59,65-68</td></tr><tr><td>EMT2</td><td>BFAST</td><td>lines 69-77,75-77,68-81,75-118</td></tr><tr><td>EMT2</td><td>DP</td><td>lines 15-33,19-34,23-24,30-38</td></tr><tr><td>DP</td><td>TS</td><td>lines 8-30, 11-13, 12-14, 12-16</td></tr></table>

![](images/75551987069f6eaf6bc7a11be133b7f65c88b2863f8935b29b9dbdd34ded57eb.jpg)  
Fig. 10. Waveforms from EMT subsystem 1.

![](images/9dfcf6860c1b2a16ada0050134f05cb90f808598611d41b1b9f6702b09a19a91.jpg)  
Fig. 11. Waveforms from EMT subsystem 2.

![](images/588c2993a26f39983b0ecd1de699c4aa2e68be1a39ca8917969659af8abed45a.jpg)  
Fig. 12. Waveforms from the BFAST subsystem.

![](images/113b3f4231c6b6053f62b1c02558b448e24ed6a726a5dc1eb74c88da94784622.jpg)  
Fig. 13. Waveforms from the DP subsystem.

As expected, no fast transients are present in the DP subsystem as seen from Fig. 13, which displays the DP-EMT interface transmission line 19–34 current and the voltage of the corresponding DP-side interface bus. A small level of dynamics is visible in the current waveform during t ∈ (5, 5.2) s due to the fault and the fault clearing events in the EMT subsystem 2. The harmonic-rich BFDPs capture this transient and follow the envelope of the waveform accurately as seen in the enlarged view of the envelope.

Waveforms associated with the TS subsystem are displayed in Fig. 14. Despite the large time-step of 5 ms, the TS solver produces identical results to those of the benchmark simulation since it mostly operates in steady state and feels no noticeable impact from the applied fault. Inclusion of rotating plants may bring electromechanical dynamics to the subsystem; however, they are unlikely to cause any complication to the simulation or the time-step, except for the requirement of intermediate iterations, as those dynamics are much slower than the power system frequency.

![](images/da48782c7de2df8fcb6152c767e11108e363c2af063fe94be3771990c1577006.jpg)  
Fig. 14. Waveforms from the TS subsystem.

## 4.3. Computational gain

Fast acting devices such as MMCs force standalone EMT simulations to use very small time-steps. The proposed multi-solver framework greatly enhances the simulation speed by simulating different network segments with larger time-steps, using efficient modeling techniques, and simultaneous solutions of subsystems. For example, in the 118-bus example, the TS subsystem uses a 5 ms time-step for its phasor solution, which is 500 times larger than that of the standalone EMT solver. This was visible from a simulation time comparison of the 118-bus case, which showed that the benchmark simulation takes 1126 s to run a 10-s simulation, whereas the multi-domain solver takes only 88 s. In addition, a multirate full-EMT simulation was performed for the benchmark 118 bus case using a 10 μs time-step for the EMT1 subsystem and a 50 μs time-step for the rest of the 118-bus network. It was found that this multirate EMT simulation takes approximately 358 s to complete a 10-s simulation. This is a time gain of four times for the proposed method compared to the multirate EMT simulation of the 118 bus system. The multi-solver co-simulator will be particularly advantageous in large networks, where the EMT pockets will represent a much smaller percentage of the whole network.

## 5. Conclusion

A multi-solver framework for co-simulation of power system transients combining the prospects of EMT, TS, DP, and BFAST solvers was implemented and validated. In this framework, a given network is partitioned into several subsystems taking the expected dynamic behaviors into account; they are then assigned to distinct solvers and solved simultaneously using multi-rate techniques. It was noted that a multisolver environment requires multiple interfacing topologies and interaction algorithms as well as special guidelines to determine which locations are most suited for segmentation given the network topology and study purposes. Implementation of the algorithm centralized around an industrial EMT simulator (PSCAD/EMTDC) enabled EMT-EMT multirate simulation, access to a large number of component and control models, and parallel processing, which substantially increase the applicability of the co-simulator. The illustrative simulations performed using the proposed multi-solver co-simulator demonstrated a great deal of accuracy and efficiency; hence, the legitimacy of its methods and the guideline developed for mixed EMT-BFAST-DP-TS algorithm were confirmed. It is expected that, compared with existing simulators, the proposed framework will be able to simulate complex and large networks with high levels of accuracy and computational gain.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

No data was used for the research described in the article.

## References

[1] M.D. Heffernan, K. Turner, J. Arrillaga, C.P. Arnold, Computation of A.C.-D.C. system disturbances - Part I, II, and III, IEEE Trans. Power Appar. Syst. PAS-100 (1981) 4341–4363.

[2] S.R. Sanders, J.M. Noworolski, X.Z. Liu, G.C. Verghese, Generalized averaging method for power conversion circuits, IEEE Trans. Power Electron. 6 (2) (1991) 251–259.

[3] V. Venkatasubramanian, Tools for dynamic analysis of the general large power system using time-varying phasors, Int. J. Elect. Power Energy Syst. 16 (6) (1994) 365–376.

[4] K. Strunz, R. Shintaku, F. Gao, Frequency-adaptive network modeling for integrative simulation of natural and envelope waveforms in power systems and circuits, IEEE Trans. Circuits Syst. I Regul. Pap. 53 (12) (2006) 2788–2803.

[5] Y. Li, D. Shu, F. Shi, Z. Yan, Y. Zhu, N. Tai, A multi-rate co-simulation of combined phasor-domain and time-domain models for large-scale wind farms, IEEE Trans. Energy Convers. 35 (1) (2020) 324–335.

[6] P. Le-Huy, G. Sybille, P. Giroux, L. Loud, J. Huang, I. Kamwa, Real-time electromagnetic transient and transient stability co-simulation based on hybrid line modelling, IET Gen. Trans. Dist. 11 (12) (2017) 2983–2990.

[7] F. Plumier, P. Aristidou, C. Geuzaine, T.V. Cutsem, Co-simulation of electromagnetic transients and phasor models: A relaxation approach, IEEE Trans. Power Del. 31 (5) (2016) 2360–2369.

[8] G.D. Irwin, C. Amarasinghe, N. Kroeker, D. Woodford, Parallel processing and hybrid simulation for HVDCNSC PSCAD studies, in: 10th IET Int. Conf. on AC and DC Power Trans, ACDC 2012, 2012.

[9] K. Mudunkotuwa, S. Filizadeh, U. Annakkage, Development of a hybrid simulator by interfacing dynamic phasors with electromagnetic transient simulation, IET Gen. Trans. Dist. 11 (12) (2017) 2991–3001.

[10] D. Shu, X. Xie, Z. Yan, V. Dinavahi, K. Strunz, A multi-domain co-simulation method for comprehensive shifted-frequency phasor DC-grid models and EMT ACgrid models, IEEE Trans. Power Electron. 34 (11) (2019) 10557–10574.

[11] D. Shu, Z. Ouyang, Z. Yan, Multi-rate and mixed solver based co-simulation of combined transient stability, shifted-frequency phasor and electro-magnetic

models: A practical LCC HVDC simulation study, IEEE Trans. Ind. Electron. (2020) 1

[12] K.M.H.K. Konara, Interfacing a Transient Stability Model to a Real-Time Electromagnetic Transient Simulation Using Dynamic Phasors (Ph.D. thesis), University of Manitoba, Winnipeg, Canada, 2020.

[13] J. Rupasinghe, S. Filizadeh, A. Gole, K. Strunz, Multi-rate co-simulation of power system transients using dynamic phasor and EMT solvers, J. Eng. (2020) 1–9.

[14] S. Filizadeh, Interfacing methods for electromagnetic transient simulation: New possibilities for analysis and design, in: Transient Analysis of Power Systems, John Wiley & Sons, Ltd, 2015, pp. 552–567.

[15] T. Noda, T. Kikuma, T. Nagashima, R. Yonezawa, A Dynamic-Phasor Simulation Method with Sparse Tableau Formulation for Distribution System Analysis: A Preliminary Result, in: 2018 Power Systems Computation Conference, PSCC, Dublin, Ireland, 2018, pp. 1–7.

[16] M. Chapariha, F. Therrien, J. Jatskevich, H.W. Dommel, Explicit formulations for constant-parameter voltage-behind-reactance interfacing of synchronous machine models, IEEE Trans. Energy Convers. 28 (4) (2013) 1053–1063.

[17] N. Watson, J. Arrillaga, Power Systems Electromagnetic Transients Simulation, first ed., IET Digital Library, London, UK, 2003.

[18] Manitoba HVDC Research Center, Winnipeg, MB, Canada, PSCAD/EMTDC User’s Guide.

[19] M.A. Tomim, J.R. Martí, J.A.P. Filho, Parallel transient stability simulation based on multi-area Th´evenin equivalents, IEEE Trans. Smart Grid 8 (3) (2017) 1366–1377.