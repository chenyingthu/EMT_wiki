# An enhanced K-means two-step clustering method for dynamic equivalent modeling of DFIG wind farms based on LVRT characteristics

Junhua Xu *, Jiyuan Shen, Xinyu You, Chunwei Wang, Bin Liu  
School of Electrical Engineering, Guangxi University, located in Nanning, China

* Corresponding author.  
E-mail address: minghuxjh@126.com (J. Xu).

**Keywords:**  
DFIG wind farms  
Dynamic equivalent modeling  
LVRT characteristics  
Two-step clustering  
Enhanced k-means clustering

**Abstract**  
To enhance the accuracy of dynamic equivalent models for wind farms utilizing doubly-fed induction generators (DFIGs), an enhanced k-means two-step clustering method for dynamic equivalent modeling of DFIG wind farms based on low-voltage ride-through (LVRT) characteristics is proposed in this study. First, the entire turbine fleet is divided into two categories based on their active power output and LVRT response: those exhibiting clustering characteristics and those that do not. For the latter, an enhanced k-means algorithm is applied. This approach optimizes initial center selection through probabilistic selection, improves search efficiency by utilizing a (K-Dimensional Tree) KD tree (reducing data search time by approximately 75% compared to traditional k-means), and determines the ideal cluster count using the Davies-Bouldin Index (DBI). The method overcomes the limitations of existing algorithms that require manual specification of initial centers and cluster numbers. Simulation results demonstrate that the equivalent model accurately corresponds to the detailed model during faults. Notably, the simulation time is reduced by about 90% while maintaining high precision, providing an efficient and accurate modeling approach for power system stability analysis with high wind power penetration.

## 1. Introduction

The large-scale integration of renewable energy into the power grid poses severe challenges to system stability and reliability [1]. The intermittency and volatility of wind power further complicate the analysis of system dynamic behavior [2]. Against this backdrop, the DFIG has been widely adopted due to its excellent performance [3], and its dynamic response during LVRT is critical for system stability analysis.

Dynamic simulation of large wind farms is computationally intensive [4], necessitating dynamic equivalent modeling to balance accuracy and efficiency [5]. Equivalent modeling methods include single-machine and multi-machine approaches [6,7]. The former cannot reflect turbine-specific dynamics arising from geographical and equipment variations [8–10], making the latter the main research focus.

While energy system optimization has advanced in areas like distributed coordination [11], multi-stage techno-economic modeling [12], demand response privacy [13], bidding systems [14], robust optimization [15], risk management [16], stochastic frameworks [17], decentralized self-healing [18], and storage-response synergy [19,20], these efforts focus on system-level and market challenges, whereas the core task of accurately aggregating unit-level dynamic responses–essential for wind farm equivalent modeling–remains a distinct, unresolved technical problem. Thus, while adjacent fields provide valuable context, they emphasize the need for domain-specific innovations.

As a mainstream equivalent modeling approach, clustering still faces challenges. Early methods reduced computational load [21], quantified turbine contributions [22], incorporated kinetic energy [23], or used fuzzy C-means for output characteristics [24]. Despite these advances, two key limitations remain: dependence on subjective parameters and neglect of LVRT analysis, reducing model reliability during faults.

To integrate LVRT characteristics, Crowbar-based binary models were developed [25,26], yet their oversimplified "switch" behavior reduced accuracy. Later three-step methods [27,28] offered improvements but still assumed uniform LVRT responses across turbines, overlooking output-dependent variations. Although [29] analyzed LVRT control strategies’ impact on output and compared results with extensive field data, the absence of quantitative clustering indices hindered effective clustering.

Thus, a clear gap remains for a clustering method that incorporates LVRT characteristics for equivalent modeling during faults. To address this gap, this paper proposes an improved LVRT-based k-means two-step clustering method, with these key contributions: (1) a novel two-step framework pre-classifying units by active power and LVRT response; (2) an automated algorithm integrating K-Means++ initialization, KD-trees (75% faster search), and DBI for optimal cluster count; and (3) a high-fidelity model replicating detailed dynamics (>98% accuracy), reducing simulation time by 90%, and outperforming existing methods.

The paper is structured as follows: Section 2 analyzes DFIG LVRT response; Section 3 details clustering method; Section 4 presents case tests; Section 5 concludes and outlines future work.

## 2. LVRT response characteristics of DFIGs

### 2.1. DFIG topology and response characteristics

The typical topology of a DFIG is depicted in Fig. 1 [30]. The stator windings are directly connected to the electrical grid, while the rotor windings are linked via a back-to-back converter. The rotor-side con-

*Fig. 2. Control diagram of RSC.*

By aligning the $d$-axis with the stator flux linkage direction, the expressions for stator active and reactive power can be derived:
$$\begin{cases}$$