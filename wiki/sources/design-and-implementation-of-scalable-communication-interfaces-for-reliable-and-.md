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



## 方法细节

### 方法概述

本文设计了一套面向高比例逆变器资源(IBR)电力系统实时协同仿真的可扩展通信接口架构，涵盖本地局域网(LAN)与远程互联网两种场景。本地接口采用Modbus协议与TCP/IP套接字结合，通过Python多线程实现RTS与能量管理系统(MCS)间的双向低延迟数据交互，并利用一阶低通滤波(LPF)结合延迟补偿实现EMT(100μs)与相量域(1ms)模型的无缝同步。远程接口提供基于云存储的文件共享(适用于分钟级非实时控制)与基于VPN的TCP/IP直连(适用于毫秒级实时控制)两种模式。针对远程协同中因数据分辨率不匹配(如10ms输电网与100μs配电网)引发的IBR锁相环(PLL)失稳问题，提出了一种实时数据外推算法。该算法通过历史数据平均变化率与外推误差反馈动态预测下一时刻状态，替代传统LPF以消除相位延迟与幅值误差，显著提升跨域交互的稳定性与仿真精度。

### 数学公式


**公式1**: $$$x_{ext}(t) = x_{ext}(t-1) + \Delta_{avg} + \Delta_{err}$$$

*外推值更新方程，用于计算当前时刻t的预测数据，结合历史平均变化率与误差补偿项*


**公式2**: $$$\Delta_{avg} = \frac{1}{n} \sum_{i=1}^{n} [x_{act}(t-i) - x_{act}(t-i-1)]$$$

*历史数据平均变化率计算，基于过去n个实际采样点的差分均值反映数据趋势*


**公式3**: $$$\Delta_{err} = \alpha \cdot [x_{act}(t-n) - x_{ext}(t-n)]$$$

*外推误差增量补偿，利用调节系数α对上一周期外推值与实际值的偏差进行反馈修正*


### 算法步骤

1. 初始化通信链路：配置TCP/IP地址与端口，建立RTS(Modbus Server)、本地接口(Client)与MCS(TCP/IP Server)的三方连接，同步全局仿真时钟并清空数据库缓存。

2. 数据采集与时间戳标记：接口按预设轮询频率通过Modbus协议从RTS采集带时间戳的测量数据，写入本地关系型数据库，并记录系统内部传播延迟(td1)。

3. 多线程并发传输：利用Python多线程技术，上游线程将测量数据通过TCP/IP套接字非阻塞发送至MCS，下游线程同步接收MCS下发的控制指令，避免数据阻塞与指令丢失。

4. 指令执行与日志记录：接收到的控制指令经时间戳对齐后转发至RTS执行，所有交互数据均持久化存储以保证可追溯性，并计算端到端通信延迟(td2)。

5. 实时外推处理(远程场景)：当检测到跨域分辨率不匹配时，接口截取过去n个实际数据点计算平均变化率Δ_avg，结合上一周期外推误差计算补偿项Δ_err，按公式(1)生成平滑的外推序列，直接输入EMT模型替代原始粗分辨率数据或LPF滤波数据。


### 关键参数

- **EMT仿真步长**: 100 μs

- **相量域仿真步长**: 1 ms

- **输电网数据更新分辨率**: 10 ms

- **低通滤波时间常数**: 0.01

- **外推历史窗口n**: 1

- **误差调节系数α**: 0.001

- **文件共享同步延迟范围**: 1.5 ~ 4 秒(典型)

- **VPN通信延迟**: 约 20 ms



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 本地局域网接口精度与稳定性测试 | 在微电网测试床中按100秒间隔顺序投入5组配电负荷，接口以1秒采样率记录数据并与OPAL-RT 1ms高分辨率基准对比。PCC电压、频率与功率响应高度吻合，基于SOC的控制策略连续运行20天无中断。 | 通信延迟在分钟级控制周期内可忽略不计，数据保真度满足实时控制要求，长周期运行稳定性达100% |

| 远程文件共享协同测试 | 两地OPAL-RT运行IEEE 123节点系统，通过Google Drive每60秒同步约500个测量点(单点4KB)。远程系统持续监控文件时间戳更新负荷参考值。 | 数据同步延迟分布在1~8.5秒之间，典型延迟为1.5~4秒，适用于更新间隔远大于延迟的非实时能量管理场景 |

| VPN跨域T&D协同与故障穿越测试 | IEEE 118节点输电网(10ms)与IEEE 123节点配电网(EMT 100μs)通过VPN互联。在Bus 94施加5周期三相接地故障，PCC电压数据接收延迟37~55ms，接收端数据更新间隔17~35ms。未处理时PLL频率出现剧烈振荡。 | 引入外推算法后，PLL频率振荡完全消除，电压幅值误差显著低于LPF滤波(τ=0.01)，系统恢复稳定同步，外推曲线平滑度提升且无相位滞后 |



## 量化发现

- 本地接口在分钟级控制周期下通信与处理延迟可忽略，支持长达20天的连续稳定运行
- 远程文件共享同步延迟典型值为1.5~4秒，最大可达8.5秒，适用于数据交换间隔远大于延迟的场景
- VPN直连通信接口间延迟约为20毫秒，显著低于文件共享方式，满足实时控制需求
- T&D协同中PCC电压数据跨域传输产生37~55毫秒的传播延迟，接收端数据更新间隔为17~35毫秒
- 传统LPF(时间常数0.01)在分辨率不匹配时引入显著相位延迟与电压幅值误差，导致IBR失稳
- 实时外推算法(参数n=1, α=0.001)有效消除PLL频率尖峰与振荡，外推曲线平滑度与精度均优于LPF


## 关键公式

### 实时数据外推更新方程

$$$x_{ext}(t) = x_{ext}(t-1) + \Delta_{avg} + \Delta_{err}$$$

*用于远程VPN协同仿真中，当输电网(10ms)与配电网EMT(100μs)存在分辨率不匹配时，替代低通滤波以预测下一时刻状态，消除延迟并维持IBR锁相环稳定*



## 验证详情

- **验证方式**: 实时硬件在环(HIL)仿真与跨地域协同测试
- **测试系统**: 微电网测试床(3MW光伏+2MWh储能+1MVA柴油发电机+IEEE 123节点配电网)及输配电网协同系统(IEEE 118节点输电网+IEEE 123节点配电网)
- **仿真工具**: OPAL-RT实时仿真器、eMEGASIM(EMT求解器)、ePHASORSIM(相量域求解器)、Python(通信接口开发)、Google Drive(文件共享)、VPN网络
- **验证结果**: 验证了本地与远程通信接口在不同延迟与分辨率条件下的有效性。本地接口实现高精度数据交互与20天长周期稳定运行；远程文件共享适用于分钟级调度；VPN接口结合实时外推算法成功解决跨域分辨率失配问题，消除PLL振荡，显著提升高比例IBR协同仿真的可靠性与数值稳定性。
