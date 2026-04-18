---
title: "Electromagnetic transient studies of large distribution systems using frequency domain modeling methods and network reduction techniques"
type: source
authors: ['Ghassan Bilal']
year: 2019
journal: "Electrical Power and Energy Systems, 110 (2019) 11-20. doi:10.1016/j.ijepes.2019.02.043"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/16/j.ijepes.2019.02.043.pdf.pdf"]
---

# Electromagnetic transient studies of large distribution systems using frequency domain modeling methods and network reduction techniques

**作者**: Ghassan Bilal
**年份**: 2019
**来源**: `16/j.ijepes.2019.02.043.pdf.pdf`

## 摘要

Electromagnetic transient studies of large distribution systems using frequency domain modeling methods and network reduction techniques Ghassan Bilala,b, Pablo Gomeza,⁎, Reynaldo Salcedoc, Juan M. Villanueva-Ramireza a Department of Electrical and Computer Engineering, Western Michigan University, 1903 W Michigan Ave., Kalamazoo, MI 49008, USA c Massachusetts Institute of Technology: Lincoln Laboratory, 244 Wood St, Lexington, MA 02421, USA

## 核心贡献


- 提出频域建模框架，避免时域有理拟合近似，适用于大规模多相配电网
- 结合Kron降阶与数值拉普拉斯变换，高效求解导纳矩阵并转换至时域
- 提供分布与集中参数线路及变压器频域建模指南，兼容多相节点分析


## 使用的方法


- [[频域分析法|频域分析法]]
- [[多相节点分析|多相节点分析]]
- [[kron降阶法|Kron降阶法]]
- [[数值拉普拉斯变换|数值拉普拉斯变换]]
- [[模态分解|模态分解]]


## 涉及的模型


- [[分布参数线路|分布参数线路]]
- [[集中参数线路|集中参数线路]]
- [[变压器|变压器]]
- [[断路器|断路器]]
- [[架空线|架空线]]
- [[地下电缆|地下电缆]]


## 相关主题


- [[电磁暂态分析|电磁暂态分析]]
- [[配电网建模|配电网建模]]
- [[频域建模|频域建模]]
- [[网络等值|网络等值]]
- [[故障暂态分析|故障暂态分析]]
- [[开关操作仿真|开关操作仿真]]


## 主要发现


- 在IEEE标准测试系统及千节点网络验证，稳态与暂态结果与ATP高度吻合
- 网络降阶大幅缩减矩阵规模与计算耗时，在保持精度同时提升大规模求解效率
- 频域方法避免卷积与有理拟合，计算更简便，为电力系统暂态评估提供高效方案



## 方法细节

### 方法概述

本文提出一种基于频域（FD）的大规模多相配电网电磁暂态（EMT）仿真框架。该方法首先在拉普拉斯域建立分布/集中参数线路、变压器及断路器的导纳模型，通过多相节点分析法构建全网导纳矩阵。为降低计算维度，采用Kron降阶技术消去非观测节点，仅保留激励与测量节点，得到简化导纳矩阵。针对开关操作，利用叠加原理与诺顿等效模型处理断路器开合。系统初始状态可通过频域稳态相量计算获得，再经数值拉普拉斯变换（NLT）转换至时域作为暂态初值。最终，通过逆NLT将频域节点电压高效反演为时域波形，避免了传统时域方法中的有理函数拟合与卷积运算，显著提升大规模网络求解效率。

### 数学公式


**公式1**: $$$\begin{bmatrix} I_0(s) \\ I_l(s) \end{bmatrix} = \begin{bmatrix} A & -B \\ -B & A \end{bmatrix} \begin{bmatrix} V_0(s) \\ V_l(s) \end{bmatrix}$$$

*多相分布参数线路二端口节点导纳方程，关联线路两端电压与电流向量*


**公式2**: $$$Y_{red}(s) = Y_{mn,mn}(s) - Y_{mn,rn}(s) Y_{rn,rn}^{-1}(s) Y_{rn,mn}(s)$$$

*Kron降阶公式，用于消去注入电流为零的冗余节点并生成等效导纳矩阵*


**公式3**: $$$f_n \approx \frac{e^{c n \Delta t}}{\pi} \text{Re} \left\{ \sum_{k=0}^{N-1} F_{2k+1} \sigma_{2k+1} e^{j[(2k+1)\Delta\omega](n\Delta t)} 2\Delta\omega \right\}$$$

*逆数值拉普拉斯变换离散公式，结合窗函数抑制吉布斯振荡，将频域解转换为时域波形*


**公式4**: $$$V_{CB\_cl} = \mathcal{L} \{ -v_{CB\_op}(t) u(t - t_c) \}$$$

*基于叠加原理的断路器闭合附加电压源模型，用于处理拓扑突变*


**公式5**: $$$Y = A^t Y_p A$$$

*三相变压器导纳矩阵构建公式，通过关联矩阵A将原始解耦导纳映射至实际节点*


### 算法步骤

1. 频域元件建模：根据分布参数/集中参数线路、变压器及断路器物理特性，推导其在拉普拉斯域的二端口导纳矩阵或诺顿等效模型，考虑频率相关参数（集肤效应与大地回流）。

2. 全网导纳矩阵组装：基于多相节点分析法，将各元件导纳子矩阵按拓扑连接关系逐元素叠加至全局节点导纳矩阵 $Y_{bus}(s)$ 中。

3. 网络降阶处理：将节点划分为观测节点（mn）与待消去节点（rn），利用Kron降阶公式计算等效导纳矩阵 $Y_{red}(s)$，大幅缩减矩阵规模与求逆计算量。

4. 初始状态设定：若需非零初值，先在额定频率下计算全网稳态相量电压，通过直接NLT转换至时域，再经拉普拉斯变换作为 $t>0$ 暂态扰动的初始条件。

5. 频域求解与开关事件处理：对指定故障或操作，利用叠加原理注入等效诺顿电流/电压源，求解 $V_{mn}(s) = Y_{red}^{-1}(s) I_{mn}(s)$，多次开关操作按时间顺序叠加响应。

6. 时域反演：采用逆数值拉普拉斯变换（NLT），结合阻尼因子 $c=2\Delta\omega$ 与窗函数 $\sigma(\omega)$ 抑制混叠与截断误差，将频域电压序列转换为时域波形。


### 关键参数

- **NLT采样点数**: 2048

- **ATP/EMTP积分步长**: 20 µs

- **基频采样率**: 833.333 点/周期

- **可捕获最高暂态频率**: 50 kHz

- **阻尼因子**: $c = 2\Delta\omega$

- **频率步长**: $\Delta\omega = \pi / T$

- **时间步长**: $\Delta t = T / N$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| IEEE 13节点系统单相接地故障 | 系统在30ms发生末端单相接地故障，断路器经约3个周期（75ms）动作切除故障。FD仿真波形与ATP/EMTP在故障前、故障中及故障恢复阶段高度重合，准确捕捉电压跌落与恢复轨迹。 | 与ATP/EMTP基准结果波形重叠度极高，无可见数值偏差，验证了暂态过程捕捉能力。 |

| IEEE 34节点系统全相合闸暂态 | 系统初始去磁，全相突然合闸。FD方法准确再现了合闸涌流与电压振荡过程，稳态与暂态响应均与参考工具一致。 | 在2048点离散采样下，时域波形与ATP/EMTP（20µs步长）结果高度吻合，证明频域方法无需有理拟合即可保持高精度。 |

| IEEE 123节点及1188节点合成系统 | 在大规模密集网状配电网中应用Kron降阶，成功完成对称/不对称故障及开关操作仿真，矩阵规模显著缩减，计算耗时大幅降低。 | Kron降阶将千节点级网络矩阵压缩至仅保留关键节点，有效避免时域方法中历史项卷积带来的计算瓶颈，实现大规模网络的高效求解。 |



## 量化发现

- NLT离散采样数固定为2048点，可精确捕获高达50 kHz的暂态频率成分
- ATP/EMTP对比基准采用20 µs积分步长（每周期833.333个采样点），FD仿真结果在稳态与暂态阶段均实现高度吻合
- 断路器操作机械延迟约3个周期（对应75ms），FD方法准确复现了故障切除后的电压恢复轨迹
- Kron降阶技术有效消除冗余节点，将大规模系统矩阵维度压缩至仅保留激励与测量节点，显著降低矩阵求逆与存储的计算负担
- 频域建模完全规避了时域方法所需的有理函数拟合与历史项卷积运算，代数方程求解直接性提升了大规模网络暂态评估的计算效率


## 关键公式

### Kron降阶等效导纳矩阵

$$$Y_{red}(s) = Y_{mn,mn}(s) - Y_{mn,rn}(s) Y_{rn,rn}^{-1}(s) Y_{rn,mn}(s)$$$

*用于大规模网络节点消去与矩阵降维，保留观测节点并消除内部节点*

### 逆数值拉普拉斯变换

$$$f_n \approx \frac{e^{c n \Delta t}}{\pi} \text{Re} \left\{ \sum_{k=0}^{N-1} F_{2k+1} \sigma_{2k+1} e^{j[(2k+1)\Delta\omega](n\Delta t)} 2\Delta\omega \right\}$$$

*用于将频域求解结果高精度反演至时域，结合窗函数抑制吉布斯振荡*

### 多相分布参数线路二端口导纳

$$$\begin{bmatrix} I_0(s) \\ I_l(s) \end{bmatrix} = \begin{bmatrix} A & -B \\ -B & A \end{bmatrix} \begin{bmatrix} V_0(s) \\ V_l(s) \end{bmatrix}$$$

*用于精确表征频率相关参数的架空线与地下电缆，支持多相不平衡分析*

### 断路器闭合附加电压源

$$$V_{CB\_cl} = \mathcal{L} \{ -v_{CB\_op}(t) u(t - t_c) \}$$$

*基于叠加原理处理开关操作引起的拓扑突变，实现时变开关事件的频域建模*



## 验证详情

- **验证方式**: 对比仿真验证（与成熟时域软件ATP/EMTP进行波形与数值对比）
- **测试系统**: IEEE 13节点、34节点、123节点标准测试馈线，以及1188节点密集网状城市配电网合成系统
- **仿真工具**: MATLAB（自主开发FD频域求解代码）与 ATP/EMTP（时域基准工具）
- **验证结果**: 在IEEE 13/34节点系统中，FD方法在稳态运行、全相合闸暂态及单相接地故障切除（30ms故障，75ms切除）等场景下，时域波形与ATP/EMTP结果高度一致。在123节点及1188节点大规模系统中，结合Kron降阶技术成功实现高效求解，验证了频域方法在避免有理拟合、处理多相不对称网络及大规模节点消去方面的精度与计算优势。
