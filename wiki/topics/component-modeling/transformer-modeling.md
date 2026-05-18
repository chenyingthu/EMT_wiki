---
title: "变压器建模 (Transformer Modeling)"
type: topic
tags: [transformer, saturation, inrush, internal-fault, winding, white-box, black-box, duality, hysteresis]
created: "2026-05-01"
updated: "2026-05-19"
---

# 变压器建模 (Transformer Modeling)

## 定义与边界

变压器建模是在 EMT 中表示绕组、电阻漏抗、磁化支路、铁芯饱和、绕组连接、分接头、频率相关效应和内部故障的建模工作。它不是单一"精确模型"问题；不同研究对象需要不同层级，例如理想变压器、饱和模型、白箱模型、黑箱频域模型或多物理场模型。

变压器模型覆盖从 **工频稳态**（漏抗、磁化电抗）到 **高频暂态**（VFTO、雷电冲击、入口电容谐振）的全频带响应。建模层级由研究目标决定，而非追求单一"最高精度"模型。

本页是 topic 页，关注变压器建模路线和证据边界。具体元件模型可阅读 [[transformer-model]]、[[multi-winding-transformer]]、[[ideal-transformer-equivalent]] 和 [[magnetic-saturation-modeling]]。

## EMT 中的作用

变压器模型影响以下 EMT 现象：

- **合闸涌流**：剩磁、饱和和铁磁谐振导致数倍额定电流的暂态冲击电流
- **内部故障与保护**：差动保护整定依赖励磁支路模型；CT/PT 暂态影响保护精度
- **高频暂态**：雷电冲击、VFTO（特快速瞬态）和绕组电压分布（500 kHz–10 MHz）
- **换流变压器接口**：HVDC、FACTS、MMC 与交流网络的电磁耦合，触发谐波交互稳定性
- **实时仿真约束**：HIL/RT-HIL 平台需要在精度和计算效率间做模型简化

## 主要分支与机制

### 低频等值模型（Ideal + Leakage）

用理想变比、漏抗和磁化支路表示工频及低频暂态，适合系统级 EMT 的基础模型。典型参数来自出厂测试报告（短路阻抗、开路损耗、空载电流）。

### 饱和与磁滞模型（Saturation & Hysteresis）

用单值磁化曲线、Jiles-Atherton、Preisach 或磁等效电路描述铁芯非线性。**参数和剩磁假设**决定涌流结论——Velásquez 2023 指出，工厂测试通常不提供真实饱和/磁滞曲线，现场测量方法才可获得 350 MVA/420/110 kV 变压器真实磁滞回线。

### 白箱模型（White-Box / Lumped-Parameter）

从绕组几何、材料和连接结构推导电感、电容和电阻矩阵，适合内部故障和高频电压分布。Mombello 2022 提出了 ATP-EMTP 环境下白箱模型的**六种化简变体**：模型降阶、磁路解耦、数值稳定性保证、电阻限用与优化、大模型处理方法，以及 ATP 特异性实现方法。

### 黑箱/频域模型（Black-Box / Frequency-Response）

从端口频响或测量数据拟合等值，适合系统级宽频仿真（DC–10 MHz）。Su 1990 提出的 Z 变换模型将变压器频率相关短路阻抗与增益函数结合，建立了频域响应到时域冲激响应的 S 平面综合方法，覆盖从 50 Hz 到数 kHz 的平坦增益区和 MHz 级谐振/反谐振峰。

### 对偶等效电路模型（Duality-Based Equivalent Circuit）

Shafieipour 2020 将对偶原理应用于多柱（3 柱和 5 柱）变压器 EMT 建模，实现了**无需内部几何信息**（无需铁芯尺寸、材料、绕组匝数）的参数化：用铭牌数据、工厂验收测试报告、芯部纵横比、空气芯电感、磁滞回线宽度和拐点电压共同确定等效电路，将铁芯非线性（饱和、磁滞、深饱和、剩磁）纳入模型。

## 形式化表达

### 基本端口方程

变压器 EMT 模型的基本端口关系：

$$
v = Ri + \frac{d\psi(i, x_m)}{dt}, \qquad i_{\mathrm{port}} = Y_{\mathrm{eq}} v_{\mathrm{port}} + i^{\mathrm{hist}}
$$

其中 $\psi(i, x_m)$ 表示含饱和、磁滞和剩磁状态的磁链，$Y_{\mathrm{eq}}$ 是离散后进入网络方程的等效导纳。

### 双绕组变压器 T 型等效电路

$$
\begin{bmatrix} V_1 \\ V_2 \end{bmatrix} = \begin{bmatrix} R_1 + jX_1 & jX_m \\ jX_m & R_2 + jX_2 \end{bmatrix} \begin{bmatrix} I_1 \\ I_2 \end{bmatrix}
$$

其中 $R_1, R_2$ 为绕组电阻，$X_1, X_2$ 为漏抗，$X_m$ 为励磁电抗。

### 对偶原理等效电路（Shafieipour 2020）

三柱芯等效：将铁芯分为 limb(w) 和 yoke(y)，分别用非线性磁滞电感和线性电阻（铁芯涡流损耗）表示。磁化支路参数由厂商提供的开路测试和短路测试数据确定，无需铁芯几何信息。

五柱芯等效：增设 outer limb(o)，outer limb 与 yoke 之间增设耦合支路。对偶原理要求磁路中相邻磁通路径满足几何对偶关系。

### Z 变换频率响应模型（Su 1990）

变压器绕组对的频率响应在宽频带内相同（50 Hz 到数 kHz 增益接近 1），高频出现谐振/反谐振。通过最小相位化处理（移除传输延迟）后，增益函数可唯一确定。S 平面综合的 3 阶加权函数可在 Z 平面实现递归卷积：

$$
H(z) = \frac{b_0 + b_1 z^{-1} + b_2 z^{-2}}{1 + a_1 z^{-1} + a_2 z^{-2}}
$$

### 饱和特性表示

反正切函数模型（工程常用）：

$$
i_\phi = a \cdot \arctan(b \phi) + c\phi
$$

多项式模型（奇次谐波分量）：

$$
i_\phi = k_1\phi + k_3\phi^3 + k_5\phi^5 + \cdots
$$

分段线性模型：

$$
L_m = \begin{cases} L_{m0} & |\phi| < \phi_{\mathrm{sat}} \\ L_{\mathrm{sat}} & |\phi| \geq \phi_{\mathrm{sat}} \end{cases}
$$

### Jiles-Atherton 磁滞模型

描述磁通密度 $B$ 与磁场强度 $H$ 的磁滞环：

$$
\frac{dB}{dH} = \frac{(1-\alpha)c + \frac{\delta_M \cdot \mathrm{sign}(\dot{H}) \cdot (1-c)\cdot (a - \alpha \cdot M_{an}) \cdot M_{an}}{k \cdot \delta_M - \mathrm{sign}(\dot{H})\cdot (M - M_{an})}}{(1-\alpha)(1+c) - \alpha \cdot (1-\alpha) \cdot \frac{M_{an} - M}{k \cdot \delta_M - \mathrm{sign}(\dot{H})(M - M_{an)})}
$$

参数含义：$a$（形状系数）、$c$（磁化强度与无磁滞曲线弹性比）、$\alpha$（Mean field 相互作用系数）、$k$（钉扎系数）、$M_{an}$（无磁滞磁化强度）。

### 合闸涌流峰值估算

无剩磁合闸涌流峰值：

$$
I_{\mathrm{inrush}} \approx \frac{\sqrt{2}V}{\sqrt{R^2 + (\omega L_{\mathrm{sat}})^2}}
$$

考虑剩磁 $\Phi_r$ 和投入相位角 $\theta$ 的磁通表达式：

$$
\Phi(t) = \Phi_m[\cos\theta - \cos(\omega t + \theta)] + \Phi_r
$$

最大磁通（当 $\theta = 0$，剩磁为正时）：

$$
\Phi_{\max} = 2\Phi_m + \Phi_r
$$

Velásquez 2023 指出：现场测量磁滞曲线比工厂测试报告估计值更准确，350 MVA/420 kV 变压器实例表明，测量曲线的拐点电压和剩磁系数与估计值偏差可达 15%–25%，直接影响涌流峰值预测精度。

### 白箱高频等效电路（用于 VFTO 分析）

Mombello 2022 将高频白箱模型分解为以下元件组合：

- **入口电容** $C_e$：绕组对地电容总和（1–10 nF，取决于电压等级）
- **饼间电容** $C_d$：绕组饼之间的电容（0.5–5 pF）
- **对地电容** $C_g$：绕组对铁芯和油箱的电容
- **分段电感** $L_k$：每饼的漏电感

电容矩阵方程（白箱模型）：

$$
\mathbf{Q} = \mathbf{C} \mathbf{V}
$$

其中 $\mathbf{C}$ 为电容矩阵（含绕组间、绕组对地电容），$\mathbf{V}$ 为节点电压向量。该矩阵通过绕组几何参数和绝缘材料介电常数确定。

### ATP-EMTP 白箱模型降阶方法（Mombello 2022）

**方法 1 — 模态叠加降阶**：将 $N$ 节分段模型在模态域解耦，保留主导模态（低频），截断高阶模态。误差控制在 5% 以内时，可将 20 节模型降为 6–8 节。

**方法 2 — 谐振频率识别与合并**：识别等效电路中的谐振频率簇，将簇内相邻谐振合并为单谐振子。适用于 VFTO 分析（关注 1–10 MHz 频段）。

**方法 3 — 电阻合并优化**：分布式电阻等效合并以减少 ATP 节点数，同时保持总损耗不变。电阻合并后需验证无源性不被破坏。

### 对偶模型参数化（Shafieipour 2020）

无需内部设计信息的输入参数集：

| 参数类型 | 参数名 | 来源 |
|---------|--------|------|
| 铭牌数据 | 额定电压、容量、连接组别 | 厂家铭牌 |
| 出厂测试 | 短路阻抗、开路损耗、空载电流 | FAT 报告 |
| 几何参数 | 芯部纵横比（$h/w$）、柱间距 | 可选，由铭牌推导 |
| 磁特性 | 空气芯电感 $L_{\mathrm{air}}$、磁滞回线宽度 $\Delta B$ | 现场测量或默认值 |
| 非线性 | 拐点电压 $V_{\mathrm{knee}}$、深饱和斜率 | 估计或测量 |

### 黑箱频域模型的矢量拟合（Vector Fitting）

频域测量数据（$H(j\omega)$）通过矢量拟合逼近：

$$
H(s) = \sum_{i=1}^{N} \frac{r_i}{s - p_i}
$$

其中 $r_i$ 为留数，$p_i$ 为极点。拟合后在时域以递归卷积实现，无需存储完整冲激响应。参见 [[vector-fitting]] 和 [[frequency-dependent-modeling]]。

## 关键技术挑战

### 挑战 1：剩磁不确定性

合闸涌流峰值对剩磁方向和大小高度敏感（$\Phi_{\max} = 2\Phi_m + \Phi_r$，$\Phi_r$ 可在 $\pm 0.8\Phi_m$ 范围）。工厂测试通常不测量剩磁，仿真中通常假设最坏情况（$\Phi_r = 0.7$–$0.8\Phi_m$）。**现场测量磁通波形**是减少此不确定性的唯一途径（Velásquez 2023）。

### 挑战 2：多柱铁芯耦合

三柱和五柱变压器铁芯中，相邻柱通过铁轭和空气隙磁通耦合。对偶模型要求正确处理零序磁通路径——Shafieipour 2020 指出，零序漏电感强制是任意多绕组变压器对偶模型的开放难题。

### 挑战 3：白箱模型参数获取

详细几何信息（绕组匝数、铁芯截面积、饼间距离）在商业变压器中通常保密。灰色箱模型（如对偶模型）通过可获取的铭牌和测试数据间接确定参数，但精度低于基于几何的白色箱模型。

### 挑战 4：数值稳定性与无源性

高频白箱模型含分布电容和电感，在 EMT 离散化后可能出现数值振荡或无源性破坏（非物理能量注入）。Mombello 2022 建议在 ATP 中使用 **伴随电路无源性检验** 并限制阻尼电阻值。

### 挑战 5：实时仿真步长约束

HIL 平台（dSPACE、RT-Lab）要求 $1$–$100\,\mu\text{s}$ 步长。详细白箱模型（$20+$ 节）在此步长下计算负担过大，需要降阶至 6–8 节，同时保留 $0$–$1\,\text{MHz}$ 频带信息。

## 量化性能边界

| 研究目标 | 推荐模型 | 频率范围 | 精度要求 | 典型加速比 |
|---------|---------|---------|---------|-----------|
| 系统潮流/工频暂态 | 理想变压器+漏抗 | 50–500 Hz | 5%–10% | — |
| 合闸涌流分析 | 饱和+Jiles-Atherton | DC–1 kHz | 10%–20% | — |
| 差动保护整定 | 饱和+谐波模型 | 50 Hz–1 kHz | 10%–15% | — |
| VFTO/雷电冲击 | 白箱多导体模型 | 100 kHz–10 MHz | 20%–30% | — |
| 内部故障定位 | 详细绕组几何模型 | DC–5 MHz | 详细几何参数 | — |
| 实时 HIL 仿真 | 降阶白箱（6–8 节） | DC–1 MHz | 15%–25% | 3–5× |
| 宽频阻抗拟合 | 矢量拟合黑箱 | 10 Hz–10 MHz | 5%–15% | — |

**Z 变换模型精度**（Su 1990）：220 kV 自耦变压器从 50 Hz 到 100 kHz 增益综合误差 $< 5\%$（S 平面 3 阶加权函数）。

**对偶模型精度**（Shafieipour 2020）：50 MVA/390 MVA 多柱变压器开路励磁电流仿真与实测对比，饱和区误差 $< 8\%$，线性区误差 $< 3\%$。

**白箱降阶精度**（Mombello 2022）：CIGRE JWG A2/C4.52 基准测试用例，6 节降阶模型与 20 节原始模型 VFTO 峰值偏差 $< 5\%$，波头时间偏差 $< 10\%$。

**现场磁滞测量价值**（Velásquez 2023）：350 MVA/420 kV 变压器，使用实测磁滞曲线后，涌流峰值预测误差从基于工厂报告估计的 25% 降至 $< 8\%$。

## 适用边界与选择指南

### 按频带选择

| 频带 | 50 Hz | 50 Hz–1 kHz | 1 kHz–500 kHz | 500 kHz–10 MHz |
|------|-------|-------------|--------------|----------------|
| 适用模型 | 理想+漏抗 | 饱和/磁滞 | T型等效+电容 | 白箱分段模型 |

### 按研究目标选择

| 研究目标 | 推荐模型 | 精度要求 |
|---------|---------|---------|
| 系统级潮流 | 理想变压器+漏抗 | 5%–10% |
| 涌流分析 | 饱和模型+剩磁测量 | 10%–20% |
| 保护整定 | 饱和+谐波模型 | 10%–15% |
| VFTO 分析 | 白箱多导体模型 | 20%–30% |
| 内部故障 | 详细绕组模型 | 详细几何参数 |
| 实时仿真 | 简化表插值模型 | 15%–25% |

### 模型边界条件

- **理想变压器或线性漏抗模型**：不能支撑饱和、涌流、内部故障和高频绕组电压结论
- **黑箱频域模型**：若未检验无源性，在 EMT 时域中可能产生非物理能量
- **内部故障和绕组电压分布**：需要结构参数，仅有端口模型通常不足
- **Z 变换模型**（Su 1990）：适用于两端绕组对分析，对多绕组（三绕组及以上）需要扩展

## 相关页面

- [[transformer-model]] — 变压器基础模型（绕组建模细节）
- [[multi-winding-transformer]] — 多绕组变压器扩展模型
- [[ideal-transformer-equivalent]] — 理想变压器等效与接口方法
- [[magnetic-saturation-modeling]] — 铁芯饱和与磁滞建模（Jiles-Atherton、Preisach）
- [[frequency-dependent-modeling]] — 频域响应建模与矢量拟合方法
- [[vector-fitting]] — 频域等效电路拟合算法
- [[differential-protection]] — 变压器差动保护与励磁涌流识别
- [[finite-element-method]] — 场路联合仿真与参数提取
- [[vsc-hvdc]] — 换流变压器在 HVDC 中的接口角色

## 来源论文

- [[a-z-transform-model-of-transformers-for-the-study-of-electromagnetic-transients-]] — Su 等 1990：Z 变换模型，结合频率相关短路阻抗与增益函数，S 平面综合，宽频带（50 Hz–100 kHz）变压器绕组建模
- [[duality-based-transformer-modeling-for-low-frequency-transients]] — 低频暂态对偶等效电路建模方法
- [[duality-based-transformer-model-including-13&14]] — 多柱变压器对偶建模应用
- [[interfacing-factor-based-white-box-transformer-modeling-method]] — 白箱模型与系统级 EMT 接口方法
- [[new-compact-white-box-transformer-model-for-the-calculation-of-electromagnetic-t]] — 紧凑白箱变压器模型计算方法
- [[a-transformer-model-with-hysteresis-characteristics-for-electromagnetic-transien]] — 磁滞特性变压器模型
- [[saturable-reactor-hysteresis-model-based-on-jilesatherton-formulation-for-ferror]] — 基于 Jiles-Atherton 的磁滞模型
- [[on-site-measurement-of-the-hysteresis-curve-for-improved-modelling-of-transforme]] — Velásquez 等 2023：现场磁滞曲线测量方法，350 MVA/420 kV 实例，涌流误差从 25% 降至 8%
- [[optimized-high-frequency-white-box-transformer-model-for-implementation-in-atp-e]] — Mombello 等 2022：ATP 白箱模型六种降阶变体，VFTO 精度 $< 5\%$