---
title: "旋转电机建模 (Rotating Machine Modeling)"
type: topic
tags: [rotating-machine, synchronous-machine, induction-machine, dfig, pmsm, park-transform, vbr, phase-domain]
created: "2026-05-01"
book-chapter: "6"
---

# 旋转电机建模 (Rotating Machine Modeling)

## 概述

旋转电机是电力系统中最核心的机电能量转换设备，包括同步电机(发电机)、感应电机(电动机/负荷)、永磁同步电机(PMSM)等类型。在EMT仿真中，旋转电机建模面临独特挑战：需要同时处理电磁暂态(微秒级)和机电暂态(毫秒-秒级)的时间尺度差异，处理转子运动方程与电磁方程的耦合，以及准确表征磁路饱和、阻尼效应等非线性特性。

EMT语境下的旋转电机建模与机电暂态仿真(TS)有本质区别：EMT需要显式建模定子绕组暂态(忽略定子暂态是TS的典型简化)，处理dq0坐标变换带来的时变电感，解决数值稳定性问题(VBR方法)，以及实现与电力电子变流器的准确接口(新能源并网场景)。

## 作用机制

### 6.1 同步电机EMTP型建模

**坐标系选择与变换**

同步电机EMT建模的核心是Park变换，将三相abc坐标系转换到与转子同步旋转的dq0坐标系：

$$
\begin{bmatrix} i_d \\ i_q \\ i_0 \end{bmatrix} = \frac{2}{3}\begin{bmatrix} \cos\theta & \cos(\theta-120°) & \cos(\theta+120°) \\ -\sin\theta & -\sin(\theta-120°) & -\sin(\theta+120°) \\ 1/2 & 1/2 & 1/2 \end{bmatrix}\begin{bmatrix} i_a \\ i_b \\ i_c \end{bmatrix}
$$

**电压方程**

定子电压方程(dq0坐标系)：

$$
\begin{aligned}
v_d &= -R_s i_d - \omega\psi_q + \frac{d\psi_d}{dt} \\
v_q &= -R_s i_q + \omega\psi_d + \frac{d\psi_q}{dt} \\
v_0 &= -R_s i_0 + \frac{d\psi_0}{dt}
\end{aligned}
$$

转子绕组电压方程：

$$
v_{fd} &= R_{fd} i_{fd} + \frac{d\psi_{fd}}{dt} \\
0 &= R_{kd} i_{kd} + \frac{d\psi_{kd}}{dt} \\
0 &= R_{kq} i_{kq} + \frac{d\psi_{kq}}{dt}
\end{aligned}
$$

**磁链方程**

$$
\begin{bmatrix} \psi_d \\ \psi_q \\ \psi_{fd} \\ \psi_{kd} \\ \psi_{kq} \end{bmatrix} = \begin{bmatrix} L_d & 0 & L_{ad} & L_{ad} & 0 \\ 0 & L_q & 0 & 0 & L_{aq} \\ L_{ad} & 0 & L_{fd} & L_{ad} & 0 \\ L_{ad} & 0 & L_{ad} & L_{kd} & 0 \\ 0 & L_{aq} & 0 & 0 & L_{kq} \end{bmatrix}\begin{bmatrix} i_d \\ i_q \\ i_{fd} \\ i_{kd} \\ i_{kq} \end{bmatrix}
$$

**转子运动方程**

$$
J\frac{d\omega_r}{dt} &= T_m - T_e - D\omega_r \\
\frac{d\delta}{dt} &= \omega_r - \omega_s
\end{aligned}
$$

### 6.2 相域模型：直接abc坐标建模

**核心思想**

直接在abc三相坐标系下建模，无需Park变换，避免时变电感问题。

**电压方程**

$$
v_{abc} = R_s i_{abc} + \frac{d\psi_{abc}}{dt}
$$

**磁链方程**

$$
\psi_{abc} = L_{abc}(\theta)i_{abc} + \psi_{abc,r}
$$

其中电感矩阵$L_{abc}(\theta)$是转子位置角$\theta$的函数。

**恒定等效导纳技术**

为保持EMTP节点导纳矩阵恒定，采用方程重构：

$$
Y_{eq}v_{abc} = i_{inj} - i_{hist}
$$

其中等效导纳$Y_{eq}$不随转子位置变化。

**相域模型优势**

| 特性 | dq0模型 | 相域模型 |
|------|---------|---------|
| 坐标变换 | 需要 | 不需要 |
| 时变电感 | 无 | 需要特殊处理 |
| 不对称工况 | 受限 | 适合 |
| 谐波分析 | 受限 | 准确 |
| 计算效率 | 高 | 中 |

### 6.3 电压Behind-Reactance(VBR)模型

**核心思想**

通过电路等效变换，将电机表示为电压源串联电抗的形式，提高数值稳定性。

**等效电路**

$$
v_{abc} = e''_{abc} - X''_d i_{abc}
$$

其中$e''_{abc}$为次暂态电势，$X''_d$为次暂态电抗。

**VBR模型优势**

- 恒导纳矩阵：等效导纳不随转子位置变化
- 数值稳定性：避免dq模型在EMT中的数值问题
- 接口友好：易于与外部网络直接连接

**dq/abc混合坐标离散化**

1. 内部状态变量使用dq坐标(简化方程)
2. 网络接口使用abc坐标(直接连接)
3. 通过变换矩阵实时转换

### 6.4 异步电机(感应电机)建模

**双笼转子模型**

$$
\begin{bmatrix} v_{ds} \\ v_{qs} \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix} = \begin{bmatrix} R_s & 0 & 0 & 0 & 0 & 0 \\ 0 & R_s & 0 & 0 & 0 & 0 \\ 0 & 0 & R_{r1} & 0 & 0 & 0 \\ 0 & 0 & 0 & R_{r1} & 0 & 0 \\ 0 & 0 & 0 & 0 & R_{r2} & 0 \\ 0 & 0 & 0 & 0 & 0 & R_{r2} \end{bmatrix}\begin{bmatrix} i_{ds} \\ i_{qs} \\ i_{dr1} \\ i_{qr1} \\ i_{dr2} \\ i_{qr2} \end{bmatrix} + \frac{d}{dt}\begin{bmatrix} \psi_{ds} \\ \psi_{qs} \\ \psi_{dr1} \\ \psi_{qr1} \\ \psi_{dr2} \\ \psi_{qr2} \end{bmatrix} + \begin{bmatrix} -\omega\psi_{qs} \\ \omega\psi_{ds} \\ -(\omega-\omega_r)\psi_{qr1} \\ (\omega-\omega_r)\psi_{dr1} \\ -(\omega-\omega_r)\psi_{qr2} \\ (\omega-\omega_r)\psi_{dr2} \end{bmatrix}
$$

**深槽效应(Deep Bar Effect)**

考虑转子导条集肤效应，转子电阻和漏感随转差率变化：

$$
R_r(s) = R_{r0}K_R(s), \quad L_{lr}(s) = L_{lr0}K_L(s)
$$

**转矩方程**

$$
T_e = \frac{3}{2}p(\psi_{ds}i_{qs} - \psi_{qs}i_{ds}) = \frac{3}{2}pL_m(i_{qs}i_{dr} - i_{ds}i_{qr})
$$

### 6.5 通用电机建模范式

**统一建模框架**

各类旋转电机可采用统一的EMT建模框架：

1. **电气方程**：电磁感应定律 + 电路约束
2. **机械方程**：牛顿运动定律
3. **接口方程**：网络连接条件

**状态空间形式**

$$
\dot{x} = Ax + Bu
$$

其中状态变量$x$包括：定子电流/磁链、转子电流/磁链、转子转速、转子位置角。

### 6.6 旋转电机的接口方法

**与EMT网络的接口**

| 接口类型 | 实现方式 | 特点 |
|---------|---------|------|
| 电流源接口 | 向网络注入电流 | 简单，但需迭代 |
| 诺顿等效 | 导纳+电流源 | 标准EMTP形式 |
| VBR接口 | 电压源+电抗 | 数值稳定 |
| 直接嵌入 | 方程联立求解 | 精度高，复杂 |

**多时间尺度接口**

- 电磁暂态(μs-ms)：定子绕组暂态
- 机电暂态(ms-s)：转子运动
- 控制器(ms)：励磁/调速系统

## 适用边界

- dq0模型适合对称工况，相域模型适合不对称和谐波分析
- VBR模型数值稳定性好，但计算量略大
- 双笼模型适合需要精确表示启动特性的场景
- 磁路饱和模型计算复杂，仅在饱和严重时必需
- 实时仿真需采用简化模型或并行计算

## 代表性来源

| 论文 | 年份 | 关联要点 |
|------|------|----------|
| A Voltage-Behind-Reactance Synchronous Machine Model | 2006 | VBR模型在EMTP中的应用，非迭代同步接口技术 |
| [[re-examination-of-synchronous-machine]] | 2007 | 证明dq、相域、VBR三种模型连续域等价性 |
| An Efficient Phase Domain Synchronous Machine Model | 2019 | 恒定等效导纳相域模型，无需人工阻尼绕组 |
| Induction Machine Modeling for Real-Time EMT | 2016 | 实时仿真的感应电机数值优化模型 |
| [[synchronous-machine-exciter-circuit-model-in-a]] | 2013 | MANA公式的相域同步电机模型，直接电气连接 |

## 技术演进脉络

### 1960-1980年代：经典dq模型
- **Park变换确立** (1929, 应用于EMT 1970s)
  - dq0坐标变换成为标准
  - 同步电机标准参数模型
- **EMTP Type-59模型** (1970s)
  - 内置同步电机模型
  - dq坐标 + 数值积分

### 1990-2000年代：相域建模
- **相域模型引入** (1990s)
  - 直接abc坐标建模
  - 适合不对称工况
- **VBR模型发展** (2000s)
  - 电压Behind-Reactance
  - 提高数值稳定性

### 2000-2015年：接口与稳定性
- **非迭代接口** (2006)
  - VBR模型与EMTP网络
  - 避免迭代求解
- **恒定导纳技术** (2010s)
  - 相域模型优化
  - 减少矩阵重新分解

### 2015-2026年：新能源与实时
- **DFIG详细模型** (2015-2020)
  - 双馈感应发电机
  - crowbar、chopper电路
- **PMSM模型** (2018-2026)
  - 永磁同步电机
  - 风电/储能应用
- **实时优化** (2020-2026)
  - 并行计算
  - 模型降阶

## 关键发现汇总

### 模型等价性理论
- **[2007]** dq模型、相域模型、VBR模型在连续时间域数学等价，离散化后表现不同
- **[2019]** 恒定导纳相域模型计算效率与dq模型相当，无需人工阻尼绕组

### 数值稳定性改进
- **[2006]** VBR模型解决dq模型在EMT中的数值稳定性问题
- **[2016]** 感应电机实时模型采用固定步长优化，保证数值稳定性
- **[2019]** 相域模型方程重构实现恒定导纳，避免时变矩阵频繁分解

### 接口技术进步
- **[2013]** MANA公式实现励磁绕组直接电气连接，突破补偿方法拓扑限制
- **[2014]** 非迭代VBR接口减少计算开销，适合大规模系统仿真

### 前沿研究方向
- **磁路饱和精确建模**：交叉饱和效应、动态饱和特性
- **高温超导电机**：新型电机EMT建模
- **模型降阶聚合**：风电场等值建模
- **AI辅助参数辨识**：机器学习电机参数在线辨识

## 深度增强内容

### 1. 电机模型分类体系

| 分类维度 | 类型 | 适用场景 | 计算复杂度 |
|---------|------|---------|-----------|
| 坐标系 | dq0模型 | 对称工况 | O(n) |
| 坐标系 | 相域模型 | 不对称、谐波 | O(n) |
| 坐标系 | VBR模型 | 数值稳定性要求高 | O(n) |
| 转子结构 | 圆柱转子 | 汽轮发电机 | 标准 |
| 转子结构 | 凸极转子 | 水轮发电机 | 考虑凸极效应 |
| 阻尼绕组 | 单阻尼 | 简化分析 | 低 |
| 阻尼绕组 | 双阻尼 | 精确暂态 | 中 |
| 饱和 | 线性模型 | 初步分析 | 低 |
| 饱和 | 饱和模型 | 精确分析 | 高 |

### 2. 关键电机参数

**同步电机典型参数**

| 参数 | 典型值 | 说明 |
|-----|-------|------|
| 额定容量 | 100-1000 MVA | 大型发电机 |
| 同步电抗$X_d$ | 1.0-2.0 pu | d轴同步电抗 |
| 暂态电抗$X'_d$ | 0.2-0.4 pu | d轴暂态电抗 |
| 次暂态电抗$X''_d$ | 0.1-0.25 pu | d轴次暂态电抗 |
| 惯性常数H | 2-8 s | 转动惯量 |
| 阻尼系数D | 0-2 pu | 机械阻尼 |

**感应电机典型参数**

| 参数 | 典型值 | 说明 |
|-----|-------|------|
| 额定功率 | 1 kW - 10 MW | 工业电机 |
| 定子电阻$R_s$ | 0.01-0.05 pu | 小电机较大 |
| 转子电阻$R_r$ | 0.01-0.05 pu | 影响启动转矩 |
| 励磁电感$L_m$ | 2-4 pu | 主磁路电感 |
| 漏感$L_{ls}, L_{lr}$ | 0.1-0.2 pu | 漏磁电感 |

### 3. 模型选择指南

| 应用场景 | 推荐模型 | 关键考量 |
|---------|---------|---------|
| 短路故障分析 | dq0+恒定导纳 | 计算效率 |
| 不对称故障 | 相域模型 | 捕捉负序 |
| 谐波分析 | 相域模型 | 谐波表示 |
| 机电混合仿真 | VBR模型 | 数值稳定性 |
| 实时仿真 | dq0简化模型 | 计算速度 |
| 风电场聚合 | 等值模型 | 规模简化 |

### 4. 饱和建模方法

**开路饱和曲线拟合**

$$
i_f = a\psi_f + b\psi_f^n
$$

**负载饱和交叉磁化**

$$
\psi_d = f_d(i_d, i_q), \quad \psi_q = f_q(i_d, i_q)
$$

**动态饱和**

考虑磁滞和涡流效应的时变饱和模型。

### 5. 模型验证方法

**对比验证**

| 验证类型 | 对比基准 | 误差指标 |
|---------|---------|---------|
| 稳态 | 解析解 | 电压误差<0.1% |
| 暂态 | 实测数据 | 波形匹配度>95% |
| 稳定性 | 特征值分析 | 阻尼比误差<5% |
| 效率 | 实测效率曲线 | 误差<1% |

## 相关方法
- [[state-space-method]] - 旋转电机状态空间建模
- [[nodal-analysis]] - 电机与网络联立求解
- [[coordinate-transformation-model]] - Park/dq0变换
- [[numerical-integration]] - 电机暂态积分方法
- [[synchronous-machine-model]] - 电压Behind-Reactance方法

## 相关模型
- [[synchronous-machine-model]] - 发电机详细模型
- [[induction-machine-model]] - 电动机/负荷模型
- [[dfig-model]] - 双馈感应发电机
- [[pmsm-model]] - 新能源发电
- [[transformer-model]] - 机端变压器

## 相关主题
- [[emt-mathematical-foundation]] - 电机建模数学基础
- [[wind-farm-modeling]] - 风力发电机群
- [[real-time-simulation]] - 电机模型实时化
- [[network-equivalent]] - 电机群等值聚合
- [[co-simulation]] - 机电混合仿真

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自EMT领域学术文献的深度分析*
*支撑书籍第二篇第6章"旋转电机建模"*
