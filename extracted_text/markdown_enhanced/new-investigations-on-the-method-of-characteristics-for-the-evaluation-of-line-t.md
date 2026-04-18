## New investigations on the method of characteristics for the evaluation of line transients
T. Kauffmann, I. Kocar*, J. Mahseredjian
Polytechnique Montreal, University of Montreal, QC H3T 1J4, Canada

*Corresponding author. E-mail address: i.kocar@polymtl.ca (I. Kocar).

### Article Info
**Article history:**
Received 13 December 2017
Received in revised form 28 February 2018
Accepted 5 March 2018

**Keywords:**
Method of characteristics
Transient analysis
Transmission lines
Frequency and time domain analysis

## Abstract
The method of characteristics (MoC) transforms line equations into ordinary differential equations, and the numerical transient solution is typically performed through discretization in time and space. There exits also a version of MoC proposed in the literature, in which the discretization in space is eliminated for uniform lines. This has the potential to render the MoC faster than the traveling wave-based models. This paper examines in detail the possibility of removing spatial discretization and extends the application for the evaluation of transients on cables in addition to transients on lines. It has been demonstrated that, although removing spatial discretization is possible by introducing certain change of variables and approximations, the resulting model has limited numerical precision and may show numerically unstable behavior. This is principally due to the approximation error introduced by the linearization of differential equations, necessary to obtain a relationship between line ends. The paper discusses other sources of numerical errors and shows that the line needs to be subdivided to improve precision.

© 2018 Elsevier B.V. All rights reserved.

## 1. Introduction
The most common transient solution method of lines is based on traveling wave equations and obtained by transforming the frequency domain equations into time domain. In the frequency domain, lines and cables are characterized with two frequency dependent coefficients: the propagation function $H$ and the characteristic admittance $Y_c$. The basic idea of the frequency dependent models in Electromagnetic Transient Type (EMT-type) programs is to use rational function approximations for these coefficients, obtained by using fitting techniques, to allow efficient computation of convolution integrals through recursive schemes. The Universal Line Model (ULM) is the prevailing approach [1]. The recent effort in this field is on the passivity enforcement of models [2], improvement of numerical stability [3,4], enforcement of symmetry [5] and real time implementation [6]. Alternative models include the frequency dependent line model [7], obtained with the assumption of constant transformation matrices, and the frequency dependent cable model proposed to deal with systems having large number of coaxial cables [8].

Another class of transient solution techniques is based on the application of method of characteristic (MoC). This technique transforms the partial differential equations (PDEs) into sets of ordinary differential equations (ODEs) directly in time domain by using characteristic curves. It was successfully applied to study corona on transmission lines with constant parameters [9]. Further research efforts not only focus on the frequency dependence of parameters but also deal with non-linear [10], external field-excited [11] and non-uniform transmission lines [12]. The MoC requires spatial discretization in addition to discretization in time. Therefore, the solution is inefficient for uniform lines compared to traveling wave models such as ULM. On the other hand, an alternative solution procedure has been proposed for MoC to remove spatial discretization for uniform lines by using the relationship on the propagation speed of modal waves along characteristic curves [13,14]. This approach seems promising since the removal of spatial discretization has the potential to render the technique very efficient due to the following key advantages:

- As opposed to two convolutions for each end in traveling wave models only one convolution is required
- Traveling wave models require the fitting of $H$ and $Y_c$. In the MoC, however, the series impedance elements are needed to be fit, which are smoother.

This paper first presents a fitting procedure for series impedance elements and then contributes important clarifications on the application of MoC without spatial discretization, identifies the sources of numerical errors, and discusses variations for improvement. It is shown that the fundamental source of numerical problems is the approximation error arising from the linearization of differential equations relating line terminal variables. A large integration step dictated by the modal delays is required when it is desired to eliminate spatial discretization. This paper concludes that the line should be subdivided to improve numerical precision and maintain stability. The subdivision of line however supresses struct the overdetermined system of equations for both stages of fitting.

One remark in the solution of (4) is related to $D$. It should correspond to a constant line inductance at high frequencies and letting it be an unknown variable has one sole purpose of relaxing the fitting process and minimizing the order of fitting. However, the fitting result should be checked carefully if the product $DC$ produces realistic modal velocities, i.e. less than speed of light.