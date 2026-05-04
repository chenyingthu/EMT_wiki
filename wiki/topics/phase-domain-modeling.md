---
title: "相域建模 (Phase-Domain Modeling)"
type: topic
tags: [phase-domain, modeling, transmission-line, cable, unbalance, modal-transformation, coupling]
created: "2026-05-02"
---

# 相域建模 (Phase-Domain Modeling)

## 定义与边界

相域建模是在 $abc$ 相坐标下直接表示线路、电缆、变压器、电机、换流器和故障的 EMT 建模路线。它不是所有场景中都比模域或序分量方法更优；其价值在于保留相间耦合、不平衡、非换位线路、非线性和任意拓扑，但代价是矩阵耦合和计算复杂度上升。

本页是 topic 页，关注相域建模的整体边界。方法层面的相域模型可阅读 [[phase-domain-modeling]]，相域与序分量关系可阅读 [[symmetrical-components]]、[[sequence-component-method]] 和 [[modal-transformation]]。

## EMT 中的作用

相域建模在 EMT 中用于：

- 表示非换位线路、地下电缆、平行线路和多导体系统的相间耦合。
- 处理单相接地、相间故障、开关不同时刻和不平衡负荷。
- 与详细开关、饱和变压器、换流器和保护模型直接在相坐标下耦合。
- 避免频率相关或不对称系统中模态变换矩阵不稳定或难以对角化的问题。

## 主要分支与机制

- 相域线路和电缆：以 $R_{abc}(\omega)$、$L_{abc}(\omega)$、$G_{abc}(\omega)$、$C_{abc}(\omega)$ 等矩阵表示多导体参数。
- 相域网络方程：支路伴随模型直接贡献到 [[nodal-admittance-matrix]]，非对角项表示相间耦合。
- 相域机器和变压器：在三相变量下表示绕组连接、磁链耦合和非线性，适合不平衡和内部故障。
- 相域-模域混合：某些线路模型仍可在内部使用模态传播，在网络接口处回到相域。

## 形式化表达

多导体相域电报方程可写为：

$$
-\frac{\partial v_{abc}}{\partial x}=R_{abc} i_{abc}+L_{abc}\frac{\partial i_{abc}}{\partial t},\qquad
-\frac{\partial i_{abc}}{\partial x}=G_{abc} v_{abc}+C_{abc}\frac{\partial v_{abc}}{\partial t}
$$

离散进入网络方程时，常表现为矩阵伴随模型：

$$
i_{abc,k}=Y_{\mathrm{eq}}v_{abc,k}+i^{\mathrm{hist}}_{abc,k}
$$

其中 $Y_{\mathrm{eq}}$ 通常不是对角矩阵。相域模型的优势和成本都来自这些耦合项是否被保留。

## 适用边界与失败模式

- 相域模型更适合不平衡和耦合显著的系统，但不自动保证更准确；参数来源和频带仍是核心限制。
- 如果线路近似对称且研究对象为工频正序响应，序分量或模域模型可能足够。
- 满矩阵耦合会增加计算成本；大规模系统中需要稀疏化、分区或等值策略。
- 频率相关相域模型进入时域时仍需检查有理拟合、无源性和时域误差。

## 代表性来源

- [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga-]] 支撑相域频变线路模型和实时/硬件实现讨论。
- [[application-of-frequency-partitioning-fitting-to-the-phase-domain-frequency-depe]] 可作为相域频变拟合方法来源入口。
- [[phase-domain-model-of-twelve-phase-synchronous-machine-for-emtp-type-simulation]] 支撑多相机器相域建模的来源入口。
- [[an-efficient-phase-domain-synchronous-machine-model-with-constant-equivalent-adm]] 可用于理解相域同步机常导纳等值的计算边界。

## 与相关页面的关系

- [[phase-domain-model]] 是相域模型概念页，本页更强调建模工作流。
- [[unbalanced-fault-analysis]] 是相域建模的重要应用。
- [[frequency-dependent-line-model]] 和 [[frequency-dependent-modeling]] 处理频变参数进入相域或模域的问题。
- [[modal-transformation]] 说明通过变换解耦的替代路线。

## 开放问题

- 如何在大规模网络中保持相域耦合，同时控制矩阵规模和实时性。
- 如何为相域频变模型报告拟合频带、无源性和时域误差。
- 如何在相域模型、序分量模型和保护算法之间保持一致的故障解释。
