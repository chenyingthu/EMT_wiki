---
title: "Modeling a voltage source converter assisted resonant current DC breaker for real time studies"
type: source
authors: ['Seyed', 'Sattar', 'Mirhosseini']
year: 2019
journal: "Electrical Power and Energy Systems, 117 (2019) 105678. doi:10.1016/j.ijepes.2019.105678"
tags: ['vsc']
created: "2026-04-13"
sources: ["EMT_Doc/26/Mirhosseini 等 - 2020 - Modeling a voltage source converter assisted resonant current DC breaker for real time studies.pdf"]
---

# Modeling a voltage source converter assisted resonant current DC breaker for real time studies

**作者**: Seyed, Sattar, Mirhosseini
**年份**: 2019
**来源**: `26/Mirhosseini 等 - 2020 - Modeling a voltage source converter assisted resonant current DC breaker for real time studies.pdf`

## 摘要

Modeling a voltage source converter assisted resonant current DC breaker Seyed Sattar Mirhosseinia,b, Siyuan Liua,c, Jose Chavez Muroa, Zhou Liud, Sadegh Jamalib, a Delft University of Technology, Faculty of EEMCS, Delft, the Netherlands b Iran University of Science and Technology, School of Electrical Engineering, Tehran, Iran c Xi’an Jiaotong University, Department of Electrical Engineering, State Key Laboratory of Electrical Insulation and Power Equipment, Xi’an, China

## 核心贡献


- 提出基于RTDS的VARC直流断路器系统级详细实时仿真模型
- 设计VSC等效电压源与开关RLC等效电路克服RTDS建模限制
- 实现含频率相关参数电缆的多端直流电网保护与开断联合仿真


## 使用的方法


- [[实时仿真|实时仿真]]
- [[小步长节点分析|小步长节点分析]]
- [[开关等效电路法|开关等效电路法]]
- [[vsc-model|VSC]]
- [[控制逻辑建模|控制逻辑建模]]


## 涉及的模型


- [[varc直流断路器|VARC直流断路器]]
- [[vsc-model|VSC]]
- [[谐振lc电路|谐振LC电路]]
- [[避雷器|避雷器]]
- [[限流电抗器|限流电抗器]]
- [[mtdc电网|MTDC电网]]
- [[频率相关电缆模型|频率相关电缆模型]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[直流断路器建模|直流断路器建模]]
- [[多端直流电网保护|多端直流电网保护]]
- [[频率相关建模|频率相关建模]]
- [[系统级仿真|系统级仿真]]
- [[故障开断特性|故障开断特性]]


## 主要发现


- 模型外部伏安特性与实际设备高度一致验证系统级仿真准确性
- 在含频率相关电缆的MTDC电网中成功验证保护算法与开断性能
- 等效建模方法避免导纳矩阵重算满足小步长实时仿真计算要求



## 方法细节

### 方法概述

基于RTDS小步长节点分析(small time step)的VARC直流断路器系统级实时仿真建模方法。采用开关RLC等效电路替代IGBT详细模型以克服RTDS建模限制，其中开关导通时等效为电感支路、关断时等效为RC串联支路，避免导纳矩阵重算。通过VSC等效电压源生成方波激励驱动LC谐振电路，向主断路器(MB)注入振荡电流创造人工电流过零点，结合分层控制逻辑实现故障检测、谐振电流注入、主断路器开断、能量耗散及隔离的完整开断过程仿真。

### 数学公式


**公式1**: $$$R_{L} = \frac{2L}{\Delta t}$$$

*开关导通状态下的等效电阻计算公式，其中L为等效电感，Δt为仿真时间步长*


**公式2**: $$$R_{RC} = \frac{\Delta t}{2C} + R_{C}$$$

*开关关断状态下的等效电阻计算公式，其中C为等效电容，RC为串联电阻*


**公式3**: $$$\frac{1}{2}CV^{2} = \frac{1}{2}LI^{2}$$$

*开关状态切换时的能量守恒约束条件，确保电容储能与电感储能相等以最小化能量损耗*


**公式4**: $$$V_{SA} = (1.5 \sim 1.6) \cdot V_{nominal,peak}$$$

*避雷器(SA)钳位电压设定，为直流系统额定峰值电压的1.5-1.6倍，用于限制开断过程中的过电压*


### 算法步骤

1. 初始化阶段：设置主断路器(MB)和残余断路器(RCB)为闭合状态(电阻1 mΩ)，故障模拟开关BKFAULT为开路状态(电阻10⁹ Ω)，系统正常运行负载电流

2. 故障注入阶段：通过LG_FLT触发按钮激活BKFAULT开关，电阻变为故障电阻值(接地故障)，故障持续时间由LG_FTIME参数控制

3. 故障检测与跳闸生成：保护系统检测故障电流，经过故障检测时间后生成跳闸信号Trip，触发VSC电压生成器使能信号OscEn置高

4. VSC电压生成：VSC Voltage Generator模块比较谐振电流IOSC与零值，产生方波电压VG输出至谐振LC电路，该模块采用小步长元件实现最小可能时间步长

5. 谐振电流注入与增长：VSC通过LC谐振电路向主断路器MB注入振荡电流IOSC，电流幅值按指数规律逐渐增大

6. 电流过零创造：当IOSC幅值等于线路故障电流幅值时，在MB触头间产生人工电流零点，为电流开断创造条件

7. 主断路器开断：MB在电流过零瞬间打开(电阻切换为10⁸ Ω)，线路电流换流至避雷器(SA)支路，SA将电压钳位至1.5-1.6倍额定峰值电压

8. 电流抑制与能量耗散：故障电流通过SA非线性电阻衰减，系统能量被SA吸收消耗，电流逐渐降至零

9. 残余断路器开断：当电流降至接近零时，RCB打开(电阻切换为10⁸ Ω)，实现故障线路与系统的物理隔离，消除谐振电路和SA上的电压

10. 系统状态保持与恢复：断路器保持隔离状态，或根据控制逻辑执行重合闸操作(若故障已清除)


### 关键参数

- **MB_open_resistance**: 10⁸ Ω

- **MB_close_resistance**: 1 mΩ

- **RCB_open_resistance**: 10⁸ Ω

- **RCB_close_resistance**: 1 mΩ

- **damping_factor**: δ (用户自定义阻尼系数，用于计算开关等效RLC参数)

- **SA_clamping_voltage**: 1.5-1.6 p.u. (额定峰值电压倍数)

- **normal_fault_switch_resistance**: 10⁹ Ω

- **simulation_timestep**: 小步长模式(small time step)，典型值1-50 μs(具体值取决于RTDS配置)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 简单测试电路验证(直流电压源+T型HVDC电缆) | VARC DC CB模型的外部电流-电压特性与实际物理设备特性高度一致，成功复现了从故障发生、谐振电流注入、电流过零创造到最终开断的完整波形。避雷器电压钳位特性符合1.5-1.6倍额定电压设定，谐振电流IOSC幅值与理论计算值吻合。 | 模型外部伏安特性与真实世界设备特性复现度一致，验证了系统级仿真的准确性 |

| 多端HVDC电网含频率相关参数电缆 | 在包含频率相关电缆模型的四端HVDC电网中，成功验证了保护算法与断路器开断性能的协调配合。故障检测、隔离与系统恢复全过程仿真稳定运行，VSC等效模型在不重算导纳矩阵的情况下实现了小步长实时仿真。 | 等效建模方法避免了传统详细IGBT模型导致的导纳矩阵重算问题，满足严格的小步长实时仿真计算要求(计算时间<物理时间) |



## 量化发现

- MB和RCB开路电阻值为10⁸ Ω，闭合电阻值为1 mΩ，电阻比达10¹¹量级，确保开关状态隔离度
- 避雷器(SA)钳位电压设定为直流系统额定峰值电压的1.5-1.6倍，确保故障电流可靠抑制
- 故障电流总开断时间由故障检测时间(保护系统)和断路器开断时间组成，其中断路器部分可在几毫秒内完成(current interruption within a few milliseconds)
- 正常工况下故障模拟开关BKFAULT电阻为10⁹ Ω，故障时切换为故障电阻值(低阻接地)
- 等效开关模型满足能量守恒约束：1/2 CV² = 1/2 LI²，确保状态切换时数值稳定性
- VSC电压生成器通过比较IOSC与零值产生方波，实现精确的频率控制和相位同步


## 关键公式

### 导通状态等效电阻公式

$$$R_{L} = \frac{2L}{\Delta t}$$$

*RTDS小步长环境中开关导通时等效为电感支路，用于节点分析计算*

### 关断状态等效电阻公式

$$$R_{RC} = \frac{\Delta t}{2C} + R_{C}$$$

*RTDS小步长环境中开关关断时等效为RC串联支路，与导通状态保持拓扑一致性*

### 开关状态切换能量守恒约束

$$$\frac{1}{2}CV^{2} = \frac{1}{2}LI^{2}$$$

*计算开关等效RLC参数时的约束条件，确保导通(电感)与关断(电容)状态间能量转移最小化，保证数值稳定性*



## 验证详情

- **验证方式**: 对比分析与系统级应用验证。通过对比模型外部伏安特性与实际设备特性进行验证，并在含频率相关电缆的多端直流电网中测试保护算法与开断性能的协调性。
- **测试系统**: 1) 简单测试电路：直流电压源+T型HVDC电缆+VARC DC CB；2) 多端HVDC电网：包含频率相关参数电缆模型的MTDC系统，用于保护配合验证。
- **仿真工具**: RTDS(Real Time Digital Simulator)实时仿真器，采用小步长环境(small time step)和Giga Processor Card(GPC)处理器卡。
- **验证结果**: 所提出的VARC DC CB模型外部电流-电压特性与实际设备高度一致，适用于系统级研究；在含频率相关电缆的MTDC电网中成功实现保护算法与开断性能的实时联合仿真，证明了模型在实时仿真环境中的鲁棒性和计算效率。
