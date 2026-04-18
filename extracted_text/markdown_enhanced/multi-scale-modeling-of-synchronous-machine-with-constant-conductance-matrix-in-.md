# Multi-scale Modeling of Synchronous Machine With Constant Conductance Matrix in Phase Domain

**Peng Zhao, Yue Xia, Juan Su**  
CIEE, China Agricultural University, Beijing, China  
zpengxm@163.com, yue.xia@cau.edu.cn, sujuan@cau.edu.cn  

**Zhikai You**  
Jiaxing Electric Power Supply Company, Jiaxing, China  
youzkzk@163.com  

**Abstract**—In this paper, a novel synchronous machine model is developed for the accurate and efficient simulation of multi-scale transients. The machine stator equations are expressed with analytic signals in the phase domain, thus providing direct interface between machine model and external network model. Frequency shifting is applied to stator quantities to eliminate the ac carrier in the stator windings which enables the use of large time-step size. An artificial damper winding is introduced to eliminate the numerical saliency based on a pioneering technique. The proposed machine model is represented as a Norton equivalent with constant conductance matrix. The analysis of test cases demonstrates the effectiveness of the proposed synchronous machine model in terms of accuracy and efficiency. model of the synchronous machine with a constant admittance matrix based on the frequency shifting concept is proposed in phase domain. Employing shift frequency as a new parameter, the multi-scale functionality supports the simulation of high-frequency and low-frequency transients in a range of time scales. Secondly, a constant conductance matrix is formulated by adding an artificial winding in the machine model. Avoiding the update of the conductance matrix for the network is maintained at every time-step. The novel rules for setting artificial winding parameters are proposed considering both accuracy and stability. Thirdly, the machine equations are reformulated and it results in a significant simplification of the expression for the machine model. This simplification reduces the required mathematical operations for modeling the synchronous machine, thereby decreasing computation time. Furthermore, the accuracy and efficiency of the proposed model are examined by test case.

**Index Terms**—synchronous machine, constant conductance matrix, multi-scale transients, frequency shifting

## I. INTRODUCTION
In recent years, modeling of synchronous machines has become a popular research topic. Numerous synchronous machine models have been proposed in the transient analysis of power systems.

The dq0 transformation finds extensive application in the modeling of synchronous machines [1]. The major advantage of the reference frame of dq0 component is that it yields constant inductances. However, the dq0 model requires an

## II. MULTI-SCALE SYNCHRONOUS MACHINE MODELING
### A. Discretized Multi-scale Synchronous Machine Model
The synchronous machine stator is connected to the grid.