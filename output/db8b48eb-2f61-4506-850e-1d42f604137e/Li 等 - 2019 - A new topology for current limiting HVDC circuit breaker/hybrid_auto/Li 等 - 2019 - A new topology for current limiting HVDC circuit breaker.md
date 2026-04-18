# A new topology for current limiting HVDC circuit breaker☆

Shuai Li⁎ , Jiyuan Zhang, Jianzhong Xu, Chengyong Zhao

The State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University, Beijing, China

![](images/709c4fb4335e43681824503552a1fbe70ec90f959abeca4b609ada1ba59bc7db.jpg)

# A R T I C L E I N F O

Keywords:

HVDC circuit breakers

Current limiters

Over-voltage protection

Stability

# A B S T R A C T

With the high voltage direct current Transmission (HVDC) booming, HVDC grid has received wide attention. As an essential component in HVDC grid, high voltage direct current circuit breakers (DCCB) requires urgent and intensive study. A novel topology for current limiting DCCB (CL-DCCB) is proposed in this paper. The topology consists of several units which are divided into two classes: main circuit breaker (MCB) and branch circuit breakers (BCBs). The number of inductor branches can be flexibly selected to enhance the current limiting effect. The CL-DCCB can start current limiting operation when a suspected fault occurs. When the detection circuit reveals what has happened, it can be determined whether to implement breaking operation or recover to normal state. This mode allows longer fault detection time and circuit breaker operation delay while guaranteeing the fault current within the maximum limit of the system. Finally, Simulation model and experiment prototype are built to study the design criteria for CL-DCCB. It is observed that the maximum detection delay can be extended to 12 ms. Moreover, the current limiting effect can be enhanced when the number of inductor branches or the inductance of each branch is increased.

# 1. Introduction

DC grid is a new type of power transmission system, which is obtained from voltage-source converter (VSC) type HVDC [1,2]. It interconnects multiple AC and DC systems with higher reliability due to its redundant DC lines. DC grid technology is especially suitable for largescale wind power or photovoltaic and other new energy integration, which is the future direction of DC transmission technology [3,4]. China is building a demonstration project named as Zhangbei DC grid. The project is designed for the collection and transportation of largescale wind power, photovoltaic, energy storage, and other energy forms. The rated voltage of this DC grid is ± 500 kV, with approximately 648 km overhead transmission lines [5].

Due to the low damping of DC system and no zero crossing point of the DC current, it is difficult to isolate the DC fault. Especially in largescale power grid. Take a scenario of DC grid shown in Fig. 1 as an example, the DC grid is divided into two parts by a DC-DC converter. The upper part $\mathrm { C _ { 1 } \mathrm { - } C _ { 4 } }$ is a cyclic and radiation mixed connection structure. The lower part is a point-to-point DC system. Obviously, the normal operation of the whole network will be hardest hit if the fault cannot be cleared in time.

One way to solve this problem is to use novel MMC sub-modules

(SMs) with DC fault clearance capability [6,7]. Once short circuit fault occurs, the fault current discharge path can be blocked by blocking MMC SMs. Finally, the mechanical switch can be used to interrupt the fault line, thus, the system fault characteristics can be greatly improved. However, the novel SMs will inevitably increase the cost and power loss of MMC. More importantly, all the converter station must be blocked under fault condition. Thus, the loss of power transmission capacity will affect the normal and stable operation of the whole grid. Taking Fig. 1 as an example, if a short-circuit fault occurs in the transmission line among converter station $\mathrm { C _ { 1 } \mathrm { - C _ { 4 } , } }$ all these converter station should be blocked, then mechanical switch can be used to isolate faulty lines when the fault current drops to zero. The outage of those converter stations means a quick stop of electricity transmission in the whole grid, which is unacceptable.

The DC-DC converter can also be configured in the grid to isolate the DC fault, and the high frequency transformer of the DC-DC converter is undoubtedly a good isolating device. Through the control of the DC-DC, the fault can be isolated quickly. However, the configuration of DC-DC in the grid is limited with the issue of cost and power loss, thus the protection area of the grid is limited [8,9].

SCFCL is featured with good current limiting effects and fast response, but the technology is not yet mature, and expensive [10,11].

![](images/23d22cab595caf293f50c41fe85f8cbc0826effc1e9fbccbdd2efc113c50d6d7.jpg)  
Fig. 1. A typical structure of DC grid.

Moreover, it does not have the fault isolation ability. It still relies on other equipment to cut off the DC fault current.

The DCCB is a relatively safe solution because it can be flexibly arranged at any point in the grid and can interrupt the fault circuit without affecting the operation of the converter and the normal DC line [12]. The hybrid DCCB has been deeply studied by [13]. The design idea of this type DCCB is to close the mechanical switch under normal condition to reduce the on-state power loss. The power electronic branch only works under the condition of fault status. A 320 kV/2kA hybrid DCCB is manufactured by ABB, Ltd., in 2012, as shown in Fig. 2. On the fault status, firstly, block all the IGBTs of branch 1 and trigger all the IGBTs of branch 2, the fault current will be transferred from branch 1 to branch 2; secondly, open the UFD (ultra-fast disconnector) of branch 1 when the fault current in this branch is attenuated to zero; thirdly, close the IGBTs of branch 2 when the UFD is fully opened, then the fault current will be transferred to the MOA and attenuated to zero quickly.

However, the fault current may rise to the maximum limit of the IGBTs in hybrid DCCB under the condition of larger capacity transmission occasion. Increasing the current limiting reactance can avoid this problem but will affect the dynamic characteristics of the system. Therefore, many fault detection methods are unable to meet the needs of DC grid protection due to the time delay, which can only be used as backup protection strategies. A feasible fault protection strategy in DC grid: the measured ROCOV [14], can meet the needs of rapidity. But in some cases it may cause misjudgment. In the case of small resistance short circuit occasion, a local line fault may be mistaken as a remote line fault, because the local ROCOV value may be lower than the critical threshold value to discriminate local and remote fault, and the misjudgment cannot be amended through communication due to high delay. At the same time, the fault current rising-rate is still too large. If the current limiting operation cannot be taken in time, the fault current will exceed the maximum breaking capacity of DCCB, and further lead to the outage of the DC grid. Thus, this type of hybrid DCCB cannot fully meet the need of DC grid.

![](images/198994bea6ec4df96fa72ce077bc689993b9476c284525a4a301fe3580505497.jpg)  
Fig. 2. Generic structure of hybrid DCCB developed by ABB.

The feasibility of future DC grids depends largely on their capabilities to withstand DC faults. In order to overcome the problems mentioned above, a novel DCCB topology with current limiting capability is proposed in this paper. It has modular characteristics. Therefore, the number of branches can be flexibly configured to increase the current limiting effect while reducing the current value of each branch to adapt large current condition. Because of its flexible current limiting ability, it can better cooperate with the ROCOV fault detection method and improve the system’s reliability.

The rest of this paper is organized as follows. The topology and working principle are introduced in Section 2. The equivalent circuit diagram of the topology and the current limiting mechanism are also studied in this Section. The comparative analysis of the typical DCCB solutions is detailed in Section 3. To verify the validity and the feasibility of the proposed CL-DCCB, the simulation studies in PSCAD/ EMTDC and experiment validation are presented in Section 4. Finally, the conclusions are given in Section 5.

# 2. Topology and working principle

# 2.1. Derivation of the topology

The proposed CL-DCCB consists of MCB and BCBs, as shown in Fig. 3(a), where L represents the reactors. The MCB includes three branches: branch 1 is a low loss branch, branch 2 is a power electronic branch, branch 3 is an energy absorption circuit, as shown in Fig. 3(b). where, power electronic branch can break fault current rapidly. The function of energy absorption circuit is to protect the IGBTs from overvoltage, which consists of MOA (metal oxide arrestor). It should be noted that IGBT modules displayed in Fig. 3(b) have been configured with equalizing circuit to prevent partial overvoltage [15–17]. Considering that each IGBT is configured with a diode rectifier circuit, the fault current is converted to the same direction. Therefore, the MCB can be able to cut bidirectional current on the premise of half the usage amount of IGBTs.

The topology of BCB is shown in Fig. 3(c), which includes three branches: branch 1 is a low loss branch, which is composed of UFD and several IGBTs, branch 2 is composed of capacitor banks, branch 3 is an energy absorption circuit.

# 2.2. Working principle

With issue to MCB, when conducting UFD and all the IGBTs in branch 1 and blocking all the IGBTs in branch 2, the MCB will run under low power loss mode. As path A in Fig. 4(a). In order to quicken the breaking speed, fault current path should always be transferred to branch 2 when a suspect fault occurs. Then breaking operation can be executed quickly when the fault is determined. The process can be described in detail as follows: firstly, trigger all the IGBTs in branch 2 and then block all the IGBTs in branch 1; secondly, open the UFD in branch 1 when the current in this branch drops to zero. The current path in this working mode is shown as path B. If the fault is confirmed, the breaking operation can be executed by blocking all the IGBTs in branch 2. As the current is interrupted by these IGBTs, the overvoltage will be induced by system inductance, then the fault current will be transferred to MOA when the over-voltage value exceeds the protection voltage of the MOA, as current path C in Fig. 4(a).

Due to the function of the diode rectifier bridge, unidirectional arrangement of the IGBTs can meet the requirement of the bidirectional breaking operation. The forward and reverse current paths are shown in Fig. 4(b) separately. Considering that the capacity and cost characteristics of diodes under the same parameters are obviously better than that of IGBTs, and the halve of IGBTs can also reduce the static and dynamic voltage balancing circuit, which can effectively reduce the system cost.

For the BCB, the UFD and IGBTs of branch 1 are conducted under

![](images/36d58bf8775705239abb77466d8a2f2b2dad82345c2c6ed3cd5d36afc8e7e55e.jpg)  
(a) Structure of CL-DCCB

![](images/7d334f2c3644916ec093bb6baee8cc0b2de8937e80feb75a0ba6f0a3ac3a3de3.jpg)  
(b) Topology of MCB

![](images/b17d83930ba645ea2d52f50cb2e8194681896f2c1d9c8198643cc728ba47e811.jpg)  
(c) Topology of BCB

![](images/67e822e22924c7256e76f191e0a7c5432ed72e1de013e80971b2968eff786563.jpg)  
Fig. 3. Topology of CL-DCCB.   
(a) Current paths under different working mode

![](images/7c79cfa8a662d3706b00d5e15ea51857824421e6ad29ce0a7cf6d6a114149b8b.jpg)

![](images/40ca0c518b04422ec99acb491cd3b29285eaf7137a1b6ccc5283b09114602518.jpg)  
(b) Current paths of power electronic branch   
Fig. 4. Current paths of MCB.

![](images/5ef698fe18dbd6ca372721873f7eba90146ab5af3920a9653e6f4b69a3d7d8b3.jpg)

![](images/bd23c21102b93efcd60681b3659154f62014d361db4a2a8437db82ed75c3b716.jpg)  
(a) The current paths of BCB   
(b) The opening process of UFD   
Fig. 5. Operation process of the BCB.

normal state, and the current path is shown as path A in Fig. 5(a). The power loss is relatively low as there are only several IGBTs in this branch. When the current limiting operation is required, block all the IGBTs in branch 1, After a short delay, open the UFD when the current of branch A dropped to zero, then fault current path as shown by path B. The opening process of UFD, as shown in Fig. 5(b), usually takes about 2 ms. Considering that the capacitor can restrain the overvoltage rising-rate, a high voltage capacitor bank is used as the auxiliary switching device in BCB. The insulation voltage level and the gap distance of UFD are positively correlated [18]. Therefore, the voltage breakdown of UFD can be prevented by an appropriate capacitor. In this case, the capacitor voltage is always less than the insulation voltage of UFD during the operation process. After the UFD is extremely open, the capacitor voltage will gradually achieve the MOA protection value. The function of MOA is to ensure that the voltage at both ends of the capacitor during current limiting operation will not exceed its maximum designed value. Then, fault current will be transferred to path C and attenuated to zero quickly. Through this control, the branch inductors are connected in series, thus the current limiting effect is achieved.

The working mode of proposed CL-DCCB is as follows: 1) Normal operation mode. In this mode, inductors of different branches are connected in parallel with current split into N branches (N is the number of reactor branches); 2) Fault current limiting mode. In this mode, the reactors of each branch are connected in series, with the system’s inductance increased from L/N to N*L to limit the suspected fault current rising-rate; 3) Current limiting plus circuit breaking mode. In this mode, the branches series will be connected with each other to reduce the current rising-rate before being shut down. Then the CL-DCCB continues to break or recover according to the feedbacks. This mode provided extra time for fault detection. However, conventional DCCB may have an increased risk of misjudging as the time for fault detection is relatively shorter.

The current directions in different modes are shown in the Fig. 6 Where, normal running state is shown in Fig. 6(a), fault current limiting state is shown in Fig. 6(b), and the rising-rate of fault current under this mode is effectively suppressed.

The operational process of mode “3″ is shown in Fig. 7. Its working process is as follows: Close all the UFDs and IGBTs of branch 1 in the

![](images/715b7b2d7e91f5e7e11c91e3350f3e2bf3fae644991f8006dc30be42a2494163.jpg)

![](images/37b831656167d2e13fe51ab2e664abd0662968e3bf44f6dcd314baa5c335d34d.jpg)  
(a) Normal working mode   
(b) Current limiting mode

![](images/eff2b82958b5a10878d262fac1fbfd506e5150d237250f2d906d529c1ba92c1a.jpg)  
Fig. 6. Different current paths under normal mode and current limiting mode.   
Fig. 7. Operational process under fault condition.

two BCBs and the MCB under normal conditions. When a suspected failure occurs, current limiting mode will be executed: firstly, block all the IGBTs in branch 1 of all the BCBs and the MCB, then, open the UFD of BCB when the fault current in branch 1 dropped to zero. In case of permanent fault, all the IGBTs of branch 2 in the MCB should be switched off to cut the fault current, otherwise, recover to normal operation by closing all the UFDs in MCB and BCBs, then turn on the IGBTs in branch 1 of MCB and BCBs.

# 2.3. Analysis of current limiting operation

In this section, the current limiting process under ideal conditions was analyzed firstly, and then the current limiting process under practical conditions was analyzed.

The proposed CL-DCCB can greatly increase the equivalent inductance by changing the connection mode of the reactor branches, as shown in Fig. 8.

Before the current limiting operation is executed, each inductor is connected in parallel. The fault current of each branch can be expressed in (1):

![](images/c5ba8787ef33af930409a8cd3ab6eef18639ade2174688ea53a89894ccb026e3.jpg)  
Fig. 8. Current limiting transformation process.

$$
\left\{ \begin{array}{l} i _ {1} = \frac {1}{L _ {1}} \int_ {- \infty} ^ {t} u (\xi) d \xi \\ i _ {2} = \frac {1}{L _ {2}} \int_ {- \infty} ^ {t} u (\xi) d \xi \\ i _ {3} = \frac {1}{L _ {3}} \int_ {- \infty} ^ {t} u (\xi) d \xi \end{array} \right. \tag {1}
$$

where u(ξ) is the transient voltage at both ends of the CL-DCCB.

The DC line current is shown in (2):

$$
\begin{array}{l} i = i _ {1} + i _ {2} + i _ {3} \\ = \left(\frac {1}{L _ {1}} + \frac {1}{L _ {2}} + \frac {1}{L _ {3}}\right) \int_ {- \infty} ^ {t} u (\xi) d \xi \\ = \frac {1}{L} \int_ {- \infty} ^ {t} u (\xi) d \xi \tag {2} \\ \end{array}
$$

The total inductance of the breaker is shown in (3):

$$
L = \frac {L _ {1} L _ {2} L _ {3}}{L _ {2} L _ {3} + L _ {1} L _ {3} + L _ {1} L _ {2}} \tag {3}
$$

The current of each branch can also be shown in (4)–(6):

$$
i _ {1} = \frac {L}{L _ {1}} i = \frac {L _ {2} L _ {3}}{L _ {2} L _ {3} + L _ {1} L _ {3} + L _ {1} L _ {2}} i \tag {4}
$$

$$
i _ {2} = \frac {L}{L _ {2}} i = \frac {L _ {1} L _ {3}}{L _ {2} L _ {3} + L _ {1} L _ {3} + L _ {1} L _ {2}} i \tag {5}
$$

$$
i _ {3} = \frac {L}{L _ {3}} i = \frac {L _ {1} L _ {2}}{L _ {2} L _ {3} + L _ {1} L _ {3} + L _ {1} L _ {2}} i \tag {6}
$$

As shown in (4)–(6), when the inductance of these branches are equal, the current value of each branch will be consistent. Thus, the current value of each branch is 1/3 of the total system current.

The value of flux linkages under normal state is shown in (7):

$$
\begin{array}{l} \psi_ {L} (0 _ {-}) = \psi_ {L 1} (0 _ {-}) + \psi_ {L 2} (0 _ {-}) + \psi_ {L 3} (0 _ {-}) \\ = L _ {1} i _ {L 1} (0 _ {-}) + L _ {2} i _ {L 2} (0 _ {-}) + L _ {3} i _ {L 3} (0 _ {-}) \tag {7} \\ \end{array}
$$

Under the current limiting mode, the reactors of each branch are connected in series. The value of flux linkages is shown in (8).

$$
\begin{array}{l} \psi_ {L} (0 _ {+}) = \psi_ {L 1} (0 _ {+}) + \psi_ {L 2} (0 _ {+}) + \psi_ {L 3} (0 _ {+}) \\ = \left(L _ {1} + L _ {2} + L _ {3}\right) i _ {\text {L i m i t}} \left(0 _ {+}\right) \tag {8} \\ \end{array}
$$

According to the conservation principle of flux linkages, (9) can be developed:

$$
\psi_ {L} (0 _ {-}) = \psi_ {L} (0 _ {+}) \tag {9}
$$

Thus, the current of the branches is limited to the value before the current limiting operation. Therefore, the current limiting mode has a function of depressing fault current to a certain extent.

From the above analysis, the inductance value of the CL-DCCB can be greatly increased by the current limiting control, and then the inductance value of the DC system can be increased to a degree. The increase of inductance can effectively restrain the rising-rate of the system fault current, thus the time margin for fault detection and breaking operation can be enlarged.

The current limiting process can be analyzed by the equivalent circuit shown in Fig. 9.

![](images/ea80f8c1fc5e1a4406fc9a5600f15388f5ee22b4d9f0c1c464fa693c9d9bbd17.jpg)  
(a) Equivalent circuit under normal mode

![](images/01d3021d9294f09bd10ef9aaf48394d23ede6225389fcd2ecb3d90f5e2d8fad0.jpg)  
(b) Equivalent circuit under current limiting mode   
Fig. 9. Equivalent circuit of proposed CL-DCCB.

When $C _ { 1 }$ and $C _ { 2 }$ are inserted in the circuit, they will be charged immediately, in which the voltage of $C _ { 1 }$ is determined by the voltage of $L _ { 1 }$ and $L _ { 2 } .$ . While the voltage of $C _ { 2 }$ is determined by the voltage of $\dot { \mathbf { L } } _ { 2 }$ and $L _ { 3 } .$ The followings can be deduced

$$
\left\{ \begin{array}{l} u _ {d c} = u _ {c 1} + L \frac {\mathrm {d} i _ {3}}{\mathrm {d} t} + i R \\ u _ {d c} = u _ {c 2} + L \frac {\mathrm {d} i _ {1}}{\mathrm {d} t} + i R \\ u _ {d c} = u _ {c 1} + u _ {c 2} - L \frac {\mathrm {d} i _ {2}}{\mathrm {d} t} + i R \\ i = i _ {1} + i _ {2} + i _ {3} \\ u _ {c 1} = L \frac {\mathrm {d} i _ {1}}{\mathrm {d} t} - L \frac {\mathrm {d} i _ {2}}{\mathrm {d} t} \\ u _ {c 2} = L \frac {\mathrm {d} i _ {3}}{\mathrm {d} t} - L \frac {\mathrm {d} i _ {2}}{\mathrm {d} t} \end{array} \right. \tag {10}
$$

Considering that the voltage of the reactor will drops to zero after entering steady state, $C _ { 1 }$ and $C _ { 2 }$ will have a charging and discharging process, and the rising-rate of charging voltage is relatively lower, thus the effective opening of the UFD is ensured. For the storage energy of $C _ { 1 }$ and $C _ { 2 }$ are limited, the subsequent discharge process will not cause a sharp increase of the system fault current.

# 3. Comparison of the three solutions

# 3.1. Economic analysis

This Section will make a comparison between the proposed topology and the existing typical DCCB schemes including the ABB’s DCCB scheme and the global energy interconnection research institute’s (GEIRI) DCCB scheme.

IGBT model 5SNA 2000 K450300 is adopted to analyze the schemes. The nominal parameter of the model is 4.5 kV/2kA [19], the design voltage is 3 kV considering the security margin, and the peak interrupting current is 9kA when applied to DCCB [13]. Diode model 5SDD

36 K5000 is chosen in proposed CL-DCCB scheme. Its nominal parameter is 5 kV/3.6kA.

On the condition of ± 500 kV project, the peak voltage value of the MCB is 1.5 times of the rated voltage of the DC cables [20]. Considering the safety allowance and the characteristic of MOA, the two sides of IGBT branches have to tolerate 800 $\mathbf { k V } ,$ therefore, 270 IGBTs need to be connected in series. on the condition of bidirectional breaking operation, the number of IGBTs is 540 in ABB’s scheme. Similarly, GEIRI’s scheme also needs 540 IGBTs.

With the issue of proposed CL-DCCB, the protection voltage of MOA in breaking valve should also be set to 800 kV. For a diode rectifier circuit configured on each IGBT modules, single direction of the IGBTs can meet the requirements of bidirectional breaking operation. Therefore, breaking valve only needs 270 IGBTs and 1080 diodes.

Considering the auxiliary capacitor is configured to achieve the breaking effect in BCB, only a few of the IGBTs are needed in the low loss branch. Therefore, the BCB is mainly composed of capacitor banks, MOAs and UFDs. As the voltage across the capacitor banks or UFD are set to 800 kV, the voltage of capacitor of BCB should also be designed to this voltage value, considering the rated voltage of a DryDCap type capacitor of ABB is 3 kV, 540 capacitors are needed in two BCBs.

The comparison of the devices usage under the three schemes is shown in the Table 1:

Table 1 shows the usage of IGBTs for proposed scheme is halved, while the usage of diodes, capacitor banks, and UFDs are increased largely. Therefore, the cost of proposed scheme is higher than other two scheme. However, the proposed scheme can effectively slow down the rising-rate of fault currents, thus more time for fault detection and isolation is permitted.

# 3.2. Performance analysis

With the increase of the voltage and current in the transmission line of large-scale HVDC grid in future, the short circuit current and its rising-rate will also be increased. Although the rate can be suppressed by increasing the line reactor, the dynamic behavior of the grid will also be affected. Because of the large reactance, the voltage source converter will be closed to the current source converter. Therefore, the characteristics of the voltage source converter will be counteracted. What’s more, at present, many fault detection methods are unable to meet the needs of DC grid protection due to the time delay. Most of them can only be used as backup protection strategies except ROCOV, etc.

When ROCOV method is adopted, the width of the boundary between the local and remote faults is limited due to the consideration of the short circuit through impedance and the bipolar short circuit. So the ROCOV method is probably to miss what the real state is.

A 4-terminal DC grid simulation model, as shown in Fig. 10, is used to test the ROCOV data. When line inductor is set to 50mH, the fault point is at $\mathrm { { F } } _ { 1 } ,$ which 10 km away from MMC4. The length of the line1, line $_ { \mathrm { 2 } } ,$ line , line is 227 km, 126 km, 219 km, 66 km, respectively. Other parameters are shown in Tables A1 and $\mathrm { A 2 } ,$ and the ROCOV data of point A (local ROCOV) and point B (remote ROCOV) under different types of faults are shown in Table 2:

It can be seen from Table 2 that, the ROCOV level of local grounding fault is 290 kV, the same as the remote bipolar short circuit when the grounding fault resistance is 50 Ω. At this time, it is easy to misjudge the local fault as the remote fault. There are two solutions to solve this

Table 1 arameters of simulated DC grid.   

<table><tr><td>schemes</td><td>IGBTs</td><td>Diodes</td><td>Capacitors</td><td>UFDs</td></tr><tr><td>ABB</td><td>540</td><td>0</td><td>0</td><td>1</td></tr><tr><td>GEIRI</td><td>540</td><td>0</td><td>270</td><td>1</td></tr><tr><td>Proposed</td><td>270</td><td>1080</td><td>540</td><td>3</td></tr></table>

![](images/49185b1b9b17ffe5b392cfaa47c9cbf06023e5c05c363b2710fb693494a0ab17.jpg)  
Fig. 10. 4-terminal DC grid simulation model.

Table 2 Parameters of simulated DC grid.   

<table><tr><td>Fault type</td><td>Local ROCOV</td><td>Remote ROCOV</td></tr><tr><td>Ground fault 0Ω</td><td>350 kV</td><td>240 kV</td></tr><tr><td>Ground fault 50Ω</td><td>290 kV</td><td>200 kV</td></tr><tr><td>Ground fault 100Ω</td><td>250 kV</td><td>165 V</td></tr><tr><td>Bipolar short circuit</td><td>525 kV</td><td>290 kV</td></tr></table>

problem. One solution is to compare and analyze the ROCOV data from positive and negative DC line reactors to determine the short circuit type. If the ROCOV of two reactors are detected simultaneously, the bipolar short circuit can be confirmed. Then, whether the fault is local or remote can be determined according to the bipolar fault type. Obviously, the additional communication process will increase time delay. The other solution is to perform a current limiting operation when a suspected fault is detected, which can increase the margin for backup protection.

The proposed CL-DCCB has many advantages. Firstly, it can present relatively low inductance in normal state to ensure the dynamic performance of the grid during normal state, while high inductance in current limiting mode to suppress the fault current. Compared with the existing DCCB topology, this topology can start current limiting operation when a suspected fault occurs, which can decrease the current rising-rate and allow longer fault detect time. When the detection circuit shows what has happened, it can be determined whether to implement breaking operation or recover to normal state. This mode allows longer fault detection time and breaking operation delay while guaranteeing the fault current under the maximum limit. Secondly, as the current in each branch are reduced, lightweight UFD can be used in CL-DCCB. This means that the cost of UFD can be reduced as it is easier to be manufactured. In addition, the breaking contact can be accelerated due to lower inertance, which can free the pull rod from the limit of materials and process. Therefore, the lightweight contact can get larger gap within the same period of time, which can alleviate the demand of multi-break UFD. Moreover, extended MMC block delay is allowed under current limiting mode for the fault rising-rate is reduced to a great extent. The above analysis indicated good potential of this method for further study.

# 4. Simulation and experimental results

# 4.1. Simulation results

A four-terminal MMC-based HVDC grid model is built in PSCAD/ EMTDC to verify the proposed CL-DCCB, and the frequency dependent overhead line model is adopted. The detailed parameters of this simulation model are shown in the Tables A1 and A2.

Simulation of the current limiting operation will be first analyzed in this Section, and the influence of the current limiting operation on the

![](images/82c0cc3f06f8a6c72401d26a3c7c4d3ce7a9cb84059cd4a2214f2f349a08195a.jpg)

![](images/9839883aa08927a884033e1711aa9b49c3c4521deb78b0d4d3a2df2768e6d6be.jpg)  
Fig. 11. Currents of MCB and BCB under current limiting operation.

fault current is verified. Then the current limiting operation plus breaking operation are shown in this Section. The current limiting operation is performed when suspect fault occurs, then breaking operation is conducted on the fault line when the fault is confirmed. Finally, the comparison between the proposed scheme and the ABB’s scheme is shown。

# 4.2. Waveforms of proposed CL-DCCB

The system is in double-pole short current fault state at 1.0 s. The distance between the MMC4 and the fault point $\mathrm { F } _ { 1 }$ is 10 km, with the fault point located on line 3. For the ROCOV algorithm has advantages of small quantity of calculations, and the fault point located not far from the breaker, the current limiting operation can be performed at 1.00015 s. The ROCOV of the reactor at point A is detected at 1.00015 s, then current limiting operation is executed, the current limiting valve is cut off, and the energy of this valve is dissipated in the MOA of this valve. Fig. 11(a) shows the current waveforms of the three branches of BCB 1. The current waveforms are the same as the branches of BCB 2. The fault current is transferred to the capacitor branch when the power electronic devices in low loss branch is closed. Then the capacitor will be charged, with the capacitor voltage reaching the threshold of the MOA protection voltage value, the fault current is transferred to the MOA. As the capacitor banks are in the circuit all the time, there will be a resonance between the branch inductor and the capacitor banks. With the energy dissipation of MOA, the capacitor current will reverse for a period of time. Then the system current will have a descending process, as shown in Fig. 11(b) At this time, the current path of MCB has been transferred to branch 2 during the current limiting operation. The UFD has been fully opened, the power electronic devices have been triggered, and thus the breaking operation can be initiated immediately. If it runs under the current limiting mode, the fault current will rise at a lower rising-rate.

The capacitor voltage waveforms of BCB 1 and BCB 2 are shown as Fig. 12. The voltage increases to 400 kV within 2 ms, and eventually admit 800 kV. Considering that the insulation voltage of the UFD will increase when the gap distance increases with time, the insulation voltage of UFD will reach to 800 kV within 2 ms. The insulation breakdown will not happen as the actual voltage of the gap is always less than the UFD insulation voltage in the whole breaking process.

Assuming that the fault detection time is 11 ms and the current limiting operation is executed at 1.00015 s when a suspected ROCOV alert occurs, the system will run under the current limiting mode before

![](images/139d2007ecc5ff184362155f714e6f35a583176d3609724352b294ceb0099fbe.jpg)  
Fig. 12. Capacitor voltage waveforms of BCB 1 and BCB 2.

![](images/4e1b776e234e7821741c63714b2d3f7ccf79b0d1880051bc2cc0caec181a9d7a.jpg)  
Fig. 13. Currents of MCB.

the fault is detected by backup protection method. When the fault is confirmed, the breaking operation will be operated at 1.011 s. The fault current waveforms of MCB are shown in Fig. 13.

The development of fault current includes four stages: firstly, the current started to rise rapidly as the fault occurs, as shown in time period $\mathbf { t } _ { 1 } ;$ secondly, the fault current is reduced for the fault energy is partly absorbed by the capacitor of BCBs when the current limiting operation is implemented, as shown in time period $\mathbf { t } _ { 2 } ;$ thirdly, the fault current rises at a lower rate under the current limiting mode, as shown in time period $\mathbf { t } _ { 3 } ;$ fourthly, due to the existence of capacitance, resistance and inductance in the loop, the fault current enters the stage of oscillation and attenuation.

As shown in Fig. 14. the absorbed energy of BCB 1 and 2 is 6.5 mJ, respectively. Considering the duration of the DC fault up to 11 ms before the breaking operation, the absorbed energy of MCB is 93 mJ, as shown in Fig. 15.

# 4.3. Waveforms of ABB’s scheme

Fig. 16 showed a comparison between the fault current of proposed scheme and ABB’s scheme. At this time, the reactance of the ABB’s scheme is consistent with the reactance of the proposed scheme under non-current-limiting conditions. Compared with the non-current-limiting mode, the fault current under current limiting mode reaches to 9kA after 12 ms, while the non-current-limiting mode only requires 2 ms to reach the same current value. Thus the time for fault detection

![](images/b8594f9d049284602dcc898504de4ac5710fa9fffaf0a8f3947df920ea6fcc7a.jpg)  
Fig. 14. Energy absorption value of BCB.

![](images/d4f35c30fcc6d0bd51d80d9bc13345adb74587b84a7a13141bbb36bad865cc73.jpg)  
Fig. 15. Energy absorption value of MCB.

![](images/c5d3ebef8b6e99282a334f2b3c4771666175654f87a75bf9515f0ffab4f5a94f.jpg)  
Fig. 16. Comparison of current limiting effect, current 1: fault current waveform without current limiting function, current 2: fault current waveform under current limiting mode.

and breaking operation delay is increased.

If the maximum reactance of the proposed CL-DCCB is taken as a reference, the line reactance of the ABB’s scheme is 0.9 mH, and the fault current is up to 11.5 kA when the breaking operation is executed at 1.011 s, as shown in Fig. 17. Unlike the proposed CL-DCCB, there is no energy absorption process before the breaking operation in ABB’s scheme, so the fault current is greater than proposed scheme.

The total energy absorption of the DCCB is 130 mJ, as shown in Fig. 18, which is much larger than 106 mJ of proposed CL-DCCB. The difference is due to the lower equivalent line reactance of the proposed scheme at normal working state. At this time, the energy stored in the reactor is smaller. What's more, the arrester and the capacitor of the BCB has absorbed part of the energy under the current limiting state. While the reactance value of ABB’s scheme is larger under normal working state, so there is more energy stored in the line reactor. Therefore, the proposed scheme is better than ABB’s scheme in terms of fault current limiting effect and arrester requirement.

# 4.4. Experimental results

A prototype is used to verify the proposed CL-DCCB, as shown in Fig. 19. The parameters of this prototype are given in Table A3.

The DC side short circuit fault is triggered by a thyristor. After 1 ms, the fault is detected and the current limiting operation is executed by blocking IGBTs in BCB. The trigger pulse of thyristor and IGBT are

![](images/f3e229add04536c222efe7449028b05e73e89ea75678d82955eb1baae0142493.jpg)  
Fig. 17. DC fault current waveform of ABB’s DCCB.

![](images/07049380e73e8c27ce2ad992a5fa26dbb1e0cab2ebb3b35ec2de84987f1fda59.jpg)  
Fig. 18. Energy absorption value of ABB’s DCCB.

![](images/b63f48617fd5528ed1e578741a81b644ec03b18f13ebe7088351c77ed20ff46d.jpg)  
Fig. 19. Prototype of proposed CL-DCCB.

![](images/d13d73e181d7bf9312e8c420d938a02bc1aa66b786332b0d5f6154942c55ecb5.jpg)  
Fig. 20. Trigger pulses of thyristor and IGBTs.

shown in Fig. 20, and the waveform of DC fault current is shown in Fig. 21. The rising-rate of the fault current is dramatically reduced after the current limiting operation. The capacitor voltage waveform of BCB is shown in Fig. 22. The voltage begins to oscillation attenuate after it is reached to the maximum value. Fig. 23 is the fault current waveform under the non-current-limiting state. Compared to Fig. 21, it is obvious that the rising-rate of the fault current is larger than the current limiting state. Therefore, the current limiting operation can greatly restrain the rising-rate of the fault current and win the time for the fault protection.

![](images/72fdfe2ca46cc691a9b47adfe3c827b95ccd64b2aa22b435bc7a269202f12617.jpg)  
Fig. 21. DC fault current waveform under current limiting mode.

![](images/2fc607a3a7776b71c45225444d3c495212c7c8476c3288d690b1a2ebd61d0c2c.jpg)  
Fig. 22. Capacitor voltage waveform of the BCB.

![](images/5b9cfe3b2770a87c06020c5a62cd7c2b64aacede4142aa25e8fc56707d6eced9.jpg)  
Fig. 23. DC fault current waveform without current limiting operation.

# 5. Conclusions

This paper focuses on the study of DCCB, and proposed a CL-DCCB topology based on the analysis of hybrid DCCB raised by ABB and GEIRI. The mathematical model of this topology is built and analyzed, then the simulation model and prototype is studied in this paper. Finally, follow conclusions are drawn.

Current limiting mode can be activated when a suspected fault occurs. The current value and the current rising-rate can be limited effectively, thus, longer fault detection time can be allowed and misoperation of DCCB can be avoided.

The number of inductor branches can be configured flexibly on the basis of current grade and costs.

With the function of diode rectifier bridge, the number of IGBTs can be reduced effectively, but the number of UFDs, MOAs and high voltage capacitor banks is increased and the total cost of proposed CL-DCCB also went up. The advantage is a longer fault tolerance time. At this time, the fault current will exceed the breaking capacity under traditional DCCB scheme.

# Appendix

See Tables A1, A2, and A3.

Table A1 Parameters of the current limiting CL-DCCB.   

<table><tr><td>Item</td><td>Symbol</td><td>Value</td></tr><tr><td>Branch inductance/mH</td><td>L</td><td>100</td></tr><tr><td>Branch numbers</td><td>N</td><td>3</td></tr><tr><td>Threshold current of IGBT/kA</td><td>IMAX</td><td>5</td></tr><tr><td>UFD delay/ms</td><td>TI</td><td>2</td></tr></table>

Table A2 Parameters of simulated DC grid.   

<table><tr><td>Item</td><td>station A</td><td>station B</td><td>station C</td><td>station D</td></tr><tr><td>Station capacity/MVA</td><td>1500</td><td>1500</td><td>3000</td><td>3000</td></tr><tr><td>Rated DC-link voltage/kV</td><td>± 500</td><td>± 500</td><td>± 500</td><td>± 500</td></tr><tr><td>Transformer capacity/MVA</td><td>3400</td><td>1700</td><td>3400</td><td>3400</td></tr><tr><td>Arm reactor/mH</td><td>100</td><td>100</td><td>100</td><td>100</td></tr><tr><td>DC reactor /mH</td><td>150</td><td>150</td><td>150</td><td>150</td></tr><tr><td>Sub-module capacitance/μF</td><td>7000</td><td>7000</td><td>7000</td><td>7000</td></tr></table>

Table A3 Parameters of the Prototype.   

<table><tr><td>Item</td><td>Symbol</td><td>Value</td></tr><tr><td>Branch inductance/mH</td><td>L</td><td>25</td></tr><tr><td>Branch numbers</td><td>N</td><td>3</td></tr><tr><td>Threshold current of IGBT/kA</td><td>IMAX</td><td>0.1</td></tr><tr><td>DC voltage/kV</td><td>Udc2</td><td>0.1</td></tr><tr><td>DC reactor/mH</td><td>Ldc</td><td>20</td></tr><tr><td>BCB capacitance/μF</td><td>Cb</td><td>50</td></tr></table>

# References

[1] Flourentzou N, Agelidis VG, Demetriades GD. VSC-based HVDC power transmission systems: an overview. IEEE Trans Power Electron Mar. 2009;24(3):592–602.   
[2] Egea-Alvarez A, Bianchi F, Junyent-Ferre A, Gross G, GomisBellmunt O. Voltage control of multiterminal VSC-HVDC transmission systems for offshore wind power plants: Design and implementation in a scaled platform. IEEE Trans Ind Electron Jun. 2013;60(6):2381–91.   
[3] FPSG (Friends of the Supergrid) WG2. Roadmap to the super grid technologies[R]. http://www.stopthecrime.net/smartmeters.   
[4] Farhadi M, Mohammed OA. Event-based protection scheme for a multiterminal hybrid dc power system. IEEE Trans Smart Grid Jul. 2015;6(4):1658–69.   
[5] T. An, G. Tang, and W. Wang, “Research and application on multi-terminal and DC grids based on VSC-HVDC technology in China,” High Voltage, vol. 2, no. 1, pp. 1–10, 2017.9.   
[6] Yu X, Wei Y, Jiang Q, Xie X, Liu Y, Wang K. A novel hybridarm bipolar MMC topology with dc fault ride-through capability. IEEE Trans Power Del May 2017;32(3):1404–13.   
[7] Zeng R, Xu L, Yao L, Morrow DJ. Precharging and DC fault ride-through of hybrid MMC-based HVDC systems. IEEE Trans Power Del Jun. 2015;30(3):1298–306.   
[8] Shi Y, Li H. Isolated Modular Multilevel DC-DC Converter With DC Fault Current Control Capability Based on Current-Fed Dual Active Bridge for MVDC Application’. IEEE Trans Power Electron 2018;33(3):2145–61.   
[9] Rojas CA, Kouro S, Perez MA, Echeverria J. Dc-dc mmc for hvdc grid interface of utility-scale photovoltaic conversion systems. IEEE Trans Ind Electron 2018;65(1):352–62.   
[10] Huang HY, Xu Z, X. L,. Improving performance of multi-infeed HVDC systems using grid dynamic segmentation technique based on fault current limiters. IEEE Trans Power Syst Mar 2012;17(3):1664–72.

[11] Morishita Y, Ishikawa T, Yamaguchi I, Okabe S. Applications of DC Breakers and Concepts for Superconducting Fault-Current Limiter for a DC Distribution Network. IEEE Trans Appl Supercond 2009;19(4):3658–64.   
[12] Majumder R, Auddy S, Berggren B, Velotto G, Barupati P, Jonsson TU. An alternative method to build DC switchyard with hybrid DC breaker for DC grids. IEEE Trans Power Del Apr. 2017;32(2):713–22.   
[13] Hassanpoor A, Hafner J, Jacobson B. Technical assessment of load commutation switch in hybrid HVDC breaker. IEEE Trans Power Electron Oct. 2015;30(10):5393–400.   
[14] Sneath J, Rajapakse AD. Fault detection and interruption in an earthed HVDC grid using ROCOV and hybrid DC breakers. IEEE Trans Power Del Jun. 2016;31(3):973–81.   
[15] Chokhawala RS, Sobhani S. Switching voltage transient protection schemes for high-current IGBT modules. IEEE Trans Ind Appl 1997;33:1601–10.   
[16] Withanage R, Shammas N. Series connection of insulated gate bipolar transistors (IGBTs). IEEE Trans Power Electron Apr. 2012;27(4):2204–12.   
[17] Shiqi J, Ting L, Zhengming Z, Hualong Y, Liqiang Y. Seriesconnected HV-IGBTs using active voltage balancing control with status feedback circuit. IEEE Trans Power Electron Aug. 2015;30(8):4165 74.   
[18] Wen T, Zhang Q, Ma J, et al. Discharge characteristics of long SF6 gas gap with and without insulator in GIS under VFTO and LI[J]. CSEE J Power Energy Syst 2015;1(3):16–22.   
[19] ABB Switzerland Ltd. Datasheet IGBT 5SNA 2000K450300 [EB/OL]. [2014-07-19]. http://new.abb.com/products/semiconductors.   
[20] Davidson C, Whitehouse R, Barker C, Dupraz J, Grieshaber W. A new ultra-fast hvdc circuit breaker for meshed dc networks. In: Proc. IET ACDC, Birmingham, U.K., Feb. 10–12 2015, p. 7.

Shuai Li was born in Henan, China. He received the B.S. and M.S. degrees from Nanyang Institute of Technology and Taiyuan University of Technology in 2011 and 2014

respectively. Currently he is a Ph.D. student at NCEPU. His research interests include MMC based dc grid protection and control.

Jiyuan Zhang was born in Zhejiang, China in 1995. He received his B.Sc. degree in Hangzhou Dianzi University, Hangzhou, China in 2017. Currently he is pursuing his Master degree at NCEPU, his research interests include MMC-HVDC and dc grid.

Jianzhong Xu (M’14) was born in Shanxi, China. He received the B.S. and Ph.D. degrees from North China Electric Power University (NCEPU) in 2009 and 2014 respectively. Currently, he is an associate professor of the State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, NCEPU. From 2012 to 2013 and 2016 to

2017, he was respectively a visiting Ph.D. student and Post-Doctoral Fellow (PDF) at the University of Manitoba. He is now working on the high-speed electromagnetic transient (EMT) modeling and control & protection of MMC-HVdc and dc grid.

Chengyong Zhao (M’05-SM’15) was born in Zhejiang, China. He received the B.S., M.S. and Ph.D. degrees in power system and its automation from NCEPU in 1988, 1993 and 2001, respectively. He was a visiting professor at the University of Manitoba from Jan. 2013 to Apr. 2013 and Sep. 2016 to Oct. 2016. Currently, he is a professor at the School of Electrical and Electronic Engineering, NCEPU. His research interests include HVdc system and dc grid.