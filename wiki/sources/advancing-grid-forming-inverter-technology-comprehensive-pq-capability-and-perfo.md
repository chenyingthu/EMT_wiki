---
title: "Advancing Grid-Forming Inverter Technology: Comprehensive PQ Capability and Performance Analysis"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Access;2025;13; ;10.1109/ACCESS.2025.3561788"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/06/Nurunnabi 等 - 2025 - Advancing Grid-Forming Inverter Technology Comprehensive PQ Capability and Performance Analysis.pdf"]
---

# Advancing Grid-Forming Inverter Technology: Comprehensive PQ Capability and Performance Analysis

**作者**: 
**年份**: 2025
**来源**: `06/Nurunnabi 等 - 2025 - Advancing Grid-Forming Inverter Technology Comprehensive PQ Capability and Performance Analysis.pdf`

## 摘要

This paper presents a performance analysis of grid-forming (GFM) inverter technology, which is essential to ensure stable and reliable operation of power systems with high penetration of inverter-based resources (IBRs). Recognizing that IBR operational constraints are distinct from those of synchronous generators, this study develops advanced PQ capability models and algorithmic frameworks that accurately characterize GFM inverter operational constraints across various coupling filter configurations (L, LC, and LCL). Electromagnetic transient (EMT) simulations show that the Enhanced Voltage Regulation (EVR) and Controlled Proportional-Integral Droop (CPID) strategies proposed in this paper improve voltage and frequency stability under dynamic loading and fault conditions, outperforming con

## 核心贡献


- 提出考虑PWM饱和与电流约束的构网型逆变器PQ能力边界建模算法
- 设计增强型电压调节与比例积分下垂控制策略以提升动态稳定性
- 揭示L/LC/LCL滤波器拓扑对逆变器谐波抑制与运行域的影响机制


## 使用的方法


- [[电磁暂态仿真|电磁暂态仿真]]
- [[实时硬件在环验证|实时硬件在环验证]]
- [[下垂控制|下垂控制]]
- [[增强型电压调节|增强型电压调节]]
- [[pq能力边界算法|PQ能力边界算法]]
- [[pwm饱和约束建模|PWM饱和约束建模]]


## 涉及的模型


- [[构网型逆变器-gfm|构网型逆变器(GFM)]]
- [[跟网型逆变器-gfl|跟网型逆变器(GFL)]]
- [[l-lc-lcl耦合滤波器|L/LC/LCL耦合滤波器]]
- [[pwm调制模型|PWM调制模型]]
- [[随机混合负载|随机混合负载]]


## 相关主题


- [[构网型逆变器控制|构网型逆变器控制]]
- [[pq能力分析|PQ能力分析]]
- [[低惯量电网稳定性|低惯量电网稳定性]]
- [[电能质量与谐波抑制|电能质量与谐波抑制]]
- [[实时仿真验证|实时仿真验证]]
- [[ieee-1547标准符合性|IEEE 1547标准符合性]]


## 主要发现


- EMT仿真表明EVR与CPID策略在动态负载与故障下电压频率稳定性更优
- 硬件实验证实所提控制能有效抑制谐波并实现故障后快速恢复
- 不同滤波器配置下PQ边界模型准确刻画了逆变器实际运行约束


