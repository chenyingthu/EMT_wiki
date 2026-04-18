---
title: "Advanced EMT and Phasor-Domain Hybrid Simulation With Simulation Mode Switching Capability for Transmission and Distribution Systems"
type: source
authors: ['未知']
year: 2018
journal: "IEEE Transactions on Power Systems;2018;33;6;10.1109/TPWRS.2018.2834561"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/06/Huang和Vittal - 2018 - Advanced EMT and Phasor-Domain Hybrid Simulation With Simulation Mode Switching Capability for Trans.pdf"]
---

# Advanced EMT and Phasor-Domain Hybrid Simulation With Simulation Mode Switching Capability for Transmission and Distribution Systems

**作者**: 
**年份**: 2018
**来源**: `06/Huang和Vittal - 2018 - Advanced EMT and Phasor-Domain Hybrid Simulation With Simulation Mode Switching Capability for Trans.pdf`

## 摘要

—Conventional electromagnetic transient (EMT) and phasor-domain hybrid simulation approaches presently exist for transmission system level studies. Their simulation efﬁciency is generally constrained by the EMT simulation. With an increasing number of distributed energy resources and nonconventional loads being installed in distribution systems, it is imperative to extend the hybrid simulation application to include distribution systems and integrated transmission and distribution systems. Meanwhile, it is equally important to improve the simulation efﬁciency as the modeling scope and complexity of the detailed system in the EMT simulation increases. To meet both requirements, this paper introduces an advanced EMT and phasor-domain hybrid simu- lation approach. This approach has two main f

## 核心贡献


- 提出适用于输配电及输配一体化系统的综合电磁暂态与相量域混合仿真框架
- 设计鲁棒的仿真模式切换机制，支持快动态平息后从混合模式平滑切回相量域
- 利用EMT捕获的离散事件协调双域模型状态，解决切换过程中的结果发散问题


## 使用的方法


- [[电磁暂态与相量域混合仿真|电磁暂态与相量域混合仿真]]
- [[仿真模式切换|仿真模式切换]]
- [[多区域戴维南等值|多区域戴维南等值]]
- [[相量域动态仿真|相量域动态仿真]]
- [[三相与序分量混合建模|三相与序分量混合建模]]


## 涉及的模型


- [[输配电网络|输配电网络]]
- [[分布式电源|分布式电源]]
- [[电力电子变换器|电力电子变换器]]
- [[单相感应电机|单相感应电机]]
- [[emt详细模型|EMT详细模型]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[输配电一体化|输配电一体化]]
- [[仿真模式切换|仿真模式切换]]
- [[计算效率优化|计算效率优化]]
- [[网络等值|网络等值]]


## 主要发现


- 引入模式切换机制后，总计算时间显著缩短，同时保持了较高的仿真精度
- 在输配电一体化系统测试中，快动态平息后切回相量域仿真有效提升了效率
- 协调策略成功解决了EMT与相量模型切换时的状态发散问题，验证了鲁棒性



## 方法细节

### 方法概述

本文提出一种适用于输配电及输配一体化系统的先进EMT-相量域混合仿真框架。核心创新在于引入鲁棒的仿真模式切换机制，在故障后快动态平息后，将混合仿真平滑切换回纯相量域动态仿真以突破EMT计算瓶颈。框架采用多区域戴维南等值（MATE）进行子系统交互，详细系统同时维护EMT与三相相量域模型。通过提取EMT仿真中的离散事件与控制信号（如电机堵转、换相失败）作为外部输入强制对齐相量模型状态，解决双域模型在切换点的发散问题。网络求解采用诺顿等值形式，边界交互通过三相/三序电压电流映射实现，支持正序、三序、三相及混合建模。

### 数学公式


**公式1**: $$$I(x, V) = YV$$$

*相量域动态仿真网络求解标准形式。用于将外部系统的三相诺顿等值导纳矩阵并入右侧导纳阵，诺顿电流源直接注入左侧向量，实现高效网络求解。*


**公式2**: $$$\max \left| \frac{dV_{boundary}}{dt} \right| < \epsilon_1$$$

*慢动态状态判据。用于切换控制器第一阶段，判断系统是否已脱离快动态暂态过程，进入可用相量模型准确表征的低频动态阶段。*


**公式3**: $$$\max \left| V_{de}^{abc}(t) - V_{ex}^{120}(t) \right| < \epsilon_2$$$

*双域边界收敛判据。用于切换控制器第二阶段，验证详细系统与外部系统边界条件是否真正收敛，确保切换后状态连续。*


### 算法步骤

1. 阶段1初始化：EMT与相量模型并行运行至故障前稳态，计算详细系统与外部系统的戴维南等值，通过虚拟断路器与MATE链路子系统互联。

2. 阶段2启动与数据上行：故障发生后，EMT侧提取边界三相瞬时波形，转换为三序电流注入向量$I_{EMT}^{120}(t)$，通过Socket发送至相量域仿真器。

3. 相量侧边界更新：相量仿真器接收$I_{EMT}^{120}(t)$作为输入，执行三序暂态稳定仿真，更新外部系统边界三序电压$V_{ex}^{120}(t+\Delta T)$。

4. 戴维南等值推导与下行：基于更新后的边界电压，推导三相戴维南等值电压$V_{T}^{abc}(t+\Delta T)$，并回传至EMT侧。

5. 诺顿等值转换：EMT侧将接收到的三相戴维南等值转换为三相诺顿等值，分离出等效导纳与电流源。

6. EMT网络求解：将诺顿导纳矩阵增广至详细系统导纳阵右侧，电流源注入左侧，执行多步EMT仿真直至下一交互时刻。

7. 切换控制器评估：在步骤7中，控制器依次检查时间延迟（0.2s）、边界电压变化率（<0.005 pu）及双域电压偏差（<0.005 pu持续3-5周期）。若全部满足，输出切换信号，阶段3启动纯相量仿真，EMT侧默认暂停。


### 关键参数

- **时间延迟阈值 $T_{Delay}$**: 0.2 s

- **边界电压最大变化率容差 $\epsilon_1$**: 0.005 pu

- **边界电压最大偏差容差 $\epsilon_2$**: 0.005 pu

- **收敛持续时间要求**: 3-5个工频周期

- **交互步长 $\Delta T$**: 相量域动态仿真步长（与TS步长一致）

- **负荷组成比例**: 50%单相空调压缩机负荷 + 50%恒定阻抗负荷



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 改进IEEE 9节点输配电一体化系统 | 在母线5接入含50%单相空调负荷的配电网。施加故障后，空调电机发生堵转。未传递离散信号时，相量模型误判两相堵转而EMT仅C相堵转；传递堵转状态信号后，双域模型在0.2s延迟后边界电压偏差收敛至<0.005 pu，成功触发模式切换。 | 相比全程运行混合仿真，总计算时间显著降低（论文验证切换机制可大幅缩短EMT计算窗口），且切换后相量域动态响应与EMT基准在慢动态阶段保持高度一致，边界电压误差控制在0.005 pu以内。 |



## 量化发现

- 切换控制器时间延迟设定为0.2 s以有效避开快动态暂态过程
- 边界电压最大变化率阈值严格设定为0.005 pu，确保系统进入慢动态
- 双域边界电压最大偏差阈值设定为0.005 pu，作为模式切换的硬性收敛指标
- 偏差需持续满足3-5个工频周期方可触发切换，防止暂态波动误触发
- 离散事件信号协调机制彻底消除因点波效应导致的堵转相数误判，使双域模型状态对齐误差降至工程可接受范围


## 关键公式

### 动态网络求解方程

$$$I(x, V) = YV$$$

*相量域动态仿真网络求解标准形式，用于将诺顿等值导纳并入右侧矩阵，电流源注入左侧*

### 慢动态状态判据

$$$\max \left| \frac{dV_{boundary}}{dt} \right| < \epsilon_1$$$

*切换控制器第一阶段，用于判断系统是否已脱离快动态暂态过程*

### 双域边界收敛判据

$$$\max \left| V_{de}^{abc}(t) - V_{ex}^{120}(t) \right| < \epsilon_2$$$

*切换控制器第二阶段，用于验证详细系统与外部系统边界条件是否真正收敛*



## 验证详情

- **验证方式**: 数字仿真对比分析
- **测试系统**: 改进的IEEE 9节点系统（母线5替换为含单相空调负荷的输配电一体化网络）
- **仿真工具**: PSCAD/EMTDC（EMT仿真器）、InterPSS（开源相量域仿真引擎）
- **验证结果**: 验证了所提混合仿真与模式切换机制的有效性。通过离散信号协调成功解决了EMT与相量模型在故障后状态不一致的问题，切换控制器在0.2s延迟及0.005 pu容差下准确触发模式切换，在保证仿真精度的同时显著提升了大规模输配电系统的计算效率。
