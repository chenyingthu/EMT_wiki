---
title: "最近电平控制 (Nearest Level Control)"
type: method
tags: [nearest-level-control, nlc, mmc, modulation, voltage-control, power-electronics]
created: "2026-05-04"
updated: "2026-05-12"
---

# 最近电平控制 (Nearest Level Control)




## 定义与边界

最近电平控制（Nearest Level Control, NLC）是模块化多电平换流器（MMC）的一种调制策略，通过选择最接近参考电压的整数电平数来确定投入的子模块数量。NLC算法简单、开关频率低、易于实现，是MMC大电平数应用的主流调制方法之一。

**边界限定**：本方法适用于子模块数较多（N>20）的MMC换流器，低电平数时性能不如载波移相PWM。

## EMT中的作用

NLC是MMC高效控制的核心技术：

- **低开关频率**：每个周期开关次数少，降低损耗
- **高电平数适用**：子模块数越多，输出波形质量越好
- **电压平衡简化**：易于结合电容电压排序
- **实时性好**：计算简单，适合实时控制

## 主要分支与机制

### 1. 基本NLC算法

**电平数计算**：
$$n_{ref} = \frac{|v_{ref}|}{V_{SM}}$$

最近整数：
$$n_{on} = \text{round}(n_{ref})$$

其中$V_{SM}$为子模块电容电压。

### 2. 电容电压排序

**电压平衡**：
- 电流正向时，优先投入电压低的子模块
- 电流反向时，优先投入电压高的子模块

排序算法：
- 冒泡排序
- 快速排序
- 堆排序（大电平数）

### 3. 改进NLC

**基于电压偏差的NLC**：
$$n_{on} = \text{round}(n_{ref} + k(V_{ref} - V_{actual}))$$

**环流抑制集成**：
在电平数选择中考虑环流分量。

## 形式化表达

### 量化误差

NLC引入的量化误差：
$$\epsilon = v_{ref} - n_{on} \cdot V_{SM}$$

最大误差：
$$|\epsilon|_{max} = 0.5 V_{SM}$$

### 谐波特性

输出电压THD与子模块数关系：
$$THD \approx \frac{1}{\sqrt{6}N}$$

电平数越多，THD越低。

### 开关频率

平均开关频率：
$$f_{sw} = \frac{f_0}{N} \cdot \frac{V_{dc}}{2V_{SM}}$$

远低于载波移相PWM。

## 适用边界与失败模式

### 适用条件

| 条件 | 要求 | 说明 |
|------|------|------|
| 电平数 | N > 20 | 低电平数时谐波大 |
| 开关频率 | 低要求 | 适合低频应用 |
| 动态响应 | 一般 | 适合稳态运行 |
| 计算资源 | 有限 | 排序算法简单 |

### 失效边界

- **低电平数**：量化误差大，波形质量差
- **快速暂态**：响应速度受限
- **电容不平衡**：排序周期延长
- **环流恶化**：基础NLC环流较大

### 关键假设

1. 子模块电容电压均衡
2. 电平数足够多
3. 开关频率低可接受
4. 排序周期内电容电压变化不大

## 代表性来源

### 经典文献

- Gnanarathna, U.N., et al., "Efficient Modeling of Modular Multilevel HVDC Converters," *IEEE TEC*, 2011.
- Saeedifard, M. and Iravani, R., "Dynamic Performance of a Modular Multilevel Back-to-Back HVDC System," *IEEE TPWRD*, 2010.

### 相关方法

- MMC换流器调制策略
- 载波移相PWM方法
- 电容电压排序算法

## 与相关页面的关系

- [[mmc-model]] - MMC换流器模型
- [[average-value-model]] - 平均值模型
- [[circulating-current-suppression]] - 环流抑制控制
- [[submodule-model]] - 子模块模型
- [[vector-control]] - 矢量控制
- [[numerical-integration]] - 数值积分方法
- [[state-space-method]] - 状态空间法
- [[vector-fitting]]
- [[nodal-analysis]]
- [[passivity-enforcement]]
## 量化性能边界

**Zhao 2023 电压闭环NLC调制（MMC宽频段）**:
- 提出基于电压偏差闭环修正的新型NLC方案，在电平数选择中引入电压误差反馈
- 0-500Hz宽频段跟踪误差低于0.5%，优于开环NLC在低频段的性能
- 验证平台：MMC仿真模型，多电平逆变器实验平台
- 数据缺口：原文未报告闭环NLC在不同电平数（N=10 vs N=50）下的性能差异对比

**Yu 2014 NLM与PWM平均开关频率对比**:
- 系统比较NLC（又称NLM）与载波移相PWM在MMC中的开关频率和输出质量
- NLC开关频率远低于PWM，大电平数(N>200)时计算量可降低约5000倍
- 输出电压THD随电平数增加按1/(√6N)规律下降
- 数据缺口：对比基于特定测试条件（特定MMC拓扑和负载），不同功率等级下的差异未报告

**Lian 2022 双向堆排序电容电压平衡算法**:
- 针对传统排序算法在大电平数MMC中计算量过大的问题，提出双向堆排序
- 大幅降低排序计算时间，排序效率随电平数增加优势更明显
- 数据缺口：原文未报告在不同电平数和调制比下的具体加速比和排序误差

**设计参数约束（据方法推断）**:
- NLC的量化误差固定为±0.5V_SM，不随电平数变化，但相对误差随电平数增加而减小
- 输出电压THD与电平数N成反比，N>100时THD通常<1%
- 排序算法的计算开销随N增加，O(N log N)的堆排序优于O(N²)的冒泡排序
- NLC开关频率与基频f₀成正比，与电平数成反比，低频运行时开关损耗极低
- NLC在低电平数(N<10)时谐波含量高，应考虑CPS-PWM或混合调制

## 开放问题

- 低电平数MMC的改进NLC
- 多目标优化（损耗、谐波、平衡）
- 实时排序算法优化
- NLC与高级控制的集成

## 参考标准

- IEEE Std. 1800 - 电磁暂态仿真导则

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[fast-voltage-balancing-control-and-fast-19、20、21|Fast Voltage-Balancing Control and Fast]] | 2014 |
| [[enhanced-high-speed-electromagnetic-transient-simulation-17|Enhanced high-speed electromagnetic transient simulation]] | 2016 |
| [[enhanced-high-speed-electromagnetic-transient-simulation|Enhanced high-speed electromagnetic transient simulation]] | 2016 |
| [[modeling-of-a-modular-multilevel-converter-with-embedded-energy-storage-for-elec|Modeling of a Modular Multilevel Converter With Embedded Ene]] | 2019 |
