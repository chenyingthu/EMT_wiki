## MODELING OF AC MACHINES USING A VOLTAGE-BEHIND-REACTANCE FORMULATION FOR SIMULATION OF ELECTROMAGNETIC TRANSIENTS IN POWER SYSTEMS

by

**LIWEI WANG**

B. Eng., Hebei University of Technology, 2001
M. Eng., Tianjian University, 2004

A THESIS SUBMITTED IN PARTIAL FULFILMENT OF THE REQUIREMENTS FOR THE DEGREE OF

DOCTOR OF PHILOSOPHY

in

THE FACULTY OF GRADUATE STUDIES

(Electrical and Computer Engineering)

THE UNIVERSITY OF BRITISH COLUMBIA

(Vancouver)

February 2010

© Liwei Wang, 2010

## ABSTRACT

Modeling of electrical machines for power system’s electromagnetic transient programs (EMTP) has been an active area of research since the late 1970s. Most machine models are based on the qd reference frame. The phase-domain (PD) model was also proposed wherein the direct interface with the external network is achieved at a price of increased the computational cost.

This thesis focuses on improving the numerical efficiency and accuracy of machine models for power systems transient simulation. The modeling approach developed in this thesis is based on the so-called voltage-behind-reactance (VBR) formulation. The new VBR models of synchronous and induction machines are proposed for EMTP-type solution. It is shown that the proposed VBR models significantly improve the overall numerical accuracy and efficiency, compared with the traditional qd and PD models, due to the direct machine-network interface and better-scaled eigenvalues. The proposed implementations of the new models require as little as 240 flops for synchronous and 108 flops for induction machines, per time-step, respectively. This amounts to 3.75μs and 1.6μs (per time-step) of the CPU time on a modest personal computer and represents a significant improvement over existing EMTP machine models. Magnetic saturation has been incorporated into the VBR models for EMTP-type solution. Computer studies demonstrate that the proposed saturable VBR model in addition of being very efficient also preserves good numerical accuracy and stability even at very large time step. A new full-order VBR induction machine model is also proposed for state-variable simulation languages, wherein three practical equivalent circuits have been introduced. Computer studies demonstrate that the proposed models achieve a 740% improvement in computational efficiency as compared with the traditional coupled-circuit models used in state-variable simulation languages. Finally, an approximate VBR induction machine model is proposed for the discretized EMTP solution wherein a constant equivalent conductance matrix is achieved. This further improves the efficiency of the machine-network solution since it avoids the re-factorization of the network conductance matrix at every time step. It is envisioned by the author that due to structural and numerical advantages, the proposed VBR models will find wide application in simulation packages and tools widely used in the power industry.

## TABLE OF CONTENTS

- Abstract
- Table of Contents
- List of Tables
- List of Figures
- Acknowledgements
- Co-Authorship Statement
- 1 INTRODUCTION
  - 1.1 The qd Model
  - 1.2 The Coupled-Circuit Phase-Domain Model
  - 1.3 The Voltage-Behind-Reactance Model
  - 1.4 Summary of Results and Contributions
  - 1.5 Thesis Organization
  - 1.6 References
- 2 A VOLTAGE-BEHIND-REACTANCE SYNCHRONOUS MACHINE MODEL FOR THE EMTP-TYPE SOLUTION
  - 2.1 Introduction
  - 2.2 Synchronous Machine Models
    - 2.2.1 Traditional qd Model
    - 2.2.2 Phase-Domain Model
    - 2.2.3 Voltage-Behind-Reactance Model
  - 2.3 Discrete-Time Model Representations
    - 2.3.1 Discrete-Time Phase-Domain Model
    - 2.3.2 Discrete-Time Voltage-Behind-Reactance Model
    - 2.3.3 Model Complexity
  - 2.4 Interface Procedure
  - 2.5 Computer Studies
    - 2.5.1 Model Verification
    - 2.5.2 Numerical Accuracy
    - 2.5.3 Model Efficiency
  - 2.6 Error Analysis
  - 2.7 Discussion of Network Solution
  - 2.8 Conclusion
  - 2.9 References
- 3 MODELING OF INDUCTION MACHINES USING A VOLTAGE-BEHIND-REACTANCE FORMULATION
  - 3.1 Introduction