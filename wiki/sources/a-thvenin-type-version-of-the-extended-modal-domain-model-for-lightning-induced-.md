---
title: "A Thévenin-Type Version of the Extended Modal-Domain Model for Lightning-Induced Voltage Calculation"
type: source
year: 2023
journal: "IEEE Transactions on Power Delivery;2023;38;1;10.1109/TPWRD.2022.3181445"
created: "2026-04-13"
sources: ["EMT_Doc/04/Leal和Conti - 2023 - A Thévenin-Type Version of the Extended Modal-Domain Model for Lightning-Induced Voltage Calculation.pdf"]
---

# A Thévenin-Type Version of the Extended Modal-Domain Model for Lightning-Induced Voltage Calculation

**年份**: 2023
**来源**: `04/Leal和Conti - 2023 - A Thévenin-Type Version of the Extended Modal-Domain Model for Lightning-Induced Voltage Calculation.pdf`

## 摘要

—In this paper, a new procedure is proposed for de- termining the external current sources required for evaluating lightning-induced voltages on overhead lines with the extended- modal domain (EMD) model. Unlike the original model, in which the calculation of the inducing current sources depends on the ﬁtting of the characteristic admittance of the line, in the proposed procedure this calculation is performed using the characteristic impedance of the line. This signiﬁcantly simpliﬁes the use of the EMD model because now all parameters can be readily obtained from the built-in ﬁtting tool that is usually available in electro- magnetic transient programs to derive the parameters of Marti’s transmission line model. The validity of the proposed procedure is demonstrated through examples that i

## 核心贡献


- 提出基于特征阻抗拟合的雷击感应电压计算方法，替代原特征导纳拟合流程。
- 将外部电磁场激励等效为戴维南型电流源，直接复用EMT软件内置线路拟合参数。
- 推导扩展模态域模型感应电流源的时域递归卷积算法，简化多导体线路建模。


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[戴维南等效变换|戴维南等效变换]]
- [[递归卷积算法|递归卷积算法]]
- [[模态域变换|模态域变换]]
- [[有理函数逼近|有理函数逼近]]


## 涉及的模型


- [[marti输电线路模型|Marti输电线路模型]]
- [[扩展模态域模型|扩展模态域模型]]
- [[多导体架空线路|多导体架空线路]]
- [[配电变压器|配电变压器]]
- [[避雷器|避雷器]]


## 相关主题


- [[雷击感应电压|雷击感应电压]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关线路建模|频率相关线路建模]]
- [[外部电磁场耦合|外部电磁场耦合]]
- [[配电线路过电压|配电线路过电压]]


## 主要发现


- 验证了基于特征阻抗的新方法在计算架空配电线路雷击感应电压时具有高精度。
- 新方法可直接调用EMT软件内置拟合参数，免除了用户独立编写拟合代码的需求。
- 在含变压器、避雷器及多点接地的复杂网络中，仿真波形与基准结果高度吻合。



## 方法细节

### 方法概述

本文提出一种基于特征阻抗（$Z_c$）拟合的扩展模态域（EMD）模型改进方法，用于计算架空线路雷击感应电压。传统EMD模型依赖特征导纳（$Y_c$）的有理函数拟合，而主流EMT软件（如ATP、PSCAD）内置的Marti线路模型仅直接提供$Z_c$的极点与留数。新方法通过戴维南-诺顿等效变换，将外部电磁场激励转化为线路两端的电流源，并修正递归卷积算法中的历史项，使其能够直接利用EMT软件内置拟合工具输出的$Z_c$参数。该方法避免了用户自行编写外部代码计算和拟合$Y_c$的繁琐流程，实现了感应电流源计算与Marti线路模型的无缝集成，大幅简化了多导体线路雷击过电压的建模与仿真流程。

### 数学公式


**公式1**: $$$z_{c,m}^{i,i}(t) = k_0^i \delta(t) + \sum_{n=1}^{N_p^i} k_n^i e^{a_n^i t} u(t)$$$

*特征阻抗模态分量的时域有理函数逼近表达式，用于将频域拟合参数转换为时域卷积核*


**公式2**: $$$e_{0,m}(t) = r_c i_{0,m}(t) + e_{h0,m}(t-\Delta t)$$$

*无外部激励时，模态电压降的递归卷积计算公式*


**公式3**: $$$e_{0,m}(t) = r_c (i_{0,m}(t) + \bar{j}_{0,m}(t)) + e_{h0,m}(t-\Delta t) + e_{u0,m}(t-\Delta t)$$$

*引入外部感应电流源后的修正电压降方程，包含线路内部历史项与外部源历史项*


**公式4**: $$$\bar{j}_{0,m}(t) = g_c [\bar{u}_{0,m}(t) - e_{u0,m}(t-\Delta t)]$$$

*修正后的模态感应电流源计算公式，用于在诺顿等效电路中准确补偿外部电磁场激励的历史效应*


**公式5**: $$$j_0(t) = t_I \bar{j}_{0,m}(t)$$$

*通过实常数模态变换矩阵$t_I$将模域电流源转换回相域，以便注入EMT软件*


### 算法步骤

1. 利用EMT软件内置拟合工具（如ATP的Bode渐近法），在0.1 Hz至10 MHz频段内对线路特征阻抗矩阵$Z_c$进行矢量拟合，提取各模态的极点$a_n^i$、留数$k_n^i$及高频渐近常数$k_0^i$。

2. 根据拟合参数计算模态等效电阻矩阵$r_c$及其逆矩阵$g_c = r_c^{-1}$，并计算递归系数$p_n^i = (2+a_n^i \Delta t)/(2-a_n^i \Delta t)$与$q_n^i = k_n^i \Delta t/(2-a_n^i \Delta t)$。

3. 基于Barbosa-Paulino公式计算入射电磁场在频域的效应，经模态变换矩阵$t_I$转换至模域，得到时域激励电压$\bar{u}_{0,m}(t)$与$\bar{u}_{L,m}(t)$。

4. 初始化历史项矩阵$e_{h0,m}$与$e_{u0,m}$为零向量/矩阵。

5. 在每个仿真时间步$\Delta t$，利用递归公式更新线路内部电流历史项$e_{h0,m}$与外部源历史项$e_{u0,m}$，其中外部源历史项需叠加当前步与上一步的感应电流源值。

6. 代入修正公式$\bar{j}_{0,m}(t) = g_c [\bar{u}_{0,m}(t) - e_{u0,m}(t-\Delta t)]$计算当前时刻的模态感应电流源。

7. 通过相模变换$j_0(t) = t_I \bar{j}_{0,m}(t)$将电流源转换回相域，并作为外部独立电流源注入EMT软件中的Marti线路模型两端节点。

8. 重复步骤5-7直至仿真结束，同步求解线路终端非线性负载（如变压器、避雷器）的暂态响应，完成全系统电磁暂态计算。


### 关键参数

- **拟合频段**: 0.1 Hz ~ 10 MHz (20点/十倍频)

- **大地电导率**: 0.002 S/m

- **导体直流电阻**: 0.822 Ω/km

- **导体半径**: 8.5 mm

- **模态变换参考频率$f_0$**: 1 MHz

- **变压器额定容量**: 10 kVA (7967/120-240 V)

- **避雷器参数**: 12 kV级无间隙氧化锌避雷器，10 kA (8/20 μs)残压39.6 kV

- **中性线接地**: 每300 m接地，接地电阻50 Ω



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 3-km三相中压配电线路（匹配与不平衡负载） | 雷击点距线路末端100 m。在500 Ω匹配负载及多导体不平衡负载工况下，B相感应电压波形呈现典型的双峰特征与多次反射振荡。 | 新模型计算波形与原始EMD模型及扩展相域(EPD)参考模型在绘图精度内完全重合，验证了多反射条件下的等效性。 |

| 1.2-km单相农村配电线路（含变压器与避雷器） | 线路含多点接地中性线及10 kVA宽频变压器。无避雷器时一次侧相地电压峰值达50 kV；加装12 kV级避雷器后，一次侧峰值降至30 kV，二次侧峰值由2 kV降至1.45 kV。 | 在包含变压器高频谐振、中性线多点反射及避雷器非线性动作的复杂工况下，新模型结果与EPD模型高度一致，且计算流程无需外部代码干预。 |



## 量化发现

- 新方法计算结果与原始EMD模型及EPD参考模型的波形误差可忽略不计（在仿真绘图精度内完全重合）。
- 避雷器安装使变压器一次侧雷击感应过电压峰值降低40%（从50 kV降至30 kV）。
- 避雷器动作使传递至变压器二次侧的过电压峰值降低约30%（从2 kV降至1.45 kV）。
- 拟合频段覆盖0.1 Hz至10 MHz，采用20点/十倍频采样即可保证全频段参数精度，满足雷击高频暂态需求。
- 模态变换矩阵参考频率在1 kHz至500 kHz范围内测试，结果无差异，证实1 MHz参考频率的鲁棒性。


## 关键公式

### 修正的模态感应电流源计算公式

$$$\bar{j}_{0,m}(t) = g_c [\bar{u}_{0,m}(t) - e_{u0,m}(t-\Delta t)]$$$

*用于在诺顿等效电路中准确补偿外部电磁场激励的历史效应，解决传统方法中直接叠加电流源导致递归卷积失真的问题*

### 含外源激励的戴维南型电压降递归方程

$$$e_{0,m}(t) = r_c (i_{0,m}(t) + \bar{j}_{0,m}(t)) + e_{h0,m}(t-\Delta t) + e_{u0,m}(t-\Delta t)$$$

*推导电流源修正项的核心方程，将外部场激励与线路内部状态解耦，实现与Marti线路模型的直接兼容*



## 验证详情

- **验证方式**: 对比仿真验证（与原始EMD模型、扩展相域EPD模型进行波形对比）
- **测试系统**: 3-km三相中压配电线路（匹配/不平衡负载）；1.2-km单相农村配电线路（含多点接地中性线、10kVA宽频变压器模型及氧化锌避雷器）
- **仿真工具**: ATP (EMD-ATP自定义代码、内置Marti模型拟合工具、ULM-ATP)
- **验证结果**: 在包含复杂终端负载、多点接地及非线性避雷器动作的工况下，新模型计算的感应电压波形与经过现场实测和FDTD/LIOV代码验证的EPD及原始EMD模型结果高度一致，证明了基于$Z_c$拟合的戴维南型EMD模型在工程应用中的高精度与可靠性，且彻底免除了用户外部编写拟合代码的需求。
