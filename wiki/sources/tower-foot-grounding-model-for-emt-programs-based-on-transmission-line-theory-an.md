---
title: "Tower-foot grounding model for EMT programs based on transmission line theory and Marti's model"
type: source
authors: ['Rafael Alipio']
year: 2023
journal: "Electric Power Systems Research, 223 (2023) 109584. doi:10.1016/j.epsr.2023.109584"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/38/Alipio 等 - 2023 - Tower-foot grounding model for EMT programs based on transmission line theory and Marti's model.pdf"]
---

# Tower-foot grounding model for EMT programs based on transmission line theory and Marti's model

**作者**: Rafael Alipio
**年份**: 2023
**来源**: `38/Alipio 等 - 2023 - Tower-foot grounding model for EMT programs based on transmission line theory and Marti's model.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. Tower-foot grounding model for EMT programs based on transmission line Rafael Alipio a,1,*, Alberto De Conti b, Felipe Vasconcellos c, Fernando Moreira c, Naiara Duarte a, a Electromagnetic Compatibility Laboratory, Swiss Federal Institute of Technology in Lausanne (EPFL), 1015, Switzerland b Department of Electrical Engineering, Federal University of Minas Gerais, Belo Horizonte, MG, Brazil

## 核心贡献



- 提出了一种基于传输线理论与Marti模型的杆塔接地系统EMT仿真模型
- 在ATP平台中实现该模型，并验证了其在雷击暂态、地电位升、绝缘子过电压及反击跳闸率计算中的高精度

## 使用的方法


- [[transmission-line]]
- [[frequency-dependent]]
- [[numerical-integration]]

## 涉及的模型


- [[transmission-line]]

## 相关主题


- [[transmission-line]]
- [[frequency-dependent]]

## 主要发现



- 基于传输线理论的接地模型在模拟地电位升和绝缘子过电压方面与全波电磁基准模型高度一致
- 该模型克服了传统集中电阻模型的局限性，能够更准确地评估输电线路的雷击反击跳闸率，同时兼顾了计算效率

## 方法细节

### 方法概述

该论文提出了一种基于传输线理论和Marti模型的杆塔接地系统EMT仿真模型。核心思想是将接地极（counterpoise wires）建模为埋地传输线，通过求解电报方程并应用Marti的频率相关传输线模型（FDLine）来考虑接地系统的频率依赖特性。模型考虑了四根辐射状接地导体的电磁耦合，通过对称性简化将问题转化为两根耦合传输线的等效表示，计算其单位长度参数（阻抗、电感、电导、电容），并在ATP中实现为稳定且计算高效的频率相关模型。

### 数学公式


**公式1**: $$$\frac{d\mathbf{V}}{dx} = -\mathbf{Z}_i\mathbf{I} - j\omega\mathbf{L}\mathbf{I}$$$

*电报方程的电压方程，描述沿传输线电压变化与电流的关系，其中Zi为导体内部阻抗矩阵，L为外部电感矩阵*


**公式2**: $$$\frac{d\mathbf{I}}{dx} = -(\mathbf{G} + j\omega\mathbf{C})\mathbf{V}$$$

*电报方程的电流方程，描述沿传输线电流变化与电压的关系，其中G为电导矩阵，C为电容矩阵*


**公式3**: $$$R_S = \frac{1}{\pi\sigma_g}\left[\ln\left(\frac{2l}{\sqrt{2hr}}\right) - 1\right]$$$

*基于Sunde公式的自接地电阻计算，σg为土壤电导率，l为接地极总长度，h为埋深(0.8m)，r为导体半径(4.7625mm)*


**公式4**: $$$R_M = \frac{e^{-\gamma_g d}}{\pi\sigma_g}\left[\ln\left(\frac{2l}{\sqrt{2hd}}\right) - 1\right]$$$

*互电阻计算，考虑地中传播延迟，γg为地的固有传播常数，d为等效间距*


**公式5**: $$$\gamma_g = \sqrt{j\omega\mu_0(\sigma_g + j\omega\varepsilon_g)}$$$

*土壤的固有传播常数，μ0为真空磁导率，εg为土壤介电常数*


**公式6**: $$$d = \frac{d_1l_1 + d_2l_2}{l}$$$

*等效间距计算，d1为对角部分平均间距，d2为平行部分间距(20m)，l1和l2分别为两段长度*


**公式7**: $$$\mathbf{G} = \mathbf{R}^{-1}, \quad \mathbf{C} = \frac{\varepsilon_g}{\sigma_g}\mathbf{G}$$$

*单位长度电导和电容矩阵计算，基于准静态近似*


### 算法步骤

1. 根据土壤电阻率ρg确定接地极最优长度l（250Ωm对应15m，500Ωm对应25m，1000Ωm对应40m，2500Ωm对应55m，5000Ωm对应80m）

2. 计算接地极几何参数：埋深h=0.8m，半径r=4.7625mm，塔基宽度6m，平行段间距d2=20m

3. 构建2×2的电阻矩阵R：对角元素RS使用Sunde公式(3)计算自电阻，非对角元素RM使用公式(4)计算考虑传播延迟的互电阻

4. 计算单位长度参数矩阵：电导矩阵G=R^(-1)，电容矩阵C=(εg/σg)G，内部阻抗Zi和电感L根据导体特性计算

5. 对耦合传输线进行模态分解，将相量转换为模态量，得到模态特征阻抗Zc(ω)和传播函数A(ω)

6. 使用Marti模型拟合频率相关的模态特征阻抗和传播函数（采用有理函数逼近，如图4和图5所示）

7. 在ATP中实现为FDLine模型，设置频率相关参数，与138kV线路模型、杆塔模型、雷电流源连接

8. 注入Heidler函数表示的雷电流（峰值31kA，虚拟波头时间3.8μs）进行瞬态仿真


### 关键参数

- **soil_resistivity**: 250-5000 Ωm（5个典型值）

- **soil_permittivity**: εg = 10ε0（相对介电常数10）

- **burial_depth**: h = 0.8 m

- **conductor_radius**: r = 4.7625 mm (3/8英寸)

- **counterpoise_length**: l = 15-80 m（根据土壤电阻率调整）

- **tower_base_width**: 6 m

- **electrode_separation**: d2 = 20 m

- **lightning_peak_current**: 31 kA

- **virtual_front_time**: 3.8 μs

- **line_voltage**: 138 kV

- **conductor_type**: ACSR LINNET（相线），3/8英寸EHS（避雷线）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 地电位升(GPR)对比验证 | 在五种土壤电阻率(250-5000Ωm)下，比较Marti传输线模型与混合电磁模型(HEM)的GPR峰值。250Ωm时：Marti模型212kV，HEM模型223kV；500Ωm时：288kV vs 293kV；1000Ωm时：390kV vs 387kV；2500Ωm时：691kV vs 688kV；5000Ωm时：906kV vs 911kV | GPR峰值误差在0.4%-4.9%范围内，高土壤电阻率时误差更小(<1%)，低电阻率时最大误差4.9% |

| 绝缘子过电压计算 | 通过比较GPR波形和绝缘子串过电压，验证模型在雷击暂态下的精度，模型能准确再现HEM的波形特征 | 波形吻合度高，能够准确预测绝缘子承受的过电压幅值和波形 |

| 反击跳闸率评估 | 应用该模型评估输电线路的雷击反击性能(backflashover outage rate) | 模型精度足以用于工程实际的雷击性能评估，同时保持计算效率 |



## 量化发现

- GPR峰值计算误差随土壤电阻率变化：250Ωm时误差最大为4.9%，500Ωm时为1.7%，1000Ωm时为0.8%，2500Ωm时为0.4%，5000Ωm时为0.5%
- 接地极长度根据土壤电阻率优化设置：250Ωm对应15m，500Ωm对应25m，1000Ωm对应40m，2500Ωm对应55m，5000Ωm对应80m
- 雷电流参数：峰值31kA，虚拟波头时间3.8μs（基于Mount San Salvatore测量数据）
- 接地系统埋深0.8m，导体半径4.7625mm，塔基宽度6m，平行段间距20m
- 在高土壤电阻率(≥1000Ωm)下，传输线模型与电磁场模型(HEM)的差异小于1%
- 模型在保持与全波电磁模型相当精度的同时，显著降低了计算复杂度，适用于大规模EMT仿真


## 关键公式

### Sunde接地电阻公式

$$$R_S = \frac{1}{\pi\sigma_g}\left[\ln\left(\frac{2l}{\sqrt{2hr}}\right) - 1\right]$$$

*计算单根水平接地极的自电阻，用于构建单位长度参数矩阵的对角元素*

### 修正互电阻公式

$$$R_M = \frac{e^{-\gamma_g d}}{\pi\sigma_g}\left[\ln\left(\frac{2l}{\sqrt{2hd}}\right) - 1\right]$$$

*计算两根平行接地极之间的互电阻，考虑地中波传播的指数衰减项*

### 耦合电报方程

$$$\frac{d\mathbf{V}}{dx} = -(\mathbf{Z}_i + j\omega\mathbf{L})\mathbf{I}, \quad \frac{d\mathbf{I}}{dx} = -(\mathbf{G} + j\omega\mathbf{C})\mathbf{V}$$$

*描述埋地导体中电压电流传输的基本方程，是Marti传输线模型的基础*



## 验证详情

- **验证方式**: 与混合电磁模型(HEM, Hybrid Electromagnetic Model)进行对比验证，作为基准模型(benchmark)
- **测试系统**: 典型138kV架空输电线路，包含杆塔几何结构、ACSR相线(LINNET)、3/8英寸EHS避雷线、四辐射状接地极(counterpoise)结构
- **仿真工具**: Alternative Transients Program (ATP)用于实现和测试所提模型；电磁场模型用于生成基准数据
- **验证结果**: 所提出的基于Marti模型的传输线接地模型与HEM模型在GPR峰值上误差小于5%（大多数情况<2%），在波形细节上高度吻合，能够准确模拟地电位升和绝缘子过电压，适用于雷击反击跳闸率计算。模型克服了传统集中电阻模型的局限性，同时比直接嵌入电磁场模型更节省计算资源。
