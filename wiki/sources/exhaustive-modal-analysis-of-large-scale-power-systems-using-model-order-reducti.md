---
title: "Exhaustive modal analysis of large-scale power systems using model order reduction"
type: source
authors: ['M. Kouki']
year: 2022
journal: "Electric Power Systems Research, 212 (2022) 108541. doi:10.1016/j.epsr.2022.108541"
tags: ['model-order-reduction']
created: "2026-04-13"
sources: ["EMT_Doc/18/Kouki 等 - 2022 - Exhaustive modal analysis of large-scale power systems using model order reduction.pdf"]
---

# Exhaustive modal analysis of large-scale power systems using model order reduction

**作者**: M. Kouki
**年份**: 2022
**来源**: `18/Kouki 等 - 2022 - Exhaustive modal analysis of large-scale power systems using model order reduction.pdf`

## 摘要

Exhaustive modal analysis of large-scale power systems using model order This paper presents an efficient modal analysis methodology that computes all modes of any given large-scale power system in exhaustive manner using the model order reduction techniques. For this, a reduced order model is generated using the Balanced Truncation (BT) method for which the controllability and observability gramians are approximated using the low-rank Cholesky factors. This leads to a rapid identification of cl

## 核心贡献


- 提出基于平衡截断法与低秩Cholesky分解的降阶模型快速识别动态设备耦合类
- 结合近似模态与修正Arnoldi迭代法实现无需先验知识的全局振荡模态精确计算
- 构建适用于高比例电力电子设备接入系统的多输入多输出交互量化分析框架


## 使用的方法


- [[平衡截断法|平衡截断法]]
- [[模型降阶技术|模型降阶技术]]
- [[低秩cholesky分解|低秩Cholesky分解]]
- [[修正arnoldi迭代法|修正Arnoldi迭代法]]
- [[状态空间线性化|状态空间线性化]]
- [[多输入多输出分析|多输入多输出分析]]


## 涉及的模型


- [[大规模互联电力系统|大规模互联电力系统]]
- [[欧洲电网模型|欧洲电网模型]]
- [[同步发电机|同步发电机]]
- [[电力电子变流器|电力电子变流器]]
- [[动态设备集群|动态设备集群]]


## 相关主题


- [[模态分析|模态分析]]
- [[小干扰稳定性|小干扰稳定性]]
- [[耦合模态识别|耦合模态识别]]
- [[高比例电力电子系统|高比例电力电子系统]]
- [[模型降阶|模型降阶]]
- [[区域间振荡|区域间振荡]]


## 主要发现


- 降阶模型显著降低耦合类识别计算复杂度且保持与原系统一致的输入输出动态特性
- 在欧洲互联电网验证中该方法能无先验知识地精确提取全部机电与电气耦合模态
- 修正Arnoldi法以近似模态为初值大幅缩短大规模系统全模态精确求解的迭代时间


