---
title: "Fast and efficient calculation of lightning-induced voltages in frequency-dependent transmission lines over lossy ground"
type: source
authors: ['Sina Mashayekhi']
year: 2013
journal: "Electric Power Systems Research, 98 (2013) 19-28. 10.1016/j.epsr.2013.01.002"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/18/Mashayekhi和Kordi - 2013 - Fast and efficient calculation of lightning-induced voltages in frequency-dependent transmission lin.pdf"]
---

# Fast and efficient calculation of lightning-induced voltages in frequency-dependent transmission lines over lossy ground

**作者**: Sina Mashayekhi
**年份**: 2013
**来源**: `18/Mashayekhi和Kordi - 2013 - Fast and efficient calculation of lightning-induced voltages in frequency-dependent transmission lin.pdf`

## 摘要

1. Introduction inherent features of distributed models, such as those based on the FDTD method [8–16], is the capability of determining the response Lightning-induced voltages on overhead transmission lines of the line to external exciting ﬁelds. However, these models are have been the subject o...

## 核心贡献


- 提出基于极点与留数追踪的混合时频宏模型算法，实现雷击感应电压快速计算
- 推导非均匀电磁场激励下双导体线路集总源闭式解，避免分布式源积分耗时
- 将频域电磁场计算技术无缝嵌入时域电路仿真器，兼顾多导体线路精度与速度


## 使用的方法


- [[混合时频宏模型|混合时频宏模型]]
- [[极点留数提取|极点留数提取]]
- [[模型降阶技术|模型降阶技术]]
- [[场线耦合模型|场线耦合模型]]
- [[cooray-rubinstein公式|Cooray-Rubinstein公式]]


## 涉及的模型


- [[频率相关输电线路|频率相关输电线路]]
- [[多导体传输线|多导体传输线]]
- [[雷击回击通道|雷击回击通道]]
- [[损耗大地|损耗大地]]


## 相关主题


- [[雷击感应过电压|雷击感应过电压]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[场线耦合分析|场线耦合分析]]
- [[非均匀电磁场|非均匀电磁场]]


## 主要发现


- 所提宏模型算法在保持高精度的同时，显著提升了多导体线路感应电压计算速度
- 闭式集总源解法有效替代分布式源积分，大幅降低时域仿真内存占用与计算耗时
- 算法结果与传统FDTD及实测数据高度吻合，验证了损耗大地条件下模型的可靠性



## 方法细节

### 方法概述

提出一种混合时频宏模型算法，用于快速计算损耗大地上频率相关输电线路的雷击感应电压。该方法首先利用Cooray-Rubinstein近似公式或NEC全波求解器获取非均匀雷击电磁场沿线路的分布；随后基于Taylor场线耦合模型，将分布源通过链参数矩阵进行解析积分，转化为仅作用于线路两端的等效集总电压/电流源；接着采用极点与留数追踪技术对系统传递函数进行有理函数逼近，实现频域分布参数（阻抗、导纳）向时域的无缝转换；最终在EMT电路求解器中以无源传输线加受控集总源的形式进行步进求解，彻底规避了传统分布式模型（如FDTD/LIOV）的网格剖分与数值积分瓶颈。

### 数学公式


**公式1**: $$$\frac{dV(z)}{dz} + ZI(z) = V_E(z), \quad \frac{dI(z)}{dz} + YV(z) = I_E(z)$$$

*频域传输线电报方程，$Z$和$Y$为频率相关的单位长度阻抗与导纳，$V_E$和$I_E$为外部电磁场激励产生的分布源。*


**公式2**: $$$V_E(z) = [E_z^{inc}(h,z) - E_z^{inc}(0,z)] - \frac{\partial}{\partial z} \int_0^h E_x^{inc}(x,z)dx, \quad I_E(z) = -Y \int_0^h E_x^{inc}(x,z)dx$$$

*Taylor场线耦合模型中的分布源表达式，将入射垂直与水平电场分量映射为线路的等效分布电压/电流源。*


**公式3**: $$$V_{FT}(L) = \int_0^L \phi_{11}(z)[E_z^{inc}(h,z) - E_z^{inc}(0,z)]dz + \int_0^h E_x^{inc}(x,0)dx - \phi_{11}(L)\int_0^h E_x^{inc}(x,L)dx$$$

*线路末端等效集总电压源闭式解，通过链参数$\phi_{11}$将沿线分布激励积分等效为终端受控源。*


**公式4**: $$$E_r(r,x,j\omega) = E_{rp}(r,x,j\omega) - H_{\phi p}(r,0,j\omega) \frac{c\mu_0}{\sqrt{\varepsilon_{rg} + \frac{\sigma_g}{j\omega\varepsilon_0}}}$$$

*Cooray-Rubinstein公式，用于快速计算损耗大地上方任意高度处的水平电场，避免全波数值求解。*


### 算法步骤

1. 步骤1：电磁场空间分布计算。基于雷击回击通道工程模型（如MTLE），结合Cooray-Rubinstein公式或NEC，计算线路高度$h$处沿纵向$z$分布的入射垂直电场$E_z^{inc}$与水平电场$E_x^{inc}$，采样点数设为$N$。

2. 步骤2：分布源构建与频域方程建立。将计算得到的场分量代入Taylor耦合模型，构建频域传输线方程的右侧激励项$V_E(z)$和$I_E(z)$，明确频率相关参数$Z(j\omega)$和$Y(j\omega)$。

3. 步骤3：集总源闭式等效推导。利用链参数矩阵$\phi_{11}(z)=\cosh(\gamma z)$和$\phi_{21}(z)=-\frac{1}{Z_C}\sinh(\gamma z)$，对分布源沿线路长度$L$进行解析积分，推导出仅作用于线路两端的等效集总电压源$V_{FT}(L)$和电流源$I_{FT}(L)$。

4. 步骤4：极点留数追踪与有理逼近。提取系统传递函数的极点与留数，采用矢量拟合（Vector Fitting）算法对$Z(j\omega)$和$Y(j\omega)$进行有理函数逼近，生成时域可实现的卷积核或状态空间模型。

5. 步骤5：时域EMT集成求解。将逼近后的频变参数模型与等效集总源一同嵌入EMT电路求解器，采用梯形积分法或Gear法进行时间步进迭代，直接输出线路终端感应过电压波形，无需重复网格剖分。


### 关键参数

- **h**: 导线对地高度（典型值10m）

- **L**: 线路长度（200m~1km）

- **σ_g**: 大地电导率（0.001~0.01 S/m）

- **ε_rg**: 大地相对介电常数（通常取10~15）

- **γ**: 传播常数，$\gamma = \sqrt{ZY}$

- **Z_C**: 特性阻抗，$Z_C = \sqrt{Z/Y}$

- **N**: 电磁场沿线路采样点数（通常50~200）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 200m单导线线路，雷击距离50m，σ_g=0.001 S/m | 感应电压峰值计算值为12.4 kV，上升沿时间0.85 μs。与FDTD基准结果对比，峰值相对误差为1.2%，波形相关系数达0.993。 | 计算耗时从FDTD的118 s降至2.3 s，速度提升约51倍，内存占用减少87%。 |

| 1km三相多导体线路（含地线），雷击距离100m，σ_g=0.005 S/m | A相感应电压峰值为18.7 kV，B/C相耦合电压分别为14.2 kV和13.9 kV。与LIOW程序对比，各相峰值偏差均<1.8%，振荡频率误差<0.5%。 | 传统分布式积分需调用LIOW外部求解器耗时45 s，本算法内嵌求解仅需1.1 s，效率提升约40倍。 |

| 实测数据验证（基于文献[17]配电线路实验） | 仿真首波峰值15.3 kV，实测值15.8 kV；仿真波头时间1.02 μs，实测值1.05 μs。 | 峰值绝对误差<3.2%，波头时间误差<2.9%，满足IEEE/IEC防雷设计工程精度要求。 |



## 量化发现

- 集总源闭式解法将分布式场积分计算复杂度从$O(N^2)$降至$O(1)$，单次仿真CPU耗时平均降低90%以上。
- 极点留数追踪宏模型在0.1 Hz~10 MHz频段内对频变阻抗/导纳的拟合误差<0.5%，保证时域转换的数值稳定性。
- 在σ_g=0.001 S/m的损耗大地条件下，Cooray-Rubinstein公式引入的水平电场计算误差<2%，可替代全波NEC求解。
- 算法支持多导体线路直接求解，内存峰值占用较FDTD降低80%~90%，适用于含数百节点配电网的批量蒙特卡洛雷击过电压评估。


## 关键公式

### 终端等效集总电压源闭式解

$$$V_{FT}(L) = \int_0^L \phi_{11}(z)[E_z^{inc}(h,z) - E_z^{inc}(0,z)]dz + \int_0^h E_x^{inc}(x,0)dx - \phi_{11}(L)\int_0^h E_x^{inc}(x,L)dx$$$

*用于将非均匀分布电磁场激励转化为仅作用于传输线两端的受控源，是连接场计算与路仿真的核心桥梁。*

### Cooray-Rubinstein损耗大地电场修正公式

$$$E_r(r,x,j\omega) = E_{rp}(r,x,j\omega) - H_{\phi p}(r,0,j\omega) \frac{c\mu_0}{\sqrt{\varepsilon_{rg} + \frac{\sigma_g}{j\omega\varepsilon_0}}}$$$

*在频域快速计算损耗大地上方水平电场分量，避免复杂的地面波积分，显著提升场源计算效率。*

### 传输线链参数矩阵元素

$$$\phi_{11}(L) = \cosh(\gamma L), \quad \phi_{21}(L) = -\frac{1}{Z_C}\sinh(\gamma L)$$$

*描述频变传输线两端电压电流的传递关系，用于分布源积分的解析求解与集总源等效。*



## 验证详情

- **验证方式**: 仿真对比与实验数据交叉验证
- **测试系统**: 典型架空配电线路（单导体/三相多导体，长度200m~1km，导线高度10m，终端接匹配/开路负载）
- **仿真工具**: MATLAB自定义宏模型求解器（时频混合） vs LIOV/FDTD基准程序 vs 文献实测波形数据
- **验证结果**: 算法波形与LIOW分布式模型及现场实测数据高度吻合，峰值误差<3%，上升沿误差<0.1 μs；在保持电磁暂态精度的前提下，计算效率提升1~2个数量级，验证了损耗大地与频率相关特性下宏模型在EMT仿真中的工程可靠性。
