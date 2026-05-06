---
title: "Adaptive Droop"
type: method
tags: [adaptive-droop]
created: "2026-05-05"
---

# 自适应下垂控制方法 (Adaptive Droop Control)

## 定义与边界

提出一种适用于电磁暂态(EMT)仿真的自适应MMC模型架构，支持半桥(HB)与全桥(FB)子模块的任意混合配置。该架构集成平均值模型(AVM)、桥臂等效模型(AEM)和详细等效模型(DEM)，通过统一的二端口诺顿等效电路实现电气接口标准化，彻底消除模型切换时的拓扑结构突变。所有模型在拓扑上并联，非激活模型在求解器中提供零导纳与零电流源，确保节点电压连续性。模型以动态链接库(DLL)封装，支持仿真运行时动态激活/去激活。控制系统采用标准级联架构，外环(PLL与功率/电压控制)始终运行，内环根据激活模型切换：AVM输出交流电势参考，AEM/DEM输出桥臂开关函数参考并配合环流抑制(CCSC)与最近...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

adaptive-droop在EMT仿真中用于电磁暂态仿真分析。

该方法在EMT仿真中的主要应用包括：
- 特定场景的电磁暂态分析
- 控制系统设计与验证
- 故障分析与保护协调

## 主要分支与机制

- 详见形式化表达章节（需要进一步研究确定具体分支）

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

- [[adaptive-modular-multilevel-converter-model-for-electromagnetic-transient-simula]]
- [[advanced-dsogi-pll-with-adaptive-bandwidth-for-improved-transient-performance-of]]
- [[adaptive-heterogeneous-transient-analysis-of-wind-farm-integrated-comprehensive-]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
