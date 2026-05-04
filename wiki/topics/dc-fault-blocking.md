---
title: "直流故障闭锁 (DC Fault Blocking)"
type: topic
tags: [dc-fault, blocking, mmc, hvdc, protection, fault-current]
created: "2026-05-04"
---

# 直流故障闭锁 (DC Fault Blocking)

## 定义与边界

直流故障闭锁是多端直流（MTDC）电网中换流器在检测到直流侧故障时采取的快速阻断故障电流的控制策略。由于直流故障电流上升快、无自然过零点，换流器需在数毫秒内闭锁或切换到故障阻断模式，防止设备损坏和系统崩溃。

**边界限定**：本页面聚焦于基于电力电子的直流故障处理策略，不包括机械断路器。

## EMT中的作用

直流故障闭锁是MTDC系统保护的核心：

- **故障隔离**：快速阻断故障电流
- **系统保护**：保护换流器不受过流损坏
- **选择性隔离**：仅隔离故障线路而非整个系统
- **恢复策略**：故障清除后的系统重启

## 主要分支与机制

### 1. 半桥MMC故障特性

**故障电流路径**：
- 子模块电容放电
- 二极管续流
- 交流侧馈入

**闭锁效果**：
- 半桥MMC无法阻断二极管续流
- 需依赖交流断路器

### 2. 全桥MMC故障阻断

**负电平输出**：
- 输出负电压抵消线路电压
- 主动阻断故障电流

**能量耗散**：
- 子模块电阻耗散能量
- 或斩波电阻

### 3. 混合拓扑

**半桥+全桥**：
- 大部分为半桥（低成本）
- 少量全桥用于故障阻断

**二极管箝位**：
- 额外二极管路径
- 成本与性能折中

## 形式化表达

### 故障电流

RLC放电：
$$i(t) = \frac{V_0}{\omega_d L}e^{-\alpha t}\sin(\omega_d t)$$

其中：
$$\alpha = \frac{R}{2L}, \quad \omega_d = \sqrt{\frac{1}{LC} - \alpha^2}$$

### 阻断时间

全桥MMC阻断时间：
$$t_{block} < 5\text{ms}$$

## 适用边界与失败模式

### 适用条件

- 故障检测快速准确
- 换流器具备阻断能力
- 系统能承受短时过流

### 失效边界

- **检测延迟**：故障扩大
- **阻断失败**：设备损坏
- **过电压**：能量无处耗散
- **通信故障**：协调失败

## 与相关页面的关系

- [[mmc-model]] - MMC换流器模型
- [[fault-analysis-methods]] - 故障分析方法
- [[fault-ride-through]] - 故障穿越
- [[vsc-hvdc]] - VSC-HVDC系统
- [[protection-relay-modeling]] - 继电保护建模

## 代表性来源

- Marquardt, R., "Modular Multilevel Converter with DC Short Circuit Current Limitation," *EPE*, 2011.
- Li, C., et al., "DC Fault Protection Strategy for MMC-HVDC," *IEEE TPWRD*, 2018.

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
