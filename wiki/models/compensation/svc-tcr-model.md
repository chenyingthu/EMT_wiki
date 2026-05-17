---
title: "晶闸管控制电抗器模型 (SVC-TCR Model)"
type: model
tags: [svc, tcr, model, facts, reactive-power, thyristor, harmonic]
created: "2026-04-29"
updated: "2026-05-17"
---

# 晶闸管控制电抗器模型 (SVC-TCR Model)

## 定义与边界

TCR（Thyristor-Controlled Reactor）是 SVC（Static Var Compensator）的核心功率支路，由两个反并联晶闸管与线性电抗器串联构成。TCR 通过控制触发角 $\alpha$ 改变等效基波电纳，实现感性无功的连续调节，其无功调节范围为 $0$（完全关断）至 $Q_{\max}$（完全导通）。

TCR 单独不产生容性无功，必须与固定电容器（FC）或晶闸管投切电容器（TSC）配合才能提供从感性到容性的双向无功调节能力。[[svc-model]] 给出 SVC 整机模型的完整边界；[[thyristor-control]] 给出触发角、导通角、自然关断和半控器件的通用约束。

**物理结构**：三相 TCR 通常接成三角形（Δ），以消除三次谐波的环流。Δ 连接的单相 TCR 支路在正负半周对称触发，只产生奇次谐波（$6k\pm1$ 次：5、7、11、13…）。

## EMT 建模对象

TCR 在 EMT 中至少需要定义以下建模对象：

- **反并联晶闸管对**：触发脉冲生成、导通角控制、电流自然过零关断、正向阻断恢复特性。
- **电抗器**：线性电感 $L$ 或考虑饱和非线性特性的模型，以及杂散电阻 $R$。
- **触发同步**：母线电压过零检测或 PLL 输出；触发角约定（以电压过零点为基准还是以相角为基准）。
- **控制输入**：触发角指令 $\alpha$ 或等效电纳参考 $B_{\mathrm{ref}}$，经查表或计算产生触发脉冲。
- **保护接口**：过流保护阈值、过压抑制、晶闸管结温估算和闭锁逻辑。

**触发角约定**是 TCR 建模中最容易出错的细节：同一 $\alpha$ 值在不同零点定义下（电压过零 vs 相角起点）对应完全不同的导通角和等效电纳，必须在模型文档中明确声明。

## 模型结构与接口变量

### 时域电路方程

TCR 支路的时域电路方程基于分段线性RL电路：

$$\frac{di_L}{dt} = \frac{v_s(t)}{L}, \quad \text{晶闸管导通期间}$$

$$\frac{di_L}{dt} = 0, \quad \text{晶闸管关断期间}$$

其中 $v_s(t)$ 为支路端电压，$i_L$ 为电抗器电流。导通期间电流由电压积分上升；关断期间支路电流为零。

### 基波等效电纳公式

TCR 的基波等效电纳是触发角 $\alpha$（从电压过零点起算，$\alpha \in [90^\circ, 180^\circ]$）的函数：

$$B_{\mathrm{TCR}}(\alpha) = \frac{2(\pi - \alpha) + \sin 2\alpha}{\pi X_L}$$

其中 $X_L = \omega L$ 为电抗器基波电抗。推导过程：将 TCR 电流波形分解为傅里叶级数，提取基波分量得到。

导通角 $\sigma = 2(\pi - \alpha)$，则等效电纳可写为：

$$B_{\mathrm{TCR}}(\sigma) = \frac{\sigma - \sin\sigma}{\pi X_L}$$

当 $\alpha = 90^\circ$（完全导通）时，$B_{\mathrm{TCR}} = 1/X_L$；当 $\alpha = 180^\circ$（完全关断）时，$B_{\mathrm{TCR}} = 0$。

### TCR 谐波电流公式

TCR 电流中含大量低次谐波，$h$ 次谐波电流幅值与触发角的关系为 (Zhijun 2009 引用 Mathur & Varma)：

$$I_h(\alpha) = \frac{V}{hX_L} \cdot \frac{4}{\pi} \left[ \frac{\sin(h+1)\alpha}{2(h+1)} - \frac{\sin(h-1)\alpha}{2(h-1)} + \frac{\cos\alpha \sin h\alpha}{h} \right]$$

其中 $V$ 为系统电压基波幅值。**特征谐波分布**：
- 6 脉动 TCR（60°基频）：$6k\pm1$ 次（5、7、11、13…）
- 12 脉动 TCR：$12k\pm1$ 次（11、13、23、25…）

七次及以上谐波对 TCR 动态特性影响较小 (Zhijun 2009)，因此 DP 模型中通常只保留基波和五次谐波。

### 受控电纳简化模型

将 TCR 写为随 $\alpha$ 变化的等效导纳（基波等效）：

$$I_{\mathrm{TCR}} = j B_{\mathrm{TCR}}(\alpha) \cdot V$$

此简化模型只保留基波分量，不能反映谐波电流与滤波器之间的交互效应。

## 动态相量建模方法

### 动态相量理论基础

动态相量（Dynamic Phasor, DP）方法基于时变傅里叶系数，将时域波形 $x(\tau)$ 在时间窗口 $\tau \in [t-T, t]$ 上展开为：

$$x(\tau) = \sum_{k=-\infty}^{\infty} X_k(t) e^{jk\omega_s \tau}$$

其中 $\omega_s = 2\pi/T$ 为基波角频率，$X_k(t)$ 为第 $k$ 次谐波的时变相量系数。**两个核心性质** (Zhijun 2009)：

**性质1** — 相量的微分：

$$\frac{dX_k}{dt} = \left\langle \frac{dx}{dt} \right\rangle_k - jk\omega_s X_k$$

**性质2** — 两个时域波形乘积的相量：

$$\langle xy \rangle_k = \sum_{m=-\infty}^{\infty} \langle x \rangle_m \langle y \rangle_{k-m}$$

这两个性质使得非线性开关电路（如 TCR）的状态方程可以在相量域中线性表达。

### TCR 动态相量模型推导

单相 TCR 的电路方程为：

$$C \frac{dv}{dt} = i_l - i, \quad L \frac{di_l}{dt} = s \cdot v$$

其中 $s$ 为开关函数：$s=1$（晶闸管导通）时，$v$ 施加于电抗器；$s=0$（晶闸管关断）时，$i_l=0$。

应用动态相量性质，将实部和虚部分离，得到 $k$ 次谐波的状态方程 (Zhijun 2009, 式(9)-(12))：

$$C \frac{dV_k^R}{dt} - k\omega_s C V_k^I = I_{lk}^R - I_k^R$$

$$C \frac{dV_k^I}{dt} + k\omega_s C V_k^R = I_{lk}^I - I_k^I$$

$$L \frac{dI_k^R}{dt} - k\omega_s L I_k^I = \sum_{m} [S_m^R V_{k-m}^R - S_m^I V_{k-m}^I] + [S_m^R V_{k-m}^R + S_m^I V_{k-m}^I]$$

$$L \frac{dI_k^I}{dt} + k\omega_s L I_k^R = \sum_{m} [S_m^R V_{k-m}^I + S_m^I V_{k-m}^R] - [S_m^R V_{k-m}^I - S_m^I V_{k-m}^R]$$

其中 $S_k$ 为开关函数的 $k$ 次相量，由触发角 $\alpha$ 和导通角 $\sigma$ 决定。

### 开关函数动态相量

触发延迟角 $\alpha$ 和导通角 $\sigma = 2(\pi-\alpha)$ 取决于 SVC 闭环控制，在每个 TSP 积分步更新。开关函数的各次相量为 (Zhijun 2009, 式(13)-(14))：

$$S_0 = \frac{1}{T} \int_{t-T}^{t} s(\tau) d\tau = \frac{\sigma}{\pi}$$

$$S_m = \frac{1}{T} \int_{t-T}^{t} s(\tau) e^{-jm\omega_s \tau} d\tau = \frac{1}{m\pi} [\sin m(\alpha+\sigma) - \sin m\alpha] + j\frac{1}{m\pi}[\cos m\alpha - \cos m(\alpha+\sigma)]$$

### 滤波器 RLC 电路的动态相量模型

在 Zhijun 2009 中，RLC 滤波器电路被分解为 RL 电路和电容串联。电容的 DP 模型为：

$$C \frac{dV_{2,k}^R}{dt} = I_k^R - k\omega_s C V_{2,k}^I$$

$$C \frac{dV_{2,k}^I}{dt} = I_k^I + k\omega_s C V_{2,k}^R$$

## 混合仿真接口

### TSP-DP 混合仿真框架

在 SVC DP 混合仿真中，电力系统被分割为 TSP 子系统和 SVC DP 子系统，通过接口 bus 连接。接口协议为 (Zhijun 2009)：

1. 在接口时刻 $T_k$，基于 TSP 子系统的状态建立 SVC 外部网络诺顿等效电路（含电流源 $I_{\mathrm{eq}}$ 和等效导纳 $Y_{\mathrm{eq}}$）。
2. 在 DP 子系统中用大步长（如 $0.001\,\mathrm{s}$）积分 $N$ 步（如20步）。
3. 计算诺顿等效的实时功率 $P$、$Q$ 并返回 TSP：
$$P = V_1^R I_1^R + V_1^I I_1^I, \quad Q = -V_1^R I_1^I + V_1^I I_1^R$$
4. TSP 子系统用标准大步长（如 $0.01$–$0.02\,\mathrm{s}$）完成一步积分。

### 等效电路参数计算

诺顿等效电路参数在每个接口时刻 $T_k$ 根据外部子系统状态更新：

$$I_{\mathrm{eq}} = I_{\mathrm{eq}}^R + jI_{\mathrm{eq}}^I, \quad Y_{\mathrm{eq}} = \frac{1}{R_{\mathrm{eq}} + j\omega L_{\mathrm{eq}}}$$

### 接口算法关键问题

Zhijun 2009 指出的接口算法三个关键问题：

- **相位不连续**：传统 TSP-EMTP 混合中等效电路的相位不连续和直流偏移是主要误差源；DP 模型使用单相等效电路和解析开关函数可避免此问题。
- **计算效率**：DP 子系统步长 $0.001\,\mathrm{s}$ 远大于 EMTP 的 $50\,\mu\mathrm{s}$，计算效率提升约 200–400 倍。
- **精度验证**：DP 混合仿真结果与 DCG/EMTP 全电磁暂态基准高度一致。

## 建模层级与选择决策

| 层级 | 保留内容 | 适合问题 | 边界 |
|------|----------|----------|------|
| 详细晶闸管开关模型 | 反并联晶闸管导通/关断、电抗器电流、触发脉冲、自然过零 | 谐波分析、投切暂态、阀级应力验证 | 小步长（<10μs），参数依赖器件资料 |
| 动态相量模型 | 基波和若干低次（1、5、7次）谐波相量、触发角动态 | 混合仿真、系统级动态、谐波交互研究 | 依赖谐波截断阶数和周期稳态假设 |
| 基波等效电纳模型 | $B_{\mathrm{TCR}}(\alpha)$、限幅和响应延迟 | 潮流计算、电压无功规划、粗略系统研究 | 不验证谐波、阀级暂态和滤波器交互 |

[[dynamic-phasor]] 给出 TCR 谐波相量的完整建模方法；[[average-value-model]] 给出基波等效电纳的降阶边界；[[thyristor-control]] 给出触发同步和半控器件约束。

## 量化性能边界

### DP 混合仿真性能（Zhijun 2009）

**E Zhijun (2009)** 在 IEEE 9 节点和 New England 39 节点系统中验证了 SVC DP 混合仿真方法：

- **步长提升**：积分步长从 EMTP 的 $50\,\mu\mathrm{s}$ 提升至 TSP 兼容的 $0.01$–$0.02\,\mathrm{s}$，加速约 **200–400 倍**。
- **精度验证**：SVC DP 模型的电压/电流波形与 DCG/EMTP 全电磁暂态基准结果高度一致。
- **接口质量**：接口处未出现传统 TSP-EMTP 混合常见的相位不连续与直流偏移。
- **模型配置**：TCR 建模为单相 DP 模型，保留基波和 5 次谐波相量（7 次及以上忽略对精度影响极小）。

该结论基于自研 DP 程序与 DCG/EMTP 的对比验证。

### HIL 实时仿真性能（Le-Huy 2023）

**Le-Huy (2023)** 在 Hydro-Québec La Verendrye 735 kV 变电站 SVC 改造项目的 HIL 实时仿真中，对比了两种建模路径：

| 仿真路径 | 步长 | 波形重合度 | 动态响应偏差 | 稳态电压调节误差 |
|----------|------|-----------|-------------|----------------|
| 小步长 EMT | $3\,\mu\mathrm{s}$ | > **99%** | < **0.5%** | < **0.2%** |
| 常规大步长 EMT | $32.5521\,\mu\mathrm{s}$（512点/60Hz周波） | > **99%** | < **0.5%** | < **0.2%** |

- **拓扑配置**：VSC 支路 70 Mvar/支路，TSC 支路 95 Mvar/支路，总补偿容量 +330/-110 Mvar。
- **小步长约束**：RTS 小步长模式仅支持最多 30 个单相节点、6 个标准 Ron/Roff 开关，其余需用 Pejovic 开关。
- **寄生元件影响**：小步长模式中的 stub 线和 Pejovic 开关引入额外 $L=90\,\mu\mathrm{H}$、$C=239\,\mathrm{nF}$ 等寄生元件，对 TSC 支路电流有 40A 量级的影响，验证时需纳入。

### TCR 谐波特性（理论公式）

基于谐波电流公式，不同触发角下的特征谐波幅值理论分布为：

| 触发角 $\alpha$ | 导通角 $\sigma$ | 5次谐波占比 | 7次谐波占比 | 11次谐波占比 |
|----------------|----------------|------------|------------|------------|
| $90^\circ$ | $180^\circ$（全导通） | 0 | 0 | 0 |
| $105^\circ$ | $150^\circ$ | ~9.5% | ~6.5% | ~4.2% |
| $120^\circ$ | $120^\circ$ | ~14.5% | ~12.3% | ~7.8% |
| $150^\circ$ | $60^\circ$ | ~19.2% | ~12.8% | ~4.3% |

触发角越大（轻载），谐波含量越高。在大触发角工况下不能仅靠基波公式评估滤波效果。

## 关键技术挑战

1. **触发角约定歧义**：同一 $\alpha$ 值在不同零点定义下（电压过零 vs 相角起点）对应完全不同的导通角和等效电纳。模型文档必须明确声明触发角基准，否则相同 $\alpha$ 在不同模型中可能对应完全不同的系统响应。

2. **谐波截断阶数选择**：Zhijun (2009) 保留基波+5次谐波在标准算例中有效，但在高补偿度或强非线性工况下（如 $\alpha > 150^\circ$）是否需要更高阶截断（如7次）缺乏系统研究。开放问题：通用截断阶数选择准则是否存在？

3. **TCR 与滤波器谐振风险**：在轻载大 $\alpha$ 工况下，TCR 谐波含量显著增加；高电缆充电功率系统中 TCR 与滤波器可能激发谐振，需在 EMT 中单独验证。

4. **弱网 SCR<3 下的 PLL 交互**：弱网条件下 PLL 同步误差和 TCR 触发同步的交互对等效电纳精度的影响缺乏系统评估。PLL 动态可能使等效电纳出现周期性波动。

5. **矩阵指数积分法的开关事件定位**：Li (2020) 提出了基于矩阵指数积分与密集输出公式的 EMT 框架，在 TCR 电路中验证了 L 稳定求解器对开关事件的处理能力，但与传统插值方法缺乏同条件系统对比。

## 适用边界与失败模式

- **触发角约定必须明确**：同一 $\alpha$ 值若零点定义不同，等效电纳结果完全不同。
- **TCR 单独不产生容性无功**：不能替代 STATCOM 或 TSC 在低电压下的无功支撑能力。
- **谐波含量随触发角增大而增加**：大 $\alpha$（轻载）工况下滤波器配置可能不足，不能只靠基波公式评估滤波效果。
- **基波等效电纳模型不能反映**：自然关断过程、晶闸管正向恢复电压、触发失败时的不对称电流。
- **TCR 与系统阻抗谐振风险**：含滤波器和高电缆充电功率的系统应单独验证。
- **SVC 整体响应受多因素影响**：测量延迟、触发同步、TCR/TSC 协调均影响 SVC 端口特性，TCR 单支路模型不能替代 SVC 端口响应验证。

## 验证需求

TCR 模型验证应覆盖：

- **电纳-触发角曲线**：触发角扫描下等效电纳与理论公式 $B_{\mathrm{TCR}}(\alpha)$ 一致性检验。
- **谐波谱验证**：TCR 电流谐波谱（各次谐波幅值随 $\alpha$ 的变化）与理论谐波公式交叉验证。
- **动态响应时间**：触发角阶跃或无功指令阶跃下的响应时间与实验数据对比。
- **不对称触发**：三相 TCR 在不对称触发或母线三相不平衡下的电流和中性点偏移。
- **SVC 端口特性**：与 FC/TSC 配合后的电压调节斜率、谐波放大和滤波器分组投切。

## 相关页面

- [[svc-model]]：SVC 整机模型，TCR 是 SVC 的核心功率支路。
- [[facts]]：FACTS 设备家族入口。
- [[reactive-compensation-device]]：无功补偿设备族入口。
- [[thyristor-control]]：触发同步和半控器件边界。
- [[statcom-model]]：VSC 型并联补偿，TCR 不能替代 STATCOM 的低电压无功能力。
- [[dynamic-phasor]]：TCR 动态相量建模方法。
- [[average-value-model]]：基波等效电纳的降阶边界。

## 来源论文

| 论文 | 年份 | 可支撑内容 |
|------|------|-----------|
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model]] E Zhijun 等 | 2009 | SVC-DP 混合仿真：单相 DP 模型、基波+5次谐波、200-400倍步长提升 |
| [[hybrid-svc-vsc-modeling-approaches-for-hardware-in-the-loop-simulation]] P. Le-Huy, O. Tremblay | 2023 | 混合 SVC-VSC HIL：两种步长路径对比、>99%波形重合度、寄生元件影响分析 |
| [[interpolation-for-power-electronic-circuit-simulation-revisited-with-matrix-expo]] Li 等 | 2020 | 矩阵指数 TCR 仿真框架、L 稳定求解器 |
| Mathur & Varma, *Thyristor-based FACTS Controllers*, Wiley 2002 | 2002 | TCR 基波电纳公式、谐波电流公式（引用来源） |