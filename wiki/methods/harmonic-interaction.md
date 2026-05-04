---
title: "谐波交互机制 (Harmonic Interaction Mechanism)"
type: method
tags: [harmonic, interaction, multi-infeed, lcc, resonance, instability]
created: "2026-05-02"
---

# 谐波交互机制 (Harmonic Interaction Mechanism)

## 定义与边界

谐波交互机制描述不同设备、网络阻抗、控制环节和频率分量之间通过电压、电流或控制变量形成的耦合关系。它关注的不只是“系统中存在谐波”，而是谐波分量如何传播、叠加、调制、反馈，并在特定条件下影响换相、保护、振荡或稳定裕度。

本页是方法/机制页，适合解释交互路径和建模假设；具体频谱提取应参见 [[fft]] 和 [[fourier-filtering]]，网络传播量参见 [[harmonic-transfer-coefficient]]，阻抗和稳定判据参见 [[frequency-domain-analysis]] 与 [[small-signal-analysis]]。

## EMT 中的作用

EMT 仿真能保留开关、控制和网络暂态，因此常用于观察谐波交互的时域过程。谐波交互分析则帮助解释以下问题：

- 多馈入 LCC-HVDC 中，交流故障和换流器谐波如何影响远端逆变器关断角。
- 并联逆变器或 MMC 系统中，控制延迟、PLL、滤波器和网络阻抗如何形成宽频振荡。
- 谐波源、滤波器和频率相关线路/电缆模型之间是否可能形成放大路径。
- 频域诊断结果与 EMT 波形中的失稳、过电压或保护误动之间是否存在可解释联系。

这些分析都应绑定拓扑、控制模型、故障类型和运行点。单个算例中的交互路径不能直接写成一般规律。

## 核心机制

在线性化频域表示中，网络响应可写为：

$$V_h=Z_h I_h$$

当设备谐波电流又受谐波电压影响时，可写成局部 Norton 或导纳型关系：

$$\Delta I_h=Y_\text{dev}(h)\Delta V_h+\Delta I_\text{src}(h)$$

代入网络方程后得到闭环关系：

$$\Delta V_h=\left(I-Z_hY_\text{dev}(h)\right)^{-1}Z_h\Delta I_\text{src}(h)$$

这个表达只是一种局部线性化解释。实际 EMT 中还可能存在频率耦合、开关非线性、限幅、离散控制延迟和保护动作，因此需要用时域仿真或分段线性分析验证。

## 分类与变体

| 交互类型 | 典型路径 | 适合分析工具 | 主要边界 |
|----------|----------|--------------|----------|
| 同频谐波叠加 | 多个源在同一频率注入 | [[harmonic-transfer-coefficient]]、谐波潮流 | 相位和源定位很关键 |
| 网络谐振放大 | 谐波源与 RLC/线路阻抗耦合 | [[frequency-scan]]、阻抗测量 | 依赖运行方式和频变模型 |
| 控制-网络耦合 | PLL、电流环、滤波器与弱网 | 小信号阻抗、EMT 扰动 | 需要控制器参数 |
| 换相相关交互 | LCC 换流、交流故障、谐波电压 | EMT + 关断角模型 | 结论绑定 LCC 拓扑和故障条件 |
| 多频率调制 | 开关频率、基波和边带耦合 | 动态相量、时频分析 | 频率耦合不能用单一谐波解释 |

## 适用边界与失败模式

- “谐波交互”不是任意谐波共存的同义词。必须说明交互路径：源、网络、控制或设备状态如何相互影响。
- 频域闭环判据常基于线性化和固定运行点；大扰动故障、限幅和保护逻辑需要 EMT 时域验证。
- 若只给 FFT 频谱而没有网络阻抗、控制模型或注入响应，不能直接断言存在谐波不稳定。
- 多设备系统中的责任归因需要相位、阻抗和源模型支撑；简单比较各节点 THD 容易误导。

## 代表性来源

- [[harmonics-interaction-mechanism-and-impact-on-extinction-angles-in-multi-infeed-]]：可作为多馈入 LCC-HVDC 谐波交互与关断角影响的代表性证据；应保留“交流故障、多馈入、LCC”这些场景边界。
- [[analysis-on-non-characteristic-harmonic-circulating-current-in-parallel-inverter]]：适合说明并联逆变器之间可能出现非特征谐波环流，但不能泛化到所有并联系统。
- [[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-]]：可支撑 MMC 高频振荡与滤波/控制耦合讨论，具体频段和抑制效果需绑定原文。
- [[a-harmonic-phasor-domain-co-simulation-method-and-new-insight-for-harmonic-analy]]：说明谐波相量域可用于多频率交互仿真，但不应写成对所有 EMT 场景的替代。

## 与相关页面的关系

- [[fourier-series]]、[[fft]] 和 [[fourier-filtering]] 提供频率分量提取语言。
- [[harmonic-transfer-coefficient]] 是描述传播路径的局部量。
- [[dynamic-phasor]] 和 [[frequency-dependent-modeling]] 支撑跨频率和宽频网络表示。
- [[vsc-model]]、[[mmc-model]]、[[lcc-model]]、[[pll-model]] 决定设备侧交互机制。
- [[wideband-oscillation-stability]] 关注交互导致的稳定性后果。

## 修订与证据使用注意事项

后续扩展本页时，优先补充“交互路径图式”和“证据边界”，而不是堆叠谐波幅值表。涉及不稳定、换相失败、振荡抑制或滤波效果时，应写清楚来源论文、系统拓扑、控制参数、故障类型和验证工具。
