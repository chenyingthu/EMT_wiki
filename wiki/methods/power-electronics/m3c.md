---
title: "M3C 建模方法 (Modular Multilevel Matrix Converter)"
type: method
tags: [m3c, modular-multilevel-matrix-converter, lfac, converter-modeling, ac-ac, nine-arm]
created: "2026-05-05"
updated: "2026-05-18"
---

# M3C 建模方法 (Modular Multilevel Matrix Converter)

## 定义与边界

M3C (Modular Multilevel Matrix Converter, 模块化多电平矩阵换流器) 是一种九桥臂 AC/AC 直接变换结构，每个桥臂由子模块（半桥或全桥）串联构成，可在两侧不同频率的交流系统之间直接实现功率变换，而无需直流环节。M3C 常见于低频交流（LFAC）输电、异步交流系统互联（50/60 Hz 与 16.7 Hz 或 20 Hz）和背靠背频率变换场景。

M3C 与普通 MMC 的核心区别在于：

| 特性 | MMC | M3C |
|------|-----|-----|
| 端口类型 | AC/DC 变换，直流侧为单极性 | AC/AC 变换，两侧均为交流 |
| 桥臂数量 | 6 桥臂（三相×上下） | 9 桥臂（输入侧3相 + 输出侧3相 + 公共桥臂） |
| 能量平衡 | 直流侧集中平衡 | 输入/输出两侧间同时平衡，控制复杂度更高 |
| 频率处理 | 单一工频 | 需处理两侧不同频率的坐标变换和功率耦合 |
| EMT 建模挑战 | 环流抑制、子模块均压 | 双频率解耦、功率耦合、桥臂能量双重平衡 |

本页作为 M3C 建模方法入口，承接相关链接并说明其与普通 MMC、VSC 的建模边界。

## EMT 中的角色

M3C 建模在电磁暂态仿真中的核心作用体现在以下几个方面：

**1. 模块化桥臂的精细化描述**
M3C 的九桥臂结构每条桥臂含 N 个子模块（半桥 SM 或全桥 FB SM），总状态量规模为 9×N。EMT 详细模型需要追踪每个子模块的开关状态、电容电压和桥臂电流，计算量随 N 线性增长。这使得 M3C 的 EMT 详细模型在计算效率上面临比 MMC 更大的挑战。

**2. 双频耦合功率变换**
M3C 连接的两个交流系统频率不同（如 50 Hz 工频侧与 16.7 Hz 铁路低频侧），两侧有功功率通过桥臂损耗耦合：

$$P_{sOut} = P_{sIn} - P_{loss}$$

这一约束是 M3C 迭代潮流算法的核心，也是 EMT 建模中两侧网络方程联解的关键。

**3. LFAC 输电系统的稳定性分析**
LFAC 输电可缓解长距离输电的功角稳定和电缆充电电流限制，但需要 M3C 实现与50/60 Hz 电网的频率变换。EMT 建模用于分析：LFAC 系统的暂态稳定性、M3C 与常规 MMC/VSC 在拓扑和控制上的差异、HVDC 与 LFAC 的互补应用。

**4. 构网型控制的去中心化运行**
M3C 可采用虚拟同步机（VSG）控制实现去中心化构网运行，多台 M3C 按阻尼系数比例分担不平衡功率：

$$P_{dis\_VSGi} = \frac{D_i}{\sum_{i=1}^k D_i} P_{mis}$$

$$f = f_{ref} - \frac{1}{\sum_{i=1}^k D_i} P_{mis}$$

## 拓扑结构

<div style="text-align:center;margin:16px 0;">

<table border="1" cellpadding="8" cellspacing="0" style="margin:0 auto;border-collapse:collapse;font-family:'Times New Roman',serif;font-size:13px;">
<caption style="font-weight:bold;margin-bottom:8px;color:#1a1a2e;">表1 · M3C 四种 EMT 建模方法对比</caption>
<tr style="background:#1a1a2e;color:white;font-weight:bold;text-align:center;">
  <td style="width:100px;">建模方法</td>
  <td style="width:80px;">等效电容</td>
  <td style="width:70px;">计算复杂度</td>
  <td style="width:70px;">EMT步长</td>
  <td style="width:60px;">加速比</td>
  <td style="width:65px;">精度误差</td>
  <td style="width:160px;">典型适用范围</td>
  <td style="width:140px;">失效场景</td>
</tr>
<tr style="background:#fee2e2;">
  <td><b>详细EMT</b></td>
  <td>不适用</td>
  <td>O(9N)</td>
  <td>1–50 μs</td>
  <td>1×</td>
  <td>高保真</td>
  <td>开关谐波·子模块均压·内部环流·故障分析</td>
  <td>系统级仿真·控制设计·大系统稳定</td>
</tr>
<tr style="background:#dcfce7;">
  <td><b>平均值模型</b></td>
  <td>C<sub>eq</sub>=9NC<sub>SM</sub></td>
  <td>O(9)</td>
  <td>10–100 μs</td>
  <td>10–50×</td>
  <td>&lt;3%</td>
  <td>系统级EMT·稳定性分析·潮流初始化·控制设计</td>
  <td>保护闭锁·均压分析·开关谐波·内部环流</td>
</tr>
<tr style="background:#dbeafe;">
  <td><b>双αβ0解耦</b></td>
  <td>C<sub>eq</sub>=9NC<sub>SM</sub></td>
  <td>O(18)</td>
  <td>100 μs–1 ms</td>
  <td>50–200×</td>
  <td>&lt;1.5%</td>
  <td>LFAC接口·迭代潮流计算·双频率耦合</td>
  <td>开关级谐波·不平衡故障·EMT细节·实时仿真</td>
</tr>
<tr style="background:#ede9fe;">
  <td><b>正序基波相量</b></td>
  <td>端口等效</td>
  <td>O(1)</td>
  <td>10 ms</td>
  <td>~200×</td>
  <td>&lt;1.5%</td>
  <td>PSS/E大系统稳定·机电暂态仿真·规划分析</td>
  <td>所有EMT现象·开关谐波·不平衡故障·保护时序</td>
</tr>
</table>

</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">表1 · M3C 四种 EMT 建模方法对比（参考 Yu 2023 验证结果整理）</p>

## EMT 建模方法

### 方法1：详细电磁暂态模型

完整保留每条桥臂的子模块开关状态、电容电压和桥臂电流。状态量规模为 9×N（9个桥臂，每桥臂N个子模块），计算量随 N 线性增长。适用于开关谐波分析、子模块均压策略研究和内部环流分析。

详细模型的每条桥臂可表示为：

$$u_{arm}(t) = \sum_{i=1}^{N} u_{SM,i}(t) = \sum_{i=1}^{N} S_i(t) \cdot u_{C,i}(t)$$

其中 $S_i(t) \in \{0, 1\}$ 为第 i 个子模块的开关状态，$u_{C,i}(t)$ 为其电容电压。桥臂电流满足：

$$L_{arm} \frac{di_{arm}}{dt} = u_{source} - u_{arm} - R_{arm} i_{arm}$$

**计算复杂度**：状态变量数 $N_{states} = 9 \times (2N + 1)$（电容电压 + 桥臂电流），每时步需要求解 9×N 个子模块的开关非线性。

### 方法2：平均值模型 (AVM)

将每个桥臂的 N 个子模块电容集中等效为单一电容：

$$C_{eq} = N \cdot C_{SM}$$

九桥臂总等效电容：

$$C_{eq,total} = 9N C_{SM}$$

平均值模型忽略子模块开关细节，保留桥臂级动态。桥臂能量：

$$W_{arm} = \frac{1}{2} C_{eq} u_{C,eq}^2$$

适用于系统级 EMT 仿真和稳定性分析，步长可达 10–100 μs，相比详细模型加速约 10–50 倍。

### 方法3：双 αβ0 变换解耦模型 [Yu 2023]

通过双重 αβ0 变换将 M3C 九桥臂变量解耦为输入侧和输出侧独立的等效电路：

**输入侧 αβ0 变换**：将输出电压和电流映射至输入频率参考系

$$L_0 \frac{d}{dt} \begin{bmatrix} i_{V\alpha} \\ i_{V\beta} \end{bmatrix} + R_0 \begin{bmatrix} i_{V\alpha} \\ i_{V\beta} \end{bmatrix} + \frac{\sqrt{3}}{3} \begin{bmatrix} u_{0\alpha} \\ u_{0\beta} \end{bmatrix} = \frac{\sqrt{3}}{3} \begin{bmatrix} u_{V\alpha} \\ u_{V\beta} \end{bmatrix}$$

**含变压器漏抗的扩展形式**：

$$(L_0 + 3L_{tIn}) \frac{d}{dt} \begin{bmatrix} i_{V\alpha} \\ i_{V\beta} \end{bmatrix} + R_0 \begin{bmatrix} i_{V\alpha} \\ i_{V\beta} \end{bmatrix} + \begin{bmatrix} u_{sum\alpha} \\ u_{sum\beta} \end{bmatrix} = \begin{bmatrix} u_{sIn\alpha} \\ u_{sIn\beta} \end{bmatrix}$$

其中 $L_{tIn}$ 为输入侧变压器漏感。类似地，输出侧经 αβ0 变换映射至输出频率参考系。解耦后的桥臂方程将九桥臂强耦合问题转化为两个独立的三相系统问题，大幅降低计算复杂度。

**等效阻抗标幺值**：

$$R_0^* = \frac{2\sqrt{3} R_{on} N}{Z_{ac,base}}$$

### 方法4：正序基波相量模型 [Yu 2023]

结合准稳态假设和频率缩放，将 M3C 表示为正序基波相量域的等效电路。适用于 PSS/E 等机电暂态平台的大系统稳定性仿真，机电暂态步长可达 10 ms，相比 EMT 详细模型加速约 200 倍。

## 形式化表达

### M3C 桥臂微分方程（输入侧）

$$L_0 \frac{d\mathbf{i}_{V}}{dt} + R_0 \mathbf{i}_{V} + \frac{\sqrt{3}}{3} \mathbf{u}_{0} = \frac{\sqrt{3}}{3} \mathbf{u}_{V}$$

其中：$\mathbf{i}_V = [i_{V\alpha}, i_{V\beta}]^T$（输入侧 αβ 坐标电流），$\mathbf{u}_V = [u_{V\alpha}, u_{V\beta}]^T$（输入侧 αβ 坐标电压），$\mathbf{u}_0 = [u_{0\alpha}, u_{0\beta}]^T$（耦合侧 αβ 坐标电压）。

### 等效电容

$$C_{eq} = 9N C_{SM}$$

九桥臂子模块电容集中等效为单一电容，$N$ 为单桥臂子模块数，$C_{SM}$ 为单个子模块电容值。

### 能量守恒方程

$$P_{sOut} = P_{sIn} - P_{loss}$$

M3C 输入侧与输出侧有功功率通过桥臂损耗耦合，是迭代潮流计算的核心约束。损耗模型通常表示为：

$$P_{loss} = \sum_{i=1}^{9} \left( a_i P_{arm,i} + b_i |i_{arm,i}| + c_i \right)$$

其中 $a_i, b_i, c_i$ 为第 i 桥臂的损耗系数。

### VSG 构网控制同步环

$$J \frac{d\omega_s}{dt} = \frac{1}{\omega_0}(P_{sref} - P_s) - D_d \omega_s$$

虚拟同步机控制下 M3C 的功率同步环微分方程，$J$ 为虚拟惯量时间常数，$D_d$ 为阻尼系数。虚拟惯量 $J$ 与等效电容 $C_{eq}$ 的关系为：

$$J = \frac{C_{eq} U_{dc}^2}{2\omega_0^2 S_{base}}$$

### 多 VSG 去中心化功率分配

$$P_{dis\_VSGi} = \frac{D_i}{\sum_{i=1}^k D_i} P_{mis}$$

$$f = f_{ref} - \frac{1}{\sum_{i=1}^k D_i} P_{mis}$$

多个构网型 M3C 按阻尼系数比例分担不平衡功率，共同确定系统频率。

### 低频线路参数频率缩放

$$Z_s = R_s + j\omega L_s$$

$$Y_s = j\omega C_s$$

低频线路参数需按运行频率 $\omega$ 缩放，这是 LFAC 系统与常规工频系统 EMT 建模的核心区别。

## 关键技术挑战

### 挑战1：双频率耦合与解耦

M3C 连接的两个交流系统频率不同，两侧电压和电流的参考系不同（输入侧在工频 αβ 坐标系，输出侧在低频 αβ 坐标系），双重坐标变换增加了模型的复杂性。双重 αβ0 变换解耦需假设桥臂参数对称，实际非对称条件下的建模精度有待验证。

### 挑战2：九桥臂能量双重平衡

M3C 的桥臂能量需在输入/输出两侧间同时平衡，不像 MMC 可以通过直流侧电容集中存储。两侧功率耦合使得潮流计算需要迭代求解——先计算一侧功率，再根据损耗更新另一侧，反复迭代至收敛。

### 挑战3：谐波耦合与开关细节

详细 EMT 模型需要追踪 9×N 个子模块的开关状态，计算量极大。子模块电压纹波和内部环流高频分量（尤其在全桥子模块 FB-SM 情况下）在平均值模型中被忽略，不适用于保护闭锁和均压分析。

### 挑战4：构网型控制的参数整定

VSG 控制中的虚拟惯量 $J$ 和阻尼系数 $D_d$ 需要根据系统容量和频率响应要求整定。多 VSG 并联时的去中心化功率分配策略（按阻尼系数比例）在 LFAC 场景下的有效性尚未有系统性验证。

### 挑战5：与机电暂态平台的接口

将 M3C 的 EMT 模型嵌入 PSS/E 等机电暂态平台需要：(1) 正序基波相量等效；(2) 频率缩放后的线路参数；(3) 迭代潮流算法与机电暂态仿真的接口。这些接口的实现依赖于 M3C 控制模式的精确建模。

## 量化性能边界

| 建模方法 | 等效电容 | 计算复杂度 | EMT 步长 | 加速比 | 精度误差 | 适用场景 |
|---------|---------|-----------|---------|--------|---------|---------|
| 详细 EMT 模型 | 不适用 | O(9N) | 1–50 μs | 1×（基准） | 高保真 | 开关谐波/故障分析 |
| 平均值模型 (AVM) | $C_{eq}=9NC_{SM}$ | O(9) | 10–100 μs | 10–50× | < 3% | 系统级 EMT/稳定性 |
| 双 αβ0 解耦 [Yu 2023] | $C_{eq}=9NC_{SM}$ | O(18) | 100 μs–1 ms | 50–200× | < 1.5% | LFAC 接口/潮流计算 |
| 正序基波相量 [Yu 2023] | 端口等效 | O(1) | 10 ms | ~200× | < 1.5% | PSS/E 大系统稳定 |

> 原文未报告可核验的全部量化数据。上表参考 Yu 2023 的验证结果整理，加速比数据为与 PSCAD 详细模型对比的近似值。详细 EMT 基准步长取 50 μs，双 αβ0 解耦模型加速比按 100 μs 步长估计，正序基波相量模型按 10 ms 机电暂态步长估计。

## 适用边界与选择指南

### 方法选择决策表

| 应用场景 | 推荐模型 | 不适用模型 | 原因 |
|---------|---------|-----------|------|
| 开关谐波分析 | 详细 EMT 模型 | AVM/相量模型 | 忽略开关细节丢失谐波信息 |
| 子模块均压策略研究 | 详细 EMT 模型 | AVM/相量模型 | 子模块级变量不可见 |
| 系统级 EMT 稳定性分析 | AVM | 详细模型（计算量过大） | 计算效率与精度平衡 |
| LFAC 系统潮流计算 | 双 αβ0 解耦模型 | 详细模型 | 双频率耦合接口必备 |
| PSS/E 大系统稳定仿真 | 正序基波相量模型 | 所有 EMT 模型 | 机电暂态平台不支持开关细节 |
| 构网型 LFAC 控制器设计 | AVM + VSG | 详细模型 | 需要快速迭代参数扫描 |

### 失效边界

- **不能跨层级外推**：Yu 2023 的 10 ms 步长正序基波模型不适用于开关级谐波、子模块均压和内部环流分析。机电暂态模型与 EMT 详细模型之间存在无法跨越的精度鸿沟。
- **平均值模型丢失信息**：等效电容简化丢失了子模块电压纹波和内部环流高频分量，不适用于保护闭锁过程和均压分析。
- **双 αβ0 变换假设**：解耦假设桥臂参数对称，当桥臂参数不一致（如不同子模块退化）时，解耦精度下降。
- **VSG 参数依赖**：多 VSG 去中心化控制的稳定性边界尚未系统验证，参数整定缺乏统一方法。
- **LFAC 频率限制**：Yu 2023 的验证约束于正序基波和机电暂态场景，未覆盖不平衡故障和电磁暂态细节。

### 关键假设

- 双重 αβ0 变换解耦假设桥臂参数对称
- 准稳态近似假设输入/输出侧频率偏差在可接受范围内
- 机电暂态模型假设 M3C 内部动态可以等效为集中电容和端口阻抗
- 子模块电容电压纹波在平均值模型中用等效集中电容代替

## 与相关方法的关系

- [[mmc-model]]：MMC 是 AC/DC 变换，M3C 是 AC/AC 变换；两者共享多电平桥臂思想但端口拓扑和控制目标不同
- [[mbsm]]：MBSM（多桥臂换流器）与 M3C 有相似的桥臂级联结构，可与多桥臂统一框架关联
- [[virtual-synchronous-generator]]：M3C 可采用 VSG 控制实现去中心化构网运行，多 VSG 功率分配公式源自此框架
- [[electromechanical-transient]]：M3C 可在机电暂态尺度下等效为端口模型用于大系统研究
- [[multi-terminal-dc]]：M3C 虽然连接交流系统，但其多端功率交换特性可与 MTDC 系统对比
- [[vector-control]]：M3C 控制常需要多坐标系（输入/输出侧不同频率）或多频率控制组织

## 来源论文

- [[electromechanical-transient-modeling-of-the-low-frequency-ac-system-with-modular]] — Yu 等 2023：提出 M3C-LFAC 系统机电暂态建模完整框架，包含双重 αβ0 变换解耦、迭代潮流算法和 PSS/E 实现，与 PSCAD 详细模型对比验证关键电气量相对误差控制在 1.5% 以内