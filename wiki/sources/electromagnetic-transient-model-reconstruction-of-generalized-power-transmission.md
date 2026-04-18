---
title: "Electromagnetic Transient Model Reconstruction of Generalized Power Transmission Lines Based on Time-Synchronized Waveform Measurements"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Access;2025;13; ;10.1109/ACCESS.2025.3617222"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/16/Gomez - 2025 - Electromagnetic Transient Model Reconstruction of Generalized Power Transmission Lines Based on Time.pdf"]
---

# Electromagnetic Transient Model Reconstruction of Generalized Power Transmission Lines Based on Time-Synchronized Waveform Measurements

**作者**: 
**年份**: 2025
**来源**: `16/Gomez - 2025 - Electromagnetic Transient Model Reconstruction of Generalized Power Transmission Lines Based on Time.pdf`

## 摘要

Thanks to the novel technology of waveform measurement units (WMUs), it is now possible to record time-synchronized waveforms (synchro-waveforms) at different power system locations. Lever- aging these new opportunities, this paper introduces a method for accurate wideband measurement-based reconstruction of single- and three-phase frequency-dependent transmission line models for electromagnetic transient (EMT) studies. This method also accommodates hybrid (overhead-underground) systems and lon- gitudinal parameter variations (nonuniformities). A 2-port line model is generated across a broad frequency spectrum using WMU terminal recordings and the numerical Laplace transform. For single-phase uniform lines, one transient recording set is sufficient for model reconstruction; this extends to

## 核心贡献


- 基于WMU同步波形数据，提出宽频输电线路电磁暂态模型重构方法
- 结合数值拉普拉斯变换与最小范数最小二乘法，求解非均匀线路二端口导纳模型
- 突破横向对称限制，实现含纵向参数变化的单相及三相线路高精度黑盒建模


## 使用的方法


- [[数值拉普拉斯变换|数值拉普拉斯变换]]
- [[二端口导纳模型|二端口导纳模型]]
- [[最小范数最小二乘法|最小范数最小二乘法]]
- [[黑盒建模|黑盒建模]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[混合架空-电缆线路|混合架空-电缆线路]]
- [[频率相关模型|频率相关模型]]
- [[二端口线路模型|二端口线路模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[测量驱动建模|测量驱动建模]]
- [[宽频建模|宽频建模]]
- [[线路模型重构|线路模型重构]]


## 主要发现


- ATP仿真验证表明，重构模型在均匀、混合及非均匀线路中均能精确复现宽频暂态响应
- 详细分析了噪声、采样分辨率及互感器误差对重构精度的影响，证实方法具备工程鲁棒性
- 仅需单组暂态录波即可完成单相均匀线路重构，多组独立数据可解算复杂非对称线路



## 方法细节

### 方法概述

本文提出一种基于波形测量单元（WMU）时间同步波形数据的宽频输电线路电磁暂态（EMT）黑盒模型重构方法。该方法首先利用数值拉普拉斯变换（NLT）将线路两端同步采集的时域电压/电流波形转换至复频域。针对单相均匀或理想换位三相线路，仅需一组暂态录波即可直接解析求解对称二端口导纳矩阵；针对非均匀线路、非换位三相线路或混合架空-电缆系统，则通过引入多组线性独立的暂态录波构建超定方程组，并采用最小范数最小二乘法（MNLS）求解导纳矩阵元素。为克服数据共线性导致的数值不稳定，引入皮尔逊相关系数（阈值<0.8）筛选有效录波数据集。最终重构的频域导纳模型可通过逆数值拉普拉斯变换（INLT）或矢量拟合（FDNE）直接用于EMT仿真，无需预先知晓线路几何参数或终端边界条件，实现了对纵向参数变化及横向不对称性的自适应建模。

### 数学公式


**公式1**: $$$\begin{bmatrix} I_S(s) \\ I_R(s) \end{bmatrix} = \begin{bmatrix} A(s) & B(s) \\ B(s) & A(s) \end{bmatrix} \begin{bmatrix} V_S(s) \\ V_R(s) \end{bmatrix}$$$

*单相均匀线路对称二端口导纳模型，描述复频域下两端电压与电流的线性关系*


**公式2**: $$$\begin{bmatrix} A(s) \\ B(s) \end{bmatrix} = \begin{bmatrix} V_S(s) & V_R(s) \\ V_R(s) & V_S(s) \end{bmatrix}^{-1} \begin{bmatrix} I_S(s) \\ I_R(s) \end{bmatrix}$$$

*对称二端口导纳矩阵元素的直接解析解，适用于仅需一组录波的均匀/换位线路*


**公式3**: $$$\begin{bmatrix} I^{T_1} \\ I^{T_2} \\ \vdots \\ I^{T_n} \end{bmatrix}_{2n \times 1} = \begin{bmatrix} V^{T_1} \\ V^{T_2} \\ \vdots \\ V^{T_n} \end{bmatrix}_{2n \times 4} [Y]_{4 \times 1}$$$

*非对称单相线路超定方程组构建形式，通过n组独立录波求解4个导纳参数*


**公式4**: $$$\rho(D_{T_j}, D_{T_k}) = \frac{\text{cov}(D_{T_j}, D_{T_k})}{\sigma(D_{T_j})\sigma(D_{T_k})}$$$

*皮尔逊线性相关系数公式，用于评估不同录波数据集间的共线性，防止模型数值病态*


**公式5**: $$$\text{NRMSD}\% = 100 \times \frac{\sqrt{\text{mean}[(X_{\text{RecM}} - X_{\text{ATP}})^2]}}{\max(X_{\text{ATP}}) - \min(X_{\text{ATP}})}$$$

*归一化均方根偏差计算公式，用于量化重构模型与基准仿真结果的误差*


### 算法步骤

1. 步骤1：同步数据采集与预处理。利用WMU在线路两端同步记录暂态电压与电流波形，确保时间戳严格对齐。对原始信号进行必要的滤波与去噪处理。

2. 步骤2：频域转换。对两端时域波形应用数值拉普拉斯变换（NLT），将$i_S(t), i_R(t), v_S(t), v_R(t)$转换至复频域$I_S(s), I_R(s), V_S(s), V_R(s)$，覆盖宽频带范围。

3. 步骤3：矩阵方程构建。根据线路类型（均匀/非均匀、单相/三相、换位/非换位）选择对应的二端口导纳拓扑结构，将频域电压电流数据组装为线性代数方程组$[I] = [V][Y]$。

4. 步骤4：数据共线性检验。计算不同录波数据集间的皮尔逊相关系数，若$\rho \ge 0.8$或为负值则剔除该数据集，确保输入变量线性独立，避免最小二乘求解时的数值不稳定。

5. 步骤5：模型参数求解。对于对称/均匀系统直接求逆求解；对于非对称/非均匀系统，采用最小范数最小二乘法（MNLS）求解超定方程组，得到全频带导纳矩阵元素$A(s), B(s), C(s), D(s)$。

6. 步骤6：时域响应重构与验证。将求解得到的频域导纳模型结合任意终端边界条件（源阻抗、负载导纳），通过逆数值拉普拉斯变换（INLT）或矢量拟合生成FDNE等效网络，输出时域电压电流响应并与基准对比。


### 关键参数

- **采样分辨率**: 50 kHz（商用WMU标准）

- **共线性剔除阈值**: 皮尔逊相关系数 $\rho \ge 0.8$ 或负相关

- **最小独立录波组数**: 均匀/理想换位线: 1组；非对称单相/非换位三相: $n \ge 3$组；全非对称三相: $n \ge 5$组

- **频域变换方法**: 数值拉普拉斯变换（NLT）与逆变换（INLT）

- **求解算法**: 直接矩阵求逆（对称情况） / 最小范数最小二乘法（MNLS，非对称情况）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Case A: 三相均匀理想换位线路 | 采用单位阶跃激励（A相，源阻抗1Ω/相，负载1000Ω/相）生成单组录波。重构模型在完全不同的测试条件下（60Hz交流源串联10mH电感，A相接5μF电容，B/C相开路）进行验证。 | 重构模型响应与ATP基准仿真高度吻合，所有电压与电流波形的归一化均方根偏差（NRMSD）均低于0.56%，证明单组录波即可实现高精度黑盒建模。 |

| Case B: 单相混合架空-地下电缆系统 | 针对纵向参数非均匀的混合拓扑，采用3组不同脉宽（1ms, 2ms, 3ms）与不同负载（5Ω, 25Ω, 1000Ω）的1 p.u.方波激励录波。 | 通过MNLS求解超定系统成功重构宽频导纳模型，有效捕捉了架空线与电缆连接处的波阻抗突变与频率相关特性，时域波形误差控制在工程允许范围内（具体NRMSD未列出但验证了方法鲁棒性）。 |



## 量化发现

- 三相均匀换位线路重构模型在复杂终端条件下的电压/电流NRMSD误差严格小于0.56%
- 数据共线性控制阈值设定为皮尔逊相关系数0.8，有效避免了超定方程求解时的矩阵病态问题
- 非对称单相线路至少需要3组线性独立录波，全非对称三相线路至少需要5组录波才能稳定求解MNLS
- 商用WMU标准采样率50 kHz足以支撑宽频EMT模型重构，满足高频暂态分量捕捉需求
- 重构模型为纯黑盒形式，无需输入线路几何尺寸、土壤电阻率或导体材料参数，直接由端点电气量驱动


## 关键公式

### 对称二端口导纳模型

$$$\begin{bmatrix} I_S(s) \\ I_R(s) \end{bmatrix} = \begin{bmatrix} A(s) & B(s) \\ B(s) & A(s) \end{bmatrix} \begin{bmatrix} V_S(s) \\ V_R(s) \end{bmatrix}$$$

*用于单相均匀线路或理想换位三相线路的频域建模基础，假设线路纵向对称*

### 超定系统MNLS求解方程

$$$\begin{bmatrix} I^{T_1} \\ \vdots \\ I^{T_n} \end{bmatrix} = \begin{bmatrix} V^{T_1} \\ \vdots \\ V^{T_n} \end{bmatrix} [Y]$$$

*用于非均匀、非换位或混合线路，通过多组独立录波构建超定矩阵，利用最小范数最小二乘法求解导纳参数*

### 归一化均方根偏差评估指标

$$$\text{NRMSD}\% = 100 \times \frac{\sqrt{\text{mean}[(X_{\text{RecM}} - X_{\text{ATP}})^2]}}{\max(X_{\text{ATP}}) - \min(X_{\text{ATP}})}$$$

*用于量化重构模型时域响应与ATP基准仿真之间的全局误差，消除幅值量纲影响*



## 验证详情

- **验证方式**: 基于ATP仿真的数字孪生验证（Emulated Measurements），通过对比重构模型与ATP基准在不同终端条件下的时域响应进行误差分析
- **测试系统**: 三相均匀理想换位架空线路（Case A）、单相混合架空-地下电缆系统（Case B）、三相非平衡非均匀线路（Case C，文中提及）
- **仿真工具**: ATP (Alternative Transient Program) 用于生成基准暂态录波与对比仿真；MATLAB/自定义算法用于NLT、MNLS求解与模型重构
- **验证结果**: 重构模型在宽频带内表现出极高的精度与鲁棒性，NRMSD误差低于0.56%。方法成功克服了传统解析模型对几何参数和均匀性假设的依赖，能够有效处理混合拓扑、纵向参数变化及非换位不对称情况。对实际测量因素（噪声、采样分辨率、互感器变比与相位误差）的敏感性分析表明，在50kHz采样率及合理信噪比下，模型重构依然保持稳定，具备工程部署潜力。
