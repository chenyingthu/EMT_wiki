## SUPPRESSION OF NUMERICAL OSCILLATIONS IN THE EMTP

**Jose R. Marti**, Member, IEEE  
The University of British Columbia, Vancouver, B.C., Canada  

**Jiming Lin**, Member, IEEE  
Electric Power Research Institute, Beijing, China  

**Abstract** - The integration scheme in the Electromagnetic Transients Program (EMTP) has been modified to solve the problem of sustained numerical oscillations that can occur when the trapezoidal rule has to act as a differentiator. These oscillations appear, for instance, on the voltage across an inductance after current interruption. The technique presented in this paper prevents these oscillations by providing critical damping of the discontinuity within one $\Delta t$ of the simulation. The critical damping adjustment (CDA) is achieved by means of two $\Delta t/2$ integration steps using the backward Euler rule. With the CDA scheme the trapezoidal rule can still be used throughout the entire simulation without the problem at discontinuities. The effectiveness of the new scheme is illustrated with simulation results. **Keywords** -- discrete-time systems, numerical oscillations, integration rules, EMTP solution.

The major disadvantage of adding artificial damping either through the integration rule or external resistances, is that the rest of the normal system response is distorted by the phase errors introduced by the damping.

Other schemes have been proposed that try to control their irregular oscillations locally, without affecting the rest of the simulation (e.g., [2]). These schemes are based on readjustments of initial conditions and interpolations. These techniques, however, are relatively complicated to implement for a general class of network components.

The critical damping adjustment (CDA) procedure presented in this paper belongs to this last group in the sense that it eliminates the numerical oscillations locally. The main difference, however, is that it is not based on interpolation or re-initialization, but on the property of the backward Euler rule to provide total damping of the overshoot at the discontinuity in exactly two integration steps (critical damping).

Due to its simplicity, the modifications required to implement the CDA procedure are very straightforward, not only for simple elements like inductances and capacitances, but also for more complicated models like frequency dependent transmission lines and non-linear elements. The CDA procedure has been implemented and tested in the UBC version of the EMTP with a minimum of modifications to the overall solution scheme. It is also currently being implemented in the larger production code of the DCG/EPRI EMTP.

This paper explains the reasons for supporting the continued use of the trapezoidal rule as the basic integration rule in the EMTP and how to solve the problem of sustained numerical oscillations at discontinuities with the new critical damping adjustment scheme.

## 1 INTRODUCTION

One important factor for the widespread use of the electromagnetic transients program EMTP [1] has probably been its choice of integration scheme. The trapezoidal rule is used in the EMTP to convert the differential equations of the network components into simple algebraic relationships involving voltage, current, and known past values.

The accuracy of a discrete-system solution depends on the step size $\Delta t$ and on the integration rule. The step size determines the maximum frequencies that can be simulated, and the integration rule determines the distortion at different frequencies. The maximum frequency that can be simulated is independent of the integration rule and is determined by the sampling rate. This is the Nyquist frequency given by $f_N = 1/(2\Delta t)$. The distortion introduced by the integration rule gets worse as we approach the Nyquist frequency.

As it is shown in this paper, the trapezoidal rule has very good characteristics in terms of low distortion and numerical stability. Moreover, the trapezoidal rule is A-stable, which means that run-off instability cannot occur. For some types of simulations, however, the rule may have to work as a pure differentiator, e.g., voltage on an inductance after current interruption, or current in a capacitance after a voltage is switched on. Under these conditions, sustained (though bounded) numerical oscillations occur. This problem has been reported in [2], [3], and [4]. One suggested solution has been to add damping to the system in order to force the oscillations to decay. Damping can be provided by the integration rule itself, e.g., with backward Euler, Gear, or

## 2 SOLUTION SCHEME IN THE EMTP

The solution scheme in the EMTP [1] is based on the discretisation of first order differential equations by means of the trapezoidal rule of integration. For instance, the differential equation for an inductance

$$u(t) = L \frac{di(t)}{dt}$$

becomes the difference equation