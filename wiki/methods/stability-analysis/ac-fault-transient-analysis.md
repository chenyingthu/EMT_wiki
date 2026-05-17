---
title: "交流故障暂态分析 (AC Fault Transient Analysis)"
type: method
tags: [ac-fault, transient, lcc, commutation, hvdc, recovery, fault-injection, commutation-failure]
created: "2026-05-02"
updated: "2026-05-17"
---

# 交流故障暂态分析 (AC Fault Transient Analysis)

## 定义与边界

交流故障暂态分析（AC Fault Transient Analysis）研究交流侧短路、接地、电压暂降、断路器动作和恢复过程如何改变电压、电流、控制状态和保护输入量。故障类型包括单相接地、两相短路、两相接地短路和三相短路；故障阻抗从零阻抗（金属性短路）到高阻故障不等。

该方法不等同于一个固定故障电流公式，也不提供工程定值。故障电流、关断角裕度、恢复时间和换相失败判断必须绑定网络拓扑、故障阻抗、控制器、保护动作、仿真步长和证据来源。若只需要经典短路量和序分量关系，应先参照 [[fault-analysis]] 和 [[unbalanced-fault-analysis]]。

在EMT研究中，交流故障暂态分析的核心是把故障事件、设备动态、控制保护闭环和测量链路放在同一时间轴上解释，而非把相量短路计算直接搬进时域。

## EMT 中的作用

在 EMT 研究中，交流故障暂态分析通常用于回答以下问题：

- 故障投入和切除瞬间，交流电压波形、衰减直流分量、谐波和不平衡分量如何进入设备模型
- LCC 逆变侧换相电压、换相重叠角和 [[extinction-angle-calculation]] 如何随电压跌落和直流电流变化
- 保护、闭锁、低压限流（VDCOL）、无功支撑和断路器动作如何改变后续网络状态
- 故障清除后，交流电压、直流电压、功率和控制器积分状态是否能按给定策略恢复

典型 EMT 分析场景包括：
- **换相失败筛查**：评估不对称故障导致 LCC 逆变侧关断角 γ 跌至临界值以下的概率
- **直流故障电流评估**：交流侧不对称故障通过换流变压器耦合至直流侧，产生非特征谐波
- **保护整定校核**：故障期间保护测量链路（CT/CVT 暂态、采样滤波）精度对保护动作的影响
- **设备应力分析**：阀电流峰值、子模块电容放电电流、母线电压应力

## 故障注入建模

### 相域 EMT 故障接入模型

相域 EMT 中，固定阻抗故障通过新增导纳支路接入网络方程。故障点相电压向量 $\mathbf{v}_f$ 与注入故障支路电流 $\mathbf{i}_f$ 的关系为：

$$
\mathbf{i}_f(t) = \mathbf{Y}_f(t) \mathbf{v}_f(t)
$$

其中 $\mathbf{Y}_f(t)$ 为故障阻抗的等效导纳矩阵，在故障投入、清除或动态电弧状态改变时更新。三相金属性短路（$R_f = 0$）时，$\mathbf{Y}_f$ 为对应故障节点与参考点之间的极大值导纳。

动态电弧故障模型（如 Mayr 或 Cassie 电弧模型）需在每个仿真步迭代更新 $\mathbf{Y}_f$，以反映电弧电阻随时间的变化。

### 序网故障等效

对称分量法将三相不平衡故障分解为正序、负序和零序网络。故障边界条件（以单相接地为例）：

$$
\dot{V}_a = 0,\quad \dot{V}_b = \dot{V}_c = 0 \quad \Rightarrow \quad \dot{V}_1 = \dot{V}_2 = \dot{V}_0 = \frac{\dot{V}_a^{(pre)}}{3}
$$

其中 $\dot{V}_a^{(pre)}$ 为故障前故障相母线电压。复合序网由正序网络、负序网络（无注入）、零序网络（接地方式决定）和故障点端口阻抗 $Z_f$ 串联构成。

## 换相失败机理与判据

### 正常换相工况

LCC-HVDC 逆变侧换相过程在两相电压驱动下完成。设换相电感为 $L_\gamma$、直流电流为 $I_d$、换流变压器变比为 $k_\gamma$、交流相电压有效值为 $E$、触发角为 $\alpha$。正常换相结束时关断角 $\gamma$ 满足 [[extinction-angle-calculation]]：

$$
\cos\gamma = \frac{2\omega L_\gamma I_d}{k_\gamma E} - \cos\alpha \tag{1}
$$

触发角 $\alpha$ 正常运行时约 $145^\circ$，关断角 $\gamma$ 正常运行时约 $17^\circ$。换相过程持续时间约 $1.0\,\text{ms}$（对应 $17^\circ$ 电角度）；12 脉动换流器换相间隔约 $1.7\,\text{ms}$。

最小关断角安全阈值 $\gamma_\text{min}$ 由反向电压-时间面积 $A_\text{min}$ 决定：

$$
\gamma_\text{min} = \arccos\left(1 - \frac{A_\text{min}}{2k_\gamma E}\right) \tag{2}
$$

安全裕度通常设定为 $7^\circ \sim 9^\circ$。当实际关断角 $\gamma < \gamma_\text{min}$ 时，阀无法在反向电压下恢复阻断能力，发生换相失败。

### 不对称故障下的换相失败快速判据

不对称故障除降低换相电压幅值外，还通过负序电压分量导致换相电压过零点偏移。设相位偏移角为 $\theta$，故障后换相电压有效值为 $E_f$。Zhang 等（2023）从换相微分方程出发，推导得到计及负序相位偏移的通用换相失败判别方程：

$$
\cos\gamma_f = \frac{2 I_d \omega L_\gamma}{k_\gamma E_f} - \cos(\alpha + \theta) \tag{3}
$$

当 $\cos\gamma_f > 1$（或 $\gamma_f < 0$）时，等效为换相电流无法过零，直接判定为换相失败。

**关键量化**：仅含 3% 负序电压分量即可使关断角产生约 $1.7^\circ$ 的偏移，显著压缩关断裕度。

### 参数化平均值模型的换相失败检测

Hong 等（2022）将参数化平均值模型（PAVM）从整流器推广至逆变器，引入自动换相失败检测算法。临界电压跌落阈值函数的表达式随故障施加时刻不同而变化。

**导通区间发生电压跌落时的临界跌落百分比阈值**：

$$
g_\text{crt} = 1 - \frac{I_d'\cos\alpha + \cos\gamma}{I_d\cos\alpha + \cos\gamma_\text{crt}} \tag{4}
$$

**换相区间发生电压跌落时的临界跌落百分比阈值**：

$$
g_\text{crt} = \frac{(I_d - I_d')\cos\alpha - I_d'\cos\gamma + I_d\cos\gamma_\text{crt}}{I_d\cos(\alpha+\tau) + I_d\cos\gamma_\text{crt}} \tag{5}
$$

其中 $\tau$ 为换相开始至跌落施加的时间间隔。自动换相失败检测判据为：

$$
F = \begin{cases} 0 & g < g_\text{crt}^k(\cdot) \\ k & g \ge g_\text{crt}^k(\cdot) \end{cases} \tag{6}
$$

输出故障开关索引 $k$。波形重构误差 $< 1\%$，与详细开关模型高度一致。

### 直流电压跌落对换相裕度的影响

故障期间直流电压 $U_{dc}$ 随换相过程畸变而跌落。设换相电抗压降为 $\Delta U_\gamma$、直流电流变化为 $\Delta I_d$：

$$
U_{dc} = N\left( \frac{\sqrt{6}}{\pi}E\cos\alpha - \frac{3}{\pi}\omega L_\gamma I_d \right) \tag{7}
$$

故障清除后，若直流电压恢复过快（overshoot），可能引起换相失败恢复过程中的二次换相失败。此时需评估换流器控制器的恢复斜率限制。

## 故障清除与恢复过程

### 恢复阶段控制链路

故障清除后，功率恢复受以下因素影响：
- **无功支撑**：交流滤波器和无功补偿设备（SVC/STATCOM）在电压恢复过程中提供无功功率
- **控制器积分状态**：故障期间触发角限幅值可能使 PI 控制器进入饱和；恢复需要正确的去积分（anti-windup）策略
- **VDCOL（低压限流）**：故障期间直流电流被限流环限制；VDCOL 解除阈值影响恢复速度
- **重合闸逻辑**：对于架空线线路，单相重合闸动作需在弧光熄灭后满足去游离时间（约 $0.3\text{-}0.5\,\text{s}$）

恢复判据来源应标注是设备资料、论文算例、标准还是本地仿真设置；若无来源，不应给出固定的恢复时间等级。

### 连续换相失败

多馈入 LCC-HVDC 系统中，一回直流换相失败可能通过耦合电抗影响邻站换相电压，造成多站并发换相失败。多馈入交互因子（MIIF）描述邻站电压对本站的影响：

$$
\text{MIIF}_{ij} = \frac{\Delta U_i / U_i}{\Delta I_j / I_j} \bigg|_{\Delta I_k=0, k\neq j} \tag{8}
$$

其中 $\Delta U_i$ 为换流站 $i$ 母线电压变化，$\Delta I_j$ 为换流站 $j$ 直流电流变化。当 MIIF 较大时，故障站的换相失败更容易引发邻站并发换相失败。

## EMT 建模方法分类

| 分支 | 关注点 | EMT 建模特点 | 适用边界 |
|------|--------|--------------|----------|
| 相量/序网故障分析 | 故障电流、序分量、电压跌落 | 适合准稳态解释，不描述开关和控制细节 | 工频分析、系统强度评估 |
| 相域 EMT 故障分析 | 瞬时电压电流、衰减直流、谐波、控制保护闭环 | 依赖步长、模型频带和控制实现 | 设备应力、保护校核、谐波分析 |
| LCC 换相暂态分析 | 关断角、换相电压、换相失败和恢复 | 只适用于线换相换流器 | 换相失败筛查、HVDC 控制保护设计 |
| 混合仿真筛查 | 大系统故障扫描和局部详细模型 | 接口误差和模型切换需要单独说明 | 大规模交直流系统批量故障计算 |
| 平均值模型分析 | 系统级多工况筛选 | 不替代阀级应力和保护细节验证 | 规划阶段多场景快速筛选 |

## 形式化表达

### 故障阻抗模型

**时变阻抗接地故障**（Mayr 电弧模型）：

$$
\frac{dR_\text{arc}}{dt} = \frac{1}{T_\text{arc}}\left(\frac{|i_\text{arc}|}{g_\text{arc}} - R_\text{arc}\right) \tag{9}
$$

其中 $T_\text{arc}$ 为电弧时间常数，$g_\text{arc}$ 为稳态电导。

### 序分量提取

**滑动平均滤波提取基波**：

$$
\bar{x}(t) = \frac{1}{T}\int_{t-T}^{t}x(\tau)d\tau \tag{10}
$$

窗口 $T = 1/f_e$（基波周期），用于从畸变波形中提取 dq 轴直流分量。

### 多馈入交互因子

**MIIF 定义**（见式 (8)），用于量化多馈入系统中换流站间的电压耦合强度。

## 关键技术挑战

### 挑战一：不平衡故障的负序相位效应

不对称故障下的换相失败判据不能只看正序电压幅值。负序电压引入的换相电压过零点偏移可能导致即使正序电压幅值跌落不严重也发生换相失败。定量边界：3% 负序电压约产生 $1.7^\circ$ 关断角偏移。

**来源**：[fast-detection-method-of-commutation-failure-based-on-multi-infeed-interaction-f]

### 挑战二：换相失败的实时检测

传统准稳态模型在不对称故障下因忽略负序相位偏移而判别失准。Zhang 等（2023）提出在现有 HVDC 准稳态模型中增加负序修正接口；Hong 等（2022）提出基于 $g_\text{crt}$ 阈值函数的自动故障开关检测，实现 PAVM 中的换相失败判定。

### 挑战三：高阻故障定位精度

MMC-HVDC 系统中，高阻故障（可达 $1005\,\Omega$）导致行波衰减严重，波头难以捕捉。Zhang 等（2024）提出基于 2.5 ms 单端电压暂态特征的 RNN 回归方法，在 $1005\,\Omega$ 过渡电阻下定位误差 $< 1.2\%$。

### 挑战四：平均值模型的换相失败表达能力

传统 LCC 平均值模型无法描述换相失败瞬态。Hong 等（2022）将 PAVM 从整流器推广至逆变器，嵌入自动故障配置识别，实现换相失败波形重构（误差 $< 1\%$），计算效率提升数个数量级。

### 挑战五：测量互感器暂态对保护的影响

故障期间 CT 饱和和 CVT 暂态响应可能使保护测量量产生误差，影响换相失败检测和保护动作的时序。EMT 分析需把测量链路（CT/CVT 模型、采样滤波、通信延迟）纳入证据链。

## 量化性能边界

| 指标 | 数值 | 来源 |
|------|------|------|
| 正常运行时触发角 $\alpha$ | $\approx 145^\circ$ | Zhang 等 2023 |
| 正常运行时关断角 $\gamma$ | $\approx 17^\circ$ | Zhang 等 2023 |
| 换相过程持续时间 | $\approx 1.0\,\text{ms}$（$17^\circ$ 电角度） | Zhang 等 2023 |
| 12 脉动换流器换相间隔 | $\approx 1.7\,\text{ms}$ | Zhang 等 2023 |
| 最小关断角安全裕度 $\gamma_\text{min}$ | $7^\circ \sim 9^\circ$ | Zhang 等 2023 |
| 3% 负序电压导致的关断角偏移 | $\approx 1.7^\circ$ | Zhang 等 2023 |
| PAVM 波形重构误差 | $< 1\%$（vs 详细开关模型） | Hong 等 2022 |
| PAVM 换相失败检测判据 | $g < g_\text{crt}$：正常；$g \ge g_\text{crt}$：换相失败 | Hong 等 2022 |
| MMC 故障定位数据窗 | $2.5\,\text{ms}$ | Zhang 等 2024 |
| MMC 高阻故障定位误差 | $< 1.2\%$（$R_f \le 1005\,\Omega$） | Zhang 等 2024 |
| MMC 故障定位抗噪水平 | $40\,\text{dB}$ 白噪声下误差 $< 1.5\%$ | Zhang 等 2024 |

## 适用边界与选择指南

**固定阻抗故障的适用范围**：适合金属性短路和已知接地电阻场景；不适用于电弧、树障、接地网和断续接触过程。

**平均值模型的适用条件**：PAVM 适用于系统级多场景筛选（正常工况 + 换相失败检测）；不替代阀级应力分析和保护闭锁细节验证。

**不对称故障分析的关键**：负序电压的相位偏移效应不可忽略；3% 负序电压即可导致 $1.7^\circ$ 关断角偏移，在 $7^\circ \sim 9^\circ$ 安全裕度边界附近可能触发换相失败。

**HVDC 故障定位的选择**：MMC-HVDC 场景优先考虑基于短窗暂态特征的方法（如 RNN 回归），高阻故障下仍保持 $< 1.2\%$ 误差；LCC-HVDC 场景优先考虑基于临界电压跌落阈值的 PAVM 检测方法。

## 相关页面

- [[fault-analysis]] — 故障分析一般框架，包括输入输出和 EMT/序网边界
- [[unbalanced-fault-analysis]] — 不平衡故障的序网分析基础
- [[concurrent-commutation-failure]] — 多馈入系统中换相失败的传播机理
- [[extinction-angle-calculation]] — LCC 关断角的符号体系和计算边界
- [[dc-protection]] — 直流侧保护原理与断路器动作逻辑
- [[thyristor-control]] — 晶闸管触发控制与 VDCOL 限流策略
- [[average-value-model]] — LCC 平均值等效模型的 EMT 建模范式
- [[transient-stability-analysis]] — 故障清除后的系统机电暂态稳定性

## 来源论文

- Hong 等 (2022). Average-Value Modeling of Line-Commutated Inverter Systems With Commutation Failure. IEEE TPWRD, 37(4). [[average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail]]
- Zhang 等 (2023). Fast Detection Method of Commutation Failure in Multi-Infeed DC System Considering the Effect of Unbalanced Fault. 中国电机工程学报. [[fast-detection-method-of-commutation-failure-based-on-multi-infeed-interaction-f]]
- Zhang 等 (2024). An Ultra-Fast MMC-HVDC Fault Location Algorithm Based on Transient Voltage Features and Regression Neural Network. Int J Electr Power Energy Syst. [[an-ultra-fast-mmc-hvdc-fault-location-algorithm-based-on-transient-voltage-featu]]