---
title: "EEAC (Extended Equal Area Criterion)"
type: method
tags: [eeac, equal-area, transient-stability, direct-method, single-machine-equivalent]
created: "2026-05-02"
updated: "2026-05-16"
---

# 扩展等面积准则 (EEAC)

## 定义与边界

扩展等面积准则（Extended Equal Area Criterion, EEAC）是把多机暂态功角稳定问题映射为等效单机无穷大系统（OMIB）后应用 [[equal-area-criterion]] 的直接法路线。它的核心不是重建完整 EMT 模型，而是识别临界机群与其余系统的相对运动，并把该相对运动转化为一条等效功率角曲线。

EEAC 最早由 Chiang（1980年代）提出，用于解决经典等面积准则（EAC）无法直接处理多机系统的问题。通过群间相对运动提取和 OMIB 等效，EEAC 将复杂的多机高维问题降维为低维面积判据，可在时域仿真轨迹上快速计算稳定裕度，无需额外迭代求解稳定边界。

本页讨论 EEAC 的方法框架。关于 EEAC 的提出年份、工程系统实现和具体性能数字，若没有可核验来源，不在本页写成强结论。EEAC 不能自动覆盖多摆失稳、电压失稳、保护连锁、换流器限流和详细 EMT 高频暂态。

## EMT 中的作用

EEAC 可作为 EMT 或 EMT-TS 混合仿真后的解释工具：从时域轨迹中识别领先机群、构造等效功角、计算加速/减速面积，并把稳定裕度与故障切除时间联系起来。它特别适合解释"哪个机群在首摆中被故障加速、切除后网络是否提供足够制动功率"。

若 EMT 细节会改变临界机群或等效电磁功率，例如 HVDC 控制、构网型变换器限流、动态负荷恢复或保护动作，则 EEAC 结果必须与完整时域轨迹互相校核。

在混合仿真场景中（参考 [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb-fix]]），EMT 侧提供详细的换流器和故障动态，TS 侧提供机电尺度轨迹。EEAC 可用于后处理 EMT-TS 混合仿真结果，解释机群分离的物理机制。

## 核心机制

### 群角与群速定义

设多机系统被划分为临界群 $C$ 和非临界群 $N$。用惯性加权平均定义群角和群速：

$$\delta_C=\frac{\sum_{i\in C}M_i\delta_i}{\sum_{i\in C}M_i},\qquad
\delta_N=\frac{\sum_{j\in N}M_j\delta_j}{\sum_{j\in N}M_j}$$

$$\omega_C=\frac{\sum_{i\in C}M_i\omega_i}{\sum_{i\in C}M_i},\qquad
\omega_N=\frac{\sum_{j\in N}M_j\omega_j}{\sum_{j\in N}M_j}$$

等效 OMIB 变量为：

$$\delta_{eq}=\delta_C-\delta_N,\qquad
\omega_{eq}=\omega_C-\omega_N$$

等效惯性可写为：

$$M_{eq}=\frac{M_C M_N}{M_C+M_N},\qquad
M_C=\sum_{i\in C}M_i,\quad M_N=\sum_{j\in N}M_j$$

### 等效摇摆方程

等效 OMIB 的单自由度摇摆方程为：

$$M_{eq}\frac{d^2\delta_{eq}}{dt^2}=P_{m,eq}-P_{e,eq}(\delta_{eq},t)$$

其中等效机械功率和电磁功率为：

$$P_{m,eq}=P_m^C - P_m^N$$

$$P_{e,eq}(\delta_{eq},t) = \frac{M_N P_e^C(\delta_{eq}) - M_C P_e^N(\delta_{eq})}{M_C+M_N}$$

### 面积裕度计算

若故障期间和切除后可得到等效功率角曲线，则加速面积和最大减速面积为：

$$A_{\mathrm{acc}}
=\int_{\delta_0}^{\delta_c}
\left(P_{m,eq}-P_{e,eq}^{fault}\right)d\delta$$

$$A_{\mathrm{dec,max}}
=\int_{\delta_c}^{\delta_u}
\left(P_{e,eq}^{post}-P_{m,eq}\right)d\delta$$

首摆稳定的等效判据是 $A_{\mathrm{acc}}<A_{\mathrm{dec,max}}$。该判据的可信度取决于机群识别、等效功率曲线和故障后稳定边界是否与原多机轨迹一致。

### 稳定裕度

稳定裕度可定义为：

$$\eta = \frac{A_{\mathrm{dec,max}} - A_{\mathrm{acc}}}{A_{\mathrm{dec,max}}}$$

临界切除时间（CCT）与稳定裕度通过时域轨迹 $\delta_{eq}(t)$ 关联：给定候选 CCT $t_c$，可计算对应切除角 $\delta_c$ 和裕度 $\eta$；若 $\eta=0$ 则为临界 CCT。

## 分类与变体

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 800 520" xmlns="http://www.w3.org/2000/svg">
  <!-- Title -->
  <text x="400" y="30" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" font-weight="bold" fill="#333">图1 · EEAC方法体系架构</text>
  
  <!-- Main branches -->
  <!-- Branch 1: Static grouping -->
  <rect x="50" y="70" width="160" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="130" y="100" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1e40af">静态分群EEAC</text>
  
  <!-- Branch 2: Dynamic grouping -->
  <rect x="50" y="140" width="160" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="130" y="170" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#166534">动态分群EEAC</text>
  
  <!-- Branch 3: Hybrid TD-EEAC -->
  <rect x="50" y="210" width="160" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="130" y="240" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#92400e">时域-EEAC混合</text>
  
  <!-- Branch 4: Multi-group -->
  <rect x="50" y="280" width="160" height="50" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="130" y="310" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#5b21b6">多群扩展EEAC</text>
  
  <!-- Branch 5: SIME relation -->
  <rect x="50" y="350" width="160" height="50" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="130" y="380" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#5b21b6">与SIME的关系</text>
  
  <!-- Core OMIB box -->
  <rect x="280" y="170" width="160" height="120" rx="8" fill="#f3f4f6" stroke="#374151" stroke-width="2"/>
  <text x="360" y="200" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#1f2937">核心：OMIB等效</text>
  <line x1="210" y1="95" x2="280" y2="200" stroke="#6b7280" stroke-width="1.5" stroke-dasharray="4,2"/>
  <line x1="210" y1="165" x2="280" y2="200" stroke="#6b7280" stroke-width="1.5" stroke-dasharray="4,2"/>
  <line x1="210" y1="235" x2="280" y2="200" stroke="#6b7280" stroke-width="1.5" stroke-dasharray="4,2"/>
  <line x1="210" y1="305" x2="280" y2="200" stroke="#6b7280" stroke-width="1.5" stroke-dasharray="4,2"/>
  <line x1="210" y1="375" x2="280" y2="200" stroke="#6b7280" stroke-width="1.5" stroke-dasharray="4,2"/>
  
  <!-- Key equations box -->
  <rect x="470" y="100" width="280" height="260" rx="8" fill="#fafafa" stroke="#374151" stroke-width="1.5"/>
  <text x="610" y="130" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1f2937">关键方程</text>
  <text x="490" y="160" font-family="Arial,sans-serif" font-size="11" fill="#374151">群角定义：</text>
  <text x="490" y="178" font-family="Arial,sans-serif" font-size="10" fill="#4b5563">δC = Σ(Miδi)/ΣMi</text>
  <text x="490" y="198" font-family="Arial,sans-serif" font-size="11" fill="#374151">等效惯性：</text>
  <text x="490" y="216" font-family="Arial,sans-serif" font-size="10" fill="#4b5563">Meq = MC·MN/(MC+MN)</text>
  <text x="490" y="236" font-family="Arial,sans-serif" font-size="11" fill="#374151">面积裕度：</text>
  <text x="490" y="254" font-family="Arial,sans-serif" font-size="10" fill="#4b5563">η = (Adec−Aacc)/Adec</text>
  <text x="490" y="274" font-family="Arial,sans-serif" font-size="11" fill="#374151">稳定判据：</text>
  <text x="490" y="292" font-family="Arial,sans-serif" font-size="10" fill="#4b5563">Aacc &lt; Adec,max</text>
  <text x="490" y="312" font-family="Arial,sans-serif" font-size="11" fill="#374151">CCT关联：</text>
  <text x="490" y="330" font-family="Arial,sans-serif" font-size="10" fill="#4b5563">η(t_c) = 0 → CCT</text>
  <text x="490" y="350" font-family="Arial,sans-serif" font-size="11" fill="#374151">数值方法：</text>
  <text x="490" y="368" font-family="Arial,sans-serif" font-size="10" fill="#4b5563">二分/逐步搜索CCT</text>
  
  <!-- Output box -->
  <rect x="470" y="380" width="280" height="80" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="610" y="405" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#991b1b">输出：稳定裕度与CCT</text>
  <text x="490" y="425" font-family="Arial,sans-serif" font-size="10" fill="#7f1d1d">· 临界清除时间（仅对该故障/模型/判据有效）</text>
  <text x="490" y="443" font-family="Arial,sans-serif" font-size="10" fill="#7f1d1d">· 面积裕度η（无量纲，需指明模型和判据）</text>
  
  <!-- Arrows -->
  <path d="M360 230 L470 150" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
  <path d="M360 230 L470 420" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
  
  <!-- Legend -->
  <rect x="50" y="430" width="160" height="70" rx="6" fill="#f9fafb" stroke="#d1d5db" stroke-width="1"/>
  <text x="60" y="450" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#374151">图例</text>
  <rect x="60" y="460" width="14" height="14" rx="2" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="82" y="471" font-family="Arial,sans-serif" font-size="10" fill="#374151">静态分群</text>
  <rect x="60" y="480" width="14" height="14" rx="2" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="82" y="491" font-family="Arial,sans-serif" font-size="10" fill="#374151">动态分群</text>
  
  <!-- Arrow marker definition -->
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · EEAC方法体系架构：五类变体共享OMIB等效核心，关键方程驱动面积裕度计算</p>

### 静态分群 EEAC

基于故障后早期角速度或功角差识别临界群，适合首摆主导场景。常用识别指标包括：

$$\omega_i(t_0) > \bar{\omega} + k\sigma_\omega$$

其中 $\bar{\omega}$ 是群内平均转速，$\sigma_\omega$ 是标准差，$k$ 是阈值参数（通常取 1.5~2.0）。临界群确定后在整个仿真窗口内保持不变。

### 动态分群 EEAC

沿时域轨迹更新机群和等效参数，适合临界群不明显或机群可能变化的场景。动态分群需要：
1. 在多个时间点检测机群分离趋势
2. 根据等效功率角曲线的非线性程度调整 OMIB 参数
3. 重新计算面积裕度

动态分群的计算成本高于静态分群，但可处理多摆失稳和机群重组场景。

### 时域-EEAC 混合

先短时域仿真生成轨迹，再做 OMIB 等效和面积裕度计算。该方法利用时域仿真的准确性识别机群，同时使用 EEAC 快速评估稳定裕度。混合策略可减少 CCT 搜索的计算量（原文未报告具体加速比，数值结果需绑定具体实现）。

### 多群扩展

当不止一个机群相互分离时，需要多自由度能量或分群方法。简单二群 OMIB 可能过度压缩信息。多群扩展方法包括：
- 分层 EEAC：对多个临界群逐层等效
- 能量函数扩展：将机群间能量转化为等效位能函数
- SIME（Single Machine Equivalent）方法：将多机系统分解为多个单机-等效群耦合

### 与 SIME 的关系

EEAC 和 SIME 都使用单机等效和面积解释，但机群识别、轨迹使用方式和实现细节可能不同。SIME 由 P. Anderson 和 A. Fouad 等人提出，主要用于暂态稳定的时间响应分析；EEAC 由 Chiang 等人提出，强调拓扑识别和稳定域边界计算。二者在数学上具有对偶关系。

## 形式化表达

### OMIB 等效推导

给定多机系统微分代数方程：

$$\dot{x} = f(x, y), \qquad 0 = g(x, y)$$

其中 $x$ 是状态变量（功角、转速），$y$ 是代数变量（电压幅值、相角）。将系统划分为临界群 $C$ 和非临界群 $N$，定义惯性加权群角：

$$\delta_C = \frac{1}{M_C}\sum_{i\in C} M_i\delta_i, \quad \delta_N = \frac{1}{M_N}\sum_{j\in N} M_j\delta_j$$

对两侧分别应用转子运动方程，可得 OMIB 摇摆方程：

$$M_{eq}\ddot{\delta}_{eq} = P_{m,eq} - P_{e,eq}(\delta_{eq})$$

### 面积裕度表达式

在 $(P_{m,eq}, P_{e,eq}^{fault}, P_{e,eq}^{post})$ 已知的情况下，面积裕度为：

$$\eta = \frac{1}{A_{dec,max}}\int_{\delta_c}^{\delta_u}(P_{e,eq}^{post} - P_{m,eq})d\delta - \frac{1}{A_{dec,max}}\int_{\delta_0}^{\delta_c}(P_{m,eq} - P_{e,eq}^{fault})d\delta$$

当 $\eta > 0$ 时系统首摆稳定；$\eta = 0$ 时为临界稳定。

## 关键技术挑战

### 临界机群识别

临界机群识别错误会直接导致裕度符号和 CCT 判断错误。常用识别方法包括：
- 角速度阈值法：基于故障后初始时刻的转速偏差
- 功角差判别法：基于相对功角的时序变化趋势
- 能量函数法：基于各机的暂态能量排序

识别准确性取决于故障类型、位置和系统运行点。对于强非线性场景（如 FIDVR 故障），静态识别可能失效。

### 等效功率曲线构建

等效功率角曲线 $P_{e,eq}(\delta_{eq})$ 若不是单值函数，面积解释会变弱。当 $P_{e,eq}$ 出现多值（如含电力电子控制的快速变化），需要采用分段线性化或查表方法。

### 首摆 vs 多摆稳定

首摆稳定不等于多摆稳定；后续控制器、调速器和保护动作可能改变结论。EEAC 的面积判据通常只保证首摆稳定裕度，多摆稳定性需要额外的时域仿真验证。

### 电力电子接口精度

含强电力电子控制、限流和不平衡故障时，$P_{e,eq}$ 可能依赖状态切换而非仅依赖 $\delta_{eq}$。此时等效功率曲线不再是光滑函数，面积积分的物理含义需要重新审视。

## 量化性能边界

EEAC 作为直接法，其计算效率远高于时域仿真（时域法需要对每个候选 CCT 重复仿真）。但 EEAC 的准确性依赖于机群识别的质量。

在理想条件下（故障后首摆主导、静态分群、单机无穷大等效成立），EEAC 可在数百毫秒内完成单次 CCT 评估，相比时域仿真（通常需要数秒到数十秒）有显著加速。**具体加速比取决于实现平台、测试系统和算法优化水平，原始文献未报告可核验的通用数值。**

稳定性分析方法的比较如下：

| 方法 | 计算效率 | 模型精度 | 机群依赖 | 适用场景 |
|------|---------|---------|---------|---------|
| EEAC | 高（直接法） | 依赖机群识别 | 关键 | 首摆稳定、快速筛查 |
| 时域仿真 | 中低 | 高 | 低 | 多摆、非线性控制 |
| 能量函数 | 中 | 中 | 中 | 能量裕度估计 |
| 特征值分析 | 低 | 线性化 | 低 | 小信号稳定性 |

任何"速度提升""误差小于某值"或"实时应用"说法都必须绑定来源、系统规模、硬件和判据。

## 适用边界与选择指南

### 适用条件

- 首摆主导的暂态功角稳定分析
- 需要快速筛查大量故障场景的筛选分析
- 作为时域仿真的后处理工具提供机制解释
- 作为混合仿真结果的解释框架

### 失效边界

- 临界机群识别错误会直接导致裕度符号和 CCT 判断错误
- 首摆稳定不等于多摆稳定；后续控制器、调速器和保护动作可能改变结论
- 等效功率角曲线若不是单值函数，面积解释会变弱
- 含强电力电子控制、限流和不平衡故障时，$P_{e,eq}$ 可能依赖状态切换而非仅依赖 $\delta_{eq}$
- 任何"速度提升""误差小于某值"或"实时应用"说法都必须绑定来源、系统规模、硬件和判据

### 选择指南

当分析目标是：
- 快速评估首摆稳定性边界 → 选择 EEAC（静态或动态分群）
- 多摆失稳分析 → 需要时域仿真辅助
- 含电力电子换流器的暂态分析 → 需要 EMT 或混合仿真验证 EEAC 结论
- 电压和功角耦合失稳 → 不适合纯 EEAC，需要综合分析

## 相关页面

- [[equal-area-criterion]] 是 EEAC 的单机判据基础
- [[energy-function]] 提供更一般的能量裕度背景
- [[swing-equation]] 给出机组和等效机群的运动方程
- [[transient-stability-analysis]] 组织故障、判据、CCT 和验证流程
- [[time-domain-simulation]] 用于生成或复核机群轨迹
- [[transient-stability]] 定义本方法服务的稳定性问题
- [[electromechanical-transient]] 给出 EEAC 所在的机电暂态时间尺度，不应与 EMT 高频暂态混淆