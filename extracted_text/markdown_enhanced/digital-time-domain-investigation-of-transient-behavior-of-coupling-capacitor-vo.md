## TIME-DOMAIN MODELING OF COUPLING CAPACITOR VOLTAGE TRANSFORMER

**M.R. Iravani, X. Wang**  
Department of Electrical and Computer Engineering  
University of Toronto  
Toronto, Ontario, Canada M5S 364  

**I. Polishchuk, J. Ribeiro**  
Haefely-Trench  
390 Midwest Road  
Scarborough, Ontario, Canada M1P 3B5  

**A. Sarshar**  
Haefely-Trench  
71 Maybrook Drive  
Scarborough, Ontario, Canada M1V 4B6  

**Abstract**—This paper reports a set of digital time-domain simulation studies conducted on TEHMP161A Coupling Capacitor Voltage Transformer (CCVT) of Haefely-Trench. The Electro-Magnetic Transients Program (EMTP) is used to develop the CCVT model and conduct the transient studies. The accuracy of the CCVT model is verified through comparison of the EMTP simulation results with those obtained from test results. The investigations demonstrate that the developed model can accurately predict CCVT transient response, e.g. the phenomenon of ferroresonance. The model is developed (1) to determine impact of transients on CCVT response, (2) to design, optimize and compare protective and ferroresonance suppressor devices of CCVT, and (3) to predict CCVT transient response on power system monitoring and protection schemes.

**Keywords:** CCVT, Ferroresonance, Simulation, EMTP, Protection, Relaying.

## 1. INTRODUCTION

CCVT is a well known apparatus to transform high-voltage (input) to low-voltage levels (output) at which monitoring devices and protection relays operate. Theoretically, the output waveform should be an exact replica of the input waveform under all operating conditions. Under steady-state conditions, this requirement can be satisfied based upon proper design and tuning of the CCVT. However, under transient conditions, e.g. faults and switching incidents, the CCVT output waveform may deviate from the input waveform due to the impacts of capacitive, inductive and nonlinear components of the CCVT [1,2]. Therefore, fidelity of CCVT during transients must be well known and quantified [3]. The other concern is thermal overstress and consequently deterioration of CCVT components due to its internal transient phenomena, e.g. the phenomenon of ferroresonance.

To address the above issues, the Instrument Transformer Division (ITD) of Haefely-Trench and the University of Toronto have embarked upon development of a comprehensive digital time-domain model of CCVT systems. The model is developed based on the use of the EMTP. The objectives of this joint project are:
- To evaluate, compare and quantify impacts of CCVT component parameters and protective/suppressive devices on its transient response, e.g. the phenomenon of ferroresonance.
- To predict and quantify impact of CCVT transient behaviour on protection systems.
- To investigate impact of power system transients, e.g. faults and planned/unplanned switching incidents, on CCVT transient behaviour.

Salient feature of the developed model as compared with the reported models [4,5,6,7,8] is that it represents details of (1) CCVT step-down transformer including its saturation characteristic and tap positions, (2) CCVT series reactor including its tap positions, (3) CCVT protective devices, (4) ferroresonance suppressor circuitry, and (5) various burden models. Due to space limitation, this paper only reports some of the studies conducted on TEHMP161A CCVT model of Haefely-Trench and highlights the conclusions.

The rest of this paper is organized as follows. Section 2 introduces TEHMP161A CCVT system used for the reported studies. Section 3 reports the results of the frequency-domain studies carried out on the CCVT system. Section 4 compares the EMTP simulation results with the test results and verifies the accuracy of the developed model. Section 5 reports the CCVT response to various simulated transient scenarios. Conclusions are summarized in Section 6.

## 2. TEHMP161A CCVT CIRCUITRY

Figure 1 shows schematic diagram of the CCVT circuitry. Switches S1, S2, S3 and S4 are not part of the CCVT circuitry, and included in the EMTP model to simulate various transient scenarios imposed on the CCVT. Major CCVT components of Fig. 1 are: voltage divider C1 and C2, drain coil Ld, step-down transformer (SDT), series reactor, harmonic suppression filter, protective device, and burden. Capacitors Cm, Ct and Cc are lumped representations of stray capacitances of STD and series reactor. STD and series reactor have multiple tap positions which are not identified on Fig. 1, but have been included in the EMTP model. Various protective devices examined for the CCVT system of Fig. 1 are: MOV, triac and spark-gap. The EMTP provides basic functions and component models to construct required models of the above protective