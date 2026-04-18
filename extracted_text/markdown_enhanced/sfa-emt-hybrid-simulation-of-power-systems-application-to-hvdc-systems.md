# SFA-EMT hybrid simulation of power systems: Application to HVDC systems

Javier O. Tarazona $^a$, Andrea T.J. Martí $^b$, José R. Martí $^{c,*}$

$^a$ PSC North America, 155-4299 Canada Way, Burnaby, BC V5G4Y2, Canada
$^b$ Department of Civil Engineering, University of British Columbia, Vancouver, BC V6T 1Z4, Canada
$^c$ Department of Electrical and Computer Engineering, University of British Columbia, Vancouver, BC V6T 1Z4, Canada

* Corresponding author. E-mail addresses: jotarazona@gmail.com (J.O. Tarazona), andrea.marti@ubc.ca (A.T.J. Martí), jrms@ece.ubc.ca (J.R. Martí).
This work was supported in part by The Natural Sciences and Engineering Research Council of Canada (NSERC).

**Keywords:** Electromagnetic transients (EMT), Hybrid simulation, Multirate simulation, Power electronic subsystems, Shifted frequency analysis (SFA)

**Abstract:** This paper presents the application of a novel hybrid multirate protocol to interface a Shifted Frequency Analysis (SFA) solution with an Electromagnetic Transients (EMT) solution. Using the Multi Area Thévenin Equivalent (MATE) framework, the protocol enables the direct interfacing of SFA and EMT solutions without time step delays, iterations, or the use of transmission lines to decouple the solutions. The protocol adds a parallel EMT solution to track both the real and imaginary parts of the EMT solution. This allows for a direct interface to the complex-number SFA solution. The proposed hybrid approach allows for large time steps in the SFA solution and does not require the time steps of the SFA and EMT systems to be multiples of each other. The protocol has been previously validated in a transient stability study, and it is applied in this paper to power electronics devices in the EMT subsystem using a modified CIGRE HVDC benchmark system. The use of SFA and the multirate nature of the solution offers significant computational savings for large power systems compared to an EMT-only solution.

## 1. Introduction

THE increased penetration of inverter-based resources (IBRs) is weakening the system’s inertia and increasing the effect of system perturbations [1]. Since the IBRs require small discretization steps, one option to study these systems is to use an electromagnetic transients (EMT) type of modelling for the entire system. However, given the size and extension of modern interconnected power systems, this approach becomes computationally expensive. A recent approach [2] uses the Multi Area Thévenin Equivalent (MATE) concept [22] to create subsystems with different discretization step sizes.

For transient stability studies [3], a common approach has been to interface a conventional phasor solution of the AC system with an EMT solution of the IBR systems. This approach has the problem of introducing one time-step delay between the transient stability solution and the EMT solution [4–6]. This delay can lead to errors in the multirate solution. The hybrid simulators presented in [7] and [8] use interfacing protocols that iterate between the transient stability TS solvers and the EMT solvers to avoid the one-time-step delay in the multirate solution at the expense of additional iteration time.

The Shifted Frequency Analysis (SFA) method for transient stability studies [15] uses EMT discretization to find equivalent discrete-time circuit branches to replace the conventional impedance and admittance branches of transient stability programs to obtain a solution where the magnitude and phase angle of the voltage and current phasors are functions of time. Other approaches to having a time-dependent magnitude and phase angle phasor are Dynamic Phasor solutions [10, 11]; these approaches are based on Fourier decomposition instead of the EMT discretization approach. The SFA-EMT approach is particularly efficient in terms of time step sizes when the frequency deviations from 60 Hz are small. For larger deviations, the method is similar in efficiency to plain EMT solutions. Recent studies [12–14] show that SFA delivers better accuracy than a transient stability simulator for both classic and low inertia systems.

In general, previous approaches to interface an SFA solution of the AC grid with an EMT solution of IBRs have used transmission lines to decouple the two subsystems and, therefore, the maximum time step that could be used in the SFA solution was limited by the travelling time of the line.

A hybrid SFA-EMT multirate simulator is presented in [16] where good solutions are obtained without transmission lines interfacing. In [16], the proposed protocol was validated for a transient stability study on the IEEE 39-bus test system. In that work we did not consider the details of power electronics subsystems. In the present paper, this SFA-EMT protocol is applied to a modified version of the CIGRE HVDC benchmark system [18] with the details of the power electronic devices simulated.

The rest of the paper is structured as follows: in Part II, a brief review of the SFA technique is presented. In Part III, some aspects of the MATE solution framework are discussed. The interaction protocol

signal is also a bandpass signal centred on $\omega_0$. From (6) and applying the properties of Fourier transform, it follows that the time-dependent phasor (TDP), or the transformed signal, has its frequency spectrum centred at zero frequency and is, therefore, a low-pass signal, which changes much less rapidly than the analytic signal. Hence, larger time steps can be used to capture this signal in the simulation. The above transformation is the one used for Shifted Frequency Analysis (SFA) [9], which changes much less rapidly than the analytic signal.