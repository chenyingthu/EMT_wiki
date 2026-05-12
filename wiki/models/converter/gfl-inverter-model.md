---
title: "跟网型变流器 (Grid-Following Inverter, GFL)"
type: model
tags: [grid-following, gfl, current-control, pll, renewable-energy, inverter]
created: "2026-04-30"
updated: "2026-05-12"
---

# 跟网型变流器 (Grid-Following Inverter, GFL)

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

### 量化性能边界

GFL 变流器的 EMT 仿真精度取决于电流环离散化方法、PLL 参数整定和电网强度，而非 GFL 控制算法框架本身的近似。以下汇总可引用的量化数据：

**等效模型精度**：Luchini (2023) 在 ATP/ATPDraw 中实现了跟网型逆变器等效时域模型（含 DSOGI-PLL 和电流环），与全开关基准模型相比，故障电流平均误差约 2.33%，仿真时间减少约 70%。

**弱网稳定性边界**：Carreño (2026) 提出 RMS+ 模型用于捕捉 GFL 中 PLL 与网络交互失稳，单换流器场景下 RMS+ 与 EMT 偏差小于 0.5%，而传统 RMS 模型在跨临界分岔边界完全失效。SCR < 2 时 Hopf 分岔临界功率下降约 40%（0.9 → 0.55 pu），时间尺度比 $\tau_L/\tau_{PLL} < 0.1$ 时 RMS+ 误差小于 2%。Ranasinghe (2024) 的改进型 DSOGI-PLL 将 SCR 稳定下限从 2.3 扩展至 1.0。

**平均值模型性能**：DAVM (2012) 验证了基于矢量控制的 VSC-HVDC 动态平均值模型，5 μs 步长下 CPU 减少 50-54%，≥40 μs 步长下减少 60-70%。

**数据缺口声明**：GFL 变流器在不同电网强度（SCR 1-10）、不同 PLL 拓扑（SRF、DSOGI、DDSRF）和不同电流环带宽下的系统对比数据在公开文献中分散且缺乏统一基准。GFL 的详细开关模型与平均值模型在谐波精度、故障暂态方面的量化对比有待补充。

## 相关方法
- [[state-space-method|状态空间法]] - GFL状态空间建模
- [[pll-model|锁相环]] - PLL动态建模
- [[pi-controller-model|PI控制器]] - PI控制参数设计
- [[coordinate-transformation-model|坐标变换]] - dq0坐标变换
- [[average-value-model|平均值模型]] - GFL平均值简化

## 相关模型
- [[gfm-inverter-model|构网型变流器]] - GFM与GFL对比
- [[vsc-model|VSC模型]] - 两电平/三电平换流器
- [[pv-system-model|光伏系统]] - 光伏并网逆变器

## 相关主题
- [[real-time-simulation]] - GFL实时仿真
- [[harmonic-analysis]] - 并网谐波分析

---
## EMT中的作用

跟网型变流器 (Grid-Following Inverter, GFL) 在EMT仿真中主要用于：

- **建模对象**：描述跟网型变流器 (Grid-Following Inverter, GFL)在电力系统中的物理角色和电气特性
- **仿真场景**：适用于跟网型变流器 (Grid-Following Inverter, GFL)相关的电磁暂态分析、故障响应、控制交互等场景
- **模型接口**：提供跟网型变流器 (Grid-Following Inverter, GFL)的端口变量、状态方程和边界条件
- **验证基准**：可作为跟网型变流器 (Grid-Following Inverter, GFL)仿真模型正确性的验证基准

## 数学模型

### 基本方程

跟网型变流器 (Grid-Following Inverter, GFL)的数学模型基于以下基本物理定律：

$$
\text{待补充：基于跟网型变流器 (Grid-Following Inverter, GFL)的物理特性建立数学描述}
$$

### 状态空间表示

$$
\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \mathbf{u})
$$

$$
\mathbf{y} = \mathbf{g}(\mathbf{x}, \mathbf{u})
$$

其中 $\mathbf{x}$ 为状态向量，$\mathbf{u}$ 为输入向量，$\mathbf{y}$ 为输出向量。


*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*