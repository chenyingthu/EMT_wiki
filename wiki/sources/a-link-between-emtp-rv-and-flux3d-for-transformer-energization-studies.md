---
title: "A link between EMTP-RV and FLUX3D for transformer energization studies"
type: source
year: 2009
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/02/Dennetière 等 - 2009 - A link between EMTP-RV and FLUX3D for transformer energization studies.pdf"]
---

# A link between EMTP-RV and FLUX3D for transformer energization studies

**年份**: 2009
**来源**: `02/Dennetière 等 - 2009 - A link between EMTP-RV and FLUX3D for transformer energization studies.pdf`

## 摘要

A link between EMTP-RV and FLUX3D for transformer energization studies S. Dennetière a,∗, Y. Guillot a,1, J. Mahseredjian b,2, M. Rioual a,3 a EDF R&D, 1 avenue du Général De Gaulle, BP 408, 92141 Clamart Cédex, France b École Polytechnique de Montréal, C.P. 6079 succ. Centre-ville, Montréal, Québec, Canada H3C 3A7 This paper presents a programmed link between the electromagnetic transients program EMTP-RV and

## 核心贡献


- 开发基于DLL的接口实现EMTP-RV电路求解与FLUX3D三维有限元磁场求解的耦合
- 提出动态切换建模策略有效处理断路器非同期合闸及开路相感应电压对暂态的影响
- 实现电压电流磁通及机械力等多物理量跨步长交互兼顾计算效率与数值稳定性


## 使用的方法


- [[有限元法-fem|有限元法(FEM)]]
- [[电路-磁场耦合|电路-磁场耦合]]
- [[动态链接库-dll-接口|动态链接库(DLL)接口]]
- [[牛顿-拉夫逊迭代法|牛顿-拉夫逊迭代法]]
- [[单步延迟耦合技术|单步延迟耦合技术]]
- [[受控源等效建模|受控源等效建模]]


## 涉及的模型


- [[三相电力变压器|三相电力变压器]]
- [[铁芯|铁芯]]
- [[绕组|绕组]]
- [[rl阻抗|RL阻抗]]
- [[戴维南等效电路|戴维南等效电路]]
- [[三维有限元变压器模型|三维有限元变压器模型]]


## 相关主题


- [[变压器空载合闸|变压器空载合闸]]
- [[开关暂态|开关暂态]]
- [[铁磁饱和|铁磁饱和]]
- [[混合仿真|混合仿真]]
- [[铁芯详细建模|铁芯详细建模]]
- [[励磁涌流|励磁涌流]]
- [[机电应力分析|机电应力分析]]


## 主要发现


- 耦合接口计算的励磁涌流波形与独立FLUX3D结果高度吻合验证了数值精度
- 引入单步时间延迟在保证数值稳定的同时大幅降低了联合求解的计算负担
- 动态切换模型能准确捕捉非同期合闸时断路器开路相的感应过电压现象


