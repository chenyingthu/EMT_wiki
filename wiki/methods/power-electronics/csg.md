---
title: "CSG（中国南方电网）在EMT仿真中的角色"
type: method
tags: [csg, china-southern-grid, test-system, grid-entity, disambiguation]
created: "2026-05-05"
updated: "2026-05-14"
---

# CSG（中国南方电网）在EMT仿真中的角色

## 定义

`CSG` 是 **China Southern Grid（中国南方电网）** 的缩写，是中国五大电网公司之一，覆盖广东、广西、云南、贵州和海南五省区。在电磁暂态（EMT）仿真领域，CSG 主要作为**工程归属标识**和**测试系统来源**出现，而非独立的仿真方法或算法。

CSG 在 Wiki 中出现时有三种可能的语义：

$$
\operatorname{meaning}(\text{CSG} \mid c) \in \{
  \text{grid-entity},\;
  \text{closed-subscribed-group},\;
  \text{unknown}
\}
$$

其中上下文 $c$ 决定具体含义：

| 上下文类型 | 含义 | 示例 |
|-----------|------|------|
| 测试系统页、工程归属页 | CSG = 中国南方电网 | `[[luxi-back-to-back-mmc]]` 中的 `[[csg]]` |
| 配电系统、电力电子控制 | CSG = Closed Subscribed Group（封闭订阅组） | 文献中的通信拓扑术语 |
| 无明确上下文 | unknown | 孤立出现的 `[[csg]]` 链接 |

**核心判断规则**：在 EMT 仿真上下文中，`[[csg]]` 几乎总是指向中国南方电网。

## EMT 中的作用

### 测试系统来源

CSG 是中国 EMT 仿真测试系统的重要来源。南方电网管辖范围内有多个标志性电力工程，这些工程被抽象为标准化测试系统，供学术界和工业界验证 EMT 仿真算法：

- **鲁西背靠背MMC工程**（±350 kV, 1000 MW）：中国首个超高压大容量柔性直流背靠背工程，测试系统见 `[[luxi-back-to-back-mmc]]`
- **滇东南多直流馈入系统**：云南至广东的多回直流输电系统，用于验证多馈入交互分析
- **西电东送大通道**：云南-广西-广东的异步联网结构，用于验证跨区域 EMT 仿真

### 工程验证基准

CSG 相关工程为 EMT 仿真提供了大量实测数据：

- 换流器故障录波数据
- 系统振荡暂态波形
- 谐波测量结果
- 保护动作时序

这些数据是验证 EMT 模型精度的重要基准。

## CSG 测试系统与 EMT 建模

### 鲁西背靠背 MMC 测试系统

鲁西背靠背工程是 CSG 在 EMT 仿真中最具代表性的测试系统。其关键参数为：

**额定运行参数**：

$$
\begin{aligned}
V_{\text{dc, rated}} &= \pm 350 \text{ kV} \\
P_{\text{rated}} &= 1000 \text{ MW} \\
I_{\text{dc, rated}} &= \frac{P_{\text{rated}}}{V_{\text{dc, rated}}} = \frac{1000 \times 10^6}{350 \times 10^3} \approx 2857 \text{ A} \\
V_{\text{ac, rated}} &= 500 \text{ kV}
\end{aligned}
$$

**MMC 子模块参数**：

$$
\begin{aligned}
N_{\text{sub}} &= 400 \text{ (单桥臂)} \\
C_{\text{sub}} &\approx 10 \text{ mF} \\
V_{\text{sub, rated}} &= 1.75 \text{ kV} \\
L_{\text{arm}} &\approx 60 \text{ mH}
\end{aligned}
$$

**总子模块数**（6桥臂）：

$$
N_{\text{total}} = 6 \times 400 = 2400 \text{ (每极)}
$$

### EMT 建模方法

对于 CSG 相关工程的 EMT 仿真，通常采用以下建模策略：

1. **详细开关模型（Detailed Switch Model）**：用于换流器子模块级仿真，步长 ≤ 10 μs，适用于谐波分析和过电压研究
2. **平均值模型（Average Value Model, AVM）**：将 MMC 等效为可控电压源，步长 50-100 μs，适用于系统级暂态分析
3. **等效阻抗模型（Equivalent Impedance Model）**：将 CSG 交流侧等效为 Thevenin 阻抗，用于快速扫描分析

**建模方法选择**：

$$
\text{选择策略} = \begin{cases}
\text{详细开关模型} & \text{子模块级分析、电容电压均衡} \\
\text{平均值模型} & \text{系统级暂态、控制策略验证} \\
\text{等效阻抗模型} & \text{大规模系统扫描、灵敏度分析}
\end{cases}
$$

## 形式化判定

在 Wiki 链接解析中，`[[csg]]` 的判定流程为：

$$
\text{resolve}(\text{CSG}) = \begin{cases}
\text{China Southern Grid} & \text{if context} \in \{\text{test-system}, \text{engineering}, \text{grid}\} \\
\text{Closed Subscribed Group} & \text{if context} \in \{\text{distribution}, \text{communication}\} \\
\text{unknown} & \text{otherwise}
\end{cases}
$$

在 EMT Wiki 中，绝大多数 `[[csg]]` 链接都属于第一种情况。

## CSG 消歧决策流程

```html
<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 700 420" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
  
  <!-- Title -->
  <text x="350" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">CSG 消歧决策流程</text>
  
  <!-- Input node -->
  <rect x="250" y="50" width="200" height="40" rx="8" ry="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="350" y="75" text-anchor="middle" font-size="13" fill="#2563eb" font-weight="bold">遇到 [[csg]] 链接</text>
  
  <!-- Decision diamond -->
  <polygon points="350,115 500,165 350,215 200,165" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="350" y="155" text-anchor="middle" font-size="12" fill="#d97706">页面类型？</text>
  <text x="350" y="170" text-anchor="middle" font-size="12" fill="#d97706">上下文判断</text>
  
  <!-- Arrow from input to decision -->
  <line x1="350" y1="90" x2="350" y2="115" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Path 1: Test system / Engineering / Grid -->
  <line x1="500" y1="165" x2="580" y2="200" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="520" y="175" font-size="10" fill="#666">测试系统/工程/电网</text>
  
  <!-- Result 1: China Southern Grid -->
  <rect x="580" y="200" width="100" height="40" rx="8" ry="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="630" y="218" text-anchor="middle" font-size="11" fill="#16a34a" font-weight="bold">CSG =</text>
  <text x="630" y="233" text-anchor="middle" font-size="11" fill="#16a34a">中国南方电网</text>
  
  <!-- Path 2: Distribution / Communication -->
  <line x1="200" y1="165" x2="120" y2="200" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="130" y="175" font-size="10" fill="#666">配电/通信</text>
  
  <!-- Result 2: Closed Subscribed Group -->
  <rect x="20" y="200" width="100" height="40" rx="8" ry="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="70" y="218" text-anchor="middle" font-size="11" fill="#16a34a" font-weight="bold">CSG =</text>
  <text x="70" y="233" text-anchor="middle" font-size="11" fill="#16a34a">Closed Subscribed</text>
  <text x="70" y="246" text-anchor="middle" font-size="11" fill="#16a34a">Group</text>
  
  <!-- Path 3: Unknown -->
  <line x1="350" y1="215" x2="350" y2="280" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="370" y="250" font-size="10" fill="#666">无明确上下文</text>
  
  <!-- Result 3: Unknown -->
  <rect x="270" y="280" width="160" height="40" rx="8" ry="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="350" y="305" text-anchor="middle" font-size="11" fill="#dc2626" font-weight="bold">CSG = unknown</text>
  <text x="350" y="318" text-anchor="middle" font-size="10" fill="#dc2626">需要进一步查证</text>
  
  <!-- Legend -->
  <rect x="50" y="360" width="15" height="15" rx="3" ry="3" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="70" y="373" font-size="10" fill="#666">输入</text>
  
  <rect x="120" y="360" width="15" height="15" rx="3" ry="3" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="140" y="373" font-size="10" fill="#666">判断</text>
  
  <rect x="170" y="360" width="15" height="15" rx="3" ry="3" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="190" y="373" font-size="10" fill="#666">确定含义</text>
  
  <rect x="270" y="360" width="15" height="15" rx="3" ry="3" fill="#fee2e2" stroke="#dc2626" stroke-width="1"/>
  <text x="290" y="373" font-size="10" fill="#666">待查证</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · CSG 消歧决策流程</p>
```

## CSG 相关测试系统的量化性能

### 鲁西背靠背 MMC 的 EMT 仿真特性

| 仿真场景 | 步长 | 加速比 | 误差 | 适用性 |
|---------|------|--------|------|--------|
| 子模块级详细仿真 | 1-10 μs | 1× | < 1% | 电容电压均衡、环流分析 |
| MMC 平均值模型 | 50-100 μs | 5-10× | < 5% | 系统级暂态、控制验证 |
| 等效阻抗模型 | 200-500 μs | 20-50× | < 10% | 大规模系统扫描 |

*数据来源：Le-Huy 2023, Sinkar 2021*

### CSG 工程在 EMT 仿真中的挑战

1. **多时间尺度耦合**：CSG 系统包含从 μs 级开关瞬态到 s 级系统振荡的多个时间尺度，需要变步长求解器
2. **大规模系统并行**：云南-广西-广东异步联网系统包含数百个母线，需要并行计算加速
3. **多直流馈入交互**：多回 LCC/HVDC 并行运行导致换相失败传播，需要精确的 LCC 建模
4. **新能源接入**：云南地区大量风电和光伏接入，需要精确的 renewable energy 模型

## 适用边界与选择指南

### CSG 作为测试系统的使用场景

| 应用场景 | 推荐方法 | 说明 |
|---------|---------|------|
| 换流器建模验证 | `[[luxi-back-to-back-mmc]]` | 鲁西背靠背 MMC 是最直接的 CSG 测试系统 |
| 大规模系统仿真 | `[[large-scale-system-simulation]]` | CSG 系统规模适合大规模仿真方法研究 |
| LCC-HVDC 仿真 | `[[lcc-model]]` | CSG 有大量的 LCC-HVDC 工程 |
| MMC 建模验证 | `[[mmc-model]]` | CSG 的 MMC 工程为模型验证提供平台 |
| 多时间尺度仿真 | `[[variable-time-step-solver]]` | CSG 系统的时间尺度多样性需要变步长求解 |

### CSG 消歧指南

当在 Wiki 中遇到 `[[csg]]` 链接时：

1. **检查页面类型**：如果是测试系统页、工程页、电网实体页 → CSG = 中国南方电网
2. **检查邻接链接**：如果页面上有 `[[luxi-back-to-back-mmc]]`、`[[mmc-model]]` 等 → CSG = 中国南方电网
3. **检查来源论文**：如果来源论文作者来自 CSG（如 `ehv.csg.cn` 邮箱）→ CSG = 中国南方电网
4. **检查页面分类**：如果是配电系统页、电力电子控制页 → 可能是 Closed Subscribed Group

## 相关页面

- [[luxi-back-to-back-mmc]]：CSG 在 EMT 仿真中最具代表性的测试系统
- [[power-system]]：CSG 作为电网实体的上位概念
- [[mmc-model]]：CSG 鲁西工程中 MMC 换流器的模型
- [[lcc-model]]：CSG 有大量的 LCC-HVDC 工程，LCC 建模是 CSG 仿真的重要内容
- [[large-scale-system-simulation]]：CSG 系统规模适合大规模仿真方法研究
- [[variable-time-step-solver]]：CSG 多时间尺度系统需要变步长求解器
- [[emt-simulation]]：EMT 仿真通用背景
- [[power-electronics-control]]：电力电子控制通用入口
- [[network-equivalent]]：CSG 系统等值方法

## 来源论文

- **Le-Huy 等 2023** — 《Lessons Learned in Porting Offline Large-Scale Power System Simulation to Real-Time》：记录了 CSG 系统仿真到实时仿真的经验，包含 CSG 相关测试系统的仿真数据
- **Sinkar 等 2021** — 《A Comparative Study of EMT Simulations Using Companion Circuit and Descriptor State Equation Approaches》：提供了 EMT 仿真方法的对比数据，包括 CSG 相关系统
- **Filizadeh 等 2025** — 《Electromagnetic Transient Modeling and Simulation of Large Power Systems》：大规模电力系统 EMT 建模综述，涵盖 CSG 等大型电网的建模挑战
- **大电网仿真工具现状及其在华北电网推广应用的思考** — 中国电网 EMT 仿真工具应用现状，包含 CSG 等电网的仿真实践

## 证据边界

- CSG 在 EMT 仿真文献中主要作为**工程归属标识**出现，而非独立的仿真方法
- CSG 相关测试系统（如鲁西背靠背 MMC）为 EMT 仿真提供了重要的验证基准
- CSG 缩写在其他领域（如配电系统）可能有不同含义，但在 EMT 仿真上下文中几乎总是指中国南方电网
- 如果未来发现 CSG 作为独立 EMT 方法的文献来源，本页应升级为对应的方法页

## 开放问题

- CSG 是否有其他在 EMT 仿真文献中被广泛使用的缩写含义？
- 是否有专门的 CSG 测试系统页面集群（如 CSG-IEEE-118, CSG-IEEE-39）？
- CSG 相关工程是否有标准化的 EMT 仿真模型库可供复用？
