---
title: "Real-time RMS-EMT co-simulation and its application in HIL testing of protective relays"
type: source
authors: ['Renzo', 'Fabián', 'Espinoza']
year: 2021
journal: "Electric Power Systems Research, 197 (2021) 107326. doi:10.1016/j.epsr.2021.107326"
tags: ['real-time', 'cosimulation']
created: "2026-04-13"
sources: ["EMT_Doc/32/j.epsr.2021.107326.pdf.pdf"]
---

# Real-time RMS-EMT co-simulation and its application in HIL testing of protective relays

**作者**: Renzo, Fabián, Espinoza
**年份**: 2021
**来源**: `32/j.epsr.2021.107326.pdf.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Real-time RMS-EMT co-simulation and its application in HIL testing of Renzo Fabi´an Espinoza a,*, Guilherme Justino a, Rodrigo B. Otto a, Rodrigo Ramos b a Itaipu Technological Park Foundation, Foz do Iguaçu, PR, Brazil b S˜ao Carlos School of Engineering, University of Sao Paulo, SP, Brazil

## 核心贡献


- 提出基于内置三相线路模型的实时RMS-EMT多域多速率联合仿真接口技术
- 设计无缓冲快速曲线拟合算法，实现满足实时约束的波形相量高效转换
- 构建OPAL-RT与RTDS跨平台架构，成功应用于继电保护硬件在环测试


## 使用的方法


- [[rms-emt联合仿真|RMS-EMT联合仿真]]
- [[多速率仿真|多速率仿真]]
- [[transmission-line-model|Bergeron线路模型]]
- [[曲线拟合|曲线拟合]]
- [[相量波形转换|相量波形转换]]
- [[诺顿等效|诺顿等效]]
- [[硬件在环|硬件在环]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[继电保护装置|继电保护装置]]
- [[三相耦合线路|三相耦合线路]]
- [[rms相量模型|RMS相量模型]]
- [[emt电磁暂态模型|EMT电磁暂态模型]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[混合仿真|混合仿真]]
- [[硬件在环|硬件在环]]
- [[多域仿真|多域仿真]]
- [[继电保护测试|继电保护测试]]
- [[网络解耦|网络解耦]]


## 主要发现


- 接口技术成功实现微秒级EMT与毫秒级RMS仿真的稳定实时数据交互
- 快速曲线拟合算法有效消除转换延迟，保障多速率联合仿真的数值稳定性
- 实际保护装置硬件在环测试验证了该架构在继电保护测试中的准确性与实用性


