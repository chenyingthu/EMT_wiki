---
title: "Accelerated Electromagnetic Transient (EMT) Equivalent Model of Solid-State Transformer"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Journal of Emerging and Selected Topics in Power Electronics;2022;10;4;10.1109/JESTPE.2021.3094278"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/05/Gao 等 - 2022 - Accelerated Electromagnetic Transient (EMT) Equivalent Model of Solid-State Transformer.pdf"]
---

# Accelerated Electromagnetic Transient (EMT) Equivalent Model of Solid-State Transformer

**作者**: 
**年份**: 2022
**来源**: `05/Gao 等 - 2022 - Accelerated Electromagnetic Transient (EMT) Equivalent Model of Solid-State Transformer.pdf`

## 摘要

—Accurate and efﬁcient electromagnetic transient (EMT) simulation of various types of solid-state transform- ers (SSTs) is extremely time-consuming due to the complex module structure, ﬂexible topology connections, large number of electrical nodes, and simulation time steps limited in the range of microseconds. Therefore, it is urgent to develop the EMT equivalent modeling and fast simulation of SSTs for system-level studies. Taking the modular multilevel converter (MMC)-based SST as an example, this article proposes an accelerated EMT model, which focuses on the equivalence of the dual-active-bridge (DAB)-based high-frequency link (HFL) in the SST. Compared with the existing algorithms, two critical factors of the proposed method that contribute the most to the efﬁciency improvement are t

## 核心贡献


- 提出节点导纳方程预处理与短路导纳参数转换技术，实现高频链路高效等效
- 建立适配多种拓扑连接的多端口参数统一转换框架，避免传统近似引入额外误差
- 构建MMC型固态变压器加速电磁暂态等效模型，消除内部节点并保留端口特性


## 使用的方法


- [[节点导纳方程预处理|节点导纳方程预处理]]
- [[短路导纳参数转换|短路导纳参数转换]]
- [[多端口网络等效|多端口网络等效]]
- [[节点消去法|节点消去法]]


## 涉及的模型


- [[固态变压器-sst|固态变压器(SST)]]
- [[mmc-model|MMC]]
- [[双有源桥-dab|双有源桥(DAB)]]
- [[高频链路-hfl|高频链路(HFL)]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[加速等效建模|加速等效建模]]
- [[系统级仿真|系统级仿真]]
- [[多端口网络等值|多端口网络等值]]


## 主要发现


- 加速模型在PSCAD中验证，仿真速度较详细模型提升一至两个数量级
- 等效模型在保留内部动态信息的同时，未牺牲电压电流波形仿真精度
- 硬件实验验证表明，所提模型能准确复现固态变压器高频链路的暂态响应


