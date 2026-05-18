---
title: "用户自定义代码模型 (User-Defined Code Model)"
type: model
tags: [user-defined, custom, code, model, s-function, programming, EMTP, FMI, TACS, FORTRAN]
created: "2026-05-02"
updated: "2026-05-19"
---

# 用户自定义代码模型 (User-Defined Code Model)

## 定义与边界

用户自定义代码模型是通过仿真器提供的脚本、动态库、外部子程序、S-Function、MODELS/TACS、FMI 或类似接口，把用户编写的微分方程、代数方程、控制逻辑或状态机嵌入 EMT 时步循环的模型。它的物理对象可以是新型设备、控制器、保护算法、非线性元件或外部工具；EMT 等效对象是接口函数、状态向量、输入输出变量、参数表和与主网络求解器的耦合方式。

本页讨论用户代码模型作为 EMT 模型的边界，不把任何特定工具的接口能力、跨平台兼容性或实时性能写成通用事实。具体语法和许可应以目标工具官方文档为准；本页只保留可迁移的建模结构。

## EMT 中的作用

用户代码模型在 EMT 仿真中承担三类核心任务：

**电气元件接口**：向网络方程贡献等效导纳、历史电流源、受控源或非线性残差。这类模型需要提供类似诺顿形式的接口方程 $\mathbf{i}_{inj,n} = \mathbf{G}_{eq,n}\mathbf{v}_n + \mathbf{i}_{hist,n}$，其中 $\mathbf{G}_{eq,n}$ 是等效导纳矩阵，$\mathbf{i}_{hist,n}$ 是历史电流源项，均需在每个时步更新。

**控制/保护逻辑嵌入**：读取电压电流或状态量，输出门极、跳闸、闭锁、参考值或限幅信号。控制逻辑通过 TACS 函数或 FORTRAN 用户子程序逐时步执行，其输出通过开关状态变化或受控源反馈到 EMT 网络。

**外部工具耦合**：与优化器、机器学习模型、FMU、硬件接口或批处理脚本交换数据。FMI 协同仿真接口通过共享内存和信号量机制实现 EMTP 主系统与控制子系统的内存解耦。

用户代码不是自由运行的外部程序，而是 EMT 求解器时序中的一个组件。其输入输出、采样时间、直接馈通、状态更新和错误处理必须与主程序求解顺序一致。

## 核心接口机制

### TACS 函数接口（EMTP 控制函数）

TACS（Transient Analysis of Control Systems）是 EMTP 中用于描述控制系统行为的专用语言和求解器。TACS 通过九类功能模块系统性地复现实际继电器硬件的动态行为，其核心创新在于利用传输延迟和脉冲发生器函数精确模拟模数转换（ADC）的采样保持动态、量化误差及采样率约束。

TACS 中的数字滤波器传递函数一般形式为：

$$

H(z) = \frac{Y(z)}{X(z)} = \frac{\sum_{m=0}^{M} b_m z^{-m}}{1 + \sum_{k=1}^{K} a_k z^{-k}}

$$

其中 $z^{-1}$ 表示单位采样延迟，$b_m$ 和 $a_k$ 为滤波器系数。该形式可用于在 TACS 中实现抗混叠滤波器和信号调理环节。

离散傅里叶变换（DFT）用于从采样序列提取基波分量的幅值和相位：

$$

X(k) = \sum_{n=0}^{N-1} x(n) \cdot e^{-j 2 \pi k n / N}

$$

其中 $N$ 为数据窗长度（全周期 DFT 取 $N$ 个采样点）。全周期 DFT 引入的固有延迟为 **16.67 ms**（1 个 60 Hz 周期），半周期 DFT 延迟为 8.33 ms 但牺牲部分精度。

为满足奈奎斯特采样定理，防止频谱混叠，采样率需满足：

$$

f_s \geq 2 f_{max}

$$

其中 $f_{max}$ 为待监测最高频率分量。典型采样率为每周波 12-24 点（$f_s = 720$–$1440$ Hz），对应采样间隔 $T_s \approx 0.7$–$1.4$ ms。

反时限过流继电器（TOC）动作时间特性方程为：

$$

t_{op} = \frac{0.14 \cdot T_{MS}}{(I/I_{pickup})^{0.02} - 1}

$$

其中 $T_{MS}$ 为时间倍数设定值，$I_{pickup}$ 为启动电流。该方程由 IEC 60255-151 标准定义。

零阶保持（ZOH）采样模型将连续信号转换为阶梯状离散信号：

$$

x_{hold}(t) = x(nT_s), \quad nT_s \leq t < (n+1)T_s

$$

### FMI 协同仿真接口

FMI（Functional Mock-up Interface）2.0 协同仿真标准将控制系统封装为 FMU（Functional Mock-up Unit）从系统，与 EMT 主网络在内存上解耦。EMTP 侧保留两个本来就存在的求解器分工：电力网络由改进增广节点法相关的稀疏雅可比迭代求解器处理，控制部分由 Jacobian-based 控制求解器处理。

主节点电力网络求解方程采用改进增广节点法：

$$

G \mathbf{v}(t) = \mathbf{i}_{src}(t) - \mathbf{i}_{hist}(t)

$$

其中 $G$ 为节点导纳矩阵，$\mathbf{v}(t)$ 为节点电压向量，$\mathbf{i}_{src}(t)$ 为等效电流源，$\mathbf{i}_{hist}(t)$ 为历史电流源项。

从节点控制系统状态空间微分代数方程（DAE）为：

$$

\dot{\mathbf{x}}_c = f(\mathbf{x}}_c, \mathbf{u}_c, t), \quad \mathbf{y}_c = g(\mathbf{x}}_c, \mathbf{u}_c, t)

$$

其中 $\mathbf{x}}_c$ 为控制状态，$\mathbf{u}}_c$ 为来自主网络的输入，$\mathbf{y}}_c$ 为反馈给主网络的控制输出。

FMI 协同接口通过共享内存缓冲区进行主从节点间控制信号与电气量的双向读写：

$$

\mathbf{u}_{slave}(t_k) = \mathcal{B}_{read}(\mathbf{y}_{master}, t_k), \quad \mathbf{u}_{master}(t_k) = \mathcal{B}_{read}(\mathbf{y}_{slave}, t_k)

$$

其中 $\mathcal{B}$ 为共享内存缓冲区。

每个 FMU slave 有独立协同仿真总线，包含三个核心信号量：SemInitialization（从系统接入总线）、SemMaster（从系统完成计算通知）、SemSlave（主节点数据就绪通知）。

### FORTRAN 用户子程序接口

EMTP 提供 FORTRAN 用户子程序接口，允许用户自定义继电器算法接入 EMT 闭环仿真。EPRI/DCG EMTP Version 2.0 增加了可链接用户 FORTRAN 子程序的结构，使计算机继电器算法可在 EMTP 仿真中处理电网数据并反馈保护动作。

FORTRAN 接口的 EMT 时域求解基本节点电压方程为：

$$

[G] \mathbf{V}_{node}(t) = \mathbf{I}_{node}(t)

$$

其中 $[G]$ 为实系数节点导纳矩阵，$\mathbf{V}_{node}(t)$ 为节点电压向量，$\mathbf{I}_{node}(t)$ 为节点注入电流向量。

## 模型结构与接口变量

连续或离散用户模型可写成状态空间形式：

$$

\dot{\mathbf{x}} = f(\mathbf{x}, \mathbf{u}, t, \mathbf{p}), \quad \mathbf{y} = g(\mathbf{x}, \mathbf{u}, t, \mathbf{p})

$$

离散时步实现可写成：

$$

\mathbf{x}_{n+1} = F(\mathbf{x}_n, \mathbf{u}_n, t_n, \mathbf{p}, \Delta t), \quad \mathbf{y}_n = G(\mathbf{x}_n, \mathbf{u}_n, t_n, \mathbf{p})

$$

若模型直接参与网络求解，还需要提供类似诺顿形式的接口方程：

$$

\mathbf{i}_{inj,n} = \mathbf{G}_{eq,n}\mathbf{v}_n + \mathbf{i}_{hist,n}

$$

接口变量应显式定义：

- **状态变量**：连续状态、离散状态、延迟队列、滤波器历史量、事件状态
- **代数变量**：当前输入、输出、残差、雅可比或等效导纳
- **控制变量**：参数、限幅、模式开关、采样时间、初始化条件
- **网络接口变量**：节点电压、支路电流、注入源、拓扑状态或外部端口变量

## 建模层级

| 层级 | 表示方式 | 适用用途 | 主要边界 |
|------|----------|----------|----------|
| 控制信号模型 | 输入输出函数或离散状态机 | 控制器、保护逻辑和调制器 | 不直接改变网络矩阵 |
| 等效电路模型 | 返回导纳、历史源或受控源 | 自定义 RLC、非线性元件和电力电子等效 | 需要满足主求解器接口 |
| 外部动态库模型 | C/C++/Fortran/S-Function 等编译接口 | 复用已有算法或加速计算 | ABI、内存和线程安全需验证 |
| 协同仿真模型 | FMI、进程间通信或外部求解器 | 多工具耦合和多速率仿真 | 同步、插值和能量一致性是主要风险 |
| 实时/HIL 模型 | 固定步长、预分配内存和确定性执行 | 实时仿真和硬件闭环 | 需报告最坏执行时间和接口延迟 |

## 量化性能边界

用户自定义代码模型在 EMT 仿真中已有可核验的量化结果，但以下数据均绑定具体接口方式、测试系统和仿真条件：

**TACS 教学框架（Boise 2004）**在 EMTP 中实现数字继电器闭环仿真，典型采样率为每周波 12-24 点（$f_s = 720$–$1440$ Hz），全周期 DFT 引入的固有延迟为 **16.67 ms**（1 个 60 Hz 周期），二阶抗混叠低通滤波器（截止频率 $f_c = 240$ Hz）可将 DFT 输出幅值误差从 **>15% 降至 <2%**。原文未报告可核验的加速比或误差上限。

**Cai（2018）**在 EMTP 中实现基于 FMI 2.0 的 master-slave 协同仿真架构，将控制系统封装为 FMU 从系统与电力网络主系统在内存上解耦。提供异步并行（多个 slave 在同一全局步长上并行运行）和同步多步（slave 在顺序环境中执行多个内部子步）两种模式。原文称观察到可观的计算时间收益并保持精度，但未报告可核验的加速比或误差上限。

**Chaudhary（2004）**在 EPRI/DCG EMTP Version 2.0 中集成 FORTRAN 用户子程序接口，典型仿真步长为 **50–100 μs**，继电器算法处理延迟 **<1 μs**，满足实时性要求。CT 模型可准确模拟频率高达数 kHz 的暂态过程；使用 Type 96 非线性电感时，$Z_{emtp}$ 必须设置为非零值（建议 $>10^{-6}$ Ω），否则矩阵条件数 $>10^{12}$ 导致数值发散。

这些量化数据不构成对所涉用户代码接口方法的全面性能评价，只说明在特定测试条件下可获得的能力边界。

## 适用边界与失败模式

- 直接馈通输入输出可能形成代数环，需要延迟、迭代或雅可比信息配合主求解器处理
- 事件、限幅和模式切换会造成不连续，若未使用插值方法或事件定位，可能出现时间步依赖结果
- 动态库模型存在内存越界、全局状态污染、线程不安全和平台 ABI 不兼容风险
- 外部协同仿真会引入通信延迟和插值误差，不能默认保持 EMT 主网精度
- 用户代码若直接修改网络矩阵或拓扑，应说明与节点导纳矩阵、数值积分和初始化流程的关系
- CT/CVT 暂态模型需校准饱和特性和频带范围，否则继电器看到的波形会失真

## 验证需求

用户自定义代码模型应从接口到系统分层验证：

- **接口验证**：输入输出维度、单位、采样时间、初值和参数范围检查
- **数值验证**：解析解、离线参考模型、等效内置模型或小信号线性化对比
- **事件验证**：边界条件、限幅、状态重置和模式切换是否可重复
- **集成验证**：接入 EMT 网络后是否破坏收敛、能量平衡或时步稳定性
- **可维护验证**：编译命令、依赖版本、错误处理和日志输出是否可复现

## 开放问题

- FMI 2.0 控制解耦方法报告了计算时间收益但未给出可核验的加速比和误差上限，不同耦合强度下的接口误差和稳定性边界尚不明确
- TACS/用户自定义代码的采样率选择（720–1440 Hz）在更高频电力电子接口场景下的适应性缺乏系统评估
- FORTRAN 用户子程序接口在现代 EMT 平台中的兼容性和与现代控制系统建模语言的桥接缺乏标准化更新
- 当换流器型电源比例较高时，用户自定义代码模型在弱电网和次同步频段下的接口延迟对闭环保护和控制精度的影响缺乏系统研究
- 用户代码模型在不同 EMT 平台（EMTP-RV、PSCAD、RTDS）间的接口语法和时序行为可移植性缺乏统一验证框架

## 相关页面

- [[modeling-language]] 讨论 EMTP 卡片、MODELS/TACS、PSCAD 自定义代码、SPICE 网表和 MATLAB/Simulink 模块等表达方式
- [[state-space-method]] 提供用户代码中常见的状态方程组织方式
- [[netlist-import-export]] 关注网表和模型文件的交换边界
- [[simulation-tools-status]] 记录工具入口和状态，不能替代具体接口文档
- [[protection-control-device]] 是用户代码模型常见应用之一，尤其是保护算法和控制逻辑
- [[nodal-admittance-matrix]] 与 [[nodal-analysis]] 是变压器进入网络方程的数值基础
- [[companion-model]] 解释 EMT 时域求解中常用的电流源并联导纳形式

## 来源论文

- [[using-tacs-functions-within-empt-to-teach-protective-relaying-fundamentals-power]] — Boise 2004, TACS函数实现数字继电器教学模型，量化数据：采样率720–1440 Hz，DFT延迟16.67 ms，滤波器误差从>15%降至<2%
- [[functional-mock-up-interface-based-approach-for-parallel-and-multistep-simulatio]] — Cai 2018, FMI 2.0 master-slave协同仿真，异步并行+同步多步两种模式
- [[protection-system-representation-in-the-electromagnetic-transients-program-power]] — Chaudhary 2004, FORTRAN用户子程序接口，步长50–100 μs，继电器延迟<1 μs
- [[functional-mock-up-interface-based-parallel-multistep-approach-with-signal-corre]] — FMI多步协同仿真信号校正方法

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*