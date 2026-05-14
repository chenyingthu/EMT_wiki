
## 建模方法体系架构

<svg viewBox="0 0 900 520" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff;">
  <!-- Title -->
  <text x="450" y="30" text-anchor="middle" font-size="18" font-weight="bold" fill="#1a1a2e">弱电网VSC建模方法体系</text>
  
  <!-- Layer 1: 输入/源参数 (Blue) -->
  <rect x="50" y="55" width="120" height="40" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="110" y="72" text-anchor="middle" font-size="11" fill="#1e3a5f">电网强度</text>
  <text x="110" y="86" text-anchor="middle" font-size="10" fill="#1e3a5f">SCR / CSCR</text>
  
  <rect x="190" y="55" width="120" height="40" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="250" y="72" text-anchor="middle" font-size="11" fill="#1e3a5f">耦合强度</text>
  <text x="250" y="86" text-anchor="middle" font-size="10" fill="#1e3a5f">κ = Kp·iP·L/ωn</text>
  
  <rect x="330" y="55" width="120" height="40" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="390" y="72" text-anchor="middle" font-size="11" fill="#1e3a5f">控制架构</text>
  <text x="390" y="86" text-anchor="middle" font-size="10" fill="#1e3a5f">GFL / GFM</text>
  
  <!-- Layer 2: 同步/控制方法 (Green) -->
  <rect x="50" y="140" width="120" height="40" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="110" y="157" text-anchor="middle" font-size="11" fill="#164e2b">SRF-PLL</text>
  <text x="110" y="171" text-anchor="middle" font-size="9" fill="#164e2b">强电网</text>
  
  <rect x="190" y="140" width="120" height="40" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="250" y="157" text-anchor="middle" font-size="11" fill="#164e2b">DSOGI-PLL</text>
  <text x="250" y="171" text-anchor="middle" font-size="9" fill="#164e2b">中等电网</text>
  
  <rect x="330" y="140" width="120" height="40" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="390" y="157" text-anchor="middle" font-size="11" fill="#164e2b">改进DSOGI-PLL</text>
  <text x="390" y="171" text-anchor="middle" font-size="9" fill="#164e2b">弱电网+自适应</text>
  
  <rect x="470" y="140" width="120" height="40" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="530" y="157" text-anchor="middle" font-size="11" fill="#164e2b">下垂控制</text>
  <text x="530" y="171" text-anchor="middle" font-size="9" fill="#164e2b">GFM P-f/Q-V</text>
  
  <rect x="610" y="140" width="120" height="40" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="670" y="157" text-anchor="middle" font-size="11" fill="#164e2b">EVR/CPID控制</text>
  <text x="670" y="171" text-anchor="middle" font-size="9" fill="#164e2b">极弱电网</text>
  
  <!-- Layer 3: 建模层级 (Yellow) -->
  <rect x="50" y="240" width="120" height="40" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="110" y="257" text-anchor="middle" font-size="11" fill="#78350f">全开关EMT</text>
  <text x="110" y="271" text-anchor="middle" font-size="9" fill="#78350f">最高精度</text>
  
  <rect x="190" y="240" width="120" height="40" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="250" y="257" text-anchor="middle" font-size="11" fill="#78350f">AVM平均值</text>
  <text x="250" y="271" text-anchor="middle" font-size="9" fill="#78350f">中等精度</text>
  
  <rect x="330" y="240" width="120" height="40" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="390" y="257" text-anchor="middle" font-size="11" fill="#78350f">EIBR等效</text>
  <text x="390" y="271" text-anchor="middle" font-size="9" fill="#78350f">Luchini 2023</text>
  
  <rect x="470" y="240" width="120" height="40" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="530" y="257" text-anchor="middle" font-size="11" fill="#78350f">DIBM离散阻抗</text>
  <text x="530" y="271" text-anchor="middle" font-size="9" fill="#78350f">Vahabzadeh 2025</text>
  
  <rect x="610" y="240" width="120" height="40" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="670" y="257" text-anchor="middle" font-size="11" fill="#78350f">RMS+增强</text>
  <text x="670" y="271" text-anchor="middle" font-size="9" fill="#78350f">Carreño 2026</text>
  
  <!-- Layer 4: 量化性能 (Purple) -->
  <rect x="50" y="340" width="120" height="40" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="110" y="357" text-anchor="middle" font-size="11" fill="#4c1d95">误差 &lt; 3%</text>
  <text x="110" y="371" text-anchor="middle" font-size="9" fill="#4c1d95">EIBR故障工况</text>
  
  <rect x="190" y="340" width="120" height="40" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="250" y="357" text-anchor="middle" font-size="11" fill="#4c1d95">误差 &lt; 0.5%</text>
  <text x="250" y="371" text-anchor="middle" font-size="9" fill="#4c1d95">DIBM 200μs</text>
  
  <rect x="330" y="340" width="120" height="40" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="390" y="357" text-anchor="middle" font-size="11" fill="#4c1d95">误差 &lt; 5%</text>
  <text x="390" y="371" text-anchor="middle" font-size="9" fill="#4c1d95">RMS+模态分析</text>
  
  <rect x="470" y="340" width="120" height="40" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="530" y="357" text-anchor="middle" font-size="11" fill="#4c1d95">调节时间↓60%</text>
  <text x="530" y="371" text-anchor="middle" font-size="9" fill="#4c1d95">改进DSOGI-PLL</text>
  
  <rect x="610" y="340" width="120" height="40" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="670" y="357" text-anchor="middle" font-size="11" fill="#4c1d95">初始化加速6.9x</text>
  <text x="670" y="371" text-anchor="middle" font-size="9" fill="#4c1d95">CISS/DI方法</text>
  
  <!-- Layer 5: 应用场景 (Amber) -->
  <rect x="100" y="430" width="120" height="36" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="160" y="445" text-anchor="middle" font-size="10" fill="#78350f">强电网并网</text>
  <text x="160" y="458" text-anchor="middle" font-size="9" fill="#78350f">SCR &gt; 5</text>
  
  <rect x="250" y="430" width="120" height="36" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="310" y="445" text-anchor="middle" font-size="10" fill="#78350f">弱电网并网</text>
  <text x="310" y="458" text-anchor="middle" font-size="9" fill="#78350f">SCR &lt; 3</text>
  
  <rect x="400" y="430" width="120" height="36" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="460" y="445" text-anchor="middle" font-size="10" fill="#78350f">极弱电网/孤岛</text>
  <text x="460" y="458" text-anchor="middle" font-size="9" fill="#78350f">SCR &lt; 2</text>
  
  <rect x="550" y="430" width="120" height="36" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="610" y="445" text-anchor="middle" font-size="10" fill="#78350f">实时仿真</text>
  <text x="610" y="458" text-anchor="middle" font-size="9" fill="#78350f">OPAL-RT</text>
  
  <rect x="700" y="430" width="120" height="36" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="760" y="445" text-anchor="middle" font-size="10" fill="#78350f">小信号稳定性</text>
  <text x="760" y="458" text-anchor="middle" font-size="9" fill="#78350f">模态分析</text>
  
  <!-- Arrows from Layer 1 to Layer 2 -->
  <line x1="110" y1="95" x2="110" y2="135" stroke="#666" stroke-width="1.2" marker-end="url(#arrowhead)"/>
  <line x1="250" y1="95" x2="250" y2="135" stroke="#666" stroke-width="1.2" marker-end="url(#arrowhead)"/>
  <line x1="390" y1="95" x2="390" y2="135" stroke="#666" stroke-width="1.2" marker-end="url(#arrowhead)"/>
  <line x1="530" y1="95" x2="530" y2="135" stroke="#666" stroke-width="1.2" marker-end="url(#arrowhead)"/>
  <line x1="670" y1="95" x2="670" y2="135" stroke="#666" stroke-width="1.2" marker-end="url(#arrowhead)"/>
  
  <!-- Arrows from Layer 2 to Layer 3 -->
  <line x1="110" y1="180" x2="110" y2="235" stroke="#666" stroke-width="1.2" marker-end="url(#arrowhead)"/>
  <line x1="250" y1="180" x2="250" y2="235" stroke="#666" stroke-width="1.2" marker-end="url(#arrowhead)"/>
  <line x1="390" y1="180" x2="390" y2="235" stroke="#666" stroke-width="1.2" marker-end="url(#arrowhead)"/>
  <line x1="530" y1="180" x2="530" y2="235" stroke="#666" stroke-width="1.2" marker-end="url(#arrowhead)"/>
  <line x1="670" y1="180" x2="670" y2="235" stroke="#666" stroke-width="1.2" marker-end="url(#arrowhead)"/>
  
  <!-- Arrows from Layer 3 to Layer 4 -->
  <line x1="110" y1="280" x2="110" y2="335" stroke="#666" stroke-width="1.2" marker-end="url(#arrowhead)"/>
  <line x1="250" y1="280" x2="250" y2="335" stroke="#666" stroke-width="1.2" marker-end="url(#arrowhead)"/>
  <line x1="390" y1="280" x2="390" y2="335" stroke="#666" stroke-width="1.2" marker-end="url(#arrowhead)"/>
  <line x1="530" y1="280" x2="530" y2="335" stroke="#666" stroke-width="1.2" marker-end="url(#arrowhead)"/>
  <line x1="670" y1="280" x2="670" y2="335" stroke="#666" stroke-width="1.2" marker-end="url(#arrowhead)"/>
  
  <!-- Arrows from Layer 4 to Layer 5 -->
  <line x1="160" y1="380" x2="160" y2="425" stroke="#666" stroke-width="1.2" marker-end="url(#arrowhead)"/>
  <line x1="310" y1="380" x2="310" y2="425" stroke="#666" stroke-width="1.2" marker-end="url(#arrowhead)"/>
  <line x1="460" y1="380" x2="460" y2="425" stroke="#666" stroke-width="1.2" marker-end="url(#arrowhead)"/>
  <line x1="610" y1="380" x2="610" y2="425" stroke="#666" stroke-width="1.2" marker-end="url(#arrowhead)"/>
  <line x1="760" y1="380" x2="760" y2="425" stroke="#666" stroke-width="1.2" marker-end="url(#arrowhead)"/>
  
  <!-- Arrow marker -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#666"/>
    </marker>
  </defs>
  
  <!-- Legend -->
  <rect x="50" y="490" width="12" height="12" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="68" y="501" font-size="9" fill="#333">输入参数</text>
  
  <rect x="140" y="490" width="12" height="12" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="158" y="501" font-size="9" fill="#333">控制方法</text>
  
  <rect x="230" y="490" width="12" height="12" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="248" y="501" font-size="9" fill="#333">建模层级</text>
  
  <rect x="320" y="490" width="12" height="12" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="338" y="501" font-size="9" fill="#333">量化性能</text>
  
  <rect x="410" y="490" width="12" height="12" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="428" y="501" font-size="9" fill="#333">应用场景</text>
</svg>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 弱电网VSC建模方法五层体系架构：从电网强度输入到应用场景输出，涵盖同步控制、建模层级和量化性能指标</p>

## 关键技术挑战

### 挑战1：PLL带宽与电网强度的耦合设计

弱电网中电网阻抗增大导致PLL与电网形成负阻效应，传统基于强网经验的PLL参数整定方法失效。需要建立PLL参数（$K_p$, $K_i$）与SCR之间的定量映射关系。Carreño (2026) 给出的耦合强度系数 $\kappa$ 提供了方向，但实际工程中还需考虑谐波、不平衡、频率斜坡等多重扰动下的综合影响。

### 挑战2：GFL/GFM在弱电网中的混合协调

高比例新能源并网系统中，GFL和GFM VSC往往共存于同一弱电网中。GFM提供电压/频率支撑，GFL负责功率追踪，两者之间的控制交互、功率分配、故障穿越协调尚缺乏系统性的建模框架。Nurunnabi (2025) 在100 kVA实验中验证了GFM/GFL并联运行的可行性，但大规模系统中的动态协调问题仍需深入研究。

### 挑战3：EMT仿真效率与精度的权衡

弱电网VSC建模需要在仿真精度和计算效率之间取得平衡。全开关EMT模型精度高但计算量大，RMS模型效率高但漏掉关键失稳机制。Carreño (2026) 的RMS+和Vahabzadeh (2025) 的DIBM分别从中低频模态分析和实时仿真角度给出了折中方案，但针对弱电网特定场景的专用降阶模型仍需发展。

### 挑战4：PQ能力边界的动态更新

GFM VSC的PQ能力边界随PCC电压、直流母线电压、滤波器拓扑动态变化。Nurunnabi (2025) 给出了RIC与PWM约束圆的几何交集算法，但实时计算效率、边界突变时的控制器切换逻辑、以及多逆变器并联时的PQ边界叠加效应仍需深入研究。

## 量化性能边界

### SCR稳定边界

| 控制类型 | PLL/控制策略 | 稳定下限SCR | 数据来源 |
|---------|-------------|------------|---------|
| GFL | SRF-PLL, 带宽30-50 Hz | ≈ 2.0-2.5 | 文献综合 |
| GFL | 改进DSOGI-PLL（Ranasinghe 2024） | ≈ 1.0 | IEEE 9节点, SCR≈1.8 |
| GFM | 下垂控制 | ≈ 1.0-1.5 | Nurunnabi 2025 |

### PLL暂态性能（SCR ≈ 1.8, IEEE 9节点, Ranasinghe 2024）

| 测试场景 | 传统DSOGI-PLL | 改进DSOGI-PLL | 改善幅度 |
|---------|--------------|--------------|---------|
| 不对称故障调节时间 | 0.040 s | 0.016 s | 缩短60% |
| 不对称故障超调量 | 0.272 rad | 0.113 rad | 降低58.5% |
| 90°相位跳变调节时间 | 0.15 s | 0.03 s | 缩短80% |
| 90°相位跳变超调量 | 2.003 rad | 1.719 rad | 降低14.2% |
| 频率跟踪RMSE (8-9s) | 2.16 Hz | 0.001 Hz | 降幅99.95% |

### 等效模型精度与效率

| 模型类型 | 测试场景 | 误差 | 效率提升 | 数据来源 |
|---------|---------|------|---------|---------|
| EIBR (Luchini 2023) | ATP/ATPDraw故障工况 | 2.33% | 时间降低70% | ATP/ATPDraw |
| DIBM (Vahabzadeh 2025) | 7节点VSC系统, 200 μs步长 | < 0.5% | 状态数降84.1% | MATLAB/OPAL-RT |
| DIBM (Vahabzadeh 2025) | 最大步长 | 80 μs → 1 ms | 步长扩大12.5倍 | MATLAB/OPAL-RT |
| RMS+ (Carreño 2026) | IEEE 39节点, 多GFL | 特征值误差<5% | 状态数降75-80% | MATLAB模态分析 |

### GFM PQ能力与初始化

| 指标 | 数值 | 数据来源 |
|------|------|---------|
| SVPWM最大输出电压 | 1.53 p.u.（SPWM为1.33 p.u.） | Nurunnabi 2025 |
| EVR电压最大偏差 | < 2.9% | Nurunnabi 2025 |
| EVR频率最大偏差 | < 0.37% | Nurunnabi 2025 |
| CISS/DI初始化加速比 | 6.9倍 | Allabadi 2024, CIGRE BM4 |

## 适用边界与选择指南

### 场景-方法推荐表

| 应用场景 | SCR范围 | 推荐模型/方法 | 关键约束 |
|---------|--------|--------------|---------|
| 强电网VSC并网 | SCR > 5 | 标准GFL + SRF-PLL | 可直接沿用同步机控制参数 |
| 中等电网VSC并网 | 3 ≤ SCR ≤ 5 | GFL + DSOGI-PLL | 需限制PLL带宽 < 谐振频率 |
| 弱电网VSC并网 | SCR < 3 | 改进DSOGI-PLL / GFM | 需暂态检测器或无PLL控制 |
| 极弱电网/孤岛 | SCR < 2 | GFM + 下垂/EVR控制 | GFL控制基本失效 |
| 大规模系统EMT | 任意 | EIBR等效模型 | 精度误差 < 3%, 效率提升70% |
| 实时仿真 | 任意 | DIBM离散阻抗接口 | 步长可达1 ms, 状态数降84% |
| 小信号稳定性分析 | 任意 | RMS+增强电路模型 | 状态数降75%, 精度保持EMT级 |
| 黑盒GVSC初始化 | 任意 | CISS / DI方法 | 初始化时间缩短6.9倍 |

### 失效边界

- **SCR < 1.0**：多数GFL控制失效，需采用GFM或混合控制
- **极弱电网大扰动**：线性化小信号模型不适用，需完整EMT仿真
- **不同PLL结构**：SRF/DSOGI/延时信号消除在相同SCR下的稳定性边界不同，不可泛化
- **开关级谐波分析**：等效模型（EIBR/DIBM）不适用，需全开关EMT模型
- **时间尺度分离假设不成立**：当 $\tau_f/\tau_s \geq 0.3$ 时，RMS+近似误差显著增大，需采用高阶修正

## 相关模型

- [[vsc-model|VSC模型]] - 通用VSC EMT模型
- [[gfl-inverter-model|跟网型逆变器模型]] - GFL VSC建模
- [[gfm-inverter-model|构网型逆变器模型]] - GFM VSC建模
- [[pll-model|PLL模型]] - 锁相环建模与稳定性分析
- [[average-value-model|平均值模型]] - VSC平均化建模方法

## 相关方法

- [[vector-control-model|矢量控制]] - dq坐标系控制策略
- [[grid-forming-control|构网控制]] - 弱网稳定控制策略
- [[impedance-modeling|阻抗建模]] - 弱网稳定性分析
- [[frequency-scan|频率扫描]] - SCR/CSCR判别方法
- [[dsogi-pll|DSOGI-PLL]] - 改进型锁相环
- [[small-signal-stability|小信号稳定性]] - 弱网稳定性分析

## 相关主题

- [[vsc-hvdc|VSC-HVDC]] - 高压直流输电系统
- [[renewable-energy-integration|新能源并网]] - 弱电网接入挑战
- [[small-signal-stability|小信号稳定性]] - 弱网稳定性评估
- [[large-scale-system-simulation|大规模系统仿真]] - 等效建模需求

## 来源论文

- **Ranasinghe 等 (2024)** - "Advanced DSOGI PLL with Adaptive Bandwidth for Improved Transient Performance of Grid Connected Inverter Control Systems" (IEEE PESGM 2024)。提出改进型DSOGI-PLL，引入暂态检测器（频率冻结）和自适应带宽机制，在SCR ≈ 1.8的极弱电网中实现不对称故障下调节时间缩短60%、相位超调降低58.5%、频率跟踪RMSE降至0.001 Hz（降幅99.95%），系统临界稳定SCR从2.3扩展至1.0。

- **Carreño 等 (2026)** - "RMS+: Augmenting the Traditional Circuit Model to Capture PLL Instability" (IEEE Trans. Power Delivery, Vol. 41, No. 1)。从慢快系统理论出发，提出RMS+增强电路模型，揭示传统RMS模型因忽略电感"di/dt"效应而完全漏掉PLL与网络交互的两种失稳机制（跨临界分岔和Hopf分岔），在IEEE 39节点系统中状态数减少75-80%且特征值预测误差 < 5%。

- **Allabadi 等 (2024)** - "Initializing EMT models of grid forming VSCs in MTDC systems" (Electric Power Systems Research, Vol. 235)。针对MTDC系统中GVSC的EMT初始化难题，提出CISS稳态控制初始化和DI解耦接口法，在CIGRE BM4基准系统中将完整系统初始化时间缩短6.9倍，DI方法成功适用于黑盒GVSC模型。

- **Nurunnabi 等 (2025)** - "Advancing Grid-Forming Inverter Technology: Comprehensive PQ Capability and Performance Analysis" (IEEE Access)。提出综合考虑PWM饱和与额定电流约束的GFM逆变器PQ能力边界建模方法，推导L/LC/LCL三种耦合滤波器下的PCC点功率方程，给出RIC与PWM约束圆的几何交集算法，EVR策略在动态负载下电压偏差 < 2.9%、频率偏差 < 0.37%。

- **Luchini 等 (2023)** - "Equivalent grid-following inverter-based generator model for ATP/ATPDraw simulations" (Electric Power Systems Research)。提出适用于EMTP的跟网型IBR等效时域模型（EIBR），采用"PLL同步+瞬时功率反解dq电流+受控电流源"架构，在故障条件下输出电流平均误差2.33%，仿真执行时间降低约70%。

- **Vahabzadeh 等 (2025)** - "Discretized Impedance-Based Modeling of Converter-Interfaced Energy Resources for State-Variable-Based Real-Time EMT Simulators" (IEEE Open J. Power Electronics)。提出离散阻抗建模（DIBM）方法，将VSC导纳模型通过梯形积分离散化并转换为戴维南等效接口，在7节点VSC系统（20台VSC）中状态数从271降至43（降幅84.1%），最大仿真步长从80 μs提升至1 ms。

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。量化数据均标注来源论文，未报告的数据已明确标注数据缺口。*
