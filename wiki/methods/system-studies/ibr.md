---
title: "逆变器型资源建模方法"
type: method
tags: [ibr, inverter-based-resource, modelica, declarative-modeling, switching-model, average-value-model, vi-model, cci-model, gfl, gfm]
created: "2026-05-05"
updated: "2026-05-14"
---

# 逆变器型资源建模方法 (IBR Modeling)

## 定义

逆变器型资源（Inverter-Based Resource, IBR）建模方法指针对电力电子并网设备——包括光伏逆变器、全功率风机、储能变流器、构网型（GFM）与跟网型（GFL）接口——建立电磁暂态（EMT）仿真模型的技术体系。IBR建模的核心矛盾在于**精度与效率的对立统一**：开关级模型能精确再现PWM谐波、死区效应和故障暂态尖峰，但仿真步长通常需 ≤ 2 µs，在大系统规模下计算时间不可接受；简化模型可通过平均值、电压插值或电流注入等方式消除开关事件，将步长放宽至 100 µs ~ 600 µs，但会丢失开关频率相关的高频动态。

IBR建模不是单一模型，而是**一组按保真度分层的建模方法族**，每个方法在"能模拟什么、不能模拟什么"上有明确的物理边界。

## EMT中的角色

IBR建模在EMT仿真中承担以下关键角色：

1. **谐波与开关动态分析**：光伏、风机、储能并网后引入的开关频率谐波（通常数百Hz至数十kHz）在相量域仿真中无法表示，必须使用EMT级模型。
2. **控制稳定性评估**：IBR的PLL、内外环电流控制、GFM的虚拟同步控制等动态过程与传统同步机完全不同，需要瞬时值级建模才能复现控制交互失稳。
3. **故障穿越与保护配合**：低电压穿越（LVRT）、过电流限幅、闭锁重启等逻辑的时序行为，要求模型能精确表示器件级开关和滤波器暂态。
4. **大规模系统仿真加速**：当系统中包含数百至数千台IBR时，必须通过模型简化（AV/CCI/SCI）、多速率仿真、并行协同等方法突破计算瓶颈。

## 核心建模方法族

IBR建模方法按保真度从高到低可分为五级，每一级在物理等效方式、控制保留度和计算效率上有显著差异。

### 1. 开关模型 (Switching Model, SW)

SW模型是IBR建模的**最详细层级**，显式表示功率器件（IGBT/MOSFET）的开通与关断操作，保留完整的电路拓扑和控制环路。

**电路等效**：功率器件通过理想开关、理想开关+无源元件或可变电阻（含导通电阻与关断电阻）表示。三相桥式逆变器的交流端连接交流电感Lf与等效串联电阻Rfl，开关纹波滤波器由电容Cf和串联电阻Rfc组成。

**控制保留**：完整保留功率控制（直流电压控制器、无功功率控制器）、电流控制（dq轴PI控制器）和调制（PWM）三部分。PLL用于电网同步，生成dq轴电流参考$ i_d^*, i_q^* $。

**数学表达**：

$$
\dot{\mathbf{x}} = f(\mathbf{x}, \mathbf{v}, \mathbf{u}, t)
$$

$$
\mathbf{i}_{inj} = g(\mathbf{x}, \mathbf{v}, \mathbf{u}, t)
$$

其中$\mathbf{x}$包含电感电流、电容电压和控制器状态，$\mathbf{v}$为并网点电压，$\mathbf{u}$为参考量、故障状态或调度输入。

**仿真步长**：必须远小于开关周期，通常为 **1 ~ 2 µs**（以解析PWM开关瞬变）。

**适用场景**：开关频率谐波分析、死区效应研究、直流侧短路故障、IGBT级故障穿越验证。

**失效场景**：大系统级参数扫描（计算时间过长）、机电暂态时间尺度分析。

### 2. 电压插值模型 (Voltage Interpolation Model, VI)

VI模型由Time-Average Method [1] 和 Subcycle Average Method [2] 发展而来，最初用于实时仿真，后被推广到离线EMT仿真 [3]。其核心思想是：**不消除开关事件，而是用代数插值精确估计开关时刻**。

**核心机制**：VI模型模拟两电平PWM电压，但在开关转换$t_{fall}$和$t_{rise}$之前或之后插入插值电压。插值电压通过计算获得，使VI模型在一个计算步长内的交流电压积分面积等于理论开关波形的积分面积。

对于三角载波同步采样PWM，电压参考$v^*$与载波$v_{carrier}$的交点$t_{fall}$和$t_{rise}$可通过代数计算获得（不受仿真步长$T_s$限制）。插值占空比$\bar{s}$由下式给出：

$$
\bar{s} = \frac{1}{2} + \frac{v^* - v_{carrier}}{h T_s}
$$

其中$h$为载波斜率（由载波幅值和频率确定），$T_s$为仿真步长。

**电路等效**：VI模型由受控电流源$i_{dc}$、六个受控电压源和六个理想二极管组成。$i_{dc}$运行以维持直流侧输入功率等于交流侧输出功率。在开关转换前后，$\bar{s}$取0到1之间的值以插入插值电压；在开关状态保持期间，$\bar{s}$取0或1（对应上臂关断/下臂关断）。

**控制保留**：与SW模型完全相同（功率控制 + 电流控制 + PWM调制）。

**仿真步长**：可放宽至 **10 µs**（约为SW的5倍），因为开关时间分辨率误差已被插值消除。

**量化性能**：Sano 2021 [4] 在统一测试条件下测得，VI模型的计算时间约为SW模型的 **19%**，同时在4.5 kHz开关频率谐振、死区低次谐波、电压暂降等场景中波形误差 < 2%。

**适用场景**：需要开关频率谐波但系统规模不允许SW步长的场景，如中等规模电网中的IBR谐波交互分析。

**失效场景**：无法表示多电平调制策略（原论文基于两电平）、无法表示器件级故障（如IGBT短路/开路）。

### 3. 平均值模型 (Average-Value Model, AV)

AV模型基于**状态空间平均法** [5]，在一个载波周期内对逆变器输出电压取平均，消除开关纹波。

**数学表达**：

$$
v_{sa} = d_a v_{dc}, \quad v_{sb} = d_b v_{dc}, \quad v_{sc} = d_c v_{dc}
$$

其中$d_a, d_b, d_c$为调制占空比，$v_{dc}$为直流侧电压。AV模型直接输出调制参考电压在一个载波周期内的平均值，不模拟开关动作。

**控制保留**：保留功率控制和电流控制，**排除PWM调制环节**。因为输出电压直接由占空比决定，无需比较器生成门极信号。

**仿真步长**：可放宽至 **100 µs**（约为SW的50倍）。

**量化性能**：Sano 2021 [4] 测得AV模型的计算时间约为SW模型的 **1.5%**。

**关键偏差**：AV模型在电流控制稳定性评估中存在**乐观偏差**——当电流控制器增益增至3 p.u.时AV模型出现振荡，而SW/VI模型在2 p.u.时已失稳。这是因为AV模型平滑了开关动态，高估了电流控制器的稳定裕度。

**适用场景**：基波控制动态分析、系统级电压/频率支撑研究、不含开关频率谐振的暂态稳定性评估。

**失效场景**：开关频率谐波分析（完全丢失开关纹波）、死区效应研究、高频谐振评估（对4.5 kHz谐振响应误差100%）。

### 4. 受控电流注入模型 (Controlled Current Injection Model, CCI)

CCI模型将逆变器交流侧等效为**受控电流源**，输入为有功/无功或电流参考，通过功率平衡计算直流侧电流。

**数学表达**：

$$
i_{sa} = S_{SW} i_a^*, \quad i_{sc} = S_{SW} i_c^*, \quad i_{dc} = \frac{v_{ab} i_{sa} + v_{cb} i_{sc}}{v_{dc}}
$$

其中$S_{SW}$为开关函数，$i_a^*, i_c^*$为电流参考。CCI模型基于理想电流源与功率控制生成参考电流，实现交直流侧能量传递。

**控制保留**：保留功率控制，**排除电流控制和PWM调制**。CCI模型直接注入电流参考，不模拟电流环的动态响应。

**仿真步长**：可放宽至 **600 µs**（约为SW的300倍）。

**量化性能**：Sano 2021 [4] 测得CCI模型的计算时间约为SW模型的 **0.20%**。

**关键局限**：
- 缺失交流侧滤波电感，导致电压突变时**高频尖峰电流缺失**。
- 在电压暂降期间，CCI模型能模拟闭锁与重启过程，但故障电流幅值误差 > 15%。
- 直流侧短路时，因缺少交流侧滤波电感阻抗，故障电流计算出现显著误差。

**适用场景**：大系统中理想电流注入近似、粗略功率交换分析、对高频动态不敏感的稳定性研究。

**失效场景**：滤波器谐振分析、故障暂态尖峰、电流控制稳定性评估。

### 5. 简化电流注入模型 (Simplified Current Injection Model, SCI)

SCI模型是IBR建模的**最简化层级**，将逆变器等效为简单电流源，排除所有控制器。

**控制保留**：**排除全部控制环路**（功率控制、电流控制、PLL、PWM）。SCI模型直接注入恒定电流，不响应电网电压变化。

**仿真步长**：可放宽至 **600 µs**。

**量化性能**：Sano 2021 [4] 测得SCI模型的计算时间约为SW模型的 **0.12%**。

**关键局限**：
- 因缺乏PLL，无法跟踪电网电压相位变化，导致无功功率$Q$与电压$V_{ab}$出现显著稳态偏差。
- 在100%电压暂降下，SCI模型无法执行闭锁逻辑，持续注入恒定电流，导致无功/电压误差 > 20%。
- 对电网谐波完全免疫，输出电流不受电网电压畸变影响。

**适用场景**：仅关注低频功率注入的大系统分析、作为其他模型的基准对比。

**失效场景**：任何需要PLL同步、无功控制、故障穿越逻辑的场景。

## 五模型精度-效率映射


Sano 2021 [4] 在统一测试条件下（相同拓扑、控制参数、求解器设置）对五种模型进行了系统对比。以下是核心量化结果：

| 模型 | 仿真步长 | 计算时间比例 | 开关谐波 | 死区效应 | 电流控制稳定性 | 电网谐波交互 | 电压暂降 | 直流短路 |
|------|----------|------------|----------|----------|--------------|------------|----------|----------|
| SW | 2 µs | 100% (基准) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| VI | 10 µs | 19% | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| AV | 100 µs | 1.5% | ✗ | ✗ | 乐观偏差(+1p.u.) | ✓ | ✓ | ✓ |
| CCI | 600 µs | 0.20% | ✗ | ✗ | ✗ (无电流环) | ✗ (免疫) | 缺尖峰 | 误差>15% |
| SCI | 600 µs | 0.12% | ✗ | ✗ | ✗ (无控制) | ✗ (免疫) | 误差>20% | ✗ (恒流) |

## 控制架构建模：GFL与GFM

IBR按控制架构可分为**跟网型（Grid-Following, GFL）**和**构网型（Grid-Forming, GFM）**两大类，两者的EMT建模有本质差异。

### 跟网型 (GFL) 建模

GFL逆变器**依赖电网电压作为同步参考**，通过PLL提取电网相位，在dq同步参考系下合成输出电流。

**核心方程**（Luchini 2023 [6]）：

$$
P = \frac{3}{2}(v_d i_d + v_q i_q)
$$

$$
Q = \frac{3}{2}(v_d i_q - v_q i_d)
$$

取$v_q = 0$作为参考，可得到dq轴电流参考：

$$
i_d = \frac{2P}{3v_d}, \quad i_q = \frac{-2Q}{3v_d}
$$

GFL建模的关键在于PLL的动态——LPF-PLL和DSOGI-PLL是两种常用方案。DSOGI-PLL通过二次广义积分器正交信号生成器（DSOGI-QSG）提供滤波后的αβ帧电压，再结合SRF-PLL实现频率自适应正序检测，在电网失真条件下更可靠。

**验证方法**：Sun 2024 [7] 提出基于Point-On-Wave (POW) 录波回放的IBR EMT模型验证方案。核心思想是将并网点(POI)实测电压录波作为边界条件，直接驱动待验证的IBR EMT模型，无需重建完整外部电网。针对IBR模型启动时间长（通常 > 1s）与录波数据扰动前时段短（通常 < 1s，实测示例仅0.23s）的矛盾，提出两种初始化技术：

1. **同步表法 (Synchroscope)**：使用理想三相电压源进行预启动，模型达到稳态后切换至回放电压源。
2. **波形扩展法 (Waveform Extension)**：在录波数据前端拼接理想电压波形，使模型直接加载扩展波形序列。

初始化参数计算：

$$
V_{init} = \sqrt{2} \cdot V_{RMS}
$$

$$
\theta_{init} = \arcsin\left(\frac{v(t_0)}{V_{peak}}\right)
$$

其中$V_{init}$为初始电压幅值，$\theta_{init}$为初始相位角，$v(t_0)$为录波起始时刻瞬时值。波形扩展法在切换瞬间的暂态扰动幅值低于同步表法。

### 构网型 (GFM) 建模

GFM逆变器**独立生成电网电压和频率**，无需大规模同步发电机即可为系统提供电压和频率支撑。

**功率传输方程**（Nurunnabi 2025 [8]）：

对于LCL耦合滤波器的GFM逆变器，逆变器侧阻抗$Z_{inv} = R_{inv} + j\omega_s L_{inv}$，PCC侧阻抗$Z_g = R_g + j\omega_s L_g$，滤波电容电抗$X_c = 1/(\omega_s C)$。PCC处电流为：

$$
\vec{I}_{PCC} = \frac{\vec{E}_{inv} - \vec{V}_{PCC\_F}}{jX_F}
$$

其中$X_F = X_{inv} + X_g - \frac{X_{inv}X_g}{X_c}$，$\vec{V}_{PCC\_F} = \vec{V}_{PCC}\left(1 - \frac{X_{inv}}{X_c}\right)$。

有功和无功功率为：

$$
P_{PCC} \approx \frac{V_{PCC} E_{inv}}{X_F} \sin\delta_{inv}
$$

$$
Q_{PCC} \approx \frac{V_{PCC}}{X_F}\left(E_{inv}\cos\delta_{inv} - V_{PCC\_F}\right)
$$

GFM建模的核心挑战在于**PWM饱和与额定电流约束**对PQ能力边界的限制，以及不同耦合滤波器（L、LC、LCL）对谐波性能的影响。Nurunnabi 2025 [8] 提出的Enhanced Voltage Regulation (EVR) 和 Controlled Proportional-Integral Droop (CPID) 策略在动态负载和故障条件下优于传统下垂控制。

## 大规模IBR并行仿真方法

当系统中包含数百至数千台IBR时，单节点串行仿真无法在合理时间内完成。以下方法实现了大规模IBR的并行加速。

### FMI协同仿真并行化 (Ouafi 2023 [9])

基于Functional Mock-up Interface (FMI) 标准的主从式协同仿真架构，利用传输线/电缆模型（TLM）的自然传播延迟将大型电网解耦为多个子网络：

**TLM解耦方程**（Bergeron模型诺顿等效）：

$$
I_k(t) = -Y_c V_k(t-\tau) + I_k^{hist}(t-\tau)
$$

其中$Y_c$为特征导纳，$\tau$为传播延迟，$I_k^{hist}$为历史等效电流源。该方程在TLM处将电网解耦为独立子网，左右两侧通过历史电流源实现无近似电气等效。

**双缓冲通信机制**：

$$
I_{master}(t) \leftrightarrow \text{Buffer}_{1/2} \leftrightarrow I_{slave}(t)
$$

通过Buffer 1和Buffer 2交替读写，确保异步并行计算中数据完整性。

**信号量同步原语**：

$$
\text{Wait}(S), \quad \text{Release}(S)
$$

Master执行Wait等待Slave完成计算，Slave执行Release通知数据就绪。

**实现特点**：
- 通过DLL接口实现，**无需修改底层EMT求解器代码**。
- 支持多速率仿真：详细IGBT模型可用10 µs步长，平均值模型可用50 µs步长，相差5倍。
- 基于潮流结果自动初始化各子网接口。

**验证案例**：Network-1测试系统含4个300 MVA风电场、25台同步发电机、791个电气节点、8016个控制图块、1244×1244的MANA矩阵。WP_DFIG1采用详细IGBT模型（$\Delta t = 10\mu s$），其余采用平均值模型（$\Delta t = 50\mu s$）。

### 状态变量保持法 (Wang 2025 [10])

状态变量保持（State-Variable-Preserving, SVP）方法使用离散状态空间表达式提取原始电路的输出特性，在保留机组所有状态变量的同时，将外部系统的表示规模缩减。该方法通过受控导纳和由内部状态变量确定的受控历史电流源组合消除内部节点，同时使用节点撕裂法实现并联仿真。

## 关键技术挑战

### 1. 精度-效率权衡的量化边界

IBR建模的核心挑战是如何在精度和效率之间做出有据可依的选择。Sano 2021 [4] 的对比研究表明，不同简化模型在**不同物理现象**上的误差差异巨大：
- 对开关频率谐振（4.5 kHz），AV/CCI/SCI的误差为100%（完全无法模拟）。
- 对电流控制稳定性，AV存在+1 p.u.的乐观偏差。
- 对电压暂降，CCI缺失高频尖峰，SCI完全无法闭锁。
- 对电网谐波交互，CCI/SCI对电压畸变完全免疫。

这意味着**不存在"万能模型"**——选择必须基于具体的仿真目的。

### 2. GFL/GFM混合系统的建模一致性

在高比例IBR系统中，GFL和GFM逆变器往往共存。两者的建模需要保持一致的接口标准（如IEEE 1547的THD限值、电压/频率偏差容限），但在EMT仿真中，GFL依赖PLL同步而GFM独立生成电压，两者的控制动态和故障响应差异显著。Nurunnabi 2025 [8] 的实验验证表明，GFL和GFM在并行运行时需特别注意PQ能力边界和控制策略的协调。

### 3. 模型验证的工程可行性

Sun 2024 [7] 的POW回放方法解决了IBR模型验证的核心工程难题——无需重建完整外部电网即可验证模型精度。但该方法依赖高质量POW电压录波（采样率、平滑时间常数必须为0 s）和正确的现场控制设定，在以下场景存在局限：
- 多端口强耦合网络中，单端口电压回放可能不足以判定模型准确性。
- 不同EMT平台间的数值差异可能影响回放结果的可比性。

## 量化性能边界

| 性能指标 | SW模型 | VI模型 | AV模型 | CCI模型 | SCI模型 | 数据来源 |
|---------|--------|--------|--------|---------|---------|---------|
| 仿真步长 | 2 µs | 10 µs | 100 µs | 600 µs | 600 µs | Sano 2021 [4] |
| 计算时间比例 | 100% | 19% | 1.5% | 0.20% | 0.12% | Sano 2021 [4] |
| 开关频率谐波再现 | ✓ (<2%误差) | ✓ (<2%误差) | ✗ (100%) | ✗ (100%) | ✗ (100%) | Sano 2021 [4] |
| 死区低次谐波再现 | ✓ | ✓ | ✗ | ✗ | ✗ | Sano 2021 [4] |
| 电流控制稳定性评估 | ✓ | ✓ | 乐观偏差(+1p.u.) | ✗ | ✗ | Sano 2021 [4] |
| 电网谐波交互响应 | ✓ (<5%误差) | ✓ (<5%误差) | ✓ | ✗ (免疫) | ✗ (免疫) | Sano 2021 [4] |
| 电压暂降闭锁逻辑 | ✓ | ✓ | ✓ | ✓ (缺尖峰) | ✗ (误差>20%) | Sano 2021 [4] |
| 直流侧短路故障 | ✓ | ✓ | ✓ | 误差>15% | ✗ | Sano 2021 [4] |
| 多速率并行 | N/A | ✓ (10µs) | ✓ (50µs) | N/A | N/A | Ouafi 2023 [9] |
| POW回放验证 | ✓ | ✓ | ✓ | - | - | Sun 2024 [7] |

## 适用边界与选择指南

### 模型选择决策树

| 仿真目的 | 推荐模型 | 理由 |
|---------|---------|------|
| 开关频率谐波分析（< 10 kHz） | SW 或 VI | 只有SW和VI能准确再现开关纹波和死区效应 |
| 死区引起的低次谐波分析 | SW 或 VI | AV/CCI/SCI完全丢失死区谐波 |
| 电流控制稳定性评估 | SW 或 VI | AV存在+1 p.u.乐观偏差，CCI/SCI无法评估 |
| 系统级电压/频率支撑 | AV | 计算效率高（1.5%），能保留基波控制动态 |
| 大系统功率交换分析 | CCI | 计算效率极高（0.20%），适合粗略功率注入 |
| 对高频动态不敏感的稳定性 | SCI | 计算最快（0.12%），但仅适用于低频场景 |
| 大规模IBR并行仿真 | VI + 多速率 | 平衡精度与并行效率，支持10 µs/50 µs多速率 |
| 模型验证（POW回放） | SW | 最高保真度，确保回放结果可靠 |
| GFM控制策略评估 | SW 或 VI | 需要精确表示PWM饱和和电流约束 |

### 失效边界

1. **SW/VI模型**：不适用于机电暂态时间尺度（秒级以上）的系统稳定性分析，步长过小导致计算不可行。
2. **AV模型**：不能用于开关频率相关分析（误差100%），电流控制稳定性评估存在系统性乐观偏差。
3. **CCI模型**：不能用于滤波器谐振分析（缺失交流侧滤波电感阻抗），故障暂态高频尖峰缺失。
4. **SCI模型**：不能用于任何需要PLL同步、无功控制或故障穿越逻辑的场景，对电网谐波完全免疫。
5. **FMI并行化**：仅适用于存在天然TLM传播延迟的网络拓扑；人工插入stubline会产生单步延迟误差，需结合具体系统验证。
6. **POW回放验证**：依赖高质量POW电压录波，多端口强耦合网络中单端口回放可能不足以判定模型准确性。

## 相关方法 / 相关模型 / 相关主题

- [[vsc-control]]：VSC控制架构，IBR控制的核心实现
- [[lvrt-control]]：低电压穿越控制，IBR故障穿越的关键场景
- [[power-electronics-control]]：电力电子控制通用框架
- [[grid-forming-inverter]]：构网型逆变器，IBR的GFM变体
- [[grid-connected-inverter]]：并网逆变器，IBR的典型应用
- [[switch-modeling]]：开关级建模，SW模型的基础
- [[average-value-model]]：平均值建模，AV模型的理论基础
- [[parallel-computing]]：并行计算，大规模IBR仿真的加速手段
- [[co-simulation]]：协同仿真，FMI并行化的核心机制
- [[model-verification-benchmark]]：模型验证基准，IBR模型精度评估
- [[renewable-energy-integration]]：新能源并网，IBR建模的应用场景
- [[variable-time-step-solver]]：变时间步长求解器，IBR仿真中的数值方法选择

## 来源论文

1. **Sano, Horiuchi & Noda (2022)** — "Comparison and Selection of Grid-Tied Inverter Models for Accurate and Efficient EMT Simulations" (*IEEE Transactions on Power Electronics*, 37(3))。系统对比五种IBR建模方法（SW/VI/AV/CCI/SCI），建立精度-效率映射关系和量化选型指南，是IBR建模方法族的核心参考文献。
2. **Luchini et al. (2023)** — "Equivalent grid-following inverter-based generator model for ATP/ATPDraw simulations" (*Electric Power Systems Research*)。提出基于ATP/ATPDraw的GFL等效IBR模型，详细实现DSOGI-PLL和电流合成逻辑，故障条件下平均误差约2.33%，执行时间减少约70%。
3. **Nurunnabi, Li & Das (2025)** — "Advancing Grid-Forming Inverter Technology: Comprehensive PQ Capability and Performance Analysis" (*IEEE Access*)。GFM逆变器的PQ能力边界建模，EVR和CPID控制策略，L/LC/LCL耦合滤波器的性能对比，IEEE 1547合规性验证。
4. **Sun et al. (2024)** — "Inverter-Based Resources Model Verification Using Electromagnetic Transient Playback Simulation" (*IEEE PES General Meeting*)。基于POW录波回放的IBR EMT模型验证方案，两种初始化技术（同步表法/波形扩展法），ISO-NE在PSCAD中的工程实现。
5. **Ouafi et al. (2023)** — "Parallelization of EMT simulations for integration of inverter-based resources" (*Electric Power Systems Research*)。基于FMI主从协同仿真的IBR大规模并行仿真方法，TLM解耦、双缓冲通信、多速率机制，Network-1和智利电网验证。
6. **Wang et al. (2025)** — "A state-variable-preserving method for the efficient modelling of inverter-based resources in parallel EMT simulation" (*IET Generation, Transmission & Distribution*)。状态变量保持（SVP）方法，离散状态空间表达式消除内部节点，节点撕裂法实现并联仿真。
7. **Xiong et al. (2024)** — "ParaEMT: An Open Source, Parallelizable, and HPC-Compatible EMT Simulator for Large-Scale IBR-Rich Power Systems"。ParaEMT开源EMT仿真器，面向高比例IBR电网的HPC并行架构。

---

## 证据边界

本页综合了7篇核心文献的建模方法、量化数据和适用边界。所有技术细节基于PDF原文，量化指标标注了数据来源。以下边界需特别注意：

- Sano 2021 [4] 的量化数据（计算时间比例、步长、误差）来自XTAP仿真程序在特定硬件上的测试结果，不能直接外推到其他EMT软件平台。
- Ouafi 2023 [9] 的并行加速效果依赖于TLM传播延迟的存在，对于无天然线路的网络，stubline插入会产生额外延迟误差。
- Sun 2024 [7] 的POW回放方法需要高质量录波数据（采样率、平滑时间常数=0 s），在录波质量不足的场景可能无法准确验证模型。
- Nurunnabi 2025 [8] 的GFM PQ能力边界基于特定耦合滤波器配置，不同滤波器拓扑和PWM策略下的结果可能不同。
- 五模型对比表中的量化数据仅适用于两电平三相桥式并网逆变器，多电平拓扑（如MMC）的建模方法有显著差异。
<div style="text-align:center;margin:16px 0;"><svg viewBox="0 0 900 480" xmlns="http://www.w3.org/2000/svg">  <defs>    <marker id="arrow" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">      <polygon points="0 0, 8 3, 0 6" fill="#333"/>    </marker>    <filter id="shadow" x="-2%" y="-2%" width="104%" height="104%">      <feDropShadow dx="1" dy="1" stdDeviation="1" flood-color="#00000033"/>    </filter>  </defs>  <!-- Title area -->  <text x="450" y="30" fill="#1a1a2e" font-size="16" font-weight="bold" text-anchor="middle" font-family="SimSun, serif">IBR五模型精度-效率映射</text>  <text x="450" y="50" fill="#666" font-size="11" text-anchor="middle" font-family="SimSun, serif">Accuracy-Efficiency Mapping for IBR EMT Modeling</text>  <!-- Axes -->  <!-- Y axis: Accuracy -->  <line x1="120" y1="80" x2="120" y2="420" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>  <text x="50" y="250" fill="#333" font-size="12" text-anchor="middle" font-family="SimSun, serif" transform="rotate(-90,50,250)">保真度 (Accuracy)</text>  <!-- X axis: Computational Time -->  <line x1="120" y1="420" x2="860" y2="420" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>  <text x="490" y="455" fill="#333" font-size="12" text-anchor="middle" font-family="SimSun, serif">计算时间 (Computational Time)</text>  <!-- Region labels -->  <!-- High accuracy, low time region (top-left) -->  <rect x="130" y="90" width="180" height="120" rx="8" fill="#dcfce7" opacity="0.3" stroke="#16a34a" stroke-width="1" stroke-dasharray="4,2"/>  <text x="220" y="105" fill="#16a34a" font-size="10" font-weight="bold" text-anchor="middle" font-family="SimSun, serif">理想区域</text>  <text x="220" y="118" fill="#3a7a5a" font-size="9" text-anchor="middle" font-family="SimSun, serif">(高精度 / 低计算)</text>  <!-- Low accuracy, high time region (bottom-right) -->  <rect x="600" y="300" width="250" height="110" rx="8" fill="#fee2e2" opacity="0.3" stroke="#dc2626" stroke-width="1" stroke-dasharray="4,2"/>  <text x="725" y="315" fill="#dc2626" font-size="10" font-weight="bold" text-anchor="middle" font-family="SimSun, serif">避免区域</text>  <text x="725" y="328" fill="#b91c1c" font-size="9" text-anchor="middle" font-family="SimSun, serif">(低精度 / 高计算)</text>  <!-- Diagonal trade-off line -->  <line x1="140" y1="100" x2="840" y2="400" stroke="#999" stroke-width="1.5" stroke-dasharray="6,4"/>  <text x="750" y="370" fill="#999" font-size="9" text-anchor="middle" font-family="SimSun, serif">精度-效率权衡边界</text>  <!-- Model 1: SW - High accuracy, high time -->  <circle cx="780" cy="100" r="22" fill="#fee2e2" stroke="#dc2626" stroke-width="2" filter="url(#shadow)"/>  <text x="780" y="96" fill="#7f1d1d" font-size="11" font-weight="bold" text-anchor="middle" font-family="SimSun, serif">SW</text>  <text x="780" y="110" fill="#b91c1c" font-size="8" text-anchor="middle" font-family="SimSun, serif">2 µs</text>  <text x="780" y="70" fill="#7f1d1d" font-size="9" text-anchor="middle" font-family="SimSun, serif">开关级</text>  <!-- Arrow from label to dot -->  <line x1="780" y1="75" x2="780" y2="78" stroke="#dc2626" stroke-width="1" stroke-dasharray="3,2"/>  <!-- Model 2: VI - High accuracy, medium time -->  <circle cx="480" cy="120" r="22" fill="#dcfce7" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>  <text x="480" y="116" fill="#14532d" font-size="11" font-weight="bold" text-anchor="middle" font-family="SimSun, serif">VI</text>  <text x="480" y="130" fill="#3a7a5a" font-size="8" text-anchor="middle" font-family="SimSun, serif">10 µs</text>  <text x="480" y="90" fill="#14532d" font-size="9" text-anchor="middle" font-family="SimSun, serif">电压插值</text>  <line x1="480" y1="95" x2="480" y2="98" stroke="#16a34a" stroke-width="1" stroke-dasharray="3,2"/>  <!-- Model 3: AV - Medium accuracy, low time -->  <circle cx="300" cy="200" r="22" fill="#fef3c7" stroke="#d97706" stroke-width="2" filter="url(#shadow)"/>  <text x="300" y="196" fill="#78350f" font-size="11" font-weight="bold" text-anchor="middle" font-family="SimSun, serif">AV</text>  <text x="300" y="210" fill="#a16207" font-size="8" text-anchor="middle" font-family="SimSun, serif">100 µs</text>  <text x="300" y="170" fill="#78350f" font-size="9" text-anchor="middle" font-family="SimSun, serif">平均值</text>  <line x1="300" y1="175" x2="300" y2="178" stroke="#d97706" stroke-width="1" stroke-dasharray="3,2"/>  <!-- Model 4: CCI - Low accuracy, very low time -->  <circle cx="200" cy="300" r="22" fill="#dbeafe" stroke="#2563eb" stroke-width="2" filter="url(#shadow)"/>  <text x="200" y="296" fill="#1e3a5f" font-size="11" font-weight="bold" text-anchor="middle" font-family="SimSun, serif">CCI</text>  <text x="200" y="310" fill="#4b6b8f" font-size="8" text-anchor="middle" font-family="SimSun, serif">600 µs</text>  <text x="200" y="270" fill="#1e3a5f" font-size="9" text-anchor="middle" font-family="SimSun, serif">受控电流注入</text>  <line x1="200" y1="275" x2="200" y2="278" stroke="#2563eb" stroke-width="1" stroke-dasharray="3,2"/>  <!-- Model 5: SCI - Lowest accuracy, lowest time -->  <circle cx="150" cy="380" r="22" fill="#ede9fe" stroke="#7c3aed" stroke-width="2" filter="url(#shadow)"/>  <text x="150" y="376" fill="#3b0764" font-size="11" font-weight="bold" text-anchor="middle" font-family="SimSun, serif">SCI</text>  <text x="150" y="390" fill="#6b21a8" font-size="8" text-anchor="middle" font-family="SimSun, serif">600 µs</text>  <text x="150" y="350" fill="#3b0764" font-size="9" text-anchor="middle" font-family="SimSun, serif">简化电流注入</text>  <line x1="150" y1="355" x2="150" y2="358" stroke="#7c3aed" stroke-width="1" stroke-dasharray="3,2"/>  <!-- Computing time annotations -->  <!-- Time proportion labels -->  <text x="795" y="125" fill="#dc2626" font-size="8" text-anchor="start" font-family="SimSun, serif">100%</text>  <text x="495" y="145" fill="#16a34a" font-size="8" text-anchor="start" font-family="SimSun, serif">19%</text>  <text x="315" y="225" fill="#d97706" font-size="8" text-anchor="start" font-family="SimSun, serif">1.5%</text>  <text x="215" y="325" fill="#2563eb" font-size="8" text-anchor="start" font-family="SimSun, serif">0.20%</text>  <text x="165" y="405" fill="#7c3aed" font-size="8" text-anchor="start" font-family="SimSun, serif">0.12%</text>  <!-- Legend -->  <text x="130" y="460" fill="#333" font-size="10" font-weight="bold" font-family="SimSun, serif">图例：</text>  <circle cx="170" cy="460" r="6" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>  <text x="182" y="464" fill="#555" font-size="9" font-family="SimSun, serif">SW 开关级</text>  <circle cx="260" cy="460" r="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>  <text x="272" y="464" fill="#555" font-size="9" font-family="SimSun, serif">VI 电压插值</text>  <circle cx="360" cy="460" r="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>  <text x="372" y="464" fill="#555" font-size="9" font-family="SimSun, serif">AV 平均值</text>  <circle cx="430" cy="460" r="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>  <text x="442" y="464" fill="#555" font-size="9" font-family="SimSun, serif">CCI 受控电流</text>  <circle cx="520" cy="460" r="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>  <text x="532" y="464" fill="#555" font-size="9" font-family="SimSun, serif">SCI 简化电流</text></svg></div><p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · IBR五模型精度-效率映射（数据来源：Sano 2021 [4]）</p>