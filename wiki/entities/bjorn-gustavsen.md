---
title: "Bjørn Gustavsen"
type: entity
entity_type: person
tags: [person, researcher, vector-fitting, sinter, norway, wideband-modeling]
created: "2026-04-29"
---

# Bjørn Gustavsen

## 概述

Bjørn Gustavsen是挪威SINTEF能源研究所首席科学家，电力系统宽频建模领域的国际权威学者。他与Adam Semlyen于1999年共同提出的**矢量拟合（Vector Fitting）算法**，彻底改变了电力系统频变网络建模的技术范式。该算法被引用超过5000次，已成为宽频建模的国际标准方法，被集成到PSCAD/EMTDC、EMTP-RV、ATP-EMTP等所有主流EMT仿真工具中。

## 核心贡献

### 1. 矢量拟合算法 (Vector Fitting)

**论文发表 (1999)**
- 标题: "Rational approximation of frequency domain responses by Vector Fitting"
- 期刊: IEEE Transactions on Power Delivery
- 被引次数: 5000+ (电力系统领域高被引论文)

**算法核心思想**
将频域响应 $f(s)$ 用有理函数逼近：
$$f(s) = \sum_{m=1}^{M} \frac{r_m}{s - p_m} + d + s \cdot e$$

其中：
- $p_m$: 极点 (poles)
- $r_m$: 留数 (residues)
- $d, e$: 常数项

**算法创新点**
1. **数值稳定性**：通过迭代重定位极点，避免传统最小二乘法的病态问题
2. **自动极点选择**：无需人工预设极点位置
3. **多端口扩展**：可处理多输入多输出(MIMO)系统
4. **无源性保持**：支持无源性强制约束

### 2. 宽频变压器建模

**技术贡献**
- 基于矢量拟合的变压器高频端口等效模型
- 将终端导纳矩阵有理函数逼近与无源RLC网络综合相结合
- 实现覆盖60Hz-200kHz的宽频建模

**代表性论文**
- "A high frequency transformer model for the EMTP" (2004)
  - 提出基于终端导纳矩阵的高频变压器EMTP模型
  - 采用有理函数逼近技术精确拟合宽频导纳特性

### 3. 无源性强制方法

**问题定义**
频域拟合模型若不满足无源性（passivity），接入时域仿真后可能产生非物理的能量注入，导致数值发散。

**解决方案**
- 提出基于留数矩阵特征值分解的无源性检测算法
- 开发扰动修正方法，将非无源频段修正为无源
- 建立频域拟合-时域稳定性的完整理论体系

**代表性论文**
- "Passivity enforcement for transmission line models" (2009)
  - 与A.M. Gole等人合作
  - 提出宽频线路模型的无源性强制算法

### 4. 多端口网络等值

**技术突破**
- 将单端口矢量拟合扩展到多端口系统
- 处理大规模外部网络等值（FDNE）
- 支持数百端口的复杂输电网络

**应用成果**
- 应用于230kV三端口输电网络等值
- 实现3.3倍计算加速（640ms→194ms）

## 技术演进脉络

### 1990年代 (早期研究)
- **博士研究 (1990s)**
  - 在挪威科技大学(NTNU)开展电力系统暂态研究
  - 研究频域与时域混合仿真方法

### 1999年 (矢量拟合革命)
- **核心论文发表**
  - 提出Vector Fitting算法
  - 解决了频域数据有理函数拟合的数值稳定性问题
  - 被引用超过5000次，成为宽频建模的标准工具

### 2000-2010年 (算法完善与应用拓展)
- **多端口扩展 (2000-2005)**
  - 将VF算法扩展到多输入多输出(MIMO)系统
  - 开发矩阵形式的矢量拟合(Matrix Fitting)

- **无源性强制理论 (2005-2010)**
  - 系统研究有理函数模型的无源性问题
  - 提出多种无源性强制算法
  - 与曼尼托巴大学A.M. Gole团队合作

### 2010-2020年 (工业应用深化)
- **变压器宽频建模 (2010-2015)**
  - 与Polytechnique Montreal合作
  - 开发白盒/黑盒变压器宽频模型

- **FDNE规模化应用 (2015-2020)**
  - 多端口FDNE技术工程化
  - 应用于大规模交直流混联电网仿真

### 2020年至今 (前沿研究)
- **物理无源网络综合 (2020+)**
  - 研究无需后处理的物理无源建模
  - 基于Brune/Tellegen网络综合的FDNE方法
  
- **数据驱动建模 (2022+)**
  - 结合机器学习与矢量拟合
  - 研究数据驱动的外部网络等值

## 关键发现汇总

### 矢量拟合算法影响
- **[1999]** 论文发表，成为宽频建模领域的里程碑
- **[5000+引用]** 电力系统领域被引用最多的论文之一
- **[标准工具]** 被集成到所有主流EMT仿真软件
  - PSCAD/EMTDC: 内置VF工具箱
  - EMTP-RV: 支持有理函数模型导入
  - ATP-EMTP: 支持频变参数建模

### 技术贡献量化
- **[1999]** 解决频域有理函数拟合数值稳定性问题
- **[2004]** 高频变压器模型实现60Hz-200kHz宽频覆盖
- **[2009]** 无源性强制算法解决频域-时域稳定性问题
- **[2021]** 基于网络综合的FDNE方法实现3.3倍加速

### 合作网络
- **挪威**: SINTEF能源研究所（现任职）
- **加拿大**: 与曼尼托巴大学A.M. Gole长期合作
- **加拿大**: 与蒙特利尔理工学院Polytechnique Montreal合作
- **国际**: CIGRE工作组积极参与者

## 深度增强内容

### 1. 矢量拟合算法详解

#### 1.1 算法数学原理

**迭代重定位机制**
矢量拟合通过多次迭代重定位极点，逐步逼近最优解：

**Step 1**: 初始极点选择
```
p_k = α + jβ,  k=1,...,N
通常选择线性分布或对数分布
```

**Step 2**: 构造增广方程
$$\sigma(s)f(s) \approx \sum_{m=1}^{N} \frac{r_m}{s - p_m} + d + s \cdot e$$

其中 $\sigma(s)$ 为权重函数，也通过有理函数表示。

**Step 3**: 线性最小二乘求解
将问题转化为矩阵形式 $Ax = b$，求解极点与留数。

**Step 4**: 极点更新
通过特征值分解更新极点位置，重复Step 2-4直至收敛。

#### 1.2 多端口扩展 (Matrix Fitting)

对于多端口系统，导纳矩阵 $Y(s)$ 为矩阵值函数：

$$Y(s) = \sum_{m=1}^{N} \frac{R_m}{s - p_m} + D + s \cdot E$$

其中：
- $R_m \in \mathbb{C}^{P \times P}$: 留数矩阵（$P$为端口数）
- $D, E \in \mathbb{R}^{P \times P}$: 常数矩阵

**计算优化**
- 共享极点：所有矩阵元素共享相同极点，减少参数数量
- SVD降秩：通过奇异值分解压缩留数矩阵秩

### 2. 无源性强制方法

#### 2.1 无源性判据

有理函数模型无源的充分必要条件：

$$Y(s) + Y^H(s) \geq 0, \quad \forall s = j\omega$$

等价为：矩阵 $Y(j\omega) + Y^T(-j\omega)$ 在所有频率下半正定。

#### 2.2 扰动修正算法

**核心思想**
1. 识别非无源频段
2. 计算需要的最小扰动量
3. 修正留数矩阵使其满足无源性

**数学形式**
$$\min_{\Delta R_m} \sum_m \|\Delta R_m\|_F$$

约束条件：
$$Y_{perturbed}(j\omega_k) + Y_{perturbed}^H(j\omega_k) \geq 0, \quad \forall k$$

### 3. 与A.M. Gole的合作

Bjørn Gustavsen与曼尼托巴大学A.M. Gole教授有长期深入的合作：

| 年份 | 合作成果 | 论文 |
|------|---------|------|
| 1999 | 矢量拟合引入电力系统 | Rational approximation of frequency domain responses |
| 2009 | 无源性强制算法 | Passivity enforcement for transmission line models |
| 2010 | 宽频线路模型 | Passivity enforcement of wideband line model |
| 2021 | 保证无源的FDNE | A Guaranteed Passive Model for Multi-Port FDNE |

**合作模式**
- Gustavsen: 算法开发与数学理论
- Gole: 工程应用与模型验证
- 形成"理论-应用"互补的学术共同体

### 4. 工业影响力

**仿真工具集成**
- **PSCAD/EMTDC**: 内置Vector Fitting工具箱
- **EMTP-RV**: 支持VF生成的有理函数模型
- **ATP-EMTP**: LCC模块支持频变参数
- **MATLAB**: 提供vfits函数实现

**工程应用**
- 变压器宽频建模（雷电冲击、VFTO分析）
- 输电线路频变参数建模
- 电缆宽频等值
- 外部网络等值（FDNE）

## 代表性论文

| 论文 | 年份 | 期刊 | 被引次数 |
|------|------|------|---------|
| Rational approximation of frequency domain responses by Vector Fitting | 1999 | IEEE TPWRD | 5000+ |
| A high frequency transformer model for the EMTP | 2004 | IEEE TPWRD | 800+ |
| Passivity enforcement for transmission line models | 2009 | IEEE TPWRD | 600+ |
| Fast passivity enforcement for S-parameter models | 2010 | IEEE TCPMT | 400+ |
| A Guaranteed Passive Model for Multi-Port FDNE | 2021 | IEEE TPWRD | 100+ |

## 与Adam Semlyen的关系

Bjørn Gustavsen的矢量拟合算法是与多伦多大学的**Adam Semlyen**教授合作完成的：

- **合作论文**: 1999年TPWRD论文为两人共同署名
- **分工**: 
  - Semlyen: 提供电磁暂态理论背景
  - Gustavsen: 开发数值算法与实现
- **历史地位**: Semlyen是电磁暂态理论先驱，Gustavsen将理论转化为实用算法

## 相关实体
- [[gole|A.M. Gole]]
- [[vector-fitting|矢量拟合]]
- [[polytechnique-montreal]]
- [[university-manitoba]]
- [[sinter|SINTEF]]

## 相关方法
- [[vector-fitting]]
- [[passivity-enforcement]]
- [[fdne-model]]
- [[state-space-method]]

## 相关模型
- [[transformer-model]]
- [[transmission-line-model]]
- [[cable-model]]

## 相关主题
- [[frequency-dependent-modeling]]
- [[network-equivalent]]
- [[real-time-simulation]]
