# Accuracy Evaluation of Electromagnetic Transients Simulation Algorithms
Huanfeng Zhao, Student Member, IEEE, Yi Zhang, Fellow, IEEE, and Aniruddha M. Gole, Fellow, IEEE

**Abstract—** This paper introduces a novel frequency domain technique to globally evaluate the accuracy of electro-magnetic transient simulations. It is shown that simulation accuracy at low frequencies can sometimes be poorer than at high frequency. A modified approach which quantifies accuracy from a driving point as a function of frequency is also introduced that uses the Bilinear Transformation and Norton equivalents, to produce a “simulation accuracy spectrum”. This approach can be applied to large systems without explicitly forming state space equations. It also permits the accuracy analysis of networks with distributed components such as frequency dependent transmission lines. Two examples are used to verify the proposed technique, a small network with a frequency dependent transmission line modeled by the universal line model; and the IEEE 39 bus system connected with an LCC-HVdc system.

**Index Terms—** Simulation accuracy, bilinear transformation, electromagnetic transients simulation, equivalent admittance, frequency dependent transmission line, controllability, observability.

## I. INTRODUCTION
IN MODERN power system analysis, electro-magnetic transient (EMT) simulation tools are widely used to investigate transient phenomena. As shown in Table I, depending on the phenomenon of interest, EMT simulation can cover a wide frequency range, from dc (0 Hz) to several tens of megahertz [1], [2].

For specific studies, higher accuracy is required in certain frequency ranges. For instance, in order to accurately study the effect of lightning surges on transmission lines, the simulation model should be highly accurate in the frequency range from 10k Hz to say, 3 MHz, but could be less accurate at low frequencies.

In reference [3], [4], the numerical accuracy is determined for individual dynamic elements such as capacitors and inductors. The mapping from discrete to continuous frequency domain is used to compare the simulation result with the theoretical result in the frequency domain. However, this technique does not accurately reflect the simulation accuracy of the whole system.

Reference [4] investigates the accuracy of simulation of individual elements considering mixed integration methods which are a combination of multiple different integration algorithms. However, all these methods focus on an individual component and, as is shown in this paper, can lead to incorrect conclusions of the accuracy of the network. Reference [5] examines the numerical accuracy based on the truncation error of the integration algorithm. The influence of distributed elements like transmission lines has also hitherto not been considered.

The key contributions from the paper to accuracy analysis of EMT simulations can be thus summarized:
a) The paper exposes a limitation of previous component level accuracy evaluation approaches by showing that it is not always true that simulation error for high frequencies is larger than for lower frequencies.
b) In order to overcome this limitation, the paper proposes (Section III) a State Space Equation based theoretical method to globally evaluate the simulation accuracy of linear lumped parameter networks.
c) Subsequently, for the purpose of applying the proposed method to large power networks, a new concept of a “Simulation Accuracy Spectrum” is introduced in Section IV, which plots the accuracy from any driving port as a function of frequency. The accuracy spectrum can be computed without forming the state space equations and therefore can easily be applied larger networks that can include distributed parameters.
d) The paper, for the first time introduces an approach to analyze the accuracy of networks that have frequency dependent transmission line elements. The Simulation Accuracy Spectrum concept is suitably extended cater to this situation.

| **TABLE I** | POWER SYSTEMS PHENOMENA AND FREQUENCY RANGES OF INTEREST [1], [2] |
|---|---|
| *(Table content not provided in source excerpt)* | |

Manuscript received December 17, 2020; revised May 20, 2021; accepted July 3, 2021. Date of publication July 26, 2021; date of current version May 24, 2022. This work was supported by the IRC program of NSERC, Canada and by Mitacs, Canada. Paper no. TPWRD-01852-2020. (Corresponding author: Huanfeng Zhao.)

Huanfeng Zhao and Aniruddha M. Gole are with the Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB R3T 5V6, Canada (e-mail: huanfengzhao@gmail.com; Gole@umanitoba.ca).

Yi Zhang is with RTDS Technologies, Winnipeg, MB R3T 2E1, Canada (e-mail: yzhang@rtds.com).

Color versions of one or more figures in this article are available at https://doi.org/10.1109/TPWRD.2021.3099008.

Digital Object Identifier 10.1109/TPWRD.2021.3099008

**Fig. 1.** Simple RLC circuit.

**Fig. 3.** Comparison of simulation and theoretical results for RLC circuit.

inductor or capacitor simulated by the trapezoidal method has no numerical error. Therefore, the ensuing conclusion is that the simulation accuracy worsens as the excitation frequency