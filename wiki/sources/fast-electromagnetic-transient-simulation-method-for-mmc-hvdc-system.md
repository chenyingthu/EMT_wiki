---
title: "Fast electromagnetic transient simulation method for MMC-HVDC system"
type: source
authors: ['CNKI']
year: 2023
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/18/Gao 等 - 2014 - Fast electromagnetic transient simulation method for PWM converters based on averaging theory. Part.pdf"]
---

# Fast electromagnetic transient simulation method for MMC-HVDC system

**作者**: CNKI
**年份**: 2023
**来源**: `18/Gao 等 - 2014 - Fast electromagnetic transient simulation method for PWM converters based on averaging theory. Part.pdf`

## 摘要

２．Ｓｃｈｏｏｌ　ｏｆ　Ｅｌｅｃｔｒｉｃａｌ　Ｅｎｇｉｎｅｅｒｉｎｇ　ａｎｄ　Ｃｏｍｐｕｔｅｒ　Ｓｃｉｅｎｃｅ，Ｗａｓｈｉｎｇｔｏｎ　Ｓｔａｔｅ　Ｕｎｉｖｅｒｓｉｔｙ，Ｐｕｌｌｍａｎ　ＷＡ　９９１６３，美国）

## 核心贡献


- 提出适用于GPU的电磁暂态细粒度并行算法，将开关处理转化为周期迭代求解
- 设计基于SIMD与共享内存的运算级并行策略，实现节点方程与控制系统高效求解
- 实现改进EMTP算法的GPU向量化与线程通信优化，突破传统粗粒度并行瓶颈


## 使用的方法


- [[细粒度并行算法|细粒度并行算法]]
- [[simd向量化|SIMD向量化]]
- [[共享内存并行|共享内存并行]]
- [[改进emtp算法|改进EMTP算法]]
- [[节点分析法|节点分析法]]
- [[开关时刻预测校正|开关时刻预测校正]]


## 涉及的模型


- [[pwm变流器|PWM变流器]]
- [[三相ac-dc变流器|三相AC/DC变流器]]
- [[直流电容|直流电容]]
- [[滤波电感|滤波电感]]
- [[vq控制系统|VQ控制系统]]


## 相关主题


- [[gpu并行计算|GPU并行计算]]
- [[快速电磁暂态仿真|快速电磁暂态仿真]]
- [[细粒度并行|细粒度并行]]
- [[大规模系统仿真|大规模系统仿真]]
- [[开关过程处理|开关过程处理]]


## 主要发现


- 仿真波形与PSCAD及CPU串行程序高度吻合，验证了算法正确性
- 变流器规模达90个时GPU加速比达6.74倍，系统规模越大并行效率越高
- 电气与控制系统仿真耗时随规模增加显著降低，突破传统CPU串行计算瓶颈


