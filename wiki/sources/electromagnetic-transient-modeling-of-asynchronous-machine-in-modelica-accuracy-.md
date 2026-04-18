---
title: "Electromagnetic Transient Modeling of Asynchronous Machine in Modelica, Accuracy, and Performance Assessment"
type: source
authors: ['未知']
year: 2024
journal: "IEEE Access;2024;12; ;10.1109/ACCESS.2024.3462255"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/16/Choi 等 - 2025 - Electromagnetic Transient Simulation of Large-Scale Inverter-Based Resources With High-Granularity.pdf"]
---

# Electromagnetic Transient Modeling of Asynchronous Machine in Modelica, Accuracy, and Performance Assessment

**作者**: 
**年份**: 2024
**来源**: `16/Choi 等 - 2025 - Electromagnetic Transient Simulation of Large-Scale Inverter-Based Resources With High-Granularity.pdf`

## 摘要

Classical EMT-type simulators are mostly programmed in procedural languages, e.g. Fortran or C. In these languages, the focus is mainly on the solution methods. Modern languages, such as Modelica, are declarative and primarily focused on modeling and simulation. Modelica offers a much higher abstraction level, which makes the codes more concise and understandable. This paper contributes to the electromagnetic transient modeling and simulation of asynchronous machines in Modelica. In this paper, the modeling of a three-phase squirrel cage (single and double cage) and wound-rotor induction machine in three different reference frames is described and implemented. The accuracy and performance of Modelica models are compared and validated with the classical modeling approach used in the referen

## 核心贡献


- 基于Modelica实现异步电机多参考系电磁暂态建模，摆脱固定步长求解限制
- 提出基于磁链状态变量的四阶非线性微分代数方程建模，提升计算效率
- 验证变步长求解器在电机顺序启动仿真中的优势，实现无附加阻尼直接收敛


## 使用的方法


- [[modelica方程建模|Modelica方程建模]]
- [[变步长求解器|变步长求解器]]
- [[park坐标变换|Park坐标变换]]
- [[磁链状态空间法|磁链状态空间法]]
- [[微分代数方程求解|微分代数方程求解]]


## 涉及的模型


- [[异步电机|异步电机]]
- [[单鼠笼感应电机|单鼠笼感应电机]]
- [[双鼠笼感应电机|双鼠笼感应电机]]
- [[绕线式感应电机|绕线式感应电机]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[声明式建模|声明式建模]]
- [[电机顺序启动|电机顺序启动]]
- [[故障与孤岛仿真|故障与孤岛仿真]]
- [[数值收敛性分析|数值收敛性分析]]


## 主要发现


- 变步长求解器结合Modelica模型在电机顺序启动暂态过程中实现快速高精度仿真
- 模型在不同容差下直接收敛，无需并联人工阻尼电阻即可有效消除数值振荡
- 与EMTP经典方法对比验证了声明式建模在暂态精度与计算效率上的等效性



## 方法细节

### 方法概述

本文提出一种基于Modelica声明式语言的异步电机（ASM）电磁暂态（EMT）建模方法。该方法摒弃传统过程式语言（如Fortran/C）中依赖固定步长和伴随电路诺顿等效的求解逻辑，转而直接以磁链为状态变量构建四阶非线性微分代数方程（DAE）组。模型支持定子、转子及同步三种参考系灵活切换，通过Modelica编译器的符号化扁平化、指标约简与方程撕裂技术自动确定计算顺序，无需预设因果性。结合变步长求解器（如DASSL），算法可根据网络暂态变化率动态调整积分步长，在长周期仿真中显著提升效率，且无需添加人工阻尼电阻即可保证数值稳定性。

### 数学公式


**公式1**: $$$v_{qds} = P(\theta) v_{abcs}$$$

*定子abc坐标系到qd参考系的Park变换电压方程*


**公式2**: $$$p\phi = \omega_{base} (A\phi + v)$$$

*以磁链为状态变量的四阶非线性电气状态空间方程，p为微分算子*


**公式3**: $$$A = -RL^{-1} + W$$$

*状态矩阵A，包含电阻、电感逆矩阵及旋转速度耦合矩阵W*


**公式4**: $$$i = L^{-1}\phi$$$

*磁链与电流的代数关系，用于从状态变量求解支路电流*


**公式5**: $$$T_e = \phi_{ds} i_{qs} - \phi_{qs} i_{ds}$$$

*电磁转矩计算公式，基于qd轴磁链与电流的叉积*


**公式6**: $$$p\omega_r = \frac{1}{2H}(T_e - T_m)$$$

*转子机械运动方程，描述转速随电磁转矩与机械负载转矩差值的动态变化*


### 算法步骤

1. 1. 参考系选择与坐标变换初始化：根据仿真需求选定参考系（定子、转子或同步），计算参考系角度θ及转子相对角度β，生成Park变换矩阵P及其逆矩阵。

2. 2. 电气状态方程构建：以定转子磁链φ为状态变量，结合电阻矩阵R、电感矩阵L及旋转耦合矩阵W，构建微分方程 $p\phi = \omega_{base}(-RL^{-1} + W)\phi + \omega_{base}v$。

3. 3. 电流与转矩计算：通过代数方程 $i = L^{-1}\phi$ 求解qd轴电流，利用Park逆变换还原至abc三相电流；同步计算电磁转矩 $T_e$。

4. 4. 机械动态更新：将 $T_e$ 与外部机械转矩 $T_m$ 代入转子运动方程，积分求解转子角速度 $\omega_r$ 和位置角 $\theta_r$，并反馈更新矩阵W中的速度项。

5. 5. 模型编译与符号处理：Modelica编译器对层级模型进行扁平化，执行指标约简（Index Reduction）和方程撕裂（Tearing），将系数矩阵转化为块下三角形式，自动确定变量求解依赖顺序。

6. 6. 变步长数值积分：调用DASSL等变步长求解器，根据用户设定的容差（如1e-6）和局部截断误差估计，动态调整时间步长。在暂态剧烈时自动缩小步长，稳态时放大步长，直接求解DAE系统直至仿真结束。


### 关键参数

- **求解器容差**: 1e-6（高精度）, 1e-3（高效率）

- **EMTP对比步长**: 10 µs, 20 µs, 200 µs, 1 µs

- **基准角频率**: $\omega_{base}$ (rad/s)

- **惯量常数H**: 1 s (Case 1)

- **电机额定参数**: 900 hp/2.4 kV/4极 (Case 1); 1100 hp/6.6 kV/4极 (Case 2)

- **参考系类型**: 定子参考系($\omega=0$)、转子参考系($\omega=\omega_r$)、同步参考系($\omega=1$)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Case 1: 900 hp单鼠笼电机启动与三相短路 | 电机从堵转启动至1.5 s达到稳态转速0.98 pu，稳态转差率1.09%。t=4.01 s发生三相短路，定转子电流出现约60 Hz衰减暂态。Modelica (DASSL, tol=1e-6) 与 EMTP (TBE, 10 µs) 波形完全重合。 | 相对误差范数：tol=1e-6时为0.64%，tol=1e-3时为0.77%。容差减半对精度影响极小，但显著降低CPU时间。 |

| Case 2: 含6台双鼠笼电机与2台同步机的复杂网络故障与孤岛 | t=9 s发生两相接地故障，t=9.15 s清除故障并孤岛运行。Modelica成功捕捉到故障清除后的高频暂态振荡，而EMTP在200 µs步长下完全丢失该高频分量。孤岛后ASM1启动电流升至7 pu，转速在14 s稳定。 | EMTP需将步长降至1 µs才能匹配Modelica精度，但仿真时间激增至1119 s；Modelica (tol=1e-6) 仅需约112.6 s，速度提升近10倍。 |

| Case 3: 电机顺序启动长周期仿真 (ASM2至ASM6) | 电机在15 s至50 s间依次启动，仿真总时长60 s。Modelica平均步长自动扩展至168.9 µs，电压波形与EMTP (20 µs固定步长) 完全一致。 | Modelica耗时112.6 s，EMTP耗时198.4 s。Modelica仿真速度提升约43%（快1.76倍），且启动间隔越长，变步长优势越明显。 |



## 量化发现

- Modelica与EMTP基准解的相对误差范数控制在0.64%~0.77%之间，满足高精度EMT仿真要求。
- 在长周期顺序启动场景中，变步长求解器平均步长可达168.9 µs，仿真耗时112.6 s，比固定步长20 µs的EMTP（198.4 s）快1.76倍。
- 为捕捉同等高频暂态精度，EMTP需采用1 µs极小步长导致耗时1119 s，而Modelica仅需约112.6 s，计算效率提升近10倍。
- 求解器容差从1e-6放宽至1e-3时，平均步长从15.05 µs增至25.45 µs，波形精度损失极小（误差范数仅增加0.13%），但CPU时间显著下降。
- 全程无需添加传统EMTP中用于抑制数值振荡的人工并联阻尼电阻，模型直接收敛且保持数值稳定。


## 关键公式

### 磁链状态空间微分方程

$$$p\phi = \omega_{base} (-RL^{-1} + W)\phi + \omega_{base}v$$$

*用于描述异步电机在任意qd参考系下的电磁暂态动态，是Modelica模型的核心状态方程，直接输入变步长DAE求解器。*

### 电磁转矩方程

$$$T_e = \phi_{ds} i_{qs} - \phi_{qs} i_{ds}$$$

*在电机启动、负载突变或故障暂态过程中，用于耦合电气网络与机械转子动力学，计算实时电磁转矩。*

### 转子机械运动方程

$$$p\omega_r = \frac{1}{2H}(T_e - T_m)$$$

*描述转子角速度随转矩不平衡量的积分过程，适用于单机或多质量块系统的机电暂态耦合仿真。*



## 验证详情

- **验证方式**: 对比仿真验证（与工业级标准EMTP软件进行波形、精度与性能对比）
- **测试系统**: 1) 900 hp单鼠笼电机单机系统；2) 含6台双鼠笼感应电机、2台同步发电机及非线性变压器的120 kV复杂配电网；3) 工业厂用电系统电机顺序启动长周期网络。
- **仿真工具**: OpenModelica (DASSL变步长求解器, ODE模式) vs EMTP (TBE梯形-后向欧拉固定步长求解器)
- **验证结果**: 在电机启动、稳态运行、三相短路、两相接地故障及孤岛运行等多种工况下，Modelica模型输出波形与EMTP高度一致。变步长策略在暂态剧烈时自动加密步长，稳态时大幅放宽步长，在保证误差<0.8%的前提下，长周期仿真效率提升43%~900%，且彻底消除了对人工阻尼电阻的依赖，验证了声明式建模结合变步长求解器在EMT仿真中的优越性。
