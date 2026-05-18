---
title: "小信号分析方法 (Small-Signal Analysis)"
type: method
tags: [small-signal, eigenvalue, modal-analysis, linearization, stability, ibr, pll, impedance]
created: "2026-05-13"
updated: "2026-05-19"
---

# 小信号分析方法 (Small-Signal Analysis)

## 定义与边界

小信号分析（Small-Signal Analysis）是在给定稳态运行点附近对非线性动态系统做线性化处理，用状态空间特征值、参与因子、频率响应或阻抗判据解释小扰动稳定性的技术路线。其输入包括：稳态运行点（潮流解或 EMT 稳态解）、状态变量和代数变量初值、控制器参数（PLL 带宽、电流环 PI、环流控制等）、网络等值参数（短路比、等效阻抗）、扰动信号的幅值和频谱；输出包括：特征值 $\lambda_i=\sigma_i+j\omega_i$、阻尼比 $\zeta_i$、振荡频率 $f_i$、参与因子矩阵 $\mathbf{P}$、模态形状（右特征向量）、参数灵敏度 $S_{k,i} = \partial \lambda_i / \partial p_k$。

**边界约束**：小信号分析只解释运行点附近的小扰动稳定性（$\Delta x / x_0 \ll 1$）。故障穿越、限流、闭锁、保护跳闸、大幅度开关瞬态需要 EMT 时域仿真单独验证，不能用线性化结论推断。开关频率附近的谐波耦合模态需用多频动态相量（DP）才能保留，用基波相量模型会遗漏。

**与其他页面的关系**：本页是 [[small-signal-stability]] 的**方法论入口**，不是稳定性结论的汇总。[[eigenvalue-analysis]] 关注特征值计算算法的数值实现；[[state-space-method]] 关注状态空间表达本身；[[impedance-measurement]] 关注端口阻抗的频域/时域辨识；[[wideband-oscillation-stability]] 是应用主题页，汇总小信号、阻抗和 EMT 时域三类证据之间的联系。

## EMT 中的角色

在 EMT 语境中，小信号分析把时域波形中观察到的振荡、控制耦合和弱阻尼现象**归因到模型结构**：

- 对 VSC、MMC、LCC-HVDC、DFIG、PMSG 和储能变流器做控制链路线性化，识别 PLL 带宽、电流环截止频率、外环响应速度和环流控制模态之间的交互
- 对 SSO（次同步振荡）、SSTI（次同步扭矩相互作用）和宽频振荡（10 Hz ~ 10 kHz）提供频率-阻尼-参与变量的定量解释
- 用 EMT 小扰动注入 + [[prony-analysis]] 或 [[fft]] 校核特征值预测的频率和阻尼比是否与时域响应一致
- 为控制器带宽整定、阻抗重塑和 FACTS/HVDC 阻尼辅助控制设计提供方向性证据

**关键约束**：若线性模型基于平均值模型（AVM），应说明省略了哪些开关边带谐波；若线性模型基于黑箱量测（EMT 扫频），应说明注入扰动幅值是否小到不触发限幅、PWM 饱和或保护动作。

## 核心机制

### 线性化数学框架

对非线性动态系统：

$$\dot{x} = f(x, u), \quad y = g(x, u)$$

在运行点 $(x_0, u_0)$ 处满足 $f(x_0, u_0) = 0$，一阶泰勒展开得到：

$$\Delta\dot{x} = A\Delta x + B\Delta u, \quad \Delta y = C\Delta x + D\Delta u$$

其中雅可比矩阵为：

$$A = \left.\frac{\partial f}{\partial x}\right|_{(x_0, u_0)}, \quad B = \left.\frac{\partial f}{\partial u}\right|_{(x_0, u_0)}$$
$$C = \left.\frac{\partial g}{\partial x}\right|_{(x_0, u_0)}, \quad D = \left.\frac{\partial g}{\partial u}\right|_{(x_0, u_0)}$$

### 特征值与阻尼

矩阵 $A$ 的特征值 $\lambda_i = \sigma_i + j\omega_i$ 决定小扰动响应的模态衰减/增长：

$$\sigma_i < 0 \Rightarrow \text{模态衰减（稳定）}, \quad \sigma_i > 0 \Rightarrow \text{模态增长（不稳定）}$$

振荡频率为 $f_i = \omega_i / (2\pi)$ Hz。阻尼比：

$$\zeta_i = \frac{-\sigma_i}{\sqrt{\sigma_i^2 + \omega_i^2}}$$

典型工程要求：本地机电模态 $\zeta > 0.05$，区域间模态 $\zeta > 0.03$，电力电子控制模态 $\zeta > 0.05 \sim 0.10$（取决于扰动持续时间）。

### 参与因子与模态归属

参与因子矩阵 $P_{ki} = \phi_{ki} \cdot \psi_{ki}$，其中 $\phi$ 是右特征向量分量，$\psi$ 是左特征向量分量。第 $k$ 状态变量在第 $i$ 模态上的参与因子越大，说明该变量对该模态的响应越强。参与因子是结构信息，不是因果证明——需与参数灵敏度、时域扰动或阻抗分析联合解释。

## 五条分析路线

### 路线一：解析线性化（Analytical Linearization）

直接对状态方程和控制器微分方程求偏导得到 $A, B, C, D$。

**优点**：雅可比矩阵元素有物理含义（时间常数、增益、耦合导纳），便于参数灵敏度分析和控制器重设计。

**典型流程**：
1. 写出并网 VSC 的 d/q 轴电流方程 + PLL 动态 + 直流电压方程 + 电网等值方程
2. 在指定运行点（$P_0, Q_0, V_g, SCR$）处令微分项为零，求解平衡点
3. 对每个状态变量求偏导，得到 $5\times5$ 或 $7\times7$ 的状态矩阵
4. 求特征值、阻尼比和参与因子

**适用**：VSC-HVDC、并网逆变器、DFIG 机组、储能变流器的解析小信号模型

**代表论文**：Fan & Miao (2021) 对 Type-3 风电场 SSO 建立了解析阻抗模型；Chindu & Kulkarni (2023) 将 EMT 伴随电路框架复用于自动化 LTI 模型生成

### 路线二：数值线性化（Numerical Linearization）

不对解析方程求偏导，而是用有限差分或自动微分（AD）对可重复求解的 EMT 模型函数做数值线性化。

**优点**：不需要知道模型内部结构，适用于黑箱商业模型、FPGA 硬件在环（HIL）和复杂 EMT 子网络。

**关键参数**：扰动幅值 $\epsilon$ 的选择需平衡数值精度和触发非线性的风险；推荐 $\epsilon \approx 10^{-6} \sim 10^{-4}$ pu

**典型流程**：
1. 将 EMT 模型在稳态运行点上做 $n$ 次小扰动（每次改变一个输入端口）
2. 采集 $n$ 次扰动响应的时间序列
3. 用最小二乘法或伪逆法拟合状态空间矩阵 $\{\hat A, \hat B, \hat C, \hat D\}$
4. 验证拟合残差 $\|\Delta x - \hat A\Delta x - \hat B\Delta u\| < \delta$

**代表论文**：Chindu & Kulkarni (2023) 的 EMT 伴随电路方法，无需手工建立状态空间，直接从 EMT 节点方程生成 LTI sampled-data 模型

### 路线三：EMT 扫频/扰动辨识（Frequency-Domain Identification）

在 EMT 仿真中向端口注入小信号扰动（单音正弦、PRBS 或 Gaussian 脉冲），测量端口电压/电流响应，构建端口导纳/阻抗矩阵。

**导纳矩阵提取**：
$$Y_{pq}(j\omega) = \frac{I_p(j\omega)}{V_q(j\omega)}\bigg|_{V_r=0, r\neq q}$$

**稳定性判据**（阻抗比法）：
$$Z_o(j\omega) / Z_{grid}(j\omega) \quad \text{的奈奎斯特判据}$$
或等效的行列式判据 $\det(I - Y_{grid}\cdot Z_{IBR}) \neq 0$ 在右半平面

**PRBS 扰动设计**（Cifuentes 2026 Z-Tool）：
- 频带宽度：$\Delta f = 1/T_{PRBS}$，分辨率 $f_s/N_{bits}$
- 幅值设计：$A_{PRBS}$ 需保证 SNR > 20 dB 但不触发限幅
- 注入方式：直流端口叠加电流扰动、交流端口叠加电压扰动

**Gaussian 脉冲扰动**（Cifuentes 2023）：
$$v_g(t) = A \cdot e^{-(t-t_0)^2/(2\sigma^2)} \cdot \cos(2\pi f_c t)$$
带宽由 $\sigma$ 控制，中心频率 $f_c$ 可调

**代表论文**：Zhou & Shen (2025) 的动态频率扫描工具；Cifuentes (2023) 的 Gaussian 脉冲 IBR dq 导纳提取

### 路线四：动态相量线性化（Dynamic Phasor Linearization）

将开关周期平均后的状态变量表示为复数相量，保留 $k$ 次谐波阶次：

$$\bar{x}_k(t) = \frac{1}{T_s}\int_t^{t+T_s} x(\tau) e^{-jk\omega_s\tau}d\tau$$

对 MMC、LCC 和多脉波整流器，动态相量模型可保留 3、5、7 次等特征谐波的耦合动态，用状态矩阵的块结构表示。

**谐波状态空间（HSS）表示**：

$$\Delta\dot{\bar{x}}_k = A_k\Delta\bar{x}_k + \sum_{m\neq k}A_{km}\Delta\bar{x}_m + B_k\Delta u$$

其中 $A_k$ 是第 $k$ 阶谐波的子矩阵，$A_{km}$ 是 $k\neq m$ 时的耦合子矩阵。

**适用场景**：MMC 内部谐波动态、LCC 换相过程、SVG/STATCOM 的 2、3 次谐波注入检测

### 路线五：时域模态辨识（Time-Domain Modal Identification）

从 EMT 小扰动仿真波形中用信号处理方法直接提取模态参数。

**Prony 分析**：
$$y(t) = \sum_{i=1}^{N} A_i e^{\sigma_i t}\cos(\omega_i t + \phi_i)$$
从等间距采样序列中估计 $\sigma_i, \omega_i, A_i$。

**Yule-Walker AR 模型**：
$$y[n] = -\sum_{k=1}^{p}a_k y[n-k] + e[n] \Rightarrow \text{特征多项式根给出模态参数}$$

**Relpron / EFDD**：对噪声鲁棒，适合从含噪 EMT 输出中识别 3-5 个主导模态

**窗口长度权衡**：窗口太短 $\Rightarrow$ 低频模态阻尼估计偏差大；窗口太长 $\Rightarrow$ 混入非线性控制和运行点漂移。推荐窗口覆盖 5-10 个目标振荡周期。

## 关键技术挑战

### 挑战一：开关谐波导致分段线性化

IGBT/二极管的开通和关断使系统在每个开关周期内产生两次状态切换。严格来说，系统是分段线性时变（PWLTV）的，而非 LTI。处理方式有两种：

1. **平均化等效**：用开关周期平均（SSA/GSSA）消除开关切换，得到连续的 LTI 模型，但会丢失开关边带谐波（$\pm f_{sw}, \pm 2f_{sw}$ 等）
2. **谐波状态空间（HSS）**：保留 $N$ 个边带谐波分量，状态矩阵扩展为 $N\times N$ 块对角加耦合项，矩阵维数随保留谐波数 $N$ 增大

**典型边界**：开关频率 1-20 kHz、谐波范围 0-20 kHz 时，若只保留基波相量，10-50 Hz 的控制模态可能被遗漏或衰减常数估计错误。

### 挑战二：PLL 与电网动态的强耦合

PLL 跟踪 PCC 电压相位，其带宽（通常 5-20 Hz）在弱电网条件下与局部模态（0.5-2 Hz）和区域间模态（0.1-0.8 Hz）重叠。PLL 动态在 d/q 变换中与电流环耦合，在小信号模型中表现为 $A$ 矩阵的条件数增大（病态矩阵），特征值对参数敏感。

**PLL 带宽与稳定性的矛盾**（据 Chindu 2023 推断）：PLL 带宽太窄 $\Rightarrow$ 快速暂态下失锁；PLL 带宽太宽 $\Rightarrow$ 引入负电阻，在弱电网中引发 20-100 Hz 振荡。典型整定范围：$f_{PLL} \in [5, 15]$ Hz，SCR < 2 时上限取 5 Hz。

### 挑战三：弱电网等值的不确定性

规划阶段常用戴维南等值（$Z_{th} = R_{th} + jX_{th}$）代表远端网络，但 $R_{th}/X_{th}$ 比值和 $X_{th}$ 随运行方式变化可达 3 倍。相同控制器参数在强电网（SCR > 5）和弱电网（SCR < 2）下可能分别产生正阻尼和负阻尼。

**量化边界**（据 Fan 2021 和 Chindu 2023 的测试结果推断）：
- SCR > 3：大多数控制器参数配置可保证 $\zeta > 0.05$
- SCR 2-3：需要精细整定，阻尼比对 PLL 带宽和电流环截止频率敏感
- SCR < 2：即使小幅参数变化也可能使 $\sigma$ 从负变正，引发 SSO

### 挑战四：IBR 低电压穿越（LVRT）期间的模型切换

LVRT 期间 IBR 从最大功率点跟踪（MPPT）切换到恒功率控制（C恒定）或恒流控制，同时触发电流限幅。限幅使控制环路退出线性区，小信号分析结论失效。

**处理策略**：
1. 在 EMT 中先仿真 LVRT 暂态，记录电流和电压轨迹
2. 分析限幅持续时间和退出后的运行点漂移
3. 用分段线性化（PWL）描述限幅非线性，用描述函数近似其等效增益
4. 验证限幅期间是否出现谐波不稳定（10-50 Hz 带外增益突变）

### 挑战五：多机多控制器的交互模态识别

多台 IBR 并联或多回 HVDC 共走走廊时，控制交互可能导致**全局振荡模态**（所有机组在同一频率上振荡），而非单台机组的本地模态。

**识别方法**：
- 参与因子矩阵 $\mathbf{P}$ 的行方向聚类：若 $\{\phi_{ki}\}_{k\in\text{IBR}_j}$ 构成同一簇，则第 $i$ 模态是机组群 $j$ 的本地模态
- 模态参与因子差的阈值：$\sum_k |P_{ki} - P_{kj}|$ 用于判定两个模态是否可合并

## 量化性能边界

| 性能指标 | 典型范围 | 说明 |
|---------|---------|------|
| 线性化精度（特征值实部） | $\|\Delta\sigma\| < 0.1$ rad/s | 在 0.1-1 Hz 振荡频率带 |
| 线性化精度（振荡频率） | $\|\Delta f\| < 0.05$ Hz | 1-10 Hz 控制模态 |
| 参与因子识别误差 | $\|\Delta P_{ki}\| < 0.1$ | 对主导模态 |
| 阻抗测量 SNR 要求 | > 20 dB | 避免噪声伪峰 |
| PRBS 最小长度 | $T_{PRBS} > 10 T_{osc}$ | 低频模态辨识 |
| Gaussian 脉冲宽度 | $\sigma \cdot f_c \in [0.5, 2]$ | 频带覆盖目标频率 |
| 特征值计算复杂度 | $O(n^3)$（稠密矩阵） | $n$ = 状态维数 |

**EMT 伴随电路自动线性化**（Chindu 2023）：在 EMT 仿真运行到稳态后，自动注入 $N$ 个小扰动并采集响应，生成 LTI 状态空间模型。无需手工建立状态方程，不需要知道控制器内部结构。量化精度：$\Delta f_i < 0.1$ Hz，$\Delta\zeta_i < 0.02$，对 PLL 参与模态的识别正确率 > 90%。

**dq 导纳提取**（Cifuentes 2023）：Gaussian 脉冲注入法在单次时域仿真中同步获取多个频点响应，相比逐频点正弦注入（需 50-100 次独立仿真），节省约 90% 的计算时间。导纳提取误差在 0.1-500 Hz 范围内 < 5%。

**动态相量 vs 开关平均值模型**：对 MMC，保留 3 次谐波的 DP 模型（3×7 状态）与开关平均值模型（7 状态）的特征值差异：在 0.1-10 Hz 范围内 $\Delta\sigma < 0.05$ rad/s，10-100 Hz 范围内差异增大至 $\Delta\sigma \approx 0.5$ rad/s（据 Zhu 2006/Huang 2016 推断，具体数值因 MMC 子模块数而异）。

**稳定性边界量化**（Fan 2021）：Type-3 风电场 SSO 风险在 $R_{th}/X_{th} > 0.4$ 且 PLL 带宽 > 10 Hz 时显著上升；在相同电网条件下，将 PLL 带宽从 15 Hz 降至 8 Hz 可将阻尼比从 $\zeta \approx -0.02$ 提升至 $\zeta \approx 0.08$（具体数值因风电场聚合台数和短路比而异，引用时应注明系统参数）。

## 适用边界与选择指南

| 分析目标 | 推荐路线 | 原因 |
|---------|---------|------|
| 控制参数整定（已知模型结构） | 路线一（解析线性化） | 偏导数有物理含义，可做灵敏度分析 |
| 商业 IBR 黑箱模型稳定性评估 | 路线二或路线三（数值/扫频） | 不需要模型内部参数 |
| 谐波耦合振荡分析（MMC/LCC） | 路线四（动态相量） | 保留开关边带和谐波阶次 |
| 现场测试数据校核 | 路线五（时域模态辨识） | 直接处理实测波形 |
| 大规模系统初步扫描 | 路线二 + 模态参与因子聚类 | 计算量可控，适合批量分析 |

**不适用场景**：
- 故障穿越期间（限幅非线性触发）
- 开关动作瞬态（分段线性而非 LTI）
- 大扰动后系统进入新的稳定运行点（原运行点线性化无效）
- 谐波不稳定（> 2 kHz）的 EMT 时域验证需单独进行

## 相关页面

- [[eigenvalue-analysis]] — 特征值计算的数值实现细节
- [[state-space-method]] — 状态空间表达是线性化的载体
- [[impedance-measurement]] — 端口阻抗/导纳的时域和频域辨识
- [[frequency-scan]] — 扫频辨识的工程实践
- [[prony-analysis]] — EMT 波形模态辨识的信号处理算法
- [[fft]] — 频率分析的快速算法
- [[pll-model]] — PLL 是 IBR 小信号模态的核心参与对象
- [[vsc-model]] — 并网 VSC 的控制链路小信号分析
- [[mmc-model]] — MMC 的谐波耦合和环流控制模态
- [[dfig-model]] — DFIG 机组的 SSO 和 SSTI 模态归属
- [[wideband-oscillation-stability]] — 宽频振荡是应用主题页
- [[small-signal-stability]] — 电力系统小信号稳定主题页
- [[harmonic-analysis]] — 谐波分析工具（10-50 次谐波与次同步振荡的区分）

## 来源论文

- Chindu & Kulkarni (2023) — EMT 伴随电路自动化小信号分析（路线一+二），IEEE Trans. Power Delivery
- Fan & Miao (2021) — Type-3 风电场 SSO 解析建模与稳定性边界（路线一）
- Cifuentes (2023) — Gaussian 脉冲 IBR dq 导纳提取（路线三）
- Zhou & Shen (2025) — EMT 动态频率扫描工具（路线三）
- Zhu et al. (2006) — 动态相量 HVDC 混合仿真（路线四）
- Huang & Vittal (2016) — EMT-TS 混合仿真与小信号验证（路线四）
- Jalili-Marandi et al. (2009) — TS/EMT 接口技术框架（路线一参考）