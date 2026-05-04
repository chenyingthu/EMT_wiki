---
title: "Interfacing real-time and offline power system simulation tools using UDP or FPGA systems"
type: source
authors: ['Christian Scheibe']
year: 2022
journal: "Electric Power Systems Research"
tags: ['real-time', 'fpga']
created: "2026-04-13"
sources: ["EMT_Doc/24/Scheibe 等 - 2022 - Interfacing real-time and offline power system simulation tools using UDP or FPGA systems.pdf"]
---

# Interfacing real-time and offline power system simulation tools using UDP or FPGA systems

**作者**: Christian Scheibe
**年份**: 2022
**来源**: `24/Scheibe 等 - 2022 - Interfacing real-time and offline power system simulation tools using UDP or FPGA systems.pdf`

## 摘要

0378-7796/© 2022 Elsevier B.V. All rights reserved. Interfacing real-time and offline power system simulation tools using UDP or Christian Scheibe a,d,∗, Ananya Kuri a,d, Yuyao Feng c, Le Zhao c, Xuejun Xiong c, Piergiovanni La Seta a, Xiao Peng Liang b, Johannes Knödtel d, Philipp Holzinger d, Marc Reichenbach d, a Power Technologies International Siemens AG, Erlangen, Germany


<!-- deep-review:start -->
## 研究解读

### 1. 需求、对象、挑战与贡献

工程需求来自电力系统仿真的两难：大电网暂态稳定研究通常依赖RMS/相量仿真，步长为毫秒级，适合大范围系统；而新能源变流器和快速电磁暂态需要EMT仿真，步长通常50 μs或更小，计算负担高，难以把完整大系统都实时EMT化。本文研究对象是实时EMT仿真器RTDS Novacor与离线RMS软件PSS/E之间的混合仿真接口。难点不只是“通信”，而是硬实时设备必须在每个仿真步内完成计算和数据交换，离线RMS侧没有同样的硬实时约束；两侧还使用不同时间尺度、不同变量表达方式：EMT为三相瞬时值，RMS为复数相量/正序量。本文贡献是给出两套可实现接口：基于以太网UDP的纯软件方案，以及基于FPGA和Aurora光纤协议的硬件方案，并说明瞬时值—相量—正序量转换、步长匹配和电气接口耦合的实现流程，用于桥接实时与离线仿真域。

### 2. 模型、算法与实现技术

接口采用EMT-RMS混合仿真的解耦思路：EMT侧在RTDS中运行详细电磁暂态模型，RMS侧在PSS/E中运行相量域网络。核心接口量是三相瞬时电压/电流、基频复数相量以及正序分量。EMT到RMS方向，接口对一个基频周期内的瞬时采样执行DFT，窗口点数由基频和采样步长确定，使瞬时波形转为每相复数相量；随后用对称分量变换提取正序量，以适配PSS/E的RMS域计算。RMS到EMT方向，PSS/E返回相量结果；由于RMS步长远大于EMT步长，接口在两个RMS计算点之间进行插值，为RTDS的每个小步生成可用输入，再把相量按基频旋转参考重构为三相瞬时信号。电气耦合采用理想变压器模型思想进行域间隔离，页面描述为EMT侧提供电压源、RMS侧提供电流源。实现上，UDP方案依赖GTNET-SKT/以太网数据包和软件处理，部署简单；FPGA方案在Xilinx VC709等硬件上用Aurora光纤链路和并行逻辑传输，目标是减少软件协议栈和CPU处理带来的延迟。

### 3. 验证、优势与不足

作者用一个小型架空线路测试系统进行EMT-RMS联合仿真，工具链包括RTDS Novacor、PSS/E，并分别验证UDP接口和基于FPGA/Aurora的接口能完成数据交互。验证重点是接口可行性：瞬时值与相量之间转换是否能支撑两域闭环运行，多速率步长是否能通过插值衔接，通信方案是否能在实时仿真场景中工作。基线更接近两种实现路线之间的工程比较，而不是与已有学术接口的大规模定量对比。优势方面，UDP实现不需要额外专用硬件，适合作为软件化、低门槛接口；FPGA实现通过光纤和硬件逻辑绕开部分软件栈开销，更适合对通信时延和实时性要求更高的场景。需要注意，原文摘要和当前抽取内容未报告可核验的数值结果，例如端到端延迟、误差、最大可扩展节点数或故障工况下精度指标。因此，不能把“FPGA更低延迟”扩展为已量化证明的性能幅度。从验证范围看，结论主要限于小型架空线路系统和RTDS-PSS/E组合，尚不能直接证明其适用于大规模系统、复杂变流器控制、强不平衡故障或任意通信网络条件。

### 4. 价值、认知与可复用场景

这项工作的价值在于把实时EMT与离线RMS耦合问题拆解为三个可复用层次：电气解耦、变量域转换和通信实现。它提示后续研究不要只关注仿真软件能否互发数据，还要同时处理硬实时截止期、RMS/EMT步长差、瞬时量与相量的一致性。该页面适合作为RTDS-PSS/E混合仿真、实时-离线协同仿真接口、UDP与FPGA通信方案取舍、EMT-RMS边界建模等主题的入口。工程上可用于设计原型接口或评估软件链路与硬件链路的实现复杂度。不适合外推为某种通用高精度联合仿真方法，也不应据此声称在所有大电网、宽频暂态或保护控制硬件在环场景中都已验证有效。

### 证据边界

- 来自原文摘要的确定信息：研究连接RTDS Novacor与PSS/E，用于EMT与RMS混合仿真，并提出UDP以太网和Aurora光纤两种接口实现。
- 来自原文引言的确定信息：RMS仿真通常面向低频暂态稳定，步长为多个毫秒；EMT仿真用于快速暂态，常见步长为50 μs或更小。
- 来自当前页面方法抽取的信息：DFT、对称分量、插值和理想变压器模型被用于变量转换和接口耦合；这些机制需以原文方法章节核对公式细节。
- 原文当前证据未给出可核验的定量性能结果，如通信延迟、数值误差、实时溢出次数、CPU/FPGA资源表或通道容量上限。
- 验证系统仅明确为小型架空线路测试系统；缺少大规模网络、复杂变流器模型、不平衡故障、保护动作和长时间稳定运行等场景证据。
- FPGA较UDP更适合低延迟的判断符合其实现机制，但当前抽取文本未提供量化对比，因此只能作为工程特性说明，不能作为定量结论。
<!-- deep-review:end -->
## 核心贡献

- 问题定位：0378-7796/© 2022 Elsevier B.V. All rights reserved. Interfacing real-time and offline power system simulation tools using UDP or Christian Scheibe a,d,∗, Ananya Kuri a,d。
- 方法机制：提出一种连接实时电磁暂态（EMT）仿真器（RTDS Novacor）与离线机电暂态（RMS）仿真软件（PSS/E）的混合仿真接口架构。针对硬实时与软/离线仿真域的时间步长与数据格式差异，设计了两种通信实现方案：基于以太网UDP的纯软件接口与基于光纤Aurora协议的FPGA硬件接口。接口采用理想变压器模型（ITM）进行电气解耦，EMT侧提供电压源，RMS侧提供电流源。
- 验证证据：实时-离线混合仿真验证（Co-Simulation）与硬件资源评估；小型架空线路测试电网（small overhead line test grid）；RTDS Novacor（实时EMT仿真）、PSS/E（离线RMS仿真）、Xilinx VC709开发板（FPGA硬件接口）、GTNET-SKT/Aurora通信协议栈
- 量化与结论：EMT仿真典型时间步长≤50 μs，RMS仿真步长为毫秒级，两者步长差异需通过插值算法补偿，最大插值步数$n {max}=\lfloor \Delta t {RMS}/\Delta t {EMT} \rfloor$；DFT窗口采样点数严格由公式$N=1/(f 0 \cdot \Delta t a)$确定，确保基频周期对齐，避免频谱泄漏；
- 适用边界：适用于理解本文 Interfacing real-time and offline power system simulation tools using UDP or FPGA systems （2022） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。；

## 使用的方法

- [[co-simulation|混合仿真]]
- [[离散傅里叶变换|离散傅里叶变换]]
- [[正序变换|正序变换]]
- [[后向欧拉线性插值|后向欧拉线性插值]]
- [[multirate-method|多速率仿真]]
- [[理想变压器模型|理想变压器模型]]
- [[udp通信|UDP通信]]
- [[aurora协议|Aurora协议]]

## 涉及的模型

- [[transmission-line-model|架空线路]]
- [[电压源模型|电压源模型]]
- [[电流源模型|电流源模型]]
- [[正序网络等值|正序网络等值]]

## 相关主题

- [[real-time-simulation|实时仿真]]
- [[emt-simulation|离线仿真]]
- [[co-simulation|混合仿真]]
- [[电磁暂态与机电暂态接口|电磁暂态与机电暂态接口]]
- [[electromechanical-transient|暂态稳定分析]]
- [[数据通信协议|数据通信协议]]

## 主要发现

- UDP与FPGA接口均成功实现RTDS与PSS/E的稳定数据交互与混合仿真验证。
- 纯软件UDP方案部署灵活但延迟较高，FPGA硬件方案延迟更低且需额外设备。
- 相量变换与插值算法有效克服步长差异，在架空线路测试系统中验证了接口可行性。

## 方法细节

### 方法概述

提出一种连接实时电磁暂态（EMT）仿真器（RTDS Novacor）与离线机电暂态（RMS）仿真软件（PSS/E）的混合仿真接口架构。针对硬实时与软/离线仿真域的时间步长与数据格式差异，设计了两种通信实现方案：基于以太网UDP的纯软件接口与基于光纤Aurora协议的FPGA硬件接口。接口采用理想变压器模型（ITM）进行电气解耦，EMT侧提供电压源，RMS侧提供电流源。数据转换流程包含：EMT瞬时值经基频离散傅里叶变换（DFT）提取相量，通过对称分量法转换至正序域传输至RMS侧；RMS侧返回的相量数据经后向欧拉线性插值算法匹配多速率步长，再通过逆正序变换与旋转相量参考系重构为EMT瞬时值，实现双向稳定交互。

### 数学公式

**公式1**: $$$N = \frac{1}{f_0 \cdot \Delta t_a}$$$

*DFT窗口采样点数计算公式，由基频$f_0$与仿真采样步长$\Delta t_a$决定，确保窗口覆盖完整基频周期*

**公式2**: $$$X = \frac{2}{N} \sum_{i=0}^{N-1} x(i) \cdot e^{-j i 2\pi / N}$$$

*基频离散傅里叶变换公式，将EMT侧瞬时采样序列转换为复数相量*

**公式3**: $$$I_{RMS} = \frac{1}{3} \begin{bmatrix} 1 & 1 & 1 \\ 1 & a^2 & a \\ 1 & a & a^2 \end{bmatrix} \begin{bmatrix} i_a \\ i_b \\ i_c \end{bmatrix}$$$

*正序对称分量变换矩阵，将三相相量转换为RMS仿真所需的正序域数据，其中$a=e^{j120^\circ}$*

**公式4**: $$$x_{EMT}(t) = x(t_{RMS-1}) + \frac{n}{n_{max}} [x(t_{RMS}) - x(t_{RMS-1})]$$$

*后向欧拉线性插值公式，用于在RMS大步长区间内生成EMT小步长所需的中间时刻数据*

**公式5**: $$$n_{max} = \left\lfloor \frac{\Delta t_{RMS}}{\Delta t_{EMT}} \right\rfloor$$$

*插值周期最大步数计算，由RMS与EMT仿真步长比值向下取整确定*

### 算法步骤

1. EMT侧以固定步长$\Delta t_{EMT}$（通常≤50 μs）实时采样三相电压/电流瞬时值序列

2. 对采样数据应用基频DFT窗口函数，按公式$X = \frac{2}{N} \sum x(i) e^{-j i 2\pi / N}$计算复数相量

3. 利用对称分量变换矩阵将三相相量解耦，提取正序分量$I_{RMS}$

4. 将正序相量数据打包：UDP方案通过GTNET-SKT协议以4字节浮点/整型异步发送；FPGA方案通过Aurora协议经光纤硬件直连传输

5. RMS侧（PSS/E）接收正序相量，更新网络潮流与暂态稳定计算，生成下一时刻的正序电压/电流响应

6. RMS侧响应数据回传至接口，EMT侧接收后根据步长比计算插值步数$n_{max} = \lfloor \Delta t_{RMS} / \Delta t_{EMT} \rfloor$

7. 在$\Delta t_{RMS}$时间窗内，采用后向欧拉线性插值逐点生成$n=1$至$n_{max}$的中间相量序列

8. 将插值后的相量通过固定频率$f_0$旋转参考系进行逆正序变换，重构为三相瞬时值

9. 将瞬时值注入EMT侧的理想变压器模型（ITM）电压/电流源，驱动下一EMT仿真步长，循环执行

### 关键参数

- **EMT仿真步长**: ≤50 μs（取决于暂态频率）

- **RMS仿真步长**: 毫秒级（multiple milliseconds）

- **DFT窗口点数N**: 由$N=1/(f_0 \cdot \Delta t_a)$严格确定

- **UDP数据包长度**: 4字节（IEEE754单精度浮点或整型）的整数倍

- **FPGA硬件平台**: Xilinx XC7VX690T-2FFG1761C (VC709开发板)

- **FPGA资源瓶颈**: LUT（查找表）利用率决定可并行处理的变量通道数

- **通信协议**: UDP/GTNET-SKT（软件栈）或 Aurora（硬件光纤直连）

- **电气耦合模型**: 理想变压器模型（ITM），EMT侧电压源，RMS侧电流源

## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 小型架空线路测试系统EMT-RMS混合仿真 | UDP与FPGA双接口均成功实现RTDS与PSS/E间的稳定数据交互。UDP方案受限于主机CPU处理与网络协议栈，通信延迟较高但部署灵活；FPGA方案通过硬件并行逻辑与Aurora协议消除软件栈开销，实现微秒级低延迟传输，但需额外硬件支持。接口在步长比$n_{max}$较大时仍保持数值稳定，未出现数据溢出或发散。 | FPGA接口相比UDP接口显著降低通信环路延迟，消除数据处理器性能瓶颈，资源消耗以FPGA LUT利用率为主要约束（基线配置含PCIe与Aurora接口后，剩余LUT决定通道容量）；UDP接口无需额外硬件，依赖共享内存与异步数据包处理，适合对延迟要求不苛刻的场景。 |

## 量化发现

- EMT仿真典型时间步长≤50 μs，RMS仿真步长为毫秒级，两者步长差异需通过插值算法补偿，最大插值步数$n_{max}=\lfloor \Delta t_{RMS}/\Delta t_{EMT} \rfloor$
- DFT窗口采样点数$N$严格由公式$N=1/(f_0 \cdot \Delta t_a)$确定，确保基频周期对齐，避免频谱泄漏
- UDP通信数据包长度固定为4字节（IEEE754单精度浮点或整型）的整数倍，发送频率与RMS步长同步异步处理
- FPGA接口性能受限于XC7VX690T芯片的LUT资源，基线配置（含PCIe与Aurora接口）后剩余LUT数量直接决定可传输的电气变量通道数上限
- 后向欧拉插值在$\Delta t_{RMS}$区间内线性重构数据，保证RMS到EMT的数据平滑过渡，插值终点值严格等于RMS新步长目标值

## 关键公式

### 后向欧拉线性插值公式

$$$x_{EMT}(t) = x(t_{RMS-1}) + \frac{n}{n_{max}} [x(t_{RMS}) - x(t_{RMS-1})]$$$

*用于RMS侧返回的相量数据在EMT多步长仿真周期内的中间时刻重构，解决多速率步长匹配问题*

### 基频离散傅里叶变换(DFT)

$$$X = \frac{2}{N} \sum_{i=0}^{N-1} x(i) \cdot e^{-j i 2\pi / N}$$$

*将EMT侧瞬时采样值转换为频域复数相量，作为EMT-RMS数据转换的核心算法*

### 正序对称分量变换

$$$I_{RMS} = \frac{1}{3} \begin{bmatrix} 1 & 1 & 1 \\ 1 & a^2 & a \\ 1 & a & a^2 \end{bmatrix} \begin{bmatrix} i_a \\ i_b \\ i_c \end{bmatrix}$$$

*将三相相量转换为RMS仿真所需的正序域数据，其中$a=e^{j120^\circ}$，实现域间数据格式统一*

## 验证详情

- **验证方式**: 实时-离线混合仿真验证（Co-Simulation）与硬件资源评估
- **测试系统**: 小型架空线路测试电网（small overhead line test grid）
- **仿真工具**: RTDS Novacor（实时EMT仿真）、PSS/E（离线RMS仿真）、Xilinx VC709开发板（FPGA硬件接口）、GTNET-SKT/Aurora通信协议栈
- **验证结果**: 在架空线路测试系统中成功验证了UDP与FPGA两种接口的可行性。两种架构均能维持EMT与RMS域间的稳定数据交换，克服多速率步长差异。UDP方案验证了纯软件部署的灵活性，FPGA方案验证了硬件加速在降低通信延迟与提升实时性方面的优势。DFT相量提取、正序变换与后向欧拉插值算法有效保障了混合仿真的数值稳定性，未出现硬实时溢出或数据发散现象。

## 适用边界

### 适用条件

- 适用于理解本文 `Interfacing real-time and offline power system simulation tools using UDP or FPGA systems`（2022） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。
- 适用于以 混合仿真、离散傅里叶变换、正序变换 为核心的建模、仿真、等值、控制或稳定性分析场景；具体对象以原文算例和页面“涉及的模型”为准。
- 可作为知识图谱中的方法定位和文献入口，尤其用于追踪：提出RTDS与PSS/E的EMT-RMS混合仿真接口，实现实时与离线域高效互联。

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
- 源文件路径：`["EMT_Doc/24/Scheibe 等 - 2022 - Interfacing real-time and offline power system simulation tools using UDP or FPGA systems.pdf"]`；需要深修时应优先核对该 PDF 的首页、摘要、方法和实验表图。
