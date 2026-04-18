## 双馈风力发电机组的电磁暂态−机电暂态混合仿真研究
顾卓远，汤涌，刘文焯，易俊，张健，戴汉扬，于强
（中国电力科学研究院，北京市 海淀区 100192）

## Electromechanical Transient-Electromagnetic Transient Hybrid Simulation of Doubly-Fed Induction Generator
GU Zhuoyuan, TANG Yong, LIU Wenzhuo, YI Jun, ZHANG Jian, DAI Hanyang, YU Qiang
(China Electric Power Research Institute, Haidian District, Beijing 100192, China)

**ABSTRACT:** To analyze the dynamic response of double-fed induction generator (DFIG) in-depth, based on the operation principle of DFIG an electromagnetic transient model of DFIG is built and the electromagnetic transient-electromechanical transient hybrid simulation of DFIG is performed. The hybrid simulation of DFIG is implemented by the self-developed large-scale power system analysis software package based hybrid simulation platform named Power System Department-Power System Model (PSD-PSModel), and the frame of the basic model of DFIG is established. The wind farm is equivalently simulated by single machine, and IEEE 14-bus test system is utilized for the detailed simulation to analyze the dynamic behavior of the system, the control strategy and dynamic response. The achievement can contribute to facilitate the cooperation with wind power generator manufactures to built detailed electromagnetic transient model of actual DFIG to provide powerful technical support for the in-depth study on the impacts of wind power generation units on power grid stability.

**KEY WORDS:** doubly-fed induction generators; electromagnetic transient; hybrid simulation; modeling

**摘要：** 为深入分析双馈型风力发电机组的动态响应，基于双馈风机的运行原理，建立了双馈风机的电磁暂态模型，并进行了电磁暂态–机电暂态混合仿真研究。在自主开发的大型电力系统分析软件包混合仿真平台 (power system department-power system model，PSD-PSModel)中实现了双馈风机的混合仿真功能，建立了双馈风机的基本模型框架。采用单台机等值模拟风电场，并利用 IEEE 14 节点算例进行了详细的仿真研究，分析了其控制策略和暂态过程中的动态响应。便于今后与风机制造厂家合作建立实际风机的详细电磁暂态模型，为深化研究风电机组对电网稳定的影响提供了有力的技术支持。

**关键词：** 双馈风力发电机组；电磁暂态；混合仿真；建模

**DOI：** 10.13335/j.1000-3673.pst.2015.03.005

基金项目：国家 863 高技术基金项目(2011AA05A103)；国家电网公司科技项目(SGHB0000KXJS1400040)。
The National High Technology Research and Development of China(863 Program)(2011AA05A103).

## 0 引言
随着全球化石能源逐渐枯竭，可再生能源在各国能源战略中的地位越来越重要。在众多新能源中，风能以其清洁、蕴藏量大、技术相对成熟等优势成为世界各国开发绿色能源的首选，双馈风力发电机 (doubly-fed induction generator，DFIG)也得到了广泛应用。风能具有间歇性和随机性的特点，大规模双馈机组接入系统对电网的安全稳定运行有诸多影响，主要表现在以下几个方面[1]：
1）对电力系统暂态稳定性的影响。随着风电接入比例的逐渐增大，其对电力系统暂态稳定性的影响不容忽视。文献[2]认为双馈风电机组接入后会降低同步机组的阻尼特性，不利于同步机组功角的快速稳定。文献[3]认为双馈风机和同步电机的功角摇摆曲线存在两类交点，在大扰动时，首摆期间双馈风机会降低系统的暂态稳定性。
2）对电压稳定性的影响。一般认为双馈风力发电机组可以实现有功无功解耦控制，通过控制策略的调整具备电压支撑能力。文献[4]详细研究了双馈风电机组对系统电压稳定性的影响。
3）对频率稳定性的影响。大多通过控制手段来增强风电机组对电网频率的支撑能力[5]。
因此，有必要开发风电机组的动态模型，研究其与电力系统之间的相互影响。目前在风电机组建模、风功率预测等方面，欧盟电网已达到较高水平，部分研究成果已经开始投入商业使用，如 PSS/E(power system simulator/engineering) [6]、PowerFactory，在今后相当长的一段时间内，这些研究成果都属于商业机密 [7]。在这种条件下，如何自主研发风力发电机组的动态模型且具备较强的仿真能力成为我国风电发展面临的主要问题之一。
根据研究的目的不同，双馈风电机组可以建立不同的数学模型。但是在建模的详细程度上仍然存在争议[8]。文献[9]给出了双馈风力发电机的降阶模型，忽略了定子和转子的暂态过程，换流器采用可控电流源模型，只给出了有限的控制细节。文献[10]介绍了一种适用于大规模电力系统稳定计算的双馈风力发电机动态模型，并分析了控制参数对暂态稳定的影响。文中将转子侧换流器处理为可控电压源，并且假设直流母线电压恒定，网侧换流器采用电流源模拟。
文献[11]为了提高计算速度，方便与机电暂态程序接口，对双馈风机模型做了大幅简化，忽略转子和换流器动态过程。文献[12]认为在电网故障情况下，应该计及类似于同步发电机的次暂态电抗，使用双鼠笼模拟转子回路。文献[13]认为，双馈风力发电机模型采用降阶模型时，在无故障情况下可以很好地反映 DFIG 的动态响应。文献[14]提出恒速风力机应该使用完整的暂态模型，不应忽略定子暂态过程。对于双馈风力发电机，发电机模型的选择会影响到定子电流，可能会导致暂态期间保护系统误动作。
本文从双馈风力发电机建模仿真的现状和实际需求出发，借助 PSD-PSModel(power system department-power system model)电磁暂态-机电暂态混合仿真平台，对风力发电机组开展电磁暂态-机电暂态混合仿真研究，为今后深化研究风电机组对电网影响提供有力的技术支持。

## 1 双馈风力发电机组的电磁暂态建模
### 1.1 双馈风力发电机组的基本结构
双馈型风力发电系统结构如图 1 所示，主要包括风力机模型、轴系传动系统模型、双馈感应发电机模型及换流器模型 4 部分和控制系统。由于时间

图 1 双馈风力发电机组结构
Fig. 1 Structure of doubly-fed induction generator

量可表示为
$$ P = \frac{1}{2} \rho \pi R^2 C_P V_{\text{wind}}^3 \tag{1} $$
式中：$P$ 代表风力机的输出功率；$\rho$ 代表空气密度；$R$ 代表叶片半径；$C_P$ 代表风能利用效率系数；$V_{\text{wind}}$ 代表风速。效率系数 $C_P$ 是表征风力机运行效率的重要参数，它与风速、风轮转速、风轮半径、浆距角均有关系，是一个非常复杂的非线性函数。

### 1.2.2 传动系统的数学模型
轴系传动系统由旋转部分、齿轮箱和轴系组成。惯量主要是风力机风轮和发电机转子质量块，齿轮箱的齿轮只占很小一部分，可以忽略齿轮惯性，只考虑变比。选用双质量块模型进行模拟，建模时采用标幺值系统，低速旋转的风轮和发电机转子转速基准值的比值选取为齿轮箱变比，其数学模型为
$$
\begin{cases}
\frac{d\omega_t}{dt} = \frac{T_t - T_{\text{shaft}}}{2H_t} \\
\frac{d\omega_g}{dt} = \frac{T_{\text{shaft}} - T_e}{2H_g} \\
T_{\text{shaft}} = K_{\text{damping}}(\omega_r - \omega_g) + K_{\text{stiffness}}\theta_k \\
\frac{d\theta_k}{dt} = \omega_r - \omega_g
\end{cases} \tag{2}
$$
式中：$\omega_t$ 代表风力机风轮转速；$t$ 代表时间；$T_t$ 代表风力机输出的机械转矩；$T_{\text{shaft}}$ 代表轴转矩；$H_t$ 代表风力机惯性时间常数；$\omega_g$ 代表发电机转子转速；$T_e$ 代表发电机电磁转矩；$H_g$ 代表发电机惯性时间常数；