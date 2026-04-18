# Acceleration of electromagnetic transient simulations in modelica using spatial data locality
A. Masoom $^{a,*}$, T. Ould-Bachir $^{b}$, J. Mahseredjian $^{a}$, A. Guironnet $^{c}$

$^{a}$ Department of Electrical Engineering, Polytechnique Montréal, Montréal, Canada
$^{b}$ Department of Computer Engineering, Polytechnique Montréal, Montréal, Canada
$^{c}$ Department of Research and Development, Réseau de Transport d’Électricité, Paris, France

**Keywords:** Modelica, Acausal modeling, Data locality, Electromagnetic transients, Transmission line modeling, IEEE 39-bus Benchmark

**Abstract:** This paper presents a new approach to boost the performance of Modelica-based electromagnetic transient (EMT) simulations by improving the data spatial locality of the wideband (WB) and constant parameter (CP) line models. In this approach, the transmission line (TL) models of a network, which account for an important portion of large-scale electrical networks, are clustered into a line block model to increase the data locality of the computations. The paper also investigates the advantage brought by passing the computations of the delay function of the line models to an external vectorized C code. The accuracy and performance of the proposed method are validated using the IEEE 39-bus benchmark. The results show an improvement in the simulation times compared with the conventional Modelica approach.

**Abbreviations:** CP, Constant Parameter; DAE, Differential-Algebraic Equation; EMT, Electromagnetic Transient; EMTP, Electromagnetic Transients Program; MSEMT, Modelica Simulator of Electromagnetic Transients; TL, Transmission Line; WB, Wideband.
* Corresponding author.
E-mail addresses: alireza.masoom@polymtl.ca (A. Masoom), tarek.ould-bachir@polymtl.ca (T. Ould-Bachir), jean.mahseredjian@polymtl.ca (J. Mahseredjian), adrien.guironnet@rte-france.com (A. Guironnet).

https://doi.org/10.1016/j.epsr.2022.108577
Received 3 October 2021; Received in revised form 16 April 2022; Accepted 2 July 2022
Available online 9 July 2022
0378-7796/© 2022 Elsevier B.V. All rights reserved.

## 1. Introduction
Classical EMT-type simulation tools are programmed using imperative programming languages in which values are assigned to functions, the sequence of execution of these functions is declared, as is done for example in C/C+ or Fortran. In such programs, model equations are tightly coupled with numerical solution methods. This characteristic complicates the model development process. The development of equation-based object-oriented declarative languages [1] with a higher level of abstraction such as Omela [2], Simscape [3], and Modelica [4] provide a convenient framework for modelers. In this paradigm, models are coded in terms of differential-algebraic equations (DAE) at high-level abstraction, which significantly eases the actual modeling process.

The Modelica language has become increasingly popular for dynamic physical simulations in the last decade. A lot of work has been carried out for developing the language and enhancing its applications. In the field of power systems, the language was first used for phasor domain studies such as transient stability and short-circuit studies using the libraries such as iPSL [5], PowerGrids [6]. The accuracy and performance of these packages are comparable with the specific domain simulators. Full compatibility with FMI standard [7] including model exchange [8,9] and convenient and efficient co-simulation [10,11] have made the language more popular in the power community. Moreover, Modelica interoperability [4] with the languages C, Python, and Julia mitigates the drawbacks of the language in the simulation of very complex systems [12,13].

Modelica was initially explored for transmission line modeling (i.e., wideband [14], and CP-line models) in [15] for EMT-type simulations. Then the work was developed for the creation of an EMT-detailed library, called MSEMT [16], with a large set of components required for simulation of the IEEE 39-bus and IEEE 118-bus benchmarks [17]. The library includes the synchronous machine model with magnetic saturation and other nonlinear models [18]. In all experiments, the simulation speed of large-scale circuits is recognized as the key drawback in Modelica. The general solutions are based on numerical optimizations, e.g., Jacobian optimization [19] and simulation in DAE mode [20]. A solution was proposed in [21] specifically for power electric simulations based on hybrid coding of Modelica and C++. The solution is tailor-made for EMT simulations and described in [22]. Although it produced a better performance compared with pure Modelica, there is still a gap in comparison with classical EMT-type simulators, such as EMTP® [23]. In most cases, the Modelica built-in delay operator had the main impact on the CPU time [18].

This paper presents a new technique relying on data locality [24] for transmission line modeling to boost the run time performance. Data spatial locality refers to the property of accessing data adjacent to recently accessed data. This technique focuses on cache performance optimization and makes the hierarchical memory layout more profitable to speed up data accesses. In the proposed technique, spatial locality is knowing that:

$$ Z_{mdf} = T_v Z_{mdf,mod} T_v^{-1} \tag{8} $$

$$ Z_{mdf,mod} = Z_{c,mod} + \frac{R_{mod}}{4} \tag{9} $$

$$ \sqrt{\phantom{...}} / ' \tag{10} $$