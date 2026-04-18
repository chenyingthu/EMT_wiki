# Passivity Enforcement for Transmission Line Models Based on the Method of Characteristics
**Bjørn Gustavsen, Senior Member, IEEE**

**Abstract**—The Universal Line Model (ULM) has been implemented in several EMT programs for simulation of electromagnetic transients. In some cases, instability problems have been encountered. This paper shows that the current approach for rational function approximation adopted in ULM can lead to large out-of-band passivity violations, thereby causing an unstable simulation. An approach is introduced which prevents the occurrence of large passivity violations. Low-frequency violations are avoided by adding an artificial shunt conductance to the diagonal elements of the shunt admittance matrix while high-frequency violations are avoided by introducing artificial attenuation using a low-pass filter. In addition, high-frequency asymptotic passivity is enforced for the characteristic admittance. Any remaining violations are removed by adding a second-order correction term to the model ports. The approach is shown to mitigate instabilities from a cable system transient simulation, without impairing the quality of the model.

**Index Terms**—Electromagnetic transients, instability, passivity, transmission line model, universal line model.

Manuscript received July 6, 2007; revised September 2, 2007. Current version published September 24, 2008. This work was supported by the Norwegian Research Council (PETROMAKS Programme) and by Deutsch, FMC Technologies, Framo, Norsk Hydro, Siemens, Statoil, Total, and Vetco Gray. Paper no. TPWRD-00380-2007.
The author is with SINTEF Energy Research, N-7465 Trondheim, Norway (e-mail: bjorn.gustavsen@sintef.no).
Digital Object Identifier 10.1109/TPWRD.2008.919034

## I. INTRODUCTION
FREQUENCY-DEPENDENT transmission line models are widely applied in electromagnetic transients programs. These models are usually based on the Method of Characteristics (traveling wave method) with rational approximation of the propagation function and the characteristic impedance, leading to recursive convolution in the time domain [1]. While the early line models were based on a constant transformation matrix and modes [1], [2], several new line models have been proposed that are based on a formulation in phase co-ordinates [3]–[9]. Since no assumption of a constant transformation matrix is made, more accurate results can in general be achieved.

One of the phase domain models, the so-called Universal Line Model (ULM) [8], [9], is based on obtaining poles and delays via mode fitting, while calculating the final residues in the phase domain. Although highly successful in most situations, some deficiencies have become apparent. Some cable cases have been encountered where mode fitting will not produce suitable poles and delays. This problem was overcome in [10] by introduction of trace fitting. A more serious problem is that the ULM sometimes gives an unstable simulation result.

This paper shows that the ULM formulation can easily lead to large out-of-band passivity violations and thus an unstable simulation. A practical approach is introduced which prevents the occurrence of out-of-band passivity violations, and a remedy is provided for removing any remaining in-band violations. Application to a cable case is shown to mitigate an unstable simulation.

In the examples, the calculation of per-unit-length cable parameters and the rational modeling is done using Matlab codes. The resulting model parameters are exported to the PSCAD simulation environment [11] and used within the existing ULM implementation (phase domain line).

## II. UNIVERSAL LINE MODEL
### A. Method of Characteristics in the Phase Domain
For a homogenous transmission line with ends and , the relation between voltage and current at end is in the frequency domain given by the matrix-vector relations
$$ \tag{1} $$
$$ \tag{2} $$
where indices and respectively denote incident and reflected wave. For a line of length , the matrices for surge admittance and propagation function are obtained from the series impedance and shunt admittance as
$$ \tag{3} $$
$$ \tag{4} $$

### B. Rational Fitting
In the Universal Line Model (ULM) [8] as implemented in PSCAD [9], the poles for are obtained by fitting the matrix trace (5) using vector fitting (VF) [12], followed by a final fitting of the residues and proportional term in the phase domain (6). The fitting can also be done by applying VF to the columns of as in the original formulation [8], giving a private pole set for each column
$$ \tag{5} $$
$$ \tag{6} $$

Poles and delays for the fitting of are obtained by fitting the modes of
$$ \tag{7} $$
Modes with nearly equal delays are lumped before doing the fitting. Finally, the residues are calculated by solving (8) with (known) poles and delays obtained from the modes
$$ \tag{8} $$

frequency dependent line models, it was found that this uncontrolled behavior near dc may lead to simulation instabilities [17]. As a practical remedy, it was proposed to insert an artificial shunt conductance to obtain a nonzero at dc, an approach that has been adopted by several EMT programs [18]. A recent discussion can be found in [19]. Values for the shunt conductance that can occur in actual overhead line systems are discussed in [20].
Adding a conductance to the diagonal elements of (14) causes to approach a nonzero value (15) while