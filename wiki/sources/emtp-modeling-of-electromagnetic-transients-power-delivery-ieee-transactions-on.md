---
title: "EMTP Modeling Of Electromagnetic Transients - Power Delivery, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/17/Meredith - 1997 - EMTP modeling of electromagnetic transients in multi-mode coaxial cables by finite sections.pdf"]
---

# EMTP Modeling Of Electromagnetic Transients - Power Delivery, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `17/Meredith - 1997 - EMTP modeling of electromagnetic transients in multi-mode coaxial cables by finite sections.pdf`

## 摘要

This paper introduces a way of modeling electro- magnetic propagation in conductive materials, termed the method of finite sections. It addresses the issues of modeling frequency-dependent impedances and frequency-dependent coupling of conductors. Its use is demonstrated by application to transient modeling of a multi-mode coaxial cable system in the Electromagnetic Transients Program (EMTP), a situation which currently eludes accurate representation. In addition to its use in modeling coaxial cables, the method is applicable to modeling of overhead lines, pipe-type cables, transformer cores and walls, lightning arrestors and other situations in which sufficient planar or cylindrical symmetry exists. The method provides the only accurate EMTP means of modeling wave propagation in non-linea

## 核心贡献


- 提出有限截面法，在EMTP中精确建模导体内部径向电磁波传播。
- 解决传统模型忽略频率相关阻抗与导体耦合的问题，支持非线性建模。
- 将导体损耗由单频近似改为多频径向传播，提升多模同轴电缆暂态精度。


## 使用的方法


- [[有限截面法|有限截面法]]
- [[π节等效电路|π节等效电路]]
- [[频率相关建模|频率相关建模]]
- [[径向波传播建模|径向波传播建模]]
- [[非线性材料建模|非线性材料建模]]


## 涉及的模型


- [[同轴电缆|同轴电缆]]
- [[架空线路|架空线路]]
- [[管型电缆|管型电缆]]
- [[变压器铁芯|变压器铁芯]]
- [[避雷器|避雷器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[电缆暂态建模|电缆暂态建模]]
- [[导体内波传播|导体内波传播]]
- [[非线性材料建模|非线性材料建模]]


## 主要发现


- 有限截面法能准确捕捉导体中心与护套处的波反射及传播延迟现象。
- 相比传统单频π模型，该方法在宽频带内精确表征导体集肤效应损耗。
- 成功实现多模同轴电缆EMTP暂态仿真，克服了模变换常数假设的局限。



## 方法细节

### 方法概述

有限截面法（Method of Finite Sections）是一种介于传统π节电路模型与有限元分析之间的电磁暂态建模技术。该方法将导体沿径向离散为多个有限体积单元（截面），每个截面独立表征电磁波在导体内部的径向传播特性。通过将导体内部的频变阻抗与耦合效应直接映射为EMTP中的集中参数电路（电阻、电感、电导），并与介电层纵向π节模型级联，实现了对多模同轴电缆、架空线及非线性磁性材料中电磁波传播、集肤效应、波反射及传播延迟的精确时域仿真。该方法摒弃了传统频域扫描与恒定模变换假设，直接在电路拓扑中构建宽带频率响应模型，支持非线性材料（如变压器铁芯、避雷器）的瞬态仿真。

### 数学公式


**公式1**: $$$\eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\varepsilon}}$$$

*介质本征阻抗公式，用于计算任意介质中电磁波传播的固有阻抗特性，是推导导体内部波传播参数的物理基础*


**公式2**: $$$Z_c = \sqrt{\frac{R + j\omega L}{G + j\omega C}}$$$

*含导体损耗的传输线特征阻抗公式，将传统仅含介电损耗的模型扩展至包含导体频变电阻与电感*


**公式3**: $$$R = \frac{N^2 \rho \cdot (\text{length-Along-E})}{\text{Area-Across-E}}$$$

*有限截面电阻计算公式，基于材料电阻率、电场方向长度及垂直截面积，支持非线性电阻率输入*


**公式4**: $$$L = \frac{N^2 \mu_R \mu_0 \cdot (\text{Area-Across-H})}{\text{Length-Along-H}}$$$

*有限截面电感计算公式，基于磁导率、磁场方向长度及垂直截面积，适用于非线性磁化曲线建模*


### 算法步骤

1. 几何离散化：根据导体几何形状（平面或圆柱对称），沿径向将导体划分为多个有限截面体积单元。每个单元的边界严格与电场(E)、磁场(H)及波传播方向正交，形成三维正交网格。

2. 截面尺寸设定：依据目标最高频率的穿透深度（δ）确定截面厚度。为保证高频精度，建议每个穿透深度内至少划分2个截面。截面厚度可随半径增加非均匀调整，以优化计算效率。

3. 参数独立计算：对每个截面独立计算其集中参数。利用电阻公式计算径向电阻R，利用电感公式计算环向电感L。若材料呈非线性，则用动态E/J或B/H曲线替代常数ρ和μ，直接映射为EMTP非线性元件。

4. 电路拓扑构建：在EMTP中替换传统单频串联阻抗支路。将导体截面模型（芯线Lc、护套Ls及对应电阻Rc0、Rs0等）与介电层纵向电感Ld按级联拓扑连接，形成多频导体损耗π节网络。

5. 时域求解与验证：在EMTP中执行暂态仿真，直接捕捉导体中心与护套界面的波反射、径向传播延迟及宽频集肤效应。通过对比模型输出阻抗与解析本征阻抗，验证频响精度与物理一致性。


### 关键参数

- **穿透深度(δ)**: 决定截面划分密度的关键尺度，1个δ对应约6.3个波长

- **截面划分密度**: 推荐≥2个截面/穿透深度以保证阻抗误差收敛至工程可用范围

- **材料参数**: 电阻率ρ、相对磁导率μ_R、真空磁导率μ_0、介电常数ε、电导率σ

- **缩放因子N**: 用于变压器绕组匝数折算或几何比例调整的无量纲系数



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 良导体本征阻抗频响验证 | 针对1平方米平面良导体表面进行有限截面建模。在1个截面/穿透深度划分下，模型阻抗误差为-5.4%，电阻误差+13.8%，电抗误差-29.7%；当划分密度提升至2个截面/穿透深度（约12.6个截面/波长）时，模型能合理复现解析本征阻抗，误差显著收敛。 | 相比传统单频π模型（仅适用于单一频率点），该方法在宽频带内保持物理一致性，避免了频域拟合带来的相位与幅值失真，且无需复杂的模变换矩阵。 |

| 多模同轴电缆EMTP暂态仿真 | 构建包含芯线、介电层及金属护套的多模同轴电缆模型，成功在时域中捕捉到电磁波在导体中心的反射、护套/大地界面的过渡延迟以及径向传播时间。模型直接输出瞬态电压电流波形。 | 克服了J. Marti方法中恒定模变换矩阵假设在电缆系统中的失效问题，无需ARMA拟合或频域扫描预处理，建模复杂度降低且物理意义明确，支持非线性导体直接仿真。 |



## 量化发现

- 在1个截面/穿透深度划分下，有限截面模型阻抗误差为-5.4%，电阻误差+13.8%，电抗误差-29.7%。
- 当划分密度提升至2个截面/穿透深度（对应约12.6个截面/波长）时，模型精度达到工程可用标准，能合理复现良导体本征阻抗。
- 传统π节模型要求每波长至少10个截面以保证精度，而有限截面法通过径向离散，在同等网格数下可覆盖从直流至高频的宽频响应。
- 该方法消除了传统频域扫描法中忽略的导体中心波反射与护套传播延迟效应，时域波形相位误差显著降低。


## 关键公式

### 介质本征阻抗方程

$$$\eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\varepsilon}}$$$

*用于推导导体与介质中电磁波传播的基础特性，是有限截面参数计算的物理起点*

### 有限截面电阻方程

$$$R = \frac{N^2 \rho \cdot (\text{length-Along-E})}{\text{Area-Across-E}}$$$

*在EMTP中直接输入，用于表征导体内部径向电流路径的频变/非线性损耗*

### 有限截面电感方程

$$$L = \frac{N^2 \mu_R \mu_0 \cdot (\text{Area-Across-H})}{\text{Length-Along-H}}$$$

*用于表征导体内部磁场储能及非线性磁化特性，支持变压器铁芯等饱和材料建模*



## 验证详情

- **验证方式**: 解析解对比与EMTP时域仿真验证
- **测试系统**: 1平方米平面良导体表面阻抗模型及多模同轴电缆系统（含芯线、介电层、金属护套）
- **仿真工具**: EMTP (Electromagnetic Transients Program)
- **验证结果**: 通过对比有限截面模型计算阻抗与解析本征阻抗，验证了径向离散策略的有效性。在2个截面/穿透深度下模型精度满足工程要求。EMTP仿真成功再现了多模同轴电缆中的波反射、传播延迟及宽频集肤效应，证明了该方法在无需模变换或频域拟合的情况下，可直接在时域中精确处理频率相关阻抗与非线性导体耦合问题。
