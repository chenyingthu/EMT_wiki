---
title: "Energy Storage"
type: method
tags: [energy-storage]
created: "2026-05-04"
---

# Energy Storage

## 定义与边界

本页面为自动创建的method类型页面，用于修复断链。内容待补充。

**边界限定**：待完善。

## EMT中的作用

- 待补充


基于相关研究的技术应用：

## 主要分支与机制

- 待补充


## 验证与测试

基于相关研究的验证证据：



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




## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]]
- [[electromagnetic-transient]]
## 代表性来源

- [[modeling-of-a-modular-multilevel-converter-with-embedded-energy-storage-for-elec]]
---

*本页面为自动生成的stub，需要进一步补充完善。*

- [[modeling-of-a-modular-multilevel-converter-with-embedded-energy-storage-for-elec]]
- [[massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high]]
- [[modeling-of-mmc-based-statcom-with-embedded-energy-storage-for-the-simulation-of]]
- [[average-value-model-for-a-modular-multilevel-converter-with-embedded-storage]]
- [[electrical-power-and-energy-systems-148-2023-108967]]
