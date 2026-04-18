# Multi-Port Frequency Dependent Network Equivalents for the EMTP
A. S. Morched (Senior Member) | J. H. Ottevangers | L. Marti (Member)
Ontario Hydro, Ontario, Canada

**Abstract** - A method is developed to reduce large power systems to single and multi-port frequency dependent equivalents. The equivalents consist of simple RLC modules that faithfully reproduce the frequency characteristics of the network. The method is implemented in the EMTP and has been extensively tested at Ontario Hydro. The implementation involves a pre-processor program to generate the model: the Frequency Dependent Equivalent (FDNE), and an EMTP time step loop module to calculate the transient response. The use of the FDNE results in major reductions in computer time and is especially beneficial for multi-case statistical EMTP studies. An example showing the accuracy and efficiency of the FDNE when used to reduce a large 500kV network is presented.

**Keywords** - Network equivalent, Multi-port, Frequency dependence, Electromagnetic transients, EMTP.

## 1. INTRODUCTION
The study of Electromagnetic transients often requires the detailed modelling of complex transmission networks. However, detailed representations may require prohibitive amounts of computer time, especially when statistical analysis is involved. It is, therefore, a common practice to represent in detail only a small portion of the system and to model the rest using equivalent networks.

Until very recently, only simplified equivalents have been used in transient studies. The most common representation consists of simple inductances derived from the short circuit impedances at the terminal buses evaluated at power frequency. A better representation, in terms of frequency response, can be obtained by shunting the power frequency impedances with the equivalent surge impedances of the lines attached to the buses. This produces improved first reflections, but degraded low frequency behaviour, and incorrect steady-state solutions.

Since these representations are only adequate for very simple transient studies, it has been necessary to represent in detail large portions of the system behind the terminal buses. The correct assessment of how much of the system should be modelled explicitly, is as much an art as it is the result of experience.

Efforts to establish rules for the size of the networks to be represented have been made. Notably, the work of the CIGRE Working Group 13.05 [1], which recommends the use of detailed representation of the system up to two buses behind the terminal buses. However, in dense networks with many transmission lines, even a two-bus explicit representation can be computationally prohibitive. If these dense networks also contain many short lines, the two-bus rule may not guarantee the accuracy of the results, and the detailed modelling of larger portions of the system could be required.

The use of the frequency dependent equivalents for power networks goes as far back as the late sixties and early seventies. Pioneering work in this area was conducted by N. Hingorani [2] and A. Clerici [3]. More recent work [5] attempted to establish systematic procedures to generate frequency dependent network equivalents. Morched and Brandwajn [4] proposed an approach to produce single-port equivalents with models that only matched the network admittances at the series resonant frequencies. Do and Gavrilovic [5] proposed a procedure where the component modules used to represent each of the admittance series resonances are selected by inspection, and a least squares method is used to match the network admittances over a range of frequencies. While they presented methods for generating multi-port equivalents, the treatment was not sufficiently general.

This paper describes an efficient method to calculate network equivalent admittances as seen from one or more ports. It describes the extension of the concepts developed in [4] to multi-port equivalents and the improvement of the fitting technique to match the admittances over a wide range of frequencies.

The application of these techniques has resulted in the development of the Frequency Dependent Network Equivalent (FDNE) program and its subsequent implementation in the EMTP. The FDNE can simulate any type of network, and the generation of its parameters is automatic and does not require special skills on the part of the user.

The FDNE is a stand-alone program which uses a description of the network similar to the one used by the EMTP. It evaluates the nodal admittance matrix seen from multi-port terminals over a user-specified frequency range. On output, the FDNE produces a number of modules consisting of RLC branches (in EMTP-compatible format) whose frequency response matches that of the system seen from the terminals.

The FDNE allows the modelling of large portions of the system at a small fraction of the computational cost required to model them explicitly. This results in more reliable simulations as the need to estimate what portion of the system should be modelled in detail becomes less crucial.

## 2. NETWORK COMPONENT MODELS
The first step in the creation of a network equivalent is to build the nodal admittance matrix of the portion of the system to be represented over a given frequency range. Rather than using the EMTP itself to produce frequency scans of the entire network, the admittance matrix is calculated explicitly at 10 frequencies over the entire frequency range; intermediate values of $X$ are calculated by interpolation.

The zero sequence admittance matrices are calculated using $(A.5)$ and $(A.6)$, w