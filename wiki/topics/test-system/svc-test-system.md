---
title: "Svc Test System"
type: topic
tags: [svc, test-system, facts, reactive-power-compensation]
created: "2026-05-04"
updated: "2026-05-19"
---

# Svc Test System

## 定义

静止无功补偿器（Static Var Compensator, SVC）是电力系统中用于电压调节和动态无功补偿的FACTS装置。SVC测试系统是用于验证SVC装置在电力系统中动态行为的EMT仿真测试平台，涵盖TCR（晶闸管控制电抗器）、TSC（晶闸管投切电容器）等典型拓扑的电磁暂态建模与仿真验证。

## EMT中的角色

SVC在电力系统EMT仿真中具有以下核心作用：

1. **精确动态行为刻画**：准确描述SVC装置的电压/电流波形响应，特别是在晶闸管触发、导通角变化等强非线性工况下
2. **控制策略验证**：在详细仿真模型中验证SVC控制系统（电压调节、电流限幅、分组投切）的有效性和鲁棒性
3. **故障与保护分析**：模拟SVC在系统中各类故障场景下的响应，评估保护装置的动作特性
4. **多场景适应性**：支持不同运行工况（滞后/超前无功范围）、参数变化和拓扑结构的仿真研究

SVC的核心挑战在于其**强非线性特性**（晶闸管开关）和**多时间尺度耦合**（基波动态与谐波动态并存），全EMTP因微小步长不适合大系统长时段动态分析，而TSP虽可用大步长但无法给出开关波形。

## SVC拓扑结构

### 基本SVC结构

典型SVC由三部分组成：

- **TCR（晶闸管控制电抗器）**：通过控制触发角α连续调节从系统吸收的无功功率，实现快速动态电压支撑
- **TSC（晶闸管投切电容器）**：分组投切，提供阶梯式电容无功输出
- **滤波器/固定电容**：滤除TCR产生的特征谐波（五次、七次等）

$$V_{d0} = \frac{3\sqrt{2}}{\pi}V_{LL}$$

$$V_d = V_{d0}\cos\alpha - \frac{3\omega L_c}{\pi}I_d$$

其中$\alpha$为TCR触发角，$V_{LL}$为线电压，$L_c$为耦合电抗。

### 混合SVC-VSC结构（Le-Huy 2023）

Hydro-Québec La Vérendrye 735 kV变电站的混合SVC采用全桥MMC（模块化多电平变换器）替代传统TCR，同时保留传统TSC：

- 每套容量：+330/-110 Mvar
- 每相VSC分支：22个子模块（FB-MM），delta连接
- 每相TSC分支：95 Mvar × 2
- 最大支路电流：1.45 kA
- VSC耦合变压器二次侧电压：16 kV

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 700 420" xmlns="http://www.w3.org/2000/svg">
  <!-- SVC Topology Structure -->
  <!-- Background -->
  <rect width="700" height="420" fill="#fafafa"/>
  
  <!-- Title -->
  <text x="350" y="25" text-anchor="middle" font-size="14" font-weight="bold" fill="#333">图1 · SVC测试系统拓扑结构</text>
  
  <!-- AC System (left) -->
  <rect x="20" y="60" width="90" height="60" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="65" y="85" text-anchor="middle" font-size="11" fill="#1e40af">交流系统</text>
  <text x="65" y="102" text-anchor="middle" font-size="10" fill="#3b82f6">735kV/16kV</text>
  
  <!-- Coupling Transformer -->
  <rect x="130" y="75" width="70" height="30" rx="3" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="165" y="94" text-anchor="middle" font-size="10" fill="#92400e">耦合变压器</text>
  <text x="165" y="108" text-anchor="middle" font-size="9" fill="#b45309">16kV</text>
  
  <!-- Arrow to SVC -->
  <line x1="110" y1="90" x2="130" y2="90" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- SVC main box -->
  <rect x="210" y="50" width="280" height="180" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
  <text x="350" y="72" text-anchor="middle" font-size="12" font-weight="bold" fill="#166534">SVC本体</text>
  
  <!-- TSC branches -->
  <rect x="225" y="85" width="70" height="55" rx="3" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="260" y="105" text-anchor="middle" font-size="10" fill="#166534">TSC支路×2</text>
  <text x="260" y="120" text-anchor="middle" font-size="9" fill="#15803d">95Mvar/支</text>
  
  <!-- VSC branches (MMC) -->
  <rect x="310" y="85" width="80" height="55" rx="3" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="350" y="105" text-anchor="middle" font-size="10" fill="#166534">VSC (MMC)</text>
  <text x="350" y="120" text-anchor="middle" font-size="9" fill="#15803d">22SM/相</text>
  <text x="350" y="133" text-anchor="middle" font-size="8" fill="#166534">Δ连接</text>
  
  <!-- Filter -->
  <rect x="405" y="85" width="70" height="55" rx="3" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="440" y="105" text-anchor="middle" font-size="10" fill="#166534">滤波器</text>
  <text x="440" y="120" text-anchor="middle" font-size="9" fill="#15803d">RLC滤波</text>
  
  <!-- TCR label -->
  <text x="260" y="155" text-anchor="middle" font-size="9" fill="#4b5563">TCR</text>
  
  <!-- Control system -->
  <rect x="225" y="155" width="250" height="60" rx="4" fill="#fef9c3" stroke="#ca8a04" stroke-width="1.5" stroke-dasharray="4,2"/>
  <text x="350" y="175" text-anchor="middle" font-size="11" fill="#854d0e">控制系统</text>
  <text x="260" y="192" text-anchor="middle" font-size="9" fill="#a16207">电压调节</text>
  <text x="350" y="192" text-anchor="middle" font-size="9" fill="#a16207">电流限幅</text>
  <text x="440" y="192" text-anchor="middle" font-size="9" fill="#a16207">分配单元</text>
  
  <!-- Output arrows -->
  <line x1="490" y1="90" x2="520" y2="90" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="505" y="83" text-anchor="middle" font-size="9" fill="#666">Vconv</text>
  
  <line x1="490" y1="195" y2="520" y2="195" stroke="#333" stroke-width="1.5"/>
  <line x1="520" y1="195" x2="520" y2="90" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="505" y="205" text-anchor="middle" font-size="9" fill="#666">Iarm</text>
  
  <!-- RTS -->
  <rect x="530" y="60" width="100" height="90" rx="5" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="580" y="82" text-anchor="middle" font-size="11" fill="#5b21b6">实时仿真器</text>
  <text x="580" y="100" text-anchor="middle" font-size="9" fill="#7c3aed">RTS</text>
  <text x="580" y="115" text-anchor="middle" font-size="9" fill="#6d28d9">ΔT=3μs/32.6μs</text>
  <text x="580" y="130" text-anchor="middle" font-size="9" fill="#6d28d9">小步长/标准</text>
  
  <!-- Arrow to load -->
  <line x1="630" y1="90" x2="650" y2="90" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="640" y="83" text-anchor="middle" font-size="8" fill="#666">等效电压</text>
  
  <!-- MMCsim box -->
  <rect x="530" y="160" width="100" height="55" rx="4" fill="#fce7f3" stroke="#be185d" stroke-width="1.5"/>
  <text x="580" y="180" text-anchor="middle" font-size="10" fill="#9d174d">MMCsim</text>
  <text x="580" y="196" text-anchor="middle" font-size="9" fill="#be185d">FO接口</text>
  <text x="580" y="210" text-anchor="middle" font-size="9" fill="#be185d">512点/周期</text>
  
  <!-- Legend -->
  <rect x="20" y="260" width="640" height="140" rx="5" fill="#f9fafb" stroke="#e5e7eb" stroke-width="1"/>
  <text x="340" y="283" text-anchor="middle" font-size="11" font-weight="bold" fill="#374151">图例</text>
  
  <!-- Legend items - row 1 -->
  <rect x="35" y="295" width="25" height="15" rx="2" fill="#dbeafe" stroke="#2563eb"/>
  <text x="68" y="306" font-size="10" fill="#374151">交流系统</text>
  
  <rect x="140" y="295" width="25" height="15" rx="2" fill="#fef3c7" stroke="#d97706"/>
  <text x="173" y="306" font-size="10" fill="#374151">耦合变压器</text>
  
  <rect x="270" y="295" width="25" height="15" rx="2" fill="#f0fdf4" stroke="#16a34a"/>
  <text x="303" y="306" font-size="10" fill="#374151">SVC本体</text>
  
  <!-- Legend items - row 2 -->
  <rect x="35" y="325" width="25" height="15" rx="2" fill="#dcfce7" stroke="#16a34a"/>
  <text x="68" y="336" font-size="10" fill="#374151">电力电子支路</text>
  
  <rect x="170" y="325" width="25" height="15" rx="2" fill="#fef9c3" stroke="#ca8a04"/>
  <text x="203" y="336" font-size="10" fill="#374151">控制系统</text>
  
  <rect x="280" y="325" width="25" height="15" rx="2" fill="#ede9fe" stroke="#7c3aed"/>
  <text x="313" y="336" font-size="10" fill="#374151">实时仿真器</text>
  
  <!-- Legend items - row 3 -->
  <rect x="35" y="355" width="25" height="15" rx="2" fill="#fce7f3" stroke="#be185d"/>
  <text x="68" y="366" font-size="10" fill="#374151">MMCsim</text>
  
  <!-- Arrow definition -->
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#333"/>
    </marker>
  </defs>
  
  <!-- Specs table -->
  <text x="35" y="385" font-size="10" font-weight="bold" fill="#374151">参数规格（Le-Huy 2023）：</text>
  <text x="35" y="402" font-size="9" fill="#6b7280">容量：+330/-110 Mvar · VSC：22SM/相 delta · TSC：95Mvar×2 · I_max=1.45kA · V_sec=16kV</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · SVC测试系统拓扑结构（混合SVC-VSC架构）</p>

## SVC的EMT建模方法

### 方法一：动态相量（DP）模型（Zhijun 2009）

**核心思想**：将SVC划分为机电暂态（TSP）交流子系统和SVC动态相量子系统，在接口母线处进行相量与时域量的双向数据交互。

**动态相量定义**：k阶动态相量定义为滑动窗口内的傅里叶系数：

$$X_k(t) = \frac{c}{T}\int_{t-T}^{t}x(\tau)e^{-jk\omega_0\tau}d\tau$$

其中$c=1$（$k=0$）或$c=2$（$k\neq0$），$\omega_0=2\pi/T$。

**微分性质**：

$$\left[\frac{dx}{dt}\right]_k(t) = \frac{dX_k}{dt}(t) + jk\omega_0 X_k(t)$$

**TCR动态相量模型**（基波与五次谐波）：

$$C\frac{dV_k}{dt} = -jk\omega_0 CV_k + I_{lk} - I_k, \quad k=1,5$$

$$L\frac{dI_k}{dt} = -jk\omega_0 LI_k + \sum_{l\in\{-5,-1,1,5\}}S_{k-l}V_l, \quad k=1,5$$

**接口算法**：TSP侧在每个大步长（0.01~0.02s）提供接口母线基波相量电压，SVC侧按DP方程推进后重构等效电流/功率注入TSP网络。

### 方法二：传统EMT详细模型（Le-Huy 2023）

**小步长方法**（DPS/FAT阶段）：$\Delta t = 3\mu s$，使用RTS实时仿真器的small time-step优化超级模型。

**标准步长方法**（预调试阶段）：$\Delta t = 32.5521\mu s$（512点/周期），使用HP Z8 gen 4工作站（双Intel Xeon Gold 6244）。

**Pejovic开关模型**：将导通开关等效为小电感$L$，断开开关等效为串联RC支路：

$$R_{eq} = \frac{2L}{\Delta T} + R + \frac{\Delta T}{2C}$$

### 方法三：混合SVC-VSC等效建模（Le-Huy 2023）

**MMC臂等效电路**：FB-MMC delta分支用戴维南等效表示，6个臂电流通过光纤接口回传至MMCsim rack计算子模块电容电压。

**MMCsim接口刷新率**：512点/周期（$32.5521\mu s$），通过光纤与控制系统的MMS通信。

## 关键技术挑战

### 挑战一：相位不连续与直流偏移
TSP等值与EMTP等值之间可能出现相位不连续、直流偏移，影响混合仿真精度。DP方法通过在慢变系数域描述非正弦波形，理论上可减轻此问题。

### 挑战二：谐波动态保留
TCR开关导致非正弦波形，需要保留基波和五次谐波动态才能准确描述电压/电流响应。动态相量方法在保留特征谐波的同时用较大步长求解。

### 挑战三：实时HIL仿真的时间步长约束
RTS小步长模式约束：每个任务最多30个单相节点，最多6个标准Ron/Roff开关，其余需用Pejovic模型。

### 挑战四：控制系统的黑箱接口
SVC控制系统的精确架构和实现细节通常不公开（商业保护），HIL测试中控制系统被当作"物理黑箱"，只能通过输入/输出接口进行验证。

## 量化性能边界

### Zhijun 2009 量化数据

| 指标 | 数值 |
|------|------|
| TSP步长 | 0.01~0.02 s |
| EMTP典型步长 | 50 μs |
| 验证系统 | IEEE 3机9节点、New England 10机39节点 |
| DP谐波阶数 | 基波 + 五次谐波 |
| TCR/RL/电容DP方程 | 复数状态方程（实部/虚部分离） |
| 精度对比 | 与EMTP电磁暂态模型结果一致 |
| 加速比 | 原文未报告具体数值 |

### Le-Huy 2023 量化数据

| 指标 | 数值 |
|------|------|
| SVC总容量 | +330/-110 Mvar |
| VSC配置 | 22 SM/相，delta连接，FB子模块 |
| TSC配置 | 95 Mvar × 2 |
| 最大支路电流 | 1.45 kA |
| 耦合变压器二次电压 | 16 kV |
| 小步长 | 3 μs（DPS/FAT阶段） |
| 标准步长 | 32.5521 μs（预调试阶段） |
| MMCsim刷新率 | 512点/周期 |
| 节点数限制（小步长） | ≤30单相节点/任务 |
| Pejovic模型参数 | $R_{eq}=2L/\Delta T+R+\Delta T/2C$ |
| 工作站 | HP Z8 gen 4，双Intel Xeon Gold 6244 |

## 适用边界与选择指南

| 场景 | 推荐方法 | 步长 |
|------|---------|------|
| 大电网长时段动态仿真 | DP模型混合仿真 | 0.01~0.02 s |
| SVC波形精度验证 | 详细EMT模型 | 50 μs |
| 实时HIL控制测试 | 小步长EMT | 3 μs |
| 预调试离线仿真 | 标准步长EMT | 32.6 μs |
| 混合SVC-VSC换流 | MMC等效模型 | 32.6 μs |

**方法选择决策**：
- 需要大系统长时段分析+局部波形精度 → DP混合模型（Zhijun 2009）
- 需要精确换流/开关动态 → 详细EMT小步长（Le-Huy 2023）
- 需要HIL测试控制保护系统 → 标准步长+Pejovic开关模型
- 混合SVC-VSC替换传统TCR → MMC等效+光纤接口

## 相关页面

- [[emt-simulation]] - EMT仿真基础
- [[electromagnetic-transient]] - 电磁暂态分析
- [[power-system]] - 电力系统建模
- [[control-system]] - 控制系统设计
- [[real-time-simulation]] - 实时仿真技术
- [[thyristor-controlled-series-capacitor]] - TCSC建模方法（同类FACTS装置）
- [[statcom]] - STATCOM补偿装置

## 来源论文

- [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model]] - Zhijun等2009，DP混合仿真方法
- [[hybrid-svc-vsc-modeling-approaches-for-hardware-in-the-loop-simulation]] - Le-Huy和Tremblay 2023，混合SVC-VSC HIL测试