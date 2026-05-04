---
title: "大步长仿真 (Large Time Step Simulation)"
type: method
tags: [large-time-step, lts, acceleration, implicit-integration, multirate]
created: "2026-05-04"
---

# 大步长仿真 (Large Time Step Simulation)

## 定义与边界

大步长仿真（Large Time Step, LTS）是通过使用比传统EMT仿真更大的时间步长来加速计算的技术，通常结合隐式积分、多速率方法或模型简化来实现。LTS适用于对快速暂态不敏感或已通过等值简化的问题，可显著缩短仿真时间。

**边界限定**：本方法适用于暂态过程较慢或可简化的场景，快速暂态分析需保持小步长。

## EMT中的作用

大步长仿真加速特定类型分析：

- **长期动态**：数秒至数分钟的机电过程
- **准稳态**：接近稳态的运行分析
- **蒙特卡洛**：批量工况的统计仿真
- **规划研究**：方案筛选的快速评估

## 主要分支与机制

### 1. 隐式积分大步长

**后向欧拉**：
L稳定特性，允许大步长：
$$x_{n+1} = x_n + \Delta t \cdot f(x_{n+1})$$

**梯形法**：
A稳定，但大步长时数值振荡：
$$x_{n+1} = x_n + \frac{\Delta t}{2}(f(x_n) + f(x_{n+1}))$$

**Gear法**：
多步法，适合刚性系统：
$$\sum_{j=0}^k \alpha_j x_{n+1-j} = \Delta t \beta_0 f(x_{n+1})$$

### 2. 多速率方法

**慢子系统大步长**：
- 机电设备用大步长
- 电磁网络用小步长
- 插值同步

**变步长**：
- 暂态期间小步长
- 稳态后大步长
- 自动调整

### 3. 模型简化

**平均值模型**：
- 开关周期平均
- 忽略高频纹波
- 允许大步长

**等值模型**：
- 外部系统等值
- 内部网络详细
- 分区求解

## 形式化表达

### 稳定性区域

隐式方法稳定区域：
- 后向欧拉：全左半平面
- 梯形法：全左半平面（除虚轴）
- Gear-2：全左半平面

### 截断误差

局部截断误差：
$$\tau_n = C \cdot \Delta t^{p+1}$$

$p$为方法阶数。

### 步长选择

自适应步长：
$$\Delta t_{new} = \Delta t_{old} \cdot \left(\frac{\epsilon}{\|e\|}\right)^{1/p}$$

## 适用边界与失败模式

### 适用条件

- 快速暂态已衰减
- 关心慢动态过程
- 精度要求适度
- 刚性系统

### 失效边界

- **快速暂态**：大步长丢失细节
- **数值振荡**：梯形法振荡
- **精度不足**：误差累积
- **稳定性**：显式方法发散

## 代表性来源

- [[numerical-integration]] - 数值积分
- [[multirate-method]] - 多速率方法
- [[average-value-model]] - 平均值模型

## 与相关页面的关系

- [[numerical-integration]] - 数值积分
- [[multirate-method]] - 多速率
- [[model-order-reduction]] - 模型降阶
- [[stiff-system-handling]] - 刚性系统处理
- [[numerical-integration]] - 数值积分方法
- [[state-space-method]] - 状态空间法

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
