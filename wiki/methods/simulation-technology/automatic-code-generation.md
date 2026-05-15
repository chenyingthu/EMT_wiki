---
title: "自动代码生成 (Automatic Code Generation)"
type: method
tags: [code-generation, real-time, fpga, automatic, model-based-design, hdl, c-code, gpu, hardware-synthesis]
created: "2026-05-02"
updated: "2026-05-16"
---

# 自动代码生成 (Automatic Code Generation)

## 定义

自动代码生成（Automatic Code Generation）是把电力系统模型、网表、控制框图或中间表示转换为可部署目标代码的过程。目标代码形式包括 C/C++ 嵌入式任务、硬件描述语言（VHDL/Verilog）模块、FPGA 位流、用户代码模型或仿真器内部任务图。

从数学上，代码生成可抽象为

$$P_{\mathrm{target}} = \mathcal{G}(M, C, \theta)$$

其中 $M$ 为源模型，$C$ 为目标平台约束（步长、数据类型、内存布局、I/O 时序），$\theta$ 为生成参数（任务划分粒度、流水线级数、接口协议），$\mathcal{G}$ 为代码生成器。生成结果 $P_{\mathrm{target}}$ 必须在目标平台上通过**仿真在环**（Simulation-in-the-Loop, SIL）或**硬件在环**（Hardware-in-the-Loop, HIL）验证才能声称与源模型语义等价。

## EMT 中的角色

自动代码生成在 EMT 仿真中承担四条核心任务：

1. **离线到实时移植**：从 EMTP/PSCAD 离线模型生成 HYPERSIM/RTDS 实时任务或 FPGA 实时求解器，减少手工重建工作（Le-Huy & Tremblay 2023）。
2. **FPGA 实时 EMT 求解器生成**：从网表提取拓扑、矩阵结构和元件参数，自动生成可在 FPGA 上运行的时域求解 HDL 代码（MTOF 2025；Zhang 等 - 2024）。
3. **GPU 并行 kernel 生成**：将电气-控制耦合系统重写为线程同构的计算图，自动生成 CUDA kernel 以实现细粒度并行（Song 等 2018）。
4. **用户代码模型与接口封装**：为无直接等价物的电气元件或控制模块生成可调用模块，处理 API 生命周期和状态保存（Le-Huy 2023）。

对 EMT 仿真，代码生成的核心挑战不是语法翻译，而是**离散时间语义保持**（事件处理顺序、数值格式一致性、接口延迟可追踪）。生成代码必须逐项与源模型在相同工况下进行对比验证。

## 核心机制

### 生成链条的六阶段模型

典型代码生成链条包括六个阶段：

1. **解析与提取**：从源模型（网表、MATLAB/Simulink、Modelica 或图形化建模环境）提取电气拓扑、元件参数、控制采样、事件逻辑和状态变量。
2. **中间表示构建**：将提取结果组织为计算图 $\mathcal{G} = (V, E)$，其中节点 $v_i \in V$ 表示基本运算（如 $R_{ij} \cdot i_j^{t}$ 或 $\int v \, dt$），边 $e_{ij} \in E$ 表示数据依赖。区分代数变量、连续状态、离散状态、端口变量和硬件 I/O。
3. **结构变换与优化**：执行常量折叠、矩阵结构预计算（对称/稀疏）、任务划分（串行/并行粒度）、查表生成和符号简化。对于 FPGA，引入**面向线程的归一化变换**：将复杂多端口元件通过线性状态扩展解耦为基本元件（电阻、电感、电容、互感、受控源）网络，每个基本元件线程执行近似同构的乘加运算（Song 等 2018）。
4. **目标后端选择**：选择目标平台后端（CPU 任务调度器、FPGA 流水线、GPU thread block/grid 或用户代码模型 API）。FPGA 后端还需处理时序约束（$t_{\mathrm{setup}} + t_{\mathrm{hold}} \leq T_{\mathrm{clock}}$）和流水线停顿条件。
5. **代码/HDL 生成**：生成目标代码并保留变量映射、单位、标幺基准、端口方向和版本信息。自动 HDL 生成需处理浮点单元例化（IEEE 754 单精度或自定义宽浮点格式）、存储控制器（双端口 RAM、FIFO）和时序约束注释（Song 等 2018；MTOF 2025）。
6. **部署与验证**：编译到目标平台（FPGA 综合、GPU JIT 编译或 CPU 交叉编译），在目标硬件上运行 SIL/HIL，对比源模型和生成代码的输出波形。

### 符号框架

若以 $\mathcal{G}_{\mathrm{CPU}}$、$\mathcal{G}_{\mathrm{FPGA}}$、$\mathcal{G}_{\mathrm{GPU}}$ 分别表示三类后端生成器，则

$$P_{\mathrm{CPU}} = \mathcal{G}_{\mathrm{CPU}}(M, C_{\mathrm{CPU}}, \theta_{\mathrm{CPU}})$$

$$P_{\mathrm{FPGA}} = \mathcal{G}_{\mathrm{FPGA}}(M, C_{\mathrm{FPGA}}, \theta_{\mathrm{FPGA}})$$

$$P_{\mathrm{GPU}} = \mathcal{G}_{\mathrm{GPU}}(M, C_{\mathrm{GPU}}, \theta_{\mathrm{GPU}})$$

其中 $C_{\mathrm{FPGA}} = \{T_{\mathrm{clock}}, N_{\mathrm{ALUT}}, N_{\mathrm{BRAM}}, L_{\mathrm{pipe}}\}$ 包含时钟周期、ALUT 数量、BRAM 数量和允许的流水线深度。

## 代码生成分类与变体

### 五类变体总览

| 变体 | 生成对象 | EMT 用途 | 核心约束 |
|------|----------|----------|----------|
| 控制代码生成 | C/C++ 或嵌入式任务 | 变流器控制、保护算法、HIL 控制接口 | 采样周期 $T_s$、限幅 $[v_{\min}, v_{\max}]$、状态初始化 |
| 求解器代码生成 | 矩阵求解任务、稀疏索引、历史项更新 | 实时 EMT、FPGA 求解器 | 数值格式（单精度/双精度）、矩阵非零结构、事件更新延迟 |
| HDL 生成 | 硬件流水线、并行算术单元 | FPGA EMT 和电力电子实时仿真 | 字长、流水线延迟（$L_{\mathrm{pipe}}$）、时序收敛、资源利用率 |
| 用户代码模型 | 目标仿真器可调用模块 | 无直接等价物的元件/控制器 | API 生命周期、状态保存/恢复、线程安全性 |
| 协同接口生成 | FMU 或主从接口胶水代码 | 多工具 EMT 协同仿真 | 步长匹配、信号校正（插值/外推）、同步策略（master-slave/平行） |

### 控制代码生成的 EMT 建模细节

控制代码生成将控制框图转换为嵌入式 C/C++ 任务，关键问题是**离散化与代码实现的语义等价性**。以 PI 控制器的离散实现为例：

连续形式：

$$u(s) = K_p \, e(s) + \frac{K_i}{s} \, e(s)$$

Tustin 变换（$s = \frac{2}{T_s} \frac{z-1}{z+1}$）离散化为：

$$u[n] = u[n-1] + \left(K_p + \frac{K_i T_s}{2}\right) e[n] - \left(K_p - \frac{K_i T_s}{2}\right) e[n-1]$$

在 EMT 仿真中，控制任务以固定步长 $T_s$ 执行，与电气网络求解同步。生成代码必须正确处理以下细节：
- **采样同步**：控制任务在每个电气步长结束时触发，$T_s$ 必须为电气步长的整数倍
- **控制延迟**：PWM 更新通常有 $1.5T_s$ 至 $2T_s$ 的延迟，需在生成代码中显式建模
- **限幅饱和**：抗饱和积分（anti-windup）的实现方式影响暂态响应

### GPU 并行 kernel 生成

Song 等 2018 提出的 GPU 代码生成框架核心变换如下：

**面向线程的归一化**：将复杂多端口元件（如 DFIG、VSC）通过线性状态扩展分解为基本元件网络：

原始状态空间形式：$\dot{x} = Ax + Bu, \; y = Cx + Du$

引入扩展状态 $z = Mx$，重写为：

$$\dot{z} = K z + L v, \; y = N z + Du$$

约束 $K$ 每行仅有一个非零元，$N$ 仅含 $\{0, 1, -1\}$，使耦合元件变为基本元件（电阻、电感、电容、互感、受控源）的连接。

**线程同构化**：每个 GPU 线程对应一个基本元件，执行融合乘加（FMA）操作：

$$i_{\mathrm{ne}}[t+\Delta t] = A \cdot u_b[t] + B \cdot i_b[t]$$

贡献累加到节点注入电流后，通过节点方程 $Y U = I$ 求解。

**控制 DAG 调度**：控制块组织为分层有向无环图（Layered DAG），同层控制块并行计算，层间同步保证数据依赖已满足。

### FPGA HDL 生成

FPGA 代码生成的输入是 EMT 网表和元件参数，输出是 VHDL/Verilog 代码。关键步骤包括：

**Modified Augmented Nodal Analysis (MANA)**：离散电路方程的未知量为节点电压和由电压源、电感、开关、传输线引入的支路电流/模态量，节点方程形式为：

$$Y_{\mathrm{aug}} \cdot u_{\mathrm{aug}} = i_{\mathrm{source}} + i_{\mathrm{hist}}$$

**Fast Assisted Modified Augmented Nodal Analysis (FAMNM)**：将开关状态变化转化为右端项更新，而非每次开关动作都重分解导纳矩阵。引入开关等效电导参数 $G_{\mathrm{eq}}$ 的最优选择以抑制数值振荡。

**稀疏矩阵-向量乘法（SpMV）硬件并行化**：在线/FPGA 侧按时间步并行更新右端向量，利用预存非零矩阵元素和稀疏索引执行 SpMV：

$$u_{\mathrm{next}} = Y^{-1} \cdot i_{\mathrm{inject}}$$

**48 位自定义浮点格式**：针对长递归卷积（如频变线路）抑制 32 位单精度的累积舍入误差。

### 求解器代码生成的数值格式问题

固定点转换（fixed-point conversion）在代码生成中至关重要。将连续参数转换为定点格式时：

$$v_{\mathrm{fixed}} = \mathrm{round}\left(\frac{v_{\mathrm{float}}}{2^{-N_{\mathrm{frac}}}}\right) = \mathrm{round}(v_{\mathrm{float}} \cdot 2^{N_{\mathrm{frac}}})$$

其中 $N_{\mathrm{frac}}$ 为小数位宽。溢出条件：

$$|v_{\mathrm{fixed}}| \leq 2^{N_{\mathrm{int}} - 1} - 1$$

溢出处理策略包括饱和截断、镜像舍入或扩展字宽。

## 量化性能边界

### GPU 加速数据（Song 等 2018）

| 测试系统 | 硬件 | 步长 | 加速比 | 实时性 |
|----------|------|------|--------|--------|
| 多 IEEE 33 节点 + DG | NVIDIA K20x | — | 相对于 CPU 程序有显著加速 | 在一定条件下实现实时 |
| 多 IEEE 33 节点 + DG | NVIDIA P100 | — | 相对于 CPU 程序有显著加速 | 在一定条件下实现实时 |

> 原文未报告可核验的具体加速比数值，各规模系统的节点/元件数量未在当前证据中完整呈现。

### FPGA 代码生成数据

| 来源 | 系统 | 代码生成时间 | 步长 | 精度 |
|------|------|-------------|------|------|
| MTOF 2025 | 4 机 11 节点 | 50 s | — | 高精度（相对离线 PSCAD/EMTDC） |
| MTOF 2025 | 10 机 39 节点 | 300 s | — | 高精度（相对离线 PSCAD/EMTDC） |
| Li 等 2025 | 15 台 PV-REG | — | 9 μs | 相对误差 < 0.5%（相对 PSCAD/EMTDC） |
| Li 等 2025 | 15 台 WT-REG | — | 10 μs | 相对误差 < 0.5%（相对 PSCAD/EMTDC） |
| Li 等 2025 | 15 台 PV-REG | — | — | 资源降低约 30%（相对传统 HDL 设计） |

> MTOF 验证局限于 4 机 11 节点和 10 机 39 节点两个标准系统，单 FPGA 板；Li 等 2025 局限于 15 台 PV/WT 规模。

### 自动代码生成工具链对比

| 工具/平台 | 输入 | 输出 | 自动化程度 | 代码透明度 |
|-----------|------|------|------------|------------|
| MTOF | MATLAB 拓扑 + 参数 | 可读 VHDL | 全自动 | 透明底层代码 |
| EMTP-RV → FPGA (自动化流程) | EMTP-RV 网表 | FPGA 实时任务 | 拓扑无关自动化 | 用户不可见 HDL |
| Song 等 2018 GPU | IEEE 33 节点 + DG | CUDA kernel | 自动生成专用 kernel | 可查看 kernel 代码 |
| Le-Huy 2023 (离线→实时) | 离线 EMT 模型 | HYPERSIM 任务/用户代码 | 半自动（需信号核对） | 用户代码可见 |

## EMT 工作流

典型自动代码生成的 EMT 工作流包含七个阶段：

1. **离线基线验证**：用源模型完成仿真，记录参数、工况和输出变量作为对比基准。
2. **目标平台约束明确化**：确定固定步长 $T_s$、deadline、I/O 延迟、数据类型（单精度/双精度/定点）、内存限制和并行粒度。
3. **变量冻结与规范**：在代码生成前冻结变量命名、单位、标幺基准和端口方向，防止生成过程中被意外修改。
4. **静态检查与编译检查**：对生成代码进行语法检查、类型检查、资源估算和时序约束预检。
5. **SIL/PIL 仿真**：运行软件在环或处理器在环仿真，比较源模型和生成代码的输出波形，分类差异来源。
6. **目标平台部署与测量**：在目标硬件上运行，记录执行时间、延迟、FPGA 资源占用/利用率（ALUT/BMB）、GPU SM 利用率和长时间运行状态稳定性。
7. **差异分类与修复**：将差异分类为模型差异（源模型与生成模型本质不同）、数值格式差异（浮点/定点精度）、接口差异（信号映射/时序）或生成器缺陷（工具 bug）。

## 关键技术挑战

### 挑战 1：连续模型到固定步长实时任务的语义间隙

源模型中的连续积分器（如 $\frac{dx}{dt} = f(x, u)$）在 EMT 离线仿真中可使用变步长求解器（如 Dormand-Prince、自适应 dt）。当目标平台要求固定步长 $T_s$ 时，连续模型必须离散化。对于 stiff 系统：

$$x[t+T_s] = x[t] + T_s \cdot f(x[t], u[t])$$

后向欧拉格式为：

$$x[t+T_s] = x[t] + T_s \cdot f(x[t+T_s], u[t+T_s])$$

变为隐式方程，需在每个步长求解代数方程。**自适应 dt 与固定 $T_s$ 的不兼容**是生成器必须处理的挑战——不是简单替换积分器，而是重新设计求解结构或引入额外缓冲。

### 挑战 2：变拓扑与事件处理的映射

开关动作、故障投入和模型切换（Mode Switching）在离线 EMT 中通过动态重新构建节点导纳矩阵处理。在实时 FPGA 任务中，**FAMNM 类方法**将拓扑变化转化为右端项更新，避免每次事件都重新分解导纳矩阵——但引入数值振荡问题需要开关等效电导参数优化协同处理。

### 挑战 3：FPGA 时序收敛与流水线延迟耦合

FPGA 上实现 $N$ 级流水线，每级延迟 $t_{\mathrm{pipe}}$，总延迟 $N \cdot t_{\mathrm{pipe}}$ 必须小于步长 $T_s$：

$$N \cdot t_{\mathrm{pipe}} < T_s$$

时序不收敛时，需插入流水线停顿（stall）或拆分运算级，但停顿引入额外延迟，反过来影响可用步长和闭环控制相位。

### 挑战 4：数值格式与精度边界

GPU 单精度（FP32）在长时间递归卷积中可能累积舍入误差。Li 等 2025 报告 48 位自定义浮点在 FPGA 上可抑制 32 位单精度的发散问题，但宽浮点格式占用更多 BRAM 资源：

$$\text{BRAM}_{\text{48-bit}} \approx 1.5 \times \text{BRAM}_{\text{32-bit}}$$

固定点格式需在动态范围和精度之间权衡：

$$\Delta v = 2^{-N_{\mathrm{frac}}}$$

量化噪声为：

$$\sigma_{\text{quant}}^2 = \frac{\Delta v^2}{12}$$

### 挑战 5：用户代码模型的 API 生命周期管理

用户代码模型（UCM）在实时仿真器中的调用顺序、内存生命周期和线程模型必须与 EMT 求解器协调。典型陷阱包括：

- **状态保存缺失**：模型在事件前后未保存内部状态，导致重启后行为不一致
- **内存泄漏**：动态内存分配在实时任务中不被允许
- **线程竞争**：多速率接口共享全局变量未加锁，导致数据不一致

## 适用边界与选择指南

### 平台选择决策表

| 场景 | 推荐后端 | 理由 |
|------|----------|------|
| 微秒级 HIL 测试（含电力电子开关） | FPGA | 低延迟、硬件并行、确定性 |
| 大规模系统参数扫描（离线） | GPU | 高并行度、大显存、适合批处理 |
| 毫秒级实时监控+控制 | CPU + RTOS | 灵活、可运行复杂操作系统任务 |
| 异构协同（CPU+FPGA+GPU） | 混合后端 | 各取所长，但接口复杂度高 |
| 多工具协同仿真（EMTP + RTDS） | FMU/FMI 接口 | 标准化的模型交换格式 |

### 代码生成器选择

| 生成器 | 适用阶段 | 不适用场景 |
|--------|----------|------------|
| MTOF（MATLAB→VHDL） | 教学/研究原型 | 大规模系统（>1000 节点）的生产级代码 |
| Song 2018 GPU kernel | 电气-控制强耦合系统 | 稀疏矩阵为主的纯网络求解 |
| FAMNM FPGA 自动化 | 开关动作频繁的电力电子 | 连续变流器（无开关事件） |
| Le-Huy 离线→实时 | 大规模电网 WAMPAC 研究 | 需要极小步长（<1 μs）的 HIL |

### 失败模式识别

- **拓扑解析失败**：网表含不支持的元件类型（生成器缺乏对应语法）→ 检查生成器元件库覆盖范围
- **时序不收敛**：FPGA 目标频率下关键路径延迟 > $T_{\mathrm{clock}}$ → 降低目标频率或拆分运算流水线
- **资源超限**：生成 HDL 超过 FPGA 板载资源（ALUT/BMB）→ 降低并行度或切换更大型号 FPGA
- **接口死锁**：多速率接口层间无正确同步信号 → 检查协调层时钟和握手协议

## 相关方法与相关页面

- [[real-time-simulation]] — 实时仿真是自动代码生成的主要应用目标
- [[fpga-real-time-simulation]] — FPGA 平台是自动 HDL 代码生成的主要目标
- [[hardware-acceleration]] — 硬件加速是代码生成的并行后端之一
- [[offline-to-realtime-porting]] — 离线到实时移植工作流依赖自动代码生成减少手工重建
- [[model-compatibility-layer]] — 模型兼容层处理源模型到目标环境的语义映射
- [[netlist-import-export]] — 网表导入导出是许多代码生成链条的输入层
- [[fixed-point-conversion]] — 定点转换处理生成代码中的数值表示问题
- [[gpu-parallel-acceleration]] — GPU 加速是自动代码生成的重要并行后端

## 来源论文

- [[2169-3536-c-2018-ieee-translations-and-content-mining-are-permitted-for-academic|Song 等 2018]] — 面向线程 GPU 并行 EMT 框架：基本元件同构化、LDAG 调度、自动 CUDA kernel 生成，IEEE Access
- [[an-automated-fpga-real-time-simulator-for-power-electronics-and-power-systems-el|Li 等 2024]]（EMT_Doc/07&08） — 自动化 FPGA 实时仿真器：MANA + FAMNM + 开关电导优化 + 稀疏矩阵并行，NI cRIO-9033 + Xilinx Kintex-7
- [[fine-grained-hardware-resource-optimization-and-design-for-fpga-based-real-time-|Li 等 2025]] — REG 控制系统细粒度资源优化：ALM/BMB 代价模型、Floyd-Warshall 关键路径、PV 9 μs / WT 10 μs
- [[mtof-a-novel-fpga-based-emt-toolbox-in-matlab|MTOF 2025]] — MATLAB 到 VHDL 自动生成工具箱：4 机 11 节点 50 s / 10 机 39 节点 300 s，Xilinx FPGA
- [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga-|Zhang 等 2022]] — FPGA 相域频变线路：诺顿等效 + 矢量拟合递归 + 48 位浮点，RTDS NovaCor 接口
- [[lessons-learned-in-porting-offline-large-scale-power-system-simulation-to-real-t|Le-Huy & Tremblay 2023]] — Hydro-Québec 离线到实时移植经验：模型库兼容、信号核对、UCM 重建、WAMPAC 工作流