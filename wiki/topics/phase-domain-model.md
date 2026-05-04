---
title: "相域模型 (Phase-Domain Model)"
type: topic
tags: [phase-domain, model, transmission-line, unbalanced, untranspose, asymmetrical]
created: "2026-05-02"
---

# 相域模型 (Phase-Domain Model)

## 概述

相域模型(Phase-Domain Model)是直接在abc三相坐标系下建立电力系统元件模型的方法，不经过模态变换到对称分量或模域。这种建模方式能够自然处理线路参数不对称、非换位线路和任意拓扑结构，适用于需要精确考虑相间耦合和不平衡工况的场合。与模域方法相比，相域模型虽然计算量较大，但能更准确地反映实际系统的不对称特性，是现代电磁暂态仿真的重要建模方法。随着计算能力的提升，相域方法在输电线路、变压器、电缆等元件建模中得到了广泛应用。

## 相域与模域对比

### 模域变换原理

**变换矩阵**:
三相到模域的变换:
$$\mathbf{T} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & a & a^2 \\ 1 & a^2 & a \end{bmatrix}, \quad a = e^{j120°}$$

**变换方程**:
$$\mathbf{V}_{mode} = \mathbf{T}^{-1}\mathbf{V}_{abc}$$
$$\mathbf{I}_{mode} = \mathbf{T}^{-1}\mathbf{I}_{abc}$$

**模域优势**:
- 三相解耦
- 独立计算
- 计算效率高

### 相域优势

**不对称处理**:
- 无需对称假设
- 自然处理不平衡
- 保留相间耦合

**非换位线路**:
- 参数不均匀性
- 电流不平衡
- 电压不平衡

**任意拓扑**:
- 灵活性强
- 适用复杂网络
- 多回线路

**谐波分析**:
- 直接谐波建模
- 保留谐波耦合
- 非线性负荷

## 相域输电线路模型

### 阻抗矩阵

**完全耦合矩阵**:
$$\mathbf{Z}_{abc} = \begin{bmatrix} Z_{aa} & Z_{ab} & Z_{ac} \\ Z_{ba} & Z_{bb} & Z_{bc} \\ Z_{ca} & Z_{cb} & Z_{cc} \end{bmatrix}$$

其中:
- 对角线元素: 自阻抗
- 非对角元素: 互阻抗
- 对称性: $Z_{ij} = Z_{ji}$

**阻抗计算**:
$$Z_{ii} = R_i + j\omega L_{ii}$$
$$Z_{ij} = R_{ij} + j\omega L_{ij} \quad (i \neq j)$$

### 导纳矩阵

**节点导纳方程**:
$$\begin{bmatrix} I_a \\ I_b \\ I_c \end{bmatrix} = \begin{bmatrix} Y_{aa} & Y_{ab} & Y_{ac} \\ Y_{ba} & Y_{bb} & Y_{bc} \\ Y_{ca} & Y_{cb} & Y_{cc} \end{bmatrix} \begin{bmatrix} V_a \\ V_b \\ V_c \end{bmatrix}$$

**导纳与阻抗关系**:
$$\mathbf{Y}_{abc} = \mathbf{Z}_{abc}^{-1}$$

### 相域Bergeron模型

**基本方程**:
历史电流源:
$$\mathbf{I}_h(t) = -2\mathbf{Y}_c\mathbf{V}(t-\tau) - \mathbf{I}_h(t-\tau)$$

**相域形式**:
$$\mathbf{I}(t) = \mathbf{Y}_c\mathbf{V}(t) + \mathbf{I}_h(t)$$

其中 $\mathbf{Y}_c$ 为相域特性导纳矩阵。

**传播时间矩阵**:
相域传播时间:
$$\mathbf{\tau} = \sqrt{\mathbf{L}_{abc}\mathbf{C}_{abc}}$$

非对角元素表示相间耦合的传播特性。

### 相域频变模型

**频率相关阻抗**:
$$\mathbf{Z}_{abc}(\omega) = \mathbf{R}(\omega) + j\omega\mathbf{L}(\omega)$$

**矢量拟合**:
对相域阻抗矩阵元素分别拟合:
$$Z_{ij}(s) = \sum_{m=1}^{N}\frac{c_m}{s-a_m} + d + se$$

**无源性检查**:
$$\mathbf{Y}_{abc}(j\omega) + \mathbf{Y}_{abc}^H(j\omega) \succeq 0$$

## 非换位线路建模

### 参数不对称性

**几何不对称**:
三相导线空间位置不同，导致:
- 自阻抗不等
- 互阻抗不等
- 电容不对称

**阻抗差异**:
$$Z_{aa} \neq Z_{bb} \neq Z_{cc}$$
$$Z_{ab} \neq Z_{bc} \neq Z_{ca}$$

### 电流不平衡

**零序电流**:
$$I_0 = \frac{1}{3}(I_a + I_b + I_c) \neq 0$$

**负序电流**:
$$I_2 = \frac{1}{3}(I_a + a^2 I_b + a I_c) \neq 0$$

**不平衡度**:
$$\varepsilon_I = \frac{I_-}{I_+} \times 100\%$$

### 电压不平衡

**电压降差异**:
$$\Delta V_a \neq \Delta V_b \neq \Delta V_c$$

**末端电压不平衡**:
$$\varepsilon_V = \frac{V_-}{V_+} \times 100\%$$

典型值: 1-3% (非换位线路)

## 相域电缆模型

### 多导体系统

**导体类型**:
- 三相芯线
- 金属护套
- 铠装层
- 接地导体

**阻抗矩阵**:
扩展的相域阻抗矩阵:
$$\mathbf{Z} = \begin{bmatrix} \mathbf{Z}_{core} & \mathbf{Z}_{c-s} \\ \mathbf{Z}_{s-c} & \mathbf{Z}_{sheath} \end{bmatrix}$$

### 护层接地方式

**单端接地**:
- 护层一端接地
- 另一端开路
- 感应电压限制

**交叉互联**:
- 分段交叉接地
- 抵消感应电压
- 环流抑制

**两端接地**:
- 护层两端接地
- 环流问题
- 损耗增加

## 相域变压器模型

### 三相变压器

**三相三柱式**:
- 磁路不对称
- 零序磁通
- 相域建模更准确

**三相组式**:
- 独立磁路
- 对称性较好
- 零序特性不同

### 多绕组变压器

**导纳矩阵**:
$$\begin{bmatrix} \mathbf{I}_1 \\ \mathbf{I}_2 \\ \mathbf{I}_3 \end{bmatrix} = \begin{bmatrix} \mathbf{Y}_{11} & \mathbf{Y}_{12} & \mathbf{Y}_{13} \\ \mathbf{Y}_{21} & \mathbf{Y}_{22} & \mathbf{Y}_{23} \\ \mathbf{Y}_{31} & \mathbf{Y}_{32} & \mathbf{Y}_{33} \end{bmatrix} \begin{bmatrix} \mathbf{V}_1 \\ \mathbf{V}_2 \\ \mathbf{V}_3 \end{bmatrix}$$

**相移处理**:
- Y/Δ接线
- 相移30°
- 相域直接处理

## 相域数值方法

### 伴随电路法

**电阻伴随**:
$$G_R = \frac{1}{R}$$

**电感伴随**:
$$G_L = \frac{\Delta t}{2L}, \quad I_{eq} = i_L(t-\Delta t) + G_L v_L(t-\Delta t)$$

**电容伴随**:
$$G_C = \frac{2C}{\Delta t}, \quad I_{eq} = -i_C(t-\Delta t) - G_C v_C(t-\Delta t)$$

**相域形式**:
$$\mathbf{G}_{abc}\mathbf{V}_{abc}(t) = \mathbf{I}_{abc}(t) + \mathbf{I}_{eq,abc}$$

### 节点分析法

**节点导纳方程**:
$$\mathbf{Y}_{node}\mathbf{V}_{node} = \mathbf{I}_{source}$$

**相域求解**:
直接求解3N×3N矩阵(N为节点数)

**稀疏技术**:
- 稀疏存储
- 最优排序
- 快速分解

## 应用场合

### 不对称故障分析

**单相接地**:
相域直接建立边界条件:
$$V_a = Z_f I_a, \quad I_b = I_c = 0$$

**两相短路**:
$$V_b = V_c, \quad I_a = 0, \quad I_b = -I_c$$

**断线故障**:
$$I_a = 0, \quad \Delta V_b = \Delta V_c = 0$$

### 非换位线路研究

**长期运行分析**:
- 电流不平衡
- 旋转电机负序
- 附加损耗

**保护整定**:
- 零序保护灵敏度
- 负序保护
- 不平衡保护

### 谐波分析

**谐波耦合**:
相域保留谐波间耦合:
$$\mathbf{I}_h = \mathbf{Y}_h \mathbf{V}_h$$

**非线性负荷**:
- 电弧炉
- 变频器
- 整流器

### 电力电子系统

**开关暂态**:
- 三相不对称开关
- PWM谐波
- 相间耦合

**控制器设计**:
- 相域控制
- 不平衡控制
- 谐波抑制

## 并行计算

### 区域分解

**分区策略**:
按相分区:
- a相子系统
- b相子系统
- c相子系统

**边界处理**:
- Dirichlet边界
- Neumann边界
- 重叠区域

### GPU加速

**大规模矩阵求解**:
- 稠密矩阵运算
- 并行LU分解
- 迭代求解器

**实时仿真**:
- 相域计算加速
- FPGA实现
- 并行处理

## 与模域方法比较

| 特性 | 相域模型 | 模域模型 |
|-----|---------|---------|
| 对称假设 | 不需要 | 需要 |
| 计算效率 | 较低 | 较高 |
| 不对称处理 | 精确 | 近似 |
| 非换位线路 | 适用 | 近似 |
| 谐波分析 | 直接 | 需多次变换 |
| 矩阵维度 | 3N×3N | 3个N×N |
| 物理意义 | 直接 | 抽象 |

## 相关主题
- [[modal-transformation]] - 模态变换
- [[symmetrical-components]] - 对称分量法
- `untransposed-line` - 非换位线路
- [[transmission-line-model]] - 输电线路模型

## 来源论文

参见 [[index]] 获取更多相域模型相关文献。
