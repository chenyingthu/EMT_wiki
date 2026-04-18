Revisiting dynamic phasors and their efficacy in simulating electric circuits
Ramin Parvari, Shaahin Filizadeh*, Dilsha Kuranage
University of Manitoba, Winnipeg, MB R3T 5V6, Canada

**Keywords:** Dynamic phasors (DP), Electromagnetic transient (EMT) simulations, Companion circuit, Eigenvalues

**Abstract:** In this paper, the theory and application of dynamic phasors (DPs) to model and simulate electrical circuits are revisited. The paper reveals foundational conditions that must be in place so that DPs are able to offer computational benefits that are commonly, yet incorrectly, attributed to them as universal characteristics. Following a companion model-based approach using DPs, eigenvalue and steady-state analyses are conducted to assess the precision of EMT and DP modeling methods as a function of the simulation time step. Through a case study of the IEEE 9-bus system, the effects of large time-steps on simulation accuracy are illustrated. The findings demonstrate that while DP-based modeling can accurately represent steady-state behavior of circuits with large time-steps, its accuracy is limited during transients conditions, highlighting the importance of judicious time-step selection for accurate simulations.

* Corresponding author.
E-mail addresses: parvarir@myumanitoba.ca (R. Parvari), shaahin.filizadeh@umanitoba.ca (S. Filizadeh), kuranagd@myumanitoba.ca (D. Kuranage).
I This work was supported in part by the Natural Sciences and Engineering Research Council (NSERC) of Canada, and by the University of Manitoba, Canada.
II Paper submitted to the International Conference on Power Systems Transients (IPST2025) in Guadalajara, Mexico, June 8–12, 2025.

## 1. Introduction

Several methods with varying degrees of accuracy and computational complexity exist for modeling and simulation of power systems [1–3]. For instance, transient stability (TS) programs ignore the fast dynamics of the electrical network, focusing instead on the relatively slow electromechanical interactions in large, interconnected systems. TS-type solvers benefit from large simulation time-steps (in the milliseconds range), thereby reducing the run time. Electromagnetic Transients (EMT) solvers, on the other hand, capture the fast dynamics of circuits, e.g., switching transients, in great detail [4,5]. EMT solvers typically require small time-steps (in the microseconds range), which significantly extend the run time, especially for large power system with sophisticated components such as high-frequency power-electronic converters.

One approach to bridge the gap between the accuracy of an EMT solver and the computational efficiency of a TS solver is to use the concept of dynamic phasors, in which frequency-shifting is used to focus on the low-frequency content of a band-pass signal [6,7]. In this approach, the circuit’s natural quantities, i.e., branch voltages and currents, are assumed to be sinusoidal but modulated with a low-frequency signal that characterizes the dynamics of the power system. Mathematically, an arbitrary voltage or current, $x(t)$, is assumed to take on the form
$$x(t) = X(t)e^{j\omega_0 t} \quad (1)$$
where $X(t)$ is the dynamic phasor, and $e^{j\omega_0 t}$ represents the sinusoidal signal of the base (i.e., shift) frequency $\omega_0$. Dynamic phasor analysis is based upon solving for the dynamic phasors of a network’s voltages and currents, whereas an EMT simulator solves the circuit for its natural quantities.

This approach has been applied to a wide range of systems, including line-commutated and modular multilevel converters (LCCs and MMCs) [8–10], flexible AC transmission systems (FACTS) [11,12], induction machines [13,14], and hybrid simulations [15–18]. Dynamic phasors have also been utilized to expand the frequency bandwidth of TS-type simulations [19].

Dynamic phasors are widely believed to substantially reduce the computational burden of discrete-time EMT-type simulations. This belief stems from the notion that simulating circuits to find a low-frequency signal, i.e., the dynamic phasor or $X(t)$, does not require the small time-steps that an EMT solver needs to use to capture the natural signal. Thus, larger time-steps can be used to speed up the simulation [3,6,20,21]. However, as this paper demonstrates, this statement is not universally valid and is subject to specific conditions that are imposed by the circuit that is modeled. In particular, the paper shows that the eigenvalues of the circuit play a crucial role in whether or not modeling in the DP domain may offer benefits without considerable loss of accuracy.

A generalized theory of dynamic phasors is developed in Section 2 using the concept of an integrating factor. It is demonstrated that the commonly-used term $e^{j\omega_0 t}$ is a special case where the shift frequency remains constant over time. Additionally, a generalized continuous-time companion circuit is developed in this section. Section 3 presents

### Table 1
Basic elements in original and companion circuit domains.
| Original Circuit | Continuous-time Companion Circuit |
| :--- | :--- |
| $e(t)$ | $e(t)e^{-\int_0^t s(\tau)d\tau}$ |