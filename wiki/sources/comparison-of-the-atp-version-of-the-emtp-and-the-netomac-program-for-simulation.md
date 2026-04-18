---
title: "Comparison of the ATP version of the EMTP and the NETOMAC program for simulation of HVDC systems"
type: source
authors: ['P. Lehn', 'J. Rittiger', 'B. Kulicke']
year: 2004
journal: "IEEE Transactions on Power Delivery;1995;10;4;10.1109/61.473344"
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/10/Lehn和Rittiger - 1995 - Comparison of the atp version of the emtp and the netomac program for simulation of hvdc systems.pdf"]
---

# Comparison of the ATP version of the EMTP and the NETOMAC program for simulation of HVDC systems

**作者**: P. Lehn, J. Rittiger, B. Kulicke
**年份**: 2004
**来源**: `10/Lehn和Rittiger - 1995 - Comparison of the atp version of the emtp and the netomac program for simulation of hvdc systems.pdf`

## 摘要

This paper investigates the capabilities and limitations of the EMTP and the NETOMAC program as applied to HVdc system simulation. The fundamental differences between the two pro- grams and their effect on simulation results are described. Con- sistency of the results obtained from these programs is examined through simulation of a test HVdc network. As expected, a very high degree of agreement between the two sets of simulation re- sults proved to be achievable, but only when particular care was taken to overcome intemal program differences. Finally, the new advanced stability feature of NETOMAC is briefly dis- cussed and then tested against the complex transient models es- tablished in the EMTP and in the NETOMAC transients pro- gram section. Keywords: HVdc simulation, ATP, EMTP, NETOMAC

## 核心贡献


- 系统对比两程序底层差异（步长机制、插值技术与控制网络解耦延迟）
- 提出消除内部差异的建模校准方法，实现复杂HVDC系统仿真高度一致
- 验证NETOMAC高级稳定性模型在含容性海缆与谐振网络中的适用性


## 使用的方法


- [[变步长求解|变步长求解]]
- [[开关时刻线性插值|开关时刻线性插值]]
- [[t型等值模型|T型等值模型]]
- [[控制网络同步求解|控制网络同步求解]]
- [[高级稳定性模型|高级稳定性模型]]


## 涉及的模型


- [[lcc-model|LCC]]
- [[交流滤波器|交流滤波器]]
- [[输电线路|输电线路]]
- [[海底电缆|海底电缆]]
- [[饱和变压器|饱和变压器]]
- [[晶闸管|晶闸管]]
- [[vdcl控制器|VDCL控制器]]


## 相关主题


- [[vsc-hvdc|VSC-HVDC]]
- [[仿真程序对比|仿真程序对比]]
- [[开关延迟与数值振荡|开关延迟与数值振荡]]
- [[控制系统建模|控制系统建模]]
- [[机电暂态稳定性仿真|机电暂态稳定性仿真]]
- [[直流侧谐波谐振|直流侧谐波谐振]]


## 主要发现


- 精细校准开关时刻与步长后，两程序在复杂HVDC暂态仿真中结果高度一致
- NETOMAC变步长与插值技术有效消除固定步长引发的触发延迟与数值振荡
- 高级稳定性模型可准确复现含高容性海缆与直流滤波器的复杂网络动态



## 方法细节

### 方法概述

本文采用跨平台对比与精细化模型校准相结合的方法，系统评估EMTP（ATP版本）与NETOMAC在高压直流（HVDC）系统电磁暂态仿真中的底层机制差异与结果一致性。研究首先构建包含复杂直流回路（含66km海底电缆、多段T型等值线路及直流阻波滤波器）的600MW/400kV单极HVDC测试系统。针对EMTP固定步长求解与TACS控制网络解耦延迟、以及NETOMAC变步长与线性插值同步求解的架构差异，通过分解PI控制器限幅逻辑、统一非线性变压器饱和数据转换标准、调整开关电流裕度以抑制截断电流振荡，实现控制与网络模型的精确对齐。随后在多种交直流故障场景下对比直流电流、电压及触发/熄弧角动态波形，并引入NETOMAC高级稳定性模型（交流侧复导纳单线正序网络与直流侧完整微分方程混合求解）进行长时域动态仿真，验证其在计算效率与工程精度上的适用边界。

### 数学公式


**公式1**: $$$t_{sw} = t_n + \frac{V_{ref} - V(t_n)}{V(t_{n+1}) - V(t_n)} \Delta t$$$

*线性插值公式，用于NETOMAC在变步长求解中精确计算晶闸管触发/关断时刻，消除固定步长带来的时序误差*


**公式2**: $$$V_d = \frac{3\sqrt{2}}{\pi} V_{LL} \cos \alpha - \frac{3}{\pi} X_c I_d$$$

*准稳态换流器方程，用于高级稳定性模型中耦合交流单线网络与直流暂态微分方程，替代详细阀组模型*


### 算法步骤

1. 物理网络参数对齐：将非线性变压器饱和曲线通过专用支持程序转换为两程序兼容格式，采用T型等值电路离散化交流线路（20km/段）与海底电缆（5km/段，共13段），确保拓扑与电气参数严格一致。

2. 控制逻辑解耦与重构：将TACS与NETOMAC中的PI控制器拆分为独立的P与I模块，统一限幅处理逻辑与数字/模拟控制接口，消除因内置函数库差异导致的控制信号相位偏移与响应延迟。

3. 开关延迟补偿与步长优化：针对EMTP固定步长导致的触发延迟（1个步长+过零点检测误差），调整开关电流裕度以抑制截断电流引发的数值振荡；通过收敛性测试确定EMTP最优步长为20μs，NETOMAC暂态模型为100μs。

4. 故障场景同步注入：在整流侧/逆变侧分别设置单相/三相接地故障及直流线路故障，严格对齐故障发生时刻与清除逻辑，记录直流电流、电压及α/γ角动态响应波形。

5. 高级稳定性模型混合求解：交流侧采用复导纳单线正序网络，直流侧保留完整暂态微分方程，接口处采用准稳态换流器方程耦合，设置AC/DC统一求解步长500μs进行长时域动态仿真与效率评估。


### 关键参数

- **EMTP_time_step**: 20 μs

- **NETOMAC_transient_time_step**: 100 μs

- **NETOMAC_stability_time_step**: 500 μs

- **HVDC_rating**: 600 MW, 400 kV

- **AC_SCR**: 5.0

- **AC_filter_compensation**: 240 Mvar (80% reactive demand)

- **Cable_length**: 66 km (13 T-sections, ~5 km each)

- **Simulation_duration**: 640 ms

- **Hardware_platform**: 80486, 33 MHz



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 三相整流侧接地故障 | 暂态模型间直流电流与电压波形高度重合；高级稳定性模型因采用平衡三相假设，故障清除后恢复速度略快，残余直流电流被轻微高估。整流侧触发角α稳态偏差0.6°（14.7° vs 15.3°）。 | 动态趋势一致，稳态偏差<0.6%，适用于对称故障快速筛查 |

| 直流线路故障（电缆与线路2交界处） | 高级稳定性模型准确捕捉直流网络故障期间的电流跌落与电压波动，波形与暂态模型吻合度极高。计算耗时仅21秒，远低于EMTP的765秒与NETOMAC暂态的193秒。 | 计算效率较EMTP提升约36.4倍，较NETOMAC暂态提升约9.2倍 |

| 单相逆变侧接地故障 | 暂态模型因需等待各相电流依次过零切断，恢复过程呈阶梯状；稳定性模型因单线正序假设呈现平滑恢复。逆变侧熄弧角γ与触发角完全一致（18.0°与145.2°）。 | 不对称故障仅能近似，但直流侧动态响应误差<2%，满足工程初设需求 |



## 量化发现

- EMTP需采用约5倍于NETOMAC的更小步长（20μs vs 100μs）方可消除因固定步长与插值缺失导致的数值振荡与触发延迟误差。
- NETOMAC高级稳定性模型计算640ms暂态过程仅需21秒，较NETOMAC暂态模型（193秒）提速约9.2倍，较EMTP（765秒）提速约36.4倍。
- 故障前稳态运行点最大偏差：整流侧触发角α偏差0.6°（14.7° vs 15.3°），逆变侧熄弧角γ与触发角完全一致（18.0°与145.2°），直流电流标幺值误差为0。
- 在大型交流系统仿真中，高级稳定性模型在暂态过程结束后可进一步增大交流侧步长，整体计算速度可再提升10倍以上。


## 关键公式

### 开关时刻线性插值公式

$$$t_{sw} = t_n + \frac{V_{ref} - V(t_n)}{V(t_{n+1}) - V(t_n)} \Delta t$$$

*NETOMAC用于精确计算晶闸管触发/关断时刻，消除EMTP固定步长带来的1个时间步延迟与过零点检测误差*

### 准稳态换流器方程

$$$V_d = \frac{3\sqrt{2}}{\pi} V_{LL} \cos \alpha - \frac{3}{\pi} X_c I_d$$$

*NETOMAC高级稳定性模型中用于耦合交流单线网络与直流暂态微分方程，替代详细阀组模型以提升计算效率*



## 验证详情

- **验证方式**: 跨程序对比仿真分析（EMTP vs NETOMAC暂态 vs NETOMAC高级稳定性）
- **测试系统**: 自定义600MW/400kV单极HVDC测试系统，含强交流系统（SCR=5.0）、240Mvar交流滤波器、66km海底电缆（13段T型等值）、直流50/100Hz阻波滤波器
- **仿真工具**: ATP/EMTP (LEC版本), NETOMAC (暂态模块与高级稳定性模块)
- **验证结果**: 经模型校准与步长优化后，两程序暂态仿真结果在对称交直流故障下实现高度一致（稳态偏差<0.6°）。NETOMAC高级稳定性模型在牺牲不对称故障精度的前提下，准确复现直流故障动态，计算效率提升近一个数量级，适用于大规模HVDC系统故障筛查与控制器初步设计。
