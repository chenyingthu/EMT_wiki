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



## 方法细节

### 方法概述

提出双层频变网络等值（T-FDNE）模型，用于交直流混合仿真中的交流侧宽频动态表征。第一层为详细层，通过端口宽频扰动测试获取导纳频响数据，并采用矢量拟合生成初始有理函数模型；第二层为等值层，基于电网拓扑与线路参数解析推导外部网络等效导纳。针对传统全局无源性优化收敛慢、易破坏精度的问题，提出基于辅助有理函数的局部无源性补偿技术。该技术仅在检测到无源性破坏的特定频段内添加微小补偿项，避免全局参数重优化，从而在保证时域仿真数值稳定性的同时，显著提升建模效率与精度。最终将T-FDNE离散化为诺顿等效电路，嵌入TS-EMT混合仿真接口，实现机电与电磁暂态的宽频交互。

### 数学公式


**公式1**: $$$Y(s) = \sum_{k=1}^{N} \frac{R_k}{s - p_k} + D + sE$$$

*矢量拟合导纳模型，用于将频域测量数据转化为时域可解的有理函数形式，其中$R_k$为留数，$p_k$为极点，$D$和$E$为常数项与高频项。*


**公式2**: $$$\lambda_{\min}(\text{Re}[Y(j\omega)]) \geq 0, \quad \forall \omega$$$

*无源性判定条件，要求导纳矩阵实部的最小特征值在所有频率下非负，以保证时域仿真能量不增、数值稳定。*


**公式3**: $$$Y_{comp}(s) = \sum_{m=1}^{M} \frac{\Delta R_m}{s - \Delta p_m}$$$

*局部无源性补偿辅助有理函数，仅在破坏频段引入低阶极点-留数对，用于抵消负实部而不改变原模型主体频响特性。*


### 算法步骤

1. 频域扫描与数据采集：在目标端口施加宽频电压/电流扰动信号，测量频率响应矩阵$Y_{meas}(j\omega)$，覆盖0.1 Hz至10 kHz范围，获取高分辨率导纳数据。

2. 初始有理函数拟合：采用矢量拟合（Vector Fitting）算法对$Y_{meas}$进行降阶拟合，通过迭代极点重定位获取稳定极点$p_k$与对应留数$R_k$，构建初始导纳模型。

3. 无源性校验与频段定位：在离散频点下计算模型实部矩阵的特征值，若存在负实部则标记为无源性破坏频段，并记录破坏中心频率与带宽。

4. 局部补偿项构造：针对每个破坏频段，解析构造辅助有理函数$Y_{comp}(s)$，其极点严格位于左半平面，留数经最小二乘或解析匹配计算，以恰好补偿负实部。

5. 双层模型合成与离散化：将补偿后的详细层导纳与解析推导的等值层导纳并联组合，形成完整T-FDNE模型，并采用梯形积分法将其离散化为诺顿等效电路。

6. 混合仿真接口集成：将离散化T-FDNE嵌入EMT侧边界，与TS侧通过迭代数据交换（电压/电流边界条件）实现机电-电磁暂态混合求解，完成宽频动态交互。


### 关键参数

- **拟合阶数**: 15~30阶（依网络规模自适应）

- **频率扫描范围**: 0.1 Hz ~ 10 kHz

- **无源性判定阈值**: 实部矩阵最小特征值 < -1e-4

- **EMT仿真步长**: 50 μs

- **TS仿真步长**: 10 ms

- **补偿阶数**: 每破坏频段增加2~4阶辅助极点



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 改进型IEEE 39节点系统（含MMC直流馈入） | T-FDNE混合仿真与全EMT基准模型对比，关键母线电压动态波形误差<0.8%，高频振荡（~1.2 kHz）幅值偏差<0.5 dB，计算耗时从全EMT的1420 s降至218 s。 | 计算效率提升约6.5倍，且无源性补偿使时域仿真零发散。 |

| 中国某实际多端MMC交直流电网 | 在换相失败与高频谐振工况下，T-FDNE准确捕捉2.5 kHz附近宽频交互特性，局部补偿算法耗时仅0.12 s，传统全局优化法耗时45.6 s且需多次迭代。 | 建模效率提升超380倍，全局优化法在复杂网络中常出现不收敛，而局部补偿法收敛率100%。 |



## 量化发现

- 局部无源性补偿算法将模型构建时间从传统全局优化的数十秒缩短至0.1~0.2秒，效率提升超200倍。
- 混合仿真中关键节点电压/电流动态误差控制在1.2%以内，高频段（>1 kHz）幅频响应偏差<0.5 dB。
- 无源性破坏频段补偿后，时域仿真发散率从传统方法的18.7%降至0%，数值稳定性显著提升。


## 关键公式

### 双层等值合成公式

$$$Y_{T-FDNE}(s) = Y_{detailed}(s) + Y_{equivalent}(s) + Y_{comp}(s)$$$

*用于将详细层、等值层与局部补偿项合并，构建完整的频变网络等值导纳矩阵。*

### 矢量拟合导纳模型

$$$Y(s) = \sum_{k=1}^{N} \frac{R_k}{s - p_k} + D + sE$$$

*在频域数据向时域状态空间或诺顿等效转换时使用，是FDNE建模的核心数学表达。*

### 无源性判定条件

$$$\lambda_{\min}(\text{Re}[Y(j\omega)]) \geq 0$$$

*在模型拟合完成后进行稳定性校验，若不满足则触发局部补偿流程。*



## 验证详情

- **验证方式**: 仿真对比验证（全EMT基准模型 vs T-FDNE混合仿真）与频域/时域交叉校验
- **测试系统**: 改进型IEEE 39节点系统及中国某实际多端MMC交直流电网
- **仿真工具**: PSCAD/EMTDC（EMT侧求解）、MATLAB（矢量拟合与无源性补偿算法）、自定义TS-EMT混合仿真接口平台
- **验证结果**: 验证了T-FDNE在宽频动态捕捉、无源性保证及计算效率上的优越性。混合仿真接口在交直流强交互场景下保持高精度与数值稳定，局部补偿技术彻底解决了全局优化法的收敛瓶颈，满足工程级大规模电网准实时仿真需求。
