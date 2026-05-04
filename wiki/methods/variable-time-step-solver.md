---
title: "变步长求解器 (Variable Time Step Solver)"
type: method
tags: [variable-time-step, adaptive, error-control, stiff-system, emt-simulation]
created: "2026-05-04"
---

# 变步长求解器 (Variable Time Step Solver)

## 定义与边界

变步长求解器是根据解的局部特性动态调整积分步长的数值积分方法，在解变化缓慢时采用大步长提高效率，在变化剧烈时采用小步长保证精度。与固定步长方法相比，变步长方法在相同精度要求下通常计算效率更高，但实现更复杂。

**边界限定**：本方法适用于离线仿真，实时仿真通常需固定步长。

## EMT中的作用

变步长求解提高非刚性系统的仿真效率：

- **暂态初期**：小步长捕捉快速变化
- **稳态阶段**：大步长提高效率
- **开关事件**：自动检测并处理
- **精度控制**：局部截断误差可控

## 主要分支与机制

### 1. 误差估计

**局部截断误差**：
$$\tau_n = \|y_{n+1} - y(t_{n+1})\|$$

**步长选择**：
$$\Delta t_{new} = \Delta t_{old} \left(\frac{\epsilon}{\|\tau_n\|}\right)^{1/p}$$

### 2. Runge-Kutta-Fehlberg

**RK45**：
4阶和5阶RK同时计算，差值作为误差估计。

**嵌入式公式**：
共享中间计算，减少开销。

### 3. 多步法

**Adams-Bashforth-Moulton**：
预测-校正格式，PECE模式。

**Gear法（BDF）**：
适合刚性系统，可变阶数。

## 形式化表达

### 步长控制

PID控制型步长选择：
$$\Delta t_{n+1} = \Delta t_n \left(\frac{\epsilon}{e_n}\right)^{k_1} \left(\frac{e_{n-1}}{e_n}\right)^{k_2} \left(\frac{e_{n-1}e_{n-2}}{e_n^2}\right)^{k_3}$$

### 开关处理

事件定位：
$$t_{switch}: g(t_{switch}) = 0$$

插值计算开关时刻状态。

## 适用边界与失败模式

### 适用条件

- 离线仿真
- 精度要求明确
- 非实时应用

### 失效边界

- **频繁开关**：步长调整开销大
- **刚性系统**：稳定性限制步长
- **事件检测**：错过开关时刻

## 与相关页面的关系

- [[numerical-integration]] - 数值积分方法
- [[stiff-system-handling]] - 刚性系统处理
- [[switch-modeling]] - 开关建模（事件处理）
- [[trapezoidal-rule]] - 梯形积分法
- [[interpolation-method]] - 插值方法
- [[numerical-integration]] - 数值积分方法
- [[state-space-method]] - 状态空间法
- [[vector-fitting]]
- [[average-value-model]]
- [[nodal-analysis]]
## 代表性来源

- Hairer, E., et al., "Solving ODE I & II," *Springer*, 1993.
- MATLAB ODE Suite文档

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
