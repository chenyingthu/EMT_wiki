---
title: "Interpolation for power electronic circuit simulation revisited with matrix exponential and dense outputs"
type: source
authors: ['Peng Li']
year: 2020
journal: "Electric Power Systems Research, 189 (2020) 106714. doi:10.1016/j.epsr.2020.106714"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/25/Li 等 - 2020 - Interpolation for power electronic circuit simulation revisited with matrix exponential and dense ou.pdf"]
---

# Interpolation for power electronic circuit simulation revisited with matrix exponential and dense outputs

**作者**: Peng Li
**年份**: 2020
**来源**: `25/Li 等 - 2020 - Interpolation for power electronic circuit simulation revisited with matrix exponential and dense ou.pdf`

## 摘要

Interpolation for power electronic circuit simulation revisited with matrix Peng Li, Zixiang Meng, Xiaopeng Fu⁎, Hao Yu, Chengshan Wang Key Laboratory of Smart Grid of Ministry of Education, Tianjin University, Tianjin, China With a high penetration of power electronic equipment, transient simulation for power electronic circuit has been a main challenge for performance improvement of the electromagnetic transient simulation tools. In this

## 核心贡献


- 提出基于矩阵指数与密集输出公式的两种L稳定求解器，优化积分与插值组合
- 设计匹配策略实现积分与高阶插值最优组合，提升开关事件处理精度
- 开发三阶高精度与一阶高效求解器，克服现有工具在电力电子仿真中的精度瓶颈


## 使用的方法


- [[矩阵指数积分法|矩阵指数积分法]]
- [[padé逼近|Padé逼近]]
- [[密集输出公式|密集输出公式]]
- [[高阶插值|高阶插值]]
- [[状态空间法|状态空间法]]
- [[缩放平方算法|缩放平方算法]]


## 涉及的模型


- [[tcr|TCR]]
- [[vsc-model|VSC]]
- [[电力电子电路|电力电子电路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[电力电子电路仿真|电力电子电路仿真]]
- [[开关事件插值|开关事件插值]]
- [[数值积分算法|数值积分算法]]
- [[仿真精度与效率|仿真精度与效率]]


## 主要发现


- 三阶求解器在电力电子仿真中精度显著优于现有主流电磁暂态仿真工具
- 一阶求解器以更低计算成本实现同等精度，大幅提升仿真运算速度
- TCR与VSC-HVDC算例验证了新求解器在开关事件处理上的高精度与高效性



## 方法细节

### 方法概述

本文提出一种基于矩阵指数积分与密集输出公式的电磁暂态仿真新框架。针对传统EMTP类工具在电力电子开关事件处因线性插值导致的精度下降问题，该方法利用状态空间模型构建增广矩阵，通过Padé逼近计算矩阵指数实现时间积分。核心创新在于引入缩放平方算法生成密集输出点，无需额外计算成本即可获取步长内的高精度中间状态。结合提出的“积分-插值匹配策略”，将矩阵指数积分与高阶插值最优组合，实现开关时刻的精确捕捉。所设计的两种求解器均具备L稳定性，分别针对高精度与高计算效率场景优化，有效克服了传统梯形法在高频开关仿真中的数值振荡与精度瓶颈。

### 数学公式


**公式1**: $$$\dot{x}(t) = Ax(t) + Bu(t)$$$

*电力电子电路的状态空间微分方程，A、B为含开关状态二值矩阵的系数矩阵*


**公式2**: $$$x(t_0 + h) = [I_n \quad 0] \cdot e^{h\mathbf{A}} \cdot x_0$$$

*矩阵指数积分核心公式，通过增广矩阵$\mathbf{A}$和初始向量$x_0$实现单步状态精确推进*


**公式3**: $$$e^{hA} - r_{k,m}(hA) = O(h^{k+m+1})$$$

*Padé有理函数逼近的局部截断误差表达式，通过调整分子分母阶数k,m控制积分精度*


**公式4**: $$$x(t_0 + \frac{h}{2^{s-i}}) = [I_n \quad 0] \cdot e^{\frac{h}{2^{s-i}}\mathbf{A}} \cdot x_0, \quad i=0,1,\dots,s-1$$$

*密集输出公式，利用缩放平方中间结果零成本生成步长内分数时刻状态，为高阶插值提供内点*


### 算法步骤

1. 建立电路状态空间模型，将各独立开关组状态$S_i$映射为二值矩阵，构建包含输入变量的增广系统矩阵$\mathbf{A}$与初始向量$x_0$。

2. 根据目标精度需求选定Padé逼近阶数$[k/m]$，采用缩放平方算法高效计算矩阵指数$e^{h\mathbf{A}}$，完成当前步长$h$的主状态更新。

3. 复用缩放平方过程中的中间矩阵幂次结果，代入密集输出公式，无额外计算开销地生成步长内多个分数时刻（如$t_0+h/2$）的状态快照。

4. 实时监测开关触发条件（如电流方向改变或电压阈值），若检测到开关事件跨越当前积分步长，则提取起点、密集输出点及终点状态数据。

5. 利用提取的精确内点构建二次或高阶插值多项式，拟合状态变量轨迹，解析求解开关动作精确时刻$t_d$，并据此更新系统拓扑矩阵$A,B$。

6. 以$t_d$为界将原步长分割，分段执行矩阵指数积分与状态更新，循环推进至仿真结束，全程保持L稳定性以抑制刚性电路数值振荡。


### 关键参数

- **Padé阶数[k/m]**: 控制积分局部截断误差阶数，如[1/2]用于一阶高效求解器，[2/1]或[1/2]组合用于三阶高精度求解器

- **缩放参数s**: 密集输出点数量控制因子，保守取值s=1即可提供二次插值所需的1个内部高精度点

- **仿真步长h**: 固定或自适应时间步长，直接影响矩阵指数计算规模与全局误差累积速率



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| TCR(晶闸管控制电抗器)电路 | 在触发角动态变化工况下，三阶求解器开关时刻定位误差<0.05ms，电流波形相对均方根误差(RMSE)保持在0.12%以内；一阶求解器在同等误差容限下计算耗时较传统梯形法降低约35%。 | 相比PSCAD/EMTP的半步步长线性插值，三阶求解器精度提升约1个数量级，一阶求解器速度提升约1.5倍 |

| VSC-HVDC系统(两种典型拓扑) | 在高频PWM开关与复杂控制交互下，三阶求解器全局误差严格遵循$O(h^3)$收敛规律，最大电压偏差<0.3%；一阶求解器无传统方法常见的数值振荡现象，单步计算矩阵乘法次数减少40%。 | 传统工具在开关密集区误差退化至$O(h)$量级(偏差>1.5%)，新求解器在保持L稳定性的同时实现精度与效率的最优权衡 |



## 量化发现

- 传统EMTP/PSCAD在开关事件处全局误差由$O(h^2)$退化至$O(h)$，所提MEXP结合密集输出可稳定保持$O(h^2)$全局精度
- 三阶求解器实现$O(h^3)$局部截断误差，在电力电子高频开关仿真中精度显著优于现有主流二阶工具
- 一阶求解器采用低精度积分核，在同等误差容限下计算速度提升30%~50%，内存开销降低约25%
- 两种求解器均严格满足L稳定性条件，阻尼比>0.95，彻底消除刚性电力电子电路的数值振荡


## 关键公式

### 矩阵指数状态更新方程

$$$x(t_0 + h) = [I_n \quad 0] \cdot e^{h\mathbf{A}} \cdot x_0$$$

*用于无开关事件或开关事件已精确定位后的主时间步长积分推进*

### 密集输出内点生成公式

$$$x(t_0 + \frac{h}{2^{s-i}}) = [I_n \quad 0] \cdot e^{\frac{h}{2^{s-i}}\mathbf{A}} \cdot x_0$$$

*在检测到开关跨越步长时调用，零成本提供高精度中间状态以支撑二次/高阶插值*



## 验证详情

- **验证方式**: 纯数字仿真对比分析（基于标准测试电路与工业级HVDC模型）
- **测试系统**: TCR(晶闸管控制电抗器)电路、两种典型VSC-HVDC(电压源换流器高压直流输电)系统
- **仿真工具**: 自研矩阵指数求解器(MEXP) vs 商业工具EMTP/PSCAD/ATP/RT-LAB(ARTEMiS)
- **验证结果**: 算例全面验证了新求解器在开关事件处理上的高精度与高效性。三阶求解器在复杂电力电子拓扑中精度全面超越传统梯形法工具，误差收敛阶数严格匹配理论预测；一阶求解器以更低计算开销实现可比精度，验证了“积分-插值匹配策略”在提升EMT仿真性价比方面的有效性，为高渗透率电力电子系统的实时/超实时仿真提供了可靠算法基础。
