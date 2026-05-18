---
title: "机电-电磁暂态混合仿真 (Electromechanical-Electromagnetic Hybrid Simulation)"
type: topic
tags: [hybrid-simulation, electromechanical, electromagnetic, multi-time-scale, interface, co-simulation]
created: "2026-05-02"
updated: "2026-05-18"
---

# 机电-电磁暂态混合仿真 (Electromechanical-Electromagnetic Hybrid Simulation)

## 定义

机电-电磁暂态混合仿真（Electromechanical-Electromagnetic Hybrid Simulation）是电力系统仿真领域将电磁暂态仿真（EMT，关注μs~ms级快速暂态、开关动作、谐波和电力电子设备细节）与机电暂态仿真（TS，关注ms~s级转子摇摆、频率变化和大规模电网稳定）进行协同求解的先进仿真技术。该方法通过时间尺度分离——将需要详细建模的区域（如含HVDC换流器、电力电子装置、单相空调压缩机等快速响应设备的内部网络）放入EMT仿真器，其余大电网系统用相量域机电暂态仿真——在保证关键设备动态细节的同时，使大规模电力系统的仿真成为可能。混合仿真的核心接口问题是：如何在两个带宽、变量形式（瞬时值vs相量/功率）、数值求解方法和时间步长均不同的仿真器之间准确交换边界量。

## EMT中的角色

随着新能源并网、HVDC输电和电力电子化电网的快速普及，电力系统中含大量通过换流器接入的快速响应元件。这些元件在故障期间需要EMT级细节才能正确描述（如换相失败过程、IGBT开关瞬态、单相电机堵转动态），但若将整个大电网全部放入EMT仿真器，计算负担远超现有硬件能力。纯机电暂态仿真则无法刻画这些快速响应设备的详细动态，尤其是单相空调压缩机电机在不对称故障下的堵转传播特性可能导致FIDVR（故障诱发的延迟电压恢复）现象，纯正序TS对此描述不准确。

机电-电磁暂态混合仿真的作用体现在以下几方面：

1. **精度-规模平衡**：兼顾局部细节与大系统覆盖范围，避免在"全EMT计算不可行"与"纯TS精度不足"之间二选一
2. **时间尺度耦合**：捕捉快速电磁暂态与慢速机电动态之间的相互耦合作用（如HVDC控制响应与大电网稳定性交互）
3. **接口灵活性**：支持多种分区方案（按电气距离、按设备类型、按关注区域），接口位置可灵活选择
4. **工程实用性**：可集成现有成熟的商业EMT软件（如PSCAD/EMTDC）和TS软件（如PSSE、InterPSS），避免重复开发

## 时间尺度与分区原则

### 时间尺度分离框架

电力系统动态按时间尺度可分为三个层次，各对应不同的仿真类型：

| 时间尺度 | 范围 | 主要现象 | 仿真类型 | 典型步长 |
|---------|------|---------|---------|---------|
| 电磁暂态 | μs~ms | 开关瞬态、换相过程、谐波、过电压 | EMT | 10~100 μs |
| 机电暂态 | ms~s | 转子摇摆、频率变化、功角稳定 | TS/相量域 | 1~10 ms |
| 中长期动态 | s~min | 负荷调节、AGC、经济调度 | 长时间动态 | 10~100 ms |

机电-电磁混合仿真的本质是**时间尺度解耦**：通过接口将快动态区域与慢动态区域分离，使各自在合适的时间步长下独立求解。

### 分区原则与接口位置选择

混合仿真分区需综合考虑以下因素：

**电气隔离点原则**：接口通常选在变压器两侧（电气上已隔离）、换流站交流侧（控制边界清晰）或关注设备与外部系统的连接点。这些位置的自然阻抗/导纳差较小，接口误差对内部EMT动态影响较小。

**时间常数差异原则**：接口应选在时间常数差异显著的区域边界，如快控设备（换流器控制、STATCOM）与慢速网络（输电线路、传统发电机）之间。

**控制耦合度原则**：强耦合的控制回路（如MMC内部均压控制、HVDC触发控制）通常保留在EMT侧；弱耦合或慢速控制（如潮流优化、发电调度）保留在TS侧。

**分区示意**（四区域模型）：

```
┌──────────────────────────────────────────────────────┐
│            大区系统 (TS/相量域, 大步长)                │
│  ┌────────────┐           ┌────────────┐             │
│  │  同步电机  │           │  输电网络  │             │
│  │  励磁系统  │           │  (等值)    │             │
│  └─────┬──────┘           └─────┬──────┘             │
│        │   (大步长 Δt_TS)        │                    │
│  ┌─────┴──────┐           ┌─────┴──────┐             │
│  │  接口区域  │◄─────────►│  接口区域  │             │
│  └─────┬──────┘           └─────┬──────┘             │
│        │   (小步长 Δt_EMT)        │                    │
│  ┌────────────┐           ┌────────────┐             │
│  │  换流器    │           │  详细线路  │             │
│  │  电力电子  │           │  (EMT级)   │             │
│  │  快速保护  │           │            │             │
│  └────────────┘           └────────────┘             │
│         ▲                       ▲                       │
│    小步长(10-100μs)       小步长(10-100μs)             │
└──────────────────────────────────────────────────────┘
```

## 接口技术

### 接口变量交换机制

机电侧（TS）与电磁侧（EMT）之间的信息交换通过以下通道实现：

**从机电侧输出到电磁侧**：
$$V_{TS}(t) \Rightarrow 	ext{电压源或诺顿等值电路注入} $$
电磁侧收到来自TS侧的等值电压或诺顿电流注入后，将其作为已知边界条件并入EMT网络方程，与EMT内部元件的动态方程联立求解。

**从电磁侧输出到机电侧**：
$$I_{EMT}(t), \; P_{EMT}(t), \; Q_{EMT}(t) \Rightarrow \text{功率/电流注入或等值阻抗} $$
EMT侧将边界节点的瞬时电流或有功/无功功率传递给TS侧，TS侧据此更新等值导纳矩阵或等值电流源。

### 主要接口方法

#### 1. 理想变压器接口（Ideal Transformer Interface）

**原理**：通过理想变压器模型在接口两侧实现功率平衡，利用变压器变比调整电压电流幅值和相角：

$$P_{TS} = P_{EMT}, \quad Q_{TS} = Q_{EMT}$$

**优点**：物理概念清晰，功率守恒严格，实现简单

**缺点**：在接口两侧动态特性差异大时可能产生数值振荡；不适用于三相不平衡条件

**适用场景**：接口两侧网络特性相近、接口位置电气距离短

#### 2. 诺顿/戴维南等值接口（Norton/Thevenin Equivalent Interface）

**诺顿等值**（电磁侧等值为诺顿电路注入机电侧）：
$$I_{eq} = I_{EMT}, \quad Y_{eq} = f(Z_{system})$$

**戴维南等值**（机电侧等值为戴维南电路注入电磁侧）：
$$V_{eq} = V_{TS}, \quad Z_{eq} = f(Y_{system})$$

诺顿等值将电磁侧对机电侧的影响表示为电流源加导纳的并联结构；戴维南等值将机电侧对电磁侧的影响表示为电压源加阻抗的串联结构。两种等值可以根据接口位置的网络特性灵活选择。

**多端口三相Thévenin等值**（Huang & Vittal 2016）：传统接口等值多基于正序网络模型，在不对称故障下需要将边界扩展到三相平衡位置，导致接口区域过大。多端口三相Thévenin等值在正、负、零三序下分别形成网络方程：

- **正序**：保留同步电机的机电动态
- **负序**：按序网络独立求解
- **零序**：按序网络独立求解

三序边界电压、电流和等值参数经相序变换映射为EMT侧可直接连接的三相多端口Thévenin电压源，从而支持接口区域的不对称故障分析而无需假定三相平衡。

#### 3. 频率相关网络等值（FDNE）

$$Z_{eq}(s) = \sum_{i=1}^{N}\frac{R_i}{s-p_i} + D + sE$$

频率相关网络等值通过有理函数拟合将外部网络的频率特性（随频率变化的阻抗特性）在时域中以等值电路形式表示，精度高于仅用基频阻抗的简单等值，适用于宽频带EMT分析场景。

- [[fdne-model]] - 频变网络等值模型详情

#### 4. 动态相量映射等效（DP-ME）

Zhu et al. 2021 提出的DP-ME方法将EMT侧行为表示为TS侧可接受的**注入功率**而非瞬时波形或基频相量。核心机制：

- 在接口处建立动态相量映射模型，输入为EMT侧的瞬时电气量，输出为TS侧所需的有功/无功功率注入
- 避免了传统FFT或最小二乘法从瞬时波形提取基频相量过程中固有的**至少一个基频周期（约20ms）的固定延迟**
- 接口位移（ID）策略将接口从强电气耦合的换流器母线移至EMT子网内部的控制回路或内部等效点，利用控制与滤波惯性削弱分区延迟影响

DP-ME的机制分析：对于含延迟交互的线性电路，接口延迟会导致特征根出现指数时滞项，特征方程可写为 $\lambda = f(\lambda, \tau)$，其中 $\tau$ 为接口延迟。延迟系统的特征根由Lambert W函数精确解析：

$$\lambda' = -\frac{R_1}{L} + \frac{W(z)}{\tau}$$

$W(z)$ 为Lambert W函数，$z = \tau(R_1+R_2)/L \cdot e^{\tau(R_1+R_2)/L}$。该分析表明接口延迟会改变混合仿真的动态响应——特征根实部随延迟增大而向复平面右半平面移动，系统阻尼降低。

#### 5. 移频分析接口（SFA-EMT）

Tarazona et al. 2026 提出的SFA-EMT混合接口在MATE（Multi-Area Thevenin Equivalent）框架下实现：

- **移频构造**：原始带通信号 $u(t)$ 构造成解析信号 $z(t)=u(t)+j\mathcal{H}[u(t)]$，再通过 $z(t)e^{-j\omega_0 t}$ 移频到零频附近，基频附近的幅值和相角变化成为慢变量，可用较大步长积分
- **并行实虚EMT求解**：EMT侧增加并行求解分别跟踪接口量的实部和虚部，与复数SFA边界量直接耦合
- **异步多速率**：允许SFA步长 $\Delta t_{SFA}$ 与EMT步长 $\Delta t_{EMT}$ 不成整数倍关系，通过插值（过采样）和抗混叠滤波抽取处理快慢数据交换

SFA-EMT的核心优势：无需传输线解耦、无需接口迭代、无时间步延迟，步长配比灵活。

## 交互协议

### 串行交互协议（Serial Protocol）

串行协议中，EMT仿真器和TS仿真器按严格的时序交替执行：

1. **EMT侧推进**：EMT仿真器完成一个交互时间步的积分，向TS侧传递边界量
2. **等待同步**：TS仿真器暂停，等待接收EMT侧边界数据
3. **TS侧推进**：TS仿真器利用EMT边界数据完成一个交互时间步的积分，向EMT侧返回等值更新
4. **周期循环**：重复以上步骤

串行协议精度稳定，但**仿真速度受限于串行等待**：EMT侧通常需要数百个小步长完成一个交互时间步，TS侧等待时间构成主要瓶颈。

### 并行交互协议（Parallel Protocol）

并行协议允许两侧利用上一交互步的信息同时推进：

1. EMT侧和TS侧同时利用各自上一交互步的边界数据进行独立积分
2. 两侧在交互时间点交换新计算出的边界量
3. 不需要等待对方完成计算

并行协议效率更高，但在系统发生大扰动（故障投入、故障清除）时，上一交互步的等值信息可能已严重过时，导致**接口误差显著增大甚至失准**。

### 组合交互协议（Combined Protocol）

Huang & Vittal 2016 提出的组合交互协议在串行和并行之间自动切换：

- **判据**：监测边界电流注入变化率 $\left|\Delta I_{boundary}/\Delta t\right|$ 识别系统扰动
- **强扰动期**（故障投入后~20个工频周期）：使用串行协议，保证等值信息及时更新
- **平稳期**（扰动后慢动态主导阶段）：切换为并行协议，提升整体效率

该自动切换机制使混合仿真的效率相对纯串行协议提升 **6~12倍**（无定量来源，属机制推断），同时在扰动期保持与串行协议相当的精度。

### 仿真模式切换（Simulation Mode Switching）

Huang & Vittal 2018 进一步提出从混合仿真模式**退回纯相量域动态仿真**的能力（"zoom-out"）：

**切换判据**（按优先级分三层）：

1. **延迟等待**：故障清除后延迟 $t_{delay} = 0.2$ s，避开快动态暂态过程
2. **边界电压变化率检测**：$\left|\Delta V_{boundary}/\Delta t\right| < 0.005$ pu，标志快动态已衰减
3. **双域边界收敛检测**：EMT详细系统与相量模型边界电压偏差持续满足 $3\sim5$ 个工频周期

**离散事件同步**：空调压缩机堵转、换相失败等EMT侧离散事件必须作为外部输入传递给相量模型，否则两个模型可能在切换点因内部状态不一致而发散。

模式切换可使总计算时间相对全程混合仿真**显著减少**（原文未给出具体倍数），同时保持较好精度。

## 数学模型

### 机电暂态侧模型

**摇摆方程**（同步发电机简化模型）：

$$M\frac{d^2\delta}{dt^2} + D\frac{d\delta}{dt} = P_m - P_e$$

其中：$M$ 为惯性常数，$D$ 为阻尼系数，$\delta$ 为功角，$P_m$ 为机械功率，$P_e$ 为电磁功率。

**接口注入功率**（机电侧输出到EMT侧）：

$$P_{TS} + jQ_{TS} = V_{TS} \cdot I_{TS}^* = \text{Re}(V_{TS} \cdot I_{TS}^*) + j\text{Im}(V_{TS} \cdot I_{TS}^*)$$

### 电磁暂态侧模型

**节点分析方程**（网络方程，时变电导矩阵）：

$$G(t)\,V(t) = I(t) + I_{hist}(t)$$

其中 $G(t)$ 为时变电导矩阵，$I_{hist}(t)$ 为历史电流源项，$V(t)$ 为节点电压向量。

**接口注入电流**（EMT侧输出到机电侧）：

$$I_{EMT}(t) = Y_{eq}\,V_{eq}(t) + I_{eq}(t)$$

### 接口耦合方程

**功率平衡条件**（接口处近似守恒）：

$$P_{TS} = \text{Re}(V_{TS}\cdot I_{TS}^*) \approx P_{EMT} = \text{Re}(V_{EMT}\cdot I_{EMT}^*)$$

**等值导纳更新**（接口两侧网络等值的核心）：

$$Y_{eq}^{(k)} = \frac{I_{EMT}^{(k)}}{V_{TS}^{(k)}}$$

其中上标 $(k)$ 表示第 $k$ 个交互时间步。

### 延迟敏感性分析

接口延迟 $\tau$ 对混合仿真稳定性的影响可通过特征根分析量化。以含诺顿等值注入的一阶系统为例：

无延迟时特征根：$\lambda_0 = -(R_1+R_2)/L$

含延迟时特征根：$\lambda(\tau) = -R_1/L + W[\tau(R_1+R_2)/L \cdot e^{\tau(R_1+R_2)/L}]/\tau$

延迟使特征根出现**正实部偏移**，系统阻尼比降低。稳定性要求接口延迟满足：

$$\tau_{max} < \frac{1}{10\,f_{max}}$$

其中 $f_{max}$ 为接口关注的最高频率分量（如基频的3~5倍谐波）。

## 多速率协调

### 步长关系与时间同步

混合仿真中 EMT 侧与 TS 侧的步长比为：

$$\Delta t_{TS} = N \times \Delta t_{EMT}$$

典型值：

| 参数 | 典型范围 |
|------|---------|
| $\Delta t_{EMT}$ | 10~100 μs |
| $\Delta t_{TS}$ | 1~10 ms |
| $N = \Delta t_{TS}/\Delta t_{EMT}$ | 10~1000 |

### 插值方法

**线性插值**（TS→EMT方向，插值提供中间时刻边界量）：

$$V(t_{EMT}) = V(t_{TS,k}) + \frac{t_{EMT}-t_{TS,k}}{\Delta t_{TS}}\bigl[V(t_{TS,k+1})-V(t_{TS,k})\bigr]$$

**三次样条插值**（更高精度要求时）：

$$V(t) = a_0 + a_1(t-t_0) + a_2(t-t_0)^2 + a_3(t-t_0)^3$$

三次样条在接口处导数连续，可避免线性插值在突变处引入的数值振荡，但计算代价约为线性的3倍。

### 抗混叠滤波抽取

从EMT侧（高频采样）向TS侧（低频采样）传递数据时，需满足**奈奎斯特采样定理**：

$$f_{TS/2} > f_{EMT\,max}$$

其中 $f_{TS/2}$ 为TS侧采样频率的一半，$f_{EMT\,max}$ 为EMT侧接口信号的最高频率分量。当高频分量超过奈奎斯特频率时，通过抗混叠低通滤波器滤除折叠噪声，再进行抽取。

## 稳定性分析

### 接口稳定性判据

**功率守恒条件**（接口能量是否正确交换）：

$$\Delta P = P_{TS} - P_{EMT} \approx 0$$

当功率差超过一定阈值时，表明接口等值信息严重过时，可能导致数值不稳定。

**阻抗匹配原则**：接口两侧的等值阻抗应尽量匹配：

$$Z_{eq,TS} \approx Z_{eq,EMT}$$

阻抗不匹配会产生反射，导致接口处电压/电流波形畸变。

### 稳定性改善措施

| 措施 | 原理 | 效果 |
|------|------|------|
| 阻尼电阻 | 在接口并联小阻值电阻，增加接口阻尼 | 抑制接口振荡 |
| 低通滤波 | 滤除边界量中的高频分量 | 避免高频分量进入TS侧造成不稳定 |
| 预测校正 | 用预测值替代延迟的边界量，减少延迟误差 | 提升仿真效率 |
| 松弛因子 | 放宽接口收敛条件 | 加速迭代收敛 |
| 接口位移 | 将接口移至弱耦合区域（如控制回路内部） | 利用控制惯性衰减接口误差 |

### 数值阻尼与误差分析

EMT-TS混合仿真的数值误差主要来源：

1. **接口延迟**：$\tau_{interface}$ 导致的等值信息滞后
2. **插值误差**：离散化边界量在时间轴上引入的截断误差
3. **等值近似**：频率相关等值简化为基频等值带来的误差
4. **三相不平衡**：三相平衡假设下的等值与实际不对称系统之差

总误差估计：

$$\epsilon_{total} \approx \epsilon_{\tau} + \epsilon_{interp} + \epsilon_{equiv} + \epsilon_{unbalanced}$$

其中接口延迟误差 $\epsilon_{\tau}$ 通常在总误差中占主导地位。

## 应用场景

### 新能源并网

**风电场并网**：大规模双馈风电场集电系统的详细电磁暂态（如Crowbar动作、换相失败）需要在EMT侧精细建模；电网侧机电动态在TS侧仿真；接口选在升压变压器高压侧。

- [[wind-farm-modeling]] - 风电场建模

**光伏电站并网**：光伏逆变器详细开关模型在EMT侧运行，电网潮流与稳定分析在TS侧进行；光伏渗透率高的区域建议在EMT侧保留更多逆变器细节。

- [[pv-power-plant]] - 光伏电站

### HVDC输电系统

**LCC-HVDC**：传统直流输电的换流器在EMT侧建模为详细阀模型，交流网侧以等值网络接入TS侧；接口通常选在换流变压器网侧。LCC-HVDC换相失败分析是混合仿真的经典应用场景。

- [[vsc-hvdc]] - VSC-HVDC

**MMC-HVDC**：模块化多电平换流器的子模块电容电压均衡、环流抑制控制等需要EMT级精度；交流网用相量模型；MMC-HVDC的混合仿真策略（Liu et al. 2020）包括在EMT侧保留详细MMC模型与在TS侧用戴维南等值代替交流网两种方案。

- [[mmc-model]] - MMC模型

### 故障诱导延迟电压恢复（FIDVR）

FIDVR研究是EMT-TS混合仿真的经典应用场景：单相空调压缩机电机在不对称SLG故障后堵转，导致电压持续偏低。Huang & Vittal 2016 用PSCAD/EMTDC+InterPSS混合仿真平台在WECC大系统中复现了以下传播过程：

1. SLG故障施加于传输系统某母线
2. 故障相电压降低，故障相空调压缩机堵转
3. 堵转传播到非故障相（电机连锁反应）
4. 多个空调压缩机同时堵转导致系统级FIDVR事件

FIDVR研究中，**空调压缩机的详细EMT模型**（含电机饱和效应和启动电流特性）和**大电网的TS等值模型**之间的接口精度直接决定仿真结果的可信度。

### 电力电子化电网的宽频振荡分析

高比例逆变器接入系统中，逆变器群与交流网之间的交互可能激发 **宽频振荡**（几Hz到几kHz）。混合仿真在以下尺度上协同建模：

- EMT侧：详细逆变器控制（PLL、电流内环、功率外环）
- TS侧：同步发电机机电动态、传统负荷
- 接口：经过阻抗归算的戴维南等值或诺顿等值

## 仿真工具实现

### 商业软件方案

| 软件 | 混合仿真方案 | 特点 |
|------|------------|------|
| PSCAD/PSSE | 通过API互联（PSCAD与PSSE之间通过数据接口交换边界量） | 业界标准，PSCAD处理EMT侧，PSSE处理TS侧 |
| DIgSILENT PowerFactory | 内置混合仿真功能（可同时运行EMT和相量域仿真） | 无缝集成，用户无需自行实现接口 |
| RTDS/RSCAD | RSCAD中内置TS侧仿真模块，通过RTPHYSCON接口与EMT侧通信 | 支持实时硬件在环（HIL）仿真 |
| MATLAB/Simulink + SimPowerSystems | Simscape电气元件构建EMT模型，Simulink控制元件构建TS模型，通过共同仿真模块互联 | 灵活定制，适合研究新接口算法 |
| ADPSS | 中国自主研发，支持机电-电磁混合仿真平台，含直流标准化模型库和接口箝位启动功能 | 适合国内大规模交直流电网分析（陈等 2020） |

### 开源方案

- **InterPSS**：开源电力系统仿真软件，提供潮流、短路分析和正序暂态稳定仿真功能，可通过Socket接口与EMT软件交换数据（与PSCAD联用构成混合仿真平台）
- **GridLAB-D**：多域联合仿真框架，支持EMT与配电网动态仿真的协同

### 典型工作流（PSCAD + InterPSS）

1. **分区配置**：在PSCAD中选定内部网络（EMT侧）和外部网络（TS侧）的边界节点
2. **接口模型构建**：在PSCAD中配置Socket通信用户模型，在InterPSS中配置对应的Socket服务端
3. **数据交换配置**：设置交互时间步 $\Delta t_{interface}$ 和数据交换变量（边界电压/电流序列或功率）
4. **协议选择**：根据仿真阶段（故障期/恢复期）选择串行或并行交互协议
5. **初始化**：两端分别初始化至稳态运行点，再启动混合仿真
6. **后处理**：对EMT侧和TS侧结果分别进行时域波形分析和相量域动态分析

## 关键技术挑战

### 接口延迟与误差控制

**挑战**：并行交互协议中接口延迟是主要误差源；串行协议虽精度高但效率受限。

**解决方向**：接口位移（将接口移至控制回路内部）、组合交互协议自动切换、DP-ME动态相量映射等值。

### 三相不平衡条件下的接口精度

**挑战**：传统正序网络等值在不对称故障下需要扩展边界到三相平衡处，削弱了混合仿真的大系统建模优势。

**解决方向**：多端口三相Thévenin等值（正/负/零三序分别建模），Huang & Vittal 2016 的三序TS算法。

### 模式切换时的状态一致性

**挑战**：从混合仿真退回到纯相量域动态仿真时，EMT侧和相量侧的内部状态（离散事件、设备状态）可能不一致，导致切换点发散。

**解决方向**：Huang & Vittal 2018 的离散事件同步机制，将EMT侧捕捉到的离散事件（电机堵转、换相失败）作为外部输入传递给相量模型。

### 计算效率瓶颈

**挑战**：EMT侧计算密集（详细开关模型需要μs级步长），与TS侧大步长之间的数据交换和同步等待时间构成效率瓶颈。

**解决方向**：SFA-EMT异步多速率（MATE框架）、大规模并行计算、FPGA/GPU硬件加速、自适应步长控制。

### 大规模系统的初始化与平稳启动

**挑战**：每个运行方式下需要将潮流数据、换流变抽头、滤波器投切、控制指令和接口初值全部对齐，人工配置成本高且容易因机电侧与电磁侧接口电压/潮流不一致产生暂态冲击。

**解决方向**：ADPSS平台的标准化直流模型库+潮流初始化+接口箝位电压源自动切除（陈等 2020），单方式建模从约15小时降至0.5小时。

## 发展趋势

### 实时混合仿真

**硬件在环（HIL）**：物理控制器与仿真电网通过实时接口联接，接口延迟要求 <1 ms。RTDS等实时仿真平台可实现EMT-TS混合实时仿真，广泛应用于继电保护和控制器的硬件在环测试。

- [[hil-simulation]] - 硬件在环仿真

**数字孪生**：将实时测量数据注入混合仿真平台，实现虚实结合的在线仿真与验证。

### 人工智能辅助

**AI优化接口**：用神经网络预测边界量，提前更新等值参数，减少接口延迟影响。

**智能分区**：基于数据驱动自动识别关注区域（高渗透新能源区域、电力电子密集区域），动态调整仿真精度配置。

### 宽频带建模与多速率耦合

**宽频EMT-TS混合**：将传统基频相量接口扩展到宽频带分析，支持次同步振荡（SSO）和超同步振荡的联合分析。

**异步多速率协议**：如SFA-EMT协议，允许EMT步长与TS步长不成整数倍关系，减少不必要的数据插值误差。

## 相关主题

- [[co-simulation]] - 协同仿真（更广义的多仿真器协同框架）
- [[fdne-model]] - 频变网络等值
- [[network-equivalent]] - 网络等值
- [[multirate-method]] - 多速率仿真方法
- [[real-time-simulation]] - 实时仿真
- [[dynamic-phasor]] - 动态相量法
- [[electromechanical-transient]] - 机电暂态仿真
- [[fault-analysis]] - 故障分析

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| [[application-of-electromagnetic-transient-transient-stability-hybrid-simulation-t\|Application of Electromagnetic Transient-Transient Stability Hybrid Simulation to FIDVR Study]] | 2006 | PSCAD+InterPSS混合仿真平台；组合交互协议自动切换；多端口三相Thévenin等值；三序TS算法 |
| [[methods-of-interfacing-rotating-machine-models-in-emtp\|Methods of Interfacing Rotating Machine Models in EMTP]] | 2010 | 旋转电机模型与EMTP接口方法；机电-电磁接口理论基础 |
| [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical\|Frequency Dependent Network Equivalent for Electromagnetic and Electromechanical Hybrid Simulation]] | 2012 | 频变网络等值用于EMT-机电混合仿真 |
| [[electromechanical-electromagnetic-hybrid-simulation-technology-with-large-number\|Electromechanical-electromagnetic Hybrid Simulation Technology With Large Number of Electromagnetic]] | 2020 | 大规模交直流电网混合仿真数据自动生成；标准化直流模型库；接口箝位启动 |
| [[interface-displacement-and-mapping-equivalence-based-hybrid-simulation-for-hvacd\|Interface Displacement and Dynamic Phasor Mapping Equivalence Based Hybrid Simulation for HVAC/DC Power Grids]] | 2020 | 接口位移+DP-ME；Lambert W延迟分析；HVAC/DC接口精度提升 |
| [[advanced-emt-and-phasor-domain-hybrid-simulation-with-simulation-mode-switching-\|Advanced EMT and Phasor-Domain Hybrid Simulation With Simulation Mode Switching Capability]] | 2018 | MATE框架；正序/三序/三相混合相量建模；两阶段模式切换控制器 |
| [[electromechanical-electromagnetic-transient-hybrid-simulation-of-an-acdc-hybrid-\|Electromechanical-electromagnetic transient hybrid simulation of an ACDC hybrid power grid with UHV]] | 2020 | 特高压交直流混联电网的EMT-TS混合仿真 |
| [[a-multi-domain-co-simulation-method-for-comprehensive-shifted-frequency-phasor-d\|A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequency Phasor Domain]] | 2019 | 移频相量域多域协同仿真 |
| [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model-22\|Hybrid simulation of power systems with SVC dynamic phasor model]] | 2022 | SVC动态相量模型的混合仿真 |
| [[a-harmonic-phasor-domain-co-simulation-method-and-new-insight-for-harmonic-analy\|A Harmonic Phasor Domain Co-Simulation Method and New Insight for Harmonic Analysis]] | 2020 | 谐波相量域协同仿真方法 |
| [[a-novel-interfacing-technique-for-distributed-hybrid-simulations-combining-emt-a\|A Novel Interfacing Technique for Distributed Hybrid Simulations Combining EMT and Dynamic Phasor]] | 2019 | 分布式混合仿真新型接口技术 |
| [[co-simulation-applied-to-power-systems-with-high-penetration-of-distributed-ener\|Co-simulation applied to power systems with high penetration of distributed energy resources]] | 2022 | 高渗透率分布式能源系统的协同仿真 |
| [[direct-interfacing-of-parametric-average-value-models-of-acx2013dc-converters-fo\|Direct Interfacing of Parametric Average-Value Models of AC&DC Converters for Hybrid EMT-TS Simulation]] | 2022 | 参数化平均值模型的直接接口技术 |
| [[acceleration-strategies-for-emt-simulation-of-hvdc-systems\|Acceleration strategies for EMT simulation of HVDC systems]] | 2025 | HVDC系统EMT仿真的加速策略 |
| [[sfa-emt-hybrid-simulation-of-power-systems-application-to-hvdc-systems\|SFA-EMT Hybrid Simulation of Power Systems: Application to HVDC Systems]] | 2026 | MATE框架下SFA-EMT异步多速率接口；消除时间步延迟；非整数倍步长配置 |
