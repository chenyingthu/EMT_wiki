# A Multi-rate Co-simulation of Combined Phasor-Domain and Time-Domain Models for Large-scale Wind Farms

Yupeng Li, Student Member, IEEE, Dewu Shu, Member, IEEE, Fan Shi, Zheng Yan, Yiying Zhu, Nengling Tai

Abstract—In the year 2015-2018, there are many sub- and super-synchronous interaction (S2SI) events, happened in China. However, traditional transient stability models, electro-magnetic transient (EMT) models and hybrid TS and EMT simulation methods fail to capture the desired wide frequency band interactions between large-scale AC grids and wind farms. To accurately and efficiently capture wide frequency band interactions between AC grids and wind farms, a simulation method which can extend the time-step to 500µs and further adopt the multi-rate structure is highly required. For this objective, we propose a multi-rate co-simulation method, in which the target system is partitioned into electro-magnetic transient (EMT) and shifted frequency phasor (SFP) subsystems, represented by our proposed transformation based SFP models and the traditional EMT models, respectively. The simulation efficiency of simulating large-scale AC grids is significantly improved by adopting a much larger time-step. Further, the multi-rate multi-domain transmission-line model (MD-TLM) and the multi-rate frequency dependent MD-TLM are respectively proposed to reflect wideband interactions between AC grids and wind farms. Eventually, the multi-rate co-simulation is implemented based on the efficient SFP models, network partitioning, and so-called the multi-rate (FD)-MD-TLM. The performance (efficiency and accuracy) of the proposed method has been fully validated on a practical system integrating large AC grids and wind farms.

Index Terms—multi-rate co-simulation, shifted frequency phasor (SFP) model, multi-domain transmission-line model (MD-TLM), frequency dependent.

# I. INTRODUCTION

W ITH the increased integration of wind power, the flex-ibility and security of power grid face significant chal- ibility and securityof power grid face significant challenges. Recently, the sub- synchronous and super-synchronous oscillations aroused by the fixed series compensation (FSC), nearby doubly-fed induction generators (DFIGs) and the largescale AC grids, has been detected in Texas of USA [1], [2] and Hebei Province of North China [3], resulting in drop-out of numerous wind turbine generators (WTGs) or even damage of crowbar circuits. Unlike the traditional shaft related subsynchronous resonance (SSR) problems [4], such new events are related to controllers of wind farms, dynamics of adjacent

This work was supported by the Science and Technology Project of State Grid (shanghai municipal electric power company) 52097018000D, open fund of FXB51201901051 (CEPRI), Shanghai Sailing Program 19YF1423500. (Corresponding author: Dewu Shu).

Yupeng Li, Dewu Shu, Fan, Shi, Zheng Yan are with Department of Electrical Engineering, Shanghai Jiaotong University, Shanghai, 200240, China. (e-mail: shudewu@sjtu.edu.cn).

Yiying Zhu, Yupeng Li is with the State Grid Simulation Center.

AC grids. Therefore, an efficient and accurate simulation method, which can capture detailed electro-magnetic transients of large-scale AC system integrating hundreds of wind turbine generators (WTGs) is highly necessary [5].

However, it is always a consuming task to simulate the large-scale wind farm related AC grids [6]. This is because: (1) a significant increase in the number of buses due to the expanding scale of AC grids and wind farms; (2) a much smaller time-step (usually as small as 2-50µs) to emulate detailed switching dynamic of each wind turbine; (3) the time-step of the whole system combining the large-scale AC grids and wind farms will be limited as a unanimous timestep, which would result in enormous computational burden. Several system equivalent methods have been proposed to improve the simulation efficiency [7]. For instance, the AC grid is simplified as a fixed Thevenin or Norton equivalent circuit, where the wind farms are represented as their detailed electro-magnetic transient models [8]. The drawback is that the electro-mechanical dynamics of AC grids as well as interactions between AC grids and wind farms are totally neglected. On the hand, if the wind farm is represented as the aggregate model, i.e., all the wind turbines are simplified as one controlled current source model [9], the controllers of different wind turbines can not be modelled. More importantly, the inner dynamics of the wind farms aroused by frequency dependent components cannot be represented, which is important to capture wide-band frequency interactions between the AC grid and the wind farm. Several other methods, such as the transient stability and electro-magnetic transient (EMT) hybrid simulations [10]-[12], and multi-rate simulation method [7], dynamic phasor model [13]-[14], etc. have been proposed to accelerate the simulation speed of the largescale AC grids incorporating wind farms. However, as the AC grid is represented as their corresponding transient stability model by using the hybrid simulation method, the EMT dynamics of the AC grid which are aroused by nonlinear dynamics of generators and frequency dependent dynamics of transmission lines cannot be captured. It should be noted that it is necessary to use EMT model of AC grids if the wide-band frequency interactions are highly interested. Moreover, even if the traditional multi-rate EMT simulation method is adopted [7], the simulation is still computationally burdensome, as the time-step is restricted by the small time-step of wind farms.

The reason why we write this paper is actually originated from practical engineering problems.In the year 2015-2018,

there are many sub- and super-synchronous oscillation events, such as in Xinjiang province, and Guyuan Area, which are happened in China [15]-[16]. In order to study the mechanism of the $\mathbf { S } ^ { 2 } \mathbf { S } \mathbf { I }$ event, the first step is to set up the accurate and efficient simulation model to reproduce the $\mathbf { S } ^ { 2 } \mathbf { S } \mathbf { I }$ event. However, traditional methods, such as eletro-magnetic transient programs, transient stability programs, and even the hybrid EMT and TS simulations, cannot represent wide frequency interactions between large-scale AC grids and wind farms. Therefore, it is highly necessary to propose a new simulation method, which can extend the time-step of large-scale AC grids to as large as 500µs or more. Second, in order to reflect the wide-band frequency interactions between the wind farm and the AC grid, a simulation method under the multi-rate structure is strongly recommended.

To address the above issues, a multi-rate co-simulation method of combined phasor-domain and time-domain models is proposed. The contributions are threefold:

(1) The SFP models are proposed to resolve the efficiency problem of large-scale AC grids. New shifted frequency phasor (SFP) models based on the rotational matrix transformation are derived for the components of AC grids. They can use a much larger time-step and the calculations are fulfilled and accelerated from the aspect of modeling.   
(2) The wide frequency band interface models are proposed to reflect the desired wide frequency band interactions. The desired frequency band can be extended to 1000Hz at the time-step of 500µs. The interface models between SFP and EMT subsystems are proposed and represented by the multirate multi-domain transmission line model (MD-TLM) and the multi-rate frequency dependent multi-domain transmission line model (FD-MD-TLM), where the latter can catch the high-frequency interactions of interfacing. Both multi-rate MD-TLM and FD-MD-TLM can produce instantaneous and phasor waveforms simultaneously. Thus, the so-called wideband frequency interactions can be captured and reflected accurately.   
(3) The overall multi-rate and multi-domain co-simulation method is constructed to reproduce the desired $\mathbf { S } ^ { 2 } \mathbf { S } \mathbf { I }$ oscillation event. A new multi-rate co-simulation simulation structure is developed based on SFP models, network partitioning, and multi-rate MD-TLM. Case studies of a practical system have fully demonstrated its effectiveness of the proposed multirate co-simulation method in simulating large-scale AC grids integrating wind farms.

The rest of the paper is organized as follows: Section II introduces the proposed transformation based shifted phasor models (SFP) of AC grids. Section III elaborates the multi-rate co-simulation combining phasor- and time-domain models. Section IV examines the performance of the proposed method by simulating a practical AC system integrating large-scale wind farms. Brief conclusions are finally drawn in Section V.

# II. TRANSFORMATION BASED SHIFTED FREQUENCY PHASOR (SFP) MODELS OF AC GRIDS

The simulation efficiency will be greatly affected by the large-scale of the AC grids. The reason is due to the following

aspects: (1) the node number of the whole system will be greatly increased by the scale of the AC grids; (2) many nonlinear and frequency dependent components are contained in the system, which require additional calculations of the nodal voltage equations. In order to improve the simulation efficiency from the aspect of modelling, the transformation based phasor (SFP) models is proposed. The key characteristic of the transformation based SFP models is that it allows a larger time-step to simulate the large-scale AC grids while the simulation accuracy can still be guaranteed.

A. Brief Introduction of Transformation based Shifted $F r e \mathrm { - }$ quency Phasor (SFP) Models

As established in [17]-[18], the electrical variable in largescale AC grids (assumed with fundamental frequency $\omega _ { s } )$ can be represented by its SFP form:

$$
\left\{ \begin{array}{c} x (t) = \hat {x} (t) e ^ {j \omega_ {\mathrm {s}} t} \\ \hat {x} (t) = x _ {I} (t) + j x _ {Q} (t) \end{array} \right. \tag {1}
$$

where ${ \hat { x } } ( t )$ is the complex envelope of the time-domain signal $x ( t )$ , and preserves its low-frequency dynamics. $x _ { I } ( t )$ and $x _ { Q } ( t )$ are the real and imaginary parts of ${ \hat { x } } ( t )$ , respectively.

Suppose the dynamic equation of a system component is written as $d x / d t = f ( x , t )$ , its dynamic equation in the SFP form can be derived as

$$
\frac {d \hat {u}}{d t} = f (\hat {u}, t) - j \omega_ {s} \hat {u} \tag {2}
$$

Decoupling into real and imaginary parts yields

$$
\frac {d \hat {u} _ {x y}}{d t} = \mathbf {F} (\hat {u} _ {x y}, t) + \omega_ {s} \mathbf {T} \left(- \frac {\pi}{2 \omega_ {s}}\right) \hat {u} _ {x y} \tag {3}
$$

where

$$
\mathbf {F} \left(\hat {u} _ {x y}, t\right) = \left[ \begin{array}{c c} \mathbf {F} \left(\hat {u} _ {x}, t\right) & \\ & \mathbf {F} \left(\hat {u} _ {y}, t\right) \end{array} \right], \mathbf {T} (t) = \left[ \begin{array}{c c} \cos \omega_ {s} t & - \sin \omega_ {s} t \\ \sin \omega_ {s} t & \cos \omega_ {s} t \end{array} \right] \tag {4}
$$

In (3), $\hat { u } _ { x y } = \left\lceil \begin{array} { l l } { \hat { u } _ { x } } & { \hat { u } _ { y } } \end{array} \right\rceil ^ { T }$ , where $\hat { u } _ { x }$ and $\hat { u } _ { y }$ are the real and imaginary parts of ${ \hat { u } } ( t )$ in the reference frame after Park transform.

Adopting the trapezoidal integration rule, (3) is discretized as:

$$
\frac {\hat {u} _ {n} - \hat {u} _ {n - 1}}{\Delta t} = \frac {\hat {f} _ {n} + \omega_ {s} \mathbf {T} \left(- \frac {\pi}{2 \omega_ {s}}\right) \hat {u} _ {n} + \hat {f} _ {n - 1} + \omega_ {s} \mathbf {T} \left(- \frac {\pi}{2 \omega_ {s}}\right) \hat {u} _ {n - 1}}{2} \tag {5}
$$

where $\boldsymbol { \hat { u } _ { n } } , \boldsymbol { \hat { f } _ { n } }$ denote the state and the differential term at the nth time-step, respectively. ∆t is the time-step.

Based on (1) and (5), the SFPs can be transformed into time domain signals

$$
\begin{array}{l} u _ {n} = \mathbf {T} (\Delta t) u _ {n - 1} \\ + \frac {\Delta t}{2} \left[ f _ {n} + \omega_ {s} \mathbf {T} \left(- \frac {\pi}{2 \omega_ {s}}\right) u _ {n} + \mathbf {T} (\Delta t) f _ {n - 1} + \omega_ {s} \mathbf {T} \left(\Delta t - \frac {\pi}{2 \omega_ {s}}\right) u _ {n - 1} \right] \tag {6} \\ \end{array}
$$

The SFP concept is adopted hereafter to develop the models for AC grids according to Eq. (6).

# B. The Derivation of a Capacitor as an example

We will take the capacitor as a typical example to make it more easier to understand the concrete steps concerning the SFP modeling. According to Eqs. (1)-(4), the differential equation for a capacitor. i.e., $i = C d u / d t$ , is derived in the SFP form:

$$
\hat {i} _ {x y} = C \frac {d \hat {u} _ {x y}}{d t} + \omega_ {s} \mathbf {T} \left(- \frac {\pi}{2 \omega_ {s}}\right) \hat {u} _ {x y} \tag {7}
$$

Eq. (7) is discretized by Trapezoidal algorithm:

$$
C \frac {\hat {u} _ {x y} (t) - \hat {u} _ {x y} (t - \Delta t)}{\Delta t} = \frac {1}{2} \left[ \begin{array}{l} \hat {i} _ {x y} (t) - \omega_ {s} \mathbf {T} \left(- \frac {\pi}{2 \omega_ {s}}\right) \hat {u} _ {x y} (t) + \\ \hat {i} _ {x y} (t - \Delta t) - \omega_ {s} \mathbf {T} \left(- \frac {\pi}{2 \omega_ {s}}\right) \hat {u} _ {x y} (t - \Delta t) \end{array} \right. \tag {8}
$$

After some rewriting:

$$
\begin{array}{l} \hat {i} _ {x y} (t) = \left[ \frac {2 C}{\Delta t} + \omega_ {s} \mathbf {T} \left(- \frac {\pi}{2 \omega_ {s}}\right) \right] \hat {u} _ {x y} (t) - \hat {i} _ {x y} (t - \Delta t) \tag {9} \\ + \left[ - \frac {2 C}{\Delta t} + \omega_ {s} \mathbf {T} \left(- \frac {\pi}{2 \omega_ {s}}\right) \right] \hat {u} _ {x y} (t - \Delta t) \\ \end{array}
$$

Then, transferring the SFP variables into their corresponding time-domain variables:

$$
\begin{array}{l} \left. i _ {x y} (t) = \left[ \frac {2 C}{\Delta t} + \omega_ {s} \mathbf {T} \left(- \frac {\pi}{2 \bar {\omega} _ {s}}\right) \right] u _ {x y} (t) - \mathbf {T} (\Delta t) i _ {x y} (t - \Delta t) \right. \tag {10} \\ + \left[ - \frac {2 C}{\Delta t} \mathbf {T} (\Delta t) + \omega_ {s} \mathbf {T} \left(\Delta t - \frac {\pi}{2 \omega_ {s}}\right) \right] u _ {x y} (t - \Delta t) \\ \end{array}
$$

Therefore, the final Norton equivalent circuit for the capacitor is derived as:

$$
i _ {x y} (t) = G _ {c x y} u _ {x y} (t) + J _ {x y} (t - \Delta t) \tag {11}
$$

where

$$
\left\{ \begin{array}{c} G _ {c x y} = \frac {2 C}{\Delta t} + \omega_ {s} \mathbf {T} \left(- \frac {\pi}{2 \omega_ {s}}\right) \\ J _ {x y} (t - \Delta t) = - \mathbf {T} (\Delta t) i _ {x y} (t - \Delta t) + \\ \left[ - \frac {2 C}{\Delta t} \mathbf {T} (\Delta t) + \omega_ {s} \mathbf {T} \left(\Delta t - \frac {\pi}{2 \omega_ {s}}\right) \right] u _ {x y} (t - \Delta t) \end{array} \right. \tag {12}
$$

# C. Physical Interpretation of SFP Models

When a time-domain signal $x ( t )$ multiplies $e ^ { \pm j \omega _ { s } t }$ , the frequency band of $x ( t )$ will be shifted by ωs, or $x ( t ) e ^ { \pm j \omega _ { s } t } \Leftrightarrow$ $X [ j ( \omega \mp \omega _ { s } ) ]$ . In other words, the frequency band are shifted from the high-frequency band to the lower frequency band, where a larger time-step can be used in order to improve the efficiency where the accuracy is still satisfied.

# III. MULTI-RATE CO-SIMULATION OF COMBINED PHASOR-DOMAIN AND TIME-DOMAIN MODELS

The transformation based SFP model is used to accelerate the simulation speed of AC grids by adopting a much larger time-step. In order to capture fast dynamics of wind farms in great details, a multi-rate co-simulation method is further adopted by partitioning the whole system into the SFP and EMT subsystems, respectively. The AC grids are contained in the SFP subsystem by adopting a much larger time-step, where the time-step can be as large as 500µs. It should be noted that even the time-step is extended to 500µs, the electro-magnetic transients, or the nonlinear dynamics of generators and frequency dependent dynamics of transmission lines, can still be retained. On the other hand, wind farms are included in the EMT subsystem by using a smaller time-step (usually as small

as 2-50µs), where their detailed dynamics can be captured by their electro-magnetic transient models. The interactions between wind farms and the AC grids are reflected by the proposed multi-domain transmission line model (MD-TLM) based on the Bergeron model and the frequency dependent line model, respectively.

# A. Network Partitioning by Multi-domain Transmission Line Model (MD-TLM) Decoupling

![](images/030ff002312a3131052da7b91aa480bfeee0b0afa4fe3428fe7f725ca99f932f.jpg)  
Fig. 1. The multi-rate multi-domain transmission line model (MD-TLM) .

As shown in Fig. 1, the target system is first separated into the SFP and EMT subsystems in phasor- and time-domain, respectively. The time-steps of the SFP/EMT subsystems are denoted as ∆T and ∆t, which satisfies $\Delta T = n \Delta t , \ n > 1$ . For the calculations of the SFP subsystem, all the network components are derived as Norton equivalents based on shifted phasors according to the procedure introduced in [17]-[18]. Then the whole system is formulated into nodal voltage equation, which is written as:

$$
\left[ \begin{array}{c c} \operatorname {R e} \left(\mathbf {G} _ {s}\right) & - \operatorname {I m} \left(\mathbf {G} _ {s}\right) \\ \operatorname {I m} \left(\mathbf {G} _ {s}\right) & \operatorname {R e} \left(\mathbf {G} _ {s}\right) \end{array} \right] \left[ \begin{array}{l} \mathbf {v} _ {s} ^ {x} (t) \\ \mathbf {v} _ {s} ^ {y} (t) \end{array} \right] = \left[ \begin{array}{l} \mathbf {i} _ {s} ^ {x} (t) \\ \mathbf {i} _ {s} ^ {y} (t) \end{array} \right] + \left[ \begin{array}{l} \mathbf {J} _ {s} ^ {x} (t - \Delta T) \\ \mathbf {J} _ {s} ^ {y} (t - \Delta T) \end{array} \right] \tag {13}
$$

where $G _ { s }$ is the complex-value based conductance matrix of the SFP subsystem; $\left[ \dot { \mathbf { v } } _ { s } ^ { x } ( t ) , \mathbf { v } _ { s } ^ { y } ( t ) \right] ^ { T }$ is the vector of nodal voltages; $\left[ \mathbf { i } _ { s } ^ { x } ( t ) , \mathbf { i } _ { s } ^ { y } ( t ) \right] ^ { T }$ is the vector of external current sources; $\left[ \mathbf { J } _ { s } ^ { x } ( t - \Delta T ) , \mathbf { J } _ { s } ^ { y } ( t - \Delta T ) \right] ^ { T }$ is the equivalent current vector. Similarly, the calculations of EMT subsystem are based on the nodal voltage equation, which is derived as [7]:

$$
\left[ \mathbf {G} _ {e} \right] \mathbf {v} _ {e} (t) = \mathbf {i} _ {e} (t) + \mathbf {J} _ {e} (t - \Delta t) \tag {14}
$$

where $G _ { e }$ is the complex-value based conductance matrix of the EMT subsystem; $\nu _ { e } ( t ) , i _ { e } ( t )$ are the vectors of voltages and currents; $J _ { e } ( t - \Delta t )$ is the equivalent current.

The network partitioning strategies between SFP and EMT subsystems can be realized by combining the following rules:

(1) In order to realize the proposed multi-domain transmission line model (MD-TLM), the partitioning point can be chosen at the long transmission lines, which have large impedances and large latency for the traveling waves.   
(2) Usually, simulation errors of interface model are larger than those inside each subsystem, especially when the selected time-step is over 50µs. In order to reduce the impact from errors of interface model on the errors of other buses, it is better to choose the partitioning point at the bus with the minimum number of connected lines.

(3) Choose the partitioning point at the weak coupling point of the network, which can be determined by the power flow, the short circuit capacity, and etc.

The network partitioning point is suggested as the weak coupling point, which can be evaluated by the electrical distance. The electrical distance can be derived from the Jacobian matrix of power flow, measuring the voltage interactions between two nodes. The electrical distance between node i and node j is defined as the sensitivity of the voltage change at node i to the voltage change node j:

$$
D _ {i j} = - \log_ {1 0} \left(\frac {\Delta U _ {i}}{\Delta U _ {j}}\right), \frac {\Delta U _ {i}}{\Delta U _ {j}} = \frac {\left(\partial U / \partial Q\right) _ {i j}}{\left(\partial U / \partial Q\right) _ {j j}} \tag {15}
$$

where $\left( \partial U \ / \partial Q \right) _ { i j } , \ \left( \partial U \ / \partial Q \right) _ { j j }$ can be obtained from the Jacobian matrix of the power flow.

# B. Multi-rate Bergeron model based MD-TLM

The interactions between SFP and EMT subsystems are reflected by the proposed multi-rate Bergeron model based MD-TLM, which is shown in Fig. 1. The multi-rate MD-TLM is a dual-port model, where each port represented by a Norton equivalent circuit in time-domain and phasordomain representations, respectively. The influence from one subsystem on the other is reflected by a Norton equivalent that is composed of a paralleled impedance and a controlled current source with a time delay (traveling time) τ.

The interface model of MD-TLM in the fast EMT subsystem is first detailed below. For the $p ^ { t h }$ iteration of SFP subsystem, i.e., the time period of $[ t _ { p } , t _ { p + 1 } ]$ , the interface model in the EMT subsystem should be updated n times at $t = t _ { p } + i \Delta t , i = 1 , 2 . . .$ n within $[ t _ { p } , t _ { p + 1 } ]$ .

The multi-rate MD-TLM in the EMT subsystem is updated through the iterative calculation of the equivalent current source $I _ { k } ( t - \tau )$ using the following formula:

$$
I _ {k} (t - \tau) = - Z ^ {- 1} u _ {n} (t - \tau) - i _ {n} (t - \tau), t = t _ {p} + i \Delta t, i = 1, 2 \dots n \tag {16}
$$

where $u _ { n } ( t - \tau ) , i _ { n } ( t - \tau )$ are instantaneous interface voltages and currents of node n in EMT subsystems with the time delay τ, which are converted from the shifted phasors of interface voltages and currents in SFP subsystems. Interface voltages are calculated by:

$$
u _ {n} (t - \tau) = \mathbf {R e} \left[ u _ {n} ^ {x y} (t - \tau) e ^ {j \omega t} \right], t = t _ {p} + i \Delta t, i = 1, 2 \dots n \tag {17}
$$

where Re[.] denotes the real part; $u _ { n } ^ { x y } ( t - \tau ) = u _ { n } ^ { x } ( t -$ $\pmb { \tau } ) + j u _ { n } ^ { y } ( t - \pmb { \tau } )$ are the interface voltages in the SFP subsystem, which are calculated using interpolations in phasor domain:

$$
\begin{array}{l} u _ {n} ^ {x y} \left(t _ {p} + i \Delta t - \tau\right) \\ = \frac {(k - i) \Delta t - \tau}{\Delta t} \mathbf {R e} \left\{u _ {n} ^ {x y} \left[ t _ {p} + i \Delta t - (k - 1) \Delta t \right] e ^ {j [ \tau - (k - i - 1) \Delta t ]} \right\} \\ + \frac {\tau - (k - i - 1) \Delta t}{\Delta t} \mathbf {R e} \left\{u _ {n} ^ {x y} \left[ t _ {p} + i \Delta t - k \Delta t \right] e ^ {j [ \tau - (k - i) \Delta t ]} \right\} \tag {18} \\ \end{array}
$$

where the time delay τ is supposed to be within the interval $[ ( k - 1 ) \Delta t , k \Delta t ]$ , and $k = [ \tau / \Delta t ] + 1$ with [.] indicating the integer floor function. The interface currents can be derived in a similar way.

The update of MD-TLM in the SFP subsystem is fulfilled as follows: First, the paralleled impedance matrix $Z ^ { x y }$ in phasor domain is calculated by $Z ^ { x y } = Z \otimes I _ { 2 \times 2 }$ and $\bullet _ { \otimes } ,$ denotes the Kronecker product. Then the equivalent current vector $\bar { \mathbf { I } } _ { \mathbf { n } } ^ { \mathbf { x y } } ( t -$ τ) in the SFP subsystem with the time delay of τ is calculated by:

$$
\bar {\mathbf {I}} _ {\mathbf {n}} ^ {\mathbf {x y}} \left(t _ {p} - \tau\right) = - \left[ \bar {\mathbf {u}} _ {\mathbf {k}} ^ {\mathbf {x y}} \left(t _ {p} - \tau\right) e ^ {- j \theta} \right] / Z - \bar {\mathbf {i}} _ {\mathbf {k}} ^ {\mathbf {x y}} \left(t _ {p} - \tau\right) e ^ {- j \theta} \tag {19}
$$

where $\tau = l / \nu , \ \theta = \omega l / \nu , \ Z = \sqrt { L / C } .$

In (19), the phasor-domain interface voltage in the SFP subsystem, $\bar { \mathbf { u } } _ { \mathbf { k } } ^ { \mathbf { x y } } ( t - \tau )$ , is obtained by applying Hilbert transform on the averaged interface voltages of the EMT subsystem, ${ \bar { u } } _ { k } ( t - \tau )$ , i.e.,

$$
\bar {\mathbf {u}} _ {\mathbf {k}} ^ {\mathbf {x y}} (t - \tau) = \mathbf {R e} \left\{\left[ \bar {u} _ {k} (t - \tau) + j H [ \bar {u} _ {k} (t - \tau) ] \right] e ^ {j \omega t} \right\} \tag {20}
$$

where $H [ . ]$ is the Hilbert transformation. Moreover, the averaged voltage at $t _ { p }$ is obtained by

$$
\bar {u} _ {k} \left(t _ {p}\right) = \frac {1}{n} \sum_ {l = 1} ^ {n} u _ {k} \left(t _ {p - 1} + l \Delta t\right) \tag {21}
$$

And the averaged voltage ${ \bar { u } _ { k } } ( t _ { p } - \tau )$ can be calculated by linear interpolations in time-domain

$$
\begin{array}{l} \bar {u} _ {k} (t _ {p} - \tau) = \frac {k \Delta t - \tau}{\Delta t} \bar {u} _ {k} [ t _ {p} - (k - 1) \Delta t ] \\ + \frac {\tau - (k - 1) \Delta t}{\Delta t} \bar {u} _ {k} [ t _ {p} - k \Delta t ], \tau \in \left[ (k - 1) \Delta t, k \Delta t \right], k = \left[ \tau / \Delta t \right] + 1 \tag {22} \\ \end{array}
$$

C. Multi-rate Frequency Dependent Multi-domain Transmission Line Model (FD-MD-TLM)

The proposed multi-rate frequency dependent multi-domain transmission line model (FD-MD-TLM) is detailed in Fig. 2. The difficulties for the FD-MD-TLM lies in the following aspects: (1) how to update the frequency-dependent characteristic impedance and the equivalent current time-domain and phasor-domain, respectively; (2) the equivalent circuit of SFP subsystem should be simulated under a much larger time-step ∆T , where that of EMT subsystem is simulated a smaller timestep ∆t. Accordingly, the equivalent circuit of SFP subsystem is calculated by the time averaging technique. On the other hand, the equivalent of EMT subsystem is calculated by timeand phasor-domain interpolation techniques.

![](images/f222587b4b712df2a1c5c1e8067cdc381b12063f05e2be806b9673bd54d67c44.jpg)  
Fig. 2. The multi-rate frequency dependent multi-domain transmission line model (FD-MD-TLM) .

As shown in Fig. 2, the frequency dependent interface transmission line of length l is characterized by the per-unitlength parameters of series impedance ${ \bf Z } ( { \bf s } ) = { \bf R } ( { \bf s } ) + { \bf s } { \bf L } ( { \bf s } )$ and shunt admittance $\mathbf { Y } ( \mathbf { s } ) = \mathbf { G } ( \mathbf { s } ) + \mathbf { s } \mathbf { C } ( \mathbf { s } )$ . These $n * n$ matrices (n denotes the number of conductors in the transmission line) are

complex and define the relation between the n ∗ 1 vectors of voltage v and current i:

$$
\left\{ \begin{array}{l} - \frac {d \mathbf {v}}{d x} = \mathbf {Z} \mathbf {i} \\ - \frac {d \mathbf {i}}{d x} = \mathbf {Y} \mathbf {v} \end{array} \right. \tag {23}
$$

In multi-rate FD-MD-TLM, the equivalent circuit model in the EMT subsystem are calculated based on current waves where the current $\mathbf { i } _ { \mathbf { k } }$ at end k is related to the voltage $\mathbf { v _ { k } }$ and the incident current wave $\mathbf { i _ { k i } }$ via discretization of the convolutions in time-domain:

$$
\left\{ \begin{array}{c} \mathbf {i} _ {k} (t) = Y _ {c} (t) * \mathbf {v} _ {k} (t) + \mathbf {I} _ {h i s, k} (t - \tau) = Y _ {c} (t) * \mathbf {v} _ {k} (t) - 2 \mathbf {i} _ {k i} (t) \\ \mathbf {i} _ {k i} (t) = \mathbf {H} (t) * \mathbf {i} _ {m r} (t) \end{array} \right.
$$

$$
t = t _ {p} + i \Delta t, i = 1, 2 \dots n \tag {24}
$$

where $Y _ { c }$ and H are the matrices of characteristic admittance and propagation, respectively. $\bf \delta i _ { \bf k i } ( t )$ is the incident current wave; and $\mathbf { i } _ { \mathbf { m r } } ( \mathbf { t } )$ is the reflected wave.

The reflected current $\mathbf { i } _ { \mathbf { m r } } ( \mathbf { t } )$ are calculated by transferring the current in the phasor domain into the time-domain, as the node m is inside the SFP subsystem:

$$
\mathrm {i} _ {m r} (t) = i _ {m r} ^ {x} (t) \cos \omega t - i _ {m r} ^ {y} (t) \sin \omega t \tag {25}
$$

where $i _ { m r } ^ { x y } ( t ) = [ i _ { m r } ^ { x } ( t ) , i _ { m r } ^ { y } ( t ) ] ^ { T }$ are the interface voltages in the SFP subsystem.

The frequency dependent matrix $\mathbf { Y _ { c } }$ is fitted by the sum of first-order rational functions as:

$$
\mathbf {Y} _ {c} = \mathbf {G} _ {0} + \sum_ {i = 1} ^ {N y} \frac {\mathbf {G} _ {i}}{s - q _ {i}} \tag {26}
$$

Where $N _ { y }$ is the fitted order $q _ { i }$ represents the $i ^ { t h }$ fitting pole; $\mathbf { G _ { i } }$ is the corresponding matrix of residues and $\bf { G _ { 0 } }$ is a constant matrix obtained at the limit of $\mathbf { Y _ { c } }$ when $s = j \omega \to \infty$ .

According to Eqs. (2)-(4), the shifted phasor equation for the shunt current $i _ { s } ( t ) = Y _ { c } ( t ) * \mathbf { v } _ { k } ( t )$ is given as:

$$
\left\{ \begin{array}{c} \hat {i} _ {s} (t) = \mathbf {G} _ {0} \hat {v} _ {k} (t) + \sum_ {i = 1} ^ {N _ {g}} \hat {w} _ {i} \\ \frac {d \hat {w} _ {i}}{d t} = q _ {i} \hat {w} _ {i} + \omega_ {s} \mathbf {T} \left(- \frac {\pi}{2 \omega_ {s}}\right) \hat {w} _ {i} + G _ {i} \hat {v} _ {k} (t) \end{array} \right. \tag {27}
$$

where $\cdot _ { \wedge } ,$ denotes the shifted phasor of the corresponding variables; T() is the transformation matrix given in Eq. (4).

Eq. (27) is discretized by the Trapezoidal algorithm and all the variables are transformed back from shifted phasors to their corresponding time-domain variables:

$$
w _ {i} (t) = \mathbf {A} _ {i} w _ {i} (t - \Delta t) + \mathbf {G} _ {i} v _ {k} (t) + \mathbf {K} _ {i} v _ {k} (t - \Delta t) \tag {28}
$$

where

$$
\left\{ \begin{array}{r l} \mathbf {A} _ {i} & = \left[ \frac {2}{\Delta t} - q _ {i} - \omega_ {s} \mathbf {T} \left(- \frac {\pi}{2 \omega_ {s}}\right) \right] ^ {- 1} \left[ \frac {2}{\Delta t} \mathbf {T} (\Delta t) + q _ {i} \mathbf {T} (\Delta t) \right] \\ \mathbf {B} _ {i} & = \left[ \frac {2}{\Delta t} - q _ {i} - \omega_ {s} \mathbf {T} \left(- \frac {\pi}{2 \omega_ {s}}\right) \right] ^ {- 1} G _ {i} \\ \mathbf {K} _ {i} & = \left[ \frac {2}{\Delta t} - q _ {i} - \omega_ {s} \mathbf {T} \left(- \frac {\pi}{2 \omega_ {s}}\right) \right] ^ {- 1} \mathbf {T} (\Delta t) G _ {i} \end{array} \right. \tag {29}
$$

Similarly, the frequency dependent propagation matrix H can be approximated by different groups of the first-order rational functions with different time-delays:

$$
\mathbf {H} = \sum_ {k = 1} ^ {N g} e ^ {- s \tau_ {k}} \sum_ {i = 1} ^ {N (k)} \frac {R _ {k , i}}{s - p _ {k , i}} \tag {30}
$$

where $\tau _ { k }$ is the delay associated with the velocity of the $k ^ { t h }$ mode and $N _ { g }$ is the number of modes; $N ( k )$ is the fitting order of $k ^ { t h }$ term; $R _ { k , i }$ and $p _ { k , i }$ represent its $k ^ { t h }$ fitting pole and a matrix of residues determined by a vector fitting process.

According to Eqs. (23)-(24), the auxiliary current $i _ { r } ( t ) =$ $\mathbf { H } ( t ) * \mathbf { i } _ { m r } ( t )$ is calculated by transforming all the variables into the shifted phasor domain:

$$
\left\{ \begin{array}{c} \hat {i} _ {r} = \sum_ {k = 1} ^ {N g} \sum_ {i = 1} ^ {N (k)} \hat {x} _ {k, i} \\ \frac {d \hat {x} _ {k , i}}{d t} = p _ {k, i} \hat {x} _ {k, i} + \omega_ {s} \mathbf {T} \left(- \frac {\pi}{2 \omega_ {s}}\right) \hat {x} _ {k, i} + R _ {k, i} \hat {i} _ {m r} (t - \tau_ {k}) \end{array} \right. \tag {31}
$$

Then, Eq. (31) is transferred back into the time domain and the time-domain auxiliary current are finally calculated by:

$$
\left\{ \begin{array}{c} i _ {r} = \sum_ {k = 1} ^ {N g} \sum_ {i = 1} ^ {N (k)} x _ {k, i} \\ x _ {k, i} = \mathbf {S} _ {k, i} x _ {k, i} (t - \Delta t) + \mathbf {D} _ {k, i} i _ {m r} (t - \tau_ {k}) + \mathbf {P} _ {k, i} i _ {m r} (t - \tau_ {k} - \Delta t) \end{array} \right. \tag {32}
$$

where

$$
\mathbf {S} _ {k, i} = \left[ I - \frac {\Delta t}{2} p _ {k, i} - \frac {\Delta t}{2} \omega_ {s} \mathbf {T} \left(- \frac {\pi}{2 \omega_ {s}}\right) \right] ^ {- 1} \tag {33}
$$

$$
\left[ \mathbf {T} (\Delta t) + \frac {\Delta t}{2} \mathbf {T} (\Delta t) p _ {k, i} - \omega_ {s} T \left(\Delta t - \frac {\pi}{2 \omega_ {s}}\right) \right]
$$

$$
\left\{ \begin{array}{c} \mathbf {D} _ {k, i} = \left[ I - \frac {\Delta t}{2} p _ {k, i} - \frac {\Delta t}{2} \omega_ {s} \mathbf {T} \left(- \frac {\pi}{2 \omega_ {s}}\right) \right] ^ {- 1} \frac {\Delta t}{2} \\ \mathbf {P} _ {k, i} = \left[ I - \frac {\Delta t}{2} p _ {k, i} - \frac {\Delta t}{2} \omega_ {s} \mathbf {T} \left(- \frac {\pi}{2 \omega_ {s}}\right) \right] ^ {- 1} \frac {\Delta t}{2} \mathbf {T} (\Delta t) \end{array} \right. \tag {34}
$$

$i _ { m r } \left( t - \tau _ { k } \right) , i _ { m r } \left( t - \tau _ { k } - \Delta t \right)$ can be obtained by linear interpolations in time-domain. Take $i _ { m r } \left( t - \tau _ { k } \right)$ as an example, it can be calculated as:

$$
\begin{array}{l} i _ {m r} (t - \tau_ {k}) = \frac {n \Delta t - \tau_ {k}}{\Delta t} i _ {m r} [ t - (n - 1) \Delta t ] \\ + \frac {\tau_ {k} - (n - 1) \Delta t}{\Delta t} i _ {m r} [ t - n \Delta t ], \tau_ {k} \in \left[ (n - 1) \Delta t, n \Delta t \right], n = \left[ \tau_ {k} / \Delta t \right] + 1 \tag {35} \\ \end{array}
$$

D. Discussion on the Interface Model of the Multi-rate Cosimulations

Two types of multi-domain transmission line model are detailed, i.e., the Bergeron based MD-TLM and frequency dependent MD-TLM. The accuracy of these two types of MD-TLM is guaranteed by the network partitioning of interfaces, and the data conversion of interfaces between phasor-domain and time-domain. How to choose the desired MT-TLM, such as the Bergeron based MD-TLM or the frequency dependent MD-TLM, is dependent upon the expected frequency band of interfaces. Specifically, the Bergeron model is suitable for studies where dynamics around the fundamental frequency are more interested, such as many load flow and protection studies. However, if high frequency dynamics, especially wide frequency band interactions, are interested, the more accurate frequency dependent models are recommended. The drawback

of the so-called frequency dependent MD-TLM is that it will increase computational burden, but not that much. As all the parameters of the frequency dependent MD-TLM can be calculated before the simulations, the increased computation is still acceptable. Therefore, to choose which model is dependent upon whether the accuracy, the wide frequency band representation or the efficiency is the first priority.

![](images/f18c41fc8d372671160de0ae1bd384368adecaedfe4f7c7106c5b694ee6167af.jpg)  
Fig. 3. Geographical wiring diagram of the target system.

![](images/428b37ccf40a6a35d91cdd334e5d7ceab189030e1283c360b81ac846da98ecd6.jpg)  
Fig. 4. The types and capacities of wind farms in Guyuan area.

# IV. NUMERICAL TESTS AND VALIDATIONS

The proposed multi-rate co-simulation method is tested on the Guyuan system in China, where a total of 24 wind farms are geographically distributed in different locations (see Fig. 3). All these wind farms distributed throughout the Guyuan area are radially connected to the 220kV substations of Guyuan, Chabei, Yiyuan and Bailongshan. Then, the electric power is collected at the 500kV Guyuan substation and next transmitted along two 500kV corridors, each with doublecircuit series-compensated transmission lines, to the North-China power grid. Four sets of fixed series capacitors (FSCs) are installed on the two parallel transmissions connecting Guyuan substation with Hanhai and Taiping substations. And

the compensation degrees are 40% and 45%, respectively. To show the benefits of the proposed method, an asymmetric fault scenario, simulation with or without harmonic injections, sub- and super-synchronous oscillation(S2SO) events, and impedance measurements are both tested. Specifically, different time-steps (from 50µs to 500µs) are adopted to compare the proposed method with the traditional one. Meanwhile, the simulation results under a unanimous time-step of 5µs are used as the high-fidelity reference values. In our case, all the wind farms are included in the EMT subsystem, the rest of the largescale AC grids is included in the SFP subsystem. The timestep of the EMT subsystem is set as a unanimous time-step of 5µs in order to capture detailed dynamics of power electronic devices. The time-step of the EMT subsystem is set from 50µs to 500µs in order to capture electro-mechanical dynamics of AC system. The “multi-rate 50µs” by the proposed method is referred to the simulation method where the time-steps of the SFP and EMT subsystems are 50µs and 5µs respectively.

Concerning the implementations of the proposed method, the SFP subsystem is simulated by a custom developed simulation package, which is written in C++. The EMT subsystem is simulated by PSCAD/EMTDC. The proposed interface models, Bergeron based MD-TLM and the frequency dependent MD-TLM, are implemented as two coordinated modules in the custom developed simulation package and PSCAD/EMTDC based on the memory sharing techniques.

# A. Description of the Simulated System

As depicted in Fig. 3, the description of the scale of the AC system is summarized in Table I. The AC grid covers the majority of ac system of Hebei Province. There are more than 400 buses including 525kV buses and 220kV buses.

TABLE I DESCRIPTION OF SCALE OF THE AC SYSTEM   

<table><tr><td>bus number</td><td>generator number</td><td>load number</td><td>transmission line number</td></tr><tr><td>412</td><td>99</td><td>219</td><td>537</td></tr></table>

The description of types and capacities of wind farms in Guyuan area is given in Fig. 4. There are three types of WTGs, namely SEIG (Type 2), DFIG (Type 3) and PMSG (Type 4), installed at those wind farms. Among the total 3426.55 MW installed capacity, 82.8%, 15.4% and 1.8% of the wind power are provided by DFIGs, PMSGs and SEIGs, respectively. Clearly, DFIG accounts for most of the proportion. For each wind farm, the installed capacity and the types of WTG are illustrated in Fig. 4. Most wind farms contain only single type of WTG. For example, the wind farms of Hanjiazhuang, Zhongbao, Muchang and Qilinshan are entirely made up of DFIGs; while Youyi and Dongshan are purely PMSG-based. A very few farms, for instance, Jinyang, Batou, Hengtai and Bingfeng, contains two or three types of WTGs.

# B. Scenario 1: A single-phase resistive fault

1) Simulation results of the single-phase resistive fault

![](images/00e60840892afdcc8277b095bb1871b7ef136d1e0255cc00c1a77e9be7694187.jpg)

![](images/925dcbd151538791c5c16f2d88a58c492393fc78fd9e5d0126c9a3845017f413.jpg)

![](images/3f8141f96c5a6d54fa4cf6d005750dd55e143a26d57770b2d1ccdf93360c3e8e.jpg)

![](images/02985be49ef42cf75a3953d6d747cb7619728c390028c1d89de2bec97557004f.jpg)

![](images/8f8ddbb8f49d4073773e430dfc463dbe4efeb7057089c11dbb198678f98f79fc.jpg)

![](images/5c3c175b2908023ad1b10f9403006a2158cdd293544277b6613e088c1b7fd5ba.jpg)  
Multirate-50μs ? Multirate-200μs Multirate-500μs c ref

![](images/b1c4b74bd4cc9abaaf6f99b2ae589139d0fd9eba08a3977e6c6d92e26c493f1f.jpg)  
Fig. 5. Simulation results of output active/reactive power and frequency of wind farms under different time-steps.

![](images/a0bb164435aca45fc4e40de560d8d09f0732b31c93b9c0d5eea875203b9758de.jpg)

![](images/f9dfd9f2700024fa05997fca569e6a7deced5f34c6f70fa80bc22da23d311e7f.jpg)

![](images/40d181ca89fa02d055d691c5a47f5403f46361ef37a0b696b465be2e8a948c54.jpg)  
Fig. 6. Instantaneous and SFP curves of the connected AC voltages between wind farms and the large-scale AC grids.

![](images/402ef99758b0c8a4ebc8cf07af22be977ca530c91998869b3d98c1ced6746867.jpg)

![](images/1525d2966cf227b4803c37bf5199d4ab03438522d2d2f5db36914bc1829d80d4.jpg)  
Fig. 7. Instantaneous and SFP curves of the connected AC currents between wind farms and the large-scale AC grids.

The first simulation scenario is tested by triggering a singlephase resistive fault at t = 2.5s, which lasts for 0.05s. Simulation results of output active/reactive power and frequency of wind farms under different time-steps are illustrated in Fig. 5. As shown in Fig. 5(a-c), there will be sustained electromechanical transient process after the fault, which is aroused by interactions between wind farms and the large-scale AC grids. More importantly, Fig. 5(d-f) has demonstrated that even when the time-step is extended to 500µs, the proposed multi-rate co-simulation method can still achieve the satisfied accuracy. Typically, the largest error gap for the output active/reactive power of wind farms is less than 0.02/0.01 p.u.

Instantaneous and SFP curves of the connected AC voltages/currents between wind farms and the large-scale AC grids are shown in Figs. 6-7, respectively. Clearly, the proposed

multi-rate co-simulation method can give instantaneous and wide-band phasor values simultaneously, where the latter matches the envelopes of the former exactly. Particularly, the following conclusions can be reached: (1) the wide-band phasor waveforms can perfectly reflect interactions of both high- and low- frequency electromagnetic transients, even around the occasions of the occurrence and clearance of the fault; (2) As shown in Fig. 7, there will be sustained lowfrequency current oscillations of small amplitude after the fault is cleared. The reason is that such low-frequency oscillation is caused by the dynamics of generators’ and converters’ control in response to power swings.

2) Comparisons between multi-rate Bergeron based MD-TLM and frequency dependent MD-TLM

Fig. 8 compares the simulation results by using different in-

![](images/312cd34563c2673b2a801a135c76031ba6ebb7381b4caba44b4e10e1dfba99b8.jpg)  
Fig. 8. Comparisons of interface AC voltages based on MD-TLM/FD-MD-TLM model.

![](images/6f8c8091465acf54d21f0bfed1cf985202d376faeac985764a2dc9747dfdedb2.jpg)  
Fig. 9. Comparisons of active/reactive power of wind farms based on the proposed method and the traditional Thevenin equivalent circuit.

terface models, i.e., the multi-rate Bergeron MD-TLM and the multi-rate frequency dependent MD-TLM. As illustrated, both interface models based on the multi-rate Bergeron MD-TLM and the multi-rate frequency dependent MD-TLM can produce wide-band phasor and instantaneous values simultaneously, where the phasors are the exact envelopes of the instantaneous values at all occasions. Additionally, the FD-MD-TLM model, even the multi-rate one, can reflect the desired high frequency dynamics of interfacing while the MD-TLM model fails. Therefore, if high frequency interactions between wind farms and the large-scale AC grids are interested, the multi-rate FD-MD-TLM model is recommended.

3) Comparisons between multi-rate MD-TLM and the traditional Thevenin equivalent circuit

Fig. 9 compares the active/reactive power of wind farms based on the proposed method and the traditional Thevenin equivalent circuit, where the fault occurs at t = 2.5s and it lasts for 0.05s. The detailed model of the traditional method is represented as a Thevenin equivalent circuit. Specifically, it contains a Thevenin voltage source, which is rated at 550kV and a Thevenin impedance. The R and X value of the Thevenin

![](images/988cfcd8a56c0fa300239cd2b0ef0aefd7ce67e4541e25aae8f907e30d5a8ba3.jpg)  
Fig. 10. Instantaneous and phasor values of AC voltages; the spectrum of ac voltages without/with harmonics.

![](images/3875788479523075480e05525ff14720bfadd6a190407dfa48e7387735f63c6e.jpg)  
Fig. 11. Instantaneous and phasor values of AC currents; the spectrum of ac currents without/with harmonics.

impedance is 0.0016 p.u. and 0.029 p.u, respectively, where the X/R ratio is 18.12. As can be seen, the proposed method can give the expected electro-mechanical dynamics, where the traditional method based on the Thevenin equivalent circuit fails. Unexpectedly, there will be large gaps between the traditional equivalent method and the reference curve. Therefore, the traditional method can not consider the interactions between large-scale AC grid and the wind farms, where the AC grid is merely simplified as a Thevenin equivalent circuit.

The differences between the traditional equivalent method and the proposed method is illustrated in Fig. 9. For the traditional equivalent method, the active/reactive power return to the steady state very soon. On the contrary, the proposed method and the reference curve will produce sustained and damped electro-mechanical transient process. Normally, for the large-scale AC grids integrating large number of wind farms, the active/reactive power will oscillate slightly even during the steady state and the active/reactive power will become almost constant after a long time due to the interactions between large-scale AC grids and wind farms. As can be seen, only the proposed method and the reference curve will produce small and damped electro-mechanical dynamic process. However, the traditional equivalent method is always

constant, which is similar to the dynamics of an ideal voltage source. Judging from the comparative simulation results, we may conclude that in our simulation scenarios, the traditional equivalent method fails to capture interactions between AC grids and wind farms.

# C. Simulation Results Including Multiple Harmonics

The additional simulation results concerning multiple harmonics are given in Figs. 10-11. The simulation scenario is set as third and fourth harmonics are injected at the connected bus between SFP and EMT subsystems since $t = 1 . 5 s$ . The following conclusions can be reached: (1) Whether the system contains the harmonics or not, the derived SFP based phasors can exactly match the envelopes of instantaneous values; (2) The proposed MD-TLM can represent wide frequency band dynamics, including the third or even the fourth harmonics. The highest frequency limit of the desired wide frequency band interactions is determined by the Nyquist frequency of the time-step. The Nyquist frequency for the time-step of 500µs is calculated as $f _ { n y } = 1 / 2 \Delta T { = } 1 / 2 \times 5 0 0 e - 6 =$ 1000Hz. That is to say, dynamics when the frequency below 1000Hz, whether components at the sub-synchronous frequency or the super-synchronous frequency, can be accurately captured.

TABLE II EXECUTION TIME OF DIFFERENT METHODS DURING THE SINGLE-PHASE FAULT (SIMULATION PERIOD:5S)   

<table><tr><td rowspan="2">CPU Time/s</td><td>Multirate-500μs</td><td>Traditional (equivalent circuit)</td><td>reference</td></tr><tr><td>160</td><td>140</td><td>17196</td></tr></table>

As shown in Table II, the speedup of the proposed method during the single-phase fault is evident, especially when the time step is extended to 500µs, it achieves a speed-up of 100 times. On the contrary, the reference curve under the tiny and unanimous time-step of $5 \mu s$ will take around 4.7 hours for a period of 5s simulations. Why the reference curve takes around 5 hours to simulate 5s is due to the following reasons: (i) in order to obtain the desired accurate reference curve, the timestep of simulating the large-scale AC systems integrating large number of wind farms is restricted as a unanimous and tiny one of 5µs; (ii) the scale of AC system is quite large to cover the majority of Hebei Province, which is detailed in Table I; (iii) around hundreds of wind turbines are contained in each wind farm (The rated capacity of each wind turbine is 2-3 MW). The controllers of each wind turbine are designed according to practical controllers. The wind farms in our simulation case are much more complicated than the benchmark wind farm examples as the control and protection system is identical to the practical case. Therefore, the proposed method of the multi-rate one can achieve the expected efficiency acceleration.

# V. SCENARIO 2: THE SUB- AND SUPER-SYNCHRONOUS OSCILLATION $( S ^ { 2 } S O )$ EVENT

In order to demonstrate the effectiveness of our proposed method, the typical and famous sub- and super-synchronous

interactions $( \mathsf { S } ^ { 2 } \mathsf { S } \mathrm { I } )$ event is reproduced by the proposed method. The reason why we write this paper demonstrating the effectiveness of our proposed method is actually originated from practical engineering problems. As traditional methods, such as eletro-magnetic transient programs, transient stability programs, and even the hybrid EMT and TS simulations, cannot represent wide frequency interactions between largescale AC grids and wind farms. After that, we turn our attention to proposed the wide frequency band interface model.

As shown in Figs. 12-14, the first scenario is to simulate the $\mathrm { S } ^ { 2 } \mathrm { S O }$ event, where the series compensation is bypassed at $t = 2 . 6 s$ . From Fig. 12(a), the $\mathrm { \mathsf { S } } ^ { 2 } \mathrm { \mathsf { S } } \mathrm { \mathsf { O } }$ appears when the series compensation is bypassed. As is shown, the proposed method can produce instantaneous and wide frequency band phasors simultaneously. The phasor values of the proposed method can match the envelope of the instantaneous values exactly during the period of $\mathrm { \mathsf { S } } ^ { 2 } \mathrm { \mathsf { S } } \mathrm { \mathsf { O } }$ oscillations. Moreover, the spectrum of phasor values in Fig. 14-15 is shifted by 50Hz compared to the spectrum of the instantaneous values. As shown in Fig. 15, the super-synchronous component is 94Hz, higher than 50Hz. Figs. 10-14, all demonstrate that it is feasible on analyzing the sub-synchronous oscillation phenomena where the oscillation frequency would be higher than 50 Hz.

From Fig. 12, The $\mathrm { S } ^ { 2 } \mathrm { S O }$ event is re-simulated by the proposed method under different time steps. Evidently, the proposed method can satisfy the accuracy expectations even when the time-step is extended to 500µs. As shown in Fig. 14, there are three peaks, one is 50Hz, the other two is 6Hz and 94Hz. The sub-synchronous frequency is 6Hz and the super-synchronous frequency is 94Hz. The sub-synchronous and super-synchronous components are coupled and why the system will produce these two components is due to controllers of power electronic devices, which can be referred to [15]- [16].

Based on the proposed multi-rate co-simulations, the measured conductance matrix in modified sequence domain $\bf ( Y _ { p n } )$ and the calculated impedance matrix from dq domain [19] can be efficiently calculated, and these values overlap with each other perfectly (see Fig. 13). As shown in Table III, the speedup is evident, especially when the time step of the proposed method is extended to 500µs, showing its advantages in improving the efficiency. It should be noted that there are many additional components are added in the scenario 2, such as, the module to extract oscillation components at the sub- and super-synchronous frequencies, the matrix transform module, and the measurements and calculations of sub- and supersynchronous components. That is why the consumed time of scenario 2 is larger than that of scenario 1.

TABLE III EXECUTION TIME OF DIFFERENT METHODS DURING THE IMPEDANCE MEASUREMENT (SIMULATION PERIOD:5S)   

<table><tr><td rowspan="2">CPU Time/s</td><td>Multirate50μs</td><td>Multirate200μs</td><td>Multirate500μs</td><td>reference</td></tr><tr><td>1728</td><td>466</td><td>255</td><td>1.8 * 10^5</td></tr></table>

![](images/757c12f096e60870aea4c27b10adffd9f7f0c3b8273e18bcd245983eb6ae6a8b.jpg)

![](images/72d858903a18d27f142049703a42be40f738c40eae16910b889e5f06fc576fc8.jpg)

![](images/23e8e5c4a4baeee3b968bfdd3da41b216d4de4846f0c41f56b81f4cf8280f5b2.jpg)

![](images/1af6a54ddcbb6aab71a5851a4f40a5395fd125c7b084b13c021c2c6f74a3fa9a.jpg)

![](images/0466372155cd083db0b4e857e535062e48d8541cf8deb76aa46aff64fc78b7de.jpg)

![](images/aa2f8c5c5df182c5997a74d1147416aa80754f4ecf0ed8b457bdee7510709ce0.jpg)  
Multirate-50μs Multirate-200μs Multirate-500μs ref

![](images/f11d389c45724282e751078616efe52dcdc3265815b761379771b75a16560a39.jpg)  
Fig. 12. Simulation results of $\mathrm { s } ^ { 2 } \mathrm { S O }$ event under different time-steps.

![](images/8c1c2eb7e44086eaffe6913e08c808372fe3f9d3de3200fa83f079f05b3a8c81.jpg)

![](images/ae37361a94b6ba51cc9aad6a49cc60376b68d4abad9686783ab93f526760f19f.jpg)

![](images/0d41d4a9bce88962e6ba1a50ae7dc08c2fb699aff2ee68662717b250dc4b4f47.jpg)

![](images/ce952c6ad8467b21e9f424f388e67a3120b72bfc87125ed3c0a3a4e9d9da1a31.jpg)

![](images/6f29d7c7c8db1fc06c479ddf2a6493ee5d573e96f69fce7f008ff10f6911068a.jpg)

![](images/9725233d8d1bcc62abed3f71137a32d302c85353039c2fc745a541aedf61572b.jpg)

![](images/7489a7a4768470618331fcf8233d91a9553e2bf25c09fe43a7f983f336f2ed83.jpg)  
Fig. 13. Comparison of the measured conductance matrix in modified sequence domain $\bf ( Y _ { p n } )$ and the calculated impedance matrix from dq domain [13].

![](images/fb77b4dc211b98991d4eb0b55c048a7ba90b8c1dbe91ffb3d14f566fe2a3c57f.jpg)

![](images/85797c68939b2dc85a55fe15a1bf1823d43ae01bae9a8f479ba5f0e544dba8ed.jpg)  
Instantaneous value (x axis)   
Instantaneous value (y axis) Phasor value   
Fig. 14. Phase A current of Guyuan Station.

# VI. DISCUSSION ON THE FREQUENCY BAND OF THEPROPOSED MULTI-RATE MD-TLM

When the time-step of the SFP subsystem is extended to 500µs, the Nyquist frequency for the time-step of 500µs is calculated as:

$$
f _ {n y} = \frac {1}{2 \Delta T} = \frac {1}{2 \times 5 0 0 e - 6} = 1 0 0 0 H z \tag {36}
$$

where ∆T denote the time-step of SFP subsystem. That is to say, dynamics when the frequency below 1000Hz, whether

![](images/7be4f13954df49aa1e39dd5f189e28468ca320c3847757a6ccd8886cf592fad8.jpg)

![](images/35de9edb1e879d590c7f2ea3c02e16b03b9fe1fa90b2431d70e2fa85e59552ec.jpg)  
Fig. 15. Spectrum for instantaneous and phasor values phase A current .

components at the sub-synchronous frequency or the supersynchronous frequency, can be accurately captured. Therefore, the proposed multi-rate MD-TLM is a wide frequency band interface model, where the frequency band can be extended to 1000Hz at the time step of 500µs.

Moreover, the differences between the SFP models of largescale AC grids and the traditional steady state phasor model, positive sequence model are summarized as follows. Phasor model is actually a steady state model. Quantities at the steady state can be obtained by phasor model under the assumption

that all the components are symmetric. Therefore, phasor model is not suitable to study asymmetric/symmetric fault scenarios. Positive-sequence model is derived by transforming all the components from three-phase domain to three-sequence domain. It should be noted that only linear and symmetric components have their corresponding three-sequence models. Consequently, the positive-sequence model is only suitable to study symmetric faults. Finally, the advantages of the SFP models are summarized as follows:

(1) The time-step of the SFP models can be extended to 50-500µs. As a consequence, the proposed SFP models of large-scale AC grids can be significantly more efficient than those of electro-magnetic transient models.   
(2) The accuracy of SFP models can be guaranteed by the frequency shifting techniques. Therefore, the proposed SFP models can be as accurate as the EMT models, but achieving much improved efficiency.   
(3) The SFP models can be used to simulate any symmetric or asymmetric faults.

# VII. CONCLUSION

To accurately emulate the desired wide-band frequency interactions between the various components, this paper proposes a multi-rate co-simulation method. The proposed cosimulation method first partitions the whole system into the EMT and SFP subsystems, which are represented by our developed phasor-domain SFP models and time-domain EMT models, respectively. To capture the desired wide-band frequency interactions, the multi-rate multi-domain transmissionline model (MD-TLM) and the multi-rate frequency dependent MD-TLM are respectively proposed.

The performance (efficiency and accuracy) of the proposed method has been validated on fault scenario and the impedance measurement of a practical wind farm system. The results have demonstrated that:

i) The MD-TLM and FD-MD-TLM can capture the wideband frequency interactions under the so-called multi-rate structure, producing instantaneous and wide-band phasors simultaneously. The desired frequency band of the proposed interface models can be extended to 1000Hz at the time-step of 500µs.   
ii) With the proposed method, simulation errors are reduced to less than 0.02 p.u. even when the time-step us extended to 500µs.   
iii) the proposed method has achieved a speedup of 100 times in simulating a practical system with a time-step of 500 µ s.

# REFERENCES

[1] Sub-Synchronous Control Interaction in the vicinity of series capacitor banks,” in Proc. 2012 IEEE PES General Meeting, pp.1-5.   
[2] ABB. Inc., ERCOT CREZ Reactive Power Compensation Study, Dec. 2010.   
[3] L. Wang, X. Xie, Q. Jiang, H. Liu, Y. Li, and H. K. Liu, “Investigation of SSR in practical DFIG-based wind farms connected to a seriescompensated power system,” IEEE Trans. Power Syst., vol. 30, no. 5, pp. 2772-2779, Sept. 2015.   
[4] Sub-synchronous Resonance Working Group of the System Dynamic Performance Subcommittee, “Reader’s guide to sub-synchronous resonance,” IEEE Trans. Power Syst., vol.7, no. 1, pp. 150-157, Feb. 1992.

[5] J. Shair, X. Xie, L. Wang, W. Liu, “Overview of emerging subsynchronous oscillations in practical wind power systems” Renew. Sustain. Energy Rev., vol. 99, pp. 159–168, .Jan. 2019.   
[6] C. Zhang, X. Cai, M. Molinas and A. Rygg, “On the impedance modeling and equivalence of AC/DC side stability analysis of a gridtied Type-IV wind turbine system,” IEEE Trans. Energy Conver., vol. 34, no. 2, pp.1000-1009, Aug. 2018.   
[7] D. Shu, X. Xie, Q. Jiang, et. al, “A multirate EMT co-simulation of large AC and MMC-based MTDC systems,” IEEE Trans. Power Syst., vol. 33, pp. 1252-1263, March 2018.   
[8] L. Fan, R. Kavasseri, Z. Miao, et al., ”Modeling of DFIG-based wind farms for SSR analysis,” IEEE Trans. on Power Del., vol. 25, no. 4, pp. 2073-2082, Oct. 2010.   
[9] P. Wang, Z. Zhang, Q. Huang, N. Wang, X. Zhang, and W. J. Lee, “Improved wind farm aggregated modeling method for large-scale power system stability studies,” IEEE Trans on Power Syst., pp. 1–1, 2018   
[10] A. A. van der Meer, M. Gibescu, M. A. M. M. van der Meijden, W. L. Kling, and J. A. Ferreira, “Advanced hybrid transient stability and EMT simulation for VSC-HVDC systems,” IEEE Trans. Power Del., vol. 30, no. 3, pp. 1057–1066, Jun. 2015.   
[11] M.V. Andreev, A. Gusev, et. a; ”Hybrid real-time simulator of large-scale power systems”, IEEE Trans Power Syst. vol. 34, no. 2, pp. 1404–1415, Oct. 2018.   
[12] F. Plumier, P. Aristidou ; C. Geuzaine ; T. Van Cutsem, “Co-simulation of electromagnetic transients and phasor models: A relaxation approach,” IEEE Trans. Power Del., vol. 31, no. 5, pp. 2360–2369, Mar. 2016   
[13] S. Chandrasekar and R. Gokaraju, “Dynamic phasor modeling of type 3 DFIG wind generators (including SSCI phenomenon) for short-circuit calculations,” IEEE Trans. on Power Del., vol. 30, no. 2, pp. 887–897, Apr. 2015.   
[14] Q. Qi, S. Chen, Y. Ni, and F. F. Wu, “Application of the dynamic phasors in modeling and simulation of HVDC,” in Proc. Int. Conf. Adv. Power Syst. Control, Oper. Manage., Hong Kong, Nov. 2003, pp. 185–190.   
[15] D. Shu, X. Xie, H. Rao, X. Gao, Q.Jiang, Y. Huang, “Sub- and super-synchronous interactions between STATCOMs and weak AC/DC transmissions with series compensations”, IEEE Trans. Power Electron., vol. 33, no. 9, pp.7424 - 7437, 2018.   
[16] Y. Xu, H. Nian, T. Wang, L. Chen, and T. Zheng, “Frequency coupling characteristic modeling and stability analysis of doubly fed induction generator,” IEEE Trans. Energy Convers., vol. 33, no. 3, pp. 1475–1486, Sep. 2018.   
[17] D. Shu, V. Dinavahi, X. Xie, and Q. Jiang, “Shifted frequency modeling of hybrid modular multilevel converters for simulation of MTDC grid,” IEEE Trans. Power Del., vol. 33, no. 3, pp. 1288–1298, Jun. 2, 2017.   
[18] K. Strunz, R. Shintaku, and F. Gao, “Frequency-adaptive network modeling for integrative simulation of natural and envelope waveforms in power systems and circuits,” IEEE Trans. Circuits Systems I, Reg. Papers, vol. 53, no. 12, pp. 2788–2803, Dec. 2006   
[19] A. Rygg, M. Molinas, C. Zhang, X. Cai, “On the Equivalence and Impact on Stability of Impedance Modeling of Power Electronic Converters in Different Domains,” IEEE J. Emerg. Sel. Top. Power Electron., vol. 5, no. 4, pp. 1444–1454, Dec. 2017.

![](images/6ccdae171ad2dde5d7d0ad1d4ae105a8080b20ffcf0fa4effa08b8c5765fcd6d.jpg)

Yupeng Li Yupeng Li received the B.S. degree in elelctrical engineering from Zhejiang University, Hangzhou, China, in 2008, and the M.S. degree in electrical engineering from Shanghai Jiaotong University, Shanghai, China, in 2011. He is currently working toward the Ph.D. degree in the Department of Elelctrical Engineering, Shanghai Jiaotong University. His research interents include modeling, analysis and control of power system with power electronic equipments.

![](images/6c1a3bb1d23145cc486573b5b665c90ca2158cab8234d0002dcd3a4069461a5c.jpg)

Dewu Shu (M’18) received the B.Sc. Ph. D degree in Electrical Engineering from Tsinghua University in 2013, 2018. Currently, he is the tenuretrack assistant professor in Electrical Engineering, Shanghai Jiaotong University. His research interests include multirate EMT/TS simulations, parallel and distributed computing.

![](images/56b2ad229f0f1915fc2e549769eba0e67a22d773f15c9c05e32a0db606b50188.jpg)

Fan Shi received the B.S. degree in elelctrical engineering from North China Electric Power University, Beijing, China, in 2017. He is currently working toward the M.S. degree in the Department of Elelctrical Engineering, Shanghai Jiao Tong University. His research interents include modeling, analysis and control of power system with power electronic equipments.

![](images/195836044bbc0607ca88294fc74c778aa81203fe0d13c114fc063a033d3f6fa0.jpg)

Zheng Yan (M’98) received the B.S. degree from Shanghai Jiao Tong University, Shanghai, China, in 1984 and the M.S. and Ph.D. degrees from Tsinghua University, Beijing, China, in 1987 and 1991, respectively, all in electrical engineering. He is currently a tenure Professor of Electrical Engineering with Shanghai Jiao Tong University. His current research interests include application of optimization theory to power systems, power markets, and dynamic security assessment.

![](images/c0abf9fb6d534c1e531d1cd3d9b7a68ac0998c41de24ff6d46705c8199867d72.jpg)

Yiying Zhu obtained the Master’s degree in Power System Engineering from China electric power research institute in 1998, obtained PH.D in North China Electric Power University in 2018. She is the director of the power system digital-analog hybrid simulation laboratory of State Grid Simulation Center which is a national key laboratory. Her main research areas are power system real time simulation, electromagnetic transient and HVDC.