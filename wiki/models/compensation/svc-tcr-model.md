---
title: "SVC/TCR (静止无功补偿器)"
type: model
tags: [svc, tcr, tsc, facts, reactive-power, thyristor]
created: "2026-04-29"
---

# SVC/TCR (静止无功补偿器)


```mermaid
graph TD
    subgraph Ncmp[SVC/TCR (静止无功补偿器)]
        N0[**TCR**: 晶闸管+电抗器]
        N1[**TSC**: 晶闸管+电容器]
        N2[**TCR+TSC**: 组合]
        N3[**TCR+FC**: TCR+固定电容]
    end
```


## 定义与概述

静止无功补偿器（SVC）是基于晶闸管控制的FACTS设备，通过调节晶闸管触发角实现无功功率的连续调节，用于电压控制、无功补偿和提高输电能力。TCR（晶闸管控制电抗器）是SVC的核心部件，与固定电容器或晶闸管投切电容器配合实现双向无功调节。本模型涵盖TCR电压-电流特性、控制系统、谐波分析，适用于高压输电系统电压稳定和无功优化研究。

## 1. 物理对象概述

### 1.1 功能与原理

静止无功补偿器(SVC)是传统的FACTS设备，用于快速无功功率调节：

**核心功能**：
- **电压调节**：维持母线电压稳定
- **无功补偿**：连续调节无功输出
- **提高稳定性**：增加输电能力，抑制振荡
- **负荷补偿**：抑制电压闪变（如电弧炉）
- **滤波**：兼作谐波滤波器

**响应速度**：
- 响应时间：1-2周波（20-40ms）
- 比机械投切电容器快10-100倍

### 1.2 SVC类型

| 类型 | 结构 | 无功特性 | 应用 |
|------|------|---------|------|
| **TCR** | 晶闸管+电抗器 | 连续感性 | 大容量补偿 |
| **TSC** | 晶闸管+电容器 | 分级容性 | 阶梯补偿 |
| **TCR+TSC** | 组合 | 双向连续 | 通用型 |
| **TCR+FC** | TCR+固定电容 | 连续调节 | 最常用 |

### 1.3 TCR基本原理

**晶闸管控制电抗器(TCR)**：
- 两个反并联晶闸管与电抗器串联
- 通过控制触发角$\alpha$调节等效电感
- $\alpha$范围：90°-180°

**等效电纳**：
$$B_{TCR}(\alpha) = \frac{2\pi - 2\alpha + \sin 2\alpha}{\pi X_L}$$

其中：
- $\alpha = 90°$：完全导通，最大感性无功
- $\alpha = 180°$：完全关断，无功为零

**基波电流**：
$$I_1(\alpha) = \frac{V}{X_L}\left(1 - \frac{2\alpha}{\pi} + \frac{\sin 2\alpha}{\pi}\right)$$

## 2. 物理模型与数学描述

### 2.1 电压-电流特性

**稳态特性**：
- 线性区：电压调节范围
- 饱和区：最大感性/容性输出
- 斜率特性：电压-无功灵敏度

**斜率电抗**：
$$X_{SL} = \frac{\Delta V}{\Delta Q}$$

典型值：$X_{SL} = 3\% \sim 5\%$（基于系统短路容量）

### 2.2 控制系统

**电压调节器**：
$$
B_{ref} = K_p(V_{ref} - V) + K_i\int(V_{ref} - V)dt$$

**触发角计算**：
- 根据所需电纳$B_{ref}$反算触发角$\alpha$
- 线性化：$\Delta\alpha = K_B \Delta B$

### 2.3 谐波特性

**特征谐波**：
- 6脉动TCR：5, 7, 11, 13, ... 次
- 12脉动TCR：11, 13, 23, 25, ... 次

**谐波电流**：
$$I_h(\alpha) = \frac{V}{hX_L}\frac{4}{\pi}\left[\frac{\sin(h+1)\alpha}{2(h+1)} - \frac{\sin(h-1)\alpha}{2(h-1)} + \frac{\cos\alpha\sin h\alpha}{h}\right]$$

## 3. EMT仿真建模

### 3.1 详细模型

**晶闸管模型**：
- 理想开关模型
- 固定导纳模型
- 详细晶闸管模型（考虑恢复特性）

**电抗器模型**：
- 线性电感
- 饱和电感（考虑铁芯饱和）

### 3.2 平均值模型

**等效电纳**：
$$B_{TCR}^{eq}(\alpha) = \frac{2(\pi - \alpha) + \sin 2\alpha}{\pi X_L}$$

**适用条件**：
- 系统级仿真
- 忽略开关细节
- 工频动态分析

## 4. 适用边界

**适用场景**：
- 高压输电系统电压控制
- 电弧炉负荷补偿
- 风电/光伏并网无功支撑
- 提高输电能力
- 抑制次同步振荡

**限制条件**：
- 谐波产生
- 无功调节范围有限
- 依赖系统短路容量
- 不能独立提供短路容量

## 代表性来源

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model|Hybrid simulation of power systems with SVC dynamic phasor model]] | 2009 | 提出基于动态相量理论的SVC混合仿真方法，建立TCR单相动态相量模型，实现积分步长200~400倍提升的同时保持波形精度 |
| [[interpolation-for-power-electronic-circuit-simulation-revisited-with-matrix-expo|Interpolation for power electronic circuit simulation revisited with matrix exponential and dense outputs]] | 2020 | 提出矩阵指数积分与密集输出公式新框架，针对TCR等电力电子电路实现开关时刻高精度捕捉与数值振荡抑制 |
| [[hybrid-svc-vsc-modeling-approaches-for-hardware-in-the-loop-simulation|Hybrid SVC-VSC modeling approaches for hardware-in-the-loop simulation]] | 2023 | 对比小步长与常规大步长EMT两种HIL建模方法，为SVC-VSC混合拓扑的实时仿真提供工程实证 |

## 相关方法
- [[average-value-model|平均值模型]] - SVC平均值建模
- [[switching-function-method|开关函数法]] - 晶闸管开关建模
- [[numerical-integration|数值积分]] - 触发角控制仿真
- [[harmonic-analysis-methods|谐波分析]] - TCR谐波分析
- [[state-space-method|状态空间法]] - 控制系统状态空间

## 相关模型
- [[svc-tcr-model|TCR模型]] - 晶闸管控制电抗器
- [[svc-tcr-model|TSC模型]] - 晶闸管投切电容器（SVC类型）
- [[vsc-model|VSC模型]] - 对比STATCOM
- [[transformer-model|变压器模型]] - 连接变压器
- [[load-model|负荷模型]] - 电弧炉负荷

## 相关主题
- [[co-simulation|混合仿真]] - FACTS装置混合仿真
- [[harmonic-analysis-methods|谐波分析]] - 谐波分析
- [[vsc-hvdc]] - 柔性直流输电对比
- [[real-time-simulation]] - 实时仿真
- [[wind-farm-modeling|风电场建模]] - 新能源并网应用

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自EMT领域学术文献的深度分析*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[application-of-emtp-rv-graphic-software-of-electromagnetic-transient-simulation|Application of EMTP-RV graphic software of electromagnetic t]] | 2007 |
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model-22|Hybrid simulation of power systems with SVC dynamic phasor m]] | 2009 |
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model|Hybrid simulation of power systems with SVC dynamic phasor m]] | 2009 |
| [[interpolation-for-power-electronic-circuit-simulation-revisited-with-matrix-expo|Interpolation for power electronic circuit simulation revisi]] | 2020 |
