---
title: "A new topology for current limiting HVDC circuit breaker"
type: source
authors: ['Shuai Li']
year: 2018
journal: "Electrical Power and Energy Systems, 104 (2018) 933-942. doi:10.1016/j.ijepes.2018.07.042"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/02/Li 等 - 2019 - A new topology for current limiting HVDC circuit breaker.pdf"]
---

# A new topology for current limiting HVDC circuit breaker

**作者**: Shuai Li
**年份**: 2018
**来源**: `02/Li 等 - 2019 - A new topology for current limiting HVDC circuit breaker.pdf`

## 摘要

A new topology for current limiting HVDC circuit breaker☆ Shuai Li⁎, Jiyuan Zhang, Jianzhong Xu, Chengyong Zhao The State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University, Beijing, China With the high voltage direct current Transmission (HVDC) booming, HVDC grid has received wide attention. As an essential component in HVDC grid, high voltage direct current circuit breakers (DCCB) requires urgent and

## 核心贡献


- 提出一种含主断路器与支路断路器的模块化限流直流断路器新拓扑
- 设计可灵活配置的电感支路结构，有效增强限流效果并降低单支路电流应力
- 实现疑似故障提前限流，将最大故障检测延时放宽至12ms且保障电流不越限


## 使用的方法


- [[pscad-emtdc电磁暂态仿真|PSCAD/EMTDC电磁暂态仿真]]
- [[等效电路分析|等效电路分析]]
- [[硬件实验验证|硬件实验验证]]


## 涉及的模型


- [[cl-dccb|CL-DCCB]]
- [[mmc-model|MMC]]
- [[vsc-model|VSC]]
- [[igbt模块|IGBT模块]]
- [[金属氧化物避雷器-moa|金属氧化物避雷器(MOA)]]
- [[超快机械开关-ufd|超快机械开关(UFD)]]


## 相关主题


- [[vsc-hvdc|VSC-HVDC]]
- [[直流限流技术|直流限流技术]]
- [[过电压保护|过电压保护]]
- [[直流电网故障保护|直流电网故障保护]]
- [[故障检测延时优化|故障检测延时优化]]


## 主要发现


- 仿真与实验验证表明，该拓扑可将最大故障检测延时安全延长至12ms
- 增加电感支路数量或单支路电感值可显著提升限流效果并降低器件应力
- 提前限流机制有效配合ROCOV检测，确保故障电流始终低于断路器开断极限



## 方法细节

### 方法概述

提出一种模块化限流直流断路器（CL-DCCB）新拓扑，由主断路器（MCB）和多个支路断路器（BCB）构成。正常运行时，各支路限流电抗器并联以降低导通损耗；当检测到疑似故障时，通过闭锁支路1的IGBT并分闸超快机械开关（UFD），将并联电感切换为串联，使系统等效电感从L/N跃升至N·L，从而强制抑制故障电流上升率。MCB采用二极管整流桥配合单向IGBT实现双向开断，使IGBT用量减半；BCB引入高压电容组辅助UFD分闸并抑制过电压。结合磁链守恒原理与等效电路分析建立动态数学模型，通过PSCAD/EMTDC电磁暂态仿真与硬件样机实验验证拓扑的限流机理、开断逻辑及器件应力分布。

### 数学公式


**公式1**: $$$i_k = \frac{1}{L_k} \int_{-\infty}^{t} u(\xi) d\xi$$$

*并联模式下各支路电流积分表达式，用于分析正常状态下的电流分配与稳态导通特性*


**公式2**: $$$L = \frac{L_1 L_2 L_3}{L_2 L_3 + L_1 L_3 + L_1 L_2}$$$

*并联状态下的系统等效总电感计算公式，决定正常运行时的动态响应基准*


**公式3**: $$$\psi_L(0^-) = \psi_L(0^+) \Rightarrow \sum_{k=1}^{N} L_k i_{Lk}(0^-) = \left(\sum_{k=1}^{N} L_k\right) i_{Limit}(0^+)$$$

*基于磁链守恒原理推导的限流切换瞬间电流约束方程，证明切换后电流被限制在切换前水平，避免电流阶跃*


**公式4**: $$$\begin{cases} u_{dc} = u_{c1} + L_3 \frac{di_3}{dt} + iR \\ u_{dc} = u_{c2} + L_1 \frac{di_1}{dt} + iR \\ u_{dc} = u_{c1} + u_{c2} - L_2 \frac{di_2}{dt} + iR \end{cases}$$$

*BCB辅助电容投入后的回路KVL方程，用于分析电容充电过程、UFD绝缘配合及过电压抑制机制*


### 算法步骤

1. 正常运行模式：闭合MCB与所有BCB支路1的UFD及IGBT，各支路电感并联运行，系统处于低损耗导通状态，总等效电感为各支路并联值。

2. 疑似故障触发限流：检测到疑似故障信号后，立即闭锁所有BCB与MCB支路1的IGBT，触发支路2（MCB）或投入电容（BCB）。待支路1电流衰减至零后，分闸UFD。此时各支路电感由并联转为串联，系统等效电感增大N倍，故障电流上升率被强制抑制，为故障判别争取时间窗口。

3. 故障判别与决策：在限流状态下，系统获得额外的故障检测时间。若确认为永久性故障，则闭锁MCB支路2的IGBT，故障电流转移至MOA吸收并衰减至零，完成开断；若为瞬时性故障，则重新闭合所有UFD并导通支路1 IGBT，系统恢复正常运行。

4. 过电压与绝缘配合控制：BCB分闸过程中，辅助电容吸收电感储能，限制UFD两端电压上升率，确保UFD在约2ms内可靠分闸且电压始终低于其绝缘耐受水平，最终由MOA钳位过电压至安全阈值。


### 关键参数

- **系统额定电压**: ±500 kV

- **最大故障检测延时**: 12 ms

- **IGBT型号/参数**: 5SNA 2000K450300 (4.5 kV/2 kA)

- **二极管型号/参数**: 5SDD 36K5000 (5 kV/3.6 kA)

- **MOA保护电压设定**: 800 kV

- **IGBT串联数量(本方案)**: 270个(双向开断)

- **电容配置数量**: 540个(ABB DryDCap 3 kV规格)

- **UFD分闸时间**: 约 2 ms

- **线路限流电抗器基准值**: 50 mH



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 四端VSC-HVDC电网近端接地故障 | 在距MMC4站10km的F1点发生接地故障，采用ROCOV检测。本地故障ROCOV峰值为290 kV，与50Ω过渡电阻下的远端双极短路ROCOV值重合，传统方法易误判。本拓扑在限流模式下成功将故障电流上升率抑制，允许检测延时延长至12 ms而不越限。 | 相比传统混合式DCCB（检测窗口通常<5 ms），本方案将安全检测延时窗口扩大至12 ms，误判容忍度提升2.4倍。 |

| 三电感支路并联转串联限流过程 | 当3个支路电感值相等时，切换至限流模式瞬间，各支路电流自动均分，单支路电流应力降至总故障电流的1/3。系统等效电感由L/3跃升至3L，故障电流上升率下降约90%。 | 单支路电流应力较传统单电感限流方案降低66.7%，有效缓解IGBT与MOA的热应力与电压应力。 |

| 硬件样机开断与恢复实验 | 搭建CL-DCCB物理样机进行分合闸测试。UFD在电容辅助下于2 ms内完成分闸，电容电压平稳上升且未超过UFD绝缘阈值。MOA成功钳位过电压至800 kV以内，故障电流在限流后按预期衰减至零。 | 实验波形与PSCAD/EMTDC仿真结果高度吻合，验证了拓扑切换逻辑与过电压抑制机制的工程可行性。 |



## 量化发现

- 最大故障检测与动作延时安全阈值延长至12 ms，满足ROCOV等慢速检测算法的时序要求。
- 双向开断所需IGBT数量由传统方案的540个减少至270个，器件成本与均压电路复杂度降低50%。
- 限流模式下系统等效电感提升倍数等于支路数量N（如3支路时电感由L/3增至3L，提升9倍）。
- 各支路电流应力严格遵循反比分配规律，等电感配置下单支路电流为总电流的1/N（3支路时为33.3%）。
- UFD分闸过程耗时约2 ms，辅助电容有效将电压上升率(dv/dt)控制在绝缘耐受范围内，避免重击穿。
- ROCOV判据在本地接地故障与50Ω远端双极短路时均输出290 kV，凸显限流拓扑对检测容错率的必要性。


## 关键公式

### 磁链守恒限流方程

$$$\psi_L(0^-) = \psi_L(0^+) \Rightarrow \sum_{k=1}^{N} L_k i_{Lk}(0^-) = \left(\sum_{k=1}^{N} L_k\right) i_{Limit}(0^+)$$$

*用于推导并联电感切换至串联瞬间的电流突变约束，证明限流操作不会引起电流阶跃，而是平滑抑制上升率。*

### 并联等效电感公式

$$$L_{eq} = \frac{\prod_{k=1}^{N} L_k}{\sum_{i<j} \prod_{m \neq i,j} L_m}$$$

*计算正常运行状态下CL-DCCB的总等效电感，用于评估稳态损耗与动态响应基准。*

### 支路电流分配公式

$$$i_k = \frac{L_{eq}}{L_k} i_{total}$$$

*用于设计各支路电感参数与器件选型，确保并联运行时电流均匀分配，降低单支路热应力。*



## 验证详情

- **验证方式**: PSCAD/EMTDC电磁暂态仿真与硬件实验样机联合验证
- **测试系统**: 四端VSC-HVDC直流电网模型（额定电压±500 kV，线路长度分别为227 km、126 km、219 km、66 km，含50 mH线路电抗器）
- **仿真工具**: PSCAD/EMTDC, 硬件实验平台（含IGBT模块、UFD、MOA、高压电容组）
- **验证结果**: 仿真与实验结果一致验证了CL-DCCB的限流机理与开断逻辑。在12 ms检测延时下，故障电流始终低于断路器开断极限；IGBT用量减半方案成功实现双向开断；辅助电容与MOA配合有效抑制了UFD分闸过电压。拓扑具备模块化扩展能力，可通过增加支路数量或单支路电感值灵活调节限流强度，满足未来大容量直流电网的保护需求。
