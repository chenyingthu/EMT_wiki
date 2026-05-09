---
title: "IEEE 118 Bus System"
type: topic
tags: [ieee-118, test-system, benchmark, power-system, large-scale]
created: "2026-05-02"
---

# IEEE 118 Bus System


```mermaid
graph LR
    N0[定义与边界]
    N1[EMT 中的作用]
    N0 --> N1
    N2[主要分支与机制]
    N1 --> N2
    N3[形式化表达]
    N2 --> N3
    N4[适用边界与失败模式]
    N3 --> N4
    N5[代表性来源]
    N4 --> N5
    N6[与相关页面的关系]
    N5 --> N6
    N7[开放问题]
    N6 --> N7
```


## 定义与边界

IEEE 118 bus system 是用于输电网潮流、稳定性、优化和大规模算法研究的标准测试系统。它通常作为正序、稳态或机电暂态 benchmark 使用；若用于 EMT，需要额外补充线路频变参数、变压器详细模型、保护定值、控制器、负荷动态和扰动脚本。

本页作为 topic 页说明 IEEE 118 在 EMT 知识网络中的使用边界。具体测试系统条目可阅读 [[ieee-118-bus-system]] 下的 test-system 页面；更小规模测试可参考 [[ieee-14-bus-system]]、[[ieee-39-bus-system]] 和 [[ieee-57-bus-system]]。

## EMT 中的作用

IEEE 118 可作为大规模 EMT 或混合仿真的外部交流系统、算法测试系统或初始化来源：

- 检查 [[power-flow-calculation]]、[[optimal-power-flow]] 和 [[economic-dispatch]] 结果如何进入 EMT 初值。
- 测试 [[large-scale-grid-simulation]]、[[parallel-computing]]、[[network-partitioning]] 和 [[model-order-reduction]] 的规模边界。
- 作为新能源、FACTS、HVDC 或保护研究的背景网络，但需要明确改造位置和动态参数来源。
- 支撑跨工具对比和 benchmark 报告，但不能替代具体 EMT 设备模型验证。

## 主要分支与机制

- 稳态网络：以节点、支路、变压器和发电/负荷数据构成正序潮流系统，常用于 OPF 和潮流算法。
- 动态扩展：加入发电机、励磁、调速、PSS、负荷和保护模型后，才可用于机电暂态或 EMT 研究。
- EMT 改造：需要把线路、变压器、负荷、换流器或故障点转化为相域或三相模型，并说明外部系统等值。
- 大规模求解：节点数和支路数使其适合检验矩阵组装、稀疏求解、分区和并行调度。

## 形式化表达

IEEE 118 的基础潮流模型可写为：

$$
I=Y_{\mathrm{bus}}V,\qquad
P_i+jQ_i=V_i I_i^\ast
$$

其中 $Y_{\mathrm{bus}}$ 是标准测试系统给出的正序网络矩阵。进入 EMT 时，必须进一步定义三相网络、动态状态 $x$、控制器 $c$ 和扰动集合 $\mathcal{D}$：

$$
\mathcal{S}_{\mathrm{EMT}} = \{Y_{abc},x_0,c,\mathcal{D},h\}
$$

没有这些扩展时，IEEE 118 只能作为稳态或机电背景，不能支撑详细 EMT 结论。

## 适用边界与失败模式

- 标准 IEEE 118 数据不包含完整 EMT 所需的设备高频参数、保护定值和控制器细节。
- 若把 IEEE 118 用作外部系统等值，应说明保留哪些区域、哪些母线被等值、边界注入如何处理。
- 新能源、HVDC 或 FACTS 改造后的结论只对改造版本成立，不能写成 IEEE 118 原始系统性质。
- 不同数据版本可能有参数差异，报告时应说明数据来源和格式。

## 代表性来源

- [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-]] 可作为大规模 benchmark 和实时仿真证据边界的参考。
- [[lessons-learned-in-porting-offline-large-scale-power-system-simulation-to-real-t]] 支撑离线大规模模型移植到实时平台时的工程边界。
- [[benchmark-high-fidelity-emt-models-for-power]] 说明高保真 EMT benchmark 需要明确模型层级和验证指标。

## 与相关页面的关系

- [[model-verification-benchmark]] 讨论 benchmark 流程和误差证据。
- [[large-scale-system-simulation]]、[[large-scale-grid-simulation]] 和 [[large-scale-power-system]] 讨论规模化系统仿真问题。
- [[power-flow-calculation]] 和 [[optimal-power-flow]] 处理该系统的常见稳态用途。
- [[ieee-39-bus-system]]、[[ieee-14-bus-system]] 和 [[ieee-57-bus-system]] 是规模较小的相关测试系统。

## 开放问题

- 如何公开一套可复现的 IEEE 118 三相 EMT 扩展版本。
- 如何为 IEEE 118 中的负荷、保护和控制器补充可信动态参数。
- 如何报告以 IEEE 118 为背景网络的新能源或 HVDC 改造，使结论不被误读为原始 benchmark 属性。
