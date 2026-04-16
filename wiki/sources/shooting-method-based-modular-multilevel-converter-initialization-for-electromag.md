---
title: "Shooting method based modular multilevel converter initialization for electromagnetic transient analysis"
type: source
authors: ['D.', 'del', 'Giudice']
year: 2024
journal: "International Journal of Electrical Power and Energy Systems, 161 (2024) 110163. doi:10.1016/j.ijepes.2024.110163"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/34/del Giudice 等 - 2024 - Shooting method based modular multilevel converter initialization for electromagnetic transient anal.pdf"]
---

# Shooting method based modular multilevel converter initialization for electromagnetic transient analysis

**作者**: D., del, Giudice
**年份**: 2024
**来源**: `34/del Giudice 等 - 2024 - Shooting method based modular multilevel converter initialization for electromagnetic transient anal.pdf`

## 摘要

International Journal of Electrical Power and Energy Systems Shooting method based modular multilevel converter initialization for D. del Giudice a,∗, F. Bizzarri a,b, D. Linaro a, A. Brambilla a a Dipartimento di Elettronica, Informazione e Bioingegneria, Politecnico di Milano, p.za Leonardo da Vinci, 32, I20133, Milano, Italy b Advanced Research Center on Electronic Systems ‘‘E. De Castro’’ (ARCES), University of Bologna, Italy

## 核心贡献



- 提出了一种基于打靶法的模块化多电平换流器（MMC）初始化策略，用于电磁暂态仿真
- 该策略兼容不同详细程度的MMC模型及包含调制与电容电压平衡的控制算法，能显著减少初始化暂态及额外CPU时间

## 使用的方法


- [[numerical-integration]]
- [[network-equivalent]]
- [[state-space]]

## 涉及的模型


- [[mmc]]
- [[mmc-model]]
- [[average-value-model]]

## 相关主题


- [[mmc]]
- [[hvdc]]
- [[vsc-hvdc]]

## 主要发现



- 基于打靶法的初始化策略可使仿真直接从接近稳态的条件启动，有效抑制了初始化暂态过程
- 在含128电平MMC的NORDIC32系统测试中，该方法大幅缩短了达到稳态所需的仿真时间，提升了EMT计算效率