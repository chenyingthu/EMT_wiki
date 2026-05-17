---
title: "特征值分析 (Eigenvalue Analysis)"
type: method
tags: [eigenvalue, linear-algebra, stability, numerical-methods, modal, small-signal]
created: "2026-05-02"
updated: "2026-05-18"
---

# 特征值分析 (Eigenvalue Analysis)

## 定义与边界

特征值分析是求解线性算子或矩阵谱结构的数学操作。对标准特征值问题

$$\mathbf{A}\mathbf{v} = \lambda\mathbf{v},$$

$\lambda$ 为特征值，$\mathbf{v}$ 为右特征向量。在线性化动态系统中，特征值用于解释局部增长、衰减、振荡频率和时间尺度。

本页覆盖特征值作为**数学和数值方法**的角色——不是[[small-signal-stability]]本身，也不等同于完整的[[modal-analysis]]。只有当矩阵来源、运行点、坐标系和线性化假设明确时，特征值才可被解释为 EMT 或电力系统动态模态。

**三种特征值类型的区分**：

| 类型 | 来源 | 稳定判据 |
|------|------|----------|
| 连续特征值 $\lambda$ | 连续时间状态矩阵 $\mathbf{A}$ | $\Re(\lambda) < 0$ |
| 离散特征值 $\mu$ | 离散状态矩阵 $\mathbf{A}_d$ 或周期状态转移矩阵 $\mathbf{\Phi}(T)$ | $|\mu| < 1$ |
| Floquet 乘子 $\mu_i$ | 线性时周期 (LTP) 系统单值矩阵 | $|\mu_i| < 1$ |

## EMT 中的作用

EMT 相关研究中，特征值分析常出现在四类位置：

1. **连续时间状态矩阵求谱**：对线性化后的连续状态矩阵 $\mathbf{A}$ 求谱，判断运行点附近的小扰动趋势。
2. **离散状态转移矩阵求谱**：对离散状态矩阵 $\mathbf{A}_d$ 或周期状态转移矩阵 $\mathbf{\Phi}(T)$ 求谱，分析采样或周期开关系统的小信号稳定性。
3. **矩阵束广义特征值**：对 DAE 线性化后的矩阵束 $(\mathbf{A}, \mathbf{B})$ 使用[[generalized-eigenvalue-method]]。
4. **频域阻抗/导纳矩阵谱**：对随频率变化的阻抗/导纳矩阵求特征值，辅助 MIMO 小信号稳定判断。

这些对象都叫"特征值"，但稳定判据不同。连续时间看实部，离散时间看单位圆内外，LTP 系统看 Floquet 乘子模值，频域矩阵看谱半径或 Nyquist 判据。

## 核心机制

### 连续时间系统

若状态空间模型为

$$\Delta\dot{\mathbf{x}} = \mathbf{A}\Delta\mathbf{x},$$

且 $\mathbf{A}$ 可对角化，则

$$\mathbf{A} = \mathbf{V}\mathbf{\Lambda}\mathbf{V}^{-1}, \quad \Delta\mathbf{x}(t) = \sum_i c_i\mathbf{v}_i e^{\lambda_i t}.$$

复特征值 $\lambda_i = \sigma_i + j\omega_i$ 中，$\sigma_i$ 控制指数增长或衰减，$\omega_i$ 控制振荡角频率。阻尼比

$$\zeta_i = -\frac{\sigma_i}{\sqrt{\sigma_i^2 + \omega_i^2}}.$$

### 离散时间系统

若模型为离散时间

$$\Delta\mathbf{x}_{k+1} = \mathbf{A}_d\Delta\mathbf{x}_k,$$

则模态响应为 $z_i[k] = \mu_i^k z_i[0]$。局部稳定要求 $|\mu_i| < 1$。离散与连续特征值通过**双线性 (Tustin) 变换**连接：

$$\lambda_i = \frac{2}{T_s}\frac{\mu_i - 1}{\mu_i + 1}, \quad \mu_i = \frac{1 + \frac{T_s}{2}\lambda_i}{1 - \frac{T_s}{2}\lambda_i},$$

其中 $T_s$ 为采样周期。注意复对数分支可能带来频率混叠问题。

### 线性时周期 (LTP) 系统

EMT 模型在同步频率附近呈周期时变特性，状态方程满足 $\dot{\mathbf{x}}(t) = \mathbf{A}(t)\mathbf{x}(t)$，$\mathbf{A}(t+T)=\mathbf{A}(t)$。Floquet 理论将周期系统模态信息压缩到**单值矩阵**（状态转移矩阵）：

$$\mathbf{\Phi}(T) = \mathcal{T}\exp\!\left(\int_0^T \mathbf{A}(\tau)d\tau\right),$$

其中 $\mathcal{T}\exp$ 为时序积分。$\mathbf{\Phi}(T)$ 的特征值为 Floquet 乘子 $\mu_i$，Floquet 指数为

$$\lambda_i = \frac{1}{T}\ln(\mu_i).$$

Floquet 乘子模值 $|\mu_i| < 1$ 等价于 $\Re(\lambda_i) < 0$，均表征系统小信号稳定。

### EMT 伴随电路的自动化特征值提取

Chindu 和 Kulkarni (2023) 提出直接复用 EMT 程序内部伴随电路信息构建 LTI 采样数据模型用于特征值分析。核心思想：

- 伴随电路节点导纳矩阵 $\mathbf{G}$ 由电阻导纳、电容等效导纳和电感等效导纳组成：
  $$\mathbf{G} = \mathbf{Y}_R + \mathbf{A}_C\!\left(\frac{2C}{h}\right)\!\mathbf{A}_C^T + \mathbf{A}_L\!\left(\frac{h}{2L}\right)^{-1}\!\mathbf{A}_L^T;$$
- 状态转移矩阵 $\mathbf{A}$ 可直接利用 EMT 中已计算的 $\mathbf{G}$ 的 LU 分解因子高效求解：
  $$\mathbf{A} = \mathbf{I} - \begin{bmatrix}\frac{h}{2}\mathbf{L}^{-1}\mathbf{A}_L^T \\ -\frac{4}{h}\mathbf{C}\mathbf{A}_C^T\end{bmatrix}\mathbf{G}^{-1}[\mathbf{A}_L \;\mathbf{A}_C];$$
- 周期状态转移矩阵 $\mathbf{\Phi}_T = \mathbf{A}_{N-1}\mathbf{A}_{N-2}\cdots\mathbf{A}_0$（$N$ 步）的特征值给出 Floquet 乘子。

**伪特征值剔除**：离散模型中 $\mu = -1$（对应 $\Omega = -1$ 在双线性变换前）的特征值数量严格等于纯电感割集与纯电容回路总数，可作为自动剔除数值伪模态的判据。系统小信号稳定的充要条件为所有**物理**特征值满足 $|\mu_i| < 1$。

## 数值算法

| 算法 | 适用对象 | 输出 | 注意事项 |
|------|----------|------|----------|
| QR / Schur | 中小规模稠密标准特征值问题 | 全部或大部分特征值 | 数值实现通常通过 Schur 形式而非显式求 $\mathbf{V}^{-1}$ |
| QZ / 广义 Schur | 矩阵束 $(\mathbf{A}, \mathbf{B})$ | 广义特征值 | 适合 [[generalized-eigenvalue-method]]；避免显式 $\mathbf{B}^{-1}\mathbf{A}$ |
| Arnoldi / Krylov | 大规模稀疏非对称矩阵 | 部分 Ritz 值和向量 | 需选择目标谱区、重启策略和残差容差 |
| Shift-invert | 靠近指定频率或虚轴的特征值 | 目标附近特征值 | 每步需要求解线性系统；矩阵病态影响精度 |
| 幂法 / 反幂法 | 简单主导特征值或教学场景 | 单个或少量特征值 | 对非正规矩阵和聚集特征值不稳健 |
| 分块 Arnoldi | 大规模多模态分析 | 多个邻近特征值簇 | 可并行计算，适合 EMT 大规模系统 |

Arnoldi 方法尤其适用于电力电子系统的**宽频带模态分析**——从低频机电振荡（0.1–2 Hz）到高频控制相互作用（数十至数百 Hz）可在同一次特征值扫描中捕获。

## 解释要点

### 特征值

特征值给出线性模型的自然响应时间尺度。实部接近零或离散特征值接近单位圆的模态通常更需要关注，但"接近"的工程含义必须由具体准则或研究目标定义。

### 右特征向量

右特征向量描述模态在状态变量上的相对幅值和相位，是 [[modal-analysis]] 中模态形状的基础。其数值受归一化和状态单位影响，不能单独当作能量贡献。

### 左特征向量

左特征向量描述扰动投影到模态坐标的权重。左、右特征向量共同用于参与因子、留数和参数灵敏度分析。

### Floquet 参与因子

Sajjadi 等 (2026) 将 Floquet 理论参与因子用于 EMT 模型边界自动划分。对 LTP 系统：

$$P_{ki}^{(h)} = \frac{\partial \lambda_i}{\partial a_{kk}^{(h)}},$$

其中 $h$ 为谐波阶数。传统相量域 (LTI) 参与因子仅为 Floquet 参与因子的零次谐波 ($h=0$) 特例，无法反映高次谐波动态交互。谐波筛选准则可剔除 $>85\%$ 的冗余状态变量，同时保证目标 SSO 模式特征值误差分别 $<0.01$ (实部) 和 $<0.5$ rad/s (虚部)。

### 残差与可信度

特征值结果应至少检查残差：

$$r_i = \|\mathbf{A}\mathbf{v}_i - \lambda_i\mathbf{v}_i\|.$$

对于广义问题，检查 $\|\mathbf{A}\mathbf{v}_i - \lambda_i\mathbf{B}\mathbf{v}_i\|$。若矩阵病态、特征值重合或系统非正规，特征向量和参与因子可能比特征值本身更敏感。

## EMT 建模方法

### 方法 1：EMT 伴随电路 → 离散 LTI 模型 → 特征值

直接复用 EMT 程序的伴随电路导纳矩阵、历史项电流源和 LU 分解因子，将储能元件的历史项电流源定义为状态变量，构建离散状态转移矩阵后求特征值。

- **核心公式**：$\mathbf{A}_d = \mathbf{I} - \mathbf{H}\mathbf{G}^{-1}\mathbf{C}$，其中 $\mathbf{H}$ 包含离散化后的电感、电容矩阵
- **特点**：自动化程度高，无需手工拓扑分析；额外计算开销趋近于零
- **适用场景**：含详细开关模型的电力电子变换器、PLL 多环控制系统
- **失效场景**：大扰动暂态、强非线性饱和、模式切换

### 方法 2：Modelica 自动线性化 → 状态矩阵 → 特征值扫描

使用 Modelica 编译器将分层物理模型自动展平为 DAE，在任意运行点处自动计算雅可比矩阵并提取状态空间矩阵 $(\mathbf{A}, \mathbf{B}, \mathbf{C}, \mathbf{D})$，随后对 $\mathbf{A}$ 进行特征值分解。

- **核心公式**：$F(t, \dot{x}, x, y, z) = 0 \Rightarrow \delta\dot{x} = \mathbf{A}\delta x + \mathbf{B}\delta u$
- **特点**：拓扑变化时自动重新线性化，保留测量滤波器等辅助环节；无需手工推导状态方程
- **适用场景**：光伏场站、风电场等多变换器并网系统；多运行点扫描
- **失效场景**：大扰动、故障穿越强非线性、实时控制器代码级延迟

### 方法 3：dq 坐标阻抗 → 特征值轨迹

在 dq 坐标系下建立子系统导纳/阻抗矩阵，通过频率扫描获得阻抗曲线后，利用 Nyquist 判据或系统矩阵特征值判断 MIMO 小信号稳定。

- **核心公式**：$\mathbf{Y}_{dq}(j\omega) = [\Delta\mathbf{i}][\Delta\mathbf{v}]^{-1}$，随后对 $\mathbf{Y}\mathbf{Z}$ 矩阵串联组合求特征值
- **特点**：适合黑盒 EMT 模型；可处理多端 AC/DC 耦合系统
- **适用场景**：VSC-HVDC、MMC-HVDC 多端系统；新能源场站宽频带稳定性筛查
- **失效场景**：不对称故障、强谐波背景、实时仿真步长限制

### 方法 4：Floquet 理论 → 周期系统特征值

将 EMT 模型在周期稳态轨迹附近视为 LTP 系统，用单周期数据构造单值矩阵，求 Floquet 乘子和参与因子。

- **核心公式**：$\mathbf{\Phi}(T) = \mathcal{T}\exp\!\left(\int_0^T \mathbf{A}(\tau)d\tau\right)$，$\lambda_i = \frac{1}{T}\ln(\mu_i)$
- **特点**：捕获周期时变耦合效应；通过 Floquet 参与因子识别关键元件
- **适用场景**：IBB 电网 SSO 分析；EMT 模型边界自动划分
- **失效场景**：非周期强暂态、保护动作频繁改变拓扑

### 方法 5：复转矩系数法 → 特征值阻尼分析

基于复转矩系数法推导注入电流与轴系电磁阻尼转矩的解析映射关系，通过特征值分析观察阻尼控制器投入前后的扭振模态变化。

- **核心公式**：$f_{mi}(s)$ 为模态带通滤波器传递函数；$\Delta\tau$ 为开关时刻扰动修正量
- **特点**：将电磁阻尼与系统特征值直接关联；支持多模态 SSR 抑制
- **适用场景**：串补输电系统次同步谐振 (SSR)；发电机端附加阻尼控制设计
- **失效场景**：多机群内相互作用、非线性饱和轴系

## 关键技术挑战

### 挑战 1：数值伪模态识别

EMT 数值离散化（梯形积分等）会在状态转移矩阵中引入与物理动态无关的数值伪模态。这些伪模态（$\mu = -1$）来源于纯电感割集和纯电容回路，其数量可用于自动剔除。

**判据**：离散模型中 $\Omega = -1$ 的特征值数量等于电路中纯电感割集数 + 纯电容回路数。

### 挑战 2：周期系统模态与 LTI 模态的区分

LTP 系统的 Floquet 乘子与连续时间特征值不是一一对应。高次谐波 ($h \neq 0$) 参与因子可能反映网络与电力电子控制在周期轨迹上的动态耦合，这些信息在传统相量域 LTI 分析中缺失。

**应对**：使用 Floquet 参与因子进行谐波筛选；保留至 5–13 次谐波以覆盖目标 SSO 频段。

### 挑战 3：大规模稀疏矩阵的部分特征值求解

大规模 EMT 系统状态矩阵可达数万维， Arnoldi 方法需要选择合适的**目标谱区**（实部范围或频率区间）。若目标谱区选择不当，可能漏掉关键模态或引入过多无用特征值。

**参数建议**：对于 SSO 分析，目标谱区设置为 5–100 Hz；对于次同步振荡，设置为 10–45 Hz。

### 挑战 4：EMT 与特征值分析的边界接口

EMT 模型边界外的网络如何等值以保留动态耦合，同时减少计算量，是大规模系统特征值分析的难点。等值方法包括多端口 Norton 等值和同步发电机戴维南等值。

**量化**：Norton 等值使边界外网络求解复杂度从 $O(N^3)$ 降至 $O(1)$。

### 挑战 5：IBR 黑盒模型的处理

IBR（逆变器型资源）通常只提供黑盒 EMT 模型，无法直接提取状态空间矩阵。

**应对**：使用 Z-Tool 等频域系统识别工具，通过小信号电压扰动和 FFT 响应提取多端导纳矩阵 $\mathbf{Y}(j\omega) = \Delta\mathbf{i}\cdot\Delta\mathbf{v}^{-1}$，再将其用于阻抗类稳定分析。

## 量化性能边界

| 方法 | 计算效率 | 精度 | 适用频率范围 |
|------|----------|------|--------------|
| EMT 伴随电路自动特征值 | 与 TDS 同量级（额外开销 $\approx 0$） | 特征值匹配误差 0%（双线性变换精确） | 全频段 |
| Modelica 自动线性化 | 拓扑变更自动重线性化，无需手工 | 保留输入滤波器等辅助环节，精度高 | 全频段 |
| dq 阻抗 + 特征值轨迹 | 需多次频率扫描，效率中等 | 精度取决于 EMT 步长和扰动幅度 | 宽频带 (0.1 Hz – 数 kHz) |
| Floquet 理论 + 参与因子 | 单周期数据，时间窗口缩短 $>99\%$ | SSO 模态频率误差 $<0.15\%$，阻尼误差 $<1.2\%$ | 次同步至超同步 |
| 复转矩系数法 | 特征值分析 + EMT 仿真协同 | 扭振频率锁定精度 $\pm 0.01$ Hz | 次同步 (10–45 Hz) |

**来源论文量化数据**：

- Chindu & Kulkarni (2023)：EMT 伴随电路特征值与理论解析值匹配误差 **0%**，额外计算开销趋近于零
- Sajjadi 等 (2026)：单周期 Floquet 分析使时间窗口缩短 **>99%**；谐波筛选剔除 **>85%** 冗余状态变量；关键动态指标误差 **<2%**
- Xie 等 (2013)：扭振模态频率锁定精度 **13.02 Hz、22.77 Hz、28.24 Hz**（$\pm 0.01$ Hz）；最优相位整定使最大电气阻尼系数提升约 **2.5 倍**
- Masoom 等 (2025)：Modelica 自动线性化支持任意运行点 $t_l$ 处的即时特征值提取，无需手工重写方程

## 适用边界与选择指南

| 场景 | 推荐方法 | 理由 |
|------|----------|------|
| 电力电子变换器详细小信号稳定性 | 方法 1（EMT 伴随电路） | 直接复用 EMT 内部数据，自动化程度最高 |
| 新能源场站多运行点扫描 | 方法 2（Modelica 自动线性化） | 拓扑变更自动重新线性化，无需手工推导 |
| 黑盒 IBR 多端系统阻抗分析 | 方法 3（dq 阻抗 + Z-Tool） | 无需内部模型，通过端口特性识别系统 |
| SSO 关键元件识别与 EMT 边界划分 | 方法 4（Floquet 参与因子） | 单周期数据，>99% 时间节省；捕捉周期耦合效应 |
| 串补系统 SSR 多模态阻尼控制 | 方法 5（复转矩系数法） | 将电磁阻尼与特征值直接关联，支持多模态设计 |
| 大规模系统初步筛查 | Arnoldi / Krylov | 部分特征值求解，避免全矩阵分解 |

**通用决策流程**：

1. 明确分析目标（SSO 筛查 / 控制参数整定 / EMT 边界划分 / 黑盒稳定性验证）
2. 判断矩阵类型（稠密 / 稀疏 / 广义 / 周期时变）
3. 选择目标谱区（低频 / 次同步 / 高频）
4. 确认是否有 EMT 内部数据可复用或需要黑盒识别
5. 验证：残差检查 → 伪模态剔除 → 阻尼比确认

## 失败模式

- 未说明矩阵来源时，特征值没有工程含义
- 把离散特征值、Floquet 乘子和连续特征值混用导致错误频率或阻尼解释
- 显式求逆 $\mathbf{A}^{-1}$ 或 $\mathbf{B}^{-1}\mathbf{A}$ 可能放大数值误差
- 对代数约束消元后的矩阵求谱时，应检查消元矩阵是否奇异或近奇异
- 参与因子受状态缩放影响，不能不加说明地比较不同模型
- 大扰动、保护动作、饱和和模式切换不由局部特征值直接覆盖
- Arnoldi 目标谱区选择不当可能漏掉关键模态
- IBR 黑盒模型无法进行解析特征值分析，需用频域识别替代

## 与相关页面的关系

- [[small-signal-stability]]：使用特征值判断局部扰动趋势
- [[small-signal-stability-analysis]]：把特征值求解放入完整分析流程
- [[modal-analysis]]：在特征值基础上解释特征向量、参与因子和灵敏度
- [[modal-decomposition]]：用特征值和特征向量展开时间响应
- [[generalized-eigenvalue-method]]：处理矩阵束和 DAE 相关谱问题
- [[dae-solvers]]：解释状态矩阵或矩阵束来自何种 DAE / 残差结构
- [[state-space-method]]：特征值分析的对象（状态矩阵）来自状态空间模型
- [[impedance-stability]]：频域阻抗矩阵的特征值用于 Nyquist 类 MIMO 稳定判据
- [[network-equivalent]]：EMT 边界外网络等值保留动态耦合，服务特征值分析的可扩展性
- [[model-order-reduction]]：降阶模型保留主导特征值，用于加速大规模系统分析
## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| [[an-automatable-approach-for-small-signal-stability-analysis-of-power-electronic-]] | 2023 | EMT 伴随电路自动提取 LTI 采样数据模型，双线性变换特征值匹配误差 0% |
| [[fast-investigation-of-control-interaction-risks-in-pv-parks-using-eigenvalue-ana]] | 2025 | Modelica 自动线性化 + 特征值扫描，多运行点控制交互风险快速定位 |
| [[damping-multimodal-subsynchronous-resonance-using-a-generator-terminal-subsynchr]] | 2013 | 复转矩系数法推导阻尼转矩，扭振模态频率锁定精度 $\pm 0.01$ Hz，阻尼提升 2.5 倍 |
| [[emt-model-boundary-determination-using-floquet-theory-based-participation-factor]] | 2026 | Floquet 参与因子划分 EMT 边界，单周期分析时间窗口缩短 >99% |
| [[z-tool-frequency-domain-characterization-of-emt-models-for-small-signal-stabilit]] | 2026 | EMT 频域系统识别，dq 导纳矩阵构建，多端 AC/DC 耦合表征 |