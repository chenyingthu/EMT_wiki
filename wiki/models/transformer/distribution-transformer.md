---
title: "配电变压器 (Distribution Transformer)"
type: model
tags: [distribution-transformer, distribution-network, step-down, power-quality, emt, saturation, ferroresonance, solid-state-transformer]
created: "2026-05-04"
updated: "2026-05-16"
---

# 配电变压器 (Distribution Transformer)

## 定义与边界

配电变压器是将中压配电网（通常6-35 kV）电压降至低压用户电压（220/380 V）的电力变压器，是配电网与用户的接口设备。与输电变压器相比，配电变压器更靠近用户侧，承受的短路电流更大、电能质量问题更敏感；与换流变压器相比，配电变压器工作于工频，设计上更关注负载损耗和电压调整率，而非谐波补偿。

**边界限定**：本页面聚焦于配电变压器的EMT建模，包括饱和特性、磁滞回线、铁磁谐振、宽频建模等核心问题；不包括输电变压器（见[[transformer-model]]）或换流变压器（见[[converter-transformer-model]]）。

## EMT中的作用

配电变压器在配电网EMT仿真中承担关键角色：

- **电压变换**：中压到低压的精确变换，需考虑负载引起的电压调整率
- **故障分析**：短路电流计算和过电压传播（见[[symmetrical-components]]）
- **电能质量**：谐波传递特性、电压暂降与恢复（见[[power-quality]]）
- **保护配合**：熔断器、断路器保护整定依据（见[[impedance-relay]]）
- **分布式电源**：DG接入对变压器负载率和谐波特性的影响（见[[distributed-parameter-line]]）
- **铁磁谐振**：非线性铁芯与分布电容耦合可能激发铁磁谐振（见[[ferroresonance]]）

## EMT建模方法

配电变压器的EMT建模按建模精度和计算效率分为四个层次：

### 1. 线性集总模型（Ideal Transformer）

将变压器视为理想变压器加串联阻抗：

$$
\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} R_k + j\omega L_k & -j\omega M \\ -j\omega M & R_k' + j\omega L_k' \end{bmatrix} \begin{bmatrix} i_1 \\ i_2 \end{bmatrix}
$$

其中$M = k\sqrt{L_1 L_2}$为互感，$k$为耦合系数。空载时$i_2 = 0$，励磁电流$i_0 = v_1/(R_k + j\omega L_k)$。

**特点**：参数少（$R_k$、$L_k$、$k$），计算快，适用于工频稳态和低频暂态分析。
**局限**：忽略饱和、磁滞、涡流，无法捕捉励磁涌流和谐波共振。

### 2. 非线性饱和模型（Saturation Model）

考虑铁芯磁化曲线的非线性特性：

$$
i_m = f(\phi) = \begin{cases} a_1 \phi + a_3 \phi^3 + a_5 \phi^5 + \cdots & \text{饱和区} \\ \frac{\phi}{L_0} & \text{线性区} \end{cases}
$$

常用三种饱和模型实现方式：

**2.1 分段线性模型（Piecewise Linear）**

将饱和曲线离散为N段，每段用线性电感$L_i$表示：

$$
L_i = \frac{\Delta \phi_i}{\Delta i_i}, \quad i \in [1, N]
$$

切换条件：当工作点超出当前段的$\phi$范围时，更新电感值。

**2.2 Jiles-Atherton磁滞模型**

Jazebi等（2015）提出的对偶原理Cauer等效电路基于JA理论将磁滞特性转化为电路接口量。Sima等（2018）进一步将JA模型表示为电压驱动的动态ψ-i磁滞电抗器：

$$
\psi = N A B = N A \mu_0 (H + M), \quad i = H l / N
$$

有效磁场$H_e = H + \alpha M$，无磁滞磁化$Man = \frac{M_s}{a} h \cdot \frac{\cosh^{-1}(H_e/a)}{\sinh(H_e/a)}$，微分磁化方程：

$$
\frac{dM}{dH} = \frac{(Man - M)}{(1 + c)\delta k - \alpha(Man - M)}
$$

其中$M_s$为饱和磁化强度，$a$、$\alpha$、$k$、$c$为材料参数。Type-94控制元件将电压驱动的动态损耗（涡流+剩余损耗）引入静态ψ-i JA模型，形成动态Model 1和Model 2两种耦合方式。

**2.3 Frolich方程模型**

$$
i = \frac{\phi}{L_0 + \lambda |\phi|}
$$

其中$\lambda$为饱和系数，$\lambda = 0$时退化为线性电感。Frolich模型比多项式更简洁，但精度略低。

**量化性能**（Sima 2018）：在50 Hz和150 Hz电流测试下，动态Model 1比Model 2更匹配实验结果；铁磁谐振测试验证了含磁滞回线的暂态特性建模必要性。

### 3. 磁滞回线详细模型（Hysteresis Loop Model）

Wu等（2017/2022）基于PSCAD/EMTDC实现的磁滞特性变压器模型：

**3.1 可变电感法**

核心是分段线性插值拟合最大磁滞回线：

$$
\frac{\phi_X - \phi_N}{\phi_{P1} - \phi_N} = \frac{d_X}{d_{P1}}
$$

次磁滞回线上支路磁链：

$$
\phi_X = \frac{\phi_{main}(\phi_{P1} - \phi_N) + d_{P1}\phi_N}{\phi_{P1} - \phi_N + d_{P1}}
$$

可变电感值实时更新：

$$
L = \frac{d\phi_X}{di} = \frac{u}{di/dt}
$$

**3.2 延时比较法工作点跟踪**

通过连续三个仿真步长的电流差分符号判定工作点位置：

$$
\begin{cases} I_k(t-\Delta t) - I_k(t-2\Delta t) < 0 \\ I_k(t) - I_k(t-\Delta t) < 0 \end{cases} \Rightarrow \text{下降段}
$$

当工作点进入单值饱和区时，切换至磁滞中线循环程序以保证数值稳定。

**量化性能**（Wu 2017）：PSCAD用户自定义模型与ATP-EMTP BCTRAN模型的三相励磁涌流最大峰值平均相对误差约12%，衰减时间相对误差约9.1%~10%；与1 kVA实测录波相比，涌流最大峰值误差约1.6%~2%，稳态峰值误差约13.3%。

### 4. 白盒宽频模型（White-Box Frequency-Dependent Model）

Jazebi等（2015）基于对偶原理构建的双侧Cauer等效电路：

**4.1 磁场扩散方程**

圆柱坐标系下的磁场扩散方程：

$$
\frac{\partial^2 H}{\partial r^2} + \frac{1}{r}\frac{\partial H}{\partial r} = \mu \sigma \frac{\partial H}{\partial t}
$$

**4.2 频变参数解析**

基于Maxwell方程求解绕组内部磁场分布，利用磁能守恒推导各子段初始电感，结合邻近效应系数矩阵修正得到频变漏感与绕组电阻的解析表达式：

$$
R_{ac}(\omega) = R_{dc} \cdot F(\omega), \quad L(\omega) = L_{\infty} + \frac{\Delta L}{1 + j\omega\tau}
$$

**4.3 理想变压器隔离**

采用1:1理想变压器将磁路元件（电感）与电路元件（电阻、电容）在物理节点处严格解耦，确保连接点符合实际电磁能量流向与安培定律。

**量化性能**（Jazebi 2015）：等效电阻与电感计算误差<5%（对比FEM）；7阶模型将有效预测范围延伸至15 MHz以上；忽略涡流效应时，高频阻抗幅值误差超过30%。

Mombello等（2022）进一步提出基于SVD低秩分解的紧凑型白盒模型，将原本满秩的耦合矩阵分解为低秩形式，辅助回路数量大幅缩减，满足ATP-EMTP≤40阶电感矩阵限制（原模型1278阶无法直接使用）。

## 关键技术挑战

### 挑战1：磁饱和对暂态仿真的影响

**问题**：配电变压器铁芯在瞬态事件（空载合闸、故障清除、直流偏磁）中进入饱和区，导致励磁电流剧增和谐波含量升高。

**机制**：饱和系数$k$随磁通变化：$k = f(\phi)$，其中$\phi = \sqrt{\phi_{ad}^2 + \phi_{aq}^2}$。考虑饱和后，d/q轴电抗变为$k \cdot x_{ad(unsat)}$和$k \cdot x_{aq(unsat)}$（Hiramatsu 2012）。

**影响**：传统线性Park模型低估甩负荷后电压偏差，实测甩负荷特性与考虑饱和的模型差异显著。

### 挑战2：铁磁谐振风险

**问题**：配电变压器非线性铁芯与配电网分布电容（电缆段长度、架空线对地电容）耦合，在特定激励下可能激发频率约0.1-10 kHz的谐振过电压。

**机制**：铁磁谐振的本质是磁链-电容能量交换的非线性振荡，可用DAE描述：

$$
C \frac{dv}{dt} = i_L(v), \quad L \frac{di_L}{dt} = v
$$

其中$i_L(v)$为饱和电感的ψ-i特性。

**抑制方法**（Sima 2018）：在变压器中性点加装阻尼电阻，或采用动态磁滞模型预估谐振风险。

### 挑战3：励磁涌流峰值估算

**问题**：变压器空载合闸时的励磁涌流峰值可达额定电流的5-10倍，对保护装置的CT饱和和断路器选择有重要影响。

**关键因素**：合闸角度、剩磁方向、饱和曲线形状。

**估算方法**（Wu 2017）：基于延时比较法的次磁滞回线簇动态拟合，实测涌流最大峰值相对误差约1.6%~2%。

### 挑战4：宽频建模与仿真效率的矛盾

**问题**：配电变压器的高频暂态（雷电冲击 VFTO、开关操作）需要模型覆盖1 Hz至数MHz，但详细白盒模型导致矩阵阶数过高。

**解决路径**：紧凑化降阶（Mombello 2022：SVD低秩分解使辅助回路数从n降至$r_k$）+ 宽频参数提取（矢量拟合，Gustavsen 2020）。

## 量化性能边界

**Wu 2017 磁滞模型验证**（10 MVA YNd11变压器，15 kV/50 Hz）：
- 涌流最大峰值相对误差：1.6%~2%（vs 实测录波）
- 稳态峰值相对误差：13.3%（vs 实测录波）
- 衰减时间相对误差：9.1%~10%

**Jazebi 2015 对偶Cauer模型**（1 kVA单相变压器，1 Hz至1 MHz）：
- 等效电阻与电感计算误差：<5%（对比FEM）
- 7阶模型有效预测范围：>15 MHz
- 忽略涡流时高频阻抗幅值误差：>30%

**Mombello 2022 紧凑白盒模型**（CIGRE JWG A2/C4.52测试变压器）：
- 扩展电感矩阵维度：1278阶（原模型）
- ATP电感矩阵限制：≤40阶
- SVD降秩后：满足ATP限制要求

**Chandrasena 2004 GIC低频模型**（3 kVA，115 V/2300 V单相，M4硅钢片）：
- 额定工况励磁电流RMS仿真误差：1.98%
- 1.1 p.u.电压下励磁电流最大误差：5.38%（vs 传统电阻模型11.25%）

**González 2014 固态变压器SST建模**（50 Hz配电网，10 kHz开关频率）：
- 负载不平衡扰动传播至一次侧电流畸变率：<1%
- 电压波动：<0.5%

**数据缺口声明**：配电变压器的EMT建模性能数据主要来自小容量单相样机（1-10 kVA），实际配电网中数百kVA至数MVA三相配电变压器的宽频建模精度和仿真加速比缺乏系统报告。GIC铁芯模型和FPGA加速分别在低频和硬件维度提供了有益参考，但配电变压器在分布式电源大量接入场景下的谐波/暂态仿真精度尚待系统验证。

## 适用边界与选择指南

| 应用场景 | 推荐模型 | 步长要求 | 参数来源 | 精度 |
|---------|---------|---------|---------|------|
| 工频稳态分析 | 线性集总模型 | >1 ms | 出厂报告 | 低 |
| 负载变化暂态 | 非线性饱和模型 | 0.1-1 ms | 短路试验 | 中 |
| 励磁涌流仿真 | 磁滞回线详细模型 | 10-100 μs | 励磁曲线试验 | 高 |
| 铁磁谐振分析 | JA动态磁滞模型 | 1-10 μs | JA参数辨识 | 高 |
| 雷电/开关暂态 | 白盒宽频模型 | 0.1-1 μs | FEM几何参数 | 最高 |
| SST系统级仿真 | SST多端口等效 | 1-10 μs | 模块测试 | 中 |

## 相关模型

- [[transformer-model]] - 变压器通用模型
- [[converter-transformer-model]] - 换流变压器
- [[solid-state-transformer]] - 固态变压器（SST）
- [[load-model]] - 负荷模型
- [[symmetrical-components]] - 对称分量法

## 相关方法

- [[frequency-dependent-modeling]] - 频率相关建模
- [[nodal-analysis]] - 节点分析
- [[vector-fitting]] - 矢量拟合
- [[real-time-simulation]] - 实时仿真

## 相关主题

- [[real-time-simulation]] - 实时仿真
- [[frequency-dependent-modeling]] - 宽频建模
- [[ferroresonance]] - 铁磁谐振
- [[power-quality]] - 电能质量
- [[harmonic-analysis-methods]] - 谐波分析

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| [[a-transformer-model-with-hysteresis-characteristics-for-electromagnetic-transien]] | 2017 | PSCAD/EMTDC磁滞特性变压器模型，分段线性插值次磁滞回线簇，可变电感法 |
| [[duality-based-transformer-model-including-13&14]] | 2015 | 对偶原理Cauer等效电路，频变参数解析，宽频1 Hz至15 MHz覆盖 |
| [[new-compact-white-box-transformer-model-for-the-calculation-of-electromagnetic-t]] | 2022 | SVD低秩紧凑化，ATP电感矩阵阶数限制突破 |
| [[saturable-reactor-hysteresis-model-based-on-jilesatherton-formulation-for-ferror]] | 2018 | JA磁滞模型ψ-i形式，电压驱动动态损耗，铁磁谐振研究 |
| [[emtp-model-of-a-bidirectional-multilevel-solid-state-transformer-for-distributio]] | 2014 | MV/LV双向SST三阶段功率变换架构，NPC+DAB+PWM四桥臂 |
| [[saturation-in-transient-and-stability-phenomena-for-cylindrical-13&14]] | 2012 | 考虑饱和的Park模型，d/q轴饱和电抗，x'_q暂态效应 |
| [[accelerated-electromagnetic-transient-emt-equivalent-model-of-solid-state-transf]] | 2022 | SST高频链路DAB模块加速EMT等效，节点导纳预处理+Kron消元 |

---