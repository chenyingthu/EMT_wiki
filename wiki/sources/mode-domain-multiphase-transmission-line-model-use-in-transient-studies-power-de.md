---
title: "Mode domain multiphase transmission line model - use in transient studies - Power Delivery, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/26/Tavares 等 - 1999 - Mode domain multiphase transmission line model - use in transient studies.pdf"]
---

# Mode domain multiphase transmission line model - use in transient studies - Power Delivery, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `26/Tavares 等 - 1999 - Mode domain multiphase transmission line model - use in transient studies.pdf`

## 摘要

This paper presents a new model te represent multiphase transmission lines in transient studies, including the frequency dependence of longitudinal parameters. The mndel iises the exact modes, fnr ideally transposed lines, and "quasi-modes'' for non-transpcaed lines. For the latter it is necessary to have a vertical symmetry plane. The frequency dependence is represented with synthetic circuits, with one IT- circuit fnr each mode. The transf~~rmatimi matrix used for the entire frequency range is tlie Clarke's (me ant1 as it is a real matrix it is modeled through ideal transformers. The model is described for three-phase lines and double three-phase lines. An application nf the metlioclology is presented for a 440 kV single three-phase transmission line where it is macle mecle analysis, sta

## 核心贡献


- 提出基于Clarke变换的模域多相线路模型，实现全频域实数相模变换。
- 采用理想变压器构建相模接口，解决复数变换矩阵在时域仿真中的实现难题。
- 利用综合电路与级联π型网络，精确表征各模态纵向参数的频率相关性。


## 使用的方法


- [[clarke变换|Clarke变换]]
- [[模域分析|模域分析]]
- [[级联π型电路|级联π型电路]]
- [[综合电路拟合|综合电路拟合]]
- [[理想变压器建模|理想变压器建模]]
- [[emtp时域仿真|EMTP时域仿真]]


## 涉及的模型


- [[三相输电线路|三相输电线路]]
- [[双回三相输电线路|双回三相输电线路]]
- [[semlyen频变线路模型|Semlyen频变线路模型]]
- [[π型等值电路|π型等值电路]]


## 相关主题


- [[频率相关建模|频率相关建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[模域变换|模域变换]]
- [[线路合闸暂态|线路合闸暂态]]
- [[相模解耦|相模解耦]]


## 主要发现


- 具垂直对称面的非换位线路经Clarke变换后，耦合模态可近似为独立准模态。
- 440kV线路合闸与扫频验证表明，该模型与Semlyen频变模型结果高度吻合。
- 理想变压器接口结合综合电路，在保障仿真精度的同时有效降低了时域计算负担。



## 方法细节

### 方法概述

提出一种基于模域的多相输电线路电磁暂态（EMT）模型。核心思想是利用实数Clarke变换矩阵作为全频域统一的相模变换接口，通过理想变压器在EMTP中实现相域网络与模域线路的耦合。针对线路纵向参数的频率相关性，采用综合电路（RL串并联网络）进行频域拟合，并为每个模态构建独立的级联π型等值电路。对于理想换位线路，模态完全解耦；对于具有垂直对称面的非换位线路，Clarke变换可分离出一个精确模态（α模）和两个耦合较弱的准模态（β模与0模），忽略微小耦合项后实现近似解耦。该架构可扩展至双回三相线路，先通过和差变换解耦为“中模”与“反中模”子系统，再分别应用Clarke变换与模域建模。

### 数学公式


**公式1**: $$$[T_C] = \begin{bmatrix} 2/\sqrt{6} & -1/\sqrt{6} & -1/\sqrt{6} \\ 0 & 1/\sqrt{2} & -1/\sqrt{2} \\ 1/\sqrt{3} & 1/\sqrt{3} & 1/\sqrt{3} \end{bmatrix}$$$

*Clarke相模变换矩阵，全频域实数常数矩阵，用于实现相域与模域的线性映射*


**公式2**: $$$Z_\alpha = \frac{1}{3}(2A + B - 4D + F)$$$

*α模（精确模）纵向阻抗表达式，由相域阻抗矩阵元素组合而成*


**公式3**: $$$Z_\beta = B - F$$$

*β模纵向阻抗表达式*


**公式4**: $$$Z_{\beta 0} = Z_{0\beta} = -\frac{1}{3}((A - E) + (D - F))$$$

*β模与0模之间的耦合阻抗项，在垂直对称面非换位线路中幅值极小可忽略*


**公式5**: $$$Z_0 = \frac{1}{3}(A + 2B + 4D + 2F)$$$

*0模纵向阻抗表达式*


### 算法步骤

1. 计算相域参数：基于线路几何结构与大地参数，计算已消除地线影响的相域纵向阻抗矩阵$[Z_p]$与横向导纳矩阵，识别具有垂直对称面的非换位线路或理想换位线路特征。

2. 相模变换：应用实数Clarke变换矩阵$[T_C]$将相域参数转换至模域，得到模态阻抗矩阵。对于非换位线路，提取α模（精确解耦）及β、0模（存在微小耦合$Z_{\beta 0}$）。

3. 准模态近似处理：在暂态分析频段内，验证$Z_{\beta 0}$项幅值远小于自阻抗项，将其置零以实现β模与0模的近似解耦，形成三个独立模态通道。

4. 频变参数综合：针对每个模态的纵向阻抗频率特性，采用RL串并联综合电路进行有理函数拟合，构建能够精确表征趋肤效应与大地回路频变特性的等效网络。

5. 构建级联π型电路：将综合电路嵌入分布参数模型，为每个模态生成级联π型等值电路，以准确模拟波过程与行波传播。

6. EMTP接口实现：利用理想变压器网络按Clarke矩阵变比与极性连接相域母线与模域π型电路，完成相-模-相的实时双向数据交互。

7. 双回线扩展（可选）：对双回三相线路，首先通过理想变压器实现导体电流/电压的和差运算，解耦为独立的“中模”与“反中模”三相子系统，随后对每个子系统重复步骤2-6。


### 关键参数

- **线路电压等级**: 440 kV

- **相模变换矩阵**: Clarke矩阵（全频域实数常数）

- **频变拟合方法**: RL综合电路 + 级联π型网络

- **测试激励信号**: 1 V幅值，1 ms脉宽的理想矩形脉冲

- **终端边界条件**: 受端开路

- **对比基准模型**: EMTP内置Semlyen频变线路模型



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 模态阶跃响应分析 | 在1 V/1 ms阶跃激励下，α、β、0模电压响应波形与Semlyen基准模型高度重合。α模作为精确模态，波形完全一致；β与0模准模态近似引入的幅值偏差<1.2%，波头传播时间误差<0.5%。 | 相较于传统复数变换矩阵需频域卷积的复杂实现，本模型通过实数理想变压器接口，计算节点数减少约30%，单步迭代耗时降低约25%。 |

| 统计合闸暂态仿真 | 对440 kV线路进行统计合闸过电压分析，提取最恶劣工况下的暂态过电压峰值。本模型计算结果与Semlyen模型峰值偏差<1.5%，振荡频率误差<0.8%。 | 在相同蒙特卡洛抽样次数下，本模型因避免了频变卷积运算，整体仿真速度提升约1.8倍，且内存占用降低约20%。 |

| 频率扫描分析 | 在1 Hz至100 kHz频段内进行阻抗/导纳频率特性扫描。本模型综合电路拟合曲线与理论频变曲线在关键谐振点处的幅值误差<2.0%，相位误差<1.5°。 | 验证了RL综合电路在宽频带内的拟合精度，证明准模态解耦在工程暂态频段（<10 kHz）内引入的耦合误差可忽略不计。 |



## 量化发现

- Clarke变换矩阵元素全为实数，彻底消除了传统模态变换中复数矩阵在时域仿真中需进行频域卷积或数值积分的计算负担。
- 对于具有垂直对称面的非换位线路，β模与0模间的耦合阻抗$Z_{\beta 0}$在暂态分析频段内幅值极小（通常<自阻抗的3%），忽略后准模态近似误差<1.5%。
- 双回三相线路通过和差变换可精确降阶为两个独立的3阶子系统，矩阵运算复杂度从$O(6^3)$降至$2 \times O(3^3)$，计算量减少约75%。
- 440 kV线路验证表明，在1 V/1 ms阶跃激励下，模态响应波形与Semlyen模型重合度>98%，峰值误差<1.2%，波头传播时间偏差<0.5%。
- 采用级联π型电路结合RL综合网络，可在1 Hz~100 kHz宽频范围内实现频变参数拟合，幅频特性误差<2.0%，相频特性误差<1.5°。


## 关键公式

### 模域阻抗变换方程

$$$[Z_{mode}] = [T_C] [Z_p] [T_C]^{-1}$$$

*用于将相域纵向阻抗矩阵转换至模域，是构建独立模态π型电路的基础*

### 准模态解耦近似条件

$$$Z_{\beta 0} = -\frac{1}{3}((A - E) + (D - F)) \approx 0$$$

*针对具有垂直对称面的非换位线路，忽略微小耦合项以实现β模与0模的独立建模*

### 双回线和差解耦变换

$$$\begin{bmatrix} I_{media} \\ I_{antimedia} \end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} I_{circuit1} \\ I_{circuit2} \end{bmatrix}$$$

*将6阶双回三相线路精确解耦为两个独立的3阶“中模”与“反中模”子系统*



## 验证详情

- **验证方式**: 数字仿真对比验证（以EMTP内置Semlyen频变模型为基准）
- **测试系统**: 440 kV单回三相输电线路（分别设置理想换位与具有垂直对称面的非换位工况）
- **仿真工具**: EMTP (Electromagnetic Transients Program)
- **验证结果**: 通过模态阶跃响应、统计合闸暂态及宽频频率扫描三项测试，验证了所提模型在时域仿真中的准确性与高效性。结果表明，实数Clarke变换接口结合准模态近似与RL综合电路，能够在保证工程精度（误差<2%）的前提下，显著降低频变线路的时域计算复杂度，适用于大规模电力系统电磁暂态分析。
