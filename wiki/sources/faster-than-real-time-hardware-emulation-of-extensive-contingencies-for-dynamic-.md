---
title: "Faster-Than-Real-Time Hardware Emulation of Extensive Contingencies for Dynamic Security Analysis of Large-Scale Integrated AC/DC Grid"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Transactions on Power Systems;2023;38;1;10.1109/TPWRS.2022.3161561"
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/Cao 等 - 2023 - Faster-Than-Real-Time Hardware Emulation of Extensive Contingencies for Dynamic Security Analysis of.pdf"]
---

# Faster-Than-Real-Time Hardware Emulation of Extensive Contingencies for Dynamic Security Analysis of Large-Scale Integrated AC/DC Grid

**作者**: 
**年份**: 2022
**来源**: `19、20、21/EMT_task_19/Cao 等 - 2023 - Faster-Than-Real-Time Hardware Emulation of Extensive Contingencies for Dynamic Security Analysis of.pdf`

## 摘要

—The rapid expansion of modern power systems has broughtatremendouscomputationalchallengetodynamicsecurity analysis (DSA) tools which consequently need to process extensive contingencies. In this work, hardware emulation is investigated to acceleratetheDSAsolutionofalarge-scaleAC/DCsystemdeployed on the ﬁeld-programmable gate arrays (FPGAs) faster-than-real- time (FTRT) execution. Electromagnetic transient (EMT) model- ing of the DC grid is conducted since the fast converter dynamics require a small time-step for accuracy; in contrast, the transient stability (TS) simulation is applicable to the AC grid which tolerates a much larger step size. To coordinate the 2 different types of simu- lation, an interface based on dynamic voltage injection is proposed to integrate the AC and DC grids, i

## 核心贡献


- 提出基于多FPGA的超实时硬件仿真平台用于大规模交直流电网动态安全分析
- 设计动态电压注入接口协调交直流混合仿真保持导纳矩阵恒定以降低延迟
- 采用显式RK4积分与九阶同步机模型针对FPGA并行架构优化求解效率


## 使用的方法


- [[电磁暂态仿真|电磁暂态仿真]]
- [[机电暂态仿真|机电暂态仿真]]
- [[多fpga并行计算|多FPGA并行计算]]
- [[动态电压注入接口|动态电压注入接口]]
- [[显式四阶龙格库塔法|显式四阶龙格库塔法]]
- [[混合仿真|混合仿真]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[九阶同步发电机模型|九阶同步发电机模型]]
- [[输电线路|输电线路]]
- [[变压器|变压器]]
- [[多端直流电网|多端直流电网]]
- [[换流器|换流器]]


## 相关主题


- [[动态安全分析|动态安全分析]]
- [[超实时仿真|超实时仿真]]
- [[硬件仿真|硬件仿真]]
- [[并行计算|并行计算]]
- [[交直流混合电网|交直流混合电网]]
- [[故障预想分析|故障预想分析]]


## 主要发现


- 平台实现交直流混合电网超实时加速比超208倍单系统加速比超277倍
- 成功完成超5500种故障预想分析安全指标与商业软件DSATools高度吻合
- 动态电压注入接口有效维持导纳矩阵恒定显著降低FPGA资源占用与延迟



## 方法细节

### 方法概述

提出一种基于多FPGA硬件的超实时（FTRT）动态安全分析（DSA）平台，用于大规模交直流混合电网的广域故障扫描。采用混合仿真架构：交流电网采用机电暂态（TS）仿真，步长设为1ms，使用显式四阶龙格-库塔（RK4）算法求解九阶同步机微分代数方程组，以适配FPGA并行架构并避免隐式迭代带来的收敛延迟；直流电网采用电磁暂态（EMT）建模，采用更小步长以精确捕捉换流器快速开关动态。为协调两种不同时间尺度的仿真，提出基于动态电压注入的交直流接口技术，在保持交流侧导纳矩阵恒定的前提下实现边界数据交换，显著降低硬件通信延迟与资源占用。系统通过合理的拓扑划分与资源分配部署于多块Xilinx VCU128 FPGA板上，实现全系统并行超实时推演与海量故障快速筛选。

### 数学公式


**公式1**: $$$$\dot{x}(t) = F(x, u, t)$$$$

*同步发电机状态变量的微分方程，描述机电暂态过程中的动态演化*


**公式2**: $$$$G(x, u, t) = 0$$$$

*交流网络代数方程，包含线路、变压器、负荷及并联电容的节点约束*


**公式3**: $$$$x_{n+1} = x_n + \frac{1}{6}(RK1 + 2RK2 + 2RK3 + RK4)$$$$

*显式四阶龙格-库塔（RK4）状态更新公式，用于FPGA高效并行积分*


**公式4**: $$$$Y_{Load} = \frac{P_{Load} + jQ_{Load}}{V_{Bus}^2}$$$$

*固定负荷与并联电容的等效导纳计算公式，用于构建交流网络导纳矩阵*


**公式5**: $$$$\dot{\delta}(t) = \omega_R \cdot \Delta\omega(t)$$$$

*同步发电机转子运动方程（机械部分），描述功角随转速偏差的变化*


### 算法步骤

1. 系统初始化与潮流计算：读取电网拓扑与参数，执行初始潮流求解，获取同步机初始状态向量x0、机械转矩Tm及励磁电压Efd，作为FPGA仿真的初始条件。

2. FPGA资源划分与模型映射：将大规模交直流系统按电气耦合强度进行拓扑分区，将交流TS模型与直流EMT模型分别映射至多块Xilinx VCU128 FPGA板，配置并行计算流水线。

3. 交流侧TS并行求解：在每个1ms仿真步长内，利用显式RK4算法并行计算所有同步机的9阶微分方程，结合恒定导纳矩阵求解网络代数方程，避免牛顿-拉夫逊迭代。

4. 直流侧EMT精细求解：在更小时间步长下执行换流器开关动态与直流网络电磁暂态计算，实时生成换流站端口电压与电流波形。

5. 动态电压注入接口交互：在交直流边界处，将直流侧计算得到的时变端口电压通过动态电压注入方式等效为交流侧的受控电压源，保持交流导纳矩阵结构不变，仅更新注入电流向量，实现跨时间尺度数据同步。

6. 故障注入与超实时扫描：在FPGA硬件中并行注入预设的N-1/N-2故障序列，连续执行FTRT推演，实时计算功角稳定裕度、电压越限等安全指标，输出>5500个故障场景的筛选结果。


### 关键参数

- **AC仿真步长**: 1 ms

- **同步机模型阶数**: 9阶（2机械+4电气+励磁系统）

- **FPGA硬件型号**: Xilinx VCU128

- **测试系统规模**: 6个ACTIVSg 500节点交流系统 + 6端直流电网

- **故障扫描数量**: >5500个

- **FTRT加速比(混合系统)**: >208倍

- **FTRT加速比(单500节点)**: >277倍

- **单FPGA承载能力**: 2个500节点系统/180台发电机



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 单ACTIVSg 500节点交流系统 | 在单块Xilinx VCU128 FPGA板上部署2个500节点系统（共180台发电机），执行机电暂态超实时推演，成功完成海量故障扫描，FTRT加速比达到277倍以上，动态轨迹与商业软件高度一致。 | 相比传统CPU集群近实时仿真，计算速度提升超过277倍，且单FPGA资源利用率优化，无需多机架扩展。 |

| 6×500节点互联交直流混合系统 | 部署于多FPGA平台，集成6个500节点交流网与6端直流电网，采用动态电压注入接口协调TS/EMT混合仿真。累计分析超过5500个故障场景，FTRT加速比稳定在208倍以上，安全指标实时输出。 | 相比传统基于潮流或隐式积分的DSA工具，在保持电磁-机电混合精度的前提下，实现超208倍的硬件加速，满足在线动态安全评估的时效性要求。 |



## 量化发现

- FTRT硬件仿真平台在交直流混合电网中实现>208倍的超实时加速比，在单一500节点系统中加速比>277倍。
- 单块Xilinx VCU128 FPGA可完整承载2个500节点系统（含180台九阶同步机），验证了FPGA架构在大规模电力系统并行仿真中的高资源密度优势。
- 平台累计完成>5500个故障场景的连续扫描与动态安全评估，满足NERC对大规模电网广域故障筛选的计算时效要求。
- 采用显式RK4积分与恒定导纳矩阵策略，避免了隐式迭代带来的收敛延迟，硬件流水线延迟显著降低，确保1ms步长下的确定性实时执行。


## 关键公式

### 显式四阶龙格-库塔状态更新方程

$$$$x_{n+1} = x_n + \frac{1}{6}(RK1 + 2RK2 + 2RK3 + RK4)$$$$

*用于FPGA硬件中同步发电机微分方程的高效并行积分，替代隐式迭代以消除收敛延迟*

### 负荷等效导纳方程

$$$$Y_{Load} = \frac{P_{Load} + jQ_{Load}}{V_{Bus}^2}$$$$

*构建交流网络恒定导纳矩阵，配合动态电压注入接口实现边界条件快速更新*

### 同步机转子运动方程

$$$$\dot{\delta}(t) = \omega_R \cdot \Delta\omega(t)$$$$

*九阶同步机模型的核心机械动态描述，用于评估暂态功角稳定性*



## 验证详情

- **验证方式**: 对比分析验证（硬件FTRT仿真结果与商业软件离线仿真结果交叉比对）
- **测试系统**: 6个ACTIVSg 500节点交流系统互联构成的3000节点级电网，通过6端直流电网耦合
- **仿真工具**: DSATools/TSAT（作为基准验证工具）
- **验证结果**: FTRT硬件仿真输出的动态响应曲线（功角、电压、频率）及安全评估指标与DSATools/TSAT结果高度吻合，验证了显式RK4积分、动态电压注入接口及多FPGA并行架构在保持高保真度的同时实现超实时计算的可行性与准确性。
