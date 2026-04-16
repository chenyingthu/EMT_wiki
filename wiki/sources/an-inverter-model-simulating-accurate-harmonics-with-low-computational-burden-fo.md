---
title: "An Inverter Model Simulating Accurate Harmonics with Low Computational Burden for Electromagnetic Transient Simulations"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Electronics; ;PP;99;10.1109/TPEL.2020.3026721"
tags: ['harmonic']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An Inverter Model Simulating Accurate Harmonics With Low Computational Burden for Electromagnetic Transient Simulations.pdf"]
---

# An Inverter Model Simulating Accurate Harmonics with Low Computational Burden for Electromagnetic Transient Simulations

**作者**: 
**年份**: 2020
**来源**: `07&08/An Inverter Model Simulating Accurate Harmonics With Low Computational Burden for Electromagnetic Transient Simulations.pdf`

## 摘要

—The electromagnetic transient (EMT) simulation of a power system involving power-electronics converters requires a fairly small time-step size to consider switching of the converters, thus leading to a heavy computational burden. To accelerate such simulations, this paper generalizes the time average method (TAM), originally developed for real-time simulations, so that it becomes suitable to off-line EMT simulations. For obtaining accurate current waveforms with a large time step, the TAM and the proposed method represent each leg of an inverter by voltage sources, and its output voltage is modiﬁed by interpolation at an instance of switching. The original TAM was intended for the primitive backward Euler method. This paper contributes to generalize it for the trapezoidal integration meth

## 核心贡献


- 将时间平均法推广至梯形积分法，使其适用于离线电磁暂态仿真程序
- 提出基于解析公式的开关时刻识别方法，替代FPGA硬件计数器以适配通用PC
- 采用电压源等效桥臂并在开关时刻进行电压插值，实现大时间步长下的高精度仿真


## 使用的方法


- [[时间平均法-tam|时间平均法(TAM)]]
- [[电压插值法|电压插值法]]
- [[梯形积分法|梯形积分法]]
- [[后向欧拉法|后向欧拉法]]
- [[电路平均模型|电路平均模型]]
- [[开关模型|开关模型]]


## 涉及的模型


- [[并网逆变器|并网逆变器]]
- [[半桥逆变器|半桥逆变器]]
- [[逆变器桥臂等效电路|逆变器桥臂等效电路]]
- [[pwm调制模型|PWM调制模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[谐波分析|谐波分析]]
- [[离线仿真加速|离线仿真加速]]
- [[电力电子变换器建模|电力电子变换器建模]]
- [[大时间步长仿真|大时间步长仿真]]


## 主要发现


- 仿真时间步长可扩大五倍而不降低精度，有效解决传统开关模型计算负担重的问题
- 单相并网逆变器离线仿真计算时间缩短至三分之一，显著提升大规模系统仿真效率
- 能够准确复现开关操作产生的谐波频谱，验证了插值模型在频域特性上的高保真度


