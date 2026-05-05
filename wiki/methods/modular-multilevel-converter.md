---
title: "Modular Multilevel Converter"
type: method
tags: [modular-multilevel-converter]
created: "2026-05-04"
---

# Modular Multilevel Converter

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

MMC桥臂电压：
$$v_{arm} = \sum_{i=1}^{N} s_i \cdot v_{c,i}$$

环流抑制控制目标：
$$i_{circ} = rac{i_p + i_n}{2} - rac{I_{dc}}{3} = 0$$

子模块电容能量平衡：
$$W_{SM} = rac{1}{2} C_{SM} v_c^2$$


## 适用边界与失败模式

**适用条件**：
- 高压大功率直流输电应用
- 需要模块化扩展的场合
- 对谐波性能要求较高的场景

**失效边界**：
- 子模块故障率超过冗余设计
- 电容老化导致参数漂移
- 控制系统通信延迟过大


## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]]
- [[electromagnetic-transient]]
## 代表性来源

- [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid]]
---

*本页面为自动生成的stub，需要进一步补充完善。*

- [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid]]
- [[modeling-of-modular-multilevel-converters-with-different-levels-of-detail-13&14]]
- [[real-time-simulation-of-hybrid-modular-multilevel-converters-using-shifted-phaso]]
- [[a-review-of-efficient-modeling-methods-for-modular-multilevel-converters]]
- [[an-enhanced-average-value-model-of-modular-multilevel-converter-for-accurate-rep]]
