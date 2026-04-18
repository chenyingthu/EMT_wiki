---
title: "An improved approach for modeling lightning transients of wind turbines"
type: source
authors: ['ZhangXiaoqing']
year: 2018
journal: "Electrical Power and Energy Systems, 101 (2018) 429-438. doi:10.1016/j.ijepes.2018.04.006"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An improved approach for modeling lightning transients of wind turbines.pdf"]
---

# An improved approach for modeling lightning transients of wind turbines

**作者**: ZhangXiaoqing
**年份**: 2018
**来源**: `07&08/An improved approach for modeling lightning transients of wind turbines.pdf`

## 摘要

An improved approach for modeling lightning transients of wind turbines a School of Electrical Engineering, Beijing Jiaotong University, Beijing, China b Global Energy Interconnection Research Institute, Beijing, China A modeling approach is proposed in this paper for calculating lightning transient responses on wind turbines (WTs). The equivalent circuits are built for blade, dynamic contact part, tower body and grounding system,

## 核心贡献


- 提出将风机塔筒离散为截头棱锥多导体系统的等效电路模型更精确描述实际几何特征
- 建立包含叶片动态接触部件塔筒及接地系统的完整风机雷击暂态电路模型
- 基于诺伊曼积分与电磁类比法计算分段线路参数实现高频雷击暂态精确求解


## 使用的方法


- [[等效电路建模|等效电路建模]]
- [[多导体系统离散化|多导体系统离散化]]
- [[诺伊曼积分法|诺伊曼积分法]]
- [[电磁类比法|电磁类比法]]
- [[分段π型电路模型|分段Π型电路模型]]


## 涉及的模型


- [[风力发电机|风力发电机]]
- [[风机叶片|风机叶片]]
- [[风机塔筒|风机塔筒]]
- [[接地系统|接地系统]]
- [[动态接触部件|动态接触部件]]


## 相关主题


- [[雷击暂态分析|雷击暂态分析]]
- [[风机暂态建模|风机暂态建模]]
- [[接地系统高频建模|接地系统高频建模]]
- [[多导体系统电磁暂态|多导体系统电磁暂态]]
- [[风电防雷设计|风电防雷设计]]


## 主要发现


- 实验室缩比模型实验验证了所提电路模型计算结果与实测数据高度吻合
- 改进的截头棱锥塔筒模型能更准确反映实际几何特征对雷击暂态响应的影响
- 模型成功应用于2MW实际风机有效预测了雷击过程中的塔顶电位升高幅值



## 方法细节

### 方法概述

本文提出一种基于多导体系统离散化与等效电路建模的风机雷击电磁暂态计算方法。首先将风机雷电流路径划分为叶片、动态接触部件、塔筒和接地系统四部分。针对塔筒，摒弃传统传输线波阻抗或圆柱笼模型，将其离散为截头棱锥多导体系统，以更精确反映实际圆台几何特征。各分段参数通过诺伊曼积分计算自感与互感，利用电磁类比法推导电容，并结合集肤效应计算电阻。随后将各部件等效为Π型或耦合电路单元并级联，形成全机集中参数电路模型。最后采用时域离散化技术将动态元件转化为等效电流源与并联电阻，构建纯电阻网络，通过节点电压法求解雷击暂态响应。

### 数学公式


**公式1**: $$$L_{vj} = \frac{\mu_0}{4\pi} \left[ 2 + \Psi\left(\frac{\Delta l_b}{a}\right) + \Psi\left(-\frac{\Delta l_b}{a}\right) + \Psi\left(\frac{-2h}{a}\right) + \Psi\left(-\frac{2h+2\Delta l_b}{a}\right) - 2\Psi\left(-\frac{\Delta l_b+2h}{a}\right) \right]$$$

*垂直分段自感计算公式，基于镜像法与诺伊曼积分，考虑地面影响*


**公式2**: $$$L_{ij} = \frac{\mu_0}{2\pi} \left[ \Delta l_b \tanh^{-1}\frac{\Delta l_b}{\sqrt{a^2+\Delta l_b^2}} + 2(w+\Delta l_b)\tanh^{-1}\frac{\Delta l_p}{2} + 2bh - 2w\tanh^{-1}\frac{\Delta l_p}{1} \right]$$$

*倾斜分段自感计算公式，用于叶片非垂直姿态下的电感求解*


**公式3**: $$$R_b = \frac{\pi f_m \rho \mu \Delta l_b}{\pi [1-\exp(-a/\sqrt{\rho/\pi f_m \mu})][2a-\sqrt{\rho/\pi f_m \mu}(1-\exp(-a/\sqrt{\rho/\pi f_m \mu}))]}$$$

*考虑高频集肤效应的分段电阻计算公式*


**公式4**: $$$C = \mu_0 \varepsilon_0 L^{-1}$$$

*基于电磁类比法，由电感矩阵求逆得到多导体系统电容矩阵*


**公式5**: $$$G_{eh} = \frac{2\pi}{\rho \Psi_{eh}} \Delta l_{eh}, \quad L_{eh} = \frac{\mu_0}{2\pi} \Psi_{eh} \Delta l_{eh}, \quad C_{eh} = \frac{2\pi \varepsilon_0 \varepsilon_r}{\Psi_{eh}} \Delta l_{eh}$$$

*接地系统水平分支的导纳、电感与电容参数计算公式*


### 算法步骤

1. 1. 几何离散化与分段：将叶片引下线、塔筒纵向与横向结构按临界长度$l_{cr}=0.1c/f_m$进行分段，塔筒圆台近似为截头棱锥网格，接地网水平环按高频要求细分，垂直接地极保持单段。

2. 2. 电磁参数计算：对每一分段及其镜像，利用诺伊曼双重线积分计算自感与互感（区分共面/非共面、平行/倾斜情况），构建全局电感矩阵$L$；通过$C=\mu_0\varepsilon_0 L^{-1}$求电容矩阵；结合材料电阻率与频率计算考虑集肤效应的电阻。

3. 3. 等效电路组装：将各分段替换为Π型电路单元（叶片/接地）或耦合电路单元（塔筒，仅考虑相邻互感耦合），动态接触部件简化为$R_C$与$C_S$并联单元，按雷电流路径串联/并联形成全机集中参数网络。

4. 4. 时域求解：在叶片接闪点注入雷电流源$i_s$（并联通道波阻抗$Z=400\Omega$），采用时域离散化算法将电容与RL支路转化为等效电流源与并联电阻，构建纯电阻导纳矩阵，通过节点分析法迭代求解各节点暂态电压与电流波形。


### 关键参数

- **临界分段长度**: $l_{cr} = 0.1c/f_m$（$c=3\times10^8$ m/s）

- **雷击通道波阻抗**: $Z \approx 400\ \Omega$

- **真空磁导率**: $\mu_0 = 4\pi \times 10^{-7}$ H/m

- **真空介电常数**: $\varepsilon_0 = (36\pi)^{-1} \times 10^{-9}$ F/m

- **后续负雷击波前时间**: 0.25/100 $\mu$s

- **叶片偏转角**: $\theta = 10^\circ$

- **接地极典型长度**: 2-3 m



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 实验室缩比风机模型验证 | 在高压实验室搭建缩比模型，注入快前沿冲击电流。计算波形与200MHz示波器实测波形高度吻合，峰值电位误差显著低于传统级联空心导体模型与圆柱导体笼模型。 | 相比文献[3-6]的传统塔筒模型，本模型计算的峰值电位与实测值偏差最小，波形上升沿与高频振荡特征匹配度提升，验证了截头棱锥离散化对高频暂态的精确描述能力。 |

| 2MW实际风机工程应用 | 将模型应用于国产2MW实际风机，输入实际几何尺寸与土壤参数，成功预测雷击过程中塔顶电位升高幅值及沿塔筒传播的暂态过电压分布。 | 克服了传统均匀波阻抗模型无法反映塔筒变截面几何特征的缺陷，为2MW风机防雷绝缘配合与接地网优化提供了定量设计依据。 |



## 量化发现

- 分段长度必须满足$\Delta l < 0.1c/f_m$以保证高频雷击暂态（最高频率$f_m$）的数值稳定性与精度
- 雷击通道波阻抗典型取值$Z=400\ \Omega$，直接影响接闪点初始电压幅值
- 后续负雷击波前时间极短（0.25/100 $\mu$s），接地系统必须采用分布参数Π型电路建模，不可简化为集中接地电阻
- 塔筒离散为截头棱锥多导体系统后，相邻分段间的互感与互容耦合显著影响高频振荡频率，仅考虑相邻耦合即可满足工程精度
- 动态接触部件等效为$R_C$与$C_S$并联单元，有效表征了滑环与轴承在高频下的分流与耦合特性


## 关键公式

### 横向分段互感诺伊曼积分公式

$$$L_{j,k} = \frac{\mu_0}{4\pi} \left[ \int_{\Delta l_j} \int_{\Delta l_k} \frac{dl_j \cdot dl_k}{r_{jk}} + \int_{\Delta l'_j} \int_{\Delta l_k} \frac{dl'_j \cdot dl_k}{r'_{jk}} \right]$$$

*用于计算塔筒截头棱锥网格中任意两个横向分段（含镜像）的互感，是构建多导体电感矩阵的核心*

### 电磁类比电容矩阵公式

$$$C = \mu_0 \varepsilon_0 L^{-1}$$$

*在均匀介质假设下，通过求逆电感矩阵直接获得多导体系统的电容矩阵，避免复杂的电位系数积分*

### 接地网几何修正因子公式

$$$\Psi_{eh} = \ln \frac{2l_{eh}}{r_{eh}} - 1, \quad \Psi_{ep} = \ln \frac{2l_{ep}}{r_{ep}} \frac{3l_{ep}+4t}{l_{ep}+4t} - 1$$$

*用于计算水平环形接地网与垂直接地极的分布参数，修正埋深$t$与导体半径对高频阻抗的影响*



## 验证详情

- **验证方式**: 实验室缩比模型冲击电流注入实验 + 实际风机工程算例对比分析
- **测试系统**: 实验室搭建的缩比风机物理模型（含叶片、塔筒、接地网）及国产2MW实际风机系统
- **仿真工具**: 自研节点分析法时域求解程序（基于时域离散化与等效电流源替换），200MHz带宽数字示波器（实测采集）
- **验证结果**: 实验室实测波形与仿真波形在上升时间、峰值及高频振荡特征上高度一致；峰值电位计算精度优于传统级联空心导体模型与圆柱导体笼模型；成功应用于2MW风机，验证了模型在工程防雷设计中的适用性与高频暂态预测能力。
