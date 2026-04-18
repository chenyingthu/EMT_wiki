# Admittance-based modelling of cables and overhead lines by idempotent decomposition

Felipe Camara $^{a,*}$, Antonio C.S. Lima $^{b}$, Maria Teresa Correia de Barros $^{c}$, Filipe Faria da Silva $^{a}$, Claus L. Bak $^{a}$

$^{a}$ Aalborg University, Denmark  
$^{b}$ Federal University of Rio de Janeiro, Brazil  
$^{c}$ University of Lisbon, Portugal  

**Keywords:** Cable, Electromagnetic transients, Idempotent decomposition, Modelling, Overhead line, Vector fitting

**Abstract:** This paper presents a new modelling approach based on idempotent decomposition of the nodal admittance matrix for representation of cables and overhead lines (OHL). By subjecting the idempotent matrices rather than the nodal admittance matrix to rational fitting, the poor observability of the smallest eigenvalues in the lower frequency range is overcome. Unlike the well-known method of characteristics (MoC), this alternative representation yields a so general fully-coupled admittance matrix suitable to tackle scenarios encompassing short and long lengths. Besides retaining the frequency dependence of parameters, the proposed phase-domain model showed to be accurate and suitable to circumvent the requirement of small time-steps.

* This work was supported in part by the European Union’s Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No 101031088, Coordenação de Aperfeiçoamento de Pessoal de Nível Superior (CAPES) under Grant 001, Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq) under grants 404068/2020-0, 400851/2021-0, Fundação de Amparo à Pesquisa do Estado de Minas Gerais (FAPEMIG) under grant APQ-03609-17 and Instituto Nacional de Energia Elétrica (INERGE).
* Corresponding author. E-mail addresses: fcn@energy.aau.dk (F. Camara), acsl@dee.ufrj.br (A.C.S. Lima), teresa.correiadebarros@tecnico.ulisboa.pt (M.T. Correia de Barros), ffs@et.aau.dk (F.F. da Silva), clb@et.aau.dk (C.L. Bak).
https://doi.org/10.1016/j.epsr.2023.109596  
Received 11 December 2022; Received in revised form 12 March 2023; Accepted 21 June 2023  
Available online 31 August 2023  
0378-7796/© 2023 Published by Elsevier B.V.

## 1. Introduction

The field of cable modelling is an important research topic regarding simulation of electromagnetic transients (EMT). As a key enabler for integration of renewable energy resources, cables and overhead lines, hereinafter referred as lines, play an important role which requires accurate and efficient numerical models.

Time-domain solvers employ MoC-based models to evaluate travelling wave phenomena and several contributions have been proposed to overcome issues in modal-domain [1–11] and phase-coordinates [12–16]. Numerical stability is reported as a concern since large residue-pole ratios cause magnifications of interpolation errors leading to unstable time-domain simulations [17–20]. The influence of earth-return effects has receiving significant contributions since most parameter routines embedded in EMT-like software are based on conservative simplifying assumptions.

Simulations involving short line lengths require very small time-steps which increase the computation burden substantially. Some efforts addressed this problem [21,22] but it has been traditionally coped by cascading $\pi$-sections which precludes frequency dependent effects.

To circumvent inherent issues related to MoC-based modelling, an alternative formulation exploits the nodal admittance matrix $\mathbf{Y}_n$ [23,24] which relates the terminal voltage and current in the frequency domain. It imposes no constraint due to the cable length, phase conductor arrangement or circuits running in parallel. However, the direct fitting of $\mathbf{Y}_n$ results in inaccurate characterization of the smallest eigenvalues in the lower frequency range. The so-called folded line equivalent model [25] addressed this issue through a similarity transformation in $\mathbf{Y}_n$ by decomposing it into open-circuit and short-circuit contributions in the phase-domain. Another distinct approach called Bergeron-cells [26] has been proposed for frequency-dependent modelling of transmission lines employing a cascade of cells in a similar fashion as in the cascaded $\pi$ modelling. This methodology avoids the modal decomposition either in the identification and time-domain realization stages.

Commonly used in linear algebra, also known as spectral decomposition, the idempotent decomposition is a technique to decompose a given matrix into a sum of elementary matrices that, when multiplied by itself, produces itself again [27]. To the best of the author’s knowledge, the first use of idempotents in power systems is reported to Prof. Wedepohl’s lecture notes [28]. Then, the idempotent decomposition was firstly proposed in the rational approximation of $\mathbf{H}$ in phase-coordinates for overhead lines [29]. Contrary to the modal domain transformation, it represents a linear transformation on idempotents instead of eigenvectors [30,31]. Later, the feasibility of applying idempotents for a full-frequency dependent line model using the MoC was investigated in the analysis of underground cables and overhead lines [32]. However, it was found that to handle $\mathbf{Y}_c$ and $\mathbf{H}$ matrices in an explicitly way. After subjected to a rational approximation, $\mathbf{Y}_n$ presents the following form

$$ \mathbf{Y}_n(s) \approx \sum_{m=1}^{M} \frac{\mathbf{R}_m}{s - p_m} + \mathbf{D} \quad (4) $$

where $p_m$ is a set of common poles, either real or complex conjugate, $\mathbf{R}_m$ is the residue matrix and $\mathbf{D}$ is the real part of $\mathbf{Y}_n$ at infinite frequency.