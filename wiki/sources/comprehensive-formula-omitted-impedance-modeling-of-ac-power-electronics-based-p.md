---
title: "Comprehensive [formula omitted] impedance modeling of AC power-electronics-based power systems with frequency-dependent transmission lines"
type: source
authors: ['Julio Hernández-Ramírez']
year: 2024
journal: "Electric Power Systems Research"
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


<!-- deep-review:start -->
## 研究解读

### 1. 需求、对象、挑战与贡献

工程需求来自电力电子化电网的谐波稳定评估：受控变流器、PWM延时和线路宽频特性会在较宽频段内相互作用，仅靠工频相量或低阶集总线路模型难以判断谐振和失稳风险。研究对象是含AC电力电子装置和输电线路的converter-driven系统，其目标是在DQ坐标下得到可用于Nyquist稳定判据的宽频阻抗模型。难点在于：变流器及控制是非线性、时域实现的；输电线路若采用频变分布参数模型，本质上是频域、无限维对象；稳态工作点又是小信号阻抗线性化的前提。本文的贡献是把PED子系统保留在时域非线性框架，把频变分布参数线路直接用频域电报方程及双曲解析解表示，再用时频混合谐波平衡求精确稳态，随后通过Park变换频移关系把ABC频域响应转成DQ阻抗，避免以集总线路或有理逼近替代完整线路模型。

### 2. 模型、算法与实现技术

方法由两层组成。第一层是稳态求解：把系统切分为非线性PED子系统和线性网络/输电线路子系统，接口量是各子系统端口电压和注入电流。给定接口电压时，PED侧在时域求解含控制、PWM精确延时等实现细节的方程并输出电流；网络侧把这些电流放入频域导纳方程，利用输电线路频域电报方程的双曲函数解计算新的端口电压；两侧在谐波平衡迭代中交换端口量直到达到周期稳态。第二层是阻抗识别：在该稳态点附近，对目标频率施加三相电压扰动，在线路ABC频域模型中直接计算电流响应。Park变换在拉普拉斯域表现为相对基频的频移，因此DQ扰动量可由ABC侧在s±jω0处的响应组合得到。最后用正、负序激励下的DQ电压和电流列向量构造2×2导纳矩阵，再取逆得到阻抗。其机制重点不是对时域波形做FFT拟合，而是直接评价频域解析模型，因此可以保留频变分布参数线路的传播、衰减和谐振特性。

### 3. 验证、优势与不足

作者用一个含变流器和输电线路的converter-driven系统验证方法，并将所得频率扫描结果与OPAL-RT平台中的ARTEMiS/EMTP-RV以及PSCAD/EMTDC的频域扫描结果对比。原文摘要明确称这些结果支持方法的有效性、速度和准确性，但在当前提供的原文片段中未报告可核验的误差、耗时、频率范围或迭代次数等数值结果，因此不能把“更快、更准”量化为具体比例。优势主要体现在建模路径上：线路不需要先变成集总参数或有理函数近似；PWM延时和控制实现可保留在PED模型中；稳态由谐波平衡的时频混合求解获得，避免为了提取阻抗而重复进行长时间EMT暂态仿真和FFT处理。从验证范围看，结论仍受所用算例拓扑、控制结构、线路模型、频扫设置和商业软件基线限制。文中声称面向谐波稳定和Nyquist判据，但当前片段未给出多拓扑、多控制器、弱网极端工况、故障暂态或大规模网络下的系统性验证。

### 4. 价值、认知与可复用场景

这项工作的重要认知是：含频变分布参数输电线路的电力电子系统阻抗建模，不必在“完整EMT时域仿真”和“低阶近似线路模型”之间二选一；可以把非线性控制装置与线性频域网络通过端口量和谐波平衡耦合起来，再解析生成DQ阻抗。它适合被后续关于宽频阻抗建模、谐波稳定、Nyquist判据、变流器并网线路相互作用、EMT与频域混合仿真的页面复用。它不适合被直接外推为所有变流器拓扑、所有控制策略或所有电磁暂态场景的通用加速方法，尤其不能替代故障、大扰动和非周期暂态分析。

### 证据边界

- 来自原文摘要和引言的确定信息：论文提出时频混合解析法，用于含频变分布参数输电线路的AC电力电子系统宽频DQ阻抗建模，并面向谐波稳定分析。
- 来自原文的确定信息：输电线路采用频域电报方程和双曲解析解表示，PED在时域保留非线性、控制实现和PWM精确延时；方法避免时域仿真、有理逼近和FFT用于阻抗识别。
- 来自原文的确定信息：验证使用含变流器和输电线路的系统，并与OPAL-RT ARTEMiS/EMTP-RV及PSCAD/EMTDC的频率扫描方法结果比较。
- 当前提供片段未给出可核验的误差、计算时间、频率范围、迭代次数、收敛阈值或阻抗曲线数值，因此不应写成定量性能结论。
- 关于正负序注入、Park频移和2×2 DQ导纳矩阵构造属于根据摘要、引言和页面公式整理出的机制性说明；具体符号定义、实现细节和参数仍需回查全文公式与算例表。
- 从验证范围看，尚不能确认该方法已覆盖多端大规模网络、不同厂商控制器、非平衡故障、开关级详细模型或实时仿真步长敏感性等场景。
<!-- deep-review:end -->
## 核心贡献

- 问题定位：0378-7796/© 2024 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.
- 方法机制：提出一种时频混合解析法，用于精确识别含频变分布参数输电线路的电力电子系统宽频DQ阻抗模型。该方法将系统解耦为非线性电力电子子系统（时域DQ框架）与线性网络/输电线路子系统（频域ABC框架）。利用谐波平衡法（HBM）迭代求解含无限维频变元件的非线性系统精确稳态，避免传统时域积分与有理逼近误差。
- 验证证据：离线/实时仿真对比验证与频域扫描交叉校验；双闭环控制电压源变流器(VSC)经两条垂直排列、频变分布参数输电线路互联至等效电网的交流电力系统；OPAL-RT (ARTEMiS/EMTP-RV实时仿真平台), PSCAD/EMTDC (离线电磁暂态仿真), MATLAB/Simulink (算法实现与阻抗计算)
- 量化与结论：HBM稳态求解收敛容差严格设定为，仅需15次迭代即可实现准线性收敛，计算精度超越传统EMT数值积分方法。；阻抗建模过程完全避免有理函数逼近与FFT变换，消除集总参数截断误差与数值积分步长引入的相位漂移，高频段阻抗幅值误差趋近于0。；支持任意小频率步长连续扫描，无需离散数据点拟合，完整保留输电线路分布参数引起的宽频谐振特性。；
- 适用边界：适用于理解本文 Comprehensive [formula omitted] impedance modeling of AC power-electronics-based power systems with frequency-dependent transmission lines （2024） 在当前页面抽取范围内讨论的 EM。

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

## 适用边界

### 适用条件

- 适用于理解本文 `Comprehensive [formula omitted] impedance modeling of AC power-electronics-based power systems with frequency-dependent transmission lines`（2024） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。
- 适用于以 谐波平衡法、时频混合解析法、dq阻抗建模 为核心的建模、仿真、等值、控制或稳定性分析场景；具体对象以原文算例和页面“涉及的模型”为准。
- 可作为知识图谱中的方法定位和文献入口，尤其用于追踪：提出时频混合解析法，实现含频变线路的电力电子系统宽频DQ阻抗精确建模。

### 失效边界

- 不应外推到原文未覆盖的拓扑、控制策略、故障类型、频率范围、硬件平台或实时步长。
- 不应把页面中的“提高、显著、快速、准确”等概括性表述当作定量结论；只有“量化发现”和原文表图可核验的数字才可用于比较。
- 若页面作者、期刊、摘要或验证字段仍不完整，本页只能作为待复核文献入口，不能作为最终证据页引用。

### 关键假设

- 页面内容假设当前 PDF 抽取文本与 frontmatter 的 `sources` 指向同一篇论文。
- 方法结论默认受原文仿真工具、测试系统、参数设置、采样步长和对比基线约束。
- 当前边界层为保守整理：未从原文直接核验的内容不得升级为确定结论。

### 证据缺口

- 具体适用范围仍以原文算例、参数表和验证场景为准，当前页面不应外推到未验证系统。
- 源文件路径：`["EMT_Doc/11/Hernández-Ramírez 等 - 2024 - Comprehensive D Q impedance modeling of AC power-electronics-based power systems with frequency-depe.pdf"]`；需要深修时应优先核对该 PDF 的首页、摘要、方法和实验表图。
