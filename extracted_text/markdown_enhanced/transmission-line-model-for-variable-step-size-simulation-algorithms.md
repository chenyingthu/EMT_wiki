## Transmission line model for variable step size simulation algorithms
**S. Henschel\*, A.I. Ibrahim, H.W. Dommel**  
*Department of Electrical and Computer Engineering, The University of British Columbia, 2356 Main Mall, Vancouver, B.C., Canada V6T 1Z4*  
Accepted 13 August 1998

**Abstract**  
In this paper, we describe a novel modeling approach for transmission lines that overcomes the maximum step size constraint of regular line models used in electromagnetic transients programs. The new model allows us to accurately simulate wave propagation phenomena as well as low network frequency variations with maximum efficiency, as the simulation step size is no longer restricted to model requirements, but can be adjusted according to the current transient state of the network. The model was tested with a CIGRE line energization case study which was performed utilizing a variable simulation step size algorithm for a combined study of electromagnetic transients and transient stability. © 1998 Elsevier Science Ltd. All rights reserved.  
**Keywords:** Transmission line modeling; Electromagnetic transients; Transient stability

## 1. Introduction
Electromagnetic transients programs (EMTP) and stability programs are extensively used for a wide range of power system studies within their respective time frames. In some cases, however, particularly in system restoration studies, the time frames of both electromagnetic and electromechanical transients, as well as the steady-state behavior, must be investigated. Frequent switching between different types of simulation programs and their respective models then becomes inevitable. To make this process user friendly, a simulation program is currently being developed at the University of British Columbia that aims at a symbiosis of both electromagnetic and electromechanical transients simulations.

While switching between electromagnetic transients models and their equivalents for stability analysis is theoretically possible, it is not always practical, as both model types may have a different internal topology. Whenever models are exchanged during a simulation, this difference in topology may cause rapid transients which, in turn, can create unrealistic behavior of the simulated network (e.g. tripping a protective device). A consistent model for all time frames is therefore preferable.

Cable and transmission line models play a special role in this regard. Transmission line models for electromagnetic transients simulations as well as for transient stability analysis have been well developed and refined over the past few decades [1–3]. Yet, a symbiosis of both types of line models is not as straightforward as with other models: The quasi-steady state, nominal $\pi$-circuit used in stability studies is not sufficiently accurate to represent wave propagation in electromagnetic transients studies. Contrarily, line models preferred in electromagnetic transients programs, such as frequency-dependent or constant parameter line models, require a simulation step size of less or equal to the lowest wave travel time. With this constraint, EMTP line models are not well suited for stability analysis.

In this paper, a new modeling approach is presented to overcome the step size constraint for EMTP transmission line models. The constant parameter line model will be used in order to keep the derivations as simple as possible. We believe, however, that the method can be applied to the more accurate frequency-dependent line models as well. The new transmission line model was tested with a line energization case study, conducted by CIGRE in 1971 [4]. The simulation was carried out using the variable step size algorithm that is presently being developed at the University of British Columbia, and compared to a reference solution obtained with this university’s EMTP version, MICROTRAN, using very small time steps.

\* Corresponding author. Tel.: +1-604-669-0594; Fax: +1-604-822-5949; e-mail: sebastih@ece.ubc.ca.

## 2. Lossless line model
Before considering transmission losses, let us first discuss the ideal case of lossless transmission lines. Albeit not very accurate, this case is particularly interesting since the line equations for a distributed line inductance and capacitance can be solved analytically. The French mathematician Jean Le Rond d’Alembert (1717–1783) first described lossless line equations where the history vector is known and can be calculated from previous current and voltage values as follows:

$$
\begin{bmatrix} \bar{h}_k(t) \\ \bar{h}_m(t) \end{bmatrix} = - \begin{bmatrix} G_c & 0 \\ 0 & G_c \end{bmatrix} \begin{bmatrix} v_k(t-\tau) \\ v_m(t-\tau) \end{bmatrix} - \begin{bmatrix} i_k(t-\tau) \\ i_m(t-\tau) \end{bmatrix} \tag{2}
$$

Eq. (2) shows that the conditions at one end depend on what happened at the other end at one travel time $\tau$ earlier. As long as the simulation time step is less than $\tau$, those conditions at the far end at time $t - \tau$ will appear at the near end at instant $t$. This leads to the galvanic separation which is exploited in the EMTP, as shown in Fig. 1. To maintain the galvanic separation, it is necessary that

$$
\Delta t \le \tau_{\min} \quad \text{and} \quad \tau_{\min} = \min[\tau_i] \quad \text{for} \quad i = 1, \dots, n \tag{3}
$$

where $n$ is the number of modes, i.e.