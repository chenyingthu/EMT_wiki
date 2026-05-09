---
title: "相域建模 (Phase-Domain Modeling)"
type: method
tags: [phase-domain, abc, three-phase, instantaneous, unbalanced, coupled]
created: "2026-05-02"
---

# 相域建模 (Phase-Domain Modeling)


```mermaid
graph TD
    subgraph Ncmp[相域建模 (Phase-Domain Modeling)]
        N0[输电线路: 多相阻抗、导纳、传播和历史项矩阵]
        N1[变压器: 绕组连接、漏抗、磁化和中性点约束]
        N2[旋转电机: abc 端口、电感矩阵或 VBR/等值源接口]
        N3[变流器: 开关函数、受控源、平均值模型或 Norton 注入]
        N4[故障和保护: 相别、故障阻抗、断路器和测量链]
    end
```


## 定义与边界

相域建模是在物理相坐标或导体坐标中直接表示电压、电流、磁链和端口约束的方法。三相系统中常写作 abc 建模；多导体线路和电缆中也可扩展为导体域或相域矩阵。

本页讨论 EMT 方法层面的相域建模，不等同于某个具体软件、某个设备模型或“永远更精确”的结论。相域模型能保留不平衡、互耦和开关细节，但可信度仍取决于参数、频带、离散化、事件处理和验证来源。

## EMT 中的作用

EMT 主网络通常以节点电压和支路电流的瞬时值求解，因此相域建模是许多元件的自然接口。它适合：

- 不平衡故障、非全相运行和单相设备接入。
- 变压器连接、接地通道、三角形环流和零序路径。
- 电力电子开关、PWM、限流和保护闭环。
- 频率相关线路、电缆护套、平行线路互耦和非换位线路。
- 电机与网络的 abc 端口接口，即使内部状态使用 dq 坐标。

当研究对象近似平衡、线性且关注基频相量时，[[symmetrical-components]] 和 [[sequence-network-model]] 可能更紧凑；当关注控制器内部变量时，[[dq-transformation]] 可能更便于表达。

## 核心方程

相域网络变量可写为

$$
\mathbf{v}_{abc}=
\begin{bmatrix} v_a \\ v_b \\ v_c \end{bmatrix},
\qquad
\mathbf{i}_{abc}=
\begin{bmatrix} i_a \\ i_b \\ i_c \end{bmatrix}.
$$

线性集中参数支路的一般形式为

$$
\mathbf{v}_{abc}
=\mathbf{R}\mathbf{i}_{abc}
+\frac{d}{dt}\boldsymbol{\psi}_{abc},
\qquad
\boldsymbol{\psi}_{abc}=\mathbf{L}(\mathbf{x},t)\mathbf{i}_{abc}.
$$

其中 $\mathbf{L}$ 可以包含自感、互感、转子位置依赖或饱和状态依赖。离散化后，支路通常通过 [[companion-circuit]] 形成等效导纳和历史源，进入 [[nodal-admittance-matrix]]：

$$
\mathbf{Y}_{n+1}\mathbf{v}_{n+1}
=\mathbf{i}_{src,n+1}+\mathbf{i}_{hist,n+1}.
$$

若开关、饱和或控制约束使方程非线性，上式会成为需要迭代求解的残差系统。

## 典型模型对象

| 对象 | 相域表示 | 关键边界 |
|---|---|---|
| 输电线路 | 多相阻抗、导纳、传播和历史项矩阵 | 频率相关、换位、地回路和互耦需说明 |
| 变压器 | 绕组连接、漏抗、磁化和中性点约束 | 零序通路和饱和不能用理想三相平均替代 |
| 旋转电机 | abc 端口、电感矩阵或 VBR/等值源接口 | 内部 dq 与外部 abc 的同步离散化需验证 |
| 变流器 | 开关函数、受控源、平均值模型或 Norton 注入 | PWM、采样延迟、限流和拓扑切换影响结果 |
| 故障和保护 | 相别、故障阻抗、断路器和测量链 | 动态电弧和互感器暂态需要专门模型 |

## 与坐标变换的关系

相域建模并不排斥坐标变换。常见组合包括：

- 主网络保持 abc，相域端口直接求解。
- 电机内部用 dq 或 VBR 状态，端口通过 abc 等效接入网络。
- VSC 控制器测量 abc 电压电流，经 dq 变换生成指令，再反变换为调制参考。
- 线路模型在内部使用模态通道，最终仍把端口量变回相域。

关键是记录坐标变换发生在哪里、哪些状态被保留、哪些历史项被映射，以及变换误差是否进入主网络。

## 优势与代价

相域模型的优势是边界条件直接、相别清楚、零序和不平衡通道显式，并且可自然表示开关和非线性。代价是矩阵规模和耦合程度较高，某些设备会出现时变电感或频变矩阵，实时仿真和大规模网络中需要矩阵复用、端口等效或模型降阶。

因此页面不应写“相域一定更准确”或“dq 一定更快”。精度和效率要看被建模对象、数值方法、步长、稀疏结构和验证目标。

## 适用边界与失败模式

- 参数矩阵缺少物理来源，虽然形式上是相域，结果仍不可验证。
- 忽略互感、接地、电缆护套或三角形环流，会削弱相域模型的主要价值。
- 对强开关和断续事件不做事件定位或历史项重置，会产生数值振荡和虚假能量。
- 时变电感矩阵若每步更新不一致，可能导致网络矩阵频繁重构或接口延迟。
- 平均值模型不能自动代表开关级 EMT；开关模型也不自动代表器件寄生和高频封装效应。
- 用单篇论文的提速、误差或步长结果外推到所有相域模型，是不受支持的强断言。

## 代表性证据

[[a-voltage-behind-reactance-synchronous-machine-model-for-the-emtp-type-solution]] 说明同步机 EMT 中相域端口接口与内部 dq 状态的组合可以减少传统接口问题；其量化效率只适用于原文算例。[[multi-scale-induction-machine-model-in-the-phase-domain-with-constant-inner-impe]] 支撑感应机相域网络接口和恒定内导纳的建模路线，但其适用范围受解析信号、偏移频率和原文测试场景约束。

[[universal-line-model]]、[[distributed-parameter-line]] 和 [[modal-domain-decoupling]] 说明线路模型可在相域和模态域之间权衡；非换位、频变和强互耦场景不应默认常数模态变换充分。

## 与相关页面的关系

- [[three-phase-instantaneous-model]]：三相瞬时量模型入口。
- [[coordinate-transformation]]：相域与 alpha-beta、dq、序分量和模态域之间的变换。
- [[dq-transformation]]：控制器和电机内部旋转坐标。
- [[symmetrical-components]] 和 [[sequence-network-model]]：基频不平衡相量分析。
- [[time-domain-formulation]]：相域方程如何进入 EMT 时域求解。
- [[nodal-admittance-matrix]] 和 [[companion-circuit]]：相域网络离散和求解结构。

## 修订与证据使用注意事项

后续扩展应优先补充模型输入、输出、端口变量、参数来源和验证对象。不要新增未绑定来源的典型步长、平台能力、误差百分比或“完全捕捉所有暂态”等强断言。
