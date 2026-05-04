---
title: "可再生能源并网 (Renewable Energy Integration)"
type: topic
tags: [renewable-energy, integration, grid-connection, wind, solar, low-voltage-ride-through]
created: "2026-05-02"
---

# 可再生能源并网 (Renewable Energy Integration)

## 定义与边界

可再生能源并网是风电、光伏、储能和其他可再生资源通过变流器、变压器、集电网络和控制保护系统接入电网的技术问题。它不是装机容量统计、政策评价或市场收益页面；在 EMT Wiki 中，本页关注并网设备在暂态、控制、保护和稳定性方面的建模边界。

可再生能源并网不等同于单个机组模型。风电、光伏、储能、并网逆变器、场站聚合和调度运行分别有不同证据边界，可参考 [[renewable-energy-units]]、[[pv-power-plant]]、[[inverter-model]]、[[gfl-inverter-model]] 和 [[gfm-inverter-model]]。

## EMT 中的作用

EMT 用于分析可再生能源并网中的快速电磁和控制暂态：

- 弱网条件下 PLL、电流环、限流器和无功控制之间的交互。
- 低电压穿越、高电压穿越、故障后恢复和保护配合。
- 多逆变器、集电线路和滤波器引起的谐波、宽频振荡和阻抗耦合。
- 构网型控制、储能和混合电站对电压频率支撑的暂态表现。

## 主要分支与机制

- 风电并网：DFIG、PMSG 和全功率变流器机组在电机、电力电子和机械环节上保留的状态不同。模型层级应随研究对象选择。
- 光伏并网：[[pv-power-plant]] 需要同时说明光伏阵列、直流侧、逆变器控制、集电网络和并网点强度。
- 跟网型控制：[[gfl-inverter-model]] 依赖同步环节和电流注入，弱网和故障期间的限流逻辑是关键边界。
- 构网型控制：[[gfm-inverter-model]] 以电压源或下垂/虚拟同步机制参与支撑，但结论必须绑定控制器、容量和故障工况。
- 场站聚合：把多台机组等值为单机或少量等值机组时，应说明容量权重、集电阻抗、控制一致性和辐照/风速分布。

## 形式化表达

并网逆变器和电网接口可抽象为控制器、限流器和网络方程的耦合：

$$
i^\star = C(v_{\mathrm{pcc}},P^\star,Q^\star,x_c),\qquad
i = \mathrm{sat}(i^\star,I_{\max}),\qquad
Y_{\mathrm{grid}}v_{\mathrm{pcc}} = i + i_{\mathrm{net}}
$$

其中 $C(\cdot)$ 是控制器，$x_c$ 是控制状态，$I_{\max}$ 是限流边界，$v_{\mathrm{pcc}}$ 是并网点电压。不同控制策略的核心差异在于同步方式、电流或电压源接口、限流处理和故障穿越逻辑。

## 适用边界与失败模式

- 无来源的容量占比、穿越时长、效率、储能配比和控制收益不应写成通用结论；这些指标依赖标准、设备和地区。
- 平均值模型可能无法表示 PWM 谐波、保护瞬时电流、直流侧纹波和子模块电容动态。
- 单机等值可能掩盖集电网络谐振、机组控制差异和局部弱网问题。
- 频域阻抗筛查只能说明某一运行点附近的小扰动风险，大扰动故障和限流过程仍需 EMT 时域验证。

## 代表性来源

- [[photovoltaic-generator-modelling-to-improve-numerical-robustness-of-emt-simulati]] 支撑光伏 EMT 模型数值鲁棒性讨论。
- [[fast-investigation-of-control-interaction-risks-in-pv-parks-using-eigenvalue-ana]] 可作为 PV 场站控制交互筛查的来源入口。
- [[a-hybrid-simulation-tool-for-the-study-of-pv-integration-impacts-on-distribution]] 支撑配电网 PV 接入影响研究，但结论应绑定作者工具链和算例。
- [[equivalent-grid-following-inverter-based-generator-model-for-atpatpdraw-simulati]] 可作为跟网型逆变器等效建模来源入口。

## 与相关页面的关系

- [[renewable-energy-units]] 更关注单个风电、光伏或储能单元的模型对象。
- [[pv-power-plant]] 是光伏电站级主题页。
- [[frequency-domain-analysis]] 和 [[harmonic-analysis]] 用于识别振荡和谐波风险；[[emt-simulation]] 用于时域验证。
- [[dispatch-operation]] 关注运行方式和场景选择，不能替代 EMT 模型验证。

## 开放问题

- 如何为厂家黑盒变流器建立可共享、可校核的 EMT 等值。
- 如何统一构网型控制、储能、保护定值和场站聚合误差的验证指标。
- 如何把频域筛查、EMT 时域仿真和现场扰动数据组织成一致证据链。
