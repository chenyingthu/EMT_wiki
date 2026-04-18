## Electromagnetic Transient Analysis Using a Frequency Dependent Network Equivalent for Power Systems Integrating Wind Generation Sources

Juan Manuel Verduzco-Durán, Aurelio Medina-Rios, Antonio Ramos-Paz, Rafael Cisneros-Magaña, Julio Cesar Godinez-Delgado

División de Estudios de Posgrado, Facultad de Ingeniería Eléctrica, Universidad Michoacana de San Nicolás de Hidalgo
Ciudad Universitaria, 58030, Morelia, Michoacán, México
juan.verduzco@umich.mx, aurelio.medina@umich.mx, antonio.ramos@umich.mx, rafael.magana@umich.mx, julio.godinez@umich.mx

## Abstract
This article addresses the application of a reduced order representation for analysis of power systems with wind generation sources under fault conditions. A frequency-dependent network equivalent (FDNE) based on a rational function in the discrete-time is used to model the external area of the power system. The characterization of the frequency-dependent terminal admittance at the boundary busbar is carried out through the excitation of a constant voltage source at variable frequency modeled by a multisine signal. Parameter identification techniques based on the recursive least squares method are applied. Regarding the wind energy conversion system (WECS), a type-4 wind turbine based on a permanent magnet synchronous generator with a full-scale back-to-back converter is used. The WECS considers wind fluctuations and output active power generation variations. The performance of FDNE in terms of CPU time and accuracy is compared against to the full-order model response. The results are validated against the response obtained with the PSCAD/EMTDC® simulator.

## Index Terms
Dynamic equivalent, EMT, frequency dependent network equivalent, reduced order representation, parameter identification, wind source.

[1], [5]. The techniques, initially emerging as solution to computational limitations in terms of memory and execution time [6], continue to be relevant today with technological advancements and improvements in computing capacity.

In 1960s, research began on a reduced order representation to analyze electromagnetic phenomena, focusing on frequency dependent network equivalents (FDNE). FDNE are used to approximate modeling the frequency-dependent terminal admittance of a network using an RLC parameter circuit model or a rational function [1], [7]. Hingorani and Burbery pioneered lumped parameter circuit model research in 1970 [8].

A rational function model is used as an adequate approximation to characterize the frequency-dependent admittance observed from a speciﬁc busbar [7]. In [9], the equivalent model is described as a ﬁlter, which is then converted into a Norton equivalent source and integrated into the study area model. This approach is subsequently extended to multiport systems [10]. A comparison of different methods for approximating