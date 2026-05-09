---
title: "自动代码生成 (Automatic Code Generation)"
type: method
tags: [code-generation, real-time, fpga, automatic, model-based-design, hdl, c-code]
created: "2026-05-02"
---

# 自动代码生成 (Automatic Code Generation)


```mermaid
graph TD
    subgraph Ncmp[自动代码生成 (Automatic Code Gener…]
        N0[控制代码生成: C/C++ 或嵌入式任务]
        N1[求解器代码生成: 矩阵求解任务、稀疏索引、历史源更新]
        N2[HDL 生成: 硬件流水线、并行算术单元]
        N3[用户代码模型: 目标仿真器可调用的模块]
        N4[协同接口生成: FMU 或主从接口胶水代码]
    end
```


## 定义与边界

自动代码生成是把模型、网表、控制框图或中间表示转换为目标代码的过程。目标代码可以是 C/C++、硬件描述语言、用户代码模型、仿真器内部任务图或其他可部署形式。

在 EMT Wiki 中，本页关注代码生成作为方法的输入、输出、验证和失败边界。它不说明某个工具生成的代码一定更快，也不把代码生成等同于模型正确性；生成代码仍需与源模型、目标平台和目标工况逐项验证。

## EMT 中的作用

自动代码生成常用于：

- 从离线模型生成 [[real-time-simulation]] 任务或 [[hil-simulation]] 被控对象。
- 从电力电子或控制模型生成处理器代码、FPGA 逻辑或用户代码模型。
- 从网表和参数表生成 EMT 求解器所需的矩阵、稀疏索引、事件表和接口代码。
- 在 [[offline-to-realtime-porting]] 中减少手工重建模型的工作量。

对 EMT 来说，生成代码的关键不是语法转换，而是保持离散时间语义、事件处理、数值格式和接口延迟可追踪。

## 核心机制

典型生成链条包括：

1. 解析源模型，提取元件、状态、连接、参数、控制采样和事件逻辑。
2. 构建中间表示，区分连续状态、代数变量、离散状态、端口变量和硬件 I/O。
3. 进行符号或结构变换，例如常量折叠、矩阵结构预计算、任务划分和查表生成。
4. 选择目标后端，例如 CPU、FPGA、实时仿真器任务或用户代码模型。
5. 生成代码和元数据，保留变量映射、单位、缩放和版本信息。
6. 编译、部署并验证生成结果。

若源模型记为 $M$，生成器记为 $\mathcal{G}$，目标平台约束记为 $C$，可抽象为

$$
P_{\mathrm{target}} = \mathcal{G}(M, C, \theta),
$$

其中 $\theta$ 包括步长、数据类型、任务划分和接口设置。该表达不代表生成结果与源模型等价；等价性必须由验证给出。

## 分类与变体

| 变体 | 生成对象 | EMT 用途 | 主要检查 |
|---|---|---|---|
| 控制代码生成 | C/C++ 或嵌入式任务 | 变流器控制、保护算法、HIL 控制接口 | 采样、限幅、延迟和状态初始化 |
| 求解器代码生成 | 矩阵求解任务、稀疏索引、历史源更新 | 实时 EMT、FPGA 求解器 | 数值格式、矩阵重构和事件更新 |
| HDL 生成 | 硬件流水线、并行算术单元 | FPGA EMT 和电力电子实时仿真 | 字长、流水线延迟、资源和时序收敛 |
| 用户代码模型 | 目标仿真器可调用的模块 | 不可直接映射的元件或控制器 | API 生命周期和状态保存 |
| 协同接口生成 | FMU 或主从接口胶水代码 | 多工具 EMT 协同仿真 | 步长、信号校正和同步策略 |

## EMT 工作流

1. 先用源模型完成离线基线验证，记录参数、工况和输出变量。
2. 明确目标平台约束：固定步长、deadline、I/O、数据类型、内存和并行粒度。
3. 生成代码前冻结变量命名、单位、标幺基准和端口方向。
4. 对生成代码进行静态检查、编译检查和接口检查。
5. 运行软件在环或位真仿真，比较源模型和生成代码。
6. 在目标平台运行，记录执行时间、延迟、资源和长时间运行状态。
7. 将差异分类为模型差异、数值格式差异、接口差异或生成器缺陷。

## 适用边界与失败模式

- 源模型中的连续求解器、变步长事件和代数环不一定能直接映射到固定步长实时任务。
- 生成代码可能改变求值顺序、舍入、限幅、状态初始化或事件触发时刻。
- 对 FPGA，时序收敛和流水线延迟会反过来影响可用步长和闭环控制相位。
- 对用户代码模型，目标仿真器的调用顺序、内存生命周期和线程模型必须明确。
- 代码生成不能替代模型审查；若源模型参数错误，生成器会把错误稳定复制到目标端。
- 生成器版本、目标编译器和硬件平台变化后，应重新运行回归验证。

## 代表性证据

| 来源 | 可支持的认识 | 证据边界 |
|---|---|---|
| [[an-automated-fpga-real-time-simulator-for-power-electronics-and-power-systems-el]] | 从 EMTP-RV 网表到 FPGA 实时求解任务的自动化流程可包含拓扑解析、矩阵预处理和硬件求解 | 证据限于论文算例、开关模型和 FPGA 平台 |
| [[lessons-learned-in-porting-offline-large-scale-power-system-simulation-to-real-t]] | 离线到实时迁移中，自动导入导出和用户代码模型可减少手工重建，但仍需信号检查和波形比较 | 当前采用其工程经验，不复用未核验的量化结论 |
| [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga-]] | 频变线路等复杂模型进入 FPGA 平台时需要模型结构和硬件实现共同设计 | 具体精度和资源边界需按原文平台核验 |
| [[fine-grained-hardware-resource-optimization-and-design-for-fpga-based-real-time-]] | 硬件资源优化可作为代码生成后端设计的一部分 | 不应外推为所有模型或芯片的资源结论 |

## 与相关页面的关系

- [[model-compatibility-layer]] 处理源模型到目标环境的语义映射。
- [[netlist-import-export]] 是许多生成链条的输入层。
- [[fixed-point-conversion]] 处理生成代码中的数值表示问题。
- [[hardware-acceleration]] 和 [[fpga-real-time-simulation]] 关注目标硬件执行。
- [[emt-simulation-verification]] 提供生成代码验证的证据框架。

## 开放问题

后续扩展本页时，应优先补充可复现的生成链条记录：源模型哈希或版本、生成器版本、目标编译器、变量映射表、测试工况和差异报告。没有这些证据时，不应新增工具清单排名、固定性能收益或目标平台能力断言。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[2169-3536-c-2018-ieee-translations-and-content-mining-are-permitted-for-academic|Efficient GPU-based Electromagnetic Transient Simulation for]] | 2018 |
| [[2169-3536-c-2018-ieee-translations-and-content-mining-are-permitted-for-academic|Efficient GPU-based Electromagnetic Transient Simulation for]] | 2018 |
| [[fine-grained-hardware-resource-optimization-and-design-for-fpga-based-real-time-|Fine-grained hardware resource optimization and design for F]] | 2025 |
| [[mtof-a-novel-fpga-based-emt-toolbox-in-matlab|MTOF: A Novel FPGA-Based EMT Toolbox in MATLAB]] | 2025 |
| [[mtof-a-novel-fpga-based-emt-toolbox-in-matlab|MTOF: A Novel FPGA-Based EMT Toolbox in MATLAB]] | 2025 |
