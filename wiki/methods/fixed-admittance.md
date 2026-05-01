---
title: "恒导纳模型 (Fixed Admittance / ADC Model)"
type: method
tags: [fixed-admittance, adc, real-time, companion-circuit]
created: "2026-04-13"
---

# 恒导纳模型 (Fixed Admittance / ADC Model)

## 定义与概述

恒导纳模型（Fixed Admittance Model）也常被称为关联离散电路模型（Associated Discrete Circuit, ADC）。它通过伴随电路和等效历史源把开关器件、桥臂模块或局部子网络表示为导纳矩阵不随开关状态改变的模型。开关动作只改变右端注入项或历史源，从而避免每次拓扑变化都重新组装和分解网络矩阵。

该方法主要服务于含大量开关器件的 EMT 仿真，尤其是实时仿真、FPGA/CPU 异构仿真、MMC 桥臂等效和电力电子变换器快速模型。

## 作用机制

常规详细开关模型会随导通/关断状态改变网络拓扑，导致导纳矩阵频繁变化。恒导纳模型的关键做法是：

$$
i_k=Y_{\mathrm{fix}}v_k+i_{\mathrm{hist}}(s_k,x_{k-1})
$$

其中 $Y_{\mathrm{fix}}$ 在开关状态 $s_k$ 改变时保持不变，开关动作和历史状态被转移到右端历史源 $i_{\mathrm{hist}}$。这样主网络矩阵可重复使用，但必须检查历史源构造是否引入虚拟损耗或状态误差。

- 为开关状态构造共享的等效导纳，使主网络矩阵在仿真过程中保持不变。
- 把开关状态、历史电压电流和控制量的影响放入等效电流源或历史源。
- 在初始化阶段完成矩阵组装和分解，后续时步主要执行右端项更新与前代/回代。
- 对桥臂、半桥腿或子模块进行分组等效，减少端口数量和全局耦合。
- 在需要保持开关时刻精度时，配合插值、分数步长或局部修正控制虚拟损耗。

恒导纳模型与 [[numerical-integration|数值积分]] 紧密相关：积分公式决定动态元件的伴随导纳和历史源形式；与 [[nodal-analysis|节点分析法]] 结合时，它的主要收益来自矩阵重复利用。

## 适用边界

- 适合开关数量多、拓扑变化频繁、矩阵分解成本占主导的电力电子 EMT 仿真。
- 适合实时仿真和硬件在环，因为固定矩阵更容易满足确定性计算时间。
- 若研究目标是器件级开关损耗、极短时标过电压或保护动作临界时刻，应检查恒导纳等效和插值策略是否保留足够细节。
- 固定导纳构造可能引入虚拟损耗、接口延迟或条件数问题，需要通过能量误差、波形对比和极端工况验证。
- 对强非线性器件或状态依赖参数，通常需要局部迭代、分段线性化或混合模型，而不是把所有元件都强行纳入同一个固定矩阵。

## 代表性来源

| 论文 | 年份 | 关联要点 |
|------|------|----------|
| [[a-bridge-arm-module-based-fixed-admittance-adc-model-for-converters-in-emt-simul|A Bridge-Arm-Module-Based Fixed-Admittance ADC Model for Converters in EMT Simulation]] | 2025 | 面向变流器桥臂模块的固定导纳 ADC 建模。 |
| [[su-等-a-fixed-admittance-algorithm-for-the-fpga-based-microsecond-level-nonlinear|Su 等：A fixed-admittance algorithm for the FPGA-based microsecond-level nonlinear EMT simulation]] | 2025 | 面向 FPGA 微秒级实时仿真的恒导纳算法。 |
| [[analytical-modeling-of-the-half-bridge-leg-using-an-associated-discrete-circuit-|Analytical Modeling of the Half-Bridge Leg Using an Associated Discrete Circuit]] | 2026 | 以 ADC 形式解析建模半桥腿。 |
| [[a-state-variables-elimination-based-emtp-type-constant-admittance-equivalent-mod|A State-Variables-Elimination-Based EMTP-Type Constant-Admittance Equivalent Model]] | 2024 | 通过状态变量消元构造恒导纳等效。 |
| [[unified-high-speed-emt-equivalent-and-implementation-method-of-mmcs-with-single-|Unified high-speed EMT equivalent and implementation method of MMCs]] | 2024 | 将恒定矩阵思想用于 MMC 高速等效。 |

## 相关方法
- [[nodal-analysis|节点分析法]] - 恒导纳模型的求解框架
- [[numerical-integration|数值积分]] - 决定伴随导纳形式
- [[switch-modeling|开关建模方法]] - 恒导纳开关等效
- [[sparse-matrix-solver|稀疏矩阵求解]] - 固定矩阵的重复利用
- [[interpolation-method|插值方法]] - 开关时刻精度修正
- [[fpga-real-time-simulation|FPGA实时仿真]] - 恒导纳的实时应用

## 相关模型
- [[mmc-model|MMC 模型]] - 恒导纳的主要应用场景
- [[vsc-model|VSC 模型]] - VSC桥臂恒导纳等效
- [[igbt-model|IGBT 模型]] - 开关器件恒导纳模型
- [[converter-transformer-model|换流变压器]] - 变压器恒导纳接口

## 相关主题
- [[real-time-simulation|实时仿真]] - 恒导纳的主要应用场景
- [[parallel-computing|并行计算]] - 固定矩阵利于并行化
- [[electromechanical-electromagnetic-hybrid-simulation|机电-电磁混合仿真]] - 恒导纳用于混合接口

## 技术演进脉络

### 2020年 (基础方法探索)
- **Simulation of electromagnetic transients with Modelica (2020)**
  - 💡 探索基于Modelica语言的电磁暂态仿真方法，为恒导纳模型的系统化建模奠定基础
  - 验证了不同数值积分方法对恒导纳实现的影响
- **适用于电磁暂态仿真的变阶变步长3S-DIRK算法 (2020)**
  - 💡 提出L稳定的多步法，为恒导纳模型提供稳定的数值积分基础
  - 通过恒定等效导纳实现矩阵复用，降低计算开销

### 2022年 (方法深化与应用扩展)
- **一种用于电磁暂态仿真的两电平VSC解耦模型 (2022)**
  - 💡 提出基于半隐式延迟解耦的恒导纳建模方法，利用桥臂互斥导通特性实现恒定等效电导
  - 等效电导 $G_{eq} = \frac{1}{R_{on}+R_{off}} \approx 0$，不随开关状态变化
- **模块化多电平换流器电磁暂态模型研究综述 (2022)**
  - 💡 系统梳理了MMC恒导纳等效建模方法，总结了戴维南等效与恒导纳技术的结合
- **计及电容过渡过程的双钳位型MMC电磁暂态高效仿真方法 (2022)**
  - 💡 将恒导纳思想应用于复杂CDSM-MMC拓扑，实现闭锁与解锁全状态的恒定导纳矩阵仿真

### 2023年 (FPGA异构实时仿真)
- **基于CPU-FPGA异构平台的虚拟同步并网逆变器实时仿真算法设计 (2023)**
  - 💡 将恒导纳模型应用于FPGA实时仿真，利用固定导纳矩阵确定性计算时间的特点
  - 实现微秒级步长的实时仿真
- **一种级联H桥型电力电子变压器电磁暂态解耦与仿真模型 (2023)**
  - 💡 提出级联H桥PET的恒导纳解耦方法，通过内部节点收缩降低矩阵维度

### 2024-2025年 (前沿发展)
- **A State-Variables-Elimination-Based EMTP-Type Constant-Admittance Equivalent Model (2024)**
  - 💡 通过状态变量消元构造恒导纳等效，实现高精度与高效率的统一
- **Unified high-speed EMT equivalent and implementation method of MMCs (2024)**
  - 💡 将恒定矩阵思想系统应用于MMC高速等效，支持任意单端口子模块拓扑
- **Su等: A fixed-admittance algorithm for FPGA-based microsecond-level EMT simulation (2025)**
  - 💡 专门针对FPGA异构平台优化的恒导纳算法，实现微秒级非线性EMT仿真
  - 利用恒定导纳矩阵特性实现确定性并行计算
- **Universal Decoupled Equivalent Circuit Models of Solid-State Transformer (2025)**
  - 💡 将恒导纳方法扩展至固态变压器，实现多级AC/DC/DC/AC变换器的高效仿真

### 2026年 (最新进展)
- **Analytical Modeling of the Half-Bridge Leg Using an Associated Discrete Circuit (2026)**
  - 💡 以ADC形式解析建模半桥腿，从理论上完善恒导纳模型的数学基础
- **A Bridge-Arm-Module-Based Fixed-Admittance ADC Model (2025+)**
  - 💡 面向变流器桥臂模块的固定导纳ADC建模，支持模块化多电平拓扑

## 关键发现汇总

### 核心优势验证
- **[2020-2022]** 恒导纳模型通过固定导纳矩阵 $G_{fix}$ 避免了每步长的LU分解重构，计算复杂度从 $O(N^3)$ 降至 $O(N)$，对于大规模MMC系统可实现数十倍至数百倍加速
- **[2022]** 基于半隐式延迟解耦的恒导纳模型实现交直流侧解耦，导纳矩阵恒定不变，计算速度提升显著

### 数值稳定性
- **[2020]** L稳定的3S-DIRK算法(λ=0.42265/0.29289)与恒导纳模型结合，可有效抑制数值振荡，同时保持A-稳定性
- **[2022]** 恒导纳模型配合后退欧拉法离散化，具有A-稳定性，适合刚性系统

### 实时仿真适用性
- **[2023-2025]** FPGA异构平台利用恒导纳模型的确定性计算时间特性，实现微秒级步长(1-10μs)的实时仿真
- **[2025]** 单芯片FPGA可实现542节点系统的实时仿真，逻辑单元占用41%，乘法器占用56%

### 虚拟损耗问题
- **[2019-2020]** 经典AEM/AVM模型通过控制框图实现时可能产生单步延迟，导致虚假功率损耗
- **[2022+]** 解决方案包括即时联立求解、直接接口方法(DI-AVM)消除延迟，确保功率守恒

## 深度增强内容

### 1. 恒导纳模型数学原理

#### 1.1 基础ADC模型

关联离散电路(ADC)的核心方程：

$$
i_k(t) = Y_{fix} \cdot v_k(t) + i_{hist}(t-\Delta t, s_k, x_{k-1})
$$

其中：
- $Y_{fix}$: 恒定导纳（不随开关状态变化）
- $i_{hist}$: 历史电流源（包含开关状态和历史信息）
- $s_k$: 开关状态
- $x_{k-1}$: 上一时步状态变量

**导纳恒定化原理**：
利用桥臂互斥导通特性，等效电导与电阻满足：
$$
G_{eq} = \frac{1}{R_{on} + R_{off}} \approx 0, \quad R_{eq} = \frac{R_{on}R_{off}}{R_{on} + R_{off}} \approx R_{on}
$$

由于 $G_{eq} \approx 0$ 不随开关状态变化，系统导纳矩阵保持恒定。

#### 1.2 半隐式延迟解耦

针对大规模交直流系统，采用半隐式延迟插入法(LIM)实现解耦：

**半步时延技术**：
$$
\mathbf{V}_{dc}(t) = f(\mathbf{I}_{ac}(t - \Delta t/2))
$$
$$
\mathbf{I}_{ac}(t) = g(\mathbf{V}_{dc}(t - \Delta t/2))
$$

交直流侧状态变量更新引入 $\Delta t/2$ 延迟，实现恒定导纳矩阵。

#### 1.3 MMC戴维南等效恒导纳模型

基于梯形积分的子模块戴维南等效：

$$
R_{eq} = \frac{2C_{SM} - \Delta t/R_{on}}{2C_{SM} + \Delta t/R_{on}} \cdot R_{on} \approx \frac{\Delta t}{2C_{SM}}
$$

**桥臂聚合**：
将 $N$ 个子模块等效为单一戴维南电路：
$$
R_{arm}^{eq} = \sum_{j=1}^{N} R_{eq,j}, \quad v_{arm}^{th} = \sum_{j=1}^{N} v_{th,j}
$$

**加速策略**：
正常运行时导纳矩阵 $G_{net}$ 保持恒定，仅在闭锁/解锁时更新：
$$
G_{net} \cdot V_{node} = I_{inj}
$$

### 2. 仿真参数参考表

| 参数类别 | 参数名称 | 典型值/范围 | 单位 | 备注 |
|---------|---------|------------|------|------|
| **开关器件** | 导通电阻 $R_{on}$ | 0.001 - 0.01 | Ω | IGBT典型值 |
| | 关断电阻 $R_{off}$ | $10^6$ | Ω | 理想开关近似 |
| | 开关频率 $f_{sw}$ | 1980 - 2000 | Hz | 两电平VSC |
| **MMC特定** | 子模块电容 $C_{SM}$ | 4 - 10 | mF | 电压波动±10% |
| | 桥臂电感 $L_{arm}$ | 50 - 200 | mH | 限流与环流抑制 |
| **仿真设置** | 详细模型步长 | 1 - 10 | μs | 需频繁矩阵重构 |
| | 恒导纳模型步长 | 10 - 50 | μs | 矩阵恒定，仅更新右端项 |
| | FPGA实时步长 | 1 - 10 | μs | 确定性计算时间 |
| | CPU-GPU并行步长 | 20 - 50 | μs | 数据映射开销需考虑 |
| **数值积分** | 梯形法(TR) | α=0 | - | A稳定，$O(\Delta t^3)$精度 |
| | 后退欧拉(BE) | α=1 | - | L稳定，强阻尼 |
| | 混合积分 | α∈[0,1] | - | 开关时刻切换至BE |

### 3. 算法流程

#### 阶段一：初始化（一次性）
1. **拓扑分析**：识别独立节点，建立节点-支路关联矩阵
2. **恒导纳构造**：计算各元件等效导纳 $Y_{fix}$
3. **矩阵组装**：构建节点导纳矩阵 $Y_n = A_a Y_b A_a^T$
4. **稀疏LU分解**：$Y_n = LU$（仅执行一次）

#### 阶段二：时步迭代（每时步）
1. **历史源更新**：
   - 电感：$I_{hist,L}(t) = i_L(t) + \frac{\Delta t}{2L} v_L(t)$
   - 电容：$I_{hist,C}(t) = -i_C(t) - \frac{2C}{\Delta t} v_C(t)$
   - 开关：根据状态 $s_k$ 更新等效历史源

2. **右端项组装**：$j_{total} = j_{inj} + j_{hist}(t-\Delta t)$

3. **前代/回代求解**：$V = (LU)^{-1} j_{total}$
   - 计算复杂度：$O(N)$（稀疏矩阵）

4. **状态更新**：计算支路电流、元件状态，为下一时步准备

### 4. 硬件平台实现对比

| 平台类型 | 典型步长 | 节点规模 | 恒导纳支持 | 性能特点 |
|---------|---------|---------|-----------|---------|
| **CPU串行** | 20-50 μs | 1000+节点 | ✅ 全支持 | 矩阵单次分解，后续仅前代/回代 |
| **FPGA** | 1-10 μs | 542节点 | ✅ 最优 | 确定性延迟，流水线并行 |
| **CPU-GPU异构** | 20-50 μs | 3000+子模块 | ⚠️ 传输瓶颈 | NMS数据映射减少传输量 |
| **RTDS** | 20-50 μs | 单机架~100节点 | ✅ 实时 | 硬实时约束，固定步长 |

### 5. 模型选择指南

| 应用场景 | 推荐方法 | 步长建议 | 关键考量 |
|---------|---------|---------|---------|
| **大规模MMC离线仿真** | 恒导纳DEM | 10-20 μs | 矩阵恒定，3000+子模块可行 |
| **实时仿真/HIL测试** | ADC固定导纳 | 1-10 μs | FPGA实现，确定性延迟 |
| **电力电子变压器** | 恒导纳+解耦 | 5-20 μs | 高频开关(1-20kHz)，内部节点收缩 |
| **构网型变换器** | 恒导纳DI-AVM | 20-50 μs | 虚拟惯量建模，大步长稳定 |
| **直流故障分析** | 恒导纳+开关插值 | 10-20 μs | 闭锁状态精确模拟 |

### 6. 前沿研究方向

#### 6.1 异构并行加速
- **FPGA流水线优化**：利用恒导纳矩阵确定性计算特性，实现桥臂级并行
- **CPU-GPU任务分配**：电磁计算在GPU，控制保护在CPU，恒导纳矩阵简化数据传输

#### 6.2 新型拓扑适配
- **混合MMC(CH-MMC)**：半桥/全桥混合拓扑的恒导纳建模，支持故障自清除
- **固态变压器(SST)**：多级AC/DC/DC/AC变换器的恒导纳等效

#### 6.3 虚拟损耗消除
- **即时联立求解**：消除单步延迟，实现与详细模型一致的功率守恒
- **Pejovic修正模型**：针对小步长限制(32.55μs)的阻尼修正

#### 6.4 多物理场耦合
- **电热联合仿真**：恒导纳模型与器件级热模型耦合，结温计算误差<2°C
- **电-机-热统一仿真**：将机械慢动态纳入恒导纳框架

### 7. 最佳实践与注意事项

#### 7.1 虚拟损耗控制
恒导纳模型中常见的虚拟损耗来源及解决方案：

| 损耗类型 | 产生原因 | 解决方案 | 验证方法 |
|---------|---------|---------|---------|
| **单步延迟损耗** | 受控源接口一步延迟 | 直接接口方法（DI） | 功率守恒检查 |
| **插值误差** | 开关时刻线性插值 | 精确开关时刻检测 | 能量误差<0.1% |
| **数值阻尼** | 后退欧拉法固有阻尼 | 梯形法/混合积分 | 与详细模型对比 |
| **矩阵条件数** | 导纳矩阵病态 | 预条件处理 | 条件数<10^12 |

#### 7.2 步长选择策略
- **详细分析**：1-10 μs（捕捉开关细节）
- **系统级仿真**：20-50 μs（平衡精度与效率）
- **实时仿真**：1-10 μs（FPGA确定性约束）
- **大步长验证**：验证恒导纳模型在大步长下的稳定性

#### 7.3 模型验证清单
- [ ] 稳态功率守恒验证
- [ ] 暂态波形与详细模型对比
- [ ] 直流故障穿越能力验证
- [ ] 开关频率响应验证
- [ ] 能量误差累计检查

## 来源论文

| 论文 | 年份 |
|------|------|
| [[simulation-of-electromagnetic-transients-with-modelica-accuracy-and-performance-|Simulation of electromagnetic transients with Modelica, accu]] | 2020 |
| [[适用于电磁暂态仿真的变阶变步长3s-dirk算法|适用于电磁暂态仿真的变阶变步长3S-DIRK算法]] | 2020 |
| [[一种用于电磁暂态仿真的两电平电压源型换流器解耦模型|一种用于电磁暂态仿真的两电平电压源型换流器解耦模型]] | 2022 |
| [[中-国-电-机-工-程-学-报-34|中  国  电  机  工  程  学  报]] | 2022 |
| [[中-国-电-机-工-程-学-报|中  国  电  机  工  程  学  报]] | 2022 |
| [[模块化多电平换流器电磁暂态模型研究综述|模块化多电平换流器电磁暂态模型研究综述]] | 2022 |
| [[计及电容过渡过程的双钳位型mmc电磁暂态高效仿真方法|计及电容过渡过程的双钳位型MMC电磁暂态高效仿真方法]] | 2022 |
| [[一种级联h桥型电力电子变压器电磁暂态解耦与仿真模型|一种级联H桥型电力电子变压器电磁暂态解耦与仿真模型]] | 2023 |
| [[基于cpu-fpga异构平台的虚拟同步并网逆变器实时仿真算法设计|基于CPU-FPGA异构平台的虚拟同步并网逆变器实时仿真算法设计]] | 2023 |
| [[su-等-a-fixed-admittance-algorithm-for-the-fpga-based-microsecond-level-nonlinear|Su 等 | A fixed-admittance algorithm for the FPGA-based micro]] | 2025 |
| [[universal-decoupled-equivalent-circuit-models-of-solid-state-transformer-for-acc|Universal Decoupled Equivalent Circuit Models of Solid-State]] | 2025 |
| [[中-国-电-机-工-程-学-报-37|中  国  电  机  工  程  学  报]] | 2025 |
| [[rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability|RMS&#x002B;: Augmenting the Traditional Circuit Model to Cap]] | 2026 |