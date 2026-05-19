---
title: "保护继电器建模 (Protection Relay Modeling)"
type: topic
tags: [protection, relay, distance-protection, differential-protection, traveling-wave, fault-detection, wavelet, high-frequency-protection]
created: "2026-05-01"
updated: "2026-05-19"
---

# 保护继电器建模 (Protection Relay Modeling)

## 定义与边界

保护继电器建模是在 EMT 仿真中表示测量链、判据算法、逻辑闭锁、通信延迟和跳闸接口的建模工作。它不是继电保护整定手册，也不能只用"速动性""可靠性"这类目标词证明模型有效——保护结论必须绑定故障类型、采样率、滤波算法、互感器模型、断路器模型和一次系统模型。

保护继电器在 EMT 中的定位可抽象为一个四层架构：

1. **测量链层**（传感器 → 信号调理 → A/D 转换）：CT/CVT 暂态模型、合并单元采样、滤波延迟
2. **信号处理层**（特征提取）：工频相量提取（傅里叶/微分方程）、暂态特征提取（行波/小波）、高频阻抗计算
3. **判据算法层**（判决逻辑）：距离判据、差动判据、行波启动/区段识别、奇异熵判据
4. **执行接口层**（动作输出）：断路器跳闸/重合闸/闭锁命令 → 拓扑变更 → EMT 网络方程更新

本页关注保护继电器如何进入 [[emt-simulation]]。具体设备模型可阅读 [[protection-control-device]]（保护控制装置）、[[differential-protection]]（差动保护）、[[distance-relay]]（距离保护），故障注入和线路暂态可阅读 [[fault-analysis-methods]]（故障分析方法）、[[distributed-parameter-line]]（分布参数线路）和 [[transmission-line-theory]]（输电线路理论）。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 580" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="900" height="580" fill="#ffffff"/>
  
  <!-- Title -->
  <text x="450" y="28" text-anchor="middle" font-size="14" font-weight="bold" fill="#1a1a2e">图1 · 保护继电器 EMT 建模四层架构</text>
  
  <!-- Layer 1: 测量链 (Blue) -->
  <rect x="40" y="50" width="820" height="90" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="60" y="75" font-size="13" font-weight="bold" fill="#1e40af">测量链层</text>
  <text x="60" y="95" font-size="11" fill="#374151">CT/CVT暂态建模 · 合并单元采样 · 滤波延迟 · A/D转换</text>
  
  <!-- CT/CVT boxes -->
  <rect x="80" y="105" width="130" height="28" rx="4" fill="#bfdbfe" stroke="#2563eb" stroke-width="1"/>
  <text x="145" y="123" text-anchor="middle" font-size="10" fill="#1e40af">CT饱和模型</text>
  <rect x="230" y="105" width="130" height="28" rx="4" fill="#bfdbfe" stroke="#2563eb" stroke-width="1"/>
  <text x="295" y="123" text-anchor="middle" font-size="10" fill="#1e40af">CVT暂态响应</text>
  <rect x="380" y="105" width="130" height="28" rx="4" fill="#bfdbfe" stroke="#2563eb" stroke-width="1"/>
  <text x="445" y="123" text-anchor="middle" font-size="10" fill="#1e40af">合并单元</text>
  <rect x="530" y="105" width="130" height="28" rx="4" fill="#bfdbfe" stroke="#2563eb" stroke-width="1"/>
  <text x="595" y="123" text-anchor="middle" font-size="10" fill="#1e40af">抗混叠滤波</text>
  <rect x="680" y="105" width="130" height="28" rx="4" fill="#bfdbfe" stroke="#2563eb" stroke-width="1"/>
  <text x="745" y="123" text-anchor="middle" font-size="10" fill="#1e40af">A/D采样</text>
  
  <!-- Arrows L1→L2 -->
  <line x1="450" y1="140" x2="450" y2="162" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Layer 2: 信号处理 (Green) -->
  <rect x="40" y="165" width="820" height="90" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="60" y="190" font-size="13" font-weight="bold" fill="#166534">信号处理层</text>
  <text x="60" y="210" font-size="11" fill="#374151">工频相量提取 · 暂态特征提取（行波/小波） · 高频阻抗计算</text>
  
  <rect x="80" y="220" width="150" height="28" rx="4" fill="#bbf7d0" stroke="#16a34a" stroke-width="1"/>
  <text x="155" y="238" text-anchor="middle" font-size="10" fill="#166534">半周期傅里叶滤波</text>
  <rect x="250" y="220" width="150" height="28" rx="4" fill="#bbf7d0" stroke="#16a34a" stroke-width="1"/>
  <text x="325" y="238" text-anchor="middle" font-size="10" fill="#166534">复数微分方程阻抗</text>
  <rect x="420" y="220" width="150" height="28" rx="4" fill="#bbf7d0" stroke="#16a34a" stroke-width="1"/>
  <text x="495" y="238" text-anchor="middle" font-size="10" fill="#166534">二进小波WTMM</text>
  <rect x="590" y="220" width="150" height="28" rx="4" fill="#bbf7d0" stroke="#16a34a" stroke-width="1"/>
  <text x="665" y="238" text-anchor="middle" font-size="10" fill="#166534">小波奇异熵WSE</text>
  <rect x="760" y="220" width="90" height="28" rx="4" fill="#bbf7d0" stroke="#16a34a" stroke-width="1"/>
  <text x="805" y="238" text-anchor="middle" font-size="10" fill="#166534">高频阻抗</text>
  
  <!-- Arrows L2→L3 -->
  <line x1="450" y1="255" x2="450" y2="277" stroke="#16a34a" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Layer 3: 判据算法 (Yellow) -->
  <rect x="40" y="280" width="820" height="90" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="60" y="305" font-size="13" font-weight="bold" fill="#92400e">判据算法层</text>
  <text x="60" y="325" font-size="11" fill="#374151">距离保护判据 · 差动保护判据 · 行波区段识别 · 暂态保护启动/跳闸</text>
  
  <rect x="80" y="335" width="140" height="28" rx="4" fill="#fde68a" stroke="#d97706" stroke-width="1"/>
  <text x="150" y="353" text-anchor="middle" font-size="10" fill="#92400e">正序阻抗距离判据</text>
  <rect x="240" y="335" width="140" height="28" rx="4" fill="#fde68a" stroke="#d97706" stroke-width="1"/>
  <text x="310" y="353" text-anchor="middle" font-size="10" fill="#92400e">WTMM区内外判据</text>
  <rect x="400" y="335" width="140" height="28" rx="4" fill="#fde68a" stroke="#d97706" stroke-width="1"/>
  <text x="470" y="353" text-anchor="middle" font-size="10" fill="#92400e">WSE启动+跳闸判据</text>
  <rect x="560" y="335" width="140" height="28" rx="4" fill="#fde68a" stroke="#d97706" stroke-width="1"/>
  <text x="630" y="353" text-anchor="middle" font-size="10" fill="#92400e">高频距离判据</text>
  <rect x="720" y="335" width="130" height="28" rx="4" fill="#fde68a" stroke="#d97706" stroke-width="1"/>
  <text x="785" y="353" text-anchor="middle" font-size="10" fill="#92400e">累积差动偏差</text>
  
  <!-- Arrows L3→L4 -->
  <line x1="450" y1="370" x2="450" y2="392" stroke="#d97706" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Layer 4: 执行接口 (Purple) -->
  <rect x="40" y="395" width="820" height="90" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="60" y="420" font-size="13" font-weight="bold" fill="#5b21b6">执行接口层</text>
  <text x="60" y="440" font-size="11" fill="#374151">跳闸/闭锁/重合闸命令 · 断路器状态变更 · EMT网络拓扑更新</text>
  
  <rect x="80" y="450" width="130" height="28" rx="4" fill="#ddd6fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="145" y="468" text-anchor="middle" font-size="10" fill="#5b21b6">Trip跳闸命令</text>
  <rect x="230" y="450" width="130" height="28" rx="4" fill="#ddd6fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="295" y="468" text-anchor="middle" font-size="10" fill="#5b21b6">Block闭锁命令</text>
  <rect x="380" y="450" width="130" height="28" rx="4" fill="#ddd6fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="445" y="468" text-anchor="middle" font-size="10" fill="#5b21b6">Reclose重合闸</text>
  <rect x="530" y="450" width="130" height="28" rx="4" fill="#ddd6fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="595" y="468" text-anchor="middle" font-size="10" fill="#5b21b6">断路器状态更新</text>
  <rect x="680" y="450" width="130" height="28" rx="4" fill="#ddd6fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="745" y="468" text-anchor="middle" font-size="10" fill="#5b21b6">导纳矩阵重建</text>
  
  <!-- Bottom: 一次系统故障注入 -->
  <rect x="40" y="505" width="820" height="55" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="60" y="530" font-size="13" font-weight="bold" fill="#991b1b">一次系统</text>
  <text x="60" y="550" font-size="11" fill="#374151">故障注入（短路/接地/断开）→ EMT暂态仿真 → 节点电压/支路电流 → 测量链输入</text>
  
  <!-- Arrow from fault to CT -->
  <line x1="450" y1="505" x2="450" y2="140" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#arrowRed)"/>
  
  <!-- Arrow definitions -->
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#555"/>
    </marker>
    <marker id="arrowRed" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#dc2626"/>
    </marker>
  </defs>
  
  <!-- Legend -->
  <rect x="700" y="55" width="150" height="75" rx="4" fill="#f9f9f9" stroke="#ddd" stroke-width="1"/>
  <text x="710" y="73" font-size="10" font-weight="bold" fill="#333">图例</text>
  <rect x="710" y="82" width="14" height="10" fill="#dbeafe" stroke="#2563eb"/>
  <text x="730" y="91" font-size="9" fill="#555">测量链层</text>
  <rect x="710" y="97" width="14" height="10" fill="#dcfce7" stroke="#16a34a"/>
  <text x="730" y="106" font-size="9" fill="#555">信号处理层</text>
  <rect x="710" y="112" width="14" height="10" fill="#fef3c7" stroke="#d97706"/>
  <text x="730" y="121" font-size="9" fill="#555">判据算法层</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 保护继电器 EMT 建模四层架构</p>

## EMT 中的作用

保护继电器模型在 EMT 中的核心价值在于揭示**测量链对保护判据的影响**以及**保护动作对系统暂态的反作用**：

- **检查测量链非理想特性的影响**：CT 饱和、CVT 暂态响应、直流偏置、谐波和行波信号对保护判据的影响需要在 EMT 仿真中显式建模
- **验证保护判据的动作边界**：距离保护、差动保护、纵联保护、行波保护在各种故障场景（故障类型、故障电阻、故障位置、信噪比）下的动作边界
- **与 [[real-time-simulation]] 和 [[hil-simulation]] 结合**：形成硬件在环（HIL）或控制器硬件在环（CHIL）测试平台
- **闭环保护动作**：跳闸、重合闸、闭锁或后备保护启动后，将保护动作反馈到一次系统，形成保护-电网闭环交互

## 主要分支与机制

保护继电器在 EMT 中的建模方法按**输入信号类型**可分为四大分支：

### 2.1 测量链建模

互感器（CT/CVT）的暂态特性直接影响继电器输入信号的保真度。

**CT 饱和模型**：采用 Type 96 伪非线性磁滞电感模拟铁芯饱和特性。磁链更新采用梯形积分：

$$\psi_{k+1} = \psi_k + \Delta t \cdot (v_s - R_s i_s)_k$$

其中 $v_s$ 为二次电压，$R_s$ 为二次绕组电阻，$i_s$ 为二次电流。当 $|\psi| > \psi_{\text{sat}}$ 时铁芯进入饱和区，二次电流传变误差可达 40%~60%（Chaudhary 2004）。

**CVT 暂态响应**：电容式电压互感器在高压侧失压后存在剩余电压瞬变过程，衰减时间常数与一次系统参数相关。EMTP 中使用线性电路模型模拟，剩余电压衰减时间常数与 TNA 结果对比误差 < 5%（Chaudhary 2004）。

若测量链简化，保护动作时间和误动/拒动结论应降级。CT 饱和可用 Type 96 伪非线性磁滞电感模拟；CVT 暂态响应会影响距离保护阻抗测量精度，简化测量链应在结论中明确标注。

### 2.2 工频量保护建模

距离、过流、差动和方向元件从电压电流基波量或序分量计算判据，适合与 [[phasor-measurement-unit]]（相量测量单元）和 [[symmetrical-components]]（对称分量法）衔接。

**基于对称分量的复数微分方程距离保护**（Rosołowski 1997）：利用半周期非递归傅里叶滤波器提取对称分量，构建等效故障回路复数微分方程：

$$\underline{v}(t) = R_1 \underline{i}_{LR}(t) + L_1 \frac{d\underline{i}_{LL}(t)}{dt} + \underline{v}_{ef}(t)$$

方程拆分为实部与虚部两个代数方程，仅需单个采样时刻数据即可直接解算正序电阻 $R_1$ 与电感 $L_1$，无需迭代或历史数据窗。采样率 1 kHz 下，单点阻抗解算计算延迟 < 1 ms，适合实时 DSP 实现。测距响应时间稳定在半个周波（10 ms）以内，满足超高速保护要求。高阻故障（$R_f = 50\ \Omega$）检测时间：近端母线 2 ms，远端母线 7 ms。

**平行线路故障选线判据**：

$$\left| \underline{v}_A \right| - \left| \underline{v}_B \right| > \Delta v$$

通过比较双回线等效压降幅值差识别故障线路，实现高阻工况下可靠选线。

### 2.3 暂态量保护建模

暂态量保护利用故障产生的高频行波或小波奇异熵特征，在 EMT 中建模的核心是**采样率**和**数据窗设计**。

#### 2.3.1 小波奇异熵暂态保护（Liu 2009）

区内故障产生宽频带阶跃信号，高频分量丰富，小波奇异熵值 $W_s$ 较大；区外故障高频分量受母线杂散电容和阻波器衰减，$W_s$ 较小。

保护启动判据：$W_s > \alpha$（$\alpha$ 为含可靠系数的门槛值）

区内故障跳闸判据：$W_s > k_{\text{set}}$（$k_{\text{set}}$ 需满足 $\max(W_{s,\text{ext}}) < k_{\text{set}} < \min(W_{s,\text{int}})$）

相继速动逻辑：故障后第 3 个周期（约 60 ms）开始计算基准阈值，检测对侧断路器跳闸引起的微弱电容电流突变。当母线对地等效电容 $C_m < 0.015\ \mu\text{F}$ 时，可靠区分线路末端故障与反向出口故障。DB4 小波 4 层分解，采样频率 $\geq 200$ kHz，数据窗 100 点（对应 0.5 ms）。

#### 2.3.2 行波保护（Pei 2019）

基于模电压行波特征的超高速保护，利用二进小波变换提取模极大值（WTMM）。

**保护启动判据**（一模电压行波幅值变化）：

$$\Delta u_1(k) = \left| u_1(k) - u_1(k-1) \right| > TH_1$$

**故障区段识别判据**：

$$\text{WTMM}_{u1r} > TH_2 \implies \text{区内故障}$$

**故障极选择判据**（0 模 WTMM 极性）：

$$
f = \begin{cases}
\text{正极接地} & \text{WTMM}_{u0r} < -TH_3 \\
\text{负极接地} & \text{WTMM}_{u0r} > TH_3 \\
\text{极间短路} & \text{others}
\end{cases}
$$

张北 ±500 kV 四端环形 VSC 直流电网验证：保护动作数据窗仅 0.512 ms（256 点 @ 500 kHz）；区内故障 1 模 WTMM（128.9）与区外故障（< 0.5）幅值差异超 250 倍，区段识别裕度极大；在 400 Ω 过渡电阻及 20 dB 高斯白噪声条件下，故障极选择准确率 100%。

#### 2.3.3 双回线路单端行波保护（Zhang 2017）

利用双回线路健康回线的耦合信息实现单端保护，采用双采样率架构。

**回路检测判据**：$I_{k,p} \geq I_{\text{th}}$（$I_{\text{th}} = 5\%$ 额定电流，消除单回运行时相间耦合影响）

**内部扰动启动判据**（累积交叉差动电流偏差）：

$$\sum_{t}^{t+\varepsilon} i_{\text{diff}}(t) = \sum_{t}^{t+\varepsilon} \left[ i_{1,p}(t) - i_{2,p}(t) \right] \geq I_{\text{op}}$$

其中 $\varepsilon = 3$ ms，$I_{\text{op}} = 10\%$ 额定电流。

**故障距离判据**：

$$x_m \leq \frac{v \cdot \Delta t}{2 \cdot k_2}$$

其中 $k_2 = 1.05$ 考虑线路参数（弧垂和行波速度）5% 误差，消除近端故障死区。高频采样率 64 kHz，低频采样率 10 kHz，在计算负担与检测精度间取得平衡。

### 2.4 柔性直流配电网高频距离保护（Jia 2019）

针对 VSC 型换流器等效阻抗随时变控制策略变化的难题，将换流器在高频段（1000~1600 Hz）等效为仅与物理参数相关的恒定阻抗模型。

**CDSM-MMC 高频恒定阻抗**：

$$Z_{S\text{-MMC}} = \frac{1}{3}\left( 2R_{\text{arm}} + 2j\omega L_0 + \frac{N}{j\omega C_0} \right)$$

其中 $N$ 为子模块数，$L_0$ 为桥臂电感，$C_0$ 为子模块电容。在 1000 Hz 频率下，上下桥臂阻抗分别为 93.36 Ω 与 94 Ω，相对差异 < 1%。

**高频距离保护动作电压**：

$$\Delta U_{\text{op}} = \Delta U - \Delta I \cdot Z_{\text{set}}$$

区内故障动作判据：$\Delta U_{\text{op}} \geq U_{k[0]}$（动作电压幅值大于等于故障点高频电动势阈值）

±10 kV 六端柔性直流配电网验证：平均动作延时 < 3 ms，高频恒定阻抗模型有效克服换流器控制策略导致的阻抗时变问题；在 1000~1600 Hz 频段内，换流器开关状态对阻抗的非线性影响可忽略不计，模型误差 < 2%。

### 2.5 EMT 闭环保护系统集成（Chaudhary 2004）

EMTP 中保护系统的闭环集成框架，实现"系统暂态计算—互感器变换—继电器算法处理—保护决策反馈—系统状态更新"的完整闭环。

核心节点电压方程：

$$[G] \mathbf{V}_{\text{node}}(t) = \mathbf{I}_{\text{node}}(t)$$

其中 $[G]$ 为实系数节点导纳矩阵，随断路器状态（跳闸/重合）动态更新。FORTRAN 接口支持每时步数据交换，典型仿真步长 50~100 μs 时，继电器算法处理延迟 < 1 μs，满足实时性要求。230 kV 输电系统验证：严重饱和工况下二次电流传变误差达 40%~60%，持续 3~5 个工频周期。

## 量化性能边界

| 方法 | 采样率 | 数据窗 | 动作时间 | 关键量化指标 | 来源 |
|------|--------|--------|----------|-------------|------|
| 对称分量复数微分方程距离保护 | 1 kHz | 半周期(10 ms) | < 10 ms | 测距误差 < 1%；高阻故障(50 Ω)检测 2~7 ms | Rosołowski 1997 |
| 小波奇异熵暂态保护 | ≥ 200 kHz | 0.5 ms (100 点) | 第 3 周期起算(≈60 ms) | $C_m < 0.015\ \mu\text{F}$ 时可靠区分末端/出口故障 | Liu 2009 |
| 行波保护(VSC-DC) | 500 kHz | 0.512 ms (256 点) | < 0.512 ms | 区内/区外 WTMM 差异 > 250 倍；400 Ω 过渡电阻、20 dB 噪声下准确率 100% | Pei 2019 |
| 双回线路行波保护 | 10+64 kHz | 3 ms | < 相量保护 | k₂=1.05 裕度消除近端死区；CT/CCVT 免疫 | Zhang 2017 |
| 高频距离保护(DC) | — | 数 ms | < 3 ms | 高频阻抗误差 < 2%；1000~1600 Hz 频段内模型准确 | Jia 2019 |
| EMTP 闭环保护集成 | — | 每时步 | — | 严重饱和下传变误差 40%~60%；FORTRAN 接口延迟 < 1 μs | Chaudhary 2004 |

## 适用边界与失效模式

- **CT 饱和未建模时**：不应给出保护动作时间或选择性的强结论。严重饱和（剩磁 > 80% 饱和磁通）下二次电流传变误差可达 60%~80%，保护判据可能误动或拒动
- **只用工频模型**：可能遗漏行波、高频暂态、直流分量和换流器限流造成的保护风险
- **行波保护和直流保护**：不能从单一线路长度、故障电阻或采样率外推到所有电网
- **HIL 测试结果**：还受接口延迟、数模转换、放大器带宽和实际装置固件影响，应与仿真模型边界分开报告
- **小波奇异熵方法**：当母线对地等效电容 $C_m \geq 0.015\ \mu\text{F}$ 时，区内外熵值差异减小，可靠性下降
- **高频距离保护**：频段选择（1000~1600 Hz）需与换流器开关频率解耦，当开关谐波落在保护频段内时等效模型失效

## 相关页面

- [[relay-protection]] 是继电保护主题页；本页聚焦 EMT 建模方法和验证边界
- [[distance-relay]] 和 [[differential-protection]] 是模型页，承载具体保护元件的结构
- [[protection-control-device]] 讨论保护控制装置的通用建模框架
- [[wide-area-monitoring-protection]] 讨论广域测量和控制闭环，涉及通信和系统级动作
- [[fault-analysis]] 与 [[fault-analysis-methods]] 提供故障场景和故障注入方法
- [[sequence-network-model]] 提供序网模型在故障分析中的应用
- [[symmetrical-components]] 提供对称分量法的理论基础
- [[impedance-relay]] 讨论阻抗继电器的算法细节

## 来源论文

- [[a-new-distance-relaying-algorithm-based-on-complex-differential-equation-for-sym|Rosołowski 1997]] — 半周期傅里叶+对称分量复数微分方程距离保护，1 kHz 采样，10 ms 内测距误差 < 1%，高阻故障 50 Ω 检测 2~7 ms
- [[a-novel-ultra-high-speed-traveling-wave-protection-principle-for-vsc-based-dc-gr|Pei 2019]] — VSC 直流电网模电压行波保护，500 kHz 采样，0.512 ms 超高速动作，250 倍区内外 WTMM 差异，400 Ω/20 dB 噪声下 100% 准确率
- [[distance-protection-scheme-for-dc-distribution-systems-based-on-the-high-frequen|Jia 2019]] — 柔性直流配电网高频距离保护，1000~1600 Hz 换流器恒定阻抗模型，动作延时 < 3 ms，模型误差 < 2%
- [[application-of-wavelet-singular-entropy-theory-in-transient-protection-and-accel|Liu 2009]] — 小波奇异熵暂态保护，200 kHz 采样，0.5 ms 数据窗，DB4 小波 4 层分解，全线相继速动无通信通道
- [[single-ended-travelling-wave-based-protection-scheme-for-double-circuit-transmis|Zhang 2017]] — 双回线路单端行波保护，10+64 kHz 双采样率，累积交叉差动偏差确认，k₂=1.05 裕度消除死区
- [[protection-system-representation-in-the-electromagnetic-transients-program-power|Chaudhary 2004]] — EMTP 闭环保护系统集成框架，CT/CVT 暂态模型，FORTRAN 接口，继电器算法处理延迟 < 1 μs