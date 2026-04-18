# Modeling and application of DQ-sequence dynamic phasors under unbalanced AC conditions

Xiaoming Mao $^{a,*}$, Hongbo Luo $^{a}$, Wenda Zhong $^{a}$, Liang Wu $^{b}$, Zhiyong Yuan $^{c}$

$^{a}$ School of Automation, Guangdong University of Technology, Guangzhou, China
$^{b}$ Power Dispatching and Control Center of the China Southern Power Grid Company, Guangzhou, China
$^{c}$ Electric Power Research Institute of the China Southern Power Grid Company, Guangzhou, China

**Keywords:** Dynamic phasor, DQ-sequence dynamic phasor, MMC, Modeling

**Abstract:** Increasing unbalanced AC operating conditions generates the need of developing models for power electronic equipment in such situations. The dq-sequence dynamic phasor method is proposed in this paper to model power electronic devices controlled in dq-rotating coordinates. Firstly, the instantaneous symmetric component decomposition and Park transformation are sequentially performed on a set of three-phase time-domain signals to define the dq-sequence dynamic phasors. Then, the multiplication property is derived. Next, the general steps for forming the state equations are provided, and the specific expressions of the state matrices are derived. Furthermore, a method is provided for quickly separating the real and imaginary parts of the complex-form state equations, as well as obtaining their simplest real-form. Case study on a two-terminal Modular Multilevel Converter − High Voltage Direct Current system verifies the effectiveness of the proposed modeling method. And the developed state space model is compared with existing similar models to show its advantages.

## 1. Introduction

With the widespread application of power electronic devices, electromagnetic transient (EMT) simulation with small time steps becomes an important means of studying the operational characteristics of power systems [1,2]. Due to the challenges of complicated models, heavy computational burden, and slow simulation speed faced by large-scale EMT simulations, it is necessary to develop more efficient simulation models and algorithms. In this regard, the dynamic phasor (DP) method provides a feasible and efficient solution.

DP refers to the time-varying Fourier coefficient of a time-domain signal based on Fourier decomposition. It breaks through the limitation of quasi-steady assumption, and has larger frequency bandwidth than conventional phasors. DP method selects the dominant frequency components for modeling and its simulation speed and accuracy are between the electromagnetic and electromechanical transient simulations.

When studying the dynamics of a power system, detailed internal dynamics of power electronic devices are generally not the focus, using DP simulation with a lower computational cost is generally more advantageous. Currently, the DP method has been widely used in modeling of power electronic equipment under symmetric operating conditions, such as in [3] with Static Var Compensator (SVC), in [4] with Line Commutated Converter (LCC), in [5] with Modular Multilevel Converter (MMC), and in [6] with LCC-MMC, all for simulation purposes. The above studies show that the DP can reflect not only the external operation characteristics, but also their internal dynamics to some extent.

DP is also used in small-signal stability study based on eigenvalue analysis [7]. Note that the fast on–off and complicated harmonic behavior of power electronic equipment, such as MMC, makes it difficult to get the DC operation point which is required by traditional linearization methods. Considering that these devices typically use vector control based on the dq rotating coordinate system, the researchers select main frequency components and convert the AC system model to the dq rotating coordinate system for interface with the control systems and then linearize it [8–12]. The models in [8–12] can be classified under the DP model category and explanations are provided in Part 3.4 of this article.

As aforementioned, the DP method has been applied in both simulations and small-signal stability analysis, and existing work mainly focuses on AC balanced systems. However, asymmetric faults are more common in utility grid disturbances [13]. To cope with imbalanced conditions, two DP modeling methods have been proposed, namely the three-phase and the sequence DP (SDP) modeling.

The three-phase DP modeling method is proposed in [14]. It defines the average value of the k-phasor in the three-phase time-domain signal within the frequency cycle as the corresponding k-DP and derives the differentiation property. Based on this method, [14] builds DP models for transmission lines et al, and [15] models the LCC-HVDC system.

The SDP modeling method [16,17] uses k-phasor in sequence time-domain signals to form the DPs and derives the differentiation and conjugation properties. However, the multiplication property that is more critical for modeling is not provided. Based on this method, state space model under unbalanced AC conditions in Section 6. Section 7 concludes the paper.

## 2. Review on the dynamic phasor theory

### 2.1. Single-phase dynamic phasor

A time-domain signal $x(\tau)$ can be represented on the interval $\tau \in (t - T, t]$ in the form of Fourier series given in (1) [22].
$$x(\tau) = \sum_{k=-\infty}^{\infty} X_k(t) e^{jk\omega\tau}$$