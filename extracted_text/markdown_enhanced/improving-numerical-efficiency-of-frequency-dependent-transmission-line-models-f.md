# Improving numerical efficiency of frequency dependent transmission line models for EMT simulations
H.M.Jeewantha De Silva *, Yi Zhang
RTDS Technologies Inc., Winnipeg, MB, Canada

**Keywords:** Frequency dependent transmission line model, Modal Truncation, Balanced Truncation, Underground cables

**Abstract:** This paper compares two model order reduction techniques for frequency dependent transmission line models to enhance numerical performance for large cable or overhead line systems. The Modal Truncation and Balanced Truncation methods are applied to reduce the order of propagation matrix. The simulation examples involving underground cable systems are presented for comparison. Time domain simulation results with linear terminations are presented.

## 1. Introduction
THE frequency dependent transmission line models are widely used in electromagnetic transient studies. In these models, frequency dependent characteristics, such as propagation ($A(\omega)$) or characteristic admittance ($Y_c(\omega)$) functions, are approximated using rational functions in the frequency domain [1]. Techniques such as Vector-Fitting can be used to obtain such approximations [2,1]. The order of the rational function is determined such that the approximation error is below a specified tolerance.

Typically, the $A(\omega)$ and $Y_c(\omega)$ functions can be approximated using low order rational functions. The optimal order of approximation for a frequency-dependent function is influenced by its characteristics and desired accuracy. However, in some cases, the order of the $A(\omega)$ function can be significantly high, particularly for complex cable systems, which necessitates significant computational effort.

In popular frequency dependent wideband models, such as the Universal Line Model, the rational function approximation (curve-fitting) is accomplished in two steps. First, the modal elements of the $A(\omega)$ matrix ($A_{\text{modes}}(\omega)$) are independently curve-fitted using a common error tolerance [1]. Next, the elements of the phase $A(\omega)$ matrix are approximated with a common set of poles (i.e. poles of $A_{\text{modes}}(\omega)$ with corresponding modal delays). This process is iterated until the desired accuracy of the phase function is achieved. For some cable systems, since a common error tolerance is used to approximate $A_{\text{modes}}(\omega)$, some modes may be overfitted with a higher-order than necessary resulting in a higher-order phase $A(\omega)$ function.

A higher-order function requires greater computational resources and memory in time domain simulations (i.e. to evaluate recursive convolution algorithm) and more critically, is prone to passivity violations arising from over-fitting [3–6].

Wide-area modeling of power systems is a growing trend in countries such as Australia, UK, and US. One major problem is that the detailed EMT wide-area modeling can significantly slow down simulations. The offshore wind farms connect to onshore grid or substation via underground cables. The multi-circuit cable systems in close proximity are modelled as mutually coupled cables in EMT simulations to accurately consider the mutual coupling between them.

The computational complexity associated with large transmission line systems, such as multi-circuit cable systems, can significantly degrade simulation performance. This is especially critical in real time simulations, which can also lead to time step overshoot.

This paper compares two methods to enhance the numerical efficiency of the transmission line models by reducing the order of the $A(\omega)$ function for multi-circuit cable systems. Model order reduction techniques (MOR) can be used to obtain reduced-order systems while ensuring a small approximation error. Some techniques offer additional benefits, such as numerical efficiency, the presence of a priori error bounds, and ensuring properties like stability and passivity. Modal order reduction is a well-studied subject and applied in many application areas, including modelling of semiconductor devices and MIMO macro-models of high-speed VLSI interconnects, etc. MOR methods can be classified into two main classes: Krylov-based methods and truncation-based methods [7–9]. The popular truncation-based methods are Modal Truncation (MT) and Balanced Truncation (BT).

The BT reduction was first introduced by Mullis and Roberts (1976) [10] and later in the systems and control literature by Moore (1981) [11]. In 1984, the Hankel-norm reduction technique was introduced by Glover [12]. The BT method is based on the solution of the Lyapunov equation of the dynamic system. The solutions are the reachability and the observability gramians. The basis is that the states that are difficult to reach are simultaneously difficult to observe. Then, the reduced model is obtained by truncating the states that have this property.

In the MT method, the state-space system is truncated by eliminating non-dominant eigenvalues after reordering them based on the magnitude of the eigenvalues of the system matrix A.

The first method related to Krylov subspaces was introduced in 1990. Some of the popular Krylov-based methods include Asymptotic Waveform Evaluation, the Padé Via Lanczos Method (PVL), the Arnoldi

### 3.1. Modal truncation (MT)
This is one of the oldest MOR techniques. In general, the MT is based on projecting the state space system on the subspace of the pencil $\lambda I - A$ for some subset of eigenvalues [7–9].

The reduced order system is obtained by eliminating the non-dominant eigenvalues (eigenvalues with smallest real part). In case of rational functions expressed as residue pole form, for some small enough tolerance (tol), the reduced order system represents the condition,

$$ \frac{\| c_k \|}{|a_k|} > \text{tol} \tag{5} $$