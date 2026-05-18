---
title: "数值积分误差 (Numerical Integration Error)"
type: method
tags: [numerical-integration, error-analysis, stability, truncation-error, round-off-error, backward-euler, trapezoidal-rule, gear-method, bdf, dirk]
created: "2026-05-02"
updated: "2026-05-18"
---

# 数值积分误差 (Numerical Integration Error)

## 定义

数值积分误差是 EMT 仿真中由时间离散化、非线性迭代、事件处理、浮点舍入和模型近似共同产生的误差综合体。在固定步长 $\Delta t$ 下，积分器将连续微分方程 $\dot{x}=f(x,t)$ 映射为离散的差分方程，每一步产生的误差向下一步传播形成全局累积误差。

对于 $p$ 阶方法，局部截断误差（单步）和全局累积误差（多步传播）满足经典阶数关系：

$$e_{\text{local}} = O(\Delta t^{p+1}), \quad e_{\text{global}} = O(\Delta t^p)$$

该阶数关系默认解足够光滑；在开关动作、故障插入、保护跳闸和控制限幅附近，光滑性假设失效，实际误差由事件处理机制主导，可能超出上述标度律。

数值积分误差**不等同于"步长太大"**单一因素：同一步长下，不同积分器的稳定函数 $R(z)$、数值阻尼特性、事件定位精度和历史项更新方式都会改变结果。这些误差在谐振频率附近可能被品质因数 $Q$ 放大——Carbone 等 (2002) 的研究表明，即使单电感、单电容的阻抗误差较小（<5%），在谐振点处等效阻抗的表观误差可达 $\sim 100\%$。

## EMT 中的角色

EMT 仿真的核心任务是在时域逐步求解微分-代数方程组 (DAE)：

$$C(x,t)\dot{x} + K(x,t)x + f(x,t) = 0$$

其中 $x$ 为节点电压和支路电流等 MNA 未知量，$C$ 承载储能元件贡献，$K$ 和 $f$ 承载网络连接、导纳和激励。数值积分误差直接影响：
- **波形精度**：基频幅值/相位偏差、高频暂态衰减或振荡
- **谐振特性**：谐振频率偏移、等效阻抗幅值/相位畸变
- **事件判断**：开关动作时刻误判、保护误动或拒动
- **稳态收敛**：长期仿真中的能量/功率漂移

## 核心机制

### 1. 截断误差 (Truncation Error)

截断误差来自用离散近似替代连续积分。对测试方程 $\dot{x}=\lambda x$，积分器的稳定函数 $R(z)$（$z=\lambda\Delta t$）替代真实解 $e^z$：

$$x_{n+1} = R(z)\, x_n$$

真实映射：$R_{\text{true}}(z) = e^z$

各类积分器的 $R(z)$ 如下：

| 积分器 | 稳定函数 $R(z)$ | 阶数 | 稳定域 |
|--------|-----------------|------|--------|
| [[backward-euler]] | $1/(1-z)$ | 1 | L 稳定（强阻尼） |
| [[trapezoidal-rule]] | $(1+z/2)/(1-z/2)$ | 2 | A 稳定（非 L） |
| [[gear-method]] (BDF-$k$) | 多项式比值 | 1~6 | 随阶数变化 |
| DIRK 类 | Butcher 矩阵决定 | 2~3 | 可设计 L 稳定 |

对梯形法，表观感抗 $X_{L}^{\text{APP}}$ 与真实感抗 $X_L$ 的复数相对误差为（Carbone 2002）：

$$\varepsilon_{X_L}(\omega) = \frac{X_L^{\text{APP}} - X_L}{X_L} = \frac{j\omega\Delta t / 2}{1 + j\omega\Delta t / 2}$$

在固定步长 $\Delta t$ 下，误差随频率增加而增加；在固定频率下，误差随步长减小而降低。在典型 $\Delta t = 50\,\mu\text{s}$ 下，频率高于 5000 Hz 时误差显著。电容阻抗误差类似。

对串联 RLC 谐振电路（共振角频率 $\omega_0 = 1/\sqrt{LC}$，品质因数 $Q = R^{-1}\sqrt{L/C}$），表观阻抗的复数相对误差为（Carbone 2002）：

$$\varepsilon_Z(\omega) = jQ\left[\frac{\omega^2/\omega_0^2 - 1}{\omega/\omega_0} - \frac{j(\omega/\omega_0)}{1+j\omega/\omega_0}\right]$$

在谐振频率 $\omega_0$ 附近，即使单元件误差较小（~5%），合成阻抗误差可被放大至接近 $Q$ 倍——**谐振放大了数值积分误差**。

### 2. 稳定性误差 (Stability Error)

稳定性误差与连续系统模态 $\lambda$ 和步长 $\Delta t$ 的组合 $z=\lambda\Delta t$ 有关。若 $R(z)$ 的幅值或相位与真实 $e^z$ 偏差较大，即使仿真不发散，也会出现：

- **幅值衰减**：真实能量被阻尼（[[backward-euler]] 的 L 稳定性会强烈衰减高频刚性模态）
- **相位偏移**：波形时移或振荡相位误差（[[trapezoidal-rule]] 的刚性极限趋向 $z=-1$，高频误差以交替形式保留）
- **虚假振荡**：物理上不存在的数值振荡（梯形法在开关不连续后尤为明显）

对测试方程 $\dot{x}=\lambda x$，$|R(z)|$ 与 $|e^{\text{Re}(z)}|$ 的比值定义了幅值稳定性误差，相位差 $\arg R(z) - \text{Im}(z)$ 定义了相位误差。

### 3. 数值阻尼误差 (Numerical Damping Error)

[[backward-euler]] 的 L 稳定性会强烈衰减高频刚性模态——这有利于抑制非物理振荡，但也可能衰减真实高频暂态。

[[trapezoidal-rule]] 的刚性极限趋向 $-1$（$z\to\infty$ 时 $R(z)\to -1$），高频误差以交替符号保留而非耗散。

两者都不是"无误差"，只是误差形态不同：

| 积分器 | 高频模态行为 | 误差类型 |
|--------|------------|---------|
| [[backward-euler]] | $|R(z)|\to 0$，强衰减 | 幅值过度衰减 |
| [[trapezoidal-rule]] | $|R(z)|\to 1$，交替保留 | 相位振荡 |
| BDF-2 | 中等阻尼 | 介于二者之间 |

### 4. 事件误差 (Event Error)

EMT 中的开关、二极管换相、故障插入、保护动作和控制限幅常发生在固定步长网格之间。事件处理引入了四类额外误差（Zhong et al. 稳定评估研究）：

**4.1 事件时间偏差**
若真实事件时刻 $t^*$ 被映射到网格点 $t_n$（$t_n < t^* < t_{n+1}$），则事件被推迟 $\delta t = t^* - t_n$，产生时间偏移误差。

**4.2 状态不连续处理误差**
事件前后电路拓扑切换，电感电流或电容电压可能发生突变。梯形法历史电流源在突变后若不正确使用 $v_L(t_+)$，会导致储能元件历史源与新拓扑不一致。

**4.3 拓扑切换暂态**
储能元件（电感/电容）在换路时需要重新初始化等值电路和历史项。多器件瞬时联动（如半桥子模块同时关断）若被错误拆分，会引入附加暂态。

**4.4 插值与 CDA 的稳定性**
工程软件常用临界阻尼调整 (CDA)：检测到突变后临时改用 [[backward-euler]]。Zhong 等人的研究表明，若原切换系统在所有开关状态下严格无源，则线性插值和 CDA 可保证扩展切换系统的数值稳定性（CQLF 公共二次李雅普诺夫函数证明）。

量化边界：事件时间偏差 $\delta t \leq \Delta t$ 时，误差上限约为 $e_{\text{event}} \leq M\cdot\delta t$（$M$ 为状态导数上界）。

### 5. 迭代与舍入误差 (Iteration & Round-off Error)

隐式积分需要解线性或非线性方程组。非线性迭代残差、雅可比近似、线性求解器容差、矩阵条件数和浮点舍入都会影响结果。对大型稀疏网络，求解器误差还会随分区策略、并行通信和预条件策略改变。

关键来源：
- 非线性迭代残差 $\Vert R(x^k) \Vert$ 与收敛判据 $\varepsilon_{\text{tol}}$
- 雅可比矩阵近似精度（冻结 vs 更新频率）
- 矩阵条件数 $\kappa(A)$ 对求解精度的影响
- 浮点舍入 $\varepsilon_{\text{mach}} \approx 2.2\times10^{-16}$（双精度）

## EMT 建模方法

### 方法 1：后向欧拉法 (Backward Euler)

对一阶常微分方程 $\dot{x} = f(x)$，后向欧拉离散为：

$$x_{n+1} = x_n + \Delta t\, f(x_{n+1})$$

等效于求解隐式方程 $(I - \Delta t J)x_{n+1} = x_n$，其中 $J = \partial f/\partial x$。

**稳定函数**：

$$R(z) = \frac{1}{1 - z}$$

**特点**：L 稳定（一阶）；对高频刚性模态（$|z|\to\infty$）有 $|R(z)|\to 0$ 强衰减。

**EMT 中的应用**：
- 等值导纳：$G_{\text{eq}} = C/\Delta t$（电容）或 $G_{\text{eq}} = \Delta t/L$（电感）
- 历史电流源：$I_{\text{hist}} = G_{\text{eq}}\cdot x_n$
- 优势：换路时电感电流/电容电压突变后无数值振荡
- 劣势：一阶精度，低频波形有耗散误差

### 方法 2：梯形积分法 (Trapezoidal Rule)

梯形法离散为：

$$x_{n+1} = x_n + \frac{\Delta t}{2}\left[f(x_n) + f(x_{n+1})\right]$$

**稳定函数**：

$$R(z) = \frac{1 + z/2}{1 - z/2}$$

**特点**：二阶、A 稳定；但非 L 稳定——$|R(z)|\to 1$（$z\to\infty$），高频模态不衰减。

**EMT 中的应用**：
- 伴随电导：$G = (2C)/\Delta t$ 或 $G = (\Delta t)/(2L)$
- 历史源：$I_{\text{hist}} = G\cdot x_n + (\Delta t/2)f(x_n)$
- 优势：二阶精度、相位准确
- 劣势：开关不连续后产生持续数值振荡，需 CDA 或插值补救

### 方法 3：BDF 方法族 (Backward Differentiation Formulas)

$k$ 阶 BDF 近似：

$$\dot{x}_{n+1} \approx -\frac{1}{h}\sum_{i=0}^{k} \alpha_i x_{n+1-i}$$

代入 DAE 得当前未知 $x_{n+1}$ 进入左端矩阵 $(- \alpha_0/h C_{n+1} + K_{n+1})$，历史项进入右端向量。历史项只进入右端，**实现上不必重写 MNA 元件 stamps**。

| 阶数 $k$ | 稳定函数特点 | 优势 | 劣势 |
|---------|------------|------|------|
| BDF-1 (= BE) | L 稳定 | 无振荡 | 一阶 |
| BDF-2 | A 稳定 | 二阶 | 多步历史 |
| BDF-3~6 | 稳定域变窄 | 高阶 | 事件处理复杂 |

BDF 族继承了后向欧拉的无振荡特性，并结合多步高阶精度（Zhong et al. 研究）。

### 方法 4：DIRK 方法 (Diagonally Implicit Runge-Kutta)

DIRK 类方法用 Butcher 矩阵描述。以 2S-DIRK 为例（两阶段单对角隐式）：

$$\begin{aligned}
k_1 &= f(x_n + a h k_1) \\
k_2 &= f(x_n + h(a k_1 + b k_2)) \\
x_{n+1} &= x_n + h(b_1 k_1 + b_2 k_2)
\end{aligned}$$

其中 $a = 1 - 1/\sqrt{2} \approx 0.2929$，第一阶段等价于一个后向欧拉步。

**关键优势**（基于 2S-DIRK 补充技术研究）：
- 形式上等价于两个顺序求解的后向欧拉阶段，无需耦合求解大系统
- 固有无持续振荡特性，不依赖"检测到突变再切换"的 CDA 逻辑
- 二阶精度

3S-DIRK（三阶段 DIRK）框架（变阶变步长研究）：

- 正常阶段：选用高阶分算法（如三阶）
- 故障/不连续阶段：切换至 L 稳定分算法，衰减高频数值模态
- 插值阶段：支持开关时刻对齐
- 变步长：通过协调 $\lambda$ 与 $h$ 保持元件等值导纳不变，减少矩阵重构

### 方法 5：移频 EMT 大步长积分 (Shift-Frequency EMT)

SFEMT 将实信号构造为解析信号 $x_a(t) = x(t) + jH[x(t)]$（$H$ 为 Hilbert 变换），再乘以 $e^{-j\omega_c t}$ 将基频搬移至零频附近，用大步长求解解析包络。

积分器选用 3S-SDIRK（移频 EMT 研究）：三阶精度 + L 稳定性，在保持移频大步长优势的同时抑制梯形法的非物理振荡。

## 量化性能边界

### 截断误差量化

| 方法 | 局部误差阶 | 全局误差阶 | 典型误差系数 |
|------|-----------|-----------|-------------|
| [[backward-euler]] | $O(\Delta t^2)$ | $O(\Delta t)$ | $\approx \lambda\Delta t/2$ |
| [[trapezoidal-rule]] | $O(\Delta t^3)$ | $O(\Delta t^2)$ | $\approx (\lambda\Delta t)^2/12$ |
| BDF-2 | $O(\Delta t^3)$ | $O(\Delta t^2)$ | $\approx (\lambda\Delta t)^2/3$ |
| 3S-DIRK | $O(\Delta t^4)$ | $O(\Delta t^3)$ | 取决于 Butcher 系数 |

谐振电路中，Carbone 2002 的实测数据：$\Delta t = 50\,\mu\text{s}$，$f_0 = 2500$ Hz，$Q=10$ 时，等效阻抗误差在谐振点处约为 $100\%$（单元件误差仅 5%）。

### 稳定性误差量化

| 积分器 | $|R(j\omega\Delta t)|$ vs $|e^{j\omega\Delta t}|$ | 相位误差 |
|--------|----------------------------------------|---------|
| [[backward-euler]] | $|1/(1+j\omega\Delta t)| < 1$（幅值衰减） | $\arg R - \omega\Delta t < 0$（相位滞后） |
| [[trapezoidal-rule]] | $= 1$（无幅值误差） | $\arg R - \omega\Delta t$ 呈非线性 |
| BDF-2 | $\approx 1$（低频） | 轻微相位误差 |

### 数值阻尼量化

| 场景 | 后向欧拉 | 梯形法 | BDF-2 |
|------|---------|--------|-------|
| 高频模态 ($\omega\Delta t \gg 1$) | 强阻尼 (|R|→0) | 交替保留 | 中等阻尼 |
| 开关后振荡抑制 | 自动抑制 | 需 CDA/插值 | 自动抑制 |
| 精度损失 | 一阶 | 二阶 | 二阶 |

### 步长加密验证

对同一模型使用 $\Delta t$、$\Delta t/2$、$\Delta t/4$ 重复仿真，比较关键输出：

$$E_{\Delta t} = \frac{\|x_{\Delta t} - x_{\Delta t/2}\|}{\|x_{\Delta t/2}\|}$$

若误差按理论阶数 $p$ 收敛（$E_{\Delta t/2} \approx E_{\Delta t}/2^p$），说明平滑区间积分误差可控。

Richardson 外推误差估计：

$$e_{\text{est}} \approx \frac{x_{\Delta t/2} - x_{\Delta t}}{2^p - 1}$$

## 关键技术挑战

### 挑战 1：谐振频率处的误差放大

单元件误差被谐振结构放大。Carbone 2002 的核心发现：对串联 RLC，误差与 $Q$ 成正比（$Q = R^{-1}\sqrt{L/C}$）。在谐振点附近，即使是 $0.1\,\mu\text{s}$ 级的数值积分误差，也可能被放大为 $10\%$ 以上的阻抗偏差。

**应对**：在谐振分析前，先用步长加密验证 $e_{\Delta t}/e_{\Delta t/2}$ 收敛比；或采用频域阻抗扫描评估表观阻抗偏差。

### 挑战 2：开关事件与数值振荡的耦合

梯形法在开关不连续后产生持续数值振荡，是 EMT 领域最常见的工程问题。常见原因：
- 突变前后状态不连续，历史电流源计算未使用 $v_L(t_+)$
- 多个器件瞬时联动被错误拆分
- 控制限幅触发的隐式不连续

**应对**：CDA（检测到突变后临时切换到后向欧拉）+ 线性插值定位真实事件时刻（Zhong et al. CQLF 稳定性证明）。或使用 2S-DIRK/3S-DIRK 从积分格式本身避免振荡。

### 挑战 3：高频 EMT 与基频稳态的多尺度误差控制

高频电力电子开关（$\mu$s 级）与基频稳态（$50/60$ Hz）共仿时，两类误差同时存在：
- 高频步长下的截断误差（$O(\Delta t^p)$）
- 基频波形中的长期漂移（$O(T)$ 累积）

**应对**：多速率方法（[[multirate-method]]）或 SFEMT 大步长方法分别处理不同频带。

### 挑战 4：数值阻尼与物理阻尼的区分

强阻尼积分器（如 [[backward-euler]]）可能同时衰减真实高频物理暂态和非物理数值模态，导致无法判断波形偏差是来自模型还是积分器。

**应对**：建立已知物理阻尼的系统（如 RLC 串联）基准，用不同积分器对比结果，分离数值阻尼与物理阻尼。

### 挑战 5：大规模系统的误差累积与分区接口误差

大型 EMT 网络常分区并行仿真，分区接口的插值误差、通信延迟和本地积分器误差需要联合验证。

**应对**：分区边界采用插值精度 $\geq 2$ 的方法；接口处用残差检查（KCL/KVL）辅助发现误差。

## 误差估计与验证方法

### 步长加密法

对同一模型使用 $\Delta t$、$\Delta t/2$、$\Delta t/4$ 重复仿真，比较关键输出：

$$E_{\Delta t} = \|x_{\Delta t} - x_{\Delta t/2}\|$$

若 $E_{\Delta t/2} / E_{\Delta t} \approx 2^{-p}$，则误差以 $p$ 阶收敛。

### Richardson 外推

$$e_{\text{est}} \approx \frac{x_{\Delta t/2} - x_{\Delta t}}{2^p - 1}$$

要求处于渐近收敛区间（光滑解区域），在开关事件附近不适用。

### 频域阻抗验证

对目标系统施加小扰动电流，扫描端口阻抗：

$$Z_{\text{EMT}}(\omega) = \frac{V(\omega)}{I(\omega)}$$

与解析阻抗或参考仿真对比，评估数值积分对阻抗特性的影响（Carbone 2002 方法）。

### 残差与物理约束检查

隐式积分后应检查：
- 非线性方程残差 $\Vert R(x^k) \Vert \leq \varepsilon_{\text{tol}}$
- KCL/KVL 满足度
- 能量、功率或电荷平衡漂移（长期仿真）
- 状态是否越物理限制或控制限幅

## 适用边界与选择指南

| 场景 | 推荐积分器 | 理由 |
|------|----------|------|
| 纯电阻网络，无开关 | 梯形法（快速、二阶） | 无刚性问题 |
| 含电力电子开关，有突变 | 2S-DIRK 或 3S-DIRK | 固有无振荡 |
| 高比例新能源，需大步长 | SFEMT + 3S-SDIRK | 大步长 + L 稳定 |
| 刚性系统，高频模态主导 | 后向欧拉或 BDF-2 | L 稳定强阻尼 |
| 谐振分析，需准确阻抗 | BDF-2+步长加密 | 低频精度 + 高频阻尼 |
| 实时仿真，计算受限 | 后向欧拉（一阶最快） | 单隐式方程，每步计算最少 |
| 多速率仿真 | DIRK 类 | 变阶变步长接口不变 |

**选择决策树**：

1. 有无开关/不连续？→ **是** → 选 DIRK 类或 CDA+梯形法
2. 是否实时仿真？→ **是** → 选后向欧拉（最快）或 2S-DIRK
3. 是否谐振分析？→ **是** → 选 BDF-2 + 步长加密验证
4. 是否大步长包络仿真？→ **是** → 选 SFEMT + 3S-SDIRK
5. 以上均不满足 → 梯形法（二阶精度，计算量适中）

## 与相关页面的关系

- [[numerical-integration]]：数值积分方法总入口
- [[backward-euler]]：一阶 L 稳定方法及阻尼误差
- [[trapezoidal-rule]]：二阶 A 稳定方法及事件振荡风险
- [[gear-method]]：多步 BDF/Gear 方法及历史误差
- [[numerical-damping-optimization]]：数值阻尼优化方法对比
- [[numerical-oscillation-suppression]]：数值振荡抑制技术
- [[large-timestep-simulation]]：大步长场景下误差和模型简化边界
- [[numerical-stability]]：稳定性概念的主题入口
- [[interpolation-method]]：事件插值定位方法
- [[vector-fitting]]：频域拟合与数值积分误差的关联（频变线路）
- [[fdne-model]]：频率相关网络等值中的数值积分误差

## 来源论文

- [[analysis-and-estimation-of-truncation-errors-in-modeling-complex-resonant-circui-fix]]：Carbone 等 (2002)，梯形积分在复杂 RLC 谐振电路中的截断误差分析，推导了单元件/串并联 RLC 的解析误差指标和表观角频率数值过程
- [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi]]：移频 EMT + 3S-SDIRK 大步长方法，三阶精度 + L 稳定性，抑制梯形法振荡
- [[improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an]]：Kocar 等 (2010)，频域 PFE 参数与时域离散卷积误差的联系，留数/极点比值约束提升数值稳定性
- [[stability-evaluation-of-interpolation-extrapolation-and-numerical-oscillation-da]]：Zhong 等，插值/CDA 的 CQLF 稳定性证明，若原切换系统无源则插值和 CDA 保证稳定仿真
- [[适用于电磁暂态仿真的变阶变步长3s-dirk算法]]：3S-DIRK 框架，正常阶数/故障 L 稳定/插值/变步长四模式切换，保持导纳矩阵接口不变
- [[numerical-integration-2s-dirk-iet-gtd]]：架空多导体线路的 2S-DIRK 频变建模，瞬态电阻矩阵卷积替代传播函数整体拟合
- [[supplementary-techniques-for-2s-dirk-based-emt-simulations]]：2S-DIRK 面向 EMT 的补充技术：源阶跃处理、开关协调、避免阶段间状态不连续
- [[simulation-of-electromagnetic-transients-with-a-family-of-implicit-multi-step-os]]：BDF 1~5 阶隐式多步方法族用于 EMT，后向欧拉无振荡特性与多步高阶精度结合