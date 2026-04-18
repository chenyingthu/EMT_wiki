# Hybrid EMT-TS Simulation Strategies to Study High Bandwidth MMC-Based HVdc Systems

Yuan Liu<sup>1</sup>, Marcelo A. Elizondo<sup>1</sup>, Suman Debnath<sup>2</sup>, Jingfan Sun<sup>3</sup>, Ahmad Tbaileh<sup>1</sup>, Yuri V. Makarov<sup>1</sup>, Qiuhua Huang<sup>1</sup>, Mallikarjuna R Vallem<sup>1</sup>, Harold Kirkham<sup>1</sup>, Nader A. Samaan<sup>1</sup>

<sup>1</sup> Pacific Northwest National Laboratory, Richland, WA, USA, 99354  
<sup>2</sup> Oak Ridge National Laboratory, Oak Ridge, TN, USA, 37830  
<sup>3</sup> Georgia Institute of Technology, Atlanta, GA, USA, 30332  

{yuan.liu, marcelo.elizondo, ahmad.tbaileh, yuri.makarov, qiuhua.huang, mallikarjuna.vallem, harold.kirkham, nader.samaan}@pnnl.gov, debnaths@ornl.gov, jingfan@gatech.edu

**Abstract**—Modular multilevel converters (MMCs) are widely used in the design of modern high-voltage direct current (HVdc) transmission system. High-fidelity dynamic models of MMCs-based HVdc system require small simulation time step and can be accurately modeled in electro-magnetic transient (EMT) simulation programs. The EMT program exhibits slow simulation speed and limitation on the size of the model and brings certain challenges to test the high-fidelity HVdc model in system-level simulations. This paper presents the design and implementation of a hybrid simulation framework, which enables the co-simulation of the EMT model of Atlanta-Orlando HVdc line and the transient stability (TS) model of the entire Eastern Interconnection system. This paper also introduces the implementation of two high-fidelity HVdc line models simulated at different time steps and discusses a dedicated method for sizing the buffer areas on both sides of the HVdc line. The simulation results of the two HVdc models with different sizes of buffer areas are presented and compared.

**Index Terms**—buffer area, electro-magnetic transient, hybrid simulation, HVdc, transient stability

## I. INTRODUCTION

Modern power grid is experiencing a major evolution from ac to mixed ac-dc transmission systems with decreasing costs and noticeable economic and technical benefits of dc technologies. Some of the technical benefits of dc technologies include the abilities to interconnect several asynchronous grids, to integrate renewable energy generations, to support underground transmission, to increase the power transfer capability over long distances [1], [2], and to supply loads through variable frequency drives (VFDs) [3] – [5]. The dc technologies are also capable of providing ancillary services to enhance the economics and reliability of power systems and optimize the performance of ac grids [2].

Several national laboratories and their industry partners launched a jointly research effort to create models and methods to explore and amplify the technical and economic benefits of dc technologies in the future grid of United States [1]. This work has developed high-fidelity dynamic models of modular multilevel converters (MMCs) -based high-voltage direct current (HVdc) system [6]. The deliverables also include the development of high-fidelity models and control algorithms of multi-terminal MMC-HVdc systems connecting Eastern Interconnection (EI), Western Electricity Coordinating Council (WECC), and Electric Reliability Council of Texas (ERCOT) [2], [6]. The developed control strategy for the multi-terminal MMC-HVdc system exhibits up to 51.75% improvement in frequency response with the connection of all the three asynchronous power grids in the United States [7]. However, the test of the developed MMC-HVdc system is performed with the aggregated models for EI, ERCOT and WECC grids based on NERC data [8]. These results represent preliminary results that require confirmation tests with the full models. The evaluation on the full model requires the setup of hybrid EMT-TS simulation platform.

Previous research implemented the hybrid simulation platform to represent a significant portion of the system model in a phasor-domain transient stability (TS) simulation program and co-simulate that with a detailed electro-magnetic transient (EMT) model of a small portion containing voltage-source converter (VSC) -HVdc [9],[10]. The communication between the TS and EMT programs is built on a software called E-TRAN Plus [11] that can simultaneously simulate the detailed model using a micro-second timestep in PSCAD [12], and the rest of the system using a milli-second time-step in PSS/E [13]. The PSS/E portion of the system model in [9] utilized an 8-machine 31-bus system, which is a limited-size test system. In addition, the paper by Farsani et al. [9] adopts an empirical approach to size the buffer area, within which a number of ac buses on either side of the HVdc line are selected and modeled in PSCAD program.

This paper presents the development of a co-simulation framework to integrate the EMT model of an MMC-HVdc system and the TS model of the external EI system. The characteristics of the EI system are described in detail. Oak Ridge National Laboratory (ORNL) designed an MMC-HVdc model based on hybrid discretization and multi-rate simulation [7]. Two simulation time steps, at $4\,\mu\text{s}$ (slow) and $60\,\mu\text{s}$ (fast) separately, are implemented for the MMC-HVdc model. This paper also proposes a specific method for sizing the buffer areas on both sides of the HVdc line by selecting the ac buses to be modeled in EMT-level simulation program. In this paper, PSCAD is used as the EMT-level simulation tool and PSS/E is used as the TS-level simulation program. The software E-TRAN Plus is utilized to provide interfacing between PSCAD and PSS/E.

The following contributions of this paper are highlighted:
* This paper is the first paper that describes the c

This paper and the work described were sponsored by the U.S. Department of Energy (DOE) Office of Electricity Delivery and Energy Reliability (OE) Transformers and Advanced Components (TRAC) under the Grid Modernization Laboratory Consortium. The authors would like to thank Dr. Kerry Cheung who leads the DOE TRAC program for providing continued guidance. The authors would also like to thank the contributions of Madhu Chinthavali and Phani Marthi from Oak Ridge National Laboratory. The Pacific Northwest National Laboratory is operated by Battelle for the U.S. Department of Energy under contract DE-AC05-76RL01830.

**TABLE I. SUMMARY OF POWER FLOW NETWORK MODEL PARAMETERS**

| Model Characteristics | Quantity |
|---|---|
| Total Generation (GW) | 728 |
| Total Load (GW) | 693 |
| Total Reactive Support (GVAr) | 177 |
| Number of Buses | 78,682 |