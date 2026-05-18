---
title: "模型验证与基准测试 (Model Verification and Benchmarking)"
type: topic
tags: [verification, benchmark, validation, cigre, ieee, standard, emt, playback, hils]
created: "2026-05-01"
updated: "2026-05-13"
---

# 模型验证与基准测试 (Model Verification and Benchmarking)

## 定义

模型验证（Verification）与基准测试（Benchmarking）是电磁暂态（EMT）仿真中确保模型可信度和结果可复现性的核心方法论。验证回答"给定假设下模型是否正确实现"，基准测试回答"多个模型、工具或算法在同一系统和扰动下是否可比"。

验证关注的层次包括：
- **单元验证**：单个元件（RLC、开关、变压器、线路、控制器）是否与解析解、频响或已知稳态一致
- **子系统验证**：换流器、线路段、保护链路或电机-控制组合的接口变量和事件时序是否正确
- **系统级基准**：在 IEEE、CIGRE 或工程系统中设置统一扰动，对比波形、特征量、收敛性和计算成本
- **跨工具对比**：不同工具之间统一拓扑、参数、初值、步长、插值和输出采样后的结果一致性

误差指标的形式化表达为：

$$\epsilon_{\mathrm{rms}} = \sqrt{\frac{\sum_k (y_k - y_k^{\mathrm{ref}})^2}{\sum_k (y_k^{\mathrm{ref}})^2}}, \qquad \epsilon_F = \frac{|F - F^{\mathrm{ref}}|}{|F^{\mathrm{ref}}|}$$

其中 $y_k$ 是波形采样，$F$ 是峰值、到达时间、频率或动作时间等特征量。报告这些指标时必须同时说明参考解来源、采样窗口、滤波处理和归一化方式。

<div style="text-align:center;margin:16px 0;">
<table border="1" cellpadding="8" cellspacing="0" style="margin:auto;border-collapse:collapse;font-size:13px;">
<tr style="background:#f8fafc;">
  <th colspan="3" style="font-weight:bold;border:1px solid #ccc;padding:8px;">模型验证与基准测试的方法体系</th>
</tr>
<tr style="background:#dbeafe;">
  <td style="border:1px solid #ccc;padding:8px;text-align:center;font-weight:bold;color:#2563eb;">单元验证<br><span style="font-size:11px;color:#475569;">RLC/开关/变压器/线路<br>与解析解/频响对比</span></td>
  <td style="border:1px solid #ccc;padding:8px;text-align:center;font-weight:bold;color:#16a34a;">子系统验证<br><span style="font-size:11px;color:#475569;">换流器/线路段/保护链路<br>接口变量与事件时序</span></td>
  <td style="border:1px solid #ccc;padding:8px;text-align:center;font-weight:bold;color:#d97706;">系统级基准<br><span style="font-size:11px;color:#475569;">IEEE/CIGRE测试系统<br>统一扰动+波形/成本对比</span></td>
</tr>
<tr style="background:#ede9fe;">
  <td style="border:1px solid #ccc;padding:8px;text-align:center;font-weight:bold;color:#7c3aed;">回放仿真<br><span style="font-size:11px;color:#475569;">POI录波驱动IBR模型<br>Sun et al. 2024</span></td>
  <td style="border:1px solid #ccc;padding:8px;text-align:center;font-weight:bold;color:#7c3aed;">跨工具对比<br><span style="font-size:11px;color:#475569;">ATP vs NETOMAC vs RTDS<br>Lehn & Rittiger 1995</span></td>
  <td style="border:1px solid #ccc;padding:8px;text-align:center;font-weight:bold;color:#7c3aed;">HIL基准验证<br><span style="font-size:11px;color:#475569;">RTDS+硬件闭环+TFR<br>Zhou et al. 2021</span></td>
</tr>
<tr style="background:#fef3c7;">
  <td style="border:1px solid #ccc;padding:8px;" colspan="3">
    <strong style="color:#d97706;">误差量化指标：</strong>
    <code style="font-size:11px;">$\epsilon_{\mathrm{rms}}$</code> 归一化波形均方根误差 ·
    <code style="font-size:11px;">$\epsilon_F$</code> 特征量相对误差 ·
    <code style="font-size:11px;">MAE</code> 归一化平均绝对误差
  </td>
</tr>
<tr style="background:#dcfce7;">
  <td style="border:1px solid #ccc;padding:8px;" colspan="3">
    <strong style="color:#16a34a;">经典基准测试系统：</strong>
    IEEE-39 / IEEE-118 节点系统 · CIGRE HVDC Benchmark (±400kV/600MW) · Nelson River 三双极LCC-HVDC
  </td>
</tr>
<tr style="background:#fee2e2;">
  <td style="border:1px solid #ccc;padding:8px;" colspan="3">
    <strong style="color:#dc2626;">关键原则：</strong>
    <span style="font-size:11px;">误差准则必须绑定模型类型/测试系统/采样窗口/参考解 · 只比较峰值可能遗漏相位/波前/频率差异 · 跨工具一致≠真实准确</span>
  </td>
</tr>
</table>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 模型验证与基准测试的方法体系总览</p>

## EMT 中的作用

EMT 验证和基准测试用于解决以下核心工程问题：

**1. 监管合规与并网标准**：NERC 的 MOD-26、FAC-02、MOD-32 和 TP/0-001 标准项目，以及 IEEE P2800.2 均要求 EMT 模型经过验证。发电业主对模型准确性负有责任，但行业正推动强制性验证要求。

**2. 模型选择与精度-效率权衡**：如 Beddard 2015 对 MMC 三种详细建模技术（TDM/DEM/AM）的比较所示，不同模型在精度和仿真速度上差异显著。基准测试为模型选择提供量化依据。

**3. 跨工具结果一致性**：Lehn 和 Rittiger 1995 对 ATP/EMTP 与 NETOMAC 的 HVDC 仿真对比表明，即使使用相同系统参数，不同工具的数值积分、时间步长和开关检测机制也会导致结果差异。基准测试揭示这些差异的来源和量级。

**4. 实时仿真和 HIL 模型移植**：Zhou 2021 在 Nelson River 多馈入 HVDC 系统中的实践表明，实时 HIL 仿真必须额外验证实时约束（deadline、overrun、I/O 延迟和模型简化），否则不能支撑 HIL 有效性。

**5. 高比例 IBR 电网的基准模型**：Marthi 2024 构建的含多个大型光伏电站的电网级高保真 EMT 基准模型，为研究多 PV 电站在故障和弱电网条件下的动态行为提供了公开可复用的测试平台。

## EMT 建模与验证方法体系

EMT 模型验证不是单一方法，而是由多层次、多策略组成的体系。下面从三个维度分类：

### 3.1 验证策略分类

**策略一：解析解/已知稳态对比（单元验证）**

对 RLC、开关、变压器、线路或控制器单独测试，与解析解或已知稳态结果对比。这是最基础的验证层次，适用于确认元件模型的基本正确性。例如，传输线的 Bergeron 模型可以与行波解析解对比；变压器模型可以与空载/短路试验数据对比。

**策略二：高保真基准模型对比（子系统验证）**

选择一个包含尽可能多物理细节的"基准模型"（Benchmark Model），将简化模型的结果与之对比。Beddard 2015 采用全详细模型（TDM, Terminal Detailed Model）作为基准，对等效详细模型（DEM, Equivalent Detailed Model）和平均值模型（AM, Average Model）进行对比。误差指标使用归一化平均绝对误差（Normalized MAE）：

$$\mathrm{MAE} = \frac{1}{N}\sum_{k=1}^{N} \frac{|y_k - y_k^{\mathrm{ref}}|}{y_{\mathrm{base}}}$$

其中 $y_{\mathrm{base}}$ 是归一化基准值（通常为额定值或稳态值），$N$ 是采样点数。

**策略三：跨工具/跨平台对比（系统基准）**

在 IEEE、CIGRE 或工程系统中设置统一扰动，对比不同工具（PSCAD、EMTDC、RTDS、ATP）的结果。Lehn 和 Rittiger 1995 的经典研究使用 CIGRE HVDC Benchmark System（±400 kV, 600 MW）作为统一测试平台，对比 ATP 和 NETOMAC 在相同参数下的仿真结果。

**策略四：回放仿真（Play-back Simulation）**

Sun 等 2024 提出的创新验证方法：将外部系统等效为 POI（Point-of-Interconnection）瞬时电压回放源，用现场录波数据直接驱动 EMT 模型，从而隔离"模型本身是否正确"这一问题。核心优势是不需重建完整外部电网和故障过程。

### 3.2 模型精度-效率权衡框架

Sano 等 2022 对并网逆变器五种建模方法（SW、VI、AV、CCI、SCI）的系统比较，建立了精度-效率权衡的通用框架：

| 模型 | 时间步长 | 相对计算时间 | 精度等级 | 适用场景 |
|------|----------|-------------|----------|----------|
| 开关模型 (SW) | 2 μs | 1.0×（基准） | 最高 | 死区谐波、故障暂态、电路拓扑验证 |
| 电压插值模型 (VI) | 10 μs | ~0.2× | 高 | 系统故障、谐振分析、PLL动态 |
| 平均值模型 (AV) | 100 μs | ~0.02× | 中 | 大规模系统潮流、稳定性分析 |
| 受控电流注入模型 (CCI) | 600 μs | ~0.005× | 中 | 快速暂态、多逆变器系统 |
| 简化电流注入模型 (SCI) | 1000 μs | ~0.002× | 低 | 大规模系统潮流、初步设计 |

计算时间比满足近似反比关系：$T_{\mathrm{ref}}/T_{\mathrm{sim}} \propto \Delta t_{\mathrm{sim}}/\Delta t_{\mathrm{ref}}$，其中 $\Delta t$ 为仿真时间步长。

### 3.3 混合仿真接口验证

Jalili-Marandi 等 2009（IEEE Task Force）构建了 TS-EMT 混合仿真的标准化接口技术框架，其验证要点包括：

- **网络分割**：将系统划分为 TS 主网（基频相量模型、毫秒级步长）与 EMT 局部详细网络（瞬时值模型、微秒级步长）
- **接口等值**：在接口母线处使用戴维南/诺顿等效实现双向数据交换
- **多速率同步**：TS 步长 $\Delta t_{\mathrm{TS}}$（通常 1~10 ms）与 EMT 步长 $\Delta t_{\mathrm{EMT}}$（通常 1~50 μs），步长比 $N = \Delta t_{\mathrm{TS}} / \Delta t_{\mathrm{EMT}}$ 通常在 50~200 范围内
- **相量-瞬时值转换**：$v_{abc}(t) = \sqrt{2}\,\mathrm{Re}\{V_{abc} e^{j\omega_0 t}\}$ 将 TS 侧基频相量重构为 EMT 侧三相瞬时电压

## 形式化表达

### 误差指标

**归一化均方根误差**（波形级）：

$$\epsilon_{\mathrm{rms}} = \sqrt{\frac{\sum_{k=1}^{N} (y_k - y_k^{\mathrm{ref}})^2}{\sum_{k=1}^{N} (y_k^{\mathrm{ref}})^2}}$$

**特征量相对误差**：

$$\epsilon_F = \frac{|F - F^{\mathrm{ref}}|}{|F^{\mathrm{ref}}|}$$

其中 $F$ 为峰值、到达时间、频率或动作时间等特征量。

**归一化平均绝对误差**（Beddard 2015）：

$$\mathrm{MAE} = \frac{1}{N}\sum_{k=1}^{N} \frac{|y_k - y_k^{\mathrm{ref}}|}{y_{\mathrm{base}}}$$

### 接口验证指标（混合仿真）

**接口功率不平衡度**：

$$\Delta P_{\mathrm{interface}} = \frac{|P_{\mathrm{TS}\to\mathrm{EMT}} - P_{\mathrm{EMT}\to\mathrm{TS}}|}{P_{\mathrm{base}}}$$

Jalili-Marandi 2009 指出，接口数据交换引入的数值反射误差应控制在 < 0.5%，功率不平衡度 < 0.2%。

**步长比约束**：当 $N > 500$ 时，接口相位漂移显著增加，需引入预测-校正算法补偿。

### 回放仿真初始化

**同步表法初始化电压幅值**：

$$V_{\mathrm{init}} = \sqrt{2} \cdot V_{\mathrm{RMS}}$$

**初始化相位角匹配**：

$$\theta_{\mathrm{init}} = \arcsin\left(\frac{v(t_0)}{V_{\mathrm{peak}}}\right)$$

其中 $v(t_0)$ 为录波起始时刻瞬时值，$V_{\mathrm{peak}}$ 为峰值电压。

### 混合仿真 TS-EMT 接口方程

**TS 区域微分代数方程**：

$$\dot{x} = f(x, y), \quad 0 = g(x, y)$$

**EMT 节点导纳方程**：

$$G v(t) = i(t) - i_{\mathrm{hist}}(t)$$

**相量至瞬时值转换**：

$$v_{\mathrm{inst}}(t) = \sqrt{2}\,|V|\cos(\omega_0 t + \angle V)$$

## 量化性能边界

### Beddard 2015：MMC 模型精度对比（稳态工况）

在 1000 MW 稳态运行点，TDM 作为基准，DEM 和 AM 的归一化 MAE 为：

- 稳态 AC 电压波形：DEM 与 TDM 差异 < 1%，AM 与 TDM 差异 < 2.5%
- 稳态直流电压波形：三种模型均能准确复现

### Beddard 2015：MMC 模型精度对比（故障工况）

直流线-线故障（4.5 s 触发）：

- DEM 和 AM 波形与 TDM 几乎一致（误差 < 1% ~ 2.5%）
- AM 在故障期间的平均误差略高于 DEM
- DEM 在换流器阻塞时可能产生数值误差

### Beddard 2015：仿真速度对比（IEEE 39 节点系统含 MMC）

| 模型 | 仿真时间 (s) | 相对速度 |
|------|-------------|----------|
| TDM | 基准 | 1.0× |
| DEM | 显著缩短 | 约 2~5× |
| AM（单组） | 最短 | 约 5~10× |
| AM（每组1个SM） | 较长 | 约 1~2× |

### Marthi 2024：光伏电站基准模型验证

- 多速率控制架构实现逆变器（50–100 μs）与 PPC（100–1000 ms）的硬件级时序匹配，控制步长跨度达 1000 倍
- 故障前稳态功率：IBR-1 ≈ 115 MW，IBR-2 ≈ 110 MW，IBR-3 ≈ 230 MW，总并网容量 470 MW
- 短路比从 25/27.5/15 降至 10/9/8 后，IBR-3 有功功率跌落幅度显著增大，验证了 SCR < 10 时弱电网对逆变器稳定性的强约束
- 故障电气距离与功率损失呈强正相关：极近故障导致 IBR-1 功率降至 0 MW，远距离故障功率损失 < 5%

### Sano 2022：逆变器模型精度-效率权衡

- SW 模型（2 μs 步长）作为基准，VI 模型（10 μs）在系统故障和 PLL 动态下波形重合度 > 98%
- AV 模型（100 μs）在功率阶跃响应中与 SW 模型高度一致，但在低阶谐波和死区效应上无法复现
- CCI 模型（600 μs）计算时间仅为 SW 模型的 ~0.5%，但在电压跌落时的尖峰电流模拟中存在误差
- SCI 模型无法模拟阻塞操作和直流故障

### Lehn 和 Rittiger 1995：ATP vs NETOMAC 跨工具对比

- 在 CIGRE HVDC Benchmark System（±400 kV, 600 MW）上，当 ATP 时间步长约为 NETOMAC 的 1/5 时，两者结果高度一致
- NETOMAC 采用变步长，在相同精度下计算速度比 ATP 快约 10 倍
- ATP 固定时间步长在开关事件检测上引入 1 个步长延迟，而 NETOMAC 的变步长仅受数值精度限制
- 当 ATP 时间步长超过 20 μs 时，瞬态仿真结果开始退化

### Zhou 2021：Nelson River 混合 HIL 基准

- Bipole I：1854 MW, ±463.5 kV，每极 3 个六脉波阀组
- Bipole II：2000 MW, ±500 kV，每极 2 个十二脉波阀组
- 两条直流线路约 900 km，Bipole I/II 承担 Manitoba Hydro 约 70% 供电
- Dorsey 站 14 个等效阀组和 9 台调相机导致实时计算瓶颈
- 采用同组降阶建模而非接口变压器分割，避免了 1 个实时仿真步长的接口延迟
- RTDS 控制模型替代了 PSCAD/EMTDC 中超过 100 个自定义控制模块

### Sun 等 2024：IBR 回放仿真验证

- 录波数据扰动前稳态段通常不足 1 秒（实测示例仅 0.23 秒），而 IBR EMT 模型完整启动需超过 1 秒
- 波形扩展法相比同步表法在信号切换瞬间产生的暂态扰动幅值更低
- PSCAD 多表计平滑时间常数必须严格设置为 0 秒，否则内部滤波会扭曲高频暂态特征

## 关键技术挑战

### 挑战一：参考解的选择与可信度

基准测试的核心是参考解（Reference Solution）的选择。常见选择包括：
- **全详细模型**（TDM）：精度最高但计算成本最大，适合作为子系统验证的参考
- **解析解**：仅适用于简单 RLC 电路和均匀传输线，不适用于复杂网络
- **跨工具一致结果**：Lehn 和 Rittiger 1995 表明，当工具时间步长设置适当时，ATP 和 NETOMAC 结果高度一致，可作为参考解
- **现场录波**：Sun 等 2024 的回放仿真方法利用现场 POI 电压录波作为边界条件，但录波本身的质量（采样率、噪声、同步精度）影响验证可信度

### 挑战二：时间步长对结果的影响

不同工具和时间步长设置对仿真结果有显著影响：
- Lehn 和 Rittiger 1995 发现 ATP 时间步长从 5 μs 增加到 20 μs 时，瞬态结果开始退化
- 开关事件检测精度受时间步长限制：ATP 固定步长引入 1 个步长延迟，NETOMAC 变步长仅受数值精度限制
- 混合仿真中步长比 $N > 500$ 时接口相位漂移显著增加

### 挑战三：模型简化与精度损失

Sano 2022 和 Beddard 2015 的研究表明，模型简化带来的精度损失具有场景依赖性：
- AV 模型在功率阶跃响应中与 SW 模型一致，但在死区谐波和低阶谐波方面无法复现
- AM 模型在稳态和故障暂态中精度可接受，但在换流器阻塞时可能产生数值误差
- SCI 模型完全无法模拟阻塞操作和直流故障

### 挑战四：实时仿真的计算瓶颈

Zhou 2021 在 Nelson River 系统中的实践表明，实时 HIL 仿真的瓶颈常不只是电磁元件精度，而是遗留控制复现、模型分层集成、实时计算分区和硬件接口一致性。Dorsey 站 14 个等效阀组和 9 台调相机的建模导致 RTDS 计算瓶颈，采用接口变压器分割会引入 1 个实时仿真步长延迟。

## 适用边界与选择指南

### 验证方法选择指南

| 验证目标 | 推荐方法 | 参考解 | 典型误差指标 |
|----------|----------|--------|-------------|
| 元件级正确性 | 解析解/频响对比 | 解析解 | $\epsilon_{\mathrm{rms}} < 1\%$ |
| 子系统精度 | 高保真基准模型对比 | TDM/全详细模型 | MAE < 2.5% |
| 跨工具一致性 | 统一参数跨工具仿真 | 变步长工具结果 | $\epsilon_{\mathrm{rms}} < 0.5\%$ |
| IBR 模型验收 | 回放仿真（POI 录波） | 现场 POW 数据 | 波形重合度 > 95% |
| 实时 HIL 验证 | 现场 TFR + 分级故障 | 现场录波 | 动态响应定性吻合 |

### 模型选择指南（基于精度-效率需求）

| 研究类型 | 推荐模型 | 理由 |
|----------|----------|------|
| 死区谐波分析 | SW / VI | 需精确复现开关动作和高频谐波 |
| 系统故障暂态 | SW / VI / AV | VI 在保持精度的同时大幅降低计算成本 |
| 大规模系统潮流 | AV / CCI / SCI | 计算效率优先，精度要求较低 |
| 保护动作时序 | SW / VI | 需精确的过电压/过电流波形 |
| 控制稳定性分析 | VI / AV | 需保留 PLL 和电流控制动态 |
| 电路拓扑验证 | SW | 唯一能验证内部电路行为的模型 |
| 故障穿越测试 | SW / VI / AV | 需模拟阻塞操作和尖峰电流 |

### 工具选择指南

| 场景 | 推荐工具 | 理由 |
|------|----------|------|
| 离线详细仿真 | PSCAD/EMTDC | 元件库最完整，社区验证最充分 |
| 实时 HIL | RTDS | 硬件闭环支持，工业界标准 |
| 大规模系统 | ATP + 稳定程序混合 | 兼顾全网机电动态和局部电磁细节 |
| 快速原型验证 | MATLAB/Simulink | 开发效率高，适合算法验证 |

## 相关方法 / 相关模型 / 相关主题

- [[emt-simulation]] — 电磁暂态仿真的基础
- [[numerical-integration]] — 数值积分方法影响仿真精度
- [[nodal-admittance-matrix]] — 节点导纳矩阵是 EMT 网络求解的核心
- [[frequency-dependent-line-model]] — 频率相关线路模型的验证
- [[transformer-model]] — 变压器模型的验证
- [[hil-simulation]] — 硬件在环仿真需要额外验证实时约束
- [[real-time-simulation]] — 实时仿真验证
- [[model-order-reduction]] — 模型降阶需要 benchmark 支撑简化误差
- [[vector-fitting]] — 矢量拟合需要 benchmark 验证拟合精度
- [[passivity-enforcement]] — 无源性强制需要 benchmark 验证
- [[simulation-practice-guide]] — 工程仿真流程和常见问题诊断
- [[ieee-118-bus-system]] — 系统级测试对象
- [[ieee-39-bus-system]] — 系统级测试对象
- [[cigre-hvdc-benchmark]] — CIGRE HVDC 基准测试系统

## 来源论文

- **Marthi 等 2024** — 构建含多个大型光伏电站的电网级高保真 EMT 基准模型，公开 PSCAD/PSCAD-Fortran 实现，在 IEEE-39 节点系统上验证故障和弱电网场景下的动态行为
- **Sun 等 2024** — 提出基于 POI 瞬时电压回放驱动的 IBR EMT 模型完整验证方案，设计两种初始化技术（同步表法和波形扩展法），使用现场 POW 录波和仿真数据验证
- **Zhou 等 2021** — 建立 Nelson River 三双极 LCC-HVDC 系统的大规模混合实时 HIL 仿真平台，采用模块化逐级组合策略和现场 TFR 基准验证
- **Beddard 等 2015** — 首次独立比较 MMC 三种详细建模技术（TDM/DEM/AM）在精度和仿真速度上的差异，使用归一化 MAE 作为统一误差指标
- **Sano 等 2022** — 系统比较五种并网逆变器建模方法（SW/VI/AV/CCI/SCI）的动态行为和计算时间，建立精度-效率权衡框架和场景-模型选择指南
- **Jalili-Marandi 等 2009**（IEEE Task Force）— 系统构建 TS-EMT 混合仿真的标准化接口技术框架，讨论网络分割、接口等值、多速率同步和频移集成方法
- **Lehn 和 Rittiger 1995** — 经典跨工具对比研究，对比 ATP/EMTP 与 NETOMAC 在 CIGRE HVDC Benchmark System 上的仿真结果，揭示时间步长对结果的影响
- **Task Force on Interfacing Techniques（de León 等）2013** — 系统总结潮流程序到 EMTP 型程序的数据翻译器开发经验与工程教训，包括数据语义映射、参数转换、缺失数据补全和格式不一致处理
- **Liu 等 2025** — 建立 275 kV 压力充油管型电缆的宽频 EMT 模型，利用 MoM-SO 方法计算单位长度参数并用现场测量波形验证投切、故障和雷击暂态仿真
