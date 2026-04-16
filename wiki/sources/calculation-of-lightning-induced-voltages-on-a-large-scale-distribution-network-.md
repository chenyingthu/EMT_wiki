---
title: "Calculation of lightning-induced voltages on a large-scale distribution network using the JMarti model"
type: source
authors: ['Alberto', 'De', 'Conti']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112232. doi:10.1016/j.epsr.2025.112232"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/10/De Conti和Leal - 2026 - Calculation of lightning-induced voltages on a large-scale distribution network using the JMarti mod.pdf"]
---

# Calculation of lightning-induced voltages on a large-scale distribution network using the JMarti model

**作者**: Alberto, De, Conti
**年份**: 2025
**来源**: `10/De Conti和Leal - 2026 - Calculation of lightning-induced voltages on a large-scale distribution network using the JMarti mod.pdf`

## 摘要

Calculation of lightning-induced voltages on a large-scale distribution a Department of Electrical Engineering, Universidade Federal de Minas Gerais (UFMG), Belo Horizonte, MG, 31270-901, Brazil b Institute of Engineering, Science and Technology, Universidade Federal dos Vales do Jequitinhonha e Mucuri (UFVJM), Janaúba, Brazil This paper illustrates the application of a recently proposed time-domain method in the calculation of lightning- induced voltages by nearby cloud-to-ground lightning stri

## 核心贡献


- 提出基于独立电流源的时域方法将外部雷击电磁场效应等效注入线路两端
- 利用ATP内置拟合工具直接获取JMartí模型参数免去额外导纳拟合步骤
- 结合JMartí模型与扩展模域方法实现大规模配网雷击暂态高效计算


## 使用的方法


- [[时域方法|时域方法]]
- [[扩展模域-emd-模型|扩展模域(EMD)模型]]
- [[独立电流源等效|独立电流源等效]]
- [[有理函数拟合|有理函数拟合]]
- [[卷积积分计算|卷积积分计算]]


## 涉及的模型


- [[jmartí输电线路模型|JMartí输电线路模型]]
- [[配电变压器|配电变压器]]
- [[避雷器|避雷器]]
- [[接地系统|接地系统]]
- [[配电网负荷|配电网负荷]]


## 相关主题


- [[雷击感应过电压|雷击感应过电压]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关损耗建模|频率相关损耗建模]]
- [[大规模配电网|大规模配电网]]
- [[atp仿真|ATP仿真]]


## 主要发现


- 忽略频率相关线路损耗会导致大规模配网雷击感应电压计算出现显著误差
- 基于JMartí模型与内置拟合数据的时域方法可精确计算复杂配网感应电压
- 外部场效应仅需计算一次大幅提升了含非线性元件系统参数扫描的效率


