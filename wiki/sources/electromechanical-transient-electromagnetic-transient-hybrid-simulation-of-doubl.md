---
title: "Electromechanical transient-electromagnetic transient hybrid simulation of doubly-fed induction gene"
type: source
authors: ['CNKI']
year: 2022
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/17/Gu 等 - 2015 - Electromechanical transient-electromagnetic transient hybrid simulation of doubly-fed induction gene.pdf"]
---

# Electromechanical transient-electromagnetic transient hybrid simulation of doubly-fed induction gene

**作者**: CNKI
**年份**: 2022
**来源**: `17/Gu 等 - 2015 - Electromechanical transient-electromagnetic transient hybrid simulation of doubly-fed induction gene.pdf`

## 摘要

To analyze the dynamic response of double-fed induction generator (DFIG) in-depth, based on the operation principle of DFIG an electromagnetic transient model of DFIG is built and the electromagnetic transient-electromechanical transient hybrid simulation of DFIG is performed. The hybrid simulation of DFIG is implemented by the self-developed large-scale power system analysis software package based hybrid simulation platform named Power System Department- Power System Model (PSD-PSModel), and the frame of the basic model of DFIG is established. The wind farm is equivalently simulated by single machine, and IEEE 14-bus test system is utilized for the detailed simulation to analyze the dynamic behavior of the system, the control strategy and dynamic response. The achievement can contribute t

## 核心贡献


- 基于dq0坐标系构建双馈风机电磁暂态模型采用梯形积分法离散求解
- 在PSD-PSModel平台实现机电与电磁暂态混合仿真接口及迭代算法
- 提出定子端口并联大电阻与补偿电流法有效解决电机开路数值不稳定问题


## 使用的方法


- [[dq0坐标变换|dq0坐标变换]]
- [[梯形积分法|梯形积分法]]
- [[戴维南等值|戴维南等值]]
- [[混合仿真接口|混合仿真接口]]
- [[单台机等值|单台机等值]]


## 涉及的模型


- [[dfig-model|DFIG]]
- [[双质量块轴系模型|双质量块轴系模型]]
- [[转子侧换流器|转子侧换流器]]
- [[网侧换流器|网侧换流器]]
- [[同步发电机|同步发电机]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[风电场等值建模|风电场等值建模]]
- [[暂态稳定性分析|暂态稳定性分析]]
- [[故障动态响应|故障动态响应]]
- [[控制系统建模|控制系统建模]]


## 主要发现


- 三相与单相短路故障下双馈风机有功无功解耦控制策略均能快速恢复平稳
- 暂态过程中转子电流与直流母线电压受冲击显著是触发机组保护动作主因
- 桨距角控制能有效抑制机械转速突变混合仿真可清晰揭示风机内部动态响应


