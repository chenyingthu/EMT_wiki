---
title: "最小二乘法 (Least Squares Method)"
type: method
tags: [least-squares, parameter-estimation, curve-fitting, optimization, system-identification]
created: "2026-05-02"
---

# 最小二乘法 (Least Squares Method)

## 概述

最小二乘法是一种优化方法，通过最小化误差平方和来拟合数据或估计参数。在电力系统EMT仿真中，最小二乘法广泛应用于系统辨识、参数估计、曲线拟合、模型降阶和谐波分析等领域。

该方法由高斯于1795年提出，其核心思想是找到使观测值与模型预测值之间误差平方和最小的参数估计。在电力系统应用中，最小二乘法特别适用于处理含有测量噪声的PMU数据、进行频域响应拟合以及从仿真数据中提取等效模型参数。

## 数学原理

### 基本形式
给定数据点$(x_i, y_i)$，$i=1,2,...,n$，寻找函数$f(x; eta)$使得误差平方和最小：

$$\min_{\beta} S(\beta) = \min_{\beta} \sum_{i=1}^{n} (y_i - f(x_i; \beta))^2$$

其中$\beta$为待估计的参数向量。该优化问题可通过令梯度为零来求解：

$$\nabla_{\beta} S(\beta) = -2\sum_{i=1}^{n}(y_i - f(x_i; \beta))\frac{\partial f(x_i; \beta)}{\partial \beta} = 0$$

### 线性最小二乘
对于线性模型 $\mathbf{y} = \mathbf{X}\beta + \mathbf{\epsilon}$，其中$\mathbf{\epsilon}$为误差向量：

$$\hat{\beta} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$$

其中：
- $\mathbf{X}$: 设计矩阵 ($n \times p$)，$n$为样本数，$p$为参数个数
- $\mathbf{y}$: 观测向量 ($n \times 1$)
- $\beta$: 参数向量 ($p \times 1$)
- $\hat{\beta}$: 参数估计值

### 正规方程的详细推导

从误差平方和出发：

$$S(\beta) = (\mathbf{y} - \mathbf{X}\beta)^T(\mathbf{y} - \mathbf{X}\beta) = \mathbf{y}^T\mathbf{y} - 2\beta^T\mathbf{X}^T\mathbf{y} + \beta^T\mathbf{X}^T\mathbf{X}\beta$$

对$\beta$求导并令其为零：

$$\frac{\partial S}{\partial \beta} = -2\mathbf{X}^T\mathbf{y} + 2\mathbf{X}^T\mathbf{X}\beta = 0$$

整理得到正规方程：

$$(\mathbf{X}^T\mathbf{X})\hat{\beta} = \mathbf{X}^T\mathbf{y}$$

当$\mathbf{X}^T\mathbf{X}$可逆时，解为：

$$\hat{\beta} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$$

### 几何解释

最小二乘解具有优雅的几何解释。观测向量$\mathbf{y}$位于$\mathbb{R}^n$空间，设计矩阵$\mathbf{X}$的列张成一个$p$维子空间$\mathcal{C}(\mathbf{X})$。最小二乘估计$\hat{\mathbf{y}} = \mathbf{X}\hat{\beta}$是$\mathbf{y}$在子空间$\mathcal{C}(\mathbf{X})$上的正交投影。

残差向量$\mathbf{r} = \mathbf{y} - \mathbf{X}\hat{\beta}$与$\mathcal{C}(\mathbf{X})$正交，即：

$$\mathbf{X}^T(\mathbf{y} - \mathbf{X}\hat{\beta}) = \mathbf{0}$$

这与正规方程等价。投影矩阵$\mathbf{P} = \mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T$将任意向量投影到$\mathcal{C}(\mathbf{X})$。

### 加权最小二乘

当不同观测具有不同精度或重要性时，引入权重矩阵：

$$\hat{\beta} = (\mathbf{X}^T\mathbf{W}\mathbf{X})^{-1}\mathbf{X}^T\mathbf{W}\mathbf{y}$$

其中$\mathbf{W} = \text{diag}(w_1, w_2, ..., w_n)$为对角权重矩阵。最优权重与误差方差成反比：

$$w_i = \frac{1}{\sigma_i^2}$$

对于相关误差，$\mathbf{W}$为满秩协方差矩阵的逆：

$$\hat{\beta} = (\mathbf{X}^T\mathbf{C}^{-1}\mathbf{X})^{-1}\mathbf{X}^T\mathbf{C}^{-1}\mathbf{y}$$

## 数值解法

### 正规方程法
直接求解正规方程：

$$(\mathbf{X}^T\mathbf{X})\beta = \mathbf{X}^T\mathbf{y}$$

**算法步骤**：
1. 计算$\mathbf{A} = \mathbf{X}^T\mathbf{X}$（对称正定）
2. 计算$\mathbf{b} = \mathbf{X}^T\mathbf{y}$
3. 解线性系统$\mathbf{A}\beta = \mathbf{b}$

**优点**：
- 实现简单
- 计算量相对较小

**缺点**：
- 条件数为原矩阵的平方：$\kappa(\mathbf{X}^T\mathbf{X}) = \kappa(\mathbf{X})^2$
- 数值不稳定，容易受舍入误差影响

### Cholesky分解

对于对称正定矩阵$\mathbf{A} = \mathbf{X}^T\mathbf{X}$，使用Cholesky分解：

$$\mathbf{A} = \mathbf{L}\mathbf{L}^T$$

其中$\mathbf{L}$为下三角矩阵。求解步骤：
1. 计算Cholesky因子$\mathbf{L}$
2. 前向替代解$\mathbf{L}\mathbf{z} = \mathbf{X}^T\mathbf{y}$
3. 后向替代解$\mathbf{L}^T\hat{\beta} = \mathbf{z}$

**复杂度**：$O(np^2 + p^3/3)$
**稳定性**：优于直接求逆，但仍受条件数平方影响

### QR分解

$$\mathbf{X} = \mathbf{QR}$$

其中$\mathbf{Q}$为正交矩阵（$\mathbf{Q}^T\mathbf{Q} = \mathbf{I}$），$\mathbf{R}$为上三角矩阵。

**求解公式**：

$$\hat{\beta} = \mathbf{R}^{-1}\mathbf{Q}^T\mathbf{y}$$

**算法步骤**：
1. 对$\mathbf{X}$进行QR分解（Householder或Givens旋转）
2. 计算$\mathbf{Q}^T\mathbf{y}$
3. 回代求解$\mathbf{R}\hat{\beta} = \mathbf{Q}^T\mathbf{y}$

**数值稳定性**：
- 条件数保持不变
- 显著优于正规方程法
- 适用于病态问题

**复杂度**：$O(2np^2 - 2p^3/3)$

### SVD分解

$$\mathbf{X} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^T$$

其中$\mathbf{U}$、$\mathbf{V}$为正交矩阵，$\mathbf{\Sigma} = \text{diag}(\sigma_1, ..., \sigma_p)$为奇异值矩阵，$\sigma_1 \geq \sigma_2 \geq ... \geq \sigma_p \geq 0$。

**求解公式**：

$$\hat{\beta} = \mathbf{V}\mathbf{\Sigma}^{-1}\mathbf{U}^T\mathbf{y} = \sum_{i=1}^{p} \frac{\mathbf{u}_i^T\mathbf{y}}{\sigma_i}\mathbf{v}_i$$

**算法步骤**：
1. 计算$\mathbf{X}$的SVD分解
2. 计算$\mathbf{U}^T\mathbf{y}$
3. 对每个分量除以对应奇异值
4. 计算$\mathbf{V}$乘以结果

**数值稳定性**：
- 最优稳定性，能处理高度病态问题
- 可识别并处理秩亏缺情况
- 可通过截断小奇异值实现正则化

**复杂度**：$O(2np^2 + 11p^3)$，计算量较大但可靠性最高

## 正则化方法

### 岭回归 (Ridge Regression)

对于病态问题或存在多重共线性时，添加$\ell_2$正则化项：

$$\min_{\beta} \|\mathbf{y} - \mathbf{X}\beta\|_2^2 + \lambda\|\beta\|_2^2$$

**解析解**：

$$\hat{\beta}_{ridge} = (\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I})^{-1}\mathbf{X}^T\mathbf{y}$$

其中$\lambda > 0$为正则化参数。

**性质**：
- 有偏估计，但方差减小
- 总是可解，即使$\mathbf{X}^T\mathbf{X}$奇异
- 收缩系数向零，但不完全为零
- 等价于假设参数服从高斯先验的最大后验估计

**参数选择**：
- 交叉验证
- L曲线准则
- 广义交叉验证(GCV)

### LASSO回归

使用$\ell_1$正则化：

$$\min_{\beta} \|\mathbf{y} - \mathbf{X}\beta\|_2^2 + \lambda\|\beta\|_1$$

其中$\|\beta\|_1 = \sum_{j=1}^{p}|\beta_j|$。

**特点**：
- 产生稀疏解（部分系数精确为零）
- 具有变量选择功能
- 无解析解，需用数值优化（如LARS、ISTA）

**与岭回归比较**：
- LASSO：稀疏解，适合特征选择
- Ridge：收缩解，适合处理共线性

### 弹性网络 (Elastic Net)

结合$\ell_1$和$\ell_2$正则化：

$$\min_{\beta} \|\mathbf{y} - \mathbf{X}\beta\|_2^2 + \lambda_1\|\beta\|_1 + \lambda_2\|\beta\|_2^2$$

兼顾LASSO的稀疏性和岭回归的稳定性。

## 非线性最小二乘

### 问题形式

最小化非线性残差平方和：

$$\min_{\beta} S(\beta) = \sum_{i=1}^{n} r_i(\beta)^2 = \|\mathbf{r}(\beta)\|_2^2$$

其中$r_i(\beta) = y_i - f(x_i; \beta)$为非线性残差。

### 高斯-牛顿法

通过线性化迭代求解。在$\beta_k$处对残差进行一阶Taylor展开：

$$\mathbf{r}(\beta) \approx \mathbf{r}(\beta_k) + \mathbf{J}_k(\beta - \beta_k)$$

其中$\mathbf{J}_k$为雅可比矩阵，$J_{ij} = \frac{\partial r_i}{\partial \beta_j}$。

**迭代公式**：

$$\beta_{k+1} = \beta_k + (\mathbf{J}_k^T\mathbf{J}_k)^{-1}\mathbf{J}_k^T\mathbf{r}(\beta_k)$$

**算法步骤**：
1. 初始化$\beta_0$
2. 计算残差$\mathbf{r}(\beta_k)$和雅可比$\mathbf{J}_k$
3. 求解线性最小二乘：$\mathbf{J}_k\Delta\beta = -\mathbf{r}(\beta_k)$
4. 更新：$\beta_{k+1} = \beta_k + \Delta\beta$
5. 重复直到收敛

**收敛性**：
- 接近最优解时具有二次收敛速度
- 对初值敏感
- 当$\mathbf{J}^T\mathbf{J}$奇异或接近奇异时不稳定

### Levenberg-Marquardt算法

结合高斯-牛顿法和梯度下降的优点：

$$\beta_{k+1} = \beta_k + (\mathbf{J}_k^T\mathbf{J}_k + \lambda_k\mathbf{I})^{-1}\mathbf{J}_k^T\mathbf{r}(\beta_k)$$

**阻尼因子$\lambda_k$的自适应调整**：
- 初始选择较大的$\lambda$
- 若目标函数下降，减小$\lambda$（趋向高斯-牛顿）
- 若目标函数上升，增大$\lambda$（趋向梯度下降）

**算法优势**：
- 全局收敛性好
- 接近最优时保持快速收敛
- 能处理雅可比矩阵秩亏缺情况

**实现变体**：
- 标准LM：$\mathbf{J}^T\mathbf{J} + \lambda\mathbf{I}$
- 缩放LM：$\mathbf{J}^T\mathbf{J} + \lambda\text{diag}(\mathbf{J}^T\mathbf{J})$

### 信赖域方法

限制每一步的步长以确保收敛：

$$\min_{\Delta\beta} \|\mathbf{J}\Delta\beta + \mathbf{r}\|_2^2 \quad \text{s.t.} \quad \|\Delta\beta\| \leq \Delta$$

通过调整信赖域半径$\Delta$来平衡收敛速度和稳定性。

## 递归最小二乘 (Recursive Least Squares)

### 在线更新公式

对于实时应用，当新数据$(x_{n+1}, y_{n+1})$到达时，无需重新计算即可更新估计：

**增益矩阵**：
$$\mathbf{K}_{n+1} = \mathbf{P}_n\mathbf{x}_{n+1}(1 + \mathbf{x}_{n+1}^T\mathbf{P}_n\mathbf{x}_{n+1})^{-1}$$

**参数更新**：
$$\hat{\beta}_{n+1} = \hat{\beta}_n + \mathbf{K}_{n+1}(y_{n+1} - \mathbf{x}_{n+1}^T\hat{\beta}_n)$$

**协方差更新**：
$$\mathbf{P}_{n+1} = (\mathbf{I} - \mathbf{K}_{n+1}\mathbf{x}_{n+1}^T)\mathbf{P}_n$$

其中$\mathbf{P}_n = (\mathbf{X}_n^T\mathbf{X}_n)^{-1}$。

### 带遗忘因子的RLS

给近期数据更高权重：

$$\mathbf{K}_{n+1} = \frac{\mathbf{P}_n\mathbf{x}_{n+1}}{\lambda + \mathbf{x}_{n+1}^T\mathbf{P}_n\mathbf{x}_{n+1}}$$

$$\mathbf{P}_{n+1} = \frac{1}{\lambda}(\mathbf{I} - \mathbf{K}_{n+1}\mathbf{x}_{n+1}^T)\mathbf{P}_n$$

其中$0 < \lambda \leq 1$为遗忘因子，通常取0.95-0.99。

**应用场景**：
- 在线参数估计
- 自适应滤波
- 时变系统辨识

## 电力系统EMT仿真应用

### 在矢量拟合中的应用

[[vector-fitting]]方法使用最小二乘进行频域响应拟合：

**问题设置**：
- 目标：拟合有理函数$H(s) = \sum_{m=1}^{N}\frac{c_m}{s-a_m} + d + se$
- 输入：频域采样点$(s_k, H(s_k))$
- 输出：极点$a_m$、留数$c_m$、直馈项$d,e$

**迭代求解**：
1. 固定极点，线性最小二乘估计留数和直馈项
2. 更新极点（非线性优化）
3. 重复直到收敛

**线性化技巧**：通过引入辅助变量将问题转化为线性最小二乘。

**数值考虑**：
- 使用QR或SVD分解处理病态性
- 正则化防止过拟合
- 约束优化确保稳定性

### 在Prony分析中的应用

[[prony-analysis]]用于从时域响应中提取模态参数：

**模型**：
$$y(k) = \sum_{i=1}^{n} A_i e^{\sigma_i k\Delta t} \cos(2\pi f_i k\Delta t + \phi_i)$$

**求解步骤**：
1. 构建Hankel矩阵
2. 线性预测（AR模型）系数估计 - 最小二乘
3. 求根得到极点（频率和阻尼）
4. 留数估计 - 线性最小二乘

**数值稳定性**：
- 使用TLS（总体最小二乘）处理噪声
- SVD-based Prony提高鲁棒性
- 模型阶数选择（SVD截断）

### 在模型降阶中的应用

[[model-order-reduction]]中的最小二乘应用：

**矩匹配**：
- 计算高阶系统的矩（传递函数Taylor展开系数）
- 最小二乘拟合低阶模型参数以匹配这些矩

**有理逼近**：
- 使用矢量拟合进行频域响应逼近
- 非线性最小二乘优化模型参数

**时域拟合**：
- 比较原始系统与降阶系统的阶跃/脉冲响应
- 最小二乘优化使误差最小

**参数估计**：
- 从EMT仿真数据中提取等效模型参数
- 加权最小二乘处理不同精度数据

### 在线路参数估计中的应用

`line-parameter-estimation`使用PMU测量：

**问题**：估计输电线路的R、L、C、G参数

**方法**：
1. 建立频域或时域测量方程
2. 构造最小二乘问题
3. 加权处理不同测量精度
4. 约束优化确保物理可行性（正参数）

**递归实现**：
- 使用RLS实现在线参数跟踪
- 适应线路温度变化引起的参数变化

### 在谐波分析中的应用

[[harmonic-analysis]]中的最小二乘应用：

**谐波估计模型**：
$$y(t) = \sum_{h=1}^{H} A_h \sin(2\pi h f_0 t + \phi_h) + \epsilon(t)$$

**求解**：
1. 扩展为线性参数形式
2. 最小二乘估计幅值和相位
3. 频率扫描或锁相环确定基频

**间谐波分析**：
- 非均匀采样最小二乘
- 稀疏优化（压缩感知方法）

## 统计推断与置信区间

### 估计量的统计性质

**无偏性**：
$$E[\hat{\beta}] = \beta$$

在误差零均值假设下，最小二乘估计是无偏的。

**协方差矩阵**：
$$\text{Cov}(\hat{\beta}) = \sigma^2(\mathbf{X}^T\mathbf{X})^{-1}$$

其中$\sigma^2$为误差方差，通常用残差估计：
$$\hat{\sigma}^2 = \frac{\|\mathbf{y} - \mathbf{X}\hat{\beta}\|_2^2}{n-p}$$

**有效性**（高斯-马尔可夫定理）：
在线性无偏估计中，最小二乘估计具有最小方差（BLUE - Best Linear Unbiased Estimator）。

### 置信区间

**参数置信区间**：
$$\hat{\beta}_j \pm t_{n-p}^{\alpha/2} \cdot \hat{\sigma}\sqrt{[(\mathbf{X}^T\mathbf{X})^{-1}]_{jj}}$$

其中$t_{n-p}^{\alpha/2}$为t分布临界值。

**预测置信区间**：
对于新观测$\mathbf{x}_*$：
$$\mathbf{x}_*^T\hat{\beta} \pm t_{n-p}^{\alpha/2} \cdot \hat{\sigma}\sqrt{1 + \mathbf{x}_*^T(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{x}_*}$$

### 假设检验

**t检验**（单个参数）：
$$t = \frac{\hat{\beta}_j}{\text{SE}(\hat{\beta}_j)}$$
检验$H_0: \beta_j = 0$

**F检验**（多个参数）：
$$F = \frac{(\text{RSS}_R - \text{RSS}_{UR})/q}{\text{RSS}_{UR}/(n-p)}$$
检验模型显著性

其中RSS为残差平方和，$q$为约束个数。

## 误差分析与病态问题

### 条件数分析

矩阵条件数衡量问题的病态程度：
$$\kappa(\mathbf{X}) = \frac{\sigma_{max}(\mathbf{X})}{\sigma_{min}(\mathbf{X})}$$

**解释**：
- $\kappa \approx 1$：良态问题
- $\kappa \gg 1$：病态问题
- $\kappa > 10^{12}$：数值上秩亏缺

**条件数与误差放大**：
$$\frac{\|\Delta\hat{\beta}\|}{\|\hat{\beta}\|} \leq \kappa(\mathbf{X}) \cdot \frac{\|\Delta\mathbf{y}\|}{\|\|\mathbf{y}\|}$$

### 病态问题处理

**原因**：
- 变量尺度差异大
- 多重共线性
- 多项式高阶拟合

**解决方法**：

1. **变量标准化**：
$$\tilde{x}_{ij} = \frac{x_{ij} - \bar{x}_j}{\sigma_j}$$

2. **正则化**：
   - 岭回归
   - 截断SVD（TSVD）
   - Tikhonov正则化

3. **数值方法选择**：
   - 优先使用QR或SVD
   - 避免正规方程法

### 残差分析

**正态性检验**：
- Q-Q图
- Shapiro-Wilk检验
- Kolmogorov-Smirnov检验

**异方差检测**：
- 残差vs拟合值图
- Breusch-Pagan检验
- White检验

**自相关检验**：
- Durbin-Watson统计量
- 残差自相关图
- Ljung-Box检验

**异常值检测**：
- Cook距离
- 杠杆值
- 学生化残差

## 应用方法

### 多项式拟合
拟合多项式 $y = a_0 + a_1x + ... + a_mx^m$:

- **设计矩阵**: Vandermonde矩阵
$$\mathbf{X} = \begin{bmatrix} 1 & x_1 & x_1^2 & \cdots & x_1^m \\ 1 & x_2 & x_2^2 & \cdots & x_2^m \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_n & x_n^2 & \cdots & x_n^m \end{bmatrix}$$
- **阶数选择**: 使用交叉验证或信息准则(AIC/BIC)避免过拟合
- `polynomial-fitting` - 多项式拟合

### 指数拟合
拟合 $y = ae^{bx}$:
- **线性化**: 对数变换 $\ln y = \ln a + bx$
- **非线性**: 迭代求解，使用非线性最小二乘

### 有理函数拟合
拟合 $y = \frac{a_0 + a_1x + ...}{1 + b_1x + ...}$:
- [[vector-fitting]] - 矢量拟合
- **频域拟合**: 宽频特性
- [[frequency-dependent-modeling]] - 频率相关建模

## 电力系统应用

### 参数估计
- **线路参数**: 基于PMU测量
- `line-parameter-estimation` - 线路参数估计
- **变压器参数**: 短路试验数据
- **负荷模型**: 基于实测数据

### 系统辨识
- **传递函数**: 频域数据拟合
- `system-identification` - 系统辨识
- **状态空间**: 时域数据拟合
- **阶数确定**: 模型复杂度

### 谐波分析
- **FFT+LS**: 傅里叶变换+最小二乘
- [[harmonic-analysis]] - 谐波分析
- **间谐波**: 非整数次谐波
- **频率估计**: 频率偏差校正

## 与优化方法对比

| 方法 | 特点 | 适用场景 |
|------|------|----------|
| 最小二乘 | 解析解、高效 | 线性问题 |
| 梯度下降 | 迭代、通用 | 大规模问题 |
| 遗传算法 | 全局搜索 | 多峰函数 |
| 贝叶斯 | 概率估计 | 不确定性量化 |

## 相关方法
- `parameter-estimation` - 参数估计
- [[review-and-comparison-of-frequency-domain-curve-fitting-techniques-vector-fittin]] - 曲线拟合
- `system-identification` - 系统辨识
- [[numerical-damping-optimization]] - 优化方法
- `svd` - 奇异值分解
- `qr-decomposition` - QR分解
- `levenberg-marquardt` - LM算法
- `uncertainty-analysis` - 不确定性分析

## 软件实现

### MATLAB
- `\`: 反斜杠运算符（自动选择最佳算法）
- `lsqcurvefit`: 非线性曲线拟合
- `regress`: 线性回归
- `ridge`: 岭回归
- `lasso`: LASSO回归
- `lsqlin`: 带约束的线性最小二乘

### Python
- `numpy.linalg.lstsq`: 基础最小二乘
- `scipy.optimize.least_squares`: 非线性最小二乘（含LM算法）
- `sklearn.linear_model.Ridge`: 岭回归
- `sklearn.linear_model.Lasso`: LASSO回归
- `statsmodels.OLS`: 统计推断功能

### R
- `lm`: 线性模型
- `nls`: 非线性最小二乘
- `glmnet`: 正则化回归
- `MASS::lm.ridge`: 岭回归

## 来源论文

参见 [[index.md]] 获取更多最小二乘法相关文献。
