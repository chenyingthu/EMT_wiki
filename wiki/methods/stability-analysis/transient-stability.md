---
title: "暂态稳定 (Transient Stability)"
type: method
tags: [transient-stability, rotor-angle, swing, first-swing, stability, cct, equal-area, energy-function, direct-method]
created: "2026-05-02"
updated: "2026-05-16"
---

# 暂态稳定 (Transient Stability)

## 定义与边界

暂态稳定是电力系统遭受大扰动后仍能保持同步运行并进入可接受动态状态的能力。典型扰动包括短路、线路跳闸、发电机或负荷切除、直流闭锁、换流器控制切换和保护动作。它关注的是扰动后数秒至数十秒时间尺度内的非线性大信号轨迹，而不是平衡点附近的微小扰动衰减。

与[[small-signal-stability]]的线性化局部模态分析不同，暂态稳定涉及大幅度的功角摆动，可能进入饱和、控制限幅和离散保护动作等非线性区域。本页定义稳定性概念和物理机制，不替代[[transient-stability-analysis]]的计算流程。若讨论具体转子方程，应链接[[swing-equation]]；若讨论励磁或PSS的控制结构，应链接[[excitation-system]]和[[power-system-stabilizer]]。

## EMT中的作用

EMT仿真可用于检验暂态稳定结论，尤其当故障、换流器控制、保护限幅、单相负荷或不平衡电压会改变电磁功率和电磁转矩时。机电暂态仿真通常能覆盖大系统同步动态；EMT或EMT-TS混合仿真则用于验证局部高频/不平衡/电力电子细节是否改变低频稳定判断。

暂态稳定在EMT Wiki中的角色是**稳定性目标**，而不是仿真域本身。一个EMT波形案例只有在明确扰动、模型、判据和观察时窗后，才能支持"稳定"或"失稳"的判断。

## 核心机制

### 单机无穷大系统的摆动方程

同步稳定的基本机制是扰动期间机械输入和电磁输出不平衡导致转子加速或减速。对第$i$台同步机，转子运动方程为：

$$\dot{\delta}_i = \omega_i - \omega_s \tag{1}$$

$$M_i \dot{\omega}_i = P_{m,i} - P_{e,i} - D_i (\omega_i - \omega_s) \tag{2}$$

其中$\delta_i$为转子角，$\omega_i$为角速度，$\omega_s$为同步速（$2\pi \times 50$或$60$ rad/s），$M_i$为惯性时间常数，$P_{m,i}$为机械输入功率，$P_{e,i}$为电磁输出功率，$D_i$为阻尼系数。

故障期间若电磁功率$P_e$降低而机械功率$P_m$尚未变化，转子获得加速能量。故障清除后，若系统能提供足够减速能力并使相对角速度衰减，则同步可能保持；若相对角度持续发散或发生滑极，则暂态失稳。

### 功率-功角特性

在单机无穷大近似中，功率-功角关系写成：

$$P_e = P_{\max} \sin \delta \tag{3}$$

其中$P_{\max} = \frac{E V}{X}$，$E$为发电机内电势，$V$为无穷大母线电压，$X$为转移电抗。该表达只适用于单机无穷大母线下的经典模型。多机系统、励磁动态、饱和、负荷恢复和电力电子控制会改变$P_e$的轨迹。

### 等面积定则（Equal Area Criterion）

对于单机无穷大系统，可用等面积定则直观判断首摆稳定性。定义加速面积：

$$A_{acc} = \int_{\delta_0}^{\delta_{cl}} (P_m - P_{\max} \sin \delta) \, d\delta \tag{4}$$

其中$\delta_0$为故障前功角，$\delta_{cl}$为故障清除时刻功角。减速面积：

$$A_{dec} = \int_{\delta_{cl}}^{\delta_{max}} (P_{\max} \sin \delta - P_m) \, d\delta \tag{5}$$

其中$\delta_{max}$为最大功角。若$A_{acc} \leq A_{dec}$，系统首摆稳定；若$A_{acc} > A_{dec}$，则首摆失稳。

等面积定则只能用于判断**单机无穷大系统**的首摆稳定性，不能推广到多机系统和非机电商用负荷动态。

### 能量函数法（直接法）

多机系统的暂态稳定可通过能量函数法（直接法）判断。系统能量函数为：

$$V = \sum_{i=1}^{n} \frac{1}{2} M_i \omega_i^2 - \sum_{i=1}^{n} P_{m,i} (\delta_i - \delta_{s,i}) + \sum_{i<j} \left[ \frac{E_i E_j}{X_{ij}} (\cos \delta_{ij} - \cos \delta_{s,ij}) \right] \tag{6}$$

其中第一项为动能，第二项为势能中的机械功率项，第三项为势能中的电磁功率项，$\delta_s$为稳定平衡点（SEP）对应的功角。

临界能量$V_{cr}$可通过不稳定平衡点（UEP）计算：

$$V_{cr} = V(\mathbf{x}_{UEP}) \tag{7}$$

若扰动后系统能量$V < V_{cr}$，则系统暂态稳定；若$V > V_{cr}$，则失稳。能量函数法的关键是构造正确的能量函数和识别正确的UEP。

### CCT与临界切除角

临界切除时间（CCT）是系统在给定故障和模型下保持稳定的最长故障持续时间。对应于等面积定则中$A_{acc} = A_{dec}$的条件。单机系统中，临界切除角$\delta_{cr}$满足：

$$\cos \delta_{cr} = \frac{P_m (\delta_{cr} - \delta_0) + P_{\max} \cos \delta_0}{P_{\max}} \tag{8}$$

CCT是场景指标，不是设备固有常数；运行点、故障阻抗、切除拓扑、控制器和判据变化都会改变CCT。

## 稳定现象与类型

| 现象 | 含义 | 需要关注的证据 |
|------|------|----------------|
| 首摆稳定 | 第一摆期间未失去同步 | 故障清除角、最大相对功角、减速趋势 |
| 多摆稳定 | 后续摆动逐步衰减 | 阻尼、励磁/PSS、负荷恢复和控制限幅 |
| 非周期失步 | 严重故障后角度持续增大 | 临界机群、保护动作、切除时间 |
| 振荡失步 | 多摆后振幅增长并滑极 | 负阻尼、控制相位、弱联络线 |
| 电压-功角耦合失稳 | 电压恢复失败降低电磁功率并诱发角失稳 | 动态负荷、励磁限制、无功支撑 |

这些类型不是互斥分类。实际系统中，短路清除、励磁限制、负荷堵转、换流器限流和保护动作可能共同决定轨迹。

## 四种分析路径

暂态稳定分析有四种互补路径，各有其适用场景和局限性：

### 路径A：时域仿真（数值积分）

通过数值积分求解转子运动方程（式(1)(2)）和机电网络代数方程，得到完整的功角-时间曲线。优点是能捕捉非线性效应和控制器限幅，缺点是计算量大且不直接给出稳定裕度。工具包括PSCAD/EMTDC、DIgSILENT、MATPOWER和ADPSS。

### 路径B：能量函数法（直接法）

基于Lyapunov函数构造系统能量函数，通过比较扰动后能量与临界能量判断稳定性。优点是可快速估计稳定裕度，缺点是能量函数构造困难且保守性较高。代表方法包括BCU（Boundary of Unstable Equilibrium Point）、PEBS（Potential Energy Boundary Surface）和UEP（Unstable Equilibrium Point）法。

### 路径C：扩展等面积定则（EEAC）

将多机系统等值为单机无穷大系统，再应用等面积定则。通过同调聚类识别临界机群，将系统分为临界机群$S$和其余机群$R$，构造等效单机系统的参数：

$$M_{eq} = \sum_{i \in S} M_i, \quad P_{m,eq} = \sum_{i \in S} P_{m,i} - \sum_{i \in R} P_{m,i} \tag{9}$$

$$P_{e,eq} = \sum_{i \in S, j \in S} \frac{E_i E_j}{X_{ij}} \sin \delta_{ij} - \sum_{i \in S, j \in R} \frac{E_i E_j}{X_{ij}} \sin \delta_{ij} \tag{10}$$

### 路径D：混合EMT-TS仿真验证

当机电模型无法覆盖电力电子细节时，通过EMT-TS混合仿真验证。[[electromechanical-electromagnetic-hybrid-simulation]]用于内部含HVDC、FACTS、IBR的系统的稳定判断。

## 关键影响因素

- **故障类型、位置、持续时间和清除后拓扑**：三相短路最严重，单相接地故障次之
- **运行点的传输水平、电气距离和同步机惯量**：重载且电气距离远时更易失稳
- **同步机模型层级、饱和和励磁/调速限制**：饱和Park模型（见[[saturation-in-transient-and-stability-phenomena-for-cylindrical-13&14]]）在甩负荷时与线性模型偏差显著
- **负荷电压特性、感应电机比例和恢复过程**：FIDVR现象（[[application-of-electromagnetic-transient-transient-stability-hybrid-simulation-t]]）表明单相电机堵转可诱发电压-功角耦合失稳
- **HVDC、FACTS、IBR、PSS等控制器的限幅和模式切换**：限流控制在故障期间改变电磁功率轨迹
- **保护、重合闸、切机切负荷等离散动作**：保护动作时机影响系统能否保持同步

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 400" xmlns="http://www.w3.org/2000/svg">
  <!-- Title -->
  <text x="450" y="25" text-anchor="middle" font-size="14" font-weight="bold" fill="#1a1a2e" font-family="Times New Roman">图1 · 暂态稳定分析的四条路径与选择决策</text>
  
  <!-- Path A: 时域仿真 -->
  <rect x="30" y="50" width="180" height="80" rx="4" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="120" y="75" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e40af" font-family="Times New Roman">路径A：时域仿真</text>
  <text x="120" y="95" text-anchor="middle" font-size="10" fill="#374151" font-family="Times New Roman">数值积分摆动方程</text>
  <text x="120" y="112" text-anchor="middle" font-size="9" fill="#6b7280" font-family="Times New Roman">PSCAD / ADPSS / MATPOWER</text>
  
  <!-- Path B: 能量函数 -->
  <rect x="240" y="50" width="180" height="80" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="330" y="75" text-anchor="middle" font-size="11" font-weight="bold" fill="#166534" font-family="Times New Roman">路径B：能量函数法</text>
  <text x="330" y="95" text-anchor="middle" font-size="10" fill="#374151" font-family="Times New Roman">Lyapunov函数构造</text>
  <text x="330" y="112" text-anchor="middle" font-size="9" fill="#6b7280" font-family="Times New Roman">BCU / PEBS / UEP</text>
  
  <!-- Path C: EEAC -->
  <rect x="450" y="50" width="180" height="80" rx="4" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="540" y="75" text-anchor="middle" font-size="11" font-weight="bold" fill="#92400e" font-family="Times New Roman">路径C：EEAC扩展等面积</text>
  <text x="540" y="95" text-anchor="middle" font-size="10" fill="#374151" font-family="Times New Roman">同调等值单机系统</text>
  <text x="540" y="112" text-anchor="middle" font-size="9" fill="#6b7280" font-family="Times New Roman">临界机群S与其余R</text>
  
  <!-- Path D: 混合仿真 -->
  <rect x="660" y="50" width="180" height="80" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="750" y="75" text-anchor="middle" font-size="11" font-weight="bold" fill="#5b21b6" font-family="Times New Roman">路径D：混合EMT-TS</text>
  <text x="750" y="95" text-anchor="middle" font-size="10" fill="#374151" font-family="Times New Roman">电力电子细节验证</text>
  <text x="750" y="112" text-anchor="middle" font-size="9" fill="#6b7280" font-family="Times New Roman">EMT-TS接口联合仿真</text>
  
  <!-- Decision diamond -->
  <polygon points="450,180 540,230 450,280 360,230" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="450" y="225" text-anchor="middle" font-size="10" font-weight="bold" fill="#991b1b" font-family="Times New Roman">选择判据</text>
  <text x="450" y="240" text-anchor="middle" font-size="9" fill="#b91c1c" font-family="Times New Roman">系统规模/精度需求</text>
  
  <!-- Arrows from paths to diamond -->
  <line x1="120" y1="130" x2="120" y2="175" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="330" y1="130" x2="330" y2="175" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="540" y1="130" x2="540" y2="175" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="750" y1="130" x2="750" y2="175" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Legend -->
  <rect x="30" y="320" width="840" height="55" rx="4" fill="#f9fafb" stroke="#e5e7eb" stroke-width="1"/>
  <text x="50" y="340" font-size="10" font-weight="bold" fill="#374151" font-family="Times New Roman">适用场景：</text>
  <circle cx="65" cy="358" r="5" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="80" y="362" font-size="9" fill="#374151" font-family="Times New Roman">时域仿真：多机系统详细轨迹、控制限幅、非线性效应</text>
  <circle cx="420" cy="358" r="5" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="435" y="362" font-size="9" fill="#374151" font-family="Times New Roman">能量函数：快速稳定裕度估计（保守）</text>
  <text x="50" y="362" font-size="9" fill="#6b7280" font-family="Times New Roman">注：稳定裕度 = (</text>
  
  <!-- Output boxes -->
  <rect x="30" y="290" width="180" height="30" rx="3" fill="#f0f9ff" stroke="#94a3b8" stroke-width="1"/>
  <text x="120" y="308" text-anchor="middle" font-size="9" fill="#475569" font-family="Times New Roman">功角-时间曲线</text>
  
  <rect x="240" y="290" width="180" height="30" rx="3" fill="#f0f9ff" stroke="#94a3b8" stroke-width="1"/>
  <text x="330" y="308" text-anchor="middle" font-size="9" fill="#475569" font-family="Times New Roman">稳定裕度（能量差值）</text>
  
  <rect x="450" y="290" width="180" height="30" rx="3" fill="#f0f9ff" stroke="#94a3b8" stroke-width="1"/>
  <text x="540" y="308" text-anchor="middle" font-size="9" fill="#475569" font-family="Times New Roman">CCT/临界切除角</text>
  
  <rect x="660" y="290" width="180" height="30" rx="3" fill="#f0f9ff" stroke="#94a3b8" stroke-width="1"/>
  <text x="750" y="308" text-anchor="middle" font-size="9" fill="#475569" font-family="Times New Roman">电力电子影响评估</text>
  
  <!-- Arrow from diamond down -->
  <line x1="450" y1="280" x2="450" y2="287" stroke="#333" stroke-width="1.5" marker-end="url(#arrow-red)"/>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 暂态稳定分析的四条路径与选择决策</p>

## 常用指标

| 指标 | 定义 | 适用范围 |
|------|------|----------|
| 临界切除时间（CCT） | 在给定故障、保护和模型下系统仍保持同步的最长故障持续时间 | 场景指标，非设备常数 |
| 临界切除角 | 单机或等效机群模型中对应临界轨迹的角度量 | 仅适用于单机或等值单机 |
| 最大相对功角 | 观察机群分离的最大功角差 | 需结合机群识别使用 |
| 失步机群 | 发生相对角度持续分离的机组集合 | 系统级指标 |
| 稳定裕度 | 可用时间、能量、角度或功率形式定义 | 必须说明计算方法和基准 |

## 量化性能边界

| 场景 | 方法 | 典型数据 | 来源 |
|------|------|----------|------|
| 大容量汽轮发电机甩负荷 | 饱和Park模型 vs 线性Park | 忽略$q$轴暂态电抗导致甩负荷后电压预测明显偏差 | Hiramatsu 2012 |
| FIDVR事件 | EMT-TS混合仿真 | 混合仿真与全EMT的最大/平均偏差均严格控制在0.05 pu以内 | Huang & Vittal 2016 |
| EMT-TS协议切换 | 组合协议（串行/并行自适应） | 纯并行协议在故障清除后首个交互步的戴维南等值电压误差显著放大 | Huang & Vittal 2016 |
| 空调电机FIDVR阈值 | 单机-无穷大母线 | 当配电母线相电压跌落至0.75 pu以下时，单相空调压缩机电机将发生不可逆堵转 | Huang & Vittal 2016 |

## 关键技术挑战

1. **模型层级与饱和**：大容量圆柱形同步机的暂态精度不只来自外部网络，机内电抗本身会因磁饱和和实心转子$q$轴暂态效应而随时间变化（Hiramatsu 2012）
2. **混合仿真接口误差**：EMT-TS接口在不对称故障下不能假定三相平衡；串行交互慢、并行交互在突变时可能失准（IEEE Task Force, Jalili-Marandi 2009）
3. **CCT的保守性与准确性矛盾**：直接法（能量函数）给出快速估计但保守性较高；时域仿真精确但计算量大
4. **同调群识别的边界**：EEAC的准确性依赖于同调聚类的正确性，机群划分错误会直接导致稳定判断错误
5. **电力电子设备对稳定的耦合**：IBR控制限幅、FACTS装置模式和HVDC换流器控制的切换可能在故障期间改变电磁功率轨迹

## 适用边界与失败模式

- **小信号稳定不能证明暂态稳定**：局部模态阻尼充足的系统仍可能在大扰动后触发限幅或失步
- **暂态稳定时域曲线不能无条件证明保护安全**：保护动作和观测时窗不足可能漏掉后续失稳
- **只看最大功角而不看相对转速、机群分裂和控制状态**：可能误判多摆失稳
- **简化机电模型在低频问题中有价值**：但对换相失败、阀级保护、谐波和不平衡负荷的暂态影响需要EMT或混合仿真验证
- **CCT是场景指标，不是设备固有常数**：运行点、故障阻抗、切除拓扑、控制器和判据变化都会改变CCT
- **等面积定则只能用于单机无穷大系统**：多机系统必须用能量函数法或EEAC

## 与相关页面的关系

- [[transient-stability-analysis]]：把本页概念转化为计算流程、判据和裕度
- [[electromechanical-modeling]]：提供暂态稳定研究所需的机电模型
- [[electromechanical-simulation]]：通过时域仿真生成暂态轨迹
- [[swing-equation]]：说明功率不平衡驱动转子运动的核心方程
- [[small-signal-stability]]：讨论平衡点附近的微扰稳定性，不能与本页互相替代
- [[electromechanical-electromagnetic-hybrid-simulation]]：用于需要EMT细节参与稳定判断的场景
- [[equal-area-criterion]]：等面积定则的详细推导页（适用于单机系统）
- [[energy-function]]：能量函数法的详细推导页

## 来源论文

- [[application-of-electromagnetic-transient-transient-stability-hybrid-simulation-t]] - Huang & Vittal 2016：EMT-TS混合仿真平台，组合交互协议，自动切换控制，多端口三相Thévenin等值。量化数据：偏差<0.05 pu，电压跌落<0.75 pu触发FIDVR
- [[saturation-in-transient-and-stability-phenomena-for-cylindrical-13&14]] - Hiramatsu 2012：饱和Park模型与线性Park模型在500/800 MVA机组的对比，甩负荷场景下q轴暂态电抗的影响。步长需设置为几十微秒级别
- [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb-fix]] - Jalili-Marandi 2009：IEEE Task Force报告，EMT-TS接口技术的综述与分类
- [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient]] - 状态空间与节点法结合的暂态仿真方法