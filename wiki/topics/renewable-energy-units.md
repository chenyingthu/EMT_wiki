---
title: "新能源机组 (Renewable Energy Units)"
type: topic
tags: [renewable-energy, wind-power, pv, inverter, grid-connection, low-voltage-ride-through]
created: "2026-05-02"
---

# 新能源机组 (Renewable Energy Units)

## 定义与边界

新能源机组是把风能、太阳能或储能侧能量转换为交流并网功率的设备单元，通常包含机械或直流能源侧、变流器、控制器、保护和并网接口。本页关注机组级 EMT 模型，不讨论政策、成本或容量统计。

新能源机组不同于新能源并网主题。[[renewable-energy-integration]] 讨论场站和系统接入问题；本页聚焦单机或少量等值机组的物理对象、控制接口和模型层级。

## EMT 中的作用

新能源机组 EMT 模型用于研究：

- 风机或光伏逆变器的电流环、PLL、直流侧、限流和故障穿越。
- DFIG、PMSG、全功率变流器和光伏逆变器在故障时的电压电流响应。
- 详细开关模型、平均值模型和受控源等值之间的保真度取舍。
- 机组控制与线路、变压器、保护和外部电网强度之间的相互作用。

## 主要分支与机制

- DFIG 机组：定子直接接入交流网，转子经部分容量变流器控制。EMT 模型需明确转子侧控制、crowbar 或保护逻辑是否保留。
- PMSG 或全功率风机：发电机经机侧和网侧变流器接入，直流链路、电流限幅和并网控制通常是主要动态。
- 光伏单元：可从单二极管阵列、直流源、DC/DC 变换器和并网逆变器不同层级建模；若只研究交流侧，阵列可降级为慢变量或功率源。
- 储能单元：电池或超级电容侧状态、DC/DC 接口和并网逆变器共同决定暂态能力；SOC 和热模型是否保留应由研究目标决定。

## 形式化表达

机组级模型可写为能源侧、直流侧和交流接口的组合：

$$
\dot{x}_e=f_e(x_e,u_e),\qquad
C_{\mathrm{dc}}\dot{v}_{\mathrm{dc}}=i_e-i_{\mathrm{conv}},\qquad
i_{\mathrm{ac}}=C_g(v_{\mathrm{pcc}},v_{\mathrm{dc}},x_c)
$$

其中 $x_e$ 表示风机、光伏或储能能源侧状态，$v_{\mathrm{dc}}$ 是直流链路电压，$C_g$ 是并网控制器和限流逻辑。不同机组模型的差别在于保留哪些状态、哪些控制环节和哪些保护事件。

## 适用边界与失败模式

- 机组控制参数、限流曲线和保护策略若来自厂家黑盒，页面应说明证据边界，不能把等效模型写成真实控制器。
- 平均值模型适合系统级暂态和稳定性研究，但可能丢失开关谐波、死区、采样延迟和保护瞬时判据。
- 单机模型不能自动代表整个场站；集电网络、机组差异和局部风速/辐照度会改变响应。
- 并网标准中的穿越要求应以具体标准版本和地区为准，本页不列无来源固定阈值。

## 代表性来源

- [[equivalent-grid-following-inverter-based-generator-model-for-atpatpdraw-simulati]] 可作为跟网型逆变器机组等值模型来源入口。
- [[photovoltaic-generator-modelling-to-improve-numerical-robustness-of-emt-simulati]] 支撑光伏发电机 EMT 模型的数值鲁棒性讨论。
- [[a-hybrid-simulation-tool-for-the-study-of-pv-integration-impacts-on-distribution]] 可作为分布式光伏接入影响研究来源。
- [[fast-investigation-of-control-interaction-risks-in-pv-parks-using-eigenvalue-ana]] 支撑机组或场站控制交互筛查，但仍需 EMT/现场数据交叉验证。

## 与相关页面的关系

- [[dfig-model]]、[[pv-system-model]]、[[inverter-model]]、[[gfl-inverter-model]] 和 [[gfm-inverter-model]] 是具体模型页。
- [[pv-power-plant]] 讨论电站级聚合和集电网络。
- [[renewable-energy-integration]] 讨论并网系统层问题。
- [[frequency-domain-analysis]] 和 [[small-signal-analysis]] 可用于筛查控制交互，不能替代故障穿越 EMT 验证。

## 开放问题

- 如何在缺少厂家详细控制器的条件下建立机组 EMT 等值并报告可信度。
- 如何评估机组聚合对场站谐振、保护和弱网稳定结论的影响。
- 如何统一机组级、场站级和系统级模型的参数来源与验证证据。
