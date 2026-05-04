---
title: "三相瞬时值模型 (Three-Phase Instantaneous Model)"
type: method
tags: [three-phase, instantaneous, abc-domain, phase-domain, electromagnetic]
created: "2026-05-02"
---

# 三相瞬时值模型 (Three-Phase Instantaneous Model)

## 定义与边界

三相瞬时值模型在 $abc$ 相域直接表示电压、电流、磁链和控制注入的时间函数：

$$
\mathbf{v}_{abc}(t)=
\begin{bmatrix}
v_a(t)\\
v_b(t)\\
v_c(t)
\end{bmatrix},\qquad
\mathbf{i}_{abc}(t)=
\begin{bmatrix}
i_a(t)\\
i_b(t)\\
i_c(t)
\end{bmatrix}.
$$

它是 EMT 时域建模的基本形式之一。与 [[phasor-model]] 不同，瞬时值模型不要求波形是单频正弦；与 [[average-value-model]] 不同，它可以保留开关纹波、暂态偏置和相间不平衡；与 [[dq-transformation]] 不同，它不依赖同步旋转坐标系。

## EMT 中的作用

三相瞬时值模型用于直接求解以下 EMT 问题：

- 三相线路、变压器、电机和负荷的相域耦合。
- 单相接地、两相短路、断相、非全相重合闸等不平衡工况。
- 电力电子开关波形、谐波、暂态过电压和控制注入。
- 饱和、非线性电阻、电弧和保护动作引起的非正弦暂态。

它通常需要比相量或平均模型更细的时间离散和更完整的网络状态，因此应按研究目标选择模型层级。

## 核心方程

线性三相支路可写为：

$$
\mathbf{v}_{abc}=\mathbf{R}_{abc}\mathbf{i}_{abc}
+\frac{d\boldsymbol{\psi}_{abc}}{dt},
\qquad
\boldsymbol{\psi}_{abc}=\mathbf{L}_{abc}\mathbf{i}_{abc}.
$$

若电感矩阵随时间或饱和状态变化：

$$
\mathbf{v}_{abc}=\mathbf{R}_{abc}\mathbf{i}_{abc}
+\mathbf{L}_{abc}\frac{d\mathbf{i}_{abc}}{dt}
+\frac{d\mathbf{L}_{abc}}{dt}\mathbf{i}_{abc}.
$$

电容支路可写为：

$$
\mathbf{i}_{abc}=\frac{d\mathbf{q}_{abc}}{dt},\qquad
\mathbf{q}_{abc}=\mathbf{C}_{abc}\mathbf{v}_{abc}.
$$

节点法 EMT 中，离散化后的相域网络通常形成分块导纳方程：

$$
\mathbf{Y}_{abc}\mathbf{V}_{abc}=\mathbf{I}_{abc},
$$

其中每个物理节点可包含三相电压未知量，也可根据接线方式包含零序和接地支路。

瞬时有功功率直接由相量乘积求和：

$$
p(t)=\mathbf{v}_{abc}^{T}(t)\mathbf{i}_{abc}(t)
=v_a i_a+v_b i_b+v_c i_c.
$$

## 变体

| 变体 | 保留内容 | 典型用途 |
|------|----------|----------|
| 纯 $abc$ 相域模型 | 三相瞬时电压电流 | EMT 网络主方程、不平衡故障 |
| 相域耦合矩阵模型 | 相间互感、互容和接地耦合 | 线路、变压器、电缆 |
| 开关函数驱动模型 | $s_a,s_b,s_c$ 对瞬时电压的作用 | VSC、MMC、整流器 |
| 瞬时空间矢量 | $\alpha\beta$ 或复空间矢量 | 调制分析和瞬时功率 |
| 多速率相域模型 | 子系统不同步长 | 大系统 EMT 和电力电子局部细化 |

## 与相量和平均模型的区别

| 维度 | 三相瞬时值模型 | 相量模型 | 平均值模型 |
|------|----------------|----------|------------|
| 基本变量 | $v_a(t),v_b(t),v_c(t)$ | 基频幅值和相角 | 周期平均状态或调制量 |
| 频率内容 | 由步长和模型决定 | 选定频率为主 | 低频和控制动态为主 |
| 开关细节 | 可显式保留 | 不保留 | 通常平均掉 |
| 不平衡 | 直接表示 | 需序分量或多相量 | 取决于模型结构 |
| 主要风险 | 计算成本和参数细节 | 忽略暂态和谐波 | 忽略纹波和器件事件 |

## 适用边界与失败模式

- **参数不足**：相域互感、互容、接地和饱和参数不足时，模型形式再详细也不能保证可信。
- **步长不足**：高频暂态、开关沿和行波需要与最高关注频率匹配的离散策略。
- **坐标混用**：$abc$、$\alpha\beta$、$dq$ 和相量变量必须标明参考系，避免把平均量和瞬时量相加。
- **理想化开关**：若只用理想开关函数，器件损耗、反向恢复和寄生振荡仍不可见。
- **后处理误读**：从瞬时波形提取 RMS、频谱或序分量时，窗口长度和暂态区间会影响结论。

## 代表性证据边界

- [[three-phase-transformer-modelling-for-fast-electromagnetic-transient-studies-pow]] 代表三相变压器 EMT 建模中的相域问题，不能外推为所有设备参数均可简化。
- [[a-phase-domain-synchronous-machine-modeling-technique-by-using-magnetic-circuit-]] 代表相域同步机模型路线，适用于其磁路和机器假设。
- [[the-impact-of-frame-transformations-on-power-system-emt-simulation]] 说明坐标变换会影响 EMT 实现和解释，不能把不同参考系结果直接混同。
- [[phase-domain-modeling]] 和 [[time-domain-formulation]] 提供相域与时域建模的相邻概念。

## 与相关页面的关系

- [[phasor-model]]：三相瞬时值在正弦稳态、单频假设下可压缩为相量。
- [[switching-function-method]]：把开关状态映射为瞬时相电压或线电压。
- [[switch-modeling]]：决定开关事件和器件非理想性的表示层级。
- [[coordinate-transformation]]、[[dq-transformation]]、[[symmetrical-components]]：提供从相域到变换域的分析工具。
- [[nodal-analysis]]：提供相域网络方程组装基础。

## 开放问题

三相瞬时值模型的难点在于边界选择：哪些子系统必须保持相域瞬时细节，哪些可以用平均值、相量或等值模型替代。模型降阶或混合仿真时，应记录被丢弃的频率分量、相间耦合和事件逻辑。
