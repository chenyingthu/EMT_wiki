---
title: "Influence of a lossy ground on the lightning performance of overhead transmission lines"
type: source
authors: ['Rafael Alipio']
year: 2022
journal: "Electric Power Systems Research, 214 (2023) 108951. doi:10.1016/j.epsr.2022.108951"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/24/Alipio 等 - 2023 - Influence of a lossy ground on the lightning performance of overhead transmission lines.pdf"]
---

# Influence of a lossy ground on the lightning performance of overhead transmission lines

**作者**: Rafael Alipio
**年份**: 2022
**来源**: `24/Alipio 等 - 2023 - Influence of a lossy ground on the lightning performance of overhead transmission lines.pdf`

## 摘要

0378-7796/© 2022 Elsevier B.V. All rights reserved. Influence of a lossy ground on the lightning performance of overhead Rafael Alipio a,*, Alberto De Conti b, Naiara Duarte c, Farhad Rachidi c a Department of Electrical Engineering, Federal Center of Technological Education of Minas Gerais (CEFET-MG), Av. Amazonas, 7675 - Nova Gameleira, Belo Horizonte, b Department of Electrical Engineering, Federal University of Minas Gerais (UFMG), Belo Horizonte, Brazil

## 核心贡献


- 将位移电流与频变土壤参数引入Sunde大地返回阻抗计算，提升瞬态建模精度
- 在ATP时域仿真器中实现改进型Marti线路模型，支持频变大地参数计算
- 首次系统评估精确损耗大地模型对架空线路雷击反击跳闸率的影响


## 使用的方法


- [[sunde大地返回阻抗公式|Sunde大地返回阻抗公式]]
- [[marti输电线路模型|Marti输电线路模型]]
- [[alipio-visacro频变土壤模型|Alipio-Visacro频变土壤模型]]
- [[heidler雷电流函数|Heidler雷电流函数]]
- [[atp电磁暂态仿真|ATP电磁暂态仿真]]
- [[carson公式对比|Carson公式对比]]


## 涉及的模型


- [[138kv-230kv架空输电线路|138kV/230kV架空输电线路]]
- [[杆塔接地阻抗|杆塔接地阻抗]]
- [[绝缘子串|绝缘子串]]
- [[频变损耗大地模型|频变损耗大地模型]]
- [[雷电流源|雷电流源]]


## 相关主题


- [[雷击反击跳闸率|雷击反击跳闸率]]
- [[频变土壤参数建模|频变土壤参数建模]]
- [[大地返回阻抗|大地返回阻抗]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[过电压分析|过电压分析]]
- [[线路防雷性能|线路防雷性能]]


## 主要发现


- 考虑频变土壤的Sunde公式计算的雷击过电压峰值显著高于传统Carson公式
- 高阻土壤中效应显著，1000至10000Ωm土壤使反击跳闸率提升4%至15%
- 无论采用快波头或慢波头雷电流，精确大地模型均呈现一致的跳闸率上升趋势



## 方法细节

### 方法概述

本文采用时域电磁暂态(EMT)仿真方法，系统评估了位移电流与频变土壤参数对架空输电线路雷击反击跳闸率的影响。研究摒弃了传统Carson公式中忽略位移电流及假设土壤参数恒定的近似，转而采用Sunde大地返回阻抗公式，并结合Alipio-Visacro频变土壤模型计算土壤电阻率与介电常数。在ATP仿真平台中，通过改进型Marti输电线路模型实现频域参数的时域转换。具体流程包括：基于典型138kV与230kV杆塔几何结构构建多导体线路模型；利用矢量拟合技术对模态特征阻抗与传播函数进行实极点拟合；采用Heidler函数构建快、中、慢三种典型首次雷电流波形；通过五塔系统模拟直击雷于中央塔顶的暂态过程，最终统计绝缘子串过电压峰值、临界闪络电流及反击跳闸率，量化精确大地模型对线路防雷性能评估的修正作用。

### 数学公式


**公式1**: $$$\rho_g(f) = \rho_0 \left(1 + 4.7 \times 10^{-6} \times \rho_0^{0.73} \times f^{0.54}\right)^{-1}$$$

*Alipio-Visacro频变土壤电阻率模型，用于计算频率f下的土壤电阻率，其中ρ0为直流电阻率。*


**公式2**: $$$\varepsilon_g(f) = 9.5\varepsilon_0 \times 10^4 \times \rho_0^{-0.27} \times f^{-0.46} + 12\varepsilon_0$$$

*Alipio-Visacro频变土壤介电常数模型，用于计算频率f下的土壤介电常数，ε0为真空介电常数。*


**公式3**: $$$\gamma_g = \sqrt{j\omega\mu_0 \left([\rho_g(f)]^{-1} + j\omega\varepsilon_g(f)\right)}$$$

*Sunde大地返回阻抗传播常数公式，引入频变电阻率ρg(f)和介电常数εg(f)以包含位移电流效应，替代传统Carson公式中的近似项。*


### 算法步骤

1. 步骤1：构建138kV与230kV架空线路多导体几何模型，定义相导线(LINNET/RAIL)、地线(EHS)空间坐标、绝缘子串结构(10/14片瓷瓶)及临界闪络电压(CFO分别为650kV与1050kV)。

2. 步骤2：设定土壤直流电阻率ρ0(1000/5000/10000 Ωm)，利用Alipio-Visacro公式(1)(2)在频域内计算各频率点对应的ρg(f)与εg(f)。

3. 步骤3：基于Sunde公式计算大地返回阻抗矩阵，代入频变传播常数γg，忽略导纳矩阵Yg的微小影响，生成频域线路阻抗Z与导纳Y矩阵。

4. 步骤4：在选定参考频率下计算YZ乘积的特征向量，通过旋转变换矩阵使其虚部最小化，提取实部作为模态变换矩阵，实现相模解耦。

5. 步骤5：对解耦后各模态的特征阻抗与传播函数应用矢量拟合技术(Vector Fitting)，仅保留实极点，生成适用于时域仿真的有理函数逼近模型。

6. 步骤6：将拟合模型嵌入ATP平台的改进型Marti线路模型中，构建包含5基杆塔的仿真系统，两端连接长线以模拟匹配阻抗并消除边界反射干扰。

7. 步骤7：采用Heidler函数叠加生成三种典型首次雷电流波形(波头时间td30分别为1.9μs、3.8μs、7.75μs)，注入中央塔顶，进行时域暂态仿真并记录绝缘子两端过电压。

8. 步骤8：基于过电压峰值与CFO阈值判定闪络事件，统计不同土壤条件下的临界雷电流幅值，结合雷电流概率分布计算反击跳闸率。


### 关键参数

- **土壤电阻率**: 1000 Ωm, 5000 Ωm, 10000 Ωm

- **绝缘子CFO**: 138kV线路: 650 kV; 230kV线路: 1050 kV

- **雷电流波头时间(td30)**: 快波头: 1.9 μs; 中值波头: 3.8 μs; 慢波头: 7.75 μs

- **杆塔配置**: 138kV: 单回LINNET导线+1根3/8'' EHS地线; 230kV: 单回RAIL导线+2根3/8'' EHS地线

- **仿真步长/时间**: 由ATP自动适配，观测时间大于边界反射波返回中央塔的时间



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 1000 Ωm土壤-138kV/230kV线路 | 采用Sunde公式结合频变土壤参数计算的雷击过电压峰值显著高于Carson公式基准，反击跳闸率相对提升4%至6%。 | 较传统Carson模型跳闸率增加4-6%，过电压幅值提升明显，尤其在高频分量丰富的快波头雷电流下差异更显著。 |

| 5000 Ωm土壤-138kV/230kV线路 | 高阻土壤条件下位移电流与频变效应放大，Sunde模型预测的过电压波形畸变更严重，反击跳闸率提升7%至12%。 | 较Carson模型跳闸率增加7-12%，证明土壤电阻率升高时传统忽略位移电流的假设会导致防雷裕度被高估。 |

| 10000 Ωm土壤-138kV/230kV线路 | 极高阻土壤中频变特性主导大地返回阻抗，Sunde模型计算的绝缘子过电压峰值最高，反击跳闸率提升9%至15%。 | 较Carson模型跳闸率增加9-15%，为所有测试工况中最大偏差，验证了精确大地模型在恶劣地质条件下的必要性。 |



## 量化发现

- Sunde公式结合频变土壤模型计算的雷击过电压峰值始终高于传统Carson公式，且随土壤电阻率升高呈非线性增长。
- 在1000 Ωm、5000 Ωm和10000 Ωm土壤条件下，线路反击跳闸率分别提升4-6%、7-12%和9-15%。
- 无论采用快波头(1.9 μs)、中值波头(3.8 μs)或慢波头(7.75 μs)雷电流，精确大地模型均呈现一致的跳闸率上升趋势，表明该效应具有波形鲁棒性。
- 传统Carson公式因假设土壤介电常数为1且忽略位移电流，在高频雷击暂态下会系统性低估过电压幅值，导致防雷设计存在安全隐患。


## 关键公式

### Sunde大地返回传播常数

$$$\gamma_g = \sqrt{j\omega\mu_0 \left([\rho_g(f)]^{-1} + j\omega\varepsilon_g(f)\right)}$$$

*用于替代Carson公式中的传播常数，在计算架空线路频域阻抗矩阵时引入位移电流项$j\omega\varepsilon_g(f)$，适用于高频雷击暂态与高阻土壤场景。*

### Alipio-Visacro频变电阻率公式

$$$\rho_g(f) = \rho_0 \left(1 + 4.7 \times 10^{-6} \times \rho_0^{0.73} \times f^{0.54}\right)^{-1}$$$

*在频域参数计算阶段，将直流电阻率ρ0转换为频率f下的动态电阻率，满足因果律并被CIGRE推荐用于雷击研究。*

### Alipio-Visacro频变介电常数公式

$$$\varepsilon_g(f) = 9.5\varepsilon_0 \times 10^4 \times \rho_0^{-0.27} \times f^{-0.46} + 12\varepsilon_0$$$

*与频变电阻率配套使用，用于修正Sunde公式中的介电常数项，准确表征土壤在雷电流频带内的极化响应。*



## 验证详情

- **验证方式**: 纯数值仿真对比验证，通过在同一测试系统中分别采用Sunde频变模型与Carson恒定模型进行雷击暂态仿真，统计过电压与跳闸率差异。
- **测试系统**: 包含5基杆塔的138kV与230kV架空输电线路系统，中央塔顶受直击雷，两侧相邻塔用于模拟波反射，末端接长线实现阻抗匹配。
- **仿真工具**: ATP (Alternative Transients Program) 用于时域电磁暂态仿真；MATLAB 用于频域参数计算、特征向量旋转及矢量拟合(Vector Fitting)处理。
- **验证结果**: 仿真结果一致表明，忽略位移电流与土壤频变特性会显著低估雷击过电压幅值。在1000~10000 Ωm土壤范围内，精确模型使反击跳闸率预测值提升4%~15%，验证了改进型Marti模型结合Sunde公式在EMT仿真中的工程必要性，为高阻土壤地区线路防雷设计提供了量化修正依据。
