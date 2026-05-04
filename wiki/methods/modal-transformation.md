---
title: "模态变换 (Modal Transformation)"
type: method
tags: [modal, transformation, decoupling, transmission-line, eigenvalue, eigenvector, phase-domain, modal-domain]
created: "2026-05-02"
---

# 模态变换 (Modal Transformation)

## 概述

模态变换(Modal Transformation)是将耦合的多相系统转换为解耦的模态系统的重要数学工具，通过特征值分解实现相间解耦，使各模态可独立分析。该方法在多相输电线路建模、电缆系统分析和EMI研究中广泛应用，能够有效降低计算复杂度并揭示系统的固有特性。

模态变换的核心思想是通过线性变换将耦合的相域方程转换到模域，使得在模域中各模态相互独立，可以分别处理。变换后的每个模态代表系统的一种固有传播模式，具有独立的传播常数、特性阻抗和传播速度。

模态变换包括实变换和复变换两类：
- **实变换**: 变换矩阵元素为实数，便于时域实现，如Clarke变换、Karrenbauer变换
- **复变换**: 变换矩阵元素为复数，通常能实现最优解耦，如对称分量变换、Wedepohl变换

在[[emt-simulation-verification]]仿真中，模态变换是[[transmission-line-model]]和[[cable-model]]的核心数学基础，与[[numerical-integration]]和[[state-space-method]]密切相关。

## 理论基础

### 耦合系统方程

#### 相域电报方程

对于n相均匀传输线，相域中的电报方程为：

**电压方程**:
$$-\frac{d\mathbf{V}}{dx} = \mathbf{Z}\mathbf{I}$$

**电流方程**:
$$-\frac{d\mathbf{I}}{dx} = \mathbf{Y}\mathbf{V}$$

其中：
- $\mathbf{V} = [V_1, V_2, ..., V_n]^T$: 相电压向量
- $\mathbf{I} = [I_1, I_2, ..., I_n]^T$: 相电流向量
- $\mathbf{Z}$: $n \times n$ 单位长度串联阻抗矩阵
- $\mathbf{Y}$: $n \times n$ 单位长度并联导纳矩阵

#### 阻抗与导纳矩阵结构

对于三相平衡系统：

**阻抗矩阵**:
$$\mathbf{Z} = \begin{bmatrix} Z_s & Z_m & Z_m \\ Z_m & Z_s & Z_m \\ Z_m & Z_m & Z_s \end{bmatrix}$$

**导纳矩阵**:
$$\mathbf{Y} = \begin{bmatrix} Y_s & Y_m & Y_m \\ Y_m & Y_s & Y_m \\ Y_m & Y_m & Y_s \end{bmatrix}$$

其中：
- $Z_s$: 自阻抗
- $Z_m$: 互阻抗
- $Y_s$: 自导纳
- $Y_m$: 互导纳

### 特征值问题

#### 基本特征值方程

为将耦合方程解耦，需要求解以下特征值问题：

$$\mathbf{Z}\mathbf{Y} \mathbf{T} = \mathbf{T} \mathbf{\Lambda}$$

或等价地：

$$(\mathbf{Z}\mathbf{Y} - \lambda_i \mathbf{I})\mathbf{t}_i = 0$$

其中：
- $\mathbf{\Lambda} = \text{diag}(\lambda_1, \lambda_2, ..., \lambda_n)$: 特征值对角矩阵
- $\mathbf{T} = [\mathbf{t}_1, \mathbf{t}_2, ..., \mathbf{t}_n]$: 特征向量矩阵（模态变换矩阵）
- $\lambda_i$: 第i个特征值
- $\mathbf{t}_i$: 对应的特征向量

#### 特征值与传播常数的关系

特征值与模态传播常数的关系为：

$$\gamma_i = \sqrt{\lambda_i}$$

因此：
$$\mathbf{\Gamma} = \sqrt{\mathbf{\Lambda}} = \text{diag}(\gamma_1, \gamma_2, ..., \gamma_n)$$

#### 特征向量的归一化

特征向量可以进行不同方式的归一化：

**1. 最大元素归一化**:
$$\mathbf{t}_i^{(norm)} = \frac{\mathbf{t}_i}{\max(|\mathbf{t}_i|)}$$

**2. 欧几里得归一化**:
$$\mathbf{t}_i^{(norm)} = \frac{\mathbf{t}_i}{\|\mathbf{t}_i\|_2}$$

**3. 首元素归一化**:
$$\mathbf{t}_i^{(norm)} = \frac{\mathbf{t}_i}{t_{i1}}$$

归一化方式的选择会影响变换矩阵的具体形式，但不改变模态解耦的本质。

### 相似变换原理

#### 数学基础

模态变换本质上是一种相似变换。设变换矩阵为$\mathbf{T}$，则：

**电压变换**:
$$\mathbf{V}_m = \mathbf{T}^{-1} \mathbf{V}$$

**电流变换**:
$$\mathbf{I}_m = \mathbf{T}^T \mathbf{I}$$

或
$$\mathbf{I}_m = \mathbf{T}^{-1} \mathbf{I}$$

（取决于功率不变性的要求）

#### 功率不变性条件

若要求变换前后功率守恒：

$$\mathbf{V}^T \mathbf{I}^* = \mathbf{V}_m^T \mathbf{I}_m^*$$

则要求：
$$\mathbf{T}^{-1} = (\mathbf{T}^T)^*$$

即$\mathbf{T}$为酉矩阵（对于复变换）或正交矩阵（对于实变换）。

#### 模域方程推导

将相域方程变换到模域：

$$-\frac{d\mathbf{V}_m}{dx} = \mathbf{T}^{-1}\mathbf{Z}\mathbf{T} \mathbf{I}_m = \mathbf{Z}_m \mathbf{I}_m$$

$$-\frac{d\mathbf{I}_m}{dx} = \mathbf{T}^T\mathbf{Y}(\mathbf{T}^T)^{-1} \mathbf{V}_m = \mathbf{Y}_m \mathbf{V}_m$$

其中模态阻抗和导纳矩阵为对角矩阵：

$$\mathbf{Z}_m = \text{diag}(Z_{m1}, Z_{m2}, ..., Z_{mn})$$
$$\mathbf{Y}_m = \text{diag}(Y_{m1}, Y_{m2}, ..., Y_{mn})$$

这使得各模态方程完全解耦。

## 常用变换矩阵

### 对称分量变换 (Symmetrical Components)

#### 变换矩阵

$$\mathbf{T}_s = \frac{1}{3}\begin{bmatrix} 1 & 1 & 1 \\ 1 & a & a^2 \\ 1 & a^2 & a \end{bmatrix}$$

逆变换：
$$\mathbf{T}_s^{-1} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & a^2 & a \\ 1 & a & a^2 \end{bmatrix}$$

其中 $a = e^{j2\pi/3} = -\frac{1}{2} + j\frac{\sqrt{3}}{2}$

#### 分量定义

- **零序(Zero Sequence)**: $V_0 = \frac{1}{3}(V_a + V_b + V_c)$
- **正序(Positive Sequence)**: $V_1 = \frac{1}{3}(V_a + aV_b + a^2V_c)$
- **负序(Negative Sequence)**: $V_2 = \frac{1}{3}(V_a + a^2V_b + aV_c)$

#### 特点与应用

**优点**:
- 物理意义明确：分别代表三相系统的零序、正序、负序分量
- 在平衡系统中完全解耦
- 与旋转电机分析自然衔接

**缺点**:
- 复数变换，时域实现需要复数运算
- 在非平衡线路上不完全解耦
- 仅适用于三相系统

#### 序阻抗

对于平衡系统：
$$Z_0 = Z_s + 2Z_m$$
$$Z_1 = Z_2 = Z_s - Z_m$$

### Clarke变换 (αβ0变换)

#### 变换矩阵

$$\mathbf{T}_c = \frac{2}{3}\begin{bmatrix} \frac{1}{2} & \frac{1}{2} & \frac{1}{2} \\ 1 & -\frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{\sqrt{3}}{2} & -\frac{\sqrt{3}}{2} \end{bmatrix}$$

或功率守恒形式：
$$\mathbf{T}_c = \sqrt{\frac{2}{3}}\begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ 1 & -\frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{\sqrt{3}}{2} & -\frac{\sqrt{3}}{2} \end{bmatrix}$$

#### 分量定义

- **0分量(零序)**: $V_0 = \frac{1}{3}(V_a + V_b + V_c)$
- **α分量**: $V_\alpha = \frac{2}{3}(V_a - \frac{1}{2}V_b - \frac{1}{2}V_c)$
- **β分量**: $V_\beta = \frac{2}{3}(\frac{\sqrt{3}}{2}V_b - \frac{\sqrt{3}}{2}V_c)$

#### 几何解释

Clarke变换将三相电压映射到二维静止坐标系：
- α轴与a相轴线重合
- β轴超前α轴90°
- 零序分量独立于αβ平面

#### 特点

**优点**:
- 实数变换，便于时域实现
- 瞬时功率守恒（适当归一化时）
- 电机控制中广泛应用
- 可以扩展到任意相数

**缺点**:
- 在非对称系统中不完全解耦
- 物理意义不如对称分量直观

### Karrenbauer变换

#### 变换矩阵

$$\mathbf{T}_k = \begin{bmatrix} 1 & 1 & 1 \\ 1 & -2 & 1 \\ 1 & 1 & -2 \end{bmatrix}$$

或归一化形式：
$$\mathbf{T}_k = \frac{1}{3}\begin{bmatrix} 1 & 1 & 1 \\ 1 & -2 & 1 \\ 1 & 1 & -2 \end{bmatrix}$$

#### 分量定义

- **地模(Ground Mode)**: $V_g = \frac{1}{3}(V_a + V_b + V_c)$
- **线模1(Line Mode 1)**: $V_{l1} = \frac{1}{3}(V_a - 2V_b + V_c)$
- **线模2(Line Mode 2)**: $V_{l2} = \frac{1}{3}(V_a + V_b - 2V_c)$

#### 特点

**优点**:
- 实数变换，计算简单
- 第一模态对应零序（地模）
- EMTP早期版本使用
- 变换矩阵元素为整数，便于手工计算

**缺点**:
- 在非对称线路上解耦效果不佳
- 线模间可能存在耦合

### Wedepohl变换

#### 变换矩阵求解

Wedepohl变换基于实际线路参数求解，通过计算$\mathbf{Z}\mathbf{Y}$的特征向量得到：

$$\mathbf{T}_w = \text{eigenvectors}(\mathbf{Z}\mathbf{Y})$$

#### 求解步骤

**1. 计算乘积矩阵**:
$$\mathbf{P} = \mathbf{Z}\mathbf{Y}$$

**2. 求解特征值**:
$$\det(\mathbf{P} - \lambda\mathbf{I}) = 0$$

**3. 求解特征向量**:
对于每个特征值$\lambda_i$，解：
$$(\mathbf{P} - \lambda_i\mathbf{I})\mathbf{t}_i = 0$$

**4. 构造变换矩阵**:
$$\mathbf{T}_w = [\mathbf{t}_1, \mathbf{t}_2, ..., \mathbf{t}_n]$$

#### 特点

**优点**:
- 在频域中实现完全解耦
- 最优的解耦效果
- 适用于任意线路参数（包括非对称）

**缺点**:
- 复数变换，时域实现复杂
- 变换矩阵随频率变化
- 需要在每个频率点重新计算

## 变换矩阵对比分析

### 对比表

| 特性 | 对称分量 | Clarke | Karrenbauer | Wedepohl |
|------|----------|--------|-------------|----------|
| 变换类型 | 复数 | 实数 | 实数 | 复数 |
| 适用范围 | 三相 | 任意相数 | 三相 | 任意相数 |
| 解耦效果 | 完全(平衡) | 部分 | 部分 | 完全(频域) |
| 时域实现 | 复杂 | 简单 | 简单 | 复杂 |
| 频率依赖 | 否 | 否 | 否 | 是 |
| 物理意义 | 明确 | 中等 | 中等 | 抽象 |

### 变换矩阵关系

对于平衡三相系统，各变换矩阵之间存在线性关系：

$$\mathbf{T}_s = \mathbf{T}_c \mathbf{A}$$
$$\mathbf{T}_c = \mathbf{T}_k \mathbf{B}$$

其中$\mathbf{A}$和$\mathbf{B}$为常数矩阵。

### 选择准则

**时域仿真（如EMTP）**:
- 优先选择实变换（Clarke或Karrenbauer）
- 需要与旋转电机接口时选Clarke

**频域分析**:
- 优先选择Wedepohl变换
- 需要完全解耦时必选

**对称故障分析**:
- 对称分量变换最直观

## 频率相关的模态变换

### 频变参数的影响

实际输电线路和电缆的参数（电阻、电感、电容）随频率变化，导致：

**1. 参数矩阵频变**:
$$\mathbf{Z}(\omega) = \mathbf{R}(\omega) + j\omega\mathbf{L}(\omega)$$
$$\mathbf{Y}(\omega) = j\omega\mathbf{C}(\omega)$$

**2. 变换矩阵频变**:
$$\mathbf{T}(\omega) = \text{eigenvectors}(\mathbf{Z}(\omega)\mathbf{Y}(\omega))$$

### 频变模态参数

**模态传播常数**:
$$\gamma_m(\omega) = \sqrt{Z_m(\omega)Y_m(\omega)}$$

**模态特性阻抗**:
$$Z_{cm}(\omega) = \sqrt{\frac{Z_m(\omega)}{Y_m(\omega)}}$$

**模态传播速度**:
$$v_m(\omega) = \frac{\omega}{\text{Im}(\gamma_m(\omega))}$$

### 频变变换的处理方法

#### 方法1: 频率点计算
在每个感兴趣的频率点计算变换矩阵：
$$\mathbf{T}(\omega_i), \quad i = 1, 2, ..., N$$

#### 方法2: 拟合逼近
使用[[vector-fitting]]等方法拟合变换矩阵元素的频率响应：
$$T_{ij}(s) \approx \sum_{k=1}^{n} \frac{r_k}{s-p_k} + d + se$$

#### 方法3: 准模态变换
在某一参考频率计算变换矩阵，然后近似用于整个频带：
$$\mathbf{T} \approx \mathbf{T}(\omega_0)$$

### 实现挑战

**1. 相位一致性**: 特征向量的相位随频率变化，需要追踪连续性

**2. 模态排序**: 特征值排序可能随频率变化，需要保持模态识别

**3. 时域实现**: 频变变换在时域难以直接实现，通常采用卷积或状态空间方法

## 模态参数的物理意义

### 传播模式解释

每个模态对应系统的一种固有传播模式：

**地模(Ground Mode)**:
- 三相电流同相流动
- 通过大地返回
- 传播速度较慢（受地电阻影响）
- 衰减较大

**线模(Line Mode)**:
- 相间电流形成回路
- 不依赖大地返回
- 传播速度接近光速
- 衰减较小

### 特征阻抗的物理意义

模态特征阻抗表示该模态中电压与电流的比值：

$$Z_{cm} = \frac{V_m}{I_m}$$

**特性**:
- 反映模态的电磁场分布
- 决定行波的反射系数
- 用于边界条件匹配

### 传播常数的分解

$$\gamma_m = \alpha_m + j\beta_m$$

**衰减常数$\alpha_m$**:
- 表示单位长度的幅值衰减
- 单位：Np/km或dB/km
- 主要来源：导体电阻、大地损耗、介质损耗

**相位常数$\beta_m$**:
- 表示单位长度的相位变化
- 单位：rad/km
- 决定传播速度：$v_m = \omega/\beta_m$

## 多导线系统的模态变换

### n相系统的扩展

对于n相系统，特征值问题为n维：

$$\mathbf{Z}_{n\times n}\mathbf{Y}_{n\times n}\mathbf{T} = \mathbf{T}\mathbf{\Lambda}$$

**特性**:
- n个特征值（可能有重根）
- n个特征向量
- 可能包含复数共轭对

### 双回线路的模态分析

双回三相线路共6相，产生6个模态：

**模态分类**:
- 2个地模（两个回路的同相分量）
- 4个线模（相间耦合模式）

**特点**:
- 两回线路间存在耦合
- 需要6×6变换矩阵
- 可能存在相近的特征值（数值计算挑战）

### 分裂导线的处理

对于分裂导线，可以先进行相-束变换：

**步骤1**: 将分裂导线等效为单导线
$$Z_{eq} = Z_{self} - \frac{Z_{mutual}^2}{Z_{self}}$$

**步骤2**: 对等效导线进行模态变换

## 电缆系统的特殊模态特性

### 同轴电缆的模态

单芯同轴电缆通常考虑3个导体：
- 芯线(Core)
- 护套(Sheath)
- 大地(Ground)

产生3个模态：

**芯-护套模态(Core-Sheath Mode)**:
- 电流在芯线和护套间流动
- 传播速度较高
- 衰减较小

**护套-地模态(Sheath-Ground Mode)**:
- 电流在护套和大地间流动
- 传播速度较低
- 衰减较大

**地模(Ground Mode)**:
- 三相护套并联接地
- 传播速度最低
- 衰减最大

### 三芯电缆的特殊性

**铠装电缆**:
- 导体：3芯线 + 护套 + 铠装 + 大地
- 模态数：5或6个
- 护套和铠装间存在耦合

**交叉互联电缆**:
- 护套分段交叉连接
- 需要分段模态分析
- 边界条件处理复杂

### 护套接地方式的影响

**两端接地**:
- 护套电流可以自由流通
- 护套模态衰减大
- 需要考虑环流损耗

**单端接地**:
- 护套电流受限
- 感应电压问题
- 过电压保护设计关键

**交叉互联**:
- 护套感应电压抵消
- 环流最小化
- 需要特殊边界处理

## EMT仿真中的实现细节

### 时域实现方法

#### 方法1: 恒定变换矩阵

**步骤**:
1. 在参考频率（如工频或几何平均频率）计算$\mathbf{T}$
2. 整个仿真过程中使用恒定$\mathbf{T}$
3. 相域↔模域转换在每个时间步进行

**转换公式**:
$$\mathbf{V}_m = \mathbf{T}^{-1}\mathbf{V}$$
$$\mathbf{V} = \mathbf{T}\mathbf{V}_m$$

**优点**:
- 实现简单
- 计算效率高

**缺点**:
- 不能精确模拟频变特性
- 在非对称线路上引入误差

#### 方法2: 模域Bergeron模型

**实现流程**:
```
相域电压 → [T⁻¹] → 模域电压 → Bergeron传输 → 模域电流 → [T] → 相域电流
```

每个模态独立计算：
$$I_{mi}(t) = I_{mi}(t-\tau_m) + \frac{1}{Z_{cm}}[V_{mi}(t) - V_{mi}(t-\tau_m)]$$

#### 方法3: 频率相关模型(FD-Line)

**步骤**:
1. 在频域计算各模态的频率响应
2. 使用[[vector-fitting]]拟合有理函数
3. 转换为时域递归卷积

**模态处理**:
$$H_m(s) = \sum_{k=1}^{N} \frac{r_{mk}}{s-p_{mk}} + d_m$$

### 数值稳定性考虑

#### 特征值求解的数值问题

**1. 相近特征值**:
当两个特征值接近时，对应的特征向量可能数值不稳定。

**解决方法**:
- 使用子空间迭代法
- 应用特征值排序和追踪算法

**2. 复数特征值**:
非对称系统中可能出现复数特征值。

**处理**:
- 复数变换矩阵的实部/虚部分离
- 或直接使用复数运算

**3. 病态矩阵**:
当$\mathbf{Z}\mathbf{Y}$条件数很大时，数值精度下降。

**改进**:
- 使用QR算法而非幂法
- 增加数值精度（双精度）

#### 时域稳定性

**1. 插值误差**:
行波传输需要插值，引入数值色散。

**处理**:
- 使用高阶插值（如三次样条）
- 或调整时间步长与传播时间的关系

**2. 数值振荡**:
集中参数模型与分布参数模型接口处可能出现振荡。

**抑制**:
- 添加小阻尼
- 使用抗混叠滤波器

### 与外部电路的接口

#### 边界条件处理

**相域边界**:
- 在相域中处理电源、负载、故障
- 通过变换矩阵转换到模域

**模态边界**:
- 各模态独立处理
- 模态间通过变换矩阵间接耦合

#### 非线性元件处理

当存在非线性元件（如避雷器）时：

**方法**:
1. 在相域处理非线性
2. 线性部分在模域处理
3. 每个时间步迭代求解

### 并行计算优化

**模态并行**:
各模态完全独立，可以并行计算：
```
对于每个模态m并行执行:
    计算模态传播
    更新模态电流
结束
同步
相域重构
```

**实现**:
- OpenMP多线程
- GPU加速
- 分布式计算

## 数值计算考虑

### 特征值求解算法

#### QR算法

**适用**: 中小型矩阵（n < 100）

**步骤**:
1. 将矩阵化为Hessenberg形式
2. 迭代应用QR分解
3. 收敛后提取特征值

**复杂度**: $O(n^3)$

#### 子空间迭代法

**适用**: 大型稀疏矩阵，只需要部分特征值

**步骤**:
1. 选择初始向量空间
2. 迭代应用矩阵乘法
3. Rayleigh-Ritz投影
4. 收敛判断

**优势**: 可以只求解需要的模态

#### Lanczos算法

**适用**: 对称大型稀疏矩阵

**特点**:
- 构造三对角矩阵
- 特征值快速收敛
- 需要重正交化防止"幽灵"模态

### 特征向量计算精度

#### 条件数分析

特征向量的条件数：
$$\kappa_i = \frac{1}{|\mathbf{y}_i^* \mathbf{x}_i|}$$

其中$\mathbf{y}_i$和$\mathbf{x}_i$分别为左右特征向量。

**影响**:
- 条件数大→特征向量对扰动敏感
- 相近特征值导致大条件数

#### 精度改进方法

**1. 迭代精化**:
$$\mathbf{t}_i^{(k+1)} = \mathbf{t}_i^{(k)} + \delta\mathbf{t}_i$$

**2. 双精度计算**:
使用双精度或扩展精度进行特征值分解

**3. 符号一致性**:
确保特征向量在连续频率点的相位连续

### 变换矩阵的正交化

当需要功率不变性时，对变换矩阵进行正交化处理：

**Gram-Schmidt正交化**:
$$\mathbf{q}_i = \frac{\mathbf{t}_i - \sum_{j=1}^{i-1}(\mathbf{q}_j^*\mathbf{t}_i)\mathbf{q}_j}{\|\mathbf{t}_i - \sum_{j=1}^{i-1}(\mathbf{q}_j^*\mathbf{t}_i)\mathbf{q}_j\|}$$

**QR分解法**:
$$\mathbf{T} = \mathbf{Q}\mathbf{R}$$
取$\mathbf{Q}$作为正交变换矩阵

## 应用实例

### 实例1: 500kV输电线路暂态分析

**线路参数**:
- 长度：300km
- 电压等级：500kV
- 导线：4分裂

**模态参数**:

| 模态 | 传播速度(km/ms) | 衰减(dB/km) | 特性阻抗(Ω) |
|------|-----------------|-------------|-------------|
| 地模 | 240 | 0.08 | 850 |
| 线模1 | 295 | 0.02 | 320 |
| 线模2 | 295 | 0.02 | 320 |

**仿真结果**:
- 单相接地故障时，地模主导暂态过程
- 线模传播速度快，首先到达对端
- 地模衰减大，波头平缓

### 实例2: XLPE电缆系统谐振分析

**系统配置**:
- 电缆长度：10km
- 电压等级：220kV
- 护套：交叉互联接地

**模态特性**:

| 模态 | 谐振频率(Hz) | 品质因数Q |
|------|--------------|-----------|
| 芯-护套 | 1530 | 45 |
| 护套-地 | 820 | 12 |
| 地模 | 340 | 5 |

**应用**:
- 识别谐振风险频率
- 设计滤波器参数
- 评估过电压水平

### 实例3: 变压器绕组波过程

**绕组模型**:
- 多层线圈，每层视为一相
- 共12层，12×12参数矩阵

**模态分析**:
- 12个模态对应不同振荡模式
- 高频模态：层间电容主导
- 低频模态：电感主导

**应用**:
- 雷击过电压分布计算
- 绝缘配合设计
- 波过程仿真加速

### 实例4: HVDC输电线路故障定位

**双极HVDC线路**:
- 极线1、极线2、地线
- 3×3阻抗矩阵

**模态应用**:
1. 将故障行波分解为模态
2. 各模态独立传播到两端
3. 利用模态到达时间差定位故障

**优势**:
- 地模对故障类型敏感
- 线模传播稳定，适合测距
- 模态分离提高抗干扰能力

## 与其他方法的关联

### 与对称分量法的关系

对称分量法是模态变换在三相平衡系统的特例：

$$\mathbf{T}_{symmetrical} = \mathbf{T}_{modal}(\text{balanced system})$$

**区别**:
- 对称分量法通常限于工频分析
- 模态变换适用于全频域
- 对称分量法物理意义更明确

### 与相域方法的比较

| 特性 | 相域方法 | 模域方法 |
|------|----------|----------|
| 方程耦合 | 是 | 否 |
| 计算效率 | 低 | 高 |
| 物理直观性 | 高 | 低 |
| 适用系统 | 任意 | 均匀线路 |
| 并行性 | 差 | 好 |

### 与EMT仿真的集成

模态变换是[[emt-simulation-verification]]仿真软件的核心算法：

**EMTP**: 使用Karrenbauer或Clarke变换
**PSCAD**: 支持模态和相域两种方法
**RTDS**: 实时实现模态变换

## 数学公式汇总

### 核心变换公式

**相域到模域**:
$$\mathbf{V}_m = \mathbf{T}^{-1}\mathbf{V}$$
$$\mathbf{I}_m = \mathbf{T}^T\mathbf{I}$$

**模域到相域**:
$$\mathbf{V} = \mathbf{T}\mathbf{V}_m$$
$$\mathbf{I} = (\mathbf{T}^T)^{-1}\mathbf{I}_m$$

### 模态参数公式

**模态阻抗**:
$$\mathbf{Z}_m = \mathbf{T}^{-1}\mathbf{Z}\mathbf{T}$$

**模态导纳**:
$$\mathbf{Y}_m = \mathbf{T}^T\mathbf{Y}(\mathbf{T}^T)^{-1}$$

**传播常数**:
$$\gamma_m = \sqrt{Z_m Y_m}$$

**特性阻抗**:
$$Z_c = \sqrt{\frac{Z_m}{Y_m}}$$

**传播速度**:
$$v = \frac{\omega}{\text{Im}(\gamma)}$$

### 特征值问题

$$\mathbf{Z}\mathbf{Y}\mathbf{T} = \mathbf{T}\mathbf{\Lambda}$$
$$\det(\mathbf{Z}\mathbf{Y} - \lambda\mathbf{I}) = 0$$

## 相关主题

- [[transmission-line-model]] - 输电线路建模
- [[cable-model]] - 电缆模型
- [[symmetrical-components]] - 对称分量法
- [[modal-domain-decoupling]] - 模域解耦
- [[bergeron-model]] - Bergeron模型
- [[vector-fitting]] - 矢量拟合
- [[frequency-dependent-modeling]] - 频率相关建模
- [[numerical-integration]] - 数值积分
- [[state-space-method]] - 状态空间法
- [[eigenvalue-analysis]] - 特征值分析

## 来源论文

参见 [[index]] 获取更多模态变换相关文献，以及以下分类页面：
- [[interface-technique]] - 所有EMT方法
- [[transmission-line-model]] - 输电线路建模方法
- [[cable-model]] - 电缆建模方法
