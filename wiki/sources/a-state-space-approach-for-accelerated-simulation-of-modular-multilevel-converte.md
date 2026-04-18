---
title: "A state-space approach for accelerated simulation of modular multilevel converters"
type: source
authors: ['Jinli Zhao']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112413. doi:10.1016/j.epsr.2025.112413"
tags: ['mmc', 'state-space']
created: "2026-04-13"
sources: ["EMT_Doc/04/Zhao 等 - 2026 - A state-space approach for accelerated simulation of modular multilevel converters.pdf"]
---

# A state-space approach for accelerated simulation of modular multilevel converters

**作者**: Jinli Zhao
**年份**: 2025
**来源**: `04/Zhao 等 - 2026 - A state-space approach for accelerated simulation of modular multilevel converters.pdf`

## 摘要

A state-space approach for accelerated simulation of modular a State Key Laboratory of Smart Power Distribution Equipment and System, Tianjin University, Tianjin 300072, China b Department of Electrical Engineering, Poly-technique Montr´eal, Montr´eal, Qu´ebec H3T 1J4, Canada Modular multilevel converter (MMC) based high-voltage direct current (HVDC) transmission technology has been widely applied in practical engineering. With the continuous increase in transmission voltage and capacity,

## 核心贡献


- 基于开关状态组合对子模块分组并引入虚拟状态变量，大幅降低状态矩阵维度
- 提出基于状态变量分组的高效电容电压均衡算法，完整保留子模块个体动态信息
- 构建状态空间框架下的MMC降阶模型，使计算耗时随电平数呈对数级增长


## 使用的方法


- [[状态空间法|状态空间法]]
- [[降阶建模|降阶建模]]
- [[数值积分|数值积分]]
- [[分段线性开关模型|分段线性开关模型]]
- [[电容电压均衡算法|电容电压均衡算法]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[hbsm|HBSM]]
- [[mmc-model|MMC]]
- [[电力网络|电力网络]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[仿真加速|仿真加速]]
- [[状态空间建模|状态空间建模]]
- [[大规模电力电子系统|大规模电力电子系统]]
- [[电容电压均衡|电容电压均衡]]


## 主要发现


- 仿真计算时间随MMC电平数增加呈对数增长，显著提升大规模系统仿真效率
- 降阶模型在保留各子模块电容电压动态的同时，与详细模型仿真精度高度一致
- 所提算法兼容高阶数值积分器，在加速仿真的同时未引入额外精度损失



## 方法细节

### 方法概述

提出一种基于状态空间框架的MMC电磁暂态仿真加速方法。核心思想是根据子模块的开关状态组合（投入组与旁路组）进行动态分组，并引入代表组内电容电压之和的虚拟状态变量，从而将系统状态矩阵维度大幅降低。通过推导降阶状态空间方程，实现与外部电力网络的高效耦合求解。针对闭锁工况，采用线性插值法精确捕捉二极管导通/关断的过零点时刻，消除时序误差。此外，利用状态空间框架下组内电容电压排序在单步长内保持不变的数学特性，设计了一种基于状态变量分组的高效电容电压均衡算法。该算法将传统的全局排序问题转化为两个有序队列的边界合并，避免重复计算，显著提升控制环节效率。该方法兼容高阶数值积分器，在实现计算耗时对数级增长的同时，完整保留各子模块个体动态信息。

### 数学公式


**公式1**: $$$\dot{x} = A_e x + B_{ev} v_M + B_{eu} u, \quad i_M = C_e x$$$

*外部电力网络的状态空间方程，描述网络状态变量x、MMC端口电压vM与端口电流iM的动态关系*


**公式2**: $$$\dot{P}_k = A_p P_k + \alpha_k B_p i_k, \quad \dot{Q}_k = A_q Q_k + (N-\alpha_k) B_q i_k, \quad v_k = C_p P_k + C_q Q_k + N D_p i_k$$$

*单桥臂分组后的虚拟状态变量方程，Pk和Qk分别为投入组与旁路组的电容电压和，αk为投入子模块数*


**公式3**: $$$\begin{bmatrix} \dot{P} \\ \dot{Q} \\ \dot{x} \end{bmatrix} = \begin{bmatrix} A_p I_M & 0 & B_p E_P C_e \\ 0 & A_q I_M & B_q E_Q C_e \\ C_p B_{ev} & C_q B_{ev} & A_e + N D_p B_{ev} C_e \end{bmatrix} \begin{bmatrix} P \\ Q \\ x \end{bmatrix} + \begin{bmatrix} 0 \\ 0 \\ B_{eu} \end{bmatrix} u$$$

*系统整体降阶状态空间矩阵方程，将MMC虚拟状态变量与外部网络状态变量耦合，用于数值积分求解*


**公式4**: $$$t_{ZC} = t + \rho \Delta t, \quad \rho = \frac{|w_i(t)|}{|w_i(t)| + |w_i(t+\Delta t)|}$$$

*闭锁工况下开关动作时刻的线性插值公式，用于精确计算状态切换的过零点时间*


**公式5**: $$$p_{sa}(t) = e^{A_p(t-t_0)} p_{sa}(t_0) + \frac{1}{\alpha_k} \left( P_k(t) - e^{A_p(t-t_0)} P_k(t_0) \right)$$$

*积分步长结束后，利用虚拟状态变量反推组内单个子模块电容电压的解析公式*


### 算法步骤

1. 在上一仿真时刻 $t_{n-1}$，根据桥臂电流 $i_k(t_{n-1})$ 的极性确定电压分组属性：若电流为正，则投入组 $P$ 对应低电压组 $G_1$，旁路组 $Q$ 对应高电压组 $G_2$。

2. 初始化双指针：指针 $m$ 与 $T_m$ 指向 $G_1$ 队列中电容电压最高的子模块，指针 $n$ 与 $T_n$ 指向 $G_2$ 队列中电容电压最低的子模块。

3. 执行边界比较：对比 $v_C(m)$ 与 $v_C(n)$ 的大小。若 $v_C(m) > v_C(n)$，说明存在逆序，交换两子模块在队列中的位置，并更新指针继续向队列内部推进；若 $v_C(m) \le v_C(n)$，则停止当前比较。

4. 重复步骤3直至所有跨组边界需要调整位置的子模块完成重排，生成当前时刻的完整有序队列。

5. 在当前时刻 $t_n$，根据最新控制指令确定的投入数量 $\alpha_k$，从有序队列中直接截取前 $\alpha_k$ 个子模块作为新的投入组，其余自动归为旁路组。

6. 利用状态空间框架下组内电压排序在单步长内保持不变的数学性质，算法仅对跨组边界附近的子模块进行局部比较与重排，彻底避免全局排序带来的指数级计算开销。


### 关键参数

- **仿真步长**: 20 μs

- **子模块电容**: 0.013 F (双端系统) / 0.01 F (四端系统)

- **桥臂电感**: 0.04 H (双端) / 0.019~0.116 H (四端)

- **测试电平数**: 21, 41, 61, 81, 101

- **硬件环境**: Intel Core i5-9300H CPU, 16 GB RAM

- **软件环境**: MATLAB R2024a, EMTP



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 传输功率阶跃 | 1s时整流侧有功功率参考值从500MW阶跃至1000MW。模型输出的有功功率、交流电压与电流波形与EMTP基准高度重合，相对误差严格控制在1%以内。 | 与EMTP戴维南等效模型误差<1%，动态响应完全一致 |

| 交流侧三相接地短路 | 2s时发生三相短路故障，0.1s后清除。准确复现故障点电压跌落至零、恢复过程及交流电流的暂态冲击波形，无数值振荡。 | 暂态波形与EMTP模型高度一致，满足高精度EMT仿真要求 |

| 直流侧双极永久短路 | 3s时发生直流短路，2ms后系统闭锁。精确捕捉闭锁瞬间的开关状态切换，并准确模拟闭锁后的不可控整流过程，线性插值法有效消除时序误差。 | 闭锁瞬态过程与EMTP模型吻合，插值法确保状态切换无精度损失 |

| 四端MMC-HVDC系统功率调节 | 2s时Cm-F1站有功功率从500MW降至200MW。101电平下系统仿真耗时256s，排序耗时10.1s，验证了算法在多端大规模网络中的扩展性。 | 运行时间约为双端系统的1.8倍，证明算法具备良好的网络规模扩展能力 |



## 量化发现

- 仿真计算时间随MMC电平数增加呈对数级增长，而详细模型呈指数级增长
- 在101电平下，加速模型相比详细模型速度提升88.4倍（详细模型12572.5s vs 加速模型142.3s）
- 系统状态矩阵维度降低 $M(N-2)$，其中M为桥臂总数，N为每桥臂子模块数
- 电容电压均衡算法的排序耗时随电平数呈线性增长，101电平下仅需5.3s
- 与EMTP基准模型对比，稳态与暂态仿真误差均严格控制在1%以内
- 四端系统（4个100电平MMC）仿真耗时256s，排序耗时10.1s，验证了多端大规模系统的扩展性


## 关键公式

### 系统整体降阶状态空间方程

$$$\begin{bmatrix} \dot{P} \\ \dot{Q} \\ \dot{x} \end{bmatrix} = \begin{bmatrix} A_p I_M & 0 & B_p E_P C_e \\ 0 & A_q I_M & B_q E_Q C_e \\ C_p B_{ev} & C_q B_{ev} & A_e + N D_p B_{ev} C_e \end{bmatrix} \begin{bmatrix} P \\ Q \\ x \end{bmatrix} + \begin{bmatrix} 0 \\ 0 \\ B_{eu} \end{bmatrix} u$$$

*用于系统级数值积分求解，将MMC虚拟状态变量与外部网络状态变量耦合，实现矩阵维度大幅压缩*

### 子模块电容电压反推公式

$$$p_{sa}(t) = e^{A_p(t-t_0)} p_{sa}(t_0) + \frac{1}{\alpha_k} \left( P_k(t) - e^{A_p(t-t_0)} P_k(t_0) \right)$$$

*在数值积分步长结束后，利用求解得到的虚拟状态变量 $P_k(t)$ 精确恢复组内每个子模块的个体电容电压*

### 开关动作时刻线性插值公式

$$$t_{ZC} = t + \rho \Delta t, \quad \rho = \frac{|w_i(t)|}{|w_i(t)| + |w_i(t+\Delta t)|}$$$

*用于闭锁工况下精确捕捉二极管导通/关断的过零点时刻，消除固定步长带来的时序误差*



## 验证详情

- **验证方式**: 纯数字仿真对比验证（自定义MATLAB状态空间模型 vs EMTP戴维南等效模型 vs 详细状态空间模型）
- **测试系统**: 双端MMC-HVDC系统（额定功率1000MW，直流电压640kV，21~101电平）与基于CIGRE B4-57标准的四端MMC-HVDC系统（直流电压400kV，100电平）
- **仿真工具**: MATLAB R2024a, EMTP
- **验证结果**: 在功率阶跃、交流短路、直流短路闭锁等多种暂态工况下，加速模型与EMTP基准结果高度吻合，误差<1%。计算耗时随电平数呈对数增长，最高实现88.4倍加速，且完整保留子模块级动态信息，验证了其在大规模电力电子系统EMT仿真中的高精度与高效率。
