---
title: "频变土壤模型 (Frequency-Dependent Soil Model)"
type: method
tags: [soil, grounding, frequency-dependent, resistivity, corrosion, polarization, alipio-visacro]
created: "2026-05-02"
---

# 频变土壤模型 (Frequency-Dependent Soil Model)


```mermaid
graph TD
    subgraph Ncmp[频变土壤模型 (Frequency-Dependent …]
        N0[常数土壤模型: 单一 $\rho$ 或 $\sigma$]
        N1[幂律/一阶经验模型: $\sigma(\omega)$ …]
        N2[弛豫模型: $\varepsilon^*(\omega)…]
        N3[分层土壤模型: 各层厚度和复参数]
        N4[有理函数模型: 频域响应的时域实现]
    end
```


## 定义与边界

频变土壤模型是把土壤电导率、电阻率或介电常数写成频率相关函数，并将其作为线路大地返回、接地电极或电缆外部介质参数输入 EMT 的模型族。它更偏向“具体参数表达和实现形式”；频变土壤在 EMT 中的总边界已由保护页 [[frequency-dependent-soil]] 说明。

本页不处理土壤电离、击穿、热效应或接地网几何建模本身。若模型没有显式非线性机制，不能把它用于强雷电电流下的土壤电离结论。

## EMT 中的作用

频变土壤模型通常向下游模型提供：

- 复电导率 $\sigma^*(\omega)$ 或复电阻率 $\rho^*(\omega)$。
- 大地返回阻抗计算所需的复穿透深度或复介质参数。
- 接地电极、杆塔接地、电缆护套和线路地模传播的频域参数。
- 若进入时域 EMT，则提供有理函数、状态空间或递归卷积表示。

它的可信度取决于测量条件、拟合模型、频率范围、土壤空间均匀性和低频/高频极限是否合理。

## 核心数学表达

常用入口是复电导率：

$$\sigma^*(\omega)=\sigma(\omega)+j\omega\varepsilon(\omega)$$

复电阻率为：

$$\rho^*(\omega)=\frac{1}{\sigma^*(\omega)}$$

在复返回平面或 Carson/Pollaczek 类地回路计算中，土壤参数会进入类似复穿透深度的表达：

$$p(\omega)=\frac{1}{\sqrt{j\omega\mu\left[\sigma(\omega)+j\omega\varepsilon(\omega)\right]}}$$

若要在时域中使用频变函数，常将频域响应拟合成有理函数：

$$F(s)\approx D+sE+\sum_{r=1}^{N}\frac{R_r}{s-p_r}$$

随后每个极点-留数项离散为状态变量或递归卷积项。此步骤需要检查稳定极点、因果性和 [[passivity-enforcement]]。

## 模型类型

| 类型 | 表达对象 | 适合用途 | 主要边界 |
|------|----------|----------|----------|
| 常数土壤模型 | 单一 $\rho$ 或 $\sigma$ | 工频近似、初步参数扫描 | 宽频暂态可能不足 |
| 幂律/一阶经验模型 | $\sigma(\omega)$ 或 $\rho(\omega)$ | 少参数拟合和线路参数扫描 | 参数需由测量或来源约束 |
| 弛豫模型 | $\varepsilon^*(\omega)$ 或 $\rho^*(\omega)$ | 介质频散、宽频拟合 | 多参数可辨识性需检查 |
| 分层土壤模型 | 各层厚度和复参数 | 接地网、地下电缆、地质分层 | 反演和积分计算复杂 |
| 有理函数模型 | 频域响应的时域实现 | EMT 状态空间/卷积接口 | 需稳定性和无源性验证 |

## 建模流程

1. 明确模型用途：线路地回路、接地网、电缆外部介质还是参数敏感性。
2. 选择参数来源：现场测量、实验室样品、文献参数或工程假设。
3. 记录频率范围、含水率、温度、样品/现场布置和土壤均匀性假设。
4. 将 $\sigma(\omega)$、$\varepsilon(\omega)$ 或 $\rho^*(\omega)$ 输入 [[earth-return-impedance]]、[[grounding-system-modeling]] 或 [[frequency-dependent-line-model]]。
5. 若需要时域 EMT，使用 [[vector-fitting]] 或状态空间实现，并检查低频极限、稳定性和拟合误差。
6. 用目标暂态的敏感频段复核常数土壤模型与频变土壤模型的差异。

## 适用边界与失败模式

- 不能把单一样品或单一地点参数写成通用土壤参数库。
- 频变线性模型不能覆盖土壤电离、击穿通道和热失稳，除非来源明确建模。
- 土壤分层和空间变化可能比频率依赖本身更影响某些接地问题。
- 频域模型直接转时域时，若未检查因果性和稳定性，可能引入非物理增长。
- 文献中的频带、湿度、温度和土样条件必须随数值一起引用；本页不保留无来源典型值。

## 代表性证据

- [[inclusion-of-frequency-dependent-soil-parameters-in]]：支撑将频变土壤电导率和介电常数纳入架空线 Carson 类公式与电缆 Pollaczek 类公式，并用频域相域模型分析暂态响应；source 的 deep-review 提醒部分量化数字未被当前摘录支持。
- [[influence-of-frequency-characteristics-of-soil-on-lightning-transient-response-o]]：支撑实测土壤频变参数进入复返回平面法并影响架空线路地回路参数；证据边界主要是线路参数计算，不是完整接地网冲击实测。
- [[comparison-of-soil-modeling-concerning-physical-factors-application-to-transient]]：可作为不同土壤物理因素影响暂态计算的比较入口。
- [[effect-of-frequency-dependent-soil-parameters-on-wave-propagation-and-transient-]]：可作为土壤频变参数影响波传播和暂态响应的来源入口。

## 与相关页面的关系

- [[frequency-dependent-soil]]：保护页，说明频变土壤特性的总边界和 EMT 接口。
- [[earth-return-impedance]]：使用土壤参数计算线路大地返回阻抗。
- [[grounding-system-modeling]] 和 [[grounding-system]]：接地系统对象与工程问题。
- [[transmission-line-model]]、[[frequency-dependent-line-model]]、[[universal-line-model]]：土壤参数进入线路模型的下游位置。
- [[underground-cable-modeling]] 和 [[cable-model]]：电缆外部介质和护套接地应用。

## 修订与证据使用注意事项

后续补充模型名、公式或参数时，应写明来源、变量定义、单位、频率范围、测量条件和是否已经用于时域 EMT。不要把“频变土壤模型提高精度”写成无条件结论；应说明相对于什么常数模型、在哪个算例、哪个指标上变化。
