---
title: "并行输电线路 (Parallel Transmission Line)"
type: method
tags: [parallel-line, mutual-coupling, zero-sequence, transposition, distance-protection]
created: "2026-05-02"
---

# 并行输电线路 (Parallel Transmission Line)

## 定义与边界

并行输电线路是指两回或多回线路在同一走廊、同塔、邻近走廊或部分区段中相互接近，使线路之间存在互感、互容和共同大地返回路径耦合的线路系统。本页关注线路本体的 EMT 建模边界：如何组织相域/序域矩阵、如何处理跨回耦合、何时需要频变或相域模型。

本页不负责保护判据整定，保护问题由 [[parallel-line-protection]] 处理；也不把并行线路简化为固定零序互感比例。耦合强弱取决于几何、换位、接地线、土壤参数、并行长度、运行方式和频率范围。

## EMT 中的作用

在 EMT 仿真中，并行线路建模通常需要回答三件事：

- 两回线路之间的互阻抗和互导纳是否会影响目标暂态。
- 能否用固定模态或序分量近似解耦，还是必须保留完整相域耦合。
- 平行区段、非平行区段、终端设备和故障点如何在网络拓扑中连接。

典型输入包括每根导体的坐标、半径、分裂导线参数、接地线、土壤模型、频率采样、线路区段长度和换位方式。输出通常是多导体单位长度矩阵 $\mathbf{Z}(\omega)$、$\mathbf{Y}(\omega)$，或可直接进入 EMT 的线路端口模型。

## 核心机制

对双回三相线路，可把相域电压电流写成分块矩阵：

$$
\begin{bmatrix}\mathbf{V}_1\\\mathbf{V}_2\end{bmatrix}
=
\begin{bmatrix}
\mathbf{Z}_{11} & \mathbf{Z}_{12}\\
\mathbf{Z}_{21} & \mathbf{Z}_{22}
\end{bmatrix}
\begin{bmatrix}\mathbf{I}_1\\\mathbf{I}_2\end{bmatrix}
$$

其中 $\mathbf{Z}_{11}$、$\mathbf{Z}_{22}$ 是各回线路自阻抗块，$\mathbf{Z}_{12}$、$\mathbf{Z}_{21}$ 是跨回互阻抗块。并联电容和对地电容也可用同样的分块导纳矩阵表示。

若换位和几何足够对称，序域中正序、负序通道可能弱耦合，而零序通道仍可能保留跨回耦合：

$$
\begin{bmatrix}V_{0,1}\\V_{0,2}\end{bmatrix}
=
\begin{bmatrix}
Z_{0,1} & Z_{0,12}\\
Z_{0,21} & Z_{0,2}
\end{bmatrix}
\begin{bmatrix}I_{0,1}\\I_{0,2}\end{bmatrix}
$$

该式只是结构表达。$Z_{0,12}$ 不能用无来源的固定比例代替，应由线路参数计算或实测/工具参数生成。

## 建模路线

| 路线 | 机制 | 适合用途 | 主要边界 |
|------|------|----------|----------|
| 完整相域多导体模型 | 保留全 $\mathbf{Z},\mathbf{Y}$ 矩阵 | 强耦合、非换位、混合区段 | 参数和拟合成本高 |
| 固定模态域模型 | 用常数变换矩阵分离模态 | 近似换位、耦合较弱或平台限制 | 可能漏掉跨回互耦 |
| 独立线路加互耦补偿 | 各回线路独立 FD-line，跨回耦合另作状态空间模型 | 平台只有 FD-line 时评估邻线扰动 | 需要单独验证互耦拟合 |
| 序域近似 | 重点保留零序互感 | 工频接地故障、保护初筛 | 宽频暂态和不平衡几何不足 |
| 分段模型 | 平行区段和非平行区段分别建模 | 部分平行线路、线路交叉 | 边界反射和参数连续性需检查 |

## 与换位和坐标变换的关系

换位可降低相间不平衡，但不必然消除跨回耦合。对同塔双回、不同电压等级共走廊或局部平行线路，应区分：

- 单回内部三相是否近似平衡。
- 两回之间同名相、异名相和地线之间是否仍有强互耦。
- 零序/地模返回路径是否受土壤和接地线状态影响。
- 常数模态变换是否在目标频带内保持有效。

这些判断分别连接到 [[transposed-three-phase-line]]、[[balanced-three-phase-line]]、[[modal-domain-decoupling]] 和 [[frequency-dependent-soil]]。

## 适用边界与失败模式

- 把“同走廊”直接写成“必须强耦合”或“必须使用 6x6 矩阵”都过强；需要按目标暂态和参数证据判断。
- 只保留零序互感可能足以做工频保护初筛，但不足以描述雷电、开关陡波和邻线高频感应。
- 常数模态 FD-line 对平行线路互耦可能不足，尤其当跨回弱模态被公共模态掩盖时。
- 部分平行线路需要分段和端口连接，不能用全长均匀平行模型替代。
- 土壤频变和大地返回路径会改变地模和零序通道，应与 [[earth-return-impedance]] 一起处理。

## 代表性证据

- [[modal-domain-based-modeling-of-parallel-transmission-lines]]：支撑“自线路传播”和“跨线路互耦”可分开建模的工程折中路线；其证据主要覆盖平行架空线路和铁路信号耦合场景，不应外推到所有线路结构。
- [[frequency-dependent-transformation-matrices-for-untransposed-transmission-lines-]]：支撑非换位/强不对称线路中频率相关变换矩阵可能影响模态解耦。
- [[locating-arc-faults-on-coupling-two-parallel-transmission-lines-using-the-novel-]] 可作为平行线路耦合量进入故障定位/保护应用的来源入口，具体判据属于 [[parallel-line-protection]]。
- [[double-ended-fault-locating-method-for-parallel-lines-without-measuring-parallel]] 可作为故障测距中处理平行回线量不可测问题的来源入口。

## 与相关页面的关系

- [[parallel-line-protection]]：保护判据、互感补偿和行波保护边界。
- [[mutual-impedance]]：互阻抗参数本身。
- [[transposed-three-phase-line]] 和 [[balanced-three-phase-line]]：内部三相平衡与换位假设。
- [[modal-domain-decoupling]]：相域到模域解耦的条件和失败模式。
- [[transmission-line-model]]、[[frequency-dependent-line-model]] 和 [[universal-line-model]]：线路模型总入口和频变实现。

## 修订与证据使用注意事项

后续补充应避免加入未来源绑定的零序互感典型值、线路间距阈值、保护误动率或电压等级结论。若要比较模型精度，应写明线路几何、并行长度、土壤参数、频带、终端条件和参考模型。
