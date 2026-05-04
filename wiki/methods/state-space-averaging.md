---
title: "状态空间平均法 (State Space Averaging)"
type: method
tags: [state-space-averaging, ssa, averaged-model, small-signal, dc-dc-converter]
created: "2026-05-04"
---

# 状态空间平均法 (State Space Averaging)

## 定义与边界

状态空间平均法（State Space Averaging, SSA）是将开关变换器在一个开关周期内的状态方程进行加权平均，得到连续时间平均模型的方法。通过对开关周期内的不同拓扑状态进行占空比加权平均，SSA将时变系统转化为时不变系统，便于小信号分析和控制器设计。

**边界限定**：本方法适用于开关频率远高于系统带宽的情况（通常$f_{sw} > 10f_{BW}$），不适用于谐振变换器或变频调制。

## EMT中的作用

SSA是电力电子系统建模的基础方法：

- **小信号分析**：推导传递函数和频率响应
- **控制器设计**：基于线性化模型设计补偿器
- **稳定性分析**：特征值分析和Nyquist判据
- **多变换器系统**：简化大规模系统分析

## 主要分支与机制

### 1. 基本SSA方法

**开关周期平均**：
$$\dot{\mathbf{x}} = [d\mathbf{A}_1 + (1-d)\mathbf{A}_2]\mathbf{x} + [d\mathbf{B}_1 + (1-d)\mathbf{B}_2]\mathbf{u}$$

其中$d$为占空比，下标1、2对应开关导通和关断状态。

### 2. 小信号线性化

**稳态工作点**：
$$\mathbf{X} = -\mathbf{A}^{-1}\mathbf{B}U$$

**小信号模型**：
$$\hat{\dot{\mathbf{x}}} = \mathbf{A}\hat{\mathbf{x}} + \mathbf{B}\hat{\mathbf{u}} + \mathbf{E}\hat{d}$$

### 3. 扩展SSA

**广义状态空间平均（GSSA）**：
考虑开关谐波的影响，保留傅里叶系数。

**多相SSA**：
用于多相交错变换器。

## 形式化表达

### 传递函数推导

从SSA模型推导控制-输出传递函数：
$$G_{vd}(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{E}$$

### 稳态解

$$\mathbf{X} = -[d\mathbf{A}_1 + (1-d)\mathbf{A}_2]^{-1}[d\mathbf{B}_1 + (1-d)\mathbf{B}_2]U$$

## 适用边界与失败模式

### 适用条件

- 开关频率远大于系统带宽
- 占空比变化缓慢
- 连续导通模式（CCM）

### 失效边界

- **谐振变换器**：谐振频率接近开关频率
- **变频控制**：无法定义固定周期
- **大信号暂态**：超出小信号范围

## 代表性来源

- Middlebrook, R.D. and Ćuk, S., "A General Unified Approach to Modelling Switching-Converter Power Stages," *PESC*, 1976.
- Sanders, S.R., et al., "Generalized Averaging Method for Power Conversion Circuits," *IEEE TPE*, 1991.

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
