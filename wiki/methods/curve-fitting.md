---
title: "曲线拟合 (Curve Fitting)"
type: method
tags: [curve-fitting, parameter-estimation, optimization, least-squares, nonlinear-fitting]
created: "2026-05-04"
---

# 曲线拟合 (Curve Fitting)

## 定义与边界

曲线拟合是通过数学函数近似描述离散数据点间关系的方法，目标是找到最佳参数使拟合函数与实测数据之间的误差最小。在EMT仿真中，曲线拟合用于从测量数据提取设备参数、频率响应的有理函数逼近、以及实验数据的数学建模。

**边界限定**：本页面聚焦于曲线拟合的数值方法，不包括统计回归分析的推断理论。

## EMT中的作用

曲线拟合是参数辨识和模型构建的核心工具：

- **频变参数拟合**：从频率扫描数据提取有理函数模型
- **饱和特性拟合**：变压器磁化曲线的数学表示
- **电弧特性拟合**：断路器电弧的V-I特性建模
- **实验数据处理**：测量数据的平滑和插值

## 主要分支与机制

### 1. 线性拟合

**多项式拟合**：
$$y = a_0 + a_1x + a_2x^2 + ... + a_nx^n$$

**最小二乘法**：
$$\min \sum_{i=1}^{N} (y_i - f(x_i))^2$$

### 2. 非线性拟合

**Levenberg-Marquardt算法**：
结合梯度下降和高斯-牛顿法的迭代优化。

**信赖域方法**：
在局部区域内近似目标函数。

### 3. EMT专用拟合

**反正切函数（变压器饱和）**：
$$i = a \cdot \arctan(b\phi) + c\phi$$

**Frolich方程**：
$$B = \frac{H}{a + b|H|}$$

**有理函数（矢量拟合）**：
$$H(s) = \sum_{k=1}^{n}\frac{r_k}{s-p_k} + d + se$$

## 形式化表达

### 最小二乘问题

目标函数：
$$J(\mathbf{\theta}) = \sum_{i=1}^{N} w_i (y_i - f(x_i, \mathbf{\theta}))^2$$

正规方程：
$$\mathbf{A}^T\mathbf{A}\mathbf{\theta} = \mathbf{A}^T\mathbf{y}$$

### 非线性优化

高斯-牛顿迭代：
$$\mathbf{\theta}_{k+1} = \mathbf{\theta}_k + (\mathbf{J}^T\mathbf{J})^{-1}\mathbf{J}^T\mathbf{r}$$

其中$\mathbf{J}$为雅可比矩阵，$\mathbf{r}$为残差向量。

## 适用边界与失败模式

### 适用条件

- 数据质量良好（噪声可控）
- 模型形式适当
- 参数可辨识
- 样本量充足

### 失效边界

- **过拟合**：模型过于复杂
- **欠拟合**：模型过于简单
- **病态问题**：参数高度相关
- **局部极小**：非凸优化问题

## 与相关页面的关系

- [[vector-fitting]] - 矢量拟合（有理函数拟合）
- [[parameter-identification]] - 参数辨识方法
- [[transmission-line-model]] - 输电线路模型（频变参数拟合）
- [[transformer-model]] - 变压器模型（饱和特性拟合）
- [[least-squares]] - 最小二乘法
- [[numerical-integration]] - 数值积分
- [[optimization-methods]] - 优化方法
- [[wideband-modeling]] - 宽频建模
- [[numerical-integration]] - 数值积分方法
- [[state-space-method]] - 状态空间法

## 代表性来源

- Press, W.H., et al., "Numerical Recipes," *Cambridge*, 2007.
- [[least-squares]] - 最小二乘法
- [[vector-fitting]] - 矢量拟合

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
