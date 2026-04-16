---
title: "Generalized Electromagnetic Transient Equivalent Modeling and Implementation of MMC With Arbitrary M"
type: source
authors: ['CNKI']
year: 2023
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/Xu 等 - 2019 - Generalized Electromagnetic Transient Equivalent Modeling and Implementation of MMC With Arbitrary M.pdf"]
---

# Generalized Electromagnetic Transient Equivalent Modeling and Implementation of MMC With Arbitrary M

**作者**: CNKI
**年份**: 2023
**来源**: `19、20、21/EMT_task_20/Xu 等 - 2019 - Generalized Electromagnetic Transient Equivalent Modeling and Implementation of MMC With Arbitrary M.pdf`

## 摘要

The key issue of electromagnetic transient (EMT) modelling of modular multilevel converters (MMC) is calculation of equivalent circuit of entire MMC arm containing a large number of cascaded sub-modules (SM) with identical structure. During this process, all internal information should be preserved. This paper proposes a general EMT modelling approach for arbitrary multi-port MMC topologies, also suitable for traditional single-port MMC and emerging two-port MMC. A submodule topology identification method is proposed to minimize the efforts of the model users when they have specific MMC topologies at hand. In addition, the model codes can be inherited to a large extent. Finally, the approaches are validated in PSCAD/EMTDC with results of very good applicability of the

## 核心贡献


- 提出任意多端口子模块拓扑自动识别方法，通过关联矩阵自动生成节点方程
- 建立无需符号解析解的通用等效建模算法，实现模型代码高度继承与快速编程
- 突破传统戴维南等效限制，实现单双端口及不对称多端口换流器的统一精确建模


## 使用的方法


- [[节点分析法|节点分析法]]
- [[伴随电路法|伴随电路法]]
- [[拓扑自动识别|拓扑自动识别]]
- [[矩阵分块消元|矩阵分块消元]]
- [[诺顿等效|诺顿等效]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[单端口子模块|单端口子模块]]
- [[双端口子模块|双端口子模块]]
- [[双半桥子模块|双半桥子模块]]
- [[并联全桥子模块|并联全桥子模块]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[等效建模|等效建模]]
- [[柔性直流输电|柔性直流输电]]
- [[实时仿真|实时仿真]]
- [[直流故障穿越|直流故障穿越]]


## 主要发现


- PSCAD验证表明算法适用于单双端口拓扑，仿真精度高且具备强通用性
- 输入拓扑矩阵即可自动生成节点方程，大幅降低编程工作量并实现代码继承
- 模型计算效率满足高电平大容量仿真需求，可无缝应用于离线与实时仿真平台


