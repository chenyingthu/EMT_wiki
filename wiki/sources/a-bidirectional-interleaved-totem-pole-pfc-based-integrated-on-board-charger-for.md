---
title: "A Bidirectional Interleaved Totem Pole PFC-Based Integrated On-Board Charger for EV SRM Drive"
type: source
authors: ['未知']
year: 2024
journal: "IEEE Access;2024;12; ;10.1109/ACCESS.2024.3432791"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/01/Faheem Ali 等 - 2024 - A Bidirectional Interleaved Totem Pole PFC-Based Integrated On-Board Charger for EV SRM Drive.pdf"]
---

# A Bidirectional Interleaved Totem Pole PFC-Based Integrated On-Board Charger for EV SRM Drive

**作者**: 
**年份**: 2024
**来源**: `01/Faheem Ali 等 - 2024 - A Bidirectional Interleaved Totem Pole PFC-Based Integrated On-Board Charger for EV SRM Drive.pdf`

## 摘要

This paper presents an improved integrated on-board charger (IOBC) tailored for a 4-phase switched reluctance motor (SRM) drive. The proposed IOBC is non-isolated and utilizes the totem pole power factor correction (PFC) operation for reduced common-mode voltage. Furthermore, the proposed system accommodates bidirectional functions, ensuring versatility during charging mode. A non-isolated IOBC for SRM with reduced common-mode voltage and bidirectional capability has largely been ignored in the literature. The proposed system utilizes a modified Miller converter in the motoring mode and is easily reconfigured into a two-phase interleaved totem pole converter during charging modes without the need for any magnetic contactors. The proposed system features zero instantaneous torque (ZIT) at s

## 核心贡献


- 提出无磁接触器重构拓扑，将改进型Miller变换器切换为交错图腾柱PFC
- 设计考虑电感位置变化的控制策略，实现充电稳态零瞬时转矩并消除偶次谐波
- 利用电机绕组并联使充电功率翻倍，同时抑制共模电压并支持双向能量流动


## 使用的方法


- [[交错图腾柱pfc控制|交错图腾柱PFC控制]]
- [[零瞬时转矩控制|零瞬时转矩控制]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[双向功率流控制|双向功率流控制]]


## 涉及的模型


- [[开关磁阻电机-srm|开关磁阻电机(SRM)]]
- [[改进型miller变换器|改进型Miller变换器]]
- [[交错图腾柱pfc变换器|交错图腾柱PFC变换器]]
- [[集成车载充电器-iobc|集成车载充电器(IOBC)]]


## 相关主题


- [[电动汽车集成车载充电|电动汽车集成车载充电]]
- [[功率因数校正|功率因数校正]]
- [[共模电压抑制|共模电压抑制]]
- [[双向充放电|双向充放电]]
- [[零瞬时转矩控制|零瞬时转矩控制]]
- [[谐波分析|谐波分析]]


## 主要发现


- 仿真与实验验证拓扑无需接触器重构，充电稳态实现零瞬时转矩且无转子振动
- 对称电流控制消除电网偶次谐波，正负半周等效电感一致显著提升电能质量
- 绕组并联配置使充电功率达驱动功率两倍，共模电压大幅降低且系统效率提升


