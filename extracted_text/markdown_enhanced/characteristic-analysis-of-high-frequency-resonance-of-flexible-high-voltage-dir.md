## 柔性直流输电系统高频振荡特性分析及抑制策略研究
郭贤珊 1，刘泽洪 1，李云丰 2*，卢亚军 3
(1．国家电网有限公司，北京市 西城区 100031；2．国网湖南省电力有限公司经济技术研究院，湖南省 长沙市 410004；3．国网经济技术研究院有限公司，北京市 昌平区 102200)

## Characteristic Analysis of High-frequency Resonance of Flexible High Voltage Direct Current and Research on Its Damping Control Strategy
GUO Xianshan1, LIU Zehong1, LI Yunfeng2*, LU Yajun3
(1. State Grid Corporation of China, Xicheng District, Beijing 100031, China; 2. State Grid Hunan Electric Power Company Limited Economic & Technical Research Institute, Changsha 410004, Hunan Province, China; 3. State Grid Economic and Technological Research Institute CO. LTD., Changping District, Beijing 102200, China)

**ABSTRACT:** Time delay is the inherent feature of MMC-based HVDC transmission system which makes the output impedance of MMC presented “negative resistance and inductance” characteristics in high frequency ranges. Those characteristics may easily cause high-frequency resonant instability interacting with the capacitance feature of long AC lines. Firstly, the equivalent model of MMC and AC lines were derived. Secondly, the impedance model of MMC under dq coordinate was established considering the factors such as internal dynamic processes of MMC, PLL, circulating current suppression controller, time delay, etc. Thirdly, the effect of corresponding factors on impedance matrix in high-frequency ranges as well as resonant characteristics was analyzed. Fourthly, a damping control strategy was proposed to suppress the high-frequency resonant instability. Parameters of damping controller to keep the system stable operation have been designed carefully using the simplified MMC model. Finally, the validity of the proposed strategy and the correctness of the parameters designing were proofed by the electromagnetic transient simulation model.

**KEY WORDS:** flexible high voltage direct current; modular multilevel convert (MMC); impedance model; high-frequency resonance; damping control; voltage feed forward

**摘要：** 柔性直流输电系统的链路延时是其固有特性，使柔直高频阻抗呈现“负电阻电感”特性，可能与长交流线路的分布电容相互作用导致高频振荡失稳现象发生。文章首先建立柔直系统和交流线路等效数学模型。其次，考虑模块化多电平换流器(modular multilevel convert，MMC)内部动态特性、锁相环、环流抑制控制器、延时等因素在内，建立 MMC 在 dq 坐标系下的阻抗模型，分析相关环节对柔直高频阻抗特性的影响及高频振荡特性。再次，提出高频振荡阻尼控制策略，采用 MMC 简化模型分析阻尼控制器参数对阻抗高频特性的影响，并设计保持系统稳定的控制器参数。最后，利用电磁暂态仿真模型验证所提策略的有效性及参数设计的正确性。

**关键词：** 柔性直流输电；模块化多电平换流器；阻抗模型；高频振荡；阻尼控制；电压前馈

## 0 引言
基于模块化多电平换流器(modular multilevel converter，MMC)的柔性直流输电技术(flexible high voltage direct current，HVDC)凭借在增压扩容、低频谐波、可控特性、弱电网联网及孤岛供电等方面的优越特性得到了快速发展[1-3]。伴随着柔性直流工程单个换流站电压和容量等级从最初 $\pm 30\text{kV}/18\text{MW}$ 到 $\pm 800\text{kV}/5000\text{MW}$ 的提升，换流站已经从 35kV 配网接入转变为 500kV 主网接入，其安全稳定运行对交流大电网的影响逐渐增大[4-6]。

随着柔直基础理论深入研究及工程应用出现的问题，科研人员逐步揭示了柔直控制系统相关参数，例如锁相环(phase-locked loop，PLL)、内外环、环流抑制，对柔直阻抗特性及稳定性的影响[7-10]，然而上述影响的研究主要集中在低频段，对柔直高频段的影响研究少有文献报道。柔直工程在新能源接入、城市供电、大电网互联等应用方面已经出现了次同步振荡、中频振荡和高频振荡现象[11-15]。次同步振荡的频率范围大致在 10~30Hz 范围；中频振荡频率在 250~350Hz；而高频振荡的频率主要出现在 550~2kHz 范围，例如厦门工程直流侧 550Hz 振荡、鲁西工程 1270Hz 以及渝鄂联网工程的 700Hz 和 1.8kHz 附近的高频振荡。高频振荡发生之后，若在一段时间内不能及时消除，柔直换流站将执行闭锁逻辑保护相关设备安全[13]。由此产生的功率缺额或盈余对交流主网将产生严重的冲击，因此，研究柔直高频振荡及其抑制方案对提高工程安全性和可靠性具有重大促进作用。

当前研究电压源换流器的方法主要基于小信号法，例如状态空间[16-17]和阻抗法[18-21]。大量文献针对装置并网稳定性问题，建立了单/三相两电平换流器的阻抗模型，并将延时所导致的相位滞后特性考虑在内，提出了多种解决方案[22-25]。这些方案之所以能解决小功率装置并网稳定性问题，主要有 2 个方面的原因：一是接入电网电压较低且线路较短，系统阻抗呈现正电阻电感特性；二是并网装置整体延时相比柔直系统来说更小。柔直工程高频振荡问题发现时间较短，国内外仅有少量文献进行了报道[12-14]，文献[12]较完整地分析了南网鲁西工程高频振荡现象，提出了在电压前馈环节加入低通滤波器和公共耦合点(point of common coupling，PCC)加装无源滤波器的解决方案，然而该文没有在控制系统中提出额外的阻尼控制方案。

本文针对实际柔直工程出现的高频振荡现象，以 dq 阻抗法为主，从建模、高频振荡特性分析、阻尼控制及验证等几个方面进行阐述，分析相关环节对柔直高频阻抗特性的影响及高频振荡特性。再次，提出高频振荡阻尼控制策略，采用 MMC 简化模型分析阻尼控制器参数对阻抗高频特性的影响，并设计保持系统稳定的控制器参数。最后，利用电磁暂态仿真模型验证所提策略的有效性及参数设计的正确性。

**图1 柔直系统主电路示意图**
*Fig. 1 Main circuit diagram of HVDC system*

柔直主电路的状态空间表达式请参考文献[16]。其中：$C$ 为子模块电容；$T$ 为桥臂子模块总数；$i_{\text{arm}}$ 为桥臂电流；$u_{\text{dc}}$ 和 $i_{\text{dc}}$ 分别为直流电压和直流电流；$i_{\text{s}j}$ 为 $j$ 相电流；$i_{\text{cir}j}$ 为 $j$ 相环流；$e^*_{\text{v}j}$ 和 $u^*_{\text{cir}j}$ 为控制系统输出的基波和二倍频电压的参考值；$R_{\text{eq}} = R_{\text{t}} + R_{\text{arm}}/2$ 和 $L_{\text{eq}} = L_{\text{t}} + L_{\text{arm}}/2$ 为 MMC 交流侧等效电阻和电感；$R_{\text{t}}$ 和 $L_{\text{t}}$ 为换流变的电阻和漏感；$R_{\text{arm}}$ 和 $L_{\text{arm}}$ 为桥臂等效电阻和电感；$C_{\text{dc\_line}}$、$R_{\text{dc\_line}}$ 和 $L_{\text{dc\_line}}$ 为直流线路的等效电容、电阻和电感，$E_{\text{s}}$ 为对站直流电压。取状态变量 $\boldsymbol{x}_{\text{mmc}} = [u_{\text{dc}}, u_{\text{c\_dc0}}, u_{\text{c\_ac1d}}, u_{\text{c\_ac1q}}, u_{\text{c\_ac2d}}, u_{\text{c\_ac2q}}, i_{\text{dc}}, i_{\text{dc\_line}}, i_{\text{sd}}, i_{\text{sq}}, i_{\text{cird}}, i_{\text{cir}q}]^{\text{T}}$，控制变量为 $\boldsymbol{u}_{\text{mmc}} = [E_{\text{s}}, u_{\text{sd}}, u_{\text{sq}}, e^*_{\text{vd}}, e^*_{\text{vq}}, u^*_{\text{cird}}, u^*_{\text{cir}q}, \omega]^{\text{T}}$，输出变量 $\boldsymbol{y}_{\text{mmc}} = [i_{\text{sd}}, i_{\text{sq}}, i_{\text{cird}}, i_{\text{cir}q}]^{\text{T}}$，则柔直主电路的状态空间表达式为

$$
\begin{cases}
\frac{\mathrm{d}\Delta \boldsymbol{x}_{\text{mmc}}}{\mathrm{d}t} = \boldsymbol{A}_{\text{mmc}} \cdot \Delta \boldsymbol{x}_{\text{mmc}} + \boldsymbol{B}_{\text{mmc}} \cdot \Delta \boldsymbol{u}_{\text{mmc}} \\
\Delta \boldsymbol{y}_{\text{mmc}} = \boldsymbol{C}_{\text{mmc}} \cdot \Delta \boldsymbol{x}_{\text{mmc}} + \boldsymbol{D}_{\text{mmc}} \cdot \Delta \boldsymbol{u}_{\text{mmc}}
\end{cases} \quad (1)
$$

式(1)所示的状态空间模型适用于电气系统和控制系统 dq 坐标系，本文将应用在控制系统 dq 坐标系中。为后续研究方便，将式(1)转换为传递函数形式，则交流侧电流和 MMC 环流的表达式为：

$$
\Delta i_{\text{sdq}} = \boldsymbol{M}_1 \cdot \Delta e^*_{\text{vdq}} + \boldsymbol{M}_2 \cdot \Delta u^*_{\text{cirdq}} + \boldsymbol{M}_3 \cdot \Delta u_{\text{sdq}} \quad (2)
$$

$$
\Delta i_{\text{cirdq}} = \boldsymbol{M}_4 \cdot \Delta e^*_{\text{vdq}} + \boldsymbol{M}_5 \cdot \Delta u^*_{\text{cirdq}} + \boldsymbol{M}_6 \cdot \Delta u_{\text{sdq}} \quad (3)
$$

其中：

$$
\begin{cases}
\boldsymbol{M}_1 = \boldsymbol{C}_{\text{mmc\_is}} (s\boldsymbol{I}_{\text{mmc}} - \boldsymbol{A}_{\text{mmc}})^{-1} \boldsymbol{B}_{\text{mmc1}} \\
\boldsymbol{M}_2 = \boldsymbol{C}_{\text{mmc\_is}} (s\boldsymbol{I}_{\text{mmc}} - \boldsymbol{A}_{\text{mmc}})^{-1} \boldsymbol{B}_{\text{mmc2}} \\
\boldsymbol{M}_3 = \boldsymbol{C}_{\text{mmc\_is}} (s\boldsymbol{I}_{\text{mmc}} - \boldsymbol{A}_{\text{mmc}})^{-1} \boldsymbol{B}_{\text{mmc3}}
\end{cases}
$$