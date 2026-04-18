# 基于 MMC 平均值仿真模型的损耗快速评估方法
孙正东，郝全睿*
(电网智能化调度与控制教育部重点实验室(山东大学)，山东省 济南市 250061)

Fast Loss Evaluation Method Based on MMC Average Simulation Model
SUN Zhengdong, HAO Quanrui*
(Key Laboratory of Power System Intelligent Dispatch and Control of Ministry of Education (Shandong University), Jinan 250061, Shandong Province, China)

**ABSTRACT:** To address the problem that the calculation accuracy and speed of MMC losses are difficult to balance, a fast online evaluation method of losses is proposed. First, based on the determined modulation and capacitor voltage balance strategy, the switching frequency surface is constructed to reflect the switching frequency under any steady-state working condition. Next, the upper limit of switching frequency and the upper limit of switching losses are calculated by using the average value model. Once again, combined with the calculation results and the switching frequency surface, the rapid calculation of the actual losses is realized with high accuracy. Then, considering the impact of losses on the simulation results, the energy absorbed by a controlled voltage source connected in series on the bridge arm is used to characterize the losses. A switching loss injection method based on attenuation function is proposed to avoid injection voltage spikes and improve injection efficiency. Finally, an MMC average simulation model considering loss injection is built in PSCAD to verify the computational efficiency and accuracy of the proposed method.

**KEY WORDS:** modular multilevel converter (MMC); power loss calculation; average value model; loss injection

**摘 要：** 针对模块化多电平换流器(modular multilevel converter，MMC)损耗计算精度和速度难以兼顾的问题，提出一种 MMC 损耗快速在线评估方法。首先，基于确定的调制和电容电压平衡策略，构建开关频率曲面以反映任意稳态工况下的开关频率；其次，利用平均值模型计算开关频率上限和开关损耗功率上限；再次，结合计算结果和开关频率曲面，近似快速计算实际开关损耗，兼顾计算精度和计算效率；然后，考虑到损耗对仿真结果的影响，利用串联在桥臂上的受控电压源吸收的能量表征损耗，同时提出一种基于衰减函数的开关损耗注入方法，避免产生注入电压尖峰并改善注入效果。最后，在 PSCAD 中搭建计及损耗注入的 MMC 平均值仿真模型，验证所提方法的计算效率和准确性。

**关键词：** 模块化多电平换流器；损耗计算；平均值模型；损耗注入

**基金项目：** 国家电网有限公司科技项目(5108-202299261A-1-0-ZB)。
Science and Technology Project of State Grid Corporation of China (5108-202299261A-1-0-ZB).

## 0 引言
模块化多电平换流器(modular multilevel converter，MMC)因其结构易拓展、波形质量高、故障处理能力强而被广泛应用于直流输电领域[1-3]。MMC 损耗是直流输电系统运行过程中损耗的主要组成部分。对于损耗的准确评估关系到散热系统的设计、电力电子器件选型和直流输电系统的经济性、可靠性评估，具有重要的现实意义和研究价值[4-5]。

MMC 损耗主要包括开关器件的导通损耗和开关损耗：导通损耗与器件导通期间流过的电流和导通数目相关，评估难度较小；开关损耗则与器件开断前的电流、电压和开断状态相关。实际工程中，MMC 单个桥臂子模块多达数百个且投切状态受电容电压平衡策略影响，动态特性复杂，开关损耗评估难度大。

现有的 MMC 损耗计算方法大体可分为 2 类。第 1 类方法通过详细电磁暂态仿真模型获得电压、电流波形与开关器件的导通信号，通过对数据二次处理得到损耗的计算结果。文献[6]结合详细模型电磁暂态仿真数据与热电路模型，迭代计算损耗，在计算损耗时考虑了器件结温的影响，并不关注计算效率；文献[7]提出了一种基于结温预估的计算方法，该方法考虑到实际情况中散热器热阻较小，进而对文献[6]所提的计算过程进行简化。

第 2 类方法根据解析公式直接计算损耗[8-11]。文献[8]分段解析计算损耗。其中开关损耗只解析计算由于参考电压变化而产生的部分，对于由电容电压平衡策略和调制方法引起的开关损耗只给出了简易、保守的估算；文献[9]提出了一种基于桥臂电流绝对值和平均值的简化解析计算方法，该方法只针对文献[12]提出的电压平衡策略计算开关损耗，缺乏通用性；文献[10]引入桥臂子模块投入占空比的概念并以此为基础计算损耗，对于开关损耗的计算提出了一种开关频率越高、误差越小的近似计算方法；文献[11]采用数值计算得出电压、电流和开关器件的导通信号，进而计算损耗，但数值计算采用的 MMC 模型过于简单。

在计算精度方面，第 1 类方法通过详细电磁暂态仿真模型获得精确的数据，特别是开关器件的导通信号，因此计算精度较高；第 2 类方法可以准确计算导通损耗，但对于开关损耗，由于其受电容电压平衡策略和调制方式的影响，解析计算困难，计算精度不高。

在计算效率方面，第 1 类方法所需数据要利用能反映 MMC 子模块开关动态的详细电磁暂态模型获得，但 MMC 中子模块数目众多，详细模型仿真速度慢，计算效率低；第 2 类方法建立了损耗的解析表达式，计算效率高。

为了提高损耗尤其是开关损耗计算的精确度并降低计算耗时，文献[13]基于平均值模型，解析表达各子模块电容的充放电过程，并在每个仿真步长更新，一定程度上提高了数据的获取速度，但仍需将仿真数据导入 Matlab 中进行损耗计算，操作较为繁琐；文献[14]利用数值计算近似模拟仿真过程，提高了损耗计算速度，但无法计及控制环节的影响；文献[15]认为在单位功率因数下，传输功率与开关频率线性相关，并通过插值获得二者的对应关系，基于对应关系得到各工况下的子模块轮换数，进而计算开关损耗。该方法仅适用于 MMC 运行在单位功率因数的情况下，具有局限性。

综上所述，现有的 MMC 损耗评估方法很难同时兼顾准确性和计算效率，或者只针对特定情况，缺乏通用性。

此外，现有关于 MMC 损耗的研究主要聚焦在损耗的精确、快速计算方面，鲜有文献考虑到损耗对 MMC 系统仿真结果的影响。文献[16]提出了一种考虑损耗的 IGBT 模型，将 IGBT 模块产生的损耗以受控电压源的形式实时注入到仿真模型中，并将其成功应用到两电平 VSC 上；文献[17]指出，传统 IGBT 的伴随离散电路模型在损耗模拟方面存在不足，并根据 IGBT 的损耗特性，采用响应匹配的方法，分工况对伴随离散电路模型进行改进。现有研究大多通过改进 IGBT 模型使得仿真过程计及损耗的影响，但 MMC 子模块数目众多，若采用改进的 IGBT 模型，仿真速度势必会进一步降低。

为了解决上述问题，本文基于仿真和解析计算的思想，提出一种利用 MMC 平均值模型快速评估损耗的方法，兼顾损耗计算精度和计算效率。同时基于所提计算方法，构建一种计及损耗影响的 MMC 快速仿真模型，将计算出的损耗注入系统中，使仿真模型更能反映实际情况。本文的创新点主要包括：
1）提出一种基于 MMC 平均值模型的损耗快速评估方法：①基于开关损耗的产生原理，构建开关损耗的近似表达式；②基于开关频率数据，二维插值生成开关频率曲面，利用开关频率曲面反映任意稳态工况下的开关频率；③提出半平均值模型的构建方法，利用半平均值模型收集开关频率数据，提高仿真效率。
2）提出一种计及损耗影响的 MMC 损耗注入方法：①用 MMC 桥臂上串联的受控电压源吸收的能量表征损耗；②将开关损耗以衰减的形式注入系统，以避免电压尖峰的产生；③设计新的衰减函数，以获得更好的注入效果。

## 1 MMC 基本拓扑结构及平均值模型
MMC 的基本拓扑结构如图 1 所示，换流器由 6 个桥臂组成，每个桥臂由 N 个结构完全相同的子模块和 1 个电抗器($L_a$)串联而成，上下 2 个桥臂构成 1 个相单元。子模块采用半桥子模块拓扑(half bridge sub-module，HBSM)，HBSM 由 2 个 IGBT($T_1$、$T_2$)、2 个反并联二极管($D_1$、$D_2$)和一个电容器($C$)组成。

MMC 平均值模型如图 2 所示。各相上、下桥臂等效为受控电压源 $u_{px}$ 和 $u_{nx}$($x = a, b, c$)，由等效电容 $C_{eq}$ 和受控电流源组成的外部耦合电路进行控制。与 MMC 详细模型相比，平均值模型用受控电压源、受控电流源和等效电容组成的耦合电路取代了详细模型中大量的开关器件和电容，简化了桥臂结构，在确保能反映 MMC 内部动态特性的同时，

损耗和底层控制损耗等相对较小，在计算损耗时通常将其忽略[18-19]，因此本文只考虑由 IGBT、二极管产生的损耗。

### 2.2 MMC 通态损耗计算
IGBT、二极管的通态损耗功率可以用通态压降与通态电流的乘积来表示：
$$P_{T\_cond} = U_{CE}i_{CE} = (R_{T0}i_{CE} + U_{CE0})i_{CE} \tag{1}$$
$$P_{D\_cond} = U_{D}i_{F} = (R_{D0}i_{F} + U_{D0})i_{F} \tag{2}$$
式中：$P_{T\_cond}$ 为 IGBT 的通态损耗功率；$P_{D\_cond}$ 为二极管的通态损耗功率；$i_{CE}$、$i_{F}$ 分别为流经 IGBT、二极管的电流；$U_{CE0}$、$U_{D0}$ 分别为 IGBT、二极管的