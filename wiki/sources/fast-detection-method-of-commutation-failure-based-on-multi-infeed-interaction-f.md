---
title: "Fast Detection Method of Commutation Failure Based on Multi-Infeed Interaction Factor"
type: source
authors: ['CNKI']
year: 2023
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/18/Zhang 等 - 2018 - Fast Detection Method of Commutation Failure in Multi Infeed DC System Considering the Effect of Unb.pdf"]
---

# Fast Detection Method of Commutation Failure Based on Multi-Infeed Interaction Factor

**作者**: CNKI
**年份**: 2023
**来源**: `18/Zhang 等 - 2018 - Fast Detection Method of Commutation Failure in Multi Infeed DC System Considering the Effect of Unb.pdf`

## 摘要

The dynamic characteristics of HVDC transmission have a serious impact on the overall power system stability, and that has become the most severe challenge in the multi infeed DC system. The correct identification of commutation failure when unbalanced faults occurred in AC system is of great significance, especially in the stability transient simulation with a quasi steady state DC model. This paper proposed a fast identification criterion to access commutation failure risk, based on the commutation equation of inverter valve, considering the effect of negative sequence voltage components on commutation voltage angle offset during unbalanced fault. The criterion can easily be used in the

## 核心贡献


- 提出计及负序电压引起换相电压角度偏移的快速判别判据，提升不对称故障识别精度
- 推导适用于对称与不对称故障的通用换相方程，弥补传统准稳态模型判别缺陷
- 将新判据嵌入机电暂态仿真接口，实现多馈入直流系统换相失败风险的快速评估


## 使用的方法


- [[准稳态模型|准稳态模型]]
- [[机电-电磁混合仿真|机电-电磁混合仿真]]
- [[对称分量法|对称分量法]]
- [[换相方程解析法|换相方程解析法]]


## 涉及的模型


- [[lcc-model|LCC]]
- [[12脉动换流器|12脉动换流器]]
- [[换流变压器|换流变压器]]
- [[多馈入直流系统|多馈入直流系统]]


## 相关主题


- [[换相失败|换相失败]]
- [[不对称故障|不对称故障]]
- [[机电-电磁混合仿真|机电-电磁混合仿真]]
- [[多馈入直流系统|多馈入直流系统]]
- [[负序电压影响|负序电压影响]]


## 主要发现


- 负序电压导致换相电压相位超前，显著减小关断角并大幅增加换相失败风险
- 所提判据与机电-电磁混合仿真结果高度一致，验证了其在暂态仿真中的准确性
- 仅含3%负序电压即可使关断角偏移约1.7度，证明计及负序分量对判别至关重要


