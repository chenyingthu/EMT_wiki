# Design of hybrid series converter valve considering device switching characteristics

Ruiqi Zhan, Yunxia Ye, Jiahang Xia, Chengyong Zhao*
*The State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University, Beijing, China*

\* Corresponding author. E-mail address: chengyongzhao2@163.com (C. Zhao).

**Keywords:** HVDC, Commutation failure, Hybrid series converter valve, Turn-off time control, Dynamic voltage equalization design

**Abstract:** The line commutated converter high voltage direct current (LCC-HVDC) has a weak ability to resist commutation failure (CF). In order to solve this problem, we studied a hybrid series converter valve (HSCV) composed of thyristors and the fully controllable switches in series. The working states of HSCV were designed, besides, the operating principle of HSCV was analyzed. Considering the characteristics of the device, HSCV’s turn-off time control was provided. The voltage and current stress in the turn-off process of HSCV was analyzed, dynamic voltage equalization parameters of HSCV were designed also. The simulation results of SABER and PSCAD/EMTDC showed that HSCV increases the time for the thyristor to recover its forward blocking capability, thereby preventing the valve from re-conducting and switching phases. That is why HSCV-HVDC has stronger commutation failure suppression than LCC-HVDC and ELCC-HVDC. In addition, the parameter design principle proposed in this paper can reasonably design the dynamic voltage balancing branch, effectively solve the overvoltage problem of the turn-off tube, and meet the device parameter requirements.

## 1. Introduction

Renewable Energy technology is currently developing rapidly around the world. The State Grid Corporation of China has built many high voltage direct current transmission projects to solve the problem of reverse distribution of energy and load in China. Line commutated converter high voltage direct current (LCC-HVDC) is an important part of HVDC transmission projects [1]. Its converter valve is composed of thyristors, and the semi-controlled characteristic of thyristor determines that the converter itself does not have the ability to actively turn off. Therefore, after the fault occurs, the converter is prone to commutation failure (CF), causing power shocks and voltage fluctuations and affecting the stable operation of the system [2–3].

It is necessary to resist CF. At present, additional installation of AC voltage regulators [4–6], commutation failure prevention control [7–9], and new converter topology [10–13] are the main methods to improve immunity against CF. Among them, the new converter topology is a hot research direction because of its direct effect on the suppression of commutation failure. Thyristor-based full-bridge module (TFBM) is connected in series to the converter valve arm to mitigate the CF of LCC-HVDC [10]. However, the semi-controlled characteristic of thyristor forces TFBM to have a span that is not conducive to the commutation. What’s more, the use of thyristors strengthens the control flexibility of capacitor commutated converter (CCC) and reduces the CF risk of LCC-HVDC [11–12]. But similarly, the semi-controlled characteristic of thyristor leads to a very complicated circuit structure. Xue and Ni both proposed a hybrid configuration using dynamic series capacitor insertion. This hybrid configuration is simple in structure and can increase the effective commutation voltage, thereby preventing commutation failure [13–14]. The hybrid configuration scheme provides a new idea for the converter topology research, but the research ignores the differences of different devices to design control strategies. Moreover, the lack of corresponding electrical stress analysis makes its guiding significance for engineering unclear. Hence, in order to demonstrate the engineering reference value of the new topology of the converter valve with simple structure and controllable resistance to commutation failure, it is necessary to consider the device switching characteristics to analyze the control coordination and electrical stress. This problem needs to be resolved by analyzing the coupling change relationship of turn-off time of different switching devices.

Recently, many studies on the turn-off time of the valve thyristor have been reported [15–18]. These studies provide references for analyzing the coupling change relationship of the turn-off time of different switching devices. Shammas et al. [15] demonstrated the relationship between the reverse recovery process and external circuit

## Nomenclature

| Symbol | Description |
| :--- | :--- |
| $\mu$ | commutation overlap angle |
| $\gamma$ | arc extinguishing angle |
| $t_{rr}$ | reverse recovery time |
| $t_{gr}$ | gate recovery time |
| $I_{dc}$ | DC current |
| $\omega$ |  |
| $i_c$ | the current of the IGBT |
| $t_f$ | the turn-off time of the IGBT |
| $i_s$ | the current of the dynamic voltage equalization branch of the IGBT |
| $u_C$ | the voltage of the dynamic balancing capacitor |
| $u_R$ | the voltage of the dynamic balancing resistor |
| $i_F$ | the turn-off current value of the IGBT |