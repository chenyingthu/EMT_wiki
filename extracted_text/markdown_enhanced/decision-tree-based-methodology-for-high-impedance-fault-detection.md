# Decision Tree-Based Methodology for High Impedance Fault Detection
Yong Sheng, Member, IEEE, and Steven M. Rovnyak, Member, IEEE

**Abstract**—This paper presents a high impedance fault (HIF) detection method based on decision trees (DTs). The features of HIF, which are the inputs of DTs, are those well-known ones, including current [in root mean square (rms)], magnitudes of the second, third, and fifth harmonics, and the phase of the third harmonics. The only measurements needed in the proposed method are the current signals sampled at 1920 Hz. It will reduce the cost of hardware compared with methods that use high sampling rates. A new HIF model is also used. The data of current signals are from the simulation of Electromagnetic Transients Program (EMTP). The DT algorithm trained can successfully distinguish the HIFs from most normal operations on simulation data, including switching loads, switching shunt capacitors, and load transformer inrush currents. Testing on experimental data is recommended for future work.

The DT uses only feeder current signals as these are standard substation relaying inputs. Also similar to what most researchers did, some of the feeder current harmonics are used in training the DTs. The DTs trained show excellent performance in 100 test cases. This technique is verified with the aid of Electromagnetic Transients Program (EMTP). The proposed method could also be trained using experimental data and those investigations are recommended using some or all of the techniques described in this paper.

**Index Terms**—Arcing, decision trees, EMTP, harmonics, high impedance fault, protection, relay.

## I. INTRODUCTION
A high impedance fault (HIF) is the headache of most utilities for its difficulty of being detected promptly and accurately. For the public safety and the potential huge expenses incurred if sued for any loss or damages resulting from an energized downed conductor [1], [2], utilities often install expensive and sophisticated commercial or self-developed HIF detection devices. Two most commonly installed commercial products are the Digital Feeder Monitor (DFM) from General Electric and the High Impedance Fault Analysis System (HIFAS) from Nordon Technologies [2].

This paper presents a decision tree (DT)-based solution with reasonable cost to utilities. Regarding the implementation, a microprocessor-based controller would perform the proposed DT and the harmonics calculations. The DT for the results reported here has 45 nodes, which was too large to show here but is straightforward to program. Execution of the trained DT algorithm is negligible compared to the harmonics calculations. DTs are to be trained offline from simulation and/or experimental data. DT training is relatively fast so updating with new data is a possibility. If the DT false trips for some reason, the DT could potentially be updated with the samples on which it falsely detected an HIF. The desired output for these samples would be set to no HIF.

Manuscript received September 6, 2002. This work was supported by the Louisiana Board of Regents through the Board of Regents Support Fund under Contract LEQSF(1999-02)-RD-A-25.
The authors are with the Electrical and Computer Engineering Department, Indiana University–Purdue University Indianapolis (IUPUI), IN 46202 USA.
Digital Object Identifier 10.1109/TPWRD.2003.820418

## II. MODEL OF SIMULATIONS
The one-line diagram of a 60-Hz distribution system is given in Fig. 1. Four overhead feeders are connected to a 138/12.5-kV substation transformer, which is served by a 50-km transmission line from a bus considered to be infinite. Assume HIF faults occur near the end of a 5-km feeder that serves an industrial user having a load transformer and 1800 kVar of shunt capacitors.

The loads have a lagging power factor equal to 0.80.

The modeling of most distribution system components is quite straightforward, including infinite source, transmission line, feeders, shunt capacitors, circuit breakers, and loads. For the transformers, BCTRAN, a supporting routine offered by EMTP to improve calculating transformer parameters, has been used to build their models. However, the most difficult model is HIF fault because most HIF phenomena involve arcing, which has not been accurately modeled so far. Some previous researchers have reached agreement that HIF is nonlinear and asymmetric, and modeling should include random and dynamic qualities of arcing. Emanuel et al. presented two dc sources connected in antiparallel with two diodes to simulate zero periods of arcing and asymmetry [3]. Yu and Khan used combinations of nonlinear resistors [4]. Wai and Xia introduced a sophisticated TACS switch controlling the open/close loop of HIF to reach nonlinearity and asymmetry [5]. In this paper, a more dynamic and random HIF model is applied. It combines most advantages of previous models proposed while it remains simple and universal.

The HIF model, as shown in Fig. 2, consists of a nonlinear resistor, two diodes, and two dc sources that change amplitudes randomly every half cycle. Thus, some dynamics and randomness are represented. Changing the mean and standard deviation of the dc source voltage amplitudes could be used to more closely approximate different ground surfaces such as asphalt, sand, or grass. A typical HIF current generated from simulations and its frequency spectrum are shown in Figs. 3 and 4. Compared with real-life HIF current waveforms that are appropriately conditioned and low-pass filtered, such as the one shown in [6, Fig. 8] by Russell and Chinchali, the current waveform in Fig. 3 shows a nearly perfect match.

Fig. 1. One-line diagram of a distribution system for simulations.

Fig.