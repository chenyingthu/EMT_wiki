---
title: "Distribution Network"
type: method
tags: [distribution-network, emt-simulation, distribution-test-feeders, microgrid-distribution-network, power-quality, lightning-overvoltage]
created: "2026-05-04"
updated: "2026-05-13"
---

# Distribution Network

## 定义

配电网（Distribution Network）是将电能从变电站分配到最终用户的中低压电力系统，通常包括10–35 kV中压（MV）配电馈线、0.4 kV低压（LV）配电网以及配电变压器。在电磁暂态（EMT）仿真语境中，配电网是包含大量电力电子接口分布式电源（DER）、非线性负荷、避雷器、接地系统和频变线路的高维度网络模型。其EMT分析关注微秒至毫秒级快速暂态过程，包括雷击感应过电压、开关操作暂态、电力电子换相暂态、谐波振荡等。

配电网EMT建模的核心方程是三相节点导纳方程：

$$\mathbf{Y}_{\text{bus}} \mathbf{V}_{\text{bus}} = \mathbf{I}_{\text{bus}}$$

其中 $\mathbf{Y}_{\text{bus}}$ 为三相节点导纳矩阵，考虑了线路耦合、变压器联结组别和中性点接地方式。与输电网不同，配电网具有三个显著特征：（1）$R/X$ 比值高（通常3–10倍于输电网），导致线路损耗和频变效应不可忽略；（2）三相严重不平衡（单相负荷占主导）；（3）分布式电源接入点多且动态特性复杂。这些特征使得 $\mathbf{Y}_{\text{bus}}$ 条件数较大（典型值 $2.9 \times 10^5$），求解时需要特殊的数值策略。

## EMT中的角色

配电网在EMT仿真体系中承担双重角色：

1. **雷电暂态研究平台**：配电网架空线路长、暴露面积大，是雷电感应过电压（LIOV）研究的主要对象。De Conti等（2025）在真实配电网中验证了频变线路损耗对低压侧感应电压的首峰误差可达28%（100 Ωm土壤）和18%（1000 Ωm土壤）。

2. **高渗透率电力电子仿真平台**：随着光伏、储能和超快充（XFC）大量接入配电网，其开关暂态和频域交互成为EMT研究热点。Debnath和Choi（2023）在含300个XFC的输配电联合系统中，验证了混合数值算法可将计算加速比提升至271倍。

配电网EMT仿真的核心挑战包括：
- **大规模网络求解**：现代配电网可达数千节点，节点导纳矩阵稀疏度从0.94（50节点）升至0.997（1000节点），但条件数仍高达 $2.9 \times 10^5$（Shukla等, 2021）。
- **频变线路损耗**：雷电波频段（0.1 Hz–10 MHz）下导体和大地损耗显著，无损假设会导致远端节点电压幅值严重高估（De Conti等, 2025）。
- **多时间尺度耦合**：从微秒级雷电流冲击到毫秒级电力电子开关，再到秒级负荷动态，要求仿真器支持多步长或多速率策略。
- **实时仿真约束**：含数百节点的配电网在1 μs步长下，传统方法实时步长可达145 μs，通过并行化可压缩至40 μs（Bruned等, 2021）。

## EMT建模方法

### 1. 节点导纳矩阵法（Nodal Analysis）

配电网EMT最基础的建模方式是节点导纳矩阵法。每个R、L、C支路经EMTP型梯形积分离散化后，等效为电导与历史电流源：

$$R_{\text{eq},L} = \frac{2L}{\Delta t}, \quad R_{\text{eq},C} = \frac{\Delta t}{2C}$$

离散化后，各支路历史电流为（电阻为0，电感为 $I_{\text{last}} + V_{\text{last}}/R_{\text{eq}}$，电容为 $I_{\text{last}} - V_{\text{last}}/R_{\text{eq}}$），系统方程简化为：

$$G_{UU} \cdot V_U = I_U$$

其中 $G_{UU}$ 为剔除已知电压源节点后的未知节点子矩阵，$I_U$ 为历史电流向量。该方法适用于所有线性配电网拓扑，是ATP、PSCAD等EMT工具的默认求解器。

**适用场景**：通用配电网EMT仿真，节点规模<1000。
**局限性**：大规模网络中直接LU分解复杂度为 $O(n^3)$，实时性受限。

### 2. 预处理共轭梯度法（PCG）

针对配电网导纳矩阵稀疏、对称正定（SPD）但高度病态的特性，Shukla等（2021）采用预处理共轭梯度法（PCG）结合Jacobi预处理子进行迭代求解。Jacobi预处理子定义为：

$$J_{ii} = \frac{1}{(G_{UU})_{ii}}$$

该预处理子通过对角缩放改善矩阵谱性质，使残差迭代更快下降。在FPGA硬件实现中，PCG的稀疏矩阵-向量乘法（SpMV）是计算瓶颈，通过5级流水线浮点乘加器和96位BRAM压缩存储（仅存储上三对角线），可实现每时钟周期1次运算的吞吐率。

**性能数据**：
- 500节点规模下PCG迭代78次收敛，单次收敛时间约8.15 ms（CPU基准）
- FPGA实现相比MATLAB软件加速12.5倍
- 浮点乘加流水线延迟3个时钟周期

**适用场景**：实时/准实时配电网EMT仿真，FPGA硬件加速平台。
**局限性**：仅适用于SPD矩阵，不适含非线性元件或不对称故障导致的非对称矩阵。

### 3. 补偿法并行解耦（Compensation Method）

当配电网缺乏自然传输线传播延迟（或延迟短于所选步长）时，Bruned等（2021）提出补偿法（CM）将网络撕裂为独立子网并行求解。核心机制是：

1. **子网独立求解**：各子网并行求解节点导纳方程 $Y_1 v_{n1} = i_1, Y_2 v_{n2} = i_2$，并提取切断节点处的戴维南电压 $v_{th1}, v_{th2}$。

2. **戴维南阻抗构建**：在各子网切断节点注入单位电流，求解 $Y_1 v_1^{(k)} = i_1^{(k)}, Y_2 v_2^{(k)} = i_2^{(k)}$，组装 $Z_{th1}, Z_{th2}$ 矩阵。

3. **补偿电流计算**：通过 $Z_C i_C = v_{th2} - v_{th1}$ 求解补偿支路电流，其中 $Z_C = Z_{th1} + Z_{th2} + Z_B$。

4. **电压修正**：最终节点电压 $v_{n}^{\text{final}} = v_{n} + v^C$，叠加补偿电流产生的电压修正量。

**性能数据**（600节点20 kV主动配电网）：
| 并行核数 | 执行时间 | 实时步长 | 加速比 |
|---------|---------|---------|--------|
| 2核 | 67 μs | 73 μs | 1.99× |
| 4核 | 38 μs | 40 μs | 3.63× |

**适用场景**：大型主动配电网实时仿真、含电力电子开关的HIL仿真。
**局限性**：补偿方程串行求解和屏障同步可能成为瓶颈；切断位置选择影响加速效果。

### 4. 混合数值离散法（Hybrid Discretization）

Debnath和Choi（2023）提出针对含大规模超快充（XFC）配电网的混合数值算法，核心思想是"按动态特性选择离散方法"：

- **刚性状态**（电感电流、滤波器电压/电流）→ 后向欧拉法（抑制数值振荡）
- **非刚性状态**（电容电压）→ 前向欧拉法（降低计算量）
- **网络线路** → 梯形法/贝杰龙模型（保留传播特性）

同时，对同一充电站内多个XFC的相似DAE方程进行聚类聚合，将全局N×N大矩阵求逆分解为聚合系统小矩阵求逆 + 各独立XFC反馈求解的两级结构。

**性能数据**：
| 场景 | XFC数量 | 加速比 | 最大误差 |
|------|--------|--------|---------|
| 单配电网 | 15 | 18× | < 5% |
| 输配电联合 | 300 | 271× | < 5% |

**适用场景**：含大量电力电子设备的配电网EMT仿真（如超快充站、光伏集群）。
**局限性**：需要精确的DAE分类和聚合规则；非线性sgn函数需引入迟滞松弛技术防失稳。

### 5. 频变线路模型（Frequency-Dependent Line Model）

配电网的频变线路建模是雷电暂态和谐波分析的关键。JMarti模型（1981）通过有理函数拟合实现频变阻抗的时域卷积：

$$\mathbf{Z}(s) = \mathbf{R}_\infty + \sum_{k=1}^{N_p} \mathbf{R}_k \frac{s}{s + p_k}$$

其中 $\mathbf{R}_\infty$ 为高频电阻矩阵，$\mathbf{R}_k, p_k$ 为极点-留数对。De Conti等（2025）在ATP中直接调用内置有理函数拟合工具，在0.1 Hz–10 MHz频段（20点/十倍频）以实极点拟合模态传播函数，参考频率 $f_0 = 60 \text{ kHz}$，避免了额外特征导纳拟合步骤。

**性能数据**：
- 地模与线模拟合误差 < 2%（高频段 > 1 MHz）
- 忽略频变损耗导致低压负荷首峰感应电压误差最大28%（100 Ωm土壤）

**适用场景**：雷电感应过电压计算、宽频谐波分析。
**局限性**：需要大量频域采样点；高频段拟合精度依赖极点数量。

### 6. 频移有理逼近（Frequency-Shifted Rational Approximation）

Kida等（2025）提出基于复矢量拟合（CVF）与频移解析信号的EMT仿真新框架。传统矢量拟合（VF）强制模型满足共轭对称性以生成实值冲激响应，而CVF解除该约束，允许极点和留数独立存在：

$$\mathbf{Y}(s) \approx \sum_{i=1}^{N_p} \frac{\mathbf{R}_i}{s - p_i} + \mathbf{D}$$

结合希尔伯特变换构造解析信号 $u_A(t) = u(t) + j\mathcal{H}\{u(t)\}$，再乘以 $\exp(-j2\pi\Delta f t)$ 实现频移，将高频激励下变频至基带（0 Hz），从而允许更大的仿真步长。

**性能数据**：
- CVF拟合误差较VF降低最高8个数量级
- 频移后精度再提升2个数量级
- 相同目标精度下，仿真步长可扩大2.33–5.5倍

**适用场景**：配电网频率相关导纳等值的基带仿真、窄带高频暂态分析。
**局限性**：CVF模型不满足Hermitian结构，无源性测试需全尺寸Hamiltonian矩阵奇异值分析；仅适合窄带或可搬移到基带的暂态成分。

### 方法对比总览

| 方法 | 适用网络规模 | 实时能力 | 加速比 | 精度 | 核心优势 |
|------|------------|---------|--------|------|---------|
| 节点导纳矩阵法 | < 1000节点 | 离线 | 1× | 高 | 通用，兼容所有EMT工具 |
| PCG迭代法 | 50–1000节点 | 准实时 | 12.5× (FPGA) | 高 | 适合SPD矩阵，硬件友好 |
| 补偿法并行 | 600+节点 | 实时 | 3.63× (4核) | 高 | 不依赖线路延迟，可任意撕裂 |
| 混合离散法 | 数百XFC | 离线 | 18–271× | < 5%误差 | 电力电子化配电网专用 |
| JMarti频变模型 | 任意 | 离线 | 1× | < 2%拟合误差 | 雷电暂态标准方法 |
| CVF频移逼近 | 任意 | 离线 | 2.33–5.5×步长 | 10⁻⁸误差 | 窄带高频仿真最优 |

## 方法体系架构

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 l10,3 l-10,3 z" fill="#333"/>
    </marker>
  </defs>
  <rect width="900" height="600" fill="#ffffff"/>
  <text x="450" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">配电网EMT仿真方法体系</text>
  <rect x="50" y="60" width="160" height="40" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="130" y="85" text-anchor="middle" font-size="12" fill="#1e40af">配电网拓扑</text>
  <rect x="50" y="120" width="160" height="40" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="130" y="145" text-anchor="middle" font-size="12" fill="#1e40af">线路/元件参数</text>
  <rect x="50" y="180" width="160" height="40" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="130" y="205" text-anchor="middle" font-size="12" fill="#1e40af">激励源 (雷电/开关)</text>
  <line x1="210" y1="80" x2="330" y2="120" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="210" y1="140" x2="330" y2="140" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="210" y1="200" x2="330" y2="160" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <rect x="340" y="100" width="200" height="80" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="440" y="125" text-anchor="middle" font-size="13" font-weight="bold" fill="#166534">节点导纳矩阵构建</text>
  <text x="440" y="145" text-anchor="middle" font-size="11" fill="#166534">Y_bus · V = I (梯形离散)</text>
  <rect x="570" y="55" width="130" height="55" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="635" y="77" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e">PCG迭代求解</text>
  <text x="635" y="93" text-anchor="middle" font-size="10" fill="#92400e">FPGA加速 12.5×</text>
  <rect x="570" y="120" width="130" height="55" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="635" y="142" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e">补偿法并行</text>
  <text x="635" y="158" text-anchor="middle" font-size="10" fill="#92400e">4核 3.63× 实时</text>
  <rect x="570" y="185" width="130" height="55" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="635" y="207" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e">混合离散法</text>
  <text x="635" y="223" text-anchor="middle" font-size="10" fill="#92400e">DAE聚合 271×</text>
  <rect x="570" y="250" width="130" height="55" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="635" y="272" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e">JMarti频变模型</text>
  <text x="635" y="288" text-anchor="middle" font-size="10" fill="#92400e">有理拟合 &lt;2%误差</text>
  <rect x="570" y="315" width="130" height="55" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="635" y="337" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e">CVF频移逼近</text>
  <text x="635" y="353" text-anchor="middle" font-size="10" fill="#92400e">步长2.33-5.5×</text>
  <rect x="570" y="380" width="130" height="55" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="635" y="402" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e">EMD电流源等效</text>
  <text x="635" y="418" text-anchor="middle" font-size="10" fill="#92400e">场路解耦 高效扫描</text>
  <line x1="540" y1="120" x2="565" y2="75" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="540" y1="135" x2="565" y2="135" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="540" y1="150" x2="565" y2="200" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="540" y1="160" x2="565" y2="265" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="540" y1="170" x2="565" y2="330" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="540" y1="180" x2="565" y2="395" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <rect x="730" y="55" width="140" height="55" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="800" y="77" text-anchor="middle" font-size="11" font-weight="bold" fill="#5b21b6">节点电压波形</text>
  <text x="800" y="93" text-anchor="middle" font-size="10" fill="#5b21b6">V(t) 时域响应</text>
  <rect x="730" y="140" width="140" height="55" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="800" y="162" text-anchor="middle" font-size="11" font-weight="bold" fill="#5b21b6">感应过电压</text>
  <text x="800" y="178" text-anchor="middle" font-size="10" fill="#5b21b6">LIOV 峰值评估</text>
  <rect x="730" y="225" width="140" height="55" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="800" y="247" text-anchor="middle" font-size="11" font-weight="bold" fill="#5b21b6">开关暂态分析</text>
  <text x="800" y="263" text-anchor="middle" font-size="10" fill="#5b21b6">谐波/振荡评估</text>
  <rect x="730" y="310" width="140" height="55" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="800" y="332" text-anchor="middle" font-size="11" font-weight="bold" fill="#5b21b6">功率质量评估</text>
  <text x="800" y="348" text-anchor="middle" font-size="10" fill="#5b21b6">不平衡/谐波指标</text>
  <rect x="730" y="395" width="140" height="55" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="800" y="417" text-anchor="middle" font-size="11" font-weight="bold" fill="#5b21b6">实时/HIL验证</text>
  <text x="800" y="433" text-anchor="middle" font-size="10" fill="#5b21b6">步长/加速比验证</text>
  <line x1="700" y1="75" x2="725" y2="75" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="700" y1="135" x2="725" y2="155" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="700" y1="200" x2="725" y2="240" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="700" y1="265" x2="725" y2="320" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="700" y1="330" x2="725" y2="395" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="700" y1="395" x2="725" y2="410" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <rect x="50" y="470" width="12" height="12" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="68" y="480" font-size="10" fill="#333">输入/源</text>
  <rect x="140" y="470" width="12" height="12" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="158" y="480" font-size="10" fill="#333">处理/模型</text>
  <rect x="240" y="470" width="12" height="12" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="258" y="480" font-size="10" fill="#333">算法/方法</text>
  <rect x="350" y="470" width="12" height="12" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="368" y="480" font-size="10" fill="#333">输出/结果</text>
  <text x="500" y="510" text-anchor="middle" font-size="11" fill="#666">关键性能：加速比 12.5× ~ 271× | 拟合误差 &lt; 2% | 雷电感应电压误差 &lt; 28% | 实时步长 40 μs</text>
  <text x="500" y="535" text-anchor="middle" font-size="10" fill="#999">来源：Shukla 2021, De Conti 2025, Bruned 2021, Debnath &amp; Choi 2023, Kida 2025</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 配电网EMT仿真方法体系架构图</p>

## 形式化表达

### 核心公式汇总

**节点导纳方程（基础）**
$$\mathbf{Y}_{\text{bus}} \mathbf{V}_{\text{bus}} = \mathbf{I}_{\text{bus}}$$

**梯形积分离散化等效电阻**
$$R_{\text{eq},L} = \frac{2L}{\Delta t}, \quad R_{\text{eq},C} = \frac{\Delta t}{2C}$$

**PCG Jacobi预处理子**
$$J_{ii} = \frac{1}{(G_{UU})_{ii}}$$

**补偿法支路电流方程**
$$Z_C i_C = v_{th2} - v_{th1}, \quad Z_C = Z_{th1} + Z_{th2} + Z_B$$

**JMarti频变阻抗有理逼近**
$$\mathbf{Z}(s) = \mathbf{R}_\infty + \sum_{k=1}^{N_p} \mathbf{R}_k \frac{s}{s + p_k}$$

**CVF导纳矩阵极点-留数形式**
$$\mathbf{Y}(s) \approx \sum_{i=1}^{N_p} \frac{\mathbf{R}_i}{s - p_i} + \mathbf{D}$$

**解析信号与频移**
$$u_A(t) = u(t) + j\mathcal{H}\{u(t)\}, \quad u_{A,sh}(t) = \exp(-j2\pi\Delta f t)u_A(t)$$

**CVF相对均方根误差**
$$Y_E = \sqrt{\frac{\sum_{m=1}^N \sum_{q=1}^N \sum_{k=1}^{N_s} |Y_{mq}(s_k) - \hat{Y}_{mq}(s_k)|^2}{N_s \sum_{m=1}^N \sum_{q=1}^N \sum_{k=1}^{N_s} |Y_{mq}(s_k)|^2}}$$

## 关键技术挑战

### 1. 大规模配电网实时求解

含数百节点的主动配电网在1 μs步长下的EMT仿真计算量巨大。Shukla等（2021）发现50–1000节点网络中，导纳矩阵条件数维持在 $2.907 \times 10^5$ 至 $2.974 \times 10^5$ 之间，呈现高度病态特性。传统直接LU分解在实时约束下难以满足步长要求。解决方案包括：FPGA硬件加速（PCG迭代，12.5倍加速）、多线程并行解耦（补偿法，3.63倍加速）、以及混合数值离散（DAE聚类聚合，最高271倍加速）。

### 2. 频变线路损耗建模

De Conti等（2025）在真实配电网中验证了频变损耗的不可忽略性：在100 Ωm土壤工况下，低压负荷首峰感应电压误差达28%；在1000 Ωm高阻土壤下误差达18%。中压线路近场区（< 100 m）受入射场主导，损耗影响较小；但远端节点和低压侧因传播距离、反射和阻抗不连续点而显著敏感。JMarti频变模型配合ATP内置有理函数拟合工具是目前最成熟的工程解决方案。

### 3. 电力电子化配电网的数值刚度

Debnath和Choi（2023）指出，含大量XFC的配电网中，电力电子开关引起的电感电流和滤波器电压/电流具有极小的时间常数（刚性状态），而储能侧电容电压变化较慢（非刚性状态）。传统梯形法对所有状态使用相同步长，导致计算效率低下。混合离散法通过刚性/非刚性分离，在保证数值稳定性的同时显著降低计算量。

### 4. 雷电感应电压的场路耦合

De Conti等（2025）提出将外部雷电电磁场对多导体线路的耦合效应完全等效为线路两端的独立电流源：

$$\mathbf{j}_0(t) = \mathbf{y}_c(t) * \bar{\mathbf{u}}_0(t), \quad \mathbf{j}_\ell(t) = \mathbf{y}_c(t) * \bar{\mathbf{u}}_\ell(t)$$

其中修正电压源通过递归方程计算：

$$\bar{\mathbf{u}}_0 = \mathbf{u}_0(t) - \mathbf{a}(t) * \bar{\mathbf{u}}_\ell(t), \quad \bar{\mathbf{u}}_\ell(t) = \mathbf{u}_\ell(t) - \mathbf{a}(t) * \bar{\mathbf{u}}_0(t)$$

这些电流源对给定雷击事件仅需离线计算一次，不随终端负载或非线性元件状态变化，大幅提升参数扫描效率。

## 量化性能边界

### 加速性能

| 方法 | 网络规模 | 加速比 | 对比基线 | 来源 |
|------|---------|--------|---------|------|
| PCG (FPGA) | 500节点 | 12.5× | MATLAB软件 | Shukla 2021 |
| 补偿法 (4核) | 600节点 | 3.63× | 串行求解 | Bruned 2021 |
| 混合离散 | 15个XFC | 18× | PSCAD梯形法 | Debnath 2023 |
| 混合离散 | 300个XFC | 271× | PSCAD梯形法 | Debnath 2023 |
| CVF频移 | 配电网等值 | 步长2.33–5.5× | VF基带仿真 | Kida 2025 |

### 精度性能

| 场景 | 误差指标 | 数值 | 来源 |
|------|---------|------|------|
| PCG FPGA | 波形误差 | 可忽略（与MATLAB一致） | Shukla 2021 |
| 混合离散 | 关键状态变量误差 | < 5% | Debnath 2023 |
| JMarti频变 | 拟合误差（> 1 MHz） | < 2% | De Conti 2025 |
| CVF频移 | 拟合误差较VF | 降低8个数量级 | Kida 2025 |

### 雷电感应过电压误差

| 工况 | 误差 | 位置 | 来源 |
|------|------|------|------|
| 100 Ωm土壤 | 首峰误差28% | 低压负荷C1-2 | De Conti 2025 |
| 1000 Ωm土壤 | 首峰误差18% | 低压负荷C2-9 | De Conti 2025 |
| 1000 Ωm土壤 | 偏差随距离非线性增长 | 远端节点P9、P11 | De Conti 2025 |

## 适用边界与选择指南

### 场景-方法推荐表

| 应用场景 | 推荐方法 | 理由 |
|---------|---------|------|
| 通用配电网稳态/暂态分析 | 节点导纳矩阵法 | 通用性强，所有EMT工具支持 |
| 实时/准实时配电网仿真 | PCG (FPGA) 或 补偿法并行 | 硬件加速突破实时约束 |
| 含大量XFC/光伏的主动配电网 | 混合离散法 | 电力电子化DAE聚类降维 |
| 雷电感应过电压计算 | JMarti频变模型 + EMD电流源等效 | 频变损耗不可忽略，场路解耦高效 |
| 窄带高频暂态分析 | CVF频移逼近 | 步长放宽2.33–5.5倍，精度提升8个数量级 |
| 含避雷器/变压器的参数扫描 | JMarti + EMD独立电流源 | 源仅需计算一次，不随非线性元件状态变化 |

### 失效边界

- **不适用于**：纯机电暂态分析（应使用 [[phasor-model]] 或 [[electromechanical-simulation]]）
- **不适用于**：配电网规划/调度等慢时间尺度问题（小时至天级）
- **PCG失效**：当网络含大量非线性元件导致导纳矩阵非对称或非正定时
- **补偿法失效**：当切断位置选择不当时，补偿方程规模过大导致串行瓶颈
- **混合离散失效**：当XFC拓扑差异大、无法有效聚类聚合时
- **CVF频移失效**：当目标现象为宽带而非窄带时，频移无法有效降低带宽

## 相关方法 / 相关模型 / 相关主题

- [[emt-simulation]] — 电磁暂态仿真基础
- [[nodal-analysis]] — 节点分析法，配电网网络方程求解核心
- [[real-time-simulation]] — 实时仿真约束下的配电网求解
- [[parallel-computing]] — 配电网并行仿真技术
- [[hil-simulation]] — 硬件在环验证
- [[fpga-real-time-simulation]] — FPGA硬件加速
- [[gpu-accelerated-simulation]] — GPU并行加速
- [[vector-fitting]] — 矢量拟合，频变线路模型基础
- [[frequency-dependent-modeling]] — 频率相关建模
- [[network-equivalent]] — 网络等值
- [[transmission-line-modeling]] — 输电/配电线路建模
- [[cable-modeling]] — 电缆建模
- [[distribution-transformer]] — 配电变压器模型
- [[surge-arrester-model]] — 避雷器模型
- [[grounding-system-model]] — 接地系统模型
- [[lightning-overvoltage]] — 雷电过电压
- [[lightning-induced-voltage]] — 雷电感应电压
- [[switching-transient]] — 开关暂态
- [[power-quality]] — 电能质量
- [[large-scale-system-simulation]] — 大规模系统仿真
- [[microgrid-distribution-network]] — 微电网与配电网
- [[power-system-network]] — 电力系统网络
- [[distribution-test-feeders]] — 配电网标准测试系统
- [[dynamic-phasor]] — 动态相量法

## 来源论文

- **Shukla et al. (2021)** — "An FPGA based electromagnetic transient analysis of power distribution network" — 提出基于SoC-FPGA的配电网EMT仿真框架，采用PCG迭代求解器实现12.5倍加速，验证了稀疏SPD矩阵的FPGA硬件加速可行性。
- **De Conti et al. (2025)** — "Calculation of lightning-induced voltages on a large-scale distribution network using the JMarti model" — 提出基于扩展模域(EMD)模型的时域计算方法，将雷电电磁场耦合等效为独立电流源注入ATP的JMarti频变线路模型，验证了频变损耗对低压侧感应电压首峰误差可达28%。
- **Bruned et al. (2021)** — "Compensation method for parallel real-time EMT studies" — 提出补偿法（CM）实现无自然线路延迟场景下的EMT并行仿真，在600节点配电网中实现3.63倍加速，实时步长从145 μs降至40 μs。
- **Debnath & Choi (2023)** — "EMT Simulation Algorithms for Evaluation of Large-Scale Extreme Fast Charging Systems" — 提出混合数值离散算法框架，联合应用数值刚度分离、时间常数分离、DAE聚类聚合和多阶积分，在300个XFC场景中实现271倍加速。
- **Kida et al. (2025)** — "Improving EMT simulations using frequency-shifted rational approximations" — 提出基于复矢量拟合(CVF)与频移解析信号的EMT仿真框架，CVF拟合误差较传统VF降低8个数量级，仿真步长可扩大2.33–5.5倍。
