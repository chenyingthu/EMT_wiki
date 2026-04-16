---
title: "Independent power producer parallel operation modeling in transient network analysis"
type: source
authors: ['未知']
year: 2009
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/23/Moura 等 - 2010 - Independent power producer parallel operation modeling in transient network simulations for intercon.pdf"]
---

# Independent power producer parallel operation modeling in transient network analysis

**作者**: 
**年份**: 2009
**来源**: `23/Moura 等 - 2010 - Independent power producer parallel operation modeling in transient network simulations for intercon.pdf`

## 摘要

Independent power producer parallel operation modeling in transient network simulations for interconnected distributed generation studies Fabrício A.M. Moura a, José R. Camacho a,∗,1, Marcelo L.R. Chaves b, Geraldo C. Guimarães b a Universidade Federal de Uberlândia, School of Electrical Engineering, Rural Electricity and Alternative Sources Lab, PO Box 593, 38400.902 Uberlândia, MG, Brazil b Universidade Federal de Uberlândia, School of Electrical Engineering, Power Systems Dynamics Group, PO B

## 核心贡献


- 利用TACS模块实现S域传递函数离散化，构建含调速器与励磁的同步机完整暂态模型
- 采用IEEE Type I电压调节器替代简化模型，显著提升分布式电源并网暂态仿真精度
- 建立含公共耦合点等效电源与内部负荷的独立发电商并网配电网电磁暂态仿真框架


## 使用的方法


- [[tacs控制建模|TACS控制建模]]
- [[s域传递函数离散化|S域传递函数离散化]]
- [[atp-emtp电磁暂态仿真|ATP-EMTP电磁暂态仿真]]
- [[潮流初始化|潮流初始化]]


## 涉及的模型


- [[同步发电机|同步发电机]]
- [[ieee-type-i电压调节器|IEEE Type I电压调节器]]
- [[汽轮机调速器|汽轮机调速器]]
- [[配电网等效模型|配电网等效模型]]
- [[理想三相电源|理想三相电源]]


## 相关主题


- [[分布式发电并网|分布式发电并网]]
- [[独立发电商建模|独立发电商建模]]
- [[暂态网络分析|暂态网络分析]]
- [[甩负荷暂态分析|甩负荷暂态分析]]
- [[电压与频率稳定性|电压与频率稳定性]]


## 主要发现


- 甩负荷后耦合点电压升至1.08pu并稳态于1.06pu，超出标准限值，需加装电抗器抑制
- 采用详细电压调节器模型显著抑制暂态振荡，验证精细控制模型对提升并网稳定性的作用
- 调速器死区使转速波动维持在60Hz附近，频率保护未动作，系统依靠惯性快速恢复同步


