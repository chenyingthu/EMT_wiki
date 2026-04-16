---
title: "A Type-4 Wind Power Plant Equivalent Model"
type: source
year: 2012
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/04/tpwrs.2012.2227845.pdf.pdf"]
---

# A Type-4 Wind Power Plant Equivalent Model

**年份**: 2012
**来源**: `04/tpwrs.2012.2227845.pdf.pdf`

## 摘要

—This paper introduces an accurate and computation- ally efﬁcient reduced-order dynamic equivalent of a Type-4–based wind power plant (WPP) for the analysis of electromagnetic transients (EMTs) in the power system external to the WPP. The proposed model signiﬁcantly reduces the computational resources and the simulation run time while preserving the WPP response ﬁdelity in the desired frequency range, e.g., 0 to 50 kHz. The proposed WPP equivalent model is composed of two parts: 1) a frequency-dependent equivalent model which represents the WPP passive component in the entire frequency range and 2) a dynamic equivalent model that represents the WPP supervisory control and the aggregated low-frequency dynamics of wind-turbine generator (WTG) units. The latter can be constructed from the: 1)

## 核心贡献


- 提出适用于外部电磁暂态分析的Type-4风电场宽频带降阶动态等值模型
- 将频变无源网络等值模型与低频动态等值模型结合实现全频段高精度响应
- 建立系统化方法构建包含风机局部控制与场站监督控制的低频动态等值模型


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[频率扫描|频率扫描]]
- [[伴随电路法|伴随电路法]]
- [[傅里叶分析|傅里叶分析]]
- [[有理函数逼近|有理函数逼近]]


## 涉及的模型


- [[type-4风电场|Type-4风电场]]
- [[type-4直驱风机|Type-4直驱风机]]
- [[fdne-model|FDNE]]
- [[dlfe低频动态等值模型|DLFE低频动态等值模型]]
- [[集电系统|集电系统]]
- [[网侧变流器|网侧变流器]]


## 相关主题


- [[电磁暂态分析|电磁暂态分析]]
- [[动态等值|动态等值]]
- [[频率相关建模|频率相关建模]]
- [[风电场建模|风电场建模]]
- [[降阶建模|降阶建模]]
- [[宽频带响应|宽频带响应]]


## 主要发现


- 模型在0至50kHz频段内保持高保真度显著降低计算资源与仿真耗时
- PSCAD对比验证表明等值模型动态响应精度与详细模型高度一致
- 背靠背变流器解耦效应使低频动态模型仅需聚合网侧变流器即可准确表征


