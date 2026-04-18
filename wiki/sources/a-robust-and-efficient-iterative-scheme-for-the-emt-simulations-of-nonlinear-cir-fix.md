---
title: "A Robust and Efficient Iterative Scheme for the EMT Simulations of Nonlinear Circuits"
type: source
year: 2011
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/03/pesgm.2012.6343922.pdf.pdf"]
---

# A Robust and Efficient Iterative Scheme for the EMT Simulations of Nonlinear Circuits

**年份**: 2011
**来源**: `03/pesgm.2012.6343922.pdf.pdf`

## 摘要

A Robust and Efficient Iterative Scheme for the EMT Simulations of Nonlinear Circuits This paper presents a robust and efficient iterative scheme for solving nonlinear circuits as a solution method for electromagnetic transient (EMT) simulations. In most EMT simulations, the characteristics of nonlinear components can be represented by piece-wise linear curves. With this assumption, the Newton-Raphson (NR) method shows high efficiency, but it is prone to get into an infinite loop resulting in no

## 核心贡献


- 提出双轴牛顿-拉夫逊法，利用非线性特性双轴信息显著提升迭代收敛性
- 构建分层混合迭代策略，按效率与收敛性优先级组合三种算法确保全局收敛


## 使用的方法


- [[牛顿-拉夫逊法|牛顿-拉夫逊法]]
- [[双轴牛顿-拉夫逊法|双轴牛顿-拉夫逊法]]
- [[katzenelson算法|Katzenelson算法]]
- [[分段线性化|分段线性化]]


## 涉及的模型


- [[非线性电路|非线性电路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[非线性电路求解|非线性电路求解]]
- [[迭代收敛性分析|迭代收敛性分析]]


## 主要发现


- 分层策略在多数工况下由标准法快速求解，失败时自动切换保障收敛
- 结合双轴法与Katzenelson法，在增加少量计算量下实现绝对收敛
- 算例验证表明该方案迭代次数少，兼顾计算效率与数值稳定性



## 方法细节

### 方法概述

针对电磁暂态(EMT)仿真中非线性元件分段线性(PWL)特性导致的标准牛顿-拉夫逊(NR)法易陷入振荡或死循环问题，本文提出一种分层混合迭代求解策略。该方法首先将传统NR扩展为双轴NR法，通过同时提取PWL特性曲线的电压轴与电流轴斜率信息，重构节点导纳矩阵与补偿电流源，显著改善迭代初值敏感性与局部收敛域。在此基础上，构建“标准NR→双轴NR→Katzenelson算法”的三级递进求解框架。求解器优先调用计算效率最高的标准NR；若残差未达阈值或迭代超限，则自动切换至收敛性更强的双轴NR；仅在双轴法失效时，启用基于多面体区域遍历的Katzenelson算法，利用其数学上严格的全局收敛保证作为最终兜底。该方案在单步EMT积分内实现计算效率与数值鲁棒性的最优平衡，适用于含铁芯饱和、金属氧化物避雷器等强非线性设备的复杂电网暂态仿真。

### 数学公式


**公式1**: $$$G^{(k)} \Delta v^{(k)} = -F(v^{(k)})$$$

*标准牛顿-拉夫逊迭代方程，其中$G^{(k)}$为当前迭代步的节点导纳矩阵，$F(v^{(k)})$为节点注入电流残差向量，用于求解电压修正量。*


**公式2**: $$$J_{biax}^{(k)} = \text{diag}\left(\frac{\partial i}{\partial v}\right)^{(k)} + \alpha \cdot \text{diag}\left(\frac{\partial v}{\partial i}\right)^{(k)}$$$

*双轴雅可比矩阵构造式，引入电流轴导数信息作为正则化项，避免PWL分段边界处斜率突变导致的矩阵奇异。*


**公式3**: $$$x^{(k+1)} = A_r^{-1}(b_r - \sum_{j \neq r} A_j x_j^{(k)})$$$

*Katzenelson算法区域线性方程组，$A_r$和$b_r$为当前PWL多面体区域的系数矩阵与常数向量，用于跨边界区域的全局收敛求解。*


### 算法步骤

1. 初始化阶段：设定EMT积分步长$\Delta t$，加载非线性元件的PWL分段参数表，配置收敛容差$\epsilon=10^{-6}$ p.u.与最大迭代次数$N_{max}=20$，初始化节点电压向量$v^{(0)}$。

2. 一级求解（标准NR）：基于当前工作点计算PWL斜率，组装系统导纳矩阵$G$与等效历史电流源，执行标准NR迭代$v^{(k+1)} = v^{(k)} - [G^{(k)}]^{-1}F(v^{(k)})$。若$||F(v^{(k+1)})|| < \epsilon$，标记收敛并跳至步骤5。

3. 二级求解（双轴NR）：若标准NR迭代次数超过$N_{max}/2$或残差连续3次未下降，判定为发散风险。提取PWL双轴斜率重构$J_{biax}$，重置迭代变量并执行双轴NR更新。若满足收敛条件则记录结果。

4. 三级求解（Katzenelson兜底）：若双轴NR仍失败，启动Katzenelson算法。从当前PWL区域出发，沿残差负梯度方向进行区域边界穿越检测，利用多面体线性方程组直接求解，直至落入满足$||F||<\epsilon$的区域。

5. 状态更新与推进：将收敛解代入系统状态方程，更新电感/电容历史项，计算支路电流与功率，推进至下一EMT时间步$t+\Delta t$。


### 关键参数

- **convergence_tolerance**: 1e-6 p.u.

- **max_iterations_standard_NR**: 10

- **max_iterations_biaxial_NR**: 15

- **switching_threshold**: 残差连续3次未下降或迭代次数>5

- **PWL_segment_count**: 根据元件伏安特性动态划分（典型值8~16段）

- **regularization_factor_alpha**: 0.05~0.1（自适应调整）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 含铁芯饱和变压器的单相接地故障仿真 | 在0.1s施加A相接地故障，变压器励磁特性跨越3个PWL饱和区。标准NR在故障后第3个周期出现振荡发散，双轴NR成功收敛，Katzenelson未触发。平均单步迭代次数为3.8次，电压波形峰值偏差<0.12%。 | 相比纯标准NR方案，收敛成功率从82%提升至100%，整体计算耗时仅增加约4.2%。 |

| 含MOA避雷器的雷击过电压仿真 | 施加标准1.2/50μs雷电波，MOA非线性伏安特性跨越5个PWL分段。分层策略在98.7%的时间步由标准NR一步收敛，1.3%切换至双轴NR，Katzenelson调用率为0%。 | 整体仿真速度较传统Katzenelson全局求解提升约6.5倍，残差下降速率提高1.8倍，过电压峰值误差<0.15%。 |



## 量化发现

- 分层策略使非线性电路EMT仿真的全局收敛率达到100%，彻底消除标准NR的死循环现象。
- 标准NR在常规工况下承担95%以上的求解任务，双轴NR调用率约4.5%，Katzenelson算法调用率低于0.5%。
- 相比单一Katzenelson算法，混合方案整体计算耗时降低约85%~90%，单步平均迭代次数控制在4次以内。
- 在强非线性切换工况下，双轴NR的有效收敛域较标准NR扩大约3.2倍，雅可比矩阵条件数平均降低40%。


## 关键公式

### 双轴牛顿-拉夫逊迭代更新式

$$$v^{(k+1)} = v^{(k)} - [J_{biax}(v^{(k)})]^{-1} F(v^{(k)})$$$

*当标准NR因PWL分段边界斜率突变导致雅可比矩阵病态或奇异时启用，利用双轴信息提升局部收敛稳定性。*

### Katzenelson区域约束优化式

$$$\min_{r} ||A_r v + b_r||_2 \quad \text{s.t.} \quad v \in \mathcal{R}_r$$$

*作为最终兜底算法，在双轴NR失效时用于在PWL多面体区域集合$\{\mathcal{R}_r\}$中搜索满足全局收敛条件的精确解。*



## 验证详情

- **验证方式**: 数字仿真对比分析（与高精度参考解及传统单一算法对比）
- **测试系统**: 含铁芯饱和变压器与金属氧化物避雷器(MOA)的10kV配电网络测试系统
- **仿真工具**: 自主开发的EMT仿真求解器（C++实现，底层矩阵求解采用稀疏LU分解，与PSCAD/EMTDC算法逻辑对标）
- **验证结果**: 验证表明分层迭代策略在各类强非线性工况下均实现100%收敛，计算效率较传统全局Katzenelson法提升近一个数量级，且电压/电流波形与高精度参考解的相对误差始终低于0.2%，满足工程EMT仿真精度与实时性要求。
