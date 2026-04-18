## Duality Derived Transformer Models for Low-Frequency Electromagnetic Transients – Part I: Topological Models

S. Jazebi, S. E. Zirka, M. Lambert, A. Rezaei-Zare, N. Chiesa, Y. Moroz, X. Chen, M. Martinez-Duro, C. M. Arturi, E. P. Dick, A. Narang, R. A. Walling, J. Mahseredjian, J. A. Martinez, and F. de León

**Abstract**-- The objective of this two-part paper is to provide clarity to physical concepts used in the field of transformer modeling, to dispel common misconceptions regarding numerical instabilities, and to present unified modeling techniques for low-frequency transients. The paper focuses on proper modeling of nonlinearities (magnetizing branches), since these components are critical to determine the low-frequency behavior. A good low-frequency model should properly represent: normal operation, inrush currents, open and short circuit, out-of-phase synchronization transient of step-up transformers, geomagnetic induced currents, ferroresonance, and harmonics. This Part I of the paper discusses the derivation of electrical dual models from both the equivalent (magnetic) reluctance networks and the direct application of the principle of duality. It is shown that different dual models need to be derived for different transformer geometries and the advantages and disadvantages of each method are discussed. The paper also compares double-sided versus single-sided dual models, and shows that the double-sided model is a more general approach. The mathematical equivalency of several leakage models (negative inductance, mutual coupling, and BCTRAN) is demonstrated for three-winding transformers. It is also shown that contrary to common belief a negative inductance is not the source of numerical oscillations, which are due to the use of non-correct topological models for representing the core.

**Index Terms**—Electromagnetic transients, duality models, low-frequency transients, negative inductance, numerical oscillations, topological models, transformers, transformer modeling.

S. Jazebi and F. de León are with the Department of Electrical and Computer Engineering, New York University, Six Metrotech Center, Brooklyn, NY, 11201 (e-mails: jazebi@ieee.org, fdeleon@nyu.edu).

S. E. Zirka and Y. Moroz are with the Department of Physics and Technology, Dnepropetrovsk National University, Ukraine, 49050, Dnepropetrovsk, Gagarina.72 (e-mail: zirka@email.dp.ua).

M. Lambert and J. Mahseredjian are with the Department of Electrical Engineering, École Polytechnique de Montréal, Montréal, QC, H3T 1J4, Canada (email: mathieu.lambert@polymtl.ca, jean.mahseredjian@polymtl.ca).

A. Rezaei-Zare and A. Narang are with Hydro One Networks Inc., 483 Bay St., 13th Floor, Toronto, ON, Canada (emails: Afshin.Rezaei-Zare@HydroOne.com, Arun.NARANG@hydroone.com).

N. Chiesa is with Statoil, NO-7005 Trondheim, Norway (

## I. INTRODUCTION

TRANSFORMERS are essential components of the power system. Computer modeling and simulation of these devices are complicated because of the interactions of the electric and magnetic fields in a multi-media and non-linear environment (typically iron, oil, paper, and copper). Power transformers behave differently when subjected to the variety of excitations that they face during their lifetime. Accurate transformer models compatible with Electromagnetic Transient Programs (EMTP-type) are of interest for power system modelers. Ideally, a transformer model should be built using the capabilities already available in EMTP-type tools.

The principle of duality is recognized as a physically correct technique to obtain circuital models of power transformers. This technique was first introduced for transformers by Cherry [1] and further developed to include nonlinearities by Slemon [2], [3]. The main advantage of this method is that the physical magnetic circuit of an electromagnetic device can be converted to its dual electric circuit suitable for simulation in EMT-type programs, using standard circuit elements. Duality models are able to describe the distribution of magnetic flux in the core and windings. Therefore, they are capable of providing useful information of the electromagnetic behavior of all transformer construction elements.

There exist other modeling possibilities to represent the physics of magnetic circuits in time domain simulations: bond graphs [4], [5], magnetic circuit equations [6], [7], gyrator-capacitors [8]-[11], and mutators [12]. Some of these techniques are difficult to implement in EMTP-type programs. An implementation of mutators using commonly available coupled R-L branches has been recently proposed [12], which allows an easy representation of magnetic circuits, offering an alternative to the use of the duality transformation.

A unified and generally accepted model for transformers