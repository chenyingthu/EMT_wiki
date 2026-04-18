# 变流器并列运行系统中非特征谐波环流分析及其抑制方法
胡应宏 1，邓春 1，王劲松 1，李雨 1，谢小荣 2，刘少宇 3，刁嘉 4，任佳佳 5
(1．华北电力科学研究院有限责任公司，北京市 西城区 100045；2．清华大学 电机系，北京市 海淀区 100084；3．国网冀北电力有限公司，北京市 西城区 100045；4．国网新源张家口风光储示范电站有限公司，河北省 张家口市 075001；5．哈尔滨工业大学 电气工程及自动化学院，黑龙江省 哈尔滨市 150001）

### Analysis on Non-Characteristic Harmonic Circulating Current in Parallel Inverter System and Its Suppression Measures
HU Yinghong1, DENG Chun1, WANG Jinsong1, LI Yu1, XIE Xiaorong2, LIU Shaoyu3, DIAO Jia4, REN Jiajia5
(1. North China Electric Power Research Institute Co., Ltd., Xicheng District, Beijing 100045, China; 2. Dept. of Electrical Engineering, Tsinghua University, Haidian District, Beijing 100084,China; 3. State Grid Jibei Electric Power Co., Ltd., Xicheng District, Beijing 100045, China; 4. State Grid Xinyuan Zhangjiakou Wind Photovoltaic Storage and Transmission Pilot Power Station Co., Ltd., Zhangjiakou 075001, Hebei Province, China; 5. School of Electrical Engineering & Automation, Haerbin Institute of Technology, Haerbin 150001, Heilongjiang Province, China)

**ABSTRACT:** In Jibei power grid, non-characteristic harmonic circulating current appeared several times and a fault occurred in parallel converters in a 500 kV station. Taking this fault as an example, recorded fault data were analyzed, finding out non-characteristic harmonic circulating current existing in several parallel converters. Analysis of relationship between the problem and parallel converter topology indicated that the problem was liable to appear in cascaded H-bridge multilevel converters. Reappearance of the phenomenon was realized with electromagnetic transient simulation. Simulation results showed validity of the proposed conclusion. Finally, countermeasures were proposed to solve the problem.
**KEY WORDS:** converter; parallel operation; non-characteristic harmonic circulating current; power electronics

**摘要：** 冀北电网中，先后出现了变流器的非特征次谐波环流问题。某 500 kV 变电站变流器并联运行时发生了一次故障，以该故障为例，通过分析变流器故障录波数据，发现多台变流器并列运行容易发生非特征谐波环流。通过分析环流与变流器拓扑结构之间的关系，得出级联 H 桥多电平变流器更容易发生非特征谐波环流；然后，通过电磁暂态仿真复现了故障现象，仿真结果验证了所得结论的正确性。最后，提出了解决非特征次谐波环流的措施。
**关键词：** 变流器；并列运行；非特征次谐波环流；电力电子

DOI：10.13335/j.1000-3673.pst.2016.07.035

基金项目：国家自然科学基金项目(51322701)。
Project Supported by National Natural Science Foundation of China (51322701).

## 0 引言
随着 FACTS 技术、新能源的迅速发展，变流器在电力系统中的并网运行，在数量和容量上都呈现快速增长的态势，但由此也带来了变流器之间环流的问题[1-3]。文献[4]通过并联逆变器具有相同的特性，即相同的输出阻抗、电压幅值与相位来实现功率分配来避免环流问题。文献[5]提出一种基于瞬时电流控制的电流权重分配控制方式，允许不同额定容量逆变器并联运行，通过在每个逆变器控制器中增加一个电路实现按额定容量分配功率。针对变流器的小信号模型建模、并联系统环流抑制以及改进滤波器应用等也有广泛研究[6-11]。针对模块化多电平拓扑结构存在的内部环流，文献[12-14]从不同的角度设计了环流抑制控制器，显著降低了内部环流。已有的谐波环流，主要是针对变流器的特征次谐波的环流，在电气距离上较近，此种类型的环流对象确定，环流频率固定，在治理措施上较易采取措施，已有成功治理此类环流的案例。但针对区域之间的环流，也就是非特征次谐波环流，存在环流对象不确定、环流频率也不固定的问题，在治理措施上，较难采用已有策略，故有必要对多变流器或区域之间的非特征次环流作进一步的研究。

2015 年 5 月 3 日冀北电网某变电站并联运行的变流器其中一台保护动作跳闸。7 月，再次在 2 个风电场之间发现了类似现象，分析其波形发现 2 台变流器在保护动作前电流波形都存在较大的谐波分量，而升压变压器高压侧不存在明显的谐波电流。多个风电场运行时也会产生类似谐波电流环流现象。本文结合本次故障现象，从变流器的拓扑结构、运行机理分析了多台变流器并联运行时产生非特征次谐波环流的原因，指出级联 H 桥结构最容易产生非特征次谐波环流，并进一步分析风电场并列运行时也存在谐波环流的风险。最后，提出了解决多台变流器并联运行时非特征次谐波环流的解决措施。

## 1 非特征次谐波环流案例及原因分析
### 1.1 变流器故障情况
冀北电网某变电站低压侧，2 台 35 kV 变流器(7 号变流器和 8 号变流器)通过一台 35 kV/66 kV 变压器连接到 66 kV 母线，2 台变流器并列运行。2015 年某日，8 号变流器保护动作跳闸。故障发生前，7 号、8 号变流器各承担一半的负载电流，跳闸时刻 8 号变流器输出电流及变流器升压变压器高压侧电流波形如图 1 所示。其中，保护动作前升压变压器 A 相电流及 8 号变流器 A 相电流放大波形如图 1(c)和图 1(d)所示。

*图 1 保护动作时刻相关电流波形*
*Fig. 1 Current waveforms when protection acted*

由图 1 可以看出：跳闸前 66 kV 母线电流中高次谐波含量较少，而 8 号变流器的高次谐波含量较大，由此可以判断，高次谐波在 7 号与 8 号之间环流；在 8 号变流器跳闸后，66 kV 电流谐波含量减小。对发生环流的电流进行快速傅里叶变换(fast fourier transform，FFT)，得到的 66 kV 和 35 kV 电流频谱如图 2 所示，可以看出在 66 kV 在 720 Hz 含量较小，而 8 号在该处含量较大，达到了 60%，可以确定该频率电流在 7 号与 8 号之间发生了环流。7 号与 8 号变流器采用级联 H 桥的拓扑结构，谐波环流会导致阀组内直流侧电压不平衡，从而引起保护动作。

*图 2 保护动作时刻相关电流频谱*
*Fig. 2 Spectrum of output current when protection acted*

某日，河北省张家口市某风电场也发生了类似问题，风机在没有出力的情况下，风场出口电流含有大量非特征次谐波，电流波形如图 3 所示。该现象并非偶发现象，故需要对其进行深一步研究。

*图 3 张家口市某风电场电流波形*
*Fig. 3 Current waveforms of a wind farm in Zhangjiakou*

### 1.2 变流器故障原因分析
以 2 台变流器并列运行为例，来分析产生谐波环流的原因，7 号与 8 号 2 台变流器并列运行示意图如图 4 所示，其中 $S_1$—$S_4$ 为 A 相桥臂的开关器件，$U_{dc}$ 为直流电压，$C$ 为对地电容。

*图 4 2 台变流器并列运行示意图*
*Fig. 4 Schematic of two paralleled converters*

变流器含有丰富的高次谐波，谐波的相位差，由某一区域内多台变流器特性叠加而成，谐波含量减