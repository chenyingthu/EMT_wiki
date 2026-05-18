---
title: "实时仿真"
type: topic
tags: [real-time, hardware-in-the-loop, fpga, rtds, parallel-computing, fixed-admittance, hil, hardware-emulation]
created: "2026-04-13"
updated: "2026-05-19"
---

# 实时仿真

## 定义与边界

实时仿真要求每个仿真步在真实时间截止期限内完成，并能与控制器、保护装置或硬件在环系统交换信号。与普通离线 EMT 相比，它首先受固定步长、确定性调度、I/O 延迟和硬件资源约束。

从物理过程上，实时 EMT 仿真是将连续的微分-代数方程组在固定步长 $\Delta t_{\mathrm{real}}$ 内完成求解，并将计算结果通过硬件接口输出到外部物理设备。从计算架构上，它需要 CPU/FPGA/GPU 等硬件资源在时序约束下协同工作。

从 EMT 建模角度，实时仿真涉及**五个核心技术挑战**：① 固定步长约束下的网络求解加速；② 非线性元件（开关、饱和磁路、避雷器）的迭代收敛；③ 外部控制器/保护装置的实时接口；④ 多速率系统的时间解耦；⑤ 硬件资源约束下的模型简化。任何一个挑战未解决都会导致 deadline miss。

本页面讨论实时 EMT 仿真，不涉及纯机电暂态的实时 RMS 仿真（见 [[electromechanical-electromagnetic-hybrid-simulation]]），也不讨论超快速的离线故障扫描（属于"超实时仿真"概念，在适用边界章节中说明）。

## 在 EMT 中的角色

实时仿真把 EMT 从离线分析工具转变为**工程验证平台**，用于以下四类工程目标：

1. **控制保护闭环测试**：将被测控制器或保护装置（Relay）接入实时仿真回路，验证其在真实时间尺度下的响应行为
2. **HIL 硬件在环验证**：将实际功率放大器+被测设备接入仿真回路，验证从控制器到功率级的完整闭环
3. **换流器/设备调试**：在实验室环境下对 HVDC/MMC/IBR 设备进行出厂测试，无需实际电网
4. **实时数字孪生**：将实际运行电网的实时状态镜像到仿真器，实现态势感知和预测控制

实时 EMT 仿真的核心价值在于保留：μs 级步长的开关暂态细节、多速率系统中快速动态与慢速动态的耦合交互、非线性元件的动作时序、外部控制器与仿真器之间的接口延迟。常见仿真输出：端口电压 $v(t)$、开关状态、控制器输出信号、接口延迟 $\delta t$、最坏情况执行时间 $T_{\mathrm{worst}}$。

## 核心约束

实时 EMT 的基本约束是每个步长内计算与 I/O 必须完成：

$$T_{\mathrm{solve}}+T_{\mathrm{io}}+T_{\mathrm{sync}} \le \Delta t_{\mathrm{real}}$$

其中 $\Delta t_{\mathrm{real}}$ 是实时步长（通常 $1\sim 50\ \mu\text{s}$），$T_{\mathrm{solve}}$ 是网络和设备模型求解时间，$T_{\mathrm{io}}$ 是硬件接口延迟（数模转换 DA、模数转换 AD、信号调理），$T_{\mathrm{sync}}$ 是多核、多机或协同仿真的同步开销。

若将 $T_{\mathrm{solve}}$ 展开为网络方程求解时间 $T_{\mathrm{net}}$ 和设备模型更新时间 $T_{\mathrm{dev}}$ 之和，则：

$$T_{\mathrm{net}} = O\left(\Delta t \cdot N_{\mathrm{iter}} \cdot f_{\mathrm{solve}}(N)\right), \quad T_{\mathrm{dev}} = O\left(\Delta t \cdot N_{\mathrm{switch}}\right)$$

其中 $N$ 为网络节点数，$N_{\mathrm{iter}}$ 为非线性迭代次数，$N_{\mathrm{switch}}$ 为开关数量。实时约束决定了在给定 $\Delta t_{\mathrm{real}}$ 下，$N$ 和 $N_{\mathrm{switch}}$ 的上限。

## EMT 建模方法

### 恒导纳模型（Fixed Admittance）

**恒导纳模型**（Fixed Admittance Model, FAD）又称**伴随离散电路**（Associated Discrete Circuit, ADC），是实时 EMT 中避免开关动作触发矩阵重分解的核心加速技术。其数学本质是将开关状态变化的影响从节点导纳矩阵 $\mathbf{Y}_n$ 转移到诺顿历史电流源 $I_{\mathrm{hist}}$，使得 $\mathbf{Y}_n$ 在整个仿真过程中恒定不变：

$$\mathbf{Y}_{\mathrm{fix}}\mathbf{v} = I_{\mathrm{hist}}(s_k, x_{k-1}, u_k)$$

其中 $s_k$ 为当前开关状态，$x_{k-1}$ 为上一时刻状态变量，$u_k$ 为当前输入。开关切换时只有 $I_{\mathrm{hist}}$ 更新，矩阵 $\mathbf{Y}_{\mathrm{fix}}$ 保持不变，每步只需前代回代 $O(nnz)$ 而非 LU 分解 $O(N^3)$。这使得含大量开关的电力电子系统（如 MMC、子模块级联结构）在 FPGA 上实现微秒级实时仿真成为可能。

固定导纳模型的关键参数选择见 [[fixed-admittance]]。

### 状态空间等效模型

对于换流器内部动态（如 MMC 子模块电容电压、DAB 移相控制），可将详细开关模型替换为**状态空间等效模型**（State-Space Equivalent Model），在保证端口电气特性一致的前提下将开关数量的复杂度解耦：

$$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}, \quad \mathbf{y} = \mathbf{C}\mathbf{x} + \mathbf{D}\mathbf{u}$$

状态空间模型的优势是：不依赖开关动作，可使用较大的等效时间步长（如 $10\ \mu\text{s}$ 而非 $1\ \mu\text{s}$），同时在端口处仍保持与详细模型一致的电气特性。详细建模方法见 [[state-space-method]] 和 [[network-partitioning]]。

### 并行网络解耦（Compensation Method）

当系统规模超出单核或单片 FPGA 的实时求解能力时，需要将网络分割为多个子系统并行求解。**补偿法**（Compensation Method）通过在子系统的边界节点注入补偿电流，将原本相互依赖的网络方程解耦为独立子问题：

$$I_{\mathrm{comp}}^{(k)} = \mathbf{Y}_{\mathrm{bus}}^{(k)}\mathbf{V}_{\mathrm{boundary}}^{(k)}$$

其中 $\mathbf{Y}_{\mathrm{bus}}^{(k)}$ 为第 $k$ 个子系统的边界导纳矩阵，$\mathbf{V}_{\mathrm{boundary}}^{(k)}$ 为边界电压向量。补偿法不依赖传输线延迟（这是传统并行 EMT 依赖的自然解耦机制），因此适用于无延迟或延迟不足的网络结构。Bruned 等在 2021 年的论文给出了配电网和 HVDC 网络的详细实现流程，并在 HYPERSIM 上验证了实时性能。

### 延迟解耦与延迟插入法

**延迟插入法**（Latency Insertion Method, LIM）利用人为引入的延迟支路将分布式网络解耦为局部子网络，实现并行计算。对于含有大量分布参数线路的微电网系统：

$$V_i^{n+1} = V_i^n + \frac{\Delta t}{C_i}\left(\frac{V_{i-1}^n - V_i^n}{Z_{c,i}} - I_{\mathrm{branch},i}^n\right)$$

Xu 等（2020）利用固定导纳模型结合延迟插入法，在 FPGA 上实现了亚微秒级（$<1\ \mu\text{s}$）实时仿真，将分布式电源的网络解耦与并行计算统一在 FPGA 流水线架构中。

### 多速率建模

多速率方法将系统按时间尺度分离：控制/机电动态使用大步长（如 $50\ \mu\text{s}$），电磁暂态使用小步长（如 $1\ \mu\text{s}$），两者通过接口滤波器交换数据。典型接口方式为功率接口（Power Interface）或电压接口（Voltage Interface），其核心是保证接口两侧的功率平衡和电压连续性：

$$\mathbf{P}_{\mathrm{EMT}} = \mathbf{P}_{\mathrm{TS}}, \quad \mathbf{V}_{\mathrm{EMT}} = \mathbf{V}_{\mathrm{TS}}$$

多速率方法与网络分区联合使用是目前大规模实时仿真的主流架构。

### HIL 接口模型

硬件在环仿真（HIL）将真实控制器通过 I/O 接口接入仿真器，其实时性要求体现在接口延迟必须小于仿真步长：

$$T_{\mathrm{calc}} + T_{\mathrm{interface}} < T_{\mathrm{step}}$$

其中接口模型的核心是保证仿真器端口电压/电流与真实设备端口一致。EMT 中的 HIL 接口通常采用诺顿等效或戴维南等效，将外部设备映射为等效电流源或电压源与阻抗的串联：

$$V_{\mathrm{device}} = V_{\mathrm{simulation}} + Z_{\mathrm{interface}} \cdot I_{\mathrm{device}}$$

稳定性条件为 $|Z_{\mathrm{simulation}} \cdot Y_{\mathrm{interface}}| < 1$，需要通过阻抗匹配保证闭环稳定性。

## 关键技术挑战

### 挑战一：非线性迭代的实时收敛

非线性元件（变压器饱和、避雷器非线性电阻、电晕对地电导）在每次开关动作或状态跳变后需要迭代求解。牛顿-拉夫逊法在实时约束下可能无法在单步内收敛到指定容差，导致求解器发散或超时。Chen 和 Dinavahi（2011）的 FPGA 迭代求解器通过稀疏技术、深度流水线浮点运算和并行高斯-约当消元法，在 5 μs 步长下实现了串联补偿线路避雷器暂态的稳定实时仿真。

### 挑战二：矩阵求解的算力瓶颈

大规模电网（如 10000+ 节点）的节点导纳矩阵 LU 分解每步耗时可达数百微秒，远超实时步长约束。解决路径包括：① 稀疏求解技术（减少填充）；② 迭代求解器（如共轭梯度法）替代直接法；③ 网络分区将大矩阵分解为多个小矩阵并行求解；④ 硬件加速（FPGA 流水线、GPU 并行）。Shukla 等（2022）在 FPGA 上实现共轭梯度求解器，避免了预存时变元件逆矩阵的瓶颈。

### 挑战三：I/O 延迟与接口稳定性

数模/模数转换延迟（通常 1-10 μs）、信号调理延迟和通信协议延迟叠加后，可能超过仿真步长的 20%，导致控制器感受到的"实时"电压与实际仿真电压之间存在相位移。UDP/TCP 以太网接口延迟约为 100-500 μs，仅适用于 RMS-EMT 协同仿真；FPGA Aurora 光纤接口可低至 1 μs，适用于高精度 EMT-HIL。

### 挑战四：开关动作的精确捕捉

对于开关频率 20 kHz 的电力电子系统（周期 50 μs），若步长取 50 μs 则一个周期内只有一步，完全无法捕捉开关暂态。实际要求步长 $< 0.5\ \mu\text{s}$ 才能在每个开关周期内采样 100 个点。EMT 中的处理方法包括：① 固定小步长（如 $0.5\ \mu\text{s}$）；② 开关事件检测+自动步长调整；③ 插值方法（如线性插值、二次插值）在事件前后加密采样。

### 挑战五：FPGA 资源约束

单片 FPGA 的 DSP 和 BRAM 资源限制了可实现的矩阵规模和并行度。典型 Virtex-7 的 DSP 数量约为 3000-8000 个，一次矩阵乘法需要约 $N^2$ 个 DSP，其中 $N$ 为矩阵维度。解决方案：① 降阶等效（FDNE 将外部网络降为 10-20 阶导纳模型）；② 混合精度（16 位浮点用于非关键路径，32 位浮点用于关键路径）；③ 流水线重排（Amdahl 定律优化串行部分）。

## 量化性能边界

以下量化数据均来自来源论文的 EMT 实时仿真测试结果：

| 平台 | 应用场景 | 步长 | 规模 | 性能指标 | 来源 |
|------|---------|------|------|---------|------|
| FPGA（单片） | 输电线路直击雷 | 12 μs（时钟周期 12.5 ns） | 15 条频变线路 | 12 μs/步，实时示波器波形与 ATP 一致 | Chen 2009 |
| FPGA（单片） | 串联补偿避雷器暂态 | 5 μs | 非线性网络 | 并行 NR+补偿法，FPGA 波形与 ATP 一致 | Chen 2011 |
| FPGA（单片） | 交流电机（PMSM/感应电机）| 44 ns/步 | 单机驱动 | 44 ns 单步，精度与 JMAG FEA 对比 | Matar 2011 |
| FPGA（可重构）| 大规模电力系统 | 24 ns | 实际规模 | 当时文献最低单步计算时间 | Rosolowski 2012 |
| FPGA | 微电网 | 0.5 μs（亚微秒级）| 含 DG 微电网 | 固定导纳+LIM，网络解耦并行 | Xu 2020 |
| FPGA | 并网变换器 | 1 μs | FDNE 等值 | 混合精度浮点，精度与全详细模型偏差 < 2% | Hajizadeh 2026 |
| FPGA | DFIG 风电场 | 10 μs（等效）| 大规模风电场 | 延迟解耦+M-NFSS，节点减少 60%，精度与详细模型一致 | Liu 2025 |
| MPSoC | CDSM MMC 电热仿真 | 1 μs | 故障容错 MMC | 等效电路+器件级电热模型联合架构 | Li 2019 |
| CPU-FPGA | 虚拟同步并网逆变器 | 1 μs | 单逆变器 | 恒导纳+支路并行拆分，FPGA 端无迭代 | 沈等 2023 |
| RTDS+FPGA | 大规模 HVDC | 50 μs/EMT 侧 | 3 端直流电网 | 实时 HIL，集成 12 个 DCCB 控制器 | rtds-fpga 2020 |
| CPU 集群 | 大规模电力系统 | 20 μs | 阿尔伯塔省网 | 双层网络等值，20 μs 步长实时仿真 | Mcley 2007 |
| GPU | 海上风电场 | 超实时（>百倍加速）| 大规模风电场 | 移频分析+延迟线性多步法 | Zhang 2024 |
| HYPERSIM | 配电网/HVDC | 实时 | 多种规模 | 稀疏求解器 MKLU，替代代码生成求解器 | sparse-solver 2023 |

**步长与精度的对应关系**（经验数据）：

| 仿真目标 | 推荐步长 | 精度要求 | 说明 |
|---------|---------|---------|------|
| 开关动作捕捉 | $< 0.5\ \mu\text{s}$ | 波形上升沿误差 < 1% | 20 kHz 开关频率要求 |
| 基波相量提取 | $> 10\ \mu\text{s}$ | 相位误差 < 0.1° | 用于保护 HIL |
| 设备级稳态响应 | $1\sim 10\ \mu\text{s}$ | 波形形态一致 | MMC、电机的工频周期响应 |
| 系统级机电动态 | $> 50\ \mu\text{s}$ | 频率偏差 < 0.1 Hz | 与 TS 混合仿真接口 |

## 适用边界与选择指南

| 建模任务 | 推荐方法 | 适用场景 | 不适用场景 |
|---------|---------|---------|-----------|
| 电力电子开关精确捕捉 | 固定导纳 + 插值 | MMC/DAB/光伏逆变器，20 kHz+ 开关频率 | 低开关频率线路（可用大步长）|
| 大规模电网（10000+ 节点）| 补偿法 + 网络分区 | 多 FPGA/多核并行，需实时 HIL | 单 FPGA 资源不足 |
| 非线性元件（饱和/避雷器）| 迭代补偿法（NR+补偿）| 变压器铁磁谐振、避雷器能量校核 | 实时约束极严（应考虑固定导纳近似）|
| 微电网（分布式电源）| 延迟插入法 + 固定导纳 | 亚微秒级步长，FPGA 单片实现 | 分布式线路过长（延迟不足）|
| EMT-TS 混合实时 | 多速率 + 功率接口 | 含新能源/IBR 的大电网混合仿真 | 两端时间尺度差异过大（>100:1）|
| 控制器 HIL 测试 | 诺顿等效接口 + 阻抗匹配 | 保护继电器 HIL、控制闭环测试 | 需要开关级精度（应选详细模型 HIL）|
| 超实时仿真（故障扫描）| 移频分析 + GPU 并行 | 百倍加速，故障场景批量评估 | 需要波形细节（超实时无实时约束）|

### 实时 vs 超实时

| 特性 | 实时仿真 | 超实时仿真 |
|------|---------|-----------|
| 约束 | $T_{\mathrm{solve}} \le \Delta t_{\mathrm{real}}$ | $T_{\mathrm{solve}} < \Delta t_{\mathrm{real}}$（可快于真实时间）|
| 目标 | HIL 测试、保护控制闭环 | 故障扫描、控制策略预演、数字孪生 |
| 验证要求 | 波形精度 + deadline 可满足性 | 波形精度（无实时 HIL 接口）|
| 典型平台 | RTDS、FPGA、MPSoC | GPU、CPU 集群、移频分析 |
| 时间步长 | 固定（1-50 μs）| 可变（通常更大步长）|

### 平台选择决策树

```
系统规模？
├─ 小规模（< 100 节点）
│   └─ 实时性要求？
│       ├─ μs 级步长 → 单片 FPGA + 固定导纳
│       └─ 100 μs 级步长 → 多核 CPU + 稀疏求解
├─ 中规模（100-1000 节点）
│   └─ 实时 HIL？
│       ├─ 是 → CPU-FPGA 协同 + 网络分区
│       └─ 否 → GPU 超实时 或 CPU 集群
└─ 大规模（> 1000 节点）
    └─ 实时 HIL？
        ├─ 是 → 多 FPGA + 补偿法并行 + RTDS 协同
        └─ 否 → 降阶等值（FDNE）+ GPU 超实时
```

## 相关方法

- [[fixed-admittance]] — 恒导纳模型：避免矩阵重分解的实时优化
- [[state-space-method]] — 状态空间法：快速状态空间求解，支持降阶建模
- [[nodal-analysis]] — 节点分析：实时 EMT 的网络方程装配线
- [[network-partitioning]] — 网络分区：并行实时仿真的分割策略
- [[multirate-method]] — 多速率方法：实时多速率调度
- [[parallel-computing]] — 并行计算：多核/FPGA 实时并行架构

## 相关模型

- [[mmc-model]] — MMC 模型：MMC 实时等效建模（固定导纳、状态空间等效）
- [[vsc-model]] — VSC 模型：换流器实时仿真
- [[fdne-model]] — 频变网络等值（FDNE）：外部系统实时等值降阶
- [[transmission-line-model]] — 输电线路模型：行波模型实时实现

## 相关主题

- [[co-simulation]] — 混合仿真：实时协同仿真（EMT-TS、EMT-RMS）
- [[electromechanical-electromagnetic-hybrid-simulation]] — 机电-电磁混合仿真：实时混合仿真的基础
- [[hil-simulation]] — 硬件在环仿真：HIL 实时测试框架
- [[frequency-dependent-modeling]] — 频率相关建模：频变模型实时实现
- [[compensation-method]] — 补偿法：并行实时仿真的网络解耦方法

## 来源论文

- Chen and Dinavahi 2009 — FPGA 流水线实时 EMTP，首个单片 FPGA 电磁暂态实时仿真器，12.5 ns 时钟周期
- Chen and Dinavahi 2011 — FPGA 迭代实时非线性 EMT 求解器，补偿法 + 牛顿-拉夫逊，5 μs 步长
- Matar and Iravani 2011 — FPGA 并行交流电机实时仿真，44 ns/步，无需预测-校正迭代
- Rosolowski 2012 — 可重构硬件实时仿真器，24 ns 单步计算（当时文献最低）
- McLey 2007 — 双层网络等值实时 EMT，20 μs 步长，阿尔伯塔省网实时验证
- Bruned et al. 2021 — 补偿法并行实时 EMT，HYPERSIM 验证，配电网/HVDC 测试
- Xu et al. 2020 — FPGA 亚微秒级实时仿真，固定导纳 + 延迟插入法，微电网验证
- Shukla et al. 2022 — FPGA 共轭梯度求解器，配电网 EMT 分析
- Liu et al. 2025 — DFIG 风电场延迟解耦实时仿真，节点减少 60%，精度与详细模型一致
- Li et al. 2019 — MPSoC 电热暂态实时仿真，CDSM MMC 故障容错验证
- Hajizadeh et al. 2026 — FPGA 并网变换器 FDNE 实时仿真，1 μs 步长
- Zhang et al. 2024 — GPU 移频超实时仿真，百倍加速，海上风电场验证
- Le-Huy et al. 2023 — 离线到实时移植经验教训，HIL 测试流程
- Scheibe et al. 2022 — RTDS-离线仿真 UDP/FPGA 接口架构