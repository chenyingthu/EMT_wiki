## A Systematical Method for Suppressing Ferroresonance at Neutral-Grounded Substations
**Yunge Li, Wei Shi, Rui Qin, and Jilin Yang**

**Abstract**—At neutral-grounded substations, ferroresonance may happen upon switching a circuit breaker or disconnector, due to the saturated magnetizing characteristics of the bus PT. In this paper, a systematical method is presented to analyze and suppress the phenomenon. The scheme for suppressing the ferroresonance is to insert resistance, made from parallel-connected resistors, into the PT’s wye secondary circuit. For a particular substation, it is first studied theoretically whether ferroresonance can possibly happen; and if so, a theoretical critical resistance is estimated to avoid the resonance. A practical one is then achieved by EMTP simulation on the basis of the theoretical one. The scheme for switching these resistors out of the circuit is to do that not all at once, but rather, in turn, to avoid exciting ferroresonance again. The appropriate resistance value of the resistors and the schedule of switching them out are also determined by EMTP simulation. A prototype was developed to fulfill the scheme, and proved to be effective by field tests.

In addition, it is demonstrated that this kind of ferroresonance cannot be suppressed by adding resistance to the PT’s delta secondary circuit.

**Index Terms**—Circuit breaker, electromagnetic transient, EMTP, ferroresonance, potential transformer, substation.

*Manuscript received July 12, 2001; revised June 19, 2002. This work was supported by Gansu Electric Power Company.*
*Y. Li and W. Shi are with the School of Electrical Engineering, Xi’an Jiaotong University, Xi’an, Shaanxi 710049, China (e-mail: yunge_li@263.net; weishi@xjtu.edu.cn).*
*R. Qin and J. Yang are with Jinyuan Power Plant, Gansu 730919, China.*
*Digital Object Identifier 10.1109/TPWRD.2003.813858*

## I. INTRODUCTION
RESONANCE occurs at a substation (referred to as station below) which is fed by two 110-kV overhead lines. The 110-kV system is neutrally grounded. A one-line diagram of the station is shown in Fig. 1. CB0, CB1, and CB2 are the circuit breakers equipped with grading capacitors, and PT1 and PT2 are the single-phase electromagnetic potential transformers (PTs) on bus sections BUS1 and BUS2, respectively.

From field experiences, resonant conditions on BUS1 are summarized as follows.
1) While either breaker CB0 or CB1 is open, resonance will occur upon opening the other one, with disconnectors DS0-1, DS0-2, DS1-1, and DS12 closed.
2) Then there is a strong probability that resonance would happen again as soon as any of the four disconnectors is opened.
3) If the disconnector opened in step 2 is reclosed subsequently, resonance has been observed for several times.

During the operating process shown before, the circuit breaker and disconnector of transformer TRANS1 remain open.

Because of the voltage dividing effect of the circuit breakers’ grading capacitances and the system capacitance to ground, any switching operation causes a step-change in voltage on BUS1. That is to say, except switching operations fully unenergizing BUS1, or completely energizing it to the normal working voltage, any operation resulting in a voltage change on BUS1 can possibly lead to a resonant condition.

This kind of voltage oscillation is apparently due to PT1’s nonlinear inductance. With breaker CB0 already open, opening CB1 leaves PT1 energized through the grading capacitances of CB0 and CB1, virtually resulting in a series–resonant circuit, where is the nonlinear inductance of PT1, and the equivalent of the bus-to-ground capacitance and the grading capacitances of CB0 and CB1.

The resonant condition on BUS2 is similar to that on BUS1. In fact, Fig. 1 shows the general circuit configuration of ferroresonance due to core saturation of electromagnetic potential transformers installed at neutral-grounded substations. Therefore analyzing the resonance and its suppressing methods, which is the aim of this paper, will hopefully be of general interest.

Ferroresonance commonly takes place at neutral-grounded substations where conventional electromagnetic PTs are installed. Great efforts have been carried out to explain this phenomenon. Parameters that influence PT behaviors were highlighted in [1]–[4], such as core losses, system capacitance, and the degree of core saturation. Besides, attentions were paid to some other features, such as ferroresonant types and safe regions. These works have presented a general conception of the ferroresonant problem. Literature [5]–[7] provided guidelines based on field experiences to avoid and suppress ferroresonance.

A particular type of ferroresonance-suppressing device, which works by inserting a small resistance at PTs’ delta secondary circuit, had been tried at station. But it turned out to be a failure.

In this paper, a novel scheme is proposed to suppress ferroresonance. Before it is likely to happen, several resistors in parallel are simultaneously switched into the wye secondary circuit of the PT. However, the resistors are switched out, not all at once, but rather, in turn, to avoid exciting ferroresonance again.

**Fig. 1.** Diagram of X station.
**Fig. 2.** Circuit arrangement of Fig. 1.
**Fig. 3.** PT’s magnetizing characteristic.
**Fig. 4.** Reduced equivalent circuit.

field measurement as a current-voltage curve, which was then converted to a current-flux curve as shown in Fig. 3.

### B. Cause and Elimination o