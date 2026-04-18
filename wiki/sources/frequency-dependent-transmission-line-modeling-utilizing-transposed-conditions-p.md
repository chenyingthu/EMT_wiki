---
title: "Frequency-dependent transmission line modeling utilizing transposed conditions - Power Delivery, IEEE Transactions on"
type: source
authors: ['未知']
year: 2001
journal: ""
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/tpwrd.2002.1022812.pdf.pdf"]
---

# Frequency-dependent transmission line modeling utilizing transposed conditions - Power Delivery, IEEE Transactions on

**作者**: 
**年份**: 2001
**来源**: `19、20、21/EMT_task_20/tpwrd.2002.1022812.pdf.pdf`

## 摘要

—Existing phase domain transmission line models are capable of producing highly accurate results for both overhead lines and underground cables. This paper introduces a hybrid line model which gives substantial savings in computation time without loss of accuracy, when one or more circuits of a transmission system are treated as continuously transposed. This is achieved by means of a constant transformation matrix in combination with a reduced-size phase domain line model and a number of single-phase (modal) line models. The calculated examples demon- strate a potential speed increase over a full phase domain model between three and four. If none of the circuits are transposed, the line model degenerates into a full phase domain line model. Index Terms—Electromagnetic transients, multicirc

## 核心贡献


- 提出结合恒定变换矩阵、降阶相域模块与单相模态模型的混合线路建模方法
- 利用连续换位特性实现阻抗矩阵块对角化，大幅降低多回线路仿真计算复杂度
- 在保持非换位部分相域精度的同时，通过模态分解实现换位线路的高效仿真


## 使用的方法


- [[恒定变换矩阵法|恒定变换矩阵法]]
- [[模态分解|模态分解]]
- [[相域建模|相域建模]]
- [[梯形积分法|梯形积分法]]
- [[混合建模|混合建模]]


## 涉及的模型


- [[多回架空线路|多回架空线路]]
- [[地下电缆|地下电缆]]
- [[频率相关输电线路模型|频率相关输电线路模型]]
- [[连续换位线路模型|连续换位线路模型]]
- [[单相模态线路模型|单相模态线路模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[输电线路建模|输电线路建模]]
- [[线路换位处理|线路换位处理]]
- [[计算加速|计算加速]]


## 主要发现


- 混合模型相比全相域模型计算速度提升3至4倍，且未牺牲仿真精度
- 当线路无换位时模型自动退化为全相域模型，保证了算法的通用性
- 通过降阶相域模块精确计及换位与非换位线路间的零序耦合效应



## 方法细节

### 方法概述

本文提出一种混合输电线路模型，旨在利用连续换位特性提升电磁暂态仿真效率。该方法首先对多导体线路的频域阻抗与导纳矩阵应用连续换位平均规则，使其呈现块对角化特征。随后构建恒定实数变换矩阵（基于Clarke变换与单位矩阵组合），将原矩阵解耦为左上角的小规模相域耦合块与对角线上的独立单相模态。相域块保留非换位线路及回路间零序耦合的精确频率特性，采用通用线路模型(ULM)进行有理函数拟合；各模态则采用单相频率相关模型独立处理。时域求解通过梯形积分法生成各模块的诺顿等效电路，最终经变换矩阵重组为相域接口，实现与EMTP类程序的无缝对接，在维持全相域精度的同时大幅降低计算维度。

### 数学公式


**公式1**: $$$$\frac{d\mathbf{V}}{dx} = -\mathbf{Z}\mathbf{I}, \quad \frac{d\mathbf{I}}{dx} = -\mathbf{Y}\mathbf{V}$$$$

*多导体输电线路频域电报方程，定义线路电压电流与串联阻抗矩阵Z、并联导纳矩阵Y的关系。*


**公式2**: $$$$\mathbf{Z}' = \mathbf{T}^{-1}\mathbf{Z}\mathbf{T}, \quad \mathbf{Y}' = \mathbf{T}^{-1}\mathbf{Y}\mathbf{T}$$$$

*恒定变换矩阵T对阻抗和导纳矩阵进行相似变换，实现系统解耦，生成相域块与对角模态矩阵。*


**公式3**: $$$$\mathbf{I}_{eq} = \mathbf{T} \mathbf{G}' \mathbf{T}^{-1} \mathbf{V} + \mathbf{T} \mathbf{I}_{hist}'$$$$

*时域诺顿等效电路组装公式，将相域块与各模态的导纳矩阵G'和历史电流源I_hist'通过变换矩阵T映射回相域，供主机程序调用。*


### 算法步骤

1. 1. 构建多回线路的原始频域串联阻抗矩阵Z与并联导纳矩阵Y，按回路划分3×3子块。

2. 2. 根据连续换位假设应用6条平均规则：对换位回路对角块进行对角/非对角元素平均；对换位与非换位回路间的耦合块按行/列平均；非换位部分保持不变，生成修正后的Z和Y。

3. 3. 构造恒定变换矩阵T：对每个换位回路插入Clarke变换矩阵，对非换位导体插入单位矩阵元素，并按未换位导体、地模、线模顺序重排列。

4. 4. 执行相似变换Z'=T⁻¹ZT与Y'=T⁻¹YT，提取左上角k×k相域耦合块（含未换位线路及零序耦合）与剩余(N-k)个对角模态元素。

5. 5. 频域参数拟合：对相域块采用通用线路模型(ULM)进行12阶有理函数逼近；对每个独立模态采用单相频率相关模型进行12阶矢量拟合，获取传播矩阵H与特征导纳Yc。

6. 6. 时域离散化：利用梯形积分法将频域拟合模型转换为各模块的诺顿等效电路（电导矩阵并联历史电流源）。

7. 7. 模型组装与接口：将相域块与模态的诺顿等效参数通过变换矩阵T线性组合，生成完整的相域诺顿等效模型，输出至EMTP主机程序进行网络求解。


### 关键参数

- **拟合阶数**: 12阶有理函数逼近

- **线路长度**: 50 km

- **变换矩阵类型**: 恒定实数矩阵（基于Clarke变换）

- **积分方法**: 梯形积分法

- **相域模型**: 通用线路模型(ULM)

- **模态模型**: 单相频率相关线路模型



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 双回平行架空线路（一回连续换位，一回未换位/或双回换位） | 在0-2ms及0-20ms时间窗口内，记录线路受端导体3和导体6的暂态电压响应波形。混合模型与全相域ULM模型的计算轨迹完全重合，未出现数值振荡或相位偏移。 | 与全相域ULM模型相比，时域电压波形误差<0.1%（视觉上完全一致），单回换位线路计算速度提升3.5倍，三回换位线路提升9.21倍。 |



## 量化发现

- 计算效率显著提升：基于浮点运算次数(FLOPs)统计，单回换位线路仿真速度提升3.5倍，三回换位线路提升9.21倍。
- 精度无损：混合模型时域电压响应与全相域模型完全一致，频域传播矩阵与特征导纳的12阶有理拟合复数偏差极小，满足工程高精度要求。
- 矩阵降维效果：将原N×N全相域矩阵解耦为k×k相域块与(N-k)个独立单相模态，卷积运算复杂度从O(N²)降至O(k²+(N-k))。
- 通用性验证：当系统中无换位线路时，变换矩阵退化为单位阵，模型自动退化为标准全相域ULM模型，保证算法普适性。


## 关键公式

### 恒定变换解耦方程

$$$$\mathbf{Z}' = \mathbf{T}^{-1}\mathbf{Z}\mathbf{T}, \quad \mathbf{Y}' = \mathbf{T}^{-1}\mathbf{Y}\mathbf{T}$$$$

*用于将连续换位线路的频域阻抗/导纳矩阵转换为块对角形式，分离相域耦合块与独立模态。*

### 时域诺顿等效组装方程

$$$$\mathbf{I}_{eq} = \mathbf{T} \mathbf{G}' \mathbf{T}^{-1} \mathbf{V} + \mathbf{T} \mathbf{I}_{hist}'$$$$

*在EMTP时间步循环中，将解耦后的相域块与模态历史电流源及电导矩阵映射回相域，用于节点电压求解。*



## 验证详情

- **验证方式**: 仿真对比验证（混合模型 vs 全相域ULM基准模型）
- **测试系统**: 50km双回/三回平行架空线路系统（含连续换位配置，一端接理想正序电压源，另一端导体接地）
- **仿真工具**: MATLAB 5.3（频域计算与模型构建）、MatTran（时域暂态仿真）、通用线路模型(ULM)算法
- **验证结果**: 频域参数拟合精度极高，时域暂态电压波形与全相域模型完全重合，无可见偏差。浮点运算统计证实计算复杂度大幅降低，验证了混合模型在保持电磁暂态仿真精度的同时实现3~9倍加速的有效性。
