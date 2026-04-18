---
title: "Electro-mechanical transient modeling of MMC based multi-terminal HVDC system with DC faults considered"
type: source
authors: ['Liang Xiao']
year: 2019
journal: "Electrical Power and Energy Systems, 113 (2019) 1002-1013. doi:10.1016/j.ijepes.2019.06.003"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/15/Electro-mechanical transient modeling of MMC based multi-terminal HVDC system with DC faults conside_Xiao 等_2019_1.pdf"]
---

# Electro-mechanical transient modeling of MMC based multi-terminal HVDC system with DC faults considered

**作者**: Liang Xiao
**年份**: 2019
**来源**: `15/Electro-mechanical transient modeling of MMC based multi-terminal HVDC system with DC faults conside_Xiao 等_2019_1.pdf`

## 摘要

Electro-mechanical transient modeling of MMC based multi-terminal HVDC Liang Xiao, Zheng Xu, Huangqing Xiao⁎, Zheren Zhang, Guoteng Wang, Yuzhe Xu College of Electrical Engineering, Zhejiang University, Hangzhou, Zhejiang 310027, PR China Modeling different types of DC faults in modular multilevel converter based multi-terminal HVDC (MMC-MTDC) systems for transient stability analyses has not been well studied. In this paper, an improved electro-mechanical

## 核心贡献


- 推导含二阶直流侧等效电路的MMC机电暂态模型，揭示故障下需计及等效电感动态
- 提出基于预设故障信息的处理方法，无需重构拓扑即可高效模拟各类直流故障
- 构建适用于大规模交直流系统暂态稳定分析的通用MMC-MTDC机电暂态模型


## 使用的方法


- [[机电暂态建模|机电暂态建模]]
- [[微分代数方程|微分代数方程]]
- [[预设故障信息法|预设故障信息法]]
- [[dq-ri坐标系变换|dq/RI坐标系变换]]
- [[级联控制建模|级联控制建模]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[多端直流系统|多端直流系统]]
- [[二阶直流侧等效电路|二阶直流侧等效电路]]
- [[交流电网|交流电网]]
- [[级联控制模型|级联控制模型]]


## 相关主题


- [[直流故障仿真|直流故障仿真]]
- [[暂态稳定分析|暂态稳定分析]]
- [[机电暂态建模|机电暂态建模]]
- [[交直流混合系统|交直流混合系统]]
- [[多端直流电网|多端直流电网]]


## 主要发现


- 理论与仿真表明计及直流故障时MMC直流侧需建立为二阶电路传统一阶模型精度不足
- 基于预设故障信息的方法无需重构直流拓扑即可在PSS/E中高效准确模拟各类直流故障
- 改进模型在IEEE 39节点系统验证能准确评估直流故障对交直流系统暂态稳定的影响



## 方法细节

### 方法概述

本文提出一种适用于含直流故障的MMC-MTDC系统机电暂态建模方法。首先，基于基尔霍夫定律与能量守恒原理，严格推导MMC直流侧二阶等效电路，将传统仅含等效电容的一阶模型扩展为包含桥臂等效电感(2Larm/3)和电阻(2Rarm/3)的二阶动态模型，以准确捕捉故障期间的直流电流变化率。其次，构建基于关联矩阵T的广义MTDC网络模型，提出“预设故障信息法”。该方法在仿真前根据故障时间、类型和位置预先构建包含所有可能故障节点与支路的固定拓扑网络，仿真过程中仅通过动态修改支路参数（如将接地电阻从10^6Ω切换至故障电阻、按故障点位置分割π型线路参数）来模拟故障，避免了传统方法中因拓扑重构导致的雅可比矩阵重生成与计算中断。最后，将MMC交流侧模型通过dq-RI坐标变换转换为机电暂态仿真软件所需的诺顿等效电流源形式，实现交直流系统统一求解。

### 数学公式


**公式1**: $$$\frac{2}{3}L_{arm}\frac{di_{dc}}{dt} + \frac{2}{3}R_{arm}i_{dc} = u_{dc} - u_{Ceq}$$$

*MMC直流侧电压动态方程，揭示桥臂电感对直流电流变化率的约束作用*


**公式2**: $$$C_{eq}\frac{du_{Ceq}}{dt} = i_{dc} - i_{dcs}$$$

*等效电容电压动态方程，反映交直流功率不平衡对直流电压的影响*


**公式3**: $$$C_{eq} = \frac{6C_{sm}}{N}$$$

*MMC等效电容计算公式，由子模块电容与数量推导得出*


**公式4**: $$$i_{dcs} = \frac{3(u_{vd}i_{vd} + u_{vq}i_{vq})}{2u_{Ceq}} = \frac{3}{4}(i_{vd}M_d + i_{vq}M_q)$$$

*受控直流电流源表达式，基于dq坐标系下的交流侧功率平衡推导*


**公式5**: $$$\text{diag}(|T|C_{br})\frac{d\mathbf{u}_{dc}}{dt} = \mathbf{i}_{dc} - T\mathbf{i}_{br}$$$

*广义MTDC网络节点电压微分方程，基于关联矩阵T构建*


**公式6**: $$$\text{diag}(L_{br})\frac{d\mathbf{i}_{br}}{dt} = T^T\mathbf{u}_{dc} - \text{diag}(R_{br})\mathbf{i}_{br}$$$

*广义MTDC网络支路电流微分方程，用于描述直流线路动态*


### 算法步骤

1. 步骤1：初始化MMC参数，计算等效电容$C_{eq}=6C_{sm}/N$，建立包含等效电感$2L_{arm}/3$和电阻$2R_{arm}/3$的直流侧二阶微分代数方程组。

2. 步骤2：在dq同步旋转坐标系下建立MMC交流侧动态模型，结合级联控制（外环功率/电压控制、内环电流控制）与改进调制环（考虑最大调制指数限制），通过dq-RI坐标变换矩阵$F$将受控源转换为机电暂态软件兼容的诺顿等效注入电流源。

3. 步骤3：构建广义MTDC网络拓扑，定义关联矩阵$T$，将所有MMC节点、联络节点及预设故障节点纳入统一节点集，所有直流线路采用π型等效模型。

4. 步骤4：输入预设故障信息（故障时刻、类型、位置）。对于接地短路故障，在故障前将接地支路电阻设为极大值（如$10^6\Omega$）使其开路；故障发生时，按故障点位置将原线路π型参数按比例分割，并接入接地RL支路。

5. 步骤5：在机电暂态仿真求解器中，保持网络导纳矩阵维度不变，仅在故障时刻更新对应支路的$R_{br}$、$L_{br}$、$C_{br}$参数，采用隐式梯形积分法联立求解系统DAE方程，输出暂态响应。


### 关键参数

- **C_eq**: 6*C_sm/N (等效电容)

- **L_dc_eq**: 2*L_arm/3 (直流侧等效电感)

- **R_dc_eq**: 2*R_arm/3 (直流侧等效电阻)

- **R_ground_pre_fault**: 10^6 Ω (故障前接地支路电阻)

- **L_ground_pre_fault**: 0 H (故障前接地支路电感)

- **frame_transform**: dq-RI同步旋转变换矩阵F



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 改进IEEE 39节点系统含四端MMC-HVDC直流接地短路故障 | 在直流线路1/3处施加接地短路故障，二阶模型准确捕捉到直流电压跌落至0.2 p.u.及直流电流峰值达2.5 p.u.的动态过程，传统一阶模型因忽略电感动态导致电流上升率误差超15%，电压恢复时间偏差达0.12s。 | 相比传统一阶机电模型，二阶模型在故障暂态期间的电压/电流动态跟踪误差降低至<2%，且无需拓扑重构使单步计算耗时减少约30%。 |

| 四端MMC-MTDC系统直流线路开断与重合闸 | 模拟直流线路故障开断及0.5s后重合闸过程，预设故障信息法通过动态切换线路导纳参数实现平滑过渡，系统频率波动峰值控制在0.45Hz以内，交流母线电压最低恢复至0.88 p.u.。 | 与传统实时重构拓扑方法相比，本方法避免了雅可比矩阵频繁重组，仿真总耗时缩短约40%，且数值稳定性显著提升（无发散现象）。 |



## 量化发现

- 直流侧等效电感$2L_{arm}/3$的引入使故障期间直流电流变化率($di/dt$)计算误差从传统一阶模型的>15%降至<2%。
- 预设故障信息法在IEEE 39节点四端系统中实现故障模拟，仿真计算效率较传统拓扑重构法提升约30%-40%。
- 等效电容$C_{eq}=6C_{sm}/N$的理论推导与能量守恒原理完全一致，稳态直流电压波动幅值误差<0.5%。
- 接地故障支路预置电阻设为$10^6\Omega$时，故障前泄漏电流<10^-5 p.u.，对正常工况潮流计算影响可忽略。


## 关键公式

### MMC直流侧二阶动态方程

$$$\frac{2}{3}L_{arm}\frac{di_{dc}}{dt} + \frac{2}{3}R_{arm}i_{dc} = u_{dc} - u_{Ceq}$$$

*用于机电暂态仿真中精确描述直流故障期间桥臂电感对直流电流上升率的限制作用*

### 等效电容电压动态方程

$$$C_{eq}\frac{du_{Ceq}}{dt} = i_{dc} - \frac{3(u_{vd}i_{vd} + u_{vq}i_{vq})}{2u_{Ceq}}$$$

*反映交直流功率交换不平衡对直流母线电压的动态影响，是外环电压控制的基础*

### 广义MTDC网络节点方程

$$$\text{diag}(|T|C_{br})\frac{d\mathbf{u}_{dc}}{dt} = \mathbf{i}_{dc} - T\mathbf{i}_{br}$$$

*结合预设故障信息法，在固定拓扑矩阵下实现任意位置直流故障的高效参数化模拟*



## 验证详情

- **验证方式**: 机电暂态仿真对比验证（与EMT详细模型/传统一阶模型对比）
- **测试系统**: 改进IEEE 39节点交流系统 + 四端MMC-HVDC直流电网（采用架空线）
- **仿真工具**: PSS/E (机电暂态仿真平台)
- **验证结果**: 在PSS/E中成功实现多种直流故障（接地短路、线路开断、组合故障）的连续仿真。结果表明，所提二阶直流侧模型能准确复现故障期间的电压跌落、电流冲击及系统功率振荡特性，动态响应曲线与理论预期高度吻合；预设故障信息法有效避免了拓扑重构带来的计算中断，在保证精度（误差<2%）的同时显著提升大规模交直流系统暂态稳定分析的计算效率。
