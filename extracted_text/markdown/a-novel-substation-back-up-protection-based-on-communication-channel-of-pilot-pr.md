# A Novel Substation Back-up Protection Based on Communication Channel of Pilot Protection

Xiangping Kong, Zhe Zhang, Fei Wang, and Xianggen Yin, Member, IEEE

Abstract--In order to solve the problems of traditional distance protection when it is used as back-up protection,a novel substation back-up protection scheme based on communication channel of pilot protection is proposed. According to comprehensive decision-making result of action states of protections in local substation and fault detection information transmitted by adjacent substations, the functions of proposed substation back-up protection are realized.Finally,a simulation model of IEEE 1O-generator-39-node system is built in PSCAD/EMTDC to test the performance of proposed substation back-up protection.Simulation results show the proposed substation back-up protection has excellent performance even in condition of fail-to trip of primary protection,DC power supply failure and heavy flow transfer. The proposed substation back-up protection can quicken the tripping of back-up protection and improve sensitivity.

Index Terms—communication channel of pilot protection, fault detection information,substation back-up protection, traditional back-up protection.

## I．INTRODUCTION

DTA tion for EHV and UHV transmission lines. Especially the zone 3 distance protection can be used as local back-up protection for local line and remote back-up protection for adjacent lines.But the time delay of zone 3 distance protection will be too large as it should be set to coordinate with zone 2 or zone 3 distance protection of the adjacent lines. Meanwhile, sensitivity of traditional distance protection is influenced by branch currents,and it will be insufficient in some conditions. Moreover,the cascading tripping of distance protection may be caused in condition of heavy flow transfer [1], [2]. In recent years,wide area back-up protection [3]-[6] is proposed to solve the problems of back-up protection. However, it needs to collect information of multi point synchronously. Wide area communication system is needed to realize communication in the whole power grid. The reliability and synchronization can not meet the requirements. Hence, the wide area back-up protection is difficult for practical application and the study of wide area back-up protection is still at exploration stage.

With the wide application and popularization of smart substation, the unified data modeling and data communication system in substation are realized based on IEC 61850 [7]. In this condition, the information sharing of equipments in bay level provides possibility to improve the traditional back-up protection.While,back-up protection scheme which is based on IEC 6185O can only collect information in local substation which has little improvement on conventional back-up protection. In order to improve performance of back-up protection greatly, it needs to get the information of adjacent substations.

As primary protection for EHV and UHV transmission lines, pilot protection uses private or multiplex fiber channel with bit rate of 2 Mbit/s as communication channel [8].At present, the fiber channel is only used to transmit sample values or phasors and a few action states of protections which will be used for primary protection.Therefore,the transfer capability of fiber channel is not fully utilized.Actually,fiber channel can be used to transmit multi information.Hence,under the precondition that the requirement of information transmission of pilot protection is satisfied, there still is redundant capability which can be used to transmit other information.

Based on it, a novel substation back-up protection scheme which can improve the performance of traditional distance protection is proposed. This novel substation back-up protection uses the existing fiber channel of pilot protection to transmit auxiliary information for the decision-making of back-up protection. Compared to wide area back-up protection, new communication channel is not needed for substation backup protection. Meanwhile, it is much easier to ensure the synchronization of substation information and the reliability is higher. Hence, the proposed substation back-up protection is applicable for engineering application. Section II introduces the basic principle of proposed substation back-up protection, including principle of fault detection and decision-making principle of tripping strategy. Detailed algorithm of fault de-tection and decision-making algorithm of substation back-up protection are presented in Section III.At last, simulations in PSCAD/ EMTDC are carried out to test the performance of proposed substation back-up protection.

## II.BASIC PRINCIPLE

In order to realize the functions of substation back-up protection，substation back-up protection decision-making unit should be installed in each substation.The function of substation protection decision-making unit comprises two parts: fault detection of transmission lines and decision-making of tripping strategy for back-up protection. With the detection results being transmitted to adjacent substations by communication channel of pilot protection, the former provides action states of protections to the latter. Then the latter identifies fault element and sets time delay for back-up protection according to comprehensive decision-making result which is based on the information provided by the former and action states of local protections. The decision-making of tripping strategy for backup protection is divided into decision-making of tripping strategy for local back-up protection and decision-making of tripping strategy for remote back-up protection.

Considering that primary protection may fail to trip, zone 1 distance protection can not protect the whole line, and protection scope of zone 2 distance protection reaches to the adjacent lines,the detection results based on action states of local protections can only indicate the direction of fault element and provide auxiliary information for the substation back-up protection decision-making unit.In order to ensure the reliability, substation protection decision-making unit should implement fault detection of transmission lines once more after the information transmitted by remote end substation is received. Hence,fault detection of transmission lines should be implemented twice.

## A. Fault detection of transmission lines

## (1) First fault detection

The aim of first fault detection is to detect the action states of local protections and obtain operation conditions of all transmission lines in local substation.

If any one of the following conditions happens, the corresponding transmission line is identified as suspicious faulty line.

a.Two sets of pilot protection both act.

b.Two sets of zone 1 distance protection both act.

c．One set of pilot protection acts,another one does not act. But one set or two sets of zone 1 distance protection act.

d. One set of pilot protection acts,another one does not act. But one set or two sets of zone 2 distance protection act.

e.Both two sets of pilot protection for transmission line do not act, but two sets of zone 2 distance protection act.

Note: Duplicated configuration is adopted for protections of EHV and UHV transmission lines. Hence, there are two sets of primary protection and two sets of back-up protection.

It needs to notice that when condition e happens, the corresponding line can not definitively be identified as suspicious faulty line. However, in order to provide auxiliary information for substation back-up protection decision-making unit, the line is still identified as suspicious faulty line.As the decisionmaking unit in adjacent substation needs action states of the local protections to determine whether trip or not, it will not result in mal-operation of back-up protection.

If at least one transmission line is identified as suspicious faulty line, the detection results of all transmission lines will be transmitted to the corresponding remote end substations by communication channels of pilot protections. For the transmis-sion line which is preliminary identified as suspicious faulty line, the transmitted information is "the line in local substation is suspicious faulty line".For other transmission lines,the transmitted information is "other line in local substation is suspicious faulty line".

Therefore,the logic diagram of the first fault detection is shown in Fig.1.

![](images/a7bbda41e38275669367a247e4a5eda7d21a2bcbf2b74b29bf1ff21f4270bf9c.jpg)  
Fig.1.Logic diagram of the first fault detection

## (2) Second fault detection

After the first fault detection and the information transmitted by remote end substations have been received completely, second fault detection is needed to identify the actual fault element.

If any one of the following conditions happens, the corresponding transmission line is identified as faulty line,and information of "fault happens in the protection scope of remote back-up protection" is transmitted to upstream substations.

a. The information of "the line in local substation is sus-picious faulty line" transmitted by remote end substation is received.

b. Two sets of pilot protection both act, and the information of "other line in local substation is suspicious faulty line” transmitted by remote end substation is not received.

Otherwise, the second fault detection should not be activated.

Actually, condition b is the redundant criterion for condition a. It can improve the reliability of second fault detection in case of communication system failure.

Therefore, the logic diagram of the second fault detection is shown in Fig.2.

![](images/d37c870a427c8c3f3d4d08cd204d7ed34f3ec570049df6e0ab0a08a6b9a623e9.jpg)  
Fig.2.Logic diagram of the second fault detection

## B. Decision-making of tripping strategy for back-up protection

The purpose of decision making of tripping strategy is to identify actual fault element and realize the local back-up protection function or remote back-up protection function according to the comprehensive decision-making result which is based on action states of local protections and fault detection results of transmission lines in adjacent substations.

The time delay of proposed substation back-up protection is set to coordinate with primary protection.If the fault is cleared by primary protection, the substation back-up protection will reset automatically.

(1) Decision making of tripping strategy for local back-up protection

If any one of the following conditions happens, it is identified that fault happens on the corresponding transmission line. In this condition, substation back-up protection should trip as local back-up protection with time delay of 0.5s.

a.Two sets of pilot protection both act.

b.Two sets of zone 1 distance protection both act.

c．One set of pilot protection acts,another one does not act. But one set or two sets of zone 1 distance protection act.

d. One set of pilot protection acts,another one does not act. But one set or two sets of zone 2 distance protection act. Meanwhile, the information transmitted by remote end substation is "the line in local substation is in fault condition".

e.Both two sets of pilot protection for transmission line do not act, but two sets of zone 2 distance protection act. Meanwhile, the information transmitted by remote end substation is "the line in local substation is in fault condition".

(2) Decision making of tripping strategy for remote back-up protection

If both of the following two conditions happen, it is identified that fault happens on the corresponding downstream transmission line.The substation back-up protection should trip as remote back-up protection with time delay of 1.0s.

a. Two sets of pilot protection and two sets of zone 1 distance protection do no act, but starting elements of two sets of protection devices both act.

b. Meanwhile,information of "fault happens in the protection scope of remote back-up protection" is received,and information of "the line in local substation is in fault condition" is not received.

## III. ALGORITHM OF SUBSTATION BACK-UP PROTECTION

## A. Algorithm offault detection

(1) Algorithm of first fault detection

In practical application, substation back-up protection deci-sion-making unit collects action states of local protections by substation communication network, like GOOSE network, to build up vector $R _ { i j } ^ { 6 }$ as expressed in (1).

$$
R _ { i j } ^ { 6 } = \left[ D _ { 1 } \quad D _ { 2 } \quad D _ { 3 } \quad D _ { 4 } \quad D _ { 5 } \quad D _ { 6 } \right] ^ { T }\tag{1}
$$

where $D _ { 1 } , D _ { 2 } , D _ { 3 } , D _ { 4 } , D _ { 5 }$ and $D _ { 6 }$ are the action states of pilot protection, zone 1 distance protection and zone 2 distance protection of device I and II respectively. If the corresponding protection acts, $D _ { k } = 1 ~ ( \ k = 1 , 2 . . . 6 ~ ) ;$ else $D _ { k } = 0$ $( k = 1 , 2 . . . 6 )$ .i is numbering of transmission line,j is numbering of substation.

Let detection matrix C to be (2).

$$
C = \left[ \begin{array} { l l l l l l l } { 1 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 1 } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 1 } & { 0 } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 0 } & { 0 } & { 1 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 0 } & { 1 } & { 1 } \end{array} \right]\tag{2}
$$

Result vector $X _ { i j }$ can be obtained as $X _ { i j } = C R _ { i j } ^ { 6 }$ .If $\left\| X _ { i j } \right\| _ { \infty } = 2$ ，the line i in substation j is identified as suspicious faulty line by first fault detection. $\operatorname { I f } \left\| X _ { i j } \right\| _ { \infty } < 2$ , no more calculation for corresponding line is activated.

$A = ( a _ { i j } ) _ { m \times n }$ represents incidence matrix of a system which has m transmission lines and n substations.If line i do not connect with substation $j , a _ { i j } = 0$ ; else, $a _ { i j } = 1$

$P _ { i } = d i a g \left( p _ { 1 } , p _ { 2 } \cdots p _ { m } \right) _ { m \times m }$ is the diagonal matrix of row information, $Q _ { j } = d i a g \left( q _ { 1 } , q _ { 2 } \cdots q _ { n } \right) _ { n \times n }$ is the diagonal matrix of column information. $\operatorname { I f } \left\| X _ { i j } \right\| _ { \infty } = 2$ ，then $p _ { i } = 2 , q _ { i } = - 2$ .The other elements in P and Q are 1.Then the obtained information matrix $Y _ { i j } = P _ { i } A Q _ { j }$ consists of elements -4,-2, 0, 1 and 2.

If there is element 2 in $Y _ { i j }$ , the detection results should be transmitted to remote end substations.If element 2 locates in kth row $( k = 1 , 2 . . . m )$ ,information of "the line in local substation is suspicious faulty line" should be transmitted to the remote end substation for line k $( k = 1 , 2 . . . m )$ .If element -2 locates in kth row,information of "other line in local substation is suspicious faulty line" should be transmitted to the remote end substation for line k .

(2) Algorithm of second fault detection

Decision-making unit obtains the action states of local protections by substation communication network and fault detection information of adjacent substations by communication channel of pilot protection. The received information vector is shown in (3)

$$
\begin{array} { r l } { R _ { i j } ^ { 3 } = \big [ S _ { 1 } } & { { } S _ { 2 } \quad G \big ] ^ { T } } \end{array}\tag{3}
$$

where $S _ { 1 }$ and $S _ { 2 }$ are receiving states of information of "the line in local substation is suspicious faulty line" and information of "other line in local substation is suspicious faulty line" respectively. If the information is received, $S _ { k } = 1$ $( k = 1 , 2 )$ ; else, $S _ { k } = 0 \ ( k = 1 , 2 )$ .According to the first fault detection, $S _ { \mathrm { 1 } }$ and $S _ { 2 }$ can not be l at the same time. G represents action state of local pilot protection. If anyone set of local pilot protection acts, $G = 1 \ \mathrm { i }$ else, $G = 0$

As it is difficult to detect $R _ { i j } ^ { 3 }$ , define revised matrix $\tilde { R } _ { i j } ^ { 3 }$ as shown in (4).

$$
\tilde { R } _ { i j } ^ { 3 } = R _ { i } ^ { 3 } - \big [ 0 \mathrm { ~  ~ 1 ~ } 0 \big ] ^ { T }\tag{4}
$$

Let detection matrix $C ^ { \prime }$ to be (5).

$$
\begin{array} { r } { C ^ { \prime } = \left[ \begin{array} { l l l } { 1 } & { - 1 } & { 0 } \\ { 0 } & { - 1 } & { 1 } \end{array} \right] } \end{array}\tag{5}
$$

Define result vector as $X _ { i j } ^ { \prime } = C ^ { \prime } R _ { i j } ^ { 6 } \ : . \ : \mathrm { ~ I f ~ } \left\| X _ { i j } ^ { \prime } \right\| _ { \infty } = 2$ ， keep on to calculate corresponding information matrix. If $\left\| X _ { i j } ^ { \prime } \right\| _ { \infty } < 2$ , no more calculation will be activated.

$P _ { i } ^ { \prime } { = } d i a g \left( p _ { 1 } ^ { \prime } , p _ { 2 } ^ { \prime } \cdots p _ { m } ^ { \prime } \right) _ { m \times m }$ is the diagonal matrix of row information, $Q _ { j } ^ { \prime } = d i a g \left( q _ { 1 } ^ { \prime } , q _ { 2 } ^ { \prime } \cdots q _ { n } ^ { \prime } \right) _ { n \times n }$ is the diagonal matrix of column information. $ \mathrm { I f } \| X _ { i j } ^ { \prime } \| _ { \infty } = 2$ ，then $p _ { i } ^ { \prime } { = } 2 , q _ { i } ^ { \prime } { = } { - } 2$ . The other elements of $P _ { i } ^ { \prime }$ and $\mathcal { Q } _ { i } ^ { \prime }$ are 1. Then the information matrix $Y _ { i j } ^ { \prime } = P _ { i } ^ { \prime } A Q _ { j } ^ { \prime }$ can be obtained. If element 2 locates in kth row $\left( k = 1 , 2 . . . m \right)$ ， information of "fault happens in the protection scope of remote back-up protection" should be transmitted to the upstream substation for line k .

## B. Decision-making algorithm of back-up protection

(1) Decision-making algorithm of local back-up protection According to the action states of local protections and received information, define $R _ { i j } ^ { 8 }$ as shown in (6).

$$
R _ { i j } ^ { 8 } = \left[ D _ { 1 } \quad D _ { 2 } \quad D _ { 3 } \quad D _ { 4 } \quad D _ { 5 } \quad D _ { 6 } \quad S _ { 1 } \quad S _ { 2 } \right] ^ { T }\tag{6}
$$

Detection matrixes $C _ { 1 }$ and $C _ { 2 }$ are defined in (7) and (8) respectively.

$$
C _ { 1 } = \left[ \begin{array} { c c c c c c c c } { 1 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 1 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 1 } & { 1 } & { 0 } & { 0 } & { 0 } & { 0 } & { 0 } \end{array} \right]\tag{7}
$$

$$
C _ { 2 } { = } \left[ \begin{array} { l l l l l l l l l } { { 1 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 1 } } & { { 0 } } & { { 0 } } & { { 1 } } & { { 0 } } & { { 1 } } & { { 0 } } \\ { { 0 } } & { { 0 } } & { { 0 } } & { { 0 } } & { { 1 } } & { { 1 } } & { { 1 } } & { { 0 } } \end{array} \right]\tag{8}
$$

$$
X _ { 1 i j } = C _ { 1 } R _ { i j } ^ { 8 }
$$

$$
X _ { 2 i j } = C _ { 2 } R _ { i j } ^ { 8 }
$$

$$
\left\| X _ { 1 i j } \right\| _ { \infty } = 2\tag{or}
$$

$\left\| X _ { 2 i j } \right\| _ { \infty } = 3$ ,the corresponding substation back-up protection will trip with time delay of O.5s as local back-up protection. Else, substation back-up protection will not trip as local backup protection.

(2) Decision-making algorithm of remote back-up protection

According to the action states of local protections and received information, define vector $R _ { i j } ^ { 1 1 }$ as shown in (9).

$$
R _ { 3 3 } ^ { 1 1 } = \left[ D _ { 1 } ~ D _ { 2 } ~ D _ { 3 } ~ D _ { 4 } ~ D _ { 5 } ~ D _ { 6 } ~ D _ { 7 } ~ D _ { 8 } ~ S _ { 1 } ~ S _ { 2 } ~ S _ { 3 } \right] ^ { T }\tag{9}
$$

where, $D _ { 7 }$ and $D _ { 8 }$ are the action states of starting elements of device I and II respectively. If the corresponding starting element acts, $D _ { \boldsymbol { k } } = 1 \ ( \boldsymbol { k } = 7 , 8 \ ) ;$ else, $D _ { k } = 0 ( k = 7 , 8 ) . \ S _ { 3 }$ is receiving state of information of "fault happens in the protection scope of remote back-up protection". If the information is received, $S _ { 3 } = 1$ ; else, $S _ { 3 } = 0$

As it is difficult to detect $R _ { i j } ^ { 1 1 }$ , revised vector $\tilde { R } _ { i j } ^ { 1 1 }$ as shown

in (10) is defined,

$$
\tilde { R } _ { i j } ^ { 1 1 } = R _ { i } ^ { 1 1 } - \left[ 1 \quad 1 \quad 1 \quad 1 \quad 0 \quad 0 \quad 0 \quad 0 \quad 1 \quad 0 \quad 0 \right] ^ { T }\tag{10}
$$

Detection matrix $C _ { 3 }$ is defined in (11).

$$
C _ { 3 } = \left[ \begin{array} { c c c c c c c c c c c c c } { - 1 } & { - 1 } & { - 1 } & { - 1 } & { 1 } & { 1 } & { 0 } & { 0 } & { - 1 } & { 0 } & { 1 } \\ { - 1 } & { - 1 } & { - 1 } & { - 1 } & { 0 } & { 0 } & { 1 } & { 1 } & { - 1 } & { 0 } & { 1 } \\ { - 1 } & { - 1 } & { - 1 } & { - 1 } & { 1 } & { 0 } & { 0 } & { 1 } & { - 1 } & { 0 } & { 1 } \\ { - 1 } & { - 1 } & { - 1 } & { - 1 } & { 0 } & { 1 } & { 1 } & { 0 } & { - 1 } & { 0 } & { 1 } \end{array} \right]\tag{11}
$$

Let $X _ { _ { 3 i j } } = C _ { 3 } \tilde { R } _ { i j } ^ { 1 1 } \mathrm { ~ . I f ~ } \left\| X _ { 3 i j } \right\| _ { \infty } = 8$ ，the transmission line i of substation j is identified in the protection scope of remote back-up protection. The corresponding substation back-up protection will trip with time delay of 1.0s as remote back-up protection. Else, substation back-up protection will not trip as remote back-up protection.

## IV.SIMULATION EXAMPLES

In order to test the performance of proposed substation back-up protection, simulation model of IEEE 10-generator-39 bus is built with PSCAD/EMTDC,as shown in Fig.3.

![](images/204f910ce7204e74a8bfd7d59412719d553f67c051b3d3b6b66d08254498d51c.jpg)  
Fig.3 Model of IEEE10-generator-39-bus system

Lots of simulations are carried out, and the following six simulation conditions are chosen as representatives. Simulation condition ①: fault happens on $L _ { 5 }$ ,the two sets of pilot protection both act correctly. Simulation condition $\textcircled{2}$ ：fault happens on $L _ { 5 }$ , but only one set of pilot protection acts. Simulation condition ③: fault happens on $L _ { 5 }$ ,but the two sets of pilot protection both do not act. Simulation condition $\textcircled{4} \textcircled{4} \textcircled{4}$ fault happens on $L _ { 5 }$ ,but the DC power supply in substation B3 is lost. Simulation condition ③: fault happens on $L _ { 5 }$ , but the DC power supply in substation B4 is lost. Simulation condition ?: $L _ { 8 }$ is out of operation, and the flow transfers to $L _ { 5 }$

The tripping time delays of relevant protections are shown in Table I. It needs to notice that "x" in the table represents the protection does not trip." B2L3 " represents the substation back-up protection for $L _ { 3 }$ in substation $B _ { 2 }$ .The others have the same meaning.

For simulation conditions ①\~③,even in condition of failto trip of primary protection,the substation back-up protections for $L _ { 5 }$ in substation B3 and B4 which are denoted as B3L5 and B4L5 respectively can trip as local back-up protection with time delay of O.5s.The other relevant substation back-up protections,like B2L3，B5L7，B14L8 and B18L6 can trip as remote back-up protection with time delay of 1.0s.

TABLE I  
Tripping Time Delays of Protection under Conditions ①\~③
<table><tr><td rowspan="2">simulation condition</td><td colspan="6">Substation back-up protection</td></tr><tr><td>B2L3</td><td>B3L5</td><td>B4L5</td><td>B5L7</td><td>B14L8</td><td>B18L6</td></tr><tr><td>①~③</td><td>1.0s</td><td>0.5s</td><td>0.5s</td><td>1.0s</td><td>1.0s</td><td>1.0s</td></tr><tr><td>④</td><td>1.0s</td><td>X</td><td>0.5s</td><td>1.0s</td><td>1.0s</td><td>1.0s</td></tr><tr><td>⑤</td><td>1.0s</td><td>0.5s</td><td>×</td><td>1.0s</td><td>1.0s</td><td>1.0s</td></tr><tr><td>⑥</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr></table>

In condition that the DC power supply failure happens, all of the breakers in corresponding substation can not trip.But the power consumption of protection devices and communication system is small. Hence, they can still keep in normal operation with UPS. Take simulation condition ④ as example to analyze the performance of proposed substation back-up protection in condition of DC power supply failure.As DC power supply in substation B3 is lost, the substation back-up protection B3L5 can not trip as local back-up protection. While the substation back-up protection B4L5 can still correctly trip as local back-up protection with time delay of O.5s.In order to isolate fault, the substation back-up protections B2L3 and B18L6 trip as remote back-up protection with time delay of 1.0s.Meanwhile, substation back-up protections B5L7 and B14L8 will trip as remote back-up protection of B3L5 with time delay of 1.0s.

For simulation condition ③, heavy flow transfer happens. In this condition, traditional distance protection will trip incorrectly. While, for the proposed substation back-up protection, the condition of decision-making of tripping strategy for local back-up protection can not be met because heavy flow transfer will not result in mal-operation of protections at both ends of line. It means that the decision-making of tripping strategy for local back-up protection is not influenced by heavy flow transfer.For the transmission line whose distance protection acts, information of "fault happens in the protection scope of remote back-up protection" can not be received. Hence, the substation back-up protection will not trip as remote back-up protection. In this sense, decision-making of tripping strategy for remote back-up protection is not influenced by heavy flow transfer either.

From the simulation results, it can be obtained that the proposed substation back-up protection has excellent performance. Even in condition of fail-to trip of primary protection, DC power supply failure in substation and heavy flow transfer, the proposed substation back-up protection can trip correctly as local back-up protection or remote back-up protection.

## V. CONCLUSION

In order to solve the problems of traditional distance protection, a novel substation back-up protection scheme based on communication channel of pilot protection is proposed.

(1) When it is used as remote back-up protection, the decision-making of tripping strategy is based on the action states of starting elements and fault detection information transmitted by adjacent substations.Hence, the proposed substation backup protection will not be influenced by branch currents,and the sensitivity of remote back-up protection is improved.

(2） When it is used as remote back-up protection, the pro-posed substation back-up protection trips with time delay of 1.0s.It means that proposed substation back-up protection effectively quicken the tripping of back-up protection.

(3)In condition of fail-to trip of primary protection, DC power supply failure and heavy flow transfer, the proposed substation back-up protection can still trip correctly to realize the function of local back-up protection or remote back-up protection.

In conclusion, the proposed substation back-up protection has excellent performance, and it is applicable for engineering application.

## REFERENCES

[1]S.H. Horowitz and A.G.Phadke,“Third zone revisited,”IEEE Trans. Power Del.,vol.21,no.1,pp.23-29,Jan.2006.

[2]D.Novosel, G.Bartok,G. Henneberg,P.Mysore,D. Tziouvaras,and S. Ward,“IEEE PSRC report on performance of relaying during wide-area stressed conditions,”IEEE Trans.Power Del.,vol.25,no.1,pp.3-16, Jan. 2010.

[3]Z.L.Yang,D.Y. Shi,and X. Z. Duan,“Wide-area protection system based on direction comparison principle,”Proc.CSEE,vol.28,no. 22, pp.87-93,Aug.2008.

[4]M.M. Eissa, M.E. Masoud,and M.M.M. Elanwar,“A novel back up wide area protection technique for power transmission grids using phasor measurement unit,”IEEE Trans.Power Del.,vol.25,no.1,pp.270- 278,Jan.2010

[5]J.C. Tan,P.A. Crossley,P.Gale,I. Hall, and J. Farrel,“Sequential tripping strategy for a transmission network back-up protection expert system".IEEE Trans.Power Del.,vol.13 no.1,pp.68-74,Jan.2002.

[6]W. Cong,Z.C.Pan,and J.G. Zhao,“A wide area relaying protection algorithm based on longitudinal comparison principle,’Proc. CSEE, vol.26,no.21,pp. 8-14,Nov.2006.

[7]Communication Networks and Systems in Substations 2007,IEC 61850, 2nd ed.

[8]Network Node Interface for the Synchronous Digital Hierarchy (SDH) 2007,ITU-T G.707/Y.1322.

Xiangping Kong was born in Jiangxi, China,in 1988.He is currently pursuing the Ph.D.degree at Huazhong University of Science and Technology (HUST),Wuhan, China.

His research interest is protection of power grid with accession of distributed generators.

Zhe Zhang received the Ph.D. degree in electrical engineering from HUST, Wuhan, China,in 1992.

Currently, he is a professor in the College of Electrical and Electronic Engineering, HUST.His interest is protective relaying.

Fei Wang was born in Wuhan,China,in 1988.She is currently pursuing the Master degree at HUST,Wuhan, China.

Her research interest is substation protection.

Xianggen Yin received the Ph.D.degree in electrical engineering from HUST, Wuhan, China,in 1989.

Currently,he is a professor in the College of Electrical and Electronic Engineering,HUST.His major areas include protective relaying and power system stability control.