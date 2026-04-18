## A 2-TRANSFORM MODEL OF TRANSFORMERS FOR THE STUDY OF ELECTROMAGNETIC TRANSIENTS IN POWER SYSTEMS

Q. Su, R.E. James, Member, D. Sutanto, Senior Member
Department of Electrical Power Engineering, University of New South Wales
P.O. Box 1, Kensington 2033, Australia

**Abstract:** A 2-transform model, which combines transformer frequency-dependent short-circuit impedances with gain functions has been developed. It sets up a relationship between transient voltages and currents on both sides of a transformer winding pair. The model can be used to calculate impulse responses of the transformers with open-circuit secondary winding as well as those connected to other networks. It could be incorporated into EMT programs for calculating the electromagnetic transients in power systems in which the distributed characteristics of transformer windings are to be considered. The wide applications of such a transformer model can be found in the areas of, for example, lightning protection of substations, busbar switching transients and recovery voltages of circuit breakers.

## I. INTRODUCTION

In the study of electromagnetic transients resulting from circuit switching in power systems, transformers are usually represented by their leakage impedances at power frequency. This simulation may not be correct in some conditions in which relatively high frequency transients are involved, for example, busbar switching in substations and clearing short-distance faults. For the study of lightning surges in substation protection, transformers are modelled by their entry capacitances. This model may not be valid for the surges of lightning which have a slower wavefront when reaching a transformer because inductances of the transformer could effect the transients as well. Over the years, two main forms of distributed-parameter model for transformers have been developed. The first is where ladder networks with a finite number of sections represent the distributed characteristics of transformer winding systems. The second is based on the derivation of input-output frequency responses for winding pairs which are then used in time convolution forms of transient analysis.

The developments reported in the present paper seek to contribute to the second method. They do so in two main ways. Firstly, transformer short-circuit impedances are included in the derivation so that, when combined with open-circuit frequency responses, the representation can be incorporated into a model for a complete network of which a transformer is one element. Secondly, the z-plane is used as an intermediate transform step between the continuous frequency-domain in which transformer frequency responses are expressed and the time-domain in which surge propagation analysis is carried out.

The frequency response of a transformer winding-pair is identical in a wide bandwidth by means of a gain function which is determined by the ratio between sinusoidal input and output voltages across the two windings. Magnitudes of a typical gain function measured on a 200MVA 220kV transformer are shown in Fig. 1. The frequency dependent function has a flat shape from 50 Hz to some kilohertz, with normalized amplitudes near to one. At high frequencies, the gain function presents some resonances and anti-resonances.

Fig. 1 S-plane synthesis of the gain function.
---- From the 200MVA auto-transformer.
---- From the frequency-weighted 3rd-order function synthesised in the S-plane.

From the theory of complex functions, if a function, $\Phi(s)$, in the complex frequency plane is not only analytic, but has no zero for $\text{Re}(s) > 0$, $\Phi(s)$ will be a minimum-phase-shift and can be uniquely determined from its magnitudes, $|\Phi(j\omega)|$. Usually, the gain function of transformers is not a minimum-phase-shift. There exists a short transit time between the input and output voltages of the transformer winding pair. However, the time delay can usually be separated from the gain function to obtain its minimum-phase-shift by the method used for transmission lines [1].

Assuming that $|D(j\omega)|$ is the magnitude of the gain function measured across a two-winding transformer,
where $V_H(\omega)$ is the sinusoidal voltage at radian frequency $\omega$ applied across the high-voltage winding,
$V_L(\omega)$ is the response across the low-voltage winding.
The gain function can be normalized as
$$B_n(\omega) = \frac{B(\omega)}{B(0)} \quad (2)$$

The errors of these two kinds of transformations are shown in Fig. 2. It can be seen from Fig. 2 that to limit the error to 1%, the product of the time step, $\Delta t$, and radian frequency, $\omega$, must be less than 0.35 for the bi-linear transformation and 0.9 for the bi-third transformation. If the highest frequency of the transient involved is $f_b$, the time step