# A Bridge-Arm-Module-Based Fixed-Admittance ADC Model for Converters in EMT Simulation

Yang Cao, Graduate Student Member, IEEE, Xiaodong Yuan , Huachun Han , Mingwang Xu , Graduate Student Member, IEEE, Fei Zhang , Member, IEEE, and Wei Gu , Senior Member, IEEE

Abstract—Electromagnetic transient (EMT) simulation models, especially converter models, face challenges in meeting the demand for precise and fast simulation of complex dynamics in modern distribution systems. Difficulty in achieving both high accuracy and efficiency simultaneously is a key issue in converter modeling, especially in real-time simulation. To address this issue, this paper proposes a parametric fixed-admittance associated discrete circuit (ADC) converter model based on bridge arm modules (BAMs), with the aim of improving simulation precision and efficiency. The paper first establishes a parametric ADC model of the BAM. An optimal parameter calculation approach is introduced to ensure high fidelity through analysis of steady-state and transient characteristics. Furthermore, to mitigate initial errors caused by state switching, a cross-re-initialization (CRI) method combined with improved state determination expressions for specific topologies is developed, effectively correcting these errors without compromising computational efficiency. Simulation and experimental results validate the effectiveness of the BAM-ADC model, highlighting its high precision, high efficiency, and broad applicability.

Index Terms—Associated discrete circuit (ADC), fixed-admittance model, power converter modeling, real-time simulation, virtual power loss.

## I. INTRODUCTION

T HE technological innovation of third-generation powerelectronic switches and the widespread adoption of electronic switches and the widespread adoption of converter-interfaced generation technologies have led to a substantial increase in dynamic response characteristics within modern power systems. As a result, the definition of power system stability has evolved to encompass “converter-driven stability” [1], [2], allowing for a more comprehensive assessment of the impact of fast-response power electronics. Converter-driven stability is primarily influenced by power converters and related control. The growing incorporation of renewable energy sources and the proliferation of power electronics offer significant promise for energy applications, but they also pose safety and stability challenges [3], [4]. This highlights the necessity for precise simulation and analysis of power systems [5]. Traditional electromagnetic transient (EMT) simulation models are inadequate for meeting the requirements of new distribution systems [6], which underscores the growing importance of accurate and efficient power electronic converter models [7], [8], [9].

In EMT simulations, achieving both high accuracy and high efficiency is crucial for converter modeling, especially in realtime simulation [8], [10], [11]. Presently, simulation platforms such as PSCAD, RTDS, and OPAL-RT still adopt the RON/ROFF [12], [13] or the L/C-based associated discrete circuit (L/C-ADC) model [14], [15]. However, the former faces challenges in scaling due to inefficiency, while the latter imposes limitations on the maximum time step and suffers from virtual power loss.

Several studies have focused on improving efficiency without compromising accuracy by employing reduced-order methods. Reduced-order methods aim to reduce the matrix size from K to K-k by eliminating internal nodes or employing alternative solver architectures, thereby reducing the computational overhead. For the same system, the matrix inverse complexity is from O(K3) to O[(K-k) 3] after dimension reduction. Li et al. [16] and Gao et al. [17] established equivalent models based on ports and components rather than nodes and branches, effectively reducing matrix order. Zhang et al. [18] combined model order reduction with state prediction to improve the accuracy of voltage source converter models. Xu et al. [19] proposed a low-dimensional equivalent model using an alternating half-step decoupling method, improving simulation efficiency. RTDS [20] has proposed a universal converter model (UCM) based on descriptor state space equations, and OPAL-RT [21] has proposed improved switching function models based on state space equations. These state-space-equation-based models reduce the computational overhead, which can also be interpreted as a form of dimension reduction. Although these methods reduce the computational complexity of per matrix inversion, they still require repeated matrix inversions, failing to fundamentally alleviate the substantial computational burden imposed by frequent matrix inversions, especially as the system scale increases. Moreover, the internal operating states of the reduced-order systems are not directly accessible, necessitating additional computations.

Some studies have traded a certain degree of model accuracy for significant gains in computational efficiency. Among them, the fixed-admittance ADC models such as L/C-ADC are widely adopted in real-time simulation due to its high efficiency, as it avoids the most time-consuming updated matrix inversion [22]. As a result, L/C-ADC remains a key modeling approach in platforms like OPAL-RT [21] and RTDS [23], especially in FPGA-based simulations, where it offers notable advantages in scalability and smaller time steps over $\mathrm { R _ { O N } / R _ { O F F } }$ [24]. However, its limited accuracy remains a critical concern. To address this, several studies have aimed to enhance the accuracy of fixed-admittance ADC models by reducing virtual power loss [25]. Hou et al. [26] introduced negative impedance to improve accuracy, though this may compromise stability. Zhang et al. [27] proposed a general linearized method based on a fixed nodal admittance matrix tailored to voltage source converters (VSCs), which improves accuracy effectively. Models like G-ADC [28] and CI-ADC [29] have notably reduced virtual power loss through optimal parameter selection and initialization techniques. Nonetheless, their applicability remains limited in certain EMT simulation scenarios, especially under non-complementary states such as blocking modes, and further reductions in virtual power loss and spurious harmonic spikes are still required.

In summary, there are few models achieving high accuracy and high efficiency under multiple operating states. To solve this dilemma, this study proposes a bridge-arm-module-based ADC (BAM-ADC) model for system-level behavioral EMT simulation, which leverages the efficiency advantage of the fixed-admittance ADC model while enhancing accuracy by reducing virtual power loss. This model represents the steady-state and transient behavior of converters with sufficient efficiency and accuracy. The key innovations of this paper are:

- A parametric fixed-admittance ADC model based on BAMs is developed, with a constant admittance matrix that enables high efficiency and reduced computational overhead.

- An optimal parameter calculation method of the BAM-ADC is proposed, which can ensure the ideal steady-state and transient error convergence characteristics.

- A novel cross-re-initialization (CRI) method is proposed to correct state-switching errors, effectively reducing virtual power loss without increasing computational burden.

The rest of this paper is organized as follows: Section II introduces the fixed-admittance ADC model. Section III details the construction of the BAM-ADC model, including optimal parameter calculation via steady-state and transient characterization, and a CRI switching error correction method. Simulation and experimental validations are presented in Sections IV and V, respectively. Section VI concludes.

## II. PRELIMINARY STUDY OF FIXED-ADMITTANCE ADC MODEL

Accurate and efficient converter models are essential for EMT simulations, as they significantly influence simulation results. For high-precision converter models applicable in real-time simulations, the following characteristics are desirable:

- Throughout the simulation, the node admittance matrix should remain constant or be easily invertible.

![](images/9360ec0db5647de584680c810291000f6f01978b5ab68e5ae1a76e057a393148.jpg)  
Fig. 1. Overall time consumption comparison diagram of EMT simulation based on RON/ROFF and fixed-admittance ADC models.

![](images/2bdff3519ae51ba3cc838a86c395a9824c1c955667cd73e9109fd85a60752684.jpg)  
Fig. 2. L/C-ADC model of switches [14], [15].

- In steady-state operation, the switch model should exhibit zero voltage and non-zero current when ON and zero current and non-zero voltage when OFF.

- Following a transient event, the transient error should decay rapidly to near zero.

Once a state switching event occurs, the initial switching error should be close to zero.

In this context, transient error refers to the computational deviation following dynamic events, such as switching operations or system faults. A specific type of transient error is the initial switching error, which denotes the numerical discrepancy when state switching occurs, resulting from the inherent discontinuity of fixed-admittance ADC models at system transitions. These errors highlight the accuracy limitations of ADC models in capturing system dynamics compared to actual systems or high-fidelity reference models.

The core of converter modeling lies in the representation of power electronic switches. Among various models, the fixedadmittance ADC model is particularly notable for its high computational efficiency. This model is established based on the EMTP theory proposed by Dommel [13], [30], which discretizes switch components to form ADC models in Norton equivalent form. It avoids repeated admittance matrix inversion, one of the most computationally intensive steps in EMT simulation, by using fixed admittance, and replaces the inversion with updated calculation of equivalent current sources, reducing significant computational burden.

As illustrated in Fig. 1, ADC models require only a single inversion of the K-dimensional nodal admittance matrix throughout the simulation versus at least 2mN for RON/ROFF, where m is the number of carrier periods and N is the number of BAMs. Thus, without prior offline pre-computation of matrix data, time complexity scales as $O ( K ^ { \bar { 3 } } )$ for ADC models versus O(2mN·K3) for $\mathrm { R _ { O N } / R _ { O F F } }$ , indicating ADC models of higher efficiency and more suitable for real-time simulation.

L/C-ADC is a commonly used fixed-admittance model in realtime simulation, which treats the switch as an inductor when ON and a capacitor when OFF [31], as shown in Fig. 2. Using the backward Euler (BE) method as an example, the L/C-ADC model is formulated as:

![](images/d9420da76491ed47aa87e7fd8456c01636047666fdf2cbff900d20ea319dae85.jpg)  
Fig. 3. Variables of ADC swich model during transient events such as state switching at $t _ { n } \colon \mathrm { ( a ) }$ Current, (b) voltage and (c) power loss.

$$
i _ { \mathrm { s w } } ^ { n } = G _ { \mathrm { e q , s w } } \cdot u _ { \mathrm { s w } } ^ { n } + I _ { \mathrm { i n j , s w } } ^ { n } ,\tag{1}
$$

$$
G _ { \mathrm { e q , s w } } = \frac { h } { 2 L _ { \mathrm { s w } } } = \frac { 2 C _ { \mathrm { s w } } } { h } , I _ { \mathrm { i n j , s w } } ^ { n } = \left\{ \begin{array} { l l } { i _ { \mathrm { s w } } ^ { n - 1 } , } \\ { - G _ { \mathrm { e q , s w } } \cdot u _ { \mathrm { s w } } ^ { n - 1 } , } \end{array} \right.\tag{ON}
$$

OFF

(2)

where $i _ { \mathrm { s w } }$ and $u _ { \mathrm { s w } }$ denote the switch current and voltage, respectively; $G _ { \mathrm { e q , s w } }$ and $I _ { \mathrm { i n j , s w } }$ are the equivalent admittance and historical injected current source; index n refers to the $n ^ { \mathrm { t h } }$ discrete moment; h is the simulation step; $L _ { \mathrm { s w } }$ and $C _ { \mathrm { s w } }$ are the virtual inductance and capacitance of switch, respectively.

While the L/C-ADC model offers a physically interpretable structure and high computational efficiency, it suffers from spurious harmonic spikes and virtual power loss, which significantly degrade simulation accuracy. As shown in Fig. 3, the virtual power loss refers to the additional power loss due to the non-ideal energy changes of ADC switch models, while the spurious harmonic spikes appear as voltage or current spikes at transient events such as state switching.

These issues impose severe limitations on the maximum feasible time step and increase hardware demands, thus making precise EMT simulation analysis highly difficult. Consequently, there is a need for more accurate fixed-admittance ADC models that can address these challenges without sacrificing computational efficiency.

## III. CONSTRUCTION OF BAM-ADC MODEL

Reducing virtual power loss is difficult by constructing improved fixed-admittance ADC models of individual switches, as a single switch unit struggles to compensate for computational errors using its own internal variables. In power converters, switch units typically operate in pairs within the same BAM and jointly determine the steady-state and transient response characteristics. The variables of one switch unit can help correct the computational deviations of the other. Therefore, this study shifts focus from individual switch units to BAMs, aiming to capture converter dynamics more accurately by considering the overall behavior of switch pairs.

Remark 1: The switch unit with BAMs may consist of a primary switch and an anti-parallel diode (e.g., IGBT + diode), or refer to an individual device (e.g., diode, IGBT).

In this section, a parametric fixed-admittance BAM is constructed as the basic building module of converters. Through the analysis of its steady-state and transient characteristics, the optimal parameters of BAMs are derived to ensure high simulation accuracy. Compared to CI-ADC [29], BAM-ADC achieves higher accuracy, offers more rigorous analytical foundations without constant capacitor voltage assumption, and allows flexible integration with L/C-ADC to simulate non-complementary conduction states. Furthermore, an improved switching error correction method (CRI) is considered, which significantly outperforms the CI method of CI-ADC, especially considering non-complementary states.

## A. Parametric Fixed-Admittance ADC Model

Before modeling, the following statement is needed. For the derivation of BAM-ADC, only the complementary conduction states of two switch units within the BAM are considered. Noncomplementary conduction states fall outside the standalone application scenario of the BAM-ADC model and should be simulated in conjunction with the L/C-ADC model.

Based on this, the BAM in converters typically operates in two complementary conduction states: (1) S1 ON, S2 OFF, and $( 2 ) S _ { 1 }$ OFF, $S _ { 2 }$ ON. These two states are essentially two discrete-time systems. Besides, (3) $S _ { 1 }$ OFF, $S _ { 2 }$ OFF is a non-complementary state to be separately discussed later.

The structure of the parametric ADC model of BAMs is developed as shown in Fig. 4. The equivalent current source I n inj is calculated based on variables $u ^ { n - 1 }$ and $i ^ { n - 1 }$ , with inductors and capacitors discretized using the trapezoidal rule (TR):

$$
\left\{ \begin{array} { l l } { i _ { 1 } ^ { n } = G _ { \mathrm { e q } , 1 } u _ { 1 } ^ { n } + I _ { \mathrm { i n j } , 1 } ^ { n } = G _ { \mathrm { e q } , 1 } u _ { 1 } ^ { n } + \alpha _ { 1 } G _ { \mathrm { e q } , 1 } u _ { 1 } ^ { n - 1 } + \beta _ { 1 } i _ { 1 } ^ { n - 1 } } \\ { i _ { 2 } ^ { n } = G _ { \mathrm { e q } , 2 } u _ { 2 } ^ { n } + I _ { \mathrm { i n j } , 2 } ^ { n } = G _ { \mathrm { e q } , 2 } u _ { 2 } ^ { n } + \alpha _ { 2 } G _ { \mathrm { e q } , 2 } u _ { 2 } ^ { n - 1 } + \beta _ { 2 } i _ { 2 } ^ { n - 1 } } \\ { i _ { L } ^ { n } = G _ { \mathrm { e q } , L } u _ { L } ^ { n } + I _ { \mathrm { i n j } , L } ^ { n } = G _ { \mathrm { e q } , L } u _ { L } ^ { n } + G _ { \mathrm { e q } , L } u _ { L } ^ { n - 1 } + i _ { L } ^ { n - 1 } } \end{array} \right.\tag{3}
$$

where  and $\beta$ denote voltage and current coefficients, respectively. The equivalent admittances of inductors and capacitors are defined as $G _ { \mathrm { e q } , L } = h / 2 L _ { \mathrm { a c } }$ and $G _ { \mathrm { e q } , C } = 2 C _ { \mathrm { d c } } / h$ . Subscripts 1, 2, $L ,$ and C refer to the upper switch, lower switch, inductor, and capacitor in the BAM.

## B. Steady-State Characterization

To ensure that the BAM exhibits ideal steady-state characteristics, it is first necessary that each individual switch unit presents ideal steady-state behavior. The ideal steady-state characteristics of a switch unit can be defined as:

$$
\begin{array}{c} \{ \underset { t  + \infty } { \operatorname* { l i m } } u _ { \mathrm { s w } } ( t ) = 0 , \underset { t  + \infty } { \operatorname* { l i m } } i _ { \mathrm { s w } } ( t ) \neq 0 , \mathrm { O N }  \\ { \underset { t  + \infty } { \operatorname* { l i m } } i _ { \mathrm { s w } } ( t ) = 0 , \underset { t  + \infty } { \operatorname* { l i m } } u _ { \mathrm { s w } } ( t ) \neq 0 , \mathrm { O F F } } \end{array}  .\tag{4}
$$

To clearly understand the steady-state characteristics of the switch unit, it is essential first to analyze its steady-state conditions in both ON and OFF states. Derived from (3), the Z-domain representation of the switch unit can be expressed as

$$
I _ { \mathrm { s w } } ( z ) = G _ { \mathrm { e q } } \cdot U _ { \mathrm { s w } } ( z ) + \alpha G _ { \mathrm { e q } } \cdot z ^ { - 1 } U _ { \mathrm { s w } } ( z ) + \beta \cdot z ^ { - 1 } I _ { \mathrm { s w } } ( z )\tag{z(5}
$$

According to the Final Value Theorem of the Z Transform, the steady-state values of ON-state voltage $u _ { \mathrm { s w } }$ and OFF-state

![](images/eba35ca95294727cc7c94320fa27ed6d2dcfdf96e9a00c491a03c4f249b0f759.jpg)  
Fig. 4. Parametric ADC model of BAMs based on half-bridge structure and its typical applicable converter topologies.

current $i _ { \mathrm { s w } }$ are determined as [28]:

$$
\begin{array}{c} \left\{ \operatorname* { l i m } _ { n \to + \infty } u _ { \mathrm { s w } } ^ { n } = \operatorname* { l i m } _ { t \to + \infty } u _ { \mathrm { s w } } ( t ) = \frac { 1 - \beta _ { 0 \mathrm { N } } } { 1 + \alpha _ { 0 \mathrm { N } } } \cdot \frac { 1 } { G _ { \mathrm { e q } } } \operatorname* { l i m } _ { t \to + \infty } i _ { \mathrm { s w } } ( t ) , \mathrm { O N }  \\ { \operatorname* { l i m } _ { n \to + \infty } i _ { \mathrm { s w } } ^ { n } = \operatorname* { l i m } _ { t \to + \infty } i _ { \mathrm { s w } } ( t ) = \frac { 1 + \alpha _ { 0 \mathrm { F F } } } { 1 - \beta _ { 0 \mathrm { F F } } } \cdot G _ { \mathrm { e q } } \operatorname* { l i m } _ { t \to + \infty } u _ { \mathrm { s w } } ( t ) , \mathrm { O F F } } \end{array} \right. .\tag{6}
$$

It indicates that the sufficient and necessary condition for the switch unit to ensure ideal steady-state characteristics of the parametric ADC model of BAMs is

$$
\left\{ \begin{array} { l } { \alpha _ { i } \neq - 1 , \beta _ { i } = 1 , \mathrm { O N } } \\ { \alpha _ { i } = - 1 , \beta _ { i } \neq 1 , \mathrm { O F F } } \end{array} , i \in \{ 1 , 2 \} . \right.\tag{7}
$$

To accurately simulate an ideal converter, the parameters of BAM must not only satisfy (7) but also be carefully selected to ensure good transient performance, including fast convergence of numerical errors and minimal initial error at state switching. These will be further addressed in subsequent sections.

## C. Transient Error Convergence Characterization

In EMT simulation, accurately capturing the transient behavior of converters is essential. The following two key characteristics define the main transient performance:

- After a transient event, the system’s response should rapidly converge to the new steady state.

- At the instant of state switching, the initial error should be sufficiently small to meet high-precision requirements.

This subsection focuses on the error convergence, while the initial switching error is discussed in the following section.

In an ideal converter model, state transitions after transient events are achieved almost instantaneously without a long error convergence process, resulting in minimal transient error. In contrast, non-ideal ADC models inherently involve a convergence process, during which errors gradually diminish. A slower convergence rate is associated with lower accuracy. To analyze the transient error convergence characteristics, based on Kirchhoff’s Voltage Law and Kirchhoff’s Current Law, the internal variable relationships is derived as follows:

$$
\left\{ \begin{array} { l l } { u _ { \mathrm { d c } } ^ { n } = u _ { \mathrm { d c 1 } } ^ { n } - u _ { \mathrm { d c 2 } } ^ { n } = u _ { 1 } ^ { n } + u _ { 2 } ^ { n } } \\ { u _ { L } ^ { n } = u _ { \mathrm { d c 1 } } ^ { n } - u _ { \mathrm { a c } } ^ { n } - u _ { 1 } ^ { n } = u _ { \mathrm { d c 2 } } ^ { n } - u _ { \mathrm { a c } } ^ { n } + u _ { 2 } ^ { n } \ . } \\ { i _ { L } ^ { n } = i _ { 1 } ^ { n } - i _ { 2 } ^ { n } } \end{array} \right.\tag{8}
$$

Given (8), the operating state of BAM at any moment can be determined using one voltage and any two currents, from which all other variables can be computed.

Taking the status with $S _ { 1 }$ OFF and $S _ { 2 }$ ON as an example, it can be obtained from (7) as:

$$
\left\{ \begin{array} { l l } { \alpha _ { 1 } = \alpha _ { \mathrm { O F F } } = - 1 , \beta _ { 2 } = \beta _ { \mathrm { O N } } = 1 } \\ { \beta _ { 1 } = \beta _ { \mathrm { O F F } } \neq 1 , \alpha _ { 2 } = \alpha _ { \mathrm { O N } } \neq - 1 } \end{array} \right.\tag{9}
$$

The remaining unknowns are the voltage coefficient $\beta _ { 1 }$ and current coefficient $\alpha _ { 2 }$ β. Substituting (8) and (9) into (3) yields:

$$
\left\{ \begin{array} { l l } { i _ { 1 } ^ { n } = - G _ { \mathrm { e q } , 1 } \big ( u _ { 2 } ^ { n } - u _ { 2 } ^ { n - 1 } \big ) + G _ { \mathrm { e q } , 1 } \big ( u _ { \mathrm { d c } } ^ { n } - u _ { \mathrm { d c } } ^ { n - 1 } \big ) + \beta _ { 1 } i _ { 1 } ^ { n - 1 } } \\ { i _ { 2 } ^ { n } = G _ { \mathrm { e q } , 2 } u _ { 2 } ^ { n } + \alpha _ { 2 } G _ { \mathrm { e q } , 2 } u _ { 2 } ^ { n - 1 } + i _ { 2 } ^ { n - 1 } } \\ { i _ { 1 } ^ { n } - i _ { 2 } ^ { n } = G _ { \mathrm { e q } , L } \big ( u _ { 2 } ^ { n } + u _ { \mathrm { d c 2 } } ^ { n - 1 } - u _ { \mathrm { a c } } ^ { n } \big ) } \\ { \qquad + G _ { \mathrm { e q } , L } \big ( u _ { 2 } ^ { n - 1 } + u _ { \mathrm { d c 2 } } ^ { n - 1 } - u _ { \mathrm { a c } } ^ { n - 1 } \big ) + i _ { 1 } ^ { n - 1 } - i _ { 2 } ^ { n - 1 } } \end{array} \right.\tag{10}
$$

Then, organizing (10) yields:

$$
\begin{array} { r l } & { u _ { 2 } ^ { n } = \left( k _ { 1 } - \alpha _ { 2 } k _ { 2 } - k _ { L } \right) u _ { 2 } ^ { n - 1 } + ( \beta _ { 1 } - 1 ) k _ { 1 } \cdot i _ { 1 } ^ { n - 1 } \big / G _ { \mathrm { e q } , 1 } } \\ & { \qquad + k _ { L } \left[ ( u _ { \mathrm { a c } } ^ { n } - u _ { \mathrm { d c 2 } } ^ { n } ) + ( u _ { \mathrm { a c } } ^ { n - 1 } - u _ { \mathrm { d c 2 } } ^ { n - 1 } ) \right] + k _ { 1 } ( u _ { \mathrm { d c } } ^ { n } - u _ { \mathrm { d c } } ^ { n - 1 } ) } \end{array}\tag{11}
$$

Combining (10) and (11), we can derive the discrete-time dynamic equation:

$$
\begin{array} { r } { \pmb { x } _ { 1 } ^ { n } = \left[ \pmb { u } _ { 2 } ^ { n } \right. } \\ { \left. i _ { 1 } ^ { n } / G _ { \mathrm { e q } , 1 } \right] = \pmb { A } _ { 1 } \cdot \left[ \pmb { u } _ { 2 } ^ { n - 1 } / G _ { \mathrm { e q } , 1 } \right] + \pmb { b } _ { 1 } ^ { n } } \end{array}\tag{12}
$$

where

$$
\{ \begin{array} { l } { \displaystyle A _ { 1 } = [ \begin{array} { c c } { \displaystyle k _ { 1 } - \alpha _ { 2 } k _ { 2 } - k _ { L } } & { ( \beta _ { 1 } - 1 ) k _ { 1 } } \\ { \displaystyle - ( k _ { 1 } - \alpha _ { 2 } k _ { 2 } - k _ { L } ) \beta _ { 1 } - ( \beta _ { 1 } - 1 ) k _ { 1 } } \end{array} ] } \\ { \displaystyle b _ { 1 } ^ { n } = [ \begin{array} { c c } { \displaystyle k _ { L } } \\ { \displaystyle - k _ { L } } \end{array} ] ( u _ { \mathrm { a s } } ^ { n } + u _ { \mathrm { a c } } ^ { n - 1 } - u _ { \mathrm { a c 2 } } ^ { n } - u _ { \mathrm { a c 2 } } ^ { n - 1 } ) + [ \begin{array} { c c } { \displaystyle k _ { 1 } } \\ { \displaystyle - k _ { 1 } } \end{array} ] \Delta u _ { \mathrm { d c } } ^ { n } } \\ { \displaystyle = O ( k _ { L } ) + O ( k _ { C } ) = O ( \operatorname* { m a x } \{ k _ { L } , k _ { C } \} ) } \\ { \displaystyle \Delta u _ { \mathrm { c } } ^ { n } = k _ { C } ( \bar { t } _ { C } ^ { n } + \bar { t } _ { C } ^ { n - 1 } ) / ( G _ { \mathrm { e q , 1 } } + G _ { \mathrm { e q , 2 } } + G _ { \mathrm { e q , L } } ) = O ( k _ { C } ) } \\ { \displaystyle \bar { t } _ { L } ^ { n } = \bar { t } _ { \mathrm { d c } } ^ { n } - \bar { t } _ { 1 } ^ { n } = \bar { t } _ { \mathrm { d c 2 } } ^ { n } - \bar { t } _ { 2 } ^ { n } } \\ { \displaystyle k _ { i } = G _ { \mathrm { e q , 1 } } / ( G _ { \mathrm { e q , 1 } } + G _ { \mathrm { e q , 2 } } + G _ { \mathrm { e q , L } } ) , i \in \{ 1 , 2 \} } \\  \displaystyle k _ { L } = 1 - k _ { 1 } - k _ { 2 } = G _  \mathrm  e \end{array}\tag{13}
$$

In this expression, $x _ { 1 }$ denotes the state variable under the current operating state, $A _ { 1 }$ is the state matrix, $\pmb { b } _ { 1 }$ is the input

vector. The parameters $k _ { i } , k _ { L } .$ , and $k _ { C }$ represent the coefficients of the $i ^ { \mathrm { { t h } } }$ switch, the inductor, and the capacitor, respectively.

Then, the local truncation error $\varepsilon x _ { 1 }$ is given by:

$$
\left\{ \begin{array} { l l } { \varepsilon u _ { 2 } ^ { n } = ( k _ { 1 } - \alpha _ { 2 } k _ { 2 } - k _ { L } ) \cdot u _ { 2 } ^ { n - 1 } + ( \beta _ { 1 } - 1 ) k _ { 1 } \cdot i _ { 1 } ^ { n } / G _ { \mathrm { e q , 1 } } } \\ { \qquad + k _ { L } \cdot ( u _ { \mathrm { a c } } ^ { n } + u _ { \mathrm { a c } } ^ { n - 1 } - u _ { \mathrm { d c 2 } } ^ { n } - u _ { \mathrm { d c 2 } } ^ { n - 1 } ) + k _ { 1 } \Delta u _ { \mathrm { d c } } ^ { n } } \\ { \varepsilon i _ { 1 } ^ { n } / G _ { \mathrm { e q , 1 } } = [ 1 - ( k _ { 1 } - \alpha _ { 2 } k _ { 2 } - k _ { L } ) ] \cdot u _ { 2 } ^ { n - 1 } } \\ { \qquad + [ \beta _ { 1 } - ( \beta _ { 1 } - 1 ) k _ { 1 } ] \cdot i _ { 1 } ^ { n } / G _ { \mathrm { e q , 1 } } } \\ { \qquad - k _ { L } \cdot ( u _ { \mathrm { a c } } ^ { n } + u _ { \mathrm { a c } } ^ { n - 1 } - u _ { \mathrm { d c 2 } } ^ { n } - u _ { \mathrm { d c 2 } } ^ { n - 1 } ) + ( 1 - k _ { 1 } ) \Delta u _ { \mathrm { d c } } ^ { n } } \end{array} \right.\tag{14}
$$

This indicates that the numerical error of $x _ { 1 }$ is directly related to its convergence rate: a faster convergence leads to more rapid error attenuation.

The incremental change in the inductor current $\Delta i _ { L }$ is:

$$
\begin{array} { r l } & { \Delta i _ { L } ^ { n } / G _ { \mathrm { e q } , L } = i _ { L } ^ { n } / G _ { \mathrm { e q } , L } - i _ { L } ^ { n - 1 } / G _ { \mathrm { e q } , L } } \\ & { = \left[ 1 + ( k _ { 1 } - \alpha _ { 2 } k _ { 2 } - k _ { L } ) \right] u _ { 2 } ^ { n - 1 } + ( \beta _ { 1 } - 1 ) k _ { 1 } i _ { 1 } ^ { n - 1 } / G _ { \mathrm { e q , 1 } } } \\ & { \quad - \left( k _ { 1 } + k _ { 2 } \right) \cdot \left( u _ { \mathrm { a c } } ^ { n } + u _ { \mathrm { a c } } ^ { n - 1 } - u _ { \mathrm { d c 2 } } ^ { n } - u _ { \mathrm { d c 2 } } ^ { n - 1 } \right) + k _ { 1 } \cdot \Delta u _ { \mathrm { d c } } ^ { n } , } \end{array}\tag{u ,(15}
$$

II

which gives the corresponding truncation error $\varepsilon \Delta i _ { L }$

$$
\left\{ \begin{array} { l l } { \varepsilon \Delta i _ { L } ^ { n } / G _ { \mathrm { e q } , L } = \Delta i _ { L } ^ { n } / G _ { \mathrm { e q } , L } - \Delta i _ { L , \mathrm { i d e a l } } ^ { n } / G _ { \mathrm { e q } , L } } \\ { = \left[ 1 + ( k _ { 1 } - \alpha _ { 2 } k _ { 2 } - k _ { L } ) \right] u _ { 2 } ^ { n - 1 } + ( \beta _ { 1 } - 1 ) k _ { 1 } i _ { 1 } ^ { n - 1 } / G _ { \mathrm { e q } , 1 } } \\ { \quad + k _ { L } \cdot ( u _ { \mathrm { a c } } ^ { n } + u _ { \mathrm { a c } } ^ { n - 1 } - u _ { \mathrm { d c 2 } } ^ { n } - u _ { \mathrm { d c 2 } } ^ { n - 1 } ) + k _ { 1 } \cdot \Delta u _ { \mathrm { d c } } ^ { n } } \\ { \Delta i _ { L , \mathrm { i d e a l } } ^ { n } / G _ { \mathrm { e q } , L } = i _ { L , \mathrm { i d e a l } } ^ { n } / G _ { \mathrm { e q } , L } - i _ { L , \mathrm { i d e a l } } ^ { n - 1 } / G _ { \mathrm { e q } , L } } \\ { = u _ { \mathrm { d c 2 } } ^ { n } + u _ { \mathrm { d c 2 } } ^ { n - 1 } - u _ { \mathrm { a c } } ^ { n } - u _ { \mathrm { a c } } ^ { n - 1 } } \end{array} \right.\tag{16}
$$

It reveals that the error in $i _ { L }$ is also primarily influenced by the convergence behavior of $u _ { 2 }$ and $i _ { 1 }$ in this state. Slower convergence results in a larger cumulative error in $i _ { L }$ . Besides, based on (8), the numerical errors of other variables are also significantly affected by the convergence rate of $u _ { 2 }$ and $i _ { 1 }$

Derived from (13), the eigenvalue λ of $A _ { 1 }$ satisfies:

$$
\left\{ \begin{array} { l l } { { \lambda } ^ { 2 } - p \cdot { \lambda } + q = 0 } \\ { p = ( k _ { 1 } - \alpha _ { 2 } k _ { 2 } - k _ { L } ) + \beta _ { 1 } - ( \beta _ { 1 } - 1 ) k _ { 1 } . } \\ { q = ( k _ { 1 } - \alpha _ { 2 } k _ { 2 } - k _ { L } ) \beta _ { 1 } - ( \beta _ { 1 } - 1 ) k _ { 1 } } \end{array} \right.\tag{17}
$$

According to the Matrix Convergence Theorem, the convergence rate depends on the matrix spectral radius $\rho ( A _ { 1 } )$ ):

$$
\rho \left( A _ { 1 } \right) = \operatorname* { m a x } \left\{ \left| \lambda _ { 1 } \right| , \left| \lambda _ { 2 } \right| \right\} .\tag{18}
$$

The condition $\rho ( A _ { 1 } ) < 1$ defines the feasible domain for ρ <parameter selection, as shown in Fig. 5, ensuring convergence of the model. A smaller spectral radius indicates faster error reduction. The spectral radii $\rho ( A _ { 1 } )$ of conventional L/C-ADC ρmodels using BE and TR integration are also marked in Fig. 5:

$$
\left\{ \begin{array} { l l } { \rho _ { \mathrm { L } / \mathrm { C - A D C \mathrm { _ { - } B E } } } \left( A _ { \mathrm { 1 } } \right) = \operatorname* { m a x } \left\{ \left| \lambda _ { \mathrm { 1 } } \right| , \left| \lambda _ { \mathrm { 2 } } \right| \right\} = \sqrt { k _ { \mathrm { 1 } } } . } \\ { \rho _ { \mathrm { L } / \mathrm { C - A D C \mathrm { _ { - } T R } } } \left( A _ { \mathrm { 1 } } \right) = \operatorname* { m a x } \left\{ \left| \lambda _ { \mathrm { 1 } } \right| , \left| \lambda _ { \mathrm { 2 } } \right| \right\} = 1 . } \end{array} \right.\tag{19}
$$

Their relatively large values explain the slow convergence rate, leading to significant virtual power loss in L/C-ADC.

![](images/3f0db6575e15e620ef3291169bcdd16f97f0afd47dde575ed5be9b179ef08321.jpg)  
Fig. 5. Spectral radius of matrix $\rho ( A _ { 1 } )$ based on voltage coefficient $\beta _ { 1 }$ of OFF-state switch unit $S _ { 1 }$ and current coefficient $\alpha _ { 2 }$ of ON-state switch unit $S _ { 2 }$ with $G _ { \mathrm { e q } , 1 } = 1 \mathrm { S } , G _ { \mathrm { e q } , 2 } = 1 \mathrm { S }$ and $G _ { \mathrm { e q } , L } = 0 . 0 4 \ : \mathrm { S }$

Within the feasible domain, there are two parameter sets corresponding to zero spectral radius $\rho ( A _ { 1 } ) = 0$ :

$$
\mathrm { I . } \alpha _ { 1 } = - 1 , \beta _ { 1 } = \frac { \sqrt { k _ { 1 } } } { 1 + \sqrt { k _ { 1 } } } , \alpha _ { 2 } = \frac { k _ { 1 } + \sqrt { k _ { 1 } } - k _ { L } } { k _ { 2 } } , \beta _ { 2 } = 1 ,\tag{20}
$$

$$
\alpha _ { 1 } = - 1 , \beta _ { 1 } = \frac { \sqrt { k _ { 1 } } } { \sqrt { k _ { 1 } } - 1 } , \alpha _ { 2 } = \frac { k _ { 1 } - \sqrt { k _ { 1 } } - k _ { L } } { k _ { 2 } } , \beta _ { 2 } = 1 .\tag{21}
$$

Based on these parameters, the model will achieve the fastest error convergence due to the Matrix Convergence Theorem. Then, it can be derived that $\begin{array} { r } { A _ { 1 } \cdot A _ { 1 } = O } \end{array}$ , and $x _ { n }$ is derived as:

$$
\pmb { x } _ { 1 } ^ { n } = \pmb { A } _ { 1 } \cdot ( \pmb { A } _ { 1 } \cdot \pmb { x } _ { 1 } ^ { n - 2 } + \pmb { b } _ { 1 } ^ { n - 1 } ) + \pmb { b } _ { 1 } ^ { n } = \pmb { A } _ { 1 } \cdot \pmb { b } _ { 1 } ^ { n - 1 } + \pmb { b } _ { 1 } ^ { n }\tag{22}
$$

If no state switching occurs, using parameters from (20) yields:

$$
\begin{array} { r l r } {  { \pmb { x } _ { 1 } ^ { n } = [ \frac { k _ { L } ( u _ { \mathrm { a c } } ^ { n } - u _ { \mathrm { d c } 2 } ^ { n } + u _ { \mathrm { a c } } ^ { n - 1 } - u _ { \mathrm { d c } 2 } ^ { n - 1 } ) } { 1 + \sqrt { k _ { 1 } } } ] + O ( h \cdot \operatorname* { m a x } \{ k _ { L } , k _ { C } \} ) } } \\ & { } & { = O ( \operatorname* { m a x } \{ 2 k _ { L } \Big / ( 1 + \sqrt { k _ { 1 } } ) , 2 k _ { C } \cdot ( 1 + \sqrt { k _ { 1 } } ) \} ) } \\ & { } & { = O ( \operatorname* { m a x } \{ k _ { L } , k _ { C } \} ) , } \end{array}\tag{}
$$

while parameters from (21) give:

$$
\begin{array} { r } { \pmb { x } _ { 1 } ^ { n } = \left[ \frac { k _ { L } \left( u _ { \mathrm { a c } } ^ { n } + u _ { \mathrm { a c } } ^ { n - 1 } - u _ { \mathrm { d c } 2 } ^ { n } - u _ { \mathrm { d c } 2 } ^ { n - 1 } \right) } { 1 - \sqrt { k _ { 1 } } } \right] + O \left( h \cdot \operatorname* { m a x } \{ k _ { L } , k _ { C } \} \right) } \\ { ( 1 - \sqrt { k _ { 1 } } ) \cdot \Delta u _ { \mathrm { d c } } ^ { n } } \\ { = O \left( \operatorname* { m a x } \left\{ 2 k _ { L } \bigg / \left( 1 - \sqrt { k _ { 1 } } \right) , 2 k _ { C } \cdot \left( 1 - \sqrt { k _ { 1 } } \right) \right\} \right) } \\ { = O \left( \operatorname* { m a x } \left\{ k _ { L } , k _ { C } \right\} \right) } \end{array}\tag{}
$$

By comparing (23) and (24), the steady-state error of group I in (20) is smaller than that of group II in (21), making group I the preferred choice for high-accuracy BAM-ADC model.

The same applies when $S _ { 1 }$ is ON and $S _ { 2 }$ is OFF. Thus, the optimal parameters for the BAM-ADC model are:

1) when $S _ { 1 }$ is ON and $S _ { 2 }$ is OFF,

$$
\alpha _ { 1 } = \frac { k _ { 2 } + \sqrt { k _ { 2 } } - k _ { L } } { k _ { 1 } } , \beta _ { 1 } = 1 , \alpha _ { 2 } = - 1 , \beta _ { 2 } = \frac { \sqrt { k _ { 2 } } } { 1 + \sqrt { k _ { 2 } } } ,\tag{k(25}
$$

2) when $S _ { 1 }$ is OFF and $S _ { 2 }$ is ON,

$$
\alpha _ { 1 } = - 1 , \beta _ { 1 } = \frac { \sqrt { k _ { 1 } } } { 1 + \sqrt { k _ { 1 } } } , \alpha _ { 2 } = \frac { k _ { 1 } + \sqrt { k _ { 1 } } - k _ { L } } { k _ { 2 } } , \beta _ { 2 } = 1 .\tag{26}
$$

Furthermore, the error of $x _ { 1 }$ is obtained from (23):

$$
\varepsilon x _ { 1 } ^ { n } = O \left( \operatorname* { m a x } \left\{ 2 k _ { L } \bigg / \left( 1 + \sqrt { k _ { 1 } } \right) , 2 k _ { C } ( 1 + \sqrt { k _ { 1 } } ) \right\} \right) .\tag{27}
$$

From (27), the model error is related to $k _ { L }$ and $k _ { C }$ . The smaller $k _ { L }$ and $k _ { C }$ are, the smaller the error is. For example, if an error of less than one percent is required, it is desirable that both $2 k _ { L } / ( 1 + \sqrt { k _ { 1 } } )$ and $2 k _ { C } ( 1 + \sqrt { k _ { 1 } } )$ should be below 0.01. Therefore, a general selection guideline for the equivalent admittance of switch unit can be established: $G _ { \mathrm { e q } , L } < < G _ { \mathrm { e q , 1 } } + G _ { \mathrm { e q , 2 } } < <$ $G _ { \mathrm { e q } , \mathrm { } C } .$

To minimize the overall error, the following constraint should also be satisfied:

$$
2 k _ { L } \Big / \left( 1 + \sqrt { k _ { 1 } } \right) = 2 k _ { C } \cdot ( 1 + \sqrt { k _ { 1 } } )\tag{28}
$$

Assuming $G _ { \mathrm { e q } , 1 }$ and $G _ { \mathrm { e q } , 2 }$ take equal values, so the optimal switch admittance becomes:

$$
\left\{ \begin{array} { l l } { G _ { \mathrm { e q , 1 } } = G _ { \mathrm { e q , 2 } } = \frac { 2 \sqrt { G _ { \mathrm { e q } , L } \cdot G _ { \mathrm { e q , } C } } } { 4 + \sqrt { 8 - 8 p + p ^ { 2 } } - p } - \frac { G _ { \mathrm { e q , } L } } { 2 } } \\ { = \left( \frac { 2 } { 4 - p + \sqrt { ( 4 - p ) ^ { 2 } - 8 } } - \frac { p } { 2 } \right) \cdot \sqrt { \frac { C _ { \mathrm { d c } } } { L _ { \mathrm { a c } } } } } \\ { p = \sqrt { G _ { \mathrm { e q , } L } / G _ { \mathrm { e q , } C } } = h / \left( 2 \sqrt { L _ { \mathrm { a c } } \cdot C _ { \mathrm { d c } } } \right) } \end{array} \right.\tag{29}
$$

For ease of implementation, given that p is typically close to 0, the preferred switch admittance can be approximated as:

$$
G _ { \mathrm { e q , 1 } } = G _ { \mathrm { e q , 2 } } = { \frac { { \sqrt { 2 } } - 1 } { \sqrt { 2 } } } { \sqrt { G _ { \mathrm { e q , } L } \cdot G _ { \mathrm { e q , } C } } } = { \frac { { \sqrt { 2 } } - 1 } { \sqrt { 2 } } } { \sqrt { \frac { C _ { \mathrm { d c } } } { L _ { \mathrm { a c } } } } }\tag{L(30}
$$

Using this value of $G _ { \mathrm { e q , s w } }$ , the error of $\mathbf { \dot { x } } _ { 1 }$ can be obtained as:

$$
\begin{array} { r l r } & { } & { \varepsilon { \pmb x } _ { 1 } ^ { n } = O \left( 2 \operatorname* { m a x } \left\{ \frac { \frac { G _ { { \mathrm { e q } } , L } } { G _ { { \mathrm { e q } } , 1 } + G _ { { \mathrm { e q } } , 2 } } } { 1 + \sqrt { \frac { G _ { { \mathrm { e q } } , 1 } } { G _ { { \mathrm { e q } } , 1 } + G _ { { \mathrm { e q } } , 2 } } } } , \frac { 1 + \sqrt { \frac { G _ { { \mathrm { e q } } , 1 } } { G _ { { \mathrm { e q } } , 1 } + G _ { { \mathrm { e q } } , 2 } } } } { \frac { G _ { { \mathrm { e q } } , C } } { G _ { { \mathrm { e q } } , 1 } + G _ { { \mathrm { e q } } , 2 } } } \right\} \right) } \\ & { } & { = O \left( h \bigg / \sqrt { L _ { \mathrm { a c } } \cdot C _ { \mathrm { d c } } } \right) \quad \quad \quad \quad ( 3 1 ) } \end{array}
$$

It is evident that accuracy depends on the time step h and parameters $L _ { \mathrm { a c } } , C _ { \mathrm { d c } }$ . With appropriate choice of h, high accuracy of the BAM-ADC model can be achieved.

Once the optimal parameters are determined, the proposed BAM-ADC model can be constructed. Compared with L/C-ADC, it demonstrates much faster error convergence rate and significantly reduced transient error. Besides, each BAM operates independently, making the model well-suited for converters with multiple BAMs, such as multi-phase VSCs. Moreover, the optimal parameters and preferred switch admittance are isolated from external systems and only depend on the time step h and passive components (L, C), granting the model strong generalizability.

As for the non-complementary conduction state (both $S _ { 1 }$ and $S _ { 2 }$ are OFF), such as the blocking or standby mode, it is simulated using the L/C-ADC method as described in (1). The corresponding ADC parameters of BAM in this state are:

$$
\alpha _ { 1 } = - 1 , \beta _ { 1 } = 0 , \alpha _ { 2 } = - 1 , \beta _ { 2 } = 0\tag{32}
$$

In this state, additional logic is required to accurately determine the current operating state and to identify the timing of switching events. Although a fast state determination method for ADC-type models has been proposed in [15], its reliance on non-state variables can lead to unreliable judgments due to the presence of spurious harmonic spikes. Therefore, this study leverages state variables at the interface and considers the previous state and detailed topology for accurate state determination. Improved state determination expressions tailored to typical topologies are presented below, which enable more reliable and accurate state judgment.

$$
\mathit { B o o s t } : \left\{ \begin{array} { l l } { D ^ { n } = \tilde { g } _ { V } ^ { n } \cdot \left( D ^ { n - 1 } \cup V ^ { n - 1 } \right) \cdot f \left( i _ { L } ^ { n - 1 } < 0 \right) } \\ { \qquad + \tilde { g } _ { V } ^ { n } \cdot \left( \tilde { D } ^ { n - 1 } \cap \tilde { V } ^ { n - 1 } \right) \cdot f \left( u _ { \mathrm { a c } } ^ { n - 1 } > u _ { \mathrm { d c 1 } } ^ { n - 1 } \right) } \\ { V ^ { n } = g _ { V } ^ { n } \cdot \left( D ^ { n - 1 } \cup V ^ { n - 1 } \right) \cdot f \left( i _ { L } ^ { n - 1 } < 0 \right) } \\ { \qquad + g _ { V } ^ { n } \cdot \left( \tilde { D } ^ { n - 1 } \cap \tilde { V } ^ { n - 1 } \right) \cdot f \left( u _ { \mathrm { a c } } ^ { n - 1 } > u _ { \mathrm { d c 2 } } ^ { n - 1 } \right) } \end{array} \right.\tag{33}
$$

$$
V S C : \left\{ \begin{array} { r l } { S _ { 1 } ^ { n } = \tilde { g } _ { 2 } ^ { n } g _ { 1 } ^ { n } + \tilde { g } _ { 1 } ^ { n } \tilde { g } _ { 2 } ^ { n } \cdot \left( S _ { 1 } ^ { n - 1 } \cup S _ { 2 } ^ { n - 1 } \right) \cdot f \left( i _ { L } ^ { n - 1 } < 0 \right) } & { } \\ { + \tilde { g } _ { 1 } ^ { n } \tilde { g } _ { 2 } ^ { n } \cdot \left( \tilde { S } _ { 1 } ^ { n - 1 } \cap \tilde { S } _ { 2 } ^ { n - 1 } \right) \cdot f \left( u _ { \mathrm { a c } } ^ { n - 1 } > u _ { \mathrm { d c 1 } } ^ { n - 1 } \right) } & { } \\ { S _ { 2 } ^ { n } = \tilde { g } _ { 1 } ^ { n } g _ { 2 } ^ { n } + \tilde { g } _ { 1 } ^ { n } \tilde { g } _ { 2 } ^ { n } \cdot \left( S _ { 1 } ^ { n - 1 } \cup S _ { 2 } ^ { n - 1 } \right) \cdot f \left( i _ { L } ^ { n - 1 } > 0 \right) } & { } \\ { + \tilde { g } _ { 1 } ^ { n } \tilde { g } _ { 2 } ^ { n } \cdot \left( \tilde { S } _ { 1 } ^ { n - 1 } \cap \tilde { S } _ { 2 } ^ { n - 1 } \right) \cdot f \left( u _ { \mathrm { a c } } ^ { n - 1 } < u _ { \mathrm { d c 2 } } ^ { n - 1 } \right) } & { } \end{array} \right.\tag{34}
$$

where g denotes the gate control signal; $f \left( \cdot \right)$ is the indicator function, which equals to one when the condition holds; the superscript ∼ represents logical negation. Other topologies can be similarly treated based on their structure and interface variables, which require additional specific analysis.

## D. Initial Error Correction at State Switching

Despite the fast error convergence rate of the BAM-ADC model, non-negligible initial switching errors may still arise when the system transitions from one discrete-time state to another. To achieve high simulation accuracy, these errors must be appropriately corrected [25].

For instance, when the operating state of BAM is switched from $S _ { 1 } \mathrm { O N } , S _ { 2 } \mathrm { O F F }$ to S1 OFF, S2 ON at $t _ { n } ,$ non-state variables such as switch voltage and current in the $\mathrm { R _ { O N } / R _ { O F F } }$ models should change to new steady-state values at $t _ { n } ,$ as illustrated in Fig. 6(a). However, in conventional L/C-ADC models, state switching often introduces substantial spurious voltage and current spikes. The corresponding initial switching error of the L/C-ADC model in Fig. 6(b) can be derived from (12):

$$
\left\{ \begin{array} { l l } { \varepsilon u _ { 2 } ^ { n } = k _ { 1 } \cdot u _ { \mathrm { d c } } ^ { n - 1 } - k _ { 1 } \cdot \frac { i _ { L } ^ { n - 1 } } { G _ { \mathrm { e q } , 1 } } + O \left( \operatorname* { m a x } \left\{ k _ { L } , k _ { C } \right\} \right) } \\ { \frac { \varepsilon i _ { 1 } ^ { n } } { G _ { \mathrm { e q } , 1 } } = \left( 1 - k _ { 1 } \right) \cdot u _ { \mathrm { d c } } ^ { n - 1 } + k _ { 1 } \cdot \frac { i _ { L } ^ { n - 1 } } { G _ { \mathrm { e q } , 1 } } + O \left( \operatorname* { m a x } \left\{ k _ { L } , k _ { C } \right\} \right) } \\ { \frac { \varepsilon \Delta i _ { L } ^ { n } } { G _ { \mathrm { e q } , L } } = \left( 1 + k _ { 1 } \right) \cdot u _ { \mathrm { d c } } ^ { n - 1 } - k _ { 1 } \cdot \frac { i _ { L } ^ { n - 1 } } { G _ { \mathrm { e q } , 1 } } + O \left( \operatorname* { m a x } \left\{ k _ { L } , k _ { C } \right\} \right) } \end{array} \right.\tag{35}
$$

![](images/617bce95ecaad41be289441440ea16f69c4100a0c14b98c8484edd50f2284e2e.jpg)  
Fig. 6. State switching process at $t _ { n }$ of (a) $\mathrm { R o N } / \mathrm { R } _ { \mathrm { O F F } }$ model, (b) ADC models without error correction, and (c) ADC models using error correction method.

In [28], the G-ADC model employs the final steady-state value from the previous occurrence of the same operating state to calculate the equivalent current source. However, this approach neglects the dynamic process between two consecutive identical states. To address this, the cross-initialization (CI) method proposed in [29] improves the accuracy of switch voltage and current by initializing their values based on the variables of the opposite switch unit in the same BAM just before switching. Although the CI method effectively reduces virtual power loss under complementary states, it does not leverage the steady-state characteristics of the CI-ADC model for further refinement. Moreover, neither the G-ADC nor CI-ADC methods account for non-complementary conduction states, which limits their generality.

To extend the applicability of the BAM-ADC model, its initial switching error must be explicitly analyzed. For the same transition scenario from $S _ { 1 } \mathrm { O N } , S _ { 2 }$ OFF to $S _ { 1 }$ OFF, $S _ { 2 }$ ON, the initial state switching error of the BAM-ADC model without correction, as shown in Fig. 6(b), is given by:

$$
\left\{ \begin{array} { l l } { \varepsilon u _ { 2 } ^ { n } { = } { - } \sqrt { k _ { 1 } } u _ { \mathrm { d c } } ^ { n - 1 } - \frac { k _ { 1 } } { 1 + \sqrt { k _ { 1 } } } \frac { i _ { L } ^ { n - 1 } } { G _ { \mathrm { e q } , 1 } } + O ( \operatorname* { m a x } \left\{ k _ { L } , k _ { C } \right\} ) } \\ { \frac { \varepsilon i _ { 1 } ^ { n } } { G _ { \mathrm { e q } , 1 } } = \left( 1 + \sqrt { k _ { 1 } } \right) u _ { \mathrm { d c } } ^ { n - 1 } + \sqrt { k _ { 1 } } \frac { i _ { L } ^ { n - 1 } } { G _ { \mathrm { e q } , 1 } } + O ( \operatorname* { m a x } \left\{ k _ { L } , k _ { C } \right\} ) } \\ { \frac { \varepsilon \Delta i _ { L } ^ { n } } { G _ { \mathrm { e q } , L } } { = } \left( 1 - \sqrt { k _ { 1 } } \right) u _ { \mathrm { d c } } ^ { n - 1 } - \frac { k _ { 1 } } { 1 + \sqrt { k _ { 1 } } } \frac { i _ { L } ^ { n - 1 } } { G _ { \mathrm { e q } , 1 } } + O ( \operatorname* { m a x } \left\{ k _ { L } , k _ { C } \right\} ) } \end{array} \right.\tag{36}
$$

Likewise, this initial switching errors cannot be neglected.

To address this issue, we propose an improved cross-reinitialization (CRI) method for BAM-ADC based on the variable relationships described in (8). This method aims to correct the historical voltage and current values, basically aligning them with the theoretical steady-state values under the new operating condition, used in computing equivalent historical injected current sources at the next time step.

When state switching occurs, the CRI method re-initializes the internal variables at the end of the previous state and recalculates the equivalent injected current source $I _ { \mathrm { i n j } }$ based on the updated variables. By incorporating the steady-state values from (23) into error correction for voltage, the method further reduces initial switching errors and improves the simulation accuracy. The CRI values of internal variables are given by:

$$
\left\{ \begin{array} { l l } { u _ { 1 \mathrm { - } \mathrm { C R I } } ^ { n - 1 } { = } \tilde { S } _ { 1 } ^ { n } ( u _ { 1 } ^ { n - 1 } + u _ { L } ^ { n - 1 } ) + S _ { 2 } ^ { n } ( u _ { 2 } ^ { n - 1 } - u _ { L } ^ { n - 1 } ) + 2 k _ { L } u _ { \mathrm { t e m p } } ^ { n - 1 } } \\ { u _ { 2 \mathrm { - } \mathrm { C R I } } ^ { n - 1 } { = } S _ { 1 } ^ { n } ( u _ { 1 } ^ { n - 1 } + u _ { L } ^ { n - 1 } ) + \tilde { S } _ { 2 } ^ { n } ( u _ { 2 } ^ { n - 1 } - u _ { L } ^ { n - 1 } ) - 2 k _ { L } u _ { \mathrm { t e m p } } ^ { n - 1 } } \\ { u _ { L \mathrm { - } \mathrm { C R I } } ^ { n - 1 } = S _ { 1 } ^ { n } ( u _ { 1 } ^ { n - 1 } + u _ { L } ^ { n - 1 } ) - S _ { 2 } ^ { n } ( u _ { 2 } ^ { n - 1 } - u _ { L } ^ { n - 1 } ) - 2 k _ { L } u _ { \mathrm { t e m p } } ^ { n - 1 } } \\ { u _ { \mathrm { t e m p } } ^ { n - 1 } { = } \frac { S _ { 1 } ^ { n } } { 1 + \sqrt { k _ { 2 } } } ( u _ { 1 } ^ { n - 1 } + u _ { L } ^ { n - 1 } ) - \frac { S _ { 2 } ^ { n } } { 1 + \sqrt { k _ { 1 } } } ( u _ { 2 } ^ { n - 1 } - u _ { L } ^ { n - 1 } ) } \end{array} \right.\tag{37}
$$

$$
i _ { 1 _ { \mathrm { - } } \mathrm { C R I } } ^ { n - 1 } \mathrm { = } S _ { 1 } ^ { n } i _ { L } ^ { n - 1 } , i _ { 2 _ { \mathrm { - } } \mathrm { C R I } } ^ { n - 1 } \mathrm { = - } S _ { 2 } ^ { n } i _ { L } ^ { n - 1 } , i _ { L _ { \mathrm { - } } \mathrm { C R I } } ^ { n - 1 } \mathrm { = } ( S _ { 1 } ^ { n } \cup S _ { 2 } ^ { n } ) i _ { L } ^ { n - 1 }\tag{38}
$$

where $u _ { \mathrm { t e m p } }$ is an intermediate voltage variable derived from the steady-state conditions of BAM-ADC for computation.

Then, $I _ { \mathrm { i n j } }$ in (3) is calculated based on (37) and (38), which are subsequently used to calculate the circuit variables at $t _ { n } \mathrm { . }$

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { I _ { \mathrm { i n j } , i } ^ { n } = \alpha _ { i } \cdot G _ { \mathrm { e q } , } \cdot u _ { i \mathrm { \scriptscriptstyle - C R I } } ^ { n - 1 } + \beta _ { i } \cdot i _ { i _ { \mathrm { \scriptscriptstyle - C R I } } } ^ { n - 1 } , i \in \{ 1 , 2 \} } \\ { I _ { \mathrm { i n j } , L } ^ { n } = G _ { \mathrm { e q } , L } \cdot u _ { L _ { \mathrm { \scriptscriptstyle - C R I } } } ^ { n - 1 } + i _ { L _ { \mathrm { \scriptscriptstyle - C R I } } } ^ { n - 1 } } \end{array} \right. } \end{array}\tag{39}
$$

For the same switching event from $S _ { 1 }$ ON, $S _ { 2 }$ OFF to $S _ { 1 }$ OFF, $S _ { 2 }$ ON, the corrected initial switching errors through the CRI method in Fig. 6(c) can be expressed as:

$$
\left\{ \begin{array} { l l } { \varepsilon u _ { 2 } ^ { n } = \frac { k _ { L } } { 1 + \sqrt { k _ { 1 } } } \left[ ( u _ { \mathrm { a c } } ^ { n } - u _ { \mathrm { d c } 2 } ^ { n } ) + ( u _ { \mathrm { a c } } ^ { n - 1 } - u _ { \mathrm { d c } 2 } ^ { n - 1 } ) \right] } \\ { \qquad + O ( h \cdot \operatorname* { m a x } \{ k _ { L } , k _ { C } \} ) } \\ { \frac { \varepsilon i _ { 1 } ^ { n } } { G _ { \mathrm { e q } , 1 } } = \left( 1 + \sqrt { k _ { 1 } } \right) \Delta u _ { \mathrm { d c } } ^ { n } + O ( h \cdot \operatorname* { m a x } \{ k _ { L } , k _ { C } \} ) } \\ { \frac { \varepsilon \Delta i _ { L } ^ { n } } { G _ { \mathrm { e q } , L } } = \frac { 2 k _ { L } } { 1 + \sqrt { k _ { 1 } } } \left[ ( u _ { \mathrm { a c } } ^ { n } - u _ { \mathrm { d c } 2 } ^ { n } ) + ( u _ { \mathrm { a c } } ^ { n - 1 } - u _ { \mathrm { d c } 2 } ^ { n - 1 } ) \right] } \\ { \qquad + O ( h \cdot \operatorname* { m a x } \{ k _ { L } , k _ { C } \} ) } \end{array} \right.\tag{40}
$$

It is demonstrated that the corrected initial switching error by the CRI method matches the theoretical value in (23). Compared to uncorrected ADC models, the CRI method significantly mitigates spurious harmonic spikes by cross-re-initializing internal variables during state switching, without adding computational overhead.

In EMT simulation, the BAM-ADC model with CRI achieves computational efficiency comparable to conventional L/C-ADC models, while significantly reducing initial switching errors during state switching, particularly compared to uncorrected ADC models. Moreover, owing to its half-bridge-based modular structure, the BAM-ADC model can be applied to various converter topologies, as illustrated in Fig. 4.

The EMT simulation flowchart using the BAM-ADC model with the CRI method is shown in Fig. 7. In this framework, system components are categorized according to their dynamic characteristics. Low-frequency components, such as passive elements including capacitors, inductors, and transformers, exhibit relatively slow dynamics (milliseconds to seconds) and are modeled using conventional EMT techniques. In contrast, high-frequency components, such as power electronic switches, exhibit rapid transient behavior (microseconds to nanoseconds) and are modeled using the BAM-ADC method.

In summary, the BAM-ADC model provides both accurate steady-state and transient performance, closely resembling that of an ideal converter model. Its effectiveness will be further demonstrated through simulation and experimental validation in the following sections.

## IV. SIMULATION TEST

The simulation cases in this section are mainly conducted on ADS-RTSim, our self-developed simulation platform based on C++. The processor is Intel Core i7-12700H with 14 cores and 2.30 GHz. For accuracy comparison, the BAM-ADC, L/C-ADC, G-ADC [28], and CI-ADC [29] models are implemented in the platform, while the $\mathrm { R _ { O N } / R _ { O F F } }$ model is constructed in PSCAD as the reference benchmark. For efficiency analysis, to ensure a consistent testing environment, all models including

![](images/461efadaa866cf593f1375fd65ac7336af87afd005fbef1c7ae1a2b657223753.jpg)  
Fig. 7. Flowchart of EMT simulation using the BAM-ADC model with the CRI method.

BAM-ADC, L/C-ADC, G-ADC, CI-ADC, and $\mathrm { R _ { O N } / R _ { O F F } }$ are simulated on the same platform under identical conditions. Moreover, for the L/C-ADC model, the state determination strategy expressions in [15] are used.

Before simulation testing, we have assessed the recommended values of switch admittance $G _ { \mathrm { e q , s w } }$ used in G-ADC, CI-ADC, and BAM-ADC models, all of which are determined based on the time step and circuit L/C parameters:

$$
{ \left\{ \begin{array} { l l } { \mathrm { G - A D C ~ \& ~ C I - A D C : ~ } G _ { \mathrm { e q , s w } } = { \sqrt { \frac { C } { L } } } } \\ { \mathrm { B A M - A D C : ~ } G _ { \mathrm { e q , s w } } = { \frac { { \sqrt { 2 } } - 1 } { \sqrt { 2 } } } { \sqrt { \frac { C } { L } } } } \end{array} \right. } \Rightarrow G _ { \mathrm { e q , s w } } = { \sqrt { \frac { C } { 2 L } } }\tag{41}
$$

Although each model provides its own recommendation for $G _ { \mathrm { e q , s w } }$ , no single value is universally optimal across all models. Therefore, to maintain fairness and consistency in model comparison, we adopt a unified conductance value of $G _ { \mathrm { e q , s w } } =$ -(C/2L) in this section, which is of the same order of magnitude with all these recommended values.

Moreover, for clear visualization, figures labeled (a), (b), and (c) depict waveforms of different variables. For each waveform, subfigures (a1)–(a3), (b1)–(b3), and (c1)–(c3) provide first-level magnified views of the corresponding main figures. Subsequently, subfigures (a4)–(a6), (b4)–(b6), and (c4)–(c6) offer second-level zoomed-in views of selected regions within the first-level magnifications, enabling detailed observation of non-state variables such as switch voltage. This hierarchical zooming strategy is consistently applied across all simulation cases for clarity and comparative analysis.

![](images/626c7dfa36cd683b736f6a7392e0be9af438c8ba52745384b3b8a4b675baec8e.jpg)  
Fig. 8. Boost chopper system.

## A. DC-DC Converter: Boost Chopper

A boost chopper circuit is constructed as shown in Fig. 8, employing an asymmetric topology composed of one BAM containing two independent switches. The relevant parameters are listed in Appendix A. The simulation lasts for 0.05 s with a time step of 2 s. The converter is in disable mode before 0.01 s μand after 0.04 s. A DC source fault is applied at 0.02 s, dropping the voltage to 0 V, and restoring it to 40 V at 0.03 s.

The waveforms are presented in Figs. 9, 10, 11, and 12.

As shown in Fig. 9, the BAM-ADC model accurately captures the circuit behavior under disable mode and fault conditions, with results consistent with those of the $\mathrm { R _ { O N } / R _ { O F F } }$ model. In contrast, the L/C-ADC model exhibits significant deviation due to its inherent modeling limitations, resulting in substantial spurious voltage spikes and virtual power loss in Fig. 10. These figures highlight the low accuracy of L/C-ADC and its limited capability in handling switching events. The BAM-ADC model, by contrast, effectively suppresses spurious voltage spikes and associated virtual power losses, achieving both high accuracy and reliable state judgment.

![](images/e4fab7bfcefea61c0f42194a4e82af85fc3d1082fa4a1b2da00bfec175946846.jpg)  
Fig. 9. Waveforms of (a) inductor current and (b) load current. (a) $i _ { L } \ \mathrm { ( A ) } .$ (b) iload (A).

![](images/1ebf59cb4feabb49831b4e04185e6a5b66a83ea66d8c79db4ec71a388ad2cb3f.jpg)  
Fig. 10. Waveforms of (a) voltage and (b) virtual power loss of switch V. (a) uV (V). (b) $\mathrm { \mathit { P } _ { l o s s } } \mathrm { v D }$ (kW).

Additionally, Fig. 9 illustrates that the G-ADC and CI-ADC models exhibit noticeable deviations under the disable mode and fault conditions. This highlights their limited applicability in non-complementary states, as both models are constructed under complementary state assumptions. Further analysis in Fig. 10 reveals that their voltage spikes and virtual power loss are increased compared to the BAM-ADC model, thereby confirming the better accuracy performance of BAM-ADC.

To further examine the impact of the recommended switch admittance $G _ { \mathrm { e q , s w } }$ and simulation time step h on simulation accuracy, two additional tests are conducted:

1) The first test investigates the effect of varying the switch admittance from 1/100 to 100 times the recommended value, as shown in Fig. 11. The results indicate that the optimal value yields the highest accuracy. While moderate deviations are observed at 1/10 and 10 times, significant errors occur at 1/100 and 100 times due to large $k _ { C }$ or $k _ { L }$ , thereby validating the appropriateness of the optimal admittance selection.

![](images/4417a659515b38aaddceb47bff580e20550788d6720429b4b32015e3707c8d27.jpg)  
Fig. 11. Waveform comparison of the BAM-ADC model under different values of $G _ { \mathrm { e q , s w } } \mathrm { . }$ (a) inductor current, and (b) load current. (a) iL (A). (b) $i _ { \mathrm { l o a d } } \left( \mathrm { A } \right)$

2) The second test evaluates the influence of different time steps (0.5 s, 2 s, 10 $\mu \mathrm { s } ,$ , and 50 s), as shown in μ μ μ μFig. 12. It shows that the deviation between BAM-ADC and $\mathrm { R _ { O N } / R _ { O F F } }$ increases with step size, validating that the BAM-ADC error is positively correlated with h, as theoretically derived in (31).

These two additional tests not only demonstrate the effectiveness of the recommended $G _ { \mathrm { e q , s w } }$ , but also confirm the rationality of the error analysis.

## B. AC-DC Converter: Three-Phase Full-Bridge Rectifier

In this subsection, a three-phase full-bridge rectifier is modeled as shown in Fig. 13, allowing investigation of the influence of inter-BAM coupling and evaluation of the BAM-ADC model’s generality. The parameters are provided in Appendix A. The duration is 0.8 s with a 10 s time step. The converter is μblocked before 0.1 s. A single-phase-to-ground fault occurs on phase A at 0.31 s and clears at 0.33 s. The control signal of switch unit $S _ { 1 }$ is lost at 0.4 s and restored at 0.6 s. The results are provided in Figs. 14, and 15.

As observed in Fig. 14, the BAM-ADC model maintains high accuracy identical to that of the $\mathrm { R _ { O N } / R _ { O F F } }$ model, even under relatively large time steps like $1 0 \mu \mathrm { s }$ and across various operating μstates, including normal operation, block mode, ground fault, and signal loss fault. By contrast, the L/C-ADC model presents severe distortions and becomes unreliable under such conditions. Besides, although G-ADC and CI-ADC show relatively high accuracy under normal operation and ground fault, they fail to simulate accurate results during block mode and signal loss fault, limiting their reliability.

![](images/4561b27636fe35b67719251c869379956db8cb95a2f4b7d1e7926d6407d70e78.jpg)  
Fig. 12. Waveform comparison of the $\mathrm { R o N } / \mathrm { R } _ { \mathrm { O F F } }$ and BAM-ADC models under different time step h: (a) Inductor current, and (b) load current. $\left( \mathrm { a } \right) i _ { L } \left( \mathrm { A } \right)$ (b) iload (A).

![](images/060861323ba9bd78f831a133e2ab586c5041c723fafecf72a7974e27af6550fe.jpg)  
Fig. 13. Three-phase full-bridge rectifier system.

Fig. 15 further confirms that BAM-ADC accurately reflects the switch voltage and midpoint voltage of BAM, while consistently maintaining low spurious harmonic spikes and virtual power loss. However, G-ADC and CI-ADC produce substantial deviations in non-complementary switching states, while L/C-ADC presents persistent high errors. These results further verify the accuracy and generality of the BAM-ADC model across diverse operating scenarios.

![](images/a8c3ffa3a89fc2bdd9f0dd24141a4bbe09946b5b9babdd5d19bc65fec858532c.jpg)  
Fig. 14. Waveforms of (a) consumed power of $R _ { \mathrm { l o a d } }$ , and (b) A-phase current. (a) $P _ { \mathrm { l o a d } }$ (kW). (b) ia (A).

## C. Two-Stage Grid-Connected PV Generation System

To further validate the generality of the BAM-ADC model, a two-stage grid-connected photovoltaic (PV) generation system is simulated as shown in Fig. 16, which includes a PV array, a boost chopper, a VSC, and their respective control systems. Thus, this test enables assessment of the model under closedloop and grid-connected conditions, as well as the impact of interconnected converters on the BAM-ADC model’s accuracy. The simulation runs for 1.0 s with a time step of $2 ~ \mu \mathrm { s }$ . The parameters are detailed in Appendix B. A ground fault occurs on phase A at 0.4 s and clears at 0.42 s. The irradiance drops to 800 $\mathrm { W } / \mathrm { m } ^ { 2 }$ at 0.8 s and recovers to 1000 $\mathrm { W } / \mathrm { m } ^ { 2 }$ at 0.85 s. The results are presented in Figs. 17 and 18.

Figs. 17 and 18 show that BAM-ADC produces waveforms consistent with the $\mathrm { R _ { O N } / R _ { O F F } }$ model throughout start-up, ground fault, and irradiance drop scenarios. In contrast, the L/C-ADC model introduces significant deviations. G-ADC and CI-ADC models exhibit substantial errors during 0-0.2 s due to the presence of non-complementary states in the boost chopper during start-up, while maintaining relatively high accuracy during normal operation. Furthermore, Fig. 18 highlights the presence of higher harmonic spikes and larger virtual losses in other ADC models, reaffirming the high fidelity and broad applicability of BAM-ADC.

## D. Accuracy and Efficiency Analysis

Table I lists the maximum relative errors of each ADC model with respect to the $\mathrm { R _ { O N } / R _ { O F F } }$ reference. For non-state quantities such as switch voltage/current, as state misjudgment leads to significant deviations, only the magnitudes of the spurious spikes are compared in this table. The incorrect state identification rates are presented in Table II.

![](images/7d8b4befd63330c1239083613c16ae87259b5950a15b08605739c26f592f0c6e.jpg)

![](images/8544c8f7199ebd47025499787b04c82f6552cc635a88a0b1240bc1f7d4214fa3.jpg)  
TABLE I  
ACCURACY COMPARISON OF FIXED-ADMITTANCE ADC MODELS (% )  
Fig. 15. Waveforms of (a) voltage of switch unit $S _ { 1 } .$ , (b) voltage of midpoint on BAM1, and (c) virtual power loss of switch unit $S _ { 1 \cdot } \left( \mathrm { a } \right) u _ { S 1 } \left( \mathrm { V } \right) . \left( \mathrm { b } \right) u _ { \mathrm { a x } } \left( \mathrm { V } \right)$ (c) PlossS1 (kW).  
Fig. 17. Waveforms of (a) output active power to grid, (b) phase A current, and (c) PV array voltage. (a) $P _ { \mathrm { g r i d } }$ (kW). (b) ia (A). (c) upv (V).

![](images/3c4ef901d86a5d7622d73f12fe88c52a5875f7be253edbbf1b876201d6712ee7.jpg)  
Fig. 16. Two-stage grid-connected PV generation system.

As shown in Table I, the BAM-ADC model exhibits significantly lower maximum virtual power loss and harmonic spikes compared to other ADC models. It also maintains high accuracy across other quantities. In contrast, the L/C-ADC model exhibits substantial errors and virtual power loss, severely undermining its simulation accuracy and highlighting its limitations in largestep or high-precision EMT simulations. Table I further reveals that the G-ADC and CI-ADC models consistently underperform in accuracy relative to BAM-ADC, with significantly larger deviations observed during non-complementary states and certain fault scenarios. The results further validate the high precision of BAM-ADC.

<table><tr><td rowspan="2">Case</td><td rowspan="2">Variables</td><td colspan="4">ADCModel</td></tr><tr><td>BAM-ADC</td><td>L/C-ADC</td><td>CI-ADC</td><td>G-ADC</td></tr><tr><td rowspan="4">A</td><td> $i _ { L }$ </td><td>1.865</td><td>33.441</td><td>84.208</td><td>84.345</td></tr><tr><td> $i _ { \mathrm { l o a d } }$ </td><td>1.128</td><td>26.626</td><td>58.634</td><td>58.661</td></tr><tr><td> $u _ { V }$ </td><td>1.391</td><td>100.118</td><td>1.457</td><td>30.006</td></tr><tr><td> $\underline { { P } } _ { \mathrm { l o s s } }$ </td><td>3.208</td><td>416.001</td><td>3.226</td><td>65.68</td></tr><tr><td rowspan="4">B</td><td> $P _ { \mathrm { l o a d } }$ </td><td>0.801</td><td>40.718</td><td>42.922</td><td>43.586</td></tr><tr><td> $i _ { \mathrm { a } }$ </td><td>1.210</td><td>53.782</td><td>128.942</td><td>129.046</td></tr><tr><td> $u _ { \mathrm { a x } }$ </td><td>0.755</td><td>54.810</td><td>0.816</td><td>26.276</td></tr><tr><td> $\underline { { P _ { \mathrm { l o s s } } } }$ </td><td>2.813</td><td>111.664</td><td>4.759</td><td>152.941</td></tr><tr><td rowspan="6">C</td><td> $P _ { \mathrm { g r i d } }$ </td><td>1.265</td><td>65.593</td><td>313.546</td><td>314.256</td></tr><tr><td> $u _ { \mathsf { p v } }$ </td><td>1.684</td><td>11.319</td><td>27.821</td><td>27.776</td></tr><tr><td> $i _ { \mathrm { a } }$ </td><td>2.214</td><td>115.652</td><td>346.002</td><td>346.155</td></tr><tr><td> $u _ { \mathrm { S l } }$ </td><td>0.030</td><td>73.815</td><td>0.027</td><td>43.115</td></tr><tr><td> $i _ { \mathrm { S 1 } }$ </td><td>0.094</td><td>543.064</td><td>0.297</td><td>298.629</td></tr><tr><td> $\boldsymbol { P _ { \mathrm { l o s s } } }$ </td><td>0.233</td><td>1388.490</td><td>0.525</td><td>827.422</td></tr></table>

Table II indicates that the BAM-ADC model achieves a high state identification accuracy, closely matching the RON/ROFF reference, while the L/C-ADC model suffers from a higher misjudgment rate. Moreover, the G-ADC and CI-ADC models fail to account for non-complementary states, resulting in drastically reduced correct identification rates under such scenarios. These underscore the limitations of existing ADC models and further demonstrate the applicability of the BAM-ADC model in diverse operating conditions To evaluate efficiency, 100 one-second simulations are conducted on the C++-based platform, and the average elapsed computation times are summarized in Table III. It indicates that the BAM-ADC, G-ADC, and CI-ADC models share comparable execution times with the L/C-ADC model, and are all significantly faster than the RON/ROFF model. This confirms that, compared to L/C-ADC, BAM-ADC does not introduce substantial computational overhead and is well-suited for real-time simulation. In contrast, the high time cost of the $\mathrm { R _ { O N } / R _ { O F F } }$ model stems from complex switching operations and corresponding additional computing overheads.

![](images/5a7838a16090c4debe3e0b2960c42cbd3f1aa964179d6a38d4148653d16778fe.jpg)  
Fig. 18. Waveforms of (a) voltage, (b) current, and (c) virtual power loss of S1. (a) uS1 (V). (b) iS1 (A). (c) $P _ { \mathrm { l o s s } , S 1 }$ (kW).

TABLE II  
INCORRECT STATE RATES OF ADC MODELS COMPARED TO RON/ROFF (% )
<table><tr><td rowspan="2">Case</td><td colspan="4">ADCModel</td></tr><tr><td>BAM-ADC</td><td>L/C-ADC</td><td>CI-ADC</td><td>G-ADC</td></tr><tr><td>A</td><td>0.048</td><td>4.124</td><td>21.230</td><td>21.232</td></tr><tr><td>B</td><td>0.330</td><td>2.725</td><td>10.735</td><td>10.755</td></tr><tr><td>C</td><td>0.269</td><td>13.277</td><td>5.761</td><td>5.783</td></tr></table>

TABLE III

AVERAGE EXECUTION TIME FOR ONE-SECOND SIMULATION (MS)
<table><tr><td rowspan="2">Model</td><td colspan="3">h =2μs</td><td colspan="3">h =10μs</td></tr><tr><td>A</td><td>B</td><td>C</td><td>A</td><td>B</td><td>C</td></tr><tr><td>BAM-ADC</td><td>55.2</td><td>233.9</td><td>482.2</td><td>12.9</td><td>52.9</td><td>102.6</td></tr><tr><td>L/C-ADC</td><td>54.1</td><td>229.3</td><td>453.1</td><td>12.8</td><td>50.3</td><td>99.9</td></tr><tr><td>CI-ADC</td><td>56.8</td><td>244.1</td><td>491.5</td><td>13</td><td>55.2</td><td>111.3</td></tr><tr><td>G-ADC</td><td>58.6</td><td>247.9</td><td>500.2</td><td>13.3</td><td>56.3</td><td>112.8</td></tr><tr><td>RoN/RoFF</td><td>470.3</td><td>1156.4</td><td>1712.6</td><td>97.6</td><td>998.3</td><td>1136.3</td></tr></table>

![](images/87b670f92dddc2434f062b327ba2f0d319053a856187efc88f0598b65c45322e.jpg)  
Fig. 19. Experiment platform: (a) topology of the three-phase full-bridge inverter, (b) physical experiment setup, and (c) HIL simulation architecture.

In summary, these cases collectively validate the BAM-ADC model’s high accuracy and computational efficiency.

## V. EXPERIMENTAL VERIFICATION

Section IV has demonstrated the outstanding accuracy and efficiency advantages of BAM-ADC. However, two key issues must still be addressed to validate its practical application in EMT simulation [22]. First, regarding accuracy, it is essential to confirm whether the simulation results align with real-world converter behavior. Second, in terms of efficiency, it is necessary to assess the model’s performance in a real-time simulation environment. To this end, a physical experiment and a hardwarein-the-loop (HIL) test of a three-phase full-bridge inverter are conducted as depicted in Fig. 19.

The physical test platform, shown in Fig. 19(a) and (b), is constructed to validate the fidelity of the BAM-ADC model. A constant voltage and constant frequency (CVCF) control strategy is employed, and relevant parameters are provided in Appendix B. The deadtime of the controller is set to 1 s.

μTo evaluate real-time performance, an HIL simulation is implemented using an OP4610XG emulator with an AMD Ryzen 3.8 GHz CPU and a Xilinx Kintex-7 410T FPGA, together with an imperix B-Box RCP 3.0 controller and two host computers, as shown in Fig. 19(c). The CPU transfers observation data to the controller; the controller processes the data and sends the control signals to the FPGA module; the FPGA carries out the whole electrical system modeling and calculation; the host computers provide the development environment and operation interface of RT-LAB and ACG SDK. The time step of the HIL test is 1 s with 1 s deadtime.

![](images/b8265eb07b876b933d34b28bdc0b125b9d88cf0a40a8584d43354ad52e23657d.jpg)  
Fig. 20. Waveforms of gate signal $S _ { 1 } ,$ and phase voltages $u _ { a } ,$ ub: (a)(b) experiment, (c)(d) BAM-ADC simulation, and (e)(f) L/C-ADC simulation.

μIn this section, the BAM-ADC model uses the recommended equivalent admittance $G _ { \mathrm { e q , s w } }$ derived in (30), while the L/C-ADC model is tested using both the same admittance and the value recommended in [32] for thorough comparison. Since the output phase voltage/current waveforms are nearly identical in both L/C-ADC cases, only the internal variables of the switch unit are presented to avoid redundancy.

$$
\left\{ \begin{array} { l l } { { \mathrm { B A M - A D C } : G _ { \mathrm { e q , s w } } = { \frac { \sqrt { 2 } - 1 } { \sqrt { 2 } } } \sqrt { \frac { C } { L } } \approx 0 . 1 5 3 \mathrm { S } } } \\ { \mathrm { L } / \mathrm { C } - \mathrm { A D C } : G _ { \mathrm { e q , s w } } = { \frac { I _ { R M S } ^ { A C } } { V ^ { D C } } } \approx { \frac { 2 / \sqrt { 2 } \cdot \sqrt { 3 } } { 1 0 0 } } \approx 0 . 0 2 5 \mathrm { S } }  \end{array} \right.\tag{42}
$$

Fig. 20 presents the experimental and simulated results for phase voltages $u _ { \mathrm { a } } , u _ { \mathrm { b } }$ and gate signal of $S _ { 1 }$ . In the experiment and simulations of BAM-ADC and L/C-ADC, the phase voltages exhibit a consistent amplitude of approximately 39 V and remain phase-aligned. In addition, as the duty cycle of $S _ { 1 }$ increases, $u _ { \mathrm { a } }$ gradually rises from −39 V to 39 V, confirming that both models present the expected external behavior.

To evaluate dynamic performance, the reference voltage in the CVCF control is changed from 40 V to 30 V. The waveforms are shown in Figs. 21 and 22. Fig. 21 shows that both BAM-ADC and L/C-ADC track the step change. However, the L/C-ADC waveforms exhibit relatively higher noise levels, indicating its elevated harmonic content. This further highlights the accuracy advantage of BAM-ADC.

Moreover, Fig. 22 compares the voltage, current, and virtual power loss of switch unit $S _ { 1 }$ . The BAM-ADC model maintains stable switching behavior with minimal voltage/current spikes and negligible power loss. In contrast, the L/C-ADC model consistently exhibits pronounced spikes and switching power loss during state transitions, regardless of the value of $G _ { \mathrm { e q , s w } } .$

![](images/8eae69a25b50d9783488fff86a6f8fbf753f2761f819476603b529fe716b19d5.jpg)  
Fig. 21. Waveforms under reference voltage step from 40 V to 30 V: A phase voltage and current of (a)(b) BAM-ADC, and (c)(d) L/C-ADC.

These results further confirm that BAM-ADC more closely resembles the ideal behavior of switches, while L/C-ADC introduces substantial inaccuracies.

Through experimental testing, both the BAM-ADC and L/C-ADC models successfully complete HIL simulations without time overruns, demonstrating the feasibility of BAM-ADC for real-time applications. In addition, although the output AC waveforms appear similar, the BAM-ADC model generates significantly lower harmonic spikes and virtual power loss compared to the L/C-ADC model. These results underscore the superior accuracy and efficiency of the BAM-ADC model in real-time simulation scenarios.

## VI. CONCLUSION

To address the dual challenges of achieving high accuracy and efficiency in EMT simulations, this paper proposes a BAM-ADC model. The model enhances simulation efficiency through a parameterized BAM structure with fixed equivalent admittance, while high accuracy is ensured via optimal parameter settings and the application of the CRI method. Simulation and experimental results confirm that BAM-ADC exhibits high accuracy with low computational overhead. Compared to existing ADC models, it consistently achieves lower simulation errors without sacrificing efficiency, making it well-suited for EMT simulations, especially in real-time scenarios where both precision and speed are essential.

Nevertheless, the BAM-ADC model has certain limitations. Specifically, it is currently unable to independently simulate non-complementary conduction scenarios. In such cases, it must be used in conjunction with the L/C-ADC model, which may compromise optimal simulation performance. Addressing this limitation presents a valuable direction for future research. In addition, there remains room for improvement in the fast state determination strategy for converters based on the ADC models. The development of high-accuracy and universal state prediction methods for various converter topologies under real-time conditions remains a highly promising and impactful research avenue.

![](images/59ed3337f8d2e7d214f1afee64f86b776cc69e32b60841a049893dbf3981ea9f.jpg)  
Fig. 22. Waveforms of gate signal $S _ { 1 }$ and voltage, current, and virtual power loss of switch unit $S _ { 1 }$ under reference voltage step from 40 V to 30 V: (a)–(d) BAM-ADC, (e)–(h) L/C-ADC using recommended $G _ { \mathrm { e q , s w } }$ in [32], and (i)–(l) L/C-ADC using same $G _ { \mathrm { e q , s w } }$ as BAM-ADC.

## APPENDIX

## A. Parameters of the Simulations

## 1) Boost Chopper:

<table><tr><td>Symbol</td><td>Parameter</td><td>Value</td></tr><tr><td> $\overline { { V _ { \mathrm { d c l } } } }$ </td><td>DC1 side voltage source</td><td>40V</td></tr><tr><td> $r _ { \mathrm { d c l } }$ </td><td>Internal resistance of DC source</td><td>0.001Ω</td></tr><tr><td> $R _ { \mathrm { d c } 2 }$ </td><td>DC2 side load resistance</td><td>2Ω</td></tr><tr><td> $C _ { \mathrm { d c l } } / C _ { \mathrm { d c } 2 }$ </td><td>DC1/DC2 side capacitance</td><td>320μF/320μF</td></tr><tr><td> $L$ </td><td>Internal inductance</td><td>80μH</td></tr><tr><td> $D$ </td><td>Duty cycle</td><td>0.6</td></tr><tr><td> $f _ { \mathrm { c } }$ </td><td>Carrier frequency</td><td>10kHz</td></tr></table>

## 2) Three-Phase Full-Bridge Rectifier:

<table><tr><td>Symbol</td><td>Parameter</td><td>Value</td></tr><tr><td> $V _ { \mathrm { a c } }$ </td><td>AC source line voltage RMS</td><td>381V</td></tr><tr><td> $f _ { \mathrm { a c } }$ </td><td>AC source frequency</td><td>50Hz</td></tr><tr><td> $\theta$ </td><td>AC source initial phase angle</td><td>0</td></tr><tr><td> $R _ { \mathrm { d c } }$ </td><td>DC side load resistance</td><td>10Ω</td></tr><tr><td> $L _ { s } / R _ { s }$ </td><td>AC side equivalent inductance/resistance</td><td>0.8mH/0.1Ω</td></tr><tr><td> $C _ { \mathrm { d c } }$ </td><td>DC side capacitance</td><td>2mF</td></tr><tr><td> $M$ </td><td>Modulation ratio</td><td>0.35</td></tr><tr><td> $\varphi$ </td><td>Modulating wave initial phase angle</td><td>-π/3</td></tr><tr><td> $f _ { \mathrm { m } } / f _ { \mathrm { c } }$ </td><td>Modulating wave/carrier frequency</td><td>50Hz/5kHz</td></tr></table>

## 3) Two-Stage Grid-Connected PV System:

## a) PV array:

<table><tr><td>Symbol</td><td>Parameter</td><td>Value</td></tr><tr><td> $C _ { T }$ </td><td>Temperature coefficient</td><td>0.0017A/K</td></tr><tr><td> $E _ { g }$ </td><td>Forbidden bandwidth</td><td>1.237eV</td></tr><tr><td> $R _ { s r } / R _ { s h }$ </td><td>Series/shunt resistance</td><td>0.01Ω/1×10Ω</td></tr><tr><td> $I _ { p h r e f }$ </td><td>Standard photogenerated current</td><td>3.35A</td></tr><tr><td> $I _ { s r e f }$ </td><td>Diode saturation current</td><td>0.545×10A</td></tr><tr><td> $N _ { m s } / N _ { m p }$ </td><td>Number of modules in series/parallel per array</td><td>20/45</td></tr><tr><td> $N _ { c s } / N _ { c p }$ </td><td>Number of cells in series/parallel per module</td><td>36/1</td></tr><tr><td> $A$ </td><td>Diode characteristic fitting factor</td><td>1.5</td></tr><tr><td> $S _ { r e f }$ </td><td>Standard irradiance</td><td>1000W/m²</td></tr><tr><td> $T _ { r e f }$ </td><td>Standard temperature</td><td>298K</td></tr></table>

## Controller: MPPT (perturbation and observation method).

## b) Boost chopper:

<table><tr><td>Symbol</td><td>Parameter</td><td>Value</td></tr><tr><td> $C _ { p \nu }$ </td><td>PV side filter capacitance</td><td>5mF</td></tr><tr><td> $L$ </td><td>Internal inductance</td><td>2mH</td></tr></table>

## Controller: Dual closed-loop control.

<table><tr><td>Symbol</td><td>Parameter</td><td>Value</td></tr><tr><td> $k _ { p } \_ u / k _ { i } \_ u$ </td><td>Voltage outer loop scaling/integration factor</td><td>0.4/10</td></tr><tr><td>kp_i/ki_i</td><td>Current inner loop scaling/integration factor</td><td>0.4/100</td></tr><tr><td> $f _ { C }$ </td><td>Carrier frequency</td><td>5kHz</td></tr></table>

## c) Three-phase bridge converter:

<table><tr><td>Symbol</td><td>Parameter</td><td>Value</td></tr><tr><td> $V _ { a c }$ </td><td>AC source line voltage RMS</td><td>400V</td></tr><tr><td> $f _ { a c }$ </td><td>AC source frequency</td><td>50Hz</td></tr><tr><td> $C _ { d c }$ </td><td>DC side capacitance</td><td>5mF</td></tr><tr><td> $L _ { s } / R _ { s }$ </td><td>Internal equivalent stray inductance/resistance</td><td>5mH/0.1Ω</td></tr></table>

## Controller: Dual closed-loop control.

<table><tr><td>Symbol</td><td>Parameter</td><td>Value</td></tr><tr><td> $k _ { p \_ P L L } / k _ { i \_ P L L }$ </td><td>Proportional/integral gain of phase-locked loop</td><td>1/0.1</td></tr><tr><td> $k _ { p } \_ P Q / k _ { i } P Q$ </td><td>Proportional/integral gain of PQ outer loop</td><td>50/2</td></tr><tr><td>kp_idg/k_idq</td><td>Proportional/integral gain current inner loop</td><td>5/10</td></tr><tr><td> $f _ { C }$ </td><td>Carrier frequency</td><td>5kHz</td></tr></table>

## B. Parameters of the Experiment

<table><tr><td>Symbol</td><td>Parameter</td><td>Value</td></tr><tr><td> $E _ { \mathrm { d c } }$ </td><td>DC voltage source</td><td>100V</td></tr><tr><td> $r _ { \mathrm { d c } }$ </td><td>Internal resistance of DC source</td><td>0.001Ω</td></tr><tr><td> $C _ { \mathrm { d c } }$ </td><td>DC side capacitance</td><td>1.36mF</td></tr><tr><td> $L _ { \mathrm { s } }$ </td><td>Internal equivalent stray inductance</td><td>5mH</td></tr><tr><td> $R _ { \mathrm { l o a d } }$ </td><td>AC side load resistance</td><td>20Ω</td></tr><tr><td> $L _ { \mathrm { f } } / C _ { \mathrm { f } }$ </td><td>AC side filter inductance/capacitance</td><td>0.1mH/0.01mF</td></tr><tr><td> $k _ { \mathrm { p } } \_ u / k _ { \mathrm { i } } \_ u$ </td><td>Voltage outer loop scaling/integration factor</td><td>1/0.1</td></tr><tr><td> $k _ { \mathrm { p } } \_ i / k _ { \mathrm { i } } \_ i$ </td><td>Current inner loop scaling/integration factor</td><td>1/2</td></tr><tr><td> $f _ { \mathrm { C } }$ </td><td>Carrier frequency</td><td>5kHz</td></tr></table>

## REFERENCES

[1] N. Hatziargyriou et al., “Definition and classification of power system stability – revisited & extended,” IEEE Trans. Power Syst., vol. 36, no. 4, pp. 3271–3281, Jul. 2021.

[2] P. Kundur et al., “Definition and classification of power system stability IEEE/CIGRE joint task force on stability terms and definitions,” IEEE Trans. Power Syst., vol. 19, no. 3, pp. 1387–1401, Aug. 2004.

[3] X. Zhou, L. Guo, X. Li, Z. Wang, J. Zhu, and C. Wang, “Transient stability analysis of renewable power generations via VSC-HVDC,” IEEE Trans. Ind. Electron., vol. 72, no. 5, pp. 4889–4899, May 2025.

[4] W. Xu et al., “Modeling of inverter-based resources for power system harmonics studies,” IEEE Trans. Power Del., vol. 40, no. 1, pp. 166–177, Feb. 2025.

[5] Y. Liu, Y. Gao, and J. Liang, “Simulation of switched-mode power conversion circuits with extended impedance method,” IEEE Trans. Circuits Syst. I: Reg. Papers, vol. 69, no. 9, pp. 3851–3860, Sep. 2022.

[6] B. K. Johnson, “Electromagnetic transient simulation: Moving to the mainstream [technology leader],” IEEE Electrific. Mag., vol. 11, no. 4, pp. 6–7, Dec. 2023.

[7] X. Fu, W. Wu, P. Li, J. Mahseredjian, J. Wu, and C. Wang, “Splitting statespace method for converter-integrated power systems EMT simulations,” IEEE Trans. Power Del., vol. 40, no. 1, pp. 584–595, Feb. 2025.

[8] J. D. Lara, R. Henriquez-Auba, D. Ramasubramanian, S. Dhople, D. S. Callaway, and S. Sanders, “Revisiting power systems time-domain simulation methods and models,” IEEE Trans. Power Syst., vol. 39, no. 2, pp. 2421–2437, Mar. 2024.

[9] B. Shi, Y. Chen, K. Chen, J. Ju, Z. Yu, and Z. Zhao, “Event-driven approach with time-scale hierarchical automaton for switching transient simulation of SiC-based high-frequency converter,” IEEE Trans. Circuits Syst. I: Reg. Papers, vol. 68, no. 11, pp. 4746–4759, Nov. 2021.

[10] X. Ma and X. -P. Zhang, “Basics of electromagnetic transients: Underlying mathematics,” IEEE Electrific. Mag., vol. 11, no. 4, pp. 8–19, Dec. 2023.

[11] J. Xu et al., “High-speed electromagnetic transient (EMT) equivalent modelling of power electronic transformers,” IEEE Trans. Power Del., vol. 36, no. 2, pp. 975–986, Apr. 2021.

[12] P. Kuffel, K. Kent, and G. Irwin, “The implementation and effectiveness of linear interpolation within digital simulation,” Int. J. Elect. Power Energy Syst., vol. 19, no. 4, pp. 221–227, May 1997.

[13] H. W. Dommel, “Digital computer solution of electromagnetic transients in single-and multiphase networks,” IEEE Trans. Power App. Syst., vol. PAS-88, no. 4, pp. 388–399, Apr. 1969.

[14] S. Y. R. Hui and C. Christopoulos, “A discrete approach to the modeling of power electronic switching networks,” IEEE Trans. Power Electron., vol. 5, no. 4, pp. 398–403, Oct. 1990.

[15] P. Pejovic and D. Maksimovic, “A method for fast time-domain simulation of networks with switches,” IEEE Trans. Power Electron., vol. 9, no. 4, pp. 449–456, Jul. 1994.

[16] Z. Li et al., “Unified real-time simulation method for DC/DC conversion systems consisting of cascaded dual-port submodules,” IEEE Trans. Ind. Electron., vol. 70, no. 11, pp. 11368–11378, Nov. 2023.

[17] C. Gao et al., “Portal analysis approach used for the efficient electromagnetic transient (EMT) simulation of power electronic systems,” IEEE Trans. Power Del., vol. 38, no. 6, pp. 4213–4225, Dec. 2023.

[18] F. Zhang, Z. Zhou, W. Gu, and D. Jia, “General modeling method of voltage source converter for electromagnetic transient simulation based on state space equation and switching function,” Automat. Electric Power Syst., vol. 47, no. 23, pp. 84–91, 2023.

[19] M. Xu, W. Gu, Y. Cao, S. Chen, F. Zhang, and W. Liu, “Low-dimensional equivalent models and multithreading-based parallel EMT simulation method for multi-converter systems,” IEEE Trans. Energy Convers., vol. 40, no. 1, pp. 437–452, Mar. 2025.

[20] RTDS Technologies, “Universal converter model: Industry leading real-time power electronic simulation,” RTDS Knowledge Center, 2025. Accessed: Sep. 25, 2024. [Online]. Available: https://knowledge.rtds. com/hc/en-us/articles/4408515011223-Universal-Converter-Model-Industry-Leading-Real-Time-Power-Electronic-Simulation

[21] OPAL-RT, “eHS single switches capability - common internal documentation - OPAL-RT,” OPAL-RT Wiki, 2024. Accessed: May 17, 2025. [Online]. Available: https://opal-rt.atlassian.net/wiki/spaces/PINT/pages/ 1027866696/eHS+Single+Switches+Capability

[22] J. Xu, K. Wang, P. Wu, and G. Li, “FPGA-based sub-microsecond-level real-time simulation for microgrids with a network-decoupled algorithm,” IEEE Trans. Power Del., vol. 35, no. 2, pp. 987–998, Apr. 2020.

[23] RTDS Technologies, “The Universal Converter Model for enhanced realtime power electronics simulation,” RTDS Blog, 2021. Accessed: May 29, 2024. [Online]. Available: https://www.rtds.com/BlogPosts/UCM

[24] T. Maguire, S. Elimban, E. Tara, and Y. Zhang, “Predicting switch ON/OFF statuses in real time electromagnetic transients simulations with voltage source converters,” in Proc. 2nd IEEE Conf. Energy Internet Energy System Integration, Oct. 2018, pp. 1–7.

[25] C. Wang, Q. Wang, H. Weng, and X. Pan, “A modified algorithm for the L/C-based switch model of power converters in real-time simulation based on FPGA,” IEEE Trans. Ind. Appl., vol. 60, no. 5, pp. 7030–7037, Sep./Oct. 2024.

[26] Y. Hou, C. Liu, L. Zheng, S. Xin, and H. Cai, “Fixed-admittance modeling method of voltage source converter based on compensation of negative resistance,” Proc. Chin. Soc. Electronical Eng., vol. 42, no. 19, pp. 6985–6994, 2022.

[27] F. Zhang, W. Gu, Y. Zhang, L. Wang, and W. Li, “General linearized model of voltage source converter with fixed nodal admittance matrix,” IEEE Trans. Power Electron., vol. 39, no. 10, pp. 12143–12148, Oct. 2024.

[28] K. Wang, J. Xu, G. Li, N. Tai, A. Tong, and J. Hou, “A generalized associated discrete circuit model of power converters in real-time simulation,” IEEE Trans. Power Electron., vol. 34, no. 3, pp. 2220–2233, Mar. 2019.

[29] Y. Cao, W. Gu, W. Liu, G. Cao, G. Lou, and D. Zou, “A parameterized fixed-admittance model of converters based on cross initialization,” Proc. Chin. Soc. Electronical Eng., vol. 41, no. 10, pp. 3518–3527, 2021.

[30] H. W. Dommel, “Electromagnetic transients in single- and multiphase networks,” IEEE Trans. Power App. Syst., vol. PAS-88, no. 4, pp. 388–399, 1969.

[31] P. Wu, J. Xu, K. Wang, Z. Li, and G. Li, “A fractional time-step simulation method suitable for the associated discrete circuit model of power electronic system,” IET Renewable Power Gener., vol. 17, no. 1, pp. 176–185, 2023.

[32] OPAL-RT, “How to tune discrete-time switch conductance - eHS FPGA-based Power Electronics Toolbox - OPAL-RT,” OPAL-RT Wiki, 2023. Accessed: May 22, 2025. [Online]. Available: https://opalrt.atlassian.net/wiki/spaces/PFPET/pages/310870375/How+to+tune+ discrete-time+switch+conductance

![](images/be28e0ab1c203f7a91ef04aa5c2e65f83108d0d23ef55ee6f68c926c2fbb1bbd.jpg)

Yang Cao (Graduate Student Member, IEEE) received the B.S. and M.S. degrees in electrical engineering in 2018 and 2021, respectively, from Southeast University, Nanjing, China, where he is currently working toward the Ph.D. degree in electrical engineering.

His research interests include modeling, control, and real-time simulation of power electronic systems.

![](images/9cb536ea4379635926c45032cf9d276b762f351c8b5127dd5877f3767e30891e.jpg)

Xiaodong Yuan received the B.S. and M.S. degrees in electrical engineering from Southeast University, Nanjing, China, in 2001 and 2005, respectively.

His research focuses on power system simulation and analysis.

![](images/19da05956f7ed570ff25b7d1cfe99f9fc6e32d827f59eaa18392c948e0872e40.jpg)

Huachun Han received the B.S. degree in electrical engineering from Shandong University, Jinan, China, in 2009 and the Ph.D. degree in power electronics and electric drives from the University of Chinese Academy of Sciences, Beijing, China, in 2016.

Her research focuses on power system simulation and modeling.

![](images/10071c43deb02d3cb89c167c652696956f5bd3abeec77bb90ef8f7f696997e52.jpg)

Mingwang Xu (Graduate Student Member, IEEE) received the B.S. and M.S. degrees in power engineering from North China Electric Power University, Beijing, China, in 2019 and 2022, respectively. He is currently working toward the Ph.D. degree in electrical engineering from Southeast University, Nanjing, China.

His research interests include modeling and realtime simulation of power electronic systems.

![](images/bc270daf9f6e7000c81d143072d841ff6c6b804da1b89f4dc606e9249403c252.jpg)

He is currently a Professor with the School of Electrical Engineering, Southeast University. He is also the Director of the Institute of Distributed Generations and Active Distribution Networks. His research

Wei Gu (Senior Member, IEEE) received the B.S. and Ph.D. degrees in electrical engineering from Southeast University, Nanjing, China, in 2001 and 2006, respectively. From 2009 to 2010, he was a Visiting Scholar with the Department of Electrical Engineering, Arizona State University, Tempe, AZ, USA.

His research interests include HVDC converters, high power electronics, and real-time simulation.

Fei Zhang (Member, IEEE) received the B.S. and M.S. degrees in electrical engineering from Tsinghua University, Beijing, China, in 2009 and 2012, respectively, and the Ph.D. degree in electrical engineering from McGill University, Montreal, Canada, in 2018. From 2018 to 2020, he was a Specialist in modeling and electrical simulation with Opal-RT Technologies, Montreal, QC, Canada. Since 2020, he has been an Associate Professor with the School of Electrical Engineering, Southeast University, Nanjing, China.

![](images/e5b848602d36fbb75d9c9a21bc15a68f42a69da5ee81597c78279477dd868457.jpg)

interests include distributed generations and microgrids, and integrated energy systems.