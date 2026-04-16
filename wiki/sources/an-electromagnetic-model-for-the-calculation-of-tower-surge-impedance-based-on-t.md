---
title: "An Electromagnetic Model for the Calculation of Tower Surge Impedance Based on Thin Wire Approximation"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2020.3003250"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An Electromagnetic Model for the Calculation of Tower Surge Impedance Based on Thin Wire Approximation.pdf"]
---

# An Electromagnetic Model for the Calculation of Tower Surge Impedance Based on Thin Wire Approximation

**作者**: 
**年份**: 2020
**来源**: `07&08/An Electromagnetic Model for the Calculation of Tower Surge Impedance Based on Thin Wire Approximation.pdf`

## 摘要

—When lightning strikes a transmission line tower or shield wires, electromagnetic waves propagate through the tower back and forth, increasing the voltage across insulator strings. Tis can eventually lead to a back-ﬂashover (BF), which may cause damage to equipment or costly power outages. To calculate the over-voltages and predict the probability of a BF, an accurate model of the tower and its grounding system is needed in electromagnetic transient (EMT) type simulators. Tere are a number of theoretical models for the equivalent circuit of a transmission tower. However, they either are not accurate enough or they are derived for a certain type of transmission tower, which limits their applicability. Numerical electromagnetic analyses have less simpliﬁcations compared to the theoretical s

## 核心贡献


- 提出基于细线近似与NEC4的自动化建模流程，精确计算任意杆塔冲击阻抗
- 采用频域冲击阻抗定义，消除电流波形依赖性，实现仅依赖几何特性的通用计算
- 完整考虑杆塔结构细节与接地极有限电阻，突破传统简化理论模型的适用局限


## 使用的方法


- [[矩量法-mom|矩量法(MoM)]]
- [[细线近似|细线近似]]
- [[nec4数值电磁计算|NEC4数值电磁计算]]
- [[频域阻抗分析|频域阻抗分析]]
- [[自动化线网生成|自动化线网生成]]


## 涉及的模型


- [[输电杆塔|输电杆塔]]
- [[接地系统|接地系统]]
- [[水平接地极|水平接地极]]
- [[损耗大地模型|损耗大地模型]]


## 相关主题


- [[雷电冲击过电压|雷电冲击过电压]]
- [[杆塔冲击阻抗|杆塔冲击阻抗]]
- [[反击闪络预测|反击闪络预测]]
- [[数值电磁分析|数值电磁分析]]
- [[接地系统建模|接地系统建模]]


## 主要发现


- 数值模型精确计及杆塔细节与接地电阻，所得冲击阻抗显著区别于传统简化理论模型
- 频域阻抗定义完全独立于注入电流波形，为电磁暂态仿真提供稳定通用的参数表征
- 仿真验证了模型在不同接地极长度与土壤电阻率下准确计及接地电阻的能力


