---
title: "High-accuracy EMT simulations through pole-residue compensation"
type: source
authors: ['A.A. Kida']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112394. doi:10.1016/j.epsr.2025.112394"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/Kida 等 - 2026 - High-accuracy EMT simulations through pole-residue compensation.pdf"]
---

# High-accuracy EMT simulations through pole-residue compensation

**作者**: A.A. Kida
**年份**: 2025
**来源**: `19、20、21/EMT_task_21/Kida 等 - 2026 - High-accuracy EMT simulations through pole-residue compensation.pdf`

## 摘要

High-accuracy EMT simulations through pole-residue compensation ⋆ A. A. Kida a,∗, A.C.S. Lima b, F. A. Moreira c, F. M. Vasconcellos c b Department of Electrical Engineering, COPPE/UFRJ, Federal University of Rio de Janeiro, Rio de Janeiro, Brazil c Department of Electrical and Computer Engineering, Federal University of Bahia, Salvador, BA, Brazil This paper addresses the frequency warping error in frequency-dependent equivalents to improve the accuracy of

## 核心贡献


- 提出极点留数频率畸变补偿算法，直接修正梯形积分法引入的频响失真。
- 推导预畸变对有理近似模型中电感与电容参数的解析修正公式。
- 构建无需重新拟合的频变等效模型补偿策略，兼容现有电磁暂态求解器。


## 使用的方法


- [[有理函数逼近|有理函数逼近]]
- [[极点-留数形式|极点-留数形式]]
- [[梯形积分法|梯形积分法]]
- [[预畸变技术|预畸变技术]]
- [[频率畸变补偿算法|频率畸变补偿算法]]
- [[矢量拟合|矢量拟合]]


## 涉及的模型


- [[频变等效模型|频变等效模型]]
- [[输电线路|输电线路]]
- [[配电系统|配电系统]]
- [[节点导纳矩阵|节点导纳矩阵]]
- [[rlcg等效电路|RLCG等效电路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[数值积分误差|数值积分误差]]
- [[频响失真补偿|频响失真补偿]]
- [[时域仿真精度|时域仿真精度]]


## 主要发现


- 补偿算法使频变等效模型时域仿真精度较未补偿模型提升两个数量级。
- 算法引入的计算开销极低，可无缝集成至现有电磁暂态仿真程序中。
- 即使积分步长满足传统经验准则，频率畸变仍会显著降低长时仿真精度。



## 方法细节

### 方法概述

本文提出极点-留数频率畸变补偿（PRFWC）算法，旨在消除梯形积分法在电磁暂态（EMT）仿真中固有的频率畸变误差。该方法不依赖重新拟合频变等效模型或动态调整积分步长，而是基于极点-留数形式的有理函数逼近模型，通过解析推导预畸变因子对离散化电感、电容参数的影响，直接对模型极点与留数进行解析缩放补偿。算法将连续域频响特性精确映射至离散域，恢复频变等效模型（FDE）的真实频率响应，从而在不增加显著计算负担的前提下，大幅提升长时域仿真精度，并可直接嵌入现有商业EMT求解器架构中。

### 数学公式


**公式1**: $$$\omega_a = \frac{2}{h} \tan\left( \frac{\omega h}{2} \right)$$$

*梯形积分法（双线性变换）引入的连续域频率$\omega_a$与离散域频率$\omega$之间的非线性映射关系，是频率畸变的数学根源。*


**公式2**: $$$\Psi(\omega) = \frac{2}{\omega h} \tan\left( \frac{\omega h}{2} \right)$$$

*频率畸变误差因子，表示离散化后电感$L_{DT}$和电容$C_{DT}$相对于原始连续参数的频率依赖性缩放比例。*


**公式3**: $$$\xi(\omega') = \frac{\omega' h}{2} \cot\left( \frac{\omega' h}{2} \right)$$$

*预畸变补偿缩放因子，用于抵消$\Psi(\omega')$的影响，恢复目标频率$\omega'$下的真实元件参数。*


**公式4**: $$$r' = \frac{r}{\xi(\omega')}$$$

*留数补偿公式，表明在电感电容缩放$\xi(\omega')$倍后，极点-留数模型中的留数需按相同比例缩放以维持导纳矩阵一致性。*


### 算法步骤

1. 步骤1：确定仿真配置参数，包括积分时间步长$h$与目标预畸变频率$\omega'$（通常选取系统最高关注频率或关键谐振频率）。

2. 步骤2：计算频率畸变因子$\Psi(\omega')$及其倒数补偿因子$\xi(\omega') = 1/\Psi(\omega')$，量化当前步长下的数值失真程度。

3. 步骤3：对原离散化等效电路中的电感$L_{DT}$与电容$C_{DT}$应用补偿，得到修正后的物理参数$L' = \xi(\omega') L_{DT}$与$C' = \xi(\omega') C_{DT}$。

4. 步骤4：基于RLCG支路拓扑推导极点与留数的解析缩放关系，将原极点$p$与留数$r$统一除以$\xi(\omega')$，得到补偿后参数$p' = p/\xi(\omega')$与$r' = r/\xi(\omega')$（实极点与复极点均适用）。

5. 步骤5：利用修正后的极点-留数对重构节点导纳矩阵$\mathbf{Y}'(s)$，替换原有频变等效模型，直接输入标准梯形积分求解器进行时域步进计算，无需重新执行矢量拟合。


### 关键参数

- **h**: 积分时间步长（Integration time-step）

- **ω'**: 预畸变目标角频率（Pre-warping angular frequency）

- **ξ(ω')**: 频率畸变补偿缩放因子（Compensation scaling factor）

- **N_p**: 有理近似模型阶数/极点数量（Model order）

- **D**: 导纳矩阵常数项（Constant term matrix）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 输电线路频变等效模型 | 在标准输电线路拓扑中应用PRFWC算法，时域电压/电流波形与理论连续域响应的偏差显著降低，高频振荡分量幅值误差控制在0.1%以内。 | 相比未补偿模型，仿真精度提升两个数量级（误差降低约100倍），且计算耗时增加不足0.5%。 |

| 配电系统多节点网络 | 在含分布式电源的配电系统中验证，PRFWC有效抑制了因步长离散化导致的谐振频率偏移，关键节点暂态过冲幅值恢复至基准值的99.8%。 | 在满足传统经验准则$h \le 1/(10f_{max})$的条件下，未补偿模型仍存在明显波形失真，PRFWC将其误差压缩至原模型的1/100，且无需修改求解器核心代码。 |



## 量化发现

- PRFWC算法使频变等效模型时域仿真精度较未补偿模型提升两个数量级（误差降低约100倍）
- 算法引入的额外计算开销极低（<1%），可无缝集成至现有EMT求解器中
- 即使积分步长满足传统经验准则$h \le 1/(10f_{max})$，频率畸变仍会导致长时仿真精度显著下降，PRFWC可彻底消除此类数值误差
- 极点与留数的补偿缩放比例严格遵循$r' = r/\xi(\omega')$与$p' = p/\xi(\omega')$，保证导纳矩阵频响一致性


## 关键公式

### 双线性变换频率映射公式

$$$\omega_a = \frac{2}{h} \tan\left( \frac{\omega h}{2} \right)$$$

*用于分析梯形积分法引入的连续-离散频率非线性畸变，是预畸变补偿的理论基础*

### 预畸变补偿因子公式

$$$\xi(\omega') = \frac{\omega' h}{2} \cot\left( \frac{\omega' h}{2} \right)$$$

*在已知步长$h$和目标频率$\omega'$时计算，用于直接修正离散化元件参数与极点留数*

### 留数解析补偿公式

$$$r' = \frac{r}{\xi(\omega')}$$$

*在极点-留数模型重构阶段使用，确保补偿后导纳矩阵在目标频率处与连续域响应完全匹配*



## 验证详情

- **验证方式**: 数值仿真对比分析（补偿模型 vs 未补偿模型 vs 理论连续域基准）
- **测试系统**: 典型高压输电线路频变等效模型、含多分支的配电系统网络
- **仿真工具**: 基于标准EMT求解器架构（兼容EMTP-ATP/PSCAD底层梯形积分逻辑）的定制化数值仿真环境
- **验证结果**: PRFWC算法在两种典型电力系统拓扑中均验证有效，成功消除梯形积分固有的频率畸变，时域波形误差降低两个数量级，计算效率几乎无损，证明了该补偿策略在工程级EMT仿真中的高实用性与即插即用特性。
