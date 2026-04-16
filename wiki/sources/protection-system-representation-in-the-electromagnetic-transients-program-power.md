---
title: "Protection system representation in the Electromagnetic Transients Program - Power Delivery, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/32/61.296247.pdf.pdf"]
---

# Protection system representation in the Electromagnetic Transients Program - Power Delivery, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `32/61.296247.pdf.pdf`

## 摘要

This paper concerns the addition of the few critical elements of a protection system to the Electromagnetic Transients Program (EMTP), which is one of the most widely used programs for the simulation of transients in power systems. It contains models for almost every major power system component. A protection system consists of instrument transformers, relays, and circuit breakers. Models for current transformers (CTs) and capacitor voltage transformers (CVTs) are developed, validated, and incorporated in the EPRI/DCG EMTP Version 2.0. The user can define the values of the CT and CVT parameters. Total FORTRAN capability has been added to the EMTP; new subroutines and an inbuilt structure to allow the linking of user-defined FORTRAN subroutines with the main EMTP

## 核心贡献


- 开发CT与CVT暂态模型并集成至EMTP，支持用户自定义参数配置
- 引入完整FORTRAN接口，实现用户自定义继电保护算法的闭环集成
- 构建电保系统动态交互框架，支持断路器跳闸与重合闸时序模拟


## 使用的方法


- [[emtp节点导纳矩阵求解|EMTP节点导纳矩阵求解]]
- [[fortran子程序动态链接|FORTRAN子程序动态链接]]
- [[type-96伪非线性磁滞电感建模|Type 96伪非线性磁滞电感建模]]
- [[闭环时序仿真|闭环时序仿真]]


## 涉及的模型


- [[电流互感器-ct|电流互感器(CT)]]
- [[电容式电压互感器-cvt|电容式电压互感器(CVT)]]
- [[距离保护继电器|距离保护继电器]]
- [[变压器差动继电器|变压器差动继电器]]
- [[断路器|断路器]]
- [[输电线路|输电线路]]


## 相关主题


- [[保护系统仿真|保护系统仿真]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[互感器暂态建模|互感器暂态建模]]
- [[继电保护动态交互|继电保护动态交互]]
- [[用户自定义模型集成|用户自定义模型集成]]
- [[闭环仿真|闭环仿真]]


## 主要发现


- 集成互感器模型准确反映磁饱和特性，显著提升继电器输入信号保真度
- FORTRAN接口实现保护算法与电网暂态实时交互，验证闭环控制可行性
- 新框架突破传统开环测试局限，有效支持复杂电网多事件序列暂态保护仿真


