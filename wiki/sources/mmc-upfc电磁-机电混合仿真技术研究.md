---
title: "MMC-UPFC电磁-机电混合仿真技术研究"
type: source
authors: ['叶小晖']
year: 2019
journal: "南方电网技术"
tags: ['mmc', 'emt']
created: "2026-04-13"
sources: ["EMT_Doc/33/叶小晖 等 - 2019 - MMC-UPFC电磁-机电混合仿真技术研究.pdf"]
---

# MMC-UPFC电磁-机电混合仿真技术研究

**作者**: 叶小晖
**年份**: 2019
**来源**: `33/叶小晖 等 - 2019 - MMC-UPFC电磁-机电混合仿真技术研究.pdf`

## 摘要

In view of the demand for large-scale power grid simulation ability in the southern Suzhou 500 kV UPFC project, the electromagnetic transient modeling for unified power flow controller (UPFC) based on MMC is studied.

## 核心贡献


- 建立基于戴维南等效的MMC-UPFC电磁暂态模型，集成串并联控制与TBS旁路逻辑
- 提出UPFC交交混合仿真接口位置选择策略，明确不同工况下的电磁网络划分原则
- 基于苏州500kV工程验证了模型在潮流阶跃与故障工况下的动态响应准确性


## 使用的方法


- [[戴维南等效法|戴维南等效法]]
- [[后退欧拉法|后退欧拉法]]
- [[电磁机电混合仿真|电磁机电混合仿真]]
- [[接口网络划分算法|接口网络划分算法]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[upfc|UPFC]]
- [[变压器|变压器]]
- [[tbs|TBS]]
- [[输电线路|输电线路]]
- [[同步电机|同步电机]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[电磁暂态建模|电磁暂态建模]]
- [[接口位置选择|接口位置选择]]
- [[潮流控制|潮流控制]]
- [[故障动态响应|故障动态响应]]
- [[大规模电网仿真|大规模电网仿真]]


## 主要发现


- 方案a因忽略受控线路动态导致启动失败，方案b适用于常规非接口故障仿真
- 接口处三相短路故障需扩大电磁网络范围，方案d与全电磁暂态结果振荡幅值高度一致
- 苏州500kV工程阶跃试验表明，仿真曲线与现场录波高度吻合，验证了模型有效性


