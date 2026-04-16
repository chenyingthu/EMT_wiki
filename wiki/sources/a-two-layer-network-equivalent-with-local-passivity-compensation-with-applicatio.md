---
title: "A Two-layer Network Equivalent with Local Passivity Compensation with Applications to Hybrid Simulations of MMC based AC/DC Grids"
type: source
authors: ['Dewu Shu', 'Xiaorong Xie', 'Zheng Yan', 'Venkata Dinavahi', 'Yingdong Wei']
year: 2019
journal: ""
tags: ['mmc', 'network-equivalent']
created: "2026-04-13"
sources: ["EMT_Doc/04/TPWRS.2019.2918229.pdf.pdf"]
---

# A Two-layer Network Equivalent with Local Passivity Compensation with Applications to Hybrid Simulations of MMC based AC/DC Grids

**作者**: Dewu Shu, Xiaorong Xie, Zheng Yan 等
**年份**: 2019
**来源**: `04/TPWRS.2019.2918229.pdf.pdf`

## 摘要

— A frequency-dependent network equivalent (FDNE) is essential to capture wide-band frequency dynamics in the hybrid simulation of large-scale modular multi-level converter (MMC) based AC/DC grids. The FDNE model must be enforced to be passive, ensuring the numerical stability in time-domain simulations. However, existing passive enforcement techniques based on global optimization perturbations cannot guarantee convergence, accuracy and efficiency simultaneously. To address the issues, a two-layer FDNE (T-FDNE) model is developed for the AC grids. The two layers, namely, detailed layer and equivalent layer, have their admittances derived from perturbation test and analytical approach, respectively. The passivity of the T-FDNE model is guaranteed by the proposed local passivity compensation

## 核心贡献


- 提出双层频变网络等值模型，导纳分别由扰动测试与解析法推导
- 提出基于辅助有理函数的局部无源性补偿技术，避免全局优化提升效率
- 构建TS-EMT混合仿真接口，有效捕捉宽频及高频动态交互特性


## 使用的方法


- [[fdne-model|FDNE]]
- [[局部无源性补偿|局部无源性补偿]]
- [[辅助有理函数拟合|辅助有理函数拟合]]
- [[扰动测试法|扰动测试法]]
- [[ts-emt混合仿真|TS-EMT混合仿真]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[交流电网|交流电网]]
- [[fdne-model|FDNE]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[网络等值|网络等值]]
- [[无源性保证|无源性保证]]
- [[宽频动态建模|宽频动态建模]]
- [[交直流电网|交直流电网]]


## 主要发现


- 局部补偿技术无需全局优化，显著提升等值模型收敛速度、精度与计算效率
- 在中国实际交直流系统算例中验证了混合仿真方法的高精度与宽频动态捕捉能力


