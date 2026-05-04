---
title: "光伏电站 (PV Power Plant)"
type: topic
tags: [pv, solar, photovoltaic, power-plant, renewable, inverter, mppt]
created: "2026-05-02"
---

# 光伏电站 (PV Power Plant)

## 定义与边界

光伏电站是由光伏阵列、直流汇集、逆变器、升压变压器、集电线路、控制保护和并网接口组成的电源系统。EMT 语境中的光伏电站不是组件成本、运维或市场收益页面；本页关注其作为逆变器型电源进入电网后，如何建模、验证控制响应和界定并网暂态风险。

光伏电站也不等同于单个 [[pv-system-model]] 或 [[inverter-model]]。电站级 EMT 需要说明聚合方式、集电网络、电气距离、控制参数、辐照度场景和并网点强度。

## EMT 中的作用

光伏电站在 EMT 中通常用于研究：

- 并网逆变器的电流控制、PLL、限流、低电压穿越和故障后恢复。
- 大规模 PV 接入后的宽频振荡、谐波传播、电压支撑和保护配合。
- 光伏与储能、构网控制或混合电站在弱网下的暂态行为。
- 详细开关模型、[[average-value-model]] 和聚合等值模型之间的精度与计算量取舍。

## 主要分支与机制

- 光伏阵列模型：单二极管或等效电流源模型把辐照度、温度和直流端电压映射为电流功率特性。若只研究交流侧控制，阵列常被简化为直流源或慢变量。
- 逆变器模型：[[inverter-model]] 可采用开关级、平均值或受控电流源/电压源等值。开关级适合谐波与保护细节，平均值模型更适合系统级控制研究。
- 并网控制：[[gfl-inverter-model]] 依赖同步与电流注入，弱网下易受 PLL、阻抗耦合和限流影响；[[gfm-inverter-model]] 关注电压源行为、下垂或虚拟同步机制，但仍需用具体控制器验证。
- 电站聚合：把多个逆变器、箱变和集电线路合并为等效机组时，应说明聚合依据，例如容量权重、拓扑分区、辐照度分布或阻抗等效。

## 形式化表达

电站级 PV EMT 模型可概括为直流源、逆变器控制和交流网络接口的耦合：

$$
\begin{aligned}
i_{\mathrm{dc}} &= f_{\mathrm{pv}}(v_{\mathrm{dc}}, G, T),\\
i_{\mathrm{ac}}^\star &= C(v_{\mathrm{pcc}}, i_{\mathrm{ac}}, v_{\mathrm{dc}}, \omega, \theta),\\
Y_{\mathrm{grid}}v_{\mathrm{pcc}} &= i_{\mathrm{ac}} + i_{\mathrm{net}}
\end{aligned}
$$

其中 $G$ 和 $T$ 表示辐照度和温度，$C(\cdot)$ 表示逆变器控制与限流逻辑，$v_{\mathrm{pcc}}$ 是并网点电压。若聚合多个逆变器，应说明哪些状态和控制差异被保留，哪些被等值。

## 适用边界与失败模式

- 无来源的效率、成本、容量配比、跟踪增益和储能时长不应作为 EMT 结论；这些指标依赖地区、设备型号和商业条件。
- 平均值模型可能无法反映 PWM 谐波、死区效应、直流侧纹波和保护动作所需的瞬时电流。
- 单机等值可能掩盖集电线路谐振、分散逆变器控制差异和局部辐照度不一致。
- 弱网稳定结论必须绑定短路比、控制参数、扰动幅值、运行点和模型层级；不能从一个 PV 算例外推到所有逆变器型电源。

## 代表性来源

- [[switch-averaged-frequency-domain-simulation-of-photovoltaic-systems]] 提供光伏系统频域开关平均仿真的来源入口，适合讨论“只平均开关函数而保留网络频域特性”的方法边界。
- [[a-hybrid-simulation-tool-for-the-study-of-pv-integration-impacts-on-distribution]] 支撑配电网 PV 接入影响研究，但其结论应限于作者工具链和配电算例。
- [[photovoltaic-generator-modelling-to-improve-numerical-robustness-of-emt-simulati]] 关注光伏发电机 EMT 模型的数值鲁棒性，可作为模型稳定性而非经济性证据。
- [[fast-investigation-of-control-interaction-risks-in-pv-parks-using-eigenvalue-ana]] 适合支撑 PV 场站控制交互筛查；频域或特征值结论仍需时域 EMT 或现场数据交叉验证。

## 与相关页面的关系

- [[pv-system-model]] 解释光伏系统等效模型；本页组织电站级对象和应用边界。
- [[inverter-model]]、[[gfl-inverter-model]]、[[gfm-inverter-model]] 讨论逆变器控制和接口；本页不重复控制器内部方程。
- [[renewable-energy-integration]] 关注新能源并网总体问题；本页聚焦光伏电站。
- [[frequency-domain-analysis]] 和 [[harmonic-analysis]] 可用于识别阻抗耦合和谐波风险，但不能替代大扰动 EMT 验证。

## 开放问题

- 如何在不泄露厂家控制器细节的情况下建立可信的光伏电站 EMT 等值。
- 如何统一光伏场站的聚合误差、弱网稳定裕度、谐波风险和故障穿越验证指标。
- 如何把储能和构网控制纳入电站级模型，同时避免把单个控制器算例外推为通用能力。
