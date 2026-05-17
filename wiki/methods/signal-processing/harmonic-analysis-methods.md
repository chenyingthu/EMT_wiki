---
title: "谐波分析方法 (Harmonic Analysis Methods)"
type: method
tags: [harmonic-analysis, fft, frequency-domain, thd, power-quality, spectrum]
created: "2026-05-04"
updated: "2026-05-18"
---

# 谐波分析方法 (Harmonic Analysis Methods)

## 定义与边界

谐波分析方法是在 EMT 波形或频域网络模型中识别、计算和解释基波整数倍频率分量的方法集合。典型输入是电压电流时域采样、频率扫描得到的端口阻抗、换流器或非线性负荷的谐波注入模型、窗口长度和基频估计；输出包括各次谐波幅值与相位、THD/TDD、谐波阻抗、谐振频点、滤波器应力和波形畸变指标。

本页关注"如何分析谐波"的方法边界，不替代 [[harmonic-analysis]] 的主题综述，也不替代 [[fft]]|[[fourier-series]]|[[frequency-scan]] 或 [[impedance-measurement]] 的具体算法页。谐波分析也不等同于全部宽频暂态分析：开关暂态、雷电、VFTO 和超谐波通常还需要 [[wideband-modeling]] 与频率相关模型。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 420" xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="10" width="880" height="70" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="450" y="35" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e40af">谐波分析EMT仿真输入</text>
  <text x="450" y="58" text-anchor="middle" font-size="12" fill="#374151">电压/电流时域采样 · 频率扫描端口阻抗 · 谐波源注入模型 · 窗口长度与基频</text>
  <line x1="450" y1="80" x2="450" y2="105" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#333"/></marker></defs>
  <rect x="10" y="110" width="165" height="160" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="92" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="#166534">FFT/DFT后处理</text>
  <text x="92" y="155" text-anchor="middle" font-size="10" fill="#374151">时域采样→频谱</text>
  <text x="92" y="172" text-anchor="middle" font-size="10" fill="#374151">窗口/基频估计</text>
  <text x="92" y="195" text-anchor="middle" font-size="10" fill="#166534">谱泄漏·非平稳</text>
  <text x="92" y="212" text-anchor="middle" font-size="10" fill="#166534">采样同步影响</text>
  <text x="92" y="235" text-anchor="middle" font-size="10" fill="#6b7280">THD/幅值/相位</text>
  <rect x="185" y="110" width="165" height="160" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="267" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="#166534">频域谐波潮流</text>
  <text x="267" y="155" text-anchor="middle" font-size="10" fill="#374151">谐波源模型</text>
  <text x="267" y="172" text-anchor="middle" font-size="10" fill="#374151">线性网络导纳</text>
  <text x="267" y="195" text-anchor="middle" font-size="10" fill="#166534">强非线性需迭代</text>
  <text x="267" y="212" text-anchor="middle" font-size="10" fill="#166534">时变控制降级</text>
  <text x="267" y="235" text-anchor="middle" font-size="10" fill="#6b7280">Y(h)V(h)=I(h)</text>
  <rect x="360" y="110" width="165" height="160" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="442" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="#166534">谐波阻抗扫描</text>
  <text x="442" y="155" text-anchor="middle" font-size="10" fill="#374151">注入扰动信号</text>
  <text x="442" y="172" text-anchor="middle" font-size="10" fill="#374151">端口响应测量</text>
  <text x="442" y="195" text-anchor="middle" font-size="10" fill="#166534">测点/扰动幅值</text>
  <text x="442" y="212" text-anchor="middle" font-size="10" fill="#166534">控制状态敏感</text>
  <text x="442" y="235" text-anchor="middle" font-size="10" fill="#6b7280">Z(jω)=V/I</text>
  <rect x="535" y="110" width="165" height="160" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="617" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="#166534">动态相量/谐波相量</text>
  <text x="617" y="155" text-anchor="middle" font-size="10" fill="#374151">保留频率集合</text>
  <text x="617" y="172" text-anchor="middle" font-size="10" fill="#374151">状态方程</text>
  <text x="617" y="195" text-anchor="middle" font-size="10" fill="#166534">谐波截断误差</text>
  <text x="617" y="212" text-anchor="middle" font-size="10" fill="#166534">慢变系数建模</text>
  <text x="617" y="235" text-anchor="middle" font-size="10" fill="#6b7280">时变傅里叶系数</text>
  <rect x="710" y="110" width="180" height="160" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="800" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="#166534">宽频有理模型</text>
  <text x="800" y="155" text-anchor="middle" font-size="10" fill="#374151">频域响应采样</text>
  <text x="800" y="172" text-anchor="middle" font-size="10" fill="#374151">矢量拟合等效</text>
  <text x="800" y="195" text-anchor="middle" font-size="10" fill="#166534">需无源性验证</text>
  <text x="800" y="212" text-anchor="middle" font-size="10" fill="#166534">频带/阶数约束</text>
  <text x="800" y="235" text-anchor="middle" font-size="10" fill="#6b7280">R(s)有理函数</text>
  <line x1="450" y1="270" x2="450" y2="295" stroke="#333" stroke-width="2" marker-end="url(#arrow2)"/>
  <defs><marker id="arrow2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#333"/></marker></defs>
  <rect x="10" y="300" width="880" height="110" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="450" y="325" text-anchor="middle" font-size="14" font-weight="bold" fill="#4c1d95">谐波分析输出与指标</text>
  <text x="130" y="350" text-anchor="middle" font-size="11" font-weight="bold" fill="#5b21b6">畸变指标</text>
  <text x="130" y="368" text-anchor="middle" font-size="10" fill="#374151">THD</text>
  <text x="130" y="383" text-anchor="middle" font-size="10" fill="#374151">TDD</text>
  <text x="130" y="398" text-anchor="middle" font-size="10" fill="#374151">K-factor</text>
  <line x1="260" y1="338" x2="260" y2="400" stroke="#7c3aed" stroke-width="1"/>
  <text x="400" y="350" text-anchor="middle" font-size="11" font-weight="bold" fill="#5b21b6">谐波阻抗与谐振</text>
  <text x="400" y="368" text-anchor="middle" font-size="10" fill="#374151">端口阻抗 Z(jω)</text>
  <text x="400" y="383" text-anchor="middle" font-size="10" fill="#374151">谐振频点识别</text>
  <text x="400" y="398" text-anchor="middle" font-size="10" fill="#374151">滤波器应力</text>
  <line x1="540" y1="338" x2="540" y2="400" stroke="#7c3aed" stroke-width="1"/>
  <text x="720" y="350" text-anchor="middle" font-size="11" font-weight="bold" fill="#5b21b6">波形与频谱</text>
  <text x="720" y="368" text-anchor="middle" font-size="10" fill="#374151">各次谐波幅值/相位</text>
  <text x="720" y="383" text-anchor="middle" font-size="10" fill="#374151">间谐波/次谐波</text>
  <text x="720" y="398" text-anchor="middle" font-size="10" fill="#374151">谐波功率分布</text>
  <text x="10" y="420" font-size="10" fill="#6b7280">图1 · 谐波分析方法体系：输入 → 5类方法 → 量化输出指标</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 谐波分析方法体系架构：输入 → 五类分析路线 → 量化输出指标</p>

## EMT 中的作用

EMT 可直接产生非正弦瞬时波形，因此谐波分析常作为后处理或频域接口：

- 从详细开关模型、平均值模型和谐波保留模型的输出中比较频谱差异
- 识别变压器饱和、电弧炉、LCC、VSC、MMC 或单相整流负荷产生的主要频率分量
- 结合 [[frequency-scan]] 或 [[impedance-measurement]] 判断电缆、滤波器、变压器和外部网络是否存在谐振风险
- 为滤波器设计、电能质量评估和保护误动分析提供证据

这些用途都需要把指标绑定到测量窗口、基频、采样率、窗函数、谐波阶数上限和被分析工况。没有这些条件的 THD、谐波电流百分比或"满足标准"说法应降级或删除。

## 核心机制

周期稳态波形可写成傅里叶级数：

$$v(t)=V_0+\sum_{h=1}^{H}V_h\sin(h\omega_1 t+\phi_h)$$

其中 $h$ 是谐波次数，$\omega_1$ 是基波角频率，$V_h$ 和 $\phi_h$ 分别是第 $h$ 次谐波幅值和相角。对离散 EMT 波形，常用 [[fft]] 或同步 DFT 在有限窗口内估计这些量；频率分辨率由窗口长度决定，非整周期截断会导致谱泄漏。

频域谐波潮流或阻抗分析常写为：

$$Y(h)\mathbf{V}(h)=\mathbf{I}(h)$$

其中 $Y(h)$ 是第 $h$ 次谐波导纳矩阵，$\mathbf{V}(h)$ 是节点电压相量，$\mathbf{I}(h)$ 是谐波注入。该表达假设每个频率点可近似线性求解；若非线性设备导致谐波间耦合，就需要迭代谐波潮流、动态相量或直接 EMT 时域仿真。

谐波阻抗扫描可用注入量和响应量估计：

$$Z(j\omega)=\frac{V(j\omega)}{I(j\omega)}$$

该比值只有在注入幅值、测点、背景谐波和控制器工作状态受控时才可解释为端口阻抗。

## 分类与变体

| 路线 | 输入 | 输出 | 主要边界 |
|------|------|------|----------|
| FFT/DFT 后处理 | EMT 时域采样、窗口和基频 | 谐波幅值、相位、THD | 受谱泄漏、非平稳和采样同步影响 |
| 频域谐波潮流 | 谐波源模型、线性网络导纳 | 节点谐波电压和电流 | 对强非线性和时变控制需迭代或降级 |
| 谐波阻抗扫描 | 注入信号、端口响应 | 阻抗曲线和谐振频点 | 测量点、扰动幅值和控制状态敏感 |
| 动态相量/谐波相量 | 保留的频率集合、状态方程 | 慢变谐波系数 | 谐波截断会遗漏未建模频率 |
| 宽频有理模型 | 频域响应采样 | 可时域实现的阻抗/导纳模型 | 需要 [[vector-fitting]] 和 [[passivity-enforcement]] 验证 |

### EMT 建模中的五条分析路线

**路线1：FFT/DFT 后处理**——最常用的时域波形分析方法。将 EMT 输出的电压电流时域采样序列通过快速傅里叶变换（FFT）或离散傅里叶变换（DFT）投影到频域。关键参数是窗口长度 $N$（或等效频率分辨率 $\Delta f = f_s/N$）和窗函数选择。对于非同步采样，谱泄漏会导致谐波幅值估计误差，需使用汉宁窗、汉明窗或布莱克曼窗抑制旁瓣。傅里叶滤波在半周期窗口（10 ms，50 Hz）下仍能有效抑制直流分量与3次以上谐波，幅值误差 < 2%（据 Rosołowski 1997 距离保护算法验证）。

**路线2：频域谐波潮流**——将谐波源建模为注入电流 $\mathbf{I}_h$，结合网络导纳矩阵 $Y(h)$ 求解 $\mathbf{V}_h = Y^{-1}(h)\mathbf{I}_h$。适用于线性或准线性网络，但对于变压器饱和产生的3、5、7次谐波，需要在迭代中更新饱和等效阻抗。Perkins 等提出的平衡谐波潮流（HPF）在时域框架中结合功率约束，解决了频率域方法无法处理特征谐波截断误差的问题。

**路线3：谐波阻抗扫描**——通过在端口注入宽频扰动信号（PRBS、阶跃或白噪声），测量端口的电压电流响应并计算阻抗频率响应 $Z(j\omega)$。对于多馈入直流系统，故障期间远端母线 $h$ 次谐波电压传递系数幅值稳定在 0.35～0.62 区间（据 Yao 等 2023 多馈入谐波交互研究），该系数与网络拓扑和频率相关阻抗密切相关。

**路线4：动态相量/谐波相量**——利用时变傅里叶级数系数表示保留的频率分量，将时域微分方程转换为谐波系数的状态方程。SVC 的 TCR 动态相量模型保留基波与5次谐波，可将仿真步长从约 50 μs 提升至 0.5～1 ms。该方法在机电-电磁混合仿真中用于接口处理。

**路线5：宽频有理模型**——在宽频范围（DC～10 kHz 甚至 MHz）采样网络阻抗或导纳响应，通过 [[vector-fitting]] 拟合为有理函数 $R(s)=\sum_{k=1}^{N}\frac{r_k}{s-p_k}$，再经 [[passivity-enforcement]] 确保无源性约束。矢量拟合精度取决于频带覆盖、阶数选择和无源性优化。

## 形式化表达补充

### 总谐波畸变率（THD）

电压 THD 定义：

$$\text{THD}_V=\frac{\sqrt{\sum_{h=2}^{H}V_h^2}}{V_1}\times 100\%$$

电流 THD 定义：

$$\text{THD}_I=\frac{\sqrt{\sum_{h=2}^{H}I_h^2}}{I_1}\times 100\%$$

其中 $V_1$、$I_1$ 为基波幅值，$H$ 为考虑的最高谐波次数。

### 总需求畸变率（TDD）

$$\text{TDD}_I=\frac{\sqrt{\sum_{h=2}^{H}I_h^2}}{I_L}\times 100\%$$

其中 $I_L$ 为额定负载电流。

### 谐波功率

第 $h$ 次谐波功率：

$$P_h=V_h I_h\cos(\phi_h)$$

总谐波功率（通常近似为零）：

$$P_H=\sum_{h=2}^{H}P_h$$

### 谐波阻抗矩阵

多导体系统谐波阻抗：

$$\mathbf{V}_h=\mathbf{Z}_h\mathbf{I}_h$$

其中 $\mathbf{Z}_h$ 为第 $h$ 次谐波阻抗矩阵。

### FFT 频率分辨率

频率分辨率：

$$\Delta f=\frac{f_s}{N}=\frac{1}{T_{\text{window}}}$$

其中 $f_s$ 为采样频率，$N$ 为采样点数，$T_{\text{window}}$ 为窗口长度。

### 窗函数频谱泄漏抑制

汉宁窗：

$$w(n)=0.5-0.5\cos\left(\frac{2\pi n}{N-1}\right)$$

汉明窗：

$$w(n)=0.54-0.46\cos\left(\frac{2\pi n}{N-1}\right)$$

布莱克曼窗：

$$w(n)=0.42-0.5\cos\left(\frac{2\pi n}{N-1}\right)+0.08\cos\left(\frac{4\pi n}{N-1}\right)$$

### 多馈入谐波传递系数（量化边界）

据 Yao 等 2023 多馈入 HVDC 系统研究，谐波电压传递系数为：

$$K_h=\frac{\dot{U}_{2h}}{\dot{U}_{1h}}$$

量化边界：远端母线 $h$ 次谐波电压传递系数幅值稳定在 **0.35～0.62 区间**；THD 每增加 1%，换相电压过零点偏移角 $\phi$ 平均增加约 **0.18°**；计及谐波后逆变器关断角 $\gamma'$ 平均减小 **2.8°～4.5°**，并发换相失败（CCF）发生概率提升约 **35%**。

### 谐波间耦合

非线性设备引起的谐波耦合：

$$I_h=f(V_1,V_2,\ldots,V_H,\theta_1,\theta_2,\ldots,\theta_H)$$

调制产生的边带频率：

$$f_{\text{side}}=|h_1 f_1\pm h_2 f_2|$$

间谐波频率：

$$f_{\text{inter}}=h f_1\pm\Delta f$$

次谐波频率：

$$f_{\text{sub}}=\frac{f_1}{h},\quad h=2,3,\ldots$$

## 适用边界与失败模式

- 稳态 THD 不代表暂态期间的频谱；故障、投切和控制限幅期间应使用滑动窗口或时频方法，并报告窗口参数
- 谐波标准限值属于工程合规语境；除非页面引用了具体标准版本、电压等级和测量定义，否则不应给固定限值表
- "主要谐波"取决于拓扑、调制、控制、滤波器和运行点；不应把六脉动或十二脉动特征谐波外推到所有换流器
- FFT 幅值精度受采样同步、窗函数和基频漂移影响；用频谱解释保护误动时还要考虑互感器带宽和滤波链路
- 频域线性叠加不能充分描述磁饱和、电弧、限流控制和开关饱和引起的谐波间耦合

### 典型谐波源特征

| 谐波源 | 主要特征谐波 | 幅值规律 | 相位特征 |
|--------|--------------|----------|----------|
| 六脉动整流 | 5, 7, 11, 13... | $1/h$ | 反对称 |
| 十二脉动整流 | 11, 13, 23, 25... | $1/h$ | 多组相位差 30° |
| PWM 逆变器 | 载波频率附近 | 与调制比相关 | 取决于载波相位 |
| 变压器饱和 | 3, 5, 7... | 与剩磁相关 | 零序3次谐波 |
| 电弧炉 | 2, 3, 4, 5... | 随机分布 | 时变非平稳 |
| 荧光灯 | 3, 5, 7, 9... | 较大3次 | 三相不平衡 |

### 量化性能边界

| 指标 | 数值 | 来源 |
|------|------|------|
| 谐波电压传递系数（MI-HVDC） | 0.35～0.62 | Yao 等 2023 |
| 关断角修正量（谐波后） | −2.8°～−4.5° | Yao 等 2023 |
| CCF 概率提升 | +35% | Yao 等 2023 |
| 等效模型 vs EMT 计算误差 | <3.5% | Yao 等 2023 |
| 等效模型计算加速比 | ~40× | Yao 等 2023 |
| 半周期 FFT 幅值误差 | <2% | Rosołowski 1997 |
| PRBS 阻抗扫描频率分辨率 | 取决于 PRBS 长度 | Cifuentes 2026 |

## 与相关页面的关系

- [[fft]] 说明离散频谱计算；本页说明 FFT 结果在谐波分析中的使用边界
- [[frequency-scan]] 和 [[impedance-measurement]] 提供谐波阻抗与谐振识别的输入
- [[harmonic-transfer-coefficient]] 和 [[harmonic-interaction]] 关注谐波传播与交互机理
- [[magnetic-saturation-modeling]]|[[lcc-model]]|[[vsc-model]] 和 [[mmc-model]] 是常见谐波来源或调制对象
- [[frequency-dependent-modeling]]|[[wideband-modeling]] 和 [[passivity-enforcement]] 决定宽频阻抗模型能否可靠进入 EMT
- [[fourier-filtering]] 详细阐述窗函数选择和频谱校正方法

## 来源论文

| 论文 | 年份 | 贡献说明 |
|------|------|----------|
| [[a-time-domain-harmonic-power-flow-algorithm]] | 2010 | 时域谐波潮流结合功率约束，解决频率域截断误差问题 |
| [[harmonic-preserved-average-value-model-for-converters-in-electromagnetic-transie]] | 2026 | 提出 HP-AVM，将平均值模型与谐波计算统一到同一仿真框架 |
| [[harmonics-interaction-mechanism-and-impact-on-extinction-angles-in-multi-infeed-]] | 2023 | 多馈入系统谐波传递等效电路，关断角修正，CCF 风险量化 |
| [[analysis-of-frequency-dependent-network-equivalents-in-dynamic-harmonic-domain]] | 2021 | 频率相关网络等值在动态谐波域中的应用与验证 |
| [[an-inverter-model-simulating-accurate-harmonics-with-low-computational-burden-fo]] | 202X | 时间平均法（TAM）推广到梯形积分，5倍步长扩展，3×加速 |
| [[analysis-on-non-characteristic-harmonic-circulating-current-in-parallel-inverter]] | 2016 | 并联变流器非特征次谐波环流分析，500 kV 实例 |
| [[a-harmonic-phasor-domain-co-simulation-method-and-new-insight-for-harmonic-analy]] | 2021 | 谐波相量域协同仿真方法，大规模 VSC-HVDC 系统谐波分析 |
| [[development-of-high-frequency-supraharmonic-models-of-small-scale-amplt5kw-singl]] | 202X | 小功率逆变器高频超谐波建模（2～150 kHz） |
| [[flexible-extended-harmonic-domain-approach-for-transient-state-analysis-of-switc]] | 202X | 灵活扩展谐波域方法，开关暂态分析 |
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model]] | 2009 | SVC 动态相量混合仿真，基波+5次谐波保留 |