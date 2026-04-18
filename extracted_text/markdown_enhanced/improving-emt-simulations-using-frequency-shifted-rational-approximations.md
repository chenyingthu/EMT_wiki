# Improving EMT simulations using frequency-shifted rational approximations ⋆
A. A. Kida$^{a,*}$, A. C. S. Lima$^{b}$, F. A. Moreira$^{c}$, F. M. Vasconcellos$^{c}$

$^{a}$ Federal Institute of Bahia, Salvador, BA, Brazil  
$^{b}$ Department of Electrical Engineering, COPPE/UFRJ, Federal University of Rio de Janeiro, Rio de Janeiro, Brazil  
$^{c}$ Department of Electrical and Computer Engineering, Federal University of Bahia, Salvador, BA, Brazil  

**Keywords:** Rational modeling, vector fitting, complex vector fitting, power system transients, frequency-shifted simulations

**Abstract:** Accurate electromagnetic transient (EMT) simulations require accounting for the frequency-dependent behavior of system components and equivalents. Rational approximations derived from curve-fitting techniques such as Vector Fitting (VF) are commonly employed to represent these equivalents. Complex Vector Fitting (CVF), a variant developed for modeling baseband communication systems, eliminates the complex conjugacy symmetry constraint found in VF. This work introduces a CVF-based framework incorporating analytic signals and frequency shifts to enhance EMT simulations of power systems. Validation with a transmission line and a distribution network demonstrates that CVF reduces errors by up to eight orders of magnitude compared to VF, along with notable passivity differences. Frequency shifts further enhanced the accuracy of the CVF-based framework by up to two additional orders of magnitude. Additionally, these frequency shifts enabled a time-step size increase by a factor of 2.33 to 5.5 for the same target accuracy, thereby reducing computational effort. These findings establish the proposed framework as an effective tool for power system analysis.

⋆ Paper submitted to the International Conference on Power Systems Transients (IPST2025) in Guadalajara, Mexico, June 8–12, 2025.  
* Corresponding author.  
E-mail addresses: alexandre.kida@ifba.edu.br (A.A. Kida), acsl@dee.ufrj.br (A.C.S. Lima), moreiraf@ufba.br (F.A. Moreira), felipe.vasconcellos@ufba.br (F.M. Vasconcellos).

## 1. Introduction
High-accuracy modeling of power system components (lines, cables, transformers, switchgear, generators and loads) must represent their dynamic behavior across a wide frequency range. However, detailed modeling of every component in a large and complex power system is computationally prohibitive for electromagnetic transient (EMT) studies.

A conventional approach that balances accuracy and efficiency divides the system into a study area and an external area [1]. The latter can be represented by a frequency-dependent equivalents (FDE), preserving its frequency response beyond the grid frequency. Rational approximations are widely used for representing such equivalents [2].

The pole-relocation algorithm known as Vector Fitting (VF) [3–5] is a reliable tool for fitting a rational approximation to a tabulated frequency response data set. VF is also integrated into major EMT simulation software, such as ATP [6], PSCAD [7] and EMTP [8].

The model built with VF inherently produces real-valued impulse response, $x(t)$, whose spectra, $X(\omega)$, exhibit Hermitian symmetry, satisfying $X(-\omega) = X^*(\omega)$ [9]. However, this constraint limits its applicability to physical systems only, hindering VF from leveraging computationally efficient baseband (frequency-shifted) simulations.

To address this limitation, Ye et al. [10] proposed Complex Vector Fitting (CVF) for baseband modeling of photonic systems described by scattering parameters. In [11], the scope of CVF was extended to the modeling of electric power system components represented by admittance parameters along with strategies aimed at enhancing its computational efficiency. However, that study focused solely on a single test system, neglected time-domain simulations, and did not explore the frequency-shifting capabilities of CVF for EMT applications. This paper addresses these limitations.

This work advances the findings of [11] through several contributions. First, it provides further evidence that the enhanced flexibility of CVF improves fitting accuracy, even without frequency shifts. Additionally, it reveals significant differences in passivity characteristics between the model set up with VF and CVF, which were previously unidentified. Lastly, it proposes a novel framework that utilizes frequency shifting and analytic signals to enhance the efficiency of EMT simulations.

This paper is structured as follows. Section II introduces admittance matrix synthesis and passivity conditions. Section III addresses the analytic signals. Section IV introduces the proposed framework for efficient EMT simulations. Results followed by discussions are presented in Section V. Finally, Section VI presents the main conclusions of this work.

## 2. Frequency-domain realization
Frequency response samples of an unknown $N$-port admittance matrix $\mathbf{Y}(s) \in \mathbb{C}^{N \times N}$ can be obtained through measurements or simulations. The behavior of $\mathbf{Y}(s)$ can be modeled by a ratio where $'$ denotes the transpose operator for systems exhibiting Hermitian symmetry [15] and the complex conjugate transpose operator for systems lacking it [16]. Consequently, CVF cannot leverage the efficient half-size singularity test used for passivity assessment in VF [15], as this