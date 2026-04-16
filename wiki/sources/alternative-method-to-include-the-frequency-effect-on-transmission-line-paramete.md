---
title: "Alternative method to include the frequency-effect on transmission line parameters via state-space representation"
type: source
authors: ['Tainá', 'F.G.', 'Pascoalato']
year: 2023
journal: "International Journal of Electrical Power and Energy Systems, 155 (2024) 109375. doi:10.1016/j.ijepes.2023.109375"
tags: ['state-space', 'transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/06/Pascoalato 等 - 2024 - Alternative method to include the frequency-effect on transmission line parameters via state-space r.pdf"]
---

# Alternative method to include the frequency-effect on transmission line parameters via state-space representation

**作者**: Tainá, F.G., Pascoalato
**年份**: 2023
**来源**: `06/Pascoalato 等 - 2024 - Alternative method to include the frequency-effect on transmission line parameters via state-space r.pdf`

## 摘要

Electrical Power and Energy Systems 155 (2023) 109375 International Journal of Electrical Power and Energy Systems Alternative method to include the frequency-effect on transmission line Tainá F.G. Pascoalato a,∗, Anderson R.J. de Araújo b, Sérgio Kurokawa a, José Pissolato Filho b a Department of Electrical Engineering, São Paulo State University (UNESP), 56 South Brazil Ave, Ilha Solteira, 15385-000, São Paulo, Brazil

## 核心贡献


- 提出逐段独立求解π型电路状态方程的替代方法，大幅压缩状态矩阵维度
- 构建直接时域求解的频变集中参数模型，免除频时域转换与反变换计算
- 实现多相输电线路暂态响应的高效精确计算，兼顾模型精度与求解速度


## 使用的方法


- [[状态空间法|状态空间法]]
- [[集中参数模型|集中参数模型]]
- [[π型电路级联|π型电路级联]]
- [[频变参数拟合|频变参数拟合]]
- [[直接时域仿真|直接时域仿真]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[频变集中参数模型-fdlpm|频变集中参数模型(FDLPM)]]
- [[π型等效电路|π型等效电路]]
- [[rl并联支路|RL并联支路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[输电线路建模|输电线路建模]]
- [[雷击过电压分析|雷击过电压分析]]
- [[投切暂态分析|投切暂态分析]]


## 主要发现


- 替代方法计算的暂态电压电流波形与传统方法高度吻合，验证了模型精度
- 状态矩阵维度缩减使计算耗时降低230至300倍，显著提升仿真求解效率
- 该方法在单相与三相线路的投切及雷击工况下均保持优异数值稳定性


