---
title: "Grid Forming Inverter"
type: model
tags: [grid-forming-inverter]
created: "2026-05-04"
---

# Grid Forming Inverter

## 定义与边界

本页面为自动创建的model类型页面，用于修复断链。内容待补充。

**边界限定**：待完善。

## EMT中的作用

- 待补充


基于相关研究的技术应用：

## 主要分支与机制

- 待补充

## 形式化表达

### 核心数学表达

虚拟同步机(VSM)转子方程：
$$J rac{d\omega}{dt} = T_m - T_e - D(\omega - \omega_0)$$

内电势控制：
$$E = E_0 + k_q (Q_{ref} - Q)$$

功角特性：
$$P = rac{EV}{X} \sin\delta$$

$\delta$为功角，$X$为等效电抗。


## 适用边界与失败模式

**适用条件**：
- 构网型储能/光伏/风电应用
- 孤岛或弱电网运行
- 高比例新能源电力系统

**失效边界**：
- 过载导致电流限幅
- 功角失稳
- 惯量支撑能力不足


## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]]
- [[electromagnetic-transient]]
## 代表性来源

- [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i]]
---

*本页面为自动生成的stub，需要进一步补充完善。*

- [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i]]
- [[advancing-grid-forming-inverter-technology-comprehensive-pq-capability-and-perfo]]
- [[grid-forming-converters-sufficient-conditions-for-rms-modeling]]
- [[comparison-and-selection-of-grid-tied-inverter-models-for-accurate-and-efficient]]
- [[equivalent-grid-following-inverter-based-generator-model-for-atpatpdraw-simulati]]
