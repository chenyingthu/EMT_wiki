# Simulation of electromagnetic transients with Modelica, accuracy and performance assessment for transmission line models

**Alireza Masoom**$^{a}$, **Tarek Ould-Bachir**$^{b}$, **Jean Mahseredjian**$^{*,a}$, **Adrien Guironnet**$^{c}$, **Ni Ding**$^{c}$

$^{a}$ Department of Electrical Engineering, Polytechnique Montréal, Canada  
$^{b}$ Department of Computer Engineering and Software Engineering, Polytechnique Montréal, Canada  
$^{c}$ R&D Department Réseau de Transport d’Electricité (RTE) Paris, France  

**Keywords:** EMT-type simulation, Equation-based modeling, Modelica, Power system transients

**Abstract**  
Electromagnetic Transient (EMT) simulation tools are typically developed using an imperative language. It is typically required to code the models using a specific numerical integration method and following existing solution algorithms. On the other hand, modern high-level, acausal and equation-based programming languages, such as Modelica, allow to formulate models that are easy to read, understand and develop by expressing what needs to be computed without stating how it should be computed. In this paper, the application of Modelica to EMT modeling is demonstrated and the benefits of the language for EMT-type simulations is established. This is done by using the declarative language concept for the development of two models, namely the Constant Parameter (CP) and the Wide-Band (WB) models. Two case studies are presented and used to validate the models and to compare accuracy and performance.

## 1. Introduction and motivation
EMT simulation tools are intended for high frequency transient studies such as over-voltages, inrush currents, relay settings and insulation coordination in power systems. For these studies, harmonics, non-linearities and unbalanced network conditions must be taken into consideration [1]. EMT-type software tools, such as EMTP [2], use imperative programming languages (FORTRAN, C, C++...) for modeling and simulation of power system transients. Such a program has a closed architecture and uses many cryptic code lines to meet the requirements of actual solution mathematics which eventually become almost impossible to visualize; moreover, the languages are ill-suited to human abilities for dealing with complexity [3]. It must be noted that the classical EMT-type software programming maintains significant computational performance advantages due to its specific programming methods and mathematics.

Declarative programming approaches have been widely used in such domains as automotive, buildings or thermal problems, for solving complex physical system simulations. The declarative programming paradigm allows to set the focus on what needs to be computed, instead of how it should be computed, and helps the modeler to concentrate on modeling rather than problem-solving strategies. Although high-level modeling environments are currently expected to be less computationally efficient than the classic application coding approaches, they help the researcher to develop models with different layouts, for interfacing with different applications and for testing modeling formulations.

Among various declarative languages, Modelica [4,5] has gained international recognition and is now one of the most used and advanced high-level modeling languages. Modelica is a multi-domain, equation-based, object-oriented, declarative language standardized for system-level modeling. Equations have no pre-defined causality; so the simulation engine determines the order in which equations are solved. In Modelica, a set of time-varying Differential-Algebraic Equations (DAE) and discrete equations are used to describe the dynamic behavior of a system [6]. Modelica is a language that needs environments to transform it into executable code and run simulations: there exists different ones - either commercial such as Dymola, Wolfram System Modeler or open-source such as Open Modelica or Dynaωo; thus the repeatability of simulation and decoupling of models from numerical solvers are guaranteed.

Several power system libraries such as iPSL, Open iPSL [7], ObjectStab [8] or PowerGrids [9] have been developed based on Modelica, but their primary focus is on phasor-domain studies computations applicable to the simulation of electromechanical transients. To our best knowledge, except for the PowerSystems library [10] which is intended for modeling of electrical power system at transient and steady-state mode, there is almost no literature for the application of Modelica to the simulation of faster electromagnetic transients.

This paper investigates the implementation of Modelica based EMT-type simulation tool and explores the related challenges. Multiphase CP and WB line/cable models are implemented with the Modelica language. The models are tested and validated against EMTP for accuracy and computational performance. The paper is organized as follows: Section 2 recollects WB and CP line model equations, Section 3 presents their implementation in Modelica and Section 4 presents test cases and

*Fig. 1. Schematic of transmission line with length $\ell$.*

*Fig. 2. (a): Distributed parameter lossless CP line model for TD calculations (b): Lossless CP line model with lumped resistance included.*

### 2.1. Constant parameter line model
One of the simplest approaches for line modeling is to neglect losses and frequency dep