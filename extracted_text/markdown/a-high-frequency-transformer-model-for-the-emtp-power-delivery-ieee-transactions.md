IEEE Transactions on Power Delivery,Vol.8,No.3,July 1993

# A High Frequency Transformer Model for the EMTP

A. Morched (SM)

L. Martf (M)

J. Ottevanger8

Ontario Hydro, Canada

Abstract - A model to simulate the high frequency behaviour of a power transformer is presented. This model is based on the frequency characteristics of the transformer admittance matrix between its terminals over a given range of frequencies. The transformer admittance characteristics can be obtained from measurements or from detailed internal models based on the physical layout of the transformer. The elements of the nodal admittance matrix are approximated with rational functions consisting of real as well as complex conjugate poles and zeroes. These approximations are realized in the form of an RLC network in a format suitable for direct use with EMTP. The high frequency transformer model can be used as a stand-alone linear model or as an add-on module of a more comprehensive model where iron core nonlinearities are represented in detail.

Keywords - Transformer, High frequency,Frequency dependence, Electromagnetic transients,EMTP.

## 1. INTRODUCTION

The transformer is probably one of the most familiar components of a power system,but it is also one of the most difficult to model accurately. A recent survey comparing EMTP simulations with field measurements indicates that studies where transformer behaviour has the.greatest influence on the results are those where EMTP simulations tend to be the least accurate1.

To model a transformer in a transient simulation,nonlinear behaviour as well as frequency-dependent effects must be taken into account. Standard EMTP transformer models such as BCTRAN and TRELEG² can accurately reproduce the response of a transformer at the frequency at which the short-circuit and open-circuit tests are made; namely,at power frequency. However, these models do not account for the frequency dependence of copper and iron losses, or the effect of stray capacitances.

The behaviour of the transformer at higher frequencies can be approximated, to some extent, by modelling the distributed stray capacitances along the windings with lumped capacitances connected across the terminals of the transformer. This type of representation cannot reproduce the behaviour of the transformer beyond the first resonance frequencies. The calculation of the capacitances is not straightforward, and it is difficult to obtain accurate values, except for simple transformcr designg³,4.

92 SM 359-O PWRD A paper recommended and approved by the IEEE Transformers Committee of the IEEE Power Engineering Society for presentation at the IEEE/PEs 1992 Summer Meeting，Seattle，WA,July 12-16,1992. Manuscript submitted February 3, 1992;made available for printing May 1,1992.

A substantial number of transformer models have been proposed to date.While it is probably inaccurate to categorize all work done in high frequency transformer modelling， it is convenient to identify two broad trends to describe the model presented in this paper within the context of earlier work.

1） Detailed internal winding models. This type of model consists of iarge networks of capacitances and coupled inductances obtained from the discretization of distributed self and mutual winding inductances and capacitances\$,6. The caiculation of these parameters involves the solution of complex field problems and requires information on the physical layout and construction details of the transformer. This information is not generally available as it is considered proprietary by transformer manufacturers. These models have the advantage of allowing access to internal points along the winding, making it possible to assess internal winding stresses. In general, internal winding models can predict transformer resonances but cannot reproduce the associated damping. This makes this class of models suitable for the calculation of initial voltage distribution along a winding due to impulse excitation, but unsuitable for the calculation of transients involving the interaction between the system and the transformer. Purthermore, the size of the matrices involved (typically 10O x 100 or larger) makes this kind of representation impractical for EMTP system studies.

2) Terminal models. Models belonging to this class are based on the simulation of the frequency and/or time domain characteristics at the terminals of the transformer by means of complex equivalent circuitsorotherclosed-form representations7-11． These "terminal" models have had varying degrees of success in reproducing the frequency behaviour of single-phase transformers accurately. The main drawback of the methods proposed to date appears to be that they are not sufficiently general to be applicable to three-phase transformers.

The high-frequency transformer model described here belongs to the class of models where the frequency dependent response at the terminals of the transformer is reproduced by means of equivalent networks. Unlike carlier frequency-dependent transformer models, the new model can simulate any type of multi-phase,multi-winding transformer as long as its frequency characteristics are known either from measurements or from calculations based on the physical layout of the transformer. The generation of the paramcters for the model is automatic,and it does not require special skills on the part of the user.This model has been developed and implemented at Ontario Hydro as part of a new and comprehensive transformer model sponsored by the EMTP Development Coordination Group - DCG for the DCG/EPRI version of the EMTP.Although originally developed ag a high-frequency representation, this model can also be used as a stand-alone linear model, if the frequency characteristics of the transformer are known over a sufficiently broad frequency range.

## 2.OVERVIEW

Consider a multi-phase,multi-winding transformer. The nodal equations which relate the voltages and currents at the accessible terminals of the transformer can be expressed as

$$
[ Y ] [ V ] \ = \ [ I ]\tag{1}
$$

where the nodal admittance matrix [Y] is complex, symmetric,and frequency dependent. In a three-phase system, equation (1) can be expressed as

$$
\begin{array} { r } { \left[ Y _ { 1 1 } \quad Y _ { 1 2 } \quad \ldots \quad Y _ { 1 n } \right] \left[ V _ { 1 } \right] \quad \ldots \quad \left[ I _ { 1 } \right] } \\ { \left[ Y _ { 2 1 } \quad Y _ { 2 2 } \quad \ldots \quad Y _ { 2 n } \right] \left[ V _ { 2 } \right] } \\ { \vdots \quad \vdots \qquad \vdots } \\ { \left[ Y _ { m l } \quad Y _ { m 2 } \quad \ldots \quad Y _ { \mathrm { m u l } } \right] \left[ V _ { n } \right] \quad \ldots \quad \left[ I _ { n } \right] } \end{array}\tag{2}
$$

$$
[ Y _ { \psi } ] \ = \left[ \begin{array} { l l l } { y _ { \psi , m } } & { y _ { \psi , m } } & { y _ { \psi , m } } \\ & & { } \\ { y _ { \psi , b , m } } & { y _ { \psi , b , b } } & { y _ { \psi , b , m } } \\ & & { } \\ { y _ { \psi , m } } & { y _ { \psi , c b } } & { y _ { \psi , c c } } \end{array} \right]\tag{3}
$$

where $\mathbf { \Pi } [ \mathbf { Y _ { i j } } ]$ is a 3×3 sub-matrix and m is the number of three-phase terminals under consideration. For example, the [Y] matrix for a two-winding, three-phase,Y-Y transformer with grounded neutrals would be of order six,with 3m $\cdot ( 3 \mathbf { m } + 1 ) / 2 = 2 1$ distinct elements. The elements of the nodal admittance matrix can be obtained from measurements,or they can be calculated from a detailed winding model over a given frequency range.

The basic idea behind the new transformer model is to produce an equivalent network whose nodal admittance matrix matches the nodal admittance matrix of the original transformer over the frequency range of interest. Such representation would correctly reproduce the transient response of the transformer at its terminals. Consider then the multi-phase network shown in Figure 1. This network will be referred to as a multi-terminal T-equivalent. The parameters of this circuit can be calculated from its nodal admittance matrix using the well-known relationships

$$
[ Y _ { i i , \kappa } ] = \sum _ { j = 1 } ^ { m } [ Y _ { i j } ]\tag{4}
$$

and

$$
[ Y _ { i j , \times } ] = - [ Y _ { i j } ]\tag{5}
$$

![](images/0f242b97b7af90ac923c393d4b93e9a610074c8fb9b3d0fdd5b6675949035cdc.jpg)  
Fig. 1: Single-line diagram of a multi-terminal x-equivalent.

The elements of $\mathbf { [ Y _ { i j , x } ] }$ are approximated with rational functions which contain real as well as complex conjugate poles and zeroes. The rational functions can then be realized with RLC networks which can be combined using (4) and (5) to produce the parameters of the equivalent r-circuit.

![](images/9a830c251dbc8db63a3686f6003947dcaf0fe164f2dd50f769aaaecde8dd6f9f.jpg)  
Fig: 2: Structure of an RLC module.

A typical RLC network used in the approximation of the elements of $\mathbf { \Pi } \mathbf { \Pi } \mathbf { \Pi } \mathbf { \Pi } \mathbf { \Pi } \mathbf { \Pi } \mathbf { \tilde { Y } } _ { \mathbf { \tilde { \Pi } } } \mathbf { \Pi } \mathbf { \tilde { d } } \mathbf { \Pi } \mathbf { \tilde { \Pi } }$ is shown in Figure 2. The general structure of these RLC networks reflects the known frequency characteristics of the admittance functions of a transformer:

Inductive behaviour at low frequencies which includes frequency dependent effects due to skin effect in the windings and iron core eddy current losses. These are simulated by the RL branches.

Series and parallel resonances from mid to high frequencies caused by winding-to-winding and winding-to-ground stray capacitances. These are reproduced by the RLC branches.

·Predominantly capacitive behaviour at high frequencies, represented by the single RC branch.

## 3. PRACTICAL CONSIDERATIONS

The transformer model must be sufficiently robust to produce consistent and numerically stable equivalent networks even when data are obtained from noisy or inconsistent measurements. To this effect, the following steps are taken:

·Fitting the elements of [Yj] and calculating $\mathbf { \Gamma } [ \mathbf { Y _ { i , x } } ]$ by adding the fitted functions using (4), instead of fitting $\mathbb { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf \Lambda } } } } } } } } } } \mathbb { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \Lambda } } } } } } } } } \mathbb { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \Lambda } } } } } } } } \mathbb { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \Lambda } } } } } } } \mathbb { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \Lambda } } } } } } }$ directly.

Averaging the diagonal and off-diagonal elements of $\mathbf { [ Y _ { \overrightarrow { j } } ] }$ so that [Y] become balanced matrices.

The explicit approximation of the elements $\mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb { \Omega } \mathbb { \mathbf { \Omega } } \mathbb { \mathbf { \Omega } } \mathbb \mathbb { \Omega } \mathbb \mathbb { \mathbf { \Omega } } \mathbb \mathbb { \Omega } \mathbb \mathbb { \mathbf { \Omega } \mathbb \Omega } \mathbb \mathbb \mathbb { \Omega } \mathbb \mathbb \mathbb { \Omega \Omega } \mathbb \mathbb \mathbb \mathbb \mathbb  \Omega \Omega \mathbb \mathbb \Omega \mathbb \Omega \mathbb \Omega \mathbb \mathbb \Omega \mathbb \Omega \mathbb \mathbb \Omega \mathbb \mathbb \Omega \mathbb \Omega \mathbb \mathbb \Omega \mathbb \mathbb \Omega \mathbb \mathbb \Omega \mathbb \Omega \mathbb \Omega \mathbb \mathbb \mathbb \Omega \mathbb \Omega \mathbb \mathbb \Omega \mathbb \mathbb \Omega \mathbb \mathbb \Omega \mathbb \mathbb \Omega \mathbb \mathbb \Omega \mathbb \Omega \mathbb \mathbb \Omega \mathbb \Omega \mathbb \mathbb \Omega \mathbb \mathbb \Omega \mathbb \mathbb \Omega \Omega \mathbb \mathbb \mathbb \Omega \mathbb \mathbb \Omega \mathbb \Omega \mathbb \Omega \mathbb \Omega \mathbb \mathbb \Omega \mathbb \mathbb \Omega \mathbb \Omega \mathbb \Omega \mathbb \Omega \mathbb \mathbb \Omega \mathbb \Omega \mathbb \mathbb \Omega \Omega \mathbb \Omega \mathbb \mathbb \Omega \Omega \mathbb \Omega \mathbb \Omega \mathbb \Omega \Omega \mathbb \Omega \Omega \mathbb \Omega \Omega \mathbb \Omega \mathbb \Omega \Omega \mathbb \Omega \Omega \Omega \mathbb \Omega \Omega \Omega \Omega \Omega \Omega \Omega \mathbb \mathbb \Omega $ ，would result in models of lower order than those obtained by first approximating [Yj] and then adding the resuits. However, it has been found that models obtained by fitting $\mathbb { \Gamma } \mathtt { \Pi } \mathtt { X } _ { \mathtt { i } , \mathtt { + } } ]$ directly may be numerically unstable.

Averaging the diagonal and off-diagonal elements of $\mathbf { [ Y _ { i j } ] }$ results in

$$
[ Y _ { \psi } ] = \left[ \begin{array} { l l l } { y _ { \psi , \alpha } } & { y _ { \psi , \alpha \ b } } & { y _ { \psi , \alpha \ c } } \\ { y _ { \psi , \lambda \ c } } & { y _ { \psi , \lambda \ b } } & { y _ { \psi , \lambda \ c } } \\ { y _ { \psi , \alpha } } & { y _ { \psi , \delta \ c } } & { y _ { \psi , \alpha \ c } } \end{array} \right] \ast \left[ \begin{array} { l l l } { y _ { \psi , \alpha } } & { y _ { \psi , \alpha } } & { y _ { \psi , \alpha } } \\ { y _ { \psi , \alpha } } & { y _ { \psi , \lambda \ c } } & { y _ { \psi , \alpha } } \\ { y _ { \psi , \mu \ n } } & { y _ { \psi , \mu \ n } } & { y _ { \psi , \alpha } } \end{array} \right]\tag{6}
$$

If the sub-matrices of [Y] are balanced, they can be diagonalized by a constant transformation [Q] such that

$$
[ Q ] ^ { - 1 } [ Y _ { \psi } ] [ Q ] = [ Y _ { \psi , \psi = \lambda \psi } ]
$$

$$
[ Y _ { \psi , m o d } ] = \left[ \begin{array} { c c c } { { y _ { \psi , 0 } } } & { { 0 } } & { { 0 } } \\ { { } } & { { } } & { { } } \\ { { 0 } } & { { y _ { \psi , 1 } } } & { { 0 } } \\ { { } } & { { } } & { { 0 } } & { { y _ { \psi , 1 } } } \end{array} \right]\tag{7}
$$

Subscripts s and m in $\textcircled{6}$ stand for "self" and "mutual", respectively; subscripts $\ " \bullet \bullet$ and $\bullet _ { 1 } \bullet$ in (7) stand for the familiar zero and positive sequence components. Matrix [Q] could be any of a number of transformation matrices which diagonalize a balanced matrix. Note that even though each sub-matrix in [Y] can be diagonalized,[Y] itself will not be diagonal. For example, for a three-phase, twowinding transformer

$$
[ Y _ { \mathbf { \mu } \mathbf { \bar { a } } \mathbf { \Lambda } \mathbf { \bar { a } } } ] = { \left[ \begin{array} { l l } { Q ^ { - 1 } } & { 0 } \\ { 0 } & { Q ^ { - 1 } } \end{array} \right] } { \left[ Y _ { \mu \mu } \begin{array} { l l } { Y _ { \mu \alpha } } & { Y _ { \mu \alpha } } \\ { Y _ { \mu \alpha } } & { Y _ { \mu } } \end{array} \right] } { \left[ Q \begin{array} { l l } { \mathbf { \Lambda } } & { 0 } \\ { 0 } & { Q } \end{array} \right] } = { \left[ \begin{array} { l l } { Y _ { \mu \mu , \mathrm { m o d } \mathbf { \Lambda } } } & { Y _ { \mu \alpha , \mathrm { m o d } \mathbf { \Lambda } } } \\ { Y _ { \mu \mu , \mathrm { m o d } \mathbf { \Lambda } } } & { Y _ { \mu , \mathrm { m o d } \mathbf { \Lambda } } } \end{array} \right] }
$$

$$
[ \mathbf { Y _ { \mathrm { s e a d } } } ] = \left[ \begin{array} { l l l l l l l } { \mathbf { y _ { \mathrm { { z } } \mathrm { { z } } , 0 } } } & { 0 } & { 0 } & { \mathbf { y _ { \mathrm { { z } } \mathrm { { z } } } } } & { 0 } & { 0 } \\ { 0 } & { y _ { \mathrm { { z } } \mathrm { { z } } , 1 } } & { 0 } & { 0 } & { y _ { \mathrm { { z } } \mathrm { { z } } , 1 } } & { 0 } \\ { 0 } & { 0 } & { y _ { \mathrm { { z } } \mathrm { { z } } , 1 } } & { 0 } & { 0 } & { y _ { \mathrm { { z } } \mathrm { { z } } , 1 } } \\ { y _ { \mathrm { { z } } \mathrm { { z } } , 0 } } & { 0 } & { 0 } & { y _ { \mathrm { { z } } \mathrm { { z } } } } & { 0 } & { 0 } \\ { 0 } & { y _ { \mathrm { { z } } \mathrm { { z } } , 1 } } & { 0 } & { 0 } & { y _ { \mathrm { { z } } , 1 } } & { 0 } \\ { 0 } & { 0 } & { y _ { \mathrm { { z } } \mathrm { { z } } , 1 } } & { 0 } & { 0 } & { y _ { \mathrm { { z } } , 1 } } \end{array} \right]\tag{8}
$$

Introducing into equation (2) we finally obtain

$$
\begin{array}{c} \begin{array} { r l } { \bigg [ Y _ { H M , \mathrm { n o d } } } & { { } Y _ { H L , \mathrm { n o d } } } \\ { \bigg [ Y _ { L M , \mathrm { n o d } } } & { { } Y _ { L L , \mathrm { n o d } } } \end{array} \bigg ] \bigg [ { \boldsymbol { V } } _ { H , \mathrm { n o o d } } \bigg ] = \left[ \begin{array} { l } { I _ { H , \mathrm { n o o d } } } \\ { I _ { L , \mathrm { n o o d } } } \end{array} \right]  \\ { \boldsymbol { Y } _ { L , \mathrm { n o o d } } } & { { } \boldsymbol { Y } _ { L , \mathrm { n o o d } } } \end{array}\tag{9}
$$

where

$$
\begin{array} { r l } { { [ Q ] ^ { - 1 } V _ { _ { H } } = V _ { _ { B , m o d } } \mathrm { ~ ; ~ } } } & { { [ Q ] ^ { - 1 } I _ { _ { H } } = I _ { _ { H , m o d } } } } \\ { { { } } } & { { { } } } \\ { { [ Q ] ^ { - 1 } V _ { _ { L } } = V _ { _ { L , m o d } } \mathrm { ~ ; ~ } } } & { { [ Q ] ^ { - 1 } I _ { _ { L } } = I _ { _ { L , m o d } } } } \end{array}
$$

The admittances to be approximated with rational functions are now the elements of $\Pi _ { \mathrm { m o d s } } ] ,$ instead of that the elements of $\mathbf { [ Y _ { i j } ] }$ Since the parameters of the positive and negative sequence networks are identical, the problem reduces to the fitting of only m·(m+1) distinct admittance elements,rather than 3m·(3m+1)/2.

Averaging the elements of $\mathbf { \Pi } ^ { \mathbf { \{ Y _ { i j } } } $ to produce balanced matrices has obvious merits from the point of view of computational speed. For example, for a two-winding, three-phase transformer, 6 rather than 21 distinct functions would have to be approximated with RLC networks. Also,the time-step loop calculations in the EMTP are also substantially reduced. Averaging the elements of $\mathbf { \Pi } _ { \mathbf { [ Y _ { i } ] } }$ also adds some robustness and consistency to the raw measurements,and contributes further to the numerical stability of the model. While averaging may,in some instances,mask the effect of legitimate asymmetries in the transformer,the differences observed in the transformers studied appear to be relatively small (see Figure 3).

![](images/f1188e310aadf4bc725be91eeb893c744165128076226ef1bf0e32776f2a195d.jpg)

![](images/539fa4001fa9223340a192aebedee2712cfa326da25a3567353b60d58f6919c6.jpg)  
Fig. 3: Diagonal elements of $\scriptstyle { \mathbf { } } ( { \mathbf { Y } } _ { H / F } ) .$ Solid trace: y H,s' Dashed traces:yHH,aa' yHH,bb, yHH,cc

To validate the transformer model, frequency domain as well as time domain measurements were conducted on a 125 MVA,215/44 kV, three-limbed core-type transformer.The transformer is YYconnected with grounded neutrals at the high and low voltage sides. The transformer has a delta-connected tertiary winding with no accessible terminals.

The effect of averaging the elements of $\mathbf { \Pi } [ \mathbf { Y _ { i j } } ]$ for the transformer indicated above,is ilustrated in Figure 3,where the solid trace corresponds to the averaged functions，and the dashed traces correspond to the raw measurements.

## 4.FITTING PROCESS

The elements of $\scriptstyle \mathbf { [ Y _ { m o d d } ] }$ in (8) are approximated with rational functions given by

$$
Y ( s ) \ : \approx \ : Y _ { _ { a } } ( s ) \ : = \ : Y _ { _ { R L } } ( s ) \ : + \ : Y _ { _ { R C } } ( s ) \ : + \ : Y _ { _ { R L C } } ( s )\tag{10}
$$

$$
Y _ { n l } ( s ) = k _ { o } + \sum _ { j = 1 } ^ { N R } { \frac { k _ { n l , j } } { s - p _ { n l , j } } }\tag{11}
$$

$$
Y _ { p c } ( s ) = \frac { s k _ { p c } } { s - p _ { p c } }\tag{12}
$$

$$
Y _ { R U C } ( s ) = \frac { k _ { R U C } \left( s - \tau _ { o } \right) } { \left( s - p _ { N C } \right) \left( s - p _ { N C } ^ { * } \right) } \cdot \prod _ { i = 1 } ^ { N C - 1 } \left( \frac { \left( s - \tau _ { o } \right) \left( s - z _ { i } ^ { * } \right) } { \left( s - p _ { i } \right) \left( s - p _ { i } ^ { * } \right) } \right)\tag{13}
$$

where k, KRLj'. $\mathbf { k } _ { \mathrm { o } } ,$ $\mathbf { k } _ { \mathbf { R C } }$ and ${ \bf k } _ { \tt R L C }$ are real constants; $\scriptstyle { \mathtt { P a t } }$ and $\mathtt { p _ { R C } }$ are real poles; $\pmb { \gamma _ { 0 } }$ is a real zero; $\pmb { \mathrm { p } _ { \mathrm { i } } }$ and $\mathbf { z }$ are complex poles and zeroes, and $\pmb { p _ { \mathrm { ~ i ~ } } ^ { * } }$ and $\pmb { z _ { \mathrm { ~ i ~ } } ^ { \bullet } }$ are their respective complex conjugates. For the practical example given, the number of real poles NR and the number of complex conjugate poles NC in (11) and (13) are typically 6 and 15, respectively. All poles are confined to the left hand side of the complex plane and s=jω. $\mathbf { Y } _ { \bullet } ( \bullet )$ can be described with the equivalent circuit shown in Figure 2, where $\yen 1$ corresponds to the RL branches, $\gamma _ { \tt R C }$ corresponds to the RC branch and $\scriptstyle \mathbf { Y _ { z u c } }$ corresponds to the RLC branches. The single resistive branch comes from $\pmb { \mathrm { k } } _ { \pmb { \mathrm { o } } }$ in equation (11), and its conductance is normally very small.

Let us now define $\mathbf { f _ { o u t } }$ a8 the frequency where the first parallel resonance of Y(s) occurs (see Figure 4). At frequencies below $\mathbf { f } _ { \infty } ,$ the admittance functions behave as combinations of RL branches without resonances. At frequencics above $\mathbf { f } _ { \mathbf { o w } }$ stray capacitances come into play and a number of resonances are present. Therefore, foran initial estimate of $\mathbf { F _ { s } ( s ) } ,$ ,it is assumed that the region between the first measured data point $\mathbf { f } _ { \mathbf { m i n } }$ and $\mathbf { f _ { o u t } }$ contains real poles only, while the region from $\hat { \mathbf { f } } _ { \mathbf { o u t } }$ to the last measured point $\mathbf { f } _ { \mathbf { m a x } }$ contains complex conjugate pairg only.

![](images/f3b2acdf8b5665b2f2fee980426aaf4978ccb0d39b8cc28b1721484de276c015.jpg)

![](images/dd82d12dc82ff0e3a6f5de6d186f47f6f16b4fbbf20c9960b79e355ace214ef4.jpg)  
Fig. 4: Element $\scriptstyle y _ { B D B , I } .$ Solid trace: raw data; Dashed trace: low frequency model.

The steps followed in the approximation of Y(s) are:

1） Numerical noise in Y(s) is removed. Peaks whose magnitude fall below a user-controlled percentage of the largest peak in Y(s) are dismissed.

2） Initialize $\mathbf { Y _ { R C } } .$ The response of an RC branch is

$$
\begin{array} { r l } { R e \{ Y _ { R C } ( s ) \} } & { = \cfrac { R ( \omega C ) ^ { 2 } } { 1 ~ + ~ ( \omega R C ) ^ { 2 } } } \\ { I m \{ Y _ { R C } ( s ) \} } & { = \cfrac { \omega C } { 1 ~ + ~ ( \omega R C ) ^ { 2 } } } \end{array}
$$

The RC branch represents the asymptotic behaviour of the transformer at very high frequency. To calculate R and $\mathbf { c } .$ it is assumed that for the frequency range of interest wRC $< < 1$ and that the imaginary part of $\mathbf { Y } _ { \mathbf { R C } } = \omega \mathbf { C } .$ The value of C is found by fitting the imaginary part of Y(s) with $\pmb { \omega } \pmb { C }$ in the least squares sense.With C known,R is found by matching $\mathbf { Y _ { R C } }$ to a point on the lower envelope of the real part of $\mathbf { Y ( 8 ) }$ 、This technique is very simple but surprisingly effective: optimization seldom changes this initial estimate by more than five percent.

![](images/be98def690282dce0c15536e4ccbd193ee4de5020c0a98040eb18cba347ea509.jpg)  
Fig. 5: Approximation $\mathcal { o f y } _ { H H , I } .$ Solid trace: fitted function; Dashed trace: raw data.

![](images/4e6920c4b83f1484465aa6b43426386f6a41b7fcdf0c4575e6c163f9360771a9.jpg)  
Fig. 6: Approximation oj $\scriptstyle \mathbf { y } _ { \pmb { L } , \pmb { o } } .$ Solid trace: fitted function; Dashed trace: raw data.

3）Initialize $\pmb { \ Y _ { \mathtt { R L C } } }$ by identifying the local maxima and minima of the magnitude of the real part of Y(s). Each local maximum or peak corresponds to a complex conjugate pole $p _ { 1 } = \alpha _ { 1 } + \mathrm { j } \beta _ { \mathrm { i } }$ and each local minimum or valley corresponds to a complex conjugate zero $z _ { \mathrm { i } } { = } \gamma _ { \mathrm { i } } { + } \mathrm { j } \delta _ { \mathrm { i } } .$ The angular frequency at which a maximum and minimum occurs determines $\pmb { \beta _ { \mathrm { i } } }$ and $\hat { \theta } _ { \mathrm { i } } ~ ( \beta _ { \mathrm { i } } { = } 2 \pi \mathrm { f } _ { \mathrm { p e a k } } , ~ \hat { \delta } _ { \mathrm { i } } { = } 2 \pi \mathrm { f } _ { \mathrm { v a l l e y } } )$ The real parts are arbitrarily initialized to 2.5% of their corresponding imaginary parts. The real zero $\gamma _ { \bullet }$ is initialized to $\gamma _ { \circ } = 2 \pi \mathrm { f } _ { \mathrm { o u t } } .$ The number of poles and zeroes assigned is determined by thc shape of Y(s) and by the tolerance that determines which peaks are considered meaningful.

3) Optimize the initial guess of $\begin{array} { r } { \mathbf { Y } _ { \mathbf { a } } ( \mathbf { s } ) { = } \mathbf { Y } _ { \mathbf { R } \mathbf { c } } { + } \mathbf { Y } _ { \mathbf { R } \mathbf { L } \mathbf { c } } , } \end{array}$ assuming ${ \bf { Y _ { R L } } = 0 , }$ over the frequency range from $\mathbf { f _ { \mathrm { e a t } } }$ to $\mathbf { f } _ { \mathbf { m a x } }$ using a modified Marquardt algorithm12. The error function is defined as the magnitude of the difference function $\mathbf { Y ( s ) } \mathbf { - Y _ { s } ( s ) }$

4）Initialize ${ \bf Y _ { R L } ( s ) }$ from 60 Hz to $\mathbf { f _ { \alpha \infty } }$ using the asymptotic fitting procedure deacribed in the Appendix.This initialization algorithm does not require that the function to be approximated be a minimum phase-shift function in order to produce an accurate initial fit. The default number of poles is four,but this number is under user's control.

5） Optimize the entire function $\mathbf { Y _ { a } ( \mathbf { s } ) }$ from 60 Hz to $\mathbf { f } _ { \mathbf { m a x } }$ using the same optimization algorithm indicated in item 3 above.

During the optimization process,all poles are confined to the left hand side of the complex plane. Zeroes are not so constrained. This often leads to the realization of branches with negative values of R, L and C. Nevertheless, because of the constraints indicated above, these branches still have a positively damped response.

The entire fitting process is fully automatic and no user input or special skills are necessary to initialize it.Some of the fitting parameters can be overridden by the user to control the number of poleg and zeroes of $\mathbf { Y _ { s } ( s ) }$ and to control the desirable error levels in the approximations.

## 5. USAGE AS AN ADD-ON MODULE

When the high frequency model is used as an add-on module of & more complex representation with linear and nonlinear components, the response of the low frequency components $\Upsilon _ { l o w }$ must be subtracted from the measured response $\mathbf { Y } _ { \mathbf { m } \mathbf { w } }$ before itis approximated. In a typical application, the frequency response of the Iow frequency nameplate model (e.g.，BCTRAN or TRELEG), including iron core losses, is subtracted.

The subtraction of the effect of the low frequency models introduces some complications if the difference between their low frequency response and the measurements is not negligible in the transition region around the lowest measured frequency $\pmb { \mathrm { f } } _ { \pmb { \mathrm { m i n } } }$ (see Figure 4). Ideally, an add-on high frequency model should have no effect on the response at power frequency. If the difference at $\mathbf { f } _ { \mathbf { m i n } }$ is too large,no causal rational function will be able to approximate the transition region and still produce a negligible contribution at 60 Hz. In these cases, the approximation in the neighbourhood of $\mathbf { f } _ { \mathbf { m i n } }$ will be somewhat degraded.

When the response of the low frequency model is subtracted from the measured data, the region between 60 Hz and $\mathbf { f _ { m i n } }$ defines a transition area where the magnitude of $\mathbf { Y ( s ) } { = } \mathbf { Y } _ { m w } { \mathbf { - } } \mathbf { Y } _ { \mathbf { l o w } }$ isdetermined by the consistency between measured data and the low frequency model and where the magnitude of Y(s) at 6O Hz should be zero. If the low frequency model were accurate from 60 Hz to $\mathbf { f } _ { \mathbf { m i n } }$ and the measurements were error free, then the magnitude of $\pmb { \mathrm { F } } ( \pmb { \mathrm { s } } )$ would be very small at $\pmb { \mathrm { f } } _ { \mathbf { m } \mathbf { \acute { m } } } .$ The smaller the difference the better the fit around $\mathbf { f } _ { \mathbf { e a t } } .$ If the difference is very large, then is not possible to approximate this transition region accurately and some compromises are necessary，namely，a larger error between $\pmb { \mathrm { f } } _ { \pmb { \mathrm { m i n } } }$ and $\mathbf { f _ { o u t } }$ and a relatively large $\mathbf { Y _ { \bullet } ( \mathfrak { s } ) }$

A high frequency model was developed for the measured transformer as an add-on module to a TRELEG model of the same transformer. Figures 5 and 6 show the approximation of the elements $\mathbf { Y _ { H H , o } } ,$ and $\mathbf { Y _ { L , 1 } }$ produced by the combined model. These illustrate the best and the worst fits,respectively,obtained for this particular transformer.

## 6.TRANSIENT RESPONSE

With the elements of [Y] available in a closed form, inclusion of the high frequency model in the EMTP is conceptually straightforward. Each branch in the equivalent network shown in Figure 1 is represented by a constant conductance matrix in parallel with a past history current source. During a transient simulation，modal voltages and currents are calculated from terminal voltages and the uncoupled sequence networks are solved to produce an updated set of modal history current sources. These current sources are transformed into phase quantities and used by the EMTP for the solution of the system in the next time step.

The approximations generated with the techniques described above, are ultimately combined using equations (1) and (2) to produce the branches of the equivalent sequence representation of the transformer. These networks can be simulated in the EMTP by means of the new FDB (Frequency Dependent Branch) model. This model was designed as a general-purpose tool to simulate multi-phase coupled RLC networks in the EMTP. The type of networks which can be modelled with the FDB model are more general than those required by the high frequency transformer model. In fact, even the EMTP implementation of the FDNE (Frequency dependent Network Equivalent) is a sub-set of the FDB model.

It is not within the scope of this paper to describe the implementation of the FDB model in the EMTP or Ontario Hydro's experience with the new high frequency transformer model. Due to space limitations these topics will have to be part of a separate paper.

To verify the EMTP implementation and to validate the developed model, a comparison between simulated versus measured transients on the same 125 MVA, 215/44 kV unit used earlier was conducted. Figure 7 shows the measured response of the transformer measured on phase 1 of the high voltage terminals when a step voltage is applied on phase 3 of the high voltage terminals. All other terminals are grounded. Figure 8 shows the results of the corresponding EMTP transient simulation. Numerical stability has been verified for this and other similar tests by allowing the simulation to run for extremely long times (several seconds).

![](images/c399afdeb9525ff1ebe7700fb2e88c11e4e21e0e0eee3bb57301a1504e5c08fe.jpg)  
Fig. 7: Step response. Field test.

## 7. CONCLUSIONS

This paper presents a model to simulate the behaviour of a multiphase, multi-winding transformer over a wide frequency range. This model reproduces the behaviour of the transformer by means of combinations of RLC networks that match the frequency response of the transformer at its terminals. The frequency response of the transformer is assumed to be known from measurements,or from calculations with models based on geometry and construction details. Its most important featureg are:

1） It can be used to model multi-winding,multi-phase transformers for which the frequency response is known.

2) It can be used as an add-on module for a more complex transformer repregentation. It can also be used as a stand-alone linear model if the frequency response of the transformer is known over a suficiently wide frequency range.

3）The fitting techniqueg developed to approximate the admittance functions of the transformer produce approximations of exceptional quality.

4）Validation tests performed indicate that the models produced are accurate and numerically stable.

5) The process to generate parameters for the model is completely automatic: no special skills or experience are required from the user.

## Acknowledgements

The authors would like to acknowledge the use of the Marquardt optimization routine from the Harwell Subroutine Library. Also we would like to thank A.Narang from Ontario Hydro's Electrical Research Division for providing the measurements for the transformer used in the numerical examples. Thanks are also due to CEA for permission,on behalf of DCG,to publish this work. Funding for this project was provided by DCG.

![](images/8122bb49a643f3e3b5b78f06afe901be8f5b5a8ddf7e626afa77a12886616508.jpg)  
Fig.8: Step response、 EMTP simulation.

## REFERENCES

[1]J. Skliutas,and J. Panek, "Electromagnetic Transients Program (EMTP)-Field Test Comparisons".EPRI EL-6768,March 1990.

[2] H. W. Dommel, Electromagnetic Transients Program Reference Manual (EMTP THEORY BOOK),Printed by The University of British Columbia, Vancouver B.C., Canada,August 1986, pp.6- 62 - 6-63.

[3]R. C Degeneff, "A Method for Calculating Terminal Models of Single Phase n-winding transformers". Paper No.A 78 539-9 presented at the IEEE PES Summer meeting in Los Angeles,July 1978.

[4]T.Adielson,A. Carison, H. B. Margolis,and J. A. Hallady, "Resonant Overvoltages in EHV Transformers -Modelling and Application",IEEE Transactions on Power Apparatus and Systems, vol.PAS-100,pp.3563-3572,July 1981.

[5] P.I. Fergerstad and T. Henriksen,"Inductances for the Calculation of Transient Oscillations in Transformers",IEEE Transactions on Power Apparatus and Systems, vol. PAs-93,No.2, pp. 500-509, March/April 1974.

[6]R. C. Degeneff, "A General Method for Determining Resonances in Transformer Windings",IEEE Transactionson Power Apparatus and Systems,vol. PAS-96,No.,pp. 423-430,March/April 1977.

[7] R. C.Degeneff,W. S. McNult, W. Neugebauer,J. Panek,M.E. McCallum,and C.C. Honey,"Transformer Response to System Switching Voltages",IEEE Transactions on Power Apparatus and Systems,vol.PAS,No.6,pp.1457-1470,June 1982.

[8]P.T.M. Vaessen,"Transformer Model for High Frequencies", IEEE Transactions on Power Delivery, vol. 3,No. 4, pp. 1761- 1768,October 1988.

[9] Q.Su,R. E. James,and D. Sutanto,"A Z-Transform Model of Transformers for the Study of Electromagnetic Transients in Power Systems",IEEE Transactions on Power Systems,vol.5,No.1,pp. 27-33, February 1990.

[10] A.Keyhani,H. Tesai,and A.Abur，"Maximum Likelyhood Estimation of High Frequency Machine and Transformer Winding Parameters", IEEE Transactions on Power Systems, vol.5, No.1, pp.212-219, January 1990.

[11]A. Keyhani,S．Chua,and S.Sebo，"Maximum Likelyhood Estimation of Transformer High Frequency Parameters from Test Data\*,IEEE Transactions on Power Delivery,vol.6,No.2,pp. 858-865, April 1991.

[12] D. W. Marquardt, "An Algorithm for Least-Square Estimation of Nonlinear Parameters",J. Soc. Indust. Appl.Math,vol.11, No. 2,pp.431-441,June 1963.

[13]J.R.Martf,"Accurate Modelling of Frequency-Dependent Transmission Lines in Electromagnetic Transient Calculations". IEEE Transactions on Power Apparatus and Systems, pp.147-157, January 1982.

[14] L. Martf, "Low-order approximation of Transmission Line Parameters for Frequency-DependentModels".IEEE Transactions on Power Apparatus and Systems, pp.3584-3589,November 1983.

## APPENDIX

To approximate a minimum phase-shift function H(s) with a rational function P(s) that contains only real poles and zeroes which lie in the left hand side of the complex plane, it is sufficient to match the magnitude functions of H(s) and P(s). This is possible because the phase angle of a minimum phase-shift function is uniquely determined by its magnitude function: if {H(s)| and |P(s)l match, their phase angles will also match.

$$
H ( s ) \ : \approx \ : P ( s ) \ : = \ : k _ { o } \prod _ { i = 1 } ^ { N } \frac { ( s \ : - \ : z _ { i } ) } { ( s \ : - \ : p _ { i } ) }
$$

A very effective technique to match the magnitude of a minimum phase-shift function is suggested in [13] and [14]:

1) Subdivide the magnitude function into N equally-spaced segments. These segments define the location of the horizontal asymptotes h, $( \mathbf { i } { = } 1 , { \ldots } , \mathbf { N } { + } 1 )$ of |P(s)|.

2)Place the corresponding vertical asymptotes at the frequency where |H(s)l equals thc geometric mean of two adjacent horizontal asymptotes.

3)The initial location of poles and zeroes is defined by the intersection of vertical and horizontal asymptotes.

4) Optimize the initial location of the poles and zeroes by reducing the error function in the least squares sense.

This technique can be extended to approximate any analytical, nonminimum phase-shift function. The basic premise is that the imaginary part of an analytical function is uniquely determined by its real part. The modified method proceeds as folows:

![](images/156a6aeb9ad859238039665a2fe7fb54b1c0a44dcc9658896017be81d09dcd27.jpg)  
frequency

1) Calculate R(s), where

$$
R ( s ) ~ = ~ \sqrt { R e \{ H ( s ) \} ~ - ~ \overline { { C } } }
$$

where C is an arbitrary constant such that $\mathbb { R } \mathbb { e } \{ \mathrm { H } ( \mathbf { s } ) \} > 0 \forall \omega \ge 0$

2) Use the fitting technique described above to approximate R(s) with R'(s).

3) Calculate the partial fraction expansion of the rational function R'(s)

$$
R ^ { \prime } ( s ) = k _ { o } + \sum _ { i = 1 } ^ { N } \frac { k _ { i } } { ( s - p _ { i } ) }
$$

4) The approximation of H(s) is then given by

$$
H ( s ) \approx k _ { \circ } ^ { \prime } + \sum _ { i = 1 } ^ { N } \frac { k _ { i } / p _ { i } } { ( s - p _ { i } ) }
$$

where $k _ { \delta } ^ { \prime } = k _ { o } + c$

## BIOGRAPHIES

Atef S.Morched (M'77-SM'90) received a B.Sc.in Electrical Engineering from Cairo University in 1964,a Ph.D.and a D.Sc. from the Norwegian Institute of Technology in Trodheim in 1970 and 1972. He has been with Ontario Hydro since 1975 where he currently holds the position of Section Head - Electromagnetic Transients in the Power System Planning Division.

Luis_Martf (M'79) received an undergraduate degree in Electrical Engineering from the Central University of Venezuela in 1979, MASc and PhD degrees in Electrical Engineering in 1983 and 1987, respectively,from The University of British Columbia.He did postdoctoral work in cable modelling in 1987-1988,and joined Ontario Hydro in 1989,where he is currently working in the Analytical Methods & Specialized Studies Department of the Power System Planning Division.

Jan H. Ottevangers received an MSc. in Electrical Engineering from the Delft Institute of Technology in 1956.He has been with Ontario Hydro since 1967 where he is currently working in the Analytical Methods and Specialized Studies Department of the Power System Planning Division.

## Discussion

Q.Su (Monash University, Clayton,Australia):The authors are to be congratulated in having presented a comprehensive high frequency transformer model of equivalent networks.In electrical power systems, the transient overvoltages of high voltage power transformers,either at the terminals or inside the windings,are of great importance for the reliability of electricity supply. The model developed by the authors will be useful for the study of system transients in which the high frequency characteristics of transformer winding are to be considered.

Obviously,the model represented by a number of R,L.C components can easily fit in EMTP programs.For a detailed internal winding model,several hundred components may be used resulting in a large size of matrix impractical for EMTP system studies,as mentioned in the paper.The authors'RLC module in Figure 2 consists of at least 15 components and 12 such modules are used to represent a three-phase, two-winding transformer. It is therefore necessary to simulate each transformer of interest in power system with a network of 180 or more RLC components.Would this be a problem with EMTP system studies?

In my previous papers [1,2],a closed-form transformer high frequency model was presented,as shown in Figure A(a).Extended to the mode form in Figure A(b), the model has also been used for three phase transformers.From my experience,the computing time for system transient studies increases significantly for a transformer represented by RLC networks rather than closed-form models.

Another question concerns the higher frequency response of a transformer under step voltages.The functions in Figures 5 and 6 fit measured data up to about 2Oo kHz and the calculated step voltage response in Figure 8 agrees with the measured in Figure 7.This confirms the fitting accuracy of the authors’method.Could the authors indicate the rise time of the step voltage and the time step interval used for the calculations of the step voltage responses?

## References

[1]Q.Su,R.E. James and D.Sutanto,“A Z-transform Model of Transformers for the Study of Electromagnetic Transients in Power Systems",Co-authored with R.E. James and D.Sutanto, IEEE Transactions on Power System，No.1,Vol.5,1990，pp. 27-33.

[2]Q.Su and T.Blackburn,“Application of Z-Transform Method for Study of Lightning Protection in Electrical Power Systems," Proceedingsof the7th International Symposium on High Voltage Engineering,Dresden,Germany,Aug.26-30,1991,pp.139-142.

![](images/f8492710722a35b22d808a11a087d4919fcec2b9cd687fed646feb83105db9cb.jpg)  
Fig.A A close-form high frequency model for two-winding,(a) single-phase and (b)three-phase lransformers.

Adam Semlyen (University of Toronto):This is an interesting and useful paper as it solves the problem of providing a realistic model for multi-phase transformers for the purpose of EMTP simulations.It has benefited of the authors'expertise and experience in fitting stable circuit models to frequency domain data [A].One of its outstanding features is the modal decomposition they have used:it has not only simplified the problem of fiting but,more importantly,it hasreduced the dynamic size of the model to that of a minimal realization.The following remarks and questions are mainly related to the problem of modal decomposition.

I note that the authors assume that the off-diagonal block $[ Y _ { i j } ]$ can be adjusted to become a balanced matrix.This,of course,implies an approximation. (The central phase may,for instance,have somewhat different parameters than the other two phases.) Then,as a result of the balancing,a real,constant, transformation [Q] can be used to obtain the desired modes．After fiting，the modal approximations are transformed back to the original phase domain.They now correspond to the given matrix [Y] of frequency domain measurements.My first question iswhether a final refinement of the fitted results is performed or contemplated for obtaining a best match with the original set of data,in order to compensate for the approximation made by the initial balancing process?

The transformer connection used in the paper is Y-Y,with the particular feature that the $[ Y _ { i j } ]$ block canin fact be balanced bya small adjustment. This is so because the connection does not produce an internal phase shift.When this is not the case,for instance in the important class of Y-△ or Y-Z (zig-zag) connected transformers,the off-diagonal block $[ Y _ { i j } ]$ has cyclic symmetry.For instance,in one particular Y-△ connection (with an admittance y associated to each phase of the Y-connected winding),we have

$$
{ \big [ } Y _ { 1 2 } { \big ] } = y { \left[ \begin{array} { l l l } { 0 } & { 1 } & { - 1 } \\ { - 1 } & { 0 } & { 1 } \\ { 1 } & { - 1 } & { 0 } \end{array} \right] } , \qquad { \big [ } Y _ { 2 1 } { \big ] } = { \big [ } Y _ { 1 2 } { \big ] } ^ { T }
$$

Eigenanalysis of this matrix leads to the symmetrical component transformation matrix with three,rather two,decoupled modes. Baiancing would yield the zero matrix.An α-type input gives a β-type output and vice versa (as expected,see for instance [B]; thus the (real) Clarke transformation does not result in modal decoupling).Positive or negative sequence voltages result in currents of the same sequence with the expected phase rotation.In the modal domain there is of course no strict symmetry,as reciprocity now implies a rotation in the opposite direction if the voltages are applied to the secondary rather than to the primary winding.

Clearly,transformers with internal phase shifting effects pose more complex problems.Could the authors please elaborate on their thoughts regarding the solution of these problems?

Finally,I wish to reassert my appreciation regarding the merits of this paper and would like to congratulate the authors for their fine contribution.

[A] A.S．Morched，J.H．Ottevangers，and L．Marti，"Multi-Port Frequency Dependent Network Equivalents for the EMTP",IEEE paper no.92 SM 461-4 PWRD,presented at the 1992 IEEE/PES Summer Meeting, in Seattle,WA.

[B] Edith Clarke,"Circuit Analysis of A-C Power Systems,Volume I: Symmetrical and Related Components",John Wiley & Sons,Inc., New York,1943.

Manuscript received July 27，1992.

X.Chen (Department of Electrical Engineering, Seattle University, Seattle,WA):This paper is very impressive in scope and in detail.The authors and their organization must be commended for their contributions to the accurate modeling of the high frequency behavior of multi-winding,multi-phase transformers.The fitting techniques to approximate the admittance functions of a transformer is both novel and practical. This discussor has learned a lot from their paper and the authors'earlier papers on transformer modeling.I would appreciate the authors'comments on the following questions:

(a)I have developed a computer program which can form the inductance matrix for a two-winding,three-phase,multi-legged transformer.

The inductance matrix for the primary winding of an unsaturated three-phase three-legged transformer computed by BC-TRAN (pages XIX-C-15 to 20,ATP Rule Book,1987-1992, BPA) is shown in Eqn. (A).

$$
{ \left( \begin{array} { l l l } { L _ { a a } } & { L _ { a b } } & { L _ { a c } } \\ { L _ { b a } } & { L _ { b b } } & { L _ { b c } } \\ { L _ { c a } } & { L _ { c b } } & { L _ { c c } } \end{array} \right) } = { \left( \begin{array} { r r r r } { 8 7 9 . 7 2 } & { - 4 3 8 . 0 2 } & { - 4 8 3 . 0 2 } \\ { - 4 3 8 . 0 2 } & { 8 7 9 . 7 2 } & { - 4 3 8 . 0 2 } \\ { - 4 3 8 . 0 2 } & { - 4 3 8 . 0 2 } & { 8 7 9 . 7 2 } \end{array} \right) } { \mathrm { ~ H e n r y ~ ( A ) } }
$$

The inductance matrix computed by my program is shown in Eqn.   
(B).

$$
\left( \begin{array} { c c c } { { L _ { a a } } } & { { L _ { a b } } } & { { L _ { a c } } } \\ { { L _ { b a } } } & { { L _ { b b } } } & { { L _ { b c } } } \\ { { L _ { c a } } } & { { L _ { c b } } } & { { L _ { c c } } } \end{array} \right) = \left( \begin{array} { c c c } { { 8 7 9 . 8 0 } } & { { - 5 8 4 . 6 8 } } & { { - 2 9 2 . 1 4 } } \\ { { - 5 8 4 . 6 8 } } & { { 1 1 7 2 . 0 6 } } & { { - 5 8 4 . 6 8 } } \\ { { - 2 9 2 . 1 4 } } & { { - 5 8 4 . 6 8 } } & { { 8 7 9 . 8 0 } } \end{array} \right) ~ \mathrm { H e n r y ~ ( B ) } .
$$

It is striking to note that $L _ { a b }$ is two times greater than $L _ { a c } ,$ and $L _ { b b }$ is 1.33 times greater than $L _ { a a }$ and $L _ { c c } .$ Because of the asymmetry of the iron core of a three-legged,core-type transformer,my work is very possibly correct.If this is the case,then Eqs.(6) to (8) of the authorspaper might not be valid.It is common practice to represent a 'transformer by its sequence impedances for short circuit analysis.To apply the symmetrical components method to an unloaded three-phase core-type transformer is not always valid,even if there is no saturation involved. (b) Figures 7 and 8 of the paper showed the comparison between the computed and measured step response of a 125 MVA,215/44 kV transformer.The applied step voltage is much lower than the rated voltage of the high voltage terminals.The main objective of developing high frequency transformer models is to study transformer overvoltages caused by switching and lightning.Aithough many researchers claimed that magnetic saturation of the core has minor influence on fast transients,and therefore can be disregarded,this discussor is interested in knowing if the authors have compared the results of their model to the field test or measurements for overvoltages caused by a lightning surge on a transmission line which is connected to a transformer and operating at rated voltage.This discussor has a strong opinion that harmonic analysis is valid for linear and slightly nonlinear systems.Whereversevereonlinearityisinvolved,diferential quations should be used and nothing else.

Again,the authors are to be congratulated for their effort in developing a comprehensive transformer model.

Manuscript received August 7,1992.

H.M.Beides and A. P. Sakis Meliopoulos (Georgia Institute of Technology). The authors should be commended for revisiting the problem of power transformer modeling. As it is widely known,a comprehensive and generally acceptable transformer model for transient simulation does not exist. One of the reasons is that transformers come in different designs and configurations and with different parameters of parasitic capacitances，etc.We would appreciate the authors response to the following comments and questions:

Has the proposed modeling method been tested using transformers with tertiary windings? If yes, the authors' comments on the accuracy and performance of the derived models will be appreciated.“What are the effects of hysteresis losses and skin effect on the accuracy of the estimated resistive components of the transformer model?

The method requires measuring the frequency response of the transformers. Is the frequency response dependent on the design of the transformer alone (i.e.two transformers of the same manufacturer and type will have identical frequency response)? If this is not the case, it appears to us that it will be necessary to measure the frequency response of each transformer to be modeled.

Manuscript received August 1l,1992.

R.Malewski(Westmount,Quebec,Canada):This study can serve as an excellent example of successful and realistic approach to modeling of a large HV power transformer complex internal circuit.The authors recognize a necessity of taking measurements of the examined transformer characteristics in order to develop the EMTP model.As an alternative,they refer to the transformer design parameters;these however,are considered proprietary by the manufacturer and not accessible to the utility engineers.

The paper title includes the mention of high frequency,and at the end of paragraph #2 a statement is made on the predominantly capacitive behavior of the windingat high frequencies.This is correct if the $f _ { \mathrm { m a x } }$ is set at some 20O kHz,as indicated in Fig.1.After all,it has been known since the time of Wagner[1] that the“standing wave” type of resonant frequencies is confined to a few hundred kilohertz interval.

![](images/5be8c583e596b46c62a774bb0e656610dfbcf0969315ec741bea0958c7a564e6.jpg)

low voltage winding nested inoide with ande shortd  
![](images/6db719bda992bde8da8159b3c994629b67f87ff5dbee673941d46b2acfcece76.jpg)

![](images/11b336fe9613c5c3a45f74a25a65ff06e0349e977eec7fe1e0f2dfcc08608e70.jpg)  
Fig.1.Transfer function of five first discs of an interleaved HV transformer winding presented at three frequency scales.These transfer functions were deconvoluted in frequency domain from transients recorded on the untanked winding.

A distinctly diferent behavior of typical HV transformer windings starts some 2 to 5 MHz,where the internal disc resonances come to play.It may be of interest to inspect a typical winding transfer function spanning all the four frequency intervals.Such a graph was obtained from an impulse voltage distribution measured along the discs on an untanked medium voltage unit. The transfer function was deconvoluted from thedigitally recorded transients and theapplied (lowvoltage) impulse.First five disccharacteristic is shown in Fig.1at three frequency scales:125kHz,300 kHz and2.8 MHz.Itcan be seen that the interval from some 50o kHz to nearly 2 MHz can be modeled byareal pole circuit,but beyond that limit a different representation is required.

Clearly,thispaperdoes notaddress theisueofvery high frequency phenomena,although they are of practical importance for transformers directly connected to SF6 insulated bus bars [2].

Practical implementation of the EMTP model presented in this paper calls for measurements of the transformer transfer function in the frequency range of at least 20o kHz. Such measurements can not be easily taken on a iarge unit in substation,but the required measured characteristicscan be obtained froman industrial laboratory performing the acceptance test of new transformers.At present,many laboratories use a digital recorder for monitoring the impulse test [3,4].The obtained records are usually processed in order to enhance the efficiency of fault detection.The processing often includes calculation of the frequency spectrum of the output and input impulses,and finding the transformer transfer function as quotient of these two spectra.

An analysis of the transfer function required for the dielectric fault detection,is not pertinent to the study presented by the authors. However,atareduced voltage level,additional recordscan be taken during the impulse test,if requested by the utility purchasing the transformer.Such additional measurements can be included in the test program,on demand of the utility system planning department.An incremental cost of the additional measurement is negligible,since the impulse generator and recording system are anyhow prepared for the acceptance test.

The algorithms for measuring the HV to LV transfer function,and forretrieving the parameters required for modeling can be implemented on existing commercial digital impulse recorders,or a specialized recording and signal procesing system can be developed using the accumulated experience in high frequency measurement of transformer winding characteristics.

## References

[1]Wagner,K.“Das Eindringen einer elektromagnetischen Welle in eine Spule mit Windungkapazitat,”Elektrotechnik und Maschinenbau,1915,p.89.

[2]Muller，W.“Fast Transients in Transformers,”CIGRE SC12, WG12.11 Report presented at the Transformer Colloquim in Graz,1990.

[3]Malewski,R.,Poulin,B.,“Impulse Testing of Power Transformers using the Transfer Function Method,"IEEE Trans.Vol.PWRD-3, 1988,p.476.

[4]Malewski,R.,Gockenbach,E.,aier,R.,Fellmann,K.H.,Claud, A.,“Five Years of Monitoring the Impulse Test of Power Transformerswith Digital Recordersand the Transfer Function Method",CIGRE Paper 12-201,1992.

Manuscript received August 21,1992.

A.Keyhani and T.Tsai (The Ohio State University,Electrical Engr., Columbus, OH):We would like to commend the authors for a wellwrittenpaper and for their effortstodevelopa practical high frequency transformer model for the EMTP.

The essential ingredient of high frequency transformer modeling is torepresent the transformer admittances as frequency dependent nonlinear functions.In general,these transfer functions are nonminimum phase system.Therefore both magnitude and phase of the transfer function are needed touniquelyidentify the transfer function model.In this paper,since only the magnitude data were used for the transfer function identification,the transfer function model had to be modified into a minimum-phase plant.It is our belief that such practice may not be necessary and the phase data of the measured transformer admittances should be used for the transfer function estimation,because by including the phase data in the estimation process does not increase the number of unknown parameters which determines the size of the estimation problem.Furthermore it adds an important constraint on the variation of the estimated parameters.

Another important aspect of the high frequency transfer function estimation is the numerical stiffness problem.This problem becomes more severe if the resonant points are spreaded in a wide frequency range.In general,this problem can be resolved if a proper scaling scheme is adopted during the curve fitting.It would be interesting to know if any frequency scaling was performed or needed for this particular study.

The authors have provided the power industry with a valuable and practical technique for modeling the transformer high frequency dynamics for the EMTP.We would appreciate the authors' comments concerning the questions and issues raised in this discussion.

Manuscript received October 16,1992.

A.S.Morched, L.Marti, and J. Ottevangers:We would like to thank the discussers for their interest and their many relevant questions presented.

Regarding Dr.Su’s questions,we would like to make the following comments: After the admittance functions are approximated with rational functions,they become closed-form representations of the original functions.Expressing the admittance functions in terms of RLC modules is a convenient form of visualization and it does not imply that a number of RLC branches have to be connected explicitly in theEMTP.Inside the EMTP,the fitted functions are modeled with FDB modules.Each n-phase FDB module consists of a constant conductance matrix and a set of past history current sources.Figure I illustrates_the EMTP representation of a two-winding transformer using FDB modules.

Therefore,the presence of a high frequency transformer (HFT) in the EMTP does not increase the size of the nodal admittance matrix of the systemmodeled,and it onlyaddsn entries to the EMTP branch tables for each n-phase FDB module.For example, the transformer shown in Figure I only adds 9 branches to the EMTP branch tables. Additional storage is needed to keep track of the updating of the past history current sources.In broad terms,this additional storage amounts to 2 cells for each complex conjugate pole in (13) and one cell for each real pole in (11) and (i2).

The computational burden of Dr.Su's transformer model should be comparable with that of the HFT model.For a single-phase,two-winding transformer Dr.Su's model requires the approximation of three functions and four numerical convolutions per time step of a transient solution.The HFT model,also requires the approximation of three distinct functions,but only three numerical convolutions per time step are needed.A comparison of the performance of both representations will depend largely on the number of terms needed in the fitting process.

The time step used in the EMTP simulation of the step response shownin Figures7and8 of thepaper,was the sampling rate used in thefield measurement,i.e., O.5 μs.An EMTP step functionwas used inthe simulation(△t rise time).In the feld test,the input step reached 95% of its peak value in 1 μs.

We agree with Messrs Keyhani and Tsai when they indicate that a non-minimum phase shift function cannot be described uniquely with the magnitude function alone.However,any causal function is uniquely defined if its real part is known.In the identification/optimization process described in the paper,both real and imaginary parts are used to compensate for possible inconsistencies in measured data.Frequency scaling is commonly used in the solution of least squares optimization problems.However,its use would not be advantageous within the context of the modified Marquardt optimization algorithm.

![](images/6539cb5231a951e0846731bee5f383de3ba746d46f54842575f8b6c5a015ecc6.jpg)  
Fig.I. Single-line diagram representation of a two-winding transformer with the FDB model.

Messrs Beides and Meliopoulos ask whether the frequency response of a transformer depends on its design alone.We have observed that transformers of the same design and make show essentially the same frequency behaviour.It is unclear to us,at this point in time,how far to generalize these observations.Inabsence of actual measurements,it might be better to use the HFT model of a similar transformer than to use no high frequency model at all.While the transformer used in the paper has a buried delta winding,we_have not yet modeled a deltaconnected tertiary winding explicitly. This requires some special considerations which will be explained in more detail in our response to Prof.Semlyen's questions.Hysteresis and eddy current effects are normally taken into account by dedicated models (e.g.,[il) when the HFT is used as an add-on module.In this case,the HFT model will match the diference between the measured data and the frequency response of the linear portions of these models.

We will now address Dr.Malewski's comments.The choice of 200 kHz as the maximum frequency was based on the simulation needs of the transient simulations for which the transformer model was required.Figure II shows the magnitude of $y _ { h _ { 1 } h _ { 1 } }$ from 400 Hz to 1 MHz. Other than additional poles and zeros and the added computational burden, we do not feel that the extended frequency range presents a problem that the HFT model cannot handle.The graphs shown by Dr. Malewski also suggest to us that frequency range beyond1 MHz does not pose any special problems either.

With regard to the techniques_used to obtain the frequency responses,we feel that direct, low voltage frequency domain admittance measurements are probably simpler,cheaper and more reliable for the purposes of the HFT model.This type of measurements can be made with relative ease in the field.It would probably be difficult to persuade manufacturers to perform all the full scale chopped-wave tests required to obtain all the data required by the HFT model. Nevertheless,Dr.Malewski's measurement techniques could provide an alternative way to obtain data for the HFT model since some of them are normally done in acceptance tests anyway.

Professor Semlyen suggests an adjustment of the final fitted functions to account for phase asymmetries.It is not clear to us how this adjustment could be made after the fitted functions are obtained.It should be possible,however,to choose a real constant transformation matrix other than α,β,o to account for unbalances.This would be roughly the same type of approximationused to model frequency dependent unbalanced lines.Whether this constant transformation matrix would also give acceptable answers at higher frequencies is probably a subject of further research.Another possibility is to approximate each element of the Y matrix.This would not rely on any assumptions of symmetry,but the additional computational burden would be substantial.

Professor Semlyen correctly points out that in the case of Y-D or Y-Z-connections,the off-diagonal $[ Y _ { i j } ]$ sub-matrices do not lend themselves to be approximated by a balanced matrix.Depending on the type of delta connection and node numbering scheme,variations of a cyclic matrix can be obtained.For instance,

$$
\left[ Y _ { i j } \right] = \left[ { \begin{array} { c c c } { y _ { i j , a a } } & { y _ { i j , a b } } & { y _ { i j , a c } } \\ { y _ { i j , b a } } & { y _ { i j , b b } } & { y _ { i j , b c } } \\ { y _ { i j , c a } } & { y _ { i j , c b } } & { y _ { i j , c c } } \end{array} } \right]
$$

$$
\approx y _ { a } ( \omega ) \cdot \left[ \begin{array} { r r r } { 0 } & { { } - 1 } & { { } + 1 } \\ { + 1 } & { { } ~ 0 } & { { } - 1 } \\ { - 1 } & { { } + 1 } & { { } ~ 0 } \end{array} \right]\tag{i}
$$

There are several ways in which this situation can be handled:The most obvious_one isto fall back onthe approximation of every element of[Y].On the other hand,it might be more practical to use a constant transformation matrix [Q] whose elements $q _ { i , k }$ for a n-phase system are given by

$$
q _ { i , k } = \frac { 1 } { \sqrt { n } } e ^ { - j \frac { 2 \pi } { n } \cdot ( i - 1 ) \cdot ( k - 1 ) }\tag{i}
$$

The well-known symmetrical components transformation_matrix is just a special case of the matrix defined by equation (ii).The resulting modal admittance matrix only has two non-zero elements,and these

![](images/4cb45cd18359b50c40547d90c1ae65b9ba790efb76f91568f9415a63273f15dd.jpg)  
Fig. II.Magnitude of $y _ { h _ { I } h _ { I } } .$

![](images/a23060295987d188b7976191c9562bc8be9f27c5933d1c74be9f378fd99a7ef5.jpg)  
Fig. III.Off-diagonal elements of $[ Y _ { H } ] .$

differ only by a constant.For example,

$$
[ Q ] ^ { - 1 } [ Y _ { i j } ] [ Q ] = [ Y _ { m o d a l } ]\tag{ii}
$$

$$
\left[ Y _ { m o d a l } \right] = y _ { a } ( \omega ) \cdot j \sqrt { 3 } \left[ \begin{array} { c c c } { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { - 1 } \end{array} \right]\tag{iv}
$$

In this case,only one admittance function $y _ { a } ( \omega )$ has to be approximated.In the time-step loop of the EMTP the complex algebra does not present a problem because even if intermediate functions are nominally complex, the final phase voltages and currents are always real.In other words,the existing FDB model can easily be modified to account for cyclic symmetric modules.

Professor Chen correctly points out that a multi-legged transformer should show some asymmetry,which would degrade the accuracy of the assumption that the sub-matrices of[Y] are balanced.However, the measurements available to us do not show the severe asymmetry indicated in Prof.Chen's calculations.Figure 3 in the paper shows that the diagonal elements of the high voltage winding block are nearly identical over a wide frequency range.Figure II below,shows the measured off-diagonal elements of the same sub-matrix.

From this plot it can be seen that while one element is indeed different, the unbalance ratio at low frequencies is in the order of 1.2 to 1.3 rather,2.0 as Professor Chen's calculations suggest.Based on these measurements we are inclined to accept the balancing procedure asareasonable simplification.It is clear,however,that the use of modal transformation matrix that accounts for center phase asymmetries would be desirable.Strictly speaking,this transformation matrix would also be frequency dependent.Therefore,further investigation would be needed to find what constant transformation matrix would represent an acceptable compromise over the entire frequency range of interest.

The question of the validity of superimposing linear high frequency behaviour on the nonlinear response due to saturation does not have a simple answer.Short of solving the nonlinear field problem with detailed knowledge of core and winding design,accounting for nonlinearand frequency dependent effects will always involve a certain degree of approximation.If the transformer is unsaturated, high frequency excitation cannot drive the transformer into saturation as the flux produced by a voltage input is inversely proportional to its frequency.If a transient of suffcient magnitude is impressed on a transformer which isalready saturated or near saturation, then superposition is not strictly valid.Onthe other hand,situations where a transient is impressed ona transformer which is already in saturation may not be all that common.It is Ontario Hydro's practice not no operate transformers near saturation because of acoustic pollution requirements.This may contribute to the lack of field measurements that would validate the assumption of superposition under nearsaturation conditions.

## Reference

[i]E.Tarasiewicz,A.S.Morched，A.Narang and E.P.Dick, “Frequency Dependent Eddy Current Models for Nonlinear Iron Cores,”PaperNo.92WM177-6 PWRS,Presented at the IEEE-PES Winter Meeting,New York,Feb.1992.

Manuscript received October 16,1992.