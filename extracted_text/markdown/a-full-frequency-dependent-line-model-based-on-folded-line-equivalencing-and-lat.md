# A full frequency dependent line model based on folded line equivalencing and latency exploitation

![](images/540cd24eb26c9f600d12c6feb894d8d605e34957a4a5948ee3c45f5b0ad3e4e3.jpg)

Felipe Camaraa, Antonio C.S. Limaa,∗, Fernando A. Moreirab

a Federal University of Rio de Janeiro, Brazil b Federal University of Bahia, Brazil

## a r t i c l e i n f o

Article history:   
Received 23 April 2017   
Received in revised form 31 July 2017   
Accepted 17 August 2017

Keywords: Overhead line modeling Network synthesis Rational approximation Time-domain modeling

## a b s t r a c t

This work proposes to improve the numerical performance in the rational modeling of full frequency dependent transmission lines. In this paper, latency is used to improve the numerical efficiency of timedomain implementation of the pole-residue representation of the nodal admittance matrix in the case of frequency dependent network equivalents. The idea of latency is to use different time-steps for distinct poles, i.e., fast poles are solved using a small time-step while slower poles may be solved using larger time-steps. For the separation of the slow and fast dynamics, a technique named Multiple Companion Networks (MCN) has been developed. The technique has been applied to transient tests of a transmission line modeled with a rational model. The results obtained indicated that a gain in numerical efficiency is possible without compromising accuracy.

© 2017 Elsevier B.V. All rights reserved.

## 1. Introduction

Electromagnetic transient (EMT)-programs allowed for a rapid and wide development of time-domain models for linear, nonlinear and frequency dependent devices. One main characteristic of such approach is to rely on the use of a single time-step for the solution of the whole network. This is often a waste of computational resources since it may be the case where only a small part of the network has to be solved using a small time step, whereas a large part of the network could be solved with a larger time step. Thus a suboptimal numerical performance is found leading to an unnecessary large simulation time.

One possibility to overcome the unnecessary simulation time and to improve the numerical performance of the models involved is to rely on the concept of latency exploitation. In latency [1], the network is divided into at least two sub-networks. The first one, associated with the fastest time-constants, is solved using a small time-step, while a larger time-step is used to solve the other part of the network. Naturally, the number of network subdivisions can increase leading to several sub-networks each being solved with a given time-step. For this reason, latency exploitation may also be called multirate simulation.

The development of numerically accurate and efficient methods for the rational approximation of frequency responses such as the so-called vector fitting routine [2–4], the frequency-partitioning fitting [5] or the matrix pencil [6,7] allowed the realization of full frequency dependent overhead lines and underground cable models in phase coordinates in EMT-simulations [8,9]. One drawback of such models which are based on the method of characteristics (MoC) is that the time-step must be smaller than the fastest modal time-delay which requires a rather accurate procedure for this identification [10]. Furthermore, inaccurate interpolation schemes between the simulation time-step and the modal traveling time might lead to numerical instabilities [11]. This scenario is more important for shorter lines where a very small time-step might be used and the interpolation of the modal time-delay might reduce the numerical efficiency of a line model based on MoC. An alternative to overcome this limitation is to use a rational approximation of the nodal admittance matrix associated with the transmission line. However, as pointed out in [12], the direct fitting of the nodal admittance matrix is not suitable for a general transmission line model as the smallest eigenvalues at the low-frequency range may not be properly fitted leading to inaccurate responses. The limitation associated with the direct fitting can be overcome with the use of the folded line equivalent (FLE) model as also shown in [12].

In [13], the authors proposed to exploit latency in a frequency dependent network using a rational approximation of the nodal admittance matrix developing the Multiple Companion Network (MCN) approach. In this work the formulation of the MCN based on a model decomposition using the FLE has been extended. It was found that the earlier approach led to rather inaccurate results for the time responses and it was needed to rearrange how latency is exploited in the MCN.

The paper is organized as follows: Section 2 summarizes the application of FLE to the modeling of an overhead line. Section 3 explains the idea behind latency exploitation and the use of MCN and how some improvements can be achieved using this formulation. Section 4 describes how a modified MCN can be integrated in the time-step loop to allow an efficient implementation of the proposed model in an EMT-type of program. Section 5 illustrates the main idea of the paper, i.e., to exploit latency considering a FLE representation of an overhead line. The main conclusions of this work are presented in Section 6.

## 2. Folded line equivalent

Consider a transmission line with n phases, the nodal admittance matrix ${ \bf Y } _ { n }$ relating the injected currents and the node voltages is given by (1) in the frequency domain,

$$
\pmb { \Upsilon } _ { n } = \left[ \begin{array} { c c } { \pmb { \Upsilon } _ { s } } & { \pmb { \Upsilon } _ { m } } \\ { \pmb { \Upsilon } _ { m } } & { \pmb { \Upsilon } _ { s } } \end{array} \right]\tag{1}
$$

where ${ \bf Y } _ { s }$ and ${ \bf { Y } } _ { m }$ are n × n block matrices defined by

$$
\begin{array} { l l } { { \displaystyle { \bf Y } _ { s } = { \bf Y } _ { c } \cdot \left( { \bf I } + { \bf H } ^ { 2 } \right) \cdot \left( { \bf I } - { \bf H } ^ { 2 } \right) ^ { - 1 } } } & { { a n d } } \\ { { \displaystyle { \bf Y } _ { m } = - 2 { \bf Y } _ { c } \cdot { \bf H } \cdot \left( { \bf I } - { \bf H } ^ { 2 } \right) ^ { - 1 } } } & { { } } \end{array}\tag{2}
$$

where I is an n × n identity matrix, $\mathbf { Y } _ { c } = \mathbf { Z } ^ { - 1 } { \sqrt { \mathbf { Z } \cdot \mathbf { Y } } }$ is the characteristic admittance matrix, $\mathbf { H } = \exp ( - \ell \sqrt { \mathbf { Z } \cdot \mathbf { Y } } )$ is the propagation matrix also known as voltage deformation matrix and - is the line length.

In EMT-programs, the line is not directly represented using a rational approximation of ${ \bf { Y } } _ { n }$ as there is a large spread of the eigenvalues throughout the frequency range of interest. The method of characteristics (MoC) is used instead which implies in a rational approximation of $\mathbf { Y } _ { c }$ and H. While the former is basically a smooth function in the frequency domain, the latter may present some oscillations that demand the use of several travelling time-delays to achieve an accurate fitting, for instance see [14,8]. This procedure also demands the use of a more elaborate interpolation scheme to avoid numerical instability [11]. A possibility to overcome this limitation is to rely on the so-called idempotent decomposition of H [15]. However, as pointed out in [16], there might be some configurations where the overall accuracy of the rational fitting of the idempotent is low. Alternatively, one may apply a rational approximation not to ${ \bf Y } _ { n }$ but to a “folded” version of it. In this case, the idea is to use a linear transformation to allow a distinct grouping in ${ \bf Y } _ { n }$ in such way that the rational approximation has a lower order and a higher accuracy. This procedure shares some similarities with the usage of a mode-revealing transformation matrix to improve the observability of small eigenvalues at the lower frequency range [17]. Thus, the nodal admittance matrix is written as

$$
\pmb { \Upsilon } _ { n } = \mathbf { K } \cdot \mathbf { \Psi } \left[ \begin{array} { c c } { \pmb { \Upsilon } _ { o c } } & { \mathbf { 0 } } \\ { \mathbf { 0 } } & { \pmb { \Upsilon } _ { s c } } \end{array} \right] \cdot \mathbf { K } ^ { - 1 }\tag{3}
$$

where $\mathbf { Y } _ { o c } = \mathbf { Y } _ { s } + \mathbf { Y } _ { m }$ is the admittance associated with the open circuit current response and $\pmb { \mathrm { Y } } _ { s c } = \pmb { \mathrm { Y } } _ { s } - \pmb { \mathrm { Y } } _ { m }$ stands for the admittance related to the short circuit current response, and

$$
\mathbf { K } = \left[ \begin{array} { l l } { \mathbf { I } } & { \mathbf { I } } \\ { \mathbf { I } } & { - \mathbf { I } } \end{array} \right]\tag{4}
$$

where I is the same as before. This formulation was proposed in [12] and received the name folded line equivalent (FLE). It has some interesting characteristics, the matrices to be fitted have half the dimension of the original admittance matrix, i.e., ${ \bf Y } _ { n }$ has a dimension 2n × 2n while both $\yen 00$ and $\mathbf { Y } _ { s c }$ are n × n matrices. Furthermore, the ratio between the largest and smallest eigenvalues in both $\yen 00$ and $\mathbf { Y } _ { s c }$ reduces considerably when compared with the ones found in ${ \bf Y } _ { n }$

The rational approximation of $\mathbf { \sigma } \mathbf { \tilde { Y } } _ { o c }$ and $\mathbf { Y } _ { s c }$ is carried out independently. In this work, the use of the so-called vector fitting routine [2–4] was chosen although other identification methods such as the frequency-partitioning fitting [5] or the matrix pencil [6,7] could be used instead. Typically, a rational approximation of a nodal admittance matrix ${ \bf Y } _ { n }$ leads to the following

$$
\mathbf { Y } _ { n } \approx \sum _ { m = 1 } ^ { N } \frac { \mathbf { R } _ { m } } { s - p _ { m } } + \mathbf { R } _ { 0 }\tag{5}
$$

where N is the number of poles (pre-defined) to be used, $p _ { m }$ is a set of common poles, either real or in complex conjugates, $\mathbf { R } _ { m }$ is the residue matrix, and $\mathbf { R } _ { 0 }$ is a real-valued matrix associated with the behavior of ${ \bf Y } _ { n }$ at an infinite frequency. In this case, $\mathbf { R } _ { 0 } =$ $\Re ( { \bf Y } _ { c } ( \infty ) ) = { \bf G } _ { c } ( \infty )$ . For the matrices $\yen 00$ and $\mathbf { Y } _ { s c , }$ , it is required that both tend to the characteristic admittance in the high frequency range, i.e., both models must be asymptotically correct. Therefore, the fitting is carried out using (6),

$$
\begin{array} { l }  { \displaystyle { \overline { { \mathbf { Y } } } } _ { o c } = { \mathbf { Y } } _ { o c } - { \mathbf { G } } _ { c } \left( \infty \right) \approx \sum _ { m = 1 } ^ { N } \frac { { \mathbf { R } } _ { o c _ { m } } } { s - p _ { o c _ { m } } } } \\ { ~ } \\ { { \displaystyle { \overline { { \mathbf { Y } } } } _ { s c } = { \mathbf { Y } } _ { s c } - { \mathbf { G } } _ { c } \left( \infty \right) \approx \sum _ { m = 1 } ^ { M } \frac { { \mathbf { R } } _ { s c _ { m } } } { s - p _ { s c _ { m } } } } } \end{array}\tag{6}
$$

It is assumed that both functions to be fitted, i.e., $\bar { \mathbf { Y } } _ { o c }$ and $\bar { \mathbf { Y } } _ { s c } ,$ are strictly proper and there is no a priori relationship between the number of poles used in the fitting of either function. Even though only stable poles are used in the fitting o $\boldsymbol { \mathrm { \mathbf { \check { f } } } } \boldsymbol { \mathbf { \check { Y } } } _ { o c }$ and $\mathbf { Y } _ { s c }$ , the passivity of both approximations must be enforced, as some of the eigenvalues might present a negative real part in the frequency band. Thus, a post-processing scheme based on residue perturbation is applied to $\yen 00$ and $\mathbf { Y } _ { s c }$ to ensure passivity [18].

It is noteworthy a great feature of this approach that the accurate eigenvalues obtained in the fitting process allows to convert the FLE realization back to phase coordinates via (3) with small errormagnifications to be applied in simulations with arbitrary terminal conditions [12].

## 3. Latency exploitation & Multiple Companion Networks

Latency was first applied by researchers in the area of VLSI (Very Large System Integration) simulation [19]. The attempts were based on the waveform relaxation method which is an iterative method capable of exploiting time-domain latency to reach significant speed gains without sacrificing accuracy. It is based on the Gauss-Seidel and Gauss-Jacobi relaxation methods applied to the numerical integration of DAEs (differential algebraic equations).

Latency was first explored in power system problems, also within the context of the waveform relaxation method, for transient stability simulation [20] and later for the solution of electromagnetic transient simulations using multiple time-steps [21,22]. Also, latency has been exploited in an HVDC converter network where the converter bridges have been simulated with a small time step while the ac sources, transformers and dc line have been simulated with a larger time step. Results have shown that accuracy has been maintained while simulation time can be significantly reduced [23].

![](images/ec5f830fa49ac6c072d2413f57be5fade8fbd9b57d7f6fd562e385a100acbf14.jpg)  
Fig. 1. Simple parallel RL circuit to illustrate latency exploitation.

The use of latency in some applications in power systems relies on the concept of Multi-Area Thevenin equivalents (MATE) [24]. In waveform relaxation each subsystem uses the previous iterate waveforms as “guesses” for the current state of the other subsystems. After that, iterations are performed to match the solutions at all interfacing points. This intrinsic iterative nature of the technique imposes limitations, particularly in the context of real-time simulation and multi-computer simulation environments. In MATE, circuit latency has been exploited using a direct simultaneous solution for the branch currents linking the subsystems [23].

In [13], the authors opted to approach latency using a distinct formulation called Multiple Companion Networks (MCN). As it is based on companion networks, i.e., Norton equivalents, it does not require a series link to split the network in two distinct parts, one with the “fast” dynamics and the other with the “slow” one.

To illustrate this procedure consider a simple RL parallel circuit as depicted in Fig. 1a, where $R _ { f } , L _ { f }$ stands for the branch with the fast dynamics, i.e., small time-constant to be solved using a small timestep $\Delta t _ { 1 }$ and $R _ { s } , L _ { s }$ is the branch with the slow dynamics, i.e., larger time-constant which can be solved with a time-step $\Delta t _ { 2 } = k \Delta t _ { 1 }$ with $k > 1$ and $k \subset \mathbb { N }$ . Using MCN in the original formulation leads to the discrete time equivalent shown in Fig. 1b, where $G _ { s }$ is the equivalent conductance obtained using a larger time-step $\Delta t _ { 2 }$ and the same can be said about the history current source $h _ { s } ( t ) , G _ { f }$ and $h _ { f } ( t )$ are the elements of the discrete circuit obtained using $\Delta t _ { 1 }$ Both $G _ { S }$ and $G _ { f }$ are added to the system nodal conductance matrix. The updating of the history current sources is distinct though. The one associated with the smaller time-step, i.e., hf(t) is updated at every time-step, while $h _ { s } ( t )$ is updated only every kth time-step. For instance, suppose that for the RL-parallel circuit shown in Fig. 1a the “fast branch” has a time-constant of 100 $\mu s$ , thus being solved with $\Delta t _ { 1 } = 1 0 \mu s$ , while the “slow branch” has a time-constant of 10 ms, which could be solved with $\Delta t _ { 2 } = 1 \mathrm { m s } , \mathrm { i } . \mathrm { e } . , k = 1 0 0$ . However, to solve these two branches in the original approach of the MCN it would be necessary to limit k to small values, typically k ≤ 10, since it was found on the original formulation that as k increases there is a significant increase in the maximum error [13].

To overcome this limitation, a small modification in the original scheme of the MCN, i.e., MCNM, which is suitable to overcome the small k limitation without a significant loss of accuracy as aforementioned is proposed. To explain this in further detail it must be considered how to implement convolution-based models in EMTprograms. Let a pole-residue model in which the set of differential equations resembles the RL-parallel circuit shown in Fig. 2a either using recursive convolution or the trapezoidal integration. The history current sources are updated as

$$
\begin{array} { r } { h _ { f } \left( t \right) = \alpha _ { f } h _ { f } \left( t - \Delta t \right) + c _ { f } \nu ( t - \Delta t ) } \\ { h _ { s } \left( t \right) = \alpha _ { s } h _ { s } \left( t - \Delta t \right) + c _ { s } \nu ( t - \Delta t ) } \end{array}\tag{7}
$$

where the coefficients $\alpha _ { f } , \alpha _ { s } , c _ { f }$ and $c _ { s }$ are defined in Appendix $\mathsf { A } .$ In its original formulation $h _ { f } ( t )$ is to be discretized using $\Delta t _ { 1 }$ while $h _ { s } ( t )$ is updated using $\Delta t _ { 2 } = k \Delta t _ { 1 }$ every kth time-step as depicted in Fig. 2a.

![](images/903e8d0c24c0c0d1cb15f2e24d52208abc9788932708125543e288cccce7680f.jpg)  
(a)original proposition

![](images/f20f284cc3640117c30c1a0d7cb381fb2f94a16ff6e4b9f34c4c29edcf7f3f4d.jpg)  
(b）modified approach

![](images/12581e335ce41363f41de905446681d19687bf42310e048cba6a6bb30d8c920d.jpg)  
(c)relaxed approach  
Fig. 2. Time-line for updating current sources in MCN.

In the modified approach both $h _ { f }$ and $h _ { s }$ are discretized using the same time-step $\Delta t _ { 1 }$ . At every kth time-step $h _ { f }$ and $h _ { s }$ are updated using (7) otherwise $h _ { s }$ is updated by (8)

$$
h _ { s } ( t ) = h _ { s } ( t - \Delta t ) + c _ { s } \nu ( t - \Delta t )\tag{8}
$$

The following pseudo-code illustrates this procedure.

for n=2:k:100   
hf(n)=alpha f\*hf(n-1)+c\*v(n-1)   
hs(n)=alpha s\*hs(n-1)+c\*v(n-1)   
htotal(n)=hf(n)+hs(n)   
// update right hand side //   
RHS=[htotal(n) Sv]   
sol(n)=solve(Yaugmented,RHS)   
for n=n+1:n+k-1   
hf(n)=alpha f\*hf(n-1)+c\*v(n-1)   
hs(n)=hs(n-1)+c\*v(n-1)   
htotal(n)=hf(n)+hs(n)   
// update right hand side //   
RHS=[htotal(n) Sv]   
sol(n)=solve(Yaugmented,RHS)   
end   
end

In the original approach, the slow poles were assumed to be the real ones. When implementing the modified approach to MCN it was found that mostly slow current history sources were associated with alpha close to unity. For so, the criteria for assignment of the slow poles was enhanced to a threshold value of ˛  0.99. This led to the relaxed version of the MCN, i.e., MCNR, in which $h _ { s }$ uses (8) at every time-step. Fig. 2b and c illustrate the updating process for the current sources in the modified and relaxed version of MCN. A pseudo-code to illustrate MCNR follows.

![](images/4945e9ecdf63523f42487e66e325548b74706937fa483d41f1768701f8493cf0.jpg)  
Fig. 3. Injected current in RL parallel circuit.

Relaxed MCN   
for n=2:100   
hf(n)=alpha f\*hf(n-1)+c\*v(n-1)   
hs(n)=hs(n-1)+c\*v(n-1)   
htotal(n)=hf(n)+hs(n)   
// update right hand side //   
RHS=[htotal(n) Sv]   
sol(n)=solve(Yaugmented,RHS)   
end

To illustrate the numerical performance of both approaches, consider again the simple circuit in Fig. 1a, assuming that a step voltage is applied at t = 0 and the modified version of MCN is used to obtain the injected current. The slow branch is represented by the following admittance,

$$
y _ { s } ( s ) = { \frac { 1 0 } { s + 1 0 0 } }\tag{9}
$$

while the fast branch has

$$
y _ { f } ( s ) = { \frac { 4 0 0 } { s + 1 0 ^ { 4 } } }\tag{10}
$$

the fast time-step is $\Delta t _ { 1 } = 1 0$ -s and the slow one is $\Delta t _ { 2 } = 5 0 0 \Delta t _ { 1 }$ The result is depicted in Fig. 3, considering both approaches of MCN, i.e., the modified and relaxed MCN. It can be noticed that all results are in very close agreement despite the large difference between the time-steps the results presented a very close agreement.

It is noteworthy to mention that the accuracy of MCNM formulation for higher values of k, in comparison with [13], is achieved due to the fact that the system conductance matrix stands the same in comparison with the current EMTP-type modeling while in the original MCN it slightly changes to accommodate two different time-steps. This statement also stands for MCNR.

## 4. Integration of the FLE in the time-step loop using MCNR

To evaluate the numerical performance of the proposed methodology, the Relaxed Multiple Companion Networks (MCNR) was applied to the FLE. For the discrete time equivalent of the convolution based models a recursive convolution as detailed in [25] and summarized in Appendix A has been considered. The formulation of the FLE as a Norton equivalent is straightforward, see [12] for details. To modify the FLE to allow the MCNR the formulation of the history current sources has to be slightly modified. The vector of history current sources in phase coordinates is obtained from the one containing the open-circuit and short-circuit counterparts by

$$
\mathbf { I } _ { h i s } = \mathbf { K } . \left[ \begin{array} { l } { \mathbf { i } _ { o c } } \\ { \mathbf { i } _ { s c } } \end{array} \right]\tag{11}
$$

and

$$
\begin{array} { r l } { \mathbf { i } _ { o c } } & { = \mathbf { h } _ { f _ { s c } } + \mathbf { h } _ { s _ { s c } } } \\ { \mathbf { i } _ { s c } } & { = \mathbf { h } _ { f _ { o c } } + \mathbf { h } _ { s _ { o c } } } \end{array}\tag{12}
$$

where ${ \bf h } _ { f _ { s c } }$ is the vector associated with the faster poles in the shortcircuit equivalent (complex poles and real poles with small timeconstants), $\mathbf { h } _ { s _ { s c } }$ is the one related with the slow dynamics, i.e., larger time constants, and $\mathbf { h } _ { f _ { o c } }$ and $\mathbf { h } _ { s _ { o c } }$ are the ones associated with the open-circuit equivalent. The line conductance to be added to the system nodal admittance is obtained as

$$
\mathbf { G } = \mathbf { K } \cdot \left[ \begin{array} { c c } { \mathbf { G } _ { o c } } & { 0 } \\ { 0 } & { \mathbf { G } _ { s c } } \end{array} \right] \cdot \mathbf { K } ^ { - 1 }\tag{13}
$$

where $\mathbf { G } _ { o c }$ is the real-value conductance matrix obtained from the discrete time counterpart of ${ \bf Y } _ { o t }$ c using a time-step t. The same can be said about $\mathbf { G } _ { s c }$ and $\mathbf { Y } _ { s c }$ which also uses the same time-step for discretization.

## 5. Test cases

For the assessment of the accuracy and numerical performance of the MCNR modeling, a set of three test cases has been considered, namely:

1 #1: a 132-kV, 300 m long overhead line.

2 #2: a 132-kV, 10 km long overhead line.

3 #3: a 500-kV, 50 km long double-circuit overhead line.

Fig. 4 depicts the geometries and data for the test cases. All overhead lines assumed ground wires to be continuously grounded and hence eliminated by means of Kron reduction. It is worth mentioning that case #1 aims to reproduce the results of the original FLE paper [12]. Test case #2 considers the same line geometry with a different length instead. Finally, case # 3 seeks to evaluate a highly coupled 500 kV double-circuit. It should be pointed out that this last case stands for a scenario where the FLE is not so efficient, as it was developed to be used to model overhead lines with shorter lengths.

## 5.1. Fitting approach

The nodal admittance matrix of each configuration aforementioned is presented in Fig. 5 in accordance with the structure of (1). In case #1, the given line with 300 m length presents a natural resonance frequency on the admittance matrix around 250 kHz and the frequency sweep is carried out in the range of 0.01 Hz to 1 MHz in order to obtain the data to be fitted, i.e., $\mathbf { Y } _ { n } .$ Case #2 consists in the same overhead line geometry as before with a length of 10 km instead. In this case, the first natural resonance occurs at 7.5 kHz and the frequency sweep of 0.01 Hz up to 150 kHz was considered. Finally, case #3 corresponds to a 50 km double-circuit line and a frequency sweep of 0.01 Hz up to 20 kHz was considered since the first natural resonance is close to 1.5 kHz.

Resorting to the similarity transformation described in Eq. (3) Fig. 6a shows the fitting results for both $\yen 00$ and $\mathbf { Y } _ { s c }$ of case #1. The number of poles used in the fitting were 16 poles for $\yen 00$ and 20 poles for $\mathbf { Y } _ { s c \cdot } \mathsf { A }$ comparison between the fitted eigenvalues and the ones obtained directly from ${ \bf Y } _ { n }$ are depicted in Fig. 6b. For case #2, the rational approximation presented in Fig. 7a was achieved using 38 poles for $\yen 00$ and 50 poles for $\mathbf { Y } _ { s c }$ with the corresponding eigenvalues depicted in Fig. 7b. It is worth mentioning that despite the higher number of resonance peeks and valleys, a high accuracy is attained in all frequency range for this line configuration. In order to perform the evaluation taking into account a circuit highly asymmetric, a 500 kV double-circuit overhead line assigned to case #3 has been adopted. The fitting was achieved with 38 and 60 poles for $\yen 00$ and $\mathbf { Y } _ { s c } ,$ respectively. Again a close agreement between the original and fitted data was achieved as can be observed in Fig. 8.

![](images/892fe1014ed33b57fa6e93e1f5bd352aa4c127a73ea22dc7b061ea560dc5c4a7.jpg)

![](images/0ea6ee4da69c7e15d41389d1b3feffd0718fe1aac12d70bc2b40b59aa14432ea.jpg)  
Fig. 4. System geometry.

![](images/49af6e0be1d0e40edf7fbdad982e95a77f5aacaa03feee9e38df018a6c80d7a3.jpg)  
(a)132kV overhead line - 300 m

![](images/d6720f4f4edd663e7be62ba52fafc8686c26e5f7cbbeb37b68b6a80ad3f34cf6.jpg)  
(b)132kV overhead line -10 km

![](images/dd106ba18cae6f48e408400dd349cf9565cf799a33dcaf696dce4a888050cfb8.jpg)  
(c) 500 kV overhead line - 50 km  
Fig. 5. Elements of $\mathbf { Y } _ { n } .$

![](images/9d7bf40df0387cf2779c4141471d3dc8f918bcc7c692a9efffd7da045ce4ca9f.jpg)  
(a)Fitting of $\mathbf { Y } _ { o c }$ and $\mathbf { Y } _ { s c }$

![](images/b2776567ac5b039b6f8c2b47fb30cad0e5d62798480c3ec7daa4c4ca81e5f6e7.jpg)  
(b)Eigenvalues of $\mathbf { Y } _ { o c } , \mathbf { Y } _ { s c }$ and ${ \bf Y } _ { n }$

Fig. 6. Fitting results – 300 m overhead line.  
![](images/0b45e08584cb3ca1a70dfac5b59c2e2207755b3d8dc087b24c8be07a74500cf5.jpg)  
(a)Fitting of $\mathbf { Y } _ { o c }$ and $\mathbf { Y } _ { s c }$

![](images/fda4195508c00f64e4c8d69bddd60e6f3921b057ad0ed25c873ce77d78ea80f9.jpg)  
(b) Eigenvalues of $\mathbf { Y } _ { o c }$ and $\mathbf { Y } _ { s c }$

Fig. 7. Fitting results – 10 km overhead line.  
![](images/a707d4a61a8fa63ff6e5d5e2638085ab62b0072fe73bd467bd6f84859dde372c.jpg)  
(a)Fitting of $\mathbf { Y } _ { o c }$ and $\mathbf { Y } _ { s c }$

![](images/1fcafd7426c5eb7710783a6882d7d273a7bdc2dbe586089cdc8917ed69c2c782.jpg)  
(b) Eigenvalues of $\mathbf { Y } _ { o c }$ and $\mathbf { Y } _ { s c }$  
Fig. 8. Fitting results – 500 kV overhead line.

## 5.2. Time-domain simulation

The time-domain simulations were carried out in Mathematica using the modified nodal analysis as in [16], based on the approach of the MatEMTP [26]. Furthermore, either the conventional FLE and the MCNR approach considered the order reduction scheme proposed in [27], which in the case of a complex conjugate pair, only one is used with the associated residue being multiplied by a factor of 2 and the imaginary part of the response associated with the pole being disregarded. This gives a close to 50% reduction in computation time for models with mainly complex poles [28].

![](images/99757465549205cfa9d64d63d45043ab8609c3c71186c4ae50c078d464855d2b.jpg)  
Fig. 9. Case #1: circuit for time-domain simulation.

![](images/45a5db64885af7324a44dead7035c780cec7a91426c43d8c22ac07a2595b21ea.jpg)  
(a) Voltage response at faulted and unfaulted phases (terminals #4 and # 5)

![](images/8440f238052446e10a8cb98aac99d5a0cc2397f31ad4a56639396b4eeb19e2a8.jpg)  
(b)Injected current at terminal # 3  
Fig. 10. Time responses for the test using the 300 m line.

## 5.2.1. 300 m 132 kV line

To illustrate this proposed formulation, consider the overhead line circuit as depicted in Fig. 4a. The first case uses the 300 m line and a time-step of 1 -s. The configuration of this test is depicted in Fig. 9. All the switches in the sending end closes at $t _ { 1 } = 0$ , while the switch at the sending end of phase a closes at $t _ { 2 } = 0 . 5 \ : \mathrm { m s }$ , and the value of the inductance is L = 110 mH. When the single phase fault occurs, it provokes a resonance that affects all the other phases.

The choice of slow and fast poles were carried out as follows. Firstly, only real poles in the rational approximation of $\yen 00$ and $\mathbf { Y } _ { s c }$ were allowed to be considered as slow. As the main goal is to speed up the overall simulation time, those poles that presented a discrete time counterpart to be close to one were considered to be slow, more precisely, $\alpha \ge 0 . 9 9$ was the threshold adopted in the sorting between fast and slow poles. At this time, all complex conjugate pairs of poles were treated as fast poles. This criterion led to the rational approximation of $\yen 00$ presenting no slow poles while 10 poles out of the 16 poles used in the rational approximation of $\mathbf { Y } _ { s c }$ can be treated as slow poles.

![](images/7f1a80d888d03e05bb5956c8bc5cd8bd2d6bcf14ad817cb6de5ecda379bbaf00.jpg)  
(a) Voltage response at faulted and unfaulted phases (terminals # 4 and # 5)

![](images/62685f749f79c4120588436d5e5b6a34689f59e3cd54d6fd8ac9b33a360e91fa.jpg)  
(b) Injected current at terminal # 3  
Fig. 12. Time responses at sending and receiving end for the 10 km line.

Fig. 10 shows the time response for voltage at the receiving end of the faulted and one unfaulted phases, i.e., terminals #4 and #5, as well as the injected current at terminal #3. A very close agreement between results was obtained using the conventional FLE and MCNR. The speed up of the simulation time due to using MCNR was close to 35%.

## 5.2.2. 10 km 132 kV line

The second case uses a line length of 10 km and a time-step of 30 -s. For the simulation using MCNR, the same criterion as in the previous test case, $\mathrm { i . e . , } \alpha \geq 0 . 9 9$ was adopted. Using this parameter, no slow poles in the rational approximation of $\mathbf { \Delta Y } _ { o c }$ were found while in $\mathbf { Y } _ { s c }$ 9 poles can be treated as slow with the other 24 poles treated as fast ones. The circuit used for the simulation of the 10 km line is depicted in Fig. 11.

![](images/93e77349265f3f40a7594007241a09a5201a091a09569a89d32191583e5dfe5b.jpg)  
Fig. 11. Case #2: circuit for time-domain simulation.

![](images/add2b59dbf780c8bc430e22e5d4d33f9341e42c5233b10ce1259d9260df88668.jpg)  
Fig. 13. Case #3: circuit for time-domain simulation.

![](images/36805324e555986ccdb11cdc1fd80d85b6d3d73aa0c2260ca9bf6cf1ac010a54.jpg)  
Fig. 14. Voltage response at terminals #9 and #12.

Fig. 12a shows the voltage behavior at faulted and unfaulted phases at the receiving end, i.e., terminals #4 and #5 and the injected current in terminal #3 is shown in Fig. 12b. Again a very close agreement between the results using the conventional FLE and MCNR is found. As the number of poles involved in the rational approximation is larger in this case, there is a decrease in the speed up gain. For this test the improvements are slightly higher than 30%.

## 5.2.3. 50 km 500 kV double-circuit line

This third case aims to evaluate a special configuration with high inherent coupling between phases. It was found that the value of alpha had to be greater than 0.9999 in the rational approximation of $\mathbf { \Delta } \mathbf { \tilde { Y } } _ { o c }$ and $\mathbf { Y } _ { s c } .$ In this case, this criterion led to the rational approximation of $\yen 00$ presenting no slow poles while 10 poles out of the 42 poles used in the rational approximation o $\mathbf { \dot { Y } } _ { s c }$ can be treated as slow poles. The former criteria would correspond to 18 slow poles.

The configuration for this evaluation is presented in Fig. 13, i.e., a three phase energization with one phase short-circuited at the receiving end, similarly as assumed in [29]. Assuming a timestep of $1 0 \mu s ,$ in Fig. 14 the simulated voltage at the unfaulted phases #9 and #12 is shown. Besides providing a simulation without significant loss of accuracy, the proposed methodology reduces considerably the computational burden. The overall simulation time provided a reduction higher than 10% when compared with the simulation when all poles were considered at each time-step. Otherwise the reduction could be as high as 15%.

## 6. Conclusions

This work proposes an approach to improve the numerical performance of full frequency dependent phase-coordinates line models based on rational approximation without a significant loss of accuracy. By relaxing some of the coefficients used in the discrete time equivalent, gains in the overall computation time were achieved. At this point, it should be pointed out that this gain will vary from case to case as it depends on the ratio between fast and slow poles. It is interesting to note that the usage of the folded line equivalent provides a model which is already fast but with the improvements associated with the MCNR it was made even faster.

It was found that only the poles associated with the shortcircuit equivalent could be splitted in a fast and slow grouping. As the open-circuit is associated with higher frequency phenomena it lacks the presence of poles with larger time constants.

Future work is needed to investigate if the approach proposed here can be efficiently implemented using parallel computing and if this approach can be adopted in the time domain realization of frequency dependent network equivalents (FDNE).

## Acknowledgments

This work was supported in part by a funding from Instituto Nacional de Energia Elétrica (INERGE), Coordenac¸ ão de Aperfeic¸ oamento de Pessoal de Nível Superior (CAPES), Conselho Nacional de Ciência, Pesquisa e Desenvolvimento (CNPq) and Fundac¸ ão de Amparo à Pesquisa do Estado de Minas Gerais (FAPEMIG).

## Appendix A. State-space realization

Consider a scalar element with the following transfer function in the frequency domain

$$
I ( s ) = \left( { \frac { r } { s - a } } + d \right) V ( s )\tag{A.1}
$$

where $V ( s )$ and $I ( s )$ are the complex voltage and current, respectively, and r, d and a are real. In the time-domain, it is possible to rewrite (A.1) as

$$
\begin{array} { l } { { \dot { x } ( t ) = a x ( t ) + b \nu ( t ) } } \\ { { \qquad i ( t ) = r x ( t ) + d \nu ( t ) } } \end{array}\tag{A.2}
$$

Using either the trapezoidal integration rule or recursive convolution leads to the following discrete time equivalent

$$
\begin{array} { c } { { x ( n ) = \alpha x ( n - 1 ) + \left( \alpha \lambda + \mu \right) \nu ( n - 1 ) } } \\ { { i ( n ) = x ( n ) + \left( \lambda + d \right) \nu ( n ) } } \end{array}\tag{A.3}
$$

where the coefficients ˛,  and $\mu$ are given by (A.4) if trapezoidal rule is applied

$$
\alpha = \frac { 2 + a \Delta t } { 2 - a \Delta t } \lambda = \mu = \frac { r \Delta t } { 2 - a \Delta t }\tag{A.4}
$$

and in the case recursive convolutions are considered

$$
\begin{array} { l } { \displaystyle \alpha = \exp ( a \Delta t ) } \\ { \displaystyle \lambda = - \frac { r } { a } \left( 1 + \frac { 1 - \alpha } { a \Delta t } \right) } \\ { \displaystyle \mu = \frac { r } { a } \left( \alpha + \frac { 1 - \alpha } { a \Delta t } \right) } \end{array}\tag{A.5}
$$

The equation in (A.3) represents a companion network where

$$
\begin{array} { c } { { i ( n ) = h ( n ) + g \nu ( n ) } } \\ { { h ( n ) = \alpha h ( n - 1 ) + c \nu ( n - 1 ) } } \end{array}\tag{A.6}
$$

with $g = \lambda + d { \mathrm { ~ a n d ~ } } c = \alpha \lambda + \mu$

## References

[1] R.A. Saleh, A.R. Newton, The exploitation of latency and multirate behavior using nonlinear relaxation for circuit simulation, IEEE Trans. Comput. Aided Des. Integr. Circuits Syst. 8 (12) (1989) 1286–1298.

[2] B. Gustavsen, A. Semlyen, Rational approximation of frequency domain responses by vector fitting, IEEE Trans. Power Deliv. 14 (3) (1999) 1052–1061.

[3] B. Gustavsen, Improving the pole relocating properties of vector fitting, IEEE Trans. Power Deliv. 21 (03) (2006) 1587–1592.

[4] D. Deschrijver, M. Mrozowski, T. Dhaene, D.D. Zutter, Macromodeling of multiport systems using a fast implementation of the vector fitting method, IEEE Microw. Wirel. Comp. Lett. 18 (6) (2008) 383–385.

[5] T. Noda, Application of frequency-partitioning fitting to the phase-domain frequency-dependent modeling of overhead transmission lines, IEEE Trans. Power Deliv. 30 (01) (2015) 174–183.

[6] K. Sheshyekani, H.R. Karami, P. Dehkhoda, M. Paolone, F. Rachidi, Application of the matrix pencil method to rational fitting of frequency-domain responses, IEEE Trans. Power Deliv. 27 (04) (2012) 2399–2408.

[7] K. Sheshyekani, B. Tabei, Multiport frequency-dependent network equivalent using a modified matrix pencil method, IEEE Trans. Power Deliv. 29 (5) (2014) 2340–2348.

[8] A. Morched, B. Gustavsen, M. Tartibi, A universal model for accurate calculation of electromagnetic transients on overhead lines and underground cables, IEEE Trans. Power Deliv. 14 (3) (1999) 1032–1038.

[9] T. Noda, Application of frequency-partitioning fitting to the phase-domain frequency-dependent modeling of underground cables, IEEE Trans. Power Deliv. 31 (4) (2016) 1776–1777, http://dx.doi.org/10.1109/TPWRD.2016. 2540526.

[10] B. Gustavsen, Optimal time delay extraction for transmission line modeling, IEEE Trans. Power Deliv. 99 (2016) 1, http://dx.doi.org/10.1109/TPWRD.2016. 2609039.

[11] B. Gustavsen, Avoiding numerical instabilities in the universal line model by a two-segment interpolation scheme, IEEE Trans. Power Deliv. 28 (3) (2013) 1643–1651.

[12] B. Gustavsen, A. Semlyen, Admittance-based modeling of transmission lines by a folded line equivalent, IEEE Trans. Power Deliv. 24 (1) (2009) 231–239.

[13] A.C. Lima, F. Camara, F. Moreira, Exploiting latency in frequency dependent networks equivalents, in: IPST – International Conference on Power System Transients, no. 13IPST044 in IPST 2013, 2013, pp. 1–6.

[15] F. Castellanos, J. Marti, F. Marcano, Phase-domain multiphase transmission line models, Electr. Power Energy Syst. 19 (4) (1997) 241–248, Elsevier Science Ltd.

[14] B. Gustavsen, A. Semlyen, Calculation of transmission line transients using polar decomposition, IEEE Trans. Power Deliv. 13 (3) (1998) 855–862.

[16] M.Y. Tomasevich, A.C. Lima, Some developments on phase coordinates line modeling based on idempotent decomposition, Int. J. Electr. Power Energy Syst. 74 (2016) 410–419.

[17] B. Gustavsen, Rational modeling of multiport systems via a symmetry and passivity preserving mode-revealing transformation, IEEE Trans. Power Deliv. 29 (1) (2014) 199–206.

[18] B. Gustavsen, Fast passivity enforcement for pole-residue models by perturbation of residue matrix eigenvalues, IEEE Trans. Power Deliv. 23 (3) (2008) 2278–2285.

[19] E. Lelarasmee, A.E. Ruehli, A.L. Sangiovanni-Vincentelli, The waveform relaxation method for time-domain analysis of large scale integrated circuits, IEEE Trans. Comput. Aided Des. Integr. Circuits Syst. 1 (3) (1982) 131–145.

[20] M. Crow, M. Ilic, The parallel implementation of the waveform relaxation method for transient stability simulations, IEEE Trans. Power Syst. 5 (3) (1990) 922–932.

[21] A. Semlyen, F. de Leon, Computation of electromagnetic transients using dual or multiple time steps, IEEE Trans. Power Syst. 8 (3) (1993) 1274–1281.

[22] F.A. Moreira, J.R. Martí, Latency techniques for time-domain power system transients simulation, IEEE Trans. Power Syst. 20 (1) (2005) 246–253.

[23] F.A. Moreira, J.R. Mart, L.C. Zanetta Jr., L.R. Linares, Multirate simulations with simultaneous-solution using direct integration methods in a partitioned network environment, IEEE Trans. Circuits Syst. I: Reg. Pap. 53 (12) (2006) 2765–2778.

[24] J.R. Martí, L.R. Linares, J.A. Hollman, F.A. Moreira, Ovni: Integrated software/hardware solution for real-time simulation of large power systems, in: Proceedings of the PSCC, vol. 2, 2002, pp. 1–6.

[25] A. Semlyen, A. Dabuleanu, Fast and accurate switching transient calculations on transmission lines with ground return using recursive convolutions, IEEE Trans. Power Appar. Syst. 94 (2) (1975) 561–571, http://dx.doi.org/10.1109/T-PAS.1975.31884.

[26] J. Mahseredjian, F. Alvarado, Creating an electromagnetic transients program in matlab: Matemtp, IEEE Trans. Power Deliv. 12 (1) (1997) 380–388, http:// dx.doi.org/10.1109/61.568262.

[27] T. Noda, Identification of a multiphase network equivalent for electromagnetic transient calculations using partitioned frequency response, IEEE Trans. Power Deliv. 20 (02) (2005) 1134–1142.

[28] B. Gustavsen, H.M.J.D. Silva, Inclusion of rational models in an electromagnetic transients program: Y-parameters, z-parameters, s-parameters, transfer functions, IEEE Trans. Power Deliv. 28 (2) (2013) 1164–1174.

[29] B. Gustavsen, Frequency-dependent transmission line modeling utilizing transposed conditions, IEEE Trans. Power Deliv. 17 (3) (2002) 834–839.