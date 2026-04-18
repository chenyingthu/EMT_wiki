# Enhanced high-speed electromagnetic transient simulation of MMC-MTdc grid

**Jianzhong Xu**$^{a,\ast}$, **Hui Ding**$^{b}$, **Shengtao Fan**$^{b}$, **Aniruddha M. Gole**$^{b}$, **Chengyong Zhao**$^{a}$

$^{a}$ The State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University, Beijing, China  
$^{b}$ Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, Manitoba, Canada  

$\ast$ Corresponding author. Tel.: +86 01061773744.  
E-mail address: xujianzhong@ncepu.edu.cn (J. Xu).

## Abstract

This paper introduces a very fast electromagnetic transient (EMT) simulation model for the HVdc modular multilevel converter (MMC) that maintains the identity of each switching level, but achieves computation speeds comparable to the much simplified averaged-value models (AVMs) when simulating the multi-terminal dc grid. Speedup is achieved by representing the off state of a MMC sub-module (SM) with ideal zero conductance, and representing the converter with a companion model using the A-stable Backward Euler (BE) method. Often, the user may wish to use the nearest level control (NLC) based voltage balancing algorithm. Then additional speedup can be obtained by using an efficient sorting algorithm which is integrated into the Thévenin equivalent circuit. This achieves a linear speedup (i.e. order $O(N)$) with system size. When compared with a fully detailed simulation (no simplifications), the method shows one to two orders of magnitude speed improvement with earlier reported fast MMC models, with negligible loss in accuracy.

**Keywords:** Thévenin equivalent, Backward Euler (BE) method, Modular multilevel converter (MMC), Nearest level control (NLC), MMC-MTdc grid

## Introduction

Modular multilevel converter (MMC) based high voltage direct current (MMC-HVdc) transmission is gaining in popularity as a dc power transmission option with low losses [1–4]. Compared to the conventional 2 and 3-level voltage source converters (VSC), the MMC topology offers several advantages such as:
- Its modular design permits easier scalability to any desired voltage level simply by using more sub-modules (SM)
- The output voltage waveform has negligible ripple content which eliminates the need for ac filters
- No common dc link capacitor is required
- It has lower switching losses and hence high efficiency

In the future, simulation of large scale multi-terminal dc grid with multiple MMCs will be urgently required especially on the off-line electromagnetic transient (EMT) simulation platforms [5]. Novel MMC models have been proposed that approach the accuracy of the detailed MMC model, but greatly reduce the computational effort. These models can be classified into two categories [6]. In the first category [7,8], each SM retains its individual identity, permitting access to its calculated internal voltages and currents. In the second category [9], all the SMs are combined into a single equivalent, accessing to internal capacitor voltages and currents in individual modules is lost and only the external behaviors are preserved.

The model proposed in this paper is of the first category, in that it maintains the individual identity of SMs and approaches the accuracy of fully detailed simulation. However, as it uses idealized representations of the switches (i.e. IGBTs and diodes) and restructuring of the way in which capacitor balancing is simulated. This accelerates the computation speed by an additional 1–2 orders of magnitude over existing high speed first category models and hence approaches the speeds possible with the second category models.

## Background: Thévenin equivalent MMC model

This section discusses relevant previous work on developing a faster MMC model [8]. Later sections will show how this is extended to construct the even faster models which are the contributions of this paper. The fully detailed MMC model is comprised of three phase legs and each leg consists of two phase arms, as shown in Fig. 1.

Each phase arm includes $N$ identical SMs and a reactor $L_S$. $I_{ARM}$ indicates the arm current. The SM is the basic building block of the converter. The Thévenin equivalents of the $N$ SMs in the bridge arm are then compressed into a single Thévenin equivalent as shown in the dashed area of Fig. 3.

In normal operation, the ON/OFF states of the SMs are determined by the controllers, $V_C$ and $T_{SM}$ in Fig. 3 are the output capacitor voltages and input firing pulses of the SMs. The values of the Thévenin equivalen