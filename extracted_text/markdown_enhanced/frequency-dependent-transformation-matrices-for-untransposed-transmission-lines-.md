## Frequency-Dependent Transformation Matrices for Untransposed Lines using Newton-Raphson Method

**L. M. Wedepohl**$^1$, **H.V. Nguyen**$^1$, **G.D. Irwin**$^2$  
$^1$ Department of Electrical Engineering, The University of British Columbia, Vancouver, Canada  
$^2$ Manitoba HVDC Research Centre, Winnipeg, Canada  
*(FEE, Student Member, IEEE, Member, IEEE)*

**ABSTRACT**  
The frequency-dependent aspects of transmission line transformation matrices along with their asymptotic behaviours at high and low frequencies are thoroughly investigated in this paper. The Newton-Raphson (NR) method for evaluating the transformation matrices as smooth functions of frequency is introduced. A different technique which utilizes a conventional diagonalization algorithm and a correlation technique for tracking the order of the eigenvectors and eigenvalues is used to confirm the validity of the NR method. Transformation matrices for typical line configurations are evaluated and discussed. The paper concludes that the NR method is more efficient and appropriate for use in the time domain frequency-dependent line models in the Electromagnetic Transient Program (EMTP).

**Key words:** transformation matrix ($T_v$), Newton-Raphson (NR), line model, EMTP.

## 1. INTRODUCTION

The interest in accurately modelling the frequency-dependent aspects of untransposed transmission lines in the time domain has been investigated over the last two decades. Although much improvement has been made, it is still usual to assume a constant transformation matrix for conversion between the modal and the time domain in the present line models [1]. It is well known that constant transformation matrices are accurate enough for single flat circuit lines. However, for the case of double- or more circuit lines, the accuracy decreases noticeably, especially in the studies which require to cover wide frequency ranges [2].

It has been recognized that in order to efficiently include the frequency-dependent nature of the transformation matrices in time domain simulations, rational approximations need to be performed [3]. To achieve this, the elements of such matrices have to be continuously evaluated over a wide frequency range (1 Hz - 1 MHz). Furthermore, they have to be smooth. This has only been possible for underground cables [3]. For multi-circuit overhead lines, however, the transformation matrix elements do not always behave smoothly. It will be shown in this paper that the proposed NR method completely overcomes this limitation. Modal parameters of multi-circuit overhead lines produced by the proposed NR method are smooth and well behaved. Furthermore, they can be fitted with rational functions of the minimum-phase-shift type with real negative poles and zeros. With this type of function, the approximate modal parameters can be effectively incorporated into the EMTP line model using the trapezoidal rule, and numerical stability is achieved [3,4]. The time-domain implementation procedure could be followed exactly in the same manner as it was formulated and described in reference 3. It will not be repeated here due to space constraint. Thus, the main contribution of the paper lies in the development of the NR-based method.

## 2. TRANSMISSION LINE THEORIES

The fundamental telegrapher's equations for a multiphase transmission line are:

$$ \frac{d^2V}{dx^2} = [ZY]V $$
$$ \frac{d^2I}{dx^2} = [YZ]I $$

Where $Z$ and $Y$ are the per unit length series impedance and the shunt admittance matrices, respectively. $V$ and $I$ are column voltage and current matrices.

It is well known that the $n$-phase equations (1) are solved by transforming the $n$ coupled equations into the $n$ decoupled equations. To achieve this, a modal transformation matrix $T_v$ which diagonalizes the $YZ$ product is evaluated from the solution of the eigenproblem

$$ T_v^{-1} [YZ] T_v = h \quad (2) $$

where $h$ is the diagonal eigenvalue matrix.

The matrix $T_v$ varies with frequency since $Y$ and $Z$ are frequency-dependent. It is necessary to investigate the nature of the $T_v$ matrix only since the matrix $T_i$ which diagonalizes the product $ZY$ can be evaluated directly from $T_v$. It is very important to mention that $T_v$ and $T_i$ are equal only when $Z$ and $Y$ are functions of the same matrix [5]. In practice, $Z$ and $Y$ are functions of the same matrix only when the system is completely balanced.

## 3. FREQUENCY-DEPENDENT NATURE OF Y & Z

In order to fully understand the characteristics of the $T_v$ matrix, it is relevant to describe individually the frequency-dependent nature of the $Y$ and $Z$ matrices. The $Y$ matrix takes the following form,

$$ Y = j \omega P^{-1} \quad \text{with} \quad P_{ij} = \ln \frac{D_{ij}}{d_i} \quad (3) $$

The term $d_e = \sqrt{\frac{\rho}{j \omega \mu_0}}$ is the earth complex depth of penetration, $x$ and $y$ are the horizontal and vertical co-ordinates of the conductors, respectively; and $\rho_e$ is the earth resistivity.

The validity of equation (6) has been tested and confirmed in [6]. The results agree very closely with those obtained from Carson's integral. The maximum error is only a few percent in the kHz range. This is of very little consequence in transient calculations where the entire frequency spectrum contributes to the results anyhow. Furthermore, the value depends amongst others on a knowledge of the earth resistivity $\rho_e$, which is not only not accurately known, but is subject to quite wide seasonal variations accord...