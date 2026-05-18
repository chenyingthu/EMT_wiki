---
title: "静止无功补偿器模型 (SVC Model)"
type: model
tags: [svc, model, facts, reactive-power, thyristor, tcr, tsc, voltage-control]
created: "2026-05-02"
updated: "2026-05-17"
---

# 静止无功补偿器模型 (SVC Model)

## 定义与边界

SVC（Static Var Compensator，静止无功补偿器）是并联接入交流母线的晶闸管型动态无功补偿装置，通过调节晶闸管控制电抗器（TCR）和晶闸管投切电容器（TSC）的等效电纳，实现母线电压调节和无功功率交换。典型 SVC 由 TCR 支路、TSC 支路、固定电容器/滤波器、测量控制系统和保护组成。

EMT 模型应解释 TCR/TSC 如何改变等效电纳、谐波和电压响应，而不是把 SVC 简化为无条件快速且精确的理想无功源。本页讨论 SVC 作为 FACTS 并联补偿设备的模型。TCR 触发和半控器件边界见 [[models/compensation/svc-tcr-model]]；VSC 型并联补偿比较见 [[models/compensation/statcom-model]]。

## EMT 建模对象

SVC 的 EMT 对象至少包括四类：

**TCR 支路**：反并联晶闸管、电抗器、触发角 $\alpha$（从电压过零点算起的电角度）、导通角 $\sigma = \pi - \alpha$、以及电流自然过零关断特性。TCR 产生谐波，滤波器参数和系统阻抗影响谐波放大。

**TSC 支路**：反并联晶闸管、电容器、阻尼元件、残压检测和零电压/低涌流投切逻辑。TSC 投切受电压相位、残压和电流过零约束，平均电纳模型不能替代涌流验证。

**滤波支路**：5 次、7 次、高通或 C 型滤波器，具体配置必须绑定工程设计或论文来源。

**控制系统**：母线电压测量、斜率特性（$V_{\text{ref}}$ + 电压-电流 droop）、电纳参考、TCR/TSC 协调、限幅和死区。

## 模型结构与接口变量

### TCR 基波等效电纳

TCR 的基波等效电纳是触发角的函数。触发角 $\alpha$ 定义为从电压过零点到触发脉冲的电角度，导通角 $\sigma = \pi - \alpha$。基波电流的有效值与导通角的关系为：

$$\sigma = \pi - \alpha$$

TCR 支路的基波电流有效值为：

$$I_{\text{TCR}} = \frac{V}{\omega L}\left(2\pi - 2\alpha - \sin 2\alpha\right)$$

对应的基波等效电纳为：

$$B_{\text{TCR}}(\alpha) = \frac{I_{\text{TCR}}}{V} = \frac{2}{\omega L}\left(\pi - \alpha + \frac{\sin 2\alpha}{2}\right)$$

其中 $\alpha \in [\pi/2, \pi]$，当 $\alpha = \pi/2$ 时 $\sigma = \pi/2$，TCR 全导通，感性和容性无功相当；当 $\alpha \to \pi$ 时 $\sigma \to 0$，TCR 近乎开路，无功输出趋近于零。

### TSC 投切电纳

TSC 支路以离散组数投入运行，每组电容固定。设 TSC 投入 $k$ 组（$k = 0, 1, 2, \ldots, N_{\text{TSC}}$），每组电纳为 $B_{\text{TSC}}$，则总 TSC 电纳为：

$$B_{\text{TSC}} = k \cdot B_{\text{TSC},k}$$

TSC 的残压检测确保在电压过零点附近触发，避免涌流。投切逻辑通常设置电压滞环：低于 $V_{\text{lo}}$ 时投入，高于 $V_{\text{hi}}$ 时切除。

### 总等效电纳与无功输出

总 SVC 等效电纳为 TCR 电纳与 TSC 电纳之和：

$$B_{\text{SVC}} = B_{\text{TCR}}(\alpha) + B_{\text{TSC}}$$

对应的无功功率为：

$$Q_{\text{SVC}} = -B_{\text{SVC}} \cdot V^2$$

其中符号约定：容性电纳产生容性无功（$Q < 0$），感性电纳消耗感性无功（$Q > 0$）。

### SVC 电压控制斜率特性

工程 SVC 采用斜率特性控制，避免多装置之间争抢同一电压目标：

$$B_{\text{ref}} = K_p \left(V_{\text{ref}} - V\right) + K_i \int \left(V_{\text{ref}} - V\right) dt$$

电压 droop 斜率 $K_{\text{droop}}$ 将电压偏差转换为等效电纳参考值：

$$V = V_{\text{ref}} + \frac{Q_{\text{SVC}}}{K_{\text{droop}}}$$

## EMT 建模层级

SVC 的 EMT 模型按精度-效率分为四个层级：

| 层级 | 步长 | 加速比 | 保留内容 | EMT 用途 | 失效场景 |
|------|------|--------|----------|----------|----------|
| 详细晶闸管模型 | 5–50 μs | 1× | 阀状态、触发脉冲、自然关断、TSC 残压、滤波器、保护 | 投切暂态、谐波、HIL 实时 | 计算量较高，参数依赖工程配置 |
| 动态相量模型 | 0.5–2 ms | 20–50× | 基波电纳、5 次谐波相量、控制延迟 | 混合仿真、低频振荡、系统级动态 | 开关尖峰和阀级应力被弱化 |
| 平均电纳模型 | 2–10 ms | 50–200× | $B_{\text{SVC}}(\alpha)$、PI 控制、限幅 | 机电暂态接口、潮流初始化 | 不能验证谐波、投切涌流和保护动作 |
| 稳态导纳模型 | 10–100 ms | 200–500× | $B_{\text{SVC}}$ 限幅、电压 droop | 稳态分析、规划筛选 | 任何暂态分析 |

## 关键技术挑战

### 挑战 1：TCR 谐波与滤波器设计

TCR 的半控特性使其产生 5 次、7 次、11 次、13 次等特征谐波。这些谐波与系统阻抗交互可能引发谐波放大，甚至谐波谐振。谐波电流的幅值与导通角相关：

$$I_{\text{TCR},h} = \frac{V}{\omega L} \cdot \frac{2\pi - 2\alpha + \sin 2\alpha + \sin(2\alpha)\cos(h\alpha)}{h\pi}$$

其中 $h = 3, 5, 7, 11, 13$。滤波器设计需要在容性无功补偿与谐波抑制之间取得平衡，且滤波器参数与系统短路容量密切相关。

### 挑战 2：TSC 投切涌流与残压管理

TSC 每次投切都需要在电压过零点触发，以限制涌流峰值。残压（电容器上残留电荷形成的电压）必须在投切前通过放电电阻消散至 5%–10% 额定电压以下。EMT 模型需要准确捕捉以下瞬态过程：

- 投切瞬态的电流尖峰（可达稳态电流的 5–10 倍）
- 电压与电流的相位突变
- 滤波器与 TSC 之间的谐振交互

### 挑战 3：多运行点等效阻抗的非线性

SVC 的等效阻抗随触发角 $\alpha$ 连续变化。在大扰动（电压跌落/故障清除）期间，TCR 从一个运行点跃变至另一个运行点，固定 $Z_{\text{th}}$ 模型在过渡过程中失效。正确的等效需要多运行点采样或实时更新 $B_{\text{TCR}}(\alpha)$。

### 挑战 4：弱电网条件下的电压控制稳定性

在弱电网（SCR < 3）中，SVC 的控制响应可能与系统阻抗形成负阻尼交互，引发低频振荡。触发角控制的响应时间（约 5–10 ms）慢于 VSC 型 STATCOM（约 1–2 ms），在严重电压跌落时可能无法提供足够的无功支撑。

## 量化性能边界

SVC EMT 模型在仿真精度和计算效率方面已有可核验的量化结果，但以下数据均绑定具体装置拓扑、控制结构和仿真条件，不能外推为通用能力：

| 指标 | 数值 | 来源 | 条件 |
|------|------|------|------|
| HIL 波形重合度 | > **99%** | Le-Huy 2023 | 小步长(<5 μs) vs 常规大步长(~32 μs)，La Verendrye 混合 SVC-VSC |
| HIL 动态响应偏差 | < **0.5%** | Le-Huy 2023 | 同上测试条件 |
| 稳态电压调节误差 | < **0.2%** | Le-Huy 2023 | 同上测试条件 |
| 混合仿真步长加速比 | **200–400×** | E Zhijun 2009 | 50 μs → 0.01–0.02 s（DP 方法） |
| DP 模型精度 | 基波 + 5 次谐波保留 | E Zhijun 2009 | IEEE 9 节点和 39 节点验证 |
| 快速等效计算复杂度 | O(4N) vs O(N²) | Zhang 2019 | 大功率链式 STATCOM（含 SVC 型拓扑） |
| Pejovic 等效开关 | Req = 2L/ΔT + ΔT/(2C) | Le-Huy 2023 | 每小步长任务限 6 个标准 Ron/Roff 开关，其余用 Pejovic 模型 |
| MMCsim 接口刷新周期 | **32.5521 μs** | Le-Huy 2023 | 512 点/60 Hz 周波 |
| TCR 最低特征谐波 | 17/19 次 | Kosterev 2004 | 18 脉波 VSC 规划模型，不适用开关级研究 |
| 电容储能时间常数 | τ = **0.5 s** | Kosterev 2004 | 12.5 kV/10 MVA, 5 kV 直流, 200 μF 电容 |

## 适用边界与失效模式

- **平均值模型**无法反映 PWM 谐波、死区效应、直流侧纹波和保护动作所需的瞬时电流——这些是 SVC 与 VSC 型补偿的根本区别。
- **TSC 投切**受电压相位、残压和电流过零约束；平均电纳模型不能替代涌流验证。
- **低电压期间** SVC 输出随电压下降，故障期间不应按额定无功恒定注入外推。
- **触发同步错误**、PLL/过零检测误差或三相不平衡会导致非特征谐波和不对称电流。
- **ELST 方法**仅适用于外部电力系统可表示为线性网络、非线性主要来自 PV 发电机单二极管模型的场景——该判据来自 Di Fazio 2012，对 SVC 的适用性需额外验证。
- **弱网稳定结论**必须绑定短路比、控制参数、扰动幅值、运行点和模型层级；不能从一个 SVC 算例外推到所有 FACTS 装置。

## 与相关页面的关系

- [[models/compensation/reactive-compensation-device]]：无功补偿设备族入口。
- [[models/compensation/statcom-model]]：VSC 型并联补偿，低电压支撑能力和控制响应速度均优于 SVC，但成本更高。
- [[models/compensation/svc-tcr-model]]：TCR 支路的更细模型入口，含触发角、导通角和半控关断机制。
- [[methods/control/thyristor-control]]：触发角、自然关断和半控器件通用边界。
- [[topics/hvdc-facts/facts]]：FACTS 设备的系统角色，不替代单设备 EMT 模型。
- [[models/converter/vsc-model]]：STATCOM 的主电路和调制接口上位模型。
- [[models/converter/pwm-modulator-model]]：详细或插值型 PWM 表示的边界。
- [[models/control/pll-model]]：并网同步环节，弱网和故障期间的关键风险来源。
- [[methods/system-studies/dynamic-phasor]]：动态相量理论是 SVC EMT-TS 混合仿真的接口基础。

## 来源论文

- [[hybrid-svc-vsc-modeling-approaches-for-hardware-in-the-loop-simulation|Le-Huy & Tremblay 2023]] — 提出 La Verendrye 735 kV 混合 SVC-VSC 的 HIL 实时仿真方法。两种建模路径（小步长 <5 μs vs 常规大步长 ~32 μs）波形重合度 >99%，动态响应偏差 <0.5%，稳态电压误差 <0.2%。给出了 MMCsim 接口刷新周期 32.5521 μs 和 Pejovic 等效开关参数公式。
- [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model|E Zhijun et al. 2009]] — 提出基于动态相量理论的 SVC 单相等效模型，用于 TSP-EMT 混合仿真。步长从 50 μs 提升至 0.01–0.02 s（200–400 倍加速），保留基波和 5 次谐波，在 IEEE 9 和 39 节点系统中验证。

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*