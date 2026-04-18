---
title: "Electromagnetic Modeling of Transformers in EMT-Type Software by a Circuit-Based Method"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Transactions on Power Delivery;2022;37;6;10.1109/TPWRD.2022.3177137"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/15/Electromagnetic modeling of transformers in EMT-type software by a circuit-based method_Pordanjani 等_2022.pdf"]
---

# Electromagnetic Modeling of Transformers in EMT-Type Software by a Circuit-Based Method

**作者**: 
**年份**: 2022
**来源**: `15/Electromagnetic modeling of transformers in EMT-type software by a circuit-based method_Pordanjani 等_2022.pdf`

## 摘要

—This work proposes a fully circuit-based method for modelling electrical transformers. This method not only offers the advantages of circuit-based methods and can be implemented in electromagnetic transient (EMT) type software, but it can also provide a detailed representation of transformers, comparable to the ﬁnite element method (FEM). The proposed method enables a detailed geometrical modelling, as well as representation of mag- netic ﬂux paths and consideration of iron core saturation. It can be implemented in EMT-type software to see the effect of power networks on transformers. In addition, the proposed method can represent internal faults in transformers. The problem is con- strained to a 2-D domain, which is often used in FEMs to represent the magnetic behavior of power equipment

## 核心贡献


- 提出分布式磁阻网络模型，在EMT软件中实现媲美有限元的变压器详细电磁建模。
- 采用网格化磁路离散方法，精确表征磁通路径分布、铁芯饱和及非均匀材料特性。
- 实现变压器内部匝间与对地故障的高效电路级仿真，兼顾计算精度与速度。


## 使用的方法


- [[磁路等效电路法|磁路等效电路法]]
- [[分布式磁阻网络模型|分布式磁阻网络模型]]
- [[空间网格离散|空间网格离散]]
- [[霍普金森类比|霍普金森类比]]
- [[有限元法验证|有限元法验证]]


## 涉及的模型


- [[变压器|变压器]]
- [[壳式变压器|壳式变压器]]
- [[三相双绕组变压器|三相双绕组变压器]]
- [[铁芯|铁芯]]
- [[绕组|绕组]]
- [[内部故障模型|内部故障模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[变压器详细建模|变压器详细建模]]
- [[铁芯饱和|铁芯饱和]]
- [[内部故障仿真|内部故障仿真]]
- [[磁路网络建模|磁路网络建模]]
- [[路场等效|路场等效]]


## 主要发现


- DRNM模型在正常运行与暂态工况下的仿真结果与有限元法高度吻合。
- 相比传统场路耦合方法，该纯电路模型大幅提升了计算效率且保持高精度。
- 模型能准确复现匝间及对地故障下的漏磁分布与铁芯饱和非线性特性。



## 方法细节

### 方法概述

提出一种完全基于电路的分布式磁阻网络模型（DRNM），用于在电磁暂态（EMT）软件中实现变压器的高精度电磁建模。该方法基于霍普金森类比（磁等效电路），将变压器二维截面空间离散为1000~3000个网格单元，每个单元包含四个正交方向的线性或非线性磁阻。通过安培定律与法拉第定律建立磁路与外部电气回路的耦合，采用Type-2 L-R互感元件（Mutator）实现电-磁双向能量交换。模型支持铁芯非线性饱和（分段线性B-H曲线）、非均匀材料分布、漏磁与边缘磁通路径的精确表征。针对三相三柱变压器，定义四种标准拓扑单元（A/B/C/D），并通过绕组分段策略实现匝间/对地内部故障建模，将故障区域视为独立子绕组并分配专属耦合系数，从而在纯电路架构下复现有限元（FEM）级别的场分布精度，同时避免传统场路耦合方法的跨域迭代瓶颈。

### 数学公式


**公式1**: $$$F = N_{MMF} I$$$

*磁动势源分布方程，将原副边绕组电流按空间位置映射至离散网格节点的磁动势源*


**公式2**: $$$E = -\frac{d}{dt} N_{EMF} \Phi$$$

*绕组感应电动势方程，基于法拉第定律将穿过网格单元的磁通量积分转化为绕组端电压*


**公式3**: $$$R = l/(\mu_0 S)$$$

*线性磁阻计算公式，l为磁路平均长度，S为截面积，μ0为真空磁导率*


**公式4**: $$$\mu_p = \frac{1}{\mu_0} \frac{B_p - B_{p-1}}{H_p - H_{p-1}}$$$

*铁芯非线性饱和特性的分段线性增量相对磁导率计算*


**公式5**: $$$\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ \mathcal{N} & 0 \end{bmatrix} \begin{bmatrix} i_1 \\ i_2 \end{bmatrix} + \begin{bmatrix} 0 & -\mathcal{N} \\ 0 & 0 \end{bmatrix} \frac{d}{dt} \begin{bmatrix} i_1 \\ i_2 \end{bmatrix}$$$

*Type-2 L-R互感元件（Mutator）状态方程，实现电回路(v1,i1)与磁回路(v2,i2)的实时耦合*


### 算法步骤

1. 步骤1（空间离散与索引）：根据目标精度将变压器二维截面从粗到细划分为网格，利用垂直对称性仅对左半部分建模，定义单元行列坐标(i,j)及四种标准拓扑类型(A/B/C/D)。

2. 步骤2（磁路拓扑连接-算法1）：遍历所有网格行(j=1~N)与列(i=1~2M)，按规则连接相邻单元的磁阻节点。内部节点执行(n_ij^(2)→n_(i+1)j^(4))与(n_ij^(3)→n_i(j+1)^(1))互联，边界节点按对称/开路条件消除外侧磁阻，完成全局磁路网络构建。

3. 步骤3（高压绕组电气连接-算法2）：确定HV绕组覆盖的行列范围(j2至j3, i1至2M-i1+1)，顺序连接互感元件电气节点(p_ij^(2)→p_(i+1)j^(1)等)，处理绕组端部闭合及对称部分的跨接，形成完整HV回路。

4. 步骤4（低压绕组电气连接-算法3）：采用与HV相同的拓扑逻辑，遍历LV绕组覆盖范围(j1至j4, i2至2M-i2+1)，建立LV侧互感元件的串联与闭合回路连接。

5. 步骤5（故障绕组重构-算法4）：针对匝间或对地故障，将故障绕组拆分为多个独立子绕组。遍历各子绕组对应的列索引集合，分别执行互感节点连接，在故障断点处接入故障阻抗，保持磁-电耦合拓扑的完整性与物理一致性。


### 关键参数

- **网格单元规模**: 1000~3000个（自适应细化至收敛）

- **标准单元类型**: Type-A（纯磁路）, Type-B（含HV互感）, Type-C（含HV/LV互感）, Type-D（含LV互感）

- **非线性建模**: 分段线性B-H曲线，斜率动态计算增量磁导率μp

- **耦合接口**: Type-2 L-R Mutator（耦合系数N）

- **故障扩展单元**: Type-B1/B2/C1（含独立耦合系数β', β'', β'''）

- **空间维度**: 2-D平面场（支持Double-2D扩展至3D近似）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 网格收敛性与空载特性验证 | 通过全局指标（蓝色）与局部指标（红色）收敛曲线验证网格细化过程。当单元数量达到1000~3000区间时，磁通分布与V-I特性曲线趋于稳定，与FEM基准解高度一致。 | 相比文献[13]传统拓扑模型（仅50~100节点），DRNM通过千级网格实现场级空间分辨率，且纯电路架构避免牛顿-拉夫逊迭代，计算效率显著提升。 |

| 三相变压器正常运行与暂态工况 | 在EMTP中部署DRNM模型，仿真三相三柱变压器额定工况下的励磁电流与暂态过程。铁芯局部饱和区域、漏磁通路径分布与ANSYS Maxwell 2-D FEM解完全吻合。 | 在保持FEM同等精度的前提下，模型可直接嵌入大型电力系统网络，支持断路器、避雷器等标准EMTP元件联合仿真，消除场路耦合数据交换延迟。 |

| 内部故障仿真（匝间/对地） | 将故障绕组拆分为独立子绕组并分配专属互感元件，精确捕捉故障区域的漏磁通路径畸变与局部饱和效应。故障电流波形、磁通重分布与FEM场解一致。 | 克服传统电路模型无法准确表征故障漏感与铁芯耦合的缺陷，实现故障位置、阻抗参数的灵活配置，计算规模可控且物理意义明确。 |



## 量化发现

- 模型网格规模在1000至3000个单元之间，远超传统拓扑模型（50~100节点），实现媲美有限元的空间分辨率。
- 采用分段线性B-H曲线表征铁芯饱和，增量磁导率μp通过相邻工作点(B,H)斜率解析计算，非线性迭代收敛稳定。
- Type-2 L-R互感元件实现电-磁双向耦合，耦合系数β_ij, γ_ij由绕组几何坐标(X,Y)与匝数(Np,Ns)严格推导，无经验拟合参数。
- 网格收敛性验证表明，全局与局部误差指标随网格细化单调下降，达到设定阈值后结果与FEM偏差可忽略。
- 纯电路架构避免了场路耦合中的跨域数据交换与双重非线性迭代，在大型网络暂态仿真中计算耗时显著降低，架构层面消除FEM求解器瓶颈。


## 关键公式

### 磁动势源分布方程

$$$F = N_{MMF} I$$$

*用于将绕组电流按空间位置映射到离散网格的磁动势源节点，建立电-磁激励接口*

### 绕组感应电动势方程

$$$E = -\frac{d}{dt} N_{EMF} \Phi$$$

*基于法拉第定律，将穿过各网格单元的磁通量积分转化为绕组端电压，完成磁路到电路的反向耦合*

### Type-2 L-R Mutator耦合方程

$$$\begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ \mathcal{N} & 0 \end{bmatrix} \begin{bmatrix} i_1 \\ i_2 \end{bmatrix} + \begin{bmatrix} 0 & -\mathcal{N} \\ 0 & 0 \end{bmatrix} \frac{d}{dt} \begin{bmatrix} i_1 \\ i_2 \end{bmatrix}$$$

*在EMT软件中实现电回路(v1,i1)与磁回路(v2,i2)的实时双向能量交换，替代传统场路耦合接口*

### 铁芯增量磁导率计算

$$$\mu_p = \frac{1}{\mu_0} \frac{B_p - B_{p-1}}{H_p - H_{p-1}}$$$

*处理铁芯非线性饱和特性，将B-H曲线离散为分段线性段，用于动态更新网格磁阻值*



## 验证详情

- **验证方式**: 与有限元法（FEM）进行对比验证，包含网格收敛性分析、空载V-I特性曲线比对、正常运行/暂态/内部故障工况下的磁通分布与电气量波形对比
- **测试系统**: 三相三柱式心式变压器（具体参数见原文Table I/II/III，包含额定容量、电压等级、绕组几何尺寸及铁芯材料B-H特性）
- **仿真工具**: EMTP（实现DRNM电路模型与暂态仿真）, ANSYS Electromagnetics/Maxwell（提供2-D FEM基准解）
- **验证结果**: DRNM模型在网格收敛后，其空载励磁特性、铁芯局部饱和分布、漏磁路径及内部故障电流波形均与ANSYS Maxwell FEM结果高度吻合。纯电路架构成功在EMT环境中复现了场级精度，同时避免了传统场路耦合方法的计算瓶颈与实现复杂性，验证了该方法在大型电力系统暂态仿真中的工程适用性与高精度。
