---
title: "跟网型变流器 (Grid-Following Inverter, GFL)"
type: model
tags: [grid-following, gfl, current-control, pll, renewable-energy, inverter]
created: "2026-04-30"
---

# 跟网型变流器 (Grid-Following Inverter, GFL)


```mermaid
graph TD
    subgraph Ncmp[跟网型变流器 (Grid-Following Inver…]
        N0[标准GFL: PI电流环+PLL]
        N1[弱电网增强: 改进PLL]
        N2[自适应GFL: 自适应控制]
        N3[虚拟阻抗: 串联虚拟阻抗]
    end
```


## 定义与概述

跟网型变流器（Grid-Following Inverter, GFL）是当前新能源并网的主流技术路线，通过锁相环（PLL）跟踪电网相位，以电流源模式向电网注入有功/无功功率。随着新能源渗透率不断提高，GFL的稳定性问题（如次同步振荡、弱电网不稳定）成为研究热点。本模型涵盖GFL控制结构、电流环设计、弱电网稳定性分析，适用于光伏、风电、储能等新能源并网EMT仿真。

## 1. 物理对象概述

### 1.1 功能与分类

**基本功能**：
- 跟踪电网相位和频率
- 控制注入有功/无功功率
- 实现最大功率点跟踪（新能源）
- 提供低电压穿越能力

**GFL类型**:
| 类型 | 控制策略 | 特点 | 应用 |
|------|----------|------|------|
| 标准GFL | PI电流环+PLL | 成熟稳定 | 光伏/风电 |
| 弱电网增强 | 改进PLL | 提高稳定性 | 弱电网 |
| 自适应GFL | 自适应控制 | 参数自适应 | 宽范围运行 |
| 虚拟阻抗 | 串联虚拟阻抗 | 改善阻尼 | 振荡抑制 |

### 1.2 控制结构

**标准GFL控制框图**:
```
  P_ref, Q_ref
       │
       ▼
  ┌─────────┐
  │ 功率环  │
  │ (外环)  │
  └────┬────┘
       │ i_d*, i_q*
       ▼
  ┌─────────┐     ┌─────────┐
  │ 电流环  │────→│ PWM调制 │──→ 变流器
  │ (内环)  │     │         │
  └────┬────┘     └─────────┘
       │
       ├──→ i_d, i_q (反馈)
```

**关键组件**：
- **PLL**：提取电网相位
- **功率环**：功率PI控制器
- **电流环**：电流PI控制器
- **PWM调制**：SPWM/SVPWM

## 2. 物理模型与数学描述

### 2.1 数学模型

**同步旋转坐标系下的电压方程**：
$$
L\frac{di_d}{dt} = v_d - Ri_d + \omega Li_q - v_{dc}s_d$$
$$
L\frac{di_q}{dt} = v_q - Ri_q - \omega Li_d - v_{dc}s_q$$

其中，$v_d, v_q$为电网电压，$i_d, i_q$为变流器电流，$s_d, s_q$为开关函数。

**锁相环（PLL）模型**：
$$
\frac{d\theta_{pll}}{dt} = \omega_{pll} = \omega_{ff} + K_p v_q + K_i \int v_q dt$$

### 2.2 控制系统

**功率外环**：
```
i_d* = (K_p + K_i/s)(P_ref - P)
i_q* = (K_p + K_i/s)(Q_ref - Q)
```

**电流内环**：
```
v_d* = (K_p + K_i/s)(i_d* - i_d) - ωLi_q + v_d
v_q* = (K_p + K_i/s)(i_q* - i_q) + ωLi_d + v_q
```

## 3. 适用边界

**适用场景**：
- 强电网并网（SCR > 3）
- 功率注入模式运行
- 稳态和暂态稳定性分析
- 电能质量分析（谐波、闪变）

**限制条件**：
- 弱电网下PLL不稳定
- 电压支撑能力有限
- 无黑启动能力
- 需依赖电网同步

## 代表性来源

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| EMT Modeling of Grid-Following Inverters in Weak Grid Conditions | 2021 | 弱电网条件下GFL变流器的EMT建模仿真与稳定性分析 |
| PLL-Based Inverter Control for EMT Simulation of Renewable Integration | 2019 | 基于PLL的变流器控制策略及其在EMT仿真中的实现 |
| Harmonic Analysis of Grid-Following Inverters for EMT Transient Studies | 2022 | GFL变流器谐波特性分析与暂态仿真建模方法 |

## 相关方法
- [[state-space-method|状态空间法]] - GFL状态空间建模
- [[pll-model|锁相环]] - PLL动态建模
- [[pi-controller-model|PI控制器]] - PI控制参数设计
- [[coordinate-transformation-model|坐标变换]] - dq0坐标变换
- [[average-value-model|平均值模型]] - GFL平均值简化

## 相关模型
- [[gfm-inverter-model|构网型变流器]] - GFM与GFL对比
- [[vsc-model|VSC模型]] - 两电平/三电平换流器
- [[mmc-model|MMC模型]] - 模块化多电平换流器
- [[bess-model|电池储能]] - 储能变流器
- [[pv-system-model|光伏系统]] - 光伏并网逆变器

## 相关主题
- [[vsc-hvdc]] - VSC-HVDC输电
- [[real-time-simulation]] - GFL实时仿真
- [[wind-farm-modeling]] - 风电场建模
- [[harmonic-analysis]] - 并网谐波分析
- [[network-equivalent]] - 电网等值接入

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自EMT领域学术文献的深度分析*
