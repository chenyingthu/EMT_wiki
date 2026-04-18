---
title: "A guaranteed passive model for multi-port frequency dependent network equivalents using network synthesis approach"
type: source
authors: ['Meysam Ahmadi']
year: 2021
journal: "Electric Power Systems Research, 197 (2021) 107248. doi:10.1016/j.epsr.2021.107248"
tags: ['frequency-dependent', 'network-equivalent']
created: "2026-04-13"
sources: ["EMT_Doc/01/Ahmadi 等 - 2021 - A guaranteed passive model for multi-port frequency dependent network equivalents using network synt.pdf"]
---

# A guaranteed passive model for multi-port frequency dependent network equivalents using network synthesis approach

**作者**: Meysam Ahmadi
**年份**: 2021
**来源**: `01/Ahmadi 等 - 2021 - A guaranteed passive model for multi-port frequency dependent network equivalents using network synt.pdf`

## 摘要

0378-7796/Crown Copyright © 2021 Published by Elsevier B.V. All rights reserved. A guaranteed passive model for multi-port frequency dependent network Meysam Ahmadi a,*, Shengtao Fan a, Aniruddha M. Gole a, H. M. Jeewantha De Silva b a Power Systems Research Group, Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB, R3T 5V6, Canada b Manitoba Hydro International, Winnipeg, MB, Canada, R3P 1A3

## 核心贡献


- 提出基于网络综合法的多端口FDNE建模方法，直接由频响表格数据构建RLCM无源网络。
- 自动化Tellegen综合法适配表格阻抗数据，实现多端口等值且无需额外无源性校正。
- 从根本上保证多端口FDNE无源性，避免矢量拟合法强制无源导致的精度损失与不收敛。


## 使用的方法


- [[brune综合法|Brune综合法]]
- [[tellegen综合法|Tellegen综合法]]
- [[网络综合法|网络综合法]]
- [[正实矩阵实现|正实矩阵实现]]


## 涉及的模型


- [[fdne-model|FDNE]]
- [[rlcm网络|RLCM网络]]
- [[多端口阻抗矩阵|多端口阻抗矩阵]]
- [[外部网络等值|外部网络等值]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关网络等值|频率相关网络等值]]
- [[无源性保证|无源性保证]]
- [[多端口网络建模|多端口网络建模]]
- [[实时仿真|实时仿真]]


## 主要发现


- 案例验证表明该方法能精确复现外部网络频响特性，且全程自动保证模型无源性。
- 相比矢量拟合法，该方法无需后处理无源性校正，彻底避免了精度损失与迭代不收敛问题。
- 成功将单端口综合法推广至多端口系统，生成的RLCM网络可直接用于EMT仿真工具。



## 方法细节

### 方法概述

本文提出一种基于Tellegen扩展Brune网络综合法的多端口频率相关网络等值（FDNE）建模方法。该方法直接针对离散频域阻抗表格数据$Z(j\omega_k)$进行数值综合，无需预先进行有理函数拟合（如矢量拟合法）。核心思想是利用正实（PR）矩阵性质，通过迭代执行四个步骤（移除虚轴极点、移除虚轴零点、提取最小实部电阻、执行Tellegen-Brune循环）逐步降阶，最终将多端口阻抗矩阵综合为由电阻、电感、电容和理想变压器构成的RLCM无源网络。由于网络完全由物理无源元件搭建，从根本上保证了模型的无源性，彻底避免了传统方法中无源性强制校正带来的精度损失与不收敛问题。最终生成的RLCM电路可转换为微分代数方程（DAE）或诺顿等效源，直接嵌入EMT仿真工具。

### 数学公式


**公式1**: $$$Z(s) = K_{\infty p} s + \frac{K_{0p}}{s} + \sum_{j_p=1}^{n_p} K_{j_p} \frac{2s}{s^2 + \omega_{j_p}^2} + Z_1(s)$$$

*虚轴极点移除公式，将阻抗矩阵分解为串联电感、电容、LC谐振支路及剩余阻抗$Z_1(s)$*


**公式2**: $$$Y_1(s) = K_{\infty z} s + \frac{K_{0z}}{s} + \sum_{j_z=1}^{n_z} K_{j_z} \frac{2s}{s^2 + \omega_{j_z}^2} + Y_2(s)$$$

*虚轴零点移除公式，通过导纳矩阵提取并联电容、电感及LC支路*


**公式3**: $$$R_{min} = \min\{\Lambda(\omega)\}, \quad \Lambda(\omega) = \frac{|A(\omega)|}{\Delta_{11}(\omega)}$$$

*最小实部电阻计算公式，其中$A(\omega)=\Re\{Z_2(j\omega)\}$，$\Delta_{11}$为其(1,1)余子式*


**公式4**: $$$Z_4(s) = Z_3(s) - t_1 t_1^T s L_1$$$

*Brune循环第一步，移除串联电感网络$L_1$及变压器变比向量$t_1$*


**公式5**: $$$L_3 = -\frac{L_1 L_2}{F^2 L_1 + L_2}, \quad F = t_1 \cdot t_2$$$

*Tellegen扩展中耦合电感$L_3$的计算关系式，保证网络物理可实现性*


### 算法步骤

1. 步骤1（数值移除虚轴极点）：通过检测低频/高频相位角是否趋近-90°/+90°（阈值0.5°）识别$s=0$或$s=\infty$极点；通过相位180°突变识别有限频率极点$\omega_{jp}$。利用公式(18)(19)数值计算留数矩阵$K_{\infty p}, K_{0p}, K_{jp}$，并按公式(20)从原始表格数据中逐点扣除极点贡献，得到剩余阻抗$Z_1(j\omega_k)$。

2. 步骤2（数值移除虚轴零点）：对$Z_1(j\omega_k)$求逆得到导纳矩阵$Y_1(j\omega_k)$，重复步骤1的相位检测与留数计算逻辑，识别导纳极点（即原阻抗零点）。计算并联元件参数及变压器变比，从导纳矩阵中扣除，得到$Y_2(j\omega_k)$并求逆回阻抗形式$Z_2(j\omega_k)$。

3. 步骤3（数值提取最小实部电阻）：计算实部矩阵$A(\omega_k)=\Re\{Z_2(j\omega_k)\}$及其函数$\Lambda(\omega_k)$。遍历所有采样点找到最小值$R_{min}$及其对应频率$\omega_0$。若$\omega_0$为端点则提取串联/并联电抗；否则在端口1串联电阻$R_{min}$，更新阻抗矩阵$Z_3(j\omega_k)=Z_2(j\omega_k)-\text{diag}(R_{min},0,\dots,0)$，使实部在$\omega_0$处秩亏。

4. 步骤4（数值实现Tellegen-Brune循环）：在$\omega_0$处计算虚部矩阵$X=\Im\{Z_3(j\omega_0)\}$，求解零空间向量$\beta$使$\Re\{Z_3(j\omega_0)\}\beta=0$。构造秩一矩阵$H=\alpha hh^T$并提取串联电感$L_1$及变比$t_1$得到$Z_4$。在$\omega_0$处通过极限法/邻域平均计算导纳极点留数$K_x$，提取并联LC支路$L_2, C_2$及变比$t_2$得到$Z_5$。最后利用耦合关系计算$L_3$并扣除，完成一个降阶循环。重复上述四步直至剩余阻抗退化为常数矩阵$R_{end}$。


### 关键参数

- **相位检测阈值**: 0.5°

- **仿真时间步长**: 20 µs

- **仿真总时长**: 0.2 s

- **三端口等值网络模块数**: 80个RLCM基本模块

- **数据输入形式**: 离散频域阻抗表格$Z(j\omega_k)$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 双端口RLC基准电路 | 对简单2端口RLC网络进行频域扫描与综合。在端口1施加1 kV、60 Hz正弦电压，对比端口2电压与端口1电流的时域波形。频响曲线（对角与非对角阻抗元素）与原始网络完全重合，时域响应误差可忽略。 | 频域与双端口时域响应实现精确复现，验证了算法基础逻辑的正确性。 |

| 230 kV三端口输电网络（9母线11回线） | 针对含多回架空线的实际三相系统构建FDNE。综合生成80个RLCM无源模块。在t=0.1 s施加三相接地故障，0.125 s清除。原始网络仿真耗时640 ms，FDNE模型耗时194 ms。三相源电流时域波形在故障暂态与稳态阶段均高度吻合。 | 计算速度提升3.3倍（640 ms降至194 ms），在保持无源性绝对保证的前提下，暂态波形匹配度极高，无传统矢量拟合强制无源导致的精度损失。 |



## 量化发现

- 仿真计算速度提升3.3倍（原始网络640 ms vs FDNE模型194 ms，时间步长20 µs，时长0.2 s）
- 三端口复杂输电网络仅需80个RLCM综合模块即可实现高精度等值
- 相位角极点/零点自动识别阈值设定为0.5°，实现全自动化表格数据处理
- 模型无源性由物理RLCM拓扑内禀保证，无源性校正误差为0%，彻底消除迭代不收敛风险
- 频域阻抗拟合在全频段（含谐振峰）实现精确匹配，时域暂态电流波形偏差极小（工程精度满足EMT要求）


## 关键公式

### 数值极点扣除更新公式

$$$Z_1(j\omega_k) = Z(j\omega_k) - j\omega_k K_{\infty p} - \frac{K_{0p}}{j\omega_k} - \sum_{j_p=1}^{n_p} K_{j_p} \frac{2s}{-\omega_k^2 + \omega_{j_p}^2}$$$

*在离散频点$k$处，从原始阻抗表格中减去已识别的虚轴极点贡献，用于迭代降阶*

### 最小实部电阻提取公式

$$$R_{min} = \min_{\omega} \left\{ \frac{|\Re\{Z_2(j\omega)\}|}{\Delta_{11}(\omega)} \right\}$$$

*用于步骤3，确定需从端口1移除的串联电阻值，使剩余阻抗实部在特定频率秩亏*

### Tellegen-Brune耦合电感关系式

$$$L_3 = -\frac{L_1 L_2}{(t_1 \cdot t_2)^2 L_1 + L_2}$$$

*步骤4核心公式，通过$L_1, L_2$及变压器变比计算负电感$L_3$，结合理想变压器实现全正无源元件等效*



## 验证详情

- **验证方式**: 频域阻抗曲线对比与时域电磁暂态仿真对比分析
- **测试系统**: 案例1：自定义双端口RLC电路；案例2：230 kV三相输电系统（含9个母线、11回不同长度架空线，多端口耦合）
- **仿真工具**: 自定义数值综合算法（实现表格数据处理与RLCM参数提取）+ 通用EMT仿真平台（通过DAE/Norton等效接口接入）
- **验证结果**: 频域扫描显示对角与非对角阻抗元素在全频段精确重合；时域三相接地故障暂态波形高度一致。模型由纯无源RLCM元件构成，内禀满足正实条件，无需后处理无源性校正。计算效率提升3.3倍，验证了该方法在复杂多端口FDNE建模中的高精度、高稳定性与工程实用性。
