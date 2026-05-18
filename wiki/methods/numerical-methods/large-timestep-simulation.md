---
title: "大步长仿真 (Large Timestep Simulation)"
type: method
tags: [large-timestep, simulation, efficiency, real-time, tsa, multirate, implicit-integration]
created: "2026-05-02"
updated: "2026-05-18"
---

# 大步长仿真 (Large Timestep Simulation)

## 定义

大步长仿真（Large Timestep Simulation）是指在满足目标精度和稳定性边界的前提下，使用比详细 EMT 更大的时间步长进行暂态计算。它不是单一积分算法，而是一组建模、积分、分区和验证策略的组合。常见路径包括隐式积分、动态相量或移频建模、平均值模型、模型降阶、多速率分区和频率相关网络等效。

大步长的收益来自减少时间步数或降低模型刚性；风险是丢失高频电磁暂态、开关细节、事件时刻和局部波形相位。任何"大步长可用"的结论都应绑定研究对象、目标频带、步长、基准解和误差指标。

## EMT 中的角色

大步长仿真在 EMT 知识体系中主要用于：

- **大系统或长时间窗口研究**：当关注机电振荡、控制包络或低频暂态时，不必解析所有微秒级细节。
- **实时和 HIL 约束**：计算时间必须小于物理步长，需要模型简化和稳定积分器共同作用。
- **EMT-TS 或 EMT-DP 混合**：详细区域保留小步长，外部系统用较大步长或等效模型。
- **宽频等效与降阶**：把远端网络、频变线路或电力电子开关细节压缩为端口模型。

这些用法都要求明确"被保留的动态"和"被平均或阻尼掉的动态"。

## 核心机制

### 隐式积分器的大步长基础

隐式方法可放宽稳定性约束，使大步长成为可能。典型形式包括：

**后向欧拉（Backward Euler）**：

$$\mathbf{x}_{n+1} = \mathbf{x}_n + \Delta t \cdot f(t_{n+1}, \mathbf{x}_{n+1})$$

**梯形法（Trapezoidal Rule）**：

$$\mathbf{x}_{n+1} = \mathbf{x}_n + \frac{\Delta t}{2}\left[f(t_n, \mathbf{x}_n) + f(t_{n+1}, \mathbf{x}_{n+1})\right]$$

**三阶段单对角隐式 Runge-Kutta（3S-SDIRK）**： [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi]]

3S-SDIRK 方法具有 L 稳定性（阻尼高频模态）和三阶精度，比 TR、2S-DIRK 和 TR-BDF2 在相同精度下允许更大步长。其 Butcher 表为：

| 阶段 | $c$ | $A$ | $b^T$ |
|------|-----|-----|-------|
| 1 | $\alpha$ | $\alpha$ | $b_1$ |
| 2 | $\gamma$ | $\gamma - \beta, \alpha$ | $b_2$ |
| 3 | 1 | $\delta - \gamma, \gamma - \alpha, \alpha$ | $b_3$ |

其中 $\alpha = 1 - \frac{2}{3}\sqrt{2}$，$\gamma = \frac{1}{6}(4 + \sqrt{2})$，$\delta = \frac{1}{6}(4 - \sqrt{2})$。

离散化后的状态更新方程：

$$\mathbf{x}_{n+1} = \mathbf{x}_n + \Delta t\left[\sum_{i=1}^{3} b_i f(t_n + c_i \Delta t, \mathbf{k}_i)\right]$$

其中每个隐式阶段 $\mathbf{k}_i$ 需要求解 $A \mathbf{k}_i = \cdots$ 形式的非线性方程。

**大步长移频 EMT（SF-EMT）**： [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi]]

将工频附近的信号平移到低频包络域，只保留正频率谱：

$$x_E(t) = \text{Re}\left[\mu(t) \cdot \mathbf{X}(t)\right], \quad \mu(t) = e^{j\omega_0 t}$$

由于 $x_E(t)$ 频谱集中在 0 Hz 附近，数值积分稳定性边界大大放宽，可使用更大步长而不产生振荡——这正是 3S-SDIRK "无振荡"（oscillation-free）特性的物理基础。

### 动态相量与移频建模

动态相量将基频附近的正弦量转为低频包络： [[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits]]

$$x(t) = \text{Re}\left[\mu(t) \cdot \bar{\mathbf{X}}(t)\right], \quad \mu(t) = e^{j\omega_0 t}$$

$$\bar{\mathbf{X}}(t) = \frac{\omega_0}{2\pi}\int_{t-\frac{2\pi}{\omega_0}}^{t} x(\tau) e^{-j\omega_0 \tau} d\tau$$

若目标是基频稳态或缓慢变化包络，可减少采样需求。但系统固有暂态模态只是被平移，并不会自动消失；故障、切换和宽频振荡仍可能要求较小步长。

### 多速率与分区

多速率方法将系统划分为快区和慢区： [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems]]

$$\dot{\mathbf{x}}_f = f_f(\mathbf{x}_f, \mathbf{x}_s, t), \quad \dot{\mathbf{x}}_s = f_s(\mathbf{x}_f, \mathbf{x}_s, t)$$

快区用小步长 $\Delta t_f$，慢区用大步长 $\Delta t_s = n \cdot \Delta t_f$（$n$ 为整数）。接口通过时间同步方程联接：

$$\mathbf{y}_f(t_k) = \mathbf{y}_s(t_k), \quad \text{接口变量在共享时刻相等}$$

Shu 2018 提出的时间同步接口模型使用时变 Norton/Thevenin 等值消除接口延迟误差，阻抗参数通过高斯消元更新。

### 模型平均与降阶

平均值模型、频率相关网络等效（FDNE）、模型降阶（MOR）和外部系统等值都可减少状态数量或去掉快动态。代价是某些物理过程被近似或删除。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 340" xmlns="http://www.w3.org/2000/svg">
  <rect width="900" height="340" fill="white"/>
  <text x="450" y="22" text-anchor="middle" font-family="Arial" font-size="13" font-weight="bold">大步长仿真方法体系架构</text>
  <rect x="20" y="35" width="860" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="450" y="52" text-anchor="middle" font-family="Arial" font-size="11" fill="#1e40af" font-weight="bold">输入：仿真目标</text>
  <text x="90" y="72" text-anchor="middle" font-family="Arial" font-size="9" fill="#1e40af">刚性系统/高频振荡</text>
  <text x="230" y="72" text-anchor="middle" font-family="Arial" font-size="9" fill="#1e40af">基频包络/机电暂态</text>
  <text x="370" y="72" text-anchor="middle" font-family="Arial" font-size="9" fill="#1e40af">电力电子详细开关</text>
  <text x="510" y="72" text-anchor="middle" font-family="Arial" font-size="9" fill="#1e40af">大系统分区</text>
  <text x="650" y="72" text-anchor="middle" font-family="Arial" font-size="9" fill="#1e40af">宽频端口等效</text>
  <text x="780" y="72" text-anchor="middle" font-family="Arial" font-size="9" fill="#1e40af">实时/HIL约束</text>
  <line x1="450" y1="85" x2="450" y2="98" stroke="#666" stroke-width="1.5" marker-end="url(#a1)"/>
  <defs><marker id="a1" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#666"/></marker></defs>
  <rect x="20" y="100" width="860" height="145" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="450" y="117" text-anchor="middle" font-family="Arial" font-size="11" fill="#166534" font-weight="bold">大步长 EMT 方法</text>
  <rect x="35" y="125" width="200" height="110" rx="5" fill="white" stroke="#86efac" stroke-width="1"/>
  <text x="135" y="140" text-anchor="middle" font-family="Arial" font-size="10" fill="#166534" font-weight="bold">① 隐式积分</text>
  <text x="135" y="155" text-anchor="middle" font-family="Arial" font-size="8" fill="#6b7280">3S-SDIRK / BE / TR / BDF</text>
  <text x="135" y="168" text-anchor="middle" font-family="Arial" font-size="8" fill="#374151">L稳定性 → 高频阻尼</text>
  <text x="135" y="180" text-anchor="middle" font-family="Arial" font-size="8" fill="#374151">步长 50-100 μs</text>
  <text x="135" y="192" text-anchor="middle" font-family="Arial" font-size="8" fill="#6b7280">适用: 刚性系统</text>
  <text x="135" y="204" text-anchor="middle" font-family="Arial" font-size="8" fill="#6b7280">目标频带 ≤5 kHz</text>
  <text x="135" y="218" text-anchor="middle" font-family="Arial" font-size="8" fill="#9ca3af">Shu 2018 / Parvari 2026</text>
  <rect x="245" y="125" width="200" height="110" rx="5" fill="white" stroke="#86efac" stroke-width="1"/>
  <text x="345" y="140" text-anchor="middle" font-family="Arial" font-size="10" fill="#166534" font-weight="bold">② 动态相量</text>
  <text x="345" y="155" text-anchor="middle" font-family="Arial" font-size="8" fill="#6b7280">DP / 移频 EMT / SF-EMT</text>
  <text x="345" y="168" text-anchor="middle" font-family="Arial" font-size="8" fill="#374151">基频包络频谱平移</text>
  <text x="345" y="180" text-anchor="middle" font-family="Arial" font-size="8" fill="#374151">步长 10-20 ms</text>
  <text x="345" y="192" text-anchor="middle" font-family="Arial" font-size="8" fill="#6b7280">适用: 机电振荡</text>
  <text x="345" y="204" text-anchor="middle" font-family="Arial" font-size="8" fill="#6b7280">故障初期不适用</text>
  <text x="345" y="218" text-anchor="middle" font-family="Arial" font-size="8" fill="#9ca3af">Parvari 2026 / Rupasinghe 2021</text>
  <rect x="455" y="125" width="200" height="110" rx="5" fill="white" stroke="#86efac" stroke-width="1"/>
  <text x="555" y="140" text-anchor="middle" font-family="Arial" font-size="10" fill="#166534" font-weight="bold">③ 平均值模型</text>
  <text x="555" y="155" text-anchor="middle" font-family="Arial" font-size="8" fill="#6b7280">SAVM / P-GSSA / DQ-AVM</text>
  <text x="555" y="168" text-anchor="middle" font-family="Arial" font-size="8" fill="#374151">开关细节省略</text>
  <text x="555" y="180" text-anchor="middle" font-family="Arial" font-size="8" fill="#374151">步长 0.1-1 ms</text>
  <text x="555" y="192" text-anchor="middle" font-family="Arial" font-size="8" fill="#6b7280">适用: 换流器建模</text>
  <text x="555" y="204" text-anchor="middle" font-family="Arial" font-size="8" fill="#6b7280">谐波/保护触发缺失</text>
  <text x="555" y="218" text-anchor="middle" font-family="Arial" font-size="8" fill="#9ca3af">Gnanarathna 2011 / Ould-Bachir</text>
  <rect x="665" y="125" width="200" height="110" rx="5" fill="white" stroke="#86efac" stroke-width="1"/>
  <text x="765" y="140" text-anchor="middle" font-family="Arial" font-size="10" fill="#166534" font-weight="bold">④ 多速率分区</text>
  <text x="765" y="155" text-anchor="middle" font-family="Arial" font-size="8" fill="#6b7280">MATE / DPIM / 插值接口</text>
  <text x="765" y="168" text-anchor="middle" font-family="Arial" font-size="8" fill="#374151">快区 Δt_f / 慢区 Δt_s</text>
  <text x="765" y="180" text-anchor="middle" font-family="Arial" font-size="8" fill="#374151">加速比 4-10×</text>
  <text x="765" y="192" text-anchor="middle" font-family="Arial" font-size="8" fill="#6b7280">适用: 大系统分区</text>
  <text x="765" y="204" text-anchor="middle" font-family="Arial" font-size="8" fill="#6b7280">接口插值误差累积</text>
  <text x="765" y="218" text-anchor="middle" font-family="Arial" font-size="8" fill="#9ca3af">Shu 2018: 6.2× 加速</text>
  <line x1="450" y1="245" x2="450" y2="258" stroke="#666" stroke-width="1.5" marker-end="url(#a2)"/>
  <rect x="20" y="260" width="860" height="50" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="450" y="277" text-anchor="middle" font-family="Arial" font-size="11" fill="#5b21b6" font-weight="bold">输出：大步长 EMT 仿真结果</text>
  <text x="130" y="297" text-anchor="middle" font-family="Arial" font-size="9" fill="#5b21b6">端口电压/RMS</text>
  <text x="290" y="297" text-anchor="middle" font-family="Arial" font-size="9" fill="#5b21b6">机电振荡包络</text>
  <text x="450" y="297" text-anchor="middle" font-family="Arial" font-size="9" fill="#5b21b6">控制响应轨迹</text>
  <text x="600" y="297" text-anchor="middle" font-family="Arial" font-size="9" fill="#5b21b6">稳态谐波含量</text>
  <text x="750" y="297" text-anchor="middle" font-family="Arial" font-size="9" fill="#5b21b6">系统能量轨迹</text>
  <rect x="20" y="320" width="10" height="10" rx="2" fill="#dbeafe" stroke="#2563eb"/>
  <text x="34" y="329" font-family="Arial" font-size="8" fill="#374151">输入</text>
  <rect x="70" y="320" width="10" height="10" rx="2" fill="#dcfce7" stroke="#16a34a"/>
  <text x="84" y="329" font-family="Arial" font-size="8" fill="#374151">方法</text>
  <rect x="120" y="320" width="10" height="10" rx="2" fill="#ede9fe" stroke="#7c3aed"/>
  <text x="134" y="329" font-family="Arial" font-size="8" fill="#374151">输出</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 大步长仿真方法体系架构</p>


## 形式化表达

### 误差基准

大步长误差定义为相对于参考解的偏差：

$$E = \frac{\|\mathbf{x}_{\text{large}} - \mathbf{x}_{\text{ref}}\|}{\|\mathbf{x}_{\text{ref}}\|}$$

其中 $\mathbf{x}_{\text{ref}}$ 应来自解析解、小步长 EMT、实验数据或已验证工具。误差指标应对应实际目标：端口电压峰值、相位、RMS、能量、控制触发时间或稳定裕度。

### 多速率接口稳定性条件

Shu 2018 推导的多速率接口稳定性条件为：

$$\rho\left(\mathbf{I} - \mathbf{G}_f \mathbf{Y}_s\right) < 1$$

其中 $\mathbf{G}_f$ 为快区电导矩阵，$\mathbf{Y}_s$ 为慢区等效导纳矩阵。该条件保证接口能量不发散。

### 三阶段 SDIRK 稳定性函数

3S-SDIRK 方法的稳定性函数为：

$$R(z) = 1 + z + \frac{z^2}{2} + \frac{z^3}{6}$$

其在复平面的极点位置确保 $|R(z)| \leq 1$ 当 $\text{Re}(z) < 0$（L 稳定性），允许大步长而不产生数值振荡。

## 关键技术挑战

### 挑战1：高频模态被数值阻尼掩盖真实物理

L 稳定的隐式方法会阻尼高频模态，这是大步长允许的代价。若研究目标是高频振荡（如行波反射、开关纹波），数值阻尼会错误地使波形衰减。**判据**：若目标频带 $f_{\text{target}} > f_{\text{Nyquist}}/n_{\text{step}}$（其中 $n_{\text{step}} = \Delta t_{\text{large}} / \Delta t_{\text{small}}$），大步长不可用。

### 挑战2：接口插值误差与数值振荡

多速率接口在慢区大步长边界处使用插值或外推重建快区变量，会引入额外误差。当接口强耦合（如 MMC 与弱电网）时，插值误差可能累积导致稳定性丧失。 [[multi-timescale-simulator-of-nonlinear-electrical-elements-by-interfacing-shifte]]

**应对**：Shu 2018 的时变 Thevenin/Norton 等值通过预测-平均协调机制抑制接口振荡，协调方程为：

$$\mathbf{G}_f \tilde{\mathbf{v}}_h = \tilde{\mathbf{i}}_h + \mathbf{G}_f \mathbf{v}_{h,f}^{\text{pred}}$$

### 挑战3：事件时刻定位与固定步长矛盾

固定大步长可能跳过故障发生、开关动作等关键时刻，导致事件处理错误。 [[accurate-time-domain-simulation-of-power-electronic-circuits]]

**应对**：采用局部步长细化（local step-size reduction）或事件检测-定位-重启机制，在事件点前后自动切换到小步长。

### 挑战4：FDNE 无源性与频带截断误差

频率相关网络等效的拟合结果可能违反无源性（passivity），在时域仿真中导致不稳定。 [[advanced-wideband-linecable-modeling-for-transient-studies]]

**应对**：使用无源性强制（passivity enforcement）方法确保 $Y(s)$ 的正实部条件；验证频带截断边界处的阻抗偏差。

## 量化性能边界

### 步长允许范围（基于目标频带）

根据采样定理和数值稳定性分析：

| 目标动态 | 最低解析频带 | 最大步长 $\Delta t_{\max}$ | 推荐积分器 |
|---------|------------|--------------------------|-----------|
| 行波反射（≥10 kHz） | 20 kHz | 25 μs | 显式 or 小步长 |
| 开关纹波（2-5 kHz） | 10 kHz | 50 μs | 隐式 |
| 机电振荡（0.5-2 Hz） | 10 Hz | 2 ms | 多速率/动态相量 |
| 基频包络稳态 | 0.5 Hz | 20 ms | 动态相量 |

### 三阶段 SDIRK 大步长性能 [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi]]

- 3S-SDIRK 在三阶精度下，步长可增大至 TR 的 2-3 倍（相同精度目标）
- L 稳定性保证高频模态阻尼，无振荡
- 每步计算量略高于单隐式方法（3 次函数求值 vs 1-2 次），但总时间步数大幅减少

### 多速率加速比 [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems]]

Shu 2018 在 MMC-MTDC + AC 系统中报告：
- 快区（MTDC）：$\Delta t_f = 100$ μs
- 慢区（AC）：$\Delta t_s = 1000$ μs（$n = 10$）
- 加速比约 **6.2×**（vs 单速率全系统 $\Delta t = 100$ μs）
- 接口误差 $< 0.5\%$（电压峰值），接口能量守恒误差 $< 0.1\%$

### 动态相量大步长边界 [[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits]]

Parvari 2026 测试表明：动态相量方法在基频包络研究中可将步长增大至 10-20 ms，但系统固有暂态模态（故障后 5-50 ms 内）被包络截断——**适用于稳态包络，不适用于暂态早期**。

## 步长选择决策表

| 仿真目标 | 目标频带 | 推荐步长 | 推荐方法 | 不适用原因 |
|---------|---------|---------|---------|-----------|
| 雷电/操作过电压 | ≥10 kHz | ≤25 μs | 详细 EMT | 大步长丢失高频 |
| 开关纹波/换相 | 1-5 kHz | 50-100 μs | 隐式积分 | 包络方法丢失细节 |
| 机电振荡 | 0.5-2 Hz | 1-5 ms | 多速率/动态相量 | 显式步长过小 |
| 基频稳态包络 | ≤0.1 Hz | 10-20 ms | 动态相量 | 高频暂态已截断 |
| 实时/HIL | — | $\Delta t_{\max} = T_{\text{compute}}$ | 隐式+模型降阶 | 受计算时限硬约束 |
| 长期合环暂态 | ≤10 Hz | 0.5-2 ms | 多速率 | 全详细计算量过大 |

## 适用边界与选择指南

**适合使用大步长仿真的场景**：

- 以基频包络、机电振荡、慢控制或外部网络影响为主要目标
- 系统可被合理分区，快动态局限在小区域或可由等效模型表示
- 有小步长参考、实验数据或可信工具进行工况级验证
- 实时仿真中计算裕度不足，需要在精度和速度间权衡

**不适合直接放大步长的场景**：

- 雷电、操作过电压、行波反射、绝缘配合等高频 EMT
- 详细电力电子开关、二极管换相、保护触发和控制采样强耦合场景
- 事件时刻不确定且不能插值或局部细化的固定步长仿真
- 需要报告波形峰值、谐波或高频振荡精确相位的研究

## 相关方法

- [[backward-euler]]：L 稳定阻尼，一阶精度，提供基础隐式积分框架
- [[trapezoidal-rule]]：二阶 A 稳定主积分器，大步长事件后可能振荡
- [[gear-method]]：BDF/Gear 方法服务刚性和大步长子问题
- [[dynamic-phasor]]：频移包络是大步长仿真的核心路线
- [[multirate-method]]：通过快慢分区而非全系统统一大步长提高效率
- [[model-order-reduction]]：通过减少状态和频带近似支持大步长
- [[numerical-integration-error]]：提供误差分类和验证方法
- [[compensation-method]]：节点补偿法在大系统分块仿真中的应用

## 来源论文

- [[three-stage-implicit-integration-for-large-time-step-size-electromagnetic-transi]] — 提出 3S-SDIRK 三阶段隐式积分，L 稳定三阶精度，专门优化大步长 EMT 移频包络仿真，验证表明步长可增大至 TR 的 2-3 倍
- [[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits]] — 重新评估动态相量在电路仿真中的效能，指出包络方法保留基频稳态但截断固有暂态模态的适用边界
- [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems]] — 提出 MMC-MTDC + AC 多速率协同仿真框架，时变 Thevenin/Norton 接口消除延迟误差，报告 6.2× 加速比
- [[nodal-reduced-induction-machine-modeling-for]] — 提出节点降阶感应电机模型，支持大步长端口等效
- [[direct-interfacing-of-parametric-average-value-models-of-acx2013dc-converters-fo]] — 提出参数化平均值模型与 EMT 的直接接口方法
- [[multi-timescale-simulator-of-nonlinear-electrical-elements-by-interfacing-shifte]] — 多时间尺度仿真器非线性电气元件的移频接口方法
- [[2728模块化多电平换流器时间尺度变换建模和仿真]] — MMC 时间尺度变换建模与仿真方法（中文论文）