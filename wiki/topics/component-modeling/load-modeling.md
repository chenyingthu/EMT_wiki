---
title: "负荷建模 (Load Modeling)"
type: topic
tags: [load-modeling, load, power-system, dynamic, static, composite-load, constant-power-load, frequency-dependent-load]
created: "2026-05-02"
updated: "2026-05-14"
---

# 负荷建模 (Load Modeling)

## 定义

负荷建模是用静态、动态或电磁暂态模型表示电力系统中各类用电设备在电压、频率、时间和控制状态变化下的功率响应特性。在 EMT 仿真中，负荷不是"被动消耗功率的黑盒子"，而是由大量终端用电设备（感应电动机、电力电子整流器、照明驱动、恒功率负载等）组成的**动态聚合体**。其核心挑战在于：不同设备类型在电压跌落、频率偏移、谐波畸变等扰动下的响应机制截然不同，而 EMT 仿真需要以足够快的时间步长（微秒至毫秒级）捕捉这些动态过程。

负荷建模的核心数学表达是**功率-电压-频率关系**。最基础的静态负荷用 ZIP 模型描述：

$$
P = P_0\left(a_z\left(\frac{V}{V_0}\right)^2 + a_i\frac{V}{V_0} + a_p\right),\qquad
Q = Q_0\left(b_z\left(\frac{V}{V_0}\right)^2 + b_i\frac{V}{V_0} + b_p\right)
$$

其中 $a_z, a_i, a_p$ 分别为恒阻抗、恒电流、恒功率分量比例（$a_z + a_i + a_p = 1$），$b_z, b_i, b_p$ 同理。ZIP 模型仅描述稳态电压依赖关系，不包含任何动态过程。

当需要描述频率依赖特性时，引入指数型频率-电压相关模型（如 fdLoad 所采用的形式）：

$$
P(f,V) = P_0\left(\frac{f}{f_0}\right)^{\alpha_f}\left(\frac{V}{V_0}\right)^{\alpha_v},\qquad
Q(f,V) = Q_0\left(\frac{f}{f_0}\right)^{\beta_f}\left(\frac{V}{V_0}\right)^{\beta_v}
$$

其中 $\alpha_f, \beta_f$ 为频率指数，$\alpha_v, \beta_v$ 为电压指数。典型电动机聚合负荷采用 $\alpha_f = 2.8$、$\beta_f = 1.8$（Fini 等 2026）。

动态电动机负荷还需要状态方程描述转速和电磁暂态：

$$
2H_m\dot{\omega}_r = T_e(V,\omega_r,x_m) - T_m(\omega_r)
$$

其中 $H_m$ 为惯性时间常数，$\omega_r$ 为转子机械角速度，$T_e$ 为电磁转矩，$T_m$ 为机械负载转矩。

## EMT 中的角色

负荷模型在 EMT 仿真中扮演三重角色：

1. **扰动响应放大器**：故障期间，感应电动机因转差增大而吸收大量无功，导致母线电压进一步跌落；故障清除后，大量电动机重合闸产生冲击电流，可能引发二次电压跌落。这一过程在 Hydro-Québec 实测数据中被验证：电压恢复至约 65% 额定值后，70% 的电机负荷在 20 ms 内完成重合闸（Torabi & Milani 2021）。

2. **频率动态调节器**：在低惯量电网中，负荷的频率依赖特性直接影响最大频率偏差和 UFLS（低频减载）动作。fdLoad 在 IEEE 39 节点系统上的研究表明，负荷频率相关性（$\alpha_f=2.8, \beta_f=1.8$）会显著影响事故期间的最大频率偏差，忽略该特性可能导致 UFLS 过早动作（Fini 等 2026）。

3. **非正弦工况边界条件**：恒功率负载在谐波电压下如果用传统的 $P/V$ 瞬时除法建模会产生功率计算误差；感性恒功率负载的 RMS 递推模型能在非正弦条件下保持恒定功率约束（Alboaouh 等 2025）。

## 负荷建模方法体系

负荷建模不是单一方法，而是根据仿真目标、时间尺度和负荷构成选择不同层级的模型。EMT 场景下主要存在四类方法：

### 1. 静态负荷模型（ZIP / 指数型）

**原理**：将负荷功率表示为电压和频率的代数函数，不包含任何状态变量。

ZIP 模型是最经典的静态负荷表示，其物理含义是将总负荷分解为三类等效元件的并联：
- **恒阻抗分量**（$a_z$）：如水加热器、电炉等电阻性负载，功率与 $V^2$ 成正比
- **恒电流分量**（$a_i$）：如部分照明设备，功率与 $V$ 成正比
- **恒功率分量**（$a_p$）：如电力电子整流器、变频器，功率与 $V$ 无关

扩展的电压-频率相关模型在 ZIP 基础上引入频率依赖：

$$
P = P_0\left(\frac{V}{V_0}\right)^{n_p}\left[1 + K_p\frac{f-f_0}{f_0}\right],\qquad
Q = Q_0\left(\frac{V}{V_0}\right)^{n_q}\left[1 + K_q\frac{f-f_0}{f_0}\right]
$$

其中 $n_p, n_q$ 为电压指数，$K_p, K_q$ 为频率系数。

**适用场景**：潮流初值、慢动态近似、不含大量电动机或电力电子负荷的简单配电系统。

**局限性**：无法描述电机失速/再加速、电力电子限流、频率动态等暂态过程。

### 2. 元件级综合负荷模型（Component-based Load Model）

**原理**：将配电母线上的综合负荷按终端设备类型分解为多个电路级子模型，每个子模型独立描述其物理动态，再按预设比例聚合到母线节点。

Torabi & Milani（2021）提出的元件级模型覆盖了以下终端设备类型：

| 设备类型 | 建模方法 | 核心状态量 |
|---------|---------|-----------|
| 开关电源(SMPS) | 等效电阻 $R_{eq} = v_{dc}^2 / P_{rated}$ | 直流侧电容电压 |
| 紧凑型荧光灯(CFL) | 充电态 $R_{eq,charging} = 11v_{dc} + 0.021v_{dc}^2 + 1300$；放电态 $R_{eq,discharging} = 23.7v_{dc} + 274$ | 电容充放电状态 |
| LED驱动 | 线性模型 $V_{thr} = 2.7\text{ V}, R_d = 0.3\ \Omega$ | — |
| 三相感应电机 | EMTP UM-40 通用电机模型 | 电磁状态 + 机械转速 |
| 单相感应电机 | EMTP UM-7 通用电机模型，二次方转矩特性 | 电磁状态 + 机械转速 |
| 变频驱动器(VSI) | PWM-VSI 模型，矢量控制 | 直流侧电压 + 电流环状态 |

**关键动态逻辑**：
- 电机接触器脱扣阈值：额定电压 45%~55% 区间，持续 1~3 个工频周波
- 电机重合闸逻辑：电压恢复至约 65% 后，延时 20 ms，70% 电机重新连接
- 单相电机机械负载：二次方转矩（$T_m \propto \omega_r^2$）经实测验证最优

**适用场景**：商业/居民配电负荷的电压暂降/恢复仿真、现场录波复现实验。

**局限性**：需要详细的负荷组成比例和现场扰动数据进行校验；不适用于工业负荷、高电力电子渗透率场景或未获取负荷构成数据的地区。

**量化验证**（Torabi & Milani 2021）：
- 商业案例（蒙特利尔购物中心，1.52 MW）：0.296 s 暂降期间三相电压最大跌落 67.9%，仿真电流谐波频谱与实测数据吻合
- 居民案例 1（4.5 MW）：0.8 s 故障期间电压跌落约 66%，二次方转矩模型全程平滑过渡
- 居民案例 2（7 MW，含 1.5 MW 工业电机）：工业电机在暂降开始后 3 个周波脱扣，负荷降至 5.5 MW，损失占比约 21.4%

### 3. 频率相关负荷综合模型（fdLoad）

**原理**：将指数型频率相关负荷转化为等效导纳，再用 Vector Fitting 在目标频带内拟合为有理函数，展开为常数 R-L-C 支路网络，使负荷频率特性以真实网络支路形式进入节点方程。

fdLoad 的核心流程：

1. **目标导纳构造**：在 $V \approx V_0$ 条件下，将功率模型转为导纳
   $$Y(f) = \frac{P(f) - jQ(f)}{V^2}$$

2. **Vector Fitting 拟合**：在关注频带内采样 $Y(f)$，拟合为有理函数
   $$Y(s) = K_0 + \frac{K_1}{s + p_1} + sK_2$$

3. **部分分式展开**：将常数项、一阶极点项和 $s$ 项映射为并联电阻、串联 R-L 支路和电容支路：
   $$Y(\omega) = \frac{1}{R_2} + \frac{1}{R_1 + j\omega L} + j\omega C$$

**IEEE 39 节点系统验证**（Bus 15 示例）：
- 基准参数：$P_0 = 306\text{ MW}, Q_0 = 152\text{ MVar}, V_0 = 350.52\text{ kV}$
- 拟合频带：57–63 Hz（60 Hz 附近 ±3 Hz）
- 合成参数：$L = -1.8\text{ mH}, R_1 = -4.96\ \Omega, R_2 = 4.99\ \Omega, C = -75.1\ \mu\text{F}$
- 最大拟合误差：约 0.5%

**适用场景**：低惯量系统频率摆动仿真、UFLS 整定分析、SFA-EMT 仿真。

**局限性**：固定/近似在 $V=V_0$ 附近，对强电压动态、负荷组成变化或动态恢复负荷的适用性未验证；验证限于 IEEE 39 节点系统。

### 4. 感性恒功率负载模型（Inductive Constant Power Load）

**原理**：传统恒功率负载用 $P/V$ 瞬时除法在 EMT 中实现，但此方法在非正弦条件下失效。Alboaouh 等（2025）提出将全周期 RMS 约束转化为逐时间步递推计算框架。

模型将负载视为 RL 串联电路，通过 KVL/KCL 建立瞬时量与 RMS 量的递推关系：

$$
(i_{rms,n})^2 = (i_{t,n})^2 + I_{n-1},\quad
(v_{Rrms,n})^2 = (v_{Rt,n})^2 + V_{R,n-1},\quad
(v_{Lrms,n})^2 = (v_{Lt,n})^2 + V_{L,n-1}
$$

其中 $I_{n-1}, V_{R,n-1}, V_{L,n-1}$ 为历史累计平方项。功率约束为：

$$
P_n = i_{rms,n} \cdot v_{Rrms,n},\quad
Q_n = i_{rms,n} \cdot v_{Lrms,n},\quad
pf_n \cdot v_{rms,n} = v_{Rrms,n}
$$

**适用场景**：需要严格保持恒定有功/无功功率和固定功率因数的 EMT 仿真，尤其适用于含谐波的电力电子接口负荷。

**局限性**：面向感性负载，对容性负载需另行推导；原文未报告大系统算例验证。

## 形式化表达

### 负荷模型分类矩阵

| 模型类型 | 数学形式 | 状态变量 | 时间尺度 | 典型应用 |
|---------|---------|---------|---------|---------|
| ZIP 静态 | $P = P_0(a_z(V/V_0)^2 + a_i(V/V_0) + a_p)$ | 无 | 稳态 | 潮流初值 |
| 指数型 V-f 相关 | $P(f,V) = P_0(f/f_0)^{\alpha_f}(V/V_0)^{\alpha_v}$ | 无 | 准稳态 | 频率动态 |
| fdLoad 网络综合 | $Y(\omega) = 1/R_2 + 1/(R_1+j\omega L) + j\omega C$ | R-L-C 支路 | EMT | SFA-EMT 频率摆动 |
| 元件级综合 | 多子电路并联聚合 | 电机转速/电磁状态 | EMT | 电压暂降/恢复 |
| 恒功率 RMS 递推 | $(i_{rms,n})^2 = (i_{t,n})^2 + I_{n-1}$ | 历史累计平方 | EMT | 非正弦恒功率负载 |
| 感应电动机 | $2H_m\dot{\omega}_r = T_e - T_m$ | $\omega_r, \psi$ | EMT/机电 | 电机负载动态 |

### ZIP 模型扩展形式

考虑不平衡三相运行时，各相 ZIP 参数可能不同：

$$
P_a = P_0\left(a_{z,a}\left(\frac{V_a}{V_0}\right)^2 + a_{i,a}\frac{V_a}{V_0} + a_{p,a}\right)
$$

### 电动机转矩-转速特性

二次方转矩负载：$T_m = T_0(\omega_r/\omega_0)^2$
恒转矩负载：$T_m = T_0$

## 关键技术挑战

### 1. 负荷构成辨识

现场测量通常只能得到总 P、Q 和潮流 ZIP 系数，无法区分各类终端设备的具体占比。Torabi & Milani（2021）通过 Hydro-Québec 现场录波数据反推负荷组成比例，但这一过程需要：
- 特定扰动事件（电压暂降）的录波数据
- 对终端设备类型和数量的先验知识
- 迭代调整负荷组成比例直至仿真与实测匹配

### 2. 大扰动下的模型外推

LOADSYN 模型库仅保证电压变化 < 15%、频率变化 < 5% 范围内的精度（Khodabakhchian 2004）。在故障等大扰动场景下（电压跌落 36%），感应电动机的零起动转矩特性、配电变压器饱和效应会显著影响负荷响应。EMTP 通用电机模型（UM-7/UM-40）通过参数整定扩展了有效电压范围至 0.5–1.5 pu。

### 3. 非正弦工况下的恒功率约束

电力电子负荷在谐波电压下维持恒定功率是一个建模难题。传统 $P/V$ 瞬时除法在非正弦条件下会产生功率波动（Alboaouh 等 2025）。RMS 递推模型通过历史状态变量实现了逐时间步的恒功率约束，但仅适用于感性负载。

### 4. 聚合负荷的信息丢失

将大量终端设备聚合为单一 ZIP 或指数模型会掩盖：
- 单相不平衡导致的零序电流
- 局部电动机失速与再加速的时序差异
- 电力电子负荷控制参数的分散性

## 量化性能边界

| 指标 | 数值 | 来源 |
|------|------|------|
| LOADSYN 有效电压范围 | 0.85–1.15 pu（±15%） | Khodabakhchian 2004 |
| EMTP 扩展负荷模型有效电压范围 | 0.5–1.5 pu（±50%） | Khodabakhchian 2004 |
| 电机接触器脱扣阈值 | 45%–55% 额定电压，持续 1–3 周波 | Torabi & Milani 2021 |
| 电机重合闸冲击 | 电压恢复至 ~65% 后 20 ms，70% 电机重连 | Torabi & Milani 2021 |
| fdLoad 拟合最大误差 | 57–63 Hz 范围内约 0.5% | Fini 等 2026 |
| SFA-EMT 步长优势 | 0.9 Hz 频偏下 55 ms vs 传统 EMT 0.8 ms（70 倍） | Fini 等 2026 |
| 恒功率 RMS 递推稳态误差 | < 0.5% | Alboaouh 等 2025 |
| 商业馈线电压暂降最大跌落 | 67.9%（三相分别 67.9%/64.0%/62.8%） | Torabi & Milani 2021 |
| 居民馈线电机脱扣负荷损失 | 1.5 MW / 7 MW ≈ 21.4% | Torabi & Milani 2021 |

## 适用边界与选择指南

### 方法选择决策树

```
                    负荷建模需求
                         │
              ┌──────────┼──────────┐
              │          │          │
        需要暂态动态？   需要频率动态？  仅需稳态
              │          │          │
          是 │          │ 是        │ 否
              │          │          │
    ┌─────────┼──────────┼───────┐  │
    │         │          │       │  │
  含大量    低惯量    一般    仅电压  ZIP/
  电动机？  系统？    场景    依赖    指数型
    │       │         │       │     模型
  是 │       │    是 │ 否    │     │
    │       │     │   │       │     │
 元件级   fdLoad  元件级  扩展   ZIP
 综合模型 │ 或详细  综合   ZIP   │
         │ 电动机  │       │   扩展
       恒功率   模型   │       │
       RMS递推 │       │     │
              │       │     │
         ┌────┴───────┴─────┘
         │
    非正弦工况？
         │
      是 │ 否
         │
    感性？
         │
    是 → RMS递推
    否 → 详细模型
```

### 场景-方法推荐表

| 应用场景 | 推荐模型 | 理由 |
|---------|---------|------|
| 电压暂降/恢复研究 | 元件级综合模型 | 需捕捉电机脱扣/重合闸动态 |
| 低惯量频率摆动 | fdLoad + SFA-EMT | 频率隐式纳入节点方程 |
| 电力电子接口负荷 | 恒功率 RMS 递推 | 非正弦下保持恒功率约束 |
| 潮流初值/慢动态 | ZIP / 指数型 | 计算成本低，足够精确 |
| 大扰动暂态稳定 | EMTP 扩展负荷模型 | 宽电压范围物理一致性 |
| 配电网不平衡研究 | 元件级综合模型（单相电机） | 需区分三相不平衡响应 |

## 相关方法 / 相关模型 / 相关主题

- [[load-model]] — 负荷模型总览页，承载具体模型结构
- [[induction-machine-model]] — 感应电动机模型，动态负荷的核心组件
- [[constant-power-load]] — 恒功率负载模型，电力电子负荷的基础表示
- [[emt-simulation]] — 电磁暂态仿真，负荷建模的应用场景
- [[transient-stability-analysis]] — 暂态稳定分析，负荷对首摆稳定的影响
- [[small-signal-stability]] — 小信号稳定性，负荷阻抗特性对稳定性的影响
- [[frequency-dependent-modeling]] — 频率相关建模，fdLoad 的技术基础
- [[power-flow-calculation]] — 潮流计算，负荷作为稳态输入
- [[dynamic-phasor]] — 动态相量法，负荷频率动态的另一种建模途径
- [[frequency-dependent-modeling]] — 频率相关建模（已列于上方）

## 来源论文

- **Khodabakhchian 2004** — 基于 LOADSYN 数据库的混合居民-商业负荷 EMTP 详细模型，突破 ±15% 电压限制至 ±50%，现场录波验证（Brossard 变电站单相接地故障，正序电压跌落 17.5%）
- **Torabi & Milani 2021** — 元件级综合负荷模型，涵盖 SMPS、CFL、LED、感应电机、变频驱动器等终端设备，Hydro-Québec 电压暂降现场数据验证（商业/居民馈线，电机脱扣阈值 45%–55%）
- **Fini 等 2026** — fdLoad 频率相关负荷综合模型，Vector Fitting 网络综合 + SFA-EMT 集成，IEEE 39 节点系统验证（57–63 Hz 拟合误差 0.5%，步长 70 倍优势）
- **Alboaouh 等 2025** — 感性恒功率负载 RMS 递推模型，逐时间步求解，非正弦工况验证（稳态误差 < 0.5%，O(1) 每步计算复杂度）

## 来源论文

| 论文 | 年份 |
|------|------|
| [[modeling-a-mixed-residential-commercial-load-for-simulations-involving-large-dis|Modeling A Mixed Residential-commercial Load  For Simulation]] | 2004 |
| [[39pes20116039582|39/pes.2011.6039582]] | 2011 |
| [[dynamic-average-modeling-of-front-end-diode-rectifier-loads-considering-13&14|Dynamic Average Modeling of Front-End Diode Rectifier Loads ]] | 2011 |
| [[development-of-data-translators-for-interfacing-13&14|Development of Data Translators for Interfacing Power-Flow P]] | 2013 |
| [[multi-fpga-digital-hardware-design-iet-gtd|Multi-FPGA digital hardware design for detailed large-scale ]] | 2013 |
| [[development-and-validation-of-a-new-detailed-emt-type-component-based-load-model|Development and Validation of a New Detailed EMT-type Compon]] | 2021 |
| [[loop-closing-analytical-calculation-system-based-on-electromagnetic-electromecha|Loop closing analytical calculation system based on electrom]] | 2023 |
| [[fpga-based-simulation-of-grid-tied-converters-using-frequency-dependent-network-|FPGA-based simulation of grid-tied converters using frequenc]] | 2025 |
| [[modeling-of-inductive-constant-power-load-for-electromagnetic-transient-simulati-26|Modeling of inductive constant power load for electromagneti]] | 2025 |
