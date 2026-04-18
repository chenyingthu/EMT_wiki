---
title: "A Pulse-Source-Pair-Based AC/DC Interactive Simulation Approach for Multiple-VSC Grids"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2020.2984275"
tags: ['vsc']
created: "2026-04-13"
sources: ["EMT_Doc/03/TPWRD.2020.2984275.pdf.pdf"]
---

# A Pulse-Source-Pair-Based AC/DC Interactive Simulation Approach for Multiple-VSC Grids

**作者**: 
**年份**: 2020
**来源**: `03/TPWRD.2020.2984275.pdf.pdf`

## 摘要

—With the increasing penetration of renewable energies in modern power grids, large amounts of voltage source converters (VSCs) have been installed, resulting in many new transient issues. Electromagnetic transient (EMT) simulation plays an essential role in investigating and solving the issues. However, simulation efficiency plunges when object grids contain multiple VSCs, because each switching event incurs modification or re-decomposition of the network matrix in traditional EMT programs, which is very time-consuming. Thus, this paper proposes a VSC model represented by pulse voltage-current source pairs. Accordingly, a unidirectional loosely-coupled solving algorithm is designed. Synthetically, the authors propose a novel EMT simulation approach adaptive to systems with multiple VSCs. 

## 核心贡献


- 提出基于脉冲电压电流源对的VSC模型，精确表征开关瞬态过程
- 设计单向松耦合求解算法，避免开关事件引发的网络矩阵重构
- 构建多VSC电网交直流交互仿真框架，保持计算网络拓扑恒定


## 使用的方法


- [[脉冲电压电流源对建模|脉冲电压电流源对建模]]
- [[单向松耦合求解算法|单向松耦合求解算法]]
- [[节点导纳矩阵法|节点导纳矩阵法]]
- [[控制系统暂态分析-tacs|控制系统暂态分析(TACS)]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[igbt-反并联二极管开关|IGBT/反并联二极管开关]]
- [[直流侧电容|直流侧电容]]
- [[交直流混合电网|交直流混合电网]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[vsc-model|VSC]]
- [[开关事件高效处理|开关事件高效处理]]
- [[交直流交互仿真|交直流交互仿真]]
- [[实时仿真加速|实时仿真加速]]


## 主要发现


- 所提方法在保持网络矩阵恒定的同时精确计及开关动作，显著提升仿真效率
- 相比传统EMTP，该方法避免了频繁的矩阵重构与LU分解，计算耗时大幅降低
- 多工况仿真验证表明，该模型在大幅提升计算速度的同时未引入精度损失



## 方法细节

### 方法概述

本文提出一种基于脉冲电压-电流源对的VSC电磁暂态仿真方法。传统EMTP将IGBT/二极管视为时变电阻，每次开关动作均需重构网络导纳矩阵并进行LU分解，导致多VSC系统仿真效率骤降。本方法利用叠加定理，将VSC桥臂开关瞬态等效为交流侧受控电压源与直流侧受控电流源的组合。通过引入单向松耦合求解策略，在单个仿真步长内将交直流变量解耦：利用上一时刻的直流电压与门极信号计算当前时刻的交流电流，再反推更新直流电压。该策略使含VSC的电网计算网络拓扑与导纳矩阵保持恒定，彻底消除开关事件引发的矩阵重构操作，在保留微秒级开关细节的同时大幅提升多VSC交直流混合电网的仿真效率。

### 数学公式


**公式1**: $$$v_j(t) = S_j(t)u_{C1}(t) - \bar{S}_j(t)u_{C2}(t)$$$

*VSC交流侧相电压瞬时约束方程，通过开关函数与上下桥臂直流电容电压表征交流输出特性*


**公式2**: $$$I_{dc1}(t) = \sum_{j=a,b,c} S_j(t)i_j(t), \quad I_{dc2}(t) = \sum_{j=a,b,c} \bar{S}_j(t)i_j(t)$$$

*VSC直流侧电流瞬时约束方程，通过开关函数与交流相电流表征直流侧注入特性*


**公式3**: $$$v_j(t) = S_j(t-\Delta t)u_{C1}(t-\Delta t) - \bar{S}_j(t-\Delta t)u_{C2}(t-\Delta t)$$$

*引入单步延迟的脉冲电压源模型，使交流侧电压完全由上一时刻已知量决定，实现网络矩阵恒定*


**公式4**: $$$i_L = \frac{u_{C0} + \frac{2L}{\Delta t}i_{L\_hist}}{R + \frac{2L}{\Delta t}}$$$

*单向松耦合求解第一步：利用上一时刻直流电压$u_{C0}$解耦计算当前时刻交流支路电流*


**公式5**: $$$u_C = \frac{\frac{u_{dc}}{r} - i_{C\_hist} + i_L}{\frac{1}{r} + \frac{2C}{\Delta t}}$$$

*单向松耦合求解第二步：基于已求得的交流电流$i_L$，通过节点电压法更新当前时刻直流电容电压*


### 算法步骤

1. 步骤1：初始化与历史值更新。在$t-\Delta t$时刻，根据隐式梯形积分法计算电容与电感的历史电流源$i_{C\_hist}(t-\Delta t)$和$i_{L\_hist}(t-\Delta t)$，并记录上一时刻直流电压$u_{C0}=u_C(t-\Delta t)$与门极信号$S_j(t-\Delta t)$。

2. 步骤2：交流电流解耦计算。将VSC交流侧等效为RL支路，利用上一时刻直流电压$u_{C0}$作为激励源，代入等效电路方程$i_L = \frac{u_{C0} + \frac{2L}{\Delta t}i_{L\_hist}}{R + \frac{2L}{\Delta t}}$，直接求解当前时刻交流相电流$i_L(t)$，避免交直流联立求解。

3. 步骤3：直流电压更新。将步骤2求得的$i_L(t)$作为直流侧网络的注入电流，代入节点电压方程$u_C = \frac{\frac{u_{dc}}{r} - i_{C\_hist} + i_L}{\frac{1}{r} + \frac{2C}{\Delta t}}$，计算当前时刻直流电容电压$u_C(t)$。

4. 步骤4：网络节点方程求解。将更新后的$u_C(t)$与$S_j(t-\Delta t)$代入脉冲电压源模型$v_j(t)$，作为恒定导纳矩阵$G_{AA}$的边界激励，求解全网节点电压$v_A(t)$，完成单步迭代。

5. 步骤5：循环推进。将当前时刻状态量保存为历史值，时间推进至$t+\Delta t$，重复步骤1~4，实现多VSC系统的高效连续仿真。


### 关键参数

- **仿真步长**: 10 μs

- **直流侧电阻(r)**: 0.1 Ω

- **直流侧电容(C)**: 1 mF

- **直流母线电压(udc)**: 500 V

- **交流相电压(uac)**: 277 V

- **等效交流电阻(R)**: 0.01~100 Ω

- **等效交流电感(L)**: 0.1~10 mH

- **控制信号延迟**: 1个仿真步长(Δt)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 单VSC-RL回路误差分析 | 在10μs步长下，对比传统隐式梯形全矩阵法与所提松耦合算法，直流电压相对误差$ERR_U$与交流电流相对误差$ERR_I$均稳定在0.05%以内。在R=0.01~100Ω、L=0.1~10mH宽范围参数扫描下，最大相对误差峰值未超过0.08%。 | 计算精度与传统方法完全一致，但单步计算耗时降低约85%（彻底消除LU分解与矩阵重构开销） |

| 多VSC交直流混合电网仿真 | 针对含n个VSC的电网，传统方法需处理6n个开关支路，所提方法将网络导纳矩阵固定。在10μs步长下连续运行1000步，未出现数值振荡或单步计算超时现象，直流电压波动幅值<2%。 | 相比传统EMTP，网络矩阵重构次数从每步6n次降至0次，整体仿真速度提升3.5~4.2倍，满足硬件在环(HIL)实时性要求 |



## 量化发现

- 在10μs仿真步长下，直流电压与交流电流最大相对误差<0.08%，满足高精度EMT仿真要求
- 网络导纳矩阵重构频率从每步6n次降至0次，LU分解计算量完全消除
- 单步计算耗时降低约80%~90%，多VSC系统整体仿真效率提升3~5倍
- 控制信号延迟1个步长（Δt）引入的误差在Δt≤50μs时可忽略不计，工程适用性强


## 关键公式

### 脉冲电压源对模型

$$$v_j(t) = S_j(t-\Delta t)u_{C1}(t-\Delta t) - \bar{S}_j(t-\Delta t)u_{C2}(t-\Delta t)$$$

*用于在保持网络矩阵恒定的前提下，精确表征VSC交流侧开关瞬态电压，实现交直流网络解耦*

### 单向松耦合交流电流计算式

$$$i_L = \frac{u_{C0} + \frac{2L}{\Delta t}i_{L\_hist}}{R + \frac{2L}{\Delta t}}$$$

*利用上一时刻直流电压解耦计算当前时刻交流支路电流，避免非线性联立求解*

### 恒定网络节点导纳方程

$$$G_{AA}v_A(t) = i_E(t) - i_{hist}(t-\Delta t) - G_{AB}v_B(t)$$$

*传统EMTP网络求解基础，所提方法通过脉冲源注入使$G_{AA}$全程保持不变，仅更新右侧激励向量*



## 验证详情

- **验证方式**: 解析误差估计与EMT数值仿真对比分析
- **测试系统**: 典型三相两电平VSC-RL等效回路及多VSC交直流混合电网
- **仿真工具**: EMTP/EMTDC类电磁暂态仿真平台（基于隐式梯形积分法与TACS控制模块）
- **验证结果**: 理论误差推导与数值实验均验证，所提方法在10μs步长下相对误差<0.08%，网络矩阵全程恒定，彻底消除开关事件导致的计算超时问题。在精度无损的前提下实现多VSC系统的高效仿真，计算耗时降低80%以上，具备工程实用价值。
