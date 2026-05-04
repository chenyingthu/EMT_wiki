---
title: "Accelerating electromagnetic transient simulations using graphical processing units"
type: source
authors: ['Devin Aluthge']
year: 2025
journal: "Electric Power Systems Research"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Aluthge 等 - 2026 - Accelerating electromagnetic transient simulations using graphical processing units.pdf"]
---

# Accelerating electromagnetic transient simulations using graphical processing units

**作者**: Devin Aluthge
**年份**: 2025
**来源**: `05/Aluthge 等 - 2026 - Accelerating electromagnetic transient simulations using graphical processing units.pdf`

## 摘要

本文提出了一种全GPU驻留的电磁暂态(EMT)仿真架构，旨在彻底消除CPU与GPU之间的数据传输与通信开销。该方法基于伴随电路理论将电网元件等效为电流源与电阻，构建实数导纳矩阵。通过系统评估KLU、Cholesky分解、Woodbury公式及补偿法，最终选定NVIDIA cuDSS稀疏求解器结合Cholesky分解作为核心网络求解引擎。算法利用CUDA内核并行处理同步发电机、无源元件及电流源的动态更新，并在每个时间步内完成右端向量组装。针对网络拓扑变化（如故障或高频开关动作），仅执行数值重分解而复用符号分解结构，从而在保证精度的前提下实现大规模、高开关频率电网的高效并行求解。


<!-- deep-review:start -->
## 研究解读

### 1. 需求、对象、挑战与贡献

工程需求来自大规模新能源和电力电子装置接入后的EMT仿真：网络规模更大、开关器件更多，微秒级步长下每一步都要更新元件历史量、组装注入电流并求解网络节点电压，传统串行或CPU并行求解容易被线性方程求解和通信开销限制。研究对象是基于节点导纳方程的EMT网络求解器，尤其是含频繁拓扑变化的大系统。难点不只是把计算搬到GPU，而是开关会反复改变导纳矩阵，使预求逆、一次性分解或分区并行方法失效或产生通信负担。本文的贡献在于系统比较KLU、Cholesky、Woodbury、补偿法等方案后，构建全GPU驻留的EMT实现：网络矩阵、元件状态、右端项组装和稀疏求解尽量都在GPU侧完成，并用cuDSS/Cholesky作为核心求解路径，以避免每个时间步CPU-GPU往返传输。

### 2. 模型、算法与实现技术

该方法仍以经典EMT伴随电路建模为基础：电感、电容、同步机和电流源等元件在每个时间步被等效为导纳/电阻与历史电流源，网络接口量是节点注入电流i和节点电压v，核心方程为Y(t)v(t)=i(t)。算法流程是先在GPU上保存稀疏导纳矩阵、元件参数、历史电流和节点电压；对Y做符号分析与数值分解；时间推进时由CUDA内核并行更新非动态电流源、无源元件历史项和同步机相关方程，再组装RHS并调用GPU稀疏求解器求v。Cholesky分解Y=LL^T利用实数、对称正定导纳矩阵结构减少存储和计算；Woodbury公式用于评估少量矩阵元素变化时是否可用低秩修正替代全矩阵重分解；补偿法则作为另一种处理网络变化的候选方案。论文的实现取舍是：对故障或开关引起的拓扑变化，尽量复用符号分解结构，仅重做数值分解，而不是在CPU侧重新组织并传输整个问题。

### 3. 验证、优势与不足

作者用商业EMT软件PSCAD/EMTDC作为主要精度基线，并在双电源简单系统、IEEE 39节点系统和Texas 2000节点合成电网中测试自研CUDA/cuDSS求解器。验证指标包括电压波形一致性、总仿真耗时、单步耗时，以及不同线性求解策略在矩阵规模和开关变化下的耗时。页面证据显示，双电源系统故障投切时节点3电压波形与PSCAD/EMTDC基本重合；IEEE 39节点算例中，101 s仿真、50 μs步长下GPU求解器220 s、PSCAD/EMTDC 260 s，且GPU侧按每步重分解模拟最坏开关情形；Texas 2000节点、15618阶矩阵、5 s仿真中，GPU求解器51 s而PSCAD/EMTDC 2016 s。优势主要体现在大规模网络和高频开关场景下减少主机-设备通信、保留稀疏结构并加速数值求解。边界是验证集中在特定GPU、步长和算例；未证明所有控制器、换流器模型、实时硬件平台或更复杂多物理耦合场景下都能保持同等收益。

### 4. 价值、认知与可复用场景

这项工作的重要认知是：EMT加速的瓶颈不只在线性代数算子本身，还在数据驻留位置、拓扑变化处理和每步RHS组装流程；如果元件更新、矩阵分解和求解跨CPU/GPU反复移动，GPU算力优势会被通信抵消。它适合作为后续研究GPU-EMT求解器、稀疏直接法、开关网络重分解策略、cuDSS在电力系统中的应用、以及大规模IBR系统暂态仿真的方法入口。工程上可启发离线大规模EMT加速和开关密集系统批量仿真。不宜直接外推为通用实时仿真方案，也不能据此断言任意网络划分、任意GPU或任意设备模型都能获得相同加速比。

### 证据边界

- 来自原文/页面证据：论文明确关注GPU加速EMT仿真，关键词包括EMT simulations、GPUs、Large systems、cuDSS，并说明目标是处理大规模、复杂和含大量开关的电力系统。
- 来自原文/页面证据：测试基线包括PSCAD/EMTDC，测试系统包括双电源简单系统、IEEE 39节点系统和Texas 2000节点合成电网；页面给出了39节点和Texas 2000节点的耗时数字。
- 来自原文/页面证据：方法比较涉及KLU、Cholesky、Woodbury公式和补偿法；Woodbury用于处理导纳矩阵变化，Cholesky用于对称正定导纳矩阵。
- 据方法推断但需原文表图复核：‘全GPU驻留’的收益来自减少CPU-GPU通信与复用符号分解结构；具体每个CUDA内核的并行粒度、内存布局和同步开销需看原文实现细节。
- 缺少或未在当前证据中充分展开：不同GPU型号、不同CPU并行库、不同步长、实时仿真约束、详细换流器控制模型和更广泛故障/开关模式下的可重复性能。
- 当前页面的作者元数据与原文首页不完全一致：页面元数据只列Devin Aluthge，而原文首页列Devin Aluthge、Ian Jeffrey、Shaahin Filizadeh、Dharshana Muthumuni；引用前应以论文首页为准。
<!-- deep-review:end -->
## 核心贡献

- 问题定位：本文提出了一种全GPU驻留的电磁暂态(EMT)仿真架构，旨在彻底消除CPU与GPU之间的数据传输与通信开销。该方法基于伴随电路理论将电网元件等效为电流源与电阻，构建实数导纳矩阵。通过系统评估KLU、Cholesky分解、Woodbury公式及补偿法，最终选定NVIDIA cuDSS稀疏求解器结合Cholesky分解作为核心网络求解引擎。
- 方法机制：本文提出了一种全GPU驻留的电磁暂态(EMT)仿真架构，旨在彻底消除CPU与GPU之间的数据传输与通信开销。该方法基于伴随电路理论将电网元件等效为电流源与电阻，构建实数导纳矩阵。通过系统评估KLU、Cholesky分解、Woodbury公式及补偿法，最终选定NVIDIA cuDSS稀疏求解器结合Cholesky分解作为核心网络求解引擎。算法利用CUDA内核并行处理同步发电机、无源元件及电流源的动态更新，并在每个时间步内完成右端向量组装。
- 验证证据：双电源简单系统、IEEE 39节点系统、Texas 2000节点合成电网；自研GPU-EMT求解器（基于CUDA/cuDSS） vs PSCAD/EMTDC；在双电源系统故障投切测试中，GPU求解器计算的节点3电压波形与PSCAD/EMTDC结果完全吻合（误差可忽略），验证了算法精度；
- 量化与结论：全GPU驻留架构彻底消除了主机与设备间的通信开销，使大规模网络求解延迟降至微秒级。；cuDSS结合Cholesky分解在万阶及以上导纳矩阵求解中表现最优，数值求解耗时仅0.030 ms。；Woodbury公式实现中，显式存储逆矩阵比存储分解因子快10倍，但当变化量k=400时，O(k^3)的稠密矩阵求逆成为性能瓶颈，整体效率不及cuDSS。；
- 适用边界：适用于理解本文 Accelerating electromagnetic transient simulations using graphical processing units （2025） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。；

## 使用的方法

- [[klu分解|KLU分解]]
- [[cholesky分解|Cholesky分解]]
- [[woodbury公式|Woodbury公式]]
- [[methods/average-value-model|补偿法]]
- [[gpu稀疏求解|GPU稀疏求解]]
- [[methods/nodal-analysis|节点分析法]]

## 涉及的模型

- [[test-systems/ieee-39-bus-system|IEEE 39节点系统]]
- [[models/transformer-model|变压器]]
- [[models/synchronous-machine-model|同步发电机]]
- [[π型输电线路|π型输电线路]]
- [[逆变器接口电源|逆变器接口电源]]
- [[电力电子换流器|电力电子换流器]]

## 相关主题

- [[topics/emt-simulation|电磁暂态仿真]]
- [[methods/gpu-accelerated-simulation|GPU并行加速]]
- [[topics/large-scale-grid-simulation|大规模电网仿真]]
- [[高频开关动态|高频开关动态]]
- [[methods/sparse-matrix-solver|稀疏矩阵求解]]
- [[topics/renewable-energy-integration|新能源并网]]

## 主要发现

- cuDSS求解器在中小规模及万阶导纳矩阵测试中，计算耗时均显著低于CPU基准算法。
- GPU全驻留架构有效克服了频繁网络拓扑变化导致的矩阵重复分解瓶颈。
- 针对含大量电力电子设备的大规模系统，GPU方案可实现数量级的仿真提速。

## 方法细节

### 方法概述

本文提出了一种全GPU驻留的电磁暂态(EMT)仿真架构，旨在彻底消除CPU与GPU之间的数据传输与通信开销。该方法基于伴随电路理论将电网元件等效为电流源与电阻，构建实数导纳矩阵。通过系统评估KLU、Cholesky分解、Woodbury公式及补偿法，最终选定NVIDIA cuDSS稀疏求解器结合Cholesky分解作为核心网络求解引擎。算法利用CUDA内核并行处理同步发电机、无源元件及电流源的动态更新，并在每个时间步内完成右端向量组装。针对网络拓扑变化（如故障或高频开关动作），仅执行数值重分解而复用符号分解结构，从而在保证精度的前提下实现大规模、高开关频率电网的高效并行求解。

### 数学公式

**公式1**: $$$\mathbf{Y}(t)\mathbf{v}(t) = \mathbf{i}(t)$$$

*EMT网络节点电压求解基本方程，其中$\mathbf{Y}$为导纳矩阵，$\mathbf{v}$为节点电压向量，$\mathbf{i}$为注入电流向量。*

**公式2**: $$$(\mathbf{Y} + \mathbf{U}\mathbf{V}^T)^{-1} = \mathbf{Y}^{-1} - \mathbf{Y}^{-1}\mathbf{U}(\mathbf{I} + \mathbf{V}^T\mathbf{Y}^{-1}\mathbf{U})^{-1}\mathbf{V}^T\mathbf{Y}^{-1}$$$

*Woodbury矩阵求逆公式，用于在不重新分解整个矩阵的情况下，高效处理导纳矩阵中$k$个元素的局部变化。*

**公式3**: $$$\mathbf{Y} = \mathbf{L}\mathbf{L}^T$$$

*Cholesky分解公式，适用于对称正定(SPD)导纳矩阵，可将计算时间和内存需求降低约一半。*

### 算法步骤

1. 初始化仿真参数，在GPU上分配系统数据、导纳矩阵、电流和电压的内存空间，并将主机(CPU)数据拷贝至设备(GPU)。

2. 对导纳矩阵$\mathbf{Y}$执行符号分解以确定稀疏填充结构，随后在GPU上完成数值分解。

3. 进入时间步进循环，根据当前时间$t$判断同步发电机是否解锁转子动力学（$t<t_1$时锁定，$t \ge t_1$时启用）。

4. 调用并行CUDA内核：更新非动态电流源；基于上一时刻电压求解发电机模型方程；更新电感、电容等无源元件的历史电流项。

5. 组装网络方程的右端向量(RHS)，准备进行线性系统求解。

6. 检测故障或开关事件：若拓扑发生变化，更新导纳矩阵$\mathbf{Y}$并执行数值重分解（符号分解保持不变）；若无变化则跳过分解。

7. 利用前代回代法在GPU上求解节点电压向量。

8. 计算当前时间步无源元件的注入电流，时间步长递增($t \leftarrow t + dt$)，循环直至达到最大仿真时间。

### 关键参数

- **仿真步长**: 50 μs

- **测试矩阵规模**: 81×81, 10000×10000, 15618×15618

- **GPU硬件**: NVIDIA Tesla V100-PCIE-16GB

- **CPU硬件**: 14核 Intel Core i7 2.1 GHz, 32GB RAM

- **Woodbury变化量k**: 400 (对应100个网络开关变化)

## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| IEEE 39节点系统 | 仿真时长101秒，步长50μs。GPU求解器耗时220秒，PSCAD/EMTDC耗时260秒。GPU代码在每个时间步均强制执行数值分解以模拟最恶劣的开关场景。 | GPU方案比PSCAD快约1.18倍（在最坏情况下仍具优势） |

| Texas 2000节点合成电网 | 仿真时长5秒，步长50μs，导纳矩阵规模15618×15618。GPU求解器总耗时51秒（单步510μs），PSCAD/EMTDC耗时2016秒（单步20.16ms）。 | GPU方案实现39.5倍的仿真加速 |

| 10000×10000稀疏矩阵求解基准测试 | cuDSS求解器（不含符号分解）耗时0.030 ms，MATLAB反斜杠算子耗时1302 ms，PARDISO耗时9000-18000 ms。 | cuDSS数值求解阶段比MATLAB快约43400倍，比PARDISO快30万至60万倍 |

## 量化发现

- 全GPU驻留架构彻底消除了主机与设备间的通信开销，使大规模网络求解延迟降至微秒级。
- cuDSS结合Cholesky分解在万阶及以上导纳矩阵求解中表现最优，数值求解耗时仅0.030 ms。
- Woodbury公式实现中，显式存储逆矩阵比存储分解因子快10倍，但当变化量k=400时，O(k^3)的稠密矩阵求逆成为性能瓶颈，整体效率不及cuDSS。
- 补偿法因需串行求解两个子网络互联方程且单时间步内需两次矩阵求解，其加速比未能超越cuDSS直接求解方案。
- 在Texas 2000节点系统中，GPU方案实现39.5倍加速，单步计算时间从20.16 ms降至510 μs。

## 关键公式

### EMT网络节点方程

$$$\mathbf{Y}(t)\mathbf{v}(t) = \mathbf{i}(t)$$$

*每个时间步求解电网节点电压的核心线性方程组*

### Woodbury矩阵恒等式

$$$(\mathbf{Y} + \mathbf{U}\mathbf{V}^T)^{-1} = \mathbf{Y}^{-1} - \mathbf{Y}^{-1}\mathbf{U}(\mathbf{I} + \mathbf{V}^T\mathbf{Y}^{-1}\mathbf{U})^{-1}\mathbf{V}^T\mathbf{Y}^{-1}$$$

*用于处理网络拓扑局部变化（如开关动作）时的导纳矩阵快速更新，避免全局重分解*

### Cholesky分解

$$$\mathbf{Y} = \mathbf{L}\mathbf{L}^T$$$

*针对对称正定导纳矩阵的分解方法，用于cuDSS求解器以降低计算复杂度和内存占用*

## 验证详情

- **验证方式**: 商业软件对比仿真验证
- **测试系统**: 双电源简单系统、IEEE 39节点系统、Texas 2000节点合成电网
- **仿真工具**: 自研GPU-EMT求解器（基于CUDA/cuDSS） vs PSCAD/EMTDC
- **验证结果**: 在双电源系统故障投切测试中，GPU求解器计算的节点3电压波形与PSCAD/EMTDC结果完全吻合（误差可忽略），验证了算法精度；在IEEE 39节点和2000节点系统中，GPU方案在保持精度的同时实现了显著的计算加速，尤其在最坏情况（每步重分解）下仍优于传统串行求解器。

## 适用边界

### 适用条件

- 适用于理解本文 `Accelerating electromagnetic transient simulations using graphical processing units`（2025） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。
- 适用于以 klu分解、cholesky分解、woodbury公式 为核心的建模、仿真、等值、控制或稳定性分析场景；具体对象以原文算例和页面“涉及的模型”为准。
- 可作为知识图谱中的方法定位和文献入口，尤其用于追踪：提出全GPU驻留的EMT网络求解架构，彻底消除主机与设备间通信开销。

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
- 源文件路径：`["EMT_Doc/05/Aluthge 等 - 2026 - Accelerating electromagnetic transient simulations using graphical processing units.pdf"]`；需要深修时应优先核对该 PDF 的首页、摘要、方法和实验表图。
