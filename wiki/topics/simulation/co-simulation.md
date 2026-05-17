---
title: "混合仿真"
type: topic
tags: [co-simulation, hybrid-simulation, interface-technique, multirate, dynamic-phasor]
created: "2026-04-13"
updated: "2026-05-18"
---

# 混合仿真

## 定义

混合仿真（Co-Simulation）是将两种或以上不同暂态表示、求解器或时间步长的仿真工具在同一研究问题中耦合执行的仿真范式。其核心目标是在保留局部波形细节的同时大幅降低全系统电磁暂态（EMT）仿真的计算成本。

在 EMT 语境下，"混合仿真"特指 **EMT 与其他仿真域的协同**，包括：
- **EMT-机电暂态（TS）混合**：详细设备模型（1-50 μs步长）与大规模相量域网络（1-10 ms步长）的边界接口
- **EMT-动态相量（DP）混合**：时域波形采样与基频相量/谐波相量的跨域映射
- **EMT-移频相量（SFA/SFP）混合**：频域等效与时域EMT的并行追踪
- **多速率EMT-EMT混合**：快变电力电子子系统（μs级）与慢变网络（ms级）的差异化步长协同
- **硬件在环（HIL）混合**：RTDS/FPGA实时仿真器与离线EMT/TS求解器的物理接口

## 在 EMT 中的角色

EMT 仿真是电力系统精细化分析的核心工具，但其步长受限于电力电子开关动作（通常 1-50 μs），无法高效处理大系统全时长仿真。混合仿真是解决这一瓶颈的关键技术：

| 系统部分 | 仿真工具 | 步长 | 典型应用 |
|---------|---------|------|---------|
| 换流器/MMC/DCDC | EMT | 1-50 μs | 详细开关波形、谐波、故障穿越 |
| 大规模交流网络 | TS/PM | 1-10 ms | 机电振荡、低频动态 |
| 直流电网 | SFA/SFP/DP | 50-500 μs | 直流故障、多端协调控制 |
| 控制器硬件 | HIL | 实时 | 保护逻辑验证、保护控制器测试 |

**核心挑战**在于接口精度、接口延迟、模型无源性和数值稳定性。

## 分类与机制

### 按接口变量形式分类

| 接口类型 | 核心等效 | 适用场景 | 代表方法 |
|---------|---------|---------|---------|
| **Thevenin/Norton等值** | 电压源+阻抗 / 电流源+导纳 | 边界母线为相对平衡点 | [[fdne-model]]、双端口等效 |
| **动态相量接口** | 基频相量/谐波相量映射 | 含直流偏置、谐波的接口 | DPIM、MATE |
| **移频相量接口** | 频域复数信号转换 | 宽频带交互分析 | HMD-TLM、SFA-EMT |
| **松弛迭代接口** | 边界变量预测+迭代修正 | 接口电气距离近、交互强 | 边界预测加速、双向阻抗更新 |
| **接口位移/映射等效** | 物理位置迁移+松耦合 | 大规模交直流混联系统 | ID-Mapping |

### 按协同架构分类

| 架构类型 | 核心机制 | 代表论文 |
|---------|---------|---------|
| **集中式混合仿真** | 单一仿真器管理EMT和TS，两侧通过接口变量交换 | InterPSS+PSCAD/EMTDC (Huang & Vittal 2016) |
| **分布式混合仿真** | 多EMT子系统和TS子系统独立求解，通过MATE协议同步 | Shu 2017、分布式MATE (Tarazona 2026) |
| **多速率EMT协同** | 快变/慢变子系统用不同步长，通过多速率接口同步 | Shu 2017多速率框架 |
| **多求解器集成** | EMT/DP/FAST/TS四求解器按需自适应分配 | Rupasinghe 2023多求解器框架 |

## 形式化表示

### 接口方程数学框架

EMT-TS 混合仿真的接口可抽象为两个子系统在边界变量上的交替求解：

$$
\mathbf{x}_E^{k+1} = \mathbf{f}_E\left(\mathbf{x}_E^k, \mathbf{z}_T^k, \Delta t_E\right), \qquad
\mathbf{x}_T^{k+1} = \mathbf{f}_T\left(\mathbf{x}_T^k, \mathbf{z}_E^k, \Delta t_T\right) \tag{1}
$$

其中 $\mathbf{x}_E$ 和 $\mathbf{x}_T$ 分别是 EMT 和 TS 子系统的状态向量，$\mathbf{z}_E, \mathbf{z}_T$ 是边界变量。关键在于边界变量的传递方式。

### Thevenin 等值接口

当 EMT 子系统在第 $k$ 步的边界电压为 $\mathbf{v}_b^k$、边界电流为 $\mathbf{i}_b^k$ 时，TS 侧看到的 Thevenin 等值为：

$$
\mathbf{v}_b^k = \mathbf{v}_{\text{th}}^k - \mathbf{Z}_{\text{th}}^k \mathbf{i}_b^k \tag{2}
$$

其中 Thevenin 阻抗 $\mathbf{Z}_{\text{th}}$ 需随频率更新（见 Plumier 2016）。阻抗更新频率影响迭代收敛速度——每步更新 vs 每 $N$ 步更新存在精度-效率权衡。

### 时变接口模型（Shu 2017 多速率）

多速率协同中，接口参数通过移动窗口预测、逐步校正和平均技术消除混叠/延迟误差：

$$
\hat{\mathbf{v}}_{\text{th}}^{k+m} = \frac{1}{W}\sum_{j=0}^{W-1}\mathbf{v}_{\text{th}}^{k-j}, \qquad m \in \mathbb{Z}^+ \tag{3}
$$

其中 $W$ 为移动窗口宽度，$\hat{\mathbf{v}}_{\text{th}}$ 为预测的 Thevenin 电压。

### 松弛迭代接口（Plumier 2016）

松弛迭代的迭代方程为：

$$
\mathbf{z}_E^{k+1,(n+1)} = \mathbf{C}_E \mathbf{z}_E^{k+1,(n)} + (1-\mathbf{C}_E)\mathbf{z}_T^{k+1,(n)} \tag{4}
$$

其中 $\mathbf{C}_E$ 为松弛矩阵（对角矩阵，控制迭代强度），$n$ 为迭代序号。收敛条件为 $\|\mathbf{z}_E^{k+1,(n+1)} - \mathbf{z}_E^{k+1,(n)}\| < \varepsilon_{\text{tol}}$。

### 接口位移与映射等效（Zhu 2021）

接口位移方法将物理端口迁移至松耦合位置，等效关系为：

$$
\mathbf{Y}_{\text{eq}} = \mathbf{A}^T \mathbf{Y}_{\text{port}} \mathbf{A}, \qquad \mathbf{v}_{\text{eq}} = \mathbf{A}^{-1} \mathbf{v}_{\text{port}} \tag{5}
$$

其中 $\mathbf{A}$ 为端口迁移变换矩阵，$\mathbf{Y}_{\text{eq}}$ 和 $\mathbf{v}_{\text{eq}}$ 分别为等效导纳矩阵和等效端口电压。

### SFA-EMT 直接接口协议（Tarazona 2026）

SFA-EMT 协议通过并行追踪 EMT 解的实部和虚部分量，实现与复数形式 SFA 解的直接耦合：

$$
\tilde{\mathbf{x}}_{\text{EMT}} = \mathbf{x}_{\text{EMT,real}} + j\mathbf{x}_{\text{EMT,imag}}, \qquad \tilde{\mathbf{x}}_{\text{SFA}} = \mathbf{x}_{\text{SFA,complex}} \tag{6}
$$

接口耦合无需时间步延迟或迭代，仅需复数变换。

## 关键技术挑战

### 挑战 1：接口精度与带宽限制

动态相量提取方法的频谱特性决定了接口带宽。Rupasinghe 2021 评估了五种相量提取方法的性能：

| 方法 | 幅值误差 | 相位误差 | 适用信号 |
|------|---------|---------|---------|
| 傅里叶变换（FFT）| 低 | 低 | 纯基频稳态 |
| 滑动 DFT | 中 | 中 | 缓变动态 |
| 正交滤波器 | 低-中 | 低 | 含谐波信号 |
| 插值 DFT | 中 | 低 | 频偏信号 |
| 广义平均 | 中 | 中-高 | 强暂态 |

**接口位移映射等效**（Zhu 2021）通过物理位置迁移将强耦合接口转换为松耦合接口，有效降低接口精度要求。

### 挑战 2：数值稳定性与无源性

FDNE 模型在宽频带内必须保持无源。Zhang 2012（FDNE for hybrid simulation）结合矢量拟合（[[vector-fitting]]）与半尺寸无源性检测：

$$
\mathbf{Y}(s) = \sum_{i=1}^{N}\frac{r_i}{s - p_i} \quad \Rightarrow \quad \text{Re}(\mathbf{Y}(j\omega)) \geq 0, \quad \forall \omega \geq 0 \tag{7}
$$

无源性强制（[[passivity-enforcement]]）后，混合仿真中的数值发散问题可彻底消除（Zhang 2012 实验验证）。

### 挑战 3：多速率同步与延迟

多速率协同的核心问题是快慢系统间的同步误差。Shu 2017 的解决策略：

1. **混叠抑制**：接口参数采用移动窗口平均（式(3)）抑制高频分量混叠
2. **延迟补偿**：逐步校正技术实时修正接口时延
3. **振荡抑制**：数值振荡抑制算法保证接口离散化稳定性

### 挑战 4：不对称故障与等值失配

机电侧不对称故障会导致 FDNE 等值失配。Zhang 2012 提出的伴随初始化与临界电气距离指标可判断何时需要更新 FDNE，避免不必要的重新计算。

### 挑战 5：接口协议与通信架构

大规模系统的分布式混合仿真需要高效的通信接口。Design and Implementation of Scalable Communication Interfaces (2025) 提出了本地局域网（低延迟交互）与远程互联网（广域数据交换）的双模通信架构，适用于IBR渗透率高的电力系统实时协同仿真。

## 量化性能边界

### 不同混合仿真方法的性能对比

| 方法/论文 | 接口类型 | 步长比 $\Delta t_T/\Delta t_E$ | 加速比 | 精度验证 |
|---------|---------|---------------------------|-------|---------|
| 松弛迭代接口（Plumier 2016）| PM-EMT | 10:1（10ms vs 1ms）| ~5× | 74-bus, 23-machine |
| 多速率EMT协同（Shu 2017）| AC-MTDC | 10:1（500μs vs 50μs）| 3-10× | 四端MMC-MTDC |
| 接口位移映射（Zhu 2021）| HVAC/DC | 10-20:1 | ~8× | 交直流混联系统 |
| SFA-EMT MATE（Tarazona 2026）| SFA-EMT | 20-50:1 | 5-20× | HVDC系统 |
| 多求解器框架（Rupasinghe 2023）| EMT/DP/FAST/TS | 自适应 | 10-50× | 现代电力系统 |
| DPIM接口（Huang & Vittal 2018）| EMT-DP | 10:1 | 6-15× | 新英格兰39节点 |

### 接口方法收敛性对比

| 等值方法 | 收敛速度 | 实现复杂度 | 稳定性 |
|---------|---------|-----------|------|
| 固定 Thevenin | 快（1步）| 低 | 边界平衡时良好 |
| 时变 Thevenin | 中（需更新）| 中 | 需阻抗更新策略 |
| 时变 Norton | 中 | 中 | 对电流源子系统更稳定 |
| 双端口等效 | 慢（需迭代）| 高 | 最通用但计算量大 |
| 松弛迭代（Plumier 2016）| 最慢（需迭代）| 高 | 最稳定但需参数整定 |

### 不同接口类型的适用场景

| 接口类型 | 步长比上限 | 边界不平衡度容忍 | 系统规模 |
|---------|----------|----------------|---------|
| Thevenin/Norton 等值 | 20:1 | 低 | 中等 |
| 动态相量接口 | 50:1 | 中 | 大规模 |
| 移频相量接口 | 100:1 | 中-高 | 大规模/宽频 |
| 松弛迭代接口 | 10:1 | 高 | 中等 |
| 接口位移映射 | 50:1 | 高 | 超大规模 |

## 适用边界与选择指南

### 方法选择决策表

**问**：需要模拟什么系统？接口电气距离如何？

**答**：根据以下决策树选择接口方法：

```
1. 接口边界平衡且电气距离远（>50km）
   → 固定 Thevenin/Norton 等值
   ↓ 不满足
2. 接口含强直流偏置或谐波分量
   → 动态相量接口（DPIM）或移频相量接口（HMD-TLM）
   ↓ 不满足
3. 需要宽频带分析（故障暂态、谐波传递）
   → SFA-EMT 直接接口（Tarazona 2026）或接口位移映射
   ↓ 不满足
4. 接口电气距离近、交互强
   → 松弛迭代接口（Plumier 2016）或 MATE 分布式协议
   ↓ 不满足
5. 超大规模系统、多求解器集成
   → 多求解器框架（Rupasinghe 2023）
```

**失效边界**：
- 接口电气距离过近（如 <5 km）、边界变量频谱超出接口模型带宽时，接口误差急剧增大
- 强不平衡故障（如单相接地）导致 Thevenin/Norton 等值失配，需要实时更新等值参数
- FDNE/有理模型无源性不足时，即使接口参数正确也会导致数值发散
- 多速率延迟不可忽略时（如通信延迟 > 1 步长），需要专门延迟补偿算法

## 相关方法

- [[multirate-method|多速率方法]] - 子系统差异化步长协同
- [[vector-fitting|矢量拟合]] - 接口频变网络等值
- [[passivity-enforcement|无源性强制]] - 等值模型稳定性保证
- [[state-space-method|状态空间法]] - 多域状态空间接口
- [[average-value-model|平均值模型]] - 多尺度模型切换
- [[dynamic-phasor|动态相量法]] - 跨域动态相量接口
- [[frequency-dependent-modeling|频率相关建模]] - 宽频混合建模
- [[real-time-simulation|实时仿真]] - 实时协同仿真

## 相关模型

- [[fdne-model|频变网络等值(FDNE)]] - 外部系统宽频等值
- [[synchronous-machine-model|同步电机模型]] - 机电侧等值模型
- [[mmc-model|MMC模型]] - 电磁侧详细模型
- [[vsc-model|VSC模型]] - 换流器接口模型

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| Plumier 等 - Co-Simulation of electromagnetic transients and Phasor models: a relaxation approach | 2016 | 松弛迭代接口理论与收敛性分析 |
| Shu 等 - A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC Systems | 2017 | 多速率接口模型与时变Thevenin/Norton等值 |
| Mudunkotuwa & Filizadeh - Co-simulation of electrical networks by interfacing EMT and dynamic-phasor simulators | 2018 | EMT-DP协同仿真接口算法 |
| Zhu 等 - Interface Displacement and Dynamic Phasor Mapping Equivalence Based Hybrid Simulation | 2021 | 接口位移与映射等效方法 |
| Rupasinghe 等 - Assessment of dynamic phasor extraction methods for power system co-simulation applications | 2021 | 五种动态相量提取方法系统评估 |
| Rupasinghe 等 - A multi-solver framework for co-simulation of transients in modern power systems | 2023 | EMT/DP/FAST/TS四求解器集成框架 |
| Tarazona 等 - SFA-EMT hybrid simulation of power systems: Application to HVDC systems | 2026 | MATE框架SFA-EMT无延迟直接接口协议 |
| Zhang 等 - Frequency dependent network equivalent for electromagnetic and electromechanical hybrid simulation | 2012 | FDNE与矢量拟合无源性强制 |
| Huang & Vittal - Advanced EMT and Phasor-Domain Hybrid Simulation With Simulation Mode Switching | 2018 | 仿真模式切换与DPIM接口 |

## 附录：混合仿真分类体系架构图

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 800 320" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="320" fill="white"/>
  
  <!-- Layer 1: Input - 仿真子系统类型 -->
  <rect x="10" y="30" width="150" height="120" rx="5" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="85" y="52" font-family="Arial" font-size="11" font-weight="bold" text-anchor="middle" fill="#1e40af">EMT 侧 (μs级)</text>
  <text x="20" y="75" font-family="Arial" font-size="9" fill="#333">• MMC/VSC 换流器</text>
  <text x="20" y="91" font-family="Arial" font-size="9" fill="#333">• DC-DC 变流器</text>
  <text x="20" y="107" font-family="Arial" font-size="9" fill="#333">• 故障暂态分析</text>
  <text x="20" y="123" font-family="Arial" font-size="9" fill="#333">• 谐波传递路径</text>
  <text x="20" y="139" font-family="Arial" font-size="9" fill="#333">步长: 1-50 μs</text>
  
  <rect x="10" y="160" width="150" height="80" rx="5" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="85" y="182" font-family="Arial" font-size="11" font-weight="bold" text-anchor="middle" fill="#166534">TS/相量侧 (ms级)</text>
  <text x="20" y="204" font-family="Arial" font-size="9" fill="#333">• 同步发电机</text>
  <text x="20" y="220" font-family="Arial" font-size="9" fill="#333">• 机电振荡分析</text>
  <text x="20" y="236" font-family="Arial" font-size="9" fill="#333">步长: 1-10 ms</text>
  
  <rect x="10" y="250" width="150" height="60" rx="5" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="85" y="272" font-family="Arial" font-size="11" font-weight="bold" text-anchor="middle" fill="#92400e">SFA/DP 侧</text>
  <text x="20" y="294" font-family="Arial" font-size="9" fill="#333">• 移频相量分析 · 步长: 50-500 μs</text>
  
  <!-- Layer 2: 接口层 - 5种接口类型 -->
  <rect x="200" y="30" width="200" height="280" rx="5" fill="#f5f5f5" stroke="#666" stroke-width="2"/>
  <text x="300" y="52" font-family="Arial" font-size="11" font-weight="bold" text-anchor="middle" fill="#333">接口层（5类方法）</text>
  
  <rect x="210" y="65" width="180" height="35" rx="3" fill="#e0e7ff" stroke="#3730a3" stroke-width="1.5"/>
  <text x="300" y="85" font-family="Arial" font-size="9" font-weight="bold" text-anchor="middle" fill="#3730a3">Thevenin/Norton 等值</text>
  
  <rect x="210" y="108" width="180" height="35" rx="3" fill="#dcfce7" stroke="#166534" stroke-width="1.5"/>
  <text x="300" y="128" font-family="Arial" font-size="9" font-weight="bold" text-anchor="middle" fill="#166534">动态相量接口 (DPIM)</text>
  
  <rect x="210" y="151" width="180" height="35" rx="3" fill="#fef3c7" stroke="#92400e" stroke-width="1.5"/>
  <text x="300" y="171" font-family="Arial" font-size="9" font-weight="bold" text-anchor="middle" fill="#92400e">移频相量接口 (SFA/SFP)</text>
  
  <rect x="210" y="194" width="180" height="35" rx="3" fill="#fce7f3" stroke="#9d174d" stroke-width="1.5"/>
  <text x="300" y="214" font-family="Arial" font-size="9" font-weight="bold" text-anchor="middle" fill="#9d174d">松弛迭代接口</text>
  
  <rect x="210" y="237" width="180" height="35" rx="3" fill="#e5e5e5" stroke="#525252" stroke-width="1.5"/>
  <text x="300" y="257" font-family="Arial" font-size="9" font-weight="bold" text-anchor="middle" fill="#525252">接口位移映射等效</text>
  
  <!-- Layer 3: 协同架构 + 输出 -->
  <rect x="440" y="30" width="160" height="120" rx="5" fill="#f5f5f5" stroke="#666" stroke-width="2"/>
  <text x="520" y="52" font-family="Arial" font-size="11" font-weight="bold" text-anchor="middle" fill="#333">协同架构</text>
  <text x="450" y="75" font-family="Arial" font-size="9" fill="#333">• 集中式混合仿真</text>
  <text x="450" y="91" font-family="Arial" font-size="9" fill="#333">• 分布式 MATE 协议</text>
  <text x="450" y="107" font-family="Arial" font-size="9" fill="#333">• 多求解器集成框架</text>
  <text x="450" y="123" font-family="Arial" font-size="9" fill="#333">• 多速率EMT协同</text>
  
  <rect x="440" y="160" width="160" height="150" rx="5" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="520" y="182" font-family="Arial" font-size="11" font-weight="bold" text-anchor="middle" fill="#5b21b6">量化性能</text>
  <text x="450" y="204" font-family="Arial" font-size="9" font-weight="bold" fill="#5b21b6">加速比:</text>
  <text x="450" y="220" font-family="Arial" font-size="9" fill="#333">EMT-TS: 5-15×</text>
  <text x="450" y="236" font-family="Arial" font-size="9" fill="#333">多速率: 3-10×</text>
  <text x="450" y="252" font-family="Arial" font-size="9" fill="#333">SFA-EMT: 5-20×</text>
  <text x="450" y="268" font-family="Arial" font-size="9" fill="#333">多求解器: 10-50×</text>
  <text x="450" y="284" font-family="Arial" font-size="9" fill="#333">步长比上限: 20-100:1</text>
  
  <!-- Layer 4: 关键方法/论文 -->
  <rect x="640" y="30" width="150" height="280" rx="5" fill="#fafafa" stroke="#ddd" stroke-width="2"/>
  <text x="715" y="52" font-family="Arial" font-size="11" font-weight="bold" text-anchor="middle" fill="#333">代表方法</text>
  <text x="650" y="75" font-family="Arial" font-size="9" fill="#333">Plumier 2016</text>
  <text x="650" y="91" font-family="Arial" font-size="9" fill="#444">松弛迭代接口</text>
  <text x="650" y="115" font-family="Arial" font-size="9" fill="#333">Shu 2017</text>
  <text x="650" y="131" font-family="Arial" font-size="9" fill="#444">时变Thevenin/Norton</text>
  <text x="650" y="155" font-family="Arial" font-size="9" fill="#333">Zhu 2021</text>
  <text x="650" y="171" font-family="Arial" font-size="9" fill="#444">接口位移映射</text>
  <text x="650" y="195" font-family="Arial" font-size="9" fill="#333">Tarazona 2026</text>
  <text x="650" y="211" font-family="Arial" font-size="9" fill="#444">SFA-EMT MATE</text>
  <text x="650" y="235" font-family="Arial" font-size="9" fill="#333">Rupasinghe 2023</text>
  <text x="650" y="251" font-family="Arial" font-size="9" fill="#444">多求解器集成</text>
  <text x="650" y="275" font-family="Arial" font-size="9" fill="#333">Zhang 2012</text>
  <text x="650" y="291" font-family="Arial" font-size="9" fill="#444">FDNE + 矢量拟合</text>
  
  <!-- 箭头 -->
  <line x1="160" y1="90" x2="200" y2="90" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  <line x1="160" y1="200" x2="200" y2="200" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  <line x1="160" y1="280" x2="200" y2="160" stroke="#333" stroke-width="2" stroke-dasharray="4,2"/>
  
  <line x1="400" y1="120" x2="440" y2="90" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  <line x1="400" y1="180" x2="440" y2="160" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  
  <line x1="600" y1="90" x2="640" y2="90" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  <line x1="600" y1="180" x2="640" y2="180" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>
  
  <text x="400" y="305" font-family="Arial" font-size="9" font-style="italic" fill="#666">关键公式: (1) 接口方程 · (2) Thevenin等值 · (3) 时变接口 · (4) 松弛迭代 · (5) 位移映射 · (6) SFA-EMT</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 混合仿真分类体系：EMT侧（μs步长）、TS/SFA侧（ms/μs步长）通过5类接口方法实现跨域协同，数据经分布式MATE协议汇聚后输出量化性能指标</p>