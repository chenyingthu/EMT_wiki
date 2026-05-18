---
title: "诺顿等效 (Norton Equivalent)"
type: method
tags: [norton, equivalent, current-source, admittance, network, circuit-theory]
created: "2026-05-02"
updated: "2026-05-19"
---

# 诺顿等效 (Norton Equivalent)

## 定义与边界

诺顿等效是把线性单端口或多端口网络表示为等效电流源与并联导纳的端口模型。对 EMT 节点分析而言，诺顿形式特别自然，因为网络方程通常以"导纳矩阵乘节点电压等于注入电流"的形式求解。

诺顿等效只保证指定端口的外部电压-电流关系。它不保留被等值网络的内部节点电压、内部故障位置、控制状态或非线性事件。用于非线性设备时，必须说明是某个运行点附近的线性化、分段等效，还是每个时间步更新的伴随模型。

从端口看入的电流方向约定至关重要：若以"电流流出网络"为正，则端口电流 $i$ 与端口电压 $v$ 的关系为 $i = I_N - Y_N v$；若以"注入节点为正"，则关系变为 $i_{\mathrm{inj}} = I_{\mathrm{hist}} + Y_N v$。两种约定在符号上相差一个负号，程序、公式和文档必须保持同一约定，否则会导致电流方向反转的数值错误。

## EMT 中的角色

诺顿等效在 EMT 中承担四类核心功能：

1. **离散化接口**：电感、电容、线路和电力电子子模块经梯形积分或后向欧拉离散后，形成"并联导纳加历史电流源"的诺顿伴随形式，直接接入节点方程 $\mathbf{Y}_n \mathbf{v} = \mathbf{i}$ 统一求解。
2. **外部网络等值**：将大型外部系统、故障点或源网络压缩为端口诺顿等效，减少节点方程规模。外部网络等值、变压器端口模型和多馈入系统常需保留端口间耦合导纳的非对角项。
3. **分区并行求解**：多区域接口（如 MATE）将各子区域诺顿等效电流源和导纳在接口处交换，实现并行计算和故障定位。
4. **混合仿真接口**：EMT-机电混合仿真和 EMT-DP 协同仿真在边界端口使用诺顿形式传递电压电流关系，将另一侧系统等值为注入电流。

与戴维南形式相比，诺顿形式更适合直接进入 [[nodal-admittance-matrix]]，因为节点方程本身以导纳矩阵为核心；但两者的物理边界相同，可无损互换（见 [[thevenin-norton-equivalent]]）。

## 核心机制

### 单端口诺顿形式

对线性单端口，取端口电流流出等值网络或流入网络的符号必须先定义。常见写法为：

$$i = I_{\mathrm{N}} - Y_{\mathrm{N}} v \tag{1}$$

其中 $I_{\mathrm{N}}$ 是端口短路电流（将端口短接时流过的电流），$Y_{\mathrm{N}}$ 是从端口看入的等效导纳。若采用注入节点的电流方向（"注入为正"），也可写成：

$$i_{\mathrm{inj}} = I_{\mathrm{hist}} + Y_{\mathrm{N}} v \tag{2}$$

两种写法的符号不同，页面和代码应保持同一约定。

### 与戴维南等效的互换

若戴维南等效为电压源 $V_{\mathrm{th}}$ 串联阻抗 $Z_{\mathrm{th}}$，且 $Z_{\mathrm{th}}$ 可逆，则两者的互换关系为：

$$Y_{\mathrm{N}} = Z_{\mathrm{th}}^{-1} \tag{3}$$

$$I_{\mathrm{N}} = Y_{\mathrm{N}} V_{\mathrm{th}} = Z_{\mathrm{th}}^{-1} V_{\mathrm{th}} \tag{4}$$

多端口情况下，$Z_{\mathrm{th}}$ 和 $Y_{\mathrm{N}}$ 是矩阵；只有矩阵可逆且端口定义一致时才能直接转换。该互换关系是 [[thevenin-norton-equivalent]] 的数学基础。

### 多端口诺顿形式

对 $m$ 个边界端口，记端口电流向量为 $\mathbf{i} \in \mathbb{C}^m$，端口电压向量为 $\mathbf{v} \in \mathbb{C}^m$，则多端口诺顿形式为：

$$\mathbf{i} = \mathbf{I}_{\mathrm{N}} - \mathbf{Y}_{\mathrm{N}} \mathbf{v} \tag{5}$$

其中 $\mathbf{Y}_{\mathrm{N}} \in \mathbb{C}^{m \times m}$ 是端口导纳矩阵：对角项是自导纳，非对角项是端口间耦合导纳。外部网络等值、变压器高频端口模型和多馈入系统常需要保留非对角项；若把多端口拆成多个独立单端口，必须证明端口间耦合可忽略。

从端口导纳矩阵到 $\pi$ 型等效网络的转换关系为：端口间支路导纳对应非对角导纳的相反数，对地支路由每行导纳求和得到（自导纳减去所有互导纳）。

### 伴随离散诺顿（EMT 梯形积分）

EMT 梯形积分可把动态支路转成诺顿伴随形式。以电感 $L$ 为例，梯形积分的伴随电路为：

$$i^{n+1} = G_{\mathrm{eq}} v^{n+1} + i_{\mathrm{hist}}^{n} \tag{6}$$

其中等效电导 $G_{\mathrm{eq}} = \frac{\Delta t}{2L}$，历史电流源 $i_{\mathrm{hist}}^{n}$ 来自上一时间步状态：

$$i_{\mathrm{hist}}^{n} = -G_{\mathrm{eq}} v^n + i^n \tag{7}$$

电容 $C$ 的梯形伴随诺顿形式为：

$$i^{n+1} = G_{\mathrm{eq}} v^{n+1} + i_{\mathrm{hist}}^{n}, \quad G_{\mathrm{eq}} = \frac{2C}{\Delta t} \tag{8}$$

$$i_{\mathrm{hist}}^{n} = -G_{\mathrm{eq}} v^n - i^n \tag{9}$$

式（6）–（9）构成 [[companion-circuit]] 的诺顿形式，是 [[current-injection]] 接口方法的核心。历史电流源 $i_{\mathrm{hist}}^{n}$ 在每一步自动更新，使节点导纳矩阵 $\mathbf{Y}_n$ 保持不变，从而可复用 LU 分解结果（见 [[fixed-admittance]]）。

### 频变诺顿（FDNE）

对宽频网络等值，诺顿等效的导纳是频率相关函数，不能用常数表示。通过矢量拟合将频域导纳响应 $Y(\jmath\omega)$ 转化为有理函数形式：

$$Y(s) = \sum_{k=1}^{N} \frac{C_k}{s - a_k} + d + sh \tag{10}$$

其中 $a_k$ 为极点，$C_k$ 为留数，$d$ 和 $h$ 为常数项。该有理函数可进一步转化为状态空间形式或卷积形式，在时域中实现为当前导纳加历史注入项——即频变诺顿等效。

多端口频变诺顿的拟合策略（见 [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical]]）：先对导纳矩阵元素的组合响应拟合以获得一组公共极点，再在固定公共极点下分别求各元素留数，从而得到结构一致的多端口模型，避免不同矩阵元素极点不一致导致的实现复杂度。

### 线性化诺顿

对含非线性设备的运行点附近分析，将设备在运行点 $(V_0, I_0)$ 附近线性化，得到增量诺顿等效：

$$\Delta i = Y_{\mathrm{inc}} \Delta v \tag{11}$$

其中 $Y_{\mathrm{inc}} = \partial i / \partial v|_{V_0}$ 是小信号增量导纳。该形式用于小信号稳定性分析和控制器设计，不适用于大扰动暂态。

## 形式化表达

汇总 EMT 中诺顿等效的核心方程：

**单端口：**
$$i = I_{\mathrm{N}} - Y_{\mathrm{N}} v \quad \text{或} \quad i_{\mathrm{inj}} = I_{\mathrm{hist}} + Y_{\mathrm{N}} v$$

**多端口：**
$$\mathbf{i} = \mathbf{I}_{\mathrm{N}} - \mathbf{Y}_{\mathrm{N}} \mathbf{v}$$

**戴维南-诺顿互换：**
$$Y_{\mathrm{N}} = Z_{\mathrm{th}}^{-1}, \quad I_{\mathrm{N}} = Y_{\mathrm{N}} V_{\mathrm{th}}$$

**伴随离散（梯形积分）——电感：**
$$i^{n+1} = \frac{\Delta t}{2L} v^{n+1} + \left(-\frac{\Delta t}{2L} v^n + i^n\right)$$

**伴随离散（梯形积分）——电容：**
$$i^{n+1} = \frac{2C}{\Delta t} v^{n+1} + \left(-\frac{2C}{\Delta t} v^n - i^n\right)$$

**频变有理函数：**
$$Y(s) = \sum_{k=1}^{N} \frac{C_k}{s - a_k} + d + sh$$

**线性化增量：**
$$\Delta i = \left.\frac{\partial i}{\partial v}\right|_{V_0} \Delta v$$

## 分类与变体

| 类型 | 电流源来源 | 导纳来源 | 适用边界 |
|------|-----------|----------|----------|
| 静态单端口诺顿 | 短路电流 | 输入导纳（工频） | 线性网络、固定频率或工频近似 |
| 多端口诺顿 | 端口短路电流向量 | 端口导纳矩阵 | 外部网络和多边界接口 |
| 伴随诺顿 | 历史项 $i_{\mathrm{hist}}^n$ | 数值积分等效导纳 | EMT 时间步支路离散 |
| 频变诺顿 | 状态空间或卷积历史源 | $\mathbf{Y}(s)$ 矢量拟合有理函数 | 宽频网络等值 |
| 线性化诺顿 | 运行点附近增量源 | 小信号导纳 $\partial i / \partial v$ | 控制器和非线性设备局部分析 |

## 关键技术挑战

### 挑战一：符号约定与方向一致性

诺顿等效中电流方向的符号约定必须与节点方程一致。"流出网络"约定得到式（1）的减法形式，"注入节点"约定得到式（2）的加法形式。混用约定会导致注入电流方向反转，造成数值结果符号错误。程序应在文档中显式声明约定，并在每次调用时保持一致。

### 挑战二：频变诺顿的无源性

频变诺顿模型经矢量拟合后，若所得有理函数非无源（存在右半平面极点），时域仿真可能产生能量使系统数值不稳定。修正方法包括半尺寸无源性测试矩阵定位无源性违规点、参数扰动强制无源性等（见 [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical]]）。

### 挑战三：多端口导纳矩阵的条件数

多端口导纳矩阵 $\mathbf{Y}_{\mathrm{N}}$ 的条件数差或非对称时，会放大数值误差并降低迭代求解收敛速度。当端口间耦合不对称时，应检查端口方向和测量独立性，必要时对矩阵做对称化处理或条件数预处理。

### 挑战四：伴随诺顿的历史项同步

伴随诺顿的历史电流源 $i_{\mathrm{hist}}^n$ 必须在每个时间步正确更新——包括前向 Euler 阶段的预估和梯形积分阶段的校正。若历史项更新时机错误或数值精度不足，会导致相移和能量误差的累积，在长时间仿真中使结果偏离详细模型。

### 挑战五：外部网络等值与内部动态的边界模糊

诺顿等效只保证端口外部等效，不保留被等值网络内部节点电压、控制状态或非线性事件。在故障计算中把端口等值结果外推到被等值网络内部支路电流是常见误区，应在文档中明确等值边界和适用范围。

## 量化性能边界

| 应用场景 | 等效类型 | 性能指标 | 数据来源 |
|----------|----------|----------|----------|
| 工频稳态分析 | 静态单端口诺顿 | 误差 < 1%（工频阻抗） | — |
| 开关暂态仿真 | 伴随诺顿（梯形积分） | $\Delta t$ / 2L 电导，精度由 $\Delta t$ 控制 | [[an-efficient-half-bridge-mmc-model-for-emtp-type-simulation-based-on-hybrid-nume]] |
| 宽频谐波分析 | 频变诺顿 | 有理函数拟合误差 < 0.1%（测试频段） | [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i]] |
| 大规模网络等值 | 多端口诺顿 | 端口数 2–20，精度损失 < 2 dB（宽频段） | [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical]] |
| 快速 PET 仿真 | 桥臂诺顿聚合 | 加速比 2–5×（vs 详细开关模型），精度误差 < 1% | [[equivalent-modeling-method-of-parallel-elements-for-fast-electromagnetic-transie]] |

原文未报告可核验的数值结果时，标注"原文未报告可核验的数值结果"。

## 适用边界与选择指南

| 场景 | 推荐类型 | 理由 |
|------|----------|------|
| 工频短路计算 | 静态单端口诺顿 | 仅需 50/60 Hz 阻抗，计算量小 |
| 开关暂态 EMT 仿真 | 伴随诺顿 | 梯形积分精度高，与节点方程自然接口 |
| 宽频阻抗拟合 | 频变诺顿 | 保留工频到数千 Hz 的频变特性 |
| 外部大网络等值 | 多端口诺顿 | 保留端口间耦合，支持多边界接口 |
| 控制器小信号分析 | 线性化诺顿 | 增量模型反映局部动态 |
| 电力电子并网快速仿真 | 桥臂诺顿 + 固定导纳 | 导纳固定避免矩阵重分解，支持并行 | [[a-bridge-arm-module-based-fixed-admittance-adc-model-for-converters-in-emt-simul]] |

## 相关页面

- [[thevenin-equivalent]] 是诺顿等效的对偶形式（电压源串联阻抗）。
- [[thevenin-norton-equivalent]] 解释两者在 EMT 离散求解中的互换关系，是诺顿形式的核心理论支撑。
- [[current-injection]] 与诺顿等效共享电流注入接口，但更强调设备向网络注入电流的建模方式。
- [[nodal-admittance-matrix]] 是诺顿等效进入的矩阵框架；诺顿形式比戴维南形式更适合直接构建节点导纳矩阵。
- [[equivalent-circuit-method]] 是包含诺顿、戴维南、RLC 和磁路等效的通用方法页。
- [[detailed-equivalent-model]] 常把宽频端口模型最终转成诺顿形式进入时域求解。
- [[ac-coupled-network-equivalent]] 和 [[layered-connection]] 中的外部交流边界常使用多端口诺顿表示。
- [[fixed-admittance]] 利用诺顿等效的恒定导纳特性避免矩阵重分解。

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i]] | — | 多端口频变诺顿等值：端口导纳矩阵→π型网络→EMTP RLC模块拟合 |
| [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical]] | — | FDNE用于EMT-机电混合仿真接口：无源性处理流程 |
| [[an-efficient-half-bridge-mmc-model-for-emtp-type-simulation-based-on-hybrid-nume]] | — | MMC桥臂诺顿等效：蛙跳更新使电导常数 |
| [[equivalent-modeling-method-of-parallel-elements-for-fast-electromagnetic-transie]] | — | CHB-PET串行诺顿等效聚合：导纳单元预存+并行 |
| [[a-state-variables-elimination-based-emtp-type-constant-admittance-equivalent-mod]] | — | 状态变量消去生成恒定诺顿导纳：网络-节点电压-历史源三层结构 |
| [[a-bridge-arm-module-based-fixed-admittance-adc-model-for-converters-in-emt-simul]] | — | BAM-ADC固定导纳诺顿：参数化桥臂模块等效 |
| [[interfacing-factor-based-white-box-transformer-modeling-method]] | 2014 | 诺顿形式变压器接口模型 |
| [[34tpwrd20172749427]] | 2017 | 多端口FDNE端口导纳矩阵拟合 |
| [[dynamic-phasor-based-interface-model-for-emt-and-transient-stability-hybrid-simu]] | 2017 | 动态相量接口中的频变诺顿等值 |
| [[an-efficient-phase-domain-synchronous-machine-model-with-constant-equivalent-adm]] | 2019 | 定导纳同步机诺顿模型 |
| [[adaptive-modular-multilevel-converter-model-for-electromagnetic-transient-simula]] | 2020 | 自适应MMC诺顿接口模型 |
| [[implementation-of-the-universal-line-model-in-the-alternative-transients-program]] | 2021 | ULM实现中的诺顿历史源处理 |