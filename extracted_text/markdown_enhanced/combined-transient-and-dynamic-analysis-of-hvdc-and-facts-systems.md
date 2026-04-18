# COMBINED TRANSIENT AND DYNAMIC ANALYSIS OF HVDC AND FACTS SYSTEMS

**M. Sultan** (Member)  
Hatch Associates, Mississauga, Ontario

**J. Reeve** (Fellow)  
University of Waterloo, Waterloo, Ontario

**R. Adapa** (Senior Member)  
Electric Power Research Institute, Palo Alto, CA

**Abstract**  
A new approach to HVDC and FACTS transient/dynamic simulation based on an interactive execution of an ac transient stability program (TSP) and the Electro-Magnetic Transients Program (EMTP) is described. Through the integration of the detailed transient model of FACTS with the transient stability program, authentic simulation is achieved without simplifications. Both HVDC and Thyristor Controlled Series Capacitor (TCSC) systems are used to validate the approach, under different coupling situations between both TSP and EMTP.

**Keywords:** FACTS, HVDC, EMTP, Frequency Dependent Network Equivalents, Transient Stability Simulation.

## I. INTRODUCTION
The ac transient stability programs based on fundamental frequency, single-phase, phasor modeling techniques cannot directly represent the faster transients characterizing the HVDC and FACTS systems. Nor can they accommodate the implied waveform distortion, phase imbalance, and discrete action of semiconductor switches at different time instants. The current approach to dc system or FACTS modeling in an ac transient stability program is by a quasi steady-state model which is developed for a particular disturbance, based upon physical simulation and/or detailed transient analysis.

There is a need to use a transient stability program (TSP) for extensive ac network modeling outside the domain of a disturbance and at the same time to represent the parts of the network vulnerable for a disturbance in greater detail for transient/dynamic analysis. It is necessary to have a realistic interaction between the two simulations to predict the overall performance of the system. A new approach for ac/dc and FACTS transient studies based on this concept is presented, relevant to the performance of current developments and future high power electronic controllers in power systems.

## II. REVIEW OF DETAILED ANALYSIS TRENDS
One common approach to studying HVDC and FACTS systems is by modeling them in a detailed analysis environment such as EMTP or EMTDC programs [1][2][3]. It is compromised by the limited representation of the ac system.

A method to deal with the problem of waveform distortion was introduced in [5][6]. The approach uses interactive execution of EMTP for detailed transient analysis and TSP for external ac system representation. The problems of wave distortion and asymmetry [4] were resolved by extending the interface location between the detailed and external systems further into the external ac system.

The interface of frequency domain program with the detailed modeling of EMTP was presented in [7]. For validity of simulation the external ac system must be linear time invariant, and should be connected to the detailed system through a transmission line. Fourier transforms provide the conversion from time domain to frequency domain and vice versa. The major restrictions of this approach are inherent in the assumptions - ac machines, controls, etc are excluded.

NETOMAC [8] is an alternative to EMTP with a built-in TSP capability. The program has two separate simulation modes. The instantaneous mode models the system in three phase detail, while the transient stability mode models the system in a single phase basis. The program can switch between the two modes as required while running. In either mode, however, the entire system has to be modeled in the same way.

The program described in [9] uses an interactive facility between a TSP and EMTDC. The implementation details and interaction philosophy resemble that of [5], with the major change of using a frequency dependent equivalent for the TSP system in the EMTDC. The system faults are incorporated into the EMTDC and TSP solutions, a mechanism avoided in the work of this paper [10].

This paper describes new developments, performed at the University of Waterloo, for enhanced integration of EMTP into a transient stability program, as part of a research contract [10] with EPRI, in the context of FACTS controllers.

## III. NEW SIMULATION CONCEPT
### General concept
Variations in performing the HVDC/FACTS transient analysis are shown in Fig. 1. Fig. 1(a) shows a detailed simulation of the HVDC/FACTS system along with an over simplified ac system. In other words, the entire ac system is reduced to a simple equivalent for dynamic analysis[1]. In Fig. 1(b) the detailed simulation is constrained to be within the terminal ac buses of the detailed system model, while the ac system is modeled with a conventional transient stability program [4]. In this way, the gross impact of the ac system on the detailed system is updated at regular time intervals. The concept shown in Fig. 1(c) was adopted in [5]. The detailed system is extended outward to take into consideration more ac system for 3-phase representation. This paper has selected the new approach (indicated by the arrows marked 3PFDEM in Fig. 1 (b) and (c)) as the most versatile and accurate method. The approach uses a time varying Thevenin or Norton frequency dependent equivalent for representation of the external ac system into the detailed simulation. It has been developed with alternative