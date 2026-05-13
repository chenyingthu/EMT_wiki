---
title: "Jiles-Atherton 磁滞模型"
type: method
tags: [jiles-atherton, hysteresis, transformer, magnetic-saturation, ferromagnetic, emtp, ferroresonance]
created: "2026-05-10"
updated: "2026-05-14"
---

# Jiles-Atherton 磁滞模型

## 定义

Jiles-Atherton（JA）磁滞模型是一种基于磁畴物理的铁磁材料磁滞回线解析模型，由 D.C. Jiles 和 D.L. Atherton 于 1984 年首次提出。该模型通过描述磁畴相互作用和磁畴壁运动，以微分方程形式刻画磁化强度 $M$ 对磁场强度 $H$ 的非线性、历史依赖关系。与分段线性或单值励磁曲线不同，JA 模型能够自然生成主磁滞回线、次磁滞回线以及磁化记忆效应，对铁磁谐振、励磁涌流、直流偏磁等磁滞敏感暂态问题至关重要。

JA 模型的核心物理假设是：总磁化由不可逆磁化 $M_{\text{irr}}$ 和可逆磁化 $M_{\text{rev}}$ 两部分组成，其中不可逆磁化由磁畴壁克服钉扎势垒后的不可逆跳跃主导，可逆磁化由磁畴壁在小范围可逆位移产生。有效磁场 $H_e = H + \alpha M$ 在外部磁场基础上加入了磁畴间平均耦合场，从而解释了磁滞回线的"滞后"特性。

在 EMT 仿真中，JA 模型通常以磁链-电流（$\psi$-$i$）形式实现，通过几何关系 $\psi = NAB = NA\mu_0(H + M)$ 将磁学变量转换为电路接口量，使模型对外表现为一个具有历史相关 $\psi$-$i$ 特性的非线性支路。

## EMT 中的角色

常规 EMT 变压器/电抗器模型通常使用单值饱和曲线，无法反映磁化历史。JA 模型在 EMT 中的价值体现在四个关键场景：

**铁磁谐振**：铁磁谐振需要非线性电感、电容、低损耗和电源四个条件同时满足。铁芯主磁滞回线和次磁滞回线的轨迹会显著改变可能的谐振运行点数量与位置，单值饱和曲线可能丢失关键的暂态路径。Sima 等（2018）明确指出， anhysteretic 近似在动态、非正弦和铁磁谐振研究中是不充分的。

**励磁涌流**：换流变压器空载合闸时，非线性铁心在不同初始磁通、剩磁和饱和状态下产生含非周期分量与高次谐波的涌流。Wu 等（2017）对比了磁滞回线与磁滞中线两种励磁特性表示，发现两者在涌流峰值上一致，但磁滞回线对稳态过程特别是三次及高次谐波特性有显著影响。

**直流偏磁**：变压器因地磁感应电流或 HVDC 单极运行导致的偏磁饱和，表现为磁化曲线沿单半周偏移，JA 模型能自然追踪这种偏磁路径的演化。

**动态铁损**：JA 模型将铁损（涡流损耗 + 剩余损耗）与电压激励耦合，而非仅并联固定电阻。Sima 等指出，恒定或非线性电阻无法准确表示铁损随激励升高的动态变化——铁损实际上随激励水平增加而减小。

## 核心机制

### 磁学到电路变量的转换

JA 模型以磁学量（$B$-$H$ 或 $M$-$H$）表述，需转换为 EMT 电路接口量（$\psi$-$i$）：

$$
\psi = NAB = NA\mu_0(H + M), \quad i = \frac{Hl}{N}, \quad v = \frac{d\psi}{dt}
$$

其中 $N$ 为绕组匝数，$A$ 为铁芯截面积，$l$ 为磁路平均长度，$\mu_0$ 为真空磁导率。这样 JA 模型对外表现为一个具有历史相关 $\psi$-$i$ 特性的非线性支路，可直接嵌入节点电压-支路电流框架的 EMT 求解器中。

动态电感由磁链对电流的导数给出：

$$
L_{\text{dyn}} = \frac{d\psi}{di} = NA\mu_0\left(1 + \frac{dM}{dH}\right)\frac{N}{l}
$$

该动态电感在每个时间步长内更新，驱动"电流采样—磁链计算—电感更新—电路求解"的闭环。

### JA 微分方程体系

JA 模型由三个核心方程组成：

**有效磁场**：

$$
H_e = H + \alpha M
$$

其中 $\alpha$ 为磁畴间耦合系数（无量纲，典型值 0~0.1），表征磁畴间的平均相互作用场。

**无磁滞磁化曲线（Anhysteretic Magnetization Curve, AMC）**：

经典 Langevin 函数形式：

$$
M_{\text{an}} = M_s \left[ \coth\left(\frac{H_e}{a}\right) - \frac{a}{H_e} \right]
$$

其中 $M_s$ 为饱和磁化强度（A/m），$a$ 为无磁滞形状因子（与温度和相关）。该函数描述了在无磁滞理想条件下，磁化强度随有效磁场的单调变化关系。

对于某些铁磁材料，Langevin 函数无法准确拟合 AMC 形状，可采用修正的有理函数形式（Sima 等, 2018）：

$$
M_{\text{an}} = M_s \frac{a_1 H_e + H_e^2}{a_3 + a_2 H_e + H_e^2}
$$

其中 $a_1$、$a_2$、$a_3$ 为修正系数，通过实验 B-H 数据拟合获得，提供更灵活的 AMC 形状控制。

**磁化微分方程**：

JA 模型将总磁化分解为不可逆和可逆两部分：$M = M_{\text{irr}} + M_{\text{rev}}$，其中 $M_{\text{rev}} = c(M_{\text{an}} - M_{\text{irr}})$，$c$ 为可逆磁化权重因子（$0 < c < 1$）。由此导出磁化对磁场的导数：

$$
\frac{dM}{dH} = \frac{M_{\text{an}} - M + \frac{k\delta c}{1-c}\frac{dM_{\text{an}}}{dH_e}}{\alpha(M - M_{\text{an}}) + \frac{k\delta}{1-c}\left(1 - \alpha c \frac{dM_{\text{an}}}{dH_e}\right)}
$$

其中 $k$ 为矫顽场幅度参数（A/m），与磁滞回线宽度直接相关；$\delta = \text{sign}(dH/dt)$ 为方向参数（$dH/dt > 0$ 时取 +1，$dH/dt < 0$ 时取 -1），决定当前处于增磁还是退磁路径。该方程是 JA 模型的核心，决定了每个时间步磁链随电流变化的轨迹。

**能量平衡方程**：

JA 模型还满足能量守恒关系（Sima 等, 2018）：

$$
\mu_0 \int M_{\text{an}} \, dH_e = \mu_0 \int M \, dH_e + \mu_0 k\delta \int dM_{\text{irr}}
$$

该方程描述了施加磁场能量与磁化能量及磁滞损耗能量的关系，是 JA 模型物理自洽性的基础。

### JA 模型参数体系

| 参数 | 符号 | 物理意义 | 典型范围 | 获取方式 |
|------|------|----------|----------|----------|
| 饱和磁化强度 | $M_s$ | 材料最大磁化能力 | $10^6$~$10^6$ A/m | B-H 回线拟合 |
| 无磁滞形状因子 | $a$ | AMC 斜率控制 | 10~1000 A/m | B-H 回线拟合 |
| 磁畴间耦合系数 | $\alpha$ | 畴间平均相互作用 | 0~0.1 | 经验值或拟合 |
| 矫顽场幅度 | $k$ | 磁滞回线宽度 | 100~1000 A/m | B-H 回线拟合 |
| 可逆磁化权重 | $c$ | 可逆磁化比例 | 0~1 | B-H 回线拟合 |
| 修正系数 | $a_1, a_2, a_3$ | AMC 有理函数系数 | 由拟合确定 | 实验数据拟合 |

参数识别通常通过实验获得的环形铁芯 B-H 回线数据，使用优化算法（如遗传算法、粒子群优化）拟合得到。Sima 等（2018）指出，JA 参数识别仅需少量测量数据即可提取五个核心参数。

### 动态损耗耦合

静态 JA 模型给出 $\psi$-$i$ 磁滞关系后，还需加入电压驱动的动态损耗（涡流损耗和剩余损耗）。Sima 等（2018）提出了两种动态模型实现方案：

**动态 Model 1**：将涡流损耗和剩余损耗作为磁链变化率的函数，通过 Type-94 元件以受控源形式串联到电抗器端口：

$$
v = \frac{d\psi}{dt} + R_{\text{eddy}}\left(\frac{d\psi}{dt}\right) + R_{\text{excess}}\left(\frac{d\psi}{dt}\right)
$$

**动态 Model 2**：采用不同的损耗耦合拓扑，将损耗等效为并联支路。

Sima 等通过 50 Hz 和 150 Hz 电流测试验证，动态 Model 1 比 Model 2 更接近实验测量结果。Model 1 的优势在于损耗项直接作用于端口电压，更准确地反映了铁损随 $dB/dt$ 变化的物理机制。

### 两种 EMT 实现路径

JA 模型在 EMT 程序中有两种主要实现路径：

**路径 A：解析 JA 微分方程（Sima 等, 2018）**

在 EMTP-ATP 中，通过 Type-94 控制元件和 MODELS 语言实现 JA 微分方程的数值积分。每个时间步的执行顺序为：

1. 从当前端电压更新 $d\psi/dt$
2. 计算动态损耗电流分量
3. 根据 $dH/dt$ 方向确定 $\delta$
4. 计算 $dM_{\text{an}}/dH_e$
5. 更新 JA 微分方程求 $dM/dH$
6. 迭代求解 $\psi$-$i$ 工作点

该方法的优点是与 JA 原始理论完全对应，能自然生成主/次回线；缺点是参数辨识复杂，需要完整的 B-H 实验数据。

**路径 B：数据驱动磁滞插值（Wu 等, 2017）**

在 PSCAD/EMTDC 中，不直接求解 JA 微分方程，而是用试验获得的最大磁滞回线数据构造主回线和次回线。核心机制是：

1. 用分段线性插值拟合最大磁滞回线的上下支路和磁滞中线
2. 通过延时比较法实时采集三相电流 $I_k(t)$、$I_k(t-\Delta t)$、$I_k(t-2\Delta t)$，判断工作点运动方向
3. 以主磁滞回线上下支路为边界，利用线性插值动态计算次磁滞回线磁链：

$$
\varphi_X = \frac{\varphi_{\text{main}}(\varphi_{P1} - \varphi_N) + d_{P1}\varphi_N}{\varphi_{P1} - \varphi_N + d_{P1}}
$$

其中 $\varphi_{P1}$ 为转折点磁链，$\varphi_N$ 为磁滞中线磁链，$d_{P1}$ 为比例因子。

4. 通过可变电感法计算瞬时电感值 $L = d\varphi_X/di$，实时赋给 PSCAD 中的可变电感元件

该方法的优点是不需要完整辨识 JA 参数，仅需最大磁滞回线数据即可运行；缺点是不能自然描述材料级的磁畴物理。

## 形式化表达

### JA 模型核心方程汇总

$$
\begin{aligned}
&\text{有效磁场:} && H_e = H + \alpha M \\
&\text{无磁滞磁化:} && M_{\text{an}} = M_s \left[ \coth\left(\frac{H_e}{a}\right) - \frac{a}{H_e} \right] \\
&\text{磁化分解:} && M = M_{\text{irr}} + c(M_{\text{an}} - M_{\text{irr}}) \\
&\text{微分方程:} && \frac{dM}{dH} = \frac{M_{\text{an}} - M + \frac{k\delta c}{1-c}\frac{dM_{\text{an}}}{dH_e}}{\alpha(M - M_{\text{an}}) + \frac{k\delta}{1-c}\left(1 - \alpha c \frac{dM_{\text{an}}}{dH_e}\right)} \\
&\text{电路转换:} && \psi = NA\mu_0(H + M), \quad i = \frac{Hl}{N}, \quad v = \frac{d\psi}{dt} \\
&\text{动态电感:} && L_{\text{dyn}} = NA\mu_0\left(1 + \frac{dM}{dH}\right)\frac{N}{l} \\
&\text{能量守恒:} && \mu_0 \int M_{\text{an}} \, dH_e = \mu_0 \int M \, dH_e + \mu_0 k\delta \int dM_{\text{irr}}
\end{aligned}
$$

### 数据驱动磁滞插值方程（Wu 等）

$$
\begin{aligned}
&\text{次回线磁链:} && \varphi_X = \frac{\varphi_{\text{main}}(\varphi_{P1} - \varphi_N) + d_{P1}\varphi_N}{\varphi_{P1} - \varphi_N + d_{P1}} \\
&\text{可变电感:} && L = \frac{d\varphi_X}{di} = \frac{u}{di/dt} \\
&\text{轨迹判据:} && \begin{cases} I_k(t-\Delta t) - I_k(t-2\Delta t) < 0 \\ I_k(t) - I_k(t-\Delta t) < 0 \end{cases}
\end{aligned}
$$

### 现场磁链测量方程（Velásquez）

$$
\begin{aligned}
&\text{磁链积分:} && \psi = \psi_R + \int V_C \, dt \\
&\text{铁芯电压:} && V_C = V_{\text{Test}} - I_{\text{Test}}R_1 - L_1\frac{dI_{\text{Test}}}{dt} \\
&\text{交流稳态:} && \psi \approx \psi_R + j\frac{V_C}{\omega}
\end{aligned}
$$

## 关键技术挑战

**参数辨识**：JA 模型有 5 个核心参数（$M_s$、$a$、$\alpha$、$k$、$c$），需要实验 B-H 回线数据配合优化算法进行拟合。不同铁芯材料（硅钢片、非晶合金、纳米晶）的参数差异显著，且同一材料在不同热处理状态下的参数也不同。Wu 等（2017）指出，JA 和 Preisach 等磁滞模型参数较多、辨识复杂，工程可用性受限。

**数值刚性**：JA 微分方程在磁滞回线转折点处（$dH/dt$ 符号切换）存在不连续性，$\delta$ 参数的跳变可能导致数值求解器步长急剧缩小。Sima 等（2018）在 EMTP-ATP 中通过 Type-94 元件和自定义 MODELS 代码处理这一问题，但仿真步长仍需控制在微秒级以保证精度。

**动态损耗建模**：铁损由涡流损耗、磁滞损耗和剩余损耗三部分组成。Sima 等（2018）指出，传统方法将铁损等效为恒定或简单非线性电阻，无法反映铁损随激励电压变化的物理特性。电压驱动的动态损耗耦合是 JA 模型在 EMT 中正确预测铁磁谐振运行点的关键。

**空间分布忽略**：$\psi$-$i$ 集总模型适合 EMT 电路仿真，但无法解析铁芯内部空间磁通分布、局部饱和和热点。这些效应仍需有限元分析或实验补充。

## 量化性能边界

| 验证场景 | 数据来源 | 关键结果 |
|----------|----------|----------|
| 50 Hz 电流测试 | Sima 等 (2018) | 动态 Model 1 比 Model 2 更接近实验测量结果（原文未报告可核验的误差百分比） |
| 150 Hz 高频测试 | Sima 等 (2018) | 验证了电压驱动动态损耗项在高频下的必要性 |
| 铁磁谐振瞬态仿真 | Sima 等 (2018) | JA 磁滞模型能表示主要/次要回线，影响铁磁谐振运行点数量 |
| 10 MVA 换流变空载合闸 | Wu 等 (2017) | UD 模型与 ATP-EMTP BCTRAN 模型三相涌流峰值平均相对误差约 12%，衰减时间误差约 9.1%~10% |
| 1 kVA 小型变压器实测 | Wu 等 (2017) | UD 模型与实际试验录波的涌流最大峰值相对误差约 1.6%~2%，稳态峰值误差约 13.3% |
| 磁滞回线 vs 磁滞中线对比 | Wu 等 (2017) | 两种方法在涌流峰值上一致，但磁滞回线对稳态谐波特性影响显著 |
| 350 MVA/420 kV 现场测量 | Velásquez (2023) | 直流法仅需 50~100 V 测试电压（交流法需 1.2~1.4 p.u. ≈ 504 kV），测量时间约 5 分钟 |
| 单相低压变压器建模 | Velásquez (2023) | 实测磁滞曲线模型能准确再现励磁涌流峰值衰减和谐波含量（2次、3次谐波） |

## 适用边界与选择指南

### 方法对比

| 特性 | 解析 JA 微分方程 (Sima 等) | 数据驱动磁滞插值 (Wu 等) |
|------|--------------------------|------------------------|
| 物理基础 | 磁畴理论，完整 JA 模型 | 实验回线数据，几何插值 |
| 参数数量 | 5+ 个（需 B-H 拟合） | 最大磁滞回线数据点 |
| 实现平台 | EMTP-ATP Type-94 | PSCAD/EMTDC 自定义模型 |
| 次回线生成 | 自动（微分方程自然生成） | 分段线性插值 |
| 工程易用性 | 参数辨识复杂 | 参数易得 |
| 适用场景 | 铁磁谐振、材料级研究 | 励磁涌流、工程暂态 |

### 选择指南

- **铁磁谐振研究** → 解析 JA 微分方程（Sima 等），需要完整的主/次回线轨迹和动态损耗
- **励磁涌流分析** → 数据驱动磁滞插值（Wu 等），参数易得，工程实用
- **现场变压器建模** → 直流励磁现场测量（Velásquez），获取真实磁滞曲线
- **材料级磁滞研究** → 解析 JA 微分方程，需要磁畴物理描述
- **实时仿真/快速估算** → 磁滞中线近似（Wu 等发现涌流峰值与完整回线一致）

### 失效边界

- JA 集总 $\psi$-$i$ 模型不能解析铁芯内部空间磁通分布、局部饱和和热点
- 参数识别依赖实验 B-H 数据，材料或铁芯几何变化后需要重新辨识
- Sima 等的验证仅覆盖环形铁芯电抗器、50/150 Hz 测试和构造的铁磁谐振电路，不能直接外推到三相变压器或宽频暂态
- Wu 等的验证集中在空载合闸励磁涌流场景，未见故障暂态、直流偏磁或宽频率范围的验证
- Velásquez 的现场测量方法适用于单相和三相变压器，但积分漂移处理和参数敏感性未充分验证

## 相关方法

- [[magnetic-saturation-modeling]] — 磁饱和基本概念
- [[companion-circuit]] — 非线性支路的 EMT 离散化
- [[numerical-integration]] — 含磁滞的刚性系统积分
- Preisach 模型 — 另一种经典磁滞模型（基于积分算子，参数较多）
- [[transformer-model]] — 变压器 EMT 建模基础

## 相关模型

- [[transformer-model]] — 变压器 EMT 模型
- [[induction-machine-model]] — 感应电机模型（含铁芯饱和）
- [[converter-transformer-model]] — 换流变压器模型

## 相关主题

- [[ferroresonance]] — 铁磁谐振
- [[transformer-modeling]] — 变压器建模
- [[power-electronic-device-modeling]] — 电力电子器件建模
- [[harmonic-analysis-methods]] — 谐波分析方法

## 来源论文

- **Sima 等 (2018)** — *Saturable reactor hysteresis model based on Jiles–Atherton formulation for ferroresonance studies*. International Journal of Electrical Power & Energy Systems. 提出基于 $\psi$-$i$ 形式的 JA 磁滞电抗器模型，在 EMTP-ATP 中通过 Type-94 元件实现电压驱动动态损耗，提出两种动态耦合方案并通过 50/150 Hz 测试验证。
- **Wu 等 (2017)** — *A Transformer Model With Hysteresis Characteristics for Electromagnetic Transients Based on PSCAD/EMTDC*. 中国电机工程学报. 在 PSCAD/EMTDC 中提出基于最大磁滞回线数据插值的三相变压器磁滞模型，采用可变电感法实现闭环控制，对比了磁滞回线与磁滞中线对励磁涌流和谐波的影响。
- **Velásquez (2023)** — *On-site measurement of the hysteresis curve for improved modelling of transformers*. Electric Power Systems Research. 提出基于直流励磁原理的便携式现场测量方案，通过 T 型等效电路分离铁芯电压并积分得到磁链，在 350 MVA/420 kV 超高压变压器上验证了方法可行性。
