## Compensation method for parallel real-time EMT studies

**Authors:** B. Bruned a, *, S. Dennetière a, J. Michel a, M. Schudel a, J. Mahseredjian b, N. Bracikowski c  
**Affiliations:**  
a RTE, Campus Transfo, Jonage, France  
b Polytechnique Montréal, Canada  
c Université de Nantes, France  

**Keywords:** Electromagnetic Transients (EMT), Parallel simulation, Compensation Method, Real-time simulation, Hardware-In-The-Loop

**Abstract:** The classical solution for computing electromagnetic transients (EMTs) in parallel relies on the propagation delay of transmission lines. The lines are used as decoupling elements to split the network into different tasks. When there is no natural delay or the delay is too short for the selected simulation time-step, other techniques have to be considered. This paper presents one of them. The compensation method is used in this paper for network decoupling for parallelization. A detailed implementation of this method is presented for real-time simulation. Performances are assessed in both offline and real-time environments with distribution and High Voltage Direct Current (HVDC) network test cases. Switching cases are also studied with HVDC power electronics devices. A Hardware-In-The-Loop (HIL) setup for an HVDC link in operation is also considered to validate the proposed method in a real-time environment.

*Paper submitted to the International Conference on Power Systems Transients (IPST2021) in Belo Horizonte, Brazil June 7–10, 2021.*  
*Corresponding author. E-mail address: boris.bruned@rte-france.com (B. Bruned).*  
*https://doi.org/10.1016/j.epsr.2021.107341*  
*Received 9 November 2020; Received in revised form 8 March 2021; Accepted 29 April 2021*  
*Available online 21 May 2021*

## 1. Introduction

The high penetration of renewable energies has increased the use of power electronics in the transmission network. Transmission Network Operators (TSOs) have to study increasingly complex interaction phenomena between power electronics devices [1]. Also for Distribution Network Operators (DNOs), the development of large active networks can impact the stability of the whole grid [2]. To study the transients of both cases, good accuracy can be achieved by lowering numerical integration time-steps [3,4,5]. Parallelization is a key method to accelerate EMT simulation to improve accuracy. It is based on the multi-core properties of modern computers.

One of the main methods to parallelize an EMT simulation relies on the propagation delay of the transmission line model. When the propagation delay is greater than the time-step, decoupling is possible. This natural latency (line-delay) allows to send computed network values to the next time-step. This method has been implemented for offline and real-time environments. In real-time [6], a topology analysis identifies the transmission lines available for decoupling. Then, it splits the network on each part of the lines and creates tasks. Transmission line-delays are also used in [7], where matrix permutation to block triangular form is applied to establish and solve the decoupled matrices.

When the network model does not contain lines (or cables) with propagation delays, other parallel solution techniques have to be considered. This is the case for large distribution networks [2] or grids with power electronics devices [1].

Attempts to decouple networks when line-delay is not available are typically based on the reformulation of the network matrix into the Bordered Bloc Diagonal (BBD) form. Domain Decomposition techniques [8-10] can be used to run the matrix solution in parallel. The main difficulty is that the BBD form may not be optimal for improving computational performance. Also, as explained in [7], existing applications assume linear networks and significant computational performance degradation is expected for nonlinearities and switching topologies due to needed matrix reformulations.

In this paper the compensation method [11,12] (CM) is used to manually decouple networks at required locations when line-delay decoupling is not available. The CM was initially used for electromagnetic transients when solving nonlinear models [13]. Its extensions and relation with hybrid-analysis are discussed in [14]. It can be in fact used for solving separately any number of components in linear and nonlinear mode. The theoretical links between CM, diakoptics and other more recent network tearing approaches are presented in [15]. In fact the original CM is more generic and includes other methods.

To the authors’ best knowledge, the CM performances/advantages have not been previously studied for practical problems with switching and real-time simulation.

The paper is organized as follows. The compensation method implementation for EMT offline/real-time environment is presented in Section 2. Validation and performance assessments are presented in Section 3 for a large distribution network and an industrial HIL application case that includes HVDC converters.

## 2. Compensation method

### 2.1. Overview

The CM uses two main fundamental principles: the Norton/Thévenin equivalents and the superposition theorem. It is equivalent to cutting connecting components, such as wires in a network to create detached subnetworks. It is also possible to cut through branches (linear or nonlinear). The basic principle is illustrated in Fig. 1 using two subnetworks (N1 and N2), but it is also applicable to an arbitrary number of subnetworks, assuming that they become independent due to cutting.

Fig. 2. Ideal current sources to replace the compensation branch.

In Step 3, it is now possible to compute the branch currents $i_C$ using:
$$Z_C i_C = v_{th2} - v_{th1} \quad (4)$$
where $Z_C = Z_{th1} + Z_{th2} + Z_B$. $Z_B$ is the connecting component impedance matrix and it is zero when the connecting components are wires.

In Step 4, the set of currents $i_C$ is used to apply compensation as