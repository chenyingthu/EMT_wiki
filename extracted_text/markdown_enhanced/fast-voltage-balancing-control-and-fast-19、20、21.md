# Fast Voltage-Balancing Control and Fast Numerical Simulation Model for the Modular Multilevel Converter
Feng Yu, Weixing Lin, Member, IEEE, Xitian Wang, Member, IEEE, and Da Xie, Member, IEEE

**Abstract**—A methodology of fast voltage-balancing control based on average comparison and a fast numerical simulation model for the modular multilevel converter are proposed. In each control cycle, the average voltage of all the submodules (SMs) in an arm is calculated. The switching state of each SM will be determined by comparing the capacitor voltage of each SM with this average value. Little sorting of the capacitor voltages is required; therefore, the calculation burden on the controller is significantly reduced. The previous switching state of each SM will be mostly retained. Two variables               and             are introduced to adjust the equivalent switching frequency of each SM. Simulation results verified the effectiveness of the proposed voltage-balancing control in normal and fault conditions. A fast numerical simulation model for MMC on PSCAD/EMTDC is also proposed. The dynamics of each SM are sufficiently represented in the proposed model. A hybrid simulation model is further developed to incorporate the detailed switching dynamics of specific interested SMs. The simulation results show that the proposed models give almost identical results as the detailed switching models while the simulation speed of the proposed model is approximately 5000 times faster than the detailed switching model.

**Index Terms**—Electromagnetic transients (EMT) simulation, HVDC transmission, modular multilevel converter (MMC), nearest level control, voltage-balancing control.

Manuscript received December 26, 2013; revised July 10, 2014; accepted August 15, 2014. This paper was supported by the National Natural Science Foundation of China (51277119). Paper no. TPWRD-01456-2013.
F. Yu, X. Wang, and D. Xie are with the School of Electronic and Electrical Engineering, Shanghai Jiaotong University, Shanghai 200240, China (e-mail: darall@sjtu.edu.cn; x.t.wang@sjtu.edu.cn; xieda@sjtu.edu.cn).
W. Lin is with the School of Electrical and Electronic Engineering, Huazhong University of Science and Technology, Wuhan 430074, China, and also with the School of Engineering, University of Aberdeen, Aberdeen AB24 3UE, U.K. (e-mail: weixinglin@foxmail.com; weixinglin@abdn.ac.uk).

## I. INTRODUCTION
THE MODULAR multilevel converter (MMC) has been making its way toward wide applications in medium- and high-voltage fields [1]–[6]. The converter arm of an MMC is constructed by series connection of a number of submodules (SMs). The typical dc voltage rating for a half-bridge SM (HBSM) is 2 kV. To make the dc voltage level of MMC suitable for HVDC transmission, hundreds of SMs are required to be connected in series [1]–[6]. The Trans Bay Cable Project, as an example, employs 216 SMs per arm for 200-kV dc voltage.

The large number of SMs (therefore power-electronic devices) in an MMC brings challenges to the simulation and control of MMC as follows.
1) Electromagnetic transient simulation are usually adopted to study the dynamic of MMCs. As the number of power-electronic switches increases, the simulation speed of the MMC becomes extremely low, typically one week for 5-s dynamics for a 201-level MMC.
2) Excessive computation is required in the controller of the MMC if typical voltage-balancing control based on voltage sorting is adopted.

A number of simplified/equivalent model of MMC have been proposed in the literature [3]–[8] that could significantly increase the simulation speed of MMC.

A continuous model was proposed in [3] where the total output voltage of the SMs in each arm is represented by a controlled voltage source. The output characteristics and the circulating current could be well represented by the model of [3]. However, the dynamics of each SM are not represented.

Reference [4] presented a modeling method of MMC that is mathematically identical to the detailed switching models in PSCAD/EMTDC. Each arm of the MMC is modelled as a single 2-node element and interfaced with the electromagnetic transient (EMT) solver in order to solve the MMC and external networks simultaneously. The drawback of this method in [4] is that the method needs to change the source code of PSCAD/EMTDC to interface with the EMT solver, which is inaccessible to the public. Therefore, the method of [4] is not user friendly. Users can only use the few preset functions of the modeling component set by the developers.

Reference [5] proposed an average value model of the MMC that simplified each arm to a controlled voltage source. Similar to the method of [3], the dynamics of each SM are also not represented.

Reference [6] proposed an accelerated model of MMC based on the idea that inverting several small matrices is much faster than inverting one big matrix of the same dimension due to the total dimension of all small matrices [7]. In [6], each SM is modelled by an independent circuit supplied with the same current source with the current magnitude equal to arm current. Since each SM is still represented by a detailed switching model, simulation speed is slower than the model of [4].

Reference [8] gave a summary and comparison of the available simplified/equivalent model for MMC.