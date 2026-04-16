---
title: "An Automatable Approach for Small-Signal Stability Analysis of Power Electronic-Based Power Systems Using EMT Companion Circuits"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Delivery;2023;38;4;10.1109/TPWRD.2023.3264296"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/06/Chindu和Kulkarni - 2023 - An Automatable Approach for Small-Signal Stability Analysis of Power Electronic-Based Power Systems.pdf"]
---

# An Automatable Approach for Small-Signal Stability Analysis of Power Electronic-Based Power Systems Using EMT Companion Circuits

**作者**: 
**年份**: 2023
**来源**: `06/Chindu和Kulkarni - 2023 - An Automatable Approach for Small-Signal Stability Analysis of Power Electronic-Based Power Systems.pdf`

## 摘要

—The increasing presence of power electronic (PE) con- trolled devices in power systems has widened the bandwidth of transients to be studied for grid stability. While these transients are normally studied using time-domain simulation (TDS), wide bandwidth linear time-invariant (LTI) state-space models are a useful complement to TDS for diagnostics, controller design and parametric analysis. A general automatable method to compute an LTI sampled-data model of a PE-based circuit is presented in this paper. The proposed method is based on the techniques employed in electro-magnetic-transient (EMT) programs to perform TDS of PE-based circuits. The method uses the building blocks of EMT nodalformulationsuchasconductancematrixofcompanioncircuit and its LU factors computed during TDS, interpolat

## 核心贡献


- 提出基于EMT节点导纳矩阵与LU分解的自动化方法构建LTI采样数据模型
- 复用EMT暂态仿真伴随电路导纳矩阵及历史项实现小信号模型自动提取
- 给出剔除EMT数值离散引入的伪特征值判据确保稳定性分析物理准确


## 使用的方法


- [[伴随电路法|伴随电路法]]
- [[节点分析法|节点分析法]]
- [[梯形积分法|梯形积分法]]
- [[lu分解|LU分解]]
- [[采样数据建模|采样数据建模]]
- [[特征值分析|特征值分析]]
- [[颤振消除校正|颤振消除校正]]


## 涉及的模型


- [[rlc电路|RLC电路]]
- [[buck变换器|Buck变换器]]
- [[并网statcom|并网STATCOM]]
- [[电力电子开关|电力电子开关]]
- [[闭环控制系统|闭环控制系统]]


## 相关主题


- [[小信号稳定性分析|小信号稳定性分析]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[电力电子化电力系统|电力电子化电力系统]]
- [[采样数据建模|采样数据建模]]
- [[状态空间模型|状态空间模型]]
- [[自动化建模|自动化建模]]


## 主要发现


- 成功提取Buck变换器与STATCOM的LTI模型特征值分析结果准确
- 证实部分特征值为EMT数值算法引入的伪模态需通过判据予以剔除
- 验证复用EMT仿真中间数据构建小信号模型的可行性提升自动化程度


