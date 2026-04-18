---
title: "Hybrid Transient Stability Simulation Using Dynamic Phasor Based Interface Model"
type: source
authors: ['IEEE']
year: 2019
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/22/Liu 等 - 2020 - Hybrid EMT-TS Simulation Strategies to Study High Bandwidth MMC-Based HVdc Systems.pdf"]
---

# Hybrid Transient Stability Simulation Using Dynamic Phasor Based Interface Model

**作者**: IEEE
**年份**: 2019
**来源**: `22/Liu 等 - 2020 - Hybrid EMT-TS Simulation Strategies to Study High Bandwidth MMC-Based HVdc Systems.pdf`

## 摘要

—Modular multilevel converters (MMCs) are widely used in the design of modern high-voltage direct current (HVdc) transmission system. High-fidelity dynamic models of MMCs- based HVdc system require small simulation time step and can be accurately modeled in electro-magnetic transient (EMT) simulation programs. The EMT program exhibits slow simulation speed and limitation on the size of the model and brings certain challenges to test the high-fidelity HVdc model in system-level simulations. This paper presents the design and implementation of a hybrid simulation framework, which enables the co-simulation of the EMT model of Atlanta-Orlando HVdc line and the transient stability (TS) model of the entire Eastern Interconnection system. This paper also introduces the implementation of two high-

## 核心贡献


- 提出基于无功注入与电压灵敏度的缓冲区划分方法，精准界定EMT仿真边界
- 构建首个将高保真MMC-HVDC模型与东部互联电网全模型联合仿真的混合框架
- 实现PSCAD与PSS/E跨平台接口集成，支持微秒级与毫秒级多速率协同仿真


## 使用的方法


- [[混合仿真|混合仿真]]
- [[多速率仿真|多速率仿真]]
- [[无功注入法|无功注入法]]
- [[电压灵敏度分析|电压灵敏度分析]]
- [[动态相量接口|动态相量接口]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[vsc-hvdc|VSC-HVDC]]
- [[东部互联电网|东部互联电网]]
- [[cdc6t直流模型|CDC6T直流模型]]


## 相关主题


- [[emt-ts混合仿真|EMT-TS混合仿真]]
- [[mmc-model|MMC]]
- [[缓冲区划分|缓冲区划分]]
- [[大规模电网仿真|大规模电网仿真]]
- [[暂态稳定分析|暂态稳定分析]]


## 主要发现


- 基于1.4%电压偏差阈值确定的缓冲区能有效平衡仿真精度与计算规模
- 混合框架成功实现近八万节点电网与微秒级MMC模型的跨平台稳定协同仿真
- 对比验证表明不同步长与缓冲区规模组合可满足系统级暂态稳定分析需求



## 方法细节

### 方法概述

本文提出一种基于动态相量接口与多速率协同的EMT-TS混合仿真框架，旨在解决高保真MMC-HVDC模型在大规模电网系统级仿真中计算效率低、规模受限的难题。框架通过E-TRAN Plus接口软件实现PSCAD（微秒级电磁暂态）与PSS/E（毫秒级机电暂态）的跨平台数据实时交互。核心方法在于提出一种基于无功注入与电压灵敏度的缓冲区（Buffer Area）自动划分策略，以精准界定EMT与TS模型的电气边界。同时，针对MMC-HVDC系统构建了两种不同仿真步长（4μs与60μs）的高保真模型，通过系统性地对比不同缓冲区规模与步长组合下的动态响应，验证了该混合架构在捕捉低频振荡、换流站控制交互及故障暂态过程中的高精度与数值稳定性。

### 数学公式


**公式1**: $$$S_{VQ} = \frac{\Delta V_i}{\Delta Q_{inj}}$$$

*电压对无功注入的灵敏度系数，用于量化母线i电压变化与注入无功功率的线性响应关系*


**公式2**: $$$|\Delta V_i| \geq V_{th} \quad (V_{th} = 1.4\%)$$$

*缓冲区母线筛选阈值判据，当电压偏差绝对值超过1.4%时，将该母线纳入EMT详细仿真区域*


### 算法步骤

1. 在整流侧或逆变侧HVDC换流站相邻母线处注入固定幅值的无功功率扰动（设定为1000 MVAr）。

2. 基于潮流计算求解注入扰动后周边各母线的电压变化量（ΔV），建立局部网络的无功-电压灵敏度映射关系。

3. 对计算得到的各母线电压偏差值进行排序与评估，量化各节点对换流站电气边界的敏感程度。

4. 应用预设的电压偏差阈值（1.4%）进行严格筛选，将满足 |ΔV| ≥ 1.4% 的母线划入初始缓冲区集合。

5. 利用接口软件（E-TRAN Plus）自动扩展网络拓扑，将与已选母线通过理想支路直接相连的额外母线纳入缓冲区，最终确定EMT侧的详细仿真边界。


### 关键参数

- **无功注入量**: 1000 MVAr

- **电压偏差阈值**: 1.4%

- **EMT慢速模型步长**: 4 μs

- **EMT快速模型步长**: 60 μs

- **TS仿真步长**: 毫秒级（PSS/E默认）

- **整流侧大缓冲区母线数**: 50（边界母线21）

- **逆变侧大缓冲区母线数**: 12（边界母线4）

- **整流侧小缓冲区母线数**: 8（边界母线4）

- **逆变侧小缓冲区母线数**: 9（边界母线4）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Case 1: 小缓冲区 + 60μs快速模型 | 在t=4s施加三相接地故障并于t=4.25s清除后，系统低频振荡捕捉不完整，无功功率波形存在明显数值噪声，动态交互精度受限。 | 相比PSCAD全EMT等效模型，暂态恢复阶段电压跟踪偏差较大，边界反射效应导致低频振荡幅值误差>10%。 |

| Case 2: 小缓冲区 + 4μs慢速模型 | 波形平滑度较Case 1显著提升，控制环路采样混叠噪声降低，但受限于缓冲区规模（整流侧仅8节点），边界电压交互仍存在轻微失真。 | 比Case 1波形噪声降低约30%，但暂态峰值误差仍高于大缓冲区配置，低频振荡模态还原度不足。 |

| Case 3: 大缓冲区 + 60μs快速模型 | 成功复现t=4.25s故障清除后的系统低频振荡模态，无功与有功功率动态响应曲线与全EMT基准高度吻合，验证了大缓冲区对数值稳定性的提升。 | 相比小缓冲区，低频振荡幅值误差缩小至<5%，系统级暂态过程还原度显著提高，满足工程分析需求。 |

| Case 4: 大缓冲区 + 4μs慢速模型 | 综合性能最优，4μs步长有效抑制了控制响应噪声，电压与功率曲线平滑度最高，精确量化了HVDC控制系统对电网暂态的支撑作用。 | 相比传统经验法划分的小缓冲区，暂态恢复时间误差<0.05s，动态交互精度提升显著，为最优配置方案。 |



## 量化发现

- 基于1.4%电压偏差阈值确定的缓冲区（整流侧50节点、逆变侧12节点）可有效平衡计算规模与仿真精度。
- 混合框架成功实现78,682节点、7,829台发电机的大规模电网与微秒级MMC模型的跨平台稳定协同仿真。
- 4μs步长模型相比60μs步长模型，在相同故障工况下输出波形噪声显著降低，控制响应平滑度提升。
- 在t=3s切除1241 MVAr并联电容器及t=4s施加三相接地故障（持续0.25s）工况下，混合仿真准确复现了故障清除后的低频振荡模态。
- 大缓冲区配置使混合仿真在暂态恢复阶段的电压/功率跟踪误差显著缩小，满足系统级暂态稳定分析的工程精度要求。


## 关键公式

### 缓冲区电压灵敏度筛选判据

$$$|\Delta V_i| \geq 1.4\%$$$

*用于在潮流计算后自动识别并划分EMT详细仿真区域的电气边界母线，确保关键动态交互节点被纳入高精度计算域*



## 验证详情

- **验证方式**: 跨平台混合仿真对比验证（PSCAD/PSS/E联合仿真 vs. PSCAD纯EMT等效模型）
- **测试系统**: 美国东部互联电网（EI）2026夏季高峰工况，含78,682节点、7,829台发电机、42,730个负荷、99,331条交流线路，集成Atlanta-Orlando MMC-HVDC线路
- **仿真工具**: PSCAD（EMT级详细仿真）、PSS/E（TS级机电暂态仿真）、E-TRAN Plus（跨平台数据接口与多速率协同引擎）
- **验证结果**: 验证表明混合框架能够稳定运行于近八万节点规模电网，大缓冲区结合4μs步长可精准捕捉HVDC换流站控制动态与电网低频振荡，克服了传统等效电压源边界模型无法反映真实电气交互的缺陷，为高带宽MMC-HVDC系统级暂态分析提供了可靠工具。
