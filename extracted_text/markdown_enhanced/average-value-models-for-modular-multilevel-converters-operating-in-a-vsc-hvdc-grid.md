## The Use of Averaged-Value Model of Modular Multilevel Converter in DC Grid
Jianzhong Xu, Student Member, IEEE, Aniruddha M. Gole, Fellow, IEEE, and Chengyong Zhao, Member, IEEE

**Abstract**—This paper investigates the applicability of averaged-value models (AVMs) for modular multilevel converters (MMCs) operating in a voltage-sourced converter-based-high-voltage dc (VSC-HVDC) grid. The AVM models are benchmarked by comparison with a detailed electromagnetic transient model of the grid, including a fully detailed MMC model. Analysis results show that the AVM is only effective as long as the capacitors are large enough to maintain nearly constant voltage across each MMC submodule. This paper also shows that previously developed MMC averaged models are not able to accurately simulate the transients under dc fault conditions. This paper introduces topology changes to a previously proposed averaged model that results in much improved simulation for such conditions. This paper also shows that the model can be used effectively to study HVDC grids with significant time savings.

**Index Terms**—Averaged-value model (AVM), detailed model (DM), electromagnetic transient (EMT), modular multilevel converter (MMC), submodule (SM).

Manuscript received May 03, 2013; revised February 12, 2014 and May 19, 2014; accepted June 08, 2014. This work was supported in part by the Chinese Scholarship Council (CSC), in part by the Natural Science Foundation of China (51177042), in part by National High Technology Research and Development Program of China (863 Program) (No. 2013AA050105), and in part by the Natural Sciences and Engineering Council (NSERC) of Canada. Paper no. TPWRD-00534-2013.

J. Xu is with the State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University, Beijing 102206, China, and also with the University of Manitoba, Winnipeg, MB R3T 5V6 Canada (e-mail: xujianzhong@ncepu.edu.cn).

A. M. Gole is with the Electrical and Computer Engineering Department, University of Manitoba, Winnipeg, MB R3T 5V6 Canada (e-mail: gole@ee.umanitoba.ca).

C. Zhao is with the State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University, Beijing 102206, China (e-mail: chengyongzhao@ncepu.edu.cn).

Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.
Digital Object Identifier 10.1109/TPWRD.2014.2332557

## I. INTRODUCTION

Recently, voltage-sourced converters (VSC) are being increasingly used in high-voltage direct-current (HVDC) transmission applications. The modular multilevel converter (MMC) is proposed for its improved waveforms, reduced switching losses and easy expansion, etc. [1]–[4]. This topology uses a series of identical capacitor submodules (SMs) that can be switched in and out of a phase in a controlled manner to create a near-sinusoidal waveform as shown in Fig. 1. However, the MMC-HVDC converter uses a large number of submodules. Detailed models (DM) for the MMC that provide completely faithful representations of converter and system characteristics are very complex and computationally challenging for electromagnetic-transient (EMT) programs, given the large number of switching elements, such as insulated-gate bipolar transistors (IGBTs) [5], [6].

**Fig. 1.** Schematic detailed MMC structure.

For accelerating the simulation of MMCs, several approaches are proposed [7]. Each is suitable for a particular operating aspect of the MMC and is described as follows.:
- Highly accurate models based on Thevenin equivalents have been developed [5], [6], which can simulate each level separately and run significantly faster than the conventional DM of the MMC. However, these models are still computationally inefficient for simulating cases with a large number of MMCs, such as HVDC grids.
- The continuous model, which is derived from the converter’s ordinary differential equations, can be used for the controller design [8], [9].
- The averaged-value models (AVM), which consider the fundamental frequency behavior on the ac side, are used for system-level analysis [10], [11].
- An extension to the AVM is to introduce a stepped waveform on the ac side, more representative of the actual converter waveform [12]. This waveform is not derived from the actual individual capacitor voltages, but instead, a simple quantization of a sine wave is carried out, which is based on the control algorithm being used, and superposes staircase steps on the underlying fundamental frequency waveform.

In the AVM, the large-scale dynamic behavior is accurately modeled although the individual capacitor voltages are not calculated. Instead, a single dc-side voltage is calculated. Hence, this type of model is significantly more efficient than models which consider the detailed MMC converter topology and has been proposed for studying the dynamic behavior of large systems, such as dc grids [7], [12], [13].

This paper focuses on the analysis and improvements of the AVM. Although the previously developed AVMs [7], [12], are quite adequate for a large range of VSC studies, as shown in this paper, their performance under dc faults and some other contingencies is not sufficiently accurate. This paper presents an approach to improve the model to remedy this inefficiency. Using EMT simulation, it also generally investigates the applicability of AVMs to different types of contingencies and suggests guidelines on when it can be used and how to use it.

**Fig. 2.** Schematic MMC submodule structure.

## II. AVERAGED-VALUE MMC MODEL

This section discusses the topology of the modular multilevel conv