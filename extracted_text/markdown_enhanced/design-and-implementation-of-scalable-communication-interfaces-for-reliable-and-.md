## Design and Implementation of Scalable Communication Interfaces for Reliable and Stable Real-time Co-Simulation of Power Systems

Qi Xiao, Jongha Woo, Lidong Song, Ning Lu  
*NC State University, Raleigh, NC, USA*  
Victor Paduani  
*New York Power Authority, Albany, NY, USA*  
{qxiao3, nlu2}@ncsu.edu

## Abstract
Co-simulation offers an integrated approach for modeling the large-scale integration of inverter-based resources (IBRs) into transmission and distribution grids. This paper presents a scalable communication interface design and implementation to enable reliable and stable real-time co-simulation of power systems with high IBR penetration. The communication interface is categorized into two types: local and remote. In local scenarios, where subsystems are connected within a single local area network (LAN), low-latency communication facilitates the seamless integration of electromagnetic transient (EMT) and phasor-domain models, enabling efficient interactions with power and energy management algorithms. For remote scenarios, data exchange is achieved via internet-based file sharing or VPN-enabled communication. The performance of both methods is evaluated using OPAL-RT as a real-time simulator, demonstrating scalability, effectiveness, and challenges specific to real-time co-simulation applications. To mitigate instability arising from data resolution mismatches in time-sensitive co-simulations, a real-time data extrapolation method is proposed. This approach significantly enhances stability and reliability, ensuring more accurate simulation outcomes. The implementation code is available on GitHub, providing researchers the tools to replicate and expand upon this work.

co-simulation offers advantages such as flexibility and scalability, it also presents challenges, particularly in managing latency and synchronization when coordinating subsystems with varying time steps, sampling rates, and control intervals. Overcoming these challenges is crucial for ensuring simulation accuracy and maintaining system stability.

In our previous studies, we observed that the choice of co-simulation communication interface is highly dependent on the application. For instance, in [3], we investigated device-level co-simulation to integrate models like EMT and phasor models. Meanwhile, in [4]-[6], we focused on network-level co-simulation frameworks to analyze interactions resulting from DER integration. Co-simulation with energy management systems is also crucial for replicating real-world conditions [7], [8], though it inherently involves communication latencies. Effectively addressing latencies with tailored data exchange methods is crucial, especially for applications like cybersecurity analysis.

To address these challenges, this paper presents solutions developed for various co-simulation scenarios and introduces a suite of communication interfaces that enable