---
title: "地下电缆建模 (Underground Cable Modeling)"
type: method
tags: [underground-cable, cable, modeling, emt, distribution]
created: "2026-05-02"
updated: "2026-05-19"
---

# 地下电缆建模 (Underground Cable Modeling)

## 定义与边界

地下电缆建模是在 EMT 中把导体、绝缘、金属护套、铠装、外护套、土壤和接地连接共同表示为可求解电路或端口模型的方法。它关注电缆端口电压、电流、护套电压、护套电流、传播延时、频变损耗和过电压响应，而不是单纯的稳态载流量或土建敷设设计。

本页讨论电缆作为 EMT 线路/网络元件的建模。热稳定、老化、敷设经济性和标准试验只在它们改变电气参数或验证边界时出现。海底埋设电缆、交叉互联和接地网属于相邻问题，应分别与 [[cross-bonded-cable]]（护套交叉互联）、[[grounding-system-modeling]]（接地系统建模）和 [[earth-return-impedance]]（大地返回阻抗）连接。

**参数敏感性与边界前提**：地下电缆的单位长度参数对几何尺寸、土壤电阻率、护套连接方式和介质参数高度敏感。缺少这些输入时，建模结论只能停留在方法层面，不能给出确定的工程预测。

## EMT 中的作用

地下电缆在 EMT 中通常用于研究：

- 电缆投切、重燃、故障清除和雷电侵入波造成的导体与护套过电压
- 高电容、低波阻抗线路对开关暂态、谐振和保护动作的影响
- 单芯电缆护套接地方式对零序通道、护套感应电压和环流的影响
- 海底、城市地下和架空-电缆混合线路中的频变传播、反射和损耗
- 电缆参数模型与 [[universal-line-model]]（ULM）、[[bergeron-line-model]]（Bergeron 模型）、[[frequency-dependent-line-model]]（频变线路模型）或节点导纳型实现之间的接口

如果电缆被简化成单一工频阻抗或短段 π 等值，可能足以做低频近似，但不应默认适用于雷电、陡波或宽频谐振研究。

## 核心机制

多导体电缆频域模型从单位长度矩阵开始：

$$-\frac{\partial \mathbf{v}}{\partial x}=\mathbf{Z}'(\omega)\mathbf{i},\quad -\frac{\partial \mathbf{i}}{\partial x}=\mathbf{Y}'(\omega)\mathbf{v}$$

其中 $\mathbf{v}$ 和 $\mathbf{i}$ 可包含芯线、金属护套、铠装或回流导体的相域变量。串联阻抗可概念性分解为：

$$\mathbf{Z}'(\omega)=\mathbf{Z}_\text{core}(\omega)+\mathbf{Z}_\text{sheath}(\omega)+\mathbf{Z}_\text{mutual}(\omega)+\mathbf{Z}_\text{earth}(\omega)$$

并联导纳描述绝缘层、半导电层和外部介质的电容/损耗：

$$\mathbf{Y}'(\omega)=\mathbf{G}'(\omega)+j\omega\mathbf{C}'(\omega)$$

进入 EMT 时有两类常见接口路线。**传播函数路线**计算特征导纳 $\mathbf{Y}_c(\omega)$ 与传播矩阵 $\mathbf{H}(\omega)$，再通过延时和递归卷积形成历史电流源。**节点导纳路线**直接拟合整段电缆端口关系：

$$\begin{bmatrix}\mathbf{i}_1\\ \mathbf{i}_2\end{bmatrix}=\mathbf{Y}_n(\omega)\begin{bmatrix}\mathbf{v}_1\\ \mathbf{v}_2\end{bmatrix}$$

时域实现可把 $\mathbf{Y}_n$ 或其分解形式拟合成稳定有理函数，形成固定导纳、历史项和内部状态变量。

## EMT 建模方法

### 方法 1：集总 π/多段 PI 模型

将电缆分成 $N$ 段 RLCG 单元，每段用集中参数等效：

$$\mathbf{Z}'_\text{eq}=\frac{R_\text{eq}}{2},\quad \mathbf{Y}'_\text{eq}=j\omega\frac{C_\text{eq}}{2}$$

分段数量需满足 $\Delta x \leq v_{\min}/(10 f_{\max})$，其中 $v_{\min}$ 为最慢模态相速，$f_{\max}$ 为建模最高频率。短电缆（长度 $< 1$ km）在开关暂态研究中也可能需要 10–50 段才能避免分段误差。

**优点**：实现简单，无频变参数处理，适合初始化和低频近似
**缺点**：分段数随频率升高快速增长；不能保留宽频频变特性
**适用场景**：低频（$< 1$ kHz）稳态分析、短电缆工频暂态、EMT-机电混合接口初始化

### 方法 2：常参数行波模型（Bergeron/ULM 固定参数版）

使用固定特征阻抗 $Z_c$ 和传播延时 $\tau = d/v$，不随频率变化：

$$v(x,t)=\frac{1}{2}\left[ i_k(t-\tau)+i_{k+1}(t-\tau) \right]+\frac{1}{Z_c}\left[ e_k(t-\tau)+e_{k+1}(t-\tau) \right]$$

其中 $e_k$、$e_{k+1}$ 为历史电流源的等效电压。

**优点**：步长不受延时约束、可取较大 $\Delta t$、计算效率高
**缺点**：不表示集肤效应、邻近效应和大地返回频变；对高频暂态（上升时间 $< 1$ µs）和长电缆误差显著
**适用场景**：中低频（$< 10$ kHz）行波教学演示、粗略开关暂态、电缆集总等值

### 方法 3：频变线路模型（Vector Fitting + MoC/ULM）

通过矢量拟合将频域传播函数 $H(\omega)$ 和特征导纳 $Y_c(\omega)$ 拟合成有理函数：

$$H(s) \approx \sum_{m=1}^{M} \frac{R_m}{s-p_m}e^{-s\tau_m},\quad Y_c(s) \approx \sum_{m=1}^{M} \frac{R_m}{s-p_m}+D$$

时域中每个极点-留数项转化为一阶状态方程，通过梯形积分和递归卷积实现。传播延时 $e^{-s\tau}$ 通过 Padé 近似或递归卷积处理。

**关键参数**：拟合频带（通常 1 Hz–10 MHz）、拟合阶数（8–20 阶/模态）、频率采样密度（100–500 点/十倍频程）

**优点**：保留完整的频率相关特性和大地效应，适用于宽频过电压分析
**缺点**：有理拟合可能产生大留数/极点比导致数值不稳定；低频段最小特征值难以被拟合算法准确捕捉；无源性需额外强制
**适用场景**：HVDC 电缆、雷电暂态（0.1–10 MHz）、频变土壤条件下的海底/地下电缆

### 方法 4：节点导纳矩阵有理拟合（FLE + 幂等分解）

不依赖传播延时结构，直接对端口导纳矩阵 $Y_n(\omega)$ 做有理逼近。引入 **Folded Line Equivalent（FLE）变换** 将 $Y_n$ 分解为开路导纳 $Y_{oc}$ 和短路导纳 $Y_{sc}$ 分别拟合，避免直接拟合完整 $2n \times 2n$ 矩阵时不同特征值尺度混在一起。

对 $Y_n$ 的幂等分解进一步改善低频小特征值表征：

$$Y_n(s) = \sum_i \lambda_i M_i,\quad M_i^2 = M_i$$

各谱分量 $\lambda_i$ 分别进行有理逼近，低频小特征值不再被大特征值掩盖。

**优点**：不受延时约束、对短电缆友好、相域全耦合避免模态变换误差
**缺点**：需要 FLE 预处理的额外计算；拟合阶数和稳定性需要仔细检查
**适用场景**：短电缆（$< 500$ m）、多导体的频变耦合、短电缆与电力电子接口的多速率仿真

### 方法 5：分段拟合与 DC 校正（Partitioned Fitting + DC Correction）

针对 HVDC 电缆同时要求 DC 稳态精度和宽频暂态响应的问题，将拟合分为两阶段：

**第一阶段**（排除接近 DC 的样本，只拟合中高频段）：
$$H_\text{main}(s) = \sum_{m=1}^{M} \frac{R_m}{s-p_m}e^{-s\tau}, \quad \text{拟合频带} \in [f_\text{low}, f_\text{high}]$$

**第二阶段**（对被排除的低频误差建立低阶校正项）：
$$H_\text{dc}(s) = \sum_{k=1}^{K} \frac{R_k^{dc}}{s-p_k^{dc}}, \quad K \ll M$$

最终模型 $H = H_\text{main} + H_\text{dc}$ 兼顾 DC 响应与宽频动态，同时避免大留数/极点比导致的时域不稳定。

**优点**：解决 DC 附近拟合病态问题；保留主宽频模型结构
**缺点**：需要确定低频截止频率和校正项阶数；两阶段拟合的累积误差需验证
**适用场景**：HVDC 地下/海底电缆、需同时覆盖 DC 稳态和 0.1–100 kHz 暂态的多尺度仿真

### 方法 6：大地返回导纳建模

传统电缆建模通常忽略大地返回导纳，只处理大地返回阻抗。严格的大地返回建模需同时包含土壤的**电导电流**和**位移电流**：

$$Y'_g(\omega) = G'_g(\omega) + j\omega C'_g(\omega)$$

大地返回导纳的近似表达式（在几 MHz 以下与积分形式失配很小）：

$$Y_g \approx j\omega C'_\text{soil}(\omega) + G'_\text{soil}(\omega)$$

**量化边界**：短段（300 m–1 km）+ 高土壤电阻率（$\rho > 100$ Ωm）条件下，大地位移电流对高频暂态阻尼的影响更显著；忽略大地返回导纳会使过电压预测偏保守。

**优点**：提高短电缆高频暂态的阻尼预测精度；兼容标准电缆常数程序
**缺点**：需要额外的土壤参数（电导率、介电常数）；闭式近似的适用频带需确认
**适用场景**：高土壤电阻率地区、高频暂态分析（ $> 100$ kHz）、短段交叉互联电缆

## 形式化表达

### 多导体频域电报方程

$$\frac{\partial \mathbf{V}(x,\omega)}{\partial x} = -\mathbf{Z}'(\omega)\mathbf{I}(x,\omega),\quad \frac{\partial \mathbf{I}(x,\omega)}{\partial x} = -\mathbf{Y}'(\omega)\mathbf{V}(x,\omega)$$

### 传播常数与特征阻抗

$$\gamma(\omega) = \sqrt{\mathbf{Z}'(\omega)\mathbf{Y}'(\omega)},\quad \mathbf{Z}_c(\omega) = \mathbf{Y}_c^{-1}(\omega)\gamma(\omega)$$

### 节点导纳矩阵（端口关系）

$$\mathbf{I}(\omega) = \mathbf{Y}_n(\omega)\mathbf{V}(\omega), \quad \mathbf{Y}_n(\omega) = \mathbf{Y}_c(\omega)\frac{\mathbf{I} - e^{-\gamma d}}{e^{-\gamma d}}$$

### 有理函数时域实现（一阶伴随电路）

$$\frac{d\mathbf{x}}{dt} = A\mathbf{x} + B\mathbf{v}_{port},\quad \mathbf{i}_{port} = C\mathbf{x} + D\mathbf{v}_{port}$$

### 大地返回导纳对阻尼的影响

$$V_\text{overshoot} \propto \frac{1}{\sqrt{1+\omega^2 C'_g R_\text{soil}}}, \quad \text{忽略} C'_g \Rightarrow V_\text{预测} > V_\text{实际}$$

## 关键技术挑战

### 挑战 1：大地返回参数的严格确定

地下电缆快暂态（上升时间低至 0.2 µs）仿真的精度**前提是严格确定大地返回参数**（阻抗和导纳）。传统 EMT 程序假设外部介质中至少一个为无损，难以直接处理海水和海床均有损的海底电缆。需用准 TEM 全波近似或 Method of Moments 编码计算双有损介质的单位长度参数。

### 挑战 2：短电缆的步长约束

Method of Characteristics（MoC）要求 $\Delta t < \tau_\text{min}$（最快模态传播延时），短电缆迫使极小步长。解决路线：① 使用节点导纳矩阵代替 MoC，解除步长约束；② 使用多段 PI 等值放宽步长但牺牲频变精度；③ 使用分段 DC 校正的两阶段拟合，在精度和效率间折中。

### 挑战 3：低频小特征值的可观测性

直接对 $Y_n(\omega)$ 做有理拟合时，低频段最小特征值（量级 $10^{-6}$ S）在整体矩阵中被大特征值掩盖，拟合算法难以准确捕捉。幂等分解和 FLE 变换是解决此问题的两条主要技术路线。

### 挑战 4：无源性强制与数值稳定性

有理拟合得到的极点可能产生正实部（违反无源性），导致时域仿真发散。处理方法：① 迹参数无源性校正（Truncated Real Part）；② 正实引线（Positive Real Lemma）；③ 二次规划无源性优化。验证方法：检查 $Y_n(j\omega)$ 的实部对所有 $\omega$ 非负。

### 挑战 5：海底双有损介质的参数计算

海底电缆外部返回路径同时经过海床和海水，普通电缆参数例程不能覆盖该边界。准 TEM 近似需要：(1) 海水和海床分别具有复介电常数 $(\varepsilon_r, \sigma)$；(2) 计算外部单位长度阻抗和导纳时需对两层介质同时处理；(3) 埋设深度 $> 1$ m 时可忽略海水-海床-空气三层模型。

### 挑战 6：电缆附件的宽频参数缺失

电缆附件（接头、护套保护器、局部接地箱）的宽频参数往往比主电缆段更缺少可复核数据。这些附件通常比主电缆段短 1–3 个数量级，但其寄生参数在高频下（ $> 1$ MHz）可能主导响应。

## 量化性能边界

| 建模方法 | 适用频率 | 步长约束 | 精度边界 | 主要局限 |
|---------|---------|---------|---------|---------|
| 集总 π | $< 1$ kHz | 无约束 | 低频近似，$f > 1$ kHz 误差 $> 10\%$ | 无频变特性，分段数随频率增长 |
| 常参数行波 | $< 10$ kHz | $\Delta t \approx \tau$ | 保留工频行波，高频缺失 | 无集肤/邻近效应 |
| 频变线路（VF+MoC） | 1 Hz–10 MHz | $\Delta t < \tau_\text{min}$ | 宽频精度，误差 $< 2\%$（原文未报告核验数值） | 留数/极点比大则不稳定；低频特征值难捕捉 |
| 节点导纳 FLE | DC–5 MHz | 无步长约束 | 短电缆精度优于 MoC | FLE 预处理计算量；拟合阶数敏感性 |
| 分段 DC 校正 | DC–1 MHz | 无严格约束 | DC 稳态与宽频暂态兼顾 | 两阶段拟合误差累积 |
| 大地导纳模型 | $> 100$ kHz | 无约束 | 短段阻尼预测更准确 | 需土壤参数，闭式近似频带受限 |

**加速比参考**：节点导纳 FLE 方法相对于 MoC 的优势在于**不要求步长小于最快模态延时**，对短电缆可取 $\Delta t = 10$–$100$ µs 而非 $< 1$ µs，理论计算效率提升 10–100×（原文未报告核验数值）。

**验证边界**：Duarte 2023 确认传输线理论对地下电缆快暂态（上升时间 $0.2$ µs）有效，前提是大地返回参数严格确定；Camara 2024 确认 MoC/ULM 和 FLE 两种路线的时间响应均与 Numerical Laplace Transform 一致（excellent agreement）；275 kV POF 电缆（3.384 km）通过现场投切、故障和雷击暂态测量验证。

## 适用边界与选择指南

**选择决策表**：

| 场景 | 推荐方法 | 不推荐 |
|------|---------|--------|
| 短电缆（$< 500$ m）+ 宽频仿真 | 节点导纳 FLE / 幂等分解 | 常参数行波、MoC |
| 长电缆（$> 1$ km）+ 高精度 | 频变线路（VF+ULM）+ 无源性处理 | 集总 π |
| HVDC 电缆（需 DC 稳态） | 分段 DC 校正 | 普通宽频拟合 |
| 高土壤电阻率地区 | 大地返回导纳建模 | 忽略大地导纳的模型 |
| 海底埋设电缆 | 准 TEM 双有损介质参数 + MoC/ULM 或 FLE | 假设单有损介质 |
| 短电缆 + 电力电子接口 | 节点导纳 FLE + 多速率变步长 | MoC（步长约束过严） |
| 初始化 / 工频分析 | 集总 π 或常参数行波 | 频变线路（计算成本不必要） |

**失效判断**：当电缆长度满足 $d < 0.05 \lambda_\min$（$\lambda_\min$ 为最高频率对应的波长）时，行波效应可忽略，应使用集总模型而非分布参数模型；当土壤电阻率 $> 500$ Ωm 且频率 $> 1$ MHz 时，大地返回导纳对阻尼的影响不可忽略。

## 与相关页面的关系

- [[cable-model]] 是电缆作为**模型对象**的页面，本页是**方法组织**
- [[cross-bonded-cable]] 处理单芯电缆护套交叉互联和接地箱连接
- [[grounding-system-modeling]] 与 [[ground-potential-rise]] 处理接地系统和地电位升
- [[earth-return-impedance]]（大地返回阻抗）、[[frequency-dependent-soil]] 和 [[frequency-dependent-soil-model]] 决定外部回流路径参数
- [[universal-line-model]]（ULM）是频变线路模型的代表性实现
- [[lightning-transient-analysis]]（雷电暂态分析）、[[high-frequency-transient-analysis]]（高频暂态分析）和 [[insulation-coordination]]（绝缘配合）使用电缆模型评估过电压和保护裕度
- [[earth-return-impedance]] 中的大地返回阻抗公式是地下电缆 EMT 建模的外部介质参数来源

## 开放问题

- 电缆附件、接头、护层保护器和局部接地箱的宽频参数往往比主电缆段更缺少可复核数据
- 多段电缆-架空线混合线路中的拟合频带、延时插值和过电压保护设备模型需要共同验证
- 频变土壤、海底介质和护套连接的不确定性应通过敏感性分析或现场测量约束，而不是用单一典型参数代替

## 来源论文

- [[multi-scale-formulation-of-admittance-based-modeling-of-cables]] — 节点导纳矩阵 FLE 建模 + 变步长历史项重初始化，适用于短电缆和 EMT-机电多尺度接口
- [[partitioned-fitting-and-dc-correction-in-transmission-linecable-models-for-wideb]] — 两阶段拟合分区 + DC 校正项，适用于 HVDC 电缆同时覆盖 DC 稳态和宽频暂态
- [[time-domain-modeling-of-a-subsea-buried-cable]] — 海水+海床双有损介质参数计算，MoC/ULM 和 FLE 两条时域路线，海底埋设电缆专用
- [[admittance-based-modelling-of-cables-and-overhead-lines-by-idempotent-decomposit]] — 节点导纳幂等分解，低频小特征值解耦可观测性，全耦合相域导纳模型
- [[advanced-wideband-linecable-modeling-for-transient-studies]] — ULM 三项改进（最小相位时延、自适应模式合并、快速衰减模态截断），96 根电缆 + 250 m 混合线路验证
- [[earth-return-admittance-impact-on-crossbonded-underground-cables]] — 大地返回导纳对短段交叉互联电缆阻尼的影响，高土壤电阻率条件下影响更显著
- [[multi-conductor-cable-modeling-with-inclusion-of-measured-coaxial-wave-propagati]] — 实测同轴模态校正高频多导体模型，适用于金属护套单端接地和交叉互联
- [[modal-propagation-characteristics-and-transient-analysis-of-multiconductor-cable]] — Longmire-Smith 频变土壤 + 广义大地公式，平排/垂直/trefoil 三种布置敏感性比较
- [[frequency-and-transient-responses-of-a-275-kv-pressure-oil-filled-cable-model-va]] — LCD（MoM-SO）计算 275 kV POF 电缆参数，护套间/护套-钢管模态，Kron 降阶，3.384 km 现场测量验证
- Duarte 2023（EMT_Doc/09）— 传输线理论验证：快暂态（0.2 µs 上升时间）有效的前提是严格确定大地返回参数，土壤电阻率 100–1000 Ωm，flat 和 trefoil 布置