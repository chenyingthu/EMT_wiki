---
title: "Proposal of an alternative transmission line model for symmetrical and asymmetrical configurations"
type: source
authors: ['Eduardo', 'Coelho', 'Marques', 'da', 'Costa']
year: 2011
journal: "International Journal of Electrical Power and Energy Systems, 33 (2011) 1375-1383. doi:10.1016/j.ijepes.2011.06.015"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/32/j.ijepes.2011.06.015.pdf.pdf"]
---

# Proposal of an alternative transmission line model for symmetrical and asymmetrical configurations

**作者**: Eduardo, Coelho, Marques 等
**年份**: 2011
**来源**: `32/j.ijepes.2011.06.015.pdf.pdf`

## 摘要

Proposal of an alternative transmission line model for symmetrical Eduardo Coelho Marques da Costa a,⇑, Sérgio Kurokawa b,2, Afonso José do Prado b,2, José Pissolato a,1 a Unicamp – Universidade Estadual de Campinas, Mail Box 6101, CEP 13081-970, Campinas, SP, Brazil b Unesp – Univ. Estadual Paulista, Av. Brasil Centro 56, Mail Box 31, CEP 15385-000, Ilha Solteira, SP, Brazil This article shows a transmission line model for simulation of fast and slow transients, applied to sym-

## 核心贡献


- 提出基于集中参数与状态空间的输电线路时域模型，无需反变换即可直接仿真快慢暂态
- 设计Clarke矩阵修正算法，获得实常数模变换矩阵，适用于非换位及不对称线路
- 采用基于特征系统的解析积分法求解状态方程，支持大固定步长且数值鲁棒性强


## 使用的方法


- [[状态空间法|状态空间法]]
- [[矢量拟合|矢量拟合]]
- [[模态分析|模态分析]]
- [[解析积分法|解析积分法]]
- [[集中参数法|集中参数法]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[三相非换位线路|三相非换位线路]]
- [[集中参数π型等效电路|集中参数π型等效电路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[时域直接仿真|时域直接仿真]]
- [[线路参数拟合|线路参数拟合]]


## 主要发现


- 模型在不对称三相线路测试中，与EMTP标准模型结果高度吻合，验证了时域精度
- 解析积分法允许采用较大固定步长，在保证精度的同时显著降低计算耗时
- 修正后的实常数模变换矩阵有效消除了高频段模域误差，适用于宽频暂态分析


