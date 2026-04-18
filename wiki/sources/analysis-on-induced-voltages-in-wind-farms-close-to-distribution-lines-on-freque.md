---
title: "Analysis on Induced Voltages in Wind Farms Close to Distribution Lines on Frequency-Dependent Soil"
type: source
authors: ['未知']
year: 2022
journal: "2022 IEEE Power & Energy Society General Meeting (PESGM);2022; ; ;10.1109/PESGM48719.2022.9917235"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/Da Silva et al. - 2022 - Analysis on Induced Voltages in Wind Farms Close to Distribution Lines on Frequency-Dependent Soil.pdf"]
---

# Analysis on Induced Voltages in Wind Farms Close to Distribution Lines on Frequency-Dependent Soil

**作者**: 
**年份**: 2022
**来源**: `07&08/Da Silva et al. - 2022 - Analysis on Induced Voltages in Wind Farms Close to Distribution Lines on Frequency-Dependent Soil.pdf`

## 摘要

—This paper investigates the impact of the frequency- dependent soil electrical parameters on the transient voltages generated along the wind tower (WT) and on the induced voltages on an overhead distribution line (DL) close to the WT for a lightning striking at the WT. For this objective, a full- wave electromagnetic commercial software XGSLab® based on the Partial Element Equivalent Circuit (PEEC) is used. The frequency-dependent soil characteristic is incorporated into the software using the CIGR `E recommended expressions for the resistivity ρ(f) and relative permittivity εr(f). The analysis is carried out for three different soil resistivities ρ0 of 1000, 2500, and 5000 Ωm. All the transient responses are compared with those computed assuming the ground modeled by its frequency- const

## 核心贡献


- 基于PEEC构建风塔与邻近配电线路全波电磁暂态仿真模型
- 引入CIGRE公式实现土壤电阻率与介电常数频率相关特性建模
- 量化评估频率相关土壤参数对雷击风塔暂态电压及线路感应过电压影响


## 使用的方法


- [[部分元等效电路法-peec|部分元等效电路法(PEEC)]]
- [[全波电磁场仿真|全波电磁场仿真]]
- [[cigre频率相关土壤模型|CIGRE频率相关土壤模型]]
- [[heidler雷电流函数|Heidler雷电流函数]]


## 涉及的模型


- [[风力发电机塔架-wt|风力发电机塔架(WT)]]
- [[架空配电线路-dl|架空配电线路(DL)]]
- [[接地系统-环形网与垂直接地极|接地系统(环形网与垂直接地极)]]
- [[频率相关土壤|频率相关土壤]]
- [[雷电流源|雷电流源]]


## 相关主题


- [[电磁暂态分析|电磁暂态分析]]
- [[雷击感应过电压|雷击感应过电压]]
- [[频率相关土壤特性|频率相关土壤特性]]
- [[风电场接地系统|风电场接地系统]]
- [[瞬态地电位升|瞬态地电位升]]


## 主要发现


- 采用频率相关土壤模型时风塔底部暂态地电位升峰值显著降低约65%
- 叶片注入点电压峰值受土壤频率特性影响极小偏差低于1.5%
- 土壤电阻率超2500Ωm时频率相关特性对后续雷击感应电压影响显著



## 方法细节

### 方法概述

本文采用基于部分元等效电路（PEEC）的全波电磁暂态仿真方法，结合商业软件XGSLab®构建风塔、接地系统与邻近架空配电线路的三维耦合模型。研究核心在于引入CIGRÉ推荐的频率相关土壤模型，在100 Hz至10 MHz宽频带内动态计算土壤电阻率ρ(f)与相对介电常数εr(f)。通过Heidler函数模拟直击雷电流注入风塔叶片，求解频域下的PEEC线性矩阵方程组，再经逆傅里叶变换获取时域暂态电压波形。最终将频变土壤模型的计算结果与恒定参数土壤模型（ρ0恒定，εr=6）进行定量对比，评估土壤频散特性对风塔本体暂态电压、地电位升（GPR）及线路感应过电压的影响机制。

### 数学公式


**公式1**: $$$\{V\} = [W]\{J\}, \quad \{J\} = [A]\{I\} + \{J_e\}, \quad \{E_z\} + \{E_e\} = -([Z] + [M])\{I\}$$$

*PEEC线性矩阵系统，描述导体网络中节点电位、泄漏电流、注入电流与自/互阻抗矩阵之间的电磁耦合关系。*


**公式2**: $$$\rho_g(f) = \rho_0 \left[1 + 4.7 \times 10^{-6} f^{0.54} \rho_0^{0.73}\right]^{-1}$$$

*CIGRÉ推荐的频变土壤电阻率公式，用于计算随频率f和低频基准电阻率ρ0变化的土壤电阻率。*


**公式3**: $$$\varepsilon_r(f) = 12 + 9.5 \times 10^4 \rho_0^{-0.27} f^{-0.46}$$$

*CIGRÉ推荐的频变土壤相对介电常数公式，表征土壤极化特性随频率的衰减规律。*


**公式4**: $$$I(t) = \frac{I_0 (t/\tau_1)^n}{\eta \left[1 + (t/\tau_1)^n\right]} e^{-t/\tau_2}$$$

*Heidler雷电流函数，用于模拟具有宽频特性的直击雷电流时域波形。*


**公式5**: $$$\Delta = \frac{V_p^C - V_p^D}{V_p^C} \times 100\%$$$

*峰值偏差计算公式，用于量化恒定土壤模型(C)与频变土壤模型(D)的电压峰值差异。*


### 算法步骤

1. 几何建模与网格离散：在XGSLab®中建立风塔结构、4层同心圆环接地网（半径18/14/9.5/6.3m，埋深0.6m）及30根12m垂直接地极，并构建邻近架空配电线路三维模型，进行PEEC网格剖分与拓扑连接。

2. 频变土壤参数配置：设定低频基准电阻率ρ0为1000、2500、5000 Ω·m，调用CIGRÉ公式在100 Hz~10 MHz频带内生成ρg(f)与εr(f)频响曲线，并设置恒定土壤对照组（ρ=ρ0, εr=6）。

3. 激励源注入与频域扫描：在风塔叶片顶端（点A）施加Heidler函数定义的雷电流源（I0=50 kA, τ1=1.82 μs, τ2=285 μs, n=10），执行宽频带频域电磁场扫描计算。

4. PEEC矩阵构建与求解：组装包含自/互部分电位系数矩阵[W]、阻抗矩阵[Z]与互阻抗矩阵[M]的线性方程组，采用全波算法求解各离散节点的频域电流与电位分布。

5. 时频转换与波形提取：对频域响应执行逆快速傅里叶变换（IFFT），提取叶片顶端（A）、塔基（B）及配电线中点（C）的时域电压波形。

6. 定量对比与机理分析：计算各工况下电压峰值偏差Δ，分析土壤频散特性对暂态振荡特性、地电位升衰减及感应过电压幅值的影响，并与CIGRÉ导则阈值进行交叉验证。


### 关键参数

- **雷电流峰值_I0**: 50 kA

- **雷电流波头时间_τ1**: 1.82 μs

- **雷电流半峰值时间_τ2**: 285 μs

- **Heidler指数_n**: 10

- **幅值修正系数_η**: 0.987

- **土壤低频电阻率_ρ0**: 1000, 2500, 5000 Ω·m

- **恒定相对介电常数_εr**: 6

- **仿真频带**: 100 Hz ~ 10 MHz

- **接地网结构**: 4层同心环(半径18/14/9.5/6.3m, 埋深0.6m) + 30根12m垂直接地极

- **磁导率_μs**: μ0 (真空磁导率)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 风塔叶片顶端电压(点A) | 在三种土壤电阻率下，频变模型与恒定模型计算的叶片电压峰值差异极小，波形呈现高频振荡特征，后续峰值略高于恒定模型。 | 峰值偏差Δ < 1.50%，表明注入点电压峰值对土壤频变特性不敏感。 |

| 风塔塔基地电位升GPR(点B) | 频变土壤模型显著降低了塔基暂态电压，尤其在5000 Ω·m高阻土壤中，高频段位移电流主导使接地系统呈现容性，有效抑制了反射波。 | 5000 Ω·m工况下，频变模型峰值较恒定模型降低约65%，偏差Δ ≈ 65%。 |

| 邻近配电线中点感应电压(点C) | 土壤频变特性使高频电导率σg(f)增大，趋近理想导体，显著削弱了感应电场。1000 Ω·m时影响微弱，2500与5000 Ω·m时波形振荡加剧且首峰大幅降低。 | 1000 Ω·m时Δ = 12.50%；5000 Ω·m时Δ ≈ -78%（频变模型峰值远低于恒定模型）。 |



## 量化发现

- 风塔叶片注入点电压峰值受土壤频变特性影响极小，最大偏差Δ < 1.50%。
- 高阻土壤（5000 Ω·m）下，频变模型使塔基地电位升（GPR）峰值较恒定模型降低约65%。
- 配电线感应电压在1000 Ω·m土壤中偏差为12.50%，在5000 Ω·m土壤中偏差达-78%，表明频变土壤显著抑制感应过电压幅值。
- CIGRÉ导则建议：当土壤电阻率ρ0 > 700 Ω·m（配电线路建议>2500 Ω·m）时，必须考虑土壤参数的频率依赖性以保证暂态计算精度。
- 频变土壤模型在高频段（>1 MHz）电导率显著上升，使接地系统高频阻抗呈容性特征，有效衰减了雷电流反射波引起的后续电压振荡。


## 关键公式

### CIGRÉ频变土壤电阻率公式

$$$\rho_g(f) = \rho_0 \left[1 + 4.7 \times 10^{-6} f^{0.54} \rho_0^{0.73}\right]^{-1}$$$

*用于在100 Hz~10 MHz频带内动态计算不同基准电阻率下的土壤频散电阻率，替代恒定ρ模型。*

### Heidler雷电流源函数

$$$I(t) = \frac{I_0 (t/\tau_1)^n}{\eta \left[1 + (t/\tau_1)^n\right]} e^{-t/\tau_2}$$$

*模拟直击雷电流的宽频时域波形，作为PEEC全波仿真的激励源注入风塔叶片。*

### PEEC阻抗矩阵方程

$$$\{E_z\} + \{E_e\} = -([Z] + [M])\{I\}$$$

*描述导体网络中电压降、电动势与自/互阻抗矩阵及电流向量的关系，是频域电磁暂态求解的核心。*



## 验证详情

- **验证方式**: 对比仿真验证（频变土壤模型 vs 恒定参数土壤模型）
- **测试系统**: 巴西某实际风电场邻近架空配电线路场景（含风塔、4环30极接地网、10kV配电线）
- **仿真工具**: XGSLab®（基于PEEC的全波电磁暂态商业仿真软件）
- **验证结果**: 仿真结果验证了在高阻土壤（>2500 Ω·m）条件下，忽略土壤频变特性将严重高估塔基地电位升与线路感应过电压峰值。频变模型计算结果与CIGRÉ技术导则（TB 781）建议高度一致，证明了在风电场防雷与绝缘配合设计中引入频变土壤模型的必要性。
