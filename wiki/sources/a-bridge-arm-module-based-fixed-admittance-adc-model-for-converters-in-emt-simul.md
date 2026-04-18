---
title: "A Bridge-Arm-Module-Based Fixed-Admittance ADC Model for Converters in EMT Simulation"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Power Delivery;2025;40;6;10.1109/TPWRD.2025.3608898"
tags: ['adc', 'fixed-admittance']
created: "2026-04-13"
sources: ["EMT_Doc/01/Cao 等 - 2025 - A Bridge-Arm-Module-Based Fixed-Admittance ADC Model for Converters in EMT Simulation.pdf"]
---

# A Bridge-Arm-Module-Based Fixed-Admittance ADC Model for Converters in EMT Simulation

**作者**: 
**年份**: 2025
**来源**: `01/Cao 等 - 2025 - A Bridge-Arm-Module-Based Fixed-Admittance ADC Model for Converters in EMT Simulation.pdf`

## 摘要

—Electromagnetic transient (EMT) simulation models, especially converter models, face challenges in meeting the demand for precise and fast simulation of complex dynamics in modern distribution systems. Difﬁculty in achieving both high accuracy and efﬁciency simultaneously is a key issue in converter modeling, especially in real-time simulation. To address this issue, this paper proposes a parametric ﬁxed-admittance associated discrete circuit (ADC) converter model based on bridge arm modules (BAMs), with the aim of improving simulation precision and efﬁciency. The paper ﬁrst establishes a parametric ADC model of the BAM. An optimal parameter calculation approach is introduced to ensure high ﬁdelity through analysis of steady-state and transient char- acteristics. Furthermore, to mitigate 

## 核心贡献


- 提出基于桥臂模块的参数化固定导纳ADC模型，保持导纳矩阵恒定以提升计算效率
- 设计最优参数计算方法，确保模型稳态与暂态误差快速收敛至高保真水平
- 开发交叉重初始化方法修正状态切换误差，有效降低虚拟功率损耗且不增加计算负担


## 使用的方法


- [[关联离散电路法-adc|关联离散电路法(ADC)]]
- [[固定导纳建模|固定导纳建模]]
- [[后向欧拉法|后向欧拉法]]
- [[交叉重初始化-cri|交叉重初始化(CRI)]]
- [[诺顿等效|诺顿等效]]


## 涉及的模型


- [[桥臂模块-bam|桥臂模块(BAM)]]
- [[电力电子换流器|电力电子换流器]]
- [[l-c型adc模型|L/C型ADC模型]]
- [[开关电阻模型|开关电阻模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[实时仿真|实时仿真]]
- [[换流器建模|换流器建模]]
- [[虚拟功率损耗|虚拟功率损耗]]
- [[状态切换误差修正|状态切换误差修正]]


## 主要发现


- 仿真与实验验证模型兼具高精度与高效率，在多种工况下均保持良好适用性
- 交叉重初始化方法有效消除切换初始误差并显著降低虚拟损耗，未牺牲计算速度
- 模型避免重复矩阵求逆，时间复杂度显著低于传统开关电阻模型，适合大规模系统



## 方法细节

### 方法概述

提出基于桥臂模块(BAM)的参数化固定导纳关联离散电路(ADC)模型。该模型突破传统单开关建模局限，将上下开关管、桥臂电感与直流侧电容整合为统一模块，采用梯形积分法(TR)离散化建立含可调参数α（电压系数）与β（电流系数）的诺顿等效电路。通过Z变换终值定理推导理想稳态条件，结合KCL/KVL构建离散状态空间方程，以状态转移矩阵谱半径ρ(A1)为核心指标进行参数寻优，实现暂态数值误差的零谱半径快速收敛。针对开关状态切换引发的初始误差，提出交叉重初始化(CRI)算法进行跨状态变量修正，并辅以基于接口电气量与拓扑逻辑的改进型状态判定策略。该模型在整个仿真过程中保持节点导纳矩阵恒定，彻底消除重复矩阵求逆开销，在维持固定导纳模型高计算效率的同时，有效抑制虚拟功率损耗与虚假谐波尖峰。

### 数学公式


**公式1**: $$i_{sw}^n = G_{eq,sw} u_{sw}^n + I_{inj,sw}^n, \quad I_{inj,sw}^n = \alpha G_{eq,sw} u_{sw}^{n-1} + \beta i_{sw}^{n-1}$$

*参数化ADC开关模型离散方程，定义等效导纳与历史注入电流源，引入可调系数α和β以优化动态响应*


**公式2**: $$\alpha_i \neq -1, \beta_i = 1 \text{ (ON)}; \quad \alpha_i = -1, \beta_i \neq 1 \text{ (OFF)}$$

*基于Z变换终值定理推导的开关单元理想稳态特性充要条件*


**公式3**: $$x_1^n = A_1 x_1^{n-1} + b_1^n$$

*BAM离散状态空间动态方程，x1为状态变量，A1为状态转移矩阵，b1为输入向量*


**公式4**: $$\rho(A_1) = \max\{|\lambda_1|, |\lambda_2|\}$$

*状态矩阵谱半径计算公式，用于评估暂态误差收敛速度，ρ越小收敛越快*


### 算法步骤

1. 模块离散化：对BAM内上下开关、电感、电容应用梯形积分法(TR)，建立含参数α、β的通用诺顿等效离散方程，替代传统固定L/C参数。

2. 稳态约束推导：利用Z变换终值定理分析开关导通/关断状态下的电压电流极限值，得出保证理想稳态特性的参数约束条件（α≠-1,β=1导通；α=-1,β≠1关断）。

3. 状态空间构建：基于基尔霍夫电压/电流定律，联立模块内部节点方程，推导以开关电压和电流为状态变量的离散动态方程x1^n = A1*x1^(n-1) + b1^n。

4. 谱半径寻优：计算状态矩阵A1的特征值与谱半径ρ(A1)，在收敛域内求解使ρ(A1)=0的参数组合，实现误差单步衰减至稳态。

5. 参数优选与导纳配置：对比零谱半径参数组，选取稳态误差更小的Group I组合，并依据误差界O(max{kL, kC})设定等效导纳配置准则Geq,L << Geq,1+Geq,2 << Geq,C。

6. 切换误差修正：在检测到状态切换时刻，触发交叉重初始化(CRI)机制，利用切换前后的交叉状态变量对历史注入电流源进行瞬时重赋值，消除初始跳变误差。

7. 状态判定与降级处理：设计基于接口电压/电流及上一时刻状态的改进型逻辑判定器；当进入非互补导通状态（如双管关断）时，自动切换至传统L/C-ADC模型进行兼容仿真。


### 关键参数

- **G_eq,L**: h/(2L_ac)，电感等效导纳

- **G_eq,C**: 2C_dc/h，电容等效导纳

- **α, β**: 电压与电流历史系数，用于调节暂态收敛特性与稳态精度

- **k_i, k_L, k_C**: 各元件导纳占总导纳的比例系数，决定误差收敛阶数与数值稳定性

- **h**: EMT仿真步长



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 稳态与暂态误差收敛测试 | 在最优参数配置下，状态矩阵谱半径ρ(A1)=0，暂态数值误差实现单步衰减至稳态，无长尾收敛过程 | 相比传统L/C-ADC模型（ρ=1或√k1），误差收敛速度提升一个数量级，彻底消除长暂态振荡 |

| 虚拟功率损耗与谐波抑制 | 通过参数优化与CRI修正，开关切换瞬间的电压/电流虚假谐波尖峰被有效抑制，虚拟功率损耗显著降低 | 在相同仿真步长下，虚拟损耗较L/C-ADC降低至可忽略水平，允许使用更大步长而不失稳 |

| 计算复杂度对比 | 全仿真周期仅需1次K维导纳矩阵求逆，历史电流源更新为O(K)复杂度 | 相比RON/ROFF模型需至少2mN次矩阵求逆，计算复杂度从O(2mN·K^3)降至O(K^3)，实时仿真效率提升显著 |



## 量化发现

- 状态矩阵最优谱半径ρ(A1)=0，实现暂态误差单步零收敛
- 模型截断误差阶数为O(max{kL, kC})，当要求误差<1%时，需满足2kL/(1+√k1)<0.01且2kC(1+√k1)<0.01
- 等效导纳配置准则为Geq,L << Geq,1+Geq,2 << Geq,C，确保数值稳定性与精度
- 计算复杂度由传统开关电阻模型的O(2mN·K^3)降至固定导纳模型的O(K^3)，矩阵求逆次数从2mN次减少至1次


## 关键公式

### BAM-ADC最优参数配置(Group I)

$$\alpha_1 = -1, \beta_1 = \frac{\sqrt{k_1}}{\sqrt{1+k_1}}, \alpha_2 = \frac{\sqrt{k_1+k_2-k_L}}{k_2}, \beta_2 = 1$$

*当S1关断、S2导通时，使状态矩阵谱半径为零的最优参数组合，用于实现最快暂态误差收敛*

### 暂态误差收敛界

$$\varepsilon_{x_1}^n = O\left(\max\left\{2k_L(1+\sqrt{k_1}), 2k_C(1+\sqrt{k_1})\right\}\right)$$

*用于评估模型离散化后的数值误差量级，指导等效导纳参数的选取以满足特定精度要求*

### 参数化ADC离散方程

$$i_{sw}^n = G_{eq,sw} u_{sw}^n + \alpha G_{eq,sw} u_{sw}^{n-1} + \beta i_{sw}^{n-1}$$

*BAM模型核心离散化公式，替代传统固定L/C参数，通过α/β调节实现高精度固定导纳建模*



## 验证详情

- **验证方式**: 仿真与实验对比验证
- **测试系统**: 典型电力电子换流器拓扑（含半桥/全桥结构及非互补导通工况）
- **仿真工具**: EMT仿真平台（对比PSCAD/RTDS/OPAL-RT内置模型），结合理论推导与数值实验
- **验证结果**: 验证表明BAM-ADC模型在多种工况下均保持高保真度，稳态与暂态误差快速收敛，虚拟功率损耗与虚假谐波显著降低，且计算效率满足实时仿真需求，具备广泛的工程适用性
