---
title: "Re-examination of Synchronous Machine"
type: source
authors: ['未知']
year: 2007
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/32/tpwrs.2007.901308.pdf.pdf"]
---

# Re-examination of Synchronous Machine

**作者**: 
**年份**: 2007
**来源**: `32/tpwrs.2007.901308.pdf.pdf`

## 摘要

—This paper re-examines the three synchronous ma- chine modeling techniques used for electromagnetic transient sim- ulations, namely, the model, phase-domain model, and voltage- behind-reactance model. Contrary to the claims made in several recent publications, these models are all equivalent in the contin- uous-time domain, as their corresponding differential equations can be algebraically derived from each other. Computer studies of a single-machine inﬁnite-bus system demonstrate that all of these models can be used for unsymmetrical operation of power sys- tems. The conversion of machine parameters is also discussed and is shown to have some impact on simulation accuracy, which is ac- ceptable for most cases. When the models are discretized and inter- faced with an EMTP-type network sol

## 核心贡献


- 证明dq0相域与电抗后电压模型在连续时域数学等价可相互代数推导
- 揭示离散化后与EMTP网络接口时VBR模型因结构优势精度最高
- 澄清参数转换对精度的影响并验证各模型均适用于不对称运行工况


## 使用的方法


- [[dq0变换建模|dq0变换建模]]
- [[相域建模|相域建模]]
- [[电抗后电压建模|电抗后电压建模]]
- [[节点分析法|节点分析法]]
- [[状态变量法|状态变量法]]
- [[数值离散化|数值离散化]]
- [[参数转换|参数转换]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[dq0模型|dq0模型]]
- [[相域模型|相域模型]]
- [[电抗后电压模型|电抗后电压模型]]
- [[单机无穷大系统|单机无穷大系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[不对称运行|不对称运行]]
- [[模型等价性|模型等价性]]
- [[参数转换|参数转换]]
- [[数值精度分析|数值精度分析]]
- [[emtp网络求解|EMTP网络求解]]


## 主要发现


- 连续时域下三种同步电机模型微分方程可相互推导数学上完全等价
- 仿真验证表明所有模型均能准确模拟电力系统不对称工况下的暂态响应
- 离散化后VBR模型在较大积分步长下仍保持最高数值精度与稳定性


