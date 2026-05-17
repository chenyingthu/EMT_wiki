---
title: "无功补偿装置 (Reactive Compensation Device)"
type: model
tags: [reactive-compensation, svc, statcom, facts, voltage-control, tcsc, shunt]
created: "2026-05-02"
updated: "2026-05-17"
---

# 无功补偿装置 (Reactive Compensation Device)

## 定义与边界

无功补偿装置是在交流电网节点或线路中调节无功交换、支撑电压和改变等效阻抗的设备族。按照接入方式，分为并联补偿（shunt compensation）和串联补偿（series compensation）两大类。并联补偿向电网注入或吸收无功电流，典型装置包括机械投切的并联电容器/电抗器、同步调相机、基于晶闸管的静止无功补偿器（SVC）、基于电压源换流器的静止同步补偿器（STATCOM）。串联补偿串联在线路中改变等效阻抗，典型装置是晶闸管控制串联电容补偿器（TCSC）。

在 EMT 仿真中，无功补偿装置的模型边界需要注意：
- SVC 和 STATCOM 属于并联动态无功装置，建模核心是受控电纳或受控电流源
- TCSC 属于串联补偿装置，其模型在 [[tcsc-model]] 中讨论，不应与并联无功源混写
- 同步调相机以同步电机电磁和机械状态提供无功支撑，其 EMT 模型应接入 [[synchronous-machine-model]]，不是简单的静态无功源
- [[facts]] 是柔性交流输电系统的主题入口

## EMT 中的角色

在 EMT 仿真中，无功补偿装置解决以下核心问题：

**电压支撑与无功调节**：在电网节点或线路中注入无功功率，平抑电压波动和维持系统电压稳定。SVC 和 STATCOM 的响应时间在数十毫秒级（电网动态），但其开关动作和谐波特性需要在 EMT 中以小步长描述。

**谐波与波形质量**：晶闸管开关动作产生特征谐波（TCR 典型为 5、7、11、13 次），滤波器设计需要精确的开关暂态波形。

**故障穿越与保护动作**：故障期间无功补偿装置的电流限幅、直流过压、闭锁行为对系统动态影响显著，需要详细模型。

**混合仿真接口**：大规模电网中，无功补偿装置通常只占据局部网络，EMT 与机电暂态程序（TSP）的接口需要动态相量法或诺顿等值。

## EMT 建模方法

### 1. 详细开关模型（Detailed Switch Model）

**原理**：保留每个半导体器件的离散开关状态（导通/关断），在每个仿真步长中精确求解电路拓扑变化。

**数学表达**：晶闸管用 Ron/Roff 电阻模型：
$$
R_{\text{on}} = 10^{-3}\ \Omega,\quad R_{\text{off}} = 10^{6}\ \Omega,\quad \eta = R_{\text{off}}/R_{\text{on}} = 10^{9}
$$
TCR 的触发角 $\alpha$ 控制晶闸管导通时刻，在一个工频周期内：
$$
\sigma = \pi - 2\alpha \quad \text{（导通角）}
$$
等效电纳为：
$$
B_{\text{TCR}}(\alpha) = \frac{\sigma - \sin\sigma}{\pi X_L}
$$
其中 $X_L = \omega L$ 为 TCR 感抗。

**特点**：最高精度，保留全部开关暂态和特征谐波；计算代价最高，每步需更新拓扑和雅可比矩阵。

**适用场景**：谐波分析、投切暂态、保护动作验证、HIL 实时仿真接口。

**失效场景**：大规模长期规划扫描（计算量不可接受）。

### 2. 受控电纳模型（Controlled Susceptance Model）

**原理**：将 TCR/TSC 等效为随触发角或控制目标连续可调的等效电纳，忽略开关暂态细节，在每个基频周期或控制周期内保持电纳值恒定。

**数学表达**：对于 TSC，固定电容电纳为：
$$
B_{\text{TSC}} = \frac{1}{\omega L_C}
$$
无功功率为：
$$
Q_{\text{TSC}} = V^2 \cdot B_{\text{TSC}}
$$
对于 TCR，触发角 $\alpha$ 连续可调，等效电纳 $B_{\text{TCR}}$ 与 $\alpha$ 成正弦函数关系：
$$
B_{\text{TCR}}(\alpha) = \frac{2(\pi - \alpha) - \sin(2\pi - 2\alpha)}{\pi \omega L}
$$

**特点**：中等计算效率，保留控制环响应；不能描述谐波和开关暂态。

**适用场景**：控制策略验证、系统级 EMT、重复扰动研究。

**失效场景**：器件损耗、阀级应力、开关谐波分析。

### 3. 动态相量模型（Dynamic Phasor Model）

**原理**：利用时变傅里叶系数将开关波形表示为有限阶动态相量，将 EMT 中的三相瞬时值模型降阶为单相等效电路，大幅增大积分步长。

**数学表达**：时域波形 $x(t)$ 在时间窗口 $[t-T, t]$（$T$ 为工频周期）内展开为傅里叶级数：
$$
x(t) = \sum_{k=-\infty}^{\infty} X_k(t) e^{jk\omega_0 t}
$$
其中 $k$ 阶动态相量定义为：
$$
X_k(t) = \frac{1}{T}\int_{t-T}^{t} x(\tau)e^{-jk\omega_0\tau}d\tau
$$
动态相量的微分性质：
$$
\frac{dX_k(t)}{dt} = \frac{d}{dt}\left\langle x(t)\right\rangle_k = \left\langle \frac{dx(t)}{dt}\right\rangle_k - jk\omega_0 X_k(t)
$$

对于 TCR 的 DP 模型（基波 $k=1$），电压方程：
$$
V_k = j\omega_0 L \cdot I_k + R \cdot I_k + j\frac{2}{\pi}(1-\cos\sigma)V_k^{\text{ac}}
$$
电感电流动态（复数形式）：
$$
\frac{dI_1}{dt} = \frac{j\omega_0 L}{L^2+R^2}\left[-R\cdot I_1 + V_{\text{ac}}\right]
$$
电容电压动态：
$$
\frac{dV_1}{dt} = \frac{1}{C}\cdot I_1
$$

**特点**：步长可提升 200-400 倍（从 EMTP 典型值 $50\ \mu\text{s}$ 至 $0.01\text{-}0.02\ \text{s}$）；适用于混合仿真接口。

**适用场景**：大规模机电-电磁混合仿真、SVC/STATCOM 的系统级动态分析。

**失效场景**：不平衡故障、保护暂态的谐波截断误差尚未系统评估（E Zhijun 2009）。

### 4. 诺顿等值接口模型（Norton Equivalent Interface Model）

**原理**：将无功补偿装置用诺顿等值电路（电流源 $I_{\text{eq}}$ + 导纳 $Y_{\text{eq}}$）表示，在混合仿真接口处与外部系统连接。

**数学表达**：诺顿等值参数由 DP 模型在接口频率下计算：
$$
I_{\text{eq}} = I_1 \cdot e^{j\phi_1},\quad Y_{\text{eq}} = \frac{I_{\text{eq}}}{V_{\text{bus}}}
$$
戴维南等值参数：
$$
V_{\text{th}} = \frac{I_{\text{eq}}}{Y_{\text{eq}}},\quad Z_{\text{th}} = \frac{1}{Y_{\text{eq}}}
$$

**特点**：接口形式简洁，便于与 TSP 或其他子系统耦合。

**适用场景**：EMT-TSP 混合仿真、多速率仿真接口。

### 5. 链式 STATCOM 快速等效模型（Fast Equivalent Model for Cascaded STATCOM）

**原理**：利用 H 桥换流链端口关系和可变电阻开关模型，将每个功率模块改写为端口电压、换流链电流和电容历史电压之间的代数关系，实现模块独立计算。

**数学表达**：对于第 $j$ 个子模块：
- 子模块输出电压：$u_{\text{sm},j}$
- 电容电压：$u_{c,j}$
- 历史等效电压：$u_{\text{ceq},j}$
- 换流链电流：$i_{\text{ab}}$
- 关断电阻：$R_{\text{off}} = 10^6\ \Omega$（$\eta = 10^{-9}$）

代数关系（每个模块独立计算）：
$$
u_{\text{sm},j} = f(u_{c,j}, u_{\text{ceq},j}, i_{\text{ab}})
$$
计算复杂度从 $O(N^2)$（经典稀疏矩阵求逆）降至 $O(4N)$，其中 $N$ 为模块数。

**特点**：误差 $< 1.2\%$（与精确开关模型对比），仿真时间缩短 $80\%$（约 5 倍加速）。

**适用场景**：大功率链式 STATCOM 离线仿真参数校核。

**失效场景**：电容参数不一致、故障旁路逻辑、器件非理想特性（Zhang 2019）。

### 6. MMC-STATCOM 多级建模框架（Multi-Level MMC-STATCOM Modeling）

**原理**：将 MMC-STATCOM 分为四级建模精度（DM/DEM/AEM/AVM），与储能系统通过统一接口连接。

**四级模型**：

| 层级 | 名称 | 描述 | 适用场景 |
|------|------|------|----------|
| DM | Detailed Model | 保留 IGBT 非线性 $v$-$i$ 特性 | 高精度参考基准 |
| DEM | Detailed Equivalent Model | IGBT 等效为通断两值电阻 | 调制和均压分析 |
| AEM | Arm Equivalent Model | 桥臂所有子模块聚合为单端口 | 实时仿真 |
| AVM | Average Value Model | 开关周期或基频平均 | 系统级 EMT |

**储能接口**：超级电容或电池经双向 DC/DC 接入 MMC DC 总线，通过差异化时间常数实现动态解耦：
$$
\tau_{\text{energy balance}} = 0.05\ \text{s} < \tau_{\text{DC voltage}} = 0.1\ \text{s} < \tau_{\text{ES frequency support}} = 0.3\ \text{s}
$$
储能功率配置范围：额定功率的 40%（部分功率）至 100%（满功率）。

**特点**：AEM 和 AVM 在保持关键动态变量精度的同时实现计算耗时数量级降低。

**适用场景**：带嵌入式储能的 MMC-STATCOM 系统仿真。

**失效场景**：Delta 全桥拓扑限定，不能默认覆盖星形、半桥或其他拓扑（Stepanov 2023）。

## 形式化表达

### TCR 等效电纳（Trigger Angle Control）

触发角 $\alpha \in [\pi/2, \pi]$ 控制 TCR 等效感纳：
$$
B_{\text{TCR}}(\alpha) = \frac{2(\pi - \alpha) - \sin(2\alpha)}{\pi \omega L},\quad \alpha \in \left[\frac{\pi}{2}, \pi\right]
$$
无功功率：
$$
Q_{\text{TCR}} = -V^2 \cdot B_{\text{TCR}}(\alpha) \quad \text{（吸收感性无功）}
$$

### TSC 等效电容（Fixed/Thyristor-Switched Capacitor）

固定电容或 TSC 电纳：
$$
B_{\text{TSC}} = \frac{1}{\omega L_C},\quad Q_{\text{TSC}} = V^2 \cdot B_{\text{TSC}} \quad \text{（发出容性无功）}
$$
注意：低电压时 $Q$ 随 $V^2$ 下降，支撑能力降低。

### STATCOM 电流注入模型（VSC-Based Shunt Compensation）

电压源换流器以受控电流注入 $I_q^*$ 实现无功支撑：
$$
I_q = I_q^* \cdot \frac{V_{\text{target}}}{V_{\text{bus}}}
$$
直流电压动态：
$$
C_{\text{dc}} \frac{dV_{\text{dc}}}{dt} = \frac{P_{\text{converter}}}{V_{\text{dc}}}
$$
调制比 $m \in [0, 1]$ 控制输出电压幅值：
$$
V_{\text{ac}} = m \cdot \frac{V_{\text{dc}}}{2}
$$

### 动态相量 TCR 模型（Single Phase, Fundamental）

基波 $(k=1)$ TCR 电压-电流关系（复数形式）：
$$
\underline{V}_1 = j\omega_0 L \cdot \underline{I}_1 + R\cdot \underline{I}_1 + j\frac{2}{\pi}(1-\cos\sigma)\underline{V}_{\text{ac}}
$$
开关函数基波分量（$k=1$）：
$$
S_1 = \frac{2}{\pi}\left(1 - e^{-j\sigma}\right) - j\frac{\sin\sigma}{\pi}
$$
诺顿等值电流源（$\sigma = \pi - 2\alpha$）：
$$
I_{\text{eq},1} = I_1 \cdot e^{j\phi_1},\quad Y_{\text{eq},1} = \frac{I_{\text{eq},1}}{V_{\text{bus},1}}
$$

## 关键技术挑战

### 挑战 1：谐波与开关暂态的精确建模
TCR 产生 5、7、11、13 次特征谐波，滤波器设计需要详细的开关动作波形。详细开关模型的计算代价高，平均值模型无法描述谐波特性。动态相量模型通常截断至高次（如 5 次），对不平衡故障场景的误差边界尚未系统评估。

### 挑战 2：多速率仿真与接口稳定性
SVC/STATCOM 与外部电网的混合仿真存在时间尺度差异：TCR 控制环路毫秒级、线路电磁暂态微秒级、系统机电动态秒级。接口处的相位不连续和直流偏移是主要稳定性问题（E Zhijun 2009）。诺顿等值参数需要在每个接口步长刷新。

### 挑战 3：弱电网条件下的控制交互
VSC/STATCOM 在弱电网或故障期间可能出现 PLL 失锁、电流限幅饱和、直流过压、宽频振荡。平均值模型和等效模型在弱电网条件下的精度显著下降，需要详细开关模型或考虑 PLL 动态的阻抗模型。

### 挑战 4：链式换流器的实时/HIL 仿真
链式 STATCOM（如 120 个 H 桥模块）的详细模型在实时平台上计算量巨大。快速等效模型（Zhang 2019）的误差在 $1.2\%$ 以内，但实时/HIL 适应性尚无充分验证。HIL 接口延迟（I/O 延迟、MMCsim 刷新周期 $32.5521\ \mu\text{s}$）影响控制保真度。

### 挑战 5：储能与无功补偿的多时间尺度耦合
MMC-STATCOM 与储能系统的耦合涉及电化学/电容动态（秒级）和换流器开关动态（微秒级）的多尺度交互。差异化时间常数设计（0.05/0.1/0.3 s 解耦）需要在仿真中精确协调，否则储能功率响应与换流器控制产生冲突。

## 量化性能边界

| 研究 | 建模方法 | 测试系统 | 步长/性能 | 精度/加速比 |
|------|----------|----------|-----------|-------------|
| Zhang 2019 | 链式 STATCOM 快速等效 | 三相级联 H 桥，120 个模块 | 仿真时间缩短 80%（~5×） | 误差 < 1.2%（vs MATLAB/Simulink 精确模型） |
| Le-Huy 2023 | 小步长 EMT（HIL） | Hydro-Québec La Verendrye 735 kV，混合 SVC-VSC | $3\ \mu\text{s}$（小步长）vs $32.5521\ \mu\text{s}$（常规步长） | 波形重合度 > 99%，动态偏差 < 0.5%，稳态误差 < 0.2% |
| Le-Huy 2023 | 常规大步长 EMT（HIL） | 同上 | $32.5521\ \mu\text{s}$（512 点/周波） | 与小步长基线对比，重合度 > 99% |
| E Zhijun 2009 | SVC 动态相量混合仿真 | IEEE 3 机 9 节点，New England 10 机 39 节点 | DP 步长 $0.001\ \text{s}$，TSP 步长 $0.01\text{-}0.02\ \text{s}$（提升 200-400×） | 与详细 EMTP 对比有"very good accuracy"（原文未给具体数值） |
| Stepanov 2023 | MMC-STATCOM 四级建模（DM/DEM/AEM/AVM） | Delta 连接全桥 MMC-STATCOM + 嵌入式储能 | AEM/AVM 计算耗时数量级降低 | 原文未报告可核验的加速比或误差百分比 |
| Kosterev 2004 | 并联 VSC 多尺度规划模型 | 18 脉波 GTO 换流器，12.5 kV/10 MVA | 与 EMTP 仿真对比验证 | 原文未报告可核验的误差或响应时间 |

## 适用边界与选择指南

| 应用场景 | 推荐模型层级 | 步长 | 说明 |
|----------|-------------|------|------|
| 谐波分析、投切暂态、保护动作验证 | 详细开关模型（DM） | $1\text{-}10\ \mu\text{s}$ | 保留全部开关暂态和特征谐波 |
| 控制策略验证、系统级 EMT | 受控电纳/平均值模型（AVM） | $20\text{-}50\ \mu\text{s}$ | 保留控制环路，忽略开关细节 |
| 大规模混合仿真（EMT-TSP 联合） | 动态相量模型（DP） | $0.001\text{-}0.02\ \text{s}$ | 大幅降低计算量，适用于系统级动态 |
| 链式 STATCOM 离线仿真参数校核 | 快速等效模型 | 近似大步长 | 误差 < 1.2%，加速 5× |
| HIL 实时测试 | 常规步长 EMT（HIL 接口） | $32.5521\ \mu\text{s}$ | 经 FAT 验证，波形重合度 > 99% |
| 带储能的 MMC-STATCOM | 多级建模框架（AEM/AVM） | $20\text{-}50\ \mu\text{s}$ | 按精度需求选择层级 |
| 谐波截断误差敏感场景 | 详细开关模型（DM） | $1\text{-}10\ \mu\text{s}$ | DP 模型截断高次谐波后可能误差偏大 |

**边界条件**：
- SVC 的无功能力受母线电压影响，低电压时电流和无功输出会下降
- STATCOM 的电流限幅、直流电压和调制范围限制低电压支撑能力
- 晶闸管装置的触发角、同步信号和滤波器影响谐波与次同步频段
- VSC/STATCOM 在弱电网或故障期间可能出现 PLL 失锁和限流饱和

## 相关方法 / 相关模型 / 相关主题

- [[facts]] — 柔性交流输电系统主题入口
- [[svc-model]] — 晶闸管并联无功补偿器（TCR/TSC）模型
- [[statcom-model]] — 基于 VSC 的 STATCOM 模型
- [[tcsc-model]] — 串联补偿设备（TCSC）模型
- [[vsc-model]] — VSC 的共同主电路/控制基础
- [[thyristor-control]] — SVC/TCSC 触发角控制
- [[average-value-model]] — 平均值模型的通用框架
- [[dynamic-phasor]] — 动态相量法的理论框架
- [[hil-simulation]] — 硬件在环仿真验证
- [[real-time-simulation]] — 实时仿真入口

## 来源论文

- [[大功率链式statcom电磁暂态快速等效建模和误差评估]] — 链式 STATCOM 快速等效建模，误差 < 1.2%、仿真时间缩短 80%、复杂度 $O(N^2) \to O(4N)$。验证限于 MATLAB/Simulink 离线仿真（张扬 2019）
- [[hybrid-svc-vsc-modeling-approaches-for-hardware-in-the-loop-simulation]] — 混合 SVC-VSC HIL 建模：$3\ \mu\text{s}$ vs $32.5521\ \mu\text{s}$ 步长对比、波形重合度 > 99%、动态偏差 < 0.5%、稳态误差 < 0.2%。结论限于 La Verendrye 项目（Le-Huy 2023）
- [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model]] — SVC 动态相量混合仿真：步长提升 200-400 倍、基波 + 5 次谐波保留。原文未报告可核验的 CPU 时间或误差范数（E Zhijun 2009）
- [[modeling-of-mmc-based-statcom-with-embedded-energy-storage-for-the-simulation-of]] — MMC-STATCOM 四级 EMT 建模框架和时间常数解耦（0.05/0.1/0.3 s）。原文报告计算耗时数量级降低但未给出可核验加速比（Stepanov 2023）
- [[combined-transient-and-dynamic-analysis-of-hvdc-and-facts-systems]] — HVDC/FACTS 暂态-动态联合仿真框架：诺顿/戴维南频率相关等值接口。原文未单独报告误差（Reeve 1998/Sultan 1998）
- [[compensation-method-for-parallel-real-time-emt-studies]] — 补偿法并行 EMT 实时仿真：无自然延迟场景的网络撕裂接口。加速比 3.30-12.8×（Bruned 2021）