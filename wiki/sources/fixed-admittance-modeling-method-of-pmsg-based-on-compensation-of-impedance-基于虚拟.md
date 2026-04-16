---
title: "Fixed-admittance Modeling Method of PMSG Based on Compensation of Impedance; [基于虚拟阻抗补偿的 PMSG 恒导纳建模方法"
type: source
authors: ['CNKI']
year: 2024
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/Shi和Liu - 2024 - Fixed-admittance Modeling Method of PMSG Based on Compensation of Impedance; [基于虚拟阻抗补偿的 PMSG 恒导纳建模方法.pdf"]
---

# Fixed-admittance Modeling Method of PMSG Based on Compensation of Impedance; [基于虚拟阻抗补偿的 PMSG 恒导纳建模方法

**作者**: CNKI
**年份**: 2024
**来源**: `19、20、21/EMT_task_19/Shi和Liu - 2024 - Fixed-admittance Modeling Method of PMSG Based on Compensation of Impedance; [基于虚拟阻抗补偿的 PMSG 恒导纳建模方法.pdf`

## 摘要

The permanent magnet generator system has a complex structure and a large number of nodes. In the real-time electromagnetic transient simulation, if the traditional modeling method is used, the calculation of the system admittance matrix will be too complicated, resulting in a serious limitation of the simulation scale. Therefore, this paper proposes a fixed-admittance modeling method of permanent magnet synchronous generator (PMSG) based on virtual impedance compensation. This method is based on the traditional generator model, and the generator admittance matrix is fixed

## 核心贡献


- 提出基于虚拟阻抗补偿的PMSG恒导纳建模方法，固定发电机导纳矩阵
- 以暂态误差最小为目标优化阻抗参数，结合ADC模型构建完整恒导纳模型
- 避免导纳矩阵实时求逆，显著降低计算复杂度，适用于FPGA等实时硬件平台


## 使用的方法


- [[隐式梯形积分法|隐式梯形积分法]]
- [[伴随离散电路模型|伴随离散电路模型]]
- [[虚拟阻抗补偿|虚拟阻抗补偿]]
- [[恒导纳建模|恒导纳建模]]
- [[诺顿等效|诺顿等效]]


## 涉及的模型


- [[pmsg|PMSG]]
- [[全功率换流器|全功率换流器]]
- [[风力机|风力机]]
- [[pd相域模型|PD相域模型]]
- [[dq同步旋转坐标系模型|dq同步旋转坐标系模型]]


## 相关主题


- [[实时电磁暂态仿真|实时电磁暂态仿真]]
- [[风电机组建模|风电机组建模]]
- [[fpga硬件仿真|FPGA硬件仿真]]
- [[大规模新能源系统|大规模新能源系统]]
- [[恒导纳网络求解|恒导纳网络求解]]


## 主要发现


- 恒导纳模型避免导纳矩阵实时求逆，大幅降低计算量并有效扩展仿真规模
- 仿真验证表明模型暂态误差小精度高，动态响应与传统变导纳模型高度一致
- 模型结构固定计算效率高，成功应用于FPGA离散硬件平台满足实时性要求


