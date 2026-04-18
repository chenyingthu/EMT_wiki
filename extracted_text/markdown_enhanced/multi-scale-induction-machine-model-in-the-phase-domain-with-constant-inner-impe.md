## Multi-scale Induction Machine Model in the Phase Domain with Constant Inner Impedance
Yue Xia and Kai Strunz

### Abstract
An efficient and accurate multi-scale induction machine model for simulating diverse transients in power systems is developed and validated. Voltages, currents, and flux linkages are described through analytic signals that consist of real in-phase and imaginary quadrature components, covering only positive frequencies of the Fourier spectrum. The stator is modeled in the $abc$ phase coordinates of an arbitrary reference frame whose rotating speed is adjusted by a simulation parameter called shift frequency. When the reference frame is stationary at a zero shift frequency, then the model processes instantaneous signals to yield natural waveforms. When the reference frame is set to rotate at the synchronous frequency of the electric network, then the Fourier spectra of the analytic signals are shifted by this synchronous frequency to become dynamic phasors that allow for efficient envelope tracking. The shift frequency can be adapted during simulation. For any rotor position and independent of the variation of the magnetizing inductances with saturation, the induction machine model appears as a Norton current source with constant inner admittance in the $abc$ phase domain to support the integration with simulators that represent the electric network in the $abc$ phase domain. The analysis of test cases covering diverse transients substantiates the claims made in terms of accuracy and efficiency across different time scales.

**Index Terms**—Dynamic phasor, electromagnetic transients, electromechanical transients, induction machine, modeling, multi-scale, power system simulation, reference frame, shift frequency.

### Nomenclature
Throughout this paper, an underscore is used to mark a quantity existing of real and imaginary parts, the symbol “$\sim$” indicates predicted quantities.

| Symbol | Description |
|---|---|
| $L_{rs}(\theta_r)$, $L_{sr}(\theta_r)$ | Matrices of mutual inductances between stator and rotor windings. |
| $L_{ss}$, $L_{rr}$ | Stator and rotor constant inductance matrices. |
| $p$ | Number of poles. |
| $R_{eq}$ | Equivalent resistance matrix. |
| $R_s$, $R_r$ | Stator and rotor diagonal constant resistance matrices. |
| $T_m$, $T_e$ | Mechanical and electromagnetic torques. |
| $v_{abcr}$, $\underline{v}_{abcr}$ | Rotor voltages. |
| $v_{abcs}$, $\underline{v}_{abcs}$ | Stator voltages. |
| $\alpha$ | Ratio of present to previous time-step sizes. |
| $\lambda_{abcr}$, $\underline{\lambda}_{abcr}$ | Rotor flux linkages. |
| $\lambda_{abcs}$, $\underline{\lambda}_{abcs}$ | Stator flux linkages. |
| $\theta_r$ | Electrical rotor position. |
| $\tilde{\theta}_r$ | Predicted electrical rotor position. |
| $\tau$ | Time-step size. |
| $\omega_r$ | Rotor electrical angular velocity. |
| $e_{abcsh}$, $\underline{e}_{abcsh}$, $e_{abcrh}$, $\underline{e}_{abcrh}$ | Stator and rotor voltage history terms. |
| $e_{dq0rh}$, $\underline{e}_{dq0rh}$ | Rotor voltage history term in rotor reference frame. |
| $e_{oc}$ | Stator open circuit voltage. |
| $f_c$ | Carrier frequency. |
| $f_{ref}$ | Shift frequency. |
| $G_{eq}$ | Equivalent conductance matrix. |
| $i_{abcr}$, $\underline{i}_{abcr}$ | Rotor currents. |
| $i_{abcs}$, $\underline{i}_{abcs}$ | Stator currents. |
| $\tilde{i}_{abcs}$ | Predicted stator currents. |
| $i_{dr}$, $i_{qr}$ | Direct and quadrature components of rotor currents. |
| $i_{ds}$, $i_{qs}$ | Direct and quadrature components of stator currents. |

## I. INTRODUCTION
Algorithms for the simulation of transients in electric power systems are commonly classified into two categories. For the simulation of electromagnetic transients, the algorithms of electromagnetic transients programs (EMTP) process instantaneous signals to track natural waveforms [1]–[3]. For the simulation of electromechanical transients, algorithms that process dynamic phasor signals to track envelope waveforms are popular [4], [5]. If it is of interest to study both electromagnetic and electromechanical transients within the same study, then the concept of frequency-adaptive simulation of transients (FAST) [6]–[10] offers an efficient multi-scale simulation. The virtues of dynamic phasors and EMTP-type modeling techniques are combined by representing all ac quantities through analytic signals and by introducing a variable simulation parameter called the shift frequency. When the shift frequency is set equal to the ac carrier frequency of either 50 Hz or 60 Hz, the ac carriers are eliminated and analytic signals are transformed into dynamic phasors. With