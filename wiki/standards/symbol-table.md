---
title: "EMT Wiki 符号表 (Symbol Table)"
type: standards
created: "2026-05-10"
updated: "2026-05-10"
---

# EMT Wiki 符号表

本表定义 EMT Wiki 全站的符号使用规范，覆盖标量、向量、矩阵、相量、算子等各类数学对象的字体和记号规则。所有 wiki 页面应遵循此标准，确保跨页面阅读一致性。

## 字体与格式规则

| 类别 | 规则 | LaTeX | 示例 |
|------|------|-------|------|
| 标量 | 斜体 | `$x$` | $v$, $i$, $t$, $h$, $L$, $C$ |
| 向量 | 粗体小写 | `$\mathbf{x}$` | $\mathbf{v}$, $\mathbf{i}$, $\mathbf{x}$ |
| 矩阵 | 粗体大写 | `$\mathbf{Y}$` | $\mathbf{Y}$, $\mathbf{Z}$, $\mathbf{A}$ |
| 相量 | 大写加点 | `$\dot{V}$` | $\dot{V}$, $\dot{I}$ |
| 估计值 | hat | `$\hat{x}$` | $\hat{x}$, $\hat{\theta}$ |
| 平均值 | langle/rangle | `$\langle x \rangle$` | $\langle x \rangle$ |
| 共轭 | star 上标 | `$V^*$` | $V^*$, $\mathbf{Y}^*$ |
| 转置 | T 上标 | `$\mathbf{A}^{\mathsf{T}}$` | $\mathbf{A}^{\mathsf{T}}$ |
| 复数幅值 | 绝对值符号 | `$|V|$` | $|V|$, $|I|$ |
| 虚数单位 | 直体 j | `$\mathrm{j}$` | $\mathrm{j}$（禁用 $i$） |
| 微分算子 | 直体 d | `$\mathrm{d}$` | $\mathrm{d}t$, $\mathrm{d}x$ |
| 偏微分 | 直体 \partial | `$\partial$` | $\partial x/\partial t$ |

## 通用符号

### 时间与步长

| 符号 | 含义 | 禁用 | 说明 |
|------|------|------|------|
| $t$ | 时间 | | 连续时间变量 |
| $h$ 或 $\Delta t$ | 仿真步长 | $\delta t$, $T_s$ | $T_s$ 留给采样周期 |
| $t_n$ | 第 $n$ 个时间点 | | $t_n = t_0 + nh$ |
| $t_{\text{sim}}$ | 仿真总时长 | | |
| $\tau$ | 传播时延 / 时间常数 | | 上下文区分 |

### 电气量

| 符号 | 含义 | 说明 |
|------|------|------|
| $v(t)$, $i(t)$ | 瞬时电压、电流 | 时域 |
| $\dot{V}$, $\dot{I}$ | 相量电压、电流 | 频域稳态 |
| $\mathbf{v}$, $\mathbf{i}$ | 电压、电流向量 | 多相或多节点 |
| $p(t)$, $q(t)$ | 瞬时有功、无功功率 | |
| $P$, $Q$ | 有功、无功功率（平均值） | |
| $S$ | 视在功率 | $S = P + \mathrm{j}Q$ |
| $\omega$ | 角频率 | $\omega = 2\pi f$ |
| $\omega_s$ | 额定角频率 | $= 2\pi f_s$，禁用 $\omega_0$、$\omega_{\text{base}}$ |
| $f$ | 频率 (Hz) | |
| $f_s$ | 额定频率 (Hz) | 通常 50 或 60 |
| $\phi$ | 相位角 | |

### 电路参数

| 符号 | 含义 | 说明 |
|------|------|------|
| $R$ | 电阻 | |
| $L$ | 电感 | |
| $C$ | 电容 | |
| $G$ | 电导 | $G = 1/R$ |
| $Z$ | 阻抗 | $Z = R + \mathrm{j}X$ |
| $Y$ | 导纳 | $Y = G + \mathrm{j}B$ |
| $Z_c$ | 特征阻抗 | 线路波阻抗 |
| $\Gamma$ | 传播常数 | $\Gamma = \alpha + \mathrm{j}\beta$ |
| $\alpha$ | 衰减常数 | |
| $\beta$ | 相位常数 | $\beta = \omega/v_p$ |
| $v_p$ | 相速度 | |
| $\rho$ | 反射系数 | |

## 状态空间与伴随电路

| 符号 | 含义 | 说明 |
|------|------|------|
| $\mathbf{x}$ | 状态向量 | |
| $\mathbf{u}$ | 输入向量 | |
| $\mathbf{y}$ | 输出向量 | |
| $\mathbf{A}$, $\mathbf{B}$, $\mathbf{C}$, $\mathbf{D}$ | 状态空间矩阵 | $\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}$ |
| $\mathbf{Y}_n$ | 节点导纳矩阵 | EMTP 求解 |
| $\mathbf{Y}_n \mathbf{v}_n = \mathbf{i}_n$ | 节点方程 | |
| $G_{\text{eq}}$ | 等效电导 | 伴随电路 |
| $I_{\text{hist}}$ | 历史电流源 | 伴随电路 |
| $\mathbf{G}$ |  nodal 电导矩阵 | |
| $\mathbf{I}_{\text{hist}}$ | 历史电流源向量 | |

## 数值方法

| 符号 | 含义 | 说明 |
|------|------|------|
| $\phi(z)$ | 指数积分器的 $\phi$ 函数 | $\phi_0(z)=e^z$, $\phi_1(z)=(e^z-1)/z$ |
| $\mathbf{\varphi}_k(h\mathbf{A})$ | 矩阵 $\phi$ 函数 | $k$ 阶 |
| $R(z)$ | 稳定函数 | 数值积分方法的稳定性特征 |
| $R(\infty)$ | 无限远稳定函数值 | $0 \to$ L 稳定, $-1 \to$ 振荡 |
| $a$ | DIRK 系数 | 2S-DIRK: $a = 1-1/\sqrt{2}$ |
| $c_i$ | RK 方法的节点系数 | |
| $k_i$ | RK 方法的阶段导数 | |
| $\lambda$ | 特征值 | test equation $\dot{x} = \lambda x$ |
| $z$ | 离散域变量 | $z = h\lambda$ |
| $s$ | 复频率 | Laplace 域 |

## 输电线路与 Bergeron 模型

| 符号 | 含义 | 说明 |
|------|------|------|
| $Z_c$ | 特征阻抗 | $Z_c = \sqrt{L/C}$ |
| $\tau$ | 传播时延 | $\tau = l/v_p$ |
| $v_p$ | 相速度 | $v_p = 1/\sqrt{LC}$ |
| $l$ | 线路长度 | |
| $I_k(t-\tau)$ | Bergeron 历史电流源 | 端 $k$ 在时刻 $t-\tau$ |
| $\mathbf{Z}_c$ | 特征阻抗矩阵 | 多导体 |
| $\mathbf{P}$ | 传播矩阵 | 多导体 |
| $\mathbf{T}_v$, $\mathbf{T}_i$ | 电压/电流模态变换矩阵 | 相域 $\leftrightarrow$ 模域 |
| $\Gamma(\omega)$ | 频变传播常数 | |
| $\mathbf{Y}_c(\omega)$ | 频变特征导纳 | |
| $\mathbf{Z}_{\text{int}}(\omega)$ | 频变内部阻抗 | 土壤/集肤效应 |
| $R_{\text{dc}}$ | 直流电阻 | |
| $R_{\text{ac}}(\omega)$ | 交流电阻（集肤效应） | |

## 电力电子与 MMC

| 符号 | 含义 | 说明 |
|------|------|------|
| $S(t)$ | 开关函数 | $S \in \{0, 1\}$ |
| $d(t)$ | 占空比 | $0 \leq d \leq 1$ |
| $f_{\text{sw}}$ | 开关频率 | |
| $m_a$ | 调幅比 | PWM |
| $m_f$ | 调频比 | PWM |
| $V_{\text{dc}}$ | 直流母线电压 | |
| $V_{\text{ref}}$ | 参考电压 | |
| $N$ | MMC 子模块数/电平数 | |
| $C_{\text{sm}}$ | 子模块电容 | |
| $L_{\text{arm}}$ | 桥臂电抗 | |
| $R_{\text{arm}}$ | 桥臂电阻 | |
| $i_{\text{arm}}$ | 桥臂电流 | |
| $i_{\text{circ}}$ | 环流 | 二倍频分量 |
| $v_{\text{sm}}$ | 子模块电容电压 | |
| $\mathbf{Y}_{\text{eq}}$ | MMC 等效导纳矩阵 | DEM |
| $v_{\text{crit}}$ | 起晕电压阈值 | 电晕 |
| $f_c(|v|)$ | 电晕增量电容函数 | |

## 混合仿真与接口

| 符号 | 含义 | 说明 |
|------|------|------|
| $T_s$ | 采样周期 | 混合仿真接口 |
| $T_{\text{EMT}}$ | EMT 侧步长 | 通常 $\mu$s 级 |
| $T_{\text{TS}}$ | 机电暂态侧步长 | 通常 ms 级 |
| $\mathbf{Z}_{\text{eq}}$ | 接口等值阻抗 | FDNE 或戴维南 |
| $\mathbf{Y}_{\text{eq}}(\omega)$ | 频变等值导纳 | FDNE |
| $p_i$ | FDNE 极点 | $i = 1, \ldots, N_p$ |
| $r_i$ | FDNE 留数 | $i = 1, \ldots, N_p$ |
| $d$ | FDNE 直通项 | |
| $\mathbf{Y}_{\text{FDNE}}(s)$ | FDNE 导纳函数 | $\sum_i r_i/(s-p_i) + d$ |
| $K$ | 接口插值阶数 | |

## 动态相量与信号处理

| 符号 | 含义 | 说明 |
|------|------|------|
| $\langle x \rangle (t)$ | 动态相量 | 基频包络 |
| $X_k(t)$ | 第 $k$ 阶动态相量 | $k = 0, \pm 1, \pm 2, \ldots$ |
| $\mathcal{H}\{v\}$ | Hilbert 变换 | 解析信号构造 |
| $v_a(t)$ | 解析信号 | $v_a = v + \mathrm{j}\mathcal{H}\{v\}$ |
| $V(\omega)$ | 频谱 | Fourier 变换 |
| $V(j\omega)$ | 频域响应 | |
| $\hat{x}(t)$ | 移频信号 / 估计值 | 上下文区分 |
| $\omega_s$ | 移频角频率 | SFA 的参考频率 |
| $T_w$ | 滑动窗宽度 | DP 计算 |

## 参考坐标系与变换

| 符号 | 含义 | 说明 |
|------|------|------|
| $v_a$, $v_b$, $v_c$ | 三相瞬时值 | abc 坐标系 |
| $v_\alpha$, $v_\beta$ | $\alpha\beta$ 坐标系分量 | Clarke 变换 |
| $v_d$, $v_q$ | $dq$ 坐标系分量 | Park 变换 |
| $v_0$, $v_1$, $v_2$ | 零/正/负序分量 | 对称分量法 |
| $\theta$ | 变换角 / 转子角 | |
| $\delta$ | 功角 | |

## 下标规范

| 下标 | 含义 | 示例 |
|------|------|------|
| d, q | dq 坐标系 | $v_d$, $i_q$ |
| $\alpha$, $\beta$ | $\alpha\beta$ 坐标系 | $v_\alpha$, $i_\beta$ |
| 0, 1, 2 | 零/正/负序 | $V_0$, $V_1$, $V_2$ |
| ref | 参考值 | $v_{\text{ref}}$ |
| err | 误差 | $v_{\text{err}}$ |
| max, min | 最大/最小 | $v_{\text{max}}$, $v_{\text{min}}$ |
| avg | 平均 | $v_{\text{avg}}$ |
| rms | 有效值 | $V_{\text{rms}}$ |
| hist | 历史源 | $I_{\text{hist}}$ |
| eq | 等效 | $G_{\text{eq}}$, $R_{\text{eq}}$ |
| crit | 临界值 | $v_{\text{crit}}$ |
| L, C, R | 元件标识 | $G_L$, $I_{\text{hist},C}$ |
| arm | 桥臂 | $i_{\text{arm}}$, $L_{\text{arm}}$ |
| circ | 环流 | $i_{\text{circ}}$ |
| sm | 子模块 | $C_{\text{sm}}$, $v_{\text{sm}}$ |
| dc | 直流侧 | $V_{\text{dc}}$ |
| ac | 交流侧 | $V_{\text{ac}}$ |
| nom | 额定值 | $V_{\text{nom}}$ |
| in, out | 输入/输出 | $v_{\text{in}}$, $v_{\text{out}}$ |

## 特殊算子与函数

| 符号 | 含义 | LaTeX |
|------|------|-------|
| $\mathrm{j}$ | 虚数单位 | `$\\mathrm{j}$` |
| $\mathrm{e}$ | 自然常数 | `$\\mathrm{e}$` |
| $\mathcal{L}\{\cdot\}$ | Laplace 变换 | `$\\mathcal{L}\\{\\cdot\\}$` |
| $\mathcal{F}\{\cdot\}$ | Fourier 变换 | `$\\mathcal{F}\\{\\cdot\\}$` |
| $\mathcal{H}\{\cdot\}$ | Hilbert 变换 | `$\\mathcal{H}\\{\\cdot\\}$` |
| $\mathbb{E}[\cdot]$ | 期望 | `$\\mathbb{E}[\\cdot]$` |
| $\|\mathbf{x}\|$ | 范数 | `$\\|\\mathbf{x}\\|$` |
| $\mathbf{A}^{\mathsf{T}}$ | 矩阵转置 | `$\\mathbf{A}^{\\mathsf{T}}$` |
| $\mathbf{A}^{-1}$ | 矩阵逆 | `$\\mathbf{A}^{-1}$` |
| $\mathbf{A}^{\dagger}$ | Moore-Penrose 伪逆 | `$\\mathbf{A}^{\\dagger}$` |
| $\otimes$ | Kronecker 积 | `$\\otimes$` |
| $\odot$ | Hadamard 积 | `$\\odot$` |
| $\nabla$ | 梯度算子 | `$\\nabla$` |
| $\partial$ | 偏微分算子 | `$\\partial$` |

## 缩写

| 缩写 | 全称 |
|------|------|
| EMT | 电磁暂态 (Electromagnetic Transient) |
| EMTP | 电磁暂态程序 (Electromagnetic Transients Program) |
| DAE | 微分代数方程 (Differential-Algebraic Equation) |
| ODE | 常微分方程 (Ordinary Differential Equation) |
| SFA | 移频分析 (Shifted Frequency Analysis) |
| DP | 动态相量 (Dynamic Phasor) |
| DEM | 详细等效模型 (Detailed Equivalent Model) |
| AVM | 平均值模型 (Average-Value Model) |
| FDNE | 频变网络等值 (Frequency-Dependent Network Equivalent) |
| VF | 矢量拟合 (Vector Fitting) |
| MMC | 模块化多电平换流器 (Modular Multilevel Converter) |
| VSC | 电压源换流器 (Voltage Source Converter) |
| LCC | 电网换相换流器 (Line-Commutated Converter) |
| HVDC | 高压直流输电 (High Voltage Direct Current) |
| MTDC | 多端直流 (Multi-Terminal DC) |
| DIRK | 对角隐式 Runge-Kutta (Diagonally Implicit Runge-Kutta) |
| CDA | 临界阻尼调整 (Critical Damping Adjustment) |
| HIL | 硬件在环 (Hardware-in-the-Loop) |
| MATE | 多区域 Thévenin 等效 (Multi-Area Thévenin Equivalent) |
| MOR | 模型降阶 (Model Order Reduction) |
| SVD | 奇异值分解 (Singular Value Decomposition) |

---

*本符号表与 `academic-polish-guidelines.md`、`mathematical-notation.md` 配合使用。新建页面应优先查表确保符号一致性。*
