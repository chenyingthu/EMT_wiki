---
title: "雷击感应电压 (Lightning Induced Voltage)"
type: topic
tags: [lightning, induced-voltage, electromagnetic-coupling, transmission-line, emt, field-to-line-coupling]
created: "2026-05-04"
updated: "2026-05-18"
---

# 雷击感应电压 (Lightning Induced Voltage)

## 定义与边界

雷击感应电压（Lightning Induced Voltage, LIV）是指雷云对地放电时，在附近架空线路或电气设备上由于电磁感应产生的过电压。与直击雷不同，感应雷不直接接触线路，而是通过电磁耦合（电场耦合和磁场耦合）在导线上感应出幅值可观的过电压——这使得感应雷成为配电线路（10–35 kV）和中低压系统雷击故障的主要原因。

**物理机制**：当雷云聚集于线路附近上空时，静电场在导线上感应出与雷云极性相反的电荷。若雷云对临近地面发生放电（回击通道建立），感应电荷瞬间被释放，形成沿线路传播的暂态过电压波。感应电压的峰值与雷电流幅值、导线高度、线路与雷击点距离以及大地电导率密切相关。

**边界限定**：本页面聚焦于雷击电磁感应的**建模与EMT计算方法**，不包括直击雷物理过程（参见 [[lightning-transient-analysis]]）、接地系统设计（参见 [[grounding-system-model]]）或绝缘子串闪络判据（参见 [[insulator-string-model]]）。

## EMT中的作用

雷击感应电压是配电系统防雷设计和电磁暂态仿真分析的核心场景：

| 应用方向 | 具体内容 |
|---------|---------|
| **配电线路防雷评估** | 计算10–35 kV线路的感应雷击跳闸风险，为差异化防雷策略提供依据 |
| **绝缘配合设计** | 确定线路绝缘水平与感应过电压幅值的关系，指导避雷器配置 |
| **防雷措施效果分析** | 评估避雷线、屏蔽线对感应过电压的抑制效果，优化接地布置 |
| **设备绝缘评估** | 评估变电站和终端设备承受的感应过电压暴露水平 |
| **配电自动化设备保护** | 近年配电网智能化设备（传感器、通信模块）对感应过电压的敏感性问题日益突出 |

在EMT仿真中，雷击感应电压模拟的核心挑战在于**外部电磁场与传输线网络方程的耦合接口**——外部场计算通常在频域进行，而EMT程序在时域求解，两者需通过端口集中源实现无缝衔接。

## 主要分支与机制

### 1. 电场耦合（容性耦合）

雷云电荷在导线上感应的电压由静电平衡决定，其本质是电容分压效应。

**静电感应模型**（Rusck, 1958）：
$$V_e = \frac{C_{12}}{C_{12} + C_{20}} \cdot V_{cloud}$$

其中 $C_{12}$ 为雷云与线路间电容，$C_{20}$ 为线路对地电容，$V_{cloud}$ 为雷云电位。对于典型配电线路，容性耦合主要影响波头时间较长的感应电压分量。

### 2. 磁场耦合（感性耦合）

雷电流产生的时变磁场在导线上感应电压，这是感应电压快速分量的主要来源。

**Agrawal场线耦合模型**（传输线近似，频域形式）：
$$\frac{dV(z)}{dz} + ZI(z) = V_E(z), \quad \frac{dI(z)}{dz} + YV(z) = I_E(z)$$

其中 $Z$ 和 $Y$ 为单位长度阻抗和导纳，$V_E(z)$ 和 $I_E(z)$ 为外部电磁场激励产生的分布电压源和电流源，分别由入射电场的垂直分量 $E_z^{inc}$ 和水平分量 $E_x^{inc}$ 决定：
$$V_E(z) = [E_z^{inc}(h,z) - E_z^{inc}(0,z)] - \frac{\partial}{\partial z}\int_0^h E_x^{inc}(x,z)dx$$
$$I_E(z) = -Y\int_0^h E_x^{inc}(x,z)dx$$

**Rusck简化模型**（距离 $y$ 处、高度 $h$ 的导线）：
$$V_{max} = \frac{Z_c \cdot I \cdot h}{y} \cdot k(y,t)$$

其中 $Z_c$ 为线路波阻抗，$I$ 为雷电流峰值，$k(y,t)$ 为时间相关函数，峰值约在 $t = y/v$ 时达到（$v$ 为雷电流传播速度）。

### 3. 损耗大地修正模型

大地有限的电导率导致电磁场在传播过程中产生衰减和相位偏移，需对理想导体大地假设进行修正。

**Cooray-Rubinstein公式**（损耗大地上水平电场计算）：
$$E_r(r,x,j\omega) = E_{rp}(r,x,j\omega) - H_{\phi p}(r,0,j\omega)\frac{c\mu_0}{\sqrt{\varepsilon_{rg} + \frac{\sigma_g}{j\omega\varepsilon_0}}}$$

该公式将有限电导率大地的影响映射为垂直电场与水平电场的修正项，避免了复杂的地面波 Sommerfeld 积分。式中 $\sigma_g$ 为大地电导率，$\varepsilon_{rg}$ 为大地相对介电常数。

**大地频率相关性**：土壤电阻率随频率增加而降低（高频电流趋向于在土壤表层流动），导致等效大地阻抗具有显著频率依赖性。高土壤电阻率地区（$\rho > 1000\,\Omega\cdot m$）的修正效应更为明显，峰值感应电压增幅可达 10%–15%（Alipio et al., 2023）。

### 4. 完整电磁耦合模型体系

基于麦克斯韦方程组的场线耦合框架中，主要有三种等效模型：

| 模型 | 提出者 | 核心特点 | 大地处理 |
|-----|-------|---------|---------|
| Taylor-Satterwhite-Harrison | Taylor et al. (1965) | 以入射电场垂直分量和水平分量描述激励源 | 需结合大地阻抗模型 |
| Agrawal | Agrawal et al. (1980) | 分离散射场和激励场，便于EMT端口接入 | 含损耗大地修正 |
| Rachidi | Rachidi (1993) | 考虑有限电导率大地的影响 | 显式修正镜像位置 |

## 形式化表达

### 感应电压峰值估算

**Rusck公式**（垂直雷击通道，距离 $y$ 处）：
$$V_{max} = 30 \cdot I \cdot \frac{h}{y} \quad (\text{kV})$$

其中 $I$ 为雷电流峰值（kA），$h$ 为导线高度（m），$y$ 为水平距离（m）。该简化公式适用于 $y \gg h$ 且大地为理想导体的条件。

**Cooray修正**（考虑回击速度 $v$ 的相对论效应）：
$$V_{max} = \frac{Z_c \cdot I \cdot h}{y} \cdot \frac{v}{c} \cdot \frac{1}{\sqrt{1 - (v/c)^2\sin^2\theta}}$$

其中 $c$ 为光速，$\theta$ 为雷击通道与线路法向的夹角。当 $v \to c/2$（典型回击速度）时，修正因子约 0.87–0.94。

### 感应电压波形特征

| 波形参数 | 典型值 | 与直击雷对比 |
|---------|--------|------------|
| 波头时间 | 1–5 μs | 快于直击雷（通常6 μs以上） |
| 波尾时间 | 50–100 μs | 短于直击雷 |
| 极性 | 通常与雷电流相反 | 与雷电流极性相关 |
| 峰值距离衰减 | $\propto 1/y$（Rusck公式） | 衰减快于直击雷 |

### 多导线系统感应电压

三相线路的感应电压由互阻抗矩阵决定：
$$\mathbf{V}_{ind} = \mathbf{Z}_{mutual} \cdot \mathbf{I}_{lightning}$$

其中 $\mathbf{Z}_{mutual}$ 为多导体系统的互阻抗矩阵，$\mathbf{I}_{lightning}$ 为雷电流分布向量。该矩阵方程可通过模态变换解耦为三个独立的模态方程，每个模态可独立应用上述感应电压公式。

### EMT端口集中源计算（核心接口）

将分布场源等效为线路两端的集总源，是将雷击感应电压模型嵌入EMT程序的关键步骤（Mashayekhi & Kordi, 2013; Leal & De Conti, 2021）。

**终端等效集总电压源**（链参数矩阵形式）：
$$V_{FT}(L) = \int_0^L \phi_{11}(z)[E_z^{inc}(h,z) - E_z^{inc}(0,z)]dz + \int_0^h E_x^{inc}(x,0)dx - \phi_{11}(L)\int_0^h E_x^{inc}(x,L)dx$$

其中 $\phi_{11}(z) = \cosh(\gamma z)$ 为链参数矩阵元素，$\gamma = \sqrt{ZY}$ 为传播常数。

**紧凑矩阵形式**（Leal & De Conti, 2021）：
线路离散为 $N_s$ 个等长段后，集中源的相域紧凑矩阵表达式为：
$$\bar{\mathbf{v}}_x(t) = [\mathbf{p}]\,\bar{\mathbf{b}}(t-\Delta t) + [\mathbf{S}_q]\,\bar{\mathbf{f}}(t)$$

最终注入EMT的集总源为：
$$u_0(t) = u_{x,0}(t) - \mathbf{h}\,e_z(0,t) + \mathbf{a}(\ell,t) * \mathbf{h}\,e_z(\ell,t)$$

该矩阵形式避免了传统逐段递归的高计算复杂度（从 $O(N_s^2)$ 降至 $O(N_s)$），使所有入射点的卷积可一次性完成。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 800 420" xmlns="http://www.w3.org/2000/svg">
  <!-- 雷云与回击通道 -->
  <ellipse cx="400" cy="50" rx="120" ry="40" fill="#9ca3af" stroke="#4b5563" stroke-width="2"/>
  <text x="400" y="55" text-anchor="middle" font-size="13" fill="#1f2937" font-family="Arial">雷云</text>
  <line x1="400" y1="90" x2="400" y2="200" stroke="#ef4444" stroke-width="3" stroke-dasharray="6,3"/>
  <text x="415" y="140" font-size="11" fill="#dc2626" font-family="Arial">回击通道</text>
  <text x="415" y="155" font-size="10" fill="#991b1b" font-family="Arial">I(t)</text>
  
  <!-- 电磁场辐射 (椭圆形传播) -->
  <ellipse cx="400" cy="200" rx="280" ry="120" fill="none" stroke="#92400e" stroke-width="1.5" stroke-dasharray="4,3" opacity="0.6"/>
  <ellipse cx="400" cy="200" rx="200" ry="85" fill="none" stroke="#92400e" stroke-width="1.5" stroke-dasharray="4,3" opacity="0.5"/>
  <ellipse cx="400" cy="200" rx="120" ry="50" fill="none" stroke="#92400e" stroke-width="1.5" stroke-dasharray="4,3" opacity="0.4"/>
  <text x="620" y="160" font-size="10" fill="#78350f" font-family="Arial">E_field辐射</text>
  
  <!-- 架空线路 -->
  <line x1="80" y1="300" x2="720" y2="300" stroke="#1d4ed8" stroke-width="3"/>
  <text x="400" y="320" text-anchor="middle" font-size="12" fill="#1e40af" font-family="Arial">架空配电线路 (高度 h, 长度 L)</text>
  
  <!-- 杆塔 -->
  <line x1="150" y1="300" x2="150" y2="370" stroke="#6b7280" stroke-width="2"/>
  <line x1="400" y1="300" x2="400" y2="370" stroke="#6b7280" stroke-width="2"/>
  <line x1="650" y1="300" x2="650" y2="370" stroke="#6b7280" stroke-width="2"/>
  <polygon points="145,370 155,370 150,380" fill="#6b7280"/>
  <polygon points="395,370 405,370 400,380" fill="#6b7280"/>
  <polygon points="645,370 655,370 650,380" fill="#6b7280"/>
  
  <!-- 感应电压标注 -->
  <text x="400" y="240" text-anchor="middle" font-size="10" fill="#7c3aed" font-family="Arial">Ez_inc (入射垂直电场)</text>
  
  <!-- 等效集总源示意 -->
  <rect x="80" y="255" width="50" height="30" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="105" y="273" text-anchor="middle" font-size="9" fill="#15803d" font-family="Arial">u_0(t)</text>
  <text x="105" y="283" text-anchor="middle" font-size="8" fill="#166534" font-family="Arial">集中源</text>
  
  <rect x="670" y="255" width="50" height="30" rx="4" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="695" y="273" text-anchor="middle" font-size="9" fill="#15803d" font-family="Arial">u_L(t)</text>
  <text x="695" y="283" text-anchor="middle" font-size="8" fill="#166534" font-family="Arial">集中源</text>
  
  <!-- 箭头：电磁场 → 线路 -->
  <line x1="400" y1="200" x2="400" y2="260" stroke="#d97706" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="420" y="235" font-size="10" fill="#92400e" font-family="Arial">耦合</text>
  
  <!-- 雷击点 -->
  <text x="550" y="215" font-size="11" fill="#dc2626" font-family="Arial">雷击点 (距离 y)</text>
  <line x1="550" y1="200" x2="550" y2="300" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3"/>
  <circle cx="550" cy="200" r="5" fill="#ef4444"/>
  
  <!-- EMT仿真器 -->
  <rect x="300" y="390" width="200" height="35" rx="5" fill="#e0e7ff" stroke="#4338ca" stroke-width="1.5"/>
  <text x="400" y="407" text-anchor="middle" font-size="11" fill="#3730a3" font-family="Arial">EMT仿真器 (PSCAD/EMTP)</text>
  <text x="400" y="420" text-anchor="middle" font-size="9" fill="#4338ca" font-family="Arial">端口注入: u₀(t), u_L(t)</text>
  
  <!-- 接地 -->
  <line x1="150" y1="380" x2="150" y2="400" stroke="#6b7280" stroke-width="2"/>
  <line x1="130" y1="400" x2="170" y2="400" stroke="#6b7280" stroke-width="2"/>
  <line x1="400" y1="380" x2="400" y2="400" stroke="#6b7280" stroke-width="2"/>
  <line x1="380" y1="400" x2="420" y2="400" stroke="#6b7280" stroke-width="2"/>
  <line x1="650" y1="380" x2="650" y2="400" stroke="#6b7280" stroke-width="2"/>
  <line x1="630" y1="400" x2="670" y2="400" stroke="#6b7280" stroke-width="2"/>
  
  <!-- 图例 -->
  <rect x="30" y="50" width="130" height="130" rx="4" fill="#f9fafb" stroke="#d1d5db" stroke-width="1"/>
  <text x="40" y="68" font-size="10" fill="#374151" font-family="Arial" font-weight="bold">图例</text>
  <line x1="40" y1="82" x2="60" y2="82" stroke="#ef4444" stroke-width="2"/>
  <text x="65" y="85" font-size="9" fill="#374151" font-family="Arial">回击通道</text>
  <ellipse cx="50" cy="100" rx="15" ry="8" fill="none" stroke="#92400e" stroke-width="1.5" stroke-dasharray="3,2"/>
  <text x="65" y="103" font-size="9" fill="#374151" font-family="Arial">电磁场传播</text>
  <line x1="40" y1="120" x2="60" y2="120" stroke="#1d4ed8" stroke-width="2.5"/>
  <text x="65" y="123" font-size="9" fill="#374151" font-family="Arial">架空线路</text>
  <rect x="40" y="135" width="20" height="12" rx="2" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="65" y="144" font-size="9" fill="#374151" font-family="Arial">EMT集总源</text>
  <line x1="40" y1="160" x2="60" y2="160" stroke="#d97706" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <text x="65" y="163" font-size="9" fill="#374151" font-family="Arial">场-线耦合</text>
  
  <!-- defs for arrowheads -->
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#d97706"/>
    </marker>
    <marker id="arrow2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#d97706"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 雷击感应电压EMT建模流程：雷云辐射电磁场→场线耦合→等效集总源→EMT端口注入</p>

## 关键技术挑战

### 挑战1：场线耦合模型的EMT接口

将外部雷电电磁场耦合到EMT传输线模型的核心难点在于：场计算在频域进行，而EMT在时域步进。传统FDTD/LIOV方法虽能处理外场耦合，但需要沿线网格剖分和高频时间步长，计算代价高。**端口集中源法**通过把分布源解析积分转化为仅作用于线路两端的等效集总源，使得雷击感应电压计算可复用EMT已有的传输线模型（ULM、Marti模型），无需修改EMT核心求解器。

### 挑战2：损耗大地的频变阻抗计算

大地有限的电导率导致电磁场在传播过程中产生衰减和相位偏移。精确计算损耗大地阻抗涉及Sommerfeld积分或Cooray-Rubinstein近似，两者在高频和近场条件下精度差异显著。高土壤电阻率地区（$\rho > 1000\,\Omega\cdot m$）的不准确建模可导致感应电压峰值误差达10%–15%（Alipio et al., 2023）。

### 挑战3：大规模配电网的多导体耦合

实际配电网络包含数百条支路、多回线路、多个接地点和非线性设备（避雷器、变压器磁饱和）。对每条线路分别计算感应电压再注入网络，会产生大量外部接口代码，降低仿真效率。Leal & De Conti (2026) 的JMarti模型实现了大规模配电网的矩阵化集中源组装，减少了外部求解器的调用开销。

### 挑战4：土壤频率依赖性的工程建模

土壤电阻率随频率增加而降低（高频电流趋向于在土壤表层流动），CIGRÉ推荐了 $\rho(f)$ 和 $\varepsilon_r(f)$ 的经验表达式。但在现有EMT程序中实现频率依赖土壤参数，需要在每个时间步更新大地阻抗矩阵，增加了计算复杂度。

### 挑战5：感应电压与直击雷的共同作用

实际雷击事件中，感应电压和直击雷可能在同一网络中同时发生（如附近直击雷引起感应过电压）。现有EMT模型通常独立处理两者，其叠加效应和绝缘配合的相互作用尚待深入研究。

## 量化性能边界

| 参数 | 典型范围 | 备注 |
|------|---------|------|
| 配电线路感应电压峰值 | 10–200 kV | 取决于雷电流幅值(5–100 kA)、线路高度(8–15 m)、距离(50–1000 m) |
| 感应电压波头时间 | 1–5 μs | 快于直击雷（6–20 μs），对配电设备绝缘挑战更大 |
| 大地电导率修正带来的峰值增幅 | 4%–15% | 高土壤电阻率地区(1000–10000 Ωm)效应更显著 (Alipio 2023) |
| Cooray-Rubinstein公式误差 | <2% | 损耗大地条件下水平电场计算误差 |
| 紧凑矩阵法vs顺序递归法效率提升 | 40%–65% | 当 $N_s > 50$ 时单步计算时间减少 (Leal & De Conti, 2021) |
| 算法精度（vs FDTD基准） | 峰值误差 <3% | Mashayekhi & Kordi (2013) 在 σ_g = 0.001 S/m 条件下验证 |
| 计算复杂度缩减 | 从 $O(N_s^2)$ 到 $O(N_s)$ | 矩阵化集中源计算 (Leal & De Conti, 2021) |

## 适用边界与失败模式

### 适用条件

- 雷击点距离线路一定距离（通常 50–2000 m）；近场（<50 m）条件下场线耦合模型需修正
- 线路高度和几何结构明确，导线可近似为均匀传输线
- 雷电流波形参数（幅值、波头）统计分布已知
- 土壤电阻率用于大地回路修正（典型值 $\sigma_g = 0.001$–$0.01$ S/m）

### 失效边界

| 失效条件 | 原因 | 修正方向 |
|---------|------|---------|
| 近场效应（<50 m） | 场线耦合模型基于远场近似，入射场空间分布不均匀 | 需用全波电磁求解器（如FDTD）替代解析公式 |
| 倾斜雷击通道 | 非垂直雷击改变电磁场沿线路的分布 | 使用三维电磁场计算 |
| 复杂地形（山地、山谷） | 地形的几何不规则性改变电场分布 | 需地形模型修正或全波仿真 |
| 多回击叠加 | 多次回击的累积效应改变感应电压波形 | 分段叠加或时域递归计算 |
| 屏蔽效应 | 建筑物、树木对线路的屏蔽改变感应电压分布 | 引入等效屏蔽系数 |
| 频率依赖土壤（高频>1 MHz） | 趋肤深度减小，电流重新分布 | 采用复频率相关土壤模型 |

### 关键假设

1. 雷击通道为垂直直线（简化场计算）
2. 线路为均匀传输线（忽略杆塔效应）
3. 大地为平面（复杂地形需修正）
4. 雷电流波形为双指数或Heidler模型
5. 回击速度恒定（通常为 $c/3$ 至 $c/2$）

## 与相关页面的关系

- [[lightning-transient-analysis]] — 雷击暂态整体分析（含直击雷和感应雷）
- [[transmission-line-model]] — 输电线路建模（含ULM、Marti等频变模型）
- [[distributed-parameter-line]] — 分布参数线路（感应电压传播的物理基础）
- [[grounding-system-model]] — 接地系统模型（大地回路建模）
- [[insulator-string-model]] — 绝缘子串模型（感应电压作用下的绝缘配合）
- [[electromagnetic-transient]] — 电磁暂态（EMT仿真框架）
- [[power-system-network]] — 电力系统网络（大规模配电网络仿真）
- [[emt-simulation]] — 电磁暂态仿真方法
- [[real-time-simulation]] — 实时仿真（硬件在环测试）
- [[co-simulation]] — 混合仿真（EMT与机电暂态混合）

## 开放问题

- **高比例分布式电源接入对感应过电压的影响**：风机、光伏接入点的感应电压叠加效应尚不清晰
- **配电网智能化设备的感应过电压防护**：传感器、通信设备对nanosecond级感应过电压的敏感性
- **城市配电网复杂环境下的感应过电压计算**：建筑物密度对电磁场分布的影响
- **气候变化对雷电活动的影响**：雷电活动频次和强度的变化趋势对配电线路防雷设计的影响
- **新型绝缘导线的感应过电压特性**：覆盖层对电容耦合的改变尚待量化研究

## 参考标准

- IEEE Std. 1243 — 输电线路雷电性能估算导则
- IEC 62305-2 — 雷电防护风险评估
- GB/T 50064 — 交流电气装置的过电压保护和绝缘配合
- CIGRÉ Working Group — 雷电电磁场与输电线路耦合模型

---

## 来源论文

| 论文 | 年份 | 贡献说明 |
|------|------|---------|
| [[fast-and-efficient-calculation-of-lightning-induced-voltages-in-frequency-depend]] | 2013 | 提出混合时频宏模型算法，将分布场源转化为集总源，效率提升90%以上 |
| [[compact-matrix-formulation-for-calculating-lightning-induced-voltages-on-electro]] | 2021 | 提出紧凑矩阵形式将卷积积分从 $O(N_s^2)$ 降至 $O(N_s)$，效率提升40%–65% |
| [[a-thvenin-type-version-of-the-extended-modal-domain-model-for-lightning-induced-]] | 2023 | 提出基于特征阻抗拟合的Thévenin型EMD模型，简化了Marti模型的端口源计算 |
| [[lightning-induced-voltage-analysis-on-a-three-phase-compact-distribution-line-co]] | 2020 | 分析三相紧凑配电线路的感应电压分布特性，考虑土壤非理想特性 |
| [[evaluation-of-the-extended-modal-domain-model-in-the-calculation-of-lightning-in]] | 2021 | 评估扩展模域模型在雷击感应电压计算中的准确性 |
| [[analysis-on-induced-voltages-in-wind-farms-close-to-distribution-lines-on-freque]] | 2022 | 分析频率依赖土壤对风电场附近配电线路感应电压的影响，量化了频率依赖效应 |
| [[calculation-of-lightning-induced-voltages-on-a-large-scale-distribution-network-]] | 2026 | 使用JMarti模型计算大规模配电网雷击感应电压，分析了频变线路损耗的影响 |
| [[influence-of-a-lossy-ground-on-the-lightning-performance-of-overhead-transmissio]] | 2023 | 研究损耗大地对输电线路雷击性能的影响，Sunde公式 vs Carson公式对比，背闪络率增幅4%–15% |