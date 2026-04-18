Proximity effect in fast transient simulations of an underground transmission cable

U.S. Gudmundsdottir  
Department Manager for HV Cables in Wind Power Systems at DONG Energy, 7000 Fredericia, Denmark  
Tel.: +45 99557429.  
E-mail address: unngu@dongenergy.dk

## Abstract
It has been discussed in various papers, how lack of proximity effect in modelling affects simulations and gives inaccurate results at high frequencies. This paper describes a method for how to include the proximity effect calculations in EMT-based simulations. A subdivision of conductors method is used to calculate conductor (core and sheath) impedances. A full phase impedance matrix is then constructed, including semiconductive layers, insulation layers and a special screen of two conducting materials. Finally the method is tested using the universal line model and is verified against field measurements. It is shown in the paper how including the proximity effect, it is possible to obtain good comparison between measurements and simulations, even for the intersheath mode.

**Keywords:** Insulated cables, Conductor partitioning, Geometric mean distance, Model verification, Proximity effect, EMT simulation

## 1. Introduction
Nowadays, extruded (XLPE) cables are the most common cable types in high voltage (HV) underground cable systems. The XLPE cable type has the advantage of having no need for auxiliary equipment and no risk of leakage as the insulation is homogeneous and without any type of fluids. For studies of cable systems, such as insulation co-ordination, it is crucial to have accurate models.

EMT-based simulations for transient studies of cable lines use the Cable Constants (CC) method for calculating series impedance and shunt admittance of the cable [1]. Although very accurate for most studies, the equations in the CC method do not include the proximity effect.

It has been discussed in [2] how lack of proximity effect can cause inaccurate simulations. It has furthermore been shown in [3] how, for the intersheath mode of propagation [4], there is inadequate damping of the signals for higher frequency oscillations (10 kHz and above). This is because of wrong imaginary part of the series impedance in the simulation which can be explained by the lack of including the proximity effect in the simulation software.

An analysis of a deviation between field measurements and simulation results has revealed how the wired part of the sheath conductor (also called metal screen) should be more accurately represented in the simulation software [3]. The analysis revealed how the wired characteristics of the metal screen of the HV cable and the proximity effect should be included in the series impedance calculations.

This paper describes the properties of an XLPE cable and addresses how the proximity effect can be modelled in detail in order to have more precise simulation results. Furthermore, in this paper, the improved modelling procedure is verified against field measurements and compared to CC method calculations.

## 2. Proximity effect variables
When AC currents flow in a conductor, the resulting magnetic flux will be time varying. When the frequency increases, the magnetic flux $d\Phi/dt$ will vary more, resulting in larger eddy currents of adjacent conductors. Therefore, the higher the frequency, the stronger the proximity effect. An example of proximity effect is shown in Fig. 1.

A HV single core XLPE cable often has a metal screen consisting of Cu wires and Al laminate, as shown in Fig. 2. The reason for this is radial water tightening. Without the Al laminate, there is a higher risk of the inner insulation becoming in contact with water.

Due to the wire part of the screen, the proximity effect for wires with the same current direction causes the current distribution in the screens to be more non-homogen. This changes the series impedance of the cable at the higher frequencies and causes more damping. Furthermore, as the intersheath part of the cable current propagates between the screens of adjacent cables, their propagation characteristics are also affected by proximity effects between

**Fig. 1.** Current distribution because of proximity effect for two adjacent conductors carrying current in the same direction and in opposite direction.

**Fig. 3.** Distribution of elements and element types for subdivision of conductors.

Based on this, the universal line model then fits $Y_c$ and $H$. The universal line model is setup by The Manitoba HVDC Research Centre (owner and distributor of EMTDC/PSCAD). This has then been manipulated, su

1. EMT: electromagnetic transients.