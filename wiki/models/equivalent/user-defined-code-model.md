---
title: "用户自定义代码模型 (User-Defined Code Model)"
type: model
tags: [user-defined, custom, code, model, s-function, programming]
created: "2026-05-02"
---

# 用户自定义代码模型 (User-Defined Code Model)


```mermaid
graph TD
    subgraph Ncmp[用户自定义代码模型 (User-Defined Code…]
        N0[控制信号模型: 输入输出函数或离散状态机]
        N1[等效电路模型: 返回导纳、历史源或受控源]
        N2[外部动态库模型: C/C++/Fortran/S-Fun…]
        N3[协同仿真模型: FMI、进程间通信或外部求解器]
        N4[实时/HIL 模型: 固定步长、预分配内存和确定性执行]
    end
```


## 定义与边界

用户自定义代码模型是通过仿真器提供的脚本、动态库、外部子程序、S-Function、MODELS/TACS、FMI 或类似接口，把用户编写的微分方程、代数方程、控制逻辑或状态机嵌入 EMT 时步循环的模型。它的物理对象可以是新型设备、控制器、保护算法、非线性元件或外部工具；EMT 等效对象是接口函数、状态向量、输入输出变量、参数表和与主网络求解器的耦合方式。

本页讨论用户代码模型作为 EMT 模型的边界，不把任何特定工具的接口能力、跨平台兼容性或实时性能写成通用事实。具体语法和许可应以目标工具官方文档为准；本页只保留可迁移的建模结构。

## EMT 建模对象

用户代码模型通常承担三类任务：

- 电气元件：向网络方程贡献等效导纳、历史电流源、受控源或非线性残差。
- 控制/保护逻辑：读取电压电流或状态量，输出门极、跳闸、闭锁、参考值或限幅信号。
- 外部耦合：与优化器、机器学习模型、FMU、硬件接口或批处理脚本交换数据。

用户代码不是自由运行的外部程序，而是 EMT 求解器时序中的一个组件。其输入输出、采样时间、直接馈通、状态更新和错误处理必须与主程序求解顺序一致。

## 模型结构与接口变量

连续或离散用户模型可写成：

$$
\dot{\mathbf{x}} = f(\mathbf{x}, \mathbf{u}, t, \mathbf{p}),
\qquad
\mathbf{y} = g(\mathbf{x}, \mathbf{u}, t, \mathbf{p}).
$$

离散时步实现可写成：

$$
\mathbf{x}_{n+1} = F(\mathbf{x}_n, \mathbf{u}_n, t_n, \mathbf{p}, \Delta t),
\qquad
\mathbf{y}_n = G(\mathbf{x}_n, \mathbf{u}_n, t_n, \mathbf{p}).
$$

若模型直接参与网络求解，还需要提供类似：

$$
\mathbf{i}_{inj,n} = \mathbf{G}_{eq,n}\mathbf{v}_n + \mathbf{i}_{hist,n}.
$$

接口变量应显式定义：

- 状态变量：连续状态、离散状态、延迟队列、滤波器历史量、事件状态。
- 代数变量：当前输入、输出、残差、雅可比或等效导纳。
- 控制变量：参数、限幅、模式开关、采样时间、初始化条件。
- 网络接口变量：节点电压、支路电流、注入源、拓扑状态或外部端口变量。

## 建模层级

| 层级 | 表示方式 | 适用用途 | 主要边界 |
|------|----------|----------|----------|
| 控制信号模型 | 输入输出函数或离散状态机 | 控制器、保护逻辑和调制器 | 不直接改变网络矩阵 |
| 等效电路模型 | 返回导纳、历史源或受控源 | 自定义 RLC、非线性元件和电力电子等效 | 需要满足主求解器接口 |
| 外部动态库模型 | C/C++/Fortran/S-Function 等编译接口 | 复用已有算法或加速计算 | ABI、内存和线程安全需验证 |
| 协同仿真模型 | FMI、进程间通信或外部求解器 | 多工具耦合和多速率仿真 | 同步、插值和能量一致性是主要风险 |
| 实时/HIL 模型 | 固定步长、预分配内存和确定性执行 | 实时仿真和硬件闭环 | 需报告最坏执行时间和接口延迟 |

## 适用边界与失败模式

- 直接馈通输入输出可能形成代数环，需要延迟、迭代或雅可比信息配合主求解器处理。
- 事件、限幅和模式切换会造成不连续，若未使用 [[interpolation-method]] 或事件定位，可能出现时间步依赖结果。
- 动态库模型存在内存越界、全局状态污染、线程不安全和平台 ABI 不兼容风险。
- 外部协同仿真会引入通信延迟和插值误差，不能默认保持 EMT 主网精度。
- 用户代码若直接修改网络矩阵或拓扑，应说明与 [[nodal-admittance-matrix]]、[[numerical-integration]] 和初始化流程的关系。

## 验证需求

用户自定义代码模型应从接口到系统分层验证：

- 接口验证：输入输出维度、单位、采样时间、初值和参数范围检查。
- 数值验证：解析解、离线参考模型、等效内置模型或小信号线性化对比。
- 事件验证：边界条件、限幅、状态重置和模式切换是否可重复。
- 集成验证：接入 EMT 网络后是否破坏收敛、能量平衡或时步稳定性。
- 可维护验证：编译命令、依赖版本、错误处理和日志输出是否可复现。

## 代表性来源

- [[protection-system-representation-in-the-electromagnetic-transients-program-power]] 支持通过 FORTRAN 用户子程序把继电器算法接入 EMTP 闭环；其证据边界不支持泛化到所有接口或实时性能。
- [[using-tacs-functions-within-empt-to-teach-protective-relaying-fundamentals-power]] 代表用 TACS 函数实现保护教学模型，适合说明控制逻辑可进入 EMT 时步循环。
- [[functional-mock-up-interface-based-approach-for-parallel-and-multistep-simulatio]] 代表 FMI 协同仿真和多步控制接口路线；计算收益和精度需绑定具体主从划分。
- [[efficient-implementation-of-multi-port-frequency-dependent-network-equivalents-f]] 说明 MODELS、TACS Type-69 和外部子模型可作为 EMTP-ATP 中实现频变网络等值的不同接口选择。

## 与相关页面的关系

- [[modeling-language]] 讨论 EMTP 卡片、MODELS/TACS、PSCAD 自定义代码、SPICE 网表和 MATLAB/Simulink 模块等表达方式。
- [[state-space-method]] 提供用户代码中常见的状态方程组织方式。
- [[netlist-import-export]] 关注网表和模型文件的交换边界。
- [[simulation-tools-status]] 记录工具入口和状态，不能替代具体接口文档。
- [[protection-control-device]] 是用户代码模型常见应用之一，尤其是保护算法和控制逻辑。

## 来源论文

参见 [[index]] 获取更多用户自定义代码模型相关文献。
