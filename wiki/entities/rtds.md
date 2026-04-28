---
title: "RTDS"
type: entity
entity_type: tool
tags: [rtds, real-time, hil, simulation-tool]
created: "2026-04-13"
---

# RTDS

## 概述

RTDS（Real-Time Digital Simulator）是广泛使用的实时数字仿真器，专门用于电力系统的硬件在环（HIL）测试。

## 特点

- 实时仿真（50-100μs步长）
- 硬件在环测试
- 保护装置验证
- 控制器接口（GTNET、GTFPGA）

## 应用场景

- 继电保护装置测试
- 换流器控制器验证
- 新能源并网测试
- 混合仿真接口

## 定义与边界

RTDS 在本 wiki 中指实时数字仿真平台及其 EMT/HIL 工作流，重点是固定步长、确定性计算和外部控制保护设备闭环。它应与 [[real-time-simulation|实时仿真]]、[[co-simulation|协同仿真]]、[[network-equivalent|网络等值]]、[[fdne-model|FDNE]]、[[vsc-model|VSC 模型]]、[[lcc-model|LCC 模型]] 和 [[pmsm-model|PMSM 模型]] 一起理解。

RTDS 的边界来自实时硬件资源、I/O 延迟、模型分区和固定步长约束。离线 EMT 模型能运行不代表可以直接实时运行；进入 RTDS 前通常需要模型降阶、接口解耦、参数重构和与离线基准或实测数据的闭环验证。

## 代表性来源与内部链接

代表性来源包括 [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-|Large-scale hybrid real-time simulation modeling and benchmark for Nelson River]]、[[real-time-digital-simulator-of-the-electromagnetic-transients-of-power-transmiss|Real-time digital simulator of electromagnetic transients of power transmission]]、[[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga--13&14|Development of phase-domain frequency-dependent transmission line model on FPGA]] 和 [[a-flux-defined-pmsm-model-based-on-fea-results-for-real-time-emt-simulation|A Flux-Defined PMSM Model Based on FEA Results for Real-Time EMT Simulation]]。相关实体包括 [[manitoba-hydro]]、[[gole]] 和 [[pscad-emtdc]]。

## 相关主题
- [[real-time-simulation]]
- [[co-simulation]]

## 深度增强内容

 基于提供的论文数据，RTDS作为**实时数字仿真平台(Real-Time Digital Simulator)**，其技术深度涵盖混合仿真接口、多速率协同、网络等值降阶及电力电子详细建模等核心领域。以下为深度增强内容：

---

## 1. 关键技术详解

### 1.1 实时仿真架构与步长约束机制

RTDS采用固定时步（Fixed Time Step）的电磁暂态（EMT）求解架构，其核心约束源于传输线模型的**最短线路长度限制**与**实时性硬约束**：

- **最短线路长度约束**：分布参数线路模型（Bergeron模型）要求线路传播时延 $\tau$ 必须大于仿真步长 $\Delta t$。由 $\tau = L/c$（$c$ 为光速，$3\times10^8$ m/s），当 $\Delta t = 50\,\mu\text{s}$ 时，可模拟的最短线路长度为：
  $$
  L_{\min} = c \cdot \Delta t = 3\times10^8 \times 50\times10^{-6} = 15\,\text{km}
  $$

- **亚微秒级仿真**：针对电力电子开关过程（如MMC子模块电容电压均衡），RTDS Novacor 2.0平台可实现 $<1.0\,\mu\text{s}$ 步长（实测1.5–2.0 $\mu\text{s}$），需采用磁链定义模型（Flux-Defined Model）避免查表反演耗时：
  $$
  \frac{d\mathbf{i}}{dt} = \mathbf{L}^{-1}(\theta, \mathbf{i}) \cdot \left( \mathbf{v} - \mathbf{e}(\theta, \mathbf{i}) - \mathbf{R}\cdot\mathbf{i} \right)
  $$
  其中 $\mathbf{L}$ 为基于FEA结果的三维查表电感矩阵，$\theta$ 为转子位置角。

### 1.2 混合仿真接口技术

#### 1.2.1 EMT-RMS多速率接口
当RTDS（EMT侧，$\Delta t_{\text{EMT}} \leq 50\,\mu\text{s}$）与机电暂态（RMS侧，$\Delta t_{\text{RMS}} \approx 10\,\text{ms}$）联合仿真时，步长比 $N = \Delta t_{\text{RMS}}/\Delta t_{\text{EMT}}$ 可达 $200:1$。关键算法包括：

- **DFT相量提取**：采样点数 $N_{\text{DFT}}$ 需严格满足基频周期对齐：
  $$
  N_{\text{DFT}} = \frac{1}{f_0 \cdot \Delta t_a}
  $$
  其中 $f_0$ 为基频，$\Delta t_a$ 为采样间隔，以避免频谱泄漏。

- **后向欧拉插值**：在RMS步长 $\Delta t_{\text{RMS}}$ 区间内线性重构EMT数据，插值公式为：
  $$
  x(t) = x_{k} + \frac{x_{k+1} - x_{k}}{\Delta t_{\text{RMS}}} \cdot (t - t_k)
  $$
  确保插值终点值严格等于RMS新步长目标值，消除数值振荡（可将过冲从12%降至1.5%）。

#### 1.2.2 频率相关网络等值（FDNE）
为提升混合仿真边界精度，FDNE采用矢量拟合（Vector Fitting）建立宽频等值模型：
$$
Y(s) = \sum_{i=1}^{n} \frac{\mathbf{r}_i}{s - p_i} + \mathbf{D} + s\mathbf{E}
$$
其中 $p_i$ 为极点，$\mathbf{r}_i$ 为留数矩阵。**无源性约束**要求所有 $p_i$ 位于左半平面且 $\mathbf{r}_i > 0$。

**计算优化**：通过奇异值分解（SVD）压缩留数矩阵秩 $r$。当 $r < (N+1)/2$（$N$ 为端口数）时，单极点计算量从 $2N^2+2N$ 降至 $4rN$，最大降幅超50%。

#### 1.2.3 交互时序与误差控制
- **串行时序**：数据交互延迟导致相位滞后约 $2\pi f \Delta t$（$f$ 为基频），在10ms步长下相位误差约18°。
- **并行时序**：通过预测-校正机制，机电侧单个交互周期内3-5次迭代可使接口功率偏差收敛至 $<0.1\%$，相位误差降至 $<2°$。

### 1.3 FPGA-RTDS多速率协同仿真

针对电力电子设备（开关频率几千至几十万赫兹），采用**RTDS（大步长）+ FPGA（小步长）**架构：

- **步长配置**：RTDS侧 $50\,\mu\text{s}$，FPGA侧 $1\,\mu\text{s}$，混合比例 $50:1$。
- **异步交互策略**：FPGA数据发送适当早于RTDS，补偿通信延时（$<2\,\mu\text{s}$，基于64个32bit数据传输）。
- **解耦方法**：基于线路惯性法（LIM）将系统分解为独立子系统，避免传统串行多速率方法的实时性瓶颈。

FPGA内部采用**相模变换（Phase-Modal Transformation）**实现分布参数线路求解，并预存储导纳矩阵与故障矩阵，实现网络拓扑变化的实时处理。

### 1.4 大规模系统分区与并行计算

针对大规模交直流电网（>6000节点），采用**连接域提取分解法（Linking-Domain Extraction, LDE）**：

将网络导纳矩阵 $\mathbf{Y}$ 分块为：
$$
\mathbf{Y} = \begin{bmatrix} \mathbf{Y}_{11} & \mathbf{Y}_{12} \\ \mathbf{Y}_{21} & \mathbf{Y}_{22} \end{bmatrix}
$$
通过Woodbury恒等式，将矩阵求逆复杂度从 $O(N^3)$ 降至 $O(N)$，实现：
- **FPGA实现**：单步仿真延迟 $<10\,\mu\text{s}$
- **GPU实现**：单步延迟 $<25\,\mu\text{s}$

当连接域规模扩大300%时，LDE方法计算时间仅增加约18%，而传统舒尔补法激增超过400%。

---

## 2. 硬件平台与仿真能力对比

| 特性 | RTDS平台 | OPAL-RT平台 | 离线仿真（PSCAD/EMTDC） |
|------|----------|-------------|------------------------|
| **典型步长** | 50–100 $\mu\text{s}$（实时）<br>可至 $<1\,\mu\text{s}$（亚微秒） | 50 $\mu\text{s}$（实时） | 10–100 $\mu\text{s}$（非实时） |
| **最大节点规模** | 单机架~100节点（纯EMT）<br>混合仿真可扩展至6000+节点 | 类似规模 | 无限制（取决于计算资源） |
| **HIL接口** | GTNET（以太网）<br>GTFPGA（光纤，微秒级延迟） | 模拟/数字IO | 不支持实时HIL |
| **多速率支持** | RTDS+FPGA联合仿真 | 支持 | 软件多速率 |
| **混合仿真** | RTDS-TSA（机电-电磁）<br>RTDS-PSS/E（UDP/FPGA接口） | RMS-EMT联合仿真 | 通过外部接口耦合 |
| **计算资源** | GPC卡（多核并行）<br>单机架最多18个FDNE子模块 | 多核CPU | 单/多核CPU |
| **成本与扩展** | 硬件成本高，线性扩展需增加Rack | 中等 | 软件许可成本 |

**关键差异**：RTDS的GTFPGA板卡提供高速数字化接口，消除传统模拟量接口的DAC/ADC转换时延（数百微秒至毫秒级），实现微秒级通信时延，较传统方式硬件资源节约67%（如Nelson River项目仅需1个Rack vs 全仿真需3个Racks）。

---

## 3. 实际应用案例汇总

| 应用场景 | 技术方案 | 关键参数与成果 | 引用论文 |
|----------|----------|----------------|----------|
| **大规模HVDC系统** | Nelson River多馈入HVDC混合HIL模型 | 承载总发电量70%，线路900km；Dorsey站14阀组/9调相机等效简化；控制模块100+自定义模块重构为标准库 | large-scale-hybrid-real-time-simulation |
| **MMC实时仿真** | 等效混合模型（主从集分组） | 2秒仿真耗时：33分钟→8分钟（4.1倍提升）；功率误差<0.07%额定；THD 4.1%；单臂400子模块@2$\mu\text{s}$步长 | equivalent-hybrid-model-for-mmc |
| **继电保护HIL测试** | RMS-EMT跨平台联合仿真（OPAL-RT+RTDS） | 零缓冲曲线拟合算法，消除FFT固有延迟（20–40ms）；支持三相耦合线路模型 | real-time-rms-emt-co-simulation |
| **直流断路器** | VARC断路器系统级模型 | 开关电阻比 $10^{11}$（$10^8\,\Omega$ / $1\,\text{m}\Omega$）；避雷器钳位电压1.5–1.6倍额定峰值；开断时间毫秒级 | modeling-varc-dc-breaker |
| **大规模电网等值** | FDNE压缩与划分 | 计算复杂度 $O=2nN^2+N^2+2nN$；Y10案例划分11子模块，实时成功率100%；单机架承载18个FDNE子模块 | compacting-partitioning-fdne |
| **变压器精细建模** | 三柱变压器零序电感闭式解 | 零序阻抗匹配误差0%；数值振荡完全消除（>10kHz→0Hz）；磁通分布误差降低85% | terminal-duality-transformers |
| **PMSM亚微秒仿真** | 磁链定义FEA模型 | 步长 $<1\,\mu\text{s}$；LUT规模7381条；外推策略处理200–250A峰值电流（超边界150A） | flux-defined-pmsm-model |
| **信息-电磁混合** | 信息-电磁-机电混合仿真展望 | 接口母线电气距离<3–5节点时需等值切换；矩阵束算法在40%谐波畸变下幅值误差<0.3% | 电力系统数字混合仿真技术综述 |

---

## 4. 研究趋势与开放问题

### 4.1 超实时仿真与数字孪生
当前RTDS已实现**硬实时**（计算时间<物理时间），未来趋势向**超实时（Super-Real-Time）**发展，支持在线模型预测控制（MPC）与数字孪生体训练。关键挑战在于保持亚微秒级精度的同时，将仿真速度提升至物理过程的10–100倍。

### 4.2 信息-电磁-机电混合仿真（Cyber-Physical）
随着电力信息物理系统（CPS）发展，需将电磁侧（RTDS）与信息系统（通信网络、保护装置逻辑）仿真平台互联：
- **接口挑战**：信息侧事件驱动与电磁侧时间驱动的同步机制
- **安全测试**：网络攻击（如虚假数据注入）对电磁暂态过程的影响评估

### 4.3 自适应变步长算法
当前RTDS采用固定步长，对于含多时间尺度（开关瞬态+机电振荡）的系统存在效率瓶颈。研究热点包括：
- **局部变步长**：仅对开关动作区域采用小步长，其余区域保持大步长
- **事件驱动插值**：精确捕捉开关时刻，避免数值振荡与伪谐波

### 4.4 AI辅助的模型降阶与参数辨识
- **数据驱动FDNE**：利用深度学习替代传统矢量拟合，实现宽频阻抗特性的快速辨识（减少10–20个频点扫描开销）
- **代理模型（Surrogate Model）**：用神经网络替代详细电力电子模型，在保证精度的同时将计算速度提升1–2个数量级，突破RTDS硬件算力限制

### 4.5 多馈入系统宽频振荡分析
针对新能源多馈入系统的次/超同步振荡（SSR/SSO），RTDS需解决：
- **宽频模型一致性**：FDNE在1–2.5kHz范围内与详细模型的阻抗匹配精度
- **多端口耦合**：单端口戴维南等值在多馈入直流系统逆变侧换相失败分析中功率误差可达8–12%，需发展自动端口选择算法以平衡计算量与精度

---

**注**：以上内容基于2021–2025年间RTDS在电磁暂态仿真、硬件在环测试及混合仿真接口领域的最新研究成果，涵盖大规模交直流电网、电力电子设备精细建模及实时仿真优化等前沿方向。
