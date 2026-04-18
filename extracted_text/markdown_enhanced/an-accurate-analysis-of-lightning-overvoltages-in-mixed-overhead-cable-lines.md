# An accurate analysis of lightning overvoltages in mixed overhead-cable lines

R. Alipio a, *, H. Xue b, A. Ametani c  
a Department of Electrical Engineering, Federal Center of Technological Education (CEFET-MG), Belo Horizonte, MG, Brazil  
b African Office, Global Energy Interconnection Development and Cooperation Organization (GEIDCO), Bole Sub City, Addis Ababa, Ethiopia  
c Department of Electrical Engineering, University of Manitoba, Winnipeg, MB, Canada  

**Keywords:** Overhead-cable line, Transmission line approach, Frequency-dependent soil, Frequency dependent grounding, Transient study  

**Abstract:** An accurate investigation of lightning overvoltages on a typical mixed overhead-cable line is performed. The recently developed extended transmission line (TL) approach, frequency-dependent (FD) soil model and FD grounding system modeling method are also reviewed. The wave propagation characteristics of an overhead and a cable in frequency domain are studied using classical and extended TL approaches. Moreover, transient simulations using Numerical Laplace Transform (NLT) are carried out with different FD soil parameters and FD grounding behavior, and the influences of FD characteristics on the transient cable sheath voltages are made clear.

## 1. Introduction

The use of underground cables for transmitting energy has been constantly increasing worldwide over the last few decades. According to [1], this stems from technical changes and strong competition in the cable sector, which have reduced prices. Furthermore, increased urbanization and public concerns have increased the difficulty and time taken to obtain consents for overhead (OH) lines. The use of short underground (UG) sections has also been common, either due to complaints from residents or due to physical restrictions regarding OH line terminating structures arriving the substation, resulting in mixed overhead lines with short underground sections [2].

The study of lighting overvoltages for a mixed overhead- cable lines is an important issue [3]. A lightning strike on the shielding wire of the OH line can propagate into the sheath circuit since the transmission tower and cable sheath often share the same grounding system at the transition site. Also, a back flashover can occur across OH line insulators or even a lightning strike can directly hit the phase conductors due to a shielding failure. In these cases, the lightning surge can directly propagate into the cable core, inducing voltages at the cable sheath. In systems comprising short sections, multiple reflections and superpositions can occur in a short period of time and cause severe overvoltages [4]. The sheath overvoltage requires careful studies to avoid failures of sheath voltage limiters and sheath interrupts [3].

Typically, the study of transients in power transmission systems, including mixed overhead-cable lines, is carried out using EMT-type programs (for instance in [4,5]), that adopt some assumptions that may lead to inaccurate results, especially considering lightning overvoltages and short underground sections. The cable models normally adopt Pollaczek’s formula of earth-return impedance and disregards ground displacement currents along with the earth-return admittance. The soil electrical parameters are also usually assumed constant and frequency independent. However, recent studies show that both aforementioned approximations can lead to inaccuracies in transients’ studies involving underground cables and frequency region of kHz up to MHz [6-10]. Furthermore, in most simulations, the sheath bonding and grounding is made through a simple lumped resistance, disregarding the frequency-dependent (FD) behavior of grounding system. It is to be noted that the level of the sheath overvoltage is highly dependent on the grounding performance at the transition site.

This paper assesses the influence of considering different modeling approaches in the computation of lightning overvoltages developed in short underground cable sections. The paper is organized as follows. The system under study, transmission line (TL) based parameters, FD soil model and grounding system are summarized in the Section II. In Section III, the wave propagation characteristics of overhead line and underground cable in frequency domain are investigated based on different approaches discussed in the Section II. Section IV performs the transient studies of a typical mixed overhead-cable line. Also, the influences of earth parameters, FD soil parameters and FD characteristics of grounding system on transient voltages of cable are made clear.

## 2. System under study and modeling guidelines

To focus on the fundamental aspects regarding the influence of several modeling approaches on the simulation of transient overvoltages developed in a mixed overhead-underground cable line, the single-phase equivalent circuit of $138\ \text{kV}$ mixed line shown in Fig. 1 is considered. It consists of an overhead bare phase conductor (radius of $0.9155\ \text{cm}$ and $R_{dc} = 0.2076\ \Omega/\text{km}$) positioned $12\ \text{m}$ above ground, which, in the transition tower, is connected to an insulated cable that goes down vertically to the transition point between the overhead line and the underground section.

At the transition site, the transmission tower and the cable sheath of the underground section share the same grounding system, which consists of four counterpoise copper wires of $9.525\ \text{mm}$ rad

*Fig. 2. Configuration of grounding systems: (a) transmission line grounding system, (b) substation grounding grid.*

where $P_i$ and $P_e$ are the internal and earth-return potential coefficient matrices of the cable [8].  
If earth permittivity and $P_e = 0$ are assumed in (1) and (2), then it is