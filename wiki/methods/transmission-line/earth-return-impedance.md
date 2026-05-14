---
title: "地回路阻抗 (Earth Return Impedance)"
type: method
tags: [earth-return, impedance, carson, pollaczek, sunde, multi-layer soil, transmission-line, ground-return]
created: "2026-05-02"
updated: "2026-05-14"
---

# 地回路阻抗 (Earth Return Impedance)

## 定义

地回路阻抗描述电流经大地或土壤介质返回时，对线路单位长度串联阻抗矩阵产生的频率相关贡献。它是 EMT 仿真中输电线路参数计算的核心组成部分，直接决定零序参数、不平衡故障电流幅值和相位、雷电暂态回流路径以及地下电缆护套耦合的准确性。

地回路阻抗 $Z_\text{earth}(\omega)$ 在物理上源于电流在有限导电性大地中传播时产生的欧姆损耗和磁场扩散效应。大地不是理想导体，电流在土壤中传播时会产生趋肤效应（skin effect in earth），导致等效镜像导体深度随频率变化——这就是 Carson 原始洞见：所谓"镜像导体"实际上是一个随频率变化的"扩散深度"（diffusion depth）。

$$Z'(\omega) = Z_\text{int}(\omega) + Z_\text{ext}(\omega) + Z_\text{earth}(\omega)$$

其中 $Z_\text{int}$ 描述导体内部集肤效应，$Z_\text{ext}$ 描述外部几何磁场（空气中），$Z_\text{earth}$ 描述大地返回路径的贡献。注意 $Z_\text{earth}$ 既出现在自阻抗项中也出现在互阻抗项中。

**重要区分**：地回路阻抗不等同于接地网接地电阻。接地电阻是直流或低频下的单点电位-电流比，而地回路阻抗是分布参数线路模型中单位长度的频率相关串联阻抗矩阵元素，用于描述沿线路方向传播的电磁暂态过程。它应与 [[grounding-system-model]] 区分开来。

## EMT 中的角色

在 EMT 仿真中，地回路阻抗影响以下关键场景：

- **零序和不平衡故障**：单相接地故障电流幅值和相位高度依赖于地回路阻抗，尤其在多回线和平行线路中
- **雷电和开关暂态**：高频段（kHz–MHz）下大地趋肤效应显著，影响波头陡度和传播损耗
- **地下电缆系统**：护套、铠装与土壤之间的电磁耦合，交叉互联接地系统的环流计算
- **多层土壤**：实际工程中土壤电阻率分层现象普遍，两层或多层土壤模型可产生高达 38% 的阻抗差异
- **平行线路感应耦合**：邻近线路的感应电压和电流计算

如果在高频或不平衡场景中简单采用工频近似（如忽略地回路阻抗的频率依赖性），可能将传播损耗、相位延迟和耦合强度估错——De Conti & Lima 2026 的误差分析显示，Saad–Gaba–Giroux 近似在 1000 Ω·m 土壤中误差超过 20%。

## 核心理论框架

### 1. 均匀半无限大地：Carson 公式

1926 年，Carson 首次推导了架空导体在均匀半无限大地中的自阻抗和互阻抗公式。其核心思想是将大地效应等效为一个频率相关的"扩散镜像"。

**物理图像**：电流 $I$ 在高度 $h$ 的架空导体中流动时，大地中感应出返回电流。由于大地具有有限电导率 $\sigma$，返回电流并非集中在地表镜像位置，而是向地下扩散。扩散深度（趋肤深度）为：

$$\delta = \sqrt{\frac{2}{\omega \mu_0 \sigma}}$$

其中 $\omega$ 为角频率，$\mu_0$ 为真空磁导率，$\sigma$ 为土壤电导率。低频时 $\delta$ 很大（返回电流分布广），高频时 $\delta$ 很小（返回电流趋近地表）。

**Carson 互阻抗公式**（单位长度，两导体间距 $D$，高度分别为 $h_m$ 和 $h_n$）：

$$Z_{mn}^\text{earth} = \frac{j\omega\mu_0}{2\pi} \left[ K_0(\gamma_0 D') - K_0(\gamma_0 D) \right]$$

其中 $D = \sqrt{(x_m-x_n)^2 + (h_m+h_n)^2}$ 为导体与其镜像之间的距离，$D' = \sqrt{(x_m-x_n)^2 + (h_m-h_n)^2}$ 为两导体之间的直接距离，$\gamma_0 = j\omega\sqrt{\mu_0\epsilon_0}$ 为空气中的传播常数（通常可近似为 0），$K_0$ 为零阶修正贝塞尔函数。

对于自阻抗（$m=n$），公式退化为 Pollaczek 积分形式：

$$Z_{mm}^\text{earth} = \frac{j\omega\mu_0}{2\pi} \int_0^\infty \frac{e^{-2h\lambda}}{\lambda + \frac{j\omega\mu_0}{Z_g}} \frac{d\lambda}{\lambda}$$

其中 $Z_g$ 为大地表面阻抗。Carson 原始公式的数值计算需要处理半无限区间上的奇异积分，这是工程实现中的主要难点。

**Carson 公式的假设**：
- 均匀半无限大地，电导率 $\sigma$ 和介电常数 $\epsilon$ 为常数
- 导体为无限长平行圆柱
- 准 TEM 传播模式
- 忽略位移电流（低频近似）

### 2. Sunde 方程与 Pollaczek 积分

Sunde (1968) 提出了更简洁的地下导体地回路阻抗表达式，将 Pollaczek 积分简化为闭合形式：

$$Z_{mn}^\text{earth} = \frac{j\omega\mu_0}{2\pi} \left[ K_0(\gamma_1 d) - K_0(\gamma_1 D) \right]$$

其中 $\gamma_1 = \sqrt{j\omega\mu_0\sigma}$ 为大地中的传播常数，$d = \sqrt{(x_m-x_n)^2 + (h_m+h_n)^2}$ 为导体间距加两倍埋深，$D = \sqrt{(x_m-x_n)^2 + (h_m-h_n)^2 + 4h^2}$ 为修正距离。

Sunde 方程是 Pollaczek 积分在准-TEM 假设下的特例。De Conti & Lima 2026 证明，当 $\gamma_0 = 0$ 时，Xue–Magalhães 方程退化为 Sunde 方程。

### 3. Xue–Magalhães 准-TEM 方程

Magalhães 等人提出的准-TEM 方程是地下电缆地回路阻抗最严格的表达式之一，Xue 等人后来证明其与 Magalhães 公式等价。该方程考虑了空气和大地两种介质的传播常数：

$$Z_g = \frac{j\omega\mu_0}{2\pi} \left[ K_0(\gamma_1 d) - K_0(\gamma_1 D) + \Theta \right]$$

其中 $\Theta$ 为多层土壤修正项（半无限积分）：

$$\Theta = 2 \int_0^\infty \frac{e^H \lambda^2}{\sqrt{\lambda^2+\gamma_0^2} + \sqrt{\lambda^2+\gamma_1^2}} \frac{\cos(r\lambda)}{\lambda} d\lambda$$

在 (1) 和 (2) 中，$K_0$ 为零阶修正贝塞尔函数，$\gamma_0 = \sqrt{j\omega\mu_0\epsilon_0}$ 和 $\gamma_1 = \sqrt{j\omega\mu_1(\sigma_1+j\omega\epsilon_1)}$ 分别为空气和大地中的传播常数，$\mu_0$、$\epsilon_0$ 为真空磁导率和介电常数，$\sigma_1$ 为土壤电导率，$\mu_1=\mu_0$ 为土壤磁导率，$\epsilon_1=\epsilon_{r1}\epsilon_0$ 为土壤介电常数（$\epsilon_{r1}$ 通常取 10），$\omega$ 为角频率，$H=h_m+h_n+\sqrt{(h_m-h_n)^2+r^2}$，$d=\sqrt{(x_m-x_n)^2+(h_m+h_n)^2}$，$D=\sqrt{(x_m-x_n)^2+(h_m-h_n)^2+4h_mh_n}$。

**Xue–Magalhães 方程的优势**：同时考虑了空气和大地介质的频率特性，是宽频带电缆参数计算的基准参考。De Conti & Lima 2026 将其作为验证所有近似公式的"真值"。

### 4. 实用近似公式

由于 Xue–Magalhães 和 Sunde 方程涉及半无限区间上的复杂积分，工程 EMT 工具广泛采用闭合形式近似。

**Saad–Gaba–Giroux 公式**（ATPDraw 内部计算模块使用）：

$$Z_g \approx \frac{j\omega\mu_0}{2\pi} \left[ K_0(\gamma_1 d) + \frac{e^{-H\gamma_1}}{4+\gamma_1^2 r^2} \right]$$

该公式最初从 Pollaczek 方程推导而来，仅适用于低频率和低电阻率土壤中的紧密间距电缆（单回线系统）。De Conti & Lima 2026 的误差分析表明，在 100 Ω·m 土壤中误差可达 10%，在 1000 Ω·m 土壤中误差超过 20%（频率高达 10 MHz）。

**De Conti–Lima 公式**（2026 年提出）：

$$Z_g \approx \frac{j\omega\mu_0}{2\pi} \left[ K_0(\gamma_1 d) + \frac{H-r^2}{D^2} K_2(\gamma_1 D) - \frac{2rHe^{-\gamma_1 D}}{\gamma_1^2 D^2} \sum_{n=1}^{3} I_n \right]$$

其中 $I_1 = (H-\frac{8}{\gamma_1}D)r^2$，$I_2 = 4(\frac{\gamma_1 D}{2})^{2-\gamma_1 D} r \cdot 2\arctan\frac{H+D}{H-D}$，$I_3 = -\frac{8-8\gamma_1 D+\gamma_1^2 D^2}{(\gamma_1 D/2)^2} \arctan\frac{r\sqrt{1-\gamma_1 D}}{H+D}$。

De Conti–Lima 公式是 Sunde 方程的直接近似，但修正了高频率和大间距情况下的系统误差。De Conti & Lima 2026 证明：在 100 Ω·m 土壤中，即使电缆间距 $s=3$ m（总分离 4 m），误差也不超过 2.5%（频率高达 10 MHz），远低于 Saad–Gaba–Giroux 的 10–20% 误差。

**Wedepohl–Wilcox 公式**（PSCAD-EMTDC 默认表达式）：

Wedepohl 和 Wilcox 提出的近似公式在 PSCAD-EMTDC 的电缆参数计算工具中作为默认表达式使用。该公式同样基于 Pollaczek 积分的低频近似，但 De Conti & Lima 2026 指出其无法扩展到高频范围，因为推导中使用的近似在高频下失效。

**Vance 闭合形式近似**（Duarte 2021 扩展）：

Vance 提出的闭合形式近似用于多导体系统的地导纳计算。Duarte 等人 2021 将其扩展到多导体系统，考虑了更复杂的导体排列和土壤参数。

### 5. 多层土壤模型

实际土壤通常不是均匀的。Tsiamitros 等人 2008（Part I & II）提出了多层土壤中架空和地下导体地回路阻抗的统一理论框架。

**Hertzian 矢量方法**：

Tsiamitros 等人采用 Hertzian 矢量 $\Pi$ 作为电磁场方程的核心求解变量。磁场矢势 $\mathbf{A}$ 和标量势 $\phi$ 可表示为：

$$\mathbf{A} = \mu \nabla \times \boldsymbol{\Pi}$$

$$\phi = -\nabla \cdot \boldsymbol{\Pi}$$

在 $N$ 层土壤中，第 $k$ 层的 Hertzian 矢量满足波动方程：

$$\nabla^2 \Pi_k + \gamma_k^2 \Pi_k = 0$$

其中 $\gamma_k = \sqrt{j\omega\mu_0(\sigma_k+j\omega\epsilon_k)}$ 为第 $k$ 层的传播常数。

**递归边界条件**：

通过逐层应用电磁场边界条件（切向 $E$ 和 $H$ 连续），Tsiamitros 等人推导出递归公式计算层间反射系数：

$$R_k = \frac{\gamma_{k+1}\Pi_{k+1} - \gamma_k\Pi_k}{\gamma_{k+1}\Pi_{k+1} + \gamma_k\Pi_k}$$

这些递归项最终进入互阻抗的半无限积分表达式中。对于架空导体与地下电缆的混合配置，互阻抗公式为：

$$Z_{mn} = \frac{j\omega\mu_0}{2\pi} \int_0^\infty \frac{e^{-(h_m+h_n)\lambda}}{\lambda + Z_\text{earth}^\text{eff}(\lambda)} \cos((x_m-x_n)\lambda) d\lambda$$

其中 $Z_\text{earth}^\text{eff}(\lambda)$ 是通过递归公式计算的有效土壤阻抗，包含了所有层的信息。

**数值积分方案**：

Tsiamitros 等人 2008 提出了一种自适应数值积分方案，对半无限区间上的复积分进行高效计算。在 Intel Pentium IV 2.66 GHz 处理器上，60 个阻抗矩阵的计算时间：
- 数值积分（容差 $10^{-4}$）：地下导体 < 15 min，架空线路 < 3 s
- FEM（相同精度）：约 180 min

**FEM 验证结果**：

Tsiamitros 等人 2008 Part II 使用有限元方法（FEM）验证了解析公式的精度。在 50 Hz 至 1 MHz 频率范围内：
- 架空线路 + 三层土壤：互阻抗幅值差异 < 0.3%
- 地下电缆 + 两层土壤：自阻抗幅值差异 < 0.4%
- 架空线路+地下电缆混合配置：所有阻抗幅值和相位差异 < 0.5%

**多层土壤的实际影响**：

Tsiamitros 等人 2008 Part II 发现，两层土壤模型与均匀土壤模型之间的阻抗差异可达 **38%**（最坏情况为两层土壤电阻率差异最大的 Case VI），差异在千赫兹频段达到最大——这直接影响开关暂态建模精度。差异在高频段趋于减小，因为趋肤效应使返回电流集中在表层。

## 形式化表达

### 核心公式汇总

| 公式 | 符号 | 适用场景 | 频率范围 |
|------|------|----------|----------|
| Carson 互阻抗 | $Z_{mn}^\text{earth} = \frac{j\omega\mu_0}{2\pi}[K_0(\gamma_0 D') - K_0(\gamma_0 D)]$ | 架空导体，均匀大地 | 工频–kHz |
| Pollaczek 积分 | $Z_{mm}^\text{earth} = \frac{j\omega\mu_0}{2\pi}\int_0^\infty\frac{e^{-2h\lambda}}{\lambda+Z_g/\mu_0}\frac{d\lambda}{\lambda}$ | 架空导体自阻抗 | 工频–kHz |
| Sunde 方程 | $Z_{mn} = \frac{j\omega\mu_0}{2\pi}[K_0(\gamma_1 d) - K_0(\gamma_1 D)]$ | 地下导体，均匀大地 | 工频–MHz |
| Xue–Magalhães | $Z_g = \frac{j\omega\mu_0}{2\pi}[K_0(\gamma_1 d) - K_0(\gamma_1 D) + \Theta]$ | 地下电缆，宽频带 | 工频–10 MHz |
| Saad–Gaba–Giroux | $Z_g \approx \frac{j\omega\mu_0}{2\pi}[K_0(\gamma_1 d) + \frac{e^{-H\gamma_1}}{4+\gamma_1^2 r^2}]$ | 紧密间距电缆 | < 100 kHz |
| De Conti–Lima | 见公式 (4)，三修正项 | 单/双回线电缆 | < 10 MHz |
| Tsiamitros 多层 | 递归边界 + 半无限积分 | 多层土壤，混合配置 | 工频–1 MHz |

### 大地趋肤深度

$$\delta = \sqrt{\frac{2}{\omega \mu_0 \sigma}}$$

典型值：$\sigma = 0.01$ S/m（中等电阻率土壤）时：
- 50 Hz: $\delta \approx 712$ m
- 1 kHz: $\delta \approx 225$ m
- 10 kHz: $\delta \approx 71$ m
- 100 kHz: $\delta \approx 22.5$ m
- 1 MHz: $\delta \approx 7.1$ m

### 大地传播常数

$$\gamma_1 = \sqrt{j\omega\mu_0(\sigma + j\omega\epsilon)} \approx \sqrt{j\omega\mu_0\sigma} \quad (\text{当 } \sigma \gg \omega\epsilon)$$

### 多层土壤递归参数

$$\eta_k = \frac{\gamma_{k+1}}{\gamma_k}, \quad \rho_k = \frac{\eta_k - 1}{\eta_k + 1}$$

层间反射系数递归传播，从最深层向表层递推。

## 关键技术挑战

### 1. 数值积分的稳定性

Carson 和 Pollaczek 公式中的半无限区间积分具有振荡被积函数，数值计算困难。ATP 的 Line and Cable Constants (LCC) 工具使用 Carson 积分的级数展开来计算 Pollaczek 积分。对于多层土壤模型，Tsiamitros 等人提出的自适应数值积分方案将容差设为 $10^{-4}$，计算时间从 FEM 的 180 min 降至 15 min（地下导体）或 3 s（架空线路）。

### 2. 土壤参数不确定性

De Conti & Lima 2026 指出，土壤参数（电阻率、介电常数）的不确定性远大于其他建模方面的影响。实际测量中，土壤电阻率可能随季节、湿度和温度变化 2–5 倍。Li 等人 2016 的研究表明，频率相关土壤模型（Alipio & Visacro 模型）与恒定参数模型在宽频带仿真中产生显著差异，特别是在雷电暂态分析中。

### 3. 高频极限

准-TEM 假设在频率高于 10 MHz 时失效。De Conti & Lima 2026 指出 10 MHz 是准-TEM 场传播的实际有效极限。超过此频率，需要考虑全波效应，如 Duarte 等人 2023 使用 FDTD 评估地下电缆传输线理论时所示。

### 4. 位移电流与接地返回导纳

在高频下，位移电流和接地返回导纳可能不可忽略。Tsiamitros 等人 2008 指出，相对土壤介电常数通常接近 10，但在频率低于 1 MHz 时对结果影响有限。

### 5. 非平行导体和三维效应

经典公式均假设无限长平行导体。有限长接地体、局部电缆附件和三维地质异常（如岩层、地下洞穴）超出标准公式适用范围。

## 量化性能边界

### 近似公式误差对比（De Conti & Lima 2026）

| 公式 | 参考基准 | 土壤电阻率 | 电缆间距 | 频率上限 | 最大误差 |
|------|----------|------------|----------|----------|----------|
| Saad–Gaba–Giroux | Sunde | 100 Ω·m | 3 m | 10 MHz | > 10% |
| Saad–Gaba–Giroux | Xue–Magalhães | 1000 Ω·m | 3 m | 10 MHz | > 20% |
| De Conti–Lima | Sunde | 100 Ω·m | 3 m | 10 MHz | < 2.5% |
| De Conti–Lima | Xue–Magalhães | 100 Ω·m | 3 m | 1 MHz | 5–10% |

### 多层土壤影响（Tsiamitros 2008 Part II）

| 配置 | 土壤模型 | 阻抗差异（最大） | 差异峰值频段 |
|------|----------|------------------|--------------|
| 150 kV 单回线 | 两层土壤 vs 均匀 | < 0.3% | — |
| 735 kV 双回线 | 两层土壤 vs 均匀 | < 0.3% | — |
| 单层电缆 | 两层土壤 vs 均匀 | 最高 38% | kHz 频段 |
| 架空+地下混合 | 两层土壤 vs 均匀 | < 0.5% | — |

### FEM 验证精度（Tsiamitros 2008 Part II）

| 配置 | 频率范围 | 幅值差异 | 相位差异 |
|------|----------|----------|----------|
| 架空线路 + 三层土壤 | 50 Hz–1 MHz | < 0.3% | < 0.3% |
| 地下电缆 + 两层土壤 | 50 Hz–1 MHz | < 0.4% | < 0.4% |
| 架空+地下混合 | 50 Hz–1 MHz | < 0.5% | < 0.5% |

### 计算效率（Tsiamitros 2008 Part II）

| 方法 | 架空线路 | 地下导体 | 说明 |
|------|----------|----------|------|
| 数值积分（容差 $10^{-4}$） | < 3 s | < 15 min | 60 个阻抗矩阵，Intel Pentium IV 2.66 GHz |
| FEM | ~3 s | ~180 min | 相同精度 |
| 容差 $10^{-5}$ | < 3 s | < 8 min | 地下导体计算时间减少 |

## 适用边界与选择指南

### 公式选择决策表

| 应用场景 | 推荐公式 | 频率范围 | 注意事项 |
|----------|----------|----------|----------|
| 架空线路工频零序参数 | Carson 公式 | 50/60 Hz | 均匀大地假设，足够精确 |
| 架空线路宽频参数 | Carson + 数值积分 | 50 Hz–100 kHz | 需处理半无限积分 |
| 地下电缆紧密间距 | Saad–Gaba–Giroux | < 100 kHz | ATPDraw 内置，低电阻率土壤 |
| 地下电缆宽频（单/双回线） | De Conti–Lima | < 10 MHz | 推荐用于宽频带电缆模型 |
| 地下电缆基准计算 | Xue–Magalhães | < 10 MHz | 计算量大，作为验证基准 |
| 多层土壤（两层/三层） | Tsiamitros 递归公式 | 50 Hz–1 MHz | 需要土壤分层参数 |
| 多层土壤快速近似 | 多层 earth 均匀近似 | < 100 kHz | 精度损失可达 38% |
| 全波频段（> 10 MHz） | FDTD 全波方法 | > 10 MHz | Duarte 2023，计算成本高 |

### 失效场景

- **全波效应**：频率 > 10 MHz 时准-TEM 假设失效，需全波方法
- **三维地质异常**：岩层、地下洞穴、不均匀地质体超出分层土壤模型
- **有限长接地体**：经典公式假设无限长导体，不适用于局部接地系统
- **非平行导体**：交叉线路、倾斜电缆超出标准公式适用范围
- **极端土壤参数**：极高电阻率（> 10000 Ω·m）或导电性异常区域

## 与相关页面的关系

- [[mutual-impedance]] 使用地回路项解释导体间耦合
- [[frequency-dependent-soil]] 和 [[frequency-dependent-soil-model]] 描述土壤参数随频率变化
- [[cable-model]]、[[grounding-system-model]] 和 [[transmission-line-model]] 是主要应用对象
- [[distributed-parameter-line]] 中地回路阻抗构成串联阻抗矩阵的一部分
- [[frequency-dependent-line-model]] 利用频变地回路阻抗构建宽频电缆模型
- [[vector-fitting]] 可将频域地回路阻抗转换为时域可实现模型
- [[frequency-scan]] 可用于检查等效参数对系统频响的影响
- [[modal-transformation]] 依赖准确的地回路阻抗进行模态分解
- [[phase-domain-modeling]] 中地回路阻抗直接影响相域参数矩阵

## 修订与证据使用注意事项

后续不要直接写固定"适用频率范围"或"误差小于某百分比"，除非已核对原始论文、标准或工具手册。涉及 Carson、Pollaczek、Sunde、Wedepohl、Xue–Magalhães 等公式时，应说明它们的假设，而不是把名字作为精度背书。De Conti & Lima 2026 的误差分析表明，同一公式在不同土壤电阻率和电缆间距下的误差可能从 2.5% 变化到 20% 以上，因此必须结合具体应用场景评估精度。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 480" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
    <marker id="arrow-red" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#dc2626"/>
    </marker>
  </defs>
  
  <!-- Title -->
  <text x="450" y="28" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">地回路阻抗计算方法体系</text>
  
  <!-- Layer 1: Input -->
  <rect x="330" y="48" width="240" height="44" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="450" y="75" text-anchor="middle" font-size="13" fill="#2563eb" font-weight="bold">输入：导体配置 + 土壤参数</text>
  
  <!-- Arrow down -->
  <line x1="450" y1="92" x2="450" y2="115" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Layer 2: Method selection -->
  <rect x="30" y="118" width="240" height="44" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="150" y="138" text-anchor="middle" font-size="12" fill="#16a34a" font-weight="bold">均匀大地模型</text>
  <text x="150" y="154" text-anchor="middle" font-size="11" fill="#16a34a">Carson / Sunde / Pollaczek</text>
  
  <rect x="330" y="118" width="240" height="44" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="450" y="138" text-anchor="middle" font-size="12" fill="#16a34a" font-weight="bold">多层土壤模型</text>
  <text x="450" y="154" text-anchor="middle" font-size="11" fill="#16a34a">Tsiamitros Hertzian 递归</text>
  
  <rect x="630" y="118" width="240" height="44" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="750" y="138" text-anchor="middle" font-size="12" fill="#16a34a" font-weight="bold">全波模型</text>
  <text x="750" y="154" text-anchor="middle" font-size="11" fill="#16a34a">FDTD 全波 (Duarte 2023)</text>
  
  <!-- Arrows down -->
  <line x1="150" y1="162" x2="150" y2="185" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="450" y1="162" x2="450" y2="185" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="750" y1="162" x2="750" y2="185" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Layer 3: Algorithms -->
  <rect x="10" y="188" width="280" height="44" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="150" y="206" text-anchor="middle" font-size="11" fill="#d97706" font-weight="bold">闭合形式近似</text>
  <text x="150" y="222" text-anchor="middle" font-size="10" fill="#d97706">Saad-Gaba-Giroux / De Conti-Lima</text>
  
  <rect x="310" y="188" width="280" height="44" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="450" y="206" text-anchor="middle" font-size="11" fill="#d97706" font-weight="bold">数值积分</text>
  <text x="450" y="222" text-anchor="middle" font-size="10" fill="#d97706">半无限区间自适应积分</text>
  
  <rect x="610" y="188" width="280" height="44" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="750" y="206" text-anchor="middle" font-size="11" fill="#d97706" font-weight="bold">有限元法</text>
  <text x="750" y="222" text-anchor="middle" font-size="10" fill="#d97706">FEM / FDTD 离散求解</text>
  
  <!-- Arrows down -->
  <line x1="150" y1="232" x2="150" y2="255" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="450" y1="232" x2="450" y2="255" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="750" y1="232" x2="750" y2="255" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Layer 4: Output -->
  <rect x="10" y="258" width="280" height="44" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="150" y="278" text-anchor="middle" font-size="11" fill="#7c3aed" font-weight="bold">Z_earth(ω) 近似公式</text>
  <text x="150" y="294" text-anchor="middle" font-size="10" fill="#7c3aed">误差 &lt; 2.5% (De Conti-Lima)</text>
  
  <rect x="310" y="258" width="280" height="44" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="450" y="278" text-anchor="middle" font-size="11" fill="#7c3aed" font-weight="bold">Z_earth(ω) 数值解</text>
  <text x="450" y="294" text-anchor="middle" font-size="10" fill="#7c3aed">误差 &lt; 0.4% (vs FEM)</text>
  
  <rect x="610" y="258" width="280" height="44" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="750" y="278" text-anchor="middle" font-size="11" fill="#7c3aed" font-weight="bold">Z_earth(ω) 全波解</text>
  <text x="750" y="294" text-anchor="middle" font-size="10" fill="#7c3aed">&gt; 10 MHz 频段</text>
  
  <!-- Arrow down -->
  <line x1="150" y1="302" x2="150" y2="325" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="450" y1="302" x2="450" y2="325" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="750" y1="302" x2="750" y2="325" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Layer 5: Final output -->
  <rect x="200" y="328" width="500" height="44" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="450" y="355" text-anchor="middle" font-size="13" fill="#7c3aed" font-weight="bold">单位长度串联阻抗矩阵 Z'(ω) → EMT 仿真</text>
  
  <!-- Frequency range labels -->
  <text x="150" y="385" text-anchor="middle" font-size="10" fill="#666">低频 &lt; 100 kHz</text>
  <text x="450" y="385" text-anchor="middle" font-size="10" fill="#666">宽频 50 Hz–1 MHz</text>
  <text x="750" y="385" text-anchor="middle" font-size="10" fill="#666">全波 &gt; 10 MHz</text>
  
  <!-- Key data callouts -->
  <rect x="10" y="400" width="430" height="60" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1" stroke-dasharray="4,2"/>
  <text x="20" y="418" font-size="10" fill="#d97706">精度对比：</text>
  <text x="20" y="434" font-size="10" fill="#d97706">De Conti-Lima: &lt; 2.5% (100 Ω·m, 10 MHz)</text>
  <text x="20" y="448" font-size="10" fill="#d97706">Saad-Gaba-Giroux: &gt; 20% (1000 Ω·m, 10 MHz)</text>
  
  <rect x="450" y="400" width="430" height="60" rx="4" fill="#fee2e2" stroke="#dc2626" stroke-width="1" stroke-dasharray="4,2"/>
  <text x="460" y="418" font-size="10" fill="#dc2626">多层土壤影响：</text>
  <text x="460" y="434" font-size="10" fill="#dc2626">两层土壤 vs 均匀土壤差异最高 38%</text>
  <text x="460" y="448" font-size="10" fill="#dc2626">差异峰值在 kHz 频段（开关暂态关键）</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 地回路阻抗计算方法体系：从导体配置输入到阻抗矩阵输出的完整流程，展示均匀大地与多层土壤两大分支及其子方法</p>

## 相关方法

- [[distributed-parameter-line]]
- [[frequency-dependent-line-model]]
- [[mutual-impedance]]
- [[frequency-dependent-soil]]
- [[frequency-dependent-soil-model]]
- [[cable-model]]
- [[grounding-system-model]]
- [[transmission-line-model]]
- [[vector-fitting]]
- [[frequency-scan]]
- [[modal-transformation]]
- [[phase-domain-modeling]]
- [[bergeron-line-model]]
- [[pi-model]]
- [[characteristic-method]]

## 来源论文

- **Tsiamitros, Papagiannis & Dokopoulos 2008 (Part I)** — 提出多层土壤中架空和地下导体地回路阻抗的统一理论框架，基于 Hertzian 矢量和递归边界条件推导广义自/互阻抗公式，适用于任意导体拓扑和 N 层土壤结构。IEEE TPWRD, Vol. 23, No. 4, pp. 2392–2401. DOI: 10.1109/TPWRS.2008.923816

- **Tsiamitros, Papagiannis & Dokopoulos 2008 (Part II)** — 数值验证 Part I 理论，使用 FEM 在 50 Hz–1 MHz 范围内验证解析公式精度（差异 < 0.3–0.5%），展示两层/三层土壤与实际架空线路和电缆配置的结合，发现多层土壤与均匀土壤阻抗差异最高达 38%。IEEE TPWRD, Vol. 23, No. 4, pp. 2401–2408. DOI: 10.1109/TPWRS.2008.923999

- **De Conti & Lima 2026** — 系统评估 Saad–Gaba–Giroux 和 De Conti–Lima 闭合形式近似公式的精度，以 Sunde 方程和 Xue–Magalhães 方程为基准，证明 De Conti–Lima 公式在 100 Ω·m 土壤中误差 < 2.5%（高达 10 MHz，电缆间距 3 m），而 Saad–Gaba–Giroux 在 1000 Ω·m 土壤中误差 > 20%。Electric Power Systems Research 250 (2026) 112146. DOI: 10.1016/j.epsr.2025.112146

- **Li et al. 2016** — 研究土壤参数频率特性对地回路输电线路参数的影响，表明频率相关土壤模型（Alipio & Visacro）与恒定参数模型在宽频带仿真中产生显著差异。

- **Duarte et al. 2021** — 扩展 Vance 闭合形式近似以计算多导体系统的地导纳，考虑更复杂的导体排列和土壤参数。

- **Duarte et al. 2023** — 使用全波 FDTD 评估地下电缆传输线理论，展示在 > 10 MHz 频段准-TEM 假设的局限性。

- **Magalhães et al. / Xue et al.** — 提出准-TEM 框架下的地下电缆地回路阻抗最严格表达式，考虑空气和大地两种介质的传播常数，是宽频带电缆参数计算的基准参考。
