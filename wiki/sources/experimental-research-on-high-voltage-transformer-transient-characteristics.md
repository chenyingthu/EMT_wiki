---
title: "Experimental research on high-voltage transformer transient characteristics"
type: source
authors: ['未知']
year: 2026
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/18/Tang 等 - 2010 - Experimental research on high-voltage transmission line protection device based on electromechanical.pdf"]
---

# Experimental research on high-voltage transformer transient characteristics

**作者**: 
**年份**: 2026
**来源**: `18/Tang 等 - 2010 - Experimental research on high-voltage transmission line protection device based on electromechanical.pdf`

## 摘要

A scheme to examine acting characteristics of high-voltage transmission line protection devices by electromechanical-electromagnetic transient hybrid simulation is proposed. The hybrid simulation can fully play the superiorities of electromechanical transient simulation and electromagnetic transient simulation, so not only the precision of system simulation can be improved, but also the workload brought by system equivalence can be reduced. Comparing the data from the faults actually occurred in

## 核心贡献


- 提出机电-电磁暂态混合仿真方案，避免大系统等值并突破纯电磁仿真规模限制
- 开发在线数据接口实现EMS实时断面自动导入，构建与实际电网一致的仿真拓扑
- 搭建高压线路保护混合测试平台，实现复杂故障工况下保护装置动作特性的全面检验


## 使用的方法


- [[机电-电磁暂态混合仿真|机电-电磁暂态混合仿真]]
- [[并行仿真技术|并行仿真技术]]
- [[实时数字仿真|实时数字仿真]]
- [[在线数据接口技术|在线数据接口技术]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[变压器|变压器]]
- [[输电线路|输电线路]]
- [[电流互感器|电流互感器]]
- [[电压互感器|电压互感器]]
- [[线路保护装置|线路保护装置]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[实时仿真|实时仿真]]
- [[继电保护测试|继电保护测试]]
- [[故障重现|故障重现]]
- [[ct饱和特性|CT饱和特性]]
- [[系统振荡分析|系统振荡分析]]


## 主要发现


- 仿真波形与实际故障录波高度一致，验证了混合仿真平台反映电网实际工况的准确性
- 转换性故障易导致保护选相错误并误发三跳令，CT饱和会显著延长保护动作时间
- 经高阻接地时保护易拒动，系统振荡下保护虽能正确选相但动作时间明显延长


