# Passivity enforcement of wideband model through a new and full perturbation formulation

Juan Miguel David Becerra $^a$, Ilhan Kocar $^{b,*}$, Jean Mahseredjian $^a$  
$^a$ Polytechnique Montreal, Canada  
$^b$ Department of Electrical Engineering, The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong  

* Corresponding author.  
E-mail address: ilhan.kocar@polyu.edu.hk (I. Kocar).

**Keywords:** Electromagnetic transients, Passivity, Transmission-line model

**Abstract:** Passive component models are necessary to ensure numerical stability in the simulation of electromagnetic transients in power systems. However, it is challenging to represent transmission lines and cables with frequency-dependent wideband models that are accurate, efficient, and passive. This paper proposes a new method for the passivity enforcement of wideband line and cable models. The wideband models rely on pole-residue identification of characteristic admittance and propagation function in rational forms. In case the resulting models are not passive, the proposed method simultaneously applies perturbation to the residue matrices of characteristic admittance and propagation function. The set of equations related to passivity enforcement through the residues of propagation function in phase domain is complex and presented for the first time in this paper. The proposed approach minimizes the overall perturbation for maintaining passivity as opposed to the existing simplified approaches that rely on the perturbation of the residues of either characteristic admittance or diagonal elements of propagation function. The performance of the method is validated with application cases, and it is shown that it outperforms the existing methods that seek simplification in problem formulation.

## 1. Introduction

Transient simulators are commonly used in power systems to assess switching and lightning-induced overvoltages, precise short-circuit currents, harmonics, and resonance conditions [1]. In these studies, wideband models that consider the frequency dependence of electrical parameters are needed for higher accuracy. Other than integration and interpolation errors, non-passivity of wideband models may also lead to numerically unstable simulations in the time domain [2–5]. Thus, ensuring passivity will facilitate troubleshooting of an unstable time-domain simulation.

To accelerate time-domain simulations, wideband line/cable models including Universal Line Model (ULM) [6,7], and Frequency Dependent Cable Model (FDCM) [4], rely on the rational fitting of the propagation function and characteristic admittance matrices (also known as line/cable functions). However, fitting processes performed in the complex domain such as vector fitting or the recently proposed more efficient algorithms [8,9] do not guarantee passive models. A model is deemed passive if its line admittance matrix is positive real. It is also known that passivity violations might stem from theoretical assumptions made to compute the line/cable parameters [10].

Passivity is usually enforced with perturbations [11–15], in case of wideband line/cable models through perturbation of residues of the rationally fitted line/cable functions. This perturbation should still preserve the accuracy of the fitted model. However, the enforcement of passivity in wideband line/cable models is not straightforward because the line admittance matrix is a complex function of the propagation function and characteristic admittance. The difficulty arises often because of the fitting of the propagation function since it is a multi-delay matrix function. The characteristic admittance itself is a passive function and its fitting is less stringent. The current methods try to enforce passivity through residue perturbation of either the fitted characteristic admittance or the diagonal elements of the fitted propagation function, but not simultaneously [5,11]. Although the passivity problem is often associated with the fitting of propagation function, perturbation of the residues of the fitted characteristic admittance as suggested in [11] is also reported to enforce passivity in some cases. Although this approach gives the impression to be disconnected from the root cause of the passivity problem, it can be justified given the fact that the reconstructed nodal admittance function of a line or cable is a function of its characteristic admittance.

Another weakness of the existing passivity enforcement techniques is the perturbation of the diagonal elements of the fitted propagation function and lack of a complete passivity enforcement scheme in full phase domain. The procedure of passivity enforcement with the perturbation of characteristic admittance residues does not apply to the propagation function because the relation between the nodal admittance and the propagation function is non-linear.

In this paper, a new passivity enforcement method is proposed, which is based on the simultaneous perturbation of the characteristic admittance and propagation function in full phase domain. Its mathematic

## 3. Passivity enforcement through mixed perturbation

### 3.1. General definition

In case a wideband model does not satisfy (1), one can enforce passivity by altering parameters of its corresponding $Y_C$ or $H_I$. Usually, only residue matrices of $Y_C$ or $H_I$ are perturbed. Furthermore, as a common practice, one desires to perturb as little as possible in order to preserve the accuracy of the fitted model. Hence, passivity enforcement