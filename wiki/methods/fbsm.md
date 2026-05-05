---
title: "Fbsm"
type: method
tags: [fbsm]
created: "2026-05-05"
---

# Fbsm

## 定义与边界

摘要：为避免同侧互补导通的功率管发生直通短路故障，模块化多电平换流器(MMC)中开关器件 需要设置死区时间，死区的存在会产生死区效应且死区难以被彻底消除。随着电力电子器件开关 频率的不断提高，死区占比增加，死区影响已不容忽视。针对死区效应越来越显著和 MMC 仿真耗 时过长的问题，提出一种考虑死区特性的提速模型。首先，对级联子模块含死区时间的实际开关状 态进行端口工况特征扫描，通过含死区的端口特性识别出各子模块实际工作模态，建立状态空间方 程。其次，基于状态空间平均法，以占空比为纽带统一子模块不同的模态性质，建立子模块分立元 件 模 型 。 进 一 步 ，根 据 平 均 值 模 型 的 解 耦...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，fbsm在EMT仿真中用于解决特定问题。

基于相关研究，该方法在EMT仿真中的主要应用包括：
- 特定场景的电磁暂态分析
- 控制系统设计与验证
- 故障分析与保护协调

## 主要分支与机制

- 待补充（需要进一步研究确定具体分支）

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





**潜在失效模式**：
- 参数设置不当可能导致仿真不稳定
- 特定工况下可能产生数值误差
- 需要进一步研究确定具体失效边界

## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]] - 电力系统基础
- [[control-system]] - 控制系统基础

## 代表性来源

- [[考虑死区特性的全桥型mmc状态空间平均化建模方法]]
- [[an-accelerated-detailed-equivalent-model-for-modular-multilevel-converters]]
- [[非隔离型直流变压器的快速电磁暂态等效建模方法]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
