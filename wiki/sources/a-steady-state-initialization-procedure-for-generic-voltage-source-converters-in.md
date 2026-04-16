---
title: "A steady-state initialization procedure for generic voltage-source converters in electromagnetic transient simulations"
type: source
authors: ['Guilherme', 'Cirilo', 'Leandro']
year: 2023
journal: "Electric Power Systems Research, 221 (2023) 109404. doi:10.1016/j.epsr.2023.109404"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/04/1-s2.0-S0378779623002936-main.pdf"]
---

# A steady-state initialization procedure for generic voltage-source converters in electromagnetic transient simulations

**作者**: Guilherme, Cirilo, Leandro
**年份**: 2023
**来源**: `04/1-s2.0-S0378779623002936-main.pdf`

## 摘要

0378-7796/© 2023 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by- A steady-state initialization procedure for generic voltage-source converters ENIC Division, Grid Innovation Research Laboratory, Central Research Institute of Electric Power Industry (CRIEPI), 2-6-1 Nagasaka, Electromagnetic transient (EMT) simulations are often performed to analyze disturbances which occur during a steady-state operati

## 核心贡献


- 提出通用VSC稳态初始化启发式流程，系统化设定电路与控制部分初值
- 基于正序与三相交流潮流解，直接计算并赋值VSC内部状态变量与历史项
- 消除零初值启动的漫长过渡过程，实现含多VSC电网EMT仿真的直接稳态启动


## 使用的方法


- [[潮流计算|潮流计算]]
- [[三相交流稳态计算|三相交流稳态计算]]
- [[启发式初始化|启发式初始化]]
- [[梯形积分法|梯形积分法]]
- [[numerical-integration|数值积分]]
- [[dq坐标变换|dq坐标变换]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[lc滤波器|LC滤波器]]
- [[直流电容|直流电容]]
- [[配电网络|配电网络]]
- [[同步发电机|同步发电机]]
- [[rlc负荷|RLC负荷]]
- [[锁相环-pll|锁相环(PLL)]]
- [[自动电压-电流调节器|自动电压/电流调节器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[稳态初始化|稳态初始化]]
- [[vsc-model|VSC]]
- [[潮流计算|潮流计算]]
- [[配电系统仿真|配电系统仿真]]
- [[控制系统初始化|控制系统初始化]]


## 主要发现


- 采用所提流程初始化后，6.6kV双VSC配网仿真几乎无暂态过程，直接达到稳态
- 未初始化时仿真运行300毫秒仍无法收敛，验证了直接稳态启动的必要性
- 电路与控制状态变量初值精准匹配潮流解，有效抑制了启动瞬间的数值振荡


