---
title: "传输线理论 (Transmission Line Theory)"
type: topic
tags: [transmission-line, distributed-parameter, wave-propagation, telegraph-equation, quasi-tem, distributed-parameter-model]
created: "2026-05-04"
updated: "2026-05-17"
---

# 传输线理论 (Transmission Line Theory)

## 定义与边界

传输线理论是研究电磁波在双导体或多导体系统中传播特性的理论框架，考虑分布参数效应（单位长度电阻$R$、电感$L$、电容$C$、电导$G$），将线路视为连续分布的电磁系统而非集中参数电路。与集总参数模型不同，传输线理论通过**电报方程**（Telegraph Equations）描述电压和电流沿空间坐标的连续变化，适用于高频或长线分析。

**边界限定**：本页面聚焦于输电线路的分布参数理论，不包括集总参数近似或低频稳态分析。

## EMT中的作用

传输线理论在电磁暂态（EMT）仿真中具有基础性地位：

- **输电线路电磁暂态建模基础**：EMT仿真的核心理论框架，所有分布参数线路模型（贝杰龙模型、频变线路模型、通用线路模型等）都建立在电报方程之上
- **行波传播与反射分析**：故障定位和过电压计算的物理基础
- **过电压计算**：雷击和操作过电压沿线路的传播特性
- **频变参数建模**：宽频范围内线路特性的准确表征（集肤效应、大地返回路径）
- **多导体系统分析**：多回线路的耦合效应和模态解耦

### 与其他理论的区别

| 特性 | 传输线理论 | 集总参数模型 | 全波电磁模型 |
|------|-----------|-------------|-------------|
| 参数分布 | 连续分布 | 集中于节点 | 场分布 |
| 适用频率 | 中高频（>1kHz） | 低频（<1kHz） | 极高频（>10MHz） |
| 计算效率 | 高 | 最高 | 最低 |
| 精度保证条件 | 波长≥线路长度 | 线路电抗<<趋肤深度 | 全频段 |

## 核心理论

### 1. 电报方程

时域传输线方程描述电压和电流沿线路的传播：

$$-\frac{\partial v(x,t)}{\partial x} = L\frac{\partial i(x,t)}{\partial t} + Ri(x,t)$$

$$-\frac{\partial i(x,t)}{\partial x} = C\frac{\partial v(x,t)}{\partial t} + Gv(x,t)$$

其中：
- $v(x,t)$、$i(x,t)$：沿线路位置$x$和时间$t$的电压、电流
- $L$、$R$、$C$、$G$：单位长度电感、电阻、电容、电导

**物理意义**：第一个方程表示电压梯度由电感压降和电阻压降组成；第二个方程表示电流梯度由电容电流和电导电流组成。

### 2. 特性阻抗与传播常数

频域中，特性阻抗和传播常数是描述传输线行为的两个核心参数：

**特性阻抗**（Characteristic Impedance）：

$$Z_c(\omega) = \sqrt{\frac{R(\omega) + j\omega L(\omega)}{G(\omega) + j\omega C(\omega)}}$$

**传播常数**（Propagation Constant）：

$$\gamma(\omega) = \sqrt{[R(\omega) + j\omega L(\omega)][G(\omega) + j\omega C(\omega)]} = \alpha(\omega) + j\beta(\omega)$$

其中：
- $\alpha(\omega)$：衰减常数（Neper/m），表示行波幅值的衰减
- $\beta(\omega)$：相位常数（rad/m），表示行波的相位变化

### 3. 行波理论

电压和电流可分解为前行波和反行波的叠加：

$$v(x,t) = v^+(x - vt) + v^-(x + vt)$$

$$i(x,t) = \frac{v^+(x - vt)}{Z_c} - \frac{v^-(x + vt)}{Z_c}$$

其中$v^+$和$v^-$分别表示正向和反向行波分量，$v$为行波传播速度。

### 4. 频变参数模型

实际线路的$R$、$L$、$C$参数具有频率依赖性：

- **集肤效应**：导体交流电阻随频率增加而增大，$R(\omega) \propto \sqrt{\omega}$
- **大地返回路径**：大地阻抗的频率相关性由Carson公式描述
- **绝缘介质**：介质损耗角正切$\tan\delta$随频率变化

## EMT建模方法

传输线理论的EMT建模涉及多种数值方法，根据精度和效率需求选择：

### 5.1 贝杰龙模型（Bergeron Model）

将分布参数线路等效为集中参数的无损线，加上历史电流源项：

$$i_k(t) = \frac{1}{Z_c}[v_m(t-\tau) - v_m(t+\tau)] + i_m(t-\tau)$$

适用于宽频暂态仿真，步长可较大。

### 5.2 频率相关贝杰龙模型（Frequency-Dependent Bergeron）

在贝杰龙模型基础上考虑频率相关参数，通过向量拟合（Vector Fitting）技术获得宽频阻抗特性。

### 5.3 通用线路模型（Universal Line Model, ULM）

Zanon等（2021）提出的高精度模型，通过时滞均衡和有理函数拟合实现宽频高精度。

### 5.4 时域等值电路法（Time-Domain Equivalent Circuit）

将频域阻抗/导纳通过递归卷积或Admittance Fitting技术转换为时域等值电路。

### EMT建模精度对比

| 模型类型 | 步长要求 | 频率范围 | 计算效率 | 实现复杂度 |
|---------|---------|---------|---------|-----------|
| 贝杰龙 | Δt ≤ 2τ | 全频段 | 最高 | 低 |
| 频变贝杰龙 | Δt ≤ 2τ | 宽频 | 高 | 中 |
| ULM | Δt ≥ τ | 宽频 | 高 | 中 |
| 时域等值 | Δt < 最小时间常数 | 宽频 | 中 | 高 |

注：$\tau = l/v$为行波传播延迟，$l$为线路长度，$v$为行波速度。

## 形式化表达

### 行波速度

$$v = \frac{1}{\sqrt{LC}} \approx \frac{c}{\sqrt{\varepsilon_r}}$$

架空线典型值：$v \approx 3 \times 10^8$ m/s（光速的$1/\sqrt{\varepsilon_r}$倍）

### 无损线简化

当$R=0, G=0$时（无损线假设）：

$$Z_c = \sqrt{\frac{L}{C}} \quad \text{（实数）}$$

$$\gamma = j\omega\sqrt{LC} = j\beta \quad \text{（纯虚数，无衰减）}$$

### 反射系数

在阻抗不连续点（如故障点、线路末端），反射系数为：

$$\Gamma = \frac{Z_L - Z_c}{Z_L + Z_c}$$

其中$Z_L$为负载阻抗，$\Gamma = 1$（全反射）、$\Gamma = 0$（完全匹配）、$\Gamma = -1$（全反相反射）。

### 耦合传输线方程（多导体系统）

对于$N$导体系统，电报方程写为矩阵形式：

$$-\frac{\partial \mathbf{v}(x,t)}{\partial x} = \mathbf{L}\frac{\partial \mathbf{i}(x,t)}{\partial t} + \mathbf{R}\mathbf{i}(x,t)$$

$$-\frac{\partial \mathbf{i}(x,t)}{\partial x} = \mathbf{C}\frac{\partial \mathbf{v}(x,t)}{\partial t} + \mathbf{G}\mathbf{v}(x,t)$$

其中$\mathbf{L}$、$\mathbf{R}$、$\mathbf{C}$、$\mathbf{G}$为$N \times N$单位长度参数矩阵。

## 关键技术挑战

### 挑战1：频变参数的精确计算

大地返回路径的阻抗计算涉及Carson公式或Pollaczek积分，对于多层土壤需要进一步广义化。参数计算的精度直接影响EMT仿真的准确性。

**代表数据**：Gustavsen（2012）指出，当土壤电阻率$\rho > 100\ \Omega\cdot m$时，Carson公式的近似误差可达5-15%。

### 挑战2：准TEM假设的有效性

传输线理论基于准横电磁波（Quasi-TEM）假设，但当地下电缆或高电阻率土壤中频率较高时，非TEM场结构会导致误差。

**代表数据**：Duarte等（2023）验证表明，对于50-100m电缆、土壤电阻率高达1000 Ωm、脉冲上升时间低至0.2 µs，传输线理论仍与全波FDTD方法吻合良好；但对于 Lateral excitation 且高土壤电阻率情况下，早期时段的偏差更为显著。

### 挑战3：数值稳定性与数值色散

离散化过程中的数值色散会导致虚假振荡，尤其在行波速度与数值波速不匹配时。

### 挑战4：非线性效应处理

当线路附近发生绝缘击穿（电弧）或铁磁谐振时，参数不再是线性的，需要迭代求解或特殊处理。

### 挑战5：模态域与相域的转换

多导体传输线通过模态变换解耦为独立单线，但变换矩阵的频率相关性增加了计算复杂度。

## 量化性能边界

### 传输线理论有效性范围（Duarte等 2023验证数据）

| 参数 | 验证条件 | 结论 |
|------|---------|------|
| 电缆长度 | 50m, 100m | 短电缆段的自然频率可达数百kHz，传输线理论仍有效 |
| 土壤电阻率 | 200 Ωm, 1000 Ωm | 即使高电阻率土壤，TL与FDTD仍吻合良好 |
| 上升时间 | 0.2 µs（相当于5MHz带宽） | 快前沿暂态可使用传输线理论 |
| 激励类型 | 纵向激励、Lateral激励 | 纵向激励吻合更好，Lateral激励需注意 |

**计算效率对比**：Duarte等（2023）报告，FDTD方法耗时约数小时，而传输线理论方法仅需数秒，效率提升约1000倍以上。

### Kurokawa等（2006）参数提取结果

| 测试条件 | 参数范围 | 频率范围 |
|---------|---------|---------|
| 440kV, 500km线路 | L≈0.89-1.10 mH/km, C≈11-12 nF/km | 10 Hz - 10 kHz |
| 土壤电阻率影响 | 当ρ>100 Ωm时，参数偏差增加 | — |

## 适用边界与选择指南

### 适用条件

- 线路长度大于波长（或大于几十公里）
- 关心暂态过程（雷击、开关操作）
- 频率足够高（>1kHz）
- 分布参数效应显著

### 失效边界

| 边界类型 | 原因 | 替代方案 |
|---------|------|---------|
| **短线路**（<1km） | 可用集总π型模型简化 | π型等值电路 |
| **极低频**（<100Hz） | 稳态分析无需行波理论 | 工频分析 |
| **非均匀线路** | 需要分段建模 | 分段级联模型 |
| **非线性效应**（电弧、铁磁谐振） | 参数非线性 | 非线性迭代求解 |
| **极高频**（>10MHz） | 辐射效应显著 | 全波电磁模型 |

### 方法选择决策表

| 场景 | 推荐模型 | 步长约束 |
|-----|---------|---------|
| 机电暂态（<1kHz） | 集总参数模型 | 无限制 |
| 电磁暂态常规（10Hz-10kHz） | 贝杰龙/频变贝杰龙 | Δt ≤ τ |
| 宽频电磁暂态（0-10MHz） | ULM/时域等值 | Δt < 最小特征时间 |
| 雷电/快前沿（>1MHz） | 频变线路模型+递归卷积 | Δt ≤ 1μs |
| 非线性暂态 | 迭代求解+动态步长 | 自适应 |

## 与相关页面的关系

- [[transmission-line-model]] - 输电线路模型（具体的线路建模实现）
- [[bergeron-model]] - 贝杰龙模型（EMT中广泛使用的传输线模型）
- [[frequency-dependent-line-model]] - 频变线路模型（考虑参数频率依赖性）
- [[wideband-modeling]] - 宽频建模（涵盖DC到高频的系统建模方法）
- [[distributed-parameter-line]] - 分布参数线路（具体的分布参数实现）
- [[quasi-tem-approximation]] - 准TEM假设（传输线理论的场论基础）
- [[electromagnetic-transient]] - 电磁暂态（EMT仿真的总体领域）
- [[power-system-network]] - 电力系统网络（网络方程与建模）
- [[emt-simulation]] - EMT仿真（仿真方法总览）
- [[real-time-simulation]] - 实时仿真（实时约束下的传输线建模）
- [[co-simulation]] - 混合仿真（机电-电磁混合仿真中的传输线接口）

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| [[assessment-of-the-transmission-line-theory-in-the-modeling-of-multiconductor-und]] | 2023 | Duarte等：验证传输线理论对50-100m短电缆、1000Ωm高土壤电阻率、快前沿0.2µs暂态的有效性 |
| [[high-frequency-transients-in-buried-insulated-wires-transmission-line-simulation]] | 2024 | Alipio等：埋地绝缘导线快暂态实验验证，证明地回路参数公式的可靠性 |
| [[efficient-modeling-of-parallel-counterpoise-wires-using-an-fdtd-based-transmissi]] | 2025 | Duarte等：平行接地极FDTD建模与传输线理论对比 |
| Kurokawa等 2006 | 2006 | 传输线参数提取的新方法，Carson/Pollaczek方程应用 |
| Wedepohl 1963 | 1963 | 多导体系统行波现象的矩阵方法奠基性工作 |
| Dommel 1969 | 1969 | EMTP参考手册，电磁暂态程序的理论基础 |

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*