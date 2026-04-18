# A NOVEL DISTANCE PROTECTION ALGORITHM IN FREQUENCY DOMAIN BASED ON PARAMETER IDENTIFICATION

J.L. SUONAN \*, Y. ZHONG †, G.B. SONG ‡

\*School of Electrical Engineering, Xi'an Jiaotong University, China Email: suonan@263.net School of Electrical Engineering, Xi'anJaotongUniversityChina Email:zhongying@stuxjtuedu.cn School of Electrical Engineering, Xi'an Jiaotong University, China Email: song.gb@mail.xjtu.edu.cn

Keywords: distance protection， overreach action, parameter identification, matrix pencil algorithm, R-L model

## Abstract

In this paper,a novel distance protection algorithm in frequency domain is introduced. Based on the R-L model of transmission lines,this algorithm is derived from the linear equations which are obtained in fault condition network and O-module network for single-phase-to-earth fault. Considering that transformers usually ground directly in high voltage power systems,a linear equation with three coefficients is deduced based on the inductive O-sequence system impedance. Theoretical analysis and simulation results prove that the algorithm is accurate when faults happen at the remote terminal and it will get a positive fault distance error when faults happen around the remote terminal. This phenomenon shows that the algorithm effectively prevents overreach action of distance relays. Meanwhile, this algorithm has a high ability of anti-resistance and is expected to form a new distance protection.

## 1 Introduction

Modern power systems have been increasingly large and complex. Voltage classes and transmission capacities of transmission lines improve and grow continuously that requires distance relays to be more excellent. However, the resistance in fault loop circuits will influence distance relay's performance greatly, especially for single-phase-to-earth fault.

Conventional distance relays [1，2] can only solve two variables by using fundamental frequency data in post-fault waveforms. They commonly suppose that currents in fault point and that in measuring point have the same phase. However, this hypothesis will cause great fault distance error when faults happen at the remote terminal with high resistance to ground. Moreover, the computed distance error usually inclines to be negative, which leads distance relay to overreach.Both zero-sequence reactance relay [3,4] and negative-sequencereactancerelay[5]improvethe performance of distance relays in some degree.However, the hypothesis of these literatures that the current distribute factor is real does not always stand. This is the essential problem that leads the distance relay to overreach. Other methods, such as method of fault component distance relay [6], method of utilizing travelling wave [7] and method of computing the lowest voltage location along the transmission line [8],are also not able to resolve the overreach problem in essence.

Based on parameter identification,Literature [9] and [10] suggest an accurate fault location algorithm using one terminal data in time domain and in frequency domain, respectively. By taking fault distance， fault resistance, equivalent resistance and inductance of opposite system as unknown variables, a non-linear equation is deduced from the analysis of fault network and fault component network. By solving the non-linear equation, the fault distance is obtained. However, since the equation is non-linear,its solution needs iterative method and has the problem of multiple solutions. Besides, they have low computational efficiency. Therefore, both methods can not be applied to distance protection algorithm.

Referred to the analytical method of literature [9], for singlephase-to-earth fault,a novel distance protection algorithm based on parameter identification of solving linear equations is presented in this paper. The core idea of the algorithm is to assume O-sequence impedance after fault point was an inductance. Taking fault distance, fault resistance and equivalent inductance of opposite system as unknown variables,a linearequation with three coefficientsis introduced from the analysis of fault condition network and 0- module network.Base on the relationship between the three variables and the three coefficients, the fault distance is easily solved.Meanwhile,the solution of the linear equation is unique,avoiding multi-solution problem when solving nonlinear equation. To avoid additional error brought by numerical differentiation in time domain, the distance protection algorithm is introduced in frequency domain in this paper. Since accurate fundamental frequency phasors can not be extracted by DFT (Discrete Fourier Transformation) due to the inference of DC offset component in post-fault waveforms, a new frequency extraction method, namely matrix pencil algorithm [11]，is introduced in this paper.Not only the fundamental frequency component, but also the DC offset component during the transient period will be accurately extracted,which fits perfectly for the distance protection algorithm proposed in this paper.At last, both theoretical analysis and simulation results prove the distance protection algorithm is accurate when faults happen at the remote terminal and gets a positive fault distance error when faults happen around the remote terminal. The algorithm can effectively prevent overreach phenomenon and is prospected to form a new distance relay.

## 2 Fundamental principle of distance protection algorithm

## 2.1 Derivation of the distance protection algorithm

According to the superposition theorem，fault network is composed of load component network and fault component network. As to single-phase-to-earth faults (here we take phase-A-to-earth fault as an example) in transmission lines, take O-module network as fault component network. In this paper,we use Clark transformation matrix as phase-module transformation matrix.

Figure 1(a) and Figure 1(b) show equivalent circuit of fault network and O-module component network of double end power system in R-L model. Distance measuring equipment is supposed to be set in terminal m.

![](images/900c1a5b0b30df6b99f5139776125c351c0899cd218ef406ad75b7b59d944be8.jpg)  
(a） equivalent circuit of fault network for single-phase-to-earth fault

![](images/2e7308f0800a67f771b7e982d8ee3477d2e62cf0efd19d448c5030f0b0703e12.jpg)  
(b） equivalent circuit of 0-module component network

Figure l: equivalent circuit of fault condition in power system

In Figure 1(a), the voltage of phase A at terminal m can be written as

$$
U _ { m a } \left( s \right) = \left[ I _ { m a } \left( s \right) + K _ { z } \cdot 3 I _ { m 0 } \left( s \right) \right] z _ { 1 } p + I _ { F a } \left( s \right) R _ { F }\tag{1}
$$

$$
K _ { z } = \frac { z _ { 0 } - z _ { 1 } } { 3 z _ { 1 } } , \ z _ { 1 } = r _ { 1 } + s L _ { 1 } , \ z _ { 0 } = r _ { 0 } + s L _ { 0 }
$$

Where $K _ { z }$ is O-sequence compensation factor for impedance; $U _ { m a } ( s )$ and $I _ { m a } ( s )$ are complex amplitude of fault voltage and current of phase A at terminal $m ,$ respectively; $I _ { m 0 } ( s )$ is complex amplitude of O-module current at terminal m; $r _ { I } ,$ $L _ { I } , r _ { 0 } , L _ { 0 }$ are mode 1 and mode O resistance and inductance per unit length, respectively; $I _ { F a } ( s )$ and $I _ { F 0 } ( s )$ are complex amplitude of fault current and O-module current at fault point, respectively; p is the fault distance.

In Figure 1(b), $R _ { m 0 } , L _ { m 0 } , R _ { n 0 }$ and $L _ { n 0 }$ are source parameters of mode O. In this paper, suppose O-sequence impedance after fault point is an inductance, namely $R _ { n 0 } ^ { ' } = R _ { n 0 } + \left( l - p \right) r _ { 0 } = 0$

According to Figure 1(b) and the hypothesis above, the relationship between $I _ { F a } ( s )$ and $I _ { m 0 } ( s )$ can be expressed as

$$
\begin{array} { c } { { I _ { F a } \left( s \right) = 3 I _ { F 0 } \left( s \right) } } \\ { { = 3 \left( I _ { m 0 } \left( s \right) + I _ { n 0 } \left( s \right) \right) } } \\ { { = 3 I _ { m 0 } \left( s \right) K _ { 0 } \left( s \right) } } \\ { { { } } } \\ { { K _ { 0 } \left( s \right) = \displaystyle \frac { Z _ { m 0 } ^ { ' } + s L _ { n 0 } ^ { ' } } { s L _ { n 0 } ^ { ' } } = \displaystyle \frac { \left( Z _ { m 0 } + z _ { 0 } p \right) + s \left( L _ { n 0 } + \left( l - p \right) L _ { 0 } \right) } { s \left( L _ { n 0 } + \left( l - p \right) L _ { 0 } \right) } . } } \end{array}\tag{2}
$$

Where $K _ { \theta } ( s )$ is the reciprocal of complex amplitude of 0- sequence current distribute factor in terminal m; $Z _ { m 0 }$ is0- sequence source impedance in terminal $m ;$ l is the length of the transmission line.

By substituting $I _ { F a } ( s )$ in equation (2) into equation (1), we can get

$$
\begin{array} { l } { { U _ { m a } \left( s \right) = } } \\ { { \left[ I _ { m a } \left( s \right) + K _ { z } \cdot 3 I _ { m 0 } \left( s \right) \right] z _ { 1 } p + 3 I _ { m 0 } \left( s \right) K _ { 0 } \left( s \right) R _ { F } } } \end{array}\tag{3}
$$

Besides,

$$
\begin{array} { l } { { { \cal K } _ { 0 } \left( s \right) { \cal R } _ { F } = \displaystyle \frac { \dot { Z _ { m 0 } } + s \dot { L _ { n 0 } } } { s \dot { L _ { n 0 } } } { \cal R } _ { F } } } \\ { { { } ~ = \displaystyle \frac { \left( { \cal R } _ { m 0 } + s { \cal L } _ { m 0 } + r _ { 0 } p + s { \cal L } _ { 0 } p \right) + s \left( { \cal L } _ { n 0 } + \left( l - p \right) { \cal L } _ { 0 } \right) } { s \left( { \cal L } _ { n 0 } + \left( l - p \right) { \cal L } _ { 0 } \right) } { \cal R } _ { F } } } \\ { { { } ~ = \displaystyle \frac { \left( { \cal R } _ { m 0 } + r _ { 0 } p \right) { \cal R } _ { F } + s \left( { \cal L } _ { m 0 } + { \cal L } _ { n 0 } + { \cal L } _ { 0 } l \right) { \cal R } _ { F } } { s \left( \left( l - p \right) { \cal L } _ { 0 } + { \cal L } _ { n 0 } \right) } } } \end{array}\tag{4}
$$

For convenience, we define

$$
\begin{array} { r l } & { \left\{ R _ { \Sigma } = \big ( R _ { m 0 } + r _ { 0 } p \big ) R _ { F } \right. } \\ & { \left\{ L _ { \Sigma } = \big ( L _ { m 0 } + L _ { n 0 } + L _ { 0 } l \big ) R _ { F } \right. } \\ & { \left. \left[ L _ { \Sigma } = \big ( l - p \big ) L _ { 0 } + L _ { n 0 } \right. \right. } \end{array}\tag{5}
$$

By substituting equation (4) and (5） into equation (3), the following expression is obtained

$$
\begin{array} { r l r } & { } & { s \dot { L _ { \Sigma } } U _ { m a } \left( s \right) = s \bar { I } ^ { ' } \left( s \right) p \dot { L _ { \Sigma } } + \left( R _ { \Sigma } + s L _ { \Sigma } \right) \cdot 3 I _ { m 0 } \left( s \right) } \\ & { } & \\ & { } & { I ^ { ' } \left( s \right) = \left[ I _ { m a } \left( s \right) + K _ { R } \cdot 3 I _ { m 0 } \left( s \right) \right] r _ { 1 } } \\ & { } & { + \left[ I _ { m a } \left( s \right) + K _ { L } \cdot 3 I _ { m 0 } \left( s \right) \right] s L _ { 1 } . } \end{array}\tag{6}
$$

Where $K _ { R }$ is O-sequence compensation factor for resistance;   
$K _ { L }$ is O-sequence compensation factor for inductance.

Divided by $L _ { \Sigma } ^ { ' }$ to both side of the equal sign, equation (6) is transformed to

$$
s U _ { m a } \left( s \right) = s I ^ { ' } \left( s \right) p + \frac { 3 R _ { \Sigma } } { \dot { L _ { \Sigma } } } I _ { m 0 } \left( s \right) + \frac { 3 L _ { \Sigma } } { \dot { L _ { \Sigma } } } s I _ { m 0 } \left( s \right)
$$

Namely,

（7)

$$
s U _ { m a } \left( s \right) = s I ^ { ^ { \prime } } \left( s \right) x _ { 1 } + I _ { m 0 } \left( s \right) x _ { 2 } + s I _ { m 0 } \left( s \right) x _ { 3 }\tag{8}
$$

Parameters $x _ { I } \sim x _ { 3 }$ in equation (8) are three coefficients of the linear equation. The relationship between these three coefficients and the three unknown variables: fault distance $p ,$ fault transition resistance $R _ { F }$ and the real time equivalent inductance of opposite system parameter $L _ { n 0 }$ is as follows

$$
\{ \begin{array} { l l } { p = x 1 } \\ { L _ { n 0 } = ( x _ { 3 } / x _ { 2 } ) ( R _ { m 0 } + r _ { 0 } p ) - ( L _ { m 0 } + L _ { 0 } l ) } \\ { R _ { F } = \{ x _ { 2 } [ ( l - p ) L _ { 0 } + L _ { n 0 } ] \} / [ 3 ( R _ { m 0 } + r _ { 0 } p ) ] } \end{array} \tag{9}
$$

Source parameters in terminal m, $R _ { m 0 }$ and $L _ { m 0 } ,$ can be calculated in real time (please see the method in literature [9]), so they are known quantities in equation (9).

By solving equation (8),we can get the three coefficients. Then using the relationship as equation (9) shows,we can get the three unknown variables.

As we know, one real equation can work out one coefficient at most. Since three coefficients are needed to be solved in equation (8), at least three real equations are needed. Because fundamental component based equation (8) is a complex one, which can be decomposed to two real equations,while DC offset component based is a real one, thus the fundamental component and one DC offset component are needed in order to solve the three coefficients of equation (8).Meanwhile, the fundamental component and the DC offset component usually exist in the fault transient period [9].Therefore, the solution of equation (8) is unique and easy to work out.

## 2.2 Data processing procedure

The data processing procedure of the algorithm in this paper is simple, as shown below.

(1） Extract complex amplitude of A-phase-voltage,A-phasecurrent and O-module-current in terminal m. Take the sampling points of voltage and current, and then extract the fundamental component and DC offset components by utilizing matrix pencil algorithm (described in section 4).

(2） Solve the three coefficients of the linear equation. Take the parameters in step (1） to compose a series of equations according to equation (8) and then solve the linear equation set.

(3）Solve fault distance. Substitute the coeficients solved in step (2) into equation (9) and the fault distance will be obtained at last.

(4) Judge the distance relay to act or not. Compare the fault distance obtained in step (3) with the action zone of the relay. If it falls in the action zone, the relay acts; if not, the relay does not act.

## 3System error analysis of the distance protection algorithm

The hypothesis that O-sequence impedance after fault point is an inductance will inevitably brings system error to the

distance protection algorithm. Here the system error expression is deduced when the transmission line is in noload operating condition.

The accurate fault location equation is as follows

$$
\begin{array} { c } { { U _ { m a } \left( s \right) = \left( I _ { m a } \left( s \right) + K _ { z } \cdot 3 I _ { m 0 } \left( s \right) \right) z _ { 1 } p } } \\ { { + 3 I _ { m 0 } \left( s \right) R _ { F } \cdot K \left( s \right) } } \end{array}\tag{10}
$$

$$
K \left( s \right) = \frac { Z _ { \Sigma ^ { 0 } } \left( s \right) } { Z _ { n 0 } ^ { \prime } \left( s \right) } { = \frac { Z _ { m 0 } ^ { \prime } \left( s \right) + Z _ { n 0 } ^ { \prime } \left( s \right) } { Z _ { n 0 } ^ { \prime } \left( s \right) } }
$$

Where $K ( s )$ is the reciprocal of complex amplitude of actual O-sequence current distribute factor in terminal m; $Z _ { m 0 } ^ { ' } \left( s \right)$ and $Z _ { n 0 } ^ { ' } \left( s \right)$ are impedance in front of fault point and behind fault point, respectively; p is the actual fault distance.

Here the distance protection algorithm is rewritten as follows

$$
\begin{array} { c } { { U _ { m a } \left( s \right) { = } { { \left( { { I _ { m a } } \left( s \right) + K _ { z } \cdot 3 I _ { m 0 } \left( s \right) } \right) } { z _ { 1 } } } p _ { 1 } } } \\ { { + 3 I _ { m 0 } \left( s \right) { R _ { F } \cdot K _ { 1 } } \left( s \right) } } \end{array}\tag{11}
$$

Where $K _ { z }$ is O-sequence compensation factor for impedance; $p _ { I }$ is the computed value of fault distance of the protection algorithm; $K _ { I } ( s )$ is the same as $K _ { \theta } ( s )$ in equation (2).

Define a function F

$$
\begin{array} { c } { { F \left( p , R _ { n 0 } ^ { \prime } \right) = U _ { m a } \left( s \right) - \left( I _ { m a } \left( s \right) + K _ { z } \cdot 3 I _ { m 0 } \left( s \right) \right) z _ { 1 } p } } \\ { { - 3 I _ { m 0 } \left( s \right) R _ { F } \cdot K \left( s \right) } } \end{array}\tag{12}
$$

Where $p$ and $R _ { n 0 } ^ { ' }$ are two variables;p is the actual fault distance; $R _ { n 0 } ^ { ' }$ is O-sequence resistance after fault point; $K ( s )$ is the same as equation (10).

Expand function F at point $( p { = } p _ { I } , R _ { n 0 } ^ { ' } = 0 )$ and neglect the higher orders. Then, we have the equation

$$
\begin{array} { l } { { \displaystyle F \big ( p , R _ { n 0 } ^ { \prime } \big ) = } } \\ { { \displaystyle F \big ( p _ { 1 } , 0 \big ) + \frac { \hat { \sigma } F } { \hat { \sigma } p } \big ( p - p _ { 1 } \big ) + \frac { \hat { \sigma } F } { \hat { \sigma } R _ { n 0 } ^ { \prime } } \big ( R _ { n 0 } ^ { \prime } - 0 \big ) } } \end{array}\tag{13}
$$

Where,

$$
\begin{array} { c } { { F \bigl ( p _ { 1 } , 0 \bigr ) = U _ { m a } \bigl ( s \bigr ) - \bigl ( I _ { m a } \bigl ( s \bigr ) + K _ { z } \cdot 3 I _ { m 0 } \bigl ( s \bigr ) \bigr ) z _ { 1 } p _ { 1 } } } \\ { { - 3 I _ { m 0 } \bigl ( s \bigr ) R _ { F } \cdot K _ { 1 } \bigl ( s \bigr ) } } \end{array}\tag{14}
$$

According to equations (10) and (11), we get

$$
\left\{ { F \left( p , R _ { n 0 } ^ { \prime } \right) = 0 } \right.\tag{15}
$$

Substitute equation (15） into equation （14） and put the element $\left( p / p _ { I } \right)$ to the left side of the equal sign

$$
p _ { 1 } - p = \frac { \left( \hat { \sigma } F / \hat { \sigma } R _ { n 0 } ^ { \prime } \right) } { \left( \hat { \sigma } F / \hat { \sigma } p \right) } \cdot R _ { n 0 } ^ { \prime }\tag{16}
$$

By substituting equation (13) into equation (16), we can get the system error function of the distance protection algorithm

$$
p _ { 1 } - p = { \frac { - K _ { _ { R _ { F } } } \cdot Z _ { m 0 } ^ { \prime } } { 1 + K _ { _ { R _ { F } } } \cdot \left( z _ { 0 } Z _ { n 0 } ^ { \prime } + s L _ { 0 } \cdot Z _ { m 0 } ^ { \prime } \right) } } \cdot R _ { n 0 } ^ { \prime }\tag{17}
$$

$$
K _ { _ { R _ { F } } } = \frac { 3 I _ { _ { m 0 } } \left( s \right) \cdot R _ { _ F } } { \left( I _ { _ { m a } } \left( s \right) + K _ { _ Z } 3 I _ { _ { m 0 } } \left( s \right) \right) z _ { 1 } \left( Z _ { n 0 } ^ { \prime } \right) ^ { 2 } }
$$

Where $K _ { R _ { F } }$ isa coefficient associated with the transition resistance.

Meanwhile, transformed by Clark transformation matrix, $I _ { F I } ( s ) , I _ { F 2 } ( s )$ and $I _ { F 0 } ( s )$ meet the following equation

$$
I _ { F 1 } ( s ) = 2 I _ { F 0 } ( s ) , I _ { F 2 } ( s ) = 0\tag{18}
$$

Where $I _ { F I } ( s ) , I _ { F 2 } ( s )$ and $I _ { F 0 } ( s )$ are 1-module current, 2-module current and O-module current at fault point, respectively.

In terms of the phase-module transformation matrix, when the transmission line is in no-load operation, we get

$$
\begin{array} { r l } & { I _ { m a } \left( s \right) = I _ { m 1 } \left( s \right) + I _ { m 2 } \left( s \right) + I _ { m 0 } \left( s \right) } \\ & { \quad = C _ { 1 } \left( s \right) I _ { F 1 } \left( s \right) + C _ { 2 } \left( s \right) I _ { F 2 } \left( s \right) + C _ { 0 } \left( s \right) I _ { F 0 } \left( s \right) } \\ & { \quad = \left( 2 C _ { 1 } \left( s \right) + C _ { 0 } \left( s \right) \right) I _ { F 0 } \left( s \right) } \end{array}\tag{19}
$$

$$
C _ { 1 } \left( s \right) = \frac { Z _ { n 1 } \left( s \right) + z _ { 1 } \left( l - p \right) } { Z _ { m 1 } \left( s \right) + Z _ { n 1 } \left( s \right) + z _ { 1 } l } \mathrm { ~ , ~ } C _ { 0 } \left( s \right) = \frac { Z _ { n 0 } \left( s \right) + z _ { 0 } \left( l - p \right) } { Z _ { m 0 } \left( s \right) + Z _ { n 0 } \left( s \right) + z _ { 0 } l }
$$

Where $C _ { I } ( s )$ and $C _ { \theta } ( s )$ are complex amplitude of 1-module and O-module current distribute factor in terminal m, respectively.

Therefore,

$$
\begin{array} { c } { { \displaystyle \frac { I _ { m 0 } \left( s \right) } { I _ { m a } \left( s \right) + K _ { Z } 3 I _ { m 0 } \left( s \right) } = \frac 1 { \displaystyle \frac { I _ { m a } \left( s \right) } { I _ { m 0 } \left( s \right) } + 3 K _ { Z } } } } \\ { { = \displaystyle \frac 1 { \displaystyle \frac { 2 C _ { 1 } \left( s \right) + C _ { 0 } \left( s \right) } { C _ { 0 } \left( s \right) } + 3 K _ { Z } } } } \end{array}\tag{20}
$$

Substitute equation (20) into $K _ { R F } ,$ we get

$$
K _ { _ { R F } } = \frac { 3 R _ { _ F } } { \left( \displaystyle \frac { 2 C _ { 1 } \left( s \right) + C _ { _ 0 } \left( s \right) } { C _ { _ 0 } \left( s \right) } + 3 K _ { _ Z } \right) z _ { 1 } \left( Z _ { _ { n 0 } } ^ { \prime } \right) ^ { 2 } }\tag{21}
$$

In terms of equation (17) and (21),we can easily get the system error of the distance protection algorithm.

## 4 The principle of matrix pencil algorithm

The fundamental component and a DC ofset component are needed in order to solve equation (8). However,both of them can not be attained accurately by DFT because of the inference in transient period. Here,a component extracting method in frequency domain, namely matrix pencil algorithm, isintroduced. It can accurately extract fundamental component and DC offset componentsin post-fault waveforms.

Response signals in linear systems can be expressed as the sum of a series of exponential functions. Suppose the signal is composed of M subsignals,we have

$$
y _ { k } = \sum _ { m = 1 } ^ { M } R _ { m } e ^ { s _ { m } k T _ { s } } ; k = 0 , 1 , \cdots , N - 1\tag{22}
$$

$$
R _ { { m } } = A _ { { m } } e ^ { j \theta _ { { m } } } , s _ { { m } } = - \alpha _ { { m } } + j \omega _ { { m } }
$$

where $y _ { k }$ is the k-th sampling point; $T _ { s }$ is the sampling interval; N is the total number of sampling points; $R _ { m }$ is the complex amplitude of m-th subsignal; $A _ { m }$ is the amplitude of m-th subsignal; $\theta _ { m }$ is the phase theta of m-th subsignal; $s _ { m }$ is the m-th complex frequency; $\alpha _ { m }$ is the attenuation factor of m-th subsignal; $\omega _ { m }$ is the angular frequency of m-th subsignal.

Define $z _ { m } = e ^ { s _ { m } T _ { s } }$ , then equation (22) is transformed to

$$
y _ { k } = \sum _ { m = 1 } ^ { M } R _ { m } z _ { m } ^ { k } ; k = 0 , 1 , \cdots , N - 1\tag{23}
$$

Here, two Hankel matrix, $Y _ { I }$ and $Y _ { 2 } ,$ are defined as follows

$$
Y _ { 1 } = \left[ \begin{array} { l l l l } { y _ { 0 } } & { y _ { 1 } } & { \cdots } & { y _ { L - 1 } } \\ { y _ { 1 } } & { y _ { 2 } } & { \cdots } & { y _ { L } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { y _ { N - L } } & { y _ { N - L + 1 } } & { \cdots } & { y _ { N - 1 } } \end{array} \right] _ { \left( N - L + 1 \right) \times L } ,
$$

$$
Y _ { 2 } = { \left[ \begin{array} { l l l l } { y _ { 1 } } & { y _ { 2 } } & { \cdots } & { y _ { L } } \\ { y _ { 2 } } & { y _ { 3 } } & { \cdots } & { y _ { L + 1 } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { y _ { N - L + 1 } } & { y _ { N - L + 2 } } & { \cdots } & { y _ { N } } \end{array} \right] } _ { ( N - L + 1 ) \times L } .
$$

Where L is a pencil parameter and is useful in eliminating effects of noise in the data,which is set between N/3 and N/2 typically.

Throughsingularvaluedecomposition (SVD), $Y _ { I }$ is decomposed into

$$
Y _ { 1 } = U \sum V ^ { T }\tag{24}
$$

where U is a $( N { - } L { + } 1 ) \times ( N { - } L { + } 1 )$ orthogonal matrix,whose column vectors are eigenvectors of matrix $Y _ { I } Y _ { I } ^ { ~ T } ;$ V is a $L \times L$ orthogonal matrix,whose column vectors are eigenvectors of matrix $Y _ { I } ^ { T } Y _ { I } ; \Sigma$ isa $( N { - } L { + } 1 ) \times L$ diagonal matrix, whose diagonal elements are the singular values and ranged in descending order.

To a signal out of noises,matrix $Y _ { I }$ will have M non-zero singular values. Once influenced by noises, some non-zero singular values may turn into small singular values. In this condition,we regard the maximum singular value in matrix £as $\sigma _ { m a x }$ and set a precision p .If singular values $\sigma _ { i } \mathord { \left/ { \vphantom { \sigma _ { i } \sigma } } \right. \kern - delimiterspace } \sigma$ max $> p$ stands,the i-th subsignal is seen as an effective one. Otherwise,the i-th subsignal is treated as a noise. The maximum subscript of singular values is taken as M. In this way, the order of signal is determined [12].

According to literature [13], $z _ { m }$ is the generalized eigenvalue of matrix pair $[ Y _ { I } , Y _ { 2 } ]$ ,namely

$$
\Big ( Y _ { 1 } ^ { + } Y _ { 2 } - z _ { m } I \Big ) r _ { m } = \big [ \mathbf { 0 } \big ]\tag{25}
$$

Where ${ Y _ { I } } ^ { + }$ is the Moore-Penrose pseudo-inverse matrix of $Y _ { I } ;$ $r _ { m }$ is the generalized eigenvector corresponded to $z _ { m } ;$

Thus, $z _ { m }$ can be worked out according to equation (25). In addition, $\alpha _ { m }$ and $\omega _ { m }$ can be solved as follows

$$
- \alpha _ { m } + j \omega _ { m } = \big ( \ln z _ { m } \big ) \big / T _ { s } ; m = 1 , 2 , \cdots , M\tag{26}
$$

In terms of equation (23), $R _ { m }$ can be solved in least square method as the following equation

$$
{ \left[ \begin{array} { l } { y _ { 0 } } \\ { y _ { 1 } } \\ { \vdots } \\ { y _ { N - 1 } } \end{array} \right] } = { \left[ \begin{array} { l l l l } { 1 } & { 1 } & { \cdots } & { 1 } \\ { z _ { 1 } } & { z _ { 2 } } & { \cdots } & { z _ { M } } \\ { \vdots } & { \vdots } & & { \vdots } \\ { z _ { 1 } ^ { N - 1 } } & { z _ { 2 } ^ { N - 1 } } & { \cdots } & { z _ { M } ^ { N - 1 } } \end{array} \right] } { \left[ \begin{array} { l } { R _ { 1 } } \\ { R _ { 2 } } \\ { \vdots } \\ { R _ { M } } \end{array} \right] }\tag{27}
$$

Moreover,the amplitude $A _ { m } ,$ the phase theta $\theta _ { m } ,$ the attenuation factor $\alpha _ { m }$ and the angular frequency $\omega _ { m }$ can be solved using equation (28).

$$
\begin{array} { r l } & { \{ A _ { m } = | R _ { m } | ; } \\ & { \theta _ { m } = \arctan ( \operatorname { I m } ( R _ { m } ) \middle / \operatorname { R e } ( R _ { m } ) ) ; } \\ & { \alpha _ { m } = - \operatorname { R e } ( \ln z _ { m } ) / T _ { s } ; } \\ & { \omega _ { m } = \operatorname { I m } ( \ln z _ { m } ) / T _ { s } \circ } \end{array}\tag{28}
$$

## 5 Simulation results

Tests have been conducted using the Electromagnetic Transient Program (EMTP).Here,110kV power system is considered. Because of the limitation of the model adopted by the algorithm in this paper, the distributed capacitance of the transmission line is ignored.The system fault model for EMTP simulation is shown in Figure 1(a). The detailed simulation parameters are listed as below

The length of transmission line l = 50 km;

The source parameters at terminal m:

$$
L _ { m 0 } { = } 1 1 . 6 \mathrm { m H } , L _ { m l } { = } 3 0 . 8 \mathrm { m H } ;
$$

The source parameters at terminal n:

$$
L _ { n 0 } { = } 2 3 . 1 \mathrm { m H } , L _ { n l } { = } 6 1 . 6 \mathrm { m H } ;
$$

The transmission line parameters:

$$
r _ { I } \mathrm { = } 0 . 1 0 5 \Omega / \mathrm { k m } , L _ { I } \mathrm { = } 1 . 2 5 8 \mathrm { m H / k m }
$$

The voltages of source generators:

$$
\dot { E } _ { m } = 1 . 0 5 \angle 0 ^ { \circ } , \dot { E } _ { n } = 1 . 0 0 \angle - 3 0 ^ { \circ } .
$$

The sampling rate is 10 kHz.

The time window for sampling data is 10 ms long.

<table><tr><td rowspan="2">fault distance /(km)</td><td rowspan="2">transient resistance /(Ω)</td><td colspan="3">computed fault distance/(km)</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td rowspan="4">10</td><td>10</td><td>11.32</td><td>10.11</td><td>9.97</td></tr><tr><td>20</td><td>11.13</td><td>10.19</td><td>9.97</td></tr><tr><td>50</td><td>10.79</td><td>10.37</td><td>9.97</td></tr><tr><td>100</td><td>10.83</td><td>10.57</td><td>9.97</td></tr></table>

<table><tr><td rowspan=4 colspan=1>20</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>22.10</td><td rowspan=1 colspan=1>19.92</td><td rowspan=1 colspan=1>20.03</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>21.85</td><td rowspan=1 colspan=1>19.86</td><td rowspan=1 colspan=1>20.03</td></tr><tr><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>20.65</td><td rowspan=1 colspan=1>19.73</td><td rowspan=1 colspan=1>20.02</td></tr><tr><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>20.07</td><td rowspan=1 colspan=1>19.60</td><td rowspan=1 colspan=1>20.02</td></tr><tr><td rowspan=4 colspan=1>30</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>32.42</td><td rowspan=1 colspan=1>29.41</td><td rowspan=1 colspan=1>30.18</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>31.90</td><td rowspan=1 colspan=1>29.01</td><td rowspan=1 colspan=1>30.18</td></tr><tr><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>29.56</td><td rowspan=1 colspan=1>28.20</td><td rowspan=1 colspan=1>30.17</td></tr><tr><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>28.12</td><td rowspan=1 colspan=1>27.42</td><td rowspan=1 colspan=1>30.17</td></tr><tr><td rowspan=3 colspan=1>40</td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>41.57</td><td rowspan=1 colspan=1>37.69</td><td rowspan=1 colspan=1>40.50</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>39.87</td><td rowspan=1 colspan=1>36.29</td><td rowspan=1 colspan=1>40.50</td></tr><tr><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>35.32</td><td rowspan=1 colspan=1>33.65</td><td rowspan=1 colspan=1>40.49</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>32.37</td><td rowspan=1 colspan=1>31.39</td><td rowspan=1 colspan=1>40.49</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>42.21</td><td rowspan=1 colspan=1>36.34</td><td rowspan=1 colspan=1>50.01</td></tr><tr><td rowspan=2 colspan=1>50</td><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>33.53</td><td rowspan=1 colspan=1>29.53</td><td rowspan=1 colspan=1>50.00</td></tr><tr><td rowspan=1 colspan=1>50</td><td rowspan=1 colspan=1>20.31</td><td rowspan=1 colspan=1>18.07</td><td rowspan=1 colspan=1>50.00</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>100</td><td rowspan=1 colspan=1>11.76</td><td rowspan=1 colspan=1>9.56</td><td rowspan=1 colspan=1>50.00</td></tr></table>

Table1:simulation results of different distance protection algorithms

Here,three different distance protection algorithmsare compared in Table 1,and they are measurement impedance algorithm [1](1),differential equation algorithm [2] (2） and frequency-domain based distance protection algorithm(3) described in this paper.

According to the simulation results in Table 1, the computed fault distance of both measurement impedance algorithm and differential equation algorithm are smaller than the real fault distance when faults happen at the remote terminal. Thus, these distance relays will easily overreach.However, the algorithm depicted in this paper is accurate when faults happen at the remote terminal. Moreover, the computed value of fault distance of the proposed algorithm is greater than the actual fault distance when faults happen around the remote terminal,which means it can effectively avoid overreach phenomenon.In the meantime, the algorithm has a high ability of anti-resistance all over the transmission line.

As to 11Okv transmission lines and above, the neutral point of transformers in power systems usually grounds directly. Thus, when faults happen at the remote terminal, O-sequence impedance of power system turns into leakage impedance of transformers.As resistance component in the transformer leakage impedance is very small and often negligible, the leakage impedance can usually be seen as a pure inductance component. Therefore, $R _ { n 0 } ^ { \prime } = 0$ ，the hypothesis stands. The system error isO according to equation (l7)，asis demonstrated in Table 1.

However， in some cases,owing to the different winding forms and connection modes of transformers,resistance component in $Z _ { n 0 } ^ { \prime }$ can not be neglected, namely $R _ { n 0 } ^ { \prime } > 0$ . The hypothesis does not stand. In order to test the algorithm in this condition,the error of computed fault distance E is defined as:

$$
E = \frac { c o m p u t e d l o c - a c t u a l l l o c } { l i n e l e n g t h } { \times 1 0 0 \% }
$$

Taking $R _ { n 0 } { = } 0 . 8 9 ~ \Omega ($ the zero-impedance angular is 83 degree) into the simulation parameters in 110kv power system, Figure 2 shows the curve of E when faults happen along the transmission line according to equation (17). The transition resistance is 50 Ω．And note that $p , R _ { F }$ and $Z _ { n 0 }$ are known variables at the moment.

![](images/a29cf769cc598724692da90572fe850cd588be5d9a51545f0a5902c1022f2c41.jpg)  
Figure 2: the curve of E when faults happen along the transmission line

Figure 2 illustrates that E>O when faults happen in a wide range around the remote terminal. This means the computed fault distance of the algorithm is greater than the actual fault distance. This phenomenon ensures the distance relay will not overreach.

## 6 Conclusions

In this paper,a novel distance protection algorithm in frequency domain has been developed. The algorithm has the following characteristics:

(1） It is a method of solving linear equations in frequency domain. Because of the abundent frequency components during the fault transient period, the solution of the linear equations is unique and is easily to be solved.

(2) The algorithm is accurate when faults happen at the remote terminal. Moreover, the algorithm has a positive error phenomenon when faults happen around the remote terminal, which will effectively avoid overreach action.

(3） This algorithm has a high ability of anti-resistance and is free from the influence in transient period.

Finally, it should be pointed out that the proposed algorithm is based on R-L model of transmission lines,and a further research should be carried out to cater for long EHV transmissionlines.Inaddition，Highperformance transformers, optical transformer for example, is needed since the algorithm relies on abundant transient components from power system.

## Acknowledgements

This work is supported by the National Science Foundation of China (Grant No．51037005)，National Basic Research Program of China (Grant No.2009CB219704)

## References

[1]T. Takagi, Y. Yamakosi, M. Yamaura, R. Kondow, T. Matsushima.“Development of a new type fault locator using the one terminal voltage and current data", IEEE Trans. PAS, vol. PAS-101, no.8, pp. 2892-2898,(1982).

[2]Q.S. Yang,I.F. Morison.“Microprocessorbased algorithm forhigh resistanceearth-fault distance protection", IEE Proc. Generat. Transm.Distrib, vol.130, no.11,pp.306-310, (1983).

[3] C.J. Fan,H.P. Yu, W.Y. Yu.“Ability Analysis of Zero-sequenceReactanceRelayAgainstTransient Resistance"，Electric Power Automation Equipment, vol.21, no.10, pp. 1-10, (2001).

[4] B. Wang， X.Z. Dong，Q.Z. Bo. “Zero-sequence Reactance Relay Application in Ultra- high-voltage AC Transmission Lines"，Automation of Electric Power Systems, vol.32, no.4, pp. 46-50,(2008).

[5]B. Wang， X.Z. Dong，Q.Z. Bo.“Analysisand Improvement of Zero-sequence Reactance Relay With ApplicationinUltra-high-voltageLongAC TransmissionLines”，TransactionsofChina Electrotechnical Society， vol.23，no.12，pp. 60-64, (2008).

[6] J.L. Suonan,F.M. He, Z.B. Jiao.“Research on the Characteristics ofDistance Element Based on the Powerfrequency Voltage and Current Variation”, Proceedings of the CSEE,vol.30, no.28, pp. 59-65,(2010).

[7] Y.Z. Ge, X.Z. Dong,X.L. Dong. “Traveling Wave-Based Distance Protection With Fault Location Part one Theory and Technology”,Automation of Electric Power Systems,vol.26, no.6, pp.34-40,(2002)

[8]S.M. Xue, J.L. He, Y.L. Li. “Distance protection based on Bergeron Model for UHV transmission lines”, Relay, vol.33, no.19, pp. 1-4, (2005).

[9]J.L. Suonan, J. Qi, F.F. Chen.“An accurate fault location algorithm for transmission lines based on R-L model parameteridentification”，ElectricPowerSystems Research,vol.76, no.1-3, pp.17-24,(2005).

[10] X.N. Kang, J.L. Suonan.“Frequency Domain Method of Fault Location Based on Parameter Identification Using One Terminal Data”,Proceeding of the CSEE, vol.25, no.2, pp. 22-27, (2005).

[11] J.L. Suonan,L. Wang, J.D. Xia, S.E. He.“Harmonic analysis of fault signal in UHV AC transmission line", High voltage engineering, vol.36,no.1, pp.37-43,(2010).

[12] Y. Hua,T.K. Sarkar.“Matrix pencil method for estimating parameters of exponentially damped/undamped sinusoids in noise", IEEE Trans on Signal Processing, vol.38, no.5, pp.814-824,(1991).

[13] Y.Hua,T.K. Sarkar.“On SVD for estimating generalized eigenvalues of singular matrix pencil in noise”,IEEE Trans on Signal Processing,vol.39,no.4, pp.892-900, (1991).