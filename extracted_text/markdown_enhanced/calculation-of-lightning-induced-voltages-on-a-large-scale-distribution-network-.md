# Calculation of lightning-induced voltages on a large-scale distribution network using the JMarti model

Alberto De Conti $^{a,*}$, Osis E.S. Leal $^{b}$

$^{a}$ Department of Electrical Engineering, Universidade Federal de Minas Gerais (UFMG), Belo Horizonte, MG, 31270-901, Brazil
$^{b}$ Institute of Engineering, Science and Technology, Universidade Federal dos Vales do Jequitinhonha e Mucuri (UFVJM), Janaúba, Brazil

**Keywords:** Distribution networks, Electromagnetic transients, Lightning-induced voltages, Overhead lines, Time-domain methods

**Abstract**
This paper illustrates the application of a recently proposed time-domain method in the calculation of lightning-induced voltages by nearby cloud-to-ground lightning strikes on a realistic, large-scale distribution network using the JMarti model in the Alternative Transients Program (ATP). In this method, the effect of the incident electromagnetic fields on the illuminated lines is accounted for entirely in terms of independent current sources that are calculated only once for a given lightning event using data obtained from the built-in fitting tool available in ATP. The simulated large-scale network includes laterals, grounding points, surge arresters, transformers, and loads. It is shown that frequency-dependent line losses may have a significant effect on the voltages induced on different parts of the simulated network, and that they should not be neglected in this type of study.

* This article is part of a Special issue entitled: ‘IPST 2025’ published in Electric Power Systems Research.
* This paper was financed in part by the Coordenação de Aperfeiçoamento de Pessoal de Nível Superior - Brasil (CAPES), and by the National Council for Scientific and Technological Development (CNPq) (304157/2022-8).
* Paper submitted to the International Conference on Power Systems Transients (IPST2025) in Guadalajara, Mexico, June 8–12, 2025.
* Corresponding author. E-mail addresses: conti@cpdee.ufmg.br (A. De Conti), osis.leal@ufvjm.edu.br (O.E.S. Leal).
* https://doi.org/10.1016/j.epsr.2025.112232
* Received 30 December 2024; Received in revised form 9 March 2025; Accepted 4 September 2025; Available online 17 September 2025.

## 1. Introduction

One of the most important features of a computer code dedicated to the calculation of lightning-induced voltages on transmission lines is the possibility of integration with electromagnetic transient (EMT) simulation tools. The usual approach consists in writing an independent code to compute the incident electromagnetic fields on the line and solve the line equations in the time domain accounting for the influence of these fields. The line model is then interfaced with the EMT simulation tool via a Norton-type equivalent. At each time step, information coming from the external code is transferred into the EMT tool and vice-versa, so that the transients on the line and on the rest of the system are updated on an incremental basis [1].

Given the distributed nature of the incident lightning electromagnetic fields, the preferred approach for the solution of the transmission line equations including the influence of external fields is generally based on the finite-difference time-domain (FDTD) method [1, 2]. However, despite the convenience of this approach, it requires careful treatment of the line terminations for the interfacing with the EMT simulation tool. In addition, the need to satisfy the Courant–Friedrichs–Lewy condition often poses challenges for the efficient and stable computation of lightning-induced voltages on complex systems including nonlinear elements [2].

Another possibility for dealing with the coupling of lightning-generated fields with overhead lines is to resort to strategies based on the method of the characteristics [3–5]. However, most of the available methods rely either on the frequency-domain solution of the transmission line equations [3] or on a time-domain solution based on a lossless line [4–6]. The former approach requires the use of a numerical transform for enabling the interface with time-domain-based EMT simulation tools, while the latter is too restrictive for a rigorous analysis of the phenomenon. When line losses are included in lightning-induced voltage calculation strategies based on the method of characteristics (e.g., [7]), the solution of the transmission line equations is performed externally to the EMT tool. This does not take advantage of the line models already implemented in the EMT simulation tool and is likely to reduce the efficiency of the solution.

To circumvent the difficulties listed above, an innovative time-domain approach was proposed by the authors in which lightning-induced voltages can be calculated in any EMT simulation tool using the frequency-dependent line models already available in its library of components [8–10]. The idea is to represent the effect of the incident electromagnetic fields in terms of independent current sources

$$ \bar{\mathbf{u}}_{\ell}(t) = \mathbf{u}_{\ell}(t) - \mathbf{a}(t) * \bar{\mathbf{u}}_{0}(t) \tag{4} $$

In (3) and (4), $\mathbf{a}(t) = (\mathbf{t}^{-1}_{I})_{t} \mathcal{L}^{-1} \mathbf{A}_{m} \mathbf{t}_{tI}$ is the propagation function of the line, $\mathcal{L}^{-1}$ is the inverse Laplace transform operator, $\mathbf{A} = \text{diag}$