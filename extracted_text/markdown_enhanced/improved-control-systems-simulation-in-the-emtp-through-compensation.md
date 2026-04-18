## IMPROVED CONTROL SYSTEMS SIMULATION IN THE EMTP THROUGH COMPENSATION

**S. Lefebvre (Member) and J. Mahseredjian (Member)**
Hydro-Quebec, IREQ
Direction Technologie de reseaux
Varennes, Quebec, Canada

**ABSTRACT:** The control systems, devices and phenomena modelled in TACS, and the electric network modeled in EMTP are solved separately with one-time-step error at the interface. This provides an efficient time-step solution, but there can be numerical stability and accuracy problems associated with the one-time-step error. This paper shows a technique which can eliminate the time delay, without having to use a simultaneous EMTP and TACS solution.

**Keywords:** EMTP compensation, power electronics

## 1. INTRODUCTION

TACS is a section of the EMTP which allows the representation of control systems in block-diagram form. It has been used to model the control of converters, FACTS and static VAR devices, excitation systems of synchronous generators, dynamic load characteristics, etc. [1-2]

It is well known that there is a one step time delay between TACS and EMTP variables. There are many cases where such delay do not cause any trouble: fast transients in the network - slow transients in the control system. However, many examples can be created where the time delay results either in numerical instability or wrong results. An example of numerical instability is the simulation of the arc behavior in a circuit breaker (resistance simulation through a current injection), while wrong results will be obtained in some power electronic circuits due to the delay of the trigger orders from TACS.

The information used by EMTP to advance to time $t$ is based on the TACS solution $T_{out}$ for time $t - \Delta t$, where $\Delta t$ is the step size. Based on the network solution $E_{in}$ at time $t$, TACS computes its outputs. This is shown in Figure 1.

The concept of separate EMTP and TACS simulation is the result of preserving solution efficiency, and as much as possible modularity. The TACS solution is simultaneous for linear blocks, and sequential for nonlinear blocks or functions. The TACS equations are sparse but unsymmetrical. There are no iterations during the solution.

TACS outputs to the EMTP may be in fact one or more time steps late because there are internal time delays in the TACS solution. The internal TACS time delays can often be minimized or compensated with proper control modelling. They may affect the accuracy or stability of the TACS solution, but have less impact on the EMTP-TACS interface stability. The one-time-step error at this interface can have a strong impact on the network solution. Selecting a smaller step size may sometimes be sufficient, but no simple general rule can be given to manage time delay errors though. There are even cases where irrespective of the step size, the solution is numerically unstable. This paper then does not concentrate on the internal time delays in TACS, but rather on the EMTP-TACS interface one-time-step error.

The purpose of this paper is to demonstrate the application of the compensation method to eliminate the one-time-step error, without having to have a simultaneous EMTP-TACS solution. This is an extension of the compensation technique used in EMTP for the solution of true nonlinear elements. [3]

## 2. BASIC ALGORITHMS

### EMTP solution

The EMTP is a nodal analysis program based on the fixed time-step trapezoidal integration method. Considering only linear elements, discretized network equations are given by $Y_n V_n = I_n - J_n$, where $Y_n$ is the symmetrical nodal admittance matrix, $V_n$ is the node to ground voltage vector while $I_n$ and $J_n$ represent respectively node current injections including current sources and 'past history' terms. For convenience in notation, assume that the impact of known voltage sources is merged with the history terms. The symmetric admittance matrix is triangularized, and the time step solution is obtained, without iteration, with forward-backward substitution. When the computation of the voltages is completed, then all history terms are updated for usage at the next time step.

Before the triangularization, it is important to order the equations in a way that will minimize the fill-ins.

There are relatively few nonlinear elements in the network and because the TACS matrices are unsymmetrical, a time-step delay exists between EMTP and TACS, (Figure 1) such that independent solutions can be carried out. The pseudo-nonlinear non iterative TACS solution has been traditionally preferred over a TACS simultaneous nonlinear formulation.

The TACS matrices are unsymmetrical, triangularization yields two distinct upper and lower matrices. Because there are typically several nonlinearities in a control system, the TACS solution is not as simple as triangularization separate of the time-step loop, and a forward-backward substitution in the time-step loop. As in the EMTP, it is necessary to distinguish linear components (explicitly declared transfer functions) from the nonlinearities. Nonlinearities in TACS