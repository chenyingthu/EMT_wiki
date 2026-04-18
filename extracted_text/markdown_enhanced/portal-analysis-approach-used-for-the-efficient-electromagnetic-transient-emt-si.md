## Portal Analysis Approach Used for the Efficient Electromagnetic Transient (EMT) Simulation of Power Electronic Systems

**Authors:** Chenxiang Gao, Jin Xu, Keyou Wang, Member, IEEE, Pan Wu, Zirun Li, Jianqi Zhou, and Ryuichi Yokoyama, Life Fellow, IEEE

**Abstract**—Efficient electromagnetic transient (EMT) simulation is crucial for addressing the challenges associated with the modularity, cascading, and complex topologies of power electronics (PE) systems. This article introduces a novel portal analysis (PA) approach that adopts a unique “port-component” view, leveraging the characteristics of “ports”. Different from the classic nodal analysis (NA) method, the networks and the components are described based on the portal voltage equations with lower orders. Furthermore, a port tearing method is introduced to partition the circuit, resulting in a block-bordered-diagonal (BBD) matrix and a small number of boundary variables in the extended port equation. The parallel processing of the network solution is implemented by utilizing the BBD forms and the band features. To validate the effectiveness of the proposed PA approach in capturing dynamics, a down-scale dual active bridge (DAB) prototype is constructed. Additionally, a simulated microgrid comprising cascaded H-bridge-type-DAB (CHB-DAB), solar photovoltaic (PV), and energy storage system (ESS) is used to furtherly verify the accuracy and efficiency. The results demonstrate that compared with the NA-based methods, the proposed models exhibit high precision under various transient conditions, with maximum relative errors of less than 2%. Moreover, they achieve a remarkable acceleration of one to two orders of magnitude.

**Index Terms**—Power electronic system, electromagnetic transient (EMT) simulation, portal analysis, port tearing approach, parallel processing.

*Manuscript received 24 February 2023; revised 2 July 2023; accepted 11 August 2023. Date of publication 15 August 2023; date of current version 22 November 2023. This work was supported in part by the National Key R&D Program of China under Grant 2022YFE0105200 and in part by State Grid Zhejiang Electric Power Company Science and Technology Program under Grant 5211JX230004. Paper no. TPWRD-00228-2023. (Corresponding authors: Keyou Wang.)*

Chenxiang Gao, Jin Xu, Keyou Wang, Pan Wu, and Zirun Li are with the Key Laboratory of Control of Power Transmission and Conversion, Ministry of Education, Shanghai Jiao Tong University, Shanghai 200240, China (e-mail: gaocx_22@sjtu.edu.cn; xujin20506@sjtu.edu.cn; wangkeyou@sjtu.edu.cn; panghuwu@sjtu.edu.cn; lzr9602@sjtu.edu.cn).

Jianqi Zhou is with the State Grid Jiaxing Power Supply Company, Jiaxing 314000, China (e-mail: zhoucity@vip.sina.com).

Ryuichi Yokoyama is with the Waseda University, Tokyo 169-8555, Japan (e-mail: yokoyama-ryuichi@waseda.jp).

Color versions of one or more figures in this article are available at https://doi.org/10.1109/TPWRD.2023.3305035.

Digital Object Identifier 10.1109/TPWRD.2023.3305035

0885-8977 © 2023 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://w

## I. INTRODUCTION

With the remarkable increase of the renewable energy integration, the proportion and scales of the power electronic (PE) equipment are experiencing an upward trend [1], [2], [3]. The utilization of high-frequency switching techniques and fast control strategies in PE devices has led to transient processes with time scales ranging from microseconds to seconds. Consequently, accurately capturing the dynamic phenomena necessitates detailed electromagnetic transient (EMT) simulation [4], [5], [6]. However, in high voltage and large capacity scenarios, various power converters with modular, cascading, and complex topologies come into play. Examples of such converters include widely used modular multilevel converters (MMCs) [7] and power electronic transformers (PETs) [8], [9]. Performing EMT simulations of these networks using commercial software like PSCAD/EMTDC often requires a simulation time step at the microsecond level and the inversion of a high-order time-varying node admittance matrix [10], [11]. Unfortunately, this combination results in unacceptably long computing times.

Efficient EMT simulation technologies and algorithms for the PE systems attract widespread attention in recent years. These developments can be categorized as follows:

1) **Circuit equivalent algorithms:** These algorithms draw inspiration from generalized Thevenin equivalent methods. By eliminating internal nodes, such as those in MMCs and PETs [12], [13], [14], accelerated models are obtained. While these models exhibit high efficiency, they require complicated manual programming efforts and lack applicability to changing topologies.
2) **Partitioning technologies:** Circuit partitioning methods divide the large-scale network into smaller subsystems based on the natural or artificial latencies. Examples include the Transmission-line model (TLM) [15], the latency insertion method (LIM) [16], [17], and the controlled-source decoupling models [18], [19]. However, these methods may introduce numerical instability and compromise accuracy. Numerical partitioning methods, such as multi-area Thevenin equivalent (MATE) [20] and nodal-splitting approach [21], [22], directly transform the admittance matrices into block-bordered-diagonal (BBD) forms through branch tearing or zero-admittance tearing. These methods are generally more flexible and accurate than the circuit partitioning methods, but their efficiency is influenced by the number of boundary variables.
3) **Sparsity technologies:** The node admittance matrices are highly sparse and diagonally dominant. Thus, sparse LU factorization algorithms, such as the Minimum Degree