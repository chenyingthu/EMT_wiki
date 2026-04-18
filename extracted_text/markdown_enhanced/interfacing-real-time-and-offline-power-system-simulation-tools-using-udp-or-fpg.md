# Interfacing real-time and offline power system simulation tools using UDP or FPGA systems

Christian Scheibe $^{a,d,*}$, Ananya Kuri $^{a,d}$, Yuyao Feng $^{c}$, Le Zhao $^{c}$, Xuejun Xiong $^{c}$, Piergiovanni La Seta $^{a}$, Xiao Peng Liang $^{b}$, Johannes Knödtel $^{d}$, Philipp Holzinger $^{d}$, Marc Reichenbach $^{d}$, Gert Mehlmann $^{d}$

$^{a}$ Power Technologies International Siemens AG, Erlangen, Germany  
$^{b}$ Power Technologies International Siemens AG, Shanghai, China  
$^{c}$ Shanghai Electric Power Research Institute, Shanghai, China  
$^{d}$ Friedrich-Alexander-Universität Erlangen-Nürnberg, Erlangen, Germany  

**Keywords:** Co-Simulation, Transient stability analysis, Electromagnetic transients, Real-time simulation, Offline simulation

**Abstract:** This contribution proposes a coupling interface between the real-time simulation system RTDS Novacor and the Power System Simulation Software PSS/E for electromagnetic transient (EMT) and phasor (RMS) hybrid simulations to enable a performant connection between the domains. For the coupling interface, two implementations with different characteristics in latency and hardware requirements are presented. Firstly, an Ethernet (UDP) based connection and secondly a fiber-based connection using the Aurora protocol. The first approach is purely software based, while the second one requires additional hardware. The technical implementation of the interfaces is explained in detail. The functionality of the interfaces is verified on the basis of an EMT-RMS simulation in a small overhead line test system.

## 1. Introduction

The field of power grid simulation evolved from a very complex and time-consuming problem to a flexible and performant task thanks to the transition from analog to digital simulators. However, for years the simulators were not performant enough to calculate big networks in real-time. This changed thanks to the advancements in hardware and software development in the recent years.

Alongside, the power system experiences the challenging transition from systems dominated by large machines to a converter-dominated grid. Hence, time constants implied by the inertia of the machines do play less of a role than previously [1]. This, however, puts strain on the requirements of power system simulation. Transient Stability (TS, RMS) type simulations require time constants to be low enough to not interfere with the phasor based nature of their algorithm. That means a typical investigation for RMS simulations is well below 10 Hz in all considered frequencies which excludes many aspects of converter-based transients. These require investigation using electromagnetic transient based simulations (EMT) [2,3].

EMT-type simulations require a lot more capable computation power to show the same per-time simulation performance as RMS simulators do. This originates from their algorithm being created to investigate different problems. RMS usually uses (complex) phasor based simulation methods to solve large portions of a grid using time steps in the range of multiple milliseconds. EMT-type simulations are usually utilized for a detailed investigation of fast and very fast transient phenomena and their impact on equipment. Also, their time step directly influences the precision of the results. Usual time steps range from 50 μs and lower depending on the frequency of the transients involved [4].

As EMT simulations spread more widely into the field formerly covered by phasor based transient stability investigations and real-time simulation methods demand EMT modeling for most applications, a challenge is to be faced to overcome the gap between the domains. A solution might be the field of Co-Simulation of power systems. The coupling of RMS- and EMT-simulations has the potential to overcome the limits of monolithic simulations and add the strengths of both domains [5]. The proposed interface, therefore, is a candidate for this field, further expanding the range of capable interfaces.

Previous works included the interfacing and coupling of EMT-RMS Co-Simulation based on offline programs such as PSCAD, PSSE, Matlab or PowerFactory [6]. Also, real-time simulators were coupled previously in [7–9]. This publication aims to provide insights into the development and the feasibility of an interface bridging the real-time and offline domains. Therefore, the development process is shown in the following sections. Finally, using a small overhead line test grid, simulations are performed to show the feasibility of the interface.

* Corresponding author at: Friedrich-Alexander-Universität Erlangen-Nürnberg, Erlangen, Germany.  
E-mail address: christian.scheibe@siemens.com (C. Scheibe).

## 2. Simulation interface concept

Coupling real-time and offline simulation domains involves bridging the gap between two completely different concepts. Generally, a real-time simulator acts based on the principle of hard real-time described by Kopetz et al. in [10]. That means, that any one of the given time steps must be executed in a period smaller than the one simulated in the device. An overflow occurs if this is not the case. Simulators handle overflows differently depending on the principles they are intended for. While some applications only run using these hard real-time criteria, others may accept some overflows. This is called firm real-time if the result of a simulation including exceeded deadlines can be rejected.

Fig. 1. EMT-RMS-Conversion concept.

The results are per-phase complex phasors. These phasors can now be transformed into the positive sequence domain of the RMS simulator. The symmetric component equations sum the phasor’s real