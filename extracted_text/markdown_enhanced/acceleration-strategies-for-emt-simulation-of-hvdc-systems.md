# Acceleration strategies for EMT Simulation of HVDC systems

**A. Allabadi**<sup>a,*</sup>, **J. Mahseredjian**<sup>a</sup>, **S. Dennetière**<sup>b</sup>, **A. Abusalah**<sup>a</sup>, **I. Kocar**<sup>a</sup>, **T. Ould-Bachir**<sup>a</sup>

<sup>a</sup> Polytechnique Montréal, Montreal, QC H3T 1J4, Canada  
<sup>b</sup> Réseau de Transport d’Electricité, Paris 92932, France

**Keywords:** EMT, HVDC, MTDC, Offline simulation, Parallel computing

**Abstract:** This paper investigates electromagnetic transient (EMT) simulation of large-scale multiterminal HVDC (MTDC) networks, focusing on methods for significant computational acceleration. Three key techniques are evaluated for their applicability: network parallelization, which exploits the natural decoupling properties of transmission lines; control system parallelization, which leverages modularity in converter and inverter-based resource controls; and optimized sequential solvers for control systems. Additionally, two hybrid approaches that integrate these strategies are proposed, achieving substantial speedups in simulation performance. Using the InterOPERA benchmark system modelled in EMTP®, the proposed approaches achieve up to 23x acceleration without compromising accuracy.

## 1. Introduction

With the growing integration of renewable energy sources and the need for flexible, long-distance power transmission, high-voltage direct current (HVDC) technology has become a vital component of modern power grids [1]. HVDC systems are particularly well-suited for transmitting large amounts of power over long distances with minimal losses, making them essential for interconnecting remote renewable energy sources, stabilizing grid operations, and supporting cross-regional power transfer. Traditional point-to-point HVDC systems are widely implemented; however, as renewable energy adoption increases, there is a shift towards multi-terminal HVDC (MTDC) systems to facilitate greater network flexibility and interconnectivity [2].

EMT simulations of large-scale MTDC systems can be computationally expensive due to the intense computational loads of solving control and power system equations at each time-point.

Several strategies have been proposed to accelerate EMT simulations, specifically targeting computationally intensive components in HVDC systems, such as the Modular Multilevel Converter (MMC). For example, optimized models for MMCs have been introduced in [3,4]. Parallel processing strategies enable efficient computations with MMC equivalent models [5]. Initialization techniques further expedite simulations by minimizing simulation time to reach steady-state, with schemes developed specifically for the MMC model [6] and for generic MTDC systems [7].

Other acceleration techniques are more generic, addressing EMT simulations broadly rather than focusing exclusively on HVDC or MTDC systems. One example is transmission line-based parallelization (TLP), which exploits transmission line propagation delays to decouple and parallelize segments of the power network [8].

Given the complexity of control systems in EMT simulations, where control system computations can represent a substantial part of the load, control system parallelization (CtrlP) methods have been proven effective. For instance, a functional mock-up interface (FMI) was used to distribute control system tasks across processors in [9].

In addition to CtrlP, altering the control system solution method offers further potential for improvement. Traditionally, control system solvers introduce an artificial delay of one time-step to break feedback loops. While this sequential solution approach provides acceptable results in several cases, especially with small numerical integration time-steps, it can become problematic in large-scale systems dominated by IBRs and power electronic devices. In such systems, particularly in sensitive control subsystems, artificial delays can lead to numerical instabilities, as demonstrated in [10]. Simultaneous control solvers avoid the introduction of artificial delays by using Jacobian matrix-based iterations [10]. However, in large-scale MTDC systems, such methods may limit computational performance. Alternatively, a non-iterative Jacobian-based approach (NIJ) is proposed in [10]. It is based on successive (at each time-point) linearizations. This NIJ appr

---
<sup>☆</sup> This work was supported by the Natural Sciences and Engineering Research Council (NSERC) of Canada as part of the industrial chair “Multi time-frame simulation of transients for large scale power systems.”  
<sup>☆☆</sup> A. Allabadi, J. Mahseredjian, A. Abusalah, Ilhan Kocar, and T. Ould-Bachir are with Polytechnique Montréal, Montreal, QC H3T 1J4, Canada.  
<sup>★</sup> S. Dennetière is with the Réseau de Transport d’Electricité, Paris 92932, France.  
<sup>★★</sup> Paper submitted to the International Conference on Power Systems Transients (IPST2025) in Guadalajara, Mexico, June 8–12, 2025.  
<sup>*</sup> Corresponding author. E-mail addresses: ahmad.allabadi@polymtl.ca (A. Allabadi), jean.mahseredjian@polymtl.ca (J. Mahseredjian), sebastien.dennetiere@rte-france.com (S. Dennetière), anas.abusalah@polymtl.ca (A. Abusalah), ilhan.kocar@polymtl.ca (I. Kocar), tarek.ould-bachir@polymtl.ca (T. Ould-Bachir).