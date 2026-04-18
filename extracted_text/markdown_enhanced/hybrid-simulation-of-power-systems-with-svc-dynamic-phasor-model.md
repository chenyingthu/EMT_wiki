# Hybrid simulation of power systems with SVC dynamic phasor model

E Zhijun$^a$, D.Z. Fang$^{a,*}$, K.W. Chan$^b$, S.Q. Yuan$^{a,b}$

$^a$ Key Laboratory of Power System Simulation and Control of Ministry of Education of China, Tianjin University, 300072 Tianjin, China
$^b$ Department of Electrical Engineering, The Hong Kong Polytechnic University, Hong Kong, China

* Corresponding author. E-mail address: dz_fang@yahoo.com.cn (D.Z. Fang).

**Article history:**
Received 16 October 2007
Received in revised form 23 January 2009
Accepted 28 January 2009

**Abstract**
A novel hybrid method for simulation of power systems equipped with static var compensators (SVC) is suggested in this paper, where dynamic phasor theory is applied for SVC, and traditional electromechanical transient models are used for ac subsystem. A detailed single-phase dynamic phasor-based SVC model is derived first, and an interface algorithm between the SVC dynamic phasor model and the ac subsystem is proposed next. Test results on the 9-bus and the New England 39-bus test power systems show clearly that the single-phase SVC dynamic phasor model has very good accuracy as compared with its electromagnetic transient model. The proposed hybrid-model simulation method provides a new approach for dynamic simulation of large-scale power systems including SVCs.

**Keywords:**
Dynamic phasors, Transient stability, Electromagnetic transients, Hybrid simulation, Static var compensator

## 1. Introduction

With the rapid development of modern power systems, flexible ac transmission systems (FACTS), a new kind of power electronic devices such as static var compensator (SVC), have been widely applied in the operation and control of power systems. There are extensively studied mathematical models available for simulating the voltage and current waveform relationships during the valve-to-valve switching and discrete control of FACTS devices using electromagnetic transient program (EMTP) [1]. However, the EMTP is not suitable for large-scale power system dynamic behavior analysis for its tiny time step and overall CPU time cost. On the other hand, transient stability program (TSP) [2,3] can simulate the transient behavior of large-scale power systems for some disturbance, but cannot provide voltage/current waveform responses of highly nonlinear components such as high voltage direct current (HVDC) links and FACTS.

To incorporate the advantages of both TSP and EMTP, hybrid simulation methods have been developed in [1,4–6]. In hybrid simulations, power systems are split into TSP and EMTP simulation subsystems through interface buses. The EMTP subsystems usually consist of nonlinear components such as HVDC and/or FACTS devices, while the rest system is considered as the TSP subsystem. The hybrid methods interactively execute programs of EMTP for HVDC links and/or FACTS devices, and of TSP for the rest of the power system, alternatively. Usually, TSP simulation utilizes relatively larger integration step size (e.g. 0.02 or 0.01 s for a 50-Hz ac system) using single-phase network model, and EMTP simulation adopts much smaller integration step size (e.g. 50 $\mu$s) using 3-phase circuit model. Hence, the hybrid simulation is faster than the traditional EMTP simulation of entire networks. Meanwhile it preserves the advantages of EMTP in the accurate voltage and current waveform simulation for the target part of system. In addition, hybrid simulation requires less computer memory resources than that the EMTP does. However, the phase discontinuity in TSP equivalent and the effect of dc-offset in EMTP equivalent are the main problems which reduce the accuracy of this type of TSP-EMTP hybrid simulation [7].

Dynamic phasor (DP) model based on the approach of time-varying Fourier coefficient series can catch and approximate waveform response of dynamic nonlinear components of power system described by EMTP models [8–10]. In recent years, DP modeling method has been successfully applied in the simulation and analysis of power systems with nonlinear devices. A number of DP models of nonlinear components, such as HVDC [11–12], static synchronous compensator (STATCOM) [12], thyristor-controlled series capacitor (TCSC) [13], and unified power-flow controller (UPFC) [14], have been studied in the hybrid simulation framework and have achieved satisfactory results.

A hybrid simulator which combines a new single-phase equivalent DP model of static var compensator (SVC) into the conventional TSP computation is presented in this paper. In the hybrid simulator, the SVC has been represented by the SVC DP subsystem. The improvement is that the DP subsystems are simulated using a new single-phase circuit model with larger integration step size.

## Nomenclature

| Symbol | Description |
|---|---|
| $x(s), y(s)$ | time-domain waveform |
| $X_k(t)$ | $k$th dynamic phasor of $x(s)$ |
| $\frac{dX_k}{dt}(t)$ | differential of $k$th dynamic phasor |
| $\left[\frac{dx}{dt}\right]_k(t)$ | $k$th dynamic phasor of the differential of $x(s)$ |
| $C$ | capacitor of TCR |
| $\alpha$ | firing angle of TCR |
| $\sigma$ | conduction angle of TCR |
| $R_f$ | resistor of the filter RLC circuit |
| $L_f$ | inductor of the filter RLC circuit |
| $C_f$ | capacitor of the filter RLC circuit |
| $V_1(t)$ | resistor voltage of filter circuit |