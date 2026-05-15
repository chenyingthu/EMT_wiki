---
title: "小信号稳定性 (Small-Signal Stability)"
type: method
tags: [small-signal, stability, oscillation, eigenvalue, damping, power-system, floquet, participation-factor]
created: "2026-05-02"
updated: "2026-05-15"
---

# 小信号稳定性 (Small-Signal Stability)

## 定义与边界

小信号稳定性指系统在某个运行点附近受到小扰动后，扰动量是否衰减、保持有界或增长。这里的"小"不是固定幅值，而是指扰动足够接近线性化点，使一阶模型能够代表局部动态。本质上，小信号稳定性分析是**在稳态工作点附近将非线性系统线性化，通过特征值位置判断系统模态是否衰减**的理论框架。

在 EMT 语境下，线性化对象可以是：
- **连续时间 LTI 系统**：状态矩阵 $\mathbf{A}$ 的特征值全部位于左半平面
- **离散时间 LTI 系统**：状态转移矩阵 $\mathbf{A}_d$ 的特征值全部位于单位圆内
- **线性时周期（LTP）系统**：Floquet 乘子全部位于单位圆内

本页讨论稳定性概念本身：它回答"这个运行点附近的微小扰动是否会衰减"。它不等同于 [[small-signal-stability-analysis]] 的建模流程，也不等同于 [[eigenvalue-analysis]] 或 [[modal-analysis]] 的计算操作。若扰动触发限幅、保护动作、控制模式切换、拓扑改变或强非线性暂态，应回到 EMT 时域仿真和场景验证，不能只凭小信号结论外推。

## EMT 中的角色

在 EMT 研究中，小信号稳定性常用于解释运行点附近的振荡、负阻尼和控制相互作用。与传统机电暂态小信号分析相比，EMT 模型可能包含开关、采样控制、PLL、多环控制、线路频变特性和电力电子装置的宽频动态。因此 EMT 语境下的小信号稳定性需要明确**四条分析路径**：

| 路径 | 线性化对象 | 核心工具 | 适用场景 |
|------|-----------|---------|---------|
| **路径A：伴随电路→采样数据模型** | EMT 伴随电路节点导纳矩阵、历史项电流源、开关插值 | 状态转移矩阵 $\mathbf{\Phi}_T$、特征值 $| \lambda_i | < 1$ | 周期性开关电力电子电路（buck、STATCOM、MMC） |
| **路径B：Modelica DAE 自动线性化** | 微分代数方程组 $F(t, \dot{x}, x, y, z) = 0$ 在运行点处泰勒展开 | 状态空间矩阵 $( \mathbf{A}, \mathbf{B}, \mathbf{C}, \mathbf{D} )$、特征值分析 | 光伏场站、风电场等多设备复杂系统的控制交互风险筛查 |
| **路径C：Floquet 理论** | 周期稳态轨迹附近的线性时变系统 $\dot{\mathbf{x}} = \mathbf{A}(t)\mathbf{x}$，$\mathbf{A}(t+T) = \mathbf{A}(t)$ | Floquet 乘子 $\mu_i$、参与因子 $P_{ki}$、单值矩阵 $\mathbf{\Phi}(T)$ | 含周期性开关的 HVDC/MMC 系统、SSO 模态定位、EMT 模型边界划分 |
| **路径D：EMT 频域阻抗扫描** | EMT 仿真黑盒模型的端口响应 | 导纳矩阵 $\mathbf{Y}(j\omega)$、阻抗矩阵 $\mathbf{Z}(j\omega)$、闭环特征值、Nyquist 判据 | 厂商黑盒模型、PLL/控制器细节不可得的 IBR 并网系统 |

这四条路线都可以支撑小信号稳定判断，但它们的状态、特征值位置、频率解释和验证边界并不相同。

## 核心机制

### 连续时间 LTI 系统的稳定性判据

若非线性系统在运行点 $(\mathbf{x}_0,\mathbf{u}_0)$ 附近可线性化，可写为

$$\Delta\dot{\mathbf{x}} = \mathbf{A}\Delta\mathbf{x} + \mathbf{B}\Delta\mathbf{u}, \quad \Delta\mathbf{y} = \mathbf{C}\Delta\mathbf{x} + \Delta\mathbf{u}.$$

当只看自由响应时，稳定性由状态矩阵 $\mathbf{A}$ 的特征值决定：

$$\mathbf{A}\mathbf{v}_i = \lambda_i\mathbf{v}_i, \quad \lambda_i = \sigma_i + j\omega_i.$$

在连续时间 LTI 模型中，若所有相关特征值满足 $\sigma_i < 0$，对应模态局部衰减；若存在 $\sigma_i > 0$，该线性化模型显示扰动会增长。复特征值的虚部可换算为振荡频率：

$$f_i = \frac{|\omega_i|}{2\pi}.$$

阻尼比常写为

$$\zeta_i = -\frac{\sigma_i}{\sqrt{\sigma_i^2 + \omega_i^2}}.$$

### 离散时间 LTI 系统的稳定性判据

EMT 仿真通常采用固定步长 $h$ 的数值积分（如梯形法、后向欧拉法），得到的等效离散模型为

$$\mathbf{x}_{k+1} = \mathbf{A}_d \mathbf{x}_k + \mathbf{B}_d \mathbf{u}_k.$$

离散系统的稳定性由 $\mathbf{A}_d$ 的特征值模值决定：

$$|\lambda_i(\mathbf{A}_d)| < 1 \quad \Longleftrightarrow \quad \text{小信号稳定}.$$

### 连续域与离散域特征值的映射

对于梯形积分法（Bilinear/Tustin 变换），离散域特征值 $\Omega$ 与连续域特征值 $\lambda$ 通过下式精确映射：

$$\lambda = \frac{2}{h} \frac{\Omega - 1}{\Omega + 1}.$$

该双线性变换保证了：$|\Omega| < 1$ 当且仅当 $\mathrm{Re}(\lambda) < 0$，两种判据等价。

### 周期性开关系统的 Floquet 理论

对于含周期性开关的电力电子系统（如 MMC、HVDC 换流器），系统在每个基波周期 $T$ 内经历多次拓扑变化，不能简单地用单一 $\mathbf{A}$ 矩阵描述。正确的分析框架是 Floquet 理论：

$$\dot{\mathbf{x}}(t) = \mathbf{A}(t)\mathbf{x}(t), \quad \mathbf{A}(t+T) = \mathbf{A}(t).$$

在一个周期内积分得到单值矩阵（状态转移矩阵）：

$$\mathbf{\Phi}(T) = \mathcal{T}\exp\left(\int_0^T \mathbf{A}(\tau)d\tau\right).$$

$\mathbf{\Phi}(T)$ 的特征值称为 Floquet 乘子 $\mu_i$。稳定性判据为

$$|\mu_i| < 1 \quad \Longleftrightarrow \quad \text{小信号稳定}.$$

Floquet 乘子与连续域特征指数 $\lambda_i$ 的转换为

$$\lambda_i = \frac{1}{T}\ln(\mu_i) = \sigma_i + j\omega_i.$$

参与因子的 Floquet 版本为

$$P_{ki}^{(h)} = \frac{\partial \lambda_i}{\partial a_{kk}^{(h)}},$$

其中 $h$ 表示谐波次数（$h = 0, \pm 1, \pm 2, \ldots$）。传统相量域参与因子仅为 $h = 0$ 的特例，无法反映高次谐波动态交互。

### 频域阻抗法的小信号稳定性

对于黑盒 EMT 模型，可通过在 PCC 注入小扰动信号提取端口导纳/阻抗矩阵：

$$\mathbf{Y}(j\omega) = [\Delta\mathbf{i}_1 \ \cdots \ \Delta\mathbf{i}_N][\Delta\mathbf{v}_1 \ \cdots \ \Delta\mathbf{v}_N]^{-1}.$$

闭环系统的传递函数为

$$\frac{\Delta V_{PCC}}{\Delta I_{Dis}} = \frac{\mathbf{Z}_{MMC}}{1 + \mathbf{Z}_{MMC} \cdot \mathbf{Y}_{ac}}.$$

系统稳定性通过开环增益矩阵 $\mathbf{Z}_{MMC}\mathbf{Y}_{ac}$ 的特征值轨迹的相位/增益裕度判断（Nyquist 判据）。

## 类型与对象

| 对象 | 小信号稳定性问题 | EMT 关注点 |
|------|-----------------|-----------|
| 同步机与励磁/PSS | 机电振荡是否有足够阻尼 | [[swing-equation]]、 [[excitation-system]] 和 [[power-system-stabilizer]] 的参数共同影响模态；EMT 中需考虑磁路饱和、励磁限幅 |
| 电力电子并网装置（IBR） | PLL、电流环、电压环和网络阻抗是否形成负阻尼 | 状态空间、阻抗扫描和 EMT 时域扰动需要交叉解释；PLL 带宽设计不当是次同步振荡（SSO）的常见诱因 |
| 周期开关系统（MMC/LCC/HVDC） | 周期稳态附近扰动是否跨周期衰减 | 状态转移矩阵或 Floquet 乘子比单一连续 $\mathbf{A}$ 矩阵更贴近问题；开关时刻插值和颤振消除影响模态精度 |
| 线路和频变网络 | 频变传播、端口导纳和控制器是否耦合出弱阻尼模式 | 与 [[frequency-scan]]、 [[impedance-measurement]] 和 [[frequency-dependent-line-model]] 相关；频变阻抗的相位旋转效应在谐波频段可能导致负阻尼 |
| 新能源场站（光伏/风电） | 控制交互风险：PLL/电流环/电压环与弱网阻抗的耦合 | Modelica DAE 自动线性化、频域阻抗扫描、SSO 模态定位与阻尼设计 |

## EMT 建模方法与实现路径

### 路径A：EMT 伴随电路→采样数据 LTI 模型（Chindu 2023）

Chindu 和 Kulkarni（2023）提出直接复用 EMT 程序内部伴随电路的节点导纳矩阵 $\mathbf{G}$ 和 LU 分解因子，将历史项电流源定义为状态变量，无需手工筛选拓扑。具体步骤：

1. 运行 EMT 时域仿真至周期性稳态，记录每个步长 $h$ 下的 $\mathbf{G}$、节点-支路关联矩阵 $\mathbf{A}_L, \mathbf{A}_C$ 和历史项电流源
2. 对每个开关区间计算离散状态矩阵 $\mathbf{A}_i$ 和 $\mathbf{B}_i$：复用 $\mathbf{G}$ 的 LU 因子避免重复求逆
3. 处理跨步长开关事件：用线性插值计算分数步 $\tau$，计算开关时刻扰动 $\Delta\tau$
4. 将一个周期 $T = Nh$ 内的所有状态转移矩阵连乘得到周期状态转移矩阵 $\mathbf{\Phi}_T$
5. 剔除 $\Omega = -1$ 的伪特征值（数量等于纯电感割集与纯电容回路总数），保留物理动态特征值
6. 稳定性判定：$|\lambda_i| < 1$ 即系统小信号稳定

关键公式——状态转移矩阵的解析表达式为

$$\mathbf{A} = \mathbf{I} - \begin{bmatrix} \frac{h}{2}\mathbf{L}^{-1}\mathbf{A}_L^T \\ -\frac{4}{h}\mathbf{C}\mathbf{A}_C^T \end{bmatrix} \mathbf{G}^{-1} [\mathbf{A}_L \ \mathbf{A}_C].$$

### 路径B：Modelica DAE 自动线性化（Masoom 2025）

Masoom 等（2025）提出基于 Modelica 方程建模的光伏场站控制交互风险快速评估框架。利用 MSEMT 库构建完整 EMT 模型后，Modelica 编译器自动将分层物理模型展平为微分代数方程组：

$$F(t, \dot{x}, x, y, z) = 0,$$

其中 $x$ 是动态状态，$y$ 是代数变量，$z$ 是外部输入。在选定运行点 $t_l$ 处进行泰勒级数线性化：

$$\delta\dot{x} = \mathbf{A}\delta x + \mathbf{B}\delta u, \quad \delta y = \mathbf{C}\delta x + \mathbf{D}\delta u.$$

随后对 $\mathbf{A}$ 做特征值分解，复特征值实部为正即指示负阻尼风险。该方法的优势在于：任意拓扑变更均可直接提取 $\mathbf{A}/\mathbf{B}/\mathbf{C}/\mathbf{D}$ 矩阵，无需手工推导；可保留输入滤波器等以往线性化中容易省略的环节。

### 路径C：Floquet 理论与参与因子（Sajjadi 2026）

Sajjadi 等（2026）将 Floquet 理论参与因子用于 EMT 模型边界自动划分。核心思路：

1. 将 EMT 模型在周期稳态轨迹附近线性化为 LTP 系统
2. 提取单周期状态转移矩阵（单值矩阵）$\mathbf{\Phi}(T)$
3. 计算 Floquet 乘子 $\mu_i$ 与左右特征向量，进而计算各状态变量对目标振荡模式（如 SSO）的参与因子 $P_{ki}$
4. 设定参与因子阈值，筛选出高参与度的 IBR、发电机、关键母线作为 EMT 详细建模区域
5. 边界外网络用多端口 Norton 等值替代

关键量化结论：仅需单周期（$1/60\text{s}$）数据即可完成全系统模态与参与因子提取，时间窗口较传统长时仿真缩短 99% 以上；谐波筛选准则可剔除 >85% 的冗余状态变量，同时保证目标 SSO 模式特征值实部与虚部误差分别 <0.01 和 <0.5 rad/s。

### 路径D：EMT 频域阻抗扫描（Jiang 2025, Cifuentes Garcia 2025）

Jiang 等（2025）提出基于 PSCAD/EMTDC 的自动化动态频率扫描工具：在稳态运行点注入多频正弦扰动信号，记录 PCC 处响应，用 DFT 提取频域幅值与相位，在 dq0 坐标系下构造阻抗/导纳矩阵，通过开环增益矩阵 $\mathbf{Z}_{MMC}\mathbf{Y}_{ac}$ 的特征值伯德图预测临界短路比（CSCR）和振荡频率。

Cifuentes Garcia 和 Beerten（2025）提出开源 Z-tool 方法，支持多端 AC/DC 混合系统的自动化频域识别，推荐扰动幅度为额定电压的 0.02%–2%，利用 dq 对称性可减少 50% 所需扰动次数。

## 关键技术挑战

### 挑战1：伪特征值的识别与剔除

在 EMT 伴随电路方法中，数值离散化会引入伪特征值。特别地，当系统存在纯电感割集或纯电容回路时，$\Omega = -1$ 的特征值对应的是数值伪模态而非物理动态。判据：离散模型中 $\Omega = -1$ 的特征值数量严格等于原电路中纯电感割集与纯电容回路的总数，自动剔除后保留物理特征值。

### 挑战2：周期系统的 Floquet 计算效率

计算 $\mathbf{\Phi}(T)$ 需要在一个基频周期内对时变 $\mathbf{A}(t)$ 积分或连乘多个开关区间的状态矩阵。对于高频率开关系统（如 PWM 变流器），周期内可能有数百个开关事件，直接数值积分代价高昂。优化策略：利用开关时刻的稀疏性，只在开关时刻前后求解 $\mathbf{A}(t)$；对稳态运行点预先计算 $\mathbf{\Phi}(T)$ 并缓存。

### 挑战3：黑盒模型的端口导纳提取

厂商提供的 EMT 模型通常不开放控制器内部结构，仅提供封装后的端口界面。频域阻抗扫描需要在不打开黑盒的前提下，通过外部扰动-响应测量推断端口动态。挑战包括：多频扰动幅值的选择（太小则信噪比低，太大则线性化假设失效）、dq0 坐标系的频率耦合处理、非最小相位系统的阻抗提取。

### 挑战4：非线性环节与限幅的线性化处理

实际电力电子系统包含 PWM 调制、PLL 同步、电流限幅、故障穿越（FRT）逻辑等强非线性环节。这些环节在小扰动分析中通常被近似为线性，但限幅器饱和、控制模式切换等事件会导致工作点突变，使小信号模型失效。Masoom 2025 的 Modelica 方法尝试保留 FRT 非线性环节，但线性化结果仍受运行点约束。

### 挑战5：多时间尺度系统的模态分离与交互分析

同步机（水轮机/汽轮机调速器、励磁系统）与电力电子装置（PLL、电压环、电流环）在 EMT 中可能跨越从微秒级开关事件到秒级机电暂态的宽时间尺度。单一特征值分析可能遗漏耦合模态；需要进行模态分离（如机电模态 0.1–2 Hz、控制模态 10–100 Hz、电磁模态 >100 Hz）后再分别评估交互风险。

## 量化性能边界

| 方法 | 适用场景 | 核心指标 | 代表性数据 |
|------|---------|---------|-----------|
| Chindu 2023 伴随电路法 | buck 变换器、STATCOM | 特征值匹配误差 | 连续域-离散域特征值通过双线性变换精确匹配，误差 0% |
| Masoom 2025 Modelica | 光伏场站控制交互 | 特征值实部 >0 指示负阻尼 | 可覆盖次/超同步频段，无需长周期 EMT 仿真 |
| Sajjadi 2026 Floquet | IEEE 39 节点 IBR 系统 | SSO 参与因子提取精度 | 单周期数据缩短 99%+；剔除 >85% 冗余状态变量；特征值实部误差 <0.01、虚部误差 <0.5 rad/s |
| Jiang 2025 频域扫描 | MMC GFM/VSG 并网 | CSCR 预测精度 | 电压源型 VSG：CSCR ≈ 3.7，振荡频率 1.15 Hz；电流源型 VSG：SCR 高达 100 仍稳定 |
| Cifuentes 2025 Z-tool | 多端 AC/DC 系统 | 导纳矩阵识别误差 | 步长依赖性误差；利用 dq 对称性减少 50% 扰动次数 |

## 适用边界与选择指南

**选择路径 A（EMT 伴随电路）当**：有 EMT 程序源码/插件接口、需要分析的电路包含 RLC 元件和简单开关、被分析系统已达周期性稳态、目标是 buck/STATCOM 等中小规模电力电子电路。

**选择路径 B（Modelica DAE）当**：分析对象是光伏/风电场站等含多设备的复杂系统、拓扑经常变更需要反复线性化、已有 Modelica/MSEMT 模型、目标是快速筛查控制交互风险。

**选择路径 C（Floquet 参与因子）当**：分析含周期性开关的 MMC/HVDC 系统、目标是确定哪些 IBR/发电机应纳入 EMT 详细建模区域（边界划分）、需要识别 SSO 等特定振荡模式的参与元件。

**选择路径 D（频域阻抗扫描）当**：只有黑盒 EMT 模型、没有控制器内部参数、目标是并网变流器的 CSCR 预测或 PLL 稳定性评估、分析对象是 IBR 主导的弱电网系统。

**通用失败模式**：限幅器饱和时仍使用小信号结论；大扰动（故障、切换）触发后仍外推原工作点附近的模态；忽略数值离散引入的伪特征值；在非周期运行点做 Floquet 分析。

## 相关方法 / 相关模型 / 相关主题

**分析方法**：
- [[eigenvalue-analysis]] — 特征值分析是判断局部模态增长/衰减的数学操作
- [[modal-analysis]] — 解释特征向量、参与因子和模态形状
- [[modal-decomposition]] — 说明线性响应如何展开为多个模态的叠加
- [[generalized-eigenvalue-method]] — 处理矩阵束、DAE 或导纳矩阵中的广义特征值问题
- [[frequency-scan]] — 频域扫描是阻抗法小信号分析的核心工具

**相关页面**：
- [[small-signal-stability-analysis]] — 把本页概念转化为建模、线性化、求解和验证流程
- [[transient-stability]] — 面向大扰动后同步保持问题，不能与小信号稳定性互相替代
- [[swing-equation]] — 同步机机电振荡的物理方程，与 PSS 阻尼设计密切相关
- [[excitation-system]] — 励磁系统参数影响同步机内电动势进而影响阻尼
- [[power-system-stabilizer]] — PSS 的设计目标是增强机电振荡阻尼
- [[frequency-dependent-line-model]] — 频变线路阻抗在谐波频段可能导致负阻尼

**稳定性分析方法族**：
- [[small-signal-analysis]] — 小信号分析的理论框架
- [[impedance-stability]] — 基于阻抗的稳定性分析方法（如 Nyquist 判据）
- [[wideband-oscillation-stability]] — 宽频带振荡稳定性，覆盖次同步、超同步、谐波不稳定

## 来源论文

- [[an-automatable-approach-for-small-signal-stability-analysis-of-power-electronic-.md|Chindu 和 Kulkarni 2023]] — 提出基于 EMT 伴随电路的自动化 LTI 采样数据模型生成方法，复用 LU 因子实现零额外开销的特征值分析；支撑 buck 变换器和 STATCOM 闭环控制分析
- [[emt-model-boundary-determination-using-floquet-theory-based-participation-factor.md|Sajjadi 等 2026]] — 提出基于 Floquet 理论参与因子的 EMT 模型边界自动划分方法，单周期数据缩短 99%+，剔除 >85% 冗余状态变量
- [[an-emt-based-dynamic-frequency-scanning-tool-for-stability-analysis-of-inverter-.md|Jiang 等 2025]] — 提出基于 PSCAD/EMTDC 的自动化动态频率扫描工具，dq0 坐标系下阻抗矩阵提取，临界短路比 CSCR ≈ 3.7（电压源型 VSG）
- [[z-tool-frequency-domain-characterization-of-emt-models-for-small-signal-stabilit.md|Cifuentes Garcia 和 Beerten 2025]] — 提出开源 Z-tool 多端 AC/DC 频域识别方法，多频激励与对称性优化减少 50% 扰动次数
- [[fast-investigation-of-control-interaction-risks-in-pv-parks-using-eigenvalue-ana.md|Masoom 等 2025]] — 提出基于 Modelica DAE 自动线性化的光伏场站控制交互风险快速评估，特征值实部 >0 直接指示负阻尼风险
- [[rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability.md|Carreño 等 2026]] — 提出 RMS+ 方法增强传统电路模型以捕获 PLL 不稳定性，用于分析 IBR 并网系统的控制稳定性