# Z-function convolution in EHV power network electromagnetic transient analysis

**W D Humpage, K P Wong and T T Nguyen**  
*Department of Electrical and Electronic Engineering, University of Western Australia, Australia*

**Abstract**  
Time-convolution in the forms arising in transformation from the frequency-domain to the time-domain has been widely used in the earlier development of electromagnetic transient methods in power systems. Independent work has recently led to new methods based on the z-transform, and the present paper develops methods based on discrete convolution arising from transformation to the time-domain now from the z-plane. The recursive solution sequences to which this leads combines high accuracy with low computing time requirements. Checks and controls in the synthesis of transmission line forward impulse response and surge impedance functions in the z-plane ensure that these are always stable system functions, and that numerical solution procedures which include them have very high inherent stability. The formulations developed are applied to transmission line energization from an equivalent source model, and the electromagnetic transients in short-circuit fault operation. Close comparisons are made between representative solutions from standard time-convolution analysis and from the methods of the present paper.

**Keywords:** electric power transmission, electromagnetic transients, z-plane function convolution

## I. Introduction
Following the earlier development [1] of several different forms of electromagnetic transient analysis in high-voltage power networks, recent work has reported power transmission line transient models which are based on digital filters [11]. One of the applications of filter models is in the derivation of computational algorithms, and recent work has produced solution sequences derived from that basis. These require the explicit structures of filter networks and they are formed in terms of the delay functions in their forward and return signal-flow paths. To reflect filter concepts formally into transient analysis leads to methods which involve the convolution of z-plane functions. Principal among the methods developed so far have been those in which transformation from the frequency-domain to the time-domain leads to time-convolution, but no paper so far has referred to formulations which derive from the convolution of z-plane functions. In principle, the z-plane is used as an intermediate transform step [2] between the frequency-domain and the time-domain. For any given boundary conditions, a complete analysis formulation is developed almost entirely in the z-plane. Only the final group of equations required in the solution are transformed from the z-plane to the time-domain in terms of discrete-function convolution. Surprisingly concise sequences provide both fully comprehensive electromagnetic transient analysis formulations and also the individual and explicit steps of recursive evaluation. The present paper develops this logical extension of recent investigations of power transmission line electromagnetic transient modelling by digital filters.

Received: 19 October 1982

## II. Principal symbols

| Symbol | Description |
|---|---|
| $F_Q(z)$ | transmission line forward impulse response |
| $Z_0(z)$ | transmission line surge-impedance function |
| $z_s(z)$ | source impedance function |
| — | matrices of source resistance and inductance coefficients |
| $v(z), i(z)$ | vectors of voltage and current variables in z-plane |
| $v(n), i(n)$ | vectors of voltage and current variables in recursive solution sequences |
| $F(z), F(n)$ | forward characteristics |
| $B(z), B(n)$ | backward characteristics |
| $w(n)$ | vector of intermediate variables |
| $C_1, C_2$ | modal transformation matrices |
| $\Delta t$ | sample interval in time-domain |
| $m$ | ratio of wave transit time to sampling interval |

The subscripts $s$ and $r$ identify variables at the switching and remote ends of the transmission line, respectively. The subscript $f$ identifies variables at a point of short-circuit fault discontinuity. The superscript $p$ distinguishes phase-variables from modal variables.

## III. Z-plane response functions
Multi-product forms of transmission line response functions in the z-plane lead directly to the cascade filter structures of earlier work [3], but the z-function convolution procedures of the present paper are approached more directly when numerator and denominator functions have open polynomial forms. It is also preferable first to consider the functions for one mode so that the subsequent working is in scalar form. The steps of the working apply identically to each mode, and, when these are complete, modes re-group to a vector form. On this basis, the forward impulse response $F_Q(z)$ and the surge impedance function $Z_0(z)$ are expressed in the forms:

$$F_Q(z) = \frac{z^{-m}}{1 + \sum_{k=1}^{M_1} b_k z^{-k}} \quad (1)$$

$$Z_0(z) = Z_c \frac{1 + \sum_{k=1}^{M_2} c_k z^{-k}}{1 + \sum_{k=1}^{M_1} d_k z^{-k}} \quad (2)$$

Owing to the term $z^{-m}$ in $F_Q(z)$,

## IV. Z-function convolution

### IV.1 Convolution involving the forward impulse response
In considering z-function convolution involving the forward impulse response, $F_Q(z)$, input and output functions, $g_1(z)$ and $f_1(z)$, are introduced so that it is required to evaluate:

$$D_Q(z) = \sum_{k=1}^{m_1} b_k z^{-k} \quad (10)$$

$$N_0(z) = \sum_{k=1}^{M_2} c_k z^{-k} - \sum_{k=1}^{m_2} d_k z^{-k} \quad (11)$$

$$D_0(z) = \sum_{k=1}^{m_2} d_k z^{-k} \quad (12)$$

$$N_s(z) = (e - 1) z^{-1} \quad (13)$$