---
title: "Haileselassie 2012 MTDC 控制策略"
type: method
tags: [haileselassie-2012-mtdc-control, mtdc-control, vsc-hvdc, droop-control, offshore-wind, north-sea]
created: "2026-05-04"
updated: "2026-05-14"
---
# Haileselassie 2012 MTDC 控制策略

## 定义

Haileselassie 2012 提出的 MTDC 控制策略面向多端 VSC-HVDC 系统，核心目标是实现**海上风电场与海上平台绿色电气化的直流汇集与功率分配**。该论文发表于 IEEE，题为 *"Multi-terminal VSC-HVDC system for integration of offshore wind farms and green electrification of platforms in the North Sea"*。

在 EMT 仿真语境中，该控制策略定义了 MTDC 系统中多个 VSC 换流站之间的**直流电压协调**与**功率-电压下垂控制**关系，是后续 MTDC 控制研究（如 Beerten 2012 广义稳态模型、Liu 2014 机电暂态模型、Allabadi 2024 EMT 初始化方法）的重要基础参考。

> **注意**：本文对应的原始 PDF 未收录于 EMT_Doc 仓库。以下内容综合了 EMT_Doc 中直接相关的 MTDC 控制文献（Liu 2014、Allabadi 2024、Xu 2016、Xiao 2019、Shu 2018），这些文献在控制机制上继承并扩展了 Haileselassie 2012 的核心思想。

## EMT 中的角色

MTDC 系统的控制是 EMT 仿真中最复杂的环节之一，原因包括：

1. **多站耦合**：$n$ 个换流站通过直流网络互联，每个站的功率输出直接影响全网直流电压
2. **控制模式切换**：正常运行（定功率/定电压）、故障闭锁、重启恢复等工况下控制模式不同
3. **时间尺度跨度大**：从微秒级开关动态到秒级功率平衡，EMT 仿真需同时捕捉
4. **初始化难题**：构网型 VSC 的控制器初值必须与潮流解一致，否则仿真启动后出现长时间振荡

Haileselassie 2012 提出的下垂控制框架为这些问题提供了基础解决方案，其核心思想是**用直流电压偏差作为功率分配信号**，使各站无需站间通信即可实现自治功率分配。

<div style="text-align:center;margin:16px 0;">
<div style="text-align:center;margin:16px 0;">
<table border="1" cellpadding="8" cellspacing="0" style="border-collapse:collapse;margin:auto;font-size:13px;">
<tr style="background:#dbeafe;">
  <td colspan="4"><b>输入层：交流系统</b></td>
</tr>
<tr style="background:#dbeafe;">
  <td>交流系统A<br/><span style="font-size:11px;color:#555;">Thevenin等效</span></td>
  <td>海上风电场<br/><span style="font-size:11px;color:#555;">DFIG/全变流</span></td>
  <td>交流系统B<br/><span style="font-size:11px;color:#555;">孤岛/无源负荷</span></td>
  <td>海上平台<br/><span style="font-size:11px;color:#555;">绿色电气化</span></td>
</tr>
<tr style="background:#dcfce7;">
  <td>VSC换流站1<br/><span style="font-size:11px;color:#555;">定电压控制</span></td>
  <td>VSC换流站2<br/><span style="font-size:11px;color:#555;">V/f构网+下垂</span></td>
  <td>VSC换流站3<br/><span style="font-size:11px;color:#555;">定功率控制</span></td>
  <td>VSC换流站4<br/><span style="font-size:11px;color:#555;">V/f构网+下垂</span></td>
</tr>
<tr style="background:#fef3c7;">
  <td colspan="4"><b>直流互联网络（DC Grid）</b><br/>
    $P_i^* = P_{i0} + k_{di}(V_{dc,0} - V_{dc,i})$ · 下垂控制功率分配</td>
</tr>
<tr style="background:#ede9fe;">
  <td>直流电压下垂控制<br/><span style="font-size:11px;">$P_i^*=P_{i0}+k_{di}(V_{dc,0}-V_{dc,i})$</span></td>
  <td>V/f构网型控制<br/><span style="font-size:11px;">$E_d^{ref}=K_{pv}\Delta V_{ac}+K_{iv}\int\Delta V_{ac}dt$</span></td>
  <td>定电压/定功率控制<br/><span style="font-size:11px;">PI外环+d/q内环解耦</span></td>
  <td>运行模式切换<br/><span style="font-size:11px;">定功率→下垂（电压越限）</span></td>
</tr>
<tr style="background:#fee2e2;">
  <td colspan="4"><b>直流故障 → DCCB动作</b> · 换流站闭锁/模式切换</td>
</tr>
</table>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · MTDC系统控制架构：交流输入→VSC换流站→直流网络→控制策略分层</p>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · MTDC 系统控制架构：交流输入 → VSC 换流站 → 直流网络 → 控制策略分层</p>

## EMT 控制架构

### 1. 直流电压下垂控制（Droop Control）

MTDC 中最核心的站间协调机制是直流电压下垂控制 [Liu 2014, Haileselassie 2012]。每个换流站 $i$ 的功率参考值与直流电压偏差成线性关系：

$$P_i^* = P_{i0} + k_{di}(V_{dc,0} - V_{dc,i})$$

其中：
- $P_i^*$ 为换流站 $i$ 的功率参考值
- $P_{i0}$ 为额定运行功率（下垂特性曲线与额定功率线的交点）
- $V_{dc,0}$ 为额定直流电压（下垂曲线零点）
- $V_{dc,i}$ 为实测直流电压
- $k_{di}$ 为下垂系数（单位：pu/MV 或 pu/kV）

**物理含义**：当直流电压因功率不平衡而下降时（$V_{dc,i} < V_{dc,0}$），所有采用下垂控制的换流站会自动增加功率注入以支撑电压。下垂系数 $k_{di}$ 决定了该站在电压恢复中的贡献权重。

**下垂系数的整定原则**：
- 定电压站（Voltage Droop Control）：$k_{d} \approx 0$（接近水平线），负责维持直流电压基准
- 定功率站（Power Droop Control）：$k_{d} \gg 0$（较大斜率），在电压偏差超过一定范围后切换为定功率模式
- 各站 $k_{di}$ 之和需满足功率平衡约束：$\sum k_{di}^{-1} \cdot \Delta P_{total} = \Delta V_{dc}$

### 2. V/f 构网型控制（Grid-Forming V/f Control）

对于连接海上风电场或无源负荷的 GVSC，采用 V/f 控制模式 [Allabadi 2024]。该模式下换流器模拟同步发电机的外特性：

**电压外环**：
$$E_d^{ref} = K_{pv}(V_{ac}^{ref} - V_{ac}) + K_{iv} \int (V_{ac}^{ref} - V_{ac}) dt$$

其中 $K_{pv}$、$K_{iv}$ 分别为电压环比例和积分增益，$E_d^{ref}$ 为 d 轴内环参考电压。

**频率外环**：
$$\omega^{ref} = \omega_0 - m_f(P - P_{ref}) + m_q(Q - Q_{ref})$$

其中 $m_f$、$m_q$ 分别为有功-频率和无功-电压下垂系数。

V/f 控制可与直流电压下垂结合使用 [Allabadi 2024]：当多个 GVSC 在同一交流孤岛中运行时，V/f 控制配合电压下垂实现功率分担和电压支撑。

### 3. 定直流电压控制（Constant DC Voltage Control）

MTDC 中通常指定 1-2 个换流站作为"定电压站"，负责维持直流电压在额定值附近 [Xiao 2019]。该站的控制框图包含：

- 直流电压外环：测量 $V_{dc,i}$ 与 $V_{dc,ref}$ 的偏差，通过 PI 控制器输出有功功率参考值
- 无功外环：通常设定 $Q_{ref} = 0$，通过 PI 控制器输出无功功率参考值
- 内环电流控制：d/q 轴电流 PI 控制，实现有功/无功的快速解耦调节
- 锁相环（PLL）：同步参考框架

定电压站的 PI 参数典型值 [Xiao 2019]：

| 控制器 | 比例增益 | 积分增益 |
|--------|---------|---------|
| 直流电压控制器 | 10.0 | 125.0 |
| 有功功率控制器 | 0.6 | 60.5 |
| 无功功率控制器 | 0.4 | 34.5 |
| PLL 控制器 | 100.0 | 200.0 |

### 4. 定功率控制（Constant Power Control）

其余换流站通常采用定功率控制模式 [Xiao 2019]，接收来自上层调度系统的功率指令：

$$P_i^* = P_{ref,i}, \quad Q_i^* = Q_{ref,i}$$

当直流电压超出安全范围时，定功率站需切换到电压下垂模式以参与电压支撑，这种**运行模式切换**是 MTDC 控制的关键特性。

## 形式化表达

### 直流网络功率平衡方程

对于 $n$ 端 MTDC 系统，节点 $i$ 的直流功率平衡为 [Liu 2014]：

$$P_{dc,i} = V_{dc,i} \sum_{j=1, j \neq i}^{n} Y_{ij}(V_{dc,i} - V_{dc,j})$$

其中 $Y_{ij} = 1/R_{ij}$ 为直流线路 $i$-$j$ 的导纳。

### MMC 等效直流侧动态

MMC 换流站的桥臂子模块电容可等效为直流侧集中电容 [Liu 2014]：

$$C_{eq} = \frac{6 C_{SM}}{N}$$

直流电压动态方程：

$$\frac{dV_{dc,i}}{dt} = \frac{1}{C_{eq,i}}(I_{conv,i} - I_{line,i})$$

### 多时间尺度分层

MTDC 控制涉及多时间尺度动态 [Liu 2014]：

| 动态环节 | 时间常数 | EMT 处理方式 |
|---------|---------|------------|
| 内环电流控制 | < 1 ms | 保留为微分方程 |
| 调制环节 | < 0.5 ms | 简化为瞬时代数环节 |
| 直流线路电感 | 1-5 ms | EMT 中保留，机电暂态中简化 |
| 外环功率/电压控制 | 10-100 ms | 保留为微分方程 |
| 直流电容动态 | 10-100 ms | 保留为微分方程 |
| 站间通信延迟 | 10-100 ms | 通常忽略（假设理想通信） |

### EMT 初始化约束

对于 V/f 控制的构网型 VSC，外环 PI 积分器的初值需从潮流解反推 [Allabadi 2024]：

$$h_0 = \frac{1}{K_{iv}}\left[\frac{2}{V_{dc}}\left(\vec{V}_{PCC}^{LF} - \vec{I}_{ac}(Z_{tr} + j\frac{X_{Larm}}{2})\right) - |V_{ac}^{set}|\right]$$

其中 $h_0$ 为 PI 积分状态初值，$Z_{tr}$ 为变压器阻抗，$X_{Larm}$ 为桥臂电抗。

## 关键技术挑战

### 1. 下垂系数的优化整定

下垂系数 $k_{di}$ 的选取需要在**功率分配精度**与**直流电压偏差容限**之间权衡。较大的 $k_{di}$ 使功率分配更精确，但会导致更大的稳态电压偏差。目前缺乏统一的数学框架用于最优下垂系数整定 [multi-terminal-dc]。

### 2. 运行模式切换的平滑性

当直流电压超出安全范围时，定功率站需切换到电压下垂模式。切换过程中的**控制信号跳变**可能引发 EMT 尺度的暂态振荡。Xiao 2019 指出，需在切换点处对控制参考值进行平滑过渡处理。

### 3. EMT 仿真初始化

传统潮流初始化方法在端口放置辅助电压源，导致 GVSC 控制误差信号强制归零，PI 积分器初值错误 [Allabadi 2024]。CISS 方法通过解析计算消除这一冲突，DI 方法通过接口辅助源解耦再重连。两种方法均使初始化时间缩短至原来的 1/6.9。

### 4. 通信延迟与分布式控制

下垂控制假设站间通信延迟可忽略。实际 MTDC 系统中，通信延迟（通常 10-100 ms）会影响下垂控制的动态响应。Shu 2018 指出，多速率协同仿真中需考虑通信延迟对接口协调的影响。

## 量化性能边界

| 指标 | 数值 | 来源 |
|------|------|------|
| 下垂控制稳态电压偏差 | $\pm 3\%$（典型运行范围） | Liu 2014 |
| EMT 初始化加速比 | 6.9$\times$（相对传统 LFSI） | Allabadi 2024 |
| CISS 初始化收敛时间 | 0.15 s | Allabadi 2024 |
| DI 初始化收敛时间 | 0.3 s | Allabadi 2024 |
| 直流电压波动容限 | $\pm 3\%$（故障清除后） | Liu 2014 |
| 简化模型相对误差 | $< 1\%$（机电暂态 vs EMT） | Liu 2014 |
| 仿真步长（EMT） | 10-50 $\mu$s | Allabadi 2024 |
| 仿真步长（机电暂态） | 1-10 ms | Liu 2014 |

## 适用边界与选择指南

### 适用场景

| 应用场景 | 推荐控制策略 | 说明 |
|---------|------------|------|
| 海上风电场 MTDC 汇集 | 下垂控制 + V/f 构网 | Haileselassie 2012 原始场景，多 GVSC 并联运行 |
| 多端直流功率分配 | 直流电压下垂 | 无需通信，各站自治功率分担 |
| 交流孤岛供电 | V/f 控制 | GVSC 维持交流电压和频率 |
| 异步电网直流互联 | 定电压 + 定功率 | 1 站定电压，其余定功率 |
| EMT 仿真初始化 | CISS / DI | Allabadi 2024，避免控制冲突 |

### 失效边界

| 条件 | 失效原因 |
|------|---------|
| LCC 主导的多端系统 | 换相失败风险，下垂控制不适用 |
| 弱交流系统下 VSC 注入功率受限 | 下垂特性可能无法保持 |
| 站间通信完全中断 | 下垂控制可暂维持但无最优功率分配 |
| 大扰动下换相失败或闭锁 | 需 EMT 时域校核，阻抗法不覆盖 |
| 不含明确保护和 DCCB 的 MTDC | 故障分析不完整 |

### 关键假设

- 直流网络假设为刚性 $\pi$ 型等效，忽略分布参数行波 [Liu 2014]
- 站间通信延迟可忽略（理想通信假设）
- MMC 桥臂子模块电压均衡 [Liu 2014]
- 运行点附近线性化在小信号分析中有效 [Xu 2025]

## 相关方法

- [[multi-terminal-dc]]：多端直流系统的网络、控制和保护边界
- [[hvdc-control]]：HVDC 控制方法的通用入口
- [[vsc-control]]：电压源换流器控制结构入口
- [[mtdc-model]]：多端直流系统建模入口
- [[emt-simulation]]：用于确认时域 EMT 语境
- [[power-flow-calculation]]：用于区分运行点求解和控制动态验证
- [[grid-forming-control]]：构网型控制在 MTDC 中的应用
- [[beerten-2012-mtdc-powerflow]]：MTDC 潮流计算专用方法
- [[dc-protection]]：直流故障检测与保护配合
- [[dccb]]：直流断路器动作特性

## 来源论文

- **Haileselassie, T.M., et al.** "Multi-terminal VSC-HVDC system for integration of offshore wind farms and green electrification of platforms in the North Sea." IEEE, 2012. — 原始 MTDC 下垂控制框架，面向北海海上风电集成场景。**（原始 PDF 未收录于 EMT_Doc，以下内容基于相关文献综合）**
- **Liu 等, 2014** "Electromechanical transient modeling of modular multilevel converter based multi-terminal hvdc system" — MMC-MTDC 机电暂态建模，下垂控制数学推导，四端系统验证，简化模型误差 < 1%
- **Allabadi 等, 2024** "Initializing EMT models of grid forming VSCs in MTDC systems" — GVSC V/f 控制与下垂控制的结合，CISS/DI 初始化方法，CIGRE BM4 基准验证，加速比 6.9$\times$
- **Xu 等, 2016** "Enhanced high-speed electromagnetic transient simulation of MMC-MTdc grid" — MMC-MTDC 快速 EMT 仿真，理想开关电阻建模，内置排序算法
- **Xiao 等, 2019** "Electro-mechanical transient modeling of MMC based multi-terminal HVDC system with DC faults considered" — MMC-MTDC 直流故障建模，定电压/定功率控制切换，PI 参数整定表
- **Shu 等, 2018** "A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC Systems" — 多速率协同仿真，AC/MTDC 分区控制协调，接口预测与校正
