---
title: "Fine-grained hardware resource optimization and design for FPGA-based real-time simulation of large-scale renewable energy generations"
type: source
authors: ['Yanfei Li']
year: 2025
journal: "International Journal of Electrical Power and Energy Systems, 169 (2025) 110754. doi:10.1016/j.ijepes.2025.110754"
tags: ['real-time', 'fpga', 'renewable']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/Li 等 - 2025 - Fine-grained hardware resource optimization and design for FPGA-based real-time simulation of large-.pdf"]
---

# Fine-grained hardware resource optimization and design for FPGA-based real-time simulation of large-scale renewable energy generations

**作者**: Yanfei Li
**年份**: 2025
**来源**: `19、20、21/EMT_task_19/Li 等 - 2025 - Fine-grained hardware resource optimization and design for FPGA-based real-time simulation of large-.pdf`

## 摘要

Fine-grained hardware resource optimization and design for FPGA-based real-time simulation of large-scale renewable energy generations a Key Laboratory of Smart Grid of Ministry of Education, Tianjin University, Tianjin 300072, China b China Southern Power Grid Electric Power Research Institute, Guangzhou 510663, China Real-time simulation of renewable energy generations (REGs) is essential for the development and testing of

## 核心贡献


- 提出面向FPGA的细粒度硬件资源优化方法，实现新能源控制系统实时仿真
- 建立算术运算级资源需求模型，综合优化最小求解时间与硬件资源约束
- 提出自动硬件描述语言生成技术，快速构建控制系统求解的功能硬件模块


## 使用的方法


- [[fpga时空并行计算|FPGA时空并行计算]]
- [[算术运算级资源调度|算术运算级资源调度]]
- [[自动hdl代码生成|自动HDL代码生成]]
- [[细粒度硬件资源优化|细粒度硬件资源优化]]


## 涉及的模型


- [[光伏阵列-pv|光伏阵列(PV)]]
- [[风力发电机-wt|风力发电机(WT)]]
- [[并网变流器|并网变流器]]
- [[控制系统详细模型|控制系统详细模型]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[fpga硬件加速|FPGA硬件加速]]
- [[硬件资源优化|硬件资源优化]]
- [[自动代码生成|自动代码生成]]
- [[大规模新能源并网|大规模新能源并网]]


## 主要发现


- 单FPGA实现15台光伏与风机系统实时仿真，步长分别达9μs与10μs
- 相比传统设计硬件资源占用降低约30%，显著提升FPGA并行计算效率
- 仿真结果与PSCAD对比相对误差小于0.5%，验证了模型的高精度


