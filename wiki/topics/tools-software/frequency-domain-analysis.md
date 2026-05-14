---
title: "频域分析 (Frequency-Domain Analysis)"
type: topic
tags: [frequency-domain, analysis, harmonic, impedance, spectrum, fft, bode, vector-fitting, fdne, laplace, stability]
created: "2026-05-02"
updated: "2026-05-14"
---

# 频域分析 (Frequency-Domain Analysis)

## 定义

频域分析将电压、电流、阻抗、导纳、传递函数或时域波形表示为频率的函数，通过 Fourier 变换、Laplace 变换或有理函数逼近等手段，在频率域中研究电力系统的动态特性。其核心思想是：**任何线性时不变（LTI）系统的输入-输出关系都可以表示为频率响应的叠加**。

在 EMT 仿真中，频域分析不是时域仿真的替代品，而是互补的诊断和建模工具。它用于：

- 构造频率相关元件模型（线路、电缆、变压器）
- 提取黑盒模型阻抗，用于小信号稳定性分析
- 识别系统谐振频率、谐波传播路径和振荡模态
- 将频域响应转换为可在时域求解的有理函数等值（FDNE）

频域分析的数学基础是复频域变换：

$$
H(s) = \int_0^{\infty} h(t)e^{-st}dt, \quad s = \sigma + j\omega
$$

其中 $H(s)$ 是系统传递函数，$h(t)$ 是脉冲响应。当 $s = j\omega$ 时，得到频率响应 $H(j\omega)$。

## EMT 中的作用

频域分析在 EMT 仿真中承担四个核心角色：

1. **频率相关建模**：对线路、电缆、变压器和外部网络建立 [[frequency-dependent-modeling]] 或 [[fdne-model]]，通过频域测量或解析计算获得复阻抗/导纳的频率依赖特性。
2. **谐波与频谱诊断**：从 EMT 波形中提取频谱、谐波和振荡模态，支撑 [[harmonic-analysis]] 与控制交互诊断。
3. **小信号稳定性筛查**：对逆变器、HVDC、FACTS 或弱网系统进行阻抗扫描，识别不稳定运行点，再选择关键工况做时域 EMT 验证。
4. **频域到时域转换**：用 [[vector-fitting]] 将离散频率响应变成极点-留数有理函数模型，便于时域递推卷积或状态空间实现。

## 核心方法体系

频域分析在 EMT 领域包含五大核心方法族，按"测量→辨识→逼近→验证"流程组织。

### 1. 频率扫描 (Frequency Scanning)

频率扫描是频域分析的基础方法，通过在指定频点注入小扰动并测量响应，得到阻抗、导纳或多端口传递函数。

**工作原理**：在稳态运行点上叠加一个正弦扰动 $v(t) = V_0 + \Delta V \sin(2\pi f t)$，等待瞬态衰减后，从 FFT 提取基频响应：

$$
Z_{abc}(f) = \frac{V_{abc}(f)}{I_{abc}(f)}
$$

对于多端口系统，阻抗矩阵 $Z(s)$ 是 $n \times n$ 矩阵，每个元素 $Z_{ij}(f)$ 表示端口 $j$ 的电流注入在端口 $i$ 产生的电压响应。

**扰动注入方式**：
- **电流注入法**：在目标频点注入小电流扰动，适用于大多数电力电子系统。扰动幅值需足够小以保证线性化近似有效，但又需足够大以克服数值噪声。
- **电压注入法**：注入小电压扰动，适用于高阻抗系统（如 HVDC 线路）。

**dq 域扫描**：对于 GFL/GFM 逆变器系统，频率扫描通常在 dq 坐标系中进行，得到 $2 \times 2$ 阻抗矩阵：

$$
\mathbf{Z}_{dq}(f) = \begin{bmatrix} Z_{dd}(f) & Z_{dq}(f) \\ Z_{qd}(f) & Z_{qq}(f) \end{bmatrix}
$$

其中对角线元素 $Z_{dd}$、$Z_{qq}$ 表示同轴阻抗，非对角线元素 $Z_{dq}$、$Z_{qd}$ 表示交叉耦合阻抗。在弱耦合系统中，非对角线元素可忽略；但在强耦合系统（如多端 HVDC）中，交叉耦合项不可忽略。

**频率耦合问题**：电力电子系统的非线性导致频率耦合效应——注入频率 $f$ 的扰动可能在输出中产生 $f \pm kf_s$（$k$ 为整数，$f_s$ 为开关频率）的频率分量。此时需采用动态相量法或谐波状态空间法进行更精确的扫描。

**量化结果**：Cifuentes Garcia & Beerten 2026 在 VSC-HVDC 系统上验证了 EMT 频率扫描方法，在 400 个频点上扫描 dq 阻抗矩阵，仿真步长 10 μs 时相对误差低于 2%（< 1 kHz），在谐振点附近最大误差约 16%。

### 2. 向量拟合 (Vector Fitting)

向量拟合是频域响应有理函数逼近的工业标准方法，由 B. Gustavsen 和 J. Semlyen 于 1999 年提出。它将离散频率响应数据拟合为极点-留数形式的有理函数：

$$
H(s) \approx \hat{H}(s) = d(s) + \sum_{k=1}^{N} \frac{c_k}{s - p_k}
$$

其中 $p_k$ 是极点，$c_k$ 是对应留数，$d(s)$ 是多项式项。

**算法流程**：
1. **初始极点选择**：用线性搜索或经验规则初始化极点 $p_k^{(0)}$
2. **线性最小二乘拟合**：固定极点，求解最优留数 $c_k$
3. **极点迁移**：用非线性最小二乘更新极点位置
4. **迭代收敛**：重复步骤 2-3 直到误差低于阈值

**变体方法**：
- **标准 VF**：直接拟合原始频率响应
- **频率分区 VF**：将频带划分为多个子带，每个子带独立拟合，适用于宽频带响应
- **极点平移 VF**：通过频域平移改善病态条件下的数值稳定性

**无源性约束**：拟合得到的有理函数可能违反无源性（passivity），导致时域仿真中产生非物理能量。Ahmadi 等 2021 提出了一种基于网络综合的被动模型构建方法，通过构造正实函数（positive-real function）保证多端口 FDNE 模型的无源性：

$$
\text{Re}[\mathbf{Z}(j\omega)] \succeq 0, \quad \forall \omega
$$

即阻抗矩阵的实部为半正定矩阵。

**量化性能**：Kida 等 2024 比较了 VF 与 Rational Krylov Fitting (RKF) 在 FDNE 拟合中的性能。RKF 在 CTWB 线模型中用 20 个极点/元素达到 RMS 误差 $2.49 \times 10^{-4}$，而 VF 需要 21-25 个极点/元素才能达到类似精度。Bode 拟合方法则产生显著更多的零极点。

### 3. Laplace 逆变换 (Laplace Inversion)

Laplace 逆变换是频域到时域转换的另一种途径，通过数值反演 Laplace 变换积分获得时域响应：

$$
f(t) = \frac{1}{2\pi j} \int_{c-j\infty}^{c+j\infty} F(s)e^{st}ds
$$

**Windowed Numerical Laplace Transform (WNLT)**：传统方法将积分截断为有限区间，通过选择数据窗口 $\sigma_k$ 控制截断误差。典型精度为 $10^{-5}$ 到 $10^{-6}$。

**Theta 算法**：Castañón 等 2021 提出使用 Brezinski 的 theta 算法替代 WNLT 的截断策略。Theta 算法通过 Shanks 变换的外推加速级数收敛，不依赖数据窗口截断，可保证 $10^{-9}$ 量级的一致性精度：

$$
\theta_{m+1}^{(j)} = \theta_m^{(j)} + e_m \cdot f_{n+m}
$$

其中 $\theta$ 是 Shanks 变换的递推序列，$e_m$ 是外推系数。

**性能对比**：在四回线系统测试中，WNLT 精度为 $10^{-5}$（0.04 ms），Theta 算法精度为 $10^{-9}$（0.17 ms），Epsilon 算法精度为 $10^{-9}$（0.32 ms）。Theta 算法在保持与 Epsilon 算法相同精度的同时计算速度更快。

### 4. 谐波与频谱分析 (Harmonic & Spectral Analysis)

从 EMT 仿真波形中提取频率成分的核心工具是 [[fft]] 和 [[discrete-fourier-transform]]。

**FFT 方法**：对采样波形 $x[n]$ 应用快速 Fourier 变换：

$$
X[k] = \sum_{n=0}^{N-1} x[n] e^{-j2\pi kn/N}, \quad k = 0, 1, \ldots, N-1
$$

**关键工程问题**：
- **采样率**：根据 Nyquist 定理，采样频率 $f_s > 2f_{max}$，其中 $f_{max}$ 是关注的最高频率。EMT 仿真中通常需捕捉 kHz 级谐波，故采样率至少为 100 kHz。
- **窗函数**：非整周期采样导致频谱泄漏，需使用 Hann、Hamming 或 Blackman 窗函数减少泄漏效应。
- **频率分辨率**：$\Delta f = f_s / N$，增加采样点数 $N$ 可提高频率分辨率，但增加计算量。
- **非平稳信号**：EMT 暂态过程是非平稳的，需使用短时傅里叶变换（STFT）或小波变换进行时频联合分析。

**Prony 分析**：[[prony-analysis]] 从时域衰减振荡波形中直接估计频率、阻尼和幅值，适合扰动后波形诊断。其模型为：

$$
x(t) = \sum_{k=1}^{P} a_k e^{s_k t}
$$

其中 $s_k = \sigma_k + j\omega_k$ 是模态复频率，$a_k$ 是复振幅。Prony 分析对噪声和窗口选择敏感，在低信噪比条件下可能产生虚假模态。

### 5. 频域网络等值 (Frequency-Dependent Network Equivalents)

大规模电力系统 EMT 仿真中，为减少计算量，常将远端网络等值为频域阻抗模型（FDNE）。

**基本原理**：将网络在端口处的频率响应 $Z_{port}(j\omega)$ 通过 [[vector-fitting]] 拟合为有理函数，然后在时域中通过递推卷积实现：

$$
i(t) = \int_0^t h(t-\tau)v(\tau)d\tau \approx \sum_{k=0}^{n_t} v(t-k\Delta t) \cdot h(k\Delta t)
$$

**多端口 FDNE**：Saldaña & Calzolari 2022 提出了高效的多端口 FDNE 实现方法，通过压缩存储和并行求解显著减少内存和计算开销。关键优化包括：
- **频带压缩**：仅在谐振频率附近加密采样点
- **矩阵压缩**：利用稀疏性减少 FDNE 矩阵存储
- **并行递推**：多端口卷积计算并行化

**量化性能**：Multi-Port FDNE 方法可将 1000+ 节点网络压缩为 10-20 个端口的频域等值模型，在保持 IEEE 39 节点系统暂态响应精度的同时减少 80% 以上的仿真时间。

## 形式化表达

### 核心公式汇总

**阻抗/导纳定义**：
$$
Z(j\omega) = \frac{V(j\omega)}{I(j\omega)}, \quad Y(j\omega) = \frac{I(j\omega)}{V(j\omega)} = Z^{-1}(j\omega)
$$

**多端口阻抗矩阵**：
$$
\begin{bmatrix} V_1 \\ V_2 \\ \vdots \\ V_n \end{bmatrix} = \begin{bmatrix} Z_{11} & Z_{12} & \cdots & Z_{1n} \\ Z_{21} & Z_{22} & \cdots & Z_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ Z_{n1} & Z_{n2} & \cdots & Z_{nn} \end{bmatrix} \begin{bmatrix} I_1 \\ I_2 \\ \vdots \\ I_n \end{bmatrix}
$$

**dq 域阻抗矩阵（逆变器系统）**：
$$
\mathbf{Z}_{dq}(s) = \begin{bmatrix} Z_{dd}(s) & Z_{dq}(s) \\ Z_{qd}(s) & Z_{qq}(s) \end{bmatrix}
$$

**稳定性判据（Nyquist）**：系统稳定的充分条件是 $1 + Z_{source}(s)Y_{load}(s)$ 的 Nyquist 图不包围 $(-1, j0)$ 点。等价地，最大奇异值满足：

$$
\overline{\sigma}(Z_{source}(j\omega)Y_{load}(j\omega)) < 1, \quad \forall \omega
$$

**向量拟合有理函数**：
$$
\hat{H}(s) = d_0 + d_1 s + \sum_{k=1}^{N} \frac{c_k}{s - p_k}
$$

**Laplace 逆变换（Theta 算法）**：
$$
f(t) \approx \frac{2e^{ct}}{e^{2c\delta t} - 1} \cdot c \cdot \Re\left[\theta_0^{(2j+2)}\right]
$$

**模态传播函数（频变线路模型）**：
$$
H(s) = T \cdot \text{diag}\left[e^{-\gamma_1(s)l}, e^{-\gamma_2(s)l}, \ldots, e^{-\gamma_m(s)l}\right] \cdot T^{-1}
$$

其中 $T$ 是模态变换矩阵，$\gamma_i(s)$ 是第 $i$ 模态的传播常数，$l$ 是线路长度。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 480" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#333"/>
    </marker>
    <marker id="arrow-red" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#dc2626"/>
    </marker>
  </defs>
  
  <!-- Background -->
  <rect width="900" height="480" fill="#ffffff" rx="8"/>
  
  <!-- Title -->
  <text x="450" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#1a1a1a" font-family="sans-serif">频域分析在 EMT 仿真中的方法体系</text>
  
  <!-- Layer 1: Input (Blue) -->
  <rect x="30" y="55" width="180" height="60" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="120" y="78" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e40af" font-family="sans-serif">时域 EMT 波形</text>
  <text x="120" y="96" text-anchor="middle" font-size="11" fill="#3b82f6" font-family="sans-serif">v(t), i(t)</text>
  
  <!-- Arrow from Input to Layer 2 -->
  <line x1="210" y1="85" x2="280" y2="85" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Layer 2: Processing - 5 methods (Green) -->
  <!-- Method 1: 频率扫描 -->
  <rect x="290" y="55" width="130" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="355" y="74" text-anchor="middle" font-size="12" font-weight="bold" fill="#15803d" font-family="sans-serif">频率扫描</text>
  <text x="355" y="90" text-anchor="middle" font-size="10" fill="#22c55e" font-family="sans-serif">Z(f), Y(f)</text>
  
  <!-- Method 2: 向量拟合 -->
  <rect x="290" y="115" width="130" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="355" y="134" text-anchor="middle" font-size="12" font-weight="bold" fill="#15803d" font-family="sans-serif">向量拟合</text>
  <text x="355" y="150" text-anchor="middle" font-size="10" fill="#22c55e" font-family="sans-serif">H(s) 有理逼近</text>
  
  <!-- Method 3: Laplace 逆变换 -->
  <rect x="290" y="175" width="130" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="355" y="194" text-anchor="middle" font-size="12" font-weight="bold" fill="#15803d" font-family="sans-serif">Laplace 逆变换</text>
  <text x="355" y="210" text-anchor="middle" font-size="10" fill="#22c55e" font-family="sans-serif">Theta / WNLT</text>
  
  <!-- Method 4: 频谱分析 -->
  <rect x="290" y="235" width="130" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="355" y="254" text-anchor="middle" font-size="12" font-weight="bold" fill="#15803d" font-family="sans-serif">频谱分析</text>
  <text x="355" y="270" text-anchor="middle" font-size="10" fill="#22c55e" font-family="sans-serif">FFT / Prony</text>
  
  <!-- Method 5: FDNE -->
  <rect x="290" y="295" width="130" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="355" y="314" text-anchor="middle" font-size="12" font-weight="bold" fill="#15803d" font-family="sans-serif">频域网络等值</text>
  <text x="355" y="330" text-anchor="middle" font-size="10" fill="#22c55e" font-family="sans-serif">FDNE 等值模型</text>
  
  <!-- Arrows from Layer 2 to Layer 3 -->
  <line x1="420" y1="80" x2="500" y2="155" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="420" y1="140" x2="500" y2="155" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="420" y1="200" x2="500" y2="155" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="420" y1="260" x2="500" y2="155" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="420" y1="320" x2="500" y2="155" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Layer 3: Output (Purple) -->
  <rect x="510" y="120" width="180" height="70" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="600" y="145" text-anchor="middle" font-size="13" font-weight="bold" fill="#5b21b6" font-family="sans-serif">频域模型输出</text>
  <text x="600" y="163" text-anchor="middle" font-size="11" fill="#8b5cf6" font-family="sans-serif">Z(s), H(s), 有理函数</text>
  <text x="600" y="179" text-anchor="middle" font-size="10" fill="#a78bfa" font-family="sans-serif">极点-留数模型</text>
  
  <!-- Arrow from Output to Layer 4 -->
  <line x1="690" y1="155" x2="750" y2="155" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Layer 4: Applications (Amber) -->
  <!-- App 1: 稳定性分析 -->
  <rect x="760" y="55" width="110" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="815" y="74" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e" font-family="sans-serif">稳定性分析</text>
  <text x="815" y="90" text-anchor="middle" font-size="9" fill="#d97706" font-family="sans-serif">阻抗比判据</text>
  
  <!-- App 2: 频变建模 -->
  <rect x="760" y="120" width="110" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="815" y="139" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e" font-family="sans-serif">频变线路建模</text>
  <text x="815" y="155" text-anchor="middle" font-size="9" fill="#d97706" font-family="sans-serif">ULM / FDNE</text>
  
  <!-- App 3: 谐波诊断 -->
  <rect x="760" y="185" width="110" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="815" y="204" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e" font-family="sans-serif">谐波诊断</text>
  <text x="815" y="220" text-anchor="middle" font-size="9" fill="#d97706" font-family="sans-serif">频谱 / Prony</text>
  
  <!-- App 4: 时域验证 -->
  <rect x="760" y="250" width="110" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="815" y="269" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e" font-family="sans-serif">时域验证</text>
  <text x="815" y="285" text-anchor="middle" font-size="9" fill="#d97706" font-family="sans-serif">EMT 仿真</text>
  
  <!-- Dashed arrows from Output to Applications -->
  <line x1="690" y1="145" x2="760" y2="80" stroke="#333" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#arrow)"/>
  <line x1="690" y1="155" x2="760" y2="145" stroke="#333" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#arrow)"/>
  <line x1="690" y1="165" x2="760" y2="210" stroke="#333" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#arrow)"/>
  <line x1="690" y1="175" x2="760" y2="275" stroke="#333" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#arrow)"/>
  
  <!-- Feedback loop (red dashed) -->
  <path d="M 815 300 L 815 340 L 120 340 L 120 115" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="6,4" fill="none" marker-end="url(#arrow-red)"/>
  <text x="460" y="355" text-anchor="middle" font-size="10" fill="#dc2626" font-family="sans-serif">时域验证反馈（不满足时修正模型参数）</text>
  
  <!-- Legend -->
  <rect x="30" y="380" width="15" height="15" rx="3" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="50" y="393" font-size="10" fill="#333" font-family="sans-serif">输入 (时域波形)</text>
  
  <rect x="160" y="380" width="15" height="15" rx="3" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="180" y="393" font-size="10" fill="#333" font-family="sans-serif">处理方法 (5种)</text>
  
  <rect x="290" y="380" width="15" height="15" rx="3" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="310" y="393" font-size="10" fill="#333" font-family="sans-serif">输出 (频域模型)</text>
  
  <rect x="420" y="380" width="15" height="15" rx="3" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="440" y="393" font-size="10" fill="#333" font-family="sans-serif">应用场景</text>
  
  <line x1="530" y1="387" x2="570" y2="387" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="6,4"/>
  <text x="580" y="393" font-size="10" fill="#333" font-family="sans-serif">时域验证反馈回路</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 频域分析在 EMT 仿真中的方法体系架构</p>

## 关键技术挑战

### 1. 频率耦合与非线性效应
电力电子设备的非线性导致多频率耦合，标准单频扫描方法可能遗漏交叉调制效应。对于 MMC-HVDC 等复杂系统，需采用多频扰动（MFP）方法同时注入多个频率分量，利用 Guillaume 方法优化频率安排以最小化交叉频率（CF）：

$$
\phi_i = -\frac{\pi i(i-1)}{m}
$$

其中 $m$ 是扰动频率数量，$\phi_i$ 是第 $i$ 个频率分量的相位。

### 2. 有理逼近的无源性保证
向量拟合得到的有理函数可能违反无源性，导致时域仿真不稳定。无源性强制（passivity enforcement）是必要后处理步骤，但可能引入额外的拟合误差。Ahmadi 等 2021 提出的网络综合方法从构造层面保证无源性，避免了后处理误差。

### 3. 多端口系统的坐标系选择
阻抗矩阵的数值特性强烈依赖于坐标系。在 abc 三相坐标系中，阻抗矩阵通常满秩且包含所有耦合项；在 dq 坐标系中，对于对称系统可简化为 $2 \times 2$ 矩阵，但需考虑频率耦合。Cifuentes Garcia & Beerten 2026 发现利用 dq 对称性可减少一半的扫描工作量。

### 4. 频域-时域一致性
频域拟合误差与时域波形误差之间没有简单映射关系。低拟合误差（如 RMS < 0.1%）不代表时域仿真稳定，非无源多端口模型可能在 EMT 中产生非物理能量。Francois 等 2023 发现，即使 modal propagation function 的拟合 RMS 误差仅 $9 \times 10^{-4}$，在时域仿真中仍可能因常数延迟 $t$ 的不当选择导致非无源性。

### 5. 宽频带建模的阶数权衡
宽频带（从 DC 到 MHz）建模需要大量极点才能准确捕捉高频谐振。Bode 拟合方法在宽频带下需要数百个零极点，而 RKF 方法可在同等精度下将极点数量减少 30-50%。Kida 等 2024 的 CTWB 线模型中，RKF 用 20 个极点/元素达到 RMS 误差 $2.49 \times 10^{-4}$，而 Bode 拟合的 RMS 误差为 0.14。

## 量化性能边界

| 方法 | 精度指标 | 典型数值 | 来源 |
|------|---------|---------|------|
| EMT 频率扫描（10 μs 步长） | dq 阻抗相对误差 | < 2% (< 1 kHz) | Cifuentes Garcia & Beerten 2026 |
| EMT 频率扫描（10 μs 步长） | 谐振点附近最大误差 | ~16% | Cifuentes Garcia & Beerten 2026 |
| Theta 算法 Laplace 逆变换 | 相对误差 | $10^{-9}$ | Castañón 等 2021 |
| WNLT Laplace 逆变换 | 相对误差 | $10^{-5}$ | Castañón 等 2021 |
| RKF 拟合（CTWB 线模型） | h RMS 误差 | $2.49 \times 10^{-4}$ (20 极点/元素) | Kida 等 2024 |
| VF 拟合（CTWB 线模型） | h RMS 误差 | $4.91 \times 10^{-4}$ (21 极点/元素) | Kida 等 2024 |
| Bode 拟合（CTWB 线模型） | h RMS 误差 | 0.14 | Kida 等 2024 |
| Theta vs Epsilon 算法 | 计算速度比 | Theta 比 Epsilon 快 1.9× | Castañón 等 2021 |
| FDNE 网络压缩 | 仿真时间减少 | ~80% | Saldaña & Calzolari 2022 |

## 适用边界与选择指南

### 方法选择决策表

| 应用场景 | 推荐方法 | 替代方法 | 注意事项 |
|---------|---------|---------|---------|
| 逆变器小信号稳定性分析 | EMT 频率扫描（dq 域） | 线性化状态空间模型 | 需验证工作点附近线性化有效性 |
| 宽频带线路/电缆建模 | RKF + FDNE | VF + FDNE | RKF 极点数量更少，计算效率更高 |
| Laplace 域瞬态分析 | Theta 算法 | WNLT | Theta 算法精度 $10^{-9}$，但计算开销为 WNLT 的 4.2× |
| 谐波频谱分析 | FFT + 窗函数 | Prony 分析 | FFT 适合稳态周期信号，Prony 适合衰减振荡 |
| 多端口系统阻抗辨识 | 多频扰动 (MFP) | 单频扰动 | MFP 需优化频率安排以最小化交叉频率 |
| 无源性保证的频域等值 | 网络综合法 (Ahmadi) | VF + 无源性强制 | 网络综合法从构造层面保证无源性 |
| 快速稳定性筛查 | 频率扫描 Bode 图 | 根轨迹分析 | 频率扫描计算效率高，根轨迹精度高但建模复杂 |

### 失效场景

- **强非线性工况**：故障穿越、保护动作、控制饱和等非线性事件必须用时域 EMT 验证，频域分析仅提供线性化近似。
- **多时间尺度系统**：当系统包含 ns 级开关瞬态和 s 级机电暂态时，单一频域模型无法覆盖全部动态。需采用多速率或混合仿真。
- **非平稳信号**：Prony 分析和 FFT 假设信号在分析窗口内平稳或准平稳，对于快速变化的暂态过程误差较大。
- **频带外推**：有理函数拟合仅在拟合频带内有效，外推到未覆盖频带可能导致严重误差甚至不稳定。

## 相关方法 / 相关模型 / 相关主题

- [[fft]] - 快速傅里叶变换，频谱分析的基础工具
- [[vector-fitting]] - 向量拟合，频域响应有理逼近的工业标准
- [[prony-analysis]] - Prony 分析，从时域波形提取模态参数
- [[harmonic-analysis]] - 谐波分析，频域分析在电能质量中的应用
- [[frequency-dependent-modeling]] - 频率相关建模，频域分析在元件建模中的应用
- [[fdne-model]] - 频域网络等值，大规模系统仿真的核心等值技术
- [[emt-simulation]] - EMT 仿真，频域分析的时域验证平台
- [[impedance-modeling]] - 阻抗建模，频域分析的物理基础
- [[frequency-scan]] - 频率扫描方法，频域分析的测量手段
- [[passivity-enforcement]] - 无源性强制，频域逼近的必要后处理
- [[numerical-inverse-laplace-transform]] - 数值 Laplace 逆变换，频域到时域转换的另一种途径
- [[modal-analysis]] - 模态分析，频域稳定性诊断的工具
- [[frequency-domain-analysis]] - 频域分析（本页面）

## 来源论文

- **Cifuentes Garcia & Beerten 2026** — 提出了 Z-Tool，一种用于 EMT 模型小信号稳定性分析的频域特征化工具。在 VSC-HVDC 系统上验证了 EMT 频率扫描方法，量化了仿真步长对阻抗辨识精度的影响（10 μs 步长下 < 1 kHz 误差 < 2%），并提出了利用 dq 对称性减少扫描工作量的优化策略。
- **Jiang et al. 2026** (EMT based dynamic frequency scanning tool) — 开发了集成频率扫描和稳定性分析的动态频率扫描工具，在 PSCAD/EMTDC 中实现。通过 MMC-VSG 系统验证了扫描方法的准确性，对比了电压源型和电流源型 VSG 在不同 SCR 下的稳定性边界。
- **Ahmadi et al. 2021** — 提出了一种保证无源性的多端口频率相关网络等值模型构建方法。通过网络综合技术构造正实函数，确保多端口 FDNE 模型在所有频率下满足无源性条件，避免了传统 VF + 无源性强制方法的后处理误差。
- **Kida et al. 2024** — 比较了 Rational Krylov Fitting (RKF) 与 Vector Fitting (VF) 在频变网络等值有理逼近中的计算性能。发现 RKF 在 CTWB 线模型中用更少的极点达到同等精度，Bode 拟合方法在宽频带下需要显著更多的零极点。
- **Saldaña & Calzolari 2022** — 提出了高效的多端口 FDNE 实现方法，通过频带压缩、矩阵压缩和并行递推卷积显著减少内存和计算开销。
- **Gustavsen 2012** — 研究了基于模态域的平行输电线路建模方法，强调了模态变换矩阵在频变线路模型中的关键作用。
- **Castañón et al. 2021** — 提出了基于 Brezinski theta 算法的 Laplace 逆变换新方法，不依赖数据窗口截断，可保证 $10^{-9}$ 量级的一致性精度。在四回线系统测试中验证了方法的准确性和效率。
- **Francois et al. 2023** — 分析了常延迟时间策略在宽频线路模型中的准确性来源，发现常延迟选择不当是导致频变模型时域误差的主要原因。比较了 RKF、VF 和 Bode 拟合在宽频线路建模中的性能。
- **Gurrala 2015** — 提出了 Loewner 矩阵方法用于电力系统 FDNE 建模，提供了另一种基于系统辨识的频域等值途径。
- **De Conti & Lima 2026** — 评估了地下电缆地返回阻抗解析表达式的准确性，为频域电缆建模提供了土壤阻抗参数基准。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[analysis-and-estimation-of-truncation-errors-in-modeling-complex-resonant-circui-fix|Analysis and estimation of truncation errors in modeling com]] | 2002 |
| [[a-novel-distance-protection-algorithm-in-frequency-domain-based-on-parameter-ide|A Novel Distance Protection Algorithm in Frequency Domain Ba]] | 2012 |
| [[dual-band-reduced-order-model-of-an-hvdc-link-embedded-into-a-power-network-for-|Dual-Band Reduced-Order Model of an HVDC Link Embedded into ]] | 2019 |
| [[laplace-transform-inversion-through-the-theta-algorithm-for-power-system-emt-ana|Laplace transform inversion through the theta algorithm for ]] | 2021 |
| [[low-complexity-graph-based-traveling-wave-models-for-hvdc-grids-with-hybrid-tran|Low-complexity graph-based traveling wave models for HVDC gr]] | 2022 |
| [[analytical-and-measurement-based-wideband-two-port-modeling-of-dc-dc-converters-|Analytical and measurement-based wideband two-port modeling ]] | 2023 |
| [[impact-of-solenoid-effects-on-series-impedance-of-three-core-armoured-cables|Impact of solenoid effects on series impedance of three-core]] | 2023 |
| [[assessment-of-the-accuracy-of-the-modal-domain-line-models-with-real-and-frequen|Assessment of the accuracy of the modal-domain line models w]] | 2024 |
| [[high-frequency-transients-in-buried-insulated-wires-transmission-line-simulation-19、20、21|High-frequency transients in buried insulated wires: Transmi]] | 2024 |
