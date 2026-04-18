**特高压自耦变压器的建模和电磁暂态仿真**
曾麟钧，林湘宁，黄景光，郑峰，李智
(三峡大学电气信息学院，湖北省 宜昌市 443002)

**Modeling and Electromagnetic Transient Simulation of UHV Autotransformer**
ZENG Lin-jun, LIN Xiang-ning, HUANG Jing-guang, ZHENG Feng, LI Zhi
(The College of Electrical Engineering and Information Technology, China Three Gorges University, Yichang 443002, Hubei Province, China)

**ABSTRACT:** To correctly apply transformer differential protection in the environment of ultra high voltage (UHV), it is necessary to model the UHV power transformer reasonably and carry out the corresponding electro-magnetic transient simulations. According to the equivalent circuit of three winding autotransformer, we set up the three winding autotransformer model by means of unified magnetic equivalent circuit (UMEC) transformer model provided by EMTDC software. The parameters of UHV transformer are converted to those of the UMEC model. By this way, the UHV transformer model is built. Under the UHV environment, the excitation and internal fault current of UHV power transformer are simulated, and the simulated data are utilized to investigate the operation reliability of the well-applied differential protection combined with second order harmonic blocking. Simulation results show that the second order harmonic ratios of inrush currents through three phases of the UHV power transformer are all below 10%. In this case, the mal-operation of the differential protection cannot be avoided if the strategy that one phase current is applied to restrain three phases is adopted and the threshold of second order harmonic restraint ratio is 15%~20%. Besides, in some light fault conditions, the second harmonic ratio of the fault current is relatively high in the beginning of fault inception, leading to the short time delay of operation of protection.

**KEY WORDS:** UHV power transformer; autotransformer; EMTDC; magnetic inrush; internal fault current; harmonic

**摘要：** 为了在特高压环境下正确应用变压器差动保护，需要对特高压变压器进行合理建模，并进行相应的电磁暂态仿真。根据三绕组自耦变压器星型等值电路的原理，用电磁暂态仿真软件 EMTDC 中的统一电磁等效电路 (unified magnetic equivalent circuit，UMEC)普通三绕组变压器模型来模拟 1 000 MVA/1 050 kV 三绕组自耦变压器，将特高压变压器参数折算成 UMEC 模型参数，形成特高压变压器模型。在特高压环境下，分别进行励磁涌流和故障电流仿真，并用于考察应用得最为广泛的 2 次谐波闭锁的变压器差动保护的动作可靠性。分析表明：当合闸角和剩磁满足一定条件时，特高压变压器三相励磁涌流的 2 次谐波含量都会在 10%以下，即使采用一相制动三相的 2 次谐波闭锁策略，如果 2 次谐波门槛值维持在 15%~20%，也不能避免差动保护误动；另外，在某些轻微故障的情况下，故障初期故障电流的 2 次谐波含量成分较高，会使保护动作短暂延迟。

**关键词：** 特高压变压器；自耦变压器；EMTDC；励磁涌流；内部故障电流；谐波

基金项目：国家自然科学基金项目(50777024)。
Project Supported by National Natural Science Foundation of China (50777024)．

## 0 引言
区分励磁涌流与内部故障电流是变压器差动保护所面临的难题，特高压变压器保护也不例外。对特高压变压器进行合理建模，并在仿真软件中再现实际的电磁暂态过程，是正确应用变压器差动保护的必要前提。

特高压变压器大多为自耦变压器，而目前大多数仿真软件中均为集成自耦变压器模型。在进行暂态仿真时，简单的做法是用普通变压器模型直接代替自耦变压器。这种处理方法仅考虑磁的耦合作用，而忽略了自耦变压器一、二次绕组之间电的联系。文献[1]提出的自耦变压器模型，选用磁通链作为状态变量，并考虑了铁心的非线性特性，物理概念清晰，但该模型计算过于复杂。文献[2]应用受控源原理建模，并用修正后的阻尼梯形算法导出自耦变压器综合友模模型，计算速度和精度都得以提高，但模型忽略了励磁阻抗非线性。另外，如果将特高压自耦变压器的电磁暂态过程放在特高压电磁环境中，特别是包含具有分布参数的特高压输电线路的系统中进行考察，结果将更加真实可信。

PSCAD/EMTDC 是一种广泛应用于电力系统各个领域的仿真软件，具有强大的电磁暂态仿真功能，只是其中也没有包含三绕组自耦变压器的模型。本文根据三绕组自耦变压器的三端星形等值电路，利用 EMTDC 中的统一电磁等效电路(unified magnetic equivalent circuit，UMEC)普通变压器模型，建立了 1 000 MVA/1 050 kV 自耦变压器模型及内部故障模型，该模型能考虑特高压变压器的特殊性以及铁心的非线性。基于以上模型，在特高压环境下进行了变压器空载合闸和匝间、匝地、引出线短路等情况的仿真，并进行了波形分析，指出了 2 次谐波制动变压器差动保护应用于特高压变压器时需要注意的问题。

## 1 特高压变压器建模
### 1.1 特高压变压器基本结构
自耦变压器具有成本低、运行效率高和励磁功率低等优点，广泛应用于 220 kV 及其以上的电网中。由于特高压变压器单相容量已达 1 000 MVA，具有容量大和绝缘水平高的特点，使变压器重量与体积必然很大。出于运输等方面的考虑，采用单相结构成为必然。中国生产的特高压变压器即为单相自耦变压器[3]。

特高压变压器设有第 3 绕组，即低压绕组。低压绕组不带负载，以角型方式联结，流通 3 次谐波电流，再经低压电抗器接地。

出于绝缘和制造工艺等方面的要求，采用中性点无励磁调压，设外置式调压补偿的变压器。主变压器和调压补偿变压器通过管路母线连接。这种绕组联结的特殊性，使特高压变压器绕组间的短路阻抗比普通变压器要大得多。

由于本文关心的是变压器各侧电流，在建立模型时，将主变压器及调压补偿变压器等效为一个三绕组自耦变压器。

的电压、电流分别为 $\dot{U}_Q$ 和 $\dot{I}_Q$；第 3 绕组的电压、电流分别为 $\dot{U}_T'$ 和 $\dot{I}_T'$。

与三绕组普通变压器的方程式的推导相同，当忽略励磁电流时，可以得出
$$
\begin{cases}
\dot{U}_S' - \dot{U}_Q' = \dot{I}_S' Z_S' + \dot{I}_Q' Z_Q \\
\dot{U}_S' - \dot{U}_T' = \dot{I}_S' Z_S' + \dot{I}_T' Z_T'
\end{cases} \tag{1}
$$
式中 $Z_S'$、$Z_Q$、$Z_T'$ 分别为串联绕组折算到公共绕组的漏阻抗、公共绕组的漏阻抗、低压绕组折算到公共绕组的漏阻抗。由式(1)可画出其对应的三端星型等值电路，如图 1 所示。

```
          S
          |
         ZS′
          |
    ZQ----+----ZT′
          |
          Q         T
```
**图 1 三端星型等值电路**  
*Fig. 1 Three-terminal Y-type equivalent circuit*

等值电路中的参数也可以用三绕组普通变压器的实验方法测得，因此，可以三绕组普通变压器为基础来模拟三绕组自耦变压器。

### 1.3 特高压变压器仿真模型
### 1.3.1 正常运行时的模型
EMTDC 中并无三绕组自耦变压器模型。根据 1.2 节的分析，考虑到自耦变压器中串联绕组、公共绕组的“电”的联系，将 UMEC 三绕组变压器模型中的 2 个绕组首尾相接，形成高压和中压绕组，来模拟特高压变压器模型。

如图 2 所示，第 1~3 绕组分别模拟低压绕组、串联绕组和公共绕组。两模型等效的前提是保证相对应的绕组的漏阻抗值相等。需要注意的是，特高压变压器的相关参数要折算到第 1 绕组，即低压绕组。

```
高压端              UMEC
                  第 2 绕组
                  第 1 绕组      低压端
中压端 第 3 绕组
```