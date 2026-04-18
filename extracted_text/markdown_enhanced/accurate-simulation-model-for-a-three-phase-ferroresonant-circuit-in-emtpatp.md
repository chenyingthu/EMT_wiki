# Accurate simulation model for a three-phase ferroresonant circuit in EMTP–ATP

Mi Zou

College of Automation, Chongqing University of Posts and Telecommunications, Chongqing 400065, China
Key Laboratory of Industrial Internet of Things and Networked Control, Ministry of Education, Chongqing University of Posts and Telecommunications, Chongqing 400065, China

**Keywords:** Ferroresonance, Jiles–Atherton model, EMTP–ATP, Electromagnetic transient

**Abstract:** This study presents a simulation model for a ferroresonant circuit. The proposed model includes a transformer model and a vacuum circuit breaker (VCB) model. Hysteresis nonlinearity and core topology are considered in the transformer model. The VCB model comprises the current chopping level, withstand capability, and quenching capability. Fundamental ferroresonance and sub-harmonic ferroresonance experiments are conducted to verify the accuracy of the proposed ferroresonance simulation model. Bifurcation, phase-plane, and Poincare methods are used to compare the difference between the simulation and experiment results. The proposed model can accurately predict the ferroresonance, and the waveform similarities calculated from the experiment and simulation data are greater than 0.9.

## 1. Introduction

Ferroresonance is a nonlinear oscillation phenomenon that occurs in electric systems that contain a transformer iron-core inductor and a capacitor [1–6]. Ferroresonance does not occur when the transformer voltage is maintained below the saturation point [7,8]. However, an energy exchange between the capacitor and nonlinear magnetizing inductance can occur when the transformer voltage exceeds the core saturation point [9–11]. The rapid changes in core flux during this condition may cause high ferroresonance overvoltages or overcurrents with highly distorted waveforms, which can pose a remarkable safety hazard and cause irreparable damage to the power equipment.

Several steady-state solutions may exist for a particular excitation condition and the range of circuit parameters due to the nonlinearity of ferroresonance [12]. Four basic modes, namely, fundamental ferroresonance, subharmonic ferroresonance, quasi-periodic ferroresonance, and chaotic ferroresonance, have been identified on steady-state responses under ferroresonance conditions [13]. Sophisticated mathematical techniques (e.g., bifurcation, phase-plane, and Poincare analysis) are introduced to deeply understand and distinguish the various types of ferroresonance after ferroresonance overvoltage or overcurrent waveforms are obtained [14–20]. However, the prediction and modeling of ferroresonance remain challenging tasks.

Transformer models are essential tools used in investigating and predicting ferroresonance. Although considerable studies have been conducted in transformer modeling over the past few decades, three-phase transformer models have not progressed compared with single-phase transformer models due to the challenges in modeling transformer core topologies and transformer core hysteresis nonlinearities [21–23]. Polynomial, arctangent, exponential, and multisegment piecewise linear expressions are widely used to model the transformer core behavior. These methods are sufficient for steady-state analysis. However, dynamic and transient disturbances, such as ferroresonance, require accurate methods. Thus, Jiles–Atherton (JA) hysteresis reactor and duality transformation are applied to solve the two problems in this study. In addition, ferroresonance is sensitive to initial conditions (e.g., residual fluxes) and system perturbations (e.g., switching) [21–24]. Therefore, the proposed vacuum circuit breaker (VCB) model is used to improve the accuracy of switching transients.

The rest of this paper is organized as follows. Section 2 derives a low-frequency transformer model. Section 3 introduces the VCB model in Electromagnetic Transients Program–Alternative Transients Program (EMTP–ATP) that is used to model the switching action. Section 4 establishes a ferroresonance electric circuit simulation model. Section 5 demonstrates the ferroresonance experiment system. Section 6 presents the validation and discussion of fundamental ferroresonance and sub-harmonic ferroresonance. Section 7 provides the conclusion.

$$
\frac{di_m}{dH} = \frac{i_{man} - i_m}{k/(1-c)} + c \frac{di_{man}}{di_{eff}} \quad \text{for } i > 0
$$
$$
\frac{di_m}{dH} = c \frac{di_{man}}{di_{eff}} \quad \text{for } i \le 0 \quad (3)
$$