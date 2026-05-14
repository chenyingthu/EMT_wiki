---
title: "构网型控制方法 (Grid-Forming Control)"
type: method
tags: [grid-forming, gfm, virtual-synchronous-machine, vsm, droop-control, black-start, vsg, cscr, weak-grid]
created: "2026-05-04"
updated: "2026-05-10"
---

# 构网型控制方法 (Grid-Forming Control)

## 1. 物理背景与工程需求

构网型控制（GFM）是电力电子变换器自主建立和维持电网电压幅值与频率的控制策略。与跟网型控制依赖 PLL 跟踪电网相位不同，GFM 在外部电网不提供参考时（孤岛、黑启动、100% 逆变器系统）仍能建立稳定交流电压。它不是单一控制算法，而是一类通过功率-频率下垂、虚拟同步机（VSG）或功率同步环（PSL）实现电压源外特性的方法集合。

GFM 在 EMT 中的工程需求覆盖四个不同场景：

1. **黑启动与孤岛运行**：光伏-电池混合电站需替代传统水电机组承担输电级黑启动电源。Nguyen (2021) 在 PSCAD/EMTDC 中验证了构网型 PV-电池电站作为 IEEE 9 节点系统黑启动电源的可行性，经 7 步 18 秒完成变压器充电、线路投切和负荷恢复
2. **弱网稳定运行**：GFM 使逆变器能在 SCR < 2 的弱电网中稳定运行。Jiang (2025) 的 EMT 动态频率扫描表明电流源型 VSG 在 SCR 高达 100 时仍保持稳定，而电压源型 VSG 的临界短路比（CSCR）约为 3.7
3. **模型选择判据**：低惯量系统中 GFM 控制时间尺度可能与线路电磁动态重叠。Misyris (2021) 推导了确保时间尺度分离的充分条件，当控制增益在边界内且 SCR ∈ [1,3] 时 RMS 模型误差 < 3%，增益越界时 RMS 预测错误率达 100%
4. **EMT 初始化**：GFM 变流器的 V/f 控制无法像跟网型那样用辅助电压源初始化。Allabadi (2024) 提出解析计算 PI 积分器初值的 CISS 方法，使 MTDC 系统初始化时间缩短 6.9 倍

## 2. 数学描述

### 2.1 P-f 下垂与 Q-V 下垂

GFM 模拟同步机外特性的基本方程（Nguyen 2021）：

$$
f_g = f_{rated} - m_p(P_{ac} - P_{ref})
$$

$$
V_g = V_{rated} - n_q(Q_{ac} - Q_{ref})
$$

$m_p$ 和 $n_q$ 为下垂系数，$f_{rated}$ 和 $V_{rated}$ 为额定值。一次下垂会产生稳态偏差，需二次 PI 补偿恢复：

$$
\Delta f_g = K_{p,f}(f_{ref} - f_g) + K_{i,f}\int(f_{ref} - f_g)dt
$$

$$
\Delta V_g = K_{p,v}(V_{ref} - V_g) + K_{i,v}\int(V_{ref} - V_g)dt
$$

最终合成参考：$f_g^* = f_{rated} - m_p(P_{ac} - P_{ref}) + \Delta f_g$，$V_g^* = V_{rated} - n_q(Q_{ac} - Q_{ref}) + \Delta V_g$。

### 2.2 VSG 摇摆方程

虚拟同步机模拟同步发电机二阶摇摆方程：

$$
J\frac{d\omega}{dt} = P_{ref} - P - D(\omega - \omega_0), \quad \frac{d\delta}{dt} = \omega - \omega_0
$$

### 2.3 功率同步环（PSL）

频率直接由有功偏差调节（Misyris 2021）：

$$
\omega_i = \omega_1 + K_p(P_{ref} - P)
$$

计及电压下垂耦合后的有功-相角开环传递函数：

$$
G_{P\theta}(s) = \frac{K_p \cdot \omega_b}{s} \cdot \frac{U_{set}U_{sc}}{|Z_g(s)|} \cdot H_{coupling}(K_q)
$$

Misyris (2021) 指出 $K_q$ 修正使相角裕度提升约 14-16°，在 SCR=1.2 时稳定性预测准确率从 62% 提升至 98%。

### 2.4 CSCR 与频域阻抗

Jiang (2025) 的 EMT 动态频率扫描通过特征值伯德图推算临界短路比：

$$
CSCR = \frac{SCR_{initial}}{|\lambda|_{180^\circ}}
$$

闭环系统传递函数：

$$
\frac{\Delta V_{PCC}}{\Delta I_{Dis}} = \frac{Z_{MMC}}{1 + Z_{MMC} \cdot Y_{ac}}
$$

## 3. 计算模型与离散化

### 3.1 GFM 控制的四层架构

| 层级 | 功能 | 时间尺度 | 实现方式 |
|------|------|---------|---------|
| 二次控制 | 稳态偏差消除，额定值恢复 | 秒级 | PI 积分补偿 |
| 一次下垂 | 功率均分，频率/电压建立 | 百毫秒级 | P-f, Q-V 下垂曲线 |
| 电压/电流外环 | dq 参考电压生成 | 数毫秒 | PI + 前馈解耦 |
| 内环调制 | PWM 开关信号 | 亚毫秒 | 载波比较或 NLM |

### 3.2 dq 坐标系下的双环控制

GFM 的下层控制与 VSC 标准 dq 矢量控制结构相同（Nguyen 2021）：外环根据参考电压和实际电压的偏差产生电流参考，内环跟踪电流并生成调制电压。区别在于 GFM 的外环参考不是由 PLL 或上层控制器设定，而是由下垂/VSG 方程自主产生。

### 3.3 GFM 初始化的两种策略（Allabadi 2024）

**CISS（稳态控制初始化）**：基于潮流相量和换流器参数解析计算外环 PI 积分器初值：

$$
h = \frac{1}{K_i} \left\{ \frac{2}{V_{dc}} \left[ \vec{V}_{PCC}^{LF} - \vec{I}_{ac} (\vec{Z}_{tr} + j\frac{X_{Larm}}{2}) \right] - |V_{ac}^{set}| \right\}
$$

**DI（解耦接口法）**：在 PCC 插入接口辅助源，将孤岛子系统与 GFM 暂时电气解耦，各自独立时域初始化后再重耦合。适用黑盒模型（内部参数不可访问）。

### 3.4 黑盒 GFM 的稳定性分析（Jiang 2025）

EMT 动态频率扫描工具（PSCAD/EMTDC）：在 PCC 注入多频正弦扰动（30 频率点、0.5% 幅值）→ DFT 提取频域响应 → dq0 坐标系阻抗/导纳矩阵 → 开环特征值伯德图 → CSCR 和振荡频率预测。

## 4. 实现方法与算法细节

### 4.1 GFM 控制策略对比

| 策略 | 核心机制 | 优势 | 关键约束 | 代表来源 |
|------|---------|------|---------|---------|
| P-f/Q-V 下垂 | 有功-频率、无功-电压线性关系 | 实现简单，多机并联自然均分 | 有静差，需二次补偿 | Nguyen 2021 |
| VSG | 二阶摇摆方程 $J\ddot{\delta} + D\dot{\delta} = \Delta P$ | 提供虚拟惯量和阻尼 | 参数 J, D 整定影响暂态 | Jiang 2025 |
| PSL | 频率 = 额定 + K_p × 有功偏差 | 时间尺度分离判据可解析推导 | 需计及 K_q 耦合修正 | Misyris 2021 |

### 4.2 RMS/EMT 模型选择条件（Misyris 2021）

| 条件 | 控制增益在边界内？ | SCR 范围 | 推荐模型 | RMS 误差 |
|------|-----------------|---------|---------|---------|
| 满足 | 是 | [1, 3] | RMS | < 3% |
| 部分满足 | 是 | > 3 | RMS 保守 | < 5% |
| 不满足 | 否（增益越界） | 任意 | EMT | 100% 误判风险 |

RMS 计算耗时较全阶 EMT 缩短 80-90%（Misyris 2021）。

### 4.3 GFM 的 CSCR 与稳定性边界（Jiang 2025）

| 控制类型 | CSCR | 失稳频率 | 强网稳定性 |
|---------|------|---------|-----------|
| 电压源型 VSG | ~3.7 | 1.05-1.15 Hz | SCR > 3.8 失稳 |
| 电流源型 VSG | < 1.2 | 无 | SCR ≤ 100 仍稳 |

电压源型 VSG：J=0.04, D=1.0, K_p=2.5, K_i=10；电流源型 VSG：H=3.42, D=5.0。

### 4.4 GFM 黑启动控制（Nguyen 2021）

1. 储能 Buck-Boost 建立直流母线电压
2. 一次下垂建立初始 f 和 V（空载）
3. 二次 PI 补偿恢复额定值
4. dq 双环调制生成 PWM
5. 按预设时序逐步投入变压器、线路和负荷（7 步/18 s）
6. 储能优先供电，超限后光伏补充

## 5. 适用边界与失效模式

### 适用条件

- 需要电压源外特性的孤岛、弱网（SCR < 2）或黑启动场景
- 含高比例 GFM 的低惯量系统需确认 RMS 模型的时间尺度分离条件（Misyris 2021）
- GFM 初始化可用 CISS（参数透明模型）或 DI（黑盒模型）（Allabadi 2024）
- 黑盒 GFM 的稳定性可用 EMT 动态频率扫描评估（Jiang 2025）

### 失效模式

| 失效场景 | 原因 | 后果 |
|----------|------|------|
| 功率过载 | GFM 容量小于负荷或故障需求 | 电压崩溃，频率跌落 |
| 直流电压失稳 | 储能或光伏无法支撑功率平衡 | 换流器闭锁 |
| RMS 误判 | 控制增益越界但使用 RMS 仿真 | 将发散振荡误判为稳定（Misyris 2021）|
| 初始化冲突 | 辅助电压源强制误差为零致积分器初值错误 | 启动后长时间暂态（Allabadi 2024）|
| 多 GFM 环流 | 并联 GFM 下垂特性不一致 | 无功环流，功率不均分 |
| PI 限流器导致失稳 | 电压源型 VSG 在强网下因限流器失稳 | SCR > 3.8 时振荡（Jiang 2025）|
| 黑启动保护配合不足 | 变压器励磁涌流或线路充电过电压 | 保护误动，黑启动失败 |

### 关键约束

- Nguyen (2021) 的 GFM 黑启动控制基于 IEEE 9 节点 PSCAD 仿真，不自动覆盖其他拓扑、保护配合或多 GFM 并列
- Misyris (2021) 的充分条件是针对 PSL 和 VSG 外环推导的，内环假设已快速收敛；条件不满足不意味着 RMS 必然失效，但不再保证可靠
- Allabadi (2024) 的 CISS 依赖 GVSC 平均值模型参数和 V/f 控制结构，DI 虽然不需要内部参数但仍需理解外部控制模式
- Jiang (2025) 的 CSCR 和动态频率扫描基于小扰动假设——强非线性、限幅器频繁动作或大扰动时结论不能直接外推

## 6. 应用案例

### 案例 1：光储 GFM 电站黑启动（Nguyen 2021）

场景：改进型 IEEE 9 节点系统，Bus 1 部署含 PV 和储能的构网型电站作为黑启动电源。一次下垂 + 二次 PI 恢复 + dq 双环调制。全过程 18 秒 7 步，依次投入变压器、线路和负荷（Step 6 最大 120.2 MW + 42.3 Mvar）。频率在 0-5 s 空载阶段有微小波动，负荷投入后稳定在 60 Hz。储能先供电，5 s 后光伏补充。稳态电压幅值与数值优化解偏差 < 1%，辅助负荷投切后电压恢复 < 0.2 s。

### 案例 2：GFM 控制增益的 RMS/EMT 模型选择边界（Misyris 2021）

场景：低惯量系统含 GFM VSC，SCR 范围 1.0-3.0。通过 PSL/VSG 外环传递函数推导时间尺度分离充分条件，并用 PM ≥ 45°、GM ≥ 6dB 为边界。条件满足时 RMS 模型评估有功平衡的动态误差 < 3%，计算耗时较 EMT 降低约 87%。增益越界时 RMS 将实际振荡发散误判为渐近稳定，预测错误率 100%。含 K_q 耦合修正的传递函数使 PM 提升 14-16°。在 SCR=1.2 弱网下稳定性预测准确率从 62%（未计 K_q）提升至 98%（计及 K_q）。

### 案例 3：GVSC 的 EMT 初始化方法（Allabadi 2024）

场景：CIGRE BM4 多端直流基准模型，含 3 个互联 HVDC 系统。CISS 方法通过潮流相量和换流器参数解析计算外环 PI 积分器初值 h，DI 方法通过接口辅助源实现黑盒模型的独立初始化。两种方法均将系统初始化时间缩短 6.9 倍（10 μs 步长，EMTP）。传统辅助电压源法因 GVSC 误差信号被强制为零致积分器初值错误，切除辅助源后出现长时间暂态振荡；CISS 和 DI 完全消除该问题。

### 案例 4：VSG 的 CSCR 与稳定性分析（Jiang 2025）

场景：270 MVA MMC（±150 kV，20 SM/臂），PSCAD/EMTDC 动态频率扫描。电压源型 VSG 的 CSCR ≈ 3.7，失稳振荡频率 1.05-1.15 Hz（频率扫描预测 vs 根轨迹法误差 < 2.7%），SCR 从 3.6 阶跃至 3.8 后约 10 s 出现持续有功振荡。电流源型 VSG 在 SCR=1.2 至 100 的宽范围内均保持稳定，无需 PI 限流器。dq0 坐标系扫描（30 频率点，0.5% 扰动幅值）有效消除 abc 域正负序频率耦合，阻抗矩阵非对角元素可忽略。

## 7. 延伸阅读

- [[droop-control]]：GFM 一次下垂控制的基础方法
- [[phase-locked-loop]]：GFM 与 GFL 的核心区别在 PLL 的依赖程度
- [[vsc-control]]：GFM 的双环 dq 矢量控制骨架
- [[vector-control]]：GFM 内环电流/电压控制所用数学工具
- [[gfl-inverter-model]]：弱电网定义及对 GFM 控制的影响
- [[average-value-model]]：GFM 系统级研究可替代详细开关模型
- [[gfm-inverter-model]]：黑启动场景是 GFM 的重要应用
- [[virtual-synchronous-generator]]：VSG 的详细建模
- [[small-signal-stability]]：GFM 小信号稳定性分析的方法背景
- [[impedance-modeling]]：与 Jiang (2025) 动态频率扫描的阻抗视角关联

*页面基于 Nguyen (2021)、Misyris (2021)、Allabadi (2024) 和 Jiang (2025) 的证据写作。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i|Control and Simulation of a Grid-Forming Inverter for Hybrid]] | 2021 |
| [[grid-forming-converters-sufficient-conditions-for-rms-modeling|Grid-forming converters: Sufficient conditions for RMS model]] | 2021 |
| [[initializing-emt-models-of-grid-forming-vscs-in-mtdc-systems|Initializing EMT models of grid forming VSCs in MTDC systems]] | 2024 |
| [[an-emt-based-dynamic-frequency-scanning-tool-for-stability-analysis-of-inverter-|An EMT based dynamic frequency scanning tool for stability a]] | 2025 |
