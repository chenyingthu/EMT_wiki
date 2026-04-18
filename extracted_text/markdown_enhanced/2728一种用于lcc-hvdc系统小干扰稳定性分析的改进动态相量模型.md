# 一种用于 LCC–HVDC 系统小干扰稳定性分析的改进动态相量模型
贺永杰$^1$，向往$^1$，赵静波$^2$，周家培$^3$，鲁晓军$^1$，倪斌业$^1$，文劲宇$^1$
（1．强电磁工程与新技术国家重点实验室(华中科技大学)，湖北省 武汉市 430074；
2．国网江苏省电力有限公司电力科学研究院，江苏省 南京市 211103；
3．先进输电技术国家重点实验室(全球能源互联网研究院有限公司)，北京市 昌平区 102209）

Modified Dynamic Phasor Model for Small-signal Stability Analysis of LCC-HVDC System
HE Yongjie$^1$, XIANG Wang$^1$, ZHAO Jingbo$^2$, ZHOU Jiapei$^3$, LU Xiaojun$^1$, NI Binye$^1$, WEN Jinyu$^1$
(1. State Key Laboratory of Advanced Electromagnetic Engineering and Technology (Huazhong University of Science and Technology), Wuhan 430074, Hubei Province, China;
2. Electric Power Research Institute of State Grid Jiangsu Electric Power Co., Ltd., Nanjing 211103, Jiangsu Province, China;
3. State Key Laboratory of Advanced Power Transmission Technology (Global Energy Interconnection Research Institute Co., Ltd.), Changping District, Beijing 102209, China)

**ABSTRACT:** With the widespread use of line commutated converter based high voltage direct current (LCC-HVDC) technology, and the couplings between AC and DC systems or the sending and receiving ends becoming more complicated, the stability of hybrid AC/DC power grids is becoming increasingly prominent. The small-signal stability analysis based on the linearized model is an important method to study the stability of hybrid AC/DC power grids. As the key equipment to connect AC and DC in hybrid AC/DC power grids, the linearized model of LCC converter is significant. Most existing literature derive the time-domain linearized model of LCC converter based on the quasi-steady assumption, which may introduce errors into the model. Therefore, this paper proposes a modified dynamic phasor model of LCC converter, which takes into account the actual sinusoidal variation of valve current during the commutation process. Firstly, a time-domain linearized model of a typical unipolar 12-pulse LCC-HVDC system is established based on the modified model. And then, it is validated by the electromagnetic transient simulation. Finally, the influence of the parameters of the rectifier-side controller, the inverter-side controller and the phase-locked loop (PLL) on the small-signal stability of the system is analyzed. Simulation and analysis show that the improved dynamic phasor model proposed in this paper has a better improvement effect than the unimproved model.
**KEY WORDS:** LCC-HVDC; dynamic phasor; small-signal stability

**摘要：** 随着基于线路换相换流器的高压直流输电(line commutated converter based high voltage direct current，LCC-HVDC)技术的广泛应用，交流和直流、送端和受端之间的耦合日益紧密，交直流混联电网的稳定性问题日益突出。基于线性化模型的小干扰稳定性分析是研究交直流混联电网稳定性的重要手段。作为交直流混联电网中连接交直流的关键设备，LCC 换流器的线性化模型十分重要。已有文献大多基于准稳态假设推导 LCC 换流器的时域线性化模型，这会在模型中引入误差。为此，提出了一种 LCC 换流器的改进动态相量模型，其考虑了换相过程中阀电流的实际正弦变化规律。首先基于该模型建立了典型的单极 12 脉动 LCC-HVDC 系统的时域线性化模型，然后通过电磁暂态仿真验证了模型的正确性，最后分析了整流侧控制器参数、逆变侧控制器参数和锁相环(phase-locked loop，PLL)参数对系统小干扰稳定性的影响。仿真和分析表明文中所提的改进动态相量模型相对未改进模型有较好的改进效果。
**关键词：** LCC-HVDC；动态相量；小干扰稳定性

DOI：10.13335/j.1000-3673.pst.2020.0226
基金项目：国家电网有限公司科技项目“多落点级联混合直流输电系统关键技术研究”(5200-201958248A-0-0-00)。
Project Supported by State Grid Corporation of China Scientific Research Program - Research on Key Technologies of Multi-infeed Cascaded Hybrid HVDC System (5200-201958248A-0-0-00).

## 0 引言
我国的能源基地和负荷中心在空间上呈现逆向分布的特点，80%以上的能源分布在西部和北部地区，而 75%以上的负荷却又集中在中部和东部地区[1]。这一特点促生了大范围能源资源优化配置的迫切需求。由于具备大容量远距离输电的优势，LCC-HVDC 技术自 20 世纪 70 年代以来得到了广泛应用。

自云南—广东$\pm$800kV 和向家坝—上海$\pm$800kV 两回特高压直流示范工程投运以来，我国又陆续投运了锦屏—苏南$\pm$800kV、哈密南—郑州$\pm$800kV 等 10 余回特高压直流工程[2]，其中 2019 年投运的准东—皖南$\pm$1100kV 特高压直流工程更是世界上电压等级最高、输送容量最大、输送距离最远、技术水平最先进的特高压直流工程。随着 LCC-HVDC 工程的不断投运，受端电网形成了多回直流密集馈入的格局，西南电网—华东电网甚至出现了 5 回特高压直流“同送同受”的局面。以上导致了受端多回直流之间以及送端与受端之间的耦合愈发紧密[3]，对交直流混联电网稳定性问题研究的需求也愈发迫切。鉴于交直流混联电网是一个高度非线性的系统，直接对其研究不仅十分困难而且也不利于稳定性机理的深入挖掘，因此基于其线性化模型的小干扰稳定性分析成为了研究交直流混联电网稳定性问题最基本、最重要的手段[4-6]。

作为交直流混联电网中连接交直流的关键设备，LCC 换流器有着十分复杂的非线性特性，其线性化模型一直是研究热点之一。文献[7]通过引入转换函数(conversion functions)的概念来计算 LCC-HVDC 系统中电流控制回路的传递函数并获得系统的频率响应。文献[8-9]通过对交流电流和直流电压波形的分段线性化表示推导出 LCC 换流器的频域线性化模型。文献[10-11]使用空间矢量传递函数(space vector transfer function)得到 LCC-HVDC 系统的频域线性化模型。文献[12]基于无限 6 脉动 LCC-HVDC 换流器的假设，提出了一种改进的 LCC 换流器频域线性化模型，模型中考虑了换相电感的动态特性以及传输延迟的影响，触发角和关断角的测量采样也被考虑在内。

上述 LCC 换流器的线性化模型均为频域模型，然而小干扰稳定性分析中常用的模态分析法需要 LCC 换流器的时域线性化模型。文献[13-15]基于 LCC 换流器的准稳态特性，建立了系统时域线性化模型。其中文献[13]研究了 PLL 动态对系统稳定性的影响，文献[14]研究了交流系统参数对系统稳定性的影响，文献[15]研究了多馈入 LCC-HVDC 之间的交互影响。文献[16]基于质量–弹簧–阻尼概念提出了一种 LCC-HVDC 系统的时域线性化模型，该模型可以帮助研究人员直观地理解和解释系统的了 LCC 逆变站的时域线性化模型，并研究了 PLL 对系统小干扰稳定性的影响。文献[19]基于 LCC 换流器的准稳态模型建立了特高压直流分层接入的时域线性化模型，并探讨了模态分析方法在特高压直流分层接入的稳定量化评估中的可行性。

上述 LCC 换流器的时域线性化模型大多基于准稳态假设，对于换相过程中阀电流的变化进行线性近似[20]，这会在模型中引入误差。为了消除这一误差，本文提出了一种 LCC 换流器的改进动态相量模型，通过考虑换相过程中阀电流的实际正弦变化规律，该模型可以有效减小误差，提高分析精度。

本文首先基于 LCC 换流器的改进动态相量模型建立典型的单极 12 脉动 LCC-HVDC 系统的时域线性化模型，然后通过与在 PSCAD/EMTDC 平台上搭建的电磁暂态模型对比验证模型的正确性，最后分析整流侧控制器参数、逆变侧控制器参数和 PLL 参数对系统小干扰稳定性的影响。

## 1 LCC 改进动态相量模型
现有 LCC-HVDC 系统按照直流电压等级的不同，分为单极 12 脉动、双极 12 脉动以及双极双 12 脉动等几种类型，6 脉动 LCC 换流器是其基本组成单元。本节首先将给出 6 脉动 LCC 换流器的动态相量模型[21]，然后以此为基础提出其改进动态相量模型。

### 1.1 LCC 动态相量模型
6 脉动 LCC 换流器的等效电路如图 1 所示。图中：$u_a$、$u_b$、$u_c$ 为换流母线三相交流电压；$i_a$、$i_b$、$i_c$ 为换流母线流入换流器的三相交流电流；$u_{dc}$ 为换流器直流电压；$i_{dc}$ 为换流器直流电流；$VT_1 \sim VT_6$ 为晶闸管阀。

**图 1 6 脉动 LCC 换流器等效电路**
**Fig. 1 Equivalent circuit of 6-pulse LCC converter**

设 $S_{va}$、$S_{vb}$、$S_{vc}$ 为三相交流电压与直流电压之间的开关函数，$S_{ia}$、$S_{ib}$、$S_{ic}$ 为直流电流与三相交流