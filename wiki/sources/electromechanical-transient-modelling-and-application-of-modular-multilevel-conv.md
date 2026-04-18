---
title: "Electromechanical transient modelling and application of modular multilevel converter with embedded energy storage"
type: source
authors: ['未知']
year: 2021
journal: "IET Generation Trans & Dist 2022.16:123-136"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/17/Yu 等 - 2022 - Electromechanical transient modelling and application of modular multilevel converter with embedded.pdf"]
---

# Electromechanical transient modelling and application of modular multilevel converter with embedded energy storage

**作者**: 
**年份**: 2021
**来源**: `17/Yu 等 - 2022 - Electromechanical transient modelling and application of modular multilevel converter with embedded.pdf`

## 摘要

This paper studies the electromechanical transient modelling techniques of the modiﬁed modular multilevel converter (MMC), named active MMC, which is equipped with embed- ded energy storage in submodules. Firstly, the mathematical model of the active MMC and its equivalent circuits at the AC and DC sides are established. Then, the control scheme of active MMC that focus on the cooperation of the MMC converter and the energy stor- age submodules is illustrated. The proposed electromechanical transient model are imple- mented on PSS/E and compared with the electromagnetic transient model on PSCAD in a two terminal active MMC sytem; the results of the active MMC system under AC and DC fault prove the validity of the proposed model. Lastly, stability studies of the practical sys- tem are carri

## 核心贡献


- 推导含储能MMC机电暂态模型，直流侧引入附加电流源模拟储能动态响应
- 提出换流器与储能子模块协同控制策略，实现交直流故障下的功率解耦
- 在PSS/E平台实现模型并与PSCAD对比，验证功角与频率稳定性提升


## 使用的方法


- [[机电暂态建模|机电暂态建模]]
- [[矢量控制|矢量控制]]
- [[一阶惯性等效|一阶惯性等效]]
- [[等效电路法|等效电路法]]
- [[电磁暂态对比验证|电磁暂态对比验证]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[储能子系统-ess|储能子系统(ESS)]]
- [[双向dc-dc变换器|双向DC-DC变换器]]
- [[两端直流输电系统|两端直流输电系统]]


## 相关主题


- [[机电暂态仿真|机电暂态仿真]]
- [[mmc-model|MMC]]
- [[暂态稳定性分析|暂态稳定性分析]]
- [[故障穿越|故障穿越]]
- [[交直流系统解耦|交直流系统解耦]]


## 主要发现


- 所提机电暂态模型在交直流故障下的动态响应与PSCAD电磁暂态模型高度吻合
- 嵌入式储能有效解耦交直流功率耦合，显著抑制故障在异步电网间的传播
- 含储能MMC的应用显著提升了实际电力系统的功角稳定性与频率稳定性



## 方法细节

### 方法概述

本文针对含嵌入式储能子模块的改进型MMC（Active MMC）提出了一套完整的机电暂态建模与仿真方法。首先，基于基频等效原理与交流侧矢量控制特性，建立交流侧诺顿等效电路模型，实现有功/无功解耦控制。其次，在直流侧将大量子模块电容等效为集中参数电容，并创新性地引入附加受控电流源以表征储能系统的动态功率补偿特性。模型采用离散时间状态空间方程描述多端直流网络，结合数值积分法求解，并支持直流断路器动作、线路投切等拓扑动态重构。最后，在PSS/E平台实现该机电暂态模型，通过PSCAD/EMTDC电磁暂态模型进行交叉验证，并应用于实际交直流混联大电网的功角与频率稳定性分析，验证了模型在交直流故障下的准确性与工程适用性。

### 数学公式


**公式1**: $$$i_{sd} = \frac{P_s}{u_{sd}}$$$

*交流侧d轴诺顿等效注入电流计算，用于网络代数方程求解*


**公式2**: $$$i_{sq} = \frac{Q_s}{u_{sq}}$$$

*交流侧q轴诺顿等效注入电流计算，实现无功/电压控制*


**公式3**: $$$C_{eq} = \frac{6}{N_{SM}} C_{SM}$$$

*直流侧等效集中电容计算，聚合所有子模块电容动态*


**公式4**: $$$i_{sci} = \frac{P_{si} - i_{si}^2 R_{eq}}{U_{dci}}$$$

*直流侧换流器等效电流源，反映交直流侧功率平衡与损耗*


**公式5**: $$$P_{si} = \frac{3}{2}(u_{sdi}i_{sdi} + u_{sqi}i_{sqi})$$$

*交流侧瞬时有功功率计算*


**公式6**: $$$i_{si} = \sqrt{\frac{3}{2}(i_{sdi}^2 + i_{sqi}^2)}$$$

*交流侧电流幅值计算，用于直流侧电流源修正*


### 算法步骤

1. 步骤1：基于矢量控制架构建立交流侧基频等效模型，将d/q轴有功与无功功率指令解耦，通过内环电流控制器生成参考电流。

2. 步骤2：根据PCC点电压与注入功率计算交流侧诺顿等效注入电流（$i_{sd}, i_{sq}$），并将其从旋转坐标系变换至静止坐标系以匹配电网代数方程。

3. 步骤3：构建直流侧等效电路，将每相$N_{SM}$个子模块电容聚合为集中等效电容$C_{eq}$，直流线路采用$\Pi$型RLC集中参数模型表示。

4. 步骤4：推导直流侧换流器等效受控电流源$i_{sci}$，通过交流侧注入功率$P_{si}$与线路损耗$i_{si}^2 R_{eq}$计算直流侧功率平衡关系。

5. 步骤5：引入储能附加电流源$i_{esi}$，通过外环功率/电压控制器与一阶惯性等效内环电流控制器协同调节，实现交直流故障下的功率解耦与动态补偿。

6. 步骤6：将交直流侧模型耦合，形成完整的机电暂态状态空间方程，采用数值积分法进行离散化求解，并根据直流断路器动作与故障清除实时更新网络关联矩阵。

7. 步骤7：在PSS/E平台中部署模型，设置故障时序（如交流三相短路0.1s、直流接地故障100ms），输出动态响应曲线并与PSCAD/EMTDC电磁暂态结果进行逐点对比验证。


### 关键参数

- **交流系统额定电压**: 220 kV

- **额定直流电压**: 400 kV

- **MMC额定容量**: 400 MVA

- **桥臂电抗**: 76 mH

- **每桥臂子模块数**: 250

- **子模块电容**: 8334 µF

- **储能电池组额定电压/电流**: 1 kV / 0.34 kA

- **电池串并联配置**: 270串34并

- **直流线路长度**: 100 km

- **直流线路电阻/电感/电容**: 0.0114 Ω/km / 0.9356 mH/km / 0.0123 µF/km

- **DC-DC变换器开关频率**: 750 Hz



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 交流侧三相短路故障 | 在t=2.0s对AC-1母线2施加0.1s三相短路故障。Active MMC通过储能补偿有功功率，直流电压维持恒定，受端AC-2发电机功角摆动幅度显著减小。PSS/E机电暂态仿真10s耗时仅125ms，与PSCAD电磁暂态结果高度吻合。 | 相比传统MMC需降功率维持直流电压，Active MMC实现交直流故障隔离；仿真速度提升超250倍（PSCAD耗时32s vs PSS/E耗时125ms）。 |

| 直流侧单极接地故障 | 在t=0.5s于线路中点施加接地故障，持续100ms，t=0.820s故障清除并重合闸。传统MMC直流功率传输中断导致交流系统功率骤降；Active MMC储能迅速补偿不平衡功率，维持换流站与交流系统功率交换不变，两端发电机功角摆动范围大幅收敛。 | 传统MMC故障后交流侧功率交换迅速降至零，引发系统失稳；Active MMC通过储能补偿实现直流故障对交流侧的完全隔离，功角稳定性显著提升。 |

| 大电网交直流混联系统直流永久故障 | 基于2030年南方电网四省同步互联规划，模拟云广直流线路永久开断。传统MMC导致送端功率过剩、受端缺额，跨省交流线路潮流越限并引发云南-广东功角失稳；Active MMC储能提供分钟级额定功率补偿，保持交流潮流基本不变，避免功角失稳。 | 传统方案引发跨省交流线路潮流越限与功角失稳；Active MMC方案通过储能阶梯式降功率控制，实现频率与功角双重稳定，验证了分钟级功率补偿的工程可行性。 |



## 量化发现

- 机电暂态仿真速度较电磁暂态提升超250倍（10s仿真：PSS/E耗时125ms，PSCAD耗时32s）
- 交流侧故障持续时间0.1s，直流侧故障持续时间100ms，故障清除时刻为t=0.820s
- 直流侧等效电容计算公式为$C_{eq} = \frac{6}{N_{SM}} C_{SM}$，本例中$N_{SM}=250$，$C_{SM}=8334 \mu F$
- 储能电池组采用270串34并配置，额定电压1kV，额定电流0.34kA，满足分钟级额定功率补偿需求
- 直流线路参数：长度100km，电阻0.0114Ω/km，电感0.9356mH/km，电容0.0123μF/km
- Active MMC在交直流故障下动态响应曲线与PSCAD电磁暂态模型误差极小，验证了附加电流源等效方法的精度


## 关键公式

### 直流侧等效集中电容公式

$$$C_{eq} = \frac{6}{N_{SM}} C_{SM}$$$

*用于机电暂态模型中聚合所有子模块电容，简化直流侧动态计算*

### 直流侧换流器等效电流源公式

$$$i_{sci} = \frac{P_{si} - i_{si}^2 R_{eq}}{U_{dci}}$$$

*反映交直流侧功率平衡关系，用于计算直流网络注入电流*

### 交流侧诺顿等效注入电流公式

$$$i_{sd} = \frac{P_s}{u_{sd}}, \quad i_{sq} = \frac{Q_s}{u_{sq}}$$$

*将MMC交流侧等效为电流源注入电网，用于机电暂态网络代数方程求解*



## 验证详情

- **验证方式**: 机电暂态与电磁暂态交叉对比仿真验证
- **测试系统**: 两端MMC-HVDC系统（连接两个四机交流系统）及2030年南方电网四省同步互联规划大电网
- **仿真工具**: PSS/E（机电暂态仿真平台），PSCAD/EMTDC（电磁暂态仿真平台）
- **验证结果**: 在交流三相短路（0.1s）与直流接地故障（100ms）工况下，PSS/E机电暂态模型输出的有功功率、直流电压/电流、发电机功角等动态响应曲线与PSCAD电磁暂态结果高度一致。验证了所提等效电路与附加电流源建模方法的准确性，并证明Active MMC在交直流故障隔离、功角稳定与频率辅助控制方面具有显著优势。
