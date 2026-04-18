# MULTIPROCESSOR BASED GENERATOR MODULE FOR A REAL-TIME POWER SYSTEM SIMULATOR

Y. KOKAI, Member, IEEE | I. MATORI, Member, IEEE | J. KAWAKAMI, Member, IEEE  
Hitachi Research Laboratory, Hitachi, Ltd., Japan

**Keywords:** Multiprocessor, Microcomputer, Power system, Generator, Simulator, Parallel processing, EMTP

**Abstract** - A new generator simulation module was developed for an electrical power system simulator. This simulator is on an analog simultaneous base. Therefore the module has to simulate a generator behavior precisely. Furthermore, it is required to be able to use the analog simulator as easily as an off-line simulation program. To meet the requirement, the developed generator module adopts a multiprocessor consisting of microprocessors and an analog three-phase sinusoidal oscillator. Any type of generator can be easily simulated only by changing the program of the microprocessors. However, the accuracy of this module depends on the simulation time interval since this module simulates the behavior of a generator digitally. To make the simulation time interval small enough for the analog simultaneous base, four microprocessors solve differential equations representing the generator dynamics in parallel, and floating point arithmetic is used to avoid numerical errors. A parallel processing method for the multiprocessor to solve the differential equations is described. The accuracy of the generator module is validated by comparisons with the off-line simulation program EMTP (Electro Magnetic Transients Program).

Analog simulators have been used to analyze phenomena in electrical power systems [1], [2]. These analog simulators use many operational amplifiers to solve differential equations which represent behavior of generators included in the power system. These analog simulation modules are superior to conventional miniature generators [3] from viewpoints of accuracy and compactness. However, they still require much time to change and adjust parameters of the modules. This disadvantage is not negligible when large numbers of generators are simulated.

On the other hand, digital computers have been used to analyze generator dynamics by off-line simulations and they have good flexibility. Then, new generator modules, which use a digital microprocessor to simulate the behavior of a generator, have been developed [4][5][6]. As described therein, a precise simulation requires a small simulation time interval and high precision arithmetic method to solve the differential equations.

In this paper, a new technique which uses a multiprocessor to lessen the simulation time interval is described. The multiprocessor calculates next-time-step variables of the differential equations in parallel, and the simulation time interval can be made small enough for the analog simultaneous base. The precision of the newly developed simulation module is evaluated by comparison with the off-line simulation program EMTP [7].

## CONFIGURATION OF SIMULATOR

Figure 1 shows the configuration of the newly developed electrical power system simulator [5][6]. In this simulator, the generator module is composed of a multiprocessor. The other parts of the simulator such as transmission line modules or transformer modules are composed of analog circuits with ohmic loss compensation circuits: Reverse voltage sources, inserted in series with the analog modules, cancel the extra ohmic losses. This simulator is easier to handle than conventional all analog-type simulators because the rated voltage and current are low, i.e. 20 V and 0.2 A. Furthermore, the generator simulation model can be easily modified by only changing the program of the multiprocessor. Main components of this simulator developed at present are 4 generator units, 4 AC transmission line units, 4 DC transmission line units, 12 transformer units, 4 AC/DC converter units, filter units and load units.

The generator modules are connected to transmission line modules through transformer modules and/or circuit breaker modules. Since a generator module consists of microprocessors, the initial condition of the simulator can be easily determined: For example, the host computer calculates the load flow before the simulation to obtain the initial condition, and the microprocessors set up their initial values of the memory in accordance with the data from the host computer. The host computer also controls the operation sequences of the generator modules, circuit breaker modules, measuring units and so on.

**Fig. 1** Configuration of real-time simulator

## GENERATOR