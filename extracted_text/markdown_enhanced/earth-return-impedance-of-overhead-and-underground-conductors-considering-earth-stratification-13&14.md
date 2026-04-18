# Earth Return Impedances of Conductor Arrangements in Multilayer Soils—Part I: Theoretical Model
**Dimitrios A. Tsiamitros, Member, IEEE, Grigoris K. Papagiannis, Member, IEEE, and Petros S. Dokopoulos, Member, IEEE**

**Abstract**—The influence of earth stratification on the conductor impedances is investigated in this paper. A general solution of the electromagnetic-field equations for the case of overhead and underground transmission-line conductors of arbitrary topology and multilayer earth is presented. Generalized expressions for the self and mutual impedances of the conductors are derived. All existing approaches result from the generalized equations, when the corresponding approximations are applied. A suitable integration scheme is also proposed for the calculation of the complex integrals involved in the expressions.

**Index Terms**—Earth conduction, electromagnetic transient analysis, nonhomogeneous earth, transmission line modeling.

*Manuscript received July 20, 2007; revised January 25, 2008. Current version published September 24, 2008. Paper no. TPWRD-00453-2007.*  
*The authors are with the Power Systems Laboratory, Department of Electrical and Computer Engineering, Aristotle University of Thessaloniki, GR-54124 Thessaloniki, Greece (e-mail: grigoris@eng.auth.gr).*  
*Digital Object Identifier 10.1109/TPWRS.2008.923816*

## I. INTRODUCTION
In transient simulations or electromagnetic compatibility studies, detailed transmission line modeling is required. Especially in cases of asymmetrical ground faults or when underground conductors are part of the configuration, the model parameters are strongly influenced by the resistive earth return path. The influence of the lossy earth on conductor impedances has been analyzed since 1926. For the case of overhead lines, proper earth correction terms can be calculated using the widely accepted Carson’s formulas [1]. Similar formulas have been developed by Pollaczek [2], applicable not only to overhead conductor systems but also to cases of underground cables and to combinations of both. In all of these approaches, the earth is assumed to be semi-infinite and homogeneous.

In practice, the earth is non homogeneous. Several techniques have been developed to simulate a nonuniform soil by means of horizontal layers of different earth resistivity [3]–[6]. The parameters of such a multilayered earth model are calculated from the actual earth surface resistivities, which are measured using standard procedures [7].

For the calculation of the earth return impedances in the case of overhead conductors and multilayered earth, the methodologies proposed by Sunde [3], Wedepohl [8], Nakagawa [9], and by the authors [10] can be used. For the case of underground conductors and a two-layer earth, expressions are proposed in [11]. For complex configurations consisting of both overhead and underground conductors and a -layered earth, expressions have been also derived in [12].

All expressions involve complex semi-infinite integral terms, and their calculation is not easy. In [13], an appropriate numerical integration technique is proposed. This technique has been used for the numerical calculation of the earth return impedances of various conductor arrangements [10]–[12].

Scope of this paper is to extend the methodology of [11] and [12] and to present the derivation of generalized formulas, which can be used for the direct calculation of the self and mutual impedances of transmission line conductor arrangements in the presence of a -layer earth. Depending on the soil representation and the conductor configuration, the generalized expressions are simplified into the formulation proposed either in [1]–[3] or in [8] and [9]. The derived expressions contain recursive terms and semi-infinite integrals. These integrals can be evaluated using the numerical integration scheme mentioned above [13].

In a companion paper [14], the numerical results by the generalized expressions are checked against those obtained by a proper finite-element method (FEM) formulation and are used in the simulation of the transient response of some typical transmission line arrangements.

## II. PROBLEM FORMULATION AND SOLUTION
### A. Electromagnetic Field Equations
Fig. 1 shows two conductors and expanding along the axis and a -layer earth structure. The conductors are assumed to be buried in the th and the th layer of the -layer earth, respectively. It will be shown, however, that this assumption does not influence the ability of the derived expressions to represent any other arbitrary conductor configuration along the -axis. The th earth layer is considered to be of infinite depth. The th earth layer has permeability , permittivity , and conductivity . The air is assumed to have conductivity equal to zero and permeability and permittivity equal to those of the free space.

The mutual impedances between the two conductors can be derived by integrating the field due to the conductor dipoles. The field intensities and potentials can be easily expressed in terms of a single vector function , usually referred to as the Hertzian vector [3]. The function has been adopted for the solution of the electromagnetic field equations in this paper, because it is an interface between all the other field quantities. More specifically, the magnetic vector potential and the scalar potential can be expressed as
$$ (1) $$
$$ (2) $$
impedances, the unequal current density on the conductor surface, due to the skin and proximity effects, can be taken into account by means of proper internal impedance terms, which