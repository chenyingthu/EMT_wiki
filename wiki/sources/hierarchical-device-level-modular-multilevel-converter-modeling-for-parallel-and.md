---
title: "Hierarchical Device-Level Modular Multilevel Converter Modeling for Parallel and Heterogeneous Transient Simulation of HVDC Systems"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Open Journal of Power Electronics;2020;1; ;10.1109/OJPEL.2020.3016296"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/OJPEL.2020.3016296.pdf.pdf"]
---

# Hierarchical Device-Level Modular Multilevel Converter Modeling for Parallel and Heterogeneous Transient Simulation of HVDC Systems

**作者**: 
**年份**: 2020
**来源**: `19、20、21/EMT_task_21/OJPEL.2020.3016296.pdf.pdf`

## 摘要

System-level electromagnetic transient (EMT) simulation of large-scale power converters with high-order nonlinear semiconductor switch models remains a challenge albeit it is essential for design pre- view. In this work, a multi-layer hierarchical modeling methodology is proposed for high-performance com- puting of the modular multilevel converter involving device-level IGBT/diode models. The computational burden induced by converter scale and model complexity is dramatically alleviated following the proposal of topological reconﬁguration and network equivalence, which create a substantial number of identical circuit units that facilitate massively parallel processing on the graphics processing unit (GPU), using the kernel-based single-instruction multi-threading computing architecture. As

## 核心贡献


- 提出多层级MMC建模方法，结合拓扑重构与网络等值，降低高阶IGBT计算负担
- 设计CPU/GPU异构协同架构，利用多速率仿真分离非线性器件，实现高效并行求解
- 基于GPU单指令多线程架构，将相同电路单元映射至并行内核，提升换流器仿真速度


## 使用的方法


- [[拓扑重构|拓扑重构]]
- [[网络等值|网络等值]]
- [[多速率仿真|多速率仿真]]
- [[cpu-gpu异构计算|CPU/GPU异构计算]]
- [[节点分析法|节点分析法]]
- [[伴随电路离散化|伴随电路离散化]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[igbt|IGBT]]
- [[续流二极管|续流二极管]]
- [[vsc-hvdc|VSC-HVDC]]
- [[子模块|子模块]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[异构计算|异构计算]]
- [[器件级建模|器件级建模]]
- [[高性能计算|高性能计算]]
- [[vsc-hvdc|VSC-HVDC]]


## 主要发现


- 混合CPU/GPU平台相比传统CPU实现超50倍加速，大幅缩短大规模系统仿真时间
- 方法经ANSYS/Simplorer与PSCAD/EMTDC验证，波形与精度高度吻合
- 拓扑重构与网络等值有效降低导纳矩阵维度，避免数值发散并提升电路求解效率



## 方法细节

### 方法概述

本文提出一种面向HVDC系统器件级MMC的多层级异构并行电磁暂态仿真方法。首先，基于物理机理建立高阶非线性IGBT/续流二极管模型，采用一阶隐式后向欧拉法进行离散化，推导包含电导、跨导及伴随电流源的离散时间域伴随电路，并引入虚拟节点处理非互易跨导。其次，通过拓扑重构利用耦合电压/电流源降低导纳矩阵维度，结合网络等值进一步压缩子模块节点数，生成大量结构相同的电路单元。随后，基于GPU的SIMT架构将同质化子模块计算映射至并行内核，而将直流网络等异构任务分配至CPU，实现CPU/GPU异构协同。最后，分离非线性器件与线性网络，采用多速率仿真策略，允许器件级与系统级使用不同时间步长，从而在保证器件级开关瞬态精度的同时，大幅提升大规模系统仿真效率。

### 数学公式


**公式1**: $$$$I_{ds}(V_{gs}, V_{ds}) = \begin{cases} 0, & V_{gs} \le V_{th} \\ I_{sat}(V_{gs}, V_{ds}) \cdot \left(2\frac{V_{ds}}{V_{sat}} - \frac{V_{ds}^2}{V_{sat}^2}\right), & V_{ds} \le V_{sat} \\ I_{sat}(V_{gs}, V_{ds}), & V_{ds} > V_{sat} \end{cases}$$$$

*MOSFET静态漏源电流分段模型，用于描述IGBT中MOSFET部分在截止、线性及饱和区的非线性伏安特性*


**公式2**: $$$$I_b = I_{SBJT} \left( e^{\frac{V_{be}}{M_{BJT} V_T}} - 1 \right)$$$$

*PNP-BJT基极电流方程，描述双极型晶体管部分的指数型非线性导通特性*


**公式3**: $$$$C_{xy}(V_{JNC}^*) = \begin{cases} C_0 (\kappa - 1) \cdot \left[ 1 - \exp\left( -\frac{\alpha \cdot V_{JNC}^*}{(\kappa-1)V_{diff}} \right) \right] + 1, & V_{JNC}^* \ge 0 \\ C_0 \left( \rho + \frac{1-\rho}{1 - \frac{V_{JNC}^*}{V_{diff}}} \right)^\alpha, & V_{JNC}^* < 0 \end{cases}$$$$

*寄生结电容非线性电压依赖模型，用于表征器件在增强/耗尽状态切换时的动态电荷积累与中和过程*


**公式4**: $$$$G_{ds} = \frac{\partial I_{ds}}{\partial V_{ds}}$$$$

*MOSFET输出电导，通过对漏源电流求偏导获得，是构建离散时间域伴随电路导纳矩阵的关键参数*


**公式5**: $$$$I_{dseq} = I_{ds} - G_{ds}V_{ds} - G_{ds,gs}V_{gs}$$$$

*MOSFET伴随电流源方程，将非线性支路等效为线性电导/跨导与历史电流源的并联组合，用于EMT迭代求解*


### 算法步骤

1. 1. 器件级物理建模：基于MOSFET与BJT级联结构及寄生电容/电阻，构建IGBT与续流二极管的高阶非线性连续时间数学模型，涵盖静态伏安特性、扩散电容及结电容的非线性电压依赖关系。

2. 2. 离散化与伴随电路生成：采用一阶隐式后向欧拉法对非线性微分方程进行离散，通过求偏导计算各支路电导与跨导，并推导伴随电流源，构建离散时间域等效电路。

3. 3. 虚拟节点引入：针对跨导的非互易特性（如$G_{ds,gs}$），在电路拓扑中引入虚拟节点以准确反映单向耦合关系，避免导纳矩阵不对称导致的求解错误。

4. 4. 拓扑重构与网络等值：利用耦合电压源与电流源对MMC主电路进行拓扑重构，削减系统导纳矩阵规模；对子模块内部进行网络等值，合并冗余节点，生成大量同构电路单元。

5. 5. 异构任务划分与多速率求解：将高度重复的同构子模块计算任务打包为GPU内核，利用SIMT架构并行执行；将直流网络、控制逻辑等异构任务分配至CPU；分离非线性器件与线性网络，分别采用微步长与大步长进行多速率迭代求解，并通过数据同步接口实现CPU/GPU协同。


### 关键参数

- **V_th**: MOSFET阈值电压

- **lambda**: 沟道长度调制参数

- **K**: MOSFET跨导系数，$K=\frac{\mu_n C_{ox} W_{eff}}{2 L_{eff}}$

- **I_SBJT**: BJT饱和电流系数

- **M_BJT**: BJT发射系数

- **V_T**: 热电压

- **C_0**: 参考电容值

- **alpha_kappa_rho**: 电容非线性拟合系数

- **I_Dsat**: 二极管饱和电流

- **R_Bk**: 二极管体电阻



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 大规模MMC-HVDC系统器件级EMT仿真 | 在包含大量子模块与高阶IGBT模型的直流输电系统中，采用所提CPU/GPU异构平台进行全尺度电磁暂态仿真，成功捕获开关瞬态波形，整体仿真耗时大幅缩短。 | 相比传统纯CPU串行求解器，混合平台实现超50倍加速，且电压/电流波形与商业软件高度一致。 |



## 量化发现

- 混合CPU/GPU异构平台相比传统CPU仿真实现>50倍的计算加速
- 采用一阶隐式后向欧拉法离散化，在器件级微秒/纳秒级时间步长下保持数值稳定性，无发散现象
- 拓扑重构与网络等值技术显著降低导纳矩阵维度，使GPU并行内核的线程利用率接近饱和
- 多速率仿真策略允许非线性器件与线性网络采用独立时间步长，进一步减少冗余计算


## 关键公式

### MOSFET输出电导分段表达式

$$$$G_{ds} = \frac{\partial I_{ds}}{\partial V_{ds}} = \begin{cases} 0, & V_{gs} \le V_{th} \\ \frac{\partial I_{sat}}{\partial V_{ds}}\left(\frac{2V_{ds}}{V_{sat}} - \frac{V_{ds}^2}{V_{sat}^2}\right) + 2I_{sat}\frac{V_{sat}-V_{ds}}{V_{sat}^2}, & V_{ds} \le V_{sat} \\ \frac{\partial I_{sat}}{\partial V_{ds}} = \lambda K (V_{gs}-V_{th})^{N_{FET}}, & V_{ds} > V_{sat} \end{cases}$$$$

*用于离散化过程中计算IGBT漏源极间的等效电导，是构建伴随电路导纳矩阵的核心参数*

### MOSFET伴随电流源方程

$$$$I_{dseq} = I_{ds} - G_{ds}V_{ds} - G_{ds,gs}V_{gs}$$$$

*将非线性电流源线性化为历史电流源与电导/跨导并联形式，用于每个时间步长的迭代求解*



## 验证详情

- **验证方式**: 商业仿真软件对比验证
- **测试系统**: 基于模块化多电平换流器(MMC)的高压直流输电系统，包含大量子模块及器件级IGBT/二极管模型
- **仿真工具**: ANSYS/Simplorer, PSCAD/EMTDC
- **验证结果**: 所提方法的电压、电流波形与两款商业EMT工具的仿真结果高度吻合，验证了高阶非线性模型离散化、拓扑重构及异构并行计算架构的精度与有效性。
