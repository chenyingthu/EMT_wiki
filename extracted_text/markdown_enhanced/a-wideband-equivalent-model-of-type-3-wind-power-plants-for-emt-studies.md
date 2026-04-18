# A Wideband Equivalent Model of Type-3 Wind Power Plants for EMT Studies
Dalia N. Hussein, Member, IEEE, Mahmoud Matar, Senior Member, IEEE, and Reza Iravani, Fellow, IEEE

Manuscript received May 31, 2015; revised January 21, 2016; accepted March 18, 2016. Date of publication April 6, 2016; date of current version September 21, 2016. Paper no. TPWRD-00655-2015.
D. N. Hussein and R. Iravani are with the University of Toronto, Toronto, ON Canada (e-mail: dalia.hussein@ieee.org; iravani@ecf.utoronto.ca).
M. Matar is with the Centre for Applied Power Electronics, the University of Toronto

## Abstract
Abstract—This paper presents the development and validation of an accurate and computationally efficient wideband reduced-order dynamic equivalent model for the Type-3-based wind power plant (WPP). The proposed Type-3 WPP equivalent model reproduces the dynamic behavior of the WPP in response to an electromagnetic transient in the host power system and is composed of two parts: 1) a static frequency-dependent network equivalent model which represents the response of all passive components of the WPP in a wideband frequency range, and 2) a dynamic low-frequency equivalent model that represents the aggregated dynamic model of the doubly-fed asynchronous generator (which is also referred to as doubly-fed induction generator) wind turbine generators, their local controls, and the WPP supervisory control. The proposed model significantly reduces the hardware/software computational burden and the computation time, as compared to the WPP detailed models, without compromising the accuracy of the simulation results. The proposed model is incorporated as a software module in the PSCAD/EMTDC environment and its computational efficiency and accuracy are verified based on comparing the results with those of a detailed model.

## Index Terms
Index Terms—Collector system, doubly-fed asynchronous generator, dynamic equivalent, electromagnetic transients, modeling, type-3 WTG, vector fitting, wind power plants.

## NOMENCLATURE
- **WPP**: Wind power plant.
- **FDNE**: Frequency-dependent network equivalent.
- **DLFE**: Dynamic low-frequency equivalent.
- **DFAG**: Doubly-fed asynchronous generator.
- **WTG**: Wind turbine generator.
- **EMT**: Electromagnetic transient.
- **RSC**: Rotor-side converter.
- **GSC**: Grid-side converter.
- **PCC**: Point of common coupling.
- **PLL**: Phase-locked loop.
- **FRT**: Fault-ride through.
- **DVR**: Dynamic voltage restorer.
- **VSC**: Voltage-sourced converter.
- **VF**: Vector fitting.

## I. INTRODUCTION
With the wide use and increased capacity of the Type-3 wind power plants (WPPs), it is necessary to develop appropriate models to analyze their response to the wide range of phenomena in the power system. For EMT studies, the full-order models based on differential equations of the components of the WPP are used for time-domain simulation which require a small integration time-step. The small integration time-step and the large number of differential equations due to the complex configuration of the doubly-fed asynchronous generator (DFAG)1 and the large number of DFAG units within the WPP result in a significant computational burden and prohibitively prolong the simulation time.

This paper presents a novel wideband dynamic equivalent model that overcomes the aforementioned limitation. The proposed equivalent model is simple yet accurate in modeling the electromagnetic transients (EMTs) behavior of the Type-3 based WPP to EMTs in the host power system, external to the WPP, within a wide frequency range. The salient features of the proposed equivalent model are:
1) It represents the dynamic behavior of the WPP components including: (i) the WPP collector network and passive components, (ii) the WPP supervisory control, and (iii) WTGs and their local controls.
2) It is computationally efficient, i.e., significantly reduces the hardware/software computational burden as compared to the WPP detailed model.
3) It accurately mimics the terminal response of the WPP with respect to the power system EMTs over a wideband of the frequency spectrum.
4) It represents the fault-ride through behavior of the WPP which is a mandatory requirement of the grid codes.
5) It is suitable for real-time simulation based on practically available computational resources.

This paper introduces the proposed equivalent model and its implementation in the time-domain simulation platform (PSCAD/EMTDC) for off-line EMT analysis. The paper also validates the accuracy of the proposed equivalent model with respect to a detailed model of a benchmark system of a Type-3 based WPP.

The remainder of this paper is organized as follows. Section II describes the DFAG unit as the building block of the Type-3 WPP. Section III presents the general structure of the proposed equivalent model. Section IV presents the structure of the DLFE. Sections V–VII present the modules of the DLFE, i.e., the equivalent model of the wind turbines, the WPP supervisory control, and the equivalent model of the generators and their converters systems. The accuracy of the proposed equivalent model