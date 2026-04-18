## Compacting and partitioning-based simulation solution for frequency-dependent network equivalents in real-time digital simulator

Yizhong Hu, Wenchuan Wu ✉, Boming Zhang  
Department of Electrical Engineering, Tsinghua University, Beijing, People’s Republic of China  
✉ E-mail: wuwench@tsinghua.edu.cn

**Abstract:** Rational models of frequency-dependent network equivalents (FDNEs) have been used in real-time digital simulator (RTDS) for power-system simulation. However, this can lead to a computational burden issue; the application of FDNEs may result in a loss of real-time simulation features because the computational cost of the FDNE component exceeds the limits of RTDS. The authors describe a solution that combines compacting and partitioning of the FDNEs, whereby the former reduces the redundancy in the mathematical model and the latter allows us to exploit parallel computer architectures. Then they describe the results of numerical simulations that demonstrate the effectiveness of the approach. Moreover, the proposed simulation solution is not limited to the applications of FDNEs in RTDS, it solves a set of subsistent computational issues when apply rational models in real-time electromagnetic transients programs tools.

### Nomenclature

| Symbol | Description |
|---|---|
| EMTP | electromagnetic transient program |
| FDNE | frequency dependent network equivalent |
| RTDS | real-time digital simulator |
| $Y(s)$ | rational model of FDNE (matrix) |
| $y(s)$ | element of $Y(s)$ |
| $a_i$ | poles in rational model |
| $c_i$ | residues in rational model |
| $d$ | constant term in rational model |
| $h$ | one-degree term in rational model |
| $N$ | number of FDNE ports |
| $n$ | number of poles |
| $P$ | number of network ports |
| $O$ | computational cost |
| $\Delta t$ | time step of simulation |
| $G_{eq}$, $I_{his}$ | equivalent admittance matrix and historical current in EMTP simulation |

## 1 Introduction

Frequency-dependent network equivalents (FDNEs) are applied in electromagnetic transients programs (EMTP) tools for power system simulation, since they can reduce the scale of the system while keep the frequency characteristics of the original network. FDNEs were firstly proposed in the form of simple RLC modules, whose parameters are tuned to match the network’s frequency response [1, 2]. This kind of model seems to be complex and inﬂexible by now. With the development of rational modelling [3] and ﬁtting method [4], the rational model of FDNEs [5] has become popular. In [6–9], some examples of implementing FDNE rational models in EMTP tools are shown.

EMTP tools are classiﬁed into two main categories: off-line and real time [10]. The main difference is that real-time EMTP tools are able to conduct real-time simulation, i.e. generating results in synchronism with a real-time clock. Such tools can be interfaced with physical devices via power ampliﬁers, therefore having signiﬁcant advantages in the study and testing of high-voltage direct current (HVDC) and ﬂexible alternating-current transmission system control, excitation control, and relays. Currently, there are several industrial grade real-time EMTP tools [10] such as HYPERSIM [11], RT-LAB [12] and real-time digital simulator (RTDS) [13].

RTDS, as with other real-time EMTP tools, is based on parallel computer architectures, so the required resources scale approximately linearly with the size of the problem [14]. In this respect, it is appropriate to use FDNEs to represent the parts of a system that need not be modelled in detail to simulate large systems in real time [6–8]. However, compressing some part of a system to an FDNE model may lead to local overload of the computational resources. Speciﬁcally, although the size of an FDNE model is signiﬁcantly less than that of the original network, the latter can be handled by parallel computing, whereas the former can only utilise limited computational resources since it is modelled on an individual processor. Therefore, when the computational cost is particularly high, it may not be possible to simulate an FDNE component in real time.

This issue has not been discussed in any detail, however, because only small-scale FDNEs with relatively few ports and poles have been studied [6–8]. (It will be shown in Section 3 that the computational cost of FDNEs is directly related to the number of ports and poles.) This is a critical issue for real-time simulation using FDNEs: if the application of FDNEs results in the loss of real-time simulation capacity, then the most important attribute of FDNEs will be lost. In this paper, we discussed two techniques to tackle the issue of FDNEs for real-time application. The ﬁrst is compacting, which decreases the calculation time by reducing the redundancy of the mathematical model. The second is partitioning, which separates the FDNE into several modules so as to utilise more computing resources in a parallel platform. The effectiveness of the approach is demonstrated using numerical tests.

It should be noted that, although this paper mainly presents the solution of accelerating FDNE simulation in RTDS, the idea can also be used for the applications of other rational models in other real-time EMTP tools.

## 2 Basics of RTDS

Most EMTP tools are based on the 1969 work of Dommel [15], so is the RTDS. All components can be represented as an equivalent admittance $G_{eq}$, as well as the historical current $I_{his}$, using the