# A multi-area Thevenin equivalent based multi-rate co-simulation for control design of practical LCC HVDC system

![](images/c7fd1fe08967b1897f91330bf44a5931dc81d154de3491a37cdfb40411c60399.jpg)

Yupeng Lia , Dewu Shua,⁎ , Jingwei Hua , Zheng Yana , Yun Zhoua , Haifeng Wang

a High-Performance Simulation Center, Key Lab of Control and Power Transmission and Conversion, Department of Electrical Engineering, Shanghai Jiaotong University, 200240 Shanghai, China

b State Grid Shanghai Municipal Electric Power Company, China

## A R T I C L E I N F O

Keywords:   
Line commutated converter (LCC) based HVDC   
Multi-rate co-simulation   
Multi-Area Thevenin Equivalent (MATE)   
Commutation failure   
Improved control strategy

## A B S T R A C T

The line commutated converter (LCC) based HVDC transmission is often adopted to transmit the large capacity of renewable energy, however, it is threatened by several critical issues, such as, commutation failures (CFs). In order to reduce CFs and improve the recovery characteristics of the HVDC, improved control and protection strategies are always desirable. On the other hand, an accurate and efficient electromagnetic transient (EMT) simulation method is highly necessary to design the so-called control strategy, where the traditional transient stability and EMT models cannot meet the accuracy and efficiency requirements simultaneously. To resolve these issues, a Multi-Area Thevenin Equivalent (MATE) based multi-rate co-simulation method is proposed, where the accuracy is guaranteed by the proposed MATE based transmission line model (MATE-TLM) and the efficiency is significantly improved by adopting several accelerating techniques, such as, the MATE-TLM and multi-rate cosimulation scheme. Further, a novel improved control strategy based on the concept of virtual impedance is proposed to reduce CFs and to increase the recovery speed of DC system. Simulation results of a practical AC/DC grid by the improved control strategy have well validated the effectiveness of the proposed MATE based multirate co-simulation method.

## 1. Introduction

With the increasing penetration of renewable energy, the line commutated converter (LCC) based HVDC is adopted to increase large capacity of renewable energy sources. However, several tough issues, such as the commutation failures (CFs), threaten the normal operation of the LCC based HVDC. Generally, CF occurs when a converter valve that is supposed to turn off keeps conducting without transferring its current to the next valve according to the firing sequence. CF can trigger temporary reduced transmission power, drop of DC voltage, over-current and sometimes longer duration serious transients, etc. These problems will become more severe when the LCC based HVDC is connected to a weak AC system. For example, the China Southern Grid recorded the continuous CFs of Guanyinyan HVDC project. This accident caused a reduction of over 3000 MW transmitted power by HVDC links and it caused the frequency stability issue at the inverter side. According to past experiences, CF should be carefully resolved by improving the control and protection schemes in order to guarantee the fault ride-through ability as well as the recovery characteristics after faults [1–6]. As a result, it is always required to propose advanced control and protection strategies to reduce CFs and improve the recovery characteristics of the HVDC.

Previous research work to reduce the CFs can be summarized in two categories: (1) the criterion to detect CFs: a power component fault detection method (PCD) is proposed to determine whether it is an asymmetric or symmetric fault [7]. Several indicators, such as Multi-Infeed Interaction Factor (MIIF), Effective Short Circuit Ratio (ESCR), etc., are proposed to evaluate the severity of the CFs [8–10]. (2) improved control strategy to reduce CFs: in [11,12], parameters of controllers are tuned based on the fuzzy logic technique in order to reduce CFs. However, the complexity of the co-called fuzzy logic will complicate the overall controllers [13]. Traditionally, the voltage-dependent current order limit (VDCOL) is adopted to lower the dc current order when the dc voltage is dropped. However, this method is not fast enough to lower dc current order and how to improve the VDCOL is an ongoing research topic. Another choice is the commutation prediction methods [14], which can effectively detect voltage sags due to AC side ground fault and prevent the potential commutation failure or even continuous commutation failure via increasing the extinction angle in advance. However, the increase of extinction angle will increase the consumed reactive power of the AC side unexpectedly.

Up to now, in order to design the desired control and protection strategies and study the interactions between the LCC based AC/DC grids, an accurate and efficient electromagnetic transient (EMT) simulation method is highly necessary. However, in order to simulate the fast-switching dynamics of power electronic devices, the time-step of the traditional EMT simulation method is always limited under 20–50 μs. It increase the computational burden dramatically under a unanimous and tiny time-step of a traditional EMT program. The computational burden is increased due to the following reasons: (1) the system scale is dramatically increased by the large-scale AC grids; (2) the tiny time-step is restricted by the power electronic devices, such as the LCC. Therefore, a multi-rate co-simulation method is a desirable solution when simulating large-scale AC/DC systems [15–18]. In other words, the entire network is partitioned into the AC and DC systems, where the time-steps of AC/DC systems are chosen as ΔT and Δt (ΔT = nΔt). Several interface models, such as the Thevenin/Norton equivalent circuit [17,19], and the transmission line model [20,21], are proposed to reflect the interactions between AC and DC systems. However, even if the multi-rate co-simulation is applied, the simulation efficiency is still un-satisfactory due to the large scale of AC systems and their nonlinear and frequency dependent dynamics. Therefore, the Multi-Area Thevenin Equivalent (MATE) technique is utilized to further improve the efficiency. Unfortunately, how to combine the MATE technique and the interface model of the multi-rate co-simulation has not yet been studied deeply and applied to control design of practical LCC HVDC systems. The previous research [22] discusses the concept of MATE based on two simple subnetworks. Its main limitation was on the simplicity of the illustrative simulation circuit, where the AC/DC systems represented by ideal equivalent circuit are inadequate to inflect the complexity of the large-scale AC/DC systems. Also in practical large-scale AC/DC systems, multi subnetworks and boundary nodes are needed to discussed in great details.

To resolve these issues, a novel improved control strategy based on the concept of virtual impedance is proposed to reduce the probability of the CFs and to increase the recovery speed of DC system, especially when connected to weak AC systems. The advantages of the proposed control strategies are well validated by the proposed multi-rate co-simulation method. The novelty of the proposed multi-area Thevenin equivalent based multi-rate co-simulation method is summarized as follows:

(1) the MATE based transmission line model (MATE-TLM) is proposed to reflect the wide frequency band interactions between the LCC and the large-scale AC grids;

(2) the efficiency of the so-called MATE based multi-rate co-simulation method is significantly improved in two aspects. The efficiency of simulating large-scale AC grids is improved by the MATE technique and the efficiency of simulating the overall LCC based AC/DC grids is further improved by the multi-rate co-simulation structure.

The rest of the paper is organized as follows: Section 2 details the method of multi-rate co-simulation based on the MATE technique; Section 3 demonstrates the foundation of the virtual resistance based improved strategy for the LCC; Section 4 demonstrates the effectiveness of the proposed simulation method as well as the proposed control strategy. Section 5 draws the conclusions.

## 2. Multi-Area Thevenin Equivalent (MATE) based multi-rate cosimulations

As claimed, the computational burden of large-scale AC/DC grids has been greatly increased by the following reasons: (1) the increased scale due to the large number of components inside the AC grid; (2) the tiny time step, which is restricted by the fast switching dynamics of power electronic devices; (3) an unanimous and tiny time-step is only allowed by the traditional EMT models, which results in huge computational burden. In order to improve the simulation efficiency from the aspect of network partitioning and coordinated simulation structure, the proposed Multi-Area Thevenin Equivalent (MATE) technique will be used to decouple the whole system into several independent and smaller subsystems. At the same time, the interactions between different subsystems are reflected by the so-called and specially designed multi-area Thevenin equivalent circuit, which is illustrated in Fig. 1.

![](images/0e15f05b3b1813baae478b42505e972bc60304066af352980d759897006cc111.jpg)  
Fig. 1. Network partitioning of the whole system.

## 2.1. Network partitioning by the MATE based transmission line model (MATE-TLM)

In order to simulate the whole system in an accurate and efficient way, the whole system is firstly partitioned into the AC and DC systems, respectively (see Fig. 1). The majority of the AC grids is included in the AC system while the power electronic devices, such as the line commutation converter (LCC), are included in the corresponding DC system. The proposed network partitioning strategies lie in the following two aspects.

(1) Network partitioning between AC and DC grids

Usually, the frequency bands for dynamics of respective AC and DC grids differ a lot, DC and AC subsystems are suggested to adopt different time-steps. As a consequence, the network partitioning strategy is adopted to decouple the whole system into different subsystems. The specially designed interface model is proposed to represent high frequency interactions between different subsystems. Especially, the network partitioning strategies for the proposed method can be realized according to the following rules:

(1) In order to realize the proposed hybrid multi-domain transmission line model (HMD-TLM), the partitioning point can be chosen at the long transmission lines, which have large impedances and large latency for the traveling waves.

(2) Usually, the simulation errors of interface model are larger than errors inside each subsystem especially when the selected time-step is over 50 μs. In order to reduce the impact from errors of interface model onto the errors of other buses, it is better to choose the partitioning point at the bus with the minimum connected lines.

(3) Choose the partitioning point at the weak network coupling point. The network coupling can be evaluated by the power flow, the short circuit capacity, etc.

(2) Network partitioning inside the AC grids based on the MATE technique

In order to further improve the simulation efficiency of the AC system, it is separated into N individual subsystems. When analyzing the interactions between the AC and DC subsystems, the MATE technique is used where each AC subsystem is represented by a Thevenin equivalent source, accompanied by the Thevenin equivalent impedance. After the solution of these equivalent AC subsystems being calculated, the voltage and current of each subsystem can be updated by injecting the current source, where its value is equal to the interface current. The overall dynamic equations of N subsystems are written in the form of the MATE circuit:

![](images/9fc77e601ebdd85d3c21535560303593bbc53127d52df5b5b6544ee2be0a1037.jpg)  
Fig. 2. MATE-TLM interface model.

$$
\left[ \begin{array} { c c c c } { Y _ { 1 } } & & & { M _ { 1 } } \\ & { \ddots } & & { \vdots } \\ & & { Y _ { N } } & { M _ { N } } \\ { M _ { 1 } ^ { T } } & { \cdots } & { M _ { N } ^ { T } } & { Z _ { b } } \end{array} \right] \left[ \begin{array} { c } { \nu _ { 1 } ( t ) } \\ { \vdots } \\ { \nu _ { N } ( t ) } \\ { i _ { b } ( t ) } \end{array} \right] = \left[ \begin{array} { c } { i _ { h 1 } ( t - \Delta T ) } \\ { \vdots } \\ { i _ { h N } ( t - \Delta T ) } \\ { 0 } \end{array} \right]\tag{1}
$$

where $Y _ { 1 } , . . . Y _ { N }$ denote the conductance matrix of each subsystem; $\nu _ { 1 } ( t ) , . . . \nu _ { N } ( t )$ are the nodal voltages of each subsystem; $i _ { h 1 } ( t { - } \Delta T ) _ { i }$ , …, $i _ { h N } ( t - \Delta T )$ are their historic currents; $Z _ { b } ,$ ib(t) are the Thevenin impedance and currents of the interface branches. $M _ { i } , i = 1 , 2 . . . N$ is the correlation vector between the nodal voltage of ith subsystem and each interface branch. $M _ { i }$ is of the form like $[ 0 , . . . 1 . . . ] ^ { T } ,$ or $[ 0 , . . . - 1 . . . ] ^ { T } ,$ where integers 1 and −1 denoting the start and end node of the corresponding branch, respectively. It should be noted that the external currents are omitted in Eq. (1) to make the following derivations more concise. If the external currents are considered, it can be added on the right side of Eq. (1).

As shown in Fig. 2, the interactions between AC and DC subsystems are reflected by the proposed interface model, i.e., the MATE based transmission line model (MATE-TLM). When simulating the DC system under the time step Δt, the impact from the AC system is represented as a MATE circuit. Taken the MATE-TLM between subsystem 2 and the DC system as an example, parameters of its Thevenin equivalent circuit are derived as:

$$
e _ { t h k } ( t ) = M _ { 2 } ^ { T } [ Y _ { 2 } ] ^ { - 1 } i _ { h 2 } ( t - \Delta T ) , Z _ { t h k } = M _ { 2 } ^ { T } [ Y _ { 2 } ] ^ { - 1 } M _ { 2 }\tag{2}
$$

During the simulation period of [(k−1)ΔT, kΔT], the DC system should be simulated n times under the time-step $\Delta t ,$ where $n = \Delta T / \Delta t .$ The equivalent current at the DC system can be obtained as:

$$
I _ { n } ( t - \tau ) = - Z ^ { - 1 } \bar { u } _ { k } ( t - \tau ) - \bar { i } _ { k } ( t - \tau ) , t = ( k - 1 ) \Delta T + i \Delta t , i = 1 , 2 . . n\tag{3}
$$

where Z denotes the equivalent impedance of transmission line.

$\bar { u } _ { k } ( t - \tau ) , \bar { i } _ { k } ( t - \tau )$ are both obtained by linear interpolations:

$$
\begin{array}{c} \left\{ \bar { u } _ { k } ( t - \tau ) = L \{ \bar { u } _ { k } [ ( k - 1 ) \Delta T - \tau ] , \bar { u } _ { k } [ ( k - 2 ) \Delta T - \tau ] \}  \\ { \bar { i } _ { k } ( t - \tau ) = L \{ \bar { i } _ { k } [ ( k - 1 ) \Delta T - \tau ] , \bar { i } _ { k } [ ( k - 2 ) \Delta T - \tau ] \} } \end{array} \right.\tag{4}
$$

where L[.] denotes the linear interpolation operator.

On the other hand, the equivalent current at the AC system should be calculated by averaging:

$$
\bar { I } _ { k } ( t - \tau ) = - Z ^ { - 1 } \bar { u } _ { n } ( t - \tau ) - \bar { i } _ { n } ( t - \tau ) , t = k \Delta T\tag{5}
$$

where

$$
\begin{array} { c } { { \bar { u } _ { n } ( t - \tau ) = \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } u _ { n } [ ( k - 1 ) \Delta T + i \Delta t - \tau ] , t = k \Delta T } } \\ { { \bar { i } _ { n } ( t - \tau ) = \displaystyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } i _ { n } [ ( k - 1 ) \Delta T + i \Delta t - \tau ] , t = k \Delta T } } \end{array}\tag{6}
$$

## 2.2. Coordinated computational scheme

Fig. 3 illustrates the coordinated computational scheme of the proposed MATE based multi-rate co-simulations. After the power flow is initialized, the whole system is partitioned into the respective AC and DC systems, where the AC system will be further separated into N subsystems. The interfaces between the AC subsystems and DC system are modeled by MATE technique based on (1)–(2). Then, the DC system will be simulated with a unanimous smaller time step Δt, while the AC subsystems will be simulated with a much larger step ΔT. The rate ratio $n = \Delta T / \Delta t$ will be set according to the required simulation accuracy and numerical stability. Afterwards, different subsystems are simulated in a separated and coordinated way. During the simulation period of [(k−1)ΔT, kΔT], the DC system is simulated by a separated electromagnetic transient program and should be simulated n times under the time-step Δt. At the same time, the AC subsystems are simulated only once under the time-step ΔT. And then, interactions between AC and DC systems are reflected by the proposed MATE based interface models, where their parameters and electric circuits are updated and re-formed in a decoupled and coordinated way. Especially, the interface variables of the DC system are obtained by the averaging technique, while those of the AC systems are obtained by the linear interpolation technique. The interfaces between the DC and AC subsystems are updated based on (3)-(6). Finally, when the total simulation time $T _ { \mathrm { m a x } }$ is reached, the cosimulation comes to the end and output the updated results.

## 3. Improved control strategy for LCC based on the virtual resistance

Usually, the DC current or DC voltage will increase or decrease quickly after the AC faults, and the traditional voltage-dependent current order limit (VDCOL) fails to change the current order of the rectifier station, as quickly as expected. In order to improve the dynamic responses of the so-called VDCOL control strategy, the input signal of VDCOL $U _ { \mathrm { d c , o r d } }$ is modified by our proposed control strategy based on the concept of virtual impedance.

![](images/556de2737f6c3fbc5b629bf0231e033a2284224671bdee6a664e82d6a554d56a.jpg)  
Fig. 3. The calculation procedure of the proposed method.

![](images/522533fcb4322e390373c5c81ca15140c8c36643c14b7b9fce64360d612514ba.jpg)  
Fig. 4. Improved control strategy based on virtual resistance.

![](images/9ffca3344f0e577bb1dee1c34f7ae231ac28dfb70df6cd63e39e9be86bb9d266.jpg)  
Fig. 5. Diagram of the GYY HVDC Project in the China Southern Power Grid.

Table 1  
The system scale of the AC grids.
<table><tr><td>Area</td><td>Bus number</td><td>Generator number</td><td>Load number</td><td>Line number</td></tr><tr><td>AC grids</td><td>2412</td><td>599</td><td>1291</td><td>3537</td></tr></table>

When the AC fault occurs, the system will produce a significant DC voltage drop $\Delta U _ { d c } ( < 0 )$ and a overcurrent $\Delta I _ { d c } ( > 0 )$ . After multiplying factors $K _ { u }$ and Ri respectively, the modified voltage drop $\Delta U _ { d c , u }$ and the modified overcurrent $\Delta U _ { d c , i }$ are regarded as the additional control signals to improve dynamic responses of the VDCOL. In other words, the input signal of VDCOL $U _ { \mathrm { d c , o r d } }$ is determined by:

$$
U _ { \mathrm { d c \_ o r d } } = U _ { \mathrm { d \_ I N V } } + \Delta U _ { d c } ^ { \prime }\tag{7}
$$

$$
\Delta U _ { d c } ^ { \prime } = \Delta U _ { \mathrm { d c \_ i } } + \Delta U _ { \mathrm { d c \_ u } } = R _ { i } { \cdot } \Delta I _ { d c } + K _ { u } { \cdot } \Delta U _ { d c }\tag{8}
$$

where $\Delta U _ { \mathrm { d c } } , \Delta I _ { d c }$ denote variations of DC voltage and current; $R _ { i s }$ and $R _ { u }$ are parameters of virtual impedance. The corresponding output after the modified VDCOL or $I _ { o r d }$ is given as:

$$
I _ { o r d } = \left\{ \begin{array} { c l } { I _ { \mathrm { m a x } } , U _ { \mathrm { d \_ I N V } } + R _ { i } { \cdot } \Delta I _ { d c } + K _ { u } { \cdot } \Delta U _ { d c } \geqslant U _ { \mathrm { m a x } } } \\ { U _ { \mathrm { m i n } } + \frac { U _ { \mathrm { m a x } } - U _ { \mathrm { m i n } } } { I _ { \mathrm { m a x } } - I _ { \mathrm { m i n } } } ( U _ { \mathrm { d \_ I N V } } + R _ { i } { \cdot } \Delta I _ { d c } + K _ { u } ) , } \\ { U _ { \mathrm { m a x } } - U _ { \mathrm { d \_ I N V } } < R _ { i } { \cdot } \Delta I _ { d c } + K _ { u } { \cdot } \Delta U _ { d c } < U _ { \mathrm { m a x } } - U _ { \mathrm { d \_ I N V } } } \\ { I _ { \mathrm { m i n } } , U _ { \mathrm { d \_ I N V } } + R _ { i } { \cdot } \Delta I _ { d c } + K _ { u } { \cdot } \Delta U _ { d c } \leqslant U _ { \mathrm { m i n } } } \end{array} \right.\tag{9}
$$

During the steady state, $\Delta U _ { \mathrm { d c } } , \Delta I _ { d c }$ equal to zero. Accordingly, the proposed control strategy is the same as the traditional VDCOL. When a fault occurs, the proposed control strategy will make $U _ { \mathrm { d c , o r d } }$ smaller. As a consequence, the proposed control strategy can detect the variation of DC current/voltage earlier, and the current order can be decreased faster. This can help reduce the possibility of commutation failures and lower the fault current of each power electronic device. It should be noted that the modified input signal $U _ { d c , o r d }$ can make the control system react more rapidly, where the response speed is in accordance with the severity of the AC fault. Normally, when the AC fault is more severe, our proposed control strategy will react more quickly. When the DC current is decreased by the controller, or $\Delta I _ { d c } < 0 ,$ the proposed control strategy will increase the output signal $U _ { \mathrm { d c _ { \mathrm { - } } o r d } } ,$ avoiding a significant drop of transmitted power.

The overall implementation of the control strategy is depicted in Fig. 4. Based on the concept of virtual impedance, the VDCOL can modify the current order accurately and quickly, reducing the possibility of CFs and improving the fault recovery characteristics.

## 4. Simulation results

To validate the accuracy and efficiency of the proposed multi-rate co-simulation method as well as to show the effectiveness of the advanced virtual resistance based control strategy, simulations are carried out on a practical LCC based HVDC system in the China Southern Power Grid (see Fig. 5). The parameters of the 12-pulse two terminal HVDC are given as follows: the rated DC voltage and current are 500 kV/3kA and the length of the DC cable is 577 km. The system scale of large-scale AC grids is detailed in Table 1. According to Section 2, the whole system is separated into the AC and DC subsystems, where the interface model is represented by the MATE-TLM. When applying the multi-rate co-simulation method based on the improved control strategy, the timesteps of the AC subsystem are ΔT = 500 µs, 100 µs, and 50 µs, respectively, and those of the DC subsystem are set as $\Delta t = 5 0$ µs. Here, the reference curve is produced by the high-fidelity model on PSCAD/ EMTDC under a very small time step of 50 μs. The duration of the simulation is 5 s in total.

4.1. Accuracy and efficiency comparisons during the three-phase and singlephase AC fault at the inverter station

In the first scenario, a temporary three-phase-to-ground fault at the inverter station is trigged at $t = 2 . 1 s$ , and lasts for 0.11 s. The second scenario includes an single-phase fault at the inverter station which is trigged at t = 2.1 s and clears at $t = 2 . 2 1 s$ . Simulation results in Figs. 6 and 7 have demonstrated even when the time-step of AC subsystem is extended to $5 0 0 \mu \mathrm { s } ,$ the proposed method can still satisfy the accuracy expectations during the three-phase-to-ground fault and the singlephase-to-ground fault, respectively. The average simulation error is quantitively evaluated as:

$$
E _ { \mathrm { a v g } } = \frac { 1 } { N } \sum _ { i = 1 } ^ { N } | x _ { i , m } - x _ { i , u } |\tag{10}
$$

where $x _ { i , m } , x _ { i , u }$ are the ith sample obtained by the multi-rate simulation and the reference curve, respectively; N is the number of the samples.

Table 2 has shown that when the time-step is extended to 500 μs, it has achieved a speedup of 150 times. The reference case (rate ratio $n = 1 )$ is referred to the simulation result produced by the high-fidelity model on PSCAD/EMTDC under a very small time-step of $5 0 \mu \mathbf { s } .$ The dimension of the conductance matrix when $n = 1$ is so huge including all the node buses of large-scale AC grids and all the node buses of the LCC. For instance, if the node number of AC grids and DC grids is 2412 and 250 respectively, the total dimension of the overall conductance matrix will be 2662\*3 = 7896.

![](images/718c64ba7b69fe77f2b4edc49edd239f6d217df982d98ceddce0d5a365c943ed.jpg)

On the contrary, when n = 2, the whole system is simulated by the proposed multi-rate co-simulation method in a decoupled and independent way as two independent and much smaller conductance matrixes. That is to say, the AC grids and DC grids will be simulated independently. The interactions between AC and DC grids will be reflected by the proposed interface model. The simulation efficiency of the AC grids will be further improved by the MATE technique. That is the reason why the results when n = 2 is much more efficient than the reference curve.

![](images/a6bb22e598f330e3fe8c261c606eae4bca15640da081daf4332d5dc472a227fd.jpg)

![](images/a59d50ca8e99be0b036e4f9d50b62d564a20a7fce433a011348a81e3f5e4ab2a.jpg)

![](images/63712c042ae17a1afd19f1f2760e470060639c6e43f32166f4d5831c8e7c3742.jpg)

![](images/3ff4b4d8fdab0eb9f502f98df992724ff65f197cdebf409cb8a1cec774b373c7.jpg)

![](images/771ddde01250f0096530dd357b2c45e7024b8fca627f07ebe714ea31a5f6d9ff.jpg)  
Fig. 6. (a) Gamma angles, (b) DC voltages and (c) DC currents under different rate ratios during the three-phase-to-ground fault.

![](images/749a883355fc13d0ab9e2e9bc05d5d1230d2dbdf0561e2d4c429b33e59daff92.jpg)

![](images/941cdc268b15abd6067c7cce1ebe68d6a8685f117e8bd359a51a39503873314e.jpg)

![](images/897a4165feb793cea89b7f174d0d12841b60bca97020095f6daf783e3ebbc250.jpg)

![](images/fc278a5c217147614292957b68596b480a976760271b2f1003034697711214cb.jpg)

![](images/0bc7c915a3d86b469e0c11b4f7e0d10313da4f196deabadb71ba271682f246f3.jpg)  
Fig. 7. (a) Gamma angles, (b) DC voltages and (c) DC currents under different rate ratios during the single-phase-to-ground fault.

Table 2  
Comparison of CPU time and average simulation errors with different rate ratios (three-phase-to ground fault).
<table><tr><td>Rate ratio n</td><td></td><td colspan="2">CPU time/sInterface variables</td><td>DC subsystem variables</td></tr><tr><td></td><td></td><td> $U _ { \mathrm { R e c } }$ </td><td> $U _ { \mathrm { I n v } }$ </td><td> $U _ { d c }$ </td></tr><tr><td>1(the reference curve)</td><td>7200</td><td>/</td><td>/</td><td>/</td></tr><tr><td>2</td><td>90.734</td><td>0.0015</td><td>0.0013</td><td>0.0016</td></tr><tr><td>10</td><td>49.453</td><td>0.0092</td><td>0.0116</td><td>0.0116</td></tr></table>

Comparison of CPU time and average simulation errors with different rate ratios (single-phase-to ground fault).
<table><tr><td>Rate ratio n</td><td></td><td colspan="2">CPU time/sInterface variables</td><td>DC subsystem variables</td></tr><tr><td></td><td></td><td> $U _ { \mathrm { R e c } }$ </td><td> $U _ { \mathrm { I n v } }$ </td><td> $U _ { d c }$ </td></tr><tr><td>1(the reference curve)</td><td>7150</td><td>/</td><td>/</td><td>/</td></tr><tr><td>2</td><td>60.954</td><td>0.0014</td><td>0.0015</td><td>0.0016</td></tr><tr><td>10</td><td>44.703</td><td>0.0084</td><td>0.0112</td><td>0.0109</td></tr></table>

![](images/4e50c1d4b4f7abc5b1fcd04907fc5b4e297f3533fd57b9980d75bac6e26dac99.jpg)

As can be seen in Table 3, during the three-phase-to-ground fault, with the large time-step $\Delta T = 5 0 0 \mu s ,$ the simulation speed is improved by 160 times. Therefore, the proposed method has improved the efficiency significantly while guaranteeing the satisfied accuracy. It should be noted that the efficiency of the single-phase fault scenario is a little bit more efficient than that of the three-phase fault scenario. This is because for the three-phase fault, three elements of the conductance matrix will be changed. On the contrary, for the single-phase fault, only one elements of the conductance matrix will be changed.

Both scenarios are simulated to show the advantage of the improved control strategy as well. As demonstrated in Fig. 8, during the singlephase fault, the voltage drop and overcurrent of the proposed control strategy are improved by 14.03% and 3.45% respectively. As shown in Figs. 8(c) and 9, with the proposed control strategy, the extinction angle will be increased after clearance of the fault and exit the commutation failure earlier than the traditional control strategy, reducing the number of commutation failure. Specifically, the traditional control strategy will induce the continuous commutation failure of VT3 and VT6, while the proposed control strategy will have the commutation failure for only once at VT3 and ${ \mathrm { V T } } 6 ,$ which evaluates the effectiveness of the proposed control strategy. Also, during the three-phase fault, it is shown in Fig. 10 that the proposed control strategy improves the voltage drop and overcurrent by 2.55% and 6.55% respectively. Figs. 10(c)

![](images/5bacab68819a1dfa0e7b0358f8325c5f3abde95d25c4458af713b9a0c860e66b.jpg)

![](images/895b45e12cd7e558626c7ae24c330ace2143a5f9b516322fd6382bd4e058d635.jpg)

![](images/fc91fa961b4697feafe2ff2043e063693e57e569c2aebbf0b1a3dd57dba15b76.jpg)  
Fig. 8. Simulation results during the single-phase fault scenario.

![](images/680fd7333084262d8db2b900777c31fcb072f8be78392aed318c3cd3be5394a0.jpg)

![](images/1466cc4ebe9f5d9b19bc1012cea3742a8c13537a46fa20991c8c6e3df9d5cb49.jpg)

![](images/045cb1577c14508ccdfc4a461477dab6b35241b135864263b20f730a758fa57e.jpg)  
Fig. 9. Valve currents during the single-phase fault scenario.

![](images/5f36f024d9a816f00a1f5882dd49ab7c7808b386eb36f20ac8b56254a3e602cd.jpg)

![](images/84906bd7a077ae1ee0121923154ca5e58a1e9f99c635ddfb6bdcbb2c3eccfcd6.jpg)

![](images/1f843230d2925f199df65d28770d6fe3113c37ab743e26add12c8fb3c5b09101.jpg)

![](images/689ef055562b22239195a17bed8ed6d4181ebb578e7c4761ac4f55d6bf344a74.jpg)

![](images/129937bc9840dbccd5b2843ed9e7be9182b01cd0374adbe101740bdaead39751.jpg)

Fig. 10. Simulation results during the three-phase fault scenario.  
![](images/f5ea9ef3b35b3e1947d58999b75a0a0717ec6a642477bf057101e9d28532e912.jpg)

![](images/8da764afe5f2c60741ddad928501785db2dd4e58f0db001c50aa4383f54ddc1b.jpg)

![](images/5058bbf6bf997d4a31aa83b0fbbf263228ef13246dce3e5033e7574de94802a3.jpg)

![](images/309227d344dda33171d77387d929f47609d8825f4e51b7f539083fb27b839b75.jpg)  
Fig. 11. Valve currents during the three-phase fault scenario.

![](images/6ba490b95d9998fac9856860ce5ae67338d2b56eadec7ec8f11b2bd6a33f90f9.jpg)  
Fig. 12. The comparisons between the proposed method and other traditional methods.

and 11 demonstrate that the proposed control strategy can also accelerate the recovery speed after clearance of the three-phase fault.

## 4.2. Accuracy comparisons of different control strategy of the LCC

In order to show the effectiveness of proposed simulation method in accuracy, the proposed control strategy is further compared with the traditional HVDC control strategy [23,24] and the commutation failure (CF) prediction control strategy [14] by using the proposed method under the time-step of 500us, which is shown in Fig. 12. Here, ‘traditional (multi-rate $\Delta \mathrm { T } = 5 0 0 \mathrm { u } s ) ^ { \th }$ ’ denote the simulation results of traditional HVDC control strategy by using the proposed multi-rate co-simulation method (the time-step ΔT = 500us); ‘PSCAD’ denote the reference curve of difference control strategies.

As can be seen, the simulation results by the proposed MATE based multi-rate co-simulation method match the PSCAD derived reference curve exactly under different control strategies. Moreover, both the proposed method and the commutation failure prediction method can reduce the number of CFs. The CF prediction method will increase the extinction angle in advance to reduce CFs. However, as shown in Fig. 12(b), the consumed reactive power of CF prediction method will increase unexpectedly.

## 5. Conclusions

In this paper, a novel improved control strategy based on the concept of virtual impedance is proposed to reduce the probability of the CFs and to increase the recovery speed of DC system. The advantages of the proposed control strategies are well validated by the proposed multi-rate co-simulation method. The accuracy of the proposed method is guaranteed by the proposed MATE based transmission line model (MATE-TLM) and the efficiency is significantly improved by both the MATE technique and multi-rate co-simulations. The proposed method firstly decouples the whole system as AC and DC systems and then partitions the AC system into several subsystems in the form of the MATE circuits. The interactions between AC and DC subsystems are reflected by the proposed interface model, i.e., the MATE-TLM. During co-simulation, the time latency between fast and slow subnetworks is resolved by linear interpolations on the AC side and averaging on the DC side.

In the case study, a practical large-scale AC/DC systems is simulated to show the effectiveness of the improved control strategy and the proposed multi-rate co-simulation method. Simulation results have demonstrated even when the time-step of AC subsystem is extended to 500 μs, the proposed method can still satisfy the accuracy expectations. During the three-phase fault scenario, when the time-step is extended to 500 μs, it has achieved a speedup of 150 times. Also, during the singlephase fault, with the large time-step $\Delta T = 5 0 0 \mu s$ , the simulation speed is improved by 160 times. Therefore, the proposed method has improved the efficiency significantly while guaranteeing the satisfied accuracy. Moreover, with the proposed control strategy, the extinction angle will be increased after clearance of the fault and exit the commutation failure earlier than the traditional control strategy, reducing the number of commutation failure. Specifically, during the single-phase fault scenario, the traditional control strategy will induce the continuous commutation failure of VT3 and VT6, while the proposed control strategy will have the commutation failure for only once at VT3 and VT6, which evaluates the effectiveness of the proposed control strategy.

## Declaration of Competing Interest

We declare that we have no financial and personal relationships with other people or organizations that can inappropriately influence our work, there is no professional or other personal interest of any nature or kind in any product, service and/or company that could be construed as influencing the position presented in, or the review of, the manuscript entitled, “A Multi-Area Thevenin Equivalent Based Multi-rate Co-simulation for Control Design of Practical LCC HVDC System”.

## Acknowledgment

This work is partly supported by Science and Technology Project of State Grid (shanghai municipal electric power company) 52097018000D, open fund of FXB51201901051 (CEPRI), SJTU Global Strategic Partnership Fund (2019 SJTU-KTH), Shanghai Sailing Program 19YF1423500.

## Appendix A. Supplementary material

Supplementary data to this article can be found online at https:// doi.org/10.1016/j.ijepes.2019.105479.

## References

[1] Mirsaeidi S, Dong X, Tzelepis D, Said DM, Dysko A, Booth C. A predictive control strategy for mitigation of commutation failure in LCC-based HVDC systems. IEEE Trans Power Electron 2018;34:160–72. https://doi.org/10.1109/TPEL.2018. 2820152.

[2] Shu D, Jiang Q, Zhang C, Liu Z, Li C. Improved current order control strategy for effective mitigation of commutation failure in HVDC system. IEEE Power Energy Soc Gen Meet 2018. https://doi.org/10.1109/PESGM.2017.8274381.

[3] Xue Y, Zhang XP, Yang C. Elimination of commutation failures of LCC HVDC system with controllable capacitors. IEEE Trans Power Syst 2016;31:3289–99. https://doi. org/10.1109/tpwrs.2015.2491784.

[4] Zeng R, Xu L, Yao L, Finney SJ, Wang Y. Hybrid HVDC for integrating wind farms with special consideration on commutation failure. IEEE Trans Power Deliv 2016;31:789–97. https://doi.org/10.1109/tpwrd.2015.2440354.

[5] Wang L, Thi MSN. Stability enhancement of large-scale integration of wind, solar, and marine-current power generation fed to an sg-based power system through an lcc-hvdc link. IEEE Trans Sustain Energy 2014;5:160–70. https://doi.org/10.1109/ tste.2013.2275939.

[6] Adapa R. High-wire act: HVdc technology: The state of the art. IEEE Power Energy Mag 2012;10:18–29.

[7] Guo C, Liu Y, Zhao C, Wei X, Xu W. Power component fault detection method and improved current order limiter control for commutation failure mitigation in HVDC. IEEE Trans Power Deliv 2015;30:1585–93. https://doi.org/10.1109/tpwrd.2015. 2411997.

[8] Rahimi E, Gole AM, Davies JB, Fernando IT, Kent KL. Commutation failure analysis in multi-infeed HVDC systems. IEEE Trans Power Deliv 2011;26:378–84. https:// doi.org/10.1109/tpwrd.2011.6612526.

[9] Aik DLH, Andersson G. Analysis of voltage and power interactions in multi-infeed HVDC systems. IEEE Trans Power Deliv 2013;28:816–24. https://doi.org/10.1109/ tpwrd.2012.2227510.

[10] Shao Y, Tang Y. Fast evaluation of commutation failure risk in multi-infeed HVDC systems. IEEE Trans Power Syst 2017;33:646–53. https://doi.org/10.1109/tpwrs. 2017.2700045.

[11] Sun YZ, Peng L, Ma F, Li GJ, Lv PF. Design a fuzzy controller to minimize the effect of HVDC commutation failure on power system. IEEE Trans Power Syst 2008;23:100–7. https://doi.org/10.1109/tpwrs.2007.913212.

[12] Bauman J, Kazerani M. Commutation failure reduction in HVDC systems 2007;22:1995–2002.

[13] Ramesh M, Laxmi AJ. Fault identification in HVDC using artificial intelligence - Recent trends and perspective. In: 2012 int conf power, signals, control comput EPSCICON 2012 2012:1–6, doi: 10.1109/EPSCICON.2012.6175256.

[14] Zhang Lidong, Dofnas Lars. A novel method to mitigate commutation failures in HVDC systems. In: Proceedings PowerCon 2002. International conference on, 2002. p. 51–6, doi: 10.1109/icpst.2002.1053503.

[15] Shu D, Xie X, Jiang Q, Guo G, Wang K. A multirate EMT co-simulation of large AC and MMC-based MTDC systems. IEEE Trans Power Syst 2018;33:1252–63. https:// doi.org/10.1109/tpwrs.2017.2734690.

[16] Wang Z, Wang C, Li P, Fu X, Wu J. Extendable multirate real-time simulation of active distribution networks based on field programmable gate arrays. Appl Energy 2018;228:2422–36. https://doi.org/10.1016/j.apenergy.2018.07.099.

[17] Lauss G, Strunz K. Multirate partitioning interface for enhanced stability of power hardware-in-the-loop real-time simulation. IEEE Trans Ind Electron 2019;66:595–605. https://doi.org/10.1109/tie.2018.2826482.

[18] Müller SC, Georg H, Nutaro JJ, Widl E, Deng Y, Palensky P, et al. Interfacing power system and ICT simulators: Challenges, state-of-the-art, and case studies. IEEE Trans Smart Grid 2018;9:14–24. https://doi.org/10.1109/tsg.2016.2542824.

[19] Ren W, Steurer M, Baldwin TL. Improve the stability and the accuracy of power hardware-in-the-loop simulation by selecting appropriate interface algorithms. IEEE Trans Ind Appl 2008;44:1286–94. https://doi.org/10.1109/icps.2007. 4292112.

[20] Benigni A, Monti A, Dougal RA. Latency-based approach to the simulation of large power electronics systems. IEEE Trans Power Electron 2014;29:3201–13. https:// doi.org/10.1109/tpel.2013.2274175.

[21] Hui SYR, Fung KK, Christopoulos C. Decoupled simulation of DC-linked power electronic systems using transmission-line links. IEEE Trans Power Electron 1994;9:85–91. https://doi.org/10.1109/63.285497.

[22] Moreira FA, Martí JR, Zanetta LC, Linares LR. Multirate simulations with simultaneous-solution using direct integration methods in a partitioned network environment. IEEE Trans Circuits Syst I Regul Pap 2006;53:2765–78. https://doi.org/10. 1109/tcsi.2006.882821.

[23] Shu D, Xie X, Dinavahi V, et al. Dynamic phasor based interface model for EMT and transient stability hybrid simulations. IEEE Trans Power Syst 2018;33:3930–40. https://doi.org/10.1109/tpwrs.2017.2766269.

[24] Daryabak M, Filizadeh S, et al. Modeling of LCC-HVDC systems using dynamic phasors. IEEE Trans Power Del 2014;29:1989–98. https://doi.org/10.1109/pesgm. 2015.7285683.