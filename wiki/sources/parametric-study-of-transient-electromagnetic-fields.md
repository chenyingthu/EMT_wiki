---
title: "Parametric Study of Transient Electromagnetic Fields"
type: source
authors: ['未知']
year: 2011
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/31/TPWRD.2011.2158592.pdf.pdf"]
---

# Parametric Study of Transient Electromagnetic Fields

**作者**: 
**年份**: 2011
**来源**: `31/TPWRD.2011.2158592.pdf.pdf`

## 摘要

—In this paper, the problem of calculating transient electromagnetic ﬁelds due to frequency-dependent multicon- ductor overhead transmission lines above lossy ground and underground cables buried in lossy soil is studied by decomposing the transmission line into a number of small segments. A modiﬁed ﬁnite-difference time-domain technique is applied to ﬁnd the current passing through each segment of the excited transmis- sion line. The contribution of each segment on the total electric and magnetic ﬁelds is calculated using two frequency-domain analytical techniques. The theoretical background and extent of validity of each technique are presented, and the results derived by applying each method are compared with those obtained using a commercial software package. The time-domain solution i

## 核心贡献


- 提出结合改进FDTD与偶极子分解的暂态电磁场计算方法精确计及频变参数与损耗大地
- 将复镜像理论与King近似公式引入多导体线路电磁场计算提升有限长线路建模精度
- 在PSCAD平台实现该算法支持导体弧垂与电缆屏蔽等复杂几何电气参数影响分析


## 使用的方法


- [[改进有限差分时域法-mfdtd|改进有限差分时域法(MFDTD)]]
- [[偶极子分解法|偶极子分解法]]
- [[复镜像理论|复镜像理论]]
- [[king近似公式|King近似公式]]
- [[傅里叶变换|傅里叶变换]]
- [[矩量法-mom|矩量法(MoM)]]


## 涉及的模型


- [[多导体架空输电线路|多导体架空输电线路]]
- [[地下电缆|地下电缆]]
- [[损耗大地模型|损耗大地模型]]
- [[频变线路参数模型|频变线路参数模型]]


## 相关主题


- [[暂态电磁场计算|暂态电磁场计算]]
- [[电磁干扰分析|电磁干扰分析]]
- [[频变参数建模|频变参数建模]]
- [[损耗大地效应|损耗大地效应]]
- [[导体弧垂影响|导体弧垂影响]]
- [[参数化研究|参数化研究]]


## 主要发现


- 忽略大地有限电导率与相对介电常数会导致暂态电磁场计算结果出现显著误差
- 导体弧垂变化会显著改变线路周围电磁场空间分布需在精确建模中予以考虑
- 复镜像理论与King近似公式计算结果与商业软件高度吻合验证了算法有效性



## 方法细节

### 方法概述

本文提出了一种计算有损大地上方有限长频变多导体架空线路及埋地电缆暂态电磁场的通用混合方法。该方法首先采用偶极子分解技术将传输线离散为N个小段（偶极子），要求每段长度远小于信号最小波长且观测点距离大于分段长度。然后利用改进有限差分时域法(MFDTD)在PSCAD/EMTDC平台上精确计算考虑频变参数和大地损耗的沿线电流分布。对于每个偶极子，采用两种频域解析技术——复镜像理论(Complex Image Theory)和King近似公式——分别计算其在有损半空间中的电磁场贡献，其中复镜像理论通过引入复深度$p$将有限导电大地等效为完美导电平面。最后通过傅里叶变换将频域场量转换至时域，叠加所有偶极子贡献得到总电磁场，并系统研究大地电导率、相对介电常数及导线弧垂等参数影响。

### 数学公式


**公式1**: $$$p = \frac{1}{\sqrt{j\omega\mu(\sigma + j\omega\varepsilon)}} = \frac{1}{\beta}$$$

*复镜像深度公式，表示将有限导电大地等效为位于复深度的完美导电平面，其中$\beta$为大地中的传播常数，$\sigma$为大地电导率，$\varepsilon$为大地介电常数*


**公式2**: $$$\beta = \sqrt{j\omega\mu(\sigma + j\omega\varepsilon)}$$$

*有损大地中的传播常数，用于计算电磁波在土壤中的衰减和相位变化*


**公式3**: $$$|p\beta_0| \ll 1$$$

*复镜像理论的适用条件，其中$\beta_0 = \omega\sqrt{\mu_0\varepsilon_0}$为空气中传播常数，要求复深度与空气中波数乘积远小于1*


**公式4**: $$$|\beta_0\rho| \geq 1$ 且 $|\beta_0\rho| \geq 10$$$

*King近似公式的适用条件，$\rho$为源点到观测点的径向距离，要求满足远场近似条件*


**公式5**: $$$v(t) = \frac{d}{dt}\left[\frac{\eta}{\tau_1/\tau_2}\cdot\frac{(t/\tau_1)^{10}}{1+(t/\tau_1)^{10}}\cdot e^{-t/\tau_2}\right]$$$

*Heidler函数导数形式的激励电压波形，用于产生宽频谱暂态信号，其中$\eta=0.93$, $\tau_1=0.5\mu s$, $\tau_2=2\mu s$，频谱覆盖至5 MHz*


### 算法步骤

1. 将多导体传输线沿纵向离散为N个短偶极子段（示例中1000m线路分为1000段，每段1m），确保每段长度远小于最小波长且观测点距离大于分段长度

2. 在PSCAD/EMTDC平台使用MFDTD技术求解Telegrapher方程，计算考虑频变集肤效应和大地损耗的沿线电流分布$I(x,t)$

3. 对每个偶极子段，通过傅里叶变换将时域电流转换为频域表示$I(x,\omega)$

4. 采用复镜像理论计算各偶极子在复深度$p$处的镜像贡献，或直接应用King近似公式求解Sommerfeld型积分，得到频域电场$\mathbf{E}(\omega)$和磁场$\mathbf{H}(\omega)$分量

5. 叠加所有偶极子段的矢量场贡献，得到总频域电磁场分布

6. 应用傅里叶逆变换将频域场量转换至时域，获得暂态电磁场波形$\mathbf{E}(t)$和$\mathbf{H}(t)$

7. 参数化扫描：系统改变大地电导率$\sigma$（0.001-0.1 S/m）、相对介电常数$\varepsilon_r$（5-10）及导线弧垂几何参数，重复步骤2-6分析参数敏感性


### 关键参数

- **line_segments**: 1000段（对于1000m线路）

- **segment_length**: 1 m

- **ground_conductivity**: 0.1 S/m（验证案例），参数研究范围0.001-0.1 S/m

- **ground_relative_permittivity**: 5（验证案例），典型值5-10

- **ground_permeability**: $\mu_r = 1$

- **observation_point**: $(0, 50, 2)$ m，即线路中点横向50m、高度2m处

- **frequency_range**: 0-10 MHz（干燥大地条件下复镜像理论有效范围），激励信号频谱覆盖至5 MHz

- **excitation_waveform**: Heidler函数导数，$\eta=0.93$, $\tau_1=0.5\mu s$, $\tau_2=2\mu s$

- **dipole_orientation**: x方向水平偶极子（架空线）或埋地垂直/水平偶极子（电缆）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 单根架空传输线验证案例 | 水平单导线沿x轴从-500m延伸至500m，离地高度未明确但通常为典型架空高度，分为1000个偶极子段。地面采用有损模型（$\sigma=0.1$ S/m, $\varepsilon_r=5$）。在观测点(0,50,2)m处计算电场分量$E_x$, $E_y$, $E_z$。结果显示三种方法（复镜像理论、King近似、NEC软件）计算的电场分量波形在幅值和相位上高度一致。 | 与基于矩量法(MoM)的商业软件NEC对比，电场各分量计算结果吻合良好，验证了复镜像理论和King近似在有限长线路建模中的等效精度 |

| 干燥大地条件下的频段适用性分析 | 对于$\sigma=0.001$ S/m和$\varepsilon_r=10$的干燥大地，复镜像理论在0-10 MHz频率范围内满足$|p\beta_0|\ll 1$条件，适用于电力系统暂态分析。King近似在低频段（<特定频率）违反$|\beta_0\rho|\geq 10$条件，导致横向电场分量计算出现偏差。 | 复镜像理论在宽频带（0-10 MHz）保持有效性，而King近似在低频段（具体阈值取决于距离$\rho$）精度下降 |



## 量化发现

- 对于典型干燥大地参数（$\sigma=0.001$ S/m, $\varepsilon_r=10$），复镜像理论的有效频率范围为0-10 MHz，覆盖电力系统开关暂态和雷电暂态的主要频谱
- King近似公式要求径向距离$\rho$满足$|\beta_0\rho|\geq 10$，在低频段（如kHz级）和近距离观测时可能不适用
- 导线离散数量：1000m线路分为1000段（每段1m），确保空间采样满足$\Delta x \ll \lambda_{min}$（最小波长条件）
- Heidler函数激励参数：幅值系数$\eta=0.93$，波前时间常数$\tau_1=0.5\mu s$，波尾时间常数$\tau_2=2\mu s$，产生的信号频谱上限达5 MHz
- 观测点位置：横向距离50m、高度2m（接近地面设备安装高度），该位置电磁场计算对大地电导率和介电常数变化敏感
- 忽略大地有限电导率（$\sigma$）和相对介电常数（$\varepsilon_r$）会导致暂态电磁场计算结果出现显著误差，具体偏差程度取决于频率和观测距离
- 导体弧垂变化会显著改变线路周围电磁场空间分布，在精确建模中必须考虑几何非线性而非简单直导线近似


## 关键公式

### 复镜像深度公式

$$$p = \frac{1}{\sqrt{j\omega\mu_0(\sigma + j\omega\varepsilon_0\varepsilon_r)}}$$$

*将有损大地等效为位于复深度$p$的完美导电平面，用于计算水平或垂直偶极子在有损半空间上方或内部的电磁场，避免直接计算困难的Sommerfeld积分*

### 偶极子叠加原理

$$$\mathbf{E}(\mathbf{r},\omega) = \sum_{k=1}^{N} \mathbf{E}_k(\mathbf{r},\omega; I_k)$$$

*将有限长线路的电磁场表示为N个偶极子段贡献的矢量叠加，其中每段电流$I_k$由MFDTD计算得到*



## 验证详情

- **验证方式**: 与商业电磁仿真软件NEC（Numerical Electromagnetics Code，基于矩量法MoM）的对比验证，以及不同解析方法（复镜像理论与King近似）之间的交叉验证
- **测试系统**: 单根水平架空导线，长度1000m（x轴方向-500m至+500m），均匀大地模型（电导率$\sigma=0.1$ S/m，相对介电常数$\varepsilon_r=5$），观测点位于线路中点横向50m、高度2m处
- **仿真工具**: PSCAD/EMTDC（用于MFDTD电流计算）、NEC-2（基于MoM的频域电磁场计算软件）、MATLAB（用于傅里叶变换和逆变换及数据处理）
- **验证结果**: 在观测点(0,50,2)m处，复镜像理论和King近似计算的电场各分量（$E_x$, $E_y$, $E_z$）时域波形与NEC计算结果高度吻合，验证了所提方法在处理频变参数、有损大地和有限长线路时的准确性。两种解析方法在有效频段内结果一致，但King近似在低频段因不满足远场条件而产生偏差，复镜像理论在0-10 MHz范围内保持稳健
