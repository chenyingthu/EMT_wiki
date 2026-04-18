---
title: "基于UMEC的双芯Sen变压器电磁暂态模型"
type: source
authors: ['CNKI']
year: 2022
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/16/卜亮 等 - 2021 - 基于UMEC的双芯Sen变压器电磁暂态模型.pdf"]
---

# 基于UMEC的双芯Sen变压器电磁暂态模型

**作者**: CNKI
**年份**: 2022
**来源**: `16/卜亮 等 - 2021 - 基于UMEC的双芯Sen变压器电磁暂态模型.pdf`

## 摘要

This paper proposes an electromagnetic transient model of the two-core Sen transformer (TCST) based on the unified magnetic equivalent circuit (UMEC) in order to analyze its electromagnetic characteristics. Firstly, the TCST may be divided into the two parts of the series winding and the exciting winding so that their magnetic equivalent circuits are established based on their iron core structures respectively, according to the magnetic coupling relationships among the internal windings of the TCST. Secondly, with the mathematical expressions of the electromagnetic transient models derived by the UMEC method for the two parts separately, an electromagnetic transient model of the TCST can be acquired by the combination of the series winding and the exciting winding in the light of their ele

## 核心贡献



- 提出基于统一磁路模型(UMEC)的双芯Sen变压器电磁暂态建模方法
- 揭示双芯结构下分接开关电流减半与调节步长缩小的特性，验证其经济性与控制精度优势

## 使用的方法


- [[state-space]]
- [[numerical-integration]]

## 涉及的模型


- [[transformer]]

## 相关主题


- [[transformer]]

## 主要发现



- 流过双芯Sen变压器分接开关的电流约为线路电流的50%，可显著降低设备制造成本
- 双芯Sen变压器的实际调节步长约为单芯结构的0.5倍，具备更高的潮流控制精度

## 方法细节

### 方法概述

本文基于统一磁路模型(UMEC)法建立双芯Sen变压器(TCST)的电磁暂态模型。该方法将TCST分解为串联变压器(三相组式结构)和励磁变压器(三相三柱式结构)两部分，分别建立磁等值回路。通过磁路-电路耦合关系，利用高斯磁通定律和法拉第电磁感应定律，推导磁通与电流的数学关系。采用梯形积分法对微分方程进行离散化，最终建立诺顿等效形式的电磁暂态模型，并通过内部电气连接关系将串-励两部分组合，形成完整的TCST电磁暂态仿真模型。该方法充分考虑了铁芯几何结构、磁通路径、绕组间磁耦合以及漏磁效应。

### 数学公式


**公式1**: $$\boldsymbol{\Phi}_{SA} = \mathbf{P}_{SA}(\mathbf{N}_{SA}\mathbf{I}_{SA} - \boldsymbol{\theta}_{SA}')$$

*支路磁通与磁动势的基本关系，其中Φ_SA为支路磁通矩阵，P_SA为支路磁导矩阵，N_SA为匝数矩阵，I_SA为绕组电流矩阵，θ_SA'为支路磁动势矩阵*


**公式2**: $$\mathbf{A}_{SA}^T\boldsymbol{\Phi}_{SA} = \mathbf{0}$$

*高斯磁通定律的矩阵形式，A_SA为节点-支路关联矩阵，表示流入节点的磁通代数和为零*


**公式3**: $$\boldsymbol{\Phi}_{MA} = \mathbf{Q}_{MMA}\mathbf{N}_{MA}\mathbf{I}_{MA}$$

*流过绕组的磁通与绕组电流的关系，Q_MMA为磁导转换子矩阵，通过Q = E - P_SA*A_SA*(A_SA^T*P_SA*A_SA)^(-1)*A_SA^T*P_SA计算得到*


**公式4**: $$\mathbf{U}_A = \mathbf{N}_{MA}\frac{d\boldsymbol{\Phi}_{MA}}{dt}$$

*法拉第电磁感应定律，U_A为绕组电压向量，N_MA为匝数对角矩阵，Φ_MA为磁通向量*


**公式5**: $$\mathbf{N}_{MA}\boldsymbol{\Phi}_{MA}(t) = \frac{\Delta t}{2}\mathbf{U}_A(t) + \boldsymbol{\Phi}_{MA,hist}(t)$$

*梯形积分离散形式，Δt为仿真时间步长，Φ_MA,hist为历史项磁链，Φ_MA,hist(t) = N_MA*Φ_MA(t-Δt) + (Δt/2)*U_A(t-Δt)*


**公式6**: $$\mathbf{I}_{MA}(t) = \mathbf{Y}_{MA}\mathbf{U}_A(t) + \mathbf{I}_{MA,hist}(t)$$

*串联变A相电磁暂态诺顿等效模型，Y_MA = (2/Δt)*Z_MA^(-1)为等效导纳矩阵，Z_MA = N_MA*Q_MMA*N_MA，I_MA,hist为历史项电流源*


**公式7**: $$\mathbf{I}_{Su}(t) = \mathbf{Y}_{Su}\mathbf{U}_{Su}(t) + \mathbf{I}_{Su,hist}(t)$$

*三相串联变整体电磁暂态模型，I_Su = [I_LA, I_LB, I_LC, I_a, I_b, I_c]^T为线路侧和阀侧电流，U_Su = [ΔU_A, ΔU_B, ΔU_C, U_a, U_b, U_c]^T为补偿电压和阀侧电压*


**公式8**: $$\mathbf{U}_{Eu} = \mathbf{N}_Z\frac{d\boldsymbol{\Phi}_{EM}}{dt}$$

*励磁变电磁感应方程，U_Eu为励磁变各绕组电压向量，N_Z为扩展匝数矩阵，Φ_EM为励磁变磁通向量*


### 算法步骤

1. 根据TCST内部绕组的磁耦合关系，将TCST分解为串联变(三相组式结构)和励磁变(三相三柱式结构)两部分

2. 对串联变每相建立单相磁等值回路，定义铁芯磁导(P_a, P_A)、漏磁导(P_la, P_lA)和铁轭磁导(P_aA)，建立支路磁通与磁动势的矩阵关系

3. 应用高斯磁通定律建立节点磁通约束方程，将支路磁动势表示为节点磁动势的线性组合

4. 推导磁通-电流转换矩阵Q_SA，建立流过绕组的磁通Φ_MA与绕组电流I_MA的关系式：Φ_MA = Q_MMA*N_MA*I_MA

5. 应用法拉第电磁感应定律建立电压-磁通微分方程，采用梯形积分法进行离散化，得到磁链与电压的离散关系式

6. 构造诺顿等效电路，计算等效导纳矩阵Y_MA = (2/Δt)*(N_MA*Q_MMA*N_MA)^(-1)和历史项电流源I_MA,hist

7. 对励磁变(三相三柱式)建立磁等值回路，考虑相间磁耦合(铁轭磁导P_AB, P_BC)和零序磁通路径(P_a0, P_b0, P_c0)

8. 重复步骤3-6，建立励磁变三相统一的电磁暂态模型，考虑9个副边调节绕组(a1-c3)的磁耦合关系

9. 根据TCST内部电气连接关系(励磁变副边输出U_Ea连接串联变原边，串联变副边串联接入线路)，将两部分模型结合

10. 建立整体TCST电磁暂态仿真模型，形成系统级诺顿等效方程，用于EMT仿真


### 关键参数

- **N_MA**: 串联变A相绕组匝数矩阵，2×2维，包含一次侧和二次侧匝数

- **P_SA**: 串联变支路磁导矩阵，包含铁芯磁导、漏磁导和铁轭磁导

- **Q_MMA**: 磁通-电流转换子矩阵，由磁导矩阵和关联矩阵计算得到

- **Δt**: 仿真时间步长，梯形积分法使用的时间离散间隔

- **Y_MA**: 等效导纳矩阵，Y_MA = (2/Δt)*Z_MA^(-1)，其中Z_MA = N_MA*Q_MMA*N_MA

- **分接开关电流比例**: 约50%，相对于线路电流

- **调节步长比例**: 约0.5倍，相对于单芯Sen变压器(SCST)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 稳态潮流控制验证 | 通过调节励磁变副边绕组抽头位置改变串联补偿电压ΔU，实现线路潮流调节。仿真显示TCST能够产生幅值和相位可调的串联补偿电压，验证模型的稳态特性 | 与理想变压器模型相比，所提UMEC模型考虑了铁芯饱和、漏磁和磁耦合效应，仿真精度更高 |

| 分接开关电流特性分析 | 流过TCST分接开关的电流约为线路电流的50%，显著低于单芯结构中分接开关直接串联在线路中的情况 | 相比单芯Sen变压器(SCST)，分接开关电流降低约50%，可大幅降低分接开关的绝缘要求和制造成本 |

| 调节步长精度对比 | TCST的实际调节步长约为单芯结构SCST的0.5倍。由于双芯结构中间接通过串联变注入补偿电压，励磁变副边绕组电压调节对线路补偿电压的影响更为精细 | 调节步长缩小为SCST的0.5倍，使得TCST具备更高的潮流控制精度 |

| MATLAB与PSCAD/EMTDC对比验证 | 在相同工况下，MATLAB解析计算结果与PSCAD/EMTDC时域仿真结果一致，验证了所建立UMEC模型的正确性和有效性 | 两种工具的仿真结果误差在可接受范围内，模型准确性得到验证 |



## 量化发现

- 流过TCST分接开关的电流约为线路电流的50%，可有效降低分接开关的绝缘水平和制造成本
- TCST的实际调节步长约为单芯Sen变压器(SCST)的0.5倍，控制精度提高一倍
- 励磁变采用三相三柱式结构，串联变采用三相组式结构，相间磁耦合通过铁轭磁导P_AB和P_BC建模
- 梯形积分法离散误差与步长Δt的平方成正比，保证数值稳定性
- 分接开关电流降低50%的同时，保持与单芯结构相同的潮流调节能力
- 双芯结构将调节绕组和分接开关从线路中隔离，避免系统故障过电流直接作用于分接开关


## 关键公式

### 电磁暂态诺顿等效模型

$$\mathbf{I}_{MA}(t) = \mathbf{Y}_{MA}\mathbf{U}_A(t) + \mathbf{I}_{MA,hist}(t)$$

*用于EMT仿真的基本方程，将变压器表示为等效导纳矩阵与历史项电流源并联的形式，适用于串联变单相建模*

### 等效导纳矩阵计算

$$\mathbf{Y}_{MA} = \left(\frac{\Delta t}{2}\mathbf{Z}_{MA}\right)^{-1}, \quad \mathbf{Z}_{MA} = \mathbf{N}_{MA}\mathbf{Q}_{MMA}\mathbf{N}_{MA}$$

*在离散化过程中，将磁路参数转换为电路导纳，用于计算当前时刻的电流-电压关系*

### 梯形积分历史项

$$\boldsymbol{\Phi}_{MA,hist}(t) = \mathbf{N}_{MA}\boldsymbol{\Phi}_{MA}(t-\Delta t) + \frac{\Delta t}{2}\mathbf{U}_A(t-\Delta t)$$

*存储前一时刻状态变量，用于计算当前时刻的历史项电流源，保证数值积分的精度和稳定性*

### 三相串联变整体模型

$$\mathbf{I}_{Su}(t) = \mathbf{Y}_{Su}\mathbf{U}_{Su}(t) + \mathbf{I}_{Su,hist}(t)$$

*将三相串联变压器组合为统一矩阵方程，I_Su包含线路电流和阀侧电流，U_Su包含补偿电压和阀侧电压*



## 验证详情

- **验证方式**: 解析计算与时域仿真对比验证，将所提UMEC模型计算结果与现有文献中SCST的电流、电压和功率结果进行对比分析
- **测试系统**: 双芯Sen变压器(TCST)测试系统，包含励磁变(原边星形联结并联接入送端，副边每相3个带分接开关绕组)和串联变(三相组式，副边串联接入线路)
- **仿真工具**: MATLAB(用于解析计算和矩阵运算)、PSCAD/EMTDC(用于电磁暂态时域仿真)
- **验证结果**: MATLAB解析计算结果与PSCAD/EMTDC时域仿真结果一致，验证了所提TCST电磁暂态模型的有效性。对比分析表明TCST分接开关电流约为线路电流50%，调节步长约为SCST的0.5倍，证实了双芯结构在经济性和控制精度上的优势
