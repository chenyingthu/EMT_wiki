---
title: "Hierarchical Control"
type: method
tags: [hierarchical-control]
created: "2026-05-05"
---

# Hierarchical Control

## 定义与边界

本文提出一种面向可控线路换相换流器高压直流（CLCC-HVDC）系统的CPU-FPGA协同多速率实时仿真框架。针对系统多时间尺度动态与复杂开关暂态耦合导致的计算瓶颈，采用异构任务分配策略：CPU子系统以20 μs步长处理低频动态（交直流电网、传统LCC及控制保护逻辑），FPGA子系统以2 μs步长高精度捕捉CLCC高频开关与换相暂态。为实现拓扑分割与数据交互，提出离散电感解耦法，利用梯形积分将电感等效为含历史电流源与受控电压源的对称子电路，作为CPU/FPGA天然解耦边界。针对FPGA端开关器件建模，构建关联离散电路（ADC）模型，通过分解CLCC运行区间求解各阀组电压/电流应力，基于最小虚拟...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，hierarchical-control在EMT仿真中用于解决特定问题。

基于相关研究，该方法在EMT仿真中的主要应用包括：
- 特定场景的电磁暂态分析
- 控制系统设计与验证
- 故障分析与保护协调

## 主要分支与机制

- 待补充（需要进一步研究确定具体分支）

## 形式化表达


### 核心数学表达

从相关研究提取的关键公式：

$$J_i\frac{d\Delta\omega_i}{dt}=\frac{P_{mi}}{\omega_0}-\frac{P_{0i}}{\omega_0}-D_i(\omega_i-\omega_0),\qquad P_{mi}=P_{refi}+k_{\omega i}(\omega_0-\omega)$$

$$E_i=\frac{1}{K_{qi}s}\left[Q_{refi}-Q_{0i}+D_{qi}(U_{cni}-U_c)\right]$$

$$P_{0i}=\frac{3U_{ci}U_g\sin\delta_i}{2\omega_0L_i}\approx\frac{3U_{ci}U_g}{2X_i}\delta_i\approx K_i\delta_i,\qquad \delta_i=\int(\omega_i-\omega_{bus})dt$$

$$\frac{\Delta\omega_i(s)}{\Delta\omega_{bus}(s)}=\frac{K_i}{J_i\omega_0s^2+(D_i\omega_0+k_{\omega i})s+K_i}$$

$$

*单台VSC-ESS相对于公共母线频率扰动的二阶频率响应传递函数。分母中二阶项由虚拟惯量决定，一阶项由虚拟阻尼和频率调制系数决定，常数项由同步功率系数决定。*


**公式5**: $$





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

- [[2728multi-rate-real-time-hybrid-simulation-of-controllable-line-commutated-conve]]
- [[active-damping-control-and-parameter-calculation-for-resonance-suppression-in-dc-distribution]]
- [[real-time-simulation-with-an-industrial-dccb-controller-in-a-hvdc-grid]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
