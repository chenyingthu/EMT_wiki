# Interpolation for power electronic circuit simulation revisited with matrix exponential and dense outputs

**Peng Li, Zixiang Meng, Xiaopeng Fu, Hao Yu, Chengshan Wang**  
*Key Laboratory of Smart Grid of Ministry of Education, Tianjin University, Tianjin, China*

**Keywords:** Electromagnetic transients, Power electronic, Exponential integrator, Dense output formula

**Abstract:** With a high penetration of power electronic equipment, transient simulation for power electronic circuit has been a main challenge for performance improvement of the electromagnetic transient simulation tools. In this paper, two new solvers for the matrix exponential-based simulation method are proposed based on the dense output formula and Padé approximation of different orders. The proposed solvers are implemented with the optimal combination of numerical integration method and interpolation method. Both solvers are L-stable. One has 3rd-order accuracy which is more accurate than existing simulation tools in power electronic simulation. The other solver achieves 1st-order accuracy with a lower precision numerical integration method than the same-order algorithms and is appealing from computation speed perspective. Numerical studies including TCR circuit and two types of VSC-HVDC systems are conducted to demonstrate the effectiveness of the proposed solvers.

*This work was supported by The National Natural Science Foundation of China under Grant 51807131 and 51961135101.*  
*Corresponding author.*  
*E-mail addresses: lip@tju.edu.cn (P. Li), mzx1996@tju.edu.cn (Z. Meng), fuxiaopeng@tju.edu.cn (X. Fu), tjuyh@tju.edu.cn (H. Yu), cswang@tju.edu.cn (C. Wang).*

## 1. Introduction

With large-scale application of power electronic equipment, the power system is facing unprecedented challenges in its operation and control. Considering the interaction between the high frequency power electronic circuits and control systems, the electromagnetic transient (EMT) simulation programs become the preferred choice among system dynamic analysis tools [1]. The increasing system scale and complexity has attracted more and more attention on the computational efficiency and accuracy of EMT simulation. Facing these challenges, traditional EMT simulation methods may experience reduced accuracy level and smaller step sizes with more computational burden. All of these have pushed the research on a more accurate and efficient EMT simulation method.

The current mainstream EMT simulation tools are the Electro-Magnetic Transient Program (EMTP)-type programs, which are based on the nodal analysis framework [2]. Among them, EMTP [3], PSCAD [4], and ATP [2,5] are commonly used. The trapezoidal integration formula is adopted as the numerical integration method for simulation calculation in most of the tools with a few exceptions such as XTAP [6]. The trapezoidal method has the characteristics of A-stability and 3rd-order local truncation error (LTE), while the 2s-DIRK formula adopted in XTAP has also L-stability. The modified-augmented-nodal analysis is proposed in [3] and applied in EMTP, which eliminates various limitations of the classical nodal and modified nodal analysis. For the switch events, PSCAD uses linear interpolation for the switching event localization and a half-step linear interpolation to suppress oscillations [4,7]. The difficulty of using higher-order interpolation formulas lies in the lack of extra points for the one-stage methods. EMTP implements Backward Euler integration for the steps after switch events to avoid numerical oscillation. The power switches are optionally modeled as nonlinear elements and solved in an iterative solution process for the accurate calculation of switch status. These 2nd-order accurate approaches, however, are reported to experience accuracy degradation for the simulation of power electronic converter studies [8].

State space formulation is an alternative framework for EMT simulation with the advantage of flexible choice of various integration methods. It can be used in combination with the nodal analysis formulation through SSN (state-space nodal) method [9]. An example in this category is the ARTEMiS art5 solver of RT-LAB, which is based on the Padé [2/3] approximation of the matrix exponential and achieves 5th-order accuracy [10]. However, the standard ARTEMiS solver does not locate switch events, which leads to similar problems as the above tools. Recently, an improved transient simulation algorithm combining TR-BDF2 method and quadratic interpolation formula was proposed [11]. TR-BDF2 is a two-stage implicit method, which enables the adoption of quadratic interpolation and keeps the 2nd-order accuracy at switch events. However, two-stage methods require more computation per step than the one-stage methods.

The matrix exponential-based integration method, originated from the applied mathematics community [12], is recently proposed to be used in power system EMT simulations [13]. Case studies have shown that compared to existing algorithms, matrix exponential method is

$$
x(t_0 + h) = [I_n \quad 0] \cdot e^{h\mathbf{A}} \cdot x_0
$$
where
$$
\mathbf{A} = \begin{bmatrix} A & B u(t_0) \\ 0 & 0 \end{bmatrix}, \quad x_0 = \begin{bmatrix} x(t_0) & 1 \end{bmatrix}^T \tag{2}
$$

where $h$ is the simulation step size and $I_n$ is the identity matrix. It turns out t