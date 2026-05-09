---
title: "模块化多电平换流器(MMC)建模 (Modular Multilevel Converter Modeling)"
type: topic
tags: [mmc, hvdc, converter-modeling, average-value-model, detailed-equivalent-model, sub-module]
created: "2026-05-01"
book-chapter: "8"
---

# 模块化多电平换流器(MMC)建模 (Modular Multilevel Converter Modeling)


```mermaid
graph TD
    subgraph Ncmp[模块化多电平换流器(MMC)建模 (Modular Mu…]
        N0[半桥(HBSM): 2开关+电容]
        N1[全桥(FBSM): 4开关+电容]
        N2[箝位双子模块(CDSM): 4开关+2电容]
    end
```


## 概述

模块化多电平换流器（Modular Multilevel Converter, MMC）是当前高压直流输电（HVDC）和柔性交流输电系统（FACTS）的主流拓扑。由多个子模块（Sub-Module, SM）级联构成桥臂，具有模块化、可扩展、输出波形谐波含量低、开关损耗小等优势，已成为远距离大容量输电、海上风电并网、城市电网供电等场景的首选技术。

在EMT语境下，MMC建模面临独特挑战：单端换流器可能包含数百个子模块，每个子模块含2-4个IGBT/二极管开关器件，若采用详细开关模型，计算量将呈指数级增长。因此，MMC建模的核心问题是如何在保持足够精度的同时，将大规模开关网络等效为可高效求解的电路形式。从2010年提出的时变戴维南等效方法到2020年代的自适应多模型框架，MMC建模技术已成为EMT仿真领域研究最活跃的方向之一。

## 作用机制

### 8.1 MMC拓扑结构

**基本结构**

三相六桥臂拓扑，每相含上、下两个桥臂：

$$
\text{每相: } \begin{cases}
v_{dc} = v_{u} + v_{l} \\
i_{ph} = i_{u} - i_{l}
\end{cases}
$$

**子模块类型**

| 类型 | 拓扑 | 电压范围 | 直流故障能力 |
|------|------|---------|-------------|
| 半桥(HBSM) | 2开关+电容 | 0, $v_C$ | 无自清除能力 |
| 全桥(FBSM) | 4开关+电容 | -$v_C$, 0, $v_C$ | 可闭锁清除故障 |
| 箝位双子模块(CDSM) | 4开关+2电容 | 多电平输出 | 有故障能力 |

**关键状态变量**
- 桥臂电流 $i_{arm}$（含基频分量与二倍频环流）
- 子模块电容电压 $v_{C,j}$（$j=1,2,...,N$）
- 投入子模块数 $n_{on}(t) \in [0, N]$

### 8.2 详细开关模型

**单个子模块动态**（以半桥为例）

开关函数 $S_j \in \{0, 1\}$：

$$
C_{SM} \frac{dv_{C,j}}{dt} = S_j \cdot i_{arm}
$$

$$
v_{SM,j} = S_j \cdot v_{C,j} + (1-S_j) \cdot 0
$$

**桥臂电压**：
$$
v_{arm} = \sum_{j=1}^{N} v_{SM,j} = \sum_{j=1}^{N} S_j \cdot v_{C,j}
$$

**计算复杂度**：
- 每个子模块2-4个开关状态
- 导纳矩阵维度：$O(N)$
- 每步需重新因子化：$O(N^3)$

**适用场景**：器件级分析、损耗计算、阀控验证

### 8.3 平均值模型(AVM)

**桥臂平均电压**

忽略开关纹波，用受控电压源表征：

$$
\bar{v}_{arm} = n_{on} \cdot \bar{v}_{C}^{arm}
$$

其中 $n_{on} \in [0,N]$ 为投入子模块数，$\bar{v}_{C}^{arm}$ 为桥臂平均电容电压。

**电容电压动态**（集中等效）：

$$
N \cdot C_{SM} \frac{d\bar{v}_{C}^{arm}}{dt} = n_{on} \cdot i_{arm}
$$

**环流动力学**（二倍频分量）：

$$
L_{arm} \frac{di_{circ}}{dt} + R_{arm}i_{circ} = \frac{V_{dc}}{2} - \frac{\bar{v}_{u} + \bar{v}_{l}}{2}
$$

**增强型平均值模型(EAVM)**

引入桥臂电流初始化补偿，解决闭锁工况建模问题：

$$
i_{arm}(t^+) = i_{arm}(t^-) \cdot \frac{L_{arm}}{L_{arm} + L_{eq}}
$$

**特点**：
- 计算效率提升20-100倍
- 步长可放宽至10-100μs
- 适用于系统级暂态分析

### 8.4 详细等效模型(DEM)

**时变戴维南等效**（梯形积分法）

将子模块群聚合成时变等效电路：

$$
\begin{aligned}
R_{eq} &= \frac{2C_{SM}R_{on} + \Delta t}{2C_{SM} + \Delta t/R_{on}} \approx \frac{\Delta t}{2C_{SM}} \\
v_{th} &= \frac{2C_{SM} - \Delta t/R_{on}}{2C_{SM} + \Delta t/R_{on}} \cdot v_{C}(t-\Delta t) + R_{eq} \cdot i_{arm}(t)
\end{aligned}
$$

**桥臂聚合**：

将$N$个子模块等效为单一戴维南电路：

$$
R_{arm}^{eq} = \sum_{j=1}^{N} R_{eq,j}, \quad v_{arm}^{th} = \sum_{j=1}^{N} v_{th,j}
$$

**嵌套快速求解(GENE方法)**

枚举子模块开关状态组合，预存LU分解结果：
- 正常运行：$2^N$种状态（不可行）
- 实用简化：按投入数量$n_{on}$分档（$N+1$种）
- 查表时间：<1μs

**加速策略**（恒定导纳矩阵）

正常运行时导纳矩阵$G_{net}$保持恒定，仅在闭锁/解锁时更新：

$$
G_{net} \cdot V_{node} = I_{inj}
$$

**性能**：
- 精度与详细模型一致（误差<0.1%）
- 计算速度提升30-60倍（全桥拓扑提升更显著）
- 适用于直流故障分析、保护设计

### 8.5 桥臂等效模型(AEM)

**诺顿等效**（简化DEM）

将桥臂等效为诺顿电路：

$$
i_{inj} = G_{eq} \cdot v_{arm} + I_{hist}
$$

其中等效电导$G_{eq}$在时步内恒定。

**虚假功率问题**

经典AEM可能因控制模块实现产生非物理损耗：

$$
\Delta P(t) = P_{arm}(t) - P_{Ctot}(t)
$$

**解决方案**：
- 即时联立求解（与网络方程同时解算）
- 可变电阻模型
- 避免单步延迟

### 8.6 动态相量与多速率模型

**动态相量模型**

适用于机电暂态混合仿真，保留关键谐波分量：

$$
\langle v \rangle_0 = f(\langle i \rangle_0, \langle i \rangle_2, \langle v_C \rangle_0, \langle v_C \rangle_2)
$$

**10阶模型**：基频+二倍频
**2阶降阶模型**：仅保留慢变模态

**多速率协同仿真**

- 交流网络：大步长（ms级）
- MMC内部：小步长（μs级）
- 接口：时变戴维南/诺顿等效

### 8.7 自适应多模型框架

**模型层次**

| 模型 | 精度 | 效率 | 适用工况 |
|------|------|------|---------|
| DSM | 基准 | 1x | 器件级分析 |
| DEM | >99.9% | 30-60x | 故障暂态 |
| EAVM | >99% | 50-100x | 正常稳态 |
| 机电模型 | >95% | 200x | 系统级稳定 |

**自适应切换策略**

基于暂态严重程度自动选择模型：

```
if (|di/dt| > threshold):
    model = DEM    # 严重故障
elif (|v_err| > limit):
    model = AEM    # 电压偏差大
else:
    model = EAVM   # 正常运行
```

切换冲击<0.1%，实现全工况高效仿真。

---

## 适用边界

- DSM仅适用于少量子模块（N<50），大规模MMC必须使用等效模型
- AVM在直流故障、闭锁工况下精度不足，需用EAVM或DEM
- DEM的恒定导纳策略在正常工况高效，但闭锁时需重新因子化
- 虚假功率问题在经典AEM中显著，需采用联立求解或改进实现
- 机电暂态模型仅适用于低频振荡分析，不适用于开关暂态

---

## 代表性来源

| 论文 | 年份 | 关联要点 |
|------|------|----------|
| [[efcient-modeling-of-modular-multilevel-hvdc-15]] | 2010 | 时变戴维南等效，2770倍加速 |
| [[modular-multilevel-converter-models]] | 2013 | 开关函数原理，改进AVM |
| [[ahmed-等-a-computationally-efficient-continuous-model-for-the-modular-multilevel-]] | 2014 | 连续等效模型，阻塞状态 |
| [[a-review-of-efficient-modeling-methods-for-modular-multilevel-converters]] | 2015 | 模型分类与对比 |
| [[模块化多电平换流器戴维南等效整体建模方法]] | 2015 | 戴维南整体模型，后退欧拉离散 |
| [[improved-accuracy-average-value-models-of-modular-multilevel-converters]] | 2016 | 高精度AVM |
| [[a-dynamic-phasor-model-of-an-mmc-with-extended-frequency-range-for-emt-simulatio]] | 2018 | 扩展频域动态相量 |
| [[an-enhanced-average-value-model-of-modular-multilevel-converter-for-accurate-rep]] | 2018 | 闭锁工况EAVM |
| [[high-speed-emt-modeling-of-mmcs-with-arbitrary-multiport-submodule-structures-us]] | 2018 | 多端口子模块通用模型 |
| [[spurious-power-losses-in-modular-multilevel-converter-arm-equivalent-model]] | 2019 | 虚假功率问题揭示 |
| [[adaptive-modular-multilevel-converter-model-for-electromagnetic-transient-simula]] | 2020 | 自适应多模型框架 |
| [[an-accelerated-detailed-equivalent-model-for-modular-multilevel-converters]] | 2023 | 仅闭锁更新导纳矩阵 |
| [[generalized-electromagnetic-transient-equivalent-modeling-and-implementation-of-]] | 2023 | 通用等效建模与自动识别 |
| [[decoupled-detailed-equivalent-model-for-parallel-and-multi-rate-emt-type-simulat]] | 2026 | 多速率与CPU-GPU并行 |

## 技术演进脉络

### 2000s：MMC诞生与早期探索
- **MMC拓扑提出** (2001-2003)
  - 模块化级联思想
  - 子模块概念确立
- **早期详细模型**
  - 逐个开关建模
  - 计算量巨大，仅适用小规模

### 2010-2014：等效建模突破
- **时变戴维南等效** (2010)
  - 导纳矩阵分区
  - 2770倍加速，精度误差<2‰
- **平均值模型** (2013-2014)
  - 桥臂整体等效
  - 效率提升1-2个数量级
- **连续模型** (2014)
  - 阻塞状态建模
  - 故障分析能力

### 2015-2019：精度与效率优化
- **模型对比研究** (2015)
  - DEM/AEM/AVM系统对比
  - 适用边界明确
- **增强型AVM** (2016-2018)
  - 闭锁工况精度提升
  - 初始化补偿
- **虚假功率问题** (2019)
  - 机理揭示
  - 解决方案提出

### 2020-2026：自适应与智能化
- **自适应模型** (2020)
  - 多模型动态切换
  - 全工况覆盖
- **通用建模框架** (2023)
  - 任意拓扑自动识别
  - 单/双/多端口子模块
- **异构并行加速** (2026)
  - CPU-GPU协同
  - 多速率解耦

## 关键发现汇总

### 模型性能基准
- **[2010]** 戴维南等效模型：121电平MMC，2770倍加速，误差<2‰
- **[2015]** DEM vs DSM：全桥拓扑加速60倍，半桥30倍
- **[2018]** 多端口模型：任意子模块拓扑，Schur补数降阶
- **[2020]** 自适应模型：切换冲击<0.1%，效率提升10-40倍
- **[2023]** 加速DEM：正常运行无需重因子化，额外10倍加速

### 精度与适用性
- **[2014]** AVM局限：直流故障工况精度不足
- **[2016]** EAVM改进：闭锁工况误差<0.5%
- **[2019]** 虚假功率：经典AEM可能产生显著非物理损耗
- **[2021]** 损耗计算：桥臂级解析估算，精度与详细模型一致

### 实时与硬件实现
- **[2018]** FPGA实现：移位相量模型，400子模块实时
- **[2021]** 并行DEM：多核CPU，桥臂级并行
- **[2026]** GPU加速：DEM细粒度并行，SIMT架构

### 前沿研究方向
- **AI辅助建模**：神经网络降阶，黑箱模型辨识
- **数字孪生集成**：MMC状态在线估计与预测
- **量子计算**：大规模MMC特征值问题量子加速
- **全工况自适应**：基于暂态强度的智能模型选择

## 深度增强内容

### 1. 子模块类型对比

| 特性 | 半桥(HBSM) | 全桥(FBSM) | 箝位双(CDSM) |
|------|-----------|-----------|-------------|
| 开关数 | 2 | 4 | 4 |
| 电容数 | 1 | 1 | 2 |
| 输出电平 | 0, $v_C$ | -$v_C$, 0, $v_C$ | 0, $v_C$/2, $v_C$ |
| 直流故障 | 无法自清除 | 可闭锁清除 | 可闭锁清除 |
| 损耗 | 低 | 高(约2倍) | 中 |
| 成本 | 低 | 高(约1.5-2倍) | 中 |
| 应用场景 | 无直流故障风险 | 需故障清除能力 | 混合MMC |

### 2. 仿真参数配置表

| 模型类型 | 子模块数 | 步长 | 加速比 | 典型误差 | 适用场景 |
|---------|---------|------|--------|---------|---------|
| **DSM** | <50 | 1-5μs | 1x | <0.1% | 器件级损耗、阀控验证 |
| **DEM** | 120-400 | 10μs | 30-60x | <0.1% | 直流故障、保护设计 |
| **EAVM** | 401电平 | 20-50μs | 20-50x | <0.5% | 闭锁工况仿真 |
| **自适应** | 401电平 | 可变 | 10-40x | <0.1% | 全工况混合 |
| **机电** | MTDC多端 | 10ms | 200x | <2% | 系统级稳定 |

**关键参数设置建议**：
- 子模块电容：$C_{SM} = 6-15$ mF（取决于功率等级）
- 桥臂电感：$L_{arm} = 50-100$ mH
- 桥臂电阻：$R_{arm} = 0.1-0.5$ Ω
- 全桥比例：$\eta = 0.2-0.5$（用于直流故障自清除）

### 3. 模型选择决策树

```
研究目标？
├── 器件级分析（损耗、热、阀控）
│   └── DSM或DEM（N<50）
├── 直流故障穿越分析
│   └── DEM或EAVM（闭锁精度）
├── 系统级控制策略
│   └── AVM或动态相量（50μs-1ms）
├── 大规模MTDC电网
│   └── 机电暂态模型（10ms）
├── 实时HIL测试
│   └── SPM或固定导纳模型（1-5μs）
└── 全工况综合研究
    └── 自适应多模型框架

系统规模？
├── N < 50 → DSM/DEM
├── 50 ≤ N ≤ 200 → DEM/AEM
├── N > 200 → AVM/自适应/机电
└── 多端MTDC → 多速率协同
```

### 4. MMC建模检查清单

**详细模型/DSM**
- [ ] IGBT/二极管开关特性准确
- [ ] 电容电压排序算法实现
- [ ] 死区时间效应考虑
- [ ] 均压控制策略验证

**等效模型/DEM**
- [ ] 梯形法离散参数正确
- [ ] 诺顿等效电流源计算
- [ ] 导纳矩阵更新策略（恒定/变导纳）
- [ ] 闭锁工况切换逻辑

**平均值模型/AVM**
- [ ] 桥臂电压计算准确
- [ ] 环流抑制控制模型
- [ ] 电容电压纹波表征
- [ ] 闭锁工况初始化补偿（EAVM）

**通用检查**
- [ ] 功率平衡验证
- [ ] 虚假功率检测
- [ ] 与详细模型对比基准
- [ ] 直流故障响应验证

### 5. 前沿技术速览

| 技术方向 | 核心思想 | 性能提升 | 代表文献 |
|---------|---------|---------|---------|
| 时间并行(MGRIT) | 粗细步长协同 | 5核3.47x加速 | 2019 |
| 状态空间降阶 | 开关状态分组 | 状态矩阵降维 | 2025 |
| 打靶法初始化 | 周期稳态直接求解 | 避免暂态等待 | 2024 |
| 损耗曲面评估 | 开关频率分布建模 | 快速在线计算 | 2024 |
| 双映射死区建模 | 死区效应精确表征 | 混合MMC适用 | 2026 |

## 相关方法
- [[average-value-model]] - 桥臂整体等效方法
- [[thevenin-norton-equivalent]] - 网络等效核心技术
- [[fixed-admittance]] - ADC避免矩阵重构
- [[dynamic-phasor]] - 频域建模与机电接口
- [[state-space-method]] - MMC状态方程降阶
- [[multirate-method]] - 交直流协同仿真

## 相关模型
- [[vsc-model]] - 两电平换流器对比
- [[mtdc-model]] - 多端直流系统
- [[converter-transformer-model]] - MMC换流变
- [[cable-model]] - 直流电缆连接
- [[fdne-model]] - MMC外部网络等值

## 相关主题
- [[vsc-hvdc]] - 柔性直流输电
- [[real-time-simulation]] - MMC实时模型
- [[co-simulation]] - 机电-电磁协同
- [[parallel-computing]] - MMC并行加速
- [[wind-farm-modeling]] - 海上风电MMC并网

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自EMT领域学术文献的深度分析*
*支撑书籍第三篇第8章"模块化多电平换流器(MMC)建模"*
