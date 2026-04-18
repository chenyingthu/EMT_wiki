# Simulation of electromagnetic transients with a family of implicit multi-step oscillation-free formulas ⋆

**Enrique Melgoza-Vázquez**  
*Tecnológico Nacional de México / I. T. Morelia, Av. Tecnológico 1500, Morelia, Mich, C P 58120, México*

**Keywords:** Time-domain simulation, Numerical oscillations

**Abstract:** The backward differentiation formulas are a family of implicit integration rules which generalize the backward Euler finite difference formula and may be used for electromagnetic transient simulation. These multi-step formulas require a number of history terms, improving the precision as the order increases. This approach was used to implement a computation platform based on the modified nodal analysis, where the integration rule may be changed as desired. Integration rules of orders one to five were tested. The additional computer memory requirements are modest and are not an issue for modern computer equipment. The obtained response is free from numerical oscillations due to switching operations in all cases, without requiring additional checks or special control of the computation. Since the history terms enter the global equation only through the right hand vector, the scheme may be implemented in existing transients programs with only minor changes to the code base, providing a reliable simulation resource with fixed or variable time step sizes.

⋆ Paper submitted to the International Conference on Power Systems Transients (IPST2025) in Guadalajara, Mexico, June 8–12, 2025.  
E-mail address: enrique.mv@morelia.tecnm.mx  
https://doi.org/10.1016/j.epsr.2025.112402  
Received 6 January 2025; Received in revised form 8 April 2025; Accepted 17 October 2025  
Available online 29 October 2025  
0378-7796/© 2025 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

## 1. Introduction

The growing addition of inverter-based resources (IBR) into electrical power systems demands the analysis of complex interaction issues such as frequency and voltage stability, sub-synchronous resonances, harmonic interactions and other phenomena. Due to the nonlinearity and frequency dependence of such systems, a time-domain analysis is required in many cases [1].

Time-domain simulations have thus become an important tool in the planning and operation of electrical power systems with high penetration of IBRs. The time scales of the analyzed phenomena often reach the order of minutes; on the other hand, the detailed representation of inverter commutation and control actions call for small time-steps, of the order of microseconds. As a result, the simulation of a complete case takes a long time, generates huge data files and is cumbersome to handle. Several alternatives are being explored to circumvent the aforementioned drawbacks, among them hybrid simulation [2], multi-scale approaches [3], parallel simulations [4–10], and other approaches. New integration rules and optimized implementations are also of interest [2,3,11,12].

The so-called electromagnetic transients (EMT) programs currently available generally use a single-step time discretization formula, namely the trapezoidal formula, because it fulfills the desirable characteristics of absolute stability and good precision. However, it is known that the trapezoidal formula is prone to numerical oscillations when certain conditions are encountered in the simulation, such as the opening of an inductive branch [13]. Therefore, some corrective measures have to be taken in the implementation of time-stepping schemes based on the trapezoidal formula, with techniques such as critical damping adjustment (CDA), and interpolation [13].

In this paper, the use of multi-step formulas is explored with the purpose of adding flexibility to the time domain simulations of electrical systems. We focus particularly on the backward differentiation formulas (BDF), a class of multi-step time discretization scheme which is a generalization of the backward Euler formula (BEF). It is known that the BEF is absolutely stable and immune to numerical oscillations; in fact, in some implementations it replaces the trapezoidal rule for a few time steps in order to eliminate the numerical oscillation. The BEF, despite this desirable feature, is not generally used in EMT programs because of its low precision. However, when applied in its generalized form with multiple steps, its precision is improved. In this paper, the implementation and performance of the multi-step BDFs in the context of EMT programs is considered.

## 2. Backward differentiation formulas

For EMT analysis, the ordinary differential equation
$$ \mathbf{C}(\mathbf{x}, t)\dot{\mathbf{x}} + \mathbf{K}(\mathbf{x}, t)\mathbf{x} + \mathbf{f}(\mathbf{x}, t) = \mathbf{0} \quad (1) $$

**Table 1:** The $\alpha_i$ coefficients for constant time step size.

| BDF order | $\alpha_i$ coefficients |
|:---:|:---|
| 1 | $-1$, $1$ |
| 2 | $-3/2$, $-1/2$, $2$ |
| 3 | $-11/6$, $3$, $-3/2$, $1/3$ |
| 4 | $-25/12$, $4$, $-3$, $4/3$, $-1/4$ |
| 5 | $-137/60$, $5$, $-5$, $10/3$, $-5/4$, $1/5$ |

### 2.2. Extension to nonlinear systems

Application of the BDF formula (2) to the system Eq. (1) results in [20]:
$$ \left( -\frac{\alpha_0}{h} \mathbf{C}_{n+1} + \mathbf{K}_{n+1} \right) \mathbf{x}_{n+1} + \left[ \dots \right] $$