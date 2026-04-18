---
title: "Adaptive Heterogeneous Transient Analysis of Wind Farm Integrated Comprehensive AC/DC Grids"
type: source
authors: ['未知']
year: 2021
journal: "IEEE Transactions on Energy Conversion;2021;36;3;10.1109/TEC.2020.3043307"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Lin 等 - 2021 - Adaptive Heterogeneous Transient Analysis of Wind Farm Integrated Comprehensive ACDC Grids.pdf"]
---

# Adaptive Heterogeneous Transient Analysis of Wind Farm Integrated Comprehensive AC/DC Grids

**作者**: 
**年份**: 2021
**来源**: `05/Lin 等 - 2021 - Adaptive Heterogeneous Transient Analysis of Wind Farm Integrated Comprehensive ACDC Grids.pdf`

## 摘要

—The increasingly complex AC/DC network as a result of the massive integration of wind farms manifests the signiﬁcance of a comprehensive transient study. In this work, the wind turbine (WT) and the DC grid are modeled in detail for the electromagnetic transient (EMT) simulation to maximize its ﬁdelity, whilst the AC grid transient stability is analyzed by dynamic simulation (DS). An interactive EMT-DS interface is thus introduced to enable their concurrency and subsequently form a co-simulation. The CPU which is dominant in system study faces a tremendous challenge in handling a great number of components albeit they exhibit homogeneity. The many-core graphics processing unit (GPU) fea- turing massive parallelism is therefore exploited and following the deﬁnition of an adaptive computing 

## 核心贡献


- 提出EMT-DS交互接口，实现风机直流网电磁暂态与交流网机电暂态并发协同仿真
- 构建自适应CPU-GPU异构架构，按组件同质性灵活分配串行与并行计算任务
- 对双馈风机进行拓扑重构与解耦，生成低维子系统以适配GPU的SIMT并行范式


## 使用的方法


- [[emt-ds协同仿真|EMT-DS协同仿真]]
- [[cpu-gpu异构并行计算|CPU-GPU异构并行计算]]
- [[拓扑重构与内部解耦|拓扑重构与内部解耦]]
- [[梯形积分法离散化|梯形积分法离散化]]
- [[状态空间建模|状态空间建模]]


## 涉及的模型


- [[dfig-model|DFIG]]
- [[风力发电机|风力发电机]]
- [[交直流电网|交直流电网]]
- [[多端直流电网|多端直流电网]]
- [[变压器|变压器]]
- [[变流器|变流器]]
- [[感应电机|感应电机]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[并行计算|并行计算]]
- [[风电场建模|风电场建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[机电暂态仿真|机电暂态仿真]]
- [[异构计算架构|异构计算架构]]
- [[系统稳定性分析|系统稳定性分析]]


## 主要发现


- 所提异构框架相比纯CPU计算实现显著加速，大幅提升大规模风电场仿真效率
- 仿真结果与PSCAD及DSATools对比验证，模型精度满足工程分析要求
- 拓扑重构有效降低系统数值阶数并提升同质性，充分释放GPU大规模并行算力



## 方法细节

### 方法概述

提出一种面向风电场交直流混合电网的自适应异构CPU-GPU协同仿真架构。该方法将风机与直流电网采用电磁暂态(EMT)详细建模以最大化保真度，交流电网采用机电暂态(DS)进行稳定性分析。通过定义自适应计算边界，根据组件同质性与数量动态分配计算任务：CPU处理同质性低、数量少的部分（如交流网、MMC外环控制、直流线路），GPU利用SIMT范式并行处理高度同质化的大规模组件（如DFIG子系统、MMC子模块）。对DFIG进行拓扑重构与内部解耦，降低数值阶数并提升同质性，结合CUDA C++编程实现高效并发计算，最终形成EMT-DS交互协同仿真框架，有效解决大规模系统仿真中的计算瓶颈问题。

### 数学公式


**公式1**: $$$$\dot{x}(t) = Ax(t) + Bu(t), \quad y(t) = Cx(t)$$$$

*感应电机5阶状态空间方程，用于描述定子与转子磁链/电流动态*


**公式2**: $$$$\frac{d\omega_r(t)}{dt} = -\frac{F}{J}\omega_r + \frac{P}{J}(T_e(t) - T_m(t))$$$$

*转子机电运动微分方程，耦合电磁转矩与机械转矩*


**公式3**: $$$$\nu(t) = \left(I - \frac{A\Delta t}{2}\right)^{-1} \left[ \left(I + \frac{A\Delta t}{2}\right)\nu(t-\Delta t) + \frac{B\Delta t}{2}(u(t) + u(t-\Delta t)) \right]$$$$

*梯形积分法离散化通用公式，用于将微分方程转化为代数方程进行EMT步进求解*


**公式4**: $$$$v_{SM} = i_{SM}r_{on} + g_1 \int \frac{i_{SM}}{C} dt + (g_1 - \text{sgn}(i_{SM}))2V_f + (g_1 + \text{sgn}(i_{SM}) - 1)V_j$$$$

*MMC子模块电压精确模型，包含IGBT导通电阻、电容积分、二极管压降及结电压*


**公式5**: $$$$v_{GF}(t) = \sqrt{V_{gd}^2 + V_{gq}^2} \cdot \sin\left(\int \omega_0 dt + k\frac{\pi}{3}\right), \quad k=0,1,2$$$$

*构网型(GF)MMC三相电压参考生成公式，为风电场提供独立电压支撑*


### 算法步骤

1. 系统初始化与组件分类：根据电网拓扑识别各组件数量与同质性特征，预设CPU与GPU的计算任务分配策略。

2. 自适应边界判定：基于预设阈值（MMC电平数约15级，风机数量约100台）动态选择纯CPU、纯GPU或异构协同模式。若规模低于阈值则回退至CPU串行计算以保证效率。

3. 交流网机电暂态求解(CPU)：求解同步发电机微分-代数方程组，计算节点电压幅值与相角，并通过零阻抗线接口转换为时域正弦函数传递给直流侧。

4. 直流网EMT外环与线路计算(CPU)：CPU执行MMC外环控制器（定直流电压/有功、定交流电压/无功）及直流线路/变压器求解，生成调制信号与边界条件。

5. GPU大规模并行内核启动：将调制信号与边界数据拷贝至CUDA显存。启动AVC与BC内核处理各相/子模块控制，并行计算所有MMC子模块电压；随后启动DFIG内核，并行求解解耦后的感应电机、变压器与变流器子系统。

6. 数据同步与网络方程求解：GPU计算结果（子模块电压、风机注入电流）回传至CPU。CPU汇总历史电流，构建并求解节点导纳矩阵，更新全网电压与电流分布。

7. 时间步推进与边界自适应更新：完成当前步长计算后，根据系统规模变化或故障扰动重新评估计算负载，动态调整下一时间步的CPU/GPU任务划分，循环直至仿真结束。


### 关键参数

- **仿真步长**: Δt (梯形积分法离散化)

- **测试硬件平台**: 192 GB RAM, 20核 Intel Xeon E5-2698 v4 CPU, NVIDIA Tesla V100 GPU

- **MMC电平阈值**: 约15级 (低于此值CPU更优)

- **风机数量阈值**: 约100台 (低于此值CPU更优)

- **最大测试规模**: 401电平MMC, 8000台DFIG



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| MMC电平数变化测试 | 在10秒仿真中，对比不同电压等级MMC的计算耗时。当MMC电平数达到401级时，GPU并行计算展现出显著优势。 | 相比纯CPU计算，GPU实现约10倍加速；在15电平附近出现性能交叉点，低于该值时CPU效率更高。 |

| 风电场规模扩展测试 | 测试风机数量从5台增至8000台时的计算效率。当8000台DFIG承担主要计算负载时，GPU加速比稳定在较高水平。 | GPU加速比在8000台风机场景下波动于20倍左右；阈值约在100台风机处，低于此规模时异构框架自动回退至CPU模式。 |

| EMT-DS协同仿真验证 | 在IEEE 39节点交流网与CIGRÉ B4直流网互联系统中进行故障暂态分析，验证模型保真度与接口数据交换稳定性。 | 仿真波形与商业软件PSCAD/EMTDC及DSATools结果高度一致，验证了异构架构在保持高保真度的同时大幅提升计算效率。 |



## 量化发现

- 在401电平MMC仿真中，GPU相比纯CPU实现约10倍加速。
- 当风电场规模达到8000台DFIG时，GPU加速比稳定在20倍左右。
- CPU与GPU性能交叉阈值确定为：MMC约15电平，风机约100台。
- 低于阈值时，GPU并行执行时间稳定在29至35秒区间，此时CPU串行计算更具效率。
- 自适应框架(ASP2)的效率曲线始终位于或重叠于纯CPU/GPU曲线之上，确保在任何规模下均能维持最优计算效率。


## 关键公式

### 梯形积分离散化方程

$$$$\nu(t) = \left(I - \frac{A\Delta t}{2}\right)^{-1} \left[ \left(I + \frac{A\Delta t}{2}\right)\nu(t-\Delta t) + \frac{B\Delta t}{2}(u(t) + u(t-\Delta t)) \right]$$$$

*用于所有微分方程（感应电机、变压器、转子运动）的时域离散，是EMT仿真步进求解的核心数学基础*

### MMC子模块精确电压方程

$$$$v_{SM} = i_{SM}r_{on} + g_1 \int \frac{i_{SM}}{C} dt + (g_1 - \text{sgn}(i_{SM}))2V_f + (g_1 + \text{sgn}(i_{SM}) - 1)V_j$$$$

*用于详细建模MMC内部IGBT与二极管开关特性，实现高保真度电磁暂态仿真*

### DFIG转子机电运动方程

$$$$\frac{d\omega_r(t)}{dt} = -\frac{F}{J}\omega_r + \frac{P}{J}(T_e(t) - T_m(t))$$$$

*描述风机机械转矩与电磁转矩的动态平衡，是机电-电磁耦合仿真的关键接口*



## 验证详情

- **验证方式**: 对比仿真验证（与商业软件结果进行波形与动态特性对比）
- **测试系统**: IEEE 39节点交流系统 + CIGRÉ B4多端直流电网基准模型 + 大规模DFIG风电场
- **仿真工具**: PSCAD/EMTDC (EMT验证), DSATools (DS验证), 自定义CUDA C++异构仿真框架
- **验证结果**: 所提详细建模与异构计算框架在IEEE 39节点与CIGRÉ B4互联系统中通过验证。EMT侧波形与PSCAD/EMTDC高度吻合，DS侧动态响应与DSATools一致。自适应边界策略有效避免了GPU在低规模下的性能损耗，在保持高保真度的前提下实现了最高20倍的计算加速，证明了其在复杂交直流电网暂态分析中的实用性与高效性。
