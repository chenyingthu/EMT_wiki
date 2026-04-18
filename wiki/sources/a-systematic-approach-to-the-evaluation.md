---
title: "A Systematic Approach to the Evaluation"
type: source
year: 2005
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/04/tpwrd.2005.855448.pdf.pdf"]
---

# A Systematic Approach to the Evaluation

**年份**: 2005
**来源**: `04/tpwrd.2005.855448.pdf.pdf`

## 摘要

—The inﬂuence of earth stratiﬁcation on overhead power transmission line impedances is investigated in this paper. A systematic comparison of existing approaches is done, while results are also obtained using a ﬁnite-element method formula- tion. A novel numerical integration technique is proposed for the calculation of the inﬁnite integrals involved. Typical single- and double-circuit line conﬁgurations are examined for a combination of layer depths and earth resistivities over a wide frequency range. The inﬂuence of the layer depth is also investigated. Results show signiﬁcant differences from those, corresponding to the case of homogeneous earth. Using the multilayered earth return imped- ances in transient simulations, the transient responses show that differences occur mainly in cases

## 核心贡献


- 提出结合高斯勒让德与拉盖尔法则的数值积分技术高效求解多层大地阻抗无穷积分
- 建立统一的多层大地线路阻抗计算框架系统对比验证经典解析模型与有限元法
- 将多层大地返回阻抗应用于电磁暂态仿真揭示分层大地对不对称故障暂态响应的显著影响


## 使用的方法


- [[有限元法-fem|有限元法(FEM)]]
- [[数值积分-高斯-勒让德-拉盖尔-洛巴托|数值积分(高斯-勒让德/拉盖尔/洛巴托)]]
- [[carson公式|Carson公式]]
- [[频域阻抗计算|频域阻抗计算]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 涉及的模型


- [[架空输电线路|架空输电线路]]
- [[多层大地模型|多层大地模型]]
- [[单回-双回线路|单回/双回线路]]
- [[acsr导线|ACSR导线]]


## 相关主题


- [[电磁暂态分析|电磁暂态分析]]
- [[频率相关建模|频率相关建模]]
- [[非均匀大地建模|非均匀大地建模]]
- [[输电线路参数计算|输电线路参数计算]]
- [[不对称故障暂态响应|不对称故障暂态响应]]


## 主要发现


- 多层大地模型计算的线路阻抗与均匀大地Carson公式结果存在显著差异尤其在低频段
- 暂态仿真表明大地分层主要影响不对称故障零序分量导致电压电流响应显著差异
- 有限元法验证了所提数值积分技术的准确性且计算耗时低于3秒具备高效数值稳定性



## 方法细节

### 方法概述

本文提出一种系统化评估多层大地对架空输电线路阻抗影响的通用计算框架。核心突破在于摒弃传统多层大地模型中依赖的无穷级数近似，转而采用直接数值积分技术求解Carson型大地返回阻抗修正项的复变无穷积分。该方法针对被积函数的数学特性，创新性地组合高斯-勒让德（Gauss-Legendre）、高斯-拉盖尔（Gauss-Laguerre）与洛巴托（Lobatto）求积法则，实现对振荡项与指数衰减项的高效分段积分。计算所得的频域自阻抗与互阻抗矩阵被输入EMTP线路常数（LINE CONSTANTS）子程序，构建频率相关的分布参数线路模型。随后，基于该模型开展电磁暂态仿真，系统对比均匀大地假设与多层大地模型在对称/不对称故障下的电压电流响应差异，并通过有限元法（FEM）场路耦合计算验证解析积分结果的准确性。

### 数学公式


**公式1**: $$$\Delta Z_{ij} = \frac{j\omega\mu_0}{2\pi} \int_0^\infty \frac{e^{-(h_i+h_j)\lambda} \cos(\lambda d_{ij})}{\lambda + \sqrt{\lambda^2 + j\omega\mu_0\sigma_{eq}}} d\lambda$$$

*多层大地返回阻抗修正项通用积分表达式，其中$h$为导线对地高度，$d$为导线水平间距，$\lambda$为积分变量，$\sigma_{eq}$为等效大地电导率函数，用于计算单位长度自阻抗与互阻抗的大地修正分量。*


**公式2**: $$$\delta = \sqrt{\frac{2\rho}{\omega\mu_0}}$$$

*大地趋肤深度（穿透深度）计算公式，用于评估电磁波在分层大地中的衰减范围，是判断何时可忽略分层效应或选择等效均匀大地电阻率的关键物理量。*


**公式3**: $$$P_n(\lambda) = \frac{\lambda - \sqrt{\lambda^2 + j\omega\mu_0\sigma_n} + P_{n+1}(\lambda)e^{-2\lambda t_n}}{\lambda + \sqrt{\lambda^2 + j\omega\mu_0\sigma_n} + P_{n+1}(\lambda)e^{-2\lambda t_n}}$$$

*Nakagawa多层大地模型中的递归反射系数函数，用于逐层计算电磁波在大地界面处的反射与透射效应，$t_n$为第$n$层厚度，$\sigma_n$为第$n$层电导率。*


### 算法步骤

1. 步骤1：识别被积函数中的振荡因子（如$\cos(\lambda d)$）的根。对于互阻抗计算（$d \neq 0$），确定积分区间内振荡项的第一个正根$\lambda_1$。

2. 步骤2：在区间$[0, \lambda_1]$内应用高斯-勒让德（Gauss-Legendre）求积法，以精确捕捉被积函数在积分起点的陡峭下降特征。

3. 步骤3：在后续相邻根之间的区间$[\lambda_k, \lambda_{k+1}]$内应用洛巴托（Lobatto）求积法则，高效处理被积函数的周期性振荡部分。

4. 步骤4：对于自阻抗计算（$d=0$）或无显式振荡根的情况，首先在初始区间$[0, \lambda_{init}]$应用高斯-勒让德法，随后对剩余无穷区间$[\lambda_{init}, \infty)$应用平移高斯-拉盖尔（Shifted Gauss-Laguerre）法处理指数衰减尾项。

5. 步骤5：采用迭代二分策略，每次将初始区间对半分割并向右扩展高斯-勒让德积分范围，计算相邻两次积分结果的绝对差值。当差值小于预设容差（$10^{-6}$）时终止迭代，通常3-4次迭代即可收敛。


### 关键参数

- **频率范围**: 50 Hz 至 1 MHz

- **大地层数**: 2层或3层（底层无限延伸）

- **土壤电阻率组合**: 10 $\Omega\cdot$m, 100 $\Omega\cdot$m, 1000 $\Omega\cdot$m

- **层厚变化范围**: 趋肤深度的10%至150%

- **数值积分容差**: $10^{-6}$

- **计算平台**: Intel Pentium IV 1.7 GHz PC

- **线路长度**: 200 km

- **故障过渡电阻**: 2 $\Omega$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 150kV单回线路双层大地阻抗对比 | 在6种双层大地模型下，计算50Hz-1MHz频段的互阻抗幅值。当第一层与第二层电阻率差异最大时（Case VI），阻抗幅值差异在kHz频段达到峰值。 | 与均匀大地Carson公式相比，阻抗幅值最大偏差达38%，主要影响开关暂态建模精度。 |

| 735kV双回线路三层大地阻抗对比 | 采用Nakagawa与Moghram模型计算三层大地阻抗，并与均匀大地模型对比。三层结构导致电磁场分布更复杂，差异在特定频段显著放大。 | 与均匀大地模型相比，自阻抗与互阻抗幅值差异最高达50%，验证了多层建模的必要性。 |

| FEM场路耦合验证 | 将数值积分结果与有限元法（FEM）直接求解麦克斯韦方程组的结果进行全频段对比。FEM采用10km×10km离散区域与一阶三角形单元，ACSR导线按管状处理。 | 全频段（50Hz-1MHz）内数值积分与FEM结果的相对误差始终小于0.3%，证明直接积分法具备极高的数值稳定性与物理准确性。 |

| 单相接地（SLG）故障暂态仿真 | 在200km线路上模拟末端经2$\Omega$电阻单相接地故障。对比多层大地模型与均匀大地模型的接收端相电压与故障电流波形。 | 暂态电压与电流的峰峰值相对差异最高达55%，零序分量响应显著偏离；而三相接地故障的对称暂态响应差异可忽略不计（<1%）。 |



## 量化发现

- 多层大地模型计算的线路阻抗与均匀大地Carson公式结果存在显著差异，幅值偏差范围在10%至55%之间，峰值差异集中出现在kHz频段。
- 所提直接数值积分算法在Intel Pentium IV 1.7 GHz平台上，完成60组不同电阻率与频率组合的阻抗计算耗时严格小于3秒，计算效率极高。
- 有限元法（FEM）验证表明，数值积分结果与场域直接求解结果的相对误差在全频段内均低于0.3%，满足工程高精度要求。
- 当第一层大地厚度达到趋肤深度的60%-70%时，分层效应对阻抗的影响最小；若第一层电阻率显著高于第二层，暂态过电压最严重。
- 电磁暂态仿真表明，大地分层主要影响零序/地模分量，导致不对称故障（如SLG）下的电压电流峰峰值差异最高达55%，而对称故障下的差异可忽略（<1%）。


## 关键公式

### 多层大地返回阻抗修正项通用积分

$$$\Delta Z_{ij} = \frac{j\omega\mu_0}{2\pi} \int_0^\infty \frac{e^{-(h_i+h_j)\lambda} \cos(\lambda d_{ij})}{\lambda + \sqrt{\lambda^2 + j\omega\mu_0\sigma_{eq}}} d\lambda$$$

*用于计算任意层数大地结构下架空线路单位长度自阻抗与互阻抗的大地返回路径修正量，是频域参数计算的核心。*

### 大地趋肤深度公式

$$$\delta = \sqrt{\frac{2\rho}{\omega\mu_0}}$$$

*用于评估电磁场穿透深度，指导工程人员判断何时可简化为均匀大地模型，或作为选择等效电阻率的实用近似工具。*

### Nakagawa多层反射系数递归式

$$$P_n(\lambda) = \frac{\lambda - \sqrt{\lambda^2 + j\omega\mu_0\sigma_n} + P_{n+1}(\lambda)e^{-2\lambda t_n}}{\lambda + \sqrt{\lambda^2 + j\omega\mu_0\sigma_n} + P_{n+1}(\lambda)e^{-2\lambda t_n}}$$$

*在多层大地模型中逐层向下递归计算界面反射系数，是构建复杂函数$P(\lambda)$并代入积分表达式的理论基础。*



## 验证详情

- **验证方式**: 对比分析（解析模型 vs 有限元法FEM）与电磁暂态时域仿真验证
- **测试系统**: 150kV单回架空线路与735kV双回架空线路（基于希腊公共电力公司与文献实测数据），线路总长200km，采用BPA现场测试配置改编的暂态测试网络
- **仿真工具**: 自定义数值积分程序（MATLAB/C实现）、有限元法（FEM）场求解器、EMTP/ATP（LINE CONSTANTS子程序用于频变参数提取与时域暂态仿真）
- **验证结果**: 数值积分结果与FEM全频段误差<0.3%，验证了算法的数学严谨性；暂态仿真表明，忽略大地分层会在不对称故障中引入高达55%的峰峰值误差，而对称故障误差<1%，充分证明在零序分量主导的暂态分析中必须采用多层大地模型。
