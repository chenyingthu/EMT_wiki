---
title: "Modeling A Mixed Residential-commercial Load  For Simulations Involving Large Disturbances - Power Systems, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/26/Khodabakhchian - 1997 - Modeling a mixed residential-commercial load for simulations involving large disturbances.pdf"]
---

# Modeling A Mixed Residential-commercial Load  For Simulations Involving Large Disturbances - Power Systems, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `26/Khodabakhchian - 1997 - Modeling a mixed residential-commercial load for simulations involving large disturbances.pdf`

## 摘要

A detailed EMTP model of a mixed residential-commercial load valid for large voltage variations has been developed. Once validated against field recordings, the model has been used to study the static, dynamic and post-fault recovery characteristics of the real load. From the simulation results, guidelines for modeling this type of load in dynamic studies such as first swing, transient and voltage stability were established. It is expected that the same methodology applied to other loads of reasonably known composition would guarantee more realistic results than those obtained with current practices. Keywords: Load Modeling, LOADSYN, EMTP Simulation, Transient Stability . INTRODUCTION It has been well established that the load characteristics have a major effect on machine-network interact

## 核心贡献


- 开发适用于大电压波动的EMTP混合负荷模型，突破传统模型窄范围限制
- 利用现场单相接地故障录波验证模型，实现大扰动下负荷动态特性的高精度还原
- 制定混合负荷在暂态与电压稳定研究中的建模指南，提升电力系统动态仿真精度


## 使用的方法


- [[emtp电磁暂态仿真|EMTP电磁暂态仿真]]
- [[基于组件的负荷建模|基于组件的负荷建模]]
- [[现场录波数据辨识|现场录波数据辨识]]
- [[静态与动态负荷建模|静态与动态负荷建模]]
- [[通用机电模型-um-7-um-40|通用机电模型(UM-7/UM-40)]]


## 涉及的模型


- [[混合居民-商业负荷|混合居民-商业负荷]]
- [[恒阻抗负荷|恒阻抗负荷]]
- [[非线性负荷|非线性负荷]]
- [[电压频率相关负荷|电压频率相关负荷]]
- [[单相感应电机|单相感应电机]]
- [[三相感应电机|三相感应电机]]
- [[配电变压器饱和模型|配电变压器饱和模型]]


## 相关主题


- [[负荷建模|负荷建模]]
- [[大扰动仿真|大扰动仿真]]
- [[暂态稳定分析|暂态稳定分析]]
- [[电压稳定分析|电压稳定分析]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[现场数据验证|现场数据验证]]


## 主要发现


- EMTP单相电机模型在大转差率下转矩特性更真实，克服了传统单笼模型局限
- 三相电机静态特性在宽电压范围外迅速发散，证实了扩展负荷模型适用域的必要性
- 复合模型精准复现严重单相接地故障期间的功率动态，验证了大扰动仿真的有效性



## 方法细节

### 方法概述

采用基于组件的负荷建模方法（Component-based Load Modeling），基于LOADSYN数据库和模型库，使用EMTP电磁暂态仿真程序建立混合居民-商业负荷的详细模型。针对大扰动场景（电压变化高达50%），分别构建三类静态负荷模型（恒阻抗、非线性、电压频率相关）和两类动态负荷模型（单相感应电机、三相感应电机）。通过调整EMTP通用电机模型UM-7（单相）和UM-40（三相）的参数，使其在额定转差率附近匹配LOADSYN的功率因数、额定转差率和转速-转矩曲线特性。模型特别考虑了配电变压器饱和（使用EMTP模型98）和单相电机在大转差率下的零起动转矩特性，突破了LOADSYN原有限制（电压变化<15%，频率变化<5%）。

### 数学公式


**公式1**: $$$P = P_0 \left(\frac{V}{V_0}\right)^{n_p} \left[1 + K_p\frac{f-f_0}{f_0}\right]$$$

*电压频率相关负荷的有功功率计算式，其中P0为额定有功功率，V/V0为电压标幺值，np为有功功率电压指数，Kp为频率有功系数，f0为额定频率*


**公式2**: $$$Q = Q_0 \left(\frac{V}{V_0}\right)^{n_q} \left[1 + K_q\frac{f-f_0}{f_0}\right]$$$

*电压频率相关负荷的无功功率计算式，其中Q0为额定无功功率，nq为无功功率电压指数，Kq为频率无功系数*


### 算法步骤

1. 基于LOADSYN数据库确定混合负荷的组成比例（居民-商业混合负荷占Hydro-Quebec总负荷的2/3以上）

2. 建立静态负荷子模型：恒阻抗负荷（水加热器、电炉等）使用线性RLC电路；非线性负荷（配电变压器饱和）使用EMTP模型98；电压频率相关负荷（电视机、荧光灯）使用被动元件和受控电流源

3. 建立动态负荷子模型：单相感应电机（冰箱等家用电器）采用EMTP UM-7模型，调整参数使在额定转差率附近匹配LOADSYN的功率因数、额定转差率和转速-转矩曲线；三相感应电机采用EMTP UM-40模型

4. 进行电压扫描测试：电压从1.0 pu升至1.5 pu（上升支），再降至0.5 pu（下降支），变化速率为-1 pu/秒，获取P-Q静态特性曲线

5. 在EMTP中搭建Brossard变电站（315/25 kV）的完整仿真模型，通过径向线路连接至Boucherville变电站（735/315 kV）

6. 利用现场录波数据（单相接地故障）进行模型验证，对比正序电压、有功功率和无功功率的仿真值与实测值

7. 分析负荷的静态特性、动态响应特性和故障后恢复特性，建立暂态稳定研究中的负荷建模指导原则


### 关键参数

- **电压变化范围**: 0.5 pu 至 1.5 pu（即50%电压跌落至150%电压升高）

- **频率变化范围**: 额定频率±5%以上（本研究中f=f0，频率变化可忽略）

- **故障正序电压跌落**: 17.5%

- **故障相电压跌落**: 36%

- **健康相电压跌落**: 8%

- **故障持续时间**: 2.5周波（约41.67 ms，基于60Hz系统）

- **电压扫描速率**: -1 pu/秒

- **监测周期**: 两年（1979年开始的监测系统）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Brossard变电站单相接地故障大扰动验证 | 故障期间正序电压从1.0 pu跌落至0.825 pu（17.5%跌落），故障相（C相）电压从1.0 pu跌落至0.64 pu（36%跌落），两健康相电压从1.0 pu跌落至0.92 pu（8%跌落）。有功功率从约300 MW降至240 MW，无功功率从约50 MVAr降至-50 MVAr。模型成功复现了故障期间（2.5周波）的功率动态变化和故障后的恢复过程。 | 与现场录波数据对比，EMTP模型在电压跌落17.5%和大转差率工况下的精度显著优于传统LOADSYN模型（后者仅保证<15%电压变化范围内的精度） |

| 单相感应电机静态特性验证 | 在0.5-1.5 pu电压范围内，EMTP单相电机模型（UM-7）的P-Q特性曲线与LOADSYN数据在额定转差率附近吻合良好。特别在大转差率区域，EMTP模型显示出单相电机特有的零起动转矩特性，而LOADSYN采用三相电机近似无法体现此特性。 | 在0.35-1.15 pu范围外，LOADSYN模型失效，而EMTP模型在0.5-1.5 pu全范围内保持物理一致性 |



## 量化发现

- 模型有效电压范围：0.5-1.5 pu（相对额定电压±50%），较LOADSYN原有范围（0.85-1.15 pu，即±15%）扩展了233%
- 验证案例电压跌落幅度：正序电压17.5%，故障相电压36%，健康相电压8%
- 故障持续时间：2.5周波（基于60Hz系统为41.67 ms）
- 负荷有功功率变化：从约300 MW降至240 MW（故障期间），故障后恢复至300 MW
- 负荷无功功率变化：从约50 MVAr吸收降至-50 MVAr（向系统注入无功功率），故障后恢复
- 电压扫描测试速率：-1 pu/秒，用于获取负荷的静态P-V和Q-V特性曲线
- 监测数据平均窗口：1周波（导致陡峭电压变化处的瞬态畸变，需进行信号重构）


## 关键公式

### 电压频率相关负荷有功功率模型

$$$P = P_0 \left(\frac{V}{V_0}\right)^{n_p} \left[1 + K_p\frac{f-f_0}{f_0}\right]$$$

*用于模拟电视机、荧光灯等负荷的有功功率随电压和频率变化的关系，本研究中因频率变化可忽略，简化为$P = P_0 (V/V_0)^{n_p}$*

### 电压频率相关负荷无功功率模型

$$$Q = Q_0 \left(\frac{V}{V_0}\right)^{n_q} \left[1 + K_q\frac{f-f_0}{f_0}\right]$$$

*用于模拟电视机、荧光灯等负荷的无功功率随电压和频率变化的关系，本研究中因频率变化可忽略，简化为$Q = Q_0 (V/V_0)^{n_q}$*



## 验证详情

- **验证方式**: 现场录波数据对比验证（Field Measurement Validation）
- **测试系统**: Brossard变电站（315/25 kV），位于Boucherville变电站（735/315 kV）供电的径向线路末端，构成实际的混合居民-商业负荷供电场景
- **仿真工具**: EMTP（Electromagnetic Transients Program），使用UM-7（单相通用电机模型）和UM-40（三相通用电机模型），以及模型98（变压器饱和模型）
- **验证结果**: EMTP模型成功复现了单相接地故障期间的正序电压（17.5%跌落）、三相电压不对称性（故障相36%跌落，健康相8%跌落）、有功功率（300MW→240MW）和无功功率（50MVAr→-50MVAr）的动态变化。验证了模型在高达36%电压不平衡和50%电压变化范围内的准确性，确认了单相电机模型在大转差率下的零起动转矩特性对精确仿真的重要性。
