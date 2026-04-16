---
title: "Photovoltaic generator modelling to improve numerical robustness of EMT simulation"
type: source
authors: ['Anna', 'Rita', 'Di', 'Fazio']
year: 2011
journal: "Electric Power Systems Research, 83 (2011) 136-143. 10.1016/j.epsr.2011.10.013"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/31/j.epsr.2011.10.013.pdf.pdf"]
---

# Photovoltaic generator modelling to improve numerical robustness of EMT simulation

**作者**: Anna, Rita, Di 等
**年份**: 2011
**来源**: `31/j.epsr.2011.10.013.pdf.pdf`

## 摘要

1. Introduction When PV systems are included into the power system sim- ulation, the non-linearities present in the PV generator models In recent years the growing concern for environment preserva- require special attention. On one side, they cannot be neglected tion has caused a wide spreading o...

## 核心贡献


- 提出扩展线性系统技术将光伏非线性方程嵌入线性网络消除单步延迟引发的数值失稳
- 构建收敛性分析框架从数学层面证明新方法相比传统分离求解法的稳定性显著提升


## 使用的方法


- [[基本线性系统技术-blst|基本线性系统技术(BLST)]]
- [[扩展线性系统技术-elst|扩展线性系统技术(ELST)]]
- [[收敛性分析|收敛性分析]]
- [[节点分析法|节点分析法]]


## 涉及的模型


- [[光伏发电机|光伏发电机]]
- [[单二极管等效电路|单二极管等效电路]]
- [[ieee标准测试系统|IEEE标准测试系统]]
- [[并网逆变器|并网逆变器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[数值稳定性|数值稳定性]]
- [[光伏系统建模|光伏系统建模]]
- [[局部阴影效应|局部阴影效应]]
- [[分布式发电|分布式发电]]


## 主要发现


- 扩展线性系统技术有效克服了传统方法在局部阴影或多二极管模型下的数值发散问题
- IEEE标准系统仿真验证表明新方法在电气故障与局部阴影工况下均能保持收敛稳定


