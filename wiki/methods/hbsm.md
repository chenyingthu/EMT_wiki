---
title: "HBSM 入口页 (HBSM)"
type: method
tags: [hbsm, half-bridge-submodule, mmc]
created: "2026-05-05"
updated: "2026-05-06"
---

# HBSM 入口页 (HBSM)


```mermaid
graph TD
    N0[HBSM 入口页 (HBSM)]
    N1[定义与边界]
    N0 --> N1
    N2[EMT 中的作用]
    N0 --> N2
    N3[常见使用方式]
    N0 --> N3
    N4[形式化表达]
    N0 --> N4
    N5[相关页面]
    N0 --> N5
    N6[代表性来源]
    N0 --> N6
    N7[证据边界]
    N0 --> N7
    N8[开放问题]
    N0 --> N8
```


## 定义与边界

HBSM 是 Half-Bridge Submodule 的常用缩写。在本 Wiki 中，它作为简称入口存在，用于承接缩写型链接并导向更完整的方法页。

## EMT 中的作用

HBSM 本身不是独立于半桥子模块之外的新方法，而是 MMC 子模块层 EMT 建模中的常见简称。

## 常见使用方式

- 作为半桥子模块页面的缩写入口；
- 作为论文或公式中的拓扑简称；
- 作为与 [[fbsm]]、混合 MMC 等页面对照时的短标签。

## 形式化表达

HBSM 相关建模通常仍回到半桥子模块的基本关系：

$$
v_{sm} = s\,v_c, \qquad C_{sm}\frac{dv_c}{dt}=i_c
$$

其中 $s$ 表示插入/旁路状态。这个入口页不展开更多推导，而是明确 HBSM 与正式方法页之间的对应关系。

## 相关页面

- [[half-bridge-submodule]]：半桥子模块的主要方法页。
- [[fbsm]]：全桥子模块的对照入口。
- [[nearest-level-modulation]]：说明子模块插入状态与输出电平关系。
- [[mmc-model]]：说明子模块层和整机层的关系。
- [[mbsm]]：说明统一子模块表示框架中的半桥分支。
- [[circulating-current-suppression]]：说明子模块层状态与桥臂内部控制的相关背景。

## 代表性来源

- [[an-efficient-half-bridge-mmc-model-for-emtp-type-simulation-based-on-hybrid-nume]]：半桥 MMC EMT 建模背景。
- [[the-diode-clamped-half-bridge-mmc-structure-with-internal-spontaneous-capacitor-]]：半桥子模块拓扑扩展背景。
- [[fast-electromagnetic-transient-modeling-method-for-half-bridge-type-voltage-sour]]：半桥型快速 EMT 表示背景。

## 证据边界

本页不重复拓扑、公式或性能结论，避免与正式方法页分叉。

## 开放问题

- 若后续图谱里 `HBSM` 链接稳定收敛到正式方法页，可考虑把本页继续保持为简短别名入口而不再扩写。
