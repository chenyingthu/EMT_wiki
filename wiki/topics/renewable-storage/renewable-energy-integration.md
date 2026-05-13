---
title: "可再生能源并网 (Renewable Energy Integration)"
type: topic
tags: [renewable-energy, integration, grid-connection, wind, solar, low-voltage-ride-through, grid-forming, grid-following, ibm, emt]
created: "2026-05-02"
updated: "2026-05-14"
---

# 可再生能源并网 (Renewable Energy Integration)

## 定义

可再生能源并网是指风电、光伏、储能等新能源发电单元通过电力电子变流器、变压器、集电网络和控制保护系统接入交流电网的技术体系。在 EMT Wiki 中，本页关注新能源并网设备在**电磁暂态（EMT）域**内的建模边界、控制交互、稳定性问题和仿真方法，而非装机容量统计、政策评价或市场收益。

可再生能源并网不是单个机组模型的简单叠加。风电（DFIG/PMSG/全功率变流器）、光伏（PV阵列+逆变器）、储能（BESS+双向变流器）、跟网型（GFL）和构网型（GFM）逆变器各自有不同的证据边界，场站聚合、集电网络谐振、宽频振荡等又涉及更高层级的系统行为。这些内容在 [[renewable-energy-units]]、[[pv-power-plant]]、[[inverter-model]]、[[gfl-inverter-model]]、[[gfm-inverter-model]] 和 [[bess-model]] 中有各自独立的建模讨论。

新能源并网的核心挑战在于：**电力电子接口取代了同步机的惯性支撑，系统的动态特性从"机电惯性主导"转变为"控制环路+电力电子开关频率"主导的多时间尺度耦合**。这要求 EMT 仿真同时覆盖 μs 级的开关暂态、ms 级的控制环路响应、以及秒级的功率平衡过程。

## EMT 中的作用

EMT 仿真在可再生能源并网分析中承担以下不可替代的角色：

- **弱网条件下的控制交互**：当短路比（SCR）低于 3 时，PLL、电流内环、限流器（current limiter）、无功/电压控制之间的耦合会产生宽频振荡（0.1 Hz ~ 10 kHz）。EMT 是唯一能同时解析 PLL 动态、PWM 开关和谐波注入的仿真域。
- **低/高电压穿越（LVRT/HVRT）与保护配合**：故障期间变流器的电流限幅、无功支撑、故障后恢复逻辑涉及非线性饱和和模式切换，相量域仿真无法准确复现。
- **多逆变器谐波与阻抗耦合**：集电线路的分布参数、滤波器谐振、多逆变器并联运行的阻抗相互作用，需要在 EMT 中通过频域阻抗扫描 + 时域验证的联合方法识别。
- **构网型控制的电压/频率支撑**：GFM 逆变器以电压源或下垂/虚拟同步机制参与系统支撑，其故障电流注入、黑启动能力、与 GFL 逆变器的功率分配需要在 EMT 中验证。
- **大规模场站的并行仿真**：当场站包含数千个 PV 模块或数百台 DFIG 时，EMT 仿真规模急剧膨胀，需要 GLIM（广义延迟插入法）、GPU 加速、多速率仿真等技术支撑。

## 新能源并网的核心机制

### 1. 跟网型（GFL）与构网型（GFM）控制架构

新能源并网的控制架构分为两大阵营，其核心差异在于**并网点电压的生成方式**：

**跟网型（Grid-Following, GFL）**：依赖外部电网电压作为同步参考，通过 PLL 提取电网相位，以电流源形式注入功率。其核心方程为：

$$i^{\star} = C(v_{\mathrm{pcc}}, P^{\star}, Q^{\star}, x_c)$$

$$i = \mathrm{sat}(i^{\star}, I_{\max})$$

$$Y_{\mathrm{grid}} v_{\mathrm{pcc}} = i + i_{\mathrm{net}}$$

其中 $C(\cdot)$ 是控制器（含 PLL、外环功率/电压控制、内环电流控制），$x_c$ 是控制状态变量，$I_{\max}$ 是限流边界。GFL 的关键边界在于：弱网条件下 PLL 带宽与短路比的匹配关系、故障期间的限流逻辑（内限 vs 外限）、以及故障后 PLL 重新锁定的瞬态过程。

**构网型（Grid-Forming, GFM）**：不依赖外部 PLL，通过下垂控制（droop）、虚拟同步机（VSG）或增强电压调节（EVR）等机制自主建立电压幅值和频率。其核心特征包括：

- **下垂控制**：$P = P_{\mathrm{ref}} - k_p(\omega - \omega_{\mathrm{ref}})$，$Q = Q_{\mathrm{ref}} - k_q(V - V_{\mathrm{ref}})$
- **虚拟同步机**：模拟同步机的摇摆方程 $M\frac{d\omega}{dt} = P_{\mathrm{ref}} - P_{\mathrm{out}} - D(\omega - \omega_{\mathrm{ref}})$
- **故障电流注入**：GFM 在故障期间可同时提供有功和无功支撑，其最大输出受 PWM 饱和和额定电流双重约束

Nurunnabi 2025 的 EMT 仿真表明，EVR 和 CPID（受比例积分下垂）策略在动态负载和故障条件下显著优于传统下垂方法，电压恢复时间缩短约 40%，频率偏差降低约 35%。

### 2. 风电并网：DFIG 与 PMSG 的 EMT 建模差异

**DFIG（双馈感应发电机，Type-3）**：转子通过背靠背变流器（RSC + GSC）与电网连接，变流器仅处理约 30% 的额定功率（滑差功率）。DFIG 的 EMT 建模需要同时解析：

- 转子侧变流器（RSC）的磁场定向控制（FOC）
- 电网侧变流器（GSC）的直流电压支撑和无功控制
- 三相三绕组变压器的集电网络
- 动态电压恢复器（DVR）等补偿装置

DFIG 的宽频动态特性在 Hussein 2016 中通过**宽频等效模型**（Wideband Equivalent Model）进行了系统建模：静态频率 dependent 网络等效（FDNE）表示集电网络和无源元件，动态低频等效（DLFE）表示聚合的 DFAG 及其局部控制。该模型在 PSCAD/EMTDC 中验证，计算时间减少约 85%，同时保持了终端响应的准确性。

**PMSG（永磁同步发电机，Type-4）**：全功率变流器架构，转子与电网完全解耦。PMSG 的 EMT 建模重点在于：

- 机侧变流器的最大风能追踪（MPPT）控制
- 网侧变流器的直流电压稳定和无功控制
- 全功率变流器的故障电流注入能力（可达 1.5~2.0 p.u.）

### 3. 光伏并网：从组件到场站的层级建模

光伏并网的 EMT 建模具有**层级嵌套**特征：

- **组件级**：PV 阵列的电压-电流关系 $I = I_{\mathrm{ph}} - I_0[\exp(\frac{V + IR_s}{nV_t}) - 1] - \frac{V + IR_s}{R_{sh}}$，包含光照和温度的非线性依赖
- **直流侧**：DC-DC 升压变换器的 MPPT 控制（扰动观察法、增量电导法）
- **逆变级**：DC-AC 逆变器的 PWM 调制和并网控制
- **集电网络**：辐射状馈线、变压器、并联电容器
- **场站控制器（PPC）**：有功/无功功率分配、电压调节、故障穿越

Marthi 2024 在 Oak Ridge National Laboratory 开发了基于 IEEE-39 母线系统的 PV 场站基准模型，包含 3 个不同配置的 PV 场站（125 MW + 125 MW + 250 MW），在 PSCAD 中验证了不同短路比（SCR）条件下的故障动态。

### 4. 场站聚合与等值建模

当场站规模达到数百台机组时，逐一详细建模的 EMT 仿真不可行。场站聚合的核心思路是：**将多台机组等值为单机或少量等值机组，同时保留关键动态特性**。

Li 2022 提出的**结构保持聚合方法**（Structure-Preserving Aggregation）通过递归组合两个 DFIG 并降阶，使聚合后的 DFIG 具有与单机相同的状态变量数量，同时保持稳态响应一致。该方法能够处理不同转速和参数的 DFIG，并通过等效阻抗计入集电线路的功率损耗。在 EMT 仿真中，聚合模型的计算时间减少约 70%，同时准确复现了主导的暂态响应。

Wang 2026 提出了面向 GPU 架构的**组件级细粒度仿真方法**（Component-Level Fine-Grained Simulation），基于 GLIM（广义延迟插入法）将可控源引入传统延迟插入法，使复杂设备的仿真转化为大规模 GLIM 基本拓扑的求解。在 GeForce RTX 3060 GPU 上，该方法实现了大规模风电场的细粒度 EMT 仿真。

## 逆变器建模方法体系（五模型精度-效率映射）

Sano 2022 系统比较了 5 种并网逆变器 EMT 建模方法，建立了精度-效率映射框架：

| 模型 | 缩写 | 时间步长 | 加速比 | 精度误差 | 适用场景 | 失效场景 |
|------|------|----------|--------|----------|----------|----------|
| 开关模型 | SW | 1~5 μs | 1×（基准） | < 0.5% | PWM 谐波分析、子模块动态、保护瞬时电流 | 大规模系统（计算量过大） |
| 电压插值模型 | VI | 10~50 μs | 10~50× | 2~5% | 粗略暂态分析、机电耦合仿真 | 谐波分析、快速限流过程 |
| 平均值模型 | AV | 50~200 μs | 50~200× | 5~15% | 场站聚合、控制交互筛查 | PWM 谐波、直流侧纹波 |
| 受控电流注入模型 | CCI | 20~100 μs | 20~100× | 1~3% | 控制稳定性分析、宽频振荡 | 开关瞬态、故障电流峰值 |
| 简化电流注入模型 | SCI | 50~500 μs | 50~500× | 3~10% | 大规模系统实时仿真 | 弱网条件、故障穿越 |

**关键发现**：

1. **SW 模型**能表示所有动态行为，但时间步长必须 ≤ 5 μs 以解析 PWM 开关，导致大规模系统仿真时间呈指数增长。
2. **VI 模型**通过线性插值近似开关动作，在电压暂态分析中精度可接受（误差 < 5%），但无法表示 PWM 谐波频谱。
3. **AV 模型**是最常用的简化模型，将 PWM 开关的平均值作为输出，适用于控制环路分析，但丢失了开关频率附近的动态。
4. **CCI 模型**通过受控电流源注入功率，保留了控制动态和一定的频率响应，是控制稳定性分析的最佳折中。
5. **SCI 模型**进一步简化，仅保留直流电压动态和功率注入，适用于大规模系统的实时仿真。

## 形式化表达

### 并网逆变器通用接口方程

并网逆变器和电网接口可抽象为控制器、限流器和网络方程的耦合：

$$i^{\star} = C(v_{\mathrm{pcc}}, P^{\star}, Q^{\star}, x_c)$$

$$i = \mathrm{sat}(i^{\star}, I_{\max})$$

$$Y_{\mathrm{grid}} v_{\mathrm{pcc}} = i + i_{\mathrm{net}}$$

其中 $C(\cdot)$ 是控制器（含 PLL、外环、内环），$x_c$ 是控制状态，$I_{\max}$ 是限流边界，$v_{\mathrm{pcc}}$ 是并网点电压。

### DFIG 聚合模型的状态方程

Li 2022 的聚合 DFIG 保留了单机 DFIG 的状态变量结构：

$$\frac{d\lambda_{dr}}{dt} = -\frac{R_r}{L_r}\lambda_{dr} + \frac{R_r}{L_r}L_m i_{ds} - s\omega_r \lambda_{qr} + v_{dr}$$

$$\frac{d\lambda_{qr}}{dt} = -\frac{R_r}{L_r}\lambda_{qr} + \frac{R_r}{L_r}L_m i_{qs} - s\omega_r \lambda_{dr} + v_{qr}$$

聚合过程中，通过递归组合两个 DFIG 并降阶，使聚合模型的状态变量数与单机相同，但等效参数（$R_r, L_r, L_m$）根据容量权重和集电网络阻抗调整。

### GFM 虚拟同步机摇摆方程

$$M\frac{d\omega}{dt} = P_{\mathrm{ref}} - P_{\mathrm{out}} - D(\omega - \omega_{\mathrm{ref}})$$

$$M\frac{d\delta}{dt} = \omega - \omega_{\mathrm{ref}}$$

$$V_{\mathrm{ref}} = V_0 - k_q(Q - Q_{\mathrm{ref}})$$

其中 $M$ 为惯性常数，$D$ 为阻尼系数，$k_q$ 为无功下垂系数。

### PV 阵列的 I-V 特性

$$I = I_{\mathrm{ph}}(G, T) - I_0(T)\left[\exp\left(\frac{V + IR_s}{nV_t}\right) - 1\right] - \frac{V + IR_s}{R_{sh}}$$

其中 $I_{\mathrm{ph}}$ 是光生电流（依赖光照 $G$），$I_0$ 是饱和电流（依赖温度 $T$），$V_t = \frac{kT}{q}$ 是热电压。


<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 1000 620" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
    <marker id="arrow-red" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#dc2626"/>
    </marker>
  </defs>
  
  <!-- Title -->
  <text x="500" y="28" text-anchor="middle" font-size="18" font-weight="bold" fill="#1a1a1a" font-family="sans-serif">可再生能源并网 EMT 仿真方法体系</text>
  
  <!-- Layer 1: 新能源机组类型 (输入层) -->
  <text x="80" y="65" font-size="13" font-weight="bold" fill="#666" font-family="sans-serif">新能源机组</text>
  
  <!-- Wind DFIG -->
  <rect x="140" y="50" width="160" height="40" rx="6" ry="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="220" y="75" text-anchor="middle" font-size="13" fill="#1e3a5f" font-family="sans-serif">DFIG (Type-3)</text>
  
  <!-- Wind PMSG -->
  <rect x="340" y="50" width="160" height="40" rx="6" ry="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="420" y="75" text-anchor="middle" font-size="13" fill="#1e3a5f" font-family="sans-serif">PMSG (Type-4)</text>
  
  <!-- PV -->
  <rect x="540" y="50" width="160" height="40" rx="6" ry="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="620" y="75" text-anchor="middle" font-size="13" fill="#1e3a5f" font-family="sans-serif">光伏阵列+逆变器</text>
  
  <!-- BESS -->
  <rect x="740" y="50" width="160" height="40" rx="6" ry="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="820" y="75" text-anchor="middle" font-size="13" fill="#1e3a5f" font-family="sans-serif">储能 (BESS)</text>
  
  <!-- Arrows from Layer 1 to Layer 2 -->
  <line x1="220" y1="90" x2="280" y2="140" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="420" y1="90" x2="420" y2="140" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="620" y1="90" x2="570" y2="140" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="820" y1="90" x2="720" y2="140" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Layer 2: 控制架构 (处理层) -->
  <text x="80" y="165" font-size="13" font-weight="bold" fill="#666" font-family="sans-serif">控制架构</text>
  
  <!-- GFL -->
  <rect x="160" y="140" width="200" height="50" rx="6" ry="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="260" y="160" text-anchor="middle" font-size="14" font-weight="bold" fill="#166534" font-family="sans-serif">跟网型 (GFL)</text>
  <text x="260" y="180" text-anchor="middle" font-size="11" fill="#166534" font-family="sans-serif">PLL + 电流源注入</text>
  
  <!-- GFM -->
  <rect x="440" y="140" width="200" height="50" rx="6" ry="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="540" y="160" text-anchor="middle" font-size="14" font-weight="bold" fill="#166534" font-family="sans-serif">构网型 (GFM)</text>
  <text x="540" y="180" text-anchor="middle" font-size="11" fill="#166534" font-family="sans-serif">下垂/VSG/电压源</text>
  
  <!-- 混合 -->
  <rect x="720" y="140" width="200" height="50" rx="6" ry="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="820" y="160" text-anchor="middle" font-size="14" font-weight="bold" fill="#166534" font-family="sans-serif">混合运行</text>
  <text x="820" y="180" text-anchor="middle" font-size="11" fill="#166534" font-family="sans-serif">GFM + GFL 功率分配</text>
  
  <!-- Arrows from Layer 2 to Layer 3 -->
  <line x1="260" y1="190" x2="200" y2="250" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="540" y1="190" x2="450" y2="250" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="820" y1="190" x2="700" y2="250" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Layer 3: 逆变器建模层级 (算法层) -->
  <text x="80" y="275" font-size="13" font-weight="bold" fill="#666" font-family="sans-serif">逆变器建模层级</text>
  
  <!-- SW -->
  <rect x="130" y="250" width="140" height="45" rx="6" ry="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="200" y="270" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e" font-family="sans-serif">SW 开关模型</text>
  <text x="200" y="288" text-anchor="middle" font-size="10" fill="#92400e" font-family="sans-serif">1~5 μs · 精度 &lt;0.5%</text>
  
  <!-- CCI -->
  <rect x="310" y="250" width="140" height="45" rx="6" ry="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="380" y="270" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e" font-family="sans-serif">CCI 受控电流注入</text>
  <text x="380" y="288" text-anchor="middle" font-size="10" fill="#92400e" font-family="sans-serif">20~100 μs · 控制动态</text>
  
  <!-- AV -->
  <rect x="490" y="250" width="140" height="45" rx="6" ry="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="560" y="270" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e" font-family="sans-serif">AV 平均值模型</text>
  <text x="560" y="288" text-anchor="middle" font-size="10" fill="#92400e" font-family="sans-serif">50~200 μs · 场站聚合</text>
  
  <!-- SCI -->
  <rect x="670" y="250" width="140" height="45" rx="6" ry="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="740" y="270" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e" font-family="sans-serif">SCI 简化电流注入</text>
  <text x="740" y="288" text-anchor="middle" font-size="10" fill="#92400e" font-family="sans-serif">50~500 μs · 实时仿真</text>
  
  <!-- VI (smaller, below) -->
  <rect x="850" y="250" width="140" height="45" rx="6" ry="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="920" y="270" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e" font-family="sans-serif">VI 电压插值</text>
  <text x="920" y="288" text-anchor="middle" font-size="10" fill="#92400e" font-family="sans-serif">10~50 μs · 粗略暂态</text>
  
  <!-- Arrows from Layer 3 to Layer 4 -->
  <line x1="200" y1="295" x2="250" y2="360" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="380" y1="295" x2="400" y2="360" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="560" y1="295" x2="550" y2="360" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="740" y1="295" x2="700" y2="360" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="920" y1="295" x2="850" y2="360" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Layer 4: EMT 分析场景 (输出层) -->
  <text x="80" y="385" font-size="13" font-weight="bold" fill="#666" font-family="sans-serif">EMT 分析场景</text>
  
  <!-- Control Interaction -->
  <rect x="140" y="360" width="180" height="50" rx="6" ry="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="230" y="382" text-anchor="middle" font-size="13" font-weight="bold" fill="#4c1d95" font-family="sans-serif">控制交互振荡</text>
  <text x="230" y="400" text-anchor="middle" font-size="10" fill="#4c1d95" font-family="sans-serif">SCR &lt; 3, PLL 动态</text>
  
  <!-- FRT -->
  <rect x="360" y="360" width="180" height="50" rx="6" ry="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="450" y="382" text-anchor="middle" font-size="13" font-weight="bold" fill="#4c1d95" font-family="sans-serif">故障穿越 (LVRT/HVRT)</text>
  <text x="450" y="400" text-anchor="middle" font-size="10" fill="#4c1d95" font-family="sans-serif">非线性限流, 无功支撑</text>
  
  <!-- Harmonic -->
  <rect x="580" y="360" width="180" height="50" rx="6" ry="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="670" y="382" text-anchor="middle" font-size="13" font-weight="bold" fill="#4c1d95" font-family="sans-serif">谐波与阻抗耦合</text>
  <text x="670" y="400" text-anchor="middle" font-size="10" fill="#4c1d95" font-family="sans-serif">集电网络谐振, 宽频振荡</text>
  
  <!-- Aggregation -->
  <rect x="800" y="360" width="180" height="50" rx="6" ry="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="890" y="382" text-anchor="middle" font-size="13" font-weight="bold" fill="#4c1d95" font-family="sans-serif">场站聚合等值</text>
  <text x="890" y="400" text-anchor="middle" font-size="10" fill="#4c1d95" font-family="sans-serif">递归降阶, GLIM, GPU</text>
  
  <!-- Arrows from Layer 4 to Layer 5 -->
  <line x1="230" y1="410" x2="280" y2="480" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="450" y1="410" x2="430" y2="480" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="670" y1="410" x2="580" y2="480" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="890" y1="410" x2="730" y2="480" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- Layer 5: 性能指标 (汇总输出) -->
  <text x="80" y="505" font-size="13" font-weight="bold" fill="#666" font-family="sans-serif">量化性能</text>
  
  <!-- Speedup -->
  <rect x="140" y="480" width="180" height="45" rx="6" ry="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="230" y="500" text-anchor="middle" font-size="13" font-weight="bold" fill="#991b1b" font-family="sans-serif">加速比: 10× ~ 400×</text>
  <text x="230" y="518" text-anchor="middle" font-size="10" fill="#991b1b" font-family="sans-serif">Cheng 2025: ML-GPU 400×</text>
  
  <!-- Accuracy -->
  <rect x="360" y="480" width="180" height="45" rx="6" ry="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="450" y="500" text-anchor="middle" font-size="13" font-weight="bold" fill="#991b1b" font-family="sans-serif">精度: &lt;0.5% ~ 30%</text>
  <text x="450" y="518" text-anchor="middle" font-size="10" fill="#991b1b" font-family="sans-serif">SW &lt;0.5%, 简化模型 10~30%</text>
  
  <!-- Time Reduction -->
  <rect x="580" y="480" width="180" height="45" rx="6" ry="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="670" y="500" text-anchor="middle" font-size="13" font-weight="bold" fill="#991b1b" font-family="sans-serif">计算时间减少: 70% ~ 85%</text>
  <text x="670" y="518" text-anchor="middle" font-size="10" fill="#991b1b" font-family="sans-serif">Hussein 2016: 85%, Li 2022: 70%</text>
  
  <!-- PLL Improvement -->
  <rect x="800" y="480" width="180" height="45" rx="6" ry="6" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="890" y="500" text-anchor="middle" font-size="13" font-weight="bold" fill="#991b1b" font-family="sans-serif">PLL 性能提升: 45% ~ 60%</text>
  <text x="890" y="518" text-anchor="middle" font-size="10" fill="#991b1b" font-family="sans-serif">Ranasinghe 2024: 相位误差 -60%</text>
  
  <!-- Legend -->
  <rect x="350" y="560" width="300" height="45" rx="4" ry="4" fill="#f8f9fa" stroke="#ddd" stroke-width="1"/>
  <text x="370" y="578" font-size="11" fill="#666" font-family="sans-serif">■ 输入/源: 蓝 | ■ 处理/模型: 绿 | ■ 算法/方法: 黄 | ■ 输出/结果: 紫 | ■ 性能指标: 红</text>
  <text x="370" y="596" font-size="10" fill="#999" font-family="sans-serif">数据来源: Sano 2022, Wang 2026, Nurunnabi 2025, Ranasinghe 2024, Cheng 2025, Marthi 2024, Hussein 2016, Li 2022</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 可再生能源并网 EMT 仿真方法体系架构</p>

## 关键技术挑战

### 1. 弱网条件下的控制-网络耦合振荡

当 SCR < 3 时，GFL 逆变器的 PLL 带宽与电网阻抗产生共振。Ranasinghe 2024 提出的**自适应带宽 DSOGI-PLL** 通过瞬态检测器临时冻结 PLL 频率输出，并在扰动期间动态调整 PLL 带宽。EMT 仿真表明，该方法在 SCR = 1.5 的极弱网条件下仍保持稳定，相位误差降低约 60%，PLL 锁定时间缩短约 45%。

### 2. 故障穿越期间的非线性限流

GFL 逆变器在故障期间的限流逻辑涉及多个非线性饱和环节：电流内环限幅、有功功率削减、无功电流注入优先级。Sano 2022 的对比实验显示，简化模型（AV/CCI/SCI）在故障期间的电流峰值误差可达 10~30%，而 SW 模型能精确复现限流过程中的模式切换。

### 3. 大规模场站的并行仿真可扩展性

Cheng 2025 提出的**机器学习增强的 CPU-GPU 大规模并行 EMT 仿真**，通过人工神经网络（GRU）建立数据驱动的 RES 模型，结合实体-组件-系统（ECS）架构，在 IEEE 118 母线系统上实现了 200 万个 RES 实体的仿真，加速比达到 400×（相比传统 CPU 非线性迭代计算）。

### 4. EMT 模型验证与现场数据匹配

Sun 2024（ISO New England）提出了基于**EMT 回放仿真**（Playback Simulation）的 IBR 模型验证方法，使用 PSCAD 回放模块和 GUI 工具，通过模拟数据和真实 Point-On-Wave 数据验证 EMT 模型的准确性。该方法已被纳入 IEEE 2800 标准，要求 EMT 模型在并网前通过验证。

### 5. 构网型与跟网型混合运行的功率分配

GFM 和 GFL 逆变器在同一系统中的混合运行涉及复杂的功率分配和稳定性问题。GFM 提供电压和频率支撑，GFL 跟随电压注入功率。Nurunnabi 2025 的 EMT 仿真和实时硬件验证表明，混合系统中 GFM 的容量占比需要 ≥ 20% 以维持足够的电压支撑，否则 GFL 逆变器的 PLL 可能失步。

## 量化性能边界

| 场景 | 指标 | 数值 | 数据来源 |
|------|------|------|----------|
| DFIG 宽频等效模型（Hussein 2016） | 计算时间减少 | ~85% | PSCAD/EMTDC 验证，Type-3 WPP |
| DFIG 聚合模型（Li 2022） | 计算时间减少 | ~70% | EMT 仿真，多机系统 |
| GFM EVR/CPID 策略（Nurunnabi 2025） | 电压恢复时间缩短 | ~40% | EMT 仿真 + 实时硬件验证 |
| GFM EVR/CPID 策略（Nurunnabi 2025） | 频率偏差降低 | ~35% | EMT 仿真 + 实时硬件验证 |
| 自适应 DSOGI-PLL（Ranasinghe 2024） | 相位误差降低 | ~60% | EMT 仿真，SCR = 1.5 |
| 自适应 DSOGI-PLL（Ranasinghe 2024） | PLL 锁定时间缩短 | ~45% | EMT 仿真，SCR = 1.5 |
| ML 增强并行仿真（Cheng 2025） | 加速比 | 400× | IEEE 118 + 200万 RES 实体 |
| 开关模型 vs 简化模型（Sano 2022） | 故障电流峰值误差 | 10~30% | 5 模型对比实验 |
| PV 场站基准模型（Marthi 2024） | 模型规模 | 3 场站，500 MW 总计 | IEEE-39 母线，PSCAD |
| GLIM 组件级仿真（Wang 2026） | 并行可扩展性 | 大规模风电场 | RTX 3060 GPU |

## 适用边界与选择指南

### 模型选择指南

| 应用场景 | 推荐模型 | 时间步长 | 理由 |
|----------|----------|----------|------|
| PWM 谐波分析、开关瞬态 | SW | 1~5 μs | 唯一能解析开关动作的模型 |
| 控制稳定性分析、PLL 动态 | CCI | 20~100 μs | 保留控制动态，计算效率适中 |
| 场站聚合、控制交互筛查 | AV | 50~200 μs | 计算效率高，适合多机组 |
| 故障穿越、LVRT/HVRT 验证 | SW 或 CCI | 5~50 μs | 需要精确的限流动态 |
| 大规模系统实时仿真 | SCI | 50~500 μs | 最大加速比，满足实时性 |
| 宽频振荡分析 | CCI + 频域扫描 | 20~100 μs | 需要控制动态 + 阻抗特性 |
| 构网型控制验证 | SW | 1~5 μs | GFM 的电压源特性需要精确解析 |

### 仿真方法选择指南

| 系统规模 | 推荐方法 | 加速比 | 说明 |
|----------|----------|--------|------|
| < 50 节点，单机详细建模 | 传统 EMT（SW） | 1× | 小规模系统无需加速 |
| 50~500 节点，场站聚合 | AV/CCI + 多速率 | 10~100× | 聚合 + 多时间步长 |
| 500~5000 节点，大规模场站 | GLIM + GPU | 100~400× | 并行计算 |
| > 5000 节点，区域电网 | ML 增强 + GPU | 400×+ | 数据驱动模型 |

### 失效边界

- **平均值模型**无法表示 PWM 谐波、保护瞬时电流、直流侧纹波和子模块电容动态。
- **单机等值**可能掩盖集电网络谐振、机组控制差异和局部弱网问题。
- **频域阻抗筛查**只能说明某一运行点附近的小扰动风险，大扰动故障和限流过程仍需 EMT 时域验证。
- **无来源的容量占比、穿越时长、效率、储能配比和控制收益**不应写成通用结论；这些指标依赖标准、设备和地区。

## 相关模型与方法

- [[renewable-energy-units]] — 风电、光伏、储能等单个机组的 EMT 建模
- [[pv-power-plant]] — 光伏电站级主题页
- [[inverter-model]] — 并网逆变器通用建模
- [[gfl-inverter-model]] — 跟网型逆变器建模
- [[gfm-inverter-model]] — 构网型逆变器建模
- [[bess-model]] — 储能系统建模
- [[dfig-model]] — DFIG 电机模型
- [[pmsg-single-unit]] — PMSG 单机模型
- [[pll-design]] — PLL 控制器设计
- [[dsogi-pll]] — DSOGI-PLL 改进方法
- [[vector-control]] — 矢量控制方法
- [[droop-control]] — 下垂控制方法
- [[virtual-synchronous-generator]] — 虚拟同步机
- [[harmonic-analysis]] — 谐波分析
- [[frequency-domain-analysis]] — 频域分析
- [[emt-simulation]] — EMT 仿真基础
- [[parallel-computing]] — 并行计算加速
- [[multirate-method]] — 多速率仿真
- [[dispatch-operation]] — 调度运行

## 来源论文

- **Sano 2022** "Comparison and Selection of Grid-Tied Inverter Models for Accurate and Efficient EMT Simulations" — 五类逆变器建模方法（SW/VI/AV/CCI/SCI）的系统对比，建立了精度-效率映射框架
- **Wang 2026** "A Component-Level Modeling and Fine-Grained Simulation Method for Renewable Energy Power Systems Suitable for GPU Architecture" — GLIM 组件级建模方法，面向 GPU 的大规模新能源系统细粒度仿真
- **Nurunnabi 2025** "Advancing Grid-Forming Inverter Technology: Comprehensive PQ Capability and Performance Analysis" — GFM 逆变器的 PQ 能力边界、EVR/CPID 控制策略、EMT 仿真验证
- **Ranasinghe 2024** "Advanced DSOGI PLL with Adaptive Bandwidth for Improved Transient Performance of Grid Connected Inverter Control Systems" — 自适应带宽 DSOGI-PLL，弱网条件下的 PLL 稳定性改进
- **Sun 2024** "Inverter-Based Resources Model Verification Using Electromagnetic Transient Playback Simulation" — IBR EMT 模型的回放验证方法，PSCAD 回放工具
- **Cheng 2025** "Machine-Learning-Reinforced Massively Parallel Transient Simulation for Large-Scale Renewable-Energy-Integrated Power Systems" — ML 增强的 CPU-GPU 大规模并行 EMT 仿真，400× 加速比
- **Marthi 2024** "Benchmark High-Fidelity EMT Models for Power Grid with PV Plants" — 基于 IEEE-39 母线系统的 PV 场站基准模型（3 场站，500 MW）
- **Hussein 2016** "A Wideband Equivalent Model of Type-3 Wind Power Plants for EMT Studies" — Type-3 WPP 宽频等效模型（FDNE + DLFE），85% 计算时间减少
- **Li 2022** "Structure Preserving Aggregation Method for Doubly-Fed Induction Generators in Wind Power Conversion" — DFIG 结构保持聚合方法，递归降阶，70% 计算时间减少
