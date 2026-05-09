---
title: "绝缘配合 (Insulation Coordination)"
type: method
tags: [insulation, coordination, overvoltage, lightning, protection, bco, statistical-method]
created: "2026-05-02"
---

# 绝缘配合 (Insulation Coordination)


```mermaid
graph TD
    subgraph Ncmp[绝缘配合 (Insulation Coordination)]
        N0[确定性配合: 代表性过电压与耐受水平加裕度比较]
        N1[统计配合: 过电压分布与闪络概率积分]
        N2[EMT 参数扫描: 对关键参数做条件仿真]
        N3[保护器能量校核: 积分计算吸收能量和热应力]
    end
```


## 定义与边界

绝缘配合是在给定电力系统结构、过电压环境、保护装置和设备耐受特性的条件下，选择设备绝缘水平和保护配置的方法。它把 EMT 或统计计算得到的代表性过电压，与设备的雷电冲击、操作冲击、工频和暂时过电压耐受能力进行有边界的比较。

本页讨论绝缘配合作为方法流程，不给出通用 BIL/BSL 数值表或固定安全裕度。具体耐受电压、保护水平、海拔修正、污秽和试验要求应回到适用标准、设备技术条件和项目设计文件。

## EMT 中的作用

在 EMT 研究中，绝缘配合通常回答：

- 雷电侵入波、反击、感应雷和开关操作会在设备端口产生什么电压波形。
- 避雷器、保护间隙、护层保护器和接地系统把设备端口电压限制到什么范围。
- 变压器、GIS、电缆终端、绝缘接头、换流阀或电力电子设备需要承受哪些波形与能量。
- 参数不确定性、雷电统计和保护器特性离散性是否改变风险排序。

因此，绝缘配合不是单次峰值比较。对于陡波、高频振荡或长尾能量，应同时检查波形、持续时间、保护器能量、接地电位和设备端口边界。

## 核心机制

确定性配合可概念性写成：

$$U_\text{withstand} \ge K_c U_\text{protective}$$

其中 $U_\text{withstand}$ 是设备耐受水平，$U_\text{protective}$ 是受保护设备端口处的代表性过电压或保护水平，$K_c$ 是考虑不确定性、老化、环境和统计离散性的配合因子。该式只是结构表达，不能替代标准给定的具体取值。

统计配合关注过电压概率分布与绝缘闪络概率的重叠。若 $f_U(u)$ 是过电压概率密度，$P_f(u)$ 是给定电压下的闪络概率，则风险指标可写为：

$$R=\int_0^\infty f_U(u)P_f(u)\,du$$

EMT 的角色是给出 $U$ 的条件分布或代表性波形：雷电流、入射点、土壤、接地、电缆长度、开关相角、重燃状态和保护器模型都会改变结果。

保护器能量也需要检查：

$$W=\int_{t_0}^{t_1}u_a(t)i_a(t)\,dt$$

其中 $u_a$、$i_a$ 是避雷器或护层保护器端口波形。

## 配合流程

1. 定义受保护对象和端口：变压器绕组、GIS 间隔、电缆终端、绝缘接头、护套、换流站设备或配电负荷。
2. 选择过电压类型：[[lightning-transient-analysis]]、[[switching-transient]]、暂时过电压、铁磁谐振或故障恢复。
3. 建立 EMT 模型：线路/电缆、接地系统、保护器、变压器/设备端口和边界网络。
4. 生成工况集合：雷电参数、开关相角、故障位置、土壤参数、保护器特性和端接条件。
5. 提取指标：峰值、陡度、波头/波尾、持续时间、能量、端口间电压和 GPR。
6. 与标准或设备耐受数据比较，并明确确定性或统计性解释。
7. 记录剩余不确定性：模型频带、设备内部模型、保护器老化、现场接地和测量缺口。

## 方法变体

| 方法 | 核心思想 | 适合用途 | 主要边界 |
|------|----------|----------|----------|
| 确定性配合 | 代表性过电压与耐受水平加裕度比较 | 工程初设、标准化设备 | 工况和裕度来源必须明确 |
| 统计配合 | 过电压分布与闪络概率积分 | 雷电风险、线路绝缘设计 | 需要可靠统计输入 |
| EMT 参数扫描 | 对关键参数做条件仿真 | 设备端口波形和保护器应力 | 不自动等于概率结论 |
| 保护器能量校核 | 积分计算吸收能量和热应力 | MOV、护层保护器、SPD | 设备热模型和额定数据需来源 |

## 适用边界与失败模式

- 不应把单个 EMT 工况的最大峰值写成系统绝缘风险，除非已说明采样范围和代表性。
- 避雷器残压、能量和老化特性依赖型号、波形和标准试验条件；无资料时只能保守描述。
- 设备内部绕组、GIS 陡波传播、电缆终端局部场强等可能不是外部端口 EMT 模型能直接覆盖的。
- 接地系统和电缆护套边界会影响端口过电压；理想接地假设必须说明。
- 标准绝缘水平和试验波形会随地区、标准版本和设备类型变化，wiki 页不应维护无来源通用表。

## 代表性证据

- [[lightning-transient-analysis]] 和 [[high-frequency-transient-analysis]]：提供 EMT 过电压波形生成和频带边界。
- [[calculation-of-lightning-induced-voltages-on-a-large-scale-distribution-network-]]：支撑配电网雷击感应过电压研究中线路频变损耗、拓扑反射和非线性元件会影响低压端口电压；量化结果只能绑定其原文网络和土壤工况。
- [[ground-potential-rise-in-wind-farms-due-to-direct-lightning]]：支撑直击雷下接地电位升和接地网络模型会影响设备端口应力；趋势不能外推为所有风电场设计结论。
- [[surge-arrester-model]]：是保护器非线性模型入口，具体参数应取自设备资料或原文。

## 与相关页面的关系

- [[lightning-transient-analysis]]、[[switching-transient]] 和 [[high-frequency-transient-analysis]] 生成配合输入波形。
- [[grounding-system-modeling]] 与 [[ground-potential-rise]] 决定接地端口电位。
- [[underground-cable-modeling]] 和 [[cross-bonded-cable]] 决定电缆终端、护套和绝缘接头应力。
- [[frequency-dependent-line-model]]、[[universal-line-model]] 和 [[earth-return-impedance]] 决定线路/电缆传播和衰减。

## 开放问题

- 设备内部绝缘模型和外部 EMT 端口模型之间的映射常需要厂家资料或专门试验。
- 多风险源联合统计，如雷电位置、土壤状态、开关相角和保护器离散性，往往缺少统一公开数据。
- 保护器能量和热恢复在重复暂态下的建模应避免用单次波形结论外推。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[application-of-emtp-rv-graphic-software-of-electromagnetic-transient-simulation|Application of EMTP-RV graphic software of electromagnetic t]] | 2007 |
| [[electromagnetic-disturbances-in-gas-insulated-substations-and-vft-calculations|Electromagnetic disturbances in gas-insulated substations an]] | 2018 |
| [[grounding-grids-in-electro-magnetic-transient-simulations-with-frequency-depende|Grounding grids in electro-magnetic transient simulations wi]] | 2019 |
| [[development-of-a-voltage-dependent-line-model-to-represent-the-corona-effect-in-|Development of a Voltage-Dependent Line Model to Represent t]] | 2020 |
| [[a-new-model-of-trapped-charge-sources-in-switching-transient-studies-in-the-pres|A New Model of Trapped Charge Sources in Switching Transient]] | 2025 |
