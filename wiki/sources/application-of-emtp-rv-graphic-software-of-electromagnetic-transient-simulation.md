---
title: "Application of EMTP-RV graphic software of electromagnetic transient simulation"
type: source
authors: ['未知']
year: 2007
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/09/Cao和Chen - 2007 - Application of EMTP-RV graphic software of electromagnetic transient simulation.pdf"]
---

# Application of EMTP-RV graphic software of electromagnetic transient simulation

**作者**: 
**年份**: 2007
**来源**: `09/Cao和Chen - 2007 - Application of EMTP-RV graphic software of electromagnetic transient simulation.pdf`

## 摘要

：In order tO introduce hoW tO use EMTP-RV(Restructured Version)．a new generation Windows-platform- based graphic software of electromagnetic transient simulation which is developed by EMTP_DCG(Development Co- ordination Group)。and to efficiently research and simulate the dynamic processes of power system and its apparatu- ses。this paper elaborates the basic features of three components of the software package：EMTP-RV core computa- tion engine，graphical user interlace EMTPWbrks and signal post-processing program ScopeView．Meanwhile-the libraries which include most important device models are depicted．A 35kV．100 MVA Static Var Compensator sire． ulation model was constructed to simulate the switching processes of its three-phase thyristors．The intuitive and US- er-friendly GraphicaI User Inte

## 核心贡献


- 阐述EMTP-RV软件架构与图形化建模流程，提供完整电磁暂态仿真环境
- 构建SVC晶闸管阀组开关暂态模型，验证软件处理电力电子动态过程能力
- 演示避雷器保护对晶闸管过电压的抑制效果，为阀组绝缘配合提供仿真依据


## 使用的方法


- [[稀疏矩阵求解|稀疏矩阵求解]]
- [[非线性迭代求解|非线性迭代求解]]
- [[时域仿真|时域仿真]]
- [[谐波分析|谐波分析]]
- [[离散傅里叶变换|离散傅里叶变换]]


## 涉及的模型


- [[svc|SVC]]
- [[tcr|TCR]]
- [[晶闸管阀组|晶闸管阀组]]
- [[zno避雷器|ZnO避雷器]]
- [[rlc支路|RLC支路]]
- [[断路器|断路器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[开关暂态|开关暂态]]
- [[过电压保护|过电压保护]]
- [[绝缘配合|绝缘配合]]
- [[facts装置建模|FACTS装置建模]]
- [[谐波分析|谐波分析]]


## 主要发现


- 仿真表明加装ZnO避雷器后晶闸管两端峰值电压由110.03kV降至62.29kV
- 软件可准确复现120度触发角下TCR阀组动态开关过程及过电压波形特征
- 图形化建模结合稀疏矩阵求解显著提升复杂电力网络电磁暂态仿真效率


