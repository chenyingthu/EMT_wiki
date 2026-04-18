## Sparse solver application for parallel real-time electromagnetic transient simulations

B. Bruned$^{a,*}$, J. Mahseredjian$^{b}$, S. Dennetière$^{a}$, A. Abusalah$^{b}$, O. Saad$^{c}$

$^{a}$ RTE, Jonage, France  
$^{b}$ Polytechnique Montréal, Québec, Canada  
$^{c}$ Hydro-Québec, Varennes, Québec, Canada  

**Keywords:** EMT simulation, Real-time, Hardware-in-the-loop, Direct sparse linear solver, Parallelization, Compensation method

**Abstract:** The main purpose of this research is to speed up real-time simulations of electromagnetic transients (EMTs) using sparse linear solver techniques. This paper presents the integration of a direct sparse linear solver (KLU) into a real-time software for EMT simulation. This solver is combined with parallelization of network solution. Fill-in reduction techniques are investigated as well as partial refactorization to speed up computations. The pivoting technique during refactorization is asserted in terms of simulation stability as compared to existing sparse solver based on code generation without pivoting. Performance and validation are studied on practical power system cases with real-time Hardware-In-the-Loop (HIL) simulation. Substantial performance gains, up to 50%, are obtained using fill-in reduction and partial refactorization. Pivoting is necessary to maintain numerical stability.

* Corresponding author. E-mail address: boris.bruned@rte-france.com (B. Bruned).

## 1. Introduction

Energy Transition raises important challenges for grid operators to integrate renewable energy sources [1]. This involves more power electronics equipment in the grid and new interaction problems that must be simulated and studied. The circuit-based electromagnetic transient (EMT) simulation approach is currently increasingly used to study the integration of renewable energy sources [2]. It is able to deliver highly accurate computations. Moreover, real-time hardware-in-the-loop (HIL) EMT simulation can be used for accurate simulations with actual controller replicas [1]. The computation time is an important factor for HIL and parallelization of solution method is essential.

The traditional line-delay (LD) technique parallelization, is based on the propagation delay of transmission lines or cables. If this delay is greater than the numerical integration time-step, the network solution can be decoupled without any loss of accuracy. This technique has been implemented in both offline [3,4] and real-time environments [5]. When there is no LD, other techniques have to be implemented. One of such techniques is the compensation method (CM) [6,7]. In recent works [8,9] the CM has been programmed and tested in real-time mode with demonstrated advantages.

In addition to parallelization, sparse linear solvers [10] can be used to improve numerical performance. The nodal formulation of network equations involves the solution of sparse linear systems. Sparse LU decomposition is commonly used to solve such systems in EMT-type software. Previous works [4] have studied and integrated an efficient sparse LU decomposition solver named KLU [11,12], for parallel offline simulation. A modified version of KLU (MKLU) has been used to benefit from partial refactorization techniques.

The first contribution of this paper is to integrate and test MKLU into the real-time environment HYPERSIM [5], as a replacement of an existing legacy sparse solver (GenCode) based on code generation. It is the first time that such a solver is integrated into an industrial real-time simulation environment. The second contribution is to identify the most efficient sparse solver techniques to speed up real-time EMT simulation: fill-in reduction, partial refactorization and pivoting strategy. All are available in MKLU. Fill-in reduction and partial refactorization are combined for best efficiency. The third contribution is to combine these sparse solver techniques with parallelization techniques to speed up even more the simulation. Two kinds of parallelization technique are used in this paper, namely LD and CM. The performance of MKLU is compared with GenCode for practical power system cases.

This paper is organized as follows. The integration of MKLU solver is described in Section II. Through each step of the sparse linear solver, speed-up techniques are identified (fill-in reduction, partial refactorization). In Section III, a detailed comparison is performed between MKLU and GenCode on the impact of fill-in reduction, pivoting strategy and real-time performance for practical power system cases with HIL.

## 2. Direct sparse linear solver

Using classic nodal (modified-augmented-nodal analysis is not available in HYPERSIM) formulation with companion circuit models, network equations can be written in a linear form to be solved at each time-point:

$$Y_n v_n = i_n \quad (1)$$

where $Y_n$ is the admittance matrix of the network, $v_n$ the vector of node voltages and $i_n$ the known vector of current sources that include history term injections from companion factorized followed by the interface variables between the two graphs. Graph partitioning algorithms are used, like Metis [19] or Scotch [20]. Nested Dissection amounts to formulating the solved matrix into a bordered-block-diagonal form.

### 2.2. Factorization

Factorization is the main element of the resolution of a linear system and consists in numerically factoring the sparse matrix into the LU form. Different strategies can be chosen regarding scaling, pivoting and decomposition.

Scaling can be used to improve matrix conditioning. Scaling does not necessarily contribute in terms of accuracy and stability for the simulation of power systems. Indeed, as an example, switch modelling as $R_{open}/R_{close}$ resistors can create a wide range of values in the admittance