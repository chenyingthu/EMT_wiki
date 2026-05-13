---
title: "Ould Bachir 2019 Unified Avm"
type: method
tags: [ould-bachir-2019-unified-avm, average-value-model, mmc, unified-modeling]
created: "2026-05-04"
updated: "2026-05-13"
---

# Ould Bachir 2019 Unified Avm

## 定义

Ould Bachir 2019 Unified Avm 页面指向一篇关于模块化多电平换流器（MMC）**统一平均值模型**（Unified Average-Value Model, AVM）的研究工作。该页面归入 [[average-value-model]] 和 MMC 平均值建模语境，是 MMC 系统级 EMT 仿真中平均值等效方法的入口页之一。

统一平均值模型的核心思想是：将 MMC 桥臂中大量子模块（Submodule, SM）的开关动作在工频周期内取平均，用连续调制函数替代离散开关函数，从而将原本包含数百个非线性开关元件的电路拓扑，等效为交流侧受控电压源与直流侧等效电流源/电容的多端口网络。该模型保留了桥臂层级的物理可解释性（区别于黑箱 VSC 级 AVM），同时大幅降低了 EMT 仿真中的网络方程维度。

核心状态方程可表述为桥臂电流与子模块等效电容电压的耦合动态：

$$
\frac{d}{dt} \begin{bmatrix} i_{\text{arm},j} \\ v_{c,\text{eq},j} \end{bmatrix} = 
\begin{bmatrix} -\frac{R_{\text{arm}}}{L_{\text{arm}}} & -\frac{m_j(t)}{L_{\text{arm}}} \\ \frac{m_j(t)}{C_{\text{eq}}} & -\frac{1}{R_{\text{loss}}C_{\text{eq}}} \end{bmatrix} 
\begin{bmatrix} i_{\text{arm},j} \\ v_{c,\text{eq},j} \end{bmatrix} + 
\begin{bmatrix} \frac{v_{\text{dc},j}}{L_{\text{arm}}} \\ 0 \end{bmatrix}
$$

其中 $j \in \{\text{up}, \text{low}\}$ 表示上下桥臂，$m_j(t)$ 为调制信号（平均值意义下的占空比），$R_{\text{arm}}$、$L_{\text{arm}}$ 为桥臂电阻和电感，$C_{\text{eq}} = \frac{N \cdot C_{\text{sm}}}{2}$ 为基于能量守恒推导的等效直流电容（$N$ 为每桥臂子模块数，$C_{\text{sm}}$ 为单个子模块电容），$R_{\text{loss}}$ 为等效损耗电阻。

## EMT中的角色

在传统 EMT 仿真中，MMC 的详细开关模型（Detailed Switching Model, DSM）需要显式表示每个子模块中的 IGBT、反并联二极管、电容及其开关事件。对于每桥臂 400 个子模块的 401 电平 MMC，仅一个换流站就包含超过 4800 个开关元件，网络导纳矩阵庞大且频繁重求逆，计算负担极重。

统一 AVM 的引入解决了以下核心挑战：

1. **计算效率**：将开关级模型降阶为连续平均值模型，允许积分步长从微秒级放宽至 40–100 μs，计算速度提升 10–100 倍。
2. **解析可解释性**：区别于黑箱 VSC 级 AVM，多阀臂级 AVM 保留了桥臂层级的状态变量（桥臂电流、等效电容电压），可用于环流分析、电容纹波评估和器件选型。
3. **故障工况适配**：传统 AVM 在直流故障和闭锁工况下因丢失续流二极管路径而失效，改进型 AVM 通过拓扑切换机制恢复故障物理通路。

## 统一平均值建模方法

基于 Herath & Filizadeh (2021)、Xu et al. (2014)、Yu et al. (2013) 等文献，MMC 统一平均值建模可归纳为以下三种层级：

### 方法一：VSC 级黑箱 AVM

将整个 MMC 换流器等效为单一交流侧受控电压源和直流侧受控电流源，不保留桥臂和子模块信息。

**原理**：
$$v_{\text{ac}} = m(t) \cdot \frac{V_{\text{dc}}}{2}, \quad i_{\text{dc}} = \frac{P_{\text{ac}}}{V_{\text{dc}}}$$

其中 $m(t)$ 为调制指数，$V_{\text{dc}}$ 为直流母线电压，$P_{\text{ac}}$ 为交流侧瞬时功率。

**特点**：
- 状态量极少（仅直流电容电压）
- 计算效率最高
- 丢失桥臂层级信息，无法分析环流和电容纹波
- 适用于纯系统级潮流和交流扰动分析

### 方法二：多阀臂级 AVM（本文核心）

将 MMC 的上下桥臂分别等效为受控电压源串联等效电阻，保留桥臂层级状态变量。

**上桥臂等效电压源**：
$$v^{\text{up}} = N \cdot m_{\text{up}} \cdot \frac{1}{C_{\text{sm}}} \int \left[ (1 - d_{\text{up}})i_L^{\text{up}} + m_{\text{up}} i^{\text{up}} \right] dt$$

**下桥臂等效电压源**：
$$v^{\text{low}} = N \cdot m_{\text{low}} \cdot \frac{1}{C_{\text{sm}}} \int \left[ (1 - d_{\text{low}})i_L^{\text{low}} + m_{\text{low}} i^{\text{low}} \right] dt$$

其中 $d$ 为 DC-DC 变换器占空比（含储能 MMC 场景），$i_L$ 为 DC-DC 电感电流，$i$ 为桥臂电流。

**特点**：
- 保留桥臂层级状态变量（桥臂电流、子模块等效电容电压）
- 可解析计算环流（基波与二次谐波）和电容电压纹波
- 适用于控制器参数整定、器件选型、环流抑制控制设计
- 计算效率较详细模型提升约 80–90 倍

### 方法三：改进型 AVM（含故障拓扑切换）

在传统多阀臂 AVM 基础上引入受控开关和二极管路径，使模型在正常运行时退化为传统 AVM，在故障/闭锁时激活续流与放电路径。

**正常运行**（闭合 S1、S3、S4，断开 S2）：
$$v_{\text{up},i} = \text{Mod}\left[\frac{V_{\text{dc}}}{2} - v_{\text{ref},i}\right], \quad v_{\text{low},i} = \text{Mod}\left[\frac{V_{\text{dc}}}{2} + v_{\text{ref},i}\right]$$

**换流器闭锁**（断开 S1、S3，闭合 S2）：
- 交流侧受控电压源置零
- 续流二极管 D1 串入电路模拟 IGBT 关断后的反并联续流路径
- 直流侧受控电流源置零，二极管 D3 钳位直流电压

**极间直流故障**（断开 S4）：
$$L_{\text{eq}} = \frac{2}{3}L_{\text{arm}}, \quad R_{\text{eq}} = \frac{2}{3}R_{\text{on}}$$

等效电容 $C_{\text{eq}}$ 通过等效电阻 $R_{\text{eq}}$ 和等效电感 $L_{\text{eq}}$ 向故障点放电，放电回路阻抗按三相并联且每相双桥臂串联关系折算。

**特点**：
- 在故障工况下误差 < 2.5%，传统 AVM 完全失效
- 计算耗时较传统 AVM 增加约 37%，但仍远快于详细模型
- 适用于直流故障传播分析和保护策略初筛

### 三种方法对比

| 维度 | VSC 级黑箱 AVM | 多阀臂级 AVM | 改进型 AVM（含故障切换） |
|------|---------------|-------------|------------------------|
| 状态变量数 | 1（直流电容电压） | 4（上下桥臂电流 + 上下桥臂等效电容电压） | 4（同左）+ 开关状态 |
| 计算步长 | 100 μs | 40–100 μs | 40–100 μs |
| 环流分析 | 不支持 | 支持（解析公式） | 支持（解析公式） |
| 电容纹波 | 不支持 | 支持（解析公式） | 支持（解析公式） |
| 直流故障 | 不支持 | 不支持（误差 > 300%） | 支持（误差 < 2.5%） |
| 换流器闭锁 | 不支持 | 不支持 | 支持（误差 < 2%） |
| 加速比（vs DSM） | ~90x | ~80x | ~50x |
| 适用场景 | 系统级潮流、交流扰动 | 控制器整定、器件选型 | 故障分析、保护策略 |

## 形式化表达

### 交直流功率平衡方程

统一 AVM 的核心约束是交直流侧瞬时功率守恒：

$$P_{\text{ac}} = P_{\text{dc}} + P_{\text{loss}}$$

展开为三相形式：
$$\sum_{i=a,b,c} v_{i}(t) \cdot i_{i}(t) = v_{\text{dc}}(t) \cdot i_{\text{dc}}(t) + P_{\text{loss}}$$

由此推导直流侧等效电流源：
$$i_{\text{dc}} = \frac{\sum_{i=a,b,c} v_{\text{ref},i} \cdot i_{\text{ac},i}}{V_{\text{dc}}} - i_{\text{dc,loss}}$$

其中 $i_{\text{dc,loss}}$ 为扣除换流器内部损耗（约 1%）后的等效损耗电流。

### 环流解析表达式

二次谐波环流在桥臂电感上产生的压降：
$$v_{2L} = 2L_{\text{arm}} \frac{d}{dt} i_2^{\text{circ}} = -4L_{\text{arm}} \omega \hat{i}_2^{\text{circ}} \sin(2\omega t + \phi_2^{\text{circ}})$$

环流幅值与相位解析解：
$$\hat{i}_2^{\text{circ}} = \frac{3Nm^2 + 2N}{12\omega L_{\text{arm}} C_{\text{sm}}} \cdot \text{function of modulation index}$$

### 子模块电容电压纹波

子模块电容电压的积分表达式：
$$v_{C,j}^k = \frac{1}{C_{\text{sm}}} \int \left[ (1 - d_{kj})i_{L,j}^k + m_{kj}i_{kj} \right] dt$$

纹波峰值解析预测误差 < 1.5%，相位偏差 < 2°。

### 等效电容推导

基于全桥能量守恒，将 $N$ 个子模块电容等效为直流侧单一电容：
$$C_{\text{eq}} = \frac{N \cdot C_{\text{sm}}}{2}$$

### Norton 等效注入

AVM 嵌入 EMT 求解器时，通过 Norton 等效将 MMC 表示为导纳矩阵可组装的支路：
$$i_{\text{inj}}(t) = Y_{\text{eq}} \cdot v(t) + i_{\text{hist}}(t)$$

其中 $i_{\text{hist}}(t)$ 为历史电流源，由前一时刻的电压/电流状态递推得到。

## 关键技术挑战

### 1. 平均储能假设的有效性边界

统一 AVM 的核心假设是子模块电容电压在工频周期内近似恒定。当子模块电容较大（$C_{\text{sm}} \geq 20\ \text{mF}$，电压纹波 < 2%）时，该假设成立；当电容降至 10 mF（纹波 > 5%）时，动态精度显著下降。

### 2. 故障工况下的拓扑正确性

传统 AVM 在直流故障时因丢失二极管续流路径而给出严重错误的电流峰值（73 p.u. vs 17 p.u.，误差 > 300%）。改进型 AVM 通过受控开关和二极管路径恢复了故障物理通路，但开关切换逻辑的时序精度对仿真结果有显著影响。

### 3. 环流抑制控制（CCSC）的集成

多阀臂级 AVM 支持在模型中集成环流抑制控制。启用 CCSC 后，环流幅值可从峰值 12.5 A 降至 1.8 A，模型预测轨迹与详细模型重合度达 98.7%。但 CCSC 的参数整定需要依赖 AVM 的解析环流公式，而非数值仿真。

## 量化性能边界

### 精度验证（Herath & Filizadeh 2021）

| 测试场景 | AVM 预测值 | 详细模型值 | 实验测量值 | 误差 |
|---------|-----------|-----------|-----------|------|
| 二次谐波环流幅值 | 1.8 A (CCSC启用) | 1.8 A | 1.85 A | < 1.5% |
| 电容电压纹波峰值 | 4.2 V | 4.3 V | 4.35 V | < 3.4% |
| 导通损耗计算 | — | — | — | < 2% |
| 功率阶跃恢复时间 | 45 ms | 46 ms | 47 ms | < 2.5% |

### 精度验证（Xu et al. 2014）

| 测试场景 | 改进 AVM 误差 | 传统 AVM 误差 |
|---------|-------------|-------------|
| 启动充电直流电压 | < 1% | 不适用 |
| 启动充电交流电流 | < 1% | 不适用 |
| 极间直流故障直流电压 | < 2.5% | 完全失效 |
| 极间直流故障交流电压 | < 2% | 完全失效 |
| 单极接地直流偏置 | < 1% | 无法显示 |

### 计算性能

| 模型类型 | 积分步长 | 相对速度 | 加速比 (vs DSM) |
|---------|---------|---------|----------------|
| 详细开关模型 (Type 2) | 1 μs | 基准 | 1x |
| 戴维南等效 (Type 4) | 40 μs | 快 12x | ~480x |
| 多阀臂 AVM (Type 5) | 40–100 μs | 快 10–16x | ~80–90x |
| 基频 AVM (Type 6) | 100 μs | 最快 | ~100x+ |

*数据来源：Yu et al. 2013 (IEEE Task Force, EMTP-RV 验证，1000 MW / 401 电平 MMC-HVDC)*

## 适用边界与选择指南

### 适用条件

- **系统级 EMT 仿真**：关注 MMC 端口的基波有功/无功交换和直流侧动态
- **控制器参数整定**：需要解析环流公式和电容纹波表达式
- **器件选型**：桥臂电感、子模块电容、DC-DC 变换器的容量评估
- **大电网集成**：需要快速仿真多端 MMC-MTDC 电网的暂态响应
- **故障传播分析**：使用改进型 AVM 分析直流故障和换流器闭锁

### 不适用条件

- **子模块级故障分析**：子模块旁路、电容电压不均衡、开关管短路/开路
- **极端调制比**：过调制工况下平均化假设失效
- **高频谐波交互**：开关频率附近的谐振分析
- **器件应力与热冲击**：IGBT 开关瞬态、反并联二极管恢复
- **电磁兼容**：开关级 EMI 分析

### 场景-方法选择指南

| 分析目标 | 推荐模型 | 理由 |
|---------|---------|------|
| 稳态潮流 / 交流扰动 | VSC 级黑箱 AVM | 状态量最少，计算最快 |
| 环流抑制控制设计 | 多阀臂级 AVM | 保留桥臂层级，可解析环流 |
| 器件容量选型 | 多阀臂级 AVM | 可解析电容纹波和导通损耗 |
| 直流故障传播 | 改进型 AVM | 恢复故障续流路径 |
| 换流器闭锁分析 | 改进型 AVM | 模拟二极管续流和能量耗散 |
| 子模块均压控制 | 详细开关模型 | AVM 丢失 SM 级信息 |
| 开关损耗评估 | 详细开关模型 | AVM 忽略开关瞬态 |

## 相关方法

- [[average-value-model]] — 平均值建模的正式方法入口
- [[mmc-model]] — MMC 设备和建模对象入口
- [[mmc-modeling]] — MMC 建模路线综述入口
- [[state-space-average-method]] — 平均化状态空间推导的相邻方法页
- [[detailed-equivalent-model]] — 详细等效模型（DEM）
- [[circulating-current-suppression]] — 环流抑制控制
- [[nearest-level-modulation]] — 最近电平调制
- [[pwm-modulation]] — PWM 调制方法
- [[submodule-model]] — 子模块建模
- [[arm-reactor]] — 桥臂电抗器建模
- [[vsc-model]] — VSC 模型
- [[dc-fault-blocking]] — 直流故障与闭锁分析
- [[emt-simulation]] — 电磁暂态仿真
- [[large-scale-system-simulation]] — 大规模系统仿真
- [[power-electronics-modeling]] — 电力电子建模
- [[companion-model]] — 伴随模型（EMT 离散化）
- [[nodal-analysis]] — 节点分析法

## AVM 方法体系架构

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 420" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#333"/>
    </marker>
    <filter id="shadow" x="-2%" y="-2%" width="104%" height="104%">
      <feDropShadow dx="1" dy="1" stdDeviation="1" flood-color="#00000033"/>
    </filter>
  </defs>

  <!-- Title -->
  <text x="450" y="25" fill="#1a1a2e" font-size="15" font-weight="bold" text-anchor="middle" font-family="serif">MMC 统一平均值模型 (AVM) 三级体系</text>

  <!-- ===== Top Row: 输入 ===== -->
  <rect x="340" y="45" width="120" height="45" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2" filter="url(#shadow)"/>
  <text x="400" y="63" fill="#1e3a5f" font-size="12" font-weight="bold" text-anchor="middle">MMC 多阀臂结构</text>
  <text x="400" y="79" fill="#4b6b8f" font-size="9" text-anchor="middle">N×SM 串联 / 双桥臂</text>

  <!-- ===== Middle Row: 三种 AVM 方法 ===== -->

  <!-- VSC级黑箱 AVM (左) -->
  <rect x="30" y="130" width="230" height="120" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2" filter="url(#shadow)"/>
  <text x="145" y="152" fill="#78350f" font-size="13" font-weight="bold" text-anchor="middle">方法一：VSC 级黑箱 AVM</text>
  <text x="145" y="170" fill="#92400e" font-size="10" text-anchor="middle">状态量: 1 (直流电容电压)</text>
  <text x="145" y="186" fill="#92400e" font-size="10" text-anchor="middle">v_ac = m(t)·V_dc/2</text>
  <text x="145" y="202" fill="#92400e" font-size="10" text-anchor="middle">i_dc = P_ac / V_dc</text>
  <text x="145" y="220" fill="#92400e" font-size="10" text-anchor="middle">加速比 ~90x</text>
  <text x="145" y="238" fill="#b91c1c" font-size="9" text-anchor="middle">✗ 环流/故障 不支持</text>

  <!-- 多阀臂级 AVM (中) -->
  <rect x="310" y="130" width="230" height="120" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>
  <text x="425" y="152" fill="#14532d" font-size="13" font-weight="bold" text-anchor="middle">方法二：多阀臂级 AVM</text>
  <text x="425" y="170" fill="#166534" font-size="10" text-anchor="middle">状态量: 4 (上下桥臂电流</text>
  <text x="425" y="186" fill="#166534" font-size="10" text-anchor="middle">  + 等效电容电压)</text>
  <text x="425" y="202" fill="#166534" font-size="10" text-anchor="middle">v_up = N·m_up·∫[...]dt</text>
  <text x="425" y="218" fill="#166534" font-size="10" text-anchor="middle">加速比 ~80x</text>
  <text x="425" y="238" fill="#16a34a" font-size="9" text-anchor="middle">✓ 环流/纹波 解析支持</text>

  <!-- 改进型 AVM (右) -->
  <rect x="610" y="130" width="230" height="120" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2" filter="url(#shadow)"/>
  <text x="725" y="152" fill="#78350f" font-size="13" font-weight="bold" text-anchor="middle">方法三：改进型 AVM</text>
  <text x="725" y="170" fill="#92400e" font-size="10" text-anchor="middle">状态量: 4 + 开关状态</text>
  <text x="725" y="186" fill="#92400e" font-size="10" text-anchor="middle">拓扑切换 S1-S4, D1-D3</text>
  <text x="725" y="202" fill="#92400e" font-size="10" text-anchor="middle">L_eq = 2/3·L_arm</text>
  <text x="725" y="218" fill="#92400e" font-size="10" text-anchor="middle">加速比 ~50x</text>
  <text x="725" y="238" fill="#b91c1c" font-size="9" text-anchor="middle">✓ 故障/闭锁 支持</text>

  <!-- Arrows from top to middle -->
  <line x1="400" y1="90" x2="145" y2="128" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="400" y1="90" x2="425" y2="128" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="400" y1="90" x2="725" y2="128" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- ===== Bottom Row: 应用场景 ===== -->

  <!-- 应用1 -->
  <rect x="30" y="290" width="230" height="50" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2" filter="url(#shadow)"/>
  <text x="145" y="310" fill="#1e3a5f" font-size="11" font-weight="bold" text-anchor="middle">系统级潮流 / 交流扰动</text>
  <text x="145" y="326" fill="#4b6b8f" font-size="9" text-anchor="middle">稳态谐波 / 大电网集成</text>

  <!-- 应用2 -->
  <rect x="310" y="290" width="230" height="50" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>
  <text x="425" y="310" fill="#14532d" font-size="11" font-weight="bold" text-anchor="middle">控制器整定 / 器件选型</text>
  <text x="425" y="326" fill="#3a7a5a" font-size="9" text-anchor="middle">环流抑制 / 电容纹波评估</text>

  <!-- 应用3 -->
  <rect x="610" y="290" width="230" height="50" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="2" filter="url(#shadow)"/>
  <text x="725" y="310" fill="#3b0764" font-size="11" font-weight="bold" text-anchor="middle">直流故障 / 换流器闭锁</text>
  <text x="725" y="326" fill="#6b21a8" font-size="9" text-anchor="middle">故障传播 / 保护策略初筛</text>

  <!-- Arrows from middle to bottom -->
  <line x1="145" y1="250" x2="145" y2="288" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="425" y1="250" x2="425" y2="288" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="725" y1="250" x2="725" y2="288" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- ===== 不适用场景 (底部红色区域) ===== -->
  <rect x="100" y="370" width="700" height="35" rx="4" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="6,3"/>
  <text x="450" y="392" fill="#7f1d1d" font-size="10" text-anchor="middle">不适用: 子模块级故障分析 · 器件应力与热冲击 · 开关损耗评估 · 高频谐波交互 · 电磁兼容</text>

</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · MMC 统一平均值模型三级体系架构与场景选择指南</p>

## 来源论文

- **Herath & Filizadeh 2021** — *Average-Value Model for a Modular Multilevel Converter With Embedded Storage* (IEEE TEC, Vol. 36, No. 2)：提出含子模块级 DC-DC 变换器的 MMC-ES 多阀臂级 AVM，支持环流解析和电容纹波表征，仿真加速比约 80–90 倍。
- **Herath et al. 2019** — *Modeling of a Modular Multilevel Converter With Embedded Energy Storage for Electromagnetic Transient Simulations* (IEEE TEC, Vol. 34, No. 4)：提出 MMC-ES 的详细等效模型（DEM），使用戴维南等效替代开关级模型，保留 SM 级信息的同时大幅降低网络维度。
- **Xu, Gole & Zhao 2014** — *Average-Value Models for Modular Multilevel Converters Operating in a VSC-HVDC Grid* (IEEE TPWRD)：改进型 AVM，引入故障拓扑切换机制（受控开关 S1-S4、二极管 D1-D3），使 AVM 在直流故障和闭锁工况下恢复物理正确性，故障误差 < 2.5%。
- **Yu, Lin, Wang & Xie 2013** — *Dynamic Averaged and Simplified Models for MMC-Based HVDC Transmission Systems* (IEEE TPWRD, IEEE Task Force)：系统比较 6 种 MMC EMT 模型（Type 1–6），建立模型选型指南，验证 AVM 在交流暂态下精度优异且计算极快，但完全不适用于直流故障（误差 > 300%）。
