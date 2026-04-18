## FPGA-based simulation of grid-tied converters using frequency-dependent network equivalent ⋆

**Authors:** Fahimeh Hajizadeh<sup>a,∗</sup>, Alireza Masoom<sup>b</sup>, Tarek Ould-Bachir<sup>c</sup>, Jean-Pierre David<sup>a</sup>

**Affiliations:**
- <sup>a</sup> Dept. electrical engineering, Polytechnique Montréal, Montreal, Canada
- <sup>b</sup> Hydro-Québec Research Institute (IREQ), Varennes, Canada
- <sup>c</sup> MOTCE Laboratory, DGIGL, Polytechnique Montréal, Canada

**Keywords:** FPGA, FDNE, Real-time simulation, Electromagnetic simulation, STATCOM

**Abstract:** 
This paper introduces a real-time simulation framework for grid-tied converters, implemented on field-programmable gate arrays (FPGAs). The framework incorporates a Frequency-Dependent Network Equivalent (FDNE) to reduce the original part of the circuit that is not directly under study into a frequency-dependent admittance model, enabling precise modeling of the power network’s frequency-dependent dynamics while streamlining the onboard simulation and modeling process. The proposed framework is implemented on the Alveo U280 FPGA, achieving sub-microsecond latencies, low resource utilization, and high computational fidelity across various data types, including single-, double-precision, and customized floating-point formats. The numerical test and validation were conducted using a high-voltage power network that includes detailed models of transmission lines, loads, and a Static Synchronous Compensator (STATCOM), etc. Simulation results show strong alignment with reference models developed in the EMTP, achieving faster-than-real-time performance. These findings demonstrate the effectiveness of the proposed solution in delivering high-speed, resource-efficient, and scalable real-time simulations, providing a promising approach for testing and validating advanced control strategies in modern power systems.

**Metadata & Footnotes:**
- ⋆ Paper submitted to the International Conference on Power Systems Transients (IPST2025) in Guadalajara, Mexico, June 8–12, 2025.
- ∗ Corresponding author.
- **E-mail addresses:** fahimeh.hajizadeh@polymtl.ca (F. Hajizadeh), alireza@hydroquebec.com (A. Masoom), tarek.ould-bachir@polymtl.ca (T. Ould-Bachir), jean-pierre.david@polymtl.ca (J.-P. David).
- https://doi.org/10.1016/j.epsr.2025.112400
- Received 6 January 2025; Received in revised form 25 February 2025; Accepted 17 October 2025
- Available online 26 October 2025

## 1. Introduction

The integration of power converters in modern power systems has become essential to accommodate the growing adoption of distributed energy resources (DER) such as wind turbines, solar photovoltaics and charging stations for electric vehicles [1]. Power converters are essential for connecting renewable energy sources to the grid, facilitating efficient energy transfer, and improving grid stability through active and reactive power management [2,3]. These converters connect various renewable energy sources to the power grid, facilitating cleaner energy consumption and addressing intermittency and fluctuating load demands [4–6]. However, the extensive use of power electronic devices, especially in grids with many DERs, poses distinct challenges to grid stability. This situation requires advanced control solutions to address potential power quality issues.

However, using power converters, such as voltage source converters (VSCs) and other inverter-based resources, presents challenges for grid stability. These devices can interact with conventional synchronous machines and other grid elements, causing oscillations, higher frequency change rates, and frequency overshoots [7,8]. Moreover, control strategies to manage the dynamic performance of these converters must be meticulously designed to minimize harmonic distortion and maintain unity power factor for improved grid resilience [9]. As the use of such devices grows, it is essential to establish effective control methodologies to manage interactions with traditional grid infrastructure.

This paper presents a simulation framework for grid-connected converters to address these challenges, designed using field-programmable gate arrays (FPGAs). The framework integrates a Frequency-Dependent Network Equivalent (FDNE) model to accurately represent the frequency-dependent behavior of the grid. The framework achieves sub-microsecond latencies while preserving computational accuracy. A Static Synchronous Compensator (STATCOM) is employed as a test case to validate the effectiveness of the proposed approach.

The primary contributions of this work include: 1) The development of two novel FDNE integration approaches based on state-space equations, enabling efficient real-time simulation of an FDNE-integrated STATCOM model on FPGA. These formulations leverage matrix-based computations, optimizing execution speed and numerical stability. 2) The implementation of a resource-efficient FPGA framework, utilizing high-level synthesis (HLS) for FPGA programming and integrating Customized Floating-Point based (CuFP-based) arithmetic. CuFP allows customizable precision, balancing accuracy, and hardware efficiency to achieve optimal FPGA utilization. 3) A demonstration that the proposed m

**Fig. 1.** A +100 Mvar/-100 Mvar STATCOM implemented by two-level VSC.