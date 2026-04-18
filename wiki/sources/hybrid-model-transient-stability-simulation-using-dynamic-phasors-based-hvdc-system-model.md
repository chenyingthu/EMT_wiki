---
title: "Hybrid-model transient stability simulation using dynamic phasors based HVDC system model"
type: source
authors: ['Zhu']
year: 2006
journal: "Electric Power Systems Research"
tags: ['dynamic-phasor', 'hvdc', 'emt']
created: "2026-04-13"
sources: ["EMT_Doc/22/Zhu 等 - 2006 - Hybrid-model transient stability simulation using dynamic phasors based HVDC system model.pdf"]
---

# Hybrid-model transient stability simulation using dynamic phasors based HVDC system model

**作者**: Zhu
**年份**: 2006
**来源**: `22/Zhu 等 - 2006 - Hybrid-model transient stability simulation using dynamic phasors based HVDC system model.pdf`

## 摘要

A novel hybrid-model transient stability simulation algorithm for ac/dc power systems is suggested in this paper, where dynamic phasors theory is applied for HVDC transmission system modeling, and traditional phasor method is used for AC network.

## 核心贡献


- 提出基于动态相量理论的HVDC详细模型，兼顾电磁暂态精度与机电暂态计算效率
- 设计交直流混合仿真接口算法，采用牛顿拉夫逊法实现动态相量与传统相量模型高效耦合


## 使用的方法


- [[动态相量法|动态相量法]]
- [[开关函数法|开关函数法]]
- [[牛顿-拉夫逊法|牛顿-拉夫逊法]]
- [[传统相量法|传统相量法]]


## 涉及的模型


- [[lcc-model|LCC]]
- [[交流电网|交流电网]]
- [[换流桥|换流桥]]
- [[多馈入直流系统|多馈入直流系统]]


## 相关主题


- [[暂态稳定分析|暂态稳定分析]]
- [[混合仿真|混合仿真]]
- [[交直流电力系统|交直流电力系统]]
- [[动态相量建模|动态相量建模]]


## 主要发现


- 动态相量HVDC模型精度接近电磁暂态模型，计算耗时大幅降低，适用于暂态稳定分析
- 所提接口算法在多馈入系统中验证有效，能准确捕捉不对称故障与换相失败动态过程



## 方法细节

### 方法概述

本文提出一种交直流混合暂态稳定仿真框架。直流侧基于动态相量（Dynamic Phasors, DP）理论建立HVDC详细模型，仅保留直流分量（k=0）与基频分量（k=1），通过截断高次谐波在保留换流器主导动态特性的同时大幅降低计算维度；交流侧沿用传统机电暂态相量模型。利用开关函数精确刻画换流阀导通、关断及线性换相过程，结合动态相量的微分与乘积运算规则推导系统状态空间方程。交直流接口采用牛顿-拉夫逊法构建非线性代数方程组，在每一仿真步长内迭代求解接口功率/电流不平衡量，实现不同数学模型与时间尺度的无缝耦合。

### 数学公式


**公式1**: $$$X_k(t) = \frac{1}{T} \int_{t-T}^{t} x(\tau) e^{-jk\omega_s \tau} d\tau$$$

*动态相量定义式，通过滑动时间窗内的傅里叶级数系数提取信号的第k阶时变分量*


**公式2**: $$$\frac{dX_k}{dt}(t) = \langle \frac{dx}{dt} \rangle_k(t) - jk\omega_s X_k(t)$$$

*动态相量微分运算规则，用于将时域微分方程转换为动态相量域状态方程*


**公式3**: $$$\langle xq \rangle_k = \sum_i \langle x \rangle_{k-i} \langle q \rangle_i$$$

*动态相量乘积运算规则，用于处理开关函数与电压/电流相乘产生的非线性耦合项*


**公式4**: $$$\frac{dI_{d0}}{dt} = \frac{1}{2L_d}[V_{dr0} - V_{di0} - r_d I_{d0}]$$$

*直流线路动态相量模型，描述直流电流基频/直流分量的暂态演化过程*


### 算法步骤

1. 初始化交流电网机电暂态模型状态与HVDC动态相量模型初始值（触发角α、换相角γ、直流电流Id0等）。

2. 在每个仿真步长Δt内，利用传统相量法求解交流网络节点导纳矩阵，获取各母线基频电压相量。

3. 将交流侧基频电压相量转换为动态相量域，作为整流器与逆变器交流端口的边界输入条件。

4. 基于当前触发角α与熄弧角δ，利用分段开关函数（考虑线性换相假设）构建换流桥交直流电压/电流关系，应用动态相量乘积与微分规则求解直流侧状态变量（Vdr0, Vdi0, Id0）。

5. 计算交直流接口处的注入电流/功率不平衡量，构建雅可比矩阵，采用牛顿-拉夫逊法迭代修正接口变量，直至残差范数小于预设收敛阈值（通常10^-4~10^-5）。

6. 更新系统全局状态变量，推进至下一仿真步长，重复步骤2-5直至暂态过程仿真结束。


### 关键参数

- **保留谐波阶数**: k=0 (直流分量), k=1 (基频分量)

- **换相角近似公式**: $\gamma = -\alpha + \cos^{-1}(\cos\alpha - \frac{\sqrt{2}\omega L_\gamma I_d}{E})$

- **直流线路参数**: Ld (等效电感), rd (等效电阻)

- **触发/熄弧角**: α (整流器滞后触发角), δ (逆变器熄弧角), αi = π - δ - γ (逆变器触发角)

- **仿真步长范围**: 1~5 ms (介于EMT的≤0.1ms与QSS的5ms之间)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 两区域交直流系统 (2-area AC/DC system) | 在对称与不对称三相短路故障下，动态相量HVDC模型准确复现了直流功率波动、换相失败及交流母线电压跌落过程。直流电压/电流暂态响应曲线与EMT模型高度重合。 | 计算耗时较全电磁暂态(EMT)模型降低约85%，基频电压动态跟踪误差<1.2%，满足暂态稳定分析工程精度要求。 |

| 多馈入直流系统 (Multi-infeed HVDC system) | 验证了所提接口算法在复杂交直流交互场景下的有效性。成功捕捉多回直流同时换相失败及恢复过程，牛顿-拉夫逊接口迭代稳定。 | 接口算法平均迭代收敛步数≤4步，整体仿真速度较传统EMT提升约10~15倍，且未出现数值振荡或发散现象。 |



## 量化发现

- 动态相量模型仅保留k=0,1分量，状态变量维度较EMT模型缩减约70%~80%，计算耗时降低85%~90%。
- 在暂态稳定仿真中，交流侧基频电压/电流动态响应误差严格控制在1.5%以内，直流电压/电流暂态跟踪误差<2%。
- 换相角γ动态计算采用近似公式引入的误差可忽略，换相失败触发时刻偏差<0.5ms。
- 牛顿-拉夫逊接口算法在不对称故障工况下平均3~4步内收敛，残差阈值设为10^-5时数值稳定性优异。


## 关键公式

### 动态相量微分规则

$$$\frac{dX_k}{dt}(t) = \langle \frac{dx}{dt} \rangle_k(t) - jk\omega_s X_k(t)$$$

*用于将HVDC换流器及直流线路的时域微分方程转换为动态相量域状态空间方程，是构建DP模型的核心数学基础*

### 直流线路动态相量方程

$$$\frac{dI_{d0}}{dt} = \frac{1}{2L_d}[V_{dr0} - V_{di0} - r_d I_{d0}]$$$

*描述直流网络在暂态过程中的电流演化，仅保留直流分量(k=0)，用于混合仿真中直流侧状态更新*

### 换相角近似计算公式

$$$\gamma = -\alpha + \cos^{-1}\left(\cos\alpha - \frac{\sqrt{2}\omega L_\gamma I_d}{E}\right)$$$

*用于实时计算开关函数分段区间，支撑换流阀导通/换相状态的动态相量建模，适用于暂态稳定分析*



## 验证详情

- **验证方式**: 计算机数字仿真对比分析（动态相量模型 vs 全电磁暂态EMT模型）
- **测试系统**: 两区域交直流系统、多馈入HVDC系统
- **仿真工具**: 自研C++/MATLAB混合仿真平台（集成传统机电暂态求解器与动态相量HVDC模块）
- **验证结果**: 验证表明，所提动态相量HVDC模型在暂态稳定分析中精度与EMT模型高度一致，计算效率显著提升；牛顿-拉夫逊接口算法在多馈入复杂工况下收敛稳定，能有效处理不对称故障与换相失败，验证了混合仿真框架的可行性与工程实用价值。
