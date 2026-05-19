---
title: "状态空间法 (State-Space Method)"
type: method
tags: [state-space, emt, matrix-exponential, descriptor-system, ssn, companion-circuit, nodal-analysis, pgssa]
created: "2026-04-13"
updated: "2026-05-19"
---

# 状态空间法 (State-Space Method)

## 定义与边界

状态空间法（State-Space Method）以状态向量 $\mathbf{x}$ 的一阶微分方程描述电气元件、控制模块和接口动态，在 EMT 仿真中的标准形式为：

$$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}, \qquad \mathbf{y} = \mathbf{C}\mathbf{x} + \mathbf{D}\mathbf{u}$$

其中 $\mathbf{x}$ 是状态向量（电感电流、电容电压、控制器积分量），$\mathbf{u}$ 是输入向量（端口电压、控制指令），$\mathbf{y}$ 是输出向量（端口电流或观测量），$\mathbf{A}$、$\mathbf{B}$、$\mathbf{C}$、$\mathbf{D}$ 为系统矩阵。

**与 [[nodal-analysis]] 的边界**：节点分析以网络节点电压为未知量，适合大规模稀疏 RLC 网络；状态空间法以内部状态为未知量，更适合内部动态丰富、端口有限、需要控制/模态/降阶解释的子系统。工程实现中常将设备内部写成状态空间，外部接入节点导纳方程——二者通过 [[companion-circuit]] 接口相互转换。

**描述符形式**：对含代数约束的系统（电感割集、电容回路、端口约束），可写成描述符形式：

$$\mathbf{E}\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}$$

其中 $\mathbf{E}$ 可能奇异，需检查一致初值和可解性。

## EMT 中的角色

状态空间法在 EMT 仿真中承担三类核心任务：

1. **子系统组织**：将变流器、控制器、旋转电机等内部动态丰富的设备组织成可离散推进的状态方程，通过接口接入全局网络方程。
2. **极点-留数模型时域递推**：将 [[vector-fitting]]、拉普拉斯逆变换或 [[prony-analysis]] 生成的极点-留数模型转成时域状态空间实现（$N$ 个一阶 RC/RL 支路对应 $N$ 状态）。
3. **模型降阶与实时压缩**：支撑 [[model-order-reduction]]（Krylov/PCA/平衡截断）和实时仿真中的模型压缩（预计算、分组）。

状态空间法特别适合描述"输入-输出-内部状态-端口变量"关系清晰的小型子系统。当研究重点是含大量开关事件的全网络拓扑重构时，直接状态矩阵重建可能比伴随电路+节点法更重。

## EMT 建模方法

### 方法一：状态空间-节点混合法（SSN）

**Dufour 等 2011** 提出的状态空间-节点混合法（State-Space Nodal, SSN）将电路分为若干 Cluster，每个 Cluster 内部用状态空间描述，Cluster 之间通过节点电压接口联立求解。

对任意 Cluster，状态空间方程离散化为：

$$\hat{\mathbf{A}}\mathbf{x}_{n+1} + \hat{\mathbf{B}}\mathbf{x}_n = \mathbf{u}_{\mathrm{ext},n}$$
$$\mathbf{y}_n = \hat{\mathbf{C}}\mathbf{x}_{n+1} + \hat{\mathbf{D}}\mathbf{x}_n$$

其中 $\hat{\mathbf{A}}$、$\hat{\mathbf{B}}$ 等为使用梯形积分法离散化后的矩阵：

$$\hat{\mathbf{A}} = \frac{2}{\Delta t}\mathbf{I} - \mathbf{A}, \qquad \hat{\mathbf{B}} = \frac{2}{\Delta t}\mathbf{I} + \mathbf{A}$$

将 Cluster 的端口电流-电压关系映射到全局节点导纳矩阵：

$$\mathbf{Y}_{\mathrm{port}} = \mathbf{G}_C - \mathbf{C}_c^T (\mathbf{A}^{*})^{-1}\mathbf{B}^{*}$$

其中 $\mathbf{A}^{*} = \mathbf{A} - \frac{2}{\Delta t}\mathbf{I}$，$\mathbf{G}_C$ 为电容伴随导纳。**SSN 方法的优势**：开关拓扑变化时只需重算目标 Cluster 的状态矩阵，无需重建全系统矩阵；每个 Cluster 可独立维护，降低大规模系统的矩阵更新成本。

### 方法二：分段广义状态空间平均法（P-GSSA）

**Wang 等 2019** 提出的分段广义状态空间平均法（P-GSSA）在广义状态空间平均法（GSSA）基础上引入分段策略，将动作特性一致的时间段合并研究。

开关函数为 $S_i \in \{0,1\}$（$i = a,b,c$ 表示三相）。对低频分量，非连续系统的微分方程为：

$$\dot{\mathbf{x}}(t) = \mathbf{f}(\mathbf{x}) + \mathbf{b}\mathbf{u}\left(d(\mathbf{x}) - \mathrm{tri}(t,T)\right)$$

其中 $d(\mathbf{x})$ 为占空比，$\mathrm{tri}(t,T)$ 为三角波。

对每一分段 $k$，开关周期 $T_s$ 内状态平均：

$$d_i^{(k)} = \frac{1}{T_s}\int_{t-T_s}^{t} S_i(\tau)d\tau, \qquad i=a,b,c$$
$$\mathbf{y}^{(k)}(t) = \mathbf{y}(t_0^{(k)}) + \int_{t_0^{(k)}}^t \mathbf{f}_0(\mathbf{y}(s))ds + \sum_{i=1}^{N}\int_{t_0^{(k)}}^t \mathbf{f}_i(\mathbf{y}(s))d_i^{(k)}(\mathbf{y}(s))ds$$

**P-GSSA 与 GSSA 的区别**：GSSA 保留谐波阶数 $K$（$K=1$ 即基本 SSA，$K$ 增大则精度提高但计算量增大）；P-GSSA 在 GSSA 基础上对开关动作特征变化点分段，使每段内谐波特性一致，从而在保持精度的前提下减少状态数量。

### 方法三：矩阵指数积分法

对于病态系统或高频暂态，直接数值积分可能引入较大数值误差。矩阵指数法直接计算 $\mathbf{x}_{n+1} = e^{\mathbf{A}\Delta t}\mathbf{x}_n + (\int_0^{\Delta t} e^{\mathbf{A}(\Delta t-\tau)}\mathbf{B}d\tau)\mathbf{u}_n$，可通过 Padé 近似或 Krylov 子空间方法实现。

**Li 等 2020** 对电力电子电路的矩阵指数插值研究指出：当 $\mathbf{A}$ 的特征值分布满足 $|\mathrm{Re}(\lambda_i\Delta t)| \ll 1$ 时，矩阵指数法优于梯形法；当 $|\mathrm{Re}(\lambda_i\Delta t)| \gg 1$ 时（刚性系统），需结合无条件稳定的后向欧拉法。

### 方法四：描述符状态空间法

对含微分-代数约束（DAE）的多端口网络，等效电路可写成微分-代数方程组：

$$\mathbf{E}\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}, \qquad \mathbf{0} = \mathbf{G}(\mathbf{x}, \mathbf{y})$$

其中 $\mathbf{E}$ 奇异时需使用隐式数值积分（如 Gear 法）避免解的矛盾。描述符形式在 [[synchronous-machine-model]]（发电机励磁绕组接口）和柔性直流换流站内部等效中应用广泛。

## 形式化表达

### 状态空间离散化（梯形积分）

$$\mathbf{x}_{n+1} = \mathbf{\Phi}\mathbf{x}_n + \mathbf{\Gamma}\mathbf{u}_n, \qquad \mathbf{\Phi} = \left(\frac{2}{\Delta t}\mathbf{I} - \mathbf{A}\right)^{-1}\left(\frac{2}{\Delta t}\mathbf{I} + \mathbf{A}\right), \quad \mathbf{\Gamma} = \left(\frac{2}{\Delta t}\mathbf{I} - \mathbf{A}\right)^{-1}\mathbf{B}$$

### SSN 端口等效

$$\mathbf{Y}_{\mathrm{port}} = \mathbf{G}_C - \mathbf{C}_c^T\left(\frac{2}{\Delta t}\mathbf{I} - \mathbf{A}\right)^{-1}\mathbf{B}^{*}$$

### P-GSSA 分段占空比

$$d_i^{(k)} = \frac{1}{T_s}\int_{t-T_s}^{t} S_i(\tau)d\tau, \quad i=a,b,c$$
$$\mathbf{\Phi}_k = \mathrm{diag}\left(e^{\lambda_1^{(k)}\Delta t}, \ldots, e^{\lambda_n^{(k)}\Delta t}\right)$$

## 关键技术挑战

**挑战一：开关拓扑频繁变化的矩阵重建**

每个开关状态对应不同 $\mathbf{A}$ 或端口矩阵时，预计算所有组合的状态矩阵集合会引发内存爆炸（$2^N$ 个矩阵，$N$ 为开关数）。SSN 方法通过 Cluster 分组策略解决——将开关集中在少数 Cluster 内，使大多数 Cluster 的 $\mathbf{A}$ 在开关动作时保持不变，从而减少矩阵重建次数。

**挑战二：非线性系统的数值稳定性**

状态空间表达非线性（饱和、磁滞）不困难，但线性矩阵形式和模态解释只对工作点或分段线性范围成立。P-GSSA 通过分段线性化将非线性系统分段处理，每段使用独立的 $\mathbf{A}^{(k)}$。

**挑战三：状态矩阵的稀疏性与计算效率**

大规模系统的 $\mathbf{A}$ 矩阵通常是稀疏的，但 $\mathbf{\Phi} = (s\mathbf{I}-\mathbf{A})^{-1}$ 的 Padé 近似或 Schur 分解可能破坏稀疏性。Krylov 子空间近似（Arnoldi 算法）在保持稀疏性的同时提供矩阵-向量乘的高效实现，适用于 $\mathbf{A}$ 规模 $n \geq 1000$ 的大系统。

**挑战四：降阶后的物理可解释性**

Krylov/PCA 降阶后的状态不一定保留原始物理含义（如特定电容电压、电感电流）。能量相关峰值和保护动作阈值需要单独验证，不能将降阶结果直接当作原始模型。

**挑战五：描述符系统的初值一致性**

$\mathbf{E}$ 奇异时，$\dot{\mathbf{x}}$ 的初始值 $\mathbf{x}(t_0)$ 必须满足与 $\mathbf{u}(t_0)$ 的一致性条件，否则离散化后的代数方程组无解。IEEE Task Force 推荐使用伴随电路初始条件求解器或小信号扰动法确认初值。

## 量化性能边界

### SSN 方法计算效率

| 应用场景 | 状态规模 | 开关组合 | SSN 效率提升 | 来源 |
|---------|---------|---------|-------------|------|
| 含 10 个开关的换流器 | 50 状态 | 2^10 = 1024 | Cluster 分组后无需全矩阵重建 | Dufour 2011 |
| 多换流器 MTDC | 每换流器 20 状态 | — | 矩阵更新仅限变化 Cluster | Dufour 2011 |
| 实时仿真（1ms 步长） | 每换流器 10 状态 | — | 预计算 + Cluster 分组 | Dufour 2011 |

### P-GSSA 精度与效率

| 谐波阶数 $K$ | 精度 | 状态数量 | 适用场景 |
|-------------|------|---------|---------|
| $K=1$（基本 SSA） | 基频分量准确，高频误差大 | 最少 | 机电暂态、低频动态 |
| $K=3$ | 基频+3次谐波 | 中等 | EMT 中频动态（$\leq 5$ kHz）|
| $K=7$ | 基频+7次谐波 | 较多 | EMT 宽频分析（$\leq 10$ kHz）|
| $K=13$ | 接近详细模型 | 最多 | 高频开关谐波（SiC/GaN，$\leq 100$ kHz）|

数据来源：Wang 等 2019，P-GSSA 方法对 401 电平 MMC 测试工况验证，$K=7$ 时误差 $<2\%$，计算时间约为详细模型的 $1/14$。

## 适用边界与选择指南

| 方法 | 适用条件 | 不适用条件 | 优势 |
|------|---------|-----------|------|
| SSN（Dufour 2011） | 含大量开关的换流器、实时仿真 | 纯 RLC 网络（稀疏矩阵法更直接） | 开关变化时局部矩阵更新 |
| P-GSSA（Wang 2019） | 大规模新能源并网变流器、多时间尺度 | 开关动作不一致性高的工况 | 多时间尺度、精度可调 |
| 矩阵指数法（Li 2020） | 病态系统、高频暂态 | 大规模稀疏系统（$\mathbf{A}$ 稠密化） | 高频精度、无条件稳定 |
| 描述符形式 | 含代数约束的多端口模型 | $\mathbf{E}$ 奇异且无物理初值 | 统一处理微分-代数约束 |

## 相关方法

- [[nodal-analysis]]：全局网络方程（节点电压法）；状态空间法用于局部动态，通过伴随电路接口接入。
- [[companion-circuit]]：动态元件的梯形积分离散化；状态空间法保留显式状态递推。
- [[vector-fitting]]：极点-留数模型转时域状态空间（$N$ 个一阶支路 = $N$ 状态）。
- [[model-order-reduction]]：状态空间模型为输入；降阶误差需时域+频域双重验证。
- [[small-signal-stability]]：小信号分析依赖线性化 $\mathbf{A}$ 矩阵；不能直接代表大扰动 EMT 行为。
- [[trapezoidal-rule]]：状态空间法最常用的离散化数值积分。
- [[backward-euler]]：无条件稳定，适合处理刚性系统状态方程。

## 来源论文

- [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient|Dufour 等 2011]] — SSN 方法奠基论文，提出状态空间-节点混合法，将状态空间 Cluster 通过梯形积分转换为端口 Norton/Thévenin 等效接入全局节点导纳矩阵；开关拓扑变化时仅更新变化 Cluster 的矩阵，显著减少计算量；适用于含大量开关的换流器和实时仿真场景。
- [[a-piecewise-generalized-state-space-model-of-power-converters-for-electromagneti|Wang 等 2019]] — P-GSSA 方法论文，将分段策略引入广义状态空间平均法（GSSA），解决变流器多时间尺度建模问题；$K=7$ 谐波阶数时误差 $<2\%$，计算时间约为详细模型 $1/14$；适用于大规模新能源并网变流器 EMT 高效仿真。
- [[splitting-state-space-method-for-converter-integrated-power-systems-emt-simulati|Fu 等 2025]] — 分裂状态空间法，将换流器集成电力系统 EMT 方程分裂为快动态（开关/换流器）和慢动态（网络/控制）两部分，采用不同步长分别求解；适用于柔性直流和新能源聚合系统的多速率联合仿真。
- [[a-state-space-approach-for-accelerated-simulation-of-modular-multilevel-converte|Zhao 等 2026]] — MMC 加速仿真状态空间方法，通过预计算状态转移矩阵和 Schur 补分解实现嵌套快速求解；相对于详细开关模型加速 310× 以上，精度损失 $<1\%$。
- [[a-semi-analytical-approach-for-state-space-electromagnetic-transient-simulation|Xiong 等 2024]] — 半解析状态空间 EMT 方法，利用解析矩阵指数和分段线性近似处理开关动作时刻的跳变；避免数值积分在奇异时刻的精度退化，适用于含硬开关的电力电子电路。