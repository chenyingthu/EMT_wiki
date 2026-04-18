## Modeling Synchronous Voltage Source Converters in Transmission System Planning Studies
D. N. Kosterev
Oregon State University

**Abstract:** A Voltage Source Converter (VSC) can be beneficial to power utilities in many ways [1, 2, 3, 4]. To evaluate the VSC performance in potential applications, the device has to be represented appropriately in planning studies. This paper addresses VSC modeling for EMTP, powerflow, and transient stability studies. First, the VSC operating principles are overviewed, and the device model for EMTP studies is presented. The ratings of VSC components are discussed, and the device operating characteristics are derived based on these ratings. A powerflow model is presented and various control modes are proposed. A detailed stability model is developed, and its step-by-step initialization procedure is described. A simplified stability model is also derived under stated assumptions. Finally, validation studies are performed to demonstrate performance of developed stability models and to compare it with EMTP simulations.

**Keywords:** transmission system planning, reactive power compensation, EMTP, transient stability.

## 1. Introduction
Acquiring new rights of way is becoming more difficult due to environmental and economical reasons. New transmission lines are expensive and it takes considerable time to permit and to build them. Power transfer capability of a transmission system is constrained by line design limitations (such as its thermal capacity) and system stability requirements (such as voltage stability, transient stability, sub-synchronous resonance, etc.). Typically, transmission lines are loaded below their thermal capacities due to the system stability requirements. Reducing stability constraints will result in better utilization of the existing transmission facilities and mitigate building new lines. Controllable network devices can improve the system stability [1, 2, 3, 9], and in many cases are economically advantageous over new transmission lines.

Voltage stability is one of major constraints limiting power transfer capability in developed systems [2, 4]. Various reactive power compensators can be employed to enhance voltage stability. A Synchronous Voltage Source Converter is one of them [1, 2, 3, 4]. To evaluate the VSC applicability to present and future projects, the device has to be represented appropriately in planning studies. Unlike conventional shunt compensators, VSCs are complex dynamical systems and require comprehensive representation in the time-domain studies. This paper addresses issues of VSC modeling for EMTP, powerflow, and transient stability studies.

To achieve full utilization of the VSC control capabilities, the device should be equipped with real-time controllers [2, 4, 7]. Developed models should provide an interface for such user-defined controls.

## 2. Operating Principles
A block-diagram of a Voltage Source Converter is depicted in Figure 1. The DC voltage source supplies voltage to a power converter array. The DC batteries and DC capacitors can be used as DC voltage sources. By controlling current flow at the DC bus, the DC source can either supply or absorb active power, and the power converter can operate as an inverter or a rectifier respectively. The converter array typically consists of several power conversion modules (PCMs). PCMs include basic six-pulse converters, in which gate-turn-off (GTO) thyristors are used as power switches. Typically, several thyristors are connected in series to form a valve. The converter output voltages are combined electro-magnetically by means of a coupling transformer array to form a multi-pulse "sinusoidal" voltage.

```
Dc VOLTAGE        POWER           TRANSFORMER
SOURCE            CONVERTER       ARRAY
                  ARRAY
```
*Figure 1. Voltage Source Converter block diagram*

The coupling transformers use harmonic neutralization techniques [3, 5, 10], so that only $kP \pm 1$ ($k = 1, 2, \dots$) harmonics are present in $P$-pulse waveform, $P = 6N$, where $N$ is a number of PCMs. Both, power converter and coupling transformer arrays can be implemented by a variety of circuits. Although the designs can be different, the converter output voltage waveforms and DC currents are essentially the same.

The VSC can be connected either in shunt or in series with the transmission line. This paper considers only shunt-connected devices. These are Battery Energy Storage (BES)-device [5] and Static Condenser (Statcon) [1, 6]. A Statcon uses only capacitors as a DC voltage source, while a BES-device has also DC batteries.

### 2.1 Converter Control
There are two levels of the converter controls: internal and external. The internal control provides gating signals to the thyristor valves in order to form a desired converter voltage waveform. The external controller determines parameters of the synthesized converter voltage (magnitude and phase of the fundamental component) required to meet specified performance objectives. These parameters are translated into thyristor firing angles and passed to the internal controls. Controllability of the synthesized voltage magnitude and phase is discussed below.

### Voltage Magnitude Controllability
The fundamental component of the converter voltage magnitude $V_{CV}$ (line-to-line value) is proportional to the DC-bus voltage $E_{DC}$. Thus, the converter voltage magnitude can be controlled by the DC source voltage. This method is effective only for a Statcon, because battery voltage changes very slowly. The rate of change of the DC voltage depends on the DC capacitor size, the smaller capacitance, the faster response is, however at the expense of larger vol