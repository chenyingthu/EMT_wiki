---
title: "A Universal Blocking-Module-Based Average Value Model of Modular Multilevel Converters with Different Types of Submodules"
type: source
authors: ['未知']
year: 2019
journal: "IEEE Transactions on Energy Conversion; ;PP;99;10.1109/TEC.2019.2944332"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/04/tec.2019.2944332.pdf.pdf"]
---

# A Universal Blocking-Module-Based Average Value Model of Modular Multilevel Converters with Different Types of Submodules

**作者**: 
**年份**: 2019
**来源**: `04/tec.2019.2944332.pdf.pdf`

## 摘要

—The large amount of power electronic submodules and semiconductor switching events in the Modular Multilevel Converter (MMC) introduces several challenges for efficient and accurate Electro-Magnetic Transient (EMT) simulation. Research efforts have focused on developing Average Value Models (AVMs) of MMC that enable fast and accurate dynamic simulation of the converter. This paper proposes a universal blocking-module-based AVM, which can simulate the MMC of different submodule types and provide accurate results for the MMC operating in both blocking and de-blocking modes. An analytical approach is included in the model to calculate the semiconductor losses of different submodule types in the MMC.

## 核心贡献


- 提出通用阻塞模块平均值模型，兼容半桥全桥及混合桥子模块的MMC仿真
- 采用受控源等效桥臂电容电压与电感初始电流，精确模拟阻塞模式动态
- 建立解析型半导体损耗计算模型，涵盖通态电阻饱和压降及开关损耗


## 使用的方法


- [[平均值模型|平均值模型]]
- [[阻塞模块法|阻塞模块法]]
- [[戴维南等效|戴维南等效]]
- [[开关函数法|开关函数法]]
- [[解析损耗计算|解析损耗计算]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[半桥子模块|半桥子模块]]
- [[全桥子模块|全桥子模块]]
- [[混合桥子模块|混合桥子模块]]
- [[mmc-model|MMC]]
- [[详细等效模型|详细等效模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[vsc-model|VSC]]
- [[多电平换流器|多电平换流器]]
- [[直流极间故障|直流极间故障]]
- [[阻塞与解锁运行|阻塞与解锁运行]]
- [[半导体损耗建模|半导体损耗建模]]


## 主要发现


- 在41电平双端MMC-HVDC系统中验证，阻塞与解锁模式下精度与效率均优
- 相比传统平均值模型，该模型在直流极间故障下能准确复现桥臂动态响应
- 解析损耗模型可精确计算不同子模块的通态与开关损耗，误差显著降低


