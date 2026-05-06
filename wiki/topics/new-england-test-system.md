---
title: "New England Test System"
type: topic
tags: [new-england-test-system]
created: "2026-05-04"
---

# New England Test System

## 定义与边界

本页面为自动创建的topic类型页面，用于修复断链。内容待补充。

**边界限定**：待完善。

## EMT中的作用

- 详见形式化表达章节


基于相关研究的技术应用：

## 主要分支与机制

- 详见形式化表达章节


## 验证与测试

基于相关研究的验证证据：

- **数值结果**: 24.82%, 4.40%


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

- [[multiphase-power-flow-solutions-using-emtp-and-newtons-method-power-systems-ieee]]
---

*本页面为自动生成的stub，需要进一步补充完善。*

- [[multiphase-power-flow-solutions-using-emtp-and-newtons-method-power-systems-ieee]]
- [[shifted-frequency-analysis-emtp-multirate-simulation-of-power-systems]]
- [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model]]
- [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model-22]]
- [[frequency-adaptive-power-system-modeling-for]]
