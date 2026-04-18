---
title: "Effects of cable insulations’ physical and geometrical parameters on sheath transients and insulation losses"
type: source
authors: ['Natheer Alatawneh']
year: 2019
journal: "Electrical Power and Energy Systems, 110 (2019) 95-106. doi:10.1016/j.ijepes.2019.02.047"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/j.ijepes.2019.02.047.pdf.pdf"]
---

# Effects of cable insulations’ physical and geometrical parameters on sheath transients and insulation losses

**作者**: Natheer Alatawneh
**年份**: 2019
**来源**: `13&14/files/j.ijepes.2019.02.047.pdf.pdf`

## 摘要

Effects of cable insulations’ physical and geometrical parameters on sheath Cysca Technologies Inc., 275A Pierre-Le Gardeur blvd., Repentigny, Quebec, Canada Polytechnique Montréal, 2900 boul. Édouard-Montpetit, Québec, Canada This paper investigates the influence of insulations’ physical and geometrical parameters on cable sheath transients and insulation losses considering power cables for high voltage alternating current (HVAC) applica-

## 核心贡献


- 提出基于有限元模型的暂态电压下电缆绝缘介质损耗计算方法
- 揭示绝缘介电常数与护套厚度对电缆电容及暂态过电压的影响规律
- 建立兼顾护套过电压与介质损耗的防护层最优介电常数选取方法


## 使用的方法


- [[emtp仿真|EMTP仿真]]
- [[有限元法-fem|有限元法(FEM)]]
- [[理论解析计算|理论解析计算]]
- [[数值电流计算|数值电流计算]]


## 涉及的模型


- [[单芯同轴电力电缆|单芯同轴电力电缆]]
- [[金属护套|金属护套]]
- [[绝缘层|绝缘层]]
- [[防护层|防护层]]


## 相关主题


- [[电缆参数计算|电缆参数计算]]
- [[护套暂态过电压|护套暂态过电压]]
- [[介质损耗分析|介质损耗分析]]
- [[绝缘参数优化|绝缘参数优化]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 主要发现


- 绝缘介电常数增大线性提升芯线与护套自电容护套厚度增加使护套电容指数衰减
- 暂态电压下绝缘层与防护层介质损耗分别为34.362W/m与3.365W/m
- 防护层相对介电常数存在最优值可同时实现护套过电压抑制与介质损耗最小化



## 方法细节

### 方法概述

本文采用理论解析、电磁暂态程序（EMTP）仿真与有限元（FEM）数值计算相结合的综合方法。首先基于静电场理论推导单芯同轴电缆的电容矩阵解析式，明确绝缘层与防护层介电常数及几何尺寸对自电容与互电容的影响规律。其次，在EMTP中构建1km长220kV/60Hz电缆的分布参数电路模型，设置特定终端电阻以模拟开路暂态条件，利用Cable Constants子程序计算波过程与护套过电压。最后，针对暂态电压下的介质损耗计算难题，提出一种基于FEM的数值电流积分法，通过求解绝缘层内的瞬态电场分布与泄漏电流，实现暂态损耗的精确量化，并与稳态解析公式进行交叉验证。

### 数学公式


**公式1**: $$$[C] = \begin{bmatrix} C_c & C_m \\ C_m & C_s \end{bmatrix}$$$

*单芯同轴电缆的电容矩阵，包含芯线自电容、护套自电容及芯-护套互电容*


**公式2**: $$$C_c = C_m = \frac{2\pi\varepsilon_0\varepsilon_1}{\ln(r_3/r_2)}$$$

*芯线自电容与芯-护套互电容解析式，仅与绝缘层介电常数$\varepsilon_1$及几何半径相关*


**公式3**: $$$C_s = \frac{2\pi\varepsilon_0\varepsilon_1\varepsilon_2}{\varepsilon_2\ln(r_3/r_2) + \varepsilon_1\ln(r_5/r_4)}$$$

*金属护套自电容解析式，同时受绝缘层与防护层介电常数及厚度影响*


**公式4**: $$$V_{smax} = k(1 - e^{-x})$$$

*护套最大暂态过电压理论表达式，用于量化介电参数与厚度对过电压的耦合影响*


**公式5**: $$$k = \frac{C_{cs}}{C_{cs}+C_{sg}}, \quad x = \frac{m \omega R_{sheath}}{\beta}, \quad m = \frac{C_{cs}+C_{sg}}{2}, \quad \beta = \frac{\omega}{v}, \quad v = \frac{c_0}{\sqrt{\varepsilon_1}}$$$

*过电压公式中的中间参数定义，涵盖电容比、衰减因子、波速与相位常数*


### 算法步骤

1. 建立单芯同轴电缆二维轴对称有限元几何模型，精确划分芯线、绝缘层($\varepsilon_1$)、金属护套、防护层($\varepsilon_2$)及大地边界，设置材料本构关系与网格剖分策略。

2. 在EMTP中配置1km电缆的频变分布参数模型，发送端施加1 pu阶跃电压激励，接收端芯线与护套保持开路状态，护套接地端分别串联$R_{s1}=10\ \Omega$（发送端）与$R_{s2}=1\ \text{M}\Omega$（接收端）以模拟实际接地与绝缘条件。

3. 调用EMTP内置的Cable Constants子程序，遍历不同$\varepsilon_1$、$\varepsilon_2$、护套厚度$d$及土壤电阻率$\rho_e$组合，计算各工况下的波阻抗矩阵与传播常数，生成暂态电压波形数据。

4. 将EMTP输出的芯线与护套暂态电压波形作为FEM模型的时变Dirichlet边界条件，在0-2 ms时间窗口内求解绝缘层与防护层内部的瞬态电场强度分布$\mathbf{E}(t)$。

5. 基于麦克斯韦方程组数值计算流过绝缘介质的位移电流与传导电流密度$\mathbf{J}(t)$，通过体积分公式$P_{loss} = \int_V \mathbf{E}(t) \cdot \mathbf{J}(t) dV$逐时步积分，获取暂态介质损耗功率。

6. 将FEM计算的暂态损耗结果与工频稳态经典解析公式进行对比，验证数值方法的收敛性、时间步长敏感性及工程适用精度。


### 关键参数

- **几何尺寸**: $r_2=25.4\ \text{mm}, r_3=45.6\ \text{mm}, r_4=50.8\ \text{mm}, r_5=65.9\ \text{mm}$

- **材料电阻率**: $\rho_c=3.19\times10^{-8}\ \Omega\cdot\text{m}, \rho_s=1.87\times10^{-7}\ \Omega\cdot\text{m}$

- **介电常数范围**: $\varepsilon_1 \in [1,4], \varepsilon_2 \in [1,6], \varepsilon_0=10^{-9}/36\pi\ \text{F/m}$

- **土壤电阻率**: $\rho_e \in [10, 2000]\ \Omega\cdot\text{m}$

- **电气与运行参数**: 额定电压220 kV (相电压峰值179.63 kV), 频率60 Hz, 电缆长度1 km, 埋深0.75 m

- **终端接地电阻**: $R_{s1}=10\ \Omega$ (发送端), $R_{s2}=1\ \text{M}\Omega$ (接收端)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 绝缘层介电常数$\varepsilon_1$变化对护套过电压的影响 | 当$\varepsilon_1$从1增至4时，护套接收端最大过电压$V_{smax}$从约0.42 pu线性上升至0.55 pu（$\rho_e=100\ \Omega\cdot\text{m}$）。芯线接收端电压$V_{c2}$首个峰值因大地回流衰减至1.4 pu，第二峰值达1.55 pu。 | 相比基准值$\varepsilon_1=2.3$，过电压峰值增加约18%，验证了高介电常数绝缘材料会加剧暂态过电压风险。 |

| 防护层介电常数$\varepsilon_2$变化对护套过电压的影响 | 当$\varepsilon_2$从1增至6时，$V_{smax}$从0.62 pu指数衰减至0.41 pu。行波到达时间从13.5 $\mu$s延迟至35.5 $\mu$s，且波形阻尼显著增强。 | 相比低介电常数工况，过电压抑制效果达33.8%，表明提高防护层介电常数可有效吸收暂态能量。 |

| 防护层厚度$d$变化对护套自电容的影响 | 当$d$从0.2 mm增至20 mm时，护套自电容$C_s$从3.3 $\mu\text{F/km}$指数衰减至0.06 $\mu\text{F/km}$。护套最大过电压$V_{smax}$随厚度增加呈指数上升趋势。 | 电容衰减幅度达98.2%，证明防护层厚度是调控护套对地耦合电容与暂态电压分布的关键几何参数。 |

| 土壤电阻率$\rho_e$变化对暂态波形的影响 | 当$\rho_e$从10增至2000 $\Omega\cdot\text{m}$时，护套接收端电压$V_{s2}$到达时间从22.4 $\mu$s延迟至30.3 $\mu$s，峰值从0.47 pu升至0.52 pu。 | 高土壤电阻率使波过程延迟约35%，且过电压峰值提升10.6%，凸显接地条件对暂态评估的重要性。 |



## 量化发现

- 在0-2 ms暂态电压激励下，绝缘层介质损耗精确计算值为34.362 W/m，防护层介质损耗为3.365 W/m。
- 护套接收端最大过电压$V_{smax}$随$\varepsilon_1$增大呈线性增长，随$\varepsilon_2$增大呈指数衰减，存在最优$\varepsilon_2$平衡点。
- 芯线接收端电压$V_{c2}$首个峰值因大地回流与内部阻抗衰减至1.4 pu，第二峰值达1.55 pu，行波到达时间为6.1 $\mu$s。
- 护套发送端过电压$V_{s1}$初始峰值为0.3 pu，接收端$V_{s2}$在约39 $\mu$s时达到峰值0.49 pu。
- 防护层厚度$d$每增加1 mm，护套对地电容$C_{sg}$下降约15%，导致$V_{smax}$呈指数上升趋势。
- FEM暂态损耗计算方法在稳态工况下与经典解析公式误差<2%，验证了数值积分法的工程可靠性。


## 关键公式

### 护套最大暂态过电压解析式

$$$V_{smax} = k(1 - e^{-x})$$$

*用于评估绝缘介电参数与防护层厚度对护套暂态过电压的定量影响，指导防护层材料选型*

### 金属护套自电容计算公式

$$$C_s = \frac{2\pi\varepsilon_0\varepsilon_1\varepsilon_2}{\varepsilon_2\ln(r_3/r_2) + \varepsilon_1\ln(r_5/r_4)}$$$

*揭示几何尺寸与双层介电参数的耦合关系，是计算波阻抗与传播常数的基础*

### 基于FEM的瞬态介质损耗数值积分公式

$$$P_{loss} = \int_V \mathbf{E}(t) \cdot \mathbf{J}(t) dV$$$

*用于暂态工况下绝缘层与防护层损耗的精确评估，弥补传统稳态公式在快速暂态过程中的不足*



## 验证详情

- **验证方式**: 理论解析对比与多物理场交叉验证
- **测试系统**: 1 km长单芯同轴地下电力电缆（220 kV/60 Hz），埋深0.75 m，终端开路配置
- **仿真工具**: EMTP (Cable Constants子程序), 有限元分析软件 (FEM)
- **验证结果**: 提出的FEM暂态损耗计算方法在稳态工况下与经典解析公式误差<2%；EMTP仿真得到的波过程（如$V_{c2}$到达时间6.1 $\mu$s，$V_{s2}$峰值0.49 pu）与行波理论预测高度一致，验证了模型在暂态过电压与损耗评估中的可靠性。
