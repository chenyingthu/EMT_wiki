---
title: "雷电过电压 (Lightning Overvoltage)"
type: topic
tags: [lightning, surge, overvoltage, arrester, grounding, insulation-coordination, lightning-current, tower-footing, soil-frequency-dependence]
created: "2026-05-01"
updated: "2026-05-16"
---

# 雷电过电压 (Lightning Overvoltage)

## 定义与边界

雷电过电压（Lightning Overvoltage）是雷电流通过直击导线、击中杆塔或避雷线、附近雷击感应等途径，在电力系统导体和设备端子上产生的快速过电压。雷电通道放电电流的波前时间为 $1\sim20\ \mu\text{s}$，波尾时间可达数十至数百微秒，频谱可从直流延伸至数 MHz 量级。

从物理过程上，雷电过电压分为**直击过电压**（direct stroke）和**感应过电压**（induced stroke）两大类：
- **直击过电压**：雷电流直接注入被击导体（导线、避雷线、杆塔），产生数十至数百千安的放电电流，沿线路传播并通过杆塔接地系统泄放入地
- **感应过电压**：雷击线路附近地面时，雷电通道的电磁场沿线导体感应耦合，感生电压沿线路传播，通常幅值较低但波前更陡

从 EMT 建模角度，雷电过电压涉及**四个核心物理机制**的协同建模：
1. **雷电流源**：描述雷电通道放电电流的时域波形（Heidler 函数、双指数函数、分段线性函数）
2. **线路耦合**：雷电通道电磁场与输电线路的能量耦合（场线耦合方程、分布电流源注入）
3. **频变传播**：雷电波沿线传播时的频率相关损耗、色散和波形畸变（[[frequency-dependent-soil]]、[[earth-return-impedance]]）
4. **接地与杆塔**：雷电流经杆塔接地系统泄放时的地电位升和反击过程（[[tower-foot-grounding-model-for-emt-programs-based-on-transmission-line-theory-an]]、[[grounding-system-modeling]]）

本页面讨论雷电激励在 EMT 仿真中的建模方法，不涉及由断路器或隔离开关操作触发的 [[switching-transient]]，也不讨论工频接地故障引起的稳态地电位升（见 [[grounding-lightning-overvoltage]]）。

## EMT 中的角色

雷电过电压研究把外部电磁扰动（雷电流、雷电电磁场）转换为 EMT 网络中的激励源，用于以下工程目标：

1. **绝缘配合**：计算雷电冲击下设备端子最大应力电压，确定避雷器额定电压和保护水平
2. **避雷器能量校核**：计算雷电流流经避雷器时的能量吸收 $W = \int v_a(t) i_a(t)\, dt$，校验避雷器热容是否满足要求
3. **接地系统设计**：评估杆塔接地电阻和地电位升（Ground Potential Rise, GPR），避免地电位反击
4. **反击闪络分析**：计算绝缘子串两端雷电过电压，评估反击闪络概率

EMT 仿真的核心价值在于保留：波前的陡度（GHz 级频谱）、反射与折射过程、频变损耗导致的波形畸变、非线性避雷器的限压动作，以及多端口系统中不同节点同时承受过电压的耦合效应。

常见仿真输出：端口电压 $v(t)$、雷电流 $i_L(t)$、避雷器电流和能量 $W$、接地电位升 $V_{\text{GPR}}(t)$、绝缘子闪络判据（电压超过伏秒曲线）。

## EMT 建模方法

### 雷电流源模型

工程算例中常用的雷电流表示方法有三种：

**1. 双指数函数（Double-Exponential）**

$$i_L(t) = I_m \left(e^{-\alpha t} - e^{-\beta t}\right)$$

其中 $I_m$ 为峰值电流，$\alpha$ 和 $\beta$ 为衰减时间常数。典型参数：$I_m = 10\sim 200\ \text{kA}$，$\alpha \approx 2\times 10^4\ \text{s}^{-1}$，$\beta \approx 10^6\ \text{s}^{-1}$，对应 $1.2/50\ \mu\text{s}$ 标准雷电冲击波形。参数与峰值电流的关系为：

$$\alpha = \frac{1}{t_1} \ln\frac{\beta/\alpha}{\beta t_1 - 1}, \quad \beta = \frac{1}{t_2} \ln\frac{\beta/\alpha}{\beta t_2 - 1}$$

其中 $t_1$ 为波前时间（约 $1.2\ \mu\text{s}$），$t_2$ 为波尾时间（约 $50\ \mu\text{s}$）。双指数函数优点是数学形式简洁、参数与标准波形直接对应，缺点是在 $t=0$ 处的导数无穷大，与实际雷电放电电流起始的连续性不符。

**2. Heidler 函数**

$$i_L(t) = \frac{I_m}{\eta} \frac{(t/\tau_1)^n}{1 + (t/\tau_1)^n} e^{-t/\tau_2}$$

其中 $\eta$ 为峰值归一化因子，$\tau_1$ 为波前时间常数，$\tau_2$ 为波尾时间常数，$n$ 为幂指数（通常取 $n=2\sim 10$）。Heidler 函数在 $t=0$ 处的电流变化率为 $di/dt \approx 0$，更符合实际雷电放电电流的上升特性。CIGRE WG 33-01 推荐参数：$I_m = 10\ \text{kA}$，$\tau_1 = 0.005\ \text{ms}$，$\tau_2 = 0.25\ \text{ms}$，$\eta \approx 0.93$。

**3. 分段线性函数（PWL）**

将雷电流波形用折线逼近，适用于需要直接指定波前/波尾时间且不想引入指数函数非线性的 EMT 求解器（如 EMTP 的 TACS/TS 模块）。典型 $10/350\ \mu\text{s}$ 波形可表示为：上升段 $0\sim 10\ \mu\text{s}$ 线性从 0 增至 $I_m$，下降段 $10\sim 350\ \mu\text{s}$ 线性从 $I_m$ 降至 $0.1 I_m$。

### 场线耦合与感应雷建模

雷电通道与输电线路的电磁耦合可用地线积分方程表示。**电场激励**等效为沿线分布的电压源：

$$e_i(x,t) = \int_0^h E_z^{\text{inc}}(x,z,t) \, dz$$

其中 $h$ 为导线对地高度，$E_z^{\text{inc}}$ 为入射雷电电场的垂直分量。

**电流源注入法**（用于 ATP/JMarti 频变线路）：把入射场作用完全转化为线路两端的 Norton 型独立电流源 $j_0(t)$、$j_L(t)$，对给定雷击事件预先计算一次，不随避雷器等非线性元件状态迭代改变。这些源是时不变的，仅取决于雷击位置和线路几何参数。

**扩展模态域模型（EMD）**通过等效阻抗拟合将外部电磁场转化为 Norton 电流源注入 ATP 已有频变线路模型。原始 EMD 电流源计算依赖特征导纳 $Y_c$ 的有理函数拟合，但 ATP/JMarti 模型输出的是特征阻抗 $Z_c = Y_c^{-1}$ 的拟合参数。A Thvenin-Type Version of EMD 解决了这一接口兼容性问题，使 EMD 外部激励可直接嵌入 ATP 的 JMarti 框架。

### 频变土壤与接地模型

雷电暂态含 kHz 至 MHz 高频分量，土壤参数（电阻率 $\rho$、介电常数 $\varepsilon_r$）具有频率依赖性。在高频下，$\omega\varepsilon$ 可能与 $\sigma = 1/\rho$ 同量级，不能简单将大地视为电导率恒定的良导体。

**频变土壤参数模型**（Comparison of Soil Modeling, 2021）：用三个统计独立参数描述频率依赖：低频电导率 $\sigma_0$ 及两个形状参数。将 $\sigma$ 替换为 $\sigma + j\omega\varepsilon$ 后扩展 Carson 和 Pollaczek 大地回流公式，用 Gauss 求积数值计算无穷积分。该方法在 $100\ \text{Hz}\sim 10\ \text{MHz}$ 范围内有效，避免了传统复平面近似的解析近似误差。

**塔脚接地传输线模型**（Tower Foot Grounding Model）：将接地极表示为埋地传输线，求解电报方程：

$$\frac{dV}{dx} = -(Z_i + j\omega L) I, \quad \frac{dI}{dx} = -(G + j\omega C) V$$

借用经典 Marti 频变传输线模型在 ATP 中实现接地组件，使接地组件可作为 EMT 网络元件参与雷击暂态计算。传播常数 $\gamma = \sqrt{(R+j\omega L)(G+j\omega C)}$ 随频率变化，导致接地阻抗在宽频带内呈非线性。

**接地网频变 π 型模型**（Grounding Grids in EMT）：把接地网抽象为二端口 π 型电路，端口间三个频变阻抗/导纳支路（$Z_1(\omega)$、$Z_2(\omega)$、$Z_{\text{coupling}}(\omega)$）由电磁场软件（XGSLab）计算得到频域响应后，转换为 ATP-EMTP 可直接使用的拉普拉斯域有理函数导纳。

**全波黑盒塔模型**（Full-Wave Black-Box Tower Model）：将三维电磁场求解得到的多端口响应（塔顶注入点→各绝缘子串电压）转化为可嵌入 EMT 的有理函数宏模型，保留塔身和接地系统的三维几何细节、土壤参数频变和电磁耦合。

### 杆塔冲击阻抗模型

雷击塔顶时，电磁波沿杆塔往返传播并抬高绝缘子串电压。杆塔冲击阻抗的建模方法包括：

**单分布参数塔模型**：将塔身视为均匀分布参数传输线，输入阻抗随频率变化：

$$Z_{\text{tower}}(\omega) = Z_0 \frac{1 + \Gamma e^{-2\gamma L}}{1 - \Gamma e^{-2\gamma L}}$$

其中 $Z_0 = \sqrt{(R+j\omega L)/(G+j\omega C)}$ 为特性阻抗，$\Gamma$ 为接地反射系数，$\gamma$ 为传播常数，$L$ 为塔高。

**多层塔模型**：将塔身分段（塔身、横担、接地极），每段用独立的传输线参数，层间通过连接点耦合。

**含横担等效电路模型**（Equivalent Circuit Model of Transmission Tower）：先用 FDTD 分析横担尖端雷击下的电磁场和绝缘子电压机理，再提出可放入 EMT 型仿真器的含横担等效电路，使电路仿真能够区分受击侧与非受击侧绝缘子电压。塔身和横担改变周围电磁场分布：受击侧电场更强，另一侧被塔体/横担结构削弱，绝缘子电压不再左右对称。

**自动化矩量法塔模型**（Electromagnetic Model for Tower Surge Impedance）：用 NEC4 矩量法电磁求解实现直接法阻抗计算，从 CAD/几何到杆塔线网的过程自动化，使同一流程可用于其他塔型，同时可考虑有限大地电阻和接地电极。

### 电晕效应与波形畸变

雷电冲击在导线上传播时，若导线附近电场超过空气临界值（约 $3\ \text{MV/m}$），则发生电晕放电，空间电荷吸收能量并改变冲击波峰值、波前时间和波形。

**波形相关电晕模型**（Waveform Dependence Lightning Impulse Corona Model）：核心状态量为导线电压/电场、起晕延时、空间电荷线密度、电晕电容和电晕支路电流。模型把电晕效应等效为线路节点上的附加电晕支路，嵌入 PSCAD/EMTDC 时无需迭代求解。

电晕电荷积累满足：

$$q_c(t) = q_0 \left(1 - e^{-t/\tau_c}\right), \quad \tau_c = \frac{\varepsilon_0}{J_c}$$

其中 $q_0$ 为饱和电晕电荷，$\tau_c$ 为电离弛豫时间常数。电晕电容非线性变化：

$$C_c(v) = C_0 + \frac{k}{|v|}$$

其中 $C_0$ 为几何电容，$k$ 为电晕系数。电晕会导致雷电波前时间延长、峰值衰减，是雷电过电压计算中不可忽略的波形畸变因素。

### 避雷器限压模型

金属氧化物压敏电阻避雷器（MOV）的伏安特性为非线性：

$$i_a = k v_a^\alpha$$

其中 $\alpha \approx 30\sim 50$ 为非线性指数，$k$ 为与额定电压相关的常数。EMT 中常用**分段线性模型**（PWL）或**状态依赖模型**（State-Dependent）表示：

$$R(v) = \begin{cases} R_1 & |v| < V_{\text{ref}} \ R_2 & |v| \ge V_{\text{ref}} \end{cases}$$

避雷器动作后限制残压 $V_{\text{res}}$，但同时吸收能量 $W = \int v_a(t) i_a(t)\, dt$ 需要校验热容。热恢复特性表现为：避雷器动作后电阻值恢复至高阻状态，若能量未完全释放则可能发生热崩溃。

## 形式化表达

### 雷电流波形函数

**双指数函数**：

$$i_L(t) = I_m \left(e^{-\alpha t} - e^{-\beta t}\right)$$

**Heidler 函数**：

$$i_L(t) = \frac{I_m}{\eta} \frac{(t/\tau_1)^n}{1 + (t/\tau_1)^n} e^{-t/\tau_2}$$

### 端口电压表达式

端口电压由入射波、反射波、接地响应和避雷器限压共同决定（简化关系式）：

$$v_{\text{term}}(t) = v^{+}(t) + \Gamma v^{-}(t) + z_g(t) * i_L(t) - v_a(t)$$

其中 $v^{+}(t)$ 与 $v^{-}(t)$ 表示入射和反射波，$\Gamma$ 为端接反射系数，$z_g(t)$ 为接地或杆塔等效冲激响应（卷积项），$v_a(t)$ 为避雷器限制后的电压贡献。该式是关系示意，不替代具体线路模型。

### 接地电位升

杆塔接地极的地电位升（GPR）为：

$$V_{\text{GPR}}(t) = Z_g(\omega) * i_L(t)$$

其中 $Z_g(\omega)$ 为接地系统频率相关阻抗，由电磁场计算或传输线模型得到。

### 避雷器能量

$$W = \int_0^{t_{\text{duration}}} v_a(t) \cdot i_a(t)\, dt \approx \int_0^{t_{\text{duration}}} V_{\text{res}} \cdot i_a(t)\, dt$$

### 土壤频变参数

复介电常数为：

$$\varepsilon_r^*(\omega) = \varepsilon_r'(\omega) - j\varepsilon_r''(\omega) = \varepsilon_\infty + \frac{\sigma}{j\omega\varepsilon_0}$$

其中 $\varepsilon_\infty$ 为高频介电常数，$\sigma$ 为直流电导率。Cole-Cole 模型进一步写为：

$$\varepsilon_r^*(\omega) = \varepsilon_\infty + \frac{\sigma}{j\omega\varepsilon_0} + \sum_k \frac{\Delta\varepsilon_k}{1 + (j\omega\tau_k)^{\alpha_k}}$$

## 关键技术挑战

**挑战一：宽频带高精度建模需求**

雷电暂态的频谱可从数十 Hz（雷电流的缓慢衰减分量）延伸至数 MHz（波前的快速上升），在此宽频带内，土壤参数变化、接地系统响应和线路传播特性均呈显著频变特性。传统工频或工频暂态模型（如固定接地电阻 $R_g = 10\Omega$）无法捕捉 MHz 量级的波前细节，导致绝缘子端电压被低估或高估。

**挑战二：杆塔几何细节与计算效率的矛盾**

含横担、斜材和接地极的完整三维杆塔模型在 EMT 中计算量过大；简化塔模型（如单一分布参数塔）又丢失了横担对电磁场分布的影响。精确建模需要 FDTD 或 MoM 场求解，但这些方法的计算结果不能直接嵌入常规 EMT 仿真器。

**挑战三：非线性耦合效应的迭代收敛**

避雷器的非线性伏安特性、土壤电离（当接地电位升高导致土壤局部击穿时，等效电导急剧增大）和电晕非线性电容同时存在时，EMT 求解需要在每个时间步迭代联解非线性方程组，收敛困难且计算时间显著增加。

**挑战四：感应雷场线耦合的等效源计算**

把外部雷电电磁场沿线分布的耦合作用转化为线路端部的等效电流源，需要预先计算入射场积分和特征导纳拟合，计算精度依赖于雷击位置模型（先导通道模型）和大地导电参数。

**挑战五：多端口接地网的频变响应提取**

风电场、变电站等复杂接地网包含数十根互联导体，用电磁场软件计算频变响应后，需要将其转换为 EMT 可用的有理函数模型（Vector Fitting），过程复杂且对模型阶数敏感。

## 量化性能边界

以下量化数据均来自来源论文的 EMT 仿真结果：

| 场景 | 雷电流波形 | 关键结果 | 来源 |
|------|-----------|---------|------|
| 138 kV 架空-电缆混合线路直击 | 10/350 μs, 10 kA | 扩展TL+频变土壤+频变接地后，护套过电压比 Pollaczek 模型高 18% | [[an-accurate-analysis-of-lightning-overvoltages-in-mixed-overhead-cable-lines]] |
| 大规模配电网感应雷 | 8/20 μs, 30 kA | ATP/JMarti 频变线路+端口电流源，单次仿真 < 1 min | [[calculation-of-lightning-induced-voltages-on-a-large-scale-distribution-network-]] |
| 电晕波形畸变 | 1.2/50 μs | 含电晕模型后波前时间延长 30%，峰值衰减 12% | [[a-waveform-dependence-lightning-impulse-corona-model-in-pscademtdc-for-investiga]] |
| 76 m 高塔（偏置雷击）| 10/350 μs, 100 kA | 含横担 FDTD 模型：受击侧绝缘子电压比无横担模型高 22% | [[equivalent-circuit-model-of-a-transmission-tower-considering-a-lightning-struck-]] |
| 频变土壤（高电阻率土壤）| 1.2/50 μs | 10 Ω·m 土壤（潮湿）vs 1000 Ω·m（干燥），GPR 相差 8 倍 | [[influence-of-frequency-characteristics-of-soil-on-lightning-transient-response-o]] |
| 风电场互联接地网 | 10/350 μs, 50 kA | 全波 FEKO/MoM + EMT，4 台风机互联 GPR 比单风机接地高 35% | [[comparison-of-soil-modeling-concerning-physical-factors-application-to-transient]] |
| 频变土壤对地回路参数 | 宽频 100 Hz–10 MHz | 频变土壤模型与常数土壤模型相比，地模衰减常数偏差 10%–15% | [[inclusion-of-frequency-dependent-soil-parameters-in]] |
| 接地网（避雷器-变压器端口）| 8/20 μs | π 型频变导纳模型 vs 集中接地电阻，GPR 峰值误差从 40% 降至 5% | [[grounding-grids-in-electro-magnetic-transient-simulations-with-frequency-depende]] |
| 全波黑盒塔模型 | 10/350 μs | 有理函数宏模型嵌入 EMT，绝缘子电压与 FDTD 参考解误差 < 3% | [[full-wave-black-box-transmission-line-tower-model-for-the-assessment-of-lightnin]] |
| 塔脚传输线接地模型 | 1.2/50 μs | 埋地 counterpoise 导体传输线模型，GPR 比集中电阻模型低 25% | [[tower-foot-grounding-model-for-emt-programs-based-on-transmission-line-theory-an]] |

## 适用边界与选择指南

| 建模任务 | 推荐模型 | 适用场景 | 不适用场景 |
|---------|---------|---------|----------|
| 雷电流源（标准波形）| 双指数或 Heidler 函数 | 需要与 IEC 60060-1 或 IEEE 1243 标准波形对应 | 需要精确拟合实测雷电流波形（应使用 PWL 或实测数据导入）|
| 感应雷（配电网络）| ATP/JMarti + 端口电流源 | 大规模配电网、考虑频变线路和分支 | 单根理想线路感应雷（可用传输线积分方程）|
| 直击塔顶（杆塔模型）| 全波黑盒宏模型或含横担等效电路 | 需要区分受击侧与非受击侧绝缘子电压 | 初步估算（可用单分布参数塔模型）|
| 接地系统（宽频）| 传输线接地模型或 π 型频变导纳 | 评估 GPR 和反击闪络概率 | 工频接地电阻计算（可用 $R_g = \rho/(2\pi r)$ 近似）|
| 频变土壤 | 实测频变参数 + Cole-Cole 模型 | 高电阻率土壤（> 100 Ω·m）或高频暂态（波前 < 1 μs）| 低频暂态或土壤参数已精确测定的算例 |
| 电晕效应 | 波形相关电晕模型（PWL 免迭代）| 波前时间延长和峰值衰减显著影响绝缘判断时 | 峰值低于电晕起始电压的感应雷算例 |
| 避雷器限压 | 分段线性或状态依赖模型 | 需要估算能量吸收和热容校验 | 只需要残压估算（可用恒压源近似）|

### 方法选择决策树

```
雷击类型？
├─ 直击导线
│   └─ 是否考虑电晕畸变？
│       ├─ 是 → 双指数/Heidler 雷电流源 + 电晕模型 + 频变线路
│       └─ 否 → 双指数/Heidler 雷电流源 + 频变线路
├─ 直击杆塔
│   └─ 是否需要区分受击侧/非受击侧？
│       ├─ 是 → 含横担等效电路 或 全波黑盒宏模型 + 传输线接地
│       └─ 否 → 单分布参数塔 + 集中接地
└─ 附近雷击（感应雷）
    └─ 网络规模？
        ├─ 大规模配电网 → ATP/JMarti + 端口电流源注入
        └─ 单根线路 → 场线耦合积分方程
```

## 相关方法与模型

- [[switching-transient]] — 开关操作触发的暂态过电压，与雷电过电压共享部分 EMT 建模方法，但激励源性质不同
- [[grounding-lightning-overvoltage]] — 聚焦接地系统和地电位升，本页面保留线路和设备端过电压视角
- [[lightning-transient-analysis]] — 雷电暂态分析方法入口，说明如何组织雷电 EMT 计算流程
- [[frequency-dependent-soil]] — 土壤参数频率依赖性的物理模型，是雷电接地系统频变响应的基础
- [[grounding-system-modeling]] — 接地网在 EMT 中的建模方法，包括集中参数和分布参数模型
- [[earth-return-impedance]] — 大地回路阻抗的精确计算方法（Carson、Pollaczek 公式及其频变扩展）
- [[surge-arrester-model]] — 金属氧化物避雷器的 EMT 等效模型，用于限压和能量计算
- [[transmission-line-theory]] — 传输线理论基础，频变线路模型是雷电波传播的数学框架
- [[insulation-coordination]] — 绝缘配合工程，基于雷电过电压计算结果确定保护水平

## 来源论文

- [[an-accurate-analysis-of-lightning-overvoltages-in-mixed-overhead-cable-lines]] (2022) — 扩展传输线方法、频变土壤、频变接地对护套雷电过电压的影响
- [[calculation-of-lightning-induced-voltages-on-a-large-scale-distribution-network-]] (2018) — ATP/JMarti 频变线路框架中感应雷端口电流源注入法
- [[a-waveform-dependence-lightning-impulse-corona-model-in-pscademtdc-for-investiga]] (2022) — 波形相关电晕模型与免迭代实现
- [[equivalent-circuit-model-of-a-transmission-tower-considering-a-lightning-struck-]] (2021) — FDTD 场分析与含横担 EMT 等效电路模型
- [[influence-of-frequency-characteristics-of-soil-on-lightning-transient-response-o]] (2021) — 频变土壤对地回路参数和雷电暂态响应的影响
- [[an-electromagnetic-model-for-the-calculation-of-tower-surge-impedance-based-on-t]] (2021) — NEC4 矩量法自动化塔阻抗计算
- [[ground-potential-rise-in-wind-farms-due-to-direct-lightning]] (2020) — 风电场互联接地系统的宽带多端口 EMT 模型
- [[a-thvenin-type-version-of-the-extended-modal-domain-model-for-lightning-induced-]] (2021) — EMD 感应雷电流源的 ATP/JMarti 接口兼容性问题解决方案
- [[comparison-of-soil-modeling-concerning-physical-factors-application-to-transient]] (2021) — 6 类土壤模型对风机雷电 GPR 的影响比较（FEKO/MoM + EMT）
- [[inclusion-of-frequency-dependent-soil-parameters-in]] (2021) — 频变土壤参数扩展 Carson/Pollaczek 公式的数值方法
- [[grounding-grids-in-electro-magnetic-transient-simulations-with-frequency-depende]] (2019) — 接地网频变 π 型导纳模型的 ATP 实现
- [[full-wave-black-box-transmission-line-tower-model-for-the-assessment-of-lightnin]] (2021) — 全波有理函数宏模型嵌入 EMT 的方法
- [[tower-foot-grounding-model-for-emt-programs-based-on-transmission-line-theory-an]] (2020) — 传输线理论塔脚接地模型的 ATP 实现