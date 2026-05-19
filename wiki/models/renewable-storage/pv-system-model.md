---
title: "光伏系统 (PV System)"
type: model
tags: [pv-system, photovoltaic, solar, inverter, mppt, lvrt, grid-forming, grid-following]
created: "2026-04-29"
updated: "2026-05-19"
---

# 光伏系统 (Photovoltaic System)

## 定义与概述

光伏系统（PV System）将太阳能通过光伏电池的光生伏打效应转换为电能，是可再生能源发电的核心形式。光伏系统由光伏阵列（PV Array）和并网逆变器组成，通过最大功率点跟踪（MPPT）实现太阳能的高效利用，并通过低电压穿越（LVRT）功能保障故障期间的系统稳定性。

在EMT仿真中，光伏系统的建模涉及两个核心层次：① 光伏电池的物理电气特性（I-V非线性特性、温度/辐照度响应）；② 并网逆变器的控制系统（MPPT、PLL、电流环、LVRT）。根据仿真精度和计算效率需求，光伏逆变器可采用开关模型（SW）、电压插值模型（VI）、平均值模型（AV）、受控电流注入模型（CCI）或简化电流注入模型（SCI）五种建模方法。

**核心挑战**：光伏系统的EMT建模面临多时间尺度耦合（毫秒级开关纹波与秒级MPPT响应）、强非线性（光伏电池I-V特性）、以及大规模光伏电站的聚合等效等挑战。

## 1. 物理对象与数学描述

### 1.1 光伏电池单二极管模型

#### 等效电路

光伏电池的单二极管模型等效电路如所示：电流源 $I_{ph}$（光生电流）与并联二极管、并联电阻 $R_{sh}$ 串联，再经串联电阻 $R_s$ 输出。

#### 输出特性方程

$$I = I_{ph} - I_0 \left[\exp\left(\frac{V + IR_s}{V_t}\right) - 1\right] - \frac{V + IR_s}{R_{sh}}$$

其中热电压 $V_t = \frac{N_s k T A}{q}$，$N_s$ 为串联电池数，$k$ 为玻尔兹曼常数，$T$ 为绝对温度，$A$ 为理想因子，$q$ 为电子电荷。

#### 参数温度依赖性

光生电流的温度和辐照度依赖关系：

$$I_{ph}(T, G) = I_{ph,ref} \left[1 + \alpha_{sc}(T - T_{ref})\right] \frac{G}{G_{ref}}$$

反向饱和电流的温度依赖：

$$I_0(T) = I_{0,ref} \left(\frac{T}{T_{ref}}\right)^3 \exp\left[\frac{qE_g}{nk}\left(\frac{1}{T_{ref}} - \frac{1}{T}\right)\right]$$

开路电压温度系数：

$$V_{oc}(T) = V_{oc,ref} \left[1 + \beta_{oc}(T - T_{ref})\right]$$

典型值（标准测试条件 $G_{ref} = 1000\text{ W/m}^2$，$T_{ref} = 25°C$）：$V_{mpp}/V_{oc} \approx 0.75$–$0.80$，$I_{mpp}/I_{sc} \approx 0.90$。

### 1.2 最大功率点跟踪（MPPT）

#### 扰动观察法（P&O）

扰动观察法通过周期性扰动光伏阵列端电压并比较输出功率变化来追踪最大功率点：

$$\Delta P = P(k) - P(k-1)$$
$$V_{ref}(k+1) = V_{ref}(k) + \Delta V \cdot \text{sign}(\Delta P)$$

当功率增加时维持扰动方向，功率减小时反向扰动。P&O在辐照度快速变化时可能产生振荡或误跟踪。

#### 增量电导法（IncCond）

增量电导法利用光伏阵列功率对电压导数的符号特性：

$$\frac{dP}{dV} = I + V \frac{dI}{dV}$$

- $dP/dV > 0$：工作点在MPP左侧 → 增加电压
- $dP/dV = 0$：工作在MPP
- $dP/dV < 0$：工作点在MPP右侧 → 减小电压

等价判据：$\frac{dI}{dV} = -\frac{I}{V}$ 时达到最大功率点。增量电导法在稳态辐照下MPPT跟踪效率可达99%以上（Hariri 2016）。

### 1.3 并网逆变器控制结构

#### 三环控制架构

光伏逆变器采用嵌套三环控制：功率外环 → 电流内环 → PWM调制。

**功率外环**（直流电压控制）：

$$i_{d,ref} = k_{p,dc}(V_{dc,ref} - V_{dc}) + k_{i,dc} \int (V_{dc,ref} - V_{dc})dt$$

无功功率控制：

$$i_{q,ref} = -\frac{Q_{ref}}{1.5V_d}$$

**电流内环**（dq旋转坐标系）：

$$v_d^* = v_d + \omega L i_q - k_{p,c}(i_{d,ref} - i_d) - k_{i,c} \int (i_{d,ref} - i_d)dt$$

$$v_q^* = v_q - \omega L i_d - k_{p,c}(i_{q,ref} - i_q) - k_{i,c} \int (i_{q,ref} - i_q)dt$$

**PLL同步**：

$$\omega = \omega_0 + k_{p,pll} \cdot v_q + k_{i,pll} \int v_q dt$$

## 2. EMT建模方法（五模型精度-效率映射）

光伏并网逆变器的EMT建模根据精度和计算效率需求，可选用五种建模方法（Sano 2022）。

### 2.1 开关模型（Switching Model, SW）

SW模型是最详细的逆变器EMT建模方法，模拟IGBT/二极管的实际开断操作。每个功率器件独立建模（理想开关、串联电阻等），包含完整的逆变器电路和控制电路。

**特点**：
- 步长要求：$\Delta t \ll T_{sw}$（开关周期），通常 $\Delta t \leq 1$–$5\mu s$
- 可模拟开关纹波、谐波、暂态响应
- 计算成本最高

**数学表达**：每个桥臂输出两电平PWM电压，通过比较调制信号与三角载波生成开关函数 $s_{ap}, s_{an} \in \{0, 1\}$。

$$v_{ab} = s_{ap} V_{dc} - s_{an} V_{dc}$$

### 2.2 电压插值模型（Voltage Interpolation Model, VI）

VI模型在较大步长下通过插值PWM电压跳变时刻来保持开关精度。核心是在开关转换时刻 $t_{rise}, t_{fall}$ 前后插入插值电压（VI model）：

$$v_{interp} = v_{ref}^* + \frac{v_{ref}^* - v_{ref}}{t_{rise} - t_{fall}}(t - t_{fall})$$

其中 $v_{ref}^*$ 为上一时刻电压参考值，$v_{ref}$ 为当前时刻电压参考值。采样与三角载波同步更新。

**特点**：
- 步长要求：$\Delta t \leq T_{sw}/10$，但可大于SW模型的最小步长
- 精度：可保留开关纹波和高次谐波
- 计算成本：约为SW模型的60–70%

**Sano 2022验证**：VI模型在谐波分析中与SW模型高度吻合，同时计算时间显著降低。

### 2.3 平均值模型（Average-Value Model, AV）

AV模型以受控电压源替代PWM开关动作，在一个载波周期内对电压取平均值：

$$v_{abc} = m_{abc} \cdot \frac{V_{dc}}{2}$$

其中 $m_{abc}$ 为三相调制比。直流侧电容动态：

$$C_{dc} \frac{dV_{dc}}{dt} = I_{pv} - I_{dc}$$

$$I_{dc} = \frac{3}{4} \sum_{k=a,b,c} m_k i_k$$

**特点**：
- 步长要求：$\Delta t \leq 50\mu s$（受电流环带宽限制）
- 精度：不包含开关纹波，交流电流不含开关谐波
- 计算成本：显著低于SW和VI模型
- 适用场景：系统级稳定性分析、长时间暂态仿真

**适用范围**：当研究重点不在逆变器自身谐波、而在系统网络响应时，AV模型是最佳选择（Sano 2022 Section VI）。

### 2.4 受控电流注入模型（Controlled Current-Injection Model, CCI）

CCI模型使用受控电流源代替电压源，保留了功率控制环节（直流电压环、无功功率环），但不含电流内环和PWM调制：

$$i_{d,ref} = f_{dc}(V_{dc,ref} - V_{dc}), \quad i_{q,ref} = f_Q(Q_{ref})$$

交流侧电流直接注入：

$$i_{abc} = \sqrt{\frac{2}{3}} \begin{bmatrix} i_d \cos(\omega t) - i_q \sin(\omega t) \\ i_d \cos(\omega t - 120°) - i_q \sin(\omega t - 120°) \\ i_d \cos(\omega t + 120°) - i_q \sin(\omega t + 120°) \end{bmatrix}$$

**特点**：
- 步长要求：与AV模型相当
- 精度：保留了功率控制动态，但不含电流环和PWM
- 计算成本：比SCI模型高60%（Sano 2022），但保留了功率控制
- 改进：相比SCI模型，CCI保留了电压/电流内环的等效效果，精度更高

### 2.5 简化电流注入模型（Simplified Current-Injection Model, SCI）

SCI模型以最简电流源替代逆变器，有功功率参考形成与电网电压同相的电流，无功功率参考形成正交电流：

$$i_d = \frac{P_{ref}}{V_{rms}}, \quad i_q = \frac{Q_{ref}}{V_{rms}}$$

**特点**：
- 不含任何控制环节，无直流侧建模
- 步长要求：可使用较大步长
- 精度：最低，仅适合潮流分析和稳态运行工况
- 计算成本：最低

**不适用场景**：故障分析、LVRTV/HVRT、谐波分析

### 五模型对比

| 模型 | 控制环节 | 功率器件 | 步长要求 | 计算成本 | 谐波精度 |
|------|---------|---------|---------|---------|---------|
| SW | 全部 | 是 | ≤$1$–$5\mu s$ | 100%（基准） | 最高 |
| VI | 全部 | 插值 | $\leq T_{sw}/10$ | 60–70% | 高 |
| AV | 功率外环 | 等效电压源 | $\leq 50\mu s$ | 较低 | 低（无纹波） |
| CCI | 功率外环 | 等效电流源 | $\leq 50\mu s$ | 较低 | 低 |
| SCI | 无 | 无 | 大步长 | 最低 | 无 |

**模型选择指南**（Sano 2022）：
- **谐波分析**（开关纹波、低次谐波）：VI模型
- **系统级稳定性/长时间仿真**：AV模型或CCI模型
- **故障分析/LVRT**：SW模型或VI模型（必须保留控制动态）
- **潮流初始化/稳态运行**：SCI模型

## 3. 低电压穿越（LVRT）与故障响应

### 3.1 LVRT要求

根据IEEE 1547-2018标准，光伏系统在电网故障期间必须保持并网：

| 电压跌落程度 | 要求 | 无功电流注入 |
|------------|------|------------|
| $V \geq 90\%$ | 正常运行 | — |
| $90\% > V \geq 50\%$ | 低电压穿越，不脱网 | $I_q \geq 1.5 \times (0.9 - V_{pu}) \times I_N$ |
| $50\% > V \geq 20\%$ | 低电压穿越，不脱网 | $I_q \geq 1.5 \times (0.9 - V_{pu}) \times I_N$ |
| $V < 20\%$ | 允许脱网 | — |

**无功支撑响应时间**：< 30 ms。

### 3.2 LVRT期间逆变器等效建模

LVRT期间逆变器需要在无功支撑和有功控制之间平衡。构网型（GFM）逆变器（如Nguyen 2021的PV-电池混合电站）可通过有功-频率/无功-电压下垂特性自主建立交流电压，支撑黑启动：

$$f = f_0 + k_{p,f} \cdot (P_{ref} - P_{meas})$$
$$V = V_0 + k_{q,v} \cdot (Q_{ref} - Q_{meas})$$

## 4. 典型参数

### 4.1 光伏组件参数（典型值）

| 参数 | 单晶硅 | 多晶硅 | 薄膜 |
|------|--------|--------|------|
| 额定功率 | 300–500 W | 250–350 W | 100–150 W |
| 开路电压 $V_{oc}$ | 40–50 V | 35–45 V | 50–80 V |
| 短路电流 $I_{sc}$ | 9–11 A | 8–10 A | 2–4 A |
| MPP电压 $V_{mpp}$ | 33–42 V | 28–37 V | 40–65 V |
| MPP电流 $I_{mpp}$ | 8–10 A | 7–9 A | 2–3 A |
| 转换效率 | 18–22% | 15–18% | 10–13% |
| 温度系数 | $-0.3\%/°C$ | $-0.4\%/°C$ | $-0.2\%/°C$ |

### 4.2 逆变器参数

| 参数 | 组串式（50 kW） | 集中式（1 MW） |
|------|---------------|----------------|
| 直流电压范围 | 200–1000 V | 500–1500 V |
| 最大效率 | 98–99% | 98.5–99% |
| 功率因数 | ±0.9可调 | ±0.9可调 |
| THD | < 3% | < 3% |
| 直流电容 | 5–10 mF | 50–100 mF |
| 开关频率 | 16–20 kHz | 2–4 kHz |

## 5. 量化性能边界

**光伏电池模型精度**（Cao 2023、Nguyen 2021）：
- 光伏阵列诺顿等效模型在FPGA上实现亚微秒级仿真步长，满足开关级EMT精度（Cao 2023）
- 非线性I-V特性通过动态电导线性化：$G_{dio} = I_0 \cdot \exp(v_{dio}/V_T)/V_T$，线性化误差由等效历史电流源补偿（Cao 2023）
- 构网型光储混合电站黑启动仿真稳态电压幅值与数值优化解匹配误差 < 1%（Nguyen 2021）
- 黑启动全过程 18 s（7步），母线电压恢复时间 < 0.2 s（Nguyen 2021）

**MPPT性能**（Hariri 2016、Di Fazio 2012）：
- 增量电导法（IncCond）MPPT跟踪效率在稳态辐照下可达99%以上
- P&O法在辐照快速变化时可能产生振荡或误跟踪，响应速度取决于步长和采样频率
- 光伏组件温度系数：单晶硅$-0.3\%/°C$，多晶硅$-0.4\%/°C$，薄膜$-0.2\%/°C$

**大规模仿真加速**（Cao 2023）：
- FPGA平台多微电网系统仿真实现51倍超实时加速
- 光伏阵列诺顿等效将非线性电路转化为两节点线性网络，大幅降低节点导纳矩阵维度

**数据缺口声明**：单二极管模型参数（$I_{ph}$、$I_0$、$n$、$R_s$、$R_{sh}$）在不同辐照和温度条件下的标准提取数据集缺乏统一公开数据库。不同光伏组件技术（单晶硅/多晶硅/薄膜/双面/钙钛矿）在EMT仿真中的模型精度对比缺乏系统性研究。

## 6. 适用边界与限制

### 6.1 适用条件

- **辐照度范围**：100–1200 W/m²（超出此范围模型误差增大）
- **温度范围**：$-20°C$ 至 $+60°C$
- **直流电压范围**：200–1500 V（由组件串联配置决定）
- **电网条件**：电压±10%，频率±0.5 Hz

### 6.2 模型限制

- **单二极管模型**：不适用于双面组件和局部遮挡场景
- **温度均匀性假设**：实际组件温度分布不均匀
- **阴影遮挡**：需采用更复杂的双二极管模型或分块模型
- **老化退化**：需叠加衰减模型

### 6.3 模型选择决策表

| 应用场景 | 推荐模型 | 原因 |
|---------|---------|------|
| 谐波共振分析 | SW或VI | 必须保留开关纹波 |
| LVRT/故障穿越 | SW或VI | 必须保留控制动态 |
| 系统级稳定性分析 | AV或CCI | 长时间仿真需效率 |
| 潮流初始化 | SCI | 仅需稳态功率流 |
| 黑启动 | GFM+AV | 自主建立电压源 |

## 相关方法

- [[numerical-integration|数值积分]] — 光伏特性与MPPT计算
- [[state-space-method|状态空间法]] — 逆变器控制分析
- [[average-value-model|平均值模型]] — 逆变器系统级仿真
- [[coordinate-transformation-model|坐标变换模型]] — dq控制实现
- [[vector-fitting|矢量拟合]] — 频域阻抗建模

## 相关模型

- [[gfl-inverter-model|跟网型变流器]] — 光伏逆变器基本控制
- [[vsc-model|VSC模型]] — 电压源变换器通用框架
- [[pll-model|锁相环]] — 并网同步
- [[pi-controller-model|PI控制器]] — 功率环/电流环
- [[igbt-model|IGBT模型]] — 开关器件
- [[grid-forming-control|构网型控制]] — 自主电压建立

## 相关主题

- [[vsc-hvdc|VSC-HVDC]] — 光伏集中外送
- [[renewable-energy-integration|新能源并网]] — 光伏接入电网
- [[power-quality|电能质量]] — 谐波与闪变
- [[low-voltage-ride-through|低电压穿越]] — 故障穿越能力
- [[real-time-simulation|实时仿真]] — FPGA/硬件加速

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

## 来源论文

| 论文 | 年份 | 贡献说明 |
|------|------|---------|
| Sano等 - Comparison and Selection of Grid-Tied Inverter Models for Accurate and Efficient EMT Simulations | 2022 | 五模型精度-效率映射（SW/VI/AV/CCI/SCI）系统对比 |
| Nguyen等 - Control and Simulation of a Grid-Forming Inverter for Hybrid PV-Battery Plants in Power System Black Start | 2021 | PV-电池构网型黑启动控制与EMT建模 |
| Cao等 - Faster-Than-Real-Time Hardware Emulation of Transients and Dynamics of a Grid of Microgrids | 2023 | FPGA超实时51倍加速，诺顿等效建模 |
| Agudelo等 - Switch-Averaged Frequency Domain Simulation of Photovoltaic Systems | 2023 | 频域开关平均PV系统仿真 |
| Hariri & Faruque - A Hybrid Simulation Tool for the Study of PV Integration Impacts | 2017 | 混合仿真框架 |