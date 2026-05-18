---
title: "小扰动线性化 (Small-Perturbation Linearization)"
type: method
tags: [linearization, small-signal, perturbation, jacobian, stability, eigenvalue, EMT, DAE]
created: "2026-05-02"
updated: "2026-05-19"
---

# 小扰动线性化 (Small-Perturbation Linearization)

## 定义与边界

小扰动线性化是在给定运行点附近对非线性微分方程、代数方程或离散步进映射做一阶泰勒近似的方法。它将"运行点附近的增量响应"写为线性模型，使 [[eigenvalue-analysis]]（特征值分析）、[[modal-analysis]]（模态分析）和控制设计工具可直接使用。线性化方程的精度直接受运行点选择、雅可比计算精度和系统非线性强度影响。

本页讨论方法本身——如何选运行点、如何构造雅可比矩阵 $\mathbf{A}$、如何处理 DAE 约束和周期切换系统。它不等同于 [[small-signal-stability-analysis]]（小信号稳定分析）概念页，也不保证故障、限幅、保护切换或大信号暂态中的行为预测能力。

## EMT 中的角色

EMT 模型通常包含电感/电容状态、节点电压、开关逻辑、PLL、采样延时和频率相关网络。小扰动线性化在 EMT 中的核心价值在于：

1. **提取局部状态空间模型**：从详细 EMT 模型生成 LTI sampled-data 小信号模型，用于特征值分析
2. **解释耦合机理**：量化换流器控制、弱网、频变网络与同步机之间的局部耦合强度
3. **加速参数扫描**：无需重新运行完整 EMT 仿真，即可通过线性模型分析参数变化对稳定性的影响
4. **自动化模型生成**：复用 EMT 程序的伴随电路信息（节点导纳矩阵、LU 分解因子、历史项电流源）自动构造线性模型

若 EMT 对象是周期切换系统（如 PWM 变流器），线性化对象不是单个连续时间矩阵，而是一个周期轨迹附近的离散状态转移矩阵 $\Phi_T$，此时需用 Floquet 理论处理。

## 核心形式

### 连续时间非线性系统

对非线性系统

$$
\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x}, \mathbf{u}), \quad \mathbf{y}=\mathbf{g}(\mathbf{x}, \mathbf{u}),
$$

在运行点 $(\mathbf{x}_0, \mathbf{u}_0)$ 附近令 $\Delta\mathbf{x}=\mathbf{x}-\mathbf{x}_0$，$Delta\mathbf{u}=\mathbf{u}-\mathbf{u}_0$，一阶近似为

$$
\Delta\dot{\mathbf{x}}=\mathbf{A}\Delta\mathbf{x}+\mathbf{B}\Delta\mathbf{u}, \quad \Delta\mathbf{y}=\mathbf{C}\Delta\mathbf{x}+\mathbf{D}\Delta\mathbf{u},
$$

其中雅可比矩阵为

$$
\mathbf{A}=\left.\frac{\partial\mathbf{f}}{\partial\mathbf{x}}\right|_0, \quad \mathbf{B}=\left.\frac{\partial\mathbf{f}}{\partial\mathbf{u}}\right|_0, \quad \mathbf{C}=\left.\frac{\partial\mathbf{g}}{\partial\mathbf{x}}\right|_0, \quad \mathbf{D}=\left.\frac{\partial\mathbf{g}}{\partial\mathbf{u}}\right|_0.
$$

### 微分代数方程（DAE）

对含代数约束的 DAE 系统

$$
\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x}, \mathbf{z}, \mathbf{u}), \quad \mathbf{0}=\mathbf{h}(\mathbf{x}, \mathbf{z}, \mathbf{u}),
$$

若 $\mathbf{h}_z$ 非奇异，可局部消去代数变量 $\mathbf{z}$：

$$
\Delta\dot{\mathbf{x}}=\left(\mathbf{f}_x-\mathbf{f}_z \mathbf{h}_z^{-1} \mathbf{h}_x\right)\Delta\mathbf{x}+\left(\mathbf{f}_u-\mathbf{f}_z \mathbf{h}_z^{-1} \mathbf{h}_u\right)\Delta\mathbf{u}.
$$

DAE 线性化的关键挑战在于代数雅可比 $\mathbf{h}_z$ 的奇异性——当网络出现电压骤降或故障时，$\mathbf{h}_z$ 可能接近奇异，导致线性化模型失效。

### 离散 EMT 步进器

对固定步长 $h$ 的 EMT 仿真，常写为离散状态转移形式：

$$
\Delta\mathbf{x}_{k+1}=\mathbf{A}_d \Delta\mathbf{x}_k+\mathbf{B}_d \Delta\mathbf{u}_k.
$$

其中 $\mathbf{A}_d$ 的特征值 $|\lambda_i|<1$ 是离散系统小扰动稳定的充要条件。连续时间特征值 $\lambda_c$ 与离散时间特征值 $\lambda_d$ 通过 **双线性变换** 关联：

$$
\lambda_c=\frac{2}{h} \cdot \frac{\lambda_d-1}{\lambda_d+1}.
$$

**注意**：连续时间特征值与离散时间特征值不能混用；解释时必须明确说明模型域和采样步长。

### 周期切换系统（Floquet 线性化）

对含 PWM 或其他周期开关的系统，稳态轨迹是周期 $T$ 的周期函数。一个周期内的状态转移矩阵为

$$
\boldsymbol{\Phi}_T=\mathbf{A}_{N-1} \mathbf{A}_{N-2} \cdots \mathbf{A}_1 \mathbf{A}_0,
$$

其中 $\mathbf{A}_i$ 是各开关区间的离散状态矩阵。Floquet 理论将 $\boldsymbol{\Phi}_T$ 的特征值 $\lambda_i$（Floquet 指数）换算为连续域阻尼：

$$
\sigma_i=\frac{\ln |\lambda_i|}{T}, \quad \omega_i=\frac{\arg(\lambda_i)}{T}.
$$

## EMT 中的线性化方法

根据 EMT 模型的类型和可获取信息，选择以下方法之一：

### 方法1：解析线性化

对白盒模型（解析方程已知），直接对 $\mathbf{f}(\mathbf{x}, \mathbf{u})$ 求偏导。优点是无数值误差；缺点是复杂控制系统的雅可比推导繁琐，且符号约定需严格一致。

适用于：控制器传递函数、电机方程、网络解析模型。

### 方法2：数值差分线性化

对状态或输入施加小扰动 $\varepsilon$，通过差分近似雅可比：

$$
\frac{\partial f_i}{\partial x_j} \approx \frac{f_i(\mathbf{x}+\varepsilon \mathbf{e}_j, \mathbf{u})-f_i(\mathbf{x}, \mathbf{u})}{\varepsilon}.
$$

扰动幅值 $\varepsilon$ 需权衡：太小受数值舍入影响，太大受非线性效应影响。经验值为额定值 $10^{-4}$~$10^{-3}$ pu。

适用于：黑盒 EMT 模型、软件模型、无法获取解析导数的复杂系统。

### 方法3：DAE 线性化

对微分-代数约束联立线性化。关键步骤：

1. 计算代数变量对状态变量的灵敏度 $\partial \mathbf{z}/\partial \mathbf{x}=-\mathbf{h}_z^{-1} \mathbf{h}_x$
2. 将灵敏度代入微分方程得到降阶状态矩阵
3. 处理代数雅可比 $\mathbf{h}_z$ 的奇异性（纯电感割集/纯电容回路会产生伪特征值 $\Omega=-1$）

Chindu 和 Kulkarni 2023 指出：当系统含纯电感割集或纯电容回路时，EMT 伴随电路会产生数值伪模态（伪特征值），这些模态与物理动态无关，需通过统计数量判据自动剔除。

### 方法4：EMT 伴随电路自动线性化

沿用 EMT 程序内部已有计算结构：

- 节点导纳矩阵 $\mathbf{G}$ 及 LU 分解因子直接复用
- 历史项电流源直接作为状态变量，避免人工状态筛选
- 开关时刻的线性插值和颤振消除算法纳入小扰动传播链

状态转移矩阵 $\mathbf{A}$ 的显式表达式为：

$$
\mathbf{A}=\mathbf{I}-\begin{bmatrix} \frac{h}{2}\mathbf{L}^{-1}\mathbf{A}_L^T \\ -\frac{4}{h}\mathbf{C}\mathbf{A}_C^T \end{bmatrix} \mathbf{G}^{-1} [\mathbf{A}_L \ \mathbf{A}_C],
$$

其中 $\mathbf{L}$、$\mathbf{C}$ 为储能元件对角矩阵，$\mathbf{A}_L$、$\mathbf{A}_C$ 为关联矩阵。

此方法由 Chindu 和 Kulkarni 2023 提出，核心优势是**状态选择完全依赖 EMT 历史项**，无需拓扑分析和状态筛选。

### 方法5：Modelica 自动线性化

使用 Modelica 编译器将物理模型自动展平为 DAE：

$$
\mathbf{F}(t, \dot{x}, x, y, z)=0,
$$

并在任意运行点 $t_l$ 处自动计算雅可比，输出状态空间矩阵 $(\mathbf{A}, \mathbf{B}, \mathbf{C}, \mathbf{D})$。流程为：

1. 在 Modelica 环境中搭建完整 EMT 模型
2. 通过符号处理与代数环打破算法展平为全局 DAE
3. 选取目标运行点（稳态或准稳态）
4. 调用内置线性化函数计算 $\mathbf{A}=\partial \mathbf{h}/\partial \mathbf{x}$

Masoom 等 2025 的 PV park 案例证明，该方法无需手动推导状态方程即可对复杂新能源场站进行特征值分析。

## 工作流

1. **固定运行点**：记录拓扑、控制模式、潮流/周期稳态、步长、坐标系和初值来源（参见 [[steady-state-initialization]]）
2. **定义状态和输入**：区分物理状态（电感电流/电容电压）、控制状态、代数变量和数值历史项
3. **计算雅可比**：优先解析求导或自动微分；黑盒 EMT 用小扰动差分或频域识别
4. **处理 DAE 消元**：检查 $\mathbf{h}_z$ 非奇异性，必要时保留代数变量
5. **形成线性模型**：处理离散化、周期映射或输入输出通道选择
6. **验证残差**：检查 $\|\mathbf{A}\mathbf{v}-\lambda\mathbf{v}\|$、时域小扰动响应、频域阻抗/导纳
7. **报告边界**：绑定运行点、扰动幅值、模型阶次、状态定义和验证方式

## 变体对比表

| 变体 | 机制 | 适用场景 | 注意事项 |
|------|------|----------|----------|
| 解析线性化 | 对模型方程显式求导 | 白盒控制器、机器模型、网络方程 | 坐标和符号约定需严格一致 |
| 数值差分线性化 | 施加小扰动 $\varepsilon$ 并差分 | 黑盒 EMT 模型、软件模型 | $\varepsilon$ 步长太小受舍入影响，太大受非线性影响 |
| DAE 线性化 | 微分和代数约束联立线性化 | 节点网络、伴随模型、控制网络耦合 | 代数雅可比 $\mathbf{h}_z$ 奇异时解释失效 |
| 离散线性化 | 线性化一步或多步映射 | 固定步长 EMT、采样控制 | 特征值依赖步长和事件处理 |
| Floquet 线性化 | 构造周期状态转移矩阵 $\Phi_T$ | 周期开关系统（PWM、方波） | 需可靠的周期稳态轨迹；伪特征值需剔除 |
| EMT 伴随电路自动线性化 | 复用 EMT 内部矩阵和 LU 因子 | PSCAD/EMTDC/EMTP 程序内嵌分析 | 依赖程序内部数据结构；需处理开关插值 |
| Modelica 自动线性化 | 编译器自动展平 DAE 并计算雅可比 | 复杂新能源场站、多级电力电子系统 | 需要 Modelica 编译器和 MSEMT 库 |

## 量化性能边界

### 数值精度

- **双线性变换精度**：连续域与离散域特征值通过 $\lambda_c=\frac{2}{h}\frac{\lambda_d-1}{\lambda_d+1}$ 精确对应，该性质**不受仿真步长影响**
- **扰动幅值敏感性**：推荐扰动幅度为额定值 $0.02\%$~$2\%$；电压控制模式换流器建议 $<0.5\%$
- **最大电压偏差**：应控制在 $\pm 5\%$ 以内以保证线性化精度（Cifuentes 2025）

### EMT 伴随电路自动线性化（Chindu 2023）

- **特征值精度**：连续/离散特征值匹配误差为 $0\%$，该性质不受步长影响
- **伪模态剔除判据**：离散模型特征值数量严格等于电路中"纯电感割集与纯电容回路"总数，可作为定量判据
- **稳定性充要条件**：状态转移矩阵所有物理特征值 $|\lambda_i|<1$

### Modelica 自动线性化（Masoom 2025）

- **特征值实部判据**：$\text{Re}(\lambda_i)>0$ 直接指示负阻尼风险，无需长周期 EMT 仿真
- **保留测量滤波器**：保留输入滤波器等非线性环节后，小扰动线性化精度显著提升
- **适用范围**：PV 场站控制交互风险快速筛查，特征值分析结果需 EMT 仿真交叉验证

### Z-Tool 频域识别（Cifuentes 2025）

- **导纳矩阵识别**：$\mathbf{Y}(j\omega)=[\Delta\mathbf{i}_1 \cdots \Delta\mathbf{i}_N][\Delta\mathbf{v}_1 \cdots \Delta\mathbf{v}_N]^{-1}$，支持 $N \times N$ 多端耦合系统
- **扰动优化**：dq 对称性利用可减少 $50\%$ 所需扰动次数，仿真时间降低近一半
- **多频激励**：单次仿真可提取多个频率点响应，总时间从 $N \times T_{\text{single}}$ 缩短至 $\approx T_{\text{single}}$

## 关键技术挑战

1. **运行点收敛性**：运行点未收敛或初始化不一致时，线性化矩阵描述启动伪暂态而非目标系统
2. **限幅与饱和**：限幅、死区、保护动作、换相失败、拓扑切换会破坏单一光滑雅可比假设
3. **强不平衡/谐波稳态**：正序相量模型的线性化不能替代 EMT 相域或周期模型
4. **数值差分误差**：扰动幅值、步长、插值策略和噪声均影响数值雅可比精度
5. **DAE 奇异性**：$\mathbf{h}_z$ 接近奇异时状态矩阵条件数剧增，特征值解释失效
6. **伪特征值剔除**：数值离散和拓扑依赖产生的伪模态需通过物理判据识别和剔除
7. **周期稳态求解**：周期切换系统的稳态轨迹需要可靠的外迭代收敛方法

## 适用边界与选择指南

- **有解析模型**且控制结构已知 → 解析线性化（精度高、无数值误差）
- **黑盒 EMT 模型**（如 PSCAD 子模块）→ 数值差分线性化（通用性强）
- **含网络代数约束的系统**（节点分析、伴随电路）→ DAE 线性化或 EMT 伴随电路自动线性化（复用 LU 因子）
- **周期切换系统**（PWM 变流器）→ Floquet 线性化（需要周期轨迹）
- **复杂新能源场站**（多级电力电子、控制器）→ Modelica 自动线性化（自动化程度高）
- **黑盒 EMT 模型 + 多端频域表征需求** → Z-Tool 频域识别（支持 AC/DC 混合系统矩阵化表征）

**不适用场景**：大扰动暂态、保护动作瞬间、故障穿越非线性过程、限幅饱和非线性闭环、实时仿真硬件在环验证。

## 来源论文

- [[an-automatable-approach-for-small-signal-stability-analysis-of-power-electronic-]]：Chindu 和 Kulkarni 2023 — EMT 伴随电路自动线性化框架，状态选择依赖历史项而非人工筛选，伪特征值判据，$|\lambda_i|<1$ 稳定性充要条件
- [[fast-investigation-of-control-interaction-risks-in-pv-parks-using-eigenvalue-ana]]：Masoom 等 2025 — Modelica 自动线性化流程，DAE 展平 + 泰勒线性化 + 特征值扫描，$\text{Re}(\lambda)>0$ 负阻尼判据
- [[z-tool-frequency-domain-characterization-of-emt-models-for-small-signal-stabilit]]：Cifuentes 和 Beerten 2026 — Z-Tool 频域导纳识别，dq 坐标变换，多频激励优化，$\pm 5\%$ 电压偏差控制，dq 对称性 $50\%$ 扰动次数减少