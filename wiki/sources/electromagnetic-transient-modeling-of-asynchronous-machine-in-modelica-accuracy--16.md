---
title: "Electromagnetic Transient Modeling of Asynchronous Machine in Modelica, Accuracy, and Performance Assessment"
type: source
authors: ['未知']
year: 2024
journal: "IEEE Access;2024;12; ;10.1109/ACCESS.2024.3462255"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/16/Masoom和Mahseredjian - 2024 - Electromagnetic Transient Modeling of Asynchronous Machine in Modelica, Accuracy, and Performance As.pdf"]
---

# Electromagnetic Transient Modeling of Asynchronous Machine in Modelica, Accuracy, and Performance Assessment

**作者**: 
**年份**: 2024
**来源**: `16/Masoom和Mahseredjian - 2024 - Electromagnetic Transient Modeling of Asynchronous Machine in Modelica, Accuracy, and Performance As.pdf`

## 摘要

Classical EMT-type simulators are mostly programmed in procedural languages, e.g. Fortran or C. In these languages, the focus is mainly on the solution methods. Modern languages, such as Modelica, are declarative and primarily focused on modeling and simulation. Modelica offers a much higher abstraction level, which makes the codes more concise and understandable. This paper contributes to the electromagnetic transient modeling and simulation of asynchronous machines in Modelica. In this paper, the modeling of a three-phase squirrel cage (single and double cage) and wound-rotor induction machine in three different reference frames is described and implemented. The accuracy and performance of Modelica models are compared and validated with the classical modeling approach used in the referen

## 核心贡献


- 基于声明式语言构建异步电机EMT详细模型，支持单双鼠笼及绕线转子结构
- 采用磁链作状态变量建立多参考系四阶模型，显著提升微分方程求解效率
- 验证变步长求解器在电机顺序启动中的优势，无需人工阻尼即可保证收敛


## 使用的方法


- [[声明式建模|声明式建模]]
- [[变步长求解器|变步长求解器]]
- [[坐标变换|坐标变换]]
- [[磁链状态空间法|磁链状态空间法]]
- [[梯形积分法|梯形积分法]]
- [[修正增广节点分析法|修正增广节点分析法]]


## 涉及的模型


- [[异步电机|异步电机]]
- [[单鼠笼感应电机|单鼠笼感应电机]]
- [[双鼠笼感应电机|双鼠笼感应电机]]
- [[绕线转子感应电机|绕线转子感应电机]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[基于方程建模|基于方程建模]]
- [[电机顺序启动|电机顺序启动]]
- [[故障与孤岛仿真|故障与孤岛仿真]]
- [[变步长求解器应用|变步长求解器应用]]


## 主要发现


- 变步长求解器在顺序启动仿真中兼具高精度与快速度，性能优于传统定步长
- 模型在不同容差下直接收敛，无需并联阻尼电阻即可有效抑制数值振荡
- 故障与孤岛工况结果与EMTP经典模型高度一致，验证了声明式建模准确性



## 方法细节

### 方法概述

本文提出一种基于声明式语言Modelica的异步电机（ASM）电磁暂态（EMT）详细建模方法。区别于传统EMTP等基于过程式语言（Fortran/C）和固定步长求解器的建模方式，该方法采用基于方程的建模（Equation-Based Modeling），以磁链为状态变量构建四阶非线性状态空间模型。模型支持定子、转子及同步三种参考系，涵盖单鼠笼、双鼠笼及绕线转子结构。在编译阶段，Modelica编译器自动执行方程扁平化、索引降阶和符号重排，将微分代数方程（DAE）转换为块下三角形式，彻底消除人工指定因果性的限制。结合变步长求解器（如DASSL），求解器根据网络暂态变化率与局部截断误差自动调整积分步长，在保证数值稳定性的同时，完全避免了传统方法中为抑制数值振荡而必须添加的人工并联阻尼电阻，显著提升了长周期暂态仿真的计算效率与模型可读性。

### 数学公式


**公式1**: $$$v_{qds} = P(\theta) v_{abcs}$$$

*Park坐标变换方程，将三相静止坐标系下的定子电压转换至任意旋转参考系（dq轴），实现交流量的解耦。*


**公式2**: $$$p\phi = \omega_{base} (A\phi + v)$$$

*磁链状态空间微分方程，以磁链为状态变量描述电机电气动态，其中$A = -RL^{-1} + W$，相比电流状态变量可减少求导次数，提升积分效率。*


**公式3**: $$$i = L^{-1} \phi$$$

*磁链-电流代数关系，通过电感矩阵求逆由状态变量磁链实时计算定转子电流。*


**公式4**: $$$T_e = \phi_{ds} i_{qs} - \phi_{qs} i_{ds}$$$

*电磁转矩计算公式，基于dq轴磁链与电流的叉积得出，用于机电能量转换分析。*


**公式5**: $$$p\omega_r = \frac{1}{2H}(T_e - T_m)$$$

*转子机械运动方程，描述转子角速度在电磁转矩与机械负载转矩作用下的动态响应，$H$为惯性常数。*


### 算法步骤

1. 定义电机物理参数（定转子电阻、漏感、互感、惯性常数等）及状态变量向量（磁链$\phi$），并初始化参考系角度$\theta$。

2. 根据仿真需求选择参考系（定子$\omega=0$、转子$\omega=\omega_r$或同步$\omega=1$），动态计算Park变换矩阵$P(\theta)$及旋转电压源矩阵$W$。

3. 构建电气微分代数方程组，将电压方程离散化为以磁链为状态变量的四阶非线性状态空间形式$p\phi = \omega_{base}(A\phi + v)$，并处理双鼠笼结构的6维扩展矩阵。

4. 耦合机械方程，通过电磁转矩与负载转矩差值更新转子角速度与位置，支持非线性机械负载特性（如$T_m \propto \omega^2$）的接入。

5. 利用Modelica物理连接器（Connector）定义端口变量（电压为跨接变量，电流为流变量），实现电机与外部电网拓扑的自动连接与基尔霍夫定律约束。

6. 调用Modelica编译器进行符号处理（扁平化、索引约减、方程撕裂），生成块下三角形式的DAE系统，自动确定方程求解顺序。

7. 配置变步长求解器（DASSL）及容差（如1e-6），启动时域仿真，求解器根据局部截断误差自动调整积分步长，输出暂态波形并保证数值收敛。


### 关键参数

- **容差设置**: 1e-6, 1e-3

- **EMTP对比步长**: 10 µs, 20 µs, 200 µs, 1 µs

- **测试电机额定参数**: 900 hp, 2.4 kV, 4极, $R_s=0.08\Omega$, $R_r=0.09\Omega$, $X_{ls}=0.32\Omega$, $X_{lr}=0.45\Omega$, $X_m=16\Omega$, 满载滑差0.15%, $H=1$ s

- **求解器配置**: OpenModelica (DASSL变步长), EMTP (TBE固定步长)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 900 hp单鼠笼电机启动与机端三相短路 | 电机启动电流达10 pu，1.5 s后衰减至稳态（滑差1.09%）。4.01 s发生三相短路，定转子暂态电流迅速衰减。Modelica与EMTP波形完全重合。 | 相对误差范数：容差1e-6时为0.64%，容差1e-3时为0.77%，精度高度一致。 |

| 含6台双鼠笼电机与2台同步机的复杂网络故障与孤岛 | 9 s发生两相接地故障，9.15 s清除故障并孤岛运行。Modelica成功捕捉故障清除后的高频振荡，而EMTP在200 µs步长下完全遗漏该暂态。 | EMTP降至1 µs步长可匹配波形，但耗时激增至1119 s；Modelica（容差1e-3）仅需约112.6 s，计算效率提升近10倍。 |

| 工业厂用电多电机顺序启动（15 s至50 s间隔启动） | ASM2至ASM6依次启动，间隔5 s至50 s。Modelica在稳态期间自动放大步长，暂态期间自动加密。 | Modelica总耗时112.6 s（平均步长168.9 µs），EMTP（20 µs固定步长）耗时198.4 s，Modelica在长周期顺序启动场景中快约1.76倍。 |



## 量化发现

- 变步长求解器在长周期顺序启动仿真中比固定步长EMTP快约1.76倍（112.6 s vs 198.4 s）。
- 模型相对误差严格控制在0.77%以内（容差1e-3时），与工业级EMTP基准结果高度吻合。
- 变步长求解器在稳态期间平均步长可达168.9 µs，大幅减少计算节点，且无需添加任何人工阻尼电阻即可保证数值稳定收敛。
- 容差从1e-6放宽至1e-3时，CPU时间显著下降，但波形精度损失极小（误差仅增加0.13%），证明容差调节对工程应用具有高性价比。
- 固定步长200 µs无法解析故障清除后的微秒级高频振荡，而变步长求解器自动将步长加密至微秒级，实现全频段暂态精确捕捉。


## 关键公式

### 磁链状态空间微分方程

$$$p\phi = \omega_{base} (A\phi + v)$$$

*用于EMT时域积分求解，以磁链为状态变量避免电流求导带来的数值刚性，适用于单/双鼠笼及绕线转子结构。*

### 电磁转矩方程

$$$T_e = \phi_{ds} i_{qs} - \phi_{qs} i_{ds}$$$

*用于机电耦合动态分析，连接电气暂态与机械运动方程，计算电机输出转矩。*

### 转子运动方程

$$$p\omega_r = \frac{1}{2H}(T_e - T_m)$$$

*描述转子角速度在电磁转矩与机械负载转矩作用下的动态响应，适用于多质量块扩展。*

### Park坐标变换

$$$v_{qds} = P(\theta) v_{abcs}$$$

*实现三相交流量到dq旋转参考系的解耦，参考系可灵活切换（定子/转子/同步），简化微分方程系数矩阵。*



## 验证详情

- **验证方式**: 仿真对比验证（与工业级EMTP软件结果进行波形、误差范数及运行时间对比）
- **测试系统**: 1) 900 hp单鼠笼感应电机启动与机端三相短路系统；2) 含6台双鼠笼电机、2台同步机、非线性变压器及非线性负载的120 kV配电网（含故障与孤岛切换）；3) 工业厂用电多电机顺序启动系统。
- **仿真工具**: OpenModelica (DASSL变步长求解器) vs. EMTP (梯形-后向欧拉TBE固定步长求解器)
- **验证结果**: Modelica模型在三种典型EMT场景下均与EMTP基准结果高度吻合，相对误差<0.8%。变步长策略在长周期、多暂态切换场景中展现出显著的计算效率优势，且无需人工阻尼即可保证数值收敛，验证了声明式建模在EMT仿真中的高精度、高稳定性与高性能。
