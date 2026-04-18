# Assessment of dynamic phasor extraction methods for power system co-simulation applications☆
Janesh Rupasinghe $^a$, Shaahin Filizadeh $^{*,a}$, Kai Strunz $^b$
$^a$ Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, Canada
$^b$ Technische Universität Berlin, Berlin, Germany

**Keywords:** Base-frequency dynamic phasors, Generalized averaging, Shifted frequency analysis, Time-varying phasors

**Abstract:** The paper examines a number of methods for extracting dynamic phasors from samples of natural waveforms that are generated using electromagnetic transient (EMT) simulators. It delves into the theory underlying each phasor extraction method and the numerical routines used for their implementation. The paper performs an in-depth analysis of the properties of the extracted phasors for general power system signals that may include electromechanical oscillations, dc and harmonic components, imbalances, and arbitrary transients. Simulation results are presented to demonstrate any limitations of these methods and to assess the resulting harmonic spectra of the phasors. An EMT-dynamic phasor co-simulation example is also included, in which various phasor extraction methods are implemented. The paper’s findings are essential in selecting and implementing phasor extraction methods used in co-simulations of large power systems using EMT and dynamic phasors solvers.

☆ This work was supported in part by Mitacs, Manitoba HVDC Research Center, and Natural Sciences and Engineering Research Council (NSERC) of Canada. Paper submitted to the International Conference on Power Systems Transients (IPST2021) in Belo Horizonte, Brazil June 6–10, 2021.
* Corresponding author.
E-mail addresses: rupasira@myumanitoba.ca (J. Rupasinghe), shaahin.filizadeh@umanitoba.ca (S. Filizadeh), kai.strunz@tu-berlin.de (K. Strunz).
https://doi.org/10.1016/j.epsr.2021.107319
Received 30 November 2020; Received in revised form 23 February 2021; Accepted 23 April 2021
Available online 12 May 2021

## 1. Introduction
Assessment of transients is vital for design and operation of a power system. The study of transients relies chiefly on simulation tools, such as electromagnetic transient (EMT) and transient stability (TS) simulators. In the analysis of slow transients, conventional phasors have been used to represent the network dynamics based upon the quasi-steady state assumption [1]. The uptake of fast-acting systems such as HVDC, FACTS, and converter-tied distribution generation, has resulted in transients with a wider frequency spectrum for which quasi-steady state assumptions are no longer valid. Although EMT-type simulators [2,3] are able to provide detailed representations of wide-band transients, they are computationally inefficient for large system studies.

The notion of a dynamic phasor is an alternative to the quasi-stationary phasors and improves the bandwidth of phasor-type transient simulations [4–6]. A dynamic phasor provides low-pass, frequency-domain representations of a band-pass, time-domain, natural signal. As a result, dynamic phasors substantially reduce the computational burden of discrete-time transient simulations by allowing sampling at a lower rate while retaining accuracy. In recent years, co-simulations using upon EMT and phasor-type solvers has been shown to be a viable solution for accurate, computationally efficient modeling and simulation of large networks.

Conversion of signals from time-domain to dynamic phasors is a necessary step in interfacing co-simulation solvers [7–12]. This task involves creating a phasor, or a series of phasors if harmonics are included, to represent a natural waveform or a subset of its harmonics using instantaneous time-domain samples of the natural waveform. Several methods to perform this task are available. This paper provides an in-depth look into their underlying principles and studies the properties of the markedly different phasors they extract.

## 2. Steady-State phasor representation
All currents and voltages in an AC linear circuit in steady state are sinusoidal, and can be characterized by their magnitudes and phase angles on a common frequency equal to the frequency of the excitation. The aim of phasor analysis is to gain computational convenience and efficiency [13].

Consider a time-domain sinusoid $x(t)$ with a frequency of $\omega_0$, magnitude of $A$, and phase angle of $\delta$ as follows.
$$x(t) = \sqrt{2}A\cos(\omega_0 t + \delta) \quad (1)$$
Using Euler’s identity, one can represent this signal as
$$x(t) = \sqrt{2}\text{Re}\left\{Ae^{j(\omega_0 t+\delta)}\right\} = \sqrt{2}\text{Re}\left\{\vec{X} e^{j\omega_0 t}\right\} \quad (2)$$
where, $\vec{X} = Ae^{j\delta}$ is a time-invariant complex quantity and is called the “phasor” corresponding to $x(t)$. One of the main benefits that phasors offer is that the time-domain differential equations that describe the behaviour of elements such as inductors and capacitors become algebraic equations in the phasor domain. This is due to the following
$$P\left(x(t)\right) = \frac{1}{\sqrt{3}} \begin{pmatrix} 1 & j & 0 \end{pmatrix} B^{-1}(t) x(t) \quad (8)$$
Using (4), (7), and (8) it is readily seen that
$$P\left(x(t)\right) = \vec{X}(t) = A(t)e^{j\delta(t)} \quad (9)$$
The phasor transformation in (8) takes balanced three-phase quantities, and decomposes them into symmetrical components to represent them as time-varying complex values. When the three-phase system is unbalanced, the transformation produces a non-