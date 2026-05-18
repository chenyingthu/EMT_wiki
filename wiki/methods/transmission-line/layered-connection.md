---
title: "分层接入 (Layered Connection)"
type: method
tags: [layered, connection, hvdc, grid, uhvdc, multi-infeed, hierarchical, network-equivalent, fdne]
created: "2026-05-02"
updated: "2026-05-19"
---

# 分层接入 (Layered Connection)

## 定义与边界

分层接入（Layered Connection）是把一个外部系统、换流站或等值网络按电气层次拆分为若干层，并在边界端口处分别给出电压、电流、功率或导纳关系的接口建模方法。它在 EMT 语境下是一种**边界组织方法**，而非某一种固定设备模型。常见对象包括：

- 多电压等级交流接入（UHVDC 受端分层接入不同交流电压层）
- 机电-电磁混合仿真接口（EMT 区域与机电区域的分层边界）
- 频变网络等值的详细层与外部等值层（两层结构）
- 多端口换流站或外部网络等值（多馈入系统的分层边界）

**核心约束**：分层接入不能把"工程层级"或"电压等级"写成自然解耦。不同电压层、换流器群或交流区域之间的显著耦合必须通过非对角导纳项保留，否则会改变故障电流分配、振荡阻尼或高频传播路径。

## EMT 中的角色

在 EMT 仿真中，分层接入主要用于三类问题：

1. **外部系统等值压缩**：将详细 EMT 区域与外部交流网络分开，避免把远方系统完整展开为节点方程
2. **多端口边界表示**：在多端口边界处分别表示不同电压层级、不同换流器群或不同外部网络分区的端口特性
3. **频变等值结构化**：对频率相关网络等值进行结构化处理——把扰动测试得到的详细层导纳与解析外部层导纳组合后进入时域仿真

核心价值是把"一个边界"改写为"多个可解释端口或层"，明确哪些动态由详细模型承担、哪些由等值模型承担、哪些跨层耦合必须通过接口算法保留。

## 核心机制

### 层与端口的数学表示

设边界端口按层分为 $L_1, L_2, \ldots, L_m$。每层端口电压和电流向量为：

$$\mathbf{v} = \begin{bmatrix} \mathbf{v}_1 \\ \mathbf{v}_2 \\ \cdots \\ \mathbf{v}_m \end{bmatrix}, \quad \mathbf{i} = \begin{bmatrix} \mathbf{i}_1 \\ \mathbf{i}_2 \\ \cdots \\ \mathbf{i}_m \end{bmatrix}$$

若外部网络在目标频段可近似为线性多端口导纳，则端口关系为：

$$\mathbf{i}(s) = \mathbf{Y}_{\mathrm{eq}}(s) \mathbf{v}(s) + \mathbf{i}_{\mathrm{src}}(s)$$

其中 $\mathbf{Y}_{\mathrm{eq}}(s)$ 的**对角块**表示各层**自导纳**，**非对角块**表示**层间耦合导纳**。忽略非对角项会改变故障电流分配、振荡阻尼或高频传播路径。

### 双层频变等值（Two-Layer FDNE）

在频变网络等值中，双层结构表示为：

$$\mathbf{Y}_{\mathrm{total}}(s) = \mathbf{Y}_{\mathrm{detail}}(s) + \mathbf{Y}_{\mathrm{external}}(s) + \mathbf{Y}_{\mathrm{comp}}(s)$$

三层含义：
- $\mathbf{Y}_{\mathrm{detail}}(s)$：详细层导纳，由端口扰动测试获得（保留宽频动态）
- $\mathbf{Y}_{\mathrm{external}}(s)$：等值层导纳，由外部网络拓扑和参数的解析消去获得
- $\mathbf{Y}_{\mathrm{comp}}(s)$：补偿层导纳，用于局部无源性补偿

该表达式说明"分层"并非简单叠加容量，而是把不同证据来源和不同建模可信度的导纳贡献放在同一端口方程中。

### 有理函数形式的频变导纳

频变导纳矩阵通常拟合为有理函数形式，以便转化为时域可递推的等效网络：

$$\mathbf{Y}(s) \approx \mathbf{Y}_{\mathrm{fit}}(s) = \mathbf{D} + s\mathbf{E} + \sum_{m=1}^{N_p} \frac{\mathbf{R}_m}{s - p_m}$$

其中 $p_m$ 为极点，$\mathbf{R}_m$ 为留数，$\mathbf{D}$ 和 $\mathbf{E}$ 为常数项。该形式可转化为 EMT 时域中的 RLC 支路和历史电流源，实现频变等值的时域接口。

### 多端口 π 型网络等效

多端口 FDNE 可转化为 π 型网络表示：

- **端口间支路导纳**：对应非对角导纳的相反数，即 $Y_{ij}^{\pi} = -Y_{ij}$（$i \neq j$）
- **对地支路导纳**：由每行导纳求和得到，即 $Y_{i\mathrm{g}} = \sum_j Y_{ij}$

该结构可直接接入 EMTP 的 RLC 支路模块进行时域仿真。

### 无源性约束

频变等值进入 EMT 时域求解前必须满足无源性约束（Passivity Enforcement），否则离散后可能产生非物理能量注入。无源性要求：

$$\lambda_{\min}\left( \frac{\mathbf{Y}(j\omega) + \mathbf{Y}^H(j\omega)}{2} \right) \geq 0, \quad \forall \omega$$

即导纳矩阵的埃尔米特部分（$\mathbf{Y} + \mathbf{Y}^H$）的所有特征值非负。局部无源性补偿通过叠加辅助有理函数在问题频带局部修正，而非全局重优化。

### 功率分配与接口约束

若分层接入用于 HVDC 或换流站功率注入，接口约束为：

$$P_{\mathrm{dc}} = \sum_{k=1}^{m} P_k + P_{\mathrm{loss}}$$

$$Q_k = Q_{\mathrm{filter},k} + Q_{\mathrm{control},k} + Q_{\mathrm{network},k}$$

其中 $P_k$ 和 $Q_k$ 是第 $k$ 层交流侧注入或吸收的有功、无功。固定比例分配只是控制策略之一，故障、限流、换相失败、控制模式切换和无功约束都会改变各层功率和电压响应。

## 分类与变体

| 变体 | 建模对象 | EMT 表示 | 主要边界 |
|------|----------|----------|----------|
| 电压等级分层接入 | 直流或换流站接入不同交流电压层 | 多端口功率注入或换流器详细模型 | 需绑定具体工程和控制策略 |
| 双层频变网络等值 | 详细层加外部等值层 | $\mathbf{Y}_{\mathrm{detail}}(s)+\mathbf{Y}_{\mathrm{external}}(s)$ | 需检查拟合精度、无源性和端口定义 |
| 分区混合仿真接口 | EMT 区域与机电区域 | 戴维南、诺顿或动态导纳接口 | 多速率同步和延迟会影响结果精度 |
| 多馈入等值边界 | 多个换流器或多端口交流网络 | 块导纳矩阵和耦合项 | 不能把端口独立化后忽略耦合 |
| 分层控制接入 | 多换流器或多层电压控制 | 控制环加网络方程联解 | 控制模式和限幅需要显式说明 |

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 800 360" xmlns="http://www.w3.org/2000/svg">
  <!-- 背景 -->
  <rect width="800" height="360" fill="white"/>
  <!-- 列头 -->
  <rect x="20" y="20" width="160" height="30" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="100" y="40" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e40af">① 物理系统</text>
  <rect x="220" y="20" width="160" height="30" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="300" y="40" text-anchor="middle" font-size="13" font-weight="bold" fill="#166534">② 层与端口</text>
  <rect x="420" y="20" width="160" height="30" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="500" y="40" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e">③ EMT建模方法</text>
  <rect x="620" y="20" width="160" height="30" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="700" y="40" text-anchor="middle" font-size="13" font-weight="bold" fill="#5b21b6">④ 量化边界</text>
  <!-- 连接线 -->
  <line x1="180" y1="35" x2="220" y2="35" stroke="#555" stroke-width="1.5"/>
  <polygon points="216,31 220,35 216,39" fill="#555"/>
  <line x1="380" y1="35" x2="420" y2="35" stroke="#555" stroke-width="1.5"/>
  <polygon points="416,31 420,35 416,39" fill="#555"/>
  <line x1="580" y1="35" x2="620" y2="35" stroke="#555" stroke-width="1.5"/>
  <polygon points="616,31 620,35 616,39" fill="#555"/>
  <!-- 分隔线 -->
  <line x1="200" y1="55" x2="200" y2="340" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="400" y1="55" x2="400" y2="340" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,3"/>
  <line x1="600" y1="55" x2="600" y2="340" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4,3"/>
  <!-- 第一列内容 -->
  <rect x="20" y="70" width="160" height="55" rx="4" fill="#f0f9ff" stroke="#93c5fd" stroke-width="1"/>
  <text x="30" y="88" font-size="11" fill="#1e40af">• UHVDC 多电压等级接入</text>
  <text x="30" y="103" font-size="11" fill="#1e40af">• MMC 换流站群落</text>
  <text x="30" y="118" font-size="11" fill="#1e40af">• 交流网络分区</text>
  <rect x="20" y="135" width="160" height="55" rx="4" fill="#f0f9ff" stroke="#93c5fd" stroke-width="1"/>
  <text x="30" y="153" font-size="11" fill="#1e40af">• 端口扰动测试</text>
  <text x="30" y="168" font-size="11" fill="#1e40af">• 外部网络解析消去</text>
  <text x="30" y="183" font-size="11" fill="#1e40af">• 局部无源补偿</text>
  <!-- 第二列内容 -->
  <rect x="220" y="70" width="160" height="55" rx="4" fill="#f0fdf4" stroke="#86efac" stroke-width="1"/>
  <text x="230" y="88" font-size="11" fill="#166534">• 端口向量 v, i</text>
  <text x="230" y="103" font-size="11" fill="#166534">• 自导纳（对角块）</text>
  <text x="230" y="118" font-size="11" fill="#166534">• 耦合导纳（非对角）</text>
  <rect x="220" y="135" width="160" height="55" rx="4" fill="#f0fdf4" stroke="#86efac" stroke-width="1"/>
  <text x="230" y="153" font-size="11" fill="#166534">• 多端口诺顿等效</text>
  <text x="230" y="168" font-size="11" fill="#166534">• π 型网络支路</text>
  <text x="230" y="183" font-size="11" fill="#166534">• RLC 模块输出</text>
  <!-- 第三列内容 -->
  <rect x="420" y="70" width="160" height="55" rx="4" fill="#fffbeb" stroke="#fcd34d" stroke-width="1"/>
  <text x="430" y="88" font-size="11" fill="#92400e">• 双层 FDNE</text>
  <text x="430" y="103" font-size="11" fill="#92400e">• 有理函数拟合 Y(s)</text>
  <text x="430" y="118" font-size="11" fill="#92400e">• 无源性强制</text>
  <rect x="420" y="135" width="160" height="55" rx="4" fill="#fffbeb" stroke="#fcd34d" stroke-width="1"/>
  <text x="430" y="153" font-size="11" fill="#92400e">• 分层节点消去</text>
  <text x="430" y="168" font-size="11" fill="#92400e">• 嵌套快速求解</text>
  <text x="430" y="183" font-size="11" fill="#92400e">• EMT-TS 接口</text>
  <!-- 第四列内容 -->
  <rect x="620" y="70" width="160" height="55" rx="4" fill="#f5f3ff" stroke="#c4b5fd" stroke-width="1"/>
  <text x="630" y="88" font-size="11" fill="#5b21b6">• 精度：详细 vs 等值</text>
  <text x="630" y="103" font-size="11" fill="#5b21b6">• 宽频段保持 vs 工频</text>
  <text x="630" y="118" font-size="11" fill="#5b21b6">• 无源性验证通过率</text>
  <rect x="620" y="135" width="160" height="55" rx="4" fill="#f5f3ff" stroke="#c4b5fd" stroke-width="1"/>
  <text x="630" y="153" font-size="11" fill="#5b21b6">• 适用：MMC 交直流</text>
  <text x="630" y="168" font-size="11" fill="#5b21b6">• 失效：强非线性故障</text>
  <text x="630" y="183" font-size="11" fill="#5b21b6">• 原文未报告数值结果</text>
  <!-- 底部标签 -->
  <rect x="20" y="210" width="160" height="40" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="100" y="230" text-anchor="middle" font-size="11" fill="#1e40af">电压等级/换流站群</text>
  <rect x="220" y="210" width="160" height="40" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="300" y="230" text-anchor="middle" font-size="11" fill="#166534">端口导纳矩阵 Y_eq(s)</text>
  <rect x="420" y="210" width="160" height="40" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="500" y="230" text-anchor="middle" font-size="11" fill="#92400e">双层FDNE + 局部补偿</text>
  <rect x="620" y="210" width="160" height="40" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="700" y="230" text-anchor="middle" font-size="11" fill="#5b21b6">宽频 + 无源 + 精度</text>
  <!-- 底部流程箭头 -->
  <line x1="100" y1="260" x2="100" y2="275" stroke="#555" stroke-width="1.5"/>
  <line x1="100" y1="275" x2="180" y2="275" stroke="#555" stroke-width="1.5"/>
  <polygon points="176,271 180,275 176,279" fill="#555"/>
  <line x1="300" y1="260" x2="300" y2="275" stroke="#555" stroke-width="1.5"/>
  <line x1="300" y1="275" x2="380" y2="275" stroke="#555" stroke-width="1.5"/>
  <polygon points="376,271 380,275 376,279" fill="#555"/>
  <line x1="500" y1="260" x2="500" y2="275" stroke="#555" stroke-width="1.5"/>
  <line x1="500" y1="275" x2="580" y2="275" stroke="#555" stroke-width="1.5"/>
  <polygon points="576,271 580,275 576,279" fill="#555"/>
  <line x1="700" y1="260" x2="700" y2="275" stroke="#555" stroke-width="1.5"/>
  <line x1="700" y1="275" x2="780" y2="275" stroke="#555" stroke-width="1.5"/>
  <polygon points="776,271 780,275 776,279" fill="#555"/>
  <!-- 工作流框 -->
  <rect x="20" y="290" width="760" height="55" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="400" y="310" text-anchor="middle" font-size="12" font-weight="bold" fill="#334155">分层接入 EMT 建模工作流</text>
  <text x="70" y="330" text-anchor="middle" font-size="10" fill="#475569">① 确定端口</text>
  <text x="200" y="330" text-anchor="middle" font-size="10" fill="#475569">② 构建 Y_eq(s)</text>
  <text x="370" y="330" text-anchor="middle" font-size="10" fill="#475569">③ 两层导纳分解</text>
  <text x="530" y="330" text-anchor="middle" font-size="10" fill="#475569">④ 无源性检查</text>
  <text x="700" y="330" text-anchor="middle" font-size="10" fill="#475569">⑤ EMTP 接口</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 分层接入 EMT 建模四层架构：物理系统输入 → 端口导纳建模 → 双层FDNE方法 → 量化性能边界</p>

## 关键技术挑战

### 挑战一：层间耦合导纳的保留

当网络包含多个电压层、换流器群或交流区域时，层间耦合通过非对角导纳项体现。若将分层接入简化为各层独立等值（即仅保留 $\mathbf{Y}_{\mathrm{eq}}(s)$ 的对角块），则故障电流分配、振荡阻尼和高频传播路径均会失真。精确的分层模型需要保留完整的非对角耦合矩阵，并在接口求解时显式联立。

### 挑战二：无源性验证与局部补偿

频域有理函数拟合得到的 $\mathbf{Y}_{\mathrm{eq}}(s)$ 可能违反无源性（Portivity），导致时域 EMT 求解时出现非物理能量注入。传统全局无源性强制需要同时改动全部模型参数，可能破坏原频响精度。全局优化扰动方法还面临不收敛、计算效率低和精度损失三者难以兼顾的问题。局部无源性补偿通过叠加辅助有理函数在问题频带增强无源性，避免全局重优化。

### 挑战三：多层边界端口选择

多层边界的端口选择影响高频耦合和故障电流分配的精度。端口定义过少会丢失层间动态，过多则增加接口计算复杂度。分层接入的端口选择需要综合考虑网络拓扑、控制耦合强度和研究频段。

### 挑战四：强非线性场景下的等值适用性

含换流器控制、保护动作和拓扑切换的分层等值不能只用单一 $\mathbf{Y}_{\mathrm{eq}}(s)$ 表示，而需要多运行点或事件驱动模型。在换相失败、故障清除、限流工况下，线性导纳等值会失效，需要切换到详细模型或分段线性模型。

### 挑战五：时域接口的数值稳定性

频变等值的多端口诺顿实现需要保证每个时间步的数值稳定性。历史电流源的递推、导纳矩阵的求逆和 RLC 支路的数值积分共同决定接口的稳定性上界。局部无源性补偿若无界放大补偿导纳，可能引入新的数值不稳定。

## 量化性能边界

分层接入的量化边界需要回到原文核验，当前可报告的信息如下：

| 维度 | 典型范围 | 备注 |
|------|----------|------|
| 适用系统 | MMC 交直流电网、UHVDC 分层接入 | 需绑定具体工程对象 |
| 保留频段 | DC – 10 kHz（详细层）；50/60 Hz – 1 kHz（等值层） | 取决于扰动测试频率范围 |
| 精度损失 | 原文未报告可核验数值 | 依赖测试系统对比 |
| 计算加速 | 原文未量化 | 定性描述为"一到两个数量级" |
| 无源性补偿 | 仅在违规频段叠加辅助项 | 局部修正 vs 全局优化 |

**证据边界**：上述数据来自 two-layer FDNE 和 multi-port FDNE 的原文摘要，**原文均未报告可核验的数值结果**（误差百分比、计算耗时、加速比、发散率等）。不应据此引用具体数字用于性能对比。

## 适用边界与选择指南

**适合场景**：
- 边界清晰、端口可定义、层间耦合可测量或可计算的系统
- 需要保留宽频动态（DC – 10 kHz）但不想展开远方系统的 EMT 仿真
- MMC 交直流混合系统的接口等值

**不适合场景**：
- 缺少端口数据、拓扑频繁改变或控制逻辑不可见时直接替代详细模型
- 强非线性故障（换相失败、严重过电流）需要切换到分段线性模型
- 工频等值研究高频振荡或宽频相互作用

**变体选择决策表**：

| 场景 | 推荐变体 | 理由 |
|------|----------|------|
| MMC 并网宽频相互作用分析 | 双层频变网络等值 | 兼顾详细层宽频精度和等值层计算效率 |
| UHVDC 受端多电压等级接入 | 电压等级分层接入 | 不同电压层需独立端口定义和控制策略 |
| 大型输电网故障计算 | 多馈入等值边界 | 端口间耦合导纳必须保留 |
| EMT-TS 混合仿真接口 | 分区混合仿真接口 | 机电区域用等值导纳，EMT 区域保留详细模型 |
| 多换流器协调控制研究 | 分层控制接入 | 各换流器控制环与网络方程需联立求解 |

## 与相关页面的关系

- [[network-equivalent]] 是更高层主题，覆盖外部系统等值、动态等值和频率相关等值
- [[ac-coupled-network-equivalent]] 关注交流接口的端口变量和混合仿真边界；分层接入可视为其多层或多端口组织形式
- [[detailed-equivalent-model]] 关注在端口处保留宽频动态的详细等值；分层接入可把详细等值作为某一层
- [[norton-equivalent]] 和 [[equivalent-circuit-method]] 提供端口电路形式，常用于各层边界的时域实现
- [[transformer-network]] 与 [[ideal-transformer-equivalent]] 处理变压器端口和绕组关系，常出现在换流站或多电压层接入中
- [[passivity-enforcement]] 是频变分层等值进入 EMT 前的重要校核步骤

## 来源论文

- [[a-two-layer-network-equivalent-with-local-passivity-compensation-with-applicatio]] — 提出双层 FDNE：详细层导纳来自扰动测试，等值层导纳来自解析方法，并用局部辅助有理函数补偿无源性违规，用于 MMC 交直流电网的 EMT-TS 混合仿真接口。原文未报告可核验数值。
- [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical]] — 将 FDNE 用于电磁-机电混合仿真接口：通过频域扫描得到边界导纳频响，用矢量拟合形成有理函数矩阵，并结合半尺寸无源性测试矩阵与参数扰动检测和修正无源性违规。原文未报告可核验数值。
- [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i]] — 将单端口频变等值扩展为自动生成的多端口 FDNE：用 EMTP 兼容的 RLC 支路模块拟合端口导纳，对角项为自导纳、非对角项为端口间耦合。验证系统为 Ontario Hydro 500 kV 网络，原文未报告可核验数值。
- [[analysis-on-dynamic-characteristic-of-control-mode-for-800-kv-yun-guang-uhvdc]] — 建立云广 ±800 kV 直流详细 EMT 模型，比较整流侧定电流控制和定功率控制下的故障动态特性。可作为 UHVDC 控制模式和受端交流网络交互的来源入口，需回到原文确认工程对象和控制细节。