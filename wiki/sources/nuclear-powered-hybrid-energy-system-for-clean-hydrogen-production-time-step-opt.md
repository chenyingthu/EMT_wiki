---
title: "Nuclear-Powered Hybrid Energy System for Clean Hydrogen Production: Time-Step-Optimized Real-Time Multi-Domain Hardware Emulation"
type: source
authors: ['未知']
year: 2026
journal: "IEEE Transactions on Energy Conversion; ;PP;99;10.1109/TEC.2026.3658726"
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/29/Chen 等 - 2026 - Nuclear-Powered Hybrid Energy System for Clean Hydrogen Production Time-Step-Optimized Real-Time Mu.pdf"]
---

# Nuclear-Powered Hybrid Energy System for Clean Hydrogen Production: Time-Step-Optimized Real-Time Multi-Domain Hardware Emulation

**作者**: 
**年份**: 2026
**来源**: `29/Chen 等 - 2026 - Nuclear-Powered Hybrid Energy System for Clean Hydrogen Production Time-Step-Optimized Real-Time Mu.pdf`

## 摘要

—Increasing global emphasis on decarbonization and the proliferation of renewable energy, energy storage, and nuclear power is driving a surge of research interest into integrated sustainable energy modeling, simulation, operation and control. Traditional electromagnetic transient (EMT) methods typically discretize electrical networks using the trapezoidal rule. When coupled with the ordinary differential equations (ODEs) of other physical domains, however, the absolute stability region of the numerical integration scheme can shift, and discrepancies in time constants across subsystems further complicate integration of disparate models. While the demand for integrating EMT with multi-domain co-simulations is increasing, existing commercial EMT simulation tools either lack support for multi

## 核心贡献


- 提出鲁棒多尺度时间步长估计框架，实现电磁暂态与多物理域实时协同仿真。
- 设计自适应最优步长选择算法，解决异构物理域时间常数差异引发的数值稳定性问题。
- 基于FPGA平台实现核能-可再生能源混合制氢系统的实时硬件协同仿真验证。


## 使用的方法


- [[梯形积分法|梯形积分法]]
- [[节点分析法|节点分析法]]
- [[多时间步长协同仿真|多时间步长协同仿真]]
- [[隐式迭代求解|隐式迭代求解]]
- [[牛顿迭代法|牛顿迭代法]]
- [[fpga硬件协同仿真|FPGA硬件协同仿真]]


## 涉及的模型


- [[小型模块化反应堆-smr|小型模块化反应堆(SMR)]]
- [[质子交换膜-pem-电解槽|质子交换膜(PEM)电解槽]]
- [[风电场|风电场]]
- [[光伏系统|光伏系统]]
- [[储氢罐|储氢罐]]
- [[dfig-model|DFIG]]
- [[热工水力系统|热工水力系统]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[多域协同仿真|多域协同仿真]]
- [[硬件协同仿真|硬件协同仿真]]
- [[核能-可再生能源混合系统|核能-可再生能源混合系统]]
- [[清洁制氢|清洁制氢]]
- [[时间步长优化|时间步长优化]]
- [[fpga加速|FPGA加速]]


## 主要发现


- RMTE框架协调了反应堆刚性方程与热工水力大时间常数，保障多域耦合数值稳定性。
- FPGA硬件协同仿真验证了自适应步长算法显著提升了系统整体仿真效率与执行速度。
- 实现了包含SMR、风光及PEM电解槽的混合能源系统微秒级实时高精度仿真。


