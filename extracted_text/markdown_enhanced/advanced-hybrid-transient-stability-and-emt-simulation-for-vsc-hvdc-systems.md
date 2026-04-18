## Advanced Hybrid Transient Stability and EMT Simulation for VSC-HVDC Systems
Arjen A. van der Meer, Madeleine Gibescu, Mart A. M. M. van der Meijden, Member, IEEE, Wil L. Kling, Senior Member, IEEE, and Jan A. Ferreira, Fellow, IEEE

**Abstract**—This paper deals with advanced hybrid transient stability and electromagnetic-transient (EMT) simulation of combined ac/dc power systems containing large amounts of renewable energy sources interfaced through voltage-source converter–high-voltage direct current (VSC-HVDC). The concerning transient stability studies require the dynamic phenomena of interest to be included with adequate detail and reasonable simulation speed. Hybrid simulation offers this functionality, and this contribution focuses on its application to (multiterminal) VSC-HVDC systems. Existing numerical interfacing methods have been evaluated and improved for averaged VSC modeling. These innovations include: 1) ac system equivalent impedance refactorization after faults; 2) amended interaction protocols for improved Thévenin equivalent source updating inside the EMT-type simulation; and 3) a special new interaction protocol for improved phasor determination during faults. The improvements introduced in this contribution lead to more accurate ac/VSC-HVDC transient stability assessment compared to conventional interfacing techniques.

**Index Terms**—Hybrid simulation, multiterminal, transient stability, voltage-source converter–high-voltage direct current (VSC-HVDC).

### NOMENCLATURE
| Abbreviation | Description |
|---|---|
| EMT | Electromagnetic transient. |
| ES,DS | External system, detailed system. |
| QSS | Quasistationary simulation. |
| ZOH | Zero-order hold. |
| FOH | First-order hold. |
| IP | Interaction protocol. |
| | Rectangular window length. |
| | Number of EMT steps per stability time-step. |

Manuscript received November 04, 2013; revised June 18, 2014; accepted December 10, 2014. Date of publication December 22, 2014; date of current version May 20, 2015. This research was financially supported by Agentschap NL, an agency of the Dutch Ministry of Economic Affairs, under the project North Sea Transnational Grid (NSTG). NSTG is a joint project of Delft University of Technology and the Energy Research Centre of the Netherlands. Paper no. TPWRD-01251-2013.

A. A. van der Meer, M. Gibescu, M. A. M. M. van der Meijden, and J. A. Ferreira are with the Department of Electrical Engineering, Mathematics, and Computer Science, Delft University of Technology, Delft 2628 CD, the Netherlands (e-mail: a.a.vanderMeer@tudelft.nl).

W. L. Kling is with the Department of Electrical Engineering, Eindhoven University of Technology, Eindhoven 5612 AZ, the Netherlands.

Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

## I. INTRODUCTION
PRESENTLY, transmission system operators are challenged to integrate increasing numbers of converter-interfaced transmission schemes, including voltage-sourced converter high-voltage dc (VSC-HVDC) [1], [2]. Their beneficial controllability enables interconnection of weak and/or asynchronous grids, eventually in multiterminal dc (MTDC) networks. In Western Europe, for instance, VSC-based MTDC (VSC-MTDC) transmission is under consideration to reinforce grids, interconnect countries, and integrate offshore wind powerplants [3].

Transient stability assessment is key in the corresponding grid integration analysis. The nonlinear and sometimes discontinuous behavior of high-capacity MTDC schemes may impair transient stability. This requires the physical phenomena that contributes to instability (e.g., dc-side EMTs) to be modeled correctly [4]. The time constants of these transients are small, and corresponding dc-side modeling does not fit into common stability-type simulations. In general, stability-type simulations cannot systematically handle combined ac/dc networks [5]. Presently, VSC-MTDC structures can be included in stability-type simulations only by decreasing the step size [6].

On the other hand, the current state of the art in computational power allows modeling of large networks in high detail by (quasi) real-time EMT-type and stability-type simulations. However, EMT-type simulation requires sophisticated line, cable, and equipment data that are necessary to produce a realistic EMT representation of the power system. These are often not available, neither are real-time simulation facilities. Grid studies will thus often be restricted to offline EMT or stability-type simulation on stand-alone computers.

Hybrid simulations offer an alternative as these allow interfacing EMT-type simulations with stability-type simulations. Being first developed in [7] by sequentially executing a stability-type and an EMT-type simulation during faults, hybrid methods were mainly used to study the integration of line-commutated converter (LCC) HVDCs. This simulation concept has been improved over the past decades [8]. In [9], the interface between both types of simulation was generalized to not only contain LCC-HVDC links, but also larger network segments. Later publications showed numerous accuracy improvements [10]–[13], and addressed computational aspects as well as the inclusion into existing tools [14]. However, generalized modeling of VSC-MTDC in stability-type simulations by hybrid methods has not yet been reported in the literature, while it is key