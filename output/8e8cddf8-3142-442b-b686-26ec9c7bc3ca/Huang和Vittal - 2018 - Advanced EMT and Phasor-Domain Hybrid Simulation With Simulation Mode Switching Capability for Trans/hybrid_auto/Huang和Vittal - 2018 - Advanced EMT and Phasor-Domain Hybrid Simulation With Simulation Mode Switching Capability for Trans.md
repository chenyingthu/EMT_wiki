# Advanced EMT and Phasor-Domain Hybrid Simulation With Simulation Mode Switching Capability for Transmission and Distribution Systems

Qiuhua Huang , Member, IEEE, and Vijay Vittal , Fellow, IEEE

Abstract—Conventional electromagnetic transient (EMT) and phasor-domain hybrid simulation approaches presently exist for transmission system level studies. Their simulation efficiency is generally constrained by the EMT simulation. With an increasing number of distributed energy resources and nonconventional loads being installed in distribution systems, it is imperative to extend the hybrid simulation application to include distribution systems and integrated transmission and distribution systems. Meanwhile, it is equally important to improve the simulation efficiency as the modeling scope and complexity of the detailed system in the EMT simulation increases. To meet both requirements, this paper introduces an advanced EMT and phasor-domain hybrid simulation approach. This approach has two main features: first, a comprehensive phasor-domain modeling and simulation framework which supports positive-sequence, three-sequence, threephase, and mixed three-sequence/three-phase representations and second, a robust and flexible simulation mode switching scheme. The developed scheme enables simulation switching from hybrid simulation mode back to pure phasor-domain dynamic simulation mode to achieve significantly improved simulation efficiency. The proposed method has been tested on integrated transmission and distribution systems. The results show that with the developed simulation switching feature, the total computational time is significantly reduced compared to running the hybrid simulation for the whole simulation period while maintaining good simulation accuracy.

Index Terms—EMT and phasor-domain hybrid simulation, multi-area Thevenin equivalent, simulation mode switching. ´

# I. INTRODUCTION

P OWER system dynamic analysis requirements are signif-icantly evolving due to the changing nature of generation and loads. A significant portion of newly installed generation resources and a variety of loads including induction motors are

Manuscript received August 9, 2017; revised December 19, 2017 and April 1, 2018; accepted April 28, 2018. Date of publication May 9, 2018; date of current version October 18, 2018. Paper no. TPWRS-01232-2017. This work was supported by the National Science Foundation under Grant EEC-9908690 at the Power System Engineering Research Center. (Corresponding author: Qiuhua Huang.)

Q. Huang is with the Electricity Infrastructure Group, Pacific Northwest National Laboratory, Richland, WA 99354 USA (e-mail:,qiuhua.huang@pnnl. gov).

V. Vittal is with the Department of Electrical, Computer and Energy Engineering, Arizona State University, Tempe, AZ 85287 USA (e-mail:,vijay.vittal@ asu.edu).

Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

Digital Object Identifier 10.1109/TPWRS.2018.2834561

interfaced with the grid through power electronic (PE) converters [1]. However, existing transient stability (TS) simulation tools cannot adequately represent PE devices in sufficient detail, particularly during the faulted period [2]–[7]. Additionally, these tools cannot adequately represent single-phase air-conditioner compressor motors [9], which account for an increasingly large percentage of summer peak load in many power systems [10]. These modeling inadequacies can result in either an over- or under-estimate of the system reliable operation boundary and/or stability limits, which in turn results in systems operating under either higher risk or less efficient conditions. On the other hand, EMT simulation tools can simulate PE and single-phase devices in detail. However, they are not suitable for large systemlevel studies. Several different simulation methods, including EMT-TS hybrid simulation [2]–[8], frequency adaptive simulation [11] and dynamic phasor based approach [12], were proposed or developed to solve similar simulation challenges. Among them, the hybrid simulation approach has attracted the most attention from both industry and academia.

Previous research and development efforts on hybrid simulation mainly focused on the following three aspects: 1) network equivalent, including fundamental frequency based equivalent [6]–[8] and frequency dependent network equivalents [13]; 2) interaction protocols for improving efficiency and performance during fault periods [6]–[8]; 3) hybrid simulation program development [13]–[16]. Except for [15], others were developed only for transmission systems.

Except for the real-time simulator-based hybrid simulation, the overall computational efficiency of hybrid simulation for realistically large system applications is still not satisfactory, as shown in a recent study in [8]. It should be noted that the computational efficiency issue was not emphasized in previous studies mainly because the EMT (or detailed) systems in these studies were relatively small and simple [2], [3], [5]–[7]. Given the present trend of increasing application of non-conventional generation and loads as well as HVDC transmission [1], it is expected that a larger portion of the system with more complex and detailed models needs to be modeled in the EMT simulator. Consequently, the computational efficiency issue of the EMT simulator will constitute a significant bottleneck. While the performance of EMT simulators are improving, the improvement is not sufficient compared to the ever-increasing computational demands. One alternative to improve the computational efficiency

of hybrid simulation is to enhance the simulation workflow. Previous studies in [2] and [3] showed that the overall simulation efficiency could be significantly improved by transitioning from the hybrid simulation mode back to TS simulation mode after the fast dynamics settle down. However, there are some outstanding limitations in the underlying assumptions and implementation in [2] and [3]. More detailed discussions will be presented in Section II.

Furthermore, almost all the previous hybrid simulation research and development efforts focused on transmission systems only, and very few on distribution systems until recently [15], and none on integrated transmission and distribution (T&D) systems. With an increasing number of distributed energy resources (DER) and new types of loads being installed in the distribution systems, it is imperative to extend the hybrid simulation application to distribution systems [15] and integrated T&D systems.

In this paper, an advanced hybrid simulation program has been developed by extending the hybrid simulation program developed by the authors in [8], [14]. Compared to the earlier work in [8], [14], the new hybrid simulation program not only has comprehensive phasor-domain modeling capabilities, supporting three-phase, three-sequence and conventional positivesequence modeling, but also features a robust ability to switch from the hybrid simulation mode back to phasor-domain dynamic simulation (DS) mode. The main contributions of the paper include: 1) a comprehensive hybrid simulation program suitable for transmission, distribution as well as integrated T&D systems, instead of separate hybrid simulation programs for each domain; 2) a robust simulation mode switching scheme. To help realize simulation mode switching, discrete events and/or control signals captured by the EMT simulation are utilized to reconcile the simulation results of the phasor-domain and EMT representations of the detailed system.

The remainder of the paper is organized as follows: a review of hybrid simulation with simulation mode switching is presented in Section II. Comprehensive phasor-domain modeling and dynamic simulation capabilities developed for hybrid simulation are discussed in Section III. In Section IV, development of an advanced hybrid simulation program is presented in detail. Test cases and results are shown in Section V. Additional discussions and conclusions are provided in Sections VI and VII, respectively.

# II. HYBRID SIMULATION WITH SIMULATION MODE SWITCHING

# A. The Concept of Simulation Mode Switching

Conventional hybrid simulation consists of two stages, as illustrated in Fig. 1. It starts with the TS simulation stage, then switches to the hybrid simulation stage prior to the fault occurrence and remains in the mode till the end of simulation.

The primary motivation behind switching from TS simulation to EMT-TS hybrid simulation is to take advantage of the detailed modeling and simulation capabilities of the EMT simulation. Fast dynamics in power systems usually settle down in a short time period after the fault is cleared. When the dominant dynamics in the system are in the low frequency range,

![](images/e7384ea3d2997e47408096545271df039d11f44f0b38ca66f22512e45ff6fc33.jpg)  
Fig. 1. A schematic illustrating conventional 2-stage hybrid simulation.

![](images/bdc0f6e3e9edafd17b2d0e5735ccf02c35495762808a7ae2aa520d1965949813.jpg)  
Fig. 2. Advanced hybrid simulation with simulation mode switching.

these components modeled in the EMT simulator can be represented by their corresponding phasor-domain dynamic or quasisteady-state (QSS) models. Therefore, it is theoretically feasible to switch from EMT-TS hybrid simulation back to pure TS simulation after the fast dynamics settle down without significantly compromising the simulation accuracy.

The two-stage hybrid simulation (depicted in Fig. 1) provides users the “zoom-in” capability. When the conventional hybrid simulation is enhanced with the simulation mode switching capability, as shown in Fig. 2, users can “zoom-out” from the detailed modeling and simulation by transitioning from hybrid simulation back to phasor-domain dynamic simulation after the fast dynamics in the detailed system settle down. Such a “zoomin/zoom-out” switching capability not only provides more flexibility to the users, but also reduces the simulation time significantly for hybrid simulation applications that involve a relatively large and/or complex detailed system. It should be noted that the durations shown in the Figs. 1 and 2 are intended to give users the basic idea regarding how long each stage usually lasts in practical applications, thus they should not be treated as exact numbers. The exact numbers vary from case to case.

Switching from stage 1 (TS) to stage 2 (hybrid simulation) is relatively easy to achieve, since it is completed under the pre-fault, normal steady state operating condition. In contrast, switching from stage 2 (hybrid simulation) to stage 3 (TS) is more complicated and challenging since the system is operating under a non-equilibrium, dynamic condition.

# B. Previous Approaches and Key Issues

In the approach proposed in [2], the detailed system has two representations, i.e., an EMT representation and a phasor model representation. During the stage 2 shown in Fig. 2, the phasor model representation of the detailed system is simulated using TS simulation in parallel with the hybrid simulation. The switching operation is performed after the simulation results of both representations converge. A fundamental issue with this approach lies in the implicit assumption that simulation results of the two representations of the detailed system would converge at some point after the fast dynamics settle down.

![](images/f53862ee749293bb87ca9bd69451fe7aa8a74e455d257e590a39185e74152548.jpg)  
Fig. 3. Comprehensive phasor modeling capabilities are developed for transmission, distribution and integrated T&D systems.

However, the convergence is not guaranteed without reconciling the simulation results, due to the inherent differences in the modeling and simulation methods between EMT and TS simulations. Furthermore, the implementation was only discussed at a high level, with many important implementation details not provided in [2].

Another simulation switching approach proposed in [3] directly initializes a phasor model representation of the detailed system before switching back to the TS simulation. It was achieved by simply assuming the states of the detailed system would fully recover to the pre-fault steady-state condition, which obviously is too strong an assumption and thus unrealistic for many hybrid simulation applications.

# III. COMPREHENSIVE PHASOR-DOMAIN MODELING AND SIMULATION CAPABILITIES

# A. Comprehensive Phasor-Domain Modeling Capabilities

Conventional transient stability simulation is developed based on positive-sequence phasor modeling of all power system components. Most of previous hybrid simulation solutions were developed based on positive-sequence phasor modeling [2], [3], [6], [7]. However, such a modeling approach is only suitable for three-phase balanced conditions. Consequently, when there are unbalanced conditions in the detailed system and/or the external system, it is challenging to interface with an EMT simulation. To overcome this drawback, the authors have developed a three-sequence transient stability simulation algorithm for an improved hybrid simulation algorithm in [8]. For both positivesequence and three-sequence modeling approaches, the resulting hybrid simulation is only suitable for modeling transmission systems in the external system. One important objective of this paper is to further enhance the modeling capabilities of the program in [8] such that the new hybrid simulation program can be readily applied to integrated T&D systems and distribution systems. This means the new program should support the three-phase modeling capability for the distribution systems. A three-phase and mixed three-phase/three-sequence modeling framework has been developed in the authors’ previous work [17]. Thus, the phasor-domain dynamic simulation tool used in the paper has comprehensive modeling capabilities as shown in Fig. 3.

# B. Multi-Area Thevenin Equivalent Based ´ Dynamic Simulation

A multi-area Thevenin equivalent (MATE) based dynamic ´ simulation algorithm has been developed in [17]. With this

simulation approach, the whole system can be partitioned into several subsystems. The subsystems are interconnected through link branches (as shown in Fig. 3 in [17]). The MATE approach is used to reconcile the individual solutions of subsystems into a full-system simultaneous solution at the network solution stage for each time step. More details of the MATE-based dynamic simulation can be found in [17].

# IV. PROPOSED HYBRID SIMULATION WITH AN IMPROVEDSIMULATION MODE SWITCHING SCHEME

# A. Overview of the Proposed Hybrid Simulation Design

The proposed hybrid simulation solution for switching from the hybrid simulation to the TS simulation extends the basic idea of the approach discussed in [2]. In the proposed approach, the hybrid simulation program developed by the authors in [8], the comprehensive modeling framework and the MATE-based dynamic algorithm presented in Section III are integrated. In this research, PSCAD/EMTDC [21] is selected as the EMT simulator and the open source power system simulation engine InterPSS [22] is chosen as the phasor-domain simulator. Significant improvements have been made to address the drawbacks of the original approach proposed in [2]. The main issue of discrepancy in simulation results between the EMT and TS simulation of the detailed system is addressed from both the modeling and simulation result coordination perspectives:

Firstly, from the modeling perspective, the three-phase phasor modeling inherently relates more closely to the three-phase point-on-wave modeling used in the EMT simulation than the positive-sequence and three-sequence phasor modeling. The developed program supports three-phase phasor modeling. This feature is particularly useful when there are some models (e.g., single-phase induction motors) and/or contingencies that are better modeled in phase-oriented representation in the detailed system.

Secondly, the phasor-domain models and the EMT models of dynamic components could produce consistent fundamental frequency, slow dynamic responses only when they are under the same operating state (for example, running or stalling for A/C motors, normal operating, blocking, or recovering for HVDC systems). It is observed from past simulation experiences that major simulation result discrepancies between the EMT and the TS simulations at the post-disturbance stage are usually related to specific control actions and/or operation state changes of some critical components modeled in the detailed system. The main reason for this discrepancy is that these actions and/or state changes may not be correctly represented by the phasor representation or captured by the TS simulation due to some inherent modeling and simulation limitations [18]. Therefore, in the proposed approach, besides the updated network equivalent data, these discrete event or control signals obtained from EMT simulation results are transferred back to the TS simulation of the detailed system. These important signals can be, for example, a converter blocking signal when an HVDC inverter is undergoing commutation failure or a state change signal of an A/C motor when the motor stalls. These signals are used as external control inputs to override the corresponding

![](images/c5b8c6748b098f8aede83ddb89aa502b949c592184f41534f28cf03021eb34c5.jpg)  
Fig. 4. (a) The full network. (b) The full network is split into the detailed system and the external system connected by virtual breakers. (c) Representations of the detailed system and the external system used in the proposed method.

control signals or to change the states of the corresponding models in the TS simulation. Thus, the incorporation of discrete event signals help ensure that these critical dynamic models are operating under the same state, and thus help both simulation results converge after the fast dynamics settle.

It should be emphasized that the objective of reconciling the simulation results of two representations of the detailed system by sharing the discrete event signal(s) is to help them to converge at the end of the stage 2, rather than to rectify all the differences between the phasor and EMT representations.

In addition, after switching back to the TS simulation mode, re-connecting the two phasor-domain systems into a full network becomes unnecessary with the proposed approach. The detailed and the external systems are still modeled as two subsystems in the MATE-based dynamic simulation.

With the proposed simulation algorithm, the full system is split into two parts, i.e., the detailed system and the external system, using the bus splitting method as shown in Fig. 4(a) and (b). For each boundary bus, a dummy bus is created during the network splitting stage. In order to make the splitting scheme compatible with the MATE-based dynamic simulation algorithm, a “virtual breaker” is introduced to link the original boundary bus and the dummy bus. The detailed system has two representations, i.e., EMT- and phasor-domain representations, as shown in Fig. 4(c).

Regarding the modeling requirements, the developed algorithm only requires that the phasor-domain and EMT representations of the detailed system produce consistent fundamental frequency responses during the stages 1 (no fault) and 3 (post fault, slow dynamics), and with the discrete signal(s) to help reconcile the simulation results, their responses converge at the end of stage 2. In other words, for most of the time during the stage 2 (when the detailed system undergoes fast dynamics or transients), our developed algorithm does not require both representations to produce consistent results. Therefore, some inherent differences between the two representations (e.g., high frequency responses) have been considered and can be tolerated by the developed algorithm. These modeling requirements are less strict than those required in [2] and they can be met with some feasible but not significant extensions to conventional hybrid simulation, which will be discussed in the following subsection.

The EMT representation of the detailed system is developed based on the requirements of the phenomenon of interest and detailed models involved in the study. The phasor-domain representation of the detailed system is developed with reference to the EMT representation counterpart, through the following four main steps:

a) Model the static components in the detailed system, such as transmission lines, transformers, capacitors, with their phasor-domain representations; then model the dynamic components with their static equivalent generation and/or load models whose parameters are determined based on the initialization results of the EMT representation;   
b) Run power flow with the phasor-domain representation of the detailed system, and then compare the power flow results with the no-fault EMT simulation results of the detailed system and make sure the steady-state results are consistent; any inconsistency in this step means modeling inconsistency or errors in the static models, go back to step a) to check the models and fix them;   
c) Once the static models are set up correctly, model the dynamic components with their appropriate, available phasor-domain dynamic models;   
d) Perform another sanity check—run some simulations with a fault in the two representations of the detailed system (using fixed external system equivalents at this modeling stage) respectively and compare their results. Their fundamental frequency responses should be consistent if the dynamic models are operating in the same state; otherwise, fix the modeling inconsistency or errors.

Models of both representations of the detailed system and the external system have to be developed before hybrid simulation. The external system is by default modeled in the three-sequence phasor representation.

The interactions between the detailed system and the external system for the three stages are shown in Fig. 5. The mutual representations of the detailed and external systems are different at different stages of hybrid simulation. As shown in Fig. 5(a), in stages 1 and 3 of hybrid simulation, the Thevenin equivalents ´ of the detailed and external systems are calculated for each system. But they are not directly added to each system, instead

![](images/6f46fe2441b4fad289de949e52ca99bee2a1ac42c87a082eb49e049d5b767773.jpg)

![](images/36238406176cdfd00d96a1fe0303f803a26b7d08fdefaa9105ef94dcd1236338.jpg)  
Fig. 5. Interactions and equivalent data exchanges between the detailed and the external systems. (a) For both stages 1 and 3. (b) For stage 2.

they are used to build a link subsystem, which produces the current injections at the boundary for the detailed and external systems. This is the multi-area Thevenin equivalent approach ´ [17] presented in Section III-B.

As shown in Fig. 5(b), in stage 2 of hybrid simulation, the detailed system is represented as three-sequence current injections (extracted from the instantaneous waveforms) in the external system, while the external system is represented as three-phase Thevenin equivalent. The approach shown in Fig. 5(b) will be ´ discussed in detail in the following Section IV-B.

In stage 1, the EMT representation will be initialized and running in parallel with the TS simulation till the time duration for stage 1; in stage 3, the EMT portion of the simulation is halted by default in the current implementation as the phasordomain counterpart takes its place. Since the EMT part can be run on a different core or different computer, it will not be a performance bottleneck for the developed algorithm.

# B. Extend Conventional Hybrid Simulation Program to Realize Simulation Mode Switching

For the stage 2, the hybrid simulation program developed in [8] has been extended. The hybrid simulation is augmented by running the dynamic simulation of the phasor-domain detailed system and the switch controller in parallel to the existing hybrid simulation algorithm, as shown in Fig. 5(b). The actual implementation of the augmented hybrid simulation algorithm is illustrated in Fig. 6. The enhancement to the original development in [8] is shown within the dashed rectangular in Fig. 6(a). In both figures, t denotes the start time for the processing step, ΔT is TS simulation time step as well as the EMT-TS interaction time step, I120E M T (t $I _ { E M T ( t ) } ^ { 1 2 0 }$ ) and I120E M T $I _ { E M T ( t - \Delta T ) } ^ { 1 2 0 }$ (t ΔT ) are the three sequence current injection vectors sent from the EMT side at the present and

previous interaction time step, respectively; $x _ { d e ( t ) }$ and $x _ { e x ( t ) }$ denote the monitored state variables of the detailed and external systems; V abc $V _ { d e ( t ) } ^ { a b c }$ denotes three-phase voltages of the boundary bus of the phasor-domain detailed system; $V _ { e x ( t ) } ^ { 1 2 0 }$ ) represents three-sequence voltages of the boundary buses of the external system.

The sequence of the main steps in stage 2 of hybrid simulation is also shown in the circles in Fig. 6(a). The first step is data transfer from EMT side to the phasor domain simulator via a socket and pre-processing. In step -2 , $I _ { E M T ( t ) } ^ { 1 2 0 }$ is used as the input for the three-sequence TS simulation and the three-sequence voltages of the boundary buses V 120ex(t $V _ { e x ( t + \Delta T ) } ^ { 1 2 0 }$ are updated. Subsequently, the three-phase Thevenin equivalent voltages ´ $V _ { T ( t + \Delta T ) } ^ { a b c }$ are derived in step $\textcircled{3}$ and sent back to the EMT side in step -4 . On receiving V abcT (t+ΔT ) , the EMT simulator contin- $V _ { T ( t + \Delta T ) } ^ { a b c }$ ues to run consecutive multi-step EMT simulations in parallel of phasor-domain simulation until the next interaction time step. At the same time, a three-phase Norton equivalent is converted from the three-phase Thevenin equivalent in step ´ -5 , and used as the external system equivalent in the dynamic simulation of the detailed system in step 6 . In the last step 7 , the hybrid simulation switching controller determines whether the simulation mode can be switched from hybrid simulation to pure phasor domain simulation at the next time step.

The main reason for using Norton equivalent is that the network solution is usually formatted as $\bar { I } ( x , V ) = Y V$ in the dynamic simulation, and the form of Norton equivalent fits the formulation very well, with the current source part being added to the left-hand side, and the admittance part being added to the right-hand side. The admittance matrix of the detailed system is augmented with admittance matrix of the three-phase Norton equivalent after switching from the stage 1 to stage 2. The three-phase current source of the Norton equivalent is directly used in the network solution step. When switching from stage 2 to stage 3, the admittance matrix of the detailed system has to be rebuilt to account for the removal of the admittance matrix of the three-phase Norton equivalent.

The simulation mode switching process is controlled by the hybrid simulation switching controller. There are two basic principles behind this controller: 1) simulation switching is only performed after the system enters a slow dynamic state; 2) simulation switching is only performed after the boundary conditions of the detailed and external systems truly converge. Based on these two principles, this controller is designed as shown in Fig. 6(b). It includes three main parts, i.e., a time delay to bypass the transient period, system state monitoring based on the maximum rate of change of boundary voltages, checking the convergence of results of the two models of the detailed system. Firstly, a time delay is necessary to account for the period of the system transiting from a fast dynamic (transient) state to a slow dynamic state where the system can be adequately represented by phasor models. Based on the simulation experiences, the delay setting $( T _ { D e l a y } )$ is chosen to be 0.2 s in this paper. Once the time delay criterion is met after a fault is cleared, the switching controller begins to check whether the maximum rate of change of the boundary voltages is small

![](images/1ccf7e1c0e2040a862d58833a25a02003df61b517560dfda0d8b9f5aa3264e46.jpg)

![](images/eab638a14278c918f387be2b9069a73319cdbec63962ba357771b7a737f312b7.jpg)  
(a)   
(b)   
Fig. 6. Implementations of the augmented hybrid simulation at the stage-2. (a) The overall simulation process (modified based on the Fig. 2 in [8]). (b) The logic of the simulation switching controller in step 7.

enough $( \varepsilon _ { 1 } ~ = 0 . 0 0 5 \mathrm { p u }$ in this paper) to ensure the systems truly enter the slow dynamic state. Secondly, the voltages of the boundary buses between the detailed system and the external system are monitored and the maximum difference between them is used as the indicator for simulation switching. At each step, this indicator is calculated and compared with a preset tolerance (for example, $\varepsilon _ { 2 } ~ = 0 . 0 0 5 \mathrm { p u } )$ . Furthermore, in order to make sure the boundary conditions of the detailed and external systems truly converge, the maximum voltage difference must be within the preset tolerance for a reasonably long period (e.g., 3–5 cycles). This is implemented in the delay counter block at the end of Fig. 6(b). If both the mismatch and time period criteria are satisfied, the simulation switch controller outputs a signal to indicate that the simulation can be switched to the TS simulation starting from the following time step. With this implementation, the first two parts ensure the first principle is

satisfied and the last part guarantees that two parts of the system converge before simulation mode switching.

# V. TEST CASE AND RESULTS

# A. Test Case

The developed advanced hybrid simulation program has been tested with a modified IEEE 9 bus system [19]. In this test case, the original aggregated load at bus 5 is replaced by an equivalent sub-transmission and distribution system, as shown in Fig. 7. Modeling of the sub-transmission and distribution system is shown in Fig. 8. The loads are connected to an equivalent feeder. As for the load composition, 50% of the total load in terms of active power is represented by single-phase residential A/C motors, while the remainder is modeled as constant impedances. The portion of the system highlighted in Fig. 7 and shown in

![](images/ce36bc2f694e1d2175b79623f8cfa22b9c0c9deaabe2015372c164dd4c321798.jpg)  
Fig. 7. One-line diagram of a modified IEEE 9 bus system.

![](images/b457ae55a2278a58da59572f0c2f07f451ed3e53c9c90e3ad475b6af1901e08e.jpg)  
Fig. 8. The sub-transmission and distribution system served by bus 5.

Fig. 8 is modeled as the detailed system. The remainder of the system is modeled as the external system and represented in three-sequence phasor domain. As discussed in Section IV-A, there are two representations of the detailed system, i.e., EMT and phasor-domain. When the detailed system is simulated by EMT simulation, an EMT detailed A/C motor model developed in [9] is used. The important effect of the point-on-wave where a fault or voltage sag is initiated on motor stalling can be captured by this model [9]. On the other hand, when the detailed system is represented by phasor-domain and simulated by three-phase dynamic simulation, a performance model of A/C motor [20] is used to represent the A/Cs. The performance model represents the operation of the A/C motors with two states, i.e., running and stalled, and each state has its own performance curve. In this test case, the TS simulation time step is 0.005 s and the EMT simulation time step is 20 μs.

# B. Use of Discrete Event Signals to Reconcile the Two Detailed System Simulations

The following two simulation cases in this section are to study the convergence of results obtained from the EMT simulation and the 3-phase dynamic simulation for the detailed system during stage 2. The convergence of both results is the prerequisite for realizing simulation mode switching from hybrid simulation to pure phasor-domain simulation.

A single-line-to-ground (SLG) fault is applied to bus 10 at 0.5 s and cleared after 0.07 s. In order to study the effects of using discrete event signals from the EMT side to enhance the accuracy of TS simulation, the simulation switching function

is intentionally disabled. The simulation results without and with sending the A/C motor operation status signals from the EMT simulation to the 3-phase dynamic simulation are shown in Figs. 9 and 10, respectively. A/C motor operation status signals indicate whether the A/C motors are running or stalled, which are used to determine the state of the corresponding A/C models in the phasor-domain representation. Note that both curves in Figs. 9 and 10 are obtained during the stage 2 of hybrid simulation for the two models of the detailed system. The curves labeled “EMT” are results of the EMT model (not full EMT simulation of the whole system), while the curves labeled “3-φ DS” are results of the phasor-domain model.

In the scenario without sending the A/C motor operation status signals from the EMT side to three-phase dynamic simulation, simulation results of the EMT and the dynamic simulation are significantly different in terms of A/C motor stalling. A/C motors on two phases stalled (status = 0) in the detailed system simulated by the 3-phase dynamic simulation. In contrast, the EMT simulation results show that only the A/C motor on phase C stalled. This difference is mainly due to the fact that the fault point-on-wave effects on A/C motor stalling [8], [9] cannot be accurately captured by the phasor-domain modeling and simulation. This difference results in significant differences between the two simulation results in the three-phase voltages of the boundary bus (bus 5 in this case), as shown in Fig. 9. Consequently, the proposed simulation switching criteria are never satisfied and the simulation keeps running in the hybrid simulation mode till the end of the whole simulation.

In the scenario in which the A/C motor operation status signals are sent from the EMT side to the 3-phase dynamic simulation, the A/C stalling results are coordinated to make sure A/C motors in the three-phase dynamic simulation have the same status as those simulated by the EMT simulation during stage 2. While there are some discrepancies observed in the three-phase boundary bus voltages after the fault is cleared, the discrepancies last only a short time period (approximately 0.15 s) and disappear after the A/C motor on phase C effectively stalls in both the EMT simulation and the three-phase dynamic simulation.

The discrepancies in Fig. 10 discussed above are related to the A/C motor stalling process, which is adequately simulated in the EMT simulator, but cannot be represented by the performance model of the A/C motor in the dynamic simulation. During the A/C motor stalling process, the reactive power drawn by the A/C motor on phase C increases significantly when the A/C motor speed decreases to lower than 0.5 pu. The increased reactive power consumption depresses the voltages of both phase A and C of bus 5 after the fault is cleared, as shown in the solid black traces in Fig. 10(b1)–(b3). On the other hand, before receiving the A/C motor stalling signals from the EMT side, all three A/C motors operate in the running mode (status =1) in the detailed system simulated by the three-phase dynamic simulation. After the fault is cleared, the bus voltages recover to the levels close to their pre-fault values, as illustrated by the dashed blue traces in Fig. 10(b1)–(b3). These different responses of the A/C motors in the two detailed system simulations contribute to the discrepancies shown in Fig. 10.

![](images/1ce4c53c27d6dd34494c206954e430fb8be3ed9073f2e84cf5dc0cefd9334fe0.jpg)  
(a1)

![](images/227fe444914cba2d1c3c4a0c05b97e07b9dd1e9dd2da79c89ea8cf5fde7983a3.jpg)  
(a2)

![](images/d1823fd065081bfeaef115886bc54c7f38df456db4cf822850c6dd9295070582.jpg)  
(a3)

![](images/057228a6427e506bf53978df82765134ed126b507b3a0f81f813fe92565d5d0f.jpg)  
(b1)

![](images/39200a66c15cbf67a4cd0ae51271eff6b98ffd9abd8b0212feb03af2cfce6c18.jpg)  
(b2)

![](images/2ee252e08739e29993bf47efa117820ff565fe9b842844a149b773832666eb6c.jpg)  
(b3)   
Fig. 9. Simulation results of the detailed system without sending the A/C motor status signals from the EMT simulation to the 3-phase dynamic simulation.

![](images/6bbf156742002e88caa71df08fb7c77dc2caddd9ddd0448b7c936051c13a131e.jpg)  
(a1)

![](images/a1a16946d2515284577605de1c0eb787babd06d7de07cc6ddae48ee4745011f4.jpg)

![](images/745f9477933dcf6558ab5ccc7c36501e91f9cb542a0422f92929aa896cb62b9a.jpg)  
(a3)

![](images/99b8f247b11ae6519c7b50ed7ac82afa2a8a95bb9250f054c510421192d9dfa5.jpg)  
(b1)

![](images/c0d92e7298f1cee14b83de7e8577525d1fd2f006ead8fe414ed2757734be8ae1.jpg)

![](images/40ec5c9ff935267aa5d3dae13529474df3a18469a6423b8ade228354f252186d.jpg)  
  
Fig. 10. Simulation results of the detailed system with sending the A/C motor status signals from the EMT simulation to the 3-phase dynamic simulation.

![](images/2a65f87f5046e1c0ea1d1aad8488920e8addcfe551d69309449fe1b5b46a7293.jpg)  
Fig. 11. The maximum voltage difference of boundary buses and the switching signal.

# C. Criteria for Switching From Hybrid Simulation to Phasor-Domain Dynamic Simulation

In this test, the switching criterion is as follows: starting at 0.2 s after the fault is cleared, if the maximum difference of boundary bus voltages (maxΔV) obtained by the dynamic simulation of the detailed and the external systems is less than 0.005 pu for more than 2 cycles, simulation will be switched from the hybrid simulation mode to the phasor-domain DS mode.

The results in the previous subsection showed that the proposed approach can significantly reduce the simulation result discrepancy caused by the modeling difference of A/C motors in the EMT and the TS simulation by coordinating the discrete motor stalling events in the EMT simulation with the TS simulation. With this approach applied to the test case, the monitored maximum bus voltage difference during stage 2 is shown in Fig. 11. The simulation is switched from the hybrid simulation to the pure TS simulation at 0.805 s, which is 0.235 s after the fault is cleared. It should be emphasized that the switching is performed under a dynamic, non-steady-state system condition, which is shown in the generator speeds in Fig. 12.

# D. Result Comparisons

The simulation results are compared with those simulated by the conventional hybrid simulation approach without switching back to TS simulation, which are shown in Figs. 12 and 13. The results of both approaches match closely, demonstrating the effectiveness of the proposed approach. The computational time for a 10-second simulation with different methods is shown in Table I. Compared to the hybrid simulation without switching back to TS simulation, the developed hybrid simulation switching method reduces the computational time by 91.86%.

Additionally, the developed program has been compared with conventional positive sequence TS simulation and full EMT simulation. The distribution system is modeled by single-phase representation (one A/C motor performance model for representing A/C motors on three phases) and the entire system is simulated positive sequence TS simulation. The results show that all A/C motors served by the substation of bus 5 stall for the same SLG fault at bus 10. This means conventional TS

![](images/6c8f3c9f20a4b304c48b9c833ddcb47e6b83c623845629e3e7cf5d26310fcb0c.jpg)  
Fig. 12. Speeds of the generators at buses 1, 2 and 3.

![](images/1b50b36818588f49eca0732aef9ed16f935a14123e8fdc22b40006bef763525b.jpg)

![](images/91ba1ea57ee7ac1a5add0ff217641c61c5b8b53b79afa56228f1b4cf3705544a.jpg)  
Fig. 13. Positive sequence voltages of bus 5 and bus 7 simulated by hybrid simulations and full EMT simulation.

TABLE I THE COMPUTATIONAL TIME OF DIFFERENT METHODS   

<table><tr><td>Simulation method</td><td>Computational time /s</td></tr><tr><td>Hybrid simulation without switching back to TS simulation (developed in [8], [14])</td><td>189.2</td></tr><tr><td>Hybrid simulation with switching back to TS simulation (developed in this paper)</td><td>15.4</td></tr></table>

simulation produces significantly different results from that simulated by hybrid simulation. To illustrate the differences, the positive sequence voltages of bus 5 in both results are shown in Fig. 14.

![](images/113757f7b19594e3c46d8a6b8942a590485b582cefaafc33502e8c938a99395c.jpg)  
Fig. 14. Positive sequence voltages of bus 5 simulated by positive sequence TS simulation, full EMT simulation and the developed hybrid simulation (the full EMT simulation result has been re-sampled at a larger time step for this plot).

# VI. DISCUSSIONS

While only one particular application is shown in this paper, as an advanced hybrid simulation tool, this tool can be applied to many applications that involve large systems and require hybrid simulation to achieve high-fidelity results, including, but not limited to, detailed analysis of fault-induced delayed voltage recovery events [8], transient stability analysis of power systems with HVDC [14] and/or FACTS, large wind or PV farm integration studies, dynamic simulation of distribution systems with a high penetration of DER [15], protection setting of distribution systems with a high penetration of DER. An older version of this tool has been applied to study fault-induced delayed voltage recovery events on a large-scale planning case of the Western Interconnection of U.S., which consists of more than 15000 buses and 3000 generators, and a portion of the system with more than 200 buses (8 boundary buses) are modeled in detail in the EMT part [8]. Thus, the scalability of the tool has been tested and proven in [8]. The tool has also been applied to detailed AC/DC power system dynamic simulations [14].

As this tool provides comprehensive modeling capabilities, and supports three-phase and three-sequence phasor domain modeling for the detailed and external systems, both balanced and unbalanced faults can be considered in either system. If the event is inside the external system, the effects of the event are first captured by the phasor-domain simulation and subsequently reflected in the detailed system by updating the Thevenin equiv- ´ alent of the external system. These capabilities overcome many limitations associated with positive-sequence only TS and hybrid simulation approaches.

# VII. CONCLUSION

In this paper, an advanced EMT-TS hybrid simulation software package with the capabilities of comprehensive phasordomain modeling and switching back to the TS simulation is developed. With this package, a whole simulation is divided

into three stages, i.e., pre-fault TS simulation stage, faulted and post-fault hybrid simulation stage and post-disturbance TS simulation stage. To address the initialization issue of switching from EMT simulation to TS simulation, a three-phase phasor representation of the detailed system is simulated in parallel of the hybrid simulation. Furthermore, the critical discrete events captured in the EMT simulation are used to improve the accuracy of the dynamic simulation of the detailed system to address the simulation result discrepancy issue caused by the modeling differences between the EMT and the TS simulation. The test results show that, with the developed simulation switching method, the total computational time is significantly reduced compared to running the hybrid simulation for the whole simulation period, while a good accuracy is maintained.

# REFERENCES

[1] L. M. Tolbert et al., “Power electronics for distributed energy systems and transmission and distribution applications,” Oak Ridge Nat. Lab., Oak Ridge, TN, USA, Tech. Rep. ORNL/TM-2005/230, 2005.   
[2] G. W. J. Anderson, N. R. Watson, C. P. Arnold, and J. Arrillaga, “A new hybrid algorithm for analysis of HVDC and FACTS systems,” in Proc. Int. Conf. Energy Manage. Power Del., 1995, vol. 2, pp. 462–467.   
[3] M. Sultan, J. Reeve, and R. Adapa, “Combined transient and dynamic analysis of HVDC and FACTS systems,” IEEE Trans. Power Del., vol. 13, no. 4, pp. 1271–1277, Oct. 1998.   
[4] V. Jalili-Marandi, V. Dinavahi, K. Strunz, J. A. Martinez, and A. Ramirez, “Interfacing techniques for transient stability and electromagnetic transient programs,” IEEE Trans. Power Del., vol. 24, no. 4, pp. 2385–2395, Oct. 2009.   
[5] Y. Zhang, A. M. Gole, W. Wu, B. Zhang, and H. Sun, “Development and analysis of applicability of a hybrid transient simulation platform combining TSA and EMT elements,” IEEE Trans. Power Syst., vol. 28, no. 1, pp. 357–366, Feb. 2013.   
[6] F. Plumier, P. Aristidou, C. Geuzaine, and T. Van Cutsem, “A relaxation scheme to combine phasor-mode and electromagnetic transients simulations,” in Proc. Power Syst. Comput. Conf., Wroclaw, Poland, Aug. 2014, pp. 1–7.   
[7] A. A van der Meer, M. Gibescu, M. A. M. M. van der Meijden, W.L. Kling, and J.A. Ferreira, “Advanced hybrid transient stability and EMT simulation for VSC-HVDC systems,” IEEE Trans. Power Del., vol. 30, no. 3, pp. 1057–1066, Jun. 2015.   
[8] Q. Huang and V. Vittal, “Application of electromagnetic transient-transient stability hybrid simulation to FIDVR study,” IEEE Trans. Power Syst., vol. 31, no. 4, pp. 2634–2646, Jul. 2016.   
[9] Y. Liu, V. Vittal, J. Undrill, and J. H. Eto, “Transient model of airconditioner compressor single phase induction motor,” IEEE Trans. Power Syst., vol. 28, no. 4, pp. 4528–4536, Nov. 2013.   
[10] California Commercial End-Use Survey (CEUS). 2017. [Online]. Available: http://www.energy.ca.gov/ceus/index.html   
[11] F. Gao and K. Strunz, “Frequency-adaptive power system modeling for multiscale simulation of transients,” IEEE Trans. Power Syst., vol. 24, no. 2, pp. 561–571, May 2009.   
[12] T. Yang, S. Bozhko, J. M. Le-Peuvedic, G. Asher, and C. I. Hill, “Dynamic phasor modeling of multi-generator variable frequency electrical power systems,” in IEEE Trans. Power Syst., vol. 31, no. 1, pp. 563–571, Jan. 2016.   
[13] X. Lin, A. M. Gole, and Y. Ming, “A wide-band multi-port system equivalent for real-time digital power system simulators,” IEEE Trans. Power Syst., vol. 24, no. 1, pp. 237–249, Feb. 2009.   
[14] Q. Huang and V. Vittal, “OpenHybridSim: An open source tool for EMT and phasor domain hybrid simulation,” in Proc. IEEE Power Energy Soc. Gen. Meeting, Boston, MA, USA, 2016, pp. 1–5.   
[15] A. Hariri and M. O. Faruque, “A hybrid simulation tool for the study of PV integration impacts on distribution networks,” in IEEE Trans. Sustain. Energy, vol. 8, no. 2, pp. 648–657, Apr. 2017.   
[16] S. Zhang, Y. Zhu, K. Ou, Q. Guo, Y. Hu, and W. Li, “A practical real-time hybrid simulator for modern large HVAC/DC power systems interfacing RTDS and external transient program,” in Proc. IEEE Power Energy Soc. Gen. Meeting, Boston, MA, USA, 2016, pp. 1–5.

[17] Q. Huang and V. Vittal, “Integrated transmission and distribution system power flow and dynamic simulation using mixed three-sequence/threephase modeling,” in IEEE Trans. Power Syst., vol. 32, no. 5, pp. 3704– 3714, Sep. 2017.   
[18] J. Arrillaga and N. R. Watson, Computer Modelling of Electrical Power Systems, 2nd ed. New York, NY, USA: Wiley, 2003.   
[19] P. M. Anderson and A. A. Fouad, Power System Control and Stability. New York, NY, USA: IEEE Press, 1994.   
[20] D. Kosterev et al., “Load modeling in power system studies: WECC progress update,” in Proc. IEEE Power Energy Soc. General Meeting, 2008, pp. 1–8.   
[21] Manitoba HVDC Res. Centre, Winnipeg, MB, Canada, PSCAD/EMTDC. 2017. [Online]. Available: https://hvdc.ca/pscad/   
[22] M. Zhou and Q. Huang, “InterPSS: A new generation power system simulation engine,” arXiv preprint arXiv:1711.10875, pp. 1–8, 2017. [Online]. Available: https://arxiv.org/abs/1711.10875

Qiuhua Huang (S’14–M’16) received the B.E. and M.S. degrees in electrical engineering from the South China University of Technology, Guangzhou, China, in 2009 and 2012, respectively, and the Ph.D. degree in electrical engineering from Arizona State University, Tempe, AZ, USA, in 2016. He is currently a Research Engineer with the Pacific Northwest National Laboratory, Richland, WA, USA. His research interests include power system modeling, simulation and control, transactive energy, and application of advanced computing and machine learning technologies in power systems.

Vijay Vittal (S’78–F’97) received the B.E. degree in electrical engineering from the B.M.S. College of Engineering, Bengaluru, India, in 1977, the M.Tech. degree from the Indian Institute of Technology Kanpur, Kanpur, India, in 1979, and the Ph.D. degree from Iowa State University, Ames, IA, USA, in 1982.

He is the Ira A. Fulton Chair Professor with the Department of Electrical, Computer and Energy Engineering, Arizona State University, Tempe, AZ, USA. He is currently the Director of the Power System Engineering Research Center, Arizona State University.

He is a member of the National Academy of Engineering.