## Accelerated Electromagnetic Transient (EMT) Equivalent Model of Solid-State Transformer
Chenxiang Gao, Student Member, IEEE, Moke Feng, Graduate Student Member, IEEE, Jiangping Ding, Hang Zhang, Jianzhong Xu, Senior Member, IEEE, Chengyong Zhao, Senior Member, IEEE, Zixin Li, Senior Member, IEEE, and Gen Li, Member, IEEE

Manuscript received 19 March 2021; revised 27 May 2021; accepted 27 June 2021. Date of publication 2 July 2021; date of current version 2 August 2022. This article was presented at the 4th International Conference on HVDC, Xi’an, China, 2020. Recommended for publication by Associate Editor Levy F. Costa. (Corresponding authors: Jianzhong Xu; Zixin Li.)
Chenxiang Gao, Moke Feng, Jianzhong Xu, and Chengyong Zhao are with the State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University (NCEPU), Beijing 102206, China (e-mail: xujianzhong@ncepu.edu.cn).
Jiangping Ding is with Guangzhou Power Supply Bureau Company Ltd., Guangzhou, Guangdong 510620, China.
Hang Zhang and Zixin Li are with the Key Laboratory of Power Electronics and Electric Drive, Institute of Electrical Engineering, Chinese Academy of Sciences, Beijing 100190, China, and also with the University of Chinese Academy of Sciences, Beijing 10049, China (e-mail: lzx@mail.iee.ac.cn).
Gen Li is with the School of Engineering, Cardiff University, Cardiff CF24 3AA, U.K.

**Abstract—** Accurate and efficient electromagnetic transient (EMT) simulation of various types of solid-state transformers (SSTs) is extremely time-consuming due to the complex module structure, flexible topology connections, large number of electrical nodes, and simulation time steps limited in the range of microseconds. Therefore, it is urgent to develop the EMT equivalent modeling and fast simulation of SSTs for system-level studies. Taking the modular multilevel converter (MMC)-based SST as an example, this article proposes an accelerated EMT model, which focuses on the equivalence of the dual-active-bridge (DAB)-based high-frequency link (HFL) in the SST. Compared with the existing algorithms, two critical factors of the proposed method that contribute the most to the efficiency improvement are the preprocessing of the nodal admittance equation and the conversion of the short-circuit admittance parameters. The proposed model is verified in PSCAD/EMTDC by comparing it with the detailed EMT model. The results show that the accelerated model is one-to-two orders of magnitude faster than the detailed model without sacrificing accuracy. The experiment validation also confirms the validity of the proposed model.

**Index Terms—** Accelerated equivalent model (EM), electromagnetic transient (EMT) simulation, parameter conversion, preprocessing, solid-state transformer (SST).

## I. INTRODUCTION
SOLID-STATE transformer (SST), which is able to realize the transformation of multiple voltage levels and integration of various energy sources, can play an important role in achieving a low-carbon smart grid [1]–[5]. To meet the needs of different application scenarios, there are various power module (PM) structures of SSTs. Specifically, cascaded H-bridge (CHB) and modular multilevel converter (MMC) can be deployed in the medium-voltage (MV) side as ac/dc converters, while dual active bridge (DAB), multiple active bridge (MAB), and single active bridge (SAB) can be used in the low-voltage (LV) side as dc/dc converters [6]–[11]. Moreover, multiple connection configurations of the PMs have been proposed to address the dilemma of increasing the converter capacity and reducing the device rating [12], [13], such as the input-series-output-parallel (ISOP), input-series-output-series (ISOS), input-parallel-output-parallel (IPOP), and input-parallel-output-series (IPOS).

Combining the advantages of MMCs and the ISOP configuration, a typical MMC-based SST is presented in [14], as shown in Fig. 1(a). Its high-frequency link (HFL) is based on the DAB PM shown in Fig. 1(b). The large number of submodules (SMs) leads to a high order of admittance matrix in the electromagnetic transient (EMT) simulation using fully detailed models (DMs), which requires the simulation time steps to be in the range of microseconds due to the power electronic switches and high-frequency isolation transformers [15], [16]. Hence, both MMC and HFL face very urgent needs for EMT equivalent modeling and fast simulation.

**Fig. 1.** MMC-based SST. (a) Converter structure. (b) DAB PM structure.

Recently, the research on the accelerated equivalent models (EMs) of MMCs has been relatively mature [17]–[20]. Specifically, the EMs in [19] and [20] create a single-port or multiport Norton equivalent circuit by recursively eliminating internal nodes. Their modeling methods show good acceleration and accuracy without losing the information of internal nodes. However, these methods are designed for MMCs and, therefore, cannot be directly applied to the HFL because the topologies and connection configurations of PMs are more complicated in HFLs.

**TABLE I**  
TYPE OF PARAMETERS FOR DIFFERENT CONNECTION CONFIGURATIONS
| Parameter Type | Connection Configuration |
|---|---|
| *(Table data truncated in source text)* | |

as listed in the first column of Table I. Among them, the short-circuit admittance parameters are closely related to the node admittance matrix of the system and can be converted to the other three types.

Taking the hybrid parameters as an example, the PM port equation can be written as follows:
$$
\begin{bmatrix} v_{\text{IN}} \\ i_{\text{OUT}} \end{bmatrix} = \begin{bmatrix} h_{11} & h_{12} \\ h_{21} & h_{22} \end{bmatrix} \begin{bmatrix} i_{\text{IN}} \\ v_{\text{OUT}} \end{bmatrix}
$$