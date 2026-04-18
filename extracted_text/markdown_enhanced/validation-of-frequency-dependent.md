# Validation of Frequency-Dependent Transmission Line Models
Bjørn Gustavsen, Senior Member, IEEE

The author is with SINTEF Energy Research, Trondheim N-7465, Norway (e-mail: bjorn.gustavsen@sintef.no).

**Abstract**—The accuracy of a transmission line model can be verified by comparing its response to that by an alternative method of indisputable accuracy. This paper shows a procedure for validation which is based on the inverse Fourier transform. Desired test responses are calculated in the frequency domain using an admittance representation of the line and its terminal conditions. Time-domain step responses are calculated using the inverse Fourier transform, with semianalytic integration between sample points to permit calculation at arbitrarily large time values. The required number of frequency samples is greatly reduced by adaptively calculating the samples while considering the frequency-domain behavior of the integrand. Responses from arbitrary excitations are calculated by superposition of weighted, time-delayed step responses. The accuracy of the approach is validated for an overhead line and a cable system by comparison with responses obtained by a phase-domain line model.

**Index Terms**—Electromagnetic transients, high-speed interconnects, power systems, transmission line modeling.

## I. INTRODUCTION

FREQUENCY-DEPENDENT transmission line models have, since the early 1970s, been developed for use in power system overvoltage studies [1]–[9], and more recently, also for the modeling of high-speed interconnects [10]. These models have found their use in many general simulation programs, such as ATP, EMTP, and EMTDC.

During the development of a new line model, it is necessary to perform time-domain tests so as to verify inaccuracies inherent to the model, and to reveal bugs in the implementation. The challenge of calculating sufficiently accurate test responses is becoming increasingly difficult as the accuracy of the transmission line models themselves keep improving. In principle, test responses can be calculated using a very accurate transmission line model as a reference (e.g., the universal line model (ULM) [7]). However, the ULM is a traveling-wave model just like the other line models and it, therefore, shares many of their properties. It is, therefore, safer to use a completely different approach so as to avoid that the reference model produces the same type of errors as the model to be tested.

Some of the earliest work on frequency-dependent transmission line modeling was based on the Laplace transform with the excitations and terminal conditions included in the frequency domain-solution [11]–[15]. In this approach, which in the papers is termed modified Fourier transform (MFT), the integration is carried out at a distance to the right of the imaginary axis. This shift gives an advantage over the Fourier transform in that the frequency responses become smoother, thus permitting usage of an equidistant frequency step and, thus, usage of the highly efficient fast Laplace transform.

However, usage of the MFT requires the capability of calculating frequency responses at complex frequencies. Realizing that not everyone has this capability (e.g., those relying on the output from EMTP’s line constants or cable constants routine), the present paper will instead present a procedure based on the Fourier transform. The usage of the Fourier transform now introduces several difficulties because poles lying close to the imaginary axis of integration cause a jagged behavior of the frequency response, thus making use of equidistant sampling difficult. As a practical remedy, the paper introduces a procedure for adaptive nonequidistant sample calculation which strongly reduces the required number of samples needed for resolving the frequency response. The time-domain response is calculated using semianalytical integration between sample points. This permits the time response to be calculated at arbitrary time points, including very long observation times. It is further shown how to generate frequency-domain step responses for voltages and currents related to arbitrary terminations. Time-domain responses for arbitrary excitations are calculated using superposition. The approach is demonstrated for an overhead line and for an underground cable system where the obtained test responses are compared against results obtained by a highly accurate phase-domain model (ULM), which has been incorporated in an EMTP-type simulation program. The same method for computation of frequency domain parameters is used for the two approaches (Fourier transform, ULM).

## II. CALCULATION OF FREQUENCY RESPONSES

### A. Frequency-Domain Model

With the usual assumption of plane-wave propagation, an -conductor homogenous transmission line can be described in the frequency domain by
$$ (1) $$
$$ (2) $$
where and are the series and shunt admittance matrices, respectively. The admittance matrix with respect to the line terminals can be formulated in terms of hyperbolic functions from the solution of the wave equation [13]. Hyperbolic functions for matrices are usually not available in programming languages, so these must be expressed in terms of exponential functions. Steps 1–3 below show a robust implementation based on diagonalization. Note tha

Fig. 1. Circuit for validation of three-phase line.

Fig. 2. Open-circuit test.