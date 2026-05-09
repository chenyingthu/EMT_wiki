---
title: "电晕效应建模 (Corona Effect Modeling)"
type: method
tags: [corona, transmission-line, emt, bergeron-model, nonlinear-modeling, overvoltage]
created: "2026-05-10"
---

# 电晕效应建模 (Corona Effect Modeling)


```mermaid
graph TD
    subgraph Ncmp[电晕效应建模 (Corona Effect Modeli…]
        N0[集中电晕支路: 节点处外接 RC 支路]
        N1[VDLM 分布模型: 电容和电导为电压相关]
        N2[频变-电晕耦合: 同时考虑频变参数与电晕]
    end
```


## 定义与边界

电晕效应是指架空线路表面电场强度超过空气击穿阈值时，导体周围空气电离引起的放电现象，在 EMT 仿真中表现为线路参数的电压相关变化。电晕使线路单位长度电容增大、引入并联电晕损耗电导，并改变行波传播速度，导致过电压波形的幅值衰减和波形畸变。

本页关注将电晕效应纳入 EMT 仿真的建模方法：从集中电晕支路到电压相关线路参数模型。经典的传输线建模基础见 [[transmission-line-theory]] 和 [[bergeron-line-model]]；频率相关线路模型见 [[universal-line-model]]；雷击过电压应用见 [[lightning-transient-analysis]]。

## EMT 中的作用

电晕效应在 EMT 仿真中直接影响过电压评估的准确性：

- **幅值衰减**：电晕增大线路对地电导，使传播中的过电压幅值低于忽略电晕时的结果。
- **波形畸变**：电压相关电容改变波前陡度和上升时间，影响被保护设备的绝缘配合设计。
- **波速变化**：电容增大使传播速度降低，改变行波到达时刻。
- 忽略电晕的线路模型在雷击过电压和操作过电压分析中给出偏保守（偏高）结果。

## 核心机制

### 电晕的物理描述

当线路电压 $v$ 低于起晕阈值 $v_0$ 时，线路为正常电容 $C_0$；超过阈值后，电容增大为电压相关函数 $C(v)$，并并联电晕损耗电导 $G(v)$：

$$
C(v) = \begin{cases} C_0, & |v| \leq v_0 \\ C_0 + f_c(|v| - v_0), & |v| > v_0 \end{cases}
$$

$$
G(v) = \begin{cases} 0, & |v| \leq v_0 \\ g_c(|v| - v_0)^\alpha, & |v| > v_0 \end{cases}
$$

经验参数 $f_c$、$g_c$、$\alpha$ 通过实测或实验确定，随线路结构和天气条件变化。

### 电压相关线路模型（VDLM）

VDLM 将电晕效应内嵌到 Bergeron/Dommel 线路模型中，替代传统的外接集中电晕支路做法。核心思路是把单位长度电容处理为电压相关量，从线路参数层面表达分布电晕：

- 特征阻抗 $Z_c(v) = \sqrt{L/C(v)}$，随电压升高而降低
- 传播时间 $\tau(v) = l \cdot \sqrt{L C(v)}$，随电压升高而增加
- 线路仍可表示为 Norton 等效形式，端口导纳和历史源随电压更新

避免迭代的求解策略：用前一时间步的电压更新当前步线路参数和历史量，再直接求解节点电压，避免同一时间步内反复迭代非线性方程。

### 集中电晕支路

传统做法将线路分段，在分段节点外接非线性 RC 支路表示电晕效应，线路参数本身保持不变。该方法实现简单，但集中而非分布的特性在长线路波过程模拟中存在精度损失。

## 分类与变体

| 模型类型 | 电晕表示 | 精度 | 计算复杂度 | 适用场景 |
|---------|---------|------|-----------|---------|
| 集中电晕支路 | 节点处外接 RC 支路 | 中等 | 低 | 工程快速评估 |
| VDLM 分布模型 | 电容和电导为电压相关 | 较高 | 中等 | 雷击过电压精确分析 |
| 频变-电晕耦合 | 同时考虑频变参数与电晕 | 高 | 较高 | 长线路精确波过程 |

## 相关方法

- [[transmission-line-theory]] — 传输线建模基础
- [[bergeron-line-model]] — Bergeron 行波模型
- [[universal-line-model]] — 通用线路模型
- [[lightning-transient-analysis]] — 雷击暂态分析
- [[frequency-dependent-network-equivalent]] — 频变参数建模

## 相关模型

- [[transmission-line-model]] — 输电线路模型
- [[cable-model]] — 电缆模型

## 相关主题

- [[grounding-lightning-overvoltage]]
- [[switching-transient]]
- [[transmission-line-modeling]]

## 代表性来源

- Pereira, Tavares — Development of a Voltage-Dependent Line Model to Represent the Corona Effect in EMT Program (2020)
- Pereira, Tavares — A New Approach to Represent the Corona Effect and Frequency-Dependent Transmission Line Models (2022)
- 其他 8 篇相关论文覆盖电晕损耗、频变特性和过电压应用
