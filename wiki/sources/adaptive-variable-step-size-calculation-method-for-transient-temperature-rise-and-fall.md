---
title: "Adaptive Variable Step Size Calculation Method for Transient Temperature Rise and Fall of Oil Immersed Transformers"
type: source
authors: ['CNKI']
year: 2024
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Liu 等 - 2024 - Adaptive Variable Step Size Calculation Method for Transient Temperature Rise and Fall of Oil Immers.pdf"]
---

# Adaptive Variable Step Size Calculation Method for Transient Temperature Rise and Fall of Oil Immersed Transformers

**作者**: CNKI
**年份**: 2024
**来源**: `05/Liu 等 - 2024 - Adaptive Variable Step Size Calculation Method for Transient Temperature Rise and Fall of Oil Immers.pdf`

## 摘要

In response to the problem of low efficiency in calculating transient temperature rise of oil immersed power transformers, this paper proposes POD-αATS reduced order adaptive variable step size transient calculation method. First, the article briefly derives the finite element discrete equation for calculating the transient temperature rise of transformer windings. Next, the proper orthogonal decomposition (POD) order reduction algorithm is adopted to improve the problems of excessive number of conditions and equation orders in traditional transient calculations. Meanwhile, for the time step selection problem in transient calculations, this paper proposes a method suitable for nonlinear problems α ATS (adaptive time stepping based on α factor, αATS) variable step size strategy. Then, in or

## 核心贡献


- 提出POD降阶算法，有效降低有限元方程阶数与条件数，提升单步求解效率。
- 提出αATS自适应变步长策略，结合收敛速率因子动态优化非线性瞬态步长。
- 构建POD-αATS耦合计算方法，实现流热耦合场高精度快速瞬态求解。


## 使用的方法


- [[有限元法|有限元法]]
- [[本征正交分解-pod|本征正交分解(POD)]]
- [[降阶建模|降阶建模]]
- [[αats自适应变步长算法|αATS自适应变步长算法]]
- [[奇异值分解|奇异值分解]]
- [[流热耦合计算|流热耦合计算]]


## 涉及的模型


- [[油浸式电力变压器|油浸式电力变压器]]
- [[变压器绕组|变压器绕组]]
- [[二维八分区流热耦合模型|二维八分区流热耦合模型]]
- [[有限元离散模型|有限元离散模型]]


## 相关主题


- [[瞬态温升计算|瞬态温升计算]]
- [[降阶算法|降阶算法]]
- [[自适应时间步长|自适应时间步长]]
- [[流热耦合仿真|流热耦合仿真]]
- [[热点温度预测|热点温度预测]]
- [[快速数值计算|快速数值计算]]


## 主要发现


- 算法精度与全阶定步长法一致，流场计算效率提升约45倍，大幅缩短耗时。
- 温度场计算效率提升约38倍，有效克服传统变步长法在非线性问题中的不稳定性。
- 温升实验验证了该方法的准确性与高效性，证明其具备工程实际应用价值。



## 方法细节

### 方法概述

本文提出POD-αATS降阶自适应变步长瞬态计算方法，用于解决油浸式变压器流热耦合瞬态温升计算中方程阶数高、条件数大及固定步长效率低的问题。首先基于有限元法推导流场与温度场的离散控制方程；随后引入本征正交分解（POD）算法，通过对历史快照矩阵进行奇异值分解提取主导模态，构建低维正交基，将原高维系统投影至低阶子空间，大幅降低矩阵阶数并改善病态条件数；针对非线性瞬态过程，提出αATS变步长策略，结合绝对-相对混合误差判据与基于收敛速率的α因子动态修正时间步长，在物理场剧烈变化阶段自动缩小步长以保证精度，在平缓阶段放大步长以提升效率。最终将POD降阶模型与αATS步长控制深度耦合，实现高精度、高效率的瞬态求解。

### 数学公式


**公式1**: $$$KX^{n+1} = LX^n + B$$$

*有限元离散后的瞬态控制方程一般形式，K、L为刚度矩阵，X为解向量，B为右端项，用于描述系统状态随时间步进演化。*


**公式2**: $$$\max_i (e_i^{n+1} - \varepsilon_R |X^{n+1}| - \varepsilon_A) < 0$$$

*绝对-相对混合误差判据，用于判断当前步长下的截断误差是否满足精度要求，避免单一绝对误差在变量幅值变化大时失效。*


**公式3**: $$$\alpha = \max_n \frac{\|u^n - u^{n-1}\|}{\|u^{n-1} - u^{n-2}\|}$$$

*非线性收敛速率因子α，通过相邻时间步解的变化率比值反映物理场非线性剧烈程度，α>1时表明变化加剧需缩小步长。*


**公式4**: $$$\Delta t^{n+1} = \alpha_{ref} \cdot \Delta t^n \times \min\left(S \frac{\varepsilon_R |X_{node}^{n+1}| + \varepsilon_A}{\max(e_{node}^{n+1}, ZEPS)}, r_{max}\right)$$$

*引入α因子修正后的成功步长更新公式，结合误差容限与收敛速率动态调整下一步长，保证非线性瞬态计算的稳定性与效率。*


**公式5**: $$$\text{cond}(G) = \frac{\sigma_{max}(G)}{\sigma_{min}(G)}$$$

*矩阵条件数计算公式，POD降阶通过最大化最小奇异值显著降低条件数，从而改善有限元方程的病态特性，提升迭代收敛稳定性。*


### 算法步骤

1. 初始化与快照采集：设定初始固定时间步长进行若干步瞬态计算，收集流场与温度场的状态变量快照矩阵。

2. POD降阶建模：对快照矩阵执行奇异值分解（SVD），截取前d个最大奇异值及其对应的左奇异向量构成正交基矩阵，将原高维有限元方程投影至低维子空间，生成降阶系统模型。

3. 步长初始化与状态求解：设定初始时间步长$\Delta t^n$，利用降阶模型计算当前时刻状态向量$X^n$。

4. 误差与收敛因子计算：基于泰勒展开的一阶与二阶精度解差值估算截断误差$e^{n+1}$，同时利用连续三步的解计算非线性收敛速率因子$\alpha$。

5. 混合误差判据校验：将截断误差代入绝对-相对混合判据。若不满足（误差超限），判定为失败时步，按回退公式缩小步长并重新计算当前步；若满足，进入下一步。

6. 自适应步长更新：根据校验结果与$\alpha$因子，利用修正后的ATS公式计算下一时间步长$\Delta t^{n+1}$，并限制在$[r_{min}, r_{max}]$范围内，随后推进至下一时刻循环求解，直至达到稳态或总仿真时间。


### 关键参数

- **保守系数S**: 0.8~0.9

- **步长放大上限r_max**: 4

- **步长缩小下限r_min**: 0.8

- **机器零近似ZEPS**: 防止分母为零或步长异常放大导致计算不稳定

- **初始时间步长**: 0.02 s

- **流场POD保留模态数**: 20

- **温度场POD保留模态数**: 15

- **相对误差容限ε_R**: 根据工程精度需求设定

- **绝对误差容限ε_A**: 根据工程精度需求设定



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 二维八分区绕组数值模型瞬态仿真 | 基于110kV变压器绕组结构建立二维流热耦合模型，总仿真时间2000s。流场节点数从1,019,216降至20阶，温度场从846,211降至15阶。流场计算时步由100步减至16步，温度场由200步减至18步。流场总计算时间从42,665.4s降至937.28s，温度场从107,221.87s降至2,818.08s。 | 流场计算效率提升约45倍，温度场计算效率提升约38倍；与全阶定步长算法相比，最大绝对误差仅0.2638 K（相对误差1.22%），精度几乎一致。 |

| 110kV变压器绕组温升实验验证 | 搭建包含空心无感绕组、强迫油循环系统的实验平台，油流量14.4 m³/h，输入功率25.0004 kW。记录70个时间点数据，对比12、20、30、38线饼共多个测温点。全阶算法计算耗时573.66 h（2760步），POD-αATS算法耗时10.91 h（58步）。 | 实验验证下计算效率提升约52.58倍；算法结果与实验数据最大绝对误差为3.17 K，与全阶定步长结果的最大偏差均不超过0.50 K，充分验证工程实用性。 |



## 量化发现

- POD降阶使流场方程阶数从1,019,216降至20，温度场从846,211降至15，单步求解时间分别缩短约137,008倍和36,967倍。
- 引入POD后有限元刚度阵条件数显著降低，例如步长0.02s时，条件数从$2.04\times10^{11}$降至$8.17\times10^6$，有效避免变步长过程中的计算发散。
- αATS策略使流场计算时步从100步优化至16步，温度场从200步优化至18步，大幅消除时步冗余。
- 数值模型中，POD-αATS与全阶定步长算法的流场最大相对误差为0.54%，温度场最大相对误差为1.22%。
- 实验验证中，算法预测热点温度与实测值最大偏差为3.17 K，全阶与降阶结果间最大偏差<0.50 K。
- 整体瞬态计算效率在数值算例中提升38~45倍，在复杂实验模型中提升52.58倍，同时保持与全阶方法一致的精度。


## 关键公式

### 非线性收敛速率因子α

$$$\alpha = \max_n \frac{\|u^n - u^{n-1}\|}{\|u^{n-1} - u^{n-2}\|}$$$

*用于量化瞬态过程中物理场变化的剧烈程度，作为自适应步长调整的核心修正因子，适用于强非线性流热耦合问题。*

### POD-αATS自适应步长更新公式

$$$\Delta t^{n+1} = \alpha_{ref} \cdot \Delta t^n \times \min\left(S \frac{\varepsilon_R |X_{node}^{n+1}| + \varepsilon_A}{\max(e_{node}^{n+1}, ZEPS)}, r_{max}\right)$$$

*在满足混合误差判据的成功时步中，结合α因子动态放大或缩小下一步长，平衡计算精度与效率。*



## 验证详情

- **验证方式**: 数值仿真对比与物理温升实验验证
- **测试系统**: 110 kV油浸式电力变压器二维八分区导向绕组模型及实体温升实验平台（含空心无感绕组、强迫油循环系统、热电偶测温阵列）
- **仿真工具**: MATLAB R2021a（自主编程实现POD-αATS算法），硬件配置Intel Core i9-12900KF CPU，128 GB内存
- **验证结果**: 数值计算与实验结果高度吻合。POD-αATS算法在流场和温度场中均保持与全阶定步长法几乎相同的精度（最大偏差<0.5 K），同时将计算效率提升38~52倍，条件数降低5个数量级，有效克服了传统变步长法在非线性大规模有限元计算中的不稳定与低效问题，具备显著的工程应用价值。
