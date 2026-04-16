---
title: "GPU-based power converter transient simulation with matrix exponential integration and memory management"
type: source
authors: ['Wei Wu']
year: 2020
journal: "Electrical Power and Energy Systems, 122 (2020) 106186. doi:10.1016/j.ijepes.2020.106186"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/j.ijepes.2020.106186.pdf.pdf"]
---

# GPU-based power converter transient simulation with matrix exponential integration and memory management

**作者**: Wei Wu
**年份**: 2020
**来源**: `19、20、21/EMT_task_21/j.ijepes.2020.106186.pdf.pdf`

## 摘要

GPU-based power converter transient simulation with matrix exponential Wei Wua, Peng Lia, Xiaopeng Fua,⁎, Zhiying Wanga, Jianzhong Wub, Chengshan Wanga a Key Laboratory of Smart Grid of Ministry of Education, Tianjin University, Tianjin 300072, China b Institute of Energy, School of Engineering, Cardiff University, Cardiff CF24 3AA, UK With the extensive application of power electronic equipment in power systems, electromagnetic transient

## 核心贡献


- 提出基于GPU的并行矩阵指数积分算法，利用细粒度并行加速变流器暂态仿真
- 设计矩阵指数缓存机制，复用开关状态数据，减少CPU与GPU间数据传输
- 提出适配变流器流程的动态内存管理策略，降低显存需求并维持加速优势


## 使用的方法


- [[矩阵指数积分法|矩阵指数积分法]]
- [[gpu并行计算|GPU并行计算]]
- [[状态空间法|状态空间法]]
- [[显式积分|显式积分]]
- [[缓存机制|缓存机制]]


## 涉及的模型


- [[电力电子变流器|电力电子变流器]]
- [[风电场|风电场]]
- [[风力发电机|风力发电机]]
- [[输电线路|输电线路]]
- [[变压器|变压器]]
- [[rlc负荷|RLC负荷]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[gpu加速|GPU加速]]
- [[变流器建模|变流器建模]]
- [[风电场建模|风电场建模]]
- [[内存管理|内存管理]]


## 主要发现


- 多规模风电场测试表明缓存策略命中率高，显著降低显存占用
- 该方法具备L稳定性，避免数值振荡，相比传统方法实现显著加速
- 动态内存管理有效扩展了大规模变流器系统的GPU仿真规模与时长


