---
title: "Enhancements to Terminal Duality-based models for three-phase multi-limb multi-winding transformers"
type: source
authors: ['Meysam Ahmadi']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112204. doi:10.1016/j.epsr.2025.112204"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/17/Ahmadi 等 - 2026 - Enhancements to Terminal Duality-based models for three-phase multi-limb multi-winding transformers.pdf"]
---

# Enhancements to Terminal Duality-based models for three-phase multi-limb multi-winding transformers

**作者**: Meysam Ahmadi
**年份**: 2025
**来源**: `17/Ahmadi 等 - 2026 - Enhancements to Terminal Duality-based models for three-phase multi-limb multi-winding transformers.pdf`

## 摘要

Enhancements to Terminal Duality-based models for three-phase multi-limb This paper introduces an enhanced electromagnetic transient (EMT) model for three-phase multi-limb multi- winding transformers based on the Terminal Duality Method (TDM). The proposed model improves accuracy by incorporating zero-sequence path inductances, specifically for three-limb transformers, which are formulated for the first time. A closed-form formula is developed to precisely calculate the zero-sequence path induct

## 核心贡献


- 首次推导三柱变压器零序路径电感闭式公式，实现用户自定义零序阻抗精确匹配
- 提出轭部电感分布建模方法，按绕组堆叠比例分配磁阻，提升多柱变压器磁路精度
- 引入油箱节点参考技术稳定非线性电感割集，有效抑制电磁暂态仿真中的数值振荡


## 使用的方法


- [[终端对偶法-tdm|终端对偶法(TDM)]]
- [[归一化铁芯概念-ncc|归一化铁芯概念(NCC)]]
- [[闭式解析计算|闭式解析计算]]
- [[磁路对偶变换|磁路对偶变换]]
- [[参考节点法|参考节点法]]


## 涉及的模型


- [[三相多柱多绕组变压器|三相多柱多绕组变压器]]
- [[三柱变压器|三柱变压器]]
- [[磁路对偶等效电路|磁路对偶等效电路]]
- [[非线性电感模型|非线性电感模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[变压器零序阻抗建模|变压器零序阻抗建模]]
- [[不对称运行分析|不对称运行分析]]
- [[实时仿真-rtds|实时仿真(RTDS)]]
- [[数值振荡抑制|数值振荡抑制]]


## 主要发现


- 模型在开路、短路及励磁涌流工况下与PSCAD基准结果高度一致，验证了计算精度
- 零序路径电感的引入使模型能准确复现三柱变压器在断相及不对称工况下的电磁特性
- 油箱参考节点法成功消除非线性电感割集引发的数值振荡，显著提升实时仿真稳定性


