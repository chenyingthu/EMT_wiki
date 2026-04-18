# A Multirate EMT Co-simulation of Large AC and MMC-based MTDC Systems

Dewu Shu, Student Member, IEEE, Xiaorong Xie, Senior Member, IEEE, Qirong Jiang, Member, IEEE Gaopeng Guo, Ke Wang

Abstract—This paper proposes a novel multi-rate co-simulation method to improve simulation efficiency of large-scale AC plus multi-terminal DC (MTDC) grids. In this method, the whole system is partitioned into different AC and MTDC subsystems. They each are simulated with different time-steps according to their requirements of accuracy. Unlike existing methods where simplified models are adopted, the proposed approach fully reserves both the detailed behavior of converters and the nonlinear dynamics of large-scale AC systems. To realize the coordination between different subsystems, updating and discretization of the interface models are significant to guarantee the overall numerical accuracy and stability of the co-simulation method. Accordingly, the interface models of the partitioned AC and DC networks are represented by time-varying Thevenin and Norton equivalents. To eliminate the aliasing or time delay errors, their parameters are derived using moving-window prediction, stepwise correction and averaging techniques. A numerical oscillation suppression algorithm is developed for the discretization of the interface model. Thus numerical stability is well guaranteed. The variables inside each subsystem as well as the interfaces, which are derived by augmented network equations (ANEs), are calculated simultaneously. The rate ratio of large AC and MTDC systems is determined based on our proposed criterion of electromagnetic transient (EMT) simulation accuracy. The effectiveness of the co-simulation method is validated on a practical system integrating large AC and modular multilevel converter (MMC) based MTDC grids.

Index Terms—Interface model, Interface error, Multirate cosimulation, MTDC system, Numerical stability.

## I. INTRODUCTION

M ODULAR multilevel converters (MMC) have receivedwide acceptance in high-voltage direct-current (HVDC) wide acceptance in high-voltage direct-current (HVDC) transmission schemes due to its additional benefits include simple realization of redundancy, low losses, and most importantly, easy extension to multi-terminal (MTDC) configurations [1]. Many MMC-based MTDC transmissions have been carried out in China in recent years, such as Zhoushan and Nanao Project [2]. Therefore, studying the interaction between MMC-based MTDC systems and AC systems has become an important subject. Electromagnetic transient (EMT) simulation is widely used for this purpose due to its capability of capturing the detailed dynamics of both converters and large AC systems [3]-[4].

Unfortunately, most established EMT software only allows users to simulate a large AC and MTDC system with the same time step, which is normally as small as several microseconds [3]. Such an unanimous small step would result in enormous computational burden. So it is generally insufficient for the conventional EMT software to simulate a huge AC system integrating MMC-based MTDC transmissions. Several system equivalent methods have been proposed to improve simulation efficiency. For instance, in [5], the DC grid is fully represented while the AC system is simplified into a fixed Norton or Thevenin equivalent. However, this method is of the obvious drawbacks of decreased accuracy and loss of nonlinear dynamics. Even worse, it would sometimes lead to misleading results [6]. MMC equivalent models, such as switch-function model [7], Thevenin equivalent model [8], have also been adopted for the same purpose. However, even if a simplified equivalent MMC model is used, the simulation would still be computationally cumbersome due to the huge scale of the external system. Therefore, a multirate co-simulation method is preferable when simulating large AC and MMC-based MTDC systems. In doing so, the entire system is divided into fast subsystems that contain MMC converters and slow subsystems including the AC systems. They each are simulated with different time steps instead of an unanimous one. As a result, computational efficiency can be considerably improved.

However, the modeling, updating and discretizing of the interfaces between different subsystems are key issues to guarantee the numerical accuracy and stability of the whole simulation. Typical multirate methods applied in power system EMT simulation include the waveform relaxation (WR) method [9] and the multi-area Thevenin equivalent (MATE) method [10]. One typical variation of multirate simulations is the hardware-in-the-loop (HIL) simulation [11], where these methods are particularly designed to improve the accuracy and efficiency of power electronic devices. Typical interface methods between subsystems include the ideal transformer (ITM) method [12], the time-variant first-order approximation (TFA) method [13], the transmission line (TLM) method [14], etc. One problem encountered for the WR method and those methods for HIL simulations are the errors caused by sampling (aliasing) or time delays. These errors are generally induced by interface variables, which are updated only on the occasion of re-synchronization that happens at the end of the largest time step. Since the contribution of the slow subsystem to the dynamics of the fast subsystem is either neglected or just taken into account after the longest time interval of all subsystems, sampling errors (aliasing errors) and time-delay errors would be introduced. These errors would even be exaggerated for subsystems with fast rates [15]. Specifically, the WR method uses the previous waveforms as the predicted values to calculate the current state for each subsystem. However, it cannot be simply applied in EMT simulations due to aliasing errors. Moreover, its convergence depends on the partitioning strategy used and the time intervals of re-synchronization [16]. As far as the MATE method is concerned, it solves each subsystem independently and then calculates the link currents using Thevenin equivalents. The aliasing errors can be reduced considerably with the linear interpolation [10]. But only simple electric circuits are tested on MATE. Its performance on practical power systems under large disturbances has not yet fully validated. In [17]-[19], a state-space nodal (SSN) method is proposed to simulate the MMCs in single-rate and multirate simulation environment successfully. The SSN method is a two layer method, where each subsystem is derived by state space equations and interfaces are further calculated by the global network equations. However, whether each subsystem can be derived by the nodal analysis approach is not given. More importantly, when studying the dynamic interactions between MTDC and AC grids, the capacitor voltages and arm currents are sensitive to the AC voltages of converters. Therefore, additional research is required to improve the accuracy of interfaces. Besides the issue of accuracy and efficiency, another noticeable point is the numerical stability of the interface model, which is vulnerable to numerical oscillation problems aroused by the diverse disturbances [20].

In this paper, a new multirate EMT co-simulation method is proposed and implemented in the cross-platform architecture, to analyze the interactions between large AC and MMC-based MTDC systems. Its salient features include:

1) the proposed method is a one-layer method, where the variables inside each subsystem as well as the interfaces, which are derived by augmented network equations (ANEs), are calculated simultaneously;

2) the interface models are represented with time-varying Thevenin and Norton equivalents so as to effectively eliminate the errors caused by aliasing and time delay. Where their model parameters can be efficiently derived using movingwindow prediction, stepwise correction and averaging techniques;

3) by incorporating the root-matching algorithm into the method for numerical oscillation suppression, the proposed method as a whole, which can be regarded as a hybrid simulation method, is highly efficient and easy to implement.

The rest of the paper is organized as follows: Section II presents the multirate EMT co-simulation method as a whole. The computation scheme of interface models is given in Section III. The selection of rate ratio is discussed in Section IV. And then Section V verifies the method on a practical MMC-based MTDC system. Brief conclusions are finally made in Section VI.

## II. MULTIRATE EMT CO-SIMULATION METHOD

The basic idea of the multirate EMT co-simulation method is to separate the entire system into an AC subsystem and several MTDC subsystems. Once partitioned, different subsystems are simulated in parallel to improve the simulation efficiency. The MTDC subsystems are simulated with an identical smaller integration step, while the AC subsystem is simulated with a larger integration step. For each subsystem, the dynamics of other neighboring subsystems are replaced with those of their interface models, which is represented with time-varying Thevenin or Norton equivalents. The variables of the interface models are predicted at an interval corresponding to the simulation step of each subsystems. And then they are corrected in a coordinated way when the largest iteration step is finished.

![](images/9c8438a48e1e6fa968064cb86e8f493e7eca3d33ae33f496f970a70d398567ee.jpg)  
Fig. 1. Network partitioning.

## A. Network Partitioning

The process of multirate co-simulation starts with the separation of the whole system into different subsystems. For network partitioning, two methods are widely used, namely transmission-line-based partitioning [14] and latency insertionbased partitioning [21]. The first method decouples the system at the end of the transmission line using the wave propagation delay [14]. So the length of the transmission line should be at least 15 to 30 km, corresponding to a time step of 50 µs to 100 µs. However, this is not always satisfied in practice [22]. The second method adds an artificial delay to separate the system. This probably makes the simulation less accurate or even unstable as the phase drift accumulates [20]-[21]. To address these issues, a different approach is used to partition the network more naturally, just by considering the different time scale of large AC and MTDC systems. As shown in Fig. 1, the whole system is split at the interconnection point of the AC and MTDC subsystems. For each subsystem, timevarying Thevenin and Norton equivalents are used to represent the dynamics of its neighboring subsystems. Generally, each MTDC subsystem contains power electronic modules that has much faster dynamics than AC power components. So they should be simulated with a faster rate. In contrast, simulation of the AC subsystem can be carried out with a slower rate.

The interactions between them are modeled as single- or multi-port circuits, through which the interface variables are conveyed during each step of EMT simulation. The impedance or admittance of each equivalent is given by

$$
\left\{ \begin{array} { l l } { \displaystyle z _ { f } ^ { l } = R _ { f } ^ { l } + j \omega L _ { f } ^ { l } , } \\ { \displaystyle y _ { f } ^ { l } = ( R _ { s } ^ { l } + j \omega L _ { s } ^ { l } ) ^ { - 1 } , } \end{array} \right.\tag{1}
$$

where $R ^ { l } , L ^ { l }$ are the equivalent resistance and inductance of the $l ^ { t h }$ interface; the subscripts f and s denote MTDC and AC subsystems, respectively. For simplicity, the superscript l will be omitted hereinafter if not specially mentioned. Our proposed interface model originates from the TFA model and the ITM model. The time-varying Thevenin and Norton equivalents are added to enhance the numerical stability of the interface model [11]. Parameters of the time-varying Thevenin and Norton equivalents are derived by Gaussian elimination.

Correspondingly, the differential equation of the interface in each MTDC subsystem is written as

$$
\frac { d } { d t } i _ { f } = \left[ L _ { f } \right] ^ { - 1 } ( \nu _ { f } - R _ { f } i _ { f } - u _ { f } ) ,\tag{2}
$$

where $i _ { f } , v _ { f }$ are the voltages and currents of the interface; $u _ { f }$ is the parameters of the Thevenin voltage, and its updating method should be specially designed.

After discretized by the root matching algorithm, (2) is derived as

$$
\begin{array} { r } { \nu _ { f } ( t _ { k } + i h ) = \alpha ^ { - 1 } \{ i _ { f } ( t _ { k } + i h ) } \\ { + \beta i _ { f } [ t _ { k } + ( i - 1 ) h ] \} + u _ { f } ( t _ { k } + i h ) , } \end{array}\tag{3}
$$

where

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \alpha = 1 - e ^ { - R _ { f } h / L _ { f } } , } \\ { \beta = e ^ { - R _ { f } h / L _ { f } } . } \end{array} \right. } \end{array}\tag{4}
$$

And $t _ { k }$ is the $k ^ { t h }$ steps of AC subsystem; h is the time step of the MTDC subsystem; $t _ { k } + i h , i = 1 , 2 . . . ,$ n refers to $i ^ { t h }$ sub-step between $\left[ t _ { k } , t _ { k + 1 } \right]$ . At each sub-step, parameters of interfaces in the MTDC subsystems should be updated.

(3) is rewritten as the impedance and equivalent voltage term, i.e., $Z _ { f } , \nu _ { h , f } ( t _ { k } + i h )$

$$
\nu _ { f } ( t _ { k } + i h ) = Z _ { f } i _ { f } ( t _ { k } + i h ) + \nu _ { h , f } ( t _ { k } + i h ) ,\tag{5}
$$

where

$$
\left\{ \begin{array} { l l } { \displaystyle Z _ { f } = \alpha ^ { - 1 } , } \\ { \nu _ { h , f } ( t _ { k } + i h ) = \alpha ^ { - 1 } \beta i _ { f } [ t _ { k } + ( i - 1 ) h ] } \\ { + u _ { f } ( t _ { k } + i h ) } \end{array} \right.\tag{6}
$$

Finally, according to Kirchhoff’s laws, the updating equation for each MTDC subsystem is rewritten as:

$$
\left[ \begin{array} { c c } { \tilde { G } _ { f } } & { I } \\ { - I } & { Z _ { f } } \end{array} \right] \left[ \begin{array} { c } { \tilde { \nu } _ { f } ( t _ { k } + i h ) } \\ { i _ { f } ( t _ { k } + i h ) } \end{array} \right] = \left[ \begin{array} { c } { \tilde { i } _ { h , f } ( t _ { k } + i h ) } \\ { \nu _ { h , f } ( t _ { k } + i h ) } \end{array} \right] ,\tag{7}
$$

where $\tilde { G } _ { f } , \tilde { i } _ { h , f } ( t _ { k } + i h )$ is the conductance matrix and equivalent current vector inside the MTDC subsystem; $\tilde { v } _ { h , f } ( t _ { k } + i h )$

![](images/e42b9f5891041b04956c68ab283f51041ea8f8650f01e7aa4564a56a3be49c6a.jpg)  
Fig. 2. Flow chart of the multirate co-simulation method.

is the node voltage vector inside the MTDC subsystem;   
$i _ { f } ( t _ { k } + i h )$ is the interface current.

Similarly, the updating equation for the AC subsystem is written as:

$$
[ \tilde { G } _ { s } + G _ { s } ] \nu _ { s } ( t _ { k } ) = \tilde { i } _ { h , s } ( t _ { k } ) + i _ { h , s } ( t _ { k } ) ,\tag{8}
$$

where $\tilde { G } _ { s } , \tilde { i } _ { h , s } ( t _ { k } )$ are the conductance matrix and the equivalent current vector inside the AC subsystem; $G _ { s } , i _ { h , s } ( t _ { k } )$ is the conductance and equivalent current terms of interfaces; $v _ { s } ( t _ { k } )$ are the node voltage vector of the AC subsystem. (7)- (8) constitutes the the proposed ANEs.

## B. Framework of the Co-simulation Method

Fig. 2 illustrates the framework of the co-simulation method. The target system is first initialized based on power flow calculations and next partitioned into an AC and several MTDC subsystems. Then all the MTDC subsystems are simulated with an identical smaller step h, while the AC subsystem is simulated with a larger step $h _ { a c }$ . The rate ratio is defined as $n = h _ { a c } / h$ . The simulations of the decoupled AC and MTDC subsystems are carried out in parallel but independently based on their common starting points.

For the AC subsystem, all its neighboring DC subsystems are replaced with time-varying Norton equivalents, the parameters of which are calculated by averaging the results of the previous iteration. During the current step, only a single iterative operation is required to advance the simulation to the next time interval, or from $t _ { k } \mathrm { ~ t o ~ } t _ { k + 1 }$ , where $t _ { k } , \ t _ { k + 1 }$ refer to the simulation time of $k ^ { t h }$ and $k + 1 ^ { t h }$ steps in the AC subsystem.

Meanwhile, for the DC subsystems, their interface models are represented with time-varying Thevenin equivalents. The simulation from $t _ { k }$ to $t _ { k + 1 }$ are divided into n sub-steps, namely $t _ { k } + i h$ $i = 1 , 2 , . . . n .$ At each subs-step, the parameters of the interface model are predicted by moving-window prediction.

After completing both types of iterations, a coupled operation called coordination is executed to exchange interactive signals, update interface variables and correct the simulation results if necessary.

Such decoupled and coupled iterations are continued until the predefined simulation time $( T _ { m a x } )$ is reached. Finally, the EMT simulation is fulfilled and the obtained results are output.

Noticeably, several key issues should be properly addressed in order to implement the multirate co-simulation method: 1) how to coordinate or update the interface parameters so as to effectively eliminate simulation errors caused by aliasing and time delay; 2) how to discretize the interface model so as to guarantee numerical stability; and 3) how to determine the rate ratio n so as to improve the efficiency as well as accuracy. The following section deals with the first two issues and the third issue will be discussed in Section IV.

## III. COMPUTATION SCHEME FOR THE INTERFACE MODELS

## A. Update of Interface Models

The interface models are illustrated in Fig. 1. For the simulation of the DC subsystem, its connected AC subsystem is equivalent to a time-varying Thevenin source $u _ { f }$ , complemented with a network equivalent $z _ { f } .$ . Correspondingly, to solve the AC subsystem, each of its neighboring MTDC subsystems is transformed into a changing Norton equivalent including a current source $i _ { s }$ and an admittance $y _ { s } .$ . At each simulation step, these interface variables should be properly updated and coordinated in order to reflect the interaction between AC and DC subsystems. So the strategy of such a update operation is essential to achieve efficient and precise simulation of the whole system.

1) Update of the Thevenin equivalents: As shown in Fig. 2, the simulation of each MTDC subsystem from step $t _ { k }$ to step $t _ { k + 1 }$ is fulfilled with n sub-steps, namely $t _ { k } + i h , \ i = 1 , 2 , . . . n$ To improve simulation accuracy as well as numerical stability, the interface variables should be properly updated at each substep. Generally, the equivalent Thevenin impedance remain almost constant and is not necessary to refresh except there is a topological change in the neighboring AC subsystem (if this is the case, a new Thevenin impedance can be obtained from the bus impedance matrix). But the Thevenin voltage should be continuously updated to reflect the constantly changing external dynamics. Otherwise, the time delay would cause apparent numerical errors, which in turn would be exaggerated during the solution of the MTDC subsystems [23]. To solve this problem, the proposed method uses moving-window prediction and stepwise correction to update the Thevenin voltage.

As shown in Fig. 3, a moving window consisting of m latest Thevenin voltages, or $u _ { f } ( t _ { k } - m ) , \dots u _ { f } ( t _ { k } - 1 )$ , is employed first to get the following piecewise cubic spline functions during the n sub-steps:

![](images/86212be3d866bd19cc5ee68cb27b7ad4e254dc3777c3b5503541ccb4848bae53.jpg)  
Fig. 3. Illustration of Moving-window prediction and linear prediction.

$$
\begin{array} { r l } & { F _ { i } ( t ) = \frac { [ t _ { k } + ( i - 1 ) h - t ] ^ { 3 } M _ { i - 2 } + [ t - t _ { k - 1 } - ( i - 2 ) h ] ^ { 3 } M _ { i - 1 } } { 6 h } + } \\ & { \frac { [ t _ { k } + ( i - 1 ) h - t ] u _ { f } [ t _ { k } + ( i - 2 ) h ] + [ t - t _ { k - 1 } - ( i - 2 ) h ] u _ { f } [ t _ { k } + ( i - 1 ) h ] } { h } } \\ & { - \frac { h \{ [ t _ { k } + ( i - 1 ) h - t ] M _ { i - 2 } + [ t - t _ { k } - ( i - 2 ) h ] M _ { i - 1 } \} } { 6 } , i = 1 , 2 . . . n , } \end{array}\tag{9}
$$

where t stands for a certain sub-step; $\begin{array} { r l } { M _ { i } } & { { } = } \end{array}$ $d ^ { 2 } \left[ u _ { f } ( n _ { k } + i h ) \right] / d t ^ { 2 }$ are parameters that can be derived by solving the tridiagonal matrix equation [25]; $u _ { f } [ t _ { k } + ( i - 2 ) h ] , u _ { f } [ t _ { k } + ( i - 1 ) h ]$ are previously obtained Thevenin voltages; $t _ { k }$ denotes the simulation time of $k ^ { t h }$ step.

As shown in Fig. 3, then the new Thevenin voltage for each sub-step can be calculated using spline interpolation, or

$$
\tilde { u } _ { f } ( t _ { k } + i h ) = F _ { i } ( t _ { k } + i h ) , i = 1 , 2 . . . n ,\tag{10}
$$

The errors of Thevenin voltages are quantified as

$$
\tilde { e } ( t _ { k } + i h ) = | | u _ { f } ( t _ { k } + i h ) - \tilde { u } _ { f } ( t _ { k } + i h ) | | .\tag{11}
$$

According to [24],

$$
\tilde { e } ( t _ { k } + i h ) = \leq \frac { h ^ { 4 } } { 4 ! } m a x | | u _ { f } ^ { ( 4 ) } ( t _ { k } + i h ) | | , i = 1 , 2 . . . n .\tag{12}
$$

That is to say, the predicted Thevenin has fourth-order accuracy. For comparison, the linear prediction (LP) technique is also illustrated in Fig. 3. Their performances will be detailed in Section V.

At the end of each step, the Thevenin voltages should be further adjusted to include the interactions between different interfaces. This is done with the so-called stepwise correction. Suppose a Thevenin impedance matrix $Z _ { I n t } = \{ Z _ { i j } , ~ i , j =$ $1 , 2 , . . . N \}$ is derived with the Gaussian elimination technique from the system impedance matrix by only keeping the interface buses. The Thevenin voltage is revised as

$$
\begin{array} { l c l } { { u _ { f } ^ { l } ( t _ { k + 1 } ) } } & { { = } } & { { \tilde { u } _ { f } ^ { l } ( t _ { k + 1 } ) + \Delta u _ { f } ^ { l } ( t _ { k + 1 } ) } } \\ { { } } & { { = } } & { { \tilde { u } _ { f } ^ { l } ( t _ { k + 1 } ) + { \textstyle \sum _ { m = 1 , m \ne l } ^ { N } } Z _ { l m } i _ { f } ^ { m } ( t _ { k + 1 } ) , } } \end{array}\tag{13}
$$

where $\tilde { u } _ { f } ^ { l } ( t _ { k + 1 } )$ is the new Thevenin voltage at time $t _ { k + 1 } ;$ $i _ { f } ^ { m } ( t _ { k + 1 } )$ is the interface current of the $m ^ { t h }$ interface, as shown in Fig. 1.

2) Update of Norton equivalents: Similarly, Norton currents are updated during each simulation step for the AC subsystem,

however with a much simpler averaging technique as in (3) [10]-[15].

$$
i _ { s } \left( n _ { k + 1 } \right) = \frac 1 n \sum _ { m = 0 } ^ { n - 1 } i _ { f } ( t _ { k } + m h ) ,\tag{14}
$$

where $i _ { f } ( t _ { k } + m h )$ ， $m = 0 , 1 , . . . n - 1$ are interface currents obtained at each simulation sub-steps of the MTDC subsystem. This technique prevents the quasi-randomness or spikes, when only taking into account the single value of the last calculated solution of the fast MTDC subsystems [10].

## B. Discretization of Interface Models

The simulation of each subsystem is carried out in independent EMT programs, where Trapezoidal (TR) approximation is used to discretize the AC and DC subsystems. As is known that TR algorithm tends to cause undesirable numerical oscillation in the case of abrupt disturbances [26]. The EMT program, such as PSCAD/EMTDC, has embedded interpolation method [27] to suppress such numerical oscillation. For the interface model, however, TR algorithm cannot be used due to the lack of mechanism to detect and mitigate the possible numerical oscillation [26]. Instead, we try to develop a new hybrid simulation method with the intention of requiring little modification of EMT models and suppressing numerical oscillations. According to [28]-[29], the root matching algorithm is selected to discrete the interface models due to its ability to suppress the numerical oscillation and higher accuracy than the backward algorithm. And the rest of the systems is still discretized by the efficient TR algorithm. Since most of the systems is discretized with the efficient TR algorithm and only the interface models is solved with root matching algorithm, the proposed method as a whole, which can be regarded as a hybrid simulation method, is highly efficient and easy to implement.

## IV. SELECTION OF THE OPTIMAL RATE RATIO

The optimal rate ratio n should be properly determined to achieve efficient and accurate simulations. For the MMC-based MTDC subsystem, the time step h is determined according to the total sub-module number of each MMC arm, the modulation ratio and the fundamental frequency of the MTDC subsystem. In our simulation, each MMC is represented with an arm equivalent model [30] instead of the detailed switch model. So the step size can be set as $h = 5 0$ µs to keep a good balance between accuracy and efficiency [30].

With h settled, the time step of the AC subsystem, or $h _ { a c } =$ nh, is only governed by the rate ratio n. It is selected in the light of two criteria: 1) $n \leq h _ { a c , m a x } / h .$ , where $h _ { a c , m a x }$ is the maximum time step that can maintain numerical stability of the AC subsystem; 2) n should be properly chosen to make the simulation accuracy of the AC subsystem consistent with that of the MTDC subsystem.

To implement the second criterion, an index namely impedance ratio is proposed to compare the simulation accuracy between AC and MTDC subsystems. It is calculated by the following several steps.

First, based on the discretized model of its own, the impedances of typical branches in either MTDC or AC subsystems can be derived. Taking an RL branch as an example, its differential equation is

$$
u - R i = L { \frac { d i } { d T } } ,\tag{15}
$$

where R, L are branch parameters.

If this RL branch is located in the AC subsystem, it is discretized using the TR algorithm. (15) becomes

$$
( R + \frac { 2 L } { n h } ) i ( t _ { k + 1 } ) + ( R - \frac { 2 L } { n h } ) i ( t _ { k } ) = u ( t _ { k + 1 } ) + u ( t _ { k } ) ,\tag{16}
$$

where $u ( t _ { k } ) , i ( t _ { k } )$ are discrete voltage and current at the simulation time tk.

The AC impedance is given by

$$
Z _ { a c } = \frac { \hat { u } } { \hat { i } } = \frac { ( R + \frac { 2 L } { n h } ) + ( R - \frac { 2 L } { n h } ) z ^ { - n } } { 1 + z ^ { - n } } ,\tag{17}
$$

where $\hat { u } , \hat { i }$ are the Fourier transform of the voltage and current and $z = e ^ { j \omega h }$

However, if the same RL branch is placed in the MTDC subsystem, after discretized within the same time interval [tk, $t _ { k + 1 } ]$ , it changes to

$$
\begin{array} { r l } & { \frac { 1 } { 2 } \left[ u ( t _ { k + 1 } ) - R i ( t _ { k + 1 } ) + u ( t _ { k } ) - R i ( t _ { k } ) \right] } \\ & { + \displaystyle \sum _ { m = 1 } ^ { n - 1 } \left[ u ( t _ { k } + m h ) - R i ( t _ { k } + m h ) \right] = \frac { L } { h } [ i ( t _ { k + 1 } ) - i ( t _ { k } ) ] . } \end{array}\tag{18}
$$

A similar impedance in the MTDC subsystem is derived as

$$
Z _ { d c } = \frac { \hat { u } } { \hat { i } } = \frac { \frac { L } { h } \big ( z ^ { n } - 1 \big ) + \frac { R } { 2 } \big ( 1 + z ^ { n } \big ) + R \sum _ { m = 1 } ^ { n - 1 } z ^ { m } } { \frac { 1 } { 2 } \big ( 1 + z ^ { n } \big ) + \sum _ { m = 1 } ^ { n - 1 } z ^ { m } } .\tag{19}
$$

Then, the impedance ratio is defined as $\varsigma ( n , \omega ) = Z _ { a c } / Z _ { d c }$ and when $R \to 0 ,$ , it can be simplified into

$$
\operatorname* { l i m } _ { R  0 } \varsigma ( n , \omega ) = [ ( 1 + z ^ { n } ) + 2 \sum _ { m = 1 } ^ { n - 1 } z ^ { m } ] / [ n \cdot ( 1 + z ^ { n } ) ] .\tag{20}
$$

The impedance ratio is used to measure the consistence of simulation accuracy among different subsystems. The closer $| \varsigma ( n , \omega )$ | is to unity, the more consistent the compared simulation accuracy becomes. (20) implies that $\varsigma ( n , \omega )$ only depends on the rate ratio (n) and the frequency (ω) provided that the branch resistance is sufficiently small (this generally holds for power networks). Similar observations can be made for other types of branch, such as RC branches or transmission lines. It should be noted that when selecting the rate ratio $n ,$ the models in the slow AC subsystem are represented by their simplified models [32]. Therein, the transmission line is represented by the PI model; transformers are represented by suitable leakage inductances and generators by transient inductances.

So, finally to follow the second criterion, the rate ration should satisfy

$$
0 . 9 \leq | \varsigma ( n , \omega ) | \leq 1 . 1 , \ \omega \in [ 0 , 0 . 2 f _ { N y } ] ,\tag{21}
$$

where $f _ { N y }$ is the Nyquist frequency; and the maximum frequency concerned is $0 . 2 f _ { N y }$ [31]. It should be noted that

![](images/df3f86f7c670b856eb1099489c4879d90fe65a528978f3a5f5c5d27878a1d7eb.jpg)  
Fig. 4. Partitioning of the studied power system

the proposed criterion is equivalent that proposed in [9] mathematically, however our criterion preserves better physical meanings.

## V. CASE STUDIES

## A. Case Study Settings

To evaluate the performance of the multirate co-simulation method, a practical MMC-based HVDC project is used as the target system for case studies [33]. Its schematic diagram is shown in Fig. 4. The 36-bus AC system has 8 generators. A four-terminal 400kV MMC-MTDC system is connected to the AC systems at Bus 10 and Bus 32. Each MMC has 250 halfbridge sub-modules in a single arm. MMC2 regulates the DC voltage while other MMCs control power flowing into or out of the DC grid. Parameters of MTDC subsystems are given in Appendix. For EMT simulation, generators are represented by classical $d q 0$ models [34] and MMCs are represented by the arm equivalent models with DC-fault blocking capability [30].

## B. Implementation of the Co-simulation Method

The whole system is firstly partitioned at the interconnection point of the AC and MTDC subsystems. Then, to implement the simulation function, a cross-platform architecture is developed. As illustrated in Fig. 5, it is made up of three part: the commercial PSCAD/EMTDC software used for the simulation of MTDC subsystems, a specially designed EMT simulator for the AC subsystem, and a coordinator between them. As the key part of the co-simulation platform, the coordinator has two basic functions for the interface models: 1) an interface parameter calculator to update model parameters, and 2) a network equivalent calculator to discretize the Thevenin and Norton equivalents. The coordinator is also responsible for the exchange of interactive signals and the correction of simulation results if necessary. All the three parts of the co-simulation platform have their own communication modules to exchange data and information. The communication network can be realized by Socket, shared memory techniques [35].

![](images/7d975e0bb3c01dc69e9d37836533fe9d1a5e6f1bb6fc73cf42a1c44bdd989633.jpg)  
Fig. 5. The developed cross-platform architecture for the multirate cosimulation.

As discussed in Section IV, the time step for MTDC subsystems is 50 µs. And the maximum step of AC subsystem or $h _ { a c , m a x } ,$ is normally 500µs, due to the numerical stability criterion [31]. Thus the rate ratio n should be a number less than 10. Fig. 6 show the impedance ratio of two typical branches (RL and RC) varying with rate ratio and frequency. It can be seen that, in our special case, when n is between 2 and 6, the criterion of accuracy consistence (10) can be satisfied. Naturally, the most efficient rate ratio should be 6.

![](images/258ad77235a0c45856fd2ff1833abab9963104623cf6db013e4e25049b89aeec.jpg)

![](images/a65b57682470fb8e85771be32792ee03e165aa6767969ab502ed2e71cc76dc48.jpg)  
Fig. 6. The impedance ratio varying with rate ratio and frequency.

## C. Comparisons of the Updating Techniques for Thevenin Equivalents

Different updating techniques of Thevenin equivalents are compared. As an example, Fig. 7 shows the voltages of Bus 10 and the AC terminal of MMC1. They are obtained with our method (moving-window prediction and stepwise correction), line-prediction (LP) method and the method without time delay correction [23], respectively. As a reference, the results obtained by simulating the whole system with an unanimous time step of 50µs are also displayed in the figure with the legends of $\mathrm { \Delta ^ { 6 6 } }$ . From these curves, it can be seen that the proposed method can effectively suppress errors caused by time delays and has higher accuracy than other methods. However, when the rate ratio as an integer is above 6, unacceptable errors will be produced. Therefore, to meet the accuracy requirement the rate ratio is recommended to be 6.

![](images/58d2cde871e7fcb921b280a73a9b5f396fe7ed413b6ba09927989b5bee856eb7.jpg)

![](images/bbdbc13d3970f1a5454d5833440abf170fe5de062509ee78b1ba301d86e3b8da.jpg)  
Fig. 7. Voltages obtained with different updating techniques for the Thevenin Equivalents.

![](images/4fcae114ac0ec0ae8043429f295e5df35e892b4db84bef9b2854f7b50a84847d.jpg)  
Fig. 8. Voltages of the interface Bus 10 following a three-phase-to-ground fault.

## D. Comparisons of the Discretization Methods for Interface Models

A temporary three-phase-to-ground fault is triggered on Bus 9 to check the numerical stability of the interface models. As shown in Fig. 8, the voltages of Bus 10 obtained with the discretization method of traditional and proposed method are compared. Here, the interfaces of traditional/proposed method are discretized by the trapezoidal/root matching algorithm, respectively. Obviously, the traditional method causes numerical oscillation immediately after the switch-off of circuit breaker. In contrast, the proposed suppress numerical oscillation effectively and produce results that are highly consistent with the reference.

![](images/cca015e5a21774ea58021d423b1418f9f15cc48deab8eff43d2b5ff613c0def3.jpg)

![](images/b98108f9dac0d7ef8a0ed467db7b06af5a18d12b80b7457eac29b70fef35325a.jpg)

![](images/d4df3cb0c17a51d500438a23e9c8e35f904c0b61840d8aa8316f57cc98970de5.jpg)  
Fig. 9. DC currents and voltages of MMC converters following the fault .

The DC currents and voltages of MMC converters following the fault are shown in Fig. 9, which also confirm the proposed method’s advantage in achieving higher simulation accuracy than the traditional method.

## E. Accuracy and Efficiency of the Proposed Method

As a case study, a DC line fault is triggered to demonstrate the accuracy and efficiency of the proposed multirate cosimulation method. At the time $t = 2 . 0 s .$ , the fault occurs on DC line 1. As a result, the DC voltage drops dramatically and the fault current grows rapidly. When the current threshold (three times of the rated dc-link current [36]) is reached, the protection scheme block all MMCs immediately. Thus MMC operates in the rectifier mode until at t = 2.1s the AC circuit breaker (CB) opens to isolate the MMCs. After another 0.1 s, the DC fault is cleared. Next, the AC CBs reclose at t = 2.3s and the AC voltages of MMC is restored. After t = 2.5s, all MMCs are restarted sequentially. MMC2 is powered first to reestablish the DC voltage. Other MMCs follow to increase their input/output to the preset loading levels. Finally, the whole system returns to its steady state at about t = 2.7s.

Cases of short (10km) interface lines and long (200km) interface lines are shown in Figs. 10-14. Here, “TLM” is referred to the TLM method [11]. The improvement in accuracy of the proposed method for the short interface line is more obvious than that for the long interface line. Take the AC voltages as an example, the maximum errors of the proposed/TLM method for the short interface line are 0.0523/0.2677 pu; and those of the proposed/TLM method for the long interface line are 0.0315/0.1981 pu. The reason for such improvement is that: the TLM method is less accurate when the interface circuit is a short transmission line [14]. Unlike the TLM method, our proposed method calculate the current time value of Thevenin voltage based on the moving-window prediction technique. Thus, the time delay errors are reduced. Also, the interactions between different interfaces are reflected in our proposed interface model by the stepwise correction technique.

![](images/217d2dde857833fa999c6c1523a287caf29f6b7febd15498b8c251c39e0a307a.jpg)

![](images/3d86edc1a8c1f268dcf20156ad3f89d6b33bf48f79de212283f7da6bc68ebfd6.jpg)  
Fig. 10. DC current (short interface lines).

![](images/ea2671f2e2de258bea385380c398c509af61acf191ff85b396f69d9a6d82115d.jpg)

![](images/1b4a9c519ee1533a43bf580f45652ef2dbb6280593959f0877dd0c37801c68f6.jpg)

![](images/a6a7eeba8938bd6dfd756ee83ba2b17f8cf8c0f1ab788cd16310918a8ba15a7b.jpg)

![](images/744ba4dd149daeab5347c273c6fdfabae0d1d13c4c6eced5ec91f9656a51fff2.jpg)  
Fig. 11. AC voltage and DC voltage of MMC1(short interface lines)

![](images/7159e353fcaf7a025f6a469047deca8c4bdf8fcbe963f742311e061fdbd64a9a.jpg)

![](images/a1f12e5e7f6311b4e217f620014e19dca657ed1ef73e447d21f8879c2c89cfec.jpg)

![](images/dd61807f9ed07ba484248ed5853c691b6aa43311dcd0ea4492aa983bb0ffd6ee.jpg)

![](images/96e364846ca11842ec654885b1a1a0e7824eb00e81e0b11343d877ba3a7a4873.jpg)

![](images/c53ccadbc730729360ca10ad981b4581f993fbc6300716b3ea48a00ddc3db637.jpg)  
Fig. 12. AC voltage and DC voltage of MMC1(long interface lines)

![](images/20f9b4bf6ab891dbc91216b399f20def677c689b2cf0c51a7fd116cef77e1251.jpg)

![](images/72cec42836021cbb1d67d361e2016b16d1258e08fd1a086e8ace56a131c07543.jpg)

![](images/3d3da4c20708ef1648245d982c4d7342fc3c2a06a7d23d65b3abcca777af58a4.jpg)

![](images/0f1e28196a51da76c4a7caf2a7c89b7c86c8f18933312200d0de926d0c342ef3.jpg)  
Fig. 13. Arm voltages and capacitor voltages of MMC1(short interface lines)

![](images/f8433a86daeaea66beeea014c8d45c93a509cbef81f8c04fbaceef80dba603d8.jpg)

![](images/7441f1e5f0eedcb0e67a373ddcfd31b0888a0117a493c1775c2976949627f1b2.jpg)

![](images/ecec8afab19b9ad1bd903867c587722d44dd42363bb722d0086177fcdcf9047a.jpg)  
Fig. 14. Arm voltages and capacitor voltages of MMC1(long interface lines)

![](images/254477c69d2ac12ebe4775104df3e7b7cbf50a49c5e16ecbcd0f28a6ec18e560.jpg)

![](images/8d928667f2c905bb22e2fcb99da49b5ffff702a70af23894865ecfcd27712239.jpg)

TABLE I  
COMPARISON OF CPU TIME AND AVERAGE SIMULATION ERRORS (UNIT: IN PU) WITH DIFFERENT RATE RATIOS (PROPOSED METHOD:SHORT INTERFACE LINE)
<table><tr><td rowspan="2">Rate ratio n CPU Time/s</td><td rowspan="2"></td><td rowspan="2">AC subsystem variables  $U _ { 8 A }$ </td><td colspan="2">Interface variable</td><td colspan="2">DC subsystem variables</td><td colspan="3">DC subsystem MMC variables</td></tr><tr><td> $U _ { 1 0 A }$ </td><td>I9-10A</td><td> $\underline { { I _ { d c - M M C 1 } } }$ </td><td> $\underline { { U _ { d c - M M C 1 } } }$ </td><td> $U _ { a p - M M C 1 }$ </td><td> $\underline { { I _ { a r m - M M C 1 } } }$ </td><td> $\underline { { U _ { c - M M C 1 } } }$ </td></tr><tr><td>1</td><td>5925</td><td>/</td><td>/</td><td>/</td><td>/</td><td>/</td><td>/</td><td>/</td><td>/</td></tr><tr><td>2</td><td>2370</td><td>0.006</td><td>0.013</td><td>0.023</td><td>0.011</td><td>0.011</td><td>0.005</td><td>0.005</td><td>0.005</td></tr><tr><td>3</td><td>799</td><td>0.012</td><td>0.018</td><td>0.026</td><td>0.017</td><td>0.012</td><td>0.011</td><td>0.006</td><td>0.008</td></tr><tr><td>4</td><td>680</td><td>0.017</td><td>0.024</td><td>0.032</td><td>0.019</td><td>0.013</td><td>0.017</td><td>0.009</td><td>0.009</td></tr><tr><td>5</td><td>530</td><td>0.023</td><td>0.031</td><td>0.039</td><td>0.022</td><td>0.014</td><td>0.021</td><td>0.012</td><td>0.012</td></tr><tr><td>6</td><td>450</td><td>0.050</td><td>0.037</td><td>0.043</td><td>0.026</td><td>0.017</td><td>0.026</td><td>0.014</td><td>0.013</td></tr></table>

TABLE II

COMPARISON OF CPU TIME AND AVERAGE SIMULATION ERRORS (UNIT: IN PU) WITH DIFFERENT RATE RATIOS (TLM METHOD:SHORT INTERFACE LINE)
<table><tr><td rowspan="2">Rate ratio n CPU Time/s</td><td rowspan="2"></td><td rowspan="2">AC subsystem variables  $U _ { 8 A }$ </td><td colspan="2">Interface variable</td><td colspan="2">DC subsystem variables</td><td colspan="3">DC subsystem MMC variables</td></tr><tr><td> $U _ { 1 0 A }$ </td><td> $I _ { 9 - 1 0 A }$ </td><td> $\underline { { I _ { d c - M M C 1 } } }$ </td><td> $\underline { { U _ { d c - M M C 1 } } }$ </td><td> $U _ { a p - M M C 1 }$ </td><td> $\underline { { I _ { a r m - M M C 1 } } }$ </td><td> $\underline { { U _ { c - M M C 1 } } }$ </td></tr><tr><td>1</td><td>5925</td><td>/</td><td>/</td><td>/</td><td>/</td><td>1</td><td>/</td><td>/</td><td>/</td></tr><tr><td>2</td><td>2573</td><td>0.014</td><td>0.023</td><td>0.037</td><td>0.012</td><td>0.014</td><td>0.009</td><td>0.006</td><td>0.006</td></tr><tr><td>3</td><td>811</td><td>0.021</td><td>0.044</td><td>0.042</td><td>0.018</td><td>0.015</td><td>0.019</td><td>0.007</td><td>0.008</td></tr><tr><td>4</td><td>694</td><td>0.027</td><td>0.058</td><td>0.052</td><td>0.020</td><td>0.016</td><td>0.023</td><td>0.010</td><td>0.009</td></tr><tr><td>5</td><td>520</td><td>0.040</td><td>0.074</td><td>0.063</td><td>0.023</td><td>0.018</td><td>0.028</td><td>0.013</td><td>0.012</td></tr><tr><td>6</td><td>474</td><td>0.084</td><td>0.092</td><td>0.070</td><td>0.028</td><td>0.021</td><td>0.031</td><td>0.018</td><td>0.012</td></tr></table>

Simulation outputs of the quantities at the boundaries, i.e., curves of Gen 8 are shown in Figs. 15 and 16. It is shown that the proposed method is more accurate the traditional method.

![](images/1ceebebda9926f7fcc3ee7e8a649923a14eaaf343eb45aceec7b3ad733eb9988.jpg)  
Fig. 15. Power curves of G8.

![](images/d102a59effc3d212a7342559ec02b282073b48424c3f02ce4dcb9602dda7534d.jpg)  
Fig. 16. Angular velocity of G8.

To quantify the accuracy, a metric called average simulation error is defined as

$$
E _ { a \nu g } = \frac { 1 } { N } \sum _ { i = 1 } ^ { N } | x _ { i , \mathrm { { m } } } - x _ { i , \mathrm { { u } } } | ,\tag{22}
$$

where $x _ { i , m } , x _ { i , u }$ are the $i ^ { t h }$ sample of the monitored variable x in per unit that are produced by the multirate and unanimous-rate simulations respectively; N is the number of the samples.

With different rate ratios, the average simulation errors and CPU time with short interface lines are given in Tables I (proposed method) and Table II (TLM method), where $n = 1$ corresponds to the unanimous time step or the reference case. It is found that as the rate ratio n increases, the CPU times of both the proposed method and TLM method drop dramatically while the average simulation errors become a little bit larger. For the proposed method, when the proposed rate ratio is used or $n = 6 .$ , the multirate simulation spends only 450s. But it takes about 5925s for the method with the unanimous step (or $n { = } 1 )$ . In other words, the proposed multirate method is more than 13 times faster. Since the root matching and trapezoidal algorithms are both single-step algorithms. With the proposed method, only the interfaces are solved with root matching algorithm. This does not add much computation burden. So the simulation efficiency of the proposed method is comparable with TLM method. However, the proposed method gains more advantages in simulation accuracy than the TLM method, especially for the short interface circuits. As shown in Tables I and II, the average simulation errors of the interface voltage (U10A) for the proposed/TLM method are about 0.037/0.092 pu, respectively.

## VI. COMPARISONS ON UPDATING OF INTERFACES

The accuracy of the interfaces is important when studying the dynamic interactions between the MTDC and AC grids, as the capacitor voltages and arm currents are sensitive to the AC voltages of converters [37]. For our proposed method, different updating techniques of interface parameters during the transient state are further compared based on the practical scenario, which is the same as that in Section V(E). Fig. 17 shows that significant errors caused by time delay will be produced if the moving window prediction technique is not adopted. As shown in Fig. 18, errors of both methods will increase as the rate ratio n rises. However, with the proposed moving window prediction technique, errors of interface voltages has been reduced almost 4 times and are all below 0.03 pu.

![](images/30445f7b2aec1bcf705a657346441a5142472f18a49bc9df3268f7a9d15ea9d2.jpg)  
Fig. 17. Voltages obtained with/without time delay correction technique.

![](images/e854c62f6606822e4c402e577f02e6822dbc55118498a801469662d7e2294f9a.jpg)  
Fig. 18. $E _ { a \nu g }$ versus rate ratio n curves with/without time delay correction technique.

According to Fig. 4, the self- and mutual impedances of interfaces are given in Table III. As shown in Fig. 19, the proposed method has significant improved accuracy when considering interactions between different interfaces using the stepwise technique. This advantage is even more pronounced after the fault is cleared. The underlying reason for such improvement is that: the parameters of interfaces have fully considered the impact between different interfaces and thus the Thevenin voltages will be more accurate.

TABLE III  
SELF- AND MUTUAL IMPEDANCES OF INTERFACES
<table><tr><td colspan="2">self impedances/Ω</td><td rowspan="2">mutual impedance/Ω</td></tr><tr><td>interface bus 10</td><td>interface bus 32</td></tr><tr><td>1.95+j36.16</td><td>2.31+j28.18</td><td>37.39+j146.32</td></tr></table>

Fig. 20 shows the $E _ { a \nu g }$ versus magintudes of self-/mutual impedance curves with/without the stepwise correction technique. As can be seen, with the stepwise corection technique, errors of interface voltages have been reduced significantly. Moreover, $E _ { a \nu g }$ will increase as the magnitude of self-/mutualimpedances drops. That is to say, when the magnitude of self-/mutual- impedances is small, the interactions between interfaces cannot be neglected. Thus, the stepwise correction technique is important to improve the accuracy of the interfaces.

![](images/8ebd4e9db8e6455a3b033d364e2ad95038308a2ac3ec62b4828adbdb5bea2daf.jpg)

Fig. 19. Voltages obtained with/without stepwise correction technique.  
![](images/25d4cdf15bf2ab7257b18489d330f7e3c9a71b5467e2b1df799c187c37503527.jpg)  
Fig. 20. $E _ { a \nu g }$ versus self-/mutual- impedance curves with/without stepwise correction technique.

Table IV gives the comparisons between the proposed method and the SSN method under the same condition. All simulation results are carried out on a 2.67 GHz Intel i7 CPU; with 8 GB of RAM and a 64-b Windows 7 operating system. As can be seen, the proposed method has improved accuracy in interfaces. This make the errors of capacitor voltages reduce from 0.085 pu to 0.013 pu. This is because when there is strong dynamic interactions beween MTDC and AC grids, capacitor voltages, as well as arm currents, are sensitive to the waveforms of the AC side. Moreover, the proposed method is 2 times faster than the SSN method. This is due to two reasons: 1) the proposed method is a one layer method, where calculations of interfaces do not require additional global network equations as the SSN method; 2) the modeling of the proposed nodal analysis based method is more efficient than that of the SSN method especially for the MTDC subsystems. To sum up, the proposed multirate co-simulation method improves its simulation efficiency dramatically without sacrificing the simulation accuracy, especially for the studies of dynamic interactions between MTDC and AC grids.

## VII. CONCLUSION

In this paper, a multirate EMT co-simulation method is proposed to improve the simulation efficiency of large AC and MMC-based multi-terminal DC (MTDC) systems. It partitions the whole system into multiple AC and MTDC subsystems and assigns them different time steps. To coordinate the simulation of different subsystems, we develop a cross-platform framework, in which their interfaces are modelled as timevarying Thevenin and Norton equivalents. The parameters of the equivalents are updated through moving-window prediction, stepwise correction and averaging techniques. Further, by discretizing the interface model with RM algorithm and selecting the best rate ratio, the numerical accuracy and stability of the co-simulation method is guaranteed Variables inside each subsystem and interface variables are obtained simultaneously by the proposed augmented network equations (ANEs).

TABLE IV  
COMPARISONS BETWEEN THE PROPOSED METHOD AND THE SSN METHOD
<table><tr><td>Method</td><td>CPU Time/s</td><td> $U _ { 1 0 A }$ </td><td> $I _ { 9 - 1 0 A }$ </td><td> $U _ { d c - M M C 1 }$ </td><td> $U _ { c - M M C 1 }$ </td></tr><tr><td>SSN</td><td>960</td><td>0.112</td><td>0.903</td><td>0.045</td><td>0.085</td></tr><tr><td>proposed</td><td>450</td><td>0.037</td><td>0.043</td><td>0.017</td><td>0.013</td></tr></table>

A practical AC/MTDC system including 36 AC buses, 8 generators and 4 MMC-based HVDC terminals is used to demonstrate the performance of the proposed method. Simulation results have fully validated the effectiveness of the method for updating and discretizing the interface model. The simulation efficiency of the proposed method is comparable with TLM method. Compared with the traditional simulation with an unanimous simulation step, the multirate co-simulation has improved the efficiency by 12 times. At the same time, the proposed method gains more advantages in simulation accuracy than the TLM method, especially for the short interface circuits. The average simulation errors of the proposed method are limited below 0.05 pu, indicating that there is no sacrifice of simulation accuracy. Future research work focuses on real time implementations of the multirate simulation method.

## VIII. APPENDIX

TABLE V  
PARAMETERS OF THE MTDC SUBSYSTEM
<table><tr><td rowspan="2">Parameters</td><td colspan="4">Values</td></tr><tr><td>MMC1</td><td>MMC2</td><td>MMC3</td><td>MMC4</td></tr><tr><td>Rated DC power/MW</td><td>400</td><td>300</td><td>100</td><td>100</td></tr><tr><td>Rated DC voltage/kV</td><td>±200</td><td>±200</td><td>±200</td><td>±200</td></tr><tr><td>Rated AC voltage/kV</td><td>220</td><td>220</td><td>110</td><td>110</td></tr><tr><td>SM number</td><td>250</td><td>250</td><td>250</td><td>250</td></tr><tr><td>SM capacitor/ mF</td><td>6</td><td>6</td><td>2.5</td><td>2</td></tr></table>

## REFERENCES

[1] S. Debnath, J. Qin, B. Bahrani, M. Saeedifard, and P. Barbosa, “Operation, control, applications of the modular multilevel converter: A review,” IEEE Trans. Power Electron., [1] vol. 30, no. 1, pp. 37-53, Jan. 2015.

[2] S. Liu, Z. Xu, W. Hua, G. Tang, and Y. Xue, “Electromechanical transient modeling of modular multilevel converter based multi-terminal HVDC systems,” IEEE Trans. Power Syst., vol. 29, no. 1, pp. 72-83, Jan. 2014.

[3] J. Mahseredjian, V. Dinavahi, and J. A. Martinez, “Simulation tools for electromagnetic transients in power systems: Overview and challenges,” IEEE Trans. Power Del., vol. 24, no. 3, pp. 1657-1669, Jul. 2009.

[4] N. Trinh, M. Zeller, K. Wuerflinger, and I. Erlich, “Generic model of MMC-VSC-HVDC for interaction study with AC power system,” IEEE Trans. Power Syst., vol. 31, no. 1, pp. 27-34, Jan. 2016.

[5] N. R. Chaudhuri and B. Chaudhuri, “Adaptive droop control for effective power sharing in multi-terminal DC (MTDC) grids,” IEEE Trans. Power Syst., vol. 28, no. 1, pp. 21-29, Feb. 2013.

[6] D. Z. Fang, W. Liwei, T. S. Chung, and K. P. Wong, “New techniques for enhancing accuracy of EMTP/TSP hybrid simulation,” Elect. Power Energy Syst., vol. 28, no. 10, pp. 707-711, 2006.

[7] J. Xu, C. Zhao, W. Liu, and C. Guo, “Accelerated model of modular multilevel converters in PSCAD/EMTDC,” IEEE Trans. Power Del., vol. 28, no. 1, pp. 129-136, Jan. 2013.

[8] U. N. Gnanarathna, A. M. Gole, and R. P. Jayasinghe, “Efficient modeling of modular multilevel HVDC converters (MMC) on electromagnetic transient simulation programs,” IEEE Trans. Power Del., vol. 26, no. 1, pp. 316-324, Jan. 2011.

[9] J. Chen, M. L. Crow, “A variable partitioning strategy for the multirate method in power systems,” IEEE Trans. Power Syst., vol. 23, no. 2, pp. 259-266, May 2008.

[10] F. A. Moreira, J. R. Marti, L. C. Zaneta, and L. Linares, “Multirate simulations with simultaneous-solution using direct integration methods in a partitioned network environment,” IEEE Trans. Circuits Syst. I, Reg. Papers , vol. 53, no. 12, pp. 2765-2778, Dec. 2006.

[11] W. Ren, M. Steurer, and T. L. Baldwin, “Improve the stability of power hardware-in-the-loop simulation by selecting appropriate interface algorithm,” IEEE Trans. Ind. Appl.,vol. 44, no. 4, pp. 1286-1294, Aug. 2008.

[12] R. Kuffel, R. P. Wierckx, H. Duchen, M. Lagerkvist, X. Wang, P. Forsyth, and P. Holmberg, “Expanding an analogue HVDC simulator’s modelling capability using a real-time digital simulator (RTDS),” in Proc. 1st ICDS, Apr. 1995, pp. 199-204.

[13] X. Wu, S. Lentijo, A. Deshmuk, A. Monti, and F. Ponci, “Design and implementation of a power-hardware-in-the-loop interface: A nonlinear load case study,” in Proc. 20th Annu. IEEE Appl. Power Electron. Conf. Expo., Mar. 2005, vol. 2, pp. 1332–1338.

[14] A. Benigni, A. Monti, and R. Dougal, “Latency based approach to the simulation of large power electronics systems,” IEEE Trans. Power Electron., vol. 29, no. 6, pp. 3201-3213, Jun. 2014.

[15] S. D. Pekarek et al., “An efficient multi-rate simulation technique for power-electronic-based systems,” IEEE Trans. Power Syst., vol. 19, no.1, pp. 399-409, Feb. 2004.

[16] F. Pruvost, P. Laurent-Gengoux, F. Magoules, and B. Haut, “Accelerated waveform relaxation methods for power systems,” in Proc. 2011 Int. Conf. Electrical and Control Eng., Wuhan, China, 2011, pp. 2877-2880.

[17] C. Dufour, J., Mahseredjian, J., Belanger, “A Combined State-Space Nodal Method for the Simulation of Power System Transients,” IEEE Trans. Power Del., vol. 26, no, 2, pp. 928-935, 2011.

[18] H. Saad, T. Ould-Bachir, J. Mahseredjian, C. Dufour, S. Dennetiere, and S. Nguefeu, “Real-time simulation of MMCs using CPU and FPGA,” IEEE Trans. Power Electron., vol. 30, no. 1, pp. 259-267, Jan. 2015.

[19] Saad, H., Dufour, C., Mahseredjian, J., Dennetiere, S., Nguefeu, S. \` “Real time simulation of MMCs using the state-space nodal approach,” In Proceedings of the IPST, vol. 13, pp. 18-20,July. 2013.

[20] S. Oh, S. Chae, “A Co-Simulation Framework for Power System Analysis,” Energies, vol. 9, no. 3, Feb. 2016.

[21] C. Dufour, J. Paquin, V. Lapointe, J. Belanger, L. Schoen, “PC cluster based real-time simulation of an 8-synchronous machine network with HVDC link using RT-LAB and Test Drive,” Proc. Int. Conf. Power Systems Transients, Lyon, France, Jun. 2007,pp. 4-7.

[22] B. Gustavsen, “Time delay identification for transmission line modeling,” in Proc. 8th IEEE Workshop Signal Propagation Interconnects, Heidelberg, Germany, May 9—12, 2004, pp. 103-106.

[23] M. L. Crow, J. G. Chen, “The multirate simulation of FACTS devices in power system dynamics,” IEEE Trans. Power Syst., vol. 11, no.1, pp. 376-382, Feb.1996.

[24] W. Gautschi, Numerical Analysis. New York, NY, USA: Springer, 2011.

[25] R.M. Corless, N. Fillion, A Graduate Introduction to Numerical Methods, New York: Springer, 2013, ch. 8.

[26] T. Noda, K. Takenaka, and T. Inoue, “Numerical integration by the 2-stage diagonally implicit Runge-Kutta method for electromagnetic transient simulations,” IEEE Trans. Power Del., vol. 24, no. 1, pp. 390- 399, Jan. 2009.

[27] D. A. Woodford, PSCAD User’s Guide. Winnipeg, MB, USA: Manitoba HVDC Research Centre, 2003.

[28] N.R.Watson, G.D. Irwin, “Comparison of root-matching techniques for electromagnetic transient simulation,” IEEE Trans. Power Del., vol. 15, no. 2, pp.629-634, Apr 2000.

[29] D. Shu, X. Xie, S. Zhang, et al., “Hybrid method for numerical oscillation suppression based on rational-fraction approximations to exponential functions,” IET Generation, Transmission Distribution, vol. 10, no. 11, pp. 2825-2832, Aug. 2016.

[30] A. Beddard, M. Barnes, and R. Preece, “Comparison of Detailed Modeling Techniques for MMC Employed on VSC-HVDC Schemes,” IEEE Trans. Power Del., vol. 30, no. 2, pp. 579-589, Jun. 2014.

[31] J. C. G. de Siqueira, B. D. Bonatto, J. R. Marti, et al, “A discussion about optimum time step size and maximum simulation time in EMTP-11 based programs,” Int. J.of Electrical Power Energy Syst., vol. 72, pp. 24–32, 2015.

[32] Y. Zhang et al., “Development and analysis of applicability of a hybrid transient simulation platform combining TSA and EMT elements,” IEEE Trans. Power Syst., vol. 28, no. 1, pp. 357-366, Feb. 2013.

[33] X. Duan, S. Su, and N. Mei, “Transmitting electric power system dynamics in SCADA using polynomial fitting,” Sci. China E, Tech. Sci., vol. 52, no. 4, pp. 937-943, 2008.

[34] U. Karaagac; J. Mahseredjian; et al., “Synchronous Machine Modeling Precision and Efficiency in Electromagnetic Transients,” IEEE Trans. Power Del., vol. 26, no. 2, pp.1072-1082, Apr. 2011.

Ke Wang received the M.E. degree in electrical engineering from North China Electric Power University, Beijing, China, in 2003. He works as the deputy director in Guangzhou Power Supply Co. Ltd.. His research interests include power system analysis and control.

[35] A.-J.N. Yzelman and D. Roose, “High-Level Strategies for Parallel Shared-Memory Sparse Matrix-Vector Multiplication,” IEEE Trans. Parallel and Distributed Systems, vol. 25, no. 1, pp. 116-125, Jan. 2014.

[36] X. Li, Q. Song, W. Liu, H. Rao, S. Xu, and L. Li, “Protection of nonpermanent faults on DC overhead lines in MMC-Based HVDC systems,” IEEE Trans. Power Del., vol. 28, no. 1, pp. 483-490, Jan. 2013.

[37] H. Yang, Y. Dong,W. LI, and X. He, “Average-value model of modular multilevel converters considering capacitor voltage ripple,” IEEE Trans. Power Del., vol. 32, no. 2, pp. 723-732, 2017.

Dewu Shu (S’14) received the B.Sc. degree in Electrical Engineering from Tsinghua University in 2013. Currently, he is pursuing the Ph.D. degree in the Dept. of Electrical Engineering, Tsinghua University. His research interests include multirate EMT/TS simulations, power system stability.

Xiaorong Xie received the B.Sc. degree from Shanghai Jiao Tong University, Shanghai, China, in 1996 and the Ph.D./M. Eng. degrees from Tsinghua University, Beijing, China, in 2001. From 2001 to 2005, he was a Lecturer with the Department of Electrical Engineering, Tsinghua University. Since 2005, he works as an Associate Professor in the same department. His current research interests focus on power system analysis and control, and flexible ac transmission systems.

Qirong Jiang (M’98) received the B.S. and Ph.D. degrees in electrical engineering from Tsinghua University, Beijing, China, in 1992 and 1997, respectively. Since 2006, he has been a Professor at Tsinghua University. His research interests include power system analysis and control, modeling and control of exible ac transmission systems, power quality analysis and mitigation, power-electronic equipment, and renewable energy power conversion.

Gaopeng Guo received the B.Sc. degree from Tianjin University, Tianjin, China, in 2008 and received the Master degree from Chinese Academy of Sciences (CAS), Hefei, China, in 2011. He received the Ph.D. degree from the China Electrical Power Research Institute (CEPRI), Beijing, China, 2015. He is currently engaged in postdoctoral research in Department of Electrical Engineering of Tsinghua University. His current research interests include offshore wind farm and MMC based HVDC.