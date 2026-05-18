---
title: "阻抗建模 (Impedance Modeling)"
type: method
tags: [impedance-modeling, frequency-domain, stability-analysis, harmonic-analysis, power-electronics]
created: "2026-05-04"
updated: "2026-05-18"
---

# 阻抗建模 (Impedance Modeling)

## 定义与边界

阻抗建模是指建立电力系统元件或子系统在频域中的阻抗-频率特性数学描述的方法。该模型以复数阻抗 $Z(f)$ 或导纳 $Y(f)$ 形式表征系统对外部扰动的动态响应特性。

在EMT仿真和稳定性分析中，阻抗建模主要应用于：
- 电力电子装置（变流器、逆变器）的频域特性分析
- 电网阻抗扫描与谐振评估
- 宽频稳定性分析（次同步振荡、高频谐振）
- 并网设备与电网的交互作用研究

**边界限定**：本方法适用于线性化小信号分析，不适用于大扰动暂态或强非线性工况。

## EMT中的作用

阻抗建模为电力系统宽频动态分析提供了关键工具：

- **稳定性判据**：基于阻抗比的奈奎斯特稳定性判据评估并网稳定性
- **谐振分析**：识别电网与设备间的谐振频率及阻尼特性
- **宽频特性**：覆盖从次同步到开关频率的宽频带特性
- **黑箱建模**：基于测量数据的设备建模，无需内部详细参数

## 主要分支与机制

### 1. 序阻抗建模

基于对称分量法的正序、负序、零序阻抗分别建模：

$$Z_+(f), \quad Z_-(f), \quad Z_0(f)$$

适用于不平衡工况分析和接地故障研究。在序域中，零序阻抗 $Z_0(f)$ 通常受接地变压器和线路布置影响较大，正序阻抗 $Z_+(f)$ 决定同步机或变流器与电网的功率交换能力，负序阻抗 $Z_-(f)$ 在不平衡故障时提供电流通路。

### 2. dq阻抗建模

在同步旋转坐标系下建立dq轴阻抗矩阵：

$$\mathbf{Z}_{dq}(s) = \begin{bmatrix} Z_{dd}(s) & Z_{dq}(s) \\ Z_{qd}(s) & Z_{qq}(s) \end{bmatrix}$$

适用于三相平衡系统的稳定性分析。dq坐标系下，控制环路的积分和比例环节表现为 $1/s$ 和常数增益，导致阻抗矩阵元素在低频段呈现 $-\mathbf{Z}_{dq,12} \neq \mathbf{Z}_{dq,21}$ 的非对称耦合特性。Sun等人(2011)的经典工作建立了这一框架，通过测试电流注入法测量 $Z_{dd}$、$Z_{dq}$、$Z_{qd}$、$Z_{qq}$ 四个元素，支撑了后续并网逆变器的小信号稳定性分析。

### 3. 相阻抗建模

在静止坐标系下建立三相阻抗矩阵：

$$\mathbf{Z}_{abc}(s) = \begin{bmatrix} Z_{aa}(s) & Z_{ab}(s) & Z_{ac}(s) \\ Z_{ba}(s) & Z_{bb}(s) & Z_{bc}(s) \\ Z_{ca}(s) & Z_{cb}(s) & Z_{cc}(s) \end{bmatrix}$$

适用于不平衡系统和高频谐波分析。相域阻抗矩阵的六个独立元素直接反映各相间的耦合程度，当系统对称时非对角元素为零。随频率升高，线路分布参数效应显著，$Z_{aa}$ 等对角元素不再能用集中参数RLC近似。

### 4. 谐波状态空间(HSS)阻抗建模

针对MMC等多端口换流器，考虑谐波耦合效应，在谐波状态空间建立多频阻抗模型：

$$\begin{bmatrix} \Delta i_{acp}(s+j\omega_1) \\ \Delta i_{acn}(s-j\omega_1) \\ \Delta i_{dc}(s) \end{bmatrix} = \mathbf{Y}_C \begin{bmatrix} \Delta v_{acp}(s+j\omega_1) \\ \Delta v_{acn}(s-j\omega_1) \\ \Delta v_{dc}(s) \end{bmatrix}$$

其中正序、负序和直流侧之间存在频率耦合，需通过3×3导纳矩阵描述。这一模型由Xu等人(2025)在多端级联混合HVDC系统中提出，用于分析LCC/MMC混联系统的振荡传播路径。

### 5. 时频混合解析阻抗建模

Hernández-Ramírez等人(2024)提出将系统分为非线性电力电子子系统和线性网络/输电线路子系统，利用谐波平衡法(HBM)迭代求解精确稳态，再通过Park变换的频移特性将ABC域响应转换至DQ域：

$$\mathbf{X}_{DQ}(s) = \mathbf{K}_1 \mathbf{X}_{abc}(s - j\omega_0) + \mathbf{K}_2 \mathbf{X}_{abc}(s + j\omega_0)$$

该方法避免了传统EMT数值积分和有理函数逼近误差，支持任意小频率步长连续扫描。

## EMT建模方法

### 小信号阻抗定义

对于非线性系统在工作点 $(V_0, I_0)$ 附近的小信号分析，阻抗定义为：

$$Z(s) = \frac{\Delta V(s)}{\Delta I(s)}$$

在频域中：

$$Z(f) = R(f) + jX(f) = |Z(f)|e^{j\varphi(f)}$$

其中 $R(f)$ 为电阻分量，$X(f)$ 为电抗分量，$|Z(f)|$ 为阻抗幅值，$\varphi(f)$ 为阻抗相位。

### 阻抗比稳定性判据

对于并网系统，源侧阻抗 $Z_s$ 与负载/设备阻抗 $Z_l$ 的稳定性判据基于阻抗比：

$$T_m(s) = \frac{Z_s(s)}{Z_l(s)}$$

系统稳定的充分条件（Middlebrook判据）：

$$|T_m(j\omega)| < 1, \quad \forall \omega$$

或更宽松的Gain Margin-Phase Margin判据。实际应用中，当 $|T_m(j\omega)|$ 在相位穿越 $-180°$ 时幅值仍小于1，系统具有正增益裕度。

### MIMO阻抗与广义奈奎斯特判据

对于三相系统，MIMO阻抗矩阵与电压-电流关系：

$$\begin{bmatrix} \Delta V_d \\ \Delta V_q \end{bmatrix} = \begin{bmatrix} Z_{dd} & Z_{dq} \\ Z_{qd} & Z_{qq} \end{bmatrix} \begin{bmatrix} \Delta I_d \\ \Delta I_q \end{bmatrix}$$

广义奈奎斯特稳定性判据基于回比矩阵的特征值：

$$\det(\mathbf{I} + \mathbf{L}(s)) = 0$$

其中 $\mathbf{L}(s) = \mathbf{Z}_{load}(s)\mathbf{Y}_{source}(s)$。若 $\mathbf{L}(s)$ 的特征轨迹不包围 $(-1, j0)$ 点，系统稳定。

### 动态频率扫描法

Jiang等人(2025)提出基于EMT的自动化动态频率扫描工具，核心步骤：

1. 在PCC注入幅值为额定值0.5%的多频正弦扰动信号
2. 采集三相电压与电流时域波形，通过DFT提取各频率点的幅值与相位
3. 在dq坐标系下构建阻抗矩阵 $\mathbf{Z}_{MMC} = \mathbf{V}_{PCC} \cdot \mathbf{I}_{MMC}^{-1}$
4. 计算开环增益矩阵 $\mathbf{Z}_{MMC} \mathbf{Y}_{ac}$ 的特征值，绘制伯德图
5. 根据相位 $180°$ 穿越点的幅值推算临界短路比 $CSCR = SCR_{initial}/|\lambda|_{180°}$

### 离散阻抗建模(DIBM)接口

Vahabzadeh等人(2025)提出为基于状态变量(SV)的实时EMT仿真器设计离散阻抗接口方法。将VSC含滤波器与控制系统的传递函数矩阵经梯形积分离散化后，转换为诺顿导纳形式再转为戴维南等效：

$$i_{VSC,dq}(t) = \mathbf{G}_{dq} v_{PCC,dq}(t) + \mathbf{h}_{dq}(t)$$

$$\mathbf{Z}_{abc} = \mathbf{G}_{abc}^{-1}, \quad e_{abc}(t) = -\mathbf{G}_{abc}^{-1} \mathbf{h}_{abc}(t)$$

量化结果：状态变量数从271降至43（减少84.1%），最大步长从80µs扩大至1ms，实时计算性能提升最高4倍。

## 关键技术挑战

### 1. 频率耦合效应

dq坐标系下正负序频率耦合导致阻抗矩阵非对称。电力电子变流器的PWM调制、控制环路积分环节与电网阻抗相互作用，在宽频频段内产生复杂的耦合模式。多端口换流器（如MMC）还需考虑内部谐波（子模块电容电压纹波、环流动态）与交流端口阻抗的耦合。

### 2. 时变特性处理

开关频率变化、控制模式切换导致阻抗在工作点附近呈现时变特性。传统小信号线性化模型只在单一工作点有效，参数漂移或工况变化后阻抗模型需要重新辨识。PR控制、滑模控制等非线性控制器使得阻抗建模不能简单套用PI控制的dq分解框架。

### 3. 测量带宽与注入扰动设计

基于扫频测量的阻抗辨识受注入信号幅值（信噪比vs线性度权衡）和频率点数限制。PRBS伪随机二进制序列可在宽频频段内同时注入多频率扰动，但工程实践中扰动设计（幅值、序列长度、注入位置）缺乏统一规范，导致测量结果重复性差。

### 4. 大规模系统阻抗聚合

多换流器并联或串接形成复杂网络，单机阻抗模型无法直接描述系统级交互。需通过MIMO端口阻抗聚合或戴维南等效将系统等价为可分析的简化结构，但聚合过程可能丢失重要高频动态或耦合模态。

### 5. 右半平面极点与接口稳定性

定直流电压控制模式的换流器端口导纳矩阵可能包含右半平面(RHP)极点，直接使用其导纳元素会导致稳定性判据误判。Xu等人(2025)通过矩阵代数变换将直流电流作为输入、直流电压作为输出，形成阻抗/导纳混合接口以规避RHP极点影响。

## 量化性能边界

### 测试系统与精度数据

| 参数 | 数值 | 来源 |
|------|------|------|
| 电压源型VSG临界短路比(CSCR) | 3.7 | Jiang 2025 |
| VSG失稳振荡频率 | 1.15 Hz | Jiang 2025 |
| CSCR推算误差 | <2.7% | Jiang 2025 |
| DIBM状态变量削减 | 271→43（降84.1%） | Vahabzadeh 2025 |
| DIBM最大步长扩展 | 80µs→1ms（扩12.5倍） | Vahabzadeh 2025 |
| DIBM波形误差（200µs步长） | <0.5% | Vahabzadeh 2025 |
| DIBM实时性能提升 | 最高4倍 | Vahabzadeh 2025 |
| HBM稳态收敛容差 | 10⁻¹⁰，15次迭代 | Hernández-Ramírez 2024 |
| MMC阻抗矩阵维度 | 3×3（正序/负序/直流） | Xu 2025 |

### 方法对比表

| 阻抗类型 | 适用场景 | 关键特征 | 代表文献 |
|---------|---------|---------|---------|
| 序阻抗 | 不平衡故障分析 | 正/负/零序解耦 | 经典 |
| dq阻抗 | 并网变流器稳定性 | 旋转坐标系耦合 | Sun 2011 |
| 相阻抗 | 高频谐波/不平衡 | 三相耦合矩阵 | Cespedes 2014 |
| HSS阻抗 | MMC多端口系统 | 谐波状态空间 | Xu 2025 |
| 时频混合 | 含频变线路系统 | 谐波平衡+解析 | Hernández-Ramírez 2024 |
| DIBM | 实时EMT接口 | 离散阻抗等效 | Vahabzadeh 2025 |

## 适用边界与选择指南

### 适用条件

| 应用场景 | 适用性 | 说明 |
|---------|-------|------|
| 线性小信号分析 | ★★★★★ | 基于工作点线性化 |
| 宽频稳定性 | ★★★★★ | 覆盖次同步到高频 |
| 谐振分析 | ★★★★★ | 识别谐振频率和阻尼 |
| 大扰动暂态 | ★☆☆☆☆ | 需分段线性化 |
| 非线性谐波 | ★★☆☆☆ | 需迭代谐波分析 |

### 失效边界

- **大扰动工况**：阻抗模型基于小信号线性化，大扰动后工作点改变需重新建模
- **饱和非线性**：变压器、电抗器饱和时阻抗特性高度非线性
- **时变特性**：开关频率变化、控制模式切换导致时变阻抗
- **测量带宽**：基于测量的阻抗模型受限于测试设备带宽

## 相关方法与模型

- [[small-signal-analysis]] - 小信号分析基础
- [[small-signal-stability]] - 小信号稳定性
- [[harmonic-analysis-methods]] - 谐波阻抗分析
- [[frequency-domain-analysis]] - 频域分析方法
- [[vector-fitting]] - 阻抗频变特性的有理近似
- [[frequency-dependent-modeling]] - 频变建模综述
- [[gfl-inverter-model]] - 跟网型逆变器阻抗模型
- [[gfm-inverter-model]] - 构网型逆变器阻抗模型
- [[mmc-model]] - 模块化多电平换流器阻抗
- [[lcc-model]] - 线换相换流器阻抗

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。如有更新或修正，请参考最新研究进展。*

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| Sun, J., "Impedance-Based Stability Criterion for Grid-Connected Inverters" | 2011 | 建立并网逆变器阻抗-稳定性判据框架 |
| Middlebrook, R.D., "Input Filter Considerations..." | 1976 | 提出阻抗比稳定性判据 |
| Cespedes, M. and Sun, J., "Impedance Modeling of Voltage Source Converters" | 2014 | 三相变流器dq阻抗建模 |
| Hernández-Ramírez 等, "Comprehensive DQ impedance modeling..." | 2024 | 时频混合解析法，含频变分布参数线路 |
| Jiang, C., "An EMT based dynamic frequency scanning tool..." | 2025 | PSCAD集成自动化动态频率扫描，CSCR预测 |
| Xu 等, "Impedance Based Stability Analysis of Multi-terminal Cascaded Hybrid HVDC" | 2025 | MIMO阻抗建模，振荡传播路径分析 |
| Chindu & Kulkarni, "An Automatable Approach for Small-Signal Stability Analysis Using EMT Companion Circuits" | 2023 | EMT伴随电路LTI采样数据模型 |
| Vahabzadeh 等, "Discretized Impedance-Based Modeling for SV Real-Time EMT Simulators" | 2025 | 离散阻抗接口，DIBM状态削减 |