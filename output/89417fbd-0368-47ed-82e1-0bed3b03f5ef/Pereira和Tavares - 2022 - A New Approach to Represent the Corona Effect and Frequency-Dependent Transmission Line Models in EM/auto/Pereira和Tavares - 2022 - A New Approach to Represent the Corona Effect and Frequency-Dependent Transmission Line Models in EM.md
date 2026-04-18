# A New Approach to Represent the Corona Effect and Frequency-Dependent Transmission Line Models in EMT-Type Programs

Thassio Matias Pereira , Graduate Student Member, IEEE, and Maria Cristina Tavares , Senior Member, IEEE

Abstract—This paper presents an accurate and efficient model to represent the corona effect and frequency dependence of line parameters in electromagnetic transient simulations. The new method, named the voltage and frequency dependent line model (VFDLM), can be seen as a more general case of the well-known frequency-dependent (FD) or wideband (WB) line models, wherein the characteristic admittance and propagation function are considered voltage- and frequency-dependent parameters. The time domain traveling wave equations are solved using recursive convolutions and rational approximation through vector fitting (VF). Since the model can be represented by Norton equivalents, it is totally compatible with EMT-type programs. The model is validated through comparisons with three field measurement data available in the literature, and good agreement could be observed between them, showing that the VFDLM is a stable, efficient, and accurate approach to represent the corona effect in EMT-type programs.

Index Terms—Corona effect, transmission line modeling, frequency-dependent line model, EMT-type programs.

## I. INTRODUCTION

E MT-TYPE programs are probably the most widespreadsimulation tools used to predict electric power system behavior under transient phenomena and are extensively used in insulation coordination studies. One of the main advantages of EMT-type programs is the capability to represent transmission lines (TLs) with low computational cost and good accuracy. Since its first version in 1969 [1], several line models have been proposed that can accurately represent the frequency dependence of line parameters [2], [3]. Despite this fact, these currently available models are not able to represent the corona effect directly in the transmission line formulation since the line is modeled as a linear component.

Due to the nonlinear nature of the corona effect, most of the approaches adopted to represent this phenomenon in wave propagation calculations are based on numerical solutions, such as the finite difference time domain (FDTD) [4], [5], finite element method [6], [7], or method of characteristics [8]. However, these approximations are not directly applicable to EMT-type programs since the line terminals cannot be represented by Norton’s equivalents.

The traditional approach to represent the corona effect in EMT-type programs consists of subdividing the TL into linear sections, and at each junction node, a shunt corona branch is placed. This procedure has been adopted in several works over the years and combined with different corona models [9]–[15]. A further improvement is achieved when nonlinear corona branches are implicitly represented, and the solution of the line equations is obtained using a recursive scheme [16], [17]. These approaches have as a common characteristic the fact that the corona effect is decoupled from the transmission line model and externally represented by lumped elements, which in fact is not consistent with the real physical nature of the phenomenon.

More recently, our previous research introduced the idea of a voltage-dependent line model (VDLM) in EMT-type programs [18]. The VDLM consists of a more general case of the Bergeron model, wherein the line capacitance and shunt conductance are modeled as voltage-dependent parameters. In addition to presenting a more realistic approach to the distributed nature of the corona effect, this model can encapsulate the representation of the corona effect directly into the line modeling, resulting in a more robust line model. Despite this fact, the VDLM still did not solve the proper representation of the frequency dependence of line parameters, which is a very important characteristic of fast transient simulations, such as lightning overvoltages.

In this context, the present paper expands the idea of VDLM and presents a voltage- and frequency-dependent line model (VFDLM). To be totally compatible with EMT-type programs, the VFDLM consists of a more general case of the wellestablished frequency-dependent (FD) [2] or wideband (WB) line models [3], with the difference that characteristic admittance and propagation function are taken as both voltage- and frequency-dependent parameters. In addition to representing the real distributed nature of the corona effect, the VFDLM couples the frequency dependence and corona representation directly into the line modeling, constituting a full and very robust line model. The VFDLM was validated through comparisons with three field measurement data available in the literature, and good agreement could be observed between them. Furthermore, the model proves to be a stable, accurate and efficient alternative to represent the corona effect in EMT-type platforms. At the current stage, the VFDLM can only deal with single-phase transmission lines.

![](images/8a619a9bb198bc9e48f8d6fecc6e2e7d4d186bbf8eaa0ece4907480b108df3c6.jpg)  
Fig. 1. Incident and reflected current waves at transmission line ends k and m.

This paper is organized as follows. Section II presents a brief review of WB line models. Section III describes the mathematical formulation of the VFDLM and its respective implementation procedure in EMT-type programs. Validation tests and discussions are presented in Sections IV and V, respectively. Concluding remarks are given in Section VI.

## II. A REVIEW OF WB LINE MODEL

## A. Traveling-Wave Equations

Consider a single-phase overhead transmission line of length l terminated by ends k and m, as shown in Fig. 1. In the frequency domain, the relationship of voltage V and current I along an infinitesimal distance $\Delta x$ of the line can be characterized by the well-known traveling wave Equations (1) – (4), where $Z ( s )$ and $Y ( s )$ correspond to per unit length series impedance and shunt admittance, respectively. Since all the analyses performed in this paper are in reference to single-phase lines, it is important to highlight that the quantities shown in these equations are scalars. Furthermore, uppercase letters represent frequency domain quantities, while lowercase letters indicate their time domain correspondents.

$$
- \ { \frac { d V } { d x } } = Z \left( s \right) \cdot I\tag{1}
$$

$$
- { \begin{array} { l } { { \frac { d I } { d x } } = Y \left( s \right) \cdot V } \end{array} }\tag{2}
$$

$$
Z \ ( s ) = R ( s ) + s L ( s )
$$

$$
Y \ ( s ) = G + s C\tag{3}
$$

(4)

As described in [19], the solution of ordinary differential Equations (1) and (2) can be expressed in terms of the incident and reflected waves at the two-line ends, as shown in (5) – (8). For simplicity, in this paper, only the equations related to the terminal k are presented, and the equations related to the terminal m can be obtained by substituting the subscript k by m. In these equations, $Y _ { c }$ and H are the characteristic admittance and propagation functions, and the subscripts i and r denote the incident and reflected waves, respectively. By observing (5) and Fig. 1, it can be noted that the current at the terminal k relates the voltage $V _ { k }$ and the incident current wave $I _ { k i }$ . The incident current wave $I _ { k i }$ is equal to the reflected wave $I _ { m r }$ propagating

![](images/0a1464f2b98e3ba53269f663a3d1b4e4a310a1286187792e1d5f5aae89217a71.jpg)  
Fig. 2. Norton equivalents for WB line model representation in EMT-type programs.

to end $k ,$ as shown in (6).

$$
I _ { k } = Y _ { c } \cdot V _ { k } - 2 I _ { k i }\tag{5}
$$

$$
I _ { k i } = \textit { H } \cdot I _ { m r }
$$

$$
Y _ { c } = Z ^ { - 1 } \cdot \sqrt { Z \cdot Y }\tag{6}
$$

$$
H _ { \mathbf { \Phi } } = e ^ { - \sqrt { Y \cdot Z } l }\tag{7}
$$

(8)

## B. Time Domain Implementation

Transforming (5) – (8) to the time domain, the products are replaced by convolutions. Furthermore, to interface with EMTtype programs, the traveling wave equations are represented through Norton equivalents, composed of nodal conductance $G _ { S }$ and historical current sources $i _ { h i s t }$ , as shown in Fig. 2. In this system, the terminal voltages $v _ { k }$ and $v _ { m }$ are first calculated by the nodal network solver of the EMT main program and then read by the transmission line subroutine, which calculates the terminal currents according to (9) – (12) [20]. In these equations, $\Delta t$ denotes the integration step, and τ is the TL time delay.

$$
i _ { k } \left( t \right) = G _ { s } \cdot v _ { k } \left( t \right) - i _ { h i s t k } \left( t \right)
$$

$$
i _ { k r } \ ( t ) = i _ { k } \ ( t ) + i _ { k i } ( t )\tag{9}
$$

(10)

$$
i _ { k i } \left( t + \Delta t \right) = H * i _ { m r } \left( t - \tau \right)\tag{11}
$$

$$
i _ { h i s t , k } \ ( t + \Delta t ) = \ Y _ { c } * v _ { k } \left( t \right) - 2 i _ { k i } \left( t + \Delta t \right)\tag{12}
$$

## C. Rational Approximation

To solve the convolutions in (11) and (12), it is convenient to represent the frequency response of $Y _ { c }$ and H through rational functions, as will be better explained in the subsequent section. In ULM [3], this approach is performed directly in the s domain using the vector fitting (VF) technique [21], which is a fast and accurate tool for rational approximation. Thus, $Y _ { c }$ and H are synthetized as shown in (13) and (14), where d is a real constant obtained at the limit of $Y _ { c }$ when $s  \infty ; r _ { i } ^ { Y _ { c } }$ and $p _ { i } ^ { Y _ { c } }$ are the i-th fitted residue and pole of $Y _ { c } ; r _ { i } ^ { H }$ and $p _ { i } ^ { \check { H } }$ are the i-th fitted residue and pole of H; $N _ { p } Y _ { c }$ and $N _ { p } H$ are the fitting order of $Y _ { c }$ and H, respectively.

$$
Y _ { c } \cong d + \sum _ { i = 1 } ^ { N _ { p } Y _ { c } } \frac { r _ { i } ^ { Y _ { c } } } { s - p _ { i } ^ { Y _ { c } } }\tag{13}
$$

$$
H \cong \sum _ { i = 1 } ^ { N _ { p } H } \left( \frac { r _ { i } ^ { H } } { s - p _ { i } ^ { H } } \right) \cdot e ^ { - s \tau }\tag{14}
$$

The fitting procedure of $Y _ { c }$ is simple and straightforward. However, as discussed in [22], to fit the propagation function H using the VF technique, we should extract the time delay before fitting is carried out. With this artifice, the adjustment can be performed with a minimum-phase-shift function and using a low-order fitting. In this sense, several approaches can be applied to extract the time delay of H, which include the use of simpler methods such as Bode’s magnitude phase relation [22] or improved procedures, as described in [23]–[25].

## D. Discrete Recursive Convolutions

With $Y _ { c }$ and H synthesized by rational functions, the solution of (11) and (12) can be obtained using recursive convolutions [26]. In addition to implementing the frequency-to-time domain transformation directly, this technique also provides a simple, fast, and accurate way to solve discrete convolutions and has been adopted by several EMT line models.

To illustrate this technique, consider the calculation of a simple convolution a $( t ) = b ( t ) * c ( t )$ , where $c ( t )$ is the input, and $b ( t )$ is the time domain image of $B ( s )$ , which is a first-order system (one pole fitting), as shown in (15).

$$
B = { \frac { r } { s - p } }\tag{15}
$$

If the solution of the convolution for the previous time step $a ( t - \Delta t )$ is known and the input has a linear variation between $t - \Delta t$ and $t ,$ the solution of $a ( t )$ can be written as [27]:

$$
\textit { a } \left( t \right) = \textit { \alpha } \cdot a \left( t - \Delta t \right) + r \left\{ \lambda \cdot c \left( t \right) + \mu \cdot c \left( t - \Delta t \right) \right\}\tag{16}
$$

where $\alpha , \lambda$ and $\mu$ are known constant coefficients calculated through poles and time step, as shown in (17) – (19):

$$
\alpha = e ^ { p \Delta t }\tag{17}
$$

$$
\lambda = - \frac { 1 } { p } \left( 1 + \frac { 1 - \alpha } { p \Delta t } \right)\tag{18}
$$

$$
\mu = - \frac { 1 } { p } \left( \frac { \alpha - 1 } { p \Delta t } - \alpha \right)\tag{19}
$$

Applying the recursive convolution to solve (11) and (12) and $\mathrm { i f } Y _ { c }$ and H were fitted as in (13) and (14), after some algebraic manipulations, we can obtain the set of equations shown in (20) – (22), which characterizes the implementation of the WB line model in EMT-type programs.

$$
\begin{array} { l } { \displaystyle { G _ { s } = { \mathrm { \it ~ d } } + \sum _ { i = 1 } ^ { N _ { p } Y _ { c } } r _ { i } ^ { Y _ { c } } \cdot \lambda _ { i } ^ { Y _ { c } } } } \\ { \displaystyle { } } \\ { \displaystyle { y _ { c } ^ { ' * } v _ { k } = a _ { Y } \mathrm { \it ~ \Psi } \left( t \right) = \sum _ { i = 1 } ^ { N _ { p } Y _ { c } } \left( \alpha _ { i } ^ { Y _ { c } } \cdot a _ { Y } \left( t - \Delta t \right) \right. } } \\ { \displaystyle { \left. + r _ { i } ^ { Y _ { c } } \cdot \mu _ { i } ^ { Y _ { c } } \cdot v _ { k } \left( t - \Delta t \right) \right) } } \end{array}\tag{20}
$$

(21)

![](images/84431edd1b13e4c612b9dad66bef568e2b7fd385ff2bb20b56e8ea6665fe198e.jpg)  
Fig. 3. Spatial discretization of the line.

$$
\begin{array} { r l } {  { h * i _ { m r } ( t - \tau ) = a _ { H } ( t ) = \sum _ { i = 1 } ^ { N _ { p } H } ( \alpha _ { i } ^ { H } \cdot a _ { H } ( t - \Delta t )  } } \\ & {  + r _ { i } ^ { H } \{ \lambda _ { i } ^ { H } \cdot i _ { m r } ( t - \tau ) + \mu _ { i } ^ { H } \cdot i _ { m r } ( t - \tau - \Delta t ) \} ) } \end{array}\tag{22}
$$

In general, the time delay in (22) will not be an integer multiple of the time step $\Delta t .$ . This problem is circumvented by applying linear interpolation, and the convolution can be performed using one- or two-interpolation segments, as described in [27]. Equations (20) – (22) show that for a time domain implementation, a transmission line can be characterized by the set of parameters $G _ { s } , r _ { i } ^ { Y _ { c } } , \alpha _ { i } ^ { Y _ { c } } , \lambda _ { i } ^ { Y _ { c } } , \mu _ { i } ^ { Y _ { c } } , r _ { i } ^ { H } , \alpha _ { i } ^ { H } , \lambda _ { i } ^ { H } , \ : \overline { { { \mu } _ { i } ^ { H } } }$ and $\tau ,$ which will henceforth be referred simply as time domain implementation parameters (TDIPs). In other words, the TDIP constitutes the set of parameters that must be stored in the computer memory after the line constants are calculated, to be used when the simulation loop starts.

Inside the simulation loop, storage should be performed only for the historical current values, whose minimum number of historical samples that needs to be kept in the memory can be calculated with (23), where BS is the buffer size. The concepts regarding the storage of the TDIP and the buffer size are highlighted because, as will be shown later, the VFDLM makes use of these same techniques.

$$
B S = \left\lfloor { \frac { \tau } { \Delta t } } \right\rfloor + 1\tag{23}
$$

III. A VOLTAGE AND FREQUENCY-DEPENDENT LINE MODEL

## A. Spatial Discretization

To represent the corona effect in any approach based on the transverse electric mode of propagation (TEM), the line must be discretized in short length sections, since in these models the voltage can only be known in the line ends. As better discussed in [18], the appropriate section length should consider that the travel time along each section is a fraction of the period associated with the maximum frequency involved in the analysis. Considering that in lightning overvoltages, the maximum frequency is approximately 1 MHz, the section length should be 100 m or less. In the case of switching overvoltage, however, there are lower frequencies involved in the analysis, and consequently, larger section lengths can be adopted, which are of the order of 10 km to 20 km. Since the VFDLM is based on the TEM, the line must be discretized to the application of this model, as shown in Fig. 3. In this figure, each line section is represented by the VFDLM, wherein the structure of the VFDLM is explained in the next subsection.

## B. Mathematical Modeling of VFDLM

The central idea behind the VFDLM is very simple and based on a pseudo-nonlinear version of the WB line model presented in the previous section. Since the corona effect changes only the shunt parameters, we can rewrite (3) and (4), as shown in (24) and (25), where the capacitance C and shunt conductance G of each line section are now considered nonlinear and voltage-dependent parameters:

$$
Z \ ( s ) = R ( s ) + s L ( s )\tag{24}
$$

$$
\begin{array} { r } { Y \ \left( s , v \right) = G \left( v \right) + s C \left( v \right) } \end{array}\tag{25}
$$

With this modification, the characteristic admittance and propagation function should be rewritten as:

$$
Y _ { c } \left( s , v \right) = Z ^ { - 1 } \left( s \right) \cdot \sqrt { Z \left( s \right) \cdot Y \left( s , v \right) }\tag{26}
$$

$$
H \left( s , v \right) = e ^ { - \sqrt { Y \left( s , v \right) \cdot Z \left( s \right) } l }\tag{27}
$$

Using a simple nonlinear corona model to describe the voltage dependence of G and $C ,$ the profiles of $Y _ { c } ( s , v )$ and $H ( s , v )$ can be characterized by the conductor voltage v and corona inception voltage $v _ { c r i t }$ . This idea is easier to understand by observing $\mathrm { F i g . 4 }$ , which presents the magnitude and phase angle of $Y _ { c } ( s , v )$ and $H ( s , v )$ for a section length $l ~ = ~ 1 0 0$ m of the Tidd line [28]. Tidd line has a $\begin{array} { r } { { v } _ { c r i t } = { } \ 4 7 0 \ \mathrm { k V } , } \end{array}$ and the line parameters are provided in Appendix B.

As shown in Fig. 4, when the conductor voltage $v \leq v _ { c r i t }$ there is no corona effect, and we can assume that $G = G _ { 0 } \ =$ $1 \cdot 1 0 ^ { - 1 1 }$ [S/m] [29] and $C \ = C _ { o } \ C _ { o }$ is the geometric capacitance of the line). On the other hand, when $v > v _ { c r i t }$ , we should update the G and C values according to v and recalculate the frequency response of $Y _ { c }$ and H. In short, this concept is like considering that we have a different transmission line each time that the voltage value is changed, resulting in a different frequency response for $Y _ { c }$ and $H .$ . It should be highlighted that in the present paper, the calculations of $G ( v )$ and $C ( v )$ were performed applying the Umoto and Hara model [30], which is described in Appendix A. Regarding the frequency response of $R ( s )$ and $L ( s )$ , the internal impedance is calculated with the Bessel functions [31], and the external impedance is calculated with the Deri-Semlyen logarithmic approximations [32].

## C. Time Domain Implementation and Solution Technique

As discussed in Section II, using recursive convolutions, the EMT-type implementation of the WB line model can be characterized by the TDIP $- \ G _ { s } , \ r _ { i } ^ { Y _ { c } } , \ \alpha _ { i } ^ { Y _ { c } } , \ \lambda _ { i } ^ { Y _ { c } } , \ \mu _ { i } ^ { Y _ { c } } , \ r _ { i } ^ { H }$ ， $\alpha _ { i } ^ { H } , \lambda _ { i } ^ { H } , \mu _ { i } ^ { H }$ and τ . Considering the corona effect, however, it was shown that there is a different frequency response for each value of $v ,$ which leads us to consider these TDIPs to be voltage-dependent. More specifically, for an arbitrary voltage value $v _ { j }$ , we can obtain rational approximations for $Y _ { c } ( s , v _ { j } )$ and ${ H } ( s , v _ { j } )$ and calculate their respective $\mathrm { T D I P } ( v _ { j } )$ , that is, $G _ { s } ( v _ { j } ) , r _ { i } ^ { \bar { Y _ { c } } } ( v _ { j } ) , \alpha _ { i } ^ { Y _ { c } } ( v _ { j } ) , \lambda _ { i } ^ { Y _ { c } } ( v _ { j } ) , \mu _ { i } ^ { Y _ { c } } ( v _ { j } ) , r _ { i } ^ { H } ( v _ { j } ) , \alpha _ { i } ^ { H } ( v _ { j } )$ $\lambda _ { i } ^ { H } ( \dot { v _ { j } } ) , \dot { \mu _ { i } ^ { H } } ( \dot { v _ { j } } )$ and $\tau ( v _ { j } )$

In the case of the Tidd line, for instance, Fig. 5 shows the magnitude fitting of $Y _ { c }$ and H for three different voltage samples:

![](images/b234c0c006ff34279f778b73a61415dfd8dc151336f1caf24823785445ef161d.jpg)

![](images/3326da223558c7de84e654f73bc4c285bc4e5b1232bbeaa4f67e9f6f3af8e5e8.jpg)  
(b)

![](images/79dad74aa192516aca1a797d6dbe440572adc5b75ac5ccdedb869235fe447037.jpg)  
（c)

![](images/a2872ca4fdf3f55a5a63d1f87e8524bc4fdd556f8e6c916ead0310195f61dc69.jpg)  
(d)  
Fig. 4. Magnitude and phase angle profiles of $Y _ { c } ( s , v )$ and $H ( s , v )$ for the Tidd line. (a) Magnitude of ${ Y _ { c } ( s , v ) }$ . (b) Phase angle of $Y _ { c } ( s , v )$ . (c) Magnitude of $H ( s , v )$ . (d) Phase angle of $H ( s , v )$

![](images/cca7c6e7d1b2607e4d1ff27a20ed8aea730590b66447aed7c6ed2531cdbc399a.jpg)  
(a)

![](images/a9157eb8ea2800844b11dff20703b619afa356317e110466026c6ef575bc3b09.jpg)  
Fig. 5. Magnitude fitting of the $Y _ { c }$ and H functions for three voltage samples at the Tidd line. (a) Magnitude of $Y _ { c } . \left( \mathbf { b } \right)$ Magnitude of H.

without corona $( v \leq v _ { c r i t } ) , v \ = \ 1 0 0 0 \mathrm { k V }$ and $v ~ = ~ 2 0 0 0 \mathrm { k V } .$ In all cases, the fitting order is automatically adjusted to obtain a maximum final fitting error less than 0.02%, as done in EMTDC [29]. For each voltage sample, the respective $\mathrm { T D I P } ( v _ { j } )$ can be calculated with the time step, residues, and poles of $Y _ { c } ( s , v _ { j } )$ and $H ( s , v _ { j } )$ , as described in Section II.

Regarding the fitting procedure of $Y _ { c }$ and H, two important aspects should be highlighted:

- As shown in the data tips of Fig. 5(a), for the case without corona, the magnitude of $Y _ { c }$ varies with frequency, although this variation is much smoother when compared with the cases of $v ~ = ~ 1 0 0 0$ kV and $v ~ = ~ 2 0 0 0 \mathrm { k V } .$

- As discussed in [18], the corona effect reduces the wave propagation velocity, which leads to higher voltage values having higher time delays. For each voltage sample $v _ { j } .$ , the time delay extraction of $H ( s , v _ { j } )$ can be carried out using the same procedure as described in Section II. In this paper, Bode’s magnitude phase relation [25] was adopted, and the following time delays were obtained for the presented cases: $\tau ~ = ~ 3 3 . 3 9$ µs for $v \leq v _ { c r i t } , \tau \ = \ 4 1 . 1 9$ µs for v = 1000 kV and $\tau = ~ 4 4 . 2 4$ µs for $v ~ = ~ 2 0 0 0 \mathrm { k V } .$

![](images/883541373073d9a94c9e96c0966afb518d5f311b1b0f48e561c26bd3818bbdd4.jpg)  
Fig. 6. History buffer management in the VFDLM.

Based on the aforementioned information, the time domain implementation of VFDLM becomes very simple and straightforward. For simplicity, this procedure is summarized in the following steps:

1. In the line constants program, the TDIPs are calculated for n voltage samples linearly distributed in the range $v _ { c r i t } \leq$ $v _ { j } \le v _ { m a x }$ , where $j = 1 2 , \dots , n$ and $v _ { m a x }$ corresponds to the maximum overvoltage expected to occur along the line. Clearly, the ideal values for n and $v _ { m a x }$ depend on the analyzed phenomenon, and more discussion about this subject is presented in Section V.

2. The respective TDIP associated with each voltage sample constitutes the output of the line constant program. These parameters are stored in the computer’s memory to be used in the simulation loop.

3. When the simulation loop starts, at each time step, the conductor voltage v is checked. If the conductor is under corona, the transmission line subroutine searches in the computer’s memory for the closest voltage sample $v _ { j }$ for which the $\mathrm { T D I P } ( v _ { j } )$ was calculated and then updates their respective values.

4. Since the time delay varies according to the voltage value, the minimum buffer size must be calculated in relation to the maximum voltage sampled, as shown in (28). This occurs because, as previously discussed, higher voltage values present larger time delays. Consequently, the historical term position inside the buffer changes according to the voltage value, as illustrated in Fig. 6. Linear interpolation should be applied when the time delay is not an integer multiple of the time step, as discussed in Section II.

$$
B S = \left\lfloor { \frac { \tau \left( v _ { m a x } \right) } { \Delta t } } \right\rfloor + 1\tag{28}
$$

5. Since the line parameters can be changed every time step in the VFDLM, the Norton equivalents are represented by nonlinear conductance and voltage-dependent current sources, as shown in Fig. 7. If the conductor voltage does not exceed the corona inception voltage, the VFDLM is the same as the WB line model described in Section II. Thus, the VFDLM can be seen as a more general representation of the WB line model.

Although the calculation and storage of the TDIP for several voltage samples increase the computational effort, this procedure is not as heavy as it seems. The reason is that, as discussed in Section III, to derive the voltage profile along the line, the line should be discretized in short sections. For the lengths of these line sections, both $Y _ { c }$ and H present smooth frequency responses for the entire voltage range, which allows them to be quickly fitted with a low number of poles. Furthermore, the VF is naturally a very fast technique, and considerable effort reduction can be obtained in terms of TDIP storage if only real poles are used [33]. As will be shown in Section IV, applying the abovementioned techniques, and using a personal computer, for the Tidd line previously mentioned, the calculation of the TDIP for $n = 1 0 0$ voltage samples was performed in less than 0.6 s.

![](images/6a495cf57e68ce4b3e12222a5d634e1e05d9fb531845643fc72eb95ed057e4af.jpg)  
Fig. 7. Norton equivalent of VFDLM.

Finally, the TDIP is obtained in the line constants calculation routine, which is performed before the simulation loop starts. Inside the simulation loop, the only computational effort increased by the VFDLM is the search for the nearest voltage sample by which the TDIP was calculated.

## D. Computational Procedure

The network solver used in EMT-type programs is based on the system nodal equations presented in (29) [1]. In this system, $[ { \pmb v } ( t ) ]$ is a column vector containing the unknown voltages in each node of the circuit; $[ Y _ { s h } ]$ is the nodal conductance matrix (made up of the conductances in the Norton equivalents); [i(t)] is a column vector of injected currents, and $[ i _ { h i s t } ( t ) ]$ is a column vector composed of historical current sources.

$$
\left[ Y _ { s h } \right] \cdot \ \left[ \pmb { v } \left( t \right) \right] = \left[ \pmb { i } \left( t \right) \right] \ - \left[ \pmb { i } _ { h i s t } \left( t \right) \right]\tag{29}
$$

Since $[ Y _ { s h } ] , [ i ( t ) ]$ ] and $[ i _ { h i s t } ( t ) ]$ are known quantities at time t, (29) corresponds to a simple system of linear equations, which can be easily solved by different methods [34]. However, in the VFDLM, the shunt conductance and historical current sources in Norton equivalents are voltage-dependent parameters (as illustrated in Fig. 7). Consequently, the nodal conductance matrix and the vector of historical currents are also voltage-dependent quantities, that is, $[ Y _ { s h } ( \pmb { v } ( t ) ) ]$ and $\left[ i _ { h i s t } ( \pmb { v } ( t ) ) \right]$ , which means that (29) should be solved only by iterative methods, increasing the computational effort.

Nevertheless, a simpler and faster solution can be obtained if the values of shunt conductances and historical current sources were taken with the basis in the voltage of the previous time step, as shown in (30) [18]. Since $\left[ Y _ { s h } ( { \pmb v } ( t - \Delta t ) ) \right]$ , [i(t)] and $[ i _ { h i s t } ( \pmb { v } ( t - \Delta t ) ) ]$ ] are known quantities at the current time t, the nodal voltages $[ { \pmb v } ( t ) ]$ can be obtained by the solution of the linear system, as in the standard procedure of EMT-type programs. As will be shown in the next section, this procedure is applied to validate the proposed model, and very good results are obtained in terms of accuracy and computational efficiency.

$$
\left[ Y _ { s h } \left( v \left( t - \Delta t \right) \right) \right] \cdot \left[ \pmb { v } \left( t \right) \right] = \left[ i \left( t \right) \right] - \left[ i _ { h i s t } \left( v \left( t - \Delta t \right) \right) \right]\tag{30}
$$

## IV. VALIDATION TESTS

Using the procedures described in the previous section, the VFDLM was implemented in the MATLAB platform, and to evaluate its accuracy, the simulation results were compared with the three well-known field measurement data available in the literature, which are the measurements performed on the Tidd [28], EDF [35] and Shiobara [36] lines. The structure adopted to reproduce these experiments in the simulations is described in Appendix B. Furthermore, to carry out more comprehensive analyses, the results obtained with the proposed VFDLM were also compared with cases in which only the frequency dependence is represented in the simulations (without corona). For this purpose, the TDIP was calculated for only one voltage sample referring to $v \leq v _ { c r i t } . $ , and inside the simulation loop, these parameters were kept invariable.

For the simulations in the Tidd and Shiobara lines, where the rise time of applied waveforms is approximately 1 µs, the lines were discretized into sections of 100 m. For the EDF line, the applied waveform has a rise time of 0.26 μs, and sections of 50 m were adopted. A time step of $\Delta t = 1 0$ ns was standardized for all simulation cases. The TDIP was calculated for $n ~ = ~ 1 0 0$ voltage samples linearly distributed in the following voltage ranges: $4 7 0 \leq v \leq 2 0 0 0 \mathrm { k V }$ for the Tidd line, $2 5 0 \leq v \leq 1 3 0 0$ kV for the EDF line and $3 0 3 \leq v \leq 1 8 0 0 \mathrm { k V }$ for the Shiobara line. The fitting procedure was set to obtain a final fitting error lower than 0.02% for $Y _ { c }$ and H, and a maximum number of poles equal to 8 was enough to obtain this accuracy for all the voltage samples. Furthermore, the adjustment procedure was carried out using only real poles through VF, as described in [33].

The obtained results are shown in Fig. 8, wherein the computed waveforms obtained with the VFDLM, and WB line model (without corona) are plotted with the measured waveforms. Due to the spatial discretization, in some cases, the measurement points shown in the figure are approximated to those recorded in the original measurements. The values of corona model parameters adopted for each line are presented in Appendix A.

As shown in Fig. 8, the calculated waveforms obtained with VFDLM agree well with the measurement data. Above the corona inception voltage, the waveforms are attenuated and distorted as the voltage surge propagates along the line. These phenomena are a consequence of the increase in the line capacitance and shunt conductance, which are adequately represented by the VFDLM. On the other hand, waveforms obtained with the WB line model (without corona) show that even though the frequency dependence is accurately represented in the simulations, disregarding the corona effect can lead to very conservative results. In this sense, the obtained results showed that WB line model led to overestimating the overvoltages by approximately 27% for the Tidd line, 49% for the EDF line and 31% for the Shiobara line.

![](images/30d3f3ba314432122a31ee4a8a675d121d9e516391f058203585347a0aaa0c65.jpg)  
(a)

![](images/2c5c78ea95418e0cc81c41649367020c0088b99aae4bbd71499600d27caf25a1.jpg)

![](images/e3acea41c9519c68f0541588fb8e825141061b72fb8560d8c2ec6864bb675773.jpg)  
Fig. 8. Comparisons between measured and calculated waveforms. (a) Tidd line, (b) EDF line, (c) Shiobara line. (a) Tidd line. (b) EDF line. (c) Shiobara line.

Regarding the CPU time, as previously mentioned, the TDIP calculation for 100 voltage samples could be performed in less than 0.6 seconds. Inside the simulation loop, the only additional time increased by VFDLM is related to the search and update of the TDIP. The total CPU time for each line case is shown in Table I, where the CPU time for the WB line model is also presented for comparison purposes. Evidently, for both cases (WB and VFDLM), the lines were discretized into the same section length. It should be noted that all simulations were performed on a Dell XPS 8930 desktop computer with an Intel Core i7 processor and 16 GB RAM memory.

TABLE I  
TOTAL CPU TIME OF SIMULATIONS
<table><tr><td rowspan=1 colspan=1>Line</td><td rowspan=1 colspan=1>WB line model(without corona)</td><td rowspan=1 colspan=1>VFDLM</td></tr><tr><td rowspan=1 colspan=1>Tidd</td><td rowspan=1 colspan=1>2.3s</td><td rowspan=1 colspan=1>3.1 s</td></tr><tr><td rowspan=1 colspan=1>EDF</td><td rowspan=1 colspan=1>24.4 s</td><td rowspan=1 colspan=1>25.5 s</td></tr><tr><td rowspan=1 colspan=1>Shiobara</td><td rowspan=1 colspan=1>1.3 s</td><td rowspan=1 colspan=1>2.0 s</td></tr></table>

## V. DISCUSSIONS

This paper has introduced a new approach to represent frequency-dependent transmission line models and the corona effect in EMT-type platforms. Unlike the traditional approach, where the corona effect is externally represented by lumped shunt elements disposed at each junction node of line sections, the proposed VFDLM embedded the frequency dependence and corona phenomena directly in the line formulation, resulting in a more robust line model.

It should be noted that, if the conductor voltage does not exceed the corona inception voltage $v _ { c r i t } .$ , the VFDLM presents the same response as the WB line model, which means that the VFDLM is a more general case of the WB line model. Thus, if the VFDLM is implemented in an EMT-type platform, the representation of the corona can be set as a user-defined choice. If the user chooses not to represent the corona, in the line constant calculations the TDIPs are calculated for only one voltage sample related to $v \leq v _ { c r i t }$ , and inside the simulation loop these parameters are kept constant.

The only disadvantage of the VFDLM is the need for fitting the $Y _ { c }$ and H functions for several voltage samples. However, this procedure needs to be performed only a single time during the line constant calculations, which is done before the simulation loop starts. Inside the simulation loop, the only computational burden added by VFDLM is to check the conductor voltage and update the TDIP when necessary.

Regarding the number of voltage samples (n) and the voltage range for which the TDIP should be calculated $( v _ { c r i t } \leq v \leq$ $v _ { m a x } )$ , the following considerations must be highlighted:

1. As previously presented, $v _ { m a x }$ is the maximum overvoltage expected to occur along the line. For practical applications, it is known that the conductor voltage rarely exceeds 4 p.u. [15], since for overvoltages above this value, an electric arc will probably occur. In this sense, we consider the adoption of $v _ { m a x } = 4 \cdot v _ { c r i t } \mathrm { o r } v _ { m a x } = 5 \cdot v _ { c r i t }$ enough to produce good results for most cases, as demonstrated in Section IV. However, if necessary, the user can change this value according to the needs.

2. The idea of voltage discretization inside the voltage range is like the idea of frequency response calculation in EMTDC [29], wherein the user can define the frequency range for which the line parameters will be calculated, as well as the number of frequency samples logarithmically distributed within this range.

TABLE II  
CORONA MODEL PARAMETERS
<table><tr><td rowspan=1 colspan=1>Line</td><td rowspan=1 colspan=1> $\sigma _ { C }$ (F/m)</td><td rowspan=1 colspan=1> $\sigma _ { G }$ (S/m)</td><td rowspan=1 colspan=1>Vcrit(kV)</td></tr><tr><td rowspan=1 colspan=1>Tidd</td><td rowspan=1 colspan=1>14.5</td><td rowspan=1 colspan=1>4-106</td><td rowspan=1 colspan=1>470</td></tr><tr><td rowspan=1 colspan=1>EDF</td><td rowspan=1 colspan=1>8.5</td><td rowspan=1 colspan=1>4.8-106</td><td rowspan=1 colspan=1>250</td></tr><tr><td rowspan=1 colspan=1>Shiobara</td><td rowspan=1 colspan=1>13.5</td><td rowspan=1 colspan=1>4-106</td><td rowspan=1 colspan=1>303</td></tr></table>

![](images/16e4bdc5720484bf9cd7d814c7ba41c67cdc81a13709304e0cf717233b0caf5d.jpg)  
Fig. 9. Influence of voltage sampling in VFDLM.

TABLE III  
TRANSMISSION LINES PARAMETERS
<table><tr><td rowspan=1 colspan=1>Line</td><td rowspan=1 colspan=1>Length(km)</td><td rowspan=1 colspan=1>Height(m)</td><td rowspan=1 colspan=1>Conductorradius(mm)</td><td rowspan=1 colspan=1>Soilresistivity(Ω·m)</td><td rowspan=1 colspan=1>Matchingresistance(Ω)</td></tr><tr><td rowspan=1 colspan=1>Tidd</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>18.89</td><td rowspan=1 colspan=1>25.40</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>470</td></tr><tr><td rowspan=1 colspan=1>EDF</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>12</td><td rowspan=1 colspan=1>13.2</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>459</td></tr><tr><td rowspan=1 colspan=1>Shiobara</td><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>16.87</td><td rowspan=1 colspan=1>12.65</td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>486</td></tr></table>

![](images/efad4ffc6400f510a0c6be550d48719f5e142fb76f7cd08bcb4a7a6b6c92982a.jpg)  
Fig. 10. Structure adopted to reproduce the field measurement tests in the simulations.

3. The ideal number of voltage samples for which the TDIP should be calculated evidently varies according to the voltage range. In the case of the Tidd line, for instance, Fig. 9 presents the results for $n = 2 0 , n = 5 0 , n = 1 0 0$ and n = 200 voltage samples linearly distributed inside the range $4 7 0 \leq v \leq 2 0 0 0 \mathrm { k V } .$ All the cases present reasonable results in terms of accuracy. However, as shown in the zoomed portion, spurious oscillations can be observed for the cases with n = 20 and n = 50. These spurious oscillations occur due to the abrupt variation in the TDIP from one integration step to the other. By increasing the number of voltage samples to $n = 1 0 0 \mathrm { o r } n = 2 0 0$ , we have a smooth variation along the voltage range, leading to smooth results. Furthermore, as seen in the zoomed portion, no significant differences are observed when increasing the number of voltage samples from n = 100 to $n \ = \ 2 0 0$ , which explains the adoption of $n ~ = ~ 1 0 0$ for all analyzed cases in Section IV.

Although not shown in the paper, it should be highlighted that we also attempted to apply trapezoidal integration instead of recursive convolutions to solve the discrete convolutions in (11) and (12). However, it was verified that the problem of spurious oscillations previously mentioned was more pronounced for trapezoidal integration, which means that recursive convolutions should be preferred over trapezoidal integration. Similar conclusions were reached in [27]. By using recursive convolutions, we performed several sensitivity analyses with the VFDLM, and for all the analyzed cases, the model proves to be stable, efficient, and accurate, as demonstrated in Section IV.

## VI. CONCLUSION

This paper has introduced a VFDLM for corona effect representation in EMT-type programs. The approach consists of a more general case of well-established FD or WB line models, wherein the characteristic admittance and propagation functions are fitted for several voltage samples above the corona inception voltage using the VF technique. The implementation procedure of VFDLM is straightforward and very similar to the WB model, which allows the model to be used in a generic way; that is, the representation of the corona effect can be set as a user-defined choice. The model was validated through comparisons with three field measurement datasets and proven to be a stable, efficient, and accurate approach to represent the corona effect in EMT-type platforms.

At the time of preparation of this paper, the VFDLM is being extended to multiphase transmission lines, in addition to being applied to more robust corona models.

## A. Corona Model

In this paper, the voltage dependence of the capacitance and shunt conductance of the line are described by the empirical equations proposed by Umoto and Hara [30]. Although these equations do not represent the frequency dependence of the corona, they can represent with good accuracy the voltage dependence of the abovementioned parameters and have been successfully applied in several papers over the years to represent the corona effect in wave propagation calculations [9], [10], [18].

According to this model, the variation of the capacitance and shunt conductance per unit length of the line can be described as shown in (31) and (32), respectively.

$$
C \left( v \right) \ = \left\{ { C _ { 0 } } , \ { v \le v _ { c r i t } } \right.\tag{31}
$$

$$
G \mathrm { ~ } ( v ) = \left\{ \begin{array} { l r } { G _ { 0 } , } & { v \leq v _ { c r i t } } \\ { G _ { 0 } + \sigma _ { G } \sqrt { \frac { r } { 2 h } } . 1 0 ^ { - 1 1 } \left( 1 - \frac { v _ { c r i t } } { v } \right) ^ { 2 } v > v _ { c r i t } } \end{array} \right.\tag{32}
$$

In the above equations, v is the conductor voltage $[ \mathrm { V } ] ; v _ { c r i t }$ is the corona inception voltage [V]; $G _ { 0 } = \ 1 E ^ { - 1 1 }$ [S/m]; r and h are the radius and height above ground of the conductor [m], respectively. Finally, $\sigma _ { C }$ and $\sigma _ { G }$ are corona loss constants (in [F/m] and [S/m], respectively), which are determined by a trial-and-error procedure by comparing calculated and field-test waveforms. The values of corona parameters used in the reproduction of the three field measurement tests presented in Section IV are shown in Table II, while the conductor radius and height above ground are shown in Table III.

## B. Experiments on Tidd, EDF, and Shiobara Lines

Experiments on the Tidd [28], EDF [35] and Shiobara [36] lines were carried out to assess the influence of the corona effect on the attenuation and distortion of traveling waves originating from lightning overvoltages. The structure adopted to represent these lines in the simulations is shown in Fig. 10. The line is composed of a single overhead wire placed at an average height H above the ground. The sending end is connected to a lumped voltage source, whereas the receiving end is connected to the ground through a matching resistor, whose resistance is equal to the characteristic impedance of the line. The line data necessary for simulations are shown in Table III. It should be noted that although these lines were originally three-phase transmission lines, only one of the phases was energized in the experiments. Since the adjacent phases did not interfere in the results, it is enough to represent only the energized phase. This same procedure has already been successfully adopted in previous works [12], [16], [18].

Regarding the waveform applied in the experiments, different characteristics are observed between them. In the Tidd line, a pulse voltage like a double exponential of 1/6.3 µs with amplitude of 1.55 MV was applied. In the EDF line, the applied waveform consists of a double exponential with damped oscillations, which is approximately a 0.26/3.4 µs curve with 1.10 MV of peak value. In the Shiobara line, a nonstandard waveform of 1.2 µs of rise time and 1.58 MV peak value was applied. The described waveforms are presented together with the measurements along the lines in Fig. 8(a)–(c).

## REFERENCES

[1] H. W. Dommel, “Digital computer solution of electromagnetic transients in Single- and Multiphase networks,” IEEE Trans. Power App. Syst., vol. PAS-88, no. 4, pp. 388–399, Apr. 1969, doi: 10.1109/TPAS.1969.292459.

[2] J. Marti, “Accurate modelling of frequency-dependent transmission lines in electromagnetic transient simulations,” IEEE Trans. Power App. Syst., vol. PAS-101, no. 1, pp. 147–157, Jan. 1982, doi: 10.1109/TPAS.1982.317332.

[3] A. Morched, B. Gustavsen, and M. Tartibi, “A universal model for accurate calculation of electromagnetic transients on overhead lines and underground cables,” IEEE Trans. Power Del., vol. 14, no. 3, pp. 1032–1038, Jul. 1999, doi: 10.1109/61.772350.

[4] T. H. Thang et al., “A simplified model of corona discharge on overhead wire for FDTD computations,” IEEE Trans. Electromagn. Compat., vol. 54, no. 3, pp. 585–593, Jun. 2012, doi: 10.1109/TEMC.2011.2172688.

[5] K. Huang, X. Zhang, and S. Tao, “Electromagnetic transient analysis of overhead lines including corona and frequency dependence effects under damped oscillation surges,” IEEE Trans. Power Del., vol. 33, no. 5, pp. 2198–2206, Oct. 2018, doi: 10.1109/TPWRD.2018.2794825.

[6] G. C. de Miranda, A. Emílio, A. de Araújo, R. R. Saldanha, and J. P. Filho, “Finite element method for transmission line corona effect simulation using the EMTP,” Electric Mach. Power Syst., vol. 27, no. 7, pp. 781–794, 1999, doi: 10.1080/073135699269019.

[7] X. Liu, J. Yang, G. Liang, and L. Wang, “Modified field-to-line coupling model for simulating the corona effect on the lightning induced voltages of multi-conductor transmission lines over a lossy ground,” IET Gener., Transmiss. Distrib., vol. 11, no. 7, pp. 1865–1876, 2017, doi: 10.1049/iet-gtd.2016.1340.

[8] J. L. Naredo, A. C. Soudack, and J. R. Marti, “Simulation of transients on transmission lines with corona via the method of characteristics,” IEE Proc. - Gener., Transmiss. Distrib., vol. 142, no. 1, 1995, Art. no. 81, doi: 10.1049/ip-gtd:19951488.

[9] K. Lee, “Non-linear corona models in an electromagnetic transients program (EMTP),” IEEE Trans. Power App. Syst., vol. PAS-102, no. 9, pp. 2936–2942, Sep. 1983, doi: 10.1109/TPAS.1983.318144.

[10] H. Motoyama and A. Ametani, “Development of a linear model for corona wave deformation and its effects on lightning surges,” Elect. Eng. Jpn., vol. 107, no. 2, pp. 98–106, 1987, doi: 10.1002/eej.4391070211.

[11] W.-G. Huang and A. Semlyen, “Computation of electro-magnetic transients on three-phase transmission lines with corona and frequency dependent parameters,” IEEE Trans. Power Del., vol. 2, no. 3, pp. 887–898, Jul. 1987, doi: 10.1109/TPWRD.1987.4308193.

[12] S. Carneiro and J. R. Marti, “Evaluation of corona and line models in electromagnetic transients’ simulations,” IEEE Trans. Power Del., vol. 6, no. 1, pp. 334–342, Jan. 1991, doi: 10.1109/61.103756.

[13] T. J. Gallagher and I. M. Dudurych, “Model of corona for an EMTP study of surge propagation along HV transmission lines,” IEE Proc. - Gener., Transmiss. Distrib., vol. 151, no. 1, 2004, Art. no. 61, doi: 10.1049/ip-gtd:20030927.

[14] Z. Anane, A. Bayadi, and K. Huang, “Distortion phenomena on transmission lines using corona modeling ATP/EMTP,” IEEE Trans. Dielectrics Elect. Insul., vol. 25, no. 2, pp. 383–389, Apr. 2018, doi: 10.1109/TDEI.2017.006484.

[15] M. Cervantes et al., “Simulation of switching overvoltages and validation with field tests,” IEEE Trans. Power Del., vol. 33, no. 6, pp. 2884–2893, Dec. 2018, doi: 10.1109/TPWRD.2018.2834138.

[16] S. Carneiro, J. R. Marti, H. W. Dommel, and H. M. Barros, “An efficient procedure for the implementation of corona models in electromagnetic transients’ programs,” IEEE Trans. Power Del., vol. 9, no. 2, pp. 849–855, Apr. 1994, doi: 10.1109/61.296266.

[17] H. M. Barros, S. Carneiro, and R. M. Azevedo, “An efficient recursive scheme for the simulation of overvoltages on multiphase systems under corona,” IEEE Trans. Power Del., vol. 10, no. 3, pp. 1443–1452, Jul. 1995, doi: 10.1109/61.400928.

[18] T. M. Pereira and M. C. Tavares, “Development of a voltage-dependent line model to represent the corona effect in electromagnetic transient program,” IEEE Trans. Power Del., vol. 36, no. 2, pp. 731–739, Apr. 2021, doi: 10.1109/TPWRD.2020.2990968.

[19] B. Gustavsen, J. Sletbak, and T. Henriksen, “Calculation of electromagnetic transients in transmission cables and lines taking frequency dependent effects accurately into account,” IEEE Trans. Power Del., vol. 10, no. 2, pp. 1076–1084, Apr. 1995, doi: 10.1109/61.400879.

[20] B. Gustavsen, G. Irwin, R. Mangelrød, D. Brandt, and K. Kent, “Transmission line models for the simulation of interaction phenomena between parallel AC and DC overhead lines,” in Proc. Int. Converence Power Syst. Transients, 1999, pp. 61–67.

[21] B. Gustavsen and A. Semlyen, “Rational approximation of frequency domain responses by vector fitting,” IEEE Trans. Power Del., vol. 14, no. 3, pp. 1052–1061, Jul. 1999, doi: 10.1109/61.772353.

[22] B. Gustavsen and A. Semlyen, “Simulation of transmission line transients using vector fitting and modal decomposition,” IEEE Trans. Power Del., vol. 13, no. 2, pp. 605–614, Apr. 1998, doi: 10.1109/61.660941.

[23] B. Gustavsen, “Time delay identification for transmission line modeling,” in Proc. 8th IEEE Workshop Signal Propag. Interconnects, 2004, pp. 103–106. doi: 10.1109/SPI.2004.1409018.

[24] I. Kocar and J. Mahseredjian, “New procedure for computation of time delays in propagation function fitting for transient modeling of cables,” IEEE Trans. Power Del., vol. 31, no. 2, pp. 613–621, Apr. 2016, doi: 10.1109/TP-WRD.2015.2444880.

[25] B. Gustavsen, “Optimal time delay extraction for transmission line modeling,” IEEE Trans. Power Del., vol. 32, no. 1, pp. 45–54, Feb. 2017, doi: 10.1109/TPWRD.2016.2609039.

[26] A. Semlyen and A. Roth, “Calculation of exponential propagation step responses - Accurately for three base frequencies,” IEEE Trans. Power App. Syst., vol. 96, no. 2, pp. 667–672, Mar. 1977, doi: 10.1109/T– PAS.1977.32378.

[27] B. Gustavsen, “Avoiding numerical instabilities in the universal line model by a two-segment interpolation scheme,” IEEE Trans. Power Del., vol. 28, no. 3, pp. 1643–1651, Jul. 2013, doi: 10.1109/TPWRD.2013.2257878.

[28] C. F. Wagner, I. W. Gross, and B. L. Lloyd, “High-voltage impulse tests on transmission lines [includes discussion],” Trans. Amer. Inst. Elect. Engineers. Part III: Power App. Syst., vol. 73, no. 2, pp. 196–210, Apr. 1954, doi: 10.1109/AIEEPAS.1954.4498810.

[29] EMTDC User’s Guide - A Comprehensive Resource for EMTDC, Manitoba Hydro Int. Ltd, Winnipeg, Manitoba, Canada, 2010.

[30] J. Umoto and T. Hara, “Numerical analysis of line equations considering corona loss on single-conductor system,” Elect. Eng. Jpn., vol. 89, pp. 909–916, 1969.

[31] S. A. Schelkunoff, “The electromagnetic theory of coaxial transmission lines and cylindrical shields,” Bell Syst. Tech. J., vol. 13, no. 4, pp. 532–579, Oct. 1934, doi: 10.1002/j.1538-7305.1934.tb00679.x.

[32] A. Deri, G. Tevan, A. Semlyen, and A. Castanheira, “The complex ground return plane. A simplified model for homogeneous and multi-layer earth return,” IEEE Power Eng. Rev., vol. PER-1, no. 8, pp. 31–32, Aug. 1981, doi: 10.1109/MPER.1981.5511760.

[33] E. S. Bañuelos-Cabral, B. Gustavsen, J. A. Gutiérrez-Robles, H. K. Høidalen, and J. L. Naredo, “Computational efficiency improvement of the universal line model by use of rational approximations with real poles,” Electric Power Syst. Res., vol. 140, pp. 424–434, Nov. 2016, doi: 10.1016/j.epsr.2016.05.033.

[34] F. H. Branin, “Computer methods of network analysis,” Proc. IEEE, vol. 55, no. 11, pp. 1787–1801, Nov. 1967, doi: 10.1109/PROC.1967.6010.

[35] C. Gary, G. Dragan, and D. Cristescu, “Attenuation of travelling waves caused by corona,” in Proc. Int. Conf. Large High Voltage Eletric Syst., 1978, Art. no. 38.

[36] A. Inoue, “Propogation analysis of overvoltage surges with corona based upon charge versus voltage curve,” IEEE Trans. Power App. Syst., vol. PAS-104, no. 3, pp. 655–662, Mar. 1985, doi: 10.1109/TPAS.1985.319001.

![](images/8087aa731d78f5531130ecf37c9d735798951dc478fcbee4cefa7f19b6b2ef27.jpg)

Thassio Matias Pereira (Graduate Student Member, IEEE) was born in Minas Gerais, Brazil, in 1994. He received the Electrical Engineering degree from the Federal University of São João del-Rei, São João del-Rei, Brazil, in 2017, and the M.Sc. degree in 2019 from the University of Campinas, Campinas, Brazil, where he is currently working toward the D.Sc. degree. His research interests include electromagnetic modeling and transients, lightning, transmission line performance, and insulation coordination.

![](images/b8c3de05bcd1eb78b2944e45be2294e6cad8fbd5aa7f375c193802f4b94ee879.jpg)

Maria Cristina Tavares (Senior Member, IEEE) received the B.Sc. and M.Sc. degrees in electrical engineering from the Federal University of Rio de Janeiro, Rio de Janeiro, Brazil, in 1984 and 1991, respectively, and the D.Sc. degree from the University of Campinas, Campinas, Brazil, in 1998. She has provided consultation for engineering firms. Since 2002, she has been with the University of Campinas, where she is currently an Associate Professor. Her research interests include electromagnetic transients in power systems, arc modeling, very long-distance

transmission systems, and computer applications for transient analysis in power systems. He is the Editor of the IEEE TRANSACTIONS ON POWER DELIVERY and an Advisory Editorial Board Member of the International Journal of Electrical Power and Energy Systems.