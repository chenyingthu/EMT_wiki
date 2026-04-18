# Direct Interfacing of Parametric Average-Value Models of AC–DC Converters for Nodal Analysis-Based Solution

**Seyyedmilad Ebrahimi**, Member, IEEE, **Hamid Atighechi**, Member, IEEE, **Sina Chiniforoosh**, Senior Member, IEEE, and **Juri Jatskevich**, Fellow, IEEE

**Abstract**—AC–DC converters are widely used in many power-electronic-based systems. There is an increasing need to simulate such systems using larger time-steps in offline and/or real-time electromagnetic transient (EMT or EMTP) simulators. The so-called parametric average-value models (PAVMs) have been developed to allow larger time-steps and provide fast simulations. However, the application of PAVMs in nodal-analysis-based EMTP programs typically requires a one-time-step delay between the interfacing sources and the network solution (i.e., indirect interfacing), causing inaccuracy and numerical instability at medium-to-large time-steps. This paper presents a direct interfacing method for PAVMs of line-commutated rectifiers (LCRs). The proposed method linearizes the PAVM interfacing equations and incorporates the respective sub-matrices and history terms into the network nodal equations, which eliminates the need for a time-step delay. Simulation studies verify the effectiveness of the proposed method in EMTP-type solution wherein very good accuracy and numerical stability is achieved at fairly large time-steps, which has not been previously possible with conventional methods.

**Index Terms**—Ac–dc converters, average-value model, direct interfacing, discretization, EMTP simulation, nodal analysis.

## I. INTRODUCTION

POWER-ELECTRONIC ac–dc converters play a vital role in integrating modern energy resources with conventional power systems. More specifically, the line-commutated converters (LCCs) and rectifiers (LCRs) composed of diodes or thyristor switches have been widely used in classic HVDC systems [1], wind generation systems [2], exciters of synchronous generators [3], vehicular, marine and aircraft power systems [4]–[6], melting induction furnaces [7], etc.

Analysis of such power systems heavily relies on simulation studies that are conducted offline and/or real-time in either state-variable-based programs (SVB, e.g., PLECS, RT-Lab, Typhoon HIL, etc.) or nodal-analysis-based electromagnetic transient programs (EMTP, e.g., EMTP-RV, PSCAD, RTDS, etc.). The SVB- and EMTP-type programs have their own merits and solve the network differently; however, the vendors of both are trying to enhance their engines and allow simulations at large time-steps to accommodate studies of larger power systems using given simulator hardware. Examples include, but are not limited to, Opal-RT’s ePHASORSIM [8], superstep in RTDS NovaCor [9], etc.

The detailed switching models of ac–dc converters have always been simulation bottlenecks for large-scale systems. Although being easy to implement and highly accurate, they require special handling of discrete switching events, e.g., using zero-crossing detection, interpolation, etc., [10]–[12], which imposes a computational burden, limiting the size of the power system and the number of switches that can be simulated.

To address this issue for system-level studies, dynamic phasor models [13]–[14] as well as average-value models (AVMs) [15]–[26] have been developed for ac–dc converters, where the individual switching is neglected. Therefore, the AVMs become independent of switching events and can adopt larger time-steps. Analytically derived AVMs (AAVMs) [15]–[18] are valid only in the specific mode of operation for which the formulations are derived. However, the parametric AVMs (PAVMs) [19]–[26] have proven accurate over a wide range of operating conditions of the LCR. An interested reader is referred to [25, Table I] for a comparison between different state-of-the-art AAVMs and PAVMs.

In both SVB and EMTP-type programs, the AVMs are typically interfaced with external networks using controlled voltage/current sources [26]. Some SVB packages are able to solve the external networks simultaneously with the AVMs. However, in EMTP-type simulators, the discretization is done at the component level (based on the nodal approach), which, when implemented without iterations, requires a one-time-step delay between the interfacing sources of the AVMs (in most EMTP programs, e.g., [9], [11]). The method of incorporating a time-step delay is often referred to as indirect interfacing [17], [20]–[21]. Consequently, with this method, to maintain the accuracy and avoid numerical instability, the simulation time-step size should be fairly small. This limits the advantage of AVMs in EMTP simulations and defies one of the original purposes of developing AVMs (which is to allow using larger time-steps for

---
*Manuscript received 16 October 2021; revised 17 February 2022; accepted 6 May 2022. Date of publication 23 May 2022; date of current version 30 November 2022. This work was supported by the Natural Science and Engineering Research Council of Canada under the Collaborative Research and Development Grant. Paper no. TEC-01128-2021. (Corresponding author: Juri Jatskevich.)*

*Seyyedmilad Ebrahimi, Sina Chiniforoosh, and Juri Jatskevich are with the Electrical and Computer Engineering Department, The University of British Columbia, Vancouver, BC V6T 1Z4, Canada (e-mail: ebrahimi@ece.ubc.ca; sinach@ece.ubc.ca; jurij@ece.ubc.ca).*

*Hamid Atighechi is with the Powerex Corp., Vancouver, BC V6C 2X8, Canada (e-mail: h.atighechi@gmail.com).*

*Color versions of one or more figures in this article are available at https://doi.org/10.1109/TEC.2022.3177131.*

*Digital Object Identifier 10.1109/TEC.2022.3177131*

*0885-8969 © 2022 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.*