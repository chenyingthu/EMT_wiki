## Hybrid-model transient stability simulation using dynamic phasors based HVDC system model
Haojun Zhu a,∗, Zexiang Cai a, Haoming Liu b, Qingru Qi c, Yixin Ni d,e
a College of Electrical Engineering, South China University of Technology, Guangzhou 510640, China
b Department of Electrical Engineering, Southeast University, Nanjing 210096, China
c North China Power Engineering Co. Ltd., Beijing 100084, China
d Department of Electrical and Electronic Engineering, The University of Hong Kong, Hong Kong, China
e Graduate School at Shenzhen, Tsinghua University, Shenzhen 518055, China

Received 4 April 2005; received in revised form 25 August 2005; accepted 25 September 2005
Available online 21 November 2005

**Abstract**
A novel hybrid-model transient stability simulation algorithm for ac/dc power systems is suggested in this paper, where dynamic phasors theory is applied for HVDC transmission system modeling, and traditional electromechanical transient models are used for ac system. A detailed dynamic-phasors-based HVDC system model is derived first, and the algorithm for interface of the dc dynamic phasors model to ac network is proposed next. Computer simulation results show that the HVDC dynamic phasors model has very good accuracy as compared with its electromagnetic transient model; the test results from a 2-area ac/dc power system and a multi-infeed HVDC power system show clearly that the suggested interface algorithm works effectively in system transient stability analysis. The proposed hybrid-model simulation algorithm provides a new approach for dynamic simulation of large-scale ac/dc power systems.
© 2005 Elsevier B.V. All rights reserved.

**Keywords:** Hybrid-model simulation; Dynamic phasors; Transient stability; HVDC transmission

## 1. Introduction
HVDC transmission system plays an important role in modern large-scale interconnected power systems. In order to study the impacts of HVDC system on large-scale ac/dc power system performance, developing a sophisticated HVDC system model is significant. In traditional time-domain simulation programs, two types of HVDC system models are often used. One is the electromagnetic transient (EMT) model with very small step length (no more than 0.1 ms), which considers detailed valve operation and their impacts on system transients. The other is the quasi-steady-state (QSS) or average-value model widely used in transient stability simulation with larger step length (say 5 ms). In general the former is not suitable for large-scale ac/dc power system transient stability analysis for its tiny time step and overall cpu time cost; while the latter is difficult to consider asymmetric ac faults and dc converter commutation failure impacts on transient stability for the model simplification.

In recent years, dynamic phasors theory and relevant methods [1] have been applied in modeling power electronic devices (PEDs). Based on the time-varying coefficients of dominant items in Fourier series, dynamic phasors method has the potential to fill in the gap between the EMT and QSS models [2]. By truncating unimportant higher order components and keeping only those significant components, the dynamic phasors model is capable of retaining the dominant dynamic features of PEDs and suitable to power system transient stability study. This approach has been successfully applied in the modeling of certain FACTS devices, such as TCSC and UPFC, and ac machines with PED controllers [3–6]. In this paper, dynamic phasors method has been extended to HVDC transmission system modeling for large-scale ac/dc power system transient stability simulation.

In the paper, a detailed dynamic-phasors-based HVDC model is derived first. Using switching functions to describe the switching status of each converter bridge and applying dynamic phasors method in converter modeling, the behaviors of the dc system can be described accurately. After that a novel hybrid-model simulation algorithm for ac/dc power systems transient stability analysis is suggested, where dc system is in dynamic phasors model and ac system is in traditional electromechanical transient model. The interface algorithm of ac and dc systems in each time step is proposed based on Newton–Raphson method for better convergence. Computer test results show that HVDC dynamic phasor model has very good accuracy as compared with its electromagnetic transient model but uses much less cpu time in simulation; and the test results from a 2-area ac/dc power system and a multi-infeed HVDC power system show clearly the effectiveness of the suggested interface algorithm in transient stability analysis.

∗ Corresponding author. Tel.: +86 755 26036003; fax: +86 755 26036001. E-mail address: zhuhaojun@vip.sina.com (H. Zhu).

## 2. HVDC modeling using dynamic phasors

### 2.1. Outline of the dynamic phasors method
The method of dynamic phasors [1] is based on the time-varying coefficients of Fourier series. An outline of the method is given below. A time-domain waveform $x(\tau)$ can be expressed over the time interval $\tau \in (t - T, t)$ using Fourier series as [1]:
$$x(\tau) = \sum_{k=-\infty}^{\infty} X_k(t) e^{j k \omega_s \tau} \quad (1)$$
Considering dynamic phasors as special state variables, the dynamic phasors based new state-space model can be established. By truncating those unimportant components, the model is simplified with only dominant components remaining, which is the key idea for dynamic phasor modeling. In general the physical characteristics of the studied problem determine which components should be neglected or kept.

### 2.2. Time-domain dynamic model of HVDC
A schematic diagram of a single-pole HVDC transmission system is shown in Fig. 1.

*Fig. 1. Schematic diagram of an HVDC system.*

For the rectifier, the instantaneous values of ac phase voltages are assumed to be:
$$v_a = \sqrt{2}V \cos(\omega t)$$
$$v_b = \sqrt{2}V \cos(\omega t - 2\pi/3)$$
$$v_c = \sqrt{2}V \cos(\omega t + 2\pi/3)$$