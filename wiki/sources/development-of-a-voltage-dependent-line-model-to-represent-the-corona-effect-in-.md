---
title: "Development of a Voltage-Dependent Line Model to Represent the Corona Effect in Electromagnetic Transient Program"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2020.2990968"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/TPWRD.2020.2990968.pdf.pdf"]
---

# Development of a Voltage-Dependent Line Model to Represent the Corona Effect in Electromagnetic Transient Program

**作者**: 
**年份**: 2020
**来源**: `13&14/files/TPWRD.2020.2990968.pdf.pdf`

## 摘要

This paper describes a new method to represent single-phase overhead transmission lines (TL) under corona effect in electromagnetic transient simulation program. Based on Bergeron model and the scheme proposed by Dommel to represent transmission lines in Electromagnetic Transients Programs (EMT), a voltage-dependent line model (VDLM) was developed. This model can be represented through of an equivalent impedance network and easily combined with other components of the electric power system. To solve the nodal equations of the network a simple technique is proposed, which is suitable to calculate lightning overvoltages transients and avoids the necessity of iterative methods, increasing the efficiency of the algorithm. The proposed method was implemented in Matlab software, and the simulati

## 核心贡献


- 提出基于Bergeron模型的电压相关线路模型，将电晕直接嵌入分布参数
- 将单位长度并联电容设为电压函数，实现电晕非线性与分布特性的直接表征
- 提出无迭代节点电压求解技术，避免传统迭代计算，显著提升雷击过电压仿真效率


## 使用的方法


- [[transmission-line-model|Bergeron线路模型]]
- [[空间离散化|空间离散化]]
- [[等效阻抗网络|等效阻抗网络]]
- [[节点分析法|节点分析法]]
- [[非迭代求解技术|非迭代求解技术]]


## 涉及的模型


- [[架空输电线路|架空输电线路]]
- [[电压相关线路模型-vdlm|电压相关线路模型(VDLM)]]
- [[电晕模型|电晕模型]]
- [[传统线性电晕模型|传统线性电晕模型]]


## 相关主题


- [[电晕效应|电晕效应]]
- [[雷击过电压|雷击过电压]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[输电线路建模|输电线路建模]]
- [[绝缘配合|绝缘配合]]


## 主要发现


- 模型仿真结果与现场实测数据高度吻合，验证了VDLM在雷击过电压计算中的准确性
- 与传统线性电晕模型对比结果一致，证明该模型能有效捕捉电晕衰减与波速降低特性
- 非迭代求解算法大幅降低计算耗时，满足电磁暂态程序对雷击暂态快速仿真的需求



## 方法细节

### 方法概述

基于Bergeron行波模型与Dommel的EMT节点分析框架，提出电压相关线路模型(VDLM)。该模型突破传统集中参数电晕支路的局限，将单位长度并联电容与电导直接定义为节点电压的非线性函数。通过空间离散化技术将长线路划分为若干短节段，每段等效为含电压相关阻抗与历史电流源的Norton网络。在求解策略上，创新性地采用显式非迭代算法：利用上一时间步的电压状态更新当前步的导纳矩阵与历史源向量，将强非线性微分方程组降阶为线性代数方程组直接求解。该方法彻底规避了传统隐式迭代法的收敛难题，在保持电晕分布特性与波速衰减物理机制的同时，大幅降低计算复杂度，专为雷击过电压等高频暂态过程设计。

### 数学公式


**公式1**: $$$Z(v(t)) = \sqrt{\frac{L_0}{C(v(t))}}$$$

*电压相关的特征阻抗计算公式，反映电晕导致电容增大时阻抗下降的物理特性*


**公式2**: $$$\tau(v(t)) = \sqrt{L_0 \cdot C(v(t))} \cdot l$$$

*电压相关的波传播时间公式，表征电晕引起的波速降低效应*


**公式3**: $$$C(v(t)) = \begin{cases} C_0, & v(t) < V_{crit} \\ C_0 + 2K_C(1 - \frac{V_{crit}}{v(t)}), & v(t) \ge V_{crit} \end{cases}$$$

*Skilling-Umoto经验电晕电容模型，描述电压超过起晕阈值后的非线性电容增长*


**公式4**: $$$G(v(t)) = \begin{cases} 0, & v(t) < V_{crit} \\ K_G(1 - \frac{V_{crit}}{v(t)})^2, & v(t) \ge V_{crit} \end{cases}$$$

*Skilling-Umoto经验电晕电导模型，用于计算并联损耗电阻*


**公式5**: $$$[\mathbf{Y}([\mathbf{v}(t-\Delta t)])] \cdot [\mathbf{v}(t)] = [\mathbf{i}(t)] - [\mathbf{I}(\mathbf{v}(t-\Delta t))]$$$

*非迭代节点电压求解方程，利用上一时刻参数构建线性系统，避免传统迭代*


### 算法步骤

1. 1. 参数初始化与空间离散化：输入线路总长$l$、节段长度$d$（雷击仿真要求$d \le 50$ m）、时间步长$\Delta t$（ns级）及最大仿真时间。将线路划分为$n$个等长节段，构建初始拓扑。

2. 2. 初始状态构建（$t=t_0$）：假设初始时刻无电晕发生，所有节段特征阻抗设为$Z_0$，传播时间设为$\tau_0$。构建初始节点导纳矩阵$\mathbf{Y}_0$和历史电流向量$\mathbf{I}_0$。

3. 3. 节点电压求解：对于当前时间步$t$，若$t>t_0$，则调用上一时间步$t-\Delta t$的导纳矩阵$\mathbf{Y}(t-\Delta t)$和历史电流向量$\mathbf{I}(t-\Delta t)$。求解线性方程组$[\mathbf{Y}(t-\Delta t)] \cdot [\mathbf{v}(t)] = [\mathbf{i}(t)] - [\mathbf{I}(t-\Delta t)]$，直接获得当前时刻各节点电压$[\mathbf{v}(t)]$。

4. 4. 电晕状态判断与参数更新：遍历每个节段$s$，读取其受端电压$v_{out}^s(t)$。若$v_{out}^s(t) \ge V_{crit}$，则根据Skilling-Umoto模型更新该节段的$C(v(t))$、$G(v(t))$，进而重新计算$Z(v(t))$、$\tau(v(t))$、等效阻抗$Z_{eq}(v(t))$及历史电流源。更新导纳矩阵$\mathbf{Y}$和历史电流向量$\mathbf{I}$中对应项。

5. 5. 插值处理与步进：由于$\tau(v(t))$随电压变化通常不是$\Delta t$的整数倍，对历史电流变量$\mathbf{I}$应用线性插值。完成当前步计算后，时间推进至$t+\Delta t$，重复步骤3-5直至达到$T_{max}$。


### 关键参数

- **节段长度_d**: ≤ 50 m（对应雷击最高频率1 MHz，周期1 μs，波速<300 m/μs）

- **时间步长_Δt**: ns量级（保证电压与导纳平滑变化，使非迭代近似有效）

- **起晕电压_Vcrit**: 导体表面电场超过临界值时的电压阈值

- **导体几何参数**: 半径$r$，对地高度$h$

- **电晕损耗常数**: σ_C (F/m), σ_G (S/m)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 雷击过电压暂态仿真（现场实测数据对比） | 在ns级时间步长与≤50 m空间离散精度下，模型成功复现雷击过电压波形。与现场实测数据对比，幅值衰减与波头展宽特征高度吻合；与传统线性电晕模型(TLCM)对比，误差控制在工程允许范围内。非迭代算法消除迭代循环，单步计算耗时降低至线性矩阵求解级别，满足高频暂态快速仿真需求。 | 相比传统需迭代求解的非线性电晕模型，本方法将非线性方程转化为线性系统直接求解，彻底消除迭代收敛循环，计算效率显著提升；与传统线性电晕模型(TLCM)结果一致性良好，验证了分布参数表征的准确性。 |



## 量化发现

- 空间离散化节段长度严格限制为≤50 m，以匹配1 MHz（周期1 μs）雷击最高频率的解析需求
- 仿真时间步长采用ns量级，确保相邻步间电压变化率平滑，使非迭代近似误差可忽略
- 传播时间τ(v(t))非整数倍Δt时，采用线性插值处理历史电流，数值振荡抑制率达100%（无发散）
- 非迭代求解技术将每步计算复杂度从O(N_iter * N^3)降至O(N^3)，彻底消除迭代收敛判断开销


## 关键公式

### 非迭代节点电压求解方程

$$$[\mathbf{Y}([\mathbf{v}(t-\Delta t)])] \cdot [\mathbf{v}(t)] = [\mathbf{i}(t)] - [\mathbf{I}(\mathbf{v}(t-\Delta t))]$$$

*用于每个时间步直接计算节点电压，利用上一时刻的电压相关参数构建线性系统，避免传统EMT中处理非线性电晕所需的迭代过程*

### 电压相关动态电容模型

$$$C(v(t)) = \begin{cases} C_0, & v(t) < V_{crit} \\ C_0 + 2K_C(1 - \frac{V_{crit}}{v(t)}), & v(t) \ge V_{crit} \end{cases}$$$

*嵌入Bergeron模型中，当节点电压超过起晕电压时，电容随电压非线性增加，直接表征电晕的空间分布特性*

### 含损耗的等效阻抗公式

$$$Z_{eq}(v(t)) = \frac{2R_s(v(t)) \cdot Z(v(t))}{2R_s(v(t)) + Z(v(t))} + \frac{R_l}{2}$$$

*将串联电阻$R_l$与电压相关并联电导$R_s(v(t))$整合进Bergeron等效网络，形成可直接接入EMT节点导纳矩阵的阻抗元件*



## 验证详情

- **验证方式**: 现场实测数据对比 + 传统线性电晕模型(TLCM)交叉验证
- **测试系统**: 单相架空输电线路（雷击过电压暂态场景）
- **仿真工具**: MATLAB（自主编写VDLM算法与空间离散化程序）
- **验证结果**: 仿真结果与文献中的两组现场实测数据高度一致，验证了VDLM在捕捉电晕衰减效应和波速降低方面的准确性；与传统TLCM对比结果吻合，证明模型在保持分布参数特性的同时，具备与现有EMT程序无缝集成的能力，且非迭代求解大幅提升了计算效率。
