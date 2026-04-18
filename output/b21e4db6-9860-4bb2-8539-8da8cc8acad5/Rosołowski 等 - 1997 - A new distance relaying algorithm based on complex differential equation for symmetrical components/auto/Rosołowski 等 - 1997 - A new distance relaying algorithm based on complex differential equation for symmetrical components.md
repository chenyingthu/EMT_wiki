# A new distance relaying algorithm based on complex diferential equation for symmetrical components

Eugeniusz Rosolowski a,\*, Jan Izykowski a, Bogdan Kasztenny ^, Murari Mohan Saha b

a The Technical University of Wroctaw (1-8), Wyb.Wyspianskiego 27,50-370 Wroclaw,Poland bABB Network Partner,Vsteras,Sweden

Received 8 February 1996; accepted 6 September 1996

## Abstract

This paper presents anew digital impedance measuring technique for transmision lines thatcombines symmetrical components and the complex diferential equationofanequivalentfault loopcircuit.The phase voltagesand currents attherelaying point aretransformed intosymmetrical componentsusing Fourier flters of short window length.Depending onfault type，an appropriate faultloopcircuitisfred,signalsof whicharetheappropriatesymmetricalcomponents,whileaparameterofwich isthe positive sequence impedancebeinga geometrical measureof the distance fromtherelaying point toafault.The impedance, however，ismeasuredveryfastbyon-linesolvingthecomplexdiferentialequationoriginatedforthisfaultloopcircuit. Consequently，this approach combines frequencydomain estimationofsymmetricalcomponents (accrate fltration)and time domain measurement of positive sequence impedance (high speed response).

The presented method suitswellthe protectionof paralel linesagainst high-resistance faults occuring very close tothe farend of aline.Anew method is proposedfordetectinghigh-resistance faultsanddeciding whichlineoutoftwoparalelinesactually suffers a fault.

The included EMTP test results demonstrate the efciency of the proposed relaying algorithm.@1997 Elsevier Science S.A.

Keywords: Digital protection; Symmetrical components; Fault impedance estimation; Line protection

## 1. Introduction

A digital distance relaying algorithm based upon symmetrical components was introduced two decades ago [l]. This protection method utilizes certain relations between voltages and currents in a three-phase postfault power system [1,2]: the phase voltages and currents are transformed into symmetrical components by means of digital filtration. Depending on fault type, an appropriate fault loop model is composed from symmetrical components of voltages and currents to that the impedance resulting from the equivalent voltage and current is the positive sequence impedance being a geometrical measure of the distance to a fault. This relaying method,however,is usually implemented in the frequency domain,i.e. phasors of voltage and current symmetrical components are calculated and based on them the apparent impedance is estimated. Consequently,the resulting impedance algorithm cannot be very fast due to the window length of used filters.

Ultra-high speed impedance estimation,in turn,is natural in the time domain methods. This group of algorithms based on the resistive-inductive model of a fault loop circuit,usually neglecting the shunt capacitances,assumes the appropriate voltages and currents as measured and solves the appropriate differential equation with respect to resistance (R） and reactance (X) of positive sequence. Various approaches to numerical differentiation and solution of the relevant equation originate a number of different relaying methods of this kind [3-5].

As its innovative contribution,this paper merges the gains of those two approaches: symmetrical components are the base for distance relaying and are numerically measured by means of Fourier filters with a short data window providing sufficient voltage and current filtration. Depending on the type of fault, an equivalent fault loop circuit is next composed with complex and instantaneous symmetrical components as signals and positive sequence impedance as a parameter. The resulting differential equation is next solved with respect to R and X in the time domain (Section 2).A single, but complex differential equation is re-written for its real and imaginary parts enabling to find the two sought variables (R and X) using the data at a single sampling instance,which further speeds up the impedance estimation.

In the case of parallel transmission lines,a number of problems arises when using distance protection [6] due to mutual coupling,back feed, in-feed,and poor discrimination between faulty and healthy lines,especially in the case of faults near to the far end bus. To overcome these difficulties,the method based on certain comparison between impedances of both lines is proposed in the literature.A more sensitive method [6] relies on comparison of quantities proportional to the average of the currents in each phase of the parallel lines.These methods,however,fail in cases of faults occurring very close to the far end of the protected line.

The technique proposed in this paper in addition enables:(1) detection of high-resistance faults on parallel transmission lines,and (2) distinguishment of which line out of two parallel lines actually suffers a fault (Section 3).

The developed relaying methods were examined by means of EMTP simulation [7]. Sample results of the performed studies,which show both speed and accuracy of the distance estimation are included and discussed (Section 4).

## 2.The distance relaying algorithm

## 2.1.Equivalent fault loop circuit

To derive the protection algorithm, let us consider the standard double-circuit line arrangement shown in Fig.1 [l]. Assuming that the fault impedance is to be measured by the protective relay of the line A at the substation I, the equivalent sequence networks are obtained as shown in Fig.2.These networks correspond to the following equations:

![](images/ac75654b04637318b1a32364e87ada048bc069986250c49531bdd0a4c5e55d4c.jpg)  
Fig.1.Double-circuit line arrangement used in the algorithm description.

![](images/66e79eefa57877c91f867840b10445af92cfe137fbbac729a28b8e18a2402e6a.jpg)  
Fig.2.Equivalent sequence circuits of the fault loop.

$$
{ \underline { { v } } } _ { 0 \mathrm { f } } ( t ) = { \underline { { v } } } _ { 0 } ( t ) - R _ { 0 } { \dot { z } } _ { 0 } ( t ) - L _ { 0 } { \frac { \mathrm { d } { \dot { z } } _ { 0 } ( t ) } { \mathrm { d } t } } - R _ { \mathrm { o m } } { \dot { z } } _ { 0 \mathrm { B } } ( t )
$$

$$
- L _ { \mathrm { o m } } \frac { \mathrm { d } i _ { 0 B } ( t ) } { \mathrm { d } t } - R _ { 0 t } i _ { 0 t } ( t )\tag{1a}
$$

$$
v _ { \mathrm { 1 f } } ( t ) = \underline { { v } } _ { 1 } ( t ) - R _ { 1 } \underline { { i } } _ { 1 } ( t ) - L _ { 1 } \frac { \mathrm { d } \underline { { i } } _ { 1 } ( t ) } { \mathrm { d } t } - R _ { 1 \mathrm { f } } \underline { { i } } _ { 1 \mathrm { f } } ( t )\tag{1b}
$$

$$
v _ { 2 \mathrm { f } } ( t ) = v _ { 2 } ( t ) - R _ { 1 } { \dot { v } } _ { 2 } ( t ) - L _ { 1 } { \frac { \mathrm { d } { \dot { v } } _ { 2 } ( t ) } { \mathrm { d } t } } - R _ { 2 \mathrm { f } } { \dot { v } } _ { 2 \mathrm { f } } ( t )\tag{lc}
$$

in which all the quantities,except the zero sequence current in the line $\begin{array} { r } { B ; i _ { 0 \ B } ( t ) ; } \end{array}$ ，are related to the line A.

Currents and voltages in Eqs.(la),(lb) and (lc) are, in general, defined as:

$$
\underline { { x } } ( t ) = X ( t ) \exp [ \mathbf { j } ( \omega t + \psi ( t ) ) ] = x _ { x } ( t ) + \mathbf { j } x _ { y } ( t )\tag{2}
$$

It should be noted that symmetrical components of voltages $\underline { { v } } _ { 0 } ( t ) , ~ \underline { { v } } _ { 1 } ( t ) , ~ \underline { { v } } _ { 2 } ( t )$ and currents i(t),i(t),i(t) are to be measured at the relay location,while the components of voltages at the fault point $\underline { { v } } _ { 0 \mathsf { f } } ( t ) , \ \underline { { v } } _ { 1 \mathsf { f } } ( t )$ and $\underline { { v } } _ { 2 \mathsf { f } } ( t )$ are determined by the fault type [1].

The distance to a fault, l, can be found by estimation of positive sequence parameters, $R _ { 1 } , \ L _ { 1 }$ of the fault loop:

$$
R _ { 1 } = l R _ { 1 } ^ { \prime } , ~ L _ { 1 } = l L _ { 1 } ^ { \prime }\tag{3}
$$

where $R _ { 1 } ^ { \prime }$ and $L _ { 1 } ^ { \prime }$ are the line resistance and inductance per unit length.

The relation analogous to Eq.(3) is valid for the zero sequence parameters. Introducing the following coefficients:

$$
\begin{array} { l } { { m _ { \mathrm { R } } = \displaystyle \frac { R _ { 0 } ^ { \prime } } { R _ { 1 } ^ { \prime } } \ : , \qquad m _ { \mathrm { L } } = \displaystyle \frac { L _ { 0 } ^ { \prime } } { L _ { 1 } ^ { \prime } } \ : , \qquad } } \\ { { m _ { \mathrm { R m } } = \displaystyle \frac { R _ { 0 \mathrm { m } } ^ { \prime } } { R _ { 1 } ^ { \prime } } \ : , \qquad m _ { \mathrm { L m } } = \displaystyle \frac { L _ { 0 \mathrm { m } } ^ { \prime } } { L _ { 1 } ^ { \prime } } \ : } } \end{array}\tag{4}
$$

Eq.(la) may be expressed in terms of positive sequence parameters of the fault loop, $R _ { 1 } , L _ { 1 }$ as follows:

$$
\begin{array} { l } { { \displaystyle v _ { \mathrm { o f } } ( t ) = \underline { { v } } _ { 0 } ( t ) - R _ { 1 } ( m _ { \mathrm { R } } i _ { 0 } ( t ) + m _ { \mathrm { R m } } i _ { 0 \mathrm { B } } ( t ) ) } } \\ { { \displaystyle ~ - { L } _ { 1 } \frac { \mathrm { d } } { \mathrm { d } t } \left( m _ { \mathrm { L } } i _ { 0 } ( t ) + m _ { \mathrm { L m } } i _ { 0 \mathrm { B } } ( t ) \right) - R _ { 0 \mathrm { t } } i _ { 0 \mathrm { f } } ( t ) } } \end{array}\tag{5}
$$

![](images/81141997d9158fa0af18582d39592c17f611832c2b621016bb9551faad8cf7c6.jpg)  
Fig.3.Equivalent fault loop circuit.

Symmetrical components of voltages at the fault location yof, Uf, U2f can be eliminated taking into account sequence conditions relevant to the fault type. As a result,the equivalent fault circuit valid for all fault types is obtained as shown in Fig.3.The general equation for this circuit is stated as follows:

$$
\underline { { v } } _ { \mathrm { e } } ( t ) = R _ { \mathrm { l } } \underline { { i } } _ { \mathrm { e R } } ( t ) + L _ { \mathrm { l } } \frac { \mathrm { d } \underline { { i } } _ { \mathrm { e L } } ( t ) } { \mathrm { d } t } + \underline { { v } } _ { \mathrm { e f } } ( t )\tag{6}
$$

where $\smash { \underline { { v _ { \mathrm { e } } } } ( t ) , \ \underline { { v } } _ { \mathrm { e f } } ( t ) , \ \underline { { i } } _ { \mathrm { e f } } ( t ) }$ and $\underline { { i } } _ { \mathrm { e L } } ( t )$ are the appropriate voltage and current signals and sources in the equivalent circuit， respectively. Voltage $\underline { { v } } _ { \mathrm { e } } ( t )$ and currents $\underline { { i } } _ { \mathrm { e R } } ( t ) , \ \underline { { i } } _ { \mathrm { e L } } ( t )$ in Eq. (6) are determined from the measured symmetrical components, taking into account the fault type. For example, for an a-g fault, the sequence condition is:

$$
\underline { { v } } _ { 0 \mathrm { f } } ( t ) + \underline { { v } } _ { 1 \mathrm { f } } ( t ) + \underline { { v } } _ { 2 \mathrm { f } } ( t ) = 0\tag{7}
$$

Inserting Eqs. (1b),(lc) and (5) into Eq.(7) results in Eq. (6) being the general eqation with the following signals:

$$
v _ { \mathrm { e } } ( t ) = v _ { 0 } ( t ) + \underline { { v } } _ { 1 } ( t ) + \underline { { v } } _ { 2 } ( t )\tag{8a}
$$

$$
\underline { { i } } _ { \mathrm { e R } } ( t ) = \underline { { i } } _ { 1 2 } ( t ) + \underline { { i } } _ { 0 \mathrm { R } } ( t ) = \underline { { i } } _ { 1 } ( t ) + \underline { { i } } _ { 2 } ( t ) + m _ { \mathrm { R } } \underline { { i } } _ { 0 } + m _ { \mathrm { R m } } \underline { { i } } _ { 0 \mathrm { B } }\tag{8b}
$$

$$
\begin{array} { r } { i _ { \mathrm { e L } } = \dot { \underline { i } } _ { 1 2 } ( t ) + \dot { \underline { i } } _ { 0 \mathrm { L } } ( t ) = \dot { \underline { i } } _ { 1 } ( t ) + \dot { \underline { i } } _ { 2 } ( t ) + m _ { \mathrm { L } } \dot { \underline { i } } _ { 0 } + m _ { \mathrm { L m } } \dot { \underline { i } } _ { 0 \mathrm { B } } } \end{array}\tag{8c}
$$

$$
v _ { \mathrm { e f } } ( t ) = R _ { 0 \mathrm { f } } i _ { 0 \mathrm { f } } ( t ) + R _ { 1 \mathrm { f } } i _ { 1 \mathrm { f } } ( t ) + R _ { 2 \mathrm { f } } { \underline { { i } } } _ { 2 \mathrm { f } } ( t )\tag{8d}
$$

The relevant conditions and parameters for the remaining types of faults are presented in Table 1.

Certainly，voltage ${ \underline { { v } } } _ { e } ( t )$ can not be estimated by measurements on one side of the protected line. Its neglection $( { \underline { { v } } } _ { \mathrm { e f } } ( t ) = 0 )$ ，as will be the case in all further considerations in this paper,is a source of the algorithm error [2].

In general, the sought fault loop positive sequence parameters $R _ { 1 } , L _ { 1 } ,$ 、are next calculated from Eq. (6) by use of one of the well known frequency domain algorithms [3.8]. In this paper,however，the complex differential Eq.(6) is solved in the time domain to speed-up the measurement and merge the gains resulting from both the frequency domain (accurate filtration) and time domain (speed of response, immunity of frequency changes,etc.） approaches.

## 2.2.Fault impedance estimation based on a differential equation

By analogy with Eq. (2), the discrete model of the voltage (or current） signals from Eq.(6) takes the complex form, for example:

$$
{ \underline { { v _ { \mathrm { e } } } } } ( k ) = v _ { \mathrm { e } x } ( k ) + \mathrm { j } v _ { \mathrm { e } y } ( k )\tag{9}
$$

Assuming that the k-th sample of the signal $x ( k ) ,$ which stands for either voltage or current in Eq. (6), is represented by the operator S[x(k)], and the signal derivative by $D [ x ( k ) ]$ ，the discrete form of Eq. (6) reduces to:

$$
S [ v _ { \mathrm { e } x } ( k ) ] = S [ i _ { \mathrm { e } \mathbf { R } x } ( k ) ] R _ { 1 } + L _ { 1 } D [ i _ { \mathrm { e } \mathbf { L } x } ( k ) ]
$$

Parameters of the equivalent fault circuit for different types of faults
<table><tr><td>Fault type</td><td>Sequence condition</td><td>L</td><td> $\underline { { i } } _ { 1 2 }$ </td><td> $\pmb { i } _ { 0 \mathrm { R } }$ </td><td> $\underline { { i } } _ { 0 \mathrm { L } }$ </td></tr><tr><td> 3-phase</td><td> $\underline { { v } } _ { 1 \mathrm { f } } = 0$ </td><td> $\underline { { \mathfrak { v } } } _ { 1 }$ </td><td> $\underline { { i } } _ { 1 }$ </td><td></td><td></td></tr><tr><td>b-c</td><td> $\underline { { v } } _ { 1 \mathrm { f } } = \underline { { \mathbf { V } } } _ { 2 \mathrm { f } }$ </td><td> $\underline { { v } } _ { 1 } - \underline { { v } } _ { 2 }$ </td><td> $\underline { { i } } _ { 1 } - \underline { { i } } _ { 2 }$ </td><td></td><td></td></tr><tr><td> $a - b$ </td><td> $\pmb { a } \underline { { v } } _ { 1 \uparrow } = \mathbf { a } ^ { 2 } \underline { { v } } _ { 2 \uparrow }$ </td><td> ${ \underline { { v } } } _ { 1 } - a { \underline { { v } } } _ { 2 }$ </td><td> $\underline { { i } } _ { 1 } - \underline { { a } } \underline { { i } } _ { 2 }$ </td><td></td><td></td></tr><tr><td>a-c</td><td> $a ^ { 2 } { \underline { { v } } } _ { 1 \mathrm { f } } = a { \underline { { v } } } _ { 2 \mathrm { f } }$ </td><td> $a v _ { 1 } - v _ { 2 }$ </td><td> $a \underline { { i } } _ { 1 } - \underline { { i } } _ { 2 }$ </td><td></td><td></td></tr><tr><td> $\scriptstyle \mathbf { b - c - g }$ </td><td> $\underline { { v } } _ { 1 \mathrm { f } } = \underline { { v } } _ { 2 \mathrm { f } }$ </td><td>As in case b-c</td><td></td><td></td><td></td></tr><tr><td></td><td> ${ \underline { { v } } } _ { 2 \mathsf { f } } = { \underline { { v } } } _ { 0 \mathsf { f } }$ </td><td> ${ \underline { { \boldsymbol { v } } } _ { 2 } } - { \underline { { \boldsymbol { v } } } _ { 0 } }$ </td><td> $\underline { { i } } _ { 2 }$ </td><td> $- m _ { \mathrm { R } } i _ { 0 } - m _ { \mathrm { R } \mathrm { m } } i _ { 0 \mathrm { B } }$ </td><td> $- m _ { \mathrm { L } } i _ { 0 } - m _ { \mathrm { L } , \mathrm { m } } i _ { 0 } \mathrm { B }$ </td></tr><tr><td rowspan="4">a-b-g</td><td> $\underline { { v } } _ { 1 \mathrm { f } } = \underline { { v } } _ { 0 \mathrm { f } }$ </td><td> ${ \underline { { \boldsymbol { v } } } } _ { 1 } - { \underline { { \boldsymbol { v } } } } _ { 0 }$ </td><td> $\underline { { i } } _ { 1 }$ </td><td> $- m _ { \mathrm { R } } i _ { 0 } - m _ { \mathrm { R m } } i _ { 0 \mathrm { B } }$ </td><td> $- m _ { \mathrm { L } } i _ { 0 } - m _ { \mathrm { L } } i _ { 0 } \mathrm { B }$ </td></tr><tr><td> $\boldsymbol { a } \underline { { v } } _ { 1 \mathrm { f } } = \boldsymbol { a } ^ { 2 } \underline { { v } } _ { 2 \mathrm { f } }$ </td><td>As in case a-b</td><td></td><td></td><td></td></tr><tr><td> $a ^ { 2 } { \underline { { v } } } _ { 2 \mathrm { f } } = { \underline { { v } } } _ { 0 \mathrm { f } }$ </td><td> $a ^ { 2 } { \underline { { v } } } _ { 2 } - { \underline { { v } } } _ { 0 }$ </td><td> $a ^ { 2 } { \underline { { i } } } _ { 2 }$ </td><td> $- m _ { \mathrm { R } } i _ { 0 } - m _ { \mathrm { R } } i _ { 0 \mathrm { B } }$ </td><td> $- m _ { \mathrm { L } } i _ { 0 } - m _ { \mathrm { L m } } i _ { 0 } \mathbf { s }$ </td></tr><tr><td> $a _ { \perp \mathsf { f } } = \underline { { v } } _ { 0 \mathsf { f } }$ </td><td> $a { \underline { { v } } } _ { 1 } - { \underline { { v } } } _ { 0 }$ </td><td> $a \dot { \iota } _ { 1 }$ </td><td> $- m _ { \mathrm { R } } i _ { 0 } - m _ { \mathrm { R } } i _ { 0 } \mathbf { { B } }$ </td><td> $- m _ { \mathrm { { L } } } i _ { 0 } - m _ { \mathrm { { L } } m } i _ { 0 } \mathrm { { B } }$ </td></tr><tr><td rowspan="3"> $\mathsf { a - c - g }$ </td><td> $a ^ { 2 } { \underline { { v } } } _ { 1 \mathrm { f } } = a { \underline { { v } } } _ { 2 \mathrm { f } }$ </td><td>As in case a-c</td><td></td><td></td><td></td></tr><tr><td> ${ a \underline { { v } } _ { 2 \mathsf { f } } = \underline { { v } } _ { 0 \mathsf { f } } }$ </td><td> $a _ { \scriptscriptstyle \perp } - \underline { { v } } _ { 0 }$ </td><td> $a \dot { \iota } _ { 2 }$ </td><td> $- m _ { \mathrm { R } } i _ { 0 } - m _ { \mathrm { R } } i _ { 0 } \mathbf { { s } }$ </td><td> $- m _ { \mathrm { L } } i _ { 0 } - m _ { \mathrm { L m } } i _ { 0 } \mathrm { B }$ </td></tr><tr><td> $a ^ { 2 } { \underline { { v } } } _ { 1 \mathrm { f } } = { \underline { { v } } } _ { 0 \mathrm { f } }$ </td><td> $a ^ { 2 } { \underline { { v } } } _ { 1 } - { \underline { { v } } } _ { 0 }$ </td><td> $a ^ { 2 } { \underline { { i } } } _ { 1 }$ </td><td> $- m _ { \mathrm { { R } } } { i _ { 0 } } - m _ { \mathrm { { R } } } { i _ { 0 } } \mathbf { { s } }$ </td><td> $- m _ { \mathrm { L } } i _ { 0 } - m _ { \mathrm { L } \mathrm { m } } i _ { 0 } \mathrm { B }$ </td></tr><tr><td>a-g</td><td> ${ \underline { { v } } } _ { 0 f } + { \underline { { v } } } _ { 1 f } + { \underline { { v } } } _ { 2 f } = 0$ </td><td> $\underline { { v } } _ { 0 } + \underline { { v } } _ { 1 } + \underline { { v } } _ { 2 }$ </td><td> $\underline { { i } } _ { 1 } + \underline { { i } } _ { 2 }$ </td><td> $m _ { \mathrm { R } } i _ { 0 } + m _ { \mathrm { R m } } i _ { 0 \mathrm { B } }$ </td><td> $m _ { 1 } \mathbf { \dot { \omega } } _ { 0 } + m _ { { \mathbf { \dot { \omega } } } } \mathbf { \dot { \omega } } _ { 0 } \mathbf { \dot { \omega } }$ </td></tr><tr><td>b-g</td><td> $\underline { { v } } _ { 0 f } + a ^ { 2 } \underline { { v } } _ { 1 f } + a \underline { { v } } _ { 1 f } = 0$ </td><td> ${ \underline { { v } } } _ { 0 } + a ^ { 2 } { \underline { { v } } } _ { 1 } + a { \underline { { v } } } _ { 2 }$ </td><td> $a ^ { 2 } i _ { 1 } + a i _ { 2 }$ </td><td> $m _ { \mathrm { R } } \dot { \iota } _ { 0 } + m _ { \mathrm { R m } } \dot { \iota } _ { 0 \mathrm { B } }$ </td><td> $m _ { \mathrm { L } } i _ { 0 } + m _ { \mathrm { L } } { } _ { \mathrm { m } } i _ { 0 } \mathbf { s }$ </td></tr><tr><td>cig</td><td> ${ \underline { { v } } } _ { 0 \mathrm { f } } + a { \underline { { v } } } _ { 1 \mathrm { f } } + a ^ { 2 } { \underline { { v } } } _ { 2 \mathrm { f } } = 0$ </td><td> $\underline { { v } } _ { 0 } + a \underline { { v } } _ { 1 } + a ^ { 2 } \underline { { v } } _ { 2 }$ </td><td> $a \ i _ { 1 } + a ^ { 2 } \ i _ { 2 }$ </td><td> $m _ { \mathrm { R } } i _ { 0 } + m _ { \mathrm { R } \mathrm { m } } i _ { 0 \mathrm { B } }$ </td><td> $m _ { \mathrm { L } } i _ { 0 } + m _ { \mathrm { L } , m } i _ { 0 \mathrm { B } }$ </td></tr></table>

$a = - { \frac { 1 } { 2 } } + \mathbf { j } { \frac { \sqrt { 3 } } { 2 } } ,$ $a ^ { 2 } = - { \frac { 1 } { 2 } } - \mathbf { j } { \frac { \sqrt { 3 } } { 2 } } .$

$$
S [ v _ { \mathrm { e } y } ( k ) ] = S [ i _ { \mathrm { e R } y } ( k ) ] R _ { 1 } + L _ { 1 } D [ i _ { \mathrm { e L } y } ( k ) ]\tag{10}
$$

Certainly, the orthogonal components (denoted by x or y at the last position of the subscripts) of the respective signals $\underline { { v } } _ { \mathrm { e } } , \underline { { i } } _ { \mathrm { e R } } , \underline { { i } } _ { \mathrm { e L } }$ are available by applying an appropriate signal pre-processing procedure.

Eq. (10) is now resolved with respect to $R _ { 1 }$ and $L _ { \mathrm { t } } \mathrm { : }$

$$
\begin{array} { r } { R _ { 1 } = \frac { S [ v _ { \mathrm { e x } } ( k ) ] D [ i _ { \mathrm { e L y } } ( k ) ] - S [ v _ { \mathrm { e y } } ( k ) ] D [ i _ { \mathrm { e L x } } ( k ) ] } { S [ i _ { \mathrm { e R } x } ( k ) ] D [ i _ { \mathrm { e L y } } ( k ) ] - S [ i _ { \mathrm { e R } y } ( k ) ] D [ i _ { \mathrm { e L x } } ( k ) ] } } \\ { L _ { 1 } = \frac { S [ v _ { \mathrm { e y } } ( k ) ] S [ i _ { \mathrm { e R x } } ( k ) ] - S [ v _ { \mathrm { e x } } ( k ) ] S [ i _ { \mathrm { e R } y } ( k ) ] } { S [ i _ { \mathrm { e R } x } ( k ) ] D [ i _ { \mathrm { e L } y } ( k ) ] - S [ i _ { \mathrm { e R } y } ( k ) ] D [ i _ { \mathrm { e L x } } ( k ) ] } } \end{array}\tag{11}
$$

Various numerical operators S[:] and D[:] are recommended for these calculations [3,9].In the simpliest case,as used in the performed studies, these operators take the following form:

$$
S [ x ( k ) ] = \frac { x ( k ) + x ( k - 1 ) } { 2 } ,
$$

$$
D [ x ( k ) ] = \frac { x ( k ) - x ( k - 1 ) } { T _ { \mathrm { s } } }\tag{12}
$$

where $T _ { \mathrm { s } }$ is the sampling period.

## 3. The modified technique for paralel lines

Distance relays installed on parallel lines meet difficulty in detecting high-resistance faults occurring close to the far end of the line as well as in detecting which line actually suffers a fault. The fundamental Eq. (6) may be the base for fault detection and identification in such cases. In the proposed method, the following voltage drops are calculated first:

$$
\begin{array} { l } { { \displaystyle \underline { { v _ { \mathrm { e A } } ( t ) = R _ { \mathrm { 1 } } ^ { * } i _ { \mathrm { e R A } } ( t ) + L _ { \mathrm { 1 } } ^ { * } \frac { \mathrm { d } i _ { \mathrm { e L A } } ( t ) } { \mathrm { d } t } } } } } \\ { { \displaystyle \underline { { v _ { \mathrm { e B } } ( t ) = R _ { \mathrm { 1 } } ^ { * } i _ { \mathrm { e R B } } ( t ) + L _ { \mathrm { 1 } } ^ { * } \frac { \mathrm { d } i _ { \mathrm { e L B } } ( t ) } { \mathrm { d } t } } } } } \end{array}\tag{13}
$$

where R\*,L\* are positive sequence parameters of the whole line.Currents and their derivatives in Eq.(13) are numerated as presented in Table 1 and Eq. (12). Note that the signals $\pmb { v _ { e A } }$ and ${ \underline { { v } } } _ { \tt e B }$ are composed as the weighted sums of the appropriate currents and their derivatives. The positive sequence impedance components play the role of weighting factors. Note also that the parameters for the whole line are used instead of actually measured impedance components.

The following condition is proposed to detect the fault state:

$$
\left| \left| \underline { { v } } _ { \mathrm { e A } } \right| - \left| \underline { { v } } _ { \mathrm { e B } } \right| \right| > \Delta v\tag{14}
$$

where △v is an appropriate threshold value. The faulty line,in turn, is selected as the one with the larger voltage magnitude $\left| \underline { { v } } _ { \mathrm { e A } } \right| \ : \mathrm { o r } \ : \left| \underline { { v } } _ { \mathrm { e B } } \right|$

![](images/ea97776418dfb5e0f4bddf24bbbeffdcb1288003e9a8238e6280d592f895e7af.jpg)  
Fig. 4. Single phase diagram of the test power system.

Certainly,application of the developed algorithms Eqs.(11) and (l4) requires earlier determination of a fault type. One of the known phase selection methods can be applied for this purpose [2].

## 4. Simulation results

The properties of the developed algorithms were studied by means of the EMTP simulation [7]. The single phase diagram of the 50 Hz power system under study is shown in Fig. 4. Current and voltage relaying signals were filtered by analog anti-aliasing filters with cut-off frequency $f _ { \mathrm { c } } = 3 5 0$ Hz and sampled with the frequency rate $f _ { \mathrm { s } } = 1$ kHz (20 samples per cycle).

## 4.1.Distance protection algorithm

The estimation of the distance to a fault comprises of three basic stages:

estimation of symmetrical components by use of a pair of half a cycle Fourier orthogonal filters (see Appendix $\mathbf { A } ) ;$

· phase selection; and

· calculation of the positive sequence impedance components $R _ { 1 } , \ L _ { 1 }$ by means of Eqs. (l1) and (12).

The estimates of resistance and reactance calculated by protective relays at the substations I and II during an a-b-g fault at location F are shown in Fig. 5. The presented plots show that the acceptable response of the impedance estimator is obtained in about half a cycle of the fundamental frequency. The performed simulations showed also that the developed algorithm is immune to distortions of different kinds.

## 4.2.Protection of parallel lines

Trajectories of fault impedance measured by the relays of both parallel lines at the substation I, for the c-g fault (Fig. 4) with fault resistance of 50 Ω, are shown in Fig.6.In this case,the impedance criterion fails: the impedance trajectories of both the relays (A and B) are located far away from the first protective zone, regardless of the shape used for it. Thus, selection of the faulty line on the base of the impedance criterion is impossible. The results of applying the algorithm Eq. (14) overcoming this difficulty,are depicted in Fig.7.

a)  
![](images/3a32c240247b98ddf02ae3613fa4da0a6379d1de5b3955b49c742809ddb4b0d6.jpg)  
Fig.5.Estimates of resistance (a) and reactance (b) for a-b-g fault as in Fig.4 calculated by the relays of the lines A and B at the substation I; fault resistance $R _ { \mathrm { f } } = 0 ~ \Omega$

The relay at the substation I (Fig. 7(a)) detects the fault after some 7 ms when the differential signal Eq. (14) exceeds the threshold. Even before fault detection the signal $\left| \underline { { v } } _ { \mathrm { e A } } \right|$ is higher than $\left| \underline { { v } } _ { \mathrm { e B } } \right|$ indicating that the line A suffers a fault. The relay at the substation II (Fig.7(b)) detects this fault much faster (2 ms) since this fault is close to this substation. The discrimination between faulty and healthy lines is also very strong.

![](images/9a64a1e127f357ac66d78b5b1623960ee3e53986d70fd85ab8dada4c100b85b6.jpg)  
Fig. 6.Fault impedance trajectories for c-g fault as in Fig.4 calculated by the relays of the lines A and B at the substation I; fault resistance $R _ { \mathrm { f } } = 5 0 \Omega$

a)  
![](images/bf5aa0e3a06059519f1837074dd73c2c20bf80fc618a422bd13434ac2a9d9c57.jpg)

![](images/8099d8940ba92d6696d1ff2f9fac95a8cc4e4269ac06834d46788437b243e22d.jpg)  
Fig.7.Plots of magnitudes of voltage drops (13) and their differences for the fault as in Fig.6,calculated by the relays of the linesA and B at the substations I (a) and II (b); secondary volts.

Generally，the algorithm proposed for parallel lines detects and locates faults in half a cycle time interval.

Certainly，selectivity and speed of operation of the proposed algorithm are higher for faults with lower fault resistances than the assumed extreme value of 50 Ω.

## 5. Conclusions

A new distance relaying algorithm for transmission lines is presented. The method employs the symmetrical components theory to determine the equivalent fault loop circuit. The symmetrical components of currents and voltages are estimated by use of half a cycle nonrecursive Fourier filters. The apparent positive sequence impedance components are estimated by on-line solution of the differential equation describing the equivalent circuit. Consequently, the proposed method enables a balance between the frequency domain (estimation of symmetrical components) and the time domain (estimation of impedance) approaches;which,in turn,enables a balance between accuracy of filtration and speed of response.

For the case of parallel transmision lines, the modified algorithm is offered based on calculation of the magnitudes of voltage drops in the equivalent fault circuit for both the parallel lines. The method allows effective detection and identification of ground faults with large fault resistances.

The developed relaying methods have been successfully tested by means of EMTP simulations showing good transient and steady state performance. Even in extreme cases of high-resistance faults occurring very close to the far end of the parallel line,the total fault detection and identification time does not exceed half a cycle.

## Appendix A

In this paper,the current and voltage symmetrical components have been calculated according to the following algorithm.

(1) First, the $\alpha , \beta , 0$ components are numerated from the three-phase signals (Clarke transformation):

$$
{ \left[ \begin{array} { l } { f _ { 0 } ( k ) } \\ { f _ { \alpha } ( k ) } \\ { f _ { \beta } ( k ) } \end{array} \right] } = { \frac { 1 } { 3 } } { \left[ \begin{array} { l l l } { 1 } & { 1 } & { 1 } \\ { 2 } & { - 1 } & { - 1 } \\ { 0 } & { { \sqrt { 3 } } } & { - { \sqrt { 3 } } } \end{array} \right] } { \left[ \begin{array} { l } { f _ { \mathrm { a } } ( k ) } \\ { f _ { \mathrm { b } } ( k ) } \\ { f _ { \mathrm { c } } ( k ) } \end{array} \right] }\tag{15}
$$

(2) Next, complex representation of $f _ { 0 } ( k ) , f _ { \alpha } ( k ) , f _ { \beta } ( k )$ is obtained using the half-cycle Fourier algorithm (with complete DC component rejection） [9]:

$$
\begin{array} { l } { { f _ { 0 x } ( k ) = \displaystyle \sum _ { i = 0 } ^ { N / 2 - 1 } h _ { x } ( i ) f _ { 0 } ( k - i ) , } } \\ { { f _ { 0 y } ( k ) = \displaystyle \sum _ { i = 0 } ^ { N / 2 - 1 } h _ { y } ( i ) f _ { 0 } ( k - i ) } } \end{array}\tag{16}
$$

where

$$
\begin{array} { l } { { \displaystyle h _ { x } ( i ) = \frac { 4 N \sin ^ { 2 } ( \varphi / 2 ) } { N ^ { 2 } \sin ^ { 2 } ( \varphi / 2 ) - 8 } \biggl ( \sin ( \varphi i + \varphi / 2 ) - \frac { 2 } { N \sin ( \varphi / 2 ) } \biggr ) , } } \\ { { \displaystyle h _ { y } ( i ) = - \frac { 4 } { N } \cos ( \varphi i + \varphi / 2 ) } } \end{array}
$$

and

$$
\varphi = \frac { 2 \pi } { N }
$$

N is the number of samples in one cycle of the fundamental frequency (similarly for the remaining components $f _ { \alpha } ( k )$ and $f _ { \beta } ( k ) )$ .The x- and y-components calculated according to Eq.(16) form the complex signal as in Eq. (2).

(3) Finally,positive and negative sequence symmetrical components are determined by [10]:

$$
{ \begin{array} { r l } { { \underline { { \int } } } _ { 1 } ( k ) { \\\ { \underline { { f } } } _ { 2 } ( k ) } { \rule { 0 ex } { 5 ex } } = { \frac { 1 } { 2 } } { \left[ \begin{array} { l l l } { 1 } & { } & { { \mathrm { j } } } \\ { 1 } & { } & { - { \mathrm { j } } } \end{array} \right] } { \underline { { f } } } _ { \alpha } ( k ) { \overset { \quad } { \jmath } } } \end{array} }\tag{17}
$$

## References

[1] A.G.Phadke,M. Ibrahim and T.Hlibka,Fundamental basis for distance relaying with symmetrical components,IEEE Trans.Power Appar. Syst.,PAS-96 (2) (1977) 635-646.

[2] D.I.Waikar，S. Elangovan and A.C.Liew,Fault impedance estimation algorithm for digital distance relaying，IEEE Trans.Power Deliv.,9(3) (1994) 1375-1383.

[3] B.Jeyasurya and W.J. Smolinski, Identification of a best algorithm for digital distance protection of transmission lines, IEEE Trans.Power Appar.Syst.,PAS-102(10) (1983) 3358- 3376.

[4] A.M. Ranjbar and B.J.Cory,An improved method for the digital protection of high voltage transmission lines,IEEE Trans.Power Appar. Syst.,PAS-91 (2) (1975) 544-550.

[5] M.S. Sachdev and M.A.Baribeau,A new algorithm for digital impedance relays,IEEE Trans.Power Appar.Syst.,PAS-98 (1979) 2232-2240.

[6] M.I. Gilany,O.P.Malik and G.S. Hope,A laboratory investigation of a digital protection technique for parallel transmissionlines,IEEETrans.PowerDel.,10 (l）(1995) 187-193.

[7] H.Dommel，Electromagnetic Transients Program.Reference Manual,BPA,Portland,Oregon,1986.

[8] A.J.Degens,Microprocessor implemented digital filters for the calculation of symmetrical components,IEE Proc.C,129 (1982) 111-118.

[9]H.Ungrad，W.Winkler and A.Wiszniewski,Protection Techniques in Electrical Energy Systems,Marcel Dekker,New York,1995,p.400.

[10] E.Rosolowski and M. Michalik,Fast identification of symmetrical components by use of a state observer,IEE Proc.- Gener.Transm.Distrib.,141 (6) (1994) 617-622.