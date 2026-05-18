---
title: "EMTP-ATP"
type: method
tags: [emtp-atp, emt-simulation, transient-analysis, alternative-transients-program, atpdraw, companion-circuit, trapezoidal-rule, nodal-analysis]
created: "2026-05-11"
updated: "2026-05-18"
---

# EMTP-ATP

## 1. 物理背景与工程需求

EMTP-ATP（Alternative Transients Program）是电磁暂态仿真程序 EMTP 家族的一个免费开源分支版本，由加拿大/欧洲用户协会（EEUA）维护。其工程背景是：输电系统遭受雷击、开关操作、故障及铁磁谐振等暂态过程时，电压和电流的瞬态变化时间尺度在微秒至毫秒级，稳态相量法无法描述这一阶段的波形细节。EMTP 类程序正是为分析这类电磁暂态过程而设计（Dommel 1969）。

ATP 版作为 EMTP 最早公开发布的免费版本，长期被学术研究和工程分析用于过电压计算、绝缘配合、保护系统校验和电力电子暂态仿真。Colqui 等（2022）利用 ATP 的开放性，以理想变压器阵列实现了 Clarke 模态变换电路，将模态域线路模型直接嵌入节点导纳矩阵，突破了 ATP 内置三相线路模型的封装限制。

ATP 的核心求解方法延续 Dommel 的伴随电路法（companion circuit），将微分方程通过梯形数值积分（trapezoidal rule）离散化为等效电阻网络，每时步求解节点导纳方程。其独特需求在于：ATP 同时支持 TACS（Transient Analysis of Control Systems）和 MODELS 语言用于控制系统建模，以及 LCC、JMarti、Semlyen 等多类输电线路模型用于波过程计算。

ATP 与商业版本 EMTP-RV 的主要区别在于：ATP 完全开放数据文件格式，用户可直接修改元件模型和数值方法；而 EMTP-RV 通过 EMTPWorks 生成 .NET 网络表，引擎采用改进非线性迭代算法求解，不对用户开放底层接口（Cao & Chen 2007）。EEUA 维护的 ATP 版本至今保持每年更新，吸引了大量研究者贡献代码（如 Colqui 2022 的模态域扩展）。

## 2. 数学描述

### 2.1 伴随电路法的核心原理

ATP 的时域求解建立在 Dommel 伴随电路法基础之上。伴随电路是连接微分方程与代数方程的核心桥梁——它把储能元件（电感、电容）的微分方程，通过数值积分在每个时步转化为诺顿等效电路（电导并联历史电流源）。

以电感 $L$ 为例，其微分方程 $v_L = L \, di_L/dt$ 通过梯形积分法在时步 $\Delta t$ 下离散化。从 $t_{k-1}$ 积分到 $t_k$：

$$
i_k = i_{k-1} + \frac{1}{L} \int_{t_{k-1}}^{t_k} v(\tau) d\tau \approx i_{k-1} + \frac{\Delta t}{2L}(v_k + v_{k-1})
$$

整理为诺顿等效的标准形式 $i_k = G_{\text{eq}} v_k + I_{\text{hist}}$：

$$
i_k = \underbrace{\frac{\Delta t}{2L}}_{G_{\text{eq},L}} v_k + \underbrace{\left(i_{k-1} + \frac{\Delta t}{2L} v_{k-1}\right)}_{I_{\text{hist},L}^{k-1}}
$$

其中 $G_{\text{eq},L} = \Delta t/(2L)$ 为等效电导（仅与元件参数和步长有关），$I_{\text{hist},L}^{k-1}$ 为历史电流源（包含上一时步的储能记忆）。

电容 $C$ 的伴随模型类似，其微分方程 $i_C = C \, dv_C/dt$ 离散化后：

$$
i_k = \underbrace{\frac{2C}{\Delta t}}_{G_{\text{eq},C}} v_k - \underbrace{\left(\frac{2C}{\Delta t} v_{k-1} + i_{k-1}\right)}_{I_{\text{hist},C}^{k-1}}
$$

注意电容的历史电流源多了一个负号——这是梯形法中积分方向不同造成的（MCC 常见 bug 来源）。

两种积分公式的等效电导对比：

$$
\begin{array}{c|cc}
\text{元件} & \text{梯形法 } G_{\text{eq}} & \text{后向欧拉 } G_{\text{eq}} \\
\hline
\text{电感} & \Delta t/2L & \Delta t/L \\
\text{电容} & 2C/\Delta t & C/\Delta t
\end{array}
$$

后向欧拉的等效电导更大（导纳更大），带来更强的数值阻尼，但精度从 $O(\Delta t^2)$ 降为 $O(\Delta t)$。

### 2.2 节点导纳方程的组装

将所有储能元件的伴随电路并入网络，得到每时步的线性方程组：

$$
\mathbf{G} \, \mathbf{v}(t) = \mathbf{i}(t)
$$

其中 $\mathbf{G}$ 为恒定节点导纳矩阵（当所有支路为线性时），$\mathbf{v}(t)$ 为节点电压向量，$\mathbf{i}(t)$ 由独立源和历史电流源构成（Dommel 1969）。

关键性质：**如果步长不变，所有动态元件的等效电导在整个仿真过程中保持不变**。进而 $\mathbf{G}$ 也保持不变，只需做一次 LU 分解，之后每步只做前代回代——这是 ATP 计算效率的根本来源。

### 2.3 输电线路的模态解耦

对于完全换位三相线路，ATP 将相域传输方程通过 Clarke 或 Karrenbauer 变换转换至模态域：

$$
\mathbf{V} = \mathbf{T}_v \mathbf{V}_m, \quad \mathbf{I} = \mathbf{T}_i \mathbf{I}_m
$$

设相域-模域变换矩阵为 $\mathbf{T}$，则模域解耦方程为：

$$
-\frac{d\mathbf{V}_m}{dx} = \mathbf{Z}_m \mathbf{I}_m, \quad -\frac{d\mathbf{I}_m}{dx} = \mathbf{Y}_m \mathbf{V}_m
$$

其中 $\mathbf{Z}_m = \mathbf{T}^{-1} \mathbf{Z} \mathbf{T}$，$\mathbf{Y}_m = \mathbf{T}^{-1} \mathbf{Y} \mathbf{T}$ 近似或严格对角化。第 $k$ 个模态的传播常数和特性阻抗为：

$$
\gamma_k = \sqrt{Z_{mk} Y_{mk}}, \quad Z_{ck} = \sqrt{Z_{mk}/Y_{mk}}
$$

Clarke 变换矩阵（实数常数）为：

$$
\mathbf{T}_{\text{Clarke}} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & -2 & 1 \\ 1 & 1 & -2 \end{bmatrix} / 3
$$

其 8 个非零元素可映射为理想变压器的变比与极性。Colqui 等（2022）利用这一特性，在 ATP 中以 8 个理想变压器实现了 Clarke 变换矩阵电路，将三相完全换位线路解耦为 $\alpha$、$\beta$、0 三个独立模态后再连接单相 Bergeron 或 JMarti 模型。

## 3. 计算模型与离散化

ATP 属于固定步长 EMT 程序，其离散化体现在三个层面：

### 3.1 伴随电路的离散化

梯形积分法将各储能元件的微分方程转化为诺顿等效电路（电阻并联历史电流源），全部并入节点导纳矩阵 $\mathbf{G}$。当 $\mathbf{G}$ 不随时间变化时，可预先 LU 分解并重复使用——这是 ATP 计算效率的重要来源。

### 3.2 输电线路的模态解耦与离散化

对完全换位三相线路，ATP 将相域传输方程通过 Clarke 或 Karrenbauer 变换转换至模态域，每个模态按单相线路模型（如 Bergeron 常参数模型或 JMarti 频变模型）处理。Colqui 等（2022）通过理想变压器阵列在 ATP 中实现此变换，频域扫描与理论解对比幅值误差低于 0.1%，相位误差低于 0.05°。各模态的传播延迟可独立处理，使长线路的仿真步长不受传播时间限制——结合 Folded Line 等效模型时，仿真速度提升约 3 倍。

### 3.3 开关与非线性的离散化

晶闸管、避雷器、饱和电抗器等非线性元件通过补偿法（compensation method）或分段线性化在每时步处理。理想开关在 $t_{\text{on}}/t_{\text{off}}$ 时刻修改 $\mathbf{G}$ 的拓扑结构。由于 ATP 采用固定步长，开关动作时刻可能落在步长之间，由此产生的时间误差可能激发数值振荡——Lehn 等（1995）在 ATP 与 NETOMAC 对比 HVDC 仿真时指出，ATP 需要采用约 20 μs 的更小步长才能抑制此类振荡（对比 NETOMAC 的 100 μs 变步长插值方案）。

### 3.4 非线性磁滞元件的离散化

变压器饱和铁芯通过 Jiles-Atherton 磁滞模型建模。在 ATP 中，Zou（2018）通过磁电对偶原理将铁芯磁路转化为等效电气网络：铁芯磁链 $\psi$ 与磁化电流 $i_m$ 通过磁化电感 $L_m$ 关联，等效电路中的电感值随磁化曲线的切线电感变化。Jiles-Atherton 模型的磁化强度 $M$ 表示为：

$$
M = \frac{M_s}{\alpha} \arctanh\left(\frac{\alpha (H + M)}{\delta M_s}\right) - M_{an}
$$

其中 $M_s$ 为饱和磁化强度，$\alpha$ 为形状系数，$H$ 为磁场强度，$\delta$ 为方向系数，$M_{an}$ 为无磁滞磁化强度。对偶变换后的等效电路参数随磁化曲线更新，实现铁磁谐振的精确时域仿真。

## 4. 实现方法与算法细节

ATP 的仿真流程按如下步骤组织：

### 步骤 1 — 网络拓扑构建

用户通过 ATPDraw 图形界面或直接编写 ATP 数据文件（.atp 或 .dat）定义网络连接、元件参数和仿真控制参数。数据文件采用固定格式卡片，定义母线名称、RLC 元件值、线路参数、开关初始状态及 TACS/MODELS 控制系统。

### 步骤 2 — 稳态初始化

ATP 在时域仿真开始前执行稳态相量求解（频率由用户指定，通常为 50/60 Hz），确定所有节点电压和支路电流的初始条件，使暂态仿真从稳态而非零状态启动。这是 EMT 仿真区别于一般 ODE 求解的关键步骤——保证了仿真从系统稳态工作点开始。

### 步骤 3 — 伴随电路矩阵组装

根据拓扑和元件参数构建节点导纳矩阵 $\mathbf{G}$。线性网络中 $\mathbf{G}$ 为常数矩阵，仅当开关状态变化时更新。Cao 和 Chen（2007）描述了 EMTP-RV（ATP 的商业衍生版）的核心引擎处理流程：EMTPWorks 生成 .NET 网络表，引擎读取后构建稀疏导纳矩阵，再采用改进非线性迭代算法求解。ATP 的矩阵组装与 EMTP-RV 类似，采用稀疏行存储格式。

### 步骤 4 — 时步递推求解

每时步 $t_k = k\Delta t$ 计算各元件的诺顿等效电流源（包括历史项），形成 $\mathbf{i}(t_k)$，求解 $\mathbf{G} \, \mathbf{v}(t_k) = \mathbf{i}(t_k)$。若含非线性元件，则采用补偿法或 Newton-Raphson 迭代。

补偿法（compensation method）处理非线性元件的核心思想：将非线性元件从电路中"补偿"出去，剩余线性网络保持 $\mathbf{G}$ 不变；非线性元件端电压通过历史电流源迭代修正，每步只需一次额外的前代回代。

### 步骤 5 — 控制系统接口

TACS（Transient Analysis of Control Systems）和 MODELS 在每时步与网络求解交替执行：网络方程求解后，将节点电压/支路电流送入 TACS；TACS 计算控制输出后返回给网络作为下一时步的受控源。Lehn 等（1995）指出，TACS 的这种解耦执行方式会导致控制信号存在一个时步的延迟，对于快速控制环节可能显著影响仿真精度。

MODELS 语言提供更灵活的控制系统描述能力，允许用户定义非线性传递函数、条件语句和离散事件，适用于同步机励磁、调速器和 HVDC 极控等复杂控制逻辑。

### 步骤 6 — 后处理与谐波分析

结果写入二进制 .mda 文件和 ASCII .m 文件，ScopeView 或 ATP_Scope 读取后进行波形显示、FFT 和谐波分析。Zou（2018）在 ATP 平台上采用分岔图、相平面轨迹和庞加莱映射对三相铁磁谐振进行非线性动力学分析，仿真与实验波形相似度大于 0.9，稳态峰值误差小于 5%。

## 5. 适用边界与失效模式

### 5.1 适用条件

- **过电压与绝缘配合**：雷电过电压、操作过电压和铁磁谐振分析是 ATP 的传统优势领域，Zou（2018）的 225 VA 三相变压器铁磁谐振实验验证了 ATP 在非线性磁滞建模和动力学分析方面的能力。
- **输电线路波过程**：支持 JMarti、Semlyen 频变模型和 Bergeron 常参数模型，Colqui 等（2022）的模态域扩展方法使自定义线路模型可在 ATP 中直接搭建。
- **电力电子暂态**：支持晶闸管等理想开关建模，Lehn 等（1995）将其用于 600 MW/400 kV 单极 HVDC 的跨平台验证，ATP 需要 20 μs 步长方可消除数值振荡。
- **控制系统仿真**：TACS 和 MODELS 支持较灵活的控制系统建模，适用于同步机励磁、调速和 HVDC 极控等基本控制环节。

### 5.2 失效边界

- **固定步长限制**：ATP 采用固定步长，不提供变步长/插值功能。Lehn 等（1995）在 HVDC 对比中明确指出，固定步长导致晶闸管开关时刻误差，可能引发数值振荡，需要缩小步长（如 20 μs）来补偿。
- **控制-网络解耦延迟**：TACS 在每时步中滞后于网络方程求解，存在一个时步的控制信号延迟。对于需要同步求解的快速功率电子控制（如 VSC 的电流内环），此延迟可能显著影响精度。
- **大规模网络性能**：ATP 的矩阵求解基于稠密/稀疏直接法，缺乏 SSN（State-Space Nodal）或 MATE（Multi-Area Thévenin Equivalent）等现代分网加速技术，面对含大量开关元件的大型网络时性能受限。
- **用户界面限制**：ATPDraw 图形界面功能弱于 PSCAD/EMTDC 或 EMTP-RV；数据文件采用固定格式卡片，参数修改和模型复用不如现代 EMT 工具方便。
- **数值振荡敏感性**：梯形法不是 L-稳定的（$R(z) \to -1$ 当 $z \to -\infty$），高频数值分量步间换号不衰减。开关突变形组件（如饱和电抗器）之后可能激发非物理数值振荡，需要用后向欧拉预插值或滤波来抑制。

## 6. 应用案例

**案例 1：三相铁磁谐振的精确仿真。** Zou（2018）在 EMTP-ATP 上构建了三相五柱变压器的 Jiles-Atherton 磁滞模型，通过磁电对偶原理将铁芯磁路转化为等效电气网络，同时建立了含截流、介质耐压恢复和高频熄弧能力的真空断路器（VCB）模型。在 225 VA 三相 Y/Y 变压器实验平台上验证了基波和次谐波铁磁谐振，仿真与实验波形相似度大于 0.9，稳态电压峰值误差小于 5%（最大 4.90%），过电压倍数预测偏差小于 0.06 p.u.。庞加莱映射准确复现了 A 相基波（1 点）和次谐波（3 点）的多稳态特征。

**案例 2：ATP 中模态域输电线路模型的自定义实现。** Colqui 等（2022）利用 8 个理想变压器搭建 Clarke 变换矩阵电路（对应 Clarke 矩阵的相域 $\rightarrow$ 模态域映射），将三相完全换位线路解耦为 $\alpha$、$\beta$、0 三个独立模态后分别连接单相 Bergeron 或 JMarti 模型。在 ATP-EMTP v7.0p7/ATPDraw 平台上实现，频域扫描与理论解对比幅值误差低于 0.1%、相位误差低于 0.05°，时域暂态波形最大相对误差低于 0.5%，上升沿时间偏差低于 2 ns。该方法将自定义频变土壤参数直接嵌入线路模型，突破了 ATP 内置三相模型无法参数化扩展的限制。

**案例 3：跨平台 HVDC 仿真对比。** Lehn 等（1995）在 ATP 和 NETOMAC 上建立 600 MW/400 kV 单极 HVDC 测试系统（含 66 km 海底电缆、直流阻波滤波器，SCR=5.0），通过精确对齐 PI 控制器限幅逻辑和变压器饱和数据，发现 ATP 需采用 20 μs 步长才能抑制固定步长导致的晶闸管触发延迟误差，而 NETOMAC 因其变步长与开关线性插值机制在 100 μs 步长下即可获得一致结果。精细校准后两程序在交直流故障暂态波形上高度一致。

## 7. 量化性能边界

| 验证研究 | 测试系统 | 关键指标 | 数值结果 |
|---------|---------|---------|---------|
| Zou 2018 | 225 VA 三相 Y/Y 变压器，铁磁谐振 | 波形相似度 | > 0.9 |
| Zou 2018 | 225 VA 三相 Y/Y 变压器，铁磁谐振 | 稳态峰值误差 | < 5%（最大 4.90%） |
| Zou 2018 | 225 VA 三相 Y/Y 变压器，铁磁谐振 | 过电压倍数偏差 | < 0.06 p.u. |
| Colqui 2022 | ATP-EMTP v7.0p7，Clarke 变换+理想变压器阵列 | 频域幅值误差 | < 0.1% |
| Colqui 2022 | ATP-EMTP v7.0p7，Clarke 变换+理想变压器阵列 | 频域相位误差 | < 0.05° |
| Colqui 2022 | ATP-EMTP v7.0p7，Clarke 变换+理想变压器阵列 | 时域波形最大相对误差 | < 0.5% |
| Colqui 2022 | ATP-EMTP v7.0p7，Clarke 变换+理想变压器阵列 | 上升沿时间偏差 | < 2 ns |
| Colqui 2022 | ATP-EMTP v7.0p7，Clarke+折叠线等效 | 仿真速度提升 | ~3× |
| Lehn 1995 | ATP vs NETOMAC，600 MW/400 kV HVDC | ATP 抑制振荡所需步长 | 20 μs |
| Lehn 1995 | ATP vs NETOMAC，600 MW/400 kV HVDC | NETOMAC 等效步长 | 100 μs（变步长插值） |

**数据缺口声明**：EMTP-ATP 的量化性能数据来自三个独立方向的验证（线路模型对比、跨平台仿真对比、铁磁谐振实验验证），各自使用不同的测试系统和评估指标，不可直接横向比较为 ATP 的整体性能。ATP 与传统 EMTP-RV、PSCAD 等商业工具在现代大规模电力电子化系统下的全面性能对比数据缺失。

## 8. 延伸阅读

- **伴随电路法与梯形积分**：ATP 的底层求解器基于 Dommel 伴随电路方法，详细推导见 [[companion-circuit]] 和 [[trapezoidal-rule]] 方法页。
- **节点分析**：ATP 每时步求解节点导纳方程，理论基础见 [[nodal-analysis]]（位于 [[companion-model]] 页面中描述的系统方程组装）。
- **输电线路模型**：ATP 中的 JMarti 频变模型和 Bergeron 常参数模型见 [[frequency-dependent-line-model]]（JMarti）和 [[bergeron-model]]（Bergeron）。
- **模态变换**：Clarke/Karrenbauer 模态变换的理论基础见 [[modal-transformation]]。
- **开关与非线性处理**：补偿法和理想开关建模原理见 [[compensation-method]]。
- **实体页**：ATP 工具生态和版本信息见 [[atp-emtp]] 实体页；EMTP-RV 商业版本信息见 [[emtp]] 实体页。
- **跨平台对比**：Lehn（1995）的 ATP 与 NETOMAC HVDC 对比研究是理解固定步长与变步长差异的重要文献。
- **铁磁谐振**：Zou（2018）的 ATP 铁磁谐振建模方法适用于变压器非线性激磁和断路器暂态研究。
- **Jiles-Atherton 磁滞模型**：详见 [[jiles-atherton-model]] 方法页。

## 9. 来源论文

| 论文 | 年份 | 贡献说明 |
|------|------|---------|
| [[accurate-simulation-model-for-a-three-phase-ferroresonant-circuit-in-emtpatp]] | 2018 | Jiles-Atherton 磁滞模型+铁磁谐振实验验证，庞加莱映射多稳态分析 |
| Colqui et al. (ATP-EMTP v7.0p7/ATPDraw) | 2022 | Clarke 变换矩阵电路，模态域输电线路自定义实现，频域误差<0.1% |
| Lehn et al. (ATP vs NETOMAC) | 1995 | 600 MW/400 kV HVDC 跨平台对比，固定步长数值振荡分析 |
