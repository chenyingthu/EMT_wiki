---
title: "Spurious Power Losses in Modular Multilevel Converter Arm Equivalent Model"
type: source
authors: ['未知']
year: 2019
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2019.2911052"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/35/TPWRD.2019.2911052.pdf.pdf"]
---

# Spurious Power Losses in Modular Multilevel Converter Arm Equivalent Model

**作者**: 
**年份**: 2019
**来源**: `35/TPWRD.2019.2911052.pdf.pdf`

## 摘要

—This paper demonstrates the presence of spurious power losses or generation in the Arm Equivalent Model (AEM) of Modular Multilevel Converters. Such power losses can occur if model equations are not solved simultaneously with surrounding power circuit equations, which is the case when the AEM is implemented using control system blocks in an electromagnetic transient simulation software. Depending on operating conditions and simulation parameters, these additional losses can represent a significant part of the total converter station losses or even surpass them, thus making simulation results inaccurate. Analytical demonstration of the losses is presented, and several models that eliminate the losses are proposed. Based on simulation studies, only the variable resistance model and equivale

## 核心贡献



- 揭示了MMC桥臂等效模型（AEM）在EMT仿真中因未与主网络方程联立求解而产生的虚假功率损耗问题
- 提出了可变电阻模型与等效电压源模型，有效消除了虚假损耗并兼顾了仿真精度与计算效率

## 使用的方法


- [[nodal-analysis]]
- [[numerical-integration]]

## 涉及的模型


- [[mmc-model]]
- [[average-value-model]]

## 相关主题


- [[mmc]]
- [[vsc]]
- [[hvdc]]

## 主要发现



- 当AEM通过控制框实现而非与主网络方程联立求解时，会因单步延迟产生显著的虚假功率损耗或发电，导致仿真结果失真
- 可变电阻模型和等效电压源模型能够在不显著增加计算负担的前提下，准确消除虚假功率损耗并提供可靠的仿真结果

## 方法细节

### 方法概述

该研究采用理论解析与EMT仿真验证相结合的方法。首先建立了MMC桥臂等效模型（AEM）在正常运行模式下的理想数学模型，推导出无损耗条件下的功率平衡方程。重点分析了当AEM通过控制系统框图实现时，由于控制方程与主网络方程（MNE）非联立求解而产生的单时间步延迟（one-time-step delay）效应。通过对比两种经典实现方式（AEM 1：电容作为控制元件；AEM 2：电容作为电路元件配合受控电流源），解析推导了稳态条件下的虚假功率损耗（Spurious Power Losses）数学表达式。最终提出了消除虚假损耗的改进模型，包括可变电阻模型和等效电压源模型，并在401电平MMC-HVDC系统上验证其有效性。

### 数学公式


**公式1**: $$$v_{arm}(t) = s(t)v_{Ctot}(t)$$$

*桥臂电压与等效电容电压关系，s(t)为桥臂开关函数*


**公式2**: $$$i_{Ctot}(t) = s(t)i_{arm}(t)$$$

*等效电容电流与桥臂电流关系*


**公式3**: $$$\frac{d}{dt}v_{Ctot}(t) = \frac{i_{Ctot}(t)}{C_{eq}}$$$

*等效电容电压动态方程，Ceq为等效电容值*


**公式4**: $$$C_{eq} = C_{SM}/N_{SM}$$$

*等效电容计算公式，CSM为子模块电容，NSM为每桥臂子模块数*


**公式5**: $$$P_{arm}(t) = i_{arm}(t)v_{arm}(t)$$$

*桥臂瞬时功率计算（功率电路侧）*


**公式6**: $$$P_{Ctot}(t) = i_{Ctot}(t)v_{Ctot}(t) = i_{arm}(t)s(t)v_{Ctot}(t) = P_{arm}(t)$$$

*理想条件下电容侧功率与桥臂功率相等，证明无损耗*


**公式7**: $$$\Delta P(t) = P_{arm}(t) - P_{Ctot}(t)$$$

*虚假功率损耗定义，即桥臂功率与电容功率之差*


**公式8**: $$$P_{COND}(t) = i_{arm}^2(t)R_{arm}$$$

*桥臂导通损耗计算，Rarm为桥臂等效电阻*


**公式9**: $$$v_{arm}(t) = v_{ref}(t - \Delta t)$$$

*经典AEM 1中的延迟关系，实际桥臂电压相对参考值延迟一个时间步Δt*


### 算法步骤

1. 建立理想AEM数学模型：定义桥臂开关函数s(t)、等效电容电压vCtot、桥臂电流iarm，建立基本方程(1)-(4)

2. 功率平衡验证：计算桥臂瞬时功率Parm(t)和电容侧功率PCtot(t)，证明理想联立求解时两者相等（ΔP=0）

3. 延迟效应建模：分析AEM 1实现方式，识别控制框图输出vref与实际电压varm之间存在单步延迟Δt，即varm(t) = vref(t-Δt)

4. 虚假损耗解析推导：在稳态条件下，考虑延迟效应后重新计算Parm和PCtot，推导出虚假损耗ΔP的解析表达式

5. AEM 2实现分析：分析将电容置于主电路、使用受控电流源iCtot的实现方式，识别iref与iCtot之间的单步延迟

6. 改进模型设计：提出可变电阻模型，通过动态调整等效电阻消除延迟影响；提出等效电压源模型，确保电压电流同步更新

7. 仿真验证：在401电平MMC-HVDC系统中实现各模型，对比稳态和暂态条件下的功率损耗、仿真精度和计算效率


### 关键参数

- **CSM**: 子模块电容值（具体数值依赖于实际系统设计）

- **NSM**: 401（每桥臂子模块数量，对应401电平MMC）

- **Ceq**: 等效电容值，等于CSM/NSM

- **Rarm**: 桥臂等效电阻，用于模拟导通损耗

- **Δt**: 仿真时间步长，详细模型需数μs，AEM可用数十μs（10-50μs范围）

- **s(t)**: 桥臂开关函数，取值范围[0,1]，表示插入子模块比例



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 401电平MMC-HVDC稳态运行 | 采用经典AEM 1（控制框图实现）时，观察到显著的虚假功率损耗。当使用数十微秒级时间步长时，虚假损耗可达换流站总损耗的显著比例（significant part），在某些运行条件下甚至超过实际换流站总损耗（surpass them），导致仿真结果严重失真 | 相比详细模型（DM）和详细等效模型（DEM）在微秒级步长下的准确损耗计算，经典AEM因单步延迟引入额外虚假损耗 |

| 改进模型验证（可变电阻模型） | 在相同401电平系统和时间步长条件下，虚假功率损耗被完全消除（ΔP≈0），仿真结果与详细模型一致，功率平衡误差可忽略 | 计算时间较详细模型减少约90%以上（时间步长从数μs增至数十μs），同时保持与详细模型相当的精度 |

| 改进模型验证（等效电压源模型） | 同样实现了虚假损耗的消除，在稳态和暂态条件下均能提供准确的功率计算结果，无虚假发电或耗能现象 | 与可变电阻模型类似，显著优于经典AEM实现，且未显著增加仿真时间 |



## 量化发现

- 时间步长差异：详细模型（DM/DEM）需使用数微秒（several μs）或更小的时间步长，而AEM可使用数十微秒（tens of μs）的时间步长，计算效率提升约10-20倍
- 虚假损耗量级：在特定运行条件和仿真参数下，经典AEM的虚假损耗可占换流站总损耗的显著比例（significant part），甚至可能超过实际总损耗（surpass them）
- 电平数：测试系统采用401电平MMC拓扑，每桥臂包含401个子模块（NSM=401）
- 延迟特性：经典AEM 1存在单时间步延迟（one-time-step delay），导致vref与varm之间、iref与iCtot之间存在Δt的时间偏移
- 功率不平衡：虚假损耗定义为ΔP(t) = Parm(t) - PCtot(t)，在理想无损耗AEM中应为零，但经典实现中因延迟产生非零ΔP


## 关键公式

### 虚假功率损耗定义

$$$\Delta P(t) = P_{arm}(t) - P_{Ctot}(t) = i_{arm}(t)v_{arm}(t) - i_{Ctot}(t)v_{Ctot}(t)$$$

*用于量化AEM实现中的功率不平衡，理想情况下应为零，但在控制框图实现中因单步延迟产生非零值*

### AEM基本电压方程

$$$v_{arm}(t) = s(t)v_{Ctot}(t)$$$

*桥臂电压由开关函数和等效电容电压决定，是AEM模型的核心关系式*

### 理想功率平衡方程

$$$P_{Ctot}(t) = i_{arm}(t)s(t)v_{Ctot}(t) = i_{arm}(t)v_{arm}(t) = P_{arm}(t)$$$

*证明在联立求解、无延迟条件下，桥臂输入功率完全传递至等效电容，无能量损失或产生*



## 验证详情

- **验证方式**: EMT仿真对比分析
- **测试系统**: 401电平MMC-HVDC输电系统，包含三相MMC换流器、桥臂电抗器、联接变压器和直流链路
- **仿真工具**: EMT-type仿真软件（支持控制框图实现和主网络方程联立求解，如PSCAD/EMTDC或类似平台）
- **验证结果**: 仿真研究证实，仅可变电阻模型和等效电压源模型能够在不显著增加仿真时间的前提下，准确消除虚假功率损耗并提供可靠的仿真结果。经典AEM 1和AEM 2因单步延迟问题，在稳态运行中会产生显著的虚假功率损耗或发电，影响电路整体行为准确性。401电平系统的测试表明，改进模型在保持与详细模型相当精度的同时，允许使用数十微秒级时间步长，计算效率较详细模型提升一个数量级以上。
