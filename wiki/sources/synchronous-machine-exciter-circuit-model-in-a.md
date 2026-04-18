---
title: "Synchronous Machine Exciter Circuit Model In A"
type: source
authors: ['未知']
year: 2013
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/37/pesmg.2013.6672704.pdf.pdf"]
---

# Synchronous Machine Exciter Circuit Model In A

**作者**: 
**年份**: 2013
**来源**: `37/pesmg.2013.6672704.pdf.pdf`

## 摘要

—This paper presents the implementation of a phase domain (PD) synchronous machine (SM) model through modified-augmented-nodal-analysis (MANA) formulation for the computation of electromagnetic transients. This formulation provides a direct and simultaneous electrical connection to the SM field winding, and enables accurate modeling of its exciter as an electrical side. Detailed exciter modeling can be used to study exciters transient performance and potential failure conditions in its circuit components. This paper also presents and tests a simple current source interface for existing dq0-type SM machine models with control signal input for field control. Realistic test cases are used to validate and compare the proposed models. Index Terms—synchronous machine, excitation system, EMTP. I.

## 核心贡献



- 基于改进增广节点分析（MANA）公式实现了相域同步电机模型，提供与励磁绕组直接同步的电气连接，实现励磁系统精确电路建模。
- 为现有dq0型同步电机模型提出并验证了一种简单的电流源接口，用于励磁控制信号输入，提升了模型兼容性与仿真灵活性。

## 使用的方法


- [[nodal-analysis]]
- [[numerical-integration]]

## 涉及的模型


- [[synchronous-machine]]

## 相关主题


- [[synchronous-machine]]
- [[parallel]]

## 主要发现



- 基于MANA的相域同步电机模型可实现励磁绕组与外部电路的直接同步连接，显著提升励磁系统瞬态性能及元件故障分析的准确性。
- 提出的电流源接口能有效兼容现有dq0型同步电机模型，在保证精度的同时简化励磁控制接入，并通过并联机组实际案例验证了其有效性。

## 方法细节

### 方法概述

本文提出两种同步电机励磁系统建模方法：第一种（SM1）基于改进增广节点分析(MANA) formulation与相域同步电机(PDSM)模型相结合，实现励磁绕组与外部电路的直接同步电气连接，消除了传统补偿法的拓扑限制；第二种（SM2）针对现有dq0型同步电机模型，提出基于受控电流源的接口方案，通过将励磁绕组电压作为控制输入、场电流作为输出，实现励磁电路与电机模型的非同步连接（含一个时间步延迟）。SM1采用梯形积分法则对相域电压方程进行离散化，对可检测不连续性采用后退欧拉法抑制数值振荡，通过MANA矩阵将电机方程直接嵌入电力系统网络方程(PSNE)进行联立求解。

### 数学公式


**公式1**: $$$J_m p \omega_m + D_m p \theta_m + K_m \theta_m = T_a$$$

*机械子系统方程，描述转子角速度ωm和角度θm的动态，其中Jm为转动惯量，Dm为阻尼系数，Km为刚度系数，Ta为加速转矩*


**公式2**: $$$v = -R i + p \lambda$$$

*相域同步电机电压方程，v为绕组电压向量，i为电流向量，R为绕组电阻对角矩阵，λ为磁链向量*


**公式3**: $$$\lambda = L(\theta) i$$$

*磁链方程，L(θ)为依赖于转子位置θ的电感矩阵*


**公式4**: $$$T_{gen} = \frac{P}{4} i^T \frac{\partial L(\theta)}{\partial \theta} i$$$

*电磁转矩方程，P为极对数，通过磁共能对转子位置求导得到*


**公式5**: $$$v = -R i + h$$$

*离散化电压方程，采用梯形积分法则得到，其中R为等效电阻矩阵，h为历史项向量*


**公式6**: $$$R = R_{actual} + k L(\hat{\theta})$$$

*等效电阻矩阵计算，k=2/Δt为积分系数，L(θ̂)为基于预测转子位置的电感矩阵*


**公式7**: $$$h = -(R_{actual} + k L(\hat{\theta}))\hat{i} + \hat{v}$$$

*历史项向量计算，带帽变量表示上一时间步的已知值*


**公式8**: $$$k = 2 / \Delta t$$$

*梯形积分法则的时间步长系数*


### 算法步骤

1. 计算梯形积分法则产生的历史项（见公式(7)），基于上一时间步的电流、电压和预测的电感矩阵

2. 预测转子位置θ以更新电感矩阵L(θ)，并计算等效电阻矩阵R（包含实际电阻和梯形积分引入的等效电阻）

3. 重新分解并求解电力系统网络方程(PSNE)的MANA矩阵，求得网络节点电压vn和绕组电流等变量

4. 利用公式(4)计算电磁转矩Tgen，基于当前电流和电感矩阵对转子位置的偏导数

5. 求解机械方程(1)，更新转子角度θm和角速度ωm

6. 返回步骤1，进入下一个时间点的求解


### 关键参数

- **J_m**: 转动惯量

- **D_m**: 机械阻尼系数

- **K_m**: 扭转刚度系数

- **P**: 电机极对数

- **R**: 绕组电阻对角矩阵（包含实际电阻和离散化等效电阻）

- **L(θ)**: 依赖于转子位置的7×7电感矩阵（定子三相+励磁绕组+三个阻尼绕组）

- **k**: 梯形积分系数，等于2/Δt

- **Δt**: 仿真时间步长

- **θ_m**: 转子机械角度

- **ω_m**: 转子机械角速度



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 场景S1：三相接地故障 | 在BUS2端的400kV BUS1-BUS2线路于0.5s时施加三相接地故障，由断路器CB1和CB2清除故障，系统总仿真时长5s。用于验证SM1和SM2模型在严重对称故障下的暂态响应一致性。 | 对比了MANA-based相域模型(SM1)与电流源接口dq0模型(SM2)的励磁电流、机端电压和电磁转矩响应 |

| 场景S2：单相接地故障及重合闸 | 在S1相同位置施加永久性单相接地故障，考虑单相重合闸设施，死区时间为500ms（0.5s），系统仿真3s。用于测试非对称故障条件下励磁系统的详细电路模型性能。 | 验证了在含重合闸时序的非对称故障下，详细励磁电路模型与电机模型的接口稳定性 |

| 场景S3：晶闸管开路故障 | 模拟励磁系统整流器晶闸管故障（开路模式，发生在t=0.5s），导致励磁变压器二次侧线间开路，但机组保持并网运行。仿真时长1s，用于研究励磁系统元件故障对电机的影响。 | 展示了详细电路模型在元件级故障（thyristor open-circuit）分析中的能力，这是传统控制框图模型无法实现的 |



## 量化发现

- 系统额定电压：机端14.85kV，电网400kV；额定功率：单机140MW，负载100MW+j50MVAR
- 梯形积分离散化系数k=2/Δt，确保数值稳定性同时引入与步长相关的等效电阻
- 电流源接口方案(SM2)引入一个时间步(Δt)的延迟，但由于励磁绕组时间常数较大（不允许电流突变），即使采用大步长仍能保持足够精度
- 故障施加时刻统一为t=0.5s，三相故障仿真总时长5s，单相故障3s，元件故障1s
- 单相重合闸死区时间设定为500ms
- MANA formulation将电机方程维度从传统导纳法的降维形式扩展为直接嵌入7个绕组方程（3定子+1励磁+3阻尼）


## 关键公式

### MANA增广节点方程

$$$$\begin{bmatrix} \mathbf{Y}_n & \mathbf{V}_{adj} & \mathbf{D}_{bdepc} & \mathbf{S}_{adj} & \mathbf{S}_{M_{adj}} \\ \mathbf{V}_{adj}^T & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} \\ \mathbf{D}_{bdepr} & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{0} \\ \mathbf{S}_{adj}^T & \mathbf{0} & \mathbf{0} & \mathbf{S}_0 & \mathbf{0} \\ \mathbf{S}_{M_{adj}}^T & \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{A}_{SM} \end{bmatrix} \begin{bmatrix} \mathbf{v}_n \\ \mathbf{i}_{V} \\ \mathbf{i}_{D} \\ \mathbf{i}_{S} \\ \mathbf{x}_{SM} \end{bmatrix} = \begin{bmatrix} \mathbf{i}_n \\ \mathbf{v}_{S} \\ \mathbf{0} \\ \mathbf{0} \\ \mathbf{b}_{SM} \end{bmatrix}$$$$

*用于同时求解电力网络方程和同步电机内部绕组方程，其中Yn为网络导纳，SMadj为电机关联矩阵，ASM包含电阻矩阵R，xSM包含绕组电流，bSM包含历史项*

### 离散化相域电压方程

$$$v = -[R_{actual} + \frac{2}{\Delta t}L(\theta)]i + [(R_{actual} + \frac{2}{\Delta t}L(\hat{\theta}))\hat{i} - \hat{v}]$$$

*基于梯形积分法则的同步电机离散时域方程，用于EMT仿真中的每个时间步求解，等效电阻R与电感L和步长Δt相关*

### 电磁转矩方程

$$$T_{gen} = \frac{P}{4} i^T \frac{\partial L(\theta)}{\partial \theta} i$$$

*计算同步电机电磁转矩，用于机械方程(1)的求解，实现电气与机械系统的耦合*



## 验证详情

- **验证方式**: 基于EMTP-RV的仿真对比验证，通过用户自定义DLL实现PDSM模型，对比SM1（MANA相域模型）与SM2（电流源接口dq0模型）在不同故障场景下的响应一致性
- **测试系统**: 两个并联运行的相同水电机组，连接至400kV电网，采用静态励磁系统（ thyristor-controlled rectifier）。系统包含400kV线路、断路器CB1/CB2、机端电压14.85kV，单机额定140MW，负载100MW+j50MVAR
- **仿真工具**: EMTP-RV（唯一采用MANA formulation的EMT-type程序），通过用户自定义动态链接库(DLL)选项实现提出的PDSM模型与励磁绕组电气接口
- **验证结果**: 三个测试场景（三相短路、单相接地重合闸、晶闸管开路故障）验证了所提模型的正确性。SM1实现了励磁电路与电机的真正同步求解，适用于详细故障分析；SM2在保持足够精度的同时提供了与现有dq0模型的兼容性，适用于大多数工程应用场景
