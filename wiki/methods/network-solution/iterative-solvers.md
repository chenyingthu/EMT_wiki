---
title: "迭代求解方法 (Iterative Solvers)"
type: method
tags: [iterative-solver, nonlinear, newton-raphson, krylov, convergence]
created: "2026-04-14"
updated: "2026-05-10"
---

# 迭代求解方法 (Iterative Solvers)

## 1. 物理背景与工程需求

EMT 仿真中，每个时间步都需要求解由网络离散化方程和非线性元件特性共同形成的代数方程。迭代求解方法用于以下场景：

1. **非线性元件**：饱和变压器、避雷器、电弧模型的伏安特性 $v = f(i)$ 使节点方程变为非线性，需迭代求解
2. **隐式积分**：后向欧拉、梯形法或 DIRK 类隐式积分在离散化后形成非线性代数方程
3. **大规模线性系统**：当网络规模太大，稀疏直接法（LU 分解）的内存或计算时间不可接受时，迭代法作为替代
4. **接口协调**：多速率、混合仿真或分区网络中的边界量耦合需松弛或固定点迭代

迭代法与直接法的根本区别在于：直接法通过因子化一次性求解线性方程；迭代法通过逐步逼近解，需要收敛判据、初值、预处理和失败处理。对于硬实时 EMT，迭代次数不确定本身就是一个建模和调度风险。

## 2. 数学描述

### 2.1 牛顿-拉夫逊法（NR）

非线性方程组 ${\bf F}({\bf x}) = {\bf 0}$ 的牛顿迭代为：

$$
{\bf J}({\bf x}^{(k)}) \Delta {\bf x}^{(k)} = -{\bf F}({\bf x}^{(k)}),
\qquad
{\bf x}^{(k+1)} = {\bf x}^{(k)} + \alpha_k \Delta {\bf x}^{(k)}
$$

其中 ${\bf J} = \partial {\bf F}/\partial {\bf x}$ 是雅可比矩阵，$\alpha_k$ 是可选阻尼因子。标准牛顿法在解附近具有二阶收敛速度，但全局收敛依赖初值、阻尼和方程光滑性。

在 EMT 中，非线性元件通常用分段线性（PWL）曲线表示。标准 NR 在每个分段内效率高，但在分段边界附近可能来回跳变，陷入无限循环。

### 2.2 双轴牛顿-拉夫逊法（Biaxial NR）

Noda & Kikuma (2011) 提出的双轴 NR 在标准 NR 的雅可比中引入电流轴导数信息作为正则化项：

$$
{\bf J}_{biax}^{(k)} = \text{diag}\left(\frac{\partial i}{\partial v}\right)^{(k)} + \alpha \cdot \text{diag}\left(\frac{\partial v}{\partial i}\right)^{(k)}
$$

其中 $\alpha$ 为正则化因子（$0.05$--$0.1$），利用 PWL 曲线两个轴向的信息约束迭代路径，降低在折点附近错误跨段的概率。双轴 NR 的有效收敛域较标准 NR 扩大约 3.2 倍。

### 2.3 Krylov 子空间方法

对线性系统 ${\bf A} {\bf x} = {\bf b}$，Krylov 方法在残差生成的子空间 $\mathcal{K}_m = \text{span}\{{\bf r}_0, {\bf A}{\bf r}_0, \dots, {\bf A}^{m-1}{\bf r}_0\}$ 中寻找近似解。预处理形式为：

$$
{\bf M}^{-1} {\bf A} {\bf x} = {\bf M}^{-1} {\bf b}
$$

| 方法 | 适用条件 | EMT 用途 |
|------|----------|----------|
| CG | 对称正定 | 特殊网络结构 |
| GMRES | 一般非对称 | 大规模稀疏系统 |
| BiCGSTAB | 非对称，每步代价低于 GMRES | 非对称网络 |

CG 需要对称正定条件，普通 EMT 导纳矩阵未必满足。GMRES 和 BiCGSTAB 更常用于非对称或不定系统。

### 2.4 固定点迭代

用于弱耦合接口协调（如混合仿真边界）：

$$
{\bf x}^{(k+1)} = {\bf G}({\bf x}^{(k)})
$$

收敛条件为 $\rho(\partial {\bf G}/\partial {\bf x}) < 1$。在强耦合系统中可能发散。

## 3. 计算模型与离散化

### 3.1 迭代求解与 EMT 时间步的集成

每个 EMT 时间步内，迭代求解器的工作流程为：

```text
每个时间步 n:

1. 组装阶段:
   - 从上一时间步获取初值 x^(0)
   - 组装导纳矩阵 G 和历史源 I_hist
   - 对非线性元件，获取当前工作点 PWL 分段斜率

2. 迭代阶段:
   while (||F(x^(k))|| > epsilon) and (k < k_max):
     - 计算雅可比 J^(k)（标准 NR）或 J_biax^(k)（双轴 NR）
     - 解 J * dx = -F(x^(k))
     - 更新 x^(k+1) = x^(k) + dx
     - k = k + 1
     - 若发散: 切换更高稳健性方法

3. 输出阶段:
   - 用收敛解更新历史源
   - 推进到下一时间步
```

### 3.2 三级递进求解框架

Noda & Kikuma (2011) 提出了针对 PWL 非线性电路的三级递进策略：

| 级别 | 方法 | 调用率 | 计算代价 |
|------|------|--------|----------|
| 1 | 标准 NR | > 95% | 最低 |
| 2 | 双轴 NR | ~4.5% | 中等 |
| 3 | Katzenelson 算法 | < 0.5% | 最高但全局收敛 |

切换判据：残差连续 3 次未下降或迭代次数 > 5。Katzenelson 算法为兜底，利用 PWL 问题可划分为多个线性区域的结构，其收敛性在数学上有保证。

该策略使非线性电路 EMT 仿真的全局收敛率达到 100%，单步平均迭代次数控制在 4 次以内。

### 3.3 FPGA 上的并行迭代实现

Chen & Dinavahi (2011) 在 FPGA 上用补偿法分离非线性元件后，采用连续牛顿法（CNR）和分段牛顿法（PNR）迭代求解端口方程。CNR 需计算雅可比 ${\bf J} = {\bf Z}_{th} + \partial {\bf f}/\partial {\bf i}$，每次迭代解 ${\bf J} \Delta {\bf i} = -{\bf F}$。PNR 免去雅可比计算，直接解 $({\bf Z}_{th} + R_j {\bf I}){\bf i}^{k+1} = {\bf v}_{oc} - e_j$。

## 4. 实现方法与算法细节

### 4.1 预处理策略

Krylov 方法的收敛速度高度依赖预处理矩阵 ${\bf M}$ 的选择：

| 预处理方法 | 机制 | 适用场景 |
|-----------|------|----------|
| ILU（不完全 LU） | 近似 LU 分解 | 通用稀疏系统 |
| 块对角 | 按区域分块求逆 | 分区网络 |
| Schur 补 | 消去内部变量 | 多区域接口 |
| 零阶 | 仅对角线缩放 | 对角占优系统 |

预处理构造本身也有计算成本，需权衡构建代价与迭代次数节省。

### 4.2 实时仿真中的迭代约束

实时 EMT 中，迭代次数必须在固定步长内完成。主要应对策略：

1. 设最大迭代次数上限 $k_{max}$，超限则使用当前近似解或回退到上一时间步解
2. 用上一时间步解作为当前步初值（${\bf x}^{(0)} = {\bf x}_n$），通常足够接近
3. 对分段线性元件，初值落在正确分段的概率高，NR 往往 1--2 次即收敛
4. 硬实时中迭代次数不确定性本身就是调度风险——需结合最坏情况分析和硬件余量

## 5. 适用边界与失效模式

### 适用条件

- 非线性元件特性可用光滑函数或 PWL 曲线合理表示
- 良好的初值可用（通常来自上一时间步解）
- 雅可比矩阵在迭代过程中不发生剧烈变化
- 内存受限或矩阵规模大到直接法不可行

### 失效模式

| 失效场景 | 原因 | 后果 |
|----------|------|------|
| PWL 边界附近来回跳变 | 标准 NR 在折点处雅可比突變 | 迭代无限循环（不收敛） |
| 初值远离解 | 牛顿步跨越物理可行域 | 发散或收敛到非物理解 |
| 预处理矩阵过旧 | 开关状态变化后未更新 | Krylov 收敛缓慢或停滞 |
| 强耦合接口单残差检查 | 只检查电压/电流残差 | 遗漏功率或能量误差 |
| 实时仿真中迭代截断 | 超限后强行使用未收敛解 | 精度损失或数值振荡 |

### 关键约束

- Noda & Kikuma (2011) 的三级策略假定非线性特性可用 PWL 表示——对光滑强非线性模型需重新验证
- 双轴 NR 的正则化因子 $\alpha$ 需针对具体系统调参
- Katzenelson 算法随区域数量增加计算代价急剧上升

## 6. 应用案例

### 案例 1：PWL 非线性电路的递进迭代策略（Noda & Kikuma 2011）

场景：10 kV 配电网中含铁芯饱和变压器和 MOA 避雷器。标准 NR 在故障后 3 个周期出现振荡发散（收敛率仅 82%）。三级递进策略（标准 NR $	o$ 双轴 NR $	o$ Katzenelson）实现 100% 收敛率。标准 NR 承担 > 95% 求解任务，双轴 NR 调用率 ~4.5%，Katzenelson 调用率 < 0.5%。相比单一 Katzenelson 算法，计算耗时降低 85%--90%。

### 案例 2：FPGA 实时非线性求解（Chen & Dinavahi 2011）

场景：避雷器暂态（CNR）和变压器铁磁谐振（PNR）。CNR 平均 3 次迭代收敛，5 $\mu$s 步长下执行时间 4.91 $\mu$s。PNR 免雅可比，执行时间降至 2.89 $\mu$s（3 $\mu$s 步长）。50 $\mu$s 步长下可支持至少 60 个非线性元件实时迭代。

### 案例 3：大规模系统的预处理 Krylov 方法

场景：节点数 > 10⁴ 的 EMT 网络。直接法因内存 $O(n^2)$ 不可行。ILU 预处理 GMRES 可在 $O(n)$ 内存下求解，但收敛性依赖矩阵性质，预处理构造本身也有 $O(n^{3/2})$ 代价。

## 7. 延伸阅读

- [[newton-raphson-method]]：牛顿法的 EMT 专用页面
- [[sparse-matrix-solver]]：直接法（LU分解），迭代法的替代选择
- [[nodal-analysis]]：节点方程作为迭代求解的线性化子问题
- [[compensation-method]]：将非线性分离后用迭代法求解端口方程
- [[stiff-system-handling]]：刚性系统的步长和稳定性问题
- [[real-time-simulation]]：硬实时中迭代次数约束的工程处理
- [[numerical-integration]]：隐式积分形成的代数方程结构

## 来源论文

| 论文 | 年份 |
|------|------|
| [[modelica-based-simulation-of-electromagnetic-transients-using-dynao-current-stat|Modelica-based simulation of electromagnetic transients usin]] | 2021 |
| [[evaluation-of-time-domain-and-phasor-domain-methods-for-power-system-transients|Evaluation of time-domain and phasor-domain methods for powe]] | 2022 |
| [[modeling-of-inductive-constant-power-load-for-electromagnetic-transient-simulati-27&28|Modeling of inductive constant power load for electromagneti]] | 2025 |
