---
title: "Loop closing analytical calculation system based on electromagnetic-electromechanical transient simu"
type: source
authors: ['CNKI']
year: 2023
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/25/Zhu 等 - 2012 - Loop closing analytical calculation system based on electromagnetic-electromechanical transient simu.pdf"]
---

# Loop closing analytical calculation system based on electromagnetic-electromechanical transient simu

**作者**: CNKI
**年份**: 2023
**来源**: `25/Zhu 等 - 2012 - Loop closing analytical calculation system based on electromagnetic-electromechanical transient simu.pdf`

## 摘要

To improve safe operation of power network, a loop closing analytical calculation system based on electromagnetic- electromechanical transient hybrid simulation theory is developed. An automatic electromagnetic network partition solution based on the maximal stair search algorithm is put forward. The system also implements the function of automatic transformation from the electromechanical transient models to electromagnetic models and links the geographic maps and station maps, which not only makes loop closing operation easy but also enhances veracity. Simulation and calculation results show that the system can increase the accuracy of loop closing, providing evidence for loop closing operation. This work is supported by National High-tech R&D Program of China (863 Program) (No. 2011AA05

## 核心贡献


- 提出基于最大级数搜索算法的电磁网络自动划分方法，实现合环区域精准分网
- 实现机电暂态模型向电磁暂态模型的自动转换，避免手工录入提升建模效率
- 构建单机多核并行计算架构，降低混合仿真硬件成本并提升计算速度


## 使用的方法


- [[机电-电磁暂态混合仿真|机电-电磁暂态混合仿真]]
- [[最大级数搜索算法|最大级数搜索算法]]
- [[戴维南-诺顿等值接口|戴维南/诺顿等值接口]]
- [[序相量与瞬时值变换|序相量与瞬时值变换]]
- [[单机多核并行计算|单机多核并行计算]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[变压器|变压器]]
- [[同步发电机|同步发电机]]
- [[负荷|负荷]]
- [[电容器|电容器]]
- [[电抗器|电抗器]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[电网合环分析|电网合环分析]]
- [[网络自动划分|网络自动划分]]
- [[模型自动转换|模型自动转换]]
- [[并行计算|并行计算]]
- [[冲击电流分析|冲击电流分析]]


## 主要发现


- 喀什电网算例验证表明，系统可准确获取合环冲击电流与过电压瞬时值
- 开关统计功能有效捕捉最恶劣合环相角下的最大冲击电流，提升安全性评估精度
- 单机并行架构显著缩短混合仿真耗时，满足实际电网合环操作的快速分析需求



## 方法细节

### 方法概述

提出一种基于机电-电磁暂态混合仿真的电网合环分析计算系统。系统采用戴维南/诺顿等值接口实现机电网络（基波相量域）与电磁网络（三相瞬时值域）的实时数据交互。通过最大级数搜索算法自动划分电磁暂态子网，避免人工分网导致的拓扑遗漏；内置机电模型至电磁模型的自动转换引擎，利用潮流初值自动初始化网络状态。计算架构采用Windows单机多核并行设计，通过Socket与MPIFIFO实现机电进程、电磁进程与IO进程的异步通信与数据交换，兼顾大规模电网潮流转移分析与局部合环点高频暂态冲击/过电压的精确捕捉。

### 数学公式


**公式1**: $$$V_{abc}(t) = V_{th,abc}(t) - Z_{th,abc} \cdot I_{abc}(t)$$$

*机电网络向电磁网络提供的戴维南等值接口方程，用于在电磁侧注入边界电压源与等值阻抗。*


**公式2**: $$$I_{012}(t) = I_{sc,012}(t) - Y_{eq,012} \cdot V_{012}(t)$$$

*电磁网络向机电网络提供的诺顿等值接口方程，用于在机电侧注入边界电流源与等值导纳。*


**公式3**: $$$\begin{bmatrix} V_a \\ V_b \\ V_c \end{bmatrix} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & a^2 & a \\ 1 & a & a^2 \end{bmatrix} \begin{bmatrix} V_0 \\ V_1 \\ V_2 \end{bmatrix}$$$

*序分量到相分量的变换矩阵，用于将机电侧的正、负、零序等值电势转换为电磁侧所需的三相瞬时值边界条件。*


**公式4**: $$$v(t) = \sqrt{2} |V| \cos(\omega t + \theta)$$$

*相量到瞬时值的时域重构公式，用于将机电侧输出的基波相量转换为电磁侧微秒/毫秒级积分所需的瞬时电压波形。*


### 算法步骤

1. 初始化拓扑：将用户指定的合环点两侧母线合并定义为初始母线，设定最大搜索级数$X$（工程默认取1），并配置是否合并死岛网络。

2. 级数搜索：以初始母线为起点，沿具有阻抗的支路向外逐层遍历。将距离初始母线级数$\le X$的所有母线及相连支路纳入电磁暂态网络集合。

3. 边界切割：识别电磁网络集合与外部网络的连接支路，将其划归机电暂态网络。通过拓扑校验确保机电子网与电磁子网电气独立，无环路交叉。

4. 模型自动转换：遍历电磁网络内元件。对线路、变压器、负荷、电容、电抗等简单元件，直接映射机电参数至电磁参数；对发电机、FACTS等复杂元件，按类型与名称从预置电磁模型库中检索匹配。利用潮流计算结果自动填充母线电压幅值、相角及发电机功率初值。

5. 并行时序调度：启动机电进程、电磁进程与IO进程。机电进程以$DTP=0.01\text{s}$步长积分，电磁进程以$DTE=0.001\text{s}$步长积分。每$DTP$时刻，机电进程向电磁进程发送边界点正负零序等值电势与阻抗阵，电磁进程返回边界点三相瞬时电压/电流。数据通过MPIFIFO异步写入，Socket负责与UI交互，实现单机多核高效协同。


### 关键参数

- **机电暂态步长(DTP)**: 0.01 s

- **电磁暂态步长(DTE)**: 0.001 s

- **最大搜索级数(X)**: 1

- **开关统计次数**: 10次/工频周期

- **并行进程数**: 3个（机电计算进程、电磁计算进程、IO进程）

- **通信机制**: Socket（UI与计算进程）、MPIFIFO（计算进程与IO进程）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 新疆喀什地区电网四站环形网络合环 | 以天色断为合环点、天巴断为解环点进行全工况仿真。系统输出合环前后潮流对比、稳态电流、冲击电流瞬时值及过电压曲线。开关统计功能遍历10个不同合环相角，成功捕捉最恶劣工况下的最大冲击电流峰值，并生成包含潮流转移、暂态冲击、过电压分析的综合报告。 | 相比传统纯机电仿真（仅能获取稳态值，无法反映暂态冲击）或纯电磁仿真（需人工等值简化且建模耗时），本系统通过混合接口与自动分网，在保持大电网潮流精度的同时，将局部合环点暂态分析建模时间缩短至分钟级，且单机多核架构使硬件部署成本降低约70%以上。 |



## 量化发现

- 机电与电磁网络数据交换周期固定为0.01 s，电磁内部积分步长为0.001 s，实现10:1的时间尺度嵌套，确保暂态高频分量不丢失。
- 最大级数搜索算法设定为1级时，即可完整覆盖合环点直接相邻的电气区域，满足工程计算精度要求，避免过度划分导致计算量指数增长。
- 开关统计功能在一个工频周期内执行10次独立混合仿真，可精确量化不同合环相角下的冲击电流波动区间，消除单一相角仿真的偶然性。
- 自动转换算法覆盖线路、变压器、负荷、电容、电抗等占电网绝大多数的简单元件，复杂元件通过模型库检索匹配，彻底消除人工录入参数带来的建模误差与漏项。


## 关键公式

### 机电-电磁混合仿真戴维南接口方程

$$$V_{abc}(t) = V_{th,abc}(t) - Z_{th,abc} \cdot I_{abc}(t)$$$

*用于机电网络向电磁网络提供边界条件，在电磁暂态求解器中作为电压源与串联阻抗注入，驱动局部高频暂态计算。*

### 相量-瞬时值时域重构方程

$$$v(t) = \sqrt{2} |V| \cos(\omega t + \theta)$$$

*在每次数据交换时刻（$t-DTE$），将机电侧输出的基波相量转换为电磁侧所需的三相瞬时值，实现跨域数据无缝衔接。*



## 验证详情

- **验证方式**: 实际区域电网仿真验证与功能对比分析
- **测试系统**: 新疆喀什地区电网（包含4个变电站组成的环形输配电网）
- **仿真工具**: 自主开发的机电-电磁暂态混合仿真计算系统（集成PQ分解/牛顿法潮流模块、机电暂态引擎、电磁暂态引擎及Windows单机多核并行调度模块）
- **验证结果**: 系统成功实现合环点自动分网与模型转换，潮流计算准确反映功率转移；混合仿真精确输出合环冲击电流瞬时值与过电压波形；开关统计功能有效识别最恶劣合环相角下的最大冲击电流，计算结果可直接与继电保护整定值比对，为喀什电网合环操作提供可靠的安全评估依据，验证了系统在工程应用中的准确性与实用性。
