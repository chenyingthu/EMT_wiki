---
title: "A new tool for calculation of line and cable parameters"
type: source
year: 2023
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/02/Morales 等 - 2023 - A new tool for calculation of line and cable parameters.pdf"]
---

# A new tool for calculation of line and cable parameters

**年份**: 2023
**来源**: `02/Morales 等 - 2023 - A new tool for calculation of line and cable parameters.pdf`

## 摘要

−This paper presents a new tool for the computation of per-unit-length parameters for transmission line and cable models used for simulating electromagnetic transients (EMT). The proposed methodology is based on the MoM-SO theory and state-of-the-art formulations for the computation of the series impedance and shunt admittance parameters. The new tool has major advantages compared to traditional approaches available in EMT-type software. These advantages include accurate skin and proximity effect modeling, above-ground cable modeling, modeling of stranded wires in cables, representation of multilayer soil, coupled overhead lines and underground cables, etc. This paper presents the

## 核心贡献


- 提出基于MoM-SO理论的新型参数计算工具，实现高精度单位长度参数求解
- 突破传统程序局限，精确计及集肤与邻近效应、多层土壤及混合线路耦合
- 将先进算法集成至EMTP平台，支持传统方法无法实现的复杂暂态仿真


## 使用的方法


- [[矩量法-mom|矩量法(MoM)]]
- [[表面导纳算子-so|表面导纳算子(SO)]]
- [[傅里叶级数展开|傅里叶级数展开]]
- [[等效定理|等效定理]]
- [[电场积分方程|电场积分方程]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[架空线路|架空线路]]
- [[地下电缆|地下电缆]]
- [[多绞线电缆|多绞线电缆]]
- [[多层土壤模型|多层土壤模型]]
- [[架空-地下混合线路|架空-地下混合线路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[单位长度参数计算|单位长度参数计算]]
- [[集肤与邻近效应|集肤与邻近效应]]
- [[线路-电缆参数计算|线路/电缆参数计算]]
- [[emtp集成|EMTP集成]]


## 主要发现


- 新工具计算精度媲美有限元法，且计算效率显著优于传统有限元技术
- 成功实现架空与地下混合线路及多层土壤耦合暂态仿真，验证模型有效性
- 精确计及集肤与邻近效应，解决传统程序在复杂电缆建模中的精度不足问题



## 方法细节

### 方法概述

该工具基于矩量法与表面导纳算子（MoM-SO）理论，结合最新并联导纳计算公式，实现输电线路与电缆单位长度参数的高精度求解。首先利用等效定理将导体内部场替换为表面电流密度，并通过傅里叶级数（通常取N=4）展开电场与电流分布。随后构建包含多层土壤格林函数的电场积分方程，应用矩量法离散化得到矩阵关系。通过表面导纳算子关联场与电流，经矩阵求逆直接推导串联阻抗矩阵。并联导纳则通过空间电位矩阵与大地回流电位矩阵（含多层土壤修正）组合计算。最终将频变参数集成至EMTP平台，支持架空线、地下电缆、混合线路及复杂地质条件下的电磁暂态仿真。

### 数学公式


**公式1**: $$$Z' = R' + j\omega L'$$$

*单位长度串联阻抗定义式，包含电阻与电感分量*


**公式2**: $$$Y' = G' + j\omega C'$$$

*单位长度并联导纳定义式，包含电导与电容分量*


**公式3**: $$$J_n = E_n \frac{2\pi}{j\omega} \left[ \frac{ka \mathcal{J}'_{|n|}(ka)}{\mu \mathcal{J}_{|n|}(ka)} - \frac{k_{out} a \mathcal{J}'_{|n|}(k_{out} a)}{\mu_0 \mathcal{J}_{|n|}(k_{out} a)} \right]$$$

*表面导纳算子傅里叶系数关系，表征集肤效应与材料属性*


**公式4**: $$$E = j\omega\mu_0 G J + U Z' I$$$

*离散化电场积分方程，引入格林函数G与总电流I*


**公式5**: $$$Z' = \left[ U^T \left( \mathbf{1} - j\omega\mu_0 Y_s G \right)^{-1} Y_s U \right]^{-1}$$$

*MoM-SO串联阻抗矩阵闭式解，精确计及邻近效应与大地回流*


**公式6**: $$$Y' = j\omega \left( P_i + P_p + P_c + P_o + P_e \right)^{-1}$$$

*管型/地下电缆并联导纳计算式，组合内部、管壁、空间及大地回流电位矩阵*


### 算法步骤

1. 几何与材料建模：定义导体截面尺寸、多层介质（空气/土壤/海水）电导率与磁导率，以及导体相对空间位置。

2. 等效定理应用：将导体内部体积替换为周围均匀介质，在导体表面引入等效面电流密度J，以维持外部电磁场分布不变。

3. 傅里叶级数展开：将表面切向电场E与电流密度J沿圆周角度展开为N阶傅里叶级数（工程取N=4），将连续场分布转化为离散系数向量。

4. 表面导纳算子构建：利用第一类贝塞尔函数及其导数建立傅里叶系数间的线性映射关系J=YsE，精确表征高频集肤效应。

5. 电场积分方程离散：引入考虑空气-大地界面或多层土壤的格林函数G，结合矢量电位与电报方程，应用矩量法得到离散矩阵方程E=jωμ0GJ+UZ'I。

6. 串联阻抗求解：联立导纳算子与离散方程，通过矩阵求逆运算Z'=[U^T(I-jωμ0YsG)^{-1}YsU]^{-1}，自动计及多导体邻近效应与复杂大地回流路径。

7. 并联导纳计算：根据线路拓扑（架空裸导线/管型电缆/单芯地下电缆）组合对应的电位矩阵（Pi, Pp, Pc, Po, Pe），通过Y'=jω(P_total)^{-1}求解频变导纳。

8. 频变参数拟合与集成：在目标频带内逐频计算Z'与Y'，生成频变传输线模型参数文件，直接导入EMTP进行时域电磁暂态仿真。


### 关键参数

- **傅里叶展开阶数**: N=4（兼顾精度与计算效率，N=0等效于忽略邻近效应）

- **计算频带范围**: 0.01 Hz 至 10 MHz

- **土壤模型支持**: 均匀土壤、多层分层土壤（含海水/海床界面）

- **集成仿真平台**: EMTP (Line/Cable Data模块)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 地下电缆邻近效应评估 | 针对3根单芯电缆（169kV网络，100km线路），在10μs注入雷击闪络。频域计算覆盖0.01Hz-10MHz，时域观测芯-地/芯-护套阻抗与暂态波形。 | 考虑邻近效应(N=4)的模型在MHz频段阻抗显著升高，暂态波形衰减率明显大于传统CC工具(N=0)；传统工具忽略邻近效应导致高频阻抗偏差，过电压预测偏保守。 |

| 并联导纳大地回流效应评估 | 针对263m三芯电缆进行1-150kHz扫频，并在41.8Mvar电容投切暂态中观测首端电压。对比计入/忽略大地回流电位矩阵Pe的模型。 | 计入Pe后，正序开路阻抗在谐振峰处幅值与频率发生显著偏移；暂态波形更平滑，最大过电压略低于忽略Pe的模型（后者与传统CC结果高度一致）。 |

| 架空HVDC与地下AC电缆平行耦合 | 400kV架空HVDC线路与132kV地下AC电缆平行敷设，AC电缆于5ms合闸，观测直流线路感应电压。 | 成功复现AC线路在HVDC正负极导体上感应的交流电压分量；传统LC/CC工具因无法处理架空-地下混合耦合，互阻抗矩阵为零，完全无法复现该现象。 |



## 量化发现

- 傅里叶级数取N=4即可满足高精度邻近效应建模要求，计算效率显著优于有限元法(FEM)，避免网格剖分带来的巨大计算负担。
- 在0.01 Hz至10 MHz宽频范围内，MoM-SO串联阻抗计算稳定，彻底克服了传统Carson/Pollaczek公式在高频段产生非物理传播模式的缺陷。
- 263m电缆在1-150kHz扫频中，并联导纳计入大地回流项(Pe)后，正序阻抗谐振峰位置与幅值发生显著偏移，验证了高频下大地回流对并联参数的关键影响。
- 10μs雷击注入仿真中，考虑邻近效应的暂态波形衰减率较忽略该效应的模型提升显著，最大过电压幅值差异在绝缘配合评估中不可忽略。


## 关键公式

### MoM-SO串联阻抗矩阵闭式解

$$$Z' = \left[ U^T \left( \mathbf{1} - j\omega\mu_0 Y_s G \right)^{-1} Y_s U \right]^{-1}$$$

*用于计算多导体系统（含实心/空心导体、多层土壤）的频变串联阻抗，自动计及集肤、邻近效应与大地回流*

### 架空线路并联导纳公式

$$$Y' = j\omega \left( P_s + P_e \right)^{-1}$$$

*用于计算架空裸导线或单芯架空电缆的并联导纳，Ps为镜像法空间电位矩阵，Pe为大地回流修正项*

### 管型/地下电缆并联导纳公式

$$$Y' = j\omega \left( P_i + P_p + P_c + P_o + P_e \right)^{-1}$$$

*用于复杂电缆结构（含护套、金属管、多层介质）的并联导纳计算，传统工具通常忽略Pe与部分内部电位项*

### 表面导纳算子傅里叶系数关系

$$$J_n = E_n \frac{2\pi}{j\omega} \left[ \frac{ka \mathcal{J}'_{|n|}(ka)}{\mu \mathcal{J}_{|n|}(ka)} - \frac{k_{out} a \mathcal{J}'_{|n|}(k_{out} a)}{\mu_0 \mathcal{J}_{|n|}(k_{out} a)} \right]$$$

*建立表面电场与电流密度的频域映射，是MoM-SO方法处理集肤效应与导体内部电磁场分布的核心*



## 验证详情

- **验证方式**: 频域扫频对比与时域暂态仿真验证（与传统Line/Cable Constants例程及忽略特定物理效应的简化模型进行交叉对比）
- **测试系统**: 169kV交叉互联地下电缆系统（100km）、263m三芯电缆、400kV架空HVDC与132kV地下AC平行混合线路
- **仿真工具**: EMTP (集成Line/Cable Data模块), 传统Line Constants/Cable Constants例程
- **验证结果**: 验证了MoM-SO在0.01Hz-10MHz宽频下精确计及集肤/邻近效应的能力；证实并联导纳大地回流项对高频谐振及暂态过电压幅值的关键影响；首次实现架空-地下混合线路电磁耦合仿真，结果符合物理预期且传统工具无法复现，整体精度媲美有限元法但计算效率显著提升。
