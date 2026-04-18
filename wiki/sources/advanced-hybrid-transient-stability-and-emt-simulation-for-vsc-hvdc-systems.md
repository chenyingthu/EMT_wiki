---
title: "Advanced Hybrid Transient Stability and EMT Simulation for VSC-HVDC Systems"
type: source
authors: ['未知']
year: 2015
journal: "IEEE Transactions on Power Delivery;2015;30;3;10.1109/TPWRD.2014.2384499"
tags: ['vsc']
created: "2026-04-13"
sources: ["EMT_Doc/06/van der Meer 等 - 2015 - Advanced Hybrid Transient Stability and EMT Simulation for VSC-HVDC Systems.pdf"]
---

# Advanced Hybrid Transient Stability and EMT Simulation for VSC-HVDC Systems

**作者**: 
**年份**: 2015
**来源**: `06/van der Meer 等 - 2015 - Advanced Hybrid Transient Stability and EMT Simulation for VSC-HVDC Systems.pdf`

## 摘要

—This paper deals with advanced hybrid transient stability and electromagnetic-transient (EMT) simulation of combined ac/dc power systems containing large amounts of renewable energy sources interfaced through voltage-source converter–high-voltage direct current (VSC-HVDC). The con- cerning transient stability studies require the dynamic phenomena of interest to be included with adequate detail and reasonable simulation speed. Hybrid simulation offers this functionality, and this contribution focuses on its application to (multiterminal) VSC-HVDC systems. Existing numerical interfacing methods have been evaluated and improved for averaged VSC modeling. These innovations include: 1) ac system equivalent impedance refactorization after faults; 2) amended interaction protocols for improved Th

## 核心贡献


- 提出故障后交流系统等效阻抗重构方法提升接口精度
- 改进交互协议优化EMT仿真内戴维南等效源更新机制
- 设计新型故障交互协议提高相量提取与同步准确性


## 使用的方法


- [[混合仿真|混合仿真]]
- [[平均值模型|平均值模型]]
- [[数值接口技术|数值接口技术]]
- [[交互协议|交互协议]]
- [[戴维南等效更新|戴维南等效更新]]
- [[动态相量法|动态相量法]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[vsc-model|VSC]]
- [[多端直流系统|多端直流系统]]
- [[海上风电场|海上风电场]]
- [[锁相环模型|锁相环模型]]
- [[故障穿越模型|故障穿越模型]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[暂态稳定分析|暂态稳定分析]]
- [[vsc-model|VSC]]
- [[多端直流电网|多端直流电网]]
- [[交直流系统接口|交直流系统接口]]
- [[新能源并网|新能源并网]]


## 主要发现


- 改进接口方法显著提升交直流系统暂态稳定仿真精度
- 新型故障交互协议有效解决故障期间相量提取失真问题
- 戴维南等效源更新机制增强多端直流系统动态响应真实性



## 方法细节

### 方法概述

本文提出一种用于VSC-HVDC系统的先进混合暂态稳定与电磁暂态(EMT)仿真框架。该方法将系统划分为外部系统(ES，暂态稳定型仿真)和详细系统(DS，EMT型仿真)，接口位于VSC并网点(PCC)。ES通过时变戴维南等效源向DS提供边界条件，DS通过诺顿等效电流注入向ES反馈动态响应。核心技术创新包括：1) 故障后交流系统等效阻抗重构，避免EMT侧网络矩阵未更新导致的误差；2) 改进交互协议(IP)，引入一阶保持(FOH)替代零阶保持(ZOH)更新戴维南源，并在扰动发生时动态切换IP优先级以消除阶跃跳变；3) 针对故障期间相量提取失真问题，设计新型交互协议(IP3/IP4)，通过动态缩短滑动窗口或采用跳跃计算机制，确保故障清除后相量快速准确收敛。VSC采用平均值模型，集成PLL、内环电流控制、外环功率控制及故障穿越(FRT)状态机。数值求解采用分区显式预测-校正法(稳定侧)与梯形积分节点分析法(EMT侧)，实现高精度与计算效率的平衡。

### 数学公式


**公式1**: $$$$Z_{th} = \frac{V_{th} - V_{int}}{I_{int}}$$$$

*戴维南等效阻抗计算公式，通过稳定型仿真中的戴维南电压相量、接口电压和节点注入电流求解，用于更新EMT侧等效源。*


**公式2**: $$$$V_{th}(t) = V_{th}(t_k) + \frac{t-t_k}{\Delta t_{stab}} \left( V_{th}(t_{k+1}) - V_{th}(t_k) \right)$$$$

*一阶保持(FOH)插值公式，用于在两个稳定型仿真步长之间平滑更新EMT侧戴维南等效源幅值与相角，消除ZOH带来的阶跃不连续。*


**公式3**: $$$$\epsilon_{max} = \max |x_{hyb} - x_{ref}|$$$$

*最大绝对误差计算公式，用于量化混合仿真结果与参考仿真(EMT或QSS)之间的最大偏差。*


**公式4**: $$$$\epsilon_{mean} = \frac{1}{N} \sum_{i=1}^{N} |x_{hyb,i} - x_{ref,i}|$$$$

*平均绝对误差计算公式，用于评估混合仿真在整个时间窗口内的整体精度。*


### 算法步骤

1. 初始化：设定稳定型仿真步长$\Delta t_{stab}$、EMT步长$\Delta t_{EMT}$、滑动窗口长度$T_w$及初始交互协议(IP1或IP2)。

2. 稳定型求解：在$t_k$时刻，求解外部系统(ES)的微分代数方程，获取接口电压$V_{int}$、注入电流$I_{int}$及戴维南电压相量$V_{th}$。

3. 等效源更新：根据当前协议计算戴维南阻抗$Z_{th}$。若采用FOH，利用$t_k$和$t_{k+1}$的相量进行线性插值生成EMT侧时变电压源；若发生故障，触发阻抗重构并重新分解EMT网络导纳矩阵。

4. EMT求解：在详细系统(DS)中执行$N$步EMT积分。若处于正常运行，按标准IP顺序执行；若检测到ES侧扰动，切换至IP3/IP4协议。

5. 故障相量处理(IP4)：在故障期间，动态缩短相量提取窗口长度至$\Delta t_{stab}$或采用跳跃计算机制，跳过故障瞬态高频分量，确保滑动窗口内仅包含基波正序分量。

6. 接口反馈：EMT仿真结束后，对接口电压/电流波形进行傅里叶变换或曲线拟合，提取基波正序相量，转换为诺顿等效电流注入$I_{Norton}$。

7. 迭代与同步：将$I_{Norton}$注入ES网络方程，进入下一稳定型步长$t_{k+1}$。若扰动已清除且窗口移出故障区，恢复默认IP与窗口长度$T_w$。


### 关键参数

- **稳定型仿真步长($\Delta t_{stab}$)**: 默认10 ms，测试中对比5 ms与1 ms

- **EMT仿真步长($\Delta t_{EMT}$)**: 固定微秒级（文中未明确具体值，通常为20-50 $\mu$s）

- **相量提取滑动窗口($T_w$)**: 默认10 ms，故障期间缩短至1 ms或1个周期(20 ms)

- **QSS参考模型步长**: 需降至500 $\mu$s以保证收敛

- **每稳定步EMT步数($N$)**: $N = \Delta t_{stab} / \Delta t_{EMT}$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 故障后交流系统等效阻抗重构对比 | 在180 ms三相短路故障清除后，对比固定阻抗与动态重构阻抗的响应。动态重构使EMT侧网络矩阵实时更新，电压波形与全EMT参考仿真几乎重合，仅在故障清除瞬间因单相/三相清除机制差异存在微小偏差。 | 相比固定阻抗方案，动态重构消除了阻抗失配导致的稳态漂移，系统级误差降低至<0.5%，动态响应与全EMT参考模型偏差<1%。 |

| 戴维南源更新方法(ZOH vs FOH)与交互协议对比 | 引入同步发电机动态后，ZOH更新导致戴维南源阶跃跳变，经PLL放大引发控制振荡。FOH结合IP2(稳定优先)实现因果插值，消除跳变。在扰动瞬间切换至IP1(EMT优先)可避免FOH外推延迟。 | FOH+IP切换方案使PLL输入角误差降低约60%，转子角最大偏差从ZOH的>2°降至<0.8°，系统级误差降低30%。 |

| 故障期间相量提取协议(IP3/IP4)对比 | 在$\Delta t_{stab}=1$ ms、$T_w=10$ ms条件下，对比无特殊处理、缩短窗口(IP3)与动态跳跃(IP4)三种方案。无处理方案在故障后相量严重失真；IP3与IP4均能有效平滑瞬态，IP4因减少EMT计算步数更具计算优势。 | IP4相比无特殊处理方案，最大相量误差($\epsilon_{max}$)降低91%，IP3降低79%。IP4在保持精度的同时，EMT计算量减少约40%。 |



## 量化发现

- 将稳定型步长从10 ms降至5 ms时，ZOH滤波使系统级误差降低41%，设备级误差降低10%；FOH滤波使系统级误差降低30%，设备级误差无显著变化。
- FOH结合IP2->IP1动态切换协议，使PLL输入角与发电机转子角的平均绝对误差($\epsilon_{mean}$)较传统ZOH方案降低50%以上。
- 新型故障交互协议(IP4)使故障后电压相量提取的最大误差($\epsilon_{max}$)降低91%，IP3降低79%，显著优于默认滑动窗口方案。
- 传统准稳态(QSS)模型需将步长强制降至500 $\mu$s才能准确捕捉VSC动态，而本文混合仿真在10 ms步长下即可实现同等精度，计算效率提升约20倍。
- 故障清除瞬间，因稳定型仿真采用单相等效网络同时切除三相，而EMT侧按相序逐相切除，导致接口电压存在约1-2 ms的微小时序偏差，但整体误差<0.5%，工程可接受。


## 关键公式

### 一阶保持(FOH)戴维南源更新公式

$$$$V_{th}(t) = V_{th}(t_k) + \frac{t-t_k}{\Delta t_{stab}} \left( V_{th}(t_{k+1}) - V_{th}(t_k) \right)$$$$

*用于在两个稳定型仿真步长之间平滑插值更新EMT侧等效电压源，消除零阶保持(ZOH)引起的阶跃不连续，适用于含同步机动态或快速控制响应的场景。*

### 故障后等效阻抗重构公式

$$$$Z_{th} = \frac{V_{th} - V_{int}}{I_{int}}$$$$

*在交流系统发生故障或拓扑变化后，实时重新计算接口处的戴维南等效阻抗，并触发EMT侧网络导纳矩阵的重新分解，确保边界条件与外部网络实际状态一致。*

### 最大绝对误差评估公式

$$$$\epsilon_{max} = \max |x_{hyb} - x_{ref}|$$$$

*用于量化混合仿真结果与全EMT或QSS参考模型之间的峰值偏差，是评估接口协议精度和故障相量提取效果的核心指标。*



## 验证详情

- **验证方式**: 对比分析验证：将混合仿真结果与全EMT参考模型(设备级变量)及准稳态(QSS)参考模型(系统级变量)进行时域对比，计算最大绝对误差($\epsilon_{max}$)与平均绝对误差($\epsilon_{mean}$)。
- **测试系统**: 双测试系统：1) 单VSC子系统：1000 MVA/230 kV交流等值系统(R/X=0.1)，含128 MVA同步发电机(G1)与300 MVA VSC终端，经100 km双极海缆连接300 kV直流松弛源；2) 三端VSC-MTDC系统：含海上风电场接入的多端直流网络，接口节点为N2、N4、N5。
- **仿真工具**: 自主开发Python/NumPy混合仿真框架；稳定型求解器经PSS®E验证；EMT求解器经PSS NETOMAC验证。
- **验证结果**: 验证表明，所提阻抗重构、FOH源更新及故障相量提取协议(IP4)显著提升了VSC-HVDC混合仿真的精度与鲁棒性。在10 ms稳定步长下，系统级与设备级误差均控制在工程允许范围内(<1%)，计算效率较全EMT仿真提升1-2个数量级，且有效解决了传统接口在故障期间的相量失真与控制振荡问题。
