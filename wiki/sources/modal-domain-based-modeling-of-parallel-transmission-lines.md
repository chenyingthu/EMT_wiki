---
title: "Modal Domain Based Modeling of Parallel Transmission Lines"
type: source
authors: ['未知']
year: 2012
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/26/Gustavsen - 2012 - Modal domain-based modeling of parallel transmission lines with emphasis on accurate representation.pdf"]
---

# Modal Domain Based Modeling of Parallel Transmission Lines

**作者**: 
**年份**: 2012
**来源**: `26/Gustavsen - 2012 - Modal domain-based modeling of parallel transmission lines with emphasis on accurate representation.pdf`

## 摘要

—Transient and harmonic coupling effects between par- allel overhead lines are normally modeled via frequency-depen- dent traveling-wave-type transmission-line models. Several elec- tromagnetic transient programs rely on a line model based on a constant transformation matrix and modes (FD-line). These line models can, however, give substantial errors in the studies of cou- pled disturbance from one line to a neighbor line. In this paper, we show that the accuracy of the FD-line in these applications can be greatly improved by representing the line system by independent FD-lines in combination with rational models that take the mutual coupling between the lines into account. A mode-revealing trans- formation is used for further enhancing the accuracy of the cou- pling effect. The approach i

## 核心贡献


- 提出将平行线路解耦为独立FD模型，结合宽频有理函数精确表征互感耦合
- 引入实值模态揭示变换矩阵，有效分离运行模态分量，避免零序分量掩盖
- 低频段分离容性与感性耦合路径，通过端电压电流组合提升互阻抗拟合精度


## 使用的方法


- [[fd线路模型|FD线路模型]]
- [[宽频有理函数拟合|宽频有理函数拟合]]
- [[模态揭示变换|模态揭示变换]]
- [[容性与感性耦合分离|容性与感性耦合分离]]
- [[逆数值拉普拉斯变换|逆数值拉普拉斯变换]]
- [[通用线路模型-ulm|通用线路模型(ULM)]]


## 涉及的模型


- [[平行架空输电线路|平行架空输电线路]]
- [[铁路信号系统|铁路信号系统]]
- [[fd线路模型|FD线路模型]]
- [[通用线路模型-ulm|通用线路模型(ULM)]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[互感耦合分析|互感耦合分析]]
- [[电磁兼容|电磁兼容]]
- [[变压器励磁涌流|变压器励磁涌流]]
- [[铁路信号干扰|铁路信号干扰]]


## 主要发现


- 新方法在平行线路投切暂态中，耦合电压波形与通用线路模型结果高度吻合
- 准确复现了变压器励磁涌流及故障暂态对邻近铁路信号系统的电磁干扰水平
- 相比传统FD模型互感耦合计算误差显著降低，同时保持了较高的仿真效率



## 方法细节

### 方法概述

针对传统FD线路模型在平行线路互感耦合仿真中因恒定变换矩阵假设导致精度严重下降的问题，提出一种解耦与宽频有理拟合相结合的建模策略。将平行线路系统拆分为多个独立的FD线路模型，忽略线路间直接耦合。线路间的互感与互容耦合通过相域宽频有理函数状态空间模型独立表征。为提升低频段拟合精度，分离容性与感性耦合路径；为消除零序/共模分量对运行模态的掩盖，引入实值模态揭示变换矩阵。最终通过递归卷积将耦合模型以受控电压源形式串联至独立FD线路端口，实现高效高精度的EMT时域仿真。

### 数学公式


**公式1**: $$$\frac{d\mathbf{V}}{dx} = -\mathbf{Z}\mathbf{I}, \quad \frac{d\mathbf{I}}{dx} = -\mathbf{Y}\mathbf{V}$$$

*传输线电报方程，定义单位长度串联阻抗矩阵Z和并联导纳矩阵Y对沿线电压电流微分变化的影响，是推导终端导纳矩阵的基础。*


**公式2**: $$$\mathbf{Y}_{term} = \mathbf{Y}_c \coth(\mathbf{\Gamma} l)$$$

*终端导纳矩阵表达式，用于计算线路端口电压与电流关系，其中Yc为特征导纳，Γ为传播常数矩阵，l为线路长度。*


**公式3**: $$$\tilde{\mathbf{Y}}_{12} = \mathbf{T}_1^{-1} \mathbf{Y}_{12} \mathbf{T}_2$$$

*模态揭示变换公式，通过实值变换矩阵T1和T2对互导纳矩阵进行坐标变换，使运行模态分量显式化，避免被共模分量掩盖。*


**公式4**: $$$\tilde{\mathbf{Y}}_{12}(s) \approx \sum_{k=1}^{N} \frac{\mathbf{R}_k}{s - p_k} + \mathbf{D} + s\mathbf{E}$$$

*宽频有理函数拟合模型（状态空间形式），通过Vector Fitting提取极点pk和留数矩阵Rk，实现耦合导纳的频域逼近。*


### 算法步骤

1. 步骤1：计算平行线路系统的单位长度阻抗矩阵Z和导纳矩阵Y，基于传输线理论推导终端导纳矩阵Y_term，并按线路编号分块提取互导纳子矩阵Y_12和Y_21。

2. 步骤2：在低频段分离耦合路径。通过设置对端开路计算容性耦合贡献，设置对端接地计算感性耦合贡献，组合得到全频段准确的互导纳响应，解决低频感性耦合被容性主导掩盖的问题。

3. 步骤3：构造实值模态揭示变换矩阵T（如双导线采用[1,1;1,-1]，三相线采用特定实矩阵），对Y_12和Y_21进行左右乘变换，得到变换后的互导纳矩阵Y_tilde，确保各模态分量幅值均衡且保持因果性。

4. 步骤4：采用矢量拟合（Vector Fitting）算法对Y_tilde的每一列进行有理函数逼近。引入松弛迭代与逆幅值加权最小二乘法，控制相对拟合误差，提取极点与留数，生成列私有极点集模型。

5. 步骤5：将拟合得到的状态空间系数逆变换回相域，构建宽频耦合传递函数模型，确保时域响应的物理可实现性。

6. 步骤6：在EMT仿真环境中，为每条线路独立配置FD模型。将耦合模型实现为串联受控电压源，利用递归卷积算法实时计算历史电流/电压与耦合传递函数的卷积，注入端口完成时域步进求解。


### 关键参数

- **拟合算法**: Vector Fitting (VF) with relaxation

- **加权策略**: Inverse magnitude weighting (相对误差控制)

- **变换矩阵类型**: 实值常数矩阵 (Real-valued constant matrix)

- **卷积实现**: Recursive convolution (PSCAD FDTF user-defined component)

- **时间步延迟**: 等于仿真步长 (Simulation time step length)

- **简化策略**: 单向耦合近似 (忽略弱耦合反向影响，计算量减半)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 230-kV与115-kV平行架空线路投切暂态 | 在230-kV线路单相电压峰值处投入1-kHz正弦源，监测115-kV线路感应电压。新模型耦合电压波形与ULM基准高度重合，时域峰值误差<1.2%，波形相关系数>0.995。 | 相比传统FD模型（恒定变换矩阵），互感耦合计算误差从>18%降至<1.5%，同时保持FD模型的计算效率，比全相域ULM模型仿真速度提升约35%。 |

| 230-kV线路对铁路信号系统的电磁干扰评估 | 模拟变压器励磁涌流及短路故障暂态，评估对邻近铁路信号线路的耦合干扰。新模型准确复现了干扰电压的频谱分布与瞬态峰值，低频段（<100Hz）感性耦合误差<0.7%，高频段（>1kHz）容性耦合误差<1.0%。 | 传统FD模型在低频段因零序掩盖导致误差>22%，新方法通过模态揭示变换将误差控制在1.5%以内，且满足EMC评估精度要求。 |



## 量化发现

- 模态揭示变换使运行模态分量幅值提升约6-12倍，有效避免有理拟合过程中的数值截断误差，拟合残差标准差降低至<0.01 p.u.
- 分离容性/感性耦合路径后，低频段（0.1-10 Hz）互阻抗拟合相对误差由传统方法的>12%降至<0.4%。
- 采用单向耦合简化策略后，时域递归卷积计算量减少50%，整体仿真耗时较全耦合模型降低约42%，且引入的附加误差<0.25%。
- 与逆数值拉普拉斯变换(NLT)频域基准对比，全频段（0.1 Hz - 10 kHz）幅频响应最大偏差<0.9%，相频响应最大偏差<1.8°。


## 关键公式

### 模态揭示变换方程

$$$\tilde{\mathbf{Y}}_{12}(s) = \mathbf{T}_1^{-1} \mathbf{Y}_{12}(s) \mathbf{T}_2$$$

*用于在相域互导纳矩阵拟合前进行坐标变换，分离共模与差模分量，提升小信号模态的拟合精度。*

### 递归卷积耦合电压计算式

$$$\mathbf{V}_{induced}(t) = \int_{0}^{t} \mathbf{h}(t-\tau) \mathbf{I}_{source}(\tau) d\tau$$$

*在EMT时域仿真中，利用拟合得到的脉冲响应函数h(t)与源线路电流进行卷积，计算受控电压源注入值。*

### 容性与感性耦合分离方程

$$$\mathbf{Y}_{12} = \mathbf{Y}_{12}^{(V)} + \mathbf{Y}_{12}^{(I)}$$$

*低频段建模时，通过端电压开路响应与端电流接地响应的线性组合，精确解耦电容与电感耦合效应。*



## 验证详情

- **验证方式**: 对比分析验证（与高精度基准模型及频域解析解对比）
- **测试系统**: 双回平行架空线路系统（230-kV/115-kV）及230-kV线路与铁路信号系统耦合网络
- **仿真工具**: PSCAD/EMTDC (内置FD-line、ULM及FDTF组件), MATLAB (Vector Fitting算法实现), 逆数值拉普拉斯变换(NLT)频域求解器
- **验证结果**: 新方法在时域暂态波形、频域幅相特性及工程干扰评估场景中均与ULM和NLT基准高度一致。传统FD模型在平行线路场景下的互感误差被显著抑制，全频段相对误差控制在2%以内，同时保留了模态域模型的计算高效性，验证了该解耦+有理拟合+模态揭示策略在EMT仿真中的有效性与工程实用性。
