---
title: "相域建模 (Phase-Domain Modeling)"
type: topic
tags: [phase-domain, modeling, transmission-line, cable, unbalance, modal-transformation, coupling, frequency-dependent, synchronous-machine, emtp]
created: "2026-05-02"
updated: "2026-05-14"
---

# 相域建模 (Phase-Domain Modeling)

## 定义

相域建模（Phase-Domain Modeling）是在原始相坐标（通常为 $abc$ 三相或更多相）下直接表示输电线路、地下电缆、变压器、同步电机、换流器及故障的电磁暂态（EMT）建模路线。其核心思想是**保留完整的相间耦合矩阵**，不通过模态变换或序分量变换进行解耦，从而在时域中直接求解多导体系统的耦合微分方程。

与模域（Modal-Domain）和序分量（Symmetrical-Component）方法不同，相域建模不要求系统具有对称性、换位均匀性或恒定变换矩阵。它的价值在于对非换位线路、地下多芯电缆、平行线路、单相接地故障、开关不同期操作和不平衡负荷等场景的原生表达能力——这些场景在模域中可能因变换矩阵强频变、非对角或复数化而引入额外误差。

相域建模的代价是**满矩阵耦合**带来的计算复杂度上升。每个多导体元件的等效导纳矩阵 $Y_{\mathrm{eq}}$ 通常不是对角矩阵，非对角项表示相间耦合，在大规模网络中会显著增加节点导纳矩阵的带宽和求解成本。

## EMT 中的角色

相域建模在 EMT 仿真中承担以下关键角色：

**1. 非对称与耦合系统的原生建模**

非换位架空线路、地下多芯电缆、平行双回线和多导体系统的相间耦合必须在相域中精确表示。以多导体架空线为例，单位长度参数为 $R_{abc}(\omega)$、$L_{abc}(\omega)$、$G_{abc}(\omega)$、$C_{abc}(\omega)$ 等矩阵，其中非对角元素刻画了相间互感和互容。若强行使用模域变换，当变换矩阵本身强频变时（如非换位线路的 Clarke 变换不再为实常数），模域解耦会引入额外误差。

**2. 不平衡故障与保护分析**

单相接地、相间短路、开关不同期、不平衡负荷等工况天然以相域描述。相域模型可直接耦合详细开关模型、饱和变压器、换流器和保护装置，无需在相域与序域之间反复转换。

**3. 频变参数的直接时域嵌入**

相域频变线路模型（如 ULM、FDPD）通过矢量拟合（Vector Fitting）将特征导纳矩阵 $Y_c(s)$ 和传播函数矩阵 $H(s)$ 转化为有理逼近的极点—留数形式，再通过递归卷积嵌入时域。相域避免了模域中每模态不同传播速度导致的变换矩阵频变问题。

**4. 多相电机的直接节点接入**

十二相、六相等多相同步电机在综合电力系统（舰船、航空器）中应用广泛。相域模型可将电机以 Norton 等效形式直接并入 EMTP 类节点分析网络，避免 qd0 模型通过预测电流源接口耦合带来的数值不稳定问题。

## 核心机制

### 1. 相域输电线路与电缆模型

相域输电线路模型以多导体电报方程为基础：

$$
-\frac{\partial v_{abc}(x,t)}{\partial x} = R_{abc}(\omega) i_{abc}(x,t) + L_{abc}(\omega) \frac{\partial i_{abc}(x,t)}{\partial t}
$$

$$
-\frac{\partial i_{abc}(x,t)}{\partial x} = G_{abc}(\omega) v_{abc}(x,t) + C_{abc}(\omega) \frac{\partial v_{abc}(x,t)}{\partial t}
$$

其中 $v_{abc}$ 和 $i_{abc}$ 分别为相电压和相电流向量，$R_{abc}$、$L_{abc}$、$G_{abc}$、$C_{abc}$ 为单位长度电阻、电感、电导和电容矩阵（可为频率的函数）。

#### 1.1 常参数相域模型（CP）

对于短线路或低频近似，参数可视为与频率无关的常数矩阵。离散化为诺顿等效伴随模型：

$$
i_{abc,k}(t) = Y_{\mathrm{eq},abc} v_{abc,k}(t) + i^{\mathrm{hist}}_{abc,k}(t)
$$

其中 $Y_{\mathrm{eq},abc}$ 为常数等效导纳矩阵，$i^{\mathrm{hist}}$ 为历史电流源（由前一时刻的电压和电流决定）。Bergeron 行波模型是此类模型的经典实现，利用特征阻抗 $Z_c = \sqrt{(R+j\omega L)/(G+j\omega C)}$ 和传播常数 $\gamma = \sqrt{(R+j\omega L)(G+j\omega C)}$ 将线路表示为集中参数 $\pi$ 型电路加行波延迟。

**适用场景**：短线路（< 50 km）、低频暂态（工频至数千赫兹）、换位良好的架空线路。

**局限性**：无法准确模拟集肤效应、大地回流的频率相关特性、长线路的分布参数效应。

#### 1.2 频变相域模型（FDPD）

架空线路和电缆的集肤效应与大地回流导致参数随频率变化。特征导纳矩阵 $Y_c(s)$ 和传播函数矩阵 $H(s)$ 需在宽频范围内进行有理逼近。

**矢量拟合（VF）方法**：将 $Y_c(s)$ 和 $H(s)$ 拟合为极点—留数形式：

$$
Y_c(s) = D + \sum_{k=1}^{N} \frac{R_k}{s - p_k}
$$

其中 $D$ 为常数矩阵，$p_k$ 为极点，$R_k$ 为留数矩阵。时域卷积通过一阶递归状态量更新：

$$
x_{Y_c}(t) = \alpha_{Y_c} x_{Y_c}(t-\Delta t) + v_k(t-\Delta t)
$$

$$
i^{\mathrm{hist}}_{Y_c}(t) = c_{Y_c} x_{Y_c}(t)
$$

其中 $\alpha_{Y_c} = e^{p_k \Delta t}$，$c_{Y_c}$ 为缩放系数。

**ULM（Universal Line Model）方法**：Noda 2015 提出将频域分区拟合（FpF）引入 ULM 相域线路建模。FpF 用频率分区和自适应加权替代传统 VF，将频率范围按性质分为低频区、谐振附近区、高频衰减区等子区间，在各分区内独立辨识极点，再组合为矩阵等值。传播函数矩阵沿用 ULM 显式时延思想，因为不同模态的行波传播时间不同，会在时域响应中产生阶跃变化。

**量化性能**（Duarte 2023, Noda 2015）：
- FDPD 模型在 500 kV 双回架空线验证中，与严格数值拉普拉斯变换法对比的暂态波形误差 < 2%
- FpF-ULM 相域模型在 500 kV 双回线现场试验验证中，频响拟合误差在 10 Hz–1 MHz 范围内 < 1.5%
- 对于 9 芯地下电缆系统（高残差/极点比），改进版 ULM 在 0.1% 拟合容差下仍保持时域稳定，而旧版 ULM 在相同条件下发散

#### 1.3 多尺度频变相域模型

Gustavsen 2017 提出多尺度频变相域线路模型，核心思想是**在不同时间尺度上使用不同的时间步长**：在电磁暂态期间使用微秒级步长跟踪行波传播，在机电暂态期间使用毫秒级步长。

多尺度模型的关键公式为解析信号处理：

$$
S[s(t-T_{\mathrm{wp}})] = \kappa^{-1} S\left[s\left(t - (\kappa-1)\tau\right)\right]
$$

其中 $T_{\mathrm{wp}}$ 为行波传播时间，$\tau$ 为基础步长，$\kappa = \lceil T_{\mathrm{wp}}/\tau \rceil$。

**量化性能**（Gustavsen 2017）：
- 在 525 kV 双回线 energization 测试中，机电暂态期间时间步长可从 5 μs 增大至 2 ms，步长放大因子达 **400 倍**
- 在 IEEE 118 节点系统验证中，多尺度模型在机电暂态阶段的计算加速比达 **200–400 倍**
- 验证系统：525 kV 双回线（Raver–Schultz 变电站），线路长度约 200 km，三相故障 energization

### 2. 相域同步电机模型

同步电机在相域建模中的核心挑战是**转子位置相关的电感矩阵**导致等效导纳随时间变化，每次时间步都需要重新分解网络矩阵。

#### 2.1 传统相域模型（PD）

PD 模型以 abc 相坐标直接表示定子绕组，转子绕组（励磁和阻尼）通过相域电感矩阵与定子耦合。连续时间模型为：

$$
v_{abc}(t) = R_s i_{abc}(t) + \frac{d\lambda_{abc}(t)}{dt}
$$

$$
\lambda_{abc}(t) = L_{s}(\theta_r(t)) i_{abc}(t) + L_{sr}(\theta_r(t)) i_{r}(t)
$$

其中 $L_s(\theta_r)$ 和 $L_{sr}(\theta_r)$ 为转子位置 $\theta_r(t)$ 的函数。离散化为 Norton 等效后，等效导纳矩阵 $Y_{\mathrm{eq}}(\theta_r)$ 随转子位置变化，导致网络矩阵每步更新。

**局限性**：在大规模网络中，每步重新因子分解网络导纳矩阵的计算成本极高。

#### 2.2 恒定电导相域模型（CC-PD）

CC-PD 模型通过引入**人工阻尼绕组**实现恒定等效导纳。人工绕组的参数经过精心设计，使得电机对网络呈现恒定电导矩阵。

**局限性**：人工绕组的参数选择引入额外物理假设，可能影响高频暂态精度。Xia 2019 指出人工绕组在高频下可能引入非物理的衰减特性。

#### 2.3 高效相域模型（E-PD）

Xia 2019 提出 E-PD 模型，通过**公式重构**将转子位置相关项从诺顿导纳中转移到历史电流源中，使电机对网络呈现"恒定诺顿导纳并联受控电流源"。

核心机制：对传统离散 PD 方程进行 Park 变换分解，将可写成常数矩阵的部分保留为等效电阻/导纳，将含转子角的耦合项并入历史电压源。每步计算时，求解器用恒定导纳和上一时步形成的受控电流源求端电压。

**量化性能**（Xia 2019, IEEE TPWRD 2019）：
- 845 MVA 圆柱转子同步电机算例：E-PD 每步计算 **175 FLOPs**，低于 VBR 的 298 FLOPs 和 CC-PD 的 316 FLOPs
- 10 机 New England 系统（39 节点）故障仿真：E-PD 总仿真时间比 VBR 减少约 15%，比 CC-PD 减少约 20%
- 在 1 ms 步长下单相接地故障测试中，CC-PD 模型在定子电流中产生约 1.17% 的最大误差，而 E-PD 和 VBR 在相同步长下误差 < 0.5%
- 50 μs 小步长下所有模型均准确，无明显差异

#### 2.4 十二相电机相域模型（Gao 2022）

Gao 2022 首次面向 EMTP 节点分析框架建立十二相同步机的相域 PD 模型，并提出恒定电导 CC-PD 模型和嵌入式小步长算法。

十二相同步机由四组三相定子绕组构成，绕组间存在复杂磁耦合。PD 模型将十二相机直接放入相域节点分析框架，避免 qd0 模型通过预测电流源接口耦合带来的数值不稳定问题。

**嵌入式小步长算法**：外部网络仍按较大步长推进，对电机内部状态采用更小子步长更新，降低大步长下电机磁链和电流积分误差。

### 3. 相域频变电缆模型

地下电缆的频变参数建模是相域建模中最为复杂的场景之一，因为电缆具有多芯、多屏蔽层结构，导体数量可达数十甚至上百。

#### 3.1 宽频电缆模型（Ramirez 2024）

Ramirez 2024 提出三项改进的宽频线路/电缆建模技术：

**（1）相位角展开优化**：通过提取最优时间延迟使传播函数相位角在拟合频段内保持连续，避免相位卷绕（phase unwinding）导致的拟合误差。

**（2）传播模态分组策略**：基于时间延迟的接近程度对传播模态进行分组。延迟相近的模态归为同一组，使用统一的代表延迟。例如，对于延迟 [45.4071, 48.4183, 48.4263] μs 的三个模态，分组后代表延迟为 45.4071 μs。

**（3）快速衰减模态的拟合频率限制**：当模态幅值低于阈值时，限制其最大拟合频率，减少相位卷绕和拟合阶数。

**量化性能**（Ramirez 2024, IEEE TPWRD 2024）：
- 9 芯地下电缆系统（高残差/极点比）：改进版 ULM 在 0.1% 拟合容差下保持时域稳定，旧版 ULM 在相同条件下发散
- 96 芯混合线路系统：改进版 ULM 获得更紧凑的延迟组（5 组 vs 旧版 4 组），总拟合阶数降低约 30%
- 11 芯架空-电缆混合系统：改进版在所有拟合容差（5%、1%、0.5%、0.1%）下均产生稳定时域解，旧版仅在 5% 容差下稳定
- 非对称双回电缆系统：改进版在 1% 和 0.5% 容差下均稳定，旧版在 0.5% 容差下发散

#### 3.2 电缆参数计算

电缆的频变参数需通过全波 FDTD 方法或闭合近似公式计算。Duarte 2023 评估了传输线理论在多芯地下电缆系统建模中的适用性，指出：

- 对于低频（< 10 kHz），集肤效应可用经典修正公式近似
- 对于高频（> 100 kHz），全波 FDTD 方法更准确，但计算成本高
- 275 kV 油压电缆的频变参数在 1 Hz–1 MHz 范围内变化可达 3–5 倍

### 4. 相域-模域混合建模

在某些场景下，可在内部使用模态传播的线路模型，在网络接口处回到相域。这种混合方法在保持计算效率的同时，在故障分析和保护动作时刻切换回相域。

**混合建模的关键问题**：
- 模态变换矩阵的频变性和非对角性
- 相域-模域接口的数值稳定性
- 非换位线路中模态变换矩阵的常数近似误差

## 形式化表达

### 多导体相域电报方程

$$
-\frac{\partial \mathbf{v}_{abc}(x,t)}{\partial x} = \mathbf{R}_{abc} \mathbf{i}_{abc}(x,t) + \mathbf{L}_{abc} \frac{\partial \mathbf{i}_{abc}(x,t)}{\partial t}
$$

$$
-\frac{\partial \mathbf{i}_{abc}(x,t)}{\partial x} = \mathbf{G}_{abc} \mathbf{v}_{abc}(x,t) + \mathbf{C}_{abc} \frac{\partial \mathbf{v}_{abc}(x,t)}{\partial t}
$$

### 诺顿等效伴随模型（通用形式）

$$
\mathbf{i}_k(t) = \mathbf{Y}_{\mathrm{eq},abc} \mathbf{v}_k(t) + \mathbf{i}^{\mathrm{hist}}_k(t)
$$

其中 $\mathbf{Y}_{\mathrm{eq},abc}$ 为相域等效导纳矩阵（非对角），$\mathbf{i}^{\mathrm{hist}}_k(t)$ 为历史电流源。

### 频变模型递归卷积

$$
\mathbf{Y}_c(s) = \mathbf{D} + \sum_{k=1}^{N} \frac{\mathbf{R}_k}{s - p_k}
$$

$$
\mathbf{x}_{Y_c}(t) = e^{\mathbf{p} \Delta t} \mathbf{x}_{Y_c}(t-\Delta t) + \mathbf{v}_k(t-\Delta t)
$$

$$
\mathbf{i}^{\mathrm{hist}}_{Y_c}(t) = \mathbf{c}_{Y_c} \mathbf{x}_{Y_c}(t)
$$

### ULM 传播函数

$$
\mathbf{H}(s) = \mathbf{H}_{\mathrm{rational}}(s) + \mathbf{H}_{\mathrm{delay}}(s)
$$

其中 $\mathbf{H}_{\mathrm{rational}}(s)$ 为有理部分（通过 VF 或 FpF 拟合），$\mathbf{H}_{\mathrm{delay}}(s)$ 为显式时延项。

### 多尺度时间步长切换

$$
\kappa = \left\lceil \frac{T_{\mathrm{wp}}}{\tau} \right\rceil, \quad \text{步长放大因子} = \frac{T_{\mathrm{step, large}}}{\tau}
$$

### 同步电机相域方程

$$
\mathbf{v}_{abc}(t) = \mathbf{R}_s \mathbf{i}_{abc}(t) + \frac{d\boldsymbol{\lambda}_{abc}(t)}{dt}
$$

$$
\boldsymbol{\lambda}_{abc}(t) = \mathbf{L}_s(\theta_r(t)) \mathbf{i}_{abc}(t) + \mathbf{L}_{sr}(\theta_r(t)) \mathbf{i}_r(t)
$$

### E-PD 恒定导纳分解

$$
\mathbf{Y}_{\mathrm{eq}}^{\mathrm{E-PD}} = \mathbf{Y}_{\mathrm{const}} \quad (\text{与 } \theta_r \text{ 无关})
$$

$$
\mathbf{i}^{\mathrm{hist}}_{\mathrm{E-PD}}(t) = \mathbf{f}(\theta_r(t), \mathbf{v}(t-\Delta t), \mathbf{i}(t-\Delta t))
$$

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 520" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#333"/>
    </marker>
    <filter id="shadow" x="-2%" y="-2%" width="104%" height="104%">
      <feDropShadow dx="1" dy="1" stdDeviation="1" flood-color="#00000033"/>
    </filter>
  </defs>

  <text x="450" y="22" fill="#555" font-size="11" text-anchor="middle" font-weight="bold">第一层 · 物理系统 (输入)</text>
  <rect x="30" y="35" width="150" height="42" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2" filter="url(#shadow)"/>
  <text x="105" y="52" fill="#1e3a5f" font-size="12" font-weight="bold" text-anchor="middle">非换位架空线</text>
  <text x="105" y="67" fill="#4b6b8f" font-size="9" text-anchor="middle">三相耦合 + 频变参数</text>

  <rect x="200" y="35" width="150" height="42" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2" filter="url(#shadow)"/>
  <text x="275" y="52" fill="#1e3a5f" font-size="12" font-weight="bold" text-anchor="middle">地下多芯电缆</text>
  <text x="275" y="67" fill="#4b6b8f" font-size="9" text-anchor="middle">芯-屏蔽-铠装耦合</text>

  <rect x="370" y="35" width="150" height="42" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2" filter="url(#shadow)"/>
  <text x="445" y="52" fill="#1e3a5f" font-size="12" font-weight="bold" text-anchor="middle">同步电机/换流器</text>
  <text x="445" y="67" fill="#4b6b8f" font-size="9" text-anchor="middle">转子位置相关电感</text>

  <rect x="540" y="35" width="150" height="42" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2" filter="url(#shadow)"/>
  <text x="615" y="52" fill="#1e3a5f" font-size="12" font-weight="bold" text-anchor="middle">不平衡故障/开关</text>
  <text x="615" y="67" fill="#4b6b8f" font-size="9" text-anchor="middle">单相接地/不同期</text>

  <rect x="710" y="35" width="160" height="42" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2" filter="url(#shadow)"/>
  <text x="790" y="52" fill="#1e3a5f" font-size="12" font-weight="bold" text-anchor="middle">多相电机(12/6相)</text>
  <text x="790" y="67" fill="#4b6b8f" font-size="9" text-anchor="middle">综合电力系统</text>

  <line x1="450" y1="77" x2="450" y2="95" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <text x="450" y="112" fill="#555" font-size="11" text-anchor="middle" font-weight="bold">第二层 · 相域参数计算 (处理)</text>
  <rect x="30" y="120" width="200" height="42" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>
  <text x="130" y="137" fill="#14532d" font-size="12" font-weight="bold" text-anchor="middle">R/L/G/C 矩阵</text>
  <text x="130" y="152" fill="#3a7a5a" font-size="9" text-anchor="middle">单位长度参数</text>

  <rect x="250" y="120" width="200" height="42" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>
  <text x="350" y="137" fill="#14532d" font-size="12" font-weight="bold" text-anchor="middle">特征导纳 Yc(s)</text>
  <text x="350" y="152" fill="#3a7a5a" font-size="9" text-anchor="middle">频变 --> 有理逼近</text>

  <rect x="470" y="120" width="200" height="42" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>
  <text x="570" y="137" fill="#14532d" font-size="12" font-weight="bold" text-anchor="middle">传播函数 H(s)</text>
  <text x="570" y="152" fill="#3a7a5a" font-size="9" text-anchor="middle">时延 + 有理部分</text>

  <rect x="690" y="120" width="180" height="42" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>
  <text x="780" y="137" fill="#14532d" font-size="12" font-weight="bold" text-anchor="middle">电感矩阵 L(theta_r)</text>
  <text x="780" y="152" fill="#3a7a5a" font-size="9" text-anchor="middle">转子位置相关</text>

  <line x1="130" y1="162" x2="130" y2="185" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="350" y1="162" x2="350" y2="185" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="570" y1="162" x2="570" y2="185" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="780" y1="162" x2="780" y2="185" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <text x="450" y="202" fill="#555" font-size="11" text-anchor="middle" font-weight="bold">第三层 · 离散化方法 (算法)</text>
  <rect x="30" y="210" width="190" height="42" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="2" filter="url(#shadow)"/>
  <text x="125" y="227" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">常参数模型 (CP)</text>
  <text x="125" y="242" fill="#a16207" font-size="9" text-anchor="middle">Bergeron / Pi型</text>

  <rect x="240" y="210" width="190" height="42" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="2" filter="url(#shadow)"/>
  <text x="335" y="227" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">频变模型 (FDPD)</text>
  <text x="335" y="242" fill="#a16207" font-size="9" text-anchor="middle">VF / FpF + 递归卷积</text>

  <rect x="450" y="210" width="190" height="42" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="2" filter="url(#shadow)"/>
  <text x="545" y="227" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">ULM 通用线路模型</text>
  <text x="545" y="242" fill="#a16207" font-size="9" text-anchor="middle">显式时延 + MPFE</text>

  <rect x="660" y="210" width="210" height="42" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="2" filter="url(#shadow)"/>
  <text x="765" y="227" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">E-PD / CC-PD 电机模型</text>
  <text x="765" y="242" fill="#a16207" font-size="9" text-anchor="middle">恒定导纳 + 历史源</text>

  <line x1="125" y1="252" x2="125" y2="275" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="335" y1="252" x2="335" y2="275" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="545" y1="252" x2="545" y2="275" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="765" y1="252" x2="765" y2="275" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <text x="450" y="292" fill="#555" font-size="11" text-anchor="middle" font-weight="bold">第四层 · 网络方程求解 (处理)</text>
  <rect x="100" y="300" width="260" height="42" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>
  <text x="230" y="317" fill="#14532d" font-size="12" font-weight="bold" text-anchor="middle">Norton 等效伴随模型</text>
  <text x="230" y="332" fill="#3a7a5a" font-size="9" text-anchor="middle">i = Y_eq * v + i_hist</text>

  <rect x="400" y="300" width="260" height="42" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>
  <text x="530" y="317" fill="#14532d" font-size="12" font-weight="bold" text-anchor="middle">节点导纳矩阵组装</text>
  <text x="530" y="332" fill="#3a7a5a" font-size="9" text-anchor="middle">满矩阵耦合 + 相间耦合</text>

  <rect x="690" y="300" width="180" height="42" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>
  <text x="780" y="317" fill="#14532d" font-size="12" font-weight="bold" text-anchor="middle">LU 因子分解</text>
  <text x="780" y="332" fill="#3a7a5a" font-size="9" text-anchor="middle">高斯消元 / 迭代法</text>

  <line x1="230" y1="342" x2="230" y2="365" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="530" y1="342" x2="530" y2="365" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="780" y1="342" x2="780" y2="365" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <text x="450" y="382" fill="#555" font-size="11" text-anchor="middle" font-weight="bold">第五层 · 输出结果</text>
  <rect x="30" y="390" width="190" height="42" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="2" filter="url(#shadow)"/>
  <text x="125" y="407" fill="#3b0764" font-size="12" font-weight="bold" text-anchor="middle">相电压/电流波形</text>
  <text x="125" y="422" fill="#6b21a8" font-size="9" text-anchor="middle">v_abc(t), i_abc(t)</text>

  <rect x="240" y="390" width="190" height="42" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="2" filter="url(#shadow)"/>
  <text x="335" y="407" fill="#3b0764" font-size="12" font-weight="bold" text-anchor="middle">过电压/过电流</text>
  <text x="335" y="422" fill="#6b21a8" font-size="9" text-anchor="middle">暂态峰值 + 行波</text>

  <rect x="450" y="390" width="190" height="42" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="2" filter="url(#shadow)"/>
  <text x="545" y="407" fill="#3b0764" font-size="12" font-weight="bold" text-anchor="middle">不平衡度 / THD</text>
  <text x="545" y="422" fill="#6b21a8" font-size="9" text-anchor="middle">负序 + 零序分量</text>

  <rect x="660" y="390" width="210" height="42" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="2" filter="url(#shadow)"/>
  <text x="765" y="407" fill="#3b0764" font-size="12" font-weight="bold" text-anchor="middle">保护动作 / 故障判据</text>
  <text x="765" y="422" fill="#6b21a8" font-size="9" text-anchor="middle">距离保护 / 差动保护</text>

  <rect x="200" y="455" width="500" height="45" rx="4" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="6,3"/>
  <text x="450" y="472" fill="#7f1d1d" font-size="11" font-weight="bold" text-anchor="middle">关键挑战：满矩阵耦合 --> 计算成本 | 频变拟合 --> 无源性风险 | 大步长 --> 积分误差</text>
  <text x="450" y="488" fill="#b91c1c" font-size="9" text-anchor="middle">应对：稀疏化 / 多尺度 / 模态分组 / 嵌入式小步长 / 并行求解</text>

  <text x="30" y="515" fill="#333" font-size="10" font-weight="bold">图例：</text>
  <rect x="60" y="505" width="14" height="10" rx="2" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="78" y="514" fill="#555" font-size="9">物理输入</text>
  <rect x="140" y="505" width="14" height="10" rx="2" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="158" y="514" fill="#555" font-size="9">处理/模型</text>
  <rect x="230" y="505" width="14" height="10" rx="2" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="248" y="514" fill="#555" font-size="9">算法/方法</text>
  <rect x="320" y="505" width="14" height="10" rx="2" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="338" y="514" fill="#555" font-size="9">输出结果</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 相域建模五层架构：物理系统 --> 相域参数计算 --> 离散化方法 --> 网络方程求解 --> 输出结果</p>

## 关键技术挑战

### 挑战 1：满矩阵耦合的计算成本

相域模型的等效导纳矩阵 $\mathbf{Y}_{\mathrm{eq},abc}$ 通常不是对角矩阵，非对角项表示相间耦合。在大规模网络中，这会导致节点导纳矩阵的带宽显著增加，LU 因子分解的计算复杂度从 $O(n)$ 升至 $O(n^{1.5-2})$（$n$ 为节点数）。

**应对策略**：
- 稀疏化：利用网络拓扑的稀疏性，仅存储非零元素
- 分区/等值：将远距离弱耦合区域等值为较小模型
- 并行求解：利用 GPU 或多线程加速矩阵运算
- 多尺度：在机电暂态阶段使用大步长减少求解次数

### 挑战 2：频变参数的有理逼近稳定性

相域频变模型需要将特征导纳矩阵 $\mathbf{Y}_c(s)$ 和传播函数矩阵 $\mathbf{H}(s)$ 拟合为稳定的有理函数。VF 和 FpF 方法在拟合多变量矩阵时可能产生非物理极点（右半平面极点）或违反无源性。

**应对策略**：
- 无源性强制（Passivity Enforcement）：在拟合后检测并修正非无源区域
- 相位角展开优化：通过提取最优时间延迟避免相位卷绕
- 自适应加权：在拟合误差敏感频段（如谐振附近）增加权重
- 模态分组：将延迟相近的模态分组，减少总拟合阶数

### 挑战 3：同步电机恒定导纳与精度的权衡

CC-PD 模型通过人工阻尼绕组获得恒定导纳，但可能影响高频暂态精度。E-PD 模型通过公式重构避免人工绕组，但在大步长下可能引入积分误差。

**应对策略**：
- 嵌入式小步长：电机内部使用更小子步长更新磁链
- 代数校正：使用定子直轴电流预测与代数校正，将预测量只用于形成下一步历史源
- 步长自适应：根据转子角变化速率动态调整步长

### 挑战 4：大规模电缆系统的拟合阶数

多芯电缆（如 96 芯混合系统）的频变参数矩阵维度高达 96×96，每个元素的有理逼近需要数十个极点。总拟合阶数可能超过 1000，导致内存占用和计算时间剧增。

**应对策略**：
- 模态分组：将延迟相近的模态分组，减少总拟合阶数约 30%
- 拟合容差自适应：在工程可接受范围内（如 1%）选择合适的拟合容差，避免过度拟合
- 低秩近似：利用矩阵的低秩特性减少存储和计算成本

### 挑战 5：相域-模域混合接口的数值稳定性

混合建模在模态变换矩阵强频变时可能引入数值不稳定性。相域-模域接口处的离散化方法（如梯形积分 vs 后向欧拉）会影响整体稳定性。

**应对策略**：
- 接口一致性：确保接口两侧的离散化方法兼容
- 历史项传递：正确传递相域-模域接口处的历史电流源
- 步长同步：在接口处使用兼容的时间步长

## 量化性能边界

| 模型类型 | 验证系统 | 步长 | 加速比/误差 | 来源 |
|---------|---------|------|-----------|------|
| FDPD 相域线路 | 500 kV 双回架空线 | 5 μs | 波形误差 < 2%（vs 数值 Laplace） | Noda 2015 |
| FpF-ULM 相域线路 | 500 kV 双回线（现场试验） | 10 μs | 频响拟合误差 < 1.5% (10 Hz–1 MHz) | Noda 2015 |
| 改进版 ULM | 9 芯地下电缆 | 5 μs | 0.1% 容差下稳定（旧版发散） | Ramirez 2024 |
| 改进版 ULM | 96 芯混合线路 | 5 μs | 拟合阶数降低 ~30% | Ramirez 2024 |
| 多尺度 FDPD | 525 kV 双回线 energization | 5 μs → 2 ms | 步长放大 400 倍 | Gustavsen 2017 |
| 多尺度 FDPD | IEEE 118 节点系统 | 5 μs → 2 ms | 机电暂态加速 200–400× | Gustavsen 2017 |
| E-PD 同步电机 | 845 MVA 圆柱转子 | 50 μs | 175 FLOPs/步（VBR: 298, CC-PD: 316） | Xia 2019 |
| E-PD 同步电机 | 10 机 New England (39 bus) | 1 ms | 总仿真时间比 VBR 减少 ~15% | Xia 2019 |
| E-PD 同步电机 | 845 MVA 单相接地故障 | 1 ms | CC-PD 最大误差 1.17%，E-PD < 0.5% | Xia 2019 |
| CC-PD 十二相电机 | EMTP-type 仿真 | 50 μs | 首次实现十二相电机 EMTP 节点接入 | Gao 2022 |

## 适用边界与选择指南

### 相域 vs 模域 vs 序分量选择指南

| 应用场景 | 推荐建模域 | 原因 |
|---------|----------|------|
| 非换位架空线路暂态 | 相域 | 模态变换矩阵强频变，模域解耦引入误差 |
| 地下多芯电缆系统 | 相域 | 导体数量多，模态变换复杂且频变 |
| 单相接地/相间故障 | 相域 | 天然相域描述，无需转换 |
| 换位良好的对称线路 | 模域或序分量 | 变换矩阵近似实常数，模域效率更高 |
| 工频正序响应分析 | 序分量 | 仅需正序/零序，计算量最小 |
| 大规模网络机电暂态 | 模域 + 多尺度 | 平衡精度与效率，大步长下模域更稳定 |
| 十二相/多相同步电机 | 相域 | qd0 接口不稳定，相域直接节点接入 |
| 实时仿真（FPGA） | 相域频变 | 避免模域频变变换矩阵的硬件实现复杂度 |

### 相域建模的失效场景

- **高度对称且仅关注工频正序的系统**：序分量方法计算量更小，精度足够
- **超大规模网络（> 10000 节点）的机电暂态**：满矩阵耦合导致计算成本不可接受，需等值或模域混合
- **极高频率（> 10 MHz）的开关瞬态**：集肤深度极小，需使用全波 FDTD 或频域方法，相域时域递推可能不稳定
- **参数未知或频变特性未知的系统**：相域模型的精度依赖于准确的频变参数，参数误差会直接传递到暂态结果

## 相关方法 / 相关模型 / 相关主题

### 线路与电缆建模
- [[frequency-dependent-line-model]] — 频变线路模型
- [[frequency-dependent-modeling]] — 频变建模总体
- [[distributed-parameter-model]] — 分布参数模型
- [[bergeron-model]] — Bergeron 行波模型
- [[universal-line-model]] — 通用线路模型（ULM）
- [[modal-transformation]] — 模态变换
- [[modal-domain-decoupling]] — 模域解耦
- [[transposed-three-phase-line]] — 换位三相线路
- [[parallel-transmission-line]] — 平行输电线路
- [[underground-cable-modeling]] — 地下电缆建模

### 电机与变压器
- [[synchronous-machine-model]] — 同步电机模型
- [[excitation-system]] — 励磁系统
- [[converter-transformer-model]] — 换流变压器模型

### 网络求解
- [[nodal-admittance-matrix]] — 节点导纳矩阵
- [[norton-equivalent]] — Norton 等效
- [[companion-model]] — 伴随模型
- [[compensation-method]] — 补偿法

### 不平衡与故障
- [[unbalanced-fault-analysis]] — 不平衡故障分析
- [[symmetrical-components]] — 对称分量法
- [[sequence-component-method]] — 序分量法
- [[fault-analysis]] — 故障分析

### 数值方法
- [[numerical-integration]] — 数值积分方法
- [[trapezoidal-rule]] — 梯形法则
- [[variable-time-step-solver]] — 变时间步长求解器
- [[numerical-stability]] — 数值稳定性

### 系统级
- [[emt-simulation]] — EMT 仿真基础
- [[power-system]] — 电力系统建模
- [[electromagnetic-transient]] — 电磁暂态分析
- [[real-time-simulation]] — 实时仿真技术
- [[large-scale-system-simulation]] — 大规模系统仿真

## 来源论文

- **Gustavsen 2017** ("Multi-Scale and Frequency-Dependent Modeling of Electric Power Transmission Lines") — 提出多尺度频变相域线路模型，实现电磁暂态与机电暂态的自适应步长切换，在 525 kV 系统验证中达到 400 倍步长放大因子。

- **Xia et al. 2019** ("An Efficient Phase Domain Synchronous Machine Model With Constant Equivalent Admittance Matrix", IEEE TPWRD) — 提出 E-PD 模型，通过公式重构将转子位置相关项从诺顿导纳转移到历史电流源，实现恒定导纳同步电机模型，每步计算 175 FLOPs（低于 VBR 的 298 和 CC-PD 的 316）。

- **Noda 2015** ("Application of Frequency-Partitioning Fitting to the Phase-Domain Frequency-Dependent Modeling of Overhead Transmission Lines", IEEE TPWRD) — 将频域分区拟合（FpF）引入 ULM 相域线路建模，在 500 kV 双回架空线验证中频响拟合误差 < 1.5%。

- **Ramirez et al. 2024** ("Advanced Wideband Line/Cable Modeling for Transient Studies", IEEE TPWRD) — 提出三项宽频线路/电缆建模改进技术（相位角展开优化、模态分组策略、快速衰减模态频率限制），在 96 芯混合线路系统中使拟合阶数降低约 30%。

- **Gao et al. 2022** ("Phase-Domain Model of Twelve-Phase Synchronous Machine for EMTP-Type Simulation", IJEPES) — 首次建立面向 EMTP 节点分析的十二相同步机相域模型，提出恒定电导 CC-PD 模型和嵌入式小步长算法。

- **Duarte et al. 2023** ("Assessment of the Transmission Line Theory in the Modeling of Multiconductor Underground Cable Systems", EPSR) — 评估传输线理论在多芯地下电缆系统建模中的适用性，指出全波 FDTD 在高频（> 100 kHz）下的必要性。

- **Liu et al. 2021** ("Development of Phase Domain Frequency-Dependent Transmission Line Model on FPGA for Real-Time Digital Simulator", EPSR) — 将相域频变线路模型实现于 FPGA，采用 48 位自定义浮点格式改善递归卷积舍入误差，支持微秒级实时步长。

- **Yonezawa 2023** ("A Phase-Domain Synchronous Machine Modeling Technique by Using Magnetic Circuit Representation", EPSR) — 利用磁路表示建立相域同步机建模技术，为相域电机模型提供磁饱和和非线性效应的建模框架。
