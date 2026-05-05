---
title: "Lvrt Control"
type: method
tags: [lvrt-control]
created: "2026-05-05"
---

# Lvrt Control

## 定义与边界

本文提出一种基于Modelica方程建模的光伏场站控制交互风险快速评估框架。首先利用MSEMT库构建包含光伏阵列、DC-AC变流器、集电线路、变压器及含故障穿越逻辑控制器的完整EMT详细模型。Modelica编译器自动将分层物理模型展平为微分代数方程组（DAEs），并在任意稳态或准稳态运行点处进行泰勒级数线性化，直接提取显式状态空间矩阵（A, B, C, D）。随后对系统矩阵A进行特征值扫描，通过复特征值的实部正负与频率分布识别潜在的不稳定振荡模态。该方法无需对输入滤波器、非线性环节或保护逻辑进行简化，克服了传统手动推导状态方程的繁琐与精度损失问题，最后通过时域EMT仿真与阻抗扫描进行交叉验证...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，lvrt-control在EMT仿真中用于解决特定问题。

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

- [[fast-investigation-of-control-interaction-risks-in-pv-parks-using-eigenvalue-ana]]
- [[2728multi-rate-real-time-hybrid-simulation-of-controllable-line-commutated-conve]]
- [[active-damping-control-and-parameter-calculation-for-resonance-suppression-in-dc-distribution]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
