---
title: "An Enhanced Average Value Model of Modular Multilevel Converter for Accurate Representation of Converter Blocking Operation"
type: source
authors: ['Periodicals']
year: 2018
journal: "978-1-7281-1981-6/19/$31.00 ©2019 IEEE"
tags: ['harmonic']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An Enhanced Average Value Model of Modular Multilevel Converter for Accurate Representation of Converter Blocking Operation.pdf"]
---

# An Enhanced Average Value Model of Modular Multilevel Converter for Accurate Representation of Converter Blocking Operation

**作者**: Periodicals
**年份**: 2018
**来源**: `07&08/An Enhanced Average Value Model of Modular Multilevel Converter for Accurate Representation of Converter Blocking Operation.pdf`

## 摘要

—Modular Multilevel Converter (MMC) has demonstrated significant advantage in harmonic elimination and improved converter efficiency due to the use of large number of submodules and low switching frequency of the submodules. However, the massive switching events of the Insulated-Gate Bipolar Transistors (IGBTs) in the MMC have also introduced high computational burden when modelling the MMC in electromagnetic transient tools. Various research efforts have dedicated to developing the numerically efficient average value models (AVMs) for the MMC. This paper gives an overview of the existing control signal based AVMs of the MMC and proposes an enhanced average value model with arm current initialization

## 核心贡献


- 提出增强型MMC平均值模型，利用桥臂电流初始化补偿闭锁瞬间初始条件缺失。
- 在闭锁模块引入受控电流源初始化电感电流，消除传统模型交直流侧电流不连续现象。


## 使用的方法


- [[平均值模型|平均值模型]]
- [[控制信号建模|控制信号建模]]
- [[戴维南等效电路|戴维南等效电路]]
- [[桥臂电流初始化|桥臂电流初始化]]
- [[闭锁模块建模|闭锁模块建模]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[半桥子模块|半桥子模块]]
- [[mmc-model|MMC]]
- [[igbt与续流二极管|IGBT与续流二极管]]
- [[桥臂电感与电阻|桥臂电感与电阻]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[mmc-model|MMC]]
- [[换流器闭锁工况|换流器闭锁工况]]
- [[实时仿真|实时仿真]]
- [[电力电子等效建模|电力电子等效建模]]


## 主要发现


- 在Simulink平台验证，闭锁工况下电气量波形与详细开关模型高度吻合。
- 有效消除了正常运行至闭锁模式切换时的直流电流不连续现象，提升了暂态仿真精度。
- 相比传统平均值模型，新模型在保持高计算效率的同时显著提高了闭锁过程建模精度。


