---
title: "VSC-MMC测试系统"
type: model
tags: [vsc, mmc, test-system, hvdc, benchmark, model-validation, emt-simulation]
created: "2026-05-04"
updated: "2026-05-14"
---

# VSC-MMC测试系统

## 定义

VSC-MMC测试系统（VSC-MMC Test System）是用于验证VSC（电压源换流器）和MMC（模块化多电平换流器）EMT建模精度与效率的标准化基准系统。该类系统通常包含两端或多端VSC/MMC换流站、交直流输电网络和控制保护系统，广泛应用于模型降阶验证、平均值模型（AVM）精度评估、控制策略开发和硬件在环（HIL）测试等研究。

VSC-MMC测试系统的核心价值在于提供了一个**可复现、可对比**的仿真基准——不同文献采用相同测试系统时，其建模方法的精度和效率可以直接比较。然而，由于不同文献的测试系统参数缺乏统一标准，实际研究中仍存在对比困难的问题。

## EMT中的角色

在EMT仿真中，VSC-MMC测试系统承担以下关键角色：

- **模型验证基准**：作为新建模方法（如戴维南等效、NFSS、AVM）的验证平台，对比其与详细开关模型的精度差异
- **控制策略开发平台**：在离线环境中测试MMC控制算法（如电容电压平衡、环流抑制、NLC调制）
- **仿真效率评估**：量化不同建模方法在计算时间、内存占用和步长选择上的差异
- **HIL测试基准**：为实时仿真提供标准化的测试场景

核心挑战在于：MMC的开关器件数量随电平数线性增长（如400电平MMC每相需4800个IGBT），导致详细模型（TDM）的节点导纳矩阵规模巨大，难以在普通计算平台上进行大规模参数扫描。

## 测试系统分类与典型配置

### 两电平VSC测试系统

两电平VSC是最基本的柔性直流测试平台，其典型配置参考2012年DAVM标准测试系统：

**额定参数**：
- 额定容量：10–1000 MVA
- AC电压等级：12.5–525 kV
- DC电压等级：±5–±800 kV
- 开关频率：1980–2000 Hz
- 直流侧电容：200–5000 μF

**控制架构**：
- 整流站（送端）：定DC电压控制 + 定无功功率控制
- 逆变站（受端）：定有功功率控制 + 定无功功率控制

两电平VSC的直流侧仅含少量电容，交流侧通常无需滤波器即可输出接近正弦的波形。其EMT建模相对简单，主要用于验证VSC控制策略和交直流耦合动态特性。

### MMC测试系统

#### 401电平MMC系统（Peralta 2012, IEEE Task Force 2013）

这是最广泛使用的MMC基准测试系统之一：

| 参数 | 数值 |
|------|------|
| 额定功率 | 1000 MW |
| 子模块数 | 400个/桥臂（共401电平） |
| DC电压 | ±320 kV |
| AC电压（线电压） | 220 kV |
| 总IGBT数量 | 4812个（6桥臂 × 400 SM × 2 IGBT） |
| 子模块电容 | 10 mF |
| 桥臂电感 | 100 mH |
| 详细模型步长 | 1–5 μs |
| AVM步长 | 20–100 μs |

该系统在IEEE Task Force报告中被用作MMC模型验证的标准基准，其参数设置为后续研究提供了重要的参考基线。

#### 41电平MMC系统（IEEE标准测试系统）

中等规模MMC测试系统，适用于算法验证和参数扫描：

| 参数 | 数值 |
|------|------|
| 额定功率 | 640 MW |
| 子模块数 | 40个/桥臂（共41电平） |
| DC电压 | ±320 kV |
| 详细模型步长 | 1–5 μs |
| AVM步长 | 20–100 μs |

#### 31电平MMC系统（Beddard 2015）

用于三种建模技术（TDM/DEM/AM）对比的测试系统：

| 参数 | 数值 |
|------|------|
| 电平数 | 31 |
| 短路比（SCR） | 3.5 |
| 变压器接线 | Delta/Star（带分接开关） |
| SM电容 | 计算得10%纹波电压 |
| 调制方式 | NLC（最近电平调制） |
| 运行功率点 | 100/500/1000 MW（三档） |

31电平的选择依据：在NLC调制下，31电平可在PCC点产生可接受的谐波性能，同时保持合理的仿真复杂度，适合公平对比不同建模技术。

#### Gnanarathna 2011点对点VSC-MMC-HVDC系统

Gnanarathna等人提出的点对点HVDC传输系统，用于验证其提出的Thévenin等效模型：

| 参数 | 数值 |
|------|------|
| DC系统额定 | 400 MW, 200 kV |
| 子模块额定电压 | 4.0 kV |
| 子模块数范围测试 | 2–120个/桥臂 |
| 仿真步长 | 20 μs |
| 计算机配置 | Intel Core 2 Duo E8400 @ 3.00 GHz, 3.37 GB RAM |
| 仿真软件 | PSCAD/EMTDC X4 (Beta) |

该系统采用直接控制方法：整流站通过移相角控制DC电压，通过调制指数控制交流侧母线电压；逆变站通过PI控制器调节有功和无功功率。

## 核心建模方法

VSC-MMC测试系统的建模方法按精度-效率权衡可分为三个层级：

### 1. 传统详细模型（TDM, Traditional Detailed Model）

TDM是MMC建模的基准方法，每个子模块的IGBT、二极管和电容均在仿真软件中显式构建，桥臂内子模块按串联方式电气连接。

**原理**：每个子模块包含两个反并联IGBT（T1/T2）和一个串联电容C。正常工作时，T1和T2中只有一个导通——T1导通时电容电压出现在SM端，T2导通时SM被旁路（端电压为0）。通过控制每个SM的开关状态，桥臂输出电压为所有激活SM电容电压之和。

**数学表达**：

a相桥臂输出电压由上下桥臂子模块状态决定：

$$u_{xu} = \frac{1}{2}u_{dc} - \sum_{i=1}^{N} s_{xi}u_{Cxi} - \frac{3}{4}m_x\frac{u_{dc}}{2}\cos(\omega t + \phi_x)$$

$$u_{xl} = \frac{1}{2}u_{dc} + \sum_{i=1}^{N} s_{xi}u_{Cxi} + \frac{3}{4}m_x\frac{u_{dc}}{2}\cos(\omega t + \phi_x)$$

其中 $u_{xu}$ 和 $u_{xl}$ 分别为x相上/下桥臂中点电压，$s_{xi} \in \{0,1\}$ 为第i个子模块的开关状态，$u_{Cxi}$ 为第i个子模块电容电压，$N$ 为每桥臂子模块数，$m_x$ 为调制指数。

**特点**：
- 精度最高：每个开关器件的瞬态行为均被精确建模
- 可获取SM电容电压的个体波动和环流谐波
- 节点导纳矩阵规模 = 总节点数（每SM约2–3个节点）
- 每开关周期需重新三角化导纳矩阵

**局限性**：对于400电平MMC，每相需800个SM × 2个器件/SM = 1600个开关器件，三相共4800个。每个开关状态变化都触发导纳矩阵重新三角化，计算量随SM数量呈超线性增长。

### 2. 详细等效模型（DEM, Detailed Equivalent Model）

DEM由Gnanarathna等人于2011年提出，采用"嵌套快速同时求解"（NFSS, Nested Fast and Simultaneous Solution）算法，将网络划分为小个子网络，对每个子网络分别求解导纳矩阵。

**原理**：将MMC的每个子模块视为独立子网络，通过Schur补法递归消去子模块内部节点，将每个SM等效为时变电导-电流源组合。桥臂内所有SM的等效电路合并为一个等效支路，但仍保留每个SM电容电压的个体身份。

**数学表达**（两分区网络等效）：

将网络分为分区1（外部系统）和分区2（MMC），节点电压方程为：

$$\begin{bmatrix} \mathbf{Y}_{11} & \mathbf{Y}_{12} \\ \mathbf{Y}_{21} & \mathbf{Y}_{22} \end{bmatrix} \begin{bmatrix} \mathbf{V}_1 \\ \mathbf{V}_2 \end{bmatrix} = \begin{bmatrix} \mathbf{I}_1 \\ \mathbf{I}_2 \end{bmatrix}$$

对分区2求Schur补，消去 $\mathbf{V}_2$，得到仅含分区1未知节点的等效方程：

$$\left(\mathbf{Y}_{11} - \mathbf{Y}_{12}\mathbf{Y}_{22}^{-1}\mathbf{Y}_{21}\right)\mathbf{V}_1 = \mathbf{I}_1 - \mathbf{Y}_{12}\mathbf{Y}_{22}^{-1}\mathbf{I}_2$$

其中 $\mathbf{Y}_{11}$ 和 $\mathbf{Y}_{22}$ 分别为分区1和分区2的导纳矩阵，$\mathbf{Y}_{12} = \mathbf{Y}_{21}^T$ 为互联导纳矩阵，$\mathbf{V}_1$ 和 $\mathbf{V}_2$ 为分区1和分区2的节点电压向量。

**等效Thévenin模型**：分区2的等效Thévenin阻抗和电压源为：

$$\mathbf{Z}_{th} = \mathbf{Y}_{22}^{-1}$$

$$\mathbf{E}_{th} = \mathbf{Z}_{th} \cdot \mathbf{I}_2 + \mathbf{Y}_{22}^{-1}\mathbf{Y}_{21}\mathbf{V}_1$$

其中 $\mathbf{Z}_{th}$ 为等效Thévenin阻抗矩阵，$\mathbf{E}_{th}$ 为等效Thévenin电压源向量。

**特点**：
- 精度与TDM完全一致（数学等价）
- 导纳矩阵规模从全局降为局部（每个SM子网络）
- 无需牺牲任何精度换取加速
- 在个人计算机上即可仿真大型MMC-HVDC系统

**局限性**：
- 每个SM的开关状态仍需追踪（用于更新等效参数）
- 子模块个体身份在主要EMT求解器中不可直接访问
- 需要额外的等效求解器模块

### 3. 加速模型（AM, Accelerated Model）

AM由Xu等人提出，是TDM和DEM的混合方法。用户可像TDM一样访问SM组件，但桥臂被建模为可控电压源。

**原理**：将串联SM从桥臂中移除，用受控电压源替代。电压源的值由SM等效电路计算得出：

$$V_{arm} = N \cdot \overline{V}_{SM} - I_{arm} \cdot Z_{arm}$$

其中 $N$ 为桥臂中激活的SM数量，$\overline{V}_{SM}$ 为SM电容平均电压，$I_{arm}$ 为桥臂电流，$Z_{arm}$ 为桥臂等效阻抗。

**特点**：
- 用户可访问SM组件（相比DEM的完全抽象）
- 桥臂作为受控电压源，大幅减少节点数
- 计算效率介于TDM和DEM之间
- 适合需要SM细节但又不需全开关精度的场景

### 4. 平均值模型（AVM, Average Value Model）

AVM将MMC等效为连续电压源，忽略开关瞬态，适用于毫秒级仿真。

**原理**：用桥臂平均电容电压替代每个SM的离散电容电压，将开关动作平均化为连续调制信号。

**数学表达**：

$$\frac{d\overline{V}_{C,i}}{dt} = \frac{s_{i} \cdot i_{arm} - C \cdot \frac{d\overline{V}_{C,i}}{dt}|_{balancing}}{C}$$

其中 $\overline{V}_{C,i}$ 为SM平均电容电压，$s_i$ 为开关占空比，$i_{arm}$ 为桥臂电流，$C$ 为SM电容值。

**特点**：
- 计算效率最高，步长可达100–1000 μs
- 丢失开关瞬态和电容电压纹波细节
- 适用于系统级研究和控制策略开发

## 量化性能边界

### 仿真步长对比

不同建模方法推荐的仿真步长范围：

| 建模方法 | 推荐步长 | 加速比（相对TDM） | 数据来源 |
|----------|----------|-------------------|----------|
| 详细开关模型（TDM） | 1–5 μs | 1×（基准） | Gnanarathna 2011 |
| DEM（戴维南等效） | 5–20 μs | 310×（120 SM/桥臂） | Gnanarathna 2011 |
| AM（加速模型） | 5–20 μs | 10–50× | Beddard 2015 |
| 改进AVM | 20–50 μs | 50–200× | Ebrahimi 2023 |
| 简化AVM（DI-AVM） | 可达1000 μs | 200–1000× | Ebrahimi 2023 |

### 精度对比（401电平MMC，稳态运行）

**Gnanarathna 2011**：
- DEM与TDM的波形在稳态和暂态下完全一致
- 直流电压误差 < 0.1%
- 交流电流波形重叠度 > 99.9%
- 子模块电容电压波动精度一致

**Beddard 2015**（31电平MMC，归一化平均绝对误差）：

| 工况 | DEM vs TDM | AM vs TDM |
|------|-----------|----------|
| 稳态1000 MW | < 0.5% | < 1.2% |
| 稳态500 MW | < 0.5% | < 1.0% |
| 稳态100 MW | < 0.8% | < 1.5% |
| DC线-线故障 | < 2.0% | < 3.5% |
| AC线-地故障 | < 1.5% | < 2.8% |

AM在电流过零点附近存在微小误差（由于受控源近似），但不影响控制保护和系统级研究。

### 计算加速比

**Gnanarathna 2011**（120 SM/桥臂，PSCAD/EMTDC）：
- TDM：5秒仿真需要 > 90分钟（Intel Core 2 Duo E8400 @ 3.00 GHz）
- DEM：5秒仿真仅需 ~17秒
- 加速比：**> 310倍**（2S-DIRK积分法结果相似）
- 2 SM/桥臂：加速比 ~ 3×
- 20 SM/桥臂：加速比 ~ 30×
- 120 SM/桥臂：加速比 > 310×
- 加速比随SM数量增加呈超线性增长

**Beddard 2015**（5秒仿真，PSCAD X4，Intel i7-2860 @ 2.5 GHz, 8 GB RAM）：
- 16电平：TDM最快，DEM和AM时间相近
- 31电平：DEM速度开始超越TDM
- 61电平：DEM比TDM快约5–10倍
- 120+电平：DEM比TDM快50–100倍

**IEEE Task Force 2013**（401电平系统）：
- AVM相比TDM加速比：10–16倍
- 步长从5 μs增至100 μs时，计算时间减少约90%

**Ebrahimi 2023**（DI-AVM）：
- 简化AVM步长可达1000 μs
- 相比TDM加速比 > 200×
- 适用于大规模MMC-MTDC系统

### 故障响应精度

**直流故障峰值电流**（401电平MMC，IEEE Task Force 2013）：
- TDM峰值电流：约17 p.u.
- AVM峰值电流：约73 p.u.
- AVM在直流故障初期高估故障电流，但稳态后误差减小
- 结论：AVM不适合直流故障电流精确评估，但可用于保护策略的初步验证

**交流故障**：
- DEM和AM在AC线-地故障下的波形误差 < 2%
- AM在电流过零点附近有微小失真，但不影响故障检测和切除逻辑

## 关键技术挑战

### 1. 测试系统参数标准化缺失

不同文献采用的测试系统参数差异显著：
- Gnanarathna 2011：400 MW, 200 kV, 4.0 kV/SM
- IEEE Task Force 2013：1000 MW, ±320 kV, 400 SM/桥臂
- Beddard 2015：未明确额定功率，31电平, SCR=3.5

这种参数不一致性使得不同研究之间的建模方法对比缺乏公平性。

### 2. 小系统结论外推风险

小规模测试系统（如31电平）的结论不可直接推广至大规模系统（如400+电平）。SM数量对加速比的影响呈超线性关系——小规模系统的加速优势在大规模系统中才被充分展现。

### 3. 直流故障建模精度

AVM在直流故障期间的精度明显低于稳态工况。这是由于AVM的连续电压源近似无法捕捉开关器件在故障期间的离散导通/关断行为。对于需要精确故障电流评估的研究，必须使用TDM或DEM。

### 4. 环流和谐波建模

TDM可精确捕捉桥臂环流（二次谐波）和SM电容电压纹波。DEM和AM在环流建模方面存在近似——DEM保留环流但通过等效阻抗近似，AM则使用平均化环流模型。对于高频振荡和环流抑制策略的研究，TDM仍是首选。

## 适用边界与选择指南

### 建模方法选择决策表

| 应用场景 | 推荐模型 | 理由 |
|----------|----------|------|
| 控制策略离线开发 | AVM | 计算效率高，步长大，适合长时间仿真 |
| 模型降阶验证 | DEM | 精度与TDM一致，加速比高 |
| 直流故障电流评估 | TDM或DEM | AVM高估故障电流 |
| SM电容电压纹波分析 | TDM | 仅TDM可获取个体SM电容波动 |
| 环流抑制策略验证 | TDM | 需精确环流谐波 |
| 大规模MMC-MTDC系统仿真 | DEM或AM | 平衡精度与效率 |
| 高频振荡分析 | TDM | 需精确开关瞬态 |
| HIL测试 | DEM或AM | 满足实时性要求 |
| 系统级稳定性研究 | AVM | 长时间仿真，关注低频动态 |

### 适用条件

- **VSC/MMC建模方法验证与对比**：TDM作为基准，DEM/AM作为候选
- **控制策略离线开发**：AVM提供足够精度且计算效率高
- **模型降阶和平均值模型基准测试**：标准化测试系统确保可复现性
- **HIL测试**：DEM/AM满足实时仿真时间约束

### 失效边界

- 小规模测试系统的结论不可直接推广至大规模系统（SM数量影响加速比）
- 测试系统参数与实际工程的差异可能导致验证结果偏差
- 不同文献的测试系统配置不一致，影响方法间公平对比
- AVM不适用于直流故障电流精确评估和开关瞬态研究

## 相关模型

- [[mmc-model|MMC模型]] - 模块化多电平换流器
- [[vsc-model|VSC模型]] - 两电平换流器EMT模型
- [[gnanarathna-2011-efficient-mmc|Gnanarathna高效MMC戴维南等效模型]] - MMC高效建模
- [[peralta-2012-detailed-mmc|Peralta 401电平MMC详细与平均模型]] - 基准模型
- [[average-value-model|平均值模型]] - 系统级等效
- [[model-order-reduction|模型降阶]] - 降阶方法

## 相关方法

- [[real-time-simulation|实时仿真]] - HIL测试
- [[co-simulation|混合仿真]] - 多速率仿真

## 来源论文

- **Gnanarathna et al. 2011** "Efficient Modeling of Modular Multilevel HVDC Converters (MMC) on Electromagnetic Transient Simulation Programs" — 提出基于Schur补的Thévenin等效模型（DEM），实现310倍加速，为后续MMC高效建模奠定基础
- **Beddard et al. 2015** "Comparison of Detailed Modeling Techniques for MMC Employed on VSC-HVDC Schemes" — 系统对比TDM/DEM/AM三种建模技术，提供31电平测试系统的精度-效率量化数据
- **Xu et al. 2015** "A Review of Efficient Modeling Methods for Modular Multilevel Converters" — 综述微秒级EMT精确模型（受控源通用提速模型、戴维南等效整体模型）和AVM方法，分析适用场景
- **IEEE Task Force 2013** — 提出401电平MMC测试系统作为AVM验证的IEEE标准基准

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 500" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="900" height="500" fill="#ffffff" rx="8"/>
  
  <!-- Title -->
  <text x="450" y="30" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" font-weight="bold" fill="#333">VSC-MMC测试系统建模方法体系</text>
  
  <!-- Input layer -->
  <rect x="30" y="60" width="140" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="100" y="85" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#2563eb" font-weight="bold">测试系统</text>
  <text x="100" y="100" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#2563eb">输入条件</text>
  
  <!-- Arrow from input -->
  <line x1="170" y1="85" x2="240" y2="85" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Modeling methods layer -->
  <!-- TDM -->
  <rect x="250" y="55" width="160" height="55" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="330" y="77" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#16a34a" font-weight="bold">TDM 详细模型</text>
  <text x="330" y="93" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#16a34a">1-5 μs步长 | 基准精度</text>
  
  <!-- DEM -->
  <rect x="250" y="130" width="160" height="55" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="330" y="152" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#16a34a" font-weight="bold">DEM 等效模型</text>
  <text x="330" y="168" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#16a34a">Schur补 | 310×加速</text>
  
  <!-- AM -->
  <rect x="250" y="205" width="160" height="55" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="330" y="227" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#d97706" font-weight="bold">AM 加速模型</text>
  <text x="330" y="243" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#d97706">受控源 | 混合方法</text>
  
  <!-- AVM -->
  <rect x="250" y="280" width="160" height="55" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="330" y="302" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#d97706" font-weight="bold">AVM 平均模型</text>
  <text x="330" y="318" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#d97706">100-1000 μs | 最高效率</text>
  
  <!-- Arrows from methods to output -->
  <line x1="410" y1="82" x2="550" y2="140" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="410" y1="157" x2="550" y2="140" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="410" y1="232" x2="550" y2="210" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="410" y1="307" x2="550" y2="280" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <!-- Output layer -->
  <rect x="560" y="130" width="160" height="55" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="640" y="152" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#7c3aed" font-weight="bold">精度评估</text>
  <text x="640" y="168" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#7c3aed">波形误差 &lt; 2%</text>
  
  <rect x="560" y="205" width="160" height="55" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="640" y="227" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#7c3aed" font-weight="bold">效率评估</text>
  <text x="640" y="243" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#7c3aed">加速比 10×–310×</text>
  
  <rect x="560" y="280" width="160" height="55" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="640" y="302" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#7c3aed" font-weight="bold">应用验证</text>
  <text x="640" y="318" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#7c3aed">故障/控制/稳定性</text>
  
  <!-- Application layer -->
  <line x1="720" y1="157" x2="790" y2="157" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="720" y1="232" x2="790" y2="232" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="720" y1="307" x2="790" y2="307" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  
  <rect x="800" y="140" width="80" height="140" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2" stroke-dasharray="4,2"/>
  <text x="840" y="165" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#dc2626" font-weight="bold">应用场景</text>
  <text x="840" y="182" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#dc2626">· 模型验证</text>
  <text x="840" y="198" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#dc2626">· 控制开发</text>
  <text x="840" y="214" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#dc2626">· HIL测试</text>
  <text x="840" y="230" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#dc2626">· 效率评估</text>
  <text x="840" y="246" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#dc2626">· 基准对比</text>
  
  <!-- Arrow marker -->
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  
  <!-- Legend -->
  <rect x="30" y="380" width="12" height="12" rx="2" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="48" y="391" font-family="Arial,sans-serif" font-size="10" fill="#666">输入/源</text>
  
  <rect x="100" y="380" width="12" height="12" rx="2" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="118" y="391" font-family="Arial,sans-serif" font-size="10" fill="#666">精确模型</text>
  
  <rect x="180" y="380" width="12" height="12" rx="2" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="198" y="391" font-family="Arial,sans-serif" font-size="10" fill="#666">近似/加速模型</text>
  
  <rect x="320" y="380" width="12" height="12" rx="2" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="338" y="391" font-family="Arial,sans-serif" font-size="10" fill="#666">评估输出</text>
  
  <rect x="420" y="380" width="12" height="12" rx="2" fill="#fee2e2" stroke="#dc2626" stroke-width="1"/>
  <text x="438" y="391" font-family="Arial,sans-serif" font-size="10" fill="#666">应用场景</text>
  
  <!-- Source citation -->
  <text x="450" y="440" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#999">来源：Gnanarathna 2011, Beddard 2015, Xu 2015, IEEE Task Force 2013</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · VSC-MMC测试系统建模方法体系架构</p>
