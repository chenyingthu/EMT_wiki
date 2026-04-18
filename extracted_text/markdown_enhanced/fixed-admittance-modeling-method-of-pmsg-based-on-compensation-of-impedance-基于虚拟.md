## 基于虚拟阻抗补偿的 PMSG 恒导纳建模方法
**史一博，刘崇茹\***
(新能源电力系统国家重点实验室(华北电力大学)，北京市 昌平区 102206)

## Fixed-admittance Modeling Method of PMSG Based on Compensation of Impedance
**SHI Yibo, LIU Chongru\***
(State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources (North China Electric Power University), Changping District, Beijing 102206, China)

**ABSTRACT:** The permanent magnet generator system has a complex structure and a large number of nodes. In the real-time electromagnetic transient simulation, if the traditional modeling method is used, the calculation of the system admittance matrix will be too complicated, resulting in a serious limitation of the simulation scale. Therefore, this paper proposes a fixed-admittance modeling method of permanent magnet synchronous generator (PMSG) based on virtual impedance compensation. This method is based on the traditional generator model, and the generator admittance matrix is fixed by compensating the virtual impedance on the rotor. The impedance parameters are optimized with the goal of minimizing the transient error. By combining the constant admittance model of voltage source converter, a complete constant admittance model of PMSG can be established and electromagnetic transient simulation can be performed, thus saving a lot of computing resources. Simulation experiments show that the model has high simulation accuracy, and can be used in discrete hardware simulation platforms such as FPGA, with good applicability.

**KEY WORDS:** fixed-admittance model; compensation of impedance; permanent magnet synchronous generator

**摘要：** 永磁直驱风力发电系统结构复杂、节点数多，在进行电磁暂态实时仿真时，若采用传统建模方法会因系统导纳矩阵计算过于复杂导致仿真规模严重受限。该文提出一种基于虚拟阻抗补偿的永磁同步发电机 (permanent magnet synchronous generator，PMSG)恒导纳建模方法，该方法基于传统发电机模型，通过在转子上补偿虚拟阻抗的方式使发电机导纳矩阵固定，并以暂态误差最小为目标，对阻抗参数进行优化设计；再通过结合换流器的伴随离散电路模型，可建立 PMSG 完整恒导纳模型并进行电磁暂态仿真，能够节省大量的计算资源。仿真试验证明，该模型具有较高的仿真精度，并且可以用于 FPGA 等离散化硬件仿真平台上，具有良好的适用性。

**关键词：** 恒导纳模型；虚拟阻抗补偿；永磁同步电机

## 0 引言
随着我国“2030 碳达峰、2060 碳中和”目标的提出，新能源发电进入快速发展建设阶段[1-3]。永磁直驱风力发电机对环境污染小、发电成本相对较低[4-6]。由于省去了齿轮箱，采用全功率变换器，永磁同步发电机 (permanent magnet synchronous generator，PMSG)具有效率高、对风速变化适应力强等特点[7]，逐渐成为风力发电的主流。

风力发电机由于定转子系统耦合关系复杂，并且除了电路磁链还涉及到转子力矩的物理部分，因此目前主流的仿真模型仍然是相域(phase domain，PD)模型 [8-9] 、转子坐标系模型 [10-12] 和电压后电抗 (voltage-behind-reactance，VBR)模型[13]等。

文献[8]提出的 PD 模型是一种常用的发电机模型。PD 模型基于原始的电压磁链耦合公式[14]表示三相的电压电流关系，参数以物理变量和相位坐标表示[15]，可以直接接入电网进行计算。

转子坐标系模型是通过派克变换将 PD 模型变为同步速旋转坐标系得到的模型，派克变换将定子三相绕组转换为定子 $dq$ 绕组，因此该模型也简称 $dq$ 模型。该模型广泛应用于电磁暂态程序如 PSCAD[12]和 Simulink[15]中。

此外，文献[13]提出的 VBR 模型也是一种常用的发电机模型。VBR 最早由 S. D. Pekarek 等提出，其核心思想是基于 PD 模型表示出电机出口端电压电流关系进行简化计算，其本质仍然是类似 PD 模型的三相坐标系仿真，与 PD 模型没有本质区别。

目前，工程上一个永磁直驱风电场往往包含几十台风力发电机，单台发电机组包含发电机和换流器等设备，结构复杂，节点数多[16]。在进行电磁暂态实时仿真时，如果采用 PD 模型、VBR 模型等传统变导纳矩阵建模方法，会导致导纳矩阵求逆计算过于困难[17]，消耗大量计算资源且系统仿真规模严重受限，难以进行大规模新能源电力系统电磁暂态仿真[18-20]。因此有必要考虑模型的恒导纳方法，将网络导纳矩阵固定进行简化计算。

恒导纳是一种建模方法，常用于绝缘栅双极晶体管(insulate-gate bipolar transistor，IGBT)等电力电子器件电磁暂态仿真建模[21-23]；在建立数学模型时采用等值近似，将原本会因为元件状态变化的导纳固定下来，以达到简化计算的效果。目前电力电子器件恒导纳模型主要包括：伴随离散电路模型(associated discrete circuit，ADC)模型[24]、附加支路模型[25]、负电阻补偿模型[26]等，相关成果已经被广泛应用在 RTDS、RT-LAB 等实时仿真平台。

本文在 PD 模型的基础上提出一种基于虚拟阻抗补偿的 PMSG 恒导纳模型。通过在发电机转子侧添加阻抗，补偿导纳矩阵的时变部分使发电机导纳矩阵恒定；在换流器侧应用电力电子开关的伴随离散电路模型，使换流器导纳矩阵恒定。在此基础上，可建立起 PMSG 完整恒导纳模型并进行电磁暂态计算，避免计算过程中的导纳矩阵求逆，能够节省大量仿真资源。

## 1 PMSG 电磁暂态模型
传统永磁直驱风力发电机组由风力机、发电机、机网侧换流器、网侧滤波器及控制部分组成，整体机组拓扑如图 1 所示。图中，$V_{\text{wind}}$ 为风速，$\omega$ 为功率存在对应关系，因此可以简化成分段函数。

当风速未达额定风速时，风力机处在最大功率点跟踪(maximum power point tracking，MPPT)控制阶段，风力机功率与风速成三次方关系。

当风速达到额定风速时，风力机处在变桨距控制阶段，风力机捕获的机械功率等于额定功率。

风力机机械功率曲线如图 2 所示。$P_M$ 为电机功率。

> 额定功率 | MPPT 控制 | 变桨距控制 | 理论功率曲线 | 实际功率曲线 | 运行范围 | 最低功率 | 切入风速 | 额定风速 | 切出风速 | $V_{\text{wind}}$

**图2 风力机机械功率曲线**  
**Fig. 2 Wind turbine mechanical power curve**

### 1.2 换流器模型
目前比较经典的电力电子开关电磁暂态模型有双值电阻模型[28]、LC 等效模型[28]、ADC 模型[25]等，此外专家学者还提出负电阻补偿模型[26]、附加支路模型[26]等新型开关模型。ADC 模型是目前应用最为广泛的开关模型，广泛应用在 RTDS、RT-LAB 等实时仿真平台。

ADC 模型的主要思路是将开关导通等效为电感支路，关断等效为电容与电阻的串联支路。等效模型如图 3 所示。通过选取电路参数，使梯形法离散后电路模型的等效导纳相等，即开关变化不影响电路导纳。离散后的差分电路为等效电导并联等效电流源的诺顿形式。