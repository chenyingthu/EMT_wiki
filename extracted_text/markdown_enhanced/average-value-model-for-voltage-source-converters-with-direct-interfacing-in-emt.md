# Average-Value Model for Voltage-Source Converters With Direct Interfacing in EMTP-Type Solution
Seyyedmilad Ebrahimi, Member, IEEE, and Juri Jatskevich, Fellow, IEEE

**Abstract**—Average-value models (AVMs) of high-frequency switching voltage-source converters (VSCs) are indispensable for fast/efficient simulation of VSC-based power systems. However, in EMT/EMTP-type programs large simulation time-steps cannot be utilized with conventional non-iterative interfacings of AVMs due to numerical inaccuracy/instability as a result of a one-time-step interfacing delay. In this letter, a directly-interfaced AVM has been developed for the VSCs which eliminates the interfacing delay and allows large time-steps. This is achieved by formulating the AVM in the nodal form that is solved simultaneously with the overall network nodal equations. The new proposed model is demonstrated to outperform the existing AVMs of VSCs in terms of accuracy at fairly large time steps.

**Index Terms**—Average-value model, direct interfacing, HVDC, interfacing, nodal, simulation, VSC.

## I. INTRODUCTION
VOLTAGE-SOURCE converters (VSCs) are utilized in a broad range of applications, e.g., HVDC Light systems [1], FACTS devices, wind generation, aircraft and vehicle power systems, etc. The offline and real-time electromagnetic transient (EMT) and EMTP-type programs that are indispensable for system studies are now being pushed to their limits. Numerical techniques that enable using large time-step sizes for simulations of VSC-based networks and better utilization of the available simulation hardware are becoming particularly important. Efforts are made to allow larger time-steps in offline/real-time simulations, e.g., superstep in RTDS NovaCor [2], etc.

Due to the high-frequency switching, the discrete detailed models of the VSCs require small time steps for numerical stability/accuracy and are thus not suitable for large-scale simulations. Alternatively, the average-value models (AVMs) [3] of VSCs have been utilized for such studies, wherein the details of switching are neglected (averaged out) to facilitate faster simulations by allowing larger time-steps. The AVMs are continuous and independent of the switching frequency; and are valid for dynamics only slower than the switching frequency [3] beyond which the averaging assumptions that are used in their derivations may no longer be valid.

*Fig. 1. A generic VSC-based ac–dc system.*

In many EMTP-type programs, e.g., PSCAD, the AVMs of VSCs can be readily implemented using controlled voltage/current sources that are interfaced with external circuits [3]. This type of non-iterative interface with the nodal approach requires a time-step delay between the external network solution and the controlled sources (and is referred to as indirect interfacing). This delay can cause numerical inaccuracy/instability at large time-steps and inevitably limits the advantage of AVMs in system-level simulations of VSC-based networks.

Recently, direct interfacing has been developed for AVMs of the line-commutated converters (i.e., diode or thyristor-controlled rectifiers) in EMTP-type programs [4]. This letter develops and presents the direct interfacing of the AVMs of the widely-utilized VSCs. This is done by formulating the VSC AVM equations according to the EMTP non-iterative approach, wherein the discretized conductance matrix and controlled history terms naturally depend on the previous time-step (thus removing any artificial time-step delays). The AVM sub-matrices are then incorporated into the overall network nodal equation and solved simultaneously with the external networks, allowing large time-steps, as verified by the presented computer studies.

It is noted the directly interfaced AVM developed in this letter would be valid for both rectifier and inverter modes of operation of the VSCs. Also, the proposed model is based on the analytical AVM [3] (as opposed to [4], which requires numerically-extracted lookup tables).

Manuscript received 17 June 2022; revised 22 September 2022; accepted 24 October 2022. Date of publication 7 November 2022; date of current version 22 August 2023. This work was supported by the Natural Science and Engineering Research Council (NSERC) of Canada under the Collaborative Research and Development Grant. Paper no. PESL-00167-2022. (Corresponding author: Juri Jatskevich.)
The authors are with the Electrical and Computer Engineering Department, The University of British Columbia, Vancouver, BC V6T 1Z4, Canada (e-mail: ebrahimi@ece.ubc.ca; jurij@ece.ubc.ca).
Color versions of one or more figures in this article are available at https://doi.org/10.1109/TEC.2022.3220085.
Digital Object Identifier 10.1109/TEC.2022.3220085

## II. FORMULATION AND INTERFACING OF AVMS FOR VSCS
For the purpose of this letter, it is assumed that the ac subsystem connected to the VSC is modeled as a Thévenin equivalent circuit shown in Fig. 1. Therein, the equivalent sources are specified by voltages $e_{abc}$ and angle $\theta_s$ which can be typically identified by a PLL-type grid synchronization. The VSC outputs the ac voltages $v_{abc}$ (with respect to the neutral point of the Thévenin sources) whose fundamental frequency components are shifted from $\theta_s$ by the angle $\delta$, and their amplitude is specified by the modulation index $M$. The variables $M$ and $\delta$ can be either set manually or calculated by the power/current controllers.

To formulate the AVM, the ac variables are transformed to a rotating $q$-$d$ reference frame using Park’s transformation matrix
AVM formu