---
title: "Dynamic Synchrophasor Estimator Based on Multi-frequency Phasor Model"
type: source
authors: ['CNKI']
year: 2023
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/Bai 等 - 2018 - Dynamic Synchrophasor Estimator Based on Multi-frequency Phasor Model; [基于多频率相量模型的动态同步相量测量算法].pdf"]
---

# Dynamic Synchrophasor Estimator Based on Multi-frequency Phasor Model

**作者**: CNKI
**年份**: 2023
**来源**: `13&14/files/Bai 等 - 2018 - Dynamic Synchrophasor Estimator Based on Multi-frequency Phasor Model; [基于多频率相量模型的动态同步相量测量算法].pdf`

## 摘要

When the power system was suffered from unbalance and fault, the fundamental frequency would deviate from the nominal frequency, and the measurement accuracy of synchrophasor estimator also would rapidly reduce. Therefore, a dynamic synchrophasor estimator was proposed based on multi-frequency phasor model. The multi-frequency phasor model was employed to reflect the effective information around real frequency, and to establish a phasor model including multi-frequency phasor. The accuracy phasor value could be obtained by estimating rough frequency, looking the matrix table calculated offline, revising the discrete Fourier transform (DFT) value and shifting phasor. Test results of both simulated signals and PSCAD/EMTDC generated signal show that the proposed estimator can provide accurate 

## 核心贡献


- 提出多频率相量模型，利用多子相量旋转频率描述真实频偏附近的有效信号信息。
- 结合粗估频率与离线矩阵查表修正DFT结果，实现动态工况下的高精度相量估计。


## 使用的方法


- [[多频率相量模型|多频率相量模型]]
- [[离散傅里叶变换-dft|离散傅里叶变换(DFT)]]
- [[最小二乘拟合|最小二乘拟合]]
- [[离线矩阵查表修正|离线矩阵查表修正]]
- [[相移运算|相移运算]]
- [[粗估频率计算|粗估频率计算]]


## 涉及的模型


- [[同步相量测量模型|同步相量测量模型]]
- [[pscad-emtdc测试信号模型|PSCAD/EMTDC测试信号模型]]


## 相关主题


- [[同步相量测量|同步相量测量]]
- [[频率偏移|频率偏移]]
- [[动态工况|动态工况]]
- [[离散傅里叶变换|离散傅里叶变换]]
- [[广域测量系统|广域测量系统]]
- [[pscad-emtdc仿真|PSCAD/EMTDC仿真]]


## 主要发现


- 在频率斜坡与功率振荡工况下，算法有效抑制频偏影响，总相量误差满足测量标准。
- 相比传统泰勒级数法，算法仅增加极少量运算量，显著提升动态相量估计精度。


