---
title: "Frequency Response"
type: method
tags: [frequency-response]
created: "2026-05-05"
---

# Frequency Response

## 定义与边界

矢量拟合（Vector Fitting）是一种通过极点迁移实现有理函数逼近的两阶段迭代算法。该方法通过引入辅助缩放函数σ(s)，将原始非线性优化问题（同时优化极点和留数）转化为两个线性最小二乘问题。第一阶段通过拟合σ(s)和σ(s)f(s)来重新定位极点（极点识别），利用σ(s)的零点作为改进后的极点；第二阶段利用这些新极点重新拟合原始函数f(s)以确定留数（留数识别）。该方法的关键创新在于允许使用复数起始极点，从而有效处理包含多个谐振峰的非光滑频率响应，避免了传统方法中的病态条件问题。...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，frequency-response在EMT仿真中用于解决特定问题。

基于相关研究，该方法在EMT仿真中的主要应用包括：
- 特定场景的电磁暂态分析
- 控制系统设计与验证
- 故障分析与保护协调

## 主要分支与机制

- 待补充（需要进一步研究确定具体分支）

## 形式化表达


### 核心数学表达

从相关研究提取的关键公式：

$$P(f,V)=P_0\left(\frac{f}{f_0}\right)^{\alpha_f}\left(\frac{V}{V_0}\right)^{\alpha_v}$$

$$Q(f,V)=Q_0\left(\frac{f}{f_0}\right)^{\beta_f}\left(\frac{V}{V_0}\right)^{\beta_v}$$

$$Y(f)=\frac{P(f)-jQ(f)}{V^2}$$

$$Y(f)=\frac{P_0}{V_0^2}\left(\frac{f}{f_0}\right)^{\alpha_f}-j\frac{Q_0}{V_0^2}\left(\frac{f}{f_0}\right)^{\beta_f}$$

$$Y(s)=H\frac{(s+z_1)(s+z_2)}{(s+p_1)}=K_0+\frac{K_1}{s+p_1}+sK_2$$





## 适用边界与失败模式


基于证据边界的分析：




**潜在失效模式**：
- 参数设置不当可能导致仿真不稳定
- 特定工况下可能产生数值误差
- 需要进一步研究确定具体失效边界

## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]] - 电力系统基础
- [[control-system]] - 控制系统基础

## 代表性来源

- [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del]]
- [[influence-of-frequency-characteristics-of-soil-on-lightning-transient-response-o]]
- [[frequency-and-transient-responses-of-a-275-kv-pressure-oil-filled-cable-model-va]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
