# 基于机电暂态–电磁暂态混合仿真的高压线路保护装置试验研究
唐宝锋，苑峰，范辉，杨潇
（河北省电力研究院 电网数字仿真实验室，河北省 石家庄市 050021）

Experimental Research on High-Voltage Transmission Line Protection Device Based on Electromechanical-Electromagnetic Transient Hybrid Simulation
TANG Baofeng, YUAN Feng, FAN Hui, YANG Xiao
(Power System Digital Simulation Laboratory, Hebei Electric Power Research Institute, Shijiazhuang 050021, Hebei Province, China)

**ABSTRACT:** A scheme to examine acting characteristics of high-voltage transmission line protection devices by electromechanical-electromagnetic transient hybrid simulation is proposed. The hybrid simulation can fully play the superiorities of electromechanical transient simulation and electromagnetic transient simulation, so not only the precision of system simulation can be improved, but also the workload brought by system equivalence can be reduced. Comparing the data from the faults actually occurred in power system and that from simulation results, it is proved that the proposed method can reflect actual operational conditions of power system. A hybrid simulation model, in which the parameters of actual domestic power system are adopted, is built, and a lot of simulation tests of protection devices for a certain high-voltage transmission line in China are performed, and simulation results show that it is available to use hybrid simulation to the examination of transmission line protection devices.

**KEY WORDS:** advanced digital power system simulator (ADPSS); hybrid simulation; line protection; online data interface

**摘要：** 提出了一种利用机电暂态与电磁暂态混合仿真方法开展高压线路保护装置动作特性检验的方案。机电暂态与电磁暂态的混合仿真，可以充分发挥二者的优势，既提高了系统仿真的精度，又可以减少由于系统等值带来的工作量。通过系统实际发生故障与仿真系统数据的对比，证明了该方法能够反映系统的实际运行工况；利用实际电网参数搭建了混合仿真模型，对国内某一高压线路保护装置进行了大量的仿真试验，验证了混合仿真用于检验线路保护装置的有效性。

**关键词：** 电力系统全数字仿真装置；混合仿真；线路保护；在线数据接口

基金项目：国家电网公司科技项目(SGKJ[2007]911)。

## 0 引言
实时数字仿真器(real-time digital simulator，RTDS)是国际最通用的继电保护产品性能检测工具，在国内也有广泛的应用[1-5]，但有些不足之处，如：RTDS 只能开展电磁暂态仿真而且仿真规模很小，必须对电网进行等值；设备昂贵、操作复杂、扩容性差。因此，较难得到普遍应用。

本文针对使用 RTDS 进行保护装置性能检测的不足，提出一种新型的高压线路保护装置检测方案。该方案利用中国电科院开发的电力系统全数字仿真装置(advanced digital power system simulator，ADPSS)的先进机电暂态–电磁暂态并行仿真技术，将大电网运行背景用机电暂态仿真而将需要研究的局部电网在电磁暂态下建模，不必对系统进行等值，从而避免了电磁仿真对系统规模的限制。此外，本文通过开发在线数据接口，可使调度能量管理系统(energy management system，EMS)自动将电网实时数据断面传送至仿真系统[6]，实现基于实际网络拓扑结构的大电网运行方式下的继电保护装置试验研究。

## 1 机电暂态–电磁暂态混合仿真
机电暂态与电磁暂态仿真有着本质的区别，电磁暂态仿真建模详细，考虑非线性、分布参数等特征，基于三相瞬时值方式，步长为$\mu\text{s}$级；机电暂态仿真简化建模，采用集总参数，系统由基波相量模式描述，步长为$\text{ms}$级。单纯的机电暂态仿真不能准确、详细地模拟系统局部快速变化过程，而电磁暂态仿真受速度和规模的限制无法对全系统进行仿真[7]，因此，机电暂态–电磁暂态混合仿真技术是互为取长补短的一个有效方案。实现电力系统电磁暂态与机电暂态混合仿真，一方面扩大了电磁暂态仿真规模，另一方面也为电磁暂态网络的仿真分析提供了必要的系统背景。采用机电暂态–电磁暂态混合仿真进行工程分析及应用，既能避免由于电磁暂态仿真规模的限制而产生的进行系统等值的工作量，还能大大提高系统分析研究的准确度[8-15]。

## 2 实际电网故障与仿真数据的对比
为了验证实际情况与仿真的一致性，特将电网某一实际故障进行故障重现，并将仿真与实际的故障数据进行了对比。故障情况：2009-06-01 T13:10，500 kV 北清 I 线发生 C 相接地故障，线路两侧保护均快速动作，跳开 C 相开关，重合闸不成功，开关三跳。

仿真系统中，在北清 I 线设置 C 相永久性接地短路故障，过渡电阻为 $7\ \Omega$。石北侧二次电流仿真波形及故障录波如图 1 所示。从图 1 可以看出，仿真数据与故障录波数据基本一致，因此，可以认为仿真平台能够反应电网实际运行工况。

*(图 1 坐标轴数据：电流/A: 8.000 (仿真故障电流), 4.000, 0.000 (实际故障电流))*

### 3.2 系统参数
保护安装于东骅 I 线，F1—F3 分别代表线路出口、中点及末端故障点，F4—F7 分别为相邻线路及保护装置背后母线的故障点。

发电机参数为：$S_n=600+j290\ \text{MVA}$，$X_d=3.233$，$X_d'=0.3975$，$X_d''=0.3075$，$X_q=3.15$，$X_q'=0.5925$，$X_q''=0.3015$，机端电压 $U=20\ \text{kV}$。变压器参数为：变比为 $525\ \text{kV}/20\ \text{kV}$，Ynd11 接线，$U_k=13.8\%$，$I_0=0.091\%$，$P_0=109.8\ \text{kW}$，$P_k=439.2\ \text{kW}$。线路参数为：$R_1=0.000493\ \text{pu}$，$X_1=0.005936\ \text{pu}$，$C_1/2=0.295376\ \text{pu}$，$R_0=0.001479\ \text{pu}$，$X_0=0.017808\ \text{pu}$，$C_0/2=0.1794\ \text{pu}$，线路长度 $L=54.55\ \text{km}$；电流互感器(current transformer，CT)变比为 $2500/1$；电压互感器(potential transformer，PT)变比为 $5000/1$。

### 3.3 性能检验
根据《电力系统继电保护产品动模试验》的相关要求，利用机电–电磁暂态混合仿真方案对国内某型高压线路保护装置进行了几百次的仿真试验，充分验证装置的性能。

该保护装置在发生区内外金属性接地故障、系统频率偏移、系统稳定性破坏情况、CT 断线、PT 断线、空载投长线路时，动作特性良好，但在某些故障类型，如经过渡电阻接地、转换性故障及 CT 饱和，保护动作特性变坏或者误动，以下进行详细说明。

1）转换性故障。
模拟系统发生区内转区外、区外转区内故障时，保护可能会误动作。图 3 为系统发生区外转区