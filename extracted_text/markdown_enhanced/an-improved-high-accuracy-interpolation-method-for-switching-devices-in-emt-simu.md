# An improved high-accuracy interpolation method for switching devices in EMT simulation programs

J. Na a,d, H. Kim b, H. Zhao c, A.M. Gole c, K. Hur a,∗

a School of Electrical and Electronic Engineering, Yonsei University, Seoul 03722, South Korea  
b R&D Center, Pion Electric, Gyeonggi-do 14348, Republic of Korea  
c Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB R3T 2N2, Canada  
d R&D Center, Korea Grid Forming, Gyeonggi-do 14348, Republic of Korea  

∗ Corresponding author.  
E-mail addresses: jongseo529@yonsei.ac.kr, jongseo529@k-gfm.com (J. Na), h.kim@pionelectric.com (H. Kim), huanfengzhao@gmail.com (H. Zhao), aniruddha.gole@umanitoba.ca (A.M. Gole), khur@yonsei.ac.kr (K. Hur).

## Abstract
This paper presents an interpolation with Backward Euler (BE) method that enhances the switching simulations accuracy in an electromagnetic transient (EMT) simulation with a fixed time-step. Because of the switching operations on discrete instants, the simulations can show artificial voltage spikes and numerical oscillations (chatter), compromising the accuracy and producing misleading results. We thus present a method that eliminates the spurious switching losses and improves the accuracy by combining interpolation and extrapolation with a half-time-step BE solution over existing interpolation-based approaches to resolve the issues above. In addition, this improved method requires the same calculation steps as the industry-accepted instantaneous interpolation. Analytical discussion reinforced by the simulation studies for a simple and complex power electronic circuits demonstrates the accuracy and efficacy of the proposed interpolation with BE method.

## Keywords
Backward Euler, Discontinuity, Interpolation, Power-electronic switches, Trapezoidal

## 1. Introduction
Electromagnetic transient (EMT) simulation programs are widely used for modeling electric power systems with power electronic devices such as high-voltage dc (HVdc) converters, flexible ac transmission systems (FACTS), and renewable energy source (RES) converters [1,2]. These power electronic switching devices are generally modeled as bivalued resistors or ideal switches in the EMT [3]. The programs create a companion circuit of the network by applying numerical integration methods such as the Trapezoidal rule with a fixed time-step value and then solve the circuit using nodal analysis (or modified nodal analysis) [4,5].

Fixed time-step simulation presents critical issues when modeling semiconductor switches such as thyristors, gate turn-off thyristors (GTO), insulated gate bipolar transistors (IGBT), etc. Without mitigation measures, switching operations can result in:
- Numerical oscillation (chatter)
- Voltage spike
- Inaccurate simulation results

Numerical chatter is usually initiated by the opening of a switch in a branch containing inductor. This phenomenon comes from the characteristic of the Trapezoidal method, employing the current state and past state in the same differential equation. This numerical chatter happens when the switching occurs between time-steps, even at a natural zero current [6]. Voltage spikes can also arise across inductor branches due to the current chopping. Finally, inaccurate representation of the switching timing decreases accuracy of the simulation results. To improve accuracy, a very small time-step (e.g., 0.1 μs) can be applied, which, however, significantly increases the execution time; A trade-off between accuracy and execution time should be balanced.

There are several previously reported approaches to overcome the limitation of fixed time-step simulation with the Trapezoidal method. Snubber circuits across switches were parameterized to reduce the effect of chatter [3,5]. However, the artificial parameters of the snubber circuit may adversely affect the simulation accuracy. Critical damping adjustment (CDA) has also been widely used to suppress the chatter [7–10]. Two advantages of the CDA are as follows: (1) the Backward Euler (BE) method suppresses numerical oscillation, and (2) the admittance matrix of the half time-step BE method is the same as that of the one-step Trapezoidal method. However, CDA cannot cope with inaccurate representation of the switching timing. Variable time-step simulation is another alternative solution for accurate simulation results [11–14]; However, it is highly challenging to set the optimal variable time-step size. In addition, 2s-DIRK, TR-BDF2, and matrix exponential methods have been proposed to remove numerical oscillation and improve accuracy. These are difficult to implement and show slower performance compared to the Trapezoidal rule [15–17]. Therefore, the interpolation meth

Fig. 1. Discontinuous inductor voltage due to switching.

Fig. 2. The ordinary interpolation process of natural-commutation.