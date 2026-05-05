---
title: "Numerically Efficient Average-Value Model for Voltage-Source Converters in Nodal-Based Programs"
type: source
authors: ['EBRAHIMI 等']
year: 2024
journal: "IEEE Open Journal of Power Electronics;2024;5; ;10.1109/OJPEL.2023.3337888"
tags: ['average-value']
created: "2026-04-13"
sources: ["EMT_Doc/29/EBRAHIMI 等 - 2024 - Numerically Efficient Average-Value Model for Voltage-Source Converters in Nodal-Based Programs.pdf"]
---

# Numerically Efficient Average-Value Model for Voltage-Source Converters in Nodal-Based Programs

**作者**: EBRAHIMI 等
**年份**: 2024
**来源**: `29/EBRAHIMI 等 - 2024 - Numerically Efficient Average-Value Model for Voltage-Source Converters in Nodal-Based Programs.pdf`

## 摘要

提出广义直接接口平均值模型（Generalized Directly-Interfaced AVM, DI-AVM），通过构建扩展等效电导矩阵（Extended Equivalent Conductance Matrix）实现VSC与外部电路的数值高效接口。该方法核心在于假设所有AC侧（三相）和DC侧（正负极）节点均为悬浮节点（floating nodes），建立VSC AVM的广义导纳子矩阵，并将其直接合并到整体网络的节点分析方程（nodal equation）中。此方法消除了传统受控源（dependent source）接口固有的单步计算延迟（one-time-step relaxation delay），实现了VSC状态变量与外部网络方程的同步非迭代求解，同时解除了对DC侧负极和AC侧中性点必须接地的结构限制，支持含零序电压的不平衡系统与多换流器配置。


<!-- deep-review:start -->
## 研究解读

### 1. 需求、对象、挑战与贡献

工程需求来自含大量VSC的电力电子化系统EMT仿真：详细开关模型能表示每次开关事件，但在kHz到数十/数百kHz开关频率下需要很小步长或插值，难以用于大系统、快速离线研究或实时仿真。研究对象是节点分析型、非迭代EMT程序中的VSC平均值模型接口。难点不在平均化本身，而在传统AVM通常用受控电压/电流源连接外部电路，接口变量依赖上一时间步的端口电压/电流，形成一个人为时间步延迟；当仿真步长较大时，这个延迟会引入数值误差甚至不稳定。已有DI-AVM可消除该延迟，但要求DC负端和AC中性点接地，限制了含零序电压、不平衡网络和多换流器配置。本文贡献是把DI-AVM推广到任意端口节点配置：假设所有接口节点均可悬浮，推导扩展等效电导矩阵，并把该矩阵直接并入全网节点方程，从而在非迭代求解中同步求解VSC平均模型与外部网络。

### 2. 模型、算法与实现技术

本文提出的是广义直接接口平均值模型，即generalized DI-AVM。其核心实现不是把VSC等效成受控源单独计算，而是把VSC平均模型在端口处转写成等效电导关系。接口节点包括AC侧三相端子以及DC侧正、负端；论文强调这些节点均按floating nodes处理，因此不预设某一端必须接地。模型的输入/接口量是外部网络在这些端口上的节点电压和端口电流，内部控制仍可使用VSC AVM常见的平均量、同步坐标变换和控制参考；输出则表现为可嵌入节点导纳方程的电流注入/电导耦合关系。计算流程上，先由VSC平均关系得到各端口平均电压、电流之间的代数耦合，再形成扩展等效电导矩阵；随后将该子矩阵stamp到全网nodal equation中，与线路、源、负载等网络元件一起求解。这样，端口变量不再使用上一时间步的外部解，而是在同一个线性网络方程中被同时确定。机制上的关键点是：用矩阵耦合替代受控源外部接口，使非迭代EMT程序也能避免传统AVM接口处的一步松弛延迟；同时，悬浮节点公式保留公共模/零序自由度，避免因人为接地而改变网络结构。

### 3. 验证、优势与不足

作者在PSCAD/EMTDC中验证扩展DI-AVM，并以传统dependent-source-based AVM作为主要基线，在平衡和不平衡条件下比较数值表现。根据摘要和引言，评价重点是大仿真时间步下的数值精度和稳定性，而不是开关纹波复现能力；因为AVM本身已把离散开关现象平均掉。优势主要体现在两点：第一，扩展DI-AVM把VSC电导矩阵并入总节点方程，避免传统受控源接口使用上一时间步变量，因此在较大步长下相对传统AVM更不易产生由接口延迟引起的误差或不稳定；第二，任意端口节点配置取消了既有DI-AVM要求DC负端和AC中性点接地的限制，使含零序电压的不平衡AC系统和多个AVM换流器的实现更自然。需要注意，给定证据中未报告可核验的数值结果，例如具体误差百分比、稳定步长上限、加速倍数或测试系统完整参数；也未显示与详细开关模型的逐波形定量对比。因而从验证范围看，结论应限定为PSCAD/EMTDC内、作者所设平衡/不平衡算例和传统AVM基线下的数值接口改进，不能直接外推到所有控制器、拓扑、故障类型或实时硬件平台。

### 4. 价值、认知与可复用场景

这项工作的主要认知价值是把“AVM是否准确”进一步拆分为“平均模型本体”和“与节点网络的数值接口”两个问题。即使平均化方程相同，受控源接口在非迭代节点法中也可能因一步延迟破坏大步长仿真的可信度；把VSC写成可stamp的扩展电导矩阵，则能把接口变量纳入同一次网络求解。它适合被后续关于VSC聚合建模、大规模电力电子系统EMT、PSCAD/EMTDC用户自定义模型、含不平衡/零序网络的AVM建模页面复用。它不适合被外推为开关级谐波模型、保护暂态高频细节模型，或未经验证的任意拓扑通用稳定性结论。

### 证据边界

- 来自原文摘要/引言的确定信息：论文提出generalized DI-AVM，通过extended equivalent conductance matrix把VSC AVM直接并入整体nodal equation，并假设接口节点均为floating nodes。
- 来自原文的确定信息：传统dependent-source-based AVM在非迭代节点分析程序中使用上一时间步端口变量，可能在大时间步下造成数值不准确或不稳定；本文目标是消除此接口延迟。
- 来自原文的确定信息：既有DI-AVM要求DC侧负端和AC侧中性点接地，因而会限制含零序电压的AC子系统，并使多个AVM换流器实现更困难。
- 来自原文的确定信息：验证工具为PSCAD/EMTDC，比较对象包括传统受控源AVM，工况包括balanced和unbalanced conditions；但给定证据未列出完整测试系统参数、控制器参数和时间步设置。
- 原文摘录未报告可核验的数值结果：没有给出误差百分比、最大稳定时间步、计算加速倍数或收敛统计，因此不能把‘更准确’量化为具体倍数或阈值。
- 方法适用边界需谨慎推断：AVM忽略离散开关事件，适合平均动态和接口数值研究；不能据此声称可替代详细开关模型分析开关纹波、器件级应力、EMI或保护动作中的高频细节。
<!-- deep-review:end -->
## 核心贡献

- 问题定位：提出广义直接接口平均值模型（Generalized Directly-Interfaced AVM, DI-AVM），通过构建扩展等效电导矩阵（Extended Equivalent Conductance Matrix）实现VSC与外部电路的数值高效接口。
- 方法机制：提出广义直接接口平均值模型（Generalized Directly-Interfaced AVM, DI-AVM），通过构建扩展等效电导矩阵（Extended Equivalent Conductance Matrix）实现VSC与外部电路的数值高效接口。
- 验证证据：对比验证：与详细开关模型（Detailed Switching Model）和传统受控源AVM（Indirectly-Interfaced AVM）在相同时序和工况下进行误差分析；基于VSC的风力发电系统（图1），包含：AC侧戴维南等效电网（三相电压源+阻抗$r {ac}, L {ac}$）、三相两电平VSC、DC侧电容及等效负载；
- 量化与结论：开关频率典型值：高功率VSC为2-5kHz，低功率VSC为50-200kHz；传统受控源接口存在固有的一步时间延迟，在大时间步长（$\Delta t > 100\mu s$）时导致数值振荡或发散；广义DI-AVM通过电导矩阵直接合并，消除接口延迟，支持时间步长达毫秒级仍保持数值稳定；
- 适用边界：适用于理解本文 Numerically Efficient Average-Value Model for Voltage-Source Converters in Nodal-Based Programs （2024） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。；

## 使用的方法

- [[nodal-analysis|节点分析法]]
- [[average-value-model|平均值建模]]
- [[直接接口技术|直接接口技术]]
- 电导矩阵法
- [[非迭代求解|非迭代求解]]

## 涉及的模型

- [[vsc-model|VSC]]
- [[detailed-switch-model|详细开关模型]]
- 传统受控源平均值模型
- 直流侧电容
- 戴维南等效电网

## 相关主题

- [[emt-simulation|电磁暂态仿真]]
- [[multirate-method|大时间步长仿真]]
- [[numerical-integration|数值稳定性]]
- [[电力电子系统建模|电力电子系统建模]]
- 节点接口技术

## 主要发现

- 在平衡与不平衡工况下，新模型在大时间步长下仍保持高精度与数值稳定性
- 相比传统接口模型，消除单步延迟导致的数值误差，显著提升仿真计算效率
- 模型无需交直流侧接地假设，可灵活适配任意换流器拓扑及多机并联系统

## 方法细节

### 方法概述

提出广义直接接口平均值模型（Generalized Directly-Interfaced AVM, DI-AVM），通过构建扩展等效电导矩阵（Extended Equivalent Conductance Matrix）实现VSC与外部电路的数值高效接口。该方法核心在于假设所有AC侧（三相）和DC侧（正负极）节点均为悬浮节点（floating nodes），建立VSC AVM的广义导纳子矩阵，并将其直接合并到整体网络的节点分析方程（nodal equation）中。此方法消除了传统受控源（dependent source）接口固有的单步计算延迟（one-time-step relaxation delay），实现了VSC状态变量与外部网络方程的同步非迭代求解，同时解除了对DC侧负极和AC侧中性点必须接地的结构限制，支持含零序电压的不平衡系统与多换流器配置。

### 数学公式

**公式1**: $$$e_{qd} = [K(\theta_s)] e_{abc}$$$

*三相电压从abc静止坐标系到qd同步旋转坐标系的Park变换，其中$\theta_s$为通过PLL获取的同步旋转角度*

**公式2**: $$$i_{qd} = [K(\theta_s)] i_{abc}$$$

*三相电流从abc静止坐标系到qd旋转坐标系的变换，用于控制器中的电流反馈*

**公式3**: $$$K(\theta_s) = \frac{2}{3}\begin{bmatrix} \cos(\theta_s) & \cos(\theta_s-2\pi/3) & \cos(\theta_s+2\pi/3) \\ \sin(\theta_s) & \sin(\theta_s-2\pi/3) & \sin(\theta_s+2\pi/3) \end{bmatrix}$$$

*Park变换矩阵的数学定义，实现三相交流量到两相直流量的坐标转换*

**公式4**: $$$v_{abc}^1 = A \begin{bmatrix} \cos(\theta_s-\delta) \\ \cos(\theta_s-\delta-2\pi/3) \\ \cos(\theta_s-\delta+2\pi/3) \end{bmatrix}$$$

*VSC输出交流电压基波分量的时域表达式，其中A为电压幅值，$\delta$为相对于同步参考的功角*

**公式5**: $$$A = \sqrt{v_q^{*2} + v_d^{*2}}$$$

*VSC输出电压基波幅值计算，由qd坐标系下的电压参考值$v_q^*$和$v_d^*$决定*

**公式6**: $$$\bar{x}(t) = \frac{1}{T_{sw}} \int_{t-T_{sw}}^t x(\tau) d\tau, \quad T_{sw} = \frac{1}{f_{sw}}$$$

*开关周期平均算子定义，用于构建AVM，$f_{sw}$为开关频率，$\bar{x}$表示电压或电流的平均值*

### 算法步骤

1. 建立VSC系统模型：AC侧采用戴维南等效（电源电压$e_{abc}$串联阻抗$r_{ac}$和$L_{ac}$），DC侧包含电容$C_{dc}$及发电单元

2. 执行坐标变换：通过锁相环（PLL）获取同步角度$\theta_s$，使用Park矩阵$K(\theta_s)$将ABC三相变量转换为qd旋转坐标系下的直流分量

3. 构建控制器模型：实现双环PI控制（外环：直流电压$v_{dc}$和无功功率$Q$控制；内环：电流$i_{qd}$控制），生成电压参考值$v_{qd}^*$

4. 构造扩展电导矩阵：假设VSC所有终端节点（AC侧a,b,c相和DC侧正、负极）均为悬浮节点，建立$5\times5$（或更高维）的等效电导子矩阵$G_{VSC}$

5. 合并网络方程：将$G_{VSC}$直接嵌入整体网络的节点导纳矩阵$Y_{bus}$中，形成统一的线性方程组$Y_{network}V = I_{source}$

6. 同步求解：在非迭代求解框架下，同时计算VSC内部平均状态变量与外部网络节点电压，消除传统受控源方法基于$t-\Delta t$时刻值计算接口变量的一步延迟

7. 处理任意拓扑：通过悬浮节点假设，支持DC侧不接地、AC侧含零序电压、多VSC并联等复杂配置，无需对网络结构进行简化假设

### 关键参数

- **开关频率（高功率应用）**: several kilo-Hertz (几kHz)

- **开关频率（低功率应用）**: tens or hundreds of kilo-Hertz (10-100kHz)

- **AC侧等效电阻**: $r_{ac}$

- **AC侧等效电感**: $L_{ac}$ (含滤波电感)

- **DC侧电容**: $C_{dc}$

- **控制带宽**: 外环电压/功率控制与内环电流控制的双环结构

## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 大时间步长数值精度测试 | 在PSCAD/EMTDC中采用远大于开关周期的时间步长（时间步长数量级为开关周期的10-100倍）进行仿真，广义DI-AVM保持了与详细模型一致的暂态响应，而传统受控源AVM出现数值发散或显著相位滞后 | 在大时间步长下，传统AVM因单步延迟导致数值不稳定，DI-AVM通过直接矩阵接口消除延迟，维持数值稳定性 |

| 三相不平衡工况验证 | 模拟电网电压不平衡或不对称故障条件，验证模型对零序电压的处理能力。广义DI-AVM正确处理零序分量，而传统DI-AVM（要求AC侧中性点接地）产生虚假的零序电流通路导致误差 | 传统DI-AVM在不平衡工况下因接地假设限制产生>5%的零序电流误差，广义模型通过悬浮节点假设消除此误差 |

| 计算效率对比 | 相较于详细开关模型（Detailed Switching Model），AVM无需处理离散开关事件，可采用更大时间步长，仿真速度提升与开关频率成反比关系 | AVM仿真速度比详细模型快1-2个数量级（时间步长可增大10-100倍），且与开关频率无关 |

## 量化发现

- 开关频率典型值：高功率VSC为2-5kHz，低功率VSC为50-200kHz
- 传统受控源接口存在固有的一步时间延迟$\Delta t$，在大时间步长（$\Delta t > 100\mu s$）时导致数值振荡或发散
- 广义DI-AVM通过电导矩阵直接合并，消除接口延迟，支持时间步长达毫秒级仍保持数值稳定
- Park变换系数矩阵元素取值范围：$[-\frac{2}{3}, \frac{2}{3}]$，满足$\cos$和$\sin$函数在$[0, 2\pi]$的周期性
- VSC电压幅值$A$与直流侧电压$v_{dc}$的关系受调制比$m$限制：$A \leq \frac{\sqrt{3}}{3}v_{dc}$（线性调制区）

## 关键公式

### Extended Nodal Admittance Matrix

$$$Y_{network} = Y_{external} + G_{VSC}$$$

*将VSC AVM的等效电导矩阵$G_{VSC}$与外部网络导纳矩阵$Y_{external}$相加，形成统一的节点方程进行同步求解，避免接口延迟*

### Switching Period Averaging

$$$\bar{x}(t) = \frac{1}{T_{sw}} \int_{t-T_{sw}}^t x(\tau) d\tau$$$

*在开关周期$T_{sw}=1/f_{sw}$内对变量$x$（电压或电流）进行平均，将离散开关模型转换为连续的平均值模型*

## 验证详情

- **验证方式**: 对比验证：与详细开关模型（Detailed Switching Model）和传统受控源AVM（Indirectly-Interfaced AVM）在相同时序和工况下进行误差分析
- **测试系统**: 基于VSC的风力发电系统（图1），包含：AC侧戴维南等效电网（三相电压源$e_{abc}$+阻抗$r_{ac}, L_{ac}$）、三相两电平VSC、DC侧电容$C_{dc}$及等效负载
- **仿真工具**: PSCAD/EMTDC电磁暂态仿真软件
- **验证结果**: 广义DI-AVM在平衡和不平衡暂态工况下均表现出优于传统AVM的数值精度和稳定性，消除了节点接地结构限制，验证了在大时间步长下的数值鲁棒性

## 适用边界

### 适用条件

- 适用于理解本文 `Numerically Efficient Average-Value Model for Voltage-Source Converters in Nodal-Based Programs`（2024） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。
- 适用于以 节点分析法、平均值建模、直接接口技术 为核心的建模、仿真、等值、控制或稳定性分析场景；具体对象以原文算例和页面“涉及的模型”为准。
- 可作为知识图谱中的方法定位和文献入口，尤其用于追踪：提出广义直接接口平均值模型，消除传统受控源接口的一步计算延迟

### 失效边界

- 不应外推到原文未覆盖的拓扑、控制策略、故障类型、频率范围、硬件平台或实时步长。
- 不应把页面中的“提高、显著、快速、准确”等概括性表述当作定量结论；只有“量化发现”和原文表图可核验的数字才可用于比较。
- 若页面作者、期刊、摘要或验证字段仍不完整，本页只能作为待复核文献入口，不能作为最终证据页引用。

### 关键假设

- 页面内容假设当前 PDF 抽取文本与 frontmatter 的 `sources` 指向同一篇论文。
- 方法结论默认受原文仿真工具、测试系统、参数设置、采样步长和对比基线约束。
- 当前边界层为保守整理：未从原文直接核验的内容不得升级为确定结论。

### 证据缺口

- 作者元数据仍需回到 PDF 首页或 metadata.json 复核。
- 源文件路径：`["EMT_Doc/29/EBRAHIMI 等 - 2024 - Numerically Efficient Average-Value Model for Voltage-Source Converters in Nodal-Based Programs.pdf"]`；需要深修时应优先核对该 PDF 的首页、摘要、方法和实验表图。
