## 基于电流过零点预计算的单有源桥变换器等效建模方法
高晨祥，王晓婷，丁江萍，许建中*，赵成勇
(新能源电力系统国家重点实验室(华北电力大学)，北京市 昌平区 102206)

## Equivalent Modelling Method of Single Active Bridge Converter by Pre-calculating the Current Zero-crossing
GAO Chenxiang, WANG Xiaoting, DING Jiangping, XU Jianzhong*, ZHAO Chengyong
(State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources (North China Electric Power University), Changping District, Beijing 102206, China)

**ABSTRACT:** As an important scheme for grid connection of photovoltaic, wind power and other DC power sources, modular isolated DC/DC converter (MIDC) has received extensive attention. The input parallel output series (IPOS) type single active bridge (SAB) converter is one of the common topologies of MIDC. Due to the high node admittance order, low simulation step size and the existence of uncontrolled rectifier bridge, its electromagnetic transient simulation efficiency is extremely low. This paper proposed an equivalent modeling method of SAB converter by the pre-calculating current zero-crossing. First, the topology and working principle of the SAB converter were analyzed to solve the inductor current expression in different modes. Secondly, the expression of the zero-crossing point of the inductance current was given with the distinguishing conditions of different modes. Then, analogy to the DAB converter, the equivalent model of the IPOS type SAB converter was established. On this basis, Lyapunov method was used to prove the stability of the proposed equivalent model. Finally, the accuracy and acceleration ratio of the proposed model were verified in the PSCAD/EMTDC environment.

**KEY WORDS:** single active bridge (SAB); current zero-crossing; equivalent model; stability

**摘要：** 模块化隔离型 DC/DC 变换器(modular isolated DC/DC converter，MIDC)作为光伏、风电等直流电源并网的重要方案，受到广泛关注。输入并联输出串联(input parallel output series，IPOS)型单有源桥(single active bridge，SAB)变换器是 MIDC 的常用拓扑之一，由于节点导纳矩阵阶数高、仿真步长小以及不控整流桥的存在，其电磁暂态仿真效率很低。文中提出一种基于电流过零点预计算的 SAB 变换器等效建模方法。首先，针对 SAB 变换器的拓扑结构和工作原理进行分析，求解不同模式下电感电流表达式。其次，计算电感电流过零点，并给出不同模式的区分条件。然后，类比 DAB 变换器，建立 IPOS 型 SAB 变换器的等效模型。在此基础上，利用 Lyapunov 法证明所提等效模型的稳定性。最后，在 PSCAD/EMTDC 环境中验证所提出模型的精度和加速比。

**关键词：** 单有源桥变换器；电流过零点；等效建模；稳定性

基金项目：国家重点研发计划资助项目(2018YFB0904600)。
National Key R&D Program of China (2018YFB0904600).

## 0 引言
近年来，我国风电和光伏在电网中的装机容量实现了 17%和 44%的迅猛增长[1]，模块化隔离型 DC/DC 变换器(modular isolated DC/DC converter，MIDC)作为实现大功率直流电源并网的重要方案之一，因为其具有无器件均压、均流问题、可靠性高、易于冗余设计等优势受到广泛关注[2]。

现有的 MIDC 拓扑结构多样，包括移相控制全桥变换器、单有源桥式变换器(single active bridge，SAB)、LCC 串并联谐振变换器、双有源桥式变换器(dual active bridge，DAB)和基于晶闸管的谐振变换器等[3-6]。文献[7]针对不同类型拓扑结构给出了元件应力、元件数与损耗方面的比较。在实际分布式电源并网过程的大多数时间内，电能为单向传输，因此双有源桥变换器会带来不必要的投资与损耗[2]。LCC 等谐振变换器虽然可以提高效率，但是所需滤波电感较大，控制较为复杂[8]。因此本文以 SAB 变换器为主要研究对象。同时，由于光伏、风电等直流电源的并网通常需要实现高增益、大容量的目标，因此常采用输入并联输出串联(input parallel output series，IPOS)的模块级联方式。

为满足大容量与高电压需求，IPOS 型 SAB 变换器包含大量功率模块，仿真系统节点数高，在 PSCAD/EMTDC 的电磁暂态仿真中，矩阵求逆工作量大。并且，每个模块内开关器件与高频变压器工作于较高频率，限制了系统的仿真步长[9]，基于详细器件搭建的换流器模型的仿真效率很低。

对此，国内外学者针对仿真提速展开了很多研究工作。文献[10-11]针对高频链全桥换流器提出了连续状态空间平均模型和非线性函数降阶大信号简化模型；文献[12]提出了针对区域电能路由器的级间电容解耦算法，但由于未对隔离变压器进行处理，加速比和通用性受限。文献[13-14]利用变压器解耦思路与嵌套快速求解法结合，提出了针对 DAB 与 CHB 型变换器的等效模型；文献[15]进一步利用 DAB 单元的对称性和稀疏性，提出了基于节点导纳矩阵预处理的等效模型，大幅提高了仿真速度。但是这几种等效建模方法均不能直接应用于 IPOS 型 SAB 变换器的仿真提速。相比于 DAB 单元，SAB 具有不控整流桥，其二极管的开关状态不是由触发信号直接决定；另一方面，SAB 变换器的 IPOS 级联方式也会导致与 ISOP 型 DAB 变换器的差异。

本文提出一种基于电流过零点预计算的 SAB 变换器等效模型。首先通过对 SAB 拓扑及工作原理进行分析，得出电感电流的表达式，然后给出不同模式下电感电流过零点计算式及模式区分条件。在此基础上，类比 ISOP 型 DAB 变换器，提出 IPOS 型 SAB 变换器的等效模型。

```
T1                 T3
D1            D3
D5             D7
T2                 T4
D2            D4
D6             D8
```
**图1 IPOS 型 SAB 变换器拓扑图**  
**Fig. 1 Topology of IPOS SAB converter**

T1 和 T3 的触发相差 $180^\circ$，如图 2 所示。通过 T1 触发信号的占空比为 $d_P$，可以实现功率控制。同时，输入侧 H 桥的输出电压仅由 IGBT 触发信号决定。

```
T1               d_P T_s
T2                                (1 - d_P) T_s
T3                                     d_P T_s
T_s / 2
T4
v_P
t
```
**图2 触发信号图**  
**Fig. 2 Waveform of the trigger signal**

### 1.2 工作原理
随着占空比 $d_P$ 的变化，SAB 变换器有 2 种工作模式，分别为连续导通模式(continuous conduction mode，CCM)和非连续导通模式[8](discontinuous conduction mode，DCM)，如图 3 所示。

$T_s / 2$