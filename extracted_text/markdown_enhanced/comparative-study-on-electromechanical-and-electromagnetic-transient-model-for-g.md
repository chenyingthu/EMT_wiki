## 并网光伏发电系统的通用性机电暂态模型及其与电磁暂态模型的对比分析

孙 浩 1，张 曼 2，陈志刚 1，刘志文 1，谢小荣 2，姜齐荣 2
（1.中国能源建设集团广东省电力设计研究院，广东 广州 510600；
2.电力系统国家重点实验室, 清华大学电机系，北京 100084）

**摘要：**针对并网光伏发电系统电磁暂态模型复杂、计算速度慢的问题，提出了一种并网光伏发电系统的通用性机电暂态模型。该模型不包含电器元件及高频开关器件，由纯粹的数学计算完成，模型简单、计算速度快。在 PSCAD/EMTDC 中对该机电暂态模型进行了仿真，得到的结果与电磁暂态模型的仿真结果吻合，且仿真时间大大减少，从而验证了该机电暂态模型的正确性及有效性。该通用性机电暂态模型为大规模并网光伏电站的仿真建模等提供了模型参考，具有实用价值。
**关键词：**光伏发电；并网；机电暂态模型；电磁暂态模型；仿真对比

**Comparative study on electromechanical and electromagnetic transient model for grid-connected photovoltaic power system**
SUN Hao 1, ZHANG Man2, CHEN Zhi-gang 1, LIU Zhi-wen 1, XIE Xiao-rong 2, JIANG Qi-rong2
(1. Guangdong Electric Power Design Institute, China Energy Engineering Group Co., Ltd, Guangzhou 510600, China;
2. State Key Lab of Power Systems Department of Electrical Engineering, Tsinghua University, Beijing 100084, China)

**Abstract:** The computing speed of electromagnetic transient model for grid-connected photovoltaic power system is very slow because of its complexity. To solve this problem, a general electromechanical transient model for grid-connected photovoltaic power system is proposed, in which there are not electrical components and high frequency switching device, and it only consists of pure mathematical calculations, is simple and has fast calculation speed. By comparing the simulation results of this electromechanical transient model with electromagnetic transient model in PSCAD/EMTDC, we found that the simulation time is reduced greatly and the results are agreeable basically, which verifies the correctness and validity of the electromechanical transient model. The electromechanical transient model provides reference model for simulation and modeling of large scale grid-connected photovoltaic power station and is of great practical value.
This work is supported by National Natural Science Foundation of China (No. 51322701).
**Key words:** photovoltaic power; grid-connected; electromagnetic transient model; electromechanical transient model; simulation comparison

中图分类号： TM76；TM743                    文献标识码：A                  文章编号： 1674-3415(2014)03-0128-06

## 0 引言
随着新能源、智能电网和微电网技术的发展，并网光伏发电系统已经取得广泛的应用，并具有广阔的发展前景[1-2]。在含光伏发电系统的电网动态分析中需要采用兼具精度和效率的暂态模型，在既往研究中，光伏发电系统模型通常采用两类模型，一类是潮流模型[3]，即将其建模成简单的功率源，不考虑其动态过程，该模型仅适用于潮流分析，而不能用于暂态分析；另一类是基于特定的光伏发电系统建立对应的电路或电磁模型[4-5]，严格体现光伏发电系统中具体的最大功率点跟踪（MPPT）控制算法和逆变器电路及其控制逻辑，这类模型非常详实，理论上能满足电网机电暂态分析要求，但也存在诸多问题，如：1）由于光伏发电系统的内部结构和控制方法因厂家不同而具体各异，导致其电路或电磁模型的通用性差，如果对不同厂家、型号的光伏发电系统均如此建模，则工作量极大，不现实；2）电路或电磁模型涉及各厂家专有的设备内部参数，往往难以取得相关的模型参数；3）电路或电磁模型复杂度高，为保证精度，计算步长往往设置得非常低，从而严重制约计算的速度。而且，电力系统机电暂态仿真往往只需要光伏发电系统的有效值电压/电流输出，并不需要其三相动态过程。加上目前大电网分析计算多采用商业或工程化仿真软件，亟需一种相对通用的光伏发电系统模型，以提高仿真分析的自动化水平和扩大计算规模。综上所述，亟需分析已有各类光伏发电系统的共性特征，并针对电力系统机电暂态仿真的需求，形成一种通用性的建模方法。

目前关于并网光伏发电系统的研究多集中在单台电磁暂态模型的建模仿真，而在实际的光伏发电站中，有多台光伏阵列同时工作。在研究光伏电站模型或者光伏电站并网给电网带来的影响时，如果对多台光伏发电系统的电磁暂态模型同时进行仿真，则仿真速度将会很慢。因此，研究并网光伏发电系统的通用性机电暂态模型对于提高仿真速度来说是非常有意义的。

本文首先简要介绍了并网光伏发电系统的构成，然后提出了一种并网光伏发电系统的通用性机电暂态模型，并对其内部结构进行了详细介绍，最后通过 PSCAD/EMTDC 对该机电暂态模型进行仿真，并与电磁暂态模型仿真的结果进行对比，验证了该机电暂态模型的正确性及有效性。

## 1 并网光伏发电系统构成
目前常见的并网光伏发电系统有单级式并网光伏发电系统、两级式并网光伏发电系统和多级式并网光伏发电系统，如图 1 所示。单级式并网光伏发电系统中，光伏阵列直接与 DC/AC 逆变器相连，逆变器将光伏阵列输出的直流电能转换为满足电网需求的交流电，逆变器不仅需要变换电能，还需要实现 MPPT。两级式并网光伏发电系统中，光伏阵列输出的电能经过 DC/DC 电路、 DC/AC 逆变器并网，DC/DC 电路实现 MPPT 及升压作用，逆变器实现电能变换。多级式并网光伏发电系统中，光伏阵列输出的电能首先经过 DC/AC 逆变器成高频交流电，然后经过高频变压器升压到目标电压等级，再经过高频整流器将电能转换成高压直流电，最后经过 DC/AC 逆变器将电能转换成符合电网要求的交流电。

不论采取何种拓扑结构，MPPT 及并网 DC/AC 逆变器都是必不可少的部分，其控制直接关系到并网系统接入电网的电能质量。MPPT 的控制方法多种多样[6]，如固定电压法、电导增量法、扰动观察法等。DC/AC 并网逆变器多采用电压型逆变器，主要的控制方式有电压控制和电流控制，电压控制是将系统作为受控电压源处理，要求其输出电压与电网电压同频同相；电流源控制是将系统作为受控电流源，要求其输出的电流与电网电压同频同相。目前的并网光伏发电系统中，DC/AC 逆变器多采用图 1 所示的电压源输入、电流源输出的连接方式。

图 1 常见光伏发电系统结构
Fig. 1 Structure of common photovoltaic system

对于电压源输入、电流源输出的 DC/AC 并网逆变器，其控制方法有多种[7-8]。用的比较多的是基于旋转坐标系的 PQ 解耦控制，主要包括外环功率控制和内环电流控制。本文后面算例中使用的即为 PQ 解耦控制。

## 2 光伏发电系统机电暂态模型
由前述知，并网光伏发电系统可能是单级的、双级或多级的，MPPT 算法多种多样，逆变器及其控制方法也千差万别，为了规避这些内部的差别，而更多地关注其机电暂态特性，本文提出一种通用性机电暂态模型，如图 2 所示，S、T 分别为光伏阵列所处环境的光照强度和温度，Vpvm 为光伏阵列最大功率点处的电压，其由光伏阵列的特性决定，并作为 MPPT 模块的输入参考电压，MPPT 的输出 Vpvm1 及直流链接的输出电压 VD、光伏阵列输出功率 Ppv1 作为 DC 变换的输入，共同决定光伏阵列的端电压，即 Vpv1。直流链接的作用是通过平衡直流侧功率 Ppv2 和交流侧功率 PDe 来维持直流母线电压为恒定值，为后级逆变器提供直流电压，逆变器的控制分为外环和内环控制，具体控制原理将在后文介绍。

图 2 机电暂态模型信号传递关系图
Fig. 2 Signal relationship of electromechanical transient model

数为 T，则 MPPT 模型可以表示为
$$V_{pvm1} = \frac{e^{-\gamma s}}{1 + Ts} V_{pvm} + \Delta V_{pvm} \quad (7)$$
其中，$\Delta V_{pvm}$ 为跟踪误差。

### 2.3 DC/DC 变换器模型
以 Boost 电路为例，DC/DC 变换器主要起到了升压及功率变换的作用，DC/DC 变换的输入输出量之间的关系分为两种情况。
于单级式并网光伏发电系统，为
$$\begin{cases} P_{pv2} = f_1(P_{pv1}) = P_{pv1} \\ V_{pv1} = f_2(V_D, V_{pvm1}) = V_D \end{cases} \quad (8)$$
对于双级式和多级式并网光伏发电系统，为
$$\begin{cases} P_{pv2} = f_1(P_{pv1}) = P_{pv1}\eta \end{cases} \quad (9)$$