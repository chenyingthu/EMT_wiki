## Earth Return Impedances of Conductor Arrangements in Multilayer Soils—Part II: Numerical Results
**Dimitrios A. Tsiamitros, Member, IEEE, Grigoris K. Papagiannis, Member, IEEE, and Petros S. Dokopoulos, Member, IEEE**

**Abstract**—The influence of earth stratification on the conductor impedances is investigated in this paper. The generalized expressions for the self and mutual impedance of conductors in the multilayer earth case, which have been derived in a companion paper, are implemented on typical overhead power transmission lines and underground single-core power cable arrangements for discrete and exponential variations of earth resistivity. The accuracy of the results over a wide frequency range is justified by a proper finite-element method formulation. The differences in the impedances due to earth stratification are presented. The influence of the earth stratification on the actual transient responses of the conductor arrangements is also investigated.

**Index Terms**—Electromagnetic transient analysis, finite-element method (FEM), nonhomogeneous earth, power cables, transmission-line modeling.

*Manuscript received July 20, 2007; revised January 25, 2008. First published June 27, 2008; current version published September 24, 2008. Paper no. TPWRD-00454-2007.*
*The authors are with the Department of Electrical and Computer Engineering, Power Systems Laboratory, Aristotle University of Thessaloniki, Thessaloniki GR-54124, Greece (e-mail: grigoris@eng.auth.gr).*
*Digital Object Identifier 10.1109/TPWRD.2008.923999*

## I. INTRODUCTION
In transient simulations, detailed transmission-line modeling is required. The model parameters are strongly influenced by the resistive earth return path. In a companion paper [1], a solution of the electromagnetic-field equations is presented for arbitrary conductor configurations expanding along one direction, including the presence of multilayer earth. This solution leads to the derivation of general expressions for the calculation of the influence of multilayer earth structures on the conductor self and mutual impedances. These expressions contain complex semiinfinite integrals which are evaluated numerically using a suitable integration scheme.

In this part, the derived expressions are applied in cases of actual overhead power transmission lines, underground single-core (SC) power cable arrangements, as well as a combination of both. Several multilayer earth structures, based on actual measurements, are combined with the aforementioned conductor configurations. The accuracy of the obtained numerical results is justified with comparison to the corresponding results from the application of a proper finite-element method (FEM) formulation, over a wide frequency range. To check the influence of earth stratification, the calculated impedances are compared to the ones corresponding to homogeneous earth structures. Finally, for each case of conductor arrangement and soil type, the calculated impedances are used in the simulation of typical electromagnetic transients to investigate their impact on the transmission-line transient response.

## II. CONDUCTOR ARRANGEMENTS
### A. Overhead Power Transmission Lines
The proposed expressions and the numerical integration method are applied in two typical overhead line configurations, namely a single circuit 150-kV transmission line shown in Fig. 1(a) and a double-circuit 735-kV line with a single conductor per phase shown in Fig. 1(b).

Data for the first line were obtained from [2]. The transmission-line data appear in Table I.

| **TABLE I** |
| :--- |
| TRANSMISSION-LINE DATA |

### B. Underground Power Cables
Two cases of SC cables are examined. First, three SC cables with the core and one insulation layer are simulated in the horizontal cable arrangement of Fig. 2(a) as in [3]. Cables are in a depth m with a spacing of m. The core radius is m, while the outer radius is m.

| **TABLE II** |
| :--- |
| DATA OF THE SC CABLE ARRANGEMENT OF FIG. 2(b) |

Fig. 2. (a) Horizontal SC cable arrangement. (b) SC cable with core and sheath.

## III. MULTILAYER EARTH STRUCTURES
### A. Two-Layer Earth
First, a two-layer earth configuration is considered. Six different two-layer earth models are investigated, based on actual grounding parameter measurements [5]. The corresponding data for the layer depths and resistivities are shown in Table III. The second layer is of infinite extent. Since most soil types are nonmagnetic, the relative permeability of the earth is assumed to be equal to unity. On the other hand, typical values for the relative earth permittivity are close to 10. However, observing the form of the proposed formulas of Part I for the per unit length mutual impedance, the relative earth permittivity appears only in the propaga