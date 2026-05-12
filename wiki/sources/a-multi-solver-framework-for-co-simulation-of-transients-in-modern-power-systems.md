---
title: "A multi-solver framework for co-simulation of transients in modern power systems"
type: source
authors: ['Janesh Rupasinghe']
year: 2023
journal: "Electric Power Systems Research"
tags: ['cosimulation']
created: "2026-04-13"
sources: ["EMT_Doc/02/Rupasinghe 等 - 2023 - A multi-solver framework for co-simulation of transients in modern power systems.pdf"]
---

# A multi-solver framework for co-simulation of transients in modern power systems

**作者**: Janesh Rupasinghe
**年份**: 2023
**来源**: `02/Rupasinghe 等 - 2023 - A multi-solver framework for co-simulation of transients in modern power systems.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. A multi-solver framework for co-simulation of transients in modern Janesh Rupasinghe a, Shaahin Filizadeh b,*, Dharshana Muthumuni c, Ramin Parvari b b Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB R3T 5V6, Canada c Manitoba Hydro International, Winnipeg, MB R3P 1A3, Canada


<!-- deep-review:start -->
## 研究解读

### 1. 需求、对象、挑战与贡献

现代电网的暂态不再是单一时间尺度问题：故障附近、MMC-HVDC和电力电子装置会产生微秒级高频EMT过程，而远离扰动的交流网络可能只需毫秒级正序暂态稳定描述。若全网用EMT求解，118节点这类规模已计算昂贵；若只用TS或普通动态相量，又会丢失局部快速波形、接口延迟和非线性暂态。本文研究对象是含MMC-HVDC的现代电力系统暂态协同仿真。其贡献不是简单把EMT与TS拼接，而是提出按设备类型、扰动电气距离、所需频带和研究目的划分网络的多求解器框架：EMT1处理持续高频区域，EMT2处理中频区域，BFAST在EMT与基频动态相量间自适应切换，DP作缓冲层，TS处理远端低频网络，并围绕工业级PSCAD/EMTDC实现多接口耦合。

### 2. 模型、算法与实现技术

框架的核心实现是“分区—选求解器—接口交换”。EMT子系统保留三相瞬时电压电流；DP/BFAST用基频动态相量压缩或重构波形；TS子系统使用正序相量和较大步长。BFAST的机制是通过基频动态相量重构式x(t−T+s)=Re(<X>_B(t)e^{jω_s(t−T+s)})在相量状态与瞬时波形间转换，并根据网络状态调整频移参数ω_s和步长，使节点导纳矩阵Y=f(Δt,ω_s)随模式切换更新。接口方面，EMT与外部区域可用无损Bergeron传输线显式耦合，利用h_M(t)=2v_K(t−τ)/Z_C−h_K(t−τ)把传播延时作为物理延时处理，从而避免额外一步计算滞后。DP与TS之间采用MATE思想：各子系统先独立求局部解，将TS正序量插值并转为三相接口量，再由戴维南等效计算联络支路电流I_α=Z_α^{-1}e_α，注入接口节点完成同步或中间步耦合。

### 3. 验证、优势与不足

作者用改进IEEE 118节点系统验证框架，母线62处发电机被替换为300 MW、230 kV侧、400 kV直流母线的MMC-HVDC系统；核心EMT仿真器为PSCAD/EMTDC，BFAST、DP和TS求解器由外部C++程序实现。验证方式是把多求解器协同仿真与PSCAD/EMTDC独立全EMT基准进行波形和计算时间比较，并考察母线47处0.2 s单相接地故障下各子系统接口波形、BFAST模式切换和耗时。页面给出的可核验量化结果包括：10 s仿真从全EMT的1126 s降至88 s，约12.8倍；相对多速率纯EMT的358 s约4.07倍；TS步长5 ms，相对10 μs EMT步长为500倍。优势主要来自把远端低频网络交给TS/DP、把高频区域保留在EMT、并用Bergeron和MATE降低接口延迟。从验证范围看，结论主要限于该118节点算例、该故障、该MMC参数和离线仿真平台；未显示对多故障类型、保护动作、强非线性控制失稳、实时仿真约束或更大系统的系统性统计验证。

### 4. 价值、认知与可复用场景

这项工作的关键认知是：现代电网暂态仿真不必在“全EMT精确但慢”和“TS快速但粗”之间二选一，可以按频率内容和电气距离构造分层求解生态，并让接口算法决定整体可信度。它适合被后续关于EMT-TS协同仿真、动态相量缓冲层、频率自适应暂态仿真、MMC-HVDC大系统等页面复用，尤其可作为多速率分区与接口设计的文献入口。工程上可用于离线暂态研究中减少远端网络计算负担。不适合直接外推为任意拓扑、任意换流器控制、任意实时步长或所有暂态类型下都同样准确高效。

### 证据边界

- 原文摘要明确说明框架结合EMT、动态相量、暂态稳定和基频动态相量FAST，并以改进118节点含MMC-HVDC系统验证；这是确定证据。
- EMT1、EMT2、BFAST、DP、TS的分区逻辑和步长参数来自页面抽取内容；若用于正式引用，应回查原文第2节、表格和算例设置。
- 1126 s、358 s、88 s、12.8倍、4.07倍等耗时数字来自当前页面抽取结果；本次提供的原文片段未展示结果表，因此需要对PDF结果章节复核。
- 接口公式Bergeron与MATE的机制可由页面公式解释，但“零额外时间步延迟”和“波形基本一致”只在给定接口和算例中成立，不能推断所有接口都稳定无误差。
- 验证场景集中在改进IEEE 118节点和一次单相接地故障；缺少多故障位置、多扰动类型、参数敏感性、控制器差异和更大规模系统的公开统计结果。
- 论文围绕工业级PSCAD/EMTDC与外部C++求解器实现；其效率结论受硬件、软件实现、分区方式和通信开销影响，不应直接等同于其他仿真平台或实时仿真器性能。
<!-- deep-review:end -->
## 核心贡献

- 问题定位：0378-7796/© 2023 Elsevier B.V. All rights reserved. A multi-solver framework for co-simulation of transients in modern Janesh Rupasinghe a, Shaahin Filizadeh b, , Dharsha。
- 方法机制：提出一种多求解器、多速率协同仿真框架，将现代电网按设备类型、精度需求、扰动电气距离及研究目的划分为五类子系统：EMT1（高频暂态，微秒级步长）、EMT2（中频暂态，数十微秒步长）、BFAST（自适应切换EMT/动态相量）、DP（动态相量缓冲，大固定步长）和TS（暂态稳定，毫秒级正序步长）。框架以工业级PSCAD/EMTDC为核心，外部C++程序实现BFAST、DP和TS求解器。
- 验证证据：协同仿真对比验证（与PSCAD/EMTDC独立全EMT基准仿真进行波形与耗时对比）；改进型IEEE 118节点测试系统（母线62发电机替换为300 MW MMC-HVDC系统）；PSCAD/EMTDC（核心EMT求解器）、Microsoft Visual Studio C++（外部BFAST/DP/TS求解器）、内置协同仿真组件与MATE算法
- 量化与结论：秒仿真计算时间由1126 s大幅缩减至88 s，整体加速比达12.8倍。；相较于多速率纯EMT仿真（358 s），计算效率提升约4.07倍。；TS求解器采用5 ms步长，为传统EMT步长(10 μs)的500倍，显著降低稳态计算负荷。；跨域接口波形误差基本不可察觉(essentially identical)，在Bergeron传输线接口下实现零时间步延迟补偿。
- 适用边界：适用于理解本文 A multi-solver framework for co-simulation of transients in modern power systems （2023） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。；

## 使用的方法

- [[multirate-method|多速率仿真]]
- [[dynamic-phasor|动态相量法]]
- 频率自适应暂态仿真
- 暂态稳定求解
- 协同仿真接口技术

## 涉及的模型

- [[mmc-model|MMC]]
- [[power-electronics|电力电子变换器]]
- [[average-value-model|平均值模型]]
- 118节点测试系统

## 相关主题

- [[co-simulation|协同仿真]]
- [[multirate-method|多速率仿真]]
- [[multirate-method|频率自适应仿真]]
- [[emt-simulation|电磁暂态仿真]]
- [[transient-stability-analysis|暂态稳定]]
- [[parallel-computing|网络分区]]

## 主要发现

- 在含MMC-HVDC的118节点系统中验证了框架的精度与计算效率优势
- 动态相量缓冲区有效隔离了EMT与暂态稳定求解器，提升了数值稳定性
- BFAST求解器能根据暂态频率自动切换步长，显著降低稳态计算耗时

## 方法细节

### 方法概述

提出一种多求解器、多速率协同仿真框架，将现代电网按设备类型、精度需求、扰动电气距离及研究目的划分为五类子系统：EMT1（高频暂态，微秒级步长）、EMT2（中频暂态，数十微秒步长）、BFAST（自适应切换EMT/动态相量）、DP（动态相量缓冲，大固定步长）和TS（暂态稳定，毫秒级正序步长）。框架以工业级PSCAD/EMTDC为核心，外部C++程序实现BFAST、DP和TS求解器。通过电气网络接口(ENI)、无损Bergeron传输线模型（显式耦合与延迟补偿）以及多区域戴维南等效(MATE)方法实现跨域接口交互。BFAST求解器基于基频动态相量(BFDP)理论，通过调节频移参数和步长在EMT与DP模式间自动切换，兼顾全频段精度与计算效率。

### 数学公式

**公式1**: $$$x(t - T + s) = \text{Re}\left( \langle X \rangle_B(t) e^{j\omega_s(t-T+s)} \right)$$$

*基频动态相量(BFDP)信号重构公式，将全谐波频谱压缩为单一频移相量，用于BFAST求解器的数学基础*

**公式2**: $$$Y = f(\Delta t, \omega_s)$$$

*网络节点导纳矩阵依赖关系式，表明导纳矩阵随仿真步长和频移参数动态变化，是模式切换的核心依据*

**公式3**: $$$h_M(t) = \frac{2v_K(t-\tau)}{Z_C} - h_K(t-\tau)$$$

*Bergeron传输线接口电流公式，用于EMT侧边界数据注入，利用波传播时间实现无延迟显式耦合*

**公式4**: $$$I_\alpha(i) = Z_\alpha^{-1} e_\alpha(i)$$$

*MATE方法联络支路电流计算公式，用于DP与TS子系统间的解耦并行求解，消除大时间步限制*

### 算法步骤

1. 在$t=t_k$时刻，独立求解TS子系统在$t_k$的局部解（不含联络支路）与DP子系统在中间时刻$t_i$的局部解。

2. 将TS子系统的局部解线性插值至$t_i$，并将正序相量转换为三相形式以匹配DP子系统的三相接口需求。

3. 基于DP与插值后的TS局部解，分别计算两子系统的戴维南等效电压，进而求解联络支路电流向量$I_\alpha(i) = Z_\alpha^{-1} e_\alpha(i)$。

4. 将计算得到的$I_\alpha(i)$注入DP子系统接口节点并独立求解完整状态，该过程在DP子系统的每个中间时刻$t_i$重复执行。

5. 到达$t=t_k$时，重新计算接口电流并同步注入DP与TS子系统，并行求解两子系统的完整网络状态，实现无时间步延迟的精确耦合。

### 关键参数

- **Δt_EMT1**: 10 μs

- **Δt_EMT2**: 50 μs

- **Δt_T (BFAST EMT模式)**: 50 μs

- **Δt_DP1 (BFAST DP模式)**: 200 μs

- **Δt_DP2**: 250 μs

- **Δt_TS**: 5 ms

- **MMC额定参数**: 230 kV, 300 MW, 直流母线400 kV, 每桥臂20个子模块, 子模块电容5 mF, 桥臂电感/电阻0.001 H/0.025 Ω

## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 改进型IEEE 118节点系统（含MMC-HVDC）母线47处0.2秒单相接地故障 | 多求解器框架输出的EMT1、EMT2及BFAST子系统电压/电流波形与PSCAD/EMTDC全EMT基准仿真完全一致。BFAST在故障发生前自动由DP模式切换至EMT模式，故障清除后切回DP模式，暂态细节完整保留。切换后因波形含微小直流分量出现轻微振荡，但不影响整体精度。 | 10秒仿真耗时从基准全EMT的1126秒降至88秒（提速约12.8倍）；相比多速率全EMT仿真（358秒）提速约4.07倍。TS子系统步长(5 ms)为基准EMT步长(10 μs)的500倍。 |

## 量化发现

- 10秒仿真计算时间由1126 s大幅缩减至88 s，整体加速比达12.8倍。
- 相较于多速率纯EMT仿真（358 s），计算效率提升约4.07倍。
- TS求解器采用5 ms步长，为传统EMT步长(10 μs)的500倍，显著降低稳态计算负荷。
- 跨域接口波形误差基本不可察觉(essentially identical)，在Bergeron传输线接口下实现零时间步延迟补偿。
- BFAST求解器在暂态期间自动切换至50 μs步长，稳态期间切换至200 μs步长，模式切换响应无额外数值延迟。

## 关键公式

### BFDP频移变换公式

$$$\langle X \rangle_B(t) = \langle x \rangle_0(t) e^{-j\omega_s(t-T+s)} + 2 \sum_{k=1}^{+\infty} \langle x \rangle_k(t) e^{j(k-1)\omega_s(t-T+s)}$$$

*用于BFAST求解器在EMT与DP模式间切换的核心数学基础，通过设置$\omega_s=0$或$\omega_s=\omega_0$实现求解域转换*

### BFAST/DP侧Bergeron边界电流注入公式

$$$\langle h_K \rangle_B(t) = \left( \frac{2\langle v_M \rangle_B(t-\tau)}{Z_C} - \left( \frac{2\langle v_K \rangle_B(t-2\tau)}{Z_C} - \langle h_K \rangle_B(t-2\tau) \right) e^{-j\omega_s \tau} \right) e^{-j\omega_s \tau}$$$

*用于EMT与BFAST/DP求解器间的显式无延迟数据交互，补偿跨求解器通信与分区带来的时间步差异*

### MATE联络电流计算式

$$$I_\alpha(i) = Z_\alpha^{-1} e_\alpha(i)$$$

*用于DP与TS子系统解耦并行计算，消除传输线接口对大时间步的限制，支持毫秒级暂态稳定求解*

## 验证详情

- **验证方式**: 协同仿真对比验证（与PSCAD/EMTDC独立全EMT基准仿真进行波形与耗时对比）
- **测试系统**: 改进型IEEE 118节点测试系统（母线62发电机替换为300 MW MMC-HVDC系统）
- **仿真工具**: PSCAD/EMTDC（核心EMT求解器）、Microsoft Visual Studio C++（外部BFAST/DP/TS求解器）、内置协同仿真组件与MATE算法
- **验证结果**: 框架在含电力电子设备的复杂电网中实现了高精度暂态波形复现，跨求解器接口无显著数值误差或延迟；通过多速率分区与自适应求解策略，计算效率较传统全EMT提升超12倍，验证了多求解器架构在兼顾精度与大规模电网仿真效率方面的优越性。

## 适用边界

### 适用条件

- 适用于理解本文 `A multi-solver framework for co-simulation of transients in modern power systems`（2023） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。
- 适用于以 多速率仿真、动态相量法、频率自适应暂态仿真 为核心的建模、仿真、等值、控制或稳定性分析场景；具体对象以原文算例和页面“涉及的模型”为准。
- 可作为知识图谱中的方法定位和文献入口，尤其用于追踪：提出融合EMT、BFAST、动态相量与暂态稳定求解器的多速率协同仿真框架

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
- 源文件路径：`["EMT_Doc/02/Rupasinghe 等 - 2023 - A multi-solver framework for co-simulation of transients in modern power systems.pdf"]`；需要深修时应优先核对该 PDF 的首页、摘要、方法和实验表图。
