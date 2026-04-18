---
title: "Simulation of electromagnetic transients with Modelica, accuracy and performance assessment for transmission line models"
type: source
authors: ['Alireza Masoom']
year: 2020
journal: "Electric Power Systems Research, 189 (2020) 106799. doi:10.1016/j.epsr.2020.106799"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/35/j.epsr.2020.106799.pdf.pdf"]
---

# Simulation of electromagnetic transients with Modelica, accuracy and performance assessment for transmission line models

**作者**: Alireza Masoom
**年份**: 2020
**来源**: `35/j.epsr.2020.106799.pdf.pdf`

## 摘要

Simulation of electromagnetic transients with Modelica, accuracy and performance assessment for transmission line models Alireza Masooma, Tarek Ould-Bachirb, Jean Mahseredjian⁎,a, Adrien Guironnetc, Ni Dingc a Department of Electrical Engineering, Polytechnique Montréal, Canada b Department of Computer Engineering and Software Engineering, Polytechnique Montréal, Canada

## 核心贡献



- 验证了Modelica声明式/方程建模语言在电磁暂态(EMT)仿真中的适用性与开发优势
- 基于Modelica开发并对比了输电线路恒定参数(CP)与宽频(WB)模型的精度与计算性能

## 使用的方法


- [[numerical-integration]]
- [[nodal-analysis]]
- [[state-space]]

## 涉及的模型


- [[transmission-line]]
- [[fixed-admittance]]
- [[frequency-dependent]]

## 相关主题


- [[harmonic]]
- [[frequency-dependent]]
- [[numerical-integration]]

## 主要发现



- Modelica等声明式语言能显著提升EMT模型的可读性、可维护性与跨平台开发效率
- 基于Modelica实现的CP与WB输电线路模型在仿真精度上与传统命令式编程工具相当，且具备优异的计算性能

## 方法细节

### 方法概述

本文采用基于Modelica的声明式（Declarative）建模方法开发电磁暂态（EMT）仿真工具，实现了两种输电线路模型：恒定参数（Constant Parameter, CP）模型和宽频（Wide-Band, WB）模型。CP模型基于贝杰龙（Bergeron）行波理论，采用实常数模态分析矩阵将多相线路解耦为独立模态，在模态域计算无损线路的历史电流后转换回相域，并通过在每端接入R/4集中电阻来近似线路损耗。WB模型基于矢量拟合（Vector Fitting）技术，在相域直接拟合频率相关的特征导纳矩阵Yc和传播函数矩阵H，采用状态空间形式实现递归卷积算法，明确考虑各模态的传播时延τk。Modelica的acausal（非因果）特性允许直接以数学方程形式描述物理系统，利用Pin连接器（包含电压和电流变量）自动实现基尔霍夫定律的连接，无需预先确定方程求解顺序，实现模型与数值求解器的解耦。

### 数学公式


**公式1**: $$$I_k = Y_c V_k - 2I_k^i$$$

*线路末端k的相电流与特性导纳、入射电流波的关系，Yc为特性导纳矩阵*


**公式2**: $$$I_k^i = H I_m^r$$$

*从末端m反射并传播到末端k的入射电流波，H为传播矩阵*


**公式3**: $$$Y_c = \sqrt{YZ^{-1}}$$$

*特性导纳矩阵定义，Y和Z分别为单位长度并联导纳和串联阻抗矩阵*


**公式4**: $$$H = e^{-\sqrt{YZ}\ell}$$$

*传播矩阵，描述信号沿线长ℓ的传播特性*


**公式5**: $$$i_k = y_c v_k - i_k^{hist}$$$

*无损CP线路时域诺顿等效方程（k端），yc为特性导纳，ihist为历史电流*


**公式6**: $$$i_k^{hist} = y_c v_m(t-\tau) + i_m(t-\tau)$$$

*k端历史电流，由对端m的延迟信号决定，τ为传播时延*


**公式7**: $$$Y_c = G_0 + \sum_{i=1}^{N_y} \frac{G_i}{s-q_i}$$$

*特征导纳的矢量拟合有理函数近似，G0为无穷频率常数留数，Gi为留数矩阵，qi为极点，Ny为拟合阶数*


**公式8**: $$$H = \sum_{k=1}^{N_g} \sum_{i=1}^{N_h(k)} \frac{R_{k,i}}{s-p_{k,i}} e^{-s\tau_k}$$$

*传播函数的矢量拟合，Ng为模态数，Nh(k)为第k模态极点数，τk为模态时延，Rk,i为留数，pk,i为极点*


**公式9**: $$$\frac{d w_i}{dt} = q_i w_i + G_i v_k$$$

*WB模型并联支路状态空间方程（第i个极点），wi为状态变量，用于计算特性导纳电流*


**公式10**: $$$i_{sh,k} = G_0 v_k + \sum_{i=1}^{N_y} w_i$$$

*WB模型k端总并联（特性导纳）电流，为直流项与所有状态变量贡献之和*


**公式11**: $$$\frac{d x_{k,i}}{dt} = p_{k,i} x_{k,i} + R_{k,i} i_{mu}(t-\tau_k)$$$

*WB模型历史电流状态空间方程，x_{k,i}为历史项状态变量，imu为正向行波电流，考虑时延τk*


**公式12**: $$$i_k^{hist} = \sum_{k=1}^{N_g} \sum_{i=1}^{N_h(k)} x_{k,i}$$$

*WB模型k端总历史电流，为所有模态所有极点状态变量之和*


### 算法步骤

1. CP模型算法步骤：1) 使用实常数模态转换矩阵Ti（在目标频率处计算）将n相耦合线路参数转换到模态域，实现解耦为n个独立模态线路；2) 对每个模态计算无损线路的传播时延τ和特性导纳yc；3) 在模态域计算历史电流ihist，采用 quarter-lumped 方法将线路总电阻R分为四份，在每端接入R/4集中电阻来近似考虑线路损耗，中间段为无损线路；4) 通过逆变换Ti将模态域历史电流转换回相域；5) 构建诺顿等效电路，计算端点注入电流ik = yc·vk - ihist,k。

2. WB模型算法步骤：1) 使用外部矢量拟合工具（如EMTP预处理）在相域直接拟合特征导纳矩阵Yc和传播矩阵H的频率响应，导出极点qi和pk,i、留数矩阵Gi和Rk,i、以及模态时延τk等参数，自动导入Modelica可读文件；2) 构建状态空间方程描述特性导纳并联支路（方程10-13），通过Ny个一阶微分方程计算并联电流ish；3) 构建状态空间方程描述历史电流（方程14-15），通过Ng×Nh(k)个带时延的微分方程计算历史项ihist，每个模态k具有独立的时延τk；4) 在Modelica中使用时滞算子(t-τk)实现传播时延，计算正向行波电流imu；5) 组装诺顿等效，总注入电流为并联导纳电流减去历史电流。

3. Modelica实现架构：1) 定义Pin连接器类（包含非流变量voltage和流变量current），确保基尔霍夫电压定律（等式耦合）和电流定律（求和为零）的自动满足；2) 定义Plug多相终端（Pin的集合）；3) 创建可复用的诺顿等效组件类（NortonEquivalent）作为一端口电气元件，严格按方程描述；4) 创建History类分别实现CP模型（模态域计算）和WB模型（状态空间时延计算）的历史电流计算；5) 通过图形化连接（黑色表示相域计算，红色表示模态域计算）组装完整线路模型，体现acausal编程特性（无预设输入输出）。


### 关键参数

- **Ny**: 特征导纳Yc拟合阶数（极点数量），决定频率依赖建模精度

- **Ng**: 模态数量，对于n相线路通常为n（三相线路为3）

- **Nh(k)**: 第k个模态传播函数H的拟合极点数，不同模态可有不同阶数

- **τk**: 第k个模态的传播时延（秒），由线路物理特性和模态速度决定

- **G0**: 特征导纳在无穷频率的实常数留数矩阵（n×n）

- **Gi**: 特征导纳第i个极点的留数矩阵（n×n）

- **qi**: 特征导纳第i个拟合极点（实数或共轭复数对）

- **Rk,i**: 第k模态第i个极点的传播函数留数矩阵

- **pk,i**: 第k模态第i个拟合极点

- **Ti**: CP模型的实常数模态转换矩阵（n×n），用于相域与模态域转换

- **R/4**: CP模型每端集中电阻值，线路总电阻R的四分之一，用于近似损耗



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 恒定参数(CP)输电线路模型精度与性能测试 | 验证基于Modelica声明式语言实现的CP线路模型与EMTP基准仿真的一致性。测试包括无损线路的波传播特性、模态转换矩阵的准确性、历史电流计算的正确性，以及quarter-lumped电阻近似对损耗模拟的影响。文本未提供具体的数值误差百分比或计算时间对比数据。 | 与EMTP传统命令式编程（FORTRAN/C）实现对比，验证声明式建模在保持等效精度的同时提升代码可读性（具体误差数值如<0.1%或计算加速比未在提供的文本片段中披露） |

| 宽频(WB)输电线路模型精度与性能测试 | 验证基于矢量拟合和状态空间实现的WB模型在宽频范围（覆盖基波至高频谐波）内的精度。测试评估相域矢量拟合参数导入后的数值稳定性、递归卷积算法的准确性，以及多模态时延处理对不同频率分量的保真度。涉及特征导纳和传播函数的频率依赖特性验证。 | 与EMTP的WB模型对比，评估频率依赖线路模型的仿真一致性（具体偏差百分比和CPU时间对比数据未在提供的文本片段中给出） |



## 量化发现

- CP模型损耗近似：采用quarter-lumped方法，在线路两端各接入R/4集中电阻（总电阻R的25%每端），中间50%为无损线路段
- 模态解耦维度：n相线路通过实常数模态矩阵Ti精确解耦为n个独立的单相模态线路
- WB模型特征导纳状态空间维度：需要Ny个状态变量（微分方程）来描述并联支路动态
- WB模型历史电流状态空间维度：需要∑(k=1 to Ng) Nh(k)个状态变量来描述所有模态的历史电流，每个模态k贡献Nh(k)个极点
- WB模型总计算复杂度：涉及Ny个并联支路状态方程和Ng×Nh(k)个历史电流状态方程的联立求解
- 时延处理：WB模型明确考虑各模态传播时延τk，通过延迟微分方程实现，时延值取决于模态传播速度和线路长度ℓ
- Modelica建模优势：实现了方程（What）与求解算法（How）的解耦，模型代码完全对应教科书方程形式


## 关键公式

### 特征导纳矢量拟合方程

$$$Y_c = G_0 + \sum_{i=1}^{N_y} \frac{G_i}{s-q_i}$$$

*WB模型核心方程，用于在相域近似频率相关的特性导纳矩阵，通过部分分式展开将有理函数拟合转化为状态空间实现*

### 传播函数矢量拟合方程

$$$H = \sum_{k=1}^{N_g} \sum_{i=1}^{N_h(k)} \frac{R_{k,i}}{s-p_{k,i}} e^{-s\tau_k}$$$

*WB模型核心方程，描述信号沿线传播的频率依赖和时延特性，是递归卷积算法的基础*

### 诺顿等效时域方程

$$$i_k = y_c v_k - i_k^{hist}$$$

*CP和WB模型通用的线路端点接口方程，将分布参数线路等效为瞬时导纳并联历史电流源，是EMT仿真中线性化网络导纳矩阵构建的基础*



## 验证详情

- **验证方式**: 对比验证（Comparative Validation）：将Modelica实现的CP和WB线路模型与成熟商业软件EMTP的仿真结果进行逐点对比（Accuracy Assessment），并对比计算性能（Performance Assessment），验证声明式语言在EMT领域的适用性
- **测试系统**: 文本提及包含两个案例研究（Two case studies），用于全面验证模型并对比准确性与性能，但具体测试系统的拓扑结构、线路长度、电压等级、相数等详细配置未在提供的文本片段中明确说明
- **仿真工具**: 基准工具：EMTP（经典EMT仿真软件，使用命令式语言FORTRAN/C实现，采用梯形积分法和特定稀疏矩阵求解算法）；开发平台：Modelica语言（支持环境包括商业软件如Dymola、Wolfram System Modeler或开源软件如OpenModelica、Dynaωo，文本未明确指定具体使用哪个环境进行最终测试）
- **验证结果**: 验证了Modelica声明式语言在EMT仿真中的技术可行性：1) CP和WB模型在仿真精度上与EMTP基准结果相当，满足工程精度要求；2) 基于方程的建模显著提升了代码可读性、可维护性和跨平台开发效率；3) 实现了模型与数值求解器的解耦，保证仿真的可重复性和多环境兼容性。具体定量指标（如最大相对误差<0.5%、均方根误差、CPU时间加速比或开销百分比）未在提供的文本片段中披露。
