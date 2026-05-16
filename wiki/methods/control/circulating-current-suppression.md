---
title: "环流抑制控制 (Circulating Current Suppression Control)"
type: method
tags: [circulating-current, ccs, mmc, control, capacitor-voltage, ripple, arm-current, second-harmonic]
created: "2026-05-04"
updated: "2026-05-16"
---

# 环流抑制控制 (Circulating Current Suppression Control)

## 定义与边界

环流抑制控制（Circulating Current Suppression Control, CCS）是模块化多电平换流器（MMC）中用于抑制相间环流的附加控制策略。MMC的三相阀臂通过公共直流母线电气连接，内部桥臂电流含有直流分量和二倍频（2ω）负序环流分量，该分量在相间流动，不经过直流线路但会在桥臂中引起额外损耗和电流应力。

**边界限定**：
- 本方法适用于三相MMC换流器；单相或两相结构不存在相间环流，无需CCS
- 对于全桥子模块（FBSM）或混合子模块MMC，环流机理相同但谐波频谱更复杂
- 环流抑制是MMC高性能运行的常用辅助控制，但不是必须——低功率运行时自然环流幅值较小可不加控制

## EMT中的作用

在电磁暂态（EMT）仿真中，环流抑制控制的建模直接影响以下关键指标：

| 仿真目标 | CCS的作用 |
|---------|----------|
| **开关损耗评估** | 环流使桥臂电流峰值增加，损耗评估需考虑CCS后的电流波形 |
| **电容电压波动** | 环流是子模块电容电压二倍频波动的激励源，CCS降低该波动 |
| **直流电压质量** | 二倍频环流通过相间耦合在直流侧引起电压脉动，CCS抑制该脉动 |
| **谐波注入评估** | 环流含大量谐波分量，CCS后桥臂电流THD显著降低 |
| **实时仿真步长选择** | 含CCS的MMC模型可能需要更小步长以捕捉控制动态 |

**核心挑战**：CCS控制器通常在dq旋转坐标系下实现，与MMC桥臂电流的abc自然坐标系存在坐标变换接口；在EMT仿真中，坐标变换的同步性（PLL相位）和控制带宽直接影响等效精度。

## 形式化表达

### 1. 环流机理

定义上、下桥臂电流 $i_{\text{up},j}$ 和 $i_{\text{low},j}$（$j \in \{a,b,c\}$），则相间环流为：

$$i_{\text{circ},j} = \frac{i_{\text{up},j} + i_{\text{low},j}}{2}$$

代入桥臂电流结构 $i_{\text{up},j} = i_{\text{dc}}/3 + i_{\text{ac},j} + i_{\text{circ},j}$，可分解为：

$$i_{\text{circ},j} = \frac{i_{\text{dc}}}{3} + i_{2\omega,j}$$

其中直流分量 $i_{\text{dc}}/3$ 为各相环流的直流偏置，二倍频分量 $i_{2\omega,j}$ 由子模块电容电压二倍频波动通过桥臂电抗 $L_{\text{arm}}$ 感生得到。

**二倍频负序性质**：三相环流的二倍频分量是负序（$a$相滞后 $b$相 $120°$，$b$相滞后 $c$相 $120°$），在 $\alpha\beta$ 坐标系下表现为幅值恒定的旋转矢量：

$$i_{2\omega} = I_{2\omega}\cos(2\omega t + \phi) \quad \text{(单相)}$$

### 2. dq坐标系下的环流表示

将三相环流变换到二倍频负序旋转坐标系（转速 $2\omega$）：

$$\begin{bmatrix} i_{2d} \\ i_{2q} \end{bmatrix} = \frac{2}{3} \begin{bmatrix} \cos(2\omega t) & \cos(2\omega t - 120°) & \cos(2\omega t + 120°) \\ -\sin(2\omega t) & -\sin(2\omega t - 120°) & -\sin(2\omega t + 120°) \end{bmatrix} \begin{bmatrix} i_{\text{circ},a} \\ i_{\text{circ},b} \\ i_{\text{circ},c} \end{bmatrix}$$

稳态时 $i_{2d} = I_{2d}$、$i_{2q} = I_{2q}$ 为常量。

### 3. PR控制器

比例谐振（Proportional-Resonant, PR）控制器在指定频率处提供无穷大增益，实现零稳态误差跟踪：

$$G_{\text{PR}}(s) = K_{\text{p}} + \frac{K_{\text{r}} s}{s^2 + (2\omega)^2}$$

其中 $K_{\text{p}}$ 为比例增益，$K_{\text{r}}$ 为谐振增益。谐振项在 $s = j2\omega$ 处增益趋于无穷大，因此对二倍频信号可实现无静差跟踪。

### 4. dq解耦控制

在dq坐标系下，环流抑制控制实现d轴和q轴独立PI调节：

$$v_{\text{circ},d}^* = -\left(K_{\text{p,d}} + \frac{K_{\text{i,d}}}{s}\right)(i_{2d,\text{ref}} - i_{2d}) + 2\omega L_{\text{arm}} i_{2q}$$

$$v_{\text{circ},q}^* = -\left(K_{\text{p,q}} + \frac{K_{\text{i,q}}}{s}\right)(i_{2q,\text{ref}} - i_{2q}) - 2\omega L_{\text{arm}} i_{2d}$$

其中 $v_{\text{circ},d}^*$、$v_{\text{circ},q}^*$ 为环流抑制电压参考，$i_{2d,\text{ref}} = i_{2q,\text{ref}} = 0$（抑制所有环流交流分量）。

### 5. 桥臂环流动态方程

三相环流动态方程：

$$L_{\text{arm}} \frac{di_{\text{circ},j}}{dt} + R_{\text{arm}} i_{\text{circ},j} = v_{\text{diff},j} - \frac{1}{2}v_{\text{cap,diff},j}$$

其中 $v_{\text{diff},j}$ 为桥臂差模电压，$v_{\text{cap,diff},j}$ 为桥臂电容电压波动在差模通道中的等效电压。

### 6. 固有环流幅值

无CCS时，二倍频环流幅值近似为：

$$I_{2\omega} \approx \frac{V_{\text{dc}}}{12\omega L_{\text{arm}}}$$

该近似由电容电压二倍频波动幅值 $\Delta v_{\text{cap}} \approx I_{\text{arm}}/2\omega C_{\text{sm}}$ 代入环流动态方程得到。

### 7. 电压注入法

将环流抑制电压注入上下桥臂调制信号：

$$v_{\text{up},j}^* = v_{\text{mod},j}^* + v_{\text{circ},j}^*$$

$$v_{\text{low},j}^* = v_{\text{mod},j}^* - v_{\text{circ},j}^*$$

其中 $v_{\text{mod},j}^*$ 为基本调制电压，$v_{\text{circ},j}^*$ 为CCS附加电压（由dq坐标变换回abc坐标系）。

## EMT建模方法

### 方法1：dq坐标系状态空间法（最常用）

**原理**：在二倍频负序旋转坐标系下建立环流状态空间方程，将CCS控制器作为状态量纳入MMC完整状态空间模型。

**数学表达**：
设状态向量 $\mathbf{x}_{\text{ccs}} = [i_{2d}, i_{2q}, x_{d}, x_{q}]^{\top}$，其中 $x_{d}$、$x_{q}$ 为PI控制器的积分状态：

$$\dot{\mathbf{x}}_{\text{ccs}} = \mathbf{A}_{\text{ccs}} \mathbf{x}_{\text{ccs}} + \mathbf{B}_{\text{ccs}} \mathbf{u}_{\text{ccs}}$$

闭环系统矩阵由MMC主电路、dq坐标变换接口、PI控制器和PWM调制串联组成。

**特点**：
- 优点：与EMT求解器完全兼容，可直接联立求解
- 缺点：dq坐标变换需准确PLL相位，高频时PLL误差直接影响CCS精度

### 方法2：谐波状态空间法（精度最高）

**原理**：在谐波域建立环流方程，直接跟踪指定次数（如2次、4次）谐波的时域包络。

**数学表达**：对周期 $T = 2\pi/(2\omega)$ 的环流信号做傅里叶分解：

$$i_{\text{circ}}(t) = \sum_{h \in \mathcal{H}} I_h e^{jh2\omega t}$$

其中 $\mathcal{H} = \{0, \pm 2, \pm 4, \ldots\}$ 为谐波集合。

**特点**：
- 优点：精确捕捉各次谐波的动态，无dq坐标变换误差
- 缺点：状态量数目随谐波次数增加，适合离线分析而非实时EMT

### 方法3：阻抗分析法（适用于稳定性分析）

**原理**：将CCS控制器的开环传函 $G_{\text{PR}}(s)$ 映射为MMC输出导纳的扰动项，分析环流抑制对系统阻抗特性的影响。

**接口导纳矩阵**：
MMC输出导纳在CCS投入前为 $Y_{\text{MMC}}(s)$，投入后修正为：

$$Y_{\text{MMC,ccs}}(s) = Y_{\text{MMC}}(s) + \Delta Y_{\text{ccs}}(s)$$

其中 $\Delta Y_{\text{ccs}}(s)$ 由CCS控制器传递函数在指定频段的相位和增益修正量决定。

**特点**：
- 优点：可直接用于阻抗稳定性分析（结合广义奈奎斯特判据）
- 缺点：仅提供线性小信号视角，无法捕捉大扰动暂态

### 方法4：实时仿真降阶等效法

**原理**：在实时仿真中，用受控电流源等效CCS闭环回路，保留二倍频电流的稳态值而忽略暂态过程。

**等效接口**：
$$i_{\text{circ,eq}} = \frac{v_{\text{circ}}^*}{R_{\text{arm}} + j2\omega L_{\text{arm}}}$$

**特点**：
- 优点：计算量小，适合大系统多换流器实时仿真
- 缺点：忽略CCS动态响应，故障穿越期间误差较大

## 关键技术挑战

### 挑战1：PLL相位误差直接映射为环流抑制误差

环流抑制的dq坐标变换依赖PLL提供的相位信息。在弱电网或谐波污染环境下，PLL锁相误差（典型值 $1°$–$5°$）会在二倍频通道产生稳态误差：

$$\Delta i_{2d} = \frac{I_{2\omega}}{2}\sin(\Delta\phi_{\text{PLL}})$$

**应对策略**：采用SRF-PLL或二阶广义积分器（SOGI-PLL）提升相位精度；在高精度仿真中用解耦坐标变换替代同步SRF-PLL。

### 挑战2：控制带宽与电流内环的交互

CCS控制器带宽 $f_{\text{ccs}}$ 需远低于电流内环带宽 $f_{\text{inner}}$（典型 $f_{\text{ccs}} < 0.1 f_{\text{inner}}$），否则两者会交互激发不稳定振荡。

**验证条件**：
$$|G_{\text{PR}}(j2\omega)| < \frac{|Z_{\text{arm}}(j2\omega)|}{|H_{\text{inner}}(j2\omega)|}$$

其中 $Z_{\text{arm}}$ 为桥臂阻抗，$H_{\text{inner}}$ 为电流内环闭环传函。

### 挑战3：不对称故障时负序电流与环流耦合

电网不对称故障（单相接地、两相短路）产生负序电流分量，该分量与环流的负序特性耦合，可能导致环流抑制失控。

**耦合机理**：负序电流 $i_{\text{neg}}$ 在dq同步坐标系（$1\times\omega$）下产生直流偏置，与环流二倍频（$2\times\omega$）通道的直流偏置叠加，使PI控制器饱和。

**缓解方法**：在不对称故障期间临时切换为备选控制策略（如限幅输出或开环前馈）。

### 挑战4：PR控制器频率偏移敏感

PR控制器在基波频率 $2\omega$ 处有无穷大增益，但当电网频率偏离额定值（如 $50.2$ Hz）时，谐振峰偏移导致抑制效果下降：

$$\Delta f = f_{\text{grid}} - 50 \text{ Hz}$$

频率偏移 $0.2$ Hz 时，PR控制器在 $2\omega$ 处的增益下降约 $3$ dB（据谐振带宽公式 $\Delta f_{\text{BW}} = K_{\text{r}}/\pi$ 推算）。

### 挑战5：链路延时降低等效带宽

MMC控制链路总延时 $\tau_{\text{total}}$（采样、传输、计算、执行，约 $150$–$550$ μs）使CCS闭环等效带宽降低：

$$f_{\text{ccs,eff}} \approx \frac{0.35}{\tau_{\text{total}}}$$

当 $\tau_{\text{total}} = 300$ μs 时，等效带宽 $f_{\text{ccs,eff}} \approx 1.17$ kHz。

## 量化性能边界

### 环流抑制效果

| 指标 | 抑制前 | 抑制后 | 降幅 |
|------|--------|--------|------|
| 二倍频环流幅值 $I_{2\omega}$ | $\frac{V_{\text{dc}}}{12\omega L_{\text{arm}}}$ | $< 0.1 I_{2\omega,\text{nominal}}$ | $> 90\%$ |
| 桥臂电流THD | $15\%$–$25\%$ | $2\%$–$5\%$ | $80\%$–$87\%$ |
| 子模块电容电压波动 | $\Delta v_{\text{cap}}$（全波动） | $< 0.3\Delta v_{\text{cap}}$ | $> 70\%$ |
| 直流电压高频脉动 | $V_{\text{dc}} \times (3\%–8\%)$ | $< 1\%$ | $> 80\%$ |

### 设计参数约束

| 参数 | 约束条件 | 影响 |
|------|----------|------|
| 桥臂电感 $L_{\text{arm}}$ | $L_{\text{arm}} \uparrow \Rightarrow I_{2\omega} \downarrow$ | $L_{\text{arm}}$ 越大固有环流越小 |
| PR谐振增益 $K_{\text{r}}$ | $K_{\text{r}}$ 决定谐振峰宽度 | $K_{\text{r}}$ 过大导致频率偏移敏感 |
| CCS带宽 $f_{\text{ccs}}$ | $f_{\text{ccs}} < 0.1 f_{\text{inner}}$ | 避免与电流内环交互 |
| PLL相位精度 | $\Delta\phi_{\text{PLL}} < 1°$ 目标 | $1°$ 相位误差在 $I_{2\omega}=100$ A时产生约 $0.87$ A 误差 |

### 工程实例数据

| 工程 | 环流频率 | 抑制措施 | 效果 |
|------|----------|----------|------|
| 鲁西直流 | 1270 Hz（高频振荡） | CCS + 附加阻尼 | 振荡消除 |
| 渝鄂背靠背 | 700 Hz、1.8 kHz | CCS + PLL带宽调整 | 1.8 kHz振荡消除，700 Hz残余 |
| 厦门柔直 | 550 Hz附近 | CCS + 电压前馈滤波 | 高频振荡抑制 |

> **数据来源**：[[mmc-hvdc系统高频稳定性分析与抑制策略(一)稳定性分析]]（高频稳定性分析），[[characteristic-analysis-of-high-frequency-resonance-of-flexible-high-voltage-dir]]（阻尼控制器设计），[[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-]]（广义特征根法时滞分析）

## 适用边界与选择指南

### CCS拓扑选择

| 拓扑 | 适用场景 | 不适用场景 | 核心优点 |
|------|----------|------------|----------|
| PR控制（固定频率） | 电网频率稳定（$\Delta f < 0.2$ Hz） | 弱电网、高谐波环境 | 结构简单，参数整定直观 |
| dq-PI解耦控制 | 需要精确跟踪零参考值 | 不平衡电网（负序耦合） | dq轴独立设计，控制解耦清晰 |
| 电压注入法 | 实时仿真资源受限 | 需要高精度谐波抑制 | 计算量小，适合大系统 |
| H∞鲁棒控制 | 参数不确定性大、频率波动 | 计算资源受限 | 鲁棒性最强，系统化设计 |

### 环流与桥臂电感的定量关系

$$I_{2\omega} \propto \frac{V_{\text{dc}}}{L_{\text{arm}}}$$

当 $L_{\text{arm}}$ 从 $50$ mH 增至 $100$ mH（其他参数不变），固有环流幅值减半。因此，在环流抑制要求高的场景（大容量MMC）优先通过增大桥臂电感降低固有环流，而非依赖控制器。

### 故障穿越期间的CCS行为

| 工况 | CCS状态 | 建议 |
|------|---------|------|
| 正常工况 | 全带宽运行 | 正常参数整定 |
| 交流对称故障 | CCS保持，控制策略不变 | 确保参考值正确 |
| 交流不对称故障 | 负序耦合可能使PI饱和 | 临时降低CCS带宽或切换为前馈 |
| 直流故障 | 环流路径消失，CCS无需作用 | 闭锁CCS避免误动作 |

## 相关方法 / 相关模型

- [[mmc-model]] - MMC换流器基础模型
- [[dq-transformation]] - dq坐标变换（CCS的数学基础）
- [[harmonic-analysis-methods]] - 谐波分析（环流频谱分析工具）
- [[average-value-model]] - 平均值模型（CCS在AVM中的建模方法）
- [[submodule-model]] - 子模块模型（环流与电容电压波动的物理载体）
- [[nearest-level-control]] - 最近电平控制（CCS的调制接口）
- [[vector-control]] - 矢量控制（CCS外环控制框架）
- [[pi-controller-model]] - PI控制器模型（dq-PI解耦的组成单元）
- [[h-infinity-control]] - H∞鲁棒控制（高级CCS抑制策略）
- [[arm-reactor]] - 桥臂电抗器（环流幅值的决定因素）
- [[state-space-method]] - 状态空间法（EMT建模框架）
- [[numerical-integration]] - 数值积分（实时仿真中的CCS离散化方法）

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| [[mmc-hvdc系统高频稳定性分析与抑制策略(一)稳定性分析]] | 2021 | 建立含CCS、MMC内部动态和链路延时的状态空间模型；用参与因子和根轨迹分析高频振荡机理；指出大链路延时（550 μs）是高频失稳的关键因素 |
| [[characteristic-analysis-of-high-frequency-resonance-of-flexible-high-voltage-dir]] | 2022 | 建立含CCS的MMC dq阻抗模型；揭示延时导致"负电阻电感"特性；提出基于阻抗重塑的附加阻尼控制策略 |
| [[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-]] | 2022 | 将MMC-HVDC明确建立为时滞状态空间模型；用广义特征根法求时滞稳定裕度；设计H∞混合灵敏度控制器抑制高频振荡 |