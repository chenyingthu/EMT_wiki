---
title: "雷电暂态分析 (Lightning Transient Analysis)"
type: method
tags: [lightning, transient, overvoltage, surge, protection, emtp, transmission-line, insulation]
created: "2026-05-02"
updated: "2026-05-03"
---

# 雷电暂态分析 (Lightning Transient Analysis)


```mermaid
graph TD
    subgraph Ncmp[雷电暂态分析 (Lightning Transient …]
        N0[直击雷: 注入电流、击中点、接地路径]
        N1[感应雷: 回击通道、外部电场、线路几何]
        N2[侵入波: 线路端入射波、保护器、变电站模型]
        N3[电缆/护套雷电暂态: 电缆护套、接地箱、保护器]
        N4[风电场/大接地网络: 风机、塔筒、互联接地]
    end
```


## 定义与边界

雷电暂态分析是在 EMT 中模拟雷电流、雷电电磁场、线路/电缆传播、接地响应、保护器动作和设备端口过电压的方法。它覆盖直击雷、反击、雷电感应过电压、侵入波和接地电位升等问题。

本页关注方法结构和证据边界。雷电流统计参数、标准波形、耐受电压和防雷设计限值必须绑定具体标准、论文或工程资料；没有来源时不应给出固定数值或“必然安全”的结论。

## EMT 中的作用

雷电暂态分析为以下任务提供输入：

- [[insulation-coordination]] 中的雷电冲击过电压和保护器应力。
- 变电站、配电网、风电场和换流站的避雷器/SPD 配置评估。
- 杆塔、接地网、电缆护套和设备外壳的 [[ground-potential-rise]]。
- 架空线、电缆和混合线路中的侵入波、反射和折射。
- 保护、通信和控制设备受到的高频干扰或端口过电压。

## 核心机制

雷电暂态模型由四个耦合层组成。

第一层是雷电源。直击或注入电流可表示为给定波形源：

$$i_L(t)=I_0 f(t;\theta)$$

其中 $\theta$ 包含波头、波尾、极性、回击类型或多脉冲时序。感应雷还需要回击通道模型和外部电磁场。

第二层是场-线或源-网接口。对于感应电压问题，外部电场可被转换为线路端口等效源，例如：

$$\mathbf{j}_0(t)=\mathbf{y}_c(t)*\bar{\mathbf{u}}_0(t),\quad
\mathbf{j}_\ell(t)=\mathbf{y}_c(t)*\bar{\mathbf{u}}_\ell(t)$$

第三层是传播网络。线路、电缆和接地体用频变或分布参数模型表示：

$$\mathbf{H}(\omega)=e^{-\ell\sqrt{\mathbf{Z}'(\omega)\mathbf{Y}'(\omega)}}$$

第四层是非线性与边界。避雷器、间隙、闪络、断路器、变压器端口和接地系统会改变反射、能量吸收和端口电压。

## 分析流程

1. 定义雷电问题：直击导线/杆塔/风机、附近雷击感应、变电站侵入波、反击或电缆护套过电压。
2. 选择雷电源模型：电流源、回击通道模型、外部场模型或标准试验波形，并记录参数来源。
3. 建立传播路径：架空线、地下电缆、混合线路、杆塔、接地引下线和接地网。
4. 选择宽频模型：[[frequency-dependent-line-model]]、[[universal-line-model]]、[[underground-cable-modeling]]、[[grounding-system-modeling]] 或等效端口源。
5. 加入保护与闪络模型：避雷器、保护间隙、绝缘子闪络、护层保护器和接地非线性。
6. 校核数值设置：步长、延时插值、拟合频带、无源性、开关事件和输出采样。
7. 输出端口波形和证据边界：峰值、陡度、到达时间、能量、GPR 和模型适用范围。

## 分类与变体

| 类型 | 典型输入 | EMT 关注点 | 主要边界 |
|------|----------|------------|----------|
| 直击雷 | 注入电流、击中点、接地路径 | GPR、反击、保护器能量 | 雷击点和接地非线性不确定 |
| 感应雷 | 回击通道、外部电场、线路几何 | 场-线耦合、端口等效源 | 外部场模型和土壤参数限制 |
| 侵入波 | 线路端入射波、保护器、变电站模型 | 设备端口电压和绝缘配合 | 进线段和接地模型很关键 |
| 电缆/护套雷电暂态 | 电缆护套、接地箱、保护器 | 护套过电压和绝缘接头应力 | 高频附件参数常缺失 |
| 风电场/大接地网络 | 风机、塔筒、互联接地 | 多端口接地和 GPR | 结论强依赖拓扑和土壤 |

## 适用边界与失败模式

- 雷电流参数和回击模型的选择会改变结果；不能把某一波形当作所有雷击的代表。
- 频变线路损耗、土壤频变和接地模型会影响远端、低压侧和多反射路径的波形。
- 避雷器和间隙模型若只用静态残压，可能不能表示能量、动态响应和引线电感。
- 闪络、电弧和土壤电离属于非线性事件，线性频域模型需要额外假设或状态切换。
- 单篇论文的数值误差、峰值或改善率只对其网络、雷击、土壤和工具设置有效。

## 代表性证据

- [[calculation-of-lightning-induced-voltages-on-a-large-scale-distribution-network-]]：支撑利用 JMarti 频变线路和端口独立电流源计算大规模配电网雷击感应电压；其量化结果必须绑定原文网络、土壤和雷击参数。
- [[ground-potential-rise-in-wind-farms-due-to-direct-lightning]]：支撑风电场直击雷 GPR 可通过接地网络宽带多端口模型接入 EMT；趋势不能外推到任意风电场。
- [[influence-of-frequency-characteristics-of-soil-on-lightning-transient-response-o]]：支撑频变土壤会影响大地返回参数，适合用于说明模型输入边界。
- [[time-domain-modeling-of-a-subsea-buried-cable]]：支撑海底电缆雷电/开关暂态中外部介质和时域实现路线的重要性，但该 source 本身不是雷电统计研究。

## 与相关页面的关系

- [[high-frequency-transient-analysis]] 给出宽频模型、步长和拟合边界。
- [[insulation-coordination]] 使用雷电端口波形做绝缘水平和保护配置判断。
- [[grounding-system-modeling]] 和 [[ground-potential-rise]] 处理接地响应。
- [[underground-cable-modeling]] 与 [[cross-bonded-cable]] 处理电缆和护套雷电过电压。
- [[earth-return-impedance]]、[[frequency-dependent-soil]] 和 [[frequency-dependent-line-model]] 决定传播和地模损耗。
- [[lightning-overvoltage]] 是雷电过电压主题页。

## 开放问题

- 大规模概率雷电研究与详细 EMT 模型之间仍存在计算成本冲突。
- 直击雷中的电弧、闪络路径、土壤电离和保护器热恢复需要更细的非线性模型与验证。
- 配电网和风电场场景下，真实接地布置、低压负荷高频模型和设备内部绝缘数据常是主要证据缺口。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[an-improved-approach-for-modeling-lightning-transients-of-wind-turbines|An improved approach for modeling lightning transients of wi]] | 2018 |
| [[computation-of-ground-potential-rise-and-grounding-impedance-of-simple-arrangeme|Computation of ground potential rise and grounding impedance]] | 2021 |
| [[earth-return-admittance-impact-on-crossbonded-underground-cables|Earth return admittance impact on crossbonded underground ca]] | 2021 |
| [[extension-of-vances-closed-form-approximation-to-calculate-the-ground-admittance|Extension of Vance]] | 2021 |
| [[full-wave-black-box-transmission-line-tower-model-for-the-assessment-of-lightnin|Full-wave black-box transmission line tower model for the as]] | 2021 |
| [[performance-of-the-recursive-methods-applied-to-compute-the-transient-responses-|Performance of the recursive methods applied to compute the ]] | 2021 |
| [[influence-of-a-lossy-ground-on-the-lightning-performance-of-overhead-transmissio|Influence of a lossy ground on the lightning performance of ]] | 2022 |
| [[comparison-of-soil-modeling-concerning-physical-factors-application-to-transient|Comparison of soil modeling concerning physical factors: App]] | 2023 |
| [[impact-of-solenoid-effects-on-series-impedance-of-three-core-armoured-cables|Impact of solenoid effects on series impedance of three-core]] | 2023 |
| [[electromagnetic-transient-modeling-and-surge-analysis-of-overhead-power-lines-ab|Electromagnetic transient modeling and surge analysis of ove]] | 2025 |
| [[influence-of-approximate-internal-impedance-formula-on-half-wavelength-transmiss|Influence of approximate internal impedance formula on half-]] | 2025 |
