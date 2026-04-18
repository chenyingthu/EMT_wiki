## Modeling a Mixed Residential-Commercial Load for Simulations involving Large Disturbances
**Bahram Khodabakhchian**  
**Gia-Tong Vuong (Member)**  
Hydro-Quebec, 855 Ste-Catherine St. East, 19th Floor  
Montréal, Québec, Canada H2L 4P5

### ABSTRACT
A detailed EMTP model of a mixed residential-commercial load valid for large voltage variations has been developed. Once validated against field recordings, the model has been used to study the static, dynamic and post-fault recovery characteristics of the real load.

From the simulation results, guidelines for modeling this type of load in dynamic studies such as first swing, transient and voltage stability were established. It is expected that the same methodology applied to other loads of reasonably known composition would guarantee more realistic results than those obtained with current practices.

**Keywords:** Load Modeling, LOADSYN, EMTP Simulation, Transient Stability.

## INTRODUCTION
It has been well established that the load characteristics have a major effect on machine-network interactions, which include first-swing transient stability, small-signal damping, dynamic overvoltages and voltage stability [1]. Moreover, special load modeling efforts were necessary to explain system dynamics during large disturbances such as the one reported in [2].

The development of the LOADSYN [3] computer package provided an easy process for utility engineers to prepare better load models for dynamic studies. However, its models are subject to some limitations, being designed for voltage variations of less than 15% and for frequency fluctuations not greater than 5%.

For the last few years, Hydro-Quebec has been using EMTP beyond the traditional tenths-of-a-second time frame to study dynamic phenomena of up to many seconds, whenever a high degree of accuracy is desired [4]. One of the issues being addressed is a more precise evaluation of the stresses (dynamic overvoltages) imposed on the transmission equipments during severe disturbances capable of causing dynamic instability and system islanding. For this kind of studies, EMTP is considered the most suitable tool because of its ability to simulate harmonics, unbalanced operations and nonlinear phenomena such as corona, transformer saturation and zinc oxide discs conduction. While many sophisticated models which are valid over a wide range of operating conditions have been developed for major network components such as synchronous machines and their controls, little has been done to develop a load model suitable for large voltage and frequency excursions. Assuming that multi-motor models are essential for accurate simulations, and that such models is obviously not practical for large power systems, detailed EMTP simulations have been conducted to confirm the need for better load models and to investigate the prospect of reduced-yet-suitable ones, for EMTP as well as for other tools.

This paper describes the efforts to model a mixed residential-commercial load under severe disturbances, e.g. voltage variations of up to 50%. Such a load is typical for more than two thirds of the total Hydro-Quebec base load. The LOADSYN component-based approach has been adopted, along with its data base.

Using EMTP simulations, the resulting composite model has been validated against field data which were recorded during a severe single-line-to-ground fault, then used to determine the static, dynamic and post-fault recovery characteristics of this type of load.

## FIELD MONITORING SET-UP
An acquisition and identification system for load modeling using natural network variations has been developed and adopted by Hydro-Quebec since 1979 [5]. With this approach, costly test campaigns are no longer required, resident monitoring units are instead installed on a semi-permanent basis where loads need to be modeled. The system has also the merit of providing data covering a much wider range of network conditions, including those which occur in natural events but impractical to reproduce by tests.

In this case, the load to be modeled is that of the Brossard substation, situated at the remote end of a radial line from the Boucherville substation where a monitoring unit has been installed during two years (Fig. 1).

Many events have been recorded, most of them correspond to small variations but a few large disturbances have also been observed. The selected case corresponds to a single-line-to-ground fault which caused a 17.5% drop of the positive sequence voltage. This voltage variation is reproduced in Fig. 2 along with the active and reactive powers.

*Figure 1: Network configuration and location of the monitoring unit*
```
Boucherville
735/1315 kV
Monitoring unit
Brossard
315/25 kV
```

*Figure 2: Voltage, active and reactive power recordings*
```
1.2
1.0
0.8
1.2
320
300
280
260
240
V L-L (kV)
```