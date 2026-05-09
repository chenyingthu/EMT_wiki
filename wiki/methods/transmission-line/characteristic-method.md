---
title: "特征线法 (Characteristic Method)"
type: method
tags: [characteristic, method, bergeron, transmission-line, wave, distributed-parameter]
created: "2026-05-02"
---

# 特征线法 (Characteristic Method)


```mermaid
graph TD
    N0[特征线法 (Characteri…]
    N1[定义与边界]
    N0 --> N1
    N2[EMT 中的作用]
    N0 --> N2
    N3[核心机制]
    N0 --> N3
    N4[多导体扩展]
    N0 --> N4
    N5[算法步骤]
    N0 --> N5
    N6[适用边界与失败模式]
    N0 --> N6
    N7[代表性证据]
    N0 --> N7
    N8[与相关页面的关系]
    N0 --> N8
```


## 定义与边界

特征线法（Method of Characteristics）是把双曲型偏微分方程沿特征方向转化为传播关系的求解思想。在 EMT 线路建模中，它主要用于从电报方程得到行波变量、传播延时和端口历史项。

本页讨论的是方法本身：如何从相域或模域线路方程得到沿线传播关系。它不同于具体元件页 [[bergeron-line-model]] 和 [[bergeron-model]]；后两者关注 EMT 端口等效电路。本页也不替代 [[universal-line-model]]，后者处理相域频变矩阵拟合与时域实现。

## EMT 中的作用

特征线法在 EMT 中连接三类对象：

- 分布参数线路的电压、电流偏微分方程。
- 行波变量和传播时延。
- 节点导纳方程中的历史源、延时队列或递归卷积项。

它的输出不是单一软件模块，而是一组可离散化的端口关系。常参数模型可得到简单延时历史源；频变模型通常需要将特征导纳、传播函数或损耗项进一步拟合成时域可递推形式。

## 核心机制

无损单相线路的电报方程为：

$$-\frac{\partial v}{\partial x}=L\frac{\partial i}{\partial t},\quad
-\frac{\partial i}{\partial x}=C\frac{\partial v}{\partial t}$$

定义 $Z_c=\sqrt{L/C}$ 和 $u=1/\sqrt{LC}$，可构造特征变量：

$$w^+(x,t)=v(x,t)+Z_ci(x,t),\quad
w^-(x,t)=v(x,t)-Z_ci(x,t)$$

它们沿两组特征线传播：

$$\frac{\partial w^+}{\partial t}+u\frac{\partial w^+}{\partial x}=0,\quad
\frac{\partial w^-}{\partial t}-u\frac{\partial w^-}{\partial x}=0$$

因此 $w^+$ 与 $w^-$ 分别表示向相反方向传播的波变量。将这组关系在长度 $\ell$ 的线路两端评价，就得到 Bergeron 类端口历史源。

有损或频变线路可形式化写为：

$$-\frac{\partial v}{\partial x}=R(\omega)i+j\omega L(\omega)i,\quad
-\frac{\partial i}{\partial x}=G(\omega)v+j\omega C(\omega)v$$

此时“沿特征线保持常数”的简单结论不再严格成立，通常需要有理函数、状态空间或卷积项描述衰减与色散。

## 多导体扩展

多导体线路的频域方程可写为：

$$-\frac{d\mathbf{V}}{dx}=\mathbf{Z}(\omega)\mathbf{I},\quad
-\frac{d\mathbf{I}}{dx}=\mathbf{Y}(\omega)\mathbf{V}$$

若存在变换矩阵 $\mathbf{T}$ 使 $\mathbf{Z}\mathbf{Y}$ 近似对角化，则每个模态可单独应用特征线关系。对平衡或完全换位三相线路，固定序分量或 Clarke/Karrenbauer 类变换可能足够；对非换位、平行线路和电缆，变换矩阵可能随频率变化，需参考 [[modal-domain-decoupling]] 与 [[universal-line-model]] 的边界。

## 算法步骤

1. 建立线路几何、导体、介质和土壤参数，得到 $L,C,R,G$ 或 $\mathbf{Z}(\omega),\mathbf{Y}(\omega)$。
2. 判断是否可用常参数近似；若可以，计算 $Z_c$、$u$ 和 $\tau$。
3. 若为多导体线路，选择相域直接处理、固定模态解耦或频率相关模态处理。
4. 将传播关系写成端口导纳和历史项，或将频变函数拟合为状态空间/递归卷积。
5. 处理非整数延时、插值、可变步长和历史队列更新。
6. 用频域拟合误差、时域波形和关键工况检查模型是否在目标频带内可信。

## 适用边界与失败模式

- 特征线法本身不自动保证宽频精度；频变损耗和大地返回路径需要独立建模。
- 将常数模态变换用于非换位或平行线路时，应检查互耦误差。
- 非整数延时插值会改变高频相位，不能省略步长和插值策略。
- 若频变函数用 [[vector-fitting]] 或状态空间实现，应检查极点稳定性、因果性和 [[passivity-enforcement]]。
- 行波测距、保护判据或过电压结论不能只由方法公式推出，必须绑定测量带宽、阈值和工况。

## 代表性证据

- [[accelerated-frequency-dependent-method-of-characteristics-for-the-simulation-of-]]：支撑频变多导体特征线法的加速实现，包括固定频率实模态变换、稀疏状态空间和传播时间离散误差修正；结论主要限于作者架空线算例。
- [[frequency-dependent-line-model-in-the-time-domain-for-simulation-of-fast-and-imp]]：支撑在 Bergeron/特征线框架中嵌入频变纵向参数的建模思路；量化结果需回到原文。
- [[new-investigations-on-the-method-of-characteristics-for-the-evaluation-of-line-t]] 可作为特征线法评价线路暂态的新近入口。
- [[transmission-line-model-for-variable-step-size-simulation-algorithms]] 支撑可变步长会改变延时历史量处理的数值边界。

## 与相关页面的关系

- [[bergeron-model]]：从特征线关系落到端口 Norton 等效。
- [[bergeron-line-model]]：常参数线路模型主页面。
- [[distributed-parameter-line]]：给出线路偏微分方程背景。
- [[modal-transformation]] 和 [[modal-domain-decoupling]]：说明多相线路解耦的坐标变换条件。
- [[frequency-dependent-line-model]] 和 [[universal-line-model]]：处理频率相关传播和相域实现。

## 修订与证据使用注意事项

本页应保持方法页边界，不加入未核验的软件功能表、典型速度、典型步长、保护动作时间或误差百分比。若引用论文算例，应同时给出线路类型、频带、拟合设置、时间步长和对比基线。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[modeling-nonuniform-transmission-lines-for-time-domain-simulation-of-electromagn|Modeling nonuniform transmission lines for time domain simul]] | 2001 |
| [[passivity-enforcement-for-transmission-line-models|Passivity Enforcement for Transmission Line Models]] | 2008 |
| [[improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an-fix|Improvement of Numerical Stability for the Computation of Tr]] | 2010 |
| [[improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an|Improvement of Numerical Stability for the Computation of Tr]] | 2010 |
| [[analyses-of-the-modifications-in-the-pi-circuits-for-inclusion-of-frequency-infl|Analyses of the modifications in the pi circuits for inclusi]] | 2011 |
| [[published-in-iet-generation-transmission-distribution-27&28|Numerical Integration by the 2-Stage Diagonally Implicit Run]] | 2013 |
| [[accelerated-frequency-dependent-method-of-characteristics-for-the-simulation-of-|Accelerated frequency-dependent method of characteristics fo]] | 2018 |
