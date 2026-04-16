---
title: "Comprehensive Full-Scale Converter Wind Park Initialization for Electromagnetic Transient Studies"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Power Delivery;2025;40;3;10.1109/TPWRD.2025.3551546"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/11/Comprehensive_Full-Scale_Converter_Wind_Park_Initialization_for_Electromagnetic_Transient_Studies.pdf"]
---

# Comprehensive Full-Scale Converter Wind Park Initialization for Electromagnetic Transient Studies

**作者**: 
**年份**: 2025
**来源**: `11/Comprehensive_Full-Scale_Converter_Wind_Park_Initialization_for_Electromagnetic_Transient_Studies.pdf`

## 摘要

—This paper proposes a comprehensive method for initializing the electromagnetic transient models of full-scale con- verter wind parks. The method uses the ac load-ﬂow solution to initialize the mechanical model, the electrical components, the machine, the converter and the control systems. The effectiveness of the method is demonstrated through EMT simulations of three different power system benchmarks: an aggregated WP connected to a small transmission grid, a detailed WP model with wind turbines connected to a small transmission grid, and a large-scale transmission grid with ten different aggregated WPs. The results show that the proposed method reduces computing times required to reach steady-state and consequently accelerates overall simula- tions. Index Terms—Initialization, full-siz

## 核心贡献


- 提出全控制初始化方法，基于潮流解同步初始化风机机械、电气、变流器及控制系统
- 采用反向传播技术初始化控制器，无需访问电机内部变量，显著提升模型通用性
- 设计变流器与永磁同步电机专用初始化算法，消除传统方法需长时间暂态过渡的缺陷


## 使用的方法


- [[交流潮流计算|交流潮流计算]]
- [[反向传播法|反向传播法]]
- [[平均值模型|平均值模型]]
- [[矢量控制|矢量控制]]
- [[时域仿真|时域仿真]]


## 涉及的模型


- [[全功率变流器风电场|全功率变流器风电场]]
- [[永磁同步电机|永磁同步电机]]
- [[机侧变流器|机侧变流器]]
- [[网侧变流器|网侧变流器]]
- [[集电网络|集电网络]]
- [[风电场控制器|风电场控制器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[风电场建模|风电场建模]]
- [[稳态初始化|稳态初始化]]
- [[控制系统初始化|控制系统初始化]]
- [[大规模电力系统|大规模电力系统]]


## 主要发现


- 在三种不同规模测试系统中验证，该方法显著缩短达到稳态所需的计算时间
- 相比传统LFSI方法，新初始化策略有效避免保护误动与持续振荡，提升仿真效率
- 无需访问电机内部变量即可完成全系统初始化，兼容主流商业电磁暂态仿真软件


