---
title: "序分量法 (Sequence Component Method)"
type: method
tags: [sequence-component, symmetrical-component, unbalanced, fault-analysis, power-system]
created: "2026-05-02"
updated: "2026-05-16"
---

# 序分量法 (Sequence Component Method)

## 定义与边界

序分量法是把三相交流量分解为零序、正序和负序分量，并利用这些分量分析不平衡运行或不对称故障的方法流程。它以 [[symmetrical-components]] 的 Fortescue 变换为数学基础，以 [[sequence-network-model]] 的序网为常见计算载体。

本页关注"如何使用序分量"而不是重复所有序网故障公式。它不等同于完整 EMT 相域仿真：当电力电子限流、频率相关线路、互感器暂态、非线性电弧或保护闭环显著时，序分量通常用于解释、初始化或后处理，不能替代瞬时波形求解。

## EMT 中的作用

在 EMT 知识体系中，序分量法有三类作用：

- 为不平衡故障提供正序、负序和零序的物理解释。
- 为保护量、故障类型识别和相量后处理提供可审计指标。
- 为 EMT 工况设置、故障前状态和结果解释提供与传统短路计算一致的桥梁。

若直接从 EMT 波形提取序分量，需要先定义采样窗口、基波估计、滤波方式和相角参考。瞬时采样值直接代入相量矩阵，只能得到某种代数分量，不自动等同于工频序相量。

## 核心公式

### Fortescue 变换（对称分量变换）

对基频相量 $\mathbf{X}_{abc}=[X_a,X_b,X_c]^T$，

$$

\begin{bmatrix} X_0 \\ X_1 \\ X_2 \end{bmatrix}
=\frac{1}{3}
\begin{bmatrix}
1 & 1 & 1 \\
1 & a & a^2 \\
1 & a^2 & a
\end{bmatrix}
\begin{bmatrix} X_a \\ X_b \\ X_c \end{bmatrix},
\qquad a=e^{j120^\circ}.

$$

反变换为

$$

\begin{bmatrix} X_a \\ X_b \\ X_c \end{bmatrix}
=
\begin{bmatrix}
1 & 1 & 1 \\
1 & a^2 & a \\
1 & a & a^2
\end{bmatrix}
\begin{bmatrix} X_0 \\ X_1 \\ X_2 \end{bmatrix}.

$$

正序表示正常相序的平衡三相分量，负序表示反相序的平衡三相分量，零序表示三相同相分量。零序电流是否存在取决于接地、中性线、变压器连接和三角形环流通道。

### 序阻抗与网络假设

在线性、基频、近似对称的网络中，可分别建立 $Z_1$、$Z_2$ 和 $Z_0$。常见判断是：

- 静止、对称的线路和变压器可近似有 $Z_1$ 与 $Z_2$ 相同。
- 旋转电机的负序阻抗与转子频率和阻尼有关，不能简单等于正序同步电抗。
- 零序阻抗高度依赖接地方式、回流路径、变压器接线组和线路几何。

这些是建模原则，不是无条件参数表。若页面给出具体数值范围、倍数或标准限值，必须绑定设备、规程或来源。

## EMT 建模方法

### 方法1：序网等效故障回路法

基于 Rosołowski 等 (1997) 的研究，序分量法在 EMT 中的核心应用是**距离保护阻抗测量**。其数学本质是将故障回路方程写成复数微分方程形式，然后在时域直接求解正序阻抗参数。

**等效故障回路电路方程**：

$$

v_0(t) = v_0(t) - R_0 i_0(t) - L_0 \frac{di_0(t)}{dt} - R_{0m} i_{0B}(t) \tag{1a}

$$

$$

v_1(t) = v_1(t) - R_1 i_1(t) - L_1 \frac{di_1(t)}{dt} - R_{1m} i_{1B}(t) \tag{1b}

$$

$$

v_2(t) = v_2(t) - R_2 i_2(t) - L_2 \frac{di_2(t)}{dt} - R_{2m} i_{2B}(t) \tag{1c}

$$

其中 $v_0(t), v_1(t), v_2(t)$ 和 $i_0(t), i_1(t), i_2(t)$ 分别是零、正、负序电压和电流，$R_{0m}, R_{1m}, R_{2m}$ 和 $L_{0m}, L_{1m}, L_{2m}$ 是互阻抗和互感参数，$i_{0B}(t), i_{1B}(t), i_{2B}(t)$ 是相邻平行线路的序电流。

**故障回路正序参数估计**：

定义正序阻抗分量：

$$

R_1 = R'_1 \cdot l, \quad L_1 = L'_1 \cdot l \tag{2}

$$

其中 $R'_1$ 和 $L'_1$ 是线路单位长度正序电阻和电感，$l$ 是故障距离。

**时域微分方程求解**（Rosołowski 1997 提出）：

将复数方程 (1) 写成实部-虚部形式，在单个采样时刻即可求解 $R_1$ 和 $L_1$：

$$

S[v_{ex}(k)] = S[i_{eRx}(k)]R_1 + L_1 D[i_{eLy}(k)] \tag{3}

$$

其中 $S[\cdot]$ 和 $D[\cdot]$ 分别是信号的平均算子和微分算子。

**电阻和电感计算公式**：

$$

R_1 = \frac{S[v_{\phi x}(k)]D[i_{\phi Ly}(k)] - S[v_{\phi y}(k)]D[i_{\phi Lx}(k)]}{S[i_{\phi Rx}(k)]D[i_{\phi Ly}(k)] - S[i_{\phi Ry}(k)]D[i_{\phi Lx}(k)]} \tag{4}

$$

$$

L_1 = \frac{S[v_{\phi y}(k)]S[i_{\phi Rx}(k)] - S[v_{\phi x}(k)]S[i_{\phi Ry}(k)]}{S[i_{\phi Rx}(k)]D[i_{\phi Ly}(k)] - S[i_{\phi Ry}(k)]D[i_{\phi Lx}(k)]} \tag{5}

$$

**算法优势**：在半个工频周期内（约 10 ms @ 50 Hz）即可获得可接受的阻抗估计结果，且对各种类型的波形畸变具有免疫性。

### 方法2：傅里叶短窗相量提取

使用半个周期傅里叶正交滤波器估计序分量，适用于保护继电器的快速相量计算。

**正交分量提取**：

设信号 $x(k)$ 的复数形式为 $x(k) = x_x(k) + jx_y(k)$，则：

$$

S[x(k)] = \frac{x(k) + x(k-1)}{2}, \quad D[x(k)] = \frac{x(k) - x(k-1)}{T_s} \tag{6}

$$

其中 $T_s$ 是采样周期。

### 方法3：序阻抗辨识的多 Fault Type 边界条件

根据故障类型，序网按边界条件连接。表 1 给出各类故障的等效故障回路参数。

| 故障类型 | 序条件 | $v_\phi$ | $i_{1\phi}$ | $i_{0R}$ | $i_{0L}$ |
|---------|--------|---------|------------|----------|----------|
| 三相 | $I_{2f}=0$ | $v_1 - v_2$ | $i_1 - i_2$ | $i_1$ | $i_1$ |
| b-c | $-v_{1f}=v_{2f}$ | $v_1 - v_2$ | $i_1 - i_2$ | $i_1 - i_2$ | $i_1 - i_2$ |
| a-b | $a^2 v_{1f} = a v_{2f}$ | $v_1 - a^2 v_2$ | $i_1 - a^2 i_2$ | $i_1 - a i_2$ | $i_1 - a i_2$ |
| a-c | $a v_{1f} = a^2 v_{2f}$ | $v_1 - a v_2$ | $i_1 - a i_2$ | $i_1 - a^2 i_2$ | $i_1 - a^2 i_2$ |
| b-c-g | $I_{1f}=I_{2f}=I_{0f}$ | 同 b-c | 同 b-c | $-m_R i_{0B} - m_{Rm} i_{0B}$ | $-m_L i_{0B} - m_{Lm} i_{0B}$ |
| a-g | $v_{0f}+v_{1f}+v_{2f}=0$ | $v_0+v_1+v_2$ | $-i_1+i_2$ | $m_R i_{0B} + m_{Rm} i_{0B}$ | $m_L i_{0B} + m_{Lm} i_{0B}$ |

其中 $a = e^{j120^\circ} = -\frac{1}{2}+j\frac{\sqrt{3}}{2}$，$a^2 = e^{j240^\circ} = -\frac{1}{2}-j\frac{\sqrt{3}}{2}$。

### 方法4：dq-序动态相量法

针对电力电子系统的非对称工况，定义 dq-序动态相量 (dq-sequence dynamic phasors)：

1. 先做瞬时对称分量分解，得到正序、负序和零序分量；
2. 对正序和负序分别在其相应旋转方向下做 Park 变换；
3. 在 dq-序坐标系中取动态傅里叶系数；
4. 推导乘法性质和状态矩阵构造步骤。

该方法解决了传统三相动态相量或序动态相量维度较高、难以直接处理电力电子方程中变量乘积的问题。

## 量化性能边界

### 阻抗估计精度

Rosołowski 等 (1997) 在 EMTP 仿真中验证了算法性能：

- **响应时间**：约半个工频周期（10 ms @ 50 Hz）即可获得可接受的阻抗估计结果
- **采样率**：$f_s = 1$ kHz（每周期 20 个采样点）
- **抗混叠滤波**：模拟低通滤波器，截止频率 $f_0 = 3$ 倍基频
- **适用故障电阻**：最高可达 50 Ω 的高阻故障仍可检测

### 平行线路保护性能

对于平行输电线路，改进算法可在：

- **故障检测时间**：约 7 ms（远端故障）至 2 ms（近端故障）
- **故障选相**：通过比较两条平行线路的电压降幅值 $|\Delta v_A|$ 和 $|\Delta v_B|$ 区分故障线路
- **高阻故障检测**：可检测电阻高达 50 Ω 的接地故障（此时传统阻抗判据失效）

### 序阻抗参数典型值

| 参数 | 典型值 | 说明 |
|------|--------|------|
| $Z_1$（正序阻抗） | $1.3+j15.0$ Ω/km（400 kV 线路） | 单位长度正序阻抗 |
| $Z_0$（零序阻抗） | $2.3+j26.6$ Ω/km（400 kV 线路） | 含大地返回路径 |
| $R_0/R_1$ | $1.5\sim3.0$ | 零序与正序电阻比 |
| $X_0/X_1$ | $1.6\sim2.0$ | 零序与正序电抗比 |

## 典型用途

| 用途 | 序分量角色 | EMT 边界 |
|------|-----------|----------|
| 单相接地故障解释 | 三序分量共同出现，零序通路决定电流 | 动态电弧和接地网频变需相域或专门模型 |
| 两相短路解释 | 正序和负序为主，理想情况下零序为零 | 互感和保护测量链会影响波形 |
| 两相接地故障解释 | 三序网络按边界条件耦合 | 故障阻抗和接地方式必须明确 |
| 保护量 | 负序、零序用于不平衡检测 | 数据窗、滤波、互感器暂态会改变测量 |
| EMT 后处理 | 从波形提取基波正/负/零序 | 需要说明频率跟踪和窗口 |

## 与相域 EMT 的关系

序分量法把不平衡量投影到对称基底，适合解释工频不平衡和保护相量。[[phase-domain-modeling]] 则直接保留 abc 相间耦合、开关和非线性。两者不是互斥关系：常见流程是用序网得到故障前或工频参考，再在 EMT 中用相域故障注入验证暂态波形和控制响应。

序分量法与相域 EMT 的具体接口过程：

1. **初始化阶段**：用序分量法计算故障前电网的稳态电压分布，作为 EMT 仿真的初始条件
2. **故障注入阶段**：在相域注入故障阻抗，同时在序域计算各序电流电压的边界条件
3. **后处理阶段**：从 EMT 输出的瞬时波形中提取基频序分量，与传统短路计算结果对比验证

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 800 380" xmlns="http://www.w3.org/2000/svg">
  <!-- 序分量法工作流程图 -->
  <!-- 输入层：故障三相电压电流 -->
  <rect x="20" y="20" width="120" height="60" fill="#dbeafe" stroke="#2563eb" stroke-width="2" rx="4"/>
  <text x="80" y="45" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#1e40af">三相电压电流</text>
  <text x="80" y="62" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="#1e40af">$v_{abc}, i_{abc}$</text>
  <!-- 箭头1 -->
  <line x1="140" y1="50" x2="180" y2="50" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <!-- Fortescue变换 -->
  <rect x="185" y="20" width="120" height="60" fill="#dcfce7" stroke="#16a34a" stroke-width="2" rx="4"/>
  <text x="245" y="42" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#166534">Fortescue变换</text>
  <text x="245" y="59" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="#166534">序分量提取</text>
  <!-- 箭头2 -->
  <line x1="305" y1="50" x2="345" y2="50" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <!-- 序网解耦 -->
  <rect x="350" y="20" width="120" height="60" fill="#dcfce7" stroke="#16a34a" stroke-width="2" rx="4"/>
  <text x="410" y="42" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#166534">序网边界条件</text>
  <text x="410" y="59" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="#166534">故障回路建立</text>
  <!-- 箭头3 -->
  <line x1="470" y1="50" x2="510" y2="50" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <!-- 微分方程求解 -->
  <rect x="515" y="20" width="120" height="60" fill="#fef3c7" stroke="#d97706" stroke-width="2" rx="4"/>
  <text x="575" y="42" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#92400e">时域阻抗估计</text>
  <text x="575" y="59" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="#92400e">复数微分方程</text>
  <!-- 箭头4 -->
  <line x1="635" y1="50" x2="675" y2="50" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <!-- 输出 -->
  <rect x="680" y="20" width="100" height="60" fill="#ede9fe" stroke="#7c3aed" stroke-width="2" rx="4"/>
  <text x="730" y="42" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#6d28d9">正序阻抗</text>
  <text x="730" y="59" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="#6d28d9">$R_1, L_1, l$</text>
  <!-- 平行线路判断分支 -->
  <rect x="185" y="130" width="120" height="60" fill="#dcfce7" stroke="#16a34a" stroke-width="2" rx="4"/>
  <text x="245" y="155" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#166534">平行线路判断</text>
  <text x="245" y="172" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="#166534">电压降比较</text>
  <!-- 故障线路选择 -->
  <rect x="350" y="130" width="120" height="60" fill="#fef3c7" stroke="#d97706" stroke-width="2" rx="4"/>
  <text x="410" y="155" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#92400e">故障线路选择</text>
  <text x="410" y="172" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="#92400e">$|\Delta v_A|$ vs $|\Delta v_B|$</text>
  <!-- 连接线 -->
  <line x1="305" y1="80" x2="305" y2="130" stroke="#333" stroke-width="1" stroke-dasharray="4"/>
  <line x1="305" y1="80" x2="245" y2="80" stroke="#333" stroke-width="1" stroke-dasharray="4"/>
  <line x1="470" y1="160" x2="510" y2="50" stroke="#333" stroke-width="1" stroke-dasharray="4"/>
  <!-- 测试系统 -->
  <rect x="20" y="250" width="760" height="110" fill="#f8fafc" stroke="#94a3b8" stroke-width="1" rx="4"/>
  <text x="400" y="270" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="#475569">IEEE 400 kV 同塔双回线路仿真系统（Rosołowski 1997）</text>
  <line x1="40" y1="280" x2="760" y2="280" stroke="#cbd5e1" stroke-width="1"/>
  <!-- 线路参数表 -->
  <text x="60" y="298" font-family="Arial,sans-serif" font-size="10" fill="#334155">线路 I: $Z_0=2.337+j26.6\Omega, Z_1=1.312+j15.0\Omega, L_0'=2.115mH/km, L_1'=0.830mH/km$</text>
  <text x="60" y="316" font-family="Arial,sans-serif" font-size="10" fill="#334155">线路 II: $Z_0=2.635+j38.0\Omega, Z_1=1.960+j24.5\Omega, L_0'=2.115mH/km$</text>
  <text x="60" y="334" font-family="Arial,sans-serif" font-size="10" fill="#334155">线路 III: $Z_0=2.835+j34.6\Omega, Z_1=1.632+j20.2\Omega, L_0'=1.145mH/km$</text>
  <text x="60" y="352" font-family="Arial,sans-serif" font-size="10" fill="#334155">$U=400kV, f=50Hz, f_s=1kHz$, 故障类型: a-b-g, 故障电阻: 0-50Ω, 检测时间: 2-7ms</text>
  <!-- 图例 -->
  <rect x="20" y="100" width="12" height="12" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="38" y="110" font-family="Arial,sans-serif" font-size="10" fill="#334155">输入</text>
  <rect x="80" y="100" width="12" height="12" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="98" y="110" font-family="Arial,sans-serif" font-size="10" fill="#334155">处理/模型</text>
  <rect x="160" y="100" width="12" height="12" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="178" y="110" font-family="Arial,sans-serif" font-size="10" fill="#334155">算法</text>
  <rect x="220" y="100" width="12" height="12" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="238" y="110" font-family="Arial,sans-serif" font-size="10" fill="#334155">输出</text>
  <!-- 箭头标记 -->
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 序分量法阻抗估计工作流程及IEEE 400kV双回线路仿真系统参数</p>

## 适用边界与失败模式

- 把基频相量序分量用于宽频暂态、谐波和直流偏置，而不说明滤波或窗口。
- 把单个设备的零序阻抗范围写成通用规律。
- 在电力电子主导系统中忽略控制限流和 PLL 动态，只用传统电源内阻解释故障电流。
- 在三相不对称线路或平行线路中忽略相间互耦对序网络解耦的破坏。
- 用序分量保护量替代保护闭环模型，漏掉互感器、采样、滤波、逻辑和断路器反馈。
- 把序分量法写成比相域法"更准确"或"更简单"的绝对结论；它只是不同假设下的表示方式。

## 代表性证据

[[fault-analysis]] 已把序分量法限定为经典交流不平衡故障解释和相量短路计算的重要工具，同时说明 EMT 故障注入需要相域模型、故障阻抗和保护闭环。[[complex-differential-equation-solving]] 说明复数变量适合相位、包络和序分量表达，但不应替代强非线性和开关细节的 EMT 验证。

## 与相关页面的关系

- [[symmetrical-components]]：序分量的数学定义和变换性质。
- [[sequence-network-model]]：把序阻抗和故障边界组织成网络。
- [[fault-analysis]]：故障分析的更宽方法入口。
- [[unbalanced-fault-analysis]]：不平衡故障类型和工程问题背景。
- [[phase-domain-modeling]]：强不平衡、非线性和开关暂态的相域路线。
- [[protection-control-device]]：保护测量量进入控制和动作逻辑的设备边界。

## 修订与证据使用注意事项

后续扩展应把序分量计算结果绑定到相量提取方式、频率、设备参数和故障条件。不要新增未来源化的电压不平衡限值、热容量公式常数或保护整定数值。

## 来源论文

- Rosołowski 等 1997 - 基于对称分量的复数微分方程距离保护算法 (Electric Power Systems Research 40: 175-180)