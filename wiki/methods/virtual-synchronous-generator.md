---
title: "Virtual Synchronous Generator"
type: method
tags: [virtual-synchronous-generator]
created: "2026-05-04"
---

# Virtual Synchronous Generator

## 定义与边界

本页面为自动创建的method类型页面，用于修复断链。内容待补充。

**边界限定**：待完善。

## EMT中的作用

- 待补充


基于相关研究的技术应用：

## 主要分支与机制

- 待补充

## 形式化表达


### 核心数学表达

从相关研究提取的关键公式：

$$I_i(V_i)=I_g-I_d(V_i)=I_g-I_o\left(e^{\beta V_i/a}-1\right)$$

$$

*理想PV模块的单二极管模型；端电流等于光生电流减去二极管电流，用于说明PV非线性来源。*


**公式2**: $$

$$\beta(T)=\frac{q}{M_s kT}$$

$$I(V)=I_g-I_o\left(e^{\beta(V+R_s I)/a}-1\right)-\frac{V+R_s I}{R_p}$$

$$a_{gen}=a,\quad I_{g,gen}=N_p I_g,\quad I_{o,gen}=N_p I_o,\quad R_{s,gen}=\frac{N_s}{N_p}R_s,\quad R_{p,gen}=\frac{N_s}{N_p}R_p,\quad \beta_{gen}=\frac{\beta}{N_s}$$



## 适用边界与失败模式


基于证据边界的分析：





## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]]
- [[electromagnetic-transient]]
## 代表性来源

- [[grid-forming-converters-sufficient-conditions-for-rms-modeling]]
---

*本页面为自动生成的stub，需要进一步补充完善。*

- [[grid-forming-converters-sufficient-conditions-for-rms-modeling]]
- [[damping-multimodal-subsynchronous-resonance-using-a-generator-terminal-subsynchr]]
- [[an-aggregation-method-of-permanent-magnet-synchronous-wind-farms-for-electromech]]
- [[multiprocessor-based-generator-module-for-a-real-time-power-system-simulator-pow]]
- [[electromagnetic-transient-modeling-of-asynchronous-machine-in-modelica-accuracy-]]
