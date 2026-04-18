# Enhancing computation performance of rational approximation for frequency-dependent network equivalents with parallelism and complex vector fitting

Alexandre A. Kida a,b,∗, Felipe N.F. Dicler c, Thomas M. Campello c,d, Loan T.F.W. Silva c, Antonio C.S. Lima c, Fernando A. Moreira a, Robson F.S. Dias c, Glauco N. Taranto c

a Federal University of Bahia, UFBA, BA, Brazil
b Federal Institute of Bahia, IFBA, BA, Brazil
c Federal University of Rio de Janeiro, COPPE/UFRJ, RJ, Brazil
d CEFET/RJ – Federal Center for Technological Education Celso Suckow da Fonseca, RJ, Brazil

**Keywords:** Complex vector fitting, Electromagnetic transients, Frequency-domain realization, Vector fitting, Parallelization

**Abstract:** This work examines two strategies for enhancing the rational approximation of Frequency-Dependent Network Equivalents (FDNE) using an 8-port FDNE featuring a frequency response marked by numerous peaks and valleys. Firstly, we employ Complex Vector Fitting (CVF), an alternative to the Vector Fitting (VF). CVF eliminates the constraint of complex conjugate pairs and was originally conceived for modeling baseband equivalents through scattering parameters. The implications of CVF for admittance (or impedance) matrix synthesis have not yet been previously reported in specialized literature. To enhance code performance and remove dependence on commercial software such as MATLAB®, VF and CVF were implemented in the C-language, utilizing a low-level linear algebra package and exploiting parallelism. We evaluated performance by varying the model order, number of ports, and frequency samples. The results confirm the feasibility of our approach, prompting a more in-depth exploration of the potential benefits regarding FDNE realization.

✩ This research was supported in part by Coordenação de Aperfeiçoamento de Pessoal de Nível Superior (CAPES), Brazil under Grant 001, Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq), Brazil under grants 404068/2020-0, 400851/2021-0, Fundação de Amparo à Pesquisa do Estado de Minas Gerais (FAPEMIG), Brazil under grant APQ-03609-17 and Instituto Nacional de Energia Elétrica (INERGE), Brazil.
∗ Corresponding author at: Federal Institute of Bahia, IFBA, BA, Brazil.
E-mail address: alexandre.kida@ifba.edu.br (A.A. Kida).

https://doi.org/10.1016/j.epsr.2024.110778
Received 1 October 2023; Received in revised form 12 March 2024; Accepted 17 June 2024
Available online 26 June 2024
0378-7796/© 2024 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

## 1. Introduction

Power systems are undergoing significant transformations, marked by the increasing adoption of converter-based generation and HVDC technologies, alongside increasing environmental constraints [1]. These transformations introduce new network dynamics, emphasizing the necessity for a comprehensive network representation to ensure accurate modeling. However, electromagnetic transient (EMT) phenomena may have extensive frequency bandwidth. Thus, modeling an entire electric power system with such a detailed representation greatly increases the model complexity. In addition, simulation times can be impractical, especially for statistical cases and sensitivity analysis [2].

Therefore, it is convenient to separate the electrical power system into two subsystems [3]. The first one is the study system, which is modeled in detail, including its nonlinearities. The second subsystem, known as the external system, is characterized by a Frequency-Dependent Network Equivalent (FDNE). This system encompasses the remainder of the network and has linear and time-invariant characteristics, tailored for analyzing EMT phenomena. The buses connecting the study and external systems are called boundary buses (or equivalent ports). The selection of these ports considers the interest area where an EMT phenomenon or equipment will be analyzed.

Typically, the external area is represented by a simplified short-circuit equivalent at grid frequency, preserving only the fundamental frequency characteristics of the external area. On the other hand, FDNEs maintain their characteristics across a wide range of frequencies, offering higher accuracy [4]. Among the available methods for obtaining FDNEs, rational models (RMs) have been extensively utilized for this purpose and other important applications [5].

Another method for obtaining FDNEs involves solving a system of differential–algebraic equations, typically derived from a circuit model formulation. This approach yields a complex equation set, often simplified using model order reduction (MOR) techniques. The resulting equations can be directly integrated into an EMT solver like ATP, EMTP or PSCAD, or synthesized as an equivalent circuit. However, most commercial programs lack external equation exporting capabilities. As an alternative, frequency scan tools within these programs, along with curve fitting methods, are commonly employed to approximate the system frequency response and obtain an FDNE [5].

where $s = j\omega \in \mathbb{C}$, $\omega$ is the angular frequency in rad/s, $\mathbf{Y}(s) \in \mathbb{C}^{N \times N}$ is the approximated (fitted) nodal admittance, $N_p$ is the number of poles (model order), $\mathbf{D} \in \mathbb{R}^{N \times N}$ and $\mathbf{E} \in \mathbb{R}^{N \times N}$ are positive definite matrices, $p_n$ is the $n$th pole and $\mathbf{R}_n \in \mathbb{C}^{N \times N}$ is the associated $n$th residues matrix.

The expression in (1) can be converted from the pole-residue realization to a state-space formulation [30–33], such as
$$\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t) \tag{2}$$

The RM employing curve fitting methods for realizing FDNE has been under considerable investigation in recent years. In addition to the pole-relocation algorithm, known as Vector Fitting (VF) [6–8], the Frequency-p