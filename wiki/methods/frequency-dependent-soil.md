---
title: "频率相关土壤特性 (Frequency-Dependent Soil Properties)"
type: method
tags: [soil, frequency-dependent, grounding, wideband, lightning, transient]
created: "2026-05-02"
---

# 频率相关土壤特性 (Frequency-Dependent Soil Properties)

## 技术背景

### 发展历史
该技术源于电力系统仿真领域的长期研究积累，随着电力电子设备在电网中的广泛应用而日益重要。

### 研究现状
当前学术界和工业界对该技术的研究主要集中在提升仿真效率、计算效率和模型通用性方面。

### 技术挑战
- 大规模系统的计算复杂度问题
- 多时间尺度混合仿真的协调问题
- 实时仿真的时效性要求
- 模型验证和不确定性量化

## 定义与边界

频率相关土壤特性指土壤电导率、电阻率和介电常数随频率变化，并通过复数介质参数影响大地返回电流、接地阻抗和线路传播特性的建模问题。它是 EMT 中的参数与方法问题，不等同于单一接地电阻测量，也不等同于土壤电离或击穿模型。

本页关注土壤频变参数如何进入 [[earth-return-impedance]]、[[grounding-system-model]]、[[frequency-dependent-line-model]] 和 [[universal-line-model]]。土壤分层、含水率、温度、季节和测量布置都会影响参数可信度，因此不能把一组“典型土壤数值”写成普遍条件。

## EMT 中的作用

在 EMT 中，频率相关土壤特性主要影响：

- 架空线路和地下电缆的大地返回阻抗。
- 接地网、杆塔接地和电极暂态响应。
- 雷电、开关陡波和宽频过电压中的地模传播、衰减和相位。
- 护套、铠装、接地线和土壤之间的耦合。
- 频域参数计算到时域线路模型的转换。

若频段内位移电流项 $\mathrm{j}\omega\varepsilon$ 与传导项 $\sigma$ 不再相对可忽略，则把土壤写成频率无关纯电阻介质可能改变 EMT 结果。

## 核心机制

土壤可用复数电导率表示：

$$\sigma^*(\omega)=\sigma(\omega)+\mathrm{j}\omega\varepsilon(\omega)$$

对应复电阻率可写为：

$$\rho^*(\omega)=\frac{1}{\sigma^*(\omega)}$$

在电磁场方程或线路参数公式中，土壤参数通常通过 $\sigma^*$ 进入大地返回阻抗积分。例如架空线 Carson 类表达式、地下电缆 Pollaczek 类表达式或多层大地格林函数，都需要在每个频点使用一致的土壤参数。

常见经验模型把 $\sigma(\omega)$、$\varepsilon(\omega)$ 或 $\rho^*(\omega)$ 写成少量弛豫项、有理函数或幂律函数。用于 EMT 时，这些频域函数还可能需要通过 [[vector-fitting]] 转成可递推的时域模型。

## 分类与变体

| 类别 | 核心输入 | 适合用途 | 主要边界 |
|------|----------|----------|----------|
| 常数土壤参数 | 单一电阻率或电导率 | 工频接地、低频近似 | 宽频和高阻土壤需复核 |
| 频变均匀土壤 | $\sigma(\omega)$、$\varepsilon(\omega)$ | 架空线/电缆宽频参数 | 不描述地层分层 |
| 分层土壤模型 | 各层厚度和复参数 | 接地网、地下电缆、地质分层 | 参数获取和积分计算复杂 |
| 非线性电离模型 | 电场、临界条件、动态电导 | 雷电大电流接地 | 不属于线性小信号频变模型 |

## 测量与参数识别

土壤参数可来自现场电阻率测试、实验室样品、频域阻抗谱或文献参数。用于 EMT 页面时，应至少说明：

- 测量对象是表观电阻率、复电阻率、接地阻抗还是线路端口响应。
- 频率范围、含水率、温度、样品或现场布置。
- 是否假设均匀半无限土壤、水平分层土壤或局部三维结构。
- 参数是否直接用于线路/接地模型，还是先经过拟合和有理化。

没有这些信息时，只能写“参数不确定性会影响结果”，不应给出固定安全裕度或误差保证。

## 适用边界与失败模式

- 土壤参数空间变化很强，单点测量不一定能代表整条线路走廊或接地网范围。
- 频变线性模型不能覆盖强雷电电流下的土壤电离、热效应和击穿通道，除非模型明确包含这些非线性机制。
- 频域土壤模型如果直接用于时域 EMT，需要检查因果性、稳定性和低频极限。
- 大地返回阻抗计算中的经典公式常依赖均匀或分层介质假设；复杂三维地质结构需要场模型或测量校核。
- 不同论文采用的土壤参数定义、符号和频率单位可能不同，引用公式时应保持单位一致。

## 代表性证据

- [[inclusion-of-frequency-dependent-soil-parameters-in]]：支撑把频变土壤电导率和介电常数纳入线路/电缆建模，并通过扩展 Carson/Pollaczek 类公式影响大地返回阻抗；其数值结论应绑定原文算例。
- [[comparison-of-soil-modeling-concerning-physical-factors-application-to-transient]]：可作为不同土壤物理因素和模型选择影响接地暂态的比较来源。
- [[effect-of-frequency-dependent-soil-parameters-on-wave-propagation-and-transient-]]：适合支撑土壤频变参数会影响波传播和暂态响应的表述。
- [[grounding-grids-in-electro-magnetic-transient-simulations-with-frequency-depende]] 和 [[electromagnetic-transient-modeling-of-grounding-electrodes-buried-in-frequency-d]]：可作为接地系统频变土壤建模入口。

## 与相关页面的关系

- [[frequency-dependent-soil-model]] 更偏向具体模型族和参数表达，本页强调方法边界和 EMT 接口。
- [[earth-return-impedance]] 使用土壤参数计算线路大地返回阻抗。
- [[grounding-system-modeling]] 和 [[grounding-system-model]] 处理接地网与电极的系统模型。
- [[cable-model]]、[[underground-cable-modeling]] 和 [[transmission-line-model]] 是主要应用对象。
- [[grounding-lightning-overvoltage]] 关注频变土壤在雷电过电压问题中的后果。

## 修订与证据使用注意事项

不要添加未来源绑定的土壤电阻率表、介电常数范围、雷电频段或临界电场数值。若确需使用数值，应同时写明来源、测量条件、频率范围和是否代表现场工程参数。
