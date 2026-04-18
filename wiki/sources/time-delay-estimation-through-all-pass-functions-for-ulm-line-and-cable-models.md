---
title: "Time-delay estimation through all-pass functions for ULM line and cable models"
type: source
authors: ['S. Loaiza-Elejalde']
year: 2026
journal: "Electric Power Systems Research, 252 (2026) 112414. doi:10.1016/j.epsr.2025.112414"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/38/Loaiza-Elejalde 等 - 2026 - Time-delay estimation through all-pass functions for ULM line and cable models.pdf"]
---

# Time-delay estimation through all-pass functions for ULM line and cable models

**作者**: S. Loaiza-Elejalde
**年份**: 2026
**来源**: `38/Loaiza-Elejalde 等 - 2026 - Time-delay estimation through all-pass functions for ULM line and cable models.pdf`

## 摘要

Time-delay estimation through all-pass functions for ULM line and , J.L. Naredo a, Martin G. Vega-Grijalva b, O. Ramos-Lea˜nos c Traveling-wave line models, such as the ULM, are widely used in time-domain EMT simulations for power systems. These models require the rational approximation of both the characteristic admittance matrix Yc, and the propagation matrix H. Rational fitting of H is challenging due to the inclusion of a mix of modal delays in all

## 核心贡献



- 提出了一种基于全通函数与延迟均衡的迭代时延估计方法，用于改进ULM线路与电缆模型的传播矩阵有理拟合
- 该方法在拟合过程中严格保证了合成模型的因果性与最小相位特性，且相比传统均方根误差最小化方法具有更高的计算效率

## 使用的方法


- [[vector-fitting]]

## 涉及的模型


- [[transmission-line]]
- [[cable]]

## 相关主题


- [[frequency-dependent]]
- [[passivity]]

## 主要发现



- 所提方法通过全通滤波器提取模态时延，成功解决了传统Bode积分法在截止频率选取上的局限性，确保了有理近似的因果性
- 在合成传递函数、地下电缆系统及架空线路EMT响应测试中，新方法在保持拟合精度与现有方法相当的前提下，显著降低了迭代次数

## 方法细节

### 方法概述

本文提出了一种基于全通滤波器（All-Pass Filter, APF）和延迟均衡的迭代时延估计方法，用于ULM（Universal Line Model）线路和电缆模型中传播矩阵H的模态时延识别。该方法通过有理拟合和全通分解，确保合成模型具有因果性和最小相位特性。与传统基于均方根误差（rms-error）最小化的方法（如Golden Section搜索）不同，本方法通过迭代提取全通分量并计算其群延迟修正量，逐步逼近真实的模态时延，直至所有零点位于复平面左半平面（LHP），从而严格保证最小相位条件。

### 数学公式


**公式1**: $$$H_{m,i} = e^{-(\alpha_i + j\beta_i)l}$$$

*第i个模态的传播函数，其中$\alpha_i$为模态衰减，$\beta_i$为模态相位，$l$为线路长度*


**公式2**: $$$H_{m,i} = e^{-(\alpha_i + j\beta_{min,i})l} e^{-j\omega\tau_i} = H_{min,i} e^{-j\omega\tau_i}$$$

*将模态传播函数分解为最小相位部分$H_{min,i}$和纯延迟部分$e^{-j\omega\tau_i}$，其中$\tau_i$为第i个模态的时延*


**公式3**: $$$H(j\omega) = H_{min}(j\omega)H_{ap}(j\omega)$$$

*任意有理系统分解为最小相位系统$H_{min}$和全通系统$H_{ap}$的乘积，全通系统的零点位于右半平面（RHP），与$H_{min}$的极点呈镜像对称*


**公式4**: $$$\tau_i = \frac{l}{v(\Omega_i)} + \frac{\phi_{min,i}(\Omega_i)}{\Omega_i}$$$

*基于Bode积分的传统时延估计公式，其中$v(\Omega_i)$为在截止频率$\Omega_i$处的模态速度，$\phi_{min,i}$为最小相位角*


**公式5**: $$$H \approx \sum_{i=1}^{N_g} \sum_{k=1}^{N_{H,i}} \frac{R_{i,k}}{j\omega - p_{i,k}} e^{-j\omega\tau_i}$$$

*传播矩阵的有理近似表达式，其中$N_g$为延迟组数，$N_{H,i}$为第i组的近似阶数，$R_{i,k}$和$p_{i,k}$分别为留数矩阵和极点*


### 算法步骤

1. 初始化：获取初始时延估计值$\tau_{est}$（可采用Bode积分法或基于物理速度的粗略估计）

2. 延迟提取：计算辅助函数$H_{aux} = H \cdot e^{j\omega\tau_{est}}$，即从原始传播函数中移除当前估计的时延

3. 有理拟合：使用Vector Fitting (VF)方法对$H_{aux}$进行有理拟合，获得零极点表示

4. 最小相位检查：分析拟合结果的零点位置。如果所有零点均位于复平面左半平面（LHP），则判定为最小相位系统，跳转至步骤8

5. 全通分解：若存在右半平面（RHP）零点，构建全通函数$H_{ap}$，使其包含所有RHP零点及其在LHP的镜像极点

6. 群延迟计算：计算全通函数$H_{ap}$的群延迟$\tau_{ap}(\omega) = -\frac{d\angle H_{ap}(j\omega)}{d\omega}$，并对频率进行平均得到延迟修正量$\Delta\tau = \text{mean}(\tau_{ap}(\omega))$

7. 迭代更新：更新时延估计$\tau_{est} = \tau_{est} + \Delta\tau$，返回步骤2

8. 收敛输出：输出最终时延估计$\tau_{est}$和对应的最小相位函数$H_{min}$，用于后续的EMT仿真


### 关键参数

- **收敛准则**: 有理拟合后的所有零点位于复平面左半平面（LHP），即系统满足最小相位条件

- **初始时延估计**: 可采用Bode积分法（截止频率$\Omega$处幅度衰减至0.1）或基于光速的物理估计

- **全通函数分解**: 将高阶全通函数分解为一阶和二阶级联，以准确计算群延迟

- **延迟分组**: 将具有相似延迟的模态归为一组（delay group），每组共享一个代表时延$\tau_i$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 合成传递函数（常数延迟识别） | 针对已知常数延迟的合成传递函数进行时延识别测试，验证了方法在理想条件下的准确性。结果表明所提方法能准确识别预设延迟，且相比前代方法（2019年版本）有显著改进 | 相比基于Golden Section (GS)的均方根误差最小化方法，迭代次数显著减少（具体数值原文未明确给出，但描述为'substantially fewer iterations'），同时保持因果性 |

| 三根地下电缆系统（每根4层导体） | 对具有4层导体结构的三根地下电缆进行模态时延估计。电缆系统的传播矩阵包含复杂的混合模态延迟，测试验证了方法在多导体复杂电缆系统中的适用性 | 成功识别各模态时延，确保合成模型满足因果性（无超光速传播），而传统GS方法在某些情况下会产生违反因果性的时延估计（传播速度超过光速） |

| 架空线路EMT瞬态响应 | 使用Numerical Laplace Transform (NLT)技术作为参考基准（采用$2^{15}$个采样点，精度 tuned to $10^{-8}$），对比了Bode积分法、GS法和所提APF方法的线路暂态响应精度 | 所提APF方法与GS方法达到相似的拟合精度（similar accuracies），但APF方法严格保证因果性和最小相位特性，而GS方法在某些情况下会产生非因果响应 |



## 量化发现

- 计算效率：所提方法比基于Golden Section (GS)的均方根误差最小化方法需要更少的迭代次数（fewer iterations）即可收敛
- 因果性保证：所提方法严格确保所有模态的传播速度不超过光速（speed of light），而GS方法在某些情况下会产生因果性违反（causality violations）
- 相位特性：通过全通滤波器迭代修正，最终合成模型严格满足最小相位（minimum-phase）条件，即所有零点位于复平面左半平面
- 参考精度：在架空线路测试中，使用Numerical Laplace Transform作为参考解，采样点数为$2^{15}$，数值精度设置为$10^{-8}$
- 截止频率问题：传统Bode积分法在截止频率$\Omega$的选取上存在局限性（原文指出magnitude may not decay to 0.1 within the frequency range），所提方法通过迭代全通补偿克服了这一问题


## 关键公式

### 全通-最小相位分解

$$$H(j\omega) = H_{min}(j\omega)H_{ap}(j\omega)$$$

*核心理论基础，用于将非最小相位系统分解为最小相位部分和全通部分，通过迭代消除全通分量中的非最小相位零点*

### 模态传播函数分解

$$$H_{m,i} = H_{min,i} e^{-j\omega\tau_i}$$$

*ULM模型中模态传播函数的表示，将衰减和最小相位特性与纯延迟分离，是时延提取的理论基础*

### 群延迟平均修正量

$$$\Delta\tau = \text{mean}\left(-\frac{d\angle H_{ap}(j\omega)}{d\omega}\right)$$$

*所提方法的关键计算步骤，通过计算全通函数群延迟的平均值作为下一次迭代的时延修正量*



## 验证详情

- **验证方式**: 仿真对比验证：与数值拉普拉斯变换（NLT）参考解对比，以及与现有方法（Bode积分法、Golden Section搜索法）的对比分析
- **测试系统**: 1) 单输入单输出合成传递函数；2) 三根地下电缆系统（每根电缆包含4层导体：芯线、护套、铠装、大地回路）；3) 架空输电线路（aerial line）的EMT暂态响应
- **仿真工具**: 基于Vector Fitting (VF)算法实现有理拟合，使用MATLAB或类似数值计算环境；EMT仿真采用时间域仿真工具（与ULM模型兼容的仿真平台）
- **验证结果**: 所提APF方法在保证因果性和最小相位特性的前提下，实现了与Golden Section方法相当的拟合精度，但收敛速度更快（迭代次数更少）。在地下电缆和架空线路测试中，成功提取了正确的模态时延，避免了GS方法可能出现的超光速因果性违反问题
