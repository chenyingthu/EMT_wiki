---
title: "分布式控制 (Distributed Control)"
type: method
tags: [distributed-control, coordination, communication, multi-agent, microgrid, consensus, droop]
created: "2026-05-05"
updated: "2026-05-16"
---

# 分布式控制 (Distributed Control)

## 定义与边界

分布式控制是指多个控制单元在仅使用局部测量和有限邻居通信的条件下，共同完成功率共享、电压恢复、频率恢复、一致性调节或协同优化的控制方法。它介于完全去中心化控制和集中式主站控制之间，通过邻居交互实现全局协调目标。

在 EMT 仿真中，分布式控制常用于研究多逆变器/多储能单元之间的功率共享与二次恢复、多端直流系统中站间电压/功率协调、通信延迟和拓扑变化对闭环性能的影响，以及一致性算法在暂态事件下的收敛性与鲁棒性评估。

本页讨论的是**控制架构与协调机制**，不涉及 CPU-FPGA 多速率仿真框架、硬件分区求解或换流器详细模型。

## EMT 中的角色

在电磁暂态仿真中，分布式控制扮演着连接系统物理层与协调控制层的桥梁角色：

1. **多逆变器/储能协调**：当系统中存在多个并联的 VSC 或储能变流器时，各单元通过分布式协议（如一致性协议）实现功率自动共享，无需中央控制器
2. **站间协同控制**：在多端直流系统（如 MTDC）或联网微电网中，各换流站通过分布式协调实现电压和功率的全局优化
3. **通信质量评估**：通过 EMT 仿真可以评估通信延迟、丢包、拓扑切换对分布式控制收敛性的影响
4. **故障穿越分析**：在短路等大扰动下，评估分布式控制能否保持同步和稳定性

分布式控制通常不是替代一次控制（如[[droop-control]]下垂控制），而是叠加在下垂、站控或保护逻辑之上，形成分层协调架构。

## 主要机制

分布式控制的运行机制包含四个核心层次：

### 1. 局部测量与状态估计

每个控制单元 $i$ 采集本地电气量：
- 频率偏差：$\Delta f_i = f_i - f_{ref}$
- 电压偏差：$\Delta V_i = V_i - V_{ref}$
- 有功/无功输出：$P_i$, $Q_i$
- 荷电状态（储能）：$SoC_i$

局部估计值 $\hat{x}_i$ 通过滤波或观测器获得，减少测量噪声影响。

### 2. 邻居信息交换

通过通信网络，单元 $i$ 与邻居集合 $\mathcal{N}_i$ 交换状态信息：

$$y_{ij} = x_j, \quad \forall j \in \mathcal{N}_i$$

信息交换可采用：
- **广播式**：周期性地向所有邻居发送本地状态
- **请求-响应式**：按需查询邻居状态
- **事件触发式**：仅当状态变化超过阈值时触发通信

### 3. 一致性协同律

分布式协同律是实现全局协调的核心。常见的一致性协议包括：

**连续时间一阶一致性协议**：
$$\dot{x}_i(t) = -\sum_{j \in \mathcal{N}_i} a_{ij}(x_i(t) - x_j(t)) + b_i u_i(t)$$

其中：
- $x_i$：单元 $i$ 的状态变量（频率偏差、电压、功率等）
- $a_{ij}$：耦合权重（与通信拓扑相关）
- $b_i$：输入增益
- $u_i$：本地控制输入

**离散时间一阶一致性协议**：
$$x_i(k+1) = x_i(k) + \epsilon \sum_{j \in \mathcal{N}_i} a_{ij}(x_j(k) - x_i(k))$$

其中 $\epsilon$ 为步长参数，需满足协议收敛条件。

**二阶一致性协议**（考虑动态系统）：
$$\begin{aligned}
\dot{x}_i &= v_i \\
\dot{v}_i &= \sum_{j \in \mathcal{N}_i} a_{ij}(x_j - x_i) + \sum_{j \in \mathcal{N}_i} b_{ij}(v_j - v_i)
\end{aligned}$$

### 4. 本地执行层与主电路接口

分布式控制的输出通过以下方式与 EMT 主电路耦合：

**电流注入接口**：将协同律计算的电流参考值注入 PWM 调制器
$$I_{ref,i} = f_{consensus}(x_i, \{x_j, j \in \mathcal{N}_i\})$$

**电压基准接口**：调整变流器输出电压基准
$$V_{ref,i}^{new} = V_{ref,i}^{old} + \Delta V_{coord,i}$$

**功率参考接口**：修改有功/无功功率设定点
$$P_{ref,i}^{new} = P_{ref,i}^{old} + \Delta P_{share,i}$$

## 主要分支与分类

在 EMT 场景下，分布式控制按功能和协调目标分为三类：

### 分支一：分布式二次频率/电压恢复

在 [[droop-control]] 一次控制的基础上，通过分布式协同实现二次恢复：

**频率二次恢复协同律**：
$$\dot{\delta} = -\sum_{j \in \mathcal{N}_i} \phi_{ij}(\delta_i - \delta_j) - k_i(\omega_i - \omega_{ref})$$

**电压二次恢复协同律**：
$$\dot{V}_{dc,i} = -\sum_{j \in \mathcal{N}_i} \psi_{ij}(V_i - V_j) - \lambda_i(V_i - V_{ref})$$

其中 $\phi_{ij}, \psi_{ij}$ 为协调权重，$k_i, \lambda_i$ 为恢复增益。

典型应用：微电网孤岛运行时，多 DG 单元协同维持频率和电压稳定。

### 分支二：分布式功率共享与协调

实现多逆变器、多储能或多端直流系统之间的功率协调：

**有功功率均分**：
$$P_i^* = P_{total}^* \cdot \frac{1}{\sum_{j \in \mathcal{V}} w_j} \cdot w_i$$

其中 $w_i$ 为权重（可以是容量、荷电状态等）。

**基于荷电状态的储能协调**：
$$P_i^* = P_{available,i} \cdot \frac{\sum_{j \in \mathcal{V}} (SoC_j - SoC_{target})}{\sum_{j \in \mathcal{V}} SoC_j - SoC_{target}}$$

典型应用：电池储能系统（BESS）多并联单元之间的荷电状态均衡。

### 分支三：分布式优化与约束协调

将经济性、约束条件融入协同控制：

**凸优化协调**：
$$\min \sum_{i \in \mathcal{V}} C_i(P_i) \quad \text{s.t.} \quad \sum P_i = P_{load}, \quad P_i \in [P_i^{min}, P_i^{max}]$$

通过交替方向乘子法（ADMM）分布式求解。

**约束协调**：保证各单元运行在安全区间内
$$\begin{aligned}
\min & \sum_{i \in \mathcal{V}} c_i(x_i) \\
\text{s.t.} & \|x_i - x_j\| \leq \epsilon_{ij}, \quad \forall i,j \in \mathcal{N}_i
\end{aligned}$$

典型应用：多端 VSC-HVDC 系统的经济调度、含多约束的微电网优化运行。

## 形式化表达

### 图论基础

分布式控制的通信拓扑用图 $\mathcal{G} = (\mathcal{V}, \mathcal{E}, A)$ 描述：

**节点集合**：$\mathcal{V} = \{1, 2, \ldots, N\}$，表示 $N$ 个控制单元

**边集合**：$\mathcal{E} \subseteq \mathcal{V} \times \mathcal{V}$，表示通信链路

**权重矩阵**：$A = [a_{ij}] \in \mathbb{R}^{N \times N}$，其中：
$$a_{ij} = \begin{cases} w_{ij} & \text{if } (j, i) \in \mathcal{E} \\ 0 & \text{otherwise} \end{cases}$$

**度矩阵**：$D = \text{diag}(d_1, d_2, \ldots, d_N)$，其中 $d_i = \sum_{j \in \mathcal{N}_i} a_{ij}$

**拉普拉斯矩阵**：$L = D - A$

### 一致性协议数学表达

**连续时间协议收敛性**：

对于无向连通图 $\mathcal{G}$，一阶协议 $\dot{x} = -L \otimes I \cdot x$ 渐近收敛到平均值：
$$\lim_{t \to \infty} x_i(t) = \frac{1}{N} \sum_{j=1}^N x_j(0)$$

**收敛速率**：
$$\|x_i(t) - \bar{x}| \leq |x_i(0) - \bar{x}| \cdot e^{-\lambda_2(L) \cdot t}$$

其中 $\lambda_2(L)$ 为拉普拉斯矩阵的第二小特征值（代数连通度）。

**离散时间协议收敛条件**：

步长 $\epsilon$ 需满足：
$$0 < \epsilon < \frac{1}{\max_i d_i}$$

收敛速率约为 $1 - \epsilon \cdot \lambda_2(L)$。

### 分布式估计器

**Kronecker 积形式**：
$$\dot{X} = (A - B K) X + B U$$

其中 $A$ 和 $B$ 为系统矩阵，$K$ 为反馈增益矩阵。

**分布式卡尔曼滤波**：
$$x_i(k+1) = A x_i(k) + w_i(k)$$
$$z_i(k) = H x_i(k) + v_i(k)$$

## 关键技术挑战

### 挑战一：通信延迟对一致性的影响

当存在通信延迟 $\tau_{ij}$ 时，协议变为：
$$\dot{x}_i = -\sum_{j \in \mathcal{N}_i} a_{ij}(x_i(t) - x_j(t - \tau_{ij}))$$

**延迟上界**：
$$\tau_{ij} < \frac{\pi}{2 \cdot \lambda_{\max}(L)}$$

超过延迟上界可能导致协议振荡或发散。

### 挑战二：通信拓扑切换的鲁棒性

当拓扑切换时，拉普拉斯矩阵从 $L_i$ 切换到 $L_j$，系统需保证：
$$\lim_{t \to \infty} \|x_i(t) - \bar{x}(t)\| = 0$$

**联合连通条件**：切换拓扑的并图 $\bigcup_{k=0}^{\infty} \mathcal{G}_{t_k}$ 需保持连通。

### 挑战三：非理想通信条件

**丢包模型**：采用伯努利丢包过程
$$P(y_{ij} = 0) = p_{ij}$$

**异步通信**：各单元通信周期可能不同步
$$T_i \in [T_{i,min}, T_{i,max}]$$

### 挑战四：大规模系统的计算效率

对于 $N$ 个单元的全耦合问题，直接求解复杂度为 $O(N^3)$。分布式方法通过：
- **图分解**：将大系统划分为若干连通子图
- **异步迭代**：各子图并行求解后协调
- **稀疏化**：利用拓扑稀疏性减少通信量

## 量化性能边界

### 一致性收敛性能

| 参数 | 典型值 | 边界条件 |
|------|--------|----------|
| 通信延迟容忍上界 | 10-50 ms | 与拓扑连通度和耦合权重相关 |
| 收敛时间（100单元） | 50-200 ms | 连通拓扑下实测 |
| 收敛精度 | $< 0.01\%$ | 稳态误差 |
| 拓扑切换恢复时间 | 20-100 ms | 联合连通条件下 |

### EMT 仿真性能

| 指标 | 典型范围 | 说明 |
|------|----------|------|
| 协同控制更新周期 | 1-10 ms | 取决于通信带宽 |
| EMT 仿真步长 | 10-100 μs | 变流器开关精度要求 |
| 步长比 | 100-1000 | 控制周期/EMT步长 |
| 通信带宽需求 | 10-100 kbps/节点 | 与状态向量维度相关 |

### 工程验证数据

**Rashidirad 2023 (MANA-based)**：提出统一潮流计算框架，每个 AC MG 可有独立频率变量，通过 IC 约束耦合实现多频 MMG 的统一求解，验证系统含 2 个 AC MG、1 个 DC MG 和 2 个 IC。

**Xu 2020 (FPGA 实时仿真)**：微电网测试系统含 3 个三相变流器、3 个 Boost 电路和 21 条三相线路，在单块 Kintex-7 410T FPGA 上实现 380 ns 步长实时仿真。网络解耦算法使计算复杂度从 $O(N^2)$ 降为 $O(N)$。

**分布式混合仿真接口 (2017)**：两级舒尔补更新策略消除了多 EMT 子系统间动态耦合带来的接口等效误差；组合交互协议在稳态阶段使通信开销降低 50% 以上；接口电流相对变化率阈值 ε 设定为 2%-10% 时可实现精度与效率的最优平衡。

## 适用边界与选择指南

### 适用场景

| 应用场景 | 推荐分支 | 关键指标 |
|----------|----------|----------|
| 微电网频率/电压二次恢复 | 分支一 | 收敛时间 < 200 ms，频率误差 < 0.01 Hz |
| 多储能系统荷电状态均衡 | 分支二 | 均衡时间 < 5 min，SoC 偏差 < 5% |
| 多端 HVDC 系统协调 | 分支二 | 功率分配误差 < 1%，响应时间 < 100 ms |
| 联网微电网经济优化 | 分支三 | 优化迭代 < 50 次，计算时间 < 1 s |
| 大规模系统分布式估计 | 估计器 | 估计误差 < 2%，通信开销 O(N) |

### 失效场景

- **通信中断**：邻居信息完全丢失时，一致性协议退化为仅本地控制
- **强非线性负荷**：负荷突变可能导致协同律跟踪误差过大
- **异构通信时延**：各单元时延差异超过 50% 可能导致振荡
- **恶意节点**：存在说谎节点时需引入容错机制

## 相关方法

- [[droop-control]]：一次共享机制，通常是分布式二次控制的下层
- [[hierarchical-control]]：说明分层结构中分布式控制通常位于中间层
- [[multi-terminal-dc]]：多端直流系统中常见协同控制背景
- [[microgrid-control]]：微电网中频率/电压恢复与功率共享场景
- [[frequency-control]]：分布式控制常作为频率和电压二次恢复层的实现方式
- [[wide-area-monitoring-protection]]：大范围测量与协调执行的背景
- [[co-simulation]]：联合仿真中用于异构子系统间的接口协调

## 来源论文

- [[unified-mana-based-load-flow-for-multi-frequency-hybrid-acdc-multi-microgrids]]：多微电网频率协同的 MANA 潮流框架，每个 AC MG 频率作为独立变量
- [[fpga-based-sub-microsecond-level-real-time-simulation-for-microgrids-with-a-netw]]：网络解耦实现微电网 380 ns 实时仿真，计算复杂度 $O(N)$
- [[a-novel-interfacing-technique-for-distributed-hybrid-simulations-combining-emt-a]]：分布式 EMT-TS 混合仿真的两级舒尔补接口与组合交互协议
- [[co-simulation-applied-to-power-systems-with-high-penetration-of-distributed-ener]]：高渗透率 DER 系统的 FMI 联合仿真与虚构传输线接口

## 开放问题

1. **异步通信下的收敛性**：当前分析主要基于同步通信假设，异步条件下的收敛性分析尚不完善
2. **事件触发更新机制**：如何设计事件触发条件减少通信量而不影响控制性能
3. **通信失效容错**：节点故障或通信链路失效时的分布式容错控制
4. **异质系统协调**：异构逆变器/储能单元的分布式协调控制
5. **实时性能保障**：大规模分布式控制在实时仿真中的性能优化