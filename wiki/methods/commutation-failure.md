---
title: "Commutation Failure"
type: method
tags: [commutation-failure]
created: "2026-05-04"
---

# Commutation Failure

## 定义与边界

Commutation failure 指 LCC 或晶闸管逆变器在换相窗口内未能把电流从退出阀转移到进入阀，导致退出阀不能按预期恢复阻断能力的事件。本页作为英文受控入口，收拢 `commutation failure` 链接；详细模型边界应优先转向 [[lcc-model]]、[[extinction-angle-calculation]] 和多馈入场景页 [[concurrent-commutation-failure]]。

## 核心机制

换相失败的核心判据是关断角：

$$
\gamma = \arccos\left(\frac{\sqrt{2} k I_d X_L}{V_L} + \cos\beta\right) < \gamma_{\min}
$$

其中 $\gamma$ 为关断角，$I_d$ 为直流电流，$X_L$ 为换相电抗，$V_L$ 为换相线电压有效值，$\beta$ 为超前触发角，$k$ 为换相重叠相关的系数。当 $\gamma$ 低于晶闸管恢复阻断能力所需的最小关断角 $\gamma_{\min}$ 时，退出阀在正向电压作用下重新导通，导致换相失败。

## 适用边界与失败模式

- **valid_when**: LCC/晶闸管逆变器依赖交流电压换相的场景；换相电压、直流电流和触发角在正常范围内。
- **invalid_when**: VSC、MMC 或构网型变流器不存在换相失败问题；弱交流系统或严重不对称故障下关断角裕度急剧下降时判据可能失效。
- **assumptions**: 假设换相电抗和系统频率在换相窗口内保持不变（据方法推断）。
- **evidence_gaps**: 多馈入场景下各换流站之间的换相失败交互机理仍未统一建模；不同文献对 $\gamma_{\min}$ 的取值不同。

### 与相关页面的关系

## 概念边界

- 换相失败只适用于依赖交流电压换相的 LCC / 晶闸管系统，不应用来描述 VSC、MMC 或构网型变流器的限流、PLL 失稳或调制饱和。
- 单站换相失败的核心量是换相电压、直流电流、触发角、换相电感和关断角；多站传播与并发事件应转向 [[concurrent-commutation-failure]]。
- 平均值模型可以用于系统级筛查，但阀级电流、保护闭锁和器件应力仍需要详细 EMT 或明确的验证基线。
- 本页不保留无来源的精度、实时性、节点规模或通用性能数字。

## 链接用法

需要英文术语锚点时可链接 [[commutation-failure]]。讨论多馈入联动、负序电压影响或事件序列时优先链接 [[concurrent-commutation-failure]]；讨论单站关断裕度时链接 [[extinction-angle-calculation]]；讨论 LCC 设备模型时链接 [[lcc-model]]。

## 代表性来源

- [[average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail]]：支撑把换相失败检测嵌入 LCC 逆变器平均值模型的做法；其结论限定在原文 PAVM 和详细开关模型对比范围内。
- [[fast-detection-method-of-commutation-failure-based-on-multi-infeed-interaction-f]]：支撑在多馈入、不对称故障下考虑负序电压相位偏移的快速判别思路。
- [[a-multi-area-thevenin-equivalent-based-multi-rate-co-simulation-for-control-desi]]：可作为大规模 LCC-HVDC 控制设计与换相失败抑制的多速率仿真来源入口。

## 证据边界

本页只提供术语收敛和链接分流，不新增换相失败阈值、概率、关断角安全裕度或仿真加速结论。任何定量结论都必须绑定具体 LCC 系统、故障类型、控制策略、步长、仿真工具和对比基线。
