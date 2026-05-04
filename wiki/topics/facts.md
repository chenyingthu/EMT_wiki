---
title: "柔性交流输电系统 (FACTS)"
type: topic
tags: [facts, power-electronics, transmission, control, hvac, compensation]
created: "2026-05-02"
---

# 柔性交流输电系统 (FACTS)

## 概述

柔性交流输电系统(Flexible AC Transmission Systems, FACTS)是指利用电力电子技术和现代控制理论，对交流输电系统的参数（电压、阻抗、功角）进行快速灵活调节，以提高输电能力、改善稳定性和增强可控性的一系列装置的总称。FACTS技术由Narain G. Hingorani博士于1988年首次提出，代表了现代电力系统控制技术的重要发展方向。

## 基本原理

### 功率传输方程
交流输电线路功率传输：
$$P = \frac{V_S V_R}{X} \sin\delta$$

其中：
- $V_S, V_R$: 送受端电压
- $X$: 线路电抗
- $\delta$: 功角差

FACTS通过调节$X$、$V$或$\delta$来控制功率传输。

### 可控参数
FACTS可实现对以下参数的快速控制：
- **串联补偿**：改变线路阻抗$X$
- **并联补偿**：调节节点电压$V$
- **相角控制**：调节功角$\delta$
- **综合控制**：多参数协调

## FACTS控制器分类

### 按连接方式分类

#### 串联型控制器
- **功能**：改变线路等效阻抗
- **TCSC** (可控串联补偿器)：晶闸管控制串联电容
- [[tcsc-model]] - TCSC模型
- **SSSC** (静止同步串联补偿器)：基于VSC的串联补偿
- `sssc` - SSSC
- **应用**：潮流控制、阻尼振荡

#### 并联型控制器
- **功能**：提供无功补偿、电压支撑
- **SVC** (静止无功补偿器)：晶闸管控制电抗器+电容器
- [[svc-model]] - SVC模型
- **STATCOM** (静止同步补偿器)：基于VSC的并联补偿
- [[statcom]] - STATCOM
- **应用**：电压调节、无功补偿

#### 综合型控制器
- **功能**：串并联组合，多目标控制
- **UPFC** (统一潮流控制器)：串联+并联VSC
- [[mmc-upfc电磁-机电混合仿真技术研究]] - UPFC
- **IPFC** (线间潮流控制器)：多线路协调
- `ipfc` - IPFC
- **应用**：全面潮流控制、多目标优化

### 按功率电子器件分类

| 类型 | 代表装置 | 器件 | 响应速度 |
|------|----------|------|----------|
| 第一代 | SVC, TCSC | 晶闸管 | 1-2周波 |
| 第二代 | STATCOM, SSSC, UPFC | VSC(IGBT) | <1周波 |
| 第三代 | 基于MMC | MMC | <1周波，高压大容量 |

## 核心功能

### 功率传输能力
- **输电能力**：提高30-50%
- **稳定裕度**：增加暂态稳定极限
- `transient-stability-limit` - 暂态稳定极限
- **负载分配**：优化潮流分布
- [[optimal-power-flow]] - 最优潮流

### 电压控制
- **电压支撑**：快速无功补偿
- `voltage-regulation` - 电压调节
- **电压质量**：抑制闪变、谐波
- `power-quality` - 电能质量

### 稳定性改善
- **阻尼振荡**：抑制低频振荡
- `power-oscillation-damping` - 功率振荡阻尼
- **电压稳定**：防止电压崩溃
- `voltage-stability` - 电压稳定

## 数学模型

### SVC模型
TCR+FC型SVC：
$$Q_{SVC} = B_{SVC} V^2$$
$$B_{SVC} = B_{FC} + B_{TCR}(\alpha)$$

其中：
- $B_{FC}$: 固定电容器导纳
- $B_{TCR}(\alpha)$: TCR可控导纳，$B_{TCR} = -\frac{2\alpha - \sin 2\alpha}{\pi X_L}$
- [[svc-model]] - SVC详细模型

### STATCOM模型
VSC型STATCOM：
$$P + jQ = V_{out} \cdot I^*$$
$$Q = \frac{V_S(V_{out} \cos\delta - V_S)}{X}$$

- [[statcom-model]] - STATCOM模型

### TCSC模型
$$X_{TCSC} = X_C \cdot k(\alpha)$$

其中$k(\alpha)$为触发角控制的补偿度。
- [[tcsc-model]] - TCSC模型

## 控制系统

### 分层控制
- **系统级**：区域协调控制
- **装置级**：FACTS本地控制
- `facts-control` - FACTS控制
- **设备级**：PWM变流器控制
- `pwm-control` - PWM控制

### 控制模式
| 模式 | 目标 | 应用 |
|------|------|------|
| 恒电压 | 维持节点电压 | 电压支撑 |
| 恒无功 | 固定无功输出 | 无功补偿 |
| 恒阻抗 | 固定等效阻抗 | 潮流控制 |
| 阻尼控制 | 抑制振荡 | 稳定性 |

## 在EMT仿真中的建模

### 详细模型
- **开关级**：IGBT详细模型
- [[detailed-switch-model]] - 详细开关模型
- **PWM控制**：脉宽调制
- `pwm-modulation` - PWM调制

### 平均值模型
- [[average-value-model]] - 平均值模型
- **占空比**：等效电压源
- **控制器**：PI/状态反馈
- [[pi-controller-model]] - PI控制器

### 等效模型
- **正序**：单相正序等效
- `positive-sequence` - 正序
- **相域**：三相详细模型
- [[phase-domain-modeling]] - 相域建模

## 应用场景

### 长距离输电
- **功率提升**：提高输送能力
- **稳定性**：增加稳定裕度
- `long-distance-transmission` - 长距离输电

### 城市电网
- **电压支撑**：重载区域
- `urban-grid` - 城市电网
- **电能质量**：抑制闪变

### 新能源并网
- [[renewable-energy-integration]] - 可再生能源并网
- **风电场**：电压波动补偿
- [[pmsg-offshore-wind-farm]] - 风电场
- **光伏电站**：无功调节
- [[pv-power-plant]] - 光伏电站

## 规划与设计

### 选址定容
- **灵敏度分析**：最大效益点
- [[sensitivity-analysis]] - 灵敏度分析
- **优化算法**：遗传算法、粒子群
- [[numerical-damping-optimization]] - 优化方法

### 协调控制
- **多FACTS协调**：避免交互
- `coordinated-control` - 协调控制
- **广域控制**：WAMS应用
- `wide-area-control` - 广域控制

## 与HVDC对比

| 特性 | FACTS | HVDC |
|------|-------|------|
| 技术 | 交流控制 | 交直流转换 |
| 成本 | 较低 | 较高 |
| 损耗 | 较小 | 较大(换流站) |
| 适用距离 | 中短距离 | 长距离 |
| 异步互联 | 不可 | 可以 |
| 控制速度 | 快 | 快 |

## 发展趋势
- **智能化**：AI优化控制
- `ai-control` - AI控制
- **宽禁带器件**：SiC/GaN应用
- `wide-bandgap` - 宽禁带器件
- **直流配网**：柔性直流
- `flexible-dc` - 柔性直流

## 相关主题
- [[power-electronics]] - 电力电子
- [[vsc-hvdc]] - 柔性直流输电
- [[modeling-synchronous-voltage-source-converters-in-transmission-system-planning-s]] - 输电系统
- `power-system-control` - 电力系统控制

## 标准规范
- **IEEE 1204**: FACTS术语
- **IEC 61954**: SVC标准
- **GB/T 20298**: 国家电网FACTS规范

## 来源论文

参见 [[index]] 获取更多FACTS相关文献。
