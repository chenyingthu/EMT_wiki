---
title: "Digital Time-Domain Investigation of Transient Behavior of Coupling Capacitor Voltage Transformer"
type: source
authors: ['M.R. Iravani', 'X. Wang', 'I. Polishchuk', 'J. Ribeiro', 'A. Sarshar']
year: 1998
journal: "IEEE Transactions on Power Delivery"
tags: ['ccvt', 'emtp', 'ferroresonance', 'transient']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/61.660947.pdf.pdf"]
---

# Digital Time-Domain Investigation of Transient Behavior of Coupling Capacitor Voltage Transformer

**作者**: Iravani, Wang, Polishchuk, Ribeiro, Sarshar
**年份**: 1998
**来源**: `13&14/files/61.660947.pdf.pdf`

## 摘要

本文报告了对TEHMPl61A耦合电容器电压互感器（CCVT）进行的数字时域仿真研究。使用EMTP开发CCVT模型并进行暂态研究，通过对比EMTP仿真结果与试验结果验证了模型精度。研究表明该模型能准确预测CCVT暂态响应（如铁磁谐振现象）。

## 核心贡献


- 构建了含饱和特性、杂散电容及保护装置的CCVT详细EMTP时域模型
- 通过物理试验验证了模型在暂态响应与铁磁谐振预测方面的高精度
- 揭示了杂散电容与负载功率因数等关键参数对CCVT频响特性的影响规律


## 使用的方法


- [[数字时域仿真|数字时域仿真]]
- [[emtp建模|EMTP建模]]
- [[频域灵敏度分析|频域灵敏度分析]]
- [[试验对比验证|试验对比验证]]


## 涉及的模型


- [[ccvt|CCVT]]
- [[降压变压器|降压变压器]]
- [[串联电抗器|串联电抗器]]
- [[mov保护器|MOV保护器]]
- [[二次负载|二次负载]]
- [[杂散电容|杂散电容]]


## 相关主题


- [[铁磁谐振|铁磁谐振]]
- [[暂态响应分析|暂态响应分析]]
- [[继电保护影响评估|继电保护影响评估]]
- [[频率响应特性|频率响应特性]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 主要发现


- 仿真与试验波形高度吻合，模型可精准预测CCVT暂态响应及铁磁谐振
- 泄放线圈电感显著影响600Hz以上频响，负载功率因数对高低频段影响明显
- 系统近端接地故障会在CCVT输出端激发高频振荡，影响保护系统可靠性


