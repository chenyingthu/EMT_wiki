# Accurate time-domain simulation of power electronic circuits

**Willy Nzale** $^{a,*}$, **Jean Mahseredjian** $^{a}$, **Xiaopeng Fu** $^{b}$, **Ilhan Kocar** $^{a}$, **Christian Dufour** $^{c}$

$^{a}$ Polytechnique Montréal, Montréal, QC H3T 1J4, Canada  
$^{b}$ Key Laboratory of Smart Grid of Ministry of Education, Tianjin, China  
$^{c}$ Opal-RT Technologies, Montréal, QC H3K 1G6, Canada

**Keywords:** Accuracy, Discontinuity, Power electronic circuits, Simulation method, Time-domain simulation

**Abstract:** Modern power electronic circuits contain numerous switches driven by high frequency controllers and can cause discontinuities in time-domain simulation methods. This paper presents numerical problems resulting from discontinuities when simulating power electronic circuits. Limitations in existing methods are analyzed. Three new methods are proposed to improve accuracy and computational performance.

✰ Paper submitted to the International Conference on Power Systems Transients (IPST2021) in Belo Horizonte, Brazil June 6–10, 2021.  
* Corresponding author. E-mail addresses: willy-arnaud.nzale-mimbe@polymtl.ca, nzal_willy@yahoo.fr (W. Nzale).

## 1. Introduction

The trapezoidal integration method is commonly used in time-domain simulation of electromagnetic transients and power electronic circuits [1,2]. It is a one-step implicit A-stable method with second order accuracy [3,4] that can perform efficiently and accurately for a wide range of transient frequencies [4].

Trapezoidal (TR) integration causes numerical oscillations at discontinuities. Discontinuities occur due to switching in power electronics circuits or due to nonlinear functions. Several techniques are proposed in the literature to eliminate such oscillations. One of them consists in using the L-stable Backward Euler (BE) method to reinitialize TR integration [5]. Another approach consists of switching from trapezoidal (TR) integration to BE method for two half time-steps after the discontinuity occurrence [4,6]. This method is implemented in [7]. Numerical oscillations can be also eliminated using the chatter removal technique [8]. It consists in performing a half time-step interpolation after crossing a discontinuity. However, as demonstrated in this paper, the existing methods are not perfect.

Discontinuities create errors and simulation methods must adapt to guarantee accuracy. In fixed time-step simulations, discontinuities may occur between two discrete time points. Interpolation techniques [9,10] are applied to fall back to discontinuity instant and to resynchronize with simulation time-mesh. Inaccurate tracking of discontinuities may result in additional errors and even in non-characteristic harmonics for some power-electronic circuits [11,12]. Interpolation is also used to attempt accurate tracking of multiple commutations occurring in-between consecutive time points [13].

As demonstrated in [14], a reliable time-domain simulation algorithm must incorporate a mechanism to accurately track discontinuities and a mechanism to account for instantaneous commutations. This is challenging because additional errors may be created, as demonstrated in this paper.

It is noteworthy to mention that some numerical integration algorithms [3,15-17] are oscillation-free. The focus of this paper is on the widely (major simulation tools) used trapezoidal integration method.

This paper summarizes numerical issues resulting from discontinuities in the computation of electromagnetic transients with power electronic circuits and proposes alternative solution methods. This paper is organized as follows. Section 2 describes the numerical problems. Section 3 presents existing methods and limitations. Section 4 contributes new methods. Finally, in Section 5, numerical results and practical simulation cases are presented.

## 2. Main issues with discontinuities in time-domain simulation

### 2.1. Generalities

In time-domain simulation, network components are described by differential equations in the form:

$$\dot{x} = f(x, t) \tag{1}$$

It is common to solve such equations using, for example, TR and BE integration (discretization) methods with fixed time-step $\Delta t$. The methods are recalled here:

$$x_{t+\Delta t} = x_t + \frac{\Delta t}{2} [f_{t+\Delta t} + f_t] \tag{2}$$

$$x_{t+\Delta t} = x_t + \Delta t f_{t+\Delta t} \tag{3}$$

Discretization methods allow creating companion models [18] and to formulate network equations using, for example,

$$i_{t_d + \Delta t/2} = \frac{\Delta t}{2L_d} v_{t_d + \Delta t/2} + i_{t_d} = -\frac{v_{t_d + \Delta t/2}}{R_d} \tag{9}$$

$$i_{t_d + \Delta t} = \frac{\Delta t}{2L_d} (v_{t_d + \Delta t} - v_{t_d + \Delta t/2}) = -\frac{v_{t_d + \Delta t}}{R_d} \tag{10}$$

$$v_{t_d + \Delta t} = -\frac{v_{t_d + \Delta t/2}}{-\frac{\Delta t}{2L} - \frac{1}{R}} \tag{11}$$

It is noticed that