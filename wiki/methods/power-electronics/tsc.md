---
title: "晶闸管投切电容方法 (TSC)"
type: method
tags: [tsc, thyristor-switched-capacitor, reactive-compensation, svc, switching, facts, overvoltage, inrush-current]
created: "2026-05-04"
updated: "2026-05-13"
---

# 晶闸管投切电容方法 (TSC)

## 定义

晶闸管投切电容（Thyristor Switched Capacitor, TSC）是一种基于晶闸管相控开关的无功补偿方法。它由固定电容器组与一对反并联晶闸管（或晶闸管-SCR阀组）串联构成，通过精确控制晶闸管的触发时刻，实现电容器组的无涌流或低涌流投切。与机械断路器投切相比，TSC 能够在毫秒级时间内完成无功功率的切换，且无触点磨损，适合频繁调节的场景。

TSC 通常作为 SVC（Static Var Compensator, 静止无功补偿器）的核心容性支路出现。在 SVC 系统中，TSC 提供分级容性无功，而 TCR（Thyristor Controlled Reactor, 晶闸管控制电抗器）提供连续感性无功，两者配合形成完整的无功调节能力。

TSC 在 EMT 仿真中的核心关注点是：投切瞬态（涌流、过电压）、晶闸管阀的触发同步、电容残压对重合闸的影响，以及投切动作与系统阻抗的交互谐振。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 420" xmlns="http://www.w3.org/2000/svg">
  <rect width="900" height="420" fill="#ffffff" rx="8"/>
  <text x="450" y="30" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" font-weight="bold" fill="#333">TSC 电磁暂态建模方法层级</text>
  <rect x="50" y="55" width="240" height="120" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="170" y="80" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#92400e">详细开关模型</text>
  <text x="170" y="100" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#666">Detailed Switch Model</text>
  <line x1="70" y1="110" x2="270" y2="110" stroke="#d97706" stroke-width="0.5"/>
  <text x="65" y="125" font-family="Arial,sans-serif" font-size="9" fill="#333">• 晶闸管阀级开关状态</text>
  <text x="65" y="140" font-family="Arial,sans-serif" font-size="9" fill="#333">• 电容涌流峰值/频率</text>
  <text x="65" y="155" font-family="Arial,sans-serif" font-size="9" fill="#333">• 谐波频谱 (500-2000Hz)</text>
  <text x="65" y="170" font-family="Arial,sans-serif" font-size="9" fill="#333">• 步长: 1-5 μs</text>
  <line x1="170" y1="175" x2="170" y2="200" stroke="#333" stroke-width="1.5"/>
  <rect x="340" y="55" width="240" height="120" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="460" y="80" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#166534">受控导纳模型</text>
  <text x="460" y="100" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#666">Controlled Admittance</text>
  <line x1="360" y1="110" x2="560" y2="110" stroke="#16a34a" stroke-width="0.5"/>
  <text x="355" y="125" font-family="Arial,sans-serif" font-size="9" fill="#333">• 等效电纳 B=ωC</text>
  <text x="355" y="140" font-family="Arial,sans-serif" font-size="9" fill="#333">• 投切状态 u(t)∈{0,1}</text>
  <text x="355" y="155" font-family="Arial,sans-serif" font-size="9" fill="#333">• SVC 端口动态响应</text>
  <text x="355" y="170" font-family="Arial,sans-serif" font-size="9" fill="#333">• 步长: 20-50 μs</text>
  <line x1="460" y1="175" x2="460" y2="200" stroke="#333" stroke-width="1.5"/>
  <rect x="630" y="55" width="240" height="120" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="750" y="80" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1e40af">动态相量模型</text>
  <text x="750" y="100" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#666">Dynamic Phasor (DP)</text>
  <line x1="650" y1="110" x2="850" y2="110" stroke="#2563eb" stroke-width="0.5"/>
  <text x="645" y="125" font-family="Arial,sans-serif" font-size="9" fill="#333">• 基波+低次谐波相量</text>
  <text x="645" y="140" font-family="Arial,sans-serif" font-size="9" fill="#333">• d-q 坐标系状态方程</text>
  <text x="645" y="155" font-family="Arial,sans-serif" font-size="9" fill="#333">• TSP-EMT 混合仿真</text>
  <text x="645" y="170" font-family="Arial,sans-serif" font-size="9" fill="#333">• 步长: 0.01-0.02 s</text>
  <rect x="50" y="230" width="820" height="100" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="460" y="255" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#5b21b6">应用场景映射</text>
  <line x1="70" y1="265" x2="850" y2="265" stroke="#7c3aed" stroke-width="0.5"/>
  <rect x="60" y="275" width="150" height="45" rx="4" fill="#f3e8ff" stroke="#7c3aed" stroke-width="1"/>
  <text x="135" y="292" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#5b21b6">投切涌流分析</text>
  <text x="135" y="307" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="#7c3aed">→ 详细开关模型</text>
  <rect x="230" y="275" width="150" height="45" rx="4" fill="#f3e8ff" stroke="#7c3aed" stroke-width="1"/>
  <text x="305" y="292" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#5b21b6">SVC 端口动态</text>
  <text x="305" y="307" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="#7c3aed">→ 受控导纳/DP</text>
  <rect x="400" y="275" width="150" height="45" rx="4" fill="#f3e8ff" stroke="#7c3aed" stroke-width="1"/>
  <text x="475" y="292" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#5b21b6">大电网混合仿真</text>
  <text x="475" y="307" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="#7c3aed">→ 动态相量模型</text>
  <rect x="570" y="275" width="150" height="45" rx="4" fill="#f3e8ff" stroke="#7c3aed" stroke-width="1"/>
  <text x="645" y="292" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#5b21b6">HIL 实时仿真</text>
  <text x="645" y="307" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="#7c3aed">→ 详细开关/等效</text>
  <rect x="740" y="275" width="130" height="45" rx="4" fill="#f3e8ff" stroke="#7c3aed" stroke-width="1"/>
  <text x="805" y="292" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#5b21b6">谐波放大研究</text>
  <text x="805" y="307" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="#7c3aed">→ 详细开关模型</text>
  <rect x="50" y="350" width="820" height="60" rx="6" fill="#f9fafb" stroke="#9ca3af" stroke-width="1"/>
  <text x="460" y="370" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#374151">核心公式</text>
  <text x="150" y="390" text-anchor="middle" font-family="Courier,monospace" font-size="10" fill="#4b5563">Q_C = ωCV²</text>
  <text x="300" y="390" text-anchor="middle" font-family="Courier,monospace" font-size="10" fill="#4b5563">f_inrush = 1/(2π√(L_lim·C))</text>
  <text x="500" y="390" text-anchor="middle" font-family="Courier,monospace" font-size="10" fill="#4b5563">I_peak = V_m·√(C/L_lim)</text>
  <text x="720" y="390" text-anchor="middle" font-family="Courier,monospace" font-size="10" fill="#4b5563">I_TSC(t) = jB_C·u(t)·V(t)</text>
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · TSC 电磁暂态建模方法层级与场景映射</p>

## EMT 中的角色

在电磁暂态（EMT）仿真中，TSC 方法主要用于：

- **投切暂态建模**：描述晶闸管导通瞬间电容器充电涌流、系统电压突变和暂态振荡过程。投切时刻的选择直接影响涌流幅值和过电压水平。
- **SVC 容性支路建模**：作为 SVC 装置的固定电容分组，TSC 提供阶梯式容性无功输出。在 EMT 中需要精确模拟每组 TSC 的投切时序和暂态响应。
- **电压支撑和无功调节**：在系统故障或负荷突变时，TSC 的快速投切可为母线提供瞬时无功支撑，抑制电压跌落。
- **谐波和过电压风险分析**：TSC 投切动作可能激发系统谐振频率，引发过电压和谐波放大，需要在 EMT 中验证最劣工况。
- **HIL（硬件在环）实时仿真**：TSC 模型需适配实时仿真步长约束，在 HYPERSIM、RTDS 等平台上验证控制保护逻辑。

## EMT 建模方法

TSC 的 EMT 建模至少存在三种层级，分别适用于不同的研究目标。

### 方法一：详细开关模型（Detailed Switch Model）

详细开关模型将 TSC 表示为物理器件级电路：固定电容器 $C$、串联电抗器（限流电抗器 $L_{lim}$）、反并联晶闸管阀、保护用压敏电阻（MOV）和并联旁路断路器。晶闸管用 EMTP 内置的开关模型（如 Pejovic 开关或 Diode 模型）实现，其导通电阻 $R_{on}$ 和关断电阻 $R_{off}$ 由仿真步长 $\Delta t$ 决定。

在 EMTP 类程序中，TSC 支路的伴随电路（companion circuit）由诺顿等效导纳和电流源组成：

$$
Y_{eq} = \frac{2C}{\Delta t}
$$

$$
I_{hist}(n) = I_{hist}(n-1) + \frac{2C}{\Delta t} v_C(n-1)
$$

其中 $v_C(n-1)$ 为上一步的电容电压，$I_{hist}$ 为历史电流源。当晶闸管关断时，支路等效为开路（$R_{off} \approx 10^6 \sim 10^{12} \Omega$）；导通时等效为 $R_{on} \approx 10^{-3} \sim 10^{-6} \Omega$ 的串联 RC 电路。

**特点**：保留阀级开关暂态，可验证涌流峰值、过电压和谐波频谱。仿真步长需 $\leq 5 \mu s$ 以捕捉开关事件。

**适用场景**：投切涌流分析、阀级应力验证、HIL 实时仿真中的精确开关建模、断路器重燃研究。

**局限**：计算量大，不适合大规模系统仿真。

### 方法二：受控导纳/等效电纳模型（Controlled Admittance Model）

受控导纳模型将 TSC 近似为一个随投切状态变化的等效导纳。当晶闸管导通时，TSC 支路的等效容纳为：

$$
B_C = \omega C
$$

当晶闸管关断时，支路导纳为零。投切状态由控制逻辑根据无功指令和母线电压决定。

在 EMT 中，该模型可表示为：

$$
I_{TSC}(t) = j B_C \cdot u(t) \cdot V(t)
$$

其中 $u(t) \in \{0, 1\}$ 为投切状态函数，由触发脉冲序列决定。该模型不保留开关暂态，只反映基波等效的无功注入。

**特点**：计算效率高，适合系统级 EMT 仿真。可嵌入动态相量（DP）或平均值模型（AVM）框架。

**适用场景**：SVC 整体端口动态响应、系统电压调节研究、大电网混合仿真（TSP-EMT 接口）。

**局限**：不验证涌流、谐波和阀级暂态。

### 方法三：动态相量模型（Dynamic Phasor Model）

动态相量模型将 TSC 的电压和电流表示为时变傅里叶系数的级数展开。对于 TSC 电容电压 $v_C(t)$，其 $k$ 次动态相量定义为：

$$
V_k(t) = \frac{1}{T} \int_{t-T/2}^{t+T/2} v_C(\tau) e^{-jk\omega_s \tau} d\tau
$$

其中 $T = 2\pi/\omega_s$ 为基波周期，$\omega_s$ 为额定角频率。TSC 的动态相量模型保留基波（$k=1$）和若干低次谐波（如 $k=3, 5$），忽略高阶谐波对精度的影响极小。

在 E Zhijun (2009) 的 SVC 动态相量模型中，TSC 的电容电压动态方程为：

$$
C \frac{dV_k(t)}{dt} + jk\omega_s C V_k(t) = I_{line, k}(t)
$$

其中 $I_{line, k}(t)$ 为线路电流的 $k$ 次动态相量。该方程在同步旋转参考系（d-q 坐标系）中可写为实数状态空间形式：

$$
\frac{d}{dt}\begin{bmatrix} V_{d}(t) \\ V_{q}(t) \end{bmatrix} = \begin{bmatrix} 0 & \omega_s \\ -\omega_s & 0 \end{bmatrix}\begin{bmatrix} V_{d}(t) \\ V_{q}(t) \end{bmatrix} + \frac{1}{C}\begin{bmatrix} I_{d}(t) \\ I_{q}(t) \end{bmatrix}
$$

**特点**：步长可从 EMTP 的 50 $\mu s$ 提升至 0.01–0.02 s，加速约 200–400 倍。保留基波和若干低次谐波，精度接近详细开关模型。

**适用场景**：大电网暂态稳定程序（TSP）中嵌入 SVC 电磁暂态等值、混合仿真（TSP-EMT 接口）、系统级动态研究。

**局限**：谐波截断阶数选择缺乏通用准则；不平衡故障下的误差边界尚未系统评估。

### 建模方法对比

| 方法 | 保留内容 | 适合问题 | 仿真步长 | 计算效率 |
|------|----------|----------|----------|----------|
| 详细开关模型 | 晶闸管状态、电容电压、涌流、谐波 | 投切暂态、阀级应力、HIL 验证 | 1–5 $\mu s$ | 低 |
| 受控导纳模型 | 等效电纳 $B_C$、投切状态 | SVC 端口动态、电压调节 | 20–50 $\mu s$ | 高 |
| 动态相量模型 | 基波和若干低次谐波相量 | 混合仿真、系统级动态 | 0.01–0.02 s | 极高 |

## 投切控制策略

TSC 的核心控制目标是选择最优投切时刻，以最小化涌流和过电压。

### 零电压投切（Zero-Voltage Switching, ZVS）

零电压投切是最经典的 TSC 控制策略。其基本原理是：在晶闸管两端电压接近零的时刻触发导通，使电容器充电涌流最小化。

设电容器初始电压为 $v_{C0}$，母线电压为 $v_s(t) = V_m \sin(\omega t + \theta)$。当晶闸管在时刻 $t_f$ 触发导通时，若满足：

$$
v_s(t_f) \approx v_{C0}
$$

则投切瞬间的电压差 $\Delta v = v_s(t_f) - v_{C0} \approx 0$，涌流理论上为零。

实际工程中，零电压投切窗口通常定义为 $|v_s(t) - v_{C0}| < \epsilon$，其中 $\epsilon$ 为允许误差（通常 5–10 V）。若电容残压与母线电压相位和幅值均接近，则可在下一个电压过零点附近触发。

### 最大涌流工况（Worst-Case Switching）

最恶劣投切工况为晶闸管在母线电压峰值时刻触发（此时 $\Delta v = V_m - v_{C0}$ 最大）。涌流峰值为：

$$
I_{peak} = V_m \sqrt{\frac{C}{L_{lim}}}
$$

其中 $L_{lim}$ 为限流电抗器电感。涌流频率为：

$$
f_{inrush} = \frac{1}{2\pi\sqrt{L_{lim}C}}
$$

典型涌流幅值为额定电流的 **100–200 倍**，频率在 **500–2000 Hz** 范围。限流电抗器的设计需在抑制涌流和避免与系统阻抗谐振之间折中。

### 触发同步

TSC 的触发脉冲必须与母线电压严格同步。同步信号通常来自：
- 母线电压过零检测（直接同步）
- PLL（锁相环）输出相位
- 外部同步信号（在 HIL 仿真中由 RT 模拟器提供）

触发角 $\alpha$ 的零点约定至关重要：

$$
\alpha = \omega(t_{fire} - t_{ref})
$$

其中 $t_{ref}$ 为电压过零时刻或特定相位参考点。不同系统中 $t_{ref}$ 的定义可能不同，必须明确标注。

## 形式化表达

### TSC 支路基本方程

TSC 支路的时域电路方程：

$$
L_{lim}\frac{di_{TSC}}{dt} + \frac{1}{C}\int i_{TSC} dt + R_{on} \cdot u_{thy}(t) \cdot i_{TSC} = u_{thy}(t) \cdot v_s(t)
$$

其中 $u_{thy}(t) \in \{0, 1\}$ 为晶闸管导通状态函数。

### 容性无功输出

TSC 导通时的容性无功功率：

$$
Q_C = \omega C V^2 = \frac{V^2}{X_C}
$$

其中 $V$ 为母线电压有效值，$X_C = 1/(\omega C)$ 为电容电抗。

### 投切涌流

投切瞬间的涌流频率和幅值：

$$
f_{inrush} = \frac{1}{2\pi\sqrt{L_{lim}C}}, \quad I_{peak} = V_m \sqrt{\frac{C}{L_{lim}}}
$$

### 动态相量状态方程

TSC 在同步旋转参考系中的状态方程：

$$
\frac{d}{dt}\begin{bmatrix} V_{d}(t) \\ V_{q}(t) \end{bmatrix} = \begin{bmatrix} 0 & \omega_s \\ -\omega_s & 0 \end{bmatrix}\begin{bmatrix} V_{d}(t) \\ V_{q}(t) \end{bmatrix} + \frac{1}{C}\begin{bmatrix} I_{d}(t) \\ I_{q}(t) \end{bmatrix}
$$

## 关键技术挑战

### 涌流和谐波

TSC 投切瞬间的涌流包含高频振荡分量（500–2000 Hz），可能激发系统谐振频率，引发过电压。限流电抗器 $L_{lim}$ 的设计需同时考虑：
1. 涌流抑制：$L_{lim}$ 越大，涌流越小
2. 谐振规避：$L_{lim}$ 与系统电容的谐振频率不应落在谐波频段（5/7/11 次）

### 残压与重合闸

TSC 关断后，电容器上可能残留电压。若残压与母线电压差异过大，再次投切时将产生较大涌流。在 SVC 系统中，TSC 分组投切策略需考虑残压衰减时间常数和下一次投切的最早时刻。

### 谐波放大

TSC 与系统阻抗的并联谐振可能放大特定次谐波。在 SVC 系统中，通常配置单调谐或双调谐滤波器（FC 分支）来吸收 TCR 产生的特征谐波（5、7、11、13 次）。TSC 投切动作可能改变滤波器-系统谐振点，需重新验证谐波水平。

### HIL 实时仿真的步长约束

在 HIL 实时仿真中，TSC 模型的仿真步长受到硬件刷新率限制。Le-Huy (2023) 在 Hydro-Québec La Verendrye 735 kV 变电站的混合 SVC-VSC 项目中，对比了小步长（3 $\mu s$）和常规大步长（32.5521 $\mu s$）两种 TSC 建模方法，发现当正确计入仿真寄生元件（stub line 和 Pejovic 开关等效参数）时，两种方法的波形重合度 > 99%。

## 量化性能边界

TSC 在 EMT 仿真中的性能已有可核验的量化结果，但以下数据均绑定具体的 SVC 拓扑、仿真条件和验证范围：

- **Le-Huy (2023)** 在 Hydro-Québec La Verendrye 735 kV 变电站混合 SVC-VSC 改造项目的 HIL 实时仿真中，TSC 支路容量为 95 Mvar/支路（共 2 组），VSC 支路容量为 70 Mvar/支路（共 2 组），总补偿容量 +330/-110 Mvar。对比了小步长 EMT（3 $\mu s$）与常规大步长 EMT（32.5521 $\mu s$，60 Hz 系统 512 点/周波）两种建模路径。波形重合度 > **99%**，动态响应偏差 < **0.5%**，稳态电压调节误差 < **0.2%**。该结论基于特定混合拓扑的 HIL 预投运测试，不适用于所有 TSC 或非 HIL 离线仿真场景 (Le-Huy 2023)。

- **E Zhijun (2009)** 在 IEEE 9 节点和 New England 39 节点系统中提出了 SVC 动态相量（DP）混合仿真方法。TSC 建模为单相 DP 模型，保留基波和 5 次谐波相量。积分步长从 EMTP 的 50 $\mu s$ 提升至 TSP 兼容的 0.01–0.02 s，加速约 **200–400 倍**。SVC DP 模型的电压/电流波形与 DCG/EMTP 全电磁暂态基准结果高度一致。该结论基于自研 DP 程序与 DCG/EMTP 的对比验证，非商业 DP 平台结果可能不同 (E Zhijun 2009)。

- **Dey (2021)** 在 IEEE 第一基准模型（SSR 脆弱系统，含 TCSC）中比较了离散时间模型、动态相量模型和频率扫描模型。对于晶闸管投切/控制类装置，频率扫描模型（黑盒方法，通过向量拟合提取状态空间模型）在次同步频段（5–60 Hz）的阻抗预测精度与离散时间解析模型相当，且提取过程不受建模细节程度限制。该结论针对 TCSC 的串联补偿场景，TSC 的并联投切场景需另行验证 (Dey 2021)。

这些量化数据不构成对 TSC 建模方法的全面性能评价，只说明在特定测试条件下可获得的能力边界。

## 适用边界与选择指南

### 建模方法选择指南

| 应用场景 | 推荐模型 | 理由 |
|----------|----------|------|
| 投切涌流和过电压分析 | 详细开关模型 | 需捕捉开关瞬态和阀级应力 |
| SVC 整体端口动态 | 受控导纳模型或动态相量模型 | 计算效率高，保留基波动态 |
| 大电网混合仿真（TSP-EMT） | 动态相量模型 | 步长匹配 TSP 需求，200–400 倍加速 |
| HIL 实时仿真验证 | 详细开关模型或小步长等效 | 需与硬件控制回路闭环交互 |
| 谐波放大研究 | 详细开关模型 | 需验证各次谐波电流频谱 |

### 运行边界

- **投切时刻约束**：零电压投切窗口通常为 $|v_s - v_C| < 5-10V$；非零电压投切涌流可达额定电流 100–200 倍。
- **最小投切间隔**：TSC 关断后需等待电容残压衰减至安全水平（通常 1–3 秒）方可再次投切，避免过电压和涌流。
- **电压范围**：TSC 的无功输出与母线电压平方成正比，低电压时输出急剧下降。在电压跌落至 0.5 p.u. 时，容性无功输出降至额定值的 25%。
- **温度限制**：晶闸管阀的结温限制了连续导通时间和最大通态电流，需配置冷却系统和温度保护。

### 不适用场景

- **不适用于需要连续无功调节的场景**：TSC 提供分级（离散）容性无功，不能像 TCR 或 STATCOM 那样连续调节。若需平滑无功控制，应选用 TCR 或 VSC/STATCOM。
- **不适用于需要快速连续响应的场景**：TSC 的投切间隔受电容残压衰减限制，响应时间通常在秒级，远慢于 STATCOM 的毫秒级响应。
- **不适用于需要容性无功快速跟踪的场景**：在故障穿越（FRT）等快速电压支撑场景中，TSC 的响应速度不足以提供有效支撑。

## 与相关方法/模型的关系

- [[svc-tcr-model]]：TCR 是 SVC 的感性支路，与 TSC 配合形成完整 SVC。TCR 连续调节感性无功，TSC 分级调节容性无功。
- [[thyristor-control]]：TSC 的触发控制遵循晶闸管控制的通用边界（同步、导通角、自然关断）。
- [[reactive-compensation-device]]：TSC 是无功补偿装置族中的容性分支。
- [[average-value-model]]：TSC 的受控导纳模型属于平均值建模范畴。
- [[dynamic-phasor]]：TSC 的动态相量模型适用于混合仿真。
- [[detailed-switch-model]]：TSC 的详细开关模型需使用器件级开关表示。
- [[overvoltage]]：TSC 投切过电压是 EMT 仿真的核心关注点之一。
- [[inrush-current]]：TSC 投切涌流分析需专门的开关暂态验证。
- [[svc-model]]：SVC 整机模型中，TSC 是容性分组的核心单元。

## 来源论文

- **Le-Huy (2023)** *"Hybrid SVC-VSC modeling approaches for hardware-in-the-loop simulation"* — 在 Hydro-Québec La Verendrye 735 kV 变电站混合 SVC-VSC 改造项目中，详细描述了 TSC（95 Mvar/支路）在 HIL 实时仿真中的两种建模方法（小步长 3 $\mu s$ vs 常规大步长 32.5521 $\mu s$），验证了波形重合度 > 99%。原文提供了 TSC 在 EMT 仿真中的 Pejovic 开关参数设定、stub line 寄生等效和仿真步长约束的完整工程经验。
- **E Zhijun (2009)** *"Hybrid simulation of power systems with SVC dynamic phasor model"* — 提出了 SVC（含 TSC 和 TCR）的单相动态相量模型，保留基波和 5 次谐波。积分步长从 50 $\mu s$ 提升至 0.01–0.02 s，加速约 200–400 倍。验证了 IEEE 9 节点和 New England 39 节点系统中的动态响应精度。
- **Dey (2021)** *"Comparison of dynamic phasor, discrete-time and frequency scanning based SSR models of a TCSC"* — 比较了晶闸管控制/投切类装置（TCSC/TSC/SVC）的三种建模方法（离散时间、动态相量、频率扫描）。频率扫描黑盒方法在次同步频段的阻抗预测精度与解析模型相当，为 TSC 的频域建模提供了参考。
