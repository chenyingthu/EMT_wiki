---
title: "DQ Admittance Model Extraction for IBRs via Gaussian Pulse Excitation"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Systems;2023;38;3;10.1109/TPWRS.2023.3256119"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/DQ_Admittance_Model_Extraction_for_IBRs_via_Gaussian_Pulse_Excitation.pdf"]
---

# DQ Admittance Model Extraction for IBRs via Gaussian Pulse Excitation

**作者**: 
**年份**: 2023
**来源**: `13&14/files/DQ_Admittance_Model_Extraction_for_IBRs_via_Gaussian_Pulse_Excitation.pdf`

## 摘要

—While dq admittance models have shown to be very useful for stability analysis, extracting admittance models of inverter-based resources (IBRs) from the electromagnetic transient (EMT) simulation environment using frequency scans takes time. In this letter, a new perturbation method based on Gaussian pulses in combination with the system identiﬁcation algorithms shows great promise for parametric dq admittance model extraction. We present the dq admittance model extracting method for a type-4 wind turbine. Challenges in implementing Gaussian pulse excitation are also pointed out. The extracted dq admittance model via the new method shows to have a high matching degree with the measurements obtained from frequency scans. Index Terms—Inverter-based resources, admittance model, measurement. 

## 核心贡献


- 提出高斯脉冲激励法替代传统扫频，实现IBR参数化dq导纳模型快速提取。
- 结合系统辨识工具变量法，直接从时域数据辨识传递函数，避免非参数拟合步骤。
- 揭示高斯脉冲在EMT仿真中的实现难点，并通过扫频与调频信号验证模型高精度。


## 使用的方法


- [[高斯脉冲激励|高斯脉冲激励]]
- [[系统辨识|系统辨识]]
- [[工具变量法|工具变量法]]
- [[频率扫描法|频率扫描法]]
- [[线性调频信号注入|线性调频信号注入]]


## 涉及的模型


- [[type-4风电机组|Type-4风电机组]]
- [[dq导纳模型|dq导纳模型]]
- [[永磁同步发电机|永磁同步发电机]]
- [[网侧变流器|网侧变流器]]
- [[逆变器并网资源|逆变器并网资源]]


## 相关主题


- [[导纳模型提取|导纳模型提取]]
- [[稳定性分析|稳定性分析]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[系统辨识|系统辨识]]
- [[风电机组建模|风电机组建模]]


## 主要发现


- 高斯脉冲激励大幅缩短仿真时间，单次实验即可替代数百次传统扫频获取完整频响。
- 提取的参数化dq导纳模型与扫频测量数据高度吻合，验证了频域辨识精度。
- 工具变量法辨识的传递函数模型，相比状态空间预测误差法具有更高的训练数据匹配度。


