---
title: "锁相环参数设计方法 (PLL Design)"
type: method
tags: [pll-design, pll, parameter-tuning, synchronization, inverter-control]
created: "2026-05-04"
updated: "2026-05-18"
---

# 锁相环参数设计方法 (PLL Design)

## 定义与边界

PLL 设计方法指围绕锁相环带宽、阻尼、滤波结构和暂态整定规则建立的参数设计路线。它关注"如何设计与整定 PLL"，而非 PLL 作为同步机制的原理本身。本页讨论 PLL 的参数与结构整定边界，不替代 [[models/control/pll-model.md]] 作为总入口。

PLL 参数设计需同时考虑三个层面：

- **稳态性能**：谐波/不平衡下的相位精度、频率跟踪精度
- **暂态性能**：故障/相位跳变下的同步恢复速度、超调控制
- **稳定边界**：PLL 与网络阻抗、电流内环、外环控制的交互稳定性

## EMT 中的作用

在 EMT 仿真中，PLL 设计方法主要用于：

- 选择 PLL 带宽、PI 增益和滤波结构参数
- 评估故障、弱网和不平衡工况下的相位误差与同步恢复时间
- 分析 PLL 参数与短路比（SCR）、外环带宽、电流内环带宽之间的联合稳定性
- 设计自适应带宽策略，在不同工况下切换 PLL 动态特性
- 验证 PLL 参数是否落入跨临界分岔或 Hopf 分岔的不稳定区域

## EMT 建模方法

PLL 参数设计在 EMT 环境中的核心是**小信号线性化 + 数值扫描**工作流：

### 1. 线性化建模

对 SRF-PLL 控制环进行小信号线性化，得到闭环传递函数：

$$
G_{pll}(s) = \frac{K_p s + K_i}{s}
$$

其中 $K_p$ 为比例增益，$K_i$ 为积分增益。PLL 的闭环带宽为：

$$
omega_c = \sqrt{K_p^2 + K_i^2}
$$

阻尼比为：

$$
xi = \frac{K_p}{2\omega_n}, \quad \omega_n = \sqrt{K_p^2 + K_i^2}
$$

### 2. 分岔边界计算

**跨临界分岔条件** [Carreño 2026]：当 PLL 比例增益越过下式边界时，系统发生鞍结型失稳：

$$
K_p > \frac{1}{i_P L}
$$

其中 $i_P$ 为滤波器输出电流幅值，$L$ 为电网电感。

**Hopf 分岔条件** [Carreño 2026]：当 PLL 参数满足下式时，与电网电感交互导致持续振荡失稳：

$$
K_p \sqrt{V^2 - (i_P X)^2} - K_i i_P L > 0
$$

其中 $V$ 为公共连接点电压幅值，$X = \omega L$。

### 3. 参数扫描验证

在 EMT 中通过**扫频法**验证 PLL 稳定性边界：

$$
K_i ext{ sweep}: K_p = K_{p0}, \quad K_i \in [K_i^{min}, K_i^{max}]
$$

$$
K_p ext{ sweep}: K_i = K_{i0}, \quad K_p \in [K_p^{min}, K_p^{max}]
$$

临界增益通过监测特征值穿过虚轴确定。典型临界值 [Carreño 2026]：

| 测试系统 | 参数 | 临界值 |
|---------|------|--------|
| 单换流器无限母线 | Kp（Ki=100 p.u.） | 547 p.u.（稳定）/623 p.u.（失稳） |
| 单换流器无限母线 | Ki（Kp=5 p.u.） | 2322 p.u.（稳定）/2600 p.u.（失稳） |
| WSCC 九节点（慢 PLL） | Ki（Kp=5 p.u.） | 3014 p.u.（稳定）/3257 p.u.（失稳） |
| WSCC 九节点（快 PLL） | Ki（Kp=500 p.u.） | 90e3 p.u.（部分失稳） |

### 4. 自适应带宽策略 [Ranasinghe 2024]

暂态检测器识别扰动并冻结 PLL 频率输出，同时自适应调整带宽：

$$
omega_{PLL} = \begin{cases}
omega_{nom} & ext{稳态} \
gamma \cdot omega_{nom} & ext{暂态检测到} \
end{cases}, \quad \gamma \approx 5
$$

暂态检测判据为相位误差超阈值：

$$
|Delta \theta| > epsilon_\theta, \quad \epsilon_\theta = 0.1 \text{ rad}
$$

频率冻结持续时间 $T_{freeze} = 0.1$ s，期间 PLL 输出频率保持不变以避免噪声放大。

### 5. 时间尺度分离校核

电感时间常数与 PLL 时间常数的比值决定建模精度：

$$
\frac{\tau_L}{\tau_{PLL}} = \frac{L/R}{1/K_p} = \frac{K_p L}{R}
$$

- **$< 0.1$**：PLL 与网络动态可近似解耦，EMT 误差 $< 2\%$
- **$> 0.3$**：需高阶修正，网络电感 $di/dt$ 效应不可忽略

## 常见设计目标

### 带宽选择策略

PLL 带宽是设计的核心参数。高带宽加速同步但放大谐波，低带宽抑制噪声但暂态响应慢。

- **固定带宽设计**：在稳态滤波和暂态响应间折中，典型值 $K_p = 20$ p.u.，$K_i = 200$ p.u.（39 节点测试系统 [Carreño 2026]）
- **自适应带宽设计** [Ranasinghe 2024]：稳态保持低带宽（62 rad/s），暂态放大至 5 倍，配合频率冻结防止噪声放大

### PI 参数整定

SRF-PLL 的 PI 参数（$K_p$, $K_i$）决定闭环动态：$K_p$ 控制同步速度，$K_i$ 消除稳态频率偏差。

- **特征方程匹配法** [Ranasinghe 2024]：根据目标阻尼比 $\xi = 0.7$ 和穿越频率 $\omega_c$ 联立求解 $K_p$, $K_i$

$$
\omega_p = 2 \xi \omega_n + A, \quad A \omega_n^2 = K_i \omega_p, \quad \omega_n^2 + 2 \xi \omega_n A = \omega_p K_p
$$

- **稳定边界约束法** [Carreño 2026]：确保 $K_p < 1/(i_P L)$ 避免跨临界分岔，$K_i/K_p < \sqrt{V^2-(i_P X)^2}/(i_P L)$ 避免 Hopf 分岔

### 耦合强度系数

引入耦合强度系数量化 PLL-电网交互弱阻尼边界 [Carreño 2026]：

$$
\kappa = \frac{K_p \cdot i_P \cdot L}{\omega_n}
$$

当 $\kappa > 0.05$ 时系统进入弱阻尼区域（阻尼比 $\zeta < 0.1$）。

## 关键技术挑战

### 挑战 1：弱电网下经验参数失效

强网中"高带宽好"的工程经验在弱网（SCR $< 2$）下可能触发失稳。降低参数反而有利，因为高带宽放大了网络阻抗对 PLL 的耦合效应。

**量化边界** [Carreño 2026]：WSCC 九节点系统中，快 PLL（$K_p = 500$ p.u.）配置下 RMS+ 模型出现两个振荡模式，其中一个为虚构模式——此时时间尺度分离假设不成立，EMT 建模失效。

### 挑战 2：PLL 与外环控制的交互稳定性

PLL 带宽接近外环控制带宽时，可能引发**次同步控制相互作用（SSCI）**。单独优化 PLL 带宽不保证整体系统稳定，必须联合校核。

**量化数据** [Carreño 2026]：39 节点测试系统中，SRF-PLL 参数（$K_p = 20$ p.u.，$K_i = 200$ p.u.）在慢 PLL 配置下使主导极点位于 $-19.6 \pm j3.9$，阻尼比充足。

### 挑战 3：忽略 PCC 并联电容效应

PCC 并联等效电容（0.15 p.u.）显著改变稳定边界。高无功工况下，忽略电容的参数设计可能失稳。

### 挑战 4：暂态检测可靠性

自适应带宽策略依赖暂态检测的可靠性。若检测阈值不当（如 $\varepsilon = 0.1$ rad），可能误触发或漏触发，导致稳态性能退化或暂态保护失效。

### 挑战 5：多机并联交互耦合

多换流器并联场景下，各 PLL 参数之间的交互耦合机制尚不明确。目前缺乏通用多机 PLL 参数协同设计理论。

## 量化性能边界

| 参数 | 值 | 来源 |
|------|-----|------|
| 标称穿越频率 | 62 rad/s | Ranasinghe 2024 |
| 暂态带宽放大倍数 | 5 倍 | Ranasinghe 2024 |
| PI 增益（$K_p$, $K_i$） | 57.1, 1660.1 | Ranasinghe 2024 |
| 目标阻尼比 | 0.7 | Ranasinghe 2024 |
| 相位误差阈值 | 0.1 rad | Ranasinghe 2024 |
| 频率冻结时间 | 0.1 s | Ranasinghe 2024 |
| $K_p$ 临界值（跨临界分岔） | $1/(i_P L)$ | Carreño 2026 |
| 耦合强度系数阈值 | $\kappa > 0.05$ 进入弱阻尼 | Carreño 2026 |
| 主导极点（外环+PLL） | $-19.6 \pm j3.9$ | Carreño 2026 |
| PLL 相关谐振频率 | 70.3 Hz | Carreño 2026 |
| RMS+ 阻尼误差（慢 PLL） | $< 0.16\%$ | Carreño 2026 |
| RMS+ 频率误差（快 PLL） | $< 2$ Hz | Carreño 2026 |

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 520" xmlns="http://www.w3.org/2000/svg">
  <!-- Layer 1: 输入参数 -->
  <rect x="20" y="30" width="160" height="80" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="100" y="55" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e40af">输入参数</text>
  <text x="100" y="73" text-anchor="middle" font-size="10" fill="#1e3a8a">目标阻尼比 ξ=0.7</text>
  <text x="100" y="88" text-anchor="middle" font-size="10" fill="#1e3a8a">目标带宽 ωc</text>
  <text x="100" y="103" text-anchor="middle" font-size="10" fill="#1e3a8a">网络参数 SCR, L, R</text>

  <!-- Layer 2: 设计方法 -->
  <!-- 方法A: 特征方程匹配 -->
  <rect x="220" y="20" width="150" height="55" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="295" y="40" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">方法A: 特征方程匹配</text>
  <text x="295" y="55" text-anchor="middle" font-size="9" fill="#166534">Ranasinghe 2024</text>
  <text x="295" y="68" text-anchor="middle" font-size="9" fill="#166534">ξ, ωn → Kp, Ki</text>

  <!-- 方法B: 分岔约束 -->
  <rect x="220" y="85" width="150" height="55" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="295" y="105" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">方法B: 分岔约束</text>
  <text x="295" y="120" text-anchor="middle" font-size="9" fill="#166534">Carreño 2026</text>
  <text x="295" y="133" text-anchor="middle" font-size="9" fill="#166534">Kp &lt; 1/(iP·L)</text>

  <!-- 方法C: 自适应带宽 -->
  <rect x="220" y="150" width="150" height="55" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="295" y="170" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e">方法C: 自适应带宽</text>
  <text x="295" y="185" text-anchor="middle" font-size="9" fill="#92400e">Ranasinghe 2024</text>
  <text x="295" y="198" text-anchor="middle" font-size="9" fill="#92400e">稳态 62 rad/s, γ=5</text>

  <!-- 方法D: 参数扫描 -->
  <rect x="220" y="215" width="150" height="55" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="295" y="235" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e">方法D: 参数扫描</text>
  <text x="295" y="250" text-anchor="middle" font-size="9" fill="#92400e">EMT 数值验证</text>
  <text x="295" y="263" text-anchor="middle" font-size="9" fill="#92400e">Kp/Ki 扫频 → 临界值</text>

  <!-- Layer 3: 输出 -->
  <rect x="410" y="90" width="170" height="140" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="495" y="115" text-anchor="middle" font-size="13" font-weight="bold" fill="#4c1d95">输出验证指标</text>
  <text x="495" y="135" text-anchor="middle" font-size="10" fill="#5b21b6">跨临界分岔边界</text>
  <text x="495" y="152" text-anchor="middle" font-size="10" fill="#5b21b6">Hopf 分岔边界</text>
  <text x="495" y="169" text-anchor="middle" font-size="10" fill="#5b21b6">耦合强度系数 κ</text>
  <text x="495" y="186" text-anchor="middle" font-size="10" fill="#5b21b6">阻尼误差 Eζ &lt; 0.16%</text>
  <text x="495" y="203" text-anchor="middle" font-size="10" fill="#5b21b6">频率误差 Eω &lt; 2 Hz</text>
  <text x="495" y="220" text-anchor="middle" font-size="10" fill="#5b21b6">时间尺度比 τL/τPLL</text>

  <!-- Layer 4: 量化数据表 -->
  <rect x="620" y="20" width="260" height="240" rx="8" fill="#fce7f3" stroke="#be185d" stroke-width="2"/>
  <text x="750" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#9d174d">量化边界汇总</text>
  <line x1="630" y1="55" x2="870" y2="55" stroke="#be185d" stroke-width="1"/>
  <text x="640" y="72" font-size="9" fill="#831843">测试系统</text>
  <text x="760" y="72" font-size="9" fill="#831843">临界Kp</text>
  <text x="840" y="72" font-size="9" fill="#831843">临界Ki</text>
  <text x="640" y="87" font-size="8" fill="#831843">SCIB (Ki=100)</text>
  <text x="760" y="87" font-size="8" fill="#831843">547 p.u.</text>
  <text x="840" y="87" font-size="8" fill="#831843">—</text>
  <text x="640" y="100" font-size="8" fill="#831843">SCIB (Kp=5)</text>
  <text x="760" y="100" font-size="8" fill="#831843">—</text>
  <text x="840" y="100" font-size="8" fill="#831843">2322 p.u.</text>
  <text x="640" y="113" font-size="8" fill="#831843">WSCC (慢)</text>
  <text x="760" y="113" font-size="8" fill="#831843">5 p.u.</text>
  <text x="840" y="113" font-size="8" fill="#831843">3014 p.u.</text>
  <text x="640" y="126" font-size="8" fill="#831843">WSCC (快)</text>
  <text x="760" y="126" font-size="8" fill="#831843">500 p.u.</text>
  <text x="840" y="126" font-size="8" fill="#831843">90e3 p.u.</text>
  <line x1="630" y1="136" x2="870" y2="136" stroke="#f9a8d4" stroke-width="0.5"/>
  <text x="640" y="152" font-size="9" fill="#9d174d">弱阻尼阈值</text>
  <text x="760" y="152" font-size="9" fill="#9d174d">κ &gt; 0.05</text>
  <text x="840" y="152" font-size="9" fill="#9d174d">—</text>
  <text x="640" y="167" font-size="9" fill="#9d174d">阻尼误差(慢)</text>
  <text x="760" y="167" font-size="9" fill="#9d174d">Eζ &lt; 0.16%</text>
  <text x="840" y="167" font-size="9" fill="#9d174d">RMS+</text>
  <text x="640" y="180" font-size="9" fill="#9d174d">频率误差(快)</text>
  <text x="760" y="180" font-size="9" fill="#9d174d">Eω &lt; 2 Hz</text>
  <text x="840" y="180" font-size="9" fill="#9d174d">RMS+</text>
  <text x="640" y="195" font-size="9" fill="#9d174d">39节点 PLL</text>
  <text x="760" y="195" font-size="9" fill="#9d174d">Kp=20</text>
  <text x="840" y="195" font-size="9" fill="#9d174d">Ki=200</text>
  <text x="640" y="210" font-size="9" fill="#9d174d">主导极点</text>
  <text x="760" y="210" font-size="9" fill="#9d174d">−19.6±j3.9</text>
  <text x="840" y="210" font-size="9" fill="#9d174d">39节点</text>
  <text x="640" y="225" font-size="9" fill="#9d174d">谐振频率</text>
  <text x="760" y="225" font-size="9" fill="#9d174d">70.3 Hz</text>
  <text x="840" y="225" font-size="9" fill="#9d174d">Li 2024</text>
  <text x="640" y="245" font-size="9" fill="#9d174d" font-style="italic">注: SCIB=单换流器无限母线系统</text>

  <!-- Arrows -->
  <path d="M180 70 L218 47" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
  <path d="M180 70 L218 112" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
  <path d="M180 70 L218 177" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
  <path d="M180 70 L218 242" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
  <path d="M370 160 L408 160" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
  <path d="M580 160 L618 140" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrow)"/>

  <!-- Legend -->
  <rect x="20" y="460" width="15" height="15" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="40" y="472" font-size="10" fill="#333">输入参数</text>
  <rect x="120" y="460" width="15" height="15" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="140" y="472" font-size="10" fill="#333">分析方法</text>
  <rect x="220" y="460" width="15" height="15" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="240" y="472" font-size="10" fill="#333">自适应/扫描</text>
  <rect x="340" y="460" width="15" height="15" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="360" y="472" font-size="10" fill="#333">输出指标</text>
  <rect x="440" y="460" width="15" height="15" fill="#fce7f3" stroke="#be185d" stroke-width="1"/>
  <text x="460" y="472" font-size="10" fill="#333">量化数据</text>

  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · PLL 参数设计方法体系：四类设计方法 → 输出验证指标 → 量化边界汇总</p>

## 与相关方法的关系

- [[models/control/pll-model.md]]：PLL 作为同步机制的总入口
- [[methods/control/dsogi-pll.md]]：基于正交信号生成的 PLL 结构，DSOGI-PLL 参数涉及 SOGI 谐振频率和阻尼系数
- [[methods/control/srf-pll.md]]：同步坐标系 PLL，参数设计以带宽和 PI 增益为核心
- [[methods/control/frequency-control.md]]：PLL 影响频率测量，但不等同于频率控制

## 适用边界与选择指南

### 适用条件

- 需要整定并网同步环的 SRF-PLL、DSOGI-PLL 或类似结构
- 弱电网（SCR $< 3$）下 PLL 参数需协同网络阻抗和外环控制联合设计
- 自适应带宽策略适用于变工况（故障、相位跳变、频率斜坡）并网场景

### 失效边界

- **参数独立假设不成立**：单独优化 PLL 带宽不保证整体系统稳定，必须校核与外环、内环的交互
- **弱网下常规经验失效**：强网经验"高带宽好"在弱网（SCR $< 2$）下可能触发失稳，降低参数反而有利
- **频率冻结依赖暂态检测**：若暂态检测阈值不当（如 Ranasinghe 2024 取 $\varepsilon = 0.1$ rad），可能误触发或漏触发
- **单篇论文结论不可外推**：Ranasinghe 2024 的参数（62 rad/s, $K_p = 57.1$）适用于其特定 DSOGI 结构，不适用于 SRF-PLL 或其他拓扑
- **忽略 PCC 电容效应**：Li 2024 表明 PCC 并联等效电容（0.15 p.u.）显著改变稳定边界，忽略电容的参数设计在高无功工况下可能失稳

### 方法选择决策表

| 应用场景 | 推荐方法 | 关键指标 |
|---------|---------|---------|
| 强网固定工况 | 方法A：特征方程匹配 | $\xi = 0.7$, $\omega_c$ 已知 |
| 弱网稳定性验证 | 方法B：分岔约束 | $K_p < 1/(i_P L)$ |
| 变工况（故障/跳变） | 方法C：自适应带宽 | 带宽放大 $\gamma = 5$ |
| 不确定网络参数 | 方法D：参数扫描 | EMT 扫频验证 |
| 多机并联系统 | 方法B+D 组合 | 分岔边界 + 数值扫描 |

## 关键公式汇总

### SRF-PLL 闭环传递函数

$$
G_{pll}(s) = \frac{K_p s + K_i}{s}
$$

### 自适应 PI 参数整定方程组 [Ranasinghe 2024]

$$
\omega_p = 2\xi\omega_n + A, \quad A\omega_n^2 = K_i \omega_p, \quad \omega_n^2 + 2\xi\omega_n A = \omega_p K_p
$$

### 跨临界分岔条件 [Carreño 2026]

$$
K_p < \frac{1}{i_P L}
$$

### Hopf 分岔稳定判据 [Carreño 2026]

$$
K_p\sqrt{V^2 - (i_P X)^2} - K_i i_P L > 0
$$

### 耦合强度系数

$$
\kappa = \frac{K_p \cdot i_P \cdot L}{\omega_n}
$$

当 $\kappa > 0.05$ 时系统进入弱阻尼区域（阻尼比 $\zeta < 0.1$）。

## 开放问题

- 自适应带宽的频率冻结时间与系统惯性之间缺乏通用整定规则
- PLL 参数如何与限流、VSG 虚拟惯量和弱网稳定性联合整定仍需进一步研究
- 多机并联场景下各 PLL 参数之间的交互耦合机制尚不明确

## 来源论文

Ranasinghe 等 2024：DSOGI-PLL 自适应带宽参数设计，提供标称带宽 62 rad/s、PI 参数 $K_p = 57.1$ / $K_i = 1660.1$、暂态放大 5 倍等具体设计值。

Carreño 等 2026：PLL 参数与网络交互失稳边界，提供跨临界分岔和 Hopf 分岔解析条件，并在 WSCC 九节点和 39 节点系统中验证了 RMS+ 模型相对 EMT 的误差（阻尼误差 $< 0.16\%$，频率误差 $< 2$ Hz）。