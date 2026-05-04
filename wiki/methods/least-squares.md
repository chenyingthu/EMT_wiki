---
title: "最小二乘法 (Least Squares Method)"
type: method
tags: [least-squares, parameter-estimation, curve-fitting, system-identification, numerical-methods]
created: "2026-05-04"
---

# 最小二乘法 (Least Squares Method)

## 定义与边界

最小二乘法是一种通过最小化观测值与模型预测值之间误差平方和来估计模型参数的优化方法。该方法通过求解正规方程或采用迭代优化算法，获得使残差平方和最小的参数估计值。

在电力系统分析中，最小二乘法主要应用于：
- 频变参数模型的有理函数拟合（如矢量拟合）
- 系统辨识与参数估计
- 测量数据拟合与去噪
- 状态估计中的不良数据检测

**边界限定**：本方法假设测量误差服从高斯分布且相互独立，对异常值敏感。

## EMT中的作用

最小二乘法是频变建模和系统辨识的核心数学工具：

- **参数辨识**：从频域测量数据提取等效电路参数
- **有理拟合**：将频变特性拟合为有理函数形式（极点-留数）
- **数据平滑**：滤除测量噪声，提取信号趋势
- **模型降阶**：在保证精度的前提下简化模型阶数

## 主要分支与机制

### 1. 线性最小二乘

模型对待估参数为线性关系：
$$\mathbf{y} = \mathbf{A}\mathbf{x} + \mathbf{e}$$

解析解通过正规方程获得：
$$\mathbf{x}_{LS} = (\mathbf{A}^T\mathbf{A})^{-1}\mathbf{A}^T\mathbf{y}$$

适用于多项式拟合、线性回归等问题。

### 2. 加权最小二乘

考虑不同测量点的可信度差异：
$$\min J = \sum_{i=1}^{n} w_i (y_i - f(x_i, \theta))^2$$

权重通常取测量方差的倒数：$w_i = 1/\sigma_i^2$。

### 3. 非线性最小二乘

模型对参数为非线性关系，需迭代求解：
$$\min J = \|\mathbf{y} - \mathbf{f}(\mathbf{x}, \boldsymbol{\theta})\|^2$$

常用Gauss-Newton或Levenberg-Marquardt算法。

## 形式化表达

### 线性最小二乘问题

给定 $m$ 个观测数据 $(x_i, y_i)$，建立 $n$ 参数模型 $(n < m)$：

$$y_i = \sum_{j=1}^{n} a_j \phi_j(x_i) + e_i, \quad i = 1, ..., m$$

其中 $\phi_j(x)$ 为基函数。

矩阵形式：
$$\mathbf{y} = \mathbf{A}\mathbf{x} + \mathbf{e}$$

目标函数（残差平方和）：
$$J(\mathbf{x}) = \|\mathbf{e}\|^2 = \|\mathbf{y} - \mathbf{A}\mathbf{x}\|^2 = (\mathbf{y} - \mathbf{A}\mathbf{x})^T(\mathbf{y} - \mathbf{A}\mathbf{x})$$

最优解满足正规方程：
$$\mathbf{A}^T\mathbf{A}\mathbf{x} = \mathbf{A}^T\mathbf{y}$$

解为：
$$\hat{\mathbf{x}} = (\mathbf{A}^T\mathbf{A})^{-1}\mathbf{A}^T\mathbf{y} = \mathbf{A}^+\mathbf{y}$$

其中 $\mathbf{A}^+ = (\mathbf{A}^T\mathbf{A})^{-1}\mathbf{A}^T$ 为Moore-Penrose伪逆。

### 频率响应拟合

将频变导纳 $Y(s)$ 拟合为有理函数：
$$Y(s) \approx \sum_{k=1}^{n} \frac{r_k}{s - p_k} + d + se$$

对于 $N$ 个频率点 $s_j = j\omega_j$，建立误差函数：
$$\min \sum_{j=1}^{N} w_j |Y(j\omega_j) - Y_{fit}(j\omega_j)|^2$$

### 数值稳定性

直接求解正规方程可能因条件数平方而数值不稳定：
$$\kappa(\mathbf{A}^T\mathbf{A}) = \kappa(\mathbf{A})^2$$

改进方法：
- **QR分解**：$\mathbf{A} = \mathbf{QR}$，解 $\mathbf{R}\mathbf{x} = \mathbf{Q}^T\mathbf{y}$
- **SVD分解**：$\mathbf{A} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^T$，$\hat{\mathbf{x}} = \mathbf{V}\mathbf{\Sigma}^+\mathbf{U}^T\mathbf{y}$

## 适用边界与失败模式

### 适用条件

| 条件 | 要求 | 说明 |
|------|------|------|
| 误差分布 | 近似高斯 | 保证BLUE性质 |
| 样本量 | $m > n$ | 超定系统 |
| 独立性 | 观测不相关 | 协方差矩阵对角 |
| 满秩 | $rank(\mathbf{A}) = n$ | 参数可辨识 |

### 失效边界

- **异常值敏感**：单个粗大误差可显著影响拟合结果
- **多重共线性**：自变量高度相关导致 $(\mathbf{A}^T\mathbf{A})^{-1}$ 病态
- **异方差性**：误差方差非恒定导致估计非有效
- **自相关**：时序数据残差自相关违反独立性假设

### 关键假设

1. 模型形式正确（无模型误差）
2. 解释变量测量无误差（仅因变量含噪声）
3. 误差均值为零、方差恒定、相互独立
4. 样本量充分（$m \gg n$）

## 代表性来源

### 经典文献

- Lawson, C.L. and Hanson, R.J., "Solving Least Squares Problems," *SIAM*, 1995. - 最小二乘数值方法经典著作
- Golub, G.H. and Van Loan, C.F., "Matrix Computations," *JHU Press*, 2013. - 矩阵计算与最小二乘

### 电力应用

- [[vector-fitting]] - 基于最小二乘的矢量拟合
- [[parameter-identification]] - 参数辨识方法
- [[frequency-dependent-modeling]] - 频变建模

### 数值方法

- [[numerical-integration]] - 数值积分
- [[modal-analysis]] - 模态分析中的拟合
- [[system-identification]] - 系统辨识

## 与相关页面的关系

- [[vector-fitting]] - 频变特性拟合的核心算法
- [[parameter-identification]] - 系统参数辨识
- [[frequency-dependent-modeling]] - 频变建模应用
- [[curve-fitting]] - 曲线拟合方法
- [[svd]] - SVD分解求解
- [[qr-decomposition]] - QR分解求解

## 开放问题

- 电力系统大数据环境下的分布式最小二乘
- 含约束条件的结构化最小二乘（如极点稳定性约束）
- 自适应遗忘因子的递推最小二乘
- 鲁棒最小二乘（对异常值不敏感）

## 参考标准

- IEEE Std. 1057 - 波形记录器测试
- IEC 61000-4-30 - 电能质量测量

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。如有更新或修正，请参考最新研究进展。*
