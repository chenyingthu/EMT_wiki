---
title: "声明式建模 (Declarative Modeling)"
type: method
tags: [declarative-modeling, equation-based, modelica, acausal, component-modeling, dae, fmi, object-oriented]
created: "2026-05-04"
updated: "2026-05-13"
---

# 声明式建模 (Declarative Modeling)

## 定义

声明式建模（Declarative Modeling）是一种基于方程而非赋值语句的建模范式。在声明式建模中，用户通过声明物理系统的守恒方程（如基尔霍夫定律、能量守恒）和本构关系（如欧姆定律、电磁感应定律）来描述模型，由求解器自动处理方程排序、因果推断和数值求解。与传统的过程式（Imperative）建模（如 C、Fortran）不同，声明式建模关注**"是什么"（what）**而非**"如何做"（how）**。

在电力系统电磁暂态（EMT）仿真中，声明式建模将组件模型表达为**微分-代数方程组（DAE）**，模型与求解器完全解耦——同一组方程可以用不同的数值积分方法（梯形法则、后向 Euler、DASSL 等）求解，而无需修改模型代码。

**核心特征**：

| 特征 | 声明式建模 | 过程式建模 |
|------|-----------|-----------|
| 方程表述 | $v - v_1 + v_2 = 0$（无因果） | $v := v_1 - v_2$（固定因果） |
| 因果推断 | 求解器自动处理 | 建模者手动指定 |
| 模型复用 | 高（与求解器无关） | 低（耦合于求解方法） |
| 多领域耦合 | 原生支持 | 需手动接口 |
| 标准交换 | FMI/FMU | 无通用标准 |

**边界限定**：本页面聚焦于声明式建模在电力系统 EMT 仿真中的应用，以 Modelica 语言为核心，涵盖方程建模、模型交换（FMI）、无因果连接语义等关键技术。

## EMT 中的角色

EMT 仿真传统上依赖过程式语言（Fortran、C++）实现，如 EMTP®、PSCAD® 等商业软件。声明式建模在 EMT 中的角色体现在三个层面：

1. **模型开发效率**：在 Masoom & Mahseredjian (2024) 中，Modelica 异步电机模型的代码量比 EMTP 原生实现减少约 60%，且公式可读性显著提升——"模型er 的注意力集中在方程本身而非求解步骤"。

2. **多领域统一建模**：电力系统涉及电气、机械、热、控制等多物理场耦合。声明式语言（如 Modelica 的 Modelica.Sensors、Modelica.Mechanical 库）允许在同一框架内描述跨领域交互，无需手动编写接口代码。

3. **模型交换与互操作**：通过 FMI/FMU 标准（FMI 3.0），声明式模型可在不同仿真工具间交换，实现"一次建模、多处仿真"。

**核心挑战**：
- **性能差距**：纯 Modelica 仿真器在处理大规模 EMT 网络时，计算速度比专用 EMT 工具慢 10~100 倍（Masoom et al. 2022, EPSR）
- **DAE 索引问题**：无因果连接产生的代数环可能导致高索引 DAE，需要符号微分降阶
- **延迟算子性能**：Modelica 内置延迟算子（delay operator）在传输线模型中成为 CPU 瓶颈

## 核心机制

### 1. 无因果建模与连接语义

声明式语言的核心是**无因果（acausal）建模**。在 Modelica 中，电阻器的方程写作：

$$v_1 - v_2 = R \cdot i \tag{1}$$

而非过程式中的 $i = (v_1 - v_2) / R$。方程 (1) 没有预设输入输出方向——求解器在编译时通过符号分析确定因果方向。

**连接点（connector）定义**：

```modelica
connector Pin
  Voltage v "节点电压";
  flow Current i "流入电流";
end Pin;
```

当两个 Pin 连接器通过 `connect()` 语句连接时，求解器自动应用：

**KCL（基尔霍夫电流定律）**：
$$i_1 + i_2 = 0 \tag{2}$$

**KVL（基尔霍夫电压定律）**：
$$v_1 = v_2 \tag{3}$$

这种自动连接语义使得复杂网络的拓扑构建无需手动编写节点方程。

### 2. DAE 系统形成与索引降阶

声明式建模将所有组件方程组装为统一的 DAE 系统：

$$\begin{aligned} \dot{x} &= f(x, z, u, t) \\ 0 &= g(x, z, u, t) \\ y &= h(x, z, u, t) \end{aligned} \tag{4}$$

其中 $x$ 为微分状态变量（如电感电流、电容电压），$z$ 为代数状态变量（如节点电压、支路电流），$u$ 为输入。

**DAE 索引（Index）** 是声明式建模的关键概念：

- **索引 1**：代数变量可通过微分方程显式求解（如节点导纳矩阵法）
- **索引 2+**：需要对代数方程进一步微分才能求解（如含理想开关的电路）

Modelica 编译器（如 Dymola、OpenModelica、Dynaωo）在执行符号微分后进行索引降阶。Masoom et al. (2021, EPSR) 指出，Modelica 工具的 **DAE 模式编译**（DAE-mode compilation）可显著提升 EMT 仿真性能，因为它在编译时完成符号处理，而非运行时。

### 3. 模型交换标准：FMI/FMU

**FMI（Functional Mock-up Interface）** 是声明式建模互操作的核心标准，由 Modelica 协会与 DASSL 团队联合开发。FMI 定义了两种模式：

**模型交换（Model Exchange）**：
- 导出格式：FMU（Functional Mock-up Unit）
- 接口函数：`fmi2Initialize()`, `fmi2FunctionalStep()`, `fmi2GetState()`, `fmi2SetState()`
- 适用场景：同一求解器在不同工具间迁移模型

**共仿真（Co-Simulation）**：
- 每个 FMU 自带求解器
- 通过主算法（Master Algorithm）协调步长和同步
- 适用场景：不同求解器/不同时间尺度的联合仿真

FMI 2.0 支持共仿真模式，FMI 3.0 新增 C API 支持实时仿真和硬件在环。

### 4. Modelica 在 EMT 中的实现架构

Modelica 语言本身不执行仿真——它需要**仿真环境**将方程转换为可执行代码。在 EMT 仿真中，主要仿真环境包括：

**OpenModelica**（开源）：
- 基于 OMCompiler 进行符号处理和代码生成
- 支持 C 代码导出，可链接 LAPACK/KLU 求解器
- 在 Masoom et al. (2021) 中，OpenModelica 实现的 CP 和 WB 传输线模型与 EMTP 精度完全匹配

**Dymola**（商业）：
- 工业级 Modelica 编译器，优化程度高
- 支持 DAE 模式编译和实时仿真

**Dynaωo**（开源，RTE 开发）：
- 混合 C++/Modelica 架构，专为大规模电力系统仿真设计
- 在 Masoom et al. (2022, 2024) 中，Dynaωo 将 Modelica 模型编译为 C++ 代码，性能接近专用 EMT 工具
- 支持变步长求解器（DASSL、IDA/SUNDIALS）和固定步长求解器

**iPSL / OpenIPSL / PowerGrids**：
- 面向相量域（phasor-domain）的 Modelica 电力系统库
- 主要用于暂态稳定分析，非 EMT 级仿真

### 5. 传输线建模中的声明式方法

Masoom et al. (2021, EPSR) 在 Modelica 中实现了两种 EMT 传输线模型：

**常参数（CP）线模型**：

集总参数等效电路如图 1 所示，时域方程为：

$$i(t) = Y \cdot v(t) + J(t - \tau) \tag{5}$$

其中 $Y$ 为导纳矩阵，$\tau = \ell / v$ 为传播延迟（$\ell$ 为线长，$v$ 为波速），$J$ 为历史电流源。

**宽频（WB）线模型**：

考虑频率依赖特性，采用频变参数：

$$Z_{mdf} = T_v Z_{c,mod} T_v^{-1} + \frac{R_{mod}}{4} \tag{6}$$

其中 $T_v$ 为模态变换矩阵，$Z_{c,mod}$ 为模域特性阻抗，$R_{mod}$ 为模域电阻。

Masoom et al. (2022, EPSR) 提出**空间数据局部性优化**：将传输线模型聚类为线块模型（line block model），改善缓存命中率。通过延迟算子计算外包给向量化 C 代码，IEEE 39-bus 基准测试的仿真时间减少约 40%。

### 6. 组件模型建模示例

**异步电机（Masoom & Mahseredjian, 2024）**：

在 dq 参考系中，异步电机的方程为：

$$\begin{aligned} v_d &= R_s i_d + \frac{d\lambda_d}{dt} - \omega_s \lambda_q \\ v_q &= R_s i_q + \frac{d\lambda_q}{dt} + \omega_s \lambda_d \\ 0 &= R_r i_{rd} + \frac{d\lambda_{rd}}{dt} - (\omega_s - \omega_r)\lambda_{rq} \\ 0 &= R_r i_{rq} + \frac{d\lambda_{rq}}{dt} + (\omega_s - \omega_r)\lambda_{rd} \end{aligned} \tag{7}$$

磁链方程：

$$\begin{aligned} \lambda_d &= L_s i_d + L_m i_{rd} \\ \lambda_q &= L_s i_q + L_m i_{rq} \\ \lambda_{rd} &= L_m i_d + L_r i_{rd} \\ \lambda_{rq} &= L_m i_q + L_r i_{rq} \end{aligned} \tag{8}$$

Modelica 实现中，这些方程直接以声明式方式写入组件类，无需指定求解顺序。与 EMTP 的 Norton 等效电路方法相比，Modelica 方法的优势在于：(1) 支持变步长求解器，在电机启动暂态中可自动增大步长；(2) 双笼和绕线转子模型通过同一方程框架实现，仅需修改参数。

**MSEMT 库组件体系（Masoom et al., 2022, TPWRD）**：

MSEMT（Modelica Simulator of Electromagnetic Transients）库包含 30+ 种 EMT 组件模型：

| 组件类别 | 模型数量 | 典型模型 |
|---------|---------|---------|
| 输电线路 | 6 | CP线、WB线、多相电缆、折叠线 |
| 旋转电机 | 8 | 同步机（含磁饱和）、异步机（单/双笼）、直流机 |
| 变压器 | 4 | 三绕组变压器、接地变压器、PT/CT |
| 电力电子 | 6 | VSC、LCC、STATCOM、SVG |
| 保护设备 | 4 | 避雷器、断路器、限流电抗器 |
| 负载 | 3 | 恒阻抗、恒功率、感应电机负载 |

## 形式化表达

### 声明式 vs 过程式方程对比

**电阻器方程**：

声明式（无因果）：
$$v_a - v_b - R \cdot i = 0 \tag{9}$$

过程式（因果，电流为输出）：
$$i = \frac{v_a - v_b}{R} \tag{10}$$

**传输线延迟方程**：

$$J(t) = Y_0 \cdot [2v(t - \tau) - v_{hist}(t)] \tag{11}$$

其中 $Y_0$ 为特性导纳，$v_{hist}$ 为历史电压项。

### DAE 系统整体形式

完整的 EMT 网络 DAE 系统：

$$\begin{bmatrix} \dot{x} \\ 0 \end{bmatrix} = \begin{bmatrix} f_x(x, z, u, t) \\ g_z(x, z, u, t) \end{bmatrix} \tag{12}$$

经过索引降阶和符号处理后，转化为显式 ODE 形式：

$$\dot{x} = F(x, t) \tag{13}$$

再由数值积分方法（梯形法则、后向 Euler、Gear 法等）离散化：

$$x_{n+1} = x_n + h \cdot \Phi(x_n, x_{n+1}, h) \tag{14}$$

### 伴随电路（Companion Circuit）转换

声明式 DAE 经数值积分后，每个储能元件转换为 Norton/Thevenin 伴随电路：

**电感（梯形法则）**：
$$i_L(t_n) = \frac{h}{2L} v_L(t_n) + i_{hist} \tag{15}$$

**电容（梯形法则）**：
$$i_C(t_n) = \frac{2C}{h} v_C(t_n) + i_{hist} \tag{16}$$

其中 $i_{hist}$ 为历史电流源，依赖于之前时刻的电压/电流值。

## 关键技术挑战

### 1. 计算性能差距

纯 Modelica 仿真器在 EMT 规模问题上的性能瓶颈：

- **Masoom et al. (2022, EPSR)**：IEEE 39-bus 系统，纯 Modelica（OpenModelica）仿真时间比 EMTP 慢约 50 倍
- **Masoom et al. (2022, TPWRD)**：采用 Dynaωo 混合 C++/Modelica 架构后，性能提升至 EMTP 的 3~5 倍差距
- **空间数据局部性优化**（Masoom et al. 2022, EPSR）：传输线模型缓存优化使仿真时间减少约 40%

**瓶颈来源**：
- Modelica 内置延迟算子（delay operator）的 CPU 开销最大
- 运行时符号解释开销（DAE 模式编译可缓解）
- 内存访问模式不佳（缓存未命中率高）

### 2. DAE 索引与代数环

无因果连接产生的代数环是声明式建模的固有挑战：

- **索引 1 DAE**：标准 EMT 网络（含伴随电路）自然形成索引 1
- **索引 2+ DAE**：含理想开关、理想变压器环路的电路需要符号微分降阶
- **代数环检测**：OpenModelica 在编译时检测代数环并尝试撕裂（tearing）

### 3. 变步长求解器的 EMT 适用性

EMT 仿真传统上使用固定小步长（1~10 μs）：

- **变步长优势**：Masoom & Mahseredjian (2024) 表明，在电机启动等事件间期较长的仿真中，变步长求解器（DASSL、IDA）可将步长从 10 μs 自动增大至 1 ms，显著提升效率
- **精度风险**：大步长可能丢失高频振荡细节，需结合自适应步长控制

### 4. 多领域耦合的数值稳定性

声明式建模允许直接耦合电气-机械-热模型，但不同物理尺度的耦合可能引入数值 stiffness：

- 电气时间尺度：纳秒~毫秒
- 机械时间尺度：秒~分钟
- 热时间尺度：分钟~小时

使用隐式求解器（后向 Euler、BDF）可缓解 stiffness 问题，但可能引入数值阻尼。

## 量化性能边界

| 指标 | 数值 | 来源 | 条件 |
|------|------|------|------|
| 代码量减少 | ~60% | Masoom & Mahseredjian 2024 | 异步电机模型 vs EMTP |
| 纯 Modelica 性能差距 | 50× | Masoom et al. 2021, EPSR | IEEE 39-bus CP线模型 |
| Dynaωo 性能差距 | 3~5× | Masoom et al. 2022, TPWRD | MSEMT库 IEEE 39-bus |
| 缓存优化加速 | ~40% | Masoom et al. 2022, EPSR | IEEE 39-bus 传输线 |
| 精度 | 与 EMTP 完全匹配 | Masoom et al. 2021, EPSR | CP/WB线模型电压/电流 |
| 变步长加速 | 10~100× | Masoom & Mahseredjian 2024 | 电机启动暂态（步长10μs→1ms） |
| 支持节点规模 | 10~1000 | Masoom et al. 2022, TPWRD | MSEMT库实际测试 |

## 适用边界与选择指南

### 适用场景

| 场景 | 推荐度 | 说明 |
|------|--------|------|
| 组件模型开发/研究 | ★★★★★ | 高抽象层，公式可读性强，修改方便 |
| 多领域耦合仿真 | ★★★★★ | 电气-机械-热-控制统一建模 |
| 模型交换/互操作 | ★★★★★ | FMI/FMU 标准支持跨工具复用 |
| 小规模 EMT 仿真（<100 节点） | ★★★★☆ | Dynaωo 可达到实用性能 |
| 相量域暂态稳定 | ★★★★☆ | iPSL/OpenIPSL 库成熟 |
| 大规模 EMT 仿真（>1000 节点） | ★★☆☆☆ | 性能差距仍显著，需混合架构 |
| 实时仿真/硬件在环 | ★★★☆☆ | FMI 3.0 C API 支持，但需代码优化 |

### 不适用场景

- **超大规模网络实时仿真**：纯 Modelica 环境无法满足 μs 级实时约束
- **需要极致性能的生产仿真**：专用 EMT 工具（EMTP®、PSCAD®）在大规模场景下仍有优势
- **封闭公司标准流程**：部分电网公司已有成熟的 Fortran/C++ 模型库，迁移成本高

## 相关方法

- [[emt-simulation]] - EMT 仿真基础
- [[dae-solvers]] - DAE 求解器
- [[numerical-integration]] - 数值积分方法
- [[companion-circuit]] - 伴随电路模型
- [[nodal-analysis]] - 节点分析法
- [[state-space-method]] - 状态空间法
- [[variable-time-step-solver]] - 变步长求解器
- [[backward-euler]] - 后向 Euler 法
- [[trapezoidal-rule]] - 梯形法则
- [[power-electronics]] - 电力电子
- [[control-system]] - 控制系统
- [[real-time-simulation]] - 实时仿真
- [[transient-stability]] - 暂态稳定分析

## 来源论文

- **Masoom et al. 2022, IEEE TPWRD** - "MSEMT: An Advanced Modelica Library for Power System EMT Studies" — 提出 MSEMT 库，30+ 组件模型，与 EMTP 精度对比验证
- **Masoom et al. 2022, Electric Power Systems Research** - "Acceleration of EMT simulations in Modelica using spatial data locality" — 传输线模型缓存优化，IEEE 39-bus 性能提升 40%
- **Masoom et al. 2022** - "Modelica-based simulation of EMT using Dynaωo: Current status and perspectives" — Dynaωo 混合 C++/Modelica 架构，性能差距缩小至 3~5 倍
- **Masoom & Mahseredjian 2024, IEEE ACCESS** - "EMT Modeling of Asynchronous Machine in Modelica" — 异步电机 dq 参考系建模，变步长求解器性能评估
- **Masoom et al. 2021, EPSR** - "Simulation of EMT with Modelica, accuracy and performance assessment for transmission line models" — CP/WB 线模型 Modelica 实现，与 EMTP 精度完全匹配
- **Fritzson 2014, Wiley** - "Principles of Object-Oriented Modeling and Simulation with Modelica 3.3" — Modelica 语言标准参考，方程建模、DAE 理论、FMI 标准
- **Wang et al.** - "Extended Habedank's Equation-Based EMTP Model of Pantograph Arcing" — 方程基 EMTP 模型在电弧仿真中的应用

---

*本页面遵循学术严谨性原则，所有技术细节和数据均基于同行评议的学术文献。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st|MSEMT: An Advanced Modelica Library for Power System Electro]] | 2022 |
| [[electromagnetic-transient-modeling-of-asynchronous-machine-in-modelica-accuracy--16|Electromagnetic Transient Modeling of Asynchronous Machine i]] | 2024 |
| [[electromagnetic-transient-modeling-of-asynchronous-machine-in-modelica-accuracy-|Electromagnetic Transient Modeling of Asynchronous Machine i]] | 2024 |
