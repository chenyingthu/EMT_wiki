# Photovoltaic generator modelling to improve numerical robustness of EMT simulation
Anna Rita Di Fazio ∗, Mario Russo
DAEIMI, Università degli Studi di Cassino, 03043 Cassino, Italy

∗ Corresponding author. Tel.: +39 07762993636; fax: +39 07762993886.
E-mail addresses: a.difazio@unicas.it (A.R. Di Fazio), russo@unicas.it (M. Russo).

## Abstract
Numerical simulation is an indispensable tool for studying photovoltaic (PV) systems, to derive component ratings, optimise protections, design controllers as well as to evaluate the impact of embedded generation on distribution system operation. In EMT simulation, the non-linear equations representing the PV generators are separated from the linear equations of the rest of the power system. This technique presents high computational efﬁciency but introduces a one-step delay, which can cause problems of numerical instability. These problems are particularly evident when the PV generator is represented by multiple single-diode equivalent circuits, such as in the cases of PV generators composed of different types of arrays or subject to partial shading or interfaced by multilevel inverters. To overcome such problems, in this paper a new approach is proposed to include the PV generator model into EMT simulation. A convergence analysis gives proof of the obtained improvements, which are also conﬁrmed by numerical results. The robustness of the proposed technique is tested by simulation of an IEEE benchmark system in the cases of partial shading and of electric faults.

**Keywords:** Distributed generation, EMT simulation, Grid-connected photovoltaic systems, Photovoltaic generators

## 1. Introduction
In recent years the growing concern for environment preservation has caused a wide spreading of photovoltaic (PV) systems in distribution networks. To derive component ratings, optimise protections, design controllers, evaluate the impact on the distribution system operation, detailed modelling of grid connected PV systems for power system simulation studies is needed.

Research has deeply analysed the models for the components of a grid connected PV system, including equivalent circuits of the PV generator [1–3], conﬁguration and dynamic response of the inverter [4–6], behavior of the grid interface and performance of the control system [7–9]. Other important aspects have been addressed, related to the inclusion of the PV system into the distribution network [10].

In a PV system, the PV generator consists of electrically connected PV modules and it is modelled by physical-oriented equivalent circuits, including one or more diode. The single-diode equivalent circuit is the most commonly used model for large PV generators and it is adopted in this paper. This model introduces a non-linear dependency of the current injected by the PV generator on the voltage at its terminals, which in turn depends on the operating conditions of the whole power system which the PV generator is connected to.

When PV systems are included into the power system simulation, the non-linearities present in the PV generator models require special attention. On one side, they cannot be neglected because they affect the performance of the various components of the PV systems, in particular of the control systems and of the Maximum Power Point Tracker (MPPT) [10]. On the other side, the non-linearities can introduce numerical problems during the power system simulation [11].

From a strict mathematical point of view, in each step of the simulation, the set formed by the non-linear equations representing the PV generators and by the linear equations representing the rest of the power system must be solved, using an iterative numerical algorithm. This approach is adopted by some simulation tools, such as PSpice and Matlab; it is accurate but presents the drawback of a heavy computational burden when simulating large distribution networks including several PV systems. To guarantee computational efﬁciency, some authors have proposed equivalent circuits based on simpliﬁed or linearised equations, thus losing in terms of model accuracy [12–14].

An alternative approach consists of separating the non-linear equations of the PV generators from the linear equations of the rest of the power system. Then, the PV generator models are solved substituting in the non-linear equations the values of voltage and/or current available from the past simulation step [15,16]. This approach can be used in any simulation tool and, in particular, it is adopted by EMTP and EMTDC [17]. It keeps the accuracy of the PV generator model while presenting a computational burden which is comparable with the one of a linear system. Unfortunately,

Ii Rs I

In general, the ﬁve circuit parameters $a$, $I_g$, $I_o$, $R_s$ and $R_p$ are functions of the type of PV device and of the environmental conditions, described by the solar irradiation $G$ and the p–n junction temper-