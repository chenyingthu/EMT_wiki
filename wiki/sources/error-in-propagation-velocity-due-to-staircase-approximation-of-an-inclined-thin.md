---
title: "Error in propagation velocity due to staircase approximation of an inclined thin wire in FDTD surge Simulation"
type: source
authors: ['T. Noda', 'R. Yonezawa', 'S. Yokoyama', 'Y. Takahashi']
year: 2004
journal: "IEEE Transactions on Power Delivery;2004;19;4;10.1109/TPWRD.2004.835396"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/18/Noda 等 - 2004 - Error in propagation velocity due to staircase approximation of an inclined thin wire in FDTD surge.pdf"]
---

# Error in propagation velocity due to staircase approximation of an inclined thin wire in FDTD surge Simulation

**作者**: T. Noda, R. Yonezawa, S. Yokoyama 等
**年份**: 2004
**来源**: `18/Noda 等 - 2004 - Error in propagation velocity due to staircase approximation of an inclined thin wire in FDTD surge.pdf`

## 摘要

—This paper presents the result of a study on the error in propagation velocity introduced by the staircase approximation of a thin wire in the ﬁnite difference time domain (FDTD) surge simulation. The FDTD method directly solves Maxwell’s equations by discretizing the space of interest into cubic cells. Thus, it is suit- able for solving very-fast surge phenomena which cannot be dealt with by conventional techniques based on the lumped- and dis- tributed-parameter circuit theories. However, FDTD has a limita- tion that the shape of a conductive object must be modeled by a combination of sides of cells with forced zero electric ﬁelds. This indicates that a thin wire, one of the most important components in the surge simulation, results in a staircase approximation, if the wire is not paral

## 核心贡献


- 提出并量化了FDTD中倾斜细线阶梯近似导致的波速误差特性
- 揭示了相邻导体单元间互感耦合对减缓波速误差的补偿机制
- 验证了阶梯近似在工程浪涌仿真中的实用精度与适用边界


## 使用的方法


- [[有限差分时域法-fdtd|有限差分时域法(FDTD)]]
- [[阶梯近似算法-sca|阶梯近似算法(SCA)]]
- [[麦克斯韦方程直接求解|麦克斯韦方程直接求解]]
- [[高斯脉冲激励|高斯脉冲激励]]


## 涉及的模型


- [[倾斜细线模型|倾斜细线模型]]
- [[双线导体系统|双线导体系统]]
- [[fdtd立方网格模型|FDTD立方网格模型]]


## 相关主题


- [[浪涌仿真|浪涌仿真]]
- [[波速误差分析|波速误差分析]]
- [[电磁暂态分析|电磁暂态分析]]
- [[空间离散化误差|空间离散化误差]]
- [[快速暂态现象|快速暂态现象]]


## 主要发现


- 阶梯近似使倾斜细线等效路径变长，理论最大波速减速可达42.3%
- 实际FDTD仿真中互感耦合显著补偿误差，最大波速误差小于14%
- 典型工程倾斜角度下阶梯近似仍能提供满足精度要求的浪涌结果



## 方法细节

### 方法概述

本文采用有限差分时域（FDTD）法直接求解麦克斯韦方程组，系统研究倾斜细线在阶梯近似（SCA）下引入的电磁波传播速度误差。FDTD将计算空间离散为立方网格，导体边界必须沿网格边建模（强制切向电场为零），导致非坐标轴平行的倾斜细线被近似为沿网格线的锯齿状路径。为量化该误差，构建了自由空间中的对称双线导体系统，在坐标原点施加高斯脉冲电流源激励。通过极坐标参数（$\theta$, $\phi$）系统改变导线空间倾角，记录脉冲峰值到达远端的时间差以计算实际传播速度。研究核心在于对比纯几何路径延长导致的理论波速衰减与实际FDTD全波仿真结果，揭示相邻导体单元间互感耦合对波速误差的物理补偿机制，从而评估SCA在工程浪涌仿真中的精度边界。

### 数学公式


**公式1**: $$$L = \sqrt{(x_B-x_A)^2 + (y_B-y_A)^2 + (z_B-z_A)^2}$$$

*理想倾斜细线的实际欧氏几何长度*


**公式2**: $$$L_{\text{SCA}} = |x_B-x_A| + |y_B-y_A| + |z_B-z_A|$$$

*阶梯近似路径长度（曼哈顿距离），用于理论误差估算*


**公式3**: $$$v_{\text{virtual}} = v_0 \frac{L}{L_{\text{SCA}}}$$$

*假设无互感耦合时的理论虚拟传播速度，反映纯几何路径延长导致的波速衰减*


**公式4**: $$$J(t) = I_0 \exp(-a(t-t_0)^2)$$$

*高斯脉冲电流源激励波形，用于激发宽频带暂态电磁波*


**公式5**: $$$\Delta t = \frac{\Delta s}{c_0 \sqrt{3}} \times 0.99$$$

*满足Courant稳定性条件的FDTD时间步长计算公式*


**公式6**: $$$v = \frac{L}{t_{\text{peak}}}$$$

*基于仿真波形峰值到达时间差计算的实际传播速度*


### 算法步骤

1. 步骤1：将当前计算点初始化为倾斜细线的起点A。

2. 步骤2：从当前点出发，识别所有朝向终点B的相邻网格边（2D平面为2条，3D空间为3条）。分别计算每条边远端点到理想直线AB的垂直距离。

3. 步骤3：比较上述垂直距离，选择距离最小的网格边作为阶梯路径的下一段。

4. 步骤4：将当前点移动至所选网格边的远端点。

5. 步骤5：重复执行步骤2至步骤4，直至当前点与终点B重合。最终生成的锯齿状路径即为最小偏差的阶梯近似（SCA），在FDTD计算中将该路径所在网格边上的电场强制置零以模拟理想导体。


### 关键参数

- **空间步长**: 1 cm

- **网格规模**: 241 (x) × 180 (y) × 241 (z) 个Yee元胞

- **导线物理长度**: 约 1 m（受网格点限制微调）

- **电流源幅值**: 1 A

- **高斯脉冲参数**: a = 1.2 × 10^18, t0 = 2.5 ns

- **倾角扫描范围**: θ ∈ [0°, 45°], φ ∈ [0°, 90°], 步长 5°

- **边界条件**: Liao二阶吸收边界（6个外边界）

- **稳定性系数**: 0.99 (Courant条件)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 坐标轴平行基准导线 (θ=0°, φ=0°) | 导线与网格轴完全平行，无阶梯近似效应。脉冲波形无畸变，传播速度等于介质本征速度，作为误差评估的零基准。 | 误差为0%，作为归一化基准值 |

| 最大空间倾角导线 (θ=45°, φ=90°) | 导线处于极坐标最大倾斜方向，阶梯路径最长。理论几何估算波速应下降42.3%，但实际FDTD仿真记录到的波速下降幅度显著减小。 | 实际波速误差<14%，远低于理论几何估算的42.3%衰减 |

| 全倾角扫描特性测试 (θ: 0°~45°, φ: 0°~90°) | 以5°为步长遍历所有空间倾角组合，提取正负峰值时间差计算波速。波速随倾角增大呈非线性下降，但下降曲线平缓，未出现数值色散导致的剧烈振荡。 | 全工况下最大波速偏差严格控制在14%以内，验证了SCA在宽角度范围内的稳定性 |



## 量化发现

- 阶梯近似导致的最大理论波速衰减为42.3%（基于纯几何曼哈顿距离假设）。
- 实际FDTD全波仿真中，相邻导体单元间的互感耦合产生电磁补偿效应，使最大波速误差被显著抑制至14%以内。
- 仿真空间步长固定为1 cm时，波速误差特性具有尺度不变性，结论可推广至任意网格尺寸。
- 高斯脉冲激励下，波速计算基于正负峰值时间差，倾角每增加5°，波速呈单调非线性下降，但始终保持在工程可接受精度范围内。
- 未应用半径修正算法的纯SCA模型，在快速浪涌暂态分析中仍能提供满足工程需求的实用精度。


## 关键公式

### 理论虚拟波速公式

$$$v_{\text{virtual}} = v_0 \frac{L}{L_{\text{SCA}}}$$$

*用于估算忽略电磁耦合时，仅由阶梯路径几何延长导致的波速衰减上限*

### FDTD仿真波速提取公式

$$$v = \frac{L}{t_{\text{peak}}}$$$

*通过记录高斯脉冲峰值在导线两端的传播时间差，反演实际电磁波传播速度*

### Courant稳定性条件

$$$\Delta t = \frac{\Delta s}{c_0 \sqrt{3}} \times 0.99$$$

*确保3D FDTD显式时间积分算法数值稳定的最大时间步长约束*



## 验证详情

- **验证方式**: 全波FDTD数值仿真与理论几何估算对比分析
- **测试系统**: 自由空间中的对称双线导体系统（长度约1m，原点激励，远端开路）
- **仿真工具**: 基于FDTD的通用浪涌仿真代码（作者团队自研，集成细线模型与Liao吸收边界）
- **验证结果**: 通过系统扫描极坐标倾角，量化了阶梯近似引入的波速误差。结果表明，尽管理论几何路径延长会导致显著波速下降，但电磁场互感耦合机制有效补偿了该误差，最大偏差控制在14%以内。该验证证实了SCA在电力系统快速浪涌暂态仿真中具备足够的工程精度与实用性，为FDTD替代矩量法（MoM）处理复杂倾斜导体提供了理论依据。
