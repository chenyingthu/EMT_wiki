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

- 改进了多端口频率相关网络等值方法，保证无源性和宽频精度
- 提出了一种改进的mmc建模方法，提高了EMT仿真效率和精度
- 提出无源性强制校正方法，确保频率相关模型的数值稳定性

## 使用的方法

- [[fdne-model|FDNE]]
- [[双层网络等值|双层网络等值]]
- [[局部无源性补偿|局部无源性补偿]]
- [[辅助有理函数|辅助有理函数]]
- [[扰动测试|扰动测试]]
- [[解析法|解析法]]
- [[机电暂态-电磁暂态混合仿真|机电暂态-电磁暂态混合仿真]]
- [[passivity-enforcement]]

## 涉及的模型

- [[mmc-model|MMC]]
- [[交直流电网|交直流电网]]
- [[fdne-model|FDNE]]
- [[fdne-model]]
- [[mmc-model]]

## 相关主题

- [[混合仿真|混合仿真]]
- [[无源性补偿|无源性补偿]]
- [[宽频动态建模|宽频动态建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[数值稳定性|数值稳定性]]
- [[网络等值|网络等值]]
- [[co-simulation]]

## 主要发现

— A frequency-dependent network equivalent (FDNE) is essential to capture wide-band frequency dynamics in the hybrid simulation of large-scale modular multi-level converter (MMC) based AC/DC grids
