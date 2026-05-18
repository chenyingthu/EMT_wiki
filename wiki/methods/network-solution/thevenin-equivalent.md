---
title: "戴维南等效 (Thevenin Equivalent)"
type: method
tags: [thevenin, equivalent, voltage-source, impedance, network, circuit-theory, port-equivalent]
created: "2026-05-02"
updated: "2026-05-19"
---

# 戴维南等效 (Thevenin Equivalent)

## 定义与边界

戴维南等效（Thevenin Equivalent）将线性单端口或多端口网络在指定端口上的外部行为表示为等效电压源与串联阻抗的组合。对单端口电路，其端口伏安关系为：

$$
v = V_{\mathrm{th}} - Z_{\mathrm{th}} \, i \tag{1}
$$

其中 $v$ 为端口电压，$i$ 为端口电流（按约定方向），$V_{\mathrm{th}}$ 为开路端口电压（open-circuit voltage），$Z_{\mathrm{th}}$ 为从端口看入的等效阻抗（Thevenin impedance）。该等效仅保证端口外部伏安特性等价，不保留被等值网络内部节点电流分布、保护动作逻辑或非线性状态变量。

本页聚焦 **EMT 仿真中的戴维南端口等效**。它不同于以电流源并联导纳表达的 [[norton-equivalent]]，也不同于涵盖 RLC 综合与磁路等效的 [[equivalent-circuit-method]]。戴维南等效与 [[network-equivalent]] 的关系：网络等值是系统级主题，包含戴维南形式、诺顿形式及频变等值三类端口等效的统一框架。

## EMT 中的作用

在 EMT 仿真中，戴维南等效承担四类核心功能：

**（1）外部交流网络等值接入**。在补偿法（compensation method）中，线性网络对非线性端口表现为多端口戴维南等效，接口量为端口开路电压 $v_o$、等效电阻矩阵 $\mathbf{R}_{\mathrm{th}}$ 以及端口电流 $i$ 和电压 $v$ 的关系 $v = v_o - \mathbf{R}_{\mathrm{th}} \, i$（Dufour 2011）。该形式使非线性元件与主网络的迭代解耦成为可能。

**（2）子系统边界的接口形式**。在多区域或多速率协同仿真（如 MATE-TLM 多速率框架，Li 2019）中，交流子系统通过接口等效为戴维南电压源 $\mathbf{e}_{\mathrm{th}}$ 与阻抗 $\mathbf{Z}_{\mathrm{th}}$，供直流侧小步长区域调用。接口形式由子系统内部节点方程和接口支路方程共同决定（MATE 方程）。

**（3）VSC-HVDC 直流故障等值**。两电平 VSC 的直流侧可表示为调制指数依赖的戴维南等效：$V_{\mathrm{th}} = \frac{m_d}{2} V_{sd} + \frac{m_q}{2} V_{sq} - \frac{8}{3m^2} R \, i_{dc}$，等效阻抗 $Z_{\mathrm{dc}} = \frac{8}{3m^2}(R + j\omega L)$（Bahirat 2015）。该模型将 AC 侧阻抗以变压器类比方式折算到 DC 侧，大幅降低直流故障仿真计算量。

**（4）状态空间集群的 I 型接口**。在状态空间-节点联合法（SSN）中，状态空间电气集群经梯形积分离散化后，可作为 I 型（戴维南型）接口并入全局节点导纳矩阵，实现状态空间子系统与节点网络的同步耦合求解（Dufour 2011）。

## EMT 建模方法

### 方法 1：工频静态戴维南（Single-Frequency Thevenin）

最基础的端口等效形式，在工频（50/60 Hz）下用标量或序网阻抗表达：

$$
V_{\mathrm{th}} = V_{\mathrm{oc}}, \qquad Z_{\mathrm{th}} = \frac{V_{\mathrm{oc}}}{I_{\mathrm{sc}}} \tag{2}
$$

其中 $V_{\mathrm{oc}}$ 为端口开路电压（工频相量），$I_{\mathrm{sc}}$ 为端口短路电流。当网络线性且不含受控源时，可通过独立源置零后加测试源法或直接计算输入阻抗得到 $Z_{\mathrm{th}}$。

**特点**：计算简单，适合短路容量评估、电压稳定性分析和静态边界条件近似。**失效场景**：不适用于谐波域（频变效应显著时 $Z_{\mathrm{th}}$ 不再是常数）、暂态初期（$\beta$ 或 $\alpha$ 主导的开关瞬态）或非线性元件附近（磁饱和导致 $Z_{\mathrm{th}}$ 随运行点变化）。

### 方法 2：EMT 时域戴维南（Time-Domain Thevenin with History Source）

时域伴随模型中，将历史电流源与步长相关等效阻抗结合表达端口特性。节点导纳矩阵求解时，若子网络用戴维南形式表示，等效于对诺顿形式的转置：

$$
\mathbf{v} = \mathbf{V}_{\mathrm{th}} - \mathbf{Z}_{\mathrm{th}} \, \mathbf{i}, \qquad \mathbf{V}_{\mathrm{th}} = [\mathbf{Y}_{\mathrm{th}}]^{-1} \, \mathbf{i}_{\mathrm{h}}(t - \Delta t) \tag{3}
$$

其中 $\mathbf{i}_{\mathrm{h}}$ 为历史电流源向量（由上一时刻状态决定），$\mathbf{Y}_{\mathrm{th}} = \mathbf{Z}_{\mathrm{th}}^{-1}$。

**特点**：与节点导纳矩阵自然融合，适合分区接口、子系统边界和补偿法非线性迭代。**失效场景**：$\mathbf{Z}_{\mathrm{th}}$ 条件数差或不对称（强耦合多端口）时误差增大；矩阵不可逆时无法转为诺顿形式。

### 方法 3：多端口戴维南（Multi-Port Thevenin）

对 $m$ 个端口的系统，戴维南等效写成矩阵-向量形式：

$$
\mathbf{v} = \mathbf{V}_{\mathrm{th}} - \mathbf{Z}_{\mathrm{th}} \, \mathbf{i} \tag{4}
$$

其中 $\mathbf{V}_{\mathrm{th}} = [V_{\mathrm{th},1}, \ldots, V_{\mathrm{th},m}]^{\mathrm{T}}$ 为开路电压向量，$\mathbf{i} = [i_1, \ldots, i_m]^{\mathrm{T}}$ 为端口电流向量，$\mathbf{Z}_{\mathrm{th}}$ 为 $m \times m$ 阻抗矩阵，**非对角项表示端口间耦合**。除非有明确的弱耦合证据（如对角块优势），不应将多端口等效拆解为互不相关的单端口。

**特点**：在 MATE-TLM 多速率协同仿真（Li 2019）中，每个交流子系统用多端口戴维南接口接入直流侧。接口方程为 $e_{\mathrm{th}k}(t) = \mathbf{M}_k^{\mathrm{T}} [\mathbf{Y}_k]^{-1} \mathbf{i}_{\mathrm{h}k}(t - \Delta T)$，$Z_{\mathrm{th}k} = \mathbf{M}_k^{\mathrm{T}} [\mathbf{Y}_k]^{-1} \mathbf{M}_k$（$\mathbf{M}_k$ 为连接矩阵），可一次性更新多个端口的等效边界。

**失效场景**：端口间存在密耦合（如紧密母线群）但被错误拆解时，会丢失 $Z_{\mathrm{th}}$ 的非对角耦合项，导致接口误差显著增加；矩阵 $\mathbf{Z}_{\mathrm{th}}$ 病态时数值稳定性变差。

### 方法 4：频变戴维南（Frequency-Dependent Thevenin）

宽频网络等值中，等效阻抗是频率的函数 $Z_{\mathrm{th}}(s)$ 或由离散状态空间模型表达。在时域中实现频变阻抗有两条路径：

**路径 A（向量拟合 + 卷积）**：先用矢量拟合（vector fitting）将 $Z_{\mathrm{th}}(s)$ 拟合为有理函数形式，进而成离散状态空间模型，在时域中以卷积历史源方式注入端口。

**路径 B（等效网络综合）**：通过 FDNE（Frequency Dependent Network Equivalent）方法，将端口看入的导纳/阻抗频率特性综合为 RLC 梯形网络或诺顿等效导纳矩阵（Morched et al. 1993）。该方法在 EMTP 中有成熟实现，可直接生成宽频等效电路。

**特点**：能够捕捉网络谐振特性，适合雷电冲击、开关操作和故障暂态的宽频分析。**失效场景**：进入时域前需检查无源性（passivity enforcement），否则离散化后系统可能出现不稳定激励；拟合阶数不足时高频或低频特性失真。

### 方法 5：调制指数依赖戴维南（Modulation-Index Dependent Thevenin for VSC）

针对两电平 VSC-HVDC，Bahirat 2015 提出的调制指数依赖戴维南模型，将交流侧阻抗通过 d-q 坐标变换和"理想 DC 变压器"类比折算到直流侧：

$$
i_{dc} = \frac{3}{4}(m_d \, i_d + m_q \, i_q) \tag{5}
$$

$$
Z_{dc,\;eq} = \frac{8}{3(m_d^2 + m_q^2)}(R + j\omega L) \tag{6}
$$

$$
V_{th} = \frac{3}{4} \cdot \frac{m_d \, V_{sd} + m_q \, V_{sq}}{m_d^2 + m_q^2} \tag{7}
$$

其中 $m_d, m_q$ 为 d-q 轴调制指数，$V_{sd}, V_{sq}$ 为电网电压 d-q 轴分量。等效阻抗与调制指数平方成反比——高调制指数（满载）时等效阻抗小，低调制指数（轻载）时等效阻抗大。

**特点**：大幅加速 VSC-HVDC 直流侧故障仿真（750 μs 步长下达 126 倍加速，精度 95% 以上，PP 故障误差 <1%）。**失效场景**：PG（极对地）故障存在 5-10% 电流低估（因零序分量处理简化）；换流器闭锁后需切换为 APDR（反并联二极管整流器）等效，而非继续使用受控 VSC 模型。

## 形式化表达

戴维南等效的核心数学框架由以下公式体系构成：

**单端口基础关系**：

$$
v = V_{\mathrm{th}} - Z_{\mathrm{th}} \, i \quad \Leftrightarrow \quad i = \frac{V_{\mathrm{th}} - v}{Z_{\mathrm{th}}}
$$

**诺顿-戴维南互换**（当 $\mathbf{Z}_{\mathrm{th}}$ 可逆时）：

$$
\mathbf{Y}_{\mathrm{N}} = \mathbf{Z}_{\mathrm{th}}^{-1}, \qquad \mathbf{I}_{\mathrm{N}} = \mathbf{Y}_{\mathrm{N}} \, \mathbf{V}_{\mathrm{th}} \tag{8}
$$

符号约定：端口电流方向需与页面、公式和代码保持一致，否则等式中符号需相应调整。

**补偿法非线性接口**（Dufour 2011）：

线性网络对非线性端口 $k$ 的戴维南接口方程：

$$
v_k = v_{ok} - R_{\mathrm{th}k} \, i_k \tag{9}
$$

其中 $v_{ok}$ 为端口开路电压，$R_{\mathrm{th}k}$ 为等效电阻，$i_k$ 为端口电流。非线性元件满足 $v_k = f(i_k)$，联立求解 $f(i_k) = v_{ok} - R_{\mathrm{th}k} \, i_k$。

**MATE-TLM 接口戴维南参数**（Li 2019）：

$$
e_{\mathrm{th}k}(t) = \mathbf{M}_k^{\mathrm{T}} [\mathbf{Y}_k]^{-1} \mathbf{i}_{\mathrm{h}k}(t - \Delta T), \quad Z_{\mathrm{th}k} = \mathbf{M}_k^{\mathrm{T}} [\mathbf{Y}_k]^{-1} \mathbf{M}_k \tag{10}
$$

**VSC 直流侧戴维南等效**（Bahirat 2015）：

$$
V_{th} = \frac{m_d}{2} V_{sd} + \frac{m_q}{2} V_{sq} - \frac{8}{3m^2} R \, i_{dc} \tag{11}
$$

$$
Z_{dc,\;eq} = \frac{8}{3m^2}(R + j\omega L) \tag{12}
$$

## 关键技术挑战

### 挑战 1：多运行点与非线性设备的固定 $Z_{\mathrm{th}}$ 失效

当被等值区域包含控制限幅、饱和或保护动作时，单一固定阻抗无法反映运行点迁移。**应对方向**：采用多运行点查表法（switching between multiple Thevenin instances）或在每次拓扑变化后重新计算 $Z_{\mathrm{th}}$。

### 挑战 2：频变等值的无源性强制

矢量拟合得到的 $Z_{\mathrm{th}}(s)$ 可能违反无源性（passivity），在时域激励下导致数值不稳定。**应对方向**：在拟合后增加无源性强迫修正（passivity enforcement）步骤，确保 $|\mathbf{Y}_{\mathrm{th}}(j\omega)|$ 和 $|\mathbf{Z}_{\mathrm{th}}(j\omega)|$ 在全频段为正实部。

### 挑战 3：多端口等效的耦合处理

$\mathbf{Z}_{\mathrm{th}}$ 的非对角项处理不当会丢失接口间耦合，导致多端系统（如 MTDC）故障电流计算误差显著。**应对方向**：保留完整的 $m \times m$ 阻抗矩阵；对强耦合端口群使用统一多端口等效而非拆解。

### 挑战 4：测量型戴维南估计的不确定度

通过现场扰动测试获取戴维南参数时，扰动幅值、窗口长度和噪声处理直接影响估计精度。**应对方向**：需明确报告扰动幅值（应足够大以克服噪声但不超过设备限额）、端口方向、采样窗口和滤波方法。

### 挑战 5：实时仿真平台的时间约束

在 FPGA 实时 EMT 求解器中，补偿法要求在固定步长（5 μs 或 3 μs）内完成"戴维南接口更新→非线性函数求值→小规模线性方程求解→收敛判定"整条链路，时间确定性是关键约束（an-iterative-real-time-nonlinear-electromagnetic-transient-solver-on-fpga）。

## 量化性能边界

| 建模方法 | 典型步长 | 加速比 | 精度/误差 | 适用场景 |
|---------|---------|--------|----------|---------|
| 工频静态戴维南 | 50 μs（工频域） | — | 近似（误差随谐波含量增加） | 短路容量评估、静态电压稳定分析 |
| EMT 时域戴维南 | 20–50 μs | — | 与节点导纳法一致 | 分区接口、补偿法非线性迭代 |
| 多端口戴维南（MATE） | 交流侧 500 μs / 直流侧 50 μs（n=10） | **150–160 倍**（vs 单速率全步长仿真） | 接口误差 0.0084–0.0116（相对参考） | LCC-HVDC 多速率协同仿真 |
| 频变戴维南（FDNE） | 依赖拟合阶数 | 取决于网络规模 | 有理函数拟合误差可控 | 宽频 EMT（雷电、开关故障） |
| 调制指数依赖戴维南 | 5 μs（详细模型）/ 750 μs（等效模型） | **3 倍**（5 μs）/ **126 倍**（750 μs） | PP 故障误差 <1%；PG 故障误差 5–10% | VSC-HVDC 直流故障快速计算 |

*数据来源：Li 2019（多速率 MATE-TLM，实测 2412 母线系统）；Bahirat 2015（VSC 戴维南，ATP-EMTP 仿真）*

## 变体分类表

| 变体 | 端口源形式 | 阻抗形式 | 适用边界 |
|------|-----------|---------|---------|
| 工频静态戴维南 | 开路相量电压（标量） | 标量或序网阻抗 | 短路容量计算、静态电压稳定边界 |
| EMT 时域戴维南 | 历史电压源 | 步长相关等效阻抗 | 伴随模型接口、分区协同仿真 |
| 多端口戴维南 | 电压源向量 | $m \times m$ 阻抗矩阵 | 多边界子系统、MATE-TLM 接口 |
| 频变戴维南 | 状态或卷积历史源 | $Z(s)$ 有理函数或离散状态空间 | 宽频网络等值、雷电/开关暂态 |
| 调制指数依赖戴维南 | 运行点相关电压源 | $Z_{dc,eq} \propto 1/m^2$ | VSC-HVDC 直流故障等值 |

## 适用边界与失效模式

### 适用条件

- 被等值区域内部拓扑已知且可用外部端口特性描述
- 端口间耦合关系明确或可通过测量获取 $\mathbf{Z}_{\mathrm{th}}$ 非对角项
- 频变等值的拟合阶数经无源性检验通过

### 失效模式

1. **端口等效用于内部故障或内部设备应力分析**：戴维南等效仅保证端口外部行为等价，内部节点电压、电流分布不受约束。
2. **非线性设备使用固定 $Z_{\mathrm{th}}$ 而不更新运行点**：饱和变压器、避雷器等元件在故障穿越过程中 $Z_{\mathrm{th}}$ 变化剧烈，固定阻抗会严重失真。
3. **开路电压和等效阻抗来自不同拓扑或不同控制状态**：导致端口特性不自洽，接口误差无法估计。
4. **多端口等效忽略互阻抗**：在 MTDC 或多端 FACTS 系统中，端口耦合是故障电流分布的主要决定因素，忽略互阻抗导致多端故障电流计算错误。
5. **宽频 EMT 中使用工频阻抗**：导致谐振分析、雷电或开关暂态结论失真——$Z_{\mathrm{th}}$ 在 1 kHz–1 MHz 频段可能变化 10 倍以上。
6. **$\mathbf{Z}_{\mathrm{th}}$ 病态或不可逆时强行转为诺顿形式**：导致数值不稳定或求解发散。

## 相关方法与相关模型

- [[norton-equivalent]]：戴维南等效的电流源对偶形式，节点导纳矩阵更偏好诺顿形式（$\mathbf{Y} = \mathbf{Z}^{-1}$）。
- [[thevenin-norton-equivalent]]：两种形式在 EMT 离散时域中的转换机制与边界条件汇总。
- [[equivalent-circuit-method]]：更宽泛的端口等效、RLC 综合与磁路等效入口。
- [[network-equivalent]]：系统级网络等值主题，统一涵盖戴维南、诺顿与频变等值三类方法。
- [[companion-circuit]]：电感、电容经梯形/后向欧拉离散化后，在局部表现为戴维南或诺顿伴随支路。
- [[co-simulation]]：多区域接口常使用戴维南或诺顿边界交换量，MATE-TLM 是典型实现框架。
- [[vector-fitting]]：频变等值的有理函数拟合工具，是 FDNE 方法的核心算法支撑。

## 来源论文

- [[a-multi-area-thevenin-equivalent-based-multi-rate-co-simulation-for-control-desi]] — Li 2019：提出 MATE-TLM 多区域戴维南等值框架，在 LCC-HVDC 多速率协同仿真中实现 150–160 倍加速，接口误差 <0.012。
- [[modulation-index-dependent-thevenin-equivalent-circuit-model-of-vsc-and-apdr]] — Bahirat 2015：提出调制指数依赖的 VSC 戴维南等效，PP 故障误差 <1%，750 μs 步长下加速 126 倍，PG 故障误差 5–10%。
- [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient]] — Dufour 2011：提出状态空间-节点联合法，集群可采用 I 型（戴维南）或 V 型（诺顿）接口并入全局导纳矩阵。
- [[an-iterative-real-time-nonlinear-electromagnetic-transient-solver-on-fpga]]：补偿法中线性网络对非线性端口表现为多端口戴维南等效，FPGA 实时求解器在 5 μs 步长内完成非线性端口迭代收敛。