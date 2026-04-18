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



## 方法细节

### 方法概述

本文提出一种基于虚拟阻抗补偿的永磁同步发电机(PMSG)恒导纳建模方法。针对传统相域(PD)模型在电磁暂态仿真中因转子位置角变化导致导纳矩阵时变、需频繁求逆而计算量大的问题，该方法在发电机转子侧引入虚拟阻抗，补偿导纳矩阵中的时变耦合分量，使等效导纳矩阵保持恒定。同时，机网侧换流器采用伴随离散电路(ADC)模型，通过合理选取等效L、C、R参数，使开关状态切换不影响网络导纳。以暂态误差最小化为目标对虚拟阻抗参数进行优化设计，最终构建完整的PMSG恒导纳模型。该模型结合隐式梯形积分法离散化，将时变网络转化为固定导纳并联历史电流源的诺顿等效形式，彻底避免了仿真过程中的实时矩阵求逆运算，显著降低计算复杂度，适用于FPGA等实时硬件平台的大规模新能源系统仿真。

### 数学公式


**公式1**: $$$u_{abc}(t) = -(r_s + \frac{2}{\Delta t} L_{ss}(t)) i_{abc}(t) + \frac{2}{\Delta t} L_{sr}(t) i_{dq}(t) + e_{sh}(t)$$$

*定子端三相电压离散方程，表示当前时刻电压与定子/转子电流及历史电压源的关系*


**公式2**: $$$i_{dq}(t) = (r_r + \frac{2}{\Delta t} L_{rr})^{-1} (\frac{2}{\Delta t} L_{rs}(t) i_{abc}(t) - e_{rh}(t))$$$

*转子阻尼绕组电流离散方程，用于消去转子状态变量*


**公式3**: $$$u_{abc}(t) = -r_{eq}(t) i_{abc}(t) + e_h(t)$$$

*发电机外部网络接口诺顿等效方程，$r_{eq}(t)$为时变等效阻抗矩阵，$e_h(t)$为历史电动势*


**公式4**: $$$r_{eq}(t) = r_s + \frac{2}{\Delta t} L_{ss}(t) - \frac{4}{\Delta t^2} L_{sr}(t) (r_r + \frac{2}{\Delta t} L_{rr})^{-1} L_{rs}(t)$$$

*时变等效阻抗矩阵完整表达式，包含定子阻抗、定子电感项及定转子耦合三重矩阵乘积项*


**公式5**: $$$Y_{eq} = \frac{\Delta t}{2L} = \frac{2C}{2CR + \Delta t}$$$

*ADC模型开关等效导纳公式，通过参数匹配使开关导通/关断状态下的等效导纳保持一致*


### 算法步骤

1. 建立PMSG相域(PD)数学模型，包含定子/转子电压方程与磁链耦合方程，明确无励磁绕组下的永磁体磁链补偿项。

2. 采用隐式梯形积分法对连续微分方程进行离散化处理，推导定子端电压与转子电流的差分表达式，引入仿真步长$\Delta t$。

3. 消去磁链变量，整理得到发电机外部网络接口的诺顿等效形式$u_{abc}(t) = -r_{eq}(t) i_{abc}(t) + e_h(t)$，识别出含转子位置角$\theta$的时变阻抗矩阵$r_{eq}(t)$。

4. 将时变阻抗矩阵分解为定子固定阻抗项与转子耦合时变项，在转子侧引入虚拟阻抗$Z_{vd}, Z_{vq}$进行补偿，使总等效导纳矩阵$Y_{fixed}$保持恒定。

5. 以暂态仿真误差最小为目标函数，采用数值优化算法求解虚拟阻抗的最优参数值，确保补偿后模型动态特性与原模型高度一致。

6. 对机网侧换流器应用伴随离散电路(ADC)模型，配置开关导通/关断的等效L、C、R参数，确保开关动作不改变网络导纳，并生成对应的历史电流源$I_h(t)$。

7. 将恒导纳发电机模型与恒导纳换流器模型级联，构建完整PMSG恒导纳网络，在FPGA或实时仿真器中通过固定导纳矩阵求解与历史源更新实现高效迭代计算。


### 关键参数

- **$\Delta t$**: 电磁暂态仿真步长（通常取$10\mu s \sim 50\mu s$）

- **$r_s, r_r$**: 定子与转子绕组电阻对角矩阵

- **$L_{ss}, L_{rr}, L_{sr}, L_{rs}$**: 定子/转子自感矩阵与定转子互感矩阵（随转子位置角$\theta$变化）

- **$Y_{eq}$**: ADC开关等效导纳（恒定值）

- **$Z_{vd}, Z_{vq}$**: 优化后的d轴与q轴虚拟补偿阻抗参数

- **$L, C, R$**: ADC模型中开关导通等效电感、关断等效电容与串联电阻



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 单机PMSG风速阶跃与电压跌落测试 | 在风速从10m/s阶跃至12m/s及电网电压跌落至0.8p.u.工况下，对比恒导纳模型与传统PD模型的定子电流、直流母线电压及电磁转矩响应曲线。 | 动态响应曲线重合度达99.6%，暂态峰值电流偏差<0.75%，直流电压超调量误差<0.5%，计算耗时降低约87.5%。 |

| 20机风电场接入IEEE 39节点系统实时仿真 | 构建含20台PMSG的风电场并网系统，在FPGA硬件平台上进行长时暂态仿真，验证模型在大规模网络中的计算效率与数值稳定性。 | 单步网络求解时间从传统变导纳模型的1.2ms降至0.15ms，仿真加速比达8倍，成功满足$50\mu s$步长下的实时性要求，资源占用率<35%。 |



## 量化发现

- 恒导纳模型避免了导纳矩阵实时求逆，单步计算时间降低约87.5%（从1.2ms降至0.15ms）。
- 暂态仿真误差控制在0.8%以内，关键电气量（定子电流、直流母线电压）动态响应与传统变导纳模型高度一致。
- 模型在FPGA硬件平台上实现，逻辑资源占用率低于35%，支持$50\mu s$仿真步长下的实时运行。
- 虚拟阻抗补偿后，导纳矩阵条件数改善，数值稳定性提升，长时仿真（>10s）无累积发散现象。


## 关键公式

### 时变等效阻抗矩阵方程

$$$r_{eq}(t) = r_s + \frac{2}{\Delta t} L_{ss}(t) - \frac{4}{\Delta t^2} L_{sr}(t) (r_r + \frac{2}{\Delta t} L_{rr})^{-1} L_{rs}(t)$$$

*用于识别传统PD模型中导致导纳矩阵时变的核心项，是虚拟阻抗补偿设计的基准对象*

### 发电机外部网络接口方程

$$$u_{abc}(t) = -r_{eq}(t) i_{abc}(t) + e_h(t)$$$

*将发电机等效为阻抗与历史电压源串联形式，是构建恒导纳诺顿等效网络的基础*

### ADC开关等效导纳匹配方程

$$$Y_{eq} = \frac{\Delta t}{2L} = \frac{2C}{2CR + \Delta t}$$$

*用于配置换流器开关的L、C、R参数，确保开关状态切换时网络导纳保持恒定*



## 验证详情

- **验证方式**: 数字仿真对比验证与FPGA硬件在环测试
- **测试系统**: 单机PMSG系统及含20台机组的风电场接入IEEE 39节点测试系统
- **仿真工具**: MATLAB/Simulink（离线高精度基准模型）, 自定义EMT求解器（恒导纳算法实现）, FPGA开发平台（实时硬件验证）
- **验证结果**: 恒导纳模型在多种暂态工况下均保持高精度，计算效率显著提升，成功部署于离散硬件平台，验证了其在大规模新能源实时仿真中的工程适用性与实时性优势。
