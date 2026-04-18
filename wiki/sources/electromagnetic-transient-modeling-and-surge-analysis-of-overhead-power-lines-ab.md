---
title: "Electromagnetic transient modeling and surge analysis of overhead power lines above two-layer earth"
type: source
authors: ['A.G. Martins-Britto']
year: 2025
journal: "Electric Power Systems Research, 250 (2026) 112142. doi:10.1016/j.epsr.2025.112142"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/16/Martins-Britto 等 - 2026 - Electromagnetic transient modeling and surge analysis of overhead power lines above two-layer earth.pdf"]
---

# Electromagnetic transient modeling and surge analysis of overhead power lines above two-layer earth

**作者**: A.G. Martins-Britto
**年份**: 2025
**来源**: `16/Martins-Britto 等 - 2026 - Electromagnetic transient modeling and surge analysis of overhead power lines above two-layer earth.pdf`

## 摘要

Electromagnetic transient modeling and surge analysis of overhead power a KU Leuven, division Electa & the Etch Competence Hub of EnergyVille, Genk, Belgium b School of Electrical & Computer Engineering, Aristotle University of Thessaloniki, 54124, Thessaloniki, Greece c R&D Department, Hellenic Cables, Maroussi, 15125 Athens, Greece Accurate modeling of earth conduction effects on line parameters is important for electromagnetic transient

## 核心贡献


- 提出等效均匀大地模型近似双层大地复杂积分，提升电磁暂态计算效率。
- 开发开源MATLAB工具箱LineCableLab，支持线路参数计算与ATP/EMTP兼容仿真。
- 系统对比严格双层大地、等效均匀及简化模型对架空线传播特性与过电压的影响。


## 使用的方法


- [[等效均匀大地模型-ehem|等效均匀大地模型(EHEM)]]
- [[严格双层大地解析法|严格双层大地解析法]]
- [[频域分析法|频域分析法]]
- [[相域时域仿真法|相域时域仿真法]]
- [[等效电阻率近似|等效电阻率近似]]
- [[等效传播常数法|等效传播常数法]]


## 涉及的模型


- [[架空输电线路-ohl|架空输电线路(OHL)]]
- [[双回架空线|双回架空线]]
- [[双层大地模型|双层大地模型]]
- [[均匀大地模型|均匀大地模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[过电压分析|过电压分析]]
- [[大地导电效应建模|大地导电效应建模]]
- [[波传播特性|波传播特性]]
- [[分层土壤建模|分层土壤建模]]


## 主要发现


- 等效均匀大地模型能有效替代严格双层积分，避免数值不稳定且保持较高精度。
- 土壤分层参数显著改变线路波传播特性，简化均匀模型在高频段易产生较大误差。
- 所提工具箱验证了不同大地模型对架空线浪涌响应的影响，为工程选型提供依据。



## 方法细节

### 方法概述

本文提出一种基于等效均匀大地模型（EHEM）的架空输电线路电磁暂态建模方法，以替代传统双层大地模型中易引发数值不稳定的复杂半无限积分。研究首先推导了严格双层大地的阻抗与导纳解析表达式，随后引入等效传播常数（$\gamma_{eq}$）与等效电导率（$\sigma_{eq}$）两种近似策略，将分层土壤参数映射为单一均匀大地参数。结合频域（FD）拉普拉斯变换模型与时域（TD）宽带/通用线路模型（WB/ULM），在MATLAB开源工具箱LineCableLab中实现参数计算与ATP/EMTP兼容的暂态仿真。通过对比不同土壤分层工况下的波传播特性与雷击浪涌响应，验证了EHEM在宽频带内的精度与工程适用性。

### 数学公式


**公式1**: $$$Z_{gij} = \frac{j\omega\mu_0}{2\pi}\ln\frac{D_{ij}}{d_{ij}} + \frac{j\omega\mu_0}{\pi}M_{ij}$$$

*双层大地互阻抗解析式，包含复杂半无限积分项$M_{ij}$，用于计算导体间的大地返回阻抗*


**公式2**: $$$P_{gij} = \frac{1}{2\pi\varepsilon_0}\ln\frac{D_{ij}}{d_{ij}} + \frac{1}{\pi\varepsilon_0}Q_{ij}$$$

*双层大地互电位系数解析式，包含积分项$Q_{ij}$，用于构建导纳矩阵*


**公式3**: $$$\gamma_{eq} = \gamma_{e1} \frac{\gamma_{e1} + \gamma_{e2} - (\gamma_{e1} - \gamma_{e2})e^{-2d\gamma_{e1}}}{\gamma_{e1} + \gamma_{e2} + (\gamma_{e1} - \gamma_{e2})e^{-2d\gamma_{e1}}}$$$

*等效传播常数公式，将双层土壤的电磁特性等效为单一均匀大地的传播常数*


**公式4**: $$$\sigma_{eq} = \sigma_1 \frac{\sqrt{\sigma_1} + \sqrt{\sigma_2} - (\sqrt{\sigma_1} - \sqrt{\sigma_2})e^{-2d\sqrt{\pi f \mu_1 \sigma_1}}}{\sqrt{\sigma_1} + \sqrt{\sigma_2} + (\sqrt{\sigma_1} - \sqrt{\sigma_2})e^{-2d\sqrt{\pi f \mu_1 \sigma_1}}}$$$

*忽略位移电流时的等效电导率近似公式，用于快速估算等效电阻率*


### 算法步骤

1. 输入线路几何参数（导线高度、间距、半径）与双层土壤电磁参数（$\rho_1, \rho_2, d, \mu_r, \epsilon_r$），构建基础拓扑矩阵。

2. 计算严格双层大地模型中的半无限积分项$M_{ij}$与$Q_{ij}$，结合Carson/Wise公式生成单位长度阻抗矩阵$\mathbf{Z}$与导纳矩阵$\mathbf{Y}$。

3. 执行EHEM近似：根据目标频率$f$计算等效传播常数$\gamma_{eq}$或等效电导率$\sigma_{eq}$，将其代入均匀大地公式生成等效参数，避免直接数值积分。

4. 频域（FD）仿真：在0.1 Hz至1 MHz范围内以20点/十倍频进行离散采样，利用拉普拉斯变换直接求解节点导纳矩阵，经逆频域变换获取高精度时域响应。

5. 时域（TD）仿真：提取频域传播函数与特征导纳，采用矢量拟合（Vector Fitting）算法进行有理函数逼近，生成ATP/EMTP兼容的WB/ULM模型参数文件（XML/MAT/dat）。

6. 暂态分析：在发送端施加1.2/50 $\mu$s双指数雷击浪涌源（1 p.u.幅值），设置线路终端匹配阻抗，计算各相端电压与跨回路感应过电压，对比不同大地模型的波形差异。


### 关键参数

- **线路电压等级**: 110 kV双回架空线

- **相导线电阻率/直径**: $2.7397 \times 10^{-8} \ \Omega\cdot\text{m}$ / 21.8 mm

- **地线电阻率/直径**: $2.8409 \times 10^{-8} \ \Omega\cdot\text{m}$ / 8 mm

- **线路长度**: 1000 m

- **土壤相对磁导率/介电常数**: $\mu_{r1}=\mu_{r2}=1$, $\epsilon_{r1}=\epsilon_{r2}=10$

- **仿真频带与采样**: 0.1 Hz - 1 MHz，20点/十倍频

- **浪涌源参数**: 1.2/50 $\mu$s双指数波，1 p.u.幅值

- **终端匹配阻抗**: 相导线 600 $\Omega$，地线 660 $\Omega$

- **土壤工况**: 4组不同$\rho_1, \rho_2, d_1$组合（Case I-IV）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Case I-IV 地模传播特性分析 | 在1 kHz至1 MHz频带内，双层大地与EHEM的地模衰减常数和波速始终介于均匀$\rho_1$与均匀$\rho_2$模型之间。低频段趋肤深度大，底层土壤主导传播特性；频率>500 kHz时，趋肤深度接近上层厚度，上层土壤对地模波速影响显著增强。 | EHEM($\gamma_{eq}$)与严格双层积分结果在全频带内高度重合，偏差极小；EHEM($\sigma_{eq}$)在宽频范围内亦保持良好一致性，显著优于单一均匀近似。 |

| Case I 暂态电压响应（FD vs ATP vs EMTP） | L1相受端电压峰值>1 p.u.，主要由空间模决定；L1/L2相感应电压幅值<1 p.u.，受地模与土壤分层强相关。FD模型、ATP-ULM与EMTP-ULM波形整体高度一致。 | ATP因采用开源矢量拟合例程在部分节点产生微小电压尖峰，EMTP与FD主导峰值幅值偏差<1%，验证了多平台WB/ULM实现的等效性。 |

| L2回路感应过电压（不同大地模型对比） | L2回路感应电压受地模主导，简化均匀$\rho_1$模型在Case I-IV中均出现明显波形畸变与幅值低估。EHEM($\gamma_{eq}$)与EHEM($\sigma_{eq}$)计算的瞬态波形与严格双层模型几乎完全重叠。 | EHEM方法在感应过电压计算中误差可忽略，成功替代了易发散的严格双层积分，计算效率与数值稳定性大幅提升。 |



## 量化发现

- 频率>500 kHz时，上层土壤电磁特性对地模波速的影响显著增强，趋肤深度缩减至与上层厚度$d$相当量级。
- 在0.1 Hz至1 MHz全频带内，EHEM($\gamma_{eq}$)计算的传播常数与严格双层积分结果的最大偏差可忽略不计（文中定性为“small differences”/“generally agree”）。
- 采用20点/十倍频采样与拉普拉斯变换FD模型，可直接从原始频域参数求解时域响应，避免了WB/ULM有理拟合引入的RMS误差与极点/残差阈值选择偏差。
- 线路匹配阻抗设定为相导线600 $\Omega$、地线660 $\Omega$时，L1相受端过电压峰值>1 p.u.，L2相感应电压幅值<1 p.u.，地模主导的感应电压对土壤分层参数敏感度远高于空间模。
- ATP与EMTP的WB/ULM实现因矢量拟合算法、最优延迟提取策略及极点/残差阈值选择不同，导致主导峰值存在边际幅值差异，但整体波形一致性满足工程精度要求。


## 关键公式

### 等效传播常数公式

$$$\gamma_{eq} = \gamma_{e1} \frac{\gamma_{e1} + \gamma_{e2} - (\gamma_{e1} - \gamma_{e2})e^{-2d\gamma_{e1}}}{\gamma_{e1} + \gamma_{e2} + (\gamma_{e1} - \gamma_{e2})e^{-2d\gamma_{e1}}}$$$

*用于将双层大地的频变传播特性映射为单一均匀大地参数，适用于任意支持均匀大地假设的线路参数计算软件或解析式*

### 等效电导率近似公式

$$$\sigma_{eq} = \sigma_1 \frac{\sqrt{\sigma_1} + \sqrt{\sigma_2} - (\sqrt{\sigma_1} - \sqrt{\sigma_2})e^{-2d\sqrt{\pi f \mu_1 \sigma_1}}}{\sqrt{\sigma_1} + \sqrt{\sigma_2} + (\sqrt{\sigma_1} - \sqrt{\sigma_2})e^{-2d\sqrt{\pi f \mu_1 \sigma_1}}}$$$

*忽略位移电流效应时，用于快速估算双层土壤的等效电阻率，适用于中低频段工程近似计算*

### 双层大地互阻抗解析式

$$$Z_{gij} = \frac{j\omega\mu_0}{2\pi}\ln\frac{D_{ij}}{d_{ij}} + \frac{j\omega\mu_0}{\pi}M_{ij}$$$

*严格双层大地模型的核心公式，包含复杂半无限积分项$M_{ij}$，作为评估EHEM精度的基准参考*



## 验证详情

- **验证方式**: 对比分析（严格双层解析法 vs EHEM vs 简化均匀模型）与多平台仿真交叉验证
- **测试系统**: 110 kV双回架空输电线路（1000 m长，含相导线与地线，4种典型双层土壤工况Case I-IV）
- **仿真工具**: LineCableLab (MATLAB开源工具箱), ATPDraw 7.5 (ATP-EMTP), EMTP
- **验证结果**: FD模型、ATP-ULM与EMTP-ULM在时域暂态响应上高度一致，验证了仿真流程的可靠性；EHEM($\gamma_{eq}$)与EHEM($\sigma_{eq}$)在宽频带内精确复现了严格双层大地的传播特性与感应过电压，显著优于单一均匀土壤近似，且避免了复杂积分的数值不稳定问题，具备工程实用价值。
