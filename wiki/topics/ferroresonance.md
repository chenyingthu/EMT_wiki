---
title: "铁磁谐振 (Ferroresonance)"
type: topic
tags: [ferroresonance, transformer, nonlinear, resonance, transient]
created: "2026-04-14"
---

# 铁磁谐振 (Ferroresonance)

## 概述

铁磁谐振是电力系统中由于变压器铁芯非线性磁化特性与系统电容相互作用产生的非线性谐振现象。铁磁谐振会导致过电压、过电流，威胁设备安全，是EMT仿真研究的重要课题。

## 产生条件

- 变压器铁芯饱和（非线性励磁）
- 系统电容（线路对地电容、CCVT电容等）
- 系统扰动（开关操作、单相接地故障等）
- 低阻尼系统

## 主要特征

- 非线性、多稳态特性
- 可能出现基频、次谐波、超谐波谐振
- 电压波形畸变严重
- 难以预测，具有混沌特性
- 持续时间可能很长

## EMT建模方法

### 1. 变压器磁滞模型
- Jiles-Atherton磁滞公式
- Preisach模型
- 实测磁滞曲线
- 精确表征非线性磁化特性

### 2. 电容模型
- 线路对地电容
- CCVT耦合电容
- 串联补偿电容

### 3. 仿真求解
- 需要小时间步长捕捉非线性动态
- 数值积分方法影响稳定性
- EMTP/EMTP-RV是主要仿真工具

## 抑制措施

- 增加阻尼电阻
- 使用消谐装置
- 优化系统参数设计
- 限制操作过电压

## 相关模型
- [[transformer-model]]
- [[cable-model]]
- [[transmission-line-model]]

## 相关方法
- [[numerical-integration]]
- [[nodal-analysis]]

## 相关主题
- [[frequency-dependent-modeling]]
- [[real-time-simulation]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[digital-time-domain-investigation-of-transient-behavior-of-coupling-capacitor-voltage-transformer-13&14|Digital Time-Domain Investigation of Transient Behavior of C]] | 1998 |
| [[saturable-reactor-hysteresis-model-based-on-jilesatherton-formulation-for-ferror|Saturable reactor hysteresis model based on Jiles-Atherton f]] | 2024 |
