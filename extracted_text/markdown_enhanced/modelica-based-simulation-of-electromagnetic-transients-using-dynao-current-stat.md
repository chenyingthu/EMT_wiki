# Modelica-based simulation of electromagnetic transients using Dynaωo: Current status and perspectives

A. Masoom a, *, A. Guironnet c, A.A. Zeghaida b, T. Ould-Bachir b, J. Mahseredjian a  
a Department of Electrical Engineering, Polytechnique Montréal, Canada  
b Department of Computer and Software Engineering, Polytechnique Montréal, Canada  
c R&D Department, Réseau de Transport d’Electricité (RTE), Paris, France  

**Keywords:** Modelica, Electromagnetic Transient, Equation-based modeling, Acausal modeling, C++, Declarative modeling, Dynaωo  

**Abstract:** This paper presents the current status, the open challenges, and perspectives for Modelica-based simulation of Electromagnetic Transient (EMT) using Dynaωo environment. The simulation efficiency in native Modelica environments requires improvements for larger-scale systems, as they have been primarily developed and used for complex but small problems. This paper investigates the use of Dynaωo, an open-source hybrid C++/Modelica tool originally developed for large-scale electromechanical transient studies, for electromagnetic transient simulations. It demonstrates that its approach manages to bring improvements in terms of performances while keeping the flexibility, accuracy, and robustness of full Modelica tools, but that there is still room for further improvements.

## 1. Introduction

POWER system electromagnetic transient (EMT) modeling contains a set of components that can be described mathematically by Ordinary Differential Equations (ODE) along with algebraic equations. Synchronous machines, power transformers, surge arresters, or power controllers can be effectively modeled using an evolving set of differential-algebraic equations (DAEs) containing discrete variables.

Modelica is an object-oriented declarative equation-based and open-source language to conveniently model the dynamic behavior of complex physical systems. Modelica is an acausal language, meaning modeling relies on equations instead of assignment statements, where the input-output causality is fixed. As a result, the programmer is not forced to handle the data flow of the solution. Equations are declarative and express relations between expressions; therefore, the equality operator used in the equations defines mathematical equality between the left and right sides of an expression. Modelica language makes modeling physical systems easier and more intuitive. In Modelica, models are described through the implicit DAEs, either created in an equation-based way for physical parts or using a block diagram approach for control parts [1]. This system is then transformed into an explicit ODE form by a Modelica tool, such as OpenModelica [2] or Dymola [3]; then, solved using a freely-selected numerical method. Power system modeling with Modelica allows working at higher abstraction levels than with classical simulation tools whose codes are based on imperative languages, e.g. Fortran or C++.

Modelica has begun to gain interest in the power system community with two European projects: PEGASE [4] and iTesla [5]. These projects, alongside other national or international initiatives coming both from the power system and the Modelica communities, have ended up in the development of several libraries: iPSL [6], OpenIPSL [7], or PowerGrids [8] for phasor-domain simulation. Regarding EMT-type simulations, the first effort in this direction has been done in [9], where Constant Parameter (CP) and Wideband (WB) transmission line models have been implemented and validated against EMTP [10]. The precision obtained with Modelica models and tools is perfect, but the simulation run-time is not satisfactory. Modelica has many built-in functions and constructs covering a vast range of EMT-modeling needs.

Many techniques have been proposed over the years to accelerate the simulation speed in Modelica simulators such as using FPGA [11], solver manipulation [12], DAE-mode compilation, power system specific solvers [13], or efficient Jacobian calculation. Despite these efforts and large improvements, the performance of full Modelica simulators remains a barrier for industrial applications and large-scale systems.

A hybrid C++/Modelica solution called Dynaωo [14, 15] was proposed for simulation in the phasor domain to bypass the limitations encountered with full Modelica tools while ensuring the advantages of an equation-based approach. Dynaωo is an open-source simulation package primarily designed by RTE for short- and long-term stability analysis. It aims at providing a transparent, flexible, interoperable, and robust simulation tool that could ease collaboration and cooperation in the power system community. This method enables to improve the performances to similar levels to domain-specific simulation tools for phasor domain simulations [15].

The contribution of this paper is to draw the status of Modelica-based EMT simulations using Dynaωo, the open challenges, and the perspectives. It presents the extension already done to the method and illustrates with different test cases the results obtained in terms of performances and accuracy.

The remainder of this paper is structured as follows: Section II presents the approach used in Dynaωo, the different models and solvers natively available, and the improvements and remaining challenges associated with EMT simulations. The results and case studies are presented and discussed in Section III.

*Fig. 1. Dynaωo structure and exchanges between solvers and models.*

equations for pending connections (typically currents), to be able to