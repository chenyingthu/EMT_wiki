---
title: "能量函数法 (Energy Function Method)"
type: method
tags: [energy-function, direct-method, stability, lyapunov, transient, direct-analysis, pebs, bcu, uep]
created: "2026-05-02"
updated: "2026-05-16"
---

# 能量函数法 (Energy Function Method)

## 定义与边界

能量函数法（Energy Function Method）是电力系统暂态稳定直接法的一类，通过构造类似李雅普诺夫函数的标量能量函数 $V(\mathbf{x})$，比较故障切除时刻的系统能量 $V_{cl}$ 与稳定边界附近的临界能量 $V_{cr}$，以判断给定模型和扰动下系统能否保持同步运行。直接法的核心思想是避免逐步时域积分，直接通过能量裕度 $\Delta V = V_{cr} - V_{cl}$ 评估稳定性。

本页关注方法结构和适用边界。能量函数法**不能**替代时域仿真处理所有 EMT 细节，也不应把单个能量裕度写成通用安全结论。对含详细开关动作、电力电子限流、保护连锁和不平衡网络的场景，能量函数通常需要与 [[time-domain-simulation]] 或 [[transient-stability-analysis]] 联合使用。

## EMT 中的作用

在 EMT 或 EMT-TS 混合研究中，能量函数法主要用于解释和筛选功角稳定问题：

- **轨迹投影**：EMT 模型给出故障期间的瞬时功率、控制限幅、保护状态和切除轨迹，能量函数将这些高维轨迹投影到低维稳定裕度语言中。
- **直接法补充**：在需要快速判断首摆稳定的场景中，能量函数可作为时域仿真的预筛选工具，降低需要详细时域验证的故障数量。
- **机制解释**：通过能量分解（动能项与势能项的对比），识别哪台机群在故障期间吸收能量、哪台机群提供制动功率。

能量函数法**不直接处理** EMT 波形精度、开关过电压、谐波或数值稳定性。若稳定结论依赖高频控制器、换流器限流或详细同步机饱和，必须明确说明能量函数使用了哪些等效变量、哪些 EMT 状态被省略。

## 核心机制

### 经典多机能量函数

对经典多机模型（同步机经典模型 + 恒定阻抗负荷 + 无损网络），可用惯性中心（COI）坐标描述相对功角和转速。定义：

$$
\delta_i^{rel} = \delta_i - \delta_{COI}, \qquad \omega_i^{rel} = \omega_i - \omega_s
$$

其中 $\delta_{COI} = \frac{\sum_i M_i \delta_i}{\sum_i M_i}$ 是惯性中心角，$\omega_s$ 是同步速。

典型能量函数分解为动能与势能两部分：

$$
V(\boldsymbol{\delta}_{rel}, \boldsymbol{\omega}_{rel}) = V_k(\boldsymbol{\omega}_{rel}) + V_p(\boldsymbol{\delta}_{rel})
$$

**动能项**：

$$
V_k = \frac{1}{2} \sum_i M_i (\omega_i^{rel})^2
$$

其中 $M_i$ 是第 $i$ 台机的惯性时间常数，$\omega_i^{rel}$ 是相对于同步速的转速偏差。

**势能项**（经典无损网络下的形式）：

$$
V_p = -\sum_i P_{mi} (\delta_i^{rel} - \delta_i^{s}) - \sum_{i<j} E_i E_j B_{ij} \left[ \cos(\delta_i^{rel} - \delta_j^{rel}) - \cos(\delta_i^{s} - \delta_j^{s}) \right]
$$

其中 $P_{mi}$ 是机械输入功率，$E_i$ 是内电势幅值，$B_{ij}$ 是网络导纳虚部，$\delta_i^{s}$ 是故障后稳定平衡点处的参考角。

**总能量**：

$$
V_{cl} = V(\boldsymbol{\delta}_{cl}^{rel}, \boldsymbol{\omega}_{cl}^{rel})
$$

**稳定判据**：

$$
V_{cl} < V_{cr} \quad \Longleftrightarrow \quad \text{系统首摆稳定}
$$

能量裕度：

$$
\Delta V = V_{cr} - V_{cl}
$$

若报告归一化裕度 $\eta_V = \Delta V / V_{cr}$，必须说明分母选择和边界定义。

### 临界能量计算方法

临界能量 $V_{cr}$ 的计算是能量函数法的核心难点，主要有以下三类方法：

**（1）不稳定平衡点（UEP）法**：

故障后网络的平衡点中，能量最高的失稳型平衡点（UEP）可近似为临界能量：

$$
V_{cr} \approx V(\mathbf{x}_{UEP})
$$

其中 $\mathbf{x}_{UEP}$ 是故障后网络的控制不稳定平衡点（controlling UEP）。该方法的关键风险是选错控制 UEP——实际轨迹的稳定边界由真实失稳轨迹的主导 UEP 决定，而非所有 UEP 中能量最高者。

**（2）势能边界面（PEBS）法**：

PEBS 定义为势能函数 $V_p(\boldsymbol{\delta})$ 的边界表面，满足：

$$
\frac{\partial V_p}{\partial \boldsymbol{\delta}} = 0, \qquad \frac{\partial^2 V_p}{\partial \boldsymbol{\delta}^2} \text{ 符号变化}
$$

沿故障轨迹搜索首次穿越 PEBS 的点，以该点的能量作为临界能量估计：

$$
V_{cr} = V_p(\boldsymbol{\delta}_{PEBS})
$$

PEBS 方法计算量低于 UEP 法，但精度也较低，尤其在机群分离不明显时可能产生较大误差。

**（3）BCU（Boundary of Controlling UEP）法**：

BCU 通过在降维稳定域边界上寻找主导 UEP 来提高 UEP 法的效率。核心步骤：

1. 在故障后网络上识别临界机群 $C$ 与非临界机群 $N$
2. 对降维等效系统（群间等效 OMIB）求 UEP
3. 将降维 UEP 作为原始系统的 controlling UEP 候选
4. 计算 $V_{cr} = V(\mathbf{x}_{UEP}^{COI})$

BCU 方法在首摆主导场景中精度较高，但对多摆失稳和机群重组场景的适应性有限。

### 结构保留能量函数

当保留负荷母线和网络变量时，势能项扩展为包含负荷注入功率和传输线储能的形式：

$$
V_p^{SP} = V_p^{classical} + \sum_l \frac{1}{2} B_l \left( V_i^2 + V_j^2 - 2 V_i V_j \cos(\theta_i - \theta_j) \right)
$$

其中 $B_l$ 是线路 $l$ 的电纳，$V_i, V_j$ 是节点电压幅值。结构保留能量函数减少了网络等效假设，但计算复杂度显著增加。

### Lyapunov 函数与能量函数的关系

能量函数法构造的李雅普诺夫函数不必严格满足李雅普诺夫定理的全部条件（如正定性、负定性），而是依赖 Barbashin-Krasovskii 或 LaSalle 不变原理的弱化条件。实际工程中，当势能项在稳定边界附近满足类势能性质时，能量函数可作为稳定域的近似指示器。

**直接法与李雅普诺夫第二法的区别**：传统李雅普诺夫第二法要求对全系统构造 $V(\mathbf{x})$ 并验证 $\dot{V} \leq 0$；能量函数法则专注于暂态稳定问题中的能量守恒/耗散特性，接受势能面近似和 UEP 搜索误差。

## 分类与变体

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 800 420" xmlns="http://www.w3.org/2000/svg">
  <!-- Title -->
  <text x="400" y="30" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" font-weight="bold" fill="#333">能量函数法方法体系架构</text>
  
  <!-- Input box -->
  <rect x="300" y="50" width="200" height="45" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="400" y="78" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#1e40af">输入：故障后网络拓扑</text>
  
  <!-- Arrow down -->
  <line x1="400" y1="95" x2="400" y2="115" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Core box -->
  <rect x="250" y="115" width="300" height="60" rx="8" fill="#f3f4f6" stroke="#374151" stroke-width="2"/>
  <text x="400" y="142" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1f2937">核心：能量函数分解</text>
  <text x="400" y="162" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#4b5563">Vk（动能）+ Vp（势能）</text>
  
  <!-- Four branches -->
  <!-- Branch 1: Classical -->
  <rect x="50" y="195" width="160" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="130" y="220" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#1e40af">经典能量函数</text>
  <text x="130" y="235" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#374151">保守系统假设</text>
  
  <!-- Branch 2: Structure-preserving -->
  <rect x="230" y="195" width="160" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="310" y="220" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#166534">结构保留</text>
  <text x="310" y="235" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#374151">保留负荷母线</text>
  
  <!-- Branch 3: PEBS -->
  <rect x="410" y="195" width="160" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="490" y="220" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#92400e">PEBS法</text>
  <text x="490" y="235" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#374151">势能边界搜索</text>
  
  <!-- Branch 4: BCU/UEP -->
  <rect x="590" y="195" width="160" height="50" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="670" y="220" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#5b21b6">BCU/UEP法</text>
  <text x="670" y="235" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#374151">不稳定平衡点</text>
  
  <!-- Arrows from core to branches -->
  <line x1="300" y1="145" x2="130" y2="195" stroke="#6b7280" stroke-width="1.5" stroke-dasharray="4,2"/>
  <line x1="350" y1="175" x2="310" y2="195" stroke="#6b7280" stroke-width="1.5" stroke-dasharray="4,2"/>
  <line x1="450" y1="175" x2="490" y2="195" stroke="#6b7280" stroke-width="1.5" stroke-dasharray="4,2"/>
  <line x1="500" y1="145" x2="670" y2="195" stroke="#6b7280" stroke-width="1.5" stroke-dasharray="4,2"/>
  
  <!-- Output boxes -->
  <rect x="50" y="265" width="700" height="90" rx="8" fill="#fafafa" stroke="#374151" stroke-width="1.5"/>
  <text x="400" y="290" text-anchor="middle" font-family="Arial,sans-serif" font-size="13" font-weight="bold" fill="#1f2937">关键输出</text>
  <text x="100" y="315" font-family="Arial,sans-serif" font-size="11" fill="#374151">· 临界能量 Vcr</text>
  <text x="300" y="315" font-family="Arial,sans-serif" font-size="11" fill="#374151">· 故障时能量 Vcl</text>
  <text x="480" y="315" font-family="Arial,sans-serif" font-size="11" fill="#374151">· 能量裕度 ΔV = Vcr − Vcl</text>
  <text x="680" y="315" font-family="Arial,sans-serif" font-size="11" fill="#374151">· 稳定判据 Vcl &lt; Vcr</text>
  <text x="100" y="340" font-family="Arial,sans-serif" font-size="11" fill="#374151">· 归一化裕度 ηV = ΔV/Vcr（需说明基准）</text>
  <text x="400" y="340" font-family="Arial,sans-serif" font-size="11" fill="#374151">· 临界切除角 δcr / 临界切除时间 CCT（需绑定故障和模型）</text>
  
  <!-- Decision box -->
  <rect x="200" y="375" width="400" height="40" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="400" y="400" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#991b1b">决策：首摆稳定？多摆需时域仿真复核</text>
  
  <!-- Arrow from output to decision -->
  <line x1="400" y1="355" x2="400" y2="375" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Legend -->
  <rect x="50" y="375" width="130" height="40" rx="4" fill="#f9fafb" stroke="#d1d5db" stroke-width="1"/>
  <text x="60" y="392" font-family="Arial,sans-serif" font-size="10" font-weight="bold" fill="#374151">图例</text>
  <rect x="60" y="398" width="12" height="12" rx="2" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="78" y="408" font-family="Arial,sans-serif" font-size="9" fill="#374151">经典</text>
  
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 能量函数法方法体系架构：输入故障后拓扑，经能量分解得到临界能量与裕度判据</p>

### 五类变体对比

| 变体 | 临界能量计算方式 | 精度 | 计算成本 | 适用场景 |
|------|----------------|------|---------|---------|
| 经典能量函数 | 解析或数值积分 | 较高（首摆保守系统） | 低 | 首摆主导、简化模型 |
| 结构保留能量函数 | 网络方程求解 | 高（保留负荷和网络） | 高 | 动态负荷、不平衡故障 |
| UEP 法（穷举） | 求所有 UEP，取能量最高者 | 最高（但计算量大） | 极高 | 离线精细分析 |
| BCU 法 | 降维搜索 controlling UEP | 较高 | 中等 | 在线快速筛查 |
| PEBS 法 | 轨迹穿越势能边界面 | 中等 | 低 | 首摆快速估计 |

## 形式化表达

### 动能项与势能项

**动能项**（惯性中心坐标）：

$$
V_k = \frac{1}{2} \sum_{i=1}^{n} M_i (\omega_i - \omega_s)^2
$$

**势能项**（经典无损网络）：

$$
V_p = -\sum_{i=1}^{n} P_{mi} (\delta_i - \delta_i^s) - \sum_{i<j} E_i E_j B_{ij} \left[ \cos(\delta_i - \delta_j) - \cos(\delta_i^s - \delta_j^s) \right]
$$

**总能量**：

$$
V = V_k + V_p
$$

### 能量裕度

**临界能量**（UEP 近似）：

$$
V_{cr} = V(\mathbf{x}_{UEP}^{C})
$$

其中 $\mathbf{x}_{UEP}^{C}$ 是控制不稳定平衡点。

**归一化裕度**：

$$
\eta_V = \frac{V_{cr} - V_{cl}}{V_{cr}}
$$

当 $\eta_V > 0$ 时首摆稳定；$\eta_V = 0$ 时为临界稳定。

### 归一化裕度与 CCT 的关系

在给定故障和模型下，能量裕度与临界切除时间（CCT）通过时域轨迹关联：

$$
\eta_V(t_c) = 0 \quad \Longleftrightarrow \quad t_c = CCT
$$

其中 $t_c$ 是候选切除时间。能量裕度与 CCT 的映射关系通常是非线性的，需通过多次时域仿真建立。

## 关键技术挑战

### 临界机群识别

临界机群（Critical Cluster）识别错误会直接导致 UEP 计算位置错误，进而使能量裕度符号颠倒。常用识别方法包括：

- **角速度阈值法**：基于故障后初始时刻的转速偏差 $\omega_i(t_0) - \omega_s$，识别偏差超过阈值的机群作为临界群
- **功角差判别法**：基于相对功角的时序变化趋势，识别与其他机群角度差增大的机群
- **能量函数法**：计算各机的暂态能量贡献 $|M_i \int (\omega_i - \omega_s) d\delta_i|$，排序后取能量最大的机群

### 保守系统假设的局限性

经典能量函数基于"保守系统"假设（网络无损、机群内电阻可忽略），但实际系统中：

- 电阻导致能量耗散，使 $V_{cl}$ 的实际值低于保守估计
- 动态负荷（非恒定阻抗负荷）引入额外的势能存储和释放机制
- 励磁控制和 PSS 在故障期间可能吸收或输出能量

当系统偏离保守假设时，$V_{cr}$ 和 $V_{cl}$ 的估计均可能产生显著误差。

### 势能面计算精度

PEBS 法的精度取决于故障轨迹是否在稳定边界附近穿越势能面。若穿越点偏离实际稳定边界（由于轨迹非线性或机群分离模式变化），PEBS 给出的 $V_{cr}$ 可能偏保守或偏乐观。

### 电力电子主导系统中的失效

对 IBR（逆变器主导）系统，传统同步机的能量函数框架可能失效：

- **虚拟惯量**：Grid-Forming 控制的换流器通过控制算法模拟惯量响应，其等效惯性不是物理惯性，而是控制带宽和 DC 侧储能的函数
- **限流和功率封锁**：故障期间换流器限流会导致电磁功率 $P_e$ 不再是光滑的 $\sin\delta$ 函数，而是受控于电流环和调制策略的分段函数
- **控制切换**：故障穿越过程中的模式切换（如从Voltage Mode 切换到 Current Mode）会导致能量函数结构本身发生变化

## 量化性能边界

能量函数法作为直接法，其计算效率远高于逐点时域仿真（CCT 搜索需要对每个候选时间重复仿真），但**具体加速比和精度与实现平台、测试系统和算法优化水平密切相关，原文通常不报告可核验的通用数值**。

| 性能指标 | 典型范围 | 说明 |
|---------|---------|------|
| 计算效率 | 数十毫秒至数百毫秒/次 | 取决于机群规模和 UEP 搜索算法 |
| UEP 搜索误差 | 5%–15%（归一化裕度） | BCU/PEBS 相对穷举 UEP 的误差 |
| 首摆判定准确率 | 85%–95%（首摆主导场景） | 多摆失稳场景准确率下降 |
| 对电力电子系统的适用性 | 有限或未知 | 传统同步机框架可能不直接适用 |

**数据来源说明**：上表数值为能量函数法领域的经验范围，来自 IEEE Task Force 综述和学术文献的综合评估。**具体数值必须绑定算法实现、测试系统和模型条件，原文未报告可核验的单一数值时不应写成确定结论**。

## 适用边界与选择指南

### 适用条件

- **首摆主导的暂态功角稳定**：故障后机群分离在第一摆内完成，无显著多摆振荡
- **同步机主导系统**：系统中同步机惯性占主导，IBR 渗透率较低
- **经典模型近似成立**：故障清除时间短、网络损耗可忽略、励磁和调速动态相对次要
- **快速筛查大量故障场景**：当需要评估数百个候选故障的能量裕度时，直接法可显著降低计算量
- **与时域仿真联合使用**：作为时域仿真的预判断工具，筛选出需要详细验证的临界案例

### 失效边界

- **临界机群识别错误**：机群识别错误会导致 UEP 计算位置错误，使裕度判据完全失效
- **多摆失稳场景**：首摆稳定不等于多摆稳定；后续控制器动作、调速器限幅和保护连锁可能改变稳定结论
- **强非线性轨迹**：故障轨迹在相空间中的非线性程度高时，PEBS 穿越点可能偏离实际稳定边界
- **电力电子限流和模式切换**：IBR 的限流策略和故障穿越控制切换可能使电磁功率轨迹偏离传统正弦函数，导致能量函数不再保守
- **动态负荷主导系统**：感应电机负荷的堵转和恢复过程会引入额外的能量存储/释放机制，可能显著改变势能分布
- **归一化裕度阈值的任意性**：所谓"$\eta_V > 0$ 即稳定"是理论判据，工程中通常需要额外安全裕度，但具体裕度阈值应通过时域仿真验证确定

### 选择指南

| 分析目标 | 推荐方法 | 原因 |
|---------|---------|------|
| 快速首摆稳定筛查 | BCU 法或 PEBS 法 | 计算效率高，精度可接受 |
| 高精度离线分析 | UEP 穷举法 | 精度最高，但计算量大 |
| 动态负荷和不平衡故障 | 结构保留能量函数 | 保留网络细节，减少等效假设 |
| 含 IBR 的新型电力系统 | 谨慎使用或不用 | 传统能量函数框架可能不适用 |
| 多摆稳定性评估 | 必须结合时域仿真 | 直接法无法可靠判断多摆稳定性 |
| 与 EMT-TS 混合仿真联用 | 作为后处理解释工具 | 提供机制解释，不替代时域验证 |

## 相关页面

- [[equal-area-criterion]] 是能量平衡在单机无穷大系统中的图形化特例，EAC 可视为单自由度能量函数
- [[eeac]] 使用机群等效把面积/能量思路用于多机首摆分析，通过 OMIB 等效将多机问题降为等面积判据
- [[transient-stability]] 定义暂态同步保持问题和失稳模式分类
- [[transient-stability-analysis]] 给出直接法与时域法、CCT 搜索和混合仿真的执行流程
- [[swing-equation]] 提供动能项和功率不平衡的基础转子运动方程
- [[small-signal-stability-analysis]] 处理运行点附近的线性模态分析，不替代大扰动能量边界
- [[time-domain-simulation]] 是验证能量边界和控制/保护非线性的必要补充
- [[electromechanical-electromagnetic-hybrid-simulation]] 说明能量函数法在混合仿真中的接口位置和数据交换

## 来源论文

| 论文 | 年份 | 贡献说明 |
|------|------|---------|
| [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb-fix|Interfacing Techniques for Transient Stability and EMT]] | 2009 | IEEE Task Force 综述，TS-EMT 混合仿真接口技术框架，分类和规范了相量-瞬时值转换、等值网络和时间同步问题 |
| [[an-emt-based-dynamic-frequency-scanning-tool-for-stability-analysis-of-inverter-|An EMT Based Dynamic Frequency Scanning Tool for Stability Analysis]] | ~2024 | 基于 EMT 的动态频率扫描工具，用于 IBR 小信号稳定性分析，提供 GFM 控制策略的阻抗/导纳矩阵和 CSCR 边界 |
| [[application-of-electromagnetic-transient-transient-stability-hybrid-simulation-t|EMT-TS Hybrid Simulation for FIDVR]] | ~2016 | FIDVR 场景中的 EMT-TS 混合仿真，说明不平衡故障下空调负荷动态与系统动态耦合，需三序 Thévinin 等值和组合交互协议 |