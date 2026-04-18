# Harmonics Interaction Mechanism and Impact on Extinction Angles in Multi-Infeed HVDC Systems
Wei Yao, Senior Member, IEEE, Lingrao Wang, Hongyu Zhou, Student Member, IEEE, Yongxin Xiong, and Jinyu Wen, Member, IEEE

**Abstract**—Harmonics interaction is an important factor in causing concurrent commutation failures (CCF) of multiple converter stations in multi-infeed HVDC (MI-HVDC) systems, but it was not studied sufficiently in existing literature. In this paper, the mechanism analysis and quantitative calculation of harmonic interaction are investigated. Firstly, the generation and interaction process of harmonic during AC fault events in the MI-HVDC systems with single-terminal connection and hierarchical connection on the receiving-end are illustrated, respectively. Then, the common characteristics of harmonic interaction in generalized MI-HVDC systems are concluded. Moreover, to evaluate the impact of harmonic interaction on the commutation process quantitatively, an equivalent circuit model of harmonic transfer in MI-HVDC systems is established. Based on this equivalent model, the harmonic voltage transfer coefficient is deduced, and the extinction angle of inverters considering harmonic interaction in MI-HVDC systems can be calculated. Finally, the calculation accuracy based on equivalent model is verified via the electromagnetic transient simulation of MI-HVDC systems. Simulation results show that harmonic interaction will eventually cause the formation of harmonic sources in each converter station of MI-HVDC systems. These harmonic components will change the extinction angle of remote inverters to increase the risk of CCFs.

**Index Terms**—Commutation failure, extinction angle calculation, harmonics interaction, hierarchical connection, LCC-HVDC, multi-infeed.

## LIST OF SYMBOLS AND ABBREVIATIONS

| Symbol/Abbreviation | Description |
|:---|:---|
| **Abbreviations** | |
| CCF | Concurrent commutation failure. |
| CF | Commutation failure. |
| LCC-HVDC | Line-commutated converter based high-voltage direct current. |
| LCF | Local commutation failure. |
| MI-HVDC | Multi-infeed high-voltage direct current. |
| THD | Total harmonic distortion ratio. |
| VTA | Voltage-time area. |
| **Parameters** | |
| $E_1$ | Equivalent electromotive force of the AC system near bus 1. |
| $E_2$ | Equivalent electromotive force of the AC system near bus 2. |
| **Variables** | |
| $\alpha$ | Firing angle. |
| $\beta$ | Leading firing angle. |
| $\dot{I}_{12h}$ | The $h$-th order harmonic current on AC coupling channel between bus 1 and 2. |
| $\dot{I}_{1h}$ | The $h$-th order harmonic current flows into bus 1. |
| $\dot{I}_{2h}$ | The $h$-th order harmonic current flows into bus 2. |
| $\dot{U}_{1h}$ | The $h$-th order harmonic voltage of bus 1. |
| $\dot{U}_{2h}$ | The $h$-th order harmonic voltage of bus 2. |
| $\gamma$ | Extinction angle. |
| $\gamma'$ | Extinction angle considering the impact of harmonics. |
| $\gamma_{\min}$ | Minimum extinction angle for a normal commutation. |
| $\mu$ | Commutation overlap angle. |
| $\mu'$ | Commutation overlap angle considering the impact of harmonics. |
| $\phi$ | Zero-crossing point shift of commutation voltage caused by harmonics. |
| $I_d$ | DC current in inverters. |
| $Z_{12h}$ | The $h$-th order harmonic impedance of the AC coupling channel between bus 1 and 2. |
| $Z_{1h}$ | The $h$-th order harmonic impedance of the receiving system connected to bus 1. |
| $Z_{2h}$ | The $h$-th order harmonic impedance of the receiving system connected to bus 2. |
| $Z_{\text{Fault}}$ | Fault impedance. |

Manuscript received 10 August 2022; revised 12 November 2022 and 29 January 2023; accepted 5 February 2023. Date of publication 9 February 2023; date of current version 25 July 2023. This work was supported by the National Natural Science Foundation of China under Grant 52022035 Paper no. TPWRD-01197-2022. (Corresponding author: Yongxin Xiong.)

Wei Yao, Hongyu Zhou, Yongxin Xiong, and Jinyu Wen are with the State Key Laboratory of Advanced Electromagnetic Engineering and Technology, School of Electrical and Electronic Engineering, Huazhong University of Science and Technology, Wuhan 430074, China (e-mail: w.yao@hust.edu.cn; ee.henry_zhou@foxmail.com; yxio@energy.aau.dk; jinyu.wen@hust.edu.cn).

Lingrao Wang is with the North China Branch of State Grid Corporation of China, Beijing 100053, China (e-mail: 1956278378@qq.com).

Color versions of one or more figures in this article are available at https://doi.org/10.1109/TPWRD.2023.3243412.
Digital Object Identifier 10.1109/TPWRD.2023.3243412

## I. INTRODUCTION

Commutation failure (CF) is a common fault in the converter station of line-commutated converter based high-voltage direct current (LCC-HVDC) line [1], [2], which is usually caused by the short-circuit fault of the receiving-end AC system [3]. As the continuous construction and operation of LCC-HVDC projects, situations are arising that two or more DC lines with single-terminal or hierarchical connection feeding into one regional AC system [4], and the interaction between AC-DC and DC-DC system becomes more complex [5]. Particularly, it is pointed out in [6] that due to the interaction characteristic

To evaluate the influence of harmonic on the commutation process and provide guidance in practical operation, several