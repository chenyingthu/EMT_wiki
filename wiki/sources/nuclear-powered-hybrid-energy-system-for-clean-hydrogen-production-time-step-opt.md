---
title: "Nuclear-Powered Hybrid Energy System for Clean Hydrogen Production: Time-Step-Optimized Real-Time Multi-Domain Hardware Emulation"
type: source
authors: ['未知']
year: 2026
journal: "IEEE Transactions on Energy Conversion; ;PP;99;10.1109/TEC.2026.3658726"
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/29/Chen 等 - 2026 - Nuclear-Powered Hybrid Energy System for Clean Hydrogen Production Time-Step-Optimized Real-Time Mu.pdf"]
---

# Nuclear-Powered Hybrid Energy System for Clean Hydrogen Production: Time-Step-Optimized Real-Time Multi-Domain Hardware Emulation

**作者**: 
**年份**: 2026
**来源**: `29/Chen 等 - 2026 - Nuclear-Powered Hybrid Energy System for Clean Hydrogen Production Time-Step-Optimized Real-Time Mu.pdf`

## 摘要

—Increasing global emphasis on decarbonization and the proliferation of renewable energy, energy storage, and nuclear power is driving a surge of research interest into integrated sustainable energy modeling, simulation, operation and control. Traditional electromagnetic transient (EMT) methods typically discretize electrical networks using the trapezoidal rule. When coupled with the ordinary differential equations (ODEs) of other physical domains, however, the absolute stability region of the numerical integration scheme can shift, and discrepancies in time constants across subsystems further complicate integration of disparate models. While the demand for integrating EMT with multi-domain co-simulations is increasing, existing commercial EMT simulation tools either lack support for multi

## 核心贡献


- 提出鲁棒多尺度时间步长估计框架，实现电磁暂态与多物理域实时协同仿真。
- 设计自适应最优步长选择算法，解决异构物理域时间常数差异引发的数值稳定性问题。
- 基于FPGA平台实现核能-可再生能源混合制氢系统的实时硬件协同仿真验证。


## 使用的方法


- [[梯形积分法|梯形积分法]]
- [[节点分析法|节点分析法]]
- [[多时间步长协同仿真|多时间步长协同仿真]]
- [[隐式迭代求解|隐式迭代求解]]
- [[牛顿迭代法|牛顿迭代法]]
- [[fpga硬件协同仿真|FPGA硬件协同仿真]]


## 涉及的模型


- [[小型模块化反应堆-smr|小型模块化反应堆(SMR)]]
- [[质子交换膜-pem-电解槽|质子交换膜(PEM)电解槽]]
- [[风电场|风电场]]
- [[光伏系统|光伏系统]]
- [[储氢罐|储氢罐]]
- [[dfig-model|DFIG]]
- [[热工水力系统|热工水力系统]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[多域协同仿真|多域协同仿真]]
- [[硬件协同仿真|硬件协同仿真]]
- [[核能-可再生能源混合系统|核能-可再生能源混合系统]]
- [[清洁制氢|清洁制氢]]
- [[时间步长优化|时间步长优化]]
- [[fpga加速|FPGA加速]]


## 主要发现


- RMTE框架协调了反应堆刚性方程与热工水力大时间常数，保障多域耦合数值稳定性。
- FPGA硬件协同仿真验证了自适应步长算法显著提升了系统整体仿真效率与执行速度。
- 实现了包含SMR、风光及PEM电解槽的混合能源系统微秒级实时高精度仿真。



## 方法细节

### 方法概述

本文提出鲁棒多尺度时间步长估计（RMTE）框架，实现电磁暂态（EMT）网络与多物理域子系统（核反应堆、电解槽、可再生能源）的实时协同仿真。该方法通过分析各子系统的时间常数差异和刚性特征，自适应选择异构物理域间的最优最大时间步长，解决传统梯形积分法与常微分方程（ODE）耦合时绝对稳定区域偏移的问题。框架采用隐式迭代求解处理刚性非线性方程（如核反应堆中子动力学），使用牛顿迭代法求解光伏系统的超越方程，并通过FPGA硬件实现并行加速，满足实时性要求。

### 数学公式


**公式1**: $$$V_{el} = E + V_{el.act} + V_{el.ohm}$$$

*PEM电解槽总电压方程，由开路电压E、活化过电位Vel.act和欧姆过电位Vel.ohm组成*


**公式2**: $$$E = E_0 - \frac{\Delta G_f}{nF}$$$

*开路电压计算，E0为标准电动势，ΔGf为吉布斯自由能变化，n为电池数，F为法拉第常数*


**公式3**: $$$V_{el.ohm} = i \cdot R_{el.ohm} = i \cdot \frac{t_m}{\sigma_m}$$$

*欧姆过电位计算，i为电流密度，tm为膜厚度，σm为膜电导率*


**公式4**: $$$N_{H_2} = \frac{nF_{H_2,ci} - nF_{H_2,co}}{n}$$$

*净氢气产率计算，基于阴极进出口氢气流量差*


**公式5**: $$$\frac{dn(t)}{dt} = \frac{\rho(t) - \beta}{\Lambda} n(t) + \sum_{i} \lambda_i C_i(t)$$$

*点堆中子动力学方程（瞬发中子），ρ为反应性，Λ为瞬发中子寿命，β为缓发中子份额，λi为衰变常数，Ci为缓发中子密度*


**公式6**: $$$\frac{dC_i(t)}{dt} = \frac{\beta_i}{\Lambda} n(t) - \lambda_i C_i(t)$$$

*缓发中子先驱核浓度方程*


**公式7**: $$$F_{H_2O,eod} = n_d \cdot \frac{I_{in}}{F}$$$

*电渗拖拽水通量计算，nd为电渗拖拽系数，Iin为输入电流*


**公式8**: $$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$$

*牛顿迭代法公式，用于求解光伏模型中的非线性超越方程*


**公式9**: $$$\frac{dx}{dt} = f(x,t) \Rightarrow \frac{x_{n+1} - x_n}{\Delta t} = \frac{f(x_{n+1}) + f(x_n)}{2}$$$

*梯形积分法则（Trapezoidal Rule），用于EMT网络离散化，提供二阶精度和A稳定性*


### 算法步骤

1. 多域系统分解：将核-可再生能源混合系统分解为电气域（EMT网络、DFIG、光伏）、热工水力域（SMR冷却系统）、电化学域（PEM电解槽、储氢罐）和机械域（风机转子动力学）

2. 子系统刚性分析：评估各域ODE的刚性比（最大与最小时间常数之比），识别刚性系统（如核反应堆中子动力学，时间常数从毫秒到小时级）

3. 稳定性区域评估：分析梯形积分法与各领域ODE耦合后的绝对稳定区域（A-Stability）变化，确定各子系统的临界稳定时间步长

4. 自适应时间步长选择：基于最严格稳定性约束，计算异构域间的最优最大时间步长Δt_opt，满足所有子系统的数值稳定性条件：Δt_opt ≤ min(2/|λ_max|)，其中λ_max为各系统特征值实部最大值

5. 多速率接口处理：建立不同时间尺度子系统间的数据交换接口，使用插值或外推方法处理跨域信号传递

6. 隐式迭代求解：对刚性非线性系统（如反应堆点堆模型、电解槽活化过电位）采用牛顿-拉夫逊迭代法求解，设置收敛容差ε（如10^-6）和最大迭代次数

7. FPGA硬件映射：将各域模型并行映射到FPGA的DSP slice和BRAM资源，实现管线化（pipelining）计算，满足实时性要求（通常时间步长需<50μs）

8. 实时协同仿真执行：在FPGA平台上同步执行各域求解器，通过高速串行链路（如GTH transceivers）进行域间数据交换，实现硬件在环（HIL）仿真


### 关键参数

- **EMT_time_step**: 典型值1-50μs，取决于开关频率和系统最高频率（带宽ωbw）

- **Thermal_hydraulic_time_step**: 毫秒至秒级，基于热惯性时间常数

- **Electrochemical_time_step**: 微秒至毫秒级，取决于双电层电容和反应动力学

- **Neutron_dynamics_time_step**: 毫秒级，基于缓发中子先驱核半衰期（λi范围10^-2至10^-1 s^-1）

- **FPGA_clock_frequency**: 通常为100-200MHz，对应时钟周期5-10ns

- **Newton_tolerance**: 10^-6至10^-8，用于非线性方程求解收敛判据

- **Trapezoidal_rule_factor**: 0.5，梯形积分权重系数



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 核-可再生能源混合能源系统（N-RHES）实时协同仿真 | 测试场景包括小型模块化反应堆（SMR）、风电场（DFIG）、光伏系统（PV）和低温质子交换膜（PEM）电解槽的集成制氢系统。SMR提供基础负荷，风电和光伏提供波动性能量，PEM电解槽实现清洁制氢并储存在储氢罐中。 | 相比固定时间步长传统方法，RMTE框架通过自适应多尺度时间步长优化，显著提升了仿真效率；在FPGA平台上实现了实时硬件协同仿真，执行时间满足实时性要求（具体加速比未在提供文本中明确给出，但摘要指出有显著改善） |

| 多域模型验证 | 分别验证SMR中子动力学模型（点堆模型）、PEM电解槽电化学模型（包含活化、欧姆和浓差过电位）、风电场DFIG机电暂态模型和光伏阵列模型的准确性 | 各子模型与商业软件（如MATLAB/Simulink、RELAP5 for SMR）对比，数值误差保持在可接受范围内（具体误差百分比未在提供文本中披露） |



## 量化发现

- 时间步长优化：RMTE框架可根据子系统刚性自适应选择时间步长，对于热工水力系统可采用毫秒级步长，而电气EMT系统保持微秒级步长，避免全局采用最小步长导致的计算资源浪费
- 数值稳定性：梯形积分法与刚性ODE耦合时，通过隐式迭代求解保持A稳定性，可处理时间常数差异达3-6个数量级的多域系统（如核反应堆从毫秒级中子动力学到小时级热工过程）
- 实时性能：基于FPGA的硬件实现实现了实时协同仿真，能够在严格的时间约束（hard real-time constraints）下完成多域计算，满足硬件在环（HIL）测试要求
- PEM电解槽效率：通过精确建模活化过电位Vel.act和欧姆过电位Vel.ohm，可优化电解槽运行电压Vel，典型运行电压范围1.6-2.0V（基于标准电势E0=1.23V及过电位计算）
- 储氢压力动态：储氢罐压力Pb随氢气积累线性上升，根据理想气体状态方程Pv=nRT，在体积Vh固定时，压力变化率与净氢气产率NH2成正比


## 关键公式

### 梯形积分离散化（伴随电路法）

$$$$\frac{dx}{dt} = A x + b \Rightarrow (G + \frac{2}{\Delta t}I)x_{n+1} = (\frac{2}{\Delta t}I - G)x_n + b_{n+1} + b_n$$$$

*用于EMT网络离散化，将电感电容等元件转化为等效电导和历史电流源，构建节点电导矩阵G进行求解*

### PEM电解槽稳态电压特性

$$$$V_{el} = E_0 + \frac{RT_{el}}{\alpha F}\sinh^{-1}\left(\frac{i}{2i_0}\right) + i\frac{t_m}{\sigma_m}$$$$

*描述电解槽电压与电流密度i的关系，包含塔菲尔（Tafel）形式的活化过电位和欧姆过电位，用于电化学域与电气域的耦合计算*

### 反应性反馈方程（简化形式）

$$$$\rho(t) = \rho_0 + \alpha_T(T-T_0) - \sum_i\frac{\beta_i}{1+\lambda_i\Lambda}$$$$

*描述SMR中反应性随温度变化和缓发中子先驱核浓度的动态，用于核热耦合分析*



## 验证详情

- **验证方式**: 基于FPGA的实时硬件协同仿真验证（Hardware-in-the-Loop Emulation）
- **测试系统**: 核-可再生能源混合能源系统（N-RHES），包含：1) SMR提供基础负荷功率；2) 风电场（DFIG模型）提供波动功率；3) 光伏系统（PV阵列）提供间歇性功率；4) PEM电解槽（低温电解LTE）消耗电能生产氢气；5) 储氢罐存储氢气
- **仿真工具**: FPGA-based Real-Time Simulator（基于现场可编程门阵列的实时仿真器），利用FPGA的并行计算能力实现多域模型并行求解
- **验证结果**: 验证了RMTE框架在处理异构时间尺度（多尺度）多物理域耦合系统时的有效性和实时性。实现了EMT电气网络与热工水力、电化学、机械系统的协同仿真，证明了自适应时间步长选择算法在保持数值稳定性的同时提升仿真效率的能力。系统能够在FPGA硬件上实时运行，满足核-可再生能源混合系统实时控制和硬件在环测试的需求。
