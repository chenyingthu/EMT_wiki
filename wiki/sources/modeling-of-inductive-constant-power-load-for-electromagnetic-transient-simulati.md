---
title: "Modeling of inductive constant power load for electromagnetic-transient simulations–Part II"
type: source
authors: ['Kamel Alboaouh']
year: 2025
journal: "Electric Power Systems Research, 242 (2025) 111415. doi:10.1016/j.epsr.2025.111415"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/26/Alboaouh 等 - 2025 - Modeling of inductive constant power load for electromagnetic-transient simulations–Part II.pdf"]
---

# Modeling of inductive constant power load for electromagnetic-transient simulations–Part II

**作者**: Kamel Alboaouh
**年份**: 2025
**来源**: `26/Alboaouh 等 - 2025 - Modeling of inductive constant power load for electromagnetic-transient simulations–Part II.pdf`

## 摘要

Modeling of inductive constant power load for electromagnetic-transient a Dept.of Eng.Tech, Norfolk State Univ., 700 Park Ave,RTC Building,Suite 420M, Norfolk VA 23501, USA b Power Syst.Eng.Center, Nat.Renewable Energy Lab., Golden CO, USA c Power Syst.Eng.Center, Nat. Renewable Energy Lab., Golden CO,USA This paper improves the dynamic constant power (CP) load model that was published in Part I, which is

## 核心贡献


- 提出逐时间步求解的恒功率负载模型，克服原模型需整周期计算的求解器集成障碍。
- 引入虚拟变量实现RMS量递归更新，使模型严格适配EMT仿真器的步进计算机制。
- 保留感性负载固定功率与功率因数约束，同时兼容正弦与非正弦电网运行工况。


## 使用的方法


- [[数值建模|数值建模]]
- [[逐时间步求解|逐时间步求解]]
- [[基尔霍夫定律|基尔霍夫定律]]
- [[递归rms量计算|递归RMS量计算]]
- [[恒阻抗负载合成验证|恒阻抗负载合成验证]]


## 涉及的模型


- [[恒功率负载|恒功率负载]]
- [[恒阻抗负载|恒阻抗负载]]
- [[感性rl电路|感性RL电路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[负荷建模|负荷建模]]
- [[恒功率负载|恒功率负载]]
- [[数值求解器集成|数值求解器集成]]
- [[固定功率因数|固定功率因数]]


## 主要发现


- 仿真验证表明模型可无缝嵌入EMT数值求解器，实现单步迭代且计算逻辑稳定。
- 在正弦与非正弦工况下，模型均能精确维持预设的有功功率消耗与固定功率因数。
- 与恒阻抗负载合成数据对比结果高度吻合，证实了模型在动态暂态过程中的准确性。



## 方法细节

### 方法概述

本文提出了一种改进的感性恒功率（CP）负载模型，通过引入虚拟变量（dummy variables）实现RMS量的递归更新，解决了Part I模型需整周期计算无法嵌入EMT数值求解器的问题。核心思想是将RMS的历史累积计算分解为前一步的累积值（虚拟变量）与当前瞬时值平方和的形式，使模型能在每个时间步独立求解。该方法基于恒阻抗（CI）负载与恒功率负载在相同电压和功率下的电流等价性，利用基尔霍夫定律（KCL/KVL）建立瞬时量关系，并通过功率约束方程（固定有功功率P和固定功率因数pf）求解当前时刻的电流值。模型适用于正弦和非正弦工况，因其完全基于时域瞬时量计算。

### 数学公式


**公式1**: $$$N = \{1, 2, \dots, k, \dots, n, \dots\}$$$

*定义采样时间索引集合，n表示当前时间步*


**公式2**: $$$(i_{rms})^2_n = \sum_{k=1, k\in N}^{k=n} (i_{tk})^2$$$

*传统RMS电流定义，基于一个周期内所有采样点的平方和*


**公式3**: $$$pf \cdot i_{rms} \cdot v_{rms} = P$$$

*功率因数定义，关联有功功率P、视在功率和功率因数pf*


**公式4**: $$$\forall k \in N: i_{tk} = i_{Rtk} = i_{Ltk}$$$

*KCL定律：RL串联电路中电流处处相等*


**公式5**: $$$\forall k \in N: v_{tk} = v_{Rtk} + v_{Ltk}$$$

*KVL定律：总电压等于电阻电压与电感电压之和*


**公式6**: $$$(v_{Rrms})^2_n = (v_{Rtn})^2 + V_{Rn-1}$$$

*递归RMS计算核心方程：当前RMS平方等于当前瞬时电压平方加前一步虚拟变量*


**公式7**: $$$(v_{Lrms})^2_n = (v_{Ltn})^2 + V_{Ln-1}$$$

*电感电压RMS的递归计算*


**公式8**: $$$(i_{rms})^2_n = (i_{tn})^2 + I_{n-1}$$$

*电流RMS的递归计算*


**公式9**: $$$V_{Rn-1} = \sum_{k=1, k\in N}^{k=n-1} (v_{Rtk})^2$$$

*虚拟变量定义：前n-1步电阻电压平方的累积和*


**公式10**: $$$P_n = i_{rmsn} \cdot v_{Rrmsn}$$$

*有功功率约束：RMS电流与RMS电阻电压的乘积等于设定功率*


**公式11**: $$$pf_n \cdot v_{rmsn} = v_{Rrmsn}$$$

*功率因数约束：电阻电压与总电压的比值等于功率因数*


**公式12**: $$$Q_n = i_{rmsn} \cdot v_{Lrmsn}$$$

*无功功率计算：RMS电流与RMS电感电压的乘积*


### 算法步骤

1. 初始化：设置虚拟变量 $V_{R0} = 0$, $V_{L0} = 0$, $I_0 = 0$，设定目标有功功率P和固定功率因数pf

2. 时间步循环：对于每个时间步n=1,2,3...执行以下计算

3. 测量瞬时电压：获取当前时刻总电压瞬时值 $v_{tn}$（由电网状态决定）

4. 建立约束方程：根据功率约束 $P = i_{rmsn} \cdot v_{Rrmsn}$ 和 $pf = v_{Rrmsn}/v_{rmsn}$，结合KVL关系

5. 求解瞬时电流：利用递归公式 $(i_{rms})^2_n = (i_{tn})^2 + I_{n-1}$ 和电压关系，求解当前时刻电流 $i_{tn}$

6. 分解电压：计算电阻电压 $v_{Rtn}$ 和电感电压 $v_{Ltn}$，满足 $v_{tn} = v_{Rtn} + v_{Ltn}$ 和功率因数约束

7. 更新RMS值：计算当前步 $(v_{Rrms})^2_n = (v_{Rtn})^2 + V_{Rn-1}$，同理计算 $(v_{Lrms})^2_n$ 和 $(i_{rms})^2_n$

8. 更新虚拟变量：为下一步准备，$V_{Rn} = V_{Rn-1} + (v_{Rtn})^2$，$V_{Ln} = V_{Ln-1} + (v_{Ltn})^2$，$I_n = I_{n-1} + (i_{tn})^2$

9. 输出电流：将计算得到的 $i_{tn}$ 作为当前时间步的负载电流注入EMT求解器

10. 周期重置（可选）：当达到一个完整周期时，可选择重置虚拟变量以消除数值累积误差


### 关键参数

- **P**: 有功功率设定值（W），恒定

- **pf**: 功率因数（固定值，感性负载通常滞后）

- **v_{tn}**: 当前时间步总电压瞬时值（由电网决定）

- **V_{Rn-1}, V_{Ln-1}, I_{n-1}**: 虚拟变量，存储前n-1步的累积平方和

- **Δt**: EMT仿真时间步长（由求解器决定）

- **i_{tn}**: 待求解的当前时间步电流瞬时值



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 恒阻抗负载合成数据对比验证 | 将提出的CP负载模型响应与基于恒阻抗（CI）负载合成的参考数据进行对比，验证模型在维持固定功率消耗方面的准确性。测试涵盖正弦电压工况下的瞬态响应。 | CP模型输出与CI合成数据高度吻合，证实了递归RMS计算方法的有效性 |

| 非正弦工况验证 | 在包含谐波分量的非正弦电压波形下测试模型性能，验证模型对非正弦系统的适应性。 | 模型成功维持预设功率和功率因数，克服了传统P/V除法方法在非正弦系统中的局限性 |



## 量化发现

- 模型实现了严格的逐时间步求解（time-step by time-step solution），消除了Part I模型需整周期（one-cycle）批量计算的约束
- 通过引入虚拟变量，RMS计算从历史全周期求和转换为递归更新，计算复杂度从O(N) per cycle降至O(1) per time-step
- 模型严格维持固定功率因数（fixed-PF）约束，功率因数偏差在仿真过程中保持为零
- 适用于非正弦系统（non-sinusoidal case studies），可处理含谐波分量的电压波形
- 模型与EMT数值求解器完全兼容，支持单步迭代（single-step iteration）集成


## 关键公式

### 递归RMS电阻电压方程

$$$(v_{Rrms})^2_n = (v_{Rtn})^2 + V_{Rn-1}$$$

*核心创新方程，允许在每个时间步更新RMS值而无需存储整个周期的历史数据，其中$V_{Rn-1} = \sum_{k=1}^{n-1} (v_{Rtk})^2$为虚拟变量*

### 有功功率约束方程

$$$P_n = i_{rmsn} \cdot v_{Rrmsn}$$$

*恒功率负载的核心约束，确保在任何时刻RMS电流与RMS电阻电压的乘积等于设定的有功功率*

### 固定功率因数约束

$$$pf_n \cdot v_{rmsn} = v_{Rrmsn}$$$

*确保负载功率因数恒定，关联总电压RMS与电阻电压RMS*



## 验证详情

- **验证方式**: 对比验证（Comparison with synthesized data）
- **测试系统**: 基于恒阻抗（CI）RL负载合成的参考系统，用于生成对比基准数据
- **仿真工具**: 理论模型验证提及适用于PSCAD、LTspice、Matlab-Simulink、PSSE等EMT仿真环境，具体实现未指定特定软件版本
- **验证结果**: 提出的CP负载模型与CI合成数据对比结果满意（satisfactory），证实了模型在维持固定功率消耗和固定功率因数方面的准确性。模型成功实现了与EMT数值求解器的逐步集成（step-by-step integration），适用于正弦和非正弦工况。
