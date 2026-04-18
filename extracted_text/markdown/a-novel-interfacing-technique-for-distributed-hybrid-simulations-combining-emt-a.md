# A Novel Interfacing Technique for Distributed Hybrid Simulations Combining EMT and Transient Stability Models

Dewu Shu, Student Member, IEEE, Xiaorong Xie, Senior Member, IEEE, Qirong Jiang, Member, IEEE, Qiuhua Huang, Chunpeng Zhang

Abstract—The steady increase of power electronic devices and nonlinear dynamic loads in large scale AC/DC systems desperately requires an efficient simulation method. However, the traditional hybrid simulation, which incorporates various components into a single EMT subsystem, causes great difficulty in network partitioning and significant deterioration in simulation efficiency. To resolve these issues, a distributed hybrid simulation method is proposed in this paper. The key factor leading the success of this method is a distinct interfacing technique, which includes: i) a new approach based on the twolevel Schur complement to update the interfaces by taking full consideration of the couplings between different EMT subsystems; and ii) a combined interaction protocol to further improve the efficiency while guaranteeing the simulation accuracy. The improved performances of the proposed method in terms of efficiency and accuracy have been verified by the simulation studies on the modified IEEE 39 system as well as a practical AC/DC system, both of which consist of a two-terminal VSC-HVDC and nonlinear dynamic loads.

Index Terms—Distributed hybrid simulation, electromagnet transient, two-level Schur complement, VSC-HVDC.

## I. INTRODUCTION

A T present, many converter-based power electronic de-vices are connected to the AC grids, and have greatly vices are connected to the AC grids,and have greatly changed the dynamic characteristics of the whole power systems [1]-[4]. In order to accurately and efficiently analyze the interactions between these power electronic devices and the AC grids, as well as to acquire the overall dynamics of the power systems, the hybrid simulation combining electromagnetic transient (EMT) and transient stability (TS) simulations is widely used [5]-[6]. In doing so, a procedure named network partitioning is carried out to partition the whole system into a Central-TS subsystem and multiple EMT subsystems. Notably, the EMT subsystems incorporate power electronic devices and nonlinear dynamic loads, thereby the electromagnetic transients are required to be represented in details [7]. In contrast, the Central-TS subsystem predominantly contains the AC grids, for which the electromechanical transients are of much more concern. Such different focuses on system dynamics drive the Central-TS and EMT subsystems to be simulated with separate TS and EMT programs. In this way, the interactions among subsystems are conveyed through the interface models so that the overall dynamics of the power system could be analyzed.

In previous studies of the hybrid simulation, the scale of the EMT subsystem is usually small, thus all power electronic devices and nonlinear dynamic loads can be included in a single EMT subsystem [5]-[9]. However, as their numbers increase rapidly in modern power systems, the EMT subsystem needs to be expanded substantially in order to contain all of them. Consequently, network partitioning becomes very difficult. Inappropriate selection of partitioning location would cause numerical instability problems [2]. Moreover, the overall simulation efficiency and accuracy could be deteriorated significantly.

To address the above challenges, the concept of distributed hybrid simulation has been proposed [10]. In light of this concept, the power electronic devices and nonlinear dynamic loads are arranged into different EMT subsystems. Each subsystem is simulated with its own EMT program, while the remaining AC grids are placed in the Central-TS subsystem and simulated with the TS program. The simulation program corresponding to each subsystem can be deployed in one or several computers and executed in a parallel and coordinated way. The variables and parameters of interface models between different subsystems are updated and then transferred through a certain communication protocol (e.g., TCP/UDP socket server[11]) in local area networks (LAN). The key to realize the distributed hybrid simulation is the interfacing technique, which includes three core issues, namely, TS/EMT models, interface models their update strategy, and the interaction protocol [2], [10]. As for the TS model, either positive-sequence [5], [9], [12] or three-sequence [13]-[15] equivalent models are used. It worth noting that the positive sequence model cannot reflect the three-phase unbalance of the interfaces in the case of asymmetric faults and thus would cause significant simulation errors. In order to maintain the assumption of the three-phase balance, some previous work extended the interface buses far into the AC grids[13]. However in doing so, the simulation accuracy cannot be satisfied and the simulation efficiency would be severely reduced. When the EMT model is concerned, the state-space approach is widely used [14]. Nevertheless, the problem is that the size/scale of the electromagnetic system would be limited due to the high modelling complexity of the power electronics involved network. Recently, a frequency dependent network equivalent (FDNE) model is developed to improve the accuracy of interfaces in the EMT subsystems without expanding the scale of the EMT subsystem [16]. However, its drawback lies in the low computational efficiency. This model would also arouse spurious transients during a switching operation in a new FDNE, which in turn affect the accuracy of interfaces dramatically [17]. As for the issue of updating interface models, the cases of a single EMT subsystem were extensively discussed [5]-[9]. Only reference [13], [18] explored the strategy of updating the interface models for multiple EMT subsystems by the hybrid simulation. Yet, the interactions among different EMT subsystems were not taken into consideration. The errors caused by interaction protocols, especially the serial and parallel ones, were analyzed in [5], [6]. But, there was a lack of an efficient interaction protocol for distributed hybrid simulation, which was actually the important foundation for achieving the high precision and efficiency of simulation.

In this paper, a distributed hybrid simulation method is proposed to analyze large-scale AC/DC systems, which contain power electronic devices and nonlinear dynamic loads. The contribution lies in the development of a new interfacing technique, which has the following important features:

i) The interfaces with the EMT subsystems are modelled as three-phase Thevenin equivalents, while those with the Central-TS subsystem are modelled as three-sequence Norton equivalents. Consequently, the mandatory assumption of threephase balance for the interfaces can be circumvented and the difficulty for network partitioning is dramatically reduced.

ii) A new strategy of updating interface model is developed based on the two-level Schur complement, through which the obtained Thevenin equivalents for each EMT subsystem could fully consider the couplings among different EMT subsystems. Thus, the proposed hybrid simulation method produces the more accurate results than the traditional one.

iii) In the implementation of the hybrid simulation method, a combined interaction protocol is utilized to further improve the efficiency and accuracy of simulation.

The rest of the paper is organized as follows: Section II outlines the proposed method of distributed hybrid simulation, including the framework, the interfaces with TS and EMT subsystems, and the general simulation procedures. Section III details the update strategy for interface models and conducts comparative studies with the traditional method. Section IV verifies the effectiveness of the proposed method on the modified IEEE 39 system as well as a practical AC/DC system. Finally, conclusions are drawn in Section V.

## II. DISTRIBUTED HYBRID SIMULATION

## A. Framework of Distributed Hybrid Simulation

As shown in Fig. 1(a), the AC/DC hybrid system containing power electronic devices and nonlinear dynamic loads are partitioned into a Central-TS subsystem and several EMT subsystems (1, 2...N). The PCCs (point of common couplings) of the power electronic devices and nonlinear dynamic loads are selected as the position for network partitioning. Once partitioned, different Central-TS and EMT subsystems are simulated separately in one or several computers. In addition, the interactions among these subsystems are realized by the interfacing technique, including interface models, their update strategy, and the interaction protocol. The three-sequence models in the Central-TS subsystem are derived by the differential algebraic equations of all the dynamic elements in the fundamental-frequency steady-state phasor form. Meanwhile, the models of each EMT subsystem are derived by the nodal analysis method in the three-phase instantaneous waveform [19]. For each subsystem, the impact of other subsystems is represented by the corresponding interface model, which is shown in Fig. 1 (b). Therein, the interface model with each EMT subsystem is represented by three-phase Thevenin equivalents, while that with the Central-TS subsystem is represented by three-sequence Norton equivalents. The parameters of the interface models are updated by the proposed strategy. The interaction protocol determines the simulation sequence of each subsystem and the moment to exchange parameters among them.

![](images/a9a26c88f92e54664f91edab4b24a7fb637ce96bd980c8059fe0cc1adf5325fb.jpg)  
Fig. 1. (a) Framework of distributed hybrid simulation. (b) Interface model between different subsystems.

The main differences between our proposed hybrid simulation method and the traditional one lie in the interaction protocol and the update strategy for interface models, which are also the focuses of this paper. The interface models for the Central-TS and EMT subsystems will be discussed in the following subsections. The general simulation procedure, as well as the combined interaction protocol, is given in Section II-D. Then the new strategy to update interface models will be elaborated in Section III.

B. Interface models with the EMT Subsystem: Three-phase Thevenin Equivalents

As shown in Fig. 1(b), the interface model with the $j ^ { t h }$ EMT subsystem is represented by its three-phase Thevenin equivalents, i.e., Thevenin voltage $\tilde { v } _ { j } ^ { a b c }$ and Thevenin impedance $\tilde { Z } _ { j } ^ { a b c }$ [12]. First, Thevenin impedance of the $j ^ { t } h$ interface is given by

$$
\tilde { Z } _ { j } ^ { a b c } = \tilde { R } _ { e , j } ^ { a b c } + j \omega \tilde { L } _ { e , j } ^ { a b c } ,\tag{1}
$$

where $\tilde { R } _ { e , j } ^ { a b c } , \tilde { L } _ { e , j } ^ { a b c }$ are the three-phase resistance and inductance matrices of the $j ^ { t h }$ interface. Generally, most components in the Central-TS subsystem are inductive, such as synchronous machines and transmission lines, etc. So the resistive and inductive impedances are taken as examples [6], [12]. Here, Thevenin impedance can be calculated at the start of the simulation, and it is not necessary to refresh unless there is a topological change in the Central-TS subsystem.

Second, the interface voltages and currents are calculated in the Central-TS subsystem, and then transformed from the three-sequence domain into the three-phase domain, i.e. $V _ { e , j } ^ { a b c } , I _ { e , j } ^ { a b c }$ [13]. At this point, the phasor values of Thevenin voltages are calculated as

$$
\tilde { V } _ { j } ^ { a b c } = V _ { e , j } ^ { a b c } + \tilde { Z } _ { j } ^ { a b c } I _ { e , j } ^ { a b c } ,\tag{2}
$$

Then the instantaneous value of Thevenin voltage is given by

$$
\tilde { \nu } _ { j } ^ { l } = \tilde { V } _ { j } ^ { l } c o s ( \delta + \tilde { \theta } _ { j } ^ { l } ) , l = a , b , c\tag{3}
$$

where $\tilde { V } _ { j } ^ { l } , ~ \tilde { \theta } _ { j } ^ { l } , ~ l = a , b , c$ are the magnitude and angle of Thevenin voltage of each phase; $\begin{array} { r } { \delta = \int _ { 0 } ^ { t } \omega d t } \end{array}$

Similarly, the instantaneous values of the interface voltage and current, $\mathrm { i } . \mathrm { e } . , v _ { e , j } ^ { a b c } , i _ { e , j } ^ { a b c }$ can be derived.

Finally, the different equation of the interface model of the jth EMT subsystem is written into

$$
\frac { d } { d t } i _ { e , j } ^ { a b c } = \left[ \tilde { L } _ { e , j } ^ { a b c } \right] ^ { - 1 } ( v _ { e , j } ^ { a b c } - \tilde { R } _ { e , j } ^ { a b c } i _ { e , j } ^ { a b c } - \tilde { v } _ { j } ^ { a b c } ) ,\tag{4}
$$

Here, an implicit trapezoidal algorithm is used for the discretization of the differential equations for the EMT subsystems and their interfaces. Thus the simulation of the EMT subsystems are fulfilled using the nodal analysis method [19].

C. Interface model with the Central-TS Subsystem: Threesequence Norton Equivalents

In order to reflect unbalanced dynamics following any asymmetric disturbances, in the Central-TS subsystem, the adjacent $j ^ { t h }$ EMT subsystem is represented by its threesequence Norton equivalents, i.e. Norton current sources $I _ { j } ^ { 1 2 0 }$ and equivalent admittances $\mathbf { \Delta } \mathbf { Y } _ { j } ^ { 1 2 0 }$ (see Fig. 1(b)).

First, the interface voltages and currents in the phasor form are calculated in the neighbouring EMT subsystems. Explicitly, the values of the interface voltages and currents are calculated by either Fourier or curve-fitting method [6]. These values are further transformed into the three-sequence domain as $V _ { t , j } ^ { 1 2 0 } , I _ { t , j } ^ { 1 2 0 }$ [13]. Thus Norton currents are derived by

$$
I _ { j } ^ { 1 2 0 } = I _ { t , j } ^ { 1 2 0 } + Y _ { j } ^ { 1 2 0 } V _ { t , j } ^ { 1 2 0 } ,\tag{5}
$$

Similarly, Norton admittances $\mathbf { \Delta } _ { J _ { j } ^ { 1 2 0 } }$ can be obtained from the admittance matrices of each EMT subsystem, or

$$
Y _ { j } ^ { 1 2 0 } = \left[ R _ { t , j } ^ { 1 2 0 } + j \omega L _ { t , j } ^ { 1 2 0 } \right] ^ { - 1 } ,\tag{6}
$$

where $R _ { t , j } ^ { 1 2 0 } , ~ L _ { t , j } ^ { 1 2 0 }$ are the corresponding three-sequence resistance and inductance matrices of the interfaces between the $j ^ { t h }$ EMT subsystem and the Central-TS subsystem.

D. General Simulation Procedures based on Combined Interaction Protocol

For distributed hybrid simulations, the computational scheme plays a crucial role in improving simulation efficiency as well as in guaranteeing simulation accuracy. Here, the overall computational scheme of our proposed method, as illustrated in Fig. 2, has the following steps.

First, the target system is initialized based on the power flow calculations.

Second, the whole system is partitioned into one Central-TS and several EMT subsystems.

Third, all EMT subsystems are simulated using an identical step $h ,$ which is sufficiently small in most cases(e.g., 10- 100µs) to ensure the accuracy of simulation; while the Central-TS subsystem is simulated with a much larger step $h _ { t s } .$ The rate ratio, defined as $n = h _ { t s } / h .$ , is properly selected for each subsystem according to the requirements for simulation accuracy and numerical stability [20], [21].

Next step, the simulations of different subsystems are separately executed but closely governed by the interaction protocol, which determines the simulation sequence of all subsystems and the moment to exchange parameters among them. Typical interaction protocols include the serial protocol and the parallel protocol [10]. Generally, the serial protocol has the higher simulation accuracy than the parallel protocol. However, a higher accuracy would result in a poorer simulation efficiency, making the serial protocol not always satisfied. Given this, in our proposed method, the advantages of the two protocols are combined with a specially designed mechanism. As shown in Fig. 2, before an interactive iteration, the change rate of current in all EMT subsystem interfaces at the moment $t _ { k }$ is calculated as follows:

$$
\Delta ( t _ { k } ) = \operatorname* { m a x } _ { j , l } \left\{ \frac { \left\| I _ { e , j } ^ { l } ( t _ { k } ) - I _ { e , j } ^ { l } ( t _ { k - 1 } \right\| } { \left\| I _ { e , j } ^ { l } ( t _ { k - 1 } \right\| } \right)  , l = a , b , c ; j = 1 , 2 , . . . N\tag{7}
$$

where $I _ { e , j } ^ { l } ( t _ { k } )$ is the $j ^ { t h }$ interface currents of EMT subsystems of phase $l ( l = a , b , c )$ at time $t _ { k } ; ~ l$ denotes each phase and j denotes the index of interfaces.

$\Delta ( t _ { k } )$ and a given threshold ε determine which protocol to be used. Specifically, if $\Delta \left( t _ { k } \right) > \varepsilon ,$ , the serial protocol is executed. In doing so, the interface parameters are first transferred from the Central-TS subsystem to each EMT subsystem. After updating their Thevenin equivalents, EMT subsystems are then simulated in parallel for n times to fulfil the simulations within a whole step $h _ { t s }$ . Next, after the interface parameters of the Central-TS subsystem refreshed with the interface variables of EMT subsystems, the Central-TS subsystem is simulated for the same step $h _ { t s }$ . The time consumed for this one-step simulation is made up of three parts: the time spent by the EMT subsystems, the Central-TS subsystem and the protocol interaction. Among them, the EMT simulations consume the longest time. Otherwise, if $\Delta ( t _ { k } ) < \varepsilon$ , the parallel protocol will be used, so that the Central-TS and EMT subsystems are simulated in a paralleled manner. At the moment that a whole simulation step is completed, the interface parameters of all subsystems are updated and exchanged simultaneously. As a result, the simulation time would be considerably reduced. The recommend threshold ε is 2%-10% step change per interaction step [13].

To put it simply, when the system is in the steady state, i.e., the change rate of current is relatively small, the more efficient parallel protocol would be applied. In contrast, if the system, especially the interface, experiences transient process, system is switched to the more accurate serial protocol. Thus, a good balance is achieved between the accuracy and efficiency. Finally, when the total simulation time $( T _ { m a x } )$ is reached, the entire simulation comes to an end and the results are output.

## III. PROPOSED UPDATE STRATEGY FOR INTERFACE PARAMETERS

In each interactive iteration shown in Fig. 2, the parameters of interface are required to be updated. During this procedure, the update scheme is paramount to guarantee the accuracy of the distributed hybrid simulation. In general, since the requirement for the simulation precision of EMT subsystems is higher than that of the Central-TS subsystem, the improvement of the accuracy of Thevenin equivalents in the EMT subsystem is more important than that of Norton equivalents in the Central-TS subsystem [10]. In the example of multiple EMT subsystems, only the impact of Central-TS subsystem is considered for the traditional hybrid method when calculating Thevenin equivalents; but the impact of other EMT subsystems is not fully considered [13]. In order to solve this problem, the proposed method takes into account the impact of both the Central-TS subsystem and all other EMT subsystems simultaneously. Further, Thevenin equivalents are updated using two-level Schur complement. The development of the update strategy and its comparison with the traditional one are given in Fig. 3 and will be elaborated below. After that, the network equation of each subsystem will be derived as well.

## A. Update of Three-phase Thevenin Equivalents

As shown in Fig. 3, for any of the EMT subsystems, its external system, including the Central-TS subsystem and other EMT subsystems, should be represented by a Thevenin equivalent circuit with the parameters of $\tilde { v } _ { j } ^ { a b c }$ and $\tilde { Z } _ { j } ^ { a b c }$ . In order to make the derivation concise, we assume that there is only one three-phase branch connecting the $j ^ { t h }$ EMT subsystem and the Central-TS subsystem. To derive these parameters, the network equation of the whole system at the $k ^ { t h }$ iteration or time $t _ { k }$ is expressed as

![](images/8f4a423a843c834af4b251fc6770d3e30ada07cb88558e3ec23c6e89cdeaa110.jpg)  
Fig. 2. Calculation procedure of the proposed method

$$
\begin{array} { r l r } { \left[ \begin{array} { c c c c c } { Y _ { 1 1 } ^ { a b c } } & { \cdots } & { \bar { Y } _ { 1 t } ^ { a b c } S ^ { - 1 } } \\ { \vdots } & { \ddots } & & { \vdots } \\ & & & & { \ddots } \\ & & & & { Y _ { N N } ^ { a b c } } & { \bar { Y } _ { N t } ^ { a b c } S ^ { - 1 } } \\ { Y _ { t 1 } ^ { 1 2 0 } S } & { \cdots } & { Y _ { t N } ^ { 1 2 0 } S } & { Y _ { t t } ^ { 1 2 0 } } \end{array} \right] \stackrel { } { \left[ \begin{array} { c } { V _ { e m t , 1 } ^ { a b c } \left( t _ { k } \right) } \\ { \vdots } \\ { \vdots } \\ { V _ { e m t , N } ^ { a b c } \left( t _ { k } \right) } \\ { V _ { t 1 } ^ { 1 2 0 } \left( t _ { k } \right) } \end{array} \right] } = \left[ \begin{array} { c } { I _ { e m t , 1 } ^ { a b c } \left( t _ { k } \right) } \\ { \vdots } \\ { I _ { e m t , N } ^ { a b c } \left( t _ { k } \right) } \\ { I _ { T S } ^ { 1 2 0 } \left( t _ { k } \right) } \end{array} \right] , } \end{array}\tag{8}
$$

where $Y _ { j j } ^ { a b c } \left( j = 1 , 2 , . . . N \right)$ are nodal admittance matrices of the $j ^ { t h }$ EMT subsystem; $I _ { e m t , j } ^ { a b c } ( t _ { k } )$ is the current injector of the $j ^ { t h }$ EMT subsystem at time $t _ { k } ; V _ { e m t , j } ^ { a b c } ( t _ { k } )$ is the three-phase voltage vectors of the $j ^ { t h }$ EMT subsystem at time $t _ { k } ; V _ { T S } ^ { 1 2 0 } ( t _ { k } ) , I _ { T S } ^ { 1 2 0 } ( t _ { k } )$ are the three-sequence voltage vector and current injector of the Central-TS subsystem; $\bar { \bar { Y } } _ { j t } ^ { a b c }$ is the equivalent admittance in the $j ^ { t h }$ EMT subsystem, corresponding to the Thevenin impedance in the $j ^ { t h }$ EMT subsystem or $\tilde { Z } _ { j } ^ { a b \bar { c } }$ , which represents the impact on the $j ^ { t h }$ EMT subsystem from the Central-TS subsystem; $Y _ { t j } ^ { 1 2 0 }$ is the equivalent admittance in the Central-TS subsystem, corresponding to $Y _ { j } ^ { 1 2 0 }$ in Fig. 1(b). S is the three-phase to three-sequence transformation matrix. All the conductances and variables above are derived in the phasor form.

By marking all the EMT subsystems except the $j ^ { t h }$ EMT subsystem as external EMT subsystems, the network equation

![](images/4888849a16e01a682b6f081ce697cf54495a940d0e9ba016ce3005441f4f1d0f.jpg)  
Fig. 3. Thevenin equivalents of the proposed method and the traditional method

of (8) can be rewritten into

$$
\begin{array} { r } { \left[ Y _ { j j } ^ { a b c } \right. \qquad \left. \bar { Y } _ { j t } ^ { a b c } S ^ { - 1 } \right] \left[ V _ { e m t , j } ^ { a b c } ( t _ { k } ) \right] \qquad \left[ I _ { e m t , j } ^ { a b c } ( t _ { k } ) \right] } \\ { \left. Y _ { e e } ^ { a b c } \quad \bar { Y } _ { e t } ^ { a b c } S ^ { - 1 } \right] \left[ V _ { e m t , e } ^ { a b c } ( t _ { k } ) \right] = \left[ I _ { e m t , e } ^ { a b c } ( t _ { k } ) \right] , } \\ { \left[ Y _ { t j } ^ { 1 2 0 } S \quad Y _ { t e } ^ { 1 2 0 } S \quad Y _ { t t } ^ { 1 2 0 } \right] \left[ V _ { T S } ^ { 1 2 0 } ( t _ { k } ) \right] \left[ I _ { T S } ^ { 1 2 0 } ( t _ { k } ) \right] } \end{array}\tag{9}
$$

where $Y _ { e e } ^ { a b c }$ represents the node admittance matrix of the external EMT subsystems; $I _ { e m t , j } ^ { a b c } ( t _ { k } ) , I _ { e m t , e } ^ { a b c } ( t _ { k } ) \mathrm { a r e }$ the current injectors of the $j ^ { t h }$ and external EMT subsystems; $V _ { e m t , j } ^ { a b c } ( t _ { k } ) , ~ V _ { e m t , e } ^ { a b c } ( t _ { k } )$ are the three-phase voltage vectors of the $j ^ { t h }$ EMT subsystem and external EMT subsystems; $\bar { Y } _ { e t } ^ { a b c }$ is the equivalent admittance of external EMT subsystems; $Y _ { t e } ^ { 1 2 0 }$ is the equivalent admittance of the Central-TS subsystem.

Then the two-level Schur complement is used to calculate parameters of Thevenin equivalents in the EMT subsystem.

In the first Schur complement, the variables of external EMT subsystems in (9) are eliminated to get the following expression:

$$
\left[ \begin{array} { c c } { Y _ { j j } ^ { a b c } } & { \bar { Y } _ { j t } ^ { a b c } S ^ { - 1 } } \\ { Y _ { t j } ^ { 1 2 0 } S } & { \tilde { Y } _ { t t } ^ { 1 2 0 } } \end{array} \right] \left[ \begin{array} { l } { V _ { e m t , j } ^ { a b c } ( t _ { k } ) } \\ { V _ { T S } ^ { 1 2 0 } ( t _ { k } ) } \end{array} \right] = \left[ \begin{array} { l } { I _ { e m t , j } ^ { a b c } ( t _ { k } ) } \\ { \tilde { I } _ { T S } ^ { 1 2 0 } ( t _ { k } ) } \end{array} \right] ,\tag{10}
$$

and

$$
\left\{ \begin{array} { l } { { \tilde { Y } _ { t t } ^ { 1 2 0 } = Y _ { t t } ^ { 1 2 0 } - Y _ { t e } ^ { 1 2 0 } S [ Y _ { e e } ^ { a b c } ] ^ { - 1 } \bar { Y } _ { e t } ^ { a b c } S ^ { - 1 } , } } \\ { { \tilde { I } _ { T S } ^ { 1 2 0 } ( t _ { k } ) = I _ { T S } ^ { 1 2 0 } ( t _ { k } ) - Y _ { t e } ^ { 1 2 0 } S [ Y _ { e e } ^ { a b c } ] ^ { - 1 } I _ { e m t , e } ^ { a b c } ( t _ { k } ) , } } \end{array} \right.\tag{11}
$$

where the term $- Y _ { t e } ^ { 1 2 0 } S [ Y _ { e e } ^ { a b c } ] ^ { - 1 } \bar { Y } _ { e t } ^ { a b c } S ^ { - 1 }$ is actually the Norton equivalent admittance of external EMT subsystems connected to the Central-TS subsystem. Therefore, $\check { \tilde { Y } } _ { t t } ^ { 1 2 0 }$ contains the three-sequence admittance of the Central-TS subsystem itself and the equivalent admittance of its neighbouring EMT subsystems.

The second Schur complement is applied to (10) to derive the Thevenin equivalent impedance of the $j ^ { t h }$ EMT subsystem or $\tilde { Z } _ { j } ^ { a b c }$ , as shown in [22].

$$
\tilde { Z } _ { j } ^ { a b c } = M _ { j } ^ { T } S ^ { - 1 } [ \tilde { Y } _ { t t } ^ { 1 2 0 } ] ^ { - 1 } S M _ { t } ,\tag{12}
$$

where Mt is the correlation vector between the branches of the $j ^ { t h }$ interface and nodes of the Central-TS subsystem [22]. $M _ { j }$ is similarly derived. They are of the form like $[ 0 . . . 1 . . - 1 . . . 0 ] ^ { T }$ with integers 1 and -1 denoting the start and end node of the corresponding branch, respectively.

Unlike our proposed method, traditionally only the impact from the Central-TS subsystem is considered when calculating the Thevenin impedance. The impact from other EMT subsystems is just neglected. Correspondingly, (8) is simplified into [13]

$$
\begin{array} { r } { \left[ Y _ { j j } ^ { a b c } \quad \bar { Y } _ { j t } ^ { a b c } S ^ { - 1 } \right] \left[ V _ { e m t , j } ^ { a b c } ( t _ { k } ) \right] = \left[ I _ { e m t , j } ^ { a b c } ( t _ { k } ) \right] , } \\ { \left[ Y _ { t j } ^ { 1 2 0 } S \quad Y _ { t t } ^ { 1 2 0 } \quad \right] \left[ V _ { T S } ^ { 1 2 0 } ( t _ { k } ) \right] ^ { = } \left[ \tilde { I } _ { T S } ^ { 1 2 0 } ( t _ { k } ) \right] ^ { , } } \end{array}\tag{13}
$$

For the Central-TS subsystem, its impedance matrix is $Z _ { t t } ^ { 1 2 0 } =$ $[ Y _ { t t } ^ { 1 2 0 } ] ^ { - 1 }$ , thereby the Thevenin impedance of the $j ^ { t h }$ EMT subsystem, or $Z _ { j } ^ { \dot { a } b c }$ , is derived as [22]

$$
Z _ { j } ^ { a b c } = M _ { j } ^ { T } S ^ { - 1 } [ Y _ { t t } ^ { 1 2 0 } ] ^ { - 1 } S M _ { t } .\tag{14}
$$

By comparing (12) and (14), it is found that $\tilde { Z } _ { j } ^ { a b c }$ is computed using Schur complement of matrix $[ \tilde { Y } _ { t t } ^ { 1 2 0 } ] ^ { - 1 }$ and thus reflects the impacts from both the Central-TS and all the other EMT subsystems.

With the parameters of Thevenin equivalents updated for each EMT subsystem, the system equations of the $j ^ { t h }$ EMT subsystem including its interface are written into [14]

$$
\left\{ \begin{array} { l l } { \frac { d { \pmb x } _ { e m t , j } ^ { a b c } } { d t } = F _ { 1 , j } ( { \pmb x } _ { e m t , j } ^ { a b c } , \pmb { i } _ { e , j } ^ { a b c } ) , } \\ { \frac { d \pmb { i } _ { e , j } ^ { a b c } } { d t } = F _ { 2 , j } ( { \pmb x } _ { e m t , j } ^ { a b c } , \pmb { i } _ { e , j } ^ { a b c } , \tilde { \nu } _ { j } ^ { a b c } ) , } \end{array} \right.\tag{15}
$$

where $\boldsymbol { x } _ { e m t , j } ^ { a b c }$ represents the dynamic variables in the $j ^ { t h }$ EMT subsystem and $F _ { 1 , j }$ is their corresponding differential terms; $F _ { 2 , j }$ is the additional set of three-phase equations due to the inclusion of the interface model in the $j ^ { t h }$ EMT subsystem:

$$
F _ { 2 , j } = \left[ \tilde { L } _ { e , j } ^ { a b c } \right] ^ { - 1 } ( v _ { e , j } ^ { a b c } - \tilde { R } _ { e , j } ^ { a b c } i _ { e , j } ^ { a b c } - \tilde { v } _ { j } ^ { a b c } ) .\tag{16}
$$

The EMT results of the $j ^ { t h }$ EMT subsystem are obtained by calculating (15)-(16) at each simulation results based on the nodal analysis method [14], [19].

## B. Update of Three-sequence Norton Equivalents

For the simulation of the Central-TS subsystem, the impact from each EMT subsystem is represented by a Norton equivalent circuit with the interface variables being $Y _ { j } ^ { 1 2 0 }$ (equivalent Norton current) and $I _ { j } ^ { 1 2 0 }$ (equivalent admittance), which should be updated in each iteration.

In our proposed method, the equivalent admittance of the $j ^ { t h }$ EMT subsystem, or $Y _ { j } ^ { 1 2 0 }$ , is derived as below [22]

$$
Y _ { j } ^ { 1 2 0 } = M _ { t } ^ { T } S Y _ { j j } ^ { a b c } S ^ { - 1 } M _ { j } ,\tag{17}
$$

![](images/e9565376c7244c8a467b4b2f623eb91cdd1921dcb66cd7f9f227a7ee55489b9f.jpg)  
Fig. 4. Studied system

where $Y _ { j j } ^ { a b c } \left( j = 1 , 2 . . . N \right)$ are the three-phase nodal admittance matrices of the $j ^ { t h }$ EMT subsystem.

And the Norton equivalent current $I _ { j } ^ { 1 2 0 }$ is computed as

$$
I _ { j } ^ { 1 2 0 } = I _ { t , j } ^ { 1 2 0 } + Y _ { j } ^ { 1 2 0 } V _ { t , j } ^ { 1 2 0 } ,\tag{18}
$$

where $V _ { t , j } ^ { 1 2 0 } , ~ I _ { t , j } ^ { 1 2 0 }$ are the interface voltage and current of the $j ^ { t h }$ EMT subsystem in the three-sequence domain.

After the update of the Norton equivalent parameters of the Central-TS subsystem, the corresponding network equation at $t _ { k }$ is given by

$$
\sum _ { j = 1 } ^ { N } Y _ { t j } ^ { 1 2 0 } S V _ { e m t , j } ^ { a b c } ( t _ { k } ) + Y _ { t t } ^ { 1 2 0 } V _ { T S } ^ { 1 2 0 } ( t _ { k } ) = I _ { T S } ^ { 1 2 0 } ( t _ { k } ) .\tag{19}
$$

Similarly, its update equation can be written into

$$
\begin{array} { r } { Y _ { t t } ^ { 1 2 0 } V _ { T S } ^ { 1 2 0 } ( t _ { k } ) = I _ { T S } ^ { 1 2 0 } ( t _ { k } ) - \underset { j = 1 } { \overset { N } { \sum } } Y _ { t j } ^ { 1 2 0 } S V _ { e m t , j } ^ { a b c } ( t _ { k } ) } \\ { = I _ { T S } ^ { 1 2 0 } ( t _ { k } ) - \underset { j = 1 } { \overset { N } { \sum } } I _ { T S , j } ^ { 1 2 0 } ( t _ { k } ) , } \end{array}\tag{20}
$$

where $I _ { T S , j } ^ { 1 2 0 } ( t _ { k } )$ denotes the equivalent currents injected into the Central-TS subsystem, representing the impact from the $j ^ { t h }$ EMT subsystem connected to the Central-TS subsystem.

## IV. CASE STUDIES

To evaluate the accuracy and efficiency of the proposed distributed hybrid simulation method, case studies are carried out on an AC/DC system shown in Fig. 4. According to the system description and parameters in [23], the two-terminal two-level VSC-HVDC connects Bus 21 and 29 to increase the transmission capacity of the power network. Its parameters are given as follows: the capacity is 600MVA; the rated DC voltage is 400kV; the rated AC voltage is 345kV; the grounding resistance of the coupling transformer is 1M; the length of DC cable is 220km [6]. VSC2 regulates the DC voltage while VSC1 controls the power flow along the DC line.

TABLE I  
THREE-PHASE THEVENIN IMPEDANCE OF DIFFERENT METHODS
<table><tr><td rowspan=2 colspan=1>Bus</td><td rowspan=2 colspan=1>Method</td><td rowspan=1 colspan=2>Three-phase Thevenin impedances</td></tr><tr><td rowspan=1 colspan=1> $\overline { { \mathrm { ~ { ~ Z ~ } ~ } _ { a a } , Z _ { b b } , Z _ { c c } / \Omega } }$ </td><td rowspan=1 colspan=1> $\overline { { \mathrm { ~ \textit ~ { ~ Z ~ } ~ } _ { a b } , \boldsymbol { Z } _ { a c } , \boldsymbol { Z } _ { b c } / \Omega } }$ </td></tr><tr><td rowspan=1 colspan=1>21</td><td rowspan=1 colspan=1>traditionalproposed</td><td rowspan=1 colspan=1> $4 . 0 1 \substack { + } \mathrm { j } 3 0 . 9 7$  $3 . 3 3 \mathrm { + j } 2 8 . 1 8$ </td><td rowspan=1 colspan=1>53.33+j425.8249.22+j402.35</td></tr><tr><td rowspan=1 colspan=1>22</td><td rowspan=1 colspan=1>traditionalproposed</td><td rowspan=1 colspan=1>3.40+j22.343.02+j20.83</td><td rowspan=1 colspan=1>43.54+j443.8739.54+j412.85</td></tr><tr><td rowspan=1 colspan=1>29</td><td rowspan=1 colspan=1>traditionalproposed</td><td rowspan=1 colspan=1>1.67+j17.971.53+j15.24</td><td rowspan=1 colspan=1>29.62+j283.8825.32+j269.69</td></tr></table>

A nonlinear dynamic load is connected at Bus 8, consisting of 60% constant impedance and 40% induction motor load. In the proposed distributed hybrid simulation, the two-terminal VSCs and the nonlinear dynamic loads are assigned to two different EMT subsystems, while the rest of the AC system is included in the Central-TS subsystem. Different EMT subsystems are simulated using PSCAD/EMTDC and the Central-TS subsystem is simulated using the TSA program [13]. The interactions among different subsystems are reflected by the interface models. Notably, the simulation step of the Central-TS subsystem is 5ms, while that of EMT subsystems is 20µs. For comparison, the reference results are obtained by simulating the whole system using EMT program (PSCAD/EMTDC) with a unanimous time step of 20µs. The Thevenin equivalent impedances viewed from Buses 21, 22 and 29 are calculated and given in Table I, where the “proposed” refers to the proposed method; and “traditional” refers to the traditional method given in [13], [18]. It is shown that two methods produce different self and mutual impedances. The impedance derived by the proposed method are slightly smaller than that by the traditional method. The reason lies in that an additional equivalent impedance of the external EMT subsystem, given by the two-level Schur complement, is in parallel connection with the interface impedance in the Central-TS subsystem.

Simulation results will be presented under different scenarios to check the performance of the proposed method and its advantages over the traditional one. To quantify the simulation accuracy, a metric called average simulation error is defined as

$$
\varepsilon _ { a \nu g } = \frac { 1 } { N } \sum _ { i = 1 } ^ { N } \| x _ { n u m , i } - x _ { r e f , i } \| ,\tag{21}
$$

where $x _ { n u m , i } , x _ { r e f , i }$ are the $i ^ { t h }$ sample of the monitored variable x in per unit that are produced by different simulation methods; N is the number of samples.

## A. Single-phase fault at bus 22

In this scenario, an asymmetric fault is applied to the nonlinear dynamic load by triggering a single-phase inductive fault on Bus 22 at t=1.0s. The fault lasts for 0.05s. Fig. 5 and Fig. 6 show the results for the two cases of short (20km) and long (200km) interface lines (marked “Line $1 ^ { \circ }$ in Fig. 3). The zoomed-in curves of AC voltages are shown in Fig. 7. It can be seen that in both cases the results of the proposed method are much closer to the reference values while the traditional method has obvious errors. The proposed method has improved simulation accuracy significantly. This advantage is even more pronounced when the interface circuit is a long transmission line. The underlying reason for such improvement is that: the interface impedances of the proposed method have fully considered the impact from both the Central-TS and all other EMT subsystems and thus is much more accurate. For the case of the longer line, the requirement for the accuracy of interface impedance is higher. So the advantages of the proposed method become more significant.

![](images/bf73ca51ec38a0cc88bffe472be90691b69dc2a8e60453fbfda738a3de34b8fd.jpg)  
Fig. 5. Curves of short(20km) interface lines

![](images/4998f17dfe443a075a0189ab488ab1c68f219ec18d50a0e9931b6ad82b264f4a.jpg)

![](images/55da55ea6cef1b0778c4e32081d5e440e9c057a23970b0a17f452d3b6fba460f.jpg)

![](images/555b5240400538a92947144b70f2b8f487794ac6a0988a0c7df20cc54a75b68e.jpg)

![](images/ea6dd043da6d40265d2ae69e7b544f325055680657a9d386199e78a850d77e08.jpg)

![](images/e28bc82d4d6db8b835b5eef6800769aa9cbeeeafc431c6b0dfdc8595d38df6be.jpg)  
Fig. 6. Curves of long(200km) interface lines

![](images/2d41ae6b9c037018d2b4b24faeeb207fe51f7f04022009042ef8466d5a7e517a.jpg)

![](images/c268f057072f6c7f34898f762876a7e152893946dce9f6343d61718eee5e4df5.jpg)

![](images/5d8e4f8acaf44527c936ddf54b68521a4c8fa51a9a0b1cbe4ded50dc690e3bfb.jpg)

![](images/8b5295d4d6572e09700798840694d7a065b873ab1218663644903fdce8567179.jpg)  
Fig. 7. Zoomed-in curves of AC voltages

![](images/9e9dc13f4d48f738b7a6d81a00160a3205b283704ae4e82c4518cc0a0ac57789.jpg)  
Fig. 8. Voltage magnitude at interface bus 23

Table II lists the average errors of different methods during this simulation scenario. If different interaction protocols are used, the resulting average errors are shown in Table III. As can be found, for the longer-line case, the average errors of the proposed method are much smaller than those of the traditional method. Taking the active power as an example, its simulation error is reduced from 12.5% to 3.1%. From Table III, it is demonstrated that the combined interaction protocol produces more accurate results than the parallel protocol. For instance, the error of the active power is lowered from 6.3% to 3.1% for the case of longer interface line.

![](images/1497708ff3eb27af3edb3139d1e8fc6c479bbed67041ecdd5acb3a1dd309d62c.jpg)

![](images/f3217f7dfa13b0db96e5cb116c3613defee70c7a3cb587407a161ae36ac66835.jpg)  
Fig. 9. Curves of Gen 6

Simulation outputs of the quantities at the boundaries and from deep in the Central-TS subsystem are also shown in Figs. 8 and 9. With the identical models as in Fig. 6, Figs. 8 and 9 show the voltage at the interface bus 23 and the terminal voltage power of Gen 6. A good consistence can be observed between the results of the proposed method and the reference values. However, the traditional method has obvious errors.

![](images/31bff3824f81e0f12eba4341972b0e936b8ea7cdb482e0411d74fb60d138c40b.jpg)

![](images/d0c236bb2af75c5adc8019213b66c2c732e066dddd9b91fa7d0833bd0cf5e5d8.jpg)  
Fig. 10. Curves of short(20km) interface lines

![](images/df781469751f323bf43cb9af4bb4bc8a6828c88a939e1f2db28f13f9318a1c3f.jpg)

![](images/c2a3c4146a60e1bf80cf7d6e7228b9f28c49125ad1fce944af0116b4588a1441.jpg)

![](images/3cc5416dc2c617a3eb388d99e0e01834ae983bdcc33682ec32fcffffd9cbda4f.jpg)

![](images/04b987229a6403d99331c34407f3e79070e54028a2974d24ab963322f8335db8.jpg)  
Fig. 11. Curves of long(200km) interface lines

![](images/a73ddd7127bf5484cf5219e4b4df247c05a1fbb6bd35df888cd3fe684d354fc1.jpg)

![](images/2c029e619e477d7e26dabd44aea4420de159910e82f79f9b81fd940990a100f0.jpg)  
TABLE II

ERRORS OF DIFFERENT METHOD (IN PER UNIT)
<table><tr><td rowspan=1 colspan=1>interface Impedance $R + j X / \Omega$ Line1</td><td rowspan=1 colspan=1>Method</td><td rowspan=1 colspan=1> $P _ { l o a d }$ </td><td rowspan=1 colspan=1> $Q _ { l o a d }$ </td><td rowspan=1 colspan=1> $U _ { 2 2 A }$ </td><td rowspan=1 colspan=1> $I _ { 2 2 - 2 3 A }$ </td></tr><tr><td rowspan=1 colspan=1>0.61+j4.82(short line)</td><td rowspan=1 colspan=1>traditionalproposed</td><td rowspan=1 colspan=1>0.0640.023</td><td rowspan=1 colspan=1>0.0870.013</td><td rowspan=1 colspan=1>0.0320.014</td><td rowspan=1 colspan=1>0.0650.013</td></tr><tr><td rowspan=1 colspan=1>6.10+j48.21(long line)</td><td rowspan=1 colspan=1>traditionalproposed</td><td rowspan=1 colspan=1>0.1250.031</td><td rowspan=1 colspan=1>0.1040.022</td><td rowspan=1 colspan=1>0.0480.025</td><td rowspan=1 colspan=1>0.0850.022</td></tr></table>

TABLE III

AVERAGE SIMULATION ERRORS UNDER DIFFERENT INTERACTION PROTOCOLS (IN PER UNIT)
<table><tr><td rowspan=1 colspan=1>interface Impedance $R + j X / \Omega$ Line1</td><td rowspan=1 colspan=1>Method</td><td rowspan=1 colspan=1> $P _ { l o a d }$ </td><td rowspan=1 colspan=1> $Q _ { l o a d }$ </td><td rowspan=1 colspan=1> $U _ { 2 2 A }$ </td><td rowspan=1 colspan=1>122-23A</td></tr><tr><td rowspan=2 colspan=1>0.61+j4.82(short line)</td><td rowspan=2 colspan=1>serialparallelcombined</td><td rowspan=2 colspan=1>0.0170.0340.023</td><td rowspan=1 colspan=1>0.011</td><td rowspan=1 colspan=1>0.008</td><td rowspan=2 colspan=1>0.0100.0280.013</td></tr><tr><td rowspan=1 colspan=1>0.0320.013</td><td rowspan=1 colspan=1>0.0350.014</td></tr><tr><td rowspan=3 colspan=1>6.10+j48.21(long line)</td><td rowspan=3 colspan=1>serialparallelcombined</td><td rowspan=2 colspan=1>0.0280.063</td><td rowspan=1 colspan=1>0.015</td><td rowspan=1 colspan=1>0.018</td><td rowspan=1 colspan=1>0.016</td></tr><tr><td rowspan=1 colspan=1>0.051</td><td rowspan=1 colspan=1>0.034</td><td rowspan=1 colspan=1>0.032</td></tr><tr><td rowspan=1 colspan=1>0.031</td><td rowspan=1 colspan=1>0.022</td><td rowspan=1 colspan=1>0.025</td><td rowspan=1 colspan=1>0.022</td></tr></table>

## B. Three-phase fault at bus 39

This simulation scenario aims to evaluate the proposed method with a focus on the transients of VSCs. A threephase, solid fault is triggered on Bus 39 at t=1.0s, and lasts for 100ms. Two cases are studied. In one case, the interface lines (marked Line 2 and Line 3 in Fig. 3) are of a shorter length of 20km. In the other case, longer (200km) interface lines are used. The results of both cases are shown in Figs. 10-11. The zoomed-in curves of the AC currents are shown in Fig. 12. It can be observed that the proposed method produces more accurate results than the traditional one. Unlike the asymmetric fault, the improvement of precision for power curves under symmetric fault is more significant than that for the AC current and voltage curves, which indicates that a more accurate calculation of interface impedances has a larger impact on the accuracy of the power curves than other quantities. Figs. 10-11 (c, d) and Fig. 12 also show that the AC voltages and currents obtained with the traditional method have obvious phase shift errors, though the DC voltages given by both methods agree with the reference value, as shown in Figs. 10-11(b). Table IV presents the average errors of different methods. If different interaction protocols are used, the resulting average errors are shown in Table V. As can be seen, the proposed method has higher simulation accuracy than the traditional method, especially for the longer-line case. For example, the simulation error is reduced from 15.7% to 3.2% for the active power. It is demonstrated in Table V that the combined interaction protocol produces more accurate results than the parallel protocol. The errors of the active power curve is reduced from 4.8% to 3.2% for the case of longer interface lines.

![](images/fd59385ddee046d28b28f04ba0467775d40cb718725c3d50558052eba3e2e858.jpg)

![](images/d073ea5cd51a62c68f7744296389c99aba5aa17fa191aeaff6dddd41d7fa1882.jpg)

Fig. 12. Zoomed-in curves  
![](images/9b8bf6f8a8117e6129e3f762a732d4cbd061d4e6205924808734b65aa677ac16.jpg)  
Fig. 13. Voltage magnitude at interface bus 21

![](images/cb439de210cbc05a6b37375964ce23bef37827f68482c8d28c3de23f78f7a9de.jpg)

![](images/c37f28dded7762c5a7b630e38bedc4c4c1b2033c73574a268862cad73ef463ea.jpg)  
Fig. 14. Curves of Gen 6

TABLE IV  
ERRORS OF DIFFERENT METHOD (IN PER UNIT)
<table><tr><td rowspan=1 colspan=2>interface ImpedanceR+jx/Ω</td><td rowspan=2 colspan=1>Method</td><td rowspan=2 colspan=1> $P _ { \nu s c }$ </td><td rowspan=2 colspan=1> $Q _ { \nu s c }$ </td><td rowspan=2 colspan=1> $U _ { d c }$ </td><td rowspan=2 colspan=1> $I _ { d c }$ </td></tr><tr><td rowspan=1 colspan=1>Line2</td><td rowspan=1 colspan=1>Line3</td></tr><tr><td rowspan=1 colspan=1>0.74+j4.78(short line)</td><td rowspan=1 colspan=1>0.98+j6.12(short line)</td><td rowspan=1 colspan=1>traditionalproposed</td><td rowspan=1 colspan=1>0.1070.025</td><td rowspan=1 colspan=1>0.0450.010</td><td rowspan=1 colspan=1>0.0140.011</td><td rowspan=1 colspan=1>0.0700.038</td></tr><tr><td rowspan=1 colspan=1>7.44+j47.88(long line)</td><td rowspan=1 colspan=1>9.81+j61.24(long line)</td><td rowspan=1 colspan=1>traditionalproposed</td><td rowspan=1 colspan=1>0.1570.032</td><td rowspan=1 colspan=1>0.0700.018</td><td rowspan=1 colspan=1>0.0250.020</td><td rowspan=1 colspan=1>0.120.028</td></tr></table>

Simulation outputs of the three-phase fault from the boundaries and from deep in the Central-TS subsystem are shown in Fig. 13 and Fig. 14. With the same models as in Fig. 11, Figs. 13 and 14 display the voltage at the interface bus 21 and power curves of Gen 6. It can be concluded that in both fault scenarios the proposed method provides more accurate results than the traditional method. Moreover, the improvement of simulation accuracy is more obvious for the scenario of the three-phase fault.

## V. APPLICATIONS TO A PRACTICAL AC/DC SYSTEM

A practical AC/DC system is studied to evaluate the accuracy and efficiency of the proposed hybrid method, which is shown in Fig. 15. The parameters of the two terminal two-level VSC-HVDC is given as follows: the rated DC power is 800 MW; the rated DC voltage is 400 kV; the rated DC current is 1 kA, and the length of the DC cable is 120km. VSC2 regulates the DC voltage while VSC1 controls the power flow along the DC line. The 110 kV and 220 kV buses of the main AC grids are shown in Fig. 15. Therein, 441 buses and 543 transmission lines, etc. are contained in the studied AC system [23].

The simulation scenario of the practical AC/DC system focuses on the transients of VSCs, where the three-phase, solid fault is triggered on Bus Mozhu at t=1s, and lasts for 80ms. Simulation results of quantities within the EMT subsystems are shown in Fig. 16. It can be concluded that the results of the proposed method is more accurate than those of the traditional method, in the case of large practical AC/DC systems.

TABLE V  
AVERAGE SIMULATION ERRORS UNDER DIFFERENT INTERACTION PROTOCOLS (IN PER UNIT)
<table><tr><td colspan="2">interface Impedance R+jx/Ω</td><td rowspan="2">Method</td><td rowspan="2"> $P _ { \nu s c }$ </td><td rowspan="2"> $Q _ { v s c }$ </td><td rowspan="2"> $U _ { d c }$ </td><td rowspan="2"> $I _ { d c }$ </td></tr><tr><td>Line2</td><td>Line3</td></tr><tr><td rowspan="2">0.74+j4.78 (short line)</td><td rowspan="2">0.98+j6.12 (short line)</td><td>serial</td><td>0.018</td><td>0.008</td><td>0.007</td><td>0.021</td></tr><tr><td>parallel</td><td>0.037</td><td>0.025</td><td>0.018</td><td>0.042</td></tr><tr><td rowspan="2">7.44+j47.88 (long line)</td><td></td><td>combined serial</td><td>0.025 0.021</td><td>0.010 0.016</td><td>0.011 0.016</td><td>0.038 0.015</td></tr><tr><td>9.81+j61.24 (long line)</td><td>parallel combined</td><td>0.048 0.032</td><td>0.035 0.018</td><td>0.038 0.020</td><td>0.048</td></tr></table>

![](images/15e0ad7c7a15e474f5e192ba51da03b2fb35fa49f1dcfb2f4ecb1ec7df0c19b3.jpg)  
Fig. 15. A Practical AC/DC Systems

Simulation results meausured at the boundaries, i.e., the interface current and voltage of Bus Mozhu, are shown in Fig. 17 and Fig. 18. Obviously the results obtained with our proposed method are highly consistent with the reference output; while the traditional method yields significant simulation errors, especially during the fault period. For example, errors of the interface voltages are reduced from 0.031 pu to 0.004 pu. It is shown that the proposed method is more accurate than the traditional one and the prospective electromechanical oscillations are more accurately preserved by the proposed method. Therefore, the effectiveness of the proposed method is fully validated.

The CPU time consumed for both of the above simulation cases is listed in Table VII. By comparing the performance of the traditional method and the proposed method with different interaction protocols, it can be concluded that the proposed method achieves much higher efficiency than the traditional one. The proposed method with combined interaction protocol is 4-5 times faster than the traditional method. Considering its previously demonstrated advantages in simulation accuracy, the proposed method is more suitable for the simulation of large scale AC/DC systems containing power electronic devices and nonlinear dynamic loads.

![](images/20b9f6fa46926a8741f3499f90033aa8f9aeb52df40c918bc87cb2eb5ef26c01.jpg)  
Fig. 16. Curves of VSC

![](images/8b3f6081598cf03fba0c3b12bd854b4030b62f422f9adcc00198f185d138faf5.jpg)  
Fig. 17. Curves of interface currents

## VI. CONCLUSION

In this paper, a distributed hybrid simulation method is proposed. The whole system is partitioned into one Central-TS subsystem and multiple EMT subsystems. The interactions between different subsystems are reflected by the interface models. One distinct feature of the proposed method is that a new interfacing technique is developed based on the two-level Schur complement technique, whereby Thevenin equivalent parameters in each EMT subsystem are calculated to fully reflect the couplings among different EMT subsystems. Therefore, the obtained interface parameters are more accurate than those of the traditional method. The other important feature is that a combined interaction protocol is developed to further improve the efficiency and accuracy of simulation.

The modified IEEE 39 system and a practical AC/DC system is used to examine the performances of the proposed method. Simulation results have fully demonstrated its advantages. Particularly, when compared with the traditional method, the proposed method has a higher simulation accuracy, keeping the average simulation errors below 0.032 pu. And the proposed method increases the simulation efficiency by 4-5 times. Thus it offers a promising method for simulating the large-scale AC/DC system which contains both power electronic devices and nonlinear dynamic loads.

## REFERENCES

[1] N. Flourentzou, V. Agelidis, and G. Demetriades, “VSC-based HVDC power transmission systems: An overview,” IEEE Trans. Power Electron., vol. 24, no. 3, pp. 592-602, Mar. 2009.

[2] J. Mahseredjian, V. Dinavahi, and J. A. Martinez, “Simulation tools for electromagnetic transients in power systems: Overview and challenges,” IEEE Trans. Power Del., vol. 24, no. 3, pp. 1657-1669, Jul. 2009.

[3] G. O. Kalcon, G. P. Adam, O. Anaya-Lara, S. Lo, and K. Uhlen, “Smallsignal stability analysis of multi-terminal VSC-based DC transmission systems,” IEEE Trans. Power Syst., vol. 27, no. 4, pp. 1818-1830, Nov. 2012.

[4] K. M. Alawasa, Y. A. R. I. Mohamed, and W. Xu, “Active mitigation of subsynchronous interactions between PWM voltage-source converters and power networks,” IEEE Trans. Power Electron., vol. 29, no. 1, pp. 121-134, Jan. 2014.

![](images/00d74f331c9c846c37ddd7069ef95da13d5fb4aa829092a9c979c298ca68257d.jpg)  
Fig. 18. Voltage magnitude at interface bus Mozhu

TABLE VI  
SIMULATION EFFICIENCY TERMS OF CPU TIME (UNIT:SECOND)
<table><tr><td colspan="3"></td></tr><tr><td>reference</td><td>2550</td><td>7321</td></tr><tr><td>traditional</td><td>798</td><td>1421</td></tr><tr><td>proposed + serial protocol</td><td>252</td><td>473</td></tr><tr><td>proposed + parallel protocol</td><td>172</td><td>462</td></tr><tr><td>proposed + combined protocol</td><td>190</td><td>478</td></tr></table>

[5] A. A. van der Meer, R. L. Hendriks, et al. , “Combined simulation method for improved performance in grid integration studies including multi-terminal VSC-HVDC,” in IET Renewable Power Generation (RPG), 2011, pp. 1–6.

[6] A. A. van der Meer, M. Gibescu, M. A. M. M. van der Meijden, W. L. Kling, and J. A. Ferreira, “Advanced hybrid transient stability and EMT simulation for VSC-HVDC systems,” IEEE Trans. Power Del., vol. 30, no. 3, pp. 1057-1066, Jun. 2015.

[7] J. Chen, M. L. Crow, “A variable partitioning strategy for the multirate method in power systems,” IEEE Trans. Power Syst., vol. 23, no. 2, pp. 259–266 , May 2008.

[8] M. D. Heffernan, K. S. Turner, J. Arrillaga, and C. P. Arnold, “Computation of A.C.-D.C. system disturbancesPart I, II and III,” IEEE Trans. Power App. Syst., vol. PAS-100, pp. 4341-4348, 1981.

[9] M. Sultan, J. Reeve, and R. Adapa, “Combined transient and dynamic analysis of HVDC and FACTS systems,” IEEE Trans. Power Del., vol. 13, no. 4, pp. 1271-1277, Oct. 1998.

[10] V. Jalili-Marandi, V. Dinavahi, K. Strunz, J. A. Martinez, and A. Ramirez, “Interfacing techniques for transient stability and electromagnetic transient programs,” IEEE Trans. Power Del., vol. 24, no. 4, pp. 2385-2395, Oct. 2009.

[11] W. Stevens, UNIX Network Programming, vol. 1: Networking APIs: Sockets and XTI. Englewood Cliffs, NJ: Prentice-Hall, 1997.

[12] F. Plumier, P. Aristidou, C. Geuzaine, et al., “Co-simulation of Electromagnetic Transients and Phasor Models: a Relaxation Approach,” IEEE Trans. Power Del., vol. 31, no. 5, Mar. 2016.

[13] Q. Huang, V.Vittal, “Application of electromagnetic transient-transient stability hybrid simulation to FIDVR study,” IEEE Trans. Power Syst., vvol. 31, no. 4, pp. 2634–2646, Jul. 2016.

[14] X. Zhang, A. J. Flueck, S. Abhyankar, “Implicitly-Coupled Electromechanical and Electromagnetic Transient Analysis using a Frequency Dependent Network Equivalent,” IEEE Trans. Power Del., accepted.

[15] S. Abhyankar, and A. J. Flueck. , “An implicitly-coupled solution approach for combined electromechanical and electromagnetic transients simulation,” IEEE Power and Energy Society General Meeting, San Diego, USA, 2012.

[16] Y. Hu, W. Wu and B. Zhang, “A semidefinite programming model for passivity enforcement of frequency-dependent network equivalents,” IEEE Trans. Power Del., vol. 31, no. 1, pp. 397399, Feb. 2016.

[17] Y. Zhang, A.M. Gole, W. Wu et al., “Development and analysis of applicability of a hybrid transient simulation platform combining TSA and EMT elements,” IEEE Trans. Power Syst., vol. 28, no. 1, pp. 357- 366, Feb. 2013.

[18] G. D. Irwin, C. Amarasinghe ,N. Kroeker, and D. Woodford, “Parallel processing and hybrid simulation for HVDC/VSC PSCAD studies,” in Proc.10th IET Int. Conf. AC and DC Power Transmission, 2012, pp.1-6.

[19] J. A. Martinez-Velasco, Transient Analysis of Power Systems: Solution Techniques, Tools and Applications. Piscataway, NJ, USA: IEEE/Wiley, 2015.

[20] J. C. G. de Siqueira, B. D. Bonatto, J. R. Marti, et al, “A discussion about optimum time step size and maximum simulation time in EMTP-

based programs,” Int. J.of Electrical Power Energy Syst., vol. 72, pp. 24–32, 2015.

[21] D. Shu, X. Xie, S. Zhang, et al., “Hybrid method for numerical oscillation suppression based on rational-fraction approximations to exponential functions,” IET Generation, Transmission Distribution, vol. 10, no. 11, pp. 2825–2832, Aug. 2016.

[22] X. Wang, Modern Power Systems Analysis. New York: Springer, 2008.

[23] S. Liu, Z. Xu, W. Hua, G. Tang, and Y. Xue, “Electromechanical transient modeling of modular multilevel converter based multi-terminal HVDC systems,” IEEE Trans. Power Syst., vol. 29, no. 1, pp. 7283, Jan. 2014.

![](images/3fb37eaa6f6a8319ca99141f7b9e6abc98e1673aa4071f4c1c4feb6aad84cbc7.jpg)  
Dewu Shu (S’14) received the B.Sc. degree in Electrical Engineering from Tsinghua University in 2013. Currently, he is pursuing the Ph.D. degree in the Dept. of Electrical Engineering, Tsinghua University. His research interests include multirate EMT/TS simulations, parallel and distributed computing.

![](images/23ad9558c7d48405417d967978b0935d430255f7d9eac13937b357f83bc6b604.jpg)

Xiaorong Xie received the B.Sc. degree from Shanghai Jiao Tong University, Shanghai, China, in 1996 and the Ph.D./M. Eng. degrees from Tsinghua University, Beijing, China, in 2001. From 2001 to 2005, he was a Lecturer with the Department of Electrical Engineering, Tsinghua University. Since 2005, he works as an Associate Professor in the same department. His current research interests focus on power system analysis and control, and flexible ac transmission systems.

![](images/2329381bc0421262535d4115cea3536d3fc923f5ba8617a5b5ab44bd5d4e746e.jpg)

Qirong Jiang (M98) received the B.S. and Ph.D. degrees in electrical engineering from Tsinghua University, Beijing, China, in 1992 and 1997, respectively. Since 2006, he has been a Professor at Tsinghua University. His research interests include power system analysis and control, modeling and control of exible ac transmission systems, power quality analysis and mitigation, power-electronic equipment, and renewable energy power conversion.

Qiuhua Huang (S’14) received the B.E. and M.S. degree in electrical engineering from the South China University of Technology, Guangzhou, China, in 2009 and 2012, respectively. He is currently pursuing the Ph.D. degree in electrical engineering in Arizona State University, Tempe, AZ, USA. His research interests include power system modeling, power system transient simulation and power system stability.

Chunpeng Zhang (M10) was born in Laiyang, China, in 1976. He received the B.S. and M.S. degrees from the Department of Electrical Engineering, Shandong University, Jinan, China, in 1997 and 2000, respectively. He is currently a Lecturer in the Department of Electrical Engineering, Tsinghua University, Beijing, China. His research interests include flexible ac transmission systems and power quality.