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



## 方法细节

### 方法概述

本文提出一种基于多频率相量模型(MFPM)的动态同步相量估计算法。针对电力系统频率大范围偏移导致传统DFT和泰勒级数法精度下降的问题，该算法利用多个不同旋转频率的子相量对真实频率附近的动态信号进行建模。首先通过相邻数据窗的DFT结果计算相位差，获得粗估频率；随后根据粗估频率调用预先离线计算好的修正矩阵，利用最小二乘法对DFT频谱泄漏进行补偿，解算出各子相量参数；最后将子相量求和并进行相移运算，对齐至标准报告时刻。该方法在仅增加极少量在线运算量的前提下，有效克服了非同步采样误差，显著提升了动态工况下的相量测量精度。

### 数学公式


**公式1**: $$$X(t) = \sum_{m=-M}^{M} \sqrt{2} A_m e^{j2\pi (\hat{f}_0 + m\Delta f)t}$$$

*多频率相量模型表达式，利用中心频率$\hat{f}_0$及间隔$\Delta f$的$2M+1$个子相量拟合动态信号。*


**公式2**: $$$\hat{X}(l_{\text{mid\_p}}) = CA + DA^*$$$

*加窗DFT后的频域相量表达式，其中C和D为包含窗函数与旋转因子的系数矩阵，A为待求子相量矩阵。*


**公式3**: $$$A = (G^T G)^{-1} G^T \hat{X} = F\hat{X}$$$

*基于最小二乘法的子相量参数求解公式，矩阵F为离线预计算的修正矩阵，用于在线快速补偿DFT误差。*


**公式4**: $$$\hat{f}_0 = \text{round}\left( f_0 + \frac{\Delta\phi}{2\pi\Delta t} \right)$$$

*粗估频率计算公式，通过相邻数据窗DFT结果的相位差$\Delta\phi$与时间差$\Delta t$推导，并四舍五入取整。*


**公式5**: $$$\hat{A} = \sum_{m=-M}^{M} A_m e^{j\delta}, \quad \delta = 2\pi f \Delta\tau$$$

*报告时刻相移校正公式，将计算参考时刻$ttot$的相量结果平移至标准报告时刻$trep$。*


### 算法步骤

1. 初始化系统参数：设定标称频率$f_0$、子相量频率间隔$\Delta f$、数据窗数量$P$、子相量半宽$M$、单周波采样点数$N$及窗函数类型。

2. 对输入离散信号$x(n)$施加数据窗，以等效窗几何中心为参考点执行离散傅里叶变换(DFT)，获取各数据窗的频域相量估计值$\hat{X}(l_{\text{mid\_p}})$。

3. 计算相邻数据窗DFT结果的累加和$X_{L1}$与$X_{L2}$，求取其共轭乘积的相位角$\Delta\phi$，结合时间差$\Delta t$计算并四舍五入得到粗估频率$\hat{f}_0$。

4. 根据粗估频率$\hat{f}_0$和固定间隔$\Delta f$，从离线存储的矩阵表中调用对应的修正矩阵$F$，并分离其实部与虚部。

5. 将DFT结果向量$\hat{X}$与修正矩阵$F$相乘，利用最小二乘原理直接解算出包含$2M+1$个子相量的参数矩阵$A$。

6. 对矩阵$A$中的所有子相量元素进行复数求和，得到数据窗中心参考时刻$ttot$的总相量估计值。

7. 计算报告时刻$trep$与参考时刻$ttot$的时间差$\Delta\tau$，结合当前频率计算相移角$\delta$，对总相量执行复数旋转校正。

8. 输出校正后的同步相量幅值、相角及频率，完成单次测量周期。


### 关键参数

- **单周波采样点数_N**: 48

- **采样频率_fs**: 2400 Hz

- **子相量半宽_M**: 1

- **子相量总数**: 3

- **计算用数据窗数_P**: 1

- **实际滑动窗总数**: 7

- **子相量频率间隔_Δf**: 1 Hz

- **窗函数类型**: 矩形窗

- **离线矩阵存储策略**: 按整数粗估频率预计算并查表调用



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 静态频偏测试 | 基波频率在45Hz~55Hz范围内以1Hz步进固定偏移。MFPM算法在各频点下TVE均稳定在0.8%以内，幅值误差<0.004pu，相角误差<0.4°。 | 相比DPMA算法在45Hz/55Hz时TVE高达~8%且超标，MFPM精度提升约10倍，完全满足测量标准。 |

| 频率斜坡测试 | 频率以1Hz/s速率从45Hz线性斜坡至55Hz。MFPM算法在整个斜坡过程中TVE始终低于1%，误差曲线平滑无突变。 | DPMA算法在斜坡两端(45Hz/55Hz)误差急剧放大至8%以上，MFPM有效抑制了频偏累积误差。 |

| 功率振荡测试 | 在45Hz基频下叠加1~5Hz幅值/频率振荡。MFPM算法在5Hz振荡时TVE最大为0.6435%，幅值误差0.0021pu，相角误差0.3645°。 | DPMA算法在同等工况下TVE飙升至11.1224%，MFPM将误差降低至1/17，且CT-DFT算法TVE为0.7756%，MFPM仍具优势。 |

| 含噪工况测试 | 叠加60dB白噪声并设置-1Hz频偏。MFPM算法TVE波动极小，稳定在0.04%左右，幅值与相角误差曲线平稳。 | DPMA算法在噪声下误差剧烈波动，MFPM凭借多子相量信息融合展现出更强的抗噪鲁棒性。 |

| PSCAD/EMTDC系统仿真 | 120MW发电机经200km线路扰动产生功率振荡。MFPM算法在电压波峰/波谷处的幅值响应曲线光滑，紧密贴合真实波形。 | DPMA与CT-DFT算法在振荡峰值处出现明显毛刺与跟踪延迟，MFPM动态跟踪精度显著优于对比算法。 |



## 量化发现

- 在±5Hz静态频偏下，MFPM算法总相量误差(TVE)始终<0.8%，远优于DPMA算法的~8%。
- 在45Hz基频叠加5Hz振荡工况下，MFPM的TVE最大值为0.6435%，较DPMA的11.1224%降低约94%。
- 算法在线运算量仅比传统DPMA(K=2)增加7次加法与3次乘法，计算负担增加可忽略不计。
- 采用7个数据窗时，算法阶跃响应时间为52.44ms(幅值)和113.47ms(相角)，均满足IEEE C37.118标准规定的140ms限值。


## 关键公式

### 多频相量DFT映射方程

$$$\hat{X}(l_{\text{mid\_p}}) = CA + DA^*$$$

*用于建立加窗DFT频谱泄漏与多子相量参数之间的线性关系，是离线矩阵构建的基础。*

### 离线矩阵修正方程

$$$A = F\hat{X}$$$

*在线实时计算核心，通过查表获取矩阵F，直接对DFT结果进行最小二乘补偿，避免迭代求解。*

### 粗估频率计算方程

$$$\hat{f}_0 = \text{round}\left( f_0 + \frac{\Delta\phi}{2\pi\Delta t} \right)$$$

*在频偏较大时提供整数级频率初值，用于动态切换离线修正矩阵，保证模型中心频率贴近真实值。*



## 验证详情

- **验证方式**: 数值仿真与电磁暂态仿真对比验证
- **测试系统**: 自定义数学信号模型(静态/斜坡/振荡/噪声)及PSCAD/EMTDC搭建的120MW发电机-200km双回输电线路-无穷大系统模型
- **仿真工具**: MATLAB(算法实现与数值测试), PSCAD/EMTDC(电磁暂态波形生成)
- **验证结果**: 算法在频率大范围偏移、功率振荡及强噪声工况下均能保持高精度测量，TVE稳定在0.8%以内，响应时间符合IEEE C37.118标准。相比传统泰勒级数法与插值DFT法，在几乎不增加计算负担的前提下，显著提升了动态相量估计的鲁棒性与准确性，具备工程实用价值。
