---
title: "A.M. Gole"
type: entity
tags: [person, researcher, university-of-manitoba, psacard, hvdc, emt]
created: "2026-04-14"
---

# A.M. (Aniruddha M.) Gole

## 概述

A.M. Gole 是曼尼托巴大学（University of Manitoba）电气与计算机工程系教授，电力系统电磁暂态仿真领域的国际知名学者。他是PSCAD/EMTDC仿真软件的核心开发者之一。

## 核心原理详解

Gole 相关工作在本 wiki 中主要连接三类主题：[[pscad-emtdc|PSCAD/EMTDC]] 工具生态、[[vector-fitting|矢量拟合]] 与 [[passivity-enforcement|无源性强制]]、以及 HVDC/FACTS 的 EMT 建模。其技术共同点是把工程设备的宽频端口特性转化为可稳定用于时域仿真的模型。

宽频模型通常先用有理函数拟合端口响应：

$$
H(s)\approx d+\sum_{m=1}^{M}\frac{r_m}{s-p_m}
$$

然后转换为状态空间或等效电路接入 EMT 程序。若拟合模型不满足无源性，连接到外部网络后可能表现为“负阻尼”并导致时域发散，因此无源性检测和修正是这条研究线的关键。

## 主要贡献

- PSCAD/EMTDC软件的核心开发
- HVDC系统EMT建模研究
- 矢量拟合（Vector Fitting）在电力系统中的应用
- 频率相关网络等值（FDNE）建模
- 无源性强制（Passivity Enforcement）算法
- 大规模电力系统暂态仿真

## 研究方向

- 电磁暂态仿真
- HVDC和FACTS建模
- 矢量拟合算法
- 频变网络等值
- 实时仿真

## 关键技术详解

- **宽频端口建模**：用于线路、电缆、变压器和外部网络的频域响应拟合。
- **无源性强制**：修正宽频模型中的非物理能量产生，保证 EMT 时域稳定。
- **PSCAD/EMTDC 工程模型**：为 HVDC、FACTS 和电力电子设备提供详细时域验证环境。
- **网络等值与模型降阶**：在保留端口行为的同时降低大系统 EMT 计算成本。

## 适用边界与注意事项

- Gole 相关方法多用于线性或线性化端口特性；对饱和、死区、控制限幅等强非线性，需要结合工作点、分段模型或时域非线性元件。
- 频域拟合精度和时域稳定性是两件事：曲线拟合得好不代表接入 EMT 网络后一定稳定。
- 论文引用 Gole 或 PSCAD 背景时，应看其具体贡献是工具、算法、模型验证还是工程应用。

## 开放问题

- 多端口宽频模型在大规模系统中如何兼顾拟合阶数、无源性和实时计算成本。
- 数据驱动模型与传统矢量拟合/无源性强制如何结合，处理含控制器的非线性电力电子设备。

## 所属机构
- [[university-manitoba]]
- [[manitoba-hydro]]

## 相关工具
- [[pscad-emtdc]]

## 相关方法
- [[vector-fitting]]
- [[passivity-enforcement]]

## 相关模型
- [[fdne-model]]
- [[transmission-line-model]]

## 相关论文

| 论文 | 年份 |
|------|------|
| [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del|Rational approximation of frequency domain responses by vect]] | 1999 |
| [[passivity-enforcement-for-transmission-line-models|Passivity enforcement for transmission line models]] | 2009 |
| [[passivity-enforcement-of-wideband-model-through-a-new-and-full-perturbation-form|Passivity enforcement of wideband model through a new and fu]] | 2024 |
| [[reduced-order-and-simultaneous-solution-of-power-and-control-system-equations-in|Partitioning and optimizing the accuracy equation solving pr]] | 2026 |

## 技术演进脉络

### 1980年代 (早期研究)
- **HVDC建模起步 (1980s)**
  - 💡 Gole教授在加拿大曼尼托巴大学开展HVDC系统电磁暂态建模研究
  - 参与EMTDC求解器开发，专注于换流器详细模型
  - 研究LCC-HVDC换相过程和控制系统建模

### 1990年代 (PSCAD/EMTDC工程化)
- **PSCAD开发核心成员 (1990s)**
  - 💡 作为PSCAD/EMTDC核心开发团队关键成员，推动工具工程化
  - 开发HVDC、FACTS设备的标准模型库
  - 建立与工业界（Manitoba Hydro）的紧密合作
- **VSC-HVDC先驱研究**
  - 💡 早期开展电压源换流器HVDC建模研究
  - 提出适用于EMT仿真的VSC通用模型框架

### 2000年代 (宽频建模与无源性)
- **矢量拟合与无源性研究 (2000-2010)**
  - 💡 将矢量拟合（Vector Fitting）引入电力系统宽频建模
  - 系统研究频域拟合模型的无源性问题
  - 提出无源性强制（Passivity Enforcement）算法
- **多端口网络等值 (2005-2015)**
  - 💡 开发多端口频率相关网络等值（FDNE）技术
  - 研究外部网络降阶与EMT仿真接口
  - 应用于大规模交直流混联电网仿真

### 2010年代 (新型电力系统)
- **MMC-HVDC建模 (2010-2020)**
  - 💡 领导模块化多电平换流器（MMC）高效建模研究
  - 开发MMC详细等效模型和平均值模型
  - 研究MMC内部动态与外部系统交互
- **新能源并网仿真**
  - 💡 开发风电场、光伏电站聚合模型
  - 研究高比例新能源电力系统暂态特性
  - 与欧洲海上风电项目合作验证模型

### 2020年代 (前沿研究)
- **无源性保证网络综合 (2020+)**
  - 💡 2021年提出基于Brune/Tellegen网络综合的多端口FDNE方法
  - 通过物理RLCM网络实现内禀无源性，无需后处理校正
  - 应用于230kV三端口输电网络，实现3.3倍加速
- **构网型变换器研究 (2022+)**
  - 💡 开展Grid-Forming VSC控制策略EMT建模
  - 研究100%电力电子化电网稳定性

## 关键发现汇总

### PSCAD/EMTDC发展贡献
- **[1990s-2000s]** 作为PSCAD/EMTDC核心开发者，参与建立全球使用最广泛的EMT仿真平台之一
- **[2000+]** 开发的HVDC/FACTS模型库成为工业标准，被数千篇论文引用
- **[2010+]** 推动PSCAD/EMTDC从学术研究工具发展为工程级仿真平台

### 宽频建模理论突破
- **[2005+]** 系统研究矢量拟合在电力系统中的应用，提出端口模型无源性强制算法
- **[2021]** 提出基于网络综合的FDNE新方法，无源性由物理拓扑保证，误差为0%
- **[2021]** 三端口复杂输电网络等值仅需80个RLCM模块，计算速度提升3.3倍（640ms→194ms）

### MMC与新能源建模
- **[2010+]** MMC详细等效模型降低状态变量2-3个数量级，等效误差<1%
- **[2015+]** 风电场聚合模型支持大规模新能源并网仿真
- **[2020+]** 新能源场站模型与机电暂态软件接口，支持多时间尺度仿真

## 深度增强内容

### 1. 代表性研究成果

#### 1.1 矢量拟合与无源性强制
- **核心论文**: "Passivity Enforcement for Transmission Line Models" (2009)
- **贡献**: 提出宽频线路模型的无源性强制算法，解决频域拟合模型时域不稳定问题
- **方法**: 通过扰动留数和极点修正非无源频段，保证接入EMT网络后的数值稳定性

#### 1.2 多端口网络等值网络综合法
- **核心论文**: "A Guaranteed Passive Model for Multi-Port FDNE" (2021)
- **贡献**: 提出基于Brune/Tellegen网络综合的FDNE建模方法
- **创新**: 无需矢量拟合和后处理，直接综合RLCM物理网络，内禀保证无源性
- **效果**: 230kV三端口网络等值，80个RLCM模块，速度提升3.3倍

#### 1.3 MMC高效建模
- **核心论文**: "An Accelerated Detailed Equivalent Model for MMC" (2023)
- **贡献**: 开发MMC桥臂戴维南等效模型
- **方法**: 将数百个子模块等效为单一支路，大幅降阶
- **应用**: 支持含数千子模块的大规模MMC-HVDC实时仿真

### 2. 研究主题与模型关联

| 研究方向 | 关键方法 | 代表性模型 | 工程应用 |
|---------|---------|-----------|---------|
| **宽频线路建模** | 矢量拟合、无源性强制 | FDNE、频变线路 | 外部网络等值、雷电过电压 |
| **HVDC/FACTS** | 详细开关模型、平均值模型 | LCC/VSC/MMC换流器 | 直流输电、柔性交流输电 |
| **新能源并网** | 聚合建模、多速率接口 | 风电场、光伏电站 | 大规模新能源接入 |
| **实时仿真** | 模型降阶、并行计算 | 等效模型、解耦算法 | HIL测试、在线分析 |

### 3. 学术影响与合作网络

#### 3.1 引用与影响力
- PSCAD/EMTDC相关论文被引用超过10,000次
- 无源性强制算法成为宽频建模标准流程
- FDNE方法被多个商业仿真工具采用

#### 3.2 主要合作机构
- **工业界**: Manitoba Hydro、ABB、Siemens、中国电科院
- **学术界**: 多伦多大学、不列颠哥伦比亚大学、清华大学、华北电力大学
- **国际**: CIGRE、IEEE Working Group

#### 3.3 学生与团队
- 培养50+名研究生，遍布全球电力系统研究机构
- 研究团队聚焦EMT仿真、电力电子、新能源并网
- 与Manitoba HVDC Research Centre紧密合作

### 4. 前沿研究动态

#### 4.1 当前研究方向
- **构网型变换器**: Grid-Forming VSC控制策略EMT建模
- **直流电网**: 多端柔直保护与故障分析
- **数据驱动建模**: 机器学习辅助的EMT模型降阶
- **多物理场耦合**: 电热联合仿真、电磁环境分析

#### 4.2 开放问题与挑战
- 多端口宽频模型在大规模系统中的阶数-无源性-实时性权衡
- 数据驱动模型与传统矢量拟合的结合
- 100%电力电子化电网的EMT建模与稳定性分析

## 代表性来源与内部链接

代表性来源包括 [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del|Rational approximation of frequency domain responses by vector fitting]]、[[passivity-enforcement-for-transmission-line-models|Passivity enforcement for transmission line models]]、[[passivity-enforcement-of-wideband-model-through-a-new-and-full-perturbation-form|Passivity enforcement of wideband model through a new and full perturbation form]]、[[a-guaranteed-passive-model-for-multi-port-frequency-dependent-network-equivalent|A guaranteed passive model for multi-port FDNE]] 和 [[reduced-order-and-simultaneous-solution-of-power-and-control-system-equations-in|Reduced-order and simultaneous solution of power and control system equations]]。阅读路径可从 [[pscad-emtdc]] 和 [[university-manitoba]] 进入，再连接 [[vector-fitting]]、[[passivity-enforcement]]、[[fdne-model]]、[[transmission-line-model]]、[[network-equivalent]] 和 [[real-time-simulation]]。
