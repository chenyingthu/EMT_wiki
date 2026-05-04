---
title: "戴维南等效 (Thevenin Equivalent)"
type: method
tags: [thevenin, equivalent, voltage-source, impedance, network, circuit-theory]
created: "2026-05-02"
---

# 戴维南等效 (Thevenin Equivalent)

## 概述

戴维南等效(Thevenin Equivalent)是电路分析中最基本、最重要的方法之一，由法国工程师Léon Charles Thévenin于1883年提出。该方法指出：任何线性含源二端网络，对外电路可等效为一个电压源串联阻抗的电路。戴维南等效大大简化了复杂电路的分析计算，是电力系统短路计算、稳定性分析、保护整定和网络等值的基础工具。在电力系统领域，戴维南等效广泛应用于故障分析、电压稳定性评估、暂态稳定计算和外部系统简化等方面，是电力工程师必须掌握的核心分析技术。

## 基本定理

### 戴维南定理

**定理内容**:
任何由线性电阻、线性受控源和独立源组成的二端网络，对外电路的作用可以用一个电压源 $V_{th}$ 串联一个阻抗 $Z_{th}$ 来等效替代。

**等效电路组成**:
- 等效电压源 $V_{th}$: 端口的开路电压
- 等效阻抗 $Z_{th}$: 所有独立源置零后的端口输入阻抗

**数学表达**:
$$V_{out} = V_{th} - Z_{th} \cdot I_{out}$$

**适用条件**:
- 线性网络
- 两个端子之间
- 外部电路分析

### 与诺顿等效转换

**诺顿等效**:
- 等效电流源 $I_n = V_{th}/Z_{th}$
- 等效导纳 $Y_n = 1/Z_{th}$

**转换关系**:
$$V_{th} = I_n \cdot Z_{th} = \frac{I_n}{Y_n}$$
$$Z_{th} = \frac{V_{th}}{I_n} = \frac{1}{Y_n}$$

**选择原则**:
- 串联电路: 戴维南等效方便
- 并联电路: 诺顿等效方便

## 等效参数计算

### 开路电压计算

**定义**:
$$V_{th} = V_{OC}$$
端口开路时的端电压

**计算方法**:
1. 节点电压法:
$$\mathbf{Y}\mathbf{V} = \mathbf{I}$$
求解目标节点电压

2. 回路电流法:
$$\mathbf{Z}\mathbf{I} = \mathbf{V}$$
求解目标支路电压

3. 叠加定理:
各独立源分别作用，结果叠加

**示例**:
分压电路:
$$V_{th} = V_s \cdot \frac{R_2}{R_1 + R_2}$$

### 等效阻抗计算

**方法1: 独立源置零法**
- 电压源短路
- 电流源开路
- 计算端口输入阻抗

**方法2: 开路-短路法**:
$$Z_{th} = \frac{V_{OC}}{I_{SC}}$$

**阻抗计算方法**:
1. 串并联化简
2. 星网变换
3. 节点导纳矩阵求逆

**驱动点阻抗**:
$$Z_{th} = Z_{ii}$$
(节点阻抗矩阵对角元素)

**转移阻抗**:
$$Z_{ij} = \frac{V_j}{I_i}$$

## 电力系统应用

### 短路电流计算

**系统等值**:
故障点戴维南等效:
$$I_f = \frac{V_{th}}{Z_{th} + Z_f}$$

**多电源系统**:
各电源贡献叠加:
$$I_f = \sum \frac{V_{thi}}{Z_{thi} + Z_f}$$

**序网等效**:
- 正序等效: $Z_1$
- 负序等效: $Z_2$
- 零序等效: $Z_0$

### 电压稳定性分析

**负荷母线等效**:
从负荷母线看入的系统戴维南等效:
$$V_L = V_{th} - Z_{th}I_L$$

**PV曲线**:
$$V_L = \frac{V_{th}}{2} \pm \sqrt{\left(\frac{V_{th}}{2}\right)^2 - P_L Z_{th}}$$

**最大功率**:
$$P_{max} = \frac{V_{th}^2}{4Z_{th}}$$

**电压稳定裕度**:
$$K_V = \frac{V_{th} - V_L}{V_{th}} \times 100\%$$

### 暂态稳定分析

**发电机外特性**:
暂态电势和暂态电抗:
$$E' = V + jX_d'I$$

**系统等值**:
多机系统简化为单机对无穷大母线:
$$E_{eq} = E' \frac{Z_{load}}{Z_{load} + Z_{line}}$$

**稳定裕度**:
基于等效电路的功率传输极限:
$$P_{max} = \frac{E'V}{X_{eq}}$$

### 保护整定

**距离保护**:
测量阻抗:
$$Z_m = Z_{line} \cdot l_f + Z_{fault}$$

**整定配合**:
基于等效阻抗的阶梯式配合:
$$Z_{set} = K_{rel} \cdot Z_{th}$$

**故障定位**:
$$d = \frac{Z_m - Z_{fault}}{Z_{line}}$$

### 网络等值

**Ward等值**:
$$\mathbf{Y}_{eq} = \mathbf{Y}_{RR} - \mathbf{Y}_{RE}\mathbf{Y}_{EE}^{-1}\mathbf{Y}_{ER}$$

**外部系统等值**:
- 保留研究区域
- 外部系统戴维南等效
- 边界点处理

## 频变戴维南等效

### 宽频等效

**频变阻抗**:
$$Z_{th}(s) = \sum_{k=1}^{N}\frac{R_k}{s-p_k} + D + sE$$

**有理函数近似**:
基于矢量拟合的频域响应拟合

**应用**:
- 雷电暂态分析
- 开关过电压
- 谐波分析
- 宽频稳定性

### 时域实现

**状态空间模型**:
$$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}$$
$$\mathbf{y} = \mathbf{C}\mathbf{x} + \mathbf{D}\mathbf{u}$$

**电路实现**:
- R-L网络
- 伴随电路
- 递归卷积

## 多端口等效

### 多端口戴维南等效

**阻抗矩阵形式**:
$$\begin{bmatrix} V_1 \\ V_2 \\ \vdots \\ V_n \end{bmatrix} = \begin{bmatrix} Z_{11} & Z_{12} & \cdots & Z_{1n} \\ Z_{21} & Z_{22} & \cdots & Z_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ Z_{n1} & Z_{n2} & \cdots & Z_{nn} \end{bmatrix} \begin{bmatrix} I_1 \\ I_2 \\ \vdots \\ I_n \end{bmatrix} + \begin{bmatrix} V_{th1} \\ V_{th2} \\ \vdots \\ V_{thn} \end{bmatrix}$$

**导纳矩阵形式**:
$$\mathbf{I} = \mathbf{Y}\mathbf{V} + \mathbf{I}_{N}$$

**混合参数形式**:
$$\begin{bmatrix} \mathbf{V}_1 \\ \mathbf{I}_2 \end{bmatrix} = \begin{bmatrix} \mathbf{H}_{11} & \mathbf{H}_{12} \\ \mathbf{H}_{21} & \mathbf{H}_{22} \end{bmatrix} \begin{bmatrix} \mathbf{I}_1 \\ \mathbf{V}_2 \end{bmatrix} + \begin{bmatrix} \mathbf{V}_{th} \\ \mathbf{I}_{N} \end{bmatrix}$$

### 应用

**多端口网络等值**:
- 外部系统简化
- 子系统互联
- 宽频等效

## 计算实例

### 简单电路

**分压电路**:
- $V_s = 10$ V
- $R_1 = 2$ Ω, $R_2 = 3$ Ω

**戴维南等效**:
$$V_{th} = 10 \times \frac{3}{2+3} = 6 \text{ V}$$
$$Z_{th} = 2 \parallel 3 = 1.2 \text{ Ω}$$

**验证**:
开路电压: 6 V
短路电流: 5 A
$$Z_{th} = 6/5 = 1.2 \text{ Ω}$$

### 电力系统

**系统等值**:
- 发电机: $E = 1.0$ p.u., $X_d'' = 0.2$ p.u.
- 变压器: $X_T = 0.1$ p.u.
- 线路: $Z_L = 0.1 + j0.5$ p.u.

**戴维南等效**:
$$V_{th} = 1.0 \angle 0° \text{ p.u.}$$
$$Z_{th} = j0.2 + j0.1 + 0.1 + j0.5 = 0.1 + j0.8 \text{ p.u.}$$

**三相短路**:
$$I_f = \frac{1.0}{0.1 + j0.8} = 1.24 \angle -82.9° \text{ p.u.}$$

## 软件实现

### 仿真软件

**MATLAB**:
- 符号计算
- Simulink建模
- 控制系统工具箱

**EMTP/ATP**:
- Thevenin等效计算
- 故障分析
- 网络等值

**DIgSILENT**:
- 网络简化
- 短路计算
- 稳定分析

### 计算流程

**预处理**:
1. 网络拓扑分析
2. 节点编号优化
3. 形成导纳矩阵

**等值计算**:
1. 指定端口
2. 计算开路电压
3. 计算等效阻抗
4. 生成等效电路

**后处理**:
1. 验证精度
2. 误差分析
3. 模型输出

## 相关方法
- [[norton-equivalent]] - 诺顿等效
- [[equivalent-circuit-method]] - 等效电路法
- [[network-equivalent]] - 网络等值
- `superposition-theorem` - 叠加原理

## 来源论文

参见 [[index.md]] 获取更多戴维南等效相关文献。
