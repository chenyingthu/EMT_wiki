---
title: "EMTP / EMTP-RV"
type: entity
entity_type: tool
tags: [emtp, emtp-rv, polytechnique, simulation-tool]
created: "2026-04-13"
---

# EMTP / EMTP-RV

## 概述

EMTP（Electromagnetic Transients Program）是最经典的电力系统电磁暂态仿真程序。EMTP-RV是其最新版本，由加拿大蒙特利尔理工学院（Polytechnique Montreal）开发。

## 历史

- 起源于1960年代BPA和Dommel的工作
- 发展为开源的ATP版本
- EMTP-RV为商业增强版本

## 特点

- 强大的电力系统元件库
- 灵活的建模能力
- 频率相关网络等值
- 多速率仿真支持
- FLUX3D耦合（磁场有限元）

## 定义与边界

EMTP / EMTP-RV 在本 wiki 中作为 EMT 仿真工具与算法生态入口，而不是单一论文方法。页面应连接到 [[numerical-integration|数值积分]]、[[nodal-analysis|节点分析]]、[[state-space-method|状态空间方法]]、[[transmission-line-model|输电线路模型]]、[[transformer-model|变压器模型]]、[[vsc-model|VSC 模型]] 和 [[network-equivalent|网络等值]]，用于说明具体模型如何进入 Dommel 型时域求解。

其边界是工具平台本身不等于技术贡献。若来源只说明“使用 EMTP-RV 仿真”，还需要识别实际贡献是模型、积分器、接口、参数辨识还是验证工况；强非线性器件、宽频等值和实时移植还需要额外说明步长、无源性、初始化和接口延迟。

## 代表性来源与内部链接

代表性来源包括 [[creating-an-electromagnetic-transients-program-in-matlab-matemtp-power-delivery-|Creating an electromagnetic transients program in MATLAB]]、[[application-of-emtp-rv-graphic-software-of-electromagnetic-transient-simulation|Application of EMTP-RV graphic software of electromagnetic transient simulation]]、[[a-link-between-emtp-rv-and-flux3d-for-transformer-energization-studies|A link between EMTP-RV and FLUX3D for transformer energization studies]] 和 [[analysis-and-estimation-of-truncation-errors-in-modeling-complex-resonant-circui-fix|EMTP 截断误差分析]]。相关实体包括 [[polytechnique-montreal]]、[[mahseredjian]]、[[atp-emtp]] 和 [[pscad-emtdc]]。

## 相关实体
- [[polytechnique-montreal]]
- [[atp-emtp]]

## 深度增强内容

 基于您提供的116篇EMTP相关论文数据，以下是为**EMTP / EMTP-RV**方法页生成的深度增强内容。本文档采用方法页（Method）结构，系统梳理该电磁暂态仿真工具的核心算法、实现细节与工程应用准则。

---

## EMTP / EMTP-RV 深度技术文档

## 1. 核心原理详解

### 1.1 梯形积分伴随电路（Dommel算法基础）

EMTP的核心基于Dommel在1960年代提出的离散伴随电路（Companion Circuit）理论。对于电感元件，采用梯形积分（Trapezoidal Rule）离散化：

$$
v(t) = L\frac{di(t)}{dt} \Rightarrow v_n = \frac{2L}{\Delta t}i_n + \underbrace{\left(v_{n-1} + \frac{2L}{\Delta t}i_{n-1}\right)}_{I_{hist,L}}
$$

其中等效导纳$G_{eq} = \frac{\Delta t}{2L}$，历史电流源$I_{hist,L}$体现储能状态。整个网络在每一时步转化为纯电阻性节点电导方程：

$$
\mathbf{Y}_{bus}\mathbf{v}(t) = \mathbf{i}_{inj}(t) + \mathbf{I}_{hist}(t)
$$

### 1.2 开关与电力电子建模

**理想开关处理**：传统EMTP采用变导纳（Variable Admittance）方法，开关状态改变时$\mathbf{Y}_{bus}$需重分解。现代改进采用**关联单元模型（AUM）**或**状态变量消去法**，通过恒定导纳矩阵$\mathbf{Y}_n$与等效历史电流源实现：

$$
\mathbf{I}_{hist,sw} = f(\mathbf{x}_{state}, \mathbf{v}_{node})
$$

其中状态变量$\mathbf{x}_{state}$通过磁链-电流($\psi$-$i$)或电荷-电压关系反演更新，避免矩阵重分解，复杂度从$O(n^3)$降至$O(q^2)$（$q$为开关子系统阶数）。

**参数化平均值模型（PAVM）接口**：针对AC-DC变流器，PAVM通过线性化接口方程嵌入节点矩阵：

$$
\mathbf{Y}_{interface}\mathbf{v}_{dc} + \mathbf{P}(\alpha)\mathbf{v}_{ac} = \mathbf{I}_{eq}(\mathbf{x}_{state})
$$

消除传统接口的1步延迟（$\Delta t$），支持大步长（1000–2000 μs）稳定仿真。

### 1.3 频变参数与传输线模型

对于架空线路，EMTP采用**模态分解**或**相域直接计算**。相域模型通过状态方程近似传递矩阵$\mathbf{H}(s)$：

$$
\mathbf{H}(s) \approx \mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B} + \mathbf{D}
$$

实现最小实现阶数（Minimal Realization），避免每时步的模态变换。对于非均匀线路，采用指数变化假设$Z(x) = Z_0e^{qx}$，特征阻抗有理函数拟合在$10^2$–$10^6$ Hz范围内幅值偏差<1%。

### 1.4 饱和与磁滞非线性

基于Jiles-Atherton（J-A）理论的磁滞模型通过Type-94元件实现动态$\psi$-$i$特性：

$$
\frac{d\psi}{dt} = v(t) - R_{eq}i(t), \quad i = f_{JA}(\psi, \frac{d\psi}{dt}, M_s, a, \alpha, k, c)
$$

其中$M_s$为饱和磁化强度，$k$为磁畴壁钉扎系数。该模型在50Hz与150Hz下电流波形误差<5%，而简化模型在饱和区偏差达8–12%。

## 2. 算法流程

```mermaid
graph TD
    A[网络数据输入] --> B[拓扑分析与导纳矩阵构建]
    B --> C[初始条件计算: 潮流/稳态]
    C --> D[LU分解或稀疏矩阵预处理]
    D --> E[时步循环: t = t + Δt]
    E --> F[历史电流源更新 I_hist(t)]
    F --> G[开关状态检测与插值]
    G --> H[节点电压求解: Y·V = I_inj + I_hist]
    H --> I[支路电流与状态变量更新]
    I --> J{误差检查/变步长?}
    J -->|是| K[调整Δt: 满足截断误差<ε]
    J -->|否| L[输出存储]
    K --> E
    L --> M{t < T_end?}
    M -->|是| E
    M -->|否| N[仿真结束]
```

**关键步骤详解**：

1. **初始化**：通过稀疏技术对$\mathbf{Y}_{bus}$进行符号LU分解，确定填充元（fill-ins）位置。对于恒定导纳模型，此步骤仅执行一次。

2. **开关处理**：采用**插值算法**（Interpolation）消除开关动作时刻的数值振荡。当检测到开关状态改变发生在$t_{sw} \in (t-\Delta t, t)$时，回退至$t_{sw}$重新计算该步。

3. **变步长控制**（适用于 advanced versions）：基于局部截断误差（LTE）估计：
   $$
   \epsilon_{LTE} \approx \frac{\Delta t^2}{12} \left\|\frac{d^3\mathbf{x}}{dt^3}\right\|
   $$
   当$\epsilon_{LTE} > \epsilon_{max}$时，缩小步长；当系统处于机电暂态慢变阶段，步长可扩展至40–60 ms。

## 3. 参数选取指南

### 3.1 时间步长选择策略

| 仿真场景 | 推荐步长 | 理论依据 | 论文来源 |
|---------|---------|---------|---------|
| **电力电子开关细节** | 0.1–10 μs | 捕捉IGBT/GTO开关瞬态（μs级），预击穿电流持续数μs | 断路器模型(2024) |
| **电机与变压器饱和** | 10–100 μs | J-A模型需Δt<100μs保证数值稳定；VBR模型支持100μs步长误差<0.8% | 饱和模型(2018), VBR(2010) |
| **输电线路雷电/操作过电压** | 10–50 μs | 满足最高频率分量（MHz级）采样，截断误差<0.0004 p.u. | 截断误差(2002) |
| **宽频接地网分析** | 自适应 1 μs–1 ms | 覆盖20Hz–2MHz，阻抗跨越6个数量级 | 接地网(2019) |
| **机电暂态混合仿真** | 10–20 ms | 动态相量模型，SVC等效步长提升200–400倍 | 混合仿真(2009) |

### 3.2 积分方法配置

- **梯形法（Trapezoidal）**：默认方法，二阶精度，但可能引发数值振荡（Trapped Charge问题）。适用于大多数 RLC 网络。
- **后向欧拉（Backward Euler）**：引入数值阻尼，适用于：
  - 消除开关操作后的虚假振荡
  - 饱和电感初始化阶段
  - 与梯形法混合使用（HBDF2：Hybrid Backward Differentiation Formula）
  
  阻尼公式：
  $$
  \mathbf{v}_n = \frac{L}{\Delta t}(\mathbf{i}_n - \mathbf{i}_{n-1}) \Rightarrow G_{eq} = \frac{\Delta t}{L}, \quad \text{无振荡但精度降低为} O(\Delta t)
  $$

### 3.3 磁饱和分段线性化

对于变压器与电机，建议采用**10段分段线性**逼近饱和曲线：
- 拐点前：5段精细划分（0.8–1.0 p.u.）
- 拐点后：5段对数间隔（1.0–1.5 p.u.）
- 均方根误差（RMSE）<0.1%，导纳矩阵条件数稳定

## 4. 性能分析

### 4.1 计算效率对比

| 模型/算法 | 步长/配置 | 单步耗时 | 相对速度提升 | 误差指标 | 论文来源 |
|----------|----------|---------|-------------|---------|---------|
| **AVBR电机模型** | 500 μs | 1.9 μs | +126% (vs PD 4.3 μs) | 峰值误差<1.2% | VBR接口(2010) |
| **精确VBR** | 500 μs | 2.2 μs | +13.6% (vs AVBR) | 基准精度 | VBR接口(2010) |
| **状态变量消去法** | - | 195次操作 | 60% (vs NEM 488次) | 稳定临界步长112 μs | 状态消去(2025) |
| **Modelica变步长** | 平均168.9 μs | 112.6 s (总) | 10× (vs EMTP固定1 μs) | 误差范数0.64–0.77% | 异步机(2024) |
| **FPGA实时EMTP** | 12 μs | 12.5 ns时钟周期 | 实时 | 峰值误差<0.5%，相位<0.2° | FPGA-RT(2009) |
| **FPGA优化架构** | - | 166周期 | 9.8% (vs 184周期) | 资源减少53.5% (Slice Reg) | FPGA-Auto(2016) |
| **PAVM直接接口** | 1000–2000 μs | - | 消除迭代开销 | 无1步延迟 | PAVM(2022) |
| **混合仿真(SVC)** | 0.01–0.02 s | - | 200–400× (vs 50 μs EMT) | 波形一致 | 混合仿真(2009) |

### 4.2 内存与存储优化

**变步长线路模型**：
- 传统模型：存储$d = \lceil \tau/\Delta t \rceil$个历史值（如$\tau=1$ ms, $\Delta t=50$ μs时需20个向量）
- 改进模型：仅需存储1个前步历史向量，内存需求降低为$1/d$

**稀疏矩阵优化**：
- 采用符号分析预先分配存储，避免动态内存分配
- 对于含$N$个节点的网络，利用稀疏LU分解使操作数从$O(N^3)$降至$O(N^{1.2-1.5})$

## 5. 最佳实践与注意事项

### 5.1 开关与电力电子建模

1. **避免数值振荡**：
   - 使用**插值开关**（Interpolated Switching）而非整数倍步长开关
   - 对高频电力电子（>10 kHz），采用AUM或PAVM替代理想开关，避免导纳矩阵每步重分解

2. **拓扑切换稳定性**：
   - 当使用Type-96非线性电感时，必须设置$Z_{emtp} > 10^{-6}$ Ω，防止矩阵条件数>$10^{12}$导致发散
   - 对于VSC模型，直流电容储能时间常数$\tau = C_{DC}E_{DC}^2/S_{rated}$应≥0.5 s以保证控制稳定性

### 5.2 变压器与磁路

1. **饱和特性初始化**：
   - 避免直接使用制造商空芯电感估算$L_{sat}$（可能高估15.1%），建议通过投切暂态测量辨识（误差可降至0.6%）
   - 剩磁>80%饱和磁通时，CT二次电流传变误差可达60–80%，持续3–5个周波，保护整定需考虑此偏差

2. **铁磁谐振预防**：
   - 采用J-A动态模型而非单值特性曲线，可识别2–3个额外谐振工作点
   - 避雷器MOV可将铁磁谐振过电压限制在设定水平（如110 kV降至62 kV，削减43.4%），并在2个周波内耗散能量

### 5.3 线路与接地系统

1. **频变参数选取**：
   - 对于雷电/VFTO研究（>100 kHz），必须采用频变土壤模型（考虑介电常数20–100），纯电阻接地模型导致地电位升（GPR）误差18–25%
   - 土壤频变特性可使接地冲击阻抗降低12–20%，反击跳闸率下降约15%

2. **长线路仿真**：
   - 步长必须满足$\Delta t < \tau_{min}$（最小传播时延），对于100 km线路约<330 μs
   - 非均匀线路（如阻抗从220 Ω指数变化至150 Ω，$q=-0.00766$）避免采用级联均匀段模型，采用指数模型可减少状态变量数量

### 5.4 实时与离线移植

1. **代数环处理**：
   - 离线加速初始化技巧（如预测-校正）直接移植至实时环境会导致数十秒至分钟级的数值漂移，必须剔除或重构为显式积分
   - 引入1步延时（One-step delay）可确保实时求解器计算时间确定性，控制信号响应延迟严格控制在1个仿真步长内

2. **模型一致性验证**：
   - 离线与实时工具采用相同模型结构、参数设置、解耦策略与数值阻尼时，仿真结果误差应为0%，波形完全重合（验证基准）

## 6. 与其他方法的对比

### 6.1 EMTP vs EMTDC/PSCAD

| 特性 | EMTP / EMTP-RV | EMTDC/PSCAD |
|------|----------------|-------------|
| **数值核心** | 稀疏矩阵节点法，支持变步长 | 固定步长节点法，基于Dommel理论 |
| **电机模型** | 原生支持VBR/AVBR，相域直接接口 | 主要基于dq0旋转坐标系 |
| **电力电子** | PAVM、AUM等高级接口，支持大步长 | 详细开关级模型为主 |
| **线路模型** | 丰富的频变模型（Jmarti, Noda, 相域） | 支持频变，但相域实现较少 |
| **磁滞建模** | J-A理论，Type-94元件 | 简化磁滞或查表法 |
| **开源生态** | ATP版本开源，RV为商业版 | 商业软件，模型库丰富 |
| **适用场景** | 学术研究、高精度离线分析、算法验证 | 工程应用、控制设计、教学 |

### 6.2 离线EMTP vs 实时仿真（HYPERSIM/RTDS）

| 维度 | 离线EMTP | 实时EMTP (FPGA/CPU) |
|------|---------|-------------------|
| **步长限制** | 可自适应（1 μs–20 ms） | 严格固定（通常12–100 μs） |
| **网络规模** | 支持>10,000节点（1666母线/6180节点验证） | 受硬件资源限制，需模型降阶 |
| **开关处理** | 插值、变导纳精确捕捉 | 需AUM或PAVM避免超实时 |
| **精度验证** | 基准参考 | 与离线误差<0.5%（FPGA实现） |
| **应用场景** | 详细设计、参数扫描 | HIL测试、保护闭环验证 |

### 6.3 电磁暂态(EMTP) vs 动态相量(Dynamic Phasor)

| 指标 | EMTP全波 | 动态相量混合 |
|------|---------|-------------|
| **步长范围** | 1–100 μs | 10–20 ms（提升200–400倍） |
| **谐波捕捉** | 全频域（至MHz） | 基波+选定谐波（如1次+5次） |
| **适用器件** | 高频开关、线路分布参数 | SVC、HVDC等慢变动态 |
| **接口误差** | 无 | 需专门接口算法消除相位不连续 |
| **最佳实践** | 精细暂态分析 | 大电网中长期动态，机电-电磁混合 |

### 6.4 数值方法对比（积分器选择）

| 方法 | 精度阶数 | 数值稳定性 | 适用场景 |
|------|---------|-----------|---------|
| **梯形法** | 2阶 | 条件稳定（潜在振荡） | 通用RLC网络，避免纯感性割集 |
| **后向欧拉** | 1阶 | 绝对稳定（强阻尼） | 消除开关振荡，饱和初始化 |
| **HBDF2** | 2阶 | 混合阻尼 | 电力电子变拓扑，抑制虚假振荡 |
| **变步长BDF** | 自适应 | 刚性稳定 | 长过程仿真，电机启动等 |

---

**参考文献**：本文档技术细节基于所提供的116篇EMTP相关论文数据，涵盖1960年代经典理论至2025年最新进展，包括Polytechnique Montreal的EMTP-RV开发团队、IEEE Transactions on Power Delivery及EMTP社区的核心研究成果。
