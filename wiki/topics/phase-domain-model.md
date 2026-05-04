---
title: "相域模型 (Phase-Domain Model)"
type: topic
tags: [phase-domain, model, transmission-line, unbalanced, untranspose, asymmetrical]
created: "2026-05-02"
---

# 相域模型 (Phase-Domain Model)

## 定义与边界

相域模型（Phase-Domain Model）是在 $abc$ 相坐标中直接表示线路、变压器、电机、电缆、故障和控制接口的建模路线。它保留相间耦合、不对称参数、非换位结构和任意相别故障，而不是先假设三相完全对称再解耦到模域或序域。

本页讨论相域建模的主题边界。它不同于 [[phase-domain-modeling]] 方法页，也不同于 [[symmetrical-components]] 的序域分析工具。相域模型不是自动更“精确”的模型；它只是减少了对称性和常数变换假设，代价是矩阵维度、参数辨识、频变拟合和数值稳定性要求更高。

## EMT 中的作用

EMT 仿真常以相电压和相电流作为网络接口，因此相域模型是非对称线路、不平衡故障、多芯电缆、三相变压器、同步机和电力电子接口的重要底层表达。它适合研究：

- [[unbalanced-fault-analysis]]、非全相运行和保护测量中的相别差异。
- 非换位或不完全换位线路中的负序、零序和相间耦合。
- [[frequency-dependent-line-model]]、电缆护层、铠装层和接地导体的多导体宽频传播。
- 三相三柱变压器、相域同步机和饱和磁路引起的相间耦合。
- [[real-time-simulation]] 中需要保留相域频变线路而又满足固定步长约束的硬件实现。

## 主要分支与机制

相域网络的基本端口形式为

$$
\mathbf{i}_{abc}(s)=\mathbf{Y}_{abc}(s)\mathbf{v}_{abc}(s),
\qquad
\mathbf{Y}_{abc}(s)=\mathbf{Z}_{abc}^{-1}(s).
$$

其中 $\mathbf{v}_{abc}=[v_a,v_b,v_c]^T$，$\mathbf{i}_{abc}=[i_a,i_b,i_c]^T$，$\mathbf{Z}_{abc}$ 是相域阻抗矩阵。非对角元素 $Z_{ab},Z_{bc},Z_{ca}$ 表示相间互耦；若线路、回流路径或几何不对称，矩阵元素随相别和频率变化。

对频变线路，常见宽频表达为

$$
\mathbf{Z}_{abc}(\omega)=\mathbf{R}(\omega)+j\omega\mathbf{L}(\omega),
\qquad
\mathbf{Y}_{sh,abc}(\omega)=\mathbf{G}(\omega)+j\omega\mathbf{C}(\omega).
$$

其中 $\mathbf{R},\mathbf{L},\mathbf{G},\mathbf{C}$ 分别表示频率相关的电阻、电感、电导和电容矩阵。进入时域 EMT 时，这些频响通常需要有理函数拟合、递归卷积或状态空间实现。

相域与模域的差异可概括为：模域通过变换 $\mathbf{T}$ 试图解耦传播模态，$\mathbf{v}_{m}=\mathbf{T}^{-1}\mathbf{v}_{abc}$；相域则保留耦合矩阵，避免把频变或不对称的 $\mathbf{T}(\omega)$ 简化为常数矩阵。是否值得这样做取决于不对称程度、目标频带和计算约束。

## 适用边界与失败模式

- 相域模型需要完整的相间和对地参数。若几何、土壤、电缆护层、接地方式或测量数据不足，直接相域计算也可能只是精细外壳。
- 对宽频模型，逐元素拟合可能破坏矩阵无源性或互易性；需要 [[passivity-enforcement]]、误差检查和时域稳定验证。
- 矩阵维度随导体数和节点数增加。三相网络约为正序网络的三倍维度，多导体电缆还会继续扩大。
- 相域模型保留不平衡，但不自动处理非线性磁路、电弧、避雷器或控制限幅；这些仍需独立模型。
- 实时或 FPGA 实现中的步长、定点/浮点格式和流水线资源结论必须绑定平台，不能从单篇线路算例外推。

## 代表性来源

- [[application-of-frequency-partitioning-fitting-to-the-phase-domain-frequency-depe]] 将频域分区拟合用于相域频变架空线建模，支撑“相域宽频矩阵拟合需要误差和稳定性检查”的讨论。
- [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga-]] 讨论 FPGA 上的相域频变线路实时模型；其步长和资源结论应限定在原文线路规模和硬件平台。
- [[an-efficient-phase-domain-synchronous-machine-model-with-constant-equivalent-adm]] 可作为相域同步机恒等效导纳模型的来源入口。
- [[phase-domain-model-of-twelve-phase-synchronous-machine-for-emtp-type-simulation]] 可作为多相同步机相域 EMT 模型的来源入口。
- [[modeling-and-application-of-dq-sequence-dynamic-phasors-under-unbalanced-ac-cond]] 可用于连接相域不平衡波形和 dq 序动态相量表示。

## 与相关页面的关系

- [[phase-domain-modeling]] 是更具体的方法页；本页说明相域模型作为主题的边界。
- [[modal-transformation]] 和 [[modal-domain-decoupling]] 解释模域路线；它们与相域模型是建模坐标选择的两端。
- [[symmetrical-components]] 与 [[sequence-component-method]] 适合工频序域解释；相域模型适合直接处理不对称 EMT 波形。
- [[frequency-dependent-line-model]]、[[universal-line-model]] 和 [[wideband-modeling]] 是相域宽频线路的重要相邻模型和方法。
- [[unbalanced-fault-analysis]] 是相域模型的典型应用场景，但故障模型和保护逻辑仍需单独定义。

## 开放问题

- 如何为相域频变模型建立统一的拟合误差、无源性、互易性和时域稳定报告格式。
- 如何在大规模 EMT 中平衡相域保真度、矩阵规模和实时仿真约束。
- 如何把相域模型参数从几何计算、现场测量和设备厂家数据中一致地追溯。
- 如何判断一个问题应使用相域模型、模域模型、序域模型或混合表示，而不是默认采用最复杂模型。
