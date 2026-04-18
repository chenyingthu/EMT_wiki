# Time-delay estimation through all-pass functions for ULM line and cable models

S. Loaiza-Elejalde$^{a,\dagger,*}$, J.L. Naredo$^a$, Martin G. Vega-Grijalva$^b$, O. Ramos-Leaños$^c$, E.S. Bañuelos-Cabral$^d$

$^a$ Cinvestav-Guadalajara, Mexico  
$^b$ Intel Corporation, Guadalajara, Mexico  
$^c$ IREQ, Varennes, PQ, Canada  
$^d$ University of Guadalajara, Mexico  

**Keywords:** All-pass filters, Electromagnetic transients, Line modeling, Minimum phase, Rational fitting, Time delays, Traveling waves

**Abstract:** Traveling-wave line models, such as the ULM, are widely used in time-domain EMT simulations for power systems. These models require the rational approximation of both the characteristic admittance matrix $Y_c$, and the propagation matrix $H$. Rational fitting of $H$ is challenging due to the inclusion of a mix of modal delays in all its elements. These delays must therefore be identified and extracted before proceeding to calculate the rational approximation. This paper proposes a new iterative method to estimate time delays employing all-pass filters and delay equalizations. Unlike other currently used methods, the one proposed here ensures causality and minimum-phase features in the synthesized $H$ model. Three test cases are included: 1) a synthetic transfer function, 2) a system of underground cables, and 3) the EMT response of an aerial line. The obtained results show that the proposed method maintains causality while achieving similar accuracies with fewer iterations compared to a state-of the art method based on rms-error minimization.

* Corresponding author. E-mail address: sebastian.loaiza@cinvestav.mx (S. Loaiza-Elejalde).  
† S. Loaiza gratefully acknowledges financial support from Cinvestav.  
Paper submitted to the International Conference on Power Systems Transients (IPST2025) in Guadalajara, Mexico, June 8-12, 2025.

## 1. Introduction

PHASE-DOMAIN line models, such as the Universal Line Model (ULM) [1], are widely used in the time-domain (TD) simulation of electromagnetic transients (EMT) in power systems. For each transmission line or cable under study, these models require that the associated matrices, $Y_c$ of characteristic admittances and $H$ of propagation factors, be approximated by rational expressions leading to computationally efficient TD simulations. While rational fit of $Y_c$ is straightforward, the fitting of $H$ presents difficulties due to its elements involving delay factors associated with the modal velocities of the line or cable. Modal delays must therefore be identified and extracted from matrix $H$ for a proper rational fit. Vector Fitting (VF) is the adopted methodology for rational fittings in the ULM [2]. As an alternative, $H$ can be adjusted rationally without prior knowledge of modal delays by means of the Bode-diagram method developed for the FDLine model in [3]; nevertheless, the rational approximations so obtained tend to be of much higher orders than those from VF.

To enable the application of VF to the fitting of $H$, Gustavsen and Semlyen introduced in 1998 a method to estimate modal delays [4]. This method is based on an integral by Bode that relates the minimum phase angle response of the modal propagation functions $H_m$ to its magnitude response [5]. These authors proposed obtaining a representative time delay for the entire function $H_m$ by evaluating Bode integral at a single cutoff frequency $\Omega$ at which the magnitude of $H_m$ decays to 0.1. However, it was found later that this may not work well in certain cases and modifications in the cutoff frequency evaluation have been proposed [6, 7]. Nevertheless, the issue of determining a proper value for $\Omega$ has remained open. Additionally, the magnitude of $H_m$ may not decay to the required value within the frequency range of analysis.

To overcome the previous limitations, it has been proposed to first obtain an approximation of the delay, possibly using the Bode integral method, and then to conduct a search around it for a better value of the delay. The criterion for comparing time delay estimates is the rms-error of the synthesized function. Initially, a half-range search algorithm was employed [8] and, later, methods based on Golden Section search (GS) were adopted [7–9]. One issue with minimum rms-error methods is that they do not always guarantee the minimum error in the TD transient responses as it is demonstrated in [10,11]. Another problem with these methods is that the delay producing the minimum rms-error can lead

Fig. 1. Traveling waves model of an aerial transmission line.

function for the $i$th mode [14]. $H_{m,i}$ is given in terms of its modal attenuation $\alpha_i$ and modal phase $\beta_i$:

$$H_{m,i} = e^{-(\alpha_i + j\beta_i)l}, \quad (3)$$

with $l$ being the length of the line. The phase-shift term $\beta_i$ can be separated into two components: one corresponding to the minimum phase and the other related to the modal delay, which can be obtained from the modal velocity [4]. Then, (3) can be rewritten as

$$H_{m,i} = e^{-(\alpha_i + j\beta_{\min,i})l} e^{-j\omega\tau_i}; \quad (4)$$

where the $i$th modal delay $\tau_i$ has been factored out from $H_{m,i}$. Afterwards, the substitution of (4) in (2) produces an expression where each mode is expressed as the product of a minimum phase function and a pure delay function: