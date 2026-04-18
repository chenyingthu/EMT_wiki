# Passivity enforcement of wideband line model through coupled perturbation of residues and poles

Juan Becerra, Ilhan Kocar, Keyhan Sheshyekani, Jean Mahseredjian  
*Department of Electrical Engineering, Ecole Polytechnique de Montreal, Montreal, Canada*

*Corresponding author.*  
*E-mail addresses: juanmigueldavid@gmail.com (J. Becerra), ilhan.kocar@polymtl.ca (I. Kocar), keyhan.sheshyekani@polymtl.ca (K. Sheshyekani), jean.mahseredjian@polymtl.ca (J. Mahseredjian).*

**Keywords:** Electromagnetic transients, Passivity, Transmission-line model, Wideband line model

**Abstract:** Ensuring stability in transient simulations of power systems requires that intrinsically passive components of the network should be represented with passive models, including transmission lines and cables. Existing research on passivity enforcement of the wideband line or cable model is based on the perturbation of residues of the state-space model of the characteristic admittance, ignoring its poles and its constant term. This paper presents the advantages and limitations of including the poles and constant matrix of the characteristic admittance in the passivity enforcement method of wideband models.

## 1. Introduction

The passivity of wideband models of transmission lines and cables is crucial to ensure numerically stable electromagnetic transient simulation of power systems [1]. Wideband models, such as Universal Line Model (ULM) [2,3], and Frequency-Dependent Cable Model (FDCM) [4], provide efficient simulations in time domain due to the use of rational functions for representing characteristic admittance and propagation matrix. However, it is well known that rational fitting algorithms do not guarantee passive models [5], where a model is deemed passive if its line admittance matrix is positive real.

For non-passive wideband models, one commonly enforces passivity by perturbing the matrix of residues of the propagation matrix. In turn, this perturbation causes a deviation in the frequency response of the model (line admittance matrix), which must be minimized to preserve the accuracy of the model. Previous works minimize the deviation in the characteristic admittance since it is more straightforward implementation-wise than minimizing the line admittance, and it yields good results [5–7]. Other works add an external correction term [8,9], or perturb the residue matrices of the propagation matrix [5] to enforce passivity.

Note that previous works do not consider the perturbation of the poles and the constant term of the characteristic admittance. This trend is likely caused by the easiness of formulating the induced deviation as a function of the controllability Grammian, which is only possible for perturbation of the matrices of residues. An argument in favor of this trend is that much work is invested in finding the natural frequencies of any system (poles), and hence, they should be left intact [1]. Nonetheless, this argument does not hold for the constant term and overlooks that passivity is a function of all components of a given model. Consequently, this paper explores and presents the advantages and limitations of perturbing all elements of the characteristic admittance. Besides, the induced deviation is suitably defined in terms of the relative error and Frobenius distance between systems for accuracy preservation.

The paper is organized as follows: Section 2 presents a summary of the passivity of wideband models; Section 3 explains the passivity enforcement of wideband models by perturbing all components of the characteristic admittance; Section 4 shows three application examples and compares its results; Finally, Section 5 presents the conclusions.

## 2. Passivity of wideband models

The passivity of a system represented by its admittance $Y_n(s)$ can be assessed with the positive realness condition, stated as [1,10–12]:

$$\lambda_i(\Theta(Y_n(s))) \ge 0; \quad s = j\omega \tag{1}$$

with $\lambda(\cdot)$ being the eigenvalue function and $\Theta(Y_n(s))$ is given by:

$$\Theta(Y_n(s)) = Y_n(s) + Y_n^H(s) \tag{2}$$

where $Y_n^H(s)$ stands for the Hermitian of $Y_n(s)$.

In the case of line/cable wideband models, $Y_n(s)$ is defined by:

$$Y_n = \begin{bmatrix} (I - H_2 I)^{-1} (I + H_2 I) Y_C & 2(I - H_2 I)^{-1} H_I Y_C \\ 2(I - H_2 I)^{-1} H_I Y_C & (I - H_2 I)^{-1} (I + H_2 I) Y_C \end{bmatrix} \tag{3}$$

where $I$ is the identity matrix, $Y_C$ and $H_I$ are the characteristic admittance and propagation matrix, respectively. We dropped $(s)$ from the matrices for the sake of simplicity.

One can verify the positive realness of $Y_n(s)$ by using frequency sweeping in (1) or looking for pure imaginary eigenvalues of the frequency-dependent Hamiltonian matrix [11]. Frequency sweeping is the most robust method, but it depends on fine sampling to avoid missing passivity violations. On the other hand, the Hamiltonian test detects all...

### 3.1. Passivity constraint

Condition (7) can be linearly approximated and rewritten as follows

$$\lambda_{j,i}(\Theta(Y_j(s))) + d_{\lambda_{j,i}}(s, \mathbf{x}) > 0 \quad \forall j,i, \quad \mathbf{x} = \begin{bmatrix} \bar{\mathbf{r}}_R \\ \bar{\mathbf{p}}_R \\ \bar{\mathbf{c}}_R \end{bmatrix} \tag{10}$$

where $d_{\lambda_i}$ is the first differential of the eigenvalue function [15], $(\bar{\mathbf{r}}_R, \bar{\mathbf{p}}_R, \bar{\mathbf{c}}_R)$ are the relative perturbations in vector form of residues, poles, and constant term, respectively. The detailed definition of $d_{\lambda_i}(s, \mathbf{x})$ is available in Appen