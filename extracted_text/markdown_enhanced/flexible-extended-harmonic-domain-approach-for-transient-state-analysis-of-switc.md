# Flexible extended harmonic domain approach for transient state analysis of switched systems

Uriel Vargas $^{a,*}$, Abner Ramirez $^{a}$, George Cristian Lazaroiu $^{b}$

$^{a}$ Electrical Engineering Department, CINVESTAV Guadalajara, Guadalajara, Mexico
$^{b}$ Department of Power Systems, University POLITEHNICA of Bucharest, Splaiul Independentei 313, 060042 Bucharest, Romania

*Corresponding author.
E-mail addresses: uvargas@gdl.cinvestav.mx (U. Vargas), abner.ramirez@cinvestav.mx (A. Ramirez), cristian.lazaroiu@upb.ro (G.C. Lazaroiu).

## Abstract
A mature mathematical technique to model power systems, aimed at computation of harmonics dynamics in a step-by-step fashion, is the extended harmonic domain (EHD). The EHD is capable of accounting for an arbitrary number of linearly-spaced sequentially-numbered harmonics; however, the dimensions of an EHD-based model are prone to explode if a large number of harmonics are considered. This fact makes computationally impossible the harmonics dynamics study when high-frequencies, inherent of electronic devices, are involved.

This paper presents a flexible extended harmonic domain (FEHD) approach that permits to include an arbitrary number of (non-sequential) harmonics in any state variable of the system. The reasoning to use distinct harmonic content for each state variable is that in a general network (especially those involving alternative energy sources), state-variables exhibit distinct harmonic content. Such different contents mainly depend on the network topology, e.g., switched devices involved, filter arrangements utilized, etc.

As shown in the paper, the proposed FEHD approach is able to provide reduced-order EHD models including high-frequency ripple information; thus, leading to computational savings while keeping accuracy compared to traditional EHD-based models and averaged-value models. A case study, involving a three-phase photovoltaic system in closed-loop operation, is presented to validate the proposed methodology. The results provided by the proposed methodology are verified with those given by the power system computer-aided design/electromagnetic transients including DC (PSCAD/EMTDC) simulation tool.

**Keywords:** Harmonic domain, Photovoltaic systems, Power quality, Reduced-order model

## 1. Introduction
Power electronic converters (PECs) have become an integral part of electrical distribution networks, especially in the distributed generation area.

Inclusion of PECs in power electrical networks conveys both positive and negative impacts into quality of power [1–3]. Analysis of harmonic dynamics in switched networks plays a major role to understand power quality phenomena. Besides harmonic distortion, harmonics dynamics permit to study potential risks of harmonic resonance, mechanical vibration in transformers, flickering, among others [1–3].

There are multiple publications on the analysis of PECs at fundamental power frequency. In those publications, converters are simplified and represented via controllable voltage sources at fundamental frequency. This consideration does not allow a detailed harmonic study [4]. On the other hand, there are few studies focusing on power quality assessment in switched networks, having as basis electromagnetic transient (EMT) software tools, e.g., [5,6]; however, those studies require a post-processing routine based on the windowed fast Fourier transform (WFFT) to obtain the dynamics of harmonic frequencies. In Ref. [7], a power quality assessment study, based on steady-state, is carried out from experimental data.

Traditionally, switched networks are simulated via time-domain (TD) techniques; nevertheless, as consequence of switching phenomena, very small time-steps have to be employed leading to both large simulation times and excessive computational resources. This drawback has been alleviated by employing generalized averaged-value models (GAVMs) at cost of inability of showing ripple information [8]. Extended harmonic domain (EHD) models provide and alternative method for harmonic transient simulations, readily providing harmonics dynamics in a step-by-step fashion [9].

EHD has been employed to model different electrical and electronic systems including photovoltaic (PV) and wind generation systems [10–19], and to obtain steady-state solutions in a single matrix/vector operation [20–32]. However, as consequence of high-frequencies, inherent of PWM schemes, EHD models present the issue of large dimensions. For example, a scalar instantaneous variable corresponds in the EHD to a $2h + 1$ (being

The EHD modeling technique has become a mature power system simulation approach where harmonics dynamics are readily available in a step-by-step fashion [9–19]. Basically, the EHD technique transforms the LTP system Eq. (1) into a linear time-invariant (LTI) system as shown in Eq. (2).

$$
\dot{x}(t) = a(t)x(t) + b(t)u(t) \qquad \dot{X}(t) + NX(t) = AX(t) + BU
$$