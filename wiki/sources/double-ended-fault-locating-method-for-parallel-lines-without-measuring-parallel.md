---
title: "Double-Ended Fault-Locating Method for Parallel Lines Without Measuring Parallel Line Currents"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Power Delivery;2025;40;6;10.1109/TPWRD.2025.3605244"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/Double-Ended_Fault-Locating_Method_for_Parallel_Lines_Without_Measuring_Parallel_Line_Currents.pdf"]
---

# Double-Ended Fault-Locating Method for Parallel Lines Without Measuring Parallel Line Currents

**作者**: 
**年份**: 2025
**来源**: `13&14/files/Double-Ended_Fault-Locating_Method_for_Parallel_Lines_Without_Measuring_Parallel_Line_Currents.pdf`

## 摘要

—This paper introduces a novel double-ended impedance-based fault-locating method for parallel lines, effectively addressing the challenges posed by mutual coupling. Instead of directly measuring the parallel line zero-sequence current, the proposed method estimates it using synchronized currents and voltages from the local end of the faulted line

## 核心贡献


- 提出无需测量平行线路电流的双端阻抗测距算法，有效解决零序互感耦合难题
- 推导多拓扑平行线路零序电流估计公式，结合二次型与迭代法实现高精度测距
- 设计零序电源阻抗误差补偿机制，提升系统参数不准确时的故障定位鲁棒性


## 使用的方法


- [[双端阻抗测距法|双端阻抗测距法]]
- [[相量法|相量法]]
- [[二次方程求解|二次方程求解]]
- [[迭代算法|迭代算法]]
- [[零序电流估计|零序电流估计]]
- [[误差补偿技术|误差补偿技术]]


## 涉及的模型


- [[平行输电线路|平行输电线路]]
- [[零序网络模型|零序网络模型]]
- [[电源阻抗模型|电源阻抗模型]]
- [[混合线路|混合线路]]


## 相关主题


- [[故障测距|故障测距]]
- [[零序互感耦合|零序互感耦合]]
- [[继电保护|继电保护]]
- [[输电线路建模|输电线路建模]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 主要发现


- EMTP仿真验证表明，该方法在多种平行线路拓扑下均能实现高精度定位
- 所提误差补偿技术有效抑制了零序电源阻抗参数偏差导致的测距误差
- 二次型与迭代法在多数工况下结果一致，且无需依赖对端电压数据即可运行


