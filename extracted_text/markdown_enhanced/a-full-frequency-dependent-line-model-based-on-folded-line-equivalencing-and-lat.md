# A full frequency dependent line model based on folded line equivalencing and latency exploitation

Felipe Camara$^{a}$, Antonio C.S. Lima$^{a,*}$, Fernando A. Moreira$^{b}$

$^{a}$ Federal University of Rio de Janeiro, Brazil  
$^{b}$ Federal University of Bahia, Brazil  

$^{*}$ Corresponding author.  
E-mail addresses: fcamara@ufrj.br (F. Camara), acsl@dee.ufrj.br (A.C.S. Lima), moreiraf@ufba.br (F.A. Moreira).

**Article history:**  
Received 23 April 2017  
Received in revised form 31 July 2017  
Accepted 17 August 2017  

**Keywords:**  
Overhead line modeling  
Network synthesis  
Rational approximation  
Time-domain modeling  

**Abstract**  
This work proposes to improve the numerical performance in the rational modeling of full frequency dependent transmission lines. In this paper, latency is used to improve the numerical efﬁciency of time-domain implementation of the pole-residue representation of the nodal admittance matrix in the case of frequency dependent network equivalents. The idea of latency is to use different time-steps for distinct poles, i.e., fast poles are solved using a small time-step while slower poles may be solved using larger time-steps. For the separation of the slow and fast dynamics, a technique named Multiple Companion Networks (MCN) has been developed. The technique has been applied to transient tests of a transmission line modeled with a rational model. The results obtained indicated that a gain in numerical efﬁciency is possible without compromising accuracy.

## 1. Introduction

Electromagnetic transient (EMT)-programs allowed for a rapid and wide development of time-domain models for linear, nonlinear and frequency dependent devices. One main characteristic of such approach is to rely on the use of a single time-step for the solution of the whole network. This is often a waste of computational resources since it may be the case where only a small part of the network has to be solved using a small time step, whereas a large part of the network could be solved with a larger time step. Thus a suboptimal numerical performance is found leading to an unnecessary large simulation time.

One possibility to overcome the unnecessary simulation time and to improve the numerical performance of the models involved is to rely on the concept of latency exploitation. In latency [1], the network is divided into at least two sub-networks. The ﬁrst one, associated with the fastest time-constants, is solved using a small time-step, while a larger time-step is used to solve the other part of the network. Naturally, the number of network subdivisions can increase leading to several sub-networks each being solved with a given time-step. For this reason, latency exploitation may also be called multirate simulation.

The development of numerically accurate and efﬁcient methods for the rational approximation of frequency responses such as the so-called vector ﬁtting routine [2–4], the frequency-partitioning ﬁtting [5] or the matrix pencil [6,7] allowed the realization of full frequency dependent overhead lines and underground cable models in phase coordinates in EMT-simulations [8,9]. One drawback of such models which are based on the method of characteristics (MoC) is that the time-step must be smaller than the fastest modal time-delay which requires a rather accurate procedure for this identiﬁcation [10]. Furthermore, inaccurate interpolation schemes between the simulation time-step and the modal traveling time might lead to numerical instabilities [11]. This scenario is more important for shorter lines where a very small time-step might be used and the interpolation of the modal time-delay might reduce the numerical efﬁciency of a line model based on MoC. An alternative to overcome this limitation is to use a rational approximation of the nodal admittance matrix associated with the transmission line. However, as pointed out in [12], the direct ﬁtting of the nodal admittance matrix is not suitable for a general transmission line model as the smallest eigenvalues at the low-frequency range may not be properly ﬁtted leading to inaccurate responses. The limitation associated with the direct ﬁtting can be overcome with the use of the folded line equivalent (FLE) model as also shown in [12].

In [13], the authors proposed to exploit latency in a frequency dependent network using a rational approximation of the nodal admittance matrix developing the Multiple Companion Network (MCN) approach. In this work the formulation of the MCN based on a model decomposition using the FLE has been extended. It was found that the earlier approach led to rather inaccurate results for the time responses and it was needed to rearrange how latency is exploited in the MCN.

where $I$ is the same as before. This formulation was proposed in [12] and received the name folded line equivalent (FLE). It has some interesting characteristics, the matrices to be ﬁtted have half the dimension of the original admittance matrix, i.e., $Y_n$ has a dimension $2n \times 2n$ while both $Y_{oc}$ and $Y_{sc}$ are $n \times n$ matrices. Furthermore, the ratio between the largest and smallest eigenvalues in both $Y_{oc}$ and $Y_{sc}$ reduces considerably when compared with the ones found in $Y_n$.

The paper is organized as follows: Section 2 summarizes the application of FLE to the modeling of an overhead line. Section 3 explains the idea behind latency exploitation and the use of MCN and how some improvements can be achieved using this formulation. Section