# A new topology for current limiting HVDC circuit breaker

**Shuai Li**, Jiyuan Zhang, Jianzhong Xu, Chengyong Zhao  
*The State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University, Beijing, China*

## Keywords
HVDC circuit breakers, Current limiters, Over-voltage protection, Stability

## Abstract
With the high voltage direct current Transmission (HVDC) booming, HVDC grid has received wide attention. As an essential component in HVDC grid, high voltage direct current circuit breakers (DCCB) requires urgent and intensive study. A novel topology for current limiting DCCB (CL-DCCB) is proposed in this paper. The topology consists of several units which are divided into two classes: main circuit breaker (MCB) and branch circuit breakers (BCBs). The number of inductor branches can be flexibly selected to enhance the current limiting effect. The CL-DCCB can start current limiting operation when a suspected fault occurs. When the detection circuit reveals what has happened, it can be determined whether to implement breaking operation or recover to normal state. This mode allows longer fault detection time and circuit breaker operation delay while guaranteeing the fault current within the maximum limit of the system. Finally, Simulation model and experiment prototype are built to study the design criteria for CL-DCCB. It is observed that the maximum detection delay can be extended to 12 ms. Moreover, the current limiting effect can be enhanced when the number of inductor branches or the inductance of each branch is increased.

<sup>☆</sup> This work was supported in part by National Natural Science Foundation of China (51777072) and in part by Fundamental Research Funds for the Central Universities (2017XS018). The authors are with the State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University (NCEPU).  
<sup>⁎</sup> Corresponding author at: 2 Beinong Road, Huilongguan Town, Changping District, Beijing, China. E-mail address: lishuaiwork@foxmail.com (S. Li).

## 1. Introduction

DC grid is a new type of power transmission system, which is obtained from voltage-source converter (VSC) type HVDC [1,2]. It interconnects multiple AC and DC systems with higher reliability due to its redundant DC lines. DC grid technology is especially suitable for large-scale wind power or photovoltaic and other new energy integration, which is the future direction of DC transmission technology [3,4]. China is building a demonstration project named as Zhangbei DC grid. The project is designed for the collection and transportation of large-scale wind power, photovoltaic, energy storage, and other energy forms. The rated voltage of this DC grid is ±500 kV, with approximately 648 km overhead transmission lines [5].

Due to the low damping of DC system and no zero crossing point of the DC current, it is difficult to isolate the DC fault. Especially in large-scale power grid. Take a scenario of DC grid shown in Fig. 1 as an example, the DC grid is divided into two parts by a DC-DC converter. The upper part C1-C4 is a cyclic and radiation mixed connection structure. The lower part is a point-to-point DC system. Obviously, the normal operation of the whole network will be hardest hit if the fault cannot be cleared in time.

One way to solve this problem is to use novel MMC sub-modules (SMs) with DC fault clearance capability [6,7]. Once short circuit fault occurs, the fault current discharge path can be blocked by blocking MMC SMs. Finally, the mechanical switch can be used to interrupt the fault line, thus, the system fault characteristics can be greatly improved. However, the novel SMs will inevitably increase the cost and power loss of MMC. More importantly, all the converter station must be blocked under fault condition. Thus, the loss of power transmission capacity will affect the normal and stable operation of the whole grid. Taking Fig. 1 as an example, if a short-circuit fault occurs in the transmission line among converter station C1-C4, all these converter station should be blocked, then mechanical switch can be used to isolate faulty lines when the fault current drops to zero. The outage of those converter stations means a quick stop of electricity transmission in the whole grid, which is unacceptable.

The DC-DC converter can also be configured in the grid to isolate the DC fault, and the high frequency transformer of the DC-DC converter is undoubtedly a good isolating device. Through the control of the DC-DC, the fault can be isolated quickly. However, the configuration of DC-DC in the grid is limited with the issue of cost and power loss, thus the protection area of the grid is limited [8,9].

SCFCL is featured with good current limiting effects and fast response, but the technology is not yet mature, and expensive [10,11].

The feasibility of future DC grids depends largely on their capabilities to withstand DC faults. In order to overcome the problems mentioned above, a novel DCCB topology with current limiting capabilities is proposed.