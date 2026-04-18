---
title: "Neural Electromagnetic Transients Program"
type: source
authors: ['未知']
year: 2022
journal: "2022 IEEE Power & Energy Society General Meeting (PESGM);2022; ; ;10.1109/PESGM48719.2022.9916869"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Neural Electromagnetic Transients Program.pdf"]
---

# Neural Electromagnetic Transients Program

**作者**: 
**年份**: 2022
**来源**: `27&28/Neural Electromagnetic Transients Program.pdf`

## 摘要

—This paper devises a neural electromagnetic tran- sients program (NeuEMTP), an unsupervised, physics-informed learning approach to numerical-integration-free EMTP solutions. The main contributions lie in: (1) a learning-based NeuEMTP architecture to simultaneously generate the electromagnetic states at all desired time steps, making the step-by-step integration unnecessary; (2) an unsupervised, physics-informed training pro- cedure to realize the NeuEMTP functionality without requiring any EMTP trajectories beforehand; (3) an EMTP-oriented- neural-network (EMTPNet) accompanied with a novel activation function Act mix to enable efﬁcient extrapolations of diverse oscillation modes under arbitrary frequencies. Case studies sys- tematically verify that NeuEMTP generates high-ﬁdelity EMTP traj

## 核心贡献


- 提出NeuEMTP架构，单次前向传播同步生成全时段状态，消除逐步积分
- 构建无监督物理信息训练流程，无需预生成轨迹数据即可完成模型训练
- 设计EMTPNet与Act_mix激活函数，实现任意频率多振荡模式高效外推


## 使用的方法


- [[物理信息神经网络-pinn|物理信息神经网络(PINN)]]
- [[无监督学习|无监督学习]]
- [[梯形积分离散化|梯形积分离散化]]
- [[参数化激活函数-act_mix|参数化激活函数(Act_mix)]]
- [[全时段同步前向传播|全时段同步前向传播]]


## 涉及的模型



- [[阻抗网络|阻抗网络]]
- [[rlc集中参数模型|RLC集中参数模型]]
- [[节点导纳矩阵|节点导纳矩阵]]


## 相关主题


- [[电磁暂态仿真-emtp|电磁暂态仿真(EMTP)]]
- [[物理信息深度学习|物理信息深度学习]]
- [[无监督学习|无监督学习]]
- [[高频电磁振荡建模|高频电磁振荡建模]]
- [[免数值积分仿真|免数值积分仿真]]
- [[数据驱动计算|数据驱动计算]]


## 主要发现


- 算法无需数值积分即可生成高保真电磁暂态轨迹，验证了方法有效性
- Act_mix函数能精准拟合基频与高频谐波叠加的复杂振荡波形
- 该方法在普通计算机上具备实现超实时电磁暂态仿真的潜力与加速优势



## 方法细节

### 方法概述

NeuEMTP采用物理信息神经网络(PINN)架构，将传统EMTP的梯形积分离散化规则嵌入深度学习框架。核心创新在于：①设计EMTPNet网络结构，通过单次前向传播同步生成全时段(t∈[0,T])的电磁状态量(v(t),i(t))，彻底消除传统逐步数值积分；②构建无监督训练范式，利用基尔霍夫定律和元件本构关系作为物理约束损失函数，无需预生成EMTP轨迹数据；③提出Act_mix参数化激活函数，通过可学习参数自适应捕获从工频到高频谐波的多样化振荡模式，解决传统激活函数拟合高频电磁振荡时的频谱偏差问题。

### 数学公式


**公式1**: $$$i(t) = gv(t) - i_h(t)$$$

*梯形离散化通用形式：将电感/电容的动态微分方程转化为等效电阻g与历史电流源i_h(t)的代数关系，是EMTP数值积分的基础*


**公式2**: $$$g_R = \frac{1}{R}, \quad i_{h,R}(t) = 0$$$

*电阻元件离散化：等效电导为电阻倒数，无历史电流项*


**公式3**: $$$g_L = \frac{\Delta t}{2L}, \quad i_{h,L}(t) = -g_L v_L(t-\Delta t) - i_L(t-\Delta t)$$$

*电感元件梯形离散化：等效电导与步长Δt成正比，历史电流项包含前一时刻电压和电流状态*


**公式4**: $$$g_C = \frac{2C}{\Delta t}, \quad i_{h,C}(t) = g_C v_C(t-\Delta t) + i_C(t-\Delta t)$$$

*电容元件梯形离散化：等效电导与步长Δt成反比，历史电流项体现电荷累积效应*


**公式5**: $$$Gv(t) = i_s(t) + i_h(t) := i(t)$$$

*系统级节点导纳方程：G为系统等效导纳矩阵，v(t)为节点电压向量，i_s为独立源注入电流，i_h为历史项等效电流源*


### 算法步骤

1. 建立物理约束方程：将RLC元件通过梯形规则(2a)-(2c)离散化，组装系统导纳矩阵G和历史电流项i_h，构建节点电压方程(3)作为网络训练的物理硬约束

2. 构建EMTPNet架构：设计包含Act_mix激活函数的多层前馈网络，输入层接收系统拓扑参数(R,L,C)、独立源特性及初始状态，输出层直接生成全时段电压轨迹{v(t_1),...,v(t_N)}

3. 定义无监督损失函数：构造残差损失L_res = ||G·v_pred(t) - i_s(t) - i_h(v_pred,t)||^2，其中i_h通过自动微分计算历史项，无需外部数据监督

4. 执行物理信息训练：利用Adam或L-BFGS优化器最小化物理残差损失，通过反向传播调整网络参数，使网络输出严格满足EMTP离散化物理定律

5. 全时段状态生成：训练完成后，对任意新工况执行单次前向传播，网络并行输出所有时间步的节点电压和支路电流，计算复杂度从O(N·M)降至O(1)（N为时间步数，M为系统规模）


### 关键参数

- **Δt**: 仿真步长，决定离散化精度与等效电导计算

- **g_L/g_C**: 电感/电容等效电导，分别与Δt成正比和反比

- **Act_mix参数**: 自适应混合激活函数的频率调制参数，用于多尺度振荡拟合

- **网络深度/宽度**: EMTPNet隐藏层配置，需足够表达高频谐波模式



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| RLC集中参数网络电磁暂态 | 验证NeuEMTP对基频叠加高频谐波振荡的拟合精度，网络单次推断生成全时段轨迹 | 相比传统逐步积分EMTP，消除累积数值误差，具备超实时仿真潜力(faster-than-real-time capability) |

| 多频率振荡模式外推 | 测试Act_mix激活函数对任意频率(包含高频电磁振荡)的 extrapolation 能力 | 传统ReLU/Tanh激活函数无法同时捕获工频与kHz级高频振荡，Act_mix实现多模式高效外推 |



## 量化发现

- 方法实现数值积分完全免除(numerical-integration-free)，训练过程无需任何预生成EMTP轨迹数据
- 单次前向传播即可生成全时段所有时间步的电磁状态，计算延迟从传统O(N)逐步积分降至常数级
- Act_mix激活函数支持 diverse oscillation modes under arbitrary frequencies 的高效外推
- 验证案例显示生成高保真(high-fidelity)EMTP轨迹，满足电力系统电磁暂态分析精度要求
- 在普通商用计算机(off-the-shelf computers)上展现出超实时(faster-than-real-time)仿真潜力


## 关键公式

### EMTP系统离散化代数方程

$$$Gv(t) = i_s(t) + i_h(t)$$$

*作为物理信息损失函数的核心约束，要求神经网络输出严格满足节点基尔霍夫电流定律和梯形离散化规则*

### 电感历史电流项

$$$i_{h,L}(t) = -\frac{\Delta t}{2L}v_L(t-\Delta t) - i_L(t-\Delta t)$$$

*体现梯形规则的时域递推特性，在NeuEMTP中通过神经网络自动微分计算，无需逐步存储历史状态*



## 验证详情

- **验证方式**: 对比验证与物理一致性检验
- **测试系统**: 包含电阻、电感、电容的集中参数阻抗网络，涵盖多种振荡模式
- **仿真工具**: 基于Python/PyTorch的NeuEMTP框架，对比基准为传统梯形积分EMTP算法
- **验证结果**: 系统验证表明，NeuEMTP在不使用任何数值积分的情况下，能够生成与传统EMTP相当的高保真轨迹，且通过无监督训练避免了海量数据生成负担，Act_mix函数有效解决了高频振荡拟合难题
