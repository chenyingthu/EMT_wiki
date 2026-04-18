# Optimization of numerical integration methods for the simulation of dynamic phasor models in power systems

Turhan Demiray *, Göran Andersson  
Power Systems Laboratory – ETH Zürich, Physikstrasse 3, ETL-I34, 8092 Zuerich, Switzerland  

* Corresponding author.  
E-mail addresses: demirayt@eeh.ee.ethz.ch (T. Demiray), andersson@eeh.ee.ethz.ch (G. Andersson).

**Article history:**  
Received 28 September 2008  
Received in revised form 30 March 2009  
Accepted 30 March 2009  

**Keywords:**  
Simulation  
Dynamic phasors approach  
Root-matching  
Frequency matched numerical integration  

**Abstract**  
This paper proposes the use of frequency matched linear numerical integration techniques for the simulation of systems modelled by the dynamic phasors approach (DPA). Such methods show an increased accuracy and computational efficiency around the matched frequency. Such frequency matched methods are derived by analyzing the local truncation error in the frequency domain and determining the coefficients of the method in such a way so that the error is minimized around the matched frequencies. The aim in this way is to increase the accuracy and the efficiency of the numerical calculation, during the inherent fast oscillations featured in such systems modelled with dynamic phasors approach.

## 1. Introduction

For the combined simulation of the electromagnetic and electromechanical transients in power systems, various system variable representations are used. The electromagnetic transients programs often use the instantaneous value representation of system variables and system equations in the original three phases [1]. Another possibility is to use a variable representation on a rotating reference frame (DQ0), which leads to constant system quantities in balanced steady state. Another form of system variable representation is the so called dynamic phasors, which is based on the time varying Fourier Series approximation of the periodic or nearly periodic system quantities [2,3]. Dynamic phasors provide a suitable framework which has the capability to model power system behavior as accurate as EMTP simulations and at the same time, computationally more efficient. In particular, the dynamic phasors approach has been applied to model three-phase systems with electric machines, FACTS devices and power converters [4–7]. Mathematical details of the dynamic phasors approach will be discussed in Section 2.

Regardless of the selected variable representation, in most of the cases, numerical integration techniques such as forward-Euler, backward-Euler, trapezoidal and Gear’s method are employed. Generally, in three-phase instantaneous value representation for modelling of power systems, the integration step size is very limited. Even if fast transients have decayed, the sinusoidal AC quantities of the electrical grid with the system frequency $f_s$ cannot be integrated with the maximum possible integration step size $h_{max} = \frac{1}{2f_s}$, due to the lack of accuracy of the used numerical integration methods at the system frequency. The most commonly used integration methods, such as forward-Euler, backward-Euler, trapezoidal and Gear’s method, are optimal for the numerical integration of low frequency signals, so that they are prone to some errors at higher frequencies if larger step sizes are used.

One approach to overcome this problem is to use the so called root-matching method [9]. Numerical integration techniques generally discretize a continuous system $H(s)$ by mapping it into an equivalent discrete time system $H(z)$. The optimum discretization method should match the poles, zeros and final value of the difference equation to those of the actual continuous system. If these conditions are fulfilled, the difference equations are stable regardless of the step size, if the actual continuous system is also stable. This root-matching approach can be interpreted as an adjustment of the discretization (numerical integration) method to the eigenvalues of the system. This method has been successfully applied for the discretization of the RL, RC, etc. branch elements in EMTP instead of the traditionally employed trapezoidal discretization method [1].

In [10], the authors introduced another integration method adapted to the periodic steady state at system frequency $f_s$. This method allows the use of larger step sizes up to $h = \frac{1}{2f_s}$ for the numerical integration of three-phase instantaneous electrical AC quantities.

Since we are using the dynamic phasor representation for power system modelling and simulation, our aim in this paper is to optimize the numerical integration method for variables represented by dynamic phasors.

As mentioned previously, in the root-matching method, the poles, zeros and final value of the discrete time system are matched to those of the actual continuous system. The idea now is to relax this condition of root-matching and to match the numerical integration not exactly to the eigenvalues of the dynamic phasors but approximately to the oscillatory frequencies of the dynamic phasors. The aim in t