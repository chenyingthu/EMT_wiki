---
title: "频变线路模型 (Frequency-Dependent Line Model)"
type: model
tags: [frequency-dependent, transmission-line, cable, wideband, transient]
created: "2026-05-02"
---

# 频变线路模型 (Frequency-Dependent Line Model)


```mermaid
graph TD
    subgraph Ncmp[频变线路模型 (Frequency-Dependent …]
        N0[物理参数: 导体半径、位置、护套、接地、电阻率、介电常数…]
        N1[端口变量: 两端相电压、导体电流、护套/地线端口电压电流]
        N2[内部状态: 极点-留数递推状态、延时队列、历史电流源]
        N3[代数变量: 当前步端口导纳矩阵、端口注入电流]
        N4[验证变量: 频域拟合误差、时域波形、能量或无源性检查结果]
    end
```


## 定义与边界

频变线路模型（Frequency-Dependent Line Model）是把架空线、电缆或混合线路的单位长度参数表示为频率相关矩阵，并在 EMT 时域仿真中重构其传播、衰减和端口耦合的模型。它的物理对象是实际线路、电缆、护套、地线、接地返回路径和周围介质；EMT 等效对象通常是端口导纳、传播延时、递归卷积历史项和内部拟合状态。

本页讨论模型结构和接口边界，不把“频变”写成自动高精度。模型可信度取决于线路几何、导体与土壤参数、频率采样范围、有理拟合质量、延时提取、无源性和时域实现。未绑定来源的误差百分比、极点数量、频带上限或软件能力不应作为通用结论。

## EMT 建模对象

频变线路的连续频域对象通常包括单位长度串联阻抗矩阵 $\mathbf{Z}(\omega)$ 和并联导纳矩阵 $\mathbf{Y}(\omega)$：

$$-\frac{d\mathbf{v}}{dx}=\mathbf{Z}(\omega)\mathbf{i},\qquad
-\frac{d\mathbf{i}}{dx}=\mathbf{Y}(\omega)\mathbf{v}.$$

其中 $\mathbf{v}$ 和 $\mathbf{i}$ 是相域或导体域电压、电流向量。$\mathbf{Z}(\omega)$ 可包含导体内阻抗、集肤效应、邻近效应、护套/地线耦合和 [[earth-return-impedance|大地返回阻抗]]；$\mathbf{Y}(\omega)$ 可包含电容、电导、介质损耗和接地相关导纳。多导体耦合由矩阵非对角项体现，不能在未验证的情况下拆成多个独立单相模型。

频域对象进入 EMT 后一般转换为端口关系：

$$\mathbf{i}_{n+1}=\mathbf{G}_{eq}\mathbf{v}_{n+1}+\mathbf{i}_{hist,n},$$

其中 $\mathbf{G}_{eq}$ 是当前步端口等效导纳，$\mathbf{i}_{hist,n}$ 汇集传播延时、卷积状态和上一时间步历史量。该形式与 [[companion-model|伴随模型]]、[[nodal-admittance-matrix|节点导纳矩阵]] 和 [[thevenin-norton-equivalent|戴维南-诺顿等效]] 的接口一致。

## 模型结构与接口变量

频变线路模型至少应说明以下变量：

| 变量类别 | 典型内容 | 说明 |
|----------|----------|------|
| 物理参数 | 导体半径、位置、护套、接地、电阻率、介电常数、土壤模型 | 决定 $\mathbf{Z}(\omega)$ 和 $\mathbf{Y}(\omega)$ 的输入边界 |
| 端口变量 | 两端相电压、导体电流、护套/地线端口电压电流 | 决定如何接入外部 EMT 网络 |
| 内部状态 | 极点-留数递推状态、延时队列、历史电流源 | 决定时域记忆和数值稳定性 |
| 代数变量 | 当前步端口导纳矩阵、端口注入电流 | 进入全局节点方程 |
| 验证变量 | 频域拟合误差、时域波形、能量或无源性检查结果 | 用于约束模型可信范围 |

常见实现会从传播常数和特性导纳构造端口函数。单相或模态通道中可写为：

$$H(s)=e^{-\gamma(s)\ell}=e^{-s\tau}H_r(s),\qquad
H_r(s)\approx D+\sum_{k=1}^{N}\frac{R_k}{s-p_k}.$$

$\ell$ 是线路长度，$\tau$ 是提取出的传播延时，$p_k$ 和 $R_k$ 是有理逼近的极点和留数。每个极点项离散后成为历史状态。若 $p_k$、$R_k$ 或常数项破坏稳定性、实系数一致性或无源性，时域仿真可能产生非物理增长。

## 建模层级

| 层级 | EMT 等效 | 适合用途 | 主要边界 |
|------|----------|----------|----------|
| 常参数行波模型 | 固定特性阻抗和传播延时 | 工频和低频暂态的基准对照 | 高频损耗、地回路和耦合频变不足 |
| 模态频变模型 | 模态变换后每个模态递归卷积 | 完全换位或近似对称线路 | 模态矩阵频率相关时需复核 |
| 相域频变模型 | 直接拟合相域矩阵函数 | 非换位线路、电缆、多导体耦合 | 矩阵拟合、延时和无源性更复杂 |
| [[universal-line-model|ULM]] | 相域特性导纳和传播函数的有理时域实现 | 宽频线路和电缆研究 | “Universal” 是模型名，不表示全条件适用 |
| [[folded-line-equivalent|FLE]] 或端口等值 | 分块导纳、开路/短路响应或端口函数 | 短线路、接口和实时实现研究 | 依赖分解方式、拟合和接口验证 |

模型选择应绑定研究目标。雷电、开关暂态、护套耦合和宽频振荡通常需要比常参数模型更细的频率相关描述；若只研究低频功率交换，过高阶频变模型可能增加计算负担和参数不确定性。

## 适用边界与失败模式

- 频率扫描范围不足会遗漏目标暂态的主要频谱；范围过宽但采样稀疏也可能造成拟合失真。
- 土壤电阻率、频变土壤、护套接地和交叉互联参数不确定时，模型结构本身不能保证物理准确。
- 固定模态变换适合特定对称条件；非换位、多回线或电缆系统中应检查相域耦合和频率相关特征向量。
- 有理函数拟合若未检查 [[passivity-enforcement|无源性强制]]，接入外部网络后可能出现非物理振荡。
- 延时提取、插值和时间步长会影响波头、反射和高频衰减；只报告频域幅值误差不足以证明时域可信。
- 用单篇论文或单一软件算例给出的误差、极点数或运行时间，只能支撑该算例，不应写成通用选型规则。

## 验证需求

频变线路页面和模型报告至少应区分三类验证：

1. 频域验证：$\mathbf{Z}(\omega)$、$\mathbf{Y}(\omega)$、特性导纳、传播函数、低频极限和高频渐近是否与参数计算或测量一致。
2. 时域验证：阶跃、合闸、雷电波、故障或谐波注入波形是否与解析模型、详细模型、软件基准或试验记录一致。
3. 互联验证：与变压器、换流器、接地系统或外部网络连接后是否保持能量一致、数值稳定和端口方向正确。

若涉及实时仿真，还需报告目标硬件、步长、计算裕度、延时队列实现和模型阶数；不能仅以“递归卷积较快”推断实时可用。

## 代表性来源

| 来源 | 可支撑内容 | 证据边界 |
|------|------------|----------|
| [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del]] | [[vector-fitting|矢量拟合]]把频域响应转成有理函数的基础方法 | 不自动保证无源性或线路参数正确 |
| [[passivity-enforcement-for-transmission-line-models]] | ULM/线路模型中的带外无源性违规和修正思路 | 量化结果限于原文线路模型和测试条件 |
| [[implementation-of-modal-domain-transmission-line-models-in-the-atp-software]] | 用理想变压器阵列表达 Clarke 模态变换并接入线路模型 | 严格适用于原文完全换位线路和 ATP 实现 |
| [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga-]] | 相域频变线路模型进入 FPGA 实时 EMT 的研究入口 | 步长、资源和精度结论需绑定原文平台 |
| [[a-full-frequency-dependent-line-model-based-on-folded-line-equivalencing-and-lat]] | FLE 频变线路路线的代表入口 | 不替代 ULM 或 JMarti 的一般结论 |

## 与相关页面的关系

- [[transmission-line-model]] 是线路模型总览，本页聚焦频率相关 EMT 等效。
- [[distributed-parameter-line]] 和 [[transmission-line-theory]] 给出线路方程基础。
- [[earth-return-impedance]]、[[frequency-dependent-soil]] 和 [[mutual-impedance]] 决定输入参数的物理边界。
- [[universal-line-model]]、[[bergeron-line-model]]、[[modal-transformation]] 和 [[modal-domain-decoupling]] 是相邻实现路线。
- [[wideband-modeling]]、[[vector-fitting]]、[[partial-fraction-expansion]] 和 [[passivity-enforcement]] 处理频域响应到稳定时域模型的共性问题。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[38tpwrd20182794887|Time-Window Based Discrete-Time Fourier Series for Electroma]] | 2018 |
| [[a-modified-implementation-of-the-folded-line-equivalent-transmission-line-model-|A modified implementation of the Folded Line Equivalent tran]] | 2022 |
| [[implementation-of-modal-domain-transmission-line-models-in-the-atp-software|Implementation of Modal Domain Transmission Line Models in t]] | 2022 |
| [[implementation-of-modal-domain-transmission-line-models-in-the-atp-software|Implementation of Modal Domain Transmission Line Models in t]] | 2022 |
