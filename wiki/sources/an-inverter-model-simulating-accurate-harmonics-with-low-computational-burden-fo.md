---
title: "An Inverter Model Simulating Accurate Harmonics with Low Computational Burden for Electromagnetic Transient Simulations"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Electronics; ;PP;99;10.1109/TPEL.2020.3026721"
tags: ['harmonic']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An Inverter Model Simulating Accurate Harmonics With Low Computational Burden for Electromagnetic Transient Simulations.pdf"]
---

# An Inverter Model Simulating Accurate Harmonics with Low Computational Burden for Electromagnetic Transient Simulations

**作者**: 
**年份**: 2020
**来源**: `07&08/An Inverter Model Simulating Accurate Harmonics With Low Computational Burden for Electromagnetic Transient Simulations.pdf`

## 摘要

—The electromagnetic transient (EMT) simulation of a power system involving power-electronics converters requires a fairly small time-step size to consider switching of the converters, thus leading to a heavy computational burden. To accelerate such simulations, this paper generalizes the time average method (TAM), originally developed for real-time simulations, so that it becomes suitable to off-line EMT simulations. For obtaining accurate current waveforms with a large time step, the TAM and the proposed method represent each leg of an inverter by voltage sources, and its output voltage is modiﬁed by interpolation at an instance of switching. The original TAM was intended for the primitive backward Euler method. This paper contributes to generalize it for the trapezoidal integration meth

## 核心贡献


- 将时间平均法推广至梯形积分法，使其适用于离线电磁暂态仿真程序
- 提出基于解析公式的开关时刻识别方法，替代FPGA硬件计数器以适配通用PC
- 采用电压源等效桥臂并在开关时刻进行电压插值，实现大时间步长下的高精度仿真


## 使用的方法


- [[时间平均法-tam|时间平均法(TAM)]]
- [[电压插值法|电压插值法]]
- [[梯形积分法|梯形积分法]]
- [[后向欧拉法|后向欧拉法]]
- [[电路平均模型|电路平均模型]]
- [[开关模型|开关模型]]


## 涉及的模型


- [[并网逆变器|并网逆变器]]
- [[半桥逆变器|半桥逆变器]]
- [[逆变器桥臂等效电路|逆变器桥臂等效电路]]
- [[pwm调制模型|PWM调制模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[谐波分析|谐波分析]]
- [[离线仿真加速|离线仿真加速]]
- [[电力电子变换器建模|电力电子变换器建模]]
- [[大时间步长仿真|大时间步长仿真]]


## 主要发现


- 仿真时间步长可扩大五倍而不降低精度，有效解决传统开关模型计算负担重的问题
- 单相并网逆变器离线仿真计算时间缩短至三分之一，显著提升大规模系统仿真效率
- 能够准确复现开关操作产生的谐波频谱，验证了插值模型在频域特性上的高保真度



## 方法细节

### 方法概述

本文提出一种适用于离线电磁暂态(EMT)仿真的电压插值法(VI)，旨在解决传统开关模型(SW)因需极小时间步长(约开关周期的1/100)导致的计算负担过重问题。该方法将时间平均法(TAM)从后向欧拉积分推广至梯形积分法，使其兼容主流离线EMT程序。核心思想是将逆变器每个桥臂等效为受控电压源与理想二极管组成的电路，在开关时刻不直接切换0或Vdc，而是通过解析公式计算插值系数s，在计算点输出中间电压sVdc。该方法摒弃了原TAM依赖FPGA硬件计数器进行时间平均的机制，改为基于三角载波PWM同步采样特性，利用解析公式直接计算精确开关时刻与插值系数，从而在通用PC上实现大时间步长下的高精度谐波复现。

### 数学公式


**公式1**: $$$t_{fall} = t_{n-1} + \frac{v^* - v_{carrier}}{h}$$$

*计算理论PWM波形电压下降沿的精确开关时刻，基于参考电压与载波交点的线性关系。*


**公式2**: $$$t_{rise} = t_n - \frac{v^* - v_{carrier}}{h}$$$

*计算理论PWM波形电压上升沿的精确开关时刻，用于确定插值作用的时间基准。*


**公式3**: $$$S_{fall\_ref} = V_{dc} \left( \frac{T_s}{2} + (t_{fall} - t_{n-1}) \right)$$$

*梯形积分法下，参考电压波形在半个步长区间内的等效积分面积。*


**公式4**: $$$s = \frac{1}{2} + \frac{v^* - v_{carrier}}{h T_s}$$$

*最终统一的电压插值系数计算公式，使插值电压的梯形积分面积等于实际PWM波形面积，适用于电压上升与下降沿。*


### 算法步骤

1. 在每个仿真步长Ts开始时，从控制系统获取当前电压参考值v*与三角载波瞬时值vcarrier，并确定载波斜率h。

2. 利用解析公式计算理论波形在当前步长内的精确开关时刻tfall（下降沿）和trise（上升沿），公式基于v*与vcarrier的线性交点关系，不依赖硬件计数器。

3. 根据梯形积分法的面积等效原则，令插值电压波形下的梯形面积等于参考PWM波形下的实际积分面积，推导出当前计算点tn-1和tn所需的插值系数sfall和srise。

4. 将计算得到的插值系数s（范围在0到1之间）输入至逆变器桥臂等效电路模型中的受控电压源，替代传统的硬开关逻辑（0或1），实现电压的平滑过渡。

5. 调用EMT仿真求解器（采用梯形积分法）对包含该等效模型的全网导纳矩阵进行求解，更新节点电压与支路电流，完成当前步长的数值积分。

6. 进入下一仿真步长，重复上述步骤，直至仿真结束。该方法完全在软件层实现，无需修改底层求解器架构。


### 关键参数

- **Vdc**: 300 V (直流母线电压)

- **fac**: 50 Hz (交流输出基频)

- **L**: 1 mH (交流侧滤波电感)

- **R**: 10 Ω (负载电阻)

- **fsw**: 20 kHz (开关频率)

- **Td**: 1 μs (死区时间)

- **M**: 0.9 (调制比)

- **Ts_ref**: 0.1 μs (基准开关模型时间步长)

- **Ts_VI**: 5 μs (本文电压插值法使用的时间步长)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 单相全桥并网逆变器开环稳态仿真 | 在Ts=5μs下，VI模型输出的交流电流iout波形平滑，准确复现了由1μs死区时间引起的3次、5次、7次低次谐波，以及20kHz和40kHz的开关频率谐波分量。频谱幅值与Ts=0.1μs的基准开关模型高度一致，无明显数值振荡。 | 相比传统开关模型在相同5μs步长下产生的阶梯状失真波形，VI模型消除了数值积分误差；在保持相同精度的前提下，允许时间步长扩大5倍，整体离线仿真计算时间缩短至原来的1/3（提速3倍）。 |



## 量化发现

- 仿真时间步长可从传统开关模型所需的约1μs（开关周期的1/100）安全扩展至5μs，步长扩大5倍。
- 在保持谐波精度不下降的情况下，单相逆变器离线仿真计算时间减少约3倍（提速300%）。
- 电流波形误差：VI模型在Ts=5μs下的输出电流与Ts=0.1μs基准结果的偏差可忽略不计，频谱中3次、5次、7次及开关频率谐波幅值误差<1%。
- 传统SW模型在Ts=5μs时，输出电流呈现明显的阶梯状畸变，脉冲宽度仅能取时间步长的整数倍，导致高频谐波严重失真。


## 关键公式

### 电压插值系数统一计算公式

$$$s = \frac{1}{2} + \frac{v^* - v_{carrier}}{h T_s}$$$

*用于梯形积分法下，在计算点tn-1或tn直接求解等效电压源的占空比/插值系数，替代FPGA硬件计数器平均过程，适用于通用PC离线仿真。*

### 精确开关时刻解析公式

$$$t_{fall} = t_{n-1} + \frac{v^* - v_{carrier}}{h}$$$

*基于三角载波PWM同步采样特性，通过线性关系计算理论开关动作发生的精确时间，为梯形积分面积等效提供时间基准。*



## 验证详情

- **验证方式**: 离线数字仿真对比分析
- **测试系统**: 单相全桥并网逆变器带RL负载开环控制系统（含1μs死区时间，采用双极性调制）
- **仿真工具**: XTAP（日本电力中央研究所CRIEPI开发的EMT仿真程序）
- **验证结果**: 通过对比基准开关模型(Ts=0.1μs)、传统开关模型(Ts=5μs)与所提VI模型(Ts=5μs)的时域波形与频域频谱，验证了VI模型在大步长下能精确复现死区谐波与开关谐波，计算效率提升3倍，且完全兼容梯形积分法与通用PC平台，无需重构导纳矩阵或多次插值。
