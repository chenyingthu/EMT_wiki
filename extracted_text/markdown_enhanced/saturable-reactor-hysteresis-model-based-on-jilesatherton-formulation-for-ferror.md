# Saturable reactor hysteresis model based on Jiles–Atherton formulation for ferroresonance studies

Wenxia Sima$^a$, Mi Zou$^{a,b}$, Ming Yang$^{a,c,*}$, Daixiao Peng$^a$, Yonglai Liu$^a$

$^a$ State Key Laboratory of Power Transmission Equipment & System Security and New Technology, Chongqing University, Chongqing 400044, China
$^b$ Centre for Applied Power Electronics, Department of Electrical & Computer Engineering, University of Toronto, Toronto, ON M5S 3G4, Canada
$^c$ Department of Electrical and Computer Engineering, Tandon School of Engineering, New York University, Brooklyn, NY 11201, USA

* Corresponding author at: State Key Laboratory of Power Transmission Equipment & System Security and New Technology, Chongqing University, Chongqing 400044, China.
E-mail address: cqucee@cqu.edu.cn (M. Yang).

**Keywords:** Jiles–Atherton model, Reactor, Ferroresonance, Electromagnetic transients

**Abstract:** Despite remarkable achievements in the field of Jiles–Atherton (JA) hysteresis theory, JA hysteresis modeling remains challenging given that most commercial software still lacks a practical dynamic JA hysteresis reactor model for electromagnetic transients. A novel voltage-driven dynamic flux linkage–current ($\psi$–$i$) JA hysteresis reactor in Electromagnetic Transients Program–Alternative Transients Program (EMTP–ATP) is developed in this study. The proposed model is based on flux linkage and current instead of magnetic flux density and magnetic field. Voltage-driven dynamic losses are incorporated into the static $\psi$–$i$ JA hysteresis model by using Type-94 element in EMTP–ATP. The two proposed models in this paper are validated using current tests under 50 and 150 Hz. The performance of the proposed dynamic Model 1 matches better with experiments than the dynamic Model 2. Ferroresonance tests are carried out to validate the performance of the proposed reactor. The results show that the proposed reactor has a broad application prospect in electromagnetic transient studies.

## 1. Introduction

Ferroresonance is one of the most common low-frequency electromagnetic transients (EMTs) [1–4]. The occurrence of ferroresonance requires a nonlinear inductance (the saturable iron core of the transformer or the reactor), a capacitance, low power loss condition and a voltage source [5–7]. Because of the modeling complexity and computational burden associated with hysteresis nonlinearities, a simple mathematical expression (e.g., piecewise-linear, exponential and polynomial) is widely used to represent the nonlinear characteristic of the transformer core in most ferroresonance studies [5,8–10]. With the development of transformer design, the width of the transformer iron core hysteresis loop has narrowed significantly. The hysteresis loop approximates to the anhysteretic loop. Thus, the single-valued magnetization characteristics are acceptable for the steady-state power quality studies such as harmonic power flow [11].

However, the anhysteretic approximation has been proven to be inadequate for the study of dynamic, transient and nonsinusoidal power system studies. The operating points of the system are significantly affected by the dynamic excitation of a nonlinear hysteretic core. Thus, the modeling of major and minor hysteresis loop trajectories becomes very important in these studies. For ferroresonance study, the accurate modeling of hysteresis loops is especially significant because the major and minor loops can potentially generate more ferroresonant operating points [6].

Another aspect of hysteresis phenomenon in the analysis of ferroresonance is the inadequate representation of core loss. In most of the existing studies, the core loss is commonly described by a constant resistance or nonlinear resistance [6]. However, the constant or nonlinear resistance cannot accurately represent the core loss because the core loss in the transformer should dynamically decrease as the core excitation level increases [6]. Thus, ferroresonance simulation still remains a challenge due to the accurate modeling of the hysteresis reactor [12–17].

Among the existing literature of hysteresis models, the Stoner–Wolhfarth model, the Jiles–Atherton (JA) model, the Globus model, and the Preisach model are widely reported [18–20]. These models use different theoretical assumptions, so their performance and applicability are also different. The JA model is proved to be best suited to the bulk material and medium ferrites [18]. Besides, the identification of the parameters of JA model requires relatively fewer measurements [19], and the accuracy of this model in EMT simulation has been widely verified [21–27]. Therefore, in this paper, the JA hysteresis model is used to ferroresonance simulation.

Mutual magnetic interaction and domain wall motion are considered in the JA hysteresis model, which also provides mathematical formulas to explain the hysteresis of magnetization $M$ against magnetic field $H$ on the assumption of uniformly impeded domain wall motion [21–23]. The original magnetic flux density and magnetic field ($B$–$H$) expressions are used in the majority of the existing applications of the JA model for EMT simulation [24–27].

weighting factor, and $\delta$ is a directional parameter and takes the value $+1$ for $dH/dt > 0$ and $-1$ for $dH/dt < 0$.

In [22], this differential equation is defined as
$$ \frac{dM}{dH} = (1-c) \frac{M_{an} - M_{irr}}{k\delta - \alpha(M_{an} - M_{irr})} + c \frac{dM_{an}}{dH} $$