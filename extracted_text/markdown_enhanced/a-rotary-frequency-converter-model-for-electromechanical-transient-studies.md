# A rotary frequency converter model for electromechanical transient studies of $16\frac{2}{3}$ Hz railway systems

John Laury, Lars Abrahamsson, Math H.J. Bollen
Luleå University of Technology, Electrical Power Engineering Group, Skellefteå, Sweden

**Keywords:** Low frequency railways, $16\frac{2}{3}$ Hz, Modelling, Simulations, Transient stability, Rotary frequency converter, Motor generator set, Multi machine system

**ABSTRACT**
Railway power systems operating at a nominal frequency below the frequency of the public grid (50 or 60 Hz) are special in many senses. One is that they exist in a just few countries around the world. However, for these countries such low frequency railways are a critical part of their infrastructure.
The number of published dynamic models as well as stability studies regarding low frequency railways is small, compared to corresponding publications regarding 50 Hz/60 Hz public grids. Since there are two main type of low frequency railways; synchronous and asynchronous, it makes the number of available useful publications even smaller. One important reason for this is the small share of such grids on a global scale, resulting in less research and development man hours spent on low frequency grids.
This work presents an open model of a (synchronous-synchronous) rotary frequency converter for electromechanical stability studies in the phasor domain, based on established synchronous machine models. The proposed model is designed such that it can be used with the available data for a rotary frequency converter.
The behaviour of the model is shown through numerical electromechanical transient stability simulations of two example cases, where a fault is cleared, and the subsequent oscillations are shown. The first example is a single-fed catenary section and the second is doubly-fed catenary section.

## 1. Introduction

Low-frequency AC railways exist only in six countries: Austria, Germany, Switzerland, Norway, Sweden and in the (North East of the) U.S. [1,2]. As the frequency in the railway is different from the public grid, frequency conversion is needed [2,3]. The conversion can be done by using Motor-Generator sets, also called Rotary Frequency Converter (RFC).

Such an RFC consists of a three-phase motor and a single-phase synchronous generator mounted on the same mechanical shaft.

In Austria, Germany and Switzerland a double-fed induction motor is used, allowing active power to be controlled [2–4]. The active power supplied by the RFCs follows an active-power-frequency droop characteristic [4].

In Sweden, Norway and the North Eastern U.S. the motor is of synchronous type and therefore the railway grid is synchronous to the three-phase public grid. Active power through an RFC with synchronous motor is dependent on the angle difference between the three-phase public grid and the single-phase low-frequency railway grid of $16\frac{2}{3}$ Hz (Sweden, Norway) or 25 Hz (North Eastern U.S.) at the RFC locations.

A very limited amount of previous published work has been done on electromechanical stability of low-frequency railways that are synchronous with the public grid.

Small-signal studies on the Norwegian synchronous low-frequency railway grid have been performed in [5–8]. It was found from those studies that one of the most commonly used RFCs has a poorly damped eigenfrequency that could be excited by modern locomotives, which could lead to system instability. Those studies either use the classical model (which is essentially a constant electromotive force (emf) behind a transient reactance) for each of the two synchronous machines, or the commercial software Simpow for simulations with higher order synchronous machine models.

In [9] a transient stability assessment is done for the low-frequency railway grid of the North Eastern U.S. No models of RFC were presented in that study as the commercial software PSLF from GE was used.

Ref. [10] uses the classical model of a synchronous machine to investigate the transient stability of the Northern part of the Swedish railway system in the end of the 1980s.

There are only a small number of commercial software packages available that simulate dynamics of low-frequency railways that are synchronously connected to the public grid. Furthermore the models

**Table 1**
RFC parameters of the Q48/Q49.

| Parameter | Value |
|---|---|
| $X_{qm}, X_{dm}, X'_{dm}, X''_{qm}, X''_{dm}$ | 0.49, 1.02, 0.3, 0.3, 0.21 [p.u.] |
| $T'_{dom}, T''_{dom}, T'_{qom}$ | 3.6, 0.04, 0.09 [s] |
| Inertia constant motor, $H_M$ | 1.06 [MWs/MVA] |
| Rated power motor | 10.7 [MVA] |
| Transformer ratio motor | 80 [kV]/6.3 [kV] |
| Transformer leakage reactance of the motor, $X_{Tm}$ | 7.9% |
| $X_{qg}, X_{dg}, X'_{dg}, X''_{qg}, X''_{dg}$ | 0.53, 1.39, 0.16, 0.10, 0.12 [p.u.] |
| $T'_{dog}, T''_{dog}, T'_{qog}$ | |