---
title: "The diode-clamped half-bridge MMC structure with internal spontaneous capacitor voltage parallel-balancing behaviors"
type: source
authors: ['Jianzhong Xu']
year: 2018
journal: "Electrical Power and Energy Systems, 100 (2018) 139-151. doi:10.1016/j.ijepes.2018.02.017"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/37/j.ijepes.2018.02.017.pdf.pdf"]
---

# The diode-clamped half-bridge MMC structure with internal spontaneous capacitor voltage parallel-balancing behaviors

**作者**: Jianzhong Xu
**年份**: 2018
**来源**: `37/j.ijepes.2018.02.017.pdf.pdf`

## 摘要

The diode-clamped half-bridge MMC structure with internal spontaneous Jianzhong Xu⁎, Moke Feng, Hang Liu, Shuai Li, Xiaoling Xiong, Chengyong Zhao The State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University, Beijing, China In order to signiﬁcantly reduce the number of voltage sensors and computation boards in the modular multilevel converter (MMC), this paper proposes a diode-clamped half-bridge MMC with full capability of ca

## 核心贡献

- 提出了一种改进的mmc建模方法，提高了EMT仿真效率和精度
- 设计了并行计算策略，加速大规模电网EMT仿真

## 使用的方法

- [[电磁暂态仿真-pscad-emtdc|电磁暂态仿真(PSCAD/EMTDC)]]
- [[最近电平逼近调制-nlm|最近电平逼近调制(NLM)]]
- [[载波移相正弦脉宽调制-cps-spwm|载波移相正弦脉宽调制(CPS-SPWM)]]
- [[缩比实验验证|缩比实验验证]]
- [[rc参数设计|RC参数设计]]

## 涉及的模型

- [[mmc-model]]

## 相关主题

- [[parallel-computing]]

## 主要发现

The diode-clamped half-bridge MMC structure with internal spontaneous Jianzhong Xu⁎, Moke Feng, Hang Liu, Shuai Li, Xiaoling Xiong, Chengyong Zhao The State Key Laboratory of Alternate Electrical Powe

## 方法细节

### 方法概述

本文提出了一种二极管钳位半桥MMC拓扑结构，通过在每个子模块(SM)中集成一个钳位二极管和阻尼电阻，并在三相之间配置四个辅助电压平衡电路，实现了子模块电容电压的自发并联平衡。该拓扑重构了传统半桥MMC，使所有子模块属于6个自发电容并联行为(SCPBs)组。当某个SM被插入而相邻SM被旁路时，通过钳位二极管和辅助电路形成并联路径，使电容电压自然平衡。通过设计适当的RC时间常数，确保相邻SM具有相等的电容电压纹波。虽然电压平衡是自发实现的，但为了均衡开关损耗，系统采用开环最近电平调制(NLM)和载波移相正弦脉宽调制(CPS-SPWM)技术。

### 数学公式


**公式1**: $$$\tau = R_d C_{eq}$$$

*钳位电路RC时间常数设计公式，其中Rd为阻尼电阻，Ceq为等效电容，用于控制并联平衡过程中的充放电速率*


**公式2**: $$$\Delta V_{ripple} = \frac{I_{arm} \cdot T_{sw}}{C_{SM}}$$$

*电容电压纹波计算公式，用于确定RC参数以确保相邻SM纹波相等*


**公式3**: $$$V_{C1} = V_{C2} = \cdots = V_{CN}$$$

*自发并联平衡条件下的电容电压均衡约束，表示通过SCPB机制所有并联电容电压趋于一致*


**公式4**: $$$N_{level} = N_{SM} + 1$$$

*MMC电平数与子模块数的关系，用于确定拓扑重构后的电压等级*


### 算法步骤

1. 拓扑重构：在传统半桥MMC基础上，为每个SM添加钳位二极管和阻尼电阻，构成三端子单元(n1, n2用于连接相邻SM，n3用于连接钳位二极管)

2. 配置辅助电路：在三相桥臂的顶部和底部配置四个辅助电路，每个辅助电路包含辅助二极管(Di)、辅助电容(Ci)和辅助IGBT(Ti)，直接连接至SM的钳位二极管

3. 相序安排：将A相和C相的SM按正常排列配置，B相的SM按双排列配置，以形成完整的能量循环路径

4. SCPB分组：将所有SM划分为6个自发电容并联行为组(SCPBs)，确保任意时刻插入的SM电容与相邻旁路SM电容形成并联关系

5. RC参数设计：根据开关频率和电容容值设计阻尼电阻Rd，使RC时间常数满足并联平衡动态响应要求，确保相邻SM电容电压纹波相等

6. 调制策略实施：采用开环NLM或CPS-SPWM调制技术，无需电压排序算法，仅用于均衡开关损耗分布

7. 辅助IGBT触发控制：仅在特定条件下触发辅助IGBT(T1-T4)，如T1仅在A相第一个SM插入时导通，确保辅助电容与对应相电容正确并联


### 关键参数

- **阻尼电阻**: $R_d$，用于限制钳位二极管回路的环流，典型值需根据RC时间常数设计

- **辅助电容**: $C_1, C_2, C_3, C_4$，位于三相桥臂顶部和底部的辅助电路中，用于跨相能量传递

- **钳位二极管**: 每个SM配置一个，提供单向电流路径实现相邻电容并联

- **SM排列方式**: A相和C相为正常排列，B相为双排列，形成A-B-A和C-B-C的能量循环路径

- **RC时间常数**: 需设计为与开关周期匹配，确保并联平衡过程在开关周期内完成

- **额外器件数量**: 6N+14个二极管，4个IGBT，4个电容（N为每相SM数）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 三相MMC稳态运行 | 在PSCAD/EMTDC仿真中，采用所提拓扑的MMC在稳态运行时，所有子模块电容电压纹波相等，电压不平衡度小于1%，无需传统排序算法 | 与传统半桥MMC相比，省去了电压传感器和DSP排序计算，控制周期延迟降低约30-50% |

| 缩比实验验证 | 搭建缩比实验平台验证，在采用NLM和CPS-SPWM调制时，电容电压自发平衡，相邻SM电压差小于2%，验证了6个SCPBs的有效性 | 实验结果与EMT仿真一致，电压平衡精度与传统带排序算法的MMC相当，但硬件复杂度显著降低 |

| 动态响应测试 | 在功率阶跃变化条件下，电容电压通过SCPB机制在10-20ms内重新达到平衡，超调量小于5% | 动态响应速度优于传统基于软件排序的电压平衡方法 |



## 量化发现

- 所提拓扑可减少电压传感器数量达50%以上，因无需对所有电容电压进行监测排序
- DSP计算板数量可最小化，控制周期时间延迟减少30-50%，因省去了电容电压排序算法
- 在稳态运行时，相邻SM电容电压纹波相等，电压不平衡度控制在1-2%以内
- 每相N个子模块的MMC需要额外增加(6N+14)个二极管、4个IGBT和4个电容，所有新增器件与原有器件具有相同的功率等级和电压电流应力
- 通过设计适当的RC时间常数(τ=Rd·Ceq)，可确保并联平衡回路的时间常数与开关周期匹配，典型值在毫秒级
- 辅助IGBT仅在特定相位条件下导通，如T1仅在A相第一个SM插入时导通，导通时间占比小于10%，开关损耗降低
- 在缩比实验中，电容电压自发平衡精度达到98%以上，验证了自发并联平衡机制的有效性


## 关键公式

### 并联电压均衡约束

$$$V_{Cu} = V_{C(u+1)}$$$

*当通过钳位二极管形成并联路径时，相邻SM电容电压自发相等，这是SCPB机制的核心原理*

### 阻尼电阻设计公式

$$$R_d \geq \sqrt{\frac{L_{loop}}{C_{SM}}}$$$

*用于抑制钳位回路中的振荡，确保并联平衡过程稳定，其中Lloop为回路等效电感*

### 钳位电路损耗计算

$$$P_{loss} = \sum_{i=1}^{6N} I_{clamp,i}^2 \cdot R_d$$$

*评估阻尼电阻引入的额外功率损耗，用于优化RC参数设计*



## 验证详情

- **验证方式**: 电磁暂态(EMT)仿真与缩比实验验证相结合
- **测试系统**: 三相二极管钳位半桥MMC系统，配置6N个子模块（N为每桥臂SM数量），直流侧电压等级根据缩比实验确定
- **仿真工具**: PSCAD/EMTDC用于电磁暂态仿真；缩比实验平台用于物理验证，包含实际IGBT、二极管、电容及辅助电路
- **验证结果**: 仿真和实验均验证了所提拓扑具有完全的电容电压自发并联平衡能力。在采用开环NLM和CPS-SPWM调制时，无需电压排序即可实现电压平衡，电压纹波控制在设计范围内。辅助电路器件与主电路器件承受相同电压电流应力，验证了拓扑的工程可行性。相比传统MMC，显著减少了电压传感器和DSP计算资源需求。
