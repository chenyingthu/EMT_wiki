# 直流机电暂态与电磁暂态模型在低频振荡分析中的比较

**王天钰，李龙源，和 鹏，王晓茹**
（西南交通大学电气工程学院，四川 成都 610031）

**摘要：**对交直流混合运行系统进行低频振荡分析时，直流系统通常采用机电暂态仿真模型。介绍了直流系统的机电暂态和电磁暂态两种仿真模型，在电力系统全数字仿真装置（ADPSS）平台上建立了 EPRI36 系统和某实际电网系统的机电暂态模型和机电-电磁暂态混合仿真模型，分别用于低频振荡分析。采用基于总体最小二乘-旋转不变技术的信号参数估计（TLS-ESPRIT）算法，分析故障后的振荡功率信号。提取低频振荡主导振荡频率、阻尼比等信息进行模态分析，并对分别利用两种仿真模型进行仿真得到的低频振荡分析的结果进行比较。结果表明，直流线路分别采取两种仿真模型时，仿真结果较为吻合，低频振荡分析的结果基本相同，机电暂态模型具有较高的实用价值。
**关键词：**交直流系统；低频振荡分析；机电暂态模型；电磁暂态模型；ADPSS；混合仿真

**Comparison between electromechanical transient model and electromagnetic transient model of DC in low frequency oscillation analysis**
**WANG Tian-yu, LI Long-yuan, HE Peng, WANG Xiao-ru**
(School of Electrical Engineering, Southwest Jiaotong University, Chengdu 610031, China)

**Abstract:** For AC and DC operating system Low Frequency Oscillation (LFO) Analysis, DC system usually adopts electromechanical transient model. This paper introduces the DC electromechanical transient and electromagnetic transient model, and then establishes the electromechanical transient model and the electromechanical-electromagnetic transient hybrid simulation model on the Advanced Digital Power System Simulator (ADPSS) platform for the LFO analysis respectively. Adopting the total least squares method-rotational invariance techniques of signal parameter estimation (TLS-ESPRIT) algorithm, the oscillation power after failure is analyzed. After extracting the LFO dominant oscillation frequency and damping ratio for making the modal analysis, it compares the LFO analysis results of the two simulation models. Results of the EPRI36 standard test system and a practical power system simulation show that the simulation results of two simulation models are tallied, besides, the LFO analysis result is basically the same. The electromechanical transient model has a high practical value.
**Key words:** AC and DC systems; low frequency oscillation analysis; electromechanical transient model; electromagnetic transient model; ADPSS; hybrid simulation

中图分类号： TM731 | 文献标识码：A | 文章编号： 1674-3415(2013)19-0017-07

## 0 引言

低频振荡（LFO）问题已经成为制约电网传输能力的主要因素之一[1]。在对交直流混合运行的电力系统[2]进行低频振荡分析时，直流系统通常采用机电暂态仿真模型，目前已有文献[3-4]比较过当直流系统分别采用机电恒功率模型和机电准稳态模型进行仿真时系统低频振荡分析的结果。机电暂态模型对直流换流器做了稳态等值简化处理，在交流系统不对称故障、换相失败时其仿真精度有限；而电磁暂态仿真模型建立了换流器、线路以及控制系统等的详细模型，理论上对系统发生不对称故障时直流系统的暂态特性分析更为精确。文献[5]在直流系统换相失败等三个方面对两种模型进行仿真研究并比较结果。但目前在低频振荡分析领域，还没有文献对机电暂态模型和电磁暂态模型的仿真结果进行比较。

中国电力科学研究院研发的电力系统全数字仿真装置（ADPSS）不仅具有机电-电磁暂态混合仿真的功能，而且可以对 10 000 节点规模的交直流混合运行系统进行机电-电磁暂态混合实时仿真。本文在 ADPSS 平台上，建立了 EPRI36 标准测试系统和某实际电网系统的机电暂态仿真模型和混合仿真模型，分别用于低频振荡分析。选取故障后的功率信号为分析对象，利用基于总体最小二乘法-旋转不变技术的信号参数估计（TLS-ESPRIT）算法[6]，分别提取采用机电暂态模型[7-8]和机电-电磁暂态混合模型[9]仿真时系统低频振荡主导振荡模式、阻尼比等信息，进行模态分析，并比较二者计算结果，为在低频振荡分析时直流系统仿真模型的选取提供依据。

## 1 直流输电系统建模

### 1.1 直流准稳态模型

高压直流（HVDC）输电准稳态模型是指，在直流系统稳定运行时，以换流站交流母线电压为换相电压，以变压器漏抗作为换相电抗，忽略交流系统对直流侧影响的仿真模型[4]。稳态运行时每个 12 脉动换流器模型表示如图 1。

**图 1 准稳态电路换流器模型**
*Fig. 1 Quasi steady state model of converter*

稳态运行方程式可表示为式（1）：
$$
\begin{cases}
V_{d0} = \dfrac{3\sqrt{2}}{\pi} B T V \\
V_d = V_{d0} \cos \alpha - \dfrac{3}{\pi} X_c I_d B \\
P = V_d I_d \\
Q = P \tan \phi \\
\phi = \arccos \dfrac{V_d}{V_{d0}} = \theta_V - \theta_I \\
I = \dfrac{6}{\pi} B T I_d
\end{cases} \tag{1}
$$
式中：$V$ 为换流母线电压；$T$ 为换流变压器变比；$X_c$ 为换相电抗；$B$ 为同一极换流器串联个数；$P$、$Q$、$I$ 分别为换流母线注入换流器的有功、无功和电流；$V_d$、$I_d$ 分别为直流电压、电流。

对直流系统各部分进行线性化[3-4]，可以形成直流系统的准稳态等值电路，如图 2 所示。文献[8]对换流变压器基本参数进行了推导。文献[9]以不同强度交流系统为对象，对这种模型的有效性进行了验证。

**图 2 准稳态等值电路**
*Fig. 2 Equivalent circuit of quasi steady state model*

图中：$V_i$、$V_j$ 为换流母线电压；$L_d$、$R_d$、$C_d$ 分别为直流线路等效电感、电阻、对地电容。

### 1.2 直流电磁暂态仿真模型

电磁暂态仿真过程是对电路中电阻电感及电容元件的微分方程进行求解的过程，可以实现对电力电子器件的详细模拟。在仿真中，直流系统的模拟主要是对换流器、直流线路、直流控制及保护设备的模型进行模拟。

（1）换流器数学模型

换流器模型[10-11]是由晶闸管等元件组成的电子电路。在 ADPSS 电磁暂态计算平台上，6 脉冲换流器采用三相暂态模型模拟，每个阀臂由一晶闸管元件和 R-C 缓冲电路并联而成，晶闸管的导通用阻值很小的电阻模拟，其等值模型如图 3(a)所示。将电容的微分方程化为差分方程后，可以得到用等值电阻 $R_{RC}$ 和等值电流源 $I_{RC}(t - \Delta t)$ 表示的暂态等值计算电路，如图 3(b)所示，其中等值电流源是与历史时刻相关的项[12]。

**图 3 换流阀臂的电磁暂态模型**
*Fig. 3 Electromagnetic transient model of converter valve arm*

对电感电阻元件用同样的方法进行等值，可以得到图 4。

**图 4 电阻电感元件电磁暂态模型**
*Fig. 4 Electromagnetic transient model of R and L*

12 脉冲换流器由两个 6 脉冲换流器串联而成，其各自相连的换流变压器分别采用 Y-Y-0 接、Y-∆-1 接法，如图 5 所示。将所有的换流阀臂由图 3(b)表示，所有的电阻电感电路由图 4(b)表示，列出节点导纳矩阵 $Y_{con}$ 和节点注入电流矩阵 $I$，根据节点电压方程公式 $YU=I$，阀的连接关系及阀的导通关断状态，最终可得到换流器的节点电压方程为
$$
Y_{con} U_{con} = H_{con} + n_1 P_{con1} i_{\alpha1} + \frac{1}{3} n_2 P_{con2} i_{\alpha2} + P_{con\beta} i_{\beta} \tag{2}
$$
式中：$n_1$、$n_2$ 分别为图中 Y-Y-0 接、Y-∆-1 接换流变压器变比；$Y_{con}$、$U_{con}$ 分别为 12 脉冲换流器的节点导纳矩阵、节点电压向量；$H_{con}$ 为与某节点相连的暂态等值电流源向量；$i_{\alpha1}=[ i_{\alpha1a}, i_{\alpha1b}, i_{\alpha1c} ]^T$ 为 Y-Y-0 接换流变压器一次侧三相电流；$i_{\alpha2}=[ i_{\alpha2a}, i_{\alpha2b}, i_{\alpha2c} ]^T$ 为 Y-∆-1 接换流变压器一次侧三相电流；$i_{\beta}$ 为注入该换流器的直流电流；$P_{con1}$、$P_{con2}$ 分别为反映该换流器

**图 6 直流线路 T 型等值电路**
*Fig. 6 T-type equivale*