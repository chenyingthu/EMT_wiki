---
title: "Co-simulation applied to power systems with high penetration of distributed energy resources"
type: source
authors: ['Igor', 'Borges', 'de', 'Oliveira', 'Chagas']
year: 2022
journal: "Electric Power Systems Research"
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


<!-- deep-review:start -->
## 研究解读

### 1. 需求、对象、挑战与贡献

高渗透率分布式能源接入后，输电网、配电网、逆变器型资源和不平衡三相网络往往需要不同建模粒度与求解器：输电侧可用正序动态模型，配电侧可能更适合三相相域潮流/暂态工具。工程需求不是简单“跑得更快”，而是在保留各专用工具优势的同时，完成同一动态事件下的协同仿真。难点在于电气接口强耦合：若直接交换端口电压电流，子系统之间会形成代数环；若通信步长较大或接口阻抗选择不当，可能引入数值振荡或失稳。本文研究对象是高DER渗透电力系统的联合仿真接口，重点在输配系统或异构工具之间的动态耦合。相对已有单一仿真工具或一般FMI封装，本文的贡献是把FMI/FMUs与基于行波理论的虚构传输线接口结合起来，用历史项交换替代即时端口耦合，并讨论OpenModelica生成模型与OpenDSS之间的接口实现，从而让正序域、相域及不同软件平台可以在固定通信点协同推进。

### 2. 模型、算法与实现技术

方法核心是将整体电力系统拆分为若干子系统，各子系统用适合自身的工具建模，并通过Functional Mock-up Interface封装或由主算法调用。互联处不直接并联两个网络端口，而是插入一条无损虚构传输线。其Bergeron形式把端口电流写成端口电压乘特征导纳再减去历史电流项；历史项由对端上一通信时刻的电压、电流计算得到。这样，在当前步内每个子系统只看到本地端口边界条件，对端影响被延迟一个传播时间，代数耦合被转化为离散通信。文中将虚构线传播延迟设为通信步长，使历史项交换与主算法步进同步。接口量主要是互联节点电压、电流、历史电流项以及虚构线路特征阻抗。为避免解耦引入的数值不稳定，作者基于两侧戴维南等效阻抗和虚构线路特征阻抗建立离散系统稳定性分析，用特征值模小于1或等价判据指导Zc选择。实现上，OpenModelica/OMPython可生成Co-Simulation模式FMU，Python主算法通过PyFMI或OMSimulator调度doStep；在OpenDSS耦合场景中，配电网通过OpenDSSDirect调用，并在每个通信步内用戴维南等效和PCC电压/电流迭代实现接口一致。

### 3. 验证、优势与不足

作者采用基准对照验证：把联合仿真结果与完整系统在单一环境中的仿真轨迹比较。页面抽取记录的算例包括11节点输电系统耦合38节点配电网的正序等效场景，以及11节点输电系统耦合IEEE 34节点三相不平衡配电网的相域/OpenDSS场景；动态扰动为输电系统母线7三相短路并在100 ms后切除。工具链涉及OpenModelica、OMEdit/OMPython、PyFMI、OMSimulator、OpenDSSDirect和Python主算法。指标使用归一化积分绝对误差NIAE衡量联合仿真轨迹与完整系统基准的一致性；当前页面记录NIAE均大于99.5%，并记录虚构线路参数优化后离散特征值模分别约为0.068和0.051。优势主要体现在两点：一是虚构传输线接口使子系统在通信点之间独立求解，适合异构模型和工具耦合；二是在页面记录的多馈线扩展算例中，完整系统仿真受时间或内存限制失败，而联合仿真仍可运行。边界也很明确：验证事件较集中，主要是三相短路动态；通信步长固定且等于虚构线延迟；稳定性结论依赖接口阻抗和两侧等效阻抗；文中未由这些算例证明所有DER控制策略、故障类型、实时仿真步长或硬件在环场景均适用。

### 4. 价值、认知与可复用场景

这项工作的主要认知价值在于说明：联合仿真能否可信，不只取决于软件能否互联，更取决于电气接口是否把强耦合网络转化为稳定的离散交换问题。虚构传输线方法提供了一个可解释的接口机制：用传播延迟和历史项实现解耦，用特征阻抗选择控制数值稳定性。它适合被后续关于FMI电力系统联合仿真、输配协同动态仿真、OpenModelica-OpenDSS接口、DER高渗透率场景可扩展仿真的页面复用。工程上可用于需要同时保留输电动态模型和配电三相模型的研究原型。不宜外推为通用实时仿真框架，也不应在未重新校验阻抗、步长和接口收敛性的情况下，直接用于任意拓扑、强电力电子控制或更高频EMT现象。

### 证据边界

- 原文摘要明确说明本文提出基于虚构传输线的联合仿真，并讨论OpenModelica生成代码与OpenDSS接口；这是本页方法定位的直接证据。
- FMI、FMU、通信点离散交换以及子系统独立求解的描述来自原文引言和FMI背景说明；具体工具链细节来自当前页面抽取内容，深度引用前应核对PDF方法章节。
- NIAE大于99.5%、特征值模0.068和0.051、多馈线完整仿真失败等量化结论出现在当前页面已有抽取中；提供的摘要片段本身未报告这些可核验数值，应以原文表图为最终依据。
- 测试系统、母线7三相短路、38节点和IEEE 34节点配网等验证范围来自当前页面记录；不能据此推出其他故障、其他DER控制器或其他拓扑下同样精度。
- 虚构线路延迟等于固定通信步长、特征阻抗靠近戴维南阻抗可改善稳定性属于本文方法机制；但步长选择、容差设置和阻抗计算细节若未在页面完整呈现，需要回到原文复核。
- 本文验证主要是离线仿真与完整系统基准对比；没有从当前证据看到硬件在环、实时性约束、随机DER场景或大规模统计测试。
<!-- deep-review:end -->
## 核心贡献

- 问题定位：0378-7796/© 2022 Elsevier B.V. All rights reserved. Co-simulation applied to power systems with high penetration of distributed Igor Borges de Oliveira Chagas ∗, Marcelo 。
- 方法机制：提出一种基于功能模型接口(FMI)与虚构传输线解耦的联合仿真架构。将高渗透率DER电力系统划分为异质子系统（如正序域输电网络与相域配电网），各子系统独立建模并封装为FMU。在互联节点处引入基于Bergeron行波理论的无损耗虚构传输线，强制设定其传播延迟等于仿真固定步长，从而在相域仿真中人为重构时间延迟以实现电气解耦。
- 验证证据：与单一工具完整系统仿真结果进行对比分析（基准对照法）；11节点输电系统耦合38节点配电网（正序等效）；11节点输电系统耦合IEEE 34节点配电网（三相不平衡相域）；OpenModelica (OMEdit/OMPython), PyFMI, OMSimulator, OpenDSS (via OpenDSSDirect Python模块), Python主算法环境
- 量化与结论：联合仿真结果与完整系统基准对比的NIAE指标均>99.5%（即相对误差<0.5%），满足高精度动态仿真要求；虚构线路特征阻抗靠近输电侧戴维南阻抗时，离散系统特征值幅值分别降至0.068（Case I）与0.051（Case II），严格满足稳定性条件；当系统规模扩展至3条及以上并联馈线时，传统单一工具完整系统仿真因内存与时间限制完全失效，联合仿真架构成功突破规模瓶颈；
- 适用边界：适用于理解本文 Co-simulation applied to power systems with high penetration of distributed energy resources （2022） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。；

## 使用的方法

- [[co-simulation|联合仿真]]
- [[功能模型接口-fmi|功能模型接口(FMI)]]
- 虚构传输线法
- [[transmission-line-model|Bergeron线路模型]]
- 行波理论
- 正序建模
- [[nodal-analysis|相域建模]]
- SUNDIALS CVODE求解器
- 主算法同步

## 涉及的模型

- 输电网(11节点)
- 配电网(38节点/IEEE 34节点)
- 分布式能源(DER)
- 静态电源与负荷
- 功能模型单元(FMU)

## 相关主题

- [[co-simulation|联合仿真]]
- 高渗透率分布式能源
- 跨平台仿真
- 动态仿真
- [[large-scale-system-simulation|计算效率优化]]
- FMI标准

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

## 适用边界

### 适用条件

- 适用于理解本文 `Co-simulation applied to power systems with high penetration of distributed energy resources`（2022） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。
- 适用于以 联合仿真、功能模型接口-fmi、虚构传输线法 为核心的建模、仿真、等值、控制或稳定性分析场景；具体对象以原文算例和页面“涉及的模型”为准。
- 可作为知识图谱中的方法定位和文献入口，尤其用于追踪：提出基于虚构传输线的联合仿真接口，实现异质子系统的解耦与历史项数据交互

### 失效边界

- 不应外推到原文未覆盖的拓扑、控制策略、故障类型、频率范围、硬件平台或实时步长。
- 不应把页面中的“提高、显著、快速、准确”等概括性表述当作定量结论；只有“量化发现”和原文表图可核验的数字才可用于比较。
- 若页面作者、期刊、摘要或验证字段仍不完整，本页只能作为待复核文献入口，不能作为最终证据页引用。

### 关键假设

- 页面内容假设当前 PDF 抽取文本与 frontmatter 的 `sources` 指向同一篇论文。
- 方法结论默认受原文仿真工具、测试系统、参数设置、采样步长和对比基线约束。
- 当前边界层为保守整理：未从原文直接核验的内容不得升级为确定结论。

### 证据缺口

- 具体适用范围仍以原文算例、参数表和验证场景为准，当前页面不应外推到未验证系统。
- 源文件路径：`["EMT_Doc/10/Chagas和Tomim - 2022 - Co-simulation applied to power systems with high penetration of distributed energy resources.pdf"]`；需要深修时应优先核对该 PDF 的首页、摘要、方法和实验表图。
