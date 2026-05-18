---
title: "VSC-HVDC"
type: topic
tags: [vsc-hvdc, hvdc, flexible-dc-transmission, voltage-source-converter]
created: "2026-04-14"
---

# VSC-HVDC（柔性直流输电）



<div style="text-align:center;margin:12px 0;">
<svg viewBox="0 0 760 220" xmlns="http://www.w3.org/2000/svg">
  <text x="380" y="18" text-anchor="middle" font-size="12" font-weight="bold" fill="#333" font-family="sans-serif">VSC-HVDC 系统建模方法体系架构</text>
  
  <rect x="10" y="26" width="170" height="32" rx="3" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="95" y="40" text-anchor="middle" font-size="9" fill="#1e40af" font-weight="bold" font-family="sans-serif">器件级应力分析</text>
  <text x="95" y="52" text-anchor="middle" font-size="8" fill="#3b82f6" font-family="sans-serif">Δt=1–10μs</text>
  
  <rect x="190" y="26" width="170" height="32" rx="3" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="275" y="40" text-anchor="middle" font-size="9" fill="#1e40af" font-weight="bold" font-family="sans-serif">系统级暂态分析</text>
  <text x="275" y="52" text-anchor="middle" font-size="8" fill="#3b82f6" font-family="sans-serif">功率阶跃/故障穿越</text>
  
  <rect x="370" y="26" width="170" height="32" rx="3" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="455" y="40" text-anchor="middle" font-size="9" fill="#1e40af" font-weight="bold" font-family="sans-serif">保护与控制</text>
  <text x="455" y="52" text-anchor="middle" font-size="8" fill="#3b82f6" font-family="sans-serif">闭锁/解锁/环流</text>
  
  <rect x="550" y="26" width="170" height="32" rx="3" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="635" y="40" text-anchor="middle" font-size="9" fill="#1e40af" font-weight="bold" font-family="sans-serif">实时HIL测试</text>
  <text x="635" y="52" text-anchor="middle" font-size="8" fill="#3b82f6" font-family="sans-serif">Δt=20–50μs</text>

  <line x1="380" y1="58" x2="380" y2="68" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  
  <rect x="10" y="72" width="170" height="32" rx="3" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="95" y="86" text-anchor="middle" font-size="9" fill="#166534" font-weight="bold" font-family="sans-serif">TDM 详细开关</text>
  <text x="95" y="98" text-anchor="middle" font-size="8" fill="#22c55e" font-family="sans-serif">逐器件/最高精度</text>
  
  <rect x="190" y="72" width="170" height="32" rx="3" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="275" y="86" text-anchor="middle" font-size="9" fill="#92400e" font-weight="bold" font-family="sans-serif">DEM 详细等效</text>
  <text x="275" y="98" text-anchor="middle" font-size="8" fill="#f59e0b" font-family="sans-serif">嵌套求解/43×加速</text>
  
  <rect x="370" y="72" width="170" height="32" rx="3" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="455" y="86" text-anchor="middle" font-size="9" fill="#92400e" font-weight="bold" font-family="sans-serif">AM/EAM 加速模型</text>
  <text x="455" y="98" text-anchor="middle" font-size="8" fill="#f59e0b" font-family="sans-serif">子模块分组/14×</text>
  
  <rect x="550" y="72" width="170" height="32" rx="3" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="635" y="86" text-anchor="middle" font-size="9" fill="#166534" font-weight="bold" font-family="sans-serif">DAVM 动态平均</text>
  <text x="635" y="98" text-anchor="middle" font-size="8" fill="#22c55e" font-family="sans-serif">Δt=20–1000μs</text>

  <line x1="380" y1="104" x2="380" y2="114" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  
  <rect x="10" y="118" width="230" height="32" rx="3" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="125" y="132" text-anchor="middle" font-size="9" fill="#5b21b6" font-weight="bold" font-family="sans-serif">矢量控制 (dq坐标)</text>
  <text x="125" y="144" text-anchor="middle" font-size="8" fill="#8b5cf6" font-family="sans-serif">i_d/i_q解耦/PLL同步</text>
  
  <rect x="250" y="118" width="230" height="32" rx="3" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="365" y="132" text-anchor="middle" font-size="9" fill="#5b21b6" font-weight="bold" font-family="sans-serif">环流抑制 (CCC)</text>
  <text x="365" y="144" text-anchor="middle" font-size="8" fill="#8b5cf6" font-family="sans-serif">2n次谐波/dq域解耦</text>

  <rect x="490" y="118" width="230" height="32" rx="3" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="605" y="132" text-anchor="middle" font-size="9" fill="#5b21b6" font-weight="bold" font-family="sans-serif">直流电压控制</text>
  <text x="605" y="144" text-anchor="middle" font-size="8" fill="#8b5cf6" font-family="sans-serif">功率平衡/电容等效</text>

  <line x1="380" y1="150" x2="380" y2="160" stroke="#333" stroke-width="1.5" marker-end="url(#arr)"/>
  
  <rect x="10" y="164" width="230" height="28" rx="3" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="125" y="178" text-anchor="middle" font-size="9" fill="#991b1b" font-weight="bold" font-family="sans-serif">直流电缆/架空线</text>
  <text x="125" y="188" text-anchor="middle" font-size="8" fill="#ef4444" font-family="sans-serif">频变模型/行波</text>
  
  <rect x="250" y="164" width="230" height="28" rx="3" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="365" y="178" text-anchor="middle" font-size="9" fill="#991b1b" font-weight="bold" font-family="sans-serif">直流断路器 (DCCB)</text>
  <text x="365" y="188" text-anchor="middle" font-size="8" fill="#ef4444" font-family="sans-serif">故障隔离/耗能</text>

  <rect x="490" y="164" width="230" height="28" rx="3" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="605" y="178" text-anchor="middle" font-size="9" fill="#991b1b" font-weight="bold" font-family="sans-serif">多端互联 (MTDC)</text>
  <text x="605" y="188" text-anchor="middle" font-size="8" fill="#ef4444" font-family="sans-serif">电压分配/站间通信</text>

  <defs>
    <marker id="arr" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto">
      <polygon points="0 0, 7 2.5, 0 5" fill="#333"/>
    </marker>
  </defs>
  
  <text x="380" y="210" text-anchor="middle" font-size="8" fill="#999" font-family="sans-serif">数据来源: Beddard 2015, Gnanarathna 2011, van der Meer 2015</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · VSC-HVDC 系统建模方法体系架构</p>



## 定义与概述

VSC-HVDC（Voltage Source Converter High Voltage Direct Current）是基于电压源换流器的高压直流输电技术。它通过自关断电力电子器件和快速控制系统实现有功、无功和直流电压控制，常用于新能源并网、海上风电送出、孤岛供电、城市电网接入和多端直流系统。

在 EMT wiki 中，VSC-HVDC 是一个系统级主题：它把 [[vsc-model|VSC模型]]、[[mmc-model|MMC模型]]、直流电缆、控制器、保护和混合仿真接口连接在一起。建模目标通常不是单个器件，而是换流站、直流线路、电网交互和控制保护动作的综合暂态。

## 作用机制

VSC-HVDC 的 EMT 模型通常由以下部分组成：

$$
P_{\mathrm{ac}}\approx v_d i_d+v_q i_q,\qquad
Q_{\mathrm{ac}}\approx v_q i_d-v_d i_q
$$

在同步旋转坐标系中，VSC 控制通常通过 $i_d/i_q$ 或等价变量调节有功、无功和直流电压。EMT 模型需要说明这些控制方程如何与换流器桥臂、PLL、直流网络和保护逻辑耦合。

- **换流器主电路**：两电平、三电平或 MMC 拓扑；工程级 VSC-HVDC 多采用 MMC 或其变体。
- **交流侧接口**：变压器、滤波器、相锁环、交流电网等值和保护测量。
- **直流侧网络**：直流电缆、架空线、直流母线、电抗器、直流断路器或耗能装置。
- **控制系统**：内环电流控制、外环功率/电压控制、直流电压控制、环流控制、子模块电容电压均衡和故障控制。
- **建模层级**：详细开关模型保留开关事件；[[average-value-model|平均值模型]] 牺牲高频开关细节换取系统级效率；混合模型在不同阶段或区域切换粒度。
- **求解加速**：[[fixed-admittance|恒导纳模型]]、[[state-space-method|状态空间法]]、多速率仿真和并行计算常用于缓解大规模 MMC-HVDC 的计算压力。

## 适用边界

- 详细 EMT 模型适合直流故障、闭锁/解锁、保护动作、子模块电容电压、谐波和开关暂态分析。
- 平均值或动态相量模型适合系统级控制、稳定性扫描、机电-电磁混合仿真和大规模多端系统研究。
- 对直流故障穿越、换流器闭锁、直流断路器动作或电缆行波保护，不能只依赖平滑平均模型，应使用可覆盖故障电流路径和保护时标的模型。
- 多端 VSC-HVDC 需要明确直流电压控制分配、站间通信假设和故障隔离策略；这些控制边界会改变 EMT 结果。
- VSC-HVDC 与交流弱电网、风电场或电缆网络耦合时，应同时检查控制带宽、频率相关线路模型和接口延迟。

## 代表性来源

| 论文 | 年份 | 关联要点 |
|------|------|----------|
| [[a-vsc-hvdc-model-with-reduced-computational-intensity|A VSC-HVDC Model with Reduced Computational Intensity]] | 2012 | 降低 VSC-HVDC EMT 模型计算强度。 |
| [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid|Average-Value Models for Modular Multilevel Converters Operating in a VSC-HVDC Grid]] | 2014 | 评估 MMC 平均值模型在 VSC-HVDC 电网中的适用性。 |
| [[advanced-hybrid-transient-stability-and-emt-simulation-for-vsc-hvdc-systems|Advanced Hybrid Transient Stability and EMT Simulation for VSC-HVDC Systems]] | 2015 | VSC-HVDC 的机电-电磁混合仿真接口。 |
| [[comparison-of-detailed-modeling-techniques-for-mmc-employed-on-vsc-hvdc-schemes|Comparison of Detailed Modeling Techniques for MMC Employed on VSC-HVDC Schemes]] | 2015 | 比较 VSC-HVDC 中 MMC 详细建模技术。 |
| [[含vsc-hvdc交直流系统多尺度暂态建模与仿真研究-40|含 VSC-HVDC 交直流系统多尺度暂态建模与仿真研究]] | 2017 | 多尺度暂态建模与仿真。 |
| [[modeling-and-electromagnetic-transient-simulation-of-vsc-hvdc-system|Modeling and electromagnetic transient simulation of VSC-HVDC system]] | 2022 | VSC-HVDC 系统 EMT 建模。 |
| [[modeling-and-simulation-of-vsc-hvdc-with-dynamic-phasors|Modeling and simulation of VSC-HVDC with dynamic phasors]] | 2023 | 用动态相量模拟 VSC-HVDC。 |

## 相关方法
- [[average-value-model|平均值模型]] - MMC/VSC平均值简化
- [[state-space-method|状态空间法]] - VSC状态空间建模
- [[fixed-admittance|恒导纳模型]] - VSC恒导纳实现
- [[multirate-method|多速率方法]] - 交直流多速率仿真
- [[switching-function-method|开关函数法]] - VSC开关建模

## 相关模型
- [[vsc-model|VSC模型]] - 两电平/三电平换流器
- [[mmc-model|MMC模型]] - 模块化多电平换流器
- [[cable-model|电缆模型]] - 直流电缆建模
- [[lcc-model|LCC模型]] - 传统HVDC对比
- [[transformer-model|换流变压器]] - 换流变建模
- [[mtdc-model|MTDC模型]] - 多端直流系统

## 相关主题
- [[dynamic-phasor|动态相量法]] - VSC动态相量简化
- [[co-simulation|混合仿真]] - VSC-HVDC机电-电磁混合
- [[real-time-simulation|实时仿真]] - VSC-HVDC实时仿真
- [[frequency-dependent-modeling|频率相关建模]] - 直流电缆频变建模
- [[harmonic-analysis-methods|谐波分析]] - VSC谐波特性分析
- [[network-equivalent|网络等值]] - 交流系统等值接入

## 技术演进脉络

### 2003-2004年 (早期探索)
- **Modeling Synchronous Voltage Source Converters in Transmission System Planning Studies (2004)**
  - 💡 首次系统化整合VSC的EMTP、潮流与暂态稳定模型，建立统一建模框架
  - 提出了适用于规划研究的逐步初始化与模型简化方法
  - 开发了与详细EMTP仿真结果高度一致的暂态稳定模型

### 2010-2014年 (高效建模突破)
- **Efficient Modeling of Modular Multilevel HVDC (2010)**
  - 💡 提出导纳矩阵分区与时变戴维南等效方法，解决MMC大规模开关器件导致的EMT仿真计算瓶颈
  - 数学严格等效，不牺牲精度，大幅缩短仿真时间
- **A VSC-HVDC Model with Reduced Computational Intensity (2012)**
  - 💡 基于动态平均值建模的简化VSC模型，灵活切换全频谱/基波输出模式
  - 在保持高精度的同时显著降低电磁暂态仿真计算负担
- **Average-Value Models for MMC in VSC-HVDC Grid (2014)**
  - 💡 系统评估平均值模型在VSC-HVDC电网中的适用性边界
  - 揭示了传统AVM在直流故障工况下精度不足的缺陷，提出拓扑改进方案

### 2015-2017年 (混合仿真与多尺度建模)
- **Advanced Hybrid Transient Stability and EMT Simulation for VSC-HVDC Systems (2015)**
  - 💡 提出故障后交流系统等效阻抗重构方法，改进戴维南等效源更新协议
  - 实现高精度、高效率的VSC-HVDC混合暂态稳定与EMT协同仿真
- **含VSC-HVDC交直流系统多尺度暂态建模与仿真研究 (2017)**
  - 💡 利用希尔伯特变换进行移频分析，实现单一模型对快变电磁暂态与慢变机电暂态的统一仿真
  - 通过调整时间步长等参数显著节省仿真计算时间

### 2018-2020年 (保护与控制深化)
- **A Novel Ultra-High-Speed Traveling-Wave Protection Principle for VSC-based DC Grids (2019)**
  - 💡 将模电压行波特性与二进小波变换相结合，实现无需通信的超高速直流线路故障区段识别
  - 在多种故障条件下均表现出优异的速动性、可靠性和鲁棒性
- **A Harmonic Phasor Domain Co-Simulation Method (2020)**
  - 💡 提出谐波相量域(HPD)建模方法，实现大规模交直流电网瞬时波形与谐波相量的同步高效协同仿真
  - 准确捕捉多换流器不同开关频率引发的宽频带谐波耦合振荡
- **A Pulse-Source-Pair-Based AC/DC Interactive Simulation Approach (2020)**
  - 💡 利用脉冲源对表征与松耦合求解策略，将VSC开关事件与主网络计算解耦
  - 消除传统EMTP中因开关动作导致的矩阵重构与LU分解瓶颈

### 2021-2023年 (高频稳定性与新型建模)
- **High Frequency Stability Analysis and Suppression Strategy of MMC-HVDC Systems (2021)**
  - 💡 建立集成MMC内部动态、控制环路、锁相环及大延时环节的统一高频状态空间模型
  - 结合参与因子与根轨迹法系统揭示柔性直流系统高频振荡的内在机理
- **Modeling and Simulation of VSC-HVDC with Dynamic Phasors (2023)**
  - 💡 基于时变傅立叶级数的动态相量建模，通过保留开关函数的直流与基频分量简化高频开关过程
  - 实现仿真精度与计算效率的有效平衡
- **Fast Electromagnetic Transient Modeling Method for Half-bridge-Type VSC (2023)**
  - 💡 提出同步开关预判方法，通过逻辑判断直接获取稳定开关状态，消除传统迭代计算

### 2024-2026年 (前沿发展)
- **Initializing EMT Models of Grid Forming VSCs in MTDC Systems (2024)**
  - 💡 提出通用解耦接口(DI)初始化技术，解决黑盒构网型VSC在MTDC系统中的EMT仿真初始化难题
- **Transient Electromagnetic Power Compensation-Based Adaptive Inertia Control (2025)**
  - 💡 将暂态电磁功率补偿与自适应惯量控制相融合，解决并联储能VSC因角加速度差异导致的频率振荡问题
- **Grid-Forming Converters: Sufficient Conditions for RMS Modeling (2021+)**
  - 💡 推导外环控制增益充分条件，确保控制与网络动态时间尺度分离，RMS模型误差可控制在3%以内

## 关键发现汇总

### 建模精度与效率权衡
- **[2004]** 所开发的暂态稳定模型在动态响应上与详细EMTP仿真结果高度一致
- **[2012]** 动态平均值模型在稳态和暂态运行条件下的仿真波形与详细模型高度吻合，CPU计算时间显著降低
- **[2014]** AVM仅在子模块电容足够大以维持电压近似恒定时才有效；传统MMC平均值模型在直流故障暂态下精度严重不足
- **[2015]** 改进拓扑后的AVM在直流故障下仿真精度显著提升，计算效率大幅提高

### 混合仿真技术贡献
- **[2015]** 所提改进接口方法显著提升了交流/VSC-HVDC系统暂态稳定评估的准确性
- **[2017]** 所提模型能够准确描述VSC-HVDC系统的多尺度暂态过程，有效增强交直流系统电磁与机电暂态混合仿真的灵活性
- **[2020]** HPD协同仿真方法在保证波形精度的同时，显著提升了大规模交直流电网的仿真计算效率

### 保护与故障分析
- **[2019]** 超高速行波保护原理可作为VSC直流电网的优秀主保护方案，在多种故障条件下均表现出优异的速动性、可靠性和鲁棒性
- **[2014]** 改进模型在直流故障工况下暂态仿真精度显著提升

### 计算效率提升
- **[2015]** 时变戴维南等效模型在数学上严格等价于全节点网络模型，避免了近似接口模型带来的误差
- **[2010]** 该方法在不损失任何精度的前提下，大幅缩短了MMC系统的电磁暂态仿真时间
- **[2020]** 脉冲源对方法成功将VSC开关事件与主网络计算解耦，消除了矩阵重构与LU分解瓶颈

## 深度增强内容

### 1. VSC-HVDC系统建模方法体系

#### 1.1 详细开关模型 (Detailed Switching Model)

适用于器件级应力分析与保护整定：

**开关状态方程：**
$$
R_{sw}(t) = \begin{cases} 
R_{on} \approx 0.01\,\Omega & \text{导通状态} \\
R_{off} \approx 10^6\,\Omega & \text{关断状态}
\end{cases}
$$

**节点导纳矩阵：**
$$
Y_{bus}(t) = A \cdot \text{diag}(G_{sw}(t)) \cdot A^T
$$

**特征**：
- 时间步长：$\Delta t \in [1, 10]\,\mu\text{s}$
- 计算复杂度：$O(N^3)$ 每步
- 精度：最高，包含开关纹波与谐波

#### 1.2 动态平均值模型 (DAVM)

基于开关周期平均化，适用于系统级暂态分析：

**交流侧受控电压源：**
$$
\mathbf{v}_{abc}(t) = \frac{1}{2} m_{abc}(t) \cdot v_{dc}(t)
$$

**直流侧受控电流源：**
$$
i_{dc}(t) = \frac{3}{4} \sum_{k=a,b,c} m_k(t) \cdot i_k(t)
$$

**直接接口改进（DI-AVM）：**
- 消除传统受控源接口的一步延迟
- 允许仿真步长放宽至 $\Delta t \leq 1000\,\mu\text{s}$

#### 1.3 动态相量模型

适用于混合仿真与多尺度分析：

**移频相量变换：**
$$
x(t) = \text{Re}\left\{ \sum_{k=-K}^{K} \langle x \rangle_k(t) \cdot e^{jk\omega_0 t} \right\}
$$

**dq-SF转换矩阵：**
$$
T_{dq\rightarrow SF} = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix} \cdot e^{-j\Delta\omega t}
$$

### 2. 仿真参数参考表

| 参数类别 | 参数名称 | 典型值/范围 | 单位 | 适用场景 |
|---------|---------|------------|------|----------|
| **额定电气** | 交流额定电压 | 12.5 - 525 | kV | 取决于应用场景 |
| | 额定容量 | 10 - 1000 | MVA | 鲁西工程±350kV/1000MW |
| | 直流额定电压 | ±5 - ±800 | kV | 新能源并网通常±30-±350kV |
| | 直流电容 | 200 - 5000 | μF | 储能时间常数 τ = 0.5s |
| **开关参数** | 开关频率 | 1980 - 2000 | Hz | 两电平VSC典型值 |
| | 导通电阻 | 0.001 - 0.01 | Ω | IGBT典型值 |
| **仿真设置** | 详细模型步长 | 1 - 10 | μs | 需插值算法 |
| | AVM步长 | 20 - 100 | μs | 基频模型 |
| | DI-AVM最大步长 | 1000 | μs | 直接接口方法 |
| | 机电暂态步长 | 10 | ms | 状态空间简化模型 |

### 3. 模型选择指南

| 应用场景 | 推荐模型 | 步长建议 | 关键考量 |
|---------|---------|---------|---------|
| **器件级应力分析** | 详细开关模型 | 1-5 μs | IGBT关断过电压、二极管反向恢复 |
| **控制保护开发** | 戴维南等效模型 | 5-10 μs | 保留子模块均压、环流抑制动态 |
| **系统级暂态稳定** | DI-AVM / 状态空间 | 50-1000 μs | 直流电压动态、功率阶跃响应 |
| **机电暂态仿真** | 平均值模型 | 1-10 ms | 功角稳定、频率控制策略验证 |
| **混合仿真（AC/DC）** | 动态相量模型 | 50 μs | 多速率接口、谐波交互 |
| **实时HIL测试** | 固定导纳模型 | 20-50 μs | 固定步长、确定性延迟 |

### 4. 前沿研究方向

#### 4.1 构网型(Grid-Forming) VSC
- **虚拟同步机(VSG)等效**：建立计及虚拟惯量 $J$ 和阻尼 $D$ 的机电暂态等效模型
- **多VSG并联一致性算法**：通过功角构造性能评价函数抑制功率振荡
- **RMS模型充分条件**：推导外环控制增益充分条件，确保控制与网络动态时间尺度分离

#### 4.2 多尺度混合仿真
- **机电-电磁暂态接口**：基于移频相量(SFP)的多速率仿真，实现10ms步长与50μs步长的无缝接口
- **谐波相量域(HPD)协同**：解决VSC-HVDC中特征谐波（11次、13次）与直流网络动态的交互问题

#### 4.3 直流故障与保护
- **超高速行波保护**：利用二进小波变换(WTMM)提取故障特征，实现<1ms超高速保护
- **故障自清除能力量化**：全桥子模块比例 $\eta$ 对故障电流阻断能力的建模

#### 4.4 高效计算架构
- **GPU并行求解**：基于OpenMP/CUDA的细粒度并行，实现100+风电场秒级仿真
- **异构计算(CPU+FPGA)**：控制保护系统HIL测试，步长32.55μs支持完整保护副本运行

## 来源论文

| 论文 | 年份 |
|------|------|

| Dead-time effect modeling for hybrid modular multilevel conv | 2026 |
| Electromechanical transientelectromagnetic transient hybrid  | 2026 |
| Fast electromagnetic transient simulation models of modular  | 2026 |
| VSC-HVDC 系统的动态相量法建模仿真分析 | 2026 |
| 适用于实时仿真的MMC子模块电容电压优化均衡方法 | 2026 |
| Analysis on dynamic characteristic of control mode for +/-80 | 2025 |
| Electromagnetic Transient Modeling and Simulation of Large P | 2025 |
| Impedance Based Stability Analysis of the Multi-terminal Cas | 2025 |
| SFA-EMT hybrid simulation of power systems: Application to H | 2025 |
| Z-Tool: Frequency-domain characterization of EMT models for  | 2025 |
| 大规模交直流电网电磁暂态数模混合仿真平台构建及验证 | 2025 |
| Analytical Calculation Method of Outer Loop Controller Param | 2024 |
| Fast Loss Evaluation Method Based on MMC Average Simulation  | 2024 |
| Key Technologies and Prospects for Electromagnetic Transient | 2024 |
| Shooting method based modular multilevel converter initializ | 2024 |
| Time-domain modeling of a subsea buried cable | 2024 |
| 基于模块化多电平换流器的超级电容储能系统高效仿真方法 | 2024 |
| 新能源电力系统细粒度并行与多速率电磁暂态仿真 | 2024 |
| 考虑死区特性的全桥型MMC状态空间平均化建模方法 | 2024 |
| 非隔离型直流变压器的快速电磁暂态等效建模方法 | 2024 |
| An Enhanced Method to Achieve Exact DC Values for Frequency- | 2023 |
| An accelerated detailed equivalent model for modular multile | 2023 |
| Generalized Electromagnetic Transient Equivalent Modeling an | 2023 |
| Lessons learned in porting offline large-scale power system  | 2023 |
| Real-Time Simulation of Power System Electromagnetic Transie | 2023 |
| 交直流电力系统分割并行电磁暂态数字仿真方法 | 2023 |
| 多样性子模块混合型MMC统一外特性高效电磁暂态模型 | 2023 |
| 多类型子模块MMC电磁暂态通用建模和实现方法 | 2023 |
| 电力系统数字混合仿真技术综述及展望 | 2023 |
| A Transformer Model With Hysteresis Characteristics for Elec | 2022 |
| Average-Value Modeling of Line-Commutated Inverter Systems W | 2022 |
| Design of hybrid series converter valve considering device s | 2022 |
| Electromechanical-electromagnetic Hybrid Simulation Technolo | 2022 |
| Electromechanical-electromagnetic transient hybrid simulatio | 2022 |
| Full-state Arm Average Value Model for Simulation of Active  | 2022 |
| Modeling_of_LCC_HVDC_Systems_Using_Dynam | 2022 |
| The Averaged-value Model of a Flexible Power Electronics Bas | 2022 |
| 中  国  电  机  工  程  学  报 | 2022 |
| 大规模电力电子设备接入的电力系统混合仿真接口技术综述 | 2022 |
| 模块化多电平换流器电磁暂态模型研究综述 | 2022 |
| 模块化多电平换流器的高效电磁暂态仿真方法研究 | 2022 |
| 混合型MMC全状态高效电磁暂态仿真方法研究 | 2022 |
| 电力系统机电-电磁混合仿真边界解耦算法研究 | 2022 |
| 计及电容过渡过程的双钳位型MMC电磁暂态高效仿真方法 | 2022 |
| 高频隔离型电力电子变压器电磁暂态加速仿真方法与展望 | 2022 |
