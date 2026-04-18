# Realization of rational models for tower-footing grounding systems

**Antonio C.S. Lima**^a,∗, **Thiago J.M.A. Parreiras**^a, **Rafael Alípio**^b, **Maria Teresa Correia de Barros**^c

^a Universidade Federal do Rio de Janeiro, P.O. Box. 68504, 21945-970, Rio de Janeiro, RJ, Brazil  
^b CEFET-MG, Belo Horizonte, MG, Brazil  
^c University of Lisbon, Lisbon, Portugal

**Keywords:** Grounding, Circuit synthesis, Lightning protection, Electromagnetic Transients

**Abstract**  
A tower footing grounding system plays an essential role in lightning-related overvoltages. For time-domain analysis, using an Electromagnetic Transient (EMT) program, one typically has to resort to a rational approximation of the harmonic impedance or a frequency-dependent network equivalent (FDNE) for the grounding system. Although one may obtain a rational approximation in several ways, a discussion of the impact of the topology considered for the rational approximation and the effect of the effective length in this realization has not been presented in the literature. Thus, this work focused on these two aspects. First, a comparison of either approach regarding a minimum-order representation. Second, comparing the two possible topologies of the rational approximation order and its relationship with the effective length. The results indicate that an accurate FDNE is slightly more robust if the effective length is respected.

---
*This study was financed in part by the Coordenação de Aperfeiçoamento de Pessoal de Nível Superior, Brazil (CAPES), Finance Code 001. It was also partially supported by INERGE (Instituto Nacional de Energia Elétrica), CNPq (Conselho Nacional de Desenvolvimento Científico e Tecnológico), and FAPERJ (Fundação Carlos Chagas Filho de Amparo à Pesquisa do Estado do Rio de Janeiro). Paper submitted to the International Conference on Power Systems Transients (IPST2025) in Guadalajara, Mexico, June 8–12, 2025.*  
*∗ Corresponding author. E-mail addresses: acsl@coppe.ufrj.br (A.C.S. Lima), masseran@coppe.ufrj.br (T.J.M.A. Parreiras), rafael.alipio@cefetmg.br (R. Alípio), teresa.correiadebarros@tecnico.ulisboa.pt (M.T. Correia de Barros).*

## 1. Introduction

Tower-footing grounding system plays an important role in assessing ground potential rise (GPR) during transients related to lighting phenomena. Typically, the frequency or time domains can be used for such evaluation. For the former, the Method of Moments (MoM) [1,2] is employed, considering either an equivalent impedance matrix [3–6] or using the Partial Element Equivalent Circuit (PEEC) method [7,8] as the Hybrid Electromagnetic Model (HEM) [9], or its modified version (mHEM) [10]. For the latter, there are two main possibilities: The finite-difference Time-Domain (FDTD) can be used to directly derive a ground system immittance [11,12] or one may adapt the grounding impedance calculated using one of the above methods to allow a representation in an Electromagnetic Transient (EMT) program such as ATP, EMTP or PSCAD.

To include a grounding system in an EMT program, one may consider using a frequency-dependent transmission line model [13–16], obtain an equivalent circuit [17–20] or use a rational approximation of the harmonic impedance of the grounding system. Some algorithms such as, Vector Fitting [21–23] or Matrix Pencil Method [24–27] can be utilized to obtain this harmonic impedance.

More recently, in the case of a tower footing grounding system, some works [28,29] have treated the tower footing grounding system as a frequency-dependent network equivalent (FDNE). In this scenario, post-processing passivity enforcement must be carried out to ensure stable time responses [30–34]. However, these works do not discuss whether or not this approach leads to a more robust implementation in terms of numerical stability, realization order, and even if a reduced-order realization is feasible.

The topic of order reduction is vast and has received considerable interest in the technical literature; see, for instance, [35–37]. Traditional methods relying on balanced truncation [38,39] have been shown to fail to provide accurate responses in the high-frequency range, demanding a different approach to achieve minimum order.

The paper is organized as follows. Section 2 briefly describes the formulation of the impedance matrices using mHEM, and the assembly of an equivalent nodal admittance matrix. Section 3.1 presents the determination of the harmonic impedance and its associated rational modeling. Section 3.2 shows the evaluation of an FDNE for the tower footing grounding system and the related rational approximation, together with a discussion of the pole number and the associated accuracy. Time responses of the GPR of the counterpoise configuration considering double-peek and fast-front currents are depicted in Section 4. The main conclusions are presented in Section 5.

**Fig. 1.** Finite length lossless electrodes in a uniform medium.

**Fig. 2.** Counterpoise configuration.

avoid a more rigorous solution to represent the air–soil interface via a series expansion of plane waves and then obtain a coherent set of reflection and refraction coefficients [41, sec. 7.6]. Furthermore, in [42], it was shown that image methods can provide suitable response for buried conductors if frequencies below 10 MHz are to be considered.