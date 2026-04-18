## EMTP MODELING OF ELECTROMAGNETIC TRANSIENTS IN MULTI-MODE COAXIAL CABLES BY FINITE SECTIONS
**Robert J. Meredith**  
Member IEEE  
New York Power Authority, White Plains, New York 10601

**Abstract** -- This paper introduces a way of modeling electromagnetic propagation in conductive materials, termed the method of finite sections. It addresses the issues of modeling frequency-dependent impedances and frequency-dependent coupling of conductors. Its use is demonstrated by application to transient modeling of a multi-mode coaxial cable system in the Electromagnetic Transients Program (EMTP), a situation which currently eludes accurate representation.

In addition to its use in modeling coaxial cables, the method is applicable to modeling of overhead lines, pipe-type cables, transformer cores and walls, lightning arrestors and other situations in which sufficient planar or cylindrical symmetry exists. The method provides the only accurate EMTP means of modeling wave propagation in non-linear resistive and/or inductive Conductors.

**Key Words** -- Electromagnetic propagation, EMTP, transients, frequency-dependency, non-linear, finite sections, pi sections, cables.

## I. INTRODUCTION
EMTP modeling of frequency-dependent resistances and reactances in transformer cores, transmission lines and cables is usually difficult for the typical user to implement, to understand and to verify. An example of this complexity is the approach of J. Marti [1] that has been implemented for transmission line and sometimes cable modeling in various versions of EMTP [2]. Its underlying principles include transformations from phase domain to modal domain, frequency-fitted modal attenuation and re-transformation to phase domain. Unfortunately even this complexity does not work adequately for most cable systems, whose natural propagation modes vary dramatically with frequency and thus are not amenable to use of J. Marti’s constant transform assumption.

At least two other complex approaches in the literature claim to overcome some of the cable modeling problems in J. Marti’s approach. L. Marti [3] claims to be able to vary the modal transform as well as the modal characteristics with frequency. T. Noda, et al [4] claims to be able to work in phase domain, using an “auto-regressive moving average” (ARMA) computational method. Implementation of the L. Marti approach has been less than universal, perhaps due to fundamental technical problems documented in [5]. The T. Noda approach is currently being implemented in at least one version of EMTP, but has not been made generally available as of this writing.

All three of the above approaches start with steady-state impedance scans of the line or cable of interest, which this author believes ignores at least two effects in coaxial cables: wave reflections at the centers of conductors and at the sheath/earth transition, as well as propagation delays in traversing the sheath. The steady-state starting points for the existing methods both fail to recognize the existence of transient conductor surface impedances and, when using (instantaneous) impedance relationships, erroneously assume induced voltages at a distance before electromagnetic waves can propagate through the sheath to those distant points.

The author has concluded that most of the complexity and uncertainties of present frequency-dependent modeling techniques would be eliminated simply by recognizing and modeling wave propagation in the conductors as well as along the dielectrics. He has termed his approach the method of finite sections to reflect its intermediate position between pi-section modeling and finite elements analysis. Coaxial cable modeling represents one of the simpler demonstrations of this method.

## II. MODELING WAVE PROPAGATION
The intrinsic impedance ($\eta$) of any medium is:
$$\eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\varepsilon}} \quad \text{ohms} \tag{1}$$
Here $\omega$ is the frequency in radians/second, $\mu$ is the magnetic permeability in Henry/meter, $\sigma$ is the conductivity in mho/meter and $\varepsilon$ is the permittivity in Farad/meter [6]. The variables $\mu$, $\sigma$ and $\varepsilon$ are analogous to the variables $L$, $G$ and $C$, representing inductance, conductance and capacitance, respectively, and having identical units. The relationship analogous to (1) for the characteristic impedance ($Z_c$) of a lossy-dielectric transmission line is:
$$Z_c = \sqrt{\frac{j\omega L}{G + j\omega C}} \quad \text{ohms}$$

## III. FINITE SECTIONS MODELING
Finite sections modeling, at its simplest manifestation, represents the integration of accurate conductor modeling in transmission pi-section modeling. Fig. 3 shows such an examp