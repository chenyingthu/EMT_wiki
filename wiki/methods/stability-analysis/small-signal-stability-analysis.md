---
title: "小信号稳定性分析 (Small-signal Stability Analysis)"
type: method
tags: [small-signal-stability, eigenvalue-analysis, oscillation-mode, damping, power-system]
created: "2026-05-02"
updated: "2026-05-16"
---

# 小信号稳定性分析 (Small-signal Stability Analysis)

## 定义与边界

小信号稳定性分析是围绕某个运行点构造线性小扰动模型，并用[[eigenvalue-analysis]]、频域矩阵判据或 EMT 扰动响应验证局部稳定性的流程。它服务于[[small-signal-stability]]这一稳定性概念本身，但分析方法是通用的——适用于同步机低频振荡（0.1–2 Hz）、电力电子控制相互作用（数十到数百 Hz）、次同步振荡（SSO）乃至谐波不稳定等宽频带场景。

本页关注"如何分析"：输入是什么、如何线性化、怎样解释结果、何时需要 EMT 时域交叉验证。它不承诺固定阻尼阈值或某个软件流程的普遍适用性。

## EMT 中的角色

EMT 小信号稳定性分析常用于以下问题：

- 对电力电子化系统的控制相互作用进行运行点筛查（PLL 交互、次同步/谐波不稳定）
- 从 EMT 详细模型中提取可用于模态解释的线性模型
- 将阻抗扫描、频率响应和状态空间特征值联系起来
- 在大扰动 EMT 仿真前识别可能的弱阻尼或负阻尼工况

与只用相量域模型的分析不同，EMT 线性化可能保留：控制采样、开关事件、伴随电路历史项、频变线路、dq/abc 坐标变换和端口导纳矩阵。这些细节直接影响特征值和参与因子的物理可解释性，因此分析报告必须说明这些取舍。

## 四种分析路径

小信号稳定性分析在 EMT 框架下存在四条相互独立的分析路径，各自对应不同的线性化对象、数学框架和适用场景。路径之间不是优劣之分，而是问题导向的选择关系。

### 路径一：EMT 伴随电路 LTI 采样数据模型（Chindu & Kulkarni 2023）

此路径直接从 EMT 时域仿真（TDS）的伴随电路出发，将电感、电容的历史项电流源定义为状态变量，复用节点导纳矩阵 $G$ 及其 LU 分解因子，构建离散状态空间模型。

**数学框架**：对于固定步长 $h$ 的梯形积分，网络中电感、电容分别等效为电导 $G_L = \frac{h}{2L^{-1}}$ 和 $G_C = \frac{2C}{h}$ 串联历史电流源。状态向量取历史电流源 $\mathbf{x}_k$，节点电压由 $G^{-1}$ 快速求解：

$$\mathbf{x}_{k+1} = \mathbf{A}\mathbf{x}_k + \mathbf{B}\mathbf{u}_k$$

其中状态转移矩阵为：

$$\mathbf{A} = \mathbf{I} - \begin{bmatrix} \frac{h}{2}\mathbf{L}^{-1}\mathbf{A}_L^\top \\ -\frac{4}{h}\mathbf{C}\mathbf{A}_C^\top \end{bmatrix} \mathbf{G}^{-1}[\mathbf{A}_L \ \mathbf{A}_C]$$

对于周期性开关系统，将一个基频周期 $T$ 内的 $N$ 个步长矩阵连乘：

$$\mathbf{\Phi}_T = \mathbf{A}_{N-1}\mathbf{A}_{N-2}\cdots\mathbf{A}_1\mathbf{A}_0$$

$\mathbf{\Phi}_T$ 的特征值 $\Omega$ 通过双线性变换映射回连续域：

$$\lambda = \frac{2}{h}\frac{\Omega - 1}{\Omega + 1}$$

**稳定性判据**：系统小信号稳定的充要条件是 $\mathbf{\Phi}_T$ 所有物理特征值模值严格小于 1（$|\Omega_i| < 1$）。同时，$\Omega = -1$ 的特征值数量等于电路中纯电感割集与纯电容回路总数——这是自动剔除数值伪模态的定量判据。

**量化性能边界**：连续域特征值与离散域特征值通过双线性变换精确匹配，误差为 0% 且与步长无关；额外计算开销主要来自状态转移矩阵连乘，计算复杂度与 TDS 同量级。

此路径的优势在于：状态选择依赖 EMT 历史项而非人工拓扑筛选；矩阵求解复用 TDS 已有的 LU 因子；周期开关系统通过单周期状态转移矩阵转化为可特征值分析问题。**主要局限**：需要系统已达到周期稳态；不适用于大扰动后的非周期暂态过程。

### 路径二：Modelica DAE 自动线性化（Masoom 2025）

此路径使用 Modelica 方程建模，通过 MSEMT 库构建包含光伏阵列、DC-AC 变流器、变压器、集电线路及故障穿越逻辑的完整 EMT 详细模型，由 Modelica 编译器自动将分层物理模型展平为微分代数方程组（DAEs），在任意运行点处进行泰勒级数线性化，直接提取显式状态空间矩阵 $\mathbf{A}, \mathbf{B}, \mathbf{C}, \mathbf{D}$。

**数学框架**：Modelica 编译器将分层图形模型展平为全局微分代数方程：

$$F(t, \dot{\mathbf{x}}, \mathbf{x}, \mathbf{y}, \mathbf{z}) = 0$$

其中 $\mathbf{x}$ 是动态状态，$\mathbf{y}$ 是代数变量，$\mathbf{z}$ 是外部输入。在选定时刻 $t_l$ 处做一阶泰勒线性化：

$$\delta\dot{\mathbf{x}} = \mathbf{A}\delta\mathbf{x} + \mathbf{B}\delta\mathbf{u}, \quad \delta\mathbf{y} = \mathbf{C}\delta\mathbf{x} + \mathbf{D}\delta\mathbf{u}$$

**量化性能边界**：特征值实部大于 0 直接指示负阻尼风险，无需依赖时域长周期仿真；保留输入滤波器与非性环节后，小扰动场景下的线性化精度显著提升；Modelica 自动线性化流程消除了手动推导状态方程的拓扑依赖，任意电路结构变更均可直接提取 $\mathbf{A}/\mathbf{B}/\mathbf{C}/\mathbf{D}$ 矩阵。

此路径的优势在于：可保留测量滤波器等手工建模中易省略的环节；拓扑变化时不必重新手写线性模型；直接给出振荡模态频率和阻尼方向。**主要局限**：本质上仍是局部小信号分析，不能直接证明大扰动、保护切换、限幅饱和或离散控制事件后的全局稳定性。

### 路径三：Floquet 理论参与因子法（Sajjadi et al. 2026）

此路径将 EMT 模型在周期稳态轨迹附近视为线性时周期（LTP）系统，利用 Floquet 理论在单个基频周期（如 60 Hz 下 $T = 1/60$ s）内提取模态信息，用于确定 EMT 建模区域边界。

**数学框架**：LTP 系统状态方程为：

$$\dot{\mathbf{x}}(t) = \mathbf{A}(t)\mathbf{x}(t), \quad \mathbf{A}(t + T) = \mathbf{A}(t)$$

Floquet 单值矩阵（状态转移矩阵）为：

$$\mathbf{\Phi}(T) = \mathcal{T}\exp\left(\int_0^T \mathbf{A}(\tau)d\tau\right)$$

Floquet 乘子 $\mu_i$ 与特征指数 $\lambda_i$ 的关系：

$$\lambda_i = \frac{1}{T}\ln(\mu_i)$$

参与因子（Floquet PF）定义为：

$$P_{ki} = \frac{\partial\lambda_i}{\partial a_{kk}}$$

**谐波筛选准则**：基于 Floquet 理论的谐波参与因子：

$$P_{ki}^{(h)} = \frac{\partial\lambda_i}{\partial a_{kk}^{(h)}}$$

**量化性能边界**：单周期（$1/60$ s）数据即可完成全系统模态与参与因子提取，时间窗口较传统长时仿真缩短 99% 以上；谐波筛选准则可剔除超过 85% 的冗余状态变量，同时保证目标 SSO 模式特征值实部误差小于 0.01 和虚部误差小于 0.5 rad/s；多端口诺顿等值在故障暂态期间无需时步更新，单次计算即可复用，使边界外网络求解复杂度从 $O(N^3)$ 降至 $O(1)$。

此路径的核心价值在于：边界选择由 Floquet 模态参与因子驱动，能围绕特定振荡模式选择 IBR、发电机、线路等关键元件；突破了传统相量域（LTI）参与因子仅为 Floquet PF 的零次谐波（$h=0$）特例的局限。**主要局限**：验证仅在两区系统和 IEEE 39 节点系统上完成。

### 路径四：频域 EMT 阻抗扫描（Z-Tool，Cifuentes & Beerten 2025）

此路径通过在 EMT 仿真中注入小扰动信号并测量响应，识别多端 AC/DC 系统的频域导纳矩阵，再基于 Nyquist 判据或阻抗比分析评估小信号稳定性。

**数学框架**：dq 坐标变换矩阵（幅值不变型）为：

$$\mathbf{T}_{dq}(\theta) = \frac{2}{3}\begin{pmatrix} \cos\theta & \cos(\theta - 2\pi/3) & \cos(\theta + 2\pi/3) \\ \sin\theta & \sin(\theta - 2\pi/3) & \sin(\theta + 2\pi/3) \end{pmatrix}$$

频域导纳矩阵通过 $N$ 次线性独立电压扰动构建：

$$\mathbf{Y}(j\omega) = [\Delta\mathbf{i}_1 \ \cdots \ \Delta\mathbf{i}_N][\Delta\mathbf{v}_1 \ \cdots \ \Delta\mathbf{v}_N]^{-1}$$

多频（多音）扰动信号表达式为：

$$\Delta v(t) = \sum_{i=1}^{m} a_i\sin(\omega_i t + \phi_i)$$

**量化性能边界**：推荐扰动幅度范围为额定电压的 0.02%–2%，最大电压偏差应控制在 ±5% 以内；对电压控制模式换流器建议采用更小扰动幅度（小于 0.5%）；利用 dq 对称性可减少 50% 的所需扰动次数，仿真时间降低近一半；多频激励技术可将总仿真时间从 $N \times T_\text{single}$ 缩短至接近 $T_\text{single}$（$N$ 为频率点数量）；支持任意 $N \times N$ 维导纳矩阵识别，其中 $N$ 为子系统 AC/DC 节点总数。

此路径的优势在于：能对黑盒 EMT 模型进行多端、混合 AC/DC、矩阵化的小信号频域表征；适用于电力电子设备厂商不提供内部控制方程时的换流器-线路-电机相互作用分析。**主要局限**：EMT 数值积分步长影响识别精度，存在 time-step-dependent 误差；未覆盖所有控制策略、故障工况和强非线性大扰动场景。

## 形式化表达

### DAE 线性化通用形式

连续时间 DAE 可写为：

$$\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \mathbf{y}, \mathbf{u}), \quad \mathbf{0} = \mathbf{g}(\mathbf{x}, \mathbf{y}, \mathbf{u})$$

若 $\partial\mathbf{g}/\partial\mathbf{y}$ 在运行点附近可逆，可消去代数变量，得到线性化状态方程：

$$\Delta\dot{\mathbf{x}} = \underbrace{\left(\mathbf{f}_\mathbf{x} - \mathbf{f}_\mathbf{y}\mathbf{g}_\mathbf{y}^{-1}\mathbf{g}_\mathbf{x}\right)}_{\mathbf{A}}\Delta\mathbf{x} + \underbrace{\left(\mathbf{f}_\mathbf{u} - \mathbf{f}_\mathbf{y}\mathbf{g}_\mathbf{y}^{-1}\mathbf{g}_\mathbf{u}\right)}_{\mathbf{B}}\Delta\mathbf{u}$$

### 离散 EMT 伴随电路形式

对于 EMT companion-circuit 路线，状态取电感、电容或历史项电流源，形成离散模型：

$$\Delta\mathbf{x}_{k+1} = \mathbf{A}_d\Delta\mathbf{x}_k + \mathbf{B}_d\Delta\mathbf{u}_k$$

周期系统则常将一个周期内的步进矩阵连乘为状态转移矩阵 $\mathbf{\Phi}(T)$，再分析其特征值或 Floquet 指数。

### 模态解释框架

特征值解释应分开以下维度：

| 维度 | 连续系统 | 离散系统 | 物理含义 |
|------|---------|---------|---------|
| 稳定性 | $\text{Re}(\lambda_i) < 0$ | $|\Omega_i| < 1$ | 局部增长/衰减趋势 |
| 振荡频率 | $\text{Im}(\lambda_i)/2\pi$ (Hz) | $\arg(\Omega_i)/2\pi T$ (Hz) | 振荡频率解释 |
| 阻尼比 | $\zeta_i = -\text{Re}(\lambda_i)/|\lambda_i|$ | — | 相对阻尼度量 |

### 参与因子

右特征向量 $\mathbf{v}_i$ 给出模态形状，左特征向量 $\mathbf{w}_i$ 与参与因子：

$$p_{ki} = w_{ki} \cdot v_{ki}$$

参与因子量化状态 $k$ 对模态 $i$ 的局部关联程度。留数或输入输出灵敏度则用于判断控制信号是否能有效作用于该模态。

## 关键技术挑战

### 挑战一：周期稳态的确定

周期性开关系统的稳态不是简单的直流量——开关导致状态在每个周期重复但轨迹非正弦。此时单个连续时间 $\mathbf{A}$ 矩阵不足以描述动态，而需要周期状态转移矩阵 $\mathbf{\Phi}(T)$ 或 Floquet 框架。单周期轨道的获取本身需要足够的仿真时间收敛到准稳态。

**解决思路**：先用长时间 EMT 仿真观察状态是否进入周期（或使用频谱分析确认谐波固定）；然后在周期轨迹上逐开关区间构造线性映射，连乘形成 $\mathbf{\Phi}(T)$。

### 挑战二：数值伪特征值的识别与剔除

EMT 离散化（尤其是梯形积分）会引入数值伪特征值——这些特征值源于数值方法而非物理动态。典型判据是：$\Omega = -1$（离散）或 $\lambda = -2/h$（连续）的特征值通常对应纯电感割集/纯电容回路的数量。

**解决思路**：利用纯电感割集与纯电容回路数量作为伪模态计数判据；或者将连续系统特征值与离散系统特征值做双线性变换交叉检查，不匹配者视为伪模态。

### 挑战三：运行点敏感性

小信号稳定性对运行点敏感：负荷水平、出力分布、网络拓扑和控制参数的变化可能导致原本稳定的系统在参数漂移后失稳。单一运行点的特征值分析不能覆盖参数空间中所有风险区域。

**解决思路**：参数扫描（在多个运行点或控制参数下复算模态）是基本手段；结合机器学习的风险预测可辅助识别高风险工况区；关键模态是否随控制参数或网络强度移动是重要检查项。

### 挑战四：电力电子控制的采样延迟与离散化

PLL、电流环、电压环等控制环节在数字实现中引入采样延迟（通常为 1 个或 1.5 个步长），这些延迟影响系统相位裕度。在小信号模型中，延迟环节表现为 $e^{-sT_d}$ 或 $z^{-1}$ 的传递函数，若处理不当会导致特征值高估阻尼。

**解决思路**：在状态空间模型中显式引入延迟状态（相位累加器或延迟队列）；在 Floquet 分析中，延迟使 $\mathbf{A}(t)$ 在一个周期内呈现分段常值特性，需按控制时钟分段构造。

### 挑战五：大规模系统的计算效率

全系统 EMT 伴随电路状态空间模型的阶数等于储能元件（电感、电容）的数量，对大规模实际电网可能达到数万阶。直接特征值分解的计算复杂度为 $O(n^3)$，在大规模系统上代价极高。

**解决思路**：模型降阶（如 [[model-order-reduction]]）先于特征值分析；稀疏特征值求解只关注目标频段内的特征值；分块/区域等值将非研究区域用简约模型替代（如 Sajjadi 2026 中的多端口诺顿等值）。

## 量化性能边界

| 分析路径 | 方法核心 | 适用频率范围 | 计算开销 | 关键量化指标 |
|---------|---------|------------|---------|------------|
| 路径一（LTI采样） | 伴随电路+状态转移矩阵 | DC–数百 Hz | 与TDS同量级 | 特征值误差 0%；额外开销≈0 |
| 路径二（Modelica） | DAE自动线性化 | 0.1 Hz–数十 Hz | 自动化，建模时间大幅缩短 | 特征值实部>0即指示负阻尼 |
| 路径三（Floquet PF） | 单周期状态转移矩阵 | 次同步（10–50 Hz） | 单周期数据，时间窗口缩短99% | 冗余状态变量剔除>85%；SSO误差实部<0.01、虚部<0.5 rad/s |
| 路径四（Z-Tool阻抗） | 频域导纳识别+Nyquist | 全频段（DC–数kHz） | 多频激励，时间减少~50% | 扰动幅度0.02%–2%；对称性利用减少50%扰动次数 |

| 测试系统 | 分析路径 | 振荡频率 | 阻尼比/判据 | 验证方式 |
|---------|---------|---------|------------|---------|
| Buck变换器+STATCOM（Chindu 2023） | 路径一 | 次同步至数百Hz | $\|Omega_i\|<1$（离散） | EMT时域仿真对比 |
| 含IBR的IEEE 39节点（Sajjadi 2026） | 路径三 | SSO 10–50 Hz | 误差<2% | 全EMT模型对比 |
| VSC串补长线路（Cifuentes 2025） | 路径四 | 次同步 | Nyquist判据 | EMT时域+阻抗扫描 |
| PV场站多工况（Masoom 2025） | 路径二 | 0.1–30 Hz | 特征值实部>0 | EMTP时域+阻抗扫描 |

## 适用边界与选择指南

**选择路径一（LTI采样）的场景**：已知系统已达周期稳态、需要最高精度、关注开关瞬态对稳定性的影响、需要自动化建模流程。

**选择路径二（Modelica）的场景**：需要保留详细控制逻辑（滤波器、FRT）、拓扑频繁变更、团队熟悉 Modelica 建模流程、需要快速多工况筛查。

**选择路径三（Floquet PF）的场景**：目标是确定 EMT 建模边界（哪些元件需详细建模）、需要识别特定振荡模态的关键参与元件、需要在含多 IBR 的大系统中进行区域等值。

**选择路径四（Z-Tool阻抗）的场景**：设备厂商只提供黑盒 EMT 模型、需分析多端 AC/DC 系统（换流器+线路+电机耦合）、目标频段跨越宽频带（从次同步到谐波）。

**通用失败模式**：

- 将局部线性结果用于故障穿越、保护切换或限幅后的非线性过程
- 只报告"稳定/不稳定"而不说明运行点、模型阶次、坐标系和状态选择
- 忽略 EMT 离散化产生的伪特征值或步长依赖误差
- 用单篇论文算例的结果支撑一般工程结论

## 相关页面

- [[small-signal-stability]]：定义局部稳定性概念
- [[eigenvalue-analysis]]：提供特征值求解和稳定性解释
- [[modal-analysis]]：解释模态、参与因子和灵敏度
- [[modal-decomposition]]：解释时域响应如何由多个模态叠加
- [[generalized-eigenvalue-method]]：处理 DAE、矩阵束和广义谱问题
- [[dae-solvers]]：说明线性化前的 DAE 建模和求解背景
- [[model-order-reduction]]：模型降阶技术在大规模系统中的应用
- [[electromechanical-electromagnetic-hybrid-simulation]]：EMT 与相量域混合仿真中的小信号分析接口

## 来源论文

- [[an-automatable-approach-for-small-signal-stability-analysis-of-power-electronic-]] — Chindu & Kulkarni 2023：EMT 伴随电路 LTI 采样数据模型，自动构建 PE 电路小信号模型，特征值双线性变换精确匹配（误差 0%）
- [[fast-investigation-of-control-interaction-risks-in-pv-parks-using-eigenvalue-ana]] — Masoom 2025：Modelica DAE 自动线性化，PV 场站控制交互风险快速评估，特征值实部正即指示负阻尼
- [[z-tool-frequency-domain-characterization-of-emt-models-for-small-signal-stabilit]] — Cifuentes & Beerten 2025：Z-Tool 开源频域 EMT 模型识别，支持多端 AC/DC 导纳矩阵，dq 对称性利用减少 50% 扰动次数
- [[emt-model-boundary-determination-using-floquet-theory-based-participation-factor]] — Sajjadi et al. 2026：Floquet 参与因子 EMT 边界划分，单周期数据缩短 99% 时间窗口，剔除>85% 冗余状态变量