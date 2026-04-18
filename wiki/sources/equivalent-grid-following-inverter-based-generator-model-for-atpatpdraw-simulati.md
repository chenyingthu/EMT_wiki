---
title: "Equivalent grid-following inverter-based generator model for ATP/ATPDraw simulations"
type: source
authors: ['M.B. Luchini']
year: 2023
journal: "Electric Power Systems Research, 223 (2023) 109624. doi:10.1016/j.epsr.2023.109624"
tags: ['ibg']
created: "2026-04-13"
sources: ["EMT_Doc/17/Luchini 等 - 2023 - Equivalent grid-following inverter-based generator model for ATPATPDraw simulations.pdf"]
---

# Equivalent grid-following inverter-based generator model for ATP/ATPDraw simulations

**作者**: M.B. Luchini
**年份**: 2023
**来源**: `17/Luchini 等 - 2023 - Equivalent grid-following inverter-based generator model for ATPATPDraw simulations.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. Equivalent grid-following inverter-based generator model for ATP/ATPDraw M.B. Luchini a,∗, O.E. Batista a, F.V. Lopes b, R.L.A. Reis b, B.A. Souza c a Department of Electrical Engineering, Federal University of Espírito Santo, Vitória, ES, Brazil b Department of Electrical Engineering, Federal University of Paraiba, João Pessoa, PB, Brazil

## 核心贡献


- 提出适用于EMTP的跟网型逆变器等效时域模型替代复杂全开关模型
- 在ATP平台实现并提供详细建模指南支持灵活配置不同控制策略
- 集成DSOGI-PLL与低通滤波锁相环精确捕捉畸变电网暂态同步动态


## 使用的方法


- [[时域等效建模|时域等效建模]]
- [[锁相环同步技术|锁相环同步技术]]
- [[参考坐标变换|参考坐标变换]]
- [[低通滤波技术|低通滤波技术]]


## 涉及的模型


- [[跟网型逆变器-ibr|跟网型逆变器(IBR)]]
- [[光伏发电系统|光伏发电系统]]
- [[vsc-model|VSC]]
- [[储能系统|储能系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[逆变器并网资源建模|逆变器并网资源建模]]
- [[故障穿越特性|故障穿越特性]]
- [[电网故障分析|电网故障分析]]
- [[计算效率优化|计算效率优化]]


## 主要发现


- 相比完整开关模型仿真耗时降低约70%显著提升大规模电网计算效率
- 故障工况下输出电流平均误差仅约2.33%准确复现逆变器暂态响应
- 采用DSOGI-PLL同步策略可有效抑制电网谐波保障电流合成质量



## 方法细节

### 方法概述

本文提出一种适用于电磁暂态程序（EMTP）的跟网型逆变器并网资源（IBR）等效时域模型（EIBR），旨在替代计算密集的全开关模型。该模型在ATP/ATPDraw平台中实现，采用平均化时域等效思想，直接以电网三相电压为同步基准，通过用户设定的有功功率P和无功功率Q指令合成输出电流。模型核心包含电网同步（GS）模块与电流合成模块。GS模块提供两种锁相环方案：传统低通滤波结合PLL（LPF-PLL）以及双二阶广义积分器锁相环（DSOGI-PLL）。DSOGI-PLL通过DSOGI-QSG生成正交信号，并结合频率自适应的正序分量计算器（PSC），在电网畸变或故障期间精确提取基波正序电压与相位。电流合成模块基于瞬时功率理论，在dq同步旋转坐标系下将P、Q指令转换为dq轴电流参考值，再经反Park变换生成三相电流注入电网。该架构支持灵活配置不同控制策略（如故障穿越），并显著降低仿真步长要求与计算负担。

### 数学公式


**公式1**: $$$P = \frac{3}{2}(v_d i_d + v_q i_q)$$$

*dq同步旋转坐标系下的瞬时有功功率计算公式*


**公式2**: $$$Q = \frac{3}{2}(v_q i_d - v_d i_q)$$$

*dq同步旋转坐标系下的瞬时无功功率计算公式*


**公式3**: $$$i_d = \frac{2P}{3v_d}, \quad i_q = -\frac{2Q}{3v_d}$$$

*基于电网电压定向（$v_q=0$）推导出的dq轴参考电流计算公式，用于电流合成模块*


### 算法步骤

1. 采集电网三相电压信号$V_{abc}$，输入至电网同步（GS）模块。

2. 在GS模块中选择LPF-PLL或DSOGI-PLL进行同步跟踪。若采用DSOGI-PLL，首先通过DSOGI-QSG生成$\alpha\beta$轴正交滤波电压，随后输入至频率自适应正序计算器（PSC）提取基波正序分量，最终经SRF-PLL输出电网相位角$\theta$与频率$\omega$。

3. 利用提取的相位角$\theta$，通过Park变换将三相电网电压$V_{abc}$转换至dq同步旋转坐标系，得到$v_d$和$v_q$。

4. 根据系统运行状态或故障穿越（FRT）策略，设定目标有功功率$P_{ref}$与无功功率$Q_{ref}$。

5. 采用电网电压定向控制（GVD），令$v_q=0$，代入瞬时功率方程反解出dq轴参考电流$i_{d,ref}$与$i_{q,ref}$。

6. 将$i_{d,ref}$与$i_{q,ref}$通过反Park变换转换回三相静止坐标系，生成三相参考电流指令$I_{abc,ref}$。

7. 将合成的三相电流作为受控电流源注入ATP/ATPDraw外部电网模型，完成等效IBR的电磁暂态交互仿真。


### 关键参数

- **SRF-PLL比例增益_kp**: 0.8

- **SRF-PLL积分增益_ki**: 61.69

- **同步策略**: LPF-PLL 或 DSOGI-PLL（含频率自适应PSC）

- **控制架构**: 电网电压定向（GVD）+ 瞬时功率理论



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 稳态运行工况 | 模型在额定功率下稳定运行，输出电流波形平滑，与基准全开关模型高度吻合，验证了等效模型在正常工况下的静态精度。 | 与ATP/ATPDraw内置完整光伏开关模型相比，波形一致，但计算资源消耗大幅降低。 |

| 对称与不对称电网故障工况 | 在电网发生三相短路及单相接地故障期间，模型准确复现了跟网型逆变器的故障穿越动态响应，输出电流平均误差仅为2.33%，有效捕捉了暂态电流突变与恢复过程。 | 相比完整开关模型，故障暂态仿真执行时间缩短约70%，且无需极小步长即可保持数值稳定性。 |



## 量化发现

- 故障工况下输出电流平均误差约为2.33%
- 仿真执行时间相比完整开关基准模型降低约70%
- DSOGI-PLL在电网电压畸变条件下可有效抑制谐波干扰，保障同步相位精度
- 模型支持灵活替换控制模块，无需修改底层网络拓扑即可适配不同故障穿越策略


## 关键公式

### dq轴参考电流合成公式

$$$i_d = \frac{2P}{3v_d}, \quad i_q = -\frac{2Q}{3v_d}$$$

*在电网电压定向（$v_q=0$）假设下，用于将功率指令直接映射为电流源控制信号，是等效模型的核心控制律*

### 瞬时有功功率方程

$$$P = \frac{3}{2}(v_d i_d + v_q i_q)$$$

*用于建立dq坐标系下功率与电流的数学关系，是推导电流参考值的基础*



## 验证详情

- **验证方式**: 电磁暂态仿真对比验证
- **测试系统**: ATP/ATPDraw环境内置的完整跟网型光伏发电站基准模型（含全开关器件与详细控制回路）
- **仿真工具**: ATP/ATPDraw (Alternative Transients Program)
- **验证结果**: 通过在稳态及对称/不对称故障场景下与全开关基准模型进行对比，验证了所提等效时域模型的准确性与高效性。模型在故障期间的电流响应平均误差控制在2.33%以内，同时仿真耗时大幅降低70%，证明其适用于高比例IBR接入的大规模电网电磁暂态分析，且具备优异的控制策略扩展性。
