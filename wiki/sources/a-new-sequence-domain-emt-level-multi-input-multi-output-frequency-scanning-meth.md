---
title: "A new sequence domain EMT-level multi-input multi-output frequency scanning method for inverter based resources"
type: source
authors: ['Lei Meng']
year: 2023
journal: "Electric Power Systems Research, 220 (2023) 109312. doi:10.1016/j.epsr.2023.109312"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/02/Meng 等 - 2023 - A new sequence domain EMT-level multi-input multi-output frequency scanning method for inverter base.pdf"]
---

# A new sequence domain EMT-level multi-input multi-output frequency scanning method for inverter based resources

**作者**: Lei Meng
**年份**: 2023
**来源**: `02/Meng 等 - 2023 - A new sequence domain EMT-level multi-input multi-output frequency scanning method for inverter base.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. A new sequence domain EMT-level multi-input multi-output frequency a Department of Electrical Engineering, Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong b Department of Electrical Engineering, Polytechnique Montr´eal, Montreal, QC, Canada The impedance-based stability analysis (IBSA) is an effective method for identifying instability issues caused by

## 核心贡献


- 提出静止坐标系下耦合序域多输入多输出频扫方法，有效计及镜像频率效应
- 无需扰动与测量信号坐标变换，计算负担较现有耦合序域方法降低一半
- 实现谐振频率与镜像频率的精准区分，提升阻抗稳定性分析精度


## 使用的方法


- [[emt级频扫法|EMT级频扫法]]
- [[阻抗稳定性分析|阻抗稳定性分析]]
- [[耦合序域扫描|耦合序域扫描]]
- [[多输入多输出建模|多输入多输出建模]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 涉及的模型


- [[全功率变流器风电场|全功率变流器风电场]]
- [[网侧变流器|网侧变流器]]
- [[锁相环控制模型|锁相环控制模型]]
- [[弱电网戴维南等效模型|弱电网戴维南等效模型]]


## 相关主题


- [[阻抗稳定性分析|阻抗稳定性分析]]
- [[镜像频率效应|镜像频率效应]]
- [[频域阻抗测量|频域阻抗测量]]
- [[弱电网交互|弱电网交互]]
- [[次同步振荡|次同步振荡]]
- [[逆变器型资源建模|逆变器型资源建模]]


## 主要发现


- 在弱电网工况下精准识别108Hz谐振与12Hz镜像频率，验证方法有效性
- 相比正序与dq频扫法，CSD扫描在阻抗稳定性分析中精度更高且计算耗时减半
- 电磁暂态仿真验证表明，该方法可有效预测全功率风机并网系统的失稳振荡



## 方法细节

### 方法概述

本文提出一种静止坐标系（SF）下的耦合序域（CSD）多输入多输出（MIMO）电磁暂态（EMT）级频扫方法（CSD-scan）。该方法直接在三相相域注入平衡正弦电压扰动，利用离散傅里叶变换（DFT）同步提取扰动频率$f_i$及其镜像频率$|f_i-2f_b|$处的正负序电流响应，构建完整计及镜像频率效应（MFE）的MIMO导纳矩阵。通过挖掘正负序导纳在频域的共轭对称特性，仅需单次扫描即可覆盖全频段，彻底免除了传统dq频扫法所需的坐标变换与信号重构步骤。提取的CSD阻抗直接用于广义奈奎斯特判据（GNC）稳定性评估，能够精准解耦并区分物理谐振频率与数学镜像频率，在保持与dq域方法同等精度的前提下，将计算负担降低50%，为逆变器型资源并网稳定性分析提供高效、高精度的频域工具。

### 数学公式


**公式1**: $$$Y_{IBR}^{p,p}(f_i) = \frac{|I^p(f_i)|}{|V^p(f_i)|} \angle (\angle I^p(f_i) - \angle V^p(f_i))$$$

*正序电压扰动下，IBR在扰动频率处的正序自导纳计算式，用于表征同频响应特性*


**公式2**: $$$Y_{IBR}^{n,p}(f_i) = \frac{|I^n(f_i-2f_b)|}{|V^p(f_i)|} \angle (\angle I^n(f_i-2f_b) - \angle V^p(f_i))$$$

*正序电压扰动下，IBR在镜像频率处的负序互导纳计算式，用于量化镜像频率耦合效应*


**公式3**: $$$Z_{IBR}^{CSD}(f_i) = (Y_{IBR}^{CSD}(f_i))^{-1} - \text{diag}([Z_{sys}(f_i) \ Z_{sys}(f_i-2f_b)])$$$

*系统阻抗剥离公式，从测量总导纳中扣除电网侧等效阻抗，获取纯净的IBR CSD阻抗*


**公式4**: $$$Y_{IBR}^{p,n}(f_i) = Y_{IBR}^{n,p*}(2f_b-f_i), \quad Y_{IBR}^{n,n}(f_i) = Y_{IBR}^{p,p*}(2f_b-f_i)$$$

*频域共轭对称关系式，利用该式可通过单次扫描推导镜像频段导纳，使计算量减半*


**公式5**: $$$L^{CSD}(f) = Z_{Grid}^{CSD}(f) Y_{IBR}^{CSD}(f)$$$

*CSD域开环传递函数定义，结合广义奈奎斯特判据用于多变量系统稳定性判定*


### 算法步骤

1. 系统初始化与稳态快照加载：运行EMT仿真至稳态，记录系统快照以跳过后续每次扫描的初始化暂态过程，提升效率。

2. 注入扰动信号：在并网点（PoI）叠加幅值为0.01 p.u.的平衡三相正弦电压扰动$v_{p-abc}(f_i, t)$，保持电网侧戴维南等效源不变。

3. 信号测量与频谱提取：采集注入点的三相电流响应，应用矩形窗DFT分析，提取扰动频率$f_i$及镜像频率$|f_i-2f_b|$处的正负序电流相量幅值与相位。

4. 导纳矩阵分量计算：基于测得的电压/电流相量，利用幅值比与相位差分别计算$Y_{IBR}^{p,p}$、$Y_{IBR}^{n,p}$（正序扰动）及$Y_{IBR}^{p,n}$、$Y_{IBR}^{n,n}$（负序扰动）四个MIMO导纳分量。

5. 收敛性判定：实时监测各导纳分量幅值与相角的变化率，当满足预设容差（如1%）且持续稳定时，判定收敛并终止当前频率仿真。

6. 阻抗剥离与矩阵构建：将收敛后的总导纳求逆，减去电网侧等效阻抗对角阵，得到IBR的CSD阻抗矩阵。

7. 对称性补全与频段扩展：利用共轭对称公式自动计算镜像频段导纳，无需额外扫描，完成全频段（1Hz~2fb-1Hz）阻抗建模。


### 关键参数

- **扰动幅值**: 0.01 p.u.（确保线性响应且不触发变流器饱和）

- **DFT窗长**: 1 s（恒定，覆盖基频与扰动频率整数周期）

- **强制运行时间**: 6 s（防止收敛检测程序过早终止）

- **收敛容差**: 1%（幅值与相角变化率阈值）

- **扫描频率范围**: 1 Hz ~ 119 Hz（步长1 Hz，覆盖次同步至超同步频段）

- **系统基准值**: 833.5 MVA, 500 kV, 60 Hz



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 弱电网FSC风电场失稳场景（SCR由3.87骤降至1.02） | CSD-scan识别出系统谐振频率为108 Hz，相位裕度为-0.5°；dq-scan识别谐振频率为108 Hz（dq域48 Hz），相位裕度为-0.1°；传统p-scan识别频率为109.5 Hz，相位裕度为1.7°。EMT时域仿真观测到108 Hz主导振荡与12 Hz镜像振荡。 | CSD-scan与dq-scan频率识别误差为0 Hz，相位裕度偏差仅0.4°；p-scan因忽略镜像频率效应导致相位裕度高估2.2°，误判为临界稳定。CSD-scan仿真耗时1983.9 s，与dq-scan的1991.1 s基本持平，但较文献现有耦合序域方法计算时间减少50%。 |



## 量化发现

- CSD-scan与dq-scan在谐振频率识别上完全一致（108 Hz），相位裕度偏差仅0.4°，验证了静止坐标系方法的等效高精度
- 传统正序频扫法(p-scan)相位裕度计算结果为1.7°，较真实失稳裕度高估2.2°，导致无法识别系统失稳
- CSD-scan在1~119 Hz全频段内仅需单次扰动扫描，理论计算耗时较现有双扰动耦合序域方法严格降低50%
- EMT时域仿真复现的振荡频率为108 Hz（谐振）与12 Hz（镜像），与CSD-IBSA频域预测值误差为0 Hz
- 扰动幅值设定为0.01 p.u.可在保证信噪比的同时避免触发变流器非线性饱和，DFT窗长≥1 s可确保全频段收敛


## 关键公式

### CSD MIMO导纳矩阵构建式

$$$Y_{IBR}^{CSD}(f_i) = \begin{bmatrix} Y_{IBR}^{p,p}(f_i) & Y_{IBR}^{p,n}(f_i) \\ Y_{IBR}^{n,p}(f_i) & Y_{IBR}^{n,n}(f_i) \end{bmatrix}$$$

*用于在静止坐标系下完整表征IBR正负序频率间的交叉耦合特性，是后续阻抗剥离与稳定性分析的基础*

### 电网阻抗剥离公式

$$$Z_{IBR}^{CSD}(f_i) = (Y_{IBR}^{CSD}(f_i))^{-1} - \text{diag}([Z_{sys}(f_i) \ Z_{sys}(f_i-2f_b)])$$$

*在频扫测量后，从包含电网阻抗的总测量值中精确扣除系统侧戴维南等效阻抗，获取纯IBR阻抗模型*

### CSD域开环传递函数

$$$L^{CSD}(f) = Z_{Grid}^{CSD}(f) Y_{IBR}^{CSD}(f)$$$

*结合广义奈奎斯特判据（GNC），通过特征值轨迹是否包围(-1, j0)点判定多变量并网系统的稳定性*



## 验证详情

- **验证方式**: EMT时域仿真对比与广义奈奎斯特频域分析交叉验证
- **测试系统**: 含全功率变流器(FSC)风电场的弱电网系统（双回线并联，切除一回后SCR降至1.02）
- **仿真工具**: EMT级电磁暂态仿真程序（支持自定义频扫脚本与DFT分析，如PSCAD/EMTDC或同类平台）
- **验证结果**: CSD-scan提取的阻抗模型与dq-scan模型在Nyquist图上高度重合，均准确包围(-1, j0)点预测失稳；时域仿真复现108 Hz振荡，验证了CSD-IBSA在弱电网交互分析中的高精度；同时证明该方法无需坐标变换即可实现与dq域等效的精度，且计算效率提升显著，具备工程黑盒模型测试的实用价值。
