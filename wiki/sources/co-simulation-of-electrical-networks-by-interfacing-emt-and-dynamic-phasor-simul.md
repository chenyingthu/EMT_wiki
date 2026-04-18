---
title: "Co-simulation of electrical networks by interfacing EMT and dynamic-phasor simulators"
type: source
authors: ['K. Mudunkotuwa']
year: 2018
journal: "Electric Power Systems Research, 163 (2018) 423-429. doi:10.1016/j.epsr.2018.06.010"
tags: ['cosimulation']
created: "2026-04-13"
sources: ["EMT_Doc/10/Mudunkotuwa和Filizadeh - 2018 - Co-simulation of electrical networks by interfacing EMT and dynamic-phasor simulators.pdf"]
---

# Co-simulation of electrical networks by interfacing EMT and dynamic-phasor simulators

**作者**: K. Mudunkotuwa
**年份**: 2018
**来源**: `10/Mudunkotuwa和Filizadeh - 2018 - Co-simulation of electrical networks by interfacing EMT and dynamic-phasor simulators.pdf`

## 摘要

Co-simulation of electrical networks by interfacing EMT and dynamic- b Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB, R3T 5V6, Canada The paper presents a hybrid co-simulator comprising EMT and dynamic phasor-based simulators. The EMT simulator models portion(s) of the network wherein fast transients are prevalent and detailed modeling is ne- cessary. The dynamic phasor solver models the rest of the network using extended-frequency Fourier compo-

## 核心贡献


- 提出EMT与动态相量混合协同架构，实现网络分区高效求解
- 开发瞬时EMT与动态相量样本精确映射算法，保障接口数据传递精度
- 解决多速率时间步长接口问题，确保大范围谐波仿真下的数值稳定性


## 使用的方法


- [[动态相量法|动态相量法]]
- [[多速率仿真|多速率仿真]]
- [[傅里叶级数展开|傅里叶级数展开]]
- [[梯形积分法|梯形积分法]]
- [[节点导纳矩阵法|节点导纳矩阵法]]
- [[接口数据映射算法|接口数据映射算法]]


## 涉及的模型


- [[ieee-118节点系统|IEEE 118节点系统]]
- [[风电场|风电场]]
- [[电力电子变流器|电力电子变流器]]
- [[输电网络|输电网络]]
- [[旋转电机|旋转电机]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[多速率仿真|多速率仿真]]
- [[网络分区|网络分区]]
- [[谐波分析|谐波分析]]
- [[数值稳定性|数值稳定性]]
- [[风电场建模|风电场建模]]


## 主要发现


- 在不同时间步长比下验证接口精度，混合仿真显著降低整体计算耗时
- 基于IEEE 118节点系统验证协同架构的数值稳定性与波形还原精度
- 动态相量法有效替代外部网络详细建模，在保证精度前提下大幅提升效率



## 方法细节

### 方法概述

本文提出一种基于传输线解耦的EMT与动态相量(DP)混合协同仿真架构。该方法将电网划分为需详细建模的快速暂态区域（EMT侧）和动态较慢的外部网络（DP侧），利用Bergeron无损传输线模型的固有传播延迟实现两侧节点方程的自然解耦。针对多速率仿真需求，设定DP侧步长ΔT为EMT侧步长Δt的整数倍，并在同步时刻进行数据交换。核心创新在于开发了瞬时EMT样本到扩展频率动态相量的精确映射算法：通过提取基波分量并从瞬时值中减去，直接构造包含直流与所有谐波的基频复合动态相量，避免了传统方法中对各次谐波逐一进行数值积分的庞大计算量。同时引入线性插值处理非同步时刻的中间数据，并可选配阻尼因子α以吸收高频分量，确保多速率接口下的数值稳定性与波形还原精度。

### 数学公式


**公式1**: $$$x(t-T+s) = x_0(t) + 2\text{Re}\left(\sum_{h=1}^{+\infty} x_h(t) e^{j h \frac{2\pi}{T} (t-T+s)}\right)$$$

*动态相量时域重构公式，利用滑动窗口内的傅里叶级数展开表示任意时刻波形*


**公式2**: $$$X(t) = x_0(t)e^{-j\frac{2\pi}{T}(t-T+s)} + 2\sum_{k=1}^{+\infty} x_h(t) e^{j(h-1)\frac{2\pi}{T}(t-T+s)}$$$

*基频复合动态相量定义，将全频谱谐波压缩至单一基频复数，大幅简化网络导纳矩阵求解规模*


**公式3**: $$$H_k(t) = \left[\frac{2V_m(t-\tau)}{Z_c} - H_m(t-\tau)\right]e^{-j\tau\frac{2\pi}{T}}$$$

*DP侧传输线历史电流源注入公式，利用延迟τ实现两侧求解器解耦*


**公式4**: $$$x(t) = \text{Re}\left(X(t)e^{j\frac{2\pi}{T}t}\right)$$$

*DP至EMT瞬时值转换公式，直接将基频复合相量还原为时域样本*


### 算法步骤

1. 网络分区与接口配置：将含电力电子变流器等快速暂态源的区域划为EMT子系统，其余电网划为DP子系统。在分区边界配置一段具有传播延迟τ的传输线作为解耦接口，设定EMT步长Δt与DP步长ΔT（满足ΔT=nΔt且ΔT≤τ）。

2. 同步时刻数据交换准备：在kΔT时刻，EMT侧输出瞬时电压/电流样本x(t)，DP侧输出基频复合动态相量X(t)。

3. DP至EMT转换：利用公式x(t)=Re(X(t)e^{j(2π/T)t})将DP侧相量直接还原为瞬时值，注入EMT侧传输线模型计算历史电流源。

4. EMT至DP转换（核心映射）：首先通过傅里叶积分计算瞬时波形x(t)的基波分量x_1(t)；随后计算x(t)-2Re(x_1(t)e^{j(2π/T)(t-T+s)})得到直流与高次谐波合成项；最后结合基波项按扩展频率动态相量定义重构复合相量X(t)，避免逐次谐波积分。

5. 多速率插值与步进：在kΔT至(k+1)ΔT之间，DP侧保持状态不变，EMT侧以Δt独立推进。EMT侧所需的历史DP数据通过kΔT与(k-1)ΔT时刻的相量线性插值获得。

6. 高频阻尼处理（可选）：若接口处高频分量显著，在EMT至DP转换过程中引入阻尼因子α∈[0,1]对高频项进行衰减，防止DP/TS侧因带宽不足引发数值振荡。


### 关键参数

- **时间步长比_n**: 25 (对应ΔT=500μs, Δt=20μs)

- **传输线延迟_τ**: 需满足τ≥ΔT以支持解耦

- **最小接口线长_lmin**: ≈150 km (对应500μs步长，光速3×10^5 km/s)

- **阻尼因子_α**: 0.93~0.97 (用于TS-EMT接口稳定性控制)

- **仿真总时长**: 3 s



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 等步长协同仿真(20μs:20μs) | 验证接口算法保真度。EMT与DP侧电压/电流波形完全重合，扩展频率动态相量完整保留全频段谐波，与全EMT基准误差可忽略不计。 | 波形重合度100%，验证了映射算法在等步长下的无损特性 |

| 多速率协同仿真(500μs:20μs) | 验证加速效果与低频精度。Bus 10与Bus 30的电压/电流低频暂态轨迹与全EMT高度一致，高频开关纹波被自然滤除。风电场端基波RMS电压、有功/无功功率曲线与基准重合。 | 低频动态误差<1%，计算耗时从694秒降至132秒，加速比5.26倍 |

| 简化模型加速验证 | 将详细风电场模型替换为受控动态电压源，进一步降低EMT侧计算负担。 | 仿真耗时降至32秒，较全EMT加速比达21.69倍 |



## 量化发现

- 在25:1时间步长比下，协同仿真计算耗时从694秒降至132秒，速度提升5.26倍。
- 接口映射算法在等步长(20μs)条件下实现与全EMT仿真的波形完全一致，高频谐波保留率100%。
- 多速率(500μs:20μs)仿真下，基波RMS电压、有功及无功功率动态响应误差<1%，低频暂态特征完整还原。
- 传输线接口最小长度需满足l_min≈3×10^5×ΔT，500μs步长对应至少150km物理线路。
- 引入阻尼因子α=0.93~0.97可有效抑制TS-EMT接口处的高频数值振荡，恢复仿真稳定性。


## 关键公式

### 基频复合动态相量方程

$$$X(t) = x_0(t)e^{-j\frac{2\pi}{T}(t-T+s)} + 2\sum_{k=1}^{+\infty} x_h(t) e^{j(h-1)\frac{2\pi}{T}(t-T+s)}$$$

*用于将全频谱谐波压缩至单一基频复数，使DP侧网络只需求解单一频率等效电路，大幅降低计算维度*

### EMT至DP样本映射核心等式

$$$x(t-T+s) = 2\text{Re}\left(x_1(t)e^{j\frac{2\pi}{T}(t-T+s)}\right) + \left(\sum_{h\neq -1,1} x_h(t)e^{-j(h-1)\frac{2\pi}{T}(t-T+s)}\right)e^{j\frac{2\pi}{T}(t-T+s)}$$$

*通过分离基波与直流/高次谐波项，避免对EMT瞬时波形进行全频段傅里叶积分，直接高效构造复合相量*

### 多速率同步与解耦条件

$$$\Delta T = n\Delta t \quad \text{且} \quad \Delta T \le \tau$$$

*确保DP侧大步长与EMT侧小步长整数倍对齐，且传输线延迟足以隔离两侧求解器，防止代数环*



## 验证详情

- **验证方式**: 纯数字仿真对比验证（全EMT基准 vs 混合协同仿真）
- **测试系统**: IEEE 118节点三相系统，含450MW Type-4风电场（75台6MW机组聚合模型，3节点EMT侧，115节点DP侧）
- **仿真工具**: PSCAD/EMTDC（EMT侧，含详细开关级变流器模型）、自定义动态相量求解器（DP侧）、TCP/IP控制网络接口
- **验证结果**: 在1.8s施加Bus 8三相接地故障（6周期后清除）场景下，验证了等步长与25:1多速率协同的精度。多速率方案在保留低频机电暂态精度的同时，计算效率提升5.26倍，最高可达21.69倍，证明了接口算法的数值稳定性与工程实用性。
