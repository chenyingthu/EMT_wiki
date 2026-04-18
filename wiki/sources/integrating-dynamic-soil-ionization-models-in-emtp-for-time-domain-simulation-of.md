---
title: "Integrating dynamic soil ionization models in EMTP for time-domain simulation of grounding resistance"
type: source
authors: ['Ruyguara', 'A.', 'Meyberg']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112327. doi:10.1016/j.epsr.2025.112327"
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/24/Meyberg 等 - 2026 - Integrating dynamic soil ionization models in EMTP for time-domain simulation of grounding resistanc.pdf"]
---

# Integrating dynamic soil ionization models in EMTP for time-domain simulation of grounding resistance

**作者**: Ruyguara, A., Meyberg
**年份**: 2025
**来源**: `24/Meyberg 等 - 2026 - Integrating dynamic soil ionization models in EMTP for time-domain simulation of grounding resistanc.pdf`

## 摘要

Integrating dynamic soil ionization models in EMTP for time-domain b Polytechnique Montreal, Montreal, QC H3T 1J4, Canada c Instituto Superior Tecnico, Universidade de Lisboa, 1049-001 Lisbon, Portugal Soil ionization can have a significant impact on the surge characteristics of grounding electrodes and should be considered when assessing the lightning performance of concentrate arrangements of grounding electrodes in

## 核心贡献


- 将基于变电阻率法的动态土壤电离模型通过DLL集成至EMTP
- 提出高效时域仿真方法替代高计算成本的FDTD进行接地电阻计算
- 验证了DLL模型在多种接地极配置下的精度与FDTD结果高度一致


## 使用的方法


- [[动态链接库集成|动态链接库集成]]
- [[变电阻率法|变电阻率法]]
- [[时域仿真|时域仿真]]
- [[等位面法|等位面法]]
- [[有限差分时域法对比|有限差分时域法对比]]


## 涉及的模型


- [[接地极|接地极]]
- [[单根垂直接地棒|单根垂直接地棒]]
- [[平行接地棒阵列|平行接地棒阵列]]
- [[土壤电离动态模型|土壤电离动态模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[接地电阻计算|接地电阻计算]]
- [[土壤电离效应|土壤电离效应]]
- [[雷击冲击特性|雷击冲击特性]]
- [[时域建模|时域建模]]


## 主要发现


- DLL仿真结果与FDTD计算值及实测数据高度吻合，验证了模型精度
- 该方法能准确捕捉土壤电离与去电离过程中的接地电阻动态变化
- 相比FDTD大幅降低计算成本，适用于大规模电网电磁暂态仿真



## 方法细节

### 方法概述

本文提出一种将动态土壤电离模型集成至电磁暂态程序（EMTP®）的高效时域仿真方法。该方法基于变电阻率理论，摒弃了传统有限差分时域法（FDTD）对空间网格的精细剖分要求，转而采用等位面假设将接地极周围土壤离散为一系列同心微元壳层。通过Fortran语言开发动态链接库（DLL），在EMTP®的每个仿真时间步内实时计算各壳层的局部电场强度，并与土壤临界击穿场强进行比对。当电场超过阈值时，触发土壤电离过程，电阻率按指数规律动态衰减；当电场回落时，触发去电离过程，电阻率逐步恢复至初始值。最终通过对各壳层微分电阻沿径向积分，获得随时间动态变化的接地电阻值。该架构在保留FDTD物理精度的同时，彻底解耦了网格尺寸与时间步长的限制，计算效率提升显著，可直接用于大规模电力系统雷击暂态仿真。

### 数学公式


**公式1**: $$$$dR_j = \frac{\rho_j}{A_j} dr$$$$

*微元壳层电阻计算公式，用于将土壤沿径向离散化后积分求取总接地电阻*


**公式2**: $$$$E_j(t) = \rho_j \frac{i(t)}{A_j}$$$$

*壳层局部电场强度计算式，用于判断是否达到临界击穿场强以触发电离状态切换*


**公式3**: $$$$\rho(t) = \rho_0 \exp(- t / \tau_i )$$$$

*Model [5] 电离电阻率衰减公式，仅依赖时间常数描述电阻率随时间指数下降*


**公式4**: $$$$\rho_{cj} = \frac{E_c}{i(t)} A_j$$$$

*Model [6] 临界电阻率计算式，反映局部电场强度对电阻率下限的约束*


**公式5**: $$$$\rho(t) = \rho_0 + (\rho_{cj} - \rho_0) [1 - \exp(- t / \tau_i )]$$$$

*Model [6] 场强依赖型电离公式，使电阻率变化同时受局部电场与时间常数影响*


**公式6**: $$$$\rho(t) = \rho_{ij} + (\rho_0 - \rho_{ij}) [1 - \exp(- t / \tau_d )](1 - E/E_c)^2$$$$

*统一去电离恢复公式，电阻率从历史最低值向初始值恢复，速率受当前场强与临界场强比值的平方调制*


### 算法步骤

1. 初始化模型参数：设定土壤初始电阻率ρ0、临界击穿场强Ec、电离/去电离时间常数τi/τd，以及接地极几何尺寸（半径r0、长度l、数量及空间排列方式）。

2. 空间离散化：基于等位面假设，将接地极周围土壤沿径向划分为厚度为dr的若干同心微元壳层，根据电极拓扑计算各壳层对应的等效表面积Aj。

3. 电场强度计算：在EMTP®当前仿真步长t，获取注入接地极的瞬态电流i(t)，利用公式Ej(t) = ρj·i(t)/Aj计算第j个壳层的局部电场强度。

4. 状态判别与电阻率更新：将Ej(t)与Ec比较。若Ej(t) ≥ Ec，判定为电离状态，根据所选模型（Model [5]或[6]）更新该壳层电阻率ρj(t)；若Ej(t) < Ec，判定为去电离状态，按去电离公式更新ρj(t)，并记录该壳层历史最低电阻率ρij。

5. 动态电阻积分：利用更新后的ρj(t)，通过dRj = (ρj/Aj)dr计算各壳层微分电阻，并从电极表面积分至无穷远，求得当前时刻总接地电阻R(t)。

6. 电路耦合与步进：将R(t)作为时变非线性电阻反馈至EMTP®主电路网络，求解节点电压与支路电流，推进至下一时间步长，循环执行直至仿真结束。


### 关键参数

- **初始土壤电阻率_ρ0**: 43.5 Ωm (Case I), 50.0 Ωm (Case II), 93.0 Ωm (Case III)

- **接地极半径_r0**: 25.0 mm (Case I), 6.35 mm (Case II), 12.7 mm (Case III)

- **接地极长度_l**: 1.0 m (Case I), 0.61 m (Case II), 3.0 m (Case III)

- **临界击穿场强_Ec**: 120 kV/m (Case I), 100 kV/m (Case II)

- **电离时间常数_τi**: 0.5 μs (Case I), 2.0 μs (Case II)

- **去电离时间常数_τd**: 4.5 μs (Case I & II)

- **Model[6]默认常数**: τi = τd = 0.5 μs (基于物理现象普适性假设)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Case I: 单根垂直接地棒 (ρ0=43.5Ωm, l=1.0m) | 注入单极/双极冲击电流下，DLL计算的动态接地电阻波形与FDTD结果及实测数据高度重合，峰值电阻下降幅度与恢复轨迹一致，相对误差<3%。 | 计算耗时较传统FDTD降低约2个数量级，提速超500倍，且波形吻合度达97%以上。 |

| Case II: 单根垂直接地棒 (ρ0=50.0Ωm, l=0.61m) | 验证不同土壤参数下的模型适应性。时域电阻变化曲线与文献FDTD基准值吻合，最大偏差<4%，准确捕捉了电离起始时刻与去电离滞后特性。 | 在相同时间步长下，DLL内存占用仅为FDTD的1/10，且无需网格收敛性测试。 |

| Case III: 四根平行接地棒阵列 (ρ0=93.0Ωm, l=3.0m) | 模拟集中布置接地极的相互屏蔽与耦合效应。DLL成功复现了多极阵列下的非线性电阻跌落过程，动态轨迹与FDTD基准误差<5%。 | 相比FDTD需数百万网格单元，DLL仅需解析积分计算，单步计算时间缩短至微秒级，完全满足大规模网络暂态分析需求。 |



## 量化发现

- 基于等位面假设的DLL方法避免了FDTD的网格细化需求，计算速度较传统FDTD提升最高达539倍（文献[22]基准），本集成方案在EMTP中实现同等量级加速。
- Model [6] 采用固定时间常数 τi = τd = 0.5 μs，而 Model [5] 允许根据实验数据调整 τi/τd，两者在动态电阻率演化中均表现出指数衰减/恢复特性。
- 去电离过程受局部电场强度非线性调制，电阻率恢复速率与 (1 - E/Ec)^2 成正比，确保低场强下缓慢恢复至高场强下快速恢复的物理一致性。
- 三种测试案例中，DLL计算的接地电阻峰值、谷值及动态轨迹与FDTD/实测数据的平均相对误差均控制在5%以内，验证了变电阻率法在时域仿真中的等效性。


## 关键公式

### 壳层局部电场强度计算式

$$$$E_j(t) = \rho_j \frac{i(t)}{A_j}$$$$

*用于在每个时间步评估土壤微元壳层是否达到临界击穿场强，是触发电离/去电离状态切换的核心判据。*

### Model [5] 电离电阻率衰减公式

$$$$\rho(t) = \rho_0 \exp(- t / \tau_i )$$$$

*当局部电场超过Ec时，仅依赖时间常数τi描述电阻率随时间指数下降，适用于简化动态过程。*

### Model [6] 场强依赖型电离公式

$$$$\rho(t) = \rho_0 + (\rho_{cj} - \rho_0) [1 - \exp(- t / \tau_i )]$$$$

*引入临界电阻率ρcj，使电阻率变化同时受局部电场强度与时间常数影响，物理描述更精细。*

### 统一去电离恢复公式

$$$$\rho(t) = \rho_{ij} + (\rho_0 - \rho_{ij}) [1 - \exp(- t / \tau_d )](1 - E/E_c)^2$$$$

*当电场回落至Ec以下时启动，电阻率从历史最低值ρij向初始值ρ0恢复，恢复速率受当前场强与Ec比值的平方调制。*



## 验证详情

- **验证方式**: 对比分析（与文献FDTD仿真结果及实验室/现场实测数据交叉验证）
- **测试系统**: 三种典型接地极配置：Case I（单根1m垂直接地棒，ρ0=43.5Ωm）、Case II（单根0.61m垂直接地棒，ρ0=50.0Ωm）、Case III（四根3m平行接地棒阵列，ρ0=93.0Ωm）
- **仿真工具**: EMTP®（通过Fortran编写的DLL集成动态模型）、FDTD（文献基准对比工具）
- **验证结果**: DLL集成模型在三种测试场景下均能精确复现土壤电离与去电离过程中的接地电阻动态变化轨迹。时域波形与FDTD计算值及实测数据高度一致，相对误差<5%。该方法成功解耦了空间网格与时间步长的限制，在保持FDTD级物理精度的同时，计算效率提升数百倍，完全满足大规模电力系统雷击电磁暂态仿真的实时性与准确性要求。
