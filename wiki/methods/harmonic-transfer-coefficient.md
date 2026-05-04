---
title: "谐波传递系数 (Harmonic Transfer Coefficient)"
type: method
tags: [harmonic, transfer, coefficient, power-electronics, harmonic-analysis, frequency-domain]
created: "2026-05-02"
---

# 谐波传递系数 (Harmonic Transfer Coefficient)

## 定义与边界

谐波传递系数用于描述某一频率分量从激励位置传到观测位置时的幅值和相位关系。它可以定义为电压比、电流比、传递阻抗或灵敏度项，具体形式必须随模型对象说明。例如，在给定谐波阶次 $h$ 和线性化频域网络下，若在节点 $i$ 注入谐波电流并观察节点 $j$ 的谐波电压，可写为：

$$Z_{ji}(h)=\frac{V_j(h)}{I_i(h)}$$

若使用电压比形式，则可写为：

$$H_{ji}(h)=\frac{V_j(h)}{V_i(h)}$$

这两个量的物理含义不同，不能混用。前者是传递阻抗或灵敏度，后者是节点间电压传递比。本页关注“如何定义和解释传递关系”，不替代 [[topics/harmonic-analysis.md]]、[[methods/frequency-scan.md]] 或 [[methods/impedance-measurement.md]]。

## EMT 中的作用

在 EMT 研究中，谐波传递系数常用于回答三个问题：

- 某个换流站、逆变器或非线性负载产生的谐波会在网络中如何传播。
- 某个网络阻抗峰值是否会放大特定谐波阶次。
- 多馈入 LCC-HVDC、并联变流器或弱网并网场景中，一个节点的谐波扰动是否会影响另一个节点的换相、控制或稳定裕度。

它通常与 EMT 时域仿真互补：EMT 给出波形和暂态过程，传递系数提供某一频率附近的网络解释。若系统强非线性、频率耦合明显或运行点快速变化，传递系数应被视为局部、工况绑定的诊断量。

## 核心机制

在线性频域近似下，节点方程可写为：

$$Y(h)V(h)=I(h)$$

若 $Y(h)$ 可逆，则：

$$V(h)=Z(h)I(h),\quad Z(h)=Y^{-1}(h)$$

其中 $Z_{ji}(h)$ 表示节点 $i$ 注入单位谐波电流时节点 $j$ 的电压响应。若要得到电压比形式，需要再选择参考电压或驱动点响应：

$$H_{ji}(h)=\frac{Z_{ji}(h)}{Z_{ii}(h)}$$

在换流器或逆变器研究中，传递关系也可能写成“扰动电压到谐波电流”“谐波电流到关断角变化”或“源侧到受端的等效电路传递”。这些定义都应保留输入、输出、阶次和运行点。

## 分类与变体

| 形式 | 输入 | 输出 | 典型用途 | 风险 |
|------|------|------|----------|------|
| 传递阻抗 $Z_{ji}(h)$ | 节点注入电流 | 节点电压响应 | 谐振识别、源定位 | 依赖网络模型和运行点 |
| 电压传递比 $H_{ji}(h)$ | 源节点电压 | 观测节点电压 | 多节点传播解释 | 参考节点选择会改变数值 |
| 灵敏度 $\partial V_j/\partial I_i$ | 小扰动注入 | 线性响应 | 频率扫描、弱网分析 | 大扰动下不一定成立 |
| 控制耦合传递 | 控制量或换相量扰动 | 电流/电压谐波变化 | LCC、VSC、PLL 耦合 | 需要明确控制模型 |

## 适用边界与失败模式

- 传递系数不是设备固定参数。网络拓扑、滤波器投切、变压器接线、控制状态和运行点都会改变结果。
- 频率相关线路、电缆、大地返回和设备宽频模型会影响 $Y(h)$；低频等值不能无条件用于高频谐波。
- 多谐波源同时存在时，观测波形是各源贡献和相位叠加的结果，单个传递系数不能直接给出责任归因。
- 对 LCC-HVDC 换相失败、VSC 宽频振荡或 PLL 耦合问题，应把传递系数与 [[methods/harmonic-interaction.md]]、[[methods/small-signal-analysis.md]] 和 EMT 时域验证结合使用。

## 代表性来源

- [[sources/harmonics-interaction-mechanism-and-impact-on-extinction-angles-in-multi-infeed-.md]]：给出多馈入直流系统交流故障期间谐波传播、传递等效电路和关断角影响的场景化证据；其结论不应外推到所有 HVDC 拓扑。
- [[sources/analysis-of-frequency-dependent-network-equivalents-in-dynamic-harmonic-domain.md]]：适合支撑频率相关网络等值对谐波传递关系的影响。
- [[sources/a-time-domain-harmonic-power-flow-algorithm.md]]：说明谐波潮流可与时域框架结合，但具体传递系数仍需绑定算法假设。
- [[sources/an-emt-based-dynamic-frequency-scanning-tool-for-stability-analysis-of-inverter-.md]]：展示通过 EMT 扰动和频域提取获得阻抗/传递信息的思路。

## 与相关页面的关系

- [[methods/fourier-series.md]] 和 [[methods/fft.md]] 解决频率分量提取问题；本页解决分量在网络中的传递解释。
- [[topics/frequency-dependent-modeling.md]] 和 [[methods/passivity-enforcement.md]] 影响传递矩阵是否可信。
- [[models/vsc-model.md]]、[[models/mmc-model.md]]、[[models/lcc-model.md]] 和 [[models/pll-model.md]] 决定谐波源和控制耦合如何进入网络方程。
- [[methods/vector-fitting.md]] 可把频域传递关系转化为可用于时域仿真的有理模型。

## 修订与证据使用注意事项

不要把本页写成“谐波治理通用方案”或“标准限值汇编”。若加入滤波器、标准或设备谐波幅值，应转到相应模型/标准页面，并保留来源、频段、阶次和验证工况。
