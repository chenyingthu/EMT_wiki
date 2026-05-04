---
title: "等面积法则 (Equal Area Criterion)"
type: method
tags: [equal-area, stability, transient, swing-equation, direct-method, single-machine, power-angle]
created: "2026-05-02"
---

# 等面积法则 (Equal Area Criterion)

## 概述

等面积法则(Equal Area Criterion)是分析单机无穷大系统暂态稳定性的经典直接法，由前苏联学者在1930年代提出，是电力系统稳定分析中最直观、最重要的方法之一。该方法通过比较转子加速过程中获得的动能(加速面积)与减速过程中消耗的动能(减速面积)来判断系统稳定性，无需进行时域仿真即可快速评估稳定性。

等面积法则的物理意义清晰，数学推导简洁，是理解暂态稳定机理的重要工具。虽然其严格适用范围限于单机无穷大系统，但通过扩展等面积准则(EEAC)等方法，已推广至多机系统分析，在工程实践中发挥着重要作用。

## 基本原理

### 摇摆方程回顾

单机无穷大系统摇摆方程：
$$M\frac{d^2\delta}{dt^2} = P_m - P_e$$

其中：
- $M$: 惯性常数(s)
- $\delta$: 功角(rad)
- $P_m$: 机械功率(p.u.)
- $P_e$: 电磁功率(p.u.)

### 等面积法则推导

**能量方程推导**:
将摇摆方程两边乘以 $\frac{d\delta}{dt}$：
$$M\frac{d^2\delta}{dt^2}\frac{d\delta}{dt} = (P_m - P_e)\frac{d\delta}{dt}$$

即：
$$M\frac{d\omega}{dt}\omega = (P_m - P_e)\frac{d\delta}{dt}$$

**积分得到能量方程**:
对两边积分：
$$\int_{\delta_0}^{\delta} M\omega d\omega = \int_{\delta_0}^{\delta} (P_m - P_e) d\delta$$

左边为动能变化：
$$\frac{1}{2}M\omega^2 - \frac{1}{2}M\omega_0^2$$

若初始静止($\omega_0 = 0$)：
$$\frac{1}{2}M\omega^2 = \int_{\delta_0}^{\delta} (P_m - P_e) d\delta$$

**物理意义**:
转子动能变化等于过剩功率对功角的积分。

## 面积分析

### 功率-功角曲线

**故障前**:
$$P_e^{pre} = \frac{E'V}{X_{pre}}\sin\delta = P_{max}^{pre}\sin\delta$$

**故障期间**:
$$P_e^{fault} = \frac{E'V}{X_{fault}}\sin\delta = P_{max}^{fault}\sin\delta$$

**故障切除后**:
$$P_e^{post} = \frac{E'V}{X_{post}}\sin\delta = P_{max}^{post}\sin\delta$$

**阻抗关系**:
$$X_{fault} > X_{post} > X_{pre}$$
$$P_{max}^{fault} < P_{max}^{post} < P_{max}^{pre}$$

### 加速面积(A1)

**定义**:
故障期间转子获得的动能：
$$A_1 = \int_{\delta_0}^{\delta_c} (P_m - P_e^{fault}) d\delta$$

**物理意义**:
- 过剩功率使转子加速
- 储存为转子动能
- 对应功角曲线下的面积

**计算**:
对于恒定机械功率和正弦功率特性：
$$A_1 = P_m(\delta_c - \delta_0) - P_{max}^{fault}(\cos\delta_0 - \cos\delta_c)$$

### 减速面积(A2)

**定义**:
故障切除后转子消耗的动能：
$$A_2 = \int_{\delta_c}^{\delta_{max}} (P_e^{post} - P_m) d\delta$$

**物理意义**:
- 制动功率使转子减速
- 消耗转子动能
- 对应功角曲线上的面积

**最大减速面积**:
$$A_{2max} = \int_{\delta_c}^{\delta_u} (P_e^{post} - P_m) d\delta$$
其中 $\delta_u$ 为不稳定平衡点。

**计算**:
$$A_2 = P_{max}^{post}(\cos\delta_c - \cos\delta_{max}) - P_m(\delta_{max} - \delta_c)$$

### 稳定判据

**稳定条件**:
$$A_1 < A_{2max}$$

**临界条件**:
$$A_1 = A_{2max}$$

**不稳定条件**:
$$A_1 > A_{2max}$$

**物理意义**:
转子获得的动能能够被系统完全吸收，系统保持稳定。

## 关键角度

### 初始功角($\delta_0$)

**定义**:
故障前稳态运行功角。

**计算**:
$$\delta_0 = \arcsin\left(\frac{P_m}{P_{max}^{pre}}\right)$$

**影响因素**:
- 传输功率水平
- 系统电压
- 等效电抗

### 故障切除角($\delta_c$)

**定义**:
故障切除时刻的功角。

**与切除时间关系**:
通过摇摆方程积分得到：
$$\delta_c = \delta(t_c)$$

### 不稳定平衡点($\delta_u$)

**定义**:
故障切除后功率特性曲线的不稳定平衡点：
$$P_m = P_{max}^{post}\sin\delta_u$$

**计算**:
$$\delta_u = \pi - \arcsin\left(\frac{P_m}{P_{max}^{post}}\right)$$

**位置**:
在功率特性曲线的下降段。

### 最大摇摆角($\delta_{max}$)

**定义**:
稳定情况下转子达到的最大功角：
$$A_1 = A_2(\delta_{max})$$

**计算**:
求解：
$$P_{max}^{post}(\cos\delta_c - \cos\delta_{max}) - P_m(\delta_{max} - \delta_c) = A_1$$

## 临界切除时间计算

### 临界切除角

**定义**:
使系统处于临界稳定状态的最小切除角：
$$A_1(\delta_{cc}) = A_{2max}$$

**计算方法**:
1. 计算 $A_{2max}$
2. 求解满足 $A_1 = A_{2max}$ 的 $\delta_{cc}$

**解析解**:
对于恒定机械功率：
$$P_m(\delta_{cc} - \delta_0) - P_{max}^{fault}(\cos\delta_0 - \cos\delta_{cc}) = A_{2max}$$

通常需要数值求解。

### 临界切除时间

**由角度转时间**:
利用摇摆方程：
$$\frac{d^2\delta}{dt^2} = \frac{P_m - P_e^{fault}}{M}$$

对于恒定过剩功率：
$$\delta(t) = \delta_0 + \frac{1}{2}\frac{P_m - P_e^{fault}}{M}t^2$$

**近似公式**:
$$CCT = \sqrt{\frac{2M(\delta_{cc} - \delta_0)}{P_m - P_e^{fault}}}$$

**精确计算**:
考虑功率特性的非线性，需要数值积分。

### 稳定裕度

**角度裕度**:
$$\Delta\delta = \delta_{cc} - \delta_c$$

**时间裕度**:
$$\Delta t = CCT - t_c$$

**功率裕度**:
$$\Delta P = P_{max}^{post}\sin\delta_u - P_m$$

## 图形化分析

### P-δ曲线分析

**曲线绘制**:
1. 绘制故障前、中、后三条功率曲线
2. 标出机械功率水平线
3. 标识各关键角度

**面积标识**:
- 加速面积：$P_m$ 与 $P_e^{fault}$ 之间的面积
- 减速面积：$P_e^{post}$ 与 $P_m$ 之间的面积

**稳定判断**:
- 加速面积 < 最大减速面积：稳定
- 两面积相等：临界
- 加速面积 > 最大减速面积：不稳定

### 相平面图

**状态空间**:
以 $\delta$ 和 $\omega$ 为坐标的状态平面。

**轨迹**:
- 稳定：闭合轨道
- 不稳定：发散轨迹
- 临界：分隔线

**稳定域**:
由分隔线包围的区域为稳定域。

## 扩展应用

### 扩展等面积准则(EEAC)

**基本思想**:
将多机系统等效为单机无穷大系统。

**步骤**:
1. 识别临界机群和剩余系统
2. 等效为两机系统
3. 转换为单机无穷大
4. 应用等面积准则

**等效**:
$$M_{eq} = \frac{M_{crit}M_{rest}}{M_{crit} + M_{rest}}$$

### SIME(单机等效)

**动态识别**:
- 时域仿真识别失稳模式
- 动态确定临界机组
- 实时等效计算

**优势**:
- 可处理复杂故障
- 适用于多摆稳定
- 精度高

### 两机系统

**直接应用**:
两机系统可精确应用等面积准则。

**等效**:
转换为相对摇摆：
$$M_{eq}\frac{d^2\delta_{12}}{dt^2} = P_{m,eq} - P_{e,eq}$$

## 局限性

### 模型假设

**经典模型**:
- 恒定暂态电势 $E'$
- 忽略励磁动态
- 适用于首摆稳定

**恒定机械功率**:
- 忽略调速器响应
- 适用于短时间分析
- 首摆期间合理

**网络简化**:
- 导纳矩阵简化
- 负荷模型简化
- 影响精度

### 适用范围

**单机无穷大**:
严格适用。

**多机系统**:
需要等效简化，精度受限。

**复杂故障**:
- 非对称故障
- 多次故障
- 分析困难

### 精度问题

**保守性**:
- 结果可能偏保守
- 稳定裕度估计偏小
- 经济性考虑

## 工程应用

### 保护整定

**CCT计算**:
- 快速评估保护配合
- 继电器定值校验
- 加速距离保护

**稳定裕度评估**:
- 运行方式安排
- 预防控制
- 紧急控制

### 规划设计

**传输极限**:
- 暂态稳定极限
- 功率传输能力
- 网架规划

**FACTS配置**:
- 补偿度优化
- 提高稳定极限
- 经济效益

### 在线应用

**快速筛选**:
- 大量故障场景
- 快速稳定评估
- 实时应用

**安全约束**:
- 预防控制
- 优化调度
- 安全运行

## 相关方法

- [[transient-stability-analysis]] - 暂态稳定性分析: 详细分析方法
- [[swing-equation]] - 摇摆方程: 数学模型
- `direct-method` - 直接法: 不通过时域仿真的方法
- [[energy-function]] - 能量函数法: 多机等效方法
- [[eeac]] - 扩展等面积准则: 多机扩展

## 来源论文

参见 [[index]] 获取更多等面积法则相关文献。
