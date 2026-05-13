---
title: "信号处理方法"
type: method
tags: [signal-processing, dsp, waveform-analysis, feature-extraction, filtering, fft, harmonic-analysis, prony-analysis, wavelet, impedance-measurement, small-signal-stability]
created: "2026-05-04"
updated: "2026-05-13"
---

# 信号处理方法

## 定义

信号处理方法是电磁暂态（EMT）仿真中对电压、电流和功率波形进行数字化分析的核心手段。它将时域波形 $x(t)$ 通过算子 $\mathcal{F}$ 映射为可用于保护、诊断、稳定性分析和参数辨识的结果 $y(t)$：

$$
y(t) = \mathcal{F}\big(x(t)\big)
$$

其中 $\mathcal{F}$ 可以是滤波、频谱分析、模态辨识、特征提取或参数识别等算子。信号处理方法在 EMT 中处于"波形→信息"的枢纽位置，是连接物理仿真与系统决策的桥梁。

信号处理在 EMT 中的核心任务包括：

1. **频谱分析**：从暂态波形中提取谐波含量、次同步振荡频率
2. **模态辨识**：从衰减振荡中提取阻尼比、频率和幅值
3. **特征提取**：从小波熵、奇异值等统计量中识别故障类型和位置
4. **参数识别**：从测量数据中辨识系统阻抗、线路参数和控制参数
5. **滤波与预处理**：去除噪声、直流偏移，提取基波分量和特定频率成分

## EMT 中的作用

在 EMT 研究中，信号处理方法主要用于以下场景：

- **谐波分析与电能质量评估**：从逆变器、换流器波形中提取谐波频谱，评估 THD 和次同步振荡
- **保护与故障诊断**：基于小波熵、频域参数识别的继电保护算法，实现故障定位和类型判别
- **小信号稳定性分析**：通过频域扫描（frequency scanning）和阻抗测量，提取系统传递函数并进行特征值分析
- **动态相量提取**：在 EMT-动态相量混合仿真中，从 EMT 侧提取动态相量传递给 TS 侧
- **参数辨识与模型验证**：从实测或仿真波形中辨识系统参数，验证模型准确性
- **频率域特征化**：通过注入扰动信号测量黑盒模型的频率响应（如 Z-Tool）

EMT 信号处理与传统电力系统分析的关键区别在于：**EMT 保留了完整的电磁暂态高频成分**（可达数百 kHz），因此信号处理方法必须处理宽频带（DC 到数百 kHz）、非正弦、非稳态的复杂波形。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 420" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <path d="M0,0 L8,3 L0,6" fill="#333"/>
    </marker>
  </defs>
  
  <!-- Title -->
  <text x="450" y="28" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">EMT 信号处理方法体系架构</text>
  
  <!-- Input node -->
  <rect x="350" y="45" width="200" height="40" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="450" y="70" text-anchor="middle" font-size="13" fill="#1e3a5f">EMT 波形 x(t)</text>
  
  <!-- Processing layer - 6 methods -->
  <rect x="30" y="120" width="140" height="50" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="100" y="140" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">傅里叶分析</text>
  <text x="100" y="155" text-anchor="middle" font-size="9" fill="#166534">DFT/FFT/拉普拉斯</text>
  
  <rect x="190" y="120" width="140" height="50" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="260" y="140" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">动态相量提取</text>
  <text x="260" y="155" text-anchor="middle" font-size="9" fill="#166534">GAM/SFA/时变相量</text>
  
  <rect x="370" y="120" width="140" height="50" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="440" y="140" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">小波分析</text>
  <text x="440" y="155" text-anchor="middle" font-size="9" fill="#166534">CWT/DWT/奇异熵</text>
  
  <rect x="550" y="120" width="140" height="50" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="620" y="140" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">谐波保真建模</text>
  <text x="620" y="155" text-anchor="middle" font-size="9" fill="#166534">VI插值/谐波AVM</text>
  
  <rect x="730" y="120" width="140" height="50" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="800" y="140" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534">频域阻抗测量</text>
  <text x="800" y="155" text-anchor="middle" font-size="9" fill="#166534">Z-Tool/扰动注入</text>
  
  <!-- Arrows from input to processing -->
  <line x1="380" y1="85" x2="100" y2="120" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="410" y1="85" x2="260" y2="120" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="450" y1="85" x2="440" y2="120" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="490" y1="85" x2="620" y2="120" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="520" y1="85" x2="800" y2="120" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Application layer -->
  <rect x="30" y="220" width="140" height="50" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="100" y="240" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e">谐波分析</text>
  <text x="100" y="255" text-anchor="middle" font-size="9" fill="#92400e">电能质量</text>
  
  <rect x="190" y="220" width="140" height="50" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="260" y="240" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e">保护与诊断</text>
  <text x="260" y="255" text-anchor="middle" font-size="9" fill="#92400e">故障定位</text>
  
  <rect x="370" y="220" width="140" height="50" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="440" y="240" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e">小信号稳定性</text>
  <text x="440" y="255" text-anchor="middle" font-size="9" fill="#92400e">特征值分析</text>
  
  <rect x="550" y="220" width="140" height="50" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="620" y="240" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e">混合仿真</text>
  <text x="620" y="255" text-anchor="middle" font-size="9" fill="#92400e">EMT-Phasor</text>
  
  <rect x="730" y="220" width="140" height="50" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="800" y="240" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e">参数辨识</text>
  <text x="800" y="255" text-anchor="middle" font-size="9" fill="#92400e">模型验证</text>
  
  <!-- Arrows from processing to application -->
  <line x1="100" y1="170" x2="100" y2="220" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="260" y1="170" x2="260" y2="220" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="440" y1="170" x2="440" y2="220" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="620" y1="170" x2="620" y2="220" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="800" y1="170" x2="800" y2="220" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Cross connections -->
  <line x1="170" y1="145" x2="260" y2="220" stroke="#999" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="330" y1="145" x2="260" y2="220" stroke="#999" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="440" y1="170" x2="440" y2="220" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="620" y1="170" x2="620" y2="220" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="800" y1="145" x2="800" y2="220" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Output node -->
  <rect x="300" y="310" width="300" height="40" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="450" y="335" text-anchor="middle" font-size="13" fill="#4c1d95">保护/诊断/稳定性/参数辨识结果 y(t)</text>
  
  <!-- Arrows from application to output -->
  <line x1="100" y1="270" x2="350" y2="310" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="260" y1="270" x2="400" y2="310" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="440" y1="270" x2="450" y2="310" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="620" y1="270" x2="500" y2="310" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="800" y1="270" x2="650" y2="310" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Key references at bottom -->
  <text x="450" y="380" text-anchor="middle" font-size="10" fill="#666">Z-Tool (Cifuentes 2026) · GAM (Rupasinghe 2021) · Theta (Castanon 2021) · WSE (Liu 2009) · VI (Horiuchi 2020)</text>
  <text x="450" y="400" text-anchor="middle" font-size="10" fill="#666">TDSS (Agarwal 2022) · Companion (Chindu 2023) · Matrix Pencil (Sun et al.)</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · EMT 信号处理方法体系架构：从波形输入到应用输出的方法分类与数据流</p>

## 核心方法体系

### 1. 傅里叶分析与频域提取

傅里叶变换是信号处理的基础工具。在 EMT 中，常用的频域提取方法包括：

**标准 DFT/FFT**：对采样信号 $x[n]$（$n=0,1,\dots,N-1$）进行离散傅里叶变换：

$$
X[k] = \sum_{n=0}^{N-1} x[n] e^{-j 2\pi kn / N}, \quad k = 0, 1, \dots, N-1
$$

FFT 将计算复杂度从 $O(N^2)$ 降至 $O(N\log N)$，是实时保护算法的基础。

**矩阵铅笔算法（Matrix Pencil）**：针对含直流偏移的暂态波形，矩阵铅笔算法能够准确提取基波分量和 DC 偏移分量。文献 [Sun et al.] 指出，传统 DFT 在暂态过程中因 DC 偏移干扰而失真，矩阵铅笔算法通过构造 Hankel 矩阵并求解广义特征值问题，在含噪环境下仍可获得准确的基波相量。该方法特别适用于故障暂态过程中的距离保护算法。

**拉普拉斯变换反演**：对于频域函数 $F(s)$，其时域响应 $f(t)$ 通过 Laplace 反演积分获得：

$$
f(t) = \frac{1}{2\pi j} \int_{c-j\infty}^{c+j\infty} F(s) e^{st} ds
$$

离散化后表示为：

$$
\tilde{f}(t) = \frac{e^{ct} \Delta\omega}{\pi} \sum_{k=0}^{\infty} \text{Re}\left[ F(c+jk\Delta\omega) e^{jk\Delta\omega t} \right]
$$

其中 $c$ 为阻尼常数，$\Delta\omega$ 为频率步长。传统 WNLT（Windowed Numerical Laplace Transform）方法通过加窗截断无限求和，典型精度为 $10^{-3} \sim 10^{-6}$。Castañón 等 [2021] 提出基于 Brezinski Theta 算法的加速方法，无需截断即可保证高一致精度，在中等计算成本下超越 WNLT 的精度极限。

### 2. 动态相量提取

动态相量（Dynamic Phasor）是 EMT-动态相量混合仿真的核心接口技术。Rupasinghe 等 [2021] 系统评估了三种动态相量提取方法：

**（1）稳态相量（Steady-State Phasor）**：基于 Blondel-Park 变换，将三相信号映射为复数相量：

$$
\mathbf{X}(t) = \frac{\sqrt{2}}{3} \begin{bmatrix}
e^{-j\theta} & e^{-j(\theta-2\pi/3)} & e^{-j(\theta+2\pi/3)}
\end{bmatrix} \begin{bmatrix} x_a(t) \\ x_b(t) \\ x_c(t) \end{bmatrix}
$$

其中 $\theta = \omega_0 t$。该方法仅适用于平衡三相系统，无法处理不平衡工况。

**（2）时变相量（Time-Varying Phasor）**：对平衡三相信号应用 Blondel-Park 变换算子 $\mathcal{P}(\cdot)$：

$$
\mathcal{P}\left(\frac{d}{dt}x(t)\right) = \frac{d}{dt}\mathcal{P}(x(t)) + j\omega_0 \mathcal{P}(x(t))
$$

该方法的算子是线性的、双射的，且保留了导数关系。时变相量是动态相量的特例，当其导数项可忽略时退化为稳态相量。

**（3）广义平均法（Generalized Averaging Method, GAM）**：基于信号的 Fourier 系数序列：

$$
\langle x \rangle_k(t) = \frac{1}{T} \int_0^T x(t-T+s) e^{-jk\omega_0(t-T+s)} ds
$$

其中 $k$ 为谐波阶次，$\omega_0 = 2\pi/T$。GAM 能够表示波形的所有谐波分量，但计算成本随谐波数量线性增长。

**（4）移频分析法（Shifted Frequency Analysis, SFA）**：将带通信号分解为低通信号与正弦载波的乘积，通过频移操作提取低频包络。SFA 与解析信号理论紧密相关，适合处理宽频带暂态信号。

Rupasinghe 等的评估表明：GAM 方法在谐波保真度上最优，但计算开销最大；时变相量在平衡工况下精度与 GAM 相当且计算更轻量；SFA 最适合宽频带信号处理。

### 3. 小波分析与时频分析

小波变换提供多分辨率时频分析能力，特别适合非平稳暂态信号的处理。

**连续小波变换（CWT）**：

$$
W(a,b) = \frac{1}{\sqrt{|a|}} \int_{-\infty}^{\infty} x(t) \psi^*\left(\frac{t-b}{a}\right) dt
$$

其中 $\psi$ 为小波基函数，$a$ 为缩放因子，$b$ 为平移因子。

**小波奇异熵（Wavelet Singular Entropy, WSE）**：刘青等 [2009] 将小波奇异熵应用于输电线路单端暂态保护。其核心思想是：故障暂态信号包含从直流到高频的宽频成分，区内故障时频谱分布宽、信号复杂度高，对应较大的小波奇异熵值；区外故障时高频分量衰减严重，熵值较小。

小波奇异熵定义为小波分解系数的概率分布熵：

$$
H = -\sum_{i=1}^{N} p_i \log p_i, \quad p_i = \frac{|W_i|}{\sum_{j=1}^{N} |W_j|}
$$

其中 $W_i$ 为第 $i$ 个小波分解系数，$N$ 为分解系数总数。

刘青等的 PS CAD/EMTDC 仿真表明：小波奇异熵判据不受故障位置、故障类型、过渡电阻及故障时刻的影响。在 500 kV 超高压线路中，DB4 小波 4 层分解、窗宽 $w=100$ 时，区内故障熵值显著大于区外故障（典型差值 > 3 倍），保护动作可靠性高。

**离散小波变换（DWT）**：Mahmoudpour 等 [2015] 实现了在线瞬时 DWT 分解工具箱，支持 EMT 仿真中的实时信号处理。DWT 通过滤波器组实现信号的逐级分解，计算复杂度为 $O(N)$，适合 FPGA 和嵌入式实现。

### 4. 谐波保真建模中的信号处理

Horiuchi 等 [2020] 提出电压插值法（Voltage Interpolation, VI），在 EMT 仿真中以较大时间步长保留逆变器开关谐波：

传统开关模型（SW model）需要仿真步长为开关周期的 1/100 才能准确模拟谐波。VI 方法通过在每个开关事件处对电压进行插值修正：

$$
v_{\text{interp}}(t_{n+1}) = s \cdot V_{dc}
$$

其中 $s \in [0,1]$ 为插值系数，由 PWM 参考信号与载波的交点时刻确定。该方法使时间步长可扩展 5 倍而不降低谐波精度，单相机组计算时间减少约 3 倍。

Cao 等 [2026] 提出谐波保留平均值模型（Harmonic-Preserved AVM），在平均值模型中嵌入谐波补偿项，通过频域信号处理提取主导谐波分量并叠加到等效电压源上，在计算效率和谐波保真度之间取得平衡。

### 5. 频域阻抗测量与小信号稳定性分析

Cifuentes Garcia 和 Beerten [2026] 开发的 Z-Tool 是首个开源的 EMT 频域辨识工具，通过 EMT 仿真测量多端 AC/DC 系统的导纳矩阵。

**扰动注入方法**：在稳态工作点处注入正弦扰动：

$$
\Delta v(t) = \sum_{i=1}^{m} a_i \sin(\omega_i t + \phi_i)
$$

其中 $a_i$ 为振幅（通常 0.02%~2% 标幺值），$\omega_i$ 为扫描频率，$\phi_i$ 为初始相位。通过 FFT 从响应中提取频率响应函数：

$$
\mathbf{Y}(j\omega) = \Delta \mathbf{i}(\omega) \cdot \Delta \mathbf{v}(\omega)^{-1}
$$

其中 $\Delta \mathbf{i}$ 和 $\Delta \mathbf{v}$ 为 $N \times N$ 电流和电压扰动矩阵。

**多频同时注入**：Z-Tool 支持多频同时注入以加速扫描，但需最小化 crest factor（峰值因子）：

$$
\text{CF} = \frac{\max|\Delta v(t)|}{\Delta v_{\text{RMS}}}
$$

**dq 坐标系解耦**：Z-Tool 采用 amplitude-invariant 的 $abc \to dq$ 变换：

$$
T_{dq}(\theta) = \frac{2}{3} \begin{bmatrix}
\cos\theta & \cos(\theta-2\pi/3) & \cos(\theta+2\pi/3) \\
\sin\theta & \sin(\theta-2\pi/3) & \sin(\theta+2\pi/3)
\end{bmatrix}
$$

dq 框架天然捕获频率耦合效应，无需显式处理频率偏移。对于 $N \times N$ 导纳矩阵，只需 $N$ 个线性独立的扰动向量即可完整辨识。

**精度分析**：辨识误差取决于仿真时间步长。Cifuentes Garcia 等量化了时间步长、扰动幅度和多频注入对辨识精度的影响，给出了参数选择的实用指南。

**Chindu 和 Kulkarni [2023]** 提出基于 EMT 伴随电路（Companion Circuit）的自动化小信号稳定性分析方法。该方法利用 EMT 仿真中的导纳矩阵及其 LU 分解因子，直接提取离散时间状态空间模型：

$$
\mathbf{x}_{k+1} = \mathbf{A}\mathbf{x}_k + \mathbf{B}\mathbf{u}_k
$$

其中状态向量 $\mathbf{x}_k = [\mathbf{i}_{\text{hist},L,k}^T, \mathbf{i}_{\text{hist},C,k}^T]^T$ 为电感和电容的历史电流源。状态转移矩阵 $\mathbf{A}$ 和输入矩阵 $\mathbf{B}$ 可由伴随电路的导纳矩阵 $\mathbf{G}$ 直接构造：

$$
\mathbf{A} = \begin{bmatrix}
\mathbf{I}_{n_L} & \mathbf{0} \\
\mathbf{0} & -\mathbf{I}_{n_C}
\end{bmatrix} - \frac{h}{2} \begin{bmatrix}
\mathbf{L}^{-1}\mathbf{A}_L \\
\frac{4}{h^2}\mathbf{C}
\end{bmatrix} \mathbf{G}^{-1} \begin{bmatrix}
\mathbf{A}_L^T & \mathbf{A}_C^T
\end{bmatrix}
$$

$$
\mathbf{B} = \begin{bmatrix}
\frac{h}{2}\mathbf{L}^{-1} \\
-\frac{4}{h}\mathbf{C}
\end{bmatrix} \mathbf{G}^{-1} \begin{bmatrix} \mathbf{A}_L^T \\ \mathbf{A}_C^T \end{bmatrix}
$$

该方法无需重新求逆 $\mathbf{G}$，直接复用 EMT 仿真中的 LU 因子，计算开销极小。

### 6. 频域参数识别与距离保护

Sun 等提出基于参数识别的频域距离保护算法。该算法在故障分量距离保护基础上，利用 R-L 模型和零序网络推导出含三个系数的线性方程：

$$
\frac{\dot{U}_{MA}}{\dot{I}_M} = Z_1 + (Z_0-Z_1) \cdot I_{\text{factor}} \cdot s
$$

其中 $Z_1$ 为正序阻抗，$Z_0$ 为零序阻抗，$s$ 为故障距离，$I_{\text{factor}}$ 为零序电流分布系数。通过矩阵铅笔算法准确提取基波和 DC 偏移分量，避免了时域微分带来的额外误差。

### 7. 时域稳态分析中的信号处理

Agarwal 和 Pileggi [2022] 提出时域稳态（Time-Domain Steady-State, TDSS）方法，通过波形迭代而非时间步进求解稳态：

传统 EMT 仿真需经过大量时间步长才能收敛到稳态，计算效率低下。TDSS 方法将系统解耦为线性传输网络和非线性设备，每次迭代更新整个波形周期：

$$
\mathbf{Y}_{\text{lin}} \dot{\mathbf{x}}_{\text{lin}} = \mathbf{Y}_{\text{lin}} \mathbf{x}_{\text{lin}} + \mathbf{J}_{\text{lin}} + \mathbf{I}_p
$$

$$
\dot{\mathbf{x}}_{\text{nlin}} = f_{\text{nlin}}(\mathbf{x}_{\text{nlin}}, \mathbf{V}_p)
$$

其中 $\mathbf{I}_p$ 为端口电流，$\mathbf{V}_p$ 为端口电压。该方法在波形级别迭代，而非时间步进，显著加速了稳态收敛。

## 形式化表达

信号处理方法的核心数学工具可归纳如下：

**频域变换**：

$$
X(\omega) = \int_{-\infty}^{\infty} x(t) e^{-j\omega t} dt
$$

**拉普拉斯反演（Theta 算法加速）**：

$$
f(n\Delta t) + \epsilon_{\text{al}} = \frac{2e^{cn\Delta t}}{\Delta t} \cdot \frac{1}{N} \sum_{k=0}^{M-1} \text{Re}\left[ F_k e^{j2\pi nk/N} \right] + \epsilon_{\text{tr}}
$$

**动态相量提取（GAM）**：

$$
\langle x \rangle_k(t) = \frac{1}{T} \int_0^T x(t-T+s) e^{-jk\omega_0(t-T+s)} ds
$$

**小波奇异熵**：

$$
H = -\sum_{i=1}^{N} \frac{|W_i|}{\sum |W_j|} \log\left(\frac{|W_i|}{\sum |W_j|}\right)
$$

**阻抗矩阵辨识**：

$$
\mathbf{Y}(j\omega) = \Delta\mathbf{i}(\omega) \cdot \Delta\mathbf{v}(\omega)^{-1}
$$

## 关键技术挑战

**（1）宽频带信号处理**：EMT 仿真覆盖 DC 到数百 kHz 的宽频带，传统基于工频的相量方法失效。需要多分辨率分析工具（如小波、动态相量）来同时捕捉慢速机电暂态和快速电磁暂态。

**（2）非稳态信号的频域提取**：故障暂态包含直流偏移、衰减振荡和高频谐波，传统 DFT 因频谱泄漏而产生显著误差。矩阵铅笔算法、Theta 算法等高级提取方法能够处理非稳态信号，但计算复杂度较高。

**（3）实时性与精度的权衡**：在线保护算法要求毫秒级响应，而高精度频域辨识需要大量数据窗口。Horiuchi 等的 VI 方法通过电压插值在保持谐波精度的同时将时间步长扩展 5 倍，Chindu 等的伴随电路方法通过复用 EMT 内部计算结构将小信号分析的计算开销降至极低。

**（4）黑盒模型的频域表征**：电力电子设备的详细模型通常为黑盒，无法获取解析传递函数。Z-Tool 通过 EMT 仿真中的扰动注入和 FFT 分析，从时域响应中提取频域导纳矩阵，为小信号稳定性分析提供了实用的频域接口。

**（5）多频同时注入的精度损失**：Z-Tool 的多频注入技术可显著加速扫描，但 crest factor 控制和频率间串扰是精度保证的关键。Cifuentes Garcia 等的量化研究表明，时间步长过小会引入数值振荡，过大则丢失高频细节。

## 量化性能边界

| 方法 | 性能指标 | 数据来源 |
|------|---------|---------|
| VI 插值法（Horiuchi 2020） | 时间步长扩展 5 倍，计算时间减少 3 倍，谐波保真度无明显下降 | IEEE Trans. Power Electronics |
| Theta 算法（Castanon 2021） | 精度 $10^{-9}$ 量级，样本数从 $2^{20}$ 降至 $2^{10}$ 量级 | Electric Power Systems Research 197 |
| 小波奇异熵（Liu 2009） | 区内/区外故障熵值差 > 3 倍，不受故障位置、类型、过渡电阻影响 | 电力系统自动化 |
| Z-Tool 多频注入（Cifuentes 2026） | 扰动幅度 0.02%~2% 标幺值，辨识误差取决于时间步长 | Electric Power Systems Research 252 |
| 伴随电路方法（Chindu 2023） | 直接复用 EMT LU 因子，无需额外求逆，计算开销极小 | IEEE Trans. Power Delivery |
| 矩阵铅笔算法（Sun et al.） | 准确提取基波和 DC 偏移，优于 DFT 在暂态过程中的表现 | 频率域距离保护 |
| TDSS 波形迭代（Agarwal 2022） | 在波形级别迭代而非时间步进，显著加速稳态收敛 | Electric Power Systems Research 213 |

## 适用边界与选择指南

| 应用场景 | 推荐方法 | 原因 |
|---------|---------|-----|
| 谐波分析与电能质量评估 | DFT/FFT + 矩阵铅笔 | 快速提取基波和主导谐波，矩阵铅笔处理 DC 偏移 |
| 小信号稳定性分析 | Z-Tool 频域扫描 | 从黑盒 EMT 模型提取导纳矩阵，支持多端 AC/DC 系统 |
| EMT-动态相量混合仿真 | GAM 动态相量提取 | 保留所有谐波分量，精度最高 |
| 故障检测与保护 | 小波奇异熵 | 对故障类型、位置、过渡电阻不敏感，灵敏度高 |
| 快速稳态分析 | TDSS 波形迭代 | 避免大量时间步进，在波形级别收敛 |
| 在线实时保护 | DWT + 矩阵铅笔 | 计算复杂度 $O(N)$，适合 FPGA 实现 |
| 伴随电路小信号分析 | Chindu 伴随电路法 | 直接复用 EMT 内部矩阵，自动化程度高 |
| 拉普拉斯反演高精度需求 | Theta 算法 | 无需截断，保证高一致精度 |

## 相关方法

- [[filtering]] — 数字滤波与预处理方法
- [[fft]] — 快速傅里叶变换
- [[discrete-fourier-transform]] — 离散傅里叶变换
- [[fourier-series]] — 傅里叶级数展开
- [[fourier-filtering]] — 傅里叶滤波
- [[prony-analysis]] — Prony 分析与模态提取
- [[vector-fitting]] — 矢量拟合与有理拟合
- [[curve-fitting]] — 曲线拟合方法
- [[impedance-measurement]] — 阻抗测量方法
- [[harmonic-analysis-methods]] — 谐波分析方法
- [[harmonic-interaction]] — 谐波相互作用分析
- [[phasor-model]] — 相量模型
- [[dynamic-phasor]] — 动态相量法
- [[small-signal-stability]] — 小信号稳定性分析
- [[frequency-domain-analysis]] — 频域分析
- [[parameter-identification]] — 参数辨识方法
- [[least-squares-method]] — 最小二乘法
- [[prony-analysis]] — Prony 分析
- [[modal-analysis]] — 模态分析
- [[time-domain-impedance-estimation]] — 时域阻抗估计
- [[frequency-scan]] — 频率扫描方法
- [[frequency-scanning]] — 频率扫描

## 来源论文

1. **Cifuentes Garcia & Beerten (2026)** — Z-Tool: 基于 EMT 仿真的多端 AC/DC 系统频域辨识工具，提出正弦扰动注入、多频同时注入、dq 坐标系解耦和导纳矩阵完整辨识方法
2. **Rupasinghe, Filizadeh & Strunz (2021)** — 系统评估动态相量提取方法（稳态相量、时变相量、GAM、SFA），为 EMT-动态相量混合仿真提供方法选择指南
3. **Castañón et al. (2021)** — 提出基于 Brezinski Theta 算法的 Laplace 反演加速方法，超越 WNLT 的精度极限，保证高一致精度
4. **Liu et al. (2009)** — 将小波奇异熵应用于输电线路单端暂态保护和全线相继速动保护，证明熵判据不受故障位置、类型、过渡电阻影响
5. **Horiuchi, Sano & Noda (2020)** — 提出电压插值法（VI），在 EMT 仿真中以较大时间步长保留逆变器开关谐波，时间步长扩展 5 倍、计算时间减少 3 倍
6. **Agarwal & Pileggi (2022)** — 提出时域稳态（TDSS）波形迭代方法，通过解耦线性网络和非线性设备，在波形级别加速稳态收敛
7. **Chindu & Kulkarni (2023)** — 提出基于 EMT 伴随电路的自动化小信号稳定性分析方法，直接复用 EMT 内部导纳矩阵和 LU 因子提取状态空间模型
8. **Sun et al.** — 提出基于参数识别的频域距离保护算法，利用矩阵铅笔算法提取基波和 DC 偏移，解决传统 DFT 在暂态过程中的频谱泄漏问题
9. **Cao et al. (2026)** — 谐波保留平均值模型，在平均值模型中嵌入谐波补偿项，平衡计算效率和谐波保真度
10. **Mahmoudpour et al. (2015)** — 在线瞬时 DWT 分解工具箱，支持 EMT 仿真中的实时小波信号处理
