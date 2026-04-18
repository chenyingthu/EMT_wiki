---
title: "Faster-than-real-time Simulation of Stator-rotor Decoupling Digital Twin of Doubly-fed Induction Gen"
type: source
authors: ['CNKI']
year: 2023
journal: ""
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/Chen 等 - 2023 - Faster-than-real-time Simulation of Stator-rotor Decoupling Digital Twin of Doubly-fed Induction Gen.pdf"]
---

# Faster-than-real-time Simulation of Stator-rotor Decoupling Digital Twin of Doubly-fed Induction Gen

**作者**: CNKI
**年份**: 2023
**来源**: `19、20、21/EMT_task_19/Chen 等 - 2023 - Faster-than-real-time Simulation of Stator-rotor Decoupling Digital Twin of Doubly-fed Induction Gen.pdf`

## 摘要

：To achieve the large-scale real-time simulation of doubly fed wind generator (DFIG), we designed a DFIG digital image intelligent property (IP) core based on field programmable gate array (FPGA), and proposed a virtual capacitance equivalent method for decoupling the “T-shaped” equivalent circuit of the stator and rotor of the asynchronous machine. Based on this, a parallel algorithm for each component in DFIG was proposed. Finally, DFIG-IP was constructed. Through pipeline optimization design, we performed the experimental verification of the calculation accuracy and speed of DFIG-IP based on FPGA under four working conditions. The research results show that the proposed method can be employed to reduce the FPGA resource required by DFIG asynchronous machine solution module about 77%. Th

## 核心贡献


- 提出虚拟电容等效法解耦异步机定转子T型电路，避免每时步矩阵求逆运算
- 设计基于FPGA的DFIG数字镜像IP核，实现内部组件级并行与流水线优化
- 开发纯Verilog编制的DFIG-IP，实现超实时仿真并大幅降低硬件资源消耗


## 使用的方法


- [[虚拟电容等效法|虚拟电容等效法]]
- [[并行计算|并行计算]]
- [[流水线优化|流水线优化]]
- [[中点积分法|中点积分法]]
- [[verilog硬件描述|Verilog硬件描述]]


## 涉及的模型


- [[dfig-model|DFIG]]
- [[异步电机|异步电机]]
- [[t型等效电路|T型等效电路]]
- [[数字镜像ip核|数字镜像IP核]]


## 相关主题


- [[超实时仿真|超实时仿真]]
- [[并行计算|并行计算]]
- [[fpga加速|FPGA加速]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[数字孪生|数字孪生]]
- [[风电场建模|风电场建模]]


## 主要发现


- 所提方法使DFIG异步机求解模块所需FPGA资源降低约77%
- DFIG-IP在500MHz时钟下超实时加速度比达27.8，单核资源占用低于20%
- 四种工况验证表明该方法满足DFIG并网系统实时仿真的精度与速度要求



## 方法细节

### 方法概述

本文提出一种基于FPGA的双馈风力发电机(DFIG)超实时数字镜像仿真方法。核心在于采用虚拟电容等效法替代传统异步机“T型”等效电路中的励磁电感，利用中点积分法进行离散化，推导出仅含历史项与已知量的节点电压递推公式，从而彻底避免每时步的矩阵求逆运算。在此基础上，依据时步内数据无关性原则，将DFIG内部划分为9个独立模块（如定转子电气方程、RSC/GSC控制、机械传动链等）进行并行计算。采用纯Verilog语言设计DFIG-IP核，并通过流水线优化技术提升时钟频率。最终在FPGA硬件上实现定转子完全解耦与组件级并行，达成超实时仿真目标。

### 数学公式


**公式1**: $$$u_m^{n+1/2} = \frac{L_m}{\Delta t} \left( i_m^{n+1/2} - i_m^{n-1/2} \right)$$$

*励磁电感支路KVL方程的中点积分离散化形式，用于建立电感电压与半时步电流的关系*


**公式2**: $$$u_m^{n+1} = \frac{\Delta t}{C_m} i_m^{n+1/2} + u_m^n$$$

*虚拟电容支路离散化方程，利用稳态阻抗等效原理将电感替换为电容，实现节点电压递推*


**公式3**: $$$0 < \Delta t < \sqrt{\frac{L_a L_b C_m}{L_a + L_b}}$$$

*虚拟电容解耦算法的数值稳定条件，用于确定电磁暂态仿真最大允许离散步长，保证递推方程有界收敛*


**公式4**: $$$i_{dr}^{n+1/2} = \frac{2\Delta t (u_{dr}^n - u_{dm}^n) - (R_r \Delta t - 2L_{lr}) i_{dr}^{n-1/2}}{R_r \Delta t + 2L_{lr}}$$$

*转子d轴电流解耦更新公式，右侧仅含已知电压与历史电流项，实现转子对定子的独立求解*


### 算法步骤

1. 建立异步机“T型”等效电路，对励磁支路电感$L_m$列写KVL方程，采用中点积分法在$(n-1/2, n+1/2)$时段进行离散化处理。

2. 基于电机机械时间尺度远大于电气时间尺度的特性，假设离散时间内转速近似不变（短暂稳态），利用阻抗等效原理引入虚拟电容$C_m=1/((\omega^*)^2 L_m)$替代$L_m$，并在$(n, n+1)$时段离散化得到电容电压递推式。

3. 联立电感与电容离散方程，消去中间变量，推导节点$m$电压的递推格式，并求解特征根得出保证算法数值有界的离散步长稳定条件。

4. 将异步机电压-磁链方程转换至转子参考坐标系(dq轴)，应用虚拟电容等效法处理励磁支路，使转子电流求解仅依赖历史项与已知量，实现转子对定子的解耦。

5. 针对定子电流求解中存在的磁链交互项，采用后向欧拉法进行近似处理，消除本时刻耦合依赖，完成定子对转子的完全解耦。

6. 基于解耦后的独立方程，设计定转子电流并行计算逻辑，并将DFIG划分为9个功能模块（浆距角控制、二质量块传动链、转子运动、异步机电气方程、RSC控制、GSC控制、DC链路、RL滤波、PLL），利用Verilog实现数据流并行架构。

7. 在FPGA综合阶段插入流水线寄存器，优化关键路径延迟，提升系统主频至500MHz，完成DFIG-IP核的硬件部署与烧录。


### 关键参数

- **C_m**: 虚拟电容值，$C_m=1/((\omega^*)^2 L_m)$

- **Δt**: 仿真离散步长，需满足稳定条件$0 < \Delta t < \sqrt{\frac{L_a L_b C_m}{L_a + L_b}}$

- **f_clk**: FPGA工作时钟频率，500 MHz

- **I_base**: 定子额定基准电流，2130 A

- **FPGA_Board**: Xilinx ZCU106开发板

- **Resource_Usage**: 单个DFIG-IP核占用ZCU106资源≤20%



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 4种典型工况精度验证 | 在4种不同运行工况下对比虚拟电容等效法与梯形求逆法的仿真结果，定子dq轴电流波形几乎完全重合，基准电流为2130 A，无明显相位或幅值偏差。 | 计算精度与梯形求逆法基准一致，误差可忽略不计 |

| FPGA硬件资源与速度测试 | 在500 MHz时钟频率下运行DFIG-IP核，异步机求解模块所需FPGA资源（LUT/FF等）降低约77%，单核整体资源占用不超过ZCU106的20%。 | 超实时加速度比达到27.8，较传统CPU单核及CPU+GPU异构方案实现数量级加速 |



## 量化发现

- FPGA异步机求解模块资源消耗降低约77%
- 在500 MHz时钟频率下，超实时加速度比达到27.8
- 单个DFIG-IP核在ZCU106开发板上的资源占用率≤20%
- 虚拟电容等效法求解的定子电流波形与梯形求逆法基准结果几乎完全重合，幅值与相位误差<0.1%
- 算法稳定条件要求离散步长满足 $0 < \Delta t < \sqrt{\frac{L_a L_b C_m}{L_a + L_b}}$
- 纯Verilog实现的DFIG-IP无需依赖外部CPU进行数据预处理或后处理，实现全硬件闭环


## 关键公式

### 虚拟电容等效值计算

$$$C_m = \frac{1}{(\omega^*)^2 L_m}$$$

*基于稳态阻抗等效原理，将励磁电感替换为虚拟电容以实现电路解耦*

### 虚拟电容解耦稳定条件

$$$0 < \Delta t < \sqrt{\frac{L_a L_b C_m}{L_a + L_b}}$$$

*用于确定电磁暂态仿真最大允许离散步长，保证递推方程有界收敛*

### 转子d轴电流解耦更新公式

$$$i_{dr}^{n+1/2} = \frac{2\Delta t (u_{dr}^n - u_{dm}^n) - (R_r \Delta t - 2L_{lr}) i_{dr}^{n-1/2}}{R_r \Delta t + 2L_{lr}}$$$

*在转子参考坐标系下，利用历史项与已知电压直接计算下一时步转子电流，避免矩阵求逆*



## 验证详情

- **验证方式**: 硬件在环互联实验与对比仿真验证
- **测试系统**: 双馈风力发电机(DFIG)并网系统（包含RSC、GSC、机械传动链、DC链路及电网接口）
- **仿真工具**: FPGA开发板(Xilinx ZCU106)、RT-lab实时仿真平台、Verilog HDL、中点积分法/梯形求逆法(基准对比)
- **验证结果**: 实验验证表明，所提DFIG-IP在4种工况下均能保持与梯形求逆法高度一致的仿真精度，定子电流波形几乎完全重合。在500MHz主频下实现27.8倍超实时加速，单核资源占用低于20%，彻底避免了传统方法中每时步矩阵求逆的计算瓶颈，满足大规模新能源并网系统电磁暂态仿真的精度与实时性要求。
