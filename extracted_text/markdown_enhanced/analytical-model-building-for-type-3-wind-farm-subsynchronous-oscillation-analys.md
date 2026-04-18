# Analytical model building for Type-3 wind farm subsynchronous oscillation analysis
**Lingling Fan** $^{*,1}$, **Zhixin Miao** $^{1}$
*Dept. of Electrical Engineering, University of South Florida, Tampa FL 33620*

$^{*}$ Corresponding author. E-mail addresses: linglingfan@usf.edu (L. Fan), zmiao@usf.edu (Z. Miao).
$^{1}$ Senior Member, IEEE

**Keywords:** Type-3 wind, Phase-locked-loop, Subsynchronous resonances, Dynamic modeling

**Abstract:** Many real-world scenarios confirmed insights developed based on the $dq$-frame nonlinear analytical model for doubly-fed induction generator (DFIG)-based type-3 wind subsynchronous resonance (SSR) study by the authors in 2010. A few real-world observations do not align with the simulation results from that model. In real-world scenarios, when a type-3 wind farm is radially connected to a series compensated line, even at a low compensation level, SSR occurs. This phenomenon has not been replicated by the nonlinear analytical model. In this paper, we revisited the analytical model by including phase-locked-loop (PLL). A modular modeling approach is presented in this paper. The inputs and outputs of each subsystem and the interconnections among subsystems are identified first. The overall system is then developed with all blocks integrated. The analytical model is capable of dealing with various transmission topologies, providing both large-signal time-domain simulation results and small-signal analysis. The new analytical model can successfully replicate the aforementioned phenomena and provide insights of type-3 wind SSR phenomena. The accompanying software package will be posted in the public domain.

## 1. Introduction
### 1.1. Type-3 wind farm SSR events and lessons learnt
The first type-3 wind farm SSR occurred in 2007 in Minnesota. This type of events occurred later in Texas (2009), China (2012-2013), and Texas (2017). The phenomena have caused great interest to the industry and an IEE PES task force wind SSO has been formed. The task force report on real-world events and industry screening practice was published in PES resource center in July 2020 [1].

The analytical state-space model developed in 2010 for type-3 wind connected to a series compensated transmission line [2] has successfully identified the following facts: (i) SSR is not related to torsional interaction, rather related to doubly fed induction generators (DFIGs)’ electromagnetic circuits and converter controls; (ii) operating at lower wind speed may make SSR worse; and (iii) reducing the gain of rotor side converter (RSC) current control is better for SSR stability. The above three points have been validated by real-world type-3 wind SSR (in north China) event data analysis [3,4].

It is recognized first in [2] and also by the industry that torsional interaction is not the issue. [2] has modeled the shaft system as a two-mass system. Based on the particular parameters of wind turbines, the torsional modes have low frequencies, e.g., 1.8 Hz [5]. To have torsional interactions, the LC resonant frequency in the electric network should be more than 50 Hz for a 60 Hz ac system, which is not realistic. In most cases, every line has 50% series compensation level. The net compensation level for an equivalent circuit is much less than 50%. In real-world, wind farm SSR frequencies in currents are observed as 9-13 Hz (2007, Minnesota), 20-30 Hz (2009, Texas), 6-8 Hz (2012-2013, China), and 20-30 Hz (2017, Texas).

### 1.2. DQ-frame analytical modeling approach versus the other modeling approaches
The nonlinear analytical state-space model in [2] is built in $dq$-frames and all state variables assume constant values at steady state. This feature makes obtaining small-signal models at various operating conditions through numerical perturbation possible.

The other most popular modeling approaches are (i) nonlinear modeling based on stationary reference frame and (ii) frequency-domain or Laplace-domain impedance modeling approach. In the first category, $dq$-frame modeling is to represent every block in a unified $dq$-frame. Take the case of DFIG, it is well known that both the stator and the rotor should be modeled in the same reference frame. For that reason, the rotor circuit model in its nature reference frame (the rotor) needs to be first converted to the stator $dq$-frame. Due to its enticing feature, $dq$-frame based modeling technique has been adopted by DIgSILENT, as shown in the 2007 report [12].

### 1.3. Motivation to revisit the model
There are a few real-world observations not agreeing with the simulation results from the $dq$-frame model developed in [2]. Analysis

**Nomenclature**
| Symbol | Description |
|---|---|
| $dq_g$, $dq_{PLL}$ | The two $dq$-frames: one based on the grid voltage, the other based on PLL. |
| $i_s$, $i_r$, $i_g$ | DFIG’s instantaneous stator current, rotor current and grid-side converter current. |
| $R_1$, $L_1$, $C_1$ | The resistance, inductance, and capacitance of a series compensated line. |
| $R_2$, $L_2$ | The resistance, inductance of a non-compensated line. |
| $R_g$, $L_g$ | The grid-side converter (GSC) filter’s resistance and inductance. |
| $v_{PCC}$, $v_c$, $v_\infty$, $i_1$, $i_2$ | AC |