## Electromagnetic Modeling of Transformers in EMT-Type Software by a Circuit-Based Method
Sadegh Rahimi Pordanjani, Mohammed Naïdjate, Nicolas Bracikowski, Mircea Fratila, Jean Mahseredjian, Fellow, IEEE, and Afshin Rezaei-Zare, Senior Member, IEEE

Manuscript received 21 December 2021; revised 31 March 2022; accepted 9 May 2022. Date of publication 23 May 2022; date of current version 28 November 2022. Paper no. TPWRD-01906-2021. (Corresponding author: Sadegh Rahimi Pordanjani.)

Sadegh Rahimi Pordanjani is with the Department of Electrical Engineering, Polytechnique Montreal, H3T 1J4 Montreal, Canada (e-mail: sadegh.rahimi-pordanjani@polymtl.ca).
Mohammed Naïdjate is with CRTT, University of Nantes, 44035 Saint Nazaire, France (e-mail: mohammed.naidjate@univ-nantes.fr).
Nicolas Bracikowski is with IREENA Laboratory, Nantes University, 44035 Saint Nazaire, France (e-mail: nicolas.bracikowski@univ-nantes.fr).
Mircea Fratila is with THEMIS, EDF Lab Paris-Saclay, 91120 Palaiseau, France (e-mail: mircea.fratila@edf.fr).
Jean Mahseredjian is with Ecole Polytechnique, H3T 1J4 Montreal, Canada (e-mail: jean.mahseredjian@polymtl.ca).
Afshin Rezaei-Zare is with the Electrical Engineering and Computer Science Department, York University-Keele Campus, M3J 2S5 Toronto, Canada (e-mail: rezaei@yorku.ca).

Color versions of one or more figures in this article are available at https://doi.org/10.1109/TPWRD.2022.3177137.
Digital Object Identifier 10.1109/TPWRD.2022.3177137

## Abstract
This work proposes a fully circuit-based method for modelling electrical transformers. This method not only offers the advantages of circuit-based methods and can be implemented in electromagnetic transient (EMT) type software, but it can also provide a detailed representation of transformers, comparable to the finite element method (FEM). The proposed method enables a detailed geometrical modelling, as well as representation of magnetic flux paths and consideration of iron core saturation. It can be implemented in EMT-type software to see the effect of power networks on transformers. In addition, the proposed method can represent internal faults in transformers. The problem is constrained to a 2-D domain, which is often used in FEMs to represent the magnetic behavior of power equipment. Finite element analysis based on ANSYS Maxwell is used to verify the proposed method.

**Index Terms**—Transformer model, electromagnetic transients, magnetic circuits, finite element method (FEM), winding fault.

## I. INTRODUCTION
Magnetic devices such as transformers and rotating electrical machines play a critical role in power systems. In order to accurately simulate phenomena like inrush currents, internal faults, ferroresonance and harmonic generation, detailed modelling of magnetic devices is a key issue in power system transient simulations. It is also critical for designers to examine how the external network affects magnetic device internal behavior. Circuit simulators and field solvers are two common tools used to carry out these analyses.

EMT-type software, such as EMTP [1], employ lumped parameter approaches to model transformers. Topological transformer models [2]–[5] are the most common lumped parameter models employed in EMT-type software. In fact, existing topological transformer models are best suited for situations where the model’s input data is test based, such as open-circuit and short-circuit tests, for example. Despite the significant gains achieved to make these models more physically meaningful [6], [7], they are unable to account in detail for internal behavior of magnetic effects, including local magnetic saturation and local magnetic flux leakages, since they use a limited number of elements to represent flux paths.

A finite element method (FEM) [8] can accurately account for material nonlinearity, geometrical complexity, and material anisotropy, making it ideal for representing completely the magnetic device internal behavior [9]. Field solvers, on the other hand, lack the variety of power system components needed to simulate a practical power network comprising control systems, surge arresters, circuit breakers, and multiphase transmission lines. To address this issue, the solutions of field equations and circuit equations can be combined with each other. In the combination of circuit-based methods and FEM, 2-D FEM is usually the method of choice for predicting magnetic behavior in power equipment, due to the difficulty of 3-D, which derives from the complexity of the geometry and time-consuming challenges.

Two strategies are used to combine the solutions of field equations and circuit equations: direct and indirect.

The direct method combines and solves simultaneously field equations and circuit equations [10]. To solve the magnetic equations, a formulation involving the magnetic vector potential is used. The conductor current is expressed in terms of current density, and the flux linkage is determined from the potential vector to establish the coupling. Step-by-step numerical integration is used to solve the time-dependent differential system that results from coupling. A Newton–Raphson iterative approach is utilized to account for the magnetic and electric nonlinearities. However, because it cannot provide enough network component models, this strategy is not ideal for complicated and large power networks.

The indirect method allows the FEM-based model and EMT circuit portions to be treated separately while maintaining connection via coupling coefficients [11]. In contrast to direct methods, indirect methods can be used to study the behavior of magnetic devices in vast power networks with a variety of component models. Because the solved equations are nonlinear, the indirect techniques require numerous iterations between the field and circuit sections, which significantly deteriorates computational performance. Although both coupling-based approaches can be quite accurate, their main disadvantages are e