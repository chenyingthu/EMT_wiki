## Single-Phase Nonuniform Transmission Lines in Electromagnetic Transient Simulations
**H.V. Nguyen**, Student Member, IEEE  
**H.W. Dommel**, Fellow, IEEE  
**J.R. Marti**, Member, IEEE  
Department of Electrical Engineering  
The University of British Columbia  
Vancouver, Canada  

**ABSTRACT**  
An exponential single-phase line model is introduced to represent nonuniform transmission lines. When the line parameters are assumed to vary exponentially, a set of two-port equations can be formed in the frequency domain, which contain frequency-dependent functions. These functions are then synthesized with rational functions of the minimum-phase-shift type. Utilizing a fast recursive convolution technique, the time-domain equations of the proposed model reduce to a form similar to those in Bergeron's method. Thus, the model is compatible with general electromagnetic transients programs such as the EMTP [1]. Time-domain simulations with the proposed model show good agreement with published experimental results, and with those produced by a cascade multi-section model, where the line is divided into many short sections of uniform transmission lines.  

**Key words:** Exponential line, EMTP, time domain, frequency domain, synthesis, rational functions.  
**Notations:** Uppercase represents frequency domain quantities, whereas lowercase indicates their time domain correspondents.  

## 1. INTRODUCTION  
Various methods for modelling nonuniform transmission lines have been proposed [2-6]. A major application of such models is the simulation of travelling waves up and down transmission line towers. The tapered line model of [4] for the representation of towers had shortcomings inasmuch as it was only a high frequency approximation. Another method in which nonuniform lines were modelled as cascaded exponential lines [5], produced accurate results, but the solution was obtained in the s domain. For general purpose time-domain programs such as the EMTP, it is difficult to interface algorithms which work in the s domain. Therefore, a method based on finite-difference approximations of the wave propagation equations was recently proposed [6], which can be interfaced with the EMTP.  

The line model described in this paper follows from the work started in [4], and uses the exponential variation assumption of [5]. With this model, the line functions are directly synthesized in the frequency domain. The non-uniformity of the line parameters can then be included in the time domain by means of recursive convolutions.  

## 2. EXPONENTIAL TRANSMISSION LINE  
### 2.1 Equations in the frequency domain  
The basic equations of a nonuniform transmission line, expressed in the frequency domain, are  
$$-\frac{dV}{dx} = Z(x)I$$  
$$-\frac{dI}{dx} = Y(x)V$$  
$V$ and $I$ are the voltage and current phasors, and $Z(x)$ and $Y(x)$ are the space-dependent per-unit-length series impedance and shunt admittance, respectively.  

Following the procedure of [5], equation (1a) is differentiated again,  
$$\frac{d^2V}{dx^2} = -\frac{dZ(x)}{dx}I - Z(x)\frac{dI}{dx}$$  
Substituting (1a) and (1b) into (2) gives  
$$\frac{d^2V}{dx^2} = Z(x)Y(x)V + \frac{1}{Z(x)}\frac{dZ(x)}{dx}\frac{dV}{dx} \quad (3)$$  
For the exponential line shown in Figure 1, with losses ignored, $Z(x)$ and $Y(x)$ are  
$$Z(x) = j\omega L(x) = j\omega L_0 e^{qx} \quad (4a)$$  
$$Y(x) = j\omega C(x) = j\omega C_0 e^{-qx} \quad (4b)$$  
where $L(x)$ and $C(x)$ are the per-unit-length inductance and capacitance, respectively; $L_0$ and $C_0$ are the values at $x = 0$. These parameters are related to the high-frequency approximation of the line characteristic impedance,  
$$Z_0(x) = Z_{0eq} e^{qx}$$  
where $Z_0 = \sqrt{L_0/C_0}$.  

Substituting (4a) and (4b) into (3) gives  
$$\frac{d^2V}{dx^2} - q\frac{dV}{dx} - \frac{\omega^2}{c^2}V = 0$$  

Figure 1: Single phase exponential line  
Figure 2: Equivalent circuit for the exponential line  

functions, their corresponding expressions in the time domain will become simple sums of exponential functions. The function $a(t)$ will also have a time delay, which approximately equals the time it takes for the fastest frequency component to travel along the line. Accordingly, the convolutions in equation (12) can be evaluated with a fast recursive algorithm [7]. Thus, the voltag