---
title: "锁相环方法 (Phase-Locked Loop)"
type: method
tags: [phase-locked-loop, pll, synchronization, inverter-control, grid-following, dsogi]
created: "2026-05-04"
updated: "2026-05-10"
---

# 锁相环方法 (Phase-Locked Loop)

## 1. 物理背景与工程需求

跟网型（Grid-Following, GFL）换流器通过锁相环（PLL）从并网点电压提取同步相位和频率，作为 dq 坐标变换和控制参考的基础。PLL 的性能直接影响换流器并网控制的稳定性，尤其在弱电网、故障和不平衡工况下。

PLL 在 EMT 中的工程需求包括：

1. **同步角生成**：为 GFL 的 dq 电流内环和功率外环提供同步旋转坐标基准
2. **弱网失稳分析**：PLL 与电网阻抗交互在小信号和小扰动下可能导致同步失稳（Carreño 2026）
3. **故障穿越**：电网故障时 PLL 需快速准确跟踪相位，否则影响换流器控制响应（Ranasinghe 2024）
4. **系统小干扰稳定性**：PLL 参数与换流器控制器参数共同影响交直流系统模态与稳定裕度（贺永杰 2026）
5. **高频谐振评估**：PLL 的带宽和延时在高频段贡献负电阻特性，与交流线路分布电容互动（Guo 2022）

## 2. 数学描述

### 2.1 SRF-PLL 基本结构

同步旋转坐标系 PLL（SRF-PLL）是最常见的同步方法。三相电压经 Clarke 变换到 $"αβ$ 静止坐标，再经 Park 变换到 dq 旋转坐标。在锁相状态下，q 轴电压分量为零：

$$
v_q = \frac{2}{3}[v_a \sin\theta + v_b \sin(\theta-120^\circ) + v_c \sin(\theta+120^\circ)] = 0
$$

PLL 的闭环控制将 $v_q$ 作为误差信号，通过 PI 调节器调整估计频率，再积分得到相角：

$$
\dot{\theta}_{pll} = \omega_{pll} = \omega_0 + K_p v_q + K_i \int v_q dt
$$

其中 $\omega_0$ 为额定同步频率，$K_p$、$K_i$ 为 PI 参数。

### 2.2 相位误差与同步误差

$$
\theta_{err} = \theta_{grid} - \theta_{pll}
$$

在小信号范围内，当 $\theta_{err}$ 较小时有 $\sin(\theta_{err}) \approx \theta_{err}$，闭环传递函数近似为二阶系统。同步误差受电网强度（SCR）、故障类型和控制参数共同决定。

### 2.3 弱网下 PLL 动态与 di/dt 耦合

Carreño (2026) 指出，传统 RMS 模型因删除电感 $di/dt$ 效应无法捕捉 PLL 与网络阻抗交互失稳。PLL 通过电压相角影响 dq 电流参考方向，电流变化经网络电感产生电压变化，再反馈至 PLL 输入——此闭环在弱电网低 SCR 下可能失稳。保留该机制需将 PLL 动态（慢子系统）与电磁暂态（快子系统）的耦合保留在降阶模型中。

## 3. 计算模型与离散化

### 3.1 SRF-PLL 的离散时间实现

每个 EMT 时间步 $n$ 的 PLL 计算流程：

```text
1. 测量三相电压 v_abc(n)
2. Clarke 变换: v_αβ = T_clarke · v_abc
3. Park 变换: v_dq = T_park(θ_pll(n)) · v_αβ
4. 误差计算: v_q_err = v_q - v_q_ref (通常 v_q_ref = 0)
5. PI 更新: ω_pll(n+1) = ω_0 + K_p·v_q_err + K_i·∫v_q_err dt
6. 积分得相角: θ_pll(n+1) = θ_pll(n) + h·ω_pll(n+1)
```

### 3.2 DSOGI-PLL 的正交信号生成

双二阶广义积分器 PLL（DSOGI-PLL）在 $\alpha\beta$ 坐标系中通过两个正交信号发生器（SOGI）提取电压基波正序分量，在不平衡和谐波工况下提供更干净的同步信号：

$$
\text{SOGI 传递函数: } \frac{v'}{v}(s) = \frac{k\omega' s}{s^2 + k\omega' s + \omega'^2}
$$

其中 $k$ 为阻尼因子，$\omega'$ 为 SOGI 的谐振频率。DSOGI 需要从 PLL 反馈当前频率估计 $\omega_{pll}$ 作为 $\omega'$ 输入——此耦合在扰动时形成反馈链：频率估计摆动 $\to$ SOGI 滤波偏移 $\to$ 相位误差增大 $\to$ 频率更剧烈摆动。

### 3.3 PLL 参数对系统稳定性的影响

贺永杰 (2026) 在 LCC-HVDC 改进动态相量模型中，将 PLL 参数纳入全系统线性化状态矩阵，特征值分析表明 PLL 带宽和阻尼比影响交直流接口的低频振荡模态。PLL 参数需与换流器电流内环、外环控制器参数协调，单独优化 PLL 带宽可能导致全系统稳定裕度下降。

## 4. 实现方法与算法细节

### 4.1 PLL 变体

| 类型 | 机制 | 适用场景 | 代价 |
|------|------|----------|------|
| SRF-PLL | dq 坐标下 $v_q \to 0$ PI 控制 | 平衡电网、GFL 并网 | 不平衡/谐波下性能差 |
| DSOGI-PLL | $\alphaβ$ 正交信号生成 +正序提取 | 不平衡电网、谐波畸变 | 频率耦合反馈可能加剧扰动 |
| 自适应带宽 PLL | 暂态检测 + 带宽动态调节（Ranasinghe 2024） | 弱网、故障穿越 | 需暂态检测器和切换逻辑 |
| 增强 PLL 稳定性模型 | 慢快分解保留 di/dt 耦合（Carreño 2026） | 弱网小信号稳定性分析 | 不适用于 EMT 波形仿真 |

### 4.2 自适应带宽 PLL 的实现（Ranasinghe 2024）

Ranasinghe (2024) 在 DSOGI-PLL 中加入两个增强模块：

1. **暂态检测-频率冻结**：检测到扰动后，临时冻结 DSOGI 结构使用的 PLL 频率输出，防止频率估计快速变化破坏 SOGI 滤波特性
2. **自适应带宽**：扰动期间提高 PLL 带宽以加速同步，恢复后降回至稳健设置

核心机制是在 PLL 内部切断"扰动 $\to$ 频率估计摆动 $\to$ SOGI 滤波偏移 $\to$ 更大同步误差"的不利反馈链。

### 4.3 PLL 稳定性分析的 RMS+ 模型（Carreño 2026）

RMS+ 模型基于 Tikhonov-Fenichel 慢快系统理论，将电磁暂态（快动态，ms 级）视为边界层、PLL 动态（慢动态，百 ms 级）视为简化流形。与传统 RMS（恒定导纳矩阵代数模型）的区别：

| 模型 | 电磁动态 | PLL-网络交互 | 计算代价 |
|------|----------|-------------|----------|
| EMT | 完整 $di/dt$, $dv/dt$ | 精确 | 高 |
| RMS | 忽略（恒定导纳） | 遗漏失稳机制 | 低 |
| RMS+ | 保留影响 PLL 的部分 | 捕捉关键耦合 | 居中 |

## 5. 适用边界与失效模式

### 适用条件

- GFL 换流器并网系统需同步相位和频率
- 电网频率变化需跟踪（扰动、故障、孤岛等暂态过程）
- 弱电网（低 SCR）下需分析 PLL 与网络阻抗交互稳定性

### 失效模式

| 失效场景 | 原因 | 后果 |
|----------|------|------|
| 弱网 PLL 失锁 | SCR 过低，PLL 与网络阻抗耦合失稳（Carreño 2026） | 换流器失控或脱网 |
| 故障后频率摆动 | DSOGI 频率反馈耦合（Ranasinghe 2024） | 同步误差放大 |
| 不平衡/谐波下 SRF 偏差 | 负序、谐波在 dq 中产生振荡分量 | 相角估计偏移 |
| PLL-控制器交互失稳 | PLL 带宽与电流内环带宽重叠（Guo 2022, 贺永杰 2026） | 系统模态失稳 |
| 暂态后持续高带宽 | 自适应带宽未正确恢复（Ranasinghe 2024） | 噪声放大 |

### 关键约束

- SRF-PLL 在平衡工况下有效，不平衡或谐波下正序基波提取需 DSOGI 或其他正交信号生成
- PLL 带宽设计需折中：高带宽快响应但噪声敏感，低带宽抗噪声但慢跟踪
- EMT 仿真中 PLL 的离散化（采样延迟、PWM 更新、计算延迟）影响控制等效带宽，Guo (2022) 在高频段（550 Hz--1.8 kHz）需计及延时
- 单类型 PLL 的稳定性结论不能外推到其他结构或控制系统

## 6. 应用案例

### 案例 1：ADSOGI-PLL 的故障穿越改进（Ranasinghe 2024）

场景：并网逆变器在电网扰动（电压暂降、相位突变）下的 PLL 响应。DSOGI-PLL 在暂态时 PLL 频率反馈到 SOGI 滤波的链路产生不利耦合。暂态检测器在识别扰动后冻结 SOGI 使用的 PLL 频率，配合自适应带宽调节，在扰动期间加速同步、扰动后恢复稳健带宽。

### 案例 2：PLL 弱网失稳的 RMS+ 分析（Carreño 2026）

场景：含大量 GFL-VSC 的电网小信号同步稳定性。传统 RMS 模型遗漏 PLL 与网络电感 $di/dt$ 的耦合，无法捕捉 SCR 临界值以下的失稳。RMS+ 以慢快系统理论保留关键电磁动态，降阶状态空间模型可用于模态分析。

### 案例 3：PLL 参数对 LCC-HVDC 小干扰稳定性的影响（贺永杰 2026）

场景：单极 12 脉动 LCC-HVDC 系统的小干扰稳定性分析。在改进动态相量模型基础上，建立包含 PLL、换流器控制和直流线路的全系统线性化状态矩阵。PLL 参数与整流侧/逆变侧控制器参数并列为影响系统稳定性的因素。

## 7. 延伸阅读

- [[dq-transformation]]：PLL 提供的同步角是 dq 坐标变换的基础
- [[vector-control]]：GFL 换流器的 dq 矢量控制依赖 PLL 的同步角
- [[grid-connected-inverter]]：GFL 并网设备的典型同步和控制背景
- [[impedance-modeling]]：dq 坐标下含 PLL 的换流器阻抗建模与稳定性分析
- [[gfl-inverter-model]]：弱电网中 PLL 与网络阻抗交互的分析方法
- [[small-signal-stability]]：PLL 参数作为小干扰稳定性分析的状态矩阵元素
- [[fault-ride-through]]：故障穿越中 PLL 的同步角估计精度要求

## 来源论文

| 论文 | 年份 |
|------|------|
| [[comparison-of-dynamic-phasor-discrete-time-and-frequency-scanning-based-ssr-mode|Comparison of dynamic phasor, discrete-time and frequency sc]] | 2021 |
| [[mmc-hvdc系统高频稳定性分析与抑制策略(一)稳定性分析|High Frequency Stability Analysis and Suppression Strategy o]] | 2021 |
| [[characteristic-analysis-of-high-frequency-resonance-of-flexible-high-voltage-dir|Characteristic Analysis of High-frequency Resonance of Flexi]] | 2022 |
