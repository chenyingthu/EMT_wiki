---
title: "开关函数法 (Switching Function Method)"
type: method
tags: [switching-function, average-value, modulation, converter, power-electronics]
created: "2026-05-02"
---

# 开关函数法 (Switching Function Method)

## 定义与边界

开关函数法用离散或连续函数表示功率电子开关网络的连接状态。最简单的半桥可写为：

$$
s(t)=
\begin{cases}
1, & \text{上桥臂导通}\\
0, & \text{下桥臂导通}
\end{cases}
$$

在详细 EMT 模型中，$s(t)$ 是随触发脉冲和保护逻辑变化的二值信号；在平均模型中，$s(t)$ 可被一个周期平均后的占空比或调制函数替代。二者的证据边界不同，不能把平均开关函数的低频响应等同于详细开关波形。

## EMT 中的作用

开关函数法连接了三类 EMT 建模层级：

- 在 [[switch-modeling]] 中，二值开关函数决定网络拓扑、受控源或等效导纳。
- 在 [[average-value-model]] 中，周期平均后的开关函数生成受控电压源、电流源或等效支路。
- 在 [[state-space-average-method]] 中，开关函数的占空比权重决定平均状态矩阵。

因此，开关函数法本身不是一种精度保证，而是一种把调制、拓扑和方程联系起来的表达方式。

## 核心方程

对两电平桥臂，若 $s_a,s_b,s_c\in\{0,1\}$，可定义极点电压：

$$
v_{xO}=\left(s_x-\frac{1}{2}\right)V_{\mathrm{dc}},\qquad x\in\{a,b,c\}.
$$

若需要去除公共模，可写为相对中性点电压：

$$
\mathbf{v}_{abc}=\left(\mathbf{I}-\frac{1}{3}\mathbf{1}\mathbf{1}^{T}\right)
\left(\mathbf{s}-\frac{1}{2}\mathbf{1}\right)V_{\mathrm{dc}}.
$$

直流侧电流由交流侧电流和开关状态耦合：

$$
i_{\mathrm{dc}}=\mathbf{s}^{T}\mathbf{i}_{abc},
$$

具体符号和比例取决于桥臂定义、极点电压基准和调制方式。对开关周期平均：

$$
d_x(t)=\frac{1}{T_s}\int_{t}^{t+T_s}s_x(\tau)\,d\tau,
$$

可得到平均电压关系：

$$
\bar{\mathbf{v}}_{abc}=
\left(\mathbf{I}-\frac{1}{3}\mathbf{1}\mathbf{1}^{T}\right)
\left(\mathbf{d}-\frac{1}{2}\mathbf{1}\right)V_{\mathrm{dc}}.
$$

## 变体

| 变体 | 表示方式 | 适用问题 |
|------|----------|----------|
| 二值开关函数 | $s(t)\in\{0,1\}$ 或 $\{-1,1\}$ | 详细开关级 EMT、调制逻辑验证 |
| 平均开关函数 | $d(t)\in[0,1]$ | 低频控制和系统级暂态 |
| 多电平开关函数 | 离散电平或投入子模块数 | NPC、CHB、MMC 等拓扑 |
| 空间矢量开关函数 | 电压矢量与作用时间 | PWM 和 SVPWM 调制分析 |
| 谐波开关函数 | 傅里叶系数或频域开关函数 | 周期稳态谐波分析 |

## 适用边界与失败模式

- **死区和互锁**：互补关系 $s_{\mathrm{lower}}=1-s_{\mathrm{upper}}$ 需要修正，否则会低估畸变和桥臂短路风险。
- **器件非理想性**：导通压降、反向恢复、寄生电容和开关损耗不由理想开关函数自动给出。
- **拓扑约束**：多电平和 MMC 模型还需要电容电压、排序均压和子模块旁路状态。
- **平均化失真**：平均开关函数会丢失载波边带、纹波、开关应力和高频共模。
- **事件同步**：详细 EMT 中多个开关同时动作会改变导纳矩阵和历史项，不能只更新代数开关变量。

## 代表性证据边界

- [[combining-detailed-equivalent-model-with-switching-function-based-average-value-]] 代表详细等效模型与开关函数平均值模型的切换路线，不能说明平均模型总能覆盖故障细节。
- [[switch-averaged-frequency-domain-simulation-of-photovoltaic-systems]] 代表开关平均思想在频域仿真中的用法，证据边界是其建模对象和频带。
- [[基于mmc平均值仿真模型的损耗快速评估方法]] 说明平均模型可与损耗估算结合，但损耗公式仍需具体器件和工况校准。

## 与相关页面的关系

- [[switch-modeling]]：处理开关器件、事件和数值实现。
- [[average-value-model]]：使用平均开关函数替代详细开关动作。
- [[state-space-average-method]]：把不同开关状态的状态方程按开关函数平均。
- [[three-phase-instantaneous-model]]：可直接接收 $s_a,s_b,s_c$ 生成的瞬时三相电压。
- [[pwm-modulator-model]]：生成开关函数的控制和调制模型。

## 开放问题

开关函数页应避免把某种调制公式写成所有拓扑的通用关系。实际使用时需要同时说明电压参考点、桥臂极性、死区处理、直流侧电流定义和平均窗口，否则相同符号可能对应不同物理量。
