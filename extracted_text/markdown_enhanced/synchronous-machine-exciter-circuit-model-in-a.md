# Synchronous Machine Exciter Circuit Model In A Simultaneous Field Winding Interface

U. Karaagac, H. Gras, J. Mahseredjian  
*Ecole Polytechnique, Montreal, Canada*  
A. El-Akoum, X. Legrand  
*Electricite de France, Paris, France*

**Abstract**—This paper presents the implementation of a phase domain (PD) synchronous machine (SM) model through modified-augmented-nodal-analysis (MANA) formulation for the computation of electromagnetic transients. This formulation provides a direct and simultaneous electrical connection to the SM field winding, and enables accurate modeling of its exciter as an electrical side. Detailed exciter modeling can be used to study exciters transient performance and potential failure conditions in its circuit components. This paper also presents and tests a simple current source interface for existing dq0-type SM machine models with control signal input for field control. Realistic test cases are used to validate and compare the proposed models.

**Index Terms**—synchronous machine, excitation system, EMTP.

## I. INTRODUCTION

Simulation of electromagnetic transients in modern power systems is widely used for the determination of component ratings such as insulation levels and energy absorption capabilities, in the design and optimization process, for testing control and protection systems and for analyzing power system performance in general [1], [2]. In order to simulate electromagnetic transients, various simulation tools have been developed such as [3]-[5]. These simulation tools are called electromagnetic transients type (EMT-type) programs and solve nodal analysis (NA) or modified-augmented-nodal-analysis (MANA) formulation based power system network equations (PSNE). EMTP-RV is the only one using the MANA [6] formulation.

Traditionally in EMT-type programs, excitation systems are modeled using control block diagrams. Therefore, the synchronous machine (SM) admittance matrix inserted into the PSNE does not include the field winding terminals. In many cases it is important to model the SM exciter as an actual electrical circuit for detailed analysis of its performance and for identifying hazardous conditions for exciters circuit components. The connection of an actual exciter circuit to the SM model can be achieved by providing access to its field terminals in the internal circuit model.

One alternative is to use the compensation method based universal machine (UM) model [7] as it provides direct electrical connection to the field winding. However, the compensation method has important topological limitations [1]. Although in theory and when topological ill-conditioning does not occur, the compensation method can be used to obtain simultaneous solutions for all interconnected nonlinear devices, its implementation is complex and most programs [4] rely on the presence of distributed-parameter transmission lines to decouple cases with several machines. Artificial one time-step delay lines are used in certain cases, such as parallel units, at the expense of reduced accuracy.

This paper uses the MANA formulation [6] with a phase-domain synchronous machine (PDSM) model [9] in order to provide an accurate and simultaneous solution method for connecting exciter electrical circuits to SM field winding terminals. In addition, this paper proposes an alternative (not simultaneous) exciter circuit connection approach based on a current source interface, for existing SM models, such as classical dq0 models.

A realistic test system containing two parallel hydraulic units with static type exciters is used to compare proposed modeling approaches. EMTP-RV [6] is used for all simulations and the proposed PDSM model with field winding electrical connection is implemented through the user-defined (dynamic link library) option available in EMTP-RV [6].

The first part of the paper presents the SM models with field winding electrical connection. The second part presents simulation results.

## II. SYNCHRONOUS MACHINE MODEL WITH FIELD WINDING ELECTRICAL CONNECTION

This model version is identified hereinafter as SM1. In this approach the SM model with field winding electrical connection (see Figure 1) is obtained by using the PDSM model and its representation in MANA formulation. The discretized PDSM model equations are given in [10]-[11] using the trapezoidal integration rule. The numerical oscillations of this rule, due to detectable discontinuities, are eliminated using the Backward Euler method.

In this model, damper winding effects are represented with three damper windings: one on d-axis, and two on q-axis. The d-axis is assumed to be leading the q-axis by $90^\circ$ and generator convention is used while expressing the voltage equations [12]. Throughout this paper, bold uppercase denotes the matrices, bold lowercase denotes the vectors and the operator $p$ is $d/dt$.

```
       iF                           ia
                                  SM             ib
      external +                                    external
                        with field winding
      electrical v
                   F   electrical connection        electrical
      network                                  ic   network
                 -
```
**Figure 1.** Synchronous machine with field winding electrical connection

### C. Power System Network Equation Formulation and Solution Algorithm

The nodal analysis based formulation of network equations requires the admittance model of the SM. This can be achieved by applying matrix reduction to (5) for expressing the voltages and currents of the stator windings and the field winding in terms of the voltages and currents of damper windings. A better and more flexible approach is to use MANA [6][8]. In such a formulation the admittance model requirements are eliminated and equation (5) can be included directly into the PSNE. In the following MANA equations, the last row and column of the coefficient matrix are used for including (5)

$$
\begin{bmatrix}
\mathbf{Y}_n & \mathbf{V}_{adj} & \mathbf{D}_{bdepc} & \mathbf{S}_{adj} & \mathbf{S}_{M_{adj}} \\
\mathbf{V}_{adj}^T & 0 & 0 & 0 & 0
\end{bmatrix}
\begin{bmatrix}
\mathbf{v}_n \\
\mathbf{i}_{adj}
\end{bmatrix}
=
\begin{bmatrix}
\mathbf{i}_n \\
\mathbf{v}_{adj}
\end{bmatrix}
$$