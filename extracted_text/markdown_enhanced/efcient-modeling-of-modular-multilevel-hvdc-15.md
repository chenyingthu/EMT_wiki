## Efficient Modeling of Modular Multilevel HVDC Converters (MMC) on Electromagnetic Transient Simulation Programs
**Udana N. Gnanarathna**, Student Member, IEEE, **Aniruddha M. Gole**, Fellow, IEEE, and **Rohitha P. Jayasinghe**, Member, IEEE

**Abstract**—The number of semiconductor switches in a modular multilevel converter (MMC) for HVDC transmission is typically two orders of magnitudes larger than that in a two or three level voltage-sourced converter (VSC). The large number of devices creates a computational challenge for electromagnetic transient simulation programs, as it can significantly increase the simulation time. The paper presents a method based on partitioning the system’s admittance matrix and deriving an efficient time-varying Thévenin’s equivalent for the converter part. The proposed method does not make use of approximate interfaced models, and mathematically, is exactly equivalent to modelling the entire network (converter and external system) as one large network. It is shown to drastically reduce the computational time without sacrificing any accuracy. The paper also presents control algorithms and other modelling aspects. The efficacy of the proposed method is demonstrated by simulating a point-to-point VSC-MMC-based HVDC transmission system.

**Index Terms**—Electromagnetic transients (EMT) simulation, HVDC transmission, modular multilevel converter (MMC), Thévenin’s equivalents, voltage-sourced converter (VSC).

Manuscript received March 25, 2010; revised June 26, 2010; accepted July 17, 2010. Date of publication October 21, 2010; date of current version December 27, 2010. This work was supported by the Industrial Research Chair (IRC) Program of the Natural Sciences and Engineering Research Council (NSERC) of Canada. Paper no. TPWRD-00216-2010.

U. N. Gnanarathna and A. M. Gole are with the Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB R3T 2N2, Canada (e-mail: udana@ee.umanitoba.ca; gole@ee.umanitoba.ca).

R. P. Jayasinghe is with the Manitoba HVDC Research Centre, Winnipeg, MB R3P 1A3, Canada (e-mail: jayas@HVDC.ca).

Digital Object Identifier 10.1109/TPWRD.2010.2060737

## I. INTRODUCTION

In recent years, the voltage and power ratings of voltage-sourced converters (VSCs) have increased significantly, making them potential candidates for use in high power high-voltage direct-current (HVDC) applications [1]–[3]. Unlike the valves of the conventional thyristor-based line commutated converters (LCCs), the VSC’s valves can be turned off with an electronic gate signal. The VSC converter thus has many advantages over the LCC, such as the ability to operate without reactive power support into weak or dead networks. With suitable pulsewidth modulated (PWM) control, its ac filter requirements are also drastically reduced.

Until recently, VSC converters for HVDC applications used a two or three level topology [4] that applied two or three different voltage levels to the ac terminal of the converter. One drawback of this topology is the significant switching power loss resulting from large voltage swings.

One approach to improving the waveform and reducing switching losses is to use multilevel converters. These converters provide an output waveform with a several voltage levels so that each step in voltage waveform is a fraction of the total voltage swing [5]–[8]. The resulting waveform can be designed to be closer to that of a sine-wave. Moreover, the switching frequency of each individual power electronics switch is smaller than that of a two level converter. The voltage step at each level is also smaller. These two factors result in a reduced switching loss.

The recent introduction of a new topology, the modular multilevel converter (MMC) is a major step forward in VSC converter technology for HVDC transmission [9]. Unlike previous multilevel topologies, the MMC uses a stack of identical modules, each providing one step in the resulting multilevel ac waveform. The topology is easily adaptable to any voltage level, as the number of modules can be adjusted in proportion to the selected dc voltage. The resulting waveform has a very small harmonic content and has reduced transient voltage stresses and hence lower high frequency (HF) noise. Also, the topology does not require series connection of several semiconductor switches, which has been a challenge in earlier VSC configurations for HVDC [5].

However, the large number of switching elements in the MMC introduces a challenge for modelling the converter, on electromagnetic transient (EMT) simulation programs. To properly model the switching operation, the admittance matrix which has a size equal to the total number of nodes in the network subsystem, must be inverted (re-triangularized) every time a switch operates. In comparison to a two or three level VSC, the number of nodes (and, hence, matrix size) in the MMC is typically orders of magnitude larger. Also a large number of switching operations are necessary to generate the large number of output waveform levels. Therefore, without an approach such as the one proposed in this paper, it would be practically impossible to simulate HVDC systems containing MMC converters on EMT-type simulation programs.

Simplified averaged models have been proposed for dynamic and steady state behavior of the MMC converter [10]. However, since they do not model every level independently, they are not able to simulate abnormal operation of the converter such as failure of a module’s control system or failure of the module itself. To overcome this drawback, this paper introduces a new

Fig. 3. Level order signal $n(t)$ for an MMC with 12 submodules per multivalve.

Fig. 4. Firing pulse control algorithm of the MMC.

Assuming th