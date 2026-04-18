---
title: "基于CPU-FPGA异构平台的虚拟同步并网逆变器实时仿真算法设计"
type: source
authors: ['CNKI']
year: 2023
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/32/吴盼 等 - 2020 - 基于CPU-FPGA异构平台的虚拟同步并网逆变器实时仿真算法设计.pdf"]
---

# 基于CPU-FPGA异构平台的虚拟同步并网逆变器实时仿真算法设计

**作者**: CNKI
**年份**: 2023
**来源**: `32/吴盼 等 - 2020 - 基于CPU-FPGA异构平台的虚拟同步并网逆变器实时仿真算法设计.pdf`

## 摘要

With the wide application of power electronic devices in power systems, the demand for small time-step (≤ 2μs) electromagnetic transient real-time simulation increases. While a CPU is unable to meet the demand alone, there is a trend to complement it with a Field Programmable Gate Array (FPGA). A CPU-FPGA heterogeneous computing platform available for real-time simulation of virtual synchronous grid-connected inverter system is built. Within it, the circuit part on the FPGA is implemented with an optimized Electro-Magnetic Transient Program (EMTP) algorithm. Constant admittance switch modeling, branch division with parallel processing and high efficiency matrix operation are used to improve real-time performance. The control part on the CPU adopts virtual synchronization control and design

## 核心贡献



- 构建了面向虚拟同步并网逆变器系统的CPU-FPGA异构实时仿真计算平台
- 提出了基于FPGA的优化EMTP算法，结合恒导纳开关建模、支路拆分并行处理与矩阵化高效运算，实现≤2μs小步长电磁暂态仿真

## 使用的方法


- [[fixed-admittance]]
- [[parallel]]
- [[nodal-analysis]]
- [[real-time]]

## 涉及的模型


- [[vsc-model]]

## 相关主题


- [[real-time]]
- [[co-simulation]]

## 主要发现



- CPU-FPGA异构架构结合优化EMTP算法可有效突破单一CPU的计算瓶颈，满足电力电子系统小步长实时仿真需求
- 所提平台的实时仿真波形与Simulink离线仿真结果高度吻合，验证了算法的准确性与FPGA资源利用的高效性

## 方法细节

### 方法概述

本文提出了一种基于NI-PXI系统的CPU-FPGA异构计算平台，用于虚拟同步并网逆变器系统的小步长实时仿真。平台采用分层异构架构：CPU（NI PXIe-8135）负责运行复杂的虚拟同步控制算法，采用大步长100μs；FPGA（NI PXIe-7975R，Kintex-7 XC7K410T）负责电磁暂态电路仿真，采用小步长1μs；上位机负责人机界面交互，周期500μs。针对FPGA架构特点，提出了优化的EMTP算法，通过广义ADC（G-ADC）开关建模实现恒导纳特性（避免开关动作时修改导纳矩阵），通过支路类型拆分实现并行向量运算，通过矩阵化流程（利用关联矩阵）替代传统串行遍历计算，显著提升实时性能。CPU与FPGA之间通过PXIe总线进行异步数据交互，实现电气量与PWM控制信号的传输。

### 数学公式


**公式1**: $$$$I_{h,i} = \begin{cases} \alpha_{\text{on}} Y_{\text{SW}} V_{b,i} + I_{b,i}, & S_i = \text{on} \\ -Y_{\text{SW}} V_{b,i} + \beta_{\text{off}} I_{b,i}, & S_i = \text{off} \end{cases}$$$$

*广义ADC(G-ADC)开关模型历史电流计算式，其中$\alpha_{\text{on}}$和$\beta_{\text{off}}$为最优广义开关模型参数，$Y_{\text{SW}}$为固定导纳，$S_i$为开关状态。该模型保证开关动作前后支路导纳维持$Y_{\text{SW}}$不变，避免更新系统网络导纳矩阵。*


**公式2**: $$$$\begin{cases} \alpha_{\text{on}} = -(1 + \sqrt{2}) \\ \beta_{\text{off}} = -(1 - \sqrt{2}) \end{cases}$$$$

*最优阻尼参数计算公式，确保在满足暂稳态特性约束及系统稳定的前提下，使开关动作暂态过程中支路电压电流快速稳定，减少初始过冲误差与开关虚拟损耗。*


**公式3**: $$$$A_{nb,L} = \begin{bmatrix} a_{nb,L,11} & \cdots & a_{nb,L,1N_L} \\ \vdots & \ddots & \vdots \\ a_{nb,L,N_n1} & \cdots & a_{nb,L,N_nN_L} \end{bmatrix}, \quad a_{nb,L,ij} = \begin{cases} -1, & \text{节点}i\text{为支路}j\text{的首端点} \\ 0, & \text{节点}i\text{不为支路}j\text{的端点} \\ 1, & \text{节点}i\text{为支路}j\text{的末端点} \end{cases}$$$$

*电感支路关联矩阵定义，用于计算节点注入电流，其中$N_n$为总节点数，$N_L$为电感支路数。类似定义适用于电容C、开关SW和电源SC支路。*


**公式4**: $$$$A_{bn,L} = -(A_{nb,L})^T$$$$

*两类关联矩阵的转置关系，$A_{bn,L}$用于计算支路电压，$A_{nb,L}$用于计算节点注入电流。*


**公式5**: $$$$\begin{cases} I_{h,L} = I_{b,L} \\ I_{h,C} = -Y_{b,C} \circ V_{b,C} \\ I_{h,SW} = (\alpha_{\text{on}} Y_{SW} V_{b,SW} + I_{b,SW}) \circ S_{SW} + (-Y_{SW} V_{b,SW} + \beta_{\text{off}} I_{b,SW}) \circ \bar{S}_{SW} \end{cases}$$$$

*各类型支路历史电流向量计算公式，其中$\circ$表示向量元素对应相乘（Hadamard积），$S_{SW}$为开关状态向量（1/0数值），$\bar{S}_{SW}$为其按位取反向量。*


**公式6**: $$$$\begin{cases} I_{inj,L} = A_{nb,L} I_{h,L} \\ I_{inj,C} = A_{nb,C} I_{h,C} \\ I_{inj,SW} = A_{nb,SW} I_{h,SW} \\ I_{inj,SC} = -A_{nb,SC} I_s \\ I_{inj} = I_{inj,L} + I_{inj,C} + I_{inj,SW} + I_{inj,SC} \end{cases}$$$$

*节点注入电流计算，通过关联矩阵与各支路历史电流向量相乘获得，体现网络拓扑连接关系。*


**公式7**: $$$$V_n = Y^{-1} I_{inj}$$$$

*节点电压求解公式，其中$Y^{-1}$为系统导纳矩阵的逆矩阵，在初始化阶段离线计算并作为固定参数输入。*


**公式8**: $$$$\begin{cases} V_{b,R} = A_{bn,R} V_n \\ V_{b,L} = A_{bn,L} V_n \\ V_{b,C} = A_{bn,C} V_n \\ V_{b,SW} = A_{bn,SW} V_n \end{cases}$$$$

*各类型支路电压更新公式，通过关联矩阵将节点电压映射为支路电压。*


**公式9**: $$$$\begin{cases} I_{b,R} = Y_{b,R} \circ V_{b,R} \\ I_{b,L} = Y_{b,L} \circ V_{b,L} + I_{h,L} \\ I_{b,C} = Y_{b,C} \circ V_{b,C} + I_{h,C} \\ I_{b,SW} = Y_{b,SW} \circ V_{b,SW} + I_{h,SW} \end{cases}$$$$

*各类型支路电流更新公式，基于支路自导纳向量与支路电压的Hadamard积加上历史电流项。*


**公式10**: $$$$\begin{cases} \dot{\omega} = \frac{1}{T_a} [K_p(\omega_{\text{ref}} - \omega) + P_{\text{ref}} - P_{\text{out}} - K_d(\omega - \omega_0)] \\ \dot{\delta} = \omega \end{cases}$$$$

*虚拟同步发电机(VSG)有功-频率调节方程（转子运动方程），其中$T_a$为虚拟惯性时间常数，$K_p$为有功下垂系数，$K_d$为阻尼系数，$\omega$为虚拟转子角速度，$\delta$为功角。*


**公式11**: $$$$V^* = V_{\text{ref}} + K_q(Q_{\text{ref}} - Q_{\text{out}})$$$$

*虚拟同步发电机无功-电压下垂控制方程，其中$K_q$为无功下垂控制系数，$V^*$为内层控制电压参考值。*


### 算法步骤

1. 初始化计算（离线执行）：根据拓扑结构计算系统导纳矩阵$Y$及其逆矩阵$Y^{-1}$；提取各支路类型自导纳向量集合$\{Y_b\}$；构建以行为节点、列为支路的关联矩阵$\{A_{nb}\}$（用于计算节点注入电流）和以行为支路、列为节点的关联矩阵$\{A_{bn}\}$（用于计算支路电压）；确定广义ADC开关模型最优参数$\alpha_{\text{on}}$和$\beta_{\text{off}}$。

2. 实时仿真主循环步骤1（计算历史电流）：根据支路类型并行计算各支路历史电流向量集合$\{I_h\}$。对电感支路：$I_{h,L}=I_{b,L}$；对电容支路：$I_{h,C}=-Y_{b,C}\circ V_{b,C}$；对开关支路：根据当前开关状态向量$S_{SW}$，利用公式(6)计算$I_{h,SW}$，实现恒导纳建模。

3. 实时仿真主循环步骤2（计算节点注入电流）：利用关联矩阵与历史电流向量进行矩阵乘法运算，按支路类型并行计算各分量$I_{inj,L}=A_{nb,L}I_{h,L}$等，最终叠加得到总节点注入电流$I_{inj}=\sum I_{inj,type}$。

4. 实时仿真主循环步骤3（计算节点电压）：执行矩阵向量乘法$V_n=Y^{-1}I_{inj}$，求解所有节点电压。由于$Y^{-1}$已预先计算，此步骤仅需一次矩阵向量乘法。

5. 实时仿真主循环步骤4（更新支路电压）：利用关联矩阵$A_{bn}$，通过矩阵运算$V_b=A_{bn}V_n$并行更新各类型支路（R、L、C、SW）的电压向量。

6. 实时仿真主循环步骤5（更新支路电流）：对各支路类型分别执行$I_b=Y_b\circ V_b+I_h$（对R支路无历史电流项），计算当前时步各支路电流。

7. 实时仿真主循环步骤6（数据交互与循环控制）：FPGA将采集的电气观测量（逆变器出口电流$i_{oabc}$、滤波后电压$u_{abc}$、电流$i_{abc}$）通过PXIe总线传输给CPU；接收CPU下发的PWM调制波$m_{\text{pwm}}$控制开关状态；返回步骤1继续下一时步仿真。


### 关键参数

- **FPGA仿真步长**: 1 μs

- **CPU控制步长**: 100 μs

- **上位机交互周期**: 500 μs

- **FPGA硬件型号**: NI PXIe-7975R (Kintex-7 XC7K410T)

- **CPU型号**: NI PXIe-8135

- **电压基准值**: 380 V

- **功率基准值**: 65 kVA

- **直流侧电压**: 750 V

- **虚拟惯性时间常数Ta**: 2 p.u.

- **阻尼系数Kd**: 100 p.u.

- **有功下垂系数Kp**: 100 p.u.

- **无功下垂系数Kq**: 3 p.u.



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 虚拟同步并网逆变器稳态运行 | 在CPU-FPGA异构平台上实现的小步长实时仿真（1μs步长）与Simulink离线仿真结果高度吻合，验证了优化EMTP算法的准确性。FPGA资源消耗分析表明所提算法有效利用了并行计算资源。 | 与Simulink离线仿真对比，波形一致性高，验证了算法的准确性；相比传统CPU串行EMTP算法，通过FPGA并行化实现了≤2μs的小步长实时仿真，突破了单一CPU的计算瓶颈。 |



## 量化发现

- FPGA电路仿真步长达到1 μs，满足电力电子器件小步长（≤2 μs）电磁暂态实时仿真需求
- CPU控制部分采用100 μs大步长，与FPGA的1 μs小步长形成100:1的异构时间尺度配合
- 上位机人机界面交互时间尺度为500 μs，满足观测需求且不占用实时计算资源
- 采用广义ADC开关模型后，开关动作前后系统导纳矩阵维持不变，避免了传统方法中每次开关动作需更新导纳矩阵的高额计算开销
- 通过支路拆分并行处理，将传统EMTP的串行遍历计算转化为向量/矩阵并行运算，显著提升了FPGA计算效率
- 定点数据类型下，各支路类型可分别选用合适的数据长度，减少了计算资源消耗和计算时间


## 关键公式

### 广义ADC开关模型历史电流方程

$$$$I_{h,i} = \begin{cases} \alpha_{\text{on}} Y_{\text{SW}} V_{b,i} + I_{b,i}, & S_i = \text{on} \\ -Y_{\text{SW}} V_{b,i} + \beta_{\text{off}} I_{b,i}, & S_i = \text{off} \end{cases}$$$$

*用于FPGA中小步长实时仿真的开关建模，确保开关动作时导纳矩阵恒定，避免实时更新矩阵，同时通过优化参数减少开关虚拟损耗。*

### 节点电压求解方程

$$$$V_n = Y^{-1} I_{inj}$$$$

*优化EMTP算法的核心步骤，通过预先离线计算导纳矩阵逆矩阵$Y^{-1}$，将实时仿真中的矩阵求逆转化为简单的矩阵向量乘法，满足实时性要求。*

### 虚拟同步发电机转子运动方程

$$$$\dot{\omega} = \frac{1}{T_a} [K_p(\omega_{\text{ref}} - \omega) + P_{\text{ref}} - P_{\text{out}} - K_d(\omega - \omega_0)]$$$$

*CPU控制部分实现虚拟同步控制(VSG)的核心方程，模拟同步发电机的惯性和阻尼特性，用于生成逆变器的PWM调制参考信号。*



## 验证详情

- **验证方式**: 对比验证：将基于CPU-FPGA异构平台的实时仿真结果与Simulink离线仿真结果进行对比分析，同时分析平台实时性能与FPGA资源消耗。
- **测试系统**: 虚拟同步并网逆变器系统，包含三相逆变器、LC滤波器、并网阻抗及电网，采用虚拟同步发电机控制策略，功率等级65kVA，电压等级380V/50Hz。
- **仿真工具**: 基准对比工具：MATLAB/Simulink（离线电磁暂态仿真）；实时仿真平台：NI-PXI系统（包含PXIe-8135 CPU控制器和PXIe-7975R FPGA模块）。
- **验证结果**: 实时仿真波形与Simulink离线仿真结果高度吻合，验证了基于所提平台实现虚拟同步并网逆变器系统实时仿真的准确性与有效性；FPGA资源消耗分析表明优化后的EMTP算法有效利用了硬件并行计算能力，实现了1μs步长的实时仿真。
