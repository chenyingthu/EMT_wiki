# Stability Assessment of Multi-Rate Electromagnetic Transient Simulations

**Ajinkya Sinkar**, Member, IEEE, **Kaustav Dey**, Member, IEEE, **Huanfeng Zhao**, Member, IEEE, and **Aniruddha M. Gole**, Life Fellow, IEEE

**Abstract**—Multi-rate Electromagnetic Transient (EMT) simulations use smaller time-steps for parts of the network requiring greater accuracy, and larger time-steps for the rest of the network. This paper presents an analytical approach for evaluating the stability of multi-rate EMT simulations of linear time-invariant (LTI) networks. It is shown that their resulting discrete time system is inherently time-periodic. Leveraging this characteristic, a sampled-data time-invariant representation of the simulated network is derived. The overall simulation’s numerical stability can then be assessed through eigenvalue analysis. The paper shows that contrary to popular belief, a multi-rate EMT simulation may become unstable even if the well-known A-stable trapezoidal rule is used. The proposed approach is validated with example simulations.

**Index Terms**—Electromagnetic transient (EMT) simulations, linear time invariant (LTI) systems, multi-rate simulations, stability assessment.

*Received 29 October 2024; revised 15 March 2025 and 31 May 2025; accepted 12 July 2025. Date of publication 18 July 2025; date of current version 24 November 2025. This work was supported in part by the IRC Program of NSERC, Canada and in part by Mitacs Elevate Program, Canada under Grant IT40444. Paper no. TPWRD-01639-2024. (Corresponding author: Ajinkya Sinkar.)*

Ajinkya Sinkar and Aniruddha M. Gole are with the Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB R3T 2N2, Canada (e-mail: sinkara@myumanitoba.ca; gole@umanitoba.ca).

Kaustav Dey was with the Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB R3T 2N2, Canada. He is now with the Department of Electrical Engineering, Indian Institute of Technology Kharagpur, Kharagpur 721302, India (e-mail: kaustav@ee.iitkgp.ac.in).

Huanfeng Zhao is with Nayak Corporation, Hamilton, NJ 08619 USA (e-mail: huanfengzhao@gmail.com).

## I. INTRODUCTION

Traditionally, Electromagnetic Transient (EMT) simulations have used a single fixed time-step for discretizing the dynamical equations of all the components in a network [1]. However, this can lead to the simulations becoming computationally intensive as this time-step, which is selected to capture the fastest transients in a network, is also used for solving relatively slower portions of the network [2]. A computationally efficient alternative to this proposed in the literature is to use the multi-rate simulation approach [2], [3], [4], [5], [6], [7].

The power network can usually be divided into multiple subnetworks, with smaller time-steps applied only to those subnetworks where higher precision is needed, while larger time-steps can be used for the remaining subnetworks [2]. Time-steps for each subnetwork are selected based on their individual time response characteristics [3]. This can be done: (i) based on the time constants obtained from eigenvalue analysis for the original network [8], or (ii) by experience if the nature of the dynamics to be simulated is known [8], or (iii) by using a more thorough analysis of accuracy based on the methodology proposed in [9]. 

**Fig. 1.** General structure of multi-rate EMT simulations.

Fig. 1 depicts a dual-rate case where a large time-step $\Delta T$ is used for the slow subnetwork while a small time-step $\Delta t$ is used for the fast subnetwork. The slow subnetwork remains dormant while the fast subnetwork’s simulation proceeds. Hence, the solutions for both these subnetworks must be reconciled every time their simulation time-grids mutually coincide. While “down-sampling” (i.e., transferring the fast subnetwork’s results to the slow subnetwork), many approaches are possible. For example, one may average the values of the fast subnetwork’s interface variables [6] or simply take the last computed value of fast subnetwork’s interface variables [3]. Similarly, while “up-sampling” (i.e., transferring the slow subnetwork’s results to the fast subnetwork), many approaches are possible. For example, one may freeze the slow subnetwork’s interface variables [3] or use interpolation for assigning values to the intermediate small time-step instants [2], [6], or use extrapolation [7]. Note that up-sampling and down-sampling approaches can impact the accuracy of the simulation i.e., up-sampling may cause error accumulation in long-term simulations whereas down-sampling may fail to accurately capture the dynamics emanating from the fast subnetwork. Hence, such approaches must be selected prudently while implementing multi-rate EMT simulation programs.

Several multi-rate simulation methods have been proposed in the literature - these include iterative [4], [5] as well as non-iterative approaches [2], [6], [7]. The former type uses iterations when reconciling the solution for the entire network while the latter type uses direct methods that avoid iterations. Non-iterative methods have deterministic execution times and hence are usually the preferred choice [10].

Reference [2] presented one of the first non-iterative approaches for multi-rate EMT simulations. It uses a frequency-dependent transmission line as the interface point for partitioning a network into fast and slow subnetworks. Alternatively, in [6], an extension of the Multi Area Thevenin Equivalent (MATE) concept [11] is proposed for carrying out multi-rate EMT simulations. 

**Fig. 2.** General timeline of multi-rate EMT simulations.

Unlike [2], it does not require a transmi