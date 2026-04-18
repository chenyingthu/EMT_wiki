---
title: "Analysis of the Harmonic Transmission Characteristics of HVDC Transmission Based on a Unified Port Theory Model"
type: source
authors: ['未知']
year: 2015
journal: "IEEE Journal of Quantum Electronics;2016;52;1;10.1109/JQE.2015.2509242"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/Analysis of the Harmonic Transmission Characteristics of HVDC Transmission Based on a Unified Port Theory Model.pdf"]
---

# Analysis of the Harmonic Transmission Characteristics of HVDC Transmission Based on a Unified Port Theory Model

**作者**: 
**年份**: 2015
**来源**: `07&08/Analysis of the Harmonic Transmission Characteristics of HVDC Transmission Based on a Unified Port Theory Model.pdf`

## 摘要

—In this paper, we demonstrate ultra-fast millimeter wave beam steering with settling times below 50 ps. A phased array antenna with two elements is employed to realize beam steering. The phased array feeder is implemented with a recently introduced time delay line that provides, at the same time, an ultra-fast tunability, broadband operation, and continuous tuning. Our implementation is used to perform symbol-by-symbol steering. In our demonstration, the beam direction is switched between two sequentially transmitted symbols toward

## 核心贡献


- 提出基于互补相移光谱的微波光子真延时线，实现宽带连续可调与超快波束控制
- 构建双单元相控阵馈电网络，实现低于五十皮秒的超快毫米波波束切换与符号级转向
- 验证符号级波束转向方案，支持十吉波特数据流，为高比特率多址接入提供新途径


## 使用的方法


- [[微波光子学处理|微波光子学处理]]
- [[真延时线技术|真延时线技术]]
- [[互补相移光谱方案|互补相移光谱方案]]
- [[延迟干涉仪与光相位调制|延迟干涉仪与光相位调制]]
- [[符号级波束转向|符号级波束转向]]


## 涉及的模型


- [[相控阵天线|相控阵天线]]
- [[馈电网络|馈电网络]]
- [[cpss-sct架构|CPSS-SCT架构]]
- [[光电探测器与光波导|光电探测器与光波导]]
- [[真延时线模型|真延时线模型]]


## 相关主题


- [[超快波束转向|超快波束转向]]
- [[毫米波通信|毫米波通信]]
- [[微波光子学|微波光子学]]
- [[无线接入网络|无线接入网络]]
- [[波束倾斜抑制|波束倾斜抑制]]
- [[高速多址接入|高速多址接入]]


## 主要发现


- CPSS方案在25%带宽内相位响应接近理想真延时，功率波动仅约1.5分贝
- 成功实现10 GBd数据流的符号级波束切换，两接收端间隔30度时切换稳定可靠
- 系统建立时间低于50皮秒，验证了超快波束转向实用性，可显著降低接收机功耗



## 方法细节

### 方法概述

本文提出一种基于微波光子学（MWP）的超快毫米波波束转向方案。核心采用互补相移光谱（CPSS）真延时线（TTD）技术替代传统电子移相器，以消除宽带信号下的波束倾斜（beam squint）。系统架构包含中心局（CO）与远程天线单元（RAU）。CO生成光载无线（RoF）数据信号与转向控制（SC）信号，通过光纤传输至RAU。RAU采用2×1相控阵天线（PAA），馈电网络利用CPSS模块对一路信号进行超快可调延时，另一路采用固定延时补偿路径差。两路光信号经光电探测器拍频生成35 GHz射频信号，驱动Vivaldi天线发射。通过符号级时间空间复用（TSDM），实现低于50 ps建立时间的波束切换，支持10 GBd数据流，显著降低终端接收机带宽需求与功耗。

### 数学公式


**公式1**: $$$P_{\text{out}} - P_{\text{in}} = L + G_t + G_r + \text{FSPL}$$$

*Friis传输公式，用于计算无线链路功率预算，包含链路损耗、收发天线增益与自由空间路径损耗。*


**公式2**: $$$\text{FSPL} = -20 \cdot \log_{10} \left( \frac{4\pi \cdot d \cdot f}{c} \right)$$$

*自由空间路径损耗公式，用于评估毫米波频段随距离和频率增加带来的传播衰减。*


**公式3**: $$$\Delta t = -\frac{x}{c} = -\frac{\sin \theta \cdot d}{c}$$$

*相控阵相邻天线单元所需的真延时差公式，其中$\theta$为波束指向角，$d$为阵元间距，$c$为光速。*


### 算法步骤

1. 信号生成与调制：使用任意波形发生器（AWG）生成10 Gbit/s TDM数据流与转向控制（SC）信号。数据流经根升余弦脉冲成形（滚降系数0.8）后，通过铌酸锂马赫-曾德尔调制器（MZM）加载至频率为$f_2$的连续波激光器上。

2. 光载无线（RoF）合成：将调制后的数据光信号与频率为$f_1$的参考激光器合束，产生频差为$f_{RF} = f_2 - f_1 = 35$ GHz的RoF信号。

3. 馈电网络延时分配：RoF信号在RAU处分为两路。第一路输入CPSS可调真延时模块，根据SC信号实时改变光谱相位斜率以实现超快延时调谐；第二路通过固定延时线（TD）补偿两臂物理路径差。

4. 光电转换与射频放大：两路光信号经光带通滤波器滤除EDFA带外噪声后，分别输入40 GHz光电探测器进行光外差拍频，生成35 GHz射频信号。随后经射频放大器提升至10 dBm。

5. 波束发射与同步控制：射频信号馈入间距为$\lambda$的2×1 Vivaldi天线阵列。严格控制SC信号与数据符号边沿同步，确保波束切换仅发生在符号过渡期，避免符号内干扰。

6. 终端接收与解调：相距30°的两个喇叭天线接收射频信号，经下变频与低通滤波后，由实时示波器捕获眼图并评估Q因子，验证符号级波束转向性能。


### 关键参数

- **载波频率**: 35 GHz

- **数据速率**: 10 GBd / 10 Gbit/s TDM

- **建立时间**: < 50 ps

- **相对带宽**: 17% (仿真) / 29% (实验)

- **滚降系数**: 0.8

- **天线阵列规模**: 2×1 (实验) / 16×16 (仿真)

- **阵元间距**: $\lambda$

- **接收机夹角**: 30°

- **射频输出功率**: 10 dBm



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 16×16阵列波束转向范围对比 | 在17%相对带宽下，CPSS-SCT方案支持120°转向范围，而传统移相器方案仅支持85°。增益平坦度保持在3 dB以内。 | CPSS-SCT方案转向范围比传统移相器方案提升约41%（120° vs 85°）。 |

| 符号级波束切换实验 | 在35 GHz载波上实现10 Gbit/s TDM信号的符号级切换，两用户间隔30°。建立时间低于50 ps，用户间功率抑制比约6 dB。 | 实现皮秒级切换，支持实时符号级空间复用，传统机械或电子方案无法达到此速度。 |

| 接收机带宽优化验证 | 对比10 GHz与5 GHz接收机带宽下的Q因子-OSNR曲线，两者性能高度吻合，5 GHz接收机可无损接收分配给单用户的5 Gbit/s数据。 | 接收机带宽需求降低50%，硬件成本与功耗显著下降，且信号质量无劣化。 |



## 量化发现

- 系统波束切换建立时间低于50 ps，满足符号级（10 GBd）实时转向需求。
- CPSS方案在25%设计带宽内相位响应逼近理想真延时，功率波动仅约1.5 dB。
- 16×16阵列仿真表明，CPSS-SCT在17%相对带宽下可实现120°无波束倾斜转向，较移相器方案提升35°。
- 实验测得两用户间信号功率抑制比约为6 dB，可通过增加阵列规模进一步优化。
- 接收机带宽从10 GHz降至5 GHz时，Q因子与OSNR关系曲线重合，证明终端硬件复杂度可线性降低。
- 传输距离增至5 m时，Q因子因自由空间损耗逐渐下降，验证了链路预算模型。


## 关键公式

### 自由空间路径损耗公式

$$$\text{FSPL} = -20 \cdot \log_{10} \left( \frac{4\pi \cdot d \cdot f}{c} \right)$$$

*用于评估毫米波频段（如35 GHz/60 GHz）无线链路的传播衰减，指导天线增益与发射功率设计。*

### 相控阵真延时差公式

$$$\Delta t = -\frac{\sin \theta \cdot d}{c}$$$

*计算相控阵馈电网络中相邻天线单元所需的精确延时量，以实现特定角度$\theta$的波束指向。*



## 验证详情

- **验证方式**: 硬件实验验证与数值仿真对比
- **测试系统**: 基于微波光子学的2×1毫米波相控阵远程天线单元（RAU）与光载无线（RoF）接入网络原型
- **仿真工具**: 任意波形发生器(AWG M8195A)、铌酸锂MZM、40 GHz光电探测器(Albis Opto)、实时示波器(DSO-X 96204Q)、定制Vivaldi天线阵列、光带通滤波器与EDFA
- **验证结果**: 实验成功验证了低于50 ps建立时间的符号级波束转向，支持10 Gbit/s数据流在35 GHz载波上的稳定传输。接收机带宽减半未导致性能下降，用户间隔离度达6 dB。仿真与实验结果一致，证实CPSS真延时方案在宽带、超快调谐场景下的优越性。
