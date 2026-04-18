---
title: "Independent power producer parallel operation modeling in transient network analysis"
type: source
authors: ['未知']
year: 2009
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/23/Moura 等 - 2010 - Independent power producer parallel operation modeling in transient network simulations for intercon.pdf"]
---

# Independent power producer parallel operation modeling in transient network analysis

**作者**: 
**年份**: 2009
**来源**: `23/Moura 等 - 2010 - Independent power producer parallel operation modeling in transient network simulations for intercon.pdf`

## 摘要

Independent power producer parallel operation modeling in transient network simulations for interconnected distributed generation studies Fabrício A.M. Moura a, José R. Camacho a,∗,1, Marcelo L.R. Chaves b, Geraldo C. Guimarães b a Universidade Federal de Uberlândia, School of Electrical Engineering, Rural Electricity and Alternative Sources Lab, PO Box 593, 38400.902 Uberlândia, MG, Brazil b Universidade Federal de Uberlândia, School of Electrical Engineering, Power Systems Dynamics Group, PO B

## 核心贡献


- 利用TACS模块实现S域传递函数离散化，构建含调速器与励磁的同步机完整暂态模型
- 采用IEEE Type I电压调节器替代简化模型，显著提升分布式电源并网暂态仿真精度
- 建立含公共耦合点等效电源与内部负荷的独立发电商并网配电网电磁暂态仿真框架


## 使用的方法


- [[tacs控制建模|TACS控制建模]]
- [[s域传递函数离散化|S域传递函数离散化]]
- [[atp-emtp电磁暂态仿真|ATP-EMTP电磁暂态仿真]]
- [[潮流初始化|潮流初始化]]


## 涉及的模型


- [[同步发电机|同步发电机]]
- [[ieee-type-i电压调节器|IEEE Type I电压调节器]]
- [[汽轮机调速器|汽轮机调速器]]
- [[配电网等效模型|配电网等效模型]]
- [[理想三相电源|理想三相电源]]


## 相关主题


- [[分布式发电并网|分布式发电并网]]
- [[独立发电商建模|独立发电商建模]]
- [[暂态网络分析|暂态网络分析]]
- [[甩负荷暂态分析|甩负荷暂态分析]]
- [[电压与频率稳定性|电压与频率稳定性]]


## 主要发现


- 甩负荷后耦合点电压升至1.08pu并稳态于1.06pu，超出标准限值，需加装电抗器抑制
- 采用详细电压调节器模型显著抑制暂态振荡，验证精细控制模型对提升并网稳定性的作用
- 调速器死区使转速波动维持在60Hz附近，频率保护未动作，系统依靠惯性快速恢复同步



## 方法细节

### 方法概述

本文采用ATP-EMTP电磁暂态仿真平台，结合TACS（控制系统暂态分析）模块构建独立发电商（IP）同步发电机及其控制系统的完整暂态模型。核心方法是将IEEE Type I型电压调节器与汽轮机调速器的S域传递函数通过数值离散化算法转换为时域差分方程，嵌入TACS控制回路中。仿真前通过潮流计算获取系统初始运行点，随后在ATP中搭建包含5MVA同步发电机、等效无穷大电网、耦合变压器及内部负荷的配电网拓扑。通过设置断路器动作与负荷投切事件，进行时域步进求解，精确捕捉电压、频率及励磁电流的毫秒级动态响应，以评估分布式电源并网对暂态稳定性的影响。

### 数学公式


**公式1**: $$G_{AVR}(s) = \frac{K_A}{1 + sT_A} \cdot \frac{1 + sT_F}{1 + sT_E} \cdot \frac{1}{1 + sT_R}$$

*IEEE Type I电压调节器S域传递函数，用于描述励磁系统对端电压偏差的动态响应与调节过程*


**公式2**: $$G_{GOV}(s) = \frac{1}{1 + sT_1} \cdot \frac{1 + sT_2}{1 + sT_3} \cdot \frac{1}{1 + sT_4} \quad (T_4=0 \text{ for steam turbine})$$

*汽轮机调速器S域传递函数，用于模拟原动机机械功率对转速偏差的调节特性*


**公式3**: $$y[k] = y[k-1] + \frac{\Delta t}{2} \left( u[k] + u[k-1] \right)$$

*TACS模块采用的梯形积分离散化公式，将S域连续控制模型转换为ATP时域差分方程以实现同步迭代*


### 算法步骤

1. 系统初始化：执行潮流计算，确定同步发电机端电压、有功/无功出力及内部负荷的稳态初始条件，设定发电机初始励磁电压与机械功率输入基准值。

2. 控制模型构建：在TACS中搭建IEEE Type I电压调节器与IEEE标准汽轮机调速器的S域传递函数框图，配置各环节增益、时间常数、反馈系数及输出限幅参数。

3. 离散化处理：利用ATP内置的梯形积分法则，将连续传递函数转换为离散状态空间方程或差分方程，确保控制信号采样步长与电磁网络求解步长严格同步。

4. 网络拓扑搭建：在ATP主网中配置5MVA同步发电机（SM 59模型）、6.6kV耦合变压器、无穷大等效电源及2.5MVA内部负荷，设置互连断路器、保护逻辑与测量节点。

5. 暂态事件注入：定义仿真时间轴，在指定时刻触发2.5MVA负荷切除或公共耦合点（CCP）三相短路故障，并配置断路器延时跳闸与孤岛切换逻辑。

6. 时域求解与数据记录：采用交替求解法（电磁网络与控制回路交替迭代），以微秒级步长推进仿真，实时记录母线电压、转子转速、励磁电压及频率响应曲线，并进行后处理分析。


### 关键参数

- **Sn**: 5 MVA

- **Un**: 6.6 kV

- **RA**: 0.004 pu

- **xd**: 1.8 pu

- **xq**: 1.793 pu

- **xd_prime**: 0.166 pu

- **xq_prime**: 0.98 pu

- **xd_double_prime**: 0.119 pu

- **xq_double_prime**: 0.17 pu

- **Td0_prime**: 1.754 s

- **H**: 74.8 kg·m²

- **f**: 60 Hz

- **内部负荷**: 2.5 MVA

- **初始功率因数**: 0.8滞后



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 独立发电商区域2.5MVA甩负荷 | 甩负荷瞬间，公共耦合点（母线3）电压从<1.05pu迅速攀升至峰值1.08pu，随后稳态维持在1.06pu（相间电压14.628kV）；发电商母线（母线4）电压瞬时升至1.03pu（7.128kV相间电压）。转子转速在188.25rad/s(59.92Hz)至188.92rad/s(60.14Hz)间振荡，最终稳定于188.49rad/s(60Hz)。电压调节器将励磁降至额定值的70%以抑制过电压。 | 相比文献[10,11]采用的简化电压调节器模型，本模型显著抑制了暂态振荡，系统响应更平稳，未出现频率保护误动，验证了精细控制模型对提升并网稳定性的作用。 |

| CCP三相短路及互连断路器延时跳闸 | 故障期间励磁电流大幅上升；t=8.2s断路器断开后，系统进入孤岛运行。电压调节器迅速降低励磁，使母线4电压恢复至约1.00pu，新稳态励磁约为原值的70%。孤岛后发电机转速上升至194.31rad/s（对应频率61.85Hz）。 | 验证了详细控制模型在孤岛工况下对电压恢复的精确跟踪能力，频率越限情况符合汽轮机调速器死区特性预期，为加装饱和电抗器抑制过电压提供了量化依据。 |



## 量化发现

- 甩负荷后CCP电压峰值达1.08pu，稳态值为1.06pu，超出标准允许范围（±10%）
- 发电商母线电压瞬时峰值为1.03pu（7.128kV相间电压）
- 甩负荷期间频率波动范围为59.92Hz~60.14Hz，未触发频率保护（阈值通常为58Hz或持续0.5s>60.14Hz）
- 孤岛运行后稳态频率升至61.85Hz（194.31rad/s）
- 电压调节器动作使稳态励磁电流降至额定值的70%
- 采用IEEE Type I详细模型后，暂态电压振荡幅度较简化模型显著降低，系统稳定性提升


## 关键公式

### IEEE Type I电压调节器传递函数

$$G_{AVR}(s) = \frac{K_A}{1 + sT_A} \cdot \frac{1 + sT_F}{1 + sT_E} \cdot \frac{1}{1 + sT_R}$$

*用于TACS模块中构建励磁控制系统，模拟电压偏差对励磁输出的动态调节，是抑制暂态过电压的核心控制方程*

### 梯形积分离散化公式

$$y[k] = y[k-1] + \frac{\Delta t}{2} \left( u[k] + u[k-1] \right)$$

*ATP-EMTP时域求解核心算法，将S域连续控制模型转换为离散差分方程以实现TACS与电磁网络的同步迭代*



## 验证详情

- **验证方式**: 电磁暂态仿真与对比分析
- **测试系统**: 含5MVA独立发电商同步发电机、2.5MVA内部负荷、耦合变压器及无穷大等效电网的配电网系统
- **仿真工具**: ATP-EMTP（Alternative Transients Program）结合TACS模块
- **验证结果**: 成功复现了甩负荷与短路孤岛工况下的电压/频率动态过程。仿真结果表明，采用离散化S域传递函数构建的详细IEEE Type I电压调节器模型能有效抑制暂态振荡，励磁与调速器动作逻辑符合物理预期，验证了该建模框架在分布式电源并网暂态分析中的高精度与工程适用性。
