---
title: "Co-simulation applied to power systems with high penetration of distributed energy resources"
type: source
authors: ['Igor', 'Borges', 'de', 'Oliveira', 'Chagas']
year: 2022
journal: "Electric Power Systems Research, 212 (2022) 108413. doi:10.1016/j.epsr.2022.108413"
tags: ['cosimulation']
created: "2026-04-13"
sources: ["EMT_Doc/10/Chagas和Tomim - 2022 - Co-simulation applied to power systems with high penetration of distributed energy resources.pdf"]
---

# Co-simulation applied to power systems with high penetration of distributed energy resources

**作者**: Igor, Borges, de 等
**年份**: 2022
**来源**: `10/Chagas和Tomim - 2022 - Co-simulation applied to power systems with high penetration of distributed energy resources.pdf`

## 摘要

0378-7796/© 2022 Elsevier B.V. All rights reserved. Co-simulation applied to power systems with high penetration of distributed Igor Borges de Oliveira Chagas ∗, Marcelo Aroca Tomim Department of Electrical Energy, Federal University of Juiz de Fora (UFJF), MG, Brazil Although co-simulation in power systems has not been widely explored yet, it has been shown to be

## 核心贡献


- 提出基于虚构传输线的联合仿真接口，实现异质子系统的解耦与历史项数据交互
- 建立基于离散系统数值稳定性的虚构线路参数选取准则，保障仿真收敛性
- 开发基于Python的FMI主算法，实现OpenModelica与OpenDSS跨平台协同


## 使用的方法


- [[联合仿真|联合仿真]]
- [[功能模型接口-fmi|功能模型接口(FMI)]]
- [[虚构传输线法|虚构传输线法]]
- [[transmission-line-model|Bergeron线路模型]]
- [[行波理论|行波理论]]
- [[正序建模|正序建模]]
- [[相域建模|相域建模]]
- [[sundials-cvode求解器|SUNDIALS CVODE求解器]]
- [[主算法同步|主算法同步]]


## 涉及的模型


- [[输电网-11节点|输电网(11节点)]]
- [[配电网-38节点-ieee-34节点|配电网(38节点/IEEE 34节点)]]
- [[分布式能源-der|分布式能源(DER)]]
- [[静态电源与负荷|静态电源与负荷]]
- [[功能模型单元-fmu|功能模型单元(FMU)]]


## 相关主题


- [[联合仿真|联合仿真]]
- [[高渗透率分布式能源|高渗透率分布式能源]]
- [[跨平台仿真|跨平台仿真]]
- [[动态仿真|动态仿真]]
- [[计算效率优化|计算效率优化]]
- [[fmi标准|FMI标准]]


## 主要发现


- 联合仿真结果与完整系统仿真高度一致，验证了虚构线路接口方法的准确性
- 相比单一工具仿真，联合仿真架构显著降低了大规模DER系统的计算耗时
- 成功实现正序域Modelica模型与相域OpenDSS模型的无缝数据交互



## 方法细节

### 方法概述

提出一种基于功能模型接口(FMI)与虚构传输线解耦的联合仿真架构。将高渗透率DER电力系统划分为异质子系统（如正序域输电网络与相域配电网），各子系统独立建模并封装为FMU。在互联节点处引入基于Bergeron行波理论的无损耗虚构传输线，强制设定其传播延迟等于仿真固定步长，从而在相域仿真中人为重构时间延迟以实现电气解耦。主算法采用Python编写，通过PyFMI/OMSimulator调度FMU，并结合OpenDSSDirect模块实现跨平台数据交互。针对解耦引入的数值振荡风险，建立基于离散系统特征值幅值的稳定性准则，优选虚构线路特征阻抗，确保联合仿真在动态过程中的收敛性与精度。

### 数学公式


**公式1**: $$$$\begin{cases} I_k(t) = Y_c V_k(t) - H_k(t) \\ I_m(t) = Y_c V_m(t) - H_m(t) \\ H_k(t) = Y_c V_m(t-\tau) + I_m(t-\tau) \\ H_m(t) = Y_c V_k(t-\tau) + I_k(t-\tau) \end{cases}$$$$

*虚构传输线相域Bergeron模型，利用历史电流项$H$与传播延迟$\tau$实现两端子系统解耦与数据交换*


**公式2**: $$$$\mathbf{x}[n] = \mathbf{A}\mathbf{x}[n-1] + \mathbf{B}\mathbf{u}[n]$$$$

*离散时间状态空间方程，用于分析虚构线路互联系统的数值稳定性*


**公式3**: $$$$f(Z_c, \theta_c) = \sqrt{\frac{\sqrt{Z_c^2 - 2Z_c Z_k \cos(\theta_c-\theta_k) + Z_k^2} \sqrt{Z_c^2 - 2Z_c Z_m \cos(\theta_c-\theta_m) + Z_m^2}}{\sqrt{Z_c^2 + 2Z_c Z_k \cos(\theta_c-\theta_k) + Z_k^2} \sqrt{Z_c^2 + 2Z_c Z_m \cos(\theta_c-\theta_m) + Z_m^2}}}$$$$

*稳定性判据函数，要求$f(Z_c, \theta_c)<1$以保证离散系统特征值幅值小于1，指导$Z_c$参数选取*


**公式4**: $$$$NIAE = 1 - \frac{\int_0^t |x^* - x| dt}{\int_0^t x^* dt}$$$$

*归一化积分绝对误差指标，用于量化联合仿真结果与完整系统基准的吻合度*


### 算法步骤

1. 数据预处理：在OMEdit中构建子系统Modelica模型，通过OMPython导出Co-Simulation模式FMU，内置SUNDIALS CVODE求解器（BDF/Adams-Moulton方法）。

2. 初始化模式：计算互联节点戴维南等效阻抗$Z_k$与$Z_m$；代入稳定性函数$f(Z_c, \theta_c)$优选特征阻抗$Z_c$；执行初始潮流计算获取节点电压电流；若含OpenDSS，则执行OpenModelica与OpenDSS交替迭代潮流，直至PCC点电压误差$\|V_{PCC-OM} - V_{PCC-OpenDSS}\| < \varepsilon$，最后利用式(8)计算初始历史电流项。

3. 积分模式：主算法调用FMU的doStep执行单步积分；检查状态后收集历史电流输出；主算法将历史项分发至对应子系统并更新输入；时间步进$t \leftarrow t+\Delta t$。

4. 跨平台嵌套迭代（OpenDSS场景）：每步内将虚构线路转为戴维南等效，OpenDSS以固定参考电压求解配网潮流返回电流$I_m$；将$I_m$注入虚构线路计算接口电压$V_{m-Berg}$；重复迭代直至$\|V_{m-Berg} - V_{m-OpenDSS}\| < \varepsilon$，期间历史项保持恒定，收敛后推进至下一时间步。


### 关键参数

- **传播延迟**: $\tau = \Delta t$（强制等于固定通信步长）

- **特征阻抗_Case_I**: $Z_c = 0.0351 \angle 86.73^\circ$ pu（11节点+38节点系统）

- **特征阻抗_Case_II**: $Z_c = 0.0350 \angle 87.38^\circ$ pu（11节点+IEEE 34节点系统）

- **内置求解器**: SUNDIALS CVODE (BDF与Adams-Moulton隐式/显式混合)

- **通信步长**: 固定步长（与EMT仿真步长一致）

- **收敛容差**: $\varepsilon$（用于OpenModelica与OpenDSS交替潮流迭代）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 11节点输电网耦合38节点配电网（正序域） | 在母线7施加三相短路故障100ms后切除。联合仿真动态轨迹与完整系统高度重合，归一化积分绝对误差(NIAE)均大于99.5%。当接入3条及以上38节点馈线时，完整系统仿真因计算耗时过长与数值发散失败，联合仿真成功完成动态评估。 | 完整系统仿真在≥3馈线时无法收敛，联合仿真成为唯一可行方案，且计算耗时显著降低 |

| 11节点输电网耦合IEEE 34节点配电网（相域/OpenDSS） | 实现正序Modelica FMU与三相相域OpenDSS的跨平台协同。通过优选$Z_c$靠近输电侧阻抗，系统离散特征值幅值降至0.051。动态响应曲线与基准一致，NIAE>99.5%，验证了虚构线路接口在异构域间数据交互的有效性。 | 相比单一EMT环境，跨平台联合仿真架构在保持精度的同时大幅降低计算负担，特征值幅值控制在0.051以内保障强稳定性 |



## 量化发现

- 联合仿真结果与完整系统基准对比的NIAE指标均>99.5%（即相对误差<0.5%），满足高精度动态仿真要求
- 虚构线路特征阻抗$Z_c$靠近输电侧戴维南阻抗$Z_k$时，离散系统特征值幅值分别降至0.068（Case I）与0.051（Case II），严格满足$|\lambda|<1$稳定性条件
- 当系统规模扩展至3条及以上并联馈线时，传统单一工具完整系统仿真因内存与时间限制完全失效，联合仿真架构成功突破规模瓶颈
- OpenDSS与FMU接口采用戴维南等效嵌套迭代策略，有效避免了Norton等效导致的潮流发散问题，每步迭代收敛容差可控制在工程允许范围内


## 关键公式

### 虚构传输线相域解耦模型

$$$$\begin{cases} I_k(t) = Y_c V_k(t) - H_k(t) \\ I_m(t) = Y_c V_m(t) - H_m(t) \\ H_k(t) = Y_c V_m(t-\tau) + I_m(t-\tau) \\ H_m(t) = Y_c V_k(t-\tau) + I_k(t-\tau) \end{cases}$$$$

*用于在相域/正序域联合仿真中人为引入时间延迟，实现异质子系统的电气解耦与历史项数据交换*

### 离散系统稳定性判据函数

$$$$f(Z_c, \theta_c) = \sqrt{\frac{\sqrt{Z_c^2 - 2Z_c Z_k \cos(\theta_c-\theta_k) + Z_k^2} \sqrt{Z_c^2 - 2Z_c Z_m \cos(\theta_c-\theta_m) + Z_m^2}}{\sqrt{Z_c^2 + 2Z_c Z_k \cos(\theta_c-\theta_k) + Z_k^2} \sqrt{Z_c^2 + 2Z_c Z_m \cos(\theta_c-\theta_m) + Z_m^2}}}$$$$

*在初始化阶段用于指导虚构线路特征阻抗$Z_c$的极坐标选取，确保联合仿真迭代过程渐近稳定*

### 归一化积分绝对误差

$$$$NIAE = 1 - \frac{\int_0^t |x^* - x| dt}{\int_0^t x^* dt}$$$$

*用于量化评估联合仿真动态轨迹与完整系统基准的吻合程度，NIAE≥0.95即认为模型精度合格*



## 验证详情

- **验证方式**: 与单一工具完整系统仿真结果进行对比分析（基准对照法）
- **测试系统**: 11节点输电系统耦合38节点配电网（正序等效）；11节点输电系统耦合IEEE 34节点配电网（三相不平衡相域）
- **仿真工具**: OpenModelica (OMEdit/OMPython), PyFMI, OMSimulator, OpenDSS (via OpenDSSDirect Python模块), Python主算法环境
- **验证结果**: 在母线7三相短路故障动态场景下，联合仿真电压、功率及功角轨迹与完整系统高度一致（NIAE>99.5%）。成功验证了虚构传输线接口在相域解耦中的有效性，以及FMI标准在跨平台（Modelica/OpenDSS）异构模型协同中的工程可行性，显著提升了高渗透率DER系统的仿真可扩展性与计算效率。
