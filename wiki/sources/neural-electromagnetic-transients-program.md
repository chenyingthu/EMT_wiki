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

- 针对EMT仿真中的问题进行了研究

## 使用的方法

- [[物理信息神经网络-pinn|物理信息神经网络(PINN)]]
- [[无监督学习|无监督学习]]
- [[免数值积分方法|免数值积分方法]]
- [[梯形离散化公式嵌入|梯形离散化公式嵌入]]
- [[新型激活函数-act-mix|新型激活函数(Act mix)]]
- [[emtpnet神经网络架构|EMTPNet神经网络架构]]

## 涉及的模型


- [[neuemtp-神经电磁暂态程序|NeuEMTP(神经电磁暂态程序)]]
- [[emtpnet-面向emtp的神经网络|EMTPNet(面向EMTP的神经网络)]]
- [[电磁暂态系统模型|电磁暂态系统模型]]

## 相关主题

- [[电磁暂态仿真-emtp|电磁暂态仿真(EMTP)]]
- [[物理信息学习|物理信息学习]]
- [[免数值积分仿真|免数值积分仿真]]
- [[高保真轨迹生成|高保真轨迹生成]]
- [[宽频振荡模式仿真|宽频振荡模式仿真]]
- [[机器学习辅助仿真|机器学习辅助仿真]]

## 主要发现

—This paper devises a neural electromagnetic tran- sients program (NeuEMTP), an unsupervised, physics-informed learning approach to numerical-integration-free EMTP solutions
