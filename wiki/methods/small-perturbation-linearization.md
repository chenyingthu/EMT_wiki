---
title: "小扰动线性化 (Small-Perturbation Linearization)"
type: method
tags: [linearization, small-signal, perturbation, jacobian, stability, eigenvalue]
created: "2026-05-02"
---

# 小扰动线性化 (Small-Perturbation Linearization)

## 概述

小扰动线性化(Small-Perturbation Linearization)是在系统工作点附近对非线性模型进行一阶泰勒展开，获得线性化近似模型的方法。该方法是电力系统小信号稳定性分析的基础，通过线性化可将复杂的非线性微分方程组转化为线性状态空间形式，便于应用特征值分析、频域方法和控制器设计技术。小扰动线性化假设扰动足够小，使得系统在工作点附近的行为可用线性模型准确描述。

## 数学原理

### 泰勒展开

**一阶近似**:
$$f(x) \approx f(x_0) + \frac{\partial f}{\partial x}\bigg|_{x_0}(x - x_0)$$

**多变量形式**:
$$f_i(x_1, ..., x_n) \approx f_i(x_0) + \sum_{j=1}^{n}\frac{\partial f_i}{\partial x_j}\bigg|_{x_0}\Delta x_j$$

**向量形式**:
$$\mathbf{f}(\mathbf{x}) \approx \mathbf{f}(\mathbf{x}_0) + J(\mathbf{x}_0)\Delta\mathbf{x}$$

**雅可比矩阵**:
$$J = \begin{bmatrix} 
\frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n} \\
\vdots & \ddots & \vdots \\
\frac{\partial f_n}{\partial x_1} & \cdots & \frac{\partial f_n}{\partial x_n}
\end{bmatrix}$$

### 状态空间线性化

**非线性系统**:
$$\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \mathbf{u})$$
$$\mathbf{y} = \mathbf{g}(\mathbf{x}, \mathbf{u})$$

**平衡点**:
$$\mathbf{f}(\mathbf{x}_0, \mathbf{u}_0) = 0$$

**线性化**:
$$\Delta\dot{\mathbf{x}} = A\Delta\mathbf{x} + B\Delta\mathbf{u}$$
$$\Delta\mathbf{y} = C\Delta\mathbf{x} + D\Delta\mathbf{u}$$

**系统矩阵**:
$$A = \frac{\partial \mathbf{f}}{\partial \mathbf{x}}\bigg|_{(\mathbf{x}_0, \mathbf{u}_0)}, \quad
B = \frac{\partial \mathbf{f}}{\partial \mathbf{u}}\bigg|_{(\mathbf{x}_0, \mathbf{u}_0)}$$

$$C = \frac{\partial \mathbf{g}}{\partial \mathbf{x}}\bigg|_{(\mathbf{x}_0, \mathbf{u}_0)}, \quad
D = \frac{\partial \mathbf{g}}{\partial \mathbf{u}}\bigg|_{(\mathbf{x}_0, \mathbf{u}_0)}$$

## 电力系统应用

### 同步发电机

**非线性方程**:
$$\begin{cases}
\dot{\delta} = \omega - \omega_0 \\
M\dot{\omega} = P_m - P_e - D(\omega - \omega_0)
\end{cases}$$

**电磁功率**:
$$P_e = \frac{E'V}{X'}\sin\delta$$

**线性化**:
$$\begin{bmatrix} \Delta\dot{\delta} \\ \Delta\dot{\omega} \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -\frac{K_1}{M} & -\frac{D}{M} \end{bmatrix}\begin{bmatrix} \Delta\delta \\ \Delta\omega \end{bmatrix}$$

**其中**:
$$K_1 = \frac{\partial P_e}{\partial \delta}\bigg|_{\delta_0} = \frac{E'V}{X'}\cos\delta_0$$

### 励磁系统

**AVR传递函数**:
$$\frac{d\Delta E_{fd}}{dt} = -\frac{1}{T_A}\Delta E_{fd} + \frac{K_A}{T_A}\Delta V_{err}$$

**线性化**:
$$\Delta V_{err} = \Delta V_{ref} - \frac{\partial V_t}{\partial E_q'}\Delta E_q' - \frac{\partial V_t}{\partial \delta}\Delta\delta$$

**系数**:
$$K_5 = -\frac{\partial V_t}{\partial \delta}, \quad K_6 = \frac{\partial V_t}{\partial E_q'}$$

### 多机系统

**扩展状态向量**:
$$\mathbf{x} = [\delta_1, \omega_1, E_{q1}', ..., \delta_n, \omega_n, E_{qn}']^T$$

**功率偏差**:
$$\Delta P_{ei} = \sum_{j=1}^{n}\frac{\partial P_{ei}}{\partial \delta_j}\Delta\delta_j + \sum_{j=1}^{n}\frac{\partial P_{ei}}{\partial E_{qj}'}\Delta E_{qj}'$$

**同步转矩系数**:
$$K_{S,ij} = \frac{\partial P_{ei}}{\partial \delta_j}$$

## 线性化步骤

```
1. 确定平衡点
   ├─ 求解f(x0, u0) = 0
   ├─ 潮流计算
   └─ 验证稳定性

2. 计算雅可比矩阵
   ├─ 解析求导(如可能)
   ├─ 或数值差分
   └─ 验证矩阵结构

3. 形成状态矩阵
   ├─ A = ∂f/∂x
   ├─ B = ∂f/∂u
   ├─ C = ∂g/∂x
   └─ D = ∂g/∂u

4. 分析线性模型
   ├─ 特征值分析
   ├─ 模态分析
   ├─ 频域响应
   └─ 控制器设计

5. 验证有效性
   ├─ 扰动幅度检查
   ├─ 线性响应验证
   └─ 误差评估
```

## 数值线性化

### 差分近似

**前向差分**:
$$\frac{\partial f}{\partial x_j} \approx \frac{f(x_0 + \epsilon_j) - f(x_0)}{\epsilon}$$

**中心差分**:
$$\frac{\partial f}{\partial x_j} \approx \frac{f(x_0 + \epsilon_j) - f(x_0 - \epsilon_j)}{2\epsilon}$$

**步长选择**:
$$\epsilon = \sqrt{\epsilon_{mach}}|x_j|$$

### 符号线性化

**自动微分**:
- 前向模式
- 反向模式
- 精确导数计算

**工具**:
- Modelica
- CasADi
- AutoDiff库

## 稳定性分析

### 特征值分析

**特征方程**:
$$\det(A - \lambda I) = 0$$

**稳定判据**:
- 稳定: $Re(\lambda_i) < 0, \forall i$
- 临界: $Re(\lambda_i) \leq 0$，存在$=0$
- 不稳定: $\exists Re(\lambda_i) > 0$

### 模态特性

**阻尼比**:
$$\zeta_i = \frac{-Re(\lambda_i)}{|\lambda_i|}$$

**振荡频率**:
$$f_i = \frac{Im(\lambda_i)}{2\pi}$$

**模态判据**:
- 良好阻尼: $\zeta > 0.05$
- 可接受: $\zeta > 0.03$
- 弱阻尼: $\zeta < 0.03$

## 灵敏度分析

### 参数灵敏度

**特征值灵敏度**:
$$\frac{\partial \lambda_i}{\partial p} = \mathbf{w}_i^T\frac{\partial A}{\partial p}\mathbf{v}_i$$

**参与因子**:
$$p_{ki} = v_{ki}w_{ki}$$

**应用**:
- 参数优化
- 控制器设计
- 关键参数识别

## 线性化误差

### 线性化区域

**有效范围**:
- 线性度: 通常$\pm 10°$功角
- 电压: $\pm 10\%$额定值

**误差估计**:
$$\|f(x) - f_{lin}(x)\| \approx \frac{1}{2}\|H\|\|\Delta x\|^2$$

### 大扰动限制

**非线性效应**:
- 饱和
- 限幅
- 开关动作

**失效场景**:
- 大故障
- 失步
- 电压崩溃

## 与潮流的关系

### 初始条件

**潮流结果**:
- 节点电压$V, \theta$
- 发电机出力$P, Q$
- 负荷消耗

**状态初始化**:
- 功角$\delta_0$
- 转速$\omega_0 = 1$
- 暂态电势$E_{q0}'$

### 连续潮流

**分岔分析**:
- 鞍结分岔
- Hopf分岔
- 稳定边界

## 软件工具

### MATLAB
- `linearize`: Simulink线性化
- `linmod`: 连续系统
- `dlinmod`: 离散系统

### Python
- `control`: 控制系统
- `sympy`: 符号微分
- `numdifftools`: 数值微分

### 电力系统专用
- PSAT: 小信号分析
- SSAT: 稳定分析
- PacDyn: 动态分析

## 相关主题
- [[state-space-method]] - 状态空间法
- [[generalized-eigenvalue-method]] - 广义特征根法
- [[small-signal-analysis]] - 小信号分析
- [[modal-analysis]] - 模态分析

## 来源论文

参见 [[index.md]] 获取更多小扰动线性化相关文献。
