# A simple and efficient method for including frequency-dependent effects in transmission line transient analysis

A Ametani, N Nagaoka, T Noda and T Matsuura
Doshisha University, Tanabe-cho, Kyoto 610-03, Japan

This paper proposes a simple and efficient method for calculating transmission line transients including frequency-dependent effects. The frequency-dependent distributed-parameter line is modeled by a combination of a distributed-parameter lossless line and an impedance circuit representing the frequency dependence of the original line. The impedance circuit is derived from a four-terminal parameter theory. Calculated examples by the proposed method are compared with the accurate results of a frequency-domain transient program FTP and a field test result. The accuracy of the proposed method is confirmed to be satisfactory. © 1997 Elsevier Science Ltd. All rights reserved.

**Keywords:** transmission line, transient, frequency-dependence, EMTP

## I. Introduction
It is well known that the frequency-dependence of line parameters causes a significant effect on transmission line transients. A frequency-domain method of a transient calculation has no difficulty in dealing with the frequency-dependent effects. A time-domain method such as the EMTP [1], however, has difficulty in including the frequency-dependent effects in the transient analysis. Thus, many approaches to its inclusion have been proposed. Principally, the approaches are based on real-time convolution. A main defect of the real-time convolution is the computation time and memory required for its numerical evaluation. To avoid this defect, a recursive convolution has been proposed [1-4], and has been widely used to deal with the frequency-dependent effects of a distributed line in its transient calculation. This recursive convolution is very efficient in comparison with the original real-time convolution. However, it still requires a large amount of memory for the past history of traveling waves on the distributed line. Also, numerical instability sometimes arises during parameter calculations of the recursive convolution.

The present paper proposes a very simple and efficient approach for including the frequency-dependent effects of a distributed-parameter line in its transient calculation. The frequency-dependent impedance of the line is approximated by a simple $L-R$ circuit combined with a distributed-parameter lossless line. The theory of the approach is explained in this paper, both for single-phase and multiphase lines. It is shown that the approach becomes identical to that of the lumped-resistive modeling of a distributed line developed by Dommel in the EMTP [1]. Example calculations are demonstrated to show the accuracy and efficiency of the proposed approach for an underground cable.

## II. Proposed model

### II.1 Theory of the model
A number of boundary conditions such as towers and groundings in a distributed line system are represented by an equivalent homogeneous line. On the other hand, a homogeneous line is represented by a combination of lumped-parameter circuits (boundary conditions) and distributed lines [5].

Let us assume that the frequency-dependent distributed-parameter line in Figure 1a is represented by an equivalent line in Figure 1b which is a combination of lumped impedances $Z_n$ and ideal lossless lines. The four-terminal parameter (F-parameter) of the original line in Figure 1a is given by:

$$ \begin{bmatrix} A & B \\ C & D \end{bmatrix} = \begin{bmatrix} \cosh \theta & Z_0 \sinh \theta \\ \sinh \theta / Z_0 & \cosh \theta \end{bmatrix} \quad (1) $$

where
$$ \theta = \Gamma x, \quad \Gamma \text{ is the propagation constant} \quad (2) $$
$$ Z_0 = \sqrt{z/y} $$

Figure 1. A proposed approach to represent a distributed line
(a) Original distributed-parameter line
(b) Proposed model for $n \ge 2$
(c) Proposed model for $n=1$

obtained from equation (3).

For $n > 2$:
$$ A' = A_0^2 + (2 + n)Z_n A_0 C_0 + B_0 C_0 + n(Z_n C_0)^2 $$
$$ B' = Z_n A' + (1 + n)Z_n A_0^2 + 2A_0 B_0 + n Z_n^2 A_0 C_0 + Z_n B_0 C_0 $$
$$ C' = C_0(2A_0 + n Z_n C_0) $$

For $n = 1$:
$$ A' = A_0^2 + (Z_n A_0 + B_0)C_0 $$
$$ B' = A_0(Z_n A_0 + 2B_0) $$
$$ C' = C_0(2A_0 + Z_n C_0) \quad (5) $$

In general, the value of the variable $\theta$ is very small. Thus, assuming $\theta \ll 1$, equations (1) and (4) are approximated by the following equations:

$$ A \approx 1 + \frac{zy x^2}{2} = 1 + \frac{(zx)(yx)}{2} = 1 + \frac{ZY}{2} $$
$$ B \approx Z, \quad C \approx Y $$