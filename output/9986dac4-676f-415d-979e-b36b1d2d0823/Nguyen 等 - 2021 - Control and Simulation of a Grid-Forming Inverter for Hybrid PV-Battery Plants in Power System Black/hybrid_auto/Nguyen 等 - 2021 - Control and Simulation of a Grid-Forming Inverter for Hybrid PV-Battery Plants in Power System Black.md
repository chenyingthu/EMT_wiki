# Control and Simulation of a Grid-Forming Inverter for Hybrid PV-Battery Plants in Power System Black Start

Quan Nguyen, Mallikarjuna R. Vallem, Bharat Vyakaranam, Ahmad Tbaileh, Xinda Ke, Nader Samaan Pacific Northwest National Laboratory, WA

Abstract—Power system restoration is an important part of system planning. Power utilities are required to maintain black start capable generators that can energize the transmission system and provide cranking power to non-blackstart capable generators. Traditionally, hydro and diesel units are used as black start capable generators. With the increased penetration of bulk size solar farms, inverter based generation can play an important role in faster and parallel black start thus ensuring system can be brought back into service without the conventional delays that can be expected with limited black start generators. Inverter-based photovoltaic (PV) power plants have advantages that are suitable for black start. This paper proposes the modeling, control, and simulation of a grid-forming inverter-based PV-battery power plant that can be used as a black start unit. The inverter control includes both primary and secondary control loops to imitate the control of a conventional synchronous machine. The proposed approach is verified using a test system modified from the IEEE 9-bus system in the timedomain electromagnetic transient simulation tool PSCAD. The simulation results shows voltage and frequency stability during a multi-step black-start and network energization process.

Index Terms—Black start, PV power plant, Grid-forming inverter, Photovoltaic integration, Energy storage.

# I. INTRODUCTION

Black start (BS) is a process of restoring a power system following a major collapse or a system-wide blackout. This process relies on one or multiple generation units that are able to start without the support from the main power system. Such units are also called BS units.

The characteristics of an ideal BS unit include small startup power requirement, fast ramping rate to quickly reach the rated power, large real and reactive power capacity to meet any needs during the black start process, and ability to stabilize system voltage and frequency due to the subsequent energizations of the remaining non-black-start (NBS) units and transmission lines as well as load pickup [1]. In practice, a BS unit can be a hydro, natural gas or diesel units [2].

Regarding renewable energy sources (RES), solar energy becomes more and more common as the photovoltaic (PV) penetration in distribution feeders has been increasing rapidly in recent years. On the other hand, there are few current and planned large-scale PV power plants that are integrated directly to the transmission network. In [3], general procedures for interconnection of large-scale PV plants and technical requirements for plant performance are discussed. In [4], the authors develop a demonstration concept and test plan to show

how different power control modes can help an inverter-based PV power plant to provides a wide range of ancillary services. A summary of operational benefits and issues for a largescale PV power plant including power quality, power control, protection, balancing and reliability under different loading conditions are presented in [5].

Considering the advantageous properties such as fast ramping rates, power ratings of several hundreds MW, and ability to coordinate with energy storages (ES), recent large-scale inverter-based PV power plants can be considered as promising BS resources. However, to the best knowledge of the authors, little focus has been given to explore such potential capability of a PV-ES power plant.

A generation system needs several characteristics to be considered as a BS unit and several studies need to be performed to assess them. These studies include power plant modeling, grid-forming inverter control, effective coordination between PV and ES during a black start process, voltage and frequency stability, and sizing of the PV and ES. Note that similar works might exist at distribution voltage level; however, the focus of this paper is on the transmission voltage level. In addition, case studies using multiple test systems with different topologies and parameters are required to thoroughly verify the modeling and control design of the grid-forming inverters. Average (positive sequence) models for inverters do not capture all the characteristics and limitations of inverters. A validation should be carried out using an electromagnetic transient (EMTP) simulation tool and a high-fidelity inverter model to capture detailed dynamic responses.

In this paper, modeling, grid-forming control, conceptual design, and detailed simulation of an inverter-based PV-ES power plant that can be used as a reliable BS resource during a black start are demonstrated. The paper is organized as follows. Section II briefly describes current black-start practice using a conventional synchronous generator. Section III presents the proposed modeling, control, and operation of a PV-ES plant during a black start. In Section IV, the simulation results of a black-start process in a test system in the timedomain EMTP simulation tool PSCAD are discussed. Final conclusions and remarks are given in Section V.

# II. BLACK-START PROCESS AND STATE OF THE ART

Current practice of a black start process includes several steps [1], [6]. First, one or multiple black-start (BS) units such

![](images/0661e3c5bc56005466d539423599a482aaf9246609d3b4e90df4a338764ad452.jpg)  
Fig. 1. A test system for black-start demonstration using a conventional hydro generator as a BS unit.

as hydro power plants start their own power without support from the grid. Next, main transmission lines and transformers are energized to form the backbone of the system. A small potion of load might be picked up during this process to assure voltage stability or handle transformer inrush current. Finally, non-black-start (NBS) units and the remaining loads are gradually picked up by energizing the rest of transmission lines while maintaining the voltage and frequency of the system.

Fig. 1 shows an example of the black-start process using a 5-bus system. The BS hydro power plant at Bus 1 and circuit breakers to pick up a NBS unit at Bus 2 and the main load at Bus 5. The simulation is conducted in the timedomain electromagnetic transient tool PSCAD [7]. The circles with numbers show the sequential order of the energizing and picking up transformers, transmission lines, generators, and load.

Figs 2 and 3 show the resulting voltage at Buses 1, 2, and 5 as well as the power generation of the BS and NBS units at Buses 1 and 2, respectively, during the black-start process. As expected, these simulation results show stable responses after each switching event of circuit breakers.

# III. MODELING, CONTROL, AND OPERATION OF AGRID-FORMING INVERTER-BASED PV-ES PLANT FORBLACK START

This section presents the modeling and its grid-forming control of an inverter-based PV-ES power plant that is capable of being a BS unit for a black-start process.

The physical structure and grid-forming control of the PV-ES power plant is shown in Fig. 4. The DC side of the inverter system consists of PV arrays and energy storages connected

![](images/38887b7286ee9efa40519955c903963e10db25cc7316c224e5c855ad1554806d.jpg)  
Fig. 2. Voltage profiles at Buses 1, 2, and 5 during the black-start process.

![](images/4a448b9c4c2123e528f1fc5006c952bc89476960d9c6a464ca78dc3962f9e247.jpg)  
Fig. 3. Real power generation from BS unit at Bus 1 and NBS unit at Bus 2.

in parallel. The AC side consists of switching components that form an H-bridge, a low-pass LC filter, and a step-up transformer.

# A. Grid-Forming Inverter Control

As shown in Fig. 4, the control of a grid-forming inverterbased PV-ES power plant includes both primary and secondary control loops, which imitates the control of conventional synchronous machines. This control strategy is adapted from the inverter control for microgrids at distribution level [8].

The primary control loop modifies the voltage magnitude and frequency at the point of common coupling (PCC) based on a pre-defined droop curve and the measured real and reactive power $P _ { a c }$ and $Q _ { a c }$ injected to the grid. The resulting voltage magnitude and frequency, both are deviated from the rated values, are used to generate a three-phase sinusoidal voltage signal. Such a signal is the input of classical nested voltage- and current- loops, designed in the synchronously rotating reference frame dq [9], to create the inverter reference voltage v∗i . The Pulse-Width-Modulation (PWM) block takes $v _ { i } ^ { * }$ and generates switching signals for the switching devices of the inverter.

![](images/a92ae3b09bfbe4f1963f9303126e2c0d9d68344e6552fffb27239827aa979681.jpg)  
Fig. 4. The grid-forming control of an inverter-based PV-ES power plant.

The secondary control loop is responsible for restore the voltage and frequency back to rated values. This goal is achieved by adding quantities $\Delta V _ { g }$ and $\Delta f _ { g } ,$ which are the output of the secondary PI controllers, to the output voltage $V _ { g }$ and frequency $f _ { g }$ of the primary droop controllers.

# B. Modeling and Control of PV and ES

Fig. 5 shows the modeling of the DC side of an inverter, which is the combination of a PV array and an ES. The models of the PV array and ES are leveraged from [10]. Due to the intermittence of solar, the ES is required in the PV-ES power plant model to guarantee a successful black start.

The input of the PV inverter includes the solar irradiation and temperature. A boost converter is used to boost the output voltage of the PV array to a sufficient inverter input voltage for achieving the desired AC voltage magnitude at the AC side. On the other hand, the ES model includes a detailed battery model and a conventional buck-boost converter. The DC voltage controller of the buck-boost converter is responsible for keeping the voltage across the DC-link capacitors, which are shared by the PV array and ES, at a constant value.

# C. Operational Concept during a Black-start Process

During the entire black-start process, the voltage magnitude and frequency at the PCC are maintained at the rated values. On the other hand, the supplied power $P _ { a c }$ and $Q _ { a c }$ at the PCC vary with each switching event of circuit breakers to energize transformers and transmission lines as well as pick up NBS units and loads. The real power $P _ { a c }$ required by the black start process entirely depends on the support from the PV array and ES at the DC side. Therefore, it is important to size the PV and ES accordingly.

At the DC side, as input DC-link voltage of the inverter is kept constant during the entire black start, the controls of the DC and AC sides are decoupled. After each switching event of circuit breakers during the black start process, the PV array and ES varies their output real power to meet the real power requirement at the AC side. In this work, the ES is assigned as the primary power supply to the AC side as long as its state of charge is positive. If the real power requirement from AC

![](images/2b6df8023453cb7a88eb30a51c45cd0c4e0f024f5e951716d19d2296edc4f165.jpg)  
Fig. 5. The modeling of PV array and ES at the DC side of an inverter-based PV-ES power plant [10].

side exceeds the upper limit of discharging power of the ES, the remaining power required is provided from the PV array.

# IV. CASE STUDY

This section shows the time-domain electromagnetic transient simulation in PSCAD to demonstrate the black-start capability of the PV-ES power plant described in Section III. More specifically, the simulation focuses on the backbone energization of the system, i.e. energizing main transmission lines and transformers as well as picking up loads. The metrics used to validate the efficacy of the grid-forming control include two folds. First, the voltage and frequency must be stable during the entire backbone-energizing process. Second, an optimal sequence of energizing transmission lines and transformers as well as optimal amounts of load from a separated optimization problem are used as the input of

![](images/ee2301d584f80369e2b7d3adbf0d6b33816c9cd0d6a8d74e14794b407baa22c5.jpg)  
Fig. 6. Test system for simulating back-bone energizing using a PV-ES power plant at Bus 1 as a BS unit.

TABLE I TOTAL AMOUNT OF PICKED-UP LOAD AT EACH BUS.   

<table><tr><td>Step</td><td>Time (s)</td><td>\( P_{5}^{load} \)</td><td>\( Q_{5}^{load} \)</td><td>\( P_{6}^{load} \)</td><td>\( Q_{6}^{load} \)</td><td>\( P_{8}^{load} \)</td><td>\( Q_{8}^{load} \)</td></tr><tr><td>1</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>2</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>3</td><td>2.5</td><td>13.4</td><td>5.3</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>4</td><td>5.0</td><td>13.4</td><td>5.3</td><td>0.0</td><td>0.0</td><td>28.8</td><td>10.1</td></tr><tr><td>5</td><td>7.5</td><td>13.4</td><td>5.3</td><td>4.0</td><td>1.3</td><td>33.4</td><td>11.7</td></tr><tr><td>6</td><td>10.0</td><td>26.1</td><td>10.4</td><td>59.8</td><td>19.9</td><td>34.3</td><td>12.0</td></tr><tr><td>7</td><td>18.0</td><td>30.1</td><td>12.0</td><td>59.8</td><td>19.9</td><td>65.7</td><td>23.0</td></tr></table>

the simulation. Therefore, another metric to verify the gridforming control is the similarity between the steady-state voltages from the simulation result and the voltages from the numerical optimization solution.

# A. System Description

The test system used in this section is the IEEE 9-bus system, as shown in Fig. 6. The BS start unit is assumed to be located at Bus 1. However, instead of using a conventional hydro plant as the BS unit as shown in Fig. 1, an inverter-based PV-ES power plant with grid-forming capability is deployed. The ratings of the PV and ES are assumed to be sufficient to meet the power requirement during the entire backboneenergizing process. The optimal switching sequence of the circuit breakers to energize transmission lines are represented by the circles with numbers. The picked up loads at Buses 5, 6, and 8 at each step are shown in Table I.

During the simulation, it is observed that the energization of transformers and transmission lines might negatively affect

![](images/d6f2ef575e98d33109d41a2017ba584dadf9f8bdb6ee4338639bfa5a49497c67.jpg)  
Fig. 7. Bus voltages during the backbone energizing process.

system stability. The former causes inrush current that results in undervoltage violations while the latter results in overvoltage violations during a low load condition. Therefore, small amount of auxiliary loads might be necessary at the secondary of a transformer and the end terminal of a transmission line to guarantee voltage stability. For example, an auxiliary load is added at Bus 4, which is the secondary side of the transformer between Buses 1 and 4. In addition, auxiliary loads are added at Buses 5, 7, and 9 when energizing the lines 4-5, 5-7, and 6-9, respectively. At the end of the simulation when the main loads are picked up, these auxiliary loads are disconnected.

# B. Simulation result

Fig. 7 shows the voltages at Buses 1 and 5 from the PSCAD simulation result and the numerical optimization solution. It

![](images/65db7279762229ad973b42de493f9c268daa942db6164deacdc5d881ef208cd5.jpg)  
Fig. 8. Frequency measured at Bus 1 during the backbone energizing process.

![](images/53ea65598f509d4fdc48a0874846d8e382774de204d94ab9341c77e0d680b503.jpg)  
Fig. 9. Power supplied by the PV-ES power plant at Bus 1 during the backbone energizing process.

![](images/009857f17a8204f6a9ab3cd945a67637421b2b425c45df38b0071fec530f00ea.jpg)  
Fig. 10. Power supplied by the PV array and ES at the DC side.

can be seen that the simulated voltages are stable after all switching events, and their stead-state values closely match the numerical optimization solution.

Fig. 8 shows the frequency at Bus 1 where the PV-ES power plant is located. The is an acceptable noise in the frequency profile during the initial no-load condition from 0 to 5 seconds. However, after the main loads are picked up, the resulting frequency is also stable and its steady-state value

closely matches the rated value of 60 Hz.

Fig. 9 shows the real and reactive power supplied from the PV-ES power plant from the simulation result and numerical optimization solution. It can be seen that the simulation result and numerical solution are also similar to each other.

Fig. 10 shows the power supplied from the PV array and ES at the DC side of the PV-ES power plant. From the beginning to 5 seconds, the ES is the main supply resource as the required power from the AC side is less than the discharging power limit of the ES. However, after 5 seconds, the power supplied from the ES remains constant while the remaining power required from the AC side is provided by the PV array.

# V. CONCLUSION

In this paper, AC- and DC-side modeling, a grid-forming control, and an operational concept for an inverter-based PV-ES power plant with ES are proposed. A time-domain EMTP simulation for the IEEE 9-bus system is used to evaluate the efficacy of the proposed approach. The simulation results show completed voltage and frequency stability during the entire black start process as well as high control accuracy when comparing the simulation result and a numerical input. Based on these results, a PV-ES power plant using the proposed work can be successfully and reliably used as a BS unit for a black start in a transmission system.

# VI. ACKNOWLEDGMENT

This material is based upon work supported by the U.S. Department of Energy’s Office of Energy Efficiency and Renewable Energy (EERE) under the Solar Energy Technologies Office Award Number DE-EE0008770.

# REFERENCES

[1] J. R. Gracia, L. C. Markel, D. T. Rizy, P. W. OConnor, R. Shan, and A. Tarditi, “Hydropower Plants as Black Start Resources,” Oak Ridge National Laboratory, Tech. Rep., May 2019.   
[2] FERC, “Blackstart Resource Availability,” Tech. Rep. [Online]. Available: https://www.ferc.gov/sites/default/files/2020-05/bsr-report.pdf   
[3] Abraham Ellis, Benjamin Karlson, Joseph Williams,, “Utility-scale photovoltaic procedures and interconnection requirements,” Tech. Rep., 2012. [Online]. Available: https://prod-ng.sandia.gov/techlib-noauth/ access-control.cgi/2012/122090.pdf   
[4] Clyde Loutan, Peter Klauer, Sirajul Chowdhury, and Stephen Hall, Mahesh Morjaria, Vladimir Chadliev, Nick Milam, and Christopher Milan, Vahan Gevorgian, “Demonstration of essential reliability services by a 300 MW solar photovoltaic power plant,” Tech. Rep., 2017. [Online]. Available: https://www.nrel.gov/docs/fy17osti/67799.pdf   
[5] E. Rakhshani, K. Rouzbehi, A. Snchez, A. Tobar, and E. Pouresmaeil, “Integration of large scale PV-based generation into power systems: A survey,” Energies, 2019.   
[6] M. Adibi, P. Clelland, L. Fink, H. Happ, R. Kafka, J. Raine, D. Scheurer, and F. Trefny, “Power system restoration - a task force report,” IEEE Transactions on Power Systems, vol. 2, no. 2, pp. 271–277, 1987.   
[7] EMTDC transient analysis for PSCAD power system simulation. [Online]. Available: https://hvdc.ca/uploads/ck/files/reference material/ EMTDC User Guide v4 3 1.pdf   
[8] Q. Shafiee, J. C. Vasquez, and J. M. Guerrero, “Distributed secondary control for islanded microgrids - a networked control systems approach,” in IECON 2012 - 38th Annual Conference on IEEE Industrial Electronics Society, 2012, pp. 5637–5642.   
[9] R. Teodorescu, M. Liserre, and P. Rodrguez, Grid converters for photovoltaic and wind power systems. John Wiley, Ltd, 2011.   
[10] PSCAD. Photovoltaic-battery system. [Online]. Available: https: //www.pscad.com/knowledge-base/article/471