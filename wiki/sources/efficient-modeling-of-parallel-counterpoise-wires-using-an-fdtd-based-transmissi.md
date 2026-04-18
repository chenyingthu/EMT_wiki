---
title: "Efficient modeling of parallel counterpoise wires using an FDTD-based transmission line approach"
type: source
authors: ['Naiara Duarte']
year: 2025
journal: "Electric Power Systems Research, 247 (2025) 111816. doi:10.1016/j.epsr.2025.111816"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/15/Efficient modeling of parallel counterpoise wires using an FDTD-based transmission line approach_Duarte 等_2025.pdf"]
---

# Efficient modeling of parallel counterpoise wires using an FDTD-based transmission line approach

**作者**: Naiara Duarte
**年份**: 2025
**来源**: `15/Efficient modeling of parallel counterpoise wires using an FDTD-based transmission line approach_Duarte 等_2025.pdf`

## 摘要

Efficient modeling of parallel counterpoise wires using an FDTD-based a Department of Electrical Engineering, Federal Center of Technological Education of Minas Gerais (CEFET-MG), Belo Horizonte, Brazil b Department of Electrical and Computer Engineering, Federal University of Bahia, Salvador, Brazil c EMC Laboratory, Swiss Federal Inst. Of Technology (EPFL), Lausanne, Switzerland This paper presents an efficient modeling approach for parallel counterpoise wires used in the tower-footing

## 核心贡献


- 提出基于FDTD的传输线求解方法，计及埋地平行导线阻抗与导纳的频率相关特性
- 建立平行接地极灵敏度分析框架，揭示有效长度与导线间距无关特性，简化工程设计


## 使用的方法


- [[有限差分时域法-fdtd|有限差分时域法(FDTD)]]
- [[传输线理论|传输线理论]]
- [[有理函数逼近|有理函数逼近]]
- [[全波电磁场模型验证|全波电磁场模型验证]]


## 涉及的模型


- [[平行接地极|平行接地极]]
- [[杆塔接地系统|杆塔接地系统]]
- [[埋地裸耦合导线|埋地裸耦合导线]]
- [[频率相关土壤模型|频率相关土壤模型]]


## 相关主题


- [[接地系统建模|接地系统建模]]
- [[雷电暂态分析|雷电暂态分析]]
- [[频率相关建模|频率相关建模]]
- [[地电位升分析|地电位升分析]]
- [[冲击阻抗评估|冲击阻抗评估]]


## 主要发现


- 模型与全波电磁场结果偏差低于5%，高电阻率下误差更小，验证了方法的高精度
- 增大导线间距使地电位升与冲击阻抗降低约10%至13%，但整体改善幅度相对有限
- 接地极有效长度与导线间距无关，该特性可简化不同走廊宽度下的接地系统设计



## 方法细节

### 方法概述

提出一种基于传输线理论（TL）与有限差分时域法（FDTD）相结合的并行接地极高效建模方法。该方法将平行埋地裸导线等效为多导体传输线，通过矩阵形式描述导线间的电磁耦合。为准确捕捉雷电暂态下的宽频特性，引入Alipio-Visacro土壤频变模型，利用矢量拟合技术（Vector Fitting）将土壤导纳和导体内部阻抗近似为有理函数（极点-留数形式），并通过逆拉普拉斯变换将其转化为时域卷积项。在FDTD求解过程中，采用递归卷积算法避免存储历史数据，显著提升计算效率。该方法直接在时域求解电报方程，无需频域-时域转换，适用于不同土壤电阻率、导线长度及间距的杆塔接地系统雷电暂态分析，并为后续引入土壤电离等非线性效应预留了接口。

### 数学公式


**公式1**: $$$\frac{\partial V(x, t)}{\partial x} = - L \frac{\partial I(x, t)}{\partial t} - \zeta_i(t) * \frac{\partial I(x, t)}{\partial t}$$$

*时域电报方程（电压），描述沿线电压梯度，包含导体内部频变阻抗的时域卷积项*


**公式2**: $$$\frac{\partial I(x, t)}{\partial x} = - G_0 V(x, t) - C_\infty \frac{\partial V(x, t)}{\partial t} - Y_{FD}(t) * \frac{\partial V(x, t)}{\partial t}$$$

*时域电报方程（电流），描述沿线电流梯度，包含土壤直流电导、高频电容及土壤频变导纳的卷积项*


**公式3**: $$$\kappa(s) = \sigma_{DC} + s\epsilon'_\infty + s \sum_{j=1}^{N} \frac{r_j}{s - p_j}$$$

*土壤导纳频变有理逼近公式，将Alipio-Visacro模型转化为拉普拉斯域极点-留数形式，便于时域递归卷积*


**公式4**: $$$R_S = \frac{1}{\pi \sigma_g} \left[ \ln\left(\sqrt{\frac{2l}{2hr}}\right) - 1 \right]$$$

*Sunde自电阻公式，用于计算单根平行埋地导线对远方大地的单位长度直流电阻*


### 算法步骤

1. 几何参数初始化与静态参数计算：根据导线长度$l$、埋深$h$、半径$r$及等效间距$D$，利用Sunde公式计算单位长度自/互电阻矩阵$R$，进而得到$G=R^{-1}$和$C=(\epsilon_g/\sigma_g)G$；采用King公式计算自/互电感矩阵$L$；计算导体内部阻抗矩阵$Z_i$。

2. 土壤频变特性建模：基于Alipio-Visacro模型获取土壤复导纳$\kappa(j\omega)$，使用矢量拟合技术将其在拉普拉斯域近似为$N=19$阶极点-留数形式，提取极点$p_j$和留数$r_j$。

3. 时域卷积核构建：对频变阻抗和导纳进行逆拉普拉斯变换，得到瞬态内部阻抗核$\zeta_i(t)=\sum b_j e^{\beta_j t}$和瞬态土壤导纳核$\eta_g(t)=\sum r_j e^{p_j t}$。

4. FDTD空间-时间离散：采用蛙跳格式（Leapfrog）对传输线方程进行离散，设定空间步长$\Delta x$与时间步长$\Delta t$，确保满足CFL稳定性条件。

5. 递归卷积迭代求解：在每一时间步更新电流$I$和电压$V$时，引入辅助变量$\Phi_{k,j}$和$\psi_{k,j}$递归计算历史卷积项，避免全量历史数据存储，实现高效时域推进。

6. 边界条件处理与暂态推进：在首端注入Heidler函数表征的雷电流源（等效为戴维南/诺顿电路），末端采用匹配或开路负载，按时间步迭代求解直至暂态过程结束。


### 关键参数

- **导线长度$l$**: 10~100 m

- **导线间距$D$**: 10, 20, 40 m

- **埋深$h$**: 0.8 m

- **导线直径**: 9.525 mm

- **土壤直流电阻率$\rho_{DC}$**: 250, 1000, 4000 $\Omega\cdot$m

- **雷电流峰值**: 31 kA

- **雷电流波头时间**: 3.8 $\mu$s

- **有理拟合阶数$N$**: 19



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 不同间距下的地电位升(GPR)分析 | 在250、1000、4000 $\Omega\cdot$m土壤电阻率下，导线长度固定为20m、40m、80m，间距从10m增至40m时，GPR峰值显著下降。 | 与全波电磁模型(HEM)对比，FDTD-TL模型GPR峰值偏差始终低于5%，且土壤电阻率越高偏差越小（高阻率下误差趋近于0）。 |

| 冲击阻抗($Z_P$)与有效长度分析 | 冲击阻抗随导线长度增加而下降，直至达到有效长度后趋于饱和。间距增大导致$Z_P$降低约10%~13%。 | FDTD-TL计算的$Z_P$曲线与HEM高度重合，验证了传输线近似在长导线场景下的有效性，计算耗时远低于全波模型。 |

| 冲击系数(IC)灵敏度分析 | 在有效长度前，$IC = Z_P/R_{LF} < 1$，且随土壤电阻率升高进一步降低。不同间距下的IC-长度曲线几乎完全重合。 | 首次揭示有效长度与导线间距无关的特性，简化了不同走廊宽度下的接地极设计流程，模型计算效率满足工程批量设计需求。 |



## 量化发现

- FDTD-TL模型与全波电磁模型(HEM)的GPR及冲击阻抗计算偏差始终低于5%，在高土壤电阻率(4000 $\Omega\cdot$m)下误差趋近于0。
- 导线间距从10m增加至40m（4倍），GPR峰值降低幅度分别为：250 $\Omega\cdot$m土壤下9.6%，1000 $\Omega\cdot$m下11.8%，4000 $\Omega\cdot$m下12.6%。
- 冲击阻抗($Z_P$)随间距增大而降低，整体改善幅度有限，约为10%至13%。
- 接地极有效长度($l_{EF}$)与导线间距$D$完全无关，该特性在不同土壤电阻率下均成立。
- 冲击系数$IC$在达到有效长度前恒小于1，且土壤电阻率越高，$IC$偏离1的程度越大。


## 关键公式

### 频变传输线电压方程

$$$\frac{\partial V(x, t)}{\partial x} = - L \frac{\partial I(x, t)}{\partial t} - \zeta_i(t) * \frac{\partial I(x, t)}{\partial t}$$$

*用于描述埋地多导体系统中电压沿线的空间变化，包含导体内部频变阻抗的时域卷积项*

### 频变传输线电流方程

$$$\frac{\partial I(x, t)}{\partial x} = - G_0 V(x, t) - C_\infty \frac{\partial V(x, t)}{\partial t} - Y_{FD}(t) * \frac{\partial V(x, t)}{\partial t}$$$

*描述电流沿线变化，包含土壤直流电导、高频电容及土壤频变导纳的卷积项*

### 土壤导纳有理逼近公式

$$$\kappa(s) = \sigma_{DC} + s\epsilon'_\infty + s \sum_{j=1}^{N} \frac{r_j}{s - p_j}$$$

*将Alipio-Visacro频变土壤模型转化为拉普拉斯域的极点-留数形式，便于FDTD时域递归卷积实现*

### Sunde自电阻公式

$$$R_S = \frac{1}{\pi \sigma_g} \left[ \ln\left(\sqrt{\frac{2l}{2hr}}\right) - 1 \right]$$$

*计算单根平行埋地导线对远方大地的单位长度直流电阻，用于构建导纳矩阵对角元*



## 验证详情

- **验证方式**: 与严格全波电磁场模型(Hybrid Electromagnetic Model, HEM)进行对比验证
- **测试系统**: 双平行埋地裸导线接地系统，导线长度10~100m，间距10/20/40m，埋深0.8m，直径9.525mm，土壤直流电阻率覆盖250~4000 $\Omega\cdot$m
- **仿真工具**: 自主开发的FDTD-TL时域求解器（基于递归卷积算法） vs HEM全波电磁仿真软件
- **验证结果**: 在全部测试工况下，FDTD-TL模型计算的GPR波形、峰值及冲击阻抗与HEM结果高度一致，最大相对误差<5%。随着土壤电阻率升高，模型偏差进一步减小至可忽略水平，充分验证了该传输线近似结合频变土壤建模方法在雷电暂态分析中的高精度与工程适用性。
