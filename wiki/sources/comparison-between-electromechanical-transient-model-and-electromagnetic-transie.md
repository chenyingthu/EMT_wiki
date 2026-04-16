---
title: "Comparison between electromechanical transient model and electromagnetic transient model of DC in lo"
type: source
authors: ['未知']
year: 2013
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/10/Wang 等 - 2013 - Comparison between electromechanical transient model and electromagnetic transient model of DC in lo.pdf"]
---

# Comparison between electromechanical transient model and electromagnetic transient model of DC in lo

**作者**: 
**年份**: 2013
**来源**: `10/Wang 等 - 2013 - Comparison between electromechanical transient model and electromagnetic transient model of DC in lo.pdf`

## 摘要

For AC and DC operating system Low Frequency Oscillation (LFO) Analysis, DC system usually adopts electromechanical transient model. This paper introduces the DC electromechanical transient and electromagnetic transient model, and then establishes the electromechanical transient model and the electromechanical-electromagnetic transient hybrid simulation model on the Advanced Digital Power System Simulator (ADPSS) platform for the LFO analysis respectively. Adopting the total least squares method-rotational invariance techniques of signal parameter estimation (TLS-ESPRIT) algorithm, the oscillation power after failure is analyzed. After extracting the LFO dominant oscillation frequency and damping ratio for making the modal analysis, it compares the LFO analysis results of the two simulatio

## 核心贡献


- 构建直流机电暂态与机电-电磁混合仿真模型，实现交直流系统低频振荡对比分析。
- 引入TLS-ESPRIT算法提取故障后功率信号特征，完成主导频率与阻尼比模态分析。
- 验证直流准稳态模型在低频振荡分析中的有效性，为工程仿真模型选型提供依据。


## 使用的方法


- [[tls-esprit算法|TLS-ESPRIT算法]]
- [[隐式梯形积分法|隐式梯形积分法]]
- [[节点分析法|节点分析法]]
- [[机电-电磁暂态混合仿真|机电-电磁暂态混合仿真]]
- [[准稳态等值建模|准稳态等值建模]]


## 涉及的模型


- [[直流准稳态模型|直流准稳态模型]]
- [[12脉冲换流器|12脉冲换流器]]
- [[换流变压器|换流变压器]]
- [[平波电抗器|平波电抗器]]
- [[交直流滤波器|交直流滤波器]]
- [[直流线路t型集中参数模型|直流线路T型集中参数模型]]
- [[同步发电机|同步发电机]]


## 相关主题


- [[低频振荡分析|低频振荡分析]]
- [[交直流混合系统|交直流混合系统]]
- [[混合仿真|混合仿真]]
- [[模态分析|模态分析]]
- [[直流输电系统建模|直流输电系统建模]]


## 主要发现


- 两种模型仿真结果趋势一致，主导振荡频率接近，阻尼比差异小于0.3%。
- 电磁暂态混合模型能更详细描述故障暂态过程，机电模型可准确反映总体振荡趋势。
- 直流机电暂态准稳态模型在低频振荡分析中具备较高精度与工程实用价值。


