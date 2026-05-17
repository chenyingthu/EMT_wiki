---
title: "断路器 (Circuit Breaker)"
type: model
tags: [circuit-breaker, switch, arc-model, protection, transient, hvdc-circuit-breaker, multi-unit-breaker]
created: "2026-04-29"
updated: "2026-05-18"
---

# 断路器 (Circuit Breaker)

## 定义与分类

断路器（Circuit Breaker, CB）是电力系统最重要的保护与控制设备，承担正常操作、故障隔离和电流开断等功能。在电磁暂态（EMT）仿真中，断路器模型的核心挑战在于：真实断路器的开断过程涉及电弧在电流过零附近的动态演化——灭弧介质恢复强度与暂态恢复电压（TRV）之间的竞争决定了开断成功与否——而传统EMTP模型仅将断路器表示为理想开关，无法描述热击穿、介质击穿、电流截流或重燃等真实现象。

断路器按灭弧介质分类：

| 类型 | 灭弧介质 | 电压等级 | 主要应用 |
|------|---------|---------|---------|
| 空气断路器 (ACB) | 空气 | <1 kV | 低压配电 |
| 真空断路器 (VCB) | 真空 | 1–40 kV | 中压配电 |
| SF₆断路器 | SF₆气体 | 40–800 kV | 高压/超高压 |
| 少油断路器 | 变压器油 | 10–220 kV | 中压（逐步淘汰） |

## EMT中的角色

断路器在EMT仿真中承担双重角色：既是**拓扑开关**（决定网络连接关系），又是**动态电弧元件**（与系统暂态相互作用）。

**核心挑战**：EMTP为保证计算效率，将电感、电容经梯形积分转化为等效电阻与历史电流源并联的形式，使节点导纳矩阵[Y]保持实对称且常数特性，便于LU分解求解。然而断路器电弧电阻随时间和电流电压强烈变化，若直接并入网络会破坏[Y]矩阵的常数特性。解决路径有二：① 补偿法（Compensation Method）将非线性断路器从网络中隔离，先求开路电压和戴维南等效阻抗，再迭代求解非线性方程；② 将断路器按功能分解为主网络（恒定矩阵）与辅助电弧网络（时变电阻），通过接口量交互实现解耦。

**工程需求**：多断口高压断路器（245 kV以上）的各合分闸单元（Making and Breaking Unit, MBU）之间存在动作非同期、均压电容耦合和介质耐受差异，导致预击穿、重燃或复燃等高频暂态现象，亟需精细化EMT建模。

## 电弧物理基础

### 能量平衡方程

所有电弧模型的核心是能量平衡方程。电弧通道中，输入功率等于热损耗功率与电弧能量变化之和：

$$\frac{dQ}{dt} = P_{\text{in}} - P_{\text{loss}} = u_a i_a - P_{\text{loss}}$$

其中 $u_a$ 为电弧电压，$i_a$ 为电弧电流，$Q$ 为电弧热能，$P_{\text{loss}}$ 为热损失功率。

### Cassie模型

Cassie模型假设电弧为圆柱形，温度分布均匀，电导与温度成正比。电弧电导 $g = 1/R_a$ 的动态方程为：

$$\frac{1}{g}\frac{dg}{dt} = \frac{1}{\tau}\left(\frac{u^2}{u_0^2} - 1\right)$$

其中 $\tau$ 为时间常数（约1 μs），$u_0$ 为稳态电弧电压（$u_0 = E_{\text{arc}} \cdot l_{\text{arc}}$，$E_{\text{arc}}$ 为电弧梯度10–50 V/cm）。该模型适用于大电流区域（>100 A），此时电弧温度足以维持热电离平衡。

### Mayr模型

Mayr模型考虑电弧冷却效应，热时间常数较大（约1 ms），电导动态方程为：

$$\frac{1}{g}\frac{dg}{dt} = \frac{1}{\tau}\left(\frac{ui}{P_0} - 1\right)$$

其中 $P_0$ 为散热功率，$\tau$ 为热时间常数。该模型适用于小电流区域和电流过零附近，能捕捉截流（current chopping）现象。

### Schwarz综合模型

Schwarz模型综合了Cassie和Mayr的特点：

$$\frac{1}{g}\frac{dg}{dt} = \frac{1}{\tau}\left(\frac{ui}{P_{\text{loss}}} - 1\right)$$

其中 $P_{\text{loss}} = P_0 + \alpha u^2 g$，$P_0$ 为恒定散热功率，$\alpha u^2 g$ 为与电导相关的附加散热。

## EMT建模方法

### 方法1：Avdonin电弧模型（改进Mayr）

Avdonin模型将Mayr模型的时间常数 $\theta$ 替换为 $A \cdot r^\alpha$、功率常数 $P$ 替换为 $B \cdot r^{-\beta}$，得到电阻形式微分方程：

$$\frac{dr}{dt} = \frac{1}{A}r^{-\alpha} - \frac{1}{A \cdot B}r^{-\alpha-\beta} i \cdot v$$

其中 $v$ 为弧电压，$i$ 为电流，$r$ 为弧电阻，$A$、$B$、$\alpha$、$\beta$ 为断路器参数。该模型源自Hydro-Quebec测试数据，可模拟热击穿和电流截流，但不能模拟介质击穿或多次重燃。

**参数典型值**（按灭弧介质）：

| 参数 | 空气 | 油 | SF₆ |
|------|------|-----|-----|
| $A$ | 6×10⁻⁶ | 6×10⁻⁶ | 1.3×10⁻⁶ |
| $B$ | 1.6×10⁷ | 1.0×10⁸ | 1.0×10⁶ |
| $\alpha$ | −0.20 | −0.15 | −0.15 |
| $\beta$ | −0.50 | −0.60 | −0.26 |

### 方法2：Urbanek模型

Urbanek模型以电导 $g$ 为状态变量，描述热恢复过程：

$$\frac{dg}{dt} = \frac{1}{\tau}(G - g), \quad G = \frac{i}{V + \frac{\zeta}{g}}$$

其中 $V$ 为大电流下弧电压（典型值8000 V），$\zeta$ 为冷弧通道击穿电压（典型值2.0×10⁻⁶），$\tau$ 为时间常数（典型值46×10⁴）。该模型能成功模拟电流截流（0.5–2 A）和重燃（re-ignition）现象，在变压器/电抗器开断场景中准确再现截流过电压波形。

### 方法3：Kopplin模型

Kopplin模型将时间常数和功率常数写为电导的函数：

$$\frac{dg}{dt} = \frac{1}{\tau(g)}\left[\frac{i \cdot v}{P(g)} - g\right]$$

其中 $\tau(g) = k_1 \cdot (g + 0.0005)^{0.25}$，$P(g) = k_2 \cdot (g + 0.0005)^{0.6}$，$k_1$ 和 $k_2$ 为模型参数。该模型在发电机断路器开断测试中，弧电压峰值误差<2%，后弧电流偏差<5%，热击穿预测准确率>95%。

### 方法4：多断口MBU-RDBV/RRBV模型

Mailhot等（2024）提出面向多断口高压断路器的EMTP模型，将每个MBU与并联均压电容构成独立电磁暂态单元。模型核心是击穿电压下降曲线（RDBV，关合时）和恢复电压上升率（RRBV，开断时）：

**关合操作RDBV（Rate of Decrease of Breakdown Voltage）**：

$$U_b(t) = E_b(t) \cdot d_c(t) \quad \text{（帕邢定律近似）}$$

$$RDBV(t) \equiv -\frac{d}{dt}U_b(t) = -\frac{d(d_c(t))}{dt} \cdot E_b \cdot \lambda(d_c)$$

其中 $d_c$ 为触点间隙，$E_b$ 为介质强度，$\lambda = 1/\beta$ 为几何因子（$\beta$ 为电场增强因子）。

**开断操作RRBV（Rate of Rise of Breakdown Voltage）**：

$$RRBV(t) = \frac{d(d_o(t))}{dt} \cdot E_b(t) \cdot \lambda(d_o)$$

其中两条包络线分别描述热恢复和介质恢复：

$$U_{b,\text{th}}(t) = U_{b0} + RRBV_{\text{th}} \cdot (t - t_{\text{extinction}})$$

$$U_{b,\text{di}}(t) = U_{b0} + RRBV_{\text{di}} \cdot (t - t_{\text{contact\_separation}})$$

**关键现象**：首个MBU预击穿导致均压电容电荷积累，第二断口瞬时电压可达第一断口的1.8–2.2倍；真空断路器重燃频率500 kHz–2 MHz，SF₆介质强度恢复率通常10–50 kV/ms。

### 方法5：HVDC限流断路器（CL-DCCB）拓扑

Li等（2018）提出的模块化限流直流断路器CL-DCCB，由主断路器MCB和多个支路断路器BCB组成。正常运行时各支路电感并联（等效电感 $L_{\text{eq}} = L/N$），降低导通损耗；疑似故障时闭锁IGBT并分闸超快机械开关UFD，将并联切换为串联（等效电感跃升至 $N \cdot L$），强制抑制故障电流上升率。

**磁链守恒约束**（切换瞬间电流连续）：

$$\psi_L(0^-) = \psi_L(0^+) \Rightarrow \sum_{k=1}^{N} L_k i_{Lk}(0^-) = \left(\sum_{k=1}^{N} L_k\right) i_{\text{Limit}}(0^+)$$

**BCB辅助电容KVL方程**：

$$\begin{cases} u_{dc} = u_{c1} + L_3 \frac{di_3}{dt} + iR \\ u_{dc} = u_{c2} + L_1 \frac{di_1}{dt} + iR \\ u_{dc} = u_{c1} + u_{c2} - L_2 \frac{di_2}{dt} + iR \end{cases}$$

## 形式化表达

### EMTP节点方程与补偿法

EMTP的节点导纳矩阵方程为：

$$[Y]e(t) = i(t) - [I]$$

其中[Y]可保持实对称并以LU形式存储。补偿法将非线性断路器从网络中隔离，先计算开路电压 $V_n$ 和戴维南等效阻抗 $Z_{\text{thev}}$，再通过迭代求解：

$$V_n - Z_{\text{thev}} \cdot I_n = f(I_n)$$

### 梯形积分离散化

电弧电阻的梯形积分更新（预测-校正迭代）为：

$$r(t + \Delta t) = r(t) + \frac{\Delta t}{2}\left(\frac{dr}{dt} + \frac{dr_p}{dt}\right)$$

其中 $dr_p/dt$ 为上一时步保存的变化率。预测步电流估计：

$$I(t + \Delta t) = I(t) + \Delta t \cdot \frac{dI}{dt}$$

### 开断成功判据

补偿法开断状态判断逻辑：

- **成功开断**：弧电阻 $r > 10^7\,\Omega$ 或变化率 $|dr/dt| > 10^{18}\,\Omega/\text{s}$
- **热击穿失败**：电阻变化率开始下降

## 关键技术挑战

### 挑战1：数值刚性与收敛性

电弧方程具有刚性特点（时间常数跨0.1 μs至100 ms量级），在时间步长 $\Delta t > 50\,\mu\text{s}$ 时Kopplin模型可能出现收敛困难。解决路径：采用预测-校正迭代算法（利用电流过零前的线性特性预测初始值，再通过梯形积分校正），通常3–4次迭代即可收敛；在电弧不稳定期间采用1–10 μs步长。

### 挑战2：多断口非同期动作

同一极内MBU的动作不同步（IEC 62271-100允许2–5 ms差异），导致预击穿、重燃和断口间电压分布瞬态失衡。均压电容的电荷积累效应使某一MBU的击穿改变其他MBU的电压分配，需在事件触发时更新网络拓扑。

### 挑战3：参数辨识困难

Avdonin/Urbanek/Kopplin模型需要大量物理参数（$A$、$B$、$\alpha$、$\beta$、$k_1$、$k_2$等），难以从设备规格书获得。Phaniraj等提出参数估计器从测试波形反推模型参数，拟合优度 $R^2 > 0.95$，但测试数据获取本身具有挑战性。

### 挑战4：HVDC开断无自然过零

直流电流无自然过零，需依靠电弧"强迫过零"（弧电流被外部电路强制降为零）或电力电子器件闭锁。CL-DCCB通过拓扑重构（并联电感→串联电感）强制抑制故障电流上升率，为保护判据争取12 ms时间窗口。

### 挑战5：高频多次重燃

真空断路器因其快速熄弧特性，在多断口结构中易诱发连续多次重燃（500 kHz–2 MHz），伴随高频电流振荡（幅值数十至数百安培）。仿真需采用10–100 ns级步长，对EMTP求解器构成挑战。

## 量化性能边界

### 电弧模型精度对比

| 模型 | 弧电压峰值误差 | 后弧电流误差 | 截流特性 | 热击穿预测 |
|------|--------------|------------|---------|-----------|
| Avdonin [Phaniraj 2004] | <0.5% | — | 可模拟 | 准确率>95% |
| Urbanek [Phaniraj 2004] | — | — | 0.5–2 A误差<3% | — |
| Kopplin [Phaniraj 2004] | <2% | <5% | — | 准确率>95% |
| MBU-RDBV/RRBV [Mailhot 2024] | 定性吻合 | — | 高频重燃可复现 | — |

### 计算效率

- 补偿法结合预测-校正迭代：CPU时间增加<15%，内存占用增加<5%（相对直接求解非线性方程组）
- 迭代收敛性：95%以上时步中迭代次数≤4次，平均迭代次数3.2次，最大迭代次数<10次
- 数值稳定性：$\Delta t \leq 10\,\mu\text{s}$ 时算法保持绝对稳定，无数值振荡

### EMT仿真步长需求

| 模型类型 | 典型步长 | 说明 |
|---------|---------|------|
| 详细电弧模型（Cassie/Mayr/Avdonin） | 0.1–10 μs | 解析电弧时间常数（τ≈0.1–100 μs） |
| 理想开关模型 | 1–50 μs | 初步开断特性分析 |
| 闭环保护系统仿真 | 50–100 μs | 含继电器算法处理延迟<1 μs |
| 高频重燃仿真 | 10–100 ns | 多MBU连续重燃（500 kHz–2 MHz） |

### HVDC断路器性能指标

- 最大故障检测延时：12 ms（满足ROCOV等慢速检测算法时序要求）[Li 2018]
- IGBT用量：270个（减半于传统方案540个）[Li 2018]
- UFD分闸时间：约2 ms[Li 2018]
- 多断口电压失衡：第二断口瞬时电压达第一断口的1.8–2.2倍[Mailhot 2024]

## 适用边界与选择指南

| 维度 | 适用条件 | 失效边界 |
|------|---------|---------|
| 电压等级 | 10 kV–800 kV（按灭弧介质） | 低于10 kV的紧凑型VCB参数需修正 |
| 电流范围 | 额定电流至100 kA短路电流 | 超高压大电流开断（>80 kA）的电弧等离子体非平衡效应 |
| 频率 | 50/60 Hz工频至高频频谱 | 真空断路器高频重燃（>2 MHz）需补充分布参数模型 |
| 介质类型 | 空气/油/SF₆/真空 | 新型替代气体（CO₂、AirDry）参数未建立 |
| 系统类型 | 交流系统/直流VSC-HVDC | 直流LCC-HVDC的换相失败场景不适用 |
| 模型选择 | 截流风险→Urbanek；热击穿→Avdonin；发电机→Kopplin | Avdonin不能模拟介质击穿或多次重燃 |
| 多断口 | 245 kV及以上多MBU串联 | 单断口VCB（<145 kV）的MBU非同期效应不显著 |

## 相关模型

- [[surge-arrester-model]] — 避雷器过电压保护配合
- [[transformer-model]] — 变压器保护配合
- [[transmission-line-model]] — 线路TRV特性
- [[load-model]] — 负荷电流开断特性
- [[inductor-model]] — 小电感电流开断
- [[lcc-model]] — LCC换流器（换相失败场景）

## 相关方法

- [[numerical-integration]] — 电弧动态方程离散化（梯形积分）
- [[state-space-method]] — 断路器状态建模
- [[frequency-dependent-modeling]] — TRV宽频分析
- [[nodal-analysis]] — 节点分析法（补偿法接口）
- [[interpolation-method]] — 电弧特性插值

## 来源论文

| 论文 | 年份 | 主要贡献 |
|------|------|---------|
| [[modelling-of-circuit-breakers-in-the-electromagnetic-transients-program-power-sy]] | 2004 | Avdonin/Urbanek/Kopplin三电弧模型EMTP实现，补偿法接口，预测-校正迭代 |
| [[modelling-of-electromagnetic-transients-in-multi-unit-high-voltage-circuit-break]] | 2024 | 多MBU串联RDBV/RRBV模型，均压电容耦合，非同期动作效应 |
| [[a-new-topology-for-current-limiting-hvdc-circuit-breaker]] | 2018 | CL-DCCB模块化拓扑，磁链守恒限流，12 ms检测延时 |
| [[protection-system-representation-in-the-electromagnetic-transients-program-power]] | 2004 | EMTP保护系统表示 |

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*