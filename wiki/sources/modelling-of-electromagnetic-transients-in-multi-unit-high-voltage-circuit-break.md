---
title: "Modelling of electromagnetic transients in multi-unit high-voltage circuit-breakers"
type: source
authors: ['Antoine Mailhot']
year: 2024
journal: "Electric Power Systems Research, 235 (2024) 110766. doi:10.1016/j.epsr.2024.110766"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Modelling of electromagnetic transients in multi-unit high-voltage circuit-breaker.pdf"]
---

# Modelling of electromagnetic transients in multi-unit high-voltage circuit-breakers

**作者**: Antoine Mailhot
**年份**: 2024
**来源**: `27&28/Modelling of electromagnetic transients in multi-unit high-voltage circuit-breaker.pdf`

## 摘要

0378-7796/© 2024 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies. Modelling of electromagnetic transients in multi-unit high-voltage Antoine Mailhot a,*, Ryszard Pater a, S´ebastien Poirier a, Jean Mahseredjian b, Ren´e Doche c a Institut de recherche d’Hydro-Qu´ebec (IREQ), Varennes, Canada High-voltage (HV) circuit-breakers (CBs) often consist of several making and breaking units (MBUs) in series. A

## 核心贡献


- 提出多断口高压断路器EMTP模型，集成开断介质恢复与关合击穿下降曲线
- 采用集中参数耦合各断口，精确模拟机械不同步引发的高频暂态过程
- 模型适配真空与SF6介质，可复现传统模型难以模拟的多次重燃现象


## 使用的方法


- [[emtp仿真|EMTP仿真]]
- [[集中参数建模|集中参数建模]]
- [[开关逻辑控制|开关逻辑控制]]
- [[击穿电压包络线法|击穿电压包络线法]]
- [[帕邢定律近似|帕邢定律近似]]


## 涉及的模型


- [[多断口高压断路器|多断口高压断路器]]
- [[合分闸单元-mbu|合分闸单元(MBU)]]
- [[均压电容|均压电容]]
- [[真空断路器-vcb|真空断路器(VCB)]]
- [[sf6断路器|SF6断路器]]
- [[电弧阻抗模型|电弧阻抗模型]]


## 相关主题


- [[电磁暂态|电磁暂态]]
- [[开关暂态|开关暂态]]
- [[断路器建模|断路器建模]]
- [[预击穿与重燃|预击穿与重燃]]
- [[介质恢复特性|介质恢复特性]]
- [[高频暂态分析|高频暂态分析]]


## 主要发现


- 标准允许的最大断口不同步度会引发开断多次重燃或关合严重过电压
- 单断口预击穿导致均压电容电荷积累，造成断口间电压分布瞬时失衡
- 真空快速熄弧特性易在多断口结构中诱发连续重燃，增加高压设计难度



## 方法细节

### 方法概述

本文提出了一种基于EMTP®的多断口高压断路器电磁暂态仿真模型，采用集中参数电路（lumped-element model）耦合各合分闸单元(MBU)。模型核心在于分别处理关合与开断两种操作模式：关合时采用击穿电压下降曲线(RDBV)模拟预击穿(pre-strike)现象，开断时采用热恢复与介质恢复双包络线(RRBV)模拟重燃(re-ignition)与复燃(restrike)。通过开关逻辑控制理想开关与电弧阻抗的插入，考虑机械不同步性(non-simultaneity)导致的断口间电压分布瞬态失衡，特别是均压电容(grading capacitor)电荷积累效应。模型适用于SF6和真空两种介质，其中真空断路器(VCB)考虑了其快速熄弧特性导致的连续重燃现象。

### 数学公式


**公式1**: $$$U_b(t) = E_b(t) \cdot d_c(t)$$$

*帕邢定律近似，计算瞬时击穿电压，其中Eb为介质强度，dc为触点间隙*


**公式2**: $$$RDBV(t) \equiv -\frac{d}{dt}U_b(t)$$$

*关合操作击穿电压下降率(Rate of Decrease of Breakdown Voltage)*


**公式3**: $$$RDBV(t) = -\frac{d(d_c(t))}{dt} \cdot E_b \cdot \lambda(d_c)$$$

*考虑几何因子的RDBV展开式，触点速度恒定假设下推导*


**公式4**: $$$\lambda(d_c) = \frac{1}{\beta(d_c)}$$$

*几何因子λ与电场增强因子β的关系，考虑触点宏观几何与微观粗糙度*


**公式5**: $$$RRBV(t) = \frac{d(d_o(t))}{dt} \cdot E_b(t) \cdot \lambda(d_o)$$$

*开断操作击穿电压恢复率(Rate of Rise of Breakdown Voltage)，do为开断触点间距*


**公式6**: $$$U_{b,th}(t) = U_{b0} + RRBV_{th} \cdot (t - t_{extinction})$$$

*热击穿电压恢复包络线，t_extinction为电流过零熄弧时刻*


**公式7**: $$$U_{b,di}(t) = U_{b0} + RRBV_{di} \cdot (t - t_{contact\_separation})$$$

*介质击穿电压恢复包络线，从触点分离时刻(O.SCA)开始计算*


### 算法步骤

1. 初始化各MBU触点位置、速度及均压电容初始电荷状态

2. 在每个时间步长计算各断口瞬时触点间隙dc(t)或do(t)

3. 关合操作：基于RDBV计算当前击穿电压阈值Ub+(t)和Ub-(t)，考虑正负极性差异

4. 开断操作：分别计算热恢复电压Ub,th(t)和介质恢复电压Ub,di(t)两条包络线

5. 电压比较逻辑：监测各MBU端电压Uu，若|Uu|≥Ub且信号允许，触发逻辑开关信号signalint

6. 电弧建模：当signalarc为真时，在理想开关串联插入非线性电弧阻抗

7. 电荷更新：预击穿发生后，计算高频暂态电流对均压电容的充电效应，更新电容电压

8. 不同步处理：根据各MBU机械动作时间差异(Δt_non-sim)，独立计算各断口状态

9. 重燃检测：开断后若Uu超过恢复包络线，触发re-ignition/restrike信号，重新导通电弧

10. 迭代求解：采用EMTP变步长算法处理高频暂态(ns~μs级)与工频暂态(ms级)的多时间尺度问题


### 关键参数

- **RDBV**: 关合时击穿电压下降率，单位kV/ms或kV/μs，正负极性可不同

- **RRBV_th**: 热恢复率，决定电流过零后弧隙热击穿强度恢复速度

- **RRBV_di**: 介质恢复率，决定触点分离后绝缘介质强度恢复速度

- **lambda**: 几何因子(0-1)，考虑触点形状对电场的畸变效应

- **beta**: 电场增强因子，取决于触点宏观几何与微观表面粗糙度

- **Eb**: 介质强度(V/m)，关合时近似恒定，开断时随气体流动变化

- **i0**: 截流值(chopping current)，通常数安培

- **di/dt_ext**: MBU能熄灭的最大电流变化率限值

- **C_grading**: 均压电容值，典型值数百pF至数nF

- **CCT**: 断口固有寄生电容(intrinsic capacitance)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 双断口SF6断路器关合操作(机械不同步) | 首个MBU预击穿后产生高频非持续电流(持续数微秒)，导致均压电容电荷积累，第二断口出现脉冲过电压(impulse overvoltage)，幅值可达工频电压的1.5-2倍，造成电压分布临时失衡 | 传统单断口模型无法模拟断口间电压分布瞬态失衡及多次预击穿现象 |

| 真空断路器单断口开断重燃 | 由于真空介质快速熄弧特性，在电流过零后出现连续多次重燃(successive re-ignitions)，重燃频率可达数百kHz至MHz级，每次重燃伴随高频电流振荡(幅值数十至数百安培) | 传统理想开关模型仅模拟单次开断，无法复现VCB特有的高频多次重燃序列 |

| 标准极限不同步度影响分析 | 按IEC 62271-100允许的最大MBU不同步度(通常2-5ms)仿真，开断容性电流时出现3-5次连续重燃，关合空载长线时过电压幅值超过2.5p.u.(标幺值) | 传统模型假设完全同步(synchronization)，低估过电压 severity约30-40% |



## 量化发现

- 预击穿高频电流持续时间：数微秒(a few microseconds)，频率范围100kHz-10MHz
- 均压电容电荷积累导致的电压失衡：第二断口瞬时电压可达第一断口的1.8-2.2倍
- 真空断路器重燃频率：典型值500kHz-2MHz，取决于回路杂散参数Ls、Cs
- 标准允许机械不同步度：2-5ms(取决于电压等级和断路器类型)
- SF6断路器介质强度恢复率RRBV_di：通常10-50kV/ms，取决于气压和气体流动速度
- 真空断路器热恢复时间常数：微秒级(1-10μs)，远快于SF6(毫秒级)
- 电弧阻抗动态范围：导通时mΩ级，熄灭后瞬态恢复电压可达数百kV
- 模型时间步长需求：仿真高频重燃需采用10-100ns级步长，工频阶段可采用10-100μs步长


## 关键公式

### 帕邢定律近似式

$$$U_b(t) = E_b(t) \cdot d_c(t)$$$

*计算任意时刻触点间隙下的击穿电压阈值，适用于关合和开断两种操作*

### 击穿电压恢复率

$$$RRBV(t) = \frac{d(d_o(t))}{dt} \cdot E_b(t) \cdot \lambda(d_o)$$$

*开断操作中描述介质绝缘强度随触点分离速度的恢复特性，区分热恢复与介质恢复*

### 几何因子定义

$$$\lambda(d_c) = \frac{1}{\beta(d_c)}$$$

*考虑实际断路器触点非均匀电场分布，将理想平行板电场修正为实际电场*



## 验证详情

- **验证方式**: 基于EMTP®的仿真研究与理论对比，结合文献[11]中SF6断路器多次预击穿的实验观测数据进行定性验证
- **测试系统**: 多断口高压断路器模型(2-4个MBU串联)，包含均压电容网络、电源阻抗(LS+CS)、母线对地电容，电压等级245kV及以上
- **仿真工具**: EMTP®(Electromagnetic Transients Program)，采用其内置开关逻辑控制模块和变步长积分算法(Trapezoidal with Gear integration for stiffness)
- **验证结果**: 仿真成功复现了文献报道的多断口断路器在机械不同步条件下的预击穿过电压现象，以及真空断路器特有的高频连续重燃特性。模型能够准确捕捉均压电容电荷积累导致的断口间电压分布瞬态失衡，其计算的重燃次数与过电压幅值与IEC标准允许的最大不同步度条件下的理论预期一致。
