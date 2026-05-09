---
title: "Coherency Clustering"
type: method
tags: [coherency-clustering]
created: "2026-05-04"
---

# Coherency Clustering


```mermaid
graph LR
    N0[定义与边界]
    N1[概念边界]
    N0 --> N1
    N2[核心机制]
    N1 --> N2
    N3[链接用法]
    N2 --> N3
    N4[代表性来源]
    N3 --> N4
    N5[证据边界]
    N4 --> N5
```


## 定义与边界

Coherency clustering 指根据暂态响应相似性把设备或机组划分为若干同调群，用于动态等值、模型降阶或分区分析。在 EMT Wiki 当前证据中，它主要出现在风电场/DFIG 机群等值语境：用故障电流轨迹或 LVRT 响应特征识别哪些机组可以合并表示。

本页是简洁方法入口，不保留此前误贴的多导体线路推导、泛化未来展望、无来源精度和实时性能声明。

## 概念边界

- 与 [[current-trajectory-similarity]] 的关系：后者是基于电流轨迹相似度的具体分群入口；本页是上位同调聚类概念。
- 与 [[network-equivalent]] 的关系：同调聚类常用于等值前的分群，但不等于完整网络等值方法。
- 与 [[wind-farm-modeling]] 的关系：风电场建模可使用聚类等值；具体聚类特征需绑定机型、故障和控制策略。
- 与 [[modal-analysis]] 的关系：模态分析关注线性化模态、参与因子或振型，不等同于基于时域轨迹的聚类。

## 核心机制

同调分群的核心判据是机组间暂态响应轨迹的相似性度量。对于任意两台机组 $i, j$，其响应向量 $\mathbf{x}_i, \mathbf{x}_j$ 在故障时段 $[0,T]$ 内的距离可写为：

$$
d_{ij} = \left( \int_0^T \|\mathbf{x}_i(t) - \mathbf{x}_j(t)\|^p dt 
ight)^{1/p}
$$

当 $d_{ij} < arepsilon_{	ext{cluster}}$ 时，两机组归入同一同调群。实际应用中 $\mathbf{x}_i$ 可选为故障电流包络线、LVRT 响应或转子角轨迹；阈值 $arepsilon_{	ext{cluster}}$ 和范数阶次 $p$ 由具体聚类算法和验证工况决定。

## 链接用法

当句子强调“按暂态响应相似性分群”时，可链接本页。若已明确是短路电流包络线方法，应链接 [[current-trajectory-similarity]]；若强调等值模型接口，应链接 [[network-equivalent]] 或 [[wind-farm-modeling]]。

## 代表性来源

- [[基于电流轨迹相似度的双馈风电机群电磁暂态同调分群方法]]：直接支撑 DFIG 风电机群在 EMT 故障暂态中的同调分群语境。
- [[an-enhanced-k-means-two-step-clustering-method-for-dynamic-equivalent-modeling-o]]：支撑基于 LVRT 特征和增强 K-means 的 DFIG 风电场动态等值分群语境。
- [[电力系统风力发电建模与仿真研究综述]]：提供风电场多时间尺度建模与聚类等值的综述背景。

## 证据边界

当前证据支持“按暂态响应相似性进行风电机群分群”的方法定位。不同论文使用的特征量、聚类算法、阈值和验证工况不同，不能写成固定分群数、固定误差百分比或对所有新能源场站通用的降阶规则。
