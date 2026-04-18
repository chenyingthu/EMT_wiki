# Hybrid EMT-TS Simulation Strategies to Study High Bandwidth MMC-Based HVdc Systems

Yuan Liu1 , Marcelo A. Elizondo1 , Suman Debnath2 , Jingfan Sun3 , Ahmad Tbaileh1 , Yuri V. Makarov1 , Qiuhua Huang1 , Mallikarjuna R Vallem1 , Harold Kirkham1 , Nader A. Samaan1

1, Pacific Northwest National Laboratory Richland, WA, USA, 99354

2, Oak Ridge National Laboratory Oak Ridge, TN, USA, 37830

3, Georgia Institute of Technology Atlanta, GA, USA, 30332

{yuan.liu, marcelo.elizondo, ahmad.tbaileh, yuri.makarov, qiuhua.huang, mallikarjuna.vallem, harold.kirkham, nader.samaan }@pnnl.gov, debnaths@ornl.gov, jingfan@gatech.edu

Abstract—Modular multilevel converters (MMCs) are widely used in the design of modern high-voltage direct current (HVdc) transmission system. High-fidelity dynamic models of MMCsbased HVdc system require small simulation time step and can be accurately modeled in electro-magnetic transient (EMT) simulation programs. The EMT program exhibits slow simulation speed and limitation on the size of the model and brings certain challenges to test the high-fidelity HVdc model in system-level simulations. This paper presents the design and implementation of a hybrid simulation framework, which enables the co-simulation of the EMT model of Atlanta-Orlando HVdc line and the transient stability (TS) model of the entire Eastern Interconnection system. This paper also introduces the implementation of two high-fidelity HVdc line models simulated at different time steps and discusses a dedicated method for sizing the buffer areas on both sides of the HVdc line. The simulation results of the two HVdc models with different sizes of buffer areas are presented and compared.

Index Terms— buffer area, electro-magnetic transient, hybrid simulation, HVdc, transient stability

# I. INTRODUCTION

Modern power grid is experiencing a major evolution from ac to mixed ac-dc transmission systems with decreasing costs and noticeable economic and technical benefits of dc technologies. Some of the technical benefits of dc technologies include the abilities to interconnect several asynchronous grids, to integrate renewable energy generations, to support underground transmission, to increase the power transfer capability over long distances [1], [2], and to supply loads through variable frequency drives (VFDs) [3] – [5]. The dc technologies are also capable of providing ancillary services to enhance the economics and reliability of power systems and optimize the performance of ac grids [2].

Several national laboratories and their industry partners launched a jointly research effort to create models and methods to explore and amplify the technical and economic benefits of dc technologies in the future grid of United States [1]. This work has developed high-fidelity dynamic models of modular multilevel converters (MMCs) -based high-voltage direct current (HVdc) system [6]. The deliverables also include the development of high-fidelity models and control

algorithms of multi-terminal MMC-HVdc systems connecting Eastern Interconnection (EI), Western Electricity Coordinating Council (WECC), and Electric Reliability Council of Texas (ERCOT) [2], [6]. The developed control strategy for the multi-terminal MMC-HVdc system exhibits up to 51.75% improvement in frequency response with the connection of all the three asynchronous power grids in the United States [7]. However, the test of the developed MMC-HVdc system is performed with the aggregated models for EI, ERCOT and WECC grids based on NERC data [8]. These results represent preliminary results that require confirmation tests with the full models. The evaluation on the full model requires the setup of hybrid EMT-TS simulation platform.

Previous research implemented the hybrid simulation platform to represent a significant portion of the system model in a phasor-domain transient stability (TS) simulation program and co-simulate that with a detailed electro-magnetic transient (EMT) model of a small portion containing voltagesource converter (VSC) -HVdc [9],[10]. The communication between the TS and EMT programs is built on a software called E-TRAN Plus [11] that can simultaneously simulate the detailed model using a micro-second timestep in PSCAD [12], and the rest of the system using a milli-second time-step in PSS/E [13]. The PSS/E portion of the system model in [9] utilized an 8-machine 31-bus system, which is a limited-size test system. In addition, the paper by Farsani et al. [9] adopts an empirical approach to size the buffer area, within which a number of ac buses on either side of the HVdc line are selected and modeled in PSCAD program.

This paper presents the development of a co-simulation framework to integrate the EMT model of an MMC-HVdc system and the TS model of the external EI system. The characteristics of the EI system are described in detail. Oak Ridge National Laboratory (ORNL) designed an MMC-HVdc model based on hybrid discretization and multi-rate simulation [7]. Two simulation time steps, at 4µs (slow) and 60µs (fast) separately, are implemented for the MMC-HVdc model. This paper also proposes a specific method for sizing the buffer areas on both sides of the HVdc line by selecting the ac buses to be modeled in EMT-level simulation program. In this

paper, PSCAD is used as the EMT-level simulation tool and PSS/E is used as the TS-level simulation program. The software E-TRAN Plus is utilized to provide interfacing between PSCAD and PSS/E.

The following contributions of this paper are highlighted:

This paper is the first paper that describes the cosimulation of a high-fidelity HVdc transmission line model with realistic EI system while other cosimulation works only consider using limited-size IEEE standard systems [9].   
This paper proposes a VAr injection method to determine the size of buffer areas that are modeled in detailed EMT simulation.

# II. SYSTEM-LEVEL MODEL

An overlay of HVdc macro grid was proposed by Midcontinent Independent System Operator (MISO) with multiple technical and economic benefits [14]. The HVdc macro grid has a maximum transfer capacity of 14.4 GW between the EI and WECC. A version of macro grid is shown in Fig. 1 with power flows from the WECC to the EI.

![](images/59252d6d7478d1bccc705e06c9a532dab78e0e9a1524ee1f43595e24224a53ae.jpg)  
Figure 1. HVdc macro grid design proposed by MISO [1]

The blue HVdc line highlighted in Fig. 1 is the Atlanta-Orlando HVdc line that is modeled in EMT in this study to setup the hybrid simulation platform. This HVdc system is based on MMCs.

Considering the memory limitations in E-Tran Plus and since the HVdc line analyzed in this study is located in EI, WECC part of the model was eliminated and replaced by power injections at the HVdc macro grid terminals. The ac interconnection of the EI was modeled by a 2026 Summer-Peak case, provided by the Multi-regional Modeling Working Group of the EI Reliability Assessment Group (ERAG-MMWG). The models used in this study are based on previously developed models in [1]. Key parameters of the final power flow model are shown in TABLE I. The dynamic models of HVdc links except the Atlanta-Orlando line in the HVdc macro grid were represented by the CDC6T HVdc model [13] in PSS/E.

# III. PSCAD MODEL OF MMC-BASED HVDC SYSTEM

# A. MMC Models & Simulation Algorithms

The circuit diagram of a three-phase MMC is shown in Fig. 2. It consists of six arms with ???? series connected submodules (SMs) and an inductor. The basics of operation of the MMC is explained in detail in [15].

TABLE I. SUMMARY OF POWER FLOW NETWORK MODEL PARAMETERS   

<table><tr><td>Model Characteristics</td><td>Quantity</td></tr><tr><td>Total Generation (GW)</td><td>728</td></tr><tr><td>Total Load (GW)</td><td>693</td></tr><tr><td>Total Reactive Support (GVAr)</td><td>177</td></tr><tr><td>Number of Buses</td><td>78,682</td></tr><tr><td>Number of ac lines</td><td>99,331</td></tr><tr><td>Number of dc lines</td><td>68</td></tr><tr><td>Number of Generators</td><td>7,829</td></tr><tr><td>Number of Loads</td><td>42,730</td></tr></table>

![](images/92c6cb0e39250c834dcc6d0fc77667d3e08acfb367429fd4a1ad054d9fb1ec24.jpg)  
Figure 2: Circuit diagram of MMC

# B. MMC Control Strategies

The hierarchical control of MMC consists of: 1) inner control system to control ac grid currents, dc-link currents, circulating currents, and SM capacitor voltages, and 2) outer control system to control ac voltage and mean of SM capacitor voltages. The inner control system in MMC has been explained in [16] and is summarized in Fig. 3. The ac grid currents, dc-link currents, and circulating currents’ control strategy is shown in Fig. 3. The SM capacitor voltage balancing algorithm is explained in [16] and not repeated here. The outer control system consists of controlling ac voltage and mean of SM capacitor voltage, as shown in Fig. 4 [17].

![](images/9e2380da3d40733863410c135feb76c93dea3ab55ac1cc00a9463cd05894d16e.jpg)  
Figure 3: MMC-HVdc arm current control

![](images/0b1395aedb4f521a3b92166fb18a9298ec49fef4198e37f4a1257da49a2c8d6e.jpg)  
Figure 4: MMC outer controller and PLL

# IV. DESIGN OF BUFFER AREAS

The hybrid simulation in this paper will be performed using E-TRAN Plus [11]. The MMC-HVdc system can perform voltage control functionality. The buffer areas on both rectifier and inverter sides of the HVdc line are identified and modeled in PSCAD to simulate voltage behavior of the model parts close to the HVdc terminals and to increase the accuracy of hybrid simulation. To obtain the buffer areas, a sensitivity-based approach is performed. A reactive power injection is placed around the rectifier or inverter bus and the voltage changes are observed on the surrounding buses. A voltage deviation criterion is defined to determine buses included within the buffer areas. The procedure is illustrated in Fig. 5 and consists of the following steps:

1. Inject a certain amount of reactive power (∆Q) into an adjacent bus near rectifier or inverter bus.   
2. Solve power flow to calculate the voltage variations (∆V) of adjacent buses in respect to the reactive power injection (∆Q)   
3. Define criteria to rank ∆V and select buses for which the calculated ∆V values lie in the specified range.

![](images/8d40a8cf5dfd1da2563f862f2be239d8625b8e9d20681a45ace00520b1139ae3.jpg)  
Figure 5. Conceptual illustration of buffer areas selected by reactive power injection and voltage sensitivity method

In this paper, a reactive power injection of 1000 MVAr is used to generate voltage variations. To include a reasonable number of buses, the buses manifesting 1.4% or higher voltage variations are considered within the buffer areas. It is noted that the E-TRAN Plus will add to the buffer areas with several more buses connected to the considered buses through ideal branches. The final number of buses are 50 buses in the rectifier-side buffer area and 12 buses in the inverter-side buffer area. The results are summarized in TABLE II. TABLE II also shows the number of buses for a pair of smaller buffer areas selected based on engineering

judgement. The simulation results for the two selections of buffer areas will be compared in Section V.

TABLE II. NUMBER OF BUSES IN THE BUFFER AREAS   

<table><tr><td>Large Buffer Areas(VAr injection method)</td><td>Total Number ofBuses</td><td>Number of BoundaryBuses</td></tr><tr><td>Rectifier-Side (Atlanta)</td><td>50</td><td>21</td></tr><tr><td>Inverter-Side (Orlando)</td><td>12</td><td>4</td></tr><tr><td>Small Buffer Areas(engineering judgement)</td><td>Total Number ofBuses</td><td>Number of BoundaryBuses</td></tr><tr><td>Rectifier-Side (Atlanta)</td><td>8</td><td>4</td></tr><tr><td>Inverter-Side (Orlando)</td><td>9</td><td>4</td></tr></table>

# V. SIMULATION RESULTS

ORNL implemented two PSCAD models of MMC-HVdc line simulated at 4µs (slow model) and 60µs (fast model) separately. In this paper, two selections of buffer areas are proposed in TABLE II. A combination of 4 simulation scenarios is formed to investigate the simulation performances of different MMC-HVdc models in different buffer areas. To compare with the hybrid simulation models, this paper also presents the simulation results of PSCAD equivalent models, for which the MMC-HVdc line and buffer areas are modeled in PSCAD, the external system is modeled as equivalent voltage sources in PSCAD. The simulation scenarios are summarized in TABLE III.

TABLE III. DEPICTION OF SIMULATION SCENARIOS   

<table><tr><td></td><td>Fast MMC-HVdc</td><td>Slow MMC-HVdc</td></tr><tr><td>Small Buffer Areas</td><td>Case 1</td><td>Case 2</td></tr><tr><td>Large Buffer Areas</td><td>Case 3</td><td>Case 4</td></tr></table>

# A. Contingencies Applied in PSCAD Portion of the System

The simulation lasts for 5 seconds. At t=1.2s, the active power flowing through the HVdc line is ramped up from 0 to 500MW. Two contingencies occurring within the buffer areas are considered when running the PSCAD equivalent model and hybrid simulation model. The first contingency is to trip a 1241 MVAr shunt capacitor close to the rectifier (Atlanta) side of the HVdc line at t=3s and reconnect it at t=3.25s. The second contingency is to apply a 3-phase-to-ground fault at t=4s and clear it at t=4.25s. The voltage, active and reactive power on rectifier and inverter sides are shown in Figs. 6 – 9.

![](images/fe178c838854db7f21ce3a6378b5ae7bf6c015c3be65cb033f360f5c3c23fccd.jpg)

![](images/b08b8fdcf1052e9f1364ce5fe5bd905ea852704295cea0748b2f5de33e21f78d.jpg)

![](images/a77dcc7e12514547aa5d8f312565145a1e24200caa8057d5910db65069e2eb6d.jpg)

![](images/a0b3d83a183a2b980dd9b72e0d2ddbb39069f871b91741b27cb1c622ac9d9ce7.jpg)

![](images/4d0788ed5d27ae376ad1e4eef261166fd7229b0186acd3f0d416a25c273c75b9.jpg)

![](images/935c3d569b7d8b238b416b0b553c2bfbcc2d3d2c9ab064628684182ebeb37ff3.jpg)  
Figure 6. Case 1: small buffer area and fast MMC-HVdc model (left: PSCAD equivalent model, right: hybrid simulation model)

Comparing the left and right three subplots in Figs. 6 – 9, PSCAD-PSS/E co-simulation captures power system dynamics more accurately than the PSCAD equivalent model. Following the clearance of the fault at t=4.25s, the system is supposed to experience low-frequency oscillations as demonstrated in many system-level simulation studies [3], [4], [18]. It can be observed from the reactive power subplots in Figs. 6 – 9 that the low-frequency oscillation is captured in the results of hybrid simulation model. Because of the utilization of ideal voltage sources at all boundary buses, the PSCAD equivalent model cannot provide accurate simulation results.

![](images/f9a95df47fe2523e03f3f645278459632d1ed4cbee4c43858584bac9aa77cb7f.jpg)

![](images/d6651602fd8ffc3e142d4b11f64d163efbfb80239b0b12981cc1967c376ee12d.jpg)

![](images/3fbaf128adb523b19ece934403dfe6eb80135f098a621c063b0182e216830fe8.jpg)

![](images/9c75b4111bbc523a631c2a4f8c2106d3c88371064712f1ef90b7a10d6da4dce9.jpg)

![](images/566263d713d7e9fac568ed316e1b448ec7e95614e50f6a3fbbc2e9e56e205bec.jpg)

![](images/04f59ea46b22bb9345f051bdde1587a0198fc8793ed698b483539c5f3b3a54fe.jpg)  
Figure 7. Case 2: small buffer area and slow MMC-HVdc model (left: PSCAD equivalent model, right: hybrid simulation model)

![](images/ea61cecaf35ad720e8c16a54f056265f6aa23416782f72d47c0cf5292f4e1f1d.jpg)

![](images/0f2e10d12aa5ddd4b83d62edf7984126390670b4d203fe092f22280cffaa1f4d.jpg)

![](images/6e7cc55efc405f141752d458c8ee3ad3b539c2a7b1227971edc6d46e2a88d2d3.jpg)

![](images/f43455d3a5d80d1d9ebeaa6581fab9c8700c3d3441383ec8fb5fe23b9437b074.jpg)

![](images/29f0320c4c0c9e429e044f94265d5a7f8798475a7fcad4c88d1e1063d5fceb32.jpg)

![](images/ae2e8a31dc8a110806b44d8ba7a3dee154f749f1a2269a4924eea95cdd22f23c.jpg)  
Figure 8. Case 3: large buffer area and fast MMC-HVdc model (left: PSCAD equivalent model, right: hybrid simulation model)

Comparing the hybrid simulation results (right three subplots) in Figs. 8 and 9 with that in Figs. 6 and 7, it can be seen that the hybrid simulation model with large buffer areas generates more stable results than that with small buffer areas modeled in PSCAD. For the results of hybrid simulation model with small buffer areas shown in Fig. 7, unwanted swells and sags noticeably appear on the active power curves of the rectifier and inverter. Similar swells and sags are not found in the results of the hybrid simulation models with

large buffer areas shown in Figs. 8 and 9. This comparison verifies that the increase in the size of buffer areas improves the stability of the hybrid simulation and accuracy in quantifying the impact of the HVdc control system.

![](images/ff64212268cccbe0955aa1d44ae4baebc97107ca602f57be8b1f70f149be1875.jpg)

![](images/915da3b8d108d3fee352d424b4831637714789454ec45deb2cfa1fc72d59609a.jpg)

![](images/6585c5d948ba301f0ebd1586fe6104050c494a1f6e89fa04c1d2a4e5a72f17ee.jpg)

![](images/17fd36f1d2dcecdf759447b9124a336fa09f4103711f8053dde263d165e99a5b.jpg)

![](images/c4281986681a5286eb992e38fbbaffd733a4c5d6d0b40cf3cc16d4e86b5020a4.jpg)

![](images/0ab84983e88a3f132b165f272bf378c4d5d08c2f7474a98db4785cf26790f735.jpg)  
Figure 9. Case 4: large buffer area and slow MMC-HVdc model (left: PSCAD equivalent model, right: hybrid simulation model)

Another observation can be drawn from comparing Figs. 7 and 9 with Figs. 6 and 8. The slow MMC-HVdc model, simulated at 4µs, renders smoother (less noisy) results than the fast MMC-HVdc model that is simulated at 60µs. The reason for this observation can be attributed to the slower sampling assumed in the slow MMC-HVdc model that interferes with the control system’s response. This phenomenon is more pronounced in the case with the larger buffer zone model (see Fig. 9), indicating the loss of fidelity in the models with a smaller buffer zone (see Fig. 7).

The simulation performances for the four cases are presented in TABLE IV. The simulation cases tabulated in TABLE III are completed in a laptop with a 64-bit operating system, Intel Core i7-6820HQ CPU at 2.7 0GHz and 16GB RAM. It can be concluded from TABLE IV that ORNL’s fast HVdc line model results in up to 3.9 times faster computation time than slow model.

TABLE IV. COMPUTATION PERFORMANCE FOR 5-SECOND SIMULATION   

<table><tr><td>Buffer area size</td><td>Simulation model</td><td>PSCAD time step - ORNL&#x27;s line model</td><td>PSS/E time step</td><td>Simulation time</td><td>Speedup</td></tr><tr><td rowspan="4">Small</td><td rowspan="2">PSCAD with equivalent</td><td>60 μs – Fast</td><td>-</td><td>247 s</td><td rowspan="2">2.4x</td></tr><tr><td>4 μs – Slow</td><td>-</td><td>610 s</td></tr><tr><td rowspan="2">PSCAD-PSS/eco-simulation</td><td>60 μs – Fast</td><td>4.16 ms</td><td>287 s</td><td rowspan="2">2.4x</td></tr><tr><td>4 μs – Slow</td><td>4.16 ms</td><td>706 s</td></tr><tr><td rowspan="4">Large</td><td rowspan="2">PSCAD with equivalent</td><td>60 μs – Fast</td><td>-</td><td>303 s</td><td rowspan="2">3.9x</td></tr><tr><td>4 μs – Slow</td><td>-</td><td>1189</td></tr><tr><td rowspan="2">PSCAD-PSS/eco-simulation</td><td>60 us – Fast</td><td>4.16 ms</td><td>391 s</td><td rowspan="2">3.4x</td></tr><tr><td>4 us – Slow</td><td>4.16 ms</td><td>1351</td></tr></table>

# B. Contingencies Applied in PSS/E Portion of the System

This scenario considers a contingency applied on the PSS/E side of the hybrid simulation model. Four adjacent generators with a total generation of 3.512 GW are tripped

offline at t=3s on the PSS/E side. The rectifier- and inverterside voltages, active and reactive powers are monitored on the PSCAD side for the 4 scenarios described in TABLE III. The results are shown in Fig. 10.

![](images/dab55d2e05eb460bc4b9ec361ce3c29431b8d7f89f2b3e4403d62e5937f61e6d.jpg)

![](images/84929b0c5cd4eccd1e3aacd1509dfbe886f607f71cf1f5a189b47dd4d8e8cfcf.jpg)

![](images/e562c5fb3737d8dd69f4da1013fa10f09f82088d8da51d067d824d7d7fdf567f.jpg)

![](images/711271555603155de01855b8a5906b9694bce2579f01b46d5991c8b8d270aa46.jpg)

![](images/62a9b99b534e95980b93d219959cd0c3e88ab69989f1e6d2ce351f25149d0329.jpg)

![](images/29274462b33b3f05ec25ed6fadd667291318a4aa6082cc4a61966cb7ff065236.jpg)  
Figure 10. HVdc rectifier- and inverter- side voltages, active and reactive powers monitored in PSCAD in response to generator tripping on PSS/E side

It can be seen from Fig. 10 that all the four models generate similar voltage and power trajectories. However, high-frequency noise is obviously seen on the voltage and power curves of the fast MMC-HVdc models with small and large buffer areas. Based on the observations from Figs. 6 – 9, it can be concluded that the slow MMC-HVdc model with large buffer areas is able to generate the most credible and stable simulation results. However, in preliminary studies where speed is important, one may begin with a small buffer zone and fast MMC-HVdc model, which also provides relatively reliable results (see Fig. 6 and Fig. 10).

# VI. CONCLUSIONS

This paper presents the development of the hybrid EMT-TS simulation framework to study the responses of highfidelity HVdc line in the full North American EI system. The PSCAD (or EMT) model of the MMC-based HVdc system is implemented based on fast and slow approaches and its control system is briefly described in this paper. The sizes of the interfacing areas between the HVdc line and EI system, known as buffer area, are determined by VAr injection techniques. It can be concluded from the studies in this paper that the size of buffer area in the hybrid simulation of HVdc line impacts the accuracy and stability of the simulation performances. A large buffer area is essential for accurate EMT-TS co-simulation with a high-fidelity HVdc system.

Though the simulation speed is compromised, a slow MMC-HVdc model is a preferable choice to provide reliable simulation results. In preliminary studies where speed is important, one may begin with a small buffer zone and fast MMC-HVdc model.

# REFERENCES

[1] M. A. Elizondo, N. Mohan, J. O'Brien, Q. Huang, D. Orser, W. Hess, W. Zhu, D. Chandrashekhara, Y. V. Makarov, D. Osborn, J. Feltes, H. Kirkham, D. Duebner, and Z. Huang, “HVdc macro grid modeling for power-flow and transient stability studies in north American continental-level interconnections,” CSEE Journal of Power and Energy Systems, vol. 3, no. 4, pp. 390 – 398, Dec. 2017.   
[2] Y. V. Makarov et al., “Models and methods for assessing the value of HVdc and MVDC technologies in modern power grids” No. PNNL-26640, July 2017. [Online]. Available: https://www.pnnl.gov/main/publications/external/technical_reports/PN NL-26640.pdf   
[3] Y. Liu, V. Vittal, and J. Undrill, “Performance-based linearization approach for modeling induction motor drive loads in dynamic simulation,” IEEE Trans. Power Syst., vol. 32, no. 6, pp. 4636 - 4643, Nov. 2017.   
[4] Y. Liu and V. Vittal, “Modeling of rectifier-controlled induction motor drive load in transient stability simulation tools,” IEEE Trans. Power Syst., vol. 33, no. 5, pp. 4719 – 4729, Sept. 2018.   
[5] Y. Liu and V. Vittal, “Distribution side mitigation strategy for fault induced delayed voltage recovery,” in Proc. IEEE PES General Meeting, Jul. 2014, pp. 1 – 5.   
[6] S. Debnath and M. Chinthavali, "Numerical-Stiffness-Based Simulation of Mixed Transmission Systems," IEEE Trans. Ind. Electron., vol. 65, no. 12, pp. 9215-9224, Dec. 2018.   
[7] S. Debnath and J. Sun, "Fidelity Requirements with Fast Transients from VSC-HVdc," IECON 2018 - 44th Annual Conference of the IEEE Industrial Electronics Society, Washington, DC, 2018, pp. 6007-6014.   
[8] NERC Resources Subcommittee, “Balancing and Frequency Control”, pp. 1-53, January 2011.   
[9] P. M. Farsani, N. R. Chaudhuri, R. Majumder “Hybrid simulation platform for VSC-HVdc-assisted large-scale system restoration studies,” 2016 IEEE PES Innovative Smart Grid Technologies (ISGT) Conference, pp. 1-5, 2016.   
[10] G. D. Irwin, C. Amarasinghe, N. Kroeker, and D. Woodford, “Parallel processing and hybrid simulation for HVdc/VSC PSCAD studies,” 10th IET International Conference on AC and DC Power Transmission, Dec. 2012.   
[11] E-Tran Plus User Guide, Electranix Corporation, Winnipeg, MB, Canada, Nov. 2016.   
[12] PSCAD User’s Guide, ver. 4.6, Manitoba Hydro International Ltd., Winnipeg, MB, Canada, May 2018.   
[13] PSS/E Program User Manual ver. 33.4, Siemens PTI, Mar. 2013.   
[14] MISO transmission expansion planning (MTEP), MISO, Carmel, IN, USA, 2014   
[15] S. Debnath, J. Qin, B. Bahrani, M. Saeedifard and P. Barbosa, "Operation, Control, and Applications of the Modular Multilevel Converter: A Review," IEEE Trans. on Power Electron., vol. 30, no. 1, pp. 37-53, Jan. 2015.   
[16] S. Debnath and M. Chinthavali, “MMC-HVdc: Simulation and control system,” 2016 IEEE Energy Conversion Congress and Exposition (ECCE), pp. 1–8, Sept 2016.   
[17] N. R. Chaudhuri, R. Majumder, B. Chaudhuri, and J. Pan, “Stability analysis of VSC MTDC grids connected to multimachine AC systems,” IEEE Trans. Power Delivery, vol. 26, no. 4, pp. 2774–2784, Oct 2011.   
[18] L. Pereira, D. Kosterev, P. Mackin, D. Davies, J. Undrill, and W. Zhu, “An interim dynamic induction motor model for stability studies in the WSCC,” IEEE Trans. Power Syst., vol. 17, no. 4, pp. 1108–1115, Nov. 2002.