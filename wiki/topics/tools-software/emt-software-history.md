---
title: "EMT 软件平台发展史 (EMT Software History)"
type: topic
tags: [emt-software, history, emtp, pscad, atp, rtds, cloudpss, development, real-time-simulation]
created: "2026-05-01"
book-chapter: "21"
updated: "2026-05-18"
---

# EMT 软件平台发展史 (EMT Software History)

## 定义与边界

EMT 软件平台发展史是电力系统仿真技术演进的缩影。从 1960 年代 H.W. Dommel 在 BPA 开创性地提出梯形积分法和节点分析法，到今天的商业软件、开源工具、实时仿真器和云计算平台，EMT 软件经历了近 60 年的持续演进。这段历史不仅是算法和计算技术的进步，更反映了电力系统从传统同步发电机主导向电力电子并网、新能源高渗透、交直流混联的转型需求。

在 EMT 语境下，软件平台发展史涵盖：核心算法的确立（梯形法、节点法）、商业软件的兴起（EMTP、PSCAD）、开源生态的形成（ATP）、实时仿真的突破（RTDS）以及中国自主软件的崛起（CloudPSS）。

## 奠基时期：1960s–1970s

### Dommel 与 EMTP 的诞生

1969 年，Hermann W. Dommel 在 IEEE Transactions on Power Apparatus and Systems 发表奠基性论文：

> "Digital Computer Solution of Electromagnetic Transients in Single-and Multiphase Networks"

这篇论文提出了至今仍是 EMT 仿真核心的两大算法——梯形积分法和节点分析法（[[nodal-analysis]]）。

**梯形积分法**将微分方程 $dx/dt = f(t, x)$ 离散化为：

$$x_{n+1} = x_n + \frac{\Delta t}{2}[f(t_n, x_n) + f(t_{n+1}, x_{n+1})] \tag{1}$$

**伴随电路离散化**将储能元件（$L$、$C$）转化为等效导纳与历史电流源的并联：

$$G_{eq} \cdot v(t) = i_{inj}(t) + i_{hist}(t) \tag{2}$$

电感诺顿等效：$G_{eq} = 2L/\Delta t$，历史电流源 $i_{hist} = i_n - G_{eq}v_n$

电容戴维南等效：$G_{eq} = \Delta t/(2C)$，历史电压源 $e_{hist} = v_n - G_{eq}i_n$

### BPA 的历史作用

- 美国邦纳维尔电力局（BPA）在 1960–70 年代资助 Dommel 的开发工作
- BPA 需要分析高压直流输电（HVDC）系统的电磁暂态
- 1970 年代初期形成可运行的 EMTP 原型程序
- 奠定了商业 EMT 软件的技术基础

**技术特征**：批处理界面 + 文本输入文件；基本元件库：R、L、C、开关、简单线路模型；离线批处理计算。

## 商业化与扩散：1980s–1990s

### PSCAD/EMTDC 的创新

1980 年代，加拿大曼尼托巴大学（University of Manitoba）在 Dennis Woodford 等人领导下开发 PSCAD/EMTDC：

| 里程碑 | 年份 | 意义 |
|--------|------|------|
| EMTDC 求解引擎开发 | 1980s 初 | 基于 Dommel 算法，优化求解效率 |
| PSCAD 图形化界面 | 1980s | 首个拖拽式 EMT 仿真环境 |
| MODELS 自定义模型 | 1990s | 支持复杂控制逻辑 |
| 工业界广泛应用 | 1990s 至今 | 成为行业标准工具 |

**核心创新**：图形化建模降低使用门槛；EMTDC 求解引擎持续优化；用户自定义模型（MODELS 语言）支持控制逻辑；频率相关线路模型成熟。

### ATP 的诞生

- 基于早期公开的 EMTP 代码，1980s 末启动
- **开源免费**：促进学术研究，全球用户社区形成
- **ATPDraw**（1990s）：提供图形化界面，大幅降低使用门槛
- 学术研究首选工具，但大型商业工程模型支持不如商业软件

### EMTP-Works 与 EMTP-RV

2000 年代初，蒙特利尔理工学院（Polytechnique Montréal）的 Jean Mahseredjian 领导开发 EMTP-RV：

- **商业软件新标杆**：取代旧版 EMTP
- **频率相关网络等值（FDNE）**：高效处理大规模系统（[[frequency-dependent-network-equivalent]]）
- **多速率仿真**：不同子系统采用不同步长（[[multirate-method]]）
- **FLUX3D 耦合**：与磁场有限元软件协同

## 实时仿真突破：1990s–2000s

### RTDS 的诞生

1990 年代初，加拿大曼尼托巴水电公司（Manitoba Hydro）开发 RTDS（Real-Time Digital Simulator）：

**核心技术**：
- **固定步长算法**：保证确定性实时计算
- **并行计算架构**：多处理器分担计算负荷
- **专用 I/O 接口**：GTNET、GTFPGA 等接口卡
- **硬件在环（HIL）能力**：连接真实控制保护设备

**步长约束公式**：

$$L_{max} = c \cdot \Delta t$$

$50\,\mu$s 步长对应最短可模拟线路 $15\,$km（光速 $c = 3\times 10^8\,$m/s）。RTDS 的步长约束是实时仿真的物理极限。

| 子系统 | 典型步长 | 说明 |
|--------|---------|------|
| 交流网络 | $50\,\mu$s–$100\,\mu$s | 固定步长，保证实时性 |
| 控制系统接口 | $50\,\mu$s–$250\,\mu$s | 与外部硬件同步 |
| 数据记录 | $1\,$ms–$10\,$ms | 与 SCADA/PMU 兼容 |

### 多速率仿真的发展

EMTP-RV 等平台引入多速率仿真（[[multirate-method]]），允许：

- 电力电子换流器：$\Delta t = 1\,\mu$s–$10\,\mu$s
- 交流网络：$\Delta t = 50\,\mu$s–$100\,\mu$s
- 机电外部系统：$\Delta t = 1\,$ms–$10\,$ms

多速率仿真通过接口技术（[[interface-technique]]）实现不同步长子系统间的数据交换。

## 云原生与并行：2010s–2020s

### CloudPSS 的崛起

2010 年代中期，清华大学陈颖教授团队开始开发 CloudPSS：

**核心理念**：
- **云原生架构**：基于云计算的 EMT 仿真
- **大规模并行**：利用云平台弹性计算资源，可达数千核并行
- **协同仿真**：支持多用户、多模型协同
- **国产自主可控**：填补国内空白

**计算能力公式**：

$$\text{计算能力} = N_{CPU} \times f_{clock} \times \text{并行效率}$$

**国产化进程**：

| 年份 | 里程碑 |
|------|--------|
| 2015 | CloudPSS 项目启动 |
| 2018 | 首个版本发布 |
| 2020 | GPU 并行加速，计算效率大幅提升 |
| 2023 | 实时仿真模块发布，进入 HIL 市场 |
| 2025+ | 持续迭代，功能日趋完善 |

**ADPSS 与 PSModel**：
- **ADPSS**：中国电科院开发，机电-电磁混合仿真 ([[electromechanical-electromagnetic-hybrid-simulation]])
- **PSModel**：上海交大开发，电力电子专用

### GPU 并行加速

现代 EMT 软件利用 GPU 实现大规模并行计算（[[gpu-parallel-acceleration]]）：

| 计算模式 | 架构 | 典型加速比 | 适用场景 |
|---------|------|-----------|---------|
| CPU 串行 | 单核 | $1\times$ | 基准 |
| CPU 多核 | 多核 CPU | $4$–$16\times$ | 中小系统 |
| GPU 通用 | CUDA/OpenCL | $50$–$200\times$ | 大规模电力电子 |
| GPU+FPGA 异构 | 混合架构 | $100$–$500\times$ | 实时仿真 |

GPU 加速特别适用于电力电子换流器详细模型（MMC、模块化多电平）的大量开关状态更新。

GPU 并行计算的核心指标——每周期浮点运算数（FLOP/cycle）：

$$N_{FLOP} = N_{threads} \times N_{ops/thread} \times \text{利用率} \tag{3}$$

现代 NVIDIA A100 GPU 提供约 $19.5\,$TFLOPS（FP64），相较 64 核 CPU 的约 $1\,$TFLOPS，理论加速比达 $20\times$。

## AI 赋能与数字孪生：2020s–2026

### 人工智能集成

- **AI 辅助建模**：自动生成等效模型 ([[automatic-model-reduction]])
- **智能步长控制**：基于机器学习的自适应步长 ([[adaptive-step-size]])
- **故障诊断**：模式识别辅助分析 ([[fault-analysis-methods]])
- **预测性仿真**：基于历史数据预测暂态行为

### 数字孪生平台

- **实时数据对接**：SCADA/PMU 数据驱动 ([[wide-area-monitoring-protection]])
- **在线仿真**：与物理系统同步运行
- **预测性分析**：提前识别潜在问题
- **全生命周期管理**：从设计到退役

### 新型计算架构

| 架构 | 特点 | 应用场景 |
|------|------|---------|
| GPU 加速 | 大规模并行 | 详细电力电子模型 |
| FPGA | 纳秒级延迟 | 超实时仿真 |
| 量子计算 | 指数级加速 | 未来潜力 |
| 边缘计算 | 分布式部署 | 配电网实时仿真 |

## 主流软件对比

### 算法特性对比

| 软件 | 开发商 | 类型 | 核心算法 | 典型步长 | 系统规模 |
|------|--------|------|---------|---------|---------|
| BPA EMTP | BPA/EMTP LLC | 商业 | 梯形法 | $50\,\mu$s | $<100$ 节点 |
| PSCAD/EMTDC | Manitoba Hydro Int'l | 商业 | 改进梯形法 | $50\,\mu$s | $<1000$ 节点 |
| ATP | 开源社区 | 开源 | 标准梯形法 | $50\,\mu$s | $<2000$ 节点 |
| EMTP-RV | Polytechnique Montréal | 商业 | DIRK + 多速率 | $10$–$100\,\mu$s | $<10000$ 节点 |
| RTDS | RTDS Technologies | 商业实时 | 固定步长 | $50\,\mu$s | $<5000$ 节点 |
| CloudPSS | 清华大学 | 国产云原生 | 云并行 | 可调 | $>100000$ 节点 |
| ADPSS | 中国电科院 | 国产 | 机电-电磁混合 | 混合 | $>50000$ 节点 |

### 技术演进时间线

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 400" xmlns="http://www.w3.org/2000/svg">
  <!-- Timeline arrow -->
  <line x1="50" y1="350" x2="850" y2="350" stroke="#333" stroke-width="2"/>
  <polygon points="850,345 860,350 850,355" fill="#333"/>
  
  <!-- Era 1: Foundation -->
  <circle cx="80" cy="350" r="8" fill="#2563eb"/>
  <line x1="80" y1="342" x2="80" y2="200" stroke="#2563eb" stroke-width="1" stroke-dasharray="3,3"/>
  <rect x="30" y="160" width="100" height="40" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5" rx="4"/>
  <text x="80" y="180" font-size="10" text-anchor="middle" fill="#1e40af">1969</text>
  <text x="80" y="193" font-size="9" text-anchor="middle" fill="#1e40af">Dommel EMTP</text>
  
  <!-- Era 2: Commercialization -->
  <circle cx="230" cy="350" r="8" fill="#16a34a"/>
  <line x1="230" y1="342" x2="230" y2="200" stroke="#16a34a" stroke-width="1" stroke-dasharray="3,3"/>
  <rect x="180" y="160" width="100" height="40" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5" rx="4"/>
  <text x="230" y="180" font-size="10" text-anchor="middle" fill="#166534">1980s</text>
  <text x="230" y="193" font-size="9" text-anchor="middle" fill="#166534">PSCAD/EMTDC</text>
  
  <circle cx="300" cy="350" r="8" fill="#16a34a"/>
  <line x1="300" y1="342" x2="300" y2="200" stroke="#16a34a" stroke-width="1" stroke-dasharray="3,3"/>
  <rect x="250" y="160" width="100" height="40" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5" rx="4"/>
  <text x="300" y="180" font-size="10" text-anchor="middle" fill="#166534">1980s末</text>
  <text x="300" y="193" font-size="9" text-anchor="middle" fill="#166534">ATP开源</text>
  
  <!-- Era 3: Real-time -->
  <circle cx="400" cy="350" r="8" fill="#d97706"/>
  <line x1="400" y1="342" x2="400" y2="200" stroke="#d97706" stroke-width="1" stroke-dasharray="3,3"/>
  <rect x="350" y="160" width="100" height="40" fill="#fef3c7" stroke="#d97706" stroke-width="1.5" rx="4"/>
  <text x="400" y="180" font-size="10" text-anchor="middle" fill="#92400e">1990s初</text>
  <text x="400" y="193" font-size="9" text-anchor="middle" fill="#92400e">RTDS实时</text>
  
  <circle cx="470" cy="350" r="8" fill="#d97706"/>
  <line x1="470" y1="342" x2="470" y2="200" stroke="#d97706" stroke-width="1" stroke-dasharray="3,3"/>
  <rect x="420" y="160" width="100" height="40" fill="#fef3c7" stroke="#d97706" stroke-width="1.5" rx="4"/>
  <text x="470" y="180" font-size="10" text-anchor="middle" fill="#92400e">2000s</text>
  <text x="470" y="193" font-size="9" text-anchor="middle" fill="#92400e">EMTP-RV</text>
  
  <!-- Era 4: Cloud -->
  <circle cx="580" cy="350" r="8" fill="#7c3aed"/>
  <line x1="580" y1="342" x2="580" y2="200" stroke="#7c3aed" stroke-width="1" stroke-dasharray="3,3"/>
  <rect x="530" y="160" width="100" height="40" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5" rx="4"/>
  <text x="580" y="180" font-size="10" text-anchor="middle" fill="#5b21b6">2015</text>
  <text x="580" y="193" font-size="9" text-anchor="middle" fill="#5b21b6">CloudPSS</text>
  
  <circle cx="660" cy="350" r="8" fill="#7c3aed"/>
  <line x1="660" y1="342" x2="660" y2="200" stroke="#7c3aed" stroke-width="1" stroke-dasharray="3,3"/>
  <rect x="610" y="160" width="100" height="40" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5" rx="4"/>
  <text x="660" y="180" font-size="10" text-anchor="middle" fill="#5b21b6">2020s</text>
  <text x="660" y="193" font-size="9" text-anchor="middle" fill="#5b21b6">GPU并行</text>
  
  <!-- Era 5: AI -->
  <circle cx="780" cy="350" r="8" fill="#dc2626"/>
  <line x1="780" y1="342" x2="780" y2="200" stroke="#dc2626" stroke-width="1" stroke-dasharray="3,3"/>
  <rect x="730" y="160" width="100" height="40" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" rx="4"/>
  <text x="780" y="180" font-size="10" text-anchor="middle" fill="#991b1b">2025+</text>
  <text x="780" y="193" font-size="9" text-anchor="middle" fill="#991b1b">AI数字孪生</text>
  
  <!-- Legend -->
  <rect x="50" y="30" width="15" height="15" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="70" y="42" font-size="10" fill="#333">奠基期</text>
  <rect x="140" y="30" width="15" height="15" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="160" y="42" font-size="10" fill="#333">商业化</text>
  <rect x="230" y="30" width="15" height="15" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="250" y="42" font-size="10" fill="#333">实时仿真</text>
  <rect x="330" y="30" width="15" height="15" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="350" y="42" font-size="10" fill="#333">云原生</text>
  <rect x="430" y="30" width="15" height="15" fill="#fee2e2" stroke="#dc2626" stroke-width="1"/>
  <text x="450" y="42" font-size="10" fill="#333">AI赋能</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · EMT 软件平台技术演进时间线（1969–2026）</p>

## 软件选择决策指南

| 应用场景 | 推荐软件 | 关键考量 |
|---------|---------|---------|
| 学术研究 | ATP / EMTP-RV | 可复现、算法透明、开源 |
| 工程设计 | PSCAD/EMTDC | 工业标准、丰富元件库 |
| 保护装置 HIL 测试 | RTDS | 实时 HIL、硬件接口 |
| 大规模系统仿真 | CloudPSS | 云并行、国产自主 |
| 教学培训 | ATP+ATPDraw | 免费、易学 |
| 多物理场耦合 | EMTP-RV+FLUX3D | 磁场协同仿真 |
| 机电-电磁混合 | ADPSS | 国网应用标准 |

## 关键技术指标演进

| 指标 | 1970s | 1990s | 2010s | 2025 |
|------|-------|-------|-------|------|
| 典型步长 | $100\,\mu$s | $50\,\mu$s | $20\,\mu$s | 自适应 |
| 最大节点数 | $<100$ | $<2000$ | $<10000$ | $>100000$ |
| 线路模型 | 无损 | Bergeron | 频变 | 宽频 |
| 开关模型 | 理想 | 改进理想 | 详细 | 混合 |
| 用户界面 | 文本 | 图形化 | 可视化 | AI 辅助 |
| 计算资源 | 大型机 | 工作站 | 集群 | 云端 |

## 相关方法

- [[numerical-integration]] — 梯形法、DIRK 等核心算法
- [[nodal-analysis]] — Dommel 求解框架
- [[real-time-simulation]] — RTDS 等实时平台技术
- [[co-simulation]] — 多软件协同仿真
- [[parallel-computing]] — 云原生仿真架构
- [[multirate-method]] — 多速率仿真方法
- [[interface-technique]] — 子系统接口技术

## 相关模型

- [[synchronous-machine-model]] — 各软件实现对比
- [[mmc-model]] — 现代电力电子建模
- [[transmission-line-model]] — 频变模型发展
- [[transformer-model]] — 宽频建模演进
- [[frequency-dependent-network-equivalent]] — FDNE 技术

## 相关主题

- [[emt-mathematical-foundation]] — 算法理论基础
- [[vsc-hvdc]] — 推动软件发展的应用需求
- [[wind-farm-modeling]] — 新能源仿真挑战
- [[electromechanical-electromagnetic-hybrid-simulation]] — 混合仿真技术

## 相关实体

- [[atp-emtp]] — 开源 EMT 软件
- [[pscad-emtdc]] — 商业图形化软件
- [[emtp]] — 现代商业软件
- [[rtds]] — 实时仿真器
- [[cloudpss]] — 国产云原生平台
- [[polytechnique-montreal]] — EMTP-RV 开发机构
- [[manitoba-hydro]] — PSCAD/RTDS 开发背景