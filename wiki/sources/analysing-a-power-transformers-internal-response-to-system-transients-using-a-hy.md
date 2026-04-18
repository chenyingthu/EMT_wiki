---
title: "Analysing a power transformer⠒s internal response to system transients using a hybrid modelling methodology"
type: source
authors: ['Steven', 'D.', 'Mitchell']
year: 2015
journal: "INTERNATIONAL JOURNAL OF ELECTRICAL POWER AND ENERGY SYSTEMS, 69 (2015) 67-75. doi:10.1016/j.ijepes.2014.12.064"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/Analysing a power transformer's internal response to system transients using a hybrid modelling methodology.pdf"]
---

# Analysing a power transformer⠒s internal response to system transients using a hybrid modelling methodology

**作者**: Steven, D., Mitchell
**年份**: 2015
**来源**: `07&08/Analysing a power transformer's internal response to system transients using a hybrid modelling methodology.pdf`

## 摘要

Analysing a power transformer’s internal response to system transients a School of Electrical Engineering and Computer Science, University of Newcastle, Callaghan, NSW 2308, Australia b Electrical Engineering Department, Federal University of Parana, Curitiba, PR 81531-990, Brazil This article presents a novel approach to analysing a power transformer’s internal response to system transients. In this approach a hybrid modelling methodology is adopted which leverages the distinct

## 核心贡献


- 提出黑箱与灰箱结合的混合建模方法，实现系统暂态仿真与内部响应分析衔接。
- 仅依赖外部测试与铭牌数据推导参数，无需制造商图纸即可构建高精度模型。
- 利用频域传递函数将终端暂态注入灰箱模型，精准预测绕组内部节点电压分布。


## 使用的方法


- [[黑箱建模|黑箱建模]]
- [[灰箱建模|灰箱建模]]
- [[混合建模|混合建模]]
- [[频响分析-fra|频响分析(FRA)]]
- [[系统辨识|系统辨识]]
- [[状态空间实现|状态空间实现]]
- [[傅里叶变换|傅里叶变换]]
- [[emtp仿真|EMTP仿真]]


## 涉及的模型


- [[电力变压器|电力变压器]]
- [[黑箱导纳矩阵模型|黑箱导纳矩阵模型]]
- [[灰箱物理结构模型|灰箱物理结构模型]]
- [[气体绝缘变电站-gis|气体绝缘变电站(GIS)]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[谐振过电压|谐振过电压]]
- [[变压器内部响应|变压器内部响应]]
- [[混合建模|混合建模]]
- [[频率相关建模|频率相关建模]]
- [[系统暂态分析|系统暂态分析]]


## 主要发现


- 混合方法在无内部图纸条件下，仍能准确复现终端暂态并映射至内部绕组节点。
- 巴西水电站GIS案例验证表明，该方法可有效识别系统操作引发的内部谐振风险。
- 灰箱参数受设计原则约束可避免非物理收敛，确保内部电压响应预测具备可靠性。



## 方法细节

### 方法概述

本文提出一种黑箱与灰箱结合的混合建模方法，用于分析电力系统暂态下变压器内部绕组的电压响应。首先，基于频域系统辨识构建变压器端口的黑箱导纳矩阵模型，并将其嵌入EMTP系统级仿真中，以获取最恶劣工况下的端口暂态电压波形。随后，利用变压器物理拓扑构建灰箱梯形网络模型，通过约束非线性优化算法将模型传递函数拟合至频响分析（FRA）测试数据，从而在无需制造商内部图纸的情况下反演模型参数。最后，将EMTP得到的端口暂态信号进行傅里叶变换，与灰箱模型各内部节点的传递函数相乘，再经逆傅里叶变换得到绕组内部各标称节点的时域暂态电压分布，实现系统级暂态与设备内部响应的无缝衔接。

### 数学公式


**公式1**: $$$I(j\omega) = Y(j\omega)V(j\omega)$$$

*变压器端口频域导纳矩阵方程，描述多端口电流与电压的频域线性关系*


**公式2**: $$$\dot{x}(t) = A(u(t))x(t) + B(u(t))u(t), \quad v(t) = C(u(t))x(t)$$$

*灰箱模型状态空间方程，其中A、B、C为频率相关的非线性矩阵，反映铁芯磁趋肤效应、绕组集肤与邻近效应及绝缘介质复介电常数*


**公式3**: $$$H(j\omega) = C(\omega)(j\omega I - A(\omega))^{-1}B(\omega)$$$

*灰箱模型传递函数，用于计算特定输入端口至内部节点的频域响应*


**公式4**: $$$\hat{V}_k(j\omega) = U(j\omega) \hat{H}_{H1k}(j\omega)$$$

*混合建模核心注入公式，将端口暂态频谱与节点传递函数相乘得到内部节点输出频谱*


**公式5**: $$$J = \left|\log_{10}\frac{\hat{H}_{H1H0}}{G_{H1H0}}\right|^2 + \left|\log_{10}\frac{\hat{H}_{H1X1}}{G_{H1X1}}\right|^2 + \left|\log_{10}\frac{\hat{H}_{X2X1}}{G_{X2X1}}\right|^2$$$

*灰箱参数辨识目标函数，基于对数误差最小化拟合高压端开路、低压端开路及绕组间电容三项FRA测试数据*


### 算法步骤

1. 步骤1：频响数据采集。对目标变压器执行高压绕组端对端开路、低压绕组端对端开路及绕组间电容三项FRA测试，获取宽频域导纳/传递函数测量数据。

2. 步骤2：黑箱模型构建。采用频域系统辨识技术，利用正交基函数（如Takenaka-Malmquist函数或单极点部分分式）展开导纳矩阵元素，通过Sanathanan-Koener迭代法求解基函数极点，最终利用最小二乘法拟合参数，生成适用于EMTP的状态空间或传递函数模型。

3. 步骤3：系统级暂态仿真。将黑箱模型接入EMTP-RV电网模型，模拟GIS变电站内隔离开关或断路器操作，提取变压器高压侧端口最恶劣暂态电压波形$u(t)$。

4. 步骤4：灰箱拓扑与参数辨识。基于变压器物理结构建立多导体梯形网络模型，定义状态空间方程。采用约束非线性优化算法，以式(15)为目标函数，调整电感、电阻、电容参数，使模型传递函数与FRA实测数据在全频段内最佳匹配，确保参数符合物理设计原则以避免非物理收敛。

5. 步骤5：频域注入与内部响应计算。对端口暂态$u(t)$执行FFT得到$U(j\omega)$。根据灰箱状态空间矩阵计算高压输入端至各内部节点（$k_{H1}$至$k_{H9}$及$k_{X1}$至$k_{X9}$）的传递函数$\hat{H}_{H1k}(j\omega)$。按式(16)相乘得到各节点频谱$\hat{V}_k(j\omega)$。

6. 步骤6：时域重构。对各节点频谱执行逆FFT，输出绕组内部各标称位置的暂态电压时域波形，完成内部谐振过电压风险评估。


### 关键参数

- **变压器额定参数**: 单相 525/18 kV, 256 MVA 发电机变压器

- **终端匹配阻抗**: 400 Ω (模拟传输线波阻抗)

- **灰箱节点划分**: 高压绕组节点 kH1~kH9，低压绕组节点 kX1~kX9

- **FRA测试类型**: 高压端对端开路、低压端对端开路、绕组间电容耦合

- **优化算法**: 约束非线性优化算法 (Constrained Nonlinear Optimization)

- **基函数极点选择**: Sanathanan-Koener迭代法



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 巴西水电站GIS变电站发电机变压器暂态注入分析 | 在EMTP-RV中模拟GIS开关操作，提取高压侧H1端口暂态电压。波形显示在约10-15 μs时刻出现峰值，幅值约600 kV。将该波形注入灰箱模型后，成功计算出高压绕组中点(kH(n/2))及低压绕组各节点的电压分布。模型在宽频范围内准确复现了FRA测试的谐振峰谷特征，内部节点电压响应清晰揭示了特定频率分量引发的局部电压放大现象。 | 相较于传统白箱模型需依赖制造商内部几何图纸，本方法仅凭外部FRA数据与铭牌参数即可实现内部响应预测，建模周期缩短且规避了知识产权限制；相较于纯黑箱模型，本方法提供了绕组内部空间分布的电压应力数据，而非仅停留在端口响应层面。 |



## 量化发现

- 变压器额定容量与电压等级为256 MVA、525/18 kV，终端匹配阻抗设定为400 Ω以模拟实际波阻抗。
- 端口暂态仿真结果显示，H1端子在开关操作下产生峰值约600 kV的暂态过电压（见图6），持续时间约45 μs。
- 灰箱参数辨识采用对数尺度误差目标函数，确保在FRA宽频带内谐振频率与幅值的拟合误差最小化，避免低频或高频段的数值主导问题。
- 混合方法通过频域乘法替代时域卷积，显著降低计算复杂度，单次内部节点响应计算可在毫秒级完成，满足工程快速评估需求。
- 模型参数受变压器设计原则约束，有效防止了优化算法陷入非物理局部最优解，保证了内部电压分布预测的物理一致性。


## 关键公式

### 频域混合注入方程

$$$\hat{V}_k(j\omega) = U(j\omega) \hat{H}_{H1k}(j\omega)$$$

*用于将系统级EMTP仿真得到的端口暂态频谱与灰箱模型内部节点传递函数结合，计算任意内部节点的频域响应*

### 灰箱状态空间模型

$$$\dot{x}(t) = A(u(t))x(t) + B(u(t))u(t), \quad v(t) = C(u(t))x(t)$$$

*描述变压器内部电磁耦合与频率相关损耗（铁芯趋肤、绕组集肤/邻近效应、介质复介电常数）的动态行为*

### 多FRA测试联合优化目标函数

$$$J = \sum_{k=1}^{3} \left|\log_{10}\frac{\hat{H}_k(j\omega)}{G_k(j\omega)}\right|^2$$$

*在灰箱参数辨识阶段使用，通过最小化模型传递函数与三项实测FRA数据的对数误差，确保全频段拟合精度*



## 验证详情

- **验证方式**: 混合仿真验证（EMTP系统级仿真 + FRA数据驱动参数辨识 + 频域注入分析）
- **测试系统**: 巴西某水电站GIS变电站局部网络（含发电机U3、单相525/18 kV/256 MVA主变T1及GIS母线/断路器）
- **仿真工具**: EMTP-RV（系统暂态仿真与黑箱模型集成）、MATLAB/自定义优化脚本（灰箱参数辨识与频域信号处理）
- **验证结果**: 验证表明，该方法在缺乏制造商内部结构图纸的条件下，仅依靠外部FRA测试与铭牌数据即可高精度构建变压器模型。EMTP仿真成功捕获了GIS开关操作引发的端口暂态（峰值~600 kV），灰箱模型准确映射了该激励至绕组内部各节点的电压分布，有效识别了由系统操作频率与变压器固有谐振频率匹配导致的内部过电压风险，证明了混合建模在工程实用性与预测可靠性方面的优势。
