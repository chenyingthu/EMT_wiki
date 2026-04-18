# Fitting the frequency-dependent parameters in the Bergeron line model
Pablo Torrez Caballero, Eduardo C. Marques Costa ∗, Sérgio Kurokawa
UNESP – University Estadual Paulista, Faculdade de Engenharia de Ilha Solteira – FEIS, Departamento de Engenharia Elétrica, Ilha Solteira, SP, Brazil

## Abstract
A new transmission line modeling – TLM is proposed based on the well-established Bergeron method. The conventional Bergeron model is characterized by the line representation through concentrated longitudinal and transversal parameters, i.e., the line electrical parameters are represented by means of electric circuit elements R, L, G and C. The novel approach of this research is the inclusion of the frequency effect in the longitudinal parameters in the Bergeron line representation. This new feature enables to extend the application of the Bergeron method for simulations of transients composed of a wide range of frequencies.

## Keywords
Bergeron line model
Transmission line modeling – TLM
Electromagnetic transients
Time-domain analysis
Frequency-dependent parameters
Power system modeling

## 1. Introduction
In general terms, the mathematical modeling of dynamic systems is a simplified and practical method to define initial and boundary conditions for the first step on real projects which are extended since electronic devices, for the most variable applications, up to complex power systems. Thus, the continuous improvement and creation of new computational tools to simulate this “first step” are definitely not outdated.

Initially, a brief review on transmission line modeling – TLM is described emphasizing the current state of the art and the main problems in the area.

There are several transmission line models available in the technical literature to study electromagnetic transients in power transmission systems. Basically, these models may be classified into two general groups: by lumped parameters and by distributed parameters.

In the first group, transmission lines are modeled from the representation by lumped elements, i.e., line is modeled by an equivalent representation by means of resistive, inductive and capacitive circuit elements. These models are developed directly in the time domain and are easily integrated to other time-variable power elements, also modeled in the time domain, such as: capacitors, relays, non-linear loads and many other power components. Since the electrical behavior of most power components are well-known in the time domain, this characteristic represents one of the main advantages in TLM by lumped elements [1].

The line modeling by distributed parameters is developed directly from the frequency-dependent parameters based on the line representation by a two-port circuit in the frequency domain. From this approach, the line modeling and simulations are carried out in the frequency domain and time-domain results are obtained using inverse transforms [2]. The frequency-dependent parameters of the line are accurately represented using frequency-domain models; however, these models have restrictions for inclusion of time-variable elements in the simulation process, since most power components are well known and easily modeled in the time domain [3].

Despite line models by lumped elements are developed in the time domain, the frequency effect on the longitudinal parameters can be included in the line modeling using fitting methods [4]. New frequency-dependent models by lumped parameters have been recently published in the technical literature on power system modeling. These models are developed directly in the time domain from the line representation by cascade of $\pi$ circuit and the frequency effect on the electrical parameters is modeled by fitting the rational functions $R_{\text{fit}}(\omega)$ and $L_{\text{fit}}(\omega)$ (resistance and inductance) based on the longitudinal impedance of the line, $Z(\omega)$, properly calculated taken into account the earth-return impedance (soil effect) and the skin effect on the cables. The frequency-dependent line model described in reference [5] shows to be robust and accurate for the most of transient conditions on a conventional power transmission system. However, depending of the transmission system characteristics (source, line and load) and transient conditions, the frequency-dependent model based on cascade of lumped elements shows to be costly in computational terms, depending of the quantity of line equivalent segments used in the cascade and total simulation time. Furthermore, some hard unbalanced conditions lead to discrete inaccuracies, because the multi-phase modeling is based on the intrinsic use of a constant and real transformation matrix to calculate each propagation mode of the line. Thus, the line representation by frequency-dependent cascade of $\pi$ circuits shows to be efficient for several situations; however, some difficulty in the modeling and inaccuracies are observed for specific cases. From this last statement, the current research proposes a new time-domain line model based on the well-known Bergeron method and using the same fitting procedure applied in the line model referred in [5].

*Fig. 1. Equivalent impedance circuit of the Bergeron line model.*