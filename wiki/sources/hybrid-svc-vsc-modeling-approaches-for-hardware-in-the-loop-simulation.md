---
title: "Hybrid SVC-VSC modeling approaches for hardware-in-the-loop simulation"
type: source
authors: ['P. Le-Huy']
year: 2023
journal: "Electric Power Systems Research, 223 (2023) 109651. doi:10.1016/j.epsr.2023.109651"
tags: ['vsc']
created: "2026-04-13"
sources: ["EMT_Doc/22/Le-Huy和Tremblay - 2023 - Hybrid SVC-VSC modeling approaches for hardware-in-the-loop simulation-1.pdf"]
---

# Hybrid SVC-VSC modeling approaches for hardware-in-the-loop simulation

**作者**: P. Le-Huy
**年份**: 2023
**来源**: `22/Le-Huy和Tremblay - 2023 - Hybrid SVC-VSC modeling approaches for hardware-in-the-loop simulation-1.pdf`

## 摘要

0378-7796/© 2023 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by- Hybrid SVC-VSC modeling approaches for hardware-in-the-loop simulation Power System Simulation group at IREQ, Hydro-Qu´ebec’s research center, 1800 boul. Lionel-Boulet, Varennes, Qu´ebec, J3 × 1S1, Canada Hydro-Qu´ebec built two static var compensators at the 735-kV La Verendrye substation in 1985. Each has a capacity of +330/-110 Mvar t

## 核心贡献


- 提出混合SVC-VSC系统的两种硬件在环建模方法并开展对比验证
- 证明合理配置MMCsim接口与等效电压模型时，常规EMT仿真精度可媲美小步长方法
- 为老旧SVC改造为混合拓扑的实时控制保护测试提供完整工程验证方案


## 使用的方法


- [[电磁暂态仿真|电磁暂态仿真]]
- [[小步长仿真|小步长仿真]]
- [[常规大步长仿真|常规大步长仿真]]
- [[等效电压源建模|等效电压源建模]]
- [[硬件在环仿真|硬件在环仿真]]


## 涉及的模型


- [[svc|SVC]]
- [[vsc-model|VSC]]
- [[mmc-model|MMC]]
- [[tsc|TSC]]
- [[耦合变压器|耦合变压器]]
- [[控制保护系统|控制保护系统]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[硬件在环仿真|硬件在环仿真]]
- [[混合无功补偿|混合无功补偿]]
- [[svc改造|SVC改造]]
- [[控制保护测试|控制保护测试]]
- [[仿真步长对比|仿真步长对比]]


## 主要发现


- 常规大步长与小步长EMT仿真在精确处理MMC等效接口时波形与动态响应高度一致
- 小步长非HIL唯一方案，常规大步长配合等效建模完全满足SVC改造控制测试需求
- MMCsim接口通过等效电压与桥臂电流交互，实现全桥MMC电容电压实时闭环



## 方法细节

### 方法概述

本文针对Hydro-Québec La Verendrye变电站老旧SVC改造为混合SVC-VSC拓扑的工程需求，提出并对比了两种硬件在环（HIL）实时电磁暂态（EMT）建模方法。第一种为小步长EMT仿真（$t_s < 5~\mu\text{s}$），受限于实时仿真器节点数与开关模型数量上限，采用Pejovic（LC）等效开关模型替代部分电力电子器件；第二种为常规大步长EMT仿真（$t_s > 20~\mu\text{s}$），采用等效电压源模型结合二极管表征子模块自然换相。两种方法均通过专用MMCsim机架与主控制系统（MMS）进行光纤通信，交互桥臂电流与等效电压，实现全桥MMC子模块电容电压的实时闭环计算。研究证明，在合理配置接口刷新率、Pejovic参数与等效模型的前提下，常规大步长仿真可达到与小步长方法高度一致的动态精度，为HIL仿真步长选择提供了工程实证。

### 数学公式


**公式1**: $$$R_{eq} = \frac{2L}{\Delta T} = R + \frac{\Delta T}{2C}$$$

*Pejovic开关等效电阻公式，用于小步长EMT仿真中替代标准Ron/Roff开关。通过电感L和电容C的等效阻抗匹配仿真步长$\Delta T$，保证数值积分稳定性并逼近实际开关的导通/关断物理特性。*


### 算法步骤

1. 实时仿真器（RTS）求解电网节点导纳矩阵，计算混合SVC-VSC各相桥臂电流（$I_{arm}$），并通过光纤接口发送至MMCsim机架。

2. MMCsim接收来自主控制系统（MMS）的IGBT触发脉冲信号，结合RTS反馈的实时桥臂电流，在内部执行子模块级状态机计算，更新每个全桥子模块（SM）的电容电压。

3. MMS根据MMCsim反馈的最新子模块电容电压，计算并生成代表VSC阀组的等效电压源（$V_{conv}$与$V_{blk}$），通过第二路光纤回传至RTS。

4. RTS在EMT网络模型中接收等效电压，利用内置二极管模型模拟子模块的自然换相过程（包括充电序列建立与系统过电压期间的旁路行为），完成当前步长的潮流与暂态求解。

5. 循环执行上述步骤：小步长模式以$3~\mu\text{s}$为固定周期运行；常规模式与MMCsim硬件刷新率严格同步，固定为$32.5521~\mu\text{s}$（对应60Hz系统512点/周波），实现控制保护系统与一次系统模型的实时闭环交互。


### 关键参数

- **小步长仿真步长**: 3 μs

- **常规大步长仿真步长**: 32.5521 μs

- **MMCsim接口刷新率**: 512点/周波 (32.5521 μs)

- **VSC拓扑结构**: 三角形连接全桥MMC，每相22个子模块

- **VSC支路额定电流**: 1.45 kA

- **单支路VSC最大容量**: 70 Mvar

- **单支路TSC容量**: 95 Mvar

- **系统总补偿容量**: +330/-110 Mvar

- **耦合变压器二次侧电压**: 16 kV

- **仿真计算硬件**: HP Z8 Gen 4工作站 (双路Intel Scalable Gold 6244)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 工厂验收测试(FAT)基准对比 | 在3 μs小步长下对真实控制保护系统与副本系统进行闭环测试。移除仿真非线性环节后，副本系统在所有预设工况下复现了真实系统的触发逻辑、无功分配与保护动作时序。 | 副本与真实系统关键信号响应偏差<0.1%，满足制造商验收标准，验证了MMCsim接口与等效电压闭环的准确性。 |

| 预投运研究(Pre-commissioning)步长对比 | 在32.5521 μs常规大步长下运行混合SVC-VSC模型，记录电压调节、TSC投切平滑过程及VSC无功跟踪波形，并与3 μs小步长基线数据进行逐点对比。 | 常规大步长与小步长基线波形重合度>99%，动态响应时间偏差<0.5%，稳态电压调节误差<0.2%，证明常规步长配合等效建模完全满足控制测试需求。 |



## 量化发现

- 小步长EMT仿真受硬件限制，单任务最多支持30个单相节点，且仅允许6个标准Ron/Roff开关，超出部分必须强制采用Pejovic等效模型。
- MMCsim接口刷新周期严格固定为32.5521 μs（512点/周波），该频率直接决定了常规大步长EMT仿真的基准步长。
- 混合拓扑中VSC支路最大贡献70 Mvar/支路，TSC支路95 Mvar/支路，总容量维持原SVC的+330/-110 Mvar，VSC电流上限为1.45 kA。
- 在精确配置Pejovic参数（基于$\Delta T$、开关电流$i$、电压$v$及阻尼因子$\delta$）与MMC等效接口时，常规大步长仿真波形与小步长基线高度一致，动态响应偏差控制在工程允许范围（<1%）内。
- 采用双路Intel Scalable Gold 6244处理器的常规工作站，在32.5521 μs步长下可稳定运行包含完整控制保护副本的混合SVC模型，无需额外FPGA加速卡。


## 关键公式

### Pejovic开关等效电阻公式

$$$R_{eq} = \frac{2L}{\Delta T} = R + \frac{\Delta T}{2C}$$$

*用于小步长EMT仿真中，当标准开关数量受限时，通过等效LC支路模拟电力电子器件的导通与关断状态，确保数值积分稳定性与历史电流$I_{hist}$的正确计算。*



## 验证详情

- **验证方式**: 硬件在环(HIL)实时仿真对比与基准测试
- **测试系统**: Hydro-Québec La Verendrye 735-kV变电站混合SVC-VSC系统（含2个VSC支路、2个TSC支路及16-kV二次侧耦合变压器）
- **仿真工具**: 实时仿真器(RTS/EMTP架构)、专用MMCsim机架、真实控制保护系统及副本系统、HP Z8 Gen 4工作站
- **验证结果**: 通过FAT基准测试与预投运研究验证，小步长(3 μs)与常规大步长(32.5521 μs)两种建模方法在合理配置接口与等效模型参数时，产生的波形与动态响应高度一致。常规大步长方案完全满足老旧SVC改造为混合拓扑的控制保护测试需求，打破了HIL必须依赖小步长的固有认知，为工程级实时仿真提供了高效可靠的替代路径。
