# An Improved Low-Frequency Transformer Model for Use in GIC Studies
W. Chandrasena, P. G. McLaren, Fellow, IEEE, U. D. Annakkage, Member, IEEE, and R. P. Jayasinghe, Member, IEEE

**Abstract**—A hysteresis model based on the Jiles–Atherton theory is incorporated into a power transformer model in an electromagnetic transient program (EMTP)-type program. The eddy current effects are also included in the same model. Comparisons are made between recorded and simulated waveforms using a single-phase distribution transformer. A good agreement is achieved between recorded and simulated data.
**Index Terms**—Eddy currents, hysteresis, losses, power transformers, simulation.

## I. INTRODUCTION
GEOMAGNETICALLY induced currents (GICs) are the ground effect of a complicated space weather chain that originates in the sun. The flow of GIC through power transformers has been the root cause of operational and equipment problems in power systems during a geomagnetic disturbance or geomagnetic storm [1].

At steady state, the magnetizing current of a power transformer is generally insignificant to the operation of power systems. However, during a GIC event current that flows through grounded-wye transformers results in a quasi dc current in the transformer high-voltage windings and, hence, results in severe half cycle saturation. Because of the half-cycle saturation, the transformer draws a large asymmetrical exciting current and it results in increased reactive power consumption as well as the generation of significant levels of harmonic currents [1]–[4]. The extent of the half-cycle saturation also depends on the history of the state of the magnetic core. Therefore, an electromagnetic transient simulation to analyze the effects of GIC on power systems requires accurate representation of the magnetizing characteristics of transformers. The correct representation of the hysteresis loop is important so that it handles long-term remanence and recoil loops [3]. In short time simulations, the piecewise linear solutions of saturation can give the impression that they handle remanence because the system time constants maintain the magnetization over several hundreds of milliseconds. However, over time scales of seconds, the flux will decay to zero. It is usually possible to initialize the remanence in a typical transformer model; however, it requires outside intervention whereas our method presented in this paper will do it automatically.

During the past decade, a considerable effort has been devoted to the development of simulation models of power transformers [5]–[9]. These models contain a wide range of modeling details of the iron core of the transformer with varying degree of complexities.

There have been numerous approaches to modeling ferromagnetic hysteresis loops. A bibliographic review of the hysteresis models presented during the past three decades is given in [10]. Many of these attempts are curve fits, which ignore the underlying physics of the material behavior. At the other extreme, micromagnetic methods consider all known energies on a very small scale and find the domain configuration that gives the minimum energy. In general intermediate solutions models, which can relate microstructural parameters to the macroscopic responses of the material to outside fields, are more suitable for time-domain simulations [11]. Four magnetization models are now considered as classical. They are the Stoner–Wolhfarth model, the Jiles–Atherton (JA) model, the Globus model, and the Preisach model. The methods each model uses to simulate the magnetization mechanisms, their advantages, and disadvantages are discussed in [11].

This paper describes a hysteresis model based on the JA phenomenological model of a ferromagnetic material [12]. This has been used in [13] in the simulation of current transformers, and it has been shown that the hysteresis model based on the JA theory accurately represents the remanence flux in the transformer cores.

There exists a wide variety of representations for hysteresis and eddy current losses in transformer models used for power system transient studies. The most commonly used method to represent losses is to add a shunt resistance across one winding as in [7]. A frequency-dependent resistance matrix is used in [14] to model the effects produced by eddy currents. A different approach is used in [15], where the relationship between an equivalent eddy current field and the rate of change of flux density has been experimentally obtained to represent losses in current transformers. In the model presented in this paper, we have extended the hysteresis model based on the JA theory to incorporate the effects of classical eddy current loss and excess or anomalous loss [16]–[18].

The simulation model of a single-phase two winding transformer is presented to describe the details of the new hysteresis model. However, this algorithm is capable of representing the hysteresis characteristic of a multilimb multiwinding transformer. The new transformer model was implemented in the electromagnetic transient simulation program EMTDC.

In the present study, the winding capacitance is neglected, because the GIC phenomena studied are of low frequency. Thus, the transformer core model presented in [9] was used as the basis of this work.

Manuscript received December 13, 2002. This work was supported by Manitoba Hydro.
W. Chandrasena and U. D. Annakkage are with the Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB R3T 5V6, Canada.
P. G. McLaren is with the Center for Advanced Power Systems, Florida State University, Tallahassee, FL 32310 USA.
R. P. Jayasinghe is with Manitoba HVDC Research Centre, Winnipeg, MB R3J 3W1, Canada.
Digital Object Identifier 10.1109/TPWRD.2004.824429

## II. REVIEW OF THE TRANSFORMER CORE MODEL
A brief review of the transformer core model described in [9] is presented in this section, and it also explains