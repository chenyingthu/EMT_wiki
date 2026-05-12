---
title: "Energy Storage System"
type: topic
tags: [energy-storage-system]
created: "2026-05-04"
updated: "2026-05-11"
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
    N4[量化性能边界]
    N3 -->|Nf4| N4
    N5[适用边界与失败模式]
    N4 -->|Nf5| N5
    N6[与相关页面的关系]
    N5 -->|Nf6| N6
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

- **介质层**：电池、超级电容、飞轮或其他储能介质，决定能量状态和约束。不同介质的时间常数跨度从毫秒（超级电容）到小时（电池），直接影响 EMT 模型的时间尺度选择。
- **变流器层**：PCS、滤波器、限流器、并网控制和直流/交流接口。MMC-BESS 还需考虑子模块级 DC-DC 变换器的独立建模（Hatahet 2026）。
- **系统层**：储能参与调频、无功支撑、直流电压支撑、微电网或大系统稳定验证。并联 VSC-ESS 的惯量协调是当前研究热点（Hu 2025）。

大规模 BESS 研究还可能涉及模型向量化、TLL 解耦、多速率 EMT-TS 接口和 GPU/CPU 异构并行，但这些是仿真实现路线，不应把单篇论文的加速结果写成本页通用结论。

## 形式化表达

储能端口模型常可抽象为：

$$
P_{\mathrm{ac}} = \eta_{\mathrm{pcs}} P_{\mathrm{dc}},\qquad
\dot{E}= -P_{\mathrm{dc}}
$$

其中 $P_{\mathrm{ac}}$ 是交流侧功率，$P_{\mathrm{dc}}$ 是储能介质与变流器直流侧交换功率，$\eta_{\mathrm{pcs}}$ 表示变流器效率或损耗近似，$E$ 表示储能状态。具体电池等效电压、SOC 方程、BMS 限制和 PCS 控制必须在设备模型或来源页中给出。

对于 MMC-BESS，Wang (2025) 使用开关函数描述子模块 DC-DC 变换器，使电池侧与 MMC 阀侧在 EMT 模型中保持电气解耦。Hatahet (2026) 的 D-DEM 进一步将子模块电容电压用前向欧拉显式离散化，节点方程从 4×4 降至 1×1。

## 量化性能边界

BESS 建模的精度-效率权衡已有可核验的量化结果：

- **Wang (2025)** 提出 MMC-BESS EMT 模型覆盖整流、逆变、STATCOM 和闭锁四种工况，在 PSCAD/EMTDC 中验证子模块电容电压平衡和功率阶跃响应，原文未报告具体加速比或步长设置。
- **Hatahet (2026)** 的 D-DEM 将节点方程从 4×4 降至 1×1，采用 CPU 大步长（50 μs）+ GPU 小步长（2.5-5 μs）多速率架构，步长比 10:1-20:1，在保留闭锁/解锁动态的前提下实现恒定导纳矩阵。
- **Hu (2025)** 在并联 VSC-ESS 中验证暂态电磁功率补偿策略，自适应惯量控制显著抑制频率响应过程中的有功超调和振荡，通过幅频特性曲线和极点轨迹分析并联单元间参数交互。

## 适用边界与失败模式

- 电池模型参数、SOC 初值和温度/老化状态会影响 EMT 响应，不能用统一参数代表所有储能。
- PCS 限流、直流电压保护和控制模式切换常决定故障期间表现。
- 大规模 BESS 的并行加速结论必须绑定硬件平台、步长、模型规模和对比基线。
- 储能改善频率或电压支撑的结论应绑定控制策略、容量、运行点和测试系统。
- Hatahet (2026) 的 D-DEM 显式电容电压更新采用前向欧拉法，可能在大步长下引入数值稳定性约束。

## 与相关页面的关系

- [[bess-model]]：电池储能设备模型。
- [[energy-storage-converter-model]]：PCS 和并网变流器模型。
- [[microgrid]]：微电网测试系统中储能的系统角色。
- [[emt-simulation]]：储能 EMT 建模与时域验证背景。
- [[virtual-synchronous-generator]]：VSG 控制是储能变流器参与调频的典型方法。
- [[inertia-control]]：储能提供虚拟惯量的控制策略方法页。

## 代表性来源

- [[massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high]]：大规模BESS的CPU-GPU异构并行和EMT-TS联合仿真。
- [[an-electromagnetic-transient-simulation-model-of-mmc-bess-for-various-operating-]]：MMC-BESS 四工况 EMT 模型（整流、逆变、STATCOM、闭锁）。
- [[decoupled-detailed-equivalent-model-for-parallel-and-multi-rate-emt-type-simulat]]：D-DEM 恒定导纳+多速率 CPU-GPU 求解，验证于 BESS-MMC 系统。
- [[transient-electromagnetic-power-compensationbased-adaptive-inertia-control-strat]]：并联 VSC-ESS 自适应惯量与暂态补偿控制。
- [[modeling-of-mmc-based-statcom-with-embedded-energy-storage-for-the-simulation-of]]：嵌入式储能 STATCOM/MMC 模型。

## 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|---------|
| [[massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high]] | 2023 | 大规模BESS并行建模与EMT-TS联合仿真 |
| [[decoupled-detailed-equivalent-model-for-parallel-and-multi-rate-emt-type-simulat|Decoupled DEM for MMC-BESS Multi-Rate EMT]] | 2026 | D-DEM恒定导纳+CPU-GPU多速率 |
| [[transient-electromagnetic-power-compensationbased-adaptive-inertia-control-strat|Transient EM Power Compensation Adaptive Inertia]] | 2025 | 并联VSC-ESS自适应惯量与功率补偿 |
| [[an-electromagnetic-transient-simulation-model-of-mmc-bess-for-various-operating-|MMC-BESS EMT Model for Various Operating Conditions]] | 2025 | MMC-BESS四工况EMT模型验证 |
| [[modeling-of-mmc-based-statcom-with-embedded-energy-storage-for-the-simulation-of|MMC STATCOM with Embedded Energy Storage]] | 2023 | 嵌入式储能STATCOM建模 |
