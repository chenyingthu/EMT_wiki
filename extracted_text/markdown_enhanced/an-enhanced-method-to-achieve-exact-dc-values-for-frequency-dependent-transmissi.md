# An Enhanced Method to Achieve Exact DC Values for Frequency-dependent Transmission lines
H.M.J. De Silva *, Z Liu
Manitoba Hydro International Ltd, Canada

**Keywords:** Dc correction, Electromagnetic transients, Rational function, Universal line model, Phase domain model

**Abstract:** This paper proposes an improved method to enhance the dc response of a frequency-dependent transmission line model used in EMT studies. A modification to the rational function approximation of propagation and characteristic admittance matrices of a transmission line is introduced to enforce exact dc values at 0 Hz. Furthermore, weighting factors are applied to improve accuracy at low frequencies. Finally, the order of the propagation function is reduced to decrease the computational effort.
The validity of the proposed approach is demonstrated using examples involving underground cables and overhead lines. First, the effect of dc correction is demonstrated by comparing transmission line frequency domain characteristics. In addition, time domain simulations via open and short circuit conditions show a more accurate simulation of HVDC transmission lines with the proposed method.

## 1. Introduction
HIGH Voltage direct current (HVDC) transmission lines are preferred to transmit power over long distances for the sake of lower cost compared to traditional ac transmission [2]. In addition, HVDC transmission lines can also be used to connect two unsynchronized networks and to integrate renewable energy resources such as wind into the main transmission grid. The transient simulations involving HVDC cable and overhead line models require accurate representation of a wide frequency range from dc to a few MHz.

The Universal Line Model (ULM) [1] is widely used in EMT transient studies including switching, lighting, and faults analysis, etc. The curve-fitting of transmission line propagation and characteristic admittance functions is required in frequency-dependent transmission line models such as ULM. This curve-fitting process is typically performed for frequencies from a few Hz to 1 MHz. Difficulties arise when trying to obtain accurate curve-fitting at very low frequencies with the traditional method [2-4]. These include (a) incorrect dc value in time domain simulations, (b) unstable simulations due to large residue/pole ratios (c) the presence of artificial overshooting in dc response (d) increased order of curve-fitted functions. To relieve these difficulties, numerous solutions have been proposed in the past by various researchers.

Reference [2] proposed a method to enforce exact dc value by modifying the functional form of rational function. However, for the propagation function, an optimization algorithm is necessary to eliminate errors at high frequencies. Such an algorithm increases complexity and there is a possibility of a non-convergence solution. Although this method guarantees the exact dc value, the curve-fitting accuracy at low frequencies may be poor. It is observed that this may lead to an artificial overshooting in some time domain simulations [3].

In [3], a two-stage fitting procedure is introduced to enhance fitting at low frequencies. First, frequency-dependent characteristics (such as propagation and characteristics admittance) at high frequency range are curve-fitted (e.g. 1 Hz to 1 MHz) and then the difference between actual and fitted curves is computed for the low frequency range (e.g. from 0.001 Hz to 1.0 Hz). The characteristics at the low frequency range are then approximated (curve-fitted) to enhance accuracy at low frequencies and to reduce the presence of large residue/pole ratios. Finally, high and low frequency curve-fitted functions are combined to represent the entire frequency range.

In [4], the frequency-dependent characteristics are curve-fitted for a wide frequency range from 1 mHz to 1 MHz. Additional low order fitting function is applied to compensate for the curve-fitting discrepancy for the propagation and characteristic admittance functions at low frequencies.

However, increased curve-fitting accuracy does not guarantee exact dc values, as the curve-fitting error at frequencies approaching dc is unavoidable. A slight deviation of curve-fitted characteristics can cause noticeable mismatch in dc response [1].

This paper introduces modified rational function formulas to enforce the exact dc value without additional constrained optimization as discussed in [2]. The following improvements are utilized to achieve the exact dc enforcement.
(a) Residue computation via dc enforcement.
(b) Use of weighing function to improve the accuracy at very low frequencies and to mitigate overshooting in time domain simulations.
(c) The rearrangement of the propagation function and order reduction at low frequency section are used to decrease the order

## 3. Proposed modified formulas to enforce exact dc value
Once the $Y_c(s)$ and $A(s)$ are expressed in rational form, (1) and (2) can be represented as EMT Norton equivalent circuits using recursive convolution technique [1].

### 3.1. Enforcing exact dc values
To enforce dc for $Y_c(s)$, the functional form described in [2] is used. The residue computation procedure of $Y_c(s)$ is modified to obtain the exact dc value. At 0 Hz, the fitted $Y_c(s)$ is set to its exact dc value ($Y_{c_{dc}}$) in (6). This dc value can be computed analytically [2].

$$Y_{c_{i,j}}(s = 0) = Y_{c_{dc_{i,j}}} = \sum c_q$$