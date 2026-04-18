# Fast investigation of control interaction risks in PV parks using eigenvalue analysis in Modelica

A. Masoom$^{a,*}$, J. Mahseredjian$^{b}$, U. Karaagac$^{c}$

$^{a}$ Hydro-Québec Research Institute, Varennes, QC J3X 1S1, Canada  
$^{b}$ Department of Electrical Engineering, Polytechnique Montréal, Montreal, QC H3T 1J4, Canada  
$^{c}$ Department of Electrical and Electronics Engineering, Middle East Technical University, Turkey

**Keywords:** Modelica, Equation-based modeling, PV park, Eigenvalue analysis, State-space equations, Linearization, Stability analysis, Impedance scanning, Phase margin, Modal Analysis

**Abstract:** This paper contributes to the fast detection of control interaction risk in a PV park using the eigenvalue analysis in Modelica. The entire PV park and its interconnected network are represented by time-domain equations in Modelica, then linearized state space equations are extracted directly by leveraging the Modelica features. This constitutes an advantageous approach for fast finding eigenvalues and extracting potential instability conditions. The presented approach is verified with electromagnetic transient (EMT) simulation and impedance-based stability analysis (IBSA) that uses EMT-type impedance scanning methods. The results show an outstanding improvement in the simulation time and accuracy.

## 1. Introduction

### 1.1. Literature review

The controllers of inverter-based resources (IBRs) with full-size converter (FSC), such as type-4 wind or photovoltaic (PV) parks, can interact with the transmission grid, potentially causing instability. The control interaction (CI) in weakly tied IBRs (either with doubly-fed induction generator (DFIG) or FSC) may occur due to the resonance formed by the capacitive IBR and the inductive grid [1,2]. This phenomenon has been confirmed with several real-world incidents [3]. In addition, the recent research in [4] identified a new CI phenomenon between a large-scale type-4 wind park and a 500 kV transmission grid in which one of the parallel transmission lines interacts with the wind park in super-synchronous frequency range.

Several methods have been evolved for the prediction of CI risks in IBR integrated systems [5]. The widely used methods include impedance-based stability analysis (IBSA) [6,7] in various reference frames [8], state-space model-based eigenvalue analysis (EV) [9–11], and electromagnetic transient (EMT) simulation [12].

The IBSA-based methods are well-defined in the literature [8]; whilst it is appropriate for large-scale power systems with black box models. The modern transmission grids employ several IBRs in addition to conventional generating units (such as thermal power plants). However, the IBSA can identify only the CI risk of the IBR under study as all other IBRs in the grid subsystem are indirectly represented in equivalent grid impedance. Hence, IBSA does not give any insight regarding CI mechanisms and any hints for its mitigation. It should be noted that the IBSA was born for analyzing two terminal systems and it is hard to extend this method for analyzing multi-terminal systems [13].

The EMT studies offer a valid and direct EMT simulations on the risk of instability; however, they are not also able to identify and explain the causes and nature of problem. The EMT simulation-based assessment is typically performed to validate either the IBSA or EV results [14].

### 1.2. Motivation

The EV analysis has been earlier employed and well documented for exploring the CI risk in the WPs [15–18]. The generic solutions presented in the literature are usually based on a simplification of each component of a system to a linear time-invariant one and representing them with its state space equations in dq-frame, finally combining them based on their actual connections to form the whole system. The state-space representation of large-scale systems is complicated. Each change of circuit topology leads to a new extraction of system equations, where this approach is not implemented in a graphical interface, and mostly relies on laborious manipulation of the adjacency matrices and equations in procedural programming languages, such as MATLAB or Julia [19]. In addition, the simplifications in the linearization process of generic models, such as ignoring input measuring filters cause significant accuracy problems even for small perturbation scenarios that do not activate any non-linearity such a

components (i.e. loads, transformers, lines, etc.) are first flattened and represented through a system of DAEs:

$$F(t, \dot{x}, x, y, z) = 0 \tag{1}$$

where $t$ denotes time, $x$ is the vector of state variables, $y$ is the vector of algebraic variables and $z$ is the vector of input variables. Eq. (1) can be reformulated as:

$$
\begin{aligned}
\dot{x} &= h(t, x, u) \\
y &= k(t, x, u)
\end{aligned} \tag{2}
$$

It is possible to linearize (2) using the Taylor series around an arbitrary time point, $t_l$, (i.e., different operating conditions and contingencies such as before and after disturbances) as: