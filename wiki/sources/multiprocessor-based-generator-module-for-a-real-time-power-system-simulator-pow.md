---
title: "Multiprocessor based generator module for a real-time power system simulator - Power Systems, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multiprocessor based generator module for a real-time power system simulator.pdf"]
---

# Multiprocessor based generator module for a real-time power system simulator - Power Systems, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `27&28/Multiprocessor based generator module for a real-time power system simulator.pdf`

## 摘要

A new geneeator simulation module was developed for an electrical power system simulator. This simulator is on an analog simultaneous base. Therefore the module has to simulate a generator behavior precisely. Furthermore, it is required to be able to use the analog simulator as easily as an off- line simulation program. To meet the requirement, the developed generator module adopts a multiprocessor consisting of microprocessors and an analog three-phase sinusoidal oscillator. Any type of generator can be easily simulated only by changing the program of the microprocessors.

## 核心贡献


- 提出多微处理器发电机仿真模块架构，结合模拟三相振荡器实现平滑波形输出
- 采用四微处理器并行求解微分方程，显著缩短仿真步长以满足实时性要求
- 引入浮点运算避免数值误差，结合梯形积分法实现高精度电磁暂态动态求解


## 使用的方法


- [[多处理器并行计算|多处理器并行计算]]
- [[梯形积分法|梯形积分法]]
- [[浮点运算|浮点运算]]
- [[dq坐标变换|dq坐标变换]]
- [[数模混合仿真|数模混合仿真]]


## 涉及的模型


- [[同步发电机|同步发电机]]
- [[励磁控制系统-avr|励磁控制系统(AVR)]]
- [[调速系统-gov|调速系统(GOV)]]
- [[模拟三相正弦振荡器|模拟三相正弦振荡器]]
- [[输电线路与变压器|输电线路与变压器]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[混合仿真|混合仿真]]
- [[并行计算|并行计算]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[发电机动态建模|发电机动态建模]]


## 主要发现


- 四微处理器并行架构有效缩短计算耗时，使仿真步长满足模拟同步基实时要求
- 浮点运算结合梯形法显著抑制数值误差，模块输出与EMTP离线结果高度吻合
- 仅修改微处理器程序即可灵活模拟各类发电机，大幅降低传统模拟模块调参时间



## 方法细节

### 方法概述

该研究提出了一种基于多处理器（4个Intel 8086/8087微处理器）的同步发电机实时仿真模块，采用模拟-数字混合架构。核心思想是通过并行处理技术将电磁暂态仿真的计算步长缩短至模拟同步基（analog simultaneous base）可接受的范围（<5ms）。系统包含一个模拟三相正弦振荡器（0.1ms更新周期），用于生成平滑的三相电压波形（20V额定电压，0.2A额定电流）。数值求解采用梯形积分法（Trapezoidal method）配合浮点运算，以避免定点运算的极限环效应（limit cycle effect）。通过将发电机微分方程组（包含转子电路、AVR、调速器和运动方程）分配到多个处理器并行求解，并允许使用前一时步的变量值作为部分输入的近似，实现了计算加速。

### 数学公式


**公式1**: $$$$x(t+\Delta t) = Cx(t) + D[u(t) + u(t+\Delta t)]$$$$

*梯形积分法离散化形式，用于求解状态空间微分方程dx/dt=Ax+Bu。其中x为状态向量，u为输入向量，C和D为离散化系数矩阵。*


**公式2**: $$$$C = \left(I - \frac{\Delta t}{2}A\right)^{-1}\left(I + \frac{\Delta t}{2}A\right), \quad D = \frac{\Delta t}{2}\left(I - \frac{\Delta t}{2}A\right)^{-1}B$$$$

*梯形法的系数矩阵计算公式，I为单位矩阵，Δt为仿真步长，A和B为连续系统状态矩阵。*


**公式3**: $$$$E_a'' = E''\sin(2\pi ft + \theta), \quad E_b'' = E''\sin(2\pi ft + \theta - 2\pi/3), \quad E_c'' = E''\sin(2\pi ft + \theta + 2\pi/3)$$$$

*模拟三相正弦振荡器生成的内部电压参考值，f为频率参考值，θ为相角参考值，E''为内电势幅值。*


**公式4**: $$$$\psi_{ad} = X_{ad}''(I_d + I_{fd} + I_{1d}), \quad \psi_{aq} = X_{aq}''(I_q + I_{1q})$$$$

*d轴和q轴气隙磁链方程，X''为次暂态电抗，I_d、I_q为电枢电流，I_fd为励磁电流，I_1d、I_1q为阻尼绕组电流。*


**公式5**: $$$$E_{fd} = R_{fd}I_{fd} + \frac{d\psi_{fd}}{dt}, \quad E_{1d}' = R_{1d}I_{1d} + \frac{d\psi_{1d}}{dt}, \quad E_{1q}' = R_{1q}I_{1q} + \frac{d\psi_{1q}}{dt}$$$$

*转子绕组（励磁绕组和d、q轴阻尼绕组）的电压方程，R为绕组电阻，ψ为磁链。*


**公式6**: $$$$M\frac{d\omega}{dt} = T_m - T_e - P_d(\omega - \omega_0), \quad \frac{d\delta}{dt} = \omega - \omega_0$$$$

*转子运动方程（摇摆方程），M为转动惯量，ω为角速度，δ为相角，T_m为机械转矩，T_e为电磁转矩，P_d为机械阻尼系数，ω_0为额定角速度。*


### 算法步骤

1. 测量发电机端三相电压和电流，通过坐标变换计算d-q轴分量（需计算sin和cos三角函数）

2. 转子电路计算：求解d轴、q轴及阻尼绕组的电流微分方程（方程4-11），更新磁链和绕组电流

3. AVR（自动电压调节器）计算：根据发电机端电压偏差，通过三个一阶滞后环节计算励磁电压Efd

4. 调速器（GOV）计算：根据转速偏差Δω，通过一阶滞后环节计算机械转矩Tm

5. 转子动态计算：使用梯形法求解运动方程，更新角速度ω和相角δ

6. 内电势计算：根据磁链和电流计算d-q轴次暂态电势E''_d和E''_q，合成内部电压幅值E''和参考信号送至模拟振荡器


### 关键参数

- **simulation_time_interval_single_processor**: 13 ms

- **target_simulation_time_interval_parallel**: <5 ms

- **analog_oscillator_update_period**: 0.1 ms

- **number_of_microprocessors**: 4

- **processor_type**: Intel 8086 with 8087 floating-point co-processor

- **rated_voltage**: 20 V

- **rated_current**: 0.2 A

- **differential_equations_per_generator**: >10

- **trapezoidal_method**: used for numerical integration

- **arithmetic_type**: floating point (to avoid fixed point limit cycle effect)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 单处理器与多处理器性能对比 | 在单套8086/8087处理器上执行完整的六步发电机仿真程序，单步执行时间约为13ms，无法满足模拟同步基实时仿真的要求。采用四处理器并行架构后，通过将微分方程组分配到不同处理器并行求解，并采用前一时步变量近似当前输入的策略，成功将仿真步长缩短至5ms以内。 | 计算耗时从13ms降低至<5ms，加速比>2.6倍，满足实时仿真步长要求 |

| 与EMTP离线仿真精度验证 | 将多处理器发电机模块的仿真结果与离线电磁暂态仿真程序EMTP（Electro Magnetic Transients Program）进行对比验证。采用浮点运算替代定点运算，有效消除了定点运算的极限环效应（limit cycle effect），在长时间动态仿真中保持了数值稳定性。梯形积分法的使用确保了较小的数值误差积累。 | 与EMTP结果高度吻合，浮点运算显著抑制了数值误差，避免了定点运算的长时漂移问题 |



## 量化发现

- 单处理器（8086/8087）执行单步仿真耗时：13ms
- 四处理器并行处理后目标步长：<5ms（满足模拟同步基实时性要求）
- 模拟三相振荡器波形更新周期：0.1ms（产生平滑正弦波，即使参考信号在仿真步长内保持恒定）
- 系统额定电气参数：20V电压，0.2A电流（低电压设计便于操作）
- 单台发电机模型微分方程数量：>10个（含转子电路、AVR、调速器）
- 处理器架构：16位Intel 8086微处理器配合8087浮点协处理器
- 数值方法：梯形积分法（Trapezoidal method）具有优良的数值稳定性和精度
- 并行策略：采用前一时步变量替代当前输入的近似，误差可忽略（因Δt很小，状态变量偏差极小）


## 关键公式

### 梯形积分法离散化公式

$$$$x(t+\Delta t) = \left(I - \frac{\Delta t}{2}A\right)^{-1}\left(I + \frac{\Delta t}{2}A\right)x(t) + \frac{\Delta t}{2}\left(I - \frac{\Delta t}{2}A\right)^{-1}B[u(t) + u(t+\Delta t)]$$$$

*用于并行求解发电机状态空间微分方程组，是实时仿真的核心数值算法，确保数值稳定性和精度*

### 转子运动方程（摇摆方程）

$$$$M\frac{d^2\delta}{dt^2} + P_d\frac{d\delta}{dt} = T_m - T_e$$$$

*描述发电机转子机械动态，与电磁暂态方程耦合，在第五步（转子动态计算）中求解*

### 次暂态磁链方程

$$$$\begin{bmatrix} \psi_d \\ \psi_q \end{bmatrix} = \begin{bmatrix} X_{ad}'' & 0 \\ 0 & X_{aq}'' \end{bmatrix} \begin{bmatrix} I_d + I_{fd} + I_{1d} \\ I_q + I_{1q} \end{bmatrix}$$$$

*在d-q坐标系下计算发电机气隙磁链，用于确定内部电压和电磁转矩*



## 验证详情

- **验证方式**: 对比验证（与行业标准离线仿真程序EMTP进行结果比对）
- **测试系统**: 包含同步发电机、励磁系统（AVR，含三个一阶滞后环节）、调速系统（GOV，含一个一阶滞后环节）、传输线路和变压器的电力系统仿真器
- **仿真工具**: EMTP (Electro Magnetic Transients Program) - 作为基准离线仿真工具
- **验证结果**: 多处理器发电机模块的输出与EMTP离线仿真结果高度一致，验证了并行处理结合浮点运算的精度。浮点运算有效避免了定点运算在长时间仿真中出现的极限环效应和数值误差积累问题，证明了该实时仿真模块在精度和速度上的有效性。
