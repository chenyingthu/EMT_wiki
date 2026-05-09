---
title: "Energy Storage System"
type: topic
tags: [energy-storage-system]
created: "2026-05-04"
---

# Energy Storage System


```mermaid
graph LR
    N0[定义与边界]
    N1[EMT中的作用]
    N0 -->|Nf1| N1
    N2[主要分支与机制]
    N1 -->|Nf2| N2
    N3[形式化表达]
    N2 -->|Nf3| N3
    N4[适用边界与失败模式]
    N3 -->|Nf4| N4
    N5[与相关页面的关系]
    N4 -->|Nf5| N5
```


## 定义与边界

储能系统是由储能介质、功率变换器、控制器、保护和并网接口共同构成的系统对象。在 EMT Wiki 中，本页作为储能系统主题入口，承接 BESS、储能变流器、MMC-BESS、调频支撑和大规模交直流电网中储能接入等研究。

储能系统不是单一 EMT 数值方法。设备级电池模型应进入 [[bess-model]]，并网功率变换器应进入 [[energy-storage-converter-model]]，具体算例或测试平台应进入 test-system 页面。本页只组织系统层问题、证据边界和相邻页面关系。

## EMT中的作用

储能系统在 EMT 仿真中主要用于：

- 表示电池等储能介质的端口电压、电流、SOC 和限幅状态。
- 验证储能变流器在故障、电压跌落、功率指令切换和弱网条件下的动态响应。
- 研究 BESS 与 HVDC、MMC、微电网或大规模交直流系统之间的暂态交互。
- 为 EMT-TS 混合仿真、GPU/并行仿真和硬件在环测试提供设备集群对象。

## 主要分支与机制

储能系统页面至少应区分 3 层：

- 介质层：电池、超级电容、飞轮或其他储能介质，决定能量状态和约束。
- 变流器层：PCS、滤波器、限流器、并网控制和直流/交流接口。
- 系统层：储能参与调频、无功支撑、直流电压支撑、微电网或大系统稳定验证。

大规模 BESS 研究还可能涉及模型向量化、TLL 解耦、多速率 EMT-TS 接口和 GPU/CPU 异构并行，但这些是仿真实现路线，不应把单篇论文的加速结果写成本页通用结论。

## 形式化表达

储能端口模型常可抽象为：

$$
P_{\mathrm{ac}} = \eta_{\mathrm{pcs}} P_{\mathrm{dc}},\qquad
\dot{E}= -P_{\mathrm{dc}}
$$

其中 $P_{\mathrm{ac}}$ 是交流侧功率，$P_{\mathrm{dc}}$ 是储能介质与变流器直流侧交换功率，$\eta_{\mathrm{pcs}}$ 表示变流器效率或损耗近似，$E$ 表示储能状态。具体电池等效电压、SOC 方程、BMS 限制和 PCS 控制必须在设备模型或来源页中给出。

## 适用边界与失败模式

- 电池模型参数、SOC 初值和温度/老化状态会影响 EMT 响应，不能用统一参数代表所有储能。
- PCS 限流、直流电压保护和控制模式切换常决定故障期间表现。
- 大规模 BESS 的并行加速结论必须绑定硬件平台、步长、模型规模和对比基线。
- 储能改善频率或电压支撑的结论应绑定控制策略、容量、运行点和测试系统。

## 与相关页面的关系

- [[bess-model]]：电池储能设备模型。
- [[energy-storage-converter-model]]：PCS 和并网变流器模型。
- [[microgrid]]：微电网测试系统中储能的系统角色。
- [[emt-simulation]]：储能 EMT 建模与时域验证背景。
## 代表性来源

- [[massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high]]：支撑大规模 BESS、CPU-GPU 异构并行和 EMT-TS 联合仿真背景；其加速结果必须限于原文硬件、模型规模和测试系统。
- [[modeling-of-mmc-based-statcom-with-embedded-energy-storage-for-the-simulation-of]]：支撑嵌入式储能 STATCOM/MMC 模型背景。
- [[an-electromagnetic-transient-simulation-model-of-mmc-bess-for-various-operating-]]：支撑 MMC-BESS EMT 模型和工况讨论。
