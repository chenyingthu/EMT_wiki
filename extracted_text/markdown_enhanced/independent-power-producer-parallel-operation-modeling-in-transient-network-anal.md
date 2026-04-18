# Independent power producer parallel operation modeling in transient network simulations for interconnected distributed generation studies

Fabrício A.M. Moura $^a$, José R. Camacho $^{a,*,1}$, Marcelo L.R. Chaves $^b$, Geraldo C. Guimarães $^b$

$^a$ Universidade Federal de Uberlândia, School of Electrical Engineering, Rural Electricity and Alternative Sources Lab, PO Box 593, 38400.902 Uberlândia, MG, Brazil  
$^b$ Universidade Federal de Uberlândia, School of Electrical Engineering, Power Systems Dynamics Group, PO Box: 593, 38400.902 Uberlândia, MG, Brazil  

$^*$ Corresponding author. Tel.: +55 34 3239 4734; fax: +55 34 3239 4704.  
E-mail address: jrcamacho@ufu.br (J.R. Camacho).  
$^1$ IEEE-SM.

**Article Info**  
Article history:  
Received 19 January 2009  
Received in revised form 25 August 2009  
Accepted 26 August 2009  
Available online 8 October 2009  

**Keywords:**  
Synchronous generator  
Voltage regulator  
Speed governor  

**Abstract**  
The main task in this paper is to present a performance analysis of a distribution network in the presence of an independent power producer (IP) synchronous generator with its speed governor and voltage regulator modeled using TACS – Transient Analysis of Control Systems, for distributed generation studies. Regulators were implemented through their transfer functions in the $s$ domain. However, since ATP-EMTP (Electromagnetic Transient Program) works in the time domain, a discretization is necessary to return the TACS output to time domain. It must be highlighted that this generator is driven by a steam turbine, and the whole system with regulators and the equivalent of the power authority system at the common coupling point (CCP) are modeled in the “ATP-EMTP – Alternative Transients Program”.

## 1. Introduction
The interest for distributed generation has increased considerably over the years due to the restructuring in the Brazilian energy sector.

With the growing demand for biofuels it has become common the ethanol production in sugar mill production plants, with the electrical energy generation in such plants gaining focus as an important asset in the national energy scene. Such plants are increasing their production and are building larger installations all over the country. Consequently, an increase exists in the number of synchronous generators owned by sugar mill plants. Some of them are connected to the local power authorities’ medium level voltage. This fact, added to the current need to benefit from different forms of primary energy, technological advances and the awareness on environment conservation, is the way to induce and contribute to the dissemination of independent electrical power production.

Therefore, it is an emerging force the need to understand the influence of such aspects in the operation and design of electrical energy distribution networks. Among the analysis to be made, the monitoring of voltage levels at the common coupling point (CCP), before and after the presence of the independent power producer (IP), as well as the analysis of load rejection, the outage of distribution lines and balanced three-phase short-circuit are made necessary. Moreover, the response of the synchronous machine controls, such as the speed governor and voltage regulator, are the subject of the studies in this paper.

## 2. System modeling

### 2.1. Voltage regulator
The synchronous generator used to represent the independent power producer is the type SM 59 with eight controls in the ATP model databank [1]. The voltage regulator is modeled according to accepted references for speed governors and excitation regulators [2–4].

According to the data input, this model can be reduced to four basic forms. The model used in this work for the voltage regulator can be seen in Fig. 1, which is the type I model, one of the most complete and compact designs recommended by the IEEE [5].

### 2.2. Speed governor
The speed governor was implemented based on one of the simplest IEEE models, and often used in transient stability studies programs.

Fig. 2 presents the generic block diagram for the speed governor associated to the steam turbine (if $T_4 = 0$) or to the hydro turbine (if $T_4 \neq 0$).

### 2.3. Electrical system
The independent power producer generator becomes part of the electrical system of a power authority distribution network, as illustrated in Fig. 3. Such system is connected to the independent power producer through an interconnecting circuit breaker, following instr

**Table 1** Synchronous machine parameters for the independent generator.
| Data needed for G2 | |
|---|---|
| $S_n = 5$ MVA | $x_0 = 0.046$ pu |
| $U_n = 6.6$ kV | $T_{d0} = 1.754$ s |