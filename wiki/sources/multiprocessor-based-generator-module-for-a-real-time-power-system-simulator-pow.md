---
title: "Multiprocessor based generator module for a real-time power system simulator - Power Systems, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multiprocessor based generator module for a real-time power system simulator.pdf"]
---

# Multiprocessor based generator module for a real-time power system simulator - Power Systems, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `27&28/Multiprocessor based generator module for a real-time power system simulator.pdf`

## 摘要

A new geneeator simulation module was developed for an electrical power system simulator. This simulator is on an analog simultaneous base. Therefore the module has to simulate a generator behavior precisely. Furthermore, it is required to be able to use the analog simulator as easily as an off- line simulation program. To meet the requirement, the developed generator module adopts a multiprocessor consisting of microprocessors and an analog three-phase sinusoidal oscillator. Any type of generator can be easily simulated only by changing the program of the microprocessors.

## 核心贡献


- 提出多微处理器发电机仿真模块架构，结合模拟三相振荡器实现平滑波形输出
- 采用四微处理器并行求解微分方程，显著缩短仿真步长以满足实时性要求
- 引入浮点运算避免数值误差，结合梯形积分法实现高精度电磁暂态动态求解


## 使用的方法


- [[多处理器并行计算|多处理器并行计算]]
- [[梯形积分法|梯形积分法]]
- [[浮点运算|浮点运算]]
- [[dq坐标变换|dq坐标变换]]
- [[数模混合仿真|数模混合仿真]]


## 涉及的模型


- [[同步发电机|同步发电机]]
- [[励磁控制系统-avr|励磁控制系统(AVR)]]
- [[调速系统-gov|调速系统(GOV)]]
- [[模拟三相正弦振荡器|模拟三相正弦振荡器]]
- [[输电线路与变压器|输电线路与变压器]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[混合仿真|混合仿真]]
- [[并行计算|并行计算]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[发电机动态建模|发电机动态建模]]


## 主要发现


- 四微处理器并行架构有效缩短计算耗时，使仿真步长满足模拟同步基实时要求
- 浮点运算结合梯形法显著抑制数值误差，模块输出与EMTP离线结果高度吻合
- 仅修改微处理器程序即可灵活模拟各类发电机，大幅降低传统模拟模块调参时间


