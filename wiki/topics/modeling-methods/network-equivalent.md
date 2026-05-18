---
title: "网络等值 (Network Equivalent)"
type: topic
tags: [network-equivalent, thevenin, ward, fdne, reduction]
created: "2026-04-13"
updated: "2026-05-18"
---

# 网络等值 (Network Equivalent)

## 定义

网络等值（Network Equivalent）是将大规模电力系统外部网络压缩为等效模型的核心技术：在保持端口电气特性（阻抗/导纳/响应）不变的前提下，用紧凑等效电路替代完整网络，将 $N$ 节点外部系统的计算复杂度从 $O(N^3)$ 降至 $O(1)$，从而使大规模电网的 EMT 仿真成为可能。

在 EMT 仿真中，网络等值不是简单删除节点，而是把外部网络替换为可接入 [[emtp|EMTP]] 或 [[pscad-emtdc|PSCAD/EMTDC]] 的等效模型。按接口性质分为三类：

| 等值类型 | 端口特性 | 典型频段 | EMT 建模复杂度 |
|---------|---------|---------|--------------|
| 稳态等值（Ward/REI） | 纯工频阻抗 | 50/60 Hz | $O(1)$ |
| 频变等值（FDNE） | 宽频导纳矩阵 | 0.1 Hz–10 kHz | $O(n_p \cdot N^2)$ |
| 动态等值 | 时域状态空间 | 全频段 | $O(n_s)$ |

## EMT 中的角色

网络等值在 EMT 仿真中有两个核心使命：

**使命一：接口等值** — 大规模交直流电网通常只有局部区域需要详细 EMT 建模（如 HVDC 换流站、FACTS 控制器、故障点附近网络），外部网络用等值模型替代。接口处若用纯工频等值，则无法反映高频谐波相互作用；若用详细模型，则计算代价过高。FDNE 在精度与效率之间提供了可调节的平衡。

**使命二：网络压缩** — 实时仿真（[[rtds|RTDS]]、FPGA）的计算资源极为有限，401 电平 MMC 的全详细模型在 RTDS 上不可行，必须用等值模型将状态变量数从 $O(N)$ 压缩至 $O(1)$。

核心挑战：等值模型必须同时满足 **宽频保真**（从基波到数十 kHz 的阻抗特性）、**数值稳定**（无源性保证）和 **计算可行**（实时步长内完成求解）。

## 形式化表达

### 频变网络等值（FDNE）有理函数模型

FDNE 的核心是将端口导纳矩阵 $\mathbf{Y}(s)$ 拟合为有理函数形式：

$$\mathbf{Y}(s) \approx \mathbf{Y}_{\mathrm{fit}}(s) = \mathbf{D} + s\mathbf{E} + \sum_{m=1}^{N_p} \frac{\mathbf{R}_m}{s - p_m}$$

其中 $p_m$ 为公共极点（所有矩阵元素共享），$\mathbf{R}_m$ 为留数矩阵，$N_p$ 为模型阶数。公共极点策略显著降低时域实现计算量——极点重定位只需执行一次，而非对每个矩阵元素独立迭代。

### 多端口戴维南等值接口方程

多区域等值（MATE）框架下的端口等值电压源与阻抗计算：

$$\mathbf{e}_{\mathrm{th},k}(t) = \mathbf{M}_k^T [\mathbf{Y}_k]^{-1} \mathbf{i}_{hk}(t - \Delta T), \quad \mathbf{Z}_{\mathrm{th},k} = \mathbf{M}_k^T [\mathbf{Y}_k]^{-1} \mathbf{M}_k$$

接口变量通过线性插值实现跨步长同步：

$$\bar{u}_k(t) = \mathcal{L}\{u_k[(k-1)\Delta T], u_k[(k-2)\Delta T]\}, \quad \bar{i}_k(t) = \mathcal{L}\{i_k[(k-1)\Delta T], i_k[(k-2)\Delta T]\}$$

### 无源性判定条件

FDNE 必须满足无源性以保证时域仿真数值稳定：

$$\lambda_{\min}\left(\mathrm{Re}[\mathbf{Y}(j\omega)]\right) \geq 0, \quad \forall\omega$$

半尺寸无源性测试矩阵的扰动修正：

$$\mathbf{G}(\omega) + \mathbf{G}^H(\omega) \geq 0, \quad \mathbf{G}(j\omega) = \mathrm{Re}[\mathbf{Y}(j\omega)]$$

### 双层 FDNE 合成公式（Shu 2019）

$$Y_{T\text{-FDNE}}(s) = Y_{\mathrm{detailed}}(s) + Y_{\mathrm{equivalent}}(s) + Y_{\mathrm{comp}}(s)$$

其中补偿项 $Y_{\mathrm{comp}}(s)$ 仅在破坏频段添加辅助极点-留数对，不改变原模型主体频响。

### Brune 网络综合基本步骤

Brune 循环将阻抗矩阵递归分解为物理元件组合：

$$R_{\min} = \min_{\omega}\left\{\frac{|\mathrm{Re}\{Z_2(j\omega)\}|}{\Delta_{11}(\omega)}\right\}$$

$$L_3 = -\frac{L_1 L_2}{(t_1 \cdot t_2)^2 L_1 + L_2}$$

## EMT 建模方法

### 方法 A：矢量拟合（Vector Fitting）— 公共极点策略

矢量拟合是 FDNE 的主流工业方法。采用"先拟合矩阵元素总和以提取公共极点，再逐元素拟合留数"的策略：

$$\mathbf{Y}(s) = \sum_{k=1}^{N_p} \frac{\mathbf{C}_k}{s - a_k} + \mathbf{D} + s\mathbf{E}$$

**步骤**：
1. 频域扫描：在边界端口施加宽频扰动，获取 $Y(j\omega_k)$ 样本
2. 总和拟合：对所有元素的频率响应求和，拟合获取公共极点 $\{a_k\}$
3. 逐元留数拟合：固定公共极点，对每个矩阵元素独立求留数 $\mathbf{C}_k$
4. 无源性检测：构造半尺寸测试矩阵，定位违规频段
5. 参数扰动修正：对极点/留数施加最小扰动消除非无源极点

Zhang 等（2012）在 IEEE 39 节点系统中验证，1–2 kHz 频段拟合误差 $<1\%$，无源性修正引入的附加误差 $<0.5\%$。

### 方法 B：Loewner 矩阵方法（Gurrala 2015）— 非迭代有理逼近

Loewner 矩阵方法直接从频响采样数据构造状态空间模型，无需初始极点猜测：

$$\mathbb{L}_{ij} = \frac{v_j r_i - l_j w_i}{\mu_j - \lambda_i}$$

$$H(\lambda_i) r_i = w_i, \quad l_j H(\mu_j) = v_j$$

广义描述符状态空间：

$$E\dot{x}(t) = Ax(t) + Bu(t), \quad y(t) = Cx(t) + Du(t) + Y_\infty \dot{u}(t)$$

**关键优势**：非迭代特性彻底消除收敛问题；SVD 奇异值谱自动指示最优阶数。Gurrala 2015 给出全频段导纳矩阵拟合相对误差 $<0.8\%$，建模计算时间较 VF 减少 $30\%$–$50\%$。

### 方法 C：Brune-Tellegen 网络综合（Ahmadi 2021）— 拓扑保证无源性

Brune-Tellegen 网络综合直接从频域阻抗表格 $Z(j\omega_k)$ 综合 RLCM 无源网络：

$$Z(s) = K_{\infty p}s + \frac{K_{0p}}{s} + \sum_{j_p=1}^{n_p} K_{j_p}\frac{2s}{s^2 + \omega_{j_p}^2} + Z_1(s)$$

**四步递归循环**：
1. 移除虚轴极点（$s=0,\infty$, 有限谐振频率）$\rightarrow$ 串联电容/电感/LC 谐振支路
2. 求逆后在导纳域移除虚轴零点 $\rightarrow$ 并联元件
3. 提取最小实部电阻 $R_{\min}$，使剩余阻抗在 $\omega_0$ 处秩亏
4. 执行 Tellegen-Brune 循环：构造秩一矩阵提取串联电感、耦合电感与理想变压器

**核心价值**：无源性由物理 RLCM 拓扑内禀保证，无需后处理校正。Ahmadi 2021 在 230 kV 三相输电系统（9 母线 11 回线）中，综合生成 80 个 RLCM 模块，计算速度提升 3.3 倍（640 ms $\rightarrow$ 194 ms，步长 20 μs）。

### 方法 D：双层 FDNE + 局部无源性补偿（Shu 2019）

双层结构将详细层（扰动测试获取导纳）与等值层（解析法推导导纳）分离：

$$Y_{\mathrm{comp}}(s) = \sum_{m=1}^{M} \frac{\Delta R_m}{s - \Delta p_m}$$

仅在检测到的破坏频段添加 2–4 阶辅助极点，避免全局参数重优化。Shu 2019 给出量化数据：
- 模型构建时间：0.1–0.2 秒（较全局优化缩短 200 倍）
- 接口电压/电流动态误差：$<1.2\%$
- 高频段（$>$1 kHz）幅频响应偏差：$<0.5$ dB
- 时域仿真发散率：$18.7\% \rightarrow 0\%$

### 方法 E：多区域戴维南等值（MATE）多速率协同仿真（Li 2019）

MATE 将大规模交直流网络按弱耦合边界分区，各交流子系统等值为戴维南接口：

$$\begin{bmatrix} \mathbf{Y}_1 & & \mathbf{M}_1 \\ & \ddots & \vdots \\ & & \mathbf{Y}_N & \mathbf{M}_N \\ \mathbf{M}_1^T & \cdots & \mathbf{M}_N^T & \mathbf{Z}_b \end{bmatrix} \begin{bmatrix} v_1(t) \\ \vdots \\ v_N(t) \\ i_b(t) \end{bmatrix} = \begin{bmatrix} i_{h1}(t-\Delta T) \\ \vdots \\ i_{hN}(t-\Delta T) \\ 0 \end{bmatrix}$$

多速率接口：直流侧 $\Delta t = 50\,\mu$s，交流侧 $\Delta T = n\Delta t$（$n=10$ 时 $\Delta T = 500\,\mu$s）。在中国南方电网观音岩 LCC-HVDC 工程（2412 母线 / 599 发电机 / 3537 线路）验证：
- 加速比：150–160 倍
- 接口变量平均误差：$0.0084$–$0.0116$
- 直流子系统误差：$<0.012$

## 量化性能边界

| 方法 | 精度 | 效率 | 无源性 | 适用场景 |
|------|------|------|--------|---------|
| 矢量拟合（公共极点） | 误差 $<1\%$（1–2 kHz） | 中等 | 需后处理强制 | 通用 FDNE 建模，工业标准 |
| Loewner 矩阵 | 误差 $<0.8\%$ | 较 VF 快 30–50% | 天然保持 | 非迭代场景，阶数自动辨识 |
| Brune-Tellegen 综合 | 频域精确匹配 | 3.3× 加速（vs 详细模型） | 拓扑内禀保证 | 高稳定性要求的接口等值 |
| 双层 FDNE + 局部补偿 | 误差 $<1.2\%$ | 建模时间 0.1–0.2 s | 局部补偿，100% 收敛 | MMC 并网混合仿真，实时需求 |
| MATE 多速率协同 | 接口误差 $<0.012$ | 150–160× 加速 | 子系统独立保证 | 大规模交直流混合仿真 |

| 关键参数 | 数值 |
|---------|------|
| 频率覆盖范围 | 0.1 Hz – 10 kHz（Shu）/ 1–2 kHz（Zhang）/ 直至 MHz（接地系统） |
| 典型极点阶数 | 15–30 阶（依网络规模自适应） |
| 无源性判定阈值 | 实部矩阵最小特征值 $< -1\times10^{-4}$ |
| EMT 仿真步长 | 20–50 μs（实时）/ 100–500 μs（多速率协同） |

## 关键技术挑战

### 挑战 1：非线性与时变系统

现有 FDNE 基于线性时不变假设。对于含饱和特性（变压器、CVT）的系统，需结合状态方程离散化与导纳互差法，但模型阶数与计算复杂度显著增加。**应对方向**：采用分段线性化或在饱和元件端口局部保留非线性。

### 挑战 2：端口规模可扩展性

当系统中存在数千个电力电子变换器时，接口母线数目随端口规模平方增长，等值导纳矩阵维数过高。**应对方向**：基于 SVD 压缩截断（如 $r < (N+1)/2$ 时，计算量从 $2N^2+2N$ 降至 $4rN$，降幅超过 50%；Y4 案例中计算量从 3900 降至 3276）。

### 挑战 3：数值稳定性与实时约束

大规模端口系统的 FDNE 实时计算面临双重约束：留数矩阵满秩时 10 端口以上即触发现实时阈值；诺顿等效的历史电流源递归更新随端口数平方增长。**应对方向**：采用分布参数长传输线实现子网弱耦合分割，或基于诺顿/戴维南等值实现电气孤岛解耦。

### 挑战 4：宽频无源性保证

矢量拟合后的无源性强制修正在某些频段可能破坏原拟合精度，尤其是高阶模型。**应对方向**：局部无源性补偿（Shu 2019）仅在问题频段添加辅助极点，不做全局重优化；Brune 综合（Ahmadi 2021）从拓扑层面内禀保证无源性。

### 挑战 5：初始化与稳态一致性

FDNE 的初始状态必须与外部网络稳态潮流一致，否则会导致仿真起步震荡。**应对方向**：打靶法初始化（将 AVM 模型状态变量从 $O(N)$ 降至 $O(1)$）或基于戴维南等值预设端口电压初值。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 520" xmlns="http://www.w3.org/2000/svg">
  <!-- Layer 1: Input (蓝) -->
  <rect x="20" y="20" width="860" height="55" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="450" y="38" text-anchor="middle" font-family="Arial" font-size="13" font-weight="bold" fill="#1e40af">物理系统输入</text>
  <text x="450" y="58" text-anchor="middle" font-family="Arial" font-size="11" fill="#374151">交流网络 / MMC-HVDC / 含分布式电源的配电网</text>

  <!-- Arrow 1 -->
  <line x1="450" y1="75" x2="450" y2="95" stroke="#374151" stroke-width="2"/>
  <polygon points="450,100 445,93 455,93" fill="#374151"/>

  <!-- Layer 2: Frequency Domain Scanning + Reduction (蓝) -->
  <rect x="20" y="100" width="860" height="55" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="450" y="118" text-anchor="middle" font-family="Arial" font-size="13" font-weight="bold" fill="#1e40af">频域扫描 + 网络降阶</text>
  <text x="450" y="138" text-anchor="middle" font-family="Arial" font-size="11" fill="#374151">宽频扰动测试 → 坐标变换 → 高斯消元 → 边界导纳矩阵 Y(ω)</text>

  <!-- Arrow 2 -->
  <line x1="450" y1="155" x2="450" y2="175" stroke="#374151" stroke-width="2"/>
  <polygon points="450,180 445,173 455,173" fill="#374151"/>

  <!-- Layer 3: N Modeling Methods (绿) - 4 cards -->
  <rect x="20" y="180" width="200" height="100" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="120" y="198" text-anchor="middle" font-family="Arial" font-size="11" font-weight="bold" fill="#166534">方法 A: 矢量拟合</text>
  <text x="120" y="213" text-anchor="middle" font-family="Arial" font-size="9" fill="#374151">公共极点 + VF</text>
  <text x="120" y="228" text-anchor="middle" font-family="Arial" font-size="9" fill="#374151">误差&lt;1%</text>
  <text x="120" y="246" text-anchor="middle" font-family="Arial" font-size="9" fill="#6b7280">工业标准方法</text>

  <rect x="230" y="180" width="200" height="100" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="330" y="198" text-anchor="middle" font-family="Arial" font-size="11" font-weight="bold" fill="#166534">方法 B: Loewner 矩阵</text>
  <text x="330" y="213" text-anchor="middle" font-family="Arial" font-size="9" fill="#374151">非迭代 + SVD 自动定阶</text>
  <text x="330" y="228" text-anchor="middle" font-family="Arial" font-size="9" fill="#374151">误差&lt;0.8%</text>
  <text x="330" y="246" text-anchor="middle" font-family="Arial" font-size="9" fill="#6b7280">无收敛问题</text>

  <rect x="440" y="180" width="200" height="100" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="540" y="198" text-anchor="middle" font-family="Arial" font-size="11" font-weight="bold" fill="#166534">方法 C: Brune-Tellegen</text>
  <text x="540" y="213" text-anchor="middle" font-family="Arial" font-size="9" fill="#374151">拓扑内禀无源性</text>
  <text x="540" y="228" text-anchor="middle" font-family="Arial" font-size="9" fill="#374151">3.3× 加速</text>
  <text x="540" y="246" text-anchor="middle" font-family="Arial" font-size="9" fill="#6b7280">无需后处理校正</text>

  <rect x="650" y="180" width="200" height="100" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="750" y="198" text-anchor="middle" font-family="Arial" font-size="11" font-weight="bold" fill="#166534">方法 D: 双层 FDNE</text>
  <text x="750" y="213" text-anchor="middle" font-family="Arial" font-size="9" fill="#374151">局部无源性补偿</text>
  <text x="750" y="228" text-anchor="middle" font-family="Arial" font-size="9" fill="#374151">0.1–0.2 s 建模</text>
  <text x="750" y="246" text-anchor="middle" font-family="Arial" font-size="9" fill="#6b7280">100% 收敛率</text>

  <!-- Arrow 3 -->
  <line x1="450" y1="280" x2="450" y2="300" stroke="#374151" stroke-width="2"/>
  <polygon points="450,305 445,298 455,298" fill="#374151"/>

  <!-- Layer 4: Equivalent Circuit Output (紫) -->
  <rect x="20" y="305" width="860" height="55" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="450" y="323" text-anchor="middle" font-family="Arial" font-size="13" font-weight="bold" fill="#5b21b6">等效电路输出</text>
  <text x="450" y="343" text-anchor="middle" font-family="Arial" font-size="11" fill="#374151">诺顿等效 / 戴维南等效 / RLCM 网络 / 状态空间描述符 → EMT 时域求解</text>

  <!-- Arrow 4 -->
  <line x1="450" y1="360" x2="450" y2="380" stroke="#374151" stroke-width="2"/>
  <polygon points="450,385 445,378 455,378" fill="#374151"/>

  <!-- Layer 5: Application Scenarios (琥珀) -->
  <rect x="20" y="385" width="270" height="85" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="155" y="403" text-anchor="middle" font-family="Arial" font-size="12" font-weight="bold" fill="#92400e">实时仿真</text>
  <text x="155" y="420" text-anchor="middle" font-family="Arial" font-size="10" fill="#374151">RTDS / FPGA / GPU</text>
  <text x="155" y="436" text-anchor="middle" font-family="Arial" font-size="10" fill="#374151">20–50 μs 步长</text>
  <text x="155" y="452" text-anchor="middle" font-family="Arial" font-size="10" fill="#374151">节点规模受限</text>

  <rect x="315" y="385" width="270" height="85" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="450" y="403" text-anchor="middle" font-family="Arial" font-size="12" font-weight="bold" fill="#92400e">混合协同仿真</text>
  <text x="450" y="420" text-anchor="middle" font-family="Arial" font-size="10" fill="#374151">EMT-TSA 接口等值</text>
  <text x="450" y="436" text-anchor="middle" font-family="Arial" font-size="10" fill="#374151">Δt=50μs / ΔT=500μs</text>
  <text x="450" y="452" text-anchor="middle" font-family="Arial" font-size="10" fill="#374151">150–160× 加速</text>

  <rect x="610" y="385" width="270" height="85" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="745" y="403" text-anchor="middle" font-family="Arial" font-size="12" font-weight="bold" fill="#92400e">大电网分割并行</text>
  <text x="745" y="420" text-anchor="middle" font-family="Arial" font-size="10" fill="#374151">MATE / 弱耦合解耦</text>
  <text x="745" y="436" text-anchor="middle" font-family="Arial" font-size="10" fill="#374151">子系统独立并行</text>
  <text x="745" y="452" text-anchor="middle" font-family="Arial" font-size="10" fill="#374151">O(n³) → O(m³)</text>

  <!-- Legend -->
  <rect x="20" y="485" width="14" height="14" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="38" y="497" font-family="Arial" font-size="10" fill="#374151">输入/扫描</text>
  <rect x="120" y="485" width="14" height="14" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="138" y="497" font-family="Arial" font-size="10" fill="#374151">建模方法</text>
  <rect x="240" y="485" width="14" height="14" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="258" y="497" font-family="Arial" font-size="10" fill="#374151">等效输出</text>
  <rect x="360" y="485" width="14" height="14" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="378" y="497" font-family="Arial" font-size="10" fill="#374151">应用场景</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 频变网络等值（FDNE）方法体系架构：频域扫描 → 降阶 → 4类建模方法 → 等效电路 → 3类应用场景</p>

## 适用边界与选择指南

**选矢量拟合**：通用工业场景，已有成熟工具链（MATLAB VF 工具箱），优先考虑公共极点策略以降低计算量。

**选 Loewner 矩阵**：需要自动阶数辨识、不想调试初始极点参数、追求非迭代稳定流程。

**选 Brune-Tellegen**：对数值稳定性要求极高（涉及开关动作、HVDC 换相失败等强暂态场景），希望从拓扑层面内禀保证无源性。

**选双层 FDNE**：MMC 并网或含电力电子的交直流混合仿真，需要兼顾宽频动态捕捉与建模效率。

**选 MATE 多速率**：大规模交直流系统（1000+ 节点），接口两侧时间尺度差异显著（200 倍），需要多速率协同仿真框架。

## 相关方法
- [[vector-fitting]] — FDNE 矢量拟合的核心算法
- [[prony-analysis]] — 网络等值的时域参数辨识方法
- [[passivity-enforcement]] — 无源性强制修正算法
- [[loewner-matrix-approach]] — Loewner 矩阵非迭代有理逼近

## 相关模型
- [[fdne-model]] — 频变网络等值模型
- [[thevenin-equivalent]] — 戴维南等效模型

## 相关主题
- [[co-simulation|混合仿真]] — 网络等值用于 EMT-机电混合
- [[frequency-dependent-modeling|频率相关建模]] — 宽频 FDNE 理论基础
- [[real-time-simulation|实时仿真]] — 等值模型的实时实现
- [[parallel-computing|并行计算]] — 网络分割与并行协同
- [[multirate-method|多速率仿真]] — MATE 多速率接口框架

## 来源论文

Ahmadi 2021 — 多端口 FDNE 的 Brune-Tellegen 网络综合：无源性由拓扑内禀保证，230 kV 三相输电系统验证，3.3× 加速，80 个 RLCM 模块。

Gurrala 2015 — Loewner 矩阵方法：非迭代 FDNE 建模，SVD 自动定阶，全频段误差 $<0.8\%$，建模时间较 VF 减少 30%–50%。

Li 2019 — 多区域戴维南等值（MATE）多速率协同仿真：2412 母线系统验证，150–160× 加速，接口误差 $<0.012$。

Zhang 2012 — FDNE 用于 EMT-机电混合仿真接口：公共极点策略，1–2 kHz 频段误差 $<1\%$，无源性修正误差 $<0.5\%$。

Shu 2019 — 双层 FDNE + 局部无源性补偿：建模时间 0.1–0.2 s（vs 全局优化 45.6 s），发散率从 18.7% 降至 0%。