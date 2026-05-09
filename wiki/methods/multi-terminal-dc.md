---
title: "多端直流系统方法 (Multi-Terminal DC)"
type: method
tags: [multi-terminal-dc, mtdc, hvdc, dc-grid, droop-control]
created: "2026-05-05"
updated: "2026-05-06"
---

# 多端直流系统方法 (Multi-Terminal DC)


```mermaid
graph TD
    subgraph S0[多端直流系统方法 (Multi-Terminal DC)]
        N0[定义与边界]
        N1[EMT 中的作用]
        N2[常见研究对象]
        N3[关键公式]
        N4[与相关方法的关系]
        N5[适用边界与失败模式]
    end
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
```


## 定义与边界

多端直流系统（MTDC）是由三个及以上换流站通过直流网络互联形成的输电系统。对应的方法问题包括网络建模、功率协调、直流电压控制、故障处理和初始化，而不仅仅是“多个换流站并联存在”。

本页讨论 MTDC 的系统级方法边界，不把某一篇关于故障时二阶等效、预设故障信息或单一控制策略的论文直接当成全部 MTDC 方法。

## EMT 中的作用

在 EMT 仿真中，MTDC 方法主要用于：

- 组织多站换流器、直流线路和站间控制的系统级模型；
- 研究直流电压协调、功率分配和运行方式切换；
- 分析直流故障传播、网络解列和保护恢复；
- 作为海上风电送出、区域互联和混合直流网研究的系统背景。

## 常见研究对象

- 直流电压下垂和功率分配；
- 多站运行方式切换与主从/分担控制；
- 故障后区段隔离、重构与恢复；
- 海上送出、区域互联和混合拓扑中的系统级协调。

## 关键公式

MTDC 中常见的系统级协调关系之一是直流电压下垂：

$$
P_i^\* = P_{i0} + k_{di}(V_{dc,0} - V_{dc,i})
$$

它说明站间功率分担与直流电压偏差之间的耦合。不同控制器的关键差异通常不在“是否有这个公式”，而在于下垂系数选择、运行模式切换和站间优先级。

## 与相关方法的关系

- [[hvdc-control]]：对应单站或站级控制结构。
- [[dc-protection]] 和 [[dccb]]：对应故障检测与开断配合。
- [[offshore-hvdc-hub]]：对应海上直流枢纽应用背景。
- [[cigre-b4-dc-grid]]：对应典型参考直流网场景入口。

## 适用边界与失败模式

- 适用于研究多站协调和直流网级动态的场景。
- 单站稳定不代表全网协调稳定，站间耦合和运行模式切换可能引入新的动态问题。
- 若不显式建模保护和断路器，MTDC 故障分析往往不完整。
- 不同论文中的 MTDC 拓扑和站级控制差异很大，不能直接拼接成统一结论。

## 代表性来源

- [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi-15]]：说明 MTDC 系统中多站 MMC 建模和故障背景。
- [[impedance-based-stability-analysis-of-the-multi-terminal-cascaded-hybrid-hvdc-sy]]：说明多端直流系统稳定性分析背景。
- [[enhancements-to-terminal-duality-based-models-for-three-phase-multi-limb-multi-w]]：可作为多端多端口建模相关背景来源。

## 证据边界

本页不写无来源的最优站数、故障隔离时间或统一控制架构。具体结论必须绑定拓扑、控制方式和测试工况。

## 开放问题

- 当前页尚未继续拆分多端直流中的控制、保护和初始化三类方法边界。
- 不同 MTDC 拓扑之间的结论可迁移性，后续仍需回到具体 benchmark 或 source 页确认。
