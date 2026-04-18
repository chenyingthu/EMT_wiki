## Modeling of overhead transmission lines for trapped charge discharge rate studies

J. Morales $^{a,*}$, J. Mahseredjian $^{b}$, I. Kocar $^{b}$, H. Xue $^{b}$, A. Daneshpooy $^{c}$

$^{a}$ PGSTech, Montréal (Québec) H2K 1C3, Canada
$^{b}$ Polytechnique Montreal, Montréal (Québec) H3C3A7, Canada
$^{c}$ Quanta Technology, Oakland (California) 92673, United States of America

**Keywords:** Transmission line, Trapped charge, Discharge rate, Wideband model, Numerical Laplace Transform

**Abstract:** This paper presents guidelines for appropriate modeling of overhead transmission lines for trapped charge discharge simulations. At first instance, the traditional Frequency-Dependent model is compared to the more recently developed Wideband model, showing that the former may lead to inconsistent results when simulating a transmission line with trapped charge due to limitations of the inherent fitting approach. Secondly, a sensitivity analysis is presented over the parameters that can affect the trapped charge discharge rate of the transmission line. Once the model is demonstrated to have consistent results, simulations obtained with the resulting model are compared with the Numerical Laplace Transform method, resulting in a good match and validating the model.

## 1. Introduction

A reliable assessment of the trapped charge dynamics on transmission lines following its disconnection from the network is crucial for utilities during operation and maintenance of power systems, not only to avoid service interruptions or damage to equipment, but also and most importantly to establish safe distance practices. For these reasons, power utilities rely on performing electromagnetic transient (EMT) simulations to estimate the decay time of trapped charge in transmission lines as result of switching events. Also, different switching techniques have been developed for the mitigation of transient overvoltages by playing with the trapped charges, examples of such techniques can be found in [1,2] and references therein.

There is a consensus in the literature that accurate representation of transmission lines for EMT-type simulations requires accounting for their distributed-parameters and their frequency-dependent nature. Among the models that account for these two characteristics are the Frequency-Dependent (FD) model [3] and the Wideband (WB) model [4-6]. These two models are available in EMTP software [7] and are widely used by power systems utilities and researchers.

Although the literature on transmission line modeling is rich, the study of overhead transmission line transient models with particular emphasis on trapped charge studies is poor.

Frequency-dependent line models such as the FD and WB models, are normally granted as adequate for most type of studies since they can cover a large range of frequencies, starting from a low-frequency region (near 0 Hz), including fundamental frequency points (50 or 60 Hz), and up to very high frequencies such as those required for switching transients, surge analysis, or lightning studies (around 100 kHz and higher). However, as demonstrated in this paper, some modeling aspects require special attention to evaluate the decay rate of trapped charges.

In the literature, the study of the decay rate of trapped charges has been mainly performed for underground cables while using simplified models for nearby transmission lines. For instance, in [8] the trapped charge is studied for an underground cable and a combined overhead line/underground cable transmission system, in both cases, the transmission line is modeled as a lumped-parameters circuit. In [9], the transmission line trapped charge decay rate is evaluated for lines connected to voltage transformers, but evidently, the inclusion of voltage transformers modifies the purely transmission line circuit dynamics, furthermore, a simplified lumped-parameters model is used to represent the line. In [10,11], the decay rate of trapped charges for underground

terminal voltages and currents are given by
$$V_k(s) - Z_c(s)I_k(s) = H(s)[Z_c(s)I_m(s) + V_m(s)] \quad (1)$$
where $V_{k,m}(s)$ and $I_{k,m}(s)$ denote voltages and currents, respectively; and $Z_c(s)$ and $H(s)$ denote the characteristic impedance matrix and the propagation function, respectively, defined as
$$Z_c(s) = \sqrt{Z'(s)/Y'(s)} \quad (2)$$
$$H(s) = e^{-\gamma \ell} = e^{-\sqrt{Z'(s)Y'(s)}\ell} \quad (3)$$
where $s = j\omega$, $Z = R(s) + sL(s)$ and $Y' = G' +$