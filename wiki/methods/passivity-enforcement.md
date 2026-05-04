---
title: "无源性强制 (Passivity Enforcement)"
type: method
tags: [passivity, stability, vector-fitting, frequency-domain]
created: "2026-04-13"
---

# 无源性强制 (Passivity Enforcement)

## 定义与边界

无源性强制是对频域辨识或有理函数拟合得到的多端口模型进行检测和修正，使其在互联到 EMT 网络后不产生非物理净能量的后处理方法。它常用于 [[vector-fitting]]、[[wideband-modeling]]、[[fdne-model]]、[[frequency-dependent-line-model]]、[[cable-model]] 和变压器宽频端口模型。

本页讨论“拟合模型如何被修正为可互联的无源端口模型”，不替代原始频响测量、参数辨识、模型阶数选择或 [[state-space-method]] 实现。无源性强制也不保证模型物理正确；若频率采样、端口定义、DC 值、时延或测量数据本身错误，强制过程只能把错误模型改成更稳定的错误模型。

## EMT 中的作用

频率相关线路、电缆、FDNE 和测量型端口模型经有理函数进入时域后，会与外部网络、控制器和数值积分器闭合互联。若模型在某些频率表现为非无源，时域仿真可能出现与实际能量流不一致的增长，表现为接口振荡、长时间仿真发散或 HIL 中的非物理响应。

因此，在 EMT 工作流中，无源性强制通常位于“频域拟合完成”和“时域接入仿真”之间。通过该步骤后，仍需重新检查拟合误差、极点稳定性、DC/高频渐近值、时域阶跃响应和目标算例波形；只报告无源性通过不足以证明模型可用于所有故障或开关暂态。

## 核心机制

对线性多端口导纳模型 $Y(s)$，常见频域无源性检查是要求：

$$\lambda_{\min}\left(\Re\{Y(j\omega)\}\right)\ge 0$$

其中 $\lambda_{\min}$ 是实部矩阵的最小特征值。若在某个频率 $\omega_v$ 出现负特征值，该频点可视为无源性违规候选。状态空间模型也可用 Hamiltonian 或相关正实性测试定位违规频率；含时延和复杂传播函数时，频率扫描仍是常见的保守检查。

强制过程一般包括：

1. 检测违规频段和关联端口/模态。
2. 选择修正变量，如留数、极点、常数项、对角电导或局部滤波器。
3. 约束修正后 $\Re\{Y(j\omega)\}$ 非负，同时最小化对原频响的扰动。
4. 重新验证无源性、拟合误差和时域仿真稳定性。

## 分类与变体

| 方法 | 修正对象 | 优点 | 边界 |
|------|----------|------|------|
| 残差/留数摄动 | 有理函数留数或矩阵元素 | 对已有极点结构扰动较小 | 对复杂多频段违规自由度有限 |
| 全摄动形式 | 极点、留数和常数项 | 可处理更复杂违规 | 优化复杂度和实现风险更高 |
| 人工电导或高频约束 | 端口导纳或渐近项 | 工程实现直接 | 可能改变低频或高频物理含义 |
| 无源 RLC 补偿 | 局部无源支路 | 便于解释和 EMT 实现 | 适合局部违规，不保证全局最优 |
| 在线局部补偿 | 运行时子网络补偿 | 适合部分混合仿真和 HIL 场景 | 需要实时计算预算和严格接口验证 |

## 适用边界与失败模式

- 无源性是互联稳定性的必要检查之一，不等同于拟合精度、因果性、参数正确性或工具级验证。
- 强制后的模型必须重新比较原始频响；过度补偿可能消除违规但破坏谐振峰、传播延时或 DC 值。
- 对含传输时延的线路模型，有限维正实测试可能不覆盖所有风险，应结合宽频扫描和时域算例。
- 多端口模型的端口方向、单位和参考地错误会导致无源性判断失真。
- 单篇论文中的收敛次数、误差百分比或频带范围只支撑其算例；本页不把这些数字写成通用参数。

## 代表性来源

| 来源 | 可支撑的内容 | 使用边界 |
|------|--------------|----------|
| [[passivity-enforcement-for-transmission-line-models]] | 线路模型无源性检测和修正的早期代表 | 结论应限定在原文 ULM/线路算例 |
| [[robust-passivity-enforcement-scheme-for]] | 鲁棒无源性强制方案入口 | 需回查原文确定修正变量和测试条件 |
| [[development-and-applicability-of-online-passivity-enforced-wide-band-multi-port-]] | 在线无源性强制宽频多端口模型 | 实时性结论受平台和网络规模约束 |
| [[a-two-layer-network-equivalent-with-local-passivity-compensation-with-applicatio]] | 双层网络等值和局部无源性补偿 | 不等同于所有 FDNE 都可局部修复 |
| [[passivity-enforcement-of-wideband-line-model-through-coupled-perturbation-of-res]] | 宽频线路模型耦合摄动修正 | 量化表现需绑定原文频带和模型 |
| [[passivity-enforcement-of-wideband-model-through-a-new-and-full-perturbation-form]] | 全摄动形式的宽频模型修正 | 不能外推为所有复杂多端口模型最优 |

## 与相关页面的关系

- [[vector-fitting]] 解决频域响应到有理函数的拟合；本页处理拟合后的无源性违规。
- [[wideband-modeling]] 描述宽频建模总流程；无源性强制是其中的验证与后处理步骤。
- [[fdne-model]]、[[frequency-dependent-line-model]]、[[transmission-line-model]] 和 [[cable-model]] 是最常见的下游应用对象。
- [[state-space-method]] 和 [[partial-fraction-expansion]] 说明时域实现形式；本页强调这些实现形式的能量一致性检查。
- [[numerical-stability]] 关注仿真算法稳定；无源性强制关注端口模型互联后的物理能量边界。
