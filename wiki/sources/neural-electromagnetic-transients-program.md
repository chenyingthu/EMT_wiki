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


