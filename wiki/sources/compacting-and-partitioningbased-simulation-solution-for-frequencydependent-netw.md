---
title: "Compacting and partitioning‐based simulation solution for frequency‐dependent network equivalents in real‐time digital simulator"
type: source
authors: ['未知']
year: 2020
journal: "IET Generation Trans & Dist 2015.9:2526-2533"
tags: ['network-equivalent']
created: "2026-04-13"
sources: ["EMT_Doc/10/Hu 等 - 2015 - Compacting and partitioning-based simulation solution for frequency-dependent network equivalents in.pdf"]
---

# Compacting and partitioning‐based simulation solution for frequency‐dependent network equivalents in real‐time digital simulator

**作者**: 
**年份**: 2020
**来源**: `10/Hu 等 - 2015 - Compacting and partitioning-based simulation solution for frequency-dependent network equivalents in.pdf`

## 摘要

Rational models of frequency-dependent network equivalents (FDNEs) have been used in real-time digital simulator (RTDS) for power-system simulation. However, this can lead to a computational burden issue; the application of FDNEs may result in a loss of real-time simulation features because the computational cost of the FDNE component exceeds the limits of RTDS. The authors describe a solution that combines compacting and partitioning of the FDNEs, whereby the former reduces the redundancy in the mathematical model and the latter allows us to exploit parallel computer architectures. Then they describe the results of numerical simulations that demonstrate the effectiveness of the approach. Moreover, the proposed simulation solution is not limited to the applications of FDNEs in RTDS, it sol

## 核心贡献


- 提出基于奇异值分解的模型压缩方法，消除状态变量冗余以降低计算量
- 设计FDNE模块划分策略，拆分等效网络以适配RTDS并行计算架构
- 融合压缩与划分技术，解决大规模频变网络等值实时仿真算力瓶颈


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[奇异值分解|奇异值分解]]
- [[状态空间实现|状态空间实现]]
- [[梯形积分法|梯形积分法]]
- [[并行计算|并行计算]]
- [[模型压缩|模型压缩]]


## 涉及的模型


- [[fdne-model|FDNE]]
- [[有理函数模型|有理函数模型]]
- [[状态空间模型|状态空间模型]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[并行计算|并行计算]]
- [[频率相关建模|频率相关建模]]
- [[网络等值|网络等值]]
- [[计算加速|计算加速]]


## 主要发现


- 计算量公式证明瓶颈源于端口与极点数，压缩法有效消除冗余状态变量
- 划分策略将计算负载分散至多处理器，成功恢复系统实时仿真运行能力
- 数值实验验证组合方案大幅降低单步耗时，彻底解决RTDS局部过载问题



## 方法细节

### 方法概述

本文提出一种结合模型压缩（Compacting）与模块划分（Partitioning）的FDNE实时仿真加速方案。首先，利用矢量拟合技术获取外部网络的频变导纳矩阵有理函数模型，并转换为状态空间形式。针对传统实现中因极点重复排列导致的状态变量冗余，采用奇异值分解（SVD）对每个极点对应的留数矩阵进行秩分析。若矩阵秩$r$满足$r < (N+1)/2$，则通过SVD分解重构状态矩阵，剔除冗余状态变量，显著降低单步计算量。随后，基于有理函数部分分式可加性，将压缩后的FDNE按极点集拆分为$k$个独立子模块。各子模块被分配至RTDS的不同处理器核上并行计算历史电流$I_{his}$，最终通过节点导纳矩阵联立求解网络电压。该方案有效化解了大规模多端口FDNE在单处理器上的局部算力过载问题，在保持$10^{-5}$量级拟合精度的前提下恢复实时仿真特性。

### 数学公式


**公式1**: $$$O = 2nN^2 + N^2 + 2nN$$$

*FDNE单步仿真计算量（浮点乘法次数），$n$为极点数，$N$为三相端口数*


**公式2**: $$$R_k = USV^T$$$

*对第$k$个极点的留数矩阵进行奇异值分解，用于评估秩$r$并提取压缩所需的左右奇异向量*


**公式3**: $$$O_{\text{reduce}} = 2N^2 + 2N - 4rN$$$

*单个留数矩阵压缩后减少的计算量，$r$为矩阵秩*


**公式4**: $$$O_{\text{component}} = \frac{2nN^2}{k} + N^2 + \frac{2nN}{k}$$$

*将FDNE划分为$k$个并行子模块后，单个模块的计算量*


**公式5**: $$$I_{\text{his}} = C a x(t-\Delta t) + C l U(t-\Delta t)$$$

*梯形积分法推导的历史电流递推公式，用于EMTP每步迭代*


### 算法步骤

1. 基于原始网络频响数据，采用矢量拟合算法求解各导纳元素共享的极点$a_i$及对应的留数矩阵$R_i$，构建FDNE有理函数模型。

2. 将频域模型转换为状态空间形式$Y(s)=C(sE-A)^{-1}B+D$，并按极点分组重排矩阵结构（Format 2），使相同极点的状态变量集中。

3. 遍历所有$n$个留数矩阵$R_k$，设定SVD截断阈值$\lambda=0.9999$计算矩阵秩$r$。若$r < (N+1)/2$，则执行压缩：计算$R_k=USV^T$，替换为$R'_k=US$，$A'_k=\text{diag}(a_k,\dots,a_k)_{1\times r}$，$B'_k=V^T$，消除冗余状态变量。

4. 根据RTDS硬件资源（单机架最多支持18个并行组件），将压缩后的FDNE按极点/留数集合划分为$k$个子模块，确保每个子模块的计算量$O_{\text{component}}$低于实时阈值$O_{\text{lim}}$。

5. 将各子模块独立部署至RTDS的不同GPC处理器核上。在每个仿真步长$\Delta t$内，各核并行计算本模块的等效导纳$G_{eq}$与历史电流$I_{his}$。

6. 汇总所有子模块的$I_{his}$，结合外部网络注入电流，求解节点电压方程$U(t) = G_{\text{total}}^{-1}(I_{\text{inj}} - \sum I_{\text{his}})$，完成单步实时迭代。


### 关键参数

- **仿真步长**: 50 μs

- **实时算力阈值**: O_lim ≈ 3396 (基于GPC处理器)

- **SVD秩判定阈值**: λ = 0.9999

- **三相端口关系**: N = 3P (P为网络端口数)

- **单机架最大并行组件数**: 18



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 单端口FDNE (Y1/Y2, P=1, N=3) | 极点数n=30时计算量O=1080，n=46时O=1656，均远低于阈值，可直接实时仿真。RMS误差分别为1.2×10⁻⁵和9.8×10⁻⁶。 | 无需压缩/划分即可满足实时性，计算量仅为阈值的30%-48% |

| 双端口FDNE (Y4, P=2, N=6, n=46) | 压缩前O=3900（超限），RMS误差1.64×10⁻⁵。经SVD压缩28个低秩留数矩阵后，O降至3276，RMS误差微增至1.96×10⁻⁵。 | 仅通过压缩使计算量降低15.9%，成功恢复实时仿真能力 |

| 六端口FDNE (Y10, P=6, N=18, n=64) | 压缩前O=44410。压缩后O=26964（仍超限）。进一步划分为11个并行子模块，各模块计算量分布在1692~3204之间，全部低于阈值。 | 压缩+划分联合策略使单模块计算量降至原值的7.2%~12.0%，彻底解决多端口算力瓶颈 |



## 量化发现

- FDNE计算复杂度与端口数$N$呈平方关系，与极点数$n$呈线性关系，公式为$O = 2nN^2 + N^2 + 2nN$。
- 当留数矩阵秩$r < (N+1)/2$时，压缩操作可使单极点计算量从$2N^2+2N$降至$4rN$，最大降幅可达50%以上。
- Y4案例中，压缩使计算量从3900降至3276，精度损失仅$0.32\times 10^{-5}$，证明压缩不显著影响频响拟合精度。
- Y10案例中，划分11个子模块后，最大单模块计算量为3204，低于RTDS阈值3396，实现100%实时仿真成功率。
- RTDS单机架（4张GPC卡）最多可并行承载18个FDNE子模块，划分策略可线性扩展算力上限。


## 关键公式

### FDNE单步计算量公式

$$$O = 2nN^2 + N^2 + 2nN$$$

*用于评估FDNE模型在给定步长下是否超出RTDS单处理器实时算力阈值*

### 模型压缩计算量削减公式

$$$O_{\text{reduce}} = 2N^2 + 2N - 4rN$$$

*用于判断特定留数矩阵是否值得压缩，以及预测压缩后的算力收益*

### 并行划分后单模块计算量公式

$$$O_{\text{component}} = \frac{2nN^2}{k} + N^2 + \frac{2nN}{k}$$$

*用于指导FDNE模块划分数量$k$的设计，确保各子模块计算量低于硬件阈值*



## 验证详情

- **验证方式**: 基于RTDS硬件平台的数值仿真与对比分析
- **测试系统**: 改进型IEEE New England 39节点系统（设置不同边界提取1~6端口FDNE）
- **仿真工具**: RTDS (Real-Time Digital Simulator, GPC处理器架构), MATLAB (矢量拟合与SVD计算)
- **验证结果**: 在50μs步长下，传统方法在P≥2且n较大时必然失步。所提压缩+划分方案在保持RMS误差<2×10⁻⁵的前提下，成功将Y4~Y10等大规模FDNE的计算负载降至阈值以下，验证了算法在恢复实时性、维持高精度及适配并行架构方面的有效性。
