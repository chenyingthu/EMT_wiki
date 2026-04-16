---
title: "Modulation Index Dependent Thévenin Equivalent Circuit Model of VSC and APDR"
type: source
authors: ['未知']
year: 2015
journal: "IEEE Transactions on Power Delivery"
tags: ['vsc', 'emt']
created: "2026-04-13"
sources: ["EMT_Doc/37/TPWRD.2015.2465812.pdf.pdf"]
---

# Modulation Index Dependent Thévenin Equivalent Circuit Model of VSC and APDR

**作者**: 未知
**年份**: 2015
**来源**: `37/TPWRD.2015.2465812.pdf.pdf`

## 摘要

The paper presents a simple modulation index dependent thévenin equivalent circuit model of the voltage source converters (VSC) and the associated anti-parallel diode rectifier (APDR).

## 核心贡献


- 提出依赖调制指数的VSC与反并联二极管整流器戴维南等效电路模型
- 利用正交变换与变压器类比法，将交流侧阻抗等效折算至直流侧
- 构建换流器闭锁时反并联二极管三相整流器的开关等效表示方法


## 使用的方法


- [[正交变换|正交变换]]
- [[变压器类比法|变压器类比法]]
- [[平均值模型|平均值模型]]
- [[开关模型|开关模型]]
- [[戴维南等效推导|戴维南等效推导]]
- [[观测器设计|观测器设计]]
- [[atp-emtp时域仿真|ATP-EMTP时域仿真]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[反并联二极管整流器-apdr|反并联二极管整流器(APDR)]]
- [[两电平换流器|两电平换流器]]
- [[多端直流系统-mtdc|多端直流系统(MTDC)]]
- [[直流输电线路|直流输电线路]]


## 相关主题


- [[直流故障研究|直流故障研究]]
- [[vsc-model|VSC]]
- [[网络等值|网络等值]]
- [[直流保护|直流保护]]
- [[仿真加速|仿真加速]]
- [[暂态分析|暂态分析]]


## 主要发现


- 该模型对极间故障电流预测高度精确，但对极地故障电流存在轻微低估
- 整流器等效模型引入电源电感后，显著提升了暂态区域的仿真精度
- 在5微秒步长下仿真提速3倍，750微秒步长下提速126倍且保持精度


