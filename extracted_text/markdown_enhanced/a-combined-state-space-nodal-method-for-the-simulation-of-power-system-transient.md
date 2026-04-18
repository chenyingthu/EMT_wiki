# A Combined State-Space Nodal Method for the Simulation of Power System Transients
Christian Dufour, Member, IEEE, Jean Mahseredjian, Senior Member, IEEE, and Jean Bélanger, Member, IEEE

**Abstract**—This paper presents a new solution method that combines state-space and nodal analysis for the simulation of electrical systems. The presented flexible clustering of state-space-described electrical subsystems into a nodal method offers several advantages for the efficient solution of switched networks, nonlinear functions, and for interfacing with nodal model equations. This paper extends the concept of discrete companion branch equivalent of the nodal approach to state-space described systems and enables natural coupling between them. The presented solution method is simultaneous and enables benefitting from the advantages of two different modeling approaches normally exclusive from one another.

**Index Terms**—Electromagnetic transients, nodal analysis, real time, state space.

*Manuscript received March 05, 2010; revised July 03, 2010 and September 13, 2010; accepted October 25, 2010. Date of publication December 13, 2010; date of current version March 25, 2011. Paper no. TPWRD-00152-2010.*

C. Dufour and J. Bélanger are with Opal-RT Technologies, Montréal, QC H3K 1G6, Canada.
J. Mahseredjian is with the École Polytechnique de Montréal, Montréal, QC H3T 1J4, Canada (e-mail: jeanm@polymtl.ca).
Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.
Digital Object Identifier 10.1109/TPWRD.2010.2090364

## I. INTRODUCTION
The computation of electromagnetic transients can be based on various numerical methods for the formulation and solution of network equations. The most widely used methods fall into two categories: 1) the state-space and 2) nodal-analysis formulations. State-space equations are used, for example, in [1] for inserting electrical circuit equations into the Simulink [2] solver. Nodal equations are widely used in Electromagnetic Transients (EMT)-type applications, such as [3] and [4]. The modified-augmented-nodal analysis method is used in [5] and [6] for eliminating topological restrictions from the nodal-analysis approach.

The nodal equations are assembled after discretizing all circuit devices with a numerical integration rule, such as trapezoidal integration. These equations are particularly powerful and efficient for simulating very large networks through sparse matrix methods. Some real-time simulator technologies are also based on the nodal formulation [7], [8].

In the case of state-space equations, the numerical integration technique can be selected after formulation, which simplifies the programming of variable time-step integration techniques. In addition, state-space representation can be particularly powerful for controller design methods [1]. The main disadvantage is the computing time required for the automatic synthesis of state-space matrices. Other complications can arise for the simultaneous solution of nonlinear models, for the simulation of large networks, and for large numbers of states in some model equations.

Some variations of the nodal approach are based on the concept of group separation for increasing efficiency and flexibility. In [9], the use of groups provides a technique for diminishing the number of nodal points and, consequently, the size of the system matrix for real-time computations [10]. In [11], the compensation method allows separating circuits and solving them independently. The compensation method is noniterative when the solved circuits are linear. A similar idea is used in [12] for reducing the number of nodal connection points. In [13], state-space equations are also used for this purpose.

The inclusion of state-space equations into nodal equations has been applied in [14] (see also [15]) for the purpose of model circuit synthesis from fitted measurements.

This paper presents a general methodology for the simultaneous interfacing of nodal equations with state-space equations for arbitrary network topologies. This interfacing allows eliminating several modeling limitations in state-space-based solvers. This interfacing allows creating state-space groups that can be maintained independently for efficient computation of switching events. In addition, each state-space group uses its own automatic formulation of state-space matrices which obviously reduces the formulation time when compared to unique state-space equations of the complete system without grouping.

The discrete state-space solvers are inefficient for handling switching events, especially in real-time applications, where precalculation methods must be used. The massive precalculation of state-space matrix sets for all switch combinations becomes problematic in terms of the required memory for large numbers of coupled switches [16].

The method proposed in this paper contributes to the improvement of state-space-based power system simulation solvers. It notably offers important advantages for real-time applications.

This paper starts with a theoretical presentation and follows with demonstration cases. The reference state-space and nodal analysis solvers used in this paper are those presented in [1] and [17], respectively.

## II. STATE-SPACE NODAL METHOD
The state-space nodal (SSN) method described in this section uses arbitrary size clusters (groups) of electrical elements and combines them into a single nodal admittance matrix. The cluster equations are discretized state-space equations. The trapezoidal integration rule is used in the discretization process. The clusters include implicitly unknown node voltages at their nodal connection points. These voltages are at common