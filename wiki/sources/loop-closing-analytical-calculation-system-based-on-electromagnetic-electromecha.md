---
title: "Loop closing analytical calculation system based on electromagnetic-electromechanical transient simu"
type: source
authors: ['CNKI']
year: 2023
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/25/Zhu 等 - 2012 - Loop closing analytical calculation system based on electromagnetic-electromechanical transient simu.pdf"]
---

# Loop closing analytical calculation system based on electromagnetic-electromechanical transient simu

**作者**: CNKI
**年份**: 2023
**来源**: `25/Zhu 等 - 2012 - Loop closing analytical calculation system based on electromagnetic-electromechanical transient simu.pdf`

## 摘要

To improve safe operation of power network, a loop closing analytical calculation system based on electromagnetic- electromechanical transient hybrid simulation theory is developed. An automatic electromagnetic network partition solution based on the maximal stair search algorithm is put forward. The system also implements the function of automatic transformation from the electromechanical transient models to electromagnetic models and links the geographic maps and station maps, which not only makes loop closing operation easy but also enhances veracity. Simulation and calculation results show that the system can increase the accuracy of loop closing, providing evidence for loop closing operation. This work is supported by National High-tech R&D Program of China (863 Program) (No. 2011AA05

## 核心贡献


- 提出基于最大级数搜索算法的电磁网络自动划分方法，实现合环区域精准分网
- 实现机电暂态模型向电磁暂态模型的自动转换，避免手工录入提升建模效率
- 构建单机多核并行计算架构，降低混合仿真硬件成本并提升计算速度


## 使用的方法


- [[机电-电磁暂态混合仿真|机电-电磁暂态混合仿真]]
- [[最大级数搜索算法|最大级数搜索算法]]
- [[戴维南-诺顿等值接口|戴维南/诺顿等值接口]]
- [[序相量与瞬时值变换|序相量与瞬时值变换]]
- [[单机多核并行计算|单机多核并行计算]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[变压器|变压器]]
- [[同步发电机|同步发电机]]
- [[负荷|负荷]]
- [[电容器|电容器]]
- [[电抗器|电抗器]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[电网合环分析|电网合环分析]]
- [[网络自动划分|网络自动划分]]
- [[模型自动转换|模型自动转换]]
- [[并行计算|并行计算]]
- [[冲击电流分析|冲击电流分析]]


## 主要发现


- 喀什电网算例验证表明，系统可准确获取合环冲击电流与过电压瞬时值
- 开关统计功能有效捕捉最恶劣合环相角下的最大冲击电流，提升安全性评估精度
- 单机并行架构显著缩短混合仿真耗时，满足实际电网合环操作的快速分析需求


