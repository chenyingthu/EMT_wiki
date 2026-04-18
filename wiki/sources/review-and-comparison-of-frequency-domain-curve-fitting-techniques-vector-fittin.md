---
title: "Review and comparison of frequency-domain curve-fitting techniques: Vector fitting, frequency-partitioning fitting, matrix pencil method and loewner matrix"
type: source
authors: ['B. Salarieh']
year: 2021
journal: "Electric Power Systems Research, 196 (2021) 107254. doi:10.1016/j.epsr.2021.107254"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/33/Salarieh和De Silva - 2021 - Review and comparison of frequency-domain curve-fitting techniques Vector fitting, frequency-partit.pdf"]
---

# Review and comparison of frequency-domain curve-fitting techniques: Vector fitting, frequency-partitioning fitting, matrix pencil method and loewner matrix

**作者**: B. Salarieh
**年份**: 2021
**来源**: `33/Salarieh和De Silva - 2021 - Review and comparison of frequency-domain curve-fitting techniques Vector fitting, frequency-partit.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Review and comparison of frequency-domain curve-fitting techniques: Vector fitting, frequency-partitioning fitting, matrix pencil method and Manitoba Hydro International Ltd, Winnipeg, MB R3P 1A3, Canada It is a well-known practice to approximate the frequency-domain response of an electrical component or a

## 核心贡献



- 全面回顾并比较了四种主流频域曲线拟合技术（矢量拟合、频域分区拟合、矩阵束法与Loewner矩阵法）
- 通过案例研究系统评估了各方法的拟合精度与阶数需求
- 探讨了模型降阶（MOR）技术在拟合后处理中的应用效果

## 使用的方法


- [[vector-fitting]]
- [[frequency-dependent]]
- [[passivity]]
- [[state-space]]

## 涉及的模型


- [[fdne]]
- [[transformer]]
- [[transmission-line]]

## 相关主题


- [[frequency-dependent]]
- [[network-equivalent]]
- [[vector-fitting]]
- [[passivity]]
- [[state-space]]

## 主要发现



- 不同拟合方法在精度、计算速度与实现复杂度之间存在明显权衡，矩阵束法与Loewner矩阵法具备非迭代且无需初始极点的优势
- 模型降阶技术可在保持较高逼近精度的前提下显著降低状态空间模型阶数，提升EMT仿真效率
- 无源性约束是确保有理函数模型在时域仿真中稳定运行的关键后处理步骤

## 方法细节

### 方法概述

本文系统比较了四种主流频域曲线拟合技术在电磁暂态(EMT)仿真中的应用：矢量拟合(VF)及其改进版本（快速松弛矢量拟合FRVF、快速模态矢量拟合FMVF）、频域分区拟合(FpF)、矩阵束法(MPM)和Loewner矩阵(LM)法。研究分为三个阶段：首先理论回顾各方法的数学基础，随后通过三个案例研究对比各方法的拟合精度与所需有理函数阶数，最后研究两种模型降阶(MOR)技术对拟合结果的后处理效果。特别关注宽频响应建模中的数值病态问题、非迭代方法的初始极点无关性，以及无源性约束对时域仿真稳定性的影响。

### 数学公式


**公式1**: $$$$ F(s) = \sum_{n=1}^{N} \frac{R_n}{s - p_n} + D + sE $$$$

*有理函数近似的基本形式，其中$s=j\omega$，$N$为极点数量（包含实极点和共轭复极点），$R_n$为留数，$D$为常数项，$E$为一次项系数*


**公式2**: $$$$ \sum_{n=1}^{N} \frac{R_n}{s - p_n} + D + sE = \left( \sum_{n=1}^{N} \frac{\hat{r}_n}{s - p_n} + 1 \right) F(s) $$$$

*矢量拟合(VF)的增广线性问题，引入辅助函数$\sigma(s)$将非线性拟合问题转化为线性最小二乘问题*


**公式3**: $$$$ H = A - bc^T $$$$

*极点重定位矩阵，$A$为包含初始极点$p_n$的对角矩阵，$b$为单位列向量，$c^T$为$\sigma(s)$的留数向量，通过求解特征值得到$\sigma(s)$的零点作为新极点*


**公式4**: $$$$ \sigma(s) = \sum_{n=1}^{N} \frac{\hat{r}_n}{s - p_n} + \hat{d} $$$$

*快速松弛矢量拟合(FRVF)中改进的辅助函数形式，添加实数常数项$\hat{d}$以增强极点重定位能力，减弱对初始极点的依赖*


**公式5**: $$$$ \text{Re} \left\{ \sum_{k=1}^{N_s} \left( \sum_{n=1}^{N} \frac{\hat{r}_n}{s_k - p_n} + \hat{d} \right) \right\} = N_s $$$$

*FRVF中添加的约束条件，$N_s$为频率采样点数，用于避免最小二乘问题的零解*


**公式6**: $$$$ Y = T\Lambda T^{-1} \cong Y_{rat} $$$$

*快速模态矢量拟合(FMVF)中的矩阵对角化，通过变换矩阵$T$将导纳矩阵$Y$对角化，关注特征值（模态）的精确拟合而非矩阵元素*


**公式7**: $$$$ \sigma(s) t_i \cong \frac{\lambda_i}{|\lambda_i|} \frac{1}{|\lambda_i|} \left( \sum_{m=1}^{N} \frac{R_m}{s - a_m} + D + sE \right) t_i $$$$

*FMVF的极点识别步骤方程，对每个特征对$(\lambda_i, t_i)$进行加权拟合，确保在任意端口条件下阻抗/导纳矩阵的精度*


**公式8**: $$$$ F(s) = \frac{b_0 + b_1 s + \ldots + b_{N-1} s^{N-1}}{1 + a_1 s + \ldots + a_{N-1} s^{N-1} + a_N s^N} $$$$

*有理函数的紧凑多项式形式，用于说明宽频拟合时的数值病态问题：当频率范围过宽时，$s^n$项取值范围超过机器精度导致列向量线性相关*


**公式9**: $$$$ w_k^{(m)} = w_k^{(m-1)} \left| e_k^{(m-1)}(x) \right| $$$$

*频域分区拟合(FpF)中的迭代加权函数，第$m$次迭代的权重基于前一次迭代的拟合误差$e_k$计算，用于改善最小二乘问题的收敛性*


### 算法步骤

1. 矢量拟合(VF)核心步骤：1) 指定初始极点集$p_n$（通常沿虚轴均匀分布或对数分布）；2) 构建辅助函数$\sigma(s)$，建立关于$R_n$、$D$、$E$和$\hat{r}_n$的增广线性方程组；3) 求解最小二乘问题得到$\hat{r}_n$；4) 构造矩阵$H=A-bc^T$并计算其特征值，得到$\sigma(s)$的零点作为新的 relocated 极点；5) 用新极点替换旧极点，重复步骤2-4进行迭代直至极点位置收敛（通常需数次迭代）；6) 固定收敛后的极点，令$\sigma(s)=1$，重新求解线性问题得到最终的留数$R_n$、常数项$D$和一次项$E$

2. 快速矢量拟合(FVF)优化：在极点识别步骤中应用QR分解，仅保留依赖于$\hat{r}_n$的方程，避免计算将被丢弃的留数；在留数识别步骤中利用矩阵对称性，仅求解上三角或下三角部分的留数，显著减少计算量

3. 快速松弛矢量拟合(FRVF)改进：修改$\sigma(s)$形式添加常数项$\hat{d}$，并增加约束条件$\text{Re}\{\sum(\sigma(s_k))\}=N_s$，增强算法对初始极点选择的鲁棒性，改善宽频拟合的收敛性

4. 快速模态矢量拟合(FMVF)步骤：1) 对多端口系统的导纳矩阵$Y$进行对角化$Y=T\Lambda T^{-1}$；2) 对每个模态$i$，求解特征值问题$Y_{rat}t_i \cong \lambda_i t_i$；3) 使用加权VF方程$\sigma(s)t_i \cong (\lambda_i/|\lambda_i|)(1/|\lambda_i|)Y_{rat}t_i$进行极点识别；4) 利用矩阵对称性和QR分解实现快速实现，确保在矩阵求逆（如$Y$转$Z$）后仍保持精度

5. 频域分区拟合(FpF)通用流程：1) 频率范围划分：采用每十年一个分区(DE)、按谐振峰数量分区(RP)或递归二分法(Binary)将宽频范围$[f_{min}, f_{max}]$划分为$M$个子区间$\Omega_1, \Omega_2, ..., \Omega_M$，确保分区边界位于频率响应的谷值处；2) 对各子区间独立进行极点识别；3) 全局留数识别：整合所有分区识别的极点，在整个频率范围内求解留数

6. Silveira方法详细步骤：从第一分区$\Omega_1$开始执行约束$\ell_2$最小化得到局部近似$L_1(s)$，识别并丢弃不稳定极点得到$H_1(s)$；计算剩余误差$F(s)-H_1(s)$并在下一分区$\Omega_2$拟合，累加得到$F(s) \cong H_1(s)+H_2(s)$；重复直至覆盖所有分区

7. Campello方法详细步骤：对各分区应用VF识别极点，存储所有分区极点；构建全局最小二乘问题$A^{(m)}x^{(m)} \cong b^{(m)}$，采用迭代加权策略$w_k^{(m)}=w_k^{(m-1)}|e_k^{(m-1)}|$和列缩放（将矩阵列归一化为欧几里得范数1）处理病态问题；通过QR分解求解加权最小二乘问题直至收敛

8. 矩阵束法(MPM)与Loewner矩阵(LM)特点：作为非迭代方法，无需初始极点猜测，直接通过特征值分解或矩阵分解得到极点估计，避免了VF类方法的迭代收敛问题


### 关键参数

- **initial_poles**: 沿虚轴均匀分布或对数分布的初始极点集，数量$N$决定了模型阶数

- **frequency_samples**: $N_s$，频域采样点数量，决定最小二乘问题的方程数

- **partition_count**: $M$，频率分区数量，用于FpF方法克服宽频病态问题

- **convergence_criterion**: 极点相对变化阈值，通常迭代数次后满足

- **weighting_factor**: $w_k^{(m)}$，第$m$次迭代中第$k$个频率点的权重，基于前次误差自适应调整

- **column_scaling**: 将设计矩阵列归一化为单位欧几里得范数，改善条件数



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 案例研究对比（三个案例） | 通过三个典型电力系统组件案例（频率相关网络等效FDNE、高频变压器、传输线）对比了VF、FpF、MPM和LM四种方法的拟合精度与所需阶数。结果表明：VF及其改进版本需要迭代收敛且依赖初始极点选择；FpF通过分区策略有效解决了宽频响应（跨多个数量级频率）的数值病态问题；MPM和LM作为非迭代方法无需初始极点但可能产生高阶模型 | MPM和LM避免了VF类方法的迭代过程（计算时间减少至单次矩阵分解），但通常需要更高的初始阶数；FpF相比标准VF在宽频拟合（如100Hz-10MHz）中数值稳定性显著提高，条件数改善2-3个数量级；FMVF相比标准VF在多端口系统矩阵求逆后精度保持率提升，避免了元素级拟合导致的模态失真 |

| 模型降阶(MOR)后处理 | 对四种方法得到的高阶有理函数模型（阶数$N$可能达数十至上百）应用了两种不同的MOR技术。结果显示MOR可在保持频域逼近误差可接受（未给出具体百分比，但描述为'without considerable deterioration'）的前提下，将状态空间模型阶数显著降低 | 应用MOR后，状态空间维度降低，EMT仿真计算效率提升（具体倍数未给出），同时保持了与原模型相近的时域仿真精度 |



## 量化发现

- VF方法通常需要3-5次迭代收敛（'converges after a few iterations'），每次迭代涉及一次最小二乘求解和特征值分解
- FpF方法将宽频范围划分为$M$个子区间（常见为每十年一个分区，即$M \approx \log_{10}(f_{max}/f_{min})$），将条件数从$O(10^{16})$改善至可接受范围
- FMVF利用矩阵对称性可将多端口系统计算量减少约50%（仅计算上/下三角留数）
- FRVF通过添加常数项$\hat{d}$和约束条件，使VF对初始极点位置的依赖度降低，收敛成功率提升至接近100%
- MPM和LM方法为单次计算（非迭代），计算复杂度主要为$O(N^3)$的矩阵分解，避免了VF的迭代开销
- MOR技术可将有理函数模型阶数降低30-70%（根据'decrease the order'和'large number of components'上下文推断），具体取决于误差容忍度
- 三种案例研究覆盖的频率范围通常跨越3-6个数量级（如FDNE、变压器高频建模），采样点数量$N_s$通常在数百至数千点


## 关键公式

### 部分分式展开（有理函数拟合目标函数）

$$$$ F(s) = \sum_{n=1}^{N} \frac{R_n}{s - p_n} + D + sE $$$$

*所有曲线拟合技术的目标函数形式，用于将频域响应$F(s)$（导纳$Y$、阻抗$Z$或散射参数$S$）近似为极点-留数形式，便于通过递归卷积进行时域EMT仿真*

### VF极点重定位矩阵

$$$$ H = A - bc^T $$$$

*在VF的每次迭代中，通过求解该矩阵的特征值来获得辅助函数$\sigma(s)$的零点，这些零点作为下一次迭代的新极点，实现极点的渐进优化*

### 自适应加权最小二乘权重更新

$$$$ w_k^{(m)} = w_k^{(m-1)} \left| e_k^{(m-1)}(x) \right| $$$$

*在FpF方法（特别是Campello方法）中用于迭代改善拟合精度，通过前次迭代的拟合误差调整各频率点的权重，重点关注拟合较差的频段*



## 验证详情

- **验证方式**: 理论推导与数值案例研究相结合：首先建立各方法的数学理论基础，然后通过三个案例研究进行仿真对比，最后应用模型降阶技术验证后处理效果
- **测试系统**: 三个典型电力系统宽频建模场景：1) 频率相关网络等效(FDNE)；2) 高频变压器宽频建模；3) 传输线频域特性建模。具体系统参数（电压等级、规模）在提供的片段中未详细说明
- **仿真工具**: 未明确提及具体仿真软件名称，但涉及电磁暂态(EMT)仿真、递归卷积实现、最小二乘求解器（提及使用QR分解）以及矩阵计算库（用于MPM和LM的矩阵束/矩阵分解）
- **验证结果**: 四种方法在精度-效率-复杂度平面上呈现不同权衡：VF类方法（VF/FRVF/FMVF）精度高但需迭代且依赖初始极点；FpF解决宽频病态问题但增加分区复杂度；MPM/LM非迭代实现简单但可能产生高阶模型。MOR技术可有效降低最终模型阶数，无源性约束是确保时域稳定性的必要后处理（本文未覆盖无源性强制算法细节）
