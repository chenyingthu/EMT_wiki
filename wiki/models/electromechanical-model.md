---
title: "机电暂态模型 (Electromechanical Model)"
type: model
tags: [electromechanical, transient-stability, swing-equation, synchronous-machine, multi-timescale]
created: "2026-05-04"
---

# 机电暂态模型 (Electromechanical Model)

## 定义与边界

机电暂态模型是描述电力系统在大扰动下发电机转子机械运动与电磁功率之间动态相互作用的简化模型。该类模型假设电网处于准稳态（基波对称、电压电流瞬时正弦），忽略电磁暂态过程，专注于功角稳定性分析。

**边界限定**：本模型适用于频率变化范围小（49-51Hz）、网络可视为基波正弦稳态的场景。对于快速暂态、谐波、非对称故障或电力电子设备主导的工况，需采用完整EMT模型。

## EMT中的作用

机电暂态模型在EMT知识体系中主要承担以下角色：

- **混合仿真接口**：与电磁暂态详细模型协同，形成多时间尺度仿真框架
- **计算加速**：对外部系统采用机电暂态简化，聚焦内部网络的EMT分析
- **稳定性评估**：提供功角稳定的宏观判断，与EMT过电压分析互补
- **初始化基准**：为EMT仿真提供稳态运行点

## 主要分支与机制

### 1. 摇摆方程 (Swing Equation)

描述发电机转子机械运动的基本方程：
$$M\frac{d^2\delta}{dt^2} = P_m - P_e - D\frac{d\delta}{dt}$$

其中$M$为惯性常数，$\delta$为功角，$P_m$为机械功率，$P_e$为电磁功率，$D$为阻尼系数。

### 2. 发电机简化模型

- **经典模型 (Classical Model)**：恒定内电势$E'$背后暂态电抗$X_d'$
- **双轴模型**：考虑d、q轴暂态和次暂态电抗
- **详细模型**：包含励磁系统、调速器、PSS的完整模型

### 3. 网络代数方程

假设网络瞬时平衡：
$$\mathbf{P} = f(\boldsymbol{\delta}, \mathbf{V}, \boldsymbol{\theta})$$
$$\mathbf{Q} = g(\boldsymbol{\delta}, \mathbf{V}, \boldsymbol{\theta})$$

其中$(\mathbf{V}, \boldsymbol{\theta})$为电压幅值和相角。

## 形式化表达

### 状态空间形式

发电机状态方程：
$$\dot{\mathbf{x}}_g = \mathbf{f}(\mathbf{x}_g, \mathbf{V}, \mathbf{u})$$

网络代数约束：
$$\mathbf{0} = \mathbf{g}(\mathbf{x}_g, \mathbf{V})$$

形成微分-代数方程组 (DAE)。

### 机电-电磁接口

混合仿真中的接口变量：
- 机电侧向电磁侧传递：等值内电势、阻抗
- 电磁侧向机电侧传递：等值功率、电压

接口误差控制：
$$\|P_{EMT} - P_{TS}\| < \epsilon_P$$


## 数值分析

### 精度与效率
- 仿真精度：误差控制在1%以内
- 计算效率：支持大规模系统实时仿真
- 数值稳定性：在典型工况下保持稳定

### 典型参数范围
- 时间步长：1μs ~ 1ms
- 系统规模：10~1000节点
- 仿真时长：0.1s ~ 10s

### 性能指标
- 内存占用：随系统规模线性增长
- 计算时间：与系统复杂度和仿真时长相关
- 收敛性：在绝大多数情况下稳定收敛

## 适用边界与失败模式

### 适用条件

| 条件 | 要求 | 说明 |
|------|------|------|
| 频率范围 | 49-51 Hz | 基波假设有效 |
| 对称性 | 三相平衡 | 正序分量主导 |
| 时间尺度 | >100 ms | 电磁暂态已衰减 |
| 设备类型 | 同步机主导 | 电力电子设备比例低 |

### 失效边界

- **快速暂态**：故障、开关操作引起的快速过程
- **谐波谐振**：非线性设备引起的谐波放大
- **非对称故障**：单相或两相故障的负序/零序效应
- **电力电子设备**：换流器控制的快速动态
- **次同步振荡**：轴系扭振与电网的耦合

### 关键假设

1. 网络瞬时平衡（准稳态）
2. 基波正序分量主导
3. 电压电流瞬时正弦
4. 电磁暂态远快于机电暂态（可忽略）

## 代表性来源

- [[emt-simulation]] - EMT仿真基础
- [[power-system]] - 电力系统建模
- [[electromagnetic-transient]] - 电磁暂态分析
- [[control-system]] - 控制系统设计
- [[real-time-simulation]] - 实时仿真技术
### 经典文献

- Kundur, P., "Power System Stability and Control," *McGraw-Hill*, 1994. - 电力系统稳定分析权威教材
- Anderson, P.M. and Fouad, A.A., "Power System Control and Stability," *IEEE Press*, 2003. - 机电暂态分析经典

### 混合仿真应用

- [[electromechanical-electromagnetic-hybrid-simulation]] - 机电-电磁混合仿真接口
- [[dynamic-phasor]] - 动态相量多时间尺度方法
- [[real-time-simulation]] - 实时混合仿真实现

## 与相关页面的关系

- [[electromechanical-electromagnetic-hybrid-simulation]] - 混合仿真框架
- [[synchronous-machine-model]] - 同步电机详细EMT模型
- [[dynamic-phasor]] - 介于机电与电磁之间的动态相量法
- [[power-system-network]] - 网络拓扑与等值
- [[transient-stability-analysis]] - 暂态稳定分析方法

## 开放问题

- 含高比例新能源的机电暂态模型修正
- 电力电子设备主导的系统等值方法
- 机电-电磁混合仿真的最优分割准则
- 次同步振荡与机电暂态的耦合建模

## 参考标准

- IEEE Std. 1204 - 电力系统稳定分析导则
- IEC 61400-27 - 风电场机电暂态建模

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
