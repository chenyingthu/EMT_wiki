---
title: "Gruson 2011 Reduced Mmc"
type: model
tags: [gruson-2011-reduced-mmc]
created: "2026-05-04"
---

# Gruson 2011 Reduced Mmc

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

从相关研究提取的关键公式：

$$u_{scp}(t)=\sum_{i=1}^{k}u_{co,i}(t)=\sum_{i=1}^{k}\left(S_i(t)u_{ci}(t)\right)=\sum_{i=1}^{k}S_i(t)\left(\frac{1}{C_i}\int_{t_0}^{t}i_{ci}(t)\mathrm{d}t+u_{ci}(t_0)\right)=\sum_{i=1}^{k}S_i(t)\left(\frac{1}{C_i}\int_{t_0}^{t}S_i(t)i_{sc}(t)\mathrm{d}t+u_{ci}(t_0)\right)$$

$$

*FBSM串联结构在解锁状态下的实际输出电压表达式。它把每个子模块端口电压写成开关函数与电容电压的乘积，并进一步利用电容电流与串联结构电流之间的关系建立动态平均化基础。*


**公式2**: $$

$$S_{run}(t)=\begin{cases}\dfrac{1-e_j}{2}, & \text{上桥臂}\\[4pt]\dfrac{1+e_j}{2}, & \text{下桥臂}\end{cases},\quad j=a,b,c$$

$$u_{sc}(t)=S_{run}(t)\left(\frac{\int_{t_0}^{t}S_{run}(t)i_{sc}(t)\mathrm{d}t}{C_{sc}}+u_{sc}(t_0)\right)=S_{run}(t)\left(\frac{k\int_{t_0}^{t}S_{run}(t)i_{sc}(t)\mathrm{d}t}{C}+ku_c(t_0)\right)$$

$$\begin{cases}u_{scu}(t)=d_{type1}S_{run}(t)\left(\dfrac{k\int_{t_0}^{t}S_{run}(t)i_{sc}(t)\mathrm{d}t}{C}+ku_c(t_0)\right)\\u_{scu1}(t)=d_{type1}\left(\dfrac{k\int_{t_1}^{t}\left(d_{type2}i_{sc1}(t)+d_{type3}i_{sc2}(t)\right)\mathrm{d}t}{C}+ku_c(t_1)\right)\\u_{scu2}(t)=d_{type4}u_{sc1}(t)\\u_{scu3}(t)=d_{type1}\left(\dfrac{k\int_{t_2}^{t}i_{sc3}(t)\mathrm{d}t}{C}+ku_c(t_2)\right)\end{cases}$$



## 适用边界与失败模式


基于证据边界的分析：





## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]]
- [[electromagnetic-transient]]
## 代表性来源

- [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid]]
---

*本页面为自动生成的stub，需要进一步补充完善。*

- [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid]]
- [[modeling-of-a-modular-multilevel-converter-with-embedded-energy-storage-for-elec]]
- [[modeling-of-modular-multilevel-converters-with-different-levels-of-detail-13&14]]
- [[real-time-simulation-of-hybrid-modular-multilevel-converters-using-shifted-phaso]]
- [[a-review-of-efficient-modeling-methods-for-modular-multilevel-converters]]
