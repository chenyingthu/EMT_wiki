---
title: "Fast electromagnetic transient simulation of modular multilevel converter based on semi-implicit delay model"
type: source
authors: ['CNKI']
year: 2023
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/18/Fan 等 - 2017 - Fast electromagnetic transient simulation for flexible DC Power Grid.pdf"]
---

# Fast electromagnetic transient simulation of modular multilevel converter based on semi-implicit delay model

**作者**: CNKI
**年份**: 2023
**来源**: `18/Fan 等 - 2017 - Fast electromagnetic transient simulation for flexible DC Power Grid.pdf`

## 摘要

*（摘要未提取到）*

## 核心贡献


- 提出MMC能量均分模型，简化子模块均压排序算法，保留桥臂闭锁外特性。
- 构建级联全桥直流断路器等值电路，实现子模块串快速等效与开断过程仿真。


## 使用的方法


- [[能量均分法|能量均分法]]
- [[等效电路法|等效电路法]]
- [[受控电压源建模|受控电压源建模]]
- [[梯形积分法|梯形积分法]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[半桥子模块|半桥子模块]]
- [[级联全桥直流断路器|级联全桥直流断路器]]
- [[直流架空线路|直流架空线路]]


## 相关主题


- [[柔性直流电网|柔性直流电网]]
- [[快速电磁暂态仿真|快速电磁暂态仿真]]
- [[换流器简化建模|换流器简化建模]]
- [[直流断路器建模|直流断路器建模]]
- [[模型降阶|模型降阶]]


## 主要发现


- 能量均分模型精度与详细等价模型一致，且仿真耗时几乎不随电平数增加。
- 断路器快速模型较详细模型提速约十倍，关键电气量波形残差可信度指标高。
- 仿真步长推荐10至25微秒，可在保证精度的同时实现最优计算效率。


