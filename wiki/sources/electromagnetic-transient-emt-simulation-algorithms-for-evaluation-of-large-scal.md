---
title: "Electromagnetic Transient (EMT) Simulation Algorithms for Evaluation of Large-Scale Extreme Fast Charging Systems (T&amp; D Models)"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Systems;2023;38;5;10.1109/TPWRS.2022.3212639"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/15/Electromagnetic transient (EMT) simulation algorithms for evaluation of large-scale extreme fast cha_Debnath和Choi_2023.pdf"]
---

# Electromagnetic Transient (EMT) Simulation Algorithms for Evaluation of Large-Scale Extreme Fast Charging Systems (T&amp; D Models)

**作者**: 
**年份**: 2023
**来源**: `15/Electromagnetic transient (EMT) simulation algorithms for evaluation of large-scale extreme fast cha_Debnath和Choi_2023.pdf`

## 摘要

—Simulation of high-ﬁdelity models of extreme fast charging (XFC) systems and large-area power grids with many XFCs can be time consuming in traditional simulators. Traditional simulators use a single method of discretization for all the com- ponents that results in imposing a large computational burden of inverting a large matrix as well as increased computations related to single method of discretization (that is typically a trapezoidal method). To overcome the problem of simulating large-area power grids with many XFCs, in this paper, advanced numerical simula- tion algorithms are applied for the ﬁrst time together to reduce the dimension of matrix inversion. The algorithms include numerical stiffness-based segregation, time constant-based segregation, clus- tering and aggregation on di

## 核心贡献


- 首次联合应用刚度分离时间常数分离DAE聚类与多阶积分算法降低矩阵求逆维度
- 提出基于状态空间法的混合离散策略替代单一梯形法有效减轻大规模系统计算负担
- 构建含数百个超快充站的高保真输配电EMT模型实现电力电子与电网协同高效仿真


## 使用的方法


- [[混合离散化|混合离散化]]
- [[多阶积分法|多阶积分法]]
- [[状态空间法|状态空间法]]
- [[微分代数方程聚类聚合|微分代数方程聚类聚合]]
- [[数值刚度分离|数值刚度分离]]
- [[时间常数分离|时间常数分离]]


## 涉及的模型


- [[超快充系统-xfc|超快充系统(XFC)]]
- [[两电平三相逆变器|两电平三相逆变器]]
- [[dc-dc升压变换器|DC-DC升压变换器]]
- [[配电网|配电网]]
- [[输电网|输电网]]
- [[ieee标准测试系统|IEEE标准测试系统]]
- [[同步发电机|同步发电机]]
- [[变压器|变压器]]
- [[输电线路|输电线路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[超快充系统建模|超快充系统建模]]
- [[输配电网协同仿真|输配电网协同仿真]]
- [[仿真加速算法|仿真加速算法]]
- [[高渗透率电力电子电网|高渗透率电力电子电网]]
- [[大规模系统仿真|大规模系统仿真]]


## 主要发现


- 在含十五个超快充站的配电网仿真中算法较传统软件实现最高十八倍加速比
- 在含三百个超快充站的输配电系统仿真中算法实现最高二百七十一倍加速比
- 混合离散与多阶积分策略有效解决单一梯形法导致的大矩阵求逆计算瓶颈



## 方法细节

### 方法概述

本文提出一种面向含大规模超快充（XFC）系统的输配电网高保真电磁暂态（EMT）仿真的混合数值算法框架。传统EMT仿真器对整个系统采用单一离散化方法（通常为梯形法），导致全局大矩阵求逆计算负担极重。本文首次联合应用基于数值刚度的分离、基于时间常数的分离、微分代数方程（DAE）聚类与聚合以及多阶积分算法。该方法基于状态空间法，将系统DAE按动态特性分类：对电力电子开关引起的刚性状态（电感电流、滤波电压/电流）采用具有刚性衰减特性的后向欧拉法离散；对非刚性状态（电容电压）采用前向欧拉法离散。针对同一充电站内多个XFC系统的相似动态，通过聚类聚合技术将DAE降维，先求解聚合后的等效系统，再将结果反馈至各独立XFC模型，从而将大规模矩阵求逆分解为多个小规模矩阵求逆。在配电网与输电网接口处，采用二阶梯形法离散线路模型以支持较大步长，并通过电流源等效与单步延迟数据交换实现输配电网解耦仿真，在保持高保真度的同时显著降低计算复杂度。

### 数学公式


**公式1**: $$$C_{ess}^k \frac{dv_{c,ess}^k}{dt} = -\left(\frac{1}{R_{ess}} + \frac{1}{R_{ess,dc}}\right)v_{c,ess}^k - i_{L,ess}^k + \frac{V_{ess}^k}{R_{ess}}$$$

*XFC系统中储能侧电容电压动态方程，描述DC-DC变换器输入侧电容的充放电过程，属于非刚性状态。*


**公式2**: $$$L_{1,ac} \frac{di_{j,ac}^k}{dt} = -R_{1,ac} i_{j,ac}^k + \frac{v_{dc}^k}{2} \left[ S_{1,j,ac}^k (1-S_{2,j,ac}^k) - S_{2,j,ac}^k (1-S_{1,j,ac}^k) - (1-S_{2,j,ac}^k)(1-S_{1,j,ac}^k)(2\text{sgn}(i_{j,ac}^k)-1) \right] - v_{j,ac,fil}^k$$$

*XFC逆变器交流侧电感电流动态方程，包含开关函数与sgn非线性项，属于刚性状态，需采用小步长与刚性衰减算法离散。*


**公式3**: $$$L_{1,ac} \frac{d \sum_k i_{j,ac}^k}{dt} = -R_{1,ac} \sum_k i_{j,ac}^k + \frac{\sum_k v_{dc}^k}{2} \left[ \cdots \right] - \sum_k v_{j,ac,fil}^k$$$

*多XFC系统聚合后的等效DAE方程，通过对同一充电站内多个XFC的相似滤波器动态进行求和聚合，实现矩阵降维。*


**公式4**: $$$v_{j,ac}^k[k-1] = \frac{v_{dc}^k[k-1]}{2} \left[ S_{1,j,ac}^k[k-2](1-S_{2,j,ac}^k[k-2]) - S_{2,j,ac}^k[k-2](1-S_{1,j,ac}^k[k-2]) - (1-S_{2,j,ac}^k[k-2])(1-S_{1,j,ac}^k[k-2])(2\text{sgn}(i_{j,ac}^k[k-1])-1) \right]$$$

*聚合系统求解所需的逆变器端口电压输入方程，引入1个时间步长的延迟以解耦聚合系统与独立XFC系统的迭代计算。*


### 算法步骤

1. 步骤1：系统高保真建模与DAE构建。为单个XFC系统（含DC-DC升压变换器、两电平三相逆变器及LCL滤波器）、充电站变压器、配电网π型/贝杰龙线路及输电网建立完整的状态空间微分代数方程（DAE）模型，准确刻画电力电子开关行为与高频暂态特性。

2. 步骤2：数值刚度与时间常数分离。分析XFC系统DAE的雅可比矩阵特征值，识别刚性状态（电感电流、滤波器电压/电流）与非刚性状态（电容电压）。刚性部分采用后向欧拉法离散以保证数值稳定性，非刚性部分采用前向欧拉法离散；针对sgn函数非线性引入迟滞松弛技术，防止分离算法在切换瞬间失稳。

3. 步骤3：DAE聚类聚合与降维求解。对同一充电站内多个XFC系统的相似动态进行聚类，构建聚合DAE方程组。在每个仿真步长内，优先求解聚合系统以获得变压器一次侧公共电压，随后将该电压作为边界条件反馈至各独立XFC的离散化DAE中求解，将全局N×N大矩阵求逆转化为多个小矩阵求逆。

4. 步骤4：多阶离散与输配网解耦接口设计。配电网线路采用二阶梯形法离散以允许较大仿真步长；输电网与配电网通过等效电流源接口连接，采用单步延迟近似进行电压/电流数据交换。利用变压器漏感与线路电感提供的平滑时间常数抑制跨域数据交换产生的数值噪声，实现输配电网的高效协同仿真。

5. 步骤5：算法集成与模块化迭代。将上述混合离散策略以Fortran编写并嵌入PSCAD环境，采用1μs统一仿真步长进行模块化迭代计算，支持从单充电站到含数百个XFC的输配电网的大规模扩展仿真。


### 关键参数

- **仿真步长**: 1 μs

- **XFC额定功率范围**: 400 kW ~ 1 MW

- **刚性离散方法**: 后向欧拉法 (Backward Euler)

- **非刚性离散方法**: 前向欧拉法 (Forward Euler)

- **配网线路离散方法**: 梯形法 (Trapezoidal) / 贝杰龙模型

- **非线性处理技术**: 迟滞松弛技术 (Hysteresis relaxation)

- **输配网接口延迟**: 1个时间步长 (1-step delay)

- **测试系统规模**: 单配电网15个XFC / 输配电网300个XFC



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 场景1：单配电网含15个XFC（5个充电站） | 在稳态运行、XFC功率阶跃变化及配电网电压突变三种工况下，对比所提算法与PSCAD基线模型的直流母线电压、电感电流及滤波电容电压波形。 | 仿真速度提升最高达18倍，所有状态变量误差均小于5%，波形高度吻合。 |

| 场景2：输配电网含300个XFC（IEEE 9节点改进系统，20条馈线） | 在稳态运行、90个XFC同时功率阶跃及输电线路故障工况下，验证大规模系统下的算法扩展性与跨域接口稳定性。 | 仿真速度提升最高达271倍，状态变量误差控制在5%以内，成功捕捉高频开关暂态与电网低频机电动态的耦合过程。 |



## 量化发现

- 在单配电网15个XFC场景下，所提混合算法相比传统PSCAD单一梯形法仿真速度提升最高达18倍。
- 在输配电网300个XFC大规模场景下，计算加速比最高达到271倍，显著突破传统EMT仿真器的算力瓶颈。
- 所有测试工况（稳态、功率阶跃、电网故障）下，关键状态变量（直流母线电压、电感电流、滤波电容电压）与高保真基线模型的相对误差均严格小于5%。
- 采用1μs固定步长时，DAE聚类聚合技术成功将全局矩阵求逆维度降低至原规模的1/N（N为充电站内XFC数量），计算复杂度呈线性下降。
- 输配网接口单步延迟近似在变压器漏感与线路电感提供的平滑时间常数作用下，未引入显著数值振荡，跨域数据交换误差可忽略不计。


## 关键公式

### XFC逆变器交流侧刚性DAE方程

$$$L_{1,ac} \frac{di_{j,ac}^k}{dt} = -R_{1,ac} i_{j,ac}^k + \frac{v_{dc}^k}{2} \left[ S_{1,j,ac}^k (1-S_{2,j,ac}^k) - S_{2,j,ac}^k (1-S_{1,j,ac}^k) - (1-S_{2,j,ac}^k)(1-S_{1,j,ac}^k)(2\text{sgn}(i_{j,ac}^k)-1) \right] - v_{j,ac,fil}^k$$$

*用于描述电力电子开关引起的高频暂态电流动态，需采用后向欧拉法与小步长离散以保证数值稳定性。*

### 多XFC系统聚合降维DAE方程

$$$L_{1,ac} \frac{d \sum_k i_{j,ac}^k}{dt} = -R_{1,ac} \sum_k i_{j,ac}^k + \frac{\sum_k v_{dc}^k}{2} \left[ \cdots \right] - \sum_k v_{j,ac,fil}^k$$$

*应用于同一充电站内多个XFC系统的动态聚合，通过求和等效将独立求解转化为先聚合后反馈的两级求解结构，大幅降低矩阵求逆维度。*

### 带单步延迟的聚合系统输入电压方程

$$$v_{j,ac}^k[k-1] = \frac{v_{dc}^k[k-1]}{2} \left[ S_{1,j,ac}^k[k-2](1-S_{2,j,ac}^k[k-2]) - S_{2,j,ac}^k[k-2](1-S_{1,j,ac}^k[k-2]) - (1-S_{2,j,ac}^k[k-2])(1-S_{1,j,ac}^k[k-2])(2\text{sgn}(i_{j,ac}^k[k-1])-1) \right]$$$

*用于解耦聚合系统与独立XFC系统的迭代计算，利用前一步长数据作为当前步长输入，结合系统固有电感平滑特性保证数值收敛。*



## 验证详情

- **验证方式**: 对比仿真分析（与PSCAD高保真基线模型进行波形与误差对比）
- **测试系统**: 改进型IEEE 9节点输配电网系统（含20条配电网馈线，共300个XFC）及单配电网系统（含5个充电站，共15个XFC）
- **仿真工具**: PSCAD/EMTDC（基线对比与平台集成），自定义Fortran算法模块（实现混合离散与聚合求解）
- **验证结果**: 在1μs统一仿真步长下，所提算法在稳态运行、功率阶跃及电网故障等多种工况下均与PSCAD高保真基线模型高度吻合，状态变量误差严格控制在5%以内。同时实现最高271倍的计算加速，验证了算法在大规模电力电子化输配电网EMT仿真中的高效性、数值稳定性与工程可扩展性。
