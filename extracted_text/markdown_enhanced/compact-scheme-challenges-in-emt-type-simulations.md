# Compact scheme challenges in EMT-Type simulations

M. Jafari Matehkolaei $^{a,*}$, B. Bruned $^{b}$, J. Mahseredjian $^{a}$, A. Masoom $^{c}$, I. Kocar $^{a}$

$^{a}$ Polytechnique Montreal, Canada  
$^{b}$ RTE, Jonage, France  
$^{c}$ Hydro Quebec Research Institute, Canada  

*Corresponding author.* E-mail addresses: mohammad.jafari-matehkolaei@polymtl.ca (M.J. Matehkolaei), boris.bruned@rte-france.com (B. Bruned), jean.mahseredjian@polymtl.ca (J. Mahseredjian), masoom.alireza@hydroquebec.com (A. Masoom), ilhan.kocar@polymtl.ca (I. Kocar).

**Keywords:** Compact scheme, Discontinuity treatment, Electromagnetic transient simulation, Nonlinearity, Numerical integration methods, Trapezoidal integration

**Abstract:** This paper investigates the potential of using the compact scheme (CS) integration method for Electromagnetic Transient simulation of power systems due to its high accuracy. It focuses on the challenges encountered with CS at discontinuity instants. Initially, the accurate response of the components at discontinuities and the impact of iterations at slope changes of nonlinear devices are elaborated. Afterward, the performance of CS at discontinuities is investigated. This work demonstrates that CS produces abnormal results at discontinuity instants. Consequently, a new method is proposed to overcome these issues. The formulation of network equations discretized with CS in the modified augmented nodal analysis (MANA) framework is then elaborated and compared to sparse Tableau formulations. Case studies are presented to validate the performance of the proposed discontinuity treatment method.

## 1. Introduction

POWER system operators mostly count on conventional system simulation models, also known as phasor-domain transient (PDT) models, for the reliable operation of their system. PDT models have demonstrated acceptable speed and performance for traditional stability studies. However, these models have a low frequency bandwidth, and are incapable of maintaining simulation accuracy as the number of inverter-based resources (IBR) and power electronic converters increases in modern power systems [1]. Conversely, electromagnetic transient (EMT) simulation tools are gaining more global attention as they address the problems associated with PDT models and offer a comprehensive insight into the details of all the parameters. However, EMT simulation tools are normally slower than PDT simulation tools due to the complexity and nonlinearity of the models involved. Therefore, it is needed to explore new strategies for enhancing the performance of EMT simulation tools [2,3].

Numerical integration methods are the core of every EMT simulation, utilized to discretize the differential equations associated with the dynamics of the system models [4]. In [5], a brief comparison of some numerical integration methods used for the EMT simulation of power systems is presented. The performance of numerical integration methods in terms of accuracy, stability, and computational burden plays a crucial role in determining the overall performance of the associated EMT simulation [4,6]. Adopting an integration method with high accuracy can potentially enhance the simulation speed due to the possibility of leveraging large simulation time-steps. Therefore, this paper explores the potential of using compact scheme (CS) [7,8] as an integration method for EMT simulations due to its stated higher accuracy compared to the widely used trapezoidal rule (TR). Compact scheme accounts for the first derivative values that can improve simulation accuracy.

Discontinuities refer to switching events and slope changes of nonlinear elements which bring challenges in EMT-type simulation tools. Unlike L-stable methods like Backward Euler (BE), A-stable methods (like TR) produce fictitious oscillations at discontinuities, necessitating additional measures to address this issue. A comprehensive analysis of various discontinuity treatment methods is presented in [9].

In this paper, the real behavior of parameters at discontinuities is investigated with their physical equations and compared with the TR, BE and CS responses. Additionally, the impact of iterations at slope changes of piecewise linear elements, on the accuracy of the simulation results will be analyzed. It is demonstrated that CS encounters limitations at discontinuity instants and further actions must be adopted. Consequently, a combined CS with BE (CS_BE) method is proposed to solve the CS issues at discontinuities. Furthermore, this paper elaborates on the procedure for formulating network equations discretized with CS in Modified-Augmented-Nodal-Analysis (MANA) [6]. Consequently, a comparison of simulation performance between MANA and Sparse Tableau Approach (STA) usage in [10] is provided. All the test cases are coded in Julia programming language to ensure consistent testing benchmarks. The KLU solver [11] is used for solving the linear systems and the results are validated with EMTP® [6].

$$x_{k+1} = x_k + \frac{\Delta t}{2} (f_{k+1} + f_k) \tag{6}$$

With TR, the discretized equation of inductor in (2) is:
$$i_{k+1} = i_k + \frac{\Delta t}{2L} (v_{k+1} + v_k) \tag{7}$$

If the inductor current is suddenly forced to zero due to switching ($i_{k+1} = 0$), the voltage of the inductor at the time-point exactly after opening the switch is calculated as:

This paper is organized as follows. Section II presents an analysis of circuit real behavior at discontinuity instants, along with a comparison to the performance of TR, BE and the combined TR and BE methods (TR_BE) used at discontinuities. The CS and its formulation in MANA are covered in Section III. Section IV presen