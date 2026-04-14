---
title: "基于RTDS和FPGA联合仿真平台的多速率实时仿真方法"
type: source
authors: ['作者']
year: 2016
journal: "科目"
tags: ['real-time', 'fpga', 'cosimulation', 'rtds']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multi-rate real-time simulation method based on RTDS and FPGA Co-simulation platform.pdf"]
---

# 基于RTDS和FPGA联合仿真平台的多速率实时仿真方法

**作者**: 作者
**年份**: 2016
**来源**: `27&28/Multi-rate real-time simulation method based on RTDS and FPGA Co-simulation platform.pdf`

## 摘要

*（摘要未提取到）*

## 核心贡献

- 提出了一种基于RTDS与FPGA联合仿真平台的多速率实时仿真方法
- 设计了FPGA数据发送适当早于RTDS的接口电气量异步交互方法以减小通信延时影响
- 通过50μs/1μs混合步长仿真含光伏的IEEE 5节点系统并与PSCAD对比，验证了平台可行性与方法准确性

## 使用的方法

- [[局部延迟插入方法-lim|局部延迟插入方法(LIM)]]
- [[拟合法与外插法|拟合法与外插法]]
- [[接口电气量异步交互方法|接口电气量异步交互方法]]
- [[并行多速率仿真算法|并行多速率仿真算法]]

## 涉及的模型

- [[rtds实时数字仿真器|RTDS实时数字仿真器]]
- [[fpga现场可编程门阵列|FPGA现场可编程门阵列]]
- [[ieee-5节点电力系统|IEEE 5节点电力系统]]
- [[光伏发电系统|光伏发电系统]]

## 相关主题

- [[电磁暂态仿真|电磁暂态仿真]]
- [[实时仿真|实时仿真]]
- [[多速率仿真|多速率仿真]]
- [[分布式电源并网|分布式电源并网]]
- [[联合仿真|联合仿真]]
- [[通信延迟补偿|通信延迟补偿]]

## 主要发现

- RTDS与FPGA联合平台能够有效实现含分布式电源电力系统的实时仿真
- FPGA提前发送数据的异步交互策略显著降低了通信延时对仿真精度的负面影响
- 50μs/1μs混合步长下的仿真结果与PSCAD数据高度吻合，证明了所提多速率方法的准确性与实时性
