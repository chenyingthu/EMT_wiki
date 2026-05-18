---
title: "电力系统网络 (Power System Network)"
type: topic
tags: [power-system, network-topology, nodal-analysis, network-equivalent, emt-integration, grid-modeling, parallel-computation, multi-rate]
created: "2026-05-04"
updated: "2026-05-15"
---

# 电力系统网络 (Power System Network)

## 定义

电力系统网络是指由发电、输电、变电、配电和用电设备通过电气连接构成的能量传输与分配系统。在EMT（电磁暂态）仿真语境中，网络特指需要详细电磁暂态建模的电网部分，其核心数学表示为节点导纳矩阵与伴随电路方程的组合。与采用简化等值的外部系统或机电暂态模型形成边界，网络部分保留了线路的分布参数特性、频变效应、开关动态以及电力电子设备的精确建模。

**边界限定**：本页面聚焦于EMT仿真中的网络表示方法，涵盖网络拓扑建模、节点方程求解、网络等值、多速率联合仿真以及并行计算等核心机制，不替代潮流计算或机电暂态稳定分析的基础教材内容。

## EMT中的角色

电力系统网络是EMT仿真的核心对象，其作用体现在四个层面：

**详细建模层**：网络中的关键设备（换流器、FACTS、新能源接口、HVDC）需要详细的电磁暂态模型，包括分布参数线路、频变电缆、非线性变压器饱和等。这些设备决定了暂态过程的物理真实性。

**等值边界层**：外部网络通过戴维南/诺顿等值、Ward等值、REI等值或FDNE（频变网络等值）简化表示。等值边界的选择应保留关键动态特性，避免在宽频带仿真中滤除重要谐振模式。

**混合仿真接口层**：与机电暂态仿真的网络分割与数据交换，通过MD-TLM（多域传输线模型）或SFP（移频相量）接口实现多时间尺度耦合。这是大规模系统仿真的关键瓶颈。

**过电压与保护分析层**：网络拓扑对操作过电压、雷击过电压、开关暂态的分布起决定作用。线路长度、接地方式、中性点配置直接影响暂态电压幅值和传播路径。

## 网络建模体系架构

电力系统网络在EMT仿真中可划分为五个层次，从物理拓扑到数值求解逐层递进：

```
┌─────────────────────────────────────────────────────────┐
│ 第1层：物理拓扑 (Physical Topology)                      │
│  发电机/变压器/线路/负荷/电力电子设备 → 节点-支路图      │
│  ↓                                                       │
│ 第2层：元件电磁模型 (Component EMT Models)               │
│  分布参数线路/频变电缆/非线性变压器/动态负荷              │
│  ↓                                                       │
│ 第3层：网络方程组装 (Network Equation Assembly)          │
│  MANA节点导纳矩阵 + 伴随电路离散 + 历史项注入            │
│  ↓                                                       │
│ 第4层：数值求解 (Numerical Solution)                     │
│  稀疏矩阵分解(KLU/BBD) + 牛顿迭代 + 并行求解             │
│  ↓                                                       │
│ 第5层：系统级扩展 (System-level Extensions)              │
│  网络等值/FDNE/多速率/并行计算/混合仿真                  │
└─────────────────────────────────────────────────────────┘
```

### 第1层：物理拓扑表示

网络拓扑描述了元件之间的电气连接关系，是EMT仿真的输入基础。

**节点-支路模型**：以节点电压为未知量，支路电流为辅助变量，形成导纳矩阵Y或阻抗矩阵Z。这是EMTP类软件的标准表示方式。节点电压方程为：

$$\mathbf{Y}(s)\mathbf{V}(s) = \mathbf{I}(s)$$

其中$\mathbf{Y}(s)$为节点导纳矩阵（可为频变形式），$\mathbf{V}(s)$为节点电压向量，$\mathbf{I}(s)$为注入电流向量。

**改进增广节点分析法（MANA）**：传统节点分析在处理含受控源、非线性元件和变压器时面临困难。Abusalah 2018提出的MANA方法通过引入附加方程系数矩阵，将节点电压与支路电流统一为全局非对称稀疏矩阵：

$$\begin{bmatrix} Y_n & A_c \\ A_r & A_d \end{bmatrix} \begin{bmatrix} v_n \\ i_x \end{bmatrix} = \begin{bmatrix} i_n \\ v_x \end{bmatrix}$$

其中$Y_n$为节点导纳矩阵，$A_c$、$A_r$、$A_d$为附加模型方程系数矩阵，$v_n$为节点电压未知量，$i_x$为支路电流或模型内部接口量。MANA的优势在于：(1) 统一处理线性/非线性元件；(2) 自动纳入变压器绕组耦合；(3) 支持开关模型直接嵌入。

**母线-断路器模型**：详细开关状态与拓扑变化建模，用于保护分析和故障仿真。拓扑变化时通过重新形成导纳矩阵或动态更新伴随电路参数处理。

**分层分区表示**：输电层、配电层、用户层的不同建模粒度。输电层采用详细分布参数模型，配电层可采用集总参数π型等值，用户层可采用恒定功率/阻抗负荷模型。

### 第2层：元件电磁模型

网络中的每个元件在EMT仿真中都有对应的电磁暂态模型，模型精度与计算效率之间存在权衡。

**输电线路模型**：

集中参数π型等值：适用于短线路（< 80 km），将线路R、L、C参数集中在三个支路中。其导纳矩阵为：

$$Y_{\pi} = \begin{bmatrix} Y + \frac{Y_s}{2} & -Y \\ -Y & Y + \frac{Y_s}{2} \end{bmatrix}$$

其中$Y$为串联支路导纳，$Y_s$为并联支路导纳。

分布参数线路模型：适用于中长线路，基于电报方程求解。时域离散后形成伴随电路：

$$i(t) = Y_{eq} \cdot v(t) + i_h(t - \Delta t)$$

其中$Y_{eq}$为等效电导，$i_h(t - \Delta t)$为历史项电流，包含传播延迟效应。分布参数模型的自然延迟特性在BTF（块三角分解）并行中形成天然的网络解耦边界。

频变线路模型：考虑大地回路频率相关特性，采用JMarti频变模型或CVF（连续矢量拟合）频移逼近。Duarte 2023评估了不同频变模型在地下电缆系统中的准确性，指出50 m/100 m地下电缆在10 kHz以上频率需采用频变模型，集总参数假设误差可达10-20%。

**变压器模型**：多绕组+饱和+频变特性。白盒变压器模型（Gustavsen 2020）在EMT仿真中采用时域实现阻尼因子，饱和特性通过磁化曲线非线性映射。

**动态负荷模型**：感应电机负荷、ZIP（恒阻抗/恒电流/恒功率）组合模型。Induction Machine Model in the Phase Domain (Gao 2022) 提出基于恒定等效导纳矩阵的相域模型，在EMT仿真中保持数值稳定性。

**电力电子设备模型**：换流器、SVG、STATCOM等采用开关模型、平均值模型或混合建模。Sano 2022提出的五类模型对比（SW/VI/AV/CCI/SCI）是通用框架，每个模型标注步长缩放因子、加速比、精度误差、适用场景和失效场景。

### 第3层：网络方程组装

每个时间步，网络方程需要重新组装，包含线性元件的伴随电路更新和非线性元件的线性化。

**伴随电路离散**：电感、电容用梯形积分离散为等效电导和历史电流。ParaEMT框架（Xiong 2024）中，电感并联$R_p \approx \frac{40L}{3\Delta t}$、电容串联$R_s \approx \frac{3\Delta t}{40C}$的人工阻尼电阻，用于抑制梯形法数值振荡。

离散化后的网络节点电压方程为：

$$\mathbf{G}\mathbf{v}(t) = \mathbf{i}(t) + \mathbf{i}_h(t - \Delta t)$$

其中$\mathbf{G}$为由线路、变压器、RLC支路及等效诺顿导纳组成的节点导纳矩阵，$\mathbf{v}$为三相瞬时节点电压向量，$\mathbf{i}$为外部或动态元件注入电流向量，$\mathbf{i}_h$保存伴随电路的历史项。

**非线性元件线性化**：非线性模型在第j次牛顿迭代时的线性化方程为：

$$i_k = y^{(j)} v_k + I_Q^{(j)}$$

其中$y$为工作点斜率，$I_Q$为截距电流。所有非线性元件（开关、铁芯饱和、非线性负荷）在牛顿迭代中同步更新等效斜率和注入项。

**历史项更新**：分布参数线路和频变元件的历史项包含传播延迟信息，是EMT仿真精度的关键。Mu 2014的网络分区并行算法中，历史项在分区边界处通过传输线模型传递。

### 第4层：数值求解

大规模网络的节点方程求解是EMT仿真的计算瓶颈，涉及稀疏矩阵分解、牛顿迭代收敛和并行计算。

**稀疏矩阵求解器**：传统EMTP使用LU分解，而KLU求解器（Abusalah 2018）采用近似最小度(AMD)排序，最小化LU分解过程中的填充元(fill-in)。KLU单线程求解器相比传统EMTP稀疏求解器基础提速约1.15倍。

**块三角分解（BTF）自动撕裂**：Abusalah 2018的核心创新是通过行/列置换矩阵$P_R$和$P_C$将原矩阵重排为块三角形式：

$$A_{BTF} = P_R A P_C$$

利用分布参数线路/电缆模型固有的时间延迟特性，自动识别由输电线路造成的计算独立性，将全局导纳矩阵撕裂为多个相互独立的对角子块。这一过程无需人工干预，在仿真初始化阶段执行一次符号分析后自动完成。

**加边块对角矩阵（BBD）分解**：ParaEMT框架（Xiong 2024）采用BBD分解将稀疏矩阵G自动划分为对角块与加边块，通过MPI通信协议将各子块分配至不同计算节点，并行执行局部LU分解、前代与回代运算。

**牛顿迭代收敛**：在每个积分步长$\Delta t$内，若检测到斜率变化或开关动作，则进入全迭代牛顿循环。Abusalah 2018在T0网络（含DFIG详细IGBT模型）中，平均牛顿迭代6.04次/步。

### 第5层：系统级扩展

面向大规模系统的网络处理方法，包括等值降阶、多速率联合仿真和并行计算。

**网络等值方法**：

| 等值类型 | 原理 | 适用场景 | 局限性 |
|---------|------|---------|--------|
| Ward等值 | 基于潮流的静态等值 | 机电暂态、稳态分析 | 不保留频变特性 |
| REI等值 | 保留外部系统关键电气特性 | 多区域互联系统 | 参数辨识复杂 |
| FDNE | 频变网络等值，有理逼近 | 宽频EMT分析、IBR系统 | 多端口耦合精度高 |
| 戴维南等值 | 单端口简化表示 | 远离非线性负荷 | 不适用于多馈入系统 |
| 动态等值 | 保留关键动态特性 | 同步机暂态、新能源场站 | 工作点依赖性强 |

**多速率联合仿真**：Li 2019提出的SFP-EMT多速率架构，将大电网划分为SFP子系统（步长500 μs）和风电场EMT子系统（步长2-50 μs）。SFP子系统通过旋转矩阵变换将高频信号频谱下移至基频附近，在保留非线性与频变电磁暂态动态的同时，允许采用大步长。两子系统通过MD-TLM（多域传输线模型）接口耦合。

**并行计算**：

| 并行方法 | 原理 | 加速比 | 适用规模 |
|---------|------|--------|---------|
| KLU+BTF | CPU共享内存并行，自动撕裂 | 1.9-3.3× | 数千节点 |
| BBD+MPI | 分布式内存并行，加边块对角 | 15-18× | 万节点以上 |
| GPU并行 | 线程级并行，矩阵运算加速 | 10-40× | 大规模IBR系统 |
| 多速率 | 不同子系统不同步长 | 10-250× | 大电网+详细风场 |

## 形式化表达

### 核心方程汇总

**节点导纳矩阵方程（频域）**：

$$\mathbf{Y}(s)\mathbf{V}(s) = \mathbf{I}(s)$$

**MANA系统方程（时域）**：

$$\begin{bmatrix} Y_n & A_c \\ A_r & A_d \end{bmatrix} \begin{bmatrix} v_n \\ i_x \end{bmatrix} = \begin{bmatrix} i_n \\ v_x \end{bmatrix}$$

**离散化网络方程（伴随电路）**：

$$\mathbf{G}\mathbf{v}(t) = \mathbf{i}(t) + \mathbf{i}_h(t - \Delta t)$$

**BTF置换公式**：

$$A_{BTF} = P_R A P_C$$

**非线性元件线性化**：

$$i_k = y^{(j)} v_k + I_Q^{(j)}$$

**分布参数线路伴随电路**：

$$i(t) = Y_{eq} \cdot v(t) + i_h(t - \Delta t)$$

**SFP移频相量表示**：

$$x(t) = \hat{x}(t)e^{j\omega_s t}$$

其中$\hat{x}(t)$为慢变包络，$\omega_s$为基频角频率。

### 数值离散公式

**电感并联人工阻尼电阻**：

$$R_p \approx \frac{40L}{3\Delta t}$$

**电容串联人工阻尼电阻**：

$$R_s \approx \frac{3\Delta t}{40C}$$

**π型等值导纳矩阵**：

$$Y_{\pi} = \begin{bmatrix} Y + \frac{Y_s}{2} & -Y \\ -Y & Y + \frac{Y_s}{2} \end{bmatrix}$$

## 关键技术挑战

### 1. 大规模网络求解的可扩展性

随着新能源渗透率提高，系统规模从数百节点扩展到数万节点。Abusalah 2018在Hydro-Québec L-Network（94706个设备，矩阵规模41797×41797）中验证了KLU+BTF方法，但最大子块13584×13584导致3线程后加速收益停滞。Xiong 2024在10,024节点系统中验证了BBD+MPI的强扩展性（15-18倍加速），但中等规模系统（240节点）的并行通信开销抵消了收益。可扩展性的核心瓶颈在于：(1) BTF/BFD分解后的子块均衡性；(2) 最大子块尺寸限制了并行上限；(3) 通信开销随进程数线性增长。

### 2. 频变特性的精确建模

输电线路和电缆的频变特性在宽频带EMT分析中不可忽略。Gustavsen 2012评估了230 kV/115 kV平行线路的模态域建模精度，指出频率相关土壤参数（如10000 Ω·m高电阻率土壤）对线路参数影响显著。Duarte 2023对50 m/100 m地下电缆的评估显示，在10 kHz以上频率，集总参数假设误差达10-20%，必须采用频变模型。频变建模的计算代价是：(1) 矢量拟合增加额外状态变量；(2) 历史项计算复杂度随频率点数增加；(3) 多端口频变等值的无源性保证。

### 3. 多时间尺度耦合的数值稳定性

混合仿真中，EMT子系统（μs级）与机电/相量子系统（ms级）的接口是数值稳定性的关键。Li 2019的SFP-EMT架构通过MD-TLM接口实现跨域同步，利用Hilbert变换、时间平均与线性插值技术实现相量与瞬时值的转换。接口模型引入的数值误差需控制在工程允许范围内（电压/电流波形最大偏差<1.0%）。Le-Huy 2023指出，离线仿真中为加速稳态而引入的数值技巧（如大阻尼系数、稳态近似初始化）在实时环境中会引发长期数值不稳定，需剔除这些技巧。

### 4. 网络等值的精度-效率权衡

FDNE等值在宽频EMT分析中不可或缺，但多端口FDNE的阶数选择和无源性保证是核心挑战。Noda 2007提出的二进制频率区域分割算法将频带划分为多个区域，每个区域独立拟合，降低单区域阶数要求。Gurrala 2015的Loewner矩阵方法避免了矢量拟合的迭代过程，直接构建频域插值模型。等值精度的评估指标包括：(1) 端口阻抗拟合误差；(2) 关键谐振频率偏移；(3) 暂态响应波形偏差。

### 5. 拓扑变化的实时处理

保护动作、开关操作导致网络拓扑突变，需要快速更新导纳矩阵或伴随电路参数。传统方法通过重新形成矩阵处理，计算代价高。Xu 2025提出的状态变量消去法（State Variables Elimination）在保持精度的同时减少矩阵维度，适用于含大量开关设备的微电网系统。拓扑变化的处理策略：(1) 预计算所有可能拓扑的伴随电路参数；(2) 在线查表插值；(3) 增量更新矩阵（仅修改受影响的行/列）。

## 量化性能边界

### 并行求解性能数据

| 测试系统 | 规模 | 方法 | 步长 | 加速比 | 数据来源 |
|---------|------|------|------|--------|---------|
| Hydro-Québec L-Network | 41797×41797矩阵, 94706设备 | KLU+BTF 12线程 | 50 μs | 1.49× | Abusalah 2018 |
| Hydro-Québec L'-Network | 217个BTF块, 最大2898×2898 | KLU+BTF 12线程 | 50 μs | 2.39× | Abusalah 2018 |
| Hydro-Québec R-Network | 3402×3402矩阵, 169个BTF块 | KLU+BTF 12线程 | 50 μs | 3.26× | Abusalah 2018 |
| T0-Network (详细模型) | 含DFIG IGBT, 28个BTF块 | KLU+BTF 12线程 | 10 μs | 1.90× | Abusalah 2018 |
| T0-Network (AVM, 50 μs) | 平均模型 | KLU+BTF 12线程 | 50 μs | 22.94× | Abusalah 2018 |
| WECC 240节点 (单核) | 240节点 | ParaEMT (Numba) | 50 μs | 3.1× (vs PSCAD) | Xiong 2024 |
| WECC 240节点 (8核) | 240节点 | ParaEMT BBD+MPI | 50 μs | 1.03× | Xiong 2024 |
| 合成10,024节点 | 10024节点 | ParaEMT BBD+MPI 84秩 | 50 μs | 15-18× | Xiong 2024 |

### 多速率联合仿真性能

| 场景 | SFP步长 | EMT步长 | 加速比 | 数据来源 |
|------|---------|---------|--------|---------|
| 大电网SFP子系统 | 500 μs | - | 10-250× | Li 2019 |
| 风电场EMT子系统 | - | 2-50 μs | - | Li 2019 |
| 宽频带交互分析 | 500 μs | 2-50 μs | 接口误差<1.0% | Li 2019 |

### 实时仿真规模

| 系统规模 | 组件数 | 平台 | 数据来源 |
|---------|--------|------|---------|
| 1666三相母线, 6180单相节点 | 13626 RLC, 432线路, 338变压器 | HYPERSIM | Le-Huy 2023 |
| 111台电机, 432条线路 | 86调速器, 81励磁, 54稳定器 | EMTP→HYPERSIM | Le-Huy 2023 |

## 适用边界与选择指南

### 网络建模粒度选择

| 应用场景 | 推荐建模粒度 | 原因 |
|---------|-------------|------|
| 操作过电压分析 | 分布参数线路 + 频变电缆 | 需精确捕捉传播延迟和反射 |
| 次/超同步振荡分析 | 频变线路 + SFP-EMT多速率 | 宽频带交互需保留电网电磁动态 |
| 大规模IBR系统仿真 | BBD+MPI并行 + 平均模型 | 万节点规模需分布式并行 |
| 保护动作仿真 | 母线-断路器模型 + 开关动态 | 需精确拓扑变化处理 |
| 实时HIL仿真 | 模型兼容层 + 数值阻尼校准 | 需保证实时确定性 |
| 规划阶段快速评估 | Ward等值 + 集总参数π型 | 计算效率优先 |

### 网络等值方法选择

| 等值需求 | 推荐方法 | 注意事项 |
|---------|---------|---------|
| 单端口简化 | 戴维南等值 | 适用于远离非线性负荷的节点 |
| 多端口宽频等值 | FDNE + 矢量拟合 | 需保证无源性，注意阶数选择 |
| 多区域互联系统 | REI等值 | 参数辨识复杂，需外部系统数据 |
| 机电暂态等值 | Ward等值 | 不保留频变特性，仅适用于低频 |
| 动态特性保留 | 动态等值 + Prony分析 | 工作点依赖性强，需定期更新 |

### 失效边界

- **参数频变忽略**：高频暂态（>10 kHz）下集总参数假设失效，误差可达10-20%（Duarte 2023）
- **等值过度简化**：关键谐振特性被等值滤除，影响IBR系统稳定性分析
- **拓扑快速变化**：大量开关动作导致频繁重构导纳矩阵，BTF撕裂需重新执行
- **多时间尺度耦合**：机电暂态与电磁暂态交互强烈区域，SFP-EMT接口可能数值不稳定
- **BTF子块不均**：最大子块尺寸决定并行上限，3线程后加速收益停滞（Abusalah 2018）
- **中等规模并行无效**：240节点系统中BBD并行收益仅1.03倍，通信开销抵消收益（Xiong 2024）

## 相关方法

- [[methods/network-solution/nodal-analysis.md|nodal-analysis]] - 节点分析解法
- [[topics/modeling-methods/network-equivalent.md|network-equivalent]] - 网络等值理论
- [[models/equivalent/fdne-model.md|fdne-model]] - 频变网络等值
- [[models/transmission-line/transmission-line-model.md|transmission-line-model]] - 输电线路详细模型
- [[topics/simulation/emt-simulation.md|emt-simulation]] - 电磁暂态仿真
- [[topics/simulation/parallel-computing.md|parallel-computing]] - 并行计算
- [[topics/simulation/co-simulation.md|co-simulation]] - 混合仿真
- [[topics/modeling-methods/dynamic-phasor.md|dynamic-phasor]] - 动态相量法
- [[methods/network-solution/sparse-matrix-solver.md|sparse-matrix-solver]] - 稀疏矩阵求解
- [[topics/modeling-methods/frequency-dependent-modeling.md|frequency-dependent-modeling]] - 频率相关建模

## 来源论文

- **Abusalah 2018** - "CPU based parallel computation of electromagnetic transients for large power grids" (Electric Power Systems Research) — 提出KLU+BTF自动网络撕裂方法，在Hydro-Québec大规模电网中实现1.9-23倍加速，MANA系统方程 formulation
- **Xiong 2024** - "An open-source parallel EMT simulation framework" (Electric Power Systems Research) — ParaEMT开源框架，BBD+MPI分布式并行，Numba JIT加速，在10,024节点系统中实现15-18倍加速
- **Le-Huy 2023** - "Lessons learned in porting offline large-scale power system simulation to real-time" (Electric Power Systems Research) — 离线EMT到实时HYPERSIM的移植经验，1666母线系统，模型兼容层与数值阻尼校准
- **Li 2019** - "A Multi-rate Co-simulation of Combined Phasor-Domain and Time-Domain Models for Large-scale Wind Farms" (IEEE TEC) — SFP-EMT多速率联合仿真，500 μs大电网步长，MD-TLM接口，宽频带次/超同步振荡分析
- **Gustavsen 2012** - "Modal domain-based modeling of parallel transmission lines" — 230 kV/115 kV平行线路模态域建模，频率相关土壤参数影响
- **Duarte 2023** - "Assessment of the transmission line theory in the modeling of multiconductor underground cable systems" — 地下电缆频变模型评估，10 kHz以上频率集总参数误差10-20%
- **Noda 2007** - "A Binary Frequency-Region Partitioning Algorithm for the Identification of a Multiphase Network Equivalent" — 二进制频率区域分割算法，降低FDNE阶数要求
- **Mu 2014** - "A parallel multi-rate electromagnetic transient simulation algorithm based on network division" — 基于网络分区的多速率并行EMT算法，历史项在分区边界传递
- **Gao 2022** - "Phase-domain model of twelve-phase synchronous machine for EMTP-type simulation" — 相域同步电机模型，恒定等效导纳矩阵，数值稳定性

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
