---
title: "电力系统稳定器 (Power System Stabilizer, PSS)"
type: method
tags: [pss, stabilizer, damping, oscillation, small-signal-stability, excitation-system, ieee-pss, anderson-pss, subsynchronous-oscillation]
created: "2026-05-02"
updated: "2026-05-15"
---

# 电力系统稳定器 (Power System Stabilizer, PSS)

## 定义与边界

电力系统稳定器（Power System Stabilizer, PSS）是同步发电机 [[excitation-system]] 的附加阻尼控制环节，通过引入与转速偏差、频率偏差、有功功率偏差或加速功率等信号成比例的附加电压调节输入，在关注的机电振荡模态上提供正阻尼转矩，从而抑制低频功率振荡。

从物理机制看，PSS 并不改变同步机的稳态电压设定值——那是 AVR 的职能。PSS 的作用是使电磁转矩的相位超前转子角度偏差，在相位滞后最严重的振荡频率点（通常为 0.2~2.0 Hz）产生与转速偏差同相位的转矩分量，从而实现阻尼。IEEE Std 421.5-2005 定义了三种标准 PSS 结构（IEEE PSS1A/2A/3A），Anderson PSS 和 Widholm PSS 等变体则在工业界广泛应用。

**PSS 是控制方法，不是 EMT 核心求解方法。** 它主要服务于机电振荡和小信号稳定分析；在 EMT 中，PSS 需要作为控制器模型离散化并接入同步机励磁系统。PSS 不能替代开关暂态、谐波、保护动作或宽频网络响应的 EMT 建模。

## EMT 中的角色

在 EMT 中，PSS 作为控制器微分方程接入同步机励磁通道，其输出信号 $V_{PSS}$ 注入 AVR 的输入端，AVR 再调节励磁电压 $E_{fd}$，进而改变电磁转矩。这个链路可以表示为：

$$\Delta T_e = \underbrace{K_s \Delta \delta}_{\text{同步转矩}} + \underbrace{K_d \Delta \omega}_{\text{阻尼转矩}}$$

其中 $K_d$ 是等效阻尼系数，PSS 的设计目标是在关注模态上提高 $K_d$。**重要约束**：上式基于小扰动线性化，只在转子角偏移较小、控制器未限幅、励磁系统未饱和的条件下成立。

在 EMT 仿真中，PSS 的典型应用场景包括：

- **同步机闭环暂态响应**：研究 AVR/PSS 与定转子饱和模型耦合时的大扰动响应
- **机电-电磁混合仿真边界**（[[electromechanical-electromagnetic-hybrid-simulation]]）：PSS 可能位于机电侧同步机模型中，或在 EMT 侧详细控制器中实现，取决于分网边界
- **多机系统机电振荡**：多台 PSS 之间的交互和协调整定

## 核心机制

### 单输入 PSS 通用结构

典型单输入 PSS 的传递函数结构为：

$$V_{PSS} = K_{PSS} \cdot G_W(s) \cdot G_C(s) \cdot G_L(s) \cdot u$$

其中：
- $u$：输入信号（转速偏差 $\Delta\omega$、频率偏差 $\Delta f$、有功功率偏差 $\Delta P$ 或加速功率 $\Delta P_a$）
- $K_{PSS}$：增益系数
- $G_W(s)$：隔直（washout）环节
- $G_C(s)$：相位补偿（phase compensation）环节
- $G_L(s)$：限幅（limiter）和保护逻辑

### 隔直环节

隔直环节的目的是阻断稳态偏置分量，使 PSS 只响应振荡分量，防止稳态电压偏差影响 AVR 基准值：

$$G_W(s) = \frac{s T_W}{1 + s T_W}$$

其中 $T_W$ 为隔直时间常数，通常取 1.0~10.0 s。隔直环节在稳态（$s\to0$）时增益趋于 0，在振荡频段（$s=j\omega$）时增益接近 1。

### 相位补偿环节

相位补偿环节用于补偿励磁系统和同步机在目标振荡频段的相位滞后，使电磁转矩与转速偏差同相。常见的超前-滞后补偿结构为：

$$G_C(s) = \prod_{k=1}^{n} \frac{1 + s T_{1k}}{1 + s T_{2k}}$$

典型值为 $T_{1}/T_{2} = 0.1/0.02$ 或 $0.3/0.06$（s），$n=1$ 或 $n=2$。参数整定需绑定具体机组、系统模态和验证方法——同一参数在不同机组上可能产生正阻尼或负阻尼。

### 限幅与保护逻辑

限幅环节限制 $V_{PSS}$ 的输出幅度，防止大扰动时 PSS 输出过大导致励磁电压越限：

$$V_{PSS}^{lim} = \begin{cases} V_{PSS}^{max} & V_{PSS} > V_{PSS}^{max} \\ V_{PSS} & V_{PSS}^{min} \le V_{PSS} \le V_{PSS}^{max} \\ V_{PSS}^{min} & V_{PSS} < V_{PSS}^{min} \end{cases}$$

典型限幅值为 $\pm 0.05 \sim \pm 0.10 \; pu$（以额定机端电压为基准）。

## 分类与变体

### IEEE 标准 PSS 结构（IEEE Std 421.5-2005）

IEEE 定义了三类标准 PSS 结构：

| 类型 | 输入信号 | 结构特点 | 适用场景 |
|------|---------|---------|---------|
| IEEE PSS1A | 转速偏差 $\Delta\omega$ | 单输入，隔直 + 两级超前-滞后补偿 | 单一机电模态，本地机组 |
| IEEE PSS2A | 转速偏差 + 电功率偏差 | 双输入复合 | 抑制本地和区域间模态 |
| IEEE PSS3A | 频率偏差 $\Delta f$ | 频率输入经过滤波 | 频率测量更稳定的情形 |

### Anderson PSS

Anderson PSS 是一种基于加速功率的 PSS 结构，其核心思想是通过转速偏差和电功率偏差构造近似加速功率：

$$u_{Anderson} = \Delta \omega - K_{p1} \Delta P$$

这种结构的优点是能在电功率测量噪声较大时保持较好的阻尼效果。Anderson PSS 的参数通常按单台机组本地机电模态整定。

### 多频段 PSS

多频段 PSS（Multi-band PSS）用多个补偿支路覆盖不同频段的机电振荡：

$$G_C(s) = G_{C1}(s) + G_{C2}(s) + G_{C3}(s)$$

典型配置：
- **低频段**（0.1~0.5 Hz）：覆盖区域间振荡模态
- **中频段**（0.5~1.5 Hz）：覆盖本地机电模态
- **高频段**（1.5~2.5 Hz）：覆盖次同步相互作用

多频段 PSS 参数更多，模态交互更复杂，必须通过特征值分析和时域验证确认。

### 广域 PSS

广域 PSS（Wide-area PSS）使用 PMU 远方信号或相位测量单元（Phasor Measurement Unit）提供的广域信号作为输入：

$$V_{PSS} = K_{PSS} \cdot G_W(s) \cdot G_C(s) \cdot (\Delta\omega_{local} + G_{comm}(s) \cdot \Delta\omega_{remote})$$

其中 $G_{comm}(s)$ 表示通信延迟和同步误差。**核心边界**：通信延迟（通常 20~100 ms）、丢包和同步误差会使广域 PSS 阻尼效果不确定，需要专门的通信质量保障机制。

### 自适应/智能 PSS

自适应 PSS 根据运行点变化自动调整参数，典型方法包括：

- 基于李雅普诺夫稳定性理论的参数自适应律
- 基于数据驱动/机器学习的增益调度

没有算例验证范围和鲁棒性证据时，不应将自适应 PSS 写成已普遍工程化的能力。

## EMT 建模方法

### 控制器离散化

在 EMT 中，PSS 控制器需要离散化以便时域求解。常见方法：

**双线性变换法（Tustin method）**：

$$s \approx \frac{2}{\Delta t} \cdot \frac{1 - z^{-1}}{1 + z^{-1}}$$

代入传递函数 $G_C(s)$ 得到离散形式：

$$G_C(z) = \prod_{k=1}^{n} \frac{1 + s T_{1k}}{1 + s T_{2k}} \bigg|_{s = \frac{2}{\Delta t} \frac{1-z^{-1}}{1+z^{-1}}}$$

**状态空间实现**：

$$x_{c}(t+\Delta t) = A_c x_c(t) + B_c u(t)$$
$$V_{PSS}(t) = C_c x_c(t) + D_c u(t)$$

其中离散矩阵 $A_c, B_c, C_c, D_c$ 由连续状态空间模型经指数映射得到。

### 采样与测量链路

PSS 的 EMT 建模需要包含完整的测量链路：

1. **三相瞬时量提取**：从 EMT 相电压/电流中提取 $u(t)$ 信号
2. **测量滤波**：滤除开关纹波和高频分量，典型截止频率 2.0~5.0 Hz
3. **坐标变换**（如采用 $\Delta P$ 输入）：$abc \to \alpha\beta \to dq$
4. **限幅和投退逻辑**：大扰动期间 PSS 可能被自动退出

### 限幅非线性的处理

PSS 限幅是大扰动 EMT 仿真中的关键非线性因素。两种处理方式：

**方式一：时域截断**（最常用）

在每个时步检查 $V_{PSS}$ 是否越限，如越限则直接截断。此方式简单但会在限幅边界引入小幅数值振荡。

**方式二：描述函数法**

用描述函数近似限幅环节的谐波传递特性，在小扰动分析中考虑其等效增益下降。

### 与同步机电磁方程的联解

PSS 输出的 $V_{PSS}$ 作为附加输入注入 [[excitation-system]]，AVR 的输出 $E_{fd}$ 再作用于同步机电磁方程。联解链路为：

$$\Delta\omega \xrightarrow{G_W} \xrightarrow{G_C} V_{PSS} \xrightarrow{AVR} E_{fd} \xrightarrow{同步机电磁方程} \Delta T_e \xrightarrow{ swing-equation} \Delta\omega$$

该闭环的稳定性需通过特征值分析（[[eigenvalue-analysis]]）和时域扰动验证。

## 关键技术挑战

### 挑战一：参数整定的模态绑定性

PSS 参数（$K_{PSS}, T_1, T_2, T_W$）必须针对具体机组的机电模态整定。同一组参数在某一机组上提供正阻尼，在另一机组上可能提供负阻尼。**典型整定流程**：

1. 通过 [[small-signal-stability-analysis]] 识别系统机电振荡模态和频率
2. 计算励磁系统和同步机在目标模态频率处的相位滞后 $\phi_{lag}$
3. 设计相位补偿 $G_C(s)$ 使总相位滞后补偿到 $-90^\circ \sim -270^\circ$ 范围内
4. 整定增益 $K_{PSS}$ 使阻尼比 $\zeta$ 达到目标值（通常 $\zeta > 0.05$）

### 挑战二：多机系统中的控制器协调

多台 PSS 并存时，若参数整定不当，可能出现：
- **相互作用**：多台 PSS 在同一模态上产生不利交互
- **负阻尼传递**：一台 PSS 改善了本地模态但恶化了区域间模态
- **控制冲突**：PSS 与 FACTS 阻尼控制、HVDC 辅助阻尼控制之间争夺同一频段

协调整定方法包括协调优化算法和基于广域测量的交互模态分析。

### 挑战三：限幅对大扰动响应的影响

PSS 限幅使小信号设计结论在大扰动下失效。大扰动时：
- $V_{PSS}$ 可能长时间处于限幅状态，阻尼控制失效
- 励磁饱和非线性使 $E_{fd}$ 实际值偏离 AVR 指令值
- 保护动作（AVR 切到手动/备用励磁）使 PSS 退出

因此需要在 [[transient-stability-analysis]] 框架下对大扰动工况进行验证。

### 挑战四：与宽频振荡控制的关系

传统 PSS 的目标频段（0.2~2.0 Hz）与次同步振荡（10~50 Hz）和宽频振荡（kHz 级）有本质区别。在 [[wideband-oscillation-stability]] 场景下，PSS 只能作为背景控制器，不能用于抑制宽频振荡。宽频振荡需要阻抗分析、谐波滤波器或主动阻尼控制。

## 量化性能边界

PSS 的阻尼效果通常以**阻尼比提升量**和**振荡衰减时间**衡量。以下数据来自文献中的典型单机-无穷大母线系统算例，**具体数值因机组参数、系统强度、运行点和 PSS 参数而异，引用时应注明来源**：

| 参数 | 典型范围 | 说明 |
|------|---------|------|
| 目标振荡频率 | 0.2~2.0 Hz | 本地/区域间机电模态 |
| 阻尼比提升 | $+0.02 \sim +0.15$ | 施加 PSS 后阻尼比改善量 |
| 振荡衰减时间 | 5~20 s | 扰动后振荡幅值衰减至 5% 所需时间 |
| 相位补偿量 | $20^\circ \sim 60^\circ$ | 补偿励磁-同步机通道滞后 |
| 增益 $K_{PSS}$ | $0.01 \sim 0.5$ | 以 pu/pu 为单位的增益值 |
| 限幅值 | $\pm 0.05 \sim \pm 0.10$ pu | 以机端电压为基准的 pu 值 |

**来源说明**：上述范围来自 IEEE Std 421.5-2005、Anderson & Aberbour 论文摘要及 EMTP-ATP 仿真经验。具体阻尼效果应以论文原文中实际系统参数和仿真结果为准。

> **注**：原文未报告可核验的标准化阻尼比数值。本页所列范围为工程经验值，引用时应注明"据工程经验，未找到标准化文献数据"。

## 适用边界与选择指南

| PSS 类型 | 适用场景 | 不适用场景 |
|---------|---------|-----------|
| IEEE PSS1A（单输入转速型） | 单一本地机电模态，机组参数已知 | 多模态系统，参数变化范围大 |
| IEEE PSS2A（双输入复合型） | 本地模态 + 区域间模态抑制 | 广域信号不可用的系统 |
| IEEE PSS3A（频率输入型） | 转速测量噪声较大的场景 | 频率测量同样受噪声影响 |
| Anderson PSS | 电功率测量相对稳定的多机系统 | 电功率快速波动场景 |
| 多频段 PSS | 存在多个振荡频段（本地+区域间） | 参数整定复杂，易过拟合 |
| 广域 PSS | 区域间振荡和广域测量可用的系统 | 通信延迟 > 100 ms，质量无保障 |
| 自适应/智能 PSS | 运行点大范围变化且有训练数据 | 缺乏验证数据的工业场景 |

**选择决策树**：
1. 目标模态是本地还是区域间？ → 本地用单输入 PSS，区域间用双输入或广域 PSS
2. 测量信号质量如何？ → 转速偏差优先，电功率和频率作为备选
3. 系统是否有多台 PSS？ → 需协调整定，避免交互负效应
4. 是否涉及大扰动和限幅主导？ → 需时域验证，不能依赖小信号结论

## 与相关页面的关系

- [[excitation-system]]：PSS 输出注入 AVR 的附加输入端，AVR 是 PSS 的直接作用对象
- [[swing-equation]]：PSS 产生的阻尼转矩通过转子运动方程影响 $\Delta\delta$ 和 $\Delta\omega$
- [[small-signal-stability-analysis]]：PSS 参数整定和模态阻尼验证的主要分析工具
- [[transient-stability-analysis]]：大扰动下控制器限幅和保护动作需要时域验证
- [[wideband-oscillation-stability]]：宽频振荡不能直接用传统 PSS 抑制，需阻抗分析或主动阻尼
- [[electromechanical-electromagnetic-hybrid-simulation]]：PSS 在混合仿真中可位于机电侧或 EMT 侧，取决于分网边界
- [[pss-model]]：是同一概念的更通用控制方法入口，本页侧重 EMT 建模细节

## 来源论文

- [[saturation-in-transient-and-stability-phenomena-for-cylindrical-13&14]]：在 EMTP-ATP 同步机暂态分析中包含 AVR/PSS 和饱和模型，说明大型圆柱形同步机组中 PSS 结论必须绑定机组参数和励磁系统边界（该 source 页的 deep-review 提供了 Park model(2) 与 PSS 耦合的等效电路描述和饱和电抗处理方法）
- [[基于adpss的电力系统和牵引供电系统机电电磁暂态混合仿真]]：在 ADPSS 平台上实现机电-电磁混合仿真，其中 EMT 侧含 V/V 牵引变压器和机车整流负荷，机电侧含 383 节点实际电网和 77 台发电机组；混合仿真接口交换边界电压电流并保持同步，是 PSS 在大规模实际电网混合仿真中应用的参考实现
- [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb]]：给出暂态稳定（TS）与 EMT 混合仿真的接口技术框架，说明两类程序在建模假设、时间尺度和数值积分上的差异，是理解 PSS 在混合仿真中接口位置的理论基础

---

## 附录：标准 PSS 参数表（IEEE Std 421.5-2005）

### IEEE PSS1A 参数（典型值）

| 参数 | 典型值 | 说明 |
|------|-------|------|
| $T_W$ | 10.0 s | 隔直时间常数 |
| $T_1$ | 0.1 s | 超前时间常数 |
| $T_2$ | 0.02 s | 滞后时间常数 |
| $T_3$ | 0.3 s | 超前时间常数（第二级） |
| $T_4$ | 0.06 s | 滞后时间常数（第二级） |
| $K_{PSS}$ | 0.1~0.5 | 增益 |

### 参数整定注意事项

- 参数必须在具体机组和系统上通过特征值分析和时域仿真验证
- 不应直接引用其他论文的 PSS 参数而不做本地化验证
- 过高增益会导致励磁电压振荡和负阻尼风险
- 参数整定应同时检查稳态不偏置（PSS 不改变稳态电压）

<div class="diagram-container">
<svg viewBox="0 0 900 420" xmlns="http://www.w3.org/2000/svg">
  <!-- Title -->
  <text x="450" y="25" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#222">图1 · PSS 控制链路与 EMT 建模架构</text>

  <!-- Column headers -->
  <text x="130" y="58" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#2563eb">输入信号</text>
  <text x="300" y="58" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#16a34a">PSS 控制器</text>
  <text x="470" y="58" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#d97706">AVR / 励磁系统</text>
  <text x="640" y="58" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#7c3aed">同步机</text>
  <text x="800" y="58" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#dc2626">网络/扰动</text>

  <!-- Input signals box -->
  <rect x="60" y="72" width="140" height="150" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="130" y="90" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#1e40af">Δω：转速偏差</text>
  <text x="130" y="107" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#1e40af">Δf：频率偏差</text>
  <text x="130" y="124" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#1e40af">ΔP：有功功率偏差</text>
  <text x="130" y="141" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#1e40af">ΔPa：加速功率</text>
  <text x="130" y="158" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#1e40af">励磁电流 I_fd</text>
  <text x="130" y="175" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#1e40af">机端电压 V_t</text>
  <text x="130" y="205" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#666">（选择一种或多种）</text>

  <!-- PSS Controller box -->
  <rect x="230" y="72" width="140" height="150" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="300" y="90" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">GW(s)：隔直环节</text>
  <text x="300" y="107" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">  sTW/(1+sTW)</text>
  <text x="300" y="124" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">GC(s)：相位补偿</text>
  <text x="300" y="141" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">  Π(1+sT1k)/(1+sT2k)</text>
  <text x="300" y="158" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">GL(s)：限幅逻辑</text>
  <text x="300" y="175" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">KPSS：增益</text>
  <text x="300" y="205" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#666">离散化：Tustin 变换</text>

  <!-- AVR/Excitation box -->
  <rect x="400" y="72" width="140" height="150" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="470" y="90" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#92400e">Verr = Vref - Vt + VPSS</text>
  <text x="470" y="107" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#92400e">GAVR(s)：AVR 传递函数</text>
  <text x="470" y="124" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#92400e">Efd = GAVR · Verr</text>
  <text x="470" y="141" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#92400e">饱和、限幅、保护逻辑</text>
  <text x="470" y="158" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#92400e">励磁机动态</text>
  <text x="470" y="175" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#92400e">Efd → 同步机励磁绕组</text>
  <text x="470" y="205" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#666">电压调节 + 阻尼附加</text>

  <!-- Synchronous machine box -->
  <rect x="570" y="72" width="140" height="150" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="640" y="90" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#5b21b6">d/q 轴电磁方程</text>
  <text x="640" y="107" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#5b21b6">ΔTe = Ks·Δδ + Kd·Δω</text>
  <text x="640" y="124" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#5b21b6">Park 变换 / 反变换</text>
  <text x="640" y="141" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#5b21b6">定子电压方程</text>
  <text x="640" y="158" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#5b21b6">转子运动方程</text>
  <text x="640" y="175" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#5b21b6">饱和磁化曲线</text>
  <text x="640" y="205" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#666">swing-equation 联解</text>

  <!-- Network/Disturbance box -->
  <rect x="730" y="72" width="140" height="150" rx="6" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="800" y="90" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#991b1b">三相瞬时值网络</text>
  <text x="800" y="107" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#991b1b">故障扰动</text>
  <text x="800" y="124" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#991b1b">开关动作</text>
  <text x="800" y="141" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#991b1b">谐波/间谐波注入</text>
  <text x="800" y="158" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#991b1b">限幅触发</text>
  <text x="800" y="175" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#991b1b">→ Δω 返回输入</text>
  <text x="800" y="205" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#666">闭环反馈</text>

  <!-- Arrows -->
  <line x1="200" y1="147" x2="225" y2="147" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="370" y1="147" x2="395" y2="147" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="540" y1="147" x2="565" y2="147" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="710" y1="147" x2="725" y2="147" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Arrow feedback (curved) -->
  <path d="M 800 222 Q 800 260 450 260 Q 100 260 100 240 Q 100 220 100 147" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="5,3" fill="none" marker-end="url(#arrowRed)"/>
  <text x="820" y="255" font-family="Arial,sans-serif" font-size="9" fill="#dc2626">扰动返回</text>

  <!-- Legend -->
  <rect x="60" y="300" width="780" height="100" rx="6" fill="#f9f9f9" stroke="#ccc" stroke-width="1"/>
  <text x="80" y="320" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#222">颜色图例</text>
  <rect x="80" y="332" width="18" height="12" rx="2" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="105" y="342" font-family="Arial,sans-serif" font-size="10" fill="#333">输入信号（Δω, Δf, ΔP 等）</text>
  <rect x="300" y="332" width="18" height="12" rx="2" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="325" y="342" font-family="Arial,sans-serif" font-size="10" fill="#333">PSS 控制器（隔直+相位补偿+限幅）</text>
  <rect x="560" y="332" width="18" height="12" rx="2" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="585" y="342" font-family="Arial,sans-serif" font-size="10" fill="#333">AVR / 励磁系统</text>
  <rect x="80" y="352" width="18" height="12" rx="2" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="105" y="362" font-family="Arial,sans-serif" font-size="10" fill="#333">同步机电磁方程（d/q 轴模型）</text>
  <rect x="300" y="352" width="18" height="12" rx="2" fill="#fee2e2" stroke="#dc2626" stroke-width="1"/>
  <text x="325" y="362" font-family="Arial,sans-serif" font-size="10" fill="#333">网络扰动 / 闭环反馈</text>
  <rect x="560" y="352" width="18" height="12" rx="2" fill="#f9f9f9" stroke="#ccc" stroke-width="1"/>
  <text x="585" y="362" font-family="Arial,sans-serif" font-size="10" fill="#333">红色虚线：大扰动反馈路径</text>

  <text x="80" y="380" font-family="Arial,sans-serif" font-size="9" fill="#666">注：PSS 主要作用于 0.2~2.0 Hz 低频机电振荡模态，不能抑制次同步（10~50 Hz）和高频（kHz）振荡</text>
  <text x="80" y="395" font-family="Arial,sans-serif" font-size="9" fill="#666">EMT 建模时需包含测量滤波链路（截止频率 2~5 Hz）和控制器离散化（Tustin 变换），限幅非线性和励磁饱和在大扰动下使小信号设计结论失效</text>

  <!-- Arrow marker defs -->
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#333"/>
    </marker>
    <marker id="arrowRed" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#dc2626"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · PSS 控制链路与 EMT 建模架构（蓝→绿→黄→紫→红：输入→控制器→AVR→同步机→网络/扰动）</p>