---
title: "Comprehensive [formula omitted] impedance modeling of AC power-electronics-based power systems with frequency-dependent transmission lines"
type: source
authors: ['Julio Hernández-Ramírez']
year: 2024
journal: "Electric Power Systems Research, 235 (2024) 110847. doi:10.1016/j.epsr.2024.110847"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/11/Hernández-Ramírez 等 - 2024 - Comprehensive D Q impedance modeling of AC power-electronics-based power systems with frequency-depe.pdf"]
---

# Comprehensive [formula omitted] impedance modeling of AC power-electronics-based power systems with frequency-dependent transmission lines

**作者**: Julio Hernández-Ramírez
**年份**: 2024
**来源**: `11/Hernández-Ramírez 等 - 2024 - Comprehensive D Q impedance modeling of AC power-electronics-based power systems with frequency-depe.pdf`

## 摘要

0378-7796/© 2024 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies. Comprehensive 𝐷𝑄impedance modeling of AC power-electronics-based power systems with frequency-dependent transmission lines Julio Hernández-Ramírez a, Juan Segundo-Ramírez a,∗, Marta Molinas b a Autonomous University of San Luis Potosí, Engineering Department, Dr. Manuel Nava No. 8, Zona Universitaria Poniente, San Luis Potosí, 78290, San Luis

## 核心贡献


- 提出时频混合解析法，实现含频变线路的电力电子系统宽频DQ阻抗精确建模。
- 直接采用频域双曲函数解析解表征输电线路，避免有理逼近与集总参数截断误差。
- 基于谐波平衡法精确求解含无限维频变元件的非线性系统稳态，免除重复时域仿真。


## 使用的方法


- [[谐波平衡法|谐波平衡法]]
- [[时频混合解析法|时频混合解析法]]
- [[dq阻抗建模|DQ阻抗建模]]
- [[频域电报方程|频域电报方程]]
- [[频率扫描法|频率扫描法]]
- [[奈奎斯特稳定判据|奈奎斯特稳定判据]]


## 涉及的模型


- [[电力电子变流器|电力电子变流器]]
- [[频变输电线路|频变输电线路]]
- [[分布参数模型|分布参数模型]]
- [[pwm延时模型|PWM延时模型]]


## 相关主题


- [[谐波稳定性|谐波稳定性]]
- [[阻抗建模|阻抗建模]]
- [[频率相关建模|频率相关建模]]
- [[小信号稳定性分析|小信号稳定性分析]]
- [[实时仿真验证|实时仿真验证]]
- [[电磁暂态分析|电磁暂态分析]]


## 主要发现


- 模型精确保留线路高频动态，稳态计算结果与OPAL-RT及PSCAD仿真高度吻合。
- 基于该阻抗模型的奈奎斯特判据分析结果准确，有效预测系统谐波稳定性边界。
- 相比传统频率扫描与有理拟合方法，该解析法大幅降低计算负担并避免仿真误差。



## 方法细节

### 方法概述

提出一种时频混合解析法，用于精确识别含频变分布参数输电线路的电力电子系统宽频DQ阻抗模型。该方法将系统解耦为非线性电力电子子系统（时域DQ框架）与线性网络/输电线路子系统（频域ABC框架）。利用谐波平衡法（HBM）迭代求解含无限维频变元件的非线性系统精确稳态，避免传统时域积分与有理逼近误差。随后，基于频域电报方程的双曲函数解析解，结合Park变换的频移特性，通过注入正负序三相电压扫描，直接解析计算DQ域导纳矩阵，无需重复时域仿真、FFT或有理拟合，实现全频段高精度阻抗建模。

### 数学公式


**公式1**: $$$\frac{d\mathbf{V}(z,s)}{dz} = -\mathbf{Z}(s)\mathbf{I}(z,s), \quad \frac{d\mathbf{I}(z,s)}{dz} = -\mathbf{Y}(s)\mathbf{V}(z,s)$$$

*频域电报方程，描述均匀输电线路沿线电压与电流的分布关系，其中$\mathbf{Z}(s)$和$\mathbf{Y}(s)$为单位长度阻抗与导纳矩阵。*


**公式2**: $$$\mathbf{I}_0(s) = \mathbf{Y}_{tl}(s)\mathbf{V}_0(s), \quad \mathbf{Y}_{tl}(s) = \mathbf{A} - \mathbf{B}(\mathbf{A} + \mathbf{Y}_r)^{-1}\mathbf{B}$$$

*输电线路单端等效导纳模型，利用双曲函数矩阵$\mathbf{A}$和$\mathbf{B}$精确表征分布参数与频变特性，避免集总参数截断。*


**公式3**: $$$\mathbf{X}_{DQ}(s) = \mathbf{K}_1 \mathbf{X}_{abc}(s - j\omega_0) + \mathbf{K}_2 \mathbf{X}_{abc}(s + j\omega_0)$$$

*Park变换在拉普拉斯域的频移表达式，建立ABC相坐标系与DQ旋转坐标系之间的线性映射关系，是频域阻抗转换的核心。*


**公式4**: $$$\begin{bmatrix} Y_{g}^{DD} & Y_{g}^{DQ} \\ Y_{g}^{QD} & Y_{g}^{QQ} \end{bmatrix} = \begin{bmatrix} I_0^D & I_{0-}^D \\ I_0^Q & I_{0-}^Q \end{bmatrix} \begin{bmatrix} V_0^D & V_{0-}^D \\ V_0^Q & V_{0-}^Q \end{bmatrix}^{-1}$$$

*DQ域导纳矩阵解析识别公式，通过正序与负序电压激励下的电流响应直接求解，无需数值拟合。*


### 算法步骤

1. 系统解耦与框架分配：将含电力电子变流器(PEDs)和输电线路(TLs)的系统拆分为非线性子系统（在时域DQ框架下建模，保留开关延时与控制非线性）与线性网络子系统（在频域ABC框架下建模，采用频变分布参数TL解析模型）。

2. 稳态初值设定：为各非线性子系统接口电压设定初始猜测值$v_k^{(0)}$，若缺乏先验信息，可对非线性部分进行6个工频周期的数值积分以衰减初始暂态。

3. 非线性子系统稳态求解：在给定接口电压下，利用牛顿-拉夫逊法求解非线性子系统的微分代数方程$\mathbf{f}_k(\mathbf{x}_k^{(i+1)}, v_k^{(i)}) = 0$，获取状态向量$\mathbf{x}_k^{(i+1)}$及注入电流$i_k^{(i+1)}$。

4. 线性网络频域求解：将非线性子系统输出的时域电流转换为频域相量，代入线性网络节点导纳方程$\mathbf{I}^{(i+1)}(s) = \mathbf{Y}(s)\mathbf{V}^{(i+1)}(s)$（令$s=j\omega_0$），求解得到接口节点电压相量$V_k^{(i+1)}(j\omega_0)$。

5. 时频域转换与迭代更新：将求得的电压相量逆变换回时域形式$v_k^{(i+1)}(t)$，作为下一轮迭代的输入。计算收敛误差$\|\mathcal{D}^{(i+1)} - \mathcal{D}^{(i)}\|$，若小于设定容差$\epsilon$则停止，否则返回步骤3继续迭代。

6. 宽频阻抗扫描激励：在精确稳态工作点基础上，针对目标频率$\omega_n$，分别注入幅值相同的平衡正序与负序三相电压扰动。

7. 频域响应解析计算：利用输电线路频域解析模型，直接计算系统在频移点$s=j(\omega_n \pm \omega_0)$处的ABC域电压与电流响应，全程避免FFT与有理函数拟合。

8. DQ阻抗矩阵构建：通过Park变换频移关系将ABC响应映射至DQ域，结合正负序激励下的电压电流向量，利用矩阵求逆公式直接解析得到目标频率下的完整DQ导纳/阻抗矩阵。


### 关键参数

- **收敛容差**: $\epsilon = 10^{-10}$

- **HBM迭代次数**: 15次

- **系统基准值**: 34.5 kV, 100 MVA, 60 Hz

- **VSC-1滤波参数**: $R_{c1}=0.008$ p.u., $L_{c1}=0.18$ p.u., $C_{f1}=0.15$ p.u.

- **VSC-2滤波参数**: $R_{c2}=0.005$ p.u., $L_{c2}=0.12$ p.u.

- **输电线路长度**: TL1: 95 km, TL2: 75 km

- **线路几何参数**: 下层导线高度28 m, 导线间距7 m, 半径$r_c=1.40716$ cm, 电阻率$\rho=0.07284\ \Omega/km$

- **电网等效阻抗**: $R_{th}=1.761\ \Omega$, $L_{th}=93.431$ mH

- **PWM延时**: $T_{d1}=181.159\ \mu s$, $T_{d2}=198.412\ \mu s$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 双VSC经频变分布参数输电线路互联系统 | 在VSC-1公共耦合点(PCC)处提取系统宽频DQ阻抗。HBM算法在15次迭代后达到$10^{-10}$精度收敛，稳态计算结果与OPAL-RT及PSCAD时域仿真完全一致。阻抗扫描覆盖宽频范围，准确捕捉由频变线路分布参数引起的高频谐振峰与相位交叉点。 | 相比传统EMT频域扫描法(FSM)，本方法无需设置极小时步长，计算时间大幅缩短；相比有理逼近法，完全消除拟合残差与高频动态截断误差，阻抗曲线在全频段与商业软件结果重合度极高。 |



## 量化发现

- HBM稳态求解收敛容差严格设定为$10^{-10}$，仅需15次迭代即可实现准线性收敛，计算精度超越传统EMT数值积分方法。
- 阻抗建模过程完全避免有理函数逼近与FFT变换，消除集总参数截断误差与数值积分步长引入的相位漂移，高频段阻抗幅值误差趋近于0。
- 支持任意小频率步长连续扫描，无需离散数据点拟合，完整保留输电线路分布参数引起的宽频谐振特性。
- 基于该解析阻抗模型的奈奎斯特稳定判据分析结果与全阶时域仿真边界高度吻合，有效预测系统谐波失稳临界点。


## 关键公式

### 频变输电线路精确导纳模型

$$$\mathbf{Y}_{tl}(s) = \mathbf{A} - \mathbf{B}(\mathbf{A} + \mathbf{Y}_r)^{-1}\mathbf{B}$$$

*用于在频域直接表征含分布参数与频率相关特性的输电线路，替代传统PI型集总电路或有理逼近模型。*

### Park变换频域频移公式

$$$\mathbf{X}_{DQ}(s) = \mathbf{K}_1 \mathbf{X}_{abc}(s - j\omega_0) + \mathbf{K}_2 \mathbf{X}_{abc}(s + j\omega_0)$$$

*在阻抗扫描阶段，将ABC相坐标系下的频域响应精确映射至DQ旋转坐标系，建立时不变阻抗模型的基础。*

### DQ域宽频导纳矩阵解析识别式

$$$\begin{bmatrix} Y_{g}^{DD} & Y_{g}^{DQ} \\ Y_{g}^{QD} & Y_{g}^{QQ} \end{bmatrix} = \begin{bmatrix} I_0^D & I_{0-}^D \\ I_0^Q & I_{0-}^Q \end{bmatrix} \begin{bmatrix} V_0^D & V_{0-}^D \\ V_0^Q & V_{0-}^Q \end{bmatrix}^{-1}$$$

*通过正负序电压激励下的DQ电流响应直接求解2x2导纳矩阵，实现无需重复时域仿真的阻抗参数提取。*



## 验证详情

- **验证方式**: 离线/实时仿真对比验证与频域扫描交叉校验
- **测试系统**: 双闭环控制电压源变流器(VSC)经两条垂直排列、频变分布参数输电线路互联至等效电网的交流电力系统
- **仿真工具**: OPAL-RT (ARTEMiS/EMTP-RV实时仿真平台), PSCAD/EMTDC (离线电磁暂态仿真), MATLAB/Simulink (算法实现与阻抗计算)
- **验证结果**: 所提时频混合解析法在稳态计算与宽频阻抗识别方面均与OPAL-RT及PSCAD的频域扫描结果高度一致。模型精确保留了输电线路的高频分布参数动态，避免了传统方法的有理拟合误差与数值积分累积误差。基于该阻抗模型的奈奎斯特稳定性分析准确预测了系统谐波稳定边界，验证了方法在电力电子化电网宽频稳定性评估中的高效性与工程适用性。
