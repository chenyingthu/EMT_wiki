---
title: "新能源机组 (Renewable Energy Units)"
type: topic
tags: [renewable-energy, wind-power, pv, inverter, grid-connection, low-voltage-ride-through, grid-forming, grid-following]
created: "2026-05-02"
updated: "2026-05-14"
---

# 新能源机组 (Renewable Energy Units)

## 定义

新能源机组是指将风能、太阳能或储能侧化学/物理能量转换为交流并网功率的单机物理对象，是电力系统 EMT 仿真中最基本的"电力电子化能源"建模单元。其典型结构包含三个逻辑层级：

- **能源侧**：风机叶片-传动链-发电机（DFAG/PMSG）、光伏阵列（单二极管等效电路）、储能电池（电化学等效电路）
- **直流链路**：DC/DC 变换器（升降压、MPPT 控制）、直流母线电容、电压外环
- **交流并网接口**：并网逆变器（两电平/三电平/多电平）、L/LC/LCL 滤波器、锁相环（PLL）、电流控制器、故障穿越（FRT）逻辑

本页聚焦**机组级 EMT 模型**，关注功率器件开关、控制器、直流侧动态和保护逻辑在微秒至毫秒时间尺度上的相互作用。不讨论场站级聚合、集电网络拓扑、政策或容量统计——这些由 [[pv-power-plant]] 和 [[renewable-energy-integration]] 覆盖。

新能源机组与常规同步发电机组的根本区别在于：其并网功率不再由电磁转矩和机械惯性直接决定，而是由**控制器指令 + 电力电子开关 + 直流侧能量约束**共同决定。这导致故障期间的电流响应不再服从同步机的短路规律，而需通过详细的电流源型等效或开关级拓扑来表征。

## EMT 中的角色

新能源机组 EMT 模型在电力系统中承担以下关键研究任务：

1. **故障穿越与电流注入动态**：研究风机或光伏逆变器在电网电压跌落期间的有功/无功电流响应、限流逻辑和闭锁-重启行为。
2. **控制交互与稳定性**：分析机组控制（PLL、电流环、电压外环）与外部电网强度（SCR）、线路阻抗、保护继电器之间的相互作用，识别次同步振荡、宽频振荡等失稳机理。
3. **建模粒度选择**：在开关模型（SW）、电压插值模型（VI）、平均值模型（AV）、受控电流注入模型（CCI）之间按仿真目的选择保真度-效率最优方案。
4. **GFM 与 GFL 行为差异**：构网型（Grid-Forming）逆变器提供电压/频率支撑，跟网型（Grid-Following）逆变器注入电流跟随电网相位——两者在 EMT 中的建模框架和控制接口完全不同。
5. **高比例新能源系统规模化仿真**：当系统中新能源渗透率超过 50% 时，机组级模型的计算负担呈指数增长，需通过降阶等值、多速率仿真或并行计算加速。

## 新能源机组分类与核心机制

新能源机组按能源类型和拓扑可分为五大类，每一类在 EMT 中有不同的建模重点。

### 1. Type-3 双馈风机（DFIG）

Type-3 风机采用定子直连电网、转子经部分容量变流器（约 30%~40% 额定功率）控制的架构。EMT 建模核心在于：

- **转子侧变流器（RSC）**：控制有功/无功功率，通过 dq 解耦电流控制实现快速响应
- **网侧变流器（GSC）**：维持直流链路电压稳定
- **Crowbar 保护**：故障期间短接转子绕组，保护变流器免受过电压

其电磁暂态动态由以下方程描述：

$$
\sigma \tau_r \frac{d\vec{i}_r}{dt} + \vec{i}_r = \frac{\vec{V}_r}{R_r} - j \frac{(1-\sigma)\tau_r}{L_m} \Delta\omega \vec{\psi}_s - j \Delta\omega \sigma \tau_r \vec{i}_r
$$

其中 $\sigma = 1 - L_m^2/(L_s L_r)$ 为漏磁系数，$\tau_r = (1+\sigma_r)L_m/R_r$ 为转子时间常数，$\Delta\omega$ 为转速偏差。该方程在忽略定子磁链导数假设下成立，是 DLFE（动态低频等值）中发电机-变流器等值模块的核心状态方程。

**气动功率模型**：

$$
P_{mech} = \frac{1}{2} \rho A v_{wind}^3 C_p(\lambda, \beta) / S_{base}^{WTG}
$$

$$
\lambda = \frac{(\omega_{req}/G) \cdot r}{v_{wind}}, \quad C_p(\lambda, \beta) = c_1 \left( \frac{c_2}{\lambda_i} - c_3 \beta - c_4 \beta^{c_5} - c_6 \right) \exp\left(\frac{-c_7}{\lambda_i}\right)
$$

其中 $\lambda_i^{-1} = \frac{1}{\lambda + 0.08\beta} - \frac{0.035}{\beta^3 + 1}$，$c_1 \sim c_9$ 为 9 个需辨识的 $C_p$ 曲线参数。

**传动链动力学**（单质量块简化）：

$$
2(H_t + H_g) \frac{d\omega}{dt} = T_m - T_e - D\omega
$$

传动链机械动态的有效频带约为 0~3 Hz，DLFE 聚合模型通常保留此低频机械动态。

**验证数据**（Hussein 等 2016）：8 台 1.7 MW Type-3 DFAG 风电场，13.8/115 kV 升压变压器。三相接地故障（150 ms，距 PCC 15 km）下 PCC 电压跌至 35% 额定值，等值模型无功电流精确升至 1.0 p.u.，有功电流降至 0，与详细模型最大动态偏差 < 1%。

### 2. Type-4 全功率风机（PMSG / 直驱风机）

Type-4 风机采用全功率背靠背变流器架构，发电机与电网完全电气解耦。EMT 建模特点：

- **机侧变流器（MSC）**：控制发电机转速/功率，通常采用 MPPT 策略
- **网侧变流器（GSC）**：控制直流链路电压和并网功率，其控制决定了 PCC 端口的动态行为
- **背靠背解耦效应**：由于机侧与网侧通过直流链路隔离，外部 PCC 端口主要看到网侧变流器及其控制形成的电流响应，机侧动态对 PCC 的影响可忽略

**宽频降阶等值模型**（Wang 等 2012）：

将 Type-4 风电场等值拆分为两部分并联于 PCC：

- **FDNE（频变无源网络等值）**：通过 PCC 端口频率扫描（0~50 kHz，5000 个对数分布点），利用矢量拟合将集电系统、变压器的宽频导纳响应拟合为有理函数：

$$
Y(s) = d + sh + \sum_{m=1}^{N} \frac{c_m}{s - a_m}
$$

其中 $N$ 为拟合阶数（原文 56 阶），$a_m$ 为极点，$c_m$ 为留数，$d$ 和 $h$ 为实常数项。该有理函数通过伴随电路法（companion circuit）和梯形积分法转换为时域等效电路。

- **DLFE（动态低频等值）**：聚合网侧变流器及其 dq 解耦电流控制、场站监督控制（含 PLL、功率参考与 VRT 逻辑），通过受控电流源注入低频动态。

**量化验证**（Lake Erie Shore 测试系统，17 台聚合 Type-4 直驱风机，原系统 66 台，34.5/115 kV 升压变压器，34.5 kV 集电系统）：
- 详细模型仿真耗时 18480 秒（5 小时 8 分钟），等值模型仅需 110 秒，**计算速度提升 218 倍**
- 三相接地故障（150 ms，15 km 处）：PCC 电压跌至 15% 额定值，无功电流精确注入 1.0 p.u.，有功电流降至 0
- 单相接地故障：精确捕捉负序分量响应
- 永久性故障与重合闸失败：完整复现两次故障冲击和拓扑切换引起的高频振荡
- **单一模型失效验证**：仅 FDNE 或仅 DLFE 均无法准确复现 PCC 电压暂态波形，两者并联集成是保证全频段精度的必要条件

### 3. 光伏（PV）单元

光伏机组的 EMT 建模从物理到系统等效存在多层级。

**单二极管 PV 模型**（Di Fazio & Russo 2012）：

理想 PV 模块的 I-V 关系：

$$
I_i(V_i) = I_g - I_o\left(e^{\beta V_i/a} - 1\right)
$$

含串联电阻 $R_s$ 和并联电阻 $R_p$ 的实际模型：

$$
I(V) = I_g - I_o\left(e^{\beta(V+R_s I)/a} - 1\right) - \frac{V+R_s I}{R_p}
$$

其中 $\beta(T) = \frac{q}{M_s kT}$ 为反热电压，$q = 1.60217646 \times 10^{-19}$ C 为电子电荷，$k = 1.3806503 \times 10^{-23}$ J/K 为玻尔兹曼常数，$M_s$ 为模块中串联电池数。

由单个模块扩展到 PV 发电机（$N_p$ 个并联阵列，每阵列 $N_s$ 个串联模块）：

$$
a_{gen} = a, \quad I_{g,gen} = N_p I_g, \quad I_{o,gen} = N_p I_o, \quad R_{s,gen} = \frac{N_s}{N_p}R_s, \quad R_{p,gen} = \frac{N_s}{N_p}R_p, \quad \beta_{gen} = \frac{\beta}{N_s}
$$

**ELST（扩展线性系统技术）**：传统 BLST 在第 $k$ 步用第 $k-1$ 步端电压代入 PV 非线性方程得到注入电流，引入一步延迟导致数值失稳。ELST 在展开点 $(V_0, I_0)$ 附近对 PV 的 I-V 曲线线性化：

$$
I(V) \approx I_0 + \left.\frac{dI}{dV}\right|_0 (V - V_0) = I_{eq} - G_{eq}V
$$

其中等效电导 $G_{eq} = -\left.\frac{dI}{dV}\right|_0$，等效电流源 $I_{eq} = I_0 + G_{eq}V_0$。$G_{eq}$ 并入 EMT 节点导纳矩阵，$I_{eq}$ 并入注入向量。该机制将 PV 端口的局部增量关系纳入同一时步网络方程，消除 BLST 的冻结电流源误差。

**I-V 斜率解析表达式**：

$$
\frac{dI}{dV} = -\frac{\frac{\beta I_o}{a}e^{\beta(V+R_s I)/a} + \frac{1}{R_p}}{1 + \frac{\beta R_s I_o}{a}e^{\beta(V+R_s I)/a} + \frac{R_s}{R_p}}
$$

**验证**：IEEE 基准配电系统，局部遮阴和电气故障工况下 ELST 相对 BLST 数值稳健性显著提升。

### 4. 跟网型逆变器（GFL / Grid-Following）

GFL 逆变器通过 PLL 跟踪电网相位，以电流源形式注入功率。EMT 建模的核心挑战是在保真度和效率之间选择恰当的模型粒度。

**五类并网逆变器模型对比**（Sano 等 2022）：

| 模型 | 描述 | 仿真步长 | 计算时间比例 | 适用场景 | 失效场景 |
|------|------|---------|------------|---------|---------|
| SW（开关模型） | 显式功率器件开关，PWM 门极信号决定拓扑 | 2 μs | 100% | 开关频率谐振、死区谐波、直流短路续流 | 大系统计算不可接受 |
| VI（电压插值） | 插值占空比 $\bar{s} = \frac{1}{2} + \frac{v^* - v_{carrier}}{h T_s}$，消除固定步长量化误差 | 10 μs | 19% | 谐波分析、暂态评估 | 不捕获开关级细节 |
| AV（平均值） | $v_{sa} = d_a v_{dc}$，输出调制参考电压的平均值 | 100 μs | 1.5% | 基波控制动态、功率交换 | 开关频率谐振(100%误差)、死区谐波(100%误差) |
| CCI（受控电流注入） | 理想电流源 + 功率平衡 | 600 μs | 0.20% | 大系统粗略功率注入 | 电网谐波免疫(100%误差)、缺失高频尖峰、直流短路误差>15% |
| SCI（简化电流注入） | 进一步简化 CCI，无 PLL | 600 μs | 0.12% | 低频动态、大电网扫描 | 无功控制显著误差、100%暂降下逻辑失效(误差>20%) |

**关键量化发现**：
- **稳定性评估偏差**：AV 模型电流控制失稳临界增益为 3 p.u.，较 SW/VI 的 2 p.u. 存在 1 p.u. 的乐观偏差
- **高频谐振**：4.5 kHz 谐振点处，SW/VI 模型误差 < 2%，AV/CCI/SCI 完全未出现谐振响应
- **死区谐波**：25 μs 死区时间下，仅 SW/VI 能准确再现电流过零点畸变
- **电网谐波交互**：10% 幅值 5 次谐波电压下，SW/VI/AV 输出电流明显畸变，CCI/SCI 输出不受影响

**等效时域 IBR 模型**（Luchini 等 2023，ATP/ATPDraw）：

采用"PLL 同步 + 瞬时功率反解 dq 电流 + 受控电流源"架构：

$$
P = \frac{3}{2}(v_d i_d + v_q i_q), \quad Q = \frac{3}{2}(v_q i_d - v_d i_q)
$$

电网电压定向（$v_q = 0$）下反解：

$$
i_d = \frac{2P}{3v_d}, \quad i_q = -\frac{2Q}{3v_d}
$$

**验证**：稳态及对称/不对称故障场景下，输出电流平均误差 2.33%，仿真执行时间降低约 70%。DSOGI-PLL 在电网电压畸变条件下可有效抑制谐波干扰。

### 5. 构网型逆变器（GFM / Grid-Forming）

GFM 逆变器不依赖外部 PLL，通过下垂控制或虚拟同步机（VSG）控制自主建立电压/频率参考。EMT 建模重点在于 PQ 能力边界、调制饱和和故障限流。

**PQ 能力边界模型**（Nurunnabi 等 2025）：

PCC 点功率传输方程（基于 L/LC/LCL 耦合滤波器）：

$$
P_{PCC} \approx V_{PCC} \frac{E_{inv}}{X_F} \delta_{inv}, \quad Q_{PCC} \approx V_{PCC} \frac{E_{inv} - V_{PCC\_F}}{X_F}
$$

PQ 运行域由两类硬约束的交集确定：

1. **额定电流约束**：$|\vec{I}_{PCC}| \leq I_{rated}$
2. **PWM 饱和约束**：$|\vec{E}_{inv}| \leq E_{max}$

其中 $E_{max}$ 取决于调制策略与直流母线电压。SVPWM 下最大允许输出电压达 1.53 p.u.，较 SPWM 的 1.33 p.u. 提升约 15%。

**下垂控制律**：

$$
f_{ik} = f_{set} + m_{pi}(P_{kset\_i} - P_{ki}), \quad V_{ik} = V_{set} + m_{qi}(Q_{kset\_i} - Q_{ki})
$$

**验证**（100 kVA GFM 逆变器，L/LC/LCL 滤波器，PCC 线电压 690 V / 60 Hz，直流母线 1500 V）：
- EVR 策略动态负载下电压最大偏差 2.9%，频率最大偏差 0.37%，严格满足 IEEE 1547 标准
- 3% Q-V 下垂系数使暂态电压恢复时间缩短至毫秒级，稳态电压精度提升约 40%
- 逆变器输出端短路容量 316 kVA，为故障穿越与限流保护提供基准
- GFM/GFL 并联运行可行，EMT 仿真与 HIL 实验结果高度一致

### 6. 储能单元（BESS）

储能机组的 EMT 建模关注电池/超级电容侧状态、DC/DC 接口和并网逆变器的耦合动态。SOC 和热模型是否保留应由研究目标决定。在故障穿越场景中，储能逆变器的快速功率注入能力（通常在 1~3 个工频周期内达到额定功率）对系统电压恢复至关重要。

## 建模粒度选择指南

基于 Sano 等 2022 和 Luchini 等 2023 的研究，新能源机组 EMT 建模粒度选择应遵循以下规则：

| 仿真目的 | 推荐模型 | 推荐步长 | 说明 |
|---------|---------|---------|------|
| 开关频率谐振分析（>10 kHz） | SW | 1~2 μs | 必须解析 PWM 开关过程 |
| 死区谐波、二极管续流路径 | SW 或 VI | 2~10 μs | VI 可在 10 μs 步长下接近 SW 精度 |
| 电流控制稳定性评估 | SW 或 VI | 2~10 μs | AV 会乐观估计 1 p.u. 增益裕度 |
| 基波控制动态、功率交换 | AV | 50~100 μs | 计算时间仅为 SW 的 1.5% |
| 场站级故障穿越扫描 | AV 或等效电流源 | 100~300 μs | 需保留 PLL 和 FRT 逻辑 |
| 大电网低频动态扫描 | CCI | 300~600 μs | 需确保控制器包含 PLL |
| 粗略功率注入近似 | SCI | 600+ μs | 仅适用于低频且不含 PLL |
| 场站级宽频等值（外部扰动） | FDNE+DLFE | 5 μs | 覆盖 0~50 kHz，218x 加速 |
| 高比例 IBR 系统故障分析 | 等效时域 IBR | 10~50 μs | 2.33% 误差，70% 时间节省 |

## EMT 建模关键技术挑战

### 1. 数值稳定性与步长选择

新能源机组中包含大量非线性元件（二极管、IGBT、饱和电抗器）和快速控制器（电流环带宽通常 1~5 kHz），对 EMT 数值积分稳定性构成挑战。Di Fazio & Russo 2012 的 ELST 技术揭示了分离求解（BLST）中一步延迟导致的数值失稳机理——当 PV 或逆变器端口电压快速变化时，冻结电流源会引入正反馈，放大数值振荡。ELST 通过将局部 I-V 斜率（等效电导）并入节点导纳矩阵，在同一时步内建立端口增量耦合，显著扩大数值稳定域。

### 2. 降阶等值与保真度折中

大规模新能源场站（数十至数百台机组）的 EMT 仿真面临"维度灾难"。Wang 等 2012 和 Hussein 等 2016 提出的 FDNE+DLFE 架构通过频段分解解决了这一问题：FDNE 负责无源网络的宽频端口特性（0~50 kHz），DLFE 负责有源控制动态（0~20 Hz）。这种"频段分工"策略避免了单一低阶模型同时拟合全部物理过程的困难，在 218 倍加速的同时保持 PCC 端口波形高度一致。

### 3. GFM 与 GFL 的混合运行建模

随着新能源渗透率提高，GFM 和 GFL 逆变器将在同一电网中并存。两者的 EMT 建模框架存在本质差异：GFL 以电流源形式注入功率，依赖外部 PLL 同步；GFM 以电压源形式建立参考，通过下垂控制实现功率分配。Nurunnabi 等 2025 的 GFM/GFL 并联运行验证表明，在合理参数设计下两者可稳定共存，但需精确刻画 GFM 的 PQ 能力边界（由 PWM 饱和和额定电流共同约束）以防止过流。

### 4. 厂家黑盒控制器的等效

实际新能源机组的控制器通常由厂家提供黑盒代码，外部研究者无法获取内部参数。这导致 EMT 模型中的控制环节只能基于公开规范（如 NERC PRC-024、IEEE 1547）或现场录波数据进行逆向参数辨识。等效模型不应把等效写成真实控制器——页面应说明证据边界和可信度。

## 量化性能边界

| 指标 | 数据来源 | 数值 |
|------|---------|------|
| Type-4 等值模型加速比 | Wang 等 2012 (Lake Erie Shore, 66→17 台聚合) | 218x (18480s → 110s) |
| 等效时域 IBR 模型误差 | Luchini 等 2023 (ATP/ATPDraw, 对称/不对称故障) | 2.33% (输出电流) |
| 等效时域 IBR 模型加速 | Luchini 等 2023 | 70% 时间节省 |
| 五类逆变器模型时间比例 | Sano 等 2022 (XTAP, 光伏并网) | SW:100%, VI:19%, AV:1.5%, CCI:0.20%, SCI:0.12% |
| AV 模型稳定性乐观偏差 | Sano 等 2022 | 1 p.u. (AV:3.0 vs SW/VI:2.0) |
| 4.5 kHz 谐振再现误差 | Sano 等 2022 | SW/VI:<2%, AV/CCI/SCI:100% |
| PV ELST 数值稳健性提升 | Di Fazio & Russo 2012 (IEEE 基准配电系统) | 局部遮阴和电气故障下 BLST 失稳→ELST 稳定 |
| GFM PQ 运行域扩展 | Nurunnabi 等 2025 (SVPWM vs SPWM) | 1.53 vs 1.33 p.u. (+15%) |
| GFM 动态负载电压偏差 | Nurunnabi 等 2025 (EVR 策略) | 2.9% (稳态), 0.37% 频率偏差 |
| DFIG 等值模型端口偏差 | Hussein 等 2016 (8×1.7 MW DFAG, 三相故障) | <1% 动态偏差 |
| DFIG 故障穿越电流精度 | Hussein 等 2016 (PCC 电压 35%) | 无功 1.0 p.u., 有功 0, 与详细模型完全一致 |

## 适用边界与选择指南

### 按仿真目标选择

| 应用场景 | 推荐机组模型 | 关键考虑 |
|---------|------------|---------|
| 开关频率谐振分析 | SW 或 VI | 必须解析 PWM 开关，步长 ≤ 5 μs |
| 保护继电器动作研究 | SW 或 VI | 需准确再现故障电流波形和死区谐波 |
| 电流控制稳定性评估 | SW 或 VI | AV 会高估 1 p.u. 增益裕度 |
| 场站级故障穿越扫描 | AV 或 FDNE+DLFE | 保留 PLL、FRT 逻辑，忽略开关细节 |
| 高比例 IBR 系统暂态 | 等效时域 IBR | 2.33% 误差，70% 加速 |
| 大电网低频动态扫描 | CCI 或降阶等值 | 需包含 PLL 和 FRT 逻辑 |
| 宽频阻抗扫描/谐振定位 | FDNE (矢量拟合) | 0~50 kHz 频率扫描 + 伴随电路实现 |
| GFM 能力边界验证 | PQ 边界模型 + 详细逆变器 | 需考虑 PWM 饱和和额定电流约束 |
| 单机到场站聚合 | FDNE+DLFE 架构 | 背靠背解耦使机侧动态对 PCC 可忽略 |

### 失效边界

- **平均值模型不适用于**：开关频率谐振（>10 kHz）、死区谐波、直流侧短路续流路径、电网谐波交互分析——这些场景下误差可达 100%（Sano 等 2022）。
- **受控电流注入模型不适用于**：电网电压畸变响应、故障暂态尖峰电流、电流控制稳定性评估——CCI 对电网谐波免疫，SCI 在 100% 电压暂降下逻辑失效。
- **FDNE+DLFE 等值不适用于**：风电场内部过电压、单台机组开关细节、超出拟合频带（>50 kHz）的现象——该架构面向外部系统 PCC 端口等值，而非内部细节分析（Wang 等 2012）。
- **ELST 不适用于**：包含大量非 PV 非线性元件且这些非线性需与网络强耦合联立求解的系统——ELST 仅针对 PV 单二极管模型与线性网络的耦合场景（Di Fazio & Russo 2012）。
- **等效时域 IBR 模型不适用于**：构网型控制、开关谐波、器件级损耗、电磁干扰分析——该模型面向跟网型、功率指令驱动的 EMTP 系统暂态（Luchini 等 2023）。
- **GFM PQ 边界模型不适用于**：所有并网逆变器的通用稳定性结论——该模型特定于 L/LC/LCL 滤波器配置下的 GFM 逆变器，不能替代具体厂商硬件的热限制和保护逻辑（Nurunnabi 等 2025）。

## 相关模型

- [[dfig-model]] — DFIG 机组详细 EMT 模型
- [[pv-system-model]] — 光伏系统 EMT 模型
- [[inverter-model]] — 并网逆变器通用 EMT 模型
- [[gfl-inverter-model]] — 跟网型逆变器 EMT 模型
- [[gfm-inverter-model]] — 构网型逆变器 EMT 模型
- [[bess-model]] — 储能系统 EMT 模型
- [[grid-side-converter]] — 网侧变流器模型
- [[pmsg-single-unit]] — 永磁直驱风机单机模型

## 相关方法

- [[average-value-model]] — 平均值建模方法
- [[switch-modeling]] — 开关级建模方法
- [[switching-function-method]] — 开关函数法
- [[state-space-average-method]] — 状态空间平均法
- [[vector-fitting]] — 矢量拟合（FDNE 有理函数逼近）
- [[companion-circuit]] — 伴随电路法（FDNE 时域实现）
- [[fdne-model]] — 频变网络等值模型
- [[wideband-modeling]] — 宽频建模方法
- [[model-order-reduction]] — 模型降阶方法
- [[dynamic-phasor]] — 动态相量法
- [[droop-control]] — 下垂控制（GFM 功率分配）
- [[pll-model]] — 锁相环模型
- [[pi-controller-model]] — PI 控制器模型
- [[nodal-analysis]] — 节点分析法
- [[numerical-integration]] — 数值积分方法
- [[frequency-dependent-modeling]] — 频率相关建模
- [[harmonic-analysis-methods]] — 谐波分析方法

## 相关主题

- [[renewable-energy-integration]] — 新能源并网系统级问题
- [[pv-power-plant]] — 光伏电站级聚合和集电网络
- [[fault-ride-through]] — 故障穿越技术
- [[power-quality]] — 电能质量
- [[electromagnetic-transient]] — 电磁暂态分析
- [[emt-simulation]] — 电磁暂态仿真
- [[control-system]] — 控制系统设计
- [[real-time-simulation]] — 实时仿真技术
- [[small-signal-analysis]] — 小信号稳定性分析
- [[frequency-domain-analysis]] — 频域分析方法

## 来源论文

- **Wang 等 2012** — *A Type-4 Wind Power Plant Equivalent Model* (IEEE TPWRS) — 提出 Type-4 风电场宽频降阶等值模型（FDNE+DLFE），218 倍加速，0~50 kHz 精度覆盖
- **Hussein 等 2016** — *A Wideband Equivalent Model of Type-3 Wind Power Plants for EMT Studies* (IEEE TPWRD) — 提出 Type-3 DFAG 风电场 FDNE+DLFE 等值，0~20 Hz 低频动态，FRT 精确复现
- **Sano 等 2022** — *Comparison and Selection of Grid-Tied Inverter Models for Accurate and Efficient EMT Simulations* (IEEE TPEL) — 五类并网逆变器模型（SW/VI/AV/CCI/SCI）精度-效率系统对比，建立选型规则
- **Luchini 等 2023** — *Equivalent grid-following inverter-based generator model for ATP/ATPDraw simulations* (EPSR) — 等效时域跟网型 IBR 模型，2.33% 误差，70% 时间节省
- **Di Fazio & Russo 2012** — *Photovoltaic generator modelling to improve numerical robustness of EMT simulation* (EPSR) — 扩展线性系统技术（ELST），解决 PV 单二极管模型在 EMT 中的数值不稳定问题
- **Nurunnabi 等 2025** — *Advancing Grid-Forming Inverter Technology: Comprehensive PQ Capability and Performance Analysis* (IEEE Access) — GFM 逆变器 PQ 能力边界建模，SVPWM vs SPWM，EVR 策略验证
