---
title: "Wind Farm Hvdc"
type: method
tags: [wind-farm-hvdc]
created: "2026-05-04"
---

# Wind Farm Hvdc

## 定义与边界

本页面为自动创建的method类型页面，用于修复断链。内容待补充。

**边界限定**：待完善。

## EMT中的作用

- 待补充


基于相关研究的技术应用：

2.1. 论文的核心实现是先在频域获得风电场接地系统的宽带多端口模型，再把该模型嵌入时域电磁暂态仿真工具。多端口模型的端口对应各风机接地系统或与外部元件相连的电气节点，接口量是端口电压和注入电流；输入包括接地网络几何、互联埋地裸导体、土壤电阻率及其频变参数，输出是可在EMT中调用的宽频阻抗/导纳关系。这样，埋...

## 主要分支与机制

- 待补充

## 形式化表达


### 核心数学表达

从相关研究提取的关键公式：

$$V_{a,n+1/2}=\frac{1}{hG_a+C_a}\left[C_aV_{a,n-1/2}-h\left(\sum_{o=1}^{M_a}I_{ao,n}-I_{a,n}\right)\right]$$

$$I_{ab,n+1}=\left(1-\frac{h}{L_{ab}}R_{ab}\right)I_{ab,n}+\frac{h}{L_{ab}}\left(V_{a,n+1/2}-V_{b,n+1/2}+V_{ab,n+1/2}\right)$$

$$V_{Cf,n+1/2}=V_{Cf,n-1/2}+hC_{if}^{-1}\left(I_{gsc,n}+I_{b,n}\right)$$

$$

*新能源出口滤波电容接口电压更新公式。该接口电容吸收网侧变换器交流侧支路电流和与变换器相连的网侧支路电流，用于解耦快速动态系统与常规动态系统。*


**公式4**: $$

$$I_{GT,n+1}=A_1I_{GT,n}+A_2V_{GT,n+1/2}$$



## 适用边界与失败模式


基于证据边界的分析：




## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]]
- [[electromagnetic-transient]]
## 代表性来源

- [[modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag]]
---

*本页面为自动生成的stub，需要进一步补充完善。*

- [[modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag]]
- [[ground-potential-rise-in-wind-farms-due-to-direct-lightning]]
- [[experimental-research-on-high-voltage-transformer-transient-characteristics]]
- [[efficient-electromagnetic-transient-simulation-for-dfig-based-wind-farms-using-f]]
- [[a-method-to-calculate-short-circuit-faults-in-high-voltage-dc-grids]]
