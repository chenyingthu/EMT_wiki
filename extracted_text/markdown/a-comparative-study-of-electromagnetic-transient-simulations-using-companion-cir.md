# A Comparative Study of Electromagnetic Transient Simulations using Companion Circuits, and Descriptor State-space Equations

![](images/42638da0b5819306790925f596da5b3b4a8f39bbed843607a475ea8b561437a1.jpg)

Ajinkya Sinkar , Huanfeng Zhao , Bolin Qu , Aniruddha M. Gole

Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB R3T 2N2 Canada

## A R T I C L E I N F O

Keywords:   
Companion Circuits (CC)   
Descriptor State-space Equations (DSE)   
EMT Simulations   
Eigenvalues

## A B S T R A C T

This paper investigates an alternative method for EMT simulation of power networks, which uses Descriptor State-space Equations (DSE) to represent the dynamical equations of the circuit. An automated procedure to formulate the DSEs directly from the circuit’s netlist is presented. Once formulated, the DSEs can be discretized using the trapezoidal integration method, and subsequently used for EMT simulations. This approach is compared with the widely used Companion Circuit (CC) approach. Advantages and disadvantages of each approach are discussed. Finally, a procedure for interfacing a DSE-based formulation with a CC-based EMT simulator is also presented. This procedure enables interfacing of arbitrary power networks with a commercial CC-based EMT simulation package and can also be used to speed up the simulation using parallel processing.

## 1. Introduction

ELECTROMAGNETIC TRANSIENT (EMT) simulations are widely used for analyzing the transient behavior of power networks. There are many commercial EMT simulation packages available today [1–3]. At its most basic level, every EMT simulator solves the dynamical equations of a circuit using a suitable numerical integration method. Most commercial EMT programs use the fixed time-step trapezoidal integration method [1–3]. It is well-known that mainly there are two approaches to formulate the equations of a given circuit for EMT simulations [4].

The first is the Companion Circuits (CC) approach proposed by Dommel [5]. In this approach, the differential equations of each branch inductor and capacitor are discretized using trapezoidal integration method to get their corresponding companion circuit representation. Subsequently, Modified Nodal Analysis (MNA) [6] is used for formulating the equations of the discretized circuit which are then solved at every time-step.

Alternatively, the second approach is to formulate the state-space equations of the circuit in the form given in (1).

$$
\underline { { \dot { x } } } _ { S } = A _ { s } \underline { { x } } _ { S } + B _ { s } \underline { { u } }\tag{1}
$$

Here, $\underline { { x } } _ { s }$ is a vector of state variables (typically consists of linearly independent inductor currents/flux-linkages and capacitor voltages/ charges [4]), u is the input vector, and $A _ { s }$ and $\pmb { B } _ { s }$ is the state and input matrix respectively. Once (1) has been formulated, we can use any numerical integration algorithm (e.g. trapezoidal method) to compute the updated values of the states $\underline { { x } } _ { s }$ knowing inputs u at every time-step.

Traditionally, graph theory-based methods have been used for formulating the state-space equations of a circuit for EMT simulations [4, 7]. But these methods have many intermediate matrix manipulation steps which makes them inefficient (w.r.t time and memory) and thus impractical for EMT simulations of large networks [8, 9].

In this paper, we investigate an alternative method to formulate the state-space equations of a circuit. It uses Descriptor State-space Equations (DSE) which are formulated using MNA. Unlike classical state variables which are always linearly independent, descriptor state variables can be linearly dependent. This avoids special considerations for all inductor-current source cutsets or all capacitor-voltage source loops which is required in many strict state variable formulations.

Once the DSEs are formulated, they can be discretized using an implicit integration method such as the trapezoidal rule and used for EMT simulations. Moreover, the paper shows that a discretized DSE-based formulation can also be easily interfaced with a CC-based EMT simulator without any time-step delay errors. The mathematical equivalence of discretized DSE-based EMT simulation with CC-based EMT simulation has been already proven in [10].

The main advantages of DSE-based formulation are: 1) it can be done automatically without any large matrix manipulations, and 2)

gives matrices which are sparse thus making it suitable for large systems. Also, the set of DSEs describing the network immediately allow for the application of widely available linear system analysis tools such as the calculation of system eigenvalues of the real-world network. Although not impossible with CC-based approaches, obtaining such eigenvalues requires additional post-processing [11] because the state-space equations in continuous time-domain are never explicitly formulated.

This paper begins with a review of the CC-based approach for EMT simulations. Next, a procedure for automatically formulating the equations for the DSE-based approach is introduced. Using various test cases, the advantages and disadvantages of the CC-based and DSE-based approaches are discussed. A procedure for combining the two approaches in a single simulation is often desirable, particularly when a user wants to interface a custom designed model to a commercial EMT simulator. Hence, an example of this is also presented.

In brief, the paper investigates an alternative method for EMT simulations using Descriptor State-space Equations (DSE) which are readily derivable from the circuit’s netlist, and makes the following key contributions:

1 It compares the accuracy and speed of the DSE-based approach with the traditional CC-based approach.

2 It develops an algorithm for interfacing a DSE-based formulation with a CC-based simulator. This can be used to interface arbitrary power networks with commercial EMT simulators and is also easily parallelizable.

3 It validates this algorithm by simulating a benchmark system viz. IEEE 39 bus with HVdc converters.

4 It demonstrates that computation time savings do accrue from the parallelization offered by the proposed interfacing algorithm.

This paper only considers lumped circuit elements viz. resistors (R), inductors (L) and capacitors (C) along with independent current sources (JS) and voltage sources $\left( V _ { S } \right)$ while formulating the equations. But this approach can be easily extended to include other elements or components.

## 2. Formulation of Equations For EMT Simulations

## 2.1. Companion Circuit (CC)-based EMT Simulation

This section briefly reviews the widely used CC-based EMT simulation [5], so that it can later be contrasted with DSE-based EMT simulation. In a CC-based EMT simulation, each branch inductor and capacitor are transformed to their corresponding companion circuits in discrete time-domain using trapezoidal integration method. The companion circuits are as shown in Fig. 1. They consist of a history current source (which is a function of the element’s current and voltage in the previous time-step) in parallel with a conductance which depends on the

![](images/efa4cef717465686172b7235ffee64670fd5a96c7fad0554105c1c55844b5187.jpg)  
Fig. 1. Companion Circuits for Inductor and Capacitor

time-step Δt used for simulation.

After this, the difference equations of the circuit are directly formulated using Modified Nodal Analysis (MNA) in the form given in (2) and solved at every time-step.

$$
G \underline { { V } } ( t ) = \underline { { J } } ( t )\tag{2}
$$

where,

G: Augmented admittance matrix.

$$
\underline { { V } } ( t ) = \left[ \begin{array} { l l } { \underline { { \nu } } _ { N } ^ { T } ( t ) } & { \underline { { i } } _ { S } ^ { T } ( t ) } \end{array} \right] ^ { T }
$$

$\underline { { \nu _ { N } } } ( t ) \mathrm { : }$ Node voltages at time t.

$i _ { S } ( t ) \colon$ Currents through independent voltage sources at time t.

$$
\underline { { J } } ( t ) = \left[ \begin{array} { l l } { i _ { H S } ^ { T } ( t ) } & { \underline { { \nu } } _ { S } ^ { T } ( t ) } \end{array} \right] ^ { T }
$$

$\underline { { i } } _ { H S } ( t ) :$ Vector containing history current sources for inductors & capacitors, and independent current sources at time t.

vS(t): Independent voltage sources at time t.

Any CC-based EMT simulator uses the following general procedure:

1 Form the G matrix using the circuit’s netlist.

2 Initialize V(t).

3 Advance the solution time $t = t + \Delta t .$

4 Update J(t) by computing the history current values for each inductor and capacitor, and the values of independent voltage and current sources.

5 If switches are present, check if any switch has changed its state and modify the G matrix accordingly.

6 Compute V(t) by solving (2).

7 Update the currents iL(t) and $i _ { C } ( t )$ for each inductor and capacitor using the history current values from Step 4 and V(t) from Step 5.

8 Go back to Step 3 if end time not reached.

The case of other non-linearities such as inductor or transformer saturation can also be accommodated by modelling them with parallel inductors with switches [12, 13]. As we can see, the CC-based EMT simulation approach is highly scalable which is why it is used in the majority of commercial EMT simulation packages today [1–3].

## 2.2. Descriptor State-space Equation (DSE)-based EMT Simulation

In this section, we discuss the DSE-based EMT simulation approach. In this approach, the equations of the circuit are formulated using MNA in the continuous time-domain in the form given in (3)1 .

$$
\pmb { { \cal E } } \underline { { { \dot { x } } } } = - \pmb { { \cal A } } \underline { { { x } } } + \pmb { { { \cal B } } } \underline { { { u } } }\tag{3}
$$

After (3) has been formulated, it is discretized using trapezoidal integration method with a time-step Δt. This gives the update equation as in (4) which can then be used to carry out EMT simulations studies.

$$
\bigg ( E + \frac { A \Delta t } { 2 } \bigg ) \underline { { x } } ( t ) = \bigg ( \bigg ( E - \frac { A \Delta t } { 2 } \bigg ) \underline { { x } } ( t - \Delta t ) + \frac { B \Delta t } { 2 } \bigg ( \underline { { u } } ( t ) + \underline { { u } } ( t - \Delta t ) \bigg ) \bigg )\tag{4}
$$

Equation (3) is called the Descriptor State-space Equation (DSE) where x is the vector of descriptor state variables and u is the input vector, both as given in (5).

$$
\underline { { x } } = \left[ \begin{array} { l l l } { \underline { { \boldsymbol { \nu } } } _ { N } ^ { T } } & { \underline { { i } } _ { L } ^ { T } } & { \underline { { i } } _ { S } ^ { T } } \end{array} \right] ^ { T } \mathrm { ~ a n d ~ } \underline { { \boldsymbol { u } } } = \left[ \begin{array} { l l } { \underline { { \boldsymbol { \nu } } } _ { S } ^ { T } } & { \underline { { j } } _ { S } ^ { T } } \end{array} \right] ^ { T }\tag{5}
$$

where,

vN: Node voltages.

iL: Inductor currents.

$\underline { { i } } _ { S } \mathrm { : }$ Currents through independent voltage sources.

$\underline { { \nu } } _ { s } \mathrm { : }$ Independent voltage sources.

j : Independent current sources.

When (3) is expanded using x and u from (5), we get (6).

$$
\begin{array} { r } { \left[ \begin{array} { l l l } { C } & { { \bf 0 } } & { { \bf 0 } } \\ { { \bf 0 } } & { L } & { { \bf 0 } } \\ { { \bf 0 } } & { { \bf 0 } } & { { \bf 0 } } \end{array} \right] \frac { d } { d t } \left[ \begin{array} { l } { \underline { { \nu } } _ { N } } \\ { \underline { { i } } _ { L } } \\ { \underline { { i } } _ { S } } \end{array} \right] = - \left[ \begin{array} { l l l } { { \bf G } } & { A _ { L } } & { A _ { \nu s } } \\ { - A _ { L } ^ { T } } & { { \bf 0 } } & { { \bf 0 } } \\ { - A _ { s } ^ { T } } & { { \bf 0 } } & { { \bf 0 } } \end{array} \right] \left[ \begin{array} { l } { \underline { { \nu } } _ { N } } \\ { \underline { { i } } _ { L } } \\ { \underline { { i } } _ { S } } \end{array} \right] + \left[ \begin{array} { l l } { { \bf 0 } } & { - A _ { j s } } \\ { { \bf 0 } } & { { \bf 0 } } \\ { - I } & { { \bf 0 } } \end{array} \right] \left[ \begin{array} { l } { \underline { { \nu } } _ { S } } \\ { \underline { { i } } _ { S } } \end{array} \right] } \end{array}\tag{6}
$$

Here,

C: Capacitance matrix

L: Diagonal matrix containing inductance values.

G: Conductance matrix (corresponding to lumped R’s)

$A _ { L } , \ A _ { v s } , \ A _ { j s } \mathrm { : }$ Incidence matrix for inductor, independent voltage source, and current source branches respectively.

In most cases, the matrix E is singular as seen in (6). The exception is the relatively rare case when there are no voltage sources $( \mathrm { i . e . }$ , the last row of E in (6) does not exist) and C is also non-singular. Singularity of E implies that the entries of the descriptor state vector x are linearly dependent. Also, when E is singular, an explicit integration method like Forward Euler cannot be used for numerical integration [14].

A detailed derivation of (6) can be found in [10]. If the sub-equations in (6) are expanded, we get (7) – (9).

$$
\begin{array} { r l } { C \frac { d \underline { { \nu } } _ { N } } { d t } = } & { { } - \pmb { G } \underline { { \nu } } _ { N } - \pmb { A } _ { L } \underline { { i } } _ { L } - \pmb { A } _ { v s } \underline { { i } } _ { S } - \pmb { A } _ { j s } \underline { { j } } _ { S } } \end{array}\tag{7}
$$

$$
L \frac { d \underline { { i } } _ { L } } { d t } = A _ { L \underline { { \nu } } _ { N } } ^ { T }\tag{8}
$$

$$
A _ { v s } ^ { T } \underline { { { \nu } } } _ { N } - \underline { { { \nu } } } _ { S } = 0\tag{9}
$$

Taking a closer look at (7) – (9), we can conclude the following:

1 Equation (7) is obtained by applying Kirchhoff’s Current Law (KCL) at every node.

2 Equation (8) is obtained by applying Kirchhoff’s Voltage Law (KVL) in every inductor branch.

3 Equation (9) is obtained by applying KVL in every independent voltage source branch.

Based on the above discussion, we can say that a DSE-based EMT simulator can use the following general procedure:

1 Form the E, A and B matrices using the circuit’s netlist.

2 Initialize x(t) and u(t).

3 Advance the solution time $t = t + \Delta t$

4 Update u(t) by computing the independent voltage source and current source values at time t.

5 Compute the RHS of (4) from the history values and u(t) from Step 4.

6 If switches are present, check if any switch has changed its state and modify the A matrix accordingly.

7 Compute x(t) by solving (4) using the RHS computed in Step 5.

8 Go back to Step 3 if end time not reached.

From the above discussion, we can see that this approach is also highly scalable (just like the CC-based approach). The key step is the automatic generation of E, A and B (from (3)) for any arbitrary circuit using its netlist. This is summarized in the remainder of this section.

## 2.3. Formulation of E, A and B

In this section, we present a procedure to automatically formulate E, A and B. We know from (6) that each of these are composed of other submatrices $( C , G , L \mathrm { e t c . } )$ . The sizes of the different sub-matrices are given in Table I. Here, $n _ { n }$ is the number of nodes, nl is the number of inductors, $n _ { v s }$ is the number of independent voltage sources, and $n _ { j s }$ is the number of independent current sources in the circuit.

The matrix C includes all the capacitors present in the circuit. The general expression for (i, j) entry of C is given by (10), where $c _ { i }$ is the sum of all the capacitance between node i and ground while $c _ { i j }$ is the capacitance between node i and j. Here both i and j vary from 1 to $n _ { n } .$ .

$$
\pmb { C } ( i , j ) = \left\{ \begin{array} { c l } { c _ { i } + \sum _ { k = 1 } ^ { n _ { n } } c _ { i k } \quad \mathrm { f o r } i = j } \\ { - c _ { i j } \quad \mathrm { f o r } i \neq j } \end{array} \right.\tag{10}
$$

The matrix $\textbf { G }$ includes all the resistors present in the circuit. The general expression for $( i , j )$ entry of G is given by (11), where gi is the sum of all the conductance between node i and ground while $g _ { i j }$ is the conductance between node i and j. Here both i and j vary from 1 to $n _ { n }$ .

$$
\mathbf { { \pmb { G } } } ( i , j ) = \left\{ \begin{array} { c } { { g _ { i } + \sum _ { { k = 1 } } ^ { n _ { n } } g _ { i k } \quad \mathrm { f o r } i = j } } \\ { { - g _ { i j } \quad f o r i \ne j } } \end{array} \right.\tag{11}
$$

The matrix L is a diagonal matrix which includes all the inductors present in the circuit. The general expression for (k, k) entry of L is given by (12) where $l _ { k }$ is the $k ^ { t h }$ inductance in the circuit’s netlist. Here k varies from 1 to $n _ { l } .$ .

$$
\pmb { L } ( k , k ) = l _ { k }\tag{12}
$$

The matrices $A _ { L } , A _ { \nu s }$ and $A _ { j s }$ are incidence matrices corresponding to inductor branches, independent voltage source branches and independent current source branches respectively. Each of these can be formulated using (13).

$$
\begin{array} { r l r } { 1 } & { { } \mathrm { i f ~ b r a n c h \ } k \mathrm { ~ h a s ~ s t a r t ~ n o d e \ } i } & { } \\ { A ( i , k ) = \{ - 1 } & { { } \mathrm { i f ~ b r a n c h \ } k \mathrm { ~ h a s ~ e n d ~ n o d e \ } i } \\ { 0 } & { { } } & { \mathrm { o t h e r w i s e } } \end{array}\tag{13}
$$

## 3. Comparison of the Two Approaches

## 3.1. Comparison of Simulation Results

Firstly, we compare the simulation results from the two approaches. For this, consider a simple power system example as shown in Fig. 2. Transmission lines are modelled by coupled Π-sections and loads as three-phase resistors, inductors, and capacitors. System data is given in Appendix A.

A time-step of 200 $\mu s$ is used for both the approaches. The system initially operates in steady state. $\mathrm { A t } ~ t = 0 . 0 5 ~ s ,$ a 50 ms (three cycles) solid three phase fault occurs at Bus 3. A comparison of the simulation results from the two approaches is shown in Fig. 3.

We can see that the simulation results from both the approaches are essentially exactly identical. The maximum absolute error in both $I _ { S 1 ( A ) }$ and $I _ { S 2 ( A ) }$ is exactly zero. This must be so since these two approaches are mathematically equivalent [10].

## 3.2. Computation of Eigenvalues

In addition to providing a framework for EMT simulation, the DSE

Table I  
Size of sub-matrices in E, A and B
<table><tr><td>Matrix</td><td>Size</td></tr><tr><td>C and G</td><td> $\pmb { n } _ { n } \times \pmb { n } _ { n }$ </td></tr><tr><td>I</td><td> ${ \pmb n } _ { l } \times { \pmb n } _ { l }$ </td></tr><tr><td> $A _ { L }$ </td><td> ${ \pmb n } _ { n } \times { \pmb n } _ { l }$ </td></tr><tr><td> $A _ { \nu s }$ </td><td> ${ \pmb n } _ { n } \times { \pmb n } _ { \nu s }$ </td></tr><tr><td> $A _ { j s }$ </td><td> ${ \pmb n } _ { n } \times { \pmb n } _ { j s }$ </td></tr></table>

![](images/4fc948d08f05317377df2340befb98d5a76891ec52b9ed9108bf07eb5058bb27.jpg)  
Fig. 2. A Simple Power System Example

![](images/01d5b04b2230f28b528c29fee6760ee8049c0549aeec51b8e88f2480457a5651.jpg)

(a) Phase A current of Source 1  
![](images/fdbfe38d315e6d03d519bb8f388b7a715d8e8a93d8237ca0c4d2da18ce7a70ae.jpg)

(b) Absolute Error in Phase A current of Source 1  
![](images/9fef6c5d297ebda7cfec3ecb52ad796d9ad0ca5f0b089bfcc6f9558444334dd6.jpg)

(c)Phase A current of Source 2  
![](images/face9c58cf51c486b62e860f9be916d5c67d526fd57df6cbd08851dcd5048069.jpg)  
(d) Absolute Error in Phase Acurrent of Source 2  
Fig. 3. Simulations Results - Example 1

(a) Phase A current of Source 1

(b) Absolute Error in Phase A current of Source 1

(c) Phase A current of Source 2

(d) Absolute Error in Phase A current of Source 2

formulation has an additional advantage which is lacking in traditional CC-based EMT solvers. It is that it directly permits the application of analytical tools for linear systems (e.g., eigenvalue analysis, root locus etc.). Although classical state-space (SS) formulations can also be used for this, formulating equations in classical SS form may involve many intermediate matrix manipulation steps. This makes them inefficient (w. r.t time and memory) and thus impractical for formulating the equations of large systems [8, 9].

An appropriately simple example as in Fig. 4 is chosen to demonstrate the basic principles. The example includes an all capacitor-voltage source (C-V) loop $\nu _ { S ^ { - } } \nu _ { C 2 } . \nu _ { C 3 } . \nu _ { C 1 }$ which highlights the advantage of DSE-based formulation over classical SS formulation.

![](images/aa609371bd478d824ca276a3121f7eb5fa19ac61d29a0218da058a0594021ad2.jpg)  
Fig. 4. Simple RLC Circuit (Computation of Eigenvalues)

For the DSEs, $\underline { { \boldsymbol { x } } } = [ \nu _ { 1 } \quad \nu _ { 2 } \quad \nu _ { 3 } \quad i _ { L } \quad i _ { S } ] ^ { T } .$ , and then the E and A matrices are as in (14) and (15).

$$
\pmb { { E } } = \left[ \begin{array} { c c c c c c } { 0 . 0 0 0 1 } & { 0 } & { - 0 . 0 0 0 1 } & { 0 } & { 0 } \\ { 0 } & { 0 . 0 0 1 5 } & { - 0 . 0 0 1 } & { 0 } & { 0 } \\ { - 0 . 0 0 0 1 } & { - 0 . 0 0 1 } & { 0 . 0 0 1 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 . 0 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right]\tag{14}
$$

$$
A = { \left[ \begin{array} { l l l l l } { 0 } & { 0 } & { 0 } & { 1 } & { 1 } \\ { 0 } & { 0 } & { 0 } & { - 1 } & { 0 } \\ { 0 } & { 0 } & { 0 . 1 } & { 0 } & { 0 } \\ { - 1 } & { 1 } & { 0 } & { 0 } & { 0 } \\ { - 1 } & { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right] }\tag{15}
$$

Due to the C-V loop $\nu _ { S ^ { - } } \nu _ { C 2 } - \nu _ { C 3 } - \nu _ { C 1 }$ , only two out of the three capacitor voltages can be state variables in a classical SS formulation. Hence, $\underline { { x } } _ { s } =$ $\left[ \nu _ { C 1 } \nu _ { C 2 } i _ { L } \right] ^ { T }$ is taken for formulating the equations in classical SS form (as in (1)). Note, to eliminate the extra algebraic variable $\nu _ { C 3 }$ in this case, intermediate matrix manipulations are needed. After eliminating $\nu _ { C 3 } ,$ we finally get the state matrix As as given in (16).

$$
A _ { s } = \left[ { \begin{array} { c c c } { 0 } & { 1 5 3 . 8 5 } & { 1 6 9 2 . 3 1 } \\ { 0 } & { - 2 3 0 . 7 7 } & { - 1 5 3 8 . 4 6 } \\ { - 1 0 0 } & { 0 } & { 0 } \end{array} } \right]\tag{16}
$$

To corroborate the fact that one can obtain the system eigenvalues from the DSE-based formulation, a comparison of the eigenvalues of $A _ { s }$ with the eigenvalues of the matrix pencil (− A, E) is given in Table II.

Here, $\sigma ( A _ { s } )$ are the system eigenvalues. We can clearly see from Table II that $\sigma ( A _ { s } ) \subseteq \sigma ( - A , E )$ . In fact, the two extra − ∞ eigenvalues arise in the case of $( - A , E )$ because E here is rank-deficient by two [15], which implies that only three elements of the descriptor state vector x (out of five) are linearly independent.

It is worthwhile to note the ease with which C-V loops are handled in a DSE-based formulation. Unlike a classical SS formulation, there is no strict requirement in a DSE-based formulation to eliminate the intermediate algebraic variables. The same can be concluded if all inductor-current source (L-J) cutsets are present in a circuit.

Note that although in the above discussion we have demonstrated the computation of eigenvalues with DSE-based formulation using a relatively simple example, it can be easily accomplished for any arbitrary circuit using the procedure to automatically formulate A and E given earlier in

## Table II

Comparison of Eigenvalues
<table><tr><td>Eigenvalues of As[σ(As)]</td><td>Eigenvalues of(-A,E)[σ(-A,E)]</td></tr><tr><td>-66.139 ± j389.65</td><td>-66.139 ± j389.65</td></tr><tr><td>-98.461</td><td>-98.491</td></tr><tr><td></td><td>-8,8</td></tr></table>

Section 2.3.

## 3.3. Comparison of Simulation Run Time

To investigate how the computer run-times for DSE-based and CCbased simulation approaches scale with increasing system sizes, we consider four different systems. These include standard IEEE test systems (39-bus, and 118-bus) and synthetic versions of the Illinois 200-bus system and the South Carolina 500-bus system. The data for the latter two is available in the public domain [16, 17]. In each case, a 10 s simulation is performed with a time-step of 50 μs. Transmission lines in each of these systems have been modelled by coupled Π-sections and loads as three-phase resistors, inductors, and capacitors.

Fig. 5 plots a comparison of the simulation run times for the CCbased and DSE-based approaches as a function of the number of three phase busses in the system. On an average, the CC-based approach is about 1.3 times faster for the cases considered here. However, note that although the DSE-based simulation approach is slower, it directly yields additional information such as system eigenvalues, which the CC-based approach does not.

To understand why this difference in simulation run times exists, let’s look at the size of the matrices involved in the computations in every time-step for each of the approaches. The G matrix (in (2)) for the CC-based approach is a square matrix of size $( n _ { n } + n _ { \nu s } )$ . On the other hand, the $\left( E + A \Delta t / 2 \right)$ matrix (in (4)) for the DSE-based approach is a square matrix of size $( n _ { n } + n _ { l } + n _ { \nu s } ) .$ . Here, $n _ { n }$ is the number of nodes, $n _ { \nu s }$ is the number of independent voltage sources and $n _ { l }$ is the number of inductors. Hence, we can conclude that the superior speed of the CCbased approach can be attributed to the fact that the size of the matrix involved in its computations at every time-step is smaller than that in a DSE-based approach.

## 4. Interfacing of DSE-based Formulation with CC-based EMT Simulator

We will now present a procedure for interfacing a DSE-based formulation with a CC-based EMT simulator. This procedure is similar to the ones presented in [18, 19] but derived here for a DSE-based formulation.

## 4.1. Interfacing Procedure

Consider the network to be interfaced is represented by a black box as shown in Fig. 6 with n ports for interfacing.

Consider that this network has lumped circuit elements (viz. resistors (R), inductors (L) and capacitors (C)) and independent voltage or current sources internally. Then, internal dynamics of this network can be easily modelled in continuous time-domain using DSEs.

For doing this, let $\underline { { \nu } } _ { p } ,$ iS and ${ \underline { { i } } _ { p } }$ be as given in (17), (18) and (19)

![](images/38aeffa2845a8f346e834b5373b9219e5e4f9dfabdcfd183ca648463b998577f.jpg)  
Fig. 5. Comparison of Simulation Run Times

![](images/4ee26f640a79f5e6b7653920431ffb576907c088af24c54d5ba15d23f747752c.jpg)  
Fig. 6. A General n-Port Network

respectively.

$$
\underline { { \boldsymbol \nu } } _ { p } = \left[ \boldsymbol \nu _ { p 1 } \quad \boldsymbol \nu _ { p 2 } \quad \ldots \quad \boldsymbol \nu _ { p n } \right] ^ { T }\tag{17}
$$

$$
\underline { { i } } _ { S } = [ i _ { S 1 } \quad i _ { S 2 } \quad \ldots \quad i _ { S n } ] ^ { T }\tag{18}
$$

$$
\underline { { i } } _ { p } = [ i _ { p 1 } \quad i _ { p 2 } \quad \ldots \quad i _ { p n } ] ^ { T }\tag{19}
$$

Then, the DSEs for this network in continuous time-domain can be written in the form given in (20).

$$
E \underline { { \dot { x } } } = - A \underline { { x } } + B \underline { { \nu } } _ { p } + B _ { i } \underline { { u } } _ { i }\tag{20}
$$

Here, $\underline { { \boldsymbol { x } } } = \left[ \begin{array} { l l l } { \underline { { \boldsymbol { \nu } } } _ { N } ^ { T } } & { \underline { { \boldsymbol { i } } } _ { L } ^ { T } } & { \underline { { \boldsymbol { i } } } _ { S } ^ { T } } \end{array} \right] ^ { T } ; ~ \underline { { \boldsymbol { \nu } } } _ { N }$ is the vector of internal node voltages, $i _ { L }$ is the vector of internal inductor currents; and u is the vector of internal sources. In addition to this, it can be easily verified that the relationship between $i _ { p }$ and $\underline { x }$ is as given in (21).

$$
\underline { { i } } _ { p } = \mathbf { \delta } \underline { { B } } ^ { T } \underline { { x } }\tag{21}
$$

Now, to interface this n-port network with a CC-based EMT simulator, we need a discrete time-domain relationship between ${ \dot { \underline { i } } } _ { p } ( t )$ and $\underline { { \nu } } _ { p } ( t )$ as given by (22).

$$
\begin{array} { r } { i _ { p } ( t ) = G _ { n } \ \underline { { \nu } } _ { p } ( t ) + \underline { { I } } _ { H I S T } ( t - \Delta t ) } \end{array}\tag{22}
$$

This relationship can be derived from the DSE-based formulation by firstly discretizing (20) using trapezoidal integration method to give (23).

$$
\begin{array} { l } { \displaystyle \underline { { x } } ( t ) = \bigg ( E + \frac { A \Delta t } { 2 } \bigg ) ^ { - 1 } \bigg \{ \bigg ( E - \frac { A \Delta t } { 2 } \bigg ) \underline { { x } } ( t - \Delta t ) + \frac { B \Delta t } { 2 } \bigg ( \underline { { \nu } } _ { p } ( t ) + \underline { { \nu } } _ { p } ( t - \Delta t ) \bigg ) } \\ { \displaystyle \qquad + \frac { B _ { i } \Delta t } { 2 } \bigg ( \underline { { u } } _ { i } ( t ) + \underline { { u } } _ { i } ( t - \Delta t ) \bigg ) \bigg \} } \end{array}\tag{23}
$$

Subsequently, substituting (23) in (21) gives ${ \dot { l } } _ { p } ( t )$ as in (24).

$$
\begin{array} { l } { \displaystyle { \dot { I } _ { p } ( t ) = B ^ { T } \bigg ( E + \frac { A \Delta t } { 2 } \bigg ) ^ { - 1 } \frac { B \Delta t } { 2 } \frac { \nu _ { p } ( t ) } { p } + \left. B ^ { T } \bigg ( E + \frac { A \Delta t } { 2 } \bigg ) ^ { - 1 } \bigg ( E - \frac { A \Delta t } { 2 } \bigg ) x ( t - \Delta t ) \right. } } \\ { \displaystyle { \mathrm { ~ + ~ } \left. B ^ { T } \bigg ( E + \frac { A \Delta t } { 2 } \bigg ) ^ { - 1 } \frac { B \Delta t } { 2 } \frac { \nu _ { p } ( t - \Delta t ) } { 2 } \right. } } \\ { \displaystyle { \left. + B ^ { T } \bigg ( E + \frac { A \Delta t } { 2 } \bigg ) ^ { - 1 } \frac { B _ { i } \Delta t } { 2 } \bigg ( \frac { u _ { i } ( t ) } { 4 } + \frac { u _ { i } ( t - \Delta t ) } { 2 } \bigg ) \right. } } \end{array}\tag{24}
$$

We can see that (24) has the same form as (22) with $G _ { n }$ and $\underline { { I } } _ { H I S T }$ as given in (25) and (26) respectively. Thus, we have the required discrete time-domain relationship between ${ \dot { \underline { i } } } _ { p } ( t )$ and $\underline { { \nu } } _ { p } ( t )$ . Note, since $\underline { { u } } _ { i }$ is a vector of internal sources, it is already known for time t and hence can be part of $\underline { { I } } _ { H I S T }$

$$
\pmb { G } _ { n } = \pmb { B } ^ { T } \left( \pmb { E } + \frac { \pmb { A } \Delta t } { 2 } \right) ^ { - 1 } \frac { \pmb { B } \Delta t } { 2 }\tag{25}
$$

$$
\begin{array} { l } { { \displaystyle { \cal I } _ { H I S T } = B ^ { T } \bigg ( E + \frac { A \Delta t } { 2 } \bigg ) ^ { - 1 } \bigg ( E - \frac { A \Delta t } { 2 } \bigg ) x ( t - \Delta t ) } } \\ { ~ + ~ B ^ { T } \bigg ( E + \frac { A \Delta t } { 2 } \bigg ) ^ { - 1 } \frac { B \Delta t } { 2 } \nu _ { p } ( t - \Delta t ) }  \\ { { ~ + ~ B ^ { T } \bigg ( E + \frac { A \Delta t } { 2 } \bigg ) ^ { - 1 } \frac { B _ { i } \Delta t } { 2 } \bigg ( \underline { { { u } } } _ { i } ( t ) + \underline { { { u } } } _ { i } ( t - \Delta t ) \bigg ) } } \end{array}\tag{26}
$$

Now we can interface this network with any CC-based EMT simulator using the following procedure:

1 Form $E , A$ and B matrices for the network to be interfaced using the procedure given in Section 2.3 and then calculate $G _ { n }$ using (25).

2 Add $G _ { n }$ to the overall G matrix of the CC-based EMT simulator.

3 Initialize x(t).

4 Advance the solution time $t = t + \Delta t .$

5 Knowing x(t − Δt) and ${ \underline { { \boldsymbol { \nu } } } _ { p } } ( t - \Delta t ) _ { : }$ , calculate $\underline { { I } } _ { H I S T }$ using (26). Then, add $\underline { { I } } _ { H I S T }$ to the overall $\underline { { J } } ( t )$ of the CC-based simulator (see (2)).

6 If switches are present inside the interfaced network, check if any switch has changed its state and modify $G _ { n }$ accordingly.

7 Update the $G _ { n }$ added to the overall G matrix of the CC-based EMT simulator.

8 The CC-based simulator computes $\underline { { V } } ( t )$ by solving (2).

9 Read $\underline { { \nu } } _ { p } ( t )$ from the overall $\underline { { V } } ( t )$ of the CC-based EMT simulator (see (2)). Then, calculate $\underline { { x } } ( t )$ using (23).

10 Go back to Step 4 if end time not reached.

Note that there is no time-step delay involved while interfacing the DSE-based formulation, and the interfaced modelling is mathematically exactly equivalent to a full CC-based approach being used directly [10]. If distributed parameter elements (such as cables or transmission lines) are present in the system, then these can be easily included as CC-models and interfaced with the DSE-based formulation using the given procedure.

Significant parts of the above algorithm can be inherently computed in parallel, thus making it suitable for implementation on a parallel computing platform. For example, if a large network is divided into multiple subnetworks {1, 2…N}, then we can see that Steps 5 to 7, and Step 9 for a subnetwork i are completely independent of those for subnetwork j. Therefore, these step sequences in the above procedure can be performed in parallel for each subnetwork. Note that the parallel implementation proposed here does not rely on transportation delays introduced by distributed parameter elements like transmissions lines [20].

Also note that Steps 6 and 7 in the above algorithm allow inclusion of time-varying network components (like switches) in DSE-based formulations. Hence it could be used for modelling complex switching systems such as HVdc converters. However, efficient implementation of such systems will require additional steps such as optimal ordering of switches to ensure efficient matrix refactorizations [21, 22]. At present, this is outside the scope of this paper and is proposed for future work.

However, the ability to interface DSE-based formulation with traditional CC-based EMT (host) platforms is a powerful feature that enables the immediate utilization of the capabilities of the host platform. For example, traditional CC-based EMT platforms have evolved advanced (efficient) models for various types of HVdc converters and controls. This feature could be exploited by including them in the host CC-based EMT simulator and including the remainder of the network in a DSEbased formulation.

## 4.2. Example Case – IEEE 39 bus system with LCC-HVdc

The main objectives of this test case are: (i) to verify the accuracy of the proposed interfacing procedure, (ii) to demonstrate that it can be used to interface arbitrary power networks with a commercial CC-based EMT simulator, and (iii) to run the partitioned system on a parallel computing platform to measure its speedup performance.

The test system is the standard IEEE 39-bus system shown in Fig. 7. The data for this system has been taken from [17]. The standard case has been modified to include an embedded LCC-HVdc link. The parameters and controls for the dc link have been taken from [23].

The interfacing procedure has been implemented as a subroutine in PSCAD/EMTDC (a commercial CC-based EMT simulator) [24]. As a reference, the entire system is also modelled in the CC-based EMT simulator to compare the accuracy of the interfacing procedure.

The system is partitioned into two parts as shown in Fig. 7. All components inside the blue dashed boxes are modelled using the DSEbased approach and then interfaced, while the components in the red dashed boxes are directly modelled in the commercial CC-based EMT simulator [24]. Transmission lines are modelled by coupled Π-sections, and loads as three-phase resistors, inductors, and capacitors.

A time-step of 20 $\mu s$ is used for simulation. The system initially operates in steady state. $\mathrm { A t } t = 0 . 1 s ,$ a three cycle (50 ms) phase-A-toground fault occurs near Bus 16 (internal to Partition #1). Note that this causes a change in the Norton equivalent admittance (i.e. $G _ { n }$ in (25)) of Partition #1.

Fig. 8(a) shows the current in phase $\mathsf { A } ( I _ { T F ( A ) } )$ flowing into the Bus 22 computed using the full CC-based simulation and the proposed DSEbased formulation interfaced with CC-based EMT simulator. As we can see, they match closely. The maximum absolute error is 0.003 kA (as shown in Fig. 8(b)) which corresponds to a relative error of 0.15% (relative to the steady state peak value of $I _ { T F ( A ) } )$ . Fig. 9(a) shows the comparison of the results for the dc link current $( I _ { d c } )$ from both the approaches. This also matches closely. The absolute error in $I _ { d c }$ is shown in Fig. 9(b).

Thus, this example verifies the accuracy of the interfacing procedure presented earlier. It also demonstrates how the DSE-based approach can be used for interfacing arbitrary power networks with a commercial CCbased EMT simulation package.

As discussed in Section 4.1, partitioning the system and using the proposed interfacing approach permits the use of parallel computing techniques for speeding up the simulation. To demonstrate this feature, the two partitions (shown in Fig. 7) were simulated in parallel on a general-purpose Intel i7-8700 based PC with 6 cores running at 3.2 GHz

![](images/65bb4a2016c3454b4e29417b5dffce35687e1263388895426aeb600df5885aa4.jpg)  
Fig. 7. Interfacing Example - IEEE 39 Bus System with LCC-HVdc

![](images/44a9ecf56cf457b7a61878c086c4f1032c9755cfbb9c446903be7f8a5296206a.jpg)

(a)Phase A Current of Transformer 22-35 on Bus 22 Side  
![](images/2fee4310be651b2ecd22462898b95d00e1c5762e1664978fae5e7d950c757888.jpg)  
(b) Absolute Error in Phase A Current of Transformer 22-35

Fig. 8. Phase A Current of Transformer 22-35 on Bus 22 Side (IEEE 39-bus) (a) Phase A Current of Transformer 22-35 on Bus 22 Side (b) Absolute Error in Phase A Current of Transformer 22-35  
![](images/77eb22b65bb329dc0f02bebe9df6446f96b9c7dbfd3f497384d6a08d406c819f.jpg)  
(a) Dc Link Current

![](images/70ef54161a289a3587b7e37500865941f9dad4a806fdf454ec4efe26bddb1f3f.jpg)  
(b) Absolute Error in dc Link Current  
Fig. 9. Dc Link Current (IEEE 39-bus)

(a) Dc Link Current

(b) Absolute Error in dc Link Current

Table III  
Comparison of Total CPU Times (IEEE 39 Bus System)
<table><tr><td>Serial SimulationTs (sec)</td><td>Parallel SimulationTp (sec)</td><td>Speedup(Ts/Tp)</td></tr><tr><td>161.25</td><td>93.15</td><td>1.73</td></tr></table>

and having Windows 10 OS. Table III shows a comparison of the CPU times for the parallel and serial simulation cases (here, serial simulation means the one that is not using parallel computing techniques). The times are for a 10 s simulation with a time-step $\Delta t = 2 0 \ \mu s$

As we can see in Table III, partitioning the system into two roughly equally sized subsystems gave a speedup factor of 173%. Thus, this also verifies the fact that the proposed interfacing procedure can be used to speed up a simulation using parallel processing.

## 5. Conclusions

This paper investigates an alternative method to formulate state variable equations of a circuit for EMT simulations using Descriptor Statespace Equations (DSE). A step-by-step procedure is presented for automatically formulating the DSEs using a circuit’s netlist. The formulation is straightforward compared to that of deriving classical state space equations. Also, intermediate matrix manipulation steps are avoided in the DSE-based formulation thus making it suitable for large systems. Once formulated, the DSEs are discretized using trapezoidal integration method and used to carry out EMT simulations studies.

This approach is compared with the widely used Companion Circuits (CC) approach. One of the advantages of using the DSE-based formulation is that in addition to running EMT simulations, it is possible to analytically calculate the eigenvalues of the network directly. However, it has the disadvantage of having a higher run-time than the CC-based approach for EMT simulation.

Finally, a procedure for interfacing a DSE-based formulation with a CC-based EMT simulator is also presented. There is no time-step delay involved while interfacing. This procedure enables interfacing of arbitrary power networks with a commercial CC-based EMT simulation package without the need for building it in that package. Moreover, this combined approach also allows easy parallel simulation as multiple DSE-based modules can be run on separate processors and then interfaced with a CC-based EMT simulator.

## CRediT authorship contribution statement

Ajinkya Sinkar: Conceptualization, Data curtion, Formal analysis, Investigation, Methodology, Software, Validation, Visualization, Writing – original draft, Writing – review & editing. Huanfeng Zhao: Conceptualization, Methodology, Investigation, Validation, Writing – review & editing. Bolin Qu: Data curtion, Software, Validation. Aniruddha M. Gole: Conceptualization, Funding acquisition, Supervision, Writing – review & editing.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Appendix

Data for Example 1 (Section 3.1)

Transmission Lines:

1000 MVA, 230 kV

$$
R _ { + } = 1 . 0 5 \times 1 0 ^ { - 5 } p u / m ; X _ { + } = 1 . 2 3 \times 1 0 ^ { - 4 } p u / m
$$

$$
B _ { + } = 1 . 6 9 8 7 \times 1 0 ^ { - 5 } { p u } / m
$$

$$
R _ { 0 } = 1 . 0 7 \times 1 0 ^ { - 4 } p u / m ; X _ { 0 } = 3 . 2 1 \times 1 0 ^ { - 4 } p u / m
$$

$$
B _ { 0 } = 1 . 2 0 6 4 \times 1 0 ^ { - 5 } \ : p u / m
$$

Transformers:

1: 1000 MVA, 16.5/230 kV, Xl = 0.181 pu, $I _ { m a g } = 2 \%$

2: 1000 MVA, 230/18 kV, Xl = 0.181 pu, $I _ { m a g } = 2 \%$

Loads:

522 MW, 150 MVAr

## References

[1] D.A. Woodford, A.M. Gole, R.W. Menzies, Digital Simulation of DC Links and AC Machines, IEEE Transactions on Power Apparatus and Systems PAS-102 (6) (1983) 1616–1623. Jun.

[2] R.P. Wierckx, W.J. Giebrecht, R. Kuffel, X. Wang, G.B. Mazur, M.A. Weekes, A. M. Gole, Validation of a Fully Digital Real-Time Electromagnetic Transients Simulator for HVDC System Controls Studies, Proceedings of Joint International Power Conference Athens Power Tech 2 (1993) 751–759.

[3] J. Mahseredjian, S. Denneti\`ere, L. Dub´e, B. Khodabakhchian, L. G´erin-Lajoie, On a new approach for the simulation of transients in power systems, Electric Power System Research 77 (11) (2007) 1514–1520. Sep.

[4] N. Watson, J. Arrillaga, Power Systems Electromagnetic Transients Simulation, IET Power and Energy Series 39, 2003.

[5] H.W. Dommel, Digital Computer Solution of Electromagnetic Transients in Singleand Multiphase Networks, IEEE Transactions on Power Apparatus and Systems PAS-88 (4) (1969) 388–399. Apr.

[6] Chung-Wen Ho, A. Ruehli, P. Brennan, The Modified Nodal Approach to Network Analysis, IEEE Transactions on Circuits and Systems 22 (6) (1975) 504–509. Jun.

[7] S. Seshu, N. Balabanian, Linear Network Analysis, Wiley, 1959.

[8] S. Natarajan, A systematic method for obtaining state equations using MNA, IEE Proceedings G-Circuits, Devices and Systems 138 (3) (1991) 341–346. Jun.

[9] A.R. Sana, J. Mahseredjian, X. Dai-Do, H.W. Dommel, Treatment of discontinuities in time-domain simulation of switched networks, Mathmatics and Computers in Simulations 38 (4–6) (1995) 377–387. Aug.

[10] H. Zhao, S. Fan, and A. Gole, “Equivalency of State Space Models and EMT Companion Circuit Models,” presented at the International Conference on Power System Transients (IPST) 2019, Perpignan, France.

[11] J.A. Hollman, J.R. Marti, Step-by-step eigenvalue analysis with EMTP discrete-time solutions, IEEE Transactions on Power Systems 25 (3) (2010) 1220–1231. Feb.

[12] H.W. Dommel, Electromagnetic Transients Program (EMTP) Theory Book, Bonneville Power Administration, 1986.

[13] H. Zhao, S. Fan, A.M. Gole, Stability of Algorithms for Electro-Magnetic-Transient Simulation of Networks with Switches and Non-linear Inductors, IEEE Transactions on Power Delivery 35 (1) (2020) 377–385. Feb.

[14] Q. Chen, S.-H. Weng, C.-K. Cheng, A Practical Regularization Technique for Modified Nodal Analysis in Large-scale Time-domain Circuit Simulation, IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems 31 (7) (2012) 1031–1040. Jul.

[15] G.H. Golub, C.F. Van Loan, Matrix Computations, Johns Hopkins University Press, Baltimore, 2012.

[16] A.B. Birchfield, T. Xu, K.M. Gegner, K.S. Shetye, T.J. Overbye, Grid Structural Characteristics as Validation Criteria for Synthetic Networks, IEEE Transactions on Power Systems 32 (4) (2017) 3258–3265. Jul.

[17] “Electric Grid Test Cases - Texas A&M University.” [Online]. Available: https://e lectricgrids.engr.tamu.edu/electric-grid-test-cases/.

[18] K. Strunz, E. Carlson, Nested Fast and Simultaneous Solution for Time-domain Simulation of Integrative Power-electric and Electronic Systems, IEEE Transactions on Power Delivery 22 (1) (2007) 277–287. Jan.

[19] C. Dufour, J. Mahseredjian, J. B´elanger, A Combined State-Space Nodal Method for the Simulation of Power System Transients, IEEE Transactions on Power Delivery 26 (2) (2011) 928–935. Apr.

[20] J.R. Marti, L.R. Linares, Real-time EMTP-based Transients Simulation, IEEE Transactions on Power Systems 9 (3) (1994) 1309–1317. Aug.

[21] H.W. Dommel, Nonlinear and Time-Varying Elements in Digital Simulation of Electromagnetic Transients, IEEE Transactions on Power Apparatus and Systems PAS-90 (6) (1971) 2561–2567. Nov.

[22] S.M. Chan, V. Brandwajn, Partial Matrix Refactorization, IEEE Transactions on Power Systems 1 (1) (1986) 193–199. Feb.

[23] M. Szechtman, First Benchmark Model for HVDC Control Studies, Electra 135 (1991) 55–73.

[24] A.M. Gole, O.B. Nayak, T.S. Sidhu, M.S. Sachdev, A graphical electromagnetic simulation laboratory for power systems engineering programs, IEEE Transactions on Power Systems 11 (2) (1996) 599–606. May.