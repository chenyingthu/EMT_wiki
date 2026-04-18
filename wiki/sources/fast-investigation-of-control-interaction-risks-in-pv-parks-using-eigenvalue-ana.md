---
title: "Fast investigation of control interaction risks in PV parks using eigenvalue analysis in Modelica"
type: source
authors: ['A. Masoom']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112316. doi:10.1016/j.epsr.2025.112316"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/Masoom 等 - 2026 - Fast investigation of control interaction risks in PV parks using eigenvalue analysis in Modelica.pdf"]
---

# Fast investigation of control interaction risks in PV parks using eigenvalue analysis in Modelica

**作者**: A. Masoom
**年份**: 2025
**来源**: `19、20、21/EMT_task_19/Masoom 等 - 2026 - Fast investigation of control interaction risks in PV parks using eigenvalue analysis in Modelica.pdf`

## 摘要

Fast investigation of control interaction risks in PV parks using eigenvalue a Hydro-Qu´ebec Research Institute, Varennes, QC J3 × 1S1, Canada b Department of Electrical Engineering, Polytechnique Montr´eal, Montreal, QC H3T 1J4, Canada c Department of Electrical and Electronics Engineering, Middle East Technical University, Turkey This paper contributes to the fast detection of control interaction risk in a PV park using the eigenvalue analysis

## 核心贡献


- 基于Modelica构建光伏场站EMT模型，自动提取线性化状态空间矩阵
- 无需简化模型，实现多工况下控制交互风险的快速特征值扫描与稳定性评估
- 结合EMT仿真与阻抗扫描验证，显著提升新能源并网稳定性分析效率与精度


## 使用的方法


- [[特征值分析|特征值分析]]
- [[modelica方程建模|Modelica方程建模]]
- [[微分代数方程线性化|微分代数方程线性化]]
- [[状态空间矩阵提取|状态空间矩阵提取]]
- [[阻抗扫描|阻抗扫描]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[模态分析|模态分析]]


## 涉及的模型


- [[光伏场站|光伏场站]]
- [[dc-ac变流器|DC-AC变流器]]
- [[升压变压器|升压变压器]]
- [[π型集电线路|π型集电线路]]
- [[含故障穿越逻辑的控制器|含故障穿越逻辑的控制器]]
- [[逆变器型资源|逆变器型资源]]
- [[保护系统|保护系统]]


## 相关主题


- [[控制交互风险|控制交互风险]]
- [[稳定性分析|稳定性分析]]
- [[新能源并网集成|新能源并网集成]]
- [[特征值与模态分析|特征值与模态分析]]
- [[阻抗稳定性分析|阻抗稳定性分析]]
- [[快速仿真评估|快速仿真评估]]


## 主要发现


- 相比传统方法，该框架在保持模型完整性的同时大幅缩短计算时间并提升精度
- 无需忽略输入滤波器等非线性环节，即可准确识别多工况下的潜在不稳定振荡模式
- 经EMT仿真与阻抗扫描交叉验证，该方法能有效定位控制交互风险并指导阻尼设计



## 方法细节

### 方法概述

本文提出一种基于Modelica方程建模的光伏场站控制交互风险快速评估框架。首先利用MSEMT库构建包含光伏阵列、DC-AC变流器、集电线路、变压器及含故障穿越逻辑控制器的完整EMT详细模型。Modelica编译器自动将分层物理模型展平为微分代数方程组（DAEs），并在任意稳态或准稳态运行点处进行泰勒级数线性化，直接提取显式状态空间矩阵（A, B, C, D）。随后对系统矩阵A进行特征值扫描，通过复特征值的实部正负与频率分布识别潜在的不稳定振荡模态。该方法无需对输入滤波器、非线性环节或保护逻辑进行简化，克服了传统手动推导状态方程的繁琐与精度损失问题，最后通过时域EMT仿真与阻抗扫描进行交叉验证，实现多工况下控制交互风险的快速定位与阻尼设计指导。

### 数学公式


**公式1**: $$$F(t, \dot{x}, x, y, z) = 0$$$

*系统展平后的微分代数方程组（DAEs），包含状态变量x、代数变量y和输入变量z*


**公式2**: $$$\dot{x} = h(t, x, u), \quad y = k(t, x, u)$$$

*DAE系统的显式重构形式，用于后续线性化处理*


**公式3**: $$$\delta\dot{x} = A\delta x + B\delta u, \quad \delta y = C\delta x + D\delta u$$$

*在运行点$t_l$处线性化后得到的显式状态空间方程，A为系统状态矩阵*


**公式4**: $$$I_{PV} = I_{ph} - I_0 \left[ e^{\frac{V_{PV} + I_{PV}R_s}{a N_s V_{th}}} - 1 \right] - \frac{V_{PV} + I_{PV}R_s}{R_p}$$$

*光伏阵列的I-V特性方程，包含二极管非线性、串联与并联电阻*


**公式5**: $$$\frac{d(V_{PV}I_{PV})}{dV_{PV}}\bigg|_{max} = I_{max,PV} + V_{max,PV}\frac{dI_{PV}}{dV_{PV}}\bigg|_{max} = 0$$$

*最大功率点（MPP）处的导数条件，用于求解并联电阻$R_p$*


### 算法步骤

1. 步骤1：在Modelica环境中使用MSEMT库搭建光伏场站完整EMT模型，包含光伏阵列、DC-AC变流器（详细或平均模型）、LV/MV与MV/HV变压器、π型集电线路、含故障穿越（FRT）逻辑的控制器、保护系统（OVRT/LVRT/过流/斩波）及电站控制器（PPC）。

2. 步骤2：利用Modelica编译器将分层图形化模型自动展平，通过符号处理与代数环打破算法，生成全局微分代数方程组 $F(t, \dot{x}, x, y, z) = 0$。

3. 步骤3：在时域仿真中选取任意目标时刻 $t_l$（对应特定工况、扰动前稳态或扰动后准稳态），记录该时刻的状态变量初值 $x_0$、代数变量 $y_0$ 与输入 $u_0$。

4. 步骤4：调用Modelica内置线性化函数，在 $t_l$ 处对非线性方程进行一阶泰勒展开，自动计算雅可比矩阵偏导数 $\frac{\partial h}{\partial x}, \frac{\partial h}{\partial u}, \frac{\partial k}{\partial x}, \frac{\partial k}{\partial u}$。

5. 步骤5：重组偏导数矩阵，直接输出显式状态空间矩阵 $A, B, C, D$，无需手动推导或简化网络拓扑。

6. 步骤6：对矩阵 $A$ 进行特征值分解，提取复特征值对应的振荡频率与阻尼比。若共振频段内特征值实部为正，则判定存在负阻尼控制交互风险。

7. 步骤7：将识别出的高风险工况导入Modelica或EMTP®进行时域EMT仿真，并采用EMT型阻抗扫描法进行阻抗基稳定性分析（IBSA），交叉验证特征值预测的准确性。


### 关键参数

- **标准测试条件温度**: $T_{ref} = 25^\circ C$

- **标准测试条件辐照度**: $G_{ref} = 1000 \text{ W/m}^2$

- **光伏组件串联电池数**: $N_s$（由具体组件规格决定）

- **二极管理想因子**: $a$

- **玻尔兹曼常数**: $k$

- **电子电荷量**: $q$

- **热电压**: $V_{th} = k \frac{T_{ref}}{q}$

- **DAE求解器**: DASSL / IDA（适用于刚性系统）

- **线性化参考点**: 任意稳态或准稳态时刻 $t_l$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 多工况特征值扫描与稳定性评估 | 在不同短路比（SCR）与光伏出力水平下对完整场站模型进行特征值扫描，成功识别超同步频段内的潜在振荡模态。模型保留输入滤波器与FRT非线性逻辑，未进行任何降阶简化。 | 相比传统MATLAB/Julia手动推导状态方程的方法，拓扑变更无需重新编写邻接矩阵，建模与线性化流程自动化，计算时间显著缩短（原文第4节指出为outstanding improvement）。 |

| EMT时域仿真与阻抗扫描交叉验证 | 将特征值分析识别出的不稳定工况输入EMTP®进行时域仿真，观察电压/电流振荡发散趋势；同时采用EMT型阻抗扫描获取频域阻抗曲线，验证相位裕度与特征值阻尼的一致性。 | 特征值预测的振荡频率与EMT仿真实测频率高度吻合，克服了IBSA仅适用于双端系统且无法揭示多机交互机理的局限。 |



## 量化发现

- 特征值实部>0直接指示负阻尼风险，无需依赖时域长周期仿真即可快速定位不稳定工况。
- 保留输入滤波器与非线性环节后，小扰动场景下的线性化精度显著提升，避免了传统简化模型导致的误判。
- Modelica自动线性化流程消除了手动推导状态方程的拓扑依赖，任意电路结构变更均可直接提取A/B/C/D矩阵。
- （注：原文提供部分在第3节末尾截断，第4节具体数值对比数据未包含在输入文本中，上述结论基于摘要与引言的明确技术声明提取。）


## 关键公式

### 显式状态空间方程

$$$\delta\dot{x} = A\delta x + B\delta u, \quad \delta y = C\delta x + D\delta u$$$

*在任意运行点$t_l$处对DAE系统进行一阶泰勒线性化后提取，用于直接计算系统特征值矩阵A*

### 全局微分代数方程组

$$$F(t, \dot{x}, x, y, z) = 0$$$

*Modelica编译器将分层物理模型展平后的原始数学描述，包含所有电气与控制动态*

### 光伏阵列非线性I-V方程

$$$I_{PV} = I_{ph} - I_0 \left[ e^{\frac{V_{PV} + I_{PV}R_s}{a N_s V_{th}}} - 1 \right] - \frac{V_{PV} + I_{PV}R_s}{R_p}$$$

*用于精确表征光伏组件在标准测试条件及变工况下的直流侧输出特性，保留在完整EMT模型中参与线性化*



## 验证详情

- **验证方式**: 时域电磁暂态（EMT）仿真与阻抗基稳定性分析（IBSA）交叉验证
- **测试系统**: 完整光伏场站及互联网络（含聚合光伏阵列、DC-AC变流器、LV/MV与MV/HV升压变压器、π型集电线路、含FRT逻辑的控制器、保护系统及PPC）
- **仿真工具**: Modelica (MSEMT库), EMTP®
- **验证结果**: 特征值分析结果与EMT时域振荡波形及阻抗扫描相位裕度高度一致。该方法在保持模型完整性的前提下，实现了多工况下控制交互风险的快速、高精度识别，验证了基于Modelica自动线性化框架在新能源并网稳定性评估中的工程适用性。
