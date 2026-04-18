# An improved passivity enforcement algorithm for transmission line models using passive filters

H.M. Jeewantha De Silva $^{a,*}$, Mohammad Shafieipour $^{b}$  
$^{a}$ Manitoba Hydro International, Canada  
$^{b}$ Safe Engineering Services & Technologies ltd., Laval, QC H7L6E8, Canada  

**Keywords:** Electromagnetic transients, Passivity enforcement, Phase domain model, Passive filters  

**Abstract:** This paper proposes a simple but effective method based on shunt passive filters to enforce passivity on a frequency dependent transmission line model for multi-conductor cables and overhead lines. The passivity enforcement algorithm is applied to a widely-used frequency dependent line model in EMT-type software, the Universal Line Model. The passivity violating regions of the transmission line model are identified using the frequency sweep method. The passive shunt series RLC filters are added to the nodes of the transmission lines to eliminate passivity violations. Examples of multi-conductor underground cable systems are presented to demonstrate the validity of the proposed approach.

## 1. INTRODUCTION

Wideband transmission line models are widely used in electromagnetic transient (EMT) studies such as temporary over-voltages, switching over-voltages, network resonance, lightning over-voltages, etc. These models accurately consider frequency dependency as well as distributed nature of the line parameters for frequencies ranging from 0 Hz to a few MHz. In this paper, transmission line refers to both overhead lines and cables.

The time domain implementation of a transmission line involves several steps, which are summarized as follows. First, the line parameters such as propagation function and characteristic admittance are formulated in frequency domain for several frequency samples [1]. Next, by applying the “Vector Fitting” technique, the frequency domain characteristics are approximated using continuous rational functions [2, 3]. Finally, the recursive convolution method is applied to represent the transmission line equations as a standard EMT-type model. This includes a shunt conductance and a parallel current source.

Transmission lines are passive as a matter of physical reality. However, due to the errors in approximating frequency domain characteristics using rational functions as well as occasional frequency domain approximations, the resulting model may become non-passive [4]. It is observed that a non-passive model may lead to unstable time domain simulations. One of the major challenges of frequency dependent transmission line models is to enforce the stability of the time domain simulations.

Several passivity enforcement algorithms have been proposed [4–6]. Some of these methods [4,5] are based on perturbation of the fitted parameters and passivity is enforced as a solution to a constrained optimization problem. However, the derivation and implementation of such algorithms are complicated, as they require many matrix linearization and eigenvalue sensitivity calculations. Furthermore, these methods are typically valid for eliminating small passivity violations, which are commonly due to approximations in the linearization process. In addition, with these methods there is no guarantee that the convergence is always achieved, as it depends on several factors and for large transmission line systems with many conductors, these methods may require significant computation time (e.g. several minutes depending on the case).

Alternatively, passivity can be enforced analytically through Hamiltonian matrix [6]. This approach is widely applied to admittance-based realization of a frequency dependent component or network equivalent. The work in [7,8] extend this method to transmission lines. However, they are limited to modal domain models based on constant transformation matrices. Note that for underground cables and vertically asymmetrical transmission lines, the transformation matrix is frequency dependent. Again, the derivation and the implementation of this enforcement algorithm is tedious and requires significant effort. The computer memory and time requirements for the algorithm can be significantly high for large transmission line configurations with several conductors/cables.

Ref. [9] discusses a filter-based method to enforce passivity for a two-layer network equivalent. A passivity enforcement method for multi-conductor transmission lines via filters is proposed in [10]. However, a drawback of this method is that the corrected model eliminates the natural decoupling of the transmission line. In EMT-type programs, the natural decoupling of frequency dependent transmission line is a significant advantage as it divides the system into small sub-systems, which leads to faster simulations.

This paper proposes an improved passivity enforcement algorithm using passive filters for transmission line models in EMT-type software. An improved quality factor estimation for passive filters is introduced. Compared to [10], an advantage of the proposed method is that the natural de-coupling of the transmission line is also maintained. Additionally, the proposed method does not requ

## 3. PASSIVITY ENFORCEMENT FOR TRANSMISSION LINES VIA PASSIVE SHUNT FILTERS

### 3.1. Preliminaries

The fundamental concept behind the passivity enforcement by filters is that the eigenvalues of a matrix can be changed by modifying the diagonal elements of the matrix. If every diagonal element ($D_{ii}$) of the analyzing the eigenvalue characteristics as a function of frequency and by taking sufficient number of samples in combination of log and linear scales. The frequency range should cover the bandwidth of frequencies in time domain simulations [4].