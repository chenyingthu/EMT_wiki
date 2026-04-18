---
title: "Comparison of Detailed Modeling Techniques for MMC Employed on VSC-HVDC Schemes"
type: source
authors: ['未知']
year: 2015
journal: "IEEE Transactions on Power Delivery;2015;30;2;10.1109/TPWRD.2014.2325065"
tags: ['mmc', 'vsc']
created: "2026-04-13"
sources: ["EMT_Doc/10/Beddard 等 - 2015 - Comparison of Detailed Modeling Techniques for MMC Employed on VSC-HVDC Schemes.pdf"]
---

# Comparison of Detailed Modeling Techniques for MMC Employed on VSC-HVDC Schemes

**作者**: 
**年份**: 2015
**来源**: `10/Beddard 等 - 2015 - Comparison of Detailed Modeling Techniques for MMC Employed on VSC-HVDC Schemes.pdf`

## 摘要

—Modular multilevel converters (MMC) are presently the converter topology of choice for voltage-source converter high-voltage direct-current (VSC-HVDC) transmission schemes due to their very high efﬁciency. These converters are complex, yet fast and detailed electromagnetic transients simulation models are necessary for the research and development of these transmis- sion schemes. Excellent work has been done in this area, though little objective comparison of the models proposed has yet been undertaken. This paper compares for the ﬁrst time, the three leading techniques for producing detailed MMC VSC-HVDC models in terms of their accuracy and simulation speed for sev- eral typical simulation cases. In addition, an improved model is proposed which further improves the computational efﬁcien

## 核心贡献


- 首次在同一平台客观对比TDM、DEM与AM三种MMC详细模型的精度与仿真速度
- 提出增强型加速模型EAM，通过优化网络划分进一步提升MMC电磁暂态仿真计算效率
- 基于对比实验结果，给出针对不同研究场景的MMC详细模型选型建议与适用指南


## 使用的方法


- [[传统详细建模-tdm|传统详细建模(TDM)]]
- [[详细等效建模-dem|详细等效建模(DEM)]]
- [[加速建模-am|加速建模(AM)]]
- [[嵌套快速同步求解-nfss|嵌套快速同步求解(NFSS)]]
- [[节点导纳矩阵求解|节点导纳矩阵求解]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[vsc-model|VSC]]
- [[半桥子模块|半桥子模块]]
- [[桥臂电抗器|桥臂电抗器]]
- [[igbt-反并联二极管|IGBT/反并联二极管]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[vsc-model|VSC]]
- [[仿真效率优化|仿真效率优化]]
- [[模型精度对比|模型精度对比]]
- [[电力电子详细建模|电力电子详细建模]]


## 主要发现


- DEM相比TDM大幅缩短仿真时间且精度无损，但无法观测子模块内部电气状态
- AM在保持组件可见性的同时显著提升计算效率，但特定工况下存在数值稳定性局限
- 提出的EAM进一步优化了AM的求解结构，在典型测试案例中实现仿真速度再提升



## 方法细节

### 方法概述

本文系统对比了三种MMC电磁暂态详细建模技术：传统详细模型(TDM)、详细等效模型(DEM)与加速模型(AM)，并提出增强型加速模型(EAM)。TDM在仿真界面直接搭建所有IGBT、反并联二极管与子模块(SM)电容，形成大型节点导纳矩阵，每开关周期求逆，计算负担极重。DEM基于嵌套快速同步求解(NFSS)原理，将每个桥臂划分为独立子网络，分别求解小型导纳矩阵，大幅降低矩阵维度但隐藏SM内部状态。AM采用混合架构，将桥臂等效为受控电压源，各SM被分离并由等于桥臂电流的电流源独立驱动，分别求解SM导纳矩阵，保留SM可访问性。针对AM在换流器闭锁时二极管状态判定存在单步延迟的缺陷，提出EAM，将多个SM（如5、10或30个）合并为一个子网络，在增加单次矩阵规模的同时显著减少求解步数，兼顾计算效率与数值稳定性。

### 数学公式


**公式1**: $$$v_{arm} = N_{on} \cdot v_{c}$$$

*桥臂输出电压方程，表示桥臂电压等于投入的子模块数量与单个SM电容电压的乘积，用于电平控制与调制*


**公式2**: $$$v_{c}(t) = v_{c}(t_0) + \frac{1}{C} \int_{t_0}^{t} i_{arm}(\tau) d\tau$$$

*SM电容电压动态方程，在电容足够大且电压均衡假设下，描述电容电压随桥臂电流积分的变化规律*


**公式3**: $$$v_{eq} = \sum_{k=1}^{N} v_{sm,k}$$$

*AM等效受控电压源方程，将桥臂内所有SM的实时电容电压求和，作为替代SM串的受控电压源输入主网络*


**公式4**: $$$V_{dc} = v_{u} + v_{l} + L_{arm} \frac{d(i_{u}+i_{l})}{dt}$$$

*直流侧电压平衡方程，用于推导环流抑制控制器(CCSC)，通过调节上下桥臂电压差抑制二倍频负序环流*


### 算法步骤

1. 网络初始化与拓扑划分：根据所选模型(TDM/DEM/AM/EAM)确定网络分割策略。TDM保持全连接；DEM按上下桥臂划分独立子网络；AM/EAM按单个或分组SM划分独立子网络，并配置等效受控源与电流源接口。

2. 边界状态采样：在每个仿真步长($\Delta t$)开始时，测量主电路的桥臂电流$i_{arm}$与节点电压，作为各子网络求解的边界激励条件。

3. 等效源参考值更新：对于AM/EAM，将采样到的$i_{arm}$赋值给驱动各SM子网络的电流源；将各SM电容电压求和赋值给桥臂等效受控电压源$v_{eq}$，实现主从网络解耦。

4. 子网络独立求解：利用梯形积分法构建各子网络的节点导纳矩阵$Y_{sub}$与历史电流源向量$I_{hist}$，求解线性方程组$Y_{sub} \cdot V_{sub} = I_{hist}$，获取当前时刻子网络内部节点电压与支路电流。

5. 状态同步与时间推进：将各子网络求解结果反馈至主网络接口，检查功率/电流收敛性。若收敛则将状态变量存入历史缓存，更新开关器件状态（IGBT/二极管），推进至下一时间步。

6. 闭锁与故障逻辑处理：当触发闭锁信号时，强制关断所有IGBT，根据瞬时电流方向判定反并联二极管导通状态。EAM通过分组求解降低单步延迟影响，提升闭锁工况下的数值稳定性。


### 关键参数

- **仿真步长**: 20 μs

- **MMC电平数**: 16/31/61级

- **子模块电容纹波设计值**: 10%

- **桥臂电抗器限制故障电流上升率**: ≤20 A/μs

- **环流抑制目标**: ≈0.15 p.u.

- **交流系统短路比(SCR)**: 3.5

- **直流电缆参数**: 300 kV, 100 km XLPE

- **仿真时长**: 5 s

- **硬件平台**: Intel Core i7-2860QM 2.5GHz, 8GB RAM



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 稳态运行(1000/500/100 MW) | DEM与AM波形与TDM高度重合，归一化平均绝对误差(MAE)普遍<1%，输出相电压总谐波畸变率(THD)稳定在1.35%~1.36%。低功率工况下因开关噪声占比增加，MAE略有上升但仍在1%以内。 | DEM与AM精度无损，THD与TDM一致(1.35%~1.36%) |

| 直流极间故障(4.5s施加, 2ms后DCCB断开) | DEM与AM的归一化MAE分别<1%与<2.5%。AM在桥臂电流过零瞬间因二极管状态判定延迟产生微小电压偏差，但整体故障电流波形与TDM高度吻合。 | DEM误差<1%，AM误差<2.5%，AM在电流过零闭锁时存在单步判定延迟 |

| 交流单相接地故障(PCC处持续60ms) | DEM与AM的MAE均<1%与<2.5%。故障清除后数周期内MMC进入过调制，AM桥臂电流波形出现轻微畸变，但峰值电流与TDM完全一致，不影响保护定值评估。 | 暂态峰值电流一致，AM在过调制恢复期存在<2.5%的波形偏差 |

| 不同电平数仿真耗时对比(61级) | DEM耗时仅为TDM的1/43，AM为TDM的1/14。将AM中的SM按30个分组(EAM)后，求解步数显著减少，运行时间较单SM分组(AM1)进一步缩短，且未引入明显精度损失。 | 61级MMC下，DEM比TDM快43倍，AM比TDM快14倍，EAM分组策略可进一步优化AM速度 |



## 量化发现

- 61级MMC仿真中，DEM计算速度比TDM快43倍，AM比TDM快14倍
- 稳态工况下，DEM与AM相对于TDM的归一化MAE均严格小于1%
- 暂态故障工况下，DEM与AM的归一化MAE控制在2.5%以内
- MMC输出相电压稳态THD为1.35%~1.36%，三种模型谐波特性一致
- AM模型在换流器闭锁且桥臂电流反向时，存在单步时间延迟导致的二极管导通状态误判误差
- 将AM中的子模块按5、10或30个分组构建子网络(EAM)，可在牺牲极小精度的前提下显著降低求解步数并提升仿真速度


## 关键公式

### 桥臂输出电压方程

$$$v_{arm} = N_{on} \cdot v_{c}$$$

*用于描述桥臂投入子模块数量与单个SM电容电压的乘积关系，是最近电平逼近调制(NLC)与电压控制的基础*

### AM等效受控电压源方程

$$$v_{eq} = \sum_{k=1}^{N} v_{sm,k}$$$

*在加速模型中替代串联SM串，将各SM实时电压求和作为桥臂等效电压源输入主网络，实现网络降维*

### 直流侧电压平衡方程

$$$V_{dc} = v_{u} + v_{l} + L_{arm} \frac{d(i_{u}+i_{l})}{dt}$$$

*用于推导环流抑制控制器(CCSC)，通过控制上下桥臂电压差抑制二倍频负序环流，降低附加损耗*

### 子网络节点导纳方程

$$$Y_{sub} \cdot V_{sub} = I_{hist,sub}$$$

*DEM与AM/EAM在每个时间步独立求解各子网络的核心线性方程组，矩阵规模直接决定计算效率*



## 验证详情

- **验证方式**: 电磁暂态(EMT)数字仿真对比分析，以TDM为精度基准，通过稳态与多种暂态故障场景进行交叉验证
- **测试系统**: 31级MMC VSC-HVDC测试系统（扩展至16级与61级进行速度评估），交流侧SCR=3.5，直流侧为300kV/100km XLPE电缆，配备最近电平逼近调制(NLC)、解耦电流控制、外环功率控制及环流抑制控制器(CCSC)
- **仿真工具**: PSCAD/EMTDC (X4版本)，运行于Windows 7系统，Intel Core i7-2860QM 2.5GHz处理器，8GB RAM
- **验证结果**: 验证表明DEM在计算效率与精度上综合最优，但无法观测SM内部状态；AM保留了SM可访问性且速度显著优于TDM，但在闭锁工况下存在二极管状态判定延迟缺陷；提出的EAM通过SM分组策略有效优化了AM的求解步数与稳定性。研究为不同应用场景（如控制保护研究需SM访问选AM/EAM，纯系统级研究选DEM）提供了明确的模型选型依据。
