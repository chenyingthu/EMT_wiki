---
title: "准TEM近似 (Quasi-TEM Approximation)"
type: method
tags: [quasi-tem, transmission-line, wave-propagation, frequency-dependent, ground-return, telegrapher]
created: "2026-05-04"
updated: "2026-05-14"
---

# 准TEM近似 (Quasi-TEM Approximation)

## 定义

准横电磁波（Quasi-Transverse Electromagnetic, Quasi-TEM）近似是输电线路电磁传播分析中的核心理论框架。当介质（如大地、电缆绝缘层）具有有限电导率或频率相关特性时，纯TEM模式无法严格存在——电场和磁场不再完全垂直于传播方向。准TEM近似假设电磁场**近似横向分布**，允许存在微小的纵向电场分量 $E_z$ 和纵向磁场分量 $H_z$，但满足：

$$|E_z| \ll |E_t|, \quad |H_z| \ll |H_t|$$

其中 $E_t$ 和 $H_t$ 分别为横向电场和磁场分量。这一近似使得沿线路方向的电磁场行为可以用**电报方程（Telegrapher's Equations）**描述，将偏微分方程简化为沿传播方向的常微分方程。

准TEM近似的物理本质是：当线路截面尺寸 $d$ 远小于工作波长 $\lambda$（即 $d \ll \lambda$，或 $f \ll c/d$）时，横向电磁场分布可以近似视为静态场分布，纵向分量仅作为小扰动存在。这一条件在电力系统工频至数百kHz范围内对架空线和电缆均成立。

## EMT中的作用

准TEM近似是电磁暂态（EMT）仿真中输电线路建模的理论基础：

- **频变参数建模**：通过准TEM框架，线路的每单位长度阻抗 $Z(\omega)$ 和导纳 $Y(\omega)$ 可表示为频率的函数，其中大地回路的频率依赖特性通过 Carson 公式或 Sunde 公式建模
- **多导体线路分析**：准TEM假设使得多导体线路的耦合电报方程可以通过模态变换对角化，实现模态解耦
- **行波传播建模**：传播常数 $\gamma(\omega)$ 和特性阻抗 $Z_c(\omega)$ 均由准TEM近似导出，是 ATP/EMTP 中频变线路模型（Marti 模型、ULM 模型）的核心
- **电缆高频瞬态分析**：在电缆系统中，准TEM近似结合 coaxial 波传播特性，可准确预测极快瞬态（VFT）下的电压应力分布
- **地回路阻抗计算**：有损大地中的准TEM近似导出 Carson 公式、Pollaczek 公式和 Sunde 公式，是地电位升高和雷电过电压分析的基础

## 核心机制

### 1. 电报方程与准TEM条件

准TEM近似下的电报方程描述了沿线路（x方向）的电压和电流变化：

$$-\frac{\partial v(x,t)}{\partial x} = R'(x,t) * i(x,t) + L_0 \frac{\partial i(x,t)}{\partial t} \tag{1}$$

$$-\frac{\frac{\partial i(x,t)}{\partial x} = C_0 \frac{\partial v(x,t)}{\partial t} \tag{2}$$

其中 $R'(x,t)$ 是瞬态电阻矩阵（反映集肤效应和大地损耗的时间域卷积核），$L_0$ 是空气磁通产生的电感矩阵，$C_0$ 是空气电容矩阵。在频域中，电报方程简化为：

$$-\frac{dV(x,\omega)}{dx} = Z(\omega)I(x,\omega) \tag{3}$$

$$-\frac{dI(x,\omega)}{dx} = Y(\omega)V(x,\omega) \tag{4}$$

其中 $Z(\omega)$ 和 $Y(\omega)$ 分别为每单位长度的串联阻抗矩阵和并联导纳矩阵。

**准TEM近似的有效性条件**（Kurokawa 2006）：
- 电磁场在垂直于线路轴的方向上具有准静态行为（quasi-stationary EM-field simplification）
- 导线间距远大于导线半径之和
- 忽略结构和绝缘体的电磁效应
- 大地假设为均匀、平面表面
- 频率满足 $f \ll c/d$（截面尺寸远小于波长）

### 2. 串联阻抗的分解

每单位长度串联阻抗矩阵可分解为三个物理分量（Kurokawa 2006；Duarte 2023）：

$$Z(\omega) = Z_i(\omega) + Z_e(\omega) + Z_g(\omega) \tag{5}$$

**内部阻抗 $Z_i(\omega)$**：与导线内部的电磁场相关，由集肤效应引起。对于圆柱导体，内部阻抗可用修正贝塞尔函数精确计算：

$$Z_{ii} = \frac{\rho_c}{2\pi a} \frac{I_0\left(j\frac{\omega\mu_0}{\rho_c}a^2\right)}{I_1\left(j\frac{\omega\mu_0}{\rho_c}a^2\right)} \tag{6}$$

其中 $I_0$ 和 $I_1$ 是第一类修正贝塞尔函数，$\rho_c$ 为导体电阻率，$a$ 为导体半径。集肤效应导致电阻随频率增加（$R \propto \sqrt{f}$），电感随频率减小。

**外部阻抗 $Z_e(\omega)$**：与导线外部（空气中）的电磁场相关。对于理想导电大地（无限电导率），外部阻抗仅表现为与频率无关的电感：

$$L_{ii} = \frac{\mu_0}{2\pi} \ln\frac{b}{a} \tag{7}$$

其中 $b$ 为参考距离（通常为导线间距）。

**大地回路的阻抗 $Z_g(\omega)$**：考虑有损大地（有限电导率 $\sigma$）的影响。这是准TEM近似中最关键的频变分量。

### 3. 大地回路阻抗公式

**Carson 公式（1926）**：经典的大地回路阻抗表达式，假设位移电流远小于传导电流（$\sigma \gg \omega\varepsilon$）：

$$Z_g = j\omega\frac{\mu_0}{2\pi} \int_0^\infty \frac{e^{-2h\lambda}}{\lambda + \sqrt{\lambda^2 + j\frac{\omega\mu_0}{\sigma}}} \frac{d\lambda}{\lambda} \tag{8}$$

其中 $h$ 为导线高度，$\sigma$ 为大地电导率。Carson 公式在低频和中频（< 10 kHz）范围内对架空线精度良好。

**Pollaczek 公式**：Carson 积分的等价解析形式，适用于地下导体：

$$Z_g = \frac{j\omega\mu_0}{2\pi} \left[ \ln\left(\frac{1.85}{h\sqrt{\frac{\omega\mu_0}{\sigma}}}\right) + j0.25 - j2\left(\frac{h}{\delta}\right) + 2\left(\frac{h}{\delta}\right)^2(1-j) \right] \tag{9}$$

其中 $\delta = \sqrt{\frac{2}{\omega\mu_0\sigma}}$ 为大地的趋肤深度。

**Sunde 公式（1968）**：更简洁的近似形式，在工程实践中广泛使用：

$$Z_g \approx j\omega\frac{\mu_0}{2\pi} \left[ \ln\left(\frac{1}{h\sqrt{j\omega\mu_0(\sigma + j\omega\varepsilon)}}\right) + \frac{j\omega\mu_0}{Z_g^{\text{carson}}} \right] \tag{10}$$

Sunde 公式的优势在于同时考虑了大地的电导率和介电常数，适用于更宽的频率范围。

**Xue 等（2011）和 Papadopoulos 等（2021）公式**：基于 Hertz 势的准TEM近似推导，适用于埋地电缆系统。Duarte 等（2023）通过全波 FDTD 方法验证了这些公式在计算地下电缆瞬态时的有效性，表明在准确计算地回路参数的前提下，传输线理论可以准确预测上升时间低至 0.2 μs 的快速瞬态。

### 4. 并联导纳与大地回路导纳

每单位长度并联导纳矩阵为：

$$Y(\omega) = j\omega P^{-1}(\omega) \tag{11}$$

其中 $P(\omega) = P_e + P_g$ 为电位系数矩阵，$P_e$ 为外部对角矩阵，$P_g$ 为大地回路电位系数矩阵。

对于架空线，通常假设空气电导为零，因此：

$$P_{ii} = \frac{1}{2\pi\varepsilon_0} \ln\frac{b}{a} \tag{12}$$

对于地下电缆，**大地回路导纳近似**（Duarte 等 2023）显著简化了计算：

$$P_g = j\omega Y_g^{-1} \tag{13}$$

$$Y_g = \gamma_g^2 Z_g^{-1} \tag{14}$$

其中 $Z_g$ 由 Sunde 公式给出，$\gamma_g^2 = j\omega\mu_0(\sigma_1 + j\omega\varepsilon_1)$ 为大地的传播常数平方。Duarte 等（2023）证明，尽管此近似形式简单，但计算结果与更完整的公式（Papadopoulos 等、Xue 等）相比具有可比精度，且计算效率显著更高。

### 5. 传播常数与特性阻抗

由电报方程（3）和（4）可导出传播常数和特性阻抗：

$$\gamma(\omega) = \sqrt{Z(\omega)Y(\omega)} \tag{15}$$

$$Z_c(\omega) = \sqrt{Z(\omega)Y^{-1}(\omega)} \tag{16}$$

对于单模线路，低频近似为：

$$\gamma \approx \frac{R}{2}\sqrt{\frac{C}{L}} + j\omega\sqrt{LC} \tag{17}$$

其中衰减常数 $\alpha = \text{Re}(\gamma) \approx \frac{R}{2}\sqrt{\frac{C}{L}}$，相位常数 $\beta = \text{Im}(\gamma) \approx \omega\sqrt{LC}$。

### 6. 模态解耦

对于 $n$ 导体多相线路，电报方程为耦合的矩阵方程。通过模态变换实现解耦：

$$Y Z = T_I \Gamma^2 T_I^{-1} = T_I \text{diag}(\gamma_1^2, \gamma_2^2, \dots, \gamma_n^2) T_I^{-1} \tag{18}$$

其中 $\Gamma^2$ 为特征值矩阵，$T_I$ 为模态变换矩阵。变换后的模态方程为：

$$\frac{d^2V_m}{dx^2} = \Gamma^2 V_m \tag{19}$$

其解为：

$$V_m(x) = e^{-\Gamma x} V_{m1} + e^{\Gamma x} V_{m2} \tag{20}$$

对于理想对称三相线路，Clarke 变换矩阵可将线路精确解耦为三个独立模态（0、$\alpha$、$\beta$）。对于非对称线路，变换矩阵为频率相关矩阵，这是 Marti 频变变换模型的基础（Marti 1982；Gustavsen & Semlyen 1998）。

### 7. 行波模型与ULM

准TEM近似导出的频变行波模型是现代 EMT 程序中最精确的线路建模方法。通用线路模型（Universal Line Model, ULM）（Morched 等 1999）是此框架下的最先进实现：

$$\tilde{H}(\omega) = T_I \text{diag}(e^{-\tilde{\gamma}_1 l}, e^{-\tilde{\gamma}_2 l}, \dots, e^{-\tilde{\gamma}_n l}) T_I^{-1} \tag{21}$$

$$\tilde{Y}_C(\omega) = \tilde{Z}^{-1}(\omega)\tilde{Y}(\omega) = (\tilde{Z}(\omega)\tilde{Y}(\omega))^{-1/2}\tilde{Y}(\omega) \tag{22}$$

其中 $\tilde{H}$ 和 $\tilde{Y}_C$ 分别用低阶延迟有理函数逼近（Gustavsen 2012），然后转换为 EMT 程序可用的 Norton 等效电路。

## 形式化表达

### 核心公式汇总

| 公式编号 | 名称 | 表达式 | 物理意义 |
|---------|------|--------|---------|
| (1)-(2) | 时域电报方程 | $-\partial_x v = R' * i + L_0\partial_t i$ | 准TEM下电压-电流耦合关系 |
| (3)-(4) | 频域电报方程 | $-\partial_x V = ZI, \; -\partial_x I = YV$ | 频域传输线基本方程 |
| (5) | 阻抗分解 | $Z = Z_i + Z_e + Z_g$ | 内部+外部+大地回路阻抗 |
| (6) | 内部阻抗（贝塞尔） | $Z_{ii} = \frac{\rho_c}{2\pi a}\frac{I_0(\xi)}{I_1(\xi)}, \; \xi = j\frac{\omega\mu_0}{\rho_c}a^2$ | 集肤效应导致的频变内部阻抗 |
| (7) | 外部电感 | $L_{ii} = \frac{\mu_0}{2\pi}\ln\frac{b}{a}$ | 空气磁通产生的几何电感 |
| (8) | Carson 大地阻抗 | $Z_g = j\omega\frac{\mu_0}{2\pi}\int_0^\infty\frac{e^{-2h\lambda}}{\lambda+\sqrt{\lambda^2+j\omega\mu_0/\sigma}}\frac{d\lambda}{\lambda}$ | 有损大地的回路阻抗（经典） |
| (9) | Pollaczek 大地阻抗 | 解析近似形式 | Carson 积分的等价解析表达 |
| (10) | Sunde 大地阻抗 | $Z_g \approx j\omega\frac{\mu_0}{2\pi}\ln\left(\frac{1}{h\sqrt{j\omega\mu_0(\sigma+j\omega\varepsilon)}}\right)$ | 同时考虑电导率和介电常数 |
| (11)-(12) | 并联导纳 | $Y = j\omega P^{-1}, \; P_{ii} = \frac{1}{2\pi\varepsilon_0}\ln\frac{b}{a}$ | 电容和大地回路导纳 |
| (13)-(14) | 大地回路导纳近似 | $P_g = j\omega Y_g^{-1}, \; Y_g = \gamma_g^2 Z_g^{-1}$ | 简化计算（Duarte 2023） |
| (15)-(16) | 传播常数和特性阻抗 | $\gamma = \sqrt{ZY}, \; Z_c = \sqrt{ZY^{-1}}$ | 行波传播参数 |
| (17) | 低频近似 | $\gamma \approx \frac{R}{2}\sqrt{\frac{C}{L}} + j\omega\sqrt{LC}$ | 低频下的传播常数近似 |
| (18)-(20) | 模态解耦 | $YZ = T_I\Gamma^2T_I^{-1}, \; V_m(x) = e^{-\Gamma x}V_{m1} + e^{\Gamma x}V_{m2}$ | 多导体线路模态解耦 |
| (21)-(22) | ULM 行波模型 | $\tilde{H} = T_I e^{-\tilde{\Gamma}l}T_I^{-1}, \; \tilde{Y}_C = (\tilde{Z}\tilde{Y})^{-1/2}\tilde{Y}$ | 通用线路模型（最先进频变模型） |

### 集肤效应与频率关系

集肤深度 $\delta$ 决定了电流在导体截面上的分布：

$$\delta = \sqrt{\frac{2}{\omega\mu_0\sigma_c}} \tag{23}$$

当导体半径 $a \ll \delta$ 时（低频），电流均匀分布，直流电阻适用。当 $a \gg \delta$ 时（高频），电流集中在导体表面，交流电阻近似为：

$$R_{ac} \approx R_{dc} \frac{a}{2\delta} = R_{dc}\sqrt{\frac{\omega\mu_0\sigma_c}{4}} \tag{24}$$

即 $R_{ac} \propto \sqrt{f}$。

### 大地趋肤深度

大地的趋肤深度决定了电磁波在大地中的穿透深度：

$$\delta_{\text{earth}} = \sqrt{\frac{2}{\omega\mu_0\sigma}} \tag{25}$$

对于典型土壤 $\sigma = 0.01 \text{ S/m}$，在 1 kHz 时 $\delta_{\text{earth}} \approx 500 \text{ m}$；在 100 kHz 时 $\delta_{\text{earth}} \approx 50 \text{ m}$。高频下大地趋肤效应显著，导致 Carson 积分中的高频分量被抑制。

## 关键技术挑战

### 1. 频变大地参数的精确建模

大地的电导率 $\sigma$ 和介电常数 $\varepsilon$ 本身具有频率依赖性（色散特性）。Alipio 等（2023）指出，在高频雷电瞬态分析中，忽略位移电流（$\sigma \gg \omega\varepsilon$ 假设）和频率无关大地参数会导致过电压幅值被低估。对于高电阻率土壤（$\rho = 1000 \; \Omega\cdot\text{m}$），考虑频率相关土壤参数后，138 kV 和 230 kV 线路的反击率增加 4-6%；对于 $\rho = 5000 \; \Omega\cdot\text{m}$ 和 $10000 \; \Omega\cdot\text{m}$ 的土壤，反击率分别增加 7-12% 和 9-15%。

### 2. 非均匀线路和弯曲段

准TEM近似假设导线平行且均匀。当线路存在非平行段（如架空线与电缆连接处、跨越河流山谷的弧垂段）时，模态变换矩阵不再是常数，传输线方程中的耦合项无法通过对角化完全消除（Kurokawa 2006；Ramirez 等 2003）。此时需要分段建模或使用非均匀线路模型。

### 3. 高频电缆建模的精度限制

Gustavsen（2023）指出，标准的多导体频变行波模型在极高频率（> 1 MHz）下可能无法准确预测电压波前的阻尼。这是因为模型忽略了导体绞线效应、绝缘层高频损耗和半导电屏蔽层损耗。对于变压器和电机绕组中的脉冲传播预测，需要引入测量的同轴波传播特性（coaxial mode propagation characteristics）进行高频修正。

### 4. 模态变换矩阵的频率依赖性

在准TEM近似下，理想对称线路的模态变换矩阵为常数（如 Clarke 变换）。但对于实际非对称线路和频变参数，变换矩阵 $T_I(\omega)$ 和 $T_V(\omega)$ 是频率相关的。Marti 模型使用常数变换矩阵近似频变特性，而 ULM 模型对变换矩阵的每个元素分别进行有理拟合，精度更高但计算量更大（Gustavsen & Semlyen 1998；Morched 等 1999）。

### 5. 多速率仿真中的准TEM适用性

Ye 和 Strunz（2016）的多尺度频变线路模型展示了准TEM框架在宽频仿真中的灵活性：在电磁暂态（高频）模式下，模型处理瞬时信号，时间步长在微秒级；在机电暂态（低频）模式下，模型处理动态相量（解析信号），时间步长可扩展至毫秒级。准TEM近似为这种多速率过渡提供了理论基础。

## 量化性能边界

### 大地回路阻抗公式对比

| 公式 | 适用频率范围 | 是否考虑位移电流 | 计算复杂度 | 验证精度 |
|------|------------|----------------|-----------|---------|
| Carson (1926) | < 10 kHz | 否（$\sigma \gg \omega\varepsilon$） | 中等（数值积分） | 架空线低频基准 |
| Pollaczek | < 100 kHz | 否 | 较低（解析公式） | Carson 的近似 |
| Sunde (1968) | < 1 MHz | 是 | 低（闭式公式） | 全频段良好 |
| Xue 等 (2011) | < 1 MHz | 是 | 高（ improper 积分） | FDTD 验证 |
| Papadopoulos 等 (2021) | < 1 MHz | 是 | 高（ improper 积分） | FDTD 验证 |
| Duarte 近似 (2023) | < 1 MHz | 是 | 极低 | 与 FDTD 误差 < 2% |

*数据来源：Duarte 等 2023, Alipio 等 2023*

### 准TEM vs 全波 FDTD 验证

Duarte 等（2023）通过全波 FDTD 方法验证了准TEM近似在地下电缆瞬态分析中的精度：
- **测试条件**：50 m 和 100 m 三相电缆，土壤电阻率 200 $\Omega\cdot\text{m}$ 和 1000 $\Omega\cdot\text{m}$
- **激励波形**：上升时间 0.2 μs、半值时间 1.83 μs 的标准化脉冲（覆盖 10 Hz - 1 MHz 频段）
- **结果**：准TEM近似（结合 Xue 等、Papadopoulos 等大地参数公式）与全波 FDTD 方法在所有场景下均展现出良好的一致性
- **结论**：在准确确定地回路参数（阻抗和导纳）的前提下，准TEM传输线理论可准确计算快速瞬态，且计算效率远高于全波 FDTD

### 集肤效应量化

| 频率 | 铜导体 $\delta$ (mm) | $R_{ac}/R_{dc}$ (a=3mm) |
|------|---------------------|------------------------|
| 50 Hz | 9.2 | 1.00 |
| 400 Hz | 2.9 | 1.03 |
| 1 kHz | 2.1 | 1.06 |
| 10 kHz | 0.66 | 1.25 |
| 100 kHz | 0.21 | 1.87 |
| 1 MHz | 0.066 | 3.5 |

*数据来源：Kurokawa 2006, 基于公式 (6) 计算*

### 大地电阻率对雷电过电压的影响

| 土壤电阻率 | 过电压增幅 | 反击率增幅 | 数据来源 |
|-----------|----------|----------|---------|
| 1000 $\Omega\cdot\text{m}$ | +4~6% | +4~6% | Alipio 2023 |
| 5000 $\Omega\cdot\text{m}$ | +7~12% | +7~12% | Alipio 2023 |
| 10000 $\Omega\cdot\text{m}$ | +9~15% | +9~15% | Alipio 2023 |

## 适用边界与选择指南

### 适用条件

- **频率范围**：$f < 1 \text{ MHz}$（架空线可达数百kHz，电缆建议 < 100 kHz）
- **几何条件**：线路截面尺寸 $d \ll \lambda$，即 $fd/c \ll 1$
- **大地条件**：均匀或分层大地，准TEM公式对分层大地的扩展（如 Marti 模型）可扩展至更复杂情况
- **线路类型**：均匀平行多导体线路（架空线、地下电缆、同轴电缆）

### 失效边界

- **高频全波效应**：当频率达到 GHz 级（波长远小于线路截面），准TEM近似完全失效，需采用全波电磁场方法（FDTD、FEM）
- **大损耗介质**：当介质损耗极大时，纵向场分量不再是小扰动，准TEM假设失效
- **非均匀/弯曲线路**：导线不平行或截面变化的区域，准TEM的均匀传输线方程不适用
- **不均匀介质**：多层土壤或异质绝缘材料中，混合模式传播，准TEM的模态解耦精度下降
- **极短电缆（< 1 m）**：当电缆长度与波长相比较短时，分布参数模型退化为集总参数模型，准TEM的连续方程失去意义

### 方法选择指南

| 场景 | 推荐模型 | 准TEM适用性 |
|------|---------|-----------|
| 架空线工频/暂态（< 10 kHz） | 常数参数 π 模型 | 高度适用 |
| 架空线频变参数（10 Hz - 100 kHz） | Marti 频变模型 | 高度适用 |
| 架空线宽频（10 Hz - 1 MHz） | ULM 通用线路模型 | 高度适用 |
| 地下电缆瞬态（0.2 μs 上升时间） | ULM + 精确地回路参数 | 适用（需精确 $Z_g, Y_g$） |
| 电缆 VFT（> 1 MHz） | 测量修正 ULM | 部分适用（需 coaxial 模式修正） |
| 非平行线路段 | 分段 ULM + 接口矩阵 | 局部适用 |
| 全波高频（> 100 MHz） | FDTD / FEM 全波 | 不适用 |

## 相关方法

- [[transmission-line-model]] - 输电线路模型
- [[cable-model]] - 电缆模型
- [[wideband-modeling]] - 宽频建模
- [[frequency-dependent-modeling]] - 频率相关建模
- [[earth-return-impedance]] - 地回路阻抗
- [[characteristic-method]] - 特征线法
- [[bergeron-model]] - Bergeron 行波模型
- [[modal-decomposition]] - 模态分解
- [[distributed-parameter-model]] - 分布参数模型
- [[universal-line-model]] - 通用线路模型（ULM）

## 来源论文

- **Kurokawa 等 2006** - "A New Procedure to Derive Transmission-Line Parameters: Applications and Restrictions" — 系统阐述了准TEM近似下输电线路参数的经典计算方法，明确了准静态电磁场简化假设的有效性条件和限制
- **Duarte 等 2023** - "Assessment of the Transmission Line Theory in the Modeling of Multiconductor Underground Cable Systems" — 通过全波 FDTD 验证了准TEM近似在地下电缆快速瞬态分析中的精度，确认了地回路导纳近似的有效性
- **Alipio 等 2023** - "Influence of a Lossy Ground on the Lightning Performance of Overhead Transmission Lines" — 研究了有损大地中位移电流和频率相关土壤参数对雷电过电压的影响，量化了高电阻率土壤下的反击率增幅
- **Gustavsen 2023** - "Multi-Conductor Cable Modeling With Inclusion of Measured Coaxial Wave Propagation Characteristics" — 提出了将测量同轴波传播特性引入宽频多导体电缆模型的高频修正方法
- **Escamilla 等 2013** - "New Model for Overhead Lossy Multiconductor Transmission Lines" — 基于特征线法提出了无空间离散化的频变多导体线路时域模型，将频率依赖性嵌入瞬态电阻矩阵
- **Ye 和 Strunz 2016** - "Multi-Scale and Frequency-Dependent Modeling of Electric Power Transmission Lines" — 基于准TEM框架开发了多尺度频变线路模型，实现了从电磁暂态到机电暂态的统一仿真
- **Carson 1926** - "Wave Propagation in Overhead Wires" — 首次推导了考虑有损大地回路的线路阻抗公式（Carson 公式），是准TEM大地回路分析的奠基性工作
- **Wedepohl 1963** - "Applications of Matrix Methods to the Solution of Traveling-Wave Phenomena" — 将矩阵方法引入行波现象分析，奠定了多导体线路准TEM模态分析的基础

## 来源论文

| 论文 | 年份 |
|------|------|
| [[fast-electromagnetic-transient-model-for-mmc-hvdc-considering-dc-fault|Fast Electromagnetic Transient Model for MMC-HVDC Considerin]] | 2018 |
| [[high-frequency-transients-in-buried-insulated-wires-transmission-line-simulation-19、20、21|High-frequency transients in buried insulated wires: Transmi]] | 2024 |
| [[high-frequency-transients-in-buried-insulated-wires-transmission-line-simulation|High-frequency transients in buried insulated wires: Transmi]] | 2024 |
