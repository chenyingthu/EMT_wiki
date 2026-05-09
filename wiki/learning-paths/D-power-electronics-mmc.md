---
title: "路线 D: 电力电子与 MMC 建模"
type: learning-path
tags: [learning-path, mmc, hvdc, power-electronics]
difficulty: "★★★"
estimated-time: "4-6 周"
created: "2026-05-10"
---

# 路线 D: 电力电子与 MMC 建模

**难度**: ★★★ | **预计时间**: 4-6 周 | **目标读者**: 电力电子研究人员

## 目标

掌握 MMC 的 EMT 建模方法，从详细开关模型到平均值模型。完成本路线后，应能独立搭建 MMC-HVDC 系统的 EMT 仿真模型并解释各模型层次的精度/效率取舍。

## 先修要求

- 路线 A（EMT 基础）或同等知识
- 电力电子技术基础（换流器基本拓扑、PWM 调制原理）
- 基本控制理论（PI 控制、dq 变换）

## 学习路径

### Phase 1: 开关建模基础

**目标**: 理解电力电子开关的 EMT 建模方法

| 步骤 | 页面 | 内容 |
|:----:|------|------|
| 1.1 | [[switch-modeling]] | 开关建模分类：二值电阻、分段线性、详细模型 |
| 1.2 | [[switching-function-method]] | 开关函数的数学描述，PWM 占空比计算 |
| 1.3 | [[fixed-admittance]] | 恒导纳模型(ADC)的原理，避免矩阵重构 |

---

### Phase 2: VSC 基础

**目标**: 掌握两电平/三电平 VSC 的 EMT 模型

| 步骤 | 页面 | 内容 |
|:----:|------|------|
| 2.1 | [[vsc-model]] | 两电平和三电平 VSC 拓扑与 EMT 实现 |
| 2.2 | [[pwm-modulation]] | SPWM/SVPWM 调制策略 |
| 2.3 | [[vector-control]] | 矢量控制：dq 解耦、电流内环、功率外环 |
| 2.4 | [[grid-forming-control]] | 构网型控制基础 |

**补充**: [[coordinate-transformation-model]]（Clarke/Park 变换）、[[pll-model]]（锁相环）

---

### Phase 3: MMC 详细模型

**目标**: 深入理解 MMC 的结构和详细开关模型

| 步骤 | 页面 | 内容 |
|:----:|------|------|
| 3.1 | [[mmc-model]] | MMC 整体结构：三相六桥臂，子模块级联 |
| 3.2 | [[submodule-model]] | 子模块类型：半桥、全桥、箝位双子模块 |
| 3.3 | [[half-bridge-smb]] | 半桥子模块的详细建模 |
| 3.4 | [[fbsm]] | 全桥子模块与故障阻断能力 |
| 3.5 | [[cdsm]] | 箝位双子模块结构 |
| 3.6 | [[mbsm]] | MMC 子模块综合比较 |
| 3.7 | [[mmc-modeling]] | 主题深化：MMC 建模技术纵览 |

---

### Phase 4: MMC 等效模型

**目标**: 学习 MMC 的等效建模方法，实现精度/效率的取舍

| 步骤 | 页面 | 内容 |
|:----:|------|------|
| 4.1 | [[average-value-model]] | 基于开关周期平均化的桥臂模型 |
| 4.2 | [[detailed-equivalent-model]] | 戴维南等效 DEM（最常用的高效模型） |

**核心对比**:

| 模型层级 | 精度 | 速度 | 适用场景 |
|---------|:----:|:----:|---------|
| 详细开关模型 | 最高 | 最慢 | 子模块级波形、器件应力 |
| DEM (戴维南等效) | 较高 | 快 | MMC-HVDC 系统级 EMT |
| AVM (平均值模型) | 中等 | 最快 | 机电暂态、控制设计 |

---

### Phase 5: MMC 控制

**目标**: 掌握 MMC 的核心控制策略

| 步骤 | 页面 | 内容 |
|:----:|------|------|
| 5.1 | [[nearest-level-control]] | 最近电平调制 NLC |
| 5.2 | [[circulating-current-suppression]] | 环流抑制控制（二倍频负序）|
| 5.3 | [[vsc-control]] | VSC 整体控制架构 |

**补充**: [[pi-controller-model]]（PI 控制器设计与离散实现）

---

### Phase 6: MMC-HVDC 系统

**目标**: 整合知识，理解 MMC-HVDC 系统级 EMT 仿真

| 步骤 | 页面 | 内容 |
|:----:|------|------|
| 6.1 | [[vsc-hvdc]] | VSC-HVDC 系统架构 |
| 6.2 | [[mtdc-model]] | 多端直流 MTDC 拓扑与控制 |
| 6.3 | [[back-to-back-hvdc]] | 背靠背 HVDC 结构 |
| 6.4 | [[hvdc-control]] | HVDC 控制策略 |
| 6.5 | [[commutation-failure]] | 换相失败分析（LCC HVDC）|
| 6.6 | [[dc-protection]] | 直流保护原理 |

---

### Phase 7（可选）: 直流电网与故障

| 页面 | 内容 |
|------|------|
| [[dc-fault-blocking]] | 直流故障阻断机制 |
| [[dc-pfc]] | 直流故障限流器 |
| [[dccb]] | 直流断路器 |

## 验证方式

完成本路线后，应能：

1. **解释模型层级**：对比 MMC 详细模型、DEM、AVM 的精度、效率和实现复杂度
2. **搭建仿真模型**：在概念层面设计一个 MMC-HVDC 系统的 EMT 模型（含主电路和控制）
3. **分析环流**：解释 MMC 环流的产生机制和抑制方法
4. **选择子模块**：根据应用需求（故障阻断、成本、损耗）选择合适的子模块类型

## 进阶方向

- 主题 [[wideband-oscillation-stability]] — MMC-HVDC 宽频振荡
- 路线 [[E-hybrid-simulation]] — 含 MMC 的混合仿真
- 路线 [[G-renewable-integration]] — 新能源并网

## 对应书稿章节

第二篇 输配电篇：Ch7（MMC 建模）、Ch8（MMC-HVDC 控制）

## 关键来源论文

- Gnanarathna 等 (2011) — 高效 MMC 等效模型（DEM）
- Peralta 等 (2012) — 详细 MMC 模型与验证
- Saad 等 (2013) — MMC 在实时仿真中的实现
- Beddard 等 (2014) — MMC 平均值模型对比
