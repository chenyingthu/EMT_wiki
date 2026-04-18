# Loewner matrix approach for modelling FDNEs of power systems
**Gurunath Gurrala**<sup>∗</sup>
*Department of Electrical and Computer Engineering, Texas A&M University, USA*

**Article history:**
Received 11 October 2014
Received in revised form 19 March 2015
Accepted 21 March 2015

**Keywords:**
Frequency dependent network equivalents
Tangential interpolation
Loewner matrix
Electromagnetic transients (EMT)
Vector fitting

**Abstract**
This paper proposes a new approach for modelling frequency dependent power system network equivalents (FDNE) using tangential interpolation framework based on Loewner matrix (LM) pencil. The Loewner matrix based tangential interpolation technique has been recently proposed for modelling of large multi-port VLSI circuits. The LM approach fits accurate state space descriptor system models from the frequency response measurements. Singular value decomposition based LM approach has been investigated in this paper for modelling of FDNEs. The proposed method’s performance is compared to the widely used vector fitting approach using four power system examples. A simple matrix implementation for LM formation and a MATLAB based stable model extraction approach is proposed. It has been shown that the data splitting step of the LM approach has significant impact on the accuracy of the fitting. The LM method is shown to be comparable to vector fitting in terms of accuracy, stability and passivity. It does not require any starting poles and has no convergence issues because it is a non-iterative method. It also gives an indication of the system order which is a unique advantage.

<sup>∗</sup> Corresponding author. Current address: Power and Energy Systems Group, Oak Ridge National Lab, USA. Tel.: +1 9796760147. E-mail address: gurunath gurrala@yahoo.co.in

## 1. Introduction
The quest for efficient frequency dependent models in power system electromagnetic transient (EMT) simulations is a never ending journey. Early electromagnetic transient programs (EMTP) used frequency dependent models mostly for switching transient studies and lightning studies for planning and design of high voltage equipment such as switchgear, insulators and high voltage DC systems (HVDC) [1]. The need for accurate and reliable electromagnetic transient equivalents have been growing significantly across the industry with the introduction of fast switching devices (power electronic circuit breakers), complex generation sources (wind, solar and other power electronic based sources) and complex transmission controls such as voltage source converter based DC systems (VSC-HVDC), flexible AC transmission controls (FACTS), etc. This need exists because their frequency responses closely overlap with the natural frequency responses of various power system components like distributed transmission lines, transformers, etc. [2]. In the near future EMT programs will become a necessity even for day to day operations because of the growing interconnections and complex control interactions.

There are several frequency dependent network equivalent (FDNE) modelling techniques available and good surveys of the techniques are presented in [1,3,4]. Rational approximations using iterative methods [5] became popular in recent years. Vector fitting and several variations of it are widely used for FDNE’s [6,7]. A multi-port time domain-vector fitting method is proposed in [8]. Vector fitting requires a good guess of the starting poles for successful pole-relocation and sometimes needs separate passivity enforcement. There is no proof of when and how fast Vector fitting converges [9]. Frequency partitioning approach has been proposed in [10–12] to avoid ill-conditioning in FDNEs. The trial and error based frequency partitioning approaches are time consuming for networks involving large number of ports. A genetic algorithm based approach that preserves the passivity of the FDNE model is proposed in [13]. In [2,14] the need for large scale FDNEs is identified and a sparse time domain network equivalent method is proposed.

Methods for constructing a controllable and observable state space model, called generalized realization problem, from a data set obtained by sampling a transfer matrix are proposed in [15]. These methods use data sampled directionally, called tangential interpolation data. Recently, an accurate multi-port modelling technique for systems with large number of terminals has been proposed in [9,16]. This method uses the Loewner matrix (LM) pencil constructed from frequency response data in the framework of tangential interpolation. Performance of the Loewner method in the presence of noisy measurements has been studied in [17]. Application of Loewner matrix approach for distributed parameter models of micro electronic circuits is presented in [18]. All the above references claim that the LM approach is superior to vector fitting as this is a non-iterative approach that accurately fits models for large multi-port systems [16] without any convergence issues. It doesn’t need any starting poles. The LM approach usually preserves

and the left interpolation data:
$$ M = \text{diag}[\lambda_1, \dots, \lambda_h] \in \mathbb{C}^{h \times h} $$
$$ \begin{bmatrix} l_1 \\ \vdots \end{bmatrix} \quad \begin{bmatrix} v_1 \\ \vdots \end{bmatrix} $$