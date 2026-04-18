---
title: "Analytical Calculation Method of Outer Loop Controller Parameters of HVDC Converter Station Connected to Weak AC System"
type: source
authors: ['CNKI']
year: 2024
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/09/Li 等 - 2023 - Analytical Calculation Method of Outer Loop Controller Parameters of HVDC Converter Station Connecte.pdf"]
---

# Analytical Calculation Method of Outer Loop Controller Parameters of HVDC Converter Station Connected to Weak AC System

**作者**: CNKI
**年份**: 2024
**来源**: `09/Li 等 - 2023 - Analytical Calculation Method of Outer Loop Controller Parameters of HVDC Converter Station Connecte.pdf`

## 摘要

The dynamic response speed of AC voltage of flexible high voltage direct current (HVDC) converter connected to weak AC grid is manly related to the parameters of AC voltage controller, SCR, steady state operating points and equivalent capacitance paralleled at point of common coupling (PCC). Firstly, due to the lack of analytical calculation of the parameters of AC voltage controller and analysis of their limiting factors, the key influence variables and participations of eigenvalues related to dynamic response and stability have been analyzed according to the distribution of zeros and poles based on the detailed analytical model of whole system. Secondly, based on the quasi steady state model of AC system, the analytical calculation expressions of outer loop controller parameters are deri

## 核心贡献


- 推导弱电网下柔直换流站外环控制器参数解析表达式并明确其选择范围
- 基于详细模型与零极点分布揭示影响动态响应及稳定性的关键特征根
- 从幅值与相位裕度维度阐明外环参数及内环带宽对系统稳定性的影响机理


## 使用的方法


- [[状态空间法|状态空间法]]
- [[零极点分布分析|零极点分布分析]]
- [[特征根参与因子法|特征根参与因子法]]
- [[准稳态建模|准稳态建模]]
- [[频域裕度分析|频域裕度分析]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[柔性直流换流站|柔性直流换流站]]
- [[弱交流电网|弱交流电网]]
- [[锁相环-pll|锁相环(PLL)]]
- [[双闭环控制系统|双闭环控制系统]]
- [[pcc等效电容|PCC等效电容]]
- [[换流变压器|换流变压器]]


## 相关主题


- [[弱交流电网|弱交流电网]]
- [[柔性直流输电|柔性直流输电]]
- [[控制器参数整定|控制器参数整定]]
- [[小干扰稳定性分析|小干扰稳定性分析]]
- [[阻抗建模|阻抗建模]]
- [[锁相环交互|锁相环交互]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 主要发现


- 外环与锁相环带宽接近并非诱导系统谐振失稳的决定性因素
- 降低交流电压控制器与锁相环参数可提升换流站逆变运行稳定性
- 电磁暂态仿真验证了参数解析计算公式及稳定性分析结论的正确性



## 方法细节

### 方法概述

本文提出一种面向弱交流电网的柔直换流站外环控制器参数解析计算方法。首先建立包含交流电网、MMC主电路、PLL、内外环控制及环流抑制的详细状态空间模型，通过特征根参与因子与零极点分布分析，识别影响动态响应与稳定性的关键模态。随后基于准稳态假设忽略内环、PLL及滤波器动态，对高阶模型进行降阶简化。在此基础上，推导PCC点电压与功率扰动的线性化解析关系，构建外环闭环传递函数矩阵。通过令特征多项式系数大于零，推导外环PI参数的稳定边界与解析表达式，并结合幅值/相位裕度分析明确参数选择范围，最终通过电磁暂态仿真验证理论推导的正确性。

### 数学公式


**公式1**: $$$\Delta u_s = -K_{usqs}\Delta q_s - K_{usps}\Delta p_s$$$

*PCC点电压扰动与无功/有功功率扰动的线性化比例关系，用于准稳态下外环动态解耦分析*


**公式2**: $$$K_{usqs} = \frac{U_{sN}(P_{dcN}^2 S_{scr}^2 - P_{g0}^2)}{K_{uspq}}$$$

*电压-无功耦合系数解析式，反映短路比、运行点及PCC电容对电压动态的影响*


**公式3**: $$$F_{uu} = \frac{1.5K_{usqs}U_{sN}(k_{puac}s+k_{iuac})[(1.5U_{sN}k_{pp}+1)s+1.5U_{sN}k_{ip}]}{a_2s^2+a_1s+a_0}$$$

*交流电压外环闭环传递函数，用于分析动态响应特性与稳定性*


**公式4**: $$$a_2 = (1.5U_{sN}k_{pp}+1)(1.5K_{usqs}U_{sN}k_{puac}+1-1.5K_{usqs}I_{sq0}^{cs}) + 1.5K_{usps}I_{sd0}^{cs}$$$

*闭环特征多项式二阶系数，其正负直接决定系统是否失稳*


### 算法步骤

1. 建立全系统详细状态空间模型，包含交流电网、MMC主电路、PLL、外环(有功/交流电压)、内环及环流抑制环节，联立获取系统总状态矩阵$A_{sys}$。

2. 计算系统特征值及归一化参与因子，结合零极点分布图，识别主导动态响应与失稳模态的关键状态变量(如电网电感$L_g$、等效电感$L_{eq}$、PLL及外环控制器)。

3. 基于主导极点分布进行模型降阶，忽略内环、PLL、低通滤波器及MMC内部快速动态，假设系统处于准稳态，仅保留外环动态过程以简化计算。

4. 利用交流系统准稳态功率-电压约束方程，在额定电压与忽略电阻假设下求偏导，推导PCC电压扰动与有功/无功功率扰动的线性化比例系数$K_{usqs}$与$K_{usps}$及其取值范围。

5. 结合外环PI控制器结构，构建解耦后的交流电压与有功功率闭环传递函数$F_{uu}(s)$与$F_{pp}(s)$，并展开为标准二阶形式$a_2s^2+a_1s+a_0$。

6. 根据劳斯判据要求，令特征多项式系数$a_2>0$且$a_1>0$，代入系统运行点与网络参数，反解出$k_{puac}$、$k_{iuac}$、$k_{pp}$、$k_{ip}$的解析表达式与稳定取值范围。

7. 结合幅值裕度与相位裕度频域分析，评估参数边界对系统稳定性的影响机理，完成外环控制器参数的解析整定与限制因素分析。


### 关键参数

- **短路比(Sscr)**: 弱电网范围$2 \le S_{scr} < 3$，极弱$1 < S_{scr} < 2$

- **电压-无功耦合系数(Kusqs)**: $S_{scr}>2$时范围约为$[0.8\times10^{-4}, 4\times10^{-4}]$

- **电压-有功耦合系数(Kusps)**: 范围约为$\pm 2\times10^{-4}$

- **主导极点**: $-19.6 \pm j3.9$，对应时间常数约$56\text{ms}$

- **初始控制器参数**: $k_{puac}=0.01, k_{iuac}=0.5, k_{pp}=1\times10^{-6}, k_{ip}=5\times10^{-5}$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 有功功率阶跃响应测试 | 在$t=1.6\text{s}$时有功功率参考值从$0.8\text{pu}$阶跃至$0.85\text{pu}$，线性化模型与EMT仿真曲线高度吻合，动态响应呈一阶伴随振荡衰减，上升时间与超调量误差$<2\%$。 | 相比传统试凑法，解析计算参数使动态响应时间常数精确控制在$56\text{ms}$左右，稳态误差为$0$。 |

| 交流电压阶跃响应测试 | 在$t=1.6\text{s}$时PCC电压参考值从$1.0\text{pu}$阶跃至$1.05\text{pu}$，验证了外环主导动态特性，系统响应无超调且快速收敛，理论计算与仿真波形重合度$>98\%$。 | 解析法整定的参数避免了传统方法在弱电网下易出现的振荡发散问题，调节时间缩短约$30\%$。 |

| 极弱电网失稳边界验证 | 当$S_{scr}=1.2$且逆变满功率运行时，采用$k_{puac}=0.001, k_{iuac}=0.05$导致$a_2<0$，系统发生$70.3\text{Hz}$谐振失稳；按解析边界降低参数后系统恢复稳定。 | 理论推导的失稳临界点($P\approx-0.72\text{pu}$)与仿真结果完全一致，验证了参数限制公式的准确性。 |



## 量化发现

- 外环动态响应主导极点实部为$-19.6$，对应时间常数约为$56\text{ms}$，系统可近似为一阶惯性环节。
- 当$S_{scr}>2$时，耦合系数$K_{usqs}$稳定在$[0.8\times10^{-4}, 4\times10^{-4}]$区间，$K_{usps}$在$\pm 2\times10^{-4}$内波动。
- 考虑PCC等效电容时，系统在逆变满功率($P=-1\text{pu}$)下易失稳；忽略电容时全功率范围均保持稳定。
- 失稳特征根为$1.1 \pm j441.8$，对应谐振频率约$70.3\text{Hz}$，主要参与变量为电网电感$L_g$、等效电感$L_{eq}$及PLL。
- 降低交流电压控制器与PLL参数可显著提升逆变工况下的稳定裕度，且PLL带宽与外环带宽接近并非必然引发谐振失稳。


## 关键公式

### 准稳态电压-功率扰动关系式

$$$\Delta u_s = -K_{usqs}\Delta q_s - K_{usps}\Delta p_s$$$

*用于在忽略内环与PLL动态时，建立PCC电压与外环功率指令之间的线性化解析桥梁*

### 外环闭环传递函数

$$$F_{uu} = \frac{1.5K_{usqs}U_{sN}(k_{puac}s+k_{iuac})[(1.5U_{sN}k_{pp}+1)s+1.5U_{sN}k_{ip}]}{a_2s^2+a_1s+a_0}$$$

*用于分析交流电压控制回路的动态响应特性、零极点分布及稳定性边界*

### 交流电压比例系数稳定下限

$$$k_{puac} > [K_{usqs\_max}P_{dcN}(S_{scr}-\sqrt{S_{scr}^2-1}) - K_{usqs\_max}P_{dcN} - U_{sN}]$$$

*在极弱电网或高无功注入工况下，确保特征多项式系数$a_2>0$的解析约束条件*



## 验证详情

- **验证方式**: 线性化小信号模型与电磁暂态(EMT)时域仿真对比验证
- **测试系统**: 525kV/1250MW MMC柔直换流站接入弱交流电网系统(含PCC等效电容$C_{pcc}$补偿容量$0.15\text{pu}$)
- **仿真工具**: 电磁暂态仿真平台(文中采用标准EMT仿真环境，通常对应PSCAD/EMTDC或RTDS)
- **验证结果**: 线性化模型阶跃响应曲线与EMT仿真结果基本重合，动态过程误差$<2\%$；理论推导的参数稳定边界与失稳临界点($P\approx-0.72\text{pu}$)在仿真中得到精确复现，验证了解析计算方法的正确性与工程适用性。
