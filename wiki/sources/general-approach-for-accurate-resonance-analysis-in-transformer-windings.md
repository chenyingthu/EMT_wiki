---
title: "General approach for accurate resonance analysis in transformer windings"
type: source
authors: ['M. Popov']
year: 2018
journal: "Electric Power Systems Research, 161 (2018) 45-51. doi:10.1016/j.epsr.2018.04.002"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/j.epsr.2018.04.002.pdf.pdf"]
---

# General approach for accurate resonance analysis in transformer windings

**作者**: M. Popov
**年份**: 2018
**来源**: `19、20、21/EMT_task_20/j.epsr.2018.04.002.pdf.pdf`

## 摘要

1. Introduction that provides insight about voltage amplitudes along the winding is the ampliﬁcation factor. This parameter was studied in Ref. [1]. Transformers are important devices which are inevitable for the During non-standard waves, resonance overvoltages may take dif- existence and the op...

## 核心贡献


- 提出基于绕组节点导纳与阻抗矩阵的变压器内部谐振精确分析方法
- 引入放大因子参数精准定位绕组内部瞬态过电压最严重的线圈位置
- 结合修正傅里叶逆变换实现频域阻抗到时域电压分布的高效数值转换


## 使用的方法


- [[节点导纳矩阵法|节点导纳矩阵法]]
- [[阻抗矩阵法|阻抗矩阵法]]
- [[修正傅里叶逆变换|修正傅里叶逆变换]]
- [[atp-emtp仿真|ATP-EMTP仿真]]
- [[白盒建模|白盒建模]]


## 涉及的模型


- [[变压器绕组|变压器绕组]]
- [[测试线圈|测试线圈]]
- [[箔式变压器|箔式变压器]]
- [[atp-emtp等效模型|ATP-EMTP等效模型]]


## 相关主题


- [[谐振分析|谐振分析]]
- [[过电压评估|过电压评估]]
- [[绕组电压分布|绕组电压分布]]
- [[放大因子|放大因子]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 主要发现


- 测试线圈在7.4kHz谐振频率处放大因子达峰值第六线圈电压应力最高
- 谐振激励下绕组各线圈电压幅值显著超越输入激励呈现强非线性分布
- 最大谐振过电压幅值直接受激励脉冲持续时间与系统固有谐振频率影响


