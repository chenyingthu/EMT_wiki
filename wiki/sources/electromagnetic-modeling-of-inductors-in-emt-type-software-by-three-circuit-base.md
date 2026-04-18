---
title: "Electromagnetic modeling of inductors in EMT-type software by three circuit-based methods"
type: source
authors: ['Sadegh', 'Rahimi', 'Pordanjani']
year: 2022
journal: "Electric Power Systems Research, 211 (2022) 108304. doi:10.1016/j.epsr.2022.108304"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/15/Electromagnetic modeling of inductors in EMT-type software by three circuit-based methods_Pordanjani 等_2022.pdf"]
---

# Electromagnetic modeling of inductors in EMT-type software by three circuit-based methods

**作者**: Sadegh, Rahimi, Pordanjani
**年份**: 2022
**来源**: `15/Electromagnetic modeling of inductors in EMT-type software by three circuit-based methods_Pordanjani 等_2022.pdf`

## 摘要

0378-7796/© 2022 Elsevier B.V. All rights reserved. Electromagnetic modeling of inductors in EMT-type software by three Sadegh Rahimi Pordanjani a,*, Jean Mahseredjian a, Mohammed Naïdjate b, Nicolas Bracikowski b, Mircea Fratila c, Afshin Rezaei-Zare d Three distributed circuit-based approaches based on Hopkinson analogy, Buntenbach analogy and duality

## 核心贡献


- 提出基于Hopkinson、Buntenbach和对偶原理的三种分布式电路建模方法
- 将几何空间离散为等效电路，无需新增EMT元件即可复现漏磁、边缘磁通及磁饱和
- 突破集总模型与有限元法局限，实现电感器在大型电网电磁暂态仿真中的高效集成


## 使用的方法


- [[hopkinson类比法|Hopkinson类比法]]
- [[buntenbach类比法|Buntenbach类比法]]
- [[对偶原理|对偶原理]]
- [[分布式电路建模|分布式电路建模]]
- [[二维有限元法|二维有限元法]]
- [[空间网格离散化|空间网格离散化]]


## 涉及的模型


- [[电感器|电感器]]
- [[壳式电感器|壳式电感器]]
- [[磁路模型|磁路模型]]
- [[分布式等效电路|分布式等效电路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[电感器建模|电感器建模]]
- [[磁路等效|磁路等效]]
- [[磁饱和建模|磁饱和建模]]
- [[漏磁与边缘磁通分析|漏磁与边缘磁通分析]]
- [[电路场耦合建模|电路场耦合建模]]


## 主要发现


- 三种分布式模型仿真结果高度一致，且与二维有限元法验证结果吻合，精度显著提升
- 模型无需新增软件元件即可在EMTP中实现，能准确复现短路阻抗与磁饱和非线性特性
- 该方法适用于中低频电磁暂态分析，为大型电网中磁性器件内部行为研究提供高效工具



## 方法细节

### 方法概述

本文提出一种基于空间网格离散化的分布式电路建模方法，将电感器二维几何结构划分为多个等效电路单元，通过Hopkinson类比、Buntenbach类比与对偶原理三种磁-电映射机制构建分布式等效网络。该方法将磁阻、磁导率与磁通路径分别映射为电阻、电容或电感，并利用15段分段线性函数精确表征铁芯磁饱和非线性特性。针对跨越不同材料的混合网格，采用方向性磁导率加权平均算法计算等效参数。模型完全依赖EMT软件内置标准元件（如L-R/L-C互变器、理想变压器）实现磁路与电路的耦合，无需开发新元件或引入虚拟回路，即可在大型电网中高效复现漏磁、边缘磁通及局部饱和等复杂电磁暂态行为，有效弥合了传统集总电路模型与有限元场求解器之间的精度与效率鸿沟。

### 数学公式


**公式1**: $$$R = \frac{1}{C} = \frac{l}{\mu_0 S}$$$

*线性磁路单元等效电阻/电容计算公式，其中l为磁路平均长度，S为截面积，μ0为真空磁导率*


**公式2**: $$$\mu_p = \frac{1}{\mu_0} \frac{B_p - B_{p-1}}{H_p - H_{p-1}}$$$

*基于B-H曲线分段线性化的增量相对磁导率计算，用于表征铁芯非线性饱和特性*


**公式3**: $$$\mu_h = \mu_1 \frac{h_1}{h_1+h_2} + \mu_2 \frac{h_2}{h_1+h_2}$$$

*混合材料网格水平方向等效磁导率加权平均公式，用于处理非均匀材料分布*


**公式4**: $$$\beta_k = \frac{50k - 25}{N W_y W_x}$$$

*磁电耦合元件（互变器/变压器）的分布参数计算，k为网格索引，N为匝数，W为网格尺寸*


### 算法步骤

1. 几何离散化：将电感器二维截面划分为规则网格（如1152个单元），利用垂直对称性缩减计算规模，并定义Type-A（非线性）、Type-B（线性）、Type-C（非线性+耦合）三种基础网格单元。

2. 材料属性映射：为每个网格分配软铁或空气材料，采用15段分段线性B-H曲线表征非线性磁化特性，计算各段增量磁导率μp，并据此生成非线性R、C、L元件的分段斜率参数。

3. 混合网格处理：对跨越不同材料的网格，沿水平与垂直方向分别计算长度加权平均磁导率μh与μv，以准确反映非均匀磁路中的磁通分布。

4. 分布式电路构建：根据所选类比法（Hopkinson/Buntenbach/对偶），将磁阻/磁导映射为电阻/电容/电感，并依据安培环路定律在闭合回路中分配磁动势源，外边界施加诺伊曼条件（移除垂直磁阻）以允许漏磁逸出。

5. 磁电耦合实现：利用EMTP内置标准元件（Type-2 L-R互变器、Type-1 L-C互变器或理想变压器）建立磁路与外部电气回路的接口，严格遵循法拉第电磁感应定律分配感应电动势。

6. 暂态求解配置：在EMT软件中设置时间步长（10μs）与激励源（60Hz正弦电压），联立求解非线性微分代数方程组，输出端口V-I特性与内部磁场强度分布。


### 关键参数

- **网格数量**: 1152个单元

- **时间步长**: 10 μs

- **仿真周期**: 32 ms

- **B-H曲线分段数**: 15段

- **绕组匝数**: 100匝

- **绕组直流电阻**: 0.032 Ω

- **激励电压幅值**: 130 V (无气隙), 200 V (有气隙)

- **铁磁谐振测试电容**: 9.82 μF



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 无气隙铁芯电感器稳态响应 | 施加130V/60Hz正弦电压，HBD分布式电路准确复现稳态电流波形，内部磁场分布与FEM高度一致 | 与FEM对比的归一化均方根误差(nRMSE)为1.13%~1.19%，计算速度提升约30倍 |

| 有气隙铁芯电感器非线性饱和 | 施加200V/60Hz电压，模型精准捕捉气隙边缘磁通与局部磁饱和现象，端口阻抗特性符合预期 | 与FEM对比的nRMSE为1.52%~1.67%，非线性工况下计算速度提升约10倍 |

| 铁磁谐振电磁暂态仿真 | 串联9.82μF电容与100cos(ωt)电压源，HBD电路完整复现非线性谐振波形与电压畸变过程 | 与FEM结果波形偏差仅2%，验证了强非线性暂态下的高保真度 |



## 量化发现

- 三种分布式模型（Hopkinson、Buntenbach、对偶）仿真结果高度一致，与2D FEM验证的归一化均方根误差（nRMSE）均严格小于2%（无气隙1.13%~1.19%，有气隙1.52%~1.67%）。
- 计算效率方面，HBD分布式电路在线性工况下比FEM快约30倍，在非线性饱和工况下快约10倍，且Hopkinson类比法因微分方程最少而速度最快。
- 铁磁谐振暂态仿真中，HBD模型与FEM的波形差异仅为2%，证明其可替代场路耦合迭代法，消除数值延迟。
- 模型仅需1152个网格单元即可实现与FEM（1102~1150个域单元+边界单元）相当的精度，且完全兼容现有EMT软件标准元件库，无需二次开发。


## 关键公式

### Type-2 L-R互变器耦合方程

$$$\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ N & 0 \end{bmatrix} \begin{bmatrix} i_1 \\ i_2 \end{bmatrix} + \begin{bmatrix} 0 & -N \\ 0 & 0 \end{bmatrix} \frac{d}{dt} \begin{bmatrix} i_1 \\ i_2 \end{bmatrix}$$$

*用于Hopkinson类比法中磁路（右侧）与电路（左侧）的分布式接口实现*

### 理想变压器对偶方程

$$$\begin{bmatrix} i_1 \\ v_1 \end{bmatrix} = \begin{bmatrix} 1/N & 0 \\ 0 & N \end{bmatrix} \begin{bmatrix} i_2 \\ v_2 \end{bmatrix}$$$

*用于对偶原理中将磁路节点/网孔方程转换为电路对偶网络，实现磁电变量直接映射*

### 分布式总感应电动势方程

$$$E_{tot} = -\frac{d}{dt} (\phi_1 + 2\phi_2 + 2\phi_3 + \phi_4 + \phi_5 + 2\phi_6 + 2\phi_7 + \phi_8)$$$

*基于法拉第定律，将各网格磁通变化率按绕组匝链关系叠加，计算电感器端口总电压*



## 验证详情

- **验证方式**: 对比仿真验证（分布式电路模型 vs 二维有限元法）
- **测试系统**: 单相壳式电感器（含无气隙与有气隙两种铁芯结构，100匝铜绕组，软铁芯材料）
- **仿真工具**: EMTP 4.1.3（分布式电路求解）, COMSOL Multiphysics 5.4（2D FEM场求解）
- **验证结果**: 三种HBD分布式模型在稳态、非线性饱和及铁磁谐振工况下均与FEM结果高度吻合，端口V-I特性与内部磁场强度误差<2%，计算效率提升10~30倍，验证了其在大型电网电磁暂态仿真中的高精度、强非线性表征能力与工程实用性。
