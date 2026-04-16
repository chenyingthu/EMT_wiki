---
title: "EMTP model of a bidirectional multilevel solid state transformer for distribution system studies"
type: source
authors: ['未知']
year: 2014
journal: "2015 IEEE Power & Energy Society General Meeting;2015; ; ;10.1109/PESGM.2015.7285869"
tags: ['transformer', 'emtp']
created: "2026-04-13"
sources: ["EMT_Doc/17/González 等 - 2015 - EMTP model of a bidirectional multilevel solid state transformer for distribution system studies.pdf"]
---

# EMTP model of a bidirectional multilevel solid state transformer for distribution system studies

**作者**: 
**年份**: 2014
**来源**: `17/González 等 - 2015 - EMTP model of a bidirectional multilevel solid state transformer for distribution system studies.pdf`

## 摘要

—This paper presents a model for a MV/LV bidirectional solid state transformer (SST) for distribution system studies. A multilevel converter configuration is used in the MV side for voltage and current harmonic reduction. The model has been implemented in the ATP version of the EMTP. Several case studies have been carried out in order to evaluate the behavior of the SST model under different operating conditions and test the impact on the power quality.

## 核心贡献


- 提出基于ATP/EMTP封装的双向固态变压器定制模型，便于配电网集成研究。
- 设计高压侧三电平NPC整流器与虚拟空间矢量调制，实现直流中点电压自平衡。
- 构建低压侧四桥臂逆变器及正负零序独立控制器，有效隔离电网不平衡扰动。


## 使用的方法


- [[脉宽调制-pwm|脉宽调制(PWM)]]
- [[电压定向控制-voc|电压定向控制(VOC)]]
- [[虚拟空间矢量调制-svm|虚拟空间矢量调制(SVM)]]
- [[序分量分离控制|序分量分离控制]]
- [[移相功率控制|移相功率控制]]


## 涉及的模型


- [[固态变压器-sst|固态变压器(SST)]]
- [[三电平npc变换器|三电平NPC变换器]]
- [[双有源桥-dab-变换器|双有源桥(DAB)变换器]]
- [[高频隔离变压器|高频隔离变压器]]
- [[四桥臂逆变器|四桥臂逆变器]]
- [[配电网架空线路|配电网架空线路]]


## 相关主题


- [[配电网建模|配电网建模]]
- [[电能质量分析|电能质量分析]]
- [[双向功率流动|双向功率流动]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[电压暂降与不平衡抑制|电压暂降与不平衡抑制]]
- [[固态变压器|固态变压器]]


## 主要发现


- 二次侧负载突变或过流时，扰动几乎不向一次侧传播，母线电压保持稳定。
- 中压侧发生短路电压暂降时，二次侧相电压与电流仍保持恒定且三相对称。
- 负载与分布式电源共存工况下，验证了模型具备快速双向潮流反转能力。


