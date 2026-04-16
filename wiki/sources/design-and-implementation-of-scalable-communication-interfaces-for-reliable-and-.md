---
title: "Design and Implementation of Scalable Communication Interfaces for Reliable and Stable Real-time Co-Simulation of Power Systems"
type: source
authors: ['未知']
year: 2025
journal: "2025 IEEE Power &amp; Energy Society General Meeting (PESGM);2025; ; ;10.1109/PESGM52009.2025.11225688"
tags: ['real-time', 'cosimulation']
created: "2026-04-13"
sources: ["EMT_Doc/12/Design_and_Implementation_of_Scalable_Communication_Interfaces_for_Reliable_and_Stable_Real-time_Co-Simulation_of_Power_Systems.pdf"]
---

# Design and Implementation of Scalable Communication Interfaces for Reliable and Stable Real-time Co-Simulation of Power Systems

**作者**: 
**年份**: 2025
**来源**: `12/Design_and_Implementation_of_Scalable_Communication_Interfaces_for_Reliable_and_Stable_Real-time_Co-Simulation_of_Power_Systems.pdf`

## 摘要

—Co-simulation offers an integrated approach for modeling the large-scale integration of inverter-based resources (IBRs) into transmission and distribution grids. This paper presents a scalable communication interface design and implementation to enable reliable and stable real-time co-simulation of power systems with high IBR penetration. The communication interface is categorized into two types: local and remote. In local scenarios, where subsystems are connected within a single local area network (LAN), low-latency communication facilitates the seamless integration of electromagnetic transient (EMT) and phasor-domain models, enabling efficient interactions with power and energy management algorithms. For remote scenarios, data exchange is achieved via internet-based file sharing or VPN-

## 核心贡献


- 设计可扩展的本地与远程通信接口支持低延迟局域网与互联网数据交换
- 提出实时数据外推方法有效缓解协同仿真中数据分辨率不匹配引发的失稳问题
- 构建EMT与相量域混合仿真同步机制采用低通滤波与延迟补偿实现跨域交互


## 使用的方法


- [[协同仿真|协同仿真]]
- [[实时数据外推|实时数据外推]]
- [[一阶低通滤波|一阶低通滤波]]
- [[延迟补偿|延迟补偿]]
- [[tcp-ip套接字通信|TCP/IP套接字通信]]
- [[modbus协议|Modbus协议]]
- [[多线程并发处理|多线程并发处理]]


## 涉及的模型


- [[ibr|IBR]]
- [[光伏电站|光伏电站]]
- [[电池储能系统|电池储能系统]]
- [[柴油发电机|柴油发电机]]
- [[ieee-123节点配电网|IEEE 123节点配电网]]
- [[微电网控制系统|微电网控制系统]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[协同仿真|协同仿真]]
- [[混合仿真|混合仿真]]
- [[通信接口设计|通信接口设计]]
- [[逆变器资源接入|逆变器资源接入]]
- [[延迟管理|延迟管理]]
- [[输配电网协同|输配电网协同]]


## 主要发现


- 局域网通信延迟仅毫秒级对分钟级能量管理系统控制周期无显著影响
- 数据分辨率不匹配会导致逆变器失稳所提外推方法可显著提升系统稳定性
- 基于OPAL-RT验证了接口可扩展性实现高比例IBR微电网稳定实时协同仿真


