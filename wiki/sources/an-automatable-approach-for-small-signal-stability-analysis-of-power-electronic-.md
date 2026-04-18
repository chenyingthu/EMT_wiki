---
title: "An Automatable Approach for Small-Signal Stability Analysis of Power Electronic-Based Power Systems Using EMT Companion Circuits"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Delivery;2023;38;4;10.1109/TPWRD.2023.3264296"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/06/Chindu和Kulkarni - 2023 - An Automatable Approach for Small-Signal Stability Analysis of Power Electronic-Based Power Systems.pdf"]
---

# An Automatable Approach for Small-Signal Stability Analysis of Power Electronic-Based Power Systems Using EMT Companion Circuits

**作者**: 
**年份**: 2023
**来源**: `06/Chindu和Kulkarni - 2023 - An Automatable Approach for Small-Signal Stability Analysis of Power Electronic-Based Power Systems.pdf`

## 摘要

—The increasing presence of power electronic (PE) con- trolled devices in power systems has widened the bandwidth of transients to be studied for grid stability. While these transients are normally studied using time-domain simulation (TDS), wide bandwidth linear time-invariant (LTI) state-space models are a useful complement to TDS for diagnostics, controller design and parametric analysis. A general automatable method to compute an LTI sampled-data model of a PE-based circuit is presented in this paper. The proposed method is based on the techniques employed in electro-magnetic-transient (EMT) programs to perform TDS of PE-based circuits. The method uses the building blocks of EMT nodalformulationsuchasconductancematrixofcompanioncircuit and its LU factors computed during TDS, interpolat

## 核心贡献


- 提出基于EMT节点导纳矩阵与LU分解的自动化方法构建LTI采样数据模型
- 复用EMT暂态仿真伴随电路导纳矩阵及历史项实现小信号模型自动提取
- 给出剔除EMT数值离散引入的伪特征值判据确保稳定性分析物理准确


## 使用的方法


- [[伴随电路法|伴随电路法]]
- [[节点分析法|节点分析法]]
- [[梯形积分法|梯形积分法]]
- [[lu分解|LU分解]]
- [[采样数据建模|采样数据建模]]
- [[特征值分析|特征值分析]]
- [[颤振消除校正|颤振消除校正]]


## 涉及的模型


- [[rlc电路|RLC电路]]
- [[buck变换器|Buck变换器]]
- [[并网statcom|并网STATCOM]]
- [[电力电子开关|电力电子开关]]
- [[闭环控制系统|闭环控制系统]]


## 相关主题


- [[小信号稳定性分析|小信号稳定性分析]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[电力电子化电力系统|电力电子化电力系统]]
- [[采样数据建模|采样数据建模]]
- [[状态空间模型|状态空间模型]]
- [[自动化建模|自动化建模]]


## 主要发现


- 成功提取Buck变换器与STATCOM的LTI模型特征值分析结果准确
- 证实部分特征值为EMT数值算法引入的伪模态需通过判据予以剔除
- 验证复用EMT仿真中间数据构建小信号模型的可行性提升自动化程度



## 方法细节

### 方法概述

提出一种基于电磁暂态(EMT)仿真程序内部计算模块的自动化小信号稳定性分析方法。该方法直接复用EMT程序在时域仿真(TDS)中已构建的伴随电路节点导纳矩阵$G$及其LU分解因子、历史项电流源、开关时刻线性插值与颤振消除算法，以及控制系统的离散状态空间模型，构建电力电子(PE)电路的线性时不变(LTI)采样数据模型。通过将各储能元件的历史项电流源直接定义为状态变量，彻底避免了传统连续时间建模中繁琐的独立状态变量筛选与网络拓扑分析。针对PE电路的周期性开关特性，通过计算一个完整基波周期$T$内的状态转移矩阵(STM) $\Phi_T$，并建立明确的判据剔除由数值离散和拓扑依赖引入的伪特征值($\Omega=-1$)，最终通过特征值分析($|\lambda|<1$)实现系统小信号稳定性的自动化、高精度评估。

### 数学公式


**公式1**: $$$G = Y_R + A_C \left(\frac{2C}{h}\right) A_C^T + A_L \left(\frac{h}{2L}\right)^{-1} A_L^T$$$

*EMT伴随电路节点导纳矩阵，由电阻导纳、电容等效导纳和电感等效导纳组成，用于求解节点电压。*


**公式2**: $$$x_{k+1} = A x_k + B u_k$$$

*离散时间状态空间模型，其中状态向量$x_k$由电感和电容的历史项电流源构成。*


**公式3**: $$$A = I - \begin{bmatrix} \frac{h}{2}L^{-1}A_L^T \\ -\frac{4}{h}C A_C^T \end{bmatrix} G^{-1} [A_L \ A_C]$$$

*状态转移矩阵$A$的解析表达式，可直接利用TDS中已计算的$G$的LU分解因子高效求解。*


**公式4**: $$$\lambda = \frac{2}{h}\frac{\Omega-1}{\Omega+1}$$$

*双线性变换公式，用于将离散域特征值$\Omega$映射回连续域特征值$\lambda$，以进行物理意义解释。*


**公式5**: $$$\Phi_T = A_{N-1} A_{N-2} \cdots A_1 A_0$$$

*周期$T$内的状态转移矩阵(STM)，由周期内各开关区间的离散状态矩阵连乘得到，用于小信号稳定性分析。*


**公式6**: $$$\Delta \tau = \frac{\tau(\Delta x_c[4]-\Delta x_{ref}[4]) + (h-\tau)(\Delta x_c[3]-\Delta x_{ref}[3])}{x_{ref}[4]-x_c[4]+x_c[3]-x_{ref}[3]}$$$

*开关时刻扰动$\Delta \tau$的线性化表达式，用于精确计算跨步长开关事件对STM的影响。*


### 算法步骤

1. 步骤1：运行EMT时域仿真(TDS)至系统达到周期性稳态，记录每个仿真步长$h$下的伴随电路导纳矩阵$G$、节点-支路关联矩阵$A_L, A_C$、历史项电流源及LU分解因子。

2. 步骤2：针对每个开关区间，利用公式(6)和(7)直接计算离散状态矩阵$A_i$和$B_i$，复用TDS已计算的$G^{-1}$（通过LU分解），避免重复求逆。

3. 步骤3：处理跨步长开关事件。利用线性插值公式(21)计算开关时刻分数$\tau$，并通过公式(22)线性化计算开关时刻扰动$\Delta \tau$。

4. 步骤4：结合EMT程序内置的颤振消除算法（如半时间步插值或临界阻尼调整），对跨开关时刻的状态跃变进行小信号线性化，建立$\Delta x_4$与$\Delta x_3, \Delta \tau$的线性映射关系。

5. 步骤5：将控制系统（如PID、PLL）离散化为状态空间形式(28)，并通过引入单步延迟接口与网络伴随电路模型耦合，形成完整的闭环系统离散模型。

6. 步骤6：将一个完整周期$T$（共$N$步）内的所有状态转移矩阵按时间顺序连乘，得到周期状态转移矩阵$\Phi_T$。

7. 步骤7：计算$\Phi_T$的特征值。根据判据剔除所有$\Omega=-1$的伪特征值（其数量等于纯电感割集与纯电容回路总数），保留物理动态特征值。

8. 步骤8：进行稳定性判定。若所有保留特征值的模值均严格小于1，则系统小信号稳定；否则不稳定，并可进一步计算参与因子进行模态分析。


### 关键参数

- **h**: EMT仿真固定步长（决定离散化精度与伪特征值位置）

- **T**: 系统基波周期或开关周期（STM计算的时间窗口）

- **N**: 周期T内的仿真步数，满足$T = N h$

- **G**: 伴随电路节点导纳矩阵（核心计算模块，维度为节点数×节点数）

- **Φ_T**: 周期状态转移矩阵（小信号稳定性分析的核心矩阵）

- **Ω**: 离散域特征值（用于直接判断稳定性及识别数值伪模态）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Buck变换器开环/闭环运行 | 验证了所提方法在简单DC-DC拓扑中的适用性。计算得到的连续域特征值与理论解析值完全一致，匹配误差为0%。忽略内部受控开关（二极管）时刻扰动引入的STM计算误差在工程允许范围内（文中指出误差显著性极低，不影响稳定性结论）。 | 相比传统连续时间状态空间建模需手动筛选独立状态变量和分段线性化，本方法直接复用EMT内部矩阵，建模自动化程度提升，且计算复杂度与TDS相当，无额外显著计算负担。 |

| 并网STATCOM闭环控制系统 | 验证了方法在含多时间尺度控制（PLL、电压/电流环）的复杂PE系统中的有效性。成功提取了包含控制延迟和开关插值的LTI采样数据模型，特征值分析准确捕捉了次同步振荡与高频谐振模态。 | 传统频域阻抗法或平均模型法在宽频带下精度受限，本方法基于精确的EMT伴随电路，可覆盖从低频机电振荡到数百Hz电磁暂态的全带宽分析，且无需对非线性控制模块进行近似线性化假设。 |



## 量化发现

- 连续域特征值$\lambda$与离散域特征值$\Omega$通过双线性变换精确匹配，匹配误差为0%，且该性质不受仿真步长$h$影响。
- 离散模型中$\Omega=-1$的特征值数量严格等于原电路中纯电感割集与纯电容回路的总数，可作为自动剔除数值伪模态的定量判据。
- 系统小信号稳定的充要条件为状态转移矩阵$\Phi_T$的所有物理特征值模值严格小于1（$|\lambda_i| < 1$）。
- 忽略内部受控开关时刻扰动对STM计算的误差在典型电力电子电路中可忽略不计，验证了该简化假设在EMT离散框架下的有效性。
- 状态矩阵$A$和$B$的计算完全复用TDS中已分解的$G$矩阵LU因子，额外计算开销趋近于0，实现了与TDS同量级的计算效率。


## 关键公式

### EMT伴随电路离散状态矩阵

$$$A = I - \begin{bmatrix} \frac{h}{2}L^{-1}A_L^T \\ -\frac{4}{h}C A_C^T \end{bmatrix} G^{-1} [A_L \ A_C]$$$

*用于从EMT节点导纳矩阵和拓扑关联矩阵直接构建离散时间状态空间模型，是自动化提取的核心公式。*

### 周期状态转移矩阵(STM)

$$$\Phi_T = A_{N-1} A_{N-2} \cdots A_1 A_0$$$

*用于描述周期性开关电力电子系统在一个完整周期内的小信号状态演化，是特征值稳定性分析的基础。*

### 双线性变换映射公式

$$$\lambda = \frac{2}{h}\frac{\Omega-1}{\Omega+1}$$$

*将离散域计算得到的特征值$\Omega$转换回连续物理域特征值$\lambda$，用于识别系统真实动态模态和剔除$\Omega=-1$伪特征值。*

### 开关时刻扰动线性化公式

$$$\Delta \tau = \frac{\tau(\Delta x_c[4]-\Delta x_{ref}[4]) + (h-\tau)(\Delta x_c[3]-\Delta x_{ref}[3])}{x_{ref}[4]-x_c[4]+x_c[3]-x_{ref}[3]}$$$

*用于精确计算跨仿真步长的外部受控开关事件对状态转移矩阵的修正项，确保小信号模型在开关瞬态的准确性。*



## 验证详情

- **验证方式**: 理论推导验证与EMT伴随电路模型对比分析，结合典型电力电子拓扑的闭环特征值分析
- **测试系统**: Buck DC-DC变换器、并网STATCOM（含PLL及多环控制系统）
- **仿真工具**: ATP-EMTP, PSCAD/EMTDC（文中提及的EMT程序架构及内置算法）
- **验证结果**: 验证表明，所提方法能够完全复用EMT时域仿真的内部计算模块（导纳矩阵、LU分解、历史项），自动化构建高精度的LTI采样数据模型。特征值分析结果与物理系统动态严格一致，成功识别并剔除了数值离散引入的伪模态。方法避免了传统建模中繁琐的拓扑分析和独立状态变量筛选，计算效率与常规TDS相当，为宽频带电力电子系统的小信号稳定性诊断、控制器参数整定和模态分析提供了高效、自动化的理论工具。
