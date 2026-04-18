# High-accuracy EMT simulations through pole-residue compensation ⋆

A. A. Kida $^{a,*}$, A.C.S. Lima $^{b}$, F. A. Moreira $^{c}$, F. M. Vasconcellos $^{c}$

$^{a}$ Federal Institute of Bahia, Salvador, BA, Brazil  
$^{b}$ Department of Electrical Engineering, COPPE/UFRJ, Federal University of Rio de Janeiro, Rio de Janeiro, Brazil  
$^{c}$ Department of Electrical and Computer Engineering, Federal University of Bahia, Salvador, BA, Brazil

**Keywords:** Rational approximation, Pole-residue formulation, Time-frequency analysis, Frequency warping, Simulation accuracy

**Abstract:** This paper addresses the frequency warping error in frequency-dependent equivalents to improve the accuracy of Electromagnetic Transient (EMT) simulations. This numerical error, intrinsic to all linear multi-step integration methods, such as the trapezoidal rule, distorts frequency response and degrades time-domain simulation accuracy. This work introduces the Pole-Residue Frequency Warping Compensation (PRFWC) algorithm to mitigate the frequency warping in rational approximations with the pole-residue formulation. Performance validation of the proposed algorithm is conducted through two case studies: a transmission line and a distribution system. Numerical results show that the PRFWC improves simulation accuracy by two orders of magnitude over uncompensated models, with minimal computational burden.

⋆ Paper submitted to the International Conference on Power Systems Transients (IPST2025) in Guadalajara, Mexico, June 8–12, 2025.  
∗ Corresponding author.  
E-mail addresses: alexandre.kida@ifba.edu.br (A.A. Kida), acsl@dee.ufrj.br (A.C.S. Lima), moreiraf@ufba.br (F.A. Moreira), felipe.vasconcellos@ufba.br (F.M. Vasconcellos).  
https://doi.org/10.1016/j.epsr.2025.112394  
Received 6 January 2025; Received in revised form 3 March 2025; Accepted 17 October 2025  
Available online 30 October 2025  
0378-7796/Published by Elsevier B.V.

## 1. Introduction

The increasing complexity of power systems are accelerated by the energy transition from fossil-based to low-carbon and renewable sources [1]. As a result, in-depth analysis of new dynamic interactions between their components and subsystems is paramount [2]. In this context, Electromagnetic Transient (EMT) simulations are an essential tool that can be tuned to provide sufficient accuracy to anticipate these interactions, ensuring reliable and efficient power system planning and operation.

Accurate yet efficient simulations can be achieved by preserving the frequency characteristics of subsystems using frequency-dependent equivalents [3,4]. A common approach is to represent these equivalents using rational functions derived from data-driven curve-fitting techniques [5–7]. Vector Fitting (VF) stands out among the curve-fitting techniques for its computational efficiency, accuracy, straightforward formulation, versatility, and open-source availability [5]. Additionally, it is embedded in various EMT-type simulators, including EMTP-ATP [8], EMTDC/PSCAD [9], and EMTP [10].

Time-domain simulations require careful consideration regarding discretization techniques. The trapezoidal rule is widely employed in commercial EMT-type simulators [11] as it is the most accurate among linear multi-step integration methods with A-stability [12].

The continuous-time domain transfer function of the integrator is
$$ \frac{b(s)}{u(s)} = \frac{1}{s}, \quad (1) $$
where $b(s)$ and $u(s)$ are the output and the input of the integrator in s-domain, respectively; $s$ is the complex frequency variable in the s-domain.

Applying the trapezoidal rule to derive the transfer function of (1) in the discrete-time domain yields:
$$ \frac{B[z]}{U[z]} = \frac{h}{2} \left( \frac{1+z^{-1}}{1-z^{-1}} \right), \quad (2) $$
where $B[z]$ and $U[z]$ are the Z-transforms of $b(s)$ and $u(s)$, respectively, obtained using the trapezoidal rule; $z$ is the complex variable in the Z-domain.

By equating (1) and (2), then solving for $z$, yields the bilinear transformation (also known as the Tustin method) [13]:
$$ z = \frac{1 + 0.5sh}{1 - 0.5sh}. \quad (3) $$

The mapping between the analog (continuous-time) frequency $\omega_a$ and its corresponding digital frequency $\omega$ is derived by substituting $s = j\omega_a$ and $z = \exp(j\omega h)$ into (3), where $h$ is the integration time-step.

Solving for $\omega_a$ yields:
$$ \omega_a = \frac{2}{h} \tan\left( \frac{\omega h}{2} \right). \quad (4) $$

The nonlinear frequency mapping between $\omega_a$ and $\omega$ in (4) compresses the discrete-time frequency scale, introducing a numerical error known as frequency warping [14]. This error is not unique to the trapezoidal rule but is inherent to all linear multi-step integration methods [13].

Strategies for frequency warping mitigation mainly involve adjusting the $h$ size, pre-warping, or relying on non-standard solution techniques.

Pre-warping techniques are mostly considered in the context of digital filter design [15–17]. For instance, a digital frequency specification, such as its cutoff frequency, is prewarped using (4) to build the analog prototype low-pass filter specification, which is then transformed into the desired filter transfer function [15]. Applications of pre-warping for frequency-dependent equivalent (FDE) and power systems are scarce in the literature. In that regard, the author in [18] p