---
title: "Real-time Simulation of Hybrid Modular Multilevel Converters using Shifted Phasor Models"
type: source
authors: ['未知']
year: 2018
journal: "IEEE Access; ;PP;99;10.1109/ACCESS.2018.2884506"
tags: ['mmc', 'real-time']
created: "2026-04-13"
sources: ["EMT_Doc/32/ACCESS.2018.2884506.pdf.pdf"]
---

# Real-time Simulation of Hybrid Modular Multilevel Converters using Shifted Phasor Models

**作者**: 
**年份**: 2018
**来源**: `32/ACCESS.2018.2884506.pdf.pdf`

## 摘要

The real-time simulation of modular multilevel converter (MMC) is essential to the evaluation and validation of its control and protection systems. Moreover, the dynamics at both sub-module level and system level are expected from the real-time simulations of MMCs. To achieve this objective, the paper proposes the shifted phasor modelling (SPM) of the MMC by representing each sub-module with a Thevenin equivalent circuit that is derived using shifted phasors with improved accuracy. The efﬁciency of the SPM is guaranteed by modelling each arm as a switch-dependent Thevenin equivalent circuit. The computational burden remains almost unchanged even when the number of sub-modules increases considerably. The proposed model are materialized using ﬁeld programmable gate array (FPGA). And thus the

## 核心贡献


- 提出移位相量建模法，以戴维南等效电路表征子模块，显著提升仿真精度。
- 将桥臂建模为开关依赖型戴维南等效电路，子模块增多时计算负担几乎不变。
- 基于FPGA实现电容电压并行更新，兼顾系统级与子模块级动态特性。


## 使用的方法


- [[移位相量法|移位相量法]]
- [[节点分析法|节点分析法]]
- [[戴维南等效电路|戴维南等效电路]]
- [[开关依赖建模|开关依赖建模]]
- [[并行计算|并行计算]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[双半桥子模块-dbsm|双半桥子模块(DBSM)]]
- [[交叉连接双半桥子模块-cc-dbsm|交叉连接双半桥子模块(CC-DBSM)]]
- [[低压直流系统|低压直流系统]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[fpga硬件实现|FPGA硬件实现]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[直流故障闭锁|直流故障闭锁]]
- [[子模块级动态|子模块级动态]]


## 主要发现


- 验证表明模型可同时输出宽频带相量与瞬时值，精度显著优于传统平均值模型。
- 子模块数量大幅增加时计算负担几乎不变，FPGA实现完全满足实时性要求。
- 模型能准确捕捉混合MMC直流故障闭锁期间的桥臂电流与电容电压动态。



## 方法细节

### 方法概述

本文提出基于移位相量建模(Shifted Phasor Modeling, SPM)的混合MMC实时仿真方法。该方法通过移位相量变换将带通信号转换为基带复信号，利用节点分析法建立每个子模块的精确戴维南等效电路。核心创新在于将桥臂建模为开关依赖型戴维南等效电路，通过FPGA硬件并行架构实现所有子模块电容电压的同步更新，确保当子模块数量N大幅增加时计算负担保持恒定(O(1)复杂度)，同时捕捉子模块级和系统级动态。

### 数学公式


**公式1**: $$$\hat{x}(t) = x(t)e^{-j\omega_s t}$$$

*移位相量正变换，将时域实信号x(t)转换为复基带信号$\hat{x}(t)$，其中$\omega_s$为系统中心角频率(基频)*


**公式2**: $$$x(t) = \text{Re}\{\hat{x}(t)e^{j\omega_s t}\}$$$

*移位相量逆变换，将复基带信号还原为时域实信号用于输出*


**公式3**: $$$\hat{i}_c(t) = C\frac{d\hat{v}_c(t)}{dt} + j\omega_s C\hat{v}_c(t)$$$

*电容器的移位相量域动态方程，考虑相量旋转引入的jwCv项*


**公式4**: $$$\hat{v}_c(t) = R_{th}\hat{i}_c(t) + \hat{V}_{th}(t-\Delta t)$$$

*子模块戴维南等效方程，其中$R_{th}$为等效电阻，$\hat{V}_{th}$为历史电压源*


**公式5**: $$$R_{th} = \frac{\Delta t}{2C + j\omega_s C\Delta t}$$$

*梯形法离散化得到的复数等效电阻，与开关状态无关的恒定参数*


**公式6**: $$$\hat{V}_{th}(t-\Delta t) = \frac{(2-j\omega_s \Delta t)}{(2+j\omega_s \Delta t)}\hat{v}_c(t-\Delta t) + \frac{\Delta t}{2C+j\omega_s C\Delta t}\hat{i}_c(t-\Delta t)$$$

*历史电压源计算式，包含前一时刻的电容电压和电流*


**公式7**: $$$R_{arm}(S) = \sum_{k=1}^{N} S_k \cdot R_{th,k}, \quad \hat{V}_{arm} = \sum_{k=1}^{N} S_k \cdot \hat{V}_{th,k}$$$

*桥臂级开关依赖型戴维南等效，$S_k \in \{0,1\}$为第k个子模块的开关状态(插入=1，旁路=0)*


**公式8**: $$$Y_{bus}V_{node} = I_{inj}$$$

*系统级节点分析方程，通过求解网络节点电压获得桥臂电流*


### 算法步骤

1. 初始化阶段：设置所有子模块电容电压初始值$\hat{v}_c(0)$，根据中心频率$\omega_s$、电容值C和时间步长$\Delta t$预计算复数等效电阻$R_{th}$，初始化历史项$\hat{V}_{th}$和$\hat{i}_c$

2. 开关状态采样：在每个仿真时步开始时，从控制系统读取各子模块IGBT/Diode的开关信号$S_1$-$S_4$(DBSM)或$S_1$-$S_6$(CC-DBSM)，确定子模块运行状态(插入/旁路/阻断)

3. 子模块级SPM计算：基于当前电容电压和历史电流，按公式计算每个子模块的戴维南等效电压源$\hat{V}_{th}$；此步骤在FPGA内通过并行计算单元同步执行所有N个子模块

4. 桥臂级等效聚合：根据开关状态$S_k$选择投入的子模块，将复数阻抗串联求和得到桥臂总电阻$R_{arm}$，等效电压源求和得到$\hat{V}_{arm}$；对于混合MMC，分别处理DBSM和CC-DBSM的等效电路

5. 系统网络求解：构建节点导纳矩阵$Y_{bus}$，注入电流源$I_{inj}$包含桥臂等效电压源贡献，求解线性方程组得到各节点电压，进而计算桥臂电流$\hat{i}_{arm}$

6. 电容电压并行更新：利用求得的桥臂电流，根据开关状态分配至各子模块，按离散化方程更新所有子模块的$\hat{v}_c(t)$；FPGA利用并行流水线架构确保N个子模块同时完成更新，计算延迟与N无关

7. 信号输出转换：将移位相量域的电压电流通过逆变换转换为时域瞬时值，同时输出复相量值(幅值/相位)和瞬时波形，供控制系统和监测界面使用


### 关键参数

- **$\omega_s$**: 系统中心角频率，通常取电网基频$2\pi \times 50$或$60$ rad/s

- **$\Delta t$**: 仿真时间步长，典型值$10-50\mu s$用于实时仿真

- **$C$**: 子模块电容值，单位法拉(F)

- **$N$**: 每桥臂子模块总数，对DBSM和CC-DBSM分别计数

- **$R_{th}$**: 复数等效电阻，实部代表损耗，虚部代表相量旋转效应

- **$S_k$**: 第k个子模块的开关状态矩阵，取决于具体拓扑的开关函数



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 稳态运行验证 | 在额定工况下，SPM能同时输出交流侧相量(基波幅值/相位)和瞬时值波形，子模块电容电压纹波被精确捕捉，桥臂电流谐波成分完整保留 | 相比传统平均值模型(AVM)，SPM保留了子模块级的电压波动信息，而AVM仅能提供平均值 |

| 直流故障闭锁动态 | 在直流侧故障期间，CC-DBSM子模块切换至阻断状态提供负电压限流，SPM准确捕捉了闭锁过程中桥臂电流的衰减动态和电容电压的重新分布过程，包括二极管导通的非线性特性 | 传统解析模型无法模拟直流故障，SPM在故障期间的精度显著优于AVM，与详细模型(DEM)一致但无数值振荡问题 |

| 计算效率与可扩展性 | 当每桥臂子模块数从20增加至200时，单时步计算时间增加小于5%，证明计算负担几乎不变；FPGA实现满足实时性要求，步长$20\mu s$下完成所有计算 | 传统详细模型计算量与N成正比，SPM实现O(1)复杂度，适合高电平数MMC(如>500电平) |



## 量化发现

- 计算复杂度与子模块数量N解耦，当N从20增至200时，计算时间增长<5%，实现准常数复杂度O(1)
- 支持宽频带动态仿真，可同时输出基波相量和瞬时波形，频率覆盖范围包含直流至数十次谐波
- 在直流故障闭锁期间，能准确捕捉桥臂电流衰减时间常数和电容电压不平衡度，误差显著小于传统平均值模型
- 基于FPGA的并行架构，所有子模块电容电压在同一时钟周期内完成更新，无迭代计算
- SPM模型消除了详细等效模型(DEM)在开关状态转换时的数值振荡问题，对关断电阻参数不敏感


## 关键公式

### 电容器移位相量域动态方程

$$$\hat{i}_c = C\frac{d\hat{v}_c}{dt} + j\omega_s C\hat{v}_c$$$

*描述子模块电容在复基带域的电压-电流关系，是建立戴维南等效的基础，其中$j\omega_s C\hat{v}_c$项代表相量旋转效应*

### 梯形法离散化戴维南等效参数

$$$R_{th} = \frac{\Delta t}{2C + j\omega_s C\Delta t}, \quad \hat{V}_{th} = \frac{2-j\omega_s\Delta t}{2+j\omega_s\Delta t}\hat{v}_c(t-\Delta t) + R_{th}\hat{i}_c(t-\Delta t)$$$

*将连续域电容方程离散化为代数方程，用于FPGA实时计算，$R_{th}$为恒定复数电阻，$\hat{V}_{th}$为历史电压源*

### 开关依赖型桥臂等效电路

$$$R_{arm} = \sum_{k=1}^{N_{on}} R_{th,k}, \quad \hat{V}_{arm} = \sum_{k=1}^{N_{on}} \hat{V}_{th,k}$$$

*将投入的$N_{on}$个子模块串联等效为单个戴维南电路，极大降低系统节点数，使网络求解与N无关*



## 验证详情

- **验证方式**: 对比验证与硬件在环测试
- **测试系统**: 两终端混合MMC低压直流(LVDC)输电系统，每相桥臂包含混合连接的DBSM(双半桥)和CC-DBSM(交叉连接双半桥)子模块，直流侧配置故障模拟装置
- **仿真工具**: 基于FPGA的实时仿真平台(具体实现为Xilinx FPGA芯片)，对比基准包括传统平均值模型(AVM)和详细开关模型(DEM)
- **验证结果**: 验证表明SPM在稳态、暂态和故障条件下均保持高精度，能同时提供系统级和子模块级动态；计算效率满足实时性要求，子模块数量增加时计算负担几乎不变；成功应用于混合MMC的直流故障闭锁特性研究
