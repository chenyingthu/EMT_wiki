---
title: "直流侧RLC滤波器 (DC-Side RLC Filter)"
type: model
tags: [dc-filter, rlc, converter, ripple, power-electronics, emi-filter, passive-filter]
created: "2026-05-02"
updated: "2026-05-12"
updated: "2026-05-11"
---

# 直流侧RLC滤波器 (DC-Side RLC Filter)


## 定义与边界

直流侧 RLC 滤波器（DC-Side RLC Filter）是在变流器、直流母线、储能或直流网络端口附近布置的无源滤波与阻尼网络。物理对象是电感、电容、电阻、连接母排、接地/屏蔽路径和器件寄生参数；EMT 等效对象是由 R、L、C 支路、状态变量、伴随导纳和历史源组成的端口网络。

本页聚焦 EMT 模型，不把 RLC 参数选择写成通用设计规范。纹波限值、阻尼比、开关频率比例、EMI 标准和元件额定值必须绑定设备、标准或论文算例；否则只应作为设计变量或验证项目出现。

## EMT 建模对象

线性 RLC 滤波器的基本状态通常是电感电流和电容电压。以串联 $R$-$L$ 后接并联 $C$ 的低通结构为例，可选：

$$\mathbf{x}=\begin{bmatrix} i_L & v_C \end{bmatrix}^{T},\qquad
\dot{\mathbf{x}}=
\begin{bmatrix}
-R/L & -1/L \\
1/C & -1/(R_d C)
\end{bmatrix}\mathbf{x}
+\mathbf{B}u,$$

其中 $R_d$ 表示可选阻尼路径，$\mathbf{B}$ 取决于端口定义。进入 EMT 节点法后，每个电感和电容通常通过 [[companion-model|伴随模型]] 转换成当前等效导纳和历史源。

滤波器不是孤立二阶系统。它的有效阻尼和谐振频率还受源阻抗、负载阻抗、换流器控制、采样延迟、电缆电容和外部网络影响。因此，单独 RLC 公式只能支撑局部模型定义，不能直接证明系统级稳定。

## 模型结构与接口变量

| 变量类别 | 典型内容 | EMT 作用 |
|----------|----------|----------|
| 端口变量 | 直流母线电压、滤波器电流、负载/源端电流 | 接入换流器和直流网络 |
| 状态变量 | 电感电流 $i_L$、电容电压 $v_C$、阻尼支路状态 | 描述储能和瞬态响应 |
| 代数变量 | 当前等效导纳、节点注入电流、约束电压 | 进入节点导纳矩阵 |
| 控制接口 | 直流电压控制、电流限幅、调制或保护状态 | 改变激励和等效阻抗 |
| 寄生变量 | ESR、ESL、绕组电阻、寄生电容、母排电感 | 影响高频谐振和 EMI |

基础谐振关系可写为：

$$\omega_0=\frac{1}{\sqrt{LC}},\qquad
\zeta=\frac{R}{2}\sqrt{\frac{C}{L}},$$

但这些式子只对应特定二阶拓扑和阻尼位置。若滤波器是 CLC、阻尼支路、共模/差模组合或与电缆耦合，应重新写出端口阻抗或状态方程。

## 建模层级

| 层级 | 保留内容 | 适合用途 | 边界 |
|------|----------|----------|------|
| 理想 RLC | 标称 R、L、C 和二阶动态 | 控制调试、低频纹波、局部谐振 | 不描述损耗、温度和高频寄生 |
| 含 ESR/ESL 模型 | 元件串联电阻、电感和阻尼支路 | 实际阻尼、损耗和中频谐振 | 参数需由器件或测量支撑 |
| 频率相关阻抗 | 电感绕组损耗、电容介质损耗、母排寄生 | EMI、传导干扰、宽频稳定 | 需要频响或结构参数 |
| 与控制耦合模型 | 变流器控制、采样、限幅和保护 | 直流母线稳定、故障恢复 | 控制模型边界必须明示 |
| 多端口直流网络模型 | 多换流器、电缆、储能和接地耦合 | VSC-HVDC、MTDC、直流配电 | 不能用单个二阶滤波器外推 |

## 量化性能边界

RLC 滤波器模型在 EMT 仿真中已有可核验的量化结果，但以下数据均绑定特定积分方法和电路条件，不能外推为通用能力：

- **Carbonea/Dommel (2002)** 针对 EMTP 中梯形积分法在谐振电路仿真中的截断误差进行了系统分析。在谐振点附近，梯形积分导致的等效阻抗误差可达约 **100%**，远超单一电感或电容元件独立误差。典型仿真步长（50 μs）下，频率超过 **5000 Hz** 时数值截断误差显著增大且不可忽略。串联谐振电路的最大误差始终紧邻谐振频率，而并联谐振电路的最大误差出现在谐振频率前约 **10%** 处。误差幅值随品质因数 Q 呈近似线性增长，随谐振频率呈近似平方律增长。该结论基于简单串/并联 RLC 及含变压器换流器的工业配电系统的解析与数值分析，限于梯形积分法和 EMTP 类程序 (Carbonea/Dommel 2002)。

这些量化数据不构成对 RLC 滤波器建模方法的全面性能评价，只说明在特定测试条件下可获得的能力边界。

## 适用边界与失败模式

- 低通传递函数只在端口定义和负载假设明确时成立；源/负载阻抗变化会移动阻尼和谐振。
- 忽略电容 ESR/ESL 与电感寄生电容时，高频振荡和 EMI 结果可能失真。
- 过小阻尼会放大开关谐波或控制扰动；过大阻尼会引入损耗和热边界，需要单独验证。
- 直流故障、闭锁和保护动作会改变等效拓扑；滤波器初始能量和历史项需重新检查。
- 纹波百分比、THD、插入损耗或标准合规结论必须绑定测试系统、频段、测量点和标准版本。
- 与 [[average-value-model|平均值模型]] 连接时，开关纹波可能被模型本身消除；此时不能用该结果评价高频滤波效果。

## 验证需求

RLC 滤波器模型至少应验证：

1. 元件参数：R、L、C、ESR、ESL、阻尼支路和温度依赖是否有来源。
2. 频域响应：端口阻抗、传递函数或插入损耗是否在目标频段匹配测量、解析或详细模型。
3. 时域响应：直流母线阶跃、负载突变、开关纹波、故障恢复和控制动作是否在同一工况下比较。
4. 数值实现：[[trapezoidal-rule|梯形法]]、[[backward-euler|后向欧拉]] 或其他积分方式是否造成数值振荡或过度阻尼。

若研究目标是电磁兼容，应明确共模/差模路径、接地电容、安全限制和测量端口；普通直流低通模型不足以替代 [[emi-filter-model|EMI 滤波器]]。

## 开放问题

- 梯形积分法在 RLC 谐振电路中截断误差的解析结论（Carbonea/Dommel 2002）基于特定电路拓扑，在多谐振、高 Q 值和混合阻尼条件下的误差叠加机理缺乏系统推广。
- 直流 RLC 滤波器与换流器控制耦合后的等效阻抗建模中，梯形积分截断误差与控制延迟的交互效应尚未被现行 RLC 滤波器模型框架覆盖。
- RLC 滤波器在直流故障暂态过程中的非线性行为（饱和电感、压敏电阻、熔断器）在 EMT 模型中的等效处理缺乏标准化验证流程。
- 当换流器开关频率持续升高（SiC/GaN 数百 kHz），RLC 滤波器的寄生参数（ESR/ESL/寄生电容）建模误差对 EMI 和共模干扰仿真的影响缺乏系统评估。
- 多换流器直流网络中，各端口 RLC 滤波器之间的谐振耦合和阻尼互作用缺乏统一的降阶建模准则。

## 代表性来源

| 来源 | 可支撑内容 | 证据边界 |
|------|------------|----------|
| [[analysis-and-estimation-of-truncation-errors-in-modeling-complex-resonant-circui-fix]] | RLC 谐振电路中数值截断误差和步长敏感性 | 量化结论限于原文 RLC 和工业算例 |
| [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient]] | RLC/开关电路用状态空间-节点法接入 EMT 的机制 | 实时性能和误差需限于原文测试 |
| [[analytical-and-measurement-based-wideband-two-port-modeling-of-dc-dc-converters-]] | DC-DC 端口宽频建模与滤波接口入口 | 不等同于所有直流滤波器通用参数 |
| [[development-of-high-frequency-supraharmonic-models-of-small-scale-amplt5kw-singl]] | 高频/超谐波模型和小功率变换器频段边界 | 结论需绑定原文设备功率和频带 |
| [[active-damping-control-and-parameter-calculation-for-resonance-suppression-in-dc-distribution]] | 直流配电谐振抑制和有源阻尼入口 | 控制效果依赖原文拓扑和参数 |

## 与相关页面的关系

- [[inductor-model]]、[[capacitor-model]] 和 [[resistor-model]] 是 RLC 元件级模型基础。
- [[companion-model]]、[[companion-circuit]] 和 [[nodal-admittance-matrix]] 说明离散后如何接入 EMT 求解。
- [[dc-dc-converter]]、[[vsc-model]]、[[energy-storage-converter-model]] 和 [[vsc-hvdc]] 是常见应用对象。
- [[harmonic-analysis]]、[[harmonic-analysis-methods]] 和 [[frequency-domain-analysis]] 支撑频域响应与谐振分析。
- [[emi-filter-model]] 处理更完整的传导干扰、共模/差模和标准测量边界。
---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[comparison-between-electromechanical-transient-model-and-electromagnetic-transie|Comparison between electromechanical transient model and ele]] | 2013 |
| [[dynamic-average-value-modeling-of-13&14|Dynamic Average-Value Modeling of]] | 2014 |
| [[average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail|Average-Value Modeling of Line-Commutated Inverter Systems W]] | 2022 |
| [[electromechanical-electromagnetic-transient-hybrid-simulation-of-an-acdc-hybrid-|Electromechanical-electromagnetic transient hybrid simulatio]] | 2022 |
| [[analysis-on-dynamic-characteristic-of-control-mode-for-800-kv-yun-guang-uhvdc|Analysis on dynamic characteristic of control mode for +/-80]] | 2025 |
| [[impedance-based-stability-analysis-of-the-multi-terminal-cascaded-hybrid-hvdc-sy|Impedance Based Stability Analysis of the Multi-terminal Cas]] | 2025 |
