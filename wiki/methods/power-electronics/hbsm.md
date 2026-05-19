---
title: "HBSM 入口页 (HBSM)"
type: method
tags: [hbsm, half-bridge-submodule, mmc, submodule, emt-modeling]
created: "2026-05-05"
updated: "2026-05-13"
---

# HBSM 入口页 (HBSM)

## 定义与物理结构

HBSM（Half-Bridge Submodule，半桥子模块）是模块化多电平换流器（MMC）中最基础、应用最广泛的子模块拓扑。其物理结构由**两个反并联 IGBT 对（上臂 T1+D1、下臂 T2+D2）串联一个子模块电容 $C_{sm}$** 构成，如图 1 所示。在 EMT 仿真语境中，HBSM 方法讨论的不是拓扑本身，而是如何在节点分析（EMTP-type）或状态空间框架中，用不同抽象层级表示其插入/旁路状态、电容电压动态以及桥臂电流路径。

HBSM 的核心电气特性：**只能输出正电压或零电压**（$v_{sm} \in \{v_c, 0\}$），不具备故障负电平阻断能力。这是 HBSM 与全桥子模块（FBSM）的根本区别，也是半桥 MMC 需要额外直流故障保护机制的原因。

```html
<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 600 420" xmlns="http://www.w3.org/2000/svg">
  <!-- Title -->
  <text x="300" y="30" text-anchor="middle" font-size="18" font-weight="bold" fill="#333">图1 · HBSM 物理拓扑与 EMT 建模层级体系</text>

  <!-- HBSM Physical Topology (left) -->
  <rect x="30" y="55" width="250" height="160" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="155" y="80" text-anchor="middle" font-size="14" font-weight="bold" fill="#2563eb">HBSM 物理拓扑</text>

  <!-- Upper IGBT -->
  <rect x="130" y="95" width="60" height="35" rx="4" fill="#ffffff" stroke="#333" stroke-width="1.5"/>
  <text x="160" y="117" text-anchor="middle" font-size="12" fill="#333">T1/D1</text>

  <!-- Lower IGBT -->
  <rect x="130" y="175" width="60" height="35" rx="4" fill="#ffffff" stroke="#333" stroke-width="1.5"/>
  <text x="160" y="197" text-anchor="middle" font-size="12" fill="#333">T2/D2</text>

  <!-- Capacitor -->
  <rect x="130" y="225" width="60" height="30" rx="4" fill="#ffffff" stroke="#333" stroke-width="1.5"/>
  <text x="160" y="245" text-anchor="middle" font-size="12" fill="#333">C_sm</text>

  <!-- Arrows between components -->
  <line x1="160" y1="130" x2="160" y2="175" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="160" y1="210" x2="160" y2="225" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Labels -->
  <text x="100" y="117" text-anchor="end" font-size="11" fill="#666">上桥臂</text>
  <text x="100" y="197" text-anchor="end" font-size="11" fill="#666">下桥臂</text>
  <text x="100" y="245" text-anchor="end" font-size="11" fill="#666">子模块电容</text>

  <!-- Port labels -->
  <text x="55" y="100" font-size="11" fill="#2563eb">a</text>
  <text x="55" y="260" font-size="11" fill="#2563eb">b</text>
  <text x="30" y="180" font-size="11" fill="#2563eb">v_sm</text>

  <!-- Modeling Levels (right) -->
  <rect x="300" y="55" width="270" height="320" rx="8" fill="#f9fafb" stroke="#666" stroke-width="1.5"/>
  <text x="435" y="80" text-anchor="middle" font-size="14" font-weight="bold" fill="#333">EMT 建模层级</text>

  <!-- Level 1: Detailed Switch -->
  <rect x="315" y="92" width="240" height="55" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="435" y="113" text-anchor="middle" font-size="12" font-weight="bold" fill="#dc2626">层级1：开关级详细模型</text>
  <text x="435" y="130" text-anchor="middle" font-size="10" fill="#666">TDM · 每个IGBT/二极管两态电阻</text>

  <!-- Level 2: Thevenin/Norton -->
  <rect x="315" y="157" width="240" height="55" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="435" y="178" text-anchor="middle" font-size="12" font-weight="bold" fill="#16a34a">层级2：戴维南/诺顿等效</text>
  <text x="435" y="195" text-anchor="middle" font-size="10" fill="#666">DEM · 后退欧拉/梯形法离散</text>

  <!-- Level 3: Hybrid Integration -->
  <rect x="315" y="222" width="240" height="55" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="435" y="243" text-anchor="middle" font-size="12" font-weight="bold" fill="#d97706">层级3：混合积分恒定导纳</text>
  <text x="435" y="260" text-anchor="middle" font-size="10" fill="#666">Gao 2023 · 梯形+中点法 + 蛙跳解耦</text>

  <!-- Level 4: Average Value -->
  <rect x="315" y="287" width="240" height="55" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="435" y="308" text-anchor="middle" font-size="12" font-weight="bold" fill="#7c3aed">层级4：平均值模型 (AVM)</text>
  <text x="435" y="325" text-anchor="middle" font-size="10" fill="#666">桥臂平均开关函数替代离散开关</text>

  <!-- Arrow between topology and levels -->
  <line x1="285" y1="150" x2="300" y2="150" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="292" y="145" text-anchor="middle" font-size="9" fill="#666">建模</text>

  <!-- Arrow down between levels -->
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <path d="M0,0 L8,3 L0,6" fill="#333"/>
    </marker>
  </defs>

  <!-- Accuracy/Efficiency axis -->
  <text x="590" y="100" text-anchor="end" font-size="10" fill="#dc2626">高精度</text>
  <text x="590" y="340" text-anchor="end" font-size="10" fill="#7c3aed">高效率</text>
  <line x1="580" y1="105" x2="580" y2="330" stroke="#999" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="580" y="350" text-anchor="middle" font-size="9" fill="#999">精度</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · HBSM 物理拓扑与 EMT 建模层级体系（从开关级详细模型到平均值模型）</p>
```

## EMT 中的角色

HBSM 是 MMC 的**基础构建单元**，其 EMT 建模面临的核心矛盾是：MMC 包含大量子模块（每桥臂几十到几百个 SM），若逐个按 IGBT/二极管开关级建模，主网络节点方程维度极高且导纳矩阵随开关状态频繁变化。已有 HBSM 建模方法围绕**恒定导纳**和**内部解耦**两个目标展开，可归为四个抽象层级（图1），从精度最高但计算最慢的开关级详细模型（TDM），到精度较低但效率极高的平均值模型（AVM）。

HBSM 在 EMT 仿真中的关键作用体现在四个维度：

**1. 故障电流分析（Fault Analysis）** — HBSM 无法阻断直流故障电流，故障时所有 SM 电容通过反并联二极管向故障点放电，形成反向续流路径。在 EMT 中必须精确模拟二极管导通/关断的拓扑切换过程，这对直流故障清除和换相失败分析至关重要。

**2. 开关暂态（Switching Transient）** — 开关级模型需精确捕捉 IGBT/二极管切换瞬间的电压/电流过冲，包括反向恢复电流和 du/dt 效应。高频开关场景（MHz 级 GaN）中还需考虑 PCB 寄生电感和非线性结电容的影响（ADC 模型 Lai 2026）。

**3. 电容电压纹波（Capacitor Voltage Ripple）** — 需跟踪每个 SM 电容电压的动态变化，用于排序和均压控制。电压纹波直接影响 MMC 的谐波性能和子模块电容的应力设计；纹波系数通常控制在 5%~15%。

**4. 系统级扩展性（System-Level Scalability）** — 戴维南等效等加速模型使计算量随 SM 数线性增长，而非指数增长，从而支持大规模 MMC-HVDC 系统的离线扫描和实时 HIL 仿真（百电平以上）。

## 四种 EMT 建模方法

### 方法1：开关级详细模型（TDM — Total Detailed Model）

**原理**：每个 IGBT 和二极管用两态可变电阻表示（通态 ~0.01 Ω，断态 ~10⁸ Ω）。桥臂内所有 SM 节点全部保留，通过 Dommel 离散后形成时变导纳矩阵，每次开关动作需重新 LU 分解。

**数学表达**：
$$R_T = \begin{cases} 0.01\ \Omega & \text{导通} \\ 10^8\ \Omega & \text{关断} \end{cases}$$

**特点**：
- 精度最高，可捕捉每个开关元件的瞬态行为
- 计算量随 SM 数呈指数增长（N 个 SM → 2N 个开关节点）
- 同步开关（simultaneous switching）导致多次全局 LU 分解
- Beddard 2015 的 201 电平 MMC 需 2400+ IGBT 和 1200+ 电容

**适用场景**：小规模 MMC 验证、开关瞬态研究、器件级故障分析

### 方法2：戴维南/诺顿等效模型（DEM — Detailed Equivalent Model）

**原理**：将每个 HBSM 的电容-IGBT 开关对离散为等效电阻与历史电压源（戴维南）或历史电流源（诺顿）的等效电路。同一桥臂内多个 SM 的等效电路串联叠加为一个桥臂级戴维南电路，再接入主网络求解桥臂电流。

**后退欧拉法离散**：
$$R_{eq} = \frac{\Delta t}{C_{sm}}, \qquad V_{hist}(t) = \frac{\Delta t}{C_{sm}} i_{arm}(t-\Delta t) + v_c(t-\Delta t)$$

$$v_c(t) = R_{eq} \cdot i_{arm}(t) + V_{hist}(t)$$

**梯形法离散**（精度更高）：
$$V_{hist}^{trap}(t) = \frac{\Delta t}{2C_{sm}} [i_{arm}(t) + i_{arm}(t-\Delta t)] + v_c(t-\Delta t)$$

**特点**：
- 桥臂内 SM 数量不影响主网络节点维度（始终为 1 个戴维南支路）
- 计算量随 SM 数线性增长（排序算法 O(NlogN) 而非 O(N²)）
- 梯形法稳态偏差比后退欧拉小 0.2~0.4%，但耗时约 2 倍
- Xu 2015 验证：N=200 时实现 15~20 倍加速

**适用场景**：中等规模 MMC-HVDC 系统、需要 SM 级精度的系统级仿真

### 方法3：混合积分恒定导纳模型（Gao 2023）

**原理**：Gao 等将梯形法与中点法混合，使桥臂等效电导在正常运行条件下保持恒定。结合蛙跳法（Leapfrog）将桥臂电感求解与 SM 电容电压更新完全解耦：主网络在 t 时刻求桥臂电流后，各 SM 用该电流显式更新 t+Δt/2 时刻的电容电压，各 SM 相互独立且计算复杂度 O(N)。

**恒定等效电导推导**（基于中点法）：
$$G = \frac{\Delta t}{2L_0 + R_{eq}\Delta t}$$

正常运行时 $R_{eq} = R_{eq1}$（单臂导通）保持不变，等效电导 G 为常数，避免频繁 LU 分解。

**蛙跳法电容更新**（解耦并行）：
$$v_{ci}(t+\frac{\Delta t}{2}) = v_{ci}(t-\frac{\Delta t}{2}) + \frac{\Delta t}{C_{smi}} i_{arm}(t)$$

**CDA 数值振荡抑制**（开关切换时触发，额外开销 <5%）：
$$i_{cda} = G_{cda} [v(t) - v(t-\Delta t)]$$

**特点**：
- 桥臂等效电导恒定 → 避免频繁 LU 分解
- SM 电容更新解耦 → 天然并行，O(N) 复杂度
- 每个桥臂等效为两节点诺顿电路嵌入主网络
- 稳态误差 <0.5%，暂态峰值误差 <1%
- 主网络节点维度降低约 90%

**适用场景**：多尺度含 MMC 系统、大规模 MMC-HVDC 离线仿真

### 方法4：平均值模型（AVM — Average Value Model）

**原理**：用桥臂平均开关函数 $S = \frac{1}{N}\sum_{i=1}^{N} S_i$ 替代逐个 SM 的离散开关，核心状态为桥臂等效电容电压和桥臂电流。改进拓扑等效可处理闭锁和直流故障时的二极管导通路径（Xu 2015 综述）。

**桥臂等效电容电压**：
$$v_{arm}(t) = \sum_{i=1}^{N} s_i(t) \cdot v_{ci}(t) \approx \frac{N}{2} \bar{v}_c(t)$$

**特点**：
- 适合系统级暂态（严重交直流故障）
- 丢失开关级细节（电容电压散布、开关事件、均压动态）
- 可用较大仿真步长（10~50 μs）

**适用场景**：大规模 MMC-MTDC 系统暂态扫描、控制系统设计验证

### 方法对比总览

|| 特性 | 开关级(TDM) | 戴维南等效(DEM) | 混合积分(Gao 2023) | 平均值(AVM) |
|---|---|---|---|---|---|
| **主网络节点维度** | O(2N) | O(1) | O(1) | O(1) |
| **计算复杂度** | O(N²) 指数 | O(NlogN) 线性 | O(N) 线性 | O(1) 最低 |
| **LU分解频率** | 每次开关 | 恒定导纳 | 恒定导纳 | 无需 |
| **稳态误差** | <0.1% | 0.2~0.4% | <0.5% | 1~5% |
| **加速比** | 1× | 15~20× | 5~15× | 50~100× |
| **SM级精度** | 完整 | 完整 | 完整 | 丢失 |
| **故障电流** | 精确 | 精确 | 精确 | 近似 |
| **适用规模** | <10 SM/arm | <200 SM/arm | <500 SM/arm | 系统级 |

## 形式化表达

### 核心方程汇总

**1. HBSM 输出电压（通用）**
$$v_{sm}(t) = s(t) \cdot v_c(t), \qquad s \in \{0, 1\}$$
其中 $s=1$ 为插入（输出 $v_c$），$s=0$ 为旁路（输出 0）。

**2. 电容电压动态（通用）**
$$C_{sm} \frac{dv_c}{dt} = s(t) \cdot i_{arm}(t)$$

**3. 同步开关预判逻辑（Zhang 2023）**
$$\begin{cases} x_2(t)=1, \ x_1(t)=1 & \text{当 } x_1(t-\Delta T)=2, x_1(t)=0, i_{hb}(t)>0 \\ x_2(t)=0, \ x_1(t)=0 & \text{当 } x_1(t-\Delta T)=0, x_1(t)=2, i_{hb}(t)>0 \end{cases}$$
通过 IGBT 门极信号和桥臂电流方向直接预判二极管续流/关断导致的同步开关状态，消除迭代搜索。

**4. 内节点收缩（Zhang 2023）**
$$Y_{reduced} = Y_{aa} - Y_{ab} Y_{bb}^{-1} Y_{ba}$$
将 SM 内部节点凝聚到端口，减少全局矩阵规模。

**5. 半桥三态定义（Zhang 2023）**

HBSM 的两个 IGBT/二极管对共有三种可能的稳态组合，分别对应三种端口电压输出状态：

状态 0（$T_{OFF}/D_{OFF}$）：IGBT 关闭、二极管关闭，端口输出电压为 0 V（旁路状态），电容电压保持不变，桥臂电流流经另一桥臂。

状态 1（$T_{OFF}/D_{ON}$）：IGBT 关闭、二极管导通，端口输出电压为电容电压 $v_c$（插入状态），电容通过二极管放电或充电，桥臂电流方向决定充放电状态。

状态 2（$T_{ON}/D_{OFF}$）：IGBT 导通、二极管关闭，端口输出电压为电容电压 $v_c$（插入状态），IGBT 流经全部桥臂电流，电容正常充电。

**三态转换规则**：实际运行中，状态切换由 IGBT 门极信号和桥臂电流方向共同决定。Zhang 2023 提出的同步开关预判逻辑通过分析当前步的门极信号和上一时步的二极管状态，直接推断当前步的稳态组合，无需迭代搜索。在 $i_{arm} > 0$ 且 $T_{OFF}$ 时，电流强制二极管导通形成状态 1；在 $i_{arm} < 0$ 且 $T_{OFF}$ 时，电流使二极管关断形成状态 0。精确的三态定义和转换规则是 HBSM EMT 建模的基础，也是同步开关预判算法能够消除迭代的根本原因。

## 关键技术挑战

**同步开关迭代**：半桥子电路中 IGBT 和二极管的状态变化可能同时引发连锁开关动作（同步开关），需要反复迭代求解稳定状态组合，导致多次全局 LU 分解。Zhang 2023 的同步开关预判方法通过逻辑判断直接得出稳定状态，消除了迭代。

**开关数值振荡**：开关动作瞬间的离散化可能引入数值振荡。Gao 2023 引入 CDA（Complementary Differential Admittance）抑制振荡，额外开销 <5%。

**高频寄生参数**：Lai 2026 指出，在 GaN HEMT 等高频场景（MHz 级）下，传统 EMT 模型需考虑 PCB 寄生参数和非线性结电容，ADC（Associated Discrete Circuit）模型提供了统一框架。

**故障电流建模**：HBSM 无法阻断直流故障，故障时所有 SM 电容通过反并联二极管向故障点放电。精确模拟此过程需要处理二极管导通路径的拓扑切换。

## 量化性能边界

**Gao et al. (2023) 混合积分恒定导纳模型**（IEEE TPWRS）：
- 梯形法与中点法组合，桥臂等效导纳在正常运行时保持恒定，避免频繁 LU 分解
- 蛙跳法（Leapfrog）解耦电容电压更新与桥臂电感方程，SM 间天然并行
- 稳态误差 <0.5%，暂态峰值误差 <1%
- 仿真速度提升 5~15 倍（对比戴维南等效模型），主网络节点维度降低 ~90%
- CDA 数值振荡抑制开销 <5%
- 验证：多尺度含 MMC 电力系统
- 数据缺口：仅验证半桥 MMC，未覆盖全桥或混合 MMC

**Zhang et al. (2023) 同步开关预判快速 EMT 建模**（中国电机工程学报）：
- 以半桥子电路为单位进行同步开关状态预判，消除迭代收敛
- 内节点收缩减少全局矩阵规模
- 80 模块 SST 仿真加速 20 倍，波形误差 <0.5%
- 验证：PSCAD/EMTDC，半桥 VSC 全工况（正常运行、短路、闭锁、状态切换）
- 数据缺口：需要二极管续流路径逻辑，不能直接推广到全桥拓扑

**Beddard et al. (2015) TDM/DEM/AM 三模型客观对比**（IEEE TPWRD）：
- 首次独立对比 TDM、DEM、AM 三种详细 MMC 模型
- TDM：201 电平 MMC 需 2400+ IGBT、1200+ 电容，导纳矩阵求逆极耗时
- DEM：显著减少仿真时间，但用户无法访问单个转换元件
- AM：计算效率高于 TDM，同时保留元件级访问
- 验证：Trans Bay Cable 项目基准（201 电平 MMC-HVDC）
- 数据缺口：不同模型在不同软件中验证，跨平台公平对比受限

**Xu et al. (2015) MMC 高效建模方法综述**：
- 三类模型族：受控源解耦、戴维南等效（后退欧拉/梯形法）、平均值模型
- 排序复杂度从 O(N²) 降至 O(N)
- 戴维南模型在 N=200 时实现 15~20 倍加速
- 梯形法比后退欧拉慢 2 倍但精度高 0.2~0.4%
- 验证：48 SM/arm 半桥 MMC-HVDC 基准，20 μs 步长
- 数据缺口：综述性质，数值来自文献汇集而非统一对比测试

**Xu et al. (2018) 二极管钳位 HBSM 自发电压均衡**：
- 每 SM 增加 1 个钳位二极管 + 阻尼电阻 + 三相 4 套辅助电路实现自动均压
- 电压传感器减少 >50%，DSP 延迟降低 30~50%
- 电压不均衡度 1~2%
- 额外器件：(6N+14) 二极管 + 4 IGBT + 4 电容每 N SM/相
- 验证：PSCAD/EMTDC + 缩比样机
- 数据缺口：硬件方案增加额外器件成本，与软件排序方案的全面经济性对比缺失

**Lai et al. (2026) 半桥桥臂 ADC 解析模型**（IEEE TPWRS）：
- 基于 EMT 恒导纳方法论的关联离散电路（ADC）模型
- 统一框架表示所有瞬态子模式，避免分段线性模型的矩阵切换
- 纳入 PCB 寄生参数和非线性结电容
- 验证：GaN HEMT 半桥腿，MHz 级开关频率
- 数据缺口：仅验证 GaN 器件，Si IGBT 场景需额外验证

## 适用边界与选择指南

### 建模层级选择指南

|| 应用场景 | 推荐层级 | 理由 |
|---|---|---|---|
| 开关瞬态/器件级故障 | 开关级 TDM | 需精确捕捉 IGBT/Diode 切换 |
| SM 级电压/电流跟踪 | 戴维南等效 DEM | 保留 SM 精度，计算量线性 |
| 大规模 MMC-HVDC 离线仿真 | 混合积分 Gao 2023 | 恒定导纳 + 并行，加速 5~15× |
| 控制系统设计/系统级暂态 | AVM | 可大步长，适合快速扫描 |
| GaN 高频开关（MHz 级） | ADC 模型 (Lai 2026) | 统一框架处理寄生参数 |
| 直流故障分析 | DEM/Gao 2023 | 需精确二极管导通路径 |

### 失效边界

- **需要故障阻断或负电平输出**：应切换到 [[fbsm]]（全桥子模块）
- **仅用 AVM 时**：丢失单个 SM 电压散布和开关事件细节
- **不显式建模排序和平衡逻辑**：可能低估电压不均衡风险
- **高频 GaN 半桥（MHz 级）**：需使用 ADC 模型（Lai 2026）等专用框架
- **实时仿真 HIL**：需考虑 DSP 延迟和排序算法实时性限制

## 与相关方法的关系

**[[fbsm]]（全桥子模块）**：FBSM 可输出 +、-、0 三种电平且具备双向故障电流阻断能力，这是其与 HBSM 的根本差异。在 EMT 建模中二者共享戴维南/诺顿等效框架（DEM），但 FBSM 的三态控制逻辑（+、-、0）和负电平输出需要额外处理开关状态组合，导致等效电路的导纳矩阵比 HBSM 复杂约 30%~50%。

**[[nearest-level-control]]（最近电平调制，NLM）**：HBSM 的输出电压波形由 NLM（或 CPS-SPWM）通过排序分配算法确定插入/旁路状态。NLM 根据当前桥臂电流方向和电容电压排序结果，将参考电压映射到最近的电平状态，是半桥 MMC 最广泛使用的调制策略。

**[[mmc-model]]（MMC 系统模型）**：HBSM 是 MMC 的基础构建单元，MMC 页面组织 HBSM 与桥臂电感、上/下桥臂耦合、直流母线交互的系统层面关系。MMC 系统模型需要协调多个 HBSM 的均压算法、循环电流抑制控制和桥臂电流平衡。

**[[average-value-model]]（平均值模型）**：AVM 忽略单个 HBSM 的开关离散性，以桥臂平均开关函数 $\bar{s} = \frac{1}{N}\sum_{i=1}^{N} s_i$ 替代 N 个离散开关状态，将每个桥臂等效为单端口受控电压源或电流源。AVM 丢失了 SM 级电压散布信息，适用于大步长（10~50 μs）系统级暂态扫描。

**[[mbsm]]（多桥臂子模块）**：MBSM 将多个半桥单元级联以扩展电压等级或提供冗余通路，扩展了 HBSM 的能力边界。在 EMT 建模中，MBSM 仍可使用戴维南等效框架，但每个 MBSM 单元内部的多个 HBSM 需要额外的排序均压逻辑。

**[[circulating-current-suppression]]（环流抑制控制，CCS）**：HBSM 的插入/旁路状态决定了各桥臂的等效电流路径，桥臂内部循环电流（2 倍频分量）由上/下桥臂电流不均衡引起，与 HBSM 的开关状态直接相关。CCS 通过在控制层注入环流指令来抵消 2 倍频电流分量，减小电容电压纹波和桥臂电流应力。

**[[companion-circuit]]（伴随电路法）**：Dommel 离散是 HBSM 电容和桥臂电感统一离散的底层数学框架。伴随电路将分布参数元件（电容、电感）替换为等效电阻与历史电压/电流源，使每个时步只需一次 LU 分解即可求得网络节点电压。

**[[half-bridge-submodule]]（半桥子模块详细方法页）**：与本页面为同一主题的详细方法页，包含完整的四种建模层级详解（TDM/DEM/混合积分/AVM）、公式推导和算法步骤。half-bridge-submodule.md 侧重于子模块电路拓扑和器件级物理，本页面侧重于 EMT 建模方法分类和性能对比，二者互为补充。

## EMT 建模方法总结

| 建模层级 | 核心思想 | 计算效率 | SM 级精度 | 代表性论文 |
|---------|---------|---------|---------|-----------|
| 开关级 TDM | 每个 IGBT/Diode 两态电阻 | 最低 | 完整 | Beddard 2015 |
| 戴维南等效 DEM | 桥臂 SM 等效为单个戴维南支路 | 中等 | 完整 | Xu 2015 |
| 混合积分 Gao 2023 | 梯形+中点法 + 蛙跳解耦 | 高 | 完整 | Gao 2023 |
| 平均值 AVM | 桥臂平均开关函数替代 | 最高 | 丢失 | Xu 2015 |

## 来源论文

- [[an-efficient-half-bridge-mmc-model-for-emtp-type-simulation-based-on-hybrid-nume]] — Gao 2023, IEEE TPWRS：混合积分恒定导纳模型，梯形+中点法+蛙跳解耦
- [[fast-electromagnetic-transient-modeling-method-for-half-bridge-type-voltage-sour]] — Zhang 2023，中国电机工程学报：同步开关预判+内节点收缩快速建模
- [[comparison-of-detailed-modeling-techniques-for-mmc-employed-on-vsc-hvdc-schemes]] — Beddard 2015, IEEE TPWRD：TDM/DEM/AM 三模型首次客观对比
- [[the-diode-clamped-half-bridge-mmc-structure-with-internal-spontaneous-capacitor-]] — Xu 2018：二极管钳位 HBSM 自均压拓扑
- [[analytical-modeling-of-the-half-bridge-leg-using-an-associated-discrete-circuit-]] — Lai 2026, IEEE TPWRS：GaN 半桥腿 ADC 解析模型
