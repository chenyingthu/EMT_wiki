# A Heterogeneous Multiscale Method for Efficient Simulation of Power Systems with Inverter-Based Resources

Kaiyang Huang, Student Member, IEEE, Min Xiong, Member, IEEE, Yang Liu, Member, IEEE, Kai Sun, Fellow, IEEE.

Abstract—As inverter-based resources (IBRs) penetrate power systems, the dynamics become more complex, exhibiting multiple timescales, including electromagnetic transient (EMT) dynamics of power electronic controllers and electromechanical dynamics of synchronous generators. Consequently, the power system model becomes highly stiff, posing a challenge for efficient simulation using existing methods that focus on dynamics within a single timescale. This paper proposes a Heterogeneous Multiscale Method for highly efficient multi-timescale simulation of a power system represented by its EMT model. The new method alternates between the microscopic EMT model of the system and an automatically reduced macroscopic model, varying the step size accordingly to achieve significant acceleration while maintaining accuracy in both fast and slow dynamics of interests. It also incorporates a semi-analytical solution method to enable a more adaptive variable-step mechanism. The new simulation method is illustrated using a two-area system and is then tested on a detailed EMT model of the IEEE 39-bus system.

Index Terms—Heterogeneous Multiscale Method, differential transformation, variable-step solver, electromagnetic transient simulation, time-domain simulation, inverter-based resource.

# I. INTRODUCTION

NVERTER-based resources (IBRs), including renewables I and energy storage systems, are rapidly increasing their presence in power grids worldwide for low-carbon, clean electricity generation. This trend is challenging the traditional dominance of conventional power plants. However, as IBRs become more prevalent in power grids, the analysis and control of power grid dynamics become more complex due to their increased timescales, as well as the high dimensionality and nonlinearity of power grid models. During contingencies, power grid dynamics can span a wide spectrum, from electromagnetic transient (EMT) dynamics with power electronic controllers of IBRs in microseconds to quasi-steady-state grid behaviors in minutes or hours to balance demand and supply against uncertainties of renewables. These dynamics are respectively 1,000-10,000 times faster and slower than transient stability related electromechanical dynamics of synchronous generators [1]. Time-domain simulation is the most important tool for assessing the stability and reliability of a power grid against

This work was supported in part by NSF grant ECCS-2329924 and in part by the ISSE seed grant of the University of Tennessee, Knoxville.(Corresponding author: Kai Sun.)

K. Huang, M. Xiong, Y. Liu and K. Sun are with the Department of Electrical Engineering and Computer Science, University of Tennessee, Knoxville, TN 37996 USA (e-mail: khuang12@vols.utk.edu; mxiong3@vols.utk.edu; yang.powersystems@gmail.com; kaisun@utk.edu).

threats from multiple timescales. However, simulating a realworld power grid with high IBR penetration poses significant challenges to the accuracy and efficiency requirements. If its dynamics of all timescales, such as EMT dynamics and electromechanical oscillations, are taken into account, this will result in a large number of nonlinear ordinary differential equations (ODEs) with a high stiffness ratio. Thus, a step size in microseconds is often required for numerical stability. Additionally, simulating a series of quasi-steady-state behaviors of the grid mixed with inverter controls and inter-area oscillations for an extended period of tens of minutes will result in an extremely slow simulation due to a huge computational burden. Therefore, the best practice of multi-timescale simulations today for power system engineers is still co-simulation, which defines interfaces between EMT models, transient stability models, and quasisteady-state models and co-simulates them iteratively using different simulation tools, with each tool focusing on a portion of the grid in one timescale while reducing the rest [2], [3]. However, it is still an open question how to determine the interface boundaries. Furthermore, the overall convergence, accuracy, and time performance for such co-simulations still pose major technical challenges [4].

Fully detailed simulations such as EMT simulations of an interconnected power grid as a single, nonlinear stiff system to capture its dynamics in all timescales are highly complex tasks [5]. In practice, power system engineers typically focus the modeling and simulating a utility-scale grid on a specific timescale for, e.g., EMT controls, transient stability and quasisteady-state analysis, depending on the purpose of the study. When EMT simulations are required for the integration studies of IBRs, a reduced EMT model can be offline developed, which maintains details only for a specific region of concern, while the rest of the grid is either equivalenced or ignored beyond its boundary [4]–[6]. Simulating of a power system using a manually reduced model pose accuracy concerns. Conventionally, models for longer timescale simulations [7] are generated manually from circuit-based EMT models by developers. The structures and parameters of these models are pending identification and validation using field event data, which, if inaccurate, can lead to incorrect simulation results. For power systems with high-penetration of IBRs, model reduction becomes even more challenging due to two factors. First, a phasor-based postive-sequence model is mainly used in transient stability simulations becomes less accurate, even for some not very fast dynamics, particularly when IBRs induce

high-frequency oscillations in the sub-synchronous frequency range (e.g. 5-60 Hz). These oscillations simulated on a phasorbased model can manifest a significant sacrifice in accuracy [1]. Second, some IBR models provided by the developers are black box models encoded to protect intellectual properties, which are hard to reduce using a traditional model reduction method for mathematical equations.

For efficient and accurate simulations of a power system with IBRs, this paper proposes a multi-timescale simulation approach built upon the Heterogeneous Multiscale Method (HMM) [8], which provides a general framework for designing multiscale algorithms to model and simulate complex, stiff nonlinear dynamical systems. Over the past two decades, the HMM has demonstrated its efficacy in simulating complex systems across various fields of science and engineering, particularly when macroscopic behaviors are of major interest but only microscopic models are available or accurate [8], [9]. Unlike [8], this paper for the first time proposes a novel HMM framework along with its theoretical foundation and a scalable simulation approach for efficient two-timescale simulations of a power system represented in its EMT model. The proposed method enables an automatic, case-specific reduction of a detailed microscopic EMT model into a macroscopic model during the simulation, significantly improving computational efficiency while preserving essential dynamics. The macro-state in the proposed HMM framework is linked to the original microstate via two transformations with a flexible dimension, which is lower than or equal to that of the micro-state. Additionally, the framework introduces a kernel-based convolution method to approximate macro-dynamics from micro-dynamics without requiring an explicitly reduced macro-model, enabling smooth and robust transitions between the micro-process and macroprocess. Furthermore, the paper establishes the theoretical foundation of the method, uncovering relationships between simulation accuracy, computational complexity, and speedup through rigorous theorems. The framework also introduces variable-step algorithms to simulate both micro-state and macro-state efficiently. By leveraging a semi-analytical solution (SAS) method, a new theorem ensures the accurate capture of critical EMT dynamics while dynamically skipping unimportant microscopic dynamics for maximum acceleration in micro-state simulations.

The rest of the paper is organized as follows: Section II briefly introduces a generic HMM framework and then provides a detailed presentation of the proposed HMM approach for efficient two-timescale simulations of power systems represented in EMT models. The section includes the main idea and steps, the overall flowchart of the approach, the power system model considered in this paper, detailed algorithms for the micro-process and macro-process of the approach on the power system model, and a discussion of the main differences from other multi-timescale methods for power system simulations. Section III validates the proposed HMM approach on three test systems represented in their EMT models: a two-area system, the IEEE 39-bus system, and a 390-bus large system, demonstrating the performance and scalability of the proposed approach. Finally, Section IV presents the conclusions.

# II. HETEROGENOUS MULTISCALE METHOD FOR SIMULATING POWER SYSTEMS IN EMT MODELS

A. Introduction of a generic HMM

Consider a stiff ODE system of two or more timescales:

$$
\dot {\mathbf {x}} = \mathbf {f} (\mathbf {x}, t) \Longleftrightarrow \left\{ \begin{array}{l} \dot {\mathbf {x}} ^ {I} = \mathbf {f} ^ {I} \left(\mathbf {x} ^ {I}, \mathbf {x} ^ {I I}, t\right) \\ \epsilon \dot {\mathbf {x}} ^ {I I} = \mathbf {f} ^ {I I} \left(\mathbf {x} ^ {I}, \mathbf {x} ^ {I I}, t\right) \end{array} , \right. \tag {1}
$$

where $\mathbf { x } ( t ) : \mathbb { R } ^ { + } \mapsto \mathbb { R } ^ { n _ { x } }$ is the state variable vector, and $n _ { x }$ is the dimension of the system. The system has dynamics of a fast timescale so that the system can be represented as a two-timescale system with a slow vector $\mathbf { x } ^ { I }$ and a fast vector $\mathbf { x } ^ { I I }$ , which are distinguished by a nonsingular matrix ϵ having eigenvalues close to zero [8]. The stiffness of a dynamical system described in the form of (1) can be defined based on the eigenvalues of the Jacobian of f . Specifically, stiffness is measured as the ratio of the largest eigenvalue to the smallest eigenvalue in terms of absolution value, i.e. $| \lambda _ { \operatorname* { m a x } } / | / \lambda _ { \operatorname* { m i n } } |$ . For a two-timescale system like (1), the eigenvalues separate into two groups due to the time-scale gap defined by ϵ. Hence, the stiffness ratio is approximately $\bar { O } \left( \bar { \| } \epsilon ^ { - 1 } \| \right) \gg \mathrm { \bar { 1 } }$ , in particular $\lVert \epsilon ^ { - 1 } \rVert$ represents the largest absolute value of eigenvalues of $\epsilon ^ { - 1 }$ when 2-norm $( \parallel \cdot \parallel _ { 2 } )$ is applied.

This paper focuses on accelerating power system simulations that include both fast EMT dynamics arising from, e.g., IBRs and the network and relatively slow electromechanical dynamics associated with synchronous generators. These dynamics span time scales from approximately $1 0 ^ { - 6 }$ s to $1 0 ^ { 2 } ~ \mathrm { s } ,$ resulting in a stiffness ratio approaching $1 0 ^ { 8 }$ or higher. To address the stiffness of power system models with IBRs for efficient simulation, two types of fast dynamics need to be considered: 1) dissipative EMT transients characterized by large eigenvalues with negative real parts, which occur immediately after a disturbance like a fault or switching, and 2) sustained oscillatory dynamics characterized by eigenvalues having nearzero real parts, whose examples include instantaneous current and voltage waveforms around the synchronous frequency and subsynchronous oscillations with IBRs. Conventional EMT simulation tools face challenges in efficiently simulating such two-timescale power system models over extended time periods due to their stiffness. These tools often require very small step sizes, in the microsecond range, to maintain numerical stability while simulating continuously until slow electromechanical dynamics, in the range of tens of seconds to minutes, conclude and the system approaches its steady-state condition. In contrast, the proposed HMM approach leverages the time-scale gap defined by ϵ and introduces a macro-process to enable more efficient simulations once dissipative EMT transients subside or oscillatory dynamics reach a steady state. Suppose the existence of an effective macro-model as a reduction of (1) with a vector u : $\mathbb R ^ { + } \mapsto \mathbb R ^ { n _ { u } }$ focusing on slow dynamics when $\lVert \epsilon \rVert$ converges to 0

$$
\dot {\mathbf {u}} = \bar {\mathbf {f}} (\mathbf {u}, t). \tag {2}
$$

To distinguish it from the original system(1), the state of the original system (1) is defined as the micro-state, and directly solving the original micro-model is called the micro-process. An engineering approach for model reduction may assume fast dynamics are all stable and ignore their state variables in (1) by simply letting ϵ = 0. Thus, the second equation in (1)

becomes an algebraic equation, reducing the stiff ODE system to a DAE (differential-algebraic equation) system, which is the conventional form of a power system model for transient stability simulations.

Comparatively, the HMM approach focuses on finding the authentic u and its vector field ¯f that characterize a macromodel as manifested from the real-time response of the stiff system. For instance, in [8], it is assumed that u ≡ x while the effective force ¯f on slow dynamics is obtained by:

$$
\bar {\mathbf {f}} (t) = \lim  _ {\delta \rightarrow 0} \left(\lim  _ {\| \boldsymbol {\epsilon} \| \rightarrow 0} \frac {1}{\delta} \int_ {t} ^ {t + \delta} \mathbf {f} (\mathbf {x}, \tau) d \tau\right). \tag {3}
$$

However, it is often time-consuming to derive ¯f by (3). Instead, the HMM suggests evaluating it “on the $\mathrm { { f l y } ^ { \mathrm { { \prime } } } }$ of simulating (1). Namely, the analytical form of ¯f (t), i.e., an explicit reduction of (1) is neither used nor required. Rather, ¯f (t) is estimated along the simulation as an implicit reduction, and hence it is adaptive to each simulated case regarding averaged macroscopic dynamics with u while important microscopic dynamics are still regained by solving (1) and (2) interactively. For instance, Ref. [8] processes f using a kernel function $K ^ { p , q } \in \mathbb { K } ^ { p , q } ( I )$ to relax all dissipative modes and average stiff dynamics over a sliding time interval for estimating ¯f (t). Kp,q is assumed to be $q ^ { \mathrm { t h } }$ -order differentiable $( \mathrm { i . e . , } \in \ C _ { c } ^ { q } ( \mathbb { R } ) )$ satisfying (4), with a compact support: supp(Kp,q) = I, i.e. $K ^ { p , q } ( t ) \equiv 0$ for $t \in \mathbb { R } \backslash I$ .

$$
\int_ {\mathbb {R}} K ^ {p, q} (t) t ^ {r} d t = \left\{ \begin{array}{l l} 1, & r = 0 \\ 0, & 1 \leq r \leq p. \end{array} \right. \tag {4}
$$

The kernel can be scaled by η with a similar shape as:

$$
K _ {\eta} ^ {p, q} (t) := \frac {2}{\eta} K ^ {p, q} \left(\frac {2 t}{\eta}\right), \tag {5}
$$

then, with $\eta  0$ as $| \epsilon | \to 0$ , ¯f is estimated by a convolution between the kernel and f:

$$
K _ {\eta} ^ {p, q} * \mathbf {f} = K _ {\eta} ^ {p, q} * \left(\bar {\mathbf {f}} + \tilde {\mathbf {f}} _ {\epsilon}\right)\rightarrow \bar {\mathbf {f}} \text {a s} \| \epsilon \| \rightarrow 0, \tag {6}
$$

where $\tilde { \mathbf { f } } _ { \epsilon } ( t )$ represents fast dynamics in (1) that need to be averaged, including dissipative transient and oscillatory dynamics.

A schematic HMM algorithm solves (1) by repeatedly taking these two steps is illustrated by Fig. 1 and the following:

Step 1: Evolve the micro-state to estimate macro-force: (i) Reconstruct the initial micro-state $\mathbf { x } _ { 0 } ^ { I } = \mathbf { x } ^ { I } \left( t _ { n } \right) , \mathbf { x } _ { 0 } ^ { I I } = \mathbf { x } ^ { I I } \left( t _ { n } \right)$ ; (ii) Evolve the micro-state for an interval η by solving (1) for $t \in [ t _ { n } , t _ { n } + \eta ]$ with $\mathbf { x } _ { 0 } ^ { I } , \mathbf { x } _ { 0 } ^ { I I }$ using a numerical solver (i.e. the “Micro-Solver” in Fig. 1) at a time step of h; (iii) Average the vector field of (1) on the fly to generate f via this convolution:

$$
K _ {\eta} ^ {p, q} * \left[ \begin{array}{c} \mathbf {f} ^ {I} \\ \boldsymbol {\epsilon} ^ {- 1} \mathbf {f} ^ {I I} \end{array} \right] (\mathbf {x} ^ {I} (\Delta), \mathbf {x} ^ {I I} (\Delta), \Delta) \to \overline {{\mathbf {f}}} (t _ {n} ^ {\prime}),
$$

where $\Delta = t _ { n } + \delta t \in [ t _ { n } , t _ { n } + \eta ]$ represents the evaluation point of the convolution operation.

ve the macro-state, comusing past macro-states $\mathbf { x } _ { n + 1 } ^ { I }$ and their $\mathbf { x } _ { n + 1 } ^ { I I }$ $t = t _ { n + 1 }$ $\mathbf { \bar { x } } _ { n } ^ { I } , \mathbf { \bar { x } } _ { n } ^ { I I }$ corresponding f by a numerical solver (i.e. the “Macro-Solver”) at a time step $H > > h ,$ , and then let $n = n + 1$ .

![](images/e9ad70779888110710052fe2855ed574cd9b66d9821913baa3def4d4c97ff5c5.jpg)  
Fig. 1. A two-timescale HMM scheme.

For an EMT model in the form of (1), its eigenvalues exhibit two distinct time scales, corresponding to the slow electromechanical dynamics associated with the state variables in $\mathrm { x } ^ { I }$ , and the fast EMT dynamics associated with the state variables in $\mathrm { x } ^ { I I }$ . In general, fast state variables in $\mathbf { x } ^ { I I }$ include instantaneous currents of inductive components, instantaneous voltages of capacitive components and the terminal variables controlled by power electronic converters. Slow state variables in $\mathrm { x } ^ { I }$ are typically associated with synchronous generators and their controllers, which have much slower time constants compared to $\mathrm { x } ^ { I I }$ . For the optimal performance of the proposed HMM approach, the separation between $x ^ { I }$ and $x ^ { \hat { I I } }$ can be fine-tuned. In particular, in the proposed new HMM framework, the macro-state and micro-state share the same $\mathbf { x } ^ { I }$ (i.e., slow state variables), unlike existing HMM algorithms.

In the rest of this section, subsection II-B will provide an overview of the proposed HMM approach for efficiently simulating EMT models, which includes its main idea and motivations to improve a generic HMM approach, basic steps, and its theoretical speedup on EMT simulations and computational complexity. Then, II-C introduces the EMT model considered in the paper for a power system with IBRs. II-D and II-E respectively present the detailed micro-process and macro-process algorithms of the proposed HMM approach applied to the EMT model.

# B. Overview of the Proposed HMM Approach

# 1) Main Idea and Motivations

Over the past two decades, the generic HMM concept, as discussed in Section II-A, has been successfully applied in various complex systems that exhibit obvious multi-timescale dynamics, including complex fluids [10], dynamics of solids at finite temperature [11], and the three-body problem [8]. However, as outlined in Section II-B, the original HMM framework proposed in the field of applied mathematics cannot be directly applied to power systems as highly stiff nonlinear systems networking a large variety of resources and devices. For the first time, this paper proposes a scalable HMM approach for simulations of power systems in EMT models. The proposed HMM approach for simulating the EMT model of power systems will build upon the generic HMM framework, with sufficient considerations given to EMT models and simulation requirements. Introduce an intermediate variable denoted by

${ \bf { u } } _ { \epsilon } ,$ , which are linked to the mciro-state via a compression transformation Q and a reconstruction transformation R:

$$
\mathbf {u} _ {\epsilon} = Q (\mathbf {x}), \mathbf {x} = R \left(\mathbf {u} _ {\epsilon}\right), \tag {7}
$$

Q and R can be inverses of each other when $n _ { u } = n _ { x }$ . Note that $\mathbf { u } _ { \epsilon }$ can still involve fast dynamics unless $\epsilon = 0 .$ , so its vector field $\hat { \mathbf { f } } _ { \epsilon } : \mathbb { R } ^ { n _ { u } } \times \mathbb { R } ^ { + } \mapsto \mathbb { R } ^ { n _ { \iota } }$ may still contain two timescales. Then, the macro-state u can be obtained based on the intermediate state and the macro-force:

$$
\dot {\mathbf {u}} _ {\varepsilon} = \hat {\mathbf {f}} _ {\varepsilon} \left(\mathbf {u} _ {\varepsilon}, t\right)\rightarrow \dot {\mathbf {u}} = \bar {\mathbf {f}} (\mathbf {u}, t) \text {a s} \| \boldsymbol {\epsilon} \| \text {c o n v e r g e s t o 0 .} \tag {8}
$$

Unlike [8], we assume that the macro-state may have a lower dimension than x, the micro-state of (1), i.e. $n _ { u } \leq n _ { x } ,$ Thus, the effective fore can be defined by

$$
\bar {\mathbf {f}} (t) = \lim  _ {\delta \rightarrow 0} \left(\lim  _ {\epsilon \rightarrow 0} \frac {1}{\delta} \int_ {t} ^ {t + \delta} \hat {\mathbf {f}} _ {\epsilon} (Q \mathbf {x}, \tau) d \tau\right), \tag {9}
$$

whose estimation, to avoid time-consuming computation, requires an algorithm similar to (6) but more sophisticated and considering power systems.

In bulk power system simulations assessing electromechanical transient stability, a DAE model that ignores the faster dynamics with $\mathbf { x } ^ { I I }$ by letting $\epsilon = 0$ is used. Thus, the ODE on $\mathbf { \dot { x } } ^ { T I }$ is reduced to an algebraic equation acting as constraints and control laws of the grid such as the power-flow equation. Comparatively, in the HMM framework, the fast transient dynamics are averaged for instantaneous voltages and currents of all capacitive or inductive components of the network. Even though there is still ${ \boldsymbol 0 } \approx { \bf f } ^ { I I }$ after averaging, it indicates a stable limit cycle for instantaneous voltages and currents varying at about the ac fundamental frequency 60 Hz. Further, by appropriately selecting transformations Q and R, phasor-like macro-states on voltages and currents can be obtained as more meaningful and slower variables from three-phase time-varying waveforms of voltages and currents, similar to the envelopes of voltages and currents defined in transient stability simulations.

However, the generic HMM [8] introduced above is unable to yield such macro-state variables since its R and Q are assumed to be identical operators with ${ \bf u } \equiv { \bf x } \mathrm { { \ a s } }$ |ϵ| converges to 0. Thus, $\hat { \mathbf { f } } _ { \epsilon } \equiv \mathbf { f }$ in (6), meaning the macro-force ¯f is approximated by solving the stiff dynamic system (1) directly. This implies a further derivation of (8) for EMT models. For instance, in our preliminary work [12], the generic HMM is not directly applied to a conventional abc-frame EMT model; rather, a derived 0dq-frame EMT model is used. In this paper, the proposed HMM approach is able to estimate macro-dynamics from computed micro-dynamics directly by selecting a kernel function properly. Thus, there is no need to know (8) explicitly, consistent with the motivation of the HMM. Approximate ¯f by a time series of ${ \mathbf { u } } _ { \epsilon } = { Q } ( { \mathbf { x } } )$ . Considering the strong symmetry in EMT waveforms on the micro-state, a symmetric variant bump kernel function:

$$
K (t) = \left\{ \begin{array}{l l} C e ^ {- \frac {D}{1 - t ^ {2}}}, & - 1 <   t <   1 \\ 0, & | t | \geq 1. \end{array} \right. \tag {10}
$$

is used to average the microscopic dynamics over a sliding time window of η to generate f , where C and D are adjustable parameters to satisfy (4). By utilizing the above kernel, a

new way to calculate the derivative of slow variables can be provided. For an arbitrary time interval $\Omega = [ t _ { n } , t _ { n } + \eta ]$ , let $\Delta = t _ { n } + \delta t = t _ { n } + \eta / 2 .$ , we have

$$
\begin{array}{l} K _ {\eta} * \dot {\mathbf {u}} _ {\epsilon} (\Delta) = \int_ {\mathbb {R}} \dot {\mathbf {u}} _ {\epsilon} (\tau) K _ {\eta} (\Delta - \tau) d \tau \\ = \int_ {t _ {n}} ^ {t _ {n} + \eta} \dot {\mathbf {u}} _ {\epsilon} (\tau) K _ {\eta} (\Delta - \tau) d \tau \\ = K _ {\eta} (\Delta - \tau) \mathbf {u} _ {\epsilon} (\tau) | _ {\Omega} - \int_ {t _ {n}} ^ {t _ {n} + \eta} \mathbf {u} _ {\epsilon} (\tau) d K _ {\eta} (\Delta - \tau) \\ = \int_ {t _ {n}} ^ {t _ {n} + \eta} \mathbf {u} _ {\epsilon} (\tau) K _ {\eta} ^ {\prime} (\Delta - \tau) d \tau \\ = K _ {\eta} ^ {\prime} * \mathbf {u} _ {\epsilon} (\Delta), \tag {11} \\ \end{array}
$$

where the first line is based on the definition of the convolution operation at $\Delta ;$ the second and fourth lines hold due to the compact supp $( K _ { \eta } ) = [ - \eta / 2 , \eta / 2 ]$ ; the third line follows from the Integration by Parts. Benefiting from (11), the calculation of $K _ { \eta } * \hat { \mathbf { f } } _ { \epsilon } ( \Delta )$ can be replaced by $K _ { \eta } ^ { \prime } * \mathbf { u } _ { \epsilon } ( \Delta )$ , which prevents the issue that the analytical or numerical form of $\hat { \mathbf { f } } _ { \epsilon }$ in (8) may be unknown when R and Q are not identical operators.

# 2) Steps of the Proposed HMM Approach

The proposed HMM approach for EMT models in the form of (1) adopts a solution process repeatedly performing the same two steps in an alternative way as illustrated by Fig. 1.

Step 1 (Micro-Process): Estimate the macro-force by: (i) reconstructing $\mathbf { x } _ { 0 } = R \left( \mathbf { u } _ { \epsilon , n } \right)$ at $t = t _ { n }$ by a linear or nonlinear transformation R; (ii) evolving the micro-state for interval η by solving (1) for $t \in [ t _ { n } , t _ { n } + \eta ]$ with $\mathbf { x } \left( t _ { n } \right) = \mathbf { x } _ { 0 }$ using an r-th order numerical or semi-analytical micro-solver at a time step of h for the EMT simulation, and (iii) constructing time series of $\mathbf { u } _ { \epsilon }$ in $[ t _ { n } , t _ { n } + \eta ]$ by ${ \mathbf { u } } _ { \epsilon } = Q \left( \mathbf { x } \right)$ and averaging the vector field of (1) on the fly to generate f at $t _ { n } ^ { \prime } = t _ { n } + \eta$ via:

$$
K _ {\eta} ^ {\prime} * \mathbf {u} _ {\epsilon} (\Delta) = K _ {\eta} * \hat {\mathbf {f}} _ {\epsilon} \left(\mathbf {u} _ {\epsilon} (\Delta), \Delta\right)\rightarrow \bar {\mathbf {f}} \left(t _ {n} ^ {\prime}\right), \tag {12}
$$

Here $\Delta = t _ { n } + \eta / 2$ unlike the generic HMM.

Step 2 (Macro-Process): Evolve the macro-state by computing $\mathbf { u } _ { n + 1 }$ at $t ~ = ~ t _ { n + 1 }$ by (2) using past macro-states $\mathbf { u } _ { n } , \mathbf { u } _ { n - 1 } , \ldots , \mathbf { u } _ { n - k }$ (or their estimates by the micro-solver at a later instance such as $t _ { n } ^ { \prime }$ for $\mathbf { u } _ { \epsilon } \mathbf { \epsilon } )$ and their corresponding f by an S-th order macro-solver at a time step $H > > h ,$ and then let $n = n + 1$ until termination time $T$ is approached. The overall steps are also summarized and shown in the flowchart Fig. 2.

Remark 1. The proposed HMM approach ensures smooth twoway transitions between the micro-process simulation (i.e., the full EMT simulation) and the macro-process simulation focusing on slower dynamics through a compression transformation Q that compresses the micro-state to a macro-state and its inverse, a reconstruction transformation R back to the micro-state. Detailed EMT dynamics are resolved in the microprocess using a small micro-step h for a duration of $\eta ,$ and the results are averaged via a kernel function (12) to estimate the macro-force driving the macro-state to be simulated over a much larger, macro-step H. Smoothness and numerical stability with the transitions can be ensured by the selection of a kernel function based on, e.g., [8, Lemma 2.2].

![](images/0282422fb7c178e0d8b531876a5f1246fe0dc66b7b01d5322374d6e48e51af71.jpg)  
Fig. 2. Flowchart of the proposed HMM approach

# 3) Speedup and Complexity

A detailed full EMT simulation using the same EMT model and the same time step as h with the micro-solver is equivalent to the proposed HMM approach having the micro-process spans the entire simulation period. Comparatively, the proposed HMM approach can speed up the simulation by involving successive macro-processes using a much larger time step of H. Hence, the times of speedup will increase with the increase of H and the decrease of the interval η. Besides these two, the computational complexity of the approach also depends on the micro-solver time step h. Define the kernel estimation error $| \mathcal { E } _ { H M M } | = \| K _ { \eta } ^ { \prime } * \bar { \mathbf { u } _ { \epsilon } } ( \Delta ) - \overline { { \mathbf { f } } } \left( t _ { n } ^ { \prime } \right)$ ∥, for a well-defined HMM approach, it should be bounded by $H ^ { S }$ , so that it is comparable to the local truncation error of the given macroscheme. There is a following theorem on the theoretical speedup and computational complexity of the simulation using the proposed HMM approach compared to a full EMT simulation.

Theorem 1. Suppose the micro-process uses an r-th order solver with a time step of h, the macro-process uses an $S .$ th order solver with a time step of H, and a k-th order differentiable kernel is applied to the first η interval of each micro-process, the HMM approach—alternating between the micro-process and macro-process via Q and R, both being invertible linear transformations—has these estimates on its computational complexity and speedup compared to a solution process involving only the micro-process:

$$
\text {C o m p l e x i t y} = \frac {\eta}{H h} \sim O \left(\| \epsilon \| ^ {- \frac {r + k + 1}{k r}} H ^ {- \frac {r + k + 1}{k r} S - 1}\right) \tag {13}
$$

$$
\operatorname {S p e e d u p} = \frac {H}{\eta} \sim O \left(\| \boldsymbol {\epsilon} \| ^ {\frac {1}{k} - 1} H ^ {\frac {S}{k} + 1}\right) \tag {14}
$$

such that the kernel estimation error $| \mathcal { E } _ { H M M } | \leq C _ { K } H ^ { S }$ , where $C _ { K }$ is a constant.

Proof. Suppose $K ~ \in ~ \mathbb { K } _ { \eta } ^ { p , k }$ is used. For a given microsolver, the error in approximating x in Step 1(ii) is $C _ { \mathrm { m i c r o } } h ^ { r } \eta \lVert \epsilon \rVert ^ { - ( r + 1 ) } , \ C _ { \mathrm { m i c r o } }$ is a constant, where the term $\lVert \epsilon \rVert ^ { - ( r + 1 ) }$ comes from $d ^ { ( r + 1 ) } { \bf x } / d t ^ { ( r + 1 ) }$ , notice that $Q$ is bounded, so the error in approximating $\mathbf { u } _ { \epsilon }$ is also bounded, namely, $\| Q \mathbf { x } ( t _ { n } ) - Q \mathbf { x } _ { n } \| \overset {  } { \leq } \| Q \| _ { \infty } C h ^ { r } \eta \| \epsilon \| ^ { - ( r + 1 ) }$ , thus we have the error ${ \mathcal { E } } _ { \mathrm { m i c r o } }$ in evaluating $\hat { \mathbf { f } } _ { \epsilon }$ accumulated in Step 1 (ii) and (iii) satisfies

$$
\begin{array}{l} \left| \mathcal {E} _ {\mathrm {m i c r o}} \right| \leq C _ {\mathrm {m i c r o}} \| Q \| _ {\infty} \left\| \frac {\partial \hat {\mathbf {f}} _ {\epsilon}}{\partial \mathbf {u} _ {\epsilon}} \right\| _ {\infty} \eta h ^ {r} \| \boldsymbol {\epsilon} \| ^ {- (r + 1)} \tag {15} \\ \leq \tilde {C} \eta h ^ {r} \| \boldsymbol {\epsilon} \| ^ {- (r + 2)}. \\ \end{array}
$$

Hence, it is required $\tilde { C } \eta h ^ { r } \vert \vert \boldsymbol { \epsilon } \vert \vert ^ { - ( r + 2 ) } \sim H ^ { S }$ . Omitting the constant, this leads to:

$$
h \sim O \left(\eta^ {- 1 / r} H ^ {S / r} \| \epsilon \| ^ {1 + 2 / r}\right). \tag {16}
$$

From [8, Theorem 2.7], the force estimation error using a kernel in $\mathbb { K } ^ { p , k }$ is

$$
\mathcal {E} _ {\mathrm {H M M}} ^ {(a)} \leq C _ {1} \eta^ {p} + C _ {2} \left(\frac {\| \boldsymbol {\epsilon} \|}{\eta}\right) ^ {k}, \tag {17}
$$

where $C _ { 2 }$ is proportional to $\left\| \partial \hat { \mathbf { f } } _ { \epsilon } / \partial \mathbf { u } _ { \epsilon } \right\| _ { \infty }$ , then we have $C _ { 2 } \left( \| \epsilon \| / \eta \right) ^ { k } = \tilde { C } _ { 2 } \| \epsilon \| ^ { k - 1 } / \eta ^ { k }$ . Ignoring the constants, observe that the term $\| \epsilon \| ^ { \dot { k } - 1 } / \eta ^ { \dot { k } }$ becomes dominant over $\eta ^ { p }$ for $\eta < \eta ^ { \ast } ( \Vert \epsilon \Vert )$ , allowing for the minimization of the number of micro-processes. In this case, the dominating term is

$$
\frac {\left\| \boldsymbol {\epsilon} \right\| ^ {k - 1}}{\eta^ {k}} \sim H ^ {S} \Longrightarrow \eta \sim H ^ {- S / k} \| \boldsymbol {\epsilon} \| ^ {(k - 1) / k}. \tag {18}
$$

Notice that given H is fixed, it is easy to know that (16) and (18) hold if and only if (13) and (14) hold. Hence, with conditions (13) and (14), $| \mathcal { E } _ { \mathrm { H M M } } | \leq | \mathcal { E } _ { \mathrm { m i c r o } } | + | \mathcal { E } _ { \mathrm { H M M } } ^ { ( a ) } | \leq C _ { K } H ^ { S }$

Theorem 1 can be applied to any simulation tool that implements the proposed HMM approach as long as the tool offers variable-order and variable-step solvers or allows for the adjustment of those parameters including $r , S$ and $H .$

Remark 2. When $k  \infty .$ , i.e., the kernel function becomes smooth, the complexity and speedup of the HMM framework simplify to:

$$
\text {C o m p l e x i t y} = \frac {\eta}{H h} \sim O \left(\| \boldsymbol {\epsilon} \| ^ {- \frac {1}{r}} H ^ {- \frac {1}{r} S - 1}\right), \tag {19}
$$

$$
\operatorname {S p e e d u p} = \frac {H}{\eta} \sim O \left(\| \epsilon \| ^ {- 1} H\right). \tag {20}
$$

When $r \gg S$ , increasing r reduces the overall complexity of the HMM approach because a higher order micro-solver enables more accurate simulation of the micro-process even with a larger micro-step h. Consequently, the number of microsteps can be reduced, decreasing the total computational time. However, increasing the order might require more computation for each step by the micro-solver. Therefore, the overall speedup needs to balance the tradeoff between the reduction in computational complexity due to fewer steps and the increase of the time per step caused by the higher-order micro-solver. For a power system with two time scales having a substantial gap defined by ϵ, where detailed EMT dynamics occur only for very limited durations through the simulation period, the overall speedup achieved using the HMM approach primarily depends on the macro-process simulation, which takes significantly larger macro-steps of H.

# C. Power System Models

This section introduces the EMT models of power systems considered in this paper for detailed designs and implementation of the proposed HMM approach.

# 1) Synchronous Generator and Controllers

The volage-behind-reactance model [13], which is used in EMT simulations for generators, is considered here to apply the proposed HMM approach. Each generator is modeled by these ODEs:

$$
\dot {\delta} = \Delta \omega_ {r}, \tag {21a}
$$

$$
\Delta \dot {\omega} _ {r} = \frac {\omega_ {0}}{2 H _ {g}} \left(p _ {m} - p _ {e} - D _ {g} \frac {\Delta \omega_ {r}}{\omega_ {0}}\right), \tag {21b}
$$

$$
\dot {\lambda} _ {f d} = e _ {f d} - \frac {r _ {f d}}{L _ {l f}} \left(\lambda_ {f d} - \lambda_ {a d}\right), \tag {21c}
$$

$$
\dot {\lambda} _ {1 d} = - \frac {r _ {1 d}}{L _ {1 d l}} \left(\lambda_ {1 d} - \lambda_ {a d}\right), \tag {21d}
$$

$$
\dot {\lambda} _ {1 q} = - \frac {r _ {1 q}}{L _ {1 q l}} \left(\lambda_ {1 q} - \lambda_ {a q}\right), \tag {21e}
$$

$$
\dot {\lambda} _ {2 q} = - \frac {r _ {2 q}}{L _ {2 q l}} \left(\lambda_ {2 q} - \lambda_ {a q}\right), \tag {21f}
$$

$$
\dot {i} _ {a b c} = - L _ {a b c} ^ {\prime \prime - 1} \left(v _ {a b c} - P ^ {- 1} v _ {0 d q} ^ {\prime \prime} + R _ {s} i _ {a b c} + \dot {L} _ {a b c} ^ {\prime \prime} i _ {a b c}\right), \tag {21g}
$$

where $\omega _ { 0 }$ is the nominal frequency of the system, $\delta , \Delta \omega _ { r } =$ $\omega _ { r } - \omega _ { 0 } , H _ { g } , D _ { g } , p _ { m }$ , and $p _ { e }$ represent the rotor angle, rotor speed deviation, inertial constant, damping coefficient, mechanical power, and electrical power of the generator, respectively. $\lambda _ { f d } , \lambda _ { 1 d } , \lambda _ { 1 q }$ , and $\lambda _ { 2 q }$ are flux linkages of the filed winding, d-axis damper winding, q-axis first damper winding, q-axis second damper winding, respectively; $r _ { f d } , r _ { 1 d } , r _ { 1 q } ,$ , and $r _ { 2 q }$ are resistances and $L _ { f d l } , L _ { 1 d l } , L _ { 1 q l }$ , and $L _ { 2 q l }$ are leakage inductances of these four windings; $e _ { f d }$ is the field voltage.

![](images/546a85e1fcc582f2bc78e28b91a415cc75baa5bbf8de178c80aafcfa7d71ddbe.jpg)  
Fig. 3. Diagram of a grid-following IBR model

Furthermore, $i _ { a b c }$ and $v _ { a b c }$ are three-phase terminal current and voltage that interface with the grid; $R _ { S }$ is the constant stator resistance matrix and $P ( \theta )$ is the Park transformation defined by

$$
P (\theta) = \frac {2}{3} \left[ \begin{array}{c c c} 1 / 2 & 1 / 2 & 1 / 2 \\ \cos (\theta) & \cos (\theta - 2 \pi / 3) & \cos (\theta + 2 \pi / 3) \\ - \sin (\theta) & - \sin (\theta - 2 \pi / 3) & - \sin (\theta + 2 \pi / 3) \end{array} \right] \tag {22}
$$

with the reference angle θ satisfying $\dot { \theta } = \omega _ { r }$ . Note that the subtransient inductance matrix $L _ { a b c } ^ { \prime \prime }$ periodically changes with $\theta .$ The related detailed calculation of $p _ { e } , L _ { a b c } ^ { \prime \prime }$ and subtransient voltage $v _ { 0 d q } ^ { \prime \prime }$ are shown in [13]. Without loss of generality, the TGOV1 turbine-governor model [14] and SEXS exciter model [15] are considered for generator controls in this paper.

# 2) Inverter-Based Resource

This paper considers the grid-following IBR model in Fig. 3, which comprises an outer-loop current regulator, an innerloop power regulator, a frequency droop controller, and a voltage droop controller [16]. The dynamics of its Pulsewidth modulation (PWM) are disregarded in the system-level simulation and analysis. Since Fig. 3 can illustrate the control loop in the frequency domain clearly, the mathematical model in the state space are not presented in detail here for the notation simplicity. For instance, a Phase-Locked Loop (PLL) is used to track the bus voltage angle. Note that the subscript ref represents the reference value, and 0 signifies the steady-state value. The PLL control loop is described as

$$
\theta_ {P L L} = \omega_ {P L L},
$$

$$
\dot {\phi} = v _ {t q}, \tag {23}
$$

$$
\omega_ {P L L} = \omega_ {\mathrm {s}} + K _ {P L L} ^ {\mathrm {p}} \dot {\phi} + K _ {P L L} ^ {\mathrm {i}} \phi ,
$$

where $\theta _ { P L L }$ is the angle of the point of common coupling (PCC) voltage, $\omega _ { P L L }$ is the frequency of the inverter, ϕ is the intermediate variable in the PLL control loop, and $K _ { P L L } ^ { \mathrm { P } }$ and $K _ { P L L } ^ { \mathrm { I } }$ are the corresponding PI gains of the PLL loop, $v _ { t q }$ is the q-axis PCC voltage under a local Park transformation $P ( \theta _ { P L L } )$ . For the current regulator, power regulator, and droop regulator, the detailed information used in this paper can be found in [16], [17].

# 3) Network

To model the power network, the Π-model is considered for each line, which includes R-L circuits and shunt capacitances

in abc-frame. Loads in EMT models are also regarded as R-L or R-C circuits.

The whole network is modeled as a directed graph $\mathcal { G } =$ $( \mathcal { N } , \mathcal { P } )$ with N nodes and P edges with an arbitrary direction assigned to each edge $l \in \mathcal { P }$ . The incidence matrix $\dot { B } \in \mathbb { R } ^ { N \times E }$ can represent the connectivity of the network topology from a one-line diagram view:

$$
B _ {k, l} := \left\{ \begin{array}{l l} + 1 & , k = i \\ - 1 & , k = j \\ 0 & , \text {o t h e r w i s e}, \end{array} \right. \forall l = (i, j) \in \mathcal {P}.
$$

Note that for a three-phase balanced system, the connectivity is identical for different phases, and the incidence matrix $B$ can be generalized easily as an incidence matrix B ∈ R3N×3E $\in \mathbb { R } ^ { 3 N \times 3 E }$ for the three-phase network by mapping each entry of B to the corresponding $3 \times 3$ matrix $( \mathrm { i . e . , ~ + 1 \mapsto + } I _ { 3 \times 3 } , - 1 \mapsto - I _ { 3 \times 3 }$ and $0 \mapsto \mathbb { O } _ { 3 \times 3 } )$ , leading this three-phase state-space network equation:

$$
\left[ \begin{array}{c c} \mathbf {C} & \\ & \mathbf {L} \end{array} \right] \left[ \begin{array}{l} \dot {\mathbf {v}} _ {a b c} \\ \dot {\mathbf {w}} _ {a b c} \end{array} \right] = \left[ \begin{array}{c c} - \mathbf {G} & - \mathbf {B} \\ \mathbf {B} ^ {\top} & - \mathbf {R} \end{array} \right] \left[ \begin{array}{l} \mathbf {v} _ {a b c} \\ \mathbf {w} _ {a b c} \end{array} \right] + \left[ \begin{array}{l} \mathbf {i} _ {a b c} \\ \mathbb {O} _ {3 E} \end{array} \right], \tag {24}
$$

where $\mathbf { v } _ { a b c } \in \mathbb { R } ^ { 3 N }$ and ${ \bf w } _ { a b c } \in \mathbb { R } ^ { 3 E }$ are three-phase node voltages and line currents associated with the capacitive and inductive storage elements inside the network, $\mathbf { i } _ { a b c }$ is the current injection from generators and IBRs to the network. $\mathbf { C } \in \mathbb { R } ^ { 3 N \times 3 N } , \mathbf { G } \in \mathbb { R } ^ { 3 N \times 3 N } , \mathbf { L } \in \mathbb { R } ^ { 3 E \times 3 E }$ , and $\mathbf { R } \in \mathbb { R } ^ { 3 E \times 3 E }$ are three-phase parameter matrices consisting of shunt capacitance $C _ { i }$ and conductance $G _ { i } = R _ { i } ^ { - 1 } , \forall i \in \mathcal { N }$ and line inductance $L _ { i j }$ and resistance $R _ { i j } , \forall ( i , j ) \in \mathcal { P }$ . Equ. (24) is derived from Kirchhoff’s current law and Kirchhoff’s voltage law with algebraic graph theory [18]. Notice that the $\mathbf { i } _ { a b c }$ represents the interconnection between sources and the network, for instance, a generator’s current injection to the connected bus is induced by (21g).

While a detailed power system model is presented here, the proposed approach also applies to models of other forms or time scales. A distinguishing feature of the HMM framework is that it requires only a single ODE model of the power system, namely the full EMT model. In other words, both the micro-process and macro-process are simulated using the same model, eliminating the need for model reduction of individual generators, control systems, or IBRs. The macro-state is computed directly from the micro-state and is driven by a macro-force derived from a kernel function. This characteristic ensures that the proposed HMM framework is potentially applicable to any dynamical system for which an ODE model is available.

Based on these power system models, the detailed algorithms of the proposed HMM approach are presented as follows.

# D. Proposed Algorithms for the Micro-Process

The DT (Differential Transformation) method [19] is applied as the micro-solver to simulate the micro-state in the proposed HMM approach.

# 1) Construction and Reconstruction

Notice that state variables $\mathbf { v } _ { a b c } , \ \mathbf { w } _ { a b c } ,$ and $\mathbf { i } _ { a b c }$ can be transformed into 0dq-frame via a global Park transformation $P ( \theta _ { \mathrm { g l o b a l } } )$ using a global reference angle $\theta _ { \mathrm { g l o b a l } }$ , by which

the dynamics associated with the synchronous frequency (e.g. 60Hz) are almost eliminated while fast EMT dynamics and slow electro-mechanical dynamics with the network state variables become more obvious [20] even under balanced cases. Thus, a kernel function is needed to average the simulated micro-state. The existence of two time scales, e.g. EMT dynamics vs. electromechanical dynamics, in the EMT model helps design the compression transformation Q from the micro-state to macrostate and the reconstruction transformation $R = Q ^ { - 1 }$ . In this paper, for $\mathbf { x } = [ \mathbf { x } ^ { I } , \mathbf { x } ^ { I I } ] ^ { \top } , \mathbf { x } ^ { I }$ on slow dynamics includes the state variables of generators and IBRs except for their terminal currents $\mathbf { i } _ { a b c } ;$ on fast dynamics, $\mathbf { x } ^ { I I } : = [ \bar { \mathbf { v } } _ { a b c } , \ \mathbf { w } _ { a b c } , \ \mathbf { i } _ { a b c } ] ^ { \top }$ includes all network state variables. Thus, the compression transformation $Q$ from the micro-state to macro-state can comprise a Park transformation for network variables and an identify matrix for the other variables. The compression and reconstruction transformations are defined accordingly as Q := diag $( \mathbb { I } , \mathbf { P } ( \theta _ { \mathrm { g l o b a l } } ) )$ ) and R := diag $\left( \mathbb { I } , \mathbf { P } ^ { - 1 } ( \theta _ { \mathrm { g l o b a l } } ) \right)$  where I is the identical matrix with the same dimension as $\mathbf { \Delta x } ^ { I }$ and $\mathbf { P } ( \theta _ { \mathrm { g l o b a l } } )$ is the vectorized invertible Park transformation for all network dynamics such that

$$
\left[ \begin{array}{l} \mathbf {v} _ {0 d q} \\ \mathbf {w} _ {0 d q} \\ \mathbf {i} _ {0 d q} \end{array} \right] = \mathbf {P} \left(\theta_ {\text {g l o b a l}}\right) \left[ \begin{array}{l} \mathbf {v} _ {a b c} \\ \mathbf {w} _ {a b c} \\ \mathbf {i} _ {a b c} \end{array} \right]. \tag {25}
$$

We have the intermediate state $\mathbf { u } _ { \epsilon } = Q ( \mathbf { x } ) = \left[ \mathbf { u } _ { \epsilon } ^ { I } , \mathbf { u } _ { \epsilon } ^ { I I } \right] ^ { \top }$ as a transformation from the micro-state where $\bar { \mathbf { u } } _ { \epsilon } ^ { I } = \mathbf { x } ^ { \bar { I } }$ and $\mathbf { u } _ { \epsilon } ^ { I I } : = \left[ \mathbf { v } _ { 0 d q } , \mathbf { w } _ { 0 d q } , \mathbf { i } _ { 0 d q } \right] ^ { \top }$ . Starting from this intermediate state, the macro-state u focusing on slow dynamics can evolve governed by a macro-force obtained by (12). Note that in general, the angle $\theta _ { \mathrm { g l o b a l } }$ is not necessarily identical for all different state variables. For instance, each interface variable $\mathbf { i } _ { a b c }$ can utilize the reference angle of the local 0dq frame of the connected generator or IBR.

# 2) Simulating Micro-State

Consider the previous dynamic system (1) which is Lipschitz on $\mathbb { R } ^ { n _ { x } }$ :

$$
\dot {\mathbf {x}} = \mathbf {f} (\mathbf {x}, t). \tag {26}
$$

The micro process involves solving (26) in $[ t _ { n } , t _ { n } + \eta ]$ . Given an initial state $\mathbf { x } _ { \mathrm { 0 } }$ at $t _ { n }$ by reconstruction ${ \bf x } _ { 0 } = R { \bf u } _ { \epsilon , n }$ , the solution of (26) is characterized by:

$$
\mathbf {x} (t) = \boldsymbol {\Phi} (t, \mathbf {x} _ {0}), \tag {27}
$$

which satisfies the corresponding initial value condition:

$$
\mathbf {x} \left(t _ {n}\right) = \boldsymbol {\Phi} \left(t _ {n}, \mathbf {x} _ {0}\right) = \mathbf {x} _ {0}. \tag {28}
$$

Suppose that $\Phi ( t , \bf { x } _ { 0 } )$ is sufficiently smooth in a neighborhood $B _ { \delta } ( t _ { n } , { \bf x _ { 0 } } )$ , its power series can be expanded up to a certain order L within $B _ { \delta } ( t _ { n } , \mathbf { x _ { 0 } } )$ :

$$
\begin{array}{l} \Phi (t, \mathbf {x} _ {\mathbf {0}}) = \sum_ {k = 0} ^ {L} \frac {1}{k !} \frac {\partial^ {k} \Phi (t , \mathbf {x} _ {\mathbf {0}})}{\partial t ^ {k}} \Bigg | _ {t = t _ {n}} (t - t _ {n}) ^ {k} \tag {29} \\ + \mathbf {R} (\boldsymbol {\Theta}) (t - t _ {n}) ^ {L + 1}, \\ \end{array}
$$

where $\mathbf { R } ( \Theta )$ is a constant related to order $L , t _ { n } .$ , and t. The approximated solution $\tilde { x }$ can be rewritten in a compact form:

$$
\begin{array}{l} \mathbf {x} (t) \approx \tilde {\mathbf {x}} \left(\mathbf {x} _ {0}, L, h\right) := \sum_ {k = 0} ^ {L} \mathbf {X} [ k ] h ^ {k}, \tag {30} \\ \mathbf {X} [ k ] = \frac {1}{k !} \frac {\partial^ {k} \Phi (t , \mathbf {x _ {0}})}{\partial t ^ {k}} \Bigg | _ {t = t _ {n}}, \\ \end{array}
$$

where $h = t - t _ { n }$ represents the step size. The main task of the DT algorithm is to find a recursive way to solve $\mathbf { X } [ k ]$ up to a desirable order L in a certain time interval around $t _ { n } .$ . The basic steps of the DT algorithm are shown as follows:

i) Derivation of DT Formulation. Given an ODE system (26), the corresponding DT formulation can be derived utilizing the characterization of the original ODE system and linear independence of polynomials’ coefficients. Some fundamental rules to transform time domain functions into DT forms are summarized by [19], [21]. For instance, consider vectorized functions ${ \pmb \sigma } ( t ) , { \pmb \xi } ( t ) , \gamma ( t ) , { \bf g } _ { s } ( t ) , { \bf g } _ { c } ( t )$ with vector coefficients $\Sigma [ k ] , \ \Gamma [ k ] , \ \mathbf { G } _ { c } [ k ] , \ \mathbf { G } _ { s } [ k ]$ , mappings of the k-th order coefficients of compositional functions are:

$\mathrm { i } ) \gamma ( t ) = \pmb { \sigma } ( t ) \pm \pmb { \xi } ( t )  \mathbf { \Gamma } [ k ] = \pmb { \Sigma } [ k ] \pm \Xi [ k ] ;$   
$\operatorname { i i } ) \gamma ( t ) = { \pmb \sigma } ^ { \top }  \Gamma [ k ] = \pmb { \Sigma } [ k ] ^ { \top } ;$

$\mathrm { i i i } ) { \bf { g } } _ { c } ( t ) = \cos ( \pmb { \sigma } ( t ) )  { \bf { G } } _ { c } [ k ] = \sum _ { j = 1 } ^ { k } \frac { j } { k } { \bf { T } } [ j ] \odot { \bf { G } } _ { s } [ k - j ] ;$ j Γ[j] ⊙ Gs[k − j]; j=1   
$\mathrm { i v } ) \ \mathbf { g } _ { s } ( t ) = \sin ( \pmb { \sigma } ( t ) )  \mathbf { G } _ { s } [ k ] = \sum _ { i = 1 } ^ { k } \frac { j } { k } \mathbf { T } [ j ] \odot \mathbf { G } _ { c } [ k - j ] ;$

where ⊙ represents the element-wise product of vectors. With these DT rules and more shown in [19], the dynamic system $\dot { \mathbf { x } } = \mathbf { f } ( \mathbf { x } , t )$ can be transformed into DT-form $\mathbf { F } [ k ]$ derived in [21]:

$$
(k + 1) \mathbf {X} [ k + 1 ] = \mathbf {F} [ k ] := \mathbf {F} (\mathbf {X} [ j ]), \quad j = 0, \dots , k, \tag {31}
$$

which allows us to solve the DT formulation instead of the original system. Note that this is a general way to solve ${ \bf x } ( t )$ up to an arbitrary desirable order approximation. Then, coefficients $\mathbf { X } [ k ]$ are solved based on the explicit DT form (31) recursively from $k = 1$ to L, providing an $L ^ { \mathrm { { \bar { t h } } } }$ order approximation solution of Φ in $B _ { \delta } ( t _ { n } , { \bf x _ { 0 } } )$ .

ii) Variable-step micro-process simulation. This paper focuses on variable-step micro-process simulation since fixed-step algorithms have been widely adopted. After calculating power coefficients $\mathbf { X } [ k ]$ , a forward result at $t _ { n } + h$ is obtained by evaluating power series (30), thanks to the desirable convergence and accuracy of power series approximations with a relative high L, the predefined step size h is relatively large compared with traditional numerical methods. Consider solving (26) requires multiple time steps, the step size $h _ { m }$ is defined as $m ^ { \mathrm { t h } }$ step at $n ^ { \mathrm { t h } }$ interval, so the result at $m + 1 ^ { \mathrm { t h } }$ step at $n ^ { \mathrm { t h } }$ interval is:

$$
\mathbf {x} _ {m + 1} = \tilde {\mathbf {x}} \left(\mathbf {x} _ {m}, L, h _ {m}\right). \tag {32}
$$

Note that $\mathbf { x } _ { m } = \mathbf { X } [ 0 ]$ is at $\begin{array} { r } { t _ { n } + \sum _ { j = 1 } ^ { m - 1 } h _ { j } } \end{array}$ with $m \geq 1$ , so suppose we are at tn + Pm−1j=1 h $\begin{array} { r } { t _ { n } + \sum _ { j = 1 } ^ { m - 1 } h _ { j } } \end{array}$ and the initial value $\mathbf { x } _ { m }$ is known, then (32) can be directly calculated. However, to maintain the accuracy towards uncertain dynamics, it is helpful to control time step $h _ { m }$ within a certain range, so the difference error is bounded [22]:

$$
\left\| \dot {\mathbf {x}} _ {m + 1} - \mathbf {f} \left(\mathbf {x} _ {m + 1}, t _ {n} + \sum_ {j = 1} ^ {m} h _ {j}\right) \right\| _ {\infty} <   \epsilon_ {1}, \tag {33}
$$

where $\epsilon _ { 1 }$ is a predefined threshold of the error, $\dot { \mathbf { x } } _ { m + 1 }$ can be calculated by (32). While (33) provides a general way to design control strategies, it is not necessary to control all equations

when the dynamics of certain state variables are known much faster than others, especially in multi-scale problems. In this paper, the defect control of time steps of (24) is proposed. The motivation is that the dynamics of internal state variables of generators and IBRs are slower, so the step size is highly limited by (24). By utilizing the DT algorithm, (33) has an explicit form provided by the following theorem. For the notation simplicity, define $\boldsymbol { \psi } : = \left[ \mathbf { v } _ { a b c } , \mathbf { w } _ { a b c } \right] ^ { \top }$ and $\pmb { \lambda } : = \left[ \mathbf { i } _ { a b c } , \mathbb { O } _ { 3 E } \right] ^ { \top }$ , also, the corresponding $k ^ { \mathrm { { t h } } }$ order coefficients are Ψ[k] and $\mathbf { \boldsymbol { \Lambda } } [ k ]$ , namely, $\psi _ { m + 1 } = \tilde { \psi } ( \psi _ { m } , L , h _ { m } )$ and $\lambda _ { m + 1 } = \tilde { \lambda } ( \lambda _ { m } , L , h _ { m } )$ and

$$
\mathbf {A} _ {e q} := \left[ \begin{array}{c c} \mathbf {C} & \\ & \mathbf {L} \end{array} \right] ^ {- 1} \left[ \begin{array}{c c} - \mathbf {G} & - \mathbf {B} \\ \mathbf {B} ^ {\top} & - \mathbf {R} \end{array} \right], \mathbf {B} _ {e q} := \left[ \begin{array}{c c} \mathbf {C} & \\ & \mathbf {L} \end{array} \right] ^ {- 1}. \tag {34}
$$

Based on (33), define the error induced by (32) in (24) as

$$
\mathcal {E} _ {m} := \| \dot {\psi} _ {m} - \mathbf {A} _ {e q} \psi_ {m} - \mathbf {B} _ {e q} \boldsymbol {\lambda} _ {m} \| _ {\infty}. \tag {35}
$$

The following theorem is provided.

Theorem 2. Given the linear form of (24) and the $L ^ { t h }$ order DT algorithm, the error in (32) can be estimated on the fly of the simulation once the highest coefficients are calculated, i.e.,

$$
\begin{array}{l} \mathcal {E} _ {m + 1} = \left\| \dot {\psi} _ {m + 1} - \mathbf {A} _ {e q} \psi_ {m + 1} - \mathbf {B} _ {e q} \boldsymbol {\lambda} _ {m + 1} \right\| _ {\infty} \tag {36} \\ = \left\| \mathbf {A} _ {e q} \boldsymbol {\Psi} [ L ] + \mathbf {B} _ {e q} \boldsymbol {\Lambda} [ L ] \right\| _ {\infty} (h _ {m}) ^ {L}. \\ \end{array}
$$

Proof. The corresponding DT formulation of (24) is

$$
\Psi [ k + 1 ] = \mathbf {A} _ {e q} \Psi [ k ] + \mathbf {B} _ {e q} \boldsymbol {\Lambda} [ k ], \forall 0 \leq k \leq L - 1. \tag {37}
$$

Notice

$$
\psi_ {m + 1} = \sum_ {\substack {k = 0 \\ I}} ^ {L} \Psi [ k ] \left(h _ {m}\right) ^ {k}, \tag{38}
$$

$$
\boldsymbol {\lambda} _ {m + 1} = \sum_ {k = 0} ^ {L} \boldsymbol {\Lambda} [ k ] \left(h _ {m}\right) ^ {k}.
$$

Substituting them into (24), we have

$$
\begin{array}{l} \mathcal {E} _ {m + 1} = \left\| \dot {\boldsymbol {\psi}} _ {m} - \mathbf {A} _ {e q} \boldsymbol {\psi} _ {m} - \mathbf {B} _ {e q} \boldsymbol {\lambda} _ {m} \right\| _ {\infty} \\ = \| \sum_ {k = 0} ^ {L - 1} \Psi [ k + 1 ] \left(h _ {m}\right) ^ {k} \\ - \sum_ {k = 0} ^ {L} \left[ \mathbf {A} _ {e q} \boldsymbol {\Psi} [ k ] (h _ {m}) ^ {k} - \mathbf {B} _ {e q} \boldsymbol {\Lambda} [ k ] (h _ {m}) ^ {k} \right] \| _ {\infty} \\ = \| \left\{\sum_ {k = 0} ^ {L - 1} \left(\boldsymbol {\Psi} [ k + 1 ] - \mathbf {A} _ {e q} \boldsymbol {\Psi} [ k ] - \mathbf {B} _ {e q} \boldsymbol {\Lambda} [ k ]\right) \right. \\ + \mathbf {A} _ {e q} \boldsymbol {\Psi} [ L ] + \mathbf {B} _ {e q} \boldsymbol {\Lambda} [ L ] \} \| _ {\infty} \left(h _ {m}\right) ^ {k}. \tag {39} \\ \end{array}
$$

With (37), the first sum term is zero and we have ${ \mathcal { E } } _ { m + 1 } =$ $\| \mathbf { A } _ { e q } \Psi [ L ] + \mathbf { B } _ { e q } \pmb { \Lambda } [ L ] \| _ { \infty } ( h _ { m } ) ^ { L }$ .

Theorem 2 ensures the accuracy and numerical stability of the micro-process in the HMM approach when applied to any dynamical system modeled by ODEs, regardless of the simulation platform. Note that different from other numerical methods, (36) provides an explicit way to compute an estimated error, then the step size $h _ { m }$ with the satisfactory error can be obtained by solving $\mathcal { E } _ { m + 1 } = \epsilon _ { 1 }$ .

iii) Evaluation at a New Point. After calculating the forward result, i.e., $\mathbf { x } _ { m + 1 }$ at $\begin{array} { r } { t _ { n } + \sum _ { j = 1 } ^ { m } h _ { j } } \end{array}$ , new $0 ^ { \mathrm { t h } }$ coefficients $\mathbf { X } [ 0 ]$ at $\begin{array} { r } { t _ { n } + \sum _ { j = 1 } ^ { m } h _ { j } } \end{array}$ are obtained. Repeat the previous steps, $\mathbf { x } _ { m + 2 }$ can then be computed until the terminated time $t _ { n } + \eta$ for the $n ^ { \mathrm { t h } }$ micro process is achieved.

# 3) Kernel Averaging

After time series of micro-state ${ \bf x } ( t )$ are simulated, the macrostate variables can be computed by ${ \mathbf { u } } _ { \epsilon } = { Q } ( { \mathbf { x } } )$ . The proposed kernel averaging method provides a general way to approximate slow dynamics behind the fast dynamics for all state variables, but only a certain group of state variables are necessary to be averaged to save the computational time and complexity. Recall state variables are separated into two groups: $\mathbf { x } \overset { \cdot } { = } \left\lceil \mathbf { x } ^ { I } , \ \mathbf { x } ^ { I I } \right\rceil ^ { \top }$ where $\mathbf { x } ^ { I I } = [ \mathbf { v } _ { a b c } , ~ \mathbf { w } _ { a b c } , ~ \mathbf { i } _ { a b c } ] ^ { \top }$ . Here vector fields of two groups are defined as $\mathbf { f } ^ { I }$ and $\mathbf { f } ^ { I I }$ respectively. The convolution operation (12) with $\mathbf { u } ^ { I I }$ is considered, and the corresponding force is estimated by (12)

$$
\bar {\mathbf {f}} ^ {I I} \left(t _ {n} ^ {\prime}\right) \approx K ^ {\prime} * \mathbf {u} _ {\epsilon} ^ {I I}, \tag {40}
$$

where $\bar { \mathbf { f } } ^ { I I }$ is independent with stiff parameters ϵ in (1). Then, the macro step-size can be large and is not limited by $\mathbf { x } ^ { I I }$ anymore. Note the accuracy of the remaining part $\mathbf { x } ^ { \bar { I } }$ will be enhanced in the macro part which will be introduced momentarily.

# E. Proposed Algorithms for the Macro-Process

This section introduces the detailed macro process for both fixed-step and variable-step simulations.

1) Fixed-step macro-process simulation: After the kernel averaging in the micro-process, the value of the macro-state u at time $t _ { n + 1 } , \mathrm { i . e . , } \ \mathbf { u } _ { n + 1 }$ , is well estimated by the Forward Euler scheme:

$$
\mathbf {u} _ {n + 1} ^ {I I} = \mathbf {u} _ {\epsilon} ^ {I I} \left(t _ {n} ^ {\prime}\right) + (H - \eta) \bar {\mathbf {f}} ^ {I I} \left(t _ {n} ^ {\prime}\right), \tag {41a}
$$

$$
\mathbf {u} _ {n + 1} ^ {I} = \mathbf {u} _ {\epsilon} ^ {I} \left(t _ {n} ^ {\prime}\right) + (H - \eta) \mathbf {f} ^ {I} \left(\mathbf {x} \left(t _ {n} ^ {\prime}\right), t _ {n} ^ {\prime}\right), \tag {41b}
$$

where ${ \mathbf { u } } _ { \epsilon } = Q { \mathbf { x } }$ and the partial vector field $\mathbf { f } ^ { I } \left( \mathbf { x } _ { n ^ { \prime } } , t _ { n } ^ { \prime } \right)$ can be obtained directly from the micro process simulation. While it depends on ϵ implicitly, it generally exhibits slow dynamics compared with $\mathbf { x } ^ { \hat { I } I }$ . So using (41b) without kernel averaging is acceptable, which also explains the reason for using identical operators for $\mathbf { x } ^ { I }$ previously. With $\mathbf { u } _ { n + 1 }$ from (41) in hand, the accuracy of $\mathbf { f } ^ { I }$ can be further enhanced by averaging two steps’ vector fields by

$$
\bar {\mathbf {f}} ^ {I} \left(t _ {n} ^ {\prime}\right) := \frac {1}{2} \left[ \mathbf {f} ^ {I} \left(\mathbf {x} \left(t _ {n} ^ {\prime}\right), t _ {n} ^ {\prime}\right) + \mathbf {f} ^ {I} \left(R \mathbf {u} _ {n + 1}, t _ {n + 1}\right) \right]. \tag {42}
$$

Then with $\bar { \bf f } = [ \bar { \bf f } ^ { I } , \bar { \bf f } ^ { I I } ] ^ { \top }$ in hand, the vector form of the macro process can be written as

$$
\mathbf {u} _ {n + 1} = \mathbf {u} _ {\epsilon} \left(t _ {n} ^ {\prime}\right) + (H - \eta) \bar {\mathbf {f}} \left(t _ {n} ^ {\prime}\right). \tag {43}
$$

Compared with the step size $h _ { m }$ in the micro process, the interval of a macro process H is much larger which can accelerate the simulation speed without causing numerical stability problems.

2) Variable-step macro-process simulation: The macrostep can be controlled by an integral controller, enabling variable-step macro-process simulations.With (41) in hand, define the macro step size $M h \quad : = \quad H \ - \ \eta , \ \mathbf { f } _ { n } \quad : =$ $[ \mathbf { f } ^ { I } \left( \mathbf { x } ( t _ { n } ^ { \prime } ) , t _ { n } ^ { \prime } \right) , \ \bar { \mathbf { f } } ^ { I I } \left( t _ { n } ^ { \prime } \right) ] ^ { \top }$ , a zeroth-order error at $n ^ { \mathrm { t h } }$ step can be estimated by

$$
r := \left(\max  _ {1 \leq i \leq \mathbb {R} ^ {n _ {u}}} \left| \frac {M h _ {n} \mathbf {f} _ {n}}{\left| \left[ \mathbf {u} _ {\epsilon} \left(t _ {n} ^ {\prime}\right) \right] _ {i} \right| + 1} \right|\right). \tag {44}
$$

Then, the local truncation error considering high-order errors and the control strategy of the macro-step can be estimated as follows, which can be used to control the truncation error induced by (41)

$$
e _ {n} = \frac {r}{1 - r},
$$

$$
\rho_ {n + 1} = \min  \left\{\left(\frac {\operatorname {T o l}}{e _ {n}}\right), \rho_ {\max } \right\}, \tag {45}
$$

$$
M h _ {n + 1} = \min  \left\{\rho_ {n + 1} M h _ {n}, M h _ {\max } \right\},
$$

where $M h _ { \operatorname* { m a x } } = 0 . 0 4$ and $\rho _ { \mathrm { m a x } } = 1 . 0 5 [ 2 3 ]$ . Then the variablesstep macro-process can be

$$
\mathbf {u} _ {n + 1} = \mathbf {u} _ {\epsilon} \left(t _ {n} ^ {\prime}\right) + M h _ {n} \bar {\mathbf {f}} \left(t _ {n} ^ {\prime}\right). \tag {46}
$$

# F. Comparison with Other Multi-Timescale Methods

To accelerate EMT simulations, multi-rate EMT methods have been proposed and applied for decades [3], [24]–[28]. To use these methods, the EMT model of a power system must be partitioned into a critical area that retains the detailed EMT model and an external area in which model reduction is required prior to simulations to generate a simplified model based on positive-sequence phasors [2], [3] or dynamic phasors [25]. For instance, in phasor-EMT co-simulations, a phasor-based transient stability model is often adopted for the external area [2]. The critical and external areas are then co-simulated using either different simulators or settings, such as step sizes, via an interfacing algorithm. While these co-simulation methods are faster than a full EMT simulation of the entire system, they have notable limitations. First, the critical EMT area is typically determined offline to include, e.g., an inverter-based solar farm or wind farm for accurate simulations. Identifying the boundary of such a critical area can be challenging when IBRs highly penetrate and become dense in the power network [27]. Second, interfacing two simulators across the boundary often introduces larger errors near the boundary [27] or even leads to divergence [29]. While increasing the number of iterations between the two simulators at each time step can reduce these errors, it also significantly increases the computational time. Third, to reduce the number of state variables, any model reduction algorithm must assume which dynamics are unimportant or ignorable. As a result, co-simulations may be unreliable or omit significant details if any assumptions are inaccurate or the model is not appropriately reduced.

The proposed HMM framework takes a fundamentally different approach with the following advantages. First, the HMM approach does not require pre-defining model partition boundaries or reducing the model prior to simulation. Instead,

it decomposes the simulation process in time by automatically alternating between a micro-process for detailed EMT simulation and a macro-process focusing on slower dynamics, both conducted on the same EMT model of the original system. Second, the HMM approach adaptively switches between the two processes at different timescales and adjusts the step size to ensure accuracy for both fast and slow dynamics. Theorem 1 provides theoretical guidance for selecting the lengths and step sizes of the micro-process and macro-process to achieve the desired performance. Third, the HMM framework can accommodate or complement other accelerated EMT simulation methods, such as the phasor-EMT co-simulation method. For example, while the external area is simulated using a phasorbased simulator, the critical EMT area can be further accelerated with the HMM approach.

# III. CASE STUDIES

In this section, the proposed HMM approach is first validated by simulations on a two-area system and the IEEE 39- bus system. The simulation results are benchmarked with simulations using the fourth-order Runge-Kutta (RK4) method with a small time step $h = 5 ~ \mu \mathrm { s }$ . Then, the approach is tested on a large 390-bus system and compared with commercial tools including PSCAD and RK45. All proposed algorithms are implemented in Matlab 2023b using scripts and tested on a desktop computer with 13th-generation Intel i7-13700K processor and 32GB RAM.

# A. Test on Kundur’s Two-area System

The case study on this small system is to verify (13) and (14) on the complexity and speedup using the proposed HMM approach. Replace generator G1 by the IBR model as shown in Fig. 4. Apply the HMM approach to simulate three contingencies (named S1, S2, and S3) which are three-phase bus grounding faults at buses 7, 8, and 9, lasting for 0.1 s and then being cleared after 5 cycles without losing any component. These contingencies are simulated for 10s.

![](images/a813de286e3a08cd57375f4ddd80db3915c1cf61408da8fec5f7a37fa785522d.jpg)  
Fig. 4. Kundur’s two-area system

TABLE I PARAMETERS FOR KUNDUR’S TWO-AREA SYSTEM   

<table><tr><td>h</td><td>L</td><td>η</td><td>C</td><td>D</td><td>θglobal</td></tr><tr><td>330 μs</td><td>30</td><td>0.0264 s</td><td>3.0739</td><td>1.25</td><td>θ1</td></tr></table>

The parameters of the HMM approach are given in Table I for all contingencies. Selection of these parameters are explained as follows. Here h is the time step for simulating the micro-state using the DT-based the micro-solver, and is assumed constant

to verify the complexity and speedup of the approach with different lengths of H. The selection of pair $( h , L )$ follows [30] which demonstrates good accuracy and speed for the DT algorithm. The micro-interval η should cover at least one period for a current or voltage waveform, i.e., 0.0167s under 60 Hz. Thus, η is selected to cover 80 steps of h. D is selected according to $[ 9 ] ,$ and C is uniquely determined to satisfy (4). Furthermore, the $\theta _ { \mathrm { g l o b a l } } = \theta _ { 1 }$ from generator G1 for simplicity. Although the proposed HMM approach is expected to provide significant acceleration in simulations, it may be also desirable to run a detailed EMT simulation for a brief initial time window to capture all fast transient dynamics under the fault. Thus, the HMM approach is activated at 1s afte the disturbance and applied for the rest of the simulation period.

![](images/92720159a540bdafbeadd544595ae817080c0818c6510d8275acb50525e3d7b1.jpg)  
(a)

![](images/aad739c9c69d8468a59aed34c804869cec95a0c6513b9203995bda0f5eb2a847.jpg)  
(b)

![](images/9ba0e7b46c077f34dde6591e70a27d6e9229a41510b354649a833c89cb9a48a2.jpg)  
(c)

![](images/e6cc991fd65f1b55cb0b44be16a8a73f88587265e1d616a0a534076a18ad927d.jpg)  
  
Fig. 5. Convergence analysis for HMM in two-area system under three scenarios. (a) Execution time under different H. (b) Speedup compared with the reference simulations. (c) Integral errors. (d) Execution time for reference simulations using a 10µs time step.

To verify (13) and (14), different values of H are tested, and the corresponding execution times and the speedup factor for three contingencies are shown in Fig. 5a and Fig. 5b. The reference simulations use a 10µs time step as the benchmark of speedup of the proposed method. Fig. 5c confirms the convergence of the simulations by an error defined as the averaged integral of the infinity norm of the difference between the benchmark $\begin{array} { r } { \mathbf { x _ { b h } } ( t _ { n } + \sum _ { j = 1 } ^ { m - 1 } h _ { j } ) } \end{array}$ j=1 and $\mathbf { x _ { m } }$ for all micro intervals along the simulation time T .

It can be concluded that for all contingencies, increasing H can accelerate the simulation, and the speedup ratio is proportional to $H / \eta ,$ , matching exactly the definition in (14). Also, note that the complexity is proportional to the reciprocal of speedup when the micro step-size h is fixed, so it is also proved well-defined as a dual form of the speedup.

In particular, simulation results on several state variables are shown in Fig. 6, including rotor angle speeds and instantaneous line currents for S1, S2, and S3 with $H = 2 . 6 2 5 \eta$ . From these figures, the micro-state and macro-state of the system are simulated alternatively with their respectively time steps h

and H. All simulated micro-state results match accurately the benchmark results. More importantly, for a majority of the simulation period, a much larger macro time step H, instead of h, is used without causing numerical instability. This leads to over eight-fold acceleration. Note that without using any reduced models created ahead of simulations, the proposed approach successfully reduces the EMT model (1) on the fly of simulation for significant speedup.

![](images/0168ba0cc87c862effbae13f37d0f5d687b50d2b0a8ed3a29014d24106e9c9ac.jpg)  
(a)

![](images/dc0c61a72576ca5b8c446f6e146ad21fea604d854921e8fa20f51573fc85b78b.jpg)  
(b)

![](images/cb2c04278de52717d70772567d1541f2ca08730a832c6e9aafe40d6c61da5fb7.jpg)  
(c)

![](images/1771d823f6d6433ba10acd41e75a61802847b5b9048d7eae661df3d000ac5932.jpg)

![](images/e24b2718a52cde6d05618c6a5561e2d315a1395d970669e765e4146c36813464.jpg)  
(e)

![](images/be83cb14d1f06250cb19bb26ffe01f37945ec87028f1f8f111af5d11e3c1eba2.jpg)  
(f)

![](images/9b827de2267310dfbc5b38b8cee30eb74158f8304c02dce6041f5a94fdfafa76.jpg)  
(g)

![](images/2c5b48b2c5c0c60e8f42bd3c69b15f05f43de3a60f50381ec402fe9909339522.jpg)  
(h)

![](images/5e987178c05d8b652ccc94c67fbaab04f836f28f29a2bdcadec6579f55dd2ccd.jpg)  
(i)   
Fig. 6. Simulation results for the two-area system under S1, S2, and S3. (a) Rotor angular frequency in S1. (b) Rotor angular frequency in S2. (c) Rotor angular frequency in S3. (d) Phase A current of the branch 7-8 for S1. (e) Zoomed-in view of (d). (f) Phase A current of the branch 7-8 for S2. (g) Zoomed-in view of (f). (h) Phase A current of the branch 7-8 for S3. (i) Zoomed-in view of (h).

![](images/90c96101ef12ba81879cd6702e135168e9917d18b5b8b407d823f41c754aacb2.jpg)

![](images/d38444765e57897a0f4e1d7477ab0768ad73947bd666b1abe803e08ae036dba9.jpg)

![](images/2623730573ce12391e2fc034cbef0471de2fe98f104f69b11841ab25afa89ab3.jpg)  
Synchronous generator   
IBR   
wv Transformer   
↓Load   
Fig. 7. A modified IEEE 39-bus System

# B. Test on the IEEE 39-bus System

The scalability of the proposed HMM approach is tested on a modified IEEE 39-bus system that has its penetration level of renewable energy reaching 50% by replacing four generators by IBRs as shown in Fig. 7. Simulate these two contingencies:

• S4: At t =0.1 s, a three-phase grounding fault is applied at bus 16 and then cleared after 5 cycles; at t =8 s, the load at bus 3 is disconnected and then reconnected after 5 cycles; the simulation ends at t =16 s.   
• S5: At t =0.1 s, generator SG4 at bus 34 is tripped permanently; the simulation ends at $t = 8 \mathrm { ~ s ~ }$ .

Use the same set of parameters in Table I. Here, the proposed defect control in micro-process is considered with a tolerance $\epsilon _ { 1 } = 1 0 ^ { - 2 }$ . The variable-step macro-process is enabled in this test. By varying T ol, the resulting speedup is given in Table II compared to a full EMT simulation using a 10µs step size RK method. Note that the micro-state from the HMM simulation results highly match the benchmark results, as observed from the small errors. Here the maximum error among all state variables is defined as the infinity norm $( \| \cdot \| _ { \infty } )$ of the difference between the results simulated by the HMM approach and the benchmark. This metric provides a strict measure of convergence and highlights the accuracy of the proposed approach across all state variables at every simulation step. For both S4 and S5, a large T ol allows a larger average macro time step and thus achieves a faster speed. The simulation results of S4 with $T o l = 1 0 ^ { - 2 }$ and S5 with $T o l = 1 0 ^ { - 2 }$ are shown in Fig. 8 and Fig. 9, respectively. For both contingencies, it is observed that the micro-dynamics become dominant when a fault occurs and immediately after it is cleared, and a large H adaptively rising to 0.04 s is achieved without causing any numerical instability seen from Fig. 8g and Fig. 9f. It demonstrates that the proposed approach adaptively adjusts the macro-step size based on real-time system dynamics, ensuring an appropriate resolution of simulation while maintaining computational efficiency. Thus, it is recommended that a microstate simulation, i.e., a full EMT simulation, is performed from the beginning of a fault until it is cleared in order to capture all fast EMT dynamics accurately under the fault. Then, when fast dynamics decay and slower dynamics become dominant, the HMM simulation may start to switch between the microstate simulation and macro-state simulation. The simulation is directly performed on the full EMT model without any explicit

model reduction. The time step 0.04 s is already in the range of time steps for transient stability simulations while EMT dynamics are still available with the micro-state results during the intervals of η.

TABLE II COMPUTATIONAL PERFORMANCE OF THE HMM METHOD   

<table><tr><td>Case</td><td>Tol</td><td>Execution Time(s)</td><td>Avg. Macro Step-size</td><td>Integral Error</td><td>Speedup</td></tr><tr><td rowspan="3">S4</td><td>10-2</td><td>91.9944</td><td>0.0248</td><td>3.4171 × 10-3</td><td>6.3766</td></tr><tr><td>7.5 × 10-3</td><td>93.7706</td><td>0.0235</td><td>1.5965 × 10-3</td><td>6.2558</td></tr><tr><td>2.5 × 10-3</td><td>110.5661</td><td>0.0149</td><td>9.9184 × 10-4</td><td>5.3055</td></tr><tr><td rowspan="3">S5</td><td>1 × 10-1</td><td>46.2250</td><td>0.0257</td><td>7.8574 × 10-3</td><td>6.5621</td></tr><tr><td>1 × 10-2</td><td>49.8745</td><td>0.0203</td><td>5.0552 × 10-4</td><td>6.0818</td></tr><tr><td>1 × 10-3</td><td>76.6401</td><td>0.0028</td><td>5.5834 × 10-5</td><td>3.9579</td></tr></table>

# C. Test on the Large-scale System

The performance of the HMM approach on the large-scale systems is further validated on a synthetic 390-bus system [30]. To compare with commercial software such as PSCAD, the proposed algorithm is translated from its MATLAB code into C code, and then compiled as an executable MEX file. The PSCAD codes used in this section are complied with GFortran 8.1 (64-bit) in PSCAD 5.0.2. A new contingency is simulated, named S6: $\mathbf { A } \mathbf { t } \ t = 0$ .1s a three-phase grounding fault is applied at bus 10 and then cleared after 0.2s, a 1 Hz forced oscillation happens due to the external three-phase current source injection $0 . 3 2 \sin ( 2 \pi t )$ [p.u.] (Phase A) at bus 30, and the simulation ends at $t = 8 \mathrm { s }$ . The HMM approach is compared with the nodal formulation-based approach [31] utilized in PSCAD and the RK45 method [32] utilized in Simulink. The simulation results are benchmarked with simulations using the nodal formulationbased approach utilized in PSCAD with a small step size $h = 1 ~ \mu \mathrm { s }$ . The time costs for the simulation and maximum normalized errors among all state variables are presented in Table III. Also, the phase-A voltage results at the grounding bus are shown in Fig 10 and Fig 11. The results in Table III highlight the advantages of the proposed HMM approach in terms of speed and accuracy, for a comparable error tolerance i.e., Max $\mathrm { E r r o r } = 8 . 2 9 \%$ , the HMM approach takes a CPU time of $1 7 6 . 5 9 \ \mathrm { s } ,$ whereas PSCAD requires 12725.77s using a $5 ~ \mu \mathrm { s }$ step size. This demonstrates that the HMM approach is approximately 70 times faster than PSCAD while achieving a similar accuracy level. Moreover, the RK45 diverges for a relaxed tolerance of $\mathrm { \ t o l = 1 0 ^ { - 1 } }$ , indicating numerical instability in the stiff simulation. For a tighter tolerance $\mathrm { ( t o l = 1 0 ^ { - 3 } ) }$ , RK45 has a maximum error of 43.60% but at a much higher computational cost of 5246.13 s. In comparison, the HMM approach has a significantly lower error and an almost 30 times speedup compared to RK45. Note that PSCAD’s time performance improves as the step size increases. However, this comes at the cost of accuracy, as larger step sizes $( h = 2 5 \mu s$ to $h = 1 0 0 \mu \mathrm { s } )$ result in progressively larger errors. This can be observed from transients shown in Fig. 10, only PSCAD with $h = 5 \mu s$ can match the benchmark in a good shape. The proposed HMM approach, however, utilizes a high-order approximation in the micro-process and provides accurate

![](images/3b29fd765c5b3f861e4759fc1e05bc77181af08048b7e233af8326d436e416ba.jpg)  
(a)

![](images/d0c809b57b2788e03fff726accf695d2a38c3a69f0b18c966b87a9f35b5e286b.jpg)  
(b)

![](images/22c8bd30138ba1f58db3950a72e092dc72782ec3e13593e3fb6f458e9e58bb30.jpg)  
(c)

![](images/fb67cf38028cda0860575751ecc9003754fb93cd6242a4646b60e9d56663b817.jpg)  
(d)

![](images/539dadad8c71edc44b51582ce0804360df6fee61b8f1cdc87a80f76ed25ae937.jpg)  
(e)

![](images/a10397170a1538e928b22fe6e301aae6ef48241018fdbcad119405b6d67fa9ce.jpg)  
(f)

![](images/971d818c87a7861d2b0c41b3f2f1d4c1d6383910ee6b5f7f75308a548e651f5b.jpg)  
(g)

![](images/68a8dfa3a57048822169d5dc357501fcd2dc97f350e75be36dfe0db44bc15fcf.jpg)  
(h)   
Fig. 8. Simulation results for S4. (a) Phase A current of the branch line 16-24. (b) Rotor angular frequencies. (c) Zoomed-in view of (a) near the fault. (d) Zoomed-in view of (a) near the generator tripping. (e) Zoomed-in view of (a) under oscillation. (e) Zoomed-in view of (a) under steady state. (g) Macro step size during the simulation. (h) Maximum errors among all state variables.

results for fast dynamics under large step sizes. Note that, if needed, detailed high-resolution micro-state dynamics can be reconstructed from the macro-process via the micro-solver. Also, the variable-step algorithm ensures that the step size of the macro-process is dynamically adjusted to maintain simulation accuracy. At the moment the fault happens, the step size of the macro-process becomes smaller to accommodate the need for higher resolution and accuracy, which is also shown in Fig. 11b.

![](images/338fc4dd663636c12c3324df2a8c7e8cf2c6a36c053ff8729724e7bc12036891.jpg)  
(a)

![](images/749d174484e2ec719ef965daf2cabf2be29685d072adc720f51213ab187d0f01.jpg)  
(b)

![](images/675c2dc46b082312a49a0b0d8c834394c4812158a7184dc69e5c8fb0347325e1.jpg)  
(c)

![](images/8f01ac2297672a35c03ee9dded0d87e210429e36be234f2667d2a3bda36fb590.jpg)  
(d)

![](images/6254f396bc0de61e17b007c74c7041ba8a006dd0cc96adef5c1ea0ca718a7d07.jpg)  
(e)

![](images/0e3e99c580d418ef28f244603e76abab48eb350728cb7117852b84980bf759eb.jpg)  
(f)

![](images/c03f8ee7317e8f82937a340b43a5c4a9e6a2947c4c4e61fe5d85beda30a5c6b9.jpg)  
(g)   
Fig. 9. Simulation results for S5. (a) Phase A current of the branch line 17-18. (b) Rotor angular frequencies. (c) Zoomed-in views of (a) near the fault. (d) Zoomed-in view of (a) under oscillation. (e) Zoomed-in view of (a) under steady-state. (f) Macro step size during the simulation. (g) Maximum errors among all state variables.

Then, the macro-step size gradually increases up to 0.04 s which can accurately simulate slow dynamics of the forced oscillation as shown in Fig.11a and Fig. 11c. The HMM approach achieves a balanced trade-off between computational speed and accuracy, outperforming traditional fixed-step methods, such as the nodal formulation method in PSCAD, and variable-step methods, such as the RK45 method in Simulink. The results demonstrate the superiority of the proposed HMM approach for accelerated,

accurate two-timescale power system simulations including both fast dynamics and slow dynamics.

TABLE IIICOMPUTATIONAL PERFORMANCE BY DIFFERENT METHODS FOR 390-BUSSYSTEM  

<table><tr><td>Approach</td><td>CPU Time(s)</td><td>Max Error(%)</td></tr><tr><td>HMM</td><td>176.59</td><td>0.0829</td></tr><tr><td>RK45 (tol = 10-1)</td><td>Diverged</td><td>Diverged</td></tr><tr><td>RK45 (tol = 10-3)</td><td>5246.133</td><td>0.4360</td></tr><tr><td>PSCAD (h = 5μs)</td><td>12725.77</td><td>0.0884</td></tr><tr><td>PSCAD (h = 25μs)</td><td>2701.64</td><td>0.7832</td></tr><tr><td>PSCAD (h = 50μs)</td><td>1354.55</td><td>1.4712</td></tr><tr><td>PSCAD (h = 75μs)</td><td>955.39</td><td>1.6350</td></tr><tr><td>PSCAD (h = 100μs)</td><td>649.97</td><td>1.4688</td></tr></table>

![](images/f7317d6388a534cf3b4a9eb0bd799a8c7b63a3a399f375ee1de5552736ab5aa0.jpg)  
(a)

![](images/fa11f8ad01418d78c707ba01e6731141ef2ced169cb2bc2ca53bcea5b5dfc453.jpg)  
(b)   
Fig. 10. Simulation results of Phase-A voltage at the grounding Bus for S6 after the fault. (a) results simulated by PSCAD using different step sizes. (b) results simulated by HMM.

# IV. CONCLUSION

This paper has proposed an HMM approach for efficient multi-timescale simulation of power systems with penetration of IBRs. On the EMT model of a power system, the HMM approach takes significantly enlarged time steps to evolve its macroscopic behavior for most of the simulation period when microscopic dynamics are either monotonic or predictable following a contingency. By leveraging a DT-based variablestep semi-analytical solver, the proposed HMM framework links detailed-level micro-state simulations over disconnected intervals via macro-state solutions to ensure numerical stability throughout the simulation, and it enables automatic zooming in and out between macroscopic and microscopic dynamics on the fly during the simulation. The proposed HHM framework is applicable to any dynamical system with an available ODE model. Thus, the proposed HHM approach may be extended and enhanced to simulate additional timescales in future power systems with integrated IBRs, addressing more detailed

![](images/2736146085dbfc6f7f9a29fd44ec4d07e29d218f07455af50054360f5e6fa759.jpg)

![](images/32314b8830c35655e200bb3ff8c27bba40d20d942320f4b1eeee474ad6b216be.jpg)  
Fig. 11. Simulation results for S6. (a) Phase A current of the branch line 1-2. (b) Macro step size during the simulation. (c) Zoomed-in views of (a). (d) Zoomed-in view of (a) near the steady state.

simulations of inverter switching cycles. Case studies have demonstrated that the proposed HMM approach can be directly applied to the full EMT model of a power system and can more efficiently capture accurate fast dynamics while skipping over less important EMT details to speed up the simulation.

# REFERENCES

[1] N. Hatziargyriou, J. Milanovic, C. Rahmann, V. Ajjarapu, C. Canizares, I. Erlich, D. Hill, I. Hiskens, I. Kamwa, B. Pal, P. Pourbeik, J. Sanchez-Gasca, A. Stankovic, T. Van Cutsem, V. Vittal, and C. Vournas, “Definition and classification of power system stability – revisited & extended,” IEEE Transactions on Power Systems, vol. 36, no. 4, pp. 3271–3281, 2021.   
[2] Q. Huang and V. Vittal, “Application of electromagnetic transient-transient stability hybrid simulation to fidvr study,” IEEE Transactions on Power Systems, vol. 31, no. 4, pp. 2634–2646, 2016.   
[3] ——, “Advanced EMT and phasor-domain hybrid simulation with simulation mode switching capability for transmission and distribution systems,” IEEE Transactions on Power Systems, vol. 33, no. 6, pp. 6298–6308, 2018.   
[4] V. Jalili-Marandi, V. Dinavahi, K. Strunz, J. A. Martinez, and A. Ramirez, “Interfacing techniques for transient stability and electromagnetic transient programs IEEE Task Force on interfacing techniques for simulation tools,” IEEE Transactions on Power Delivery, vol. 24, no. 4, pp. 2385–2395, 2009.   
[5] X. Lin, A. M. Gole, and M. Yu, “A wide-band multi-port system equivalent for real-time digital power system simulators,” IEEE Transactions on Power Systems, vol. 24, no. 1, pp. 237–249, 2009.   
[6] Y. Zhang, A. M. Gole, W. Wu, B. Zhang, and H. Sun, “Development and analysis of applicability of a hybrid transient simulation platform combining TSA and EMT elements,” IEEE Transactions on Power Systems, vol. 28, no. 1, pp. 357–366, 2013.   
[7] K. Strunz, R. Shintaku, and F. Gao, “Frequency-adaptive network modeling for integrative simulation of natural and envelope waveforms in power systems and circuits,” IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 53, no. 12, pp. 2788–2803, 2006.   
[8] B. Engquist and Y.-H. R. Tsai, “Heterogeneous multiscale methods for stiff ordinary differential equations,” Math. Comput., vol. 74, pp. 1707–1742, 2005.   
[9] G. Ariel, B. Engquist, and R. Tsai, “A multiscale method for highly oscillatory ordinary differential equations with resonance,” Math. Comput., vol. 78, pp. 929–956, 2008.

[10] W. Ren and W. E, “Heterogeneous multiscale method for the modeling of complex fluids and micro-fluidics,” Journal of Computational Physics, vol. 204, no. 1, pp. 1–26, 2005. [Online]. Available: https://www.sciencedirect.com/science/article/pii/S0021999104004048   
[11] W. E, B. Engquist, X. Li, W. Ren, and E. Vanden-Eijnden, “Heterogeneous multiscale methods: A review,” Communications in Computational Physics, vol. 2, no. 3, pp. 367–450, Jun. 2007.   
[12] K. Huang, M. Xiong, Y. Liu, K. Sun, and F. Qiu, “A heterogeneous multiscale method for power system simulation considering electromagnetic transients,” in 2023 IEEE Power & Energy Society General Meeting (PESGM), 2023, pp. 1–5.   
[13] L. Wang and J. Jatskevich, “A voltage-behind-reactance synchronous machine model for the EMTP-type solution,” IEEE Transactions on Power Systems, vol. 21, no. 4, pp. 1539–1549, 2006.   
[14] G. Kou, P. Markham, S. Hadley, T. King, and Y. Liu, “Impact of governor deadband on frequency response of the U.S. Eastern Interconnection,” IEEE Transactions on Smart Grid, vol. 7, no. 3, pp. 1368–1377, 2016.   
[15] “IEEE recommended practice for excitation system models for power system stability studies,” IEEE Std 421.5-2016 (Revision of IEEE Std 421.5-2005), pp. 1–207, 2016.   
[16] B. She, F. Li, H. Cui, J. Zhang, and R. Bo, “Fusion of microgrid control with model-free reinforcement learning: Review and vision,” IEEE Transactions on Smart Grid, vol. 14, no. 4, pp. 3232–3245, 2023.   
[17] O. Ajala, N. Baeckeland, B. Johnson, S. Dhople, and A. Dom´ınguez-Garc´ıa, “Model reduction and dynamic aggregation of grid-forming inverter networks,” IEEE Transactions on Power Systems, vol. 38, no. 6, pp. 5475–5490, 2023.   
[18] F. Dorfler, J. W. Simpson-Porco, and F. Bullo, “Electrical networks and¨ algebraic graph theory: models, properties, and applications,” Proceedings of the IEEE, vol. 106, no. 5, pp. 977–1005, 2018.   
[19] Y. Liu, K. Sun, R. Yao, and B. Wang, “Power system time domain simulation using a differential transformation method,” IEEE Transactions on Power Systems, vol. 34, no. 5, pp. 3739–3748, 2019.   
[20] F. Milano, “The frenet frame as a generalization of the park transform,” IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 70, no. 2, pp. 966–976, 2023.   
[21] Y. Liu and K. Sun, “Solving power system differential algebraic equations using differential transformation,” IEEE Transactions on Power Systems, vol. 35, no. 3, pp. 2289–2299, 2019.   
[22] W. Enright, “Continuous numerical methods for ODEs with defect control,” Journal of Computational and Applied Mathematics, vol. 125, no. 1, pp. 159–170, 2000, numerical Analysis 2000. Vol. VI: Ordinary Differential Equations and Integral Equations.   
[23] K. Huang, Y. Liu, K. Sun, and F. Qiu, “Pi-controlled variable timestep power system simulation using an adaptive order differential transformation method,” IEEE Transactions on Power Systems, pp. 1–13, 2024.   
[24] A. Semlyen and F. de Leon, “Computation of electromagnetic transients using dual or multiple time steps,” IEEE Transactions on Power Systems, vol. 8, no. 3, pp. 1274–1281, 1993.   
[25] P. Mattavelli, G. Verghese, and A. Stankovic, “Phasor dynamics of thyristor-controlled series capacitor systems,” IEEE Transactions on Power Systems, vol. 12, no. 3, pp. 1259–1267, 1997.   
[26] D. Shu, X. Xie, Q. Jiang, G. Guo, and K. Wang, “A multirate emt cosimulation of large ac and mmc-based mtdc systems,” IEEE Transactions on Power Systems, vol. 33, no. 2, pp. 1252–1263, 2018.   
[27] Y. Li, D. Shu, F. Shi, Z. Yan, Y. Zhu, and N. Tai, “A multi-rate cosimulation of combined phasor-domain and time-domain models for largescale wind farms,” IEEE Transactions on Energy Conversion, vol. 35, no. 1, pp. 324–335, 2020.   
[28] H. Zhao, A. Sinkar, A. M. Gole, and Y. Zhang, “Accuracy quantification of multi-rate electromagnetic transients simulation,” IEEE Transactions on Power Delivery, vol. 39, no. 2, pp. 1051–1062, 2024.   
[29] S. Fan and H. Ding, “Time domain transformation method for accelerating emtp simulation of power system dynamics,” IEEE Transactions on Power Systems, vol. 27, no. 4, pp. 1778–1787, 2012.   
[30] M. Xiong, K. Huang, Y. Liu, R. Yao, K. Sun, and F. Qiu, “A semianalytical approach for state-space electromagnetic transient simulation using the differential transformation,” arXiv preprint arXiv:2312.12611, 2023.   
[31] H. W. Dommel, “Digital computer solution of electromagnetic transients in single-and multiphase networks,” IEEE Transactions on Power Apparatus and Systems, vol. PAS-88, no. 4, pp. 388–399, 1969.   
[32] J. R. Dormand and P. J. Prince, “A family of embedded runge-kutta formulae,” Journal of computational and applied mathematics, vol. 6, no. 1, pp. 19–26, 1980.

![](images/15cb7ba00ddc85e004cdc8677990cbcfdbf4fb3616655a870fcb5cd7be2e953e.jpg)

Kaiyang Huang (Graduate Student Member, IEEE) received the B.S. degree in electrical engineering from North China Electric Power University, China, in 2020. He is currently pursuing the Ph.D. degree at the Department of Electrical Engineering and Computer Science, University of Tennessee, Knoxville, USA. His research interests include power system simulation, transient stability analysis, and dynamics.

![](images/9f0558c126b7199e29e34f77a2f5c4fdb6d7f67c2c205c193ff2bc747cd92d73.jpg)

Min Xiong (Member, IEEE) received the B.S. and M.S. degrees from Wuhan University, Wuhan, China, in 2013 and 2016, respectively, and the Ph.D. degree from the University of Tennessee, Knoxville, TN, USA, in 2023, all in electrical engineering. He was an engineer with State Grid Hubei Power Company from 2016 to 2019. He is now a postdoctoral researcher at the Power Systems Engineering Center, National Renewable Energy Laboratory, Golden, CO, USA. His research interests include electrical parameter measurement, relay protection, power system stability

analysis, electromagnetic transient simulation, and integration of renewable resources.

![](images/cbd71d8fc54322dc726a24d7f2524113c803171cda8e09cd45a1ef9615c85312.jpg)

Yang Liu (Member, IEEE) is currently a principal engineer at Quanta Technology LLC. He received his B.S. degree in energy and power engineering from Xi’an Jiaotong University, China, in 2013, his M.S. degree in power engineering from Tsinghua University, China, in 2016, and his Ph.D. degree in electrical engineering from the University of Tennessee, Knoxville, USA, in 2021. He was a Post-Doctoral Researcher at the University of Tennessee in 2022 and at Argonne National Laboratory in 2023. His research interests include power system

simulation, dynamics, stability, and control.

![](images/3263e4c681747dd669bbb2b0e3d46ac1d936c45c88b7791fef67d2568e2d9e2b.jpg)

Kai Sun (Fellow, IEEE) is a professor in the Department of Electrical Engineering and Computer Science at the University of Tennessee, Knoxville, USA. He received his B.S. degree in Automation in 1999 and his Ph.D. degree in Control Science and Engineering in 2004, both from Tsinghua University, Beijing, China. From 2007 to 2012, he served as a Project Manager in grid operations, planning, and renewable integration at the Electric Power Research Institute (EPRI), Palo Alto, CA.