---
title: "伴随电路 (Companion Circuit)"
type: method
tags: [companion-circuit, nodal-analysis, discretization, emtp, trapezoidal, numerical-integration]
created: "2026-05-02"
---

# 伴随电路 (Companion Circuit)

## 概述

伴随电路法(Companion Circuit Method)是电磁暂态仿真软件(如EMTP、PSCAD)的核心数值方法，通过数值积分将动态元件(电感、电容)的时域微分方程转化为等效的离散代数方程。该方法将每个动态元件表示为诺顿等效电路——一个等效电阻与一个历史电流源并联，使得整个网络在每个时间步可表示为纯电阻性电路，便于使用节点电压法统一求解。伴随电路法由Hermann Dommel于1969年提出，是电力系统电磁暂态仿真的基础。

## 基本原理

### 离散化思想

**微分方程**:
$$L\frac{di}{dt} = v(t)$$

**数值积分**:
$$i_{n+1} - i_n = \frac{1}{L}\int_{t_n}^{t_{n+1}}v(t)dt$$

**梯形近似**:
$$i_{n+1} = i_n + \frac{\Delta t}{2L}(v_{n+1} + v_n)$$

### 诺顿等效

**标准形式**:
$$i_{n+1} = G_{eq}v_{n+1} + I_{hist}$$

**电感元件**:
$$G_{eq} = \frac{\Delta t}{2L}, \quad I_{hist} = i_n + G_{eq}v_n$$

**电容元件**:
$$G_{eq} = \frac{2C}{\Delta t}, \quad I_{hist} = -i_n - G_{eq}v_n$$

## 电感伴随电路

### 梯形法

**离散方程**:
$$i_{n+1} = i_n + \frac{\Delta t}{2L}(v_{n+1} + v_n)$$

**整理**:
$$i_{n+1} = \frac{\Delta t}{2L}v_{n+1} + \left(i_n + \frac{\Delta t}{2L}v_n\right)$$

**等效参数**:
- 等效电导: $G_{eq} = \frac{\Delta t}{2L}$
- 历史电流源: $I_{hist} = i_n + G_{eq}v_n$

**等效电路**:
```
         Geq
    ┌────/\/\/\────┐
    │              │
   (+)            (+)
    v            Ihist
   (-)            (-)
    │              │
    └──────────────┘
```

### 后向欧拉法

**离散方程**:
$$i_{n+1} = i_n + \frac{\Delta t}{L}v_{n+1}$$

**等效参数**:
- 等效电导: $G_{eq} = \frac{\Delta t}{L}$
- 历史电流源: $I_{hist} = i_n$

### 前向欧拉法

**离散方程**:
$$i_{n+1} = i_n + \frac{\Delta t}{L}v_n$$

**特点**:
- 显式计算
- 条件稳定
- 不用于EMTP

## 电容伴随电路

### 梯形法

**微分方程**:
$$i = C\frac{dv}{dt}$$

**离散方程**:
$$i_{n+1} = \frac{2C}{\Delta t}(v_{n+1} - v_n) - i_n$$

**整理**:
$$i_{n+1} = \frac{2C}{\Delta t}v_{n+1} - \left(\frac{2C}{\Delta t}v_n + i_n\right)$$

**等效参数**:
- 等效电导: $G_{eq} = \frac{2C}{\Delta t}$
- 历史电流源: $I_{hist} = -\left(\frac{2C}{\Delta t}v_n + i_n\right)$

### 后向欧拉法

**离散方程**:
$$i_{n+1} = \frac{C}{\Delta t}(v_{n+1} - v_n)$$

**等效参数**:
- 等效电导: $G_{eq} = \frac{C}{\Delta t}$
- 历史电流源: $I_{hist} = -\frac{C}{\Delta t}v_n$

## 电阻伴随电路

**纯电阻**:
$$i = Gv$$

**特点**:
- 无时变特性
- 无需离散化
- $G_{eq} = G$, $I_{hist} = 0$

## 节点导纳方程

### 网络构建

**每个元件贡献**:
- 电导矩阵G: $G_{eq}$连接到节点
- 电流向量I: $I_{hist}$注入节点

**节点方程**:
$$[G_{n}][V_{n}] = [I_{s}] + [I_{hist}]$$

其中:
- $[G_n]$: 节点电导矩阵(n×n)
- $[V_n]$: 节点电压向量(n×1)
- $[I_s]$: 外部电流源(n×1)
- $[I_{hist}]$: 历史电流源(n×1)

### 矩阵结构

**电感贡献**:
$$G_{ii} += \frac{\Delta t}{2L}, \quad G_{jj} += \frac{\Delta t}{2L}, \quad G_{ij} = G_{ji} -= \frac{\Delta t}{2L}$$

**电容贡献**:
$$G_{ii} += \frac{2C}{\Delta t}, \quad G_{jj} += \frac{2C}{\Delta t}, \quad G_{ij} = G_{ji} -= \frac{2C}{\Delta t}$$

**电流源贡献**:
$$I_i += I_{hist}, \quad I_j -= I_{hist}$$

## 时步推进

### 计算流程

```
1. 初始化(t=0)
   ├─ 计算初始条件
   ├─ 设置初始历史源
   └─ 构建初始导纳矩阵

2. 每个时步循环
   a. 构建历史电流源向量
      ├─ 读取上一时步v_n, i_n
      ├─ 计算各元件I_hist
      └─ 组装I_hist向量
      
   b. 求解节点电压
      ├─ 解方程 G_n * V_n = I_total
      └─ 得到V_{n+1}
      
   c. 更新支路电流
      ├─ 对每个动态元件
      ├─ i_{n+1} = G_eq * v_{n+1} + I_hist
      └─ 保存i_{n+1}, v_{n+1}
      
   d. 更新时间
      └─ t = t + Δt
      
   e. 检查事件
      └─ 开关动作、故障等
```

### 数值稳定性

**梯形法**:
- A-稳定
- 二阶精度
- 数值振荡问题

**后向欧拉**:
- L-稳定
- 一阶精度
- 数值阻尼大

**Critical Damping Adjustment(CDA)**:
- 抑制梯形法振荡
- 后向欧拉替换

## 开关处理

### 理想开关

**闭合**:
- 小电阻: $R_{on} = 0.001 \Omega$
- 等效电导: $G_{eq} = 1000$ S

**断开**:
- 大电阻: $R_{off} = 10^6 \Omega$
- 等效电导: $G_{eq} = 10^{-6}$ S

### 开关时刻插值

**问题**:
- 开关不在时间网格点上
- 需要精确确定时刻

**线性插值**:
$$t_{sw} = t_n - v(t_n)\frac{t_{n+1} - t_n}{v(t_{n+1}) - v(t_n)}$$

**重初始化**:
- 插值回退
- 重新计算
- 继续仿真

## 多相系统

### 三相模型

**相域表示**:
$$\begin{bmatrix} G_{aa} & G_{ab} & G_{ac} \\ G_{ba} & G_{bb} & G_{bc} \\ G_{ca} & G_{cb} & G_{cc} \end{bmatrix}\begin{bmatrix} V_a \\ V_b \\ V_c \end{bmatrix} = \begin{bmatrix} I_a \\ I_b \\ I_c \end{bmatrix}$$

**互耦处理**:
- 互电感: 相应位置耦合
- 互电容: 等效处理

## 分布式参数线路

### Bergeron模型

**无损线**:
$$i_k(t) = \frac{1}{Z_c}v_k(t) + I_k(t-\tau)$$

**历史电流**:
$$I_k(t-\tau) = -\frac{1}{Z_c}v_m(t-\tau) - i_m(t-\tau)$$

**等效**:
- 等效电导: $G_{eq} = 1/Z_c$
- 历史电流: $I_k(t-\tau)$

### 频率相关线路

**卷积形式**:
$$i(t) = \int_{0}^{t}y(t-\tau)v(\tau)d\tau$$

**伴随近似**:
- 状态空间实现
- 历史电流计算

## 非线性元件

### 非线性电阻

**迭代求解**:
$$G_{eq}^{(k)} = \frac{di}{dv}\bigg|_{v^{(k)}}$$
$$I_{hist}^{(k)} = i(v^{(k)}) - G_{eq}^{(k)}v^{(k)}$$

**牛顿法**:
- 雅可比矩阵包含$G_{eq}$
- 迭代直到收敛

### 非线性电感

**磁化特性**:
$$i = f(\psi)$$

**离散化**:
$$\psi_{n+1} = \psi_n + \frac{\Delta t}{2}(v_{n+1} + v_n)$$
$$i_{n+1} = f(\psi_{n+1})$$

## 数值振荡

### 梯形法振荡

**原因**:
- 突变量(开关、故障)
- 梯形法非L稳定
- 理想化模型

**表现**:
- 2Δt周期振荡
- 幅值不衰减

**CDA方法**:
- 检测突变量
- 后向欧拉两步
- 消除振荡

### 抑制方法

**方法对比**:

| 方法 | 稳定性 | 精度 | 适用 |
|-----|-------|------|------|
| 梯形 | A-稳定 | 二阶 | 正常仿真 |
| 后向欧拉 | L-稳定 | 一阶 | 开关时刻 |
| CDA | L-稳定 | 混合 | 振荡抑制 |

## 稀疏技术

### 稀疏矩阵

**特点**:
- 大型系统稀疏度>99%
- 稀疏存储格式

**求解**:
- 稀疏LU分解
- 前代回代

### 重排序

**目的**:
- 减少填充
- 保持稀疏

**算法**:
- AMD (Approximate Minimum Degree)
- METIS

## 软件实现

### EMTP

**算法**:
- 标准伴随电路
- CDA振荡抑制
- 变步长

### PSCAD
n- 电导矩阵方法
- 插值开关
- 并行求解

### MATLAB/Simulink

**Power System Blockset**:
- 状态空间方法
- 可选伴随电路

## 优缺点

### 优点

**统一框架**:
- 所有元件统一处理
- 节点电压法求解
- 便于实现

**数值稳定**:
- 隐式方法
- 适合刚性系统
- 大步长可行

### 缺点

**数值振荡**:
- 梯形法固有
- 需CDA处理

**计算量**:
- 每步矩阵求解
- 大型系统挑战

## 相关主题
- [[nodal-analysis]] - 节点分析
- [[numerical-integration]] - 数值积分
- [[discretization-methods]] - 离散化方法
- [[emt-mathematical-foundation]] - EMT数学基础

## 来源论文

参见 [[index.md]] 获取更多伴随电路相关文献。
