# A modified implementation of the Folded Line Equivalent transmission line model in the Alternative Transient Program

![](images/8d820390b6c6c268c5dd39d2aede4ea5d2297e23061b903d972b2c7a8e1b9588.jpg)

Jaimis S.L. Colqui a,∗, Luis Carlos Timaná b, Pablo Torrez Caballero a,c, Sérgio Kurokawa d, José Pissolato Filho a

a School of Electrical and Computer Engineering, State University of Campinas - UNICAMP, Av. Albert Einstein 400, Campinas, Brazil

b Department of Electronic and Telecommunications Engineering, Catholic University of Colombia, Av. Caracas 46 -13, Bogotá, Colombia

c Research and Development Center in Telecommunications - CPQD, R. Dr. Ricardo Benetton Martins 1.000, Campinas, Brazil

d Department of Electrical Engineering, São Paulo State University - UNESP, Av. Brasil 56, Ilha Solteira, Brazil

## A R T I C L E I N F O

Keywords: Transmission line modeling Electromagnetic transients Folded Line Equivalent EMT-type programs

## A B S T R A C T

This paper proposes a modified implementation of the Folded Line Equivalent transmission line model to represent three-phase transmission lines. The Folded line equivalent decomposes a line into its open circuit and short circuit contributions. We propose an alternative orthogonal matrix to transform single-phase transmission line parameters, voltages, and currents to the Folded Line Equivalent domain. Because the proposed matrix is orthogonal, it can directly represent bidirectional transformations using circuit components in simulation software, such as the ATP-EMTP. First, the circuit implementation of Clarke’s matrix decouples a three-phase transmission line into its modes. Then, the circuit implementation of the proposed matrix decouples each mode into its open circuit and short circuit contributions. This paper proves that the proposed approach outputs similar results as those obtained by the Universal Line Model and the JMarti model in the simulation of transmission lines under open-circuit, energization, and fault conditions. However, because the proposed model does not derive from the method of characteristics, it can run with simulation times greater than the propagation delay of the transmission line. It is shown that the proposed approach outputs accurate results for time steps that are 10%, 100%, 200%, and 400% of the propagation delay of the transmission line. Thus, one major advantage of the proposed approach is that it can be used to reduce runtimes in the representation of short transmission lines in large complex networks by increasing time steps without compromising accuracy.

## 1. Introduction

Frequency-dependent cable and transmission line (TL) models have been widely used in the analysis of electromagnetic transients studies in power systems for fault detection [1], analysis of electromagnetic transients in the frequency domain [2], fault prevention [3], medicine [4], and other applications. These models are developed in the mode domain or directly in the phase domain. For instance, the ATP-EMTP implements the JMarti model, introduced in [5,6]. The JMarti model uses constant transformation matrices to decouple TLs. Constant transformation matrices are valid for ideally transposed TLs and provide good results for non-transposed TLs with vertical symmetry. However, constant transformation matrices do not provide good results for non-transposed asymmetrical TLs or multi-circuit TLs because of the frequency dependence of their components. For these cases, the frequency dependence of the transformation matrix must be taken into account. The Universal Line Model (ULM), introduced in [7], is one of the most accurate and general TL models. The ULM and the JMarti model are fundamentally different. The ULM accurately represents cables and TLs in the phase domain. As a result, many programs such as the PSCAD/EMTDC [8] and the Electromagnetic Transients Program-Restructured Version (EMTP-RV) [9] implement the ULM. Numerous TL models (including the ULM and the JMarti model) had derived from the method of characteristics. Models that had derived from the method of characteristics require (simulation) time steps to be smaller than the propagation delay of the TL. Therefore, the time step used in the simulation of complex power systems is limited to the propagation time of the shortest line. The Folded Line Equivalent (FLE) introduced in [10] addresses this issue. The FLE decomposes the nodal admittance matrix of the TL in two blocks that represent the open-circuit and short-circuit conditions of the TL. The Vector Fitting (VF) algorithm [11] fits rational functions to these blocks and imposes passivity, thus ensuring a stable and passive circuit [12]. The FLE had been applied to non-uniform TLs [13,14], combined with the propagation time to represent TLs [15] and cables [16]. The main advantage of the FLE is that it provides accurate results when the time step is greater than the propagation time of the TL, reducing execution times in the simulation of complex power systems. In contrast, other TL models require smaller time steps and therefore take longer to compute simulations.

This paper introduces a modified version of the FLE (MFLE) and implement it in the ATP-EMTP using circuit elements. The main objective of the proposed model is to accurately represent short TLs in the simulation of large complex networks where the time step of the simulation may not be small enough to be compatible with the propagation time of the shortest TLs. Instead of using the transformation matrix introduced in [10], this paper proposes an orthogonal matrix to transform voltages and currents without altering their length. To represent multiconductor TLs by the MFLE, the line is decoupled by a circuit implementation of Clarke’s matrix. Then each mode is represented by the proposed MFLE. The proposed approach is compared against the ULM implementation of the PSCAD and the JMarti built-in model of the ATP-EMTP. Results show that the proposed approach is accurate and has the following advantages:

• Like the FLE, the MFLE accurately represents the eigenvalues of the nodal admittance matrix of the TL.

• Because the proposed model is based on the FLE, it outputs accurate results when the step size of the simulation is greater than the propagation delay of the TL, effectively reducing simulation runtimes.

• The circuit implementation of the proposed transformation matrix performs a bidirectional transformation using only ideal transformers.

• The proposed model provides a better understanding of mode behavior during high-frequency phenomena because it provides access to mode voltages and currents

• The proposed model is efficient because analyzing three independent modes is simpler than analyzing the entire coupled TL.

• The proposed approach can be implemented using ideal transformers, making it easy to implement in simulation software e.g., EMTP-RV, ATP, and PSCAD/EMTDC.

Since the MFLE derives from the FLE model, it inherits all of the features and limitations mentioned in [10].

## 2. The folded line equivalent transmission line model

In the frequency domain, the nodal admittance matrix $Y _ { \mathrm { n o d } }$ relates voltages ?? and currents ?? at line terminals terminals of the TL of Fig. 1 as follows

$$
{ \left[ \begin{array} { l } { I _ { 1 } } \\ { I _ { 2 } } \end{array} \right] } = Y _ { n o d } { \left[ \begin{array} { l } { V _ { 1 } } \\ { V _ { 2 } } \end{array} \right] }\tag{1}
$$

where ?? and ?? are vectors containing voltages and currents at line terminals 1 and 2. The nodal admittance matrix $Y _ { n o d }$ of an overhead TL is composed of 4 symmetrical matrices as follows

$$
\mathbf { \boldsymbol { Y } } _ { n o d } = \left[ \boldsymbol { Y } _ { p } ~ \mathbf { \boldsymbol { Y } } _ { m } \right] .\tag{2}
$$

In (2), $\boldsymbol { Y } _ { p }$ and $\pmb { Y } _ { m }$ are obtained from the traveling wave formulation of the TL and are given by [17]

$$
\pmb { Y } _ { p } = \pmb { Y } _ { c } \left( \pmb { U } + \pmb { H } ^ { 2 } \right) \left( \pmb { U } - \pmb { H } ^ { 2 } \right) ^ { - 1 }\tag{3a}
$$

$$
Y _ { m } = - 2 Y _ { c } \left( U - H ^ { 2 } \right) ^ { - 1 }\tag{3b}
$$

where ?? is the ??×?? identity matrix, the characteristic impedance matrix $Y _ { c } = Z ^ { - 1 } \sqrt { Z Y }$ , the propagation matrix $\begin{array} { r } { { \cal H } = \exp \left( - \ell \sqrt { Z Y } \right) } \end{array}$ , ?? is the number of phases, ?? is the per-unit-length (p.u.l.) impedance matrix of the TL, ?? is the per-unit-length (p.u.l.) admittance matrix of the TL, and ?? is the length of the line.

A time domain representation of the TL can be obtained by fitting $Y _ { n o d }$ in (1). However, even for simple lines, the representation of the eigenvalues of $Y _ { n o d }$ using fitting techniques is inaccurate [10]. To address this issue, Gustavsen and Semlyen have introduced in [10] the Folded Line Equivalent (FLE). The FLE is an alternative representation of the TL that decomposes $Y _ { n o d }$ into its open circuit admittance $\pmb { Y _ { \mathrm { o c } } }$ and short circuit admittance $\pmb { Y } _ { \mathrm { s c } }$ using a real similarity matrix ?? that is given by

$$
\begin{array}{c} \begin{array} { r } { \pmb { K } = \left[ \pmb { U } \qquad \pmb { U } \right]} \\ { \pmb { U } } & { - \pmb { U } } \end{array}   \end{array}\tag{4}
$$

where ?? is the ??×?? identity matrix. Gustavsen and Semlyen’s approach accurately represents the eigenvalues of $Y _ { \mathrm { n o d } }$

Voltages and currents are transformed to and from the FLE domain as follows

$$
\begin{array} { r l r } { \left[ \boldsymbol { V } _ { 1 } \right] = K \left[ \boldsymbol { V } _ { \mathrm { o c } } \right] , } & { { } } & { \left[ \boldsymbol { I } _ { 1 } \right] = K \left[ \boldsymbol { I } _ { \mathrm { o c } } \right] . } \end{array}\tag{5}
$$

Substitution of (5) in (1) gives

$$
\begin{array} { r } { \bigg [ \frac { I _ { \mathrm { o c } } } { I _ { \mathrm { s c } } } \bigg ] = Y _ { \mathrm { F L E } } \bigg [ \frac { V _ { \mathrm { o c } } } { V _ { \mathrm { s c } } } \bigg ] } \end{array}\tag{6}
$$

where

$$
Y _ { \mathrm { F L E } } = K ^ { - 1 } Y _ { \mathrm { n o d } } \ K = \left[ \begin{array} { c c } { Y _ { \mathrm { o c } } } & { 0 } \\ { 0 } & { Y _ { \mathrm { s c } } } \end{array} \right]\tag{7}
$$

and thus $I _ { \mathrm { o c } } { = } Y _ { \mathrm { o c } } V _ { \mathrm { o c } }$ and $I _ { \mathrm { s c } } { = } Y _ { \mathrm { s c } } \ V _ { \mathrm { s c } }$

In general, the FLE solves voltages and currents in five stages as detailed in the flowchart of Fig. 2:

1. First Stage The real similarity matrix ?? transforms $Y _ { \mathrm { n o d } }$ to $\pmb { Y _ { \mathrm { o c } } }$ and $\pmb { Y } _ { s \mathrm { c } } ;$

2. Second Stage The Vector Fitting (VF) procedure [11] approximates the poles and residues of $\pmb { Y } _ { \mathrm { s c } }$ and $\pmb { Y } _ { \mathrm { o c } }$ . The fitted functions are referred to as $\pmb { Y } _ { \mathrm { s c , f i t } }$ and $\mathbf { \Delta } \mathbf { Y } _ { \mathrm { o c , f i t } } ;$

3. Third Stage Passivity is enforced to $\pmb { Y } _ { \mathrm { s c , f i t } }$ and $\pmb { Y } _ { \mathrm { o c , f i t } }$ by the VF algorithm, ensuring stable functions and circuits [12]. The resulting functions are $Y _ { \mathrm { s c , f i t , p a s } }$ and ?? oc,fit,pas.

4. Fourth Stage The state-space representation of $Y _ { \mathrm { s c , f i t , p a s } }$ and $Y _ { \mathrm { o c , f i t , p a s } }$ are constructed as detailed in [18] and then represented by a Norton equivalent as detailed in [19].

5. Fifth Stage The Norton equivalents of $Y _ { \mathrm { { s c , f i t , p a s } } }$ and $Y _ { \mathrm { o c , f i t , p a s } }$ are transformed to the phase domain using the inverse of the similarity matrix ?? and combined into a single Norton equivalent. The time-domain Norton equivalent is then solved using the trapezoidal rule of integration [10] or recursive convolutions [20].

This paper proposes an alternative transformation matrix ?? that is given by

$$
L = \left[ \begin{array} { c c } { { 1 } } & { { 1 } } \\ { { \sqrt { 2 } } } & { { \sqrt { 2 } } } \\ { { 1 } } & { { - \displaystyle \frac { 1 } { \sqrt { 2 } } } } \end{array} \right] ,\tag{8}
$$

to decouple single-phase TLs into their short-circuit and open-circuit contributions as shown in Fig. 3. The proposed matrix ?? retains all properties of matrix ?? proposed in [10]. However, the implementation of ?? is more convenient. We take advantage of the fact that ?? is orthogonal, i.e., its columns form an orthonormal basis of R2. Therefore, ?? does not alter the length of ?? or ?? in each transformation in (5).

To represent multiconductor TLs in simulation software, the TL is decoupled into its modes using the circuit representation of Clarke’s matrix proposed in [21]. Then, each mode is transformed to its short circuit and open circuit conditions using an arrangement of ideal transformers that represent ?? (Fig. 3).

Note that there is no coupling between the open circuit and short circuit contributions. Each fitted admittance is individually represented by a combination of resistors, inductors, and capacitors [22] or by a Norton equivalent [19]. This paper implements a modified version of the FLE (MFLE) that uses an orthogonal matrix to transform voltages to and from the FLE domain instead of the transformation matrix introduced in [10]. The main benefit of using an orthogonal matrix is that it does not alter the length of voltages and currents. To represent multiconductor TLs, first we show the Clarke’s transformation and its circuit implementation. Then a circuit representation of the proposed orthogonal matrix using ideal transformers is presented. Each open circuit and short circuit contribution is represented using circuit elements. In technical literature, the FLE had only been implemented in MatLab. This paper shows an alternative implementation of the FLE in the ATPDraw/ATP-EMTP using ideal transformers.

![](images/74c2318e0a130c9e3ea51095fc70317772de47a1238e1dae7c44277e49b03aba.jpg)  
Fig. 1. Two port network representation of a transmission line.

![](images/cbf56d9f4fd01690e5ca4abf6ba61803d9cc0756b08fe73f0e3f3f6c1260d33b.jpg)  
Fig. 2. Folded Line Equivalent Flowchart.

## 3. Circuit representation of Clarke’s matrix

A perfectly transposed TL that has its ground wires embedded using Kron’s reduction [23] has a per-unit-length (p.u.l.) impedance ?? and admittance ?? given by

$$
Z = { \left[ \begin{array} { l l l } { Z _ { p } } & { Z _ { m } } & { Z _ { m } } \\ { Z _ { m } } & { Z _ { p } } & { Z _ { m } } \\ { Z _ { m } } & { Z _ { m } } & { Z _ { p } } \end{array} \right] } , \qquad Y = { \left[ \begin{array} { l l l } { Y _ { p } } & { Y _ { m } } & { Y _ { m } } \\ { Y _ { m } } & { Y _ { p } } & { Y _ { m } } \\ { Y _ { m } } & { Y _ { m } } & { Y _ { p } } \end{array} \right] }\tag{9}
$$

where subscripts $p$ and ?? represent the diagonal and non-diagonal elements of each matrix, respectively. Clarke’s matrix $T _ { c l k }$ decouples a perfectly transposed TL into its exact modes irrespective of the line geometry, as shown in Fig. 4 [24]. The parameters of modes ?? and ?? are equal but different from the parameters of mode 0 and are given by

$$
Z _ { \mathrm { m } } = T _ { \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } l k } ^ { T } \ : Z \ : T _ { \mathrm { } \mathrm { } _ { c l k } } = \left[ \begin{array} { c c c } { Z _ { \alpha } } & { \ : \ : \ : 0 } & { \ : \ : 0 } \\ { 0 } & { Z _ { \beta } } & { \ : \ : \ : 0 } \\ { 0 } & { \ : \ : \ : 0 } & { Z _ { 0 } } \end{array} \right] = \left[ \begin{array} { c c c } { Z _ { s } - Z _ { m } } & { \ : \ : \ : 0 } & { \ : \ : \ : 0 } \\ { \ : \ : \ : 0 } & { Z _ { s } - Z _ { m } } & { \ : \ : \ : 0 } \\ { \ : \ : \ : 0 } & { \ : \ : \ : 0 } & { Z _ { s } + 2 Z _ { m } } \end{array} \right]\tag{10a}
$$

$$
Y _ { \mathrm { m } } = T _ { c l k } ^ { - 1 } ~ Y ~ T _ { c l k } ^ { - T } = \left[ { \begin{array} { c c c } { Y _ { \alpha } } & { ~ 0 } & { ~ 0 } \\ { 0 } & { ~ Y _ { \beta } } & { ~ 0 } \\ { 0 } & { ~ 0 } & { Y _ { 0 } } \end{array} } \right] = \left[ { \begin{array} { c c c } { Y _ { s } - Y _ { m } } & { ~ 0 } & { ~ 0 } \\ { ~ 0 } & { ~ Y _ { s } - Y _ { m } } & { ~ 0 } \\ { ~ 0 } & { ~ 0 } & { ~ Y _ { s } + 2 Y _ { m } } \end{array} } \right]\tag{10b}
$$

where

$$
T _ { c l k } = \left[ \begin{array} { c c c } { { \frac { 2 } { \sqrt { 6 } } } } & { { 0 } } & { { \frac { 1 } { \sqrt { 3 } } } } \\ { { - \frac { 1 } { \sqrt { 6 } } } } & { { \frac { 1 } { \sqrt { 2 } } } } & { { \frac { 1 } { \sqrt { 3 } } } } \\ { { - \frac { 1 } { \sqrt { 6 } } } } & { { - \frac { 1 } { \sqrt { 2 } } } } & { { \frac { 1 } { \sqrt { 3 } } } } \end{array} \right] .\tag{11}
$$

In [21], Tavares et al. propose a circuit representation of Clarke’s matrix using an arrangement of ideal two-coil transformers. This arrangement of transformers transforms voltages and currents from the phase domain to the mode domain and vice-versa. Due to its nature, the arrangement can be used in simulation software such as the ATP-EMTP.

The block labeled as transformation matrix in Fig. 4 transforms voltages and currents from the phase domain to the mode domain and vice versa. This block contains the arrangement of ideal transformers of Fig. 5(a) [25], which relates voltages at the left and right terminals.

Fig. 5 shows the arrangement of transformers that represents Clarke’s matrix and its interface. Each ideal transformer represents an element of Clarke’s matrix. $\boldsymbol { T } _ { c l k }$ has eight non-zero elements. Therefore, the circuit of Fig. 5(a) contains eight two-coil transformers. Primary windings are connected in series, whereas secondary windings are connected in parallel.

In Fig. 5, phase voltages are given by

$$
v _ { \mathrm { a } } = v _ { { \mathrm { a } } 1 } + v _ { { \mathrm { a } } 2 } + v _ { { \mathrm { a } } 3 }\tag{12a}
$$

![](images/444fe0212b86c271d0f1eb4f554892831e5374abef7ecf0621f1d56e5cd5af64.jpg)  
Fig. 3. Mode represented by the FLE.

![](images/9d76fd6e79211423f4caca4e948cae660ddd20aa9a46647d686b72531b1d309a.jpg)  
Fig. 4. Representation of a perfectly transposed three-phase transmission line in the mode domain.

![](images/76e4aed134415e5564633c6234e69165ed64532bdd131bbd592859597a6ca8f1.jpg)  
Fig. 5. Representation of Clarke’s matrix (a) using eight ideal two-coil transformers, and (b) its circuit interface in the ATP-EMTP.

$$
v _ { \mathrm { b } } = v _ { \mathrm { b 1 } } + v _ { \mathrm { b 2 } } + v _ { \mathrm { b 3 } }\tag{12b}
$$

$$
i _ { \beta } = i _ { \beta 2 } + i _ { \beta 3 }\tag{13b}
$$

$$
v _ { \mathrm { c } } = v _ { \mathrm { c 1 } } + v _ { \mathrm { c 2 } } + v _ { \mathrm { c 3 } } ,\tag{12c}
$$

(13c)

and mode currents are given by

$$
i _ { z } = i _ { \mathrm { z 1 } } + i _ { \mathrm { z 2 } } + i _ { \mathrm { z 3 } } .
$$

$$
i _ { \alpha } = i _ { \alpha 1 } + i _ { \alpha 2 } + i _ { \alpha 3 }\tag{13a}
$$

The turns ratio and polarity of each transformer come from the magnitude and sign of each element of $\pmb { T } _ { c l k }$ in (11). In matrix form,

![](images/24aa51d3eca400f8b8bd18ee4b5a31f183c89dc70f55b209b9d5a8e0345a5da4.jpg)  
Fig. 6. Representation of the proposed ?? transformation matrix (a) using 4 ideal transformers, and (b) its circuit interface in the ATP-EMTP.

![](images/f330d55bb62c7bfbd7bdca6becb87c314f998079d7792041810b6bf356e07ce1.jpg)  
（(a)

![](images/51119f64544f43705965d8f3c4307239a2bc2bad26325f899b4f44e063d24e1d.jpg)  
(b）

Fig. 7. Representation of the fitted admittance ?? (a) by circuit elements, and (b) ATP’s built-in LIB component.  
![](images/841d1f1520c2baa783ac7962b7e5d0e616493a5ee842389acec66e4d92e0e845.jpg)  
Fig. 8. Implementation of the proposed approach in the ATPDraw.

the circuit of Fig. 5 relates voltages and currents as follows

$$
\begin{array} { r } { \left[ \begin{array} { l } { v _ { a } } \\ { v _ { b } } \\ { v _ { c } } \end{array} \right] = T _ { c l k } \left[ \begin{array} { l } { v _ { \alpha } } \\ { v _ { \beta } } \\ { v _ { z } } \end{array} \right] \qquad ; \qquad \left[ \begin{array} { l } { i _ { \alpha } } \\ { i _ { \beta } } \\ { i _ { z } } \end{array} \right] = T _ { c l k } ^ { - 1 } \left[ \begin{array} { l } { i _ { a } } \\ { i _ { b } } \\ { i _ { c } } \end{array} \right] . } \end{array}\tag{14}
$$

Eq. (14) shows that the transformer arrangement of Fig. 5 transforms voltages and currents from the phase domain to the mode domain and vice-versa.

## 4. Circuit implementation of the modified folded line equivalentfle in the atpdraw

This paper proposes to use ?? in (8) instead of ??, which is used in the original implementation of the FLE [10]. This change does not alter the values of $Y _ { \mathrm { o c } }$ or $Y _ { \mathrm { s c } }$ as shown below

$$
\begin{array} { r } { \boldsymbol { Y } _ { \mathrm { F L E } } = K ^ { - 1 } \boldsymbol { Y } _ { \mathrm { n o d } } \ K = \boldsymbol { L } ^ { - 1 } \boldsymbol { Y } _ { \mathrm { n o d } } \ L = \left[ \begin{array} { c c } { \boldsymbol { Y } _ { \mathrm { o c } } } & { \quad \boldsymbol { 0 } } \\ { \boldsymbol { 0 } } & { \boldsymbol { Y } _ { s c } } \end{array} \right] . } \end{array}\tag{15}
$$

Furthermore, because ?? is orthogonal, it can be represented in the time domain by an arrangement of ideal transformers without changing the length of vectors ?? and ?? as follows

$$
{ \binom { V } { V } } = L \left[ { \binom { V _ { \mathrm { o c } } } { V _ { \mathrm { s c } } } } \right] , \qquad { \binom { I _ { \mathrm { 0 c } } } { I _ { \mathrm { s c } } } } = L \left[ { \binom { I _ { 1 } } { I _ { 2 } } } \right]\tag{16}
$$

Fig. 6 shows the arrangement of transformers that represents (16). Ports 1 and 2 represent the input terminals. Ports OC and SC represent, respectively, the output terminals related to the open-circuit and shortcircuit contributions of the TL, respectively. The primary windings of all transformers are connected to ports 1 and 2, and the secondary windings to ports OC and SC. The turns ratio of all transformers is 1: ${ \sqrt { 2 } } .$ The sign of each element in ?? determines the polarity of its corresponding transformer, e.g., the polarity of T4 is inverted because $L _ { 2 , 2 }$ is negative.

Admittances $Y _ { \mathrm { s c } }$ and $Y _ { \mathrm { o c } }$ are approximated by a rational function ?? defined as

$$
Y ( s ) \approx G ( s ) = \sum _ { k = 1 } ^ { N _ { p } } \left( \frac { r _ { k } } { s + p _ { k } } \right) + d + e s\tag{17}
$$

where $N _ { p }$ is the number of pairs of residues ?? and poles ??, ?? is the optional linear term, ?? is the optional high-frequency asymptotic term, and ?? is the complex frequency variable [11].

A circuit with an admittance equal to ??(??) can be constructed by cascading shunt circuits associated with each of the elements of ??(??). For instance, Antonini proposed the circuit of Fig. 7 [26], which has an admittance equal to ??(??). To guarantee that the equivalent circuit is stable and passive, i.e., that it does not generate energy, ??(??) must comply with the following criteria:

i residues ?? and poles ?? must be real;

ii the optional linear term ?? and the optional high-frequency asymptotic term ?? must be real;

iii poles ?? must be on the left half of the s-plane to ensure stability.

In this paper, we use the built-in LIB component of Fig. 7(b) to represent the synthesized circuit of Fig. 7(a). Writing the data into a LIB file is straightforward. However, to keep this paper short, we did not include this specification.

## 4.1. Our approach: The modified folded line equivalent

To represent three-phase TLs in simulation software, we propose to

• use the circuit of Fig. 5 to transform voltages and currents to the mode domain,

• use the circuit of Fig. 6 to transform voltages and currents from the mode domain to the FLE domain using ??(8) instead of ??(4), and

![](images/62043fdac699b415e75a9d980a6743865011d7ed77fed640058cfd8ab836d815.jpg)  
Fig. 9. Implementation of the FLE/MFLE in the ATP-EMTP.

• represent the open circuit and short circuit admittance of each mode using the circuit of Fig. 7.

One of the most widely accepted software for the simulation of electromagnetic transients is the ATP-EMTP, and its graphical interface, the ATPDraw. To generate results in the ATPDraw:

![](images/0db96c04ba7fb280945363a174027bbe0d096048c729ab5bbc6c57757bd6a26f.jpg)  
Fig. 10. Geometry of the TL used in the simulations.

![](images/3c40541ba4b7a5613c4936946c660721fbb070a025089735335f7afd51341aa8.jpg)  
(a)

![](images/08500d8cda62f67afa8217cb4e6391d4338e7976d64ba3179547bd0420f5ade4.jpg)  
(b)

![](images/511aae60a0378bbf9ce459f0cef4d694921e393e4de343faf022e4e630895c73.jpg)  
(c）  
Fig. 11. Fitting of $Y _ { \mathrm { s c } }$ and $Y _ { \mathrm { o c } }$ (a) mode ??, (b) mode ??, and (c) mode 0.

1. compute the frequency-dependent parameters of the TL ?? and ?? ,

2. transform ?? and ?? to the mode domain,

3. calculate the nodal admittance matrix of each mode,

4. compute the open circuit $Y _ { \mathrm { o c , m o d e } }$ and short circuit $Y _ { \mathrm { s c , m o d e } }$ admittances of each mode using ?? in (8)

5. use the VF algorithm to fit $Y _ { \mathrm { o c , m o d e } }$ and $Y _ { \mathrm { s c , m o d e } }$ to rational functions $G _ { \mathrm { o c , m o d e } }$ and $G _ { \mathrm { s c , m o d e } }$

6. calculate the RLC values of the circuit of Fig. 7 that represent $G _ { \mathrm { o c , m o d e } }$ and $G _ { \mathrm { s c , m o d e } }$

![](images/cc9818ebaa86c66a85dc9b3490ea1b2d4229be0967af1a2abbbdf38763ea42a7.jpg)  
(a)

![](images/a82e157d1a788e60ca16696fa7117679edfe90646d2fe2399d49977cae44d82d.jpg)  
(b)

![](images/439cdc0b082ec9e3243e0d147d1759d8d483a983f208e8397e5ffc93b5d848e6.jpg)  
（c）  
Fig. 12. Eigenvalues of the nodal admittance matrix and their fitting (a) mode ??, (b) mode ??, and (c) mode 0.

7. generate a LIB file containing information about the equivalent circuits, and

8. implement the modified FLE model of Fig. 8 in the ATPDraw.

The flowchart of Fig. 9 shows all the steps mentioned above.

## 5. Results

## 5.1. Line configuration

Fig. 10 shows the line geometry that we used in the simulations. The TL is 300 m long and has a propagation time of approximately 1 μs. We used the LINE CONSTANTS routine of the ATP-EMTP, which gives similar results to the PSCAD/EMTDC, to compute the frequency dependent line parameters of the TL of Fig. 10.

The TL geometry of Fig. 10 has three modes, each represented by an open circuit and short circuit admittance. The vectfit3 (Fast Relaxed Vector Fitting) routine fits $Y _ { \mathrm { s c , m o d e } }$ and $Y _ { \mathrm { o c , m o d e } } \mathrm { t o } G _ { \mathrm { s c } }$ and $G _ { \mathrm { o c } }$ with 20 poles [27]. Fig. 11 shows the open circuit and short circuit admittances of each mode, their fitted functions, and the deviation between them.

One advantage of the FLE is that it can accurately represent the eigenvalues of the nodal admittance matrix. The proposed ?? matrix retains this property, as shown in Fig. 12. Fig. 12 shows the eigenvalues of the nodal admittance matrix, which come from the union of the eigenvalues of $\pmb { G } _ { \mathrm { s c } }$ and ${ \bf { G } } _ { \infty }$ [10]. The vectfit3 algorithm enforces stability by fitting poles located on the left side of the s-plane that come in conjugate pairs [28,29].

We simulate the TL geometry of Fig. 10 when its terminals are connected as shown in Fig. 13 and:

i At 0 ms the TL is energized and left open circuited at the receiving terminal

ii At 4 ms the receiving terminal of the TL is connected to a load iii At 8 ms, we induce a single-phase fault in the receiving end of phase A

## 5.1.1. The JMarti model and the Universal Line Model

In this section, we show that the JMarti model and the ULM output similar results for time steps smaller than the propagation delay of the transmission line. The ULM uses fitting techniques to substitute convolutions with recursive convolutions. Recursive convolutions are computationally easy to solve and their accuracy depends on the quality of the fitting [7,8]. The JMarti model uses fitting techniques to represent the frequency dependence of the line parameters using equivalent circuits and historic current sources [5,6].

We simulate the TL of Fig. 13 using the built-in JMarti model available in the ATP-EMTP and the built-in ULM available in the PSCAD with time steps of 0.1 and 1 μs. Phases a, b, and c are respectively shown in red, blue, and green. Each combination of TL model and time step uses different markers. In general, the The JMarti model and the ULM provide similar results as long as the time step is less than the propagation time of the TL (1 μs).

Figs. 14–16 show the voltages at the receiving terminal and currents at the sending terminal of the TL right after the line is energized, a load is connected, and a single-phase fault occurs, as shown in Fig. 13. Overall, Figs. 14–16 show that the JMarti model and the ULM provide similar results and are not affected by the time step as long as this time step is shorter than the propagation time of the TL. Therefore, any simulation that includes the 300 m TL geometry of Fig. 10 has to run with time steps smaller than 1 μs, considerably increasing execution times in the simulation of complex networks that contain longer TLs.

![](images/6e76a5ab684a30d8af402c5b561215e82310acc4d9dcbfa47256e40de0c79302.jpg)  
Fig. 13. Transmission line used in the simulations.

![](images/8b17f1b9324cc8993450ce61574efa1d12886674691d546505f5c76663194b05.jpg)  
(a)

![](images/94db576f1f7c81df7688c43405707885f149c47a19e5448549eefff388c525a4.jpg)  
(b)

Fig. 14. Simulation results obtained using the JMarti model and the ULM right after the line is energized and left open-circuited: (a) voltages at the receiving terminal and (b) currents at the sending terminal.  
![](images/16e09f2a2dd179cca8286c50b0d4c3d4fcacefa8a63990e7e870c5d9ac35a83a.jpg)  
(a)

![](images/2ccd68a248d52ef61f0c900b60653a350a6df4412be3098feac09ade9e080033.jpg)  
(b)  
Fig. 15. Simulation results obtained using the JMarti model and the ULM right after a load is connected to the line: (a) voltages at the receiving terminal and (b) currents at the sending terminal.

## 5.2. The ULM vs our approach

Considering that the ULM and the JMarti model give similar results and, to keep plots simple, we only compare the proposed MFLE to the ULM. Figs. 17–19 show the voltages at the receiving terminal and currents at the sending terminal of the TL right after the line is energized, a load is connected, and a single-phase fault occurs, as shown in Fig. 13.

Figs. 14–19 show that the proposed MFLE outputs similar results with time steps equal to 10%, 100%, 200%, and 400% of the propagation delay of the TL. All the results obtained by the MFLE are similar to those obtained by the ULM with a time step of 10% of the propagation delay of the TL. Note that the ULM requires (simulation) time steps to be smaller than the propagation delay of the TL. Therefore, one major advantage of using the proposed MFLE is that the time step of the simulation can be increased without compromising accuracy, significantly reducing runtimes.

![](images/3a1ae09b0d9dbac85f88159c4a887ebae73c58a01f78f765c02e64e185757ffa.jpg)  
(a)

![](images/15ea3f51794e7be0ec904dbf2099eda0fd292ac47b34ea0a0f42dfd0553870dc.jpg)  
(b)

Fig. 16. Simulation results obtained using the JMarti model and the ULM right after a single-phase fault occurs: (a) voltages at the receiving terminal and (b) currents at the sending terminal.  
![](images/f812c5a720705040baf41acfa3c4ecfaeab01d391f2f53bd5f0a3084b2a9726c.jpg)  
(a)

![](images/22cc1f307e3e7789569360087eadc6d6a0d7fdf4c880a965cbd797fd8cc2b289.jpg)  
(b)

Fig. 17. Simulation results obtained using the ULM and the proposed MFLE for various time steps right after the line is energized and left open-circuited: (a) voltages at the receiving terminal and (b) currents at the sending terminal.  
![](images/45fb610ab61000be9c2382861cc4075b33bfcbb3c7c9dee21c4c1fb40745be67.jpg)  
(a)

![](images/68749f96e60a5019e2dda7d68649a5d880829be7083c4493b98f321ec94836a7.jpg)  
(b)  
Fig. 18. Simulation results obtained using the ULM and the proposed MFLE for various time steps right after a load is connected to the line: (a) voltages at the receiving terminal and (b) currents at the sending terminal.

## 5.3. Error

Table 1 shows the normalized root-mean-square deviation (NRMSD) between the ULM, the JMarti model, and the proposed model in Figs. 14–19. For comparison purposes, the ULM computed with a time step of 0.1 μs is used as reference for all figures. The NRMSD is given

by

$$
\mathrm { N R M S D } = \frac { \sqrt { \frac { 1 } { N } \sum _ { i = 1 } ^ { N } \left( y _ { P M , i } - y _ { \mathrm { U L M } } \right) ^ { 2 } } } { \operatorname* { m a x } \{ y _ { \mathrm { U L M } } \} - \operatorname* { m i n } \{ y _ { \mathrm { U L M } } \} }\tag{18}
$$

![](images/b4d1d5a9a6a3c340b572b861e1b057f33bed01f134feb2db8eb2ea839bb58546.jpg)  
(a)

![](images/98273005da578f26af7085b164eedbcf39620202999e30ee3c12313da53eb48c.jpg)  
(b)  
Fig. 19. Simulation results obtained using the ULM and the proposed MFLE for various time steps right after a single-phase fault occurs: (a) voltages at the receiving terminal and (b) currents at the sending terminal.

NRMSD of the voltage and current curves obtained with the JMarti model and the MFLE with respect to the voltage and current curves obtained with the ULM computed with a time step of 0.1 μs.
<table><tr><td colspan="4">Voltage</td><td colspan="4">Current</td></tr><tr><td>Fig.</td><td>Phases</td><td>At</td><td>NRMSD</td><td>Fig.</td><td>Phases</td><td>At</td><td>NRMSD</td></tr><tr><td rowspan="4">14(a)</td><td rowspan="2">1</td><td>0.1 μs</td><td>0.004</td><td rowspan="4">14(b)</td><td rowspan="2">1</td><td>0.1 μs 1 μs</td><td>0.005</td></tr><tr><td>1 μs</td><td>0.007</td><td></td><td>0.006</td></tr><tr><td rowspan="2">2&amp;3</td><td>0.1 μs</td><td>0.003</td><td rowspan="2">2&amp;3</td><td>0.1 μs</td><td>0.005</td></tr><tr><td>1 μs</td><td>0.007</td><td>1 μs</td><td>0.007</td></tr><tr><td rowspan="4">15(a)</td><td rowspan="2">1</td><td>0.1 μs</td><td>0.006</td><td rowspan="4">15(b)</td><td rowspan="2"></td><td>0.1 μs</td><td>0.004</td></tr><tr><td>1 μs</td><td>0.007</td><td>1 μs</td><td>0.005</td></tr><tr><td rowspan="2">2&amp;3</td><td>0.1 μs</td><td>0.005</td><td rowspan="2">2&amp;3</td><td>0.1 μs</td><td>0.004</td></tr><tr><td>1 μs</td><td>0.006</td><td>1 μs</td><td>0.006</td></tr><tr><td rowspan="4">16(a)</td><td rowspan="2">1</td><td>0.1 μs</td><td>0.001</td><td rowspan="2">16(b)</td><td rowspan="2">1</td><td>0.1 μs</td><td>0.001</td></tr><tr><td>1 us</td><td>0.001</td><td>1 us</td><td>0.001</td></tr><tr><td rowspan="2">2&amp;3</td><td>0.1 μs</td><td>0.005</td><td rowspan="2"></td><td rowspan="2">2&amp;3</td><td>0.1 μs</td><td>0.004</td></tr><tr><td>1 μs</td><td>0.002</td><td>1 μs</td><td>0.002</td></tr><tr><td rowspan="8">17(a)</td><td rowspan="4">1</td><td>0.1 μs</td><td>0.003</td><td rowspan="6">17(b)</td><td rowspan="4">1</td><td>0.1 μs</td><td>0.004</td></tr><tr><td>1 μs</td><td>0.004</td><td>1 μs</td><td>0.004</td></tr><tr><td>2 us</td><td>0.004</td><td></td><td></td><td>0.005</td></tr><tr><td>4 μs</td><td>0.005</td><td></td><td>2 μs 4μs</td><td>0.005</td></tr><tr><td rowspan="4">2&amp;3</td><td>0.1 μs</td><td>0.003</td><td rowspan="4"></td><td></td><td>0.1 μs</td><td>0.003</td></tr><tr><td>1 μs</td><td>0.003</td><td>2&amp;3</td><td>1 μs</td><td>0.004</td></tr><tr><td>2 μs</td><td>0.004</td><td rowspan="2"></td><td>2 us</td><td>0.005</td></tr><tr><td>4 μs</td><td>0.005</td><td>4 μs</td><td>0.005</td></tr><tr><td rowspan="8">18(a)</td><td rowspan="4">1</td><td>0.1 μs</td><td>0.005</td><td rowspan="6">18(b)</td><td rowspan="4">1</td><td>0.1 μs</td><td>0.006</td></tr><tr><td>1 us</td><td>0.006</td><td>1 μs</td><td>0.006</td></tr><tr><td>2 μs</td><td>0.006</td><td></td><td>2 μs</td><td>0.007</td></tr><tr><td>4 μs</td><td>0.007</td><td></td><td>4 μs</td><td>0.008</td></tr><tr><td rowspan="4">2&amp;3</td><td>0.1 μs</td><td>0.006</td><td rowspan="4"></td><td>0.1 μs</td><td></td><td>0.006</td></tr><tr><td>1 μs</td><td>0.006</td><td>2&amp;3</td><td>1 μs</td><td>0.007</td></tr><tr><td>2 μs</td><td>0.007</td><td></td><td>2 μs</td><td>0.007</td></tr><tr><td>4 μs</td><td>0.007</td><td></td><td>4 μs</td><td>0.008</td></tr><tr><td rowspan="8">19(a)</td><td rowspan="4">1</td><td>0.1 μs</td><td>0.001</td><td rowspan="6">19(b)</td><td rowspan="6">1</td><td>0.1 μs</td><td>0.002</td></tr><tr><td>1 us</td><td>0.002</td><td>1 μs</td><td>0.002</td></tr><tr><td>2 us</td><td>0.002</td><td></td><td>2 μs</td><td>0.003 0.004</td></tr><tr><td>4 μs</td><td>0.004</td><td rowspan="4"></td><td>4 μs</td><td></td></tr><tr><td>0.1 μs</td><td>0.002</td><td>0.1 μs 1 μs</td><td>0.003</td></tr><tr><td>1 us</td><td>0.003</td><td>2&amp;3</td><td>0.004</td></tr><tr><td rowspan="3">2&amp;3</td><td>2 μs</td><td>0.003</td><td rowspan="3"></td><td>2 μs</td><td></td><td>0.004</td></tr><tr><td>4 μs</td><td></td><td></td><td>4 μs</td><td>0.004</td></tr><tr><td></td><td>0.004</td><td></td><td></td><td></td></tr></table>

## 6. Conclusions

This paper introduces a modified Folded Line Equivalent to represent three-phase TLs considering the frequency dependence of the

TL parameters. We propose to use an alternative orthogonal transformation matrix instead of the original transformation matrix presented in [10]. The proposed matrix does not alter the length of current and voltages vectors and thus allows us to implement a bidirectional transformation in simulation software using ideal transformers.

The Fast Relaxed Vector Fitting algorithm is used to fit the open circuit and short circuit admittances of each mode. We chose the Fast Relaxed Vector Fitting algorithm because it generates complex conjugate pairs of poles located on the left side of the s-plane. The resulting functions are associated with electrical circuits, which are connected to line terminals through the circuit implementation of Clarke’s matrix and the proposed orthogonal matrix.

This paper implements the proposed modified Folded Line Equivalent in the ATP-EMTP. Ideal transformers and the LIB component are used to represent the transformation matrices and the open circuit or short circuit contributions of each mode. The equivalent circuits of the fitted functions can also be inserted into simulation software using RLC components.

Traditional models based on the method of characteristics can only run on simulations where the step size is equal to or less than the propagation time of the shortest TL in the network. This paper showed that the proposed approach outputs similar results as those obtained by the ULM and the JMarti model in the simulation of transmission lines under open-circuit, energization, and fault conditions. The results presented in Figs. 14–19 show that the proposed approach outputs accurate results in simulations where the time step is 10%, 100%, 200%, and 400% of the propagation time of the TL. Thus, the proposed approach can be used to represent short transmission lines in large complex networks to reduce runtimes without compromising accuracy.

## CRediT authorship contribution statement

Jaimis S.L. Colqui: Conception and design of study, Acquisition of data, Analysis and/or interpretation of data, Writing – original draft, Writing – review & editing. Luis Carlos Timaná: Conception and design of study, Acquisition of data, Analysis and/or interpretation of data, Writing – original draft, Writing – review & editing. Pablo Torrez Caballero: Conception and design of study, Acquisition of data, Analysis and/or interpretation of data, Writing – original draft, Writing – review & editing. Sérgio Kurokawa: Conception and design of study, Writing – review & editing. José Pissolato Filho: Conception and design of study, Writing – review & editing.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgments

This study was financed in part by the Coordenação de Aperfeiçoamento de Pessoal de Nível Superior - Brasil (CAPES) - Finance Code 001 and by São Paulo Research Foundation (FAPESP) (grant: 2021/06157-5). All authors approved the version of the manuscript to be published.

## References

[1] A. Saber, H.H. Zeineldin, T.H. El-Fouly, A. Al-Durra, Time-domain fault location algorithm for double-circuit transmission lines connected to large scale wind farms, IEEE Access (ISSN: 21693536) 9 (2021) 11393–11404, http://dx.doi.org/ 10.1109/ACCESS.2021.3049484.

[2] K.K. Challa, G. Gurrala, Development of an experimental scaled-down frequency dependent transmission line model, IEEE Access (ISSN: 21693536) 9 (2021) 64639–64652, http://dx.doi.org/10.1109/ACCESS.2021.3075906.

[3] B. Yang, H. Yu, G. Li, A. Hu, H. Li, Energy storage system control strategy for restraining overvoltage caused by switching non-load power transmission lines, IEEE Access (ISSN: 21693536) 9 (2021) 60215–60222, http://dx.doi.org/ 10.1109/ACCESS.2020.3031903.

[4] M.B. Lodi, N. Curreli, A. Fanti, C. Cuccu, D. Pani, A. Sanginario, A. Spanu, P.M. Ros, M. Crepaldi, D. Demarchi, G. Mazzarella, A periodic transmission line model for body channel communication, IEEE Access (ISSN: 21693536) 8 (2020) 160099–160115, http://dx.doi.org/10.1109/ACCESS.2020.3019968.

[5] Laurent Dubé European EMTP-ATP Users Group e. V, Users guide to models in atp, 1999.

[6] J.R. Marti, Accurate modeling of frequency-dependent transmission lines in electromagnetic transient simulations, IEEE Power Eng. Rev. (ISSN: 0272-1724) PER-2 (1) (1982) 29–30, http://dx.doi.org/10.1109/MPER.1982.5519686,

[7] A.S. Morched, B. Gustavsen, M. Tartibi, A universal model for accurate calculation of electromagnetic transients on overhead lines and underground cables, IEEE Trans. Power Deliv. (ISSN: 08858977) 14 (3) (1999) 1032–1037, http: //dx.doi.org/10.1109/61.772350.

[8] PSCAD-EMTDS, Manitoba HVDC Research Centre, PSCAD-EMTDS, URL https: //hvdc.ca/pscad/.

[9] EMTP-RV, EMTP-RV, URL http://emtp.com.

[10] B. Gustavsen, A. Semlyen, Admittance-based modeling of transmission lines by a folded line equivalent, IEEE Trans. Power Deliv. (ISSN: 08858977) 24 (1) (2009) 231–239, http://dx.doi.org/10.1109/TPWRD.2008.2002960,

[11] S. B. Gustavsen, Rational approximation of frequency domain responses by vector fitting, IEEE Trans. Power Deliv. (ISSN: 08858977) 14 (3) (1999) 1052–1059.

[12] B. Gustavsen, A. Semlyen, Enforcing passivity for admittance matrices approximated by rational functions, IEEE Trans. Power Syst. (ISSN: 08858950) 16 (1) (2001) 97–104, http://dx.doi.org/10.1109/59.910786.

[13] A.C. Lima, R.A. Moura, B. Gustavsen, M.A. Schroeder, Modelling of non-uniform lines using rational approximation and mode revealing transformation, IET Gener. Transm. Distrib. (ISSN: 1751-8695) 11 (8) (2017) 2050–2055, http: //dx.doi.org/10.1049/IET-GTD.2016.1676.

[14] A.C. Lima, F. Camara, J.P.L. Salvador, M.T.C. de Barros, Frequency-dependent equivalent based on idempotent decomposition and grouping, Electr. Power Syst. Res. (ISSN: 03787796) 189 (2020) 106800, http://dx.doi.org/10.1016/j.epsr. 2020.106800.

[15] F. Camara, A.C. Lima, F.A. Moreira, A full frequency dependent line model based on folded line equivalencing and latency exploitation, Electr. Power Syst. Res. (ISSN: 03787796) 154 (2018) 352–360, http://dx.doi.org/10.1016/j.epsr.2017. 08.018.

[16] F. Camara, A.C. Lima, K. Strunz, Multi-scale formulation of admittance-based modeling of cables, Electr. Power Syst. Res. (ISSN: 0378-7796) 195 (2021) 107120, http://dx.doi.org/10.1016/J.EPSR.2021.107120.

[17] A.S. Morched, J.H. Ottevangers, L. Marti, Multi-port frequency dependent network equivalents for the EMTP, IEEE Trans. Power Deliv. (ISSN: 19374208) 8 (3) (1993) 1402–1412, http://dx.doi.org/10.1109/61.252667.

[18] A. Semlyen, B. Gustavsen, A half-size singularity test matrix for fast and reliable passivity assessment of rational models, IEEE Trans. Power Deliv. (ISSN: 08858977) 24 (1) (2009) 345–351, http://dx.doi.org/10.1109/TPWRD.2008. 923406.

[19] B. Gustavsen, H.M.J. De Silva, Inclusion of rational models in an electromagnetic transients program: Y-parameters, Z-parameters, S-parameters, transfer functions, IEEE Trans. Power Deliv. (ISSN: 08858977) 28 (2) (2013) 1164–1174, http: //dx.doi.org/10.1109/TPWRD.2013.2247067.

[20] A. Semlyen, A. Dabuleanu, Fast and accurate switching transient calculations on transmission lines with ground return using recursive convolutions, IEEE Trans. Power Appar. Syst. (ISSN: 00189510) 94 (2) (1975) 561–571, http: //dx.doi.org/10.1109/T-PAS.1975.31884.

[21] M.C. Tavares, J. Pissolato Filho, C.M. Portela, New mode domain multiphase transmission line model applied to transient studies, in: International Conference on Power System Technology, vol. 2, ISBN: 0780347544, 1998, pp. 865–869, http://dx.doi.org/10.1109/ICPST.1998.729208.

[22] B. Gustavsen, Computer code for rational approximation of frequency dependent admittance matrices, IEEE Trans. Power Deliv. (ISSN: 08858977) 17 (4) (2002) 1093–1098, http://dx.doi.org/10.1109/TPWRD.2002.803829.

[23] G. Kron, Tensor analysis of networks, new york, 1939.

[24] E. Clarke, Circuit Analysis of AC Power Systems; Symmetrical and Related Components, vol. 1, Wiley, 1943.

[25] J.S.L. Colqui, L. Timaná, P.T. Caballero, S. Kurokawa, J.P. Filho, Implementation of modal domain transmission line models in the atp software, IEEE Access (2022) 1, http://dx.doi.org/10.1109/ACCESS.2022.3146880.

[26] G. Antonini, Spice equivalent circuits of frequency-domain responses, IEEE Trans. Electr. Compat. 45 (3) (2003) 502–512.

[27] B. Gustavsen, User’s Guide for vectfit3.m (Fast, Relaxed Vector Fitting), SINTEF Energy Research, N-7465 Trondheim, Norway, 2008.

[28] H.M.J. De Silva, A.M. Gole, J.E. Nordstrom, L.M. Wedepohl, Robust passivity enforcement scheme for time-domain simulation of multi-conductor transmission lines and cables, IEEE Trans. Power Deliv. 25 (2) (2010) 930–938, http://dx.doi. org/10.1109/TPWRD.2009.2035916.

[29] S. Boyd, L.O. Chua, On the passivity criterion for LTI n-ports, Circuit Theory Appl. 10 (1982) 323–333.