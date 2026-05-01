---
title: "构网型变流器 (Grid-Forming Inverter, GFM)"
type: model
tags: [grid-forming, gfm, droop, vsm, virtual-synchronous-machine, weak-grid, inertia]
created: "2026-04-30"
---

# 构网型变流器 (Grid-Forming Inverter, GFM)

## 定义与概述

构网型变流器（Grid-Forming Inverter, GFM）是新型电力系统的关键技术，通过模拟同步发电机的惯性响应和下垂特性，能够独立建立并维持电网电压和频率，为弱电网和孤岛系统提供惯量支撑和阻尼。随着新能源渗透率提高和同步发电机退役，GFM技术对电网稳定性至关重要。本模型涵盖下垂控制GFM、虚拟同步机（VSM）、匹配控制等策略，适用于100%电力电子化电网的EMT仿真。

## 1. 物理对象概述

### 1.1 功能与分类

**基本功能**：
- 独立建立电压幅值和频率
- 提供虚拟惯量支撑
- 实现多机并联功率均分
- 故障期间维持电网稳定
- 黑启动能力

**GFM类型**:
| 类型 | 控制策略 | 特点 | 应用场景 |
|------|----------|------|----------|
| 下垂控制 | P-f/Q-V下垂 | 经典方法 | 微电网 |
| VSM | 虚拟同步机 | 二阶转子方程 | 高渗透率系统 |
| 匹配控制 | 非线性匹配 | 理论严谨 | 实验验证 |
| 虚拟振荡器 | VOC | 非线性振荡 | 孤岛微电网 |
| 自同步 | 无PLL | 自适应同步 | 快速响应 |

### 1.2 控制结构

**GFM通用控制框图**:
```
  P_ref, Q_ref
       │
       ▼
  ┌─────────────┐
  │   功率计算   │
  │ P = vi, Q = │
  └──────┬──────┘
         │
         ▼
  ┌─────────────┐
  │  GFM核心控制 │←── 对比GFL无PLL
  │  - 下垂/VSM │    GFM自主生成角度
  │  - 惯性响应 │
  └──────┬──────┘
         │
         ▼
  ┌─────────────┐
  │   电压环    │
  │ (控制v_dq)  │
  └──────┬──────┘
         │ v_dq*
         ▼
  ┌─────────────┐
  │   PWM调制   │
  └─────────────┘
```

**关键特征**：
- 无PLL，自主生成相位
- 电压源特性
- 内置惯量和阻尼

## 2. 物理模型与数学描述

### 2.1 下垂控制

**P-f下垂**：
$$
f = f_0 - k_p (P - P_0)$$

**Q-V下垂**：
$$
V = V_0 - k_q (Q - Q_0)$$

其中，$k_p, k_q$为下垂系数，$f_0, V_0$为额定值。

### 2.2 虚拟同步机(VSM)

**转子运动方程**：
$$
J\frac{d\omega}{dt} = P_{ref} - P - D(\omega - \omega_0)$$
$$
\frac{d\theta}{dt} = \omega$$

**励磁系统**：
$$
\tau_f \frac{dE}{dt} = V_{ref} + k_q(Q_{ref} - Q) - E$$

其中，$J$为虚拟惯量，$D$为阻尼系数。

### 2.3 输出功率计算

**瞬时功率**：
$$
P = \frac{3}{2}(v_d i_d + v_q i_q)$$
$$
Q = \frac{3}{2}(v_q i_d - v_d i_q)$$

## 3. 适用边界

**适用场景**：
- 弱电网/孤岛系统
- 100%新能源电网
- 需要惯量支撑的场合
- 黑启动需求
- 多机并联运行

**挑战与限制**：
- 故障电流大
- 暂态稳定性复杂
- 多机同步问题
- 保护协调困难
- 控制参数整定

## 代表性来源

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| Virtual Synchronous Machine Modeling for EMT Simulation of Grid-Forming Inverters | 2020 | VSM控制GFM变流器的EMT仿真建模与惯量响应分析 |
| Transient Stability Analysis of Droop-Controlled Grid-Forming Inverters | 2021 | 下垂控制GFM的暂态稳定性分析与EMT建模方法 |
| Grid-Forming Inverter Black-Start Capability in EMT Studies | 2023 | GFM变流器黑启动能力建模与EMT仿真验证 |

## 相关方法
- [[state-space-method|状态空间法]] - GFM状态空间建模
- [[droop-control-model|下垂控制]] - 下垂控制策略
- [[average-value-model|平均值模型]] - GFM平均值简化
- [[numerical-integration|数值积分]] - 惯量响应仿真
- [[multirate-method|多速率方法]] - 多GFM并行仿真

## 相关模型
- [[gfl-inverter-model|跟网型变流器]] - GFL与GFM对比
- [[vsc-model|VSC模型]] - 换流器主电路
- [[pll-model|锁相环]] - 对比GFM无PLL
- [[bess-model|电池储能]] - 储能GFM
- [[mtdc-model|MTDC模型]] - 多端直流GFM

## 相关主题
- [[vsc-hvdc]] - 柔性直流输电
- [[droop-control-model|下垂控制]] - 功率均分策略
- [[real-time-simulation]] - GFM实时仿真
- [[wind-farm-modeling]] - 风电场GFM
- [[network-equivalent]] - 电网等值

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自EMT领域学术文献的深度分析*
