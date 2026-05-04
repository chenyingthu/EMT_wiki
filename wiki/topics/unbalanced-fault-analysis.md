---
title: "不平衡故障分析 (Unbalanced Fault Analysis)"
type: topic
tags: [fault-analysis, unbalanced, sequence-components, power-system, short-circuit]
created: "2026-05-02"
---

# 不平衡故障分析 (Unbalanced Fault Analysis)

## 定义与边界

不平衡故障分析（Unbalanced Fault Analysis）研究单相接地、两相短路、两相接地、断相、高阻接地和非全相运行等非对称扰动下的电压、电流和保护测量量。它关注相别差异、零序和负序通道、故障阻抗、接地方式以及暂态分量。

本页是 topic 页，讨论不平衡故障在 EMT 语境下的概念边界。它不同于 [[fault-analysis]] 或 [[fault-analysis-methods]] 的方法页，也不替代保护装置模型。传统短路计算可给出工频相量和序网结果；EMT 分析还需要故障施加时刻、直流偏置、控制器限流、CT 饱和、保护采样和开关动作。

## EMT 中的作用

不平衡故障是 EMT 中检验相域模型、接地系统、保护逻辑和电力电子故障响应的重要工况。对于单相接地和两相故障，正序等值无法保留零序通道、非换位耦合和暂态波形；对于 IBR、LCC、MMC 或含大量电缆的网络，控制限流和频变耦合还会改变传统序网假设。

EMT 输出通常包括相电压 $\mathbf{v}_{abc}(t)$、相电流 $\mathbf{i}_{abc}(t)$、序分量、保护滤波后的测量值、故障点能量和断路器开断量。若只报告稳态故障电流最大值，应说明它不是完整的 EMT 证据。

## 主要分支与机制

对称分量法（Symmetrical Components）把相量映射为零序、正序和负序：

$$
\begin{bmatrix} I_0 \\ I_1 \\ I_2 \end{bmatrix}
=\frac{1}{3}
\begin{bmatrix}
1&1&1\\
1&a&a^2\\
1&a^2&a
\end{bmatrix}
\begin{bmatrix} I_a \\ I_b \\ I_c \end{bmatrix},
\qquad a=e^{j2\pi/3}.
$$

其中 $I_a,I_b,I_c$ 是相电流相量，$I_0,I_1,I_2$ 分别为零序、正序和负序分量。对于稳态或准稳态短路，这一变换能清楚说明序网连接；对于 EMT 波形，可对基波相量、滑动窗口或动态相量使用类似分解，但窗口和滤波会影响结果。

典型故障边界条件可写为：

- 单相接地：$I_b=I_c=0,\; V_a=Z_f I_a$，常对应三序串联。
- 两相短路：$I_a=0,\; I_b=-I_c,\; V_b=V_c$，零序通道通常不开通。
- 两相接地：$I_a=0,\; V_b=Z_f I_b,\; V_c=Z_f I_c$，零序和负序均参与。
- 断相：开路相电流为零，残余相的电压和电流由负荷、接地和保护动作决定。

在相域 EMT 中，更一般的写法是直接对三相节点方程施加故障支路：

$$
\mathbf{Y}_{abc,n}\mathbf{v}_{abc,n}
=\mathbf{i}_{abc,n}^{\mathrm{src}}+\mathbf{i}_{abc,n}^{\mathrm{hist}}
\mathbf{Y}_{f,n}\mathbf{v}_{abc,n}.
$$

其中 $\mathbf{Y}_{f,n}$ 是故障支路导纳矩阵，可表示单相接地、相间短路、弧光电阻或时变故障阻抗。

## 适用边界与失败模式

- 序网公式依赖线性、频率固定和参数对称等假设；非换位线路、多导体电缆和饱和变压器可能需要 [[phase-domain-model]]。
- 零序通道取决于变压器接线、接地方式、线路回流路径和土壤参数，不能只从正序阻抗推断。
- 故障阻抗和电弧模型缺失时，故障电流、保护灵敏度和重燃风险只能做保守场景分析。
- 电力电子设备故障响应受控制器限流、PLL、保护闭锁和直流侧动态影响；传统短路公式通常不覆盖这些控制边界。
- 保护结论应绑定测量链、采样率、滤波窗口和动作逻辑；仅有一次 EMT 波形不能证明继电保护总体可靠性。

## 代表性来源

- [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne]] 可作为 LCC 在不平衡交流网络中平均值建模的来源入口；结论应限定在原文控制和网络假设内。
- [[modeling-and-application-of-dq-sequence-dynamic-phasors-under-unbalanced-ac-cond]] 支撑不平衡条件下 dq 序动态相量建模的讨论，适合连接 EMT 与动态相量方法。
- [[decision-tree-based-methodology-for-high-impedance-fault-detection]] 是高阻故障检测的代表来源；其高准确率应限于作者 EMTP 仿真数据和特征集。
- [[analysis-and-general-calculation-of-dc-fault-currents-in-mmc-mtdc-grids]] 与 [[a-method-to-calculate-short-circuit-faults-in-high-voltage-dc-grids]] 可作为直流电网故障电流分析入口，但后者页面存在文献串页风险，使用前需复核 PDF。
- [[an-ultra-fast-mmc-hvdc-fault-location-algorithm-based-on-transient-voltage-featu]] 可作为 MMC-HVDC 暂态故障定位的来源入口，不能外推为所有交流不平衡故障保护。

## 与相关页面的关系

- [[fault-analysis]] 和 [[fault-analysis-methods]] 承载故障计算方法；本页承载不平衡故障主题边界。
- [[symmetrical-components]]、[[sequence-component-method]] 和 [[sequence-network-model]] 解释序域分析工具。
- [[phase-domain-model]] 提供相域建模路线，适合非换位、强耦合和严重不平衡场景。
- [[fault-impedance-model]]、[[grounding-system-model]] 和 [[grounding-system-modeling]] 决定故障支路和回流路径。
- [[relay-protection]]、[[distance-relay]] 和 [[differential-protection]] 使用故障波形，但保护动作还需要测量和逻辑模型。

## 开放问题

- 如何在含 IBR 和 HVDC 的系统中定义可复现的不平衡故障基准。
- 如何把序域解释、相域 EMT 波形和保护滤波输出一致地报告。
- 如何校核高阻故障、电弧接地和间歇性故障的参数，而不把仿真训练集结果外推到现场。
- 如何在大规模配电网中同时保留零序回流、非换位耦合和可承受的计算规模。
