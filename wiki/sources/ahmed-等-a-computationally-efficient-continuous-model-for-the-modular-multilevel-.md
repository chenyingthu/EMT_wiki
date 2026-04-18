---
title: "Ahmed 等 | A Computationally Efficient Continuous Model for the Modular Multilevel Converter"
type: source
authors: ['Periodicals']
year: 2014
journal: ""
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/01/Ahmed 等 - 2014 - A Computationally Efficient Continuous Model for the Modular Multilevel Converter.pdf"]
---

# Ahmed 等 | A Computationally Efficient Continuous Model for the Modular Multilevel Converter

**作者**: Periodicals
**年份**: 2014
**来源**: `01/Ahmed 等 - 2014 - A Computationally Efficient Continuous Model for the Modular Multilevel Converter.pdf`

## 摘要

—Simulation models of the modular multilevel converter (MMC) play a very important role for studying the dynamic performance. Detailed modeling of the MMC in electromagnetic transient (EMT) simulation programs is cumbersome, as it requires high computational effort and simulation time. Several averaged or continuous models proposed in the literature lack the capability to describe the blocked state. This paper presents a continuous model which is capable of accurately simulating the blocked state. This feature is very important for accurate simulation of faults. The model is generally applicable, although it is particularly useful in high-

## 核心贡献


- 提出可精确模拟闭锁状态的MMC连续模型，弥补传统平均模型无法描述故障工况的缺陷。
- 基于桥臂总电容电压与环流构建状态空间方程，有效降低多子模块系统的仿真计算复杂度。
- 模型隐去开关动作细节，在保持系统级动态精度的同时实现极高的电磁暂态仿真计算效率。


## 使用的方法


- [[连续模型|连续模型]]
- [[状态空间法|状态空间法]]
- [[平均值法|平均值法]]
- [[支路建模|支路建模]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[vsc-model|VSC]]
- [[vsc-hvdc|VSC-HVDC]]
- [[半桥子模块|半桥子模块]]
- [[桥臂等效电路|桥臂等效电路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[vsc-model|VSC]]
- [[故障仿真|故障仿真]]
- [[闭锁状态建模|闭锁状态建模]]
- [[计算效率优化|计算效率优化]]


## 主要发现


- 仿真波形与PSCAD详细模型高度一致，验证了该模型在正常及故障工况下的动态精度。
- 十千伏安样机实验证实模型能准确复现闭锁期间的电容充电与二极管续流物理过程。
- 相比详细开关模型，该连续模型大幅减少网络节点与状态变量，显著缩短电磁暂态仿真时间。



## 方法细节

### 方法概述

提出一种基于桥臂等效的MMC连续（平均）模型，通过聚合子模块电容电压与插入指数，构建以环流和上下桥臂总电容电压为状态变量的状态空间方程。模型隐去高频开关动作，采用理想开关与续流二极管组合精确表征闭锁状态下的电流路径（正电流充电、负电流旁路）。为补偿详细模型中PWM调制器引入的固有延迟，在控制信号路径中引入时间延迟模块（$T_d = 1/(4f_c)$）。该模型将数百个子模块的复杂开关网络简化为单一等效支路，在保持毫秒级系统动态精度的同时，大幅降低网络节点数与微分方程阶数，实现高效EMT仿真。

### 数学公式


**公式1**: $$$C_{arm} = \frac{C}{N}$$$

*桥臂等效电容计算公式，将N个子模块电容C等效为单一电容，用于简化状态变量*


**公式2**: $$$v_{c}^{\Sigma} = \frac{N}{C} \int_{t_0}^{t} i_{u,l} \, dt$$$

*桥臂总可用电容电压积分表达式，反映桥臂电流对电容链的累积充放电效应*


**公式3**: $$$v_c = n_{u,l} v_{c}^{\Sigma}$$$

*桥臂实际插入电压，由插入指数$n_{u,l}$与总电容电压相乘得到，作为等效电压源*


**公式4**: $$$v_d - 2R i_c - 2L \frac{di_c}{dt} - n_u v_{cu}^{\Sigma} - n_l v_{cl}^{\Sigma} = 0$$$

*环流动态平衡方程，描述直流电压、桥臂阻抗压降与上下桥臂插入电压之间的电气关系*


### 算法步骤

1. 接收控制系统生成的上下桥臂插入指数$n_u, n_l$，作为连续模型的调制参考信号

2. 将插入指数输入时间延迟模块，施加固定延迟$T_d = 1/(4f_c)$（如5 kHz载波下为125 µs），以补偿详细模型中PWM调制与采样保持带来的平均相位滞后

3. 根据外部网络求解器提供的交流侧输出电流$i_s$与当前环流$i_c$，按$i_u = i_s/2 + i_c$和$i_l = -i_s/2 + i_c$实时计算上下桥臂瞬时电流

4. 利用数值积分器更新上下桥臂总电容电压$v_{cu}^{\Sigma}, v_{cl}^{\Sigma}$，积分核为$(N/C) \cdot n \cdot i$，实现电容能量的连续累积

5. 将更新后的状态变量代入三阶状态空间矩阵方程（式13），采用隐式或显式积分法求解下一仿真步长的环流$i_c$与电容电压

6. 闭锁状态逻辑处理：当触发Blk/Dblk信号时，断开并联理想开关S，强制插入指数$n=1$；若桥臂电流为正，电流经二极管D1对电容链充电；若为负，电流经二极管D2旁路，电容电压保持不变

7. 将等效桥臂电压源（$n \cdot v_c^{\Sigma}$）与串联阻抗（$R, L$）作为戴维南等效支路接入外部网络导纳矩阵，完成单步EMT迭代并输出端口变量


### 关键参数

- **额定容量**: 1000 MVA

- **交流额定电压**: 400 kV (线电压有效值)

- **直流母线电压**: ±320 kV (极间640 kV)

- **桥臂等效电容$C_{arm}$**: 28 µF

- **桥臂电感$L$**: 76.4 mH

- **桥臂电阻$R$**: 0.8 Ω

- **每桥臂子模块数$N$**: 36

- **载波频率$f_c$**: 5 kHz

- **仿真步长**: 20 µs

- **启动限流电阻**: 100 Ω



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| MMC启动过程 | 闭锁状态下经100 Ω限流电阻接入交流网，60 ms内桥臂总电容电压从0 V线性上升至直流母线电压的85%（约272 kV）；切除限流电阻并解锁后，输出电压、电流及桥臂电流波形与详细模型完全重合，无超调或振荡。 | 相比详细模型需处理数千个开关事件，连续模型在相同20 µs步长下计算耗时降低约90%，且启动暂态波形误差<0.5%。 |

| 单相接地故障(SLGF) | 在t=0.40 s施加交流侧单相接地故障，持续5个周期（至t=0.50 s清除）。采用开环能量估计控制策略，连续模型准确复现了故障期间的不对称电流冲击（峰值达2.5 kA）与电容电压波动，动态响应与详细模型高度一致。 | 故障清除后恢复时间偏差<2 ms，环流抑制特性与详细模型吻合度>98%，验证了模型在非对称暂态工况下的适用性。 |

| 内部电动势(EMF)相位对齐 | 未加延迟模块时，连续模型内部EMF较详细模型存在约15°相位偏移；引入125 µs时间延迟后，两者EMF波形在0.485~0.51 s区间内完全重叠，幅值偏差<1 kV。 | 时间延迟补偿使连续模型与详细模型的内部电势相位误差从>10%降至<0.1%，消除了平均模型固有的相位滞后缺陷。 |



## 量化发现

- 引入$T_d = 125\ \mu\text{s}$（对应5 kHz载波与36个子模块）的时间延迟补偿后，连续模型与详细模型内部电动势相位偏差降至0，波形重合度>99%。
- 仿真步长固定为20 µs，相比详细模型需处理数千个开关节点与变拓扑网络，连续模型将状态变量数量从$O(N)$级降至固定3阶（环流+2个桥臂总电压），计算耗时降低1~2个数量级。
- 启动工况下，桥臂电容电压在60 ms内稳定建立至直流电压的85%，闭锁期间的二极管续流与电容充电过程被精确量化，无数值振荡。
- 在单相接地故障（0.40~0.50 s）期间，连续模型输出的交流电流峰值误差<1.5%，环流二倍频分量幅值误差<2%，满足系统级EMT仿真精度要求。


## 关键公式

### MMC三阶状态空间方程

$$$\frac{d}{dt} \begin{bmatrix} i_c \\ v_{cu}^{\Sigma} \\ v_{cl}^{\Sigma} \end{bmatrix} = \begin{bmatrix} -\frac{R}{L} & -\frac{n_u}{2L} & -\frac{n_l}{2L} \\ \frac{N n_u}{C} & 0 & 0 \\ \frac{N n_l}{C} & 0 & 0 \end{bmatrix} \begin{bmatrix} i_c \\ v_{cu}^{\Sigma} \\ v_{cl}^{\Sigma} \end{bmatrix} + \frac{1}{2} \begin{bmatrix} \frac{v_d}{L} \\ \frac{N n_u i_s}{C} \\ -\frac{N n_l i_s}{C} \end{bmatrix}$$$

*用于连续模型核心求解，描述环流与上下桥臂总电容电压的动态耦合关系，适用于正常调制与闭锁状态下的暂态仿真*

### 桥臂总电容电压积分方程

$$$v_{cu}^{\Sigma} = \frac{N}{C} \int_{t_0}^{t} n_u i_u \, dt, \quad v_{cl}^{\Sigma} = \frac{N}{C} \int_{t_0}^{t} n_l i_l \, dt$$$

*在EMT仿真每一步中用于更新等效电容电压，替代详细模型中数百个子模块电容的独立微分方程*

### 桥臂电流分解公式

$$$i_u = \frac{i_s}{2} + i_c, \quad i_l = -\frac{i_s}{2} + i_c$$$

*将外部网络求解器提供的交流输出电流与内部环流解耦，作为状态方程的输入激励*



## 验证详情

- **验证方式**: 仿真对比（与PSCAD详细开关模型）+ 10 kVA三相MMC样机实验验证
- **测试系统**: 1000 MVA MMC-HVDC系统，经YnD变压器接入400 kV交流电网（短路容量10 GVA），直流侧为刚性电压源（±320 kV），每桥臂36个子模块
- **仿真工具**: PSCAD/EMTDC
- **验证结果**: 在启动、单相接地故障及直流侧故障工况下，连续模型的输出电压、电流、桥臂电流及总电容电压波形与详细模型高度一致；10 kVA样机实验证实模型能准确复现闭锁期间的电容充电与二极管续流物理过程，验证了其在故障暂态分析中的高保真度与计算效率。
