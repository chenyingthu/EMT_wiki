---
title: "多端直流电网-mtdc"
type: method
tags: [多端直流电网-mtdc, high-value-link]
created: "2026-05-05"
---

# 多端直流电网-mtdc

## 定义与边界

多端直流电网-mtdc是电力系统电磁暂态仿真中的重要概念，涉及电力网络的分析与建模。

**边界限定**：待进一步完善。

## EMT中的作用

- 支撑电力系统暂态过程分析
- 为保护和控制设计提供仿真验证
- 与[[emt-simulation]]紧密相关


基于相关研究的技术应用：

## 主要分支与机制

- 基础理论与方法
- 数值实现技术
- 工程应用案例

## 形式化表达


### 核心数学表达

从相关研究提取的关键公式：

$$\begin{cases}J\frac{d\omega}{dt}=\frac{P_m}{\omega_0}-\frac{P_e}{\omega_0}-D(\omega-\omega_0)\\\frac{d\theta}{dt}=\omega\end{cases}$$

$$P_m=P_{ref}+K_f(\omega_n-\omega)$$

$$

*有功功率参考值生成式，体现一次调频下垂特性。*

**公式3**: $$

$$\begin{cases}Q_m=Q_{ref}+K_v(U_n-U)\\e_d=\frac{K}{s}(Q_m-Q_e)\end{cases}$$

$$

*无功-电压积分下垂控制方程，用于模拟同步机励磁调节特性。*

**公式4**: $$

数学模型与公式

## 适用边界与失败模式

- 模型精度与计算效率的权衡
- 参数敏感性分析

## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- power-system - 电力系统基础
- [[electromagnetic-transient]]
## 代表性来源

- [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems]]
学术文献

---

*本页面为自动生成的增强模板，需要进一步补充专业内容。*
