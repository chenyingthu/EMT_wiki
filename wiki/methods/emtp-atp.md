---
title: "Emtp Atp"
type: method
tags: [emtp-atp]
created: "2026-05-04"
---

# Emtp Atp

## 定义与边界

本页面为自动创建的method类型页面，用于修复断链。内容待补充。

**边界限定**：待完善。

## EMT中的作用

- 待补充


基于相关研究的技术应用：

2.1. 本文介绍的实现架构以数据流为主线。输入端是用户在EMTPWorks中用图形模块搭建的电力网络和控制/元件模型，接口文件是计算引擎可识别的*....

2.2. NET网络表。核心引擎读取网络表后执行拓扑分析、元器件模型解析、系统计算矩阵构成，并按用户指定条件进行频域、时域、稳态或统计分析；其输出包括二进制*....

## 主要分支与机制

- 待补充


## 验证与测试

基于相关研究的验证证据：


- **数值结果**: 35 kV

## 形式化表达


### 核心数学表达

从相关研究提取的关键公式：

$$-\frac{dV(x,s)}{dx}=Z(s)I(x,s),\qquad -\frac{dI(x,s)}{dx}=Y(s)V(x,s)$$

$$Z(s)=Z_C(s)+Z_E(s)+Z_G(s)$$

$$Z_G(s)=sL_0$$

$$Y(s)=sC_0$$

$$-\frac{dV(x,s)}{dx}=\left(R'(s)+L_0s\right)I(x,s)$$



## 适用边界与失败模式


基于证据边界的分析：




## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]]
- [[electromagnetic-transient]]
## 代表性来源

- [[emtp-modeling-of-electromagnetic-transients-power-delivery-ieee-transactions-on]]
---

*本页面为自动生成的stub，需要进一步补充完善。*

- [[emtp-modeling-of-electromagnetic-transients-power-delivery-ieee-transactions-on]]
- [[application-of-emtp-rv-graphic-software-of-electromagnetic-transient-simulation]]
- [[comparison-of-the-atp-version-of-the-emtp-and-the-netomac-program-for-simulation]]
- [[creating-an-electromagnetic-transients-program-in-matlab-matemtp-power-delivery-]]
- [[accurate-simulation-model-for-a-three-phase-ferroresonant-circuit-in-emtpatp]]
