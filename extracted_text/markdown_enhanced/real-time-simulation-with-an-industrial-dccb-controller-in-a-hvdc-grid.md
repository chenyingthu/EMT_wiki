# Real-time simulation with an industrial DCCB controller in a HVDC grid

P. Rault^a,⁎, S. Dennetière^a, H. Saad^a, M. Yazdani^b, C. Wikström^b, N. Johannesson^b

^a Réseau de Transport d'Electricité (RTE), Lyon, France  
^b Hitachi-ABB power grids, Ludvika, Sweden

⁎ Corresponding author.  
E-mail address: pierre.rault@rte-france.com (P. Rault).

**Keywords:** HVDC, MMC, DCCBs, HIL

**Abstract**  
DC breakers and their associated control are seen as important lever for the DC grid expansion. In complement to dynamic studies, as intermediate step towards on-site implementation, factory tests using real control and protection hardware enable to fine tune control sequences, to check the software implementation and then test the coordination and interaction between different devices connected to the same grid.  
This article presents a hardware-in-the-loop setup for testing industrial DCCB controllers and their interoperability with converter controllers. A hybrid DCCB model suitable for real-time simulation has been developed and then validated against offline model. Industrial DCCB controller functions are described. A set-up of three-terminal DC grid with physical controllers for one MMC converter station and 12 DCCBs is described. The results of two application cases including cable energization and fault clearance are presented and discussed.

## 1. Introduction
DC networks are seen as an important solution for increasing renewable generation in the energy mix as they increase the capacity of the transmission system and its flexibility. Currently, point to point HVDC links are already common for both onshore and offshore projects, converter stations are provided by one single manufacturer and in case of DC fault the whole system trips. However, looking forward, dealing with DC grid to exchange more energy, two additional aspects have to be considered: the VSC-HVDC multivendor interoperability and handling DC faults [1]. Clearing a DC fault in a DC grid is challenging, since the faulty part must be isolated in a few milliseconds to avoid the whole DC grid collapsing. Due to recent innovation in DC circuit breaker (DCCB) technology, Hybrid HVDC Breaker (HHB) makes isolation of faulty parts in a DC grid possible, since this device is able to interrupt DC current in less than 5 ms with acceptable losses [2]. This kind of DCCB is a good trade-off between loss efficiency which are too large with pure semiconductor based DCCB and speed which are too slow with pure mechanical DCCB. Other similar technologies which are currently at the prototype stage, like VARC circuit breaker [3], should also be evaluated in the near future.

A fast circuit breaking device is an important aspect of the fault handling in DC grids but will be useless without efficient detection of faults with DC protections. In fact, the protection system, is utmost importance since it must selectively detect the eventual fault and then send triggering signal to relevant DCCBs within few milliseconds. In literature a lot of attention were put in one of these aspects, for instance, Wang et al. [4] discusses the fault current limiting, Augustin et al. [5] exhibits the pole to ground DC fault characteristics in monopolar and bipolar configurations, while Descloux et al. [6] and Johannesson et al. [7] investigate different fault detection strategies.

In addition, most of the studies dealing with simulation of DC grid protection raise the attention on the DC system modelling, some general recommendations are provided in [8], some other discussed DC breaker modelling [9]. Descloux [10] justifies the need of frequency dependent cable model to get relevant results.

Some relevant works which include the full chain of protection system using offline simulation are available in literature [11]. In real HVDC projects, such EMT offline studies constitute the first step, to perform control tuning and preliminary studies of the upcoming project. After such preliminary study, the second step involves real time simulation using Hardware In the Loop (HIL) setup with the physical control cubicles. The aim of such HIL simulation are:
- to validate and/or correct initial control tuning
- to validate the full process chain of the control and protection cubicles (i.e. acquisition, processing time, coordination of actions from independent controllers etc.)
- to cover a wider range of dynamic performance that are not possible to perform in EMT offline study: either due to the long computation time either due to the simplification made in the control system of the offline model

The aim of this work is to perform a HIL simulation of a three-terminal DC grid including DCCBs, which is an essential stage in an innovative industrial context. Physical Control and Protection (C&P) cubicles for ABB DCCBs and converter station are used in this project. High Voltage equipment data and topology come from actual manufacturer design. C&P hardware and software, for converter station and DCCB, have been provided by the manufacturer and correspond to their latest technology. This set-up was first developed to test VSC-HVDC multivendor interoperability in the European founded project called Best Paths DEMO#2 [12]. More information about this multivendor HIL set-up and manufacturers equipment description can be found in [13]. To the authors’ best knowledge this final setup is one of the most detailed platforms ever that has been setup to analyse industrial interoperability issues and coordination.

Fig. 2. Detailed valve model in EMTP-RV for offline simulation.