## COMPUTATION OF THE PERIODIC STEADY STATE IN SYSTEMS WITH NONLINEAR COMPONENTS USING A HYBRID TIME AND FREQUENCY DOMAIN METHODOLOGY

**Adam Semlyen** and **Aurelio Medina**  
Department of Electrical and Computer Engineering  
University of Toronto  
Toronto, Ontario, Canada M5S 1A4

**Abstract** The basic principles of an efficient new methodology for the calculation of the non-sinusoidal periodic steady state in systems with nonlinear and time-varying components are described. All linear parts, including the network and part of the loads, are represented in the frequency domain, while nonlinear and time-varying components, mainly loads, are represented in the time domain. This hybrid procedure is iterative, with periodic, non-sinusoidal, bus voltages as inputs for both frequency domain solutions and time domain simulations: a current mismatch is calculated at each bus and used to update the voltages until convergence is reached. Thus the process, but not the solution, is decoupled for the individual harmonics. Its efficiency is enhanced by the use of Newton type algorithms for fast convergence to the periodic steady state in the time domain simulations. Potential applications of this methodology are in the computation of a Harmonic Power Flow and in the Steady State Initialization needed in the calculation of electromagnetic transients.

**Keywords:** Periodic steady state, Harmonic power flow, Initialization for transients, Hybrid solution, Decoupled solution, Newton's method.

## 1. INTRODUCTION

Nonlinear and time-varying elements are the main source of harmonics in power systems. With a periodic single frequency input, the output will in general contain harmonics of many frequencies. Thus, nonlinear elements (time-varying included) are responsible for having all harmonics coupled in the system. This phenomenon of harmonic coupling is explicitly represented in detailed a.c. models of power network components [1] and of their interaction [2]. Accordingly, a program for the calculation of the non-sinusoidal Periodic Steady State of the system (Harmonic Power Flow) may be of very high dimension [2-6].

The intrinsic harmonic coupling produced by a nonlinear element is itself nonlinear. Only by a linearization around a particular operating point is a linear relation between harmonic domain voltages and currents possible [1-2], [9] and it is of course accurate only in a close neighborhood of that point. Not only is the calculation of such a harmonic Norton equivalent computationally difficult but, for accurate results, it has to be iteratively updated. The computational burden is thus further increased in direct proportion with the size of the system and the number of harmonics represented. Nevertheless, improvements in computational efficiency can be achieved by the following actions:

(a) Replace the harmonic domain calculations for nonlinear elements by direct time domain computations followed by Fourier transforms.

(b) Decouple the harmonics but recover the accuracy of the coupling by an iterative process.

Reference [7] has presented results along the ideas outlined above. There the iterative procedure consists of injecting harmonic current phasors into the network and using the resultant voltages, converted to the time domain, as inputs to a nonlinear element yielding a periodic current as output, with all the required harmonic components. This is a fixed point (successive replacement) iteration [8]. The convergence of the process may however be very slow, first, because the network impedance increases with frequency and resonance phenomena may occur [9] and, second, because the time domain simulation for the load must reach the periodic steady state condition of a limit cycle, a process that can take excessive time in the case of lightly damped circuits.

Therefore, the present paper incorporates the following features that assure a very efficient overall solution (see Figure 1):

(1) Fundamentally, frequency domain methods are used for the linear parts where they are computationally most efficient and intrinsically accurate (as in the case of transmission lines with distributed, frequency dependent parameters); and time domain simulation is used for the nonlinear parts (normally loads) where it is the only natural approach.

(2) The iterative process is not cyclical in the fixed point iteration sense of [7]. Instead, it is based on the calculation of a current mismatch $\Delta I_h$, for all harmonics, followed by a voltage update $\Delta V_h$. The mismatch computation is accurate: for the linear part it obtains $I_h = Y_h V_h$ for all harmonics $h$, and for each load it performs a time domain simulation to obtain the periodic steady state solution $i(t)$, with $v(t)$ as input. The mismatch vector $\Delta I_h$ (comprising all load buses) is then used with an appropriate iteration matrix $G$, equal or close to $Y_h$, to calculate the update increment $\Delta V_h$ from $G \Delta V_h = \Delta I_h$. This process always converges.

(3) The time domain simulation is accelerated by noting that the dynamics of cycles in the neighborhood of a limit cycle is almost linear [11], so that the intercepts with a Poincaré plane can be used to extrapolate to the limit cycle by Newton's Method, possibly with numerical differentiation. The latter has the advantage that it can be applied to nondifferentiable nonlinear load characteristics.

The above fundamental principles for the calculation of the non-sinusoidal Periodic Steady State in a system with both linear and nonlinear components are described and validated in this paper. They can be applied to the development of a full-fledged, three-phase Harmonic Power Flow Program or for the particular application of Steady State Initialization needed in an Electro-Magnetic Transients Program (EMTP). It is beyond the objectives of this paper to deal with the details of either application.