---
title: "电磁暂态仿真验证 (EMT Simulation Verification)"
type: method
tags: [verification, validation, emt, benchmark, accuracy, testing]
created: "2026-05-02"
updated: "2026-05-15"
---

# 电磁暂态仿真验证 (EMT Simulation Verification)

## 定义

电磁暂态仿真验证（EMT Simulation Verification）是把 EMT 模型、数值算法或系统算例的输出与明确参考进行对照，并说明差异是否可由模型假设、参数、步长、接口或测量误差解释的过程。验证的核心不是证明模型"正确"，而是系统地建立**证据边界**（evidence boundary）：在什么对象、什么工况、什么参考基线、什么指标和什么容差下，当前的仿真输出可以置信。

参考基线可以是五类之一：解析解（含 RLC 电路、理想传输线、线性状态方程等可解析求解的对象）、小步长离线基线、另一 EMT 平台或实时仿真器、实测/现场录波（含 HIL 采集）、以及已审核的基准算例。任何"通过验证"的结论都必须绑定这五个维度；跨维度外推需要新的验证证据。

## EMT 中的角色

EMT 仿真用于开关暂态、换流器控制、保护动作、线路行波、绝缘配合和混合仿真接口分析。验证是建立仿真可信度的唯一系统性手段，回答以下问题：

- **验证对象**：被验证的是元件模型、控制器算法、网络求解器、接口算法还是整套系统？
- **参考类型**：参考结果来自解析推导、实测录波、离线基线、实时平台还是跨工具对比？
- **对比维度**：比较的是波形、特征量（峰值/积分值）、事件时刻（故障清除时间、继电保护动作时刻）、频谱、能量平衡、实时 deadline，还是保护逻辑序列？
- **证据覆盖**：当前证据能否覆盖目标用途，还是只覆盖来源论文中的算例边界？

## 核心机制：六步审计流程

一个可审计的 EMT 验证流程通常包含六个步骤：

**第一步：定义验证对象和用途**
- 明确是验证 [[mmc-model]] 端口外特性、 [[trapezoidal-rule]] 积分误差，还是 [[hil-simulation]] 闭环接口
- 用途决定验证的严格程度和参考类型选择

**第二步：建立参考基线**
说明参考来源的解析公式、实测数据、离线 EMT、小步长结果或硬件平台的具体获取方式。参考的质量直接决定验证结论的可信度。

**第三步：固定输入条件**
包括拓扑、参数、初始状态、控制设置、故障时刻、采样频率和步长。任一条件的不对齐都会使波形差异无法归因于算法误差。

**第四步：对齐输出数据**
处理时间零点偏移、单位制转换、标幺基准差异、相位对准、采样率重采样和滤波方式统一。时间零点偏移是跨工具对比中最常见的误差来源。

**第五步：计算误差指标**
每个指标必须解释为物理量或数值误差，而非孤立分数。

**第六步：记录失效样例和敏感参数**
记录失败样例、敏感参数和不可外推范围——这是验证报告中最容易被忽略却最有价值的部分。

## 形式化表达：误差指标体系

### 波形均方根误差

$$e_{\mathrm{rms}} = \sqrt{\frac{\sum_{k=1}^{N}\left(y_k - y_k^{\mathrm{ref}}\right)^2}{\sum_{k=1}^{N}\left(y_k^{\mathrm{ref}}\right)^2}}$$

其中 $y_k$ 为被评估波形在时刻 $t_k$ 的采样值，$y_k^{\mathrm{ref}}$ 为参考波形对应时刻的值，$N$ 为采样点总数。当参考值在某些时刻接近零（如电压过零点附近）时，单独使用相对误差会给出病态结果；此时应同时报告绝对误差：

$$e_{\mathrm{abs}} = \frac{1}{N}\sum_{k=1}^{N}\left|y_k - y_k^{\mathrm{ref}}\right|$$

### 事件时刻误差

对于故障清除时间 $t_{\mathrm{clear}}$、保护动作时刻 $t_{\mathrm{trip}}$ 等离散事件，对齐后报告时刻偏差：

$$\Delta t_{\mathrm{event}} = \left| t_{\mathrm{event}}^{\mathrm{sim}} - t_{\mathrm{event}}^{\mathrm{ref}} \right|$$

### 频谱误差

对谐波分析场景，比较指定次数谐波的幅值和相位：

$$e_{\mathrm{harm},\,h} = \frac{\left| I_h^{\mathrm{sim}} - I_h^{\mathrm{ref}} \right|}{\left| I_h^{\mathrm{ref}} \right|} \times 100\%, \quad h = 2, 3, 5, \ldots$$

### 能量误差

对涉及积分能量的场景（如开关损耗、线路传输能量），报告能量偏差：

$$e_{\mathrm{energy}} = \frac{\left| E_{\mathrm{sim}} - E_{\mathrm{ref}} \right|}{E_{\mathrm{ref}}} \times 100\%$$

## 五类验证方法

| 类型 | 参考对象 | EMT 用途 | 主要边界 |
|------|----------|----------|----------|
| **解析验证** | RLC 电路、理想线路、线性状态方程等可解析求解对象 | 检查积分公式、伴随电路和初始条件的数值实现 | 只覆盖简化模型；无法覆盖饱和、限幅、保护逻辑 |
| **小步长基线** | 更小步长或更精细网络拓扑的离线仿真 | 评估插值误差、开关处理误差、平均值模型误差、降阶误差 | 小步长结果本身也受模型假设限制；两者模型假设必须一致 |
| **跨工具对比** | 另一个 EMT 仿真器或实时仿真平台 | 发现建模约定、实现细节差异和数值稳定性差异 | 不能自动判定哪一方更接近物理真实；需记录双方步长、积分方法、开关模型 |
| **实测/现场录波** | 试验录波、故障录波、HIL 采集 | 校核工程事件复现、控制保护动作序列 | 测量链带宽、传感器标定、故障阻抗估计和工况复现都会引入误差 |
| **回归验证** | 已审核基准算例及预期输出 | 防止工具升级、模型库更新或转换流程引入退化 | 只能覆盖已有样例空间；新场景可能出现未覆盖的失效模式 |

## 关键技术挑战

### 对齐误差的来源分离

当波形出现差异时，误差来源可能是模型假设不一致、参数值不准确、数值积分误差、接口同步误差或测量链误差。EMT 验证的难点在于这些来源经常耦合。分离方法：控制参数扫描（将某一参数在合理范围内连续变化，观察误差趋势）和接口隔离测试（将接口算法单独用已知输入测试）。

### 参考自身的可信度

解析基线依赖数学推导的正确性；小步长基线依赖模型假设的一致性；跨工具对比需要同时记录双方的数值设置；实测录波需要标定链的完整校准。任何一个环节的参考自身不可信，验证结论就不可靠。

### 非线性与开关事件的验证覆盖

在强非线性系统（含饱和、限幅、状态跳变）中，某一参数下的验证成功不能直接外推到另一参数。验证必须覆盖关键参数边界，并在报告中明确标注参数敏感区间。

### IBR 模型的初始化对齐

IBR（Inverter-Based Resource）EMT 模型验证面临特殊挑战：录波扰动前的稳态段往往不足以为IBR的PLL、滤波器等内部状态提供收敛初值。Sun et al.（2024）提出两类解决方案：一是构造稳态三相电压让控制器先行启动，二是对端子母线做初始化以保证切入录波时刻的电压幅值和相位连续。

### 端口级验证 vs 网络级验证

验证可以在端口级（单个设备的电压-电流特性）进行，也可以在网络级（系统响应、故障穿越行为）进行。网络级验证需要端口级验证作为前提，但不等于端口级验证成功就能保证网络级正确。网络级验证必须考虑接口算法、延迟和耦合路径的影响。

## 量化性能边界

### 小步长基线加速比与误差关系

| 步长比（基准/被测） | 典型波形误差 | 适用场景 |
|--------------------|--------------|----------|
| 10× | $< 0.1\%$ | 平滑波形区域 |
| 50× | $0.1\% - 1\%$ | 含开关事件但无硬过零点 |
| 100× | $1\% - 5\%$ | 仅用于定性误差趋势判断 |

注：误差随步长比非单调变化——某些系统在特定步长比下会出现数值共振放大事实（Accuracy Evaluation of EMT Simulation Algorithms, Zhao et al. 2022）。

### 跨工具验证典型偏差范围

| 验证类型 | 典型波形差异 | 注意事项 |
|----------|--------------|----------|
| 解析 vs 数值（梯形法） | RMS 误差 $< 0.01\%$（平滑区） | 开关附近误差可能骤增 |
| 梯形 vs 后向欧拉 | 相位差约 $\Delta t / 2$ | BE 数值阻尼更大 |
| 离线 EMT vs 实时平台 | $1\% - 5\%$（事件时刻对齐后） | 实时时钟量化误差 |

### IBR 模型验证加速比

Sun et al.（2024）提出的 EMT 回放验证方法，在 PSCAD 平台上对 IBR 模型进行 POI（Point of Interface）电压回放验证。具体加速比取决于IBR数量和接口网络复杂度，原文未给出统一数值，但验证流程本身相比全系统 EMT 重建可显著降低计算成本。

### 大规模 XFC 充电站加速比

| 场景 | XFC 数量 | 加速比 | 关键变量误差 |
|------|----------|--------|--------------|
| 配电系统 | 15 个 XFC | 最高 18× | $< 5\%$（直流母线电压、电感电流、滤波电容电压）|
| 输配电联合系统 | 300 个 XFC | 最高 271× | $< 5\%$（同上前三指标）|

来源：Electromagnetic Transient Simulation Algorithms for Evaluation of Large-Scale Extreme Fast Charging Stations, Debnath & Choi (2023)，测试平台 PSCAD/EMTDC，步长 $1\,\mu\text{s}$。

### PV 电站模型验证边界

Marthi et al.（2024）构建的 IEEE-39 节点接入多大型光伏电站基准模型，通过 PSCAD/PSCAD-Fortran 实现。验证覆盖故障条件下多 PV 电站响应和不同短路比（SCR）条件下系统动态行为。原文未给出逐点波形误差数值，验证结论限于所构建的 IEEE-39 系统、配置的 PV 电站规模和所选故障/SCR 工况。

## 适用边界与选择指南

| 验证目标 | 推荐参考类型 | 关键注意事项 |
|----------|--------------|--------------|
| 数值积分算法精度验证 | 解析验证（RLC 基准） | 只能覆盖线性集总元件 |
| 开关事件时刻精度 | 小步长基线 | 步长比需 $\ge 50\times$ |
| 新模型在工程系统中的有效性 | 实测/现场录波 | 需完整的测量链标定 |
| 跨平台仿真一致性 | 跨工具对比 | 双方步长、积分方法、开关模型必须对齐记录 |
| 模型库/工具版本回归 | 回归验证 | 基准算例需覆盖关键场景 |
| IBR 设备级认证 | POI 电压回放 | 需IBR初值初始化技术 |
| 大规模电力电子系统效率 | 小步长基线+性能测试 | 误差$<5\%$ 且加速比 $>10\times$ |

## SVG 验证方法体系架构

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 520" xmlns="http://www.w3.org/2000/svg">
  <!-- 第一层：输入节点 -->
  <rect x="30" y="30" width="200" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="130" y="60" font-family="Arial,sans-serif" font-size="13" text-anchor="middle" fill="#1e40af">解析验证基线</text>

  <rect x="30" y="100" width="200" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="130" y="130" font-family="Arial,sans-serif" font-size="13" text-anchor="middle" fill="#1e40af">小步长离线基线</text>

  <rect x="30" y="170" width="200" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="130" y="200" font-family="Arial,sans-serif" font-size="13" text-anchor="middle" fill="#1e40af">跨工具/实时平台</text>

  <rect x="30" y="240" width="200" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="130" y="270" font-family="Arial,sans-serif" font-size="13" text-anchor="middle" fill="#1e40af">实测/现场录波</text>

  <rect x="30" y="310" width="200" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="130" y="340" font-family="Arial,sans-serif" font-size="13" text-anchor="middle" fill="#1e40af">回归基准算例</text>

  <!-- 第二层：六步审计流程 -->
  <rect x="300" y="30" width="140" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="370" y="50" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#166534">1. 定义对象</text>
  <text x="370" y="66" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#166534">&amp; 用途</text>

  <rect x="300" y="100" width="140" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="370" y="120" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#166534">2. 建立</text>
  <text x="370" y="136" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#166534">参考基线</text>

  <rect x="300" y="170" width="140" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="370" y="190" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#166534">3. 固定</text>
  <text x="370" y="206" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#166534">输入条件</text>

  <rect x="300" y="240" width="140" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="370" y="260" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#166534">4. 对齐</text>
  <text x="370" y="276" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#166534">输出数据</text>

  <rect x="300" y="310" width="140" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="370" y="330" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#166534">5. 计算</text>
  <text x="370" y="346" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#166534">误差指标</text>

  <rect x="300" y="380" width="140" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="370" y="400" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#166534">6. 记录失效</text>
  <text x="370" y="416" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#166534">边界</text>

  <!-- 第三层：误差指标 -->
  <rect x="510" y="30" width="150" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="585" y="50" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#92400e">RMS 波形误差</text>
  <text x="585" y="66" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#92400e">e_rms</text>

  <rect x="510" y="100" width="150" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="585" y="120" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#92400e">事件时刻偏差</text>
  <text x="585" y="136" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#92400e">Δt_event</text>

  <rect x="510" y="170" width="150" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="585" y="190" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#92400e">谐波幅值误差</text>
  <text x="585" y="206" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#92400e">e_harm,h</text>

  <rect x="510" y="240" width="150" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="585" y="260" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#92400e">能量偏差</text>
  <text x="585" y="276" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" fill="#92400e">e_energy</text>

  <!-- 第四层：验证结论 -->
  <rect x="730" y="130" width="140" height="120" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="800" y="160" font-family="Arial,sans-serif" font-size="13" text-anchor="middle" fill="#5b21b6">验证结论</text>
  <text x="800" y="182" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="#6b21b6">证据边界报告</text>
  <text x="800" y="200" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="#6b21b6">失效模式记录</text>
  <text x="800" y="218" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="#6b21b6">参数敏感区间</text>
  <text x="800" y="236" font-family="Arial,sans-serif" font-size="11" text-anchor="middle" fill="#6b21b6">外推限制条件</text>

  <!-- 箭头：参考基线 → 六步流程 -->
  <line x1="230" y1="55" x2="300" y2="55" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="230" y1="125" x2="300" y2="125" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="230" y1="195" x2="300" y2="195" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="230" y1="265" x2="300" y2="265" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="230" y1="335" x2="300" y2="335" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- 箭头：六步流程 → 误差指标 -->
  <line x1="440" y1="55" x2="510" y2="55" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="440" y1="125" x2="510" y2="125" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="440" y1="195" x2="510" y2="195" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="440" y1="265" x2="510" y2="265" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- 箭头：误差指标 → 验证结论 -->
  <line x1="660" y1="55" x2="730" y2="170" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="660" y1="125" x2="730" y2="170" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="660" y1="195" x2="730" y2="190" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="660" y1="265" x2="730" y2="230" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- 步骤间的垂直连接线 -->
  <line x1="370" y1="80" x2="370" y2="100" stroke="#333" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="370" y1="150" x2="370" y2="170" stroke="#333" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="370" y1="220" x2="370" y2="240" stroke="#333" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="370" y1="290" x2="370" y2="310" stroke="#333" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="370" y1="360" x2="370" y2="380" stroke="#333" stroke-width="1" stroke-dasharray="3,2"/>

  <!-- 指标间的垂直连接线 -->
  <line x1="585" y1="80" x2="585" y2="100" stroke="#333" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="585" y1="150" x2="585" y2="170" stroke="#333" stroke-width="1" stroke-dasharray="3,2"/>
  <line x1="585" y1="210" x2="585" y2="240" stroke="#333" stroke-width="1" stroke-dasharray="3,2"/>

  <!-- 底部图例 -->
  <rect x="30" y="440" width="16" height="16" rx="2" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="52" y="452" font-family="Arial,sans-serif" font-size="11" fill="#333">参考基线（输入）</text>

  <rect x="190" y="440" width="16" height="16" rx="2" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="212" y="452" font-family="Arial,sans-serif" font-size="11" fill="#333">六步审计流程</text>

  <rect x="370" y="440" width="16" height="16" rx="2" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="392" y="452" font-family="Arial,sans-serif" font-size="11" fill="#333">误差指标</text>

  <rect x="510" y="440" width="16" height="16" rx="2" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="532" y="452" font-family="Arial,sans-serif" font-size="11" fill="#333">验证结论</text>

  <!-- 定义箭头 -->
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#333"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · EMT 仿真验证方法体系：五类参考基线经六步审计流程产出误差指标，最终形成带边界的验证结论</p>

## 代表性证据

| 来源 | 可支持的验证认识 | 证据边界 |
|------|------------------|----------|
| [[an-improved-high-accuracy-interpolation-method-for-switching-devices-in-emt-simu]]（Na et al. 2023）| 开关插值方法可用小步长基线和电力电子算例比较波形、事件时刻与虚假振荡；核心机制是半步后向欧拉解耦开关时刻定位与数值阻尼 | 具体量化结果（虚假损耗降低幅度、chatter抑制效果）需回查原文；验证限于简单IGBT/二极管电路、单相两电平逆变器和DAB，固定步长离线EMT |
| [[benchmark-high-fidelity-emt-models-for-power]]（Marthi et al. 2024）| 高保真PV电站-电网基准模型可用于多PV电站在故障和弱电网条件下的动态行为验证；PSCAD和PSCAD-Fortran双实现 | 原文未给出逐点波形误差数值；验证限于IEEE-39节点、所构建PV电站配置、PSCAD实现和所选故障/SCR场景 |
| [[inverter-based-resources-model-verification-using-electromagnetic-transient-play]]（Sun et al. 2024）| IBR模型验证可将POI瞬时电压录波作为端口边界驱动，无需重建完整外部电网；包含ramp-up初始化和端子母线初始化技术 | 原文未报告可核验的统一误差百分比；验证结论限于可用POI录波、局部网络参数已知的场景 |
| [[accuracy-evaluation-of-electromagnetic-transients-simulation-algorithms]]（Zhao et al. 2022）| 仿真精度频谱方法可从端口等效导纳角度评估线性网络在梯形积分下的全局频域精度；揭示低频段误差不一定低于高频段 | 原文未给出具体误差曲线数值；方法扩展至频率相关线路的细节需回原文核验 |
| [[electromagnetic-transient-emt-simulation-algorithms-for-evaluation-of-large-scal]]（Debnath & Choi 2023）| XFC输配电EMT中按刚性与非刚性动态分类离散化+站内DAE聚合，最高可在300个XFC场景中实现271×加速且关键变量误差$<5\%$ | 该加速比数据来自PSCAD/EMTDC平台和$1\,\mu\text{s}$步长；验证限于XFC拓扑和所配置的LCL滤波器参数 |
| [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-]]（Zhou et al. 2021）| 大规模交直流混合实时仿真平台可通过离线EMTP-RV和HIL测试共同验证工程故障场景；UHVDC工程算例 | 验证结论限于所测试UHVDC工程拓扑和所列故障工况；不宜外推至其他主回路拓扑 |

## 与相关页面的关系

- [[model-verification-benchmark]] 讨论基准测试主题；本页强调验证方法流程和证据边界
- [[numerical-stability]] 和 [[numerical-integration-error]] 解释数值误差来源，为验证提供误差分析基础
- [[steady-state-initialization]] 是验证前的初值一致性步骤，初值对齐是跨工具验证的常见误差来源
- [[offline-to-realtime-porting]] 需要将离线基线、实时运行和接口时序一起验证
- [[voltage-interpolation]] 是开关事件验证中的典型局部方法，其半步后向欧拉机制可作为本页六步流程中"数值阻尼"分析的参考
- [[interface-technique]] 和 [[multirate-method]] 涉及多速率或协同仿真接口误差，是网络级验证的特有挑战

## 开放问题

EMT 验证的难点通常不是缺少误差公式，而是**缺少可复现的参考条件**。具体挑战包括：

1. **IBR 实测录波的边界完整性**：POI电压录波能否代表IBR实际面临的扰动边界，取决于录波时刻外部电网拓扑是否已知、故障阻抗是否准确、控制器状态是否记录完整
2. **大规模系统的参考基线构建**：当系统规模超过几千节点时，小步长基线本身的计算代价可能导致验证不可行；如何用代理指标（端口频域响应、能量平衡误差）代替逐点波形对比是开放问题
3. **误差来源的可分离性**：模型误差、参数误差和数值误差经常耦合；在什么条件下可以分离、在什么条件下必须联合分析，目前缺乏系统方法论
4. **跨平台验证的统一误差语言**：不同 EMT 平台的开关模型细节、状态初始化顺序和输出采样方式不同，使得跨平台波形对成本身就需要额外的标准化步骤

后续扩展本页时，应优先补充经过人工核查的基准算例（含参数、拓扑、工况和预期输出）、字段完整的现场录波证据（附测量链标定信息）、以及不同模型层级之间可追踪的参数转换记录。

## 来源论文

- Na, Kim, Zhao, Gole & Hur (2023). An improved high-accuracy interpolation method for switching devices in EMT simulation programs. *IEEE Transactions on Power Systems*.
- Marthi, Choi & Debnath (2024). Benchmark High-Fidelity EMT Models for Power Grid with PV Plants. *IEEE Transactions on Power Systems*.
- Sun, Zhang, Luo, Serritella, Hussey & Marszalkowski (2024). Inverter-Based Resources Model Verification Using Electromagnetic Transient Playback Simulation. *IEEE PES General Meeting*.
- Zhao, Zhang & Gole (2022). Accuracy Evaluation of Electromagnetic Transients Simulation Algorithms. *IEEE Transactions on Power Delivery*.
- Debnath & Choi (2023). Electromagnetic Transient (EMT) Simulation Algorithms for Evaluation of Large-Scale Extreme Fast Charging Stations. *IEEE Transactions on Transportation Electrification*.
- Zhou, Fang, Kandic, Wang, Kent & Menzies (2021). Large-scale Hybrid Real Time Simulation Modeling and Benchmark for Nelson River Multi-infeed HVDC System. *IEEE Transactions on Power Systems*.