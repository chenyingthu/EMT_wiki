---
title: "线路换相换流器 (LCC)"
type: model
tags: [lcc, hvdc, thyristor, line-commutated, converter, commutation-failure, rectifier, inverter]
created: "2026-04-14"
updated: "2026-05-13"
---

# 线路换相换流器 (LCC)

## 定义

线路换相换流器（Line-Commutated Converter, LCC）是传统高压直流输电（HVDC）的核心换流设备，以晶闸管（Thyristor）为开关器件，依赖交流电网电压提供换相能量的半控型换流器。LCC不能主动关断电流，必须依靠交流系统电压在导通晶闸管上施加反向电压（即"换相"）来实现电流转移，因此被称为"线路换相"。

LCC的基本拓扑为**6脉波桥式电路**（6-pulse bridge），由6个晶闸管串联组成，每个桥臂含1个晶闸管。两个6脉波桥串联可构成**12脉波换流器**，通过换流变压器的星-三角接线产生30°相位差，有效抑制5次、7次等特征谐波。

LCC的运行模式由触发角$\alpha$决定：
- **整流模式**（$0° < \alpha < 90°$）：交流侧功率流向直流侧，直流电压$V_d > 0$
- **逆变模式**（$90° < \alpha < 180°$）：直流侧功率流向交流侧，逆变器通常以熄弧角$\gamma$（extinction angle）作为控制变量，典型值为$15° \sim 18°$

$$
V_d = V_{d0} \cdot \cos \alpha - \frac{3\omega_e L_c}{\pi} \cdot I_d = V_{d0} (\cos \alpha - \frac{\sqrt{3}\omega_e L_c}{\pi} \cdot I_d)
$$

其中$V_{d0}$为空载直流电压，$L_c$为换相电感，$I_d$为直流电流。

## EMT中的角色

在电磁暂态（EMT）仿真中，LCC建模的核心挑战在于**精确表征晶闸管的换相过程与换相失败（Commutation Failure, CF）动态**。与MMC不同，LCC的开关行为完全由外部交流电压决定，其换相过程涉及多个晶闸管同时导通的换相重叠期，以及因交流电压跌落导致的换相失败——这是LCC-HVDC系统最严重、最常见的故障模式。

LCC在EMT仿真中的关键需求：
1. **换相过程精确建模**：换相重叠角$\mu$的计算直接影响直流电压波形和换相失败判据
2. **换相失败检测与仿真**：交流电压跌落导致熄弧角$\gamma$小于临界值$\gamma_{crt}$时，晶闸管无法恢复阻断能力，引发换相失败
3. **谐波特性分析**：LCC是系统中主要的谐波源，需准确模拟特征谐波（$6k \pm 1$次）和非特征谐波
4. **换相失败连锁效应**：换相失败导致直流电压跌落、无功功率突增、直流电流激增，可能引发多馈入系统中的连锁换相失败

## EMT建模方法

### 1. 详细开关模型（Detailed Switching Model）

**原理**：使用EMT仿真软件（PSCAD/EMTDC、MATLAB/Simulink/PLECS）中的分立晶闸管元件，逐器件搭建6脉波或12脉波LCC换流桥。每个晶闸管包含正向导通、反向阻断、换相过程中的完整物理特性。

**数学表达**：晶闸管$i$的状态由变量$s_i \in \{0, 1\}$描述，导通条件为：
- 门极触发信号$g_i(t) = 1$
- 正向电压$v_i(t) > 0$
- 换相过程中需满足电流积分判据：$\int_0^t i_k(\tau)d\tau \geq Q_g$（门极电荷）

换相过程（$k \to j$晶闸管换相）期间，两晶闸管同时导通，换相电压$e_{kj} = e_k - e_j$驱动换相电感$L_c$中的电流变化：

$$
e_{kj} = 2L_c \frac{di_k}{dt} = -2L_c \frac{di_j}{dt}
$$

换相重叠角$\mu$由伏秒面积平衡确定：

$$
\cos \alpha - \cos(\alpha + \mu) = \frac{2\omega_e L_c I_d}{\sqrt{2}E}
$$

熄弧角$\gamma$为换相结束到线电压过零点的角度：

$$
\gamma = \pi - \alpha - \mu = \cos^{-1}\left(\frac{\sqrt{2}\omega_e L_c I_d}{E} - \cos \alpha\right) - \alpha
$$

**特点**：
- **精度最高**：完整保留晶闸管开关动态、换相过程、换相失败
- **可仿真所有故障**：换相失败、阀短路、开路故障、直流故障
- **计算量极大**：需处理大量开关事件，仿真步长通常为5～50 μs
- **适用场景**：换相失败机理研究、保护策略验证、单站/双站HVDC系统

**局限**：对于多站交直流混联系统，大量开关事件导致仿真速度极慢，成为系统级研究的计算瓶颈。

### 2. 开关函数模型（Switching Function Model）

**原理**：用连续开关函数替代离散开关动作，将晶闸管的导通/关断过程映射为时间相关的函数$s(t)$，通过傅里叶展开保留主要谐波分量。

**数学表达**：6脉波LCC的开关函数可展开为：

$$
s(t) = \frac{2\sqrt{3}}{\pi} \left[ \sin(\omega_e t - \alpha) - \frac{1}{5}\sin(5\omega_e t - 5\alpha) + \frac{1}{7}\sin(7\omega_e t - 7\alpha) + \cdots \right]
$$

直流电压与开关函数的关系：

$$
v_d(t) = s(t) \cdot v_{ac}(t)
$$

**特点**：
- **计算效率高于详细模型**：无需处理开关事件
- **保留主要谐波**：通过截断阶数控制精度
- **换相过程近似**：通常用等效换相电感近似，不精确模拟换相重叠
- **适用场景**：交直流混联系统稳定性分析、控制策略验证

### 3. 平均值模型（Average Value Model, AVM）

**原理**：在一个换相周期（60°电角度）内对LCC的交直流变量取平均，用代数方程描述交直流侧平均电压-电流关系，忽略开关细节。

**数学表达**（整流模式，忽略换相重叠）：

$$
\overline{V}_d = \frac{3\sqrt{2}}{\pi} V_{LL} \cos \alpha, \quad \overline{I}_{ac} = \frac{2}{3} \frac{V_d}{V_{ac}} \cdot I_d
$$

考虑换相重叠的平均模型：

$$
\overline{V}_d = \frac{3\sqrt{2}}{\pi} V_{LL} (\cos \alpha + \cos(\alpha + \mu)) / 2
$$

**特点**：
- **计算效率高**：无需开关级细节，可使用较大步长
- **无法仿真换相失败**：平均化抹平了瞬时电压跌落
- **无法仿真阀短路**：开关级故障信息被平均化
- **适用场景**：系统级稳态分析、低频振荡研究、多馈入HVDC的宏观特性分析

**局限**：在换相失败、交流故障等暂态过程中精度显著下降。

### 4. 参数化平均值模型（Parametric Average-Value Model, PAVM）

**原理**：由Jatskevich团队（UBC）提出，用数值函数（查找表）描述LCC交直流侧变量之间的物理关系，而非解析推导。通过详细模型仿真生成参数表，在仿真时根据触发角和负载工况查表求解。

**数学表达**：将交流电压、电流变换到同步旋转坐标系，平均化后得到参数方程：

$$
\| \overline{v}_{dq,pos}^n \| = w_v^{(n)}(\alpha, y_d) \cdot \overline{V}_d
$$

$$
\| \overline{i}_{dq,pos}^n \| = w_i^{(n)}(\alpha, y_d) \cdot \overline{I}_d
$$

$$
\phi(\alpha, y_d) = \theta_{i,dq} - \theta_{v,dq}
$$

其中$\alpha$为触发角，$y_d$为动态阻抗（整流侧）或动态导纳（逆变侧）：

$$
y_d = \frac{\| \overline{i}_{dq,pos}^1 \|}{\| \overline{v}_{dq,pos}^1 \|}
$$

参数$w_v, w_i, \phi$通过详细模型仿真生成二维查找表（触发角$\alpha$ vs 负载工况$y_d$）。

**特点**：
- **精度接近详细模型**：误差通常$< 1\%$
- **计算效率高**：CPU时间可比详细模型快3～13倍
- **支持谐波重构**：可扩展到n次谐波（通常$n_{max} = 7$）
- **支持不平衡工况**：通过正负序分解和动态/代数谐波表示
- **适用场景**：大规模交直流混联系统仿真、阻抗分析、稳定性研究

**量化性能**（Ebrahimi 2021）：
- 5秒暂态仿真：详细模型8.43秒 vs PAVM-DH 3.17秒 vs PAVM-PH 0.65秒
- 时间步长：详细模型平均194 μs vs PAVM-DH 326 μs vs PAVM-PH 990 μs

### 5. 扩展PAVM（含换相失败检测）

**原理**：由Hong等（2022）将PAVM扩展至逆变侧并集成自动换相失败检测。核心创新是通过伏秒面积法判断换相失败，自动切换参数表。

**换相失败判据**（Hong 2022）：
1. 监测交流电压幅值，检测电压跌落$g = \Delta E / E$
2. 从预存查找表获取临界跌落$g_{crt}(\alpha, y_d, \theta_{sag})$
3. 若$g > g_{crt}$，则判定换相失败，自动切换至故障工况参数表

**换相失败三阶段**（Hong 2022）：
- **阶段1**：故障晶闸管与同相导通晶闸管并联导通，直流电压部分跌落
- **阶段2**：故障晶闸管持续导通，换相过程异常延长
- **阶段3**：同相上下桥臂导通，形成阀短路，直流电压降至零

**特点**：
- **自动换相失败检测**：无需人工干预
- **准确预测换相失败波形**：与详细模型高度一致
- **优于动态相量模型**：DP模型在换相失败期间误差显著
- **适用场景**：含换相失败的多端HVDC系统仿真、交直流混联系统暂态分析

**量化性能**（Hong 2022）：
- 3秒仿真（含换相失败）：详细模型5.14秒 vs PAVM 1.94秒 vs DP模型 2.09秒
- 换相失败期间，PAVM波形与详细模型几乎一致，DP模型完全失效

### 6. 含内部故障的PAVM

**原理**：由洪泽祺等（2019）提出，在PAVM基础上增加参数表切换逻辑，支持晶闸管开路/短路故障仿真。

**参数表切换逻辑**（洪泽祺 2019）：

| 故障类型 | 故障原因 | 切换时刻 |
|----------|----------|----------|
| 开路故障 | 开关管本身损坏 | 若此刻导通则立即切换；若关断则在下一个导通时刻切换 |
| 开路故障 | 触发信号错误 | 下一个导通时刻切换 |
| 短路故障 | 开关管本身损坏 | 若此刻导通，当前导通过程结束时切换；若关断则立即切换 |
| 短路故障 | 触发信号错误 | 故障时刻在关断后下一个线电压过零点之前，在过零点切换；在过零点之后，立即切换 |

**等效电路设计**：
- 整流侧：交流侧等效为受控电压源，直流侧等效为受控电流源
- 逆变侧：交流侧等效为受控电流源，直流侧等效为受控电压源（避免受控电压源在小稳定域下的数值不稳定）
- 整流侧直流电流源串联电感需添加惯性环节（时间常数$\tau \approx 2.5 \times 10^{-4}$ s），避免数值振荡

**特点**：
- **支持开路/短路故障**：覆盖开关管本身故障和触发信号故障
- **参数表切换时刻判别**：避免错误切换导致的暂态误差
- **考虑谐波**：可包含7次及以下谐波正负序分量
- **故障稳态误差**：基波及2～7次谐波正负序幅值误差$< 1\%$，相角误差$< 1°$
- **适用场景**：交直流混联电网换流器故障分析、保护策略验证

**量化性能**（洪泽祺 2019）：
- CIGRE标准系统：详细模型（变步长）441.40秒 vs PAVM考虑谐波382.82秒
- 故障后1个周期内存在过渡误差，1个周期后误差在可接受范围内

### 7. 动态相量模型（Dynamic Phasor Model, DPM）

**原理**：将LCC的交直流变量表示为基波和谐波的时变相量，通过微分方程描述相量的幅值和相位动态。

**数学表达**：

$$
v_{abc}(t) = \text{Re}\left\{ \overline{V}_{dq}(t) \cdot e^{j\omega_e t} \right\} + \sum_{n} \text{Re}\left\{ \overline{V}_{dq}^n(t) \cdot e^{jn\omega_e t} \right\}
$$

**特点**：
- **平衡不平衡工况**：通过正负序动态相量
- **可预测换相失败**：通过伏秒面积法
- **假设理想开关**：零熄弧时间，忽略串联电阻
- **仅考虑3次谐波**：对交流变量的谐波考虑有限
- **适用场景**：不平衡工况下的LCC-HVDC系统分析

**局限**（Daryabak 2019）：
- 仅对推导时假设的单一运行模式有效
- 假设理想开关，忽略换相电感和串联电阻
- 换相失败期间精度显著低于PAVM

## 形式化表达

**LCC换流器端口关系**：

$$
V_d(\alpha, I_d) = V_{d0} \cos \alpha - X_c I_d = \frac{3\sqrt{2}}{\pi} V_{LL} \cos \alpha - \frac{3\omega_e L_c}{\pi} I_d
$$

**换相重叠角**：

$$
\mu = \cos^{-1}\left(\cos \alpha - \frac{2\omega_e L_c I_d}{\sqrt{2}E}\right) - \alpha
$$

**熄弧角**：

$$
\gamma = \pi - \alpha - \mu = \cos^{-1}\left(\frac{\sqrt{2}\omega_e L_c I_d}{E} - \cos \alpha\right) - \alpha
$$

**换相失败判据**：

$$
\gamma < \gamma_{crt} \quad \text{(通常} \gamma_{crt} \approx 10° \sim 15°\text{)}
$$

**PAVM参数表方程**：

$$
\begin{bmatrix} \overline{V}_d \\ \overline{I}_d \end{bmatrix} = \begin{bmatrix} w_v(\alpha, y_d) \\ w_i(\alpha, y_d) \end{bmatrix} \cdot \begin{bmatrix} \overline{V}_{ac} \\ \overline{I}_{ac} \end{bmatrix}
$$

## 关键技术挑战

### 1. 换相失败（Commutation Failure）

换相失败是LCC-HVDC系统最常见和最严重的故障。当交流电压跌落时，熄弧角$\gamma$减小，若$\gamma < \gamma_{crt}$（临界熄弧角，约10°～15°），晶闸管在恢复阻断能力前再次承受正向电压而导通，导致换相失败。

**换相失败的连锁效应**：
- 直流电压跌落（可能降至零）
- 直流电流激增（电容放电）
- 无功功率需求突增（换相重叠角增大）
- 可能引发多馈入系统中的连锁换相失败

**换相失败检测**：
- 伏秒面积法：通过比较换相电压的伏秒面积与所需恢复面积
- 临界电压跌落阈值法：$g > g_{crt}$时触发换相失败
- 熄弧角监测法：直接监测$\gamma$是否小于$\gamma_{crt}$

### 2. 不平衡工况下的谐波特性

正常工况下，12脉波LCC的交流侧仅含$12k \pm 1$次特征谐波（11次、13次、23次、25次...）。但在不平衡工况或内部故障时，串并联换流器之间的互补效应消失，交流侧出现大量非特征谐波（5次、7次、3次等）。

**谐波分解**（Ebrahimi 2021）：
- 交流侧：正负序分解，考虑$n = 1, 3, 5, 7$次谐波
- 直流侧：$h = 2, 4, 6, 8$次谐波（不平衡时2次谐波占主导）

### 3. 参数表切换逻辑

对于含内部故障的PAVM，参数表切换时刻的判别至关重要。错误的切换时刻会导致暂态波形与详细模型出现显著差异。洪泽祺等（2019）提出了4类故障场景的切换逻辑，确保模型在正确的物理时刻切换到故障工况参数表。

### 4. 数值稳定性

逆变侧采用受控电流源等效而非受控电压源，以避免在小稳定域下的数值不稳定。整流侧直流电流源串联电感需添加惯性环节，避免电流源与孤立电感串联引起的数值振荡。惯性环节时间常数$\tau$的选择需权衡暂态误差与数值稳定性（典型值$\tau \approx 2.5 \times 10^{-4}$ s）。

### 5. 多馈入换相失败

在多馈入HVDC系统中，一个换流站的交流电压跌落可能引发相邻换流站的换相失败，形成连锁故障。LCC模型需准确表征多馈入系统中的换相失败传播特性。

## 量化性能边界

**PAVM vs 详细模型**（Ebrahimi 2021）：
- 5秒暂态仿真（不平衡工况）：详细模型8.43秒 vs PAVM-DH 3.17秒 vs PAVM-PH 0.65秒
- PAVM-PH比详细模型快**13倍**
- 交流/直流变量波形与详细模型高度一致，误差$< 1\%$

**含换相失败的PAVM**（Hong 2022）：
- 3秒仿真（含CF）：详细模型5.14秒 vs PAVM 1.94秒 vs DP模型 2.09秒
- PAVM比详细模型快**2.65倍**
- 换相失败期间，PAVM波形与详细模型几乎一致，DP模型完全失效

**含内部故障的PAVM**（洪泽祺 2019）：
- CIGRE标准系统：详细模型441.40秒 vs PAVM 382.82秒
- 故障稳态误差：各次谐波幅值误差$< 1\%$，相角误差$< 1°$
- 故障后1个周期内存在过渡误差，1个周期后误差在可接受范围内

**动态相量模型**（Daryabak 2019）：
- 换相失败期间精度显著低于PAVM
- 假设理想开关，忽略换相电感，误差较大

## 适用边界与选择指南

| 应用场景 | 推荐模型 | 原因 |
|----------|----------|------|
| 换相失败机理研究 | 详细开关模型 | 需精确表征晶闸管开关动态 |
| 单站/双站HVDC系统 | 详细开关模型 | 计算量可接受，精度最高 |
| 多站交直流混联系统 | PAVM（含CF检测） | 精度与效率的最佳平衡 |
| 不平衡工况分析 | PAVM（扩展版） | 支持正负序谐波分解 |
| 换流器内部故障分析 | 含内部故障的PAVM | 支持开路/短路故障仿真 |
| 系统级稳态分析 | 平均值模型（AVM） | 计算效率高 |
| 低频振荡研究 | 平均值模型（AVM） | 无需开关级细节 |
| 阻抗稳定性分析 | PAVM（代数谐波） | 连续可线性化，比详细模型快13倍 |

## 相关方法

- [[average-value-model|平均值模型]] - LCC的基本平均化方法
- [[parametric-average-value-model]] - 参数化平均值模型（PAVM）
- [[dynamic-phasor-model|动态相量模型]] - LCC的动态相量方法
- [[switching-function-model|开关函数模型]] - 用开关函数替代离散开关
- [[thevenin-equivalent-model|戴维南等效]] - 外部网络等效

## 相关模型

- [[vsc-model|VSC模型]] - 电压源换流器对比
- [[mmc-model|MMC模型]] - 模块化多电平换流器对比
- [[thyristor-valve|晶闸管阀]] - 晶闸管器件建模
- [[converter-transformer|换流变压器]] - 换流变建模
- [[dc-line-model|直流线路]] - 直流线路建模
- [[harmonic-filter|谐波滤波器]] - LCC谐波滤波

## 相关主题

- [[hvdc|高压直流输电（HVDC）]] - 传统HVDC系统
- [[commutation-failure|换相失败]] - LCC核心故障模式
- [[multi-infeed-hvdc|多馈入HVDC]] - 多站LCC-HVDC系统
- [[ac-dc-hybrid-grid|交直流混联电网]] - 含LCC-HVDC的混合电网
- [[voltage-sag|电压跌落]] - 换相失败的诱因
- [[extinction-angle|熄弧角]] - LCC逆变运行的关键参数

## 来源论文

**奠基性文献**：
- [[thio-1996-commutation-failure|Thio et al. 1996]] - 换相失败的经典分析（伏秒面积法）
- [[arrillaga-hvdc|Arrillaga 1998]] - HVDC系统基础理论

**PAVM系列**：
- [[ebrahimi-2018-generalized-pavm|Ebrahimi et al. 2018]] - 广义PAVM（含谐波）
- [[ebrahimi-2021-unbalanced-lcc|Ebrahimi et al. 2021]] - 不平衡工况PAVM（正负序谐波分解）
- [[hong-2022-cf-pavm|Hong et al. 2022]] - 含换相失败检测的扩展PAVM
- [[hong-2019-fault-pavm|洪泽祺 等 2019]] - 含内部故障的LCC-HVDC动态平均化建模

**动态相量模型**：
- [[daryabak-2019-dp-lcc|Daryabak et al. 2019]] - LCC-HVDC动态相量模型（不平衡工况与换相失败）
- [[liu-2014-dp-lcc|Liu et al. 2014]] - 三相动态相量LCC建模

**解析平均模型**：
- [[sudhoff-1993-avm|Sudhoff 1993]] - 线换相换流器-同步电机系统的平均模型
- [[sudhoff-1996-transient-avm|Sudhoff 1996]] - 瞬态和动态平均模型
- [[atighechi-2014-cigre-avm|Atighechi et al. 2014]] - CIGRE标准HVDC系统动态平均化建模

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。核心模型描述基于Ebrahimi 2021、Hong 2022、洪泽祺 2019、Daryabak 2019等文献的PDF原文提取和交叉验证。换相失败判据基于Thio 1996的经典伏秒面积法。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[comparison-of-the-atp-version-of-the-emtp-and-the-netomac-program-for-simulation|Comparison of the ATP version of the EMTP and the NETOMAC pr]] | 2004 |
| [[hybrid-transient-stability-simulation-using-dynamic-phasor-based-interface-model-22|Hybrid Transient Stability Simulation Using Dynamic Phasor B]] | 2006 |
| [[hybrid-model-transient-stability-simulation-using-dynamic-phasors-based-hvdc-system-model|Hybrid-model transient stability simulation using dynamic ph]] | 2006 |
| [[2728nested-fast-and-simultaneous-solution-for-time-domain-simulation-of-integrat|Nested fast and simultaneous solution for time-domain simula]] | 2006 |
| [[application-of-emtp-rv-graphic-software-of-electromagnetic-transient-simulation|Application of EMTP-RV graphic software of electromagnetic t]] | 2007 |
| [[dynamic-average-value-modeling-of-13&14|Dynamic Average-Value Modeling of]] | 2014 |
| [[dynamic-phasor-based-interface-model-for-emt-and-transient-stability-hybrid-simu|Dynamic Phasor Based Interface Model for EMT and Transient S]] | 2017 |
| [[a-multi-area-thevenin-equivalent-based-multi-rate-co-simulation-for-control-desi|A multi-area Thevenin equivalent based multi-rate co-simulat]] | 2019 |
| [[measurement-based-frequency-dependent-model-of-a-hvdc-transformer-for-electromag|Measurement-based frequency-dependent model of a HVDC transf]] | 2019 |
| [[基于状态空间法的高压直流输电系统电磁暂态简化模型的解析算法|基于状态空间法的高压直流输电系统电磁暂态简化模型的解析算法]] | 2019 |
| [[基于状态空间法的高压直流输电系统电磁暂态简化模型的解析算法|基于状态空间法的高压直流输电系统电磁暂态简化模型的解析算法]] | 2019 |
| [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne|Average-Value Modeling of Line-Commutated AC-DC Converters W]] | 2021 |
| [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-|Large-scale hybrid real time simulation modeling and benchma]] | 2021 |
| [[accuracy-evaluation-of-electromagnetic-transients-simulation-algorithms|Accuracy Evaluation of Electromagnetic Transients Simulation]] | 2022 |
| [[average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail|Average-Value Modeling of Line-Commutated Inverter Systems W]] | 2022 |
| [[design-of-hybrid-series-converter-valve-considering-device-switching-characteris|Design of hybrid series converter valve considering device s]] | 2022 |
| [[electromechanical-electromagnetic-transient-hybrid-simulation-of-an-acdc-hybrid-|Electromechanical-electromagnetic transient hybrid simulatio]] | 2022 |
| [[2728modeling|Modeling_of_LCC_HVDC_Systems_Using_Dynam]] | 2022 |
| [[fast-detection-method-of-commutation-failure-based-on-multi-infeed-interaction-f|Fast Detection Method of Commutation Failure Based on Multi-]] | 2023 |
| [[harmonics-interaction-mechanism-and-impact-on-extinction-angles-in-multi-infeed-|Harmonics Interaction Mechanism and Impact on Extinction Ang]] | 2023 |
| [[交直流电力系统分割并行电磁暂态数字仿真方法|交直流电力系统分割并行电磁暂态数字仿真方法]] | 2023 |
| [[a-topology-based-simplified-dynamic-model-and-solving-algorithm-for-lcc-hvdc-con|A topology-based simplified dynamic model and solving algori]] | 2025 |
| [[a-topology-based-simplified-dynamic-model-and-solving-algorithm-for-lcc-hvdc-con|A topology-based simplified dynamic model and solving algori]] | 2025 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling and Simulation of Large P]] | 2025 |
| [[impedance-based-stability-analysis-of-the-multi-terminal-cascaded-hybrid-hvdc-sy|Impedance Based Stability Analysis of the Multi-terminal Cas]] | 2025 |
| [[2728multi-rate-real-time-hybrid-simulation-of-controllable-line-commutated-conve|Multi-rate real time hybrid simulation of controllable line ]] | 2026 |
| [[2728multi-rate-real-time-hybrid-simulation-of-controllable-line-commutated-conve|Multi-rate real time hybrid simulation of controllable line ]] | 2026 |
| [[2728multi-rate-real-time-hybrid-simulation-of-controllable-line-commutated-conve|Multi-rate real time hybrid simulation of controllable line ]] | 2026 |
| [[2728一种用于lcc-hvdc系统小干扰稳定性分析的改进动态相量模型|一种用于LCC-HVDC系统小干扰稳定性分析的改进动态相量模型]] | 2026 |
| [[2728一种用于lcc-hvdc系统小干扰稳定性分析的改进动态相量模型|一种用于LCC-HVDC系统小干扰稳定性分析的改进动态相量模型]] | 2026 |
