---
title: "An Iterative Real-Time Nonlinear Electromagnetic Transient Solver on FPGA"
type: source
authors: ['未知']
year: 2011
journal: "IEEE Transactions on Industrial Electronics;2011;58;6;10.1109/TIE.2010.2060461"
tags: ['real-time', 'fpga']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/Chen and Dinavahi - 2011 - An iterative real-time nonlinear electromagnetic transient solver on FPGA.pdf"]
---

# An Iterative Real-Time Nonlinear Electromagnetic Transient Solver on FPGA

**作者**: 
**年份**: 2011
**来源**: `07&08/Chen and Dinavahi - 2011 - An iterative real-time nonlinear electromagnetic transient solver on FPGA.pdf`

## 摘要

—A real-time transient simulation of nonlinear ele- ments in transmission networks requires signiﬁcant computational power. This paper proposes an iterative nonlinear transient solver on a ﬁeld-programmable gate array. The parallel solver, based on the compensation method and the Newton–Raphson algo- rithm (continuous and piecewise), is entirely implemented in Very high speed integrated circuit Hardware Description Language. It also involves sparsity techniques, deeply pipelined arithmetic ﬂoating-point processing, and parallel Gauss–Jordan elimination. To validate the new solver, two case studies are simulated in real time: surge arrester transients in a series-compensated line and ferroresonance transients in a transformer, with time steps of 5 and 3 μs, respectively. The captured real-t

## 核心贡献


- 提出基于FPGA的迭代非线性暂态求解器，实现补偿法与牛顿拉夫逊算法硬件并行化
- 设计深度流水线浮点运算与并行高斯约当消元架构，突破实时非线性迭代计算瓶颈
- 完整VHDL实现连续与分段牛顿法，结合稀疏矩阵技术，显著提升求解速度与精度


## 使用的方法


- [[补偿法|补偿法]]
- [[牛顿-拉夫逊算法|牛顿-拉夫逊算法]]
- [[连续牛顿法|连续牛顿法]]
- [[分段牛顿法|分段牛顿法]]
- [[稀疏矩阵技术|稀疏矩阵技术]]
- [[深度流水线浮点运算|深度流水线浮点运算]]
- [[并行高斯-约当消元法|并行高斯-约当消元法]]


## 涉及的模型


- [[避雷器|避雷器]]
- [[串联补偿线路|串联补偿线路]]
- [[变压器|变压器]]
- [[铁磁谐振模型|铁磁谐振模型]]
- [[线性多端口网络|线性多端口网络]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[fpga硬件加速|FPGA硬件加速]]
- [[并行计算|并行计算]]
- [[非线性网络求解|非线性网络求解]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 主要发现


- 避雷器暂态与变压器铁磁谐振仿真分别实现5μs与3μs步长，满足硬实时要求
- 示波器实测波形与ATP离线仿真高度吻合，验证了求解器的高精度与快速收敛性
- 并行架构有效克服传统处理器迭代计算瓶颈，实现非线性元件实时精确仿真


