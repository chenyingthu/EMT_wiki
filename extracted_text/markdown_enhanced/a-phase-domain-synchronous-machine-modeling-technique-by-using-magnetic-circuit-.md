# A phase-domain synchronous machine modeling technique by using magnetic circuit representation of armature and rotor windings
R. Yonezawa
Grid and Communication Technology Division, Grid Innovation Research Laboratory, CRIEPI (Central Research Institute of Electric Power Industry), 2-6-1, Nagasaka, Yokosuka, Kanagawa 240-0196, Japan

**Keywords:**
Electromagnetic transient (EMT) analysis
Magnetic circuit representation
Park’s equations
Phase domain
Spatial harmonics
Synchronous machine

**Abstract**
A phase-domain synchronous machine modeling technique by using only basic circuit components and applying the magnetic circuit representation used for transformer modeling is proposed in this paper. The model based on the proposed technique is implemented into XTAP, one of the electromagnetic transient analysis programs, and the accuracy of the proposed model is validated through simulation in an infinite-bus case system by comparing it with some conventional synchronous machine models in this paper.

## 1. Introduction
Although the number of synchronous machines has been decreasing owing to the recent increase in the utilization of renewable energy, they are still a major source of energy in power systems and models that can accurately reproduce the electrical and mechanical behaviors of synchronous machines in power system simulation are needed.

A synchronous machine consists of armature windings, a field winding, and one or more damper windings arranged spatially, and its electrical behavior (the relationship between voltage and current in each winding) can be expressed by circuit equations composed of an inductance matrix consisting of the self- and mutual inductances and a resistance matrix to express the resistances of each winding [1]. However, the values of some elements of the inductance matrix change from time to time depending on the rotor position (angle), which makes their handling complicated in transient analysis. Therefore, in the field of power system analysis, a model based on Park’s equations (referred to as Park’s model in this paper), which eliminates the time-varying inductances between windings by using the dq0 transformation on the inductance matrix, is the standard model for synchronous machines and has been widely used for many years [2].

Park’s model assumes the following two points: (1) the magnetic field distribution in the air gap is sinusoidal, and (2) the circuit constants such as the inductances and resistances of each phase winding are balanced among the three phases. Although the first assumption is not strictly true, many synchronous machines use distributed armature windings so that the spatial distribution of the magnetomotive force approaches a sinusoidal one, and adopting this assumption does not pose a major problem. In most of the analyses that have been conducted, Park’s model has been sufficiently accurate.

However, with the increase in the number of power conditioning systems and other power electronics equipment used in renewable energy interconnection, the need for analysis that takes harmonics into account is expected to increase in the future. Accordingly, a synchronous machine model that can appropriately take into account spatial harmonics in the magnetic field distribution, which has been ignored until now because it has no significant impact, is considered necessary. In the design of synchronous machines, it is sometimes necessary to analyze a situation in which the machine parameters become three-phase unbalanced, such as an internal short-circuit accident in an armature winding [3]. Under such condition, Park’s model cannot be used as it is because it does not satisfy the second assumption [4].

A method for solving the circuit equations of a synchronous machine in the three-phase domain without using the dq0 transformation (called a phase-domain model) has been proposed to realize these analyses [5, 6]. Therefore, for analyses where Park’s model cannot be used, users can create a phase-domain model of a synchronous machine according to the type of analysis and perform their analysis using this model.

When performing analysis of a power system that includes synchronous machines, it is not practical to create an analysis program, including a synchronous machine model, from scratch. In the case of electromagnetic transient (EMT) analysis, EMTP (DCG-EMTP [7], EMTP-RV [8]), ATP [9], PSCAD [10], and XTAP [11] are the typical analysis programs used. Since the source codes of these programs are usually not disclosed, models that require incorporation into the program are not practically available except to the program developers. However, the phase-domain models proposed so far have been implemented as models embedded in programs (black-box models where the models cannot be edited). Therefore, it is virtually difficult for users to create a phase-domain model that can simulate spatial harmonics and internal faults. It was also practically impossible to improve or expand the existing model for research and development purposes, such as simulating a dual-excited synchronous machine [12].

In this paper, the author proposes a phase-domain modeling technique for synchronous machine and the induced electromotive voltage of the winding corresponds to the magnetic flux. Depending on the method of connection between the electric and magnetic circuits, both circuits can also be solved simultaneously [14,15]. Therefore, in this paper, the author proposes a technique to represent a synchronous machine by a combination of basic circuit elements by applying the magnetic-circuit-based method in transformer modeling described above to the circuit equations for a synchronous machine.

### 2.1. Magnetic circuit modeling of the circuit equations for a synchronous machine