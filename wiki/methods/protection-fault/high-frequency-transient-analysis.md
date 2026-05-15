---
title: "高频暂态分析 (High-frequency Transient Analysis)"
type: method
tags: [high-frequency, transient, lightning, switching, surge, frequency-dependent]
created: "2026-05-02"
updated: "2026-05-15"
---

# 高频暂态分析 (High-frequency Transient Analysis)

## 定义

高频暂态分析是在电磁暂态（EMT）仿真中研究快速电磁过程、宽频传播、反射、耦合和局部过电压的方法论领域。它覆盖从直流稳态到数兆赫兹的宽频带，研究对象包括雷电波头（ns~μs级）、开关陡波（μs级）、断路器重燃、电缆/GIS/变压器内部波过程、接地冲击响应和电磁干扰等问题。与工频阻抗分析不同，高频暂态分析需要显式处理**频变损耗**、**波过程**和**数值稳定性**三要素。

在EMT知识体系中，高频暂态分析是连接**线路建模**（[[frequency-dependent-line-model]]、[[universal-line-model]]）、**接地系统**（[[grounding-system-modeling]]）、**保护设备**（[[surge-arrester-model]]）和**绝缘配合**（[[insulation-coordination]]）的枢纽——它回答的是"这些元件模型在目标频带内是否有效"这一核心问题。

## EMT中的角色

高频暂态分析在EMT仿真中承担**频域有效性验证**和**宽频建模指导**双重职责：

1. **模型有效性判据**：线路、电缆、接地和设备模型是否在目标频带内有效。高频暂态不能只用工频阻抗描述，因为传输线和电缆的阻抗、导纳参数具有强频率依赖性。
2. **波过程追踪**：波在阻抗不连续点、分支、接地箱、变压器端口和避雷器处的反射与折射行为。
3. **参数敏感性**：频变损耗、土壤参数、护套/铠装和设备杂散参数对峰值、陡度和振荡的影响。
4. **数值步长决策**：时间步长、延时插值、有理拟合和无源性处理是否足以支撑目标波形。

**典型应用场景**：
- 雷电直击或感应过电压下线路绝缘配合分析
- 开关操作引起的操作过电压评估
- 电缆/GIS内部波过程与设备端口应力分析
- 接地冲击阻抗与大地电位升（GPR）计算

## 核心机制

### 1. 频变传输线端口关系

高频暂态分析的基本方程是频域端口关系。对于多导体传输线，频域电压-电流关系可写为：

$$\mathbf{i}(\omega) = \mathbf{Y}(\omega) \mathbf{v}(\omega)$$

其中 $\mathbf{Y}(\omega)$ 是节点导纳矩阵，$\mathbf{v}(\omega)$ 和 $\mathbf{i}(\omega)$ 分别是端口电压和注入电流的频域向量。

传播函数矩阵 $\mathbf{H}(\omega)$ 描述行波从线路一端到另一端的传播特性：

$$\mathbf{H}(\omega) = e^{-\ell \sqrt{\mathbf{Z}'(\omega) \mathbf{Y}'(\omega)}}$$

其中 $\ell$ 为线路长度，$\mathbf{Z}'(\omega)$ 和 $\mathbf{Y}'(\omega)$ 分别是单位长度串联阻抗矩阵和并联导纳矩阵。传播常数 $\boldsymbol{\gamma}(\omega) = \sqrt{\mathbf{Z}'(\omega) \mathbf{Y}'(\omega)}$ 包含集肤效应、邻近效应、介质损耗、大地返回路径和接地/护套耦合等因素。

### 2. 宽频有理函数拟合

将频域函数转换为时域卷积是EMT实现的关键步骤。宽频函数通常需有理拟合才能进入时域状态空间或递归卷积形式：

$$\hat{F}(s) = D + \sum_{r=1}^{N} \frac{R_r}{s - p_r}$$

其中 $R_r$ 为留数（residue），$p_r$ 为极点（pole），$D$ 为直接项（scalar term），$N$ 为拟合阶数。该形式可通过部分分式展开转化为状态空间方程或递推卷积历史项。

**Vector Fitting（VF）** 是目前EMT领域最广泛使用的有理拟合方法，其本质是迭代求解极点位置使拟合误差在频域最小化。对于传播函数 $H(s)$，VF拟合形式为：

$$H(s) \approx \sum_{i=1}^{N_{grp}} \left( \sum_{m=1}^{M_i} \frac{R_{i,m}}{s - p_{i,m}} \right) e^{-s \tau_i}$$

其中 $N_{grp}$ 为模态组数，$M_i$ 为第 $i$ 组的逼近阶数，$\tau_i$ 为模态传播时延。指数项 $e^{-s\tau_i}$ 反映行波传播的延迟特性。

### 3. 场路耦合接口

对于外部电磁场耦合问题（如雷击感应电压），入射场需转换为线路端口等效源。De Conti & Leal（2026）提出的方法是：把外部雷电电磁场对多导体线路的耦合效应完全等效为连接在线路两端的独立Norton电流源：

$$\mathbf{j}_0(t) = \mathbf{y}_c(t) * \overline{\mathbf{u}}_0(t)$$

$$\mathbf{j}_\ell(t) = \mathbf{y}_c(t) * \overline{\mathbf{u}}(t)$$

其中 $\mathbf{y}_c(t)$ 是特征导纳的时域响应（通过有理拟合从 $Y_c(\omega)$ 获得），$*$ 表示卷积运算。修正电压源 $\overline{\mathbf{u}}_0(t)$ 和 $\overline{\mathbf{u}}(t)$ 通过递归方程计算：

$$\overline{\mathbf{u}}_0(t) = \mathbf{u}_0(t) - \mathbf{a}(t) * \overline{\mathbf{u}}(t)$$

$$\overline{\mathbf{u}}(t) = \mathbf{u}(t) - \mathbf{a}(t) * \overline{\mathbf{u}}_0(t)$$

其中 $\mathbf{a}(t)$ 是传播函数 $H(\omega)$ 的时域对应，$\mathbf{u}_0(t)$ 和 $\mathbf{u}(t)$ 是由入射电场积分得到的等效电压源。这些电流源对给定雷击事件仅需离线计算一次，不随终端负载或非线性元件状态变化。

### 4. 直流校正与分频段拟合

传统ULM拟合面临的一个挑战是直流（DC）附近的拟合精度。 Camilo（2020）提出的FDM/DC（Frequency Dependent Model with DC correction）方法通过分频段策略解决此问题：

1. **高频段拟合**（排除接近DC的样本）：对传播函数 $H(s)$ 进行标准ULM有理拟合，获得主要动态特性

$$\tilde{H}_{HF}(s) \approx \sum_{i=1}^{N_{grp}} \left( \sum_{m=1}^{M_i} \frac{R_{i,m}^{HF}}{s - p_{i,m}^{HF}} \right) e^{-s \tau_i}$$

2. **低频误差提取**：在低频样本点 $s_{LF}$ 处计算拟合误差

$$\Delta H_{LF} = H_{LF} - \tilde{H}_{HF}(s_{LF})$$

3. **直流校正项拟合**：对误差函数进行低阶有理函数拟合

$$\tilde{H}_{LF}(s) \approx \sum_{k=1}^{N_{dc}} \frac{R_k^{dc}}{s - p_k^{dc}}$$

其中 $N_{dc}$ 通常远小于主模型阶数（1~3阶）。最终合成传播函数为：

$$H_{final}(s) = \tilde{H}_{HF}(s) + \tilde{H}_{LF}(s)$$

这种分区策略避免了为捕捉DC响应而产生的大留数/极点比问题，显著提高时域数值稳定性。

### 5. 双有损介质埋设海缆建模

海底埋设电缆的建模需要同时考虑**海水**和**海床双损耗介质**。 Camara（2024）基于准TEM近似提出两种时域实现路径：

**方法一：特征线法（MoC）+ ULM**

对传播函数进行模态分解，提取模态时延 $\tau_i$，通过Vector Fitting对模态传播函数和特征导纳分别拟合。电缆单位长度参数由内部阻抗和外部介质阻抗叠加：

$$\mathbf{Z} = \mathbf{Z}_{in} + \mathbf{Z}_0$$

其中外部阻抗 $z_0$ 基于Sommerfeld积分和准TEM近似计算：

$$z_0 = \frac{j\omega\mu_0}{2\pi} \left[ K_0(\gamma_1 r) + K_0(\gamma_1 \sqrt{4h^2 + r^2}) + S_1 \right]$$

这里 $K_0$ 为修正Bessel函数，$\gamma_1$ 为介质传播常数，$h$ 为埋设深度，$S_1$ 为Sommerfeld积分项。

**方法二：折叠线等效（FLE）**

直接构造整段电缆的节点导纳矩阵 $\mathbf{Y}_n$，通过FLE分解将 $\mathbf{Y}_n$ 变换为开路导纳 $\mathbf{Y}_{oc}$ 和短路导纳 $\mathbf{Y}_{sc}$ 两部分分别拟合：

$$\mathbf{Y}_n = \mathbf{K} \begin{bmatrix} \mathbf{Y}_{oc} & 0 \\ 0 & \mathbf{Y}_{sc} \end{bmatrix} \mathbf{K}^{-1}$$

这种分解避免了直接拟合完整 $2n \times 2n$ 节点导纳时不同特征值尺度混在一起的问题，尤其改善低频小特征值的数值处理。

### 6. 频变土壤参数与地回路阻抗

Li等（2016）指出土壤电阻率和介电常数均随频率升高呈显著下降趋势。完整复穿透深度公式综合考虑土壤电导率与介电常数：

$$p = \frac{1}{\sqrt{j\omega\mu(\sigma + j\omega\varepsilon)}}$$

基于复穿透深度的复返回平面法自阻抗和互阻抗公式为：

$$Z_{ii} = j\omega \frac{\mu_0}{2\pi} \ln \frac{2(h_i + p)}{r}$$

$$Z_{ij} = j\omega \frac{\mu_0}{2\pi} \ln \frac{\sqrt{(h_i + h_j + 2p)^2 + d_{ij}^2}}{\sqrt{(h_i - h_j)^2 + d_{ij}^2}}$$

其中 $h_i$ 为导线高度，$r$ 为导线半径，$d_{ij}$ 为导线间距。**关键发现**：50 Hz恒定参数模型在高频暂态分析中误差最大；1 MHz恒定参数模型的计算结果最逼近全频变模型，可作为高频电磁暂态仿真的有效近似。

## 形式化表达

### 核心方程汇总

**频域端口关系**

$$\mathbf{i}(\omega) = \mathbf{Y}(\omega) \mathbf{v}(\omega)$$

$$\mathbf{H}(\omega) = e^{-\ell \sqrt{\mathbf{Z}'(\omega) \mathbf{Y}'(\omega)}}$$

**Vector Fitting通用形式**

$$\hat{F}(s) = D + \sum_{r=1}^{N} \frac{R_r}{s - p_r}$$

**传播函数ULM形式**

$$H(s) \approx \sum_{i=1}^{N_{grp}} \left( \sum_{m=1}^{M_i} \frac{R_{i,m}}{s - p_{i,m}} \right) e^{-s\tau_i}$$

**场路耦合电流源（Norton等效）**

$$\mathbf{j}_0(t) = \mathbf{y}_c(t) * \overline{\mathbf{u}}_0(t)$$

**修正电压源递归方程**

$$\overline{\mathbf{u}}_0(t) = \mathbf{u}_0(t) - \mathbf{a}(t) * \overline{\mathbf{u}}(t)$$

**直流校正分频段拟合**

$$\tilde{H}_{HF}(s) \approx \sum_{i=1}^{N_{grp}} \left( \sum_{m=1}^{M_i} \frac{R_{i,m}^{HF}}{s - p_{i,m}^{HF}} \right) e^{-s\tau_i}$$

$$\Delta H_{LF} = H_{LF} - \tilde{H}_{HF}(s_{LF})$$

$$H_{final}(s) = \tilde{H}_{HF}(s) + \tilde{H}_{LF}(s)$$

**双有损介质外部阻抗**

$$z_0 = \frac{j\omega\mu_0}{2\pi} \left[ K_0(\gamma_1 r) + K_0(\gamma_1 \sqrt{4h^2 + r^2}) + S_1 \right]$$

**复穿透深度公式**

$$p = \frac{1}{\sqrt{j\omega\mu(\sigma + j\omega\varepsilon)}}$$

**复返回平面法阻抗**

$$Z_{ii} = j\omega \frac{\mu_0}{2\pi} \ln \frac{2(h_i + p)}{r}$$

## 关键技术挑战

### 挑战1：频域参数测量与提取

高频暂态分析的精度直接取决于输入参数的频域覆盖范围。土壤参数（电阻率、介电常数）、电缆参数（铠装磁导率、护套电阻率）和设备参数（端口杂散电容、引线电感）均需在目标频带内进行测量或计算。实测挑战包括：
- 宽带介电谱测量需要专用仪器（0.1 Hz ~ 10 MHz甚至更高）
- 土壤参数受湿度、温度、粒径影响显著，同一场地不同时间的测量结果可能差异较大
- 电缆铠装钢材料的磁导率在高频下呈现非线性（相对磁导率从静态值90左右下降至高频下接近真空值1）

**应对策略**：优先使用论文中已有测试数据（如Li 2016的500 kV线路参数、Camara 2024的75 kV海缆参数），在缺少直接测量数据时采用文献中的典型值并标注不确定性。

### 挑战2：Vector Fitting阶数与稳定性

VF拟合阶数直接影响计算精度和数值稳定性。阶数过低导致拟合精度不足，阶数过高则引入病态极点-留数组合，可能导致时域不稳定。此外，模态组数的选择需要平衡拟合精度与计算效率。

**应对策略**：采用分区拟合策略（如FDM/DC），将DC/低频与高频分离建模，避免用单一高频模型强行拟合全频段。拟合后需检查留数/极点比是否在合理范围内。

### 挑战3：数值步长与插值精度

高频暂态的波过程时间常数在ns~μs级，要求EMT仿真步长足够小以解析最高频率分量。对于延时有理函数形式 $e^{-s\tau_i}$，当 $\tau_i$ 不是步长 $\Delta t$ 的整数倍时，需要延时插值处理。常用方案包括：
- **双段插值（two-segment interpolation）**：在两个相邻步长点之间插值
- **分数延时滤波**：用All-pass滤波器逼近非整数延时

步长设置需满足：$\Delta t \leq \min(\tau_{fastest}) / 10$，其中 $\tau_{fastest}$ 为最快相关波形的特征时间常数。

### 挑战4：多频段模型接口与一致性

当系统包含多个频变模型（如JMarti线路模型+避雷器模型+变压器高频模型）时，各模型的频率覆盖范围、拟合频段和无源性处理方式可能不一致。多模型接口可能导致：
- 不同模型在重叠频段内的响应不一致
- 接口处注入/抽出电流的不连续导致数值振荡
- 无源性违背后造成的数值不稳定（尤其在互联多个宽频模型时）

**应对策略**：在仿真前对各模型进行无源性检查和频段一致性验证，必要时在接口处添加缓冲网络或采用伴随电路模型确保端口匹配。

### 挑战5：雷电场耦合的预先计算假设

雷击感应电压分析中，外部场源通常假定可预先计算（基于雷电通道模型和电磁场积分公式）作为独立源注入EMT网络。这一假设的局限性在于：
- 直击导线、电弧和强非线性反馈可能超出该假设适用范围
- 避雷器等非线性元件的状态变化不会反向影响场源计算
- 多雷击场景下，每次雷击事件需要重新计算场源

**适用边界**：该方法适用于评估附近云地雷击引起的感应过电压场景，特别适合含分支、接地点、避雷器的配电网参数扫描研究。

## 量化性能边界

| 指标 | 数值 | 条件 | 来源 |
|------|------|------|------|
| 低压负荷首峰误差（频变损耗忽略） | **28%** | 土壤电阻率100 Ωm，中压主干线1.26 km | De Conti & Leal 2026 |
| 低压负荷首峰误差（频变损耗忽略） | **18%** | 土壤电阻率1000 Ωm，同算例 | De Conti & Leal 2026 |
| 避雷器保护水平 | < **30 kV**（相地过电压） | P4节点，频变模型，土壤1000 Ωm | De Conti & Leal 2026 |
| 拟合频率范围 | 0.1 Hz ~ **10 MHz**（20点/十倍频） | ATP内置VF工具，参考频率60 kHz | De Conti & Leal 2026 |
| 仿真步长 | **10 ns**，总时长80 μs | 雷电暂态仿真 | De Conti & Leal 2026 |
| 低频段范围 | 0.001 Hz ~ 1 Hz | FDM/DC第一阶段排除的频段 | Camilo 2020 |
| 高频段范围 | 1 Hz ~ 1 MHz（可扩展） | FDM/DC第一阶段拟合频段 | Camilo 2020 |
| 直流校正项阶数 | 1~3阶（远小于主模型） | FDM/DC第二阶段校正函数 | Camilo 2020 |
| 海缆拟合精度 | 与NLT基准**高度一致** | MoC/ULM和FLE两种方法对比 | Camara 2024 |
| 海缆埋深 | 1 m（典型），最深>5 m | 海上风电场景，水深17~30 m | Camara 2024 |
| 土壤自阻差异敏感频段 | **>1 kHz** | 频变土壤模型 vs 恒定参数模型 | Li et al 2016 |
| 土壤自感差异敏感频段 | **<1 MHz** | 频变土壤模型 vs 恒定参数模型 | Li et al 2016 |
| 最优恒定参数近似 | **1 MHz** | 逼近全频变模型精度最高 | Li et al 2016 |

**注**：上述量化数据均来自论文原文。原文未报告可核验数值结果的场景标注为"原文未报告可核验的数值结果"。

## 适用边界与选择指南

### 建模方法选择

| 场景 | 推荐模型 | 不适用场景 | 说明 |
|------|----------|------------|------|
| 雷电感应电压（配电网） | JMarti频变模型 + Norton电流源等效 | 无损Bergeron模型 | 频变损耗使低压侧首峰误差达28% |
| 宽频线路/电缆EMT | FDM/DC分区拟合 | 强制全频段VF拟合 | 避免大留数/极点比导致的数值不稳定 |
| 海底埋设电缆（双有损介质） | MoC/ULM 或 FLE | 单有损介质电缆模型 | 双有损介质（海水+海床）需要准TEM参数化 |
| 土壤频变对接地阻抗影响 | 复穿透深度 + 复返回平面法 | 50 Hz恒定土壤参数 | 1 MHz恒定参数近似精度最优 |
| 开关/操作过电压 | 频变线路 + 避雷器AVM | 常参数Bergeron | 需要覆盖kHz~MHz频段 |
| 变压器端口振荡 | 高频白盒变压器模型 | 工频变压器等效 | 端口杂散参数决定高频响应 |

### 常见失败模式

1. **步长足够但模型频带不足**：使用常参数Bergeron模型分析雷电暂态时，忽略了频变衰减和土壤损耗，可能导致远端节点过电压被严重高估（如无损模型在100 Ωm土壤下误差达28%）。

2. **只用峰值评估绝缘配合**：若只报告峰值而不报告波形、端口定义和模型边界，绝缘配合结论不可复核。需同时关注波形陡度、振荡频率和持续时间。

3. **外部场源等效的静态假设**：对于直击导线或强非线性反馈场景（如金属氧化物避雷器在雷击下的导通），电流源等效可能不成立。

4. **高频接地引线的传输线效应**：当引线长度与最高频率分量波长的 $1/4$ 可比时，引线本身应作为传输线建模而非集总参数元件。

5. **多宽频模型互联的无源性**：多个有理模型直接互联后，整体系统可能丧失无源性，导致数值不稳定。需进行全系统无源性检查。

## 分析流程

1. **定义目标现象**：雷电、开关陡波、重燃、护套过电压、GPR、GIS/变压器端口振荡或感应电压。

2. **确定有效频带和指标**：峰值、陡度、到达时间、振荡频率、能量、端口间电压或设备内部应力。

3. **选择模型**：根据场景从以下选项中选择：
   - 架空线：[[frequency-dependent-line-model]]、[[universal-line-model]]、JMarti频变模型
   - 电缆：[[underground-cable-modeling]]、双有损介质海缆模型
   - 接地：[[grounding-system-modeling]]、复穿透深度模型
   - 变压器：高频白盒模型
   - 避雷器：[[surge-arrester-model]]非线性模型

4. **处理宽频参数**：
   - 频率采样：0.1 Hz至目标最高频率（20点/十倍频）
   - 参数测量/计算：土壤频变参数、缆参数、杂散参数
   - [[vector-fitting]]：拟合传播函数和特征导纳
   - 低频/DC校正：FDM/DC或其他分区拟合策略
   - 无源性和因果性检查

5. **设置数值步长**：保证事件时刻、延时插值、开关动作和最快相关波形能被解析。建议 $\Delta t \leq \min(\tau_{fastest}) / 10$。

6. **敏感性分析**：对以下参数进行扫描：
   - 土壤电阻率（100 Ωm、1000 Ωm等典型值）
   - 电缆接地方式
   - 避雷器参数
   - 端接阻抗
   - 线路分段
   - 拟合阶数和步长

7. **结果验证**：将结论绑定到模型边界，不把单一算例外推为系统通用规律。

## 常见模型与接口

| 对象 | 高频关键点 | 相邻页面 |
|------|------------|----------|
| 架空线/配电线 | 地模损耗、分支反射、外部场耦合 | [[lightning-transient-analysis]] |
| 地下/海底电缆 | 护套/铠装、介质损耗、短线步长约束 | [[underground-cable-modeling]] |
| 接地系统 | 冲击阻抗、频变土壤、GPR、多端口耦合 | [[grounding-system-modeling]] |
| 避雷器/SPD | 非线性残压、能量、引线电感 | [[surge-arrester-model]] |
| 变压器/GIS | 端口杂散参数和内部波过程 | [[frequency-dependent-modeling]] |

## 相关方法

- [[lightning-transient-analysis]] — 高频暂态中的雷电专页
- [[switching-transient]] — 开关、重燃和操作过电压
- [[insulation-coordination]] — 使用高频暂态结果做设备和保护配置判断
- [[earth-return-impedance]] — 地模/土壤参数基础
- [[frequency-dependent-soil]] — 频变土壤参数
- [[frequency-dependent-soil-model]] — 频变土壤建模方法
- [[universal-line-model]] — 通用线路模型的时域接口
- [[bergeron-line-model]] — Bergeron模型的时域实现
- [[frequency-dependent-line-model]] — 频变线路模型入口
- [[vector-fitting]] — 有理函数拟合方法

## 来源论文

- [[calculation-of-lightning-induced-voltages-on-a-large-scale-distribution-network-]] — De Conti & Leal 2026，JMarti频变模型雷击感应电压场路耦合方法，含配电网节点电压量化误差
- [[partitioned-fitting-and-dc-correction-in-transmission-linecable-models-for-wideb]] — Camilo 2020，FDM/DC分区拟合与直流校正方法，解决宽频ULM低频数值稳定性问题
- [[time-domain-modeling-of-a-subsea-buried-cable]] — Camara 2024，双有损介质海底电缆时域建模（MoC/ULM + FLE），与NLT基准高度一致
- [[influence-of-frequency-characteristics-of-soil-on-lightning-transient-response-o]] — Li et al 2016，频变土壤参数对地回路阻抗的影响，量化1 kHz以上自阻差异和1 MHz以下自感差异