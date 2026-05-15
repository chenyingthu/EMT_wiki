---
title: "电磁暂态 (Electromagnetic Transient)"
type: topic
tags: [electromagnetic-transient, emt, fast-transient, switching, overvoltage]
created: "2026-05-02"
updated: "2026-05-16"
---

# 电磁暂态 (Electromagnetic Transient)

## 定义与边界

电磁暂态（Electromagnetic Transient，EMT）指电力系统中电压、电流、磁链、电荷和电磁场在扰动后发生的快速时域变化过程。它覆盖开关动作、雷电冲击、短路故障、铁磁饱和、电力电子开关和行波传播等波形级现象，通常需要在相域或多导体坐标中保留瞬时量。

EMT 现象的时间跨度从微秒级（雷电波头 0.1~10μs、开关动作 1~100μs）到秒级（故障清除后恢复 0.1~10s），对应频率范围从直流分量到数十 kHz（雷电波头 10kHz~1MHz、开关暂态 1~500kHz）。这与以机电能量交换为主的研究对象（转子角慢速摆动、秒级频率恢复）形成鲜明对比。

本页讨论"物理现象与研究对象"。它不同于 [[emt-simulation]]，后者讨论如何用数值程序求解这些现象；也不同于 [[electromechanical-transient]]，后者以机电能量交换、转子角和慢速控制为主。若研究问题只依赖工频正序相量、潮流或秒级频率恢复，直接使用 EMT 语言会夸大模型需求。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 600" xmlns="http://www.w3.org/2000/svg">
  <!-- 输入层：扰动源 -->
  <rect x="20" y="20" width="180" height="80" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="110" y="55" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle" fill="#1e40af">扰动源类型</text>
  <text x="110" y="80" font-family="Arial" font-size="11" text-anchor="middle" fill="#1e40af">开关/雷电/故障</text>

  <!-- 箭头 -->
  <path d="M200 60 L270 60" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>

  <!-- EMT核心方程 -->
  <rect x="270" y="20" width="360" height="80" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="450" y="55" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle" fill="#166534">EMT 控制方程组</text>
  <text x="450" y="78" font-family="Arial" font-size="11" text-anchor="middle" fill="#166534">Y(v)=i_src+i_hist+i_nl</text>

  <!-- 箭头到输出 -->
  <path d="M630 60 L700 60" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrow)"/>

  <!-- 输出层 -->
  <rect x="700" y="20" width="180" height="80" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="790" y="55" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle" fill="#6b21a8">时域波形</text>
  <text x="790" y="78" font-family="Arial" font-size="11" text-anchor="middle" fill="#6b21a8">电压/电流/磁链</text>

  <!-- 五类暂态 -->
  <rect x="270" y="140" width="360" height="280" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="450" y="170" font-family="Arial" font-size="13" font-weight="bold" text-anchor="middle" fill="#92400e">EMT 五大分支</text>

  <rect x="290" y="185" width="100" height="50" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="340" y="215" font-family="Arial" font-size="11" font-weight="bold" text-anchor="middle" fill="#991b1b">开关暂态</text>

  <rect x="410" y="185" width="100" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="460" y="215" font-family="Arial" font-size="11" font-weight="bold" text-anchor="middle" fill="#1e40af">雷电暂态</text>

  <rect x="530" y="185" width="100" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="580" y="215" font-family="Arial" font-size="11" font-weight="bold" text-anchor="middle" fill="#166534">故障暂态</text>

  <rect x="290" y="255" width="100" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="340" y="285" font-family="Arial" font-size="11" font-weight="bold" text-anchor="middle" fill="#92400e">频变传播</text>

  <rect x="410" y="255" width="100" height="50" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="460" y="285" font-family="Arial" font-size="11" font-weight="bold" text-anchor="middle" fill="#6b21a8">非线性暂态</text>

  <rect x="530" y="255" width="100" height="50" rx="6" fill="#fce7f3" stroke="#db2777" stroke-width="1.5"/>
  <text x="580" y="285" font-family="Arial" font-size="11" font-weight="bold" text-anchor="middle" fill="#9d174d">电磁振荡</text>

  <!-- 数值求解 -->
  <rect x="290" y="325" width="340" height="75" rx="6" fill="#f3f4f6" stroke="#6b7280" stroke-width="1.5"/>
  <text x="460" y="350" font-family="Arial" font-size="12" font-weight="bold" text-anchor="middle" fill="#374151">数值积分方法</text>
  <text x="460" y="370" font-family="Arial" font-size="10" text-anchor="middle" fill="#4b5563">梯形积分 | 后向欧拉 | Gear法 | 插值策略</text>

  <!-- 典型参数 -->
  <rect x="20" y="460" width="860" height="100" rx="8" fill="#f9fafb" stroke="#9ca3af" stroke-width="1.5"/>
  <text x="450" y="490" font-family="Arial" font-size="13" font-weight="bold" text-anchor="middle" fill="#374151">典型参数范围</text>
  <text x="150" y="520" font-family="Arial" font-size="11" text-anchor="middle" fill="#4b5563">时间步长</text>
  <text x="150" y="540" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle" fill="#1f2937">1μs ~ 1ms</text>
  <text x="320" y="520" font-family="Arial" font-size="11" text-anchor="middle" fill="#4b5563">系统规模</text>
  <text x="320" y="540" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle" fill="#1f2937">10~1000节点</text>
  <text x="490" y="520" font-family="Arial" font-size="11" text-anchor="middle" fill="#4b5563">电压等级</text>
  <text x="490" y="540" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle" fill="#1f2937">10kV ~ 500kV</text>
  <text x="660" y="520" font-family="Arial" font-size="11" text-anchor="middle" fill="#4b5563">功率范围</text>
  <text x="660" y="540" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle" fill="#1f2937">1MW ~ 1000MW</text>
  <text x="830" y="520" font-family="Arial" font-size="11" text-anchor="middle" fill="#4b5563">频率范围</text>
  <text x="830" y="540" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle" fill="#1f2937">50Hz / 60Hz</text>

  <!-- 图例 -->
  <rect x="20" y="570" width="15" height="15" rx="2" fill="#fee2e2"/>
  <text x="42" y="582" font-family="Arial" font-size="10" fill="#4b5563">开关</text>
  <rect x="90" y="570" width="15" height="15" rx="2" fill="#dbeafe"/>
  <text x="112" y="582" font-family="Arial" font-size="10" fill="#4b5563">雷电</text>
  <rect x="160" y="570" width="15" height="15" rx="2" fill="#dcfce7"/>
  <text x="182" y="582" font-family="Arial" font-size="10" fill="#4b5563">故障</text>
  <rect x="230" y="570" width="15" height="15" rx="2" fill="#fef3c7"/>
  <text x="252" y="582" font-family="Arial" font-size="10" fill="#4b5563">频变</text>
  <rect x="300" y="570" width="15" height="15" rx="2" fill="#ede9fe"/>
  <text x="322" y="582" font-family="Arial" font-size="10" fill="#4b5563">非线性</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 电磁暂态（EMT）分类体系与典型参数范围</p>

## EMT 中的角色

电磁暂态是 EMT 建模和验证的核心对象。仿真模型需要回答的不是"系统是否正常运行"，而是扰动后某个端口、设备或保护判据看到的瞬时波形是否可信。典型用途包括：

- 在 [[switching-transient]] 中评估合闸、分闸、重燃、截流和暂态恢复电压（TRV）。
- 在 [[lightning-overvoltage]] 中评估行波、反射、接地响应、避雷器应力和绝缘配合。
- 在 [[unbalanced-fault-analysis]] 中保留相别、零序、负序、直流偏置和保护测量链。
- 在 [[power-electronics]]、[[vsc-hvdc]] 和 [[mmc-model]] 中观察阀级开关、限流、控制采样和非线性保护动作。

## 主要分支与机制

电磁暂态可按扰动源和传播机制分为五个相互重叠的分支：

### 1. 开关暂态

拓扑状态 $s(t)$ 改变，使网络方程在事件点发生重组或等值切换。典型场景包括：

- **合闸操作**：断路器闭合，线路或设备投入，伴随暂态恢复电压（TRV）和励磁涌流。
- **分闸操作**：断路器断开，感性负荷产生截流过电压。
- **重燃事件**：断路器分闸后触头间隙重燃，产生高频振荡。
- **故障清除**：保护动作隔离故障，系统恢复时的电压和电流恢复过程。

开关暂态的数值挑战在于事件点处理：插值策略、梯形积分在事件点的能量误差、以及开关状态变化时的方程重组。

### 2. 雷电暂态

雷电流、外部电磁场和接地系统共同产生入射波、反射波和侵入波。雷电暂态建模需要与 [[transmission-line-theory]]、[[frequency-dependent-soil]] 和 [[surge-arrester-model]] 衔接。雷电流波形通常用双指数函数或 Heidler 函数描述：

$$i(t) = \frac{I_0}{\eta}\left(e^{-t/\tau_1} - e^{-t/\tau_2}\right)$$

其中 $I_0$ 为峰值电流，$\tau_1$ 和 $\tau_2$ 分别为波尾和波头时间常数，$\eta$ 为峰值归一化因子。雷电波沿导线传播时发生折射和反射，接地杆塔的冲击接地阻抗导致电压升高，避雷器动作限制过电压幅值。

### 3. 故障暂态

故障阻抗、接地路径、保护动作和电机次暂态响应共同决定电流波形。故障暂态的突出特征是直流偏置分量——对称分量法在故障后首个周期内不再适用。电流可分解为：

$$i(t) = I_m\sin(\omega t + \theta - \phi) + I_{dc}e^{-t/\tau_a}$$

其中 $I_m$ 为稳态基频幅值，$I_{dc}$ 为直流偏置初始值，$\tau_a = L/R$ 为衰减时间常数。直流偏置使电流峰值远超稳态值，影响断路器开断能力选择和保护定值整定。

### 4. 频变传播

导体集肤效应、大地回流和电缆护层使阻抗和导纳随频率变化。频变特性通常由 [[wideband-modeling]]、[[vector-fitting]] 或 [[universal-line-model]] 表示为有理函数形式或卷积形式。频变线路模型的 EMT 时域实现需要递归卷积或状态空间等效：

$$\mathbf{Y}_{s,n}\mathbf{v}_n = \mathbf{i}^{\mathrm{src}}_n + \mathbf{i}^{\mathrm{hist}}_n + \mathbf{i}^{\mathrm{nl}}(\mathbf{v}_n, \mathbf{x}_n)$$

其中 $\mathbf{i}^{\mathrm{hist}}_n$ 为历史源项，源于频率相关的卷积核。J. Marti 首先引入频率相关线路模型，将分布参数线路的频域阻抗 $Z(\omega)$ 和导纳 $Y(\omega)$ 拟合为有理函数后转换到时域。

### 5. 非线性暂态

磁饱和、电弧、避雷器、开关器件和控制限幅使局部关系从线性导纳变为 $i = f(v, x, t)$。非线性 EMT 暂态需要迭代求解——每个时步，牛顿-拉夫森迭代或直接替代法处理非线性元件的更新：

$$x_{n+1} = F_{\Delta t}(x_n, v_n, u_n, s_n)$$

其中状态更新函数 $F_{\Delta t}$ 包含积分算法的离散化映射和非线性元件的查表或函数求值。

## 形式化表达

EMT 问题的保守时域表达可写为节点方程形式：

$$\mathbf{Y}_n \mathbf{v}_n = \mathbf{i}^{\mathrm{src}}_n + \mathbf{i}^{\mathrm{hist}}_n + \mathbf{i}^{\mathrm{nl}}(\mathbf{v}_n, \mathbf{x}_n)$$

$$\mathbf{x}_{n+1} = \mathbf{A}\mathbf{x}_n + \mathbf{B}\mathbf{v}_n$$

其中：
- $\mathbf{v}_n$ 为 $t = n\Delta t$ 时刻的节点电压向量
- $\mathbf{Y}_n$ 为节点导纳矩阵（与拓扑状态 $s_n$ 相关）
- $\mathbf{i}^{\mathrm{src}}_n$ 为独立电源注入
- $\mathbf{i}^{\mathrm{hist}}_n$ 为由卷积历史项转化而来的等效历史源
- $\mathbf{i}^{\mathrm{nl}}$ 为非线性元件的等效注入电流
- $\mathbf{x}_n$ 为储能元件（电感电流、电容电压）的状态向量

### 数值积分离散化

对电感元件 $v = L\frac{di}{dt}$，梯形积分给出：

$$i_{n+1} = i_n + \frac{\Delta t}{2L}(v_{n+1} + v_n)$$

等效伴随电路为电导与历史电流源的并联：

$$G_L = \frac{\Delta t}{2L}, \quad i^{\mathrm{hist}}_n = i_n + G_L v_n$$

对电容元件 $i = C\frac{dv}{dt}$，类似推导可得：

$$G_C = \frac{2C}{\Delta t}, \quad i^{\mathrm{hist}}_n = G_C v_n - i_n$$

### 事件点处理

开关状态变化导致 $\mathbf{Y}_n$ 重组。直接法在事件点重构导纳矩阵并重新因子分解；补偿法保持 $\mathbf{L}\mathbf{U}$ 不变，仅修改右端项。当事件密集时（如故障清除后拓扑恢复），补偿法效率显著高于直接法。

## 关键技术挑战

### 1. 步长-精度权衡

开关暂态需要 0.1~10μs 步长以捕捉高频振荡，而机电暂态只需 1~10ms 步长。多速率仿真（multi-rate EMT）通过接口模型连接不同速率子系统，是大规模系统仿真的关键技术。

Zhao 等（2022）提出的"仿真精度频谱"显示：低频段误差可能大于高频段。例如在 Δt=90μs 时，550 Hz 激励下仿真电流幅值误差达 33%，步长阈值效应明显。

### 2. 数值振荡与阻尼

梯形积分在后向欧拉（Gear）方法中引入数值阻尼以抑制高频振荡。阻尼系数 $\alpha$ 控制阻尼强度：

$$x_{n+1} = \frac{1}{1+\alpha}\left[(1-\alpha)x_n + \Delta t f(\dots)\right]$$

插值策略会改变高频阻尼与事件点能量误差，应在 [[numerical-integration]] 和 [[interpolation-method]] 的边界内解释。

### 3. 频变参数精确性

详细 EMT 结果依赖参数质量：线路频变参数、变压器饱和特性、避雷器伏安曲线、电弧参数和控制限幅缺失时，结论只能作为场景探索而不能作为工程决策依据。

### 4. 大规模系统矩阵效率

大系统 EMT 可能因矩阵重构、非线性迭代、事件密集和初始化不一致而失败。稀疏矩阵技术、并行计算和模型降阶是主要加速手段。

## 量化性能边界

| 指标 | 典型范围 | 备注 |
|------|---------|------|
| 时间步长 | 0.1~100μs | 取决于研究对象的最高频率 |
| 仿真时长 | 0.1~10s | 包括故障清除和恢复过程 |
| 系统规模 | 10~10000 节点 | 与可用计算资源相关 |
| 计算效率 | 10~1000 实时倍速 | 取决于系统复杂度和硬件 |
| 数值阻尼 | 0~20% | 高频振荡的数值衰减 |

**来源数据**：
- Zhao 等（2022）：300km ULM 线路，Δt=10μs 时 230 Hz 处误差 0.8%（向量拟合误差 2%）
- Meredith（1997）：有限截面法，2 截面/穿透深度时模型精度满足工程要求

## 适用边界与选择指南

| 场景 | 推荐建模层级 | 步长 | 关键考虑 |
|------|------------|------|---------|
| 开关操作暂态 | 详细开关/弧柱模型 | 0.1~1μs | TRV 峰值、重燃判据 |
| 雷电过电压 | 行波模型/冲击接地 | 0.01~0.1μs | 波头陡度、折射系数 |
| 故障暂态分析 | 分布参数线路、饱和变压器 | 1~10μs | 直流偏置、恢复电压 |
| 电力电子暂态 | 详细开关/平均值模型 | 1~50μs | PWM 谐波、控制响应 |
| 机电暂态研究 | 准稳态 / 动态相量 | 0.5~5ms | 转子角、功角稳定 |

**边界条件**：
- 若只关心工频正序相量，不必使用 EMT 详细模型
- 若系统含大量电力电子变流器，需评估开关谐振频段是否被激励
- 实时仿真约束下，均方根（RMS）模型可能优于 EMT 详细模型

## 与相关页面的关系

- [[emt-simulation]] 是仿真范式页；本页是现象边界页。
- [[switching-transient]]、[[lightning-overvoltage]] 和 [[unbalanced-fault-analysis]] 是本主题下的高频、过电压和故障分支。
- [[phase-domain-model]] 说明在相域保留不对称和耦合的建模路线，是许多电磁暂态问题的底层表达。
- [[frequency-domain-analysis]] 和 [[harmonic-analysis]] 提供频域诊断，但不能替代事件驱动的瞬时波形验证。
- [[real-time-simulation]] 与 [[hil-simulation]] 是执行约束；实时通过不等于物理模型自动更可信。

## 来源论文

- [[emtp-modeling-of-electromagnetic-transients-power-delivery-ieee-transactions-on]] — 有限截面法（Method of Finite Sections）：将导体径向离散为有限体积单元，在 EMTP 中实现导体内部电磁波传播的精确时域仿真，精度达工程要求（1~2 截面/穿透深度）。
- [[accuracy-evaluation-of-electromagnetic-transients-simulation-algorithms]] — 仿真精度频谱方法：提出基于双线性变换和诺顿等效的全局频域精度评估，550 Hz 处误差可达 33%（Δt=90μs），首次实现分布参数网络的系统级精度量化。
- [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient]] — 状态空间与节点分析组合方法：支撑状态空间法与节点分析组合的机制讨论。
- [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir]] — 伴随电路实现比较：提醒不同伴随电路实现之间可能存在数值差异。
- [[improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an]] — 线路暂态数值稳定性改进：可作为线路与电缆暂态中数值稳定性问题的来源入口。