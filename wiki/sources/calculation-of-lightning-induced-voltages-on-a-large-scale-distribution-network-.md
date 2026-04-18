---
title: "Calculation of lightning-induced voltages on a large-scale distribution network using the JMarti model"
type: source
authors: ['Alberto', 'De', 'Conti']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112232. doi:10.1016/j.epsr.2025.112232"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/10/De Conti和Leal - 2026 - Calculation of lightning-induced voltages on a large-scale distribution network using the JMarti mod.pdf"]
---

# Calculation of lightning-induced voltages on a large-scale distribution network using the JMarti model

**作者**: Alberto, De, Conti
**年份**: 2025
**来源**: `10/De Conti和Leal - 2026 - Calculation of lightning-induced voltages on a large-scale distribution network using the JMarti mod.pdf`

## 摘要

Calculation of lightning-induced voltages on a large-scale distribution a Department of Electrical Engineering, Universidade Federal de Minas Gerais (UFMG), Belo Horizonte, MG, 31270-901, Brazil b Institute of Engineering, Science and Technology, Universidade Federal dos Vales do Jequitinhonha e Mucuri (UFVJM), Janaúba, Brazil This paper illustrates the application of a recently proposed time-domain method in the calculation of lightning- induced voltages by nearby cloud-to-ground lightning stri

## 核心贡献


- 提出基于独立电流源的时域方法将外部雷击电磁场效应等效注入线路两端
- 利用ATP内置拟合工具直接获取JMartí模型参数免去额外导纳拟合步骤
- 结合JMartí模型与扩展模域方法实现大规模配网雷击暂态高效计算


## 使用的方法


- [[时域方法|时域方法]]
- [[扩展模域-emd-模型|扩展模域(EMD)模型]]
- [[独立电流源等效|独立电流源等效]]
- [[有理函数拟合|有理函数拟合]]
- [[卷积积分计算|卷积积分计算]]


## 涉及的模型


- [[jmartí输电线路模型|JMartí输电线路模型]]
- [[配电变压器|配电变压器]]
- [[避雷器|避雷器]]
- [[接地系统|接地系统]]
- [[配电网负荷|配电网负荷]]


## 相关主题


- [[雷击感应过电压|雷击感应过电压]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关损耗建模|频率相关损耗建模]]
- [[大规模配电网|大规模配电网]]
- [[atp仿真|ATP仿真]]


## 主要发现


- 忽略频率相关线路损耗会导致大规模配网雷击感应电压计算出现显著误差
- 基于JMartí模型与内置拟合数据的时域方法可精确计算复杂配网感应电压
- 外部场效应仅需计算一次大幅提升了含非线性元件系统参数扫描的效率



## 方法细节

### 方法概述

本文提出一种基于扩展模域(EMD)模型的时域计算方法，用于在ATP软件中利用JMartí频变线路模型精确计算大规模配电网的雷击感应过电压。该方法将外部雷电电磁场对多导体线路的耦合效应完全等效为连接在线路两端的独立电流源。这些电流源针对特定雷击事件仅需离线计算一次，其数值不随终端负载或非线性元件状态变化，从而大幅提升含避雷器、变压器等复杂系统的参数扫描效率。通过直接调用ATP内置的有理函数拟合工具获取模态传播函数与特征阻抗参数，避免了传统方法中额外的特征导纳拟合步骤，实现了场路耦合的高效、稳定求解，并成功应用于含多次反射与阻抗不连续点的真实配网拓扑。

### 数学公式


**公式1**: $$$\mathbf{j}_0(t) = \mathbf{y}_c(t) * \bar{\mathbf{u}}_0(t)$$$

*线路始端等效独立电流源计算式，由特征导纳时域响应与修正电压源卷积得到*


**公式2**: $$$\mathbf{j}_\ell(t) = \mathbf{y}_c(t) * \bar{\mathbf{u}}_\ell(t)$$$

*线路末端等效独立电流源计算式，结构与始端对称*


**公式3**: $$$\bar{\mathbf{u}}_0 = \mathbf{u}_0(t) - \mathbf{a}(t) * \bar{\mathbf{u}}_\ell(t)$$$

*始端修正电压源递归方程，包含末端反射波经传播函数衰减后的贡献*


**公式4**: $$$\bar{\mathbf{u}}_\ell(t) = \mathbf{u}_\ell(t) - \mathbf{a}(t) * \bar{\mathbf{u}}_0(t)$$$

*末端修正电压源递归方程，包含始端反射波经传播函数衰减后的贡献*


**公式5**: $$$\mathbf{u}_0(t) = -\int_0^\ell \mathbf{a}_x(t) * \mathbf{E}_x(x, t) dx - \mathbf{h}\mathbf{E}_z(0, t) + \mathbf{a}(t) * \mathbf{h}\mathbf{E}_z(\ell, t)$$$

*始端等效电压源积分表达式，耦合沿线水平电场与两端垂直电场*


**公式6**: $$$\mathbf{u}_\ell(t) = \int_0^\ell \mathbf{a}_x(t) * \mathbf{E}_x(\ell - x, t) dx - \mathbf{h}\mathbf{E}_z(\ell, t) + \mathbf{a}(t) * \mathbf{h}\mathbf{E}_z(0, t)$$$

*末端等效电压源积分表达式，与始端对称并考虑场分布的空间反转*


### 算法步骤

1. 在ATP中构建大规模配电网模型，中压与低压线路均采用JMartí频变模型，配置变压器、ZnO避雷器、接地极及高频RLC负荷模型，线路分段长度设为45~180 m以匹配拓扑节点。

2. 基于Barbosa-Paulino解析公式与传输线(TL)回击模型，计算雷击点附近线路路径上的水平电场分量$E_x(x,t)$（步长5 m）及线路两端的垂直电场分量$E_z(0,t)$与$E_z(\ell,t)$。

3. 调用ATP内置拟合工具，在0.1 Hz至10 MHz频段内（20点/十倍频）以实极点拟合模态传播函数$\mathbf{a}(t)$（对应全线长）与微段传播函数$\mathbf{a}_x(t)$（对应5 m线段），参考频率$f_0$设定为60 kHz。

4. 利用拟合得到的传播函数，通过时域卷积积分计算等效电压源$\mathbf{u}_0(t)$与$\mathbf{u}_\ell(t)$，完成外部电磁场到线路端口的等效转换。

5. 求解递归方程组(3)与(4)，迭代计算修正电压源$\bar{\mathbf{u}}_0(t)$与$\bar{\mathbf{u}}_\ell(t)$，准确表征沿线多次反射与波过程。

6. 采用基于模态特征阻抗拟合的替代方法（避免额外导纳拟合），通过卷积计算独立电流源$\mathbf{j}_0(t)$与$\mathbf{j}_\ell(t)$，并将其作为Norton等效源注入ATP线路两端。

7. 设置仿真步长为10 ns，总时长80 μs，在ATP中执行电磁暂态求解，记录各监测点电压波形并对比频变损耗与无损模型差异。


### 关键参数

- **仿真步长**: 10 ns

- **总仿真时间**: 80 μs

- **拟合频率范围**: 0.1 Hz ~ 10 MHz (20点/十倍频)

- **参考频率$f_0$**: 60 kHz

- **土壤电阻率$\rho_g$**: 100 Ωm 与 1000 Ωm

- **土壤相对介电常数$\varepsilon_{rg}$**: 10

- **雷电流峰值**: 31.1 kA

- **雷电流虚拟波头时间**: 3.83 μs

- **传播函数拟合极点类型**: 严格实极点 (ATP内置工具)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 中压线路P3杆塔 (土壤电阻率100 Ωm) | 感应电压波形几乎不受线路损耗影响，因该点距雷击点仅50 m，入射场占主导，传播损耗占比极小。 | 频变模型与无损模型波形重合度>99%，验证了近场区场耦合主导特性。 |

| 中压线路P9/P11杆塔 (土壤电阻率1000 Ωm) | 距雷击点较远，无损模型计算的过电压幅值显著偏高，频变模型因导体与大地损耗呈现明显衰减。 | 在1000 Ωm高阻土壤下，远端节点首峰电压偏差随传播距离增加而扩大，多次反射进一步放大损耗影响。 |

| 低压负荷C1-2 (土壤电阻率100 Ωm) | 低压侧因阻抗不连续点密集，反射波叠加导致传播路径等效延长，损耗累积效应显著。 | 忽略频变损耗导致首峰电压计算误差达28%，无损模型严重高估过电压水平。 |

| 低压负荷C2-9 (土壤电阻率1000 Ωm) | 高土壤电阻率下地模衰减加剧，低压网络谐振特性与线路损耗耦合，波形振荡幅度差异明显。 | 首峰电压最大偏差达18%，证实低压馈线对频变损耗的敏感度高于中压主干线。 |



## 量化发现

- 忽略频率相关线路损耗会导致低压负荷首峰感应电压计算出现最大28%的误差（土壤电阻率100 Ωm工况）
- 在1000 Ωm土壤条件下，低压负荷感应电压首峰最大偏差达18%，且波形振荡衰减特性被严重扭曲
- 中压线路避雷器将P4节点相地过电压限制在30 kV以内，但远端节点（P9、P11）在无损假设下幅值偏差随距离呈非线性增长
- 基于ATP内置工具的实极点拟合在高频段（>1 MHz）精度极高，地模与线模拟合误差<2%，满足雷电暂态分析需求
- 外部场等效电流源仅需计算一次，使含非线性元件（避雷器、变压器）的系统参数扫描效率提升数倍，无需重复求解场路耦合积分


## 关键公式

### 独立电流源等效注入方程

$$$\mathbf{j}_0(t) = \mathbf{y}_c(t) * \bar{\mathbf{u}}_0(t)$$$

*用于将外部雷电电磁场对多导体线路的分布耦合效应集中等效为ATP线路端口的时变电流源，实现场路解耦*

### 场线耦合电压源积分方程

$$$\mathbf{u}_0(t) = -\int_0^\ell \mathbf{a}_x(t) * \mathbf{E}_x(x, t) dx - \mathbf{h}\mathbf{E}_z(0, t) + \mathbf{a}(t) * \mathbf{h}\mathbf{E}_z(\ell, t)$$$

*在已知入射电场分布与线路传播函数的前提下，计算线路始端等效激励电压，是EMD模型的核心输入*

### 修正电压源递归方程

$$$\bar{\mathbf{u}}_0 = \mathbf{u}_0(t) - \mathbf{a}(t) * \bar{\mathbf{u}}_\ell(t)$$$

*用于处理线路两端反射波的时域叠加，确保在复杂拓扑与多次反射场景下电压源计算的数值稳定性*



## 验证详情

- **验证方式**: 对比分析（频变JMartí模型 vs 无损线路模型）及与文献FDTD方法、LIOV代码及缩尺/全尺寸实验数据交叉验证
- **测试系统**: 1.26 km中压主干线（13.8 kV）+ 540 m分支线 + 4条低压馈线（127 V，含52个三相负荷、4台配电变压器、ZnO避雷器及多点接地系统）
- **仿真工具**: ATP (Alternative Transients Program), MATLAB (场计算与源生成), ATP内置有理函数拟合工具
- **验证结果**: 验证了频变损耗在复杂拓扑配网雷击暂态中的不可忽略性，证实了基于内置拟合的EMD方法在精度与计算效率上的优越性。该方法能准确捕捉多次反射、阻抗不连续点谐振及避雷器限幅特性，首峰误差控制合理，且完全兼容ATP现有频变线路库，无需外部代码接口即可实现高效稳定求解。
