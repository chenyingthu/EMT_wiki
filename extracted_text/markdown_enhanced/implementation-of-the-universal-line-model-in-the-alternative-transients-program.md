# Implementation of the universal line model in the alternative transients program

**Felipe O.S. Zanon**$^{a,*}$, **Osis E.S. Leal**$^{b}$, **Alberto De Conti**$^{c}$

$^{a}$ Graduate Program of Electrical Engineering (PPGEE), UFMG, Brazil  
$^{b}$ UTFPR – Federal University of Technology – Paraná, Pato Branco, Brazil  
$^{c}$ Department of Electrical Engineering (DEE), Federal University of Minas Gerais (UFMG), Brazil  

**Keywords:** Electromagnetic transients, Transmission line models, Phase-domain models, EMT-type programs, Frequency-dependent soil parameters

**Abstract:** The universal line model (ULM) is a transmission line model developed directly in the phase domain that is recognized for its accuracy and generality. It is currently the reference model for transient studies, but is exclusively found on commercial electromagnetic transients programs. This paper describes an implementation of ULM in the Alternative Transients Program (ATP), which is free for licensed users, using the foreign models tool and the type-94 component available in this platform. The implemented model is validated through comparisons with EMTP-RV. Then, it is used to investigate transients on overhead transmission lines considering a rigorous representation of the ground return impedance and ground admittance assuming frequency-dependent ground parameters.

*This paper was supported by the National Council for Scientific and Technological Development (CNPq) (306006/2019-7) and by the State of Minas Gerais Research Foundation (FAPEMIG) (TEC-PPM-00280–17).*  
*Corresponding author. E-mail addresses: felipeos.zanon@gmail.com (F.O.S. Zanon), osisleal@utfpr.edu.br (O.E.S. Leal), conti@cpdee.ufmg.br (A. De Conti).*

## 1. Introduction
The analysis of transients on realistic power systems is usually performed in electromagnetic transient (EMT) simulators. For this, the correct modeling of the system components is crucial, especially the solution of the transmission line equations in the time domain. The two most popular transmission line models currently available in EMT-type tools are the frequency-dependent model proposed by Marti (JMarti) [1] and the Universal Line Model (ULM) [2].

Marti’s model solves the transmission line equations in the modal domain considering a real and constant transformation matrix. The magnitudes of the propagation function and characteristic impedance of each line mode are represented as rational functions using Bode’s asymptotic fitting [3]. The resulting model can accurately simulate a number of overhead line configurations [4], even if frequency-dependent ground parameters are considered [5]. However, it is not recommended to simulate underground cable systems and strongly asymmetric overhead transmission lines because the associated eigenvectors present a strong variation with frequency. In this case, the assumption of a real and constant transformation matrix no longer holds.

ULM circumvents the limitations of Marti’s model by solving telegrapher’s equations directly in the phase domain. It has been successfully used to simulate transients on overhead transmission lines and underground cables [6]. The model is based on the fitting of both the characteristic admittance matrix $Y_C$ and the propagation matrix $H$ with complex poles and zeros [7]. The development of ULM is relatively recent and the model has been continuously improved [8].

Despite its advantages over Marti’s model, ULM is only available in commercial EMT simulators (e.g., [9, 10]). Its absence in the Alternative Transients Program (ATP), which is free to licensed users, frequently poses difficulties to the analysis of transient phenomena for which Marti’s model is not sufficiently accurate. In principle, this problem could be overcome with Noda’s phase-domain transmission line model [11], which is available in ATP. However, this model is sensitive to the selected time step and prone to fitting errors [12]. As a consequence, it is often difficult for ATP users to deal with cases that require a phase-domain line model. This context has motivated this paper, which presents an implementation of ULM in ATP. In this proposal, the line parameters are first calculated and fitted in MATLAB. The fitted parameters are then used as input parameters of a code written in C language that implements the ULM equations. The code is finally interfaced with ATP as a foreign model using a type-94 component [13].

This paper is organized as follows. Section II discusses ULM in brief. Section III presents its implementation in ATP. Section IV validates the implemented model using EMTP-RV as a reference. Section V evaluates the impact of considering more rigorous formulations for the calculation of the ground return impedance and per-unit-length admittance including frequency-dependent soil electrical parameters. Finally, Section VI presents the conclusions.

## 2. ULM
ULM is presented in detail in [2]. This section aims to highlight the aspects of the model that are the most important for its implementation.

### 2.1. Model formulation
described in the next sections.

### 2.2. Characteristic admittance matrix $Y_C$
The characteristic admittance matrix presents a smooth behavior and can be fitted directly in the phase domain with a relatively small number of poles [14]. The poles of the approximate matrix $\tilde{Y}_C$ are obtained by

*Fig. 2. Frequency-domain equivalent circuit of ULM.*