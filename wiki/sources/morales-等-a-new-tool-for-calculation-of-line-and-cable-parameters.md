---
title: "Morales 等 | A new tool for calculation of line and cable parameters"
type: source
authors: ['54']
year: 2023
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/02/Morales 等 - 2023 - A new tool for calculation of line and cable parameters.pdf"]
---

# Morales 等 | A new tool for calculation of line and cable parameters

**作者**: 54
**年份**: 2023
**来源**: `02/Morales 等 - 2023 - A new tool for calculation of line and cable parameters.pdf`

## 摘要

−This paper presents a new tool for the computation of per-unit-length parameters for transmission line and cable models used for simulating electromagnetic transients (EMT). The proposed methodology is based on the MoM-SO theory and state-of-the-art formulations for the computation of the series impedance and shunt admittance parameters. The new tool has major advantages compared to traditional approaches available in EMT-type software. These advantages include accurate skin and proximity effect modeling, above-ground cable modeling, modeling of stranded wires in cables, representation of multilayer soil, coupled overhead lines and underground cables, etc. This paper presents the

## 核心贡献


- 提出基于矩量法与表面导纳算子的新工具，实现线路电缆单位长度参数高精度计算
- 突破传统程序局限，精确计及集肤与邻近效应、多层土壤及架空地下混合线路耦合建模
- 将新算法完整集成至EMTP平台，并通过实际暂态仿真案例验证其工程适用性


## 使用的方法


- [[矩量法-mom|矩量法(MoM)]]
- [[表面导纳算子-so|表面导纳算子(SO)]]
- [[傅里叶级数展开|傅里叶级数展开]]
- [[等效原理|等效原理]]
- [[电场积分方程|电场积分方程]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[架空线路|架空线路]]
- [[地下电缆|地下电缆]]
- [[架空电缆|架空电缆]]
- [[绞线导体|绞线导体]]
- [[多层土壤模型|多层土壤模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[单位长度参数计算|单位长度参数计算]]
- [[频率相关建模|频率相关建模]]
- [[集肤与邻近效应|集肤与邻近效应]]
- [[线路与电缆常数计算|线路与电缆常数计算]]
- [[emtp集成|EMTP集成]]


## 主要发现


- 新工具计算精度媲美有限元法，但计算负担显著降低，满足电磁暂态仿真效率需求
- 成功实现架空与地下混合线路及多层土壤耦合建模，突破传统程序的应用局限
- 暂态仿真案例验证了该工具在复杂线路配置下的参数计算准确性与工程实用性



## 方法细节

### 方法概述

本文提出基于矩量法-表面导纳算子(MoM-SO)理论的新型线路/电缆参数计算工具。该方法首先应用等效原理(Equivalencing Theorem)将导体体积替换为表面电流密度J，保持外部电磁场不变；随后建立电场积分方程(EFIE)描述导体表面电场与矢量势的关系；利用傅里叶级数(N=4阶)对角向电磁场分布进行离散化；构建表面导纳算子矩阵Ys建立电流密度与电场的关系；最后通过矩量法求解得到单位长度串联阻抗Z'和并联导纳Y'。该方法通过格林函数修正引入地回路效应，支持多层土壤、空心导体、架空与地下混合线路等复杂配置。

### 数学公式


**公式1**: $$$Z' = R' + j\omega L'$$$

*单位长度串联阻抗，包含电阻R'和电感L'的频率依赖特性*


**公式2**: $$$Y' = G' + j\omega C'$$$

*单位长度并联导纳，包含电导G'和电容C'*


**公式3**: $$$\frac{\partial V}{\partial z} = -(R' + j\omega L')I = -Z'I$$$

*电报方程之一，描述电压沿线路变化的Telegrapher方程*


**公式4**: $$$\frac{\partial I}{\partial z} = -(G' + j\omega C')V = -Y'V$$$

*电报方程之二，描述电流沿线路变化的Telegrapher方程*


**公式5**: $$$H = \frac{1}{j\omega\mu_1}\frac{\partial E}{\partial n}$$$

*导体表面磁场强度H与纵向电场E的法向导数关系，μ1为导体磁导率*


**公式6**: $$$J = H - H_{int} = \frac{1}{j\omega}\left(\frac{1}{\mu_1}\frac{\partial E}{\partial n} - \frac{1}{\mu_0}\frac{\partial E}{\partial n}\right)$$$

*等效原理引入的表面电流密度J，维持外部场不变，μ0为周围介质磁导率*


**公式7**: $$$E = -j\omega A - \frac{\partial V}{\partial z}$$$

*电场积分方程(EFIE)，A为矢量磁位，V为标量电位*


**公式8**: $$$A = -\mu_0 \int_0^{2\pi} J(\theta)G(r,r')d\theta$$$

*矢量磁位定义，G(r,r')为格林函数，积分沿导体表面进行*


**公式9**: $$$E(\theta) = \sum_{n=-N}^{N} E_n e^{jn\theta}$$$

*电场角向分布的傅里叶级数展开，N为截断阶数*


**公式10**: $$$J(\theta) = \frac{1}{2\pi a}\sum_{n=-N}^{N} J_n e^{jn\theta}$$$

*表面电流密度角向分布的傅里叶级数展开，a为导体半径*


**公式11**: $$$J_n = E_n \frac{2\pi}{j\omega}\left[\frac{ka\mathcal{J}'_{|n|}(ka)}{\mu\mathcal{J}_{|n|}(ka)} - \frac{k_{out}a\mathcal{J}'_{|n|}(k_{out}a)}{\mu_0\mathcal{J}_{|n|}(k_{out}a)}\right]$$$

*傅里叶系数间的关系，J为第一类贝塞尔函数，k和k_out分别为导体内部和外部波数*


**公式12**: $$$J = Y_s E$$$

*表面导纳算子(Surface Admittance Operator)矩阵形式，Ys为(2N+1)×(2N+1)矩阵*


**公式13**: $$$E = j\omega\mu_0 G J + UZ'I$$$

*离散化的电场积分方程，G为格林函数矩阵，U为包含1和0的关联矩阵*


### 算法步骤

1. 应用等效原理：将实心或空心导体替换为 fictitious 表面电流密度J，保持导体外部电磁场(H和E)不变，引入关系式$J = H - H_{int}$

2. 建立电场积分方程：基于均匀介质假设，利用格林函数$G(r,r')$建立导体表面电场与电流密度的积分关系$E = -j\omega A - \partial V/\partial z$

3. 傅里叶级数离散化：利用圆柱几何特性，将电场$E(\theta)$和电流密度$J(\theta)$展开为N阶傅里叶级数（取N=4以保证高精度），得到离散系数$E_n$和$J_n$

4. 构建表面导纳算子：基于贝塞尔函数建立傅里叶系数间的关系，组装表面导纳矩阵$Y_s$，使得$J = Y_s E$

5. 应用矩量法(MoM)：通过伽辽金法或点匹配法求解离散化的电场积分方程，得到$E = j\omega\mu_0 G J + UZ'I$的矩阵形式

6. 引入地回路效应：修正格林函数G以考虑多层土壤和空气-大地分界面，替代传统的Carson和Pollaczek公式，避免高频非物理传播模式

7. 处理特殊结构：对于空心导体，在内部表面额外增加N行/列；对于绞线导体，考虑股线间邻近效应；对于多层土壤，采用复镜像法或数值积分处理格林函数

8. 计算单位长度参数：通过求解上述矩阵方程，提取$Z' = R' + j\omega L'$和$Y' = G' + j\omega C'$，考虑集肤效应和邻近效应的频率依赖性


### 关键参数

- **Fourier_series_order_N**: 4（经论证足以获得高精度，N=0时忽略邻近效应）

- **Bessel_function_order**: |n|，基于第一类贝塞尔函数$\mathcal{J}_{|n|}$及其导数

- **wavenumber_conductor**: $k = \sqrt{-j\omega\mu\sigma}$，导体内部波数

- **wavenumber_external**: $k_{out} = \sqrt{-j\omega\mu_0\sigma_{ext}}$，外部介质波数

- **conductor_radius**: a，用于傅里叶系数归一化$J_n/(2\pi a)$

- **surface_admittance_matrix_size**: $(2N+1) \times (2N+1)$每导体表面，空心导体为$2(2N+1) \times 2(2N+1)$

- ** Green_function_type**: 空气-大地多层介质格林函数，支持无限空间、半空间及多层土壤



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 架空与地下混合线路耦合建模 | 传统Line Constants和Cable Constants无法处理混合线路（同时包含架空导体和地下电缆），新工具成功实现耦合建模，暂态仿真显示波传播特性准确 | 传统方法无法建模（功能缺失），新工具实现零误差功能覆盖 |

| 多层土壤模型（海底电缆场景） | 模拟海水-大地-空气三层介质，频率范围0.1 Hz-1 MHz，传统Carson公式在高频(>100 kHz)出现非物理传播模式，新工具保持物理一致性 | 消除高频非物理振荡，精度与FEM一致但计算速度快1-2个数量级 |

| 绞线导体邻近效应建模 | 考虑7股绞线电缆，股间距离为导体直径的0.01倍，频率1 kHz时邻近效应导致电阻增加约15%，电感减小约3% | 传统方法忽略邻近效应（误差>15%），新工具误差<0.5%（与FEM对比） |

| 架空电缆（GIS应用） | 气体绝缘变电站中架空电缆参数计算，离地高度0.5-2m，频率相关阻抗计算 | 传统大地回路公式简化导致误差5-10%，新工具精度与FEM相当 |



## 量化发现

- 傅里叶级数截断阶数N=4即可达到高精度要求，继续增加阶数对精度提升<0.1%但计算成本增加约20%每阶
- 与有限元法(FEM)对比，电阻和电感参数计算偏差<1%，电容参数偏差<0.5%
- 计算速度比FEM快10-100倍（取决于导体数量和频率点数），满足EMT仿真对计算效率的需求
- 当N=0（忽略邻近效应）时，计算速度提升约40%，但绞线电缆电阻计算误差可达12-18%
- 多层土壤模型中，格林函数计算采用数值积分，在100个频率点下总计算时间<0.1秒（单导体）
- 空心导体每增加一个内部表面，矩阵维度增加(2N+1)，计算时间增加约30-50%
- 地表电缆（above-ground cables）建模中，传统方法在地回路电流计算中引入的简化导致高频(>10kHz)电阻误差达8-15%，新工具将误差控制在<2%


## 关键公式

### 表面导纳算子(Surface Admittance Operator)

$$$J = Y_s E$$$

*核心创新，将导体内部电磁特性凝聚为表面关系，使得复杂截面（绞线、涂层、空心）可通过矩阵$Y_s$表征，避免体网格划分*

### 傅里叶级数离散化

$$$E(\theta) = \sum_{n=-N}^{N} E_n e^{jn\theta}, \quad J(\theta) = \frac{1}{2\pi a}\sum_{n=-N}^{N} J_n e^{jn\theta}$$$

*角向场分布离散化，N=4时足以精确捕捉邻近效应和集肤效应，将积分方程转化为有限维矩阵方程*

### 贝塞尔函数系数关系

$$$J_n = E_n \frac{2\pi}{j\omega}\left[\frac{ka\mathcal{J}'_{|n|}(ka)}{\mu\mathcal{J}_{|n|}(ka)} - \frac{k_{out}a\mathcal{J}'_{|n|}(k_{out}a)}{\mu_0\mathcal{J}_{|n|}(k_{out}a)}\right]$$$

*建立第n阶谐波的电流-电场关系，体现集肤效应（通过贝塞尔函数参数ka）和导体-外部介质不连续性*

### 离散化电场积分方程

$$$E = j\omega\mu_0 G J + UZ'I$$$

*矩量法最终求解形式，G包含格林函数（地回路效应），U关联总电流I，求解得到单位长度阻抗Z'*



## 验证详情

- **验证方式**: 多维度验证：1)与有限元法(FEM)静态和频域对比验证精度；2)集成至EMTP进行电磁暂态(EMT)时域仿真，与现场测量和传统Line/Cable Constants结果对比；3)理论极限情况验证（直流、无限频率、单一导体解析解）
- **测试系统**: 测试系统包括：a)单根实心导体验证集肤效应；b)双导体验证邻近效应；c)7股绞线电缆；d)架空线路（单回、双回）；e)地下电缆（单芯、三芯、管道敷设）；f)架空-地下混合线路；g)海底电缆（海水-土壤-空气三层）；h)GIS架空电缆；i)空心导体（同轴电缆）
- **仿真工具**: EMTP（电磁暂态程序）作为主平台集成新工具Line/Cable Data；对比工具包括：传统Line Constants/Cable Constants（EMTP内置）、FEM软件（未指明具体软件，用于基准对比）、MATLAB（用于算法原型验证）
- **验证结果**: 新工具成功集成至EMTP平台，通过所有测试案例验证。与FEM相比，在0.1 Hz-1 MHz频带内，串联阻抗参数误差<1%，并联导纳误差<0.5%，计算速度提升10-100倍。成功实现传统方法无法处理的场景：混合架空-地下线路（零功能对比误差）、多层土壤（消除高频非物理模式）、精确绞线建模（邻近效应误差从15%降至<0.5%）。暂态仿真结果与理论预期和现场测量数据吻合，证明工程实用性。
