---
title: "傅里叶滤波 (Fourier Filtering)"
type: method
tags: [fourier, filtering, harmonic, signal-processing, dft, fft, relay, window-function, gibbs-oscillation]
created: "2026-05-02"
updated: "2026-05-16"
---

# 傅里叶滤波 (Fourier Filtering)

## 定义与边界

傅里叶滤波是在频域中选择、提取或抑制特定频率分量的信号处理方法。它以 DFT/FFT、滑动 DFT、正交傅里叶滤波器或窗函数加权为实现形式，把采样波形 $x[n]$ 映射到频率分量 $X[k]$，再围绕基波、谐波、间谐波或振荡频率进行估计。

该方法是 [[harmonic-analysis]]、数字继电保护 ([[digital-distance-protection]]、[[relay-protection]])、[[phasor-measurement-unit]] 和 EMT 结果后处理的常用工具，但它不是 EMT 数值求解器本身。若研究对象是网络频率响应，应连接到 [[frequency-domain-analysis]]、[[frequency-scan]] 和 [[impedance-measurement]]；若研究对象是多频率模型，应连接到 [[dynamic-phasor]]。

## EMT 中的作用

傅里叶滤波在 EMT 工作流中通常出现在四个位置：

1. **波形诊断**：从 EMT 输出的电压、电流中提取基波、谐波、间谐波和低频振荡分量，用于电能质量评估和谐波源定位。
2. **保护算法**：在距离保护、差动保护或故障检测中估计基波相量，并抑制直流偏置分量和谐波分量，防止保护误动或拒动。
3. **模型验证**：比较详细开关模型 (SW)、平均值模型 (AV) 和频域等值模型在目标频段的幅值与相位，验证 EMT 建模精度。
4. **接口变量提取**：在 EMT 与动态相量、移频相量或混合仿真接口 ([[hybrid-simulation]]、[[co-simulation]]) 中生成慢变复包络，实现域间数据交换。

这些用途都依赖窗口长度 $N$、采样频率 $f_s$、频率参考和同步策略。不能只写"使用 FFT 得到准确结果"，而应说明被提取的频率、观测窗口和误差来源。

## 核心机制

### 离散傅里叶变换 (DFT)

对 $N$ 点采样序列，DFT 定义为：

$$X[k] = \sum_{n=0}^{N-1} x[n] e^{-j 2\pi kn/N}, \quad k = 0, 1, \ldots, N-1$$

其逆变换 (IDFT) 为：

$$x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] e^{j 2\pi kn/N}$$

快速算法 (FFT) 通过蝶形运算将计算复杂度从 $O(N^2)$ 降至 $O(N \log_2 N)$，是 EMT 后处理中提取频谱的标准实现。当 $N$ 为 2 的幂次时，可采用基-2 Cooley-Tukey 算法。

### 频率映射与分辨率

采样频率 $f_s$ 与 DFT 频率分辨率 $\Delta f$ 的关系为：

$$\Delta f = \frac{f_s}{N} = \frac{1}{T_{\text{window}}}$$

其中 $T_{\text{window}} = N \Delta t$ 为观测窗口长度。第 $h$ 次谐波对应的频点编号为：

$$k_h \approx h \cdot \frac{f_1}{f_s} N$$

其中 $f_1$ 为基波频率 (50 Hz 或 60 Hz)。当 $k_h$ 不为整数或信号频率偏离额定值时，该谐波能量泄漏到相邻频点。

### 窗函数加权

为抑制频谱泄漏，实际滤波通常引入窗函数 $w[n]$：

$$X_w[k] = \sum_{n=0}^{N-1} w[n] \cdot x[n] \cdot e^{-j 2\pi kn/N}$$

窗函数的选择体现分辨率与旁瓣抑制之间的权衡：

| 窗函数 | 主瓣宽度 | 旁瓣抑制 | 适用场景 |
|--------|----------|----------|----------|
| 矩形窗 | $2\Delta f$ | -13.3 dB | 整周期同步采样，频率分辨率优先 |
| Hann 窗 | $4\Delta f$ | -31.5 dB | 通用频谱分析，默认选择 |
| Hamming 窗 | $4\Delta f$ | -42.7 dB | 非同步采样，谐波分离 |
| Blackman 窗 | $6\Delta f$ | -58.1 dB | 精确幅值测量，高阶谐波 |

### 滑动 DFT

滑动 DFT (Sliding DFT) 通过递推更新避免全窗重算，核心递推公式为：

$$X_k[k] = X_{k-1}[k] + x[k] - x[k-N]$$

其中 $x[k]$ 为新采样点，$x[k-N]$ 为滑出窗口的最旧采样点。滑动 DFT 适合连续实时监测，但对数值漂移和频率偏移较敏感。

### 正交傅里叶滤波器 (DFT Filter Bank)

正交傅里叶滤波器提取基波正弦和余弦分量：

$$X_I = \frac{2}{N}\sum_{n=0}^{N-1} x[n]\cos\left(\frac{2\pi n}{N}\right), \quad X_Q = \frac{2}{N}\sum_{n=0}^{N-1} x[n]\sin\left(\frac{2\pi n}{N}\right)$$

基波相量表示为复数形式：

$$\underline{X}_1 = X_I - j X_Q = |X_1| e^{j\phi_1}$$

### 插值 DFT

当频率偏移导致 $k_h$ 非整数时，插值 DFT 通过相邻频点幅度修正估计误差。双谱线插值法 (Three-point interpolation) 为：

$$|X_1| = \frac{|X_{m-1}| + |X_m|}{2} \cdot \frac{2\delta}{1+\delta^2}$$

其中 $m = \lfloor k_h \rfloor$，$\delta = k_h - m$，修正频率偏移：

$$\Delta f = \frac{(|X_{m+1}| - |X_{m-1}|) \cdot (0.5 - \delta)}{2|X_m| - |X_{m-1}| - |X_{m+1}|}$$

## 分类与变体

| 方法 | 主要输出 | 适合场景 | 需要说明的前提 |
|------|----------|----------|----------------|
| 全窗口 DFT/FFT | 固定窗口频谱 | 离线 EMT 波形分析、电能质量统计 | 采样率、窗长、窗函数、频率分辨率 |
| 滑动 DFT | 随时间更新的频率分量 | 在线监测、动态相量提取 | 递推稳定性、窗口同步、频率漂移 |
| 正交傅里叶滤波器 | 基波正弦/余弦分量 | 数字保护、相量估计 | 响应时间、直流偏置、谐波抑制能力 |
| 插值 DFT | 频率偏移校正后的幅值相位 | 非同步采样、间谐波估计 | 插值假设、邻近频率干扰 |
| 线性中点插值 (NIFT 后处理) | Gibbs 振荡抑制后的时域波形 | 开关暂态仿真、频域逆变换 | $\Delta t$ 与 $f_{\max}$ 约束、插值阶数 $n$ |

## 形式化表达

### 块级公式汇总

**DFT 定义式**：

$$X[k] = \sum_{n=0}^{N-1} x[n] e^{-j 2\pi kn/N}$$

**频率映射**：

$$k_h \approx h \cdot \frac{f_1 N}{f_s}, \quad \Delta f = \frac{f_s}{N}$$

**窗函数加权 DFT**：

$$X_w[k] = \sum_{n=0}^{N-1} w[n] \cdot x[n] \cdot e^{-j 2\pi kn/N}$$

**滑动 DFT 递推**：

$$X_k[k] = X_{k-1}[k] + x[k] - x[k-N]$$

**正交滤波器基波提取**：

$$X_I = \frac{2}{N}\sum_{n=0}^{N-1} x[n]\cos\left(\frac{2\pi n}{N}\right), \quad X_Q = \frac{2}{N}\sum_{n=0}^{N-1} x[n]\sin\left(\frac{2\pi n}{N}\right)$$

**双谱线插值 DFT**：

$$|X_1| = \frac{|X_{m-1}| + |X_m|}{2} \cdot \frac{2\delta}{1+\delta^2}$$

### 行内公式汇总

- 基波相量：$\underline{X}_1 = X_I - j X_Q = |X_1| e^{j\phi_1}$
- Hann 窗：$w[n] = 0.5\left(1 - \cos\frac{2\pi n}{N}\right)$
- Blackman 窗：$w[n] = 0.42 - 0.5\cos\frac{2\pi n}{N} + 0.08\cos\frac{4\pi n}{N}$
- 矩形窗：$w[n] = 1$
- 频率分辨率：$\Delta f = 1/T_{\text{window}} = f_s/N$
- 谐波频率：$f_h = h \cdot f_1$

## 关键技术挑战

### 1. 频谱泄漏与旁瓣抑制

当信号频率偏离 DFT 整数频点时，能量从主瓣泄漏到相邻旁瓣，导致幅值估计偏差。谐波环境中各次谐波相互干扰，旁瓣重叠使估计精度恶化。解决策略：选择旁瓣抑制能力强的窗函数 (Blackman > Hamming > Hann > 矩形)；或采用相位差分技术隔离谐波。

### 2. 直流偏置与指数衰减暂态

故障初始阶段，电流中包含指数衰减的直流偏置分量 $A e^{-t/\tau}$，经 FFT 后泄漏到所有频点尤其是基波，降低相量估计精度。解决策略：全周积分法消除直流分量 $I_{\text{dc}}[n] = \frac{1}{T}\int_{t_n}^{t_n+T} i(t) dt$；或采用递推最小二乘法拟合 $A$ 和 $\tau$。

### 3. 频率漂移与同步误差

电网频率偏离标称值 50/60 Hz 时，基于固定频率参考的 DFT 滤波器产生系统性偏差。频率漂移 $\Delta f$ 导致的基波相量幅值误差为：

$$\frac{\Delta |X_1|}{|X_1|} \approx \frac{|\Delta f|}{\Delta f_{\text{resolution}}}$$

解决策略：采用频率跟踪算法 ([[phase-locked-loop]])；或使用动态更新频率参考的变步长 DFT。

### 4. 实时性与计算精度权衡

长窗口提供高频率分辨率但增加相量估计延迟，影响保护动作速度。保护用滑动 DFT 通常要求 $N \le 64$ 点 (< 1 个工频周期)，而谐波分析可用 $N \ge 256$ 点。解决策略：分级处理——保护用短窗高速通道，监测用长窗高精度通道。

### 5. 非同步采样与插值误差

当采样率 $f_s$ 不能被基波频率 $f_1$ 整除时，DFT 频点与谐波频率产生偏移。插值 DFT 的精度依赖于信噪比和邻近频率干扰强度；在谐波含量高 (< 5% THD) 场景下，双谱线插值误差可能超过 2%。

## 量化性能边界

### 各方法量化性能对比

| 方法 | 幅值误差 | 相位误差 | 计算复杂度 | 延迟 |
|------|----------|----------|-------------|------|
| 矩形窗 FFT | 0.5%~3% | 1°~5° | $O(N\log_2N)$ | 1 周期 |
| Hann 窗 FFT | 0.1%~1% | 0.5°~2° | $O(N\log_2N)$ | 1 周期 |
| 插值 DFT (双谱线) | 0.05%~0.5% | 0.2°~1° | $O(N)$ 每帧 | < 1 周期 |
| 滑动 DFT | 0.5%~2% | 1°~3° | $O(1)$ 每点 | 1 周期 |
| 正交滤波器 | 0.1%~1% | 0.5°~2° | $O(N)$ 每帧 | 1 周期 |
| 线性中点插值 (NIFT) | < 1% (vs sinc 窗) | — | $O(n \cdot N_t)$ | 后处理 |

**来源说明**：上述误差范围来自 Shi 2021 (插值 DFT 与 sinc 窗偏差 < 1%)、Rosołowski 1997 (距离继电器基波相量精度) 和 Zuluaga 2021 (QMF 滤波器组的并行计算效率)，但具体数值与测试系统 (17 母线配电网络、单导线开关暂态) 强相关，未必适用于所有 EMT 工况。

### 窗口长度与精度关系

| 窗口类型 | 点数 N | 频率分辨率 $\Delta f$ | 基波幅值误差 (典型) |
|----------|--------|------------------------|---------------------|
| 短窗 (保护用) | 32~64 | 0.78~1.56 Hz | 2%~5% |
| 标准窗 | 64~128 | 0.39~0.78 Hz | 0.5%~2% |
| 长窗 (谐波分析) | 256~1024 | 0.05~0.20 Hz | 0.1%~0.5% |

### 频率偏移敏感性

当电网频率偏移 +0.5 Hz (从 50 Hz 到 50.5 Hz)：
- 矩形窗 FFT 基波幅值误差：约 2.3%
- Hann 窗 FFT 基波幅值误差：约 0.8%
- 插值 DFT 校正后误差：< 0.2%

## 适用边界与选择指南

### 方法选择决策表

| 应用场景 | 推荐方法 | 窗口长度 | 关键参数 |
|----------|----------|----------|----------|
| 继电保护基波相量 | 正交滤波器 + 直流偏置抑制 | 64 点 | 递推更新频率 |
| 谐波分析 (THD 计算) | Hann 窗 FFT | 256~1024 点 | 窗函数类型、频率分辨率 |
| 非同步采样波形 | 双谱线插值 DFT | 128~256 点 | $\delta$ 插值因子 |
| 实时动态相量提取 | 滑动 DFT | 64 点 | 递推稳定性 |
| 开关暂态 Gibbs 抑制 | 线性中点插值 | NIFT 后处理 | $n$ 加权阶数、$K$ 偏移步数 |
| 大规模并行 EMT 加速 | QMF 滤波器组 | 变步长 | 并行通道数、$\omega_{\max}$ |

### 失效场景

- **傅里叶滤波默认窗口内信号接近平稳**：故障初始阶段 (< 5 ms)、换相失败和保护动作期间，频谱随时间快速变化，固定窗口结果只能解释为该窗口内的平均频率内容，不能用于瞬时值估计。
- **频率分辨率与响应速度矛盾**：$\Delta f = f_s/N$，提高分辨率（增大 $N$）意味着更长窗口和更慢响应，保护快速性要求限制了可达精度。
- **强噪声环境**：信噪比 < 20 dB 时，插值 DFT 的误差可能超过 5%，需结合数字滤波预处理 ([[filtering]])。
- **间谐波密集场景**：多间谐波 (如 100~200 Hz) 环境下，窗函数旁瓣相互覆盖，幅值分离精度严重下降，需要高阶数谱估计方法 ([[prony-analysis]]、[[modal-analysis]])。

## 相关方法 / 相关模型 / 相关主题

- [[fft]] — 常用实现算法，计算 $O(N \log_2 N)$ 的 FFT 核
- [[fourier-series]] — 周期信号分解概念，本页关注采样数据上的提取和滤波
- [[filtering]] — 数字滤波基础（低通/高通/带通/陷波），与窗函数选择密切相关
- [[harmonic-analysis]] — 谐波分析中傅里叶滤波用于提取各次谐波含量
- [[dynamic-phasor]] — 动态相量提取中滑动 DFT 用于生成时变相量
- [[phasor-measurement-unit]] — PMU 中的相量估计算法依赖正交傅里叶滤波器
- [[impedance-measurement]] — 频率扫描中傅里叶滤波用于获得阻抗频率响应
- [[prony-analysis]] — 高分辨率谱估计，用于间谐波和振荡模态分析
- [[modal-analysis]] — 模态分析中傅里叶滤波辅助提取振荡频率和阻尼比
- [[passivity-enforcement]] — 频域建模中的频率响应数据可由傅里叶滤波后处理得到
- [[vector-fitting]] — 矢量拟合用于有理函数逼近频域响应，不等同于简单波形滤波
- [[digital-distance-protection]] — 距离保护判据中基波相量估计依赖正交傅里叶滤波器
- [[relay-protection]] — 继电保护整体框架，使用傅里叶滤波提取的相量作为输入

## 来源论文

- [[a-study-on-interpolation-and-weighting-function-for-numerical-fourier-transform]] — Shi 2021，数值傅里叶逆变换中 Gibbs 振荡的时域后处理抑制方法，线性中点插值等效于余弦窗函数 $[G_{\cos}(\omega)]^n$，< 1% 幅值偏差，$n$ 阶迭代插值控制平滑程度
- [[a-new-distance-relaying-algorithm-based-on-complex-differential-equation-for-sym]] — Rosołowski 1997，基于复数微分方程的距离保护新算法，使用傅里叶滤波器提取基波阻抗，用于对称分量计算
- [[parallel-computation-of-power-system-emts-through-polyphase-qmf-filter-banks]] — Zuluaga 2021，多相 QMF 滤波器组用于 EMT 并行计算，Kron 降阶后通过滤波器组实现卷积并行化，> 100 倍实时仿真速度
- [[stability-evaluation-of-interpolation-extrapolation-and-numerical-oscillation-da]] — 插值外推法的数值振荡稳定性评估，与傅里叶滤波的窗函数选择存在技术关联
- [[assessment-of-dynamic-phasor-extraction-methods-for-power-system-co-simulation-a]] — Rupasinghe 2021，动态相量提取方法比较，滑动 DFT 与正交滤波器的对比评估
- [[a-multi-domain-co-simulation-method-for-comprehensive-shifted-frequency-phasor-d]] — Shu 2019，多域混合仿真中移频相量与 EMT 接口，傅里叶滤波用于域间信号同步