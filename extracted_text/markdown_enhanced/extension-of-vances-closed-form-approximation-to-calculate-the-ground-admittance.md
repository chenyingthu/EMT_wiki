## Extension of Vance’s closed-form approximation to calculate the ground admittance of multiconductor underground cable systems

Naiara Duarte^a, *, Alberto De Conti^b, Rafael Alipio^c  
^a Graduate Program of Electrical Engineering (PPGEE), Universidade Federal de Minas Gerais (UFMG), Belo Horizonte, Brazil  
^b Department of Electrical Engineering, Universidade Federal de Minas Gerais (UFMG), Belo Horizonte, Brazil  
^c Department of Electrical Engineering of Federal Center of Technological Education (CEFET-MG), Belo Horizonte, Minas Gerais, Brazil  

* Corresponding author.  
E-mail addresses: naiara.duarte@gmail.com (N. Duarte), conti@cpdee.ufmg.br (A. De Conti), rafael.alipio@cefetmg.br (R. Alipio).

**Keywords:** Underground cables, Ground admittance, Ground-return impedance, Electromagnetic transients, Power cable modeling

**Abstract:** In this paper, Vance’s closed-form approximation for the ground admittance of a single underground cable is extended to represent three-phase underground cable systems. The proposed methodology considers Sunde’s expression for the ground-return impedance calculation. The accuracy of the proposed extension is investigated taking as reference the generalized formulas of Xue et al. considering frequency-dependent soil parameters according to the Alipio-Visacro model. It is shown that the agreement between the approximate and generalized formulations is improved as the frequency increases. More importantly, it is shown that both methodologies lead to transient waveforms in good agreement for different types of excitation, different values of soil resistivity, and usual underground cable system configurations.

## 1. Introduction

The application of underground cables in electrical power systems requires an accurate representation of cable parameters considering the influence of a finitely-conducting ground. Much attention has been given to the ground-return impedance calculation [1], but recent studies show that the ground admittance plays a significant role in the transient analysis of underground cable systems in case of high-resistivity soils and high-frequency phenomena [1-5].

Early efforts to derive correction terms to account for the effect of a finitely conducting ground on underground cables are reported in [6-8]. More recently, Papadopoulos et al. [3], Magalhães et al. [9], and Xue et al. [10] proposed expressions for calculating the ground impedance and admittance of underground cables, each derived under different approximations. Their application requires the evaluation of infinite integrals that may present singularities and/or slow convergence. To overcome this problem, logarithmic approximations for the ground admittance and impedance of underground cables were proposed in [11]. However, these approximate expressions were derived assuming the air-ground interface as the reference point for calculating the cable voltages, which limits their application. The above difficulties may explain why the ground admittance is completely neglected in popular electromagnetic transient (EMT) simulation tools, which restricts the application of such tools to the simulation of low-frequency transients in cable systems buried in low-resistivity soils.

An alternative to the solution of the complex integrals required for calculating the ground admittance of a single underground cable is the use of Vance’s expression $Y_g \approx \gamma_g^2 Z_g^{-1}$ [8], where $Y_g$ is the ground admittance, $Z_g$ is the ground-return impedance, and $\gamma_g$ is the propagation constant of the soil. This expression was later recommended in [12] and [1] for including the ground admittance in the modeling of a single overhead wire or a single underground cable, respectively. In [4], it was used in the simulation of lightning overvoltages on an underground conductor considering or not the presence of an insulating layer, leading to a relatively good agreement with a rigorous full-wave model based on the finite-difference time-domain (FDTD) method. In [13], this simplified expression was used to investigate the influence of frequency-dependent soil parameters on transient voltages on an underground cable. In none of the cases, however, it was investigated whether Vance’s expression could be used to simulate transients on multiconductor cable systems.

In this paper, an extension of Vance’s formula is proposed to calculate the ground admittance of trefoil, vertical and flat three-phase cable systems considering different types of excitations and different values of soil resistivity. The validity of the proposed extension is investigated taking as reference results obtained with the generalized ground-return impedance and ground admittance formulas derived by Xue et al. [10] considering frequency-dependent soil parameters using Alipio-Visacro model [14].

This paper is organized as follows. Section II presents modeling details. Frequency- and time-domain analyses are presented in Sections III and IV, respectively. A discussion is presented in Section V, followed by conclusions in Section VI.

## 2. Modeling

$1.26 \times \sigma^{-0.73}$, where $\varepsilon_0$ is the vacuum permittivity.

The per-unit-length impedance $Z$ and admittance $Y$ matrices of an underground cable system are given by

$$Z = Z_i + Z_e + Z_g \tag{3}$$

$$Y = (Y_e^{-1} + Y_g^{-1})^{-1} \tag{4}$$

The impedance given by (3) is the sum of the internal impedance $Z_i$