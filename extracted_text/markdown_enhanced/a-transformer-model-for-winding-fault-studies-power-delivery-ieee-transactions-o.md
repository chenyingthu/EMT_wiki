# A TRANSFORMER MODEL FOR WINDING FAULT STUDIES

**Patrick BASTARD**  
Electrical Engineering Dpt.  
ECOLE SUPERIEURE D'ELECTRICITE  
91190 Gif-sur-Yvette, FRANCE

**Pierre BERTRAND**  
Protection and Control Dpt.  
MERLIN-GERIN  
38000 Grenoble, FRANCE

**Michel MEUNIER**  
Electrical Engineering Dpt.  
ECOLE SUPERIEURE D'ELECTRICITE  
91190 Gif-sur-Yvette, FRANCE

**KEY WORDS**  
Transformer ; Modeling ; Simulation ; Winding faults ; EMTP ; Leakage

**ABSTRACT**  
This paper deals with a method of modeling internal faults in a power transformer. The method leads to a model which is entirely compatible with the EMTP software. It enables simulation of faults between any turn and the earth or between any two turns of the transformer windings. Implementation of the proposed method assumes knowledge of how to evaluate the leakage factors between the various coils of the transformer. A very simple method is proposed to evaluate these leakage factors. At last, an experimental validation of the model allows the estimation of its accuracy.

## INTRODUCTION

The development and the validation of algorithms for a digital differential transformer protection require the preliminary determination of a power transformer model [5]. This model must allow to simulate all the situations which will be chosen to study the behaviour of the protection algorithms. In particular, it must allow the simulation of internal faults [4]. This is the aspect of the model that we shall study in this paper.

Study of the algorithms implemented in a transformer protection leads us to simulate a large part of the power network, and not only the transformer itself. The upstream circuit with its lines, cables and grounding system, the power transformer itself, current transformers, potential transformers and a part of the downstream circuit with its grounding system and loads must be taken into account. If the aim is not to finally develop a complete simulation software for electrical transients, the transformer model must absolutely be compatible with a commercially available software ensuring the simulation of the "environment" and the computation management. That's why we have developed a model which is entirely compatible with EMTP.

## I. GENERAL MODELING PRINCIPLES

The basic model used is the one supplied by the BCTRAN routine of the EMTP simulation software.

Based on excitation and short-circuit tests, in positive and zero sequences, this routine computes two matrices $[R]$ and $[L]$ modeling the transformer. In the case of a three-phase transformer with two windings, these matrices are of order 6: see figure 1, where $R_i$ and $L_i$ are the resistance and the self inductance of coil $i$, and $M_{ij}$ is the mutual inductance between coils $i$ and $j$. Note that BCTRAN does not take magnetic asymmetry into account.

$$
[R] = \begin{bmatrix}
R_1 & 0 & 0 & 0 & 0 & 0 \\
0 & R_2 & 0 & 0 & 0 & 0 \\
0 & 0 & R_3 & 0 & 0 & 0 \\
0 & 0 & 0 & R_4 & 0 & 0 \\
0 & 0 & 0 & 0 & R_5 & 0 \\
0 & 0 & 0 & 0 & 0 & R_6
\end{bmatrix}
$$

$$
[L] = \begin{bmatrix}
L_1 & M_{12} & M_{13} & M_{14} & M_{15} & M_{16} \\
M_{21} & L_2 & M_{23} & M_{24} & M_{25} & M_{26} \\
M_{31} & M_{32} & L_3 & M_{34} & M_{35} & M_{36} \\
M_{41} & M_{42} & M_{43} & L_4 & M_{45} & M_{46} \\
M_{51} & M_{52} & M_{53} & M_{54} & L_5 & M_{56} \\
M_{61} & M_{62} & M_{63} & M_{64} & M_{65} & L_6
\end{bmatrix}
$$

*Figure 1*

The BCTRAN routine must clearly be considered as an auxiliary routine of the EMTP itself, and not as a part of the main program. In point of fact, BCTRAN merely computes the elements of the matrices $[R]$ and $[L]$ and makes a file which can be directly read by EMTP. This file $[R,L]$ can then be included in any EMTP input file. The transformer will thus be handled as mutually coupled R,L branches [1] [2].

This document does not aim at validating the BCTRAN routine. All the theoretical details relating to this routine are explained in [3]. Let us therefore assume the accuracy of the 6x6 matrices.

The principle used to model a fault between a coil turn and the earth or between any two turns is to divide the faulty coil.

Figure 2a shows the diagram enabling study of a turn-to-earth fault and figure 2b shows the diagram enabling study of a turn-to-turn fault. In the former case, the transformer can be described with two 7x7 matrices $[R]$, $[L]$; in the latter case, two