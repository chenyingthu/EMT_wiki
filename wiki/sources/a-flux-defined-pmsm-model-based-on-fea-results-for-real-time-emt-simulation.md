---
title: "A Flux-Defined PMSM Model Based on FEA Results for Real-Time EMT Simulation"
type: source
authors: ['Dong Li']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112427. doi:10.1016/j.epsr.2025.112427"
tags: ['real-time', 'pmsm']
created: "2026-04-13"
sources: ["EMT_Doc/01/Li 等 - 2025 - A Flux-Defined Pmsm Model Based on Fea Results for Real-Time Emt Simulation.pdf"]
---

# A Flux-Defined PMSM Model Based on FEA Results for Real-Time EMT Simulation

**作者**: Dong Li
**年份**: 2025
**来源**: `01/Li 等 - 2025 - A Flux-Defined Pmsm Model Based on Fea Results for Real-Time Emt Simulation.pdf`

## 摘要

A Flux-Defined PMSM Model Based on FEA Results for Real-Time To expedite the PMSM design and test process, high-fidelity PMSM model derived from Finite Element Analysis (FEA) has been studied by many researchers. This paper proposed a new approach to calculate derivatives of currents with flux linkage data, which does not require taking hours to inverse the data table. Detailed math­ ematical proof is reported, based on which the implementation is explained, including presenting an efficient

## 核心贡献


- 提出基于磁链数据直接求解电流导数的方法，免去传统查表反演耗时。
- 设计高效三线性插值与外推平滑策略，提升实时仿真数值稳定性。
- 将FEA降阶模型部署于RTDS平台，实现亚微秒步长实时电磁暂态仿真。


## 使用的方法


- [[有限元分析-fea|有限元分析(FEA)]]
- [[查表法-lut|查表法(LUT)]]
- [[降阶模型-rom|降阶模型(ROM)]]
- [[三线性插值|三线性插值]]
- [[外推平滑算法|外推平滑算法]]
- [[dq0坐标变换|dq0坐标变换]]


## 涉及的模型


- [[pmsm-model|PMSM]]
- [[pmsm-model|PMSM]]
- [[集中参数电机模型|集中参数电机模型]]
- [[电动汽车动力总成|电动汽车动力总成]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[基于有限元的降阶建模|基于有限元的降阶建模]]
- [[空间谐波与磁饱和建模|空间谐波与磁饱和建模]]
- [[硬件在环测试|硬件在环测试]]
- [[电动汽车动力总成仿真|电动汽车动力总成仿真]]


## 主要发现


- 模型在RTDS上以小于1微秒步长稳定运行，计算效率显著优于传统FEA联合仿真。
- 仿真结果与FEA及集中参数模型对比验证，新模型能精确捕捉空间谐波与饱和效应。
- 外推平滑策略有效解决查表越界数值振荡，保障电动汽车工况下的仿真精度。



## 方法细节

### 方法概述

本文提出一种基于磁链定义的永磁同步电机（FD-PMSM）降阶模型，用于实时电磁暂态（EMT）仿真。传统方法需通过迭代反演磁链-电流查表（LUT）以获取电流，耗时数小时。本文创新性地直接利用有限元分析（FEA）预计算的磁链数据求解电流导数（$di/dt$），构建“电流-磁链-电流导数”关联，彻底免去LUT反演过程。模型采用三线性插值算法高效获取运行点处的磁链及其偏导数，并引入预平滑外推策略解决暂态越界时的数值振荡问题。最终将电机等效为受控电流源接入EMT网络，实现亚微秒级步长的实时高精度仿真。

### 数学公式


**公式1**: $$$$\begin{cases} u_d = R_s i_d + \frac{\partial \phi_d}{\partial i_d} \frac{di_d}{dt} + \frac{\partial \phi_d}{\partial i_q} \frac{di_q}{dt} + \frac{\omega_e}{p} \frac{\partial \phi_d}{\partial \theta} - \omega_e \phi_q \\ u_q = R_s i_q + \frac{\partial \phi_q}{\partial i_d} \frac{di_d}{dt} + \frac{\partial \phi_q}{\partial i_q} \frac{di_q}{dt} + \frac{\omega_e}{p} \frac{\partial \phi_q}{\partial \theta} + \omega_e \phi_d \end{cases}$$$$

*核心电压-电流导数方程。通过全微分展开定子电压方程，将磁链偏导数项分离，构建关于$di_d/dt$和$di_q/dt$的线性方程组，用于直接求解电流变化率。*


**公式2**: $$$$u_0 = R_s i_0 + \frac{\partial \phi_0}{\partial i_d} \frac{di_d}{dt} + \frac{\partial \phi_0}{\partial i_q} \frac{di_q}{dt} + \frac{\omega_e}{p} \frac{\partial \phi_0}{\partial \theta}$$$$

*零序电压方程。在求解出$d$、$q$轴电流导数后，用于计算零序电流分量，完整考虑三相不对称工况。*


**公式3**: $$$$f(O') = C_{000}(1-x)(1-y)(1-z) + C_{100}x(1-y)(1-z) + C_{010}(1-x)y(1-z) + C_{001}(1-x)(1-y)z + C_{101}x(1-y)z + C_{011}(1-x)yz + C_{110}xy(1-z) + C_{111}xyz$$$$

*三线性插值公式。将运行点映射至归一化单位立方体$(x,y,z)$内，利用8个顶点的已知LUT值$C_{ijk}$计算任意运行点的磁链或转矩值。*


**公式4**: $$$$\frac{\partial f(O')}{\partial x} = C_{000}(-1)(1-y)(1-z) + C_{100}(1)(1-y)(1-z) + C_{010}(-1)y(1-z) + C_{001}(-1)(1-y)z + C_{101}(1)(1-y)z + C_{011}(-1)yz + C_{110}(1)y(1-z) + C_{111}(1)yz$$$$

*插值函数偏导数公式。用于计算$\partial \phi / \partial i$和$\partial \phi / \partial \theta$，其计算复杂度低于插值本身，且中间变量可复用，显著提升实时计算效率。*


### 算法步骤

1. 1. FEA数据预计算：在$i_d$、$i_q$和转子位置$\theta$的指定范围内进行三维扫描，利用有限元软件计算并存储对应的$d$、$q$、$0$轴磁链（$\phi_d, \phi_q, \phi_0$）及电磁转矩（$T_e$），生成3D查表（LUT）。

2. 2. 坐标归一化映射：在仿真每一步，获取当前运行点$(i_{d,op}, i_{q,op}, \theta_{op})$，通过线性变换将其映射至相邻LUT索引构成的单位立方体内，得到归一化坐标$(x, y, z)$。

3. 3. 插值与偏导计算：利用三线性插值公式计算当前点的磁链值，同时利用偏导数公式计算$\partial \phi / \partial i_d$、$\partial \phi / \partial i_q$和$\partial \phi / \partial \theta$。复用中间变量以降低计算量。

4. 4. 求解电流导数：将插值得到的磁链及其偏导数代入核心电压方程，结合上一时刻的电压$u_d, u_q$和转速$\omega_e$，构建二元一次线性方程组，直接求解出$di_d/dt$和$di_q/dt$。

5. 5. 零序分量计算：将已求得的$di_d/dt$和$di_q/dt$代入零序方程，计算零序电流$i_0$或其导数，完成三相电流重构。

6. 6. 网络接口与积分：将计算出的电流导数进行数值积分得到下一时刻电流值，以受控电流源形式注入EMT网络，并采用补偿策略保证接口稳定性。

7. 7. 越界外推处理：若运行点超出LUT预设范围，采用预平滑外推策略。在仿真前预先计算并扩展LUT边界数据，消除独立外推导致的边界不连续，确保暂态大电流下的数值稳定性。


### 关键参数

- **LUT电流扫描范围**: ±150 A（验证工况），±300 A（对比工况）

- **LUT电流步长**: 30 A

- **LUT转子位置范围**: 0°~60°（对应2对极电机）

- **LUT位置步长**: 1°

- **LUT总记录数**: 11 × 11 × 61 = 7381 条

- **仿真时间步长**: < 1.0 µs（理论能力），验证测试1.5 µs，EV案例2.0 µs

- **外推扩展索引**: extp = 10^6 A（概念值），实际测试扩展至±300 A



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 开路（OC）与短路（SC）基准测试 | 在1000 Ω对地电阻（近开路）和1 Ω对地电阻（短路）条件下，对比FEA与FD-PMSM模型。电压波形中的空间谐波高度吻合，转矩RMS值匹配良好。仅因线性插值导致转矩脉动幅值存在微小偏差。 | 与Ansys/Maxwell FEA瞬态分析结果高度一致，验证了模型在稳态与极端短路工况下的精度。 |

| 反演LUT法对比测试 | 将所提方法与传统的LUT反演法进行对比。两者波形几乎完全重合，单步计算耗时相近（主要计算量均在插值环节）。 | 精度与反演法持平，但彻底省去了构建反演LUT所需的数小时预处理时间，大幅缩短模型部署周期。 |

| 三相接地故障暂态测试 | 施加0.025 s三相接地故障，故障清除瞬间峰值瞬态电流达200~250 A。使用±150 A范围LUT的模型进入外推区，波形与±300 A全范围模型高度接近，故障清除后迅速重合。 | 预平滑外推策略有效抑制了越界振荡，在电流超出原始LUT边界约66%时仍保持数值稳定与趋势正确。 |

| 电动汽车（EV）动力总成全系统仿真 | 在150 kW、1000 V直流母线电压的EV系统中，测试静态加速与50 km/h稳态运行。模型准确捕捉了终端电压、电流、转矩及调制波形中的低频空间谐波。 | 相比传统集中参数模型，额外揭示了可能引发过调制和转矩控制环设计偏差的高次谐波细节，证明其在HIL控制设计中的必要性。 |



## 量化发现

- 实时仿真步长可稳定运行于< 1.0 µs（RTDS Novacor 2.0平台实测1.5 µs与2.0 µs），满足亚微秒级EMT仿真需求。
- LUT数据规模为7381条记录，单点FEA计算耗时约1~2秒，总预处理时间可控；免去反演LUT节省数小时计算时间。
- 故障清除瞬态峰值电流达200~250 A，超出原始LUT边界（±150 A）时，外推模型波形与全范围模型（±300 A）偏差极小，趋势完全一致。
- 数据粒度直接影响精度：将电流步长从30 A增至60 A、位置步长从1°增至4°时，空间谐波与饱和效应的捕捉精度显著下降。
- 三线性插值偏导数计算的中间变量可直接复用至插值计算，有效降低单步浮点运算量，保障实时性。


## 关键公式

### FD-PMSM核心电流导数求解方程

$$$$\begin{cases} u_d = R_s i_d + \frac{\partial \phi_d}{\partial i_d} \frac{di_d}{dt} + \frac{\partial \phi_d}{\partial i_q} \frac{di_q}{dt} + \frac{\omega_e}{p} \frac{\partial \phi_d}{\partial \theta} - \omega_e \phi_q \\ u_q = R_s i_q + \frac{\partial \phi_q}{\partial i_d} \frac{di_d}{dt} + \frac{\partial \phi_q}{\partial i_q} \frac{di_q}{dt} + \frac{\omega_e}{p} \frac{\partial \phi_q}{\partial \theta} + \omega_e \phi_d \end{cases}$$$$

*用于在已知上一时刻电压、转速及插值所得磁链偏导数的情况下，直接构建线性方程组求解$di_d/dt$和$di_q/dt$，替代传统反演查表法。*

### 三线性插值与偏导复用公式

$$$$f(O') = \sum_{i,j,k \in \{0,1\}} C_{ijk} \cdot w_{ijk}(x,y,z)$$$$

*在3D LUT中快速计算任意运行点$(i_d, i_q, \theta)$的磁链值及其对电流和角度的偏导数，是模型实时计算的核心算法。*

### 预平滑外推索引扩展公式

$$$$\begin{cases} i_{d,\text{index}} = [-\text{extp}, -150, \dots, 150, \text{extp}] \\ i_{q,\text{index}} = [-\text{extp}, -150, \dots, 150, \text{extp}] \end{cases}$$$$

*在仿真前预先扩展LUT边界，通过平均冲突边界点消除独立外推的不连续性，确保大电流暂态工况下的数值稳定性。*



## 验证详情

- **验证方式**: 仿真对比验证（与高精度FEA软件、传统集中参数模型及反演LUT模型进行多维度基准测试）
- **测试系统**: 包含理想速度源/电压源驱动的PMSM单机系统（含开/短路、负载突变、三相接地故障），以及150 kW电动汽车全动力总成系统（含DC-DC、DC-AC逆变器、FOC-MTPA控制器）
- **仿真工具**: RSCAD (RTDS Novacor 2.0 实时仿真平台), Ansys/Maxwell (有限元分析基准)
- **验证结果**: 所提FD-PMSM模型在<1 µs步长下实现实时运行，电压空间谐波与转矩RMS值与FEA高度一致；预平滑外推策略成功解决暂态越界振荡问题；EV案例证明模型能准确反映影响控制性能的低频谐波与转矩脉动，有效弥合电机设计与驱动系统HIL测试之间的鸿沟。
