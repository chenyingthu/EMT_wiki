---
title: "Proximity effect in fast transient simulations of an underground transmission cable"
type: source
authors: ['U.S. Gudmundsdottir']
year: 2014
journal: "Electric Power Systems Research, Corrected proof. doi:10.1016/j.epsr.2014.03.016"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/32/j.epsr.2014.03.016.pdf.pdf"]
---

# Proximity effect in fast transient simulations of an underground transmission cable

**作者**: U.S. Gudmundsdottir
**年份**: 2014
**来源**: `32/j.epsr.2014.03.016.pdf.pdf`

## 摘要

1. Introduction conductor (also called metal screen) should be more accurately rep- resented in the simulation software [3]. The analysis revealed how Nowadays, extruded (XLPE) cables are the most common cable the wired characteristics of the metal screen of the HV cable and types in high voltage...

## 核心贡献


- 提出导体细分法计算含邻近效应的电缆频变串联阻抗矩阵
- 将外部计算的阻抗矩阵导入通用线路模型替代传统CC解析法
- 精确建模铜线铝复合屏蔽层及半导电层并计入大地回路阻抗


## 使用的方法


- [[导体细分法|导体细分法]]
- [[通用线路模型|通用线路模型]]
- [[电缆常数法|电缆常数法]]
- [[几何平均距离法|几何平均距离法]]
- [[频变参数拟合|频变参数拟合]]


## 涉及的模型


- [[高压xlpe电缆|高压XLPE电缆]]
- [[金属屏蔽层|金属屏蔽层]]
- [[半导电层|半导电层]]
- [[通用线路模型|通用线路模型]]
- [[大地回路|大地回路]]


## 相关主题


- [[邻近效应建模|邻近效应建模]]
- [[频率相关建模|频率相关建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[电缆参数计算|电缆参数计算]]
- [[护套间模态传播|护套间模态传播]]


## 主要发现


- 引入邻近效应后高频振荡衰减显著改善护套间模态仿真精度大幅提升
- 改进模型仿真结果与现场实测数据高度吻合验证了导体细分法有效性
- 传统CC法在十千赫兹以上频段阻尼不足新模型有效修正串联阻抗虚部



## 方法细节

### 方法概述

本文提出一种结合导体细分法（Conductor Partitioning Method）与通用线路模型（Universal Line Model/FDPM）的混合仿真方法。首先将电缆导体（芯线、屏蔽层铜线部分、铝层）细分为多个子导体（subconductors/filaments），在MATLAB中基于几何平均距离（GMD）法计算包含邻近效应和集肤效应的频变串联阻抗矩阵Z(ω)。然后将计算得到的Z(ω)作为外部数据导入EMT仿真软件（PSCAD/EMTDC），替代传统电缆常数法（CC Method）的解析计算，而导纳矩阵Y(ω)仍采用传统CC法计算。该方法特别处理了半导电层（semiconductive layers）和复合屏蔽层（铜线+铝层）的电磁特性，并包含大地回路阻抗。

### 数学公式


**公式1**: $$$R_i = \frac{\rho}{A_i}$$$

*子导体电阻计算公式，其中ρ为电阻率，Ai为第i个子导体的横截面积*


**公式2**: $$$L_{ii} = \frac{\mu_0}{2\pi} \ln\frac{r_q}{D_{ii}}$, $L_{ij} = \frac{\mu_0}{2\pi} \ln\frac{r_q}{D_{ij}}$$$

*自感和互感计算公式，基于几何平均距离（GMD）法，rq为远大于GMD的参考距离，Dii为自几何平均距离，Dij为互几何平均距离*


**公式3**: $$$C = \frac{2\pi\varepsilon}{\ln(b/a)}$$$

*单位长度电容计算公式，ε为绝缘层介电常数，b为外半径，a为内半径*


**公式4**: $$$\varepsilon_{eff} = \varepsilon_s \cdot \frac{\ln(r_i/r_o)}{\ln(b/a)}$$$

*半导电层等效介电常数修正公式，εs为纯XLPE介电常数（2.3），ri为金属屏蔽层内半径，ro为导体外半径*


**公式5**: $$$\begin{bmatrix} V_{C} \\ V_{Sh1} \\ V_{Sh2} \end{bmatrix} = [R] \cdot \begin{bmatrix} I_{C} \\ I_{Sh1} \\ I_{Sh2} \end{bmatrix} + j\omega[L] \begin{bmatrix} I_{C} \\ I_{Sh1} \\ I_{Sh2} \end{bmatrix}$$$

*单芯电缆电压-电流关系矩阵方程，其中Sh1为铜线屏蔽部分，Sh2为铝层部分，[R]和[L]为N×N矩阵（N=n1+n2+n3）*


**公式6**: $$$Z_{total} = \begin{bmatrix} [R_{C1}] & & \\ & [R_{C2}] & \\ & & [R_{C3}] \end{bmatrix} + j\omega \begin{bmatrix} [L_{C1}] & [L_{C1C2}] & [L_{C1C3}] \\ [L_{C1C2}] & [L_{C2}] & [L_{C2C3}] \\ [L_{C1C3}] & [L_{C2C3}] & [L_{C3}] \end{bmatrix}$$$

*三相电缆完整阻抗矩阵构建，包含三相之间的互耦和每相内部子导体的自阻抗*


### 算法步骤

1. 步骤1：几何建模与细分。将每相电缆的导体芯（n1个子导体）、铜线屏蔽层（n2个子导体）和铝层（n3个子导体）按指数分布进行细分，表面附近网格更密，以准确捕捉集肤效应和邻近效应。

2. 步骤2：坐标分配。为每个子导体分配x-y坐标，三相电缆按紧密三叶形（tight trefoil）或平面排列布置，以(0,0)为中心。

3. 步骤3：计算几何平均距离（GMD）。分别计算自几何平均距离（self-GMD）和互几何平均距离（mutual-GMD），区分远距离和近距离元素的不同计算方法。

4. 步骤4：构建电阻矩阵[R]。基于每个子导体的截面积和材料电阻率，构建对角电阻矩阵。

5. 步骤5：计算电感矩阵[L]。基于GMD方法计算所有子导体之间的自感和互感，考虑 fictitious return path（假想无损返回路径）。

6. 步骤6：组装全相阻抗矩阵Z(ω)。将三相所有子导体的阻抗矩阵组装成完整的频变阻抗矩阵，包含导体内部和三相之间的所有电磁耦合。

7. 步骤7：计算导纳矩阵Y(ω)。使用传统电缆常数法（CC Method）计算导纳，包含半导电层介电常数修正。

8. 步骤8：导入通用线路模型。将外部计算的Z(ω)导入EMTDC/PSCAD的通用线路模型（FDPM），替代原有的解析Z(ω)计算，进行电磁暂态仿真。


### 关键参数

- **n1**: 导体芯细分数量（通常为数十至数百个filaments）

- **n2**: 铜线屏蔽层细分数量

- **n3**: 铝层屏蔽细分数量

- **ε_s**: 纯XLPE绝缘介电常数，取值为2.3

- **μ_0**: 真空磁导率，4π×10^-7 H/m

- **r_q**: 假想返回路径半径，远大于任何GMD值

- **f_critical**: 邻近效应显著频率阈值，约10 kHz



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 护套间模态（Intersheath Mode）高频振荡衰减 | 在10 kHz以上频率范围，包含邻近效应的模型显示出明显更高的阻尼特性，高频振荡衰减速度显著快于传统CC方法。仿真波形与现场实测数据在波形形状、衰减时间和幅值上均达到高度一致。 | 传统CC方法在10 kHz以上频段存在阻尼不足（inadequate damping）问题，改进模型修正了串联阻抗虚部，使高频段仿真精度显著提升 |

| 三相电缆系统暂态过电压 | 对三相单芯XLPE电缆系统进行快速暂态仿真，考虑复合屏蔽层（铜线+铝层）和半导电层的精确建模，仿真结果与现场测量数据对比误差显著降低。 | 相比传统方法仅将屏蔽层视为均匀圆柱导体，新模型考虑铜线结构的非均匀电流分布，在护套间模态传播特性上实现与实测数据的良好吻合（good comparison） |



## 量化发现

- 邻近效应在频率超过10 kHz时变得显著，传统电缆常数法在此频段以上会产生明显的阻抗虚部计算误差
- 传统CC方法由于缺乏邻近效应建模，导致护套间模态（intersheath mode）的高频振荡呈现不足的阻尼特性（inadequate damping for higher frequency oscillations 10 kHz and above）
- 改进模型通过导体细分法，将屏蔽层电流分布的非均匀性纳入计算，使串联阻抗的虚部（imaginary part of series impedance）计算更加准确
- 半导电层介电常数需按公式ε = 2.3 × ln(ri/ro)/ln(b/a)进行修正，以准确反映其在高频下的电气特性
- 采用指数分布的子导体细分策略，在导体表面附近使用更细密的网格（thinner subconductors），以精确捕捉电流密度的高梯度变化


## 关键公式

### 基于GMD的互感计算公式

$$$L_{ij} = \frac{\mu_0}{2\pi} \ln\frac{r_q}{D_{ij}}$$$

*用于计算任意两个子导体（filaments）之间的互感，是构建频变阻抗矩阵的基础*

### 半导电层等效介电常数修正公式

$$$\varepsilon = \varepsilon_s \cdot \frac{\ln(r_i/r_o)}{\ln(b/a)}$$$

*在计算电缆导纳矩阵时，对半导电层（semiconductive layers）的介电常数进行修正，以考虑其几何和材料特性*

### 频变阻抗矩阵

$$$Z(\omega) = R(\omega) + j\omega L(\omega)$$$

*通过导体细分法计算得到的频变串联阻抗，作为外部输入导入通用线路模型，替代传统解析法*



## 验证详情

- **验证方式**: 现场测量数据验证（Field Measurements Verification），与仿真结果进行时域波形对比
- **测试系统**: 高压（HV）XLPE地下输电电缆系统，三相单芯电缆，采用紧密三叶形（tight trefoil）敷设方式，包含复合金属屏蔽层（铜线+铝层）和半导电层
- **仿真工具**: MATLAB（用于导体细分法编程计算Z(ω)），PSCAD/EMTDC（电磁暂态仿真，使用通用线路模型FDPM）
- **验证结果**: 改进模型与现场实测数据达到良好吻合（good comparison），特别是在护套间模态（intersheath mode）传播特性方面，验证了导体细分法在考虑邻近效应和集肤效应方面的有效性。传统CC方法在10 kHz以上频段因忽略邻近效应导致阻尼不足，而新模型通过精确建模铜线屏蔽层的非均匀电流分布，有效修正了高频段串联阻抗特性。
