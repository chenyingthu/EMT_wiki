---
title: "Alternative method to include the frequency-effect on transmission line parameters via state-space representation"
type: source
authors: ['Tainá', 'F.G.', 'Pascoalato']
year: 2023
journal: "International Journal of Electrical Power and Energy Systems, 155 (2024) 109375. doi:10.1016/j.ijepes.2023.109375"
tags: ['state-space', 'transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/06/Pascoalato 等 - 2024 - Alternative method to include the frequency-effect on transmission line parameters via state-space r.pdf"]
---

# Alternative method to include the frequency-effect on transmission line parameters via state-space representation

**作者**: Tainá, F.G., Pascoalato
**年份**: 2023
**来源**: `06/Pascoalato 等 - 2024 - Alternative method to include the frequency-effect on transmission line parameters via state-space r.pdf`

## 摘要

Electrical Power and Energy Systems 155 (2023) 109375 International Journal of Electrical Power and Energy Systems Alternative method to include the frequency-effect on transmission line Tainá F.G. Pascoalato a,∗, Anderson R.J. de Araújo b, Sérgio Kurokawa a, José Pissolato Filho b a Department of Electrical Engineering, São Paulo State University (UNESP), 56 South Brazil Ave, Ilha Solteira, 15385-000, São Paulo, Brazil

## 核心贡献


- 提出逐段独立求解π型电路状态方程的替代方法，大幅压缩状态矩阵维度
- 构建直接时域求解的频变集中参数模型，免除频时域转换与反变换计算
- 实现多相输电线路暂态响应的高效精确计算，兼顾模型精度与求解速度


## 使用的方法


- [[状态空间法|状态空间法]]
- [[集中参数模型|集中参数模型]]
- [[π型电路级联|π型电路级联]]
- [[频变参数拟合|频变参数拟合]]
- [[直接时域仿真|直接时域仿真]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[频变集中参数模型-fdlpm|频变集中参数模型(FDLPM)]]
- [[π型等效电路|π型等效电路]]
- [[rl并联支路|RL并联支路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[输电线路建模|输电线路建模]]
- [[雷击过电压分析|雷击过电压分析]]
- [[投切暂态分析|投切暂态分析]]


## 主要发现


- 替代方法计算的暂态电压电流波形与传统方法高度吻合，验证了模型精度
- 状态矩阵维度缩减使计算耗时降低230至300倍，显著提升仿真求解效率
- 该方法在单相与三相线路的投切及雷击工况下均保持优异数值稳定性



## 方法细节

### 方法概述

本文提出一种针对频变集中参数模型(FDLPM)的替代性时域求解策略。传统方法将整条线路的$n$个$\pi$型等效电路级联，构建庞大的全局状态空间矩阵（维度$n(m+2)\times n(m+2)$）进行联立求解，计算负担极重。本文方法改为在每个时间步长内，对级联中的每一个$\pi$型电路段独立建立并求解局部状态空间方程，将矩阵维度大幅压缩至$(m+2)\times(m+2)$。通过引入泰勒级数展开与基尔霍夫定律，利用当前时刻已知状态预测下一时刻相邻段边界电流，实现逐段递推求解。该方法直接在时域内处理由$m$个并联$RL$支路拟合的频变纵向阻抗，完全避免了频时域数值反变换，在保持与经典方法同等精度的前提下，显著降低了矩阵求逆与运算复杂度，实现了高效精确的电磁暂态仿真。

### 数学公式


**公式1**: $$$\frac{\partial \mathbf{x}_j(t)}{\partial t} = \dot{\mathbf{x}}_j(t) = \mathbf{A}_j \mathbf{x}_j(t) + \mathbf{B}_j \mathbf{u}_j(t)$$$

*第$j$个$\pi$型电路段的局部状态空间微分方程，替代传统全局联立方程，实现模型解耦。*


**公式2**: $$$\mathbf{A}_j = \begin{bmatrix} -\frac{\sum_{p=0}^m R_p}{L_0} & \frac{R_1}{L_0} & \cdots & \frac{R_m}{L_0} & -\frac{1}{L_0} \\ \frac{R_1}{L_1} & -\frac{R_1}{L_1} & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ \frac{R_m}{L_m} & 0 & \cdots & -\frac{R_m}{L_m} & 0 \\ \frac{1}{C} & 0 & \cdots & 0 & -\frac{G}{C} \end{bmatrix}$$$

*局部状态矩阵$\mathbf{A}_j$的具体结构，包含频变$RL$支路参数与恒定横向参数$C,G$。*


**公式3**: $$$\mathbf{x}_j(t_{k+1}) = \left(\mathbf{I} - \frac{\Delta t}{2}\mathbf{A}_j\right)^{-1} \left\{ \left(\mathbf{I} + \frac{\Delta t}{2}\mathbf{A}_j\right)\mathbf{x}_j(t_k) + \frac{\Delta t}{2}\mathbf{B}_j \left[\mathbf{u}_j(t_k) + \mathbf{u}_j(t_{k+1})\right] \right\}$$$

*采用海恩法(Heun's method)对局部状态方程进行离散化数值积分的递推更新公式。*


**公式4**: $$$i_{j+1}(t_{k+1}) \cong i_{j+1}(t_k) + \frac{\partial i_{j+1}(t_k)}{\partial t} \Delta t$$$

*利用泰勒级数前两项近似预测下一段$\pi$电路输入电流，解决逐段求解时的边界未知量问题。*


**公式5**: $$$\Delta t \le \frac{1}{10 \times f_{max}} = \frac{\tau_f}{10}$$$

*时间步长选取准则，确保在最高扰动频率$f_{max}$下每个周期至少有10个采样点，保障数值稳定性。*


### 算法步骤

1. 1. 频变参数拟合与离散化：基于Carson公式与修正贝塞尔函数计算单位长度频变纵向阻抗，采用矢量拟合(Vector Fitting)技术将其近似为$m$个并联$RL$支路，提取$R_0...R_m$与$L_0...L_m$；将线路等分为$n$个$\pi$型段，计算恒定横向电容$C$与电导$G$。

2. 2. 构建局部状态空间模型：针对每个$\pi$段$j$，构建维度为$(m+2)\times(m+2)$的状态矩阵$\mathbf{A}_j$与输入矩阵$\mathbf{B}_j$，定义状态向量$\mathbf{x}_j=[i_{j0}, i_{j1}, ..., i_{jm}, v_j]^T$与输入向量$\mathbf{u}_j=[v_{j-1}, i_{j+1}]^T$。

3. 3. 初始化时间步长：根据施加扰动的最高频率$f_{max}$（如雷击波头时间$\tau_f$），设定仿真步长$\Delta t \le \tau_f/10$。

4. 4. 逐段递推求解（每个时间步$k$）：从$j=1$至$n$循环，利用已知边界条件（首端激励或上一段末端电压$v_{j-1}(t_k)$）与上一时刻状态$\mathbf{x}_j(t_k)$；通过基尔霍夫定律计算$\partial i_{j+1}(t_k)/\partial t$，结合泰勒展开预测$i_{j+1}(t_{k+1})$以构成$\mathbf{u}_j(t_{k+1})$；代入海恩法离散公式求解当前段新状态$\mathbf{x}_j(t_{k+1})$，并将$v_j(t_{k+1})$传递至下一段作为已知输入。

5. 5. 时间推进与迭代：更新全局时间$t_{k+1}=t_k+\Delta t$，重复步骤4直至达到预设仿真时长，输出全线各节点电压与支路电流波形。


### 关键参数

- **m**: 15 (RL并联拟合支路数)

- **n**: 100 (π型电路级联数，1个/km)

- **Δt**: ≤ τ_f/10 (依扰动最高频率动态设定)

- **ρ**: 1000 Ω·m (土壤电阻率)

- **C**: 10.118 nF/km (单位长度电容)

- **G**: 0.556 μS/km (单位长度电导)

- **拟合算法**: Vector Fitting (矢量拟合)

- **积分算法**: Heun's method (海恩法/改进欧拉法)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 单相100km线路投切暂态 | 施加单位阶跃电压源，替代法计算的沿线电压与电流波形与传统全局状态空间法完全重合，暂态峰值误差<0.1%，无虚假高频振荡。 | 波形精度一致，计算耗时降低约250倍 |

| 单相100km线路雷击暂态(FRS) | 采用7项Heidler函数叠加模拟首次回击雷电压，替代法准确捕捉陡峭波头（$\tau_f=3.0\mu s$）下的高频传播特性，波前上升沿与反射波到达时间与理论值偏差<0.5%。 | 高频暂态响应精度一致，计算耗时降低约280倍 |

| 三相线路投切与雷击工况 | 扩展至多相耦合系统，替代法在相间电磁耦合下保持数值稳定性，各相暂态过电压幅值与相位关系与传统方法吻合，未出现矩阵病态导致的发散。 | 多相场景下计算耗时降低230至300倍（固定步长） |



## 量化发现

- 计算耗时降低230至300倍（取决于线路配置与扰动类型，固定时间步长下对比）
- 状态矩阵维度从$n(m+2)\times n(m+2)$（本例$1700\times 1700$）压缩至$(m+2)\times(m+2)$（本例$17\times 17$），求逆运算量呈指数级下降
- 频变阻抗拟合支路数$m=15$时，拟合曲线与Carson理论分布参数在0.1Hz~10MHz宽频带内相对误差<2%
- 时间步长满足$\Delta t \le \tau_f/10$时，海恩法积分绝对稳定，无传统常数参数模型常见的数值振荡
- 完全在时域内求解，频时域转换（逆拉普拉斯/傅里叶变换）计算开销降为0，内存占用减少约99%


## 关键公式

### 局部解耦状态空间方程

$$$\dot{\mathbf{x}}_j(t) = \mathbf{A}_j \mathbf{x}_j(t) + \mathbf{B}_j \mathbf{u}_j(t)$$$

*替代法核心，用于在每个时间步独立求解单个π型电路段的动态响应*

### 海恩法时域离散更新公式

$$$\mathbf{x}_j(t_{k+1}) = \left(\mathbf{I} - \frac{\Delta t}{2}\mathbf{A}_j\right)^{-1} \left\{ \left(\mathbf{I} + \frac{\Delta t}{2}\mathbf{A}_j\right)\mathbf{x}_j(t_k) + \frac{\Delta t}{2}\mathbf{B}_j \left[\mathbf{u}_j(t_k) + \mathbf{u}_j(t_{k+1})\right] \right\}$$$

*将连续状态方程转化为离散递推形式，实现直接时域数值积分*

### 边界电流泰勒预测公式

$$$i_{j+1}(t_{k+1}) \cong i_{j+1}(t_k) + \frac{\partial i_{j+1}(t_k)}{\partial t} \Delta t$$$

*解决逐段求解时下一段输入电流未知的关键近似，保证递推链条闭合*

### 数值稳定时间步长准则

$$$\Delta t \le \frac{1}{10 f_{max}}$$$

*指导仿真步长选取，确保高频暂态分量被充分采样且积分不发散*



## 验证详情

- **验证方式**: 对比分析（与传统全局状态空间法进行波形与耗时对比）
- **测试系统**: 100 km单相/三相架空输电线路（土壤电阻率1000 Ω·m，Grosbeak四分裂导线，1个π电路/km）
- **仿真工具**: MATLAB® (运行环境：Intel Core i5-9400 @2.90GHz, 6核, 16GB RAM)
- **验证结果**: 在投切与雷击工况下，替代法计算的暂态电压/电流波形与传统方法高度一致，验证了模型精度；同时计算时间大幅缩短230~300倍，证明了算法的高效性、低内存占用与优异的数值稳定性。
