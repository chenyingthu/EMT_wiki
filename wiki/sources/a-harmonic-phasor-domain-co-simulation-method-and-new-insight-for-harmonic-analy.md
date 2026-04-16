---
title: "A Harmonic Phasor Domain Co-Simulation Method and New Insight for Harmonic Analysis of Large-scale VSC-MMC based AC/DC Grids"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Electronics; ;PP;99;10.1109/TPEL.2020.3024236"
tags: ['mmc', 'vsc', 'cosimulation', 'harmonic']
created: "2026-04-13"
sources: ["EMT_Doc/01/Shu 等 - 2021 - A Harmonic Phasor Domain Cosimulation Method and New Insight for Harmonic Analysis of Large-Scale VS.pdf"]
---

# A Harmonic Phasor Domain Co-Simulation Method and New Insight for Harmonic Analysis of Large-scale VSC-MMC based AC/DC Grids

**作者**: 
**年份**: 2020
**来源**: `01/Shu 等 - 2021 - A Harmonic Phasor Domain Cosimulation Method and New Insight for Harmonic Analysis of Large-Scale VS.pdf`

## 摘要

—Recently, frequency coupling oscillation events, such as harmonic oscillations, sub- and super-synchronous oscillations (S2SO), driven by multiple converters with different switching frequencies have brought new challenges of AC/DC grid mod- eling, despite the traditional one of improving the accuracy and efﬁciency. There is an urgent requirement of practical engineering projects to produce a modeling method that can produce instantaneous and harmonic phasor waveforms simul- taneously, dedicated to harmonic interaction analysis of large- scale ac/dc grids. To realize the above-mentioned targets, the harmonic phasor domain (HPD) modeling of power electronic based dc grids is proposed. The HPD modeling is then combined and coordinated with EMT based ac-grid models based on the proposed HPD 

## 核心贡献


- 提出谐波相量域建模方法，同步输出瞬时波形与谐波相量波形
- 构建HPD输电线路接口模型，实现EMT交流网与HPD直流网协同仿真
- 建立基于节点分析的大信号动态模型，系统方程维数不随谐波阶数扩展


## 使用的方法


- [[谐波相量法|谐波相量法]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[协同仿真|协同仿真]]
- [[节点分析法|节点分析法]]
- [[解耦时序协调|解耦时序协调]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[mmc-model|MMC]]
- [[交流电网|交流电网]]
- [[直流电网|直流电网]]
- [[输电线路|输电线路]]


## 相关主题


- [[谐波分析|谐波分析]]
- [[交直流电网|交直流电网]]
- [[vsc-model|VSC]]
- [[宽频带振荡|宽频带振荡]]
- [[大规模电网建模|大规模电网建模]]


## 主要发现


- HPD模型将仿真步长扩展至500微秒，同时保持瞬时与谐波波形的高精度
- 在中国实际大规模VSC-MMC交直流电网中验证了方法的高效性与准确性
- 谐波相量波形可精确包络瞬时谐波值，有效追踪故障后大信号动态过程


