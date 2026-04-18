## Analytical and measurement-based wideband two-port modeling of DC-DC converters for electromagnetic transient studies
H. Alameri a, P. Gomez b, *
a Computer Engineering Department, University of Baghdad, Baghdad, Iraq
b Department of Electrical and Computer Engineering, Western Michigan University, Kalamazoo, MI 49008 United States of America

*Paper submitted to the International Conference on Power Systems Transients (IPST2023) in Thessaloniki, Greece, June 12–15, 2023.*
* Corresponding author. E-mail address: pablo.gomez@wmich.edu (P. Gomez).

## Keywords
Black-box models, DC-DC converters, Frequency domain analysis, Numerical Laplace transform, Two-port models, Wideband representation

## Abstract
Power-electronic converters are essential elements for the effective interconnection of renewable energy sources to the power grid, as well as to include energy storage units, vehicle charging stations, microgrids, etc. Converter models that provide an accurate representation of their wideband operation and interconnection with other active and passive grid components and systems are necessary for reliable steady state and transient analyses during normal or abnormal grid operating conditions. This paper introduces two Laplace domain-based approaches to model buck and boost DC-DC converters for electromagnetic transient studies. The first approach is an analytical one, where the converter is represented by a two-port admittance model via mode averaging and inclusion of switching effects. The second approach consists of reconstructing the two-port admittance model of the converter from terminal measurements for a series of tests. The performance of both approaches is evaluated against EMTP simulations, with very close results.

## 1. Introduction
POWER electronic-based converters are the gateway for efficient and reliable integration of distributed energy resources (DER), energy storage units, electric vehicles, and other modern technologies, to the electric grid. Thus, accurate and practical modeling of these devices to evaluate their interaction with other active and passive power components is critical for various power systems studies.

Over the last decades, it has become clear that the dynamic simulation of power systems with DER integration requires, in many cases, of electromagnetic transient (EMT) models that can provide an accurate response over a wide frequency range [1]. This is mainly due to the fast dynamics of modern power electronic components, which extend to a much wider frequency range above the nominal frequency [2]. Thus, the use of EMTP (Electro Magnetic Transient Program)-type software tools is now a common practice by the power systems community for grid studies with converter-based DER integration [3].

Although EMTP is a very valuable and robust tool for general EMT studies, it can be ineffective for dynamic studies of power electronic-based power systems given the combination of small time-steps and long simulation times to account for wideband transient behavior, which can result in prohibitive computational costs, especially for large systems [4]. In addition, results accuracy can be compromised by the approximations required to introduce frequency dependence of power components, a crucial aspect for the correct prediction of dynamic and transient response of systems with wide frequency content [2].

Another challenge of the EMT simulation of power electronic-based power systems is the limited availability of generic models of power converters, which in many cases are provided as black boxes by manufacturers due to technology proprietary issues [5]. Even when nominal models are provided by manufacturers, parameters may vary over time due to fluctuations in operating state, weather conditions, component aging, etc [6].

Considering the drawbacks of utilizing time domain techniques, there have been recent efforts to develop models of power electronic devices for dynamic studies based on the use of frequency domain representations [7–9]. Recent studies have also showcased the advantages of using impedance/admittance-based models for stability studies of grid-connected inverters [10–12]. In addition, further work has explored the generation of measurement-based converter models using time and frequency domain methods [13–15].

One of the salient features of an impedance/admittance-based approach is the straightforward analysis of interoperability between converters from different vendors, which is regarded as a key issue for the reliability of future power systems [2]. Frequency domain approaches are also well suited for design-oriented analysis [11], they are considered more computationally efficient and scalable than state-space representations, and they are also highly compatible with the use of reduction/partitioning techniques, which are “urgently demanded for the stability analysis of very large power-electronic-based power systems” [11].

Building upon the aforementioned work, as well as our preliminary work in [16], in this paper we aim to contribute to the state-of-the-art on converter modeling by proposing alternative analytical and measurement-based approaches for wideband representation of power converters, focusing on DC-DC buck and boost converters given their well-known topologies and extended use as part of DER-populated systems. Our analytical approach is based on two-port representation of mode average converter models in the Laplace domain, with further addition of switching frequency, and time domain solution using the inverse numerical Laplace transform (INLT) [17]. On the other hand, our measurement-based approach is based on performing a series of tests

Fig. 1. Buck converter: (a) schematic, (b) admittance model for mode 1 with S: