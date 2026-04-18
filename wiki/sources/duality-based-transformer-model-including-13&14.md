---
title: "Duality-Based Transformer Model Including"
type: source
authors: ['未知']
year: 2015
journal: ""
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/TPWRD.2015.2424223.pdf.pdf"]
---

# Duality-Based Transformer Model Including

**作者**: 
**年份**: 2015
**来源**: `13&14/files/TPWRD.2015.2424223.pdf.pdf`

## 摘要

—This paper presents a general method for building equivalent electric circuits of power transformers, including eddy current effects in windings and core. A high-frequency equiva- lent dual model for single- and three-phase transformers with two multilayer windings is derived from the application of the principle of duality. The model is built from elements available in circuit simulation programs, such as Electromagnetic Transients Program (EMTP)–Alternative Transients Program, EMTP-RV, PSCAD, and PSpice. The parameters of the frequency-dependent leakage inductance and winding resistance are computed with analytical formulae obtained from the solution of Maxwell’s equations that are based on the geometrical dimensions and material information. Ideal transformers are utilized to isolate t

## 核心贡献


- 提出基于对偶原理的双侧Cauer等效电路，实现绕组涡流效应的高频精确建模
- 推导基于麦克斯韦方程的解析公式，直接由几何尺寸计算频变漏感与电阻参数
- 利用理想变压器隔离电磁元件并明确物理连接点，模型可直接部署于EMTP等软件


## 使用的方法


- [[对偶原理|对偶原理]]
- [[cauer等效电路|Cauer等效电路]]
- [[解析参数计算|解析参数计算]]
- [[有限元验证|有限元验证]]
- [[理想变压器隔离法|理想变压器隔离法]]


## 涉及的模型


- [[电力变压器|电力变压器]]
- [[单相变压器|单相变压器]]
- [[三相变压器|三相变压器]]
- [[多层绕组|多层绕组]]
- [[频变漏感模型|频变漏感模型]]


## 相关主题


- [[电磁暂态|电磁暂态]]
- [[频率相关建模|频率相关建模]]
- [[涡流效应|涡流效应]]
- [[变压器高频建模|变压器高频建模]]
- [[电路等效|电路等效]]


## 主要发现


- 双侧Cauer模型与单侧模型在宽频范围内电阻与电感特性完全等效，且便于接入电容
- 解析公式计算的频变参数与有限元仿真及实验室实测数据高度吻合，验证了模型精度
- 模型通过理想变压器实现电磁解耦，可直接在EMTP/PSCAD中搭建并高效运行



## 方法细节

### 方法概述

基于对偶原理构建双侧Cauer等效电路，将多层绕组沿径向离散为多个薄层子段。在准静态假设下求解圆柱坐标系磁场扩散方程，获取绕组内部磁场分布。利用磁能守恒推导各子段初始电感，结合邻近效应系数矩阵修正得到频变漏感与绕组电阻的解析表达式。采用1:1理想变压器将磁路元件（电感）与电路元件（电阻、电容）在物理节点处严格解耦，确保连接点符合实际电磁能量流向与安培定律。绝缘层电感与层间/绕组间分布电容由几何尺寸、介电常数与匝数直接计算。铁芯采用传统Cauer电路（中心柱采用背靠背对称离散以降低阶数），油箱在低频下用常规Cauer表示。模型仅使用标准电路元件，可直接部署于EMTP/PSCAD进行DC至MHz级宽频电磁暂态仿真。

### 数学公式


**公式1**: $$$\frac{\partial^2 H}{\partial r^2} + \frac{1}{r}\frac{\partial H}{\partial r} = \mu \sigma \frac{\partial H}{\partial t}$$$

*圆柱坐标系下的磁场扩散方程，用于求解绕组内部低频/直流磁场强度分布，是推导频变参数的物理基础。*


**公式2**: $$$L_k = \frac{2W_{mk}}{I_k^2}$$$

*基于磁能守恒的子段电感计算公式，将各离散层存储的磁能转换为等效低频电感。*


**公式3**: $$$L_{k} = \frac{2 \mu_0 \pi r_{avg} h}{N_{sub}^2} \cdot K_{prox}$$$

*含邻近效应修正的Cauer电路电感公式，$K_{prox}$为邻近效应系数，用于适配双侧拓扑并反映高频涡流分布。*


**公式4**: $$$R_k = \frac{l}{\sigma A_k}$$$

*子段直流电阻计算公式，结合材料电导率与几何截面积确定绕组欧姆损耗。*


**公式5**: $$$L_{ins} = \frac{\mu_0 \pi r_{avg} h}{\ln(r_{out}/r_{in})}$$$

*绝缘层或冷却气道等效漏感公式，表征非导电区域的线性磁阻特性。*


**公式6**: $$$C = \frac{2 \pi \epsilon h N_{turns}^2}{\ln(r_{out}/r_{in})}$$$

*层间/绕组间分布电容公式，基于圆柱电容模型计算高频下主导电压分布的寄生电容。*


### 算法步骤

1. 根据目标暂态频率范围与趋肤深度，将每个绕组层沿径向离散为N个薄层子段（高频需在导体边缘加密，低频可中心加厚以优化阶数）。

2. 在直流/准静态假设下，建立圆柱坐标系中的磁场扩散方程，结合安培环路定律设定内外边界条件，解析求解各子段的轴向磁场强度分布。

3. 计算每个离散子段存储的磁能$W_{mk}$，利用磁能-电感转换公式推导初始低频电感值。

4. 引入邻近效应系数矩阵，对初始电感进行拓扑修正，适配双侧Cauer电路的对称结构（参数减半），准确反映高频涡流引起的磁场畸变。

5. 根据子段几何截面积、长度与材料电导率计算各段电阻，完成绕组频变阻抗参数提取。

6. 利用平均半径、绕组高度与绝缘厚度计算层间/绕组间漏感，结合介电常数与匝数计算分布电容，并按双侧模型均分。

7. 构建双侧Cauer拓扑，通过1:1理想变压器将电感网络与电阻/电容网络在物理节点处隔离连接，确保磁/电能量路径独立且可访问。

8. 接入铁芯Cauer电路（中心柱采用背靠背对称离散）与低频油箱模型，完成全系统等效电路组装，并在EMTP/PSCAD中验证频响特性。


### 关键参数

- **离散子段数**: 依频率优化（慢波前2段，快波前7段）

- **填充系数**: 0.6（考虑圆导线与层间绝缘的实际占空比）

- **材料参数**: 电导率$\sigma$、磁导率$\mu$、介电常数$\epsilon$

- **理想变压器变比**: 1:1（隔离磁/电网络，提供物理连接节点）

- **模型适用频段**: DC ~ 10 MHz

- **双侧模型参数缩放**: 单侧模型参数的一半（因能量对称分流）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| FEM短路阻抗验证 | 双绕组变压器（单层厚4mm）短路工况，频率扫描1Hz~1MHz。模型计算的等效电阻与电感曲线与有限元结果高度重合，准确捕捉涡流引起的频变特性与趋肤/邻近效应。 | 在1Hz~1MHz全频段内，阻抗幅值与相位误差<5%，显著优于忽略涡流的传统集中参数模型（高频误差>30%）。 |

| 实验室1kVA变压器实测对比 | 单层厚1.61mm，采用2阶模型（<10kHz）与7阶模型（~1MHz）。阻抗幅频特性在2MHz内与实测吻合，低频谐振点偏差约20%。 | 2阶模型即可准确预测至1MHz的感性行为；7阶模型在15MHz处呈现单一谐振峰，而2阶模型在2/5/9MHz出现虚假多谐振，验证了高阶离散对超高频的必要性。 |



## 量化发现

- 模型在1 Hz至1 MHz宽频范围内，等效电阻与电感计算误差<5%（对比FEM）。
- 实验室实测谐振频率最大偏差约20%，主要源于绝缘纸介电常数不确定性与制造公差。
- 2阶离散模型可准确覆盖至1 MHz频段；7阶模型将有效预测范围延伸至15 MHz以上。
- 忽略涡流效应时，高频阻抗幅值误差超过30%，证明涡流建模对MHz级暂态至关重要。
- 双侧Cauer模型参数为单侧模型的一半，但物理节点完全暴露，便于直接并联层间电容且不影响磁路精度。
- 中心柱采用背靠背Cauer离散可使等效电路阶数降低约40%，同时保持高频边缘磁通集中特性。


## 关键公式

### 圆柱坐标系磁场扩散方程

$$$\frac{\partial^2 H}{\partial r^2} + \frac{1}{r}\frac{\partial H}{\partial r} = \mu \sigma \frac{\partial H}{\partial t}$$$

*用于求解绕组内部低频/直流磁场分布，是推导频变参数的基础。*

### 磁能-电感转换公式

$$$L_k = \frac{2W_{mk}}{I_k^2}$$$

*根据各离散子段存储的磁能计算初始低频电感值。*

### 绝缘层/气道等效漏感公式

$$$L_{ins} = \frac{\mu_0 \pi r_{avg} h}{\ln(r_{out}/r_{in})}$$$

*计算绕组层间或高低压绕组间非导电区域的线性漏感。*

### 层间/绕组间分布电容公式

$$$C = \frac{2 \pi \epsilon h N_{turns}^2}{\ln(r_{out}/r_{in})}$$$

*基于圆柱电容模型计算高频下起主导作用的寄生电容。*



## 验证详情

- **验证方式**: 有限元仿真(FEM)对比 + 实验室阻抗扫频实测
- **测试系统**: 双绕组单相变压器（绕组厚度4mm）及1kVA实验室单相变压器（层厚1.61mm）
- **仿真工具**: EMTP/EMTP-RV（电路仿真）、有限元分析软件（磁场验证）、实验室阻抗分析仪
- **验证结果**: 模型在DC至MHz频段内与FEM及实测数据高度一致。涡流效应显著改善高频阻抗预测精度；2阶模型适用于10kHz以下慢波前，7阶模型适用于1MHz快波前。谐振频率偏差约20%属材料参数公差合理范围，验证了纯几何/材料解析参数化方法的工程实用性。模型可直接用于电力系统绝缘配合与电力电子高频变压器设计。
