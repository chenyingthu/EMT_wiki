# A Comparative Study of Electromagnetic Transient Simulations using Companion Circuits, and Descriptor State-space Equations
Ajinkya Sinkar, Huanfeng Zhao, Bolin Qu, Aniruddha M. Gole
Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB R3T 2N2 Canada

**Keywords:** Companion Circuits (CC), Descriptor State-space Equations (DSE), EMT Simulations, Eigenvalues

**Abstract:** This paper investigates an alternative method for EMT simulation of power networks, which uses Descriptor State-space Equations (DSE) to represent the dynamical equations of the circuit. An automated procedure to formulate the DSEs directly from the circuit’s netlist is presented. Once formulated, the DSEs can be discretized using the trapezoidal integration method, and subsequently used for EMT simulations. This approach is compared with the widely used Companion Circuit (CC) approach. Advantages and disadvantages of each approach are discussed. Finally, a procedure for interfacing a DSE-based formulation with a CC-based EMT simulator is also presented. This procedure enables interfacing of arbitrary power networks with a commercial CC-based EMT simulation package and can also be used to speed up the simulation using parallel processing.

*This work was supported by the IRC program of NSERC, Canada. Paper submitted to the International Conference on Power Systems Transients (IPST2021) in Belo Horizonte, Brazil June 6-10, 2021.*
*E-mail addresses: ajinkyasinkar@gmail.com (A. Sinkar), huanfengzhao@gmail.com (H. Zhao), qub@myumanitoba.ca (B. Qu), gole@umanitoba.ca (A.M. Gole).*

## 1. Introduction
ELECTROMAGNETIC TRANSIENT (EMT) simulations are widely used for analyzing the transient behavior of power networks. There are many commercial EMT simulation packages available today [1–3]. At its most basic level, every EMT simulator solves the dynamical equations of a circuit using a suitable numerical integration method. Most commercial EMT programs use the fixed time-step trapezoidal integration method [1–3]. It is well-known that mainly there are two approaches to formulate the equations of a given circuit for EMT simulations [4].

The first is the Companion Circuits (CC) approach proposed by Dommel [5]. In this approach, the differential equations of each branch inductor and capacitor are discretized using trapezoidal integration method to get their corresponding companion circuit representation. Subsequently, Modified Nodal Analysis (MNA) [6] is used for formulating the equations of the discretized circuit which are then solved at every time-step.

Alternatively, the second approach is to formulate the state-space equations of the circuit in the form given in (1).

$$\dot{x}_S = A_s x_S + B_s u \tag{1}$$

Here, $x_S$ is a vector of state variables (typically consists of linearly independent inductor currents/flux-linkages and capacitor voltages/charges [4]), $u$ is the input vector, and $A_s$ and $B_s$ is the state and input matrix respectively. Once (1) has been formulated, we can use any numerical integration algorithm (e.g. trapezoidal method) to compute the updated values of the states $x_S$ knowing inputs $u$ at every time-step.

Traditionally, graph theory-based methods have been used for formulating the state-space equations of a circuit for EMT simulations [4, 7]. But these methods have many intermediate matrix manipulation steps which makes them inefficient (w.r.t time and memory) and thus impractical for EMT simulations of large networks [8, 9].

In this paper, we investigate an alternative method to formulate the state-space equations of a circuit. It uses Descriptor State-space Equations (DSE) which are formulated using MNA. Unlike classical state variables which are always linearly independent, descriptor state variables can be linearly dependent. This avoids special considerations for all inductor-current source cutsets or all capacitor-voltage source loops which is required in many strict state variable formulations.

Once the DSEs are formulated, they can be discretized using an implicit integration method such as the trapezoidal rule and used for EMT simulations. Moreover, the paper shows that a discretized DSE-based formulation can also be easily interfaced with a CC-based EMT simulator without any time-step delay errors. The mathematical equivalence of discretized DSE-based EMT simulation with CC-based EMT simulation has been already proven in [10].

The main advantages of DSE-based formulation are: 1) it can be done automatically without any large matrix manipulations, and 2) gives matrices which are sparse thus making it suitable for large systems. Also, the set of DSEs describing the network immediately allow for the application of widely available linear system analysis tools such as the calculation of system eigenvalues of the real-world network. Although not impossible with CC-based approaches, obtaining such eigenvalues requires additional post-processing [11] because the state-space equations in continuous time-domain are never explicitly formulated.

This paper begins with a review of the CC-based approach for EMT simulations. Next, a procedure for autom
time-step $\Delta t$ used for simulation.
After this, the difference equations of the circuit are directly formulated using Modified Nodal Analysis (MNA) in the form given in (2) and solved at every time-step.

$$G V(t) = J(t) \tag{2}$$

where,
$G$: Augmented admittance matrix.
$[\quad]^T$