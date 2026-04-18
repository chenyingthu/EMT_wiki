---
title: "Application of EMTP-RV graphic software of electromagnetic transient simulation"
type: source
authors: ['未知']
year: 2007
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/09/Cao和Chen - 2007 - Application of EMTP-RV graphic software of electromagnetic transient simulation.pdf"]
---

# Application of EMTP-RV graphic software of electromagnetic transient simulation

**作者**: 
**年份**: 2007
**来源**: `09/Cao和Chen - 2007 - Application of EMTP-RV graphic software of electromagnetic transient simulation.pdf`

## 摘要

：In order tO introduce hoW tO use EMTP-RV(Restructured Version)．a new generation Windows-platform- based graphic software of electromagnetic transient simulation which is developed by EMTP_DCG(Development Co- ordination Group)。and to efficiently research and simulate the dynamic processes of power system and its apparatu- ses。this paper elaborates the basic features of three components of the software package：EMTP-RV core computa- tion engine，graphical user interlace EMTPWbrks and signal post-processing program ScopeView．Meanwhile-the libraries which include most important device models are depicted．A 35kV．100 MVA Static Var Compensator sire． ulation model was constructed to simulate the switching processes of its three-phase thyristors．The intuitive and US- er-friendly GraphicaI User Inte

## 核心贡献


- 阐述EMTP-RV软件架构与图形化建模流程，提供完整电磁暂态仿真环境
- 构建SVC晶闸管阀组开关暂态模型，验证软件处理电力电子动态过程能力
- 演示避雷器保护对晶闸管过电压的抑制效果，为阀组绝缘配合提供仿真依据


## 使用的方法


- [[稀疏矩阵求解|稀疏矩阵求解]]
- [[非线性迭代求解|非线性迭代求解]]
- [[时域仿真|时域仿真]]
- [[谐波分析|谐波分析]]
- [[离散傅里叶变换|离散傅里叶变换]]


## 涉及的模型


- [[svc|SVC]]
- [[tcr|TCR]]
- [[晶闸管阀组|晶闸管阀组]]
- [[zno避雷器|ZnO避雷器]]
- [[rlc支路|RLC支路]]
- [[断路器|断路器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[开关暂态|开关暂态]]
- [[过电压保护|过电压保护]]
- [[绝缘配合|绝缘配合]]
- [[facts装置建模|FACTS装置建模]]
- [[谐波分析|谐波分析]]


## 主要发现


- 仿真表明加装ZnO避雷器后晶闸管两端峰值电压由110.03kV降至62.29kV
- 软件可准确复现120度触发角下TCR阀组动态开关过程及过电压波形特征
- 图形化建模结合稀疏矩阵求解显著提升复杂电力网络电磁暂态仿真效率



## 方法细节

### 方法概述

本文采用基于EMTP-RV软件平台的图形化建模与时域数值仿真相结合的方法。首先利用EMTPWorks图形界面通过拖拽方式搭建35kV/100MVA SVC的TCR回路拓扑，设置元件参数后自动生成网络表（*.NET）文件。核心计算引擎读取网络表后，基于面向对象架构解析拓扑，构建系统稀疏导纳矩阵，并采用改进的非线性迭代算法与自动稳态初始化技术进行求解。仿真过程以1μs为步长进行时域步进计算，处理晶闸管开关状态切换与ZnO避雷器非线性伏安特性，最终将结果输出为二进制（*.mda）与ASCII（*.m）文件。后处理阶段通过ScopeView程序进行离散傅里叶变换（DFT）、谐波分析及波形可视化，完整覆盖从建模、求解到数据分析的电磁暂态仿真全流程。

### 数学公式


**公式1**: $$$[G] \cdot [v(t)] = [i(t)] - [I_{hist}(t)]$$$

*EMTP核心节点电压方程，其中[G]为系统稀疏导纳矩阵，[v(t)]为节点电压向量，[i(t)]为注入电流源向量，[I_{hist}(t)]为历史电流项（包含电感、电容及非线性元件的等效历史源），用于时域步进求解。*


**公式2**: $$$\alpha = 2\pi f \cdot t_{delay}$$$

*晶闸管触发角与触发延迟时间的换算关系，用于将控制信号中的时间延迟转换为对应的电角度，本例中t_delay=1.667ms对应α=120°。*


### 算法步骤

1. 1. 图形化建模与网络表生成：在EMTPWorks中通过拖拽内置元件库（如RLC支路、晶闸管、ZnO避雷器、6脉冲触发器等）搭建TCR主回路及控制回路，设置元件电气参数与控制逻辑（如触发脉冲宽度、延迟时间、阻断信号函数t≥t0），利用子网络封装功能构建层次化模型，最终导出标准网络表文件（*.NET）。

2. 2. 拓扑解析与矩阵构建：核心计算引擎读取*.NET文件，自动识别节点连接关系与元件类型，采用Fortran-95标准编写的稀疏矩阵表述形式构建系统导纳矩阵，消除传统方法对网络拓扑的限制，并自动执行稳态潮流初始化计算。

3. 3. 时域步进与非线性迭代求解：以1μs为固定步长推进仿真时间。在每个时间步内，更新所有动态元件（电感、电容）的历史电流项，根据晶闸管导通/关断状态切换开关模型拓扑，针对ZnO避雷器等非线性元件采用改进的牛顿-拉夫逊迭代法求解局部非线性方程组，直至收敛。

4. 4. 线性系统求解与状态更新：将收敛后的非线性等效电路并入全局网络，调用稀疏矩阵求解器求解节点电压方程，更新所有支路电流与元件状态变量，并将当前步结果写入内存缓冲区。

5. 5. 数据输出与后处理：仿真达到设定时间（60ms）后，引擎将时域数据流写入二进制文件（*.mda）及绘图脚本（*.m）。ScopeView读取数据文件，支持多通道波形叠印、光标动态追踪、区域统计（最大/最小/均值/有效值），并调用内置函数编辑器执行DFT与谐波分析，最终导出为PDF、PNG等格式。


### 关键参数

- **仿真步长**: 1 μs

- **仿真总时长**: 60 ms

- **系统额定电压/容量**: 35 kV / 100 MVA

- **电压源电势（最大运行电压）**: 38.5 kV

- **晶闸管触发角**: 120°

- **触发延迟时间**: 1.667 ms

- **触发脉冲控制逻辑**: width控制脉宽，delay控制触发角，blocking输入函数为t≥t0用于屏蔽脉冲



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 35kV/100MVA SVC TCR阀组开关暂态（无避雷器工况） | 在120°触发角下，晶闸管由导通转向关断瞬间产生操作过电压，实测阀组两端峰值电压达到110.03 kV，波形呈现典型的高频振荡与电压尖峰特征。 | 作为基准工况，未加装保护装置时过电压倍数较高，直接威胁晶闸管绝缘安全。 |

| 35kV/100MVA SVC TCR阀组开关暂态（ZnO避雷器保护工况） | 在阀组两侧并联ZnO避雷器（at、bt、ct）及进线侧避雷器（1、2、3）后，相同触发条件下晶闸管两端峰值电压被有效钳位，降至62.29 kV。 | 相比无避雷器工况，峰值电压降低47.74 kV（降幅约43.4%），验证了避雷器对开关过电压的显著抑制效果，满足绝缘配合要求。 |



## 量化发现

- 加装ZnO避雷器后，晶闸管两端峰值过电压由110.03 kV精确降至62.29 kV，电压应力削减幅度达43.4%。
- 采用1 μs微秒级仿真步长与60 ms总时长，成功捕捉TCR阀组在120°触发角下的完整开关暂态过程，波形分辨率满足电力电子器件绝缘评估需求。
- 触发延迟时间1.667 ms与系统工频（50 Hz）严格对应120°电角度，软件控制逻辑与主电路动态响应同步误差可忽略。
- EMTP-RV核心引擎支持频域、时域、稳态及统计分析4种计算模式，结合稀疏矩阵求解技术，可高效处理含大量非线性开关元件的巨型网络拓扑。


## 关键公式

### 电磁暂态网络节点导纳方程

$$$[G] \cdot [v(t)] = [i(t)] - [I_{hist}(t)]$$$

*用于EMTP-RV核心引擎在每个仿真步长内求解全网络节点电压，是时域步进计算的基础数学模型。*

### 触发角-延迟时间映射关系

$$$\alpha = 2\pi f \cdot t_{delay}$$$

*用于将6脉冲触发器DEV1的时间域控制信号转换为晶闸管导通相位，本例中f=50Hz，t_delay=1.667ms对应α=120°。*



## 验证详情

- **验证方式**: 纯数字仿真对比验证（有无避雷器工况对照）
- **测试系统**: 35 kV/100 MVA静止无功补偿器（SVC）晶闸管控制电抗器（TCR）三相回路，采用三角形连接，每相臂由L1与L2电感串联反并联晶闸管阀组（Th1~Th6）构成，配置阀侧ZnO避雷器（at/bt/ct）与进线侧ZnO避雷器（1/2/3）
- **仿真工具**: EMTP-RV（EMTPWorks图形建模、Fortran-95核心计算引擎、ScopeView可视化后处理）
- **验证结果**: 仿真结果准确复现了TCR阀组在120°触发角下的动态开关过程与过电压波形特征。对比数据表明，ZnO避雷器可将晶闸管承受的操作过电压峰值从110.03 kV有效抑制至62.29 kV，验证了EMTP-RV在电力电子开关暂态分析、过电压保护整定及绝缘配合研究中的高精度与工程实用性。
