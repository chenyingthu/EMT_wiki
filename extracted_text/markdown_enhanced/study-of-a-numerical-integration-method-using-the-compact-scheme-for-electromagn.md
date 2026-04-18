# Study of a numerical integration method using the compact scheme for electromagnetic transient simulations

Yohei Tanaka a, *, Yoshihiro Baba b  
a Grid and Communication Technology Division, Grid Innovation Research Laboratory, Central Research Institute of Electric Power Industry, Kanagawa 240-0196, Japan  
b Graduate School of Science and Engineering, Doshisha University, Kyotanabe, Kyoto 610-0394, Japan  

**Keywords:** Circuit equation, Compact scheme, Electromagnetic Transient analysis, Integration method, SPARSE Tableau approach, Stability  

**Abstract:** This paper proposes a one-stage and oscillation free numerical integration method using the compact scheme for electromagnetic transient simulations. Since the compact scheme becomes L-stable at a moment when a circuit suddenly changes to a stiff system, the method is capable of suppressing the spurious numerical oscillations. Moreover, the compact scheme, which is a one-stage method, does not produce spurious spikes due to nonlinear elements. The compact scheme is compared with the trapezoidal method, the two-stage diagonally implicit Runge-Kutta (2S-DIRK) and the trapezoidal method with the second order backward difference formula (TR-BDF2). It follows from the comparison that the compact scheme does not produce the spurious numerical oscillations and spikes.

## 1. Introduction

Electromagnetic transients (EMT) simulations have been used for the studies of abnormal voltage/current, power quality, and so on. Recently, EMT simulations have become increasingly important in the dynamic analysis of power systems including many fast-speed-switching power electronics devices [1,2].

In the EMT simulation, a numerical integration method is required to obtain the time solution of a circuit system including inductors and capacitors. The trapezoidal method has been used for many EMT simulation programs such as electromagnetic transients analysis program (EMTP) [1–3] and PSCAD [4], since the method has a second order accuracy and is A-stable in spite of its simple calculation principle. However, the trapezoidal method produces spurious numerical oscillations due to sudden changes of inductor currents or capacitor voltages.

To solve this problem or to eliminate spurious oscillations, the critical damping adjustment (CDA) method has been introduced [5,6]. In the CDA, the backward Euler method is employed at a moment of sudden changes of inductor currents or capacitor voltages. Since the backward Euler method is L-stable, numerical oscillation is not sustained. PSCAD uses the interpolation method [4] to suppress the numerical oscillations. In the method, the linear interpolation is used for determining the time when the current or voltage is suddenly changed. Conventional and latest methods for suppressing numerical oscillations are reviewed and discussed in [2]. However, since the detection of a sudden change of currents or voltages not always feasible, it is not guaranteed that the numerical oscillation is suppressed with CDA or the interpolation method [7,8].

To cope with the problem of these techniques, the application of the two-stage diagonally implicit Runge-Kutta (2S-DIRK) or the trapezoidal method with the second order backward difference formula (TR-BDF2) to EMT simulations have been proposed [7,9]. The 2S-DIRK and TR-BDF2 have a second-order accuracy and are L-stable. Unlike the trapezoidal method, it is mathematically guaranteed that the 2S-DIRK and TR-BDF2 never produce spurious numerical oscillations. Thus, no detection of the events which can lead to numerical oscillations is required. However, since the 2S-DIRK and TR-BDF2 are two-stage methods, which calculate a solution at the present time step from the values obtained in the previous and intermediate steps, spurious spikes can be generated because of nonlinear elements contained in a circuit system [7]. Thus, a one-stage integration method, which can suppress the numerical oscillations, is desired.

This paper proposes a one-stage and oscillation free numerical integration method using the compact scheme [10] for EMT simulations. At first, the fundamental of the compact scheme is described, and the formulas of the compact scheme of inductors and capacitors for both linear and nonlinear cases are derived. Then, it is shown that the compact scheme can suppress numerical oscillations due to switching events, sudden changes of voltage and current source values and changes of the operating points of nonlinear components. Finally, some simulation cases computed using the compact scheme are compared with those computed using CDA, the trapezoidal method, 2S-DIRK and TR-BDF2.

## 2. Compact scheme

### 2.1. Integration of a differential equation by compact scheme

The compact scheme proposed by Lele [10] is a finite difference method. The scheme is characterized by handling not only discretized function values but also their derivatives. The compact scheme has been frequently used in numerical calculations for solving Navier-Stokes

*Fig. 1. Equivalent circuit of a linear or a nonlinear inductor based on the approximation of the compact scheme.*

current. GL, GLT and JL are given by
h