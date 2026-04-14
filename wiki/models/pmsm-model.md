---
title: "永磁同步电机 (PMSM)"
type: model
tags: [pmsm, synchronous-machine, permanent-magnet, motor, generator]
created: "2026-04-14"
---

# 永磁同步电机 (PMSM)

## 概述

永磁同步电机（Permanent Magnet Synchronous Machine, PMSM）是采用永磁体励磁的同步电机。相比电励磁同步电机，PMSM具有效率高、功率密度大、响应快等优点，广泛应用于风力发电、电动汽车和工业驱动领域。

## 主要特点

- 永磁体励磁，无需励磁绕组
- 高效率、高功率密度
-  dq轴电感不对称（凸极效应）
- 退磁风险（高温、大电流）
- 适用于变速恒频运行

## EMT建模方法

### 1. 传统dq0模型
- Park变换建立dq轴方程
- 适用于对称运行条件
- 计算效率高

### 2. 相域模型
- 直接在abc坐标系下建模
- 适用于不对称和故障条件
- 计算量大

### 3. 有限元耦合模型
- 基于FEA结果定义磁链
- 精确表征磁饱和和非线性
- 适用于高精度实时仿真

## 应用场景

- 直驱风力发电
- 电动汽车驱动
- 工业伺服系统
- 航空航天

## 相关方法
- [[state-space-method]]
- [[fixed-admittance]]

## 相关主题
- [[real-time-simulation]]
- [[frequency-dependent-modeling]]


## 论文方法分析
> 基于 1 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|| 基于有限元分析(FEA)的降阶建模 | 1 | A Flux-Defined PMSM Model Based on FEA Results for Real-Time EMT Simul |
| 磁链定义法 | 1 | A Flux-Defined PMSM Model Based on FEA Results for Real-Time EMT Simul |
| 三线性插值算法 | 1 | A Flux-Defined PMSM Model Based on FEA Results for Real-Time EMT Simul |
| 免数据表求逆的电流导数直接计算法 | 1 | A Flux-Defined PMSM Model Based on FEA Results for Real-Time EMT Simul |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|| 永磁同步电机(PMSM) | 1 |
| 基于FEA的降阶模型(ROM) | 1 |
| 传统集总参数PMSM模型 | 1 |
| 电动汽车动力总成系统 | 1 |
### 验证方式分布
- **仿真与RTDS硬件实验对比**: 1 篇
## 技术演进脉络
### 2025年 (1篇)
- **A Flux-Defined PMSM Model Based on FEA Results for Real-Time EMT Simulation**
  - 💡 提出了一种直接基于磁链数据计算电流导数的免求逆方法，结合高效插值与外推稳定策略，实现了高保真FEA级PMSM模型的微秒级实时电磁暂态仿真。
  - 提出了一种无需对磁链数据表求逆即可直接计算电流导数的新方法，大幅缩短模型预处理时间。
  - 设计了一种高效的三线性插值算法，有效提升了模型在电磁暂态仿真中的计算效率。
## 关键发现汇总
- [2025] **A Flux-Defined PMSM Model Based on FEA Results for Real-Time**: 模型在RTDS硬件上实现了小于1 µs的仿真步长，满足严格的实时性要求。
- [2025] **A Flux-Defined PMSM Model Based on FEA Results for Real-Time**: 仿真结果与高精度FEA基准高度一致，精度显著优于传统集总参数模型。
- [2025] **A Flux-Defined PMSM Model Based on FEA Results for Real-Time**: 在电动汽车动力总成测试案例中验证了模型在复杂动态工况下的高保真度与实用性。
## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-flux-defined-pmsm-model-based-on-fea-results-for-real-time-emt-simulation|A Flux-Defined PMSM Model Based on FEA Results for Real-Time]] | 2025 |
