---
title: "Power Electronics Modeling"
type: model
tags: [power-electronics, modeling, switching, average-value, emt-simulation, vsc, converter]
created: "2026-05-04"
updated: "2026-05-15"
---

# Power Electronics Modeling（电力电子建模）

## 定义

电力电子建模（Power Electronics Modeling）是指在电磁暂态（EMT）仿真中对电力电子变换器及其开关器件进行数学描述和数值实现的技术。电力电子变换器包括电压源换流器（VSC）、电网换相换流器（LCC）、模块化多电平换流器（MMC）、DC-DC变换器等类型，广泛应用于HVDC输电、可再生能源并网、FACTS设备等场景。

电力电子系统的特点是包含高频开关动作和快速暂态过程，其EMT建模需要在**精度**和**效率**之间进行权衡。Sano等（2022）提出了五类模型的系统分类框架，将建模方法按精度和计算效率分为：详细开关模型（SW）、电压插值模型（VI）、平均值模型（AV）、受控电流注入模型（CCI）和简化电流注入模型（SCI）。

## EMT中的角色

电力电子建模在EMT仿真中承担以下核心功能：

1. **换流器暂态行为表征**：精确模拟换流器的高频开关动作、换相过程、谐波生成与传播
2. **控制策略验证**：在时域中验证PLL、功率外环、电流内环、调制策略等控制算法
3. **系统稳定性分析**：评估大规模电力电子并网系统的阻抗稳定性、谐振特性、故障穿越能力
4. **实时仿真加速**：通过模型简化（AVM、DEM等）在实时仿真中实现大步长计算

### 核心建模挑战

| 挑战类型 | 具体问题 | 影响 |
|---------|---------|------|
| 刚性系统 | 高频开关（ns-μs级）与机电动态（ms-s级）耦合 | 数值稳定性条件限制步长 |
| 开关事件检测 | 开关时刻的精确捕捉与插值 | 虚假数值振荡、开关损耗误差 |
| 大规模系统 | 包含数千个开关器件的场站聚合仿真 | 计算瓶颈 |
| 接口延迟 | AVM与传统EMTP程序的非迭代接口存在一拍延迟 | 大步长下数值不稳定 |

## 建模方法分类体系

根据Sano等（2022）的五类模型框架，电网并网逆变器的EMT建模方法可按如下分类：

### 五模型精度-效率映射（Sano 2022）

| 模型类型 | 符号 | 控制部件 | 功率器件 | 步长要求 | 计算效率 | 精度 |
|---------|------|---------|---------|---------|---------|------|
| 详细开关模型 | SW | 全部包含 | 电压源 | ≤ 开关周期/20 | 1×（基准） | 最高 |
| 电压插值模型 | VI | 全部包含 | 电压源+插值 | 开关周期/5~1/2 | 10~30× | 高 |
| 平均值模型 | AV | 去除调制 | 电压源 | 40~100 μs | 50~100× | 中 |
| 受控电流注入模型 | CCI | 仅功率控制 | 电流源 | 100~200 μs | 200~500× | 中 |
| 简化电流注入模型 | SCI | 全部去除 | 电流源 | 200~500 μs | 500×+ | 低 |

### 核心机制详解

#### 1. 详细开关模型（Switching Model, SW）

SW模型是最直接、最完整的建模方法，在EMT仿真中模拟功率器件的完整开通和关断操作。

**电路拓扑**：三相桥式逆变器连接至交流电感$L_f$、串联电阻$R_{fl}$和开关纹波滤波器（电容$C_f$、电阻$R_{fc}$）。

**开关函数定义**：开关函数$S(t) \in \{0, 1\}$描述器件状态，上桥臂导通时$S=1$，下桥臂导通时$S=0$。输出电压表示为：
$$v_{out}(t) = S(t) \cdot V_{dc}$$

**PWM调制**：正弦脉宽调制（SPWM）下，电压参考$v^*$与三角载波$v_{carrier}$比较生成门极信号。开关时刻$t_{fall}$和$t_{rise}$由代数计算精确获得，与仿真步长$T_s$无关。

**数值限制**：SW模型需要$T_s$足够小以捕捉开关瞬态。当$T_s$大于开关周期时，开关时刻分辨率下降，交流电流误差增加。

#### 2. 电压插值模型（Voltage Interpolation Model, VI）

VI模型在保持全部控制部件的同时，通过插值方法在大步长下精确模拟逆变器开关产生的谐波。

**核心原理**：在每个计算步长内，在开关转换时刻$t_{fall}$和$t_{rise}$前后插入插值电压，使该步长内VI模型的积分面积$S_{VI}$等于理论值$S_T$（见下图）。

**插值公式**（梯形积分法）：
$$\bar{s} = \frac{1}{2} + \frac{v^* - v_{carrier}}{h}$$

其中$h$为三角载波的斜率，由载波幅度和频率决定。

**步长扩展能力**：VI模型可将仿真步长扩展至开关周期的1/2至1/5，同时保持开关谐波精度。

#### 3. 平均值模型（Average-Value Model, AVM）

AVM忽略开关纹波，将变换器等效为受控电压/电流源，在同步旋转坐标系（dq0）下建立连续模型。

**状态空间平均法**（Middlebrook & Cuk 1976）：

交流侧电流方程（dq坐标系）：
$$L\frac{di_d}{dt} = v_d - Ri_d + \omega L i_q - v_{dc}s_d$$
$$L\frac{di_q}{dt} = v_q - Ri_q - \omega L i_d - v_{dc}s_q$$

其中$s_d$、$s_q$为dq坐标系下的调制信号。

**Park变换关系**：
$$\begin{bmatrix} v_d \\ v_q \end{bmatrix} = \frac{M}{2} \begin{bmatrix} \cos\delta \\ \sin\delta \end{bmatrix} v_{dc}$$

其中$M$为调制指数，$\delta$为功率角。

**直接接口AVM**（Ebrahimi & Jatskevich 2023）：传统间接接口（IDI-AVM）存在一拍延迟，导致大步长下数值不稳定。直接接口AVM（DI-AVM）将AVM公式按节点形式重新 formulation，使得AVM方程与网络方程同时求解，消除接口延迟。

DI-AVM的节点方程形式：
$$\begin{bmatrix} \mathbf{G}_{abc,dc}^{VSC} & \mathbf{Z}_{abc,dc}^{VSC} \\ -\mathbf{Z}_{dc,abc}^{VSC} & -Z_{dc,dc}^{VSC} \end{bmatrix} \begin{bmatrix} \mathbf{v}_{abc} \\ v_{dc} \end{bmatrix} = \begin{bmatrix} \mathbf{i}_{abc} \\ i_{dc} \end{bmatrix} + \begin{bmatrix} \mathbf{e}_{abc,dc}^{h,VSC} \\ e_{dc}^{h,VSC} \end{bmatrix}$$

#### 4. 受控电流注入模型（Controlled Current-Injection Model, CCI）

CCI模型在AVM基础上进一步简化，仅保留功率控制部分，去除电流内环控制，用电流源等效换流器。

**接口电流公式**：
$$\bar{i}_{dc} = \frac{3}{4}M\cos\phi \|\bar{i}_{qd}\|$$

其中$\phi$为功率因数角，$\|\bar{i}_{qd}|$为dq坐标系电流幅值。

**精度边界**：CCI模型无法准确处理快速电压变化引起的尖峰电流和过电压，适用于稳态和准稳态分析。

#### 5. 简化电流注入模型（Simplified Current-Injection Model, SCI）

SCI模型去除所有控制部件，仅用恒定电流源等效换流器，计算效率最高但精度最低。

**适用场景**：需要毫秒级步长的大规模系统机电暂态分析，不关注开关谐波和暂态细节。

### 各模型可模拟的事件类型（Sano 2022）

| 仿真目的 | SW | VI | AV | CCI | SCI |
|---------|----|----|----|-----|-----|
| 开关纹波电流 | ✓ | ✓ | ✗ | ✗ | ✗ |
| 开关谐波电压 | ✓ | ✓ | ✗ | ✗ | ✗ |
| 锁相环动态 | ✓ | ✓ | ✓ | ✓ | ✗ |
| 电流控制器响应 | ✓ | ✓ | ✓ | ✗ | ✗ |
| 直流电压故障 | ✓ | ✓ | ✓ | ✗ | ✗ |
| 交流故障（单相/三相） | ✓ | ✓ | ✓ | ✓ | ✗ |
| 故障穿越（FRT） | ✓ | ✓ | ✓ | ✓ | ✗ |
| 瞬态稳定性分析 | ✓ | ✓ | ✓ | ✓ | ✗ |
| 稳态电压分析 | ✓ | ✓ | ✓ | ✓ | ✓ |

## 形式化表达

### 核心方程汇总

**1. 开关函数定义**
$$S_k(t) = \begin{cases} 1 & \text{上桥臂导通} \\ 0 & \text{下桥臂导通} \end{cases}, \quad k \in \{a, b, c\}$$

**2. PWM开关时刻计算**
$$t_{fall} = \frac{v^* - v_{carrier}(t)}{h}, \quad h = \frac{2V_{dc}}{T_{carrier}}$$

**3. VI模型插值电压**
$$\bar{s} = \frac{1}{2} + \frac{v^* - v_{carrier}}{h}$$

**4. Park变换（abc → dq）**
$$\begin{bmatrix} v_d \\ v_q \end{bmatrix} = \frac{2}{3} \begin{bmatrix} \cos\theta_s & \cos(\theta_s - 2\pi/3) & \cos(\theta_s + 2\pi/3) \\ -\sin\theta_s & -\sin(\theta_s - 2\pi/3) & -\sin(\theta_s + 2\pi/3) \end{bmatrix} \begin{bmatrix} v_a \\ v_b \\ v_c \end{bmatrix}$$

**5. AVM接口方程**
$$i_{dc} = \frac{3}{4}M\cos\phi \|\bar{i}_{qd}\|$$

**6. DI-AVM节点导纳矩阵**
$$\mathbf{G}_{VSC} = \begin{bmatrix} \mathbf{Z}_{abc} & \mathbf{Z}_{abc,dc} \\ -\mathbf{Z}_{dc,abc} & -Z_{dc,dc} \end{bmatrix}^{-1}$$

**7. SW模型计算时间比**
$$\frac{T_{mes}}{T_{sim}} \approx \frac{T_{switch}}{T_s}$$

## 关键技术挑战

### 挑战1：开关事件精确捕捉

**问题**：当仿真步长$T_s$大于开关过渡时间时，开关时刻分辨率退化，导致开关损耗计算误差和虚假数值振荡。

**解决方案**：插值法精确捕捉开关时刻。Na（2023）的双线性伴随模型（BAM）在开关时刻实现$\rho=0$的数值无损耗特性，虚假损耗消除率达99%以上。

**典型参数**：
- 开关过渡时间：$t_{rise}, t_{fall} \approx 1-10 \, \mu s$
- 推荐插值精度：$\Delta t_{int} \leq 0.1 \, \mu s$

### 挑战2：AVM大步长稳定性

**问题**：传统IDI-AVM存在一拍接口延迟，导致大步长（>40 μs）下数值不稳定或误差增大。

**解决方案**：Ebrahimi & Jatskevich（2023）提出的DI-AVM通过节点 formulation消除接口延迟，允许1000 μs级步长：

| 接口类型 | 最大可用步长 | 误差 |
|---------|------------|------|
| IDI-AVM（无snubber） | < 100 μs | 失控 |
| IDI-AVM（$R_x = 10 \Omega$） | 400 μs | 稳态误差大 |
| DI-AVM | 1000 μs | < 1% |

### 挑战3：大规模系统计算负担

**问题**：含数千个换流器器件的大规模场站（如134台逆变器光伏电场）中，SW模型每个步长需处理大量开关状态变化。

**解决方案**：
- 平均值等效模型（AVM）：忽略开关细节，允许大步长
- 并行计算（GPU/FPGA）：Wang（2024）在FPGA上实现亚微秒级步长实时仿真
- 多速率仿真：将换流器与网络划分为不同速率子系统

### 挑战4：换相失败瞬态（LCC）

**问题**：电网换相换流器（LCC）在交流故障时发生换相失败，导致直流电流上升和换流失败。

**Hong（2022）AVM模型**：改进的LCC平均值模型，通过换相失败指数（CFI）检测换相失败状态：
$$CFI = \frac{\cos\alpha - \cos(\alpha+\mu)}{\cos\alpha - \cos\beta}$$

其中$\alpha$为触发角，$\mu$为换相角，$\beta$为备用角。

### 挑战5：谐波时域精度

**问题**：AVM和CCI模型丢失开关频率及以上谐波信息，无法进行谐波分析。

**解决方案**：VI模型通过分段线性插值保留开关谐波，精度接近SW模型但计算效率提高10-30倍。

## 量化性能边界

### 计算时间加速比（Sano 2022）

| 模型 | 步长$T_s$ | 计算时间比$T_{mes}/T_{sim}$ | 相对SW加速比 |
|------|-----------|---------------------------|-------------|
| SW | 2 μs | 1.0 | 1× |
| VI | 20 μs | 0.05~0.1 | 10~20× |
| AV | 50 μs | 0.015~0.02 | 50~70× |
| CCI | 100 μs | 0.005~0.002 | 200~500× |
| SCI | 200 μs | 0.002~0.001 | 500×+ |

### 平均值模型精度验证

**DAVM（2012）**验证数据：
- VSC-HVDC动态平均值模型
- 5 μs步长下CPU减少50-54%
- ≥40 μs步长下减少60-70%

**Misyris（2021）**验证数据：
- 构网型变流器（GFM）在满足时间尺度分离条件下
- RMS模型与EMT误差小于3%
- RMS计算时间缩短80-90%

**Ebrahimi（2023）**DI-AVM验证数据：
- 1000 μs步长下2-norm误差< 1%
- 相对于IDI-AVM在400 μs步长下的失控行为

### FPGA实时仿真（Wang 2024）

- 实现亚微秒级步长电力电子实时仿真
- 与离线EMT基准对比波形一致
- 适用于硬件在环（HIL）测试

## 适用边界与选择指南

### 模型选择决策表

| 应用场景 | 推荐模型 | 理由 |
|---------|---------|------|
| 器件级谐波分析、EMI预估 | SW | 需要完整开关细节 |
| 换流器控制系统设计与验证 | SW, VI | 需要电流控制器动态 |
| 谐振特性分析、谐波稳定性 | VI | 保留开关谐波，大步长 |
| 故障穿越、FRT验证 | SW, VI, AV, CCI | 需要换流器暂态响应 |
| 系统级机电暂态稳定性 | CCI, SCI | 需要长时间仿真 |
| HVDC并网故障分析 | SW, AV | 需要直流侧故障动态 |
| 实时仿真（硬件在环） | AV, CCI | 大步长，计算效率高 |
| 直流电网故障定位 | VI | 快速暂态响应 |

### 各模型失效场景

| 模型 | 失效场景 | 替代方案 |
|------|---------|---------|
| SW | 大规模系统实时仿真（计算量过大） | AV, CCI |
| VI | 需要ms级步长的机电暂态 | CCI, SCI |
| AV | 开关频率及以上谐波分析 | VI |
| CCI | 快速电压变化引起的尖峰电流 | SW, VI |
| SCI | 需要控制响应精度 | CCI, AV |

### 数据缺口声明

1. **五模型统一基准测试**：不同拓扑（两电平、三电平NPC、MMC、CHB）下的建模精度与加速比数据分散，缺乏标准化测试用例
2. **GFM与GFL模型对比**：构网型与跟网型换流器在故障穿越过程中的精度对比数据不足
3. **多换流器聚合等效**：大规模场站中数百台换流器的聚合等效模型精度边界尚无系统研究

## 相关模型

- [[vsc-model|VSC模型]] — 电压源换流器基础模型
- [[mmc-model|MMC模型]] — 模块化多电平换流器
- [[lcc-model|LCC模型]] — 电网换相换流器
- [[switching-model|开关模型]] — 开关器件建模基础
- [[dc-dc-converter|DC-DC变换器]] — 直流变换器拓扑
- [[average-value-model|平均值模型]] — 系统级AVM建模方法
- [[companion-circuit|伴随电路]] — 离散化等效方法
- [[interpolation-method|插值方法]] — 开关时刻精确捕捉
- [[ideal-switch-model|理想开关]] — 开关建模基础

## 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|---------|
| [[sano-2022-comparison|Sano 等 - Comparison and Selection of Grid-Tied Inverter Models for Accurate and Efficient EMT Simulations]] | 2022 | 五类模型框架（SW/VI/AV/CCI/SCI），步长-精度映射，500×加速比数据 |
| [[ebrahimi-2023-average-value|Ebrahimi 和 Jatskevich - Average-Value Model for Voltage-Source Converters With Direct Interfacing in EMTP-Type Solution]] | 2023 | DI-AVM节点formulation，消除一拍延迟，1000 μs步长稳定 |
| [[hong-2022-average-value|Hong 等 - Average-Value Modeling of Line-Commutated Inverter Systems With Commutation Failure]] | 2022 | LCC换相失败AVM，CFI指标，故障暂态验证 |
| [[ebrahimi-2021-average-value|Ebrahimi 等 - Average-Value Modeling of Line-Commutated AC-DC Converters With Unbalanced AC Network]] | 2021 | 不平衡交流网络下LCC平均值模型 |
| [[beddard-2015-comparison|Beddard 等 - Comparison of Detailed Modeling Techniques for MMC Employed on VSC-HVDC Schemes]] | 2015 | MMC详细建模技术对比 |
| [[na-2023-bilinear|Cao 等 - BAM双线性伴随模型]] | 2023 | 开关时刻数值无损耗特性，ρ=0 |

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*