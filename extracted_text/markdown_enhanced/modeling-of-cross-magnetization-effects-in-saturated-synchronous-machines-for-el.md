# Modeling of cross-magnetization effects in saturated synchronous machines for electro-magnetic transient programs

A.B. Dehkordi $^{a,*}$, A.M. Gole $^{b}$, T.L. Maguire $^{c}$

$^{a}$ A. B. Dehkordi is with RTDS Technologies Inc., Winnipeg, Canada
$^{b}$ Ani Gole is with the University of Manitoba, Winnipeg, Canada
$^{c}$ T L. Maguire is retired from RTDS Technologies Inc. as a co-founder, Canada

**Keywords:** Synchronous machine, Generator, Saturation, Cross-magnetizing effects, Electro-magnetic transient programs, Real-time digital simulation

**Abstract**
The saturation of magnetizing paths in synchronous machines significantly impacts machine performance, including loading capability. In electromagnetic transient (EMT) programs, magnetic saturation is traditionally modeled by adjusting the d-axis or q-axis magnetizing inductances (or flux linkages) [1-4]. A similar approach is applied in phasor-domain programs [5]. While these methods account for d- and q-axis saturation simultaneously, they overlook the rotor’s inherent structure and the angular displacement of the MMF wave in the airgap.
This paper presents the development and validation of an EMT synchronous machine model that incorporates cross-magnetizing effects into the saturation algorithm. The proposed method evaluates saturation based on the magnitude and angle of the MMF. Additionally, the paper examines the impact of various simplifications on the loading capability of synchronous generators.

## 1. Introduction
Magnetic saturation in synchronous machines impacts both steady-state loading and transient performance. Although the presence of an air gap in electric machines reduces the severity of saturation compared to power transformers, accurately modeling saturation effects in the magnetizing path is essential for simulating networks containing electric machines. The most direct consequence of saturation is the alteration of magnetizing reactances, which affects a machine’s capability to handle various loading conditions. Additionally, saturation can influence the rotor angle stability limit of synchronous generators.

The scope of this paper focuses on modeling saturation in synchronous machines used as generators in power system networks. For such studies, an idealized machine model is sufficient. This model assumes sinusoidal magnetomotive force (MMF) distributions from the windings and sinusoidally distributed permeance, effectively ignoring space harmonics.

This assumption enables the use of the two-reaction theory [6] and [7] and the widely adopted D- and q-axis equivalent circuit for synchronous machines in power system studies. One key advantage of the dq equivalent circuit is its simplicity, making it accessible to a broader group of power engineers. Moreover, the model effectively predicts essential behaviors of synchronous generators concerning the network, including time constants, loading capability, short-circuit currents, and more.

In the two-reaction theory, also known as the dq0 theory, the effects of iron saturation in synchronous machines are modeled by adjusting the D- and q-axis magnetizing inductances $L_{md}$ and $L_{mq}$ (or reactances) in the machine’s equivalent circuit. This adjustment is typically based on the magnitudes of the magnetizing currents $i_{md}$ and $i_{mq}$, or the corresponding flux linkages.

The following assumptions are generally made when representing magnetic saturation in synchronous machines using the two-reaction theory [6] and [7]:
- Leakage inductances are independent of saturation. Since leakage fluxes flow predominantly through air, their path is minimally influenced by the saturation of the iron portion. Consequently, only the magnetizing inductances in the equivalent circuit are affected by saturation.
- Saturation does not deform the sinusoidal distribution of the magnetic field. It is assumed that the magnetic field over the face of a pole retains its sinusoidal distribution, ensuring that all inductances maintain their sinusoidal dependence on rotor position.

Given the above assumptions, the effect of saturation can be represented by (1). In this equation, $L_{mdu}$ and $L_{mqu}$ are the unsaturated values of $L_{md}$ and $L_{mq}$ respectively. $K_{sd}$ and $K_{sq}$ are called the saturation factors and identify the level of saturation in the D- and q- axes respectively. These factors are functions of D- and/or q- axis magnetizing fluxes (or currents) referred to as saturation indices. In unsaturated conditions these factors are equal to 1.0.

$$
\begin{aligned}
L_{md} &= K_{sd} \cdot L_{mdu} \\
L_{mq} &= K_{sq} \cdot L_{mqu}
\end{aligned} \tag{1}
$$

### 2.1. Macroscopic and microscopic view of synchronous machine open circuit characteristics
Open circuit characteristics are typically the primary data set available for modeling saturation in simulation studies. These characteristics are obtained by operating the synchronous machine at open circuit, running it at the rated rotor speed, and gradually increasing the field winding current. The terminal voltage is measured and recorded (usually in per-unit) as a function of the field current. This open circuit saturation characteristic is also referred to as the D-axis magnetization characteristic. To replicate this behavior in a numerical model of a synchronous machine, it is sufficient to vary the D-axis magnetizing