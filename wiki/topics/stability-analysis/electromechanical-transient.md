---
title: "机电暂态 (Electromechanical Transient)"
type: topic
tags: [electromechanical-transient, rotor-dynamics, swing-equation, stability, transient-stability]
created: "2026-05-02"
---

# 机电暂态 (Electromechanical Transient)


```mermaid
graph TD
    subgraph Ncmp[机电暂态 (Electromechanical Tran…]
        N0[[[electromagnetic-transient]…]
        N1[**机电暂态**: 0.1s - 10s]
        N2[`long-term-dynamics`: 10s - 分钟]
    end
```


## 核心原理详解

### 技术概述
机电暂态是电力系统电磁暂态仿真领域的重要技术，对提高仿真精度和效率具有重要意义。

### 理论基础
该技术建立在严格的电磁场理论和电路分析基础之上，通过数学建模描述系统的动态行为。

### 核心机制
- **物理建模**：基于物理定律建立准确的数学模型
- **数值求解**：采用高效的数值算法求解系统方程
- **参数分析**：研究关键参数对系统性能的影响

### 技术优势
- 提高仿真精度和计算效率
- 支持复杂系统的详细分析
- 为工程设计和优化提供理论支撑

## 概述

机电暂态是指电力系统中发电机转子机械运动与电磁过程相互耦合的动态过程，时间尺度通常在0.1秒至数十秒范围。主要研究同步发电机在扰动后的功角稳定性，是电力系统安全稳定分析的核心内容。

机电暂态过程涉及机械能、电磁能和动能之间的复杂转换，是电力系统在大扰动后能否保持稳定运行的关键。深入理解机电暂态特性对于电力系统的规划设计、运行控制和安全防御具有重要工程意义。

## 物理基础

### 转子动力学基础

同步发电机的转子运动遵循经典力学中的刚体转动定律。转子的动力学行为由作用在转子轴上的净转矩决定：

$$J\frac{\mathrm{d}omega_m}{\mathrm{d}t} = T_a = T_m - T_e$$

其中：
- $J$: 转子的转动惯量（kg·m²）
- $\omega_m$: 转子机械角速度（rad/s）
- $T_m$: 原动机输入的机械转矩（N·m）
- $T_e$: 发电机输出的电磁转矩（N·m）
- $T_a$: 加速转矩（N·m）

### 摇摆方程的详细推导

摇摆方程（Swing Equation）是描述同步发电机转子运动的核心方程。将其转换为标幺值形式：

首先定义惯性时间常数 $H$：

$$H = \frac{W_{kinetic}}{S_{rated}} = \frac{\frac{1}{2}J\omega_{m0}^2}{S_{rated}}$$

其中：
- $H$: 惯性时间常数（秒），表示发电机在额定转速下存储的动能与额定容量的比值
- $\omega_{m0}$: 同步机械角速度（rad/s）
- $S_{rated}$: 发电机额定容量（VA）

利用关系式 $\omega = \frac{p}{2}\omega_m$（$p$为极对数），将机械角速度转换为电气角速度：

$$\frac{2H}{\omega_0}\frac{d^2\delta}{dt^2} = P_m - P_e - D\frac{\mathrm{d}delta}{\mathrm{d}t}$$

其中：
- $M = \frac{2H}{\omega_0}$: 惯性常数（s²/rad）
- $\omega_0 = 2\pi f_0$: 同步电气角速度（rad/s）
- $\delta$: 转子功角（rad），表示转子位置与同步旋转参考轴的夹角
- $P_m$: 机械功率（标幺值）
- $P_e$: 电磁功率（标幺值）
- $D$: 阻尼系数（标幺值·s/rad）

### 状态空间形式

摇摆方程可表示为两个一阶微分方程组成的系统：

$$\frac{\mathrm{d}delta}{\mathrm{d}t} = \omega - \omega_0$$

$$\frac{2H}{\omega_0}\frac{\mathrm{d}omega}{\mathrm{d}t} = P_m - P_e - D(\omega - \omega_0)$$

这种形式便于数值积分求解，也是[[state-space-method]]分析的基础。

## 电磁功率特性

### 功角特性曲线

对于简化的发电机模型（经典模型），电磁功率与功角的关系为：

$$P_e = \frac{EV}{X_{eq}}\sin\delta$$

其中：
- $E$: 发电机内电势（标幺值）
- $V$: 无穷大母线电压（标幺值）
- $X_{eq}$: 发电机与无穷大母线间的等值电抗（标幺值）
- $\delta$: 功角（rad或°）

电磁功率最大值（功率极限）为：

$$P_{max} = \frac{EV}{X_{eq}}$$

发生在功角 $\delta = 90°$ 时。

### 稳定平衡点与不稳定平衡点

根据摇摆方程，平衡状态满足 $P_m = P_e$。在功角特性曲线上存在两个平衡点：

**稳定平衡点（SEP）**：
- 位置：$\delta_s < 90°$，通常称为正常功角
- 特性：小扰动后系统能够回到该平衡点
- 条件：$\frac{dP_e}{d\delta}\bigg|_{\delta_s} > 0$

**不稳定平衡点（UEP）**：
- 位置：$\delta_u > 90°$，通常位于90°至180°之间
- 特性：任何小扰动都会使系统偏离该点
- 条件：$\frac{dP_e}{d\delta}\bigg|_{\delta_u} < 0$

**临界功角**：$\delta_{cr} = 180° - \delta_s$

### 功率-功角关系的扩展模型

考虑励磁系统调节作用时，采用暂态电势 $E'_q$ 表示：

$$P_e = \frac{E'_q V}{X'_{d\Sigma}}\sin\delta + \frac{V^2}{2}\frac{X'_{d\Sigma} - X_{q\Sigma}}{X'_{d\Sigma}X_{q\Sigma}}\sin(2\delta)$$

其中：
- $E'_q$: q轴暂态电势（由励磁绕组磁链决定）
- $X'_{d\Sigma}$: d轴暂态等值电抗
- $X_{q\Sigma}$: q轴同步等值电抗

该模型考虑了凸极效应，功率特性中出现两倍功角项。

## 时间尺度分析

### 电力系统动态的时间层次

电力系统的动态过程按时间尺度可分为三个层次：

| 暂态类型 | 时间尺度 | 研究对象 | 主要现象 |
|----------|----------|----------|----------|
| [[electromagnetic-transient]] | μs - ms (10⁻⁶~10⁻³s) | 电压、电流快速变化 | 行波传播、过电压、短路电流 |
| **机电暂态** | 0.1s - 10s | 转子功角摇摆 | 功角稳定、振荡、失步 |
| `long-term-dynamics` | 10s - 分钟 | 慢速控制过程 | 频率调节、电压调节、负荷恢复 |

### 电磁暂态与机电暂态的耦合

电磁暂态与机电暂态之间存在紧密耦合关系：

**电磁暂态对机电暂态的影响**：
- 短路故障期间电磁功率突降，转子加速
- 故障切除后电磁功率恢复，决定转子减速能力
- 励磁调节（时间常数0.1-1s）影响暂态电势变化

**机电暂态对电磁暂态的简化**：
- 在机电暂态仿真中，网络方程采用准稳态模型
- 忽略高频电磁振荡，假设电压电流为工频正弦
- [[phasor-model]]替代瞬时波形

### 混合仿真接口

[[hybrid-simulation]]技术将电磁暂态（EMT）与机电暂态（TS）模型结合：

**接口原理**：
- 机电暂态侧提供等值阻抗和电压源
- 电磁暂态侧返回瞬时功率或等值电流
- 接口位置通常选在边界母线

**接口技术**：
- [[thevenin-equivalent]]: 电压源串联阻抗
- [[norton-equivalent]]: 电流源并联导纳
- 多端口等值: 考虑机群之间的电气联系

## 稳定性分析

### 暂态稳定（Transient Stability）

[[transient-stability]]研究系统在遭受大扰动后保持同步运行的能力：

**扰动类型**：
- 短路故障：三相短路、两相短路、单相接地
- 切机切负荷：发电机组或负荷突然退出
- 线路跳闸：输电线路断开或重合闸失败

**首摆稳定**：
- 定义：系统在第一次摇摆中恢复同步
- 判据：转子功角在达到最大值后开始减小
- 关键指标：首摆最大功角 $\delta_{max}$

**临界切除时间（CCT）**：

$$CCT = t_{critical}$$

当故障切除时间小于CCT时，系统暂态稳定；反之则失步。CCT可通过时域仿真或[[equal-area-criterion]]估算。

### 小信号稳定（Small-Signal Stability）

[[small-signal-stability]]分析系统在平衡点邻域内的动态特性：

**线性化方法**：

在平衡点 $(\delta_0, \omega_0)$ 附近线性化摇摆方程：

$$\Delta\dot{\delta} = \Delta\omega$$
$$\frac{2H}{\omega_0}\Delta\dot{\omega} = -\frac{\partial P_e}{\partial\delta}\bigg|_{\delta_0}\Delta\delta - D\Delta\omega$$

**同步功率系数**：

$$K_s = \frac{\partial P_e}{\partial\delta}\bigg|_{\delta_0} = \frac{EV}{X_{eq}}\cos\delta_0$$

**机电振荡模式**：

线性化系统的特征方程为：

$$s^2 + \frac{D\omega_0}{2H}s + \frac{K_s\omega_0}{2H} = 0$$

振荡频率和阻尼比：

$$f_{osc} = \frac{1}{2\pi}\sqrt{\frac{K_s\omega_0}{2H} - \left(\frac{D\omega_0}{4H}\right)^2}$$

$$\zeta = \frac{D}{2}\sqrt{\frac{\omega_0}{2HK_s}}$$

### 稳定判据

**等面积法则（Equal Area Criterion）**：

[[equal-area-criterion]]是判断单机无穷大系统暂态稳定性的直接方法。

稳定判据：加速面积等于减速面积

$$A_{acc} = \int_{\delta_0}^{\delta_c}(P_m - P_{e,fault})d\delta$$

$$A_{dec} = \int_{\delta_c}^{\delta_{max}}(P_{e,post} - P_m)d\delta$$

稳定条件：$A_{acc} \leq A_{dec,max}$

**能量函数法**：

系统总能量：

$$V = \frac{1}{2}M\omega^2 + \int_{\delta_0}^{\delta}(P_e - P_m)d\delta$$

其中：
- 动能：$V_{ke} = \frac{1}{2}M\omega^2$
- 势能：$V_{pe} = \int_{\delta_0}^{\delta}(P_e - P_m)d\delta$

稳定边界由不稳定平衡点的势能决定。

## 影响因素

### 系统参数

**惯性时间常数（H）**：
- 物理意义：反映转子储存的动能大小
- 影响：H越大，转速变化越慢，暂态稳定性越好
- 典型值：火电机组3-6s，水电机组2-4s，风电机组较小

**电气距离**：
- 定义：发电机与系统间的等值电抗
- 影响：电气距离越短（$X_{eq}$越小），功率极限越高
- 措施：采用串联补偿、增加线路回数

**传输功率水平**：
- 初始功角：$\delta_0 = \arcsin(\frac{P_0}{P_{max}})$
- 影响：重载时初始功角大，稳定裕度小
- 运行建议：留足稳定储备（通常20-30%）

### 故障特性

**故障类型**：
- 三相短路：$P_{e,fault} \approx 0$，加速面积最大
- 两相短路：$P_{e,fault} > 0$，严重程度次之
- 单相接地：$P_{e,fault}$最大，影响最小

**故障位置**：
- 电气距离近：故障对机组影响大
- 电气距离远：等值阻抗大，影响小
- 母线故障：最严重，可能导致系统解列

**故障持续时间**：
- 与保护动作时间、断路器跳闸时间相关
- 快速保护（<100ms）显著提高稳定性
- 重合闸策略影响系统恢复

### 控制作用

**励磁系统**：
- 强励功能：故障时提高内电势E
- 暂态增益：快速响应提高暂态稳定
- 时间常数：$T'_{do}$（1-10s）影响E'_q恢复速度

**电力系统稳定器（PSS）**：
- 功能：提供附加阻尼，抑制低频振荡
- 输入信号：转速、功率、频率
- 相位补偿：补偿励磁系统滞后特性

**快速汽门控制**：
- 原理：故障时快速关小汽门，减少机械功率
- 效果：减小加速面积
- 实现：快关时间200-500ms

**高压直流（HVDC）附加控制**：
- 功率调制：调节HVDC传输功率
- 紧急功率支援：故障时快速增加/减少功率
- 异步互联优势：避免交流系统间的暂态稳定问题

## 数学模型详解

### 发电机模型

**经典模型（Classical Model）**：

假设：
- 暂态电势$E'$恒定
- 忽略阻尼绕组
- 机械功率$P_m$恒定

方程：

$$P_e = \frac{E'V}{X'_{d\Sigma}}\sin\delta$$

适用于首摆稳定分析，计算简单，物理概念清晰。

**两轴模型（Two-Axis Model）**：

考虑d、q轴暂态过程：

$$T'_{do}\frac{dE'_q}{dt} = E_{fd} - E'_q - (X_d - X'_d)I_d$$
$$T'_{qo}\frac{dE'_d}{dt} = -E'_d + (X_q - X'_q)I_q$$

$$P_e = E'_qI_q + E'_dI_d + (X'_q - X'_d)I_dI_q$$

适用于分析励磁系统对暂态稳定的影响。

**详细模型（Detailed Model）**：

考虑：
- 阻尼绕组（g、D绕组）
- 饱和效应
- 完整的电压方程
- `park-transformation`实现

适用于精确仿真，但计算量大。

### 网络模型

**节点导纳方程**：

$$\mathbf{I} = \mathbf{Y}\mathbf{V}$$

其中：
- $\mathbf{I}$: 节点注入电流向量
- $\mathbf{V}$: 节点电压向量
- $\mathbf{Y}$: [[nodal-admittance-matrix]]

**发电机接口**：

将发电机表示为电流源注入网络：

$$\mathbf{I}_g = f(E'_q, E'_d, \delta, \mathbf{V}_g)$$

**网络简化**：
- 消去非发电机节点（高斯消去法）
- 保留发电机内节点
- 等值阻抗矩阵$\mathbf{Z}_{reduced}$

### 负荷模型

**静态负荷模型**：

ZIP模型（恒阻抗Z、恒电流I、恒功率P）：

$$P = P_0\left[a_1\left(\frac{V}{V_0}\right)^2 + a_2\frac{V}{V_0} + a_3\right]$$

$$Q = Q_0\left[b_1\left(\frac{V}{V_0}\right)^2 + b_2\frac{V}{V_0} + b_3\right]$$

其中$a_1+a_2+a_3 = 1$，$b_1+b_2+b_3 = 1$。

**动态负荷模型**：

考虑感应电动机：

$$T_j\frac{ds}{dt} = T_m - T_e$$

其中$s$为转差率，$T_j$为惯性时间常数。

**综合负荷模型**：

$$S_{load} = S_{ZIP} + S_{motor} + S_{discrete}$$

包含静态负荷、电动机和离散负荷（如电弧炉）。

## 仿真方法

### 时域仿真

[[time-domain-simulation]]是暂态稳定分析的最基本方法：

**数值积分方法**：

- **梯形法（Trapezoidal）**：
  - 精度：二阶
  - 稳定性：A-稳定
  - 步长：通常1-10ms

- **Gear法**：
  - 变步长、变阶数
  - 适合刚性系统
  - 自动误差控制

- **龙格-库塔法**：
  - 显式方法
  - 适合非刚性系统
  - 计算效率高

**仿真流程**：

1. 初始化：潮流计算确定初始状态
2. 故障施加：修改导纳矩阵$Y$
3. 数值积分：求解微分-代数方程组（DAE）
4. 故障清除：恢复原网络或采用故障后网络
5. 稳定性判断：检查功角差是否发散

**DAE求解**：

$$\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \mathbf{y})$$
$$\mathbf{0} = \mathbf{g}(\mathbf{x}, \mathbf{y})$$

交替求解微分方程（发电机动态）和代数方程（网络约束）。

### 直接法

**等面积法则**：

适用条件：单机无穷大系统

$$\int_{\delta_0}^{\delta_{max}}(P_m - P_e)d\delta = 0$$

优点：
- 无需数值积分
- 物理概念清晰
- 快速估算稳定裕度

**扩展等面积准则（EEAC）**：

[[eeac]]将多机系统等值为单机无穷大系统：

1. 机群识别：将发电机分为临界机群和非临界机群
2. 等值参数：
   $$\delta_{OMIB} = \delta_{critical} - \delta_{non-critical}$$
3. 应用等面积法则

**能量函数法**：

构造李雅普诺夫函数：

$$V(\delta, \omega) = V_{ke}(\omega) + V_{pe}(\delta)$$

稳定域由势能函数在不稳定平衡点的值决定：

$$V_{cr} = V_{pe}(\delta_u)$$

稳定裕度：$\eta = \frac{V_{cr} - V_{fault}}{V_{cr}}$

### 混合法

**单机等效法（SIME）**：

基于EEAC思想，但利用时域仿真结果在线计算等值参数：

1. 进行时域仿真获得轨迹
2. 识别机群分离模式
3. 计算等值参数
4. 预测稳定裕度

**复合方法**：

结合时域仿真与直接法优点：
- 时域仿真提供精确轨迹
- 直接法快速评估稳定裕度
- 适用于在线安全评估

## 提高暂态稳定的措施

### 快速保护

**快速切除故障**：
- 目标：故障切除时间<100ms
- 技术：光纤差动保护、行波保护
- 效果：显著减小加速面积

**单相重合闸**：
- 原理：单相故障只跳开故障相，重合成功率高
- 优点：非故障相保持连接，维持功率传输
- 成功率：80-90%（瞬时性故障）

**连锁切机**：
- 策略：切除失步或加速过快的发电机
- 触发条件：功角>阈值或角速度>阈值
- 目的：防止系统崩溃，保证主网稳定

### 电气制动

**电阻制动**：
- 原理：投入并联电阻消耗过剩功率
- 控制：故障时投入，稳定后切除
- 计算：$P_{brake} = \frac{V^2}{R_{brake}}$

**投切并联补偿**：
- 故障时投入：提高电压，增加电磁功率
- 故障后切除：避免过电压
- 设备：STATCOM、SVC、并联电容器

**串联补偿**：
- TCSC（可控串联补偿）：
  - 原理：调节串联电容补偿度
  - 故障时：增加补偿，减小等值电抗
  - 提高功率极限：$P_{max} = \frac{EV}{X_{line}(1-K_{comp})}$

### 网络加强

**增加传输走廊**：
- 新建线路：减小等值阻抗
- 提高电压等级：增加传输容量
- 分区供电：减小送受端距离

**直流输电异步互联**：
- 优势：HVDC不传递功角失步
- 应用：大区电网互联
- 附加控制：功率调制提高交流侧稳定

[[facts]]：

- UPFC：统一潮流控制器
  - 功能：调节电压、相位、阻抗
  - 效果：提高传输能力和稳定性

- SSSC：静止同步串联补偿器
  - 功能：等效可变串联阻抗
  - 应用：潮流控制和振荡阻尼

## 与EMT混合仿真的接口技术

### 接口原理

机电暂态与[[emt-simulation]]的接口是混合仿真的核心技术：

**多速率仿真**：
- EMT侧：微秒级步长
- 机电暂态侧：毫秒级步长
- 接口周期：1-10ms

**数据交换**：
- 机电暂态→EMT：等值阻抗、电压相量
- EMT→机电暂态：功率、电流相量

### 等值方法

**戴维南等值**：

机电暂态侧提供：
$$\mathbf{V}_{th} = \mathbf{V}_{boundary}$$
$$\mathbf{Z}_{th} = \mathbf{Z}_{eq}$$

EMT侧求解瞬时方程。

**诺顿等值**：

$$\mathbf{I}_{nor} = \mathbf{Y}_{eq}\mathbf{V}_{boundary}$$
$$\mathbf{Y}_{nor} = \mathbf{Y}_{eq}$$

**动态等值**：

考虑机电暂态侧发电机动态：
- 保留详细发电机模型
- 网络等值到边界点
- 多端口等值考虑机群交互

### 接口稳定性

**时延问题**：
- 机电暂态→EMT存在计算时延
- 可能导致数值不稳定
- 解决方法：预测-校正算法

**阻抗匹配**：
- 两侧阻抗应连续变化
- 避免接口处反射和振荡
- 阻尼注入技术

### 应用场景

**直流输电研究**：
- 换流器用EMT详细模型
- 交流系统用机电暂态模型
- 研究直流故障对交流系统的冲击

**风电场接入**：
- 风机用详细EMT模型
- 集电系统和电网用机电暂态
- 分析低电压穿越能力

**FACTS设备**：
- FACTS控制器详细建模（EMT）
- 系统级机电暂态仿真
- 协调控制策略验证

## 实际应用案例

### 区域互联系统暂态稳定评估

**系统概况**：
- 某大区电网通过500kV双回线互联
- 总装机容量：80000MW
- 关键断面传输功率：6000MW

**故障场景**：
- 三相短路故障
- 故障位置：送端枢纽变电站
- 故障持续时间：100ms

**分析结果**：
- 临界切除时间：120ms
- 稳定裕度：15%
- 薄弱环节：送端发电机组加速严重

**改进措施**：
- 安装PSS提供附加阻尼
- 快关汽门控制
- 优化保护配置（单相重合闸）

### 风电大规模接入的暂态稳定问题

**问题描述**：
- 风电场容量：3000MW
- 采用双馈感应发电机（DFIG）
- 电网故障时大规模脱网

**分析发现**：
- 低电压穿越能力不足
- 故障期间无功支撑缺失
- 传统同步机惯性减少

**解决方案**：
- 改造风机控制系统
- 配置STATCOM提供无功支撑
- 采用虚拟同步机技术（VSM）

### HVDC异步互联的稳定效益

**工程背景**：
- 传统交流互联：功角稳定约束传输极限
- 改为HVDC异步互联
- 直流功率：5000MW

**效益分析**：
- 消除功角稳定约束
- 两侧电网可独立运行
- 直流功率调制提高交流侧稳定性

**运行经验**：
- 交流故障不传递
- 直流闭锁需紧急控制
- 协调控制策略关键

## 研究前沿与发展趋势

### 高比例电力电子电源接入

**挑战**：
- 传统同步机被电力电子电源替代
- 系统惯性降低
- 阻尼特性改变

**研究方向**：
- 构网型控制（Grid-Forming）
- 虚拟惯量技术
- 暂态电压支撑

### 人工智能在稳定分析中的应用

**应用场景**：
- 快速稳定评估：神经网络预测
- 紧急控制决策：强化学习优化
- 稳定边界识别：机器学习方法

**技术路线**：
- 离线训练：大量仿真样本
- 在线应用：毫秒级响应
- 安全验证：物理约束保证

### 广域测量系统（WAMS）

**技术应用**：
- PMU提供同步相量测量
- 基于实测的稳定性监测
- 预测性控制策略

**功能实现**：
- 实时功角差监测
- 振荡模式在线辨识
- 自适应紧急控制

## 相关主题

- [[transient-stability]] - 暂态稳定性详细分析
- [[small-signal-stability]] - 小信号稳定性与阻尼
- `power-system-stability` - 综合稳定性理论
- [[swing-equation]] - 摇摆方程专题
- [[equal-area-criterion]] - 等面积法则详解
- [[hybrid-simulation]] - EMT与机电暂态混合仿真
- [[emt-simulation]] - 电磁暂态仿真
- [[time-domain-simulation]] - 数值积分方法
- [[state-space-method]] - 状态空间分析
- `rotor-dynamics` - 发电机转子动力学

## 来源论文

参见 [[index]] 获取更多中机电暂态相关文献，包括：
- 暂态稳定直接法研究
- 混合仿真接口技术
- 大规模系统稳定分析
- 新能源接入稳定问题

## 来源论文

| 论文 | 年份 |
|------|------|
| [[modeling-a-mixed-residential-commercial-load-for-simulations-involving-large-dis|Modeling A Mixed Residential-commercial Load  For Simulation]] | 2004 |
| [[modeling-synchronous-voltage-source-converters-in-transmission-system-planning-s|Modeling Synchronous Voltage Source Converters in Transmissi]] | 2004 |
| [[hybrid-transient-stability-simulation-using-dynamic-phasor-based-interface-model-22|Hybrid Transient Stability Simulation Using Dynamic Phasor B]] | 2006 |
| [[hybrid-transient-stability-simulation-using-dynamic-phasor-based-interface-model-22|Hybrid Transient Stability Simulation Using Dynamic Phasor B]] | 2006 |
| [[hybrid-model-transient-stability-simulation-using-dynamic-phasors-based-hvdc-system-model|Hybrid-model transient stability simulation using dynamic ph]] | 2006 |
| [[frequency-adaptive-power-system-modeling-for|Frequency-Adaptive Power System Modeling for]] | 2009 |
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model-22|Hybrid simulation of power systems with SVC dynamic phasor m]] | 2009 |
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model-22|Hybrid simulation of power systems with SVC dynamic phasor m]] | 2009 |
| [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb|Interfacing Techniques for Transient Stability and Electroma]] | 2009 |
| [[electromechanical-transient-modeling-of-modular-multilevel-converter-based-multi|Electromechanical Transient Modeling of Modular Multilevel C]] | 2013 |
| [[electromechanical-transient-modeling-of-modular-multilevel-converter-based-multi|Electromechanical Transient Modeling of Modular Multilevel C]] | 2013 |
| [[comparative-study-on-electromechanical-and-electromagnetic-transient-model-for-g|Comparative study on electromechanical and electromagnetic t]] | 2014 |
| [[a-review-of-efficient-modeling-methods-for-modular-multilevel-converters|A review of efficient modeling methods for modular multileve]] | 2015 |
| [[advanced-hybrid-transient-stability-and-emt-simulation-for-vsc-hvdc-systems|Advanced Hybrid Transient Stability and EMT Simulation for V]] | 2015 |
| [[2728multi-scale-and-frequency-dependent-modeling-of-electric-power-transmission-|Multi-scale and Frequency-dependent Modeling of Electric Pow]] | 2017 |
| [[含vsc-hvdc交直流系统多尺度暂态建模与仿真研究-40|含VSC-HVDC交直流系统多尺度暂态建模与仿真研究]] | 2017 |
| [[half-wavelength-system-transients-stability-simulation-using-dynamic-phasor-mode|输电线路工频动态相量模型在半波长交流输电系统机电暂态仿真中的应用研究]] | 2017 |
| [[development-and-applicability-of-online-passivity-enforced-wide-band-multi-port-|Development and Applicability of Online Passivity Enforced W]] | 2018 |
| [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi-15|Electro-mechanical transient modeling of MMC based multi-ter]] | 2019 |
| [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi-15|Electro-mechanical transient modeling of MMC based multi-ter]] | 2019 |
| [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi-15|Electro-mechanical transient modeling of MMC based multi-ter]] | 2019 |
| [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi|Electro-mechanical transient modeling of MMC based multi-ter]] | 2019 |
| [[electro-mechanical-transient-modeling-of-mmc-based-multi-terminal-hvdc-system-wi|Electro-mechanical transient modeling of MMC based multi-ter]] | 2019 |
| [[hybrid-transient-stability-simulation-using-dynamic-phasor-based-interface-model|Hybrid Transient Stability Simulation Using Dynamic Phasor B]] | 2019 |
| [[multi-scale-induction-machine-model-in-the-phase-domain-with-constant-inner-impe|Multi-scale Induction Machine Model in the Phase Domain with]] | 2019 |
| [[adaptive-heterogeneous-transient-analysis-of-wind-farm-integrated-comprehensive-|Adaptive Heterogeneous Transient Analysis of Wind Farm Integ]] | 2021 |
| [[damping-of-subsynchronous-control-interactions-in-large-scale-pv-installations-t|Damping of Subsynchronous Control Interactions in Large-Scal]] | 2021 |
| [[electromechanical-transient-modelling-and-application-of-modular-multilevel-conv|Electromechanical transient modelling and application of mod]] | 2021 |
| [[electromechanical-transient-modelling-and-application-of-modular-multilevel-conv|Electromechanical transient modelling and application of mod]] | 2021 |
| [[flexible-time-stepping-dynamic-emulation-of-acdc-grid-for-faster-than-scada-appl|Flexible Time-Stepping Dynamic Emulation of AC/DC Grid for F]] | 2021 |
| [[mitigation-of-subsynchronous-interactions-in-hybrid-acdc-grid-with-renewable-ene|Mitigation of Subsynchronous Interactions in Hybrid AC/DC Gr]] | 2021 |
| [[faster-than-real-time-hardware-emulation-of-extensive-contingencies-for-dynamic-|Faster-Than-Real-Time Hardware Emulation of Extensive Contin]] | 2022 |
| [[interfacing-real-time-and-offline-power-system-simulation-tools-using-udp-or-fpg|Interfacing real-time and offline power system simulation to]] | 2022 |
| [[electromechanical-transient-modeling-of-the-low-frequency-ac-system-with-modular|Electromechanical Transient Modeling of the Low-Frequency AC]] | 2023 |
| [[electromechanical-transient-modeling-of-the-low-frequency-ac-system-with-modular|Electromechanical Transient Modeling of the Low-Frequency AC]] | 2023 |
| [[multirate-method-for-dynamic-phasor-simulation-of-large-scale-power-systems|Multirate Method for Dynamic Phasor Simulation of Large-Scal]] | 2026 |
| [[vsc-hvdc-系统的动态相量法建模仿真分析|VSC-HVDC 系统的动态相量法建模仿真分析]] | 2026 |
