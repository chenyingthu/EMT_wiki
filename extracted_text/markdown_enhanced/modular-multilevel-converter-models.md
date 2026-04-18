# Modular Multilevel Converter Models for Electromagnetic Transients
**Hani Saad**, Member, IEEE, **Sébastien Dennetière**, Member, IEEE, **Jean Mahseredjian**, Fellow, IEEE, **Philippe Delarue**, Member, IEEE, **Xavier Guillaud**, Member, IEEE, **Jaime Peralta**, Member, IEEE, and **Samuel Nguefeu**, Member, IEEE

**Abstract**—Modular multilevel converters (MMCs) may contain numerous insulated-gate bipolar transistors. The modeling of such converters for electromagnetic transient-type (EMT-type) simulations is complex. Detailed models used in MMC-HVDC simulations may require very large computing times. Simplified and averaged models have been proposed in the past to overcome this problem. In this paper, existing averaged and simplified models are improved in order to increase their range of applications. The models are compared and analyzed for different transient events on an MMC-HVDC system.

**Index Terms**—Average-value model (AVM), EMT-type programs, HVDC transmission, modular multilevel converter (MMC), switching function, voltage-source converter (VSC).

*Manuscript received April 07, 2013; revised September 11, 2013; accepted October 08, 2013. Paper no. TPWRD-00396-2013.*  
H. Saad, J. Mahseredjian, and J. Peralta are with the École Polytechnique de Montréal, Montréal, QC H3C 3A7 Canada (e-mail: hani.saad@polymtl.ca; jean.mahseredjian@polymtl.ca; jaime.peralta@polymtl.ca).  
S. Dennetière and S. Nguefeu are with Réseau de Transport d’Electricité (RTE), Paris-La Défense, Paris 92068, France (e-mail: sebastien.dennetiere@rte-france.com; samuel.nguefeu@rte-france.com).  
P. Delarue and X. Guillaud are with L2EP, École Centrale de Lille, Lille 59651, France (e-mail: Philippe.Delarue@univ-lille1.fr; xavier.guillaud@ec-lille.fr).  
Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.  
Digital Object Identifier 10.1109/TPWRD.2013.2285633

## I. INTRODUCTION
THE inclusion of high-voltage direct current (HVDC) transmission in electric power grids is expanding rapidly. Two HVDC technologies are prevailing: 1) line-commutated converters (LCC) based on thyristor semiconductor devices and 2) voltage-source converter (VSC) type using insulated-gate bipolar transistors (IGBTs). VSC–HVDC systems present several advantages over the traditional LCC–HVDC links [1], such as independent control of active and reactive powers, ability to supply weak grids or passive networks, and black start capability.

The recent modular multilevel converter (MMC) topology [2] offers significant benefits compared to previous VSC technologies [3]. With a sufficient number of MMC levels per phase, the filter requirements can be eliminated. Moreover, switching frequency and transient peak voltages on IGBT devices are lower in MMCs, which reduces converter losses [4]. Scalability to higher voltages is easily achieved and reliability is improved by increasing the number of submodules (SMs) per phase [5].

The large number of IGBTs in MMCs complicates the simulations in electromagnetic transient-type (EMT-type) simulation tools. Detailed MMC–HVDC models must include the representation of thousands of IGBTs and small numerical integration time steps are required to accurately represent fast and multiple simultaneous switching events [5]. The excessive computational burden introduced by such models requires researching more efficient models. A current trend is based on simplified and averaged value models capable of delivering sufficient accuracy [6] in dynamic simulations.

Average value models (AVMs) approximate system dynamics by neglecting switching details [7], [8]. They require significantly less computational resources and can use larger integration time steps leading to much faster computations [9]. In [10], an AVM model for a 401-level MMC-HVDC system has been presented. A phasor-domain-based model of the MMC was presented in [11].

This paper introduces a new model based on the switching function principle applied to each MMC arm. An improved AVM model is also presented.

References [12] and [13] are based on circuit reduction achieved by the replacement of IGBTs by ON/OFF resistors in the SMs. The mathematical formulation and computational performance of this approach have been already demonstrated [14]. However, the blocked state of submodules has not been previously addressed. This paper presents an iterative solution for correcting this limitation within a more efficient overall model implementation.

This paper also presents comparisons between different types of MMC models for deriving their advantages and limitations according to simulation needs.

## II. MMC TOPOLOGY
Fig. 1 shows the three-phase configuration of the MMC topology. The MMC model developed here is based on the preliminary MMC–HVDC system design for the planned interconnection between France and Spain 400-kV networks in 2013 [10]. The MMC is comprised of           SMs per arm which results in a line-to-neutral voltage waveform of           levels [15]. The inductor         is added on each arm to limit arm-current harmonics and fault currents. Each SM is a half-bridge converter as depicted in Fig. 2 and includes mainly a capacitor    and two IGBTs with antiparallel diodes (S1 and S2).

## III. SUBMODULE OPERATION
Since the IGBT device is controllable through gate signals and   , the SM can have three different states. In the ON state: