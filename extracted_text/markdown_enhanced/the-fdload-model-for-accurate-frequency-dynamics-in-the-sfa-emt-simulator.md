# The fdLoad model for accurate frequency dynamics in the SFA-EMT simulator

Masoud Hajiakbari Fini $^a$, Andrea T.J. Martí $^b$, José R. Martí $^{a,*}$

$^a$ Department of Electrical and Computer Engineering, University of British Columbia, Vancouver, BC, V6T 1Z4, Canada  
$^b$ Department of Civil Engineering, University of British Columbia, Vancouver, BC, V6T 1Z4, Canada  

$^*$ Corresponding author. E-mail addresses: mhf@ece.ubc.ca (M.H. Fini), andrea.marti@ubc.ca (A.T.J. Martí), jrms@ece.ubc.ca (J.R. Martí).

**Keywords:** Accurate frequency swing solutions in low inertia systems, Frequency dependent load model (fdLoad), Shifted Frequency Analysis (SFA) modelling

**Abstract:** Due to the reduction in the system’s total mechanical inertia, frequency swing deviations increase with the penetration of inverter-based resources (IBR). For frequency swings, transient stability programs usually model the load as frequency-dependent using, for example, exponential load models. These programs usually use a phasor solution at 60 Hz for the AC network, and the frequency is estimated from the solution for the phase angles at previous and current time steps but is not explicitly included in the present time step solution. On the other hand, in Dommel’s EMT time domain solution, the frequency is implicitly included in the solution at all locations in the network, including the load busses. A full-system EMT solution, however, is expensive compared to a phasor solution. In this paper, the Shifted-Frequency Analysis method (SFA), which is a phasor solution with magnitude and phase angle discretized with the EMT method, is combined with a frequency-dependent load synthesis model to study the influence of the frequency dependence of the load in frequency swings. The IEEE-39-Bus system is used for tests of load-shedding conditions. The results show that using a frequency-dependent load model has an important influence on the maximum frequency deviations during the contingency.

## 1. Introduction

The transition from synchronous generation to inverter-based resources (IBR) has created challenges for traditional power system simulation software due to the wider swings caused by the decrease of system inertia. In particular, frequency swings during generation loss, load shedding, and faults can be larger than expected by frequency relays.

The SFA-EMT simulator [1] was developed to solve a phasor-domain electric circuit using Dommel’s EMT discretization techniques [2] applied to the magnitude and phase angle of the voltage and current phasors. (In this paper, whenever the generic term EMT is used, it refers to Dommel’s EMT discretization method of [2].) SFA-EMT can simulate any frequency in the system, but it is particularly efficient for frequency deviations around 60 Hz.

In conventional phasor-based software, frequency is estimated from the rate of change of the phase angles from the previous solution to the present solution (e.g., [3–6]). This approach does not use the current step frequency for frequency dependent loads and has difficulties at discontinuities, for example during load shedding.

In SFA-EMT, the phase angles are continuous variables, and the frequency at the present solution step is implicit in the solution. As a result, it is possible to model the frequency dependence of the loads using a frequency-dependent network synthesis branch, as in the frequency-dependent models of the EMT solutions (e.g., [7,8]).

For the SFA-EMT solution, discontinuities can be treated as in the EMT programs using, for example, CDA [9] or using the backward Euler rule instead of the trapezoidal rule for the entire simulation. Since in the SFA-EMT solution, the frequency is implicit in the solution, the system impedances or admittances are not constant at 60 Hz but are obtained at the correct frequency at every solution step.

This paper extends the accuracy of the SFA-EMT simulator of [1] for modelling frequency swings by developing a frequency-dependent load model (fdLoad) that synthesizes the load as a combination of constant $R$, $L$, and $C$ components (Fig. 3).

The fdLoad model follows the EMT frequency-dependent line models (e.g., [7]) that use a network synthesis to model impedances or admittances. The Vector Fitting procedure of [8] was chosen for this modelling because it can synthesize complicated frequency-dependent functions defined in a relatively narrow frequency band, as compared to Bode’s method of [7].

The IEEE-39-Bus system is used to test the fdLoad model during frequency swings during load-shedding situations with variable amounts of IBR penetration. These results are important for Under-frequency Load Shedding schemes (UFLS). The existing UFLS may be set to operate too early when the load’s frequency dependence is not considered.

## 2. SFA-EMT shifted frequency analysis simulation

The application of Dommel’s EMT solution methods to complex signals was discussed in [10]. The Shifted Frequency Analysis (SFA) algorithm to model synchronous machines was discussed in [11]. The SFA-EMT simulator to solve a general network for the time-dependent magnitude and phase angle of phasor voltages and currents using EMT discretization methods w

---
*This work was supported in part by the Natural Sciences and Engineering Research Council of Canada (NSERC).*