---
title: "详细等效模型-dem"
type: method
tags: [详细等效模型-dem, high-value-link]
created: "2026-05-05"
---

# 详细等效模型-dem

## 定义与边界

详细等效模型-dem是电力系统电磁暂态仿真中的重要概念，涉及电力网络的分析与建模。

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

$$-\frac{dV(x,s)}{dx}=Z(s)I(x,s),\qquad -\frac{dI(x,s)}{dx}=Y(s)V(x,s)$$

$$Z(s)=Z_C(s)+Z_E(s)+Z_G(s)$$

$$Z_G(s)=sL_0$$

$$Y(s)=sC_0$$

$$-\frac{dV(x,s)}{dx}=\left(R'(s)+L_0s\right)I(x,s)$$

数学模型与公式

## 适用边界与失败模式

- 模型精度与计算效率的权衡
- 参数敏感性分析

## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- power-system - 电力系统基础
- [[electromagnetic-transient]]
## 代表性来源

- [[parallelization-of-mmc-detailed-equivalent-model]]
学术文献

---

*本页面为自动生成的增强模板，需要进一步补充专业内容。*
